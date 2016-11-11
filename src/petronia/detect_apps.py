
from petronia.arch import funcs
import io
import sys

if __name__ == '__main__':
    # Until Python 3.6 comes out, which supposedly supports Windows output
    # in UTF-8
    out = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    invisible_handles = {}
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
            pos = funcs.window__border_rectangle(hwnd)
            for key, val in pos.items():
                info[key] = val
            out.write(("Window Handle {hwnd}, PID {pid.value}\n" +
                       "    exec_path: {exec_filename}\n" +
                       "    module_path: {module_filename}\n" +
                       "    class_name: {class}\n" +
                       "    title: {title}\n" +
                       "    @ ({left}x{top}) -> ({right}x{bottom})\n\n").format(**info))
        else:
            if info['pid'].value not in invisible_handles:
                invisible_handles[info['pid'].value] = (info['exec_filename'], [])
            invisible_handles[info['pid'].value][1].append(str(hwnd))

    # for pid, x in invisible_handles.items():
    #     filename, handles = x
    #     out.write("PID {0}, {3} handles :: {1}\n".format(pid, filename, ", ".join(handles), len(handles)))

    out.flush()
