import cv2

pic=cv2.imread('me.jpg')
resized=cv2.resize(pic, (413, 626),interpolation=cv2.INTER_AREA)
cv2.imwrite('resizedPic.jpg',resized)