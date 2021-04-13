"""Announce that the extension has started."""

from petronia_common.util import StdRet
from ..events import foreman_announcement
from ..runner import EventRegistryContext


def send_announce_started(
        context: EventRegistryContext,
        extension_name: str,
) -> StdRet[None]:
    """Send the announcement that the extension has finished initialization phase.
    Until this is sent, the extension loader will not load dependencies."""
    print(f"*************** FINISHED LOADING {extension_name}")
    return context.send_event(
        extension_name + ':extension',
        foreman_announcement.ExtensionStartupCompleteEvent.UNIQUE_TARGET_FQN,
        foreman_announcement.ExtensionStartupCompleteEvent(),
    )
