
"""
Generic widgets the the platform must support creating.
These must be embedded inside other things.
"""
from typing import Union

from .infobox import (
    COMPONENT_ID_CREATE_INFOBOX,
    InfoBoxWidget,
)

from .separator import (
    COMPONENT_ID_CREATE_SEPARATOR,
    SeparatorWidget,
)

from .spacer import (
    COMPONENT_ID_CREATE_SPACER,
    SpacerWidget,
)

from .textfield import (
    COMPONENT_ID_CREATE_TEXTFIELD,
    TextFieldWidget,
)

from .icon_area import (
    COMPONENT_ID_CREATE_NOTIFICATION_ICON_AREA,
    NotificationIconArea,
)

from .label import (
    COMPONENT_ID_CREATE_LABEL,
    LabelWidget,
)


Widget = Union[
    InfoBoxWidget, SeparatorWidget, SpacerWidget, TextFieldWidget,
    NotificationIconArea, LabelWidget,
]
