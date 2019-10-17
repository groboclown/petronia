
"""
Changes the assertion mode at runtime.

Used for parts of the system that are performance dependent.
"""

ASSERTION_ENABLED = __debug__

def is_assertion_enabled() -> bool:
    """
    Method to get the validation mode.  Should instead, for performance reasons, use the module value.
    """
    return ASSERTION_ENABLED

def internal_set_validation_mode(enabled: bool) -> None:
    """
    Set the validation mode at runtime.

    Protected access to only the `validation`, because this does not trigger state
    events.
    """
    global ASSERTION_ENABLED # pylint: disable=global-statement
    if enabled != ASSERTION_ENABLED:
        ASSERTION_ENABLED = enabled
