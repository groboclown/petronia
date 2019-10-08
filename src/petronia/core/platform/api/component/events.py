
"""
Component events
"""

from .....aid.std import (
    EventBus,
    EventId,
    ComponentId,
    EventCallback,
    ListenerSetup,
)
from .chrome import (
    Chrome
)

# ---------------------------------------------------------------------------


EVENT_ID_REQUEST_CREATE_CHROME_WRAPPER = EventId('core.platform.api/component/request-create-chrome-wrapper')


class RequestCreateChromeWrapperEvent:
    """
    When the theme (or anything else) wants to create chrome around an
    existing window.

    If the chrome already exists, it is rejected.

    If the chrome does not exist, then it should be created;
    creation works and is accepted, then any reference to the native window ID
    will go through the chrome.  This means extensions don't need special
    handling for chrome handles; the platform invisibly handles it.

    This is why there is a special creation event, rather than going through
    the normal creation lifecycle - the created chrome will not be directly
    callable.
    """

    __slots__ = (
        '__chrome', '__window', '__request_id'
    )

    def __init__(
            self,
            window: ComponentId,
            chrome: Chrome,
            request_id: int
    ) -> None:
        self.__chrome = chrome
        self.__window = window
        self.__request_id = request_id

    @property
    def chrome(self) -> Chrome:
        return self.__chrome

    @property
    def window(self) -> ComponentId:
        return self.__window

    @property
    def request_id(self) -> int:
        return self.__request_id


def as_request_create_chrome_wrapper_listener(
        callback: EventCallback[RequestCreateChromeWrapperEvent]
) -> ListenerSetup[RequestCreateChromeWrapperEvent]:
    return (EVENT_ID_REQUEST_CREATE_CHROME_WRAPPER, callback)


def send_request_create_chrome_wrapper_event(
        bus: EventBus,
        window: ComponentId,
        chrome: Chrome,
        request_id: int
) -> None:
    bus.trigger(
        EVENT_ID_REQUEST_CREATE_CHROME_WRAPPER, window,
        RequestCreateChromeWrapperEvent(window, chrome, request_id)
    )
