
"""
Portals, Containers, and Managers, oh my!
"""

from typing import Optional, List
from ....aid.simp import (
    EventBus,
    ComponentId,
)
from ....aid.lifecycle import (
    create_component_listener_helper,
)
from ....core.platform.api import (
    ScreenUnit,
    ScreenArea,
)


class Portal:
    """
    Manages zero or more windows within a small area.
    """

    __slots__ = (
        '__name',
        '__cid',
        '__size',
        '_window_cids',
        '__chrome_cid',
        '__listeners',
    )

    _window_cids: List[ComponentId]

    def __init__(
            self,
            bus: EventBus,
            name: str,
            cid: ComponentId,
            initial_size: ScreenArea,
            chrome_cid: ComponentId
    ) -> None:
        self.__name = name
        self.__cid = cid
        self.__size = initial_size
        self.__chrome_cid = chrome_cid
        self.__listeners = create_component_listener_helper(bus, cid)

