
"""
A top-level window that can store widgets and containers.
"""


from typing import Optional
from ..defs import RespondsToAction
from .....base import (
    create_singleton_identity,
    ComponentId,
)
from .widgets import Widget

COMPONENT_ID_CREATE_CHROME = create_singleton_identity('core.platform.api/chrome')
