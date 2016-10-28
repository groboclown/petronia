
from petronia.arch import funcs
from petronia.util.hotkey_chain import STR_VK_MAP


def shell_hook():
    handle = [None]

    def on_exit_callback():
        print("Quitting")
        funcs.shell__unhook(handle[0])
        exit(0)

    def handler(vk_code, scan_code, is_key_up, is_injected):
        print("{0} {1} ({2}){3}".format(
            vk_to_str(vk_code), is_key_up and "Up" or "Dn", hex(vk_code), is_injected and " Injected" or ""
        ))
    handle[0] = funcs.shell__keyboard_hook(handler)

    # We could probably inject a quit notification into the pump messages function.
    funcs.shell__pump_messages(on_exit_callback)


def vk_to_str(vk):
    maps = []
    for vk_str, code in STR_VK_MAP.items():
        # There are multiple mappings; return them all.
        if code == vk:
            maps.append(vk_str)
    if len(maps) <= 0:
        return "<unknown>"
    return ",".join(maps)

if __name__ == '__main__':
    print("Warning: Ctrl+C won't normally exit.  You'll need to kill the python process with Task Manager.")
    shell_hook()
