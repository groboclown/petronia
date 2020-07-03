
from typing import Tuple, List, Callable, Optional
from .global_state import are_assertions_enabled
from ..error import PetroniaReturnError, error_message, possible_error
from ..message import I18n, UserMessage, UserMessageData, i18n
from ..message import i18n as _


class PetroniaAssertionError(AssertionError):
    def __init__(
            self, src: str, validation_problem: str,
            cause: Optional[BaseException],
            **details: UserMessageData,
    ) -> None:
        AssertionError.__init__(self, f'{src}: {validation_problem}'.format(**details), cause)


def assert_that(
        src: str, validation_problem: str,
        first_condition: Callable[[], bool],
        *conditions: Callable[[], bool],
        **details: UserMessageData,
) -> None:
    """
    Makes an assertion that one or more conditions are valid.
    This is for programmer stability purposes.  Production environments may not have
    this turned on.

    Because this is for programmer stability, it will raise exceptions rather than return
    error conditions.  It also takes strings, rather than i18n values.

    This exits at the first error.  This allows for ordering checks, where later ones would
    otherwise fail due to some unmet condition.

    :param first_condition:
    :param src:
    :param validation_problem:
    :param conditions: the first one to fail or return False will cause an assertion failure.
    :return:
    """
    if are_assertions_enabled():
        try:
            res = first_condition()
        except BaseException as e:
            raise PetroniaAssertionError(src, validation_problem, e, **details)
        if not res:
            raise PetroniaAssertionError(src, validation_problem, None, **details)

        for condition in conditions:
            try:
                res = condition()
            except BaseException as e:
                raise PetroniaAssertionError(src, validation_problem, e, **details)
            if not res:
                raise PetroniaAssertionError(src, validation_problem, None, **details)


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
                i18n(_("{src}: validation error: ") + validation_problem),
                src=src,
                **details,
            )
        for condition in conditions:
            if not condition():
                return error_message(
                    i18n(_("{src}: validation error: ") + validation_problem),
                    src=src,
                    **details,
                )
        return None
    except BaseException as e:
        return error_message(
            i18n(_("{src}: validation error ({e}): ") + validation_problem),
            src=src,
            e=e,
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
                i18n(_("{src}: validation error: ") + first_condition[0]),
                src=src,
                **details,
            ))
    except BaseException as e:
        error_messages.append(UserMessage(
            i18n(_("{src}: validation error ({e}): ") + first_condition[0]),
            src=src,
            e=e,
            **details,
        ))

    for validation_problem, condition in conditions:
        try:
            if not condition():
                error_messages.append(UserMessage(
                    i18n(_("{src}: validation error: ") + validation_problem),
                    src=src,
                    **details,
                ))
        except BaseException as e:
            error_messages.append(UserMessage(
                i18n(_("{src}: validation error ({e}): ") + validation_problem),
                src=src,
                e=e,
                **details,
            ))
    return possible_error(messages=error_messages)
