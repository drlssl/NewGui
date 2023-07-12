import cv2
import numpy as np
import pytesseract

cv2.namedWindow('1', cv2.WINDOW_NORMAL)

pytesseract.pytesseract.tesseract_cmd = "D:\\Tesseract_OCR\\tesseract.exe"
# img = cv2.imread('measurePage.png')
img = cv2.imread('../resources4test/0025.bmp')
# img = cv2.imread("../resources4test02/01/00032.bmp")

numberRegion = img[586:606, 1:40]
lineRegion = img[595:992, 54:1411]

coord_height = float(pytesseract.image_to_string(numberRegion))
print(f"coord height is {coord_height}")
pixel_height = 992 - 595
heightScale = pixel_height / coord_height
print(f"scale of height is {heightScale:.2f}")

coord_width = 347.09
pixel_width = 1411 - 54
widthScale = pixel_width / coord_width
print(f"scale of width is {widthScale:.2f}")

grayLine = cv2.cvtColor(lineRegion, cv2.COLOR_BGR2GRAY)
_, binLine = cv2.threshold(grayLine, 50, 255, cv2.THRESH_BINARY)
res = cv2.findNonZero(binLine)
points = np.squeeze(res)
x, y = np.split(points, 2, axis=1)
x = np.squeeze(x)
y = np.squeeze(y)

widthIndex = np.where(y == int(pixel_height - 2 * heightScale))

# widthIndex is a tuple likes ([],array)
widthLeftIndex = widthIndex[0][0]
for i in widthIndex[0]:
    if x[i] - x[widthLeftIndex] >= 100:
        widthRightIndex = i
        break

width = (x[widthRightIndex] - x[widthLeftIndex]) / widthScale
print(f"the curve width is :{width:.2f}μm")

cv2.circle(img, (x[widthLeftIndex] + 54, y[widthLeftIndex] + 595), radius=2, color=(0, 255, 0),
           thickness=3)

cv2.circle(img, (x[widthRightIndex] + 54, y[widthRightIndex] + 595), radius=2, color=(0, 255, 0),
           thickness=3)

cv2.imshow('1', img)
cv2.waitKey()

cv2.destroyAllWindows()
