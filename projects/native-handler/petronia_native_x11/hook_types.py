"""Basic hook."""

from typing import Union
from petronia_common.util import StdRet, UserMessage
from petronia_ext_lib.runner import LookupEventRegistryContext
from .configuration import ConfigurationStore
from .common_data import Libraries, WindowManagerData, CommonData


class Hook:
    """Sets up a hook based on the different phases."""

    def setup_wm_screen(self, data: WindowManagerData) -> StdRet[None]:
        """Setup after the connection to the X server is established as the window manager and
        the screen is grabbed."""
        raise NotImplemented

    def setup_pre_event_loop(self, data: CommonData) -> StdRet[None]:
        """Setup after the screen is released ("ungrabbed") and just before the
        event loop starts running."""
        raise NotImplemented

    def shutdown(self, data: CommonData) -> StdRet[None]:
        """After the event loop stops, shut down.  The X server connection will still
        be open."""
        raise NotImplemented


class HookFactory:
    """Creates a hook if it's valid."""

    def create(self, libs: Libraries) -> StdRet[Union[Hook, UserMessage]]:
        """Creates a hook after the libraries are loaded.  If the hook can't
        be created but that doesn't stop the extension, then a user message
        is returned indicating a warning."""
        raise NotImplemented


class PhaseRunner:
    """Runs the different phases between the hooks."""

    def boot(
            self,
            context: LookupEventRegistryContext, config: ConfigurationStore,
    ) -> StdRet[Libraries]:
        """Setup enough to get to the point where the 'setup_boot' can run."""
        raise NotImplemented

    def become_window_manager(self, libs: Libraries) -> StdRet[WindowManagerData]:
        """Setup enough to connect to the server and become a window manager."""
        raise NotImplemented

    def prepare_event_loop(self, data: WindowManagerData) -> StdRet[CommonData]:
        """Release the screen and prepare for the loop to start."""
        raise NotImplemented

    def run_event_loop(self, data: CommonData) -> StdRet[None]:
        """Run the event loop.  Exits after the loop is running, which should be in another
        thread."""
        raise NotImplemented

    def shutdown(self, data: CommonData) -> StdRet[None]:
        """After all the hooks finish shutting down, shut down the connection to the
        X server nicely."""
        raise NotImplemented
