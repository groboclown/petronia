
import sys
import codecs
from petronia.arch import funcs

# Allow outputting UTF-8 characters to the console
if sys.stdout.encoding != 'utf-8':
    # cp850
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')


# process_info_list = funcs.process__load_all_process_details()
service_info_list = funcs.process__get_all_service_information()


def get_process_name(hwnd):
    thread_pid = funcs.window__get_thread_process_id(hwnd)
    name = funcs.process__get_executable_filename(thread_pid)
    if name is not None:
        return name
    # for pinfo in process_info_list:
    #     if pinfo['ProcessId'] == str(thread_pid):
    #         return pinfo['CommandLine']
    for s_info in service_info_list:
        if s_info['process_id'] == thread_pid:
            return s_info['service_name']
    return None


# for pinfo in process_info_list:
#     print("{0}:{1}".format(pinfo['ProcessId'], pinfo['CommandLine']))


for monitor_details in funcs.monitor__find_monitors():
    print(str(monitor_details))

for window_handle in funcs.window__find_handles():
    pid = funcs.window__get_thread_process_id(window_handle)
    if funcs.window__is_visible(window_handle):
        print("+ {0} {1} {2}: [{3}]".format(
              pid,
              funcs.window__get_class_name(window_handle),
              get_process_name(window_handle),
              funcs.window__get_title(window_handle)))
    else:
        print("- {0} {1} {2}: [{3}]".format(
              pid,
              funcs.window__get_class_name(window_handle),
              get_process_name(pid),
              funcs.window__get_title(window_handle)))


def get_process_name(hwnd):
    return
    #try:
    #    return funcs.process__get_executable_filename(thread_pid)
    #except OSError as e:
    #    print(e)
    #    try:
    #        return funcs.window__get_module_filename(hwnd)
    #    except OSError as x:
    #        print(x)
    #        return "<<{0}>>".format(thread_pid)


# Note that this doesn't work for windows 7+ using slideshow wallpaper:
# http://stackoverflow.com/questions/8364758/get-handle-to-desktop-shell-window
progman_handle = funcs.window__find_handle_for_class_title('Progman', None)
if progman_handle is not None:
    print("Found the progman handle")

toolbar_handles = funcs.shell__get_task_bar_window_handles()
for hwnd in toolbar_handles:
    print("toolbar: {0} {1} {2} {3}".format(
        funcs.window__get_class_name(hwnd),
        funcs.window__get_title(hwnd),
        get_process_name(hwnd),
        funcs.window__get_visibility_states(hwnd)))

icons = funcs.shell__find_notification_icons()
for parent_hwnd in icons:
    print("{0}:".format(funcs.window__get_class_name(parent_hwnd)))
    #for child_hwnd in funcs.window__get_child_window_handles(parent_hwnd):
    #    print("  {0}".format(funcs.window__get_class_name(child_hwnd)))
# parents = []
# for i in range(len(icons)):
#     p = "+"
#     if i == 0:
#         p = "\\"
#     parents.append(["", p, icons[i]])
# while len(parents) > 0:
#     indent, sep, parent_hwnd = parents.pop()
#     children = funcs.window__get_child_window_handles(parent_hwnd)
#     if len(children) <= 0:
#         print("{0}{1}-- {2}".format(indent, sep, funcs.window__get_class_name(parent_hwnd)))
#     else:
#         print("{0}{1}-v {2}:".format(indent, sep, funcs.window__get_class_name(parent_hwnd)))
#         for i in range(len(children)):
#             p = "+"
#             if i == 0:
#                 p = "\\"
#             parents.append([indent + "   ", p, children[i]])
