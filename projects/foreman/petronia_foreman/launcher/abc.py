"""
Abstract class for all launchers.

The "runtime" definition on an extension determines which extension runner to use.  The
extension runner selects a launcher on its own.  This means there is no longer the 2-part
extension start chain, which is really complex and error-prone.  Instead, an event is sent
to foreman to start an extension (along with the necessary extension metadata + configuration
data), then foreman starts the registered extension runner (specified in the foreman configuration),
and that runner does the process start (if necessary) and extension loading.
"""

from typing import Tuple, Sequence, Iterable, Callable
from petronia_common.event_stream import BinaryWriter, BinaryReader
from petronia_common.util import StdRet
from ..configuration.runtime import RuntimeConfig
from ..configuration.runtime_parameters import RuntimeLauncherOptions
from ..events import foreman
from ..event_router.handler import EventTargetHandle
from ..event_router.channel import InternalEventHandler


class RuntimeContext:
    """Context used by a launcher category to handle events to/from the launcher."""
    __slots__ = ()

    def register_channel(
            self,
            name: str,
            channel_creator: Callable[
                [],
                StdRet[Tuple[BinaryReader, BinaryWriter]],
            ],
    ) -> StdRet[None]:
        """Creates the channel.  The name must be unique."""
        raise NotImplementedError()

    def close_channel(self, name: str) -> bool:
        """Closes the channel."""
        raise NotImplementedError()

    def add_handler(
            self, channel_name: str, handler_id: str,
            produces: Iterable[str], consumes: Iterable[EventTargetHandle],
            source_id_prefixes: Iterable[str],
    ) -> StdRet[None]:
        """Adds the handler to the channel with the given name.  If the
        handler ID is registered anywhere, or the channel does not exist, then
        an error is returned."""
        raise NotImplementedError()

    def remove_handler(self, handler_id: str) -> bool:
        """Removes the handler from its registered channel.
        Returns True if it was successfully removed."""
        raise NotImplementedError()

    def add_internal_event_handler(self, channel_name: str, handler: InternalEventHandler) -> None:
        """Adds an internal event handler to manage communication between the launcher and the
        launcher channel.  The handlers are only removed by an invocation that returns
        a removal message."""
        raise NotImplementedError()


class AbcLauncherCategory:
    """
    Defines how to run and interact with extensions.  The extension loader requests that
    a runtime launcher starts based on a runtime category.  The category determines how
    it is launched and interacts.

    Some examples:
    1. A sandbox process manager that launches the processes in the correct limited
       way.  The manager is launched once at first launcher start time, and that process
       internally manages the "launchers".
    2. Each launcher is a separate docker container.  Running a new launcher starts up
       a new container.
    3. The launcher connects to a remotely running TCP/IP server and asks that to run
       new processes.

    Launcher Category describes how to run launchers.  Launchers define the permissions
    allowed for extensions running inside them.

    The standard call approach is:
    1. At startup time, the foreman process loads the configuration file to create the
       launcher categories.  Only these categories can be used during the runtime.
       Changing the categories requires restarting.
    2. The foreman uses the category API with specialty
    2. The extension-loader pro

    A category is declared in the foreman configuration.
    """
    __slots__ = ('__options',)

    def __init__(
            self,
            options: RuntimeConfig,
    ) -> None:
        self.__options = options

    @property
    def config(self) -> RuntimeConfig:
        """Get the configuration for the launcher."""
        return self.__options

    @property
    def options(self) -> RuntimeLauncherOptions:
        """List of options used to start the launcher."""
        return self.__options.options

    def is_valid(self) -> StdRet[None]:
        """Is this launcher valid, including all options?"""
        raise NotImplementedError()

    def initialize(self, context: RuntimeContext) -> StdRet[None]:
        """Initialize the launcher.  Only called once."""
        raise NotImplementedError()

    def start_extension(
            self,
            handler_id: str,
            start_event: foreman.LauncherStartExtensionRequestEvent,
    ) -> StdRet[None]:
        """Start the extension as requested by the event.  This will need to register with the
        RuntimeContext a new handler, and what events the extension is capable of consuming and
        producing."""
        raise NotImplementedError()

    def get_active_handler_ids(self) -> Sequence[str]:
        """Get the list of all active extension handler IDs."""
        raise NotImplementedError()

    def stop_extension(self, handler_id: str) -> StdRet[None]:
        """Stops the specific extension.  If the extension is not registered or not running, then
        the appropriate error is returned.  This should run until the extension is completely
        stopped."""
        raise NotImplementedError()

    def stop(self) -> StdRet[None]:
        """Stop all running launchers and shuts down the category.  Called only once."""
        raise NotImplementedError()


RuntimeFactory = Callable[[RuntimeConfig], AbcLauncherCategory]
