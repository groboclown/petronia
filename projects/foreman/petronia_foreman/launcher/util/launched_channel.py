"""Per launcher or channel launched handler helpers."""

from typing import Tuple, Callable
from petronia_common.util import StdRet
from petronia_common.event_stream import BinaryReader, BinaryWriter
from ...configuration import RuntimeConfig
from ...configuration.runtime_parameters import get_stop_timeout


class LaunchedInstance:
    """Wrapper for the information used to interact with a launched instance."""
    __slots__ = (
        '_launcher_id', '_reader', '_writer', '_stopper', '_timeout',
    )

    def __init__(  # pylint:disable=too-many-arguments
            self,
            launcher_id: str,
            options: RuntimeConfig,
            reader: BinaryReader,
            writer: BinaryWriter,
            stopper: Callable[[float], StdRet[None]],
    ) -> None:
        self._launcher_id = launcher_id
        self._reader = reader
        self._writer = writer
        self._stopper = stopper
        self._timeout = get_stop_timeout(options.options)

    @property
    def launcher_id(self) -> str:
        """The launcher's ID."""
        return self._launcher_id

    @property
    def reader(self) -> BinaryReader:
        """The read stream"""
        return self._reader

    @property
    def writer(self) -> BinaryWriter:
        """The write stream"""
        return self._writer

    def as_channel_res(self) -> StdRet[Tuple[BinaryReader, BinaryWriter]]:
        """Convert this value into a channel registration result."""
        return StdRet.pass_ok((self._reader, self._writer))

    def stop(self) -> StdRet[None]:
        """Attempt to stop the launched."""
        return self._stopper(self._timeout)
