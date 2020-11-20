
"""
Async IO Helpers.
"""

from typing import Callable, Optional
import os
import asyncio
import concurrent.futures


READ_LIMIT = 4 * 1024

FILE_DESCRIPTOR_CLOSED_ERROR_NUMBERS = (9,)
# 9 == bad file descriptor
#   This can happen when a handle has finished being read then the
#   next read is on the closed handle.


async def aio_fd_reader(
        file_desc: int, stream: asyncio.StreamReader, limit: int,
        loop: Optional[asyncio.AbstractEventLoop] = None,
) -> None:
    """Use the asyncio processing to read the file descriptor.  This is non-blocking,
    even though the underlying read is blocking.

    Due to the way Windows (and maybe other platforms) handle closing off file handlers
    when a process ends, this is specially set up to handle that situation, because that's
    the primary use case for this function.  That means if a bad file descriptor is
    passed in, the caller does not see an error.
    """
    if limit <= 0:
        limit = READ_LIMIT

    def read_func() -> Optional[bytes]:
        try:
            # print("[DEBUG] Reading data...")
            ret = os.read(file_desc, limit)
            # print("[DEBUG]  - read {0}".format(repr(ret)))
            return ret
        except OSError as err:
            if err.errno in FILE_DESCRIPTOR_CLOSED_ERROR_NUMBERS:
                return None
            raise err

    return await aio_reader(stream, read_func, loop)


async def aio_reader(
        stream: asyncio.StreamReader,
        read_func: Callable[[], Optional[bytes]],
        loop: Optional[asyncio.AbstractEventLoop] = None,
) -> None:
    """Use the asyncio processing to run the read loop.  The caller must provide
    the function that performs the read.  The loop only handles OSError exceptions,
    so anything else possibly raised by the read_func must be caught and reraised
    as an OSError.
    """
    if loop is None:
        run_loop = asyncio.get_event_loop()
    else:
        run_loop = loop

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

    while True:
        try:
            # print("aio_fd_reader: reading data in loop")
            data = await run_loop.run_in_executor(executor, read_func)
            # print("aio_fd_reader: read data", repr(data))
            if data:
                stream.feed_data(data)
            else:
                stream.feed_eof()
                break
        except EOFError:
            stream.feed_eof()
            break
        except OSError as err:
            stream.set_exception(err)
            break
