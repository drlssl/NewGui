import cv2
import numpy as np
import pytesseract

cv2.namedWindow('1', cv2.WINDOW_NORMAL)

pytesseract.pytesseract.tesseract_cmd = "D:\\Tesseract_OCR\\tesseract.exe"
img = cv2.imread("../resources4test02/01/00032.bmp")
numberRegion = img[1002:1023, 6:40]
lineRegion = img[595:992, 54:1411]

ocr01=pytesseract.image_to_string(numberRegion)
print(ocr01)

# coord_height = float(pytesseract.image_to_string(numberRegion))
# pixel_height = 992 - 595
# heightScale = pixel_height / coord_height
# print(f"scale of height is {heightScale:.2f}")
#
# coord_width = 347.09
# pixel_width = 1411 - 54
# widthScale = pixel_width / coord_width
# print(f"scale of width is {widthScale:.2f}")