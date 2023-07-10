# import cv2
# import numpy as np
# import pyautogui
#
# # 获取屏幕截图
# # currentScreen = np.array(pyautogui.screenshot())
#
# # 矩形框的左上角和右下角坐标
# top_left01 = (100, 100)
# bottom_right01 = (200, 200)
#
# # 将屏幕截图转换为RGB格式
# # currentScreen = cv2.cvtColor(currentScreen, cv2.COLOR_BGR2RGB)
# currentScreen = np.array(pyautogui.screenshot())[:, :, ::-1]
# # 在屏幕截图上绘制矩形框
# cv2.rectangle(currentScreen, top_left01, bottom_right01, (255, 0, 0), 3)
#
# # 显示绘制矩形框后的屏幕截图
# cv2.imshow("result", currentScreen)
# cv2.waitKey(0)
import matplotlib.pyplot as plt

data = [
    (30.18, 8.52),
    (31.22, 8.22),
    (30.73, 7.99),
    (33.22, 8.53),
    (33.45, 8.24),
    (32.12, 9.41),
    (32.65, 8.76),
    (31.98, 9.01),
    (33.78, 8.87),
    (31.59, 8.88),
    (33.01, 8.67),
    (31.59, 8.93)
]

x = [point[0] for point in data]
y = [point[1] for point in data]

plt.scatter(x, y)
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.title('数据散点图')
plt.show()
