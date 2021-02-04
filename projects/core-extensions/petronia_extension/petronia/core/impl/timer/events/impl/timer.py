# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-03T21:03:11.410312

"""
Data structures and marshalling for extension petronia.core.api.timer version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint: disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements


from typing import (
    SupportsFloat,
    List,
    Any,
    Dict,
)
import datetime
from petronia_common.util import i18n as _
from petronia_common.util import (
    STANDARD_PETRONIA_CATALOG,
    not_none,
    collect_errors_from,
    StdRet,
)

EXTENSION_NAME = 'petronia.core.api.timer'
EXTENSION_VERSION = (1, 0, 0)


class HeartbeatEvent:
    """
    The heart beat for the time.
    """
    __slots__ = ('datetime',)
    FULL_EVENT_NAME = 'petronia.core.api.timer:heartbeat'
    SHORT_EVENT_NAME = 'heartbeat'

    UNIQUE_TARGET_FQN = 'petronia.core.api.timer:heartbeat'
    UNIQUE_TARGET_REL = 'heartbeat'

    def __init__(
        self,
        datetime: datetime.datetime,
    ) -> None:
        self.datetime = datetime

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return HeartbeatEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'datetime': self.datetime.strftime('%Y%m%d:%H%M%S.%f:%z'),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['HeartbeatEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('datetime')
        f_datetime: datetime.datetime
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='datetime',
                name='HeartbeatEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type datetime for structure {name}'),
                    field_name='datetime',
                    name='HeartbeatEvent',
                )
            try:
                f_datetime = datetime.datetime.strptime(val, '%Y%m%d:%H%M%S.%f:%z')
            except ValueError:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Invalid date-time format: {value}'),
                    value=val,
                )
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(HeartbeatEvent(
            datetime=not_none(f_datetime),
        ))

    def __repr__(self) -> str:
        return "HeartbeatEvent(" + repr(self.export_data()) + ")"


class HeartbeatIntervalState:
    """
    Interval, in seconds, for the heartbeat. The timer extension should listen to
    changes to this data, so that it can on-the-fly change this configuration state.
    """
    __slots__ = ('seconds',)

    UNIQUE_TARGET_FQN = 'petronia.core.api.timer:heartbeat-interval'
    UNIQUE_TARGET_REL = 'petronia.core.api.timer:heartbeat-interval'

    def __init__(
        self,
        seconds: float,
    ) -> None:
        self.seconds = seconds

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'seconds': self.seconds,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['HeartbeatIntervalState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('seconds')
        f_seconds: float
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='seconds',
                name='HeartbeatIntervalState',
            )
        else:
            if not isinstance(val, SupportsFloat):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='seconds',
                    type='float',
                    name='HeartbeatIntervalState',
                )
            f_seconds = float(val)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(HeartbeatIntervalState(
            seconds=not_none(f_seconds),
        ))

    def __repr__(self) -> str:
        return "HeartbeatIntervalState(" + repr(self.export_data()) + ")"


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
