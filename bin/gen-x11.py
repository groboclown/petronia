#!/usr/bin/python3

# https://xcb.freedesktop.org/XmlXcb/
# About:
#   https://cgit.freedesktop.org/xcb/proto/plain/doc/xml-xcb.txt
from io import StringIO
from typing import Sequence, Dict, Set, List, Tuple, Literal, Optional, Any
import os
import sys
import subprocess
import tempfile
import shutil
import xml.dom.minidom
from xml.dom.minidom import Element, Node


# ---------------------------------------------------------------------------
# Structure Representations


class Expression:
    """Structured expression"""
    def __init__(self) -> None:
        self.expression_doc: Optional[Element] = None
        self.value_expr: Optional[str] = None

    @property
    def lambda_expr(self) -> str:
        if self.value_expr is None:
            if self.expression_doc is None:
                return f'lambda d, c: raise ValueExpression("Nothing is here")'
            else:
                writer = StringIO()
                self.expression_doc.writexml(writer)
                return f'lambda d, c: raise ValueError({repr(writer.getvalue())})'

        return f'lambda d, c: {self.value_expr}'


class AbstractFieldDef:
    """A generic field definition."""

    def generate_packet_field(self, indent: str) -> Optional[str]:
        """Create a packet field (DataPacketField) constructor text.  If it isn't
        included in the model, then it returns None"""
        raise NotImplementedError

    def generate_py_type(self) -> Optional[str]:
        raise NotImplementedError


class Field:
    """Details about a field.  Not only the type, but also restrictions around it."""
    __slots__ = ('name', 'field_def')

    def __init__(self, name: str, field_def: AbstractFieldDef) -> None:
        self.name = name
        self.field_def = field_def


class CalculatedFieldDef(AbstractFieldDef):
    """A calculated field"""

    def __init__(self, expr: Expression) -> None:
        self.expr = expr

    def generate_packet_field(self, indent: str) -> Optional[str]:
        return None

    def generate_py_type(self) -> Optional[str]:
        return 'int'


class SimpleFieldDef(AbstractFieldDef):
    __slots__ = (
        'value_type', 'py_type', 'count', 'mask', 'alt_mask', 'enum', 'alt_enum',
        'ctype_type',
    )

    def __init__(self, value_type: str, py_type: str, ctype_type: str) -> None:
        self.value_type = value_type
        self.py_type = py_type
        self.ctype_type = ctype_type
        self.count = 1
        self.mask: Optional[str] = None
        self.alt_mask: Optional[str] = None
        self.enum: Optional[str] = None
        self.alt_enum: Optional[str] = None

    def generate_packet_field(self, indent: str) -> Optional[str]:
        """Create a packet field (DataPacketField) constructor text.  If it isn't
        included in the model, then it returns None"""
        if self.count < 1:
            return None
        if self.count == 1:
            return f'FixedDataPacketField({self.value_type})'
        return f'FixedDataPacketField({self.value_type}, {self.count})'

    def generate_py_type(self) -> Optional[str]:
        if self.count < 1:
            return None
        if self.count == 1:
            return self.py_type
        return f'Sequence[{self.py_type}]'


class FieldDefPrototype:
    __slots__ = ('value_type', 'py_type', 'ctype_type')

    def __init__(self, value_type: str, py_type: str, ctype_type: str) -> None:
        self.value_type = value_type
        self.py_type = py_type
        self.ctype_type = ctype_type

    def mk(self) -> 'SimpleFieldDef':
        ret = SimpleFieldDef(self.value_type, self.py_type, self.ctype_type)
        ret.count = 1
        return ret


class ListFieldDef(AbstractFieldDef):
    """List of a type"""
    def __init__(
            self, base: AbstractFieldDef, length_expr: Expression,
    ) -> None:
        self.base = base
        self.length_expr = length_expr
        self.alignment = 0

    def generate_packet_field(self, indent: str) -> Optional[str]:
        if isinstance(self.base, SimpleFieldDef):
            return (
                f'SimpleListDataPacketField('
                f'{self.base.value_type}, '
                f'{self.length_expr.lambda_expr}, '
                f'{self.alignment})'
            )
        return (
            f'ListDataPacketField('
            f'{self.base.generate_packet_field(indent)}, '  # must not return None
            f'{self.length_expr.lambda_expr})'
        )

    def generate_py_type(self) -> Optional[str]:
        return f'Sequence[{self.base.generate_py_type()}]'


class PadFieldDef(AbstractFieldDef):
    """Padding"""
    __slots__ = ('count', 'align')

    def __init__(self, count: Optional[int], align: Optional[int]) -> None:
        assert (
                not (count is not None and align is not None)
                and not (count is None and align is None)
        )
        self.count = count
        self.align = align

    def generate_packet_field(self, indent: str) -> Optional[str]:
        if self.count is not None:
            return f'FixedPadDataPacketField({self.count})'
        assert self.align is not None  # nosec  # programmer aid
        return f'AlignedPadDataPacketField({self.align})'

    def generate_py_type(self) -> Optional[str]:
        return None


class AliasFieldDef(SimpleFieldDef):
    """Alias to another type; generally, an XID."""

    def __init__(self) -> None:
        SimpleFieldDef.__init__(self, 'MARKER_UINT32', 'int', 'ctypes.c_uint32')


ALIAS_FIELD_DEF = AliasFieldDef()


class EnumRefFieldDef(AbstractFieldDef):
    """Field that references an enum value."""
    # Enum types can be all sorts of int sizes.

    def __init__(self, enum_name: str) -> None:
        self.enum_name = enum_name
        self.limits: Optional[List[str]] = None

    def generate_packet_field(self, indent: str) -> Optional[str]:
        raise ValueError(f'{self.enum_name}: cannot generate packet field')

    def generate_py_type(self) -> Optional[str]:
        return 'int'


PREDEFINED_FIELDS: Dict[str, FieldDefPrototype] = {
    # Cardinal bit count
    'CARD8': FieldDefPrototype('MARKER_UINT8', 'int', 'ctypes.c_uint8'),
    'CARD16': FieldDefPrototype('MARKER_UINT16', 'int', 'ctypes.c_uint16'),
    'CARD32': FieldDefPrototype('MARKER_UINT32', 'int', 'ctypes.c_uint32'),
    'CARD64': FieldDefPrototype('MARKER_UINT64', 'int', 'ctypes.c_uint64'),

    'INT8': FieldDefPrototype('MARKER_INT8', 'int', 'ctypes.c_int8'),
    'INT16': FieldDefPrototype('MARKER_INT16', 'int', 'ctypes.c_int16'),
    'INT32': FieldDefPrototype('MARKER_INT32', 'int', 'ctypes.c_int32'),
    'INT64': FieldDefPrototype('MARKER_INT64', 'int', 'ctypes.c_int64'),

    'char': FieldDefPrototype('MARKER_INT8', 'int', 'ctypes.c_int8'),
    'float': FieldDefPrototype('MARKER_FLOAT32', 'float', 'ctypes.c_float'),
    'double': FieldDefPrototype('MARKER_FLOAT64', 'float', 'ctypes.c_double'),
    'BYTE': FieldDefPrototype('MARKER_INT8', 'int', 'ctypes.c_int8'),
    'BOOL': FieldDefPrototype('MARKER_UINT8', 'bool', 'ctypes.c_int8'),
    'BOOL8': FieldDefPrototype('MARKER_UINT8', 'bool', 'ctypes.c_int8'),
    'BOOL16': FieldDefPrototype('MARKER_UINT16', 'bool', 'ctypes.c_int16'),
    'BOOL32': FieldDefPrototype('MARKER_UINT32', 'bool', 'ctypes.c_int32'),
    'void': FieldDefPrototype('MARKER_UINT8', 'None', 'ctypes_c_void_p'),
}

# TODO This one is weird and needs to be specially managed.
FD_FIELD = FieldDefPrototype('file_descriptor', 'int', 'ctypes.c_int32')


class StructFieldDef(AbstractFieldDef):
    __slots__ = ('fields',)

    def __init__(self) -> None:
        self.fields: List[Tuple[str, AbstractFieldDef]] = []

    def generate_packet_field(self, indent: str) -> Optional[str]:
        ret = 'StructureDataPacketField((\n'
        for name, field in self.fields:
            field_val = field.generate_packet_field(indent + '    ')
            if not field_val:
                continue
            ret += f'{indent}    ({repr(name)}, {field_val}),\n'
        ret += f'{indent}))'
        return ret

    def generate_py_type(self) -> Optional[str]:
        # This should be stronger typed
        types = set()
        for _name, field in self.fields:
            py_type = field.generate_py_type()
            if py_type is not None:
                types.add(py_type)
        if len(types) == 1:
            return f'Mapping[str, {list(types)[0]}]'
        return f'Mapping[str, Union[{", ".join(list(types))}]]'


class StructureData:
    """A structure"""
    __slots__ = ('name', 'records', 'length_expr', 'category', 'doc', 'consts', 'has_reply')

    def __init__(self) -> None:
        # list of entries, name, type
        self.name = ''
        self.records: List[Field] = []
        self.length_expr: Optional[Expression] = None
        self.category = 'Struct'
        self.doc: Optional[Element] = None
        self.has_reply = False
        self.consts: Dict[str, int] = {}

    def as_struct_field(self) -> StructFieldDef:
        ret = StructFieldDef()
        ret.fields = [
            (rec.name, rec.field_def)
            for rec in self.records
        ]
        return ret


class FieldCase:
    """A case in a field for a bit value."""
    def __init__(self, enum_ref: str, enum_value: str, field_def: AbstractFieldDef) -> None:
        self.enum_ref = enum_ref
        self.enum_value = enum_value
        self.field_def = field_def


class SwitchFieldDef(AbstractFieldDef):
    """A variable length field whose value depends on the bits of another value."""
    __slots__ = ('cases', 'field_ref', 'lookup', 'alignment', 'has_value', 'has_bit')

    def __init__(self, field_ref: str, cases: List[FieldCase]) -> None:
        self.cases = cases
        self.field_ref = field_ref
        self.lookup = Expression()
        self.lookup.value_expr = f'd[{repr(field_ref)}]'
        self.alignment = 0
        self.has_value = False
        self.has_bit = False

    def generate_packet_field(self, indent: str) -> Optional[str]:
        if self.has_bit:
            if self.has_value:
                raise ValueError('switch field has both bit and value cases')
            category = 'BitDataPacketField'
        elif self.has_value:
            category = 'UnionDataPacketField'
        else:
            raise ValueError('switch field has no cases')
        ret = f'{category}({self.lookup.lambda_expr}, {{\n'
        for case in self.cases:
            enum_ref_name = normalize_name(case.enum_ref, 'Camel')
            ret += (
                f"{indent}    {enum_ref_name}Values."
                f"{normalize_name(case.enum_value, 'SCREAMING')}: "
                f"{case.field_def.generate_packet_field(indent + '    ')},\n"  # should not be None
            )
        ret += f'{indent}}}, {self.alignment})'
        return ret

    def generate_py_type(self) -> Optional[str]:
        types = set()
        for case in self.cases:
            # types.add(case.field_def.generate_py_type())
            types.add(normalize_name(case.enum_ref, 'Camel') + 'Values')
        if len(types) == 1:
            return f'Mapping[str, {list(types)[0]}]'
        return f'Mapping[str, Union[{", ".join(list(types))}]]'


class EventStructureData:
    """An event's structure"""
    def __init__(self) -> None:
        # list of entries, name, type
        self.name = ''
        self.struct_data: Optional[StructureData] = None


class RequestData:
    """A request"""
    def __init__(self) -> None:
        self.name = ''
        self.brief = ''
        self.long = ''
        self.opcode = 0
        self.combine_adjacent: Optional[str] = ''
        self.start_align: Optional[int] = None
        self.request: Optional[StructureData] = None
        self.reply: Optional[StructureData] = None


class UnionData:
    """A union"""
    def __init__(self) -> None:
        self.name = ''
        self.as_structure: Optional[StructureData] = None
        self.fields_as_structure: Dict[str, StructureData] = {}


class EventData:
    """An event"""
    def __init__(self) -> None:
        self.name = ''
        self.event_number = 0
        self.as_structure: Optional[StructureData] = None
        self.body_structure: Optional[StructureData] = None
        self.has_sequence_number = True
        self.is_generic_event = False


class ErrorData:
    """An error"""
    def __init__(self) -> None:
        self.name = ''
        self.args: List[Field] = []


class ProtoFile:
    """A structure."""
    def __init__(self) -> None:
        self.lib_name = ''
        self.version = ''

        # name -> structure
        self.structures: Dict[str, StructureData] = {}
        self.event_structures: Dict[str, EventStructureData] = {}
        self.unions: Dict[str, UnionData] = {}

        # new type alias -> old alias
        self.type_aliases: Dict[str, str] = {}

        # error alias name -> new error number, original error reference
        self.error_aliases: Dict[str, Tuple[int, str]] = {}

        # event alias name -> new event number, original event reference
        self.event_aliases: Dict[str, Tuple[int, str]] = {}

        self.enums: Dict[str, Dict[str, int]] = {}
        self.requests: Dict[str, RequestData] = {}
        self.events: Dict[str, EventData] = {}
        self.errors: Dict[str, ErrorData] = {}
        self.imports: Set[str] = set()
        self.xid_types: Set[str] = set()
        self.xid_unions: Dict[str, Set[str]] = {}

    def add_structure(self, struct_data: Optional[StructureData]) -> None:
        if not struct_data:
            return
        name = normalize_name(struct_data.name, 'Camel') + struct_data.category
        if name in self.structures:
            raise ValueError(f'Duplicate structures named {name}')
        self.structures[name] = struct_data

# ---------------------------------------------------------------------------
# Parsers


def parse_proto_file(filename: str) -> Optional[ProtoFile]:
    doc = xml.dom.minidom.parse(filename)
    root_nodes = doc.getElementsByTagName('xcb')
    if not root_nodes:
        return None
    # Should just be one root, but...
    ret = ProtoFile()
    for xcb in root_nodes:
        if not isinstance(xcb, Element):
            continue
        ret.lib_name = _str_attr(xcb, 'header')
        ret.version = _str_attr(xcb, 'major-version') or '0'
        for item in xcb.childNodes:
            if not isinstance(item, Element):
                continue
            if item.tagName == 'import':
                text = _dom_text(item)
                if text:
                    ret.imports.add(text)
            elif item.tagName == 'struct':
                struct_data = parse_struct(item)
                if struct_data:
                    ret.add_structure(struct_data)
            elif item.tagName == 'union':
                union_data = parse_union(item)
                if union_data:
                    ret.unions[union_data.name] = union_data
            elif item.tagName == 'eventstruct':
                event_struct_data = parse_event_struct(item)
                if event_struct_data:
                    ret.event_structures[event_struct_data.name] = event_struct_data
                    ret.add_structure(event_struct_data.struct_data)
            elif item.tagName == 'xidtype':
                name = _str_attr(item, 'name')
                if name:
                    ret.xid_types.add(name)
            elif item.tagName == 'xidunion':
                name = _str_attr(item, 'name')
                unions = ret.xid_unions.get(name)
                if unions is None:
                    unions = set()
                    ret.xid_unions[name] = unions
                for child in item.getElementsByTagName('type'):
                    unions.add(_dom_text(child))
            elif item.tagName == 'enum':
                parse_enum(item, ret.enums)
            elif item.tagName == 'typedef':
                old_name = _str_attr(item, 'oldname')
                new_name = _str_attr(item, 'newname')
                if old_name and new_name:
                    ret.type_aliases[new_name] = old_name
            elif item.tagName == 'request':
                request_data = parse_request(item)
                if request_data:
                    ret.requests[request_data.name] = request_data
                    ret.add_structure(request_data.request)
                    ret.add_structure(request_data.reply)
            elif item.tagName == 'event':
                event_data = parse_event(item)
                if event_data:
                    ret.events[event_data.name] = event_data
                    ret.add_structure(event_data.as_structure)
            elif item.tagName == 'error':
                error_data = parse_error(item)
                if error_data:
                    ret.errors[error_data.name] = error_data
            elif item.tagName == 'eventcopy':
                name = _str_attr(item, 'name')
                number = _int_attr(item, 'number')
                ref = _str_attr(item, 'ref')
                if name and ref and number is not None:
                    ret.event_aliases[name] = number, ref
            elif item.tagName == 'errorcopy':
                name = _str_attr(item, 'name')
                number = _int_attr(item, 'number')
                ref = _str_attr(item, 'ref')
                if name and ref and number is not None:
                    ret.error_aliases[name] = number, ref
            else:
                raise ValueError(f'Unknown tag {item.tagName}')
    return ret


def parse_struct(parent: Element, given_name: Optional[str] = None) -> Optional[StructureData]:
    name = given_name or _str_attr(parent, 'name')
    ret = StructureData()
    ret.name = name
    pad_index = 0
    for item in parent.childNodes:
        if not isinstance(item, Element):
            continue

        if item.tagName == 'pad':
            byte_count = _int_attr(item, 'bytes')
            align_amount = _int_attr(item, 'align')
            # ignore "serialize" attribute
            if byte_count is None and align_amount is None:
                raise ValueError(f'{name}: no "bytes" or "align" attribute on pad')
            field = PadFieldDef(byte_count, align_amount)
            ret.records.append(Field(f'pad{pad_index}', field))
            pad_index += 1

        elif item.tagName == 'length':
            ret.length_expr = parse_expression(item, False)

        elif item.tagName in ('field', 'list', 'exprfield'):
            field_name = _str_attr(item, 'name')
            if not field_name:
                raise ValueError(f'{name}: no field name for {item.tagName}')
            field_val: AbstractFieldDef = parse_basic_field(item)
            if item.tagName == 'list':
                expr = parse_expression(item, False)
                if not isinstance(field_val, SimpleFieldDef):
                    raise ValueError(f'{name}: list field type is not simple')
                field_val = ListFieldDef(field_val, expr)
            elif item.tagName == 'exprfield':
                # calculated field, not sent in the request.
                expr = parse_expression(item, False)
                field_val = CalculatedFieldDef(expr)
            ret.records.append(Field(field_name, field_val))

        elif item.tagName == 'fd':
            field_name = _str_attr(item, 'name')
            if not field_name:
                raise ValueError(f'{name}: no name in file descriptor field')
            ret.records.append(Field(field_name, FD_FIELD.mk()))

        elif item.tagName == 'switch':
            field_name = _str_attr(item, 'name')
            if not field_name:
                raise ValueError(f'{name}: no name in switch field')
            cases: List[FieldCase] = []
            value_case_count = 0
            bit_case_count = 0
            ref_field = ''

            for child in item.childNodes:
                if not isinstance(child, Element):
                    continue
                if child.tagName == 'fieldref':
                    ref_field = _dom_text(child)
                elif child.tagName in ('bitcase', 'case'):
                    enumref_el = child.getElementsByTagName('enumref')[0]
                    enum_ref = _str_attr(enumref_el, 'ref')
                    enum_val = _dom_text(enumref_el)
                    inner_struct = parse_struct(child, f'{enum_ref}_{enum_val}')
                    if len(inner_struct.records) == 1:
                        cases.append(FieldCase(enum_ref, enum_val, inner_struct.records[0].field_def))
                    else:
                        cases.append(FieldCase(enum_ref, enum_val, inner_struct.as_struct_field()))
                    if child.tagName == 'bitcase':
                        bit_case_count += 1
                    else:
                        value_case_count += 1

            switch_field = SwitchFieldDef(ref_field, cases)
            switch_field.has_bit = bit_case_count > 0
            switch_field.has_value = value_case_count > 0
            ret.records.append(Field(field_name, switch_field))

        elif item.tagName == 'valueparam':
            # Older type that we're not supporting right now?
            raise ValueError(f'{name}: valueparam not supported')
        elif item.tagName in ('enumref', 'required_start_align', 'reply'):
            # Only should be present for inner structure switches.
            pass
        elif item.tagName == 'doc':
            ret.doc = item
        else:
            raise ValueError(f'{name}: unknown tag {item.tagName}')
    return ret


def parse_basic_field(field: Element) -> SimpleFieldDef:
    field_type = _str_attr(field, 'type')
    if field_type in PREDEFINED_FIELDS:
        field_val = PREDEFINED_FIELDS[field_type].mk()
    else:
        field_val = AliasFieldDef()
    field_val.mask = _str_attr(field, 'mask') or None
    field_val.alt_mask = _str_attr(field, 'altmask') or None
    field_val.enum = _str_attr(field, 'enum') or None
    field_val.alt_enum = _str_attr(field, 'altenum') or None
    return field_val


def parse_expression(
        expr: Element, is_top: bool, key: str = 'd',
) -> Expression:
    ret = Expression()
    ret.expression_doc = expr

    # There can be at most 1 entry in the expression element.
    node: Optional[Element] = None
    if not is_top:
        for child in expr.childNodes:
            if isinstance(child, Element):
                if node is not None:
                    raise ValueError('expression can have at most 1 inner element')
                node = child
        if not node:
            print(f'WARNING: No expression in value')
            ret.value_expr = '1'
            return ret
    else:
        node = expr
    ret.value_expr = parse_expr_as_py(node, key)
    return ret


def parse_expr_as_py(value: Element, key: str) -> str:
    if value.tagName == 'popcount':
        expr = parse_expression(value, False, key)
        return expr.value_expr
    if value.tagName == 'fieldref':
        return f'{key}[{repr(_dom_text(value))}]'
    if value.tagName == 'paramref':
        return f'{key}[{repr(_dom_text(value))}]'
    if value.tagName == 'value':
        return _dom_text(value)
    if value.tagName in ('op', 'unop'):
        operand = _str_attr(value, 'op')
        first: Optional[str] = None
        second: Optional[str] = None
        for child in value.childNodes:
            if not isinstance(child, Element):
                continue
            if not first:
                first = '(' + parse_expr_as_py(child, key) + ')'
            elif not second:
                second = '(' + parse_expr_as_py(child, key) + ')'
            else:
                raise ValueError('operand with more than 2 values')
        if second:
            return f'{first} {operand} {second}'
        return f'{operand}{first}'
    if value.tagName == 'sumof':
        # ugh.
        inner: Optional[str] = None
        item_name = _str_attr(value, 'ref')
        for child in value.childNodes:
            if not isinstance(child, Element):
                continue
            if inner:
                raise ValueError('sumof with more than 1 value')
            inner = '(' + parse_expr_as_py(child, f'{key}1') + ')'
        return f'sum([{inner} for {key}1 in {key}[{repr(item_name)}]])'
    if value.tagName == 'listelement-ref':
        # current list element inside iterating expressions such as sumof
        return key
    raise ValueError(f'Unknown expression tag {value.tagName}')


def parse_union(parent: Element) -> Optional[UnionData]:
    as_struct = parse_struct(parent)
    # each element in this is an alternate for the others.
    ret = UnionData()
    ret.name = as_struct.name
    if as_struct.length_expr is not None:
        raise ValueError(f'union {ret.name} with length expression not allowed')
    for field in as_struct.records:
        new_struct = StructureData()
        new_struct.name = field.name
        new_struct.records.append(field)
        ret.fields_as_structure[new_struct.name] = new_struct
    ret.as_structure = as_struct
    return ret


def parse_event_struct(parent: Element) -> Optional[EventStructureData]:
    name = _str_attr(parent, 'name')
    print(f"{name}: skipping event structure; not supported")
    return None


def parse_enum(parent: Element, enums: Dict[str, Dict[str, int]]) -> None:
    name = _str_attr(parent, 'name')
    data = enums.get(name)
    if data is None:
        data = {}
        enums[name] = data
    else:
        print(f"Duplicate enum group {name}; joining results together.")

    for item in parent.getElementsByTagName('item'):
        item_name = _str_attr(item, 'name')
        for child in item.childNodes:
            if not isinstance(child, Element):
                continue
            raw_val = _dom_text(child)
            try:
                val = int(raw_val)
            except ValueError as err:
                raise ValueError(f'{name}: invalid value {raw_val}') from err
            if child.tagName == 'value':
                data[item_name] = val
            elif child.tagName == 'bit':
                data[item_name] = 1 << val
            else:
                raise ValueError(f'{name}: unknown enum tag {child.tagName}')


def parse_request(parent: Element) -> Optional[RequestData]:
    ret = RequestData()
    ret.name = _str_attr(parent, 'name')
    ret.opcode = _int_attr(parent, 'opcode')
    ret.combine_adjacent = _str_attr(parent, 'combine-adjacent')
    ret.request = parse_struct(parent, ret.name)
    ret.request.consts['OPCODE'] = ret.opcode
    ret.request.category = 'Request'
    for child in parent.childNodes:
        if not isinstance(child, Element):
            continue
        if child.tagName == 'required_start_align':
            ret.start_align = _int_attr(child, 'align')
        elif child.tagName == 'reply':
            ret.reply = parse_struct(child, ret.name + '_reply')
            ret.reply.category = 'Reply'
            ret.request.has_reply = True
        elif child.tagName == 'doc':
            ret.brief = _dom_text(child.getElementsByTagName('brief'))
            ret.long = _dom_text(child.getElementsByTagName('description'))
    return ret


def parse_event(parent: Element) -> Optional[EventData]:
    ret = EventData()
    ret.name = _str_attr(parent, 'name')
    ret.event_number = _int_attr(parent, 'number')
    ret.has_sequence_number = not _bool_attr(parent, 'no-sequence-number')
    ret.is_generic_event = _bool_attr(parent, 'xge')
    ret.body_structure = parse_struct(parent)

    ret.as_structure = StructureData()
    ret.as_structure.name = ret.name
    ret.as_structure.category = 'Event'

    ret.as_structure.records.append(Field(
        'response_type', PREDEFINED_FIELDS['CARD8'].mk(),
    ))
    if ret.is_generic_event:
        ret.as_structure.records.append(Field(
            'extension', PREDEFINED_FIELDS['CARD8'].mk(),
        ))
        ret.as_structure.records.append(Field(
            'sequence', PREDEFINED_FIELDS['CARD16'].mk(),
        ))
        ret.as_structure.records.append(Field(
            'length', PREDEFINED_FIELDS['CARD32'].mk(),
        ))
        ret.as_structure.records.append(Field(
            'event_type', PREDEFINED_FIELDS['CARD16'].mk(),
        ))
        if ret.body_structure.records:
            ret.as_structure.records.extend(ret.body_structure.records)
        else:
            length_expr = Expression()
            length_expr.value_expr = 'd["length"]'
            ret.as_structure.records.append(Field(
                'data', ListFieldDef(PREDEFINED_FIELDS['CARD8'].mk(), length_expr),
            ))

        # TODO The generic event structure xcb_ge_event_t has the full_sequence field
        #  at the 32byte boundary. That's why we've to inject this field into GE
        #  events while generating the structure for them.
    else:
        if ret.has_sequence_number:
            ret.as_structure.records.append(Field(
                'descriptor', PREDEFINED_FIELDS['CARD8'].mk(),
            ))
            ret.as_structure.records.append(Field(
                'sequence', PREDEFINED_FIELDS['CARD16'].mk(),
            ))
        ret.as_structure.records.extend(ret.body_structure.records)
    return ret


def parse_error(parent: Element) -> Optional[ErrorData]:
    name = _str_attr(parent, 'name')
    number = _int_attr(parent, 'number')
    print(f"{name}: skipping error {number}; not implemented")
    return None


# ---------------------------------------------------------------------------
# XML Helpers

def _dom_text(node_list: Any, trim: bool = True) -> str:
    ret = ''
    if isinstance(node_list, Element):
        node_list = node_list.childNodes
    for node in node_list:
        if isinstance(node, str):
            ret += node
        elif node and node.nodeType == Node.TEXT_NODE:
            ret += node.data
    if trim:
        return ret.strip()
    return ret


def _int_attr(node: Element, name: str) -> Optional[int]:
    val = node.getAttribute(name).strip()
    try:
        return int(val)
    except ValueError:
        return None


def _bool_attr(node: Element, name: str) -> Optional[bool]:
    val = node.getAttribute(name).strip()
    if val == 'true':
        return True
    if val == 'false':
        return False
    return None


def _str_attr(node: Element, name: str, trim: bool = True) -> Optional[str]:
    if node.hasAttribute(name):
        ret = node.getAttribute(name)
        if trim:
            return ret.strip()
        return ret
    return None


# ---------------------------------------------------------------------------
# Repo / File Discovery

def pull_repo(outdir: str) -> int:
    try:
        subprocess.run([
            "git", "clone", "https://gitlab.freedesktop.org/xorg/proto/xcbproto.git", outdir,
        ], check=True)
        return 0
    except subprocess.CalledProcessError as err:
        return err.returncode


def find_xcb_src(src_dir: str) -> Sequence[str]:
    ret: List[str] = []
    basedir = os.path.join(src_dir, 'src')
    for fn in os.listdir(basedir):
        fqn = os.path.join(basedir, fn)
        if os.path.isfile(fqn) and fn.endswith('.xml'):
            ret.append(fqn)
    return ret


# ---------------------------------------------------------------------------
# Generators


def normalize_name(src_name: str, case: Literal['snake', 'SCREAMING', 'camel', 'Camel']) -> str:
    prefix = ''
    name = ''
    if case == 'snake':
        prefix = 'v_'
        last_lower = True
        last_under = True
        for c in src_name:
            if last_lower and not last_under and c.isupper():
                last_lower = False
                last_under = True
                c = '_' + c
            elif c == '_':
                last_under = True
            name += c.lower()
    elif case == 'SCREAMING':
        prefix = 'V_'
        last_lower = True
        last_under = True
        for c in src_name:
            if c == '_':
                last_under = True
                last_lower = False
            elif last_lower and not last_under and c.isupper():
                last_lower = False
                last_under = True
                c = '_' + c
            else:
                last_under = False
                last_lower = c.islower()
            name += c.upper()
    elif case in ('camel', 'Camel'):
        prefix = 'v' if case == 'camel' else 'V'
        last_under = True
        last_upper = False
        for c in src_name:
            if name == '' and c.isalpha():
                if case == 'camel':
                    name += c.lower()
                else:
                    name += c.upper()
                    last_upper = True
                last_under = False
            elif c == '_':
                last_under = True
            elif c.isupper():
                last_under = False
                if last_upper:
                    name += c.lower()
                else:
                    name += c
                    last_upper = True
            elif last_under:
                last_under = False
                last_upper = True
                name += c.upper()
            else:
                last_under = False
                last_upper = False
                name += c
    name = name.replace('.', '_')
    if name[0].isnumeric():
        name = prefix + name
    if name in ('None', 'and', 'or', 'Any', 'str', 'int', 'float', 'class'):
        name = f'{prefix}{name}'
    return name


def gen_alignment_padding_lambda(padding: PadFieldDef) -> str:
    return str(padding.align)


def generate_data_packet(
        struct_val: StructureData,
        indent: str,
) -> str:
    ret = f'DataPacket((\n'
    for field in struct_val.records:
        ret += (
            f'{indent}    ({repr(field.name)},'
            f' {field.field_def.generate_packet_field(indent + "    ")}),\n'
        )
    ret += f'{indent}))'
    return ret


def gen_call_name(contents: ProtoFile, struct_val: StructureData) -> str:
    return contents.lib_name + '_' + normalize_name(struct_val.name, 'snake')


def gen_ctype_name(field: Field) -> Optional[str]:
    if isinstance(field.field_def, SimpleFieldDef):
        return field.field_def.ctype_type
    if isinstance(field.field_def, PadFieldDef) and field.field_def.count is not None:
        if field.field_def.count > 1:
            return f'ctypes.c_uint8 * {field.field_def.count}'
        return 'ctypes.c_uint8'
    # raise ValueError(f'{field.name}: Not a ctype_type field ({field.field_def})')
    return None


def generate_proto_src(
        outdir: str, package_name: str, contents: ProtoFile, index_files: List[str],
) -> None:
    pkg_dir = os.path.join(outdir, package_name.replace('.', '/'))
    os.makedirs(pkg_dir, exist_ok=True)
    pkg_file = os.path.join(pkg_dir, contents.lib_name + '.py')
    index_files.append(contents.lib_name)
    with open(pkg_file, 'w', encoding='utf-8') as fos:
        fos.write("""# GENERATED FILE.  DO NOT EDIT

from typing import Dict, Mapping, Sequence, BinaryIO, NewType, Union, Callable, Optional, Any
import ctypes
from ..packet import (
    DataPacket,
    FixedDataPacketField, SimpleListDataPacketField,
    FixedPadDataPacketField, AlignedPadDataPacketField,
    StructureDataPacketField, ListDataPacketField,
    BitDataPacketField, UnionDataPacketField,
    MARKER_PAD, MARKER_INT8, MARKER_UINT8, MARKER_INT16,
    MARKER_UINT16, MARKER_INT32, MARKER_UINT32, MARKER_INT64,
    MARKER_UINT64, MARKER_FLOAT32, MARKER_FLOAT64, MARKER_FLEXIBLE,
) 

""")
        fos.write(
            "# ------------------------------------------------------------------\n"
            "# Enums\n\n"
        )
        for enum_name, enum_values in contents.enums.items():
            name = normalize_name(enum_name, 'Camel')
            fos.write(f"{name}Type = NewType('{name}Type', int)\n\n\n")
            fos.write(f"class {name}Values:\n")
            for key, value in enum_values.items():
                fos.write(f"    {normalize_name(key, 'SCREAMING')} = {name}Type({value})\n")
            fos.write("\n\n")

        fos.write(
            "# ------------------------------------------------------------------\n"
            "# Aliases\n\n"
        )
        for xid_name in contents.xid_types:
            name = normalize_name(xid_name, 'Camel')
            fos.write(f"{name} = NewType('{name}', ctypes.c_uint32)\n")
        fos.write("\n\n")

        fos.write(
            "# ------------------------------------------------------------------\n"
            "# Structures, Events, Requests, Replies\n\n"
        )
        for struct_name, struct_val in contents.structures.items():
            if struct_val.has_reply:
                # This is a simple structure containing only a sequence value.
                fos.write(
                    f"\n{struct_name}Cookie = NewType('{struct_name}Cookie', ctypes.c_uint32)\n\n"
                )
            fos.write(f'\n{struct_name}Packet = ')
            fos.write(generate_data_packet(struct_val, ''))
            fos.write(f"\n\n\nclass {struct_name}:\n")
            for const_name, const_val in struct_val.consts.items():
                fos.write(f"    {normalize_name(const_name, 'SCREAMING')} = {repr(const_val)}\n")
            if struct_val.consts:
                fos.write("\n")
            if struct_val.records:
                fos.write("    __slots__ = (")
                first = True
                for field in struct_val.records:
                    # Pad values are not stored
                    if not isinstance(field.field_def, PadFieldDef):
                        if first:
                            first = False
                        else:
                            fos.write(", ")
                        fos.write(repr(normalize_name(field.name, 'snake')))
                fos.write(",)\n\n")
                fos.write(f"    def __init__(\n            self, *,\n")
                for field in struct_val.records:
                    py_type = field.field_def.generate_py_type()
                    if py_type:
                        fos.write(
                            f"            {normalize_name(field.name, 'snake')}: "
                            f"Optional[{py_type}] = None,\n"
                        )
                fos.write("    ) -> None:\n")
                for field in struct_val.records:
                    if not isinstance(field.field_def, PadFieldDef):
                        fos.write(
                            f"        self.{normalize_name(field.name, 'snake')} = "
                            f"{normalize_name(field.name, 'snake')}\n"
                        )
                fos.write("\n    def as_dict(self) -> Dict[str, Any]:\n        return {\n")
                for field in struct_val.records:
                    if not isinstance(field.field_def, PadFieldDef):
                        fos.write(
                            f"            {repr(field.name)}: "
                            f"self.{normalize_name(field.name, 'snake')},\n"
                        )
                fos.write(
                    f"        }}\n\n"
                    f"    @staticmethod\n"
                    f"    def from_data(inp: BinaryIO) -> '{struct_name}':\n"
                    f"        return {struct_name}(**{struct_name}Packet.unpack(inp))\n\n"
                    f"    def to_data(self) -> bytes:\n"
                    f"        return {struct_name}Packet.pack(**self.as_dict())\n\n"
                )
            else:
                fos.write(
                    f"    __slots__ = ()\n\n"
                    f"    def as_dict(self) -> Dict[str, Any]:\n"
                    f"        return {{}}\n\n"
                    f"    @staticmethod\n"
                    f"    def from_data(inp: BinaryIO) -> '{struct_name}':\n"
                    f"        return {struct_name}()\n\n"
                    f"    def to_data(self) -> bytes:\n"
                    f"        return b''\n\n"
                )

            if struct_val.category == 'Request':
                if struct_val.has_reply:
                    cookie_name = f'{struct_name}Cookie'
                else:
                    cookie_name = 'ctypes.c_uint32'
                fos.write('    lib: Optional[Callable[[')
                first = True
                for field in struct_val.records:
                    py_type = field.field_def.generate_py_type()
                    if py_type:
                        if first:
                            first = False
                        else:
                            fos.write(', ')
                        fos.write(py_type)
                fos.write(
                    f'], {cookie_name}]] = None\n\n'
                    f'    @staticmethod\n'
                    f'    def lib_call(library: ctypes.CDLL) -> None:\n'
                    f'        {struct_name}.lib = library.{gen_call_name(contents, struct_val)}\n'
                    f'        {struct_name}.lib.restype = {cookie_name}\n'
                    f'        {struct_name}.lib.argstype = ('
                )
                args = ", ".join([
                    gen_ctype_name(f) or "ctypes.c_void_p"
                    for f in struct_val.records
                ])
                if len(struct_val.records) == 1:
                    args += ','
                fos.write(f'{args})\n\n')

            fos.write(
                f"\nclass {struct_name}CType(ctypes.Structure):\n"
                f'    """{contents.lib_name} {struct_val.name}"""\n'
                f"    _fields_ = [\n"
            )
            for field in struct_val.records:
                cname = gen_ctype_name(field)
                if cname:
                    fos.write(f'        ("{field.name}", {cname}),\n')
                else:
                    fos.write('        ("var_data", ctypes.c_void_p),\n')
                    break
            fos.write("    ]\n\n")
            # TODO more?

        fos.write(
            "\n# ------------------------------------------------------------------\n"
            "# Unions\n\n"
        )
        for union_data in contents.unions.values():
            fos.write(f"{normalize_name(union_data.name, 'Camel')}Union = {{\n")
            for key, struct_val in union_data.fields_as_structure.items():
                fos.write(
                    f"    {repr(key)}: {generate_data_packet(struct_val, '    ')},\n"
                )
            fos.write("}\n\n")


def generate_index(
        outdir: str, package_name: str, index_files: List[str],
):
    pkg_dir = os.path.join(outdir, package_name.replace('.', '/'))
    os.makedirs(pkg_dir, exist_ok=True)
    pkg_file = os.path.join(pkg_dir, '__index__.py')
    with open(pkg_file, 'w', encoding='utf-8') as fos:
        fos.write("# GENERATED FILE.  DO NOT EDIT\n\n")
        # Do not import the files.  These must be individually imported as necessary
        #   to minimize memory.
        # for index_file in index_files:
        #     fos.write(f"from . import {index_file}\n")


# ---------------------------------------------------------------------------
# Main


def main(args: Sequence[str]) -> int:
    package_name = 'petronia_native_x11.libs.xproto.inner'
    outdir = os.path.join(os.path.dirname(args[0]), '..', 'projects', 'native-handler')
    repo_dir: Optional[str] = None
    rm_repo = False
    skip = False
    for i in range(1, len(args)):
        if skip:
            continue
        if args[i] in ('-h', '--help'):
            print(
                f"Usage: {args[0]} [--package package-name] [--outdir out-dir] [--repo repo-dir]\n"
                f"\n"
                f"where:\n"
                f"  package-name    name of the Python package to generate.\n"
                f"                  Default: {package_name}\n"
                f"  out-dir         base directory for the generated files.\n"
                f"                  Default: {outdir}\n"
                f"  repo-dir        directory of the xcbproto cloned git repository.\n"
                f"                  If not given, it is pulled using git."
            )
            return 0
        if args[i] == '--package':
            package_name = args[i + 1]
            skip = True
        elif args[i] == '--outdir':
            outdir = args[i + 1]
            skip = True
        elif args[i] == '--repo':
            repo_dir = args[i + 1]
            skip = True
        else:
            print(f"Unknown argument {args[i]}.  Use '--help' for detailed help.")
            return 1
    try:
        if repo_dir is None:
            rm_repo = True
            repo_dir = tempfile.mkdtemp()
            pull_repo(repo_dir)
        index_files: List[str] = []
        for src_file in find_xcb_src(repo_dir):
            print(f"Parsing {src_file} -------------------------------------------")
            contents = parse_proto_file(src_file)
            if contents:
                generate_proto_src(outdir, package_name, contents, index_files)
        generate_index(outdir, package_name, index_files)
    finally:
        if rm_repo and repo_dir:
            shutil.rmtree(repo_dir, ignore_errors=True)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
