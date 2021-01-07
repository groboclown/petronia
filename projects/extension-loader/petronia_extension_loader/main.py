"""Main Entry Point."""

from typing import Sequence
import os
import sys
from petronia_common.event_stream.arg_handle import (
    get_fd_from_argument,
    get_fd_reader, get_fd_writer,
)
from .entrypoint import entrypoint


def main(args: Sequence[str]) -> int:
    """Extension loader CLI entry."""
    event_read_fd = sys.stdin.fileno()
    event_write_fd_res = get_fd_from_argument(args[0])
    if event_write_fd_res.has_error:
        for msg in event_write_fd_res.error_messages():
            sys.stderr.write('{0}\n'.format(msg.debug()))
        return 1
    event_write = get_fd_writer(event_write_fd_res.result)
    event_read = get_fd_reader(event_read_fd)
    try:
        entrypoint(event_read, event_write)
    finally:
        event_write.close()
        event_read.close()
    return 0
