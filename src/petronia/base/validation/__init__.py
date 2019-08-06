"""
Safety checks on the system.

These are split into two groups:

- assertions: debugging assertions that can be
    conditionally disabled.  That means these cannot
    be used to enforce restricitons on the code,
    so use with care.
    These should be considered "internal consistency
    checks", used for finding coding problems.
- validations: always-enabled checks.
"""

from .global_state import is_assertion_enabled
from .assertions import (
    assert_all,
    assert_formatted,
    assert_state,
    assert_all_calls,
    assert_call,
    assert_has_signature,
)
