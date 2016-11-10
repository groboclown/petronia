
from ...util import worker_thread
from ...arch import funcs
from ...arch.windows_constants import *
import time
import threading
import sys
import _thread


def shutdown_system():
    worker_thread.stop_all_threads()
    _thread.interrupt_main()
    current_pid = funcs.process__get_current_pid()
    matched = False
    for hwnd in funcs.window__find_handles():
        pid = funcs.window__get_process_id(hwnd)
        if pid == current_pid:
            print("Sending PostMessage to hwnd owned by {0}".format(pid))
            funcs.window__post_message(hwnd, WM_QUIT, 0, 0)
            matched = True
            # Continue in case there are more windows we own
    if not matched:
        time.sleep(0.1)
        # print("DEBUG could not find a window to post a quit to.  Forcing quit.")
        # for t in threading.enumerate():
        #     print("Running thread: {0}".format(t))
        sys.exit()
