
"""
Functions that enforce certain conditions, and returns errors on failures.
"""

from typing import Tuple, List, Callable, Optional
from ..error import PetroniaReturnError, error_message, possible_error
from ..message import I18n, UserMessage, UserMessageData, STANDARD_PETRONIA_CATALOG, i18n
# _ and i18n both need to exist to allow for correct
# translation and non-translation.
_ = i18n  # pylint: disable=C0103


def enforce_that(
        src: str, validation_problem: I18n,
        first_condition: Callable[[], bool],
        *conditions: Callable[[], bool],
        **details: UserMessageData,
) -> Optional[PetroniaReturnError]:
    """
    Always runs the enforcement check.  Use this if you must guarantee that a condition
    must be satisfied, rather than as a developer check.

    This exits at the first error.  This allows for ordering checks, where later ones would
    otherwise fail due to some unmet condition.

    :param first_condition:
    :param src:
    :param validation_problem:
    :param conditions:
    :param details:
    :return:
    """
    try:
        if not first_condition():
            return error_message(
                STANDARD_PETRONIA_CATALOG,
                i18n(_("{src}: validation error: ") + validation_problem),
                src=src,
                **details,
            )
        # This section is weird.  Windows can show these lines and branches as not covered.
        # See https://github.com/nedbat/coveragepy/issues/1022
        for condition in conditions:
            if not condition():
                return error_message(
                    STANDARD_PETRONIA_CATALOG,
                    i18n(_("{src}: validation error: ") + validation_problem),
                    src=src,
                    **details,
                )
        return None
    except BaseException as err:  # pylint: disable=W0703
        return error_message(
            STANDARD_PETRONIA_CATALOG,
            i18n(_("{src}: validation error ({e}): ") + validation_problem),
            src=src,
            e=err,
            **details,
        )


def enforce_all(
        src: str,
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

    :param first_condition:
    :param src:
    :param conditions:
    :param details:
    :return:
    """
    error_messages: List[UserMessage] = []
    try:
        if not first_condition[1]():
            error_messages.append(UserMessage(
                STANDARD_PETRONIA_CATALOG,
                i18n(_("{src}: validation error: ") + first_condition[0]),
                src=src,
                **details,
            ))
    except BaseException as err:  # pylint: disable=W0703
        error_messages.append(UserMessage(
            STANDARD_PETRONIA_CATALOG,
            i18n(_("{src}: validation error ({e}): ") + first_condition[0]),
            src=src,
            e=err,
            **details,
        ))

    for validation_problem, condition in conditions:
        try:
            if not condition():
                error_messages.append(UserMessage(
                    STANDARD_PETRONIA_CATALOG,
                    i18n(_("{src}: validation error: ") + validation_problem),
                    src=src,
                    **details,
                ))
        except BaseException as err:  # pylint: disable=W0703
            error_messages.append(UserMessage(
                STANDARD_PETRONIA_CATALOG,
                i18n(_("{src}: validation error ({e}): ") + validation_problem),
                src=src,
                e=err,
                **details,
            ))
    return possible_error(messages=error_messages)
