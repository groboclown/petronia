"""
Loads the extension documentation.
"""

from typing import List, Sequence, Iterable, Dict, Any
import json
import collections
from petronia_common.util import (
    StdRet,
    load_yaml_documents, join_results,
    STANDARD_PETRONIA_CATALOG,
)
from petronia_common.util import i18n as _
from petronia_common.extension.config import AbcExtensionMetadata, ApiExtensionMetadata, EventType
from petronia_common.extension.config.extension_loader import load_extension
from .state_metadata import StateData, parse_state_data


class ExtensionDataFile:
    """Fully parsed extension metadata."""
    __slots__ = ('metadata', 'state_data',)

    def __init__(self, metadata: AbcExtensionMetadata, state_data: Iterable[StateData]) -> None:
        self.metadata = metadata
        self.state_data = tuple(state_data)

    @property
    def events(self) -> Sequence[EventType]:
        """Get the events, if any are present."""
        if isinstance(self.metadata, ApiExtensionMetadata):
            return self.metadata.events
        return ()


def load_extension_file(filename: str) -> StdRet[Sequence[ExtensionDataFile]]:
    """Load the metadata from the extension file."""
    if filename.lower().endswith('.json'):
        with open(filename, 'r') as f:
            ret_data = json.load(f)
    elif filename.lower().endswith('.yaml') or filename.lower().endswith('.yml'):
        with open(filename, 'r') as f:
            ret_data = load_yaml_documents(f.read())
    else:
        return StdRet.pass_errmsg(
            STANDARD_PETRONIA_CATALOG,
            _('Invalid extension metadata file type: {name}'), name=filename,
        )
    if ret_data.has_error:
        # Strange.
        # MyPy is reporting "Returning Any from function declared to return ..."
        # return ret_data.forward()
        return StdRet.pass_error(ret_data.valid_error)

    data = ret_data.result
    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, collections.abc.Iterable):
        return StdRet.pass_errmsg(
            STANDARD_PETRONIA_CATALOG,
            _(
                'Extension metadata file ({name}) must contain a dictionary '
                'or a list of dictionaries, found {data}'
            ),
            name=filename,
            data=repr(data),
        )

    ret: List[StdRet[ExtensionDataFile]] = []
    for item in data:
        if not isinstance(item, dict):
            ret.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _(
                    'Extension metadata file ({name}) must contain a dictionary '
                    'or a list of dictionaries'
                ),
                name=filename,
            ))
        else:
            ret.append(process_extension(item))
    return join_results(tuple, *ret)


def process_extension(data: Dict[str, Any]) -> StdRet[ExtensionDataFile]:
    """Process the extension section."""
    ret_ext = load_extension(data)
    if ret_ext.has_error:
        return ret_ext.forward()
    ret_state_data = parse_state_data(ret_ext.result.name, data)
    if ret_state_data.has_error:
        return ret_state_data.forward()
    return StdRet.pass_ok(ExtensionDataFile(ret_ext.result, ret_state_data.result))
