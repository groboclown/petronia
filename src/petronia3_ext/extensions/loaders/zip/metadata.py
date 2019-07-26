
# mypy: allow-any-expr
# mypy: allow-any-explicit
# mypy: allow-any-generics

"""
Read the JSON metadata from the zip file.
"""

import zipfile
import json
from typing import Dict, Optional, Any
from petronia3.system.bus import EventBus
from petronia3.errors import PetroniaExtensionError, PetroniaInternalError
from ...defs import DiscoveredExtension, INSECURE_ANY_VERSION

METADATA_FILENAME = 'manifest.json'
MAXIMUM_FILE_LENGTH = 1024 * 1024 # 1 mb

def read_zipfile_metadata_contents(zip_filename: str) -> Optional[str]:
    """
    Reads the metadata from the contents without checking if it's a valid
    JSON file.
    """
    if not zipfile.is_zipfile(zip_filename):
        return None

    with zipfile.ZipFile(zip_filename) as zipf:
        try:
            info = zipf.getinfo(METADATA_FILENAME)
            if info.is_dir() or info.file_size > MAXIMUM_FILE_LENGTH:
                return None
            with zipf.open(info) as inp:
                return inp.read().decode('utf-8')
        except KeyError:
            return None


def is_metadata_valid(metadata: str) -> Optional[Dict[str, Any]]:
    """
    Checks if the metadata contents are valid.  If valid, returns the contents
    as a dictionary.
    """
    try:
        value = json.loads(metadata)
        if not isinstance(value, dict):
            return None

        # inspect the internal data of the structure by
        # using the discover object's constructor checks.
        # If it's not valid, then the constructor will raise
        # an error.
        DiscoveredExtension(
            'test',
            INSECURE_ANY_VERSION,
            value,
            _never_call_module_loader
        )

        return value
    except json.JSONDecodeError:
        return None
    except PetroniaExtensionError:
        return None

def _never_call_module_loader(bus: EventBus) -> None:
    raise PetroniaInternalError('should not be called')
