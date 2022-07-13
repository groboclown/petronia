"""Runs the extension."""

from typing import Callable
from petronia_common.util import StdRet, UserMessage
from petronia_common.util import i18n as _
from petronia_ext_lib.runner import EventRegistryContext
from petronia_native.common import user_messages
from .configuration import ConfigurationStore


def run_server(
        context: EventRegistryContext,
        config: ConfigurationStore,
        on_warning: Callable[[UserMessage], None],
) -> StdRet[None]:
    """Run the extension.  Returns on exit."""
    return StdRet.pass_errmsg(
        user_messages.TRANSLATION_CATALOG,
        _("Wayland server not implemented yet"),
    )
