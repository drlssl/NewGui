import cv2
import numpy as np
import imutils


def findLine(currentScreen):
    img = currentScreen
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

    # lineRegionTopLeft = top_left
    # lineRegionBottomRight = bottom_right

    cv2.rectangle(img, top_left, bottom_right, (0, 255, 255), 3)
    cv2.imshow('1', img)
    cv2.waitKey()
    cv2.destroyAllWindows()

    return top_left, bottom_right


def calculate_blur_sobel(img):
    # 将图像转换为灰度图
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    grad = np.sqrt(sobelx ** 2 + sobely ** 2)
    score = np.average(grad)
    return score


def getLineSharpness(currentScreen, lineRegionTopLeft, lineRegionBottomRight):
    try:
        if lineRegionTopLeft == 0:
            return f"please find the line firstly"
        else:
            selectedRegion = currentScreen[
                             lineRegionTopLeft[1]: lineRegionBottomRight[1],
                             lineRegionTopLeft[0]: lineRegionBottomRight[0]
                             ]
            grayRegion = cv2.cvtColor(selectedRegion, cv2.COLOR_BGR2GRAY)
            # round用于舍到小数点后两位
            # sharpness = round(cv2.Laplacian(grayRegion, cv2.CV_64F).var(), 2)
            sharpness = round(calculate_blur_sobel(grayRegion), 2)
            # sharpness = sharpness
            # cv2.imshow('1', selectedRegion)
            return sharpness
    except Exception as e:
        print(f"{e}")
        return f"{e}"


path_list = ['../resources4test/0019.png',
             '../resources4test/0171.png',
             '../resources4test/0174.png',
             '../resources4test/3330.png',
             ]

path_prefix = "I:\\microscope\\res01\\savedVideo\\pic\\"

currentScreen = cv2.imread('I:\\microscope\\res01\\savedVideo\\pic\\1.png')
# currentScreen = cv2.imread('../resources4test/0171.png')
topLeft, bottomRight = findLine(currentScreen)

for i in range(1, 75):
    path = f"{path_prefix}{i}.png"
    currentScreen = cv2.imread(path)
    sharpness = getLineSharpness(currentScreen, topLeft, bottomRight)
    print(f"sharpness of{path} is that:{sharpness}")
