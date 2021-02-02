
"""A test runner, launched by the process manager."""

import os
import sys
import platform


def main() -> None:
    """Main function"""
    print("Runner: Invoked with", sys.argv)
    event_read_fd = sys.stdin.fileno()
    event_write_fd = int(sys.argv[1])
    data_count = 2 ** 16
    # MyPy wants the sys version...
    # if platform.system() == 'Windows':
    if sys.platform == "win32":
        # On Windows, the file handle is passed in, not the fd.
        import msvcrt  # pylint: disable=import-outside-toplevel,import-error
        event_write_fd = msvcrt.open_osfhandle(event_write_fd, 0)

    event_write = os.fdopen(event_write_fd, 'wb')

    print("Runner: Reading data")
    data = os.read(event_read_fd, data_count)
    print("Runner: read data [{0}]; will write.".format(repr(data)))
    event_write.write(data)
    event_write.flush()
    event_write.close()
    print("Runner: exiting")


if __name__ == '__main__':
    main()
