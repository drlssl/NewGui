import cv2
import aircv as ac
import pyautogui
import numpy as np
import time


def findButton(roi, button):
    time.sleep(3)
    currentScreen = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
    roi_template = cv2.imread(roi)
    button_template = cv2.imread(button)

    # 找大框roi
    roi_res = ac.find_template(currentScreen, roi_template, threshold=0.8)
    if roi_res is not None:
        roi_pos = [roi_res['rectangle'][0], roi_res['rectangle'][3]]
        print(roi_pos)
        selectedScreen = currentScreen[
                         roi_pos[0][1]:roi_pos[1][1],
                         roi_pos[0][0]:roi_pos[1][0]
                         ]
        button_res = ac.find_template(selectedScreen,
                                      button_template,
                                      threshold=0.8)
        if button_res is not None:
            button_pos = button_res['result']
            print(f"button pos:{button_pos}")
            # print([button_res['rectangle'][0][0] + roi_res['rectangle'][0][0],
            # button_res['rectangle'][0][1] + roi_res['rectangle'][1][1]])
            abs_button_pos = [button_pos[0] + roi_pos[0][0],
                              button_pos[1] + roi_pos[0][1]]
            return True, abs_button_pos
        else:
            return False, roi_pos
    else:
        return False, roi_res


focus_bar_path = r'../resources/img/focusBar.png'
focus_down_path = r'../resources/img/focusUp.png'

ret, res = findButton(focus_bar_path, focus_down_path)
if ret:
    print(f"match successfully {res}")
    pyautogui.moveTo(res)
else:
    print(f"fail to match")
