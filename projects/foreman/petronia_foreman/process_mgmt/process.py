
"""The process handler."""

from typing import Iterable, List, Coroutine, Callable, Any
import asyncio
import os
import shutil
from petronia_common.event_stream import BinaryWriter
from petronia_common.util.aio import FdStreamReader


class ManagedProcess:
    """The process handler."""
    __slots__ = ('__ident', '__reader', '__writer', '__tmp_resources')

    def __init__(
            self,
            ident: str,
            reader: asyncio.StreamReader,
            writer: BinaryWriter,
            temp_files: Iterable[str],
    ) -> None:
        self.__ident = ident
        self.__reader = reader
        self.__writer = writer
        self.__tmp_resources = list(temp_files)

    @property
    def ident(self) -> str:
        """Identity of this process, for use as its target and source ID."""
        return self.__ident

    @property
    def reader(self) -> asyncio.StreamReader:
        """The event reader stream from the process."""
        return self.__reader

    @property
    def writer(self) -> BinaryWriter:
        """The event writer stream for the process"""
        return self.__writer

    def stop(self) -> None:
        """Stop the running process."""
        raise NotImplementedError()

    def get_watchers(
            self,
            on_exit_cb: Callable[[int], None],
    ) -> List[Coroutine[Any, Any, None]]:
        ret: List[Coroutine[Any, Any, None]] = [
            self.watch_process(on_exit_cb),
        ]
        if isinstance(self.__reader, FdStreamReader):
            ret.append(self.__reader.run_reader())
        return ret

    async def watch_process(self, on_exit_cb: Callable[[int], None]) -> None:
        """Watch the process."""
        raise NotImplementedError()

    def _close(self) -> None:
        for temp_dir in self.__tmp_resources:
            if os.path.isdir(temp_dir):
                shutil.rmtree(temp_dir)
            self.__tmp_resources.clear()

        self.__reader.feed_eof()
