
"""
Only exists for the custom event bus implementations.
"""

# Shoved into a sub-directory so that this can
# export the internal stuff without pylint complaining.

from ...internal_.identity_types import (
    ComponentId,
    create_component_identity_from_unique_id,
)
