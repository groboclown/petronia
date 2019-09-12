
# mypy: allow-any-expr
# mypy: allow-any-explicit
# mypy: allow-any-


from typing import Iterable, Dict, Union, Optional, Type, Any
from types import FunctionType, MethodType
from ...base import EventBus
from ...base.events.system_events import send_error_event
from ...base.logging import (
    log, logerr, ERROR,
)


def report_error(
        bus: Optional[EventBus],
        source: Any,
        message: str,
        **arguments: Union[
            str, int, bool, float, BaseException,
            Iterable[Union[str, int, bool, float]],
            Dict[str, Union[str, int, bool, float]]
        ]
) -> None:
    if 'error' in arguments and isinstance(arguments['error'], BaseException):
        logerr(ERROR, source, arguments['error'], message, **arguments)
    else:
        log(ERROR, source, message, **arguments)

    if bus:
        send_error_event(bus, _to_src_str(source), message, **arguments)


def _to_src_str(src: Any) -> str:
    if hasattr(src, '__name__'):
        if hasattr(src, '__module__'):
            return '{0}.{1}'.format(src.__module__, src.__name__)
        return str(src.__name__)
    return str(src)
