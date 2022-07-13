"""Data packet definition to send/receive from the server."""

from typing import (
    Literal, BinaryIO,
    Sequence, Tuple, List,
    Mapping, Dict,
    Callable, Type, Union, Optional, Any,
)
import ctypes
import struct


# Native endian-ness, standard data sizes.
ENDIAN_MARKER = '='

MarkerType = Literal[
    'x', 'b', 'B', 'h', 'H', 'i', 'I', 'q', 'Q', 'f', 'd', '*',
]
MARKER_PAD: MarkerType = 'x'
MARKER_INT8: MarkerType = 'b'
MARKER_UINT8: MarkerType = 'B'
MARKER_INT16: MarkerType = 'h'
MARKER_UINT16: MarkerType = 'H'
MARKER_INT32: MarkerType = 'i'
MARKER_UINT32: MarkerType = 'I'
MARKER_INT64: MarkerType = 'q'
MARKER_UINT64: MarkerType = 'Q'
MARKER_FLOAT32: MarkerType = 'f'
MARKER_FLOAT64: MarkerType = 'd'
MARKER_FLEXIBLE: MarkerType = '*'

VALUE_TYPE_LOOKUP: Mapping[str, Optional[Tuple[Type[Any], Type[Any]]]] = {
    MARKER_PAD: None,
    MARKER_INT8: (int, ctypes.c_int8),
    MARKER_UINT8: (int, ctypes.c_uint8),
    MARKER_INT16: (int, ctypes.c_int16),
    MARKER_UINT16: (int, ctypes.c_uint16),
    MARKER_INT32: (int, ctypes.c_int32),
    MARKER_UINT32: (int, ctypes.c_uint32),
    MARKER_INT64: (int, ctypes.c_int64),
    MARKER_UINT64: (int, ctypes.c_uint64),
    MARKER_FLOAT32: (float, ctypes.c_float),
    MARKER_FLOAT64: (float, ctypes.c_double),

    MARKER_FLEXIBLE: (bytes, bytearray),
}
INT_MARKERS = (
    MARKER_INT8, MARKER_UINT8,
    MARKER_INT16, MARKER_UINT16,
    MARKER_INT32, MARKER_UINT32,
    MARKER_INT64, MARKER_UINT64,
)
FLOAT_MARKERS = (MARKER_FLOAT32, MARKER_FLOAT64)


PackMemberBasic = Union[int, float]
PackMemberType = Union[
    bytes, PackMemberBasic,
    Mapping[str, Union[PackMemberBasic, List[PackMemberBasic]]],
    Sequence[Union[PackMemberBasic, Mapping[str, Union[bytes, PackMemberBasic]]]],
]
LengthCallback: Callable[[Mapping[str, PackMemberType], int], int]
CountCallback: Callable[[Mapping[str, PackMemberType]], int]
IntLookupCallback: Callable[[Mapping[str, PackMemberType]], int]


class DataPacketField:
    """Abstract class for a field in a data packet, either static or variable length."""

    @property
    def is_padding(self) -> bool:
        """Is this a padding field?  Padding fields are not included in the structure."""
        return False

    def size(self, parent_struct: Mapping[str, PackMemberType], read_bytes: int) -> int:
        """Discovers the size, in bytes, of this structure based on previously read values."""
        raise NotImplementedError

    def pack(
            self, value: PackMemberType,
            parent_struct: Mapping[str, PackMemberType], written_bytes: int,
    ) -> bytes:
        """Packs up the value from the parent structure."""
        raise NotImplementedError

    def unpack(
            self, parent_struct: Mapping[str, PackMemberType], read_bytes: int, data: bytes,
    ) -> PackMemberType:
        """Unpacks the data into this structure"""
        raise NotImplementedError


class DataPacket:
    """A data packet with a final value that has a variable length set of bytes at the
    end of the packet.  Pad values are ignored from packing and unpacking.

    Could eventually create a very optimized version for fixed size packets.
    """
    __slots__ = ('__fields',)

    def __init__(
            self,
            name_map: Sequence[Tuple[str, DataPacketField]],
    ) -> None:
        self.__fields = name_map

    def unpack(self, reader: BinaryIO) -> Dict[str, PackMemberType]:
        """Unpack this packet out of the data stream."""
        base_data: Dict[str, PackMemberType] = {}
        read_count = 0
        for var_name, field in self.__fields:
            to_read = field.size(base_data, read_count)
            read_data = reader.read(to_read)
            if not field.is_padding:
                base_data[var_name] = field.unpack(base_data, read_count, read_data)
            # else it's a padding value and is ignored
            read_count += to_read
        return base_data

    def pack(
            self,
            **kwargs: PackMemberType,
    ) -> bytes:
        res = b''
        remaining = set(kwargs.keys())
        for var_name, field in self.__fields:
            write_count = len(res)
            if field.is_padding:
                res += field.pack(0, kwargs, write_count)
            else:
                remaining.remove(var_name)
                variable_value = kwargs[var_name]
                res += field.pack(variable_value, kwargs, write_count)
        if remaining:
            # Programmer Error
            raise ValueError(f'extra values packed in structure: {remaining}')
        return res


class FixedDataPacketField(DataPacketField):
    """Fixed size data field."""
    __slots__ = ('__format', '__size', '__count')

    def __init__(self, format_str: MarkerType, count: int = 1) -> None:
        if format_str == MARKER_FLEXIBLE:
            raise ValueError('cannot use a flexible marker in a fixed size packet field')
        self.__format = ENDIAN_MARKER + format_str * count
        self.__count = count
        self.__size = struct.calcsize(self.__format)

    def size(self, parent_struct: Mapping[str, PackMemberType], read_bytes: int) -> int:
        return self.__size

    def pack(
            self, value: PackMemberType,
            parent_struct: Mapping[str, PackMemberType], written_bytes: int,
    ) -> bytes:
        if isinstance(value, Sequence):
            return struct.pack(self.__format, *value)
        return struct.pack(self.__format, value)

    def unpack(
            self, parent_struct: Mapping[str, PackMemberType], read_bytes: int, data: bytes,
    ) -> PackMemberType:
        return struct.unpack(self.__format, data)


class SimpleListDataPacketField(DataPacketField):
    """A simple list of a single value type."""
    __slots__ = ('__count_callback', '__format', '__alignment')

    def __init__(
            self,
            format_str: MarkerType,
            count_callback: CountCallback,
            alignment: int = 0,
    ) -> None:
        self.__format = format_str
        self.__count_callback = count_callback
        self.__alignment = alignment

    def size(self, parent_struct: Mapping[str, PackMemberType], read_bytes: int) -> int:
        count = self.__count_callback(parent_struct)
        basic_format = ENDIAN_MARKER + (self.__format * count)
        byte_count = struct.calcsize(basic_format)
        if self.__alignment > 1:
            # Note: padding here is only internal, not based on read_bytes.
            padding_count = byte_count % self.__alignment
            byte_count += padding_count
        return byte_count

    def pack(
            self, value: PackMemberType,
            parent_struct: Mapping[str, PackMemberType], written_bytes: int,
    ) -> bytes:
        if not isinstance(value, (list, tuple)):
            raise ValueError('value must be a sequence')
        val = tuple(value)
        basic_format = ENDIAN_MARKER + (self.__format * len(val))
        if self.__alignment > 1:
            # Note: padding here is only internal, not based on read_bytes.
            byte_count = struct.calcsize(basic_format)
            padding_count = byte_count % self.__alignment
            basic_format += MARKER_PAD * padding_count
        return struct.pack(basic_format, *val)

    def unpack(
            self, parent_struct: Mapping[str, PackMemberType], read_bytes: int, data: bytes,
    ) -> PackMemberType:
        count = self.__count_callback(parent_struct)
        basic_format = ENDIAN_MARKER + (self.__format * count)
        if self.__alignment > 1:
            # Note: padding here is only internal, not based on read_bytes.
            byte_count = struct.calcsize(basic_format)
            padding_count = byte_count % self.__alignment
            basic_format += MARKER_PAD * padding_count
        return struct.unpack(basic_format, data)


class FixedPadDataPacketField(DataPacketField):
    """Padding field with a fixed size."""
    __slots__ = ('__count',)

    def __init__(self, count: int = 1) -> None:
        self.__count = count

    @property
    def is_padding(self) -> bool:
        return True

    def size(self, parent_struct: Mapping[str, PackMemberType], read_bytes: int) -> int:
        return self.__count

    def pack(
            self, value: PackMemberType,
            parent_struct: Mapping[str, PackMemberType], written_bytes: int,
    ) -> bytes:
        return b'\0' * self.__count

    def unpack(
            self, parent_struct: Mapping[str, PackMemberType], read_bytes: int, data: bytes,
    ) -> PackMemberType:
        return 0


class AlignedPadDataPacketField(DataPacketField):
    """Padding field with possible alignment."""
    __slots__ = ('__alignment',)

    def __init__(self, alignment: int) -> None:
        self.__alignment = alignment

    @property
    def is_padding(self) -> bool:
        return True

    def size(self, parent_struct: Mapping[str, PackMemberType], read_bytes: int) -> int:
        # The data must be sized modulo alignment == 0
        # if alignment is 4, and read bytes == 3, then must generate 1 value.
        return self.__alignment - (read_bytes % self.__alignment)

    def pack(
            self, value: PackMemberType,
            parent_struct: Mapping[str, PackMemberType], written_bytes: int,
    ) -> bytes:
        count = self.size(parent_struct, written_bytes)
        return b'\0' * count

    def unpack(
            self, parent_struct: Mapping[str, PackMemberType], read_bytes: int, data: bytes,
    ) -> Optional[PackMemberType]:
        return None


class StructureDataPacketField(DataPacketField):
    """A simple key/value inner structure field.  Any padding in the structure
    is internally aligned."""
    __slots__ = ('__fields',)

    def __init__(self, fields: Sequence[Tuple[str, DataPacketField]]) -> None:
        self.__fields = fields

    def size(self, parent_struct: Mapping[str, PackMemberType], read_bytes: int) -> int:
        count = 0
        for _name, field in self.__fields:
            count += field.size(parent_struct, count)
        return count

    def pack(
            self, value: PackMemberType,
            parent_struct: Mapping[str, PackMemberType], written_bytes: int,
    ) -> bytes:
        if not isinstance(value, Mapping):
            raise ValueError('structure fields must be Python dictionaries')
        ret = b''
        for name, field in self.__fields:
            if field.is_padding:
                field_value = 0
            else:
                field_value = value[name]
            ret += field.pack(field_value, parent_struct, len(ret))
        return ret

    def unpack(
            self, parent_struct: Mapping[str, PackMemberType], read_bytes: int, data: bytes,
    ) -> PackMemberType:
        ret: Dict[str, PackMemberType] = {}
        pos = 0
        for name, field in self.__fields:
            size = field.size(parent_struct, pos)
            if not field.is_padding:
                ret[name] = field.unpack(parent_struct, pos, data[pos:pos+size])
            # else it's padding, and we can just skip over the data
            pos += size
        return ret


class ListDataPacketField(DataPacketField):
    """A list of structured data.  Alignment is relative to the per-list item structure,
    but padding must be added to the inner structure, not explicitly on this structure."""
    __slots__ = ('__count_callback', '__inner')

    def __init__(
            self,
            inner: DataPacketField,
            count_callback: LengthCallback,
    ) -> None:
        self.__inner = inner
        self.__count_callback = count_callback

    def size(self, parent_struct: Mapping[str, PackMemberType], read_bytes: int) -> int:
        count = self.__count_callback(parent_struct, read_bytes)
        size = count * self.__inner.size(parent_struct, 0)
        return count * size

    def pack(
            self, value: PackMemberType,
            parent_struct: Mapping[str, PackMemberType], written_bytes: int,
    ) -> bytes:
        if not isinstance(value, Sequence):
            raise ValueError('value must be a sequence of dictionaries')
        ret = b''
        for val in value:
            ret += self.__inner.pack(val, parent_struct, 0)
        return ret

    def unpack(
            self, parent_struct: Mapping[str, PackMemberType], read_bytes: int, data: bytes,
    ) -> PackMemberType:
        count = self.__count_callback(parent_struct, read_bytes)
        ret: List[PackMemberType] = []
        size = self.__inner.size(parent_struct, 0)
        pos = 0
        for idx in range(count):
            ret.append(self.__inner.unpack(parent_struct, 0, data[pos:pos+size]))
            pos += size
        return ret


class BitDataPacketField(DataPacketField):
    """A structure whose shape depends upon bits in a previous value.
    Alignment is based on this structure, not previously written parts.
    The field is represented in Python as a dictionary."""
    __slots__ = ('__chooser', '__bit_choices', '__alignment')

    def __init__(
            self, chooser: CountCallback,
            bit_choices: Dict[int, Tuple[str, DataPacketField]],
            alignment: int,
    ) -> None:
        self.__chooser = chooser
        self.__bit_choices = bit_choices
        self.__alignment = alignment

    def items(
            self, parent_struct: Mapping[str, PackMemberType],
    ) -> List[Tuple[str, DataPacketField]]:
        ret: List[Tuple[str, DataPacketField]] = []
        bit_value = self.__chooser(parent_struct)
        # Slow, but works.
        bit = 1
        while bit < 0xfffffff:
            bit = bit << 1
            if bit & bit_value == bit:
                choice = self.__bit_choices[bit]
                ret.append(choice)
        return ret

    def size(self, parent_struct: Mapping[str, PackMemberType], read_bytes: int) -> int:
        choices = self.items(parent_struct)
        count = 0
        for _name, choice in choices:
            count += choice.size(parent_struct, count)
        if self.__alignment > 1:
            # Do not take the read_bytes into account
            count += self.__alignment - (count % self.__alignment)
        return count

    def pack(
            self, value: PackMemberType,
            parent_struct: Mapping[str, PackMemberType], written_bytes: int,
    ) -> bytes:
        if not isinstance(value, Mapping):
            raise ValueError('value must be a dictionary')
        ret = b''
        for name, field in self.items(parent_struct):
            if field.is_padding:
                ret += field.pack(0, parent_struct, len(ret))
            else:
                field_val = value[name]
                ret += field.pack(field_val, parent_struct, len(ret))
        if self.__alignment > 1:
            # Do not take the read_bytes into account
            pad_count = self.__alignment - (len(ret) % self.__alignment)
            ret += b'\0' * pad_count
        return ret

    def unpack(
            self, parent_struct: Mapping[str, PackMemberType],
            read_bytes: int, data: bytes,
    ) -> PackMemberType:
        pos = 0
        ret: Dict[str, PackMemberBasic] = {}
        for name, item in self.items(parent_struct):
            size = item.size(parent_struct, pos)
            if not item.is_padding:
                ret[name] = item.unpack(parent_struct, pos, data[pos:pos+size])
            # else ignore field
            pos += size
        # trailing alignment padding can be ignored here
        return ret


class UnionDataPacketField(DataPacketField):
    """A structure whose structure depends upon a value previously read.
    Alignment is based on this structure itself, not total bytes."""
    __slots__ = ('__chooser', '__choices', '__alignment')

    def __init__(
            self, chooser: IntLookupCallback,
            choices: Dict[int, DataPacketField],
    ) -> None:
        self.__chooser = chooser
        self.__choices = choices

    def size(self, parent_struct: Mapping[str, PackMemberType], read_bytes: int) -> int:
        inner = self.__choices[self.__chooser(parent_struct)]
        return inner.size(parent_struct, 0)

    def pack(
            self, value: PackMemberType,
            parent_struct: Mapping[str, PackMemberType], written_bytes: int,
    ) -> bytes:
        inner = self.__choices[self.__chooser(parent_struct)]
        return inner.pack(value, parent_struct, 0)

    def unpack(
            self, parent_struct: Mapping[str, PackMemberType],
            read_bytes: int, data: bytes,
    ) -> PackMemberType:
        inner = self.__choices[self.__chooser(parent_struct)]
        return inner.unpack(parent_struct, 0, data)
