
"""
Basic definitions for the components.
"""

from typing import Tuple


# A component can be told to send notices when actions happen on the
# component.  The first item is the action type (such as key press,
# mouse press, gain focus, etc), and the second item is the argument
# description.
RespondsToAction = Tuple[str, str]
