#!/usr/bin/python3

# https://xcb.freedesktop.org/XmlXcb/
# About:
#   https://cgit.freedesktop.org/xcb/proto/plain/doc/xml-xcb.txt

from typing import Sequence, Dict, Set, List, Tuple, Optional, Any
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


class FieldType:
    """Details about a field.  Not only the type, but also restrictions around it."""
    def __init__(self) -> None:
        self.name = ''
        self.py_type: Optional[str] = None
        self.count = 1  # 1 == A single value, > 1 a fixed array of these values, 0 == variable list
        self.list_size_expr: Optional[Expression] = None
        self.calculated_expr: Optional[Expression] = None
        self.min_val: Optional[int] = None
        self.max_val: Optional[int] = None
        self.mask: Optional[str] = None
        self.alt_mask: Optional[str] = None
        self.enum: Optional[str] = None
        self.alt_enum: Optional[str] = None
        self.align: Optional[int] = None

        # The order of the items in the switch statement are very important.
        # enum group, enum item, field type
        self.switch_ref_field: Optional[str] = None
        self.bit_switch: Optional[List[Tuple[str, str, StructureData]]] = None
        self.value_switch: Optional[List[Tuple[str, StructureData]]] = None

    def copy(self) -> 'FieldType':
        ret = FieldType()
        ret.name = self.name
        ret.py_type = self.py_type
        ret.count = self.count
        ret.list_size_expr = self.list_size_expr
        ret.calculated_expr = self.calculated_expr
        ret.min_val = self.min_val
        ret.max_val = self.max_val
        ret.switch_ref_field = self.switch_ref_field
        ret.bit_switch = None if self.bit_switch is None else list(self.bit_switch)
        ret.value_switch = None if self.value_switch is None else list(self.value_switch)
        return ret

    @property
    def is_alias(self) -> bool:
        return self.py_type is None

    @staticmethod
    def basic(name: str, py_type: str) -> 'FieldType':
        ret = FieldType()
        ret.name = name
        ret.py_type = py_type
        return ret

    @staticmethod
    def alias(name: str) -> 'FieldType':
        ret = FieldType()
        ret.name = name
        return ret


PREDEFINED_FIELDS: Dict[str, FieldType] = {
    # Cardinal bit count
    'CARD8': FieldType.basic('ctypes.c_uint8', 'int'),
    'CARD16': FieldType.basic('ctypes.c_uint16', 'int'),
    'CARD32': FieldType.basic('ctypes.c_uint32', 'int'),
    'CARD64': FieldType.basic('ctypes.c_uint64', 'int'),

    'INT8': FieldType.basic('ctypes.c_int8', 'int'),
    'INT16': FieldType.basic('ctypes.c_int16', 'int'),
    'INT32': FieldType.basic('ctypes.c_int32', 'int'),
    'INT64': FieldType.basic('ctypes.c_int64', 'int'),

    'char': FieldType.basic('ctypes.c_int64', 'int'),
    'float': FieldType.basic('ctypes.c_float', 'float'),
    'double': FieldType.basic('ctypes.c_double', 'float'),
    'BYTE': FieldType.basic('ctypes.c_uint8', 'int'),
    'BOOL': FieldType.basic('ctypes.c_uint8', 'bool'),
    'BOOL8': FieldType.basic('ctypes.c_uint8', 'bool'),
    'BOOL16': FieldType.basic('ctypes.c_uint16', 'bool'),
    'BOOL32': FieldType.basic('ctypes.c_uint32', 'bool'),
    'void': FieldType.basic('ctypes.c_uint8', 'None'),
}

FD_FIELD = FieldType.basic('file_descriptor', 'int')


class StructureData:
    """A structure"""
    def __init__(self) -> None:
        # list of entries, name, type
        self.name = ''
        self.records: List[Tuple[str, FieldType]] = []
        self.length_expr: Optional[Expression] = None


class EventStructureData:
    """An event's structure"""
    def __init__(self) -> None:
        # list of entries, name, type
        self.name = ''
        self.records: List[Tuple[str, FieldType]] = []


class RequestData:
    """A request"""
    def __init__(self) -> None:
        self.name = ''
        self.brief = ''
        self.long = ''
        self.args: List[Tuple[str, FieldType]] = []
        self.ret: Optional[FieldType] = None


class UnionData:
    """A union"""
    def __init__(self) -> None:
        self.name = ''
        self.args: List[Tuple[str, FieldType]] = []
        self.ret: Optional[FieldType] = None


class EventData:
    """An event"""
    def __init__(self) -> None:
        self.name = ''
        self.args: List[Tuple[str, FieldType]] = []
        self.ret: Optional[FieldType] = None


class ErrorData:
    """An error"""
    def __init__(self) -> None:
        self.name = ''
        self.args: List[Tuple[str, FieldType]] = []
        self.ret: Optional[FieldType] = None


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
                    ret.structures[struct_data.name] = struct_data
            elif item.tagName == 'union':
                union_data = parse_union(item)
                if union_data:
                    ret.unions[union_data.name] = union_data
            elif item.tagName == 'eventstruct':
                event_struct_data = parse_event_struct(item)
                if event_struct_data:
                    ret.event_structures[event_struct_data.name] = event_struct_data
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
            elif item.tagName == 'event':
                event_data = parse_event(item)
                if event_data:
                    ret.events[event_data.name] = event_data
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
            if byte_count is None:
                if align_amount is None:
                    raise ValueError(f'{name}: no "bytes" or "align" attribute on pad')
                field = FieldType.basic(f'ctypes.c_uint8 * ?', 'Sequence[int]')
                field.count = 0
                field.align = align_amount
            else:
                field = FieldType.basic(f'ctypes.c_uint8 * {byte_count}', 'Sequence[int]')
                field.count = byte_count
            ret.records.append((f'pad{pad_index}', field))
            pad_index += 1

        elif item.tagName == 'length':
            ret.length_expr = parse_expression(item)

        elif item.tagName in ('field', 'list', 'exprfield'):
            field_name = _str_attr(item, 'name')
            if not field_name:
                raise ValueError(f'{name}: no field name for {item.tagName}')
            field_val = parse_basic_field(item)
            if item.tagName == 'list':
                expr = parse_expression(item.childNodes)
                field_val.count = 0
                field_val.list_size_expr = expr
            elif item.tagName == 'exprfield':
                # calculated field, not sent in the request.
                expr = parse_expression(item.childNodes)
                field_val.calculated_expr = expr
            ret.records.append((field_name, field_val))

        elif item.tagName == 'fd':
            field_name = _str_attr(item, 'name')
            if not field_name:
                raise ValueError(f'{name}: no name in file descriptor field')
            ret.records.append((field_name, FD_FIELD))

        elif item.tagName == 'switch':
            field_name = _str_attr(item, 'name')
            if not field_name:
                raise ValueError(f'{name}: no name in switch field')
            field_val = FieldType()
            field_val.name = 'ctypes.c_void_p'
            field_val.value_switch = []
            field_val.bit_switch = []
            for child in item.childNodes:
                if not isinstance(child, Element):
                    continue
                if child.tagName == 'fieldref':
                    field_val.switch_ref_field = _dom_text(child)
                elif child.tagName in ('bitcase', 'case'):
                    enumref = child.getElementsByTagName('enumref')[0]
                    enum_ref = _str_attr(enumref, 'ref')
                    enum_val = _dom_text(enum_ref)
                    # ref="CW">BackPixmap</enumref>
                    inner_struct = parse_struct(child, f'{enum_ref}_{enum_val}')
                    if child.tagName == 'bitcase':
                        field_val.bit_switch.append((enum_ref, enum_val, inner_struct))
                    else:
                        field_val.value_switch.append((enum_ref, enum_val, inner_struct))
            if not field_val.switch_ref_field:
                raise ValueError(f'{name}: no fieldref in switch {field_name}')
            ret.records.append((field_name, field_val))

        elif item.tagName == 'valueparam':
            # Older type that we're not supporting right now?
            raise ValueError(f'{name}: valueparam not supported')
        elif item.tagName in ('enumref', 'required_start_align'):
            # Only should be present for inner structure switches.
            pass
        else:
            raise ValueError(f'{name}: unknown tag {item.tagName}')
    return ret


def parse_basic_field(field: Element) -> FieldType:
    field_type = _str_attr(field, 'type')
    field_val = PREDEFINED_FIELDS.get(field_type)
    if field_val:
        field_val = field_val.copy()
    else:
        field_val = FieldType.alias(field_type)
    field_val.mask = _str_attr(field, 'mask') or None
    field_val.alt_mask = _str_attr(field, 'altmask') or None
    field_val.enum = _str_attr(field, 'enum') or None
    field_val.alt_enum = _str_attr(field, 'altenum') or None
    return field_val


def parse_expression(expr: Element) -> Expression:
    ret = Expression()
    ret.expression_doc = expr
    return ret


def parse_union(parent: Element) -> Optional[UnionData]:
    name = _str_attr(parent, 'name')
    print(f"{name}: skipping union; not supported")
    return None


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
    name = _str_attr(parent, 'name')
    opcode = _int_attr(parent, 'opcode')
    combine_adjacent = _str_attr(parent, 'combine-adjacent')
    print(f"{name}: skipping request {opcode}; not implemented")
    return None


def parse_event(parent: Element) -> Optional[EventData]:
    name = _str_attr(parent, 'name')
    number = _int_attr(parent, 'number')
    no_sequence_number = _bool_attr(parent, 'no-sequence-number')
    is_generic_event = _bool_attr(parent, 'xge')
    print(f"{name}: skipping event {number}; not implemented")
    return None


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
# Main

def main(args: Sequence[str]) -> int:
    if len(args) != 3 or '-h' in args or '--help' in args:
        print(f"Usage: {args[0]} (package name) (outdir)")
        return 0
    tmpdir = tempfile.mkdtemp()
    try:
        xcb_src = os.path.join(tmpdir, 'xcb')
        pull_repo(xcb_src)
        for src_file in find_xcb_src(xcb_src):
            print(f"Parsing {src_file} -------------------------------------------")
            contents = parse_proto_file(src_file)
            if contents:
                pass
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
