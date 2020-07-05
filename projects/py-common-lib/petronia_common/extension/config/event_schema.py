
"""
Events have a common structure.

See `docs/events.md` for details.
"""

from typing import Literal, Sequence, Dict, List, Iterable, Tuple, Optional, Union, Any
from abc import ABC
import re
import datetime
from .defs import AbcConfigType
from ...util import PetroniaReturnError, UserMessage, possible_error, StdRet, readonly_dict
from ...util import i18n as _


EventDataType = Literal[
    # Simple types
    "string", "int", "float", "bool", "enum", "datetime",

    # Complex types
    "array", "structure", "selector",

    # intermediate types
    "reference",
]


class AbcEventDataType(AbcConfigType, ABC):
    __slots__ = ('__type_name', '__description',)

    def __init__(
            self,
            type_name: EventDataType,
            description: Optional[str],
    ) -> None:
        self.__type_name = type_name
        self.__description = description

    @property
    def type_name(self) -> EventDataType:
        return self.__type_name

    @property
    def description(self) -> Optional[str]:
        return self.__description

    def validate_value(self, value: Any) -> bool:
        raise NotImplementedError()


class BoolEventDataType(AbcEventDataType):
    __slots__ = ()

    def __init__(self, description: Optional[str]) -> None:
        AbcEventDataType.__init__(self, "bool", description)

    def __repr__(self) -> str:
        return f'BoolEventDataType({repr(self.description)})'

    def validate_type(self) -> Optional[PetroniaReturnError]:
        return None

    def validate_value(self, value: Any) -> bool:
        return isinstance(value, bool)


MIN_STRING_LENGTH = 0
MAX_STRING_LENGTH = 65535
DEFAULT_MIN_STRING_LENGTH = 0
DEFAULT_MAX_STRING_LENGTH = 255


class StringEventDataType(AbcEventDataType):
    __slots__ = ('__min_length', '__max_length')

    def __init__(
            self,
            description: Optional[str],
            min_length: Union[int, float],
            max_length: Union[int, float],
    ) -> None:
        AbcEventDataType.__init__(self, "string", description)
        self.__min_length = int(min_length)
        self.__max_length = int(max_length)

    def __repr__(self) -> str:
        return (
            f'StringEventDataType({repr(self.description)}, '
            f'min_length={self.min_length}, '
            f'max_length = {self.max_length})'
        )

    @property
    def min_length(self) -> int:
        return self.__min_length

    @property
    def max_length(self) -> int:
        return self.__max_length

    def validate_type(self) -> Optional[PetroniaReturnError]:
        messages: List[UserMessage] = []
        if self.min_length > self.max_length:
            messages.append(UserMessage(
                _('min_length ({min_length}) must be equal to or less than max_length ({max_length})'),
                min_length=self.min_length,
                max_length=self.max_length,
            ))
        if self.min_length < MIN_STRING_LENGTH:
            messages.append(UserMessage(
                _('min_length ({min_length}) must be greater than or equal to {MIN_STRING_LENGTH}'),
                min_length=self.min_length,
                MIN_STRING_LENGTH=MIN_STRING_LENGTH,
            ))
        if self.max_length > MAX_STRING_LENGTH:
            messages.append(UserMessage(
                _('max_length ({max_length}) must be less than or equal to {MAX_STRING_LENGTH}'),
                max_length=self.max_length,
                MAX_STRING_LENGTH=MAX_STRING_LENGTH,
            ))
        return possible_error(messages)

    def validate_value(self, value: Any) -> bool:
        if not isinstance(value, str):
            return False
        if not (self.min_length <= len(value) <= self.max_length):
            return False
        return True


MIN_INT_VALUE = -9223372036854775808
MAX_INT_VALUE = 9223372036854775807
DEFAULT_MIN_INT_VALUE = MIN_INT_VALUE
DEFAULT_MAX_INT_VALUE = MAX_INT_VALUE


class IntEventDataType(AbcEventDataType):
    __slots__ = ('__min_value', '__max_value')

    def __init__(
            self,
            description: Optional[str],
            min_value: Union[float, int],
            max_value: Union[float, int],
    ) -> None:
        AbcEventDataType.__init__(self, "int", description)
        self.__min_value = int(min_value)
        self.__max_value = int(max_value)

    def __repr__(self) -> str:
        return (
            f'IntEventDataType({repr(self.description)}, '
            f'min_value={self.min_value}, '
            f'max_value={self.max_value})'
        )

    @property
    def min_value(self) -> int:
        return self.__min_value

    @property
    def max_value(self) -> int:
        return self.__max_value

    def validate_type(self) -> Optional[PetroniaReturnError]:
        messages: List[UserMessage] = []
        if self.min_value > self.max_value:
            messages.append(UserMessage(
                _('min_value ({min_value}) must be equal to or less than max_value ({max_value})'),
                min_value=self.min_value,
                max_value=self.max_value,
            ))
        if self.min_value < MIN_INT_VALUE:
            messages.append(UserMessage(
                _('min_length ({min_value}) must be greater than or equal to {MIN_INT_VALUE}'),
                min_value=self.min_value,
                MIN_INT_VALUE=MIN_INT_VALUE,
            ))
        if self.max_value > MAX_INT_VALUE:
            messages.append(UserMessage(
                _('max_value ({max_value}) must be less than or equal to {MAX_INT_VALUE}'),
                max_value=self.max_value,
                MAX_INT_VALUE=MAX_INT_VALUE,
            ))
        return possible_error(messages)

    def validate_value(self, value: Any) -> bool:
        if not isinstance(value, (int, float)):
            return False
        if not (self.min_value <= value <= self.max_value):
            return False
        return True


class FloatEventDataType(AbcEventDataType):
    __slots__ = ('__min_value', '__max_value')

    def __init__(
            self,
            description: Optional[str],
            min_value: Optional[float],
            max_value: Optional[float],
    ) -> None:
        AbcEventDataType.__init__(self, "float", description)
        self.__min_value = min_value
        self.__max_value = max_value

    def __repr__(self) -> str:
        return (
            f'FloatEventDataType({repr(self.description)}, '
            f'min_value={self.min_value}, '
            f'max_value={self.max_value})'
        )

    @property
    def min_value(self) -> Optional[float]:
        return self.__min_value

    @property
    def max_value(self) -> Optional[float]:
        return self.__max_value

    def validate_type(self) -> Optional[PetroniaReturnError]:
        messages: List[UserMessage] = []
        if self.min_value is not None and self.max_value is not None and self.min_value > self.max_value:
            messages.append(UserMessage(
                _('min_value ({min_value}) must be equal to or less than max_value ({max_value})'),
                min_value=self.min_value,
                max_value=self.max_value,
            ))
        return possible_error(messages)

    def validate_value(self, value: Any) -> bool:
        if not isinstance(value, (int, float)):
            return False
        if self.min_value is not None and value < self.min_value:
            return False
        if self.max_value is not None and value > self.max_value:
            return False
        return True


MIN_ENUM_VALUE_LENGTH = 1
MAX_ENUM_VALUE_LENGTH = 255


class EnumEventDataType(AbcEventDataType):
    __slots__ = ('__values',)

    def __init__(
            self,
            description: Optional[str],
            values: Iterable[str],
    ) -> None:
        AbcEventDataType.__init__(self, "enum", description)
        self.__values = set(values)

    def __repr__(self) -> str:
        return f'EnumEventDataType({repr(self.description)}, values={repr(self.__values)})'

    @property
    def values(self) -> Sequence[str]:
        return tuple(self.__values)

    def validate_type(self) -> Optional[PetroniaReturnError]:
        messages: List[UserMessage] = []
        if len(self.__values) <= 0:
            messages.append(UserMessage(
                _('value list must contain at least 1 item')
            ))
        for v in self.__values:
            if not isinstance(v, str):
                messages.append(UserMessage(
                    _('enum value {value} must be a string'),
                    value=v,
                ))
            else:
                if len(v) < MIN_ENUM_VALUE_LENGTH:
                    messages.append(UserMessage(
                        _('enum value "{value}" must have at least {MIN_ENUM_VALUE_LENGTH} characters'),
                        value=v,
                        MIN_ENUM_VALUE_LENGTH=MIN_ENUM_VALUE_LENGTH,
                    ))
                if len(v) > MAX_ENUM_VALUE_LENGTH:
                    messages.append(UserMessage(
                        _('enum value "{value}" must have no more than {MAX_ENUM_VALUE_LENGTH} characters'),
                        value=v,
                        MAX_ENUM_VALUE_LENGTH=MAX_ENUM_VALUE_LENGTH,
                    ))
        return possible_error(messages)

    def validate_value(self, value: Any) -> bool:
        if value not in self.values:
            return False
        return True


DATETIME_FORMAT = re.compile(r'^\d\d\d\d\d\d\d\d:\d\d\d\d\d\d\.\d\d\d:+?\d\d?$')


class DatetimeEventDataType(AbcEventDataType):
    __slots__ = ()

    def __init__(self, description: Optional[str]) -> None:
        AbcEventDataType.__init__(self, "datetime", description)

    def __repr__(self) -> str:
        return f'DatetimeEventDataType({repr(self.description)})'

    def validate_type(self) -> Optional[PetroniaReturnError]:
        return None

    @staticmethod
    def str_to_datetime(raw_value: str) -> StdRet[datetime.datetime]:
        raise NotImplementedError()

    @staticmethod
    def datetime_to_str(value: datetime.datetime) -> str:
        raise NotImplementedError()

    def validate_value(self, value: Any) -> bool:
        """Datetime values are strings."""
        if not isinstance(value, str):
            return False
        match = DATETIME_FORMAT.match(value)
        return match is not None


class ReferenceEventDataType(AbcEventDataType):
    """
    An intermediate event data type.  A fully loaded data structure
    will not contain any of these, and it is a validation error to
    contain one.
    """

    __slots__ = ('__ref',)

    def __init__(self, description: Optional[str], ref: str) -> None:
        AbcEventDataType.__init__(self, "reference", description)
        self.__ref = ref

    def __repr__(self) -> str:
        return f'ReferenceEventDataType({repr(self.description)}, ref={repr(self.reference)})'

    @property
    def reference(self) -> str:
        return self.__ref

    def validate_value(self, value: Any) -> bool:
        # This is never valid.
        return False

    def validate_type(self) -> Optional[PetroniaReturnError]:
        # This type is never valid.
        return possible_error([UserMessage(
            _('`reference` type not replaced'),
        )])


MIN_ARRAY_LENGTH = 0
MAX_ARRAY_LENGTH = 65535
DEFAULT_MIN_ARRAY_LENGTH = MIN_ARRAY_LENGTH
DEFAULT_MAX_ARRAY_LENGTH = MAX_ARRAY_LENGTH


class ArrayEventDataType(AbcEventDataType):
    __slots__ = ('__value_type', '__min_length', '__max_length',)

    def __init__(
            self,
            description: Optional[str],
            value_type: AbcEventDataType,
            min_length: Union[int, float],
            max_length: Union[int, float],
    ) -> None:
        AbcEventDataType.__init__(self, "array", description)
        self.__value_type = value_type
        self.__min_length = int(min_length)
        self.__max_length = int(max_length)

    def __repr__(self) -> str:
        return (
            f'ArrayEventDataType({repr(self.description)}, '
            f'value_type={repr(self.value_type)}, '
            f'min_length={self.min_length}, '
            f'max_length={self.max_length})'
        )

    @property
    def value_type(self) -> AbcEventDataType:
        return self.__value_type

    @property
    def min_length(self) -> int:
        return self.__min_length

    @property
    def max_length(self) -> int:
        return self.__max_length

    def validate_type(self) -> Optional[PetroniaReturnError]:
        messages: List[UserMessage] = []
        error = self.value_type.validate_type()
        if error:
            messages.extend(error.messages())
        if self.min_length > self.max_length:
            messages.append(UserMessage(
                _('min_length ({min_length}) must be equal to or less than max_length ({max_length})'),
                min_length=self.min_length,
                max_length=self.max_length,
            ))
        if self.min_length < MIN_ARRAY_LENGTH:
            messages.append(UserMessage(
                _('min_length ({min_length}) must be greater than or equal to {MIN_ARRAY_LENGTH}'),
                min_length=self.min_length,
                MIN_ARRAY_LENGTH=MIN_ARRAY_LENGTH,
            ))
        if self.max_length > MAX_ARRAY_LENGTH:
            messages.append(UserMessage(
                _('max_length ({max_length}) must be less than or equal to {MAX_ARRAY_LENGTH}'),
                max_length=self.max_length,
                MAX_ARRAY_LENGTH=MAX_ARRAY_LENGTH,
            ))
        return possible_error(messages=messages)

    def validate_value(self, value: Any) -> bool:
        if not isinstance(value, Sequence):
            return False
        if not (self.min_length <= len(value) <= self.max_length):
            return False
        for item in value:
            if not self.value_type.validate_value(item):
                return False
        return True


class StructureFieldType:
    __slots__ = ('__optional', '__data_type',)

    def __init__(self, data_type: AbcEventDataType, optional: bool) -> None:
        self.__data_type = data_type
        self.__optional = optional

    def __repr__(self) -> str:
        return f'StructureFieldType(optional={self.is_optional}, data_type={repr(self.data_type)})'

    @property
    def data_type(self) -> AbcEventDataType:
        return self.__data_type

    @property
    def is_optional(self) -> bool:
        return self.__optional


MIN_FIELD_NAME_LENGTH = 1
MAX_FIELD_NAME_LENGTH = 255
VALID_FIRST_FIELD_NAME_CHAR = 'abcdefghijklmnopqrstuvwxyz'
VALID_FIELD_NAME_CHAR = VALID_FIRST_FIELD_NAME_CHAR + '_0123456789'


class StructureEventDataType(AbcEventDataType):
    __slots__ = ('__field_types', '__required_field_names')

    def __init__(
            self,
            description: Optional[str],
            field_types: Dict[str, StructureFieldType],
    ) -> None:
        AbcEventDataType.__init__(self, "structure", description)
        self.__field_types = readonly_dict(field_types)
        required_names: List[str] = []
        for field_name, field_type in field_types.items():
            if not field_type.is_optional:
                required_names.append(field_name)
        self.__required_field_names = tuple(required_names)

    def __repr__(self) -> str:
        return f'StructureEventDataType({repr(self.description)}, fields={repr(self.__field_types)})'

    def field_names(self) -> Iterable[str]:
        return self.__field_types.keys()

    def get_field_type(self, field_name: str) -> Optional[StructureFieldType]:
        return self.__field_types.get(field_name)

    def fields(self) -> Iterable[Tuple[str, StructureFieldType]]:
        return self.__field_types.items()

    def validate_type(self) -> Optional[PetroniaReturnError]:
        messages: List[UserMessage] = []
        for field_name, field_type in self.fields():
            if not (MIN_FIELD_NAME_LENGTH <= len(field_name) <= MAX_FIELD_NAME_LENGTH):
                messages.append(UserMessage(
                    _(
                        'field name ({field_name}) must have {MIN_FIELD_NAME_LENGTH} to '
                        '{MAX_FIELD_NAME_LENGTH} characters'
                    ),
                    field_name=field_name,
                    MIN_FIELD_NAME_LENGTH=MIN_FIELD_NAME_LENGTH,
                    MAX_FIELD_NAME_LENGTH=MAX_FIELD_NAME_LENGTH,
                ))
            elif field_name[0] not in VALID_FIRST_FIELD_NAME_CHAR:
                messages.append(UserMessage(
                    _('field name ({field_name}) must match `[a-z][a-z0-9_]*`'),
                    field_name=field_name,
                ))
            else:
                for c in field_name[1:]:
                    if c not in VALID_FIELD_NAME_CHAR:
                        messages.append(UserMessage(
                            _('field name ({field_name}) must match `[a-z][a-z0-9_]*`'),
                            field_name=field_name,
                        ))
                        break
            error = field_type.data_type.validate_type()
            if error:
                messages.extend(error.messages())
        return possible_error(messages=messages)

    def validate_value(self, value: Any) -> bool:
        if not isinstance(value, dict):
            return False

        # Check if all the required fields are given.
        not_provided = set(self.__required_field_names).difference(set(value.keys()))
        if not_provided:
            return False

        for key, val in value.items():
            field_type = self.get_field_type(key)
            if not field_type:
                # To allow for future versions of events, there can be extra
                # fields in the event data.  These are ignored.
                continue
            if not field_type.data_type.validate_value(val):
                return False
        return True


MIN_TYPE_MAPPING_VALUES = 1
MAX_TYPE_MAPPING_VALUES = 255
MIN_TYPE_MAPPING_KEY_LENGTH = MIN_ENUM_VALUE_LENGTH
MAX_TYPE_MAPPING_KEY_LENGTH = MAX_ENUM_VALUE_LENGTH


class SelectorEventDataType(AbcEventDataType):
    __slots__ = ('__type_mapping',)

    def __init__(
            self,
            description: Optional[str],
            type_mapping: Dict[str, AbcEventDataType],
    ) -> None:
        AbcEventDataType.__init__(self, "selector", description)
        self.__type_mapping = readonly_dict(type_mapping)

    def __repr__(self) -> str:
        return f'SelectorEventDataType({repr(self.description)}, type_mapping={repr(self.__type_mapping)})'

    @property
    def selectors(self) -> Sequence[str]:
        return tuple(self.__type_mapping.keys())

    def get_type_for(self, selector: str) -> Optional[AbcEventDataType]:
        return self.__type_mapping.get(selector)

    def selector_items(self) -> Iterable[Tuple[str, AbcEventDataType]]:
        return self.__type_mapping.items()

    def validate_value(self, value: Any) -> bool:
        if not isinstance(value, dict):
            return False
        selector = value.get('^')
        data = value.get('$')
        data_type = self.get_type_for(selector)
        if not data_type or not data_type.validate_value(data):
            return False
        return True

    def validate_type(self) -> Optional[PetroniaReturnError]:
        messages: List[UserMessage] = []
        if not (MIN_TYPE_MAPPING_VALUES <= len(self.__type_mapping) <= MAX_TYPE_MAPPING_VALUES):
            messages.append((UserMessage(
                _('must have {MIN_TYPE_MAPPING_VALUES} to {MAX_TYPE_MAPPING_VALUES} selectors ({count})'),
                count=len(self.__type_mapping),
                MIN_TYPE_MAPPING_VALUES=MIN_TYPE_MAPPING_VALUES,
                MAX_TYPE_MAPPING_VALUES=MAX_TYPE_MAPPING_VALUES,
            )))
        for key, value in self.__type_mapping.items():
            if not (MIN_TYPE_MAPPING_KEY_LENGTH <= len(key) <= MAX_TYPE_MAPPING_KEY_LENGTH):
                messages.append((UserMessage(
                    _('selector ({selector}) must have {n} to {x} characters'),
                    selector=key,
                    n=MIN_TYPE_MAPPING_KEY_LENGTH,
                    x=MAX_TYPE_MAPPING_KEY_LENGTH,
                )))
            error = value.validate_type()
            if error:
                messages.extend(error.messages())
        return possible_error(messages)


EventAccessType = Literal["public", "implementations"]
EventPriorityType = Literal["high", "user", "normal", "io"]
EVENT_NAME_FORMAT = re.compile(r'^[a-z0-9][a-z0-9]*(?:-[a-z0-9][a-z0-9]*)*$')


class EventType:
    """
    Description of an event.

    Events are only defined in API extensions.

    The fully qualified event name is '(api extension name)/(event id)'
    """
    __slots__ = ('__structure', '__name', '__priority', '__send_access', '__receive_access',)

    def __init__(
            self,
            name: str,
            priority: EventPriorityType,
            send_access: EventAccessType,
            receive_access: EventAccessType,
            structure: StructureEventDataType,
    ) -> None:
        self.__name = name
        self.__priority = priority
        self.__send_access = send_access
        self.__receive_access = receive_access
        self.__structure = structure

    def __repr__(self) -> str:
        return (
            f'EventType({self.name}, {self.priority}, '
            f'tx={self.send_access}, rx={self.receive_access}), '
            f'structure={self.structure})'
        )

    @property
    def name(self) -> str:
        return self.__name

    @property
    def priority(self) -> EventPriorityType:
        return self.__priority

    @property
    def send_access(self) -> EventAccessType:
        return self.__send_access

    @property
    def receive_access(self) -> EventAccessType:
        return self.__receive_access

    @property
    def structure(self) -> StructureEventDataType:
        return self.__structure

    def validate_type(self) -> Optional[PetroniaReturnError]:
        messages: List[UserMessage] = []
        if EVENT_NAME_FORMAT.match(self.name) is None:
            messages.append(UserMessage(
                _('event name ({event_name}) must conform to the pattern `[a-z0-9][a-z0-9-]*`'),
                event_name=self.name,
            ))
        return possible_error(messages)
