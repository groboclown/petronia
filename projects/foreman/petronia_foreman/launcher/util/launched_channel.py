"""Per launcher or channel launched handler helpers."""

from typing import Tuple, Sequence, Callable
from petronia_common.util import StdRet, RET_OK_NONE, EMPTY_TUPLE
from petronia_common.event_stream import BinaryReader, BinaryWriter
from ..abc import RuntimeContext
from ...configuration import LauncherConfig
from ...configuration.launcher_parameters import (
    is_boot_launcher, get_stop_timeout, get_boot_launcher_produces,
)


class LaunchedInstance:
    """Wrapper for the information used to interact with a launched instance."""
    __slots__ = (
        '_launcher_id', '_boot_launcher', '_reader', '_writer', '_stopper',
        '_timeout', '_boot_events',
    )

    def __init__(  # pylint:disable=too-many-arguments
            self,
            launcher_id: str,
            options: LauncherConfig,
            reader: BinaryReader,
            writer: BinaryWriter,
            stopper: Callable[[float], StdRet[None]],
    ) -> None:
        self._launcher_id = launcher_id
        self._boot_launcher = is_boot_launcher(options.options)
        self._boot_events: Sequence[str] = get_boot_launcher_produces(options.options)
        self._reader = reader
        self._writer = writer
        self._stopper = stopper
        self._timeout = get_stop_timeout(options.options)

    @property
    def launcher_id(self) -> str:
        """The launcher's ID."""
        return self._launcher_id

    @property
    def is_boot_launcher(self) -> bool:
        """Is this launched instance classified as a boot launcher?"""
        return self._boot_launcher

    @property
    def events_launcher_produces(self) -> Sequence[str]:
        """Get all the events the launcher itself produces.  This only has
        meaning for boot launchers."""
        return self._boot_events

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

    def post_launch_processing(self, context: RuntimeContext) -> StdRet[None]:
        """Run additional processing after the launch."""
        res = RET_OK_NONE
        if self.is_boot_launcher:
            res = context.register_channel(
                self.launcher_id,
                self.as_channel_res,
            )
            if res.has_error:
                # Close off our process
                res_stop = self.stop()
                if res_stop.has_error:
                    res = StdRet.pass_error(res.valid_error, res_stop.valid_error)
            else:
                context.add_handler(
                    self.launcher_id, self._launcher_id,
                    self.events_launcher_produces, EMPTY_TUPLE,
                )
        return res

    def stop(self) -> StdRet[None]:
        """Attempt to stop the launched."""
        return self._stopper(self._timeout)
