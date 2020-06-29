
import sys
import io
from petronia.arch import funcs, windows_constants


if __name__ == '__main__':
    out = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    app_class = sys.argv[1]
    dx = int(sys.argv[2])
    dy = int(sys.argv[3])

    hwnd_list = funcs.window__find_handles()
    for hwnd in hwnd_list:
        module_filename = funcs.window__get_module_filename(hwnd)
        pid = funcs.window__get_process_id(hwnd)
        exec_filename = funcs.process__get_executable_filename(pid)
        info = {
            'hwnd': hwnd,
            'title': funcs.window__get_title(hwnd),
            'class': funcs.window__get_class_name(hwnd),
            'module_filename': module_filename,
            'exec_filename': exec_filename,
            'pid': pid,
            'visible': funcs.window__is_visible(hwnd),
        }
        if info['visible'] and info['class'] == app_class:
            pos = funcs.window__border_rectangle(hwnd)
            ret = funcs.window__set_position(
                    hwnd, None, pos['x'] + dx, pos['y'] + dy, pos['width'] + 4, pos['height'] + 4,
                    ['frame-changed', 'draw-frame', 'async-window-pos'])
            if not ret:
                out.write(" - Error setting position.")
            ret = funcs.window__activate(hwnd)
            if not ret:
                out.write(" - Error activating window.")
    out.flush()
