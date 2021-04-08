
"""
Create the extension loader.
"""

from typing import List, Iterable, cast
import os
import importlib
from ...base import EventBus
from ...core.extensions.api import (
    LoadedExtension,
    EXTENSION_LOADER_MODULE_BOOTSTRAP_FUNCTION_NAME,
    ExtensionLoaderSetup,
    ExtensionLoaderBootstrapFunction,
)
from ...core.platform.preboot import DiscoveryData
from .args import UserArguments


def bootstrap_extension_extension(
        bus: EventBus, data: DiscoveryData,
        args: UserArguments,
        already_loaded_extensions: Iterable[LoadedExtension]
) -> None:
    """
    Create the extension loader and register it to the event bus.
    """
    extension_sets: List[Iterable[str]] = list(data.preboot_extensions)
    extension_sets.append(args.preboot_extensions)
    extension_sets.extend(data.extension_sets)
    # Add the already loaded extensions at the end, so that any default
    # API implementation that hasn't been loaded will be added.
    extension_sets.append([ext.name for ext in already_loaded_extensions])
    cache_dir = os.path.join(data.temp_dir, 'extension-cache')
    if not os.path.isdir(cache_dir):
        os.mkdir(cache_dir)
    setup = ExtensionLoaderSetup(
        data.ext_paths.secure_paths,
        data.ext_paths.sandbox_paths,
        data.ext_paths.secure_zip_dirs,
        data.ext_paths.sandbox_zip_dirs,
        already_loaded_extensions,
        extension_sets,
        cache_dir
    )
    # TODO Error checking?
    module = importlib.import_module(data.extension_loader_module.name)
    loader_func = cast(
        ExtensionLoaderBootstrapFunction,
        getattr(module, EXTENSION_LOADER_MODULE_BOOTSTRAP_FUNCTION_NAME)
    )
    loader_func(bus, setup)
