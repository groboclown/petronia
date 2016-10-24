
from petronia.arch import funcs

if __name__ == '__main__':
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
        if info['visible']:
            print(str(info))
