
import sys
import codecs
import time
from petronia.arch.windows import funcs

def _rect_str(rect):
    return "({left},{top}) -> ({right},{bottom})".format(**rect)


def describe_hwnd(window_handle, indent=""):    
    pid = funcs.window__get_process_id(window_handle)
    print("{0}{1} {2} [{3}] {4}: [{5}] {6}".format(
        funcs.window__is_visible(window_handle) and "V" or "H",
        indent,
        pid.value,
        funcs.window__get_class_name(window_handle),
        funcs.process__get_executable_filename(window_handle),
        funcs.window__get_title(window_handle),
        _rect_str(funcs.window__border_rectangle(window_handle))
    ))


def inspect_child_windows(parent_hwnd, indent="    ", follow_children=False):
    for hwnd in funcs.window__get_child_window_handles(parent_hwnd):
        describe_hwnd(hwnd, indent)
        if follow_children or funcs.window__get_class_name(hwnd) == 'Windows.UI.Core.CoreWindow':
            inspect_child_windows(hwnd, indent + "    ", True)


def inspect_process(pid):
    name = funcs.process__get_executable_filename(pid)
    hwnds = funcs.window__get_thread_window_handles(pid)
    if len(hwnds) > 0:
        print("{0} - {1} ->".format(pid, name))
        for hwnd in hwnds:
            describe_hwnd(hwnd)
            inspect_child_windows(hwnd)
    else:
        print("{0} - {1} -> no windows".format(pid, name))

    
if __name__ == '__main__':
    # Allow outputting UTF-8 characters to the console
    if sys.stdout.encoding != 'utf-8':
        # cp850
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    
    time.sleep(3.0)
    funcs.shell__open_start_menu(True)

    for window_handle in funcs.window__find_handles():
        describe_hwnd(window_handle)
        inspect_child_windows(window_handle)
    
    for pid in funcs.process__get_all_pids():
        inspect_process(pid)


    # toolbar_handles = funcs.shell__get_task_bar_window_handles()
    # for hwnd in toolbar_handles:
    #     print("toolbar: {0} {1} {2} {3}".format(
    #         funcs.window__get_class_name(hwnd),
    #         funcs.window__get_title(hwnd),
    #         funcs.process__get_executable_filename(hwnd),
    #         funcs.window__get_visibility_states(hwnd)))
    # 
    # icons = funcs.shell__find_notification_icons()
    # for parent_hwnd in icons:
    #     print("{0}:".format(funcs.window__get_class_name(parent_hwnd)))
