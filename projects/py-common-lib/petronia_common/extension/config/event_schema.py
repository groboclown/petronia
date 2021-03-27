
"""
Events have a common structure.

See `docs/events.md` for details.
"""

# pylint:disable=too-many-lines

from typing import Sequence, Dict, List, Iterable, Tuple, Optional, Union, Literal, Any
from abc import ABC
import re
import datetime
import collections.abc
import time
from .defs import AbcConfigType
from ...util import (
    PetroniaReturnError, UserMessage, StdRet,
    possible_error, readonly_dict, not_none,
    STANDARD_PETRONIA_CATALOG, RET_OK_NONE, EMPTY_TUPLE,
)
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
    """Base class for event data types."""
    __slots__ = ('__type_name', '__description', 'suggested_name')

    def __init__(
            self,
            type_name: EventDataType,
            description: Optional[str],
    ) -> None:
        """Common data values."""
        self.suggested_name: Optional[str] = None
        self.__type_name = type_name
        self.__description = description

    @property
    def type_name(self) -> EventDataType:
        """Name for this specific subclass."""
        return self.__type_name

    @property
    def description(self) -> Optional[str]:
        """Description of the type."""
        return self.__description

    # pragma no cover
    def validate_value(self, value: Any) -> bool:
        """Validates that the value conforms to this type's constraints."""
        raise NotImplementedError()  # pragma no cover


class InternalType(AbcConfigType):
    """Holder for another type owned by a parent. It may have been a reference,
    but the data type stored cannot be a reference."""
    __slots__ = ('__ref_name', '__data_type')

    def __init__(self, ref_name: Optional[str] = None) -> None:
        self.__ref_name = ref_name
        self.__data_type: Optional[AbcEventDataType] = None

    def __repr__(self) -> str:
        return f'InternalType({repr(self.__ref_name)}, {type(self.__data_type)})'

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, InternalType):
            return False
        # Ref name should be set if this came from a reference, which allows for
        # infinite recursion.  Instead, we'll check only the name if it's set.
        if self.__ref_name or other.ref_name:
            return self.__ref_name == other.ref_name
        return self.__data_type == other.raw_type

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self.__data_type) + 99

    @property
    def raw_type(self) -> Optional[AbcEventDataType]:
        """Get the type, possibly None."""
        return self.__data_type

    @property
    def ref_name(self) -> Optional[str]:
        """Reference name, if this came from a reference."""
        return self.__ref_name

    def is_not_set(self) -> bool:
        """Has the data type not been set yet?"""
        return self.__data_type is None

    def set(self, data_type: AbcEventDataType) -> StdRet[None]:
        """Set the data type; can be called only once."""
        if isinstance(data_type, ReferenceEventDataType):
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('cannot store a reference type in an internal type ({name})'),
                name=self.__ref_name or 'not reference',
            )
        if self.__data_type is None:
            self.__data_type = data_type
            return RET_OK_NONE
        return StdRet.pass_errmsg(
            STANDARD_PETRONIA_CATALOG,
            _('attempted double setting of internal type ({name})'),
            name=self.__ref_name or 'not reference',
        )

    def validate_type(
            self, parents: Sequence['AbcConfigType'] = EMPTY_TUPLE,
    ) -> Optional[PetroniaReturnError]:
        """Check if this value has been set."""
        if self.__data_type is None:
            return possible_error([UserMessage(
                STANDARD_PETRONIA_CATALOG,
                _('internal type not set ({name})'),
                name=self.__ref_name or 'not reference',
            )])
        # Prevent infinite recursion...
        for parent in parents:
            if parent is self or parent is self.__data_type:
                return None
        if len(parents) > 30:
            return possible_error([UserMessage(
                STANDARD_PETRONIA_CATALOG,
                _('types nested too deep: {types}'),
                types=[*(repr(p) for p in parents), repr(self)],
            )])
        return self.__data_type.validate_type((*parents, self))

    def not_none(self) -> AbcEventDataType:
        """Return the valid set value.  Must be valid to call."""
        assert self.__data_type is not None  # nosec
        return self.__data_type


class BoolEventDataType(AbcEventDataType):
    """Boolean type, represents true or false."""
    __slots__ = ()

    def __init__(self, description: Optional[str]) -> None:
        """The boolean type constructor."""
        AbcEventDataType.__init__(self, "bool", description)

    def __repr__(self) -> str:
        return f'BoolEventDataType({repr(self.description)})'

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, BoolEventDataType):
            return False
        return self.description == other.description

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self.description) + 4

    def validate_type(
            self, parents: Sequence['AbcConfigType'] = EMPTY_TUPLE,
    ) -> Optional[PetroniaReturnError]:
        return None

    def validate_value(self, value: Any) -> bool:
        return isinstance(value, bool)


MIN_STRING_LENGTH = 0
MAX_STRING_LENGTH = 65535
DEFAULT_MIN_STRING_LENGTH = 0
DEFAULT_MAX_STRING_LENGTH = 255


class StringEventDataType(AbcEventDataType):
    """Represents a string type."""
    __slots__ = ('__min_length', '__max_length')

    def __init__(
            self,
            description: Optional[str],
            min_length: Union[int, float],
            max_length: Union[int, float],
    ) -> None:
        """String data type constructor."""
        AbcEventDataType.__init__(self, "string", description)
        self.__min_length = int(min_length)
        self.__max_length = int(max_length)

    def __repr__(self) -> str:
        return (
            f'StringEventDataType({repr(self.description)}, '
            f'min_length={self.min_length}, '
            f'max_length = {self.max_length})'
        )

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, StringEventDataType):
            return False
        return (
            self.description == other.description
            and self.min_length == other.min_length
            and self.max_length == other.max_length
        )

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self.description) + self.min_length + self.max_length + 5

    @property
    def min_length(self) -> int:
        """String values can have no less than this number of characters."""
        return self.__min_length

    @property
    def max_length(self) -> int:
        """String values can have no more than this number of characters."""
        return self.__max_length

    def validate_type(
            self, parents: Sequence['AbcConfigType'] = EMPTY_TUPLE,
    ) -> Optional[PetroniaReturnError]:
        messages: List[UserMessage] = []
        if self.min_length > self.max_length:
            messages.append(UserMessage(
                STANDARD_PETRONIA_CATALOG,
                _(
                    'min_length ({min_length}) must be equal to or '
                    'less than max_length ({max_length})',
                ),
                min_length=self.min_length,
                max_length=self.max_length,
            ))
        if self.min_length < MIN_STRING_LENGTH:
            messages.append(UserMessage(
                STANDARD_PETRONIA_CATALOG,
                _('min_length ({min_length}) must be greater than or equal to {MIN_STRING_LENGTH}'),
                min_length=self.min_length,
                MIN_STRING_LENGTH=MIN_STRING_LENGTH,
            ))
        if self.max_length > MAX_STRING_LENGTH:
            messages.append(UserMessage(
                STANDARD_PETRONIA_CATALOG,
                _('max_length ({max_length}) must be less than or equal to {MAX_STRING_LENGTH}'),
                max_length=self.max_length,
                MAX_STRING_LENGTH=MAX_STRING_LENGTH,
            ))
        return possible_error(messages)

    def validate_value(self, value: Any) -> bool:
        if not isinstance(value, str):
            return False
        if not self.min_length <= len(value) <= self.max_length:
            return False
        return True


MIN_INT_VALUE = -9223372036854775808
MAX_INT_VALUE = 9223372036854775807
DEFAULT_MIN_INT_VALUE = MIN_INT_VALUE
DEFAULT_MAX_INT_VALUE = MAX_INT_VALUE


class IntEventDataType(AbcEventDataType):
    """Represents an integer value type."""
    __slots__ = ('__min_value', '__max_value')

    def __init__(
            self,
            description: Optional[str],
            min_value: Union[float, int],
            max_value: Union[float, int],
    ) -> None:
        """Integer event data type constructor."""
        AbcEventDataType.__init__(self, "int", description)
        self.__min_value = int(min_value)
        self.__max_value = int(max_value)

    def __repr__(self) -> str:
        return (
            f'IntEventDataType({repr(self.description)}, '
            f'min_value={self.min_value}, '
            f'max_value={self.max_value})'
        )

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, IntEventDataType):
            return False
        return (
            self.description == other.description
            and self.min_value == other.min_value
            and self.max_value == other.max_value
        )

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self.description) + self.min_value + self.max_value + 3

    @property
    def min_value(self) -> int:
        """Integer values cannot be less than this value."""
        return self.__min_value

    @property
    def max_value(self) -> int:
        """Integer values cannot be more than this value."""
        return self.__max_value

    def validate_type(
            self, parents: Sequence['AbcConfigType'] = EMPTY_TUPLE,
    ) -> Optional[PetroniaReturnError]:
        messages: List[UserMessage] = []
        if self.min_value > self.max_value:
            messages.append(UserMessage(
                STANDARD_PETRONIA_CATALOG,
                _('min_value ({min_value}) must be equal to or less than max_value ({max_value})'),
                min_value=self.min_value,
                max_value=self.max_value,
            ))
        if self.min_value < MIN_INT_VALUE:
            messages.append(UserMessage(
                STANDARD_PETRONIA_CATALOG,
                _('min_value ({min_value}) must be greater than or equal to {MIN_INT_VALUE}'),
                min_value=self.min_value,
                MIN_INT_VALUE=MIN_INT_VALUE,
            ))
        if self.max_value > MAX_INT_VALUE:
            messages.append(UserMessage(
                STANDARD_PETRONIA_CATALOG,
                _('max_value ({max_value}) must be less than or equal to {MAX_INT_VALUE}'),
                max_value=self.max_value,
                MAX_INT_VALUE=MAX_INT_VALUE,
            ))
        return possible_error(messages)

    def validate_value(self, value: Any) -> bool:
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            return False
        if not self.min_value <= value <= self.max_value:
            return False
        return True


class FloatEventDataType(AbcEventDataType):
    """Floating point number event data type."""
    __slots__ = ('__min_value', '__max_value')

    def __init__(
            self,
            description: Optional[str],
            min_value: Optional[float],
            max_value: Optional[float],
    ) -> None:
        """Floating point number event data type constructor."""
        AbcEventDataType.__init__(self, "float", description)
        self.__min_value = min_value
        self.__max_value = max_value

    def __repr__(self) -> str:
        return (
            f'FloatEventDataType({repr(self.description)}, '
            f'min_value={self.min_value}, '
            f'max_value={self.max_value})'
        )

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, FloatEventDataType):
            return False
        return (
            self.description == other.description
            and self.min_value == other.min_value
            and self.max_value == other.max_value
        )

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self.description) + hash(self.min_value) + hash(self.max_value) + 2

    @property
    def min_value(self) -> Optional[float]:
        """If given, floating point numbers cannot be less than this value."""
        return self.__min_value

    @property
    def max_value(self) -> Optional[float]:
        """If given, floating point numbers cannot be more than this value."""
        return self.__max_value

    def validate_type(
            self, parents: Sequence['AbcConfigType'] = EMPTY_TUPLE,
    ) -> Optional[PetroniaReturnError]:
        messages: List[UserMessage] = []
        if (
                self.min_value is not None and
                self.max_value is not None and
                self.min_value > self.max_value
        ):
            messages.append(UserMessage(
                STANDARD_PETRONIA_CATALOG,
                _('min_value ({min_value}) must be equal to or less than max_value ({max_value})'),
                min_value=self.min_value,
                max_value=self.max_value,
            ))
        return possible_error(messages)

    def validate_value(self, value: Any) -> bool:
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            return False
        if self.min_value is not None and value < self.min_value:
            return False
        if self.max_value is not None and value > self.max_value:
            return False
        return True


MIN_ENUM_VALUE_LENGTH = 1
MAX_ENUM_VALUE_LENGTH = 255


class EnumEventDataType(AbcEventDataType):
    """Enumerated value event data type."""
    __slots__ = ('__values',)

    def __init__(
            self,
            description: Optional[str],
            values: Iterable[str],
    ) -> None:
        """Constructor."""
        AbcEventDataType.__init__(self, "enum", description)
        self.__values = set(values)

    def __repr__(self) -> str:
        return f'EnumEventDataType({repr(self.description)}, values={repr(self.__values)})'

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, EnumEventDataType):
            return False
        return (
            self.description == other.description
            and self.values == other.values
        )

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self.description) + hash(self.values) + 1

    @property
    def values(self) -> Sequence[str]:
        """The list of valid values"""
        return tuple(self.__values)

    def validate_type(
            self, parents: Sequence['AbcConfigType'] = EMPTY_TUPLE,
    ) -> Optional[PetroniaReturnError]:
        messages: List[UserMessage] = []
        if len(self.__values) <= 0:
            messages.append(UserMessage(
                STANDARD_PETRONIA_CATALOG,
                _('enum must contain at least 1 item ({description})'),
                description=self.description or 'no description',
            ))
        for val in self.__values:
            if not isinstance(val, str):
                messages.append(UserMessage(
                    STANDARD_PETRONIA_CATALOG,
                    _('enum value {value} must be a string'),
                    value=val,
                ))
            else:
                if len(val) < MIN_ENUM_VALUE_LENGTH:
                    messages.append(UserMessage(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'enum value "{value}" must have at least '
                            '{MIN_ENUM_VALUE_LENGTH} characters',
                        ),
                        value=val,
                        MIN_ENUM_VALUE_LENGTH=MIN_ENUM_VALUE_LENGTH,
                    ))
                if len(val) > MAX_ENUM_VALUE_LENGTH:
                    messages.append(UserMessage(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'enum value "{value}" must have no more '
                            'than {MAX_ENUM_VALUE_LENGTH} characters',
                        ),
                        value=val,
                        MAX_ENUM_VALUE_LENGTH=MAX_ENUM_VALUE_LENGTH,
                    ))
        return possible_error(messages)

    def validate_value(self, value: Any) -> bool:
        if value not in self.values:
            return False
        return True


DATETIME_FORMAT = re.compile(
    r'^\d\d\d\d\d\d\d\d:\d\d\d\d\d\d(?:\.\d{1,6})?:[+-]?\d\d\d\d(?:\d\d(?:\.\d{1,6})?)?$'
)


class DatetimeEventDataType(AbcEventDataType):
    """The datetime event data type."""
    __slots__ = ()

    def __init__(self, description: Optional[str]) -> None:
        """Constructor"""
        AbcEventDataType.__init__(self, "datetime", description)

    def __repr__(self) -> str:
        return f'DatetimeEventDataType({repr(self.description)})'

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, DatetimeEventDataType):
            return False
        return self.description == other.description

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self.description) + 12

    def validate_type(
            self, parents: Sequence['AbcConfigType'] = EMPTY_TUPLE,
    ) -> Optional[PetroniaReturnError]:
        return None

    @staticmethod
    def str_to_datetime(raw_value: str) -> StdRet[datetime.datetime]:
        """Convert a compatible string to a datetime instance."""
        try:
            return StdRet.pass_ok(datetime.datetime.strptime(raw_value, '%Y%m%d:%H%M%S.%f:%z'))
        except ValueError as err:
            return StdRet.pass_exception(
                STANDARD_PETRONIA_CATALOG,
                _('invalid formatted date string ({date})'),
                err,
                date=raw_value,
            )

    @staticmethod
    def datetime_to_str(value: datetime.datetime) -> str:
        """Convert a datetime instance to a compatible string."""
        if value.tzinfo is None:
            value = datetime.datetime(
                year=value.year, month=value.month, day=value.day,
                hour=value.hour, minute=value.minute,
                second=value.second, microsecond=value.microsecond,
                tzinfo=LOCAL_TIMEZONE,
            )
        return datetime.datetime.strftime(value, '%Y%m%d:%H%M%S.%f:%z')

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

    __slots__ = ('__ref', '__references')

    def __init__(self, description: Optional[str], ref: str) -> None:
        """Constructor."""
        AbcEventDataType.__init__(self, "reference", description)
        self.__ref = ref

    def __repr__(self) -> str:
        return f'ReferenceEventDataType({repr(self.description)}, ref={repr(self.reference)})'

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ReferenceEventDataType):
            return False
        return self.__ref == other.reference

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)

    @property
    def reference(self) -> str:
        """The type this references."""
        return self.__ref

    def validate_value(self, value: Any) -> bool:
        # This is never valid.
        return False

    def validate_type(
            self, parents: Sequence['AbcConfigType'] = EMPTY_TUPLE,
    ) -> Optional[PetroniaReturnError]:
        # This type is never valid.
        return possible_error([UserMessage(
            STANDARD_PETRONIA_CATALOG,
            _('`reference` type not replaced'),
        )])


MIN_ARRAY_LENGTH = 0
MAX_ARRAY_LENGTH = 65535
DEFAULT_MIN_ARRAY_LENGTH = MIN_ARRAY_LENGTH
DEFAULT_MAX_ARRAY_LENGTH = MAX_ARRAY_LENGTH


class ArrayEventDataType(AbcEventDataType):
    """An array of a single data type."""
    __slots__ = ('__value_type', '__min_length', '__max_length',)

    def __init__(
            self,
            description: Optional[str],
            value_type: InternalType,
            min_length: Union[int, float],
            max_length: Union[int, float],
    ) -> None:
        """Constructor"""
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

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ArrayEventDataType):
            return False
        return (
            self.description == other.description
            and self.value_type == other.value_type
            and self.min_length == other.min_length
            and self.max_length == other.max_length
        )

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return (
            hash(self.description) +
            hash(self.value_type) + self.min_length + self.max_length
        )

    @property
    def value_type(self) -> InternalType:
        """The per-item type."""
        return self.__value_type

    @property
    def min_length(self) -> int:
        """Arrays of this type cannot contain less than this number of items."""
        return self.__min_length

    @property
    def max_length(self) -> int:
        """Arrays of this length cannot have more than this number of items."""
        return self.__max_length

    def validate_type(
            self, parents: Sequence['AbcConfigType'] = EMPTY_TUPLE,
    ) -> Optional[PetroniaReturnError]:
        messages: List[UserMessage] = []
        error = self.value_type.validate_type(parents)
        if error:
            messages.extend(error.messages())
        if self.min_length > self.max_length:
            messages.append(UserMessage(
                STANDARD_PETRONIA_CATALOG,
                _(
                    'min_length ({min_length}) must be equal to '
                    'or less than max_length ({max_length})',
                ),
                min_length=self.min_length,
                max_length=self.max_length,
            ))
        if self.min_length < MIN_ARRAY_LENGTH:
            messages.append(UserMessage(
                STANDARD_PETRONIA_CATALOG,
                _('min_length ({min_length}) must be greater than or equal to {MIN_ARRAY_LENGTH}'),
                min_length=self.min_length,
                MIN_ARRAY_LENGTH=MIN_ARRAY_LENGTH,
            ))
        if self.max_length > MAX_ARRAY_LENGTH:
            messages.append(UserMessage(
                STANDARD_PETRONIA_CATALOG,
                _('max_length ({max_length}) must be less than or equal to {MAX_ARRAY_LENGTH}'),
                max_length=self.max_length,
                MAX_ARRAY_LENGTH=MAX_ARRAY_LENGTH,
            ))
        return possible_error(messages=messages)

    def validate_value(self, value: Any) -> bool:
        if not isinstance(value, collections.abc.Sequence):
            return False
        if not self.min_length <= len(value) <= self.max_length:
            return False
        if self.value_type.is_not_set():
            return False
        for item in value:
            if not self.value_type.not_none().validate_value(item):
                return False
        return True


class StructureFieldType:
    """A structured field definition."""
    __slots__ = ('__optional', '__data_type',)

    def __init__(self, data_type: InternalType, optional: bool) -> None:
        """The field type, which can optionally exist."""
        self.__data_type = data_type
        self.__optional = optional

    def __repr__(self) -> str:
        """Representation of this value."""
        return (
            f'StructureFieldType(optional={self.is_optional}, '
            f'data_type={repr(self.data_type)})'
        )

    def __hash__(self) -> int:
        return 100 + hash(self.__data_type) + hash(self.__optional)

    def __eq__(self, other: Any) -> bool:
        if self is other:
            return True
        if not isinstance(other, StructureFieldType):
            return False
        return self.data_type == other.data_type and self.is_optional == other.is_optional

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)

    def validate(
            self, field_name: str, parents: Sequence['AbcConfigType'] = EMPTY_TUPLE,
    ) -> Optional[PetroniaReturnError]:
        """Is this field valid?"""
        res = self.__data_type.validate_type(parents)
        if res is not None:
            res = possible_error(messages=[UserMessage(
                STANDARD_PETRONIA_CATALOG,
                _('error in field {field_name}'),
                field_name=field_name,
            )], errors=[res])
        return res

    @property
    def data_type(self) -> InternalType:
        """The contained data type."""
        return self.__data_type

    @property
    def is_optional(self) -> bool:
        """True if this value is not required to exist, and False if it is required."""
        return self.__optional


MIN_FIELD_NAME_LENGTH = 1
MAX_FIELD_NAME_LENGTH = 255
VALID_FIRST_FIELD_NAME_CHAR = 'abcdefghijklmnopqrstuvwxyz'
VALID_FIELD_NAME_CHAR = VALID_FIRST_FIELD_NAME_CHAR + '_0123456789'


class StructureEventDataType(AbcEventDataType):
    """The structured event data type.
    Field names must conform to standard name typing, which is
    all lower-case ascii characters, underscore, and numbers, with
    only lower-case characters allowed as the first character."""
    __slots__ = ('__field_types', '__required_field_names', '__field_names')

    def __init__(
            self,
            description: Optional[str],
            field_types: Dict[str, StructureFieldType],
    ) -> None:
        """Constructor."""
        AbcEventDataType.__init__(self, "structure", description)
        self.__field_types = readonly_dict(field_types)
        required_names: List[str] = []
        for field_name, field_type in field_types.items():
            if not field_type.is_optional:
                required_names.append(field_name)
        self.__field_names = tuple(sorted(list(self.__field_types.keys())))
        self.__required_field_names = tuple(sorted(list(required_names)))

    def __repr__(self) -> str:
        return (
            f'StructureEventDataType({repr(self.description)}, '
            f'fields={repr(self.__field_types)})'
        )

    def __eq__(self, other: Any) -> bool:
        if self is other:
            return True
        if not isinstance(other, StructureEventDataType):
            return False
        return (
            # Don't need to match type name...
            self.description == other.description
            and self.__field_types == dict(other.fields())
            and self.__required_field_names == other.required_field_names
        )

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        type_hash = hash(self.__field_names) + hash(self.__required_field_names)
        for field_name in self.__field_names:
            type_hash += hash(self.__field_types[field_name])
        return type_hash

    def field_names(self) -> Iterable[str]:
        """All the field names used by this structure."""
        return self.__field_names

    def get_field_type(self, field_name: str) -> Optional[StructureFieldType]:
        """The field type for the given field, if it exists, or None."""
        return self.__field_types.get(field_name)

    def fields(self) -> Iterable[Tuple[str, StructureFieldType]]:
        """A list of field name, field type."""
        return self.__field_types.items()

    @property
    def required_field_names(self) -> Sequence[str]:
        """All fields that must be present."""
        return self.__required_field_names

    def validate_type(
            self, parents: Sequence['AbcConfigType'] = EMPTY_TUPLE,
    ) -> Optional[PetroniaReturnError]:
        messages: List[UserMessage] = []
        for field_name, field_type in self.fields():
            if not MIN_FIELD_NAME_LENGTH <= len(field_name) <= MAX_FIELD_NAME_LENGTH:
                messages.append(UserMessage(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'field name ({field_name}) must have {MIN_FIELD_NAME_LENGTH} to '
                        '{MAX_FIELD_NAME_LENGTH} characters',
                    ),
                    field_name=field_name,
                    MIN_FIELD_NAME_LENGTH=MIN_FIELD_NAME_LENGTH,
                    MAX_FIELD_NAME_LENGTH=MAX_FIELD_NAME_LENGTH,
                ))
            elif field_name[0] not in VALID_FIRST_FIELD_NAME_CHAR:
                messages.append(UserMessage(
                    STANDARD_PETRONIA_CATALOG,
                    _('field name ({field_name}) must match `[a-z][a-z0-9_]*`'),
                    field_name=field_name,
                ))
            else:
                for name_char in field_name[1:]:
                    if name_char not in VALID_FIELD_NAME_CHAR:
                        messages.append(UserMessage(
                            STANDARD_PETRONIA_CATALOG,
                            _('field name ({field_name}) must match `[a-z][a-z0-9_]*`'),
                            field_name=field_name,
                        ))
                        break

            error = field_type.validate(field_name, (*parents, self))
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
            if (
                    field_type.data_type.is_not_set()
                    or not field_type.data_type.not_none().validate_value(val)
            ):
                return False
        return True


MIN_TYPE_MAPPING_VALUES = 1
MAX_TYPE_MAPPING_VALUES = 255
MIN_TYPE_MAPPING_KEY_LENGTH = MIN_ENUM_VALUE_LENGTH
MAX_TYPE_MAPPING_KEY_LENGTH = MAX_ENUM_VALUE_LENGTH


class SelectorEventDataType(AbcEventDataType):
    """A selector event data type.  This allows for creating a fixed set of
    types a value can store, using a classifying name to differentiate the
    expected types."""
    __slots__ = ('__type_mapping',)

    def __init__(
            self,
            description: Optional[str],
            type_mapping: Dict[str, InternalType],
    ) -> None:
        """Constructor."""
        AbcEventDataType.__init__(self, "selector", description)
        self.__type_mapping = readonly_dict(type_mapping)

    def __repr__(self) -> str:
        return (
            f'SelectorEventDataType({repr(self.description)}, '
            f'type_mapping={repr(self.__type_mapping)})'
        )

    def __hash__(self) -> int:
        return hash(self.description) + hash(tuple(self.__type_mapping))

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SelectorEventDataType):
            return False
        return (
            self.__type_mapping == dict(other.selector_items())
        )

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)

    @property
    def selectors(self) -> Sequence[str]:
        """List of selector names."""
        return tuple(self.__type_mapping.keys())

    def get_type_for(self, selector: str) -> Optional[InternalType]:
        """Returns the type for the selector, if it exists, or None."""
        return self.__type_mapping.get(selector)

    def selector_items(self) -> Iterable[Tuple[str, InternalType]]:
        """Returns a list of selector name, selector type."""
        return self.__type_mapping.items()

    def validate_value(self, value: Any) -> bool:
        if not isinstance(value, dict):
            return False
        selector = value.get('^')
        if not isinstance(selector, str):
            return False
        data = value.get('$')
        data_type = self.get_type_for(selector)
        if not data_type or data_type.is_not_set() or not data_type.not_none().validate_value(data):
            return False
        return True

    def validate_type(
            self, parents: Sequence['AbcConfigType'] = EMPTY_TUPLE,
    ) -> Optional[PetroniaReturnError]:
        messages: List[UserMessage] = []
        if not MIN_TYPE_MAPPING_VALUES <= len(self.__type_mapping) <= MAX_TYPE_MAPPING_VALUES:
            messages.append(UserMessage(
                STANDARD_PETRONIA_CATALOG,
                _(
                    'must have {MIN_TYPE_MAPPING_VALUES} to '
                    '{MAX_TYPE_MAPPING_VALUES} selectors ({count})',
                ),
                count=len(self.__type_mapping),
                MIN_TYPE_MAPPING_VALUES=MIN_TYPE_MAPPING_VALUES,
                MAX_TYPE_MAPPING_VALUES=MAX_TYPE_MAPPING_VALUES,
            ))
        for key, value in self.__type_mapping.items():
            if not MIN_TYPE_MAPPING_KEY_LENGTH <= len(key) <= MAX_TYPE_MAPPING_KEY_LENGTH:
                messages.append(UserMessage(
                    STANDARD_PETRONIA_CATALOG,
                    _('selector ({selector}) must have {n} to {x} characters'),
                    selector=key,
                    n=MIN_TYPE_MAPPING_KEY_LENGTH,
                    x=MAX_TYPE_MAPPING_KEY_LENGTH,
                ))
            error = value.validate_type((*parents, self))
            if error:
                messages.extend(error.messages())
        return possible_error(messages)


EventAccessType = Literal["public", "implementations", "internal", "target"]
PUBLIC_ACCESS: EventAccessType = 'public'
IMPLEMENTATIONS_ACCESS: EventAccessType = 'implementations'
INTERNAL_ACCESS: EventAccessType = 'internal'
TARGET_ACCESS: EventAccessType = 'target'

EventPriorityType = Literal["high", "user", "normal", "io"]
EVENT_NAME_FORMAT = re.compile(r'^[a-z0-9][a-z0-9]*(?:[-:][a-z0-9][a-z0-9]*)*$')


class EventType:
    """
    Description of an event.

    Events are only defined in API extensions.

    The fully qualified event name is '(api extension name):(event id)'
    """
    __slots__ = (
        '__structure', '__name', '__priority', '__send_access', '__receive_access',
        '__unique_target',
    )

    def __init__(  # pylint: disable=R0913
            self,
            name: str,
            priority: EventPriorityType,
            send_access: EventAccessType,
            receive_access: EventAccessType,
            structure: Optional[StructureEventDataType],
            unique_target: Optional[str],
    ) -> None:
        """Constructor"""
        self.__name = name
        self.__priority = priority
        self.__send_access = send_access
        self.__receive_access = receive_access
        self.__structure = structure
        self.__unique_target = unique_target

    def __repr__(self) -> str:
        return (
            f'EventType({self.name}, {self.priority}, '
            f'tx={self.send_access}, rx={self.receive_access}), '
            f'structure={self.structure})'
        )

    @property
    def name(self) -> str:
        """Event name."""
        return self.__name

    @property
    def priority(self) -> EventPriorityType:
        """Event priority."""
        return self.__priority

    @property
    def send_access(self) -> EventAccessType:
        """Access allowed for sending the event."""
        return self.__send_access

    @property
    def receive_access(self) -> EventAccessType:
        """Access allowed for receiving the event."""
        return self.__receive_access

    def is_binary(self) -> bool:
        """Is this a binary data event?  Such events have no formally defined
        structured data."""
        return self.__structure is None

    def is_object(self) -> bool:
        """Is this an object data event?  Such events have a formally defined
        structured data."""
        return self.__structure is not None

    @property
    def structure(self) -> Optional[StructureEventDataType]:
        """The event data structure, or None if this is a binary event."""
        return self.__structure

    @property
    def object_structure(self) -> StructureEventDataType:
        """The event data structure.  Only call when the
        caller guarantees that this is an object data type."""
        return not_none(self.__structure)

    @property
    def unique_target(self) -> Optional[str]:
        """If given, the only target ID allowed for the event. Must be a relative target ID."""
        return self.__unique_target

    def validate_type(
            self, parents: Sequence['AbcConfigType'] = EMPTY_TUPLE,
    ) -> Optional[PetroniaReturnError]:
        """Validates whether this event definition is valid."""
        messages: List[UserMessage] = []
        if EVENT_NAME_FORMAT.match(self.name) is None:
            messages.append(UserMessage(
                STANDARD_PETRONIA_CATALOG,
                _('event name ({event_name}) must conform to the pattern `[a-z0-9][a-z0-9:-]*`'),
                event_name=self.name,
            ))
        if self.structure:
            struct_validate = self.structure.validate_type(parents)
            if struct_validate:
                messages.extend(struct_validate.messages())
        return possible_error(messages)


LOCAL_TIMEZONE = datetime.timezone(datetime.timedelta(seconds=time.timezone))
