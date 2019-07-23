
from petronia.system.bus import Bus
from petronia.config import load_config
from petronia.shell.native.windows_hook_event import WindowsHookEvent
from petronia.arch import funcs

import sys
import threading


def shell_hook():
    handle = [None]

    def on_exit_callback():
        funcs.shell__unhook(handle[0])
        sys.exit(0)

    def message_pumper():
        def handler(vk_code, scan_code, is_key_up, is_injected):
            print("{0} {1} {2} {3}".format(hex(vk_code), hex(scan_code), is_key_up and "Up" or "Dn", is_injected and "Injected" or "Natural"))
        print("Hooking")
        handle[0] = funcs.shell__keyboard_hook(handler)
        print("pumping")
        funcs.shell__pump_messages(on_exit_callback)

    pump_thread = threading.Thread(
        target=message_pumper,
        daemon=False
    )
    pump_thread.start()


if __name__ == '__main__':
    shell_hook()

    # config = load_config()
    # bus = Bus()
    # whe = WindowsHookEvent(bus, config)
    # sys.stdin.read()
