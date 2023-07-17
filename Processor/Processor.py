import time
import re
import cv2
import numpy as np
import imutils
import pyautogui

import pytesseract
import aircv as ac
from datetime import datetime

from pynput import keyboard

pytesseract.pytesseract.tesseract_cmd = r"tesseract\tesseract.exe"
pyautogui.FAILSAFE = False


# get time
# /////////////////////////////////////////////////////////////////
def getTime():
    now = datetime.now()
    formatted_time = now.strftime("%m-%d-%H-%M-%S")
    return formatted_time


class Processor:
    def __init__(self):

        self.runningFlag = True
        self.listen_quitKey()
        # 设置预设的预定值
        self.std_w = .0
        self.std_h = .0
        self.err_w = .0
        self.err_h = .0

        self.surface_area_list = []

        self.lineNum = 0
        self.posNum = 0
        self.curveNum = 30

        self.workSpacePath = ''
        self.resultIndex = 0  # 水平移动换了线后，这个index 就 +1

        # 默认是向上移动
        self.verticalMoveUpDirection = True

        # 对位置的标记 3-2-13：第三条线 第二个位置检测 第13个曲线
        self.currentLineIndex = 1
        self.currentPosIndex = 1
        self.currentCurveIndex = 1

        self.currentScreen = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
        # self.currentScreen = np.array(pyautogui.screenshot())[:, :, ::-1]
        # self.currentScreen=cv2.imread("resources4test/page01.png")
        self.screenWidth = pyautogui.size().width
        self.screenHeight = pyautogui.size().height
        self.recordFlag = False
        # the line region box
        self.lineRegionBottomRight = 0
        self.lineRegionTopLeft = 0
        # sharpness init
        self.sharpness = 0
        self.allButtonsType = {
            'focus_bar': 'resources/img/focusBar.png',
            'focus_up': 'resources/img/focusUp.png',
            'focus_down': 'resources/img/focusDown.png',
            'focus_up02': 'resources/img/focusUp02.png',
            'focus_down02': 'resources/img/focusDown02.png',

            'start_reconstruction_region': 'resources/img/startReconstructionRegion.png',
            'start_reconstruction': 'resources/img/startReconstruction.png',
            'show_reconstruction_result_region': 'resources/img/showReconstructionResultRegion.png',
            'show_reconstruction_result': 'resources/img/showReconstructionResult.png',

            'reconstruction_result_region': 'resources/img/reconstructionResultRegion.png',
            '3d_show': 'resources/img/3dShow.png',

            'show_bar': 'resources/img/showBar.png',
            'select_contour': 'resources/img/selectContour.png',

            'contour_menu': 'resources/img/contourMenu.png',
            'contour_parallel_line': 'resources/img/contourParallelLine.png',
            'clicked': 'resources/img/clicked.png',
            'not_clicked': 'resources/img/notClicked.png',
            'average_contour_font': 'resources/img/averageContourFont.png',
            'close_region': 'resources/img/closeRegion.png',
            'close': 'resources/img/close.png',
            'quit_region': 'resources/img/quitRegion.png',
            'yes_button': 'resources/img/yesButton.png',

            'back_first_page_region': 'resources/img/backFirstPageRegion.png',
            'back_first_page': 'resources/img/backFirstPage.png',

            'first_page': 'resources/img/firstPage.png',
            "adjust_height_region": 'resources/img/adjustHeightRegion.png',
            'adjust_height_cursor': 'resources/img/adjustHeightCursor.png',
            'measure_width': 'resources/img/measureWidth.png',
            'measure_height': 'resources/img/measureHeight.png',
            'height_or_color': "resources/img/heightOrColor.png",
            'click_button01': 'resources/img/clickButton01.png',
            'click_button02': 'resources/img/clickButton02.png',
            'bottom_menu': 'resources/img/bottomMenu.png',
            'save_file': 'resources/img/saveFile.png',

            'show_img': 'resources/img/show_img.png',
            'measure': 'resources/img/measure.png',
            "task_bar": 'resources/img/taskBar.png',
            "panel_measurement": 'resources/img/panelMeasurement.png',
            'panel_measurement_button': 'resources/img/panelMeasurementButton.png',
            'measurement_menu': 'resources/img/measurementMenu.png',
            'parallel_line': 'resources/img/parallelLine.png',
        }

    def on_release(self, key):
        """定义释放时候的响应"""
        if key == keyboard.Key.esc:
            self.runningFlag = False

    def listen_quitKey(self):
        listener = keyboard.Listener(
            on_release=self.on_release
        )
        listener.start()

    def findButton(self, buttonRegion, button, getOut=None):
        # currentScreenshot=cv2.imread('resources4test/page01.png')
        currentScreen = self.currentScreen
        region_template = cv2.imread(self.allButtonsType[buttonRegion])
        button_template = cv2.imread(self.allButtonsType[button])
        region_res = ac.find_template(currentScreen,
                                      region_template,
                                      threshold=0.8)
        if region_res is not None:
            region_top_left = region_res['rectangle'][0]
            region_bottom_right = region_res['rectangle'][3]
            getOut(f"find {buttonRegion}:in {region_top_left},{region_bottom_right}")
            selectedScreen = currentScreen[
                             region_top_left[1]:region_bottom_right[1],
                             region_top_left[0]:region_bottom_right[0]
                             ]
            button_res = ac.find_template(selectedScreen,
                                          button_template,
                                          threshold=0.8)
            if button_res is not None:
                button_pos = button_res['result']
                getOut(f"button pos:{button_pos}")
                abs_button_pos = [button_pos[0] + region_top_left[0],
                                  button_pos[1] + region_top_left[1]]
                getOut(f"abs button pos:{abs_button_pos}")
                return True, abs_button_pos
            else:
                getOut(f"cannot find button:{button}")
                return False, None
        else:
            getOut(f"cannot find button region: {buttonRegion}")
            return False, None

    def click(self, buttonRegion, button, getOut=None):
        # if self.runningFlag:
        # try:
        # self.currentScreen = cv2.imread('resources4test/10.png')
        if not self.runningFlag:
            raise Exception("中途停止", )
        self.screenshot()
        ret, res = self.findButton(buttonRegion, button, getOut=getOut)
        if ret:
            getOut(f"find btn res:{res}")
            pyautogui.moveTo(res)
            pyautogui.click()
            return f"{res}"
        else:
            getOut(f"click failed:{res}")
            return res

    def ifClicked(self, getOut=None):
        # try:  # 主要用于检测第三页的平均轮廓是否已经选中
        self.screenshot()
        currentScreen = self.currentScreen
        roi_template = cv2.imread(self.allButtonsType['average_contour_font'])
        click_template_list = [
            self.allButtonsType['not_clicked'],
            self.allButtonsType['clicked']
        ]
        roi_res = ac.find_template(currentScreen, roi_template, threshold=0.8)
        # 根据这个区域得到框的区域
        if roi_res is not None:
            box_top_left = [roi_res['rectangle'][0][0] - 20,
                            roi_res['rectangle'][0][1]]
            box_bottom_right = [roi_res['rectangle'][0][0],
                                roi_res['rectangle'][0][1] + 20]
            getOut(f"find box region:{box_top_left},{box_bottom_right}")
            box_region = currentScreen[
                         box_top_left[1]:box_bottom_right[1],
                         box_top_left[0]:box_bottom_right[0]
                         ]
            index = 0
            while index < 2:
                # 对框进行一个匹配
                click_template = cv2.imread(click_template_list[index])
                click_res = ac.find_template(box_region, click_template, threshold=0.9)
                if click_res is not None:
                    click_pos = [
                        click_res['result'][0] + box_top_left[0],
                        click_res['result'][1] + box_top_left[1]
                    ]
                    int_click_pos = [int(pos) for pos in click_pos]
                    getOut(f"find click box:{int_click_pos}")
                    break
                else:
                    index += 1

            if index == 0:
                getOut(f"not click yet")
                return True, False, int_click_pos
            elif index == 1:
                getOut(f"clicked")
                return True, True, int_click_pos
            else:
                getOut(f"cannot recognize click box")
                return True, None, None
        else:
            getOut('cannot find the region')
            return False, None, None

    def screenshot(self):
        self.currentScreen = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)

    def recordScreen(self, fileName):
        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        fps = 30
        print(fileName)
        out = cv2.VideoWriter(f"{self.workSpacePath}/开发者记录/{fileName}.mp4", fourcc, fps,
                              (self.screenWidth, self.screenHeight))
        while True:
            time_elapsed = time.time()
            img = pyautogui.screenshot()
            if time_elapsed > 1.0 / fps:
                frame = np.array(img)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                out.write(frame)
                if self.recordFlag is False:  # or self.runningFlag is False:
                    break
            cv2.waitKey(1)
        cv2.destroyAllWindows()
        out.release()

    def findLine(self, getOut=None):

        self.screenshot()
        # self.currentScreen = cv2.imread('resources4test02/line/1.bmp')
        img = self.currentScreen
        imgSelected = img[:, :1440]

        imgHSV = cv2.cvtColor(imgSelected, cv2.COLOR_BGR2HSV)
        # hsv_low = np.array([0, 0, 86])
        # hsv_high = np.array([108, 255, 255])
        hsv_low = np.array([0, 0, 36])
        hsv_high = np.array([120, 255, 255])
        mask = cv2.inRange(imgHSV, hsv_low, hsv_high)

        lineRegion = cv2.bitwise_and(imgSelected, imgSelected, mask=mask)

        grayLine = cv2.cvtColor(lineRegion, cv2.COLOR_BGR2GRAY)
        # x_grad = cv2.Sobel(grayLine, cv2.CV_32F, dx=1, dy=0, ksize=-1)
        # y_grad = cv2.Sobel(grayLine, cv2.CV_32F, dx=0, dy=1, ksize=-1)
        # gradLine = cv2.subtract(x_grad, y_grad)
        # gradLine = cv2.convertScaleAbs(gradLine)

        blurredLine = cv2.blur(grayLine, (5, 5))
        _, thresholdLine = cv2.threshold(blurredLine, 100, 255, cv2.THRESH_BINARY)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 7))
        closedLine = cv2.morphologyEx(thresholdLine, cv2.MORPH_CLOSE, kernel)

        lineContours = cv2.findContours(closedLine, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        lineCnts = imutils.grab_contours(lineContours)
        lineContour = sorted(lineCnts, key=cv2.contourArea, reverse=True)[0]
        lineRect = cv2.minAreaRect(lineContour)
        boxPoints = cv2.boxPoints(lineRect)
        intBoxPoints = np.intp(boxPoints)

        getOut(f"intBoxPoints:{intBoxPoints}")

        top_left = [min(point[0] for point in intBoxPoints), min(point[1] for point in intBoxPoints)]
        bottom_right = [max(point[0] for point in intBoxPoints), max(point[1] for point in intBoxPoints)]
        top_left[0] = max(0, top_left[0])
        top_left[1] = min(1080, top_left[1])
        bottom_right[0] = max(0, bottom_right[0])
        bottom_right[1] = min(1080, bottom_right[1])
        getOut(f"top left is {top_left}")
        getOut(f"bottom right is {bottom_right}")

        w_diff = bottom_right[0] - top_left[0]
        h_diff = bottom_right[1] - top_left[1]

        if w_diff + h_diff <= 1080:
            getOut(f"cannot find the line")
            return top_left, bottom_right, 0
        elif top_left[0] <= 50:
            getOut(f"the line located at the left edge")
            getOut(f"should move it more")
            return top_left, bottom_right, 0
        elif w_diff < 80 or w_diff > 600 or h_diff < 900:
            getOut(f"maybe it's the cross point")
            getOut(f"should move it more")
            return top_left, bottom_right, 0
        else:
            self.lineRegionTopLeft = top_left
            self.lineRegionBottomRight = bottom_right
            getOut(f"find the line")
            getOut(f"current top left is: {top_left}, bottom right is: {bottom_right}")
            cv2.rectangle(img, top_left, bottom_right, (0, 255, 255), 3)
            # cv2.imshow('1',img)
            cv2.imwrite(f"{self.workSpacePath}/开发者记录/findLineTestResult.jpg", img)
            getOut(f"current line region pic saved")
            return top_left, bottom_right, 1

    def getLineSharpness(self, getOut=None):
        self.screenshot()
        # 计算银线对应region的清晰度
        try:
            if self.lineRegionTopLeft == 0:
                getOut(f"please find the line firstly")
                return f"please find the line firstly"
            else:
                selectedRegion = self.currentScreen[
                                 self.lineRegionTopLeft[1]: self.lineRegionBottomRight[1],
                                 self.lineRegionTopLeft[0]: self.lineRegionBottomRight[0]
                                 ]
                selectedRegion01 = self.currentScreen[
                                   self.lineRegionTopLeft[1]:self.lineRegionBottomRight[1],
                                   self.lineRegionTopLeft[0]:self.lineRegionTopLeft[0] + 3 * int(
                                       (self.lineRegionBottomRight[0] - self.lineRegionTopLeft[0]) / 8)
                                   ]
                selectedRegion02 = self.currentScreen[
                                   self.lineRegionTopLeft[1]:self.lineRegionBottomRight[1],
                                   self.lineRegionTopLeft[0] + 5 * int(
                                       (self.lineRegionBottomRight[0] - self.lineRegionTopLeft[0]) / 8):
                                   self.lineRegionBottomRight[0]
                                   ]

                cv2.imwrite(f"{self.workSpacePath}/开发者记录/selectedRegionLeft.jpg", selectedRegion01)
                cv2.imwrite(f"{self.workSpacePath}/开发者记录/selectedRegionRight.jpg", selectedRegion02)
                getOut(f"selecedRegion pic saved")

                grayRegion01 = cv2.cvtColor(selectedRegion01, cv2.COLOR_BGR2GRAY)
                sharpness01 = round(cv2.Laplacian(grayRegion01, cv2.CV_64F).var(), 2)
                grayRegion02 = cv2.cvtColor(selectedRegion02, cv2.COLOR_BGR2GRAY)
                sharpness02 = round(cv2.Laplacian(grayRegion02, cv2.CV_64F).var(), 2)
                sharpness = (sharpness01 + sharpness02) / 2
                self.sharpness = sharpness
                getOut(f"sharpness is:{sharpness:.2f}")
                return sharpness
        except Exception as e:
            getOut(f"ERROR:{e}")
            return f"{e}"

    def clickTest(self, getOut=None):
        self.click('focus_bar', 'focus_up', getOut)
        # getOut(f"res: {res01}")
        time.sleep(1)
        self.click('focus_bar', 'focus_down02', getOut)

        # self.focusOperationTest(getOut)
        # getOut(f"res: {res02}")
        return None

    def focusOperationTest(self, getOut=None):
        try:
            # 先把镜头往上拉，然后重新找线
            # self.screenshot()
            for i in range(4):
                self.click('focus_bar', 'focus_up', getOut=getOut)
                time.sleep(0.5)
            self.findLine(getOut)
            oldSharpness = self.getLineSharpness(getOut)
            getOut(f"sharpness:{oldSharpness}")
            # 对焦算法
            while True:
                self.click('focus_bar', 'focus_down', getOut)
                time.sleep(0.5)
                sharpness = self.getLineSharpness(getOut)
                if sharpness < oldSharpness:
                    self.click('focus_bar', 'focus_up', getOut)
                    time.sleep(0.5)
                    sharpness = self.getLineSharpness(getOut)
                    getOut(f"final sharpness is :{sharpness}")
                    break
                oldSharpness = sharpness
            # 对焦完后往下再向下点几下
            for j in range(8):
                self.click('focus_bar', 'focus_down', getOut)
                time.sleep(0.5)
            return f"focus test finished ,current sharpness is {self.sharpness}"
        except Exception as e:
            return f"error:{e}"

    def numberDetect(self):
        pos_w, pos_h = pyautogui.position()
        # 直接根据当前位置进行OCR
        self.screenshot()
        numberRegion = self.currentScreen[pos_h - 50:pos_h + 50, pos_w - 80:pos_w + 80]
        res = pytesseract.image_to_string(numberRegion)
        match = re.search(r"\d+\.\d+", res)  # 匹配一个或多个数字，加上一个小数点，再加上一个或多个数字
        if match:
            num = match.group()  # 提取匹配到的字符串
            return True, num[:3] + num[-1]  # 打印小数点前两位和小数点后一位
        else:
            return False

    def pullParallelLineTest(self):
        # 这个是点三个点，然后拉一条线
        try:
            self.click("task_bar", "measure")
            time.sleep(0.5)
            self.click("panel_measurement", "panel_measurement_button")
            time.sleep(0.5)
            self.click("measurement_menu", "parallel_line")
            left_point = (100, 100)
            pyautogui.moveTo(left_point)
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.moveRel(0, 200)
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.moveRel(100, 0)
            pyautogui.click()
            return f"current pos :{pyautogui.position()}"
        except Exception as e:
            return f"{e}"

    def parallelLineMeasurementTest(self):
        # 点三个点，拉一条线，然后读出来数字
        try:
            self.click("task_bar", "measure")
            time.sleep(0.5)
            self.click("panel_measurement", "panel_measurement_button")
            time.sleep(0.5)
            self.click("measurement_menu", "parallel_line")
            left_point = (self.lineRegionTopLeft[0], self.screenHeight // 2)
            pyautogui.moveTo(left_point)
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.moveRel(0, 200)
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.moveRel(self.lineRegionBottomRight[0] - self.lineRegionTopLeft[0], 0)
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.moveRel(200, 0)

            time.sleep(2)
            pos_w, pos_h = pyautogui.position()
            self.screenshot()
            numberRegion = self.currentScreen[pos_h - 50:pos_h + 50, pos_w - 80:pos_w + 80]
            res = pytesseract.image_to_string(numberRegion)
            match = re.search(r"\d+\.\d+", res)
            if match:
                num = match.group()
                final_num = num[:3] + num[-1]
            else:
                final_num = f"error"
            return final_num
        except Exception as e:
            return f"{e}"

    def adjustHeightTest(self):
        try:
            ret, res = self.findButton("adjust_height_region", "adjust_height_cursor")
            if ret:  # and self.runningFlag:
                pyautogui.moveTo(res[0], res[1])
                pyautogui.dragRel(-80, 0)
                return f"adjust height finished"
            else:
                return f"cannot find button"
        except Exception as e:
            return e

    def selectHeightOrColorTest(self):
        try:
            time.sleep(1)
            res = self.click("height_or_color", "click_button01")
            return res
        except Exception as e:
            return e

    def contourParallelLineSelectTest(self):
        try:
            self.click('show_bar', 'select_contour')
            time.sleep(3)
            self.click('contour_menu', 'contour_parallel_line')
            # 先测试点一个固定点
            res = pyautogui.click(1094, 172)
            return res
        except Exception as e:
            return e

    def tesseractTest(self, getOut=None):
        try:
            time.sleep(3)
            pos = pyautogui.position()
            self.screenshot()
            getOut(f"pos:{pos}")
            # print(pos)
            img = self.currentScreen[pos[1]:pos[1] + 50, 0:pos[0] + 100]
            res = pytesseract.image_to_string(img)
            getOut(f"res is :{res}")
            return res

        except Exception as e:
            return e

    def readAxisNumberTest(self):
        try:
            self.screenshot()
            numberRegion = self.currentScreen[586:606, 1:40]
            coordHeight = float(pytesseract.image_to_string(numberRegion))
            return f"{coordHeight:.2f}"
        except Exception as e:
            return e

    def getScaleTest(self):
        # try:
        self.screenshot()
        numberRegion = self.currentScreen[586:606, 1:40]
        lineRegion = self.currentScreen[595:992, 54:1411]
        coordHeight = float(pytesseract.image_to_string(numberRegion))
        pixelHeight = 992 - 595
        heightScale = pixelHeight / coordHeight

        coordWidth = 347.09
        pixelWidth = 1411 - 54
        widthScale = pixelWidth / coordWidth

        return f"{heightScale:.2f}", f"{widthScale:.2f}"

        # except Exception as e:
        #     return e

    def getWidthHeightTest(self, getOut=None, getOut02=None):
        # 这里除了宽高，还有面积的计算

        def find_unique_index(sequence):
            # 用于key-value的一一对应
            unique_values = set(sequence)  # 获取序列中的唯一值
            index_dir = {}  # 存储不同值的索引字典
            for value in unique_values:
                index_dir[value] = [i for i, x in enumerate(sequence) if x == value]
            return index_dir

        # try:
        self.screenshot()
        # 检测宽高的误差范围和标准值
        std_width = self.std_w
        std_height = self.std_h
        err_w = self.err_w
        err_h = self.err_h

        getOut(f"std_width is :{std_width}")

        # 测试用，真用就这俩注释了
        # img = cv2.imread('resources4test02/03/2.bmp')
        # self.currentScreen = cv2.imread('resources4test02/03/2.bmp')

        # 通过银线位置来预估宽度的范围
        left_scale = self.lineRegionTopLeft[0] / 1440
        right_scale = self.lineRegionBottomRight[0] / 1440
        lineRegion_left = int((1411 - 54) * left_scale) + 54
        lineRegion_right = int((1411 - 54) * right_scale) + 54

        getOut(f"lineRegion for x from {lineRegion_left} to {lineRegion_right}")

        numberRegion = self.currentScreen[586:606, 1:40]
        # w：54:1411;
        # h:595:992
        lineRegion = self.currentScreen[595:992, lineRegion_left:lineRegion_right]

        coordHeight = float(pytesseract.image_to_string(numberRegion))
        getOut(f"coord height is: {coordHeight:.2f}")

        pixelHeight = 992 - 595
        heightScale = pixelHeight / coordHeight
        getOut(f"height scale is: {heightScale:.2f}")

        coordWidth = 347.09
        pixelWidth = 1411 - 54
        widthScale = pixelWidth / coordWidth
        getOut(f"width scale is: {widthScale:.2f}")

        grayLine = cv2.cvtColor(lineRegion, cv2.COLOR_BGR2GRAY)
        _, binLine = cv2.threshold(grayLine, 5, 255, cv2.THRESH_BINARY)

        # cv2.imshow('2',binLine)

        res = cv2.findNonZero(binLine)
        points = np.squeeze(res)
        getOut(f"points:{points.shape}")
        x, y = np.split(points, 2, axis=1)
        # getOut(f"x:{x},y:{y}")
        x = np.squeeze(x)
        y = np.squeeze(y)
        nonrepeat_x_list = []
        nonrepeat_y_list = []
        nonrepeat_index_list = []
        # 固定住x的index，让x的index唯一
        nonrepeat_index_dir = find_unique_index(x)

        for value, index in nonrepeat_index_dir.items():
            nonrepeat_index_list.append(index[0])

        for norepeat_index in nonrepeat_index_list:
            nonrepeat_x_list.append(x[norepeat_index])
            nonrepeat_y_list.append(y[norepeat_index])
        # 返回波峰的索引
        height_index = np.argmin(nonrepeat_y_list)
        getOut(f"height index is {height_index}")

        # 这个是一个邻域
        left_index = 0
        current_left_height = nonrepeat_y_list[left_index]
        current_left_res01 = 0
        res02_left_list = []
        while left_index <= height_index:
            old_left_height = current_left_height
            old_left_res01 = current_left_res01
            current_left_height = nonrepeat_y_list[left_index]
            left_index += 1
            current_left_res01 = old_left_height - current_left_height
            current_left_res02 = old_left_res01 - current_left_res01
            # print(current_left_res02)
            res02_left_list.append(current_left_res02)
        res02_left_np = np.array(res02_left_list)
        max_res02_left_index = np.argmax(res02_left_np)
        left_width_index = max_res02_left_index - 9
        getOut(f"left_width_index is :{left_width_index}")

        # 找右边，
        right_index = height_index
        current_right_height = nonrepeat_y_list[right_index]
        current_right_res01 = 0
        res02_right_list = []
        while right_index < len(nonrepeat_y_list):  # height_index + width_index_offset:
            old_right_height = current_right_height
            old_right_res01 = current_right_res01
            current_right_height = nonrepeat_y_list[right_index]
            right_index += 1
            current_right_res01 = current_right_height - old_right_height
            current_right_res02 = current_right_res01 - old_right_res01
            # print(current_right_res02)
            res02_right_list.append(current_right_res02)
        res02_right_np = np.array(res02_right_list)
        # 梯度一直下降，所以是二阶导最小的地方
        min_res02_right_index = np.argmin(res02_right_np)
        right_width_index = height_index + min_res02_right_index + 9
        getOut(f"right_width_index is :{right_width_index}")

        print(nonrepeat_x_list)
        # 计算高宽
        width = (nonrepeat_x_list[right_width_index] - nonrepeat_x_list[left_width_index]) / widthScale
        width = round(width, 3)
        getOut(f"width 计算值为：{width}")
        height = ((nonrepeat_y_list[left_width_index] + nonrepeat_y_list[right_width_index]) / 2 - nonrepeat_y_list[
            height_index]) / heightScale
        height = round(height, 3)
        getOut(f"height 计算值为：{height}")

        # 测试宽高是否找对了
        # cv2.circle(img,
        #            (nonrepeat_x_list[left_width_index] + lineRegion_left, nonrepeat_y_list[left_width_index] + 595),
        #            radius=2, color=(0, 255, 0),
        #            thickness=3)
        #
        # cv2.circle(img, (
        # nonrepeat_x_list[right_width_index] + lineRegion_left, nonrepeat_y_list[right_width_index] + 595),
        #            radius=2, color=(0, 255, 0),
        #            thickness=3)
        # cv2.namedWindow('1', cv2.WINDOW_NORMAL)
        # cv2.imshow('1', img)

        # 计算面积
        area = 0
        height_offset = (nonrepeat_y_list[right_width_index] - nonrepeat_y_list[left_width_index]) / (
                right_width_index - left_width_index)
        getOut(f"height_offset is :{height_offset}")
        for i in range(left_width_index, right_width_index):
            cubeHeight = (height_offset * i + nonrepeat_y_list[left_width_index] - nonrepeat_y_list[i]) / heightScale
            cubeWidth = 1 / widthScale
            area += cubeWidth * cubeHeight
        area = round(area, 3)

        getOut(f"area 计算值为:{area}")
        getOut(f"type of std is :{type(std_width)}")
        getOut(f"type of width is :{type(width)}")

        getOut(f"sub_res:{std_width - width}")

        if abs(std_width - width) < err_w and abs(std_height - height) < err_h:
            with open(f"{self.workSpacePath}/结果查看/原始数据.txt", 'a+') as f:
                f.write(
                    f"{self.currentLineIndex}-{self.currentPosIndex}-{self.currentCurveIndex}"
                    f": W:{width:.2f}, H:{height:.2f}, A:{area:.2f}\n")

            getOut(f"已写入,文件位置为{self.workSpacePath}/结果查看/原始数据.txt")
            getOut(f"height is :{height:.2f} μm")
            getOut(f"width is: {width:.2f} μm")
            getOut(f"area is: {area:.2f} μm^2")
            getOut02(width, height, area)
            return width, height

        elif width < std_width - err_w and height < std_height - err_h:
            with open(f"{self.workSpacePath}/broken_points/broken_points_data.txt", 'a+') as f:
                f.write(
                    f"{self.currentLineIndex}-{self.currentPosIndex}-{self.currentCurveIndex}"
                    f": W:{width:.2f}, H:{height:.2f}, A:{area:.2f}\n")

            getOut(f"发现一处断点,位置为: {self.currentLineIndex}-{self.currentLineIndex}-{self.currentCurveIndex}")

            pic = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
            cv2.imwrite(
                f"{self.workSpacePath}/broken_points/{self.currentLineIndex}-{self.currentLineIndex}-{self.currentCurveIndex}.png",
                pic)
            getOut(f"height is :{height:.2f} μm")
            getOut(f"width is: {width:.2f} μm")
            getOut(f"area is: {area:.2f} μm^2")
            getOut(f"已保存此处断点图片")
            getOut02(width, height, area)
            return width, height
        else:
            return width, height

    def analyseResult(self, file, getOut=None):
        w_list = []
        h_list = []
        a_list = []

        with open(file, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(': ')
                    values = parts[1].split(',')
                    w = float(values[0].split('W:')[1].strip())
                    h = float(values[1].split('H:')[1].strip())
                    a = float(values[2].split('A:')[1].strip())
                    w_list.append(w)
                    h_list.append(h)
                    a_list.append(a)

        w_np = np.array(w_list)
        getOut(f"W_AVG: {w_np.mean():.2f}")
        getOut(f"W_STD: {w_np.std():.2f}")
        getOut(f"W_MAX: {w_np.max()}")
        getOut(f"W_MIN: {w_np.min()}")
        getOut(f"W_SUM: {w_np.sum()}")

        h_np = np.array(h_list)
        getOut(f"H_AVG: {h_np.mean():.2f}")
        getOut(f"H_STD: {h_np.std():.2f}")
        getOut(f"H_MAX: {h_np.max()}")
        getOut(f"H_MIN: {h_np.min()}")

        a_np = np.array(a_list)
        getOut(f"A_AVG: {a_np.mean():.2f}")
        getOut(f"A_STD: {a_np.std():.2f}")
        getOut(f"A_MAX: {a_np.max()}")
        getOut(f"A_MIN: {a_np.min()}")

        s_np = np.array(self.surface_area_list)
        getOut(f"S_AVG: {s_np.mean():.2f}")
        getOut(f"S_STD: {s_np.std():.2f}")
        getOut(f"S_MAX: {s_np.max():.2f}")
        getOut(f"S_MIN: {s_np.min():.2f}")
        # 1/s 的求和
        a_1 = 0
        for a in a_np:
            a_1 += 1 / a
        getOut(f"A_INV_SUM: {a_1:.2f}")
        with open(f"{self.workSpacePath}/结果查看/统计结果.txt", 'w+') as f:
            f.write(f"==========  参数设置  ==================\n")
            f.write(f"设置宽度标准值: {self.Processor.std_w}\n")
            f.write(f"设置宽度误差阈值: {self.Processor.err_w}\n")
            f.write(f"设置高度标准值: {self.Processor.std_h}\n")
            f.write(f"设置高度误差阈值: {self.Processor.err_h}\n")
            f.write(f"设置栅线条数为: {self.Processor.lineNum}\n")
            f.write(f"设置每条栅线检测点位为: {self.Processor.posNum}\n")
            f.write(f"设置每个点位中的切片个数为: {self.Processor.curveNum}\n")

            f.write(f"==========  宽度统计  ==================\n")

            f.write(f"平均宽度: {w_np.mean():.2f}\n")
            f.write(f"宽度标准差: {w_np.std():.2f}\n")
            f.write(f"最大宽度: {w_np.max()}\n")
            f.write(f"最小宽度: {w_np.min()}\n")
            f.write(f"宽度之和: {w_np.sum()}\n")

            f.write(f"==========  高度统计  ==================\n")

            f.write(f"高度平均值: {h_np.mean():.2f}\n")
            f.write(f"高度标准差: {h_np.std():.2f}\n")
            f.write(f"最大高度: {h_np.max()}\n")
            f.write(f"最小高度: {h_np.min()}\n")

            f.write(f"==========  横截面积统计  ================\n")

            f.write(f"横截面积平均值: {a_np.mean():.2f}\n")
            f.write(f"横截面积标准差: {a_np.std():.2f}\n")
            f.write(f"最大横截面积: {a_np.max()}\n")
            f.write(f"最小横截面积: {a_np.min()}\n")
            f.write(f"横截面积倒数之和: {a_1:.2f}\n")

            f.write(f"===========  表面积统计  ================\n")
            f.write(f"表面积平均值: {s_np.mean():.2f}\n")
            f.write(f"表面积标准差: {s_np.std():.2f}\n")
            f.write(f"最大表面积: {s_np.max()}\n")
            f.write(f"最小表面积: {s_np.min()}\n")

    def verticalMoveTest(self, getOut=None):
        #   这里是向上移动的
        if not self.runningFlag:
            raise Exception("中途停止", )
        pyautogui.click(700, 500)
        old_pos_topLeft = self.lineRegionTopLeft
        getOut(f"old top left pos: {old_pos_topLeft}")
        time.sleep(0.5)
        times = 0  # just for count to break
        while 1:

            if not self.runningFlag:
                raise Exception("中途停止", )

            if self.verticalMoveUpDirection:
                for i in range(2):
                    pyautogui.click(self.screenWidth // 2, self.screenHeight // 2)
                    pyautogui.moveTo(self.screenWidth // 2, self.screenHeight // 4)
                    pyautogui.dragRel(0, self.screenHeight // 2, button='left', duration=0.5)
                    time.sleep(0.5)
                res = self.findLine(getOut)
                times += 1
                if res[2] == 1 or times >= 20:
                    break
            else:
                for i in range(2):
                    pyautogui.click(self.screenWidth // 2, self.screenHeight // 2)
                    pyautogui.moveTo(self.screenWidth // 2, 3 * self.screenHeight // 4)
                    pyautogui.dragRel(0, -self.screenHeight // 2, button='left', duration=0.5)
                    time.sleep(0.5)
                res = self.findLine(getOut)
                times += 1
                if res[2] == 1 or times >= 20:
                    break

        if times >= 5:
            getOut(f"垂直移动的途中可能遇到了节点")

        new_pos_topLeft, _, _ = self.findLine(getOut)
        getOut(f"new top left pos: {new_pos_topLeft}")
        offset = old_pos_topLeft[0] - new_pos_topLeft[0]
        getOut(f"offset is: {offset}")
        pyautogui.dragRel(offset, 0, 0.5)
        time.sleep(1)
        res = self.findLine(getOut)

        # 如果是向上的话，就是加
        if self.verticalMoveUpDirection:
            getOut(f"方向是向上")
            self.currentPosIndex += 1
        else:
            getOut(f"方向是向下")
            self.currentPosIndex -= 1

        getOut(f"finish vertical move")
        return res

    def horizontalMoveTest(self, getOut=None):
        if not self.runningFlag:
            raise Exception("中途停止", )
        # 从右边向左边移动
        pyautogui.click(700, 500)
        time.sleep(0.5)
        pyautogui.moveTo(self.screenWidth // 4, self.screenHeight // 2)
        pyautogui.dragRel(self.screenWidth // 2, 0, button='left', duration=0.5)
        time.sleep(0.5)
        times = 0
        while 1:
            if not self.runningFlag:
                raise Exception("中途停止", )
            pyautogui.moveTo(self.screenWidth // 4, self.screenHeight // 2)
            pyautogui.dragRel(self.screenWidth // 2, 0, button='left', duration=0.5)
            time.sleep(0.5)

            try:
                res = self.findLine(getOut)
                getOut(f"res of find the line:{res}")
                times += 1
                if res[2] == 1 or times >= 100:
                    break
            except IndexError as e:
                getOut(f"{e}")
                times += 1
                continue

        self.verticalMoveUpDirection = not self.verticalMoveUpDirection
        self.currentLineIndex += 1

        self.resultIndex += 1
        # 注意这里的次数应该是需要除以2的，因为每次都是只移动了半个屏幕尺寸
        getOut(f"resultIndex is ：{self.resultIndex}")
        return res

    def getSurfaceArea(self, img, getOut=None):
        img_line = img[
                   self.lineRegionTopLeft[1]: self.lineRegionBottomRight[1],
                   self.lineRegionTopLeft[0]: self.lineRegionBottomRight[0]
                   ]
        img_gray = cv2.cvtColor(img_line, cv2.COLOR_BGR2GRAY)
        # 以像素个数来代表面积，和实际面积差了一个 像素到坐标，坐标再到实际的一个变化
        # 1440 pixels = 347.09 um
        scale = 347.09 / 1440
        surface_area_count = 0
        height, width = img_gray.shape
        # 遍历图像的每个像素
        for y in range(height):
            for x in range(width):
                gray_value = img_gray[y, x]
                if gray_value > 30:
                    surface_area_count += 1
        surface_area = surface_area_count * scale * scale
        getOut(f"surface_area: {surface_area}")
        self.surface_area_list.append(surface_area)
        return surface_area

    def firstPageProcess(self, getOut=None):
        # 第一页应该是开始对焦的那个界面
        self.findLine(getOut=getOut)
        # self.focusOperationTest(getOut=getOut)
        self.click('start_reconstruction_region', 'start_reconstruction', getOut=getOut)
        time.sleep(5)
        self.click('show_reconstruction_result_region', 'show_reconstruction_result', getOut=getOut)
        time.sleep(5)
        self.click('reconstruction_result_region', '3d_show', getOut=getOut)
        time.sleep(4)

    def secondPageProcess(self, getOut=None):
        self.click('show_bar', 'select_contour', getOut=getOut)
        time.sleep(2)

    def thirdPageProcess(self, getOut01=None, getOut02=None):
        # 不选平均轮廓，检查一下先
        # if_clicked_res = self.ifClicked(getOut=getOut01)
        # if if_clicked_res[1]:
        #     pyautogui.click(if_clicked_res[2])
        # time.sleep(0.4)
        # 开始一边划一边计算宽高
        self.click('contour_menu', 'contour_parallel_line', getOut=getOut01)
        pyautogui.moveTo(1000, 40)
        self.currentCurveIndex = 1
        move_offset = 480 // self.curveNum
        while self.currentCurveIndex <= self.curveNum:
            # 注意这里移动的像素乘上 i的最大值等于480
            if not self.runningFlag:
                raise Exception("中途停止", )
            try:
                pyautogui.moveRel(0, move_offset)
                time.sleep(0.5)
                self.getWidthHeightTest(getOut=getOut01, getOut02=getOut02)
                self.currentCurveIndex += 1
            except IndexError as e:
                self.currentCurveIndex += 1
                getOut01(f"ERR:{e}")

        # 选中平均轮廓，获取平均宽高
        # 这里我标记一下次数，
        # pyautogui.click(if_clicked_res[2])
        # time.sleep(0.4)
        # self.click('contour_menu', 'contour_parallel_line', getOut=getOut01)
        # pyautogui.moveTo(1000, 40)
        # time.sleep(0.4)
        # self.getWidthHeightTest(getOut=getOut01, getOut02=getOut02)
        # 点击Bar上的关闭，然后是弹窗的处理
        self.click('close_region', 'close', getOut=getOut01)
        time.sleep(1)
        # self.click('quit_region', 'yes_button', getOut=getOut01)
        # time.sleep(2)

    def fourthPageProgress(self, getOut=None):
        pic = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)[:, :1440]
        cv2.imwrite(f"{self.workSpacePath}/img/{self.currentLineIndex}-{self.currentPosIndex}.png", pic)
        self.getSurfaceArea(pic, getOut=getOut)
        self.click('back_first_page_region', 'back_first_page', getOut=getOut)
        time.sleep(2)

    def pipelineTest01(self, getOut01, getOut02, draw=None):
        try:
            self.firstPageProcess(getOut=getOut01)
            self.secondPageProcess(getOut=getOut01)
            self.thirdPageProcess(getOut01=getOut01, getOut02=getOut02)
            self.fourthPageProgress(getOut=getOut01)
            draw(self.currentLineIndex, self.currentPosIndex)
            self.verticalMoveTest(getOut=getOut01)

        except Exception as e:
            getOut01(f"ERR:{e}")

    def pipelineTest02(self, getOut01, getOut02, draw=None):
        self.resultPath = f"{getTime()}.txt"
        try:
            for i in range(2):
                for j in range(5):
                    self.pipelineTest01(getOut01=getOut01, getOut02=getOut02, draw=draw)
                self.horizontalMoveTest(getOut01)

        except Exception as e:
            getOut01(f"{e}")

    def followLineDirectionTest(self, getOut01, getOut02, draw=None):
        self.resultPath = f"{getTime()}.txt"
        try:
            for i in range(7):
                self.pipelineTest01(getOut01=getOut01, getOut02=getOut02, draw=draw)
        except Exception as e:
            getOut01(f"ERR:{e}")

    def move_infinite(self):
        while 1:
            if not self.runningFlag:
                raise Exception("中途停止", )
            pyautogui.moveTo(100, 100)
            time.sleep(0.2)
            pyautogui.moveTo(1000, 1000)
            time.sleep(0.2)
            pyautogui.moveTo(500, 500)
            time.sleep(0.2)

    def verticalLineDirectionTest(self, getOut01):
        self.runningFlag = True
        try:
            self.move_infinite()
        except Exception as e:
            getOut01(f"ERR:{e}")

    # ===========================================================================================
    #  这里开始就是真正的应用了
    # ===========================================================================================
    def pipeline(self, getOut01, getOut02, draw=None):
        if not self.runningFlag:
            raise Exception("中途停止", )
        self.firstPageProcess(getOut=getOut01)

        if not self.runningFlag:
            raise Exception("中途停止", )
        self.secondPageProcess(getOut=getOut01)

        if not self.runningFlag:
            raise Exception("中途停止", )
        self.thirdPageProcess(getOut01=getOut01, getOut02=getOut02)

        if not self.runningFlag:
            raise Exception("中途停止", )
        self.fourthPageProgress(getOut=getOut01)

        draw(self.currentLineIndex, self.currentPosIndex)

    def fastPointDetection(self, getOut01, getOut02, draw=None):
        self.runningFlag = True
        try:
            self.pipeline(getOut01=getOut01, getOut02=getOut02, draw=draw)
            self.analyseResult(f"{self.workSpacePath}/结果查看/原始数据.txt", getOut=getOut01)
        except Exception as e:
            getOut01(f"ERR:{e}")

    def doubleLineStdDetection(self, getOut01, getOut02, draw=None):
        self.runningFlag = True
        try:
            self.pipeline(getOut01=getOut01, getOut02=getOut02, draw=draw)
            for i in range(4):
                self.verticalMoveTest(getOut=getOut01)
                self.pipeline(getOut01=getOut01, getOut02=getOut02, draw=draw)

            self.horizontalMoveTest(getOut01)

            self.pipeline(getOut01=getOut01, getOut02=getOut02, draw=draw)
            for j in range(4):
                self.verticalMoveTest(getOut=getOut01)
                self.pipeline(getOut01=getOut01, getOut02=getOut02, draw=draw)

            self.analyseResult(f"{self.workSpacePath}/结果查看/原始数据.txt", getOut=getOut01)
        except Exception as e:
            getOut01(f"ERR:{e}")

    def customDetection(self, getOut01, getOut02, draw=None):
        self.runningFlag = True
        try:
            # 开始检测
            for i in range(self.lineNum):
                self.pipeline(getOut01=getOut01, getOut02=getOut02, draw=draw)
                for j in range(self.posNum - 1):
                    self.verticalMoveTest(getOut=getOut01)
                    self.pipeline(getOut01=getOut01, getOut02=getOut02, draw=draw)
                self.horizontalMoveTest(getOut01)
            # 分析数据
            self.analyseResult(f"{self.workSpacePath}/结果查看/原始数据.txt", getOut=getOut01)
        except Exception as e:
            getOut01(f"ERR:{e}")
