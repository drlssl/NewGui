import cv2
#调用opencv库

x1 = cv2.imread('solar_panel05.png', cv2.IMREAD_GRAYSCALE)
#读取一张图片，并且把它灰度化处理

ret,x2=cv2.threshold(x1, 100, 255, cv2.THRESH_BINARY_INV)
#对已经灰度化的图片进行阈值化处理
inv=cv2.bitwise_not(x2)
inv[inv==0]=90
inv[inv==255]=250
cv2.imwrite('solar_panel06.png',inv)
cv2.imshow("name", inv)

cv2.waitKey(0)
#把图片展示出来
