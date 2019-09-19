
# mypy: allow-any-expr
# mypy: allow-any-explicit
# mypy: allow-any-generics


from typing import Optional, Any
from ...base import EventBus
from ...base.events.system_events import (
    MessageArgumentValueType,
    ErrorReport,
    send_error_reports_event,
    ERROR_CATEGORY_BUG, ERROR_CATEGORY_USER,
)
from ...base.logging import (
    log, logerr, ERROR,
)


def report_user_error(
        bus: Optional[EventBus],
        source: Any,
        message: str,
        **arguments: MessageArgumentValueType
) -> None:
    report_error(bus, ErrorReport(_to_src_str(source), ERROR_CATEGORY_USER, message, arguments))


def report_bug(
        bus: Optional[EventBus],
        source: Any,
        message: str,
        **arguments: MessageArgumentValueType
) -> None:
    report_error(bus, ErrorReport(_to_src_str(source), ERROR_CATEGORY_BUG, message, arguments))


def report_error(
        bus: Optional[EventBus],
        report: ErrorReport
) -> None:
    # TODO look up the message key in the localization tools
    if 'error' in report.arguments and isinstance(report.arguments['error'], BaseException):
        logerr(ERROR, report.source, report.arguments['error'], report.message_code, **report.arguments)
    else:
        log(ERROR, report.source, report.message_code, **report.arguments)

    if bus:
        send_error_reports_event(bus, report)


def _to_src_str(src: Any) -> str:
    if hasattr(src, '__name__'):
        if hasattr(src, '__module__'):
            return '{0}.{1}'.format(src.__module__, src.__name__)
        return str(src.__name__)
    return str(src)
