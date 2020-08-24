
"""
Async IO Helpers.
"""

from typing import Optional
import os
import asyncio


READ_LIMIT = 4 * 1024


class FdStreamReader(asyncio.StreamReader):
    """A stream reader for file descriptors."""

    def __init__(
            self, fd: int, limit: int = READ_LIMIT,
            loop: Optional[asyncio.AbstractEventLoop] = None,
    ) -> None:
        asyncio.StreamReader.__init__(self, limit=limit, loop=loop)
        self._fd = fd
        self._running = True

    def __del__(self) -> None:
        self.feed_eof()

    async def run_reader(self) -> None:
        """The background runner for reading the input."""
        while self._running:
            await self._loop.run_in_executor(None, self._on_read_ready)

    def feed_eof(self) -> None:
        asyncio.StreamReader.feed_eof(self)
        if self._fd >= 0:
            os.close(self._fd)
            self._fd = -1
            self._running = False

    def _on_read_ready(self) -> None:
        data = os.read(self._fd, self._limit)
        if len(data) <= 0:
            self.feed_eof()
        else:
            self.feed_data(data)
