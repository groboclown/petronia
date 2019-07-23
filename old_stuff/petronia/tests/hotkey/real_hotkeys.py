
from ctypes import windll, wintypes, byref
import threading
import sys


def hk_1():
    print("1 pressed")

HOTKEY_REGISTRATION = {

}


def register_hotkeys():
    hotkey_list = {}
    res = 1
    return hotkey_list


def unregister_hotkeys(hotkey_list):
    for hid in hotkey_list.keys():
        windll.user32.UnregisterHotKey(None, hid)


def hook_keyboard():
    hotkey_list = register_hotkeys()

    try:
        message = wintypes.MSG()
        while True:
            msg = windll.user32.GetMessageW(byref(message), 0, 0, 0)
            print("found message {0}".format(msg))
            if msg == -1:
                sys.exit(0)
            elif msg == 0:  # WM_QUIT
                sys.exit(0)
            else:
                windll.user32.TranslateMessage(byref(message))
                windll.user32.DispatchMessageW(byref(message))

    finally:
        unregister_hotkeys(hotkey_list)


if __name__ == '__main__':
    pump_thread = threading.Thread(
        target=hook_keyboard,
        daemon=False
    )
    pump_thread.start()
