"""
Loads the extension documentation.
"""

from typing import List, Sequence, Iterable, Dict, Any
from petronia_common.util import (
    StdRet,
    load_structured_file, join_results,
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
    res_data = load_structured_file(filename)
    if res_data.has_error:
        return res_data.forward()

    data = res_data.result
    if isinstance(data, dict):
        data = [data]

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
