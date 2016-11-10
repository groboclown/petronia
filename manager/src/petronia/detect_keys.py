
from petronia.arch import funcs
from petronia.util.hotkey_chain import vk_to_names
import sys
import threading
import getpass


def shell_hook():
    handle = [None]

    down_keys = []

    def on_exit_callback():
        print("Quitting")
        funcs.shell__unhook(handle[0])
        sys.exit(0)

    # noinspection PyUnusedLocal
    def handler(vk_code, scan_code, is_key_up, is_injected):
        vk = "[{0}]".format(vk_to_str(vk_code))
        if is_key_up:
            if vk in down_keys:
                down_keys.remove(vk)
        else:
            if vk not in down_keys:
                down_keys.append(vk)
        print("<< {0} >>".format(" + ".join(down_keys)))

        # Raw output
        # print("{0} {1} ({2}){3}".format(
        #     vk_to_str(vk_code), is_key_up and "Up" or "Dn", hex(vk_code), is_injected and " Injected" or ""
        # ))
    handle[0] = funcs.shell__keyboard_hook(handler)

    # We could probably inject a quit notification into the pump messages function.
    funcs.shell__pump_messages(on_exit_callback)


def vk_to_str(vk):
    maps = vk_to_names(vk)
    if len(maps) <= 0:
        return "<unknown>"
    return ",".join(maps)


if __name__ == '__main__':
    # print("Warning: Ctrl+C won't normally exit.  You'll need to kill the python process with Task Manager.")
    # shell_hook()

    print("Press Ctrl+C to stop checking keys.")
    pump_thread = threading.Thread(
        target=shell_hook,
        daemon=True
    )
    pump_thread.start()

    # Hide stdin user input.
    # Otherwise, the keys are echoed out, and we see duplicate
    # values.
    while True:
        getpass.getpass("")

    sys.exit()
