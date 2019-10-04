

from .....aid.simp import (
    EventBus,
    create_singleton_identity,
    ComponentId,
    EventCallback,
    ListenerSetup,
)


# ---------------------------------------------------------------------------


EVENT_ID_CHROME_WRAPPED_WINDOW = create_singleton_identity('core.platform.api/component/chrome-wrapped')


class ChromeWrappedWindowEvent:
    """
    Triggered when chrome is created to wrap around a window.  This means that
    the chrome should replace the window when layout managers arrange windows.
    The platform should manage the relationship between the position of the
    chrome and the position of the window.
    """

    __slots__ = (
        '__chrome', '__window'
    )

    def __init__(
            self,
            chrome: ComponentId,
            window: ComponentId
    ) -> None:
        self.__chrome = chrome
        self.__window = window

    @property
    def chrome(self) -> ComponentId:
        return self.__chrome

    @property
    def window(self) -> ComponentId:
        return self.__window


def as_chrome_wrapped_window_listener(
        callback: EventCallback[ChromeWrappedWindowEvent]
) -> ListenerSetup[ChromeWrappedWindowEvent]:
    return (EVENT_ID_CHROME_WRAPPED_WINDOW, callback)
