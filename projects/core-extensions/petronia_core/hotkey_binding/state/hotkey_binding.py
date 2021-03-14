# GENERATED CODE - DO NOT MODIFY

"""
Data structures and marshalling for extension petronia_core.hotkey_binding version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods

# Allow forward references and thus cyclic data types
from __future__ import annotations
from typing import (
    Any,
    Dict,
    Optional,
    List,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    STANDARD_PETRONIA_CATALOG,
    not_none,
    StdRet,
    collect_errors_from,
)

EXTENSION_NAME = 'petronia_core.hotkey_binding'
EXTENSION_VERSION = (1, 0, 0)


class BoundEventParameter:
    """
    A single parameter value sent with a triggered bound hotkey event.
    """
    __slots__ = ('key', 'value',)

    def __init__(
        self,
        key: str,
        value: str,
    ) -> None:
        self.key = key
        self.value = value

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'key': self.key,
            'value': self.value,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['BoundEventParameter']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('key')
        f_key: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='key',
                name='BoundEventParameter',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='key',
                    type='str',
                    name='BoundEventParameter',
                )
            f_key = val
        val = data.get('value')
        f_value: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='value',
                name='BoundEventParameter',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='value',
                    type='str',
                    name='BoundEventParameter',
                )
            f_value = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(BoundEventParameter(
            key=not_none(f_key),
            value=not_none(f_value),
        ))

    def __repr__(self) -> str:
        return "BoundEventParameter(" + repr(self.export_data()) + ")"


class BoundEvent:
    """
    Generated event details that are sent when a bound key sequence is pressed.
    """
    __slots__ = ('target_id', 'parameters',)

    def __init__(
        self,
        target_id: str,
        parameters: List[BoundEventParameter],
    ) -> None:
        self.target_id = target_id
        self.parameters = parameters

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'target_id': self.target_id,
            'parameters': [v.export_data() for v in self.parameters],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['BoundEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('target_id')
        f_target_id: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='target_id',
                name='BoundEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='target_id',
                    type='str',
                    name='BoundEvent',
                )
            f_target_id = val
        val = data.get('parameters')
        f_parameters: List[BoundEventParameter]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='parameters',
                name='BoundEvent',
            )
        else:
            f_parameters = []
            for item in val:
                parsed_parameters = BoundEventParameter.parse_data(item)
                if parsed_parameters.has_error:
                    return parsed_parameters.forward()
                f_parameters.append(parsed_parameters.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(BoundEvent(
            target_id=not_none(f_target_id),
            parameters=not_none(f_parameters),
        ))

    def __repr__(self) -> str:
        return "BoundEvent(" + repr(self.export_data()) + ")"


class BoundHotkey:
    """
    A single hotkey sequence bound to an event.
    """
    __slots__ = ('keys', 'event', 'comment',)

    def __init__(
        self,
        keys: List[str],
        event: BoundEvent,
        comment: Optional[str],
    ) -> None:
        self.keys = keys
        self.event = event
        self.comment = comment

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'keys': list(self.keys),
            'event': self.event.export_data(),
            'comment': self.comment,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['BoundHotkey']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('keys')
        f_keys: List[str]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='keys',
                name='BoundHotkey',
            )
        else:
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='keys',
                    type='List[str]',
                    name='BoundHotkey',
                )
            f_keys = []
            for item in val:
                if not isinstance(item, str):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='keys',
                        type='str',
                        name='BoundHotkey',
                    )
                f_keys.append(item)
        val = data.get('event')
        f_event: BoundEvent
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='event',
                name='BoundHotkey',
            )
        else:
            parsed_event = BoundEvent.parse_data(val)
            if parsed_event.has_error:
                return parsed_event.forward()
            if parsed_event.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='event',
                )
            f_event = parsed_event.result
        val = data.get('comment')
        f_comment: Optional[str] = None
        if val is not None:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='comment',
                    type='str',
                    name='BoundHotkey',
                )
            f_comment = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(BoundHotkey(
            keys=not_none(f_keys),
            event=not_none(f_event),
            comment=f_comment,
        ))

    def __repr__(self) -> str:
        return "BoundHotkey(" + repr(self.export_data()) + ")"


class BoundKeys:
    """
    All the bound key sequences and their triggered event data.
    """
    __slots__ = ('sequence_type', 'master_sequence', 'bindings',)

    def __init__(
        self,
        sequence_type: str,
        master_sequence: List[str],
        bindings: List[BoundHotkey],
    ) -> None:
        self.sequence_type = sequence_type
        self.master_sequence = master_sequence
        self.bindings = bindings

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'sequence_type': self.sequence_type,
            'master_sequence': list(self.master_sequence),
            'bindings': [v.export_data() for v in self.bindings],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['BoundKeys']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('sequence_type')
        f_sequence_type: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='sequence_type',
                name='BoundKeys',
            )
        else:
            if val not in ('sequence','meta', ):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='sequence_type',
                    type='str',
                    name='BoundKeys',
                )
            f_sequence_type = val
        val = data.get('master_sequence')
        f_master_sequence: List[str]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='master_sequence',
                name='BoundKeys',
            )
        else:
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='master_sequence',
                    type='List[str]',
                    name='BoundKeys',
                )
            f_master_sequence = []
            for item in val:
                if not isinstance(item, str):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='master_sequence',
                        type='str',
                        name='BoundKeys',
                    )
                f_master_sequence.append(item)
        val = data.get('bindings')
        f_bindings: List[BoundHotkey]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='bindings',
                name='BoundKeys',
            )
        else:
            f_bindings = []
            for item in val:
                parsed_bindings = BoundHotkey.parse_data(item)
                if parsed_bindings.has_error:
                    return parsed_bindings.forward()
                f_bindings.append(parsed_bindings.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(BoundKeys(
            sequence_type=not_none(f_sequence_type),
            master_sequence=not_none(f_master_sequence),
            bindings=not_none(f_bindings),
        ))

    def __repr__(self) -> str:
        return "BoundKeys(" + repr(self.export_data()) + ")"


class ConfigurationState:
    """
    User configuration data.
    """
    __slots__ = ('bindings',)

    UNIQUE_TARGET_FQN = 'petronia_core.hotkey_binding:configuration'
    UNIQUE_TARGET_REL = 'petronia_core.hotkey_binding:configuration'

    def __init__(
        self,
        bindings: BoundKeys,
    ) -> None:
        self.bindings = bindings

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'bindings': self.bindings.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ConfigurationState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('bindings')
        f_bindings: BoundKeys
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='bindings',
                name='ConfigurationState',
            )
        else:
            parsed_bindings = BoundKeys.parse_data(val)
            if parsed_bindings.has_error:
                return parsed_bindings.forward()
            if parsed_bindings.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='bindings',
                )
            f_bindings = parsed_bindings.result
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ConfigurationState(
            bindings=not_none(f_bindings),
        ))

    def __repr__(self) -> str:
        return "ConfigurationState(" + repr(self.export_data()) + ")"


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
