
# mypy: allow-any-explicit
# mypy: allow-untyped-defs
# mypy: allow-any-expr

"""
Consistent validation checks.  These are runtime debug checks to ensure the
programming is consistent.  In a production environment, these will not run.

These should be thought of as equivalent to the "assert" keyword.

DO NOT USE THESE FOR DATA OR PERMISSION VALIDATION.

These are only to be used with coding convention practices.
"""

from types import LambdaType
from typing import Tuple, Callable, Dict, Any, Optional, Sequence, Union, Type
from inspect import signature
from ..errors import PetroniaInvalidState
from .global_state import ASSERTION_ENABLED
from ..util.memory import EMPTY_DICT, EMPTY_LIST

CallableCondition = Callable[[], bool]
CallableConditionReason = Tuple[CallableCondition, str]
CallableConditionReasonFormat1 = Tuple[CallableCondition, str, Sequence[Any]]
CallableConditionReasonFormat2 = Tuple[CallableCondition, str, Dict[str, Any]]
CallableConditionReasonFormat3 = Tuple[CallableCondition, str, Sequence[Any], Dict[str, Any]]
CallableConditionOption = Union[
    CallableCondition,
    CallableConditionReason,
    CallableConditionReasonFormat1,
    CallableConditionReasonFormat2,
    CallableConditionReasonFormat3,
]

ConditionReason = Tuple[bool, str]
ConditionReasonFormat1 = Tuple[bool, str, Sequence[Any]]
ConditionReasonFormat2 = Tuple[bool, str, Dict[str, Any]]
ConditionReasonFormat3 = Tuple[bool, str, Sequence[Any], Dict[str, Any]]
ConditionOption = Union[
    bool,
    ConditionReason,
    ConditionReasonFormat1,
    ConditionReasonFormat2,
    ConditionReasonFormat3,
]

def assert_state(
        condition: bool,
        src: str, validation_problem: str, details: Optional[str] = None
) -> None:
    """
    Perform a state validation check.
    """
    if ASSERTION_ENABLED and not condition:
        raise PetroniaInvalidState(src, validation_problem, details)

def assert_formatted(
        condition: bool,
        src: str, validation_problem: str,
        format_str: str,
        *vargs: Any, **kvargs: Any
) -> None:
    """
    Performs validation check with a format string, which is evaluated only when
    the condition is false and validations are enabled.
    """
    if ASSERTION_ENABLED and not condition:
        raise PetroniaInvalidState(
            src, validation_problem,
            format_str.format(*vargs, **kvargs)
        )

def assert_call(
        condition: CallableCondition,
        src: str, validation_problem: str,
        format_str: str,
        *vargs: Any, **kvargs: Any
) -> None:
    """
    Performs validation check with a format string, which is evaluated only when
    the condition is false and validations are enabled.
    """
    if ASSERTION_ENABLED and not condition():
        raise PetroniaInvalidState(
            src, validation_problem,
            format_str.format(*vargs, **kvargs)
        )

def assert_all(
        src: str, validation_problem: str,
        *conditions: ConditionOption
) -> None:
    """
    Ensure all the given conditions are met.
    """
    if ASSERTION_ENABLED: # pylint: disable=too-many-nested-blocks
        for cond in conditions:
            if isinstance(cond, bool):
                if not cond:
                    raise PetroniaInvalidState(src, validation_problem, None)
            else:
                if not cond[0]:
                    reason = 'failed check'
                    vargs: Sequence[Any] = EMPTY_LIST
                    kvargs: Dict[str, Any] = EMPTY_DICT
                    if len(cond) >= 2:
                        reason = cond[1]
                        if len(cond) >= 4:
                            vargs = cond[2] # type: ignore
                            kvargs = cond[3] # type: ignore
                        elif len(cond) == 3:
                            if isinstance(cond[2], dict): # type: ignore
                                kvargs = cond[2] # type: ignore
                            else:
                                vargs = cond[2] # type: ignore
                    raise PetroniaInvalidState(
                        src,
                        validation_problem,
                        reason.format(*vargs, **kvargs)
                    )

def assert_all_calls(
        src: str, validation_problem: str,
        *conditions: CallableConditionOption
) -> None:
    """
    Ensure all the given conditions are met.

    Each condition item is a callable that, when invoked, must return a truthy value.
    """
    if ASSERTION_ENABLED: # pylint: disable=too-many-nested-blocks
        for cond in conditions:
            if callable(cond):
                if not cond():
                    raise PetroniaInvalidState(src, validation_problem, None)
            else:
                if not cond[0]():
                    reason = 'failed check'
                    vargs: Sequence[Any] = EMPTY_LIST
                    kvargs: Dict[str, Any] = EMPTY_DICT
                    if len(cond) >= 2:
                        reason = cond[1]
                        if len(cond) >= 4:
                            vargs = cond[2] # type: ignore
                            kvargs = cond[3] # type: ignore
                        elif len(cond) == 3:
                            if isinstance(cond[2], dict): # type: ignore
                                kvargs = cond[2] # type: ignore
                            else:
                                vargs = cond[2] # type: ignore
                    raise PetroniaInvalidState(
                        src,
                        validation_problem,
                        reason.format(*vargs, **kvargs)
                    )

def assert_has_signature(
        src: str,
        validation_problem: str,
        fcn: Callable, # type: ignore
        return_type: Optional[Type[Any]],
        *argument_types: Type[Any]
) -> None:
    """
    Ensure the callable has the given signature.
    """
    if ASSERTION_ENABLED:
        if isinstance(fcn, LambdaType):
            # lambdas can't have annotations, but they don't get a free pass.
            sig = signature(fcn)
            assert_formatted(
                len(sig.parameters) == len(argument_types),
                src,
                validation_problem,
                'must have {0} arguments, found {1}',
                len(argument_types),
                sig.parameters
            )
            return
        assert_formatted(
            callable(fcn),
            src,
            validation_problem,
            'function must be callable, found {0}',
            fcn
        )
        sig = signature(fcn)
        assert_formatted(
            sig.return_annotation == return_type,
            src,
            validation_problem,
            'function must have {0} return type, found {1}',
            return_type,
            fcn
        )
        ordered_argument_names = tuple(sig.parameters)
        assert_formatted(
            len(ordered_argument_names) == len(argument_types),
            src,
            validation_problem,
            'must have {0} arguments, found {1}',
            len(argument_types),
            sig.parameters
        )
        for idx in range(len(argument_types)): # pylint: disable=consider-using-enumerate
            arg_type = argument_types[idx]
            arg_name = ordered_argument_names[idx]
            param = sig.parameters[arg_name]
            param_type = param.annotation
            assert_formatted(
                param_type == arg_type,
                src,
                validation_problem,
                'argument {0} must be {1}, found {2}',
                idx + 1,
                arg_type,
                param_type
            )
