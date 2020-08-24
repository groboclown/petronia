
"""A test runner, launched by the process manager."""

import os
import sys
import platform

print("Runner: Invoked with", sys.argv)
event_read = sys.stdin
event_write_fd = int(sys.argv[1])
if platform.system() == 'Windows':
    # On Windows, the file handle is passed in, not the fd.
    import msvcrt
    event_write_fd = msvcrt.open_osfhandle(event_write_fd, 0)

event_write = os.fdopen(event_write_fd, 'wb')

print("Runner: Reading data")
data = event_read.read()
print("Runner: read data [{d}]".format(d=data))
event_write.write(data)
os.close(event_write_fd)
print("Runner: exiting")