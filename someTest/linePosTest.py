import cv2
import numpy as np
import imutils


def findLine(img):
    try:
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hsv_low = np.array([0, 0, 86])
        hsv_high = np.array([108, 255, 255])
        mask = cv2.inRange(imgHSV, hsv_low, hsv_high)

        lineRegion = cv2.bitwise_and(img, img, mask=mask)

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

        cv2.rectangle(img, top_left, bottom_right, (0, 255, 255), 3)
        cv2.imwrite("findLineTestResult.jpg", img)
        return top_left, bottom_right
    except Exception as e:
        return f"{e}"

img01 = cv2.imread('../resources4test/halfInLeft.png')
img02=cv2.imread('withoutLine.png')

res=findLine(img02)

if (res[1][0]-res[0][0])+(res[1][1]-res[1][0])<=1080:
    print(f"no line found")

if res[0][0]<=50:
    print(f'line in left edge')