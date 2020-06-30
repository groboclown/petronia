

"""
One of the few places where non-local state is stored.

It's local to the running instance.
"""

_ASSERTION_ENABLED = [False]


def set_global_assertion_state(enabled: bool) -> None:
    """
    Sets whether assertion calls are used.  By default, they are not.

    :param enabled:
    :return:
    """
    _ASSERTION_ENABLED[0] = enabled


def are_assertions_enabled() -> bool:
    return _ASSERTION_ENABLED[0]
