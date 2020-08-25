
"""The process handler."""

from typing import Iterable, Callable
import asyncio
import os
import shutil


class ManagedProcess:
    """The process handler."""
    __slots__ = ('__ident', '__reader', '__tmp_resources')

    def __init__(
            self,
            ident: str,
            reader: asyncio.StreamReader,
            temp_files: Iterable[str],
    ) -> None:
        self.__ident = ident
        self.__reader = reader
        self.__tmp_resources = list(temp_files)

    @property
    def ident(self) -> str:
        """Identity of this process, for use as its target and source ID."""
        return self.__ident

    @property
    def reader(self) -> asyncio.StreamReader:
        """The event reader stream from the process."""
        return self.__reader

    def write(self, data: bytes) -> None:
        """Act as a Binary Writer"""
        raise NotImplementedError()

    def close_writer(self) -> None:
        """Close the writer stream.  This is usually used as a soft signal to the child process
        to terminate."""
        raise NotImplementedError()

    def stop(self) -> None:
        """Stop the running process."""
        raise NotImplementedError()

    async def watch_process(self, on_exit_cb: Callable[[int], None]) -> None:
        """Watch the process."""
        raise NotImplementedError()

    def _close(self) -> None:
        for temp_dir in self.__tmp_resources:
            if os.path.isdir(temp_dir):
                shutil.rmtree(temp_dir)
            self.__tmp_resources.clear()

        self.__reader.feed_eof()
