
# mypy: allow-any-expr
# mypy: allow-any-explicit
# mypy: allow-any-generics


from typing import Optional, Any
from ...base import EventBus
from ...base.events.system_events import (
    ErrorReport,
    send_error_reports_event,
    ERROR_CATEGORY_BUG, ERROR_CATEGORY_USER, ERROR_CATEGORY_ENVIRONMENT,
)
from ...base.logging import (
    log, logerr, ERROR,
)
from ...base.util import (
    I18n,
    UserMessageData,
    UserMessage,
)


def report_user_error(
        bus: EventBus,
        source: Any,
        message: I18n,
        **arguments: UserMessageData
) -> None:
    report_error(bus, create_user_error(source, message, **arguments))


def create_user_error(
        source: Any,
        message: I18n,
        **arguments: UserMessageData
) -> ErrorReport:
    return ErrorReport(_to_src_str(source), ERROR_CATEGORY_USER, UserMessage(message, **arguments))


def report_bug(
        bus: EventBus,
        source: Any,
        message: I18n,
        **arguments: UserMessageData
) -> None:
    report_error(bus, create_bug_report(source, message, **arguments))


def create_bug_report(
        source: Any,
        message: I18n,
        **arguments: UserMessageData
) -> ErrorReport:
    return ErrorReport(_to_src_str(source), ERROR_CATEGORY_BUG, UserMessage(message, **arguments))


def report_enviro_problem(
        bus: EventBus,
        source: Any,
        message: I18n,
        **arguments: UserMessageData
) -> None:
    report_error(bus, create_enviro_problem_report(source, message, **arguments))


def create_enviro_problem_report(
        source: Any,
        message: I18n,
        **arguments: UserMessageData
) -> ErrorReport:
    return ErrorReport(_to_src_str(source), ERROR_CATEGORY_ENVIRONMENT, UserMessage(message, **arguments))


def report_error(
        bus: Optional[EventBus],
        report: ErrorReport
) -> None:
    # TODO look up the message key in the localization tools
    if 'error' in report.message.arguments and isinstance(report.message.arguments['error'], BaseException):
        logerr(
            ERROR, report.source, report.message.arguments['error'],
            report.message.message, **report.message.arguments
        )
    else:
        log(ERROR, report.source, report.message.message, **report.message.arguments)

    if bus:
        send_error_reports_event(bus, report)


def _to_src_str(src: Any) -> str:
    if hasattr(src, '__name__'):
        if hasattr(src, '__module__'):
            return '{0}.{1}'.format(src.__module__, src.__name__)
        return str(src.__name__)
    return str(src)
