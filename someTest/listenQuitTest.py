import sys

from pynput import keyboard


def on_release(key):
    global flag
    """定义释放时候的响应"""
    if key == "'q'":
        print(f"quit !")
        sys.exit(0)
    print(f'{key}')


def listen_quitKey():
    listener = keyboard.Listener(
        # on_press=on_press,
        on_release=on_release
    )
    listener.start()  # 启动线程


if __name__ == '__main__':
    listen_quitKey()
    global flag
    flag = True
    while flag:
        pass

    print(0)
