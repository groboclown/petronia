
"""
Routes raw events between different streams.  Each stream has a set of consumers and producers.
"""

from . import router, channel, handler
from .router import EventRouter
from .channel import EventChannel, EventRouteDestinationCallback
