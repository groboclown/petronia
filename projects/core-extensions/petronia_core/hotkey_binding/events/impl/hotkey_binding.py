# GENERATED CODE - DO NOT MODIFY

"""
Data structures and marshalling for extension petronia.core.api.hotkey_binding version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods,unused-import,invalid-name,consider-using-f-string

# Allow forward references and thus cyclic data types
from __future__ import annotations
from typing import (
    cast,
    List,
    Dict,
    Optional,
    Any,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    StdRet,
    STANDARD_PETRONIA_CATALOG,
    not_none,
    collect_errors_from,
)

EXTENSION_NAME = 'petronia.core.api.hotkey_binding'
EXTENSION_VERSION = (1, 0, 0)


class SetMasterSequenceRequestEvent:
    """
    Sets the primary sequence that begins all hotkey sequences. For example, this
    could be simply the "super" key.
    """
    __slots__ = ('sequence_type', 'keys', 'comment',)
    FULL_EVENT_NAME = 'petronia.core.api.hotkey_binding:set-master-sequence:request'
    SHORT_EVENT_NAME = 'set-master-sequence:request'

    UNIQUE_TARGET_FQN = 'petronia.core.api.hotkey_binding:master-sequence'
    UNIQUE_TARGET_REL = 'master-sequence'

    def __init__(
        self,
        sequence_type: str,
        keys: List[str],
        comment: Optional[str],
    ) -> None:
        self.sequence_type = sequence_type
        self.keys = keys
        self.comment = comment

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return SetMasterSequenceRequestEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'sequence_type': self.sequence_type,
            'keys': list(self.keys),
            'comment': self.comment,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['SetMasterSequenceRequestEvent']:  # pylint: disable=R0912,R0911
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
                name='SetMasterSequenceRequestEvent',
            )
        else:
            if val not in ('meta','sequence', ):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='sequence_type',
                    type='str',
                    name='SetMasterSequenceRequestEvent',
                )
            f_sequence_type = val
        val = data.get('keys')
        f_keys: List[str]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='keys',
                name='SetMasterSequenceRequestEvent',
            )
        else:
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='keys',
                    type='List[str]',
                    name='SetMasterSequenceRequestEvent',
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
                        name='SetMasterSequenceRequestEvent',
                    )
                f_keys.append(item)
        val = data.get('comment')
        f_comment: Optional[str] = None
        if val is not None:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='comment',
                    type='str',
                    name='SetMasterSequenceRequestEvent',
                )
            f_comment = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(SetMasterSequenceRequestEvent(
            sequence_type=not_none(f_sequence_type),
            keys=not_none(f_keys),
            comment=f_comment,
        ))

    def __repr__(self) -> str:
        return "SetMasterSequenceRequestEvent(" + repr(self.export_data()) + ")"


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


class BoundKeyRegisterEvent:
    """
    Binds a key sequence to a triggered event.
    """
    __slots__ = ('keys', 'comment', 'event',)
    FULL_EVENT_NAME = 'petronia.core.api.hotkey_binding:bound-key:register'
    SHORT_EVENT_NAME = 'bound-key:register'

    UNIQUE_TARGET_FQN = 'petronia.core.api.hotkey_binding:key'
    UNIQUE_TARGET_REL = 'key'

    def __init__(
        self,
        keys: List[str],
        comment: Optional[str],
        event: BoundEvent,
    ) -> None:
        self.keys = keys
        self.comment = comment
        self.event = event

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return BoundKeyRegisterEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'keys': list(self.keys),
            'comment': self.comment,
            'event': self.event.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['BoundKeyRegisterEvent']:  # pylint: disable=R0912,R0911
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
                name='BoundKeyRegisterEvent',
            )
        else:
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='keys',
                    type='List[str]',
                    name='BoundKeyRegisterEvent',
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
                        name='BoundKeyRegisterEvent',
                    )
                f_keys.append(item)
        val = data.get('comment')
        f_comment: Optional[str] = None
        if val is not None:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='comment',
                    type='str',
                    name='BoundKeyRegisterEvent',
                )
            f_comment = val
        val = data.get('event')
        f_event: BoundEvent
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='event',
                name='BoundKeyRegisterEvent',
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
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(BoundKeyRegisterEvent(
            keys=not_none(f_keys),
            comment=f_comment,
            event=not_none(f_event),
        ))

    def __repr__(self) -> str:
        return "BoundKeyRegisterEvent(" + repr(self.export_data()) + ")"


class BoundKeyRemoveEvent:
    """
    Remove a bound key sequence.
    """
    __slots__ = ('keys',)
    FULL_EVENT_NAME = 'petronia.core.api.hotkey_binding:bound-key:remove'
    SHORT_EVENT_NAME = 'bound-key:remove'

    UNIQUE_TARGET_FQN = 'petronia.core.api.hotkey_binding:key'
    UNIQUE_TARGET_REL = 'key'

    def __init__(
        self,
        keys: List[str],
    ) -> None:
        self.keys = keys

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return BoundKeyRemoveEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'keys': list(self.keys),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['BoundKeyRemoveEvent']:  # pylint: disable=R0912,R0911
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
                name='BoundKeyRemoveEvent',
            )
        else:
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='keys',
                    type='List[str]',
                    name='BoundKeyRemoveEvent',
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
                        name='BoundKeyRemoveEvent',
                    )
                f_keys.append(item)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(BoundKeyRemoveEvent(
            keys=not_none(f_keys),
        ))

    def __repr__(self) -> str:
        return "BoundKeyRemoveEvent(" + repr(self.export_data()) + ")"


class EventParameterDescription:
    """
    Information about a bound event parameter.
    """
    __slots__ = ('key', 'description', 'default_value',)

    def __init__(
        self,
        key: str,
        description: str,
        default_value: Optional[str],
    ) -> None:
        self.key = key
        self.description = description
        self.default_value = default_value

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'key': self.key,
            'description': self.description,
            'default_value': self.default_value,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['EventParameterDescription']:  # pylint: disable=R0912,R0911
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
                name='EventParameterDescription',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='key',
                    type='str',
                    name='EventParameterDescription',
                )
            f_key = val
        val = data.get('description')
        f_description: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='description',
                name='EventParameterDescription',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='description',
                    type='str',
                    name='EventParameterDescription',
                )
            f_description = val
        val = data.get('default_value')
        f_default_value: Optional[str] = None
        if val is not None:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='default_value',
                    type='str',
                    name='EventParameterDescription',
                )
            f_default_value = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(EventParameterDescription(
            key=not_none(f_key),
            description=not_none(f_description),
            default_value=f_default_value,
        ))

    def __repr__(self) -> str:
        return "EventParameterDescription(" + repr(self.export_data()) + ")"


class ExtensionEventRegisterEvent:
    """
    Registers a description about a known extension's event. This is useful to
    end-users for understanding which key bound events an extension can handle.
    """
    __slots__ = ('name', 'description', 'target_id', 'parameters',)
    FULL_EVENT_NAME = 'petronia.core.api.hotkey_binding:extension-event:register'
    SHORT_EVENT_NAME = 'extension-event:register'

    UNIQUE_TARGET_FQN = 'petronia.core.api.hotkey_binding:extension-event'
    UNIQUE_TARGET_REL = 'extension-event'

    def __init__(
        self,
        name: str,
        description: Optional[str],
        target_id: str,
        parameters: List[EventParameterDescription],
    ) -> None:
        self.name = name
        self.description = description
        self.target_id = target_id
        self.parameters = parameters

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return ExtensionEventRegisterEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'name': self.name,
            'description': self.description,
            'target_id': self.target_id,
            'parameters': [v.export_data() for v in self.parameters],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ExtensionEventRegisterEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('name')
        f_name: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='name',
                name='ExtensionEventRegisterEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='name',
                    type='str',
                    name='ExtensionEventRegisterEvent',
                )
            f_name = val
        val = data.get('description')
        f_description: Optional[str] = None
        if val is not None:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='description',
                    type='str',
                    name='ExtensionEventRegisterEvent',
                )
            f_description = val
        val = data.get('target_id')
        f_target_id: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='target_id',
                name='ExtensionEventRegisterEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='target_id',
                    type='str',
                    name='ExtensionEventRegisterEvent',
                )
            f_target_id = val
        val = data.get('parameters')
        f_parameters: List[EventParameterDescription]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='parameters',
                name='ExtensionEventRegisterEvent',
            )
        else:
            f_parameters = []
            for item in val:
                parsed_parameters = EventParameterDescription.parse_data(item)
                if parsed_parameters.has_error:
                    return parsed_parameters.forward()
                f_parameters.append(parsed_parameters.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ExtensionEventRegisterEvent(
            name=not_none(f_name),
            description=f_description,
            target_id=not_none(f_target_id),
            parameters=not_none(f_parameters),
        ))

    def __repr__(self) -> str:
        return "ExtensionEventRegisterEvent(" + repr(self.export_data()) + ")"


class HotkeyFiredEvent:
    """
    A bound hotkey event fired.
    """
    __slots__ = ('event',)
    FULL_EVENT_NAME = 'petronia.core.api.hotkey_binding:hotkey-fired'
    SHORT_EVENT_NAME = 'hotkey-fired'

    UNIQUE_TARGET_FQN = 'petronia.core.api.hotkey_binding:hotkey'
    UNIQUE_TARGET_REL = 'hotkey'

    def __init__(
        self,
        event: BoundEvent,
    ) -> None:
        self.event = event

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return HotkeyFiredEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'event': self.event.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['HotkeyFiredEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('event')
        f_event: BoundEvent
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='event',
                name='HotkeyFiredEvent',
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
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(HotkeyFiredEvent(
            event=not_none(f_event),
        ))

    def __repr__(self) -> str:
        return "HotkeyFiredEvent(" + repr(self.export_data()) + ")"


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


class BoundKeysState:
    """
    All the bound key sequences and their triggered event data.
    """
    __slots__ = ('sequence_type', 'master_sequence', 'bindings',)

    UNIQUE_TARGET_FQN = 'petronia.core.api.hotkey_binding:bound-keys'
    UNIQUE_TARGET_REL = 'petronia.core.api.hotkey_binding:bound-keys'

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
    def parse_data(data: Dict[str, Any]) -> StdRet['BoundKeysState']:  # pylint: disable=R0912,R0911
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
                name='BoundKeysState',
            )
        else:
            if val not in ('meta','sequence', ):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='sequence_type',
                    type='str',
                    name='BoundKeysState',
                )
            f_sequence_type = val
        val = data.get('master_sequence')
        f_master_sequence: List[str]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='master_sequence',
                name='BoundKeysState',
            )
        else:
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='master_sequence',
                    type='List[str]',
                    name='BoundKeysState',
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
                        name='BoundKeysState',
                    )
                f_master_sequence.append(item)
        val = data.get('bindings')
        f_bindings: List[BoundHotkey]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='bindings',
                name='BoundKeysState',
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
        return StdRet.pass_ok(BoundKeysState(
            sequence_type=not_none(f_sequence_type),
            master_sequence=not_none(f_master_sequence),
            bindings=not_none(f_bindings),
        ))

    def __repr__(self) -> str:
        return "BoundKeysState(" + repr(self.export_data()) + ")"


class Events:
    """
    (no description)
    """
    __slots__ = ('name', 'description', 'target_id', 'parameters',)

    def __init__(
        self,
        name: str,
        description: Optional[str],
        target_id: str,
        parameters: List[EventParameterDescription],
    ) -> None:
        self.name = name
        self.description = description
        self.target_id = target_id
        self.parameters = parameters

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'name': self.name,
            'description': self.description,
            'target_id': self.target_id,
            'parameters': [v.export_data() for v in self.parameters],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['Events']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('name')
        f_name: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='name',
                name='Events',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='name',
                    type='str',
                    name='Events',
                )
            f_name = val
        val = data.get('description')
        f_description: Optional[str] = None
        if val is not None:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='description',
                    type='str',
                    name='Events',
                )
            f_description = val
        val = data.get('target_id')
        f_target_id: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='target_id',
                name='Events',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='target_id',
                    type='str',
                    name='Events',
                )
            f_target_id = val
        val = data.get('parameters')
        f_parameters: List[EventParameterDescription]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='parameters',
                name='Events',
            )
        else:
            f_parameters = []
            for item in val:
                parsed_parameters = EventParameterDescription.parse_data(item)
                if parsed_parameters.has_error:
                    return parsed_parameters.forward()
                f_parameters.append(parsed_parameters.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(Events(
            name=not_none(f_name),
            description=f_description,
            target_id=not_none(f_target_id),
            parameters=not_none(f_parameters),
        ))

    def __repr__(self) -> str:
        return "Events(" + repr(self.export_data()) + ")"


class ExtensionEventsState:
    """
    All events registered by extensions for usable events.
    """
    __slots__ = ('events',)

    UNIQUE_TARGET_FQN = 'petronia.core.api.hotkey_binding:extension-events'
    UNIQUE_TARGET_REL = 'petronia.core.api.hotkey_binding:extension-events'

    def __init__(
        self,
        events: List[Events],
    ) -> None:
        self.events = events

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'events': [v.export_data() for v in self.events],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ExtensionEventsState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('events')
        f_events: List[Events]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='events',
                name='ExtensionEventsState',
            )
        else:
            f_events = []
            for item in val:
                parsed_events = Events.parse_data(item)
                if parsed_events.has_error:
                    return parsed_events.forward()
                f_events.append(parsed_events.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ExtensionEventsState(
            events=not_none(f_events),
        ))

    def __repr__(self) -> str:
        return "ExtensionEventsState(" + repr(self.export_data()) + ")"


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
