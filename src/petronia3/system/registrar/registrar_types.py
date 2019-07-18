
"""
Standard type definitions for the registrar
"""

from typing import Callable
from ..participant import ComponentId
from ...util.memory import T

CategoryFactory = Callable[[T], ComponentId]
