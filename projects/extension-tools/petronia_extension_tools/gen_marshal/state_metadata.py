"""Loads the state-data section for an extension metadata file."""

from typing import Iterable, List, Dict, Any
from petronia_common.extension.config.event_schema import StructureEventDataType
from petronia_common.extension.config.event_loader import (
    load_event_structure_data_type, parse_references,
)
from petronia_common.util import StdRet


class StateData:
    """Definition for the state data."""
    __slots__ = ('__fqn', '__short_name', '__data_type',)

    def __init__(
            self,
            fqn: str,
            short_name: str, data_type: StructureEventDataType,
    ) -> None:
        self.__fqn = fqn
        self.__short_name = short_name
        self.__data_type = data_type

    @property
    def short_name(self) -> str:
        """Name of the state data, without the extension name."""
        return self.__short_name

    @property
    def fqn(self) -> str:
        """Formal ID of the state data."""
        return self.__fqn

    @property
    def data_type(self) -> StructureEventDataType:
        """Stored data type."""
        return self.__data_type


def parse_state_data(
        extension_name: str, raw_extension_data: Dict[str, Any],
) -> StdRet[Iterable[StateData]]:
    """Parse the state-data structures from inside the extension metadata structure."""
    raw_state_data = raw_extension_data.get('state-data')
    state_data: List[StateData] = []
    if isinstance(raw_state_data, dict):
        raw_references = raw_extension_data.get('references', {})
        parsed_references_res = parse_references(raw_references)
        if not parsed_references_res.ok:
            return parsed_references_res.forward()
        parsed_references = parsed_references_res.result
        for key, value in raw_state_data.items():
            if not isinstance(value, dict):
                continue
            structure_res = load_event_structure_data_type(key, value, parsed_references)
            if structure_res.has_error:
                return structure_res.forward()
            data_type = structure_res.result
            if not isinstance(data_type, StructureEventDataType):
                # This is an internal error...
                raise RuntimeError(  # pragma no cover
                    f'Incorrectly re-formatted structure to {data_type}',
                )
            state_data.append(StateData(
                f'{extension_name}:{key}',
                key, data_type,
            ))
    return StdRet.pass_ok(state_data)
