
"""
Add the extensions into the system.
"""

from typing import Sequence, Set, Optional
from petronia3.extensions.extensions.api import (
    ExtensionLoadedEvent,
    ExtensionState,
    LoadedExtension,
)
from petronia3.extensions.extensions.api.events import (
    TARGET_EXTENSION_LOADER,
    EVENT_ID_EXTENSION_LOADED,
    EVENT_ID_REQUEST_LOAD_EXTENSION,
    RequestLoadExtensionEvent,
)
from petronia3.extensions.extensions.api.state import (
    STATE_EXTENSION_LOADER,
)
from petronia3.extensions.state.api import (
    set_state,
)
from petronia3.system.bus import (
    EventBus,
    EventId,
    EventCallback,
    ListenerSetup,
)
from petronia3.system.participant import (
    ParticipantId
)
from petronia3.errors import PetroniaExtensionNotFound
from .defs import (
    ExtensionLoader,
    ExtensionCompatibility,
)
from .ext_loader import (
    load_additional_extension,
    load_extensions,
)

def bootstrap_extension_loader(
        bus: EventBus,
        initial_extensions: Sequence[ExtensionCompatibility],
        initial_only_secure: bool,
        loader: ExtensionLoader
) -> None:
    """
    Adds the extension loader into the bus.  Because the extensions loader has
    very specific, immutable security concerns, it must be loaded at boot time
    with configuration state.
    """

    # TODO error reporting / checking?
    loaded = load_extensions(
        initial_extensions, loader, bus, initial_only_secure
    )
    extloader = _ExtensionStatefulLoader(bus, ExtensionState(loaded), loader)
    bus.add_listener(
        TARGET_EXTENSION_LOADER,
        _as_request_load_extension_listener,
        extloader.on_extension_load_request
    )

    # TODO if the system supports disposing extensions, then this needs to
    # listen to the dispose event and remove it from the state.



class _ExtensionStatefulLoader:
    __slots__ = ('__bus', '__state', '__loader', '_loaded')
    _loaded: Set[LoadedExtension]
    def __init__(
            self,
            bus: EventBus,
            state: ExtensionState,
            loader: ExtensionLoader,
    ) -> None:
        self.__bus = bus
        self.__state = state
        self.__loader = loader
        self._loaded = set(state.loaded_extensions)

    def on_extension_load_request(
            self,
            event_id: EventId, target_id: ParticipantId, # pylint: disable=unused-argument
            event_object: RequestLoadExtensionEvent
    ) -> None:
        """on the event happening."""
        for ext in self._loaded:
            if  event_object.extension_name == ext.name:
                # Already loaded the extension.  Nothing to do.
                return
        # TODO error reporting / checking?
        deps = load_additional_extension(
            event_object.extension_name,
            self.__loader,
            self.__bus,
            self._loaded
        )
        loaded: Optional[LoadedExtension] = None
        for found in deps:
            if found.name == event_object.extension_name:
                loaded = found
        if not loaded:
            # TODO error reporting?
            raise PetroniaExtensionNotFound(
                event_object.extension_name,
                map(lambda x: x.name, deps) # type: ignore
            )
        _send_extension_loaded_event(
            self.__bus,
            loaded,
            deps
        )
        self._loaded = self._loaded.union(deps)
        if self._loaded != self.__state.loaded_extensions:
            _send_extension_state_change(self.__bus, ExtensionState(self._loaded))



def _as_request_load_extension_listener(
        callback: EventCallback[RequestLoadExtensionEvent]
) -> ListenerSetup[RequestLoadExtensionEvent]:
    return (EVENT_ID_REQUEST_LOAD_EXTENSION, callback,)

def _send_extension_loaded_event(
        bus: EventBus,
        extension: LoadedExtension,
        loaded_dependencies: Sequence[LoadedExtension]
) -> None:
    bus.trigger(
        EVENT_ID_EXTENSION_LOADED, TARGET_EXTENSION_LOADER,
        ExtensionLoadedEvent(extension, loaded_dependencies)
    )

def _send_extension_state_change(
        bus: EventBus,
        state: ExtensionState
) -> None:
    set_state(bus, STATE_EXTENSION_LOADER, ExtensionState, state)
