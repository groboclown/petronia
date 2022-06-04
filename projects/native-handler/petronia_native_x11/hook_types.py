"""Basic hook."""

from typing import Union, Callable
from petronia_common.util import StdRet, UserMessage
from petronia_ext_lib.runner import EventRegistryContext
from .configuration import ConfigurationStore
from .common_data import Libraries, WindowManagerData
from .running_data import RunningData


class Hook:
    """Sets up a hook based on the different phases."""

    def setup_wm_screen(self, data: WindowManagerData) -> StdRet[None]:
        """Setup after the connection to the X server is established as the window manager and
        the screen is grabbed."""
        raise NotImplementedError

    def setup_pre_event_loop(self, data: RunningData) -> StdRet[None]:
        """Setup after the screen is released ("ungrabbed") and just before the
        event loop starts running."""
        raise NotImplementedError

    def shutdown(self, data: RunningData) -> StdRet[None]:
        """After the event loop stops, shut down.  The X server connection will still
        be open."""
        raise NotImplementedError


"""
HookFactory: Creates a hook after the libraries are loaded.  If the hook can't
be created but that doesn't stop the extension, then a user message
is returned indicating a warning."""
HookFactory = Callable[[Libraries], StdRet[Union[Hook, UserMessage]]]


class PhaseRunner:
    """Runs the different phases between the hooks."""

    def boot(
            self,
            context: EventRegistryContext, config: ConfigurationStore,
    ) -> StdRet[Libraries]:
        """Setup enough to get to the point where the 'setup_boot' can run."""
        raise NotImplementedError

    def become_window_manager(self, libs: Libraries) -> StdRet[WindowManagerData]:
        """Setup enough to connect to the server and become a window manager."""
        raise NotImplementedError

    def prepare_event_loop(self, data: WindowManagerData) -> StdRet[RunningData]:
        """Release the screen and prepare for the loop to start."""
        raise NotImplementedError

    def run_event_loop(self, data: RunningData) -> StdRet[None]:
        """Run the event loop.  Exits after the loop is running, which should be in another
        thread."""
        raise NotImplementedError

    def shutdown(self, data: RunningData, timeout: float) -> StdRet[None]:
        """After all the hooks finish shutting down, shut down the connection to the
        X server nicely."""
        raise NotImplementedError
