
# mypy: allow-any-explicit
# mypy: allow-any-expr
# mypy: allow-any-generics

from typing import Callable, Optional, Any
from .global_state import are_assertions_enabled
from ..error import PetroniaReturnError, as_error
from ..message import UserMessage, I18n
from ..message import i18n as _


class PetroniaAssertionError(AssertionError):
    def __init__(
            self, src: str, validation_problem: str,
            cause: Optional[BaseException],
            **details: Any,
    ) -> None:
        AssertionError.__init__(self, f'{src}: {validation_problem}'.format(**details), cause)


def assert_that(
        src: str, validation_problem: str,
        first_condition: Callable[[], bool],
        *conditions: Callable[[], bool],
        **details: Any,
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
        **details: Any,
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
            return as_error(UserMessage(
                _("{src}: validation error for {problem}"),
                src=src,
                problem=validation_problem.format(**details),
            ))
        for condition in conditions:
            if not condition():
                return as_error(UserMessage(
                    _("{src}: validation error for {problem}"),
                    src=src,
                    problem=validation_problem.format(**details),
                ))
        return None
    except BaseException as e:
        return as_error(UserMessage(
            _("{src}: validation error for {problem} ({e})"),
            src=src,
            problem=validation_problem.format(**details),
            e=e,
        ))
