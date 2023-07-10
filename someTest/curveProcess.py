import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt


def find_unique_index(sequence):
    unique_values = set(sequence)  # 获取序列中的唯一值
    index_dir = {}  # 存储不同值的索引字典
    for value in unique_values:
        index_dir[value] = [i for i, x in enumerate(sequence) if x == value]
    return index_dir


def stopRepeat(raw_array):
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


cv2.namedWindow('1', cv2.WINDOW_NORMAL)
pytesseract.pytesseract.tesseract_cmd = "D:\\Tesseract_OCR\\tesseract.exe"
# img = cv2.imread('measurePage.png')
img = cv2.imread('../resources4test/08.png')

numberRegion = img[586:606, 1:40]
lineRegion = img[595:992, 54:1411]

coord_height = float(pytesseract.image_to_string(numberRegion))
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
nonrepeat_x_list = []
nonrepeat_y_list = []
nonrepeat_index_list = []
nonrepeat_index_dir = find_unique_index(x)

for value, index in nonrepeat_index_dir.items():
    nonrepeat_index_list.append(index[0])

for norepeat_index in nonrepeat_index_list:
    nonrepeat_x_list.append(x[norepeat_index])
    nonrepeat_y_list.append(y[norepeat_index])

height_index = np.argmin(nonrepeat_y_list)
# print(f"point is {nonrepeat_x_list[height_index]},{nonrepeat_y_list[height_index]}")
# 先找左边
# ///////////////////////////////////////////////////////////////////////
left_index = height_index-50
current_left_height = nonrepeat_y_list[left_index]
current_left_res01 = 0
res02_left_list = []
while left_index >= 1:
    old_left_height = current_left_height
    old_left_res01 = current_left_res01
    current_left_height = nonrepeat_y_list[left_index]
    left_index -= 1
    current_left_res01 = old_left_height - current_left_height
    current_left_res02 = old_left_res01 - current_left_res01
    # print(current_left_res02)
    res02_left_list.append(current_left_res02)
res02_left_np = np.array(res02_left_list)
max_res02_left_index = np.argmax(res02_left_np)
left_width_index = height_index - max_res02_left_index - 50
# //////////////////////////////////////////////////////////////
# 找右边
right_index = height_index+50
current_right_height = nonrepeat_y_list[right_index]
current_right_res01 = 0
res02_right_list = []
while right_index < len(nonrepeat_y_list) -3:
    old_right_height = current_right_height
    old_right_res01 = current_right_res01
    current_right_height = nonrepeat_y_list[right_index]
    right_index += 1
    current_right_res01 = current_right_height - old_right_height
    current_right_res02 = current_right_res01 - old_right_res01
    # print(current_right_res02)
    res02_right_list.append(current_right_res02)
res02_right_np = np.array(res02_right_list)
min_res02_right_index = np.argmin(res02_right_np)
right_width_index = height_index + min_res02_right_index+53
# 求高
height=((nonrepeat_y_list[left_width_index]+nonrepeat_y_list[right_width_index])/2-nonrepeat_y_list[height_index])/heightScale

print(f"height is :{height:.2f} μm")



# 创建图形对象和子图
fig, ax = plt.subplots()
ax.plot(nonrepeat_x_list, nonrepeat_y_list)
ax.scatter(nonrepeat_x_list[left_width_index], nonrepeat_y_list[left_width_index], color='r')
ax.scatter(nonrepeat_x_list[right_width_index], nonrepeat_y_list[right_width_index], color='r')
ax.scatter(nonrepeat_x_list[height_index], nonrepeat_y_list[height_index], color='r')
ax.set_title('simple plot')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
# 显示图形
plt.show()

width = (nonrepeat_x_list[right_width_index] - nonrepeat_x_list[left_width_index]) / widthScale
print(f"the curve width is :{width:.2f}μm")

cv2.circle(img,
           (nonrepeat_x_list[left_width_index] + 54, nonrepeat_y_list[left_width_index] + 595),
           radius=3,
           color=(0, 0, 255),
           thickness=3)

cv2.circle(img,
           (nonrepeat_x_list[right_width_index] + 54, nonrepeat_y_list[right_width_index] + 595),
           radius=3,
           color=(0, 0, 255),
           thickness=3)

cv2.imshow('1', img)
cv2.waitKey()

cv2.destroyAllWindows()
