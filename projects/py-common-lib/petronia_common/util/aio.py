
"""
Async IO Helpers.
"""

from typing import Optional
import os
import asyncio


READ_LIMIT = 4 * 1024


async def aio_fd_reader(
        file_desc: int, stream: asyncio.StreamReader, limit: int,
        loop: Optional[asyncio.AbstractEventLoop] = None,
) -> None:
    """Use the asyncio processing to read the file descriptor.  This is non-blocking."""
    if loop is None:
        run_loop = asyncio.get_event_loop()
    else:
        run_loop = loop

    while True:
        try:
            print("aio_fd_reader: reading data in loop")
            data = await run_loop.run_in_executor(None, lambda: os.read(file_desc, limit))
            print("aio_fd_reader: read data", repr(data))
            if data:
                stream.feed_data(data)
            else:
                stream.feed_eof()
                break
        except OSError:
            stream.feed_eof()
            break
