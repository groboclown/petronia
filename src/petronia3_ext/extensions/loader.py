
"""
Loads extensions into the system.
"""

import os
# import zipimport
import importlib
import importlib.util
import importlib.machinery
from types import ModuleType
from typing import List, Callable
from ..api.state import ExtensionConfiguration, ExtensionState
from ....system.bus import EventBus
from ....system.logging import log, logerr, DEBUG, INFO, ERROR
from ....errors import (
    PetroniaInternalError,
    PetroniaExtensionNotFound,
    PetroniaInvalidExtension,
    PetroniaCyclicExtensionDependency,
    PetroniaExtensionInitializationError,
)
from ....util.memory import EMPTY_TUPLE

ModuleLoadedCallback = Callable[[str], None]

class _LoadState:
    __slots__ = ('loading', 'loaded', 'state', 'config', 'bus', 'origin', 'pathfinder')
    loading: List[str]
    loaded: List[str]

    def __init__(
            self, origin: str,
            bus: EventBus,
            config: ExtensionConfiguration,
            state: ExtensionState
    ) -> None:
        self.origin = origin
        self.bus = bus
        self.config = config
        self.state = state
        self.loading = []
        self.loaded = []
        self.pathfinder = importlib.machinery.PathFinder()


def load_extension(
        name: str,
        bus: EventBus,
        config: ExtensionConfiguration,
        state: ExtensionState
) -> ExtensionState:
    """
    Add an extension to the system.  The extension must know how to
    properly register itself.  The configuration setup for the extension
    must be performed as setting the state after the extension is added.

    If an extension name starts with 'core.', then the petronia core
    extensions are searched.  Otherwise, only the paths are searched.
    """
    if name in state.loaded_extensions:
        return state
    importlib.invalidate_caches()
    lstate = _LoadState(name, bus, config, state)
    _internal_load(name, lstate)
    loaded = list(state.loaded_extensions)
    loaded.extend(lstate.loaded)
    return ExtensionState(loaded)


def _internal_load(
        name: str, lstate: _LoadState
) -> None:
    if name in lstate.state.loaded_extensions or name in lstate.loaded:
        # Dependency was already loaded.  Don't do anything.
        return
    if name in lstate.loading:
        raise PetroniaCyclicExtensionDependency(name, lstate.loading, lstate.loaded)
    lstate.loading.append(name)
    if name.startswith('core.'):
        formal_name = 'petronia3.extensions.' + name[5:]
        log(DEBUG, load_extension, 'loading internal module {0}', formal_name)
        mod_spec = importlib.util.find_spec(formal_name)
        if mod_spec is None:
            raise PetroniaExtensionNotFound(name, lstate.loaded)
        _load_extension_from_module_spec(name, mod_spec, lstate)
    else:
        _try_dirs(name, lstate)
    lstate.loading.remove(name)
    lstate.loaded.append(name)


def _try_dirs(
        name: str, lstate: _LoadState
) -> None:
    paths: List[str] = []
    for zipdir in lstate.config.zip_dirs:
        if os.path.isdir(zipdir):
            for filename in os.listdir(zipdir):
                fpath = os.path.join(zipdir, filename)
                if os.path.isfile(fpath) and fpath.endswith('.zip'):
                    paths.append(fpath)
    paths.extend(lstate.config.paths)

    mod_spec = lstate.pathfinder.find_spec(fullname=name, path=paths)
    if mod_spec is None:
        raise PetroniaExtensionNotFound(name, lstate.loaded)
    return _load_extension_from_module_spec(name, mod_spec, lstate)


def _load_extension_from_module_spec(
        name: str,
        mod_spec: importlib.machinery.ModuleSpec,
        lstate: _LoadState
) -> None:
    if not mod_spec.loader:
        raise PetroniaInternalError('`loader` not defined on module specification')

    try:
        mod = importlib.util.module_from_spec(mod_spec)

        # MyPy doesn't see the "exec_module" on the loader, but it's there.
        mod_spec.loader.exec_module(mod) # type: ignore
    except Exception as err: # pylint: disable=broad-except
        logerr(ERROR, load_extension, err, 'Failed when processing module {0}'.format(mod_spec))
        raise PetroniaInvalidExtension(name, lstate.loaded, str(err))
    _load_extension_from_module(name, mod, lstate)


def _load_extension_from_module(
        name: str,
        mod: ModuleType,
        lstate: _LoadState
) -> None:
    # Ensure the module has the required attributes.
    dependencies = EMPTY_TUPLE # type: ignore
    if hasattr(mod, 'EXTENSION_DEPENDENCIES') and isinstance(mod, tuple): # type: ignore
        dependencies = mod.EXTENSION_DEPENDENCIES # type: ignore
    if not hasattr(mod, 'start_extension') or not callable(mod.start_extension): # type: ignore
        raise PetroniaInvalidExtension(
            name, lstate.loaded,
            'module does not provide function `start_extension`'
        )
    if dependencies: # type: ignore
        for dep in dependencies: # type: ignore
            if isinstance(dep, str): # type: ignore
                _internal_load(dep, lstate)
    try:
        mod.start_extension(lstate.bus) # type: ignore
        log(INFO, load_extension, 'loaded extension {0}', name)
    except BaseException as err: # pylint: disable=broad-except
        logerr(ERROR, load_extension, err, 'module {0} failed to load', name)
        raise PetroniaExtensionInitializationError(name, lstate.loaded, err)
