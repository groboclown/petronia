
"""
Add the extensions into the system.
"""

from typing import Sequence, Set, List, Tuple, Iterable, Optional
from ...base.security import SandboxPermission
from ...core.extensions.api import (
    ExtensionLoadedEvent,
    ExtensionState,
    LoadedExtension,
    ExtensionLoaderSetup,
    ANY_VERSION,
)
from ...core.extensions.api.events import (
    TARGET_EXTENSION_LOADER,
    EVENT_ID_EXTENSION_LOADED,
    EVENT_ID_REQUEST_LOAD_EXTENSION,
    RequestLoadExtensionEvent,
)
from ...core.extensions.api.state import (
    STATE_EXTENSION_LOADER,
)
from ...core.state.api import (
    set_state,
)
from ...base import (
    EventBus,
    EventId,
    EventCallback,
    ParticipantId,
    log,
    DEBUG,
    ERROR,
)
from ...base.bus import (
    ListenerSetup,
    ExtensionMetadataStruct,
)
from ...errors import (
    PetroniaExtensionNotFound,
    PetroniaExtensionError,
)
from .defs import (
    ExtensionLoader,
)
from .create_loader import create_extension_loader
from .ext_loader import (
    load_additional_extensions,
)


def compatible_start_extension(bus: EventBus) -> None: # pylint: disable=unused-argument
    """For extension compatibility.  Doesn't do anything."""


EXTENSION_METADATA: ExtensionMetadataStruct = {
    "type": "impl",
    "implements": [
        {
            "extension": "core.extensions.api",
            "minimum": ANY_VERSION,
        },
    ],
    "depends": [
        {
            "extension": "core.state.api",
            "minimum": ANY_VERSION,
        }
    ],

    "name": "default.extensions",
    "version": (1, 0, 0,),
    "authors": ["Petronia"],
}


def bootstrap_extension_loader(
        bus: EventBus,
        setup: ExtensionLoaderSetup
) -> None:
    """
    Adds the extension loader into the bus.  Because the extensions loader has
    very specific, immutable security concerns, it must be loaded at boot time
    with configuration state.
    """

    module_dirs: List[Tuple[str, Optional[Iterable[SandboxPermission]]]] = [
        (secure_path, None,) for secure_path in setup.secure_paths
    ]
    module_dirs.extend(setup.sandbox_paths)

    zip_dirs: List[Tuple[str, Optional[Iterable[SandboxPermission]]]] = [
        (secure_path, None,) for secure_path in setup.secure_zip_dirs
    ]
    zip_dirs.extend(setup.sandbox_zip_dirs)

    loader = create_extension_loader(
        setup.cache_dir,
        module_dirs,
        zip_dirs
    )

    loaded = list(setup.preloaded_extensions)
    # Add in ourself to the list of preloaded extensions.
    loaded.append(LoadedExtension('default.extensions', True, (1, 0, 0,)))
    for extensions in setup.initial_extension_groups:
        # load_additional_extensions returns newly loaded extensions only
        log(
            DEBUG, bootstrap_extension_loader,
            'Loading extension group {0}, using already loaded extensions {1}',
            extensions, loaded
        )
        loaded.extend(load_additional_extensions(extensions, loader, bus, loaded))

    ext_loader = _ExtensionStatefulLoader(bus, ExtensionState(loaded), loader)
    bus.add_listener(
        TARGET_EXTENSION_LOADER,
        _as_request_load_extension_listener,
        ext_loader.on_extension_load_request
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
        try:
            deps = load_additional_extensions(
                (event_object.extension_name,),
                self.__loader,
                self.__bus,
                self._loaded
            )
        except PetroniaExtensionError as err:
            log(
                ERROR,
                load_additional_extensions,
                'Failed to load extension {0}: {2}; already loaded extensions {1}',
                event_object.extension_name,
                ", ".join([ext.name for ext in self._loaded]),
                str(err)
            )
            return
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
