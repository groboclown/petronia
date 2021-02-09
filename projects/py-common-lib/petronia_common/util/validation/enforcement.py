
"""
Functions that enforce certain conditions, and returns errors on failures.
"""

from typing import Tuple, List, Callable, Optional
from ..error import PetroniaReturnError, join_errors
from ..message import I18n, UserMessage, UserMessageData, STANDARD_PETRONIA_CATALOG
from ..message import i18n as _


def enforce_that(
        src: str, catalog: str, validation_problem: I18n,
        first_condition: Callable[[], bool],
        *conditions: Callable[[], bool],
        **details: UserMessageData,
) -> Optional[PetroniaReturnError]:
    """
    Always runs the enforcement check.  Use this if you must guarantee that a condition
    must be satisfied, rather than as a developer check.

    This exits at the first error.  This allows for ordering checks, where later ones would
    otherwise fail due to some unmet condition.
    """
    try:
        if not first_condition():
            return join_errors(
                _validation_problem_message(src),
                UserMessage(catalog, validation_problem, **details),
            )
        # This section is weird.  Windows can show these lines and branches as not covered.
        # See https://github.com/nedbat/coveragepy/issues/1022
        for condition in conditions:
            if not condition():
                return join_errors(
                    _validation_problem_message(src),
                    UserMessage(catalog, validation_problem, **details),
                )
        return None
    except BaseException as err:  # pylint: disable=W0703
        return join_errors(
            _validation_error(src, err),
            UserMessage(catalog, validation_problem, **details),
        )


def enforce_all(
        src: str, catalog: str,
        first_condition: Tuple[I18n, Callable[[], bool]],
        *conditions: Tuple[I18n, Callable[[], bool]],
        **details: UserMessageData,
) -> Optional[PetroniaReturnError]:
    """
    Always runs the enforcement check.  Use this if you must guarantee that a condition
    must be satisfied, rather than as a developer check.

    This runs through all the conditions and gathers the accumulated messages.
    Therefore, this function is costlier than the enforce_that function.  It can
    also lead to chained errors if one condition checks for a condition that later
    conditions assume to be true.
    """
    error_messages: List[UserMessage] = []
    try:
        if not first_condition[1]():
            error_messages.append(UserMessage(catalog, first_condition[0], **details))
    except BaseException as err:  # pylint: disable=W0703
        error_messages.append(_validation_error(src, err))

    for validation_problem, condition in conditions:
        try:
            if not condition():
                error_messages.append(UserMessage(catalog, validation_problem, **details))
        except BaseException as err:  # pylint: disable=W0703
            error_messages.append(_validation_error(src, err))
    if error_messages:
        error_messages.insert(0, _validation_problem_message(src))
        return join_errors(*error_messages)
    return None


def _validation_problem_message(src: str) -> UserMessage:
    return UserMessage(
        STANDARD_PETRONIA_CATALOG,
        _("{src}: validation error"),
        src=src,
    )


def _validation_error(src: str, err: BaseException) -> UserMessage:
    return UserMessage(
        STANDARD_PETRONIA_CATALOG,
        _("{src}: validation error ({e})"),
        src=src,
        e=err,
    )
