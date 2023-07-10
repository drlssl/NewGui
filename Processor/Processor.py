import time
import re
import cv2
import numpy as np
import imutils
import pyautogui

import pytesseract
import aircv as ac

pytesseract.pytesseract.tesseract_cmd = r"tesseract\tesseract.exe"
pyautogui.FAILSAFE = False


class Processor:
    def __init__(self):
        # 默认是向上移动
        self.verticalMoveUpDirection = True
        self.savedPath = 'savedVideo/'
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

            'first_page': 'resources/img/fistPage.png',
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

    def findButton(self, buttonRegion, button, getOut=None):
        try:
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
        except Exception as e:
            getOut(f"ERROR:{e}")
            print(f"{e}")
            return False, None

    def click(self, buttonRegion, button, getOut=None):
        try:
            # self.currentScreen = cv2.imread('resources4test/10.png')
            self.screenshot()
            ret, res = self.findButton(buttonRegion, button, getOut=getOut)
            if ret:
                getOut(f"res:{res}")
                pyautogui.moveTo(res)
                pyautogui.click()
                return f"{res}"
            else:
                getOut(f"click failed:{res}")
                return res
        except Exception as e:
            print(f"{e}")
            getOut(f"Error:{e}")
            return None

    def ifClicked(self, getOut=None):
        try:  # 主要用于检测第三页的平均轮廓是否已经选中
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
        except Exception as e:
            getOut(f'ERROR:{e}')
            return None

    def screenshot(self):
        self.currentScreen = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)

    def recordScreen(self, fileName):
        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        fps = 30
        print(fileName)
        out = cv2.VideoWriter("savedVideo/" + fileName + ".mp4", fourcc, fps, (self.screenWidth, self.screenHeight))
        while True:
            time_elapsed = time.time()
            img = pyautogui.screenshot()
            if time_elapsed > 1.0 / fps:
                frame = np.array(img)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                out.write(frame)
                if self.recordFlag is False:
                    break
            cv2.waitKey(1)
        cv2.destroyAllWindows()
        out.release()

    def findLine(self, getOut=None):
        try:
            self.screenshot()
            # self.currentScreen = cv2.imread('resources4test/0171.png')
            img = self.currentScreen
            imgSelected = img[:, :1440]

            imgHSV = cv2.cvtColor(imgSelected, cv2.COLOR_BGR2HSV)
            hsv_low = np.array([0, 0, 86])
            hsv_high = np.array([108, 255, 255])
            mask = cv2.inRange(imgHSV, hsv_low, hsv_high)

            lineRegion = cv2.bitwise_and(imgSelected, imgSelected, mask=mask)

            grayLine = cv2.cvtColor(lineRegion, cv2.COLOR_BGR2GRAY)
            x_grad = cv2.Sobel(grayLine, cv2.CV_32F, dx=1, dy=0, ksize=-1)
            y_grad = cv2.Sobel(grayLine, cv2.CV_32F, dx=0, dy=1, ksize=-1)
            gradLine = cv2.subtract(x_grad, y_grad)
            gradLine = cv2.convertScaleAbs(gradLine)
            blurredLine = cv2.blur(gradLine, (5, 5))
            _, thresholdLine = cv2.threshold(blurredLine, 100, 255, cv2.THRESH_BINARY)

            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 7))
            closedLine = cv2.morphologyEx(thresholdLine, cv2.MORPH_CLOSE, kernel)

            lineContours = cv2.findContours(closedLine, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            lineCnts = imutils.grab_contours(lineContours)
            lineContour = sorted(lineCnts, key=cv2.contourArea, reverse=True)[0]
            lineRect = cv2.minAreaRect(lineContour)
            boxPoints = cv2.boxPoints(lineRect)
            intBoxPoints = np.intp(boxPoints)

            top_left = [min(point[0] for point in intBoxPoints), min(point[1] for point in intBoxPoints)]
            bottom_right = [max(point[0] for point in intBoxPoints), max(point[1] for point in intBoxPoints)]
            top_left[0] = max(0, top_left[0])
            top_left[1] = min(1080, top_left[1])
            bottom_right[0] = max(0, bottom_right[0])
            bottom_right[1] = min(1080, bottom_right[1])
            getOut(f"top left is {top_left}")
            getOut(f"bottom right is {bottom_right}")

            if (bottom_right[0] - top_left[0] + bottom_right[1] - top_left[1]) <= 1080:
                getOut(f"cannot find the line")
                return top_left, bottom_right, 0
            elif (top_left[0] <= 50):
                getOut(f"the line located at the left edge")
                getOut(f"should move it right more")
                return top_left, bottom_right, 0
            else:
                self.lineRegionTopLeft = top_left
                self.lineRegionBottomRight = bottom_right
                getOut(f"find the line")
                getOut(f"current top left is: {top_left}, bottom right is: {bottom_right}")
                cv2.rectangle(img, top_left, bottom_right, (0, 255, 255), 3)
                cv2.imwrite("savedVideo/findLineTestResult.jpg", img)
                getOut(f"current line region pic saved at savedVideo dir")
                return top_left, bottom_right, 1
        except Exception as e:
            getOut(f"{e}")
            return f"{e}"

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
                                   self.lineRegionTopLeft[0]:self.lineRegionTopLeft[0] + int(
                                       (self.lineRegionBottomRight[0] - self.lineRegionTopLeft[0]) / 3)
                                   ]
                selectedRegion02 = self.currentScreen[
                                   self.lineRegionTopLeft[1]:self.lineRegionBottomRight[1],
                                   self.lineRegionTopLeft[0] + 2 * int(
                                       (self.lineRegionBottomRight[0] - self.lineRegionTopLeft[0]) / 3):
                                   self.lineRegionBottomRight[0]
                                   ]

                cv2.imwrite("savedVideo/selectedRegionLeft.jpg", selectedRegion01)
                cv2.imwrite("savedVideo/selectedRegionRight.jpg", selectedRegion02)
                getOut(f"selecedRegion has saved at savedVideo dir")

                grayRegion01 = cv2.cvtColor(selectedRegion01, cv2.COLOR_BGR2GRAY)
                sharpness01 = round(cv2.Laplacian(grayRegion01, cv2.CV_64F).var(), 2)
                grayRegion02 = cv2.cvtColor(selectedRegion02, cv2.COLOR_BGR2GRAY)
                sharpness02 = round(cv2.Laplacian(grayRegion02, cv2.CV_64F).var(), 2)
                sharpness = sharpness01 + sharpness02
                self.sharpness = sharpness
                getOut(f"sharpness is:{sharpness:.2f}")
                return sharpness
        except Exception as e:
            getOut(f"ERROR:{e}")
            return f"{e}"

    def clickTest(self, getOut=None):
        # self.click('back_first_page_region', 'back_first_page', getOut=getOut)
        # self.click('quit_region', 'yes_button',getOut=getOut)
        # self.click('close_region', 'close', getOut=getOut)
        # if_clicked_res = self.ifClicked(getOut=getOut)
        # if if_clicked_res[1]:
        #     pyautogui.click(if_clicked_res[2])
        # time.sleep(0.4)
        #
        # self.click('contour_menu', 'contour_parallel_line', getOut=getOut)
        # self.click('contour_menu', 'contour_parallel_line', getOut=getOut)
        # self.click('show_bar', 'select_contour', getOut=getOut)
        # self.click('reconstruction_result_region', '3d_show', getOut=getOut)
        # self.click('start_reconstruction_region', 'start_reconstruction', getOut=getOut)
        # self.click('show_reconstruction_result_region', 'show_reconstruction_result', getOut=getOut)

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
            if ret:
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
        try:
            self.screenshot()
            numberRegion = self.currentScreen[586:606, 1:40]
            lineRegion = self.currentScreen[595:992, 54:1411]
            coordHeight = float(pytesseract.image_to_string(numberRegion))
            pixelHeight = 992 - 595
            heightScale = pixelHeight / coordHeight

            coordWidth = 312.38  # 347.09
            pixelWidth = 1411 - 54
            widthScale = pixelWidth / coordWidth

            return f"{heightScale:.2f}", f"{widthScale:.2f}"
        except Exception as e:
            return e

    def getWidthHeightTest(self, getOut=None, getOut02=None):

        def find_unique_index(sequence):
            # 用于key-value的一一对应
            unique_values = set(sequence)  # 获取序列中的唯一值
            index_dir = {}  # 存储不同值的索引字典
            for value in unique_values:
                index_dir[value] = [i for i, x in enumerate(sequence) if x == value]
            return index_dir

        def stopRepeat(raw_array):
            # 找到数组中不重复的索引列表，这个好像没用到
            index = 0
            index_list = [0]
            for i in range(len(raw_array)):
                comparision = raw_array[index]
                if raw_array[i] == comparision:
                    i += 1
                else:
                    index = i
                    index_list.append(index)
                    i += 1
            return index_list

        try:
            self.screenshot()

            # 测试用，真用就这俩注释了
            # img = cv2.imread('resources4test/08.png')
            # self.currentScreen = cv2.imread('resources4test/08.png')

            numberRegion = self.currentScreen[586:606, 1:40]
            # w：54:1411;
            # h:595:992
            lineRegion = self.currentScreen[595:992, 54:1411]

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
            # getOut(f"points:{points.shape}")
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


            # 这个是一个邻域
            width_index_offset=80
            left_index = height_index - width_index_offset
            current_left_height = nonrepeat_y_list[left_index]
            current_left_res01 = 0
            res02_left_list = []
            while left_index <=height_index:
                old_left_height = current_left_height
                old_left_res01 = current_left_res01
                current_left_height = nonrepeat_y_list[left_index]
                left_index += 1
                current_left_res01 = old_left_height - current_left_height
                current_left_res02 = old_left_res01 - current_left_res01
                # print(current_left_res02)
                res02_left_list.append(current_left_res02)
            res02_left_np = np.array(res02_left_list)
            # max_res02_left_index = np.argmax(res02_left_np)
            max_res02_left_index = np.argmax(res02_left_np)
            left_width_index = height_index - max_res02_left_index-9

            # 找右边，
            right_index = height_index
            current_right_height = nonrepeat_y_list[right_index]
            current_right_res01 = 0
            res02_right_list = []
            while right_index < height_index+width_index_offset:
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
            # min_res02_right_index = np.argmin(np.abs(res02_right_np))
            right_width_index = height_index + min_res02_right_index+9

            # 计算高宽
            width = (nonrepeat_x_list[right_width_index] - nonrepeat_x_list[left_width_index]) / widthScale
            height = ((nonrepeat_y_list[left_width_index] + nonrepeat_y_list[right_width_index]) / 2 - nonrepeat_y_list[
                height_index]) / heightScale

            # 测试宽高是否找对了
            # cv2.circle(img, (nonrepeat_x_list[left_width_index] + 54, nonrepeat_y_list[left_width_index] + 595), radius=2, color=(0, 255, 0),
            #            thickness=3)
            #
            # cv2.circle(img, (nonrepeat_x_list[right_width_index] + 54, nonrepeat_y_list[right_width_index] + 595), radius=2, color=(0, 255, 0),
            #            thickness=3)
            # cv2.namedWindow('1',cv2.WINDOW_NORMAL)
            # cv2.imshow('1',img)

            std_width=32
            std_height=7
            err_w=5
            err_h=1

            if abs(std_width-width)<err_w and abs(std_height-height)<err_h:
                with open(self.savedPath + "记录.txt", 'a+') as f:
                    f.write(
                        f"{self.currentLineIndex}-{self.currentPosIndex}-{self.currentCurveIndex}: 宽:{width:.2f} μm , 高:{height:.2f} μm\n")
                getOut(f"已写入,文件位置为 {self.savedPath}记录.txt")
                getOut(f"height is :{height:.2f} μm")
                getOut(f"width is: {width:.2f} μm")
                getOut02(width, height)
                return width, height
            else:
                return width,height
            # 之前走死位置的老方法
            # peakIndex = np.argmin(y)
            # height = (pixelHeight - y[peakIndex]) / heightScale
            # getOut(f"height is: {height:.2f} μm")
            #
            # widthIndex = np.where(y == int(pixelHeight - 4 * heightScale))
            # widthLeftIndex = widthIndex[0][0]
            # for i in widthIndex[0]:
            #     if x[i] - x[widthLeftIndex] >= 100:
            #         widthRightIndex = i
            #         break
            # width = (x[widthRightIndex] - x[widthLeftIndex]) / widthScale
            # getOut(f"width is: {width:.2f} μm")
            # getOut02(width, height)
            # return width, height
        except Exception as e:
            getOut(f"ERROR: {e}")
            return e

    def verticalMoveTest(self, getOut=None):
        #   这里是向上移动的
        try:
            pyautogui.click(700, 500)
            old_pos_topLeft = self.lineRegionTopLeft
            getOut(f"old top left pos: {old_pos_topLeft}")
            time.sleep(0.5)
            if self.verticalMoveUpDirection:
                for i in range(2):
                    # pyautogui.click(self.screenWidth // 2, self.screenHeight // 2)
                    pyautogui.moveTo(self.screenWidth // 2, self.screenHeight // 4)
                    pyautogui.dragRel(0, self.screenHeight // 2, button='left', duration=0.5)
                    time.sleep(0.5)

            else:
                for i in range(2):
                    # pyautogui.click(self.screenWidth // 2, self.screenHeight // 2)
                    pyautogui.moveTo(self.screenWidth // 2, 3 * self.screenHeight // 4)
                    pyautogui.dragRel(0, -self.screenHeight // 2, button='left', duration=0.5)
                    time.sleep(0.5)

            new_pos_topLeft, _, _ = self.findLine(getOut)
            getOut(f"new top left pos: {new_pos_topLeft}")

            offset = old_pos_topLeft[0] - new_pos_topLeft[0]
            getOut(f"offset is: {offset}")
            pyautogui.dragRel(offset, 0, 0.5)
            time.sleep(1)
            res = self.findLine(getOut)

            return res
        except Exception as e:
            getOut(f"ERROR:{e}")
            return e

    def horizontalMoveTest(self, getOut=None):
        # 从右边向左边移动
        pyautogui.click(700, 500)
        time.sleep(1.5)
        pyautogui.moveTo(self.screenWidth // 4, self.screenHeight // 2)
        pyautogui.dragRel(self.screenWidth // 2, 0, button='left', duration=0.5)
        time.sleep(0.5)
        times = 0
        try:
            while 1:
                # pyautogui.click(self.screenWidth // 2, self.screenHeight // 2)
                pyautogui.moveTo(self.screenWidth // 4, self.screenHeight // 2)
                pyautogui.dragRel(self.screenWidth // 2, 0, button='left', duration=0.5)
                time.sleep(0.5)
                res = self.findLine(getOut)
                times += 1
                if res[2] == 1 or times >= 100:
                    break
            self.verticalMoveUpDirection = not self.verticalMoveUpDirection
            # 注意这里的次数应该是需要除以2的，因为每次都是只移动了半个屏幕尺寸
            getOut(f"本次水平移动的总次数是：{times}")
            return res
        except Exception as e:
            getOut(f"ERROR:{e}")
            return e

    def firstPageProcess(self, getOut=None):
        try:
            self.click('task_bar', 'first_page', getOut=getOut)
            self.findLine(getOut=getOut)
            self.focusOperationTest(getOut=getOut)
            self.click('start_reconstruction_region', 'start_reconstruction', getOut=getOut)
            time.sleep(8)
            self.click('show_reconstruction_result_region', 'show_reconstruction_result', getOut=getOut)
            time.sleep(5)
            self.click('reconstruction_result_region', '3d_show', getOut=getOut)
            time.sleep(3)
        except Exception as e:
            getOut(f"ERROR:{e}")

    def secondPageProcess(self, getOut=None):
        try:
            self.click('show_bar', 'select_contour', getOut=getOut)
            time.sleep(2)
        except Exception as e:
            getOut(f"ERROR:{e}")

    def thirdPageProcess(self, getOut01=None, getOut02=None):
        try:
            # 不选平均轮廓，检查一下先
            if_clicked_res = self.ifClicked(getOut=getOut01)
            if if_clicked_res[1]:
                pyautogui.click(if_clicked_res[2])
            time.sleep(0.4)
            # 开始一边划一边计算宽高
            self.click('contour_menu', 'contour_parallel_line', getOut=getOut01)
            pyautogui.moveTo(1000, 40)
            self.currentCurveIndex = 1
            for i in range(30):
                pyautogui.moveRel(0, 16)
                time.sleep(0.5)
                self.getWidthHeightTest(getOut=getOut01, getOut02=getOut02)
                self.currentCurveIndex += 1
            # 选中平均轮廓，获取平均宽高
            # 这里我标记一下次数，
            pyautogui.click(if_clicked_res[2])
            time.sleep(0.4)
            self.click('contour_menu', 'contour_parallel_line', getOut=getOut01)
            pyautogui.moveTo(1000, 40)
            time.sleep(0.4)
            self.getWidthHeightTest(getOut=getOut01, getOut02=getOut02)
            # 点击Bar上的关闭，然后是弹窗的处理
            self.click('close_region', 'close', getOut=getOut01)
            time.sleep(1)
            self.click('quit_region', 'yes_button', getOut=getOut01)
            time.sleep(2)
        except Exception as e:
            getOut01(f"ERROR:{e}")

    def fourthPageProgress(self, getOut=None):
        try:
            self.click('back_first_page_region', 'back_first_page', getOut=getOut)
            time.sleep(2)
        except Exception as e:
            getOut(f"ERROR:{e}")

    def pipelineTest01(self, getOut01, getOut02, draw=None):
        try:
            self.firstPageProcess(getOut=getOut01)
            self.secondPageProcess(getOut=getOut01)
            self.thirdPageProcess(getOut01=getOut01, getOut02=getOut02)
            self.fourthPageProgress(getOut=getOut01)
            draw(self.currentLineIndex, self.currentPosIndex)
            self.verticalMoveTest(getOut=getOut01)
            # 如果是向上的话，就是加
            if self.verticalMoveUpDirection:
                self.currentPosIndex += 1
            else:
                self.currentPosIndex -= 1
        except Exception as e:
            getOut01(f"e")

    def pipelineTest02(self, getOut01, getOut02, draw=None):
        for i in range(3):
            for j in range(3):
                self.pipelineTest01(getOut01=getOut01, getOut02=getOut02, draw=draw)
            self.horizontalMoveTest(getOut01)
            self.currentLineIndex += 1
        # for i in range(2):
        #     self.pipelineTest01(getOut01=getOut01, getOut02=getOut02, draw=draw)
