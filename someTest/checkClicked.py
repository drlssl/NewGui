import cv2
import aircv as ac
import pyautogui
import numpy as np
import time


def ifClicked():
    currentScreen = cv2.imread('../resources4test/10.png')
    roi_template = cv2.imread('../resources4test/averageContourFont.png')
    click_template_list = [
        '../resources4test/click01.png',
        '../resources4test/click02.png'
    ]
    # 先模板匹配得到字的区域
    roi_res = ac.find_template(currentScreen, roi_template, threshold=0.8)
    cv2.rectangle(currentScreen,
                  roi_res['rectangle'][0],
                  roi_res['rectangle'][3],
                  (0, 255, 0),
                  thickness=1
                  )
    cv2.imwrite('1.jpg', currentScreen)
    # 根据这个区域得到框的区域
    if roi_res is not None:
        box_top_left = [roi_res['rectangle'][0][0] - 20,
                        roi_res['rectangle'][0][1]]
        box_bottom_right = [roi_res['rectangle'][0][0],
                            roi_res['rectangle'][0][1] + 20]

        box_region = currentScreen[
                     box_top_left[1]:box_bottom_right[1],
                     box_top_left[0]:box_bottom_right[0]
                     ]
        cv2.imwrite('2.jpg', box_region)
        index = 0
        while index < 2:
            # 对框进行一个匹配
            click_template = cv2.imread(click_template_list[index])
            click_res = ac.find_template(box_region, click_template, threshold=0.8)
            if click_res is not None:
                click_pos = [
                    click_res['result'][0] + box_top_left[0],
                    click_res['result'][1] + box_top_left[1]
                ]
                int_click_pos = [int(pos) for pos in click_pos]
                cv2.circle(currentScreen, int_click_pos, 2, (255, 0, 0), 2)
                cv2.imwrite('3.jpg', currentScreen)
                break
            else:
                index += 1

        if index == 0:
            print(f"not click yet")
        elif index == 1:
            print(f"clicked")
        else:
            print(f"cannot recognize click box")
    else:
        print('cannot find the region')


ifClicked()
