import cv2
import numpy as np
import pyautogui

# 获取屏幕截图
# currentScreen = np.array(pyautogui.screenshot())

# 矩形框的左上角和右下角坐标
top_left01 = (100, 100)
bottom_right01 = (200, 200)

# 将屏幕截图转换为RGB格式
# currentScreen = cv2.cvtColor(currentScreen, cv2.COLOR_BGR2RGB)
currentScreen = np.array(pyautogui.screenshot())[:, :, ::-1]
# 在屏幕截图上绘制矩形框
cv2.rectangle(currentScreen, top_left01, bottom_right01, (255, 0, 0), 3)

# 显示绘制矩形框后的屏幕截图
cv2.imshow("result", currentScreen)
cv2.waitKey(0)
