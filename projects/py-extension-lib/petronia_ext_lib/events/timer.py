# GENERATED CODE - DO NOT MODIFY
# Created on 2021-03-01T15:28:58.988147+00:00

"""
Data structures and marshalling for extension petronia.core.api.timer version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods


from typing import (
    Dict,
    Any,
    List,
)
import datetime
from petronia_common.util import i18n as _
from petronia_common.util import (
    StdRet,
    STANDARD_PETRONIA_CATALOG,
    collect_errors_from,
    not_none,
)

EXTENSION_NAME = 'petronia.core.api.timer'
EXTENSION_VERSION = (1, 0, 0)


class HeartbeatEvent:
    """
    The heart beat for the time.
    """
    __slots__ = ('sent_on',)
    FULL_EVENT_NAME = 'petronia.core.api.timer:heartbeat'
    SHORT_EVENT_NAME = 'heartbeat'

    UNIQUE_TARGET_FQN = 'petronia.core.api.timer:heartbeat'
    UNIQUE_TARGET_REL = 'heartbeat'

    def __init__(
        self,
        sent_on: datetime.datetime,
    ) -> None:
        self.sent_on = sent_on

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return HeartbeatEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'sent_on': self.sent_on.strftime('%Y%m%d:%H%M%S.%f:%z'),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['HeartbeatEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('sent_on')
        f_sent_on: datetime.datetime
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='sent_on',
                name='HeartbeatEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type datetime for structure {name}'),
                    field_name='sent_on',
                    name='HeartbeatEvent',
                )
            try:
                f_sent_on = datetime.datetime.strptime(val, '%Y%m%d:%H%M%S.%f:%z')
            except ValueError:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Invalid date-time format: {value}'),
                    value=val,
                )
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(HeartbeatEvent(
            sent_on=not_none(f_sent_on),
        ))

    def __repr__(self) -> str:
        return "HeartbeatEvent(" + repr(self.export_data()) + ")"


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
