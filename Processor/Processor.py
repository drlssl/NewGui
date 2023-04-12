import time
import re
import cv2
import numpy as np
import imutils
import pyautogui

import pytesseract
import aircv as ac

pytesseract.pytesseract.tesseract_cmd = "D:\\Tesseract_OCR\\tesseract.exe"


class Processor:
    def __init__(self):
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
            'focus_up': 'resources/img/focusUp.png',
            'focus_down': 'resources/img/focusDown.png',

            'focus_up02': 'resources/img/focusUp02.png',
            'focus_down02': 'resources/img/focusDown02.png',

            'start_reconstruction_region': 'resources/img/startReconstructionRegion.png',
            'start_reconstruction': 'resources/img/startReconstruction.png',
            'show_reconstruction_result': 'resources/img/showReconstructionResult.png',
            'reconstruction_result_region': 'resources/img/reconstructionResultRegion.png',
            '3d_show': 'resource/img/3dShow.png',
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
            'close': 'resources/img/close.png',
            'select_contour': 'resources/img/selectContour',
            'show_img': 'resources/img/show_img.png',
            'measure': 'resources/img/measure.png',
            "task_bar": 'resources/img/taskBar.png',
            "panel_measurement": 'resources/img/panelMeasurement.png',
            'panel_measurement_button': 'resources/img/panelMeasurementButton.png',
            'measurement_menu': 'resources/img/measurementMenu.png',
            'parallel_line': 'resources/img/parallelLine.png',
            'focus_bar': 'resources/img/focusBar.png',
            'show_bar': 'resources/img/showBar.png',
            'contour_menu': 'resources/img/contourMenu.png',
            'contour_parallel_line': 'resources/img/contourParallelLine.png',
            'average_contour': 'resources/img/averageContour.png',
            'quit_region': 'resources/img/quitRegion.png',
            'yes_button': 'resources/img/yesButton.png',
            'back_first_page': 'resources/img/backFirstPage.png'

        }

    # def findButton(self, buttonType, icon=None, getOut=None):
    #     try:
    #         # currentScreenshot=cv2.imread('resources4test/page01.png')
    #         currentScreenshot = self.currentScreen
    #         template01 = cv2.imread(self.allButtonsType[buttonType])
    #         template01_height, template01_width = template01.shape[:2]
    #         res01 = cv2.matchTemplate(currentScreenshot, template01, cv2.TM_SQDIFF)
    #         _, _, top_left01, _ = cv2.minMaxLoc(res01)
    #         bottom_right01 = (top_left01[0] + template01_width, top_left01[1] + template01_height)
    #         # print(f"the button pos is :{top_left01, bottom_right01}")
    #         getOut(f"the button pos is :{top_left01, bottom_right01}")
    #         if icon is not None:
    #             template02 = cv2.imread(self.allButtonsType[icon])
    #             roi = currentScreenshot[top_left01[1]:bottom_right01[1], top_left01[0]:bottom_right01[0]]
    #             template02_height, template02_width = template02.shape[:2]
    #             res02 = cv2.matchTemplate(roi, template02, cv2.TM_SQDIFF_NORMED)
    #             _, _, top_left02, _ = cv2.minMaxLoc(res02)
    #             bottom_right02 = (top_left02[0] + template02_width, top_left02[1] + template02_height)
    #             abs_top_left = (top_left01[0] + top_left02[0], top_left01[1] + top_left02[1])
    #             abs_bottom_right = (top_left01[0] + bottom_right02[0], top_left01[1] + bottom_right02[1])
    #             abs_icon_pos_x = (abs_top_left[0] + abs_bottom_right[0]) // 2
    #             abs_icon_pos_y = (abs_top_left[1] + abs_bottom_right[1]) // 2
    #             # print(f"the icon pos is :{abs_icon_pos_x, abs_icon_pos_y}")
    #             getOut(f"the icon pos is :{abs_icon_pos_x, abs_icon_pos_y}")
    #             return True, (abs_icon_pos_x, abs_icon_pos_y)
    #         else:
    #             abs_button_pos_x = (top_left01[0] + bottom_right01[0]) // 2
    #             abs_button_pos_y = (top_left01[1] + bottom_right01[1]) // 2
    #             # print(abs_button_pos_x, abs_button_pos_y)
    #             getOut(f"{abs_button_pos_x}, {abs_button_pos_y}")
    #             return True, (abs_button_pos_x, abs_button_pos_y)
    #     except cv2.error as e:
    #         getOut(f"ERROR: {e}")
    #         return False, f"An error occurred during image processing: {e}"

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

    def screenshot(self):
        # self.currentScreen = np.array(pyautogui.screenshot())[:, :, ::-1]
        self.currentScreen = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)

    def recordScreen(self, fileName):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        fps = 30
        print(fileName)
        out = cv2.VideoWriter("savedVideo/" + fileName + ".avi", fourcc, fps, (self.screenWidth, self.screenHeight))
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
            # self.screenshot()
            self.currentScreen = cv2.imread('resources4test/0171.png')
            img = self.currentScreen
            # lineRegion = img[:, :1440]
            # 这里改成了更改颜色通道来获取大致点，再获取对应的bbox
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
            top_left[1] = max(0, top_left[1])
            top_left[1] = min(1080, top_left[1])
            bottom_right[1] = max(0, bottom_right[1])
            bottom_right[1] = min(1080, bottom_right[1])

            self.lineRegionTopLeft = top_left
            self.lineRegionBottomRight = bottom_right
            getOut(f"current top left is: {top_left}, bottom right is: {bottom_right}")
            cv2.rectangle(img, top_left, bottom_right, (0, 255, 255), 3)
            cv2.imwrite("savedVideo/findLineTestResult.jpg", img)
            getOut(f"current line region pic saved at savedVideo dir")
            return top_left, bottom_right
        except Exception as e:
            getOut(f"{e}")
            return f"{e}"

    def getLineSharpness(self, getOut=None):
        # self.findLine()
        # self.screenshot()
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
                grayRegion = cv2.cvtColor(selectedRegion, cv2.COLOR_BGR2GRAY)
                # round用于舍到小数点后两位
                sharpness = round(cv2.Laplacian(grayRegion, cv2.CV_64F).var(), 2)
                self.sharpness = sharpness
                # cv2.imshow('1', selectedRegion)
                getOut(f"sharpness is:{sharpness}")
                return sharpness
        except Exception as e:
            getOut(f"ERROR:{e}")
            return f"{e}"

    def clickTest(self, getOut=None):
        res01 = self.click('focus_bar', 'focus_up', getOut)
        # getOut(f"res: {res01}")
        time.sleep(1)
        # res02 = self.click('focus_bar', 'focus_down02', getOut)
        # getOut(f"res: {res02}")
        return res01

    def focusOperationTest(self, getOut=None):
        try:
            # for i in range(15):
            #     self.click('focus_bar', 'focus_up')
            #     time.sleep(0.3)
            oldSharpness = self.getLineSharpness()
            delta = 0
            times = 0
            getOut(f"sharpness:{oldSharpness},delta:{delta}")
            while delta >= 0 or times < 20:
                self.click('focus_bar', 'focus_down02', getOut)
                time.sleep(0.3)
                self.getLineSharpness(getOut)
                delta = self.sharpness - oldSharpness
                oldSharpness = self.sharpness
                times += 1

            self.click('focus_bar', 'focus_up02', getOut)
            time.sleep(0.3)
            for j in range(3):
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

    def firstPageProgress(self):
        try:
            self.click("task_bar", "first_page")
            time.sleep(1)
            # 对焦
            focus_res = self.focusOperationTest()
            time.sleep(1)
            # 测量
            # measure_res = self.parallelLineMeasurementTest
            # time.sleep(1)
            # 重建按钮
            self.click("start_reconstruction_region", "start_reconstruction")
            time.sleep(5)
            self.click("show_reconstruction_result")
            # time.sleep(5)
            # self.click('reconstruction_result_region', '3d_show')
            # return focus_res, measure_res
            return focus_res
        except Exception as e:
            return e

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

    def secondPageProgress(self):
        try:
            # 先设置高度为0
            self.adjustHeightTest()
            # 再点击彩色/高度选项
            self.selectHeightOrColorTest()
            # 点击轮廓，进入后面的测量界面
            res = self.contourParallelLineSelectTest()
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

            coordWidth = 347.09
            pixelWidth = 1411 - 54
            widthScale = pixelWidth / coordWidth

            return f"{heightScale:.2f}", f"{widthScale:.2f}"
        except Exception as e:
            return e

    def getWidthHeightTest(self, getOut=None, getOut02=None):
        try:
            # self.screenshot()
            self.currentScreen = cv2.imread('resources4test/10.png')
            numberRegion = self.currentScreen[586:606, 1:40]
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
            _, binLine = cv2.threshold(grayLine, 50, 255, cv2.THRESH_BINARY)
            res = cv2.findNonZero(binLine)
            points = np.squeeze(res)
            # getOut(f"points:{points.shape}")
            x, y = np.split(points, 2, axis=1)
            # getOut(f"x:{x},y:{y}")
            x = np.squeeze(x)
            y = np.squeeze(y)

            peakIndex = np.argmin(y)
            height = (pixelHeight - y[peakIndex]) / heightScale
            getOut(f"height is: {height:.2f} μm")

            widthIndex = np.where(y == int(pixelHeight - 2 * heightScale))
            widthLeftIndex = widthIndex[0][0]
            for i in widthIndex[0]:
                if x[i] - x[widthLeftIndex] >= 100:
                    widthRightIndex = i
                    break
            width = (x[widthRightIndex] - x[widthLeftIndex]) / widthScale
            getOut(f"width is: {width:.2f} μm")
            getOut02(width, height)
            return width, height
        except Exception as e:
            getOut(f"ERROR: {e}")
            return e

    def thirdPageProgressTest(self):
        try:
            # 点击水平线
            self.screenshot()
            self.click('contour_menu', 'contour_parallel_line')
            # 选择平均轮廓
            time.sleep(1)
            self.click('average_contour', 'click_button02')
            time.sleep(1)
            pyautogui.click(1094, 172)
            # 波形检测
            res = self.getWidthHeightTest()
            return res
        except Exception as e:
            return e

    def moveTest(self, getOut=None):
        #   这里是向上移动的
        try:
            old_pos_topLeft = self.lineRegionTopLeft
            getOut(f"old top left pos: {old_pos_topLeft}")

            pyautogui.click(self.screenWidth // 2, self.screenHeight // 2)
            pyautogui.moveTo(self.screenWidth // 2, self.screenHeight // 4)
            time.sleep(0.5)
            pyautogui.dragRel(0, self.screenHeight // 2, 0.5, button='left')
            pyautogui.moveTo(self.screenWidth // 2, self.screenHeight // 4)
            time.sleep(0.5)
            pyautogui.dragRel(0, self.screenHeight // 2, 0.5)
            new_pos_topLeft, _ = self.findLine(getOut)
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

    def pipeLineTest01(self, getOut=None, getOut02=None):
        try:
            # /////////////////////////////////////////////////////////////
            # 第一页
            self.click('task_bar', 'first_page', getOut=getOut)
            self.findLine(getOut)
            self.focusOperationTest()
            self.click('start_reconstruction_region', 'start_reconstruction', getOut=getOut)
            time.sleep(4)
            self.click("show_reconstruction_result", getOut=getOut)
            time.sleep(5)
            self.click('reconstruction_result_region', '3d_show', getOut=getOut)
            time.sleep(3)

            # ////////////////////////////////////////////////////////////////
            # 第二页
            self.click('show_bar', 'select_contour', getOut=getOut)
            time.sleep(2)

            # /////////////////////////////////////////////////////////////////
            # 第三页
            self.click('contour_menu', 'contour_parallel_line', getOut=getOut)
            # 画面左上选线的高度区域为 【40，440】
            pyautogui.moveTo(1000, 40)
            # widthHeightList = [self.getWidthHeightTest(getOut=getOut,getOut02=getOut02)]
            for i in range(100):
                pyautogui.moveRel(0, 4)
                time.sleep(0.5)
                self.getWidthHeightTest(getOut=getOut, getOut02=getOut02)
                # getOut(res)
                # widthHeightList.append()

            pyautogui.click(1556, 337)
            time.sleep(0.5)
            self.click('contour_menu', 'contour_parallel_line', getOut=getOut)
            pyautogui.moveTo(1000, 40)

            avgWidthHeight = self.getWidthHeightTest(getOut=getOut, getOut02=getOut02)

            # //////////////////////////////////////////////////////////////////
            # 关闭
            pyautogui.click(1488, 1045)
            time.sleep(1)
            self.click('quit_region', 'yes_button')
            time.sleep(1)
            self.click('reconstruction_result_region', 'back_first_page')
            time.sleep(1)

            # //////////////////////////////////////////////////////////////////
            # 重新开始移动
            self.moveTest()
            return avgWidthHeight

        except Exception as e:
            return e
