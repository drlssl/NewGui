import cv2
import numpy as np
import imutils


def findLine(img, name):
    try:
        # self.screenshot()
        # self.currentScreen = cv2.imread('resources4test02/04/1.bmp')
        # img = self.currentScreen

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
        # getOut(f"top left is {top_left}")
        # getOut(f"bottom right is {bottom_right}")

        cv2.namedWindow('1', cv2.WINDOW_NORMAL)
        cv2.rectangle(img, top_left, bottom_right, (0, 255, 255), 3)
        cv2.imshow('1', img)
        cv2.imwrite(f"findLineTest/{name}", img)
        cv2.waitKey()



        if (bottom_right[0] - top_left[0] + bottom_right[1] - top_left[1]) <= 1080:
            # getOut(f"cannot find the line")
            return top_left, bottom_right, 0
        elif top_left[0] <= 50:
            # getOut(f"the line located at the left edge")
            # getOut(f"should move it right more")
            print("不合格")
            return top_left, bottom_right, 0
        elif bottom_right[0] - top_left[0] < 80 or bottom_right[0] - top_left[0] > 500 or bottom_right[1] - top_left[
            1] < 900:
            print("不合格")

        else:
            print("合格")
            # self.lineRegionTopLeft = top_left
            # self.lineRegionBottomRight = bottom_right
            # getOut(f"find the line")
            # getOut(f"current top left is: {top_left}, bottom right is: {bottom_right}")
            # cv2.rectangle(img, top_left, bottom_right, (0, 255, 255), 3)
            # cv2.imwrite("savedVideo/findLineTestResult.jpg", img)
            # getOut(f"current line region pic saved at savedVideo dir")
            return top_left, bottom_right, 1
    except Exception as e:
        # getOut(f"{e}")
        return f"{e}"


imgPrefix = r'../resources4test02/crossPoint'

for i in range(1, 22):
    imgPath = imgPrefix + f"/{i}.bmp"
    img = cv2.imread(imgPath)
    findLine(img, f"{i}.bmp")
