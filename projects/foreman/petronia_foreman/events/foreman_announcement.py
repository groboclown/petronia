# GENERATED CODE - DO NOT MODIFY

"""
Data structures and marshalling for extension petronia.core.api.foreman_announcement version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods,unused-import,invalid-name,consider-using-f-string

# Allow forward references and thus cyclic data types
from __future__ import annotations
from typing import (
    Dict,
    List,
    Any,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    STANDARD_PETRONIA_CATALOG,
    collect_errors_from,
    not_none,
    StdRet,
)

EXTENSION_NAME = 'petronia.core.api.foreman_announcement'
EXTENSION_VERSION = (1, 0, 0)


class ExtensionStartupCompleteEvent:
    """
    Report by a loaded extension when it has completed all of its startup phase.
    Usually, this is just before the extension begins the read-events loop. The
    source ID of the event must be the loaded extension name, followed by a colon
    (':'), and some other text afterwards.
    """
    __slots__ = ()
    FULL_EVENT_NAME = 'petronia.core.api.foreman_announcement:extension-startup-complete'
    SHORT_EVENT_NAME = 'extension-startup-complete'

    UNIQUE_TARGET_FQN = 'petronia.core.api.foreman_announcement:launcher'
    UNIQUE_TARGET_REL = 'launcher'

    def __init__(
        self,
    ) -> None:
        pass

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return ExtensionStartupCompleteEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        return {}

    @staticmethod
    def parse_data(_data: Dict[str, Any]) -> StdRet['ExtensionStartupCompleteEvent']:
        """Parse the marshalled data into this structured form.  There are no fields, so this is
        essentially a no-op."""
        return StdRet.pass_ok(ExtensionStartupCompleteEvent())

    def __repr__(self) -> str:
        return "ExtensionStartupCompleteEvent(" + repr(self.export_data()) + ")"


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
