import sys
import time

from pynput import keyboard


# 我的想法，开辟一个线程，监听按键，按键后，把flag改成false，然后程序停止
# 想的是直接在main这里做手脚

def on_release(key):
    """定义释放时候的响应"""
    global flag
    if key == keyboard.Key.esc:
        print(f"quit !")
        flag = False

    print(f'{key}')


def listen_quitKey():
    listener = keyboard.Listener(
        on_release=on_release
    )
    listener.start()  # 启动线程


if __name__ == '__main__':
    listen_quitKey()
    global flag
    flag = True
    i = 0
    while flag:
        print(i)
        i += 1
        time.sleep(1)

    print(0)
