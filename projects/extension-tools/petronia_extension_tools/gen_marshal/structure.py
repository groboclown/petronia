
"""
Create the marshaller Python object source.
"""

from typing import Dict, List, Sequence, Iterable, Set, Tuple, Union, Optional, Any
import functools
from petronia_common.util import StdRet, i18n
from petronia_common.extension.config import (
    AbcEventDataType,
    StructureEventDataType,
    ArrayEventDataType,
    BoolEventDataType,
    DatetimeEventDataType,
    EnumEventDataType,
    FloatEventDataType,
    IntEventDataType,
    StringEventDataType,
    SelectorEventDataType,
)
from .load_definition import ExtensionDataFile
from .gen_test_data import create_field_data_sample


# Import in the form of: from {0} import {1}
ImportStruct = Tuple[str, Optional[str], Optional[str]]

_REQUIRED_IMPORTS: Sequence[ImportStruct] = (
    ('typing', 'List', None),
    ('typing', 'Dict', None),
    ('typing', 'Any', None),
    ('petronia_common.util', 'StdRet', None),
    ('petronia_common.util', 'collect_errors_from', None),
    ('petronia_common.util', 'not_none', None),
    ('petronia_common.util', 'STANDARD_PETRONIA_CATALOG', None),
    ('petronia_common.util', 'i18n', '_'),
)

_EVENT_NAME_SUFFIX = 'Event'
_STATE_NAME_SUFFIX = 'State'

_ALLOWED_PUBLIC_ACCESS = ('public', 'target',)


def create_structures(
        data: ExtensionDataFile,
        generate_api: bool,
        generate_internals: bool,
        generate_states: bool,
) -> StdRet[Tuple[List[Dict[str, Any]], List[ImportStruct]]]:
    """
    Returns the structures document, along with required imports.
    """
    structures: List[Dict[str, Any]] = []
    seen_structures: Dict[Union[StructureEventDataType, SelectorEventDataType], List[str]] = {}
    imports: List[ImportStruct] = list(_REQUIRED_IMPORTS)
    if generate_api:
        for event in data.events:
            if not generate_internals:
                if (
                        event.receive_access not in _ALLOWED_PUBLIC_ACCESS
                        and event.send_access not in _ALLOWED_PUBLIC_ACCESS
                ):
                    continue
            # Look into skipping parse or export if the access isn't appropriate,
            # or if it's a binary event.
            # Note that __repr__ requires the export, so skipping that may not be
            # correct.
            ret_inner_structures = create_inner_structure(
                event.name, '{0}:{1}'.format(data.metadata.name, event.name),
                event.unique_target,
                event.structure, seen_structures, imports,
            )
            if ret_inner_structures.has_error:
                return ret_inner_structures.forward()
            structures.extend(ret_inner_structures.result)
    if generate_states:
        print(f"Creating state data for {data.metadata.name}")
        for state in data.state_data:
            print(f"Creating state data for {state.fqn}")
            ret_inner_structures = create_inner_structure(
                state.short_name + _STATE_NAME_SUFFIX, None, state.fqn,
                state.data_type, seen_structures, imports,
            )
            if ret_inner_structures.has_error:
                return ret_inner_structures.forward()
            structures.extend(ret_inner_structures.result)
    return StdRet.pass_ok((structures, imports))


def create_inner_structure(  # pylint: disable=too-many-locals,too-many-arguments,too-many-branches,too-many-statements
        name: str, fq_event_name: Optional[str], unique_target: Optional[str],
        structure: Union[StructureEventDataType, SelectorEventDataType, None],
        seen_structures: Dict[Union[StructureEventDataType, SelectorEventDataType], List[str]],
        imports: List[ImportStruct],
) -> StdRet[List[Dict[str, Any]]]:
    """Create a single structure, and any dependent structure."""
    struct_name = normalize_structure_name(name)
    is_event = False
    unique_target_fqn = unique_target
    if fq_event_name:
        is_event = True
        struct_name += _EVENT_NAME_SUFFIX
        if unique_target and ':' in fq_event_name:
            unique_target_fqn = fq_event_name[:fq_event_name.index(':') + 1] + unique_target
    if structure in seen_structures:
        if struct_name in seen_structures[structure]:
            # Exact same as a previous definition
            return StdRet.pass_ok([])
        # New definition
        seen_structures[structure].append(struct_name)

    if structure:
        for seen_struct, seen_names in seen_structures.items():
            if struct_name in seen_names:
                return StdRet.pass_errmsg(
                    'errors',
                    i18n(
                        'Duplicate structure name encountered: {name}; alternate names: {seen}; '
                        'original structure: {struct1}, overriding structure: {struct2}'
                    ),
                    name=struct_name, seen=seen_names,
                    struct1=repr(seen_struct), struct2=repr(structure),
                )
        seen_structures[structure] = [struct_name]

    ret: List[Dict[str, Any]] = []
    ret_struct: Dict[str, Any]
    if structure is None:
        # Binary structure
        ret.append({
            'structure_class_name': struct_name,
            'structure_const_name': camel_case_as_screaming_snake(struct_name),
            'indented_description': create_indented_description('Binary event'),
            'is_selector': False,
            'is_binary': True,
            'is_object': False,
            'field_names': [],
            'is_event': is_event,
            'unique_ids': [],
            'fq_event_name': repr(fq_event_name),
            'short_event_name': repr(name),
            'has_non_optional_fields': False,
            'has_fields': True,
            'raw_name': name,
        })
    elif isinstance(structure, SelectorEventDataType):
        imports.append(('typing', 'Union', None))
        ret_struct = {
            'structure_class_name': struct_name,
            'structure_const_name': camel_case_as_screaming_snake(struct_name),
            'indented_description': create_indented_description(structure.description),
            'is_selector': True,
            'is_binary': False,
            'is_object': False,
            'has_non_optional_fields': True,
            'selector_types': [],
            'unique_selector_type_names': [],
            'has_fields': True,
            'raw_name': name,
            'is_event': False,
        }
        for s_key, s_type in structure.selector_items():
            # Assertion for mypy requirements
            assert isinstance(s_key, str)  # nosec
            if not isinstance(s_type, (SelectorEventDataType, StructureEventDataType)):
                # Casting is added for non-simple types.
                imports.append(('typing', 'cast', None))
            ret_selector_item = get_field_struct(
                s_key, s_type, False, structure, ret,
                seen_structures, imports,
            )
            if ret_selector_item.has_error:
                return ret_selector_item.forward()
            selector_item = ret_selector_item.result
            selector_item['selector_type_repr'] = repr(s_key)
            ret_struct['selector_types'].append(selector_item)
        unique_names = {
            f['field_python_type']
            for f in ret_struct['selector_types']
        }
        ret_struct['unique_selector_type_names'] = [{
            'selector_type_name': n,
        } for n in unique_names]
        ret.append(ret_struct)
    else:
        field_names: List[Dict[str, Any]] = []
        non_optional_field_names: List[str] = []
        unique_ids: List[Dict[str, str]] = []
        if unique_target:
            unique_ids.append({
                'upper': 'TARGET',
                'rel_id': repr(unique_target),
                'fqn_id': repr(unique_target_fqn),
            })
        ret_struct = {
            'structure_class_name': struct_name,
            'structure_const_name': camel_case_as_screaming_snake(struct_name),
            'indented_description': create_indented_description(structure.description),
            'field_names': field_names,
            'is_selector': False,
            'is_binary': False,
            'is_object': True,
            'is_event': is_event,
            'unique_ids': unique_ids,
            'fq_event_name': repr(fq_event_name),
            'short_event_name': repr(name),
        }
        # The created structure is added to the list at the end
        last_field: Optional[Dict[str, Any]] = None
        for field_name, field_type in structure.fields():
            ret_field = get_field_struct(
                field_name, field_type.data_type, field_type.is_optional,
                structure, ret, seen_structures, imports,
            )
            if ret_field.has_error:
                return ret_field.forward()
            ret_struct['field_names'].append(ret_field.result)
            if not field_type.is_optional:
                non_optional_field_names.append(field_name)
            last_field = ret_field.result

        if last_field:
            last_field['last'] = True
        ret_struct['has_fields'] = len(field_names) > 0
        ret_struct['has_non_optional_fields'] = len(non_optional_field_names) > 0
        ret.append(ret_struct)
    return StdRet.pass_ok(ret)


def create_indented_description(desc: Optional[str]) -> str:
    """Create the description text that's indented by 4 spaces with a maximum width of 80."""
    if not desc:
        return '(no description)'
    ret = []
    line = ''
    word = ''
    hard_break = True

    def on_word_end() -> None:
        nonlocal line, word
        if word and line:
            if len(word) + len(line) + 1 > 80:
                ret.append(line)
                line = word
            else:
                line += ' ' + word
        elif word:
            line = word
        word = ''

    for i in desc:
        if i in '\r\n':
            on_word_end()
            hard_break = True
        elif i in ' \t':
            if hard_break:
                # allow for indents
                word += i
            else:
                on_word_end()
        else:
            hard_break = False
            word += i

    on_word_end()
    if line:
        ret.append(line)
    return '\n    '.join(ret)


def find_or_add_structure(
        field_name: str, structure: Union[StructureEventDataType, SelectorEventDataType],
        structures: List[Dict[str, Any]],
        seen_structures: Dict[Union[StructureEventDataType, SelectorEventDataType], List[str]],
        imports: List[ImportStruct],
) -> StdRet[str]:
    """Generate the structure text."""
    if structure in seen_structures:
        names = seen_structures[structure]
        # return the first name found, or, if for some reason there isn't
        # anything in this list, the structure name will be added.
        for name in names:
            return StdRet.pass_ok(name)
    name = normalize_structure_name(structure.suggested_name or field_name)
    ret_inner_structures = create_inner_structure(
        name, None, None, structure, seen_structures, imports,
    )
    if ret_inner_structures.has_error:
        return ret_inner_structures.forward()
    structures.extend(ret_inner_structures.result)
    return StdRet.pass_ok(name)


def get_field_struct(  # pylint: disable=R0912,R0913,R0915
        field_name: str, fdt: AbcEventDataType, is_optional: bool,
        owning_type: AbcEventDataType,
        structures: List[Dict[str, Any]],
        seen_structures: Dict[Union[StructureEventDataType, SelectorEventDataType], List[str]],
        imports: List[ImportStruct],
) -> StdRet[Dict[str, Any]]:
    """Get the data input for the structure's template."""
    ret_sample_full = create_field_data_sample(fdt, True)
    if ret_sample_full.has_error:
        return ret_sample_full.forward()
    ret_sample_bare = create_field_data_sample(fdt, False)
    if ret_sample_bare.has_error:
        return ret_sample_bare.forward()

    field: Dict[str, Any] = {
        'field_name': field_name,
        'last': False,
        'is_parent': fdt == owning_type,
        'is_optional': is_optional,
        'is_simple_type': False,
        'is_string_type': False,
        'is_int_type': False,
        'is_float_type': False,
        'is_bool_type': False,
        'is_datetime_type': False,
        'is_enum_type': False,
        'is_array_simple_type': False,
        'is_array_datetime_type': False,
        'is_struct_type': False,
        'is_array_struct_type': False,
        'enum_values': [],
        'selector_types': [],
        'unique_selector_type_names': [],
        'field_python_type': '--error--',
        'field_python_instance_type': '--not used--',
        'field_python_cast_type': None,
        'field_python_item_type': '--not used--',
        'sample_full': ret_sample_full.result,
        'sample_bare': ret_sample_bare.result,
    }
    if is_optional:
        imports.append(('typing', 'Optional', None,))
    if isinstance(fdt, IntEventDataType):
        field['is_simple_type'] = True
        field['is_int_type'] = True
        field['field_python_type'] = 'int'
        field['field_python_instance_type'] = 'SupportsInt'
        field['field_python_cast_type'] = 'int'
        imports.append(('typing', 'SupportsInt', None))
    elif isinstance(fdt, FloatEventDataType):
        field['is_simple_type'] = True
        field['is_float_type'] = True
        field['field_python_type'] = 'float'
        field['field_python_instance_type'] = 'SupportsFloat'
        field['field_python_cast_type'] = 'float'
        imports.append(('typing', 'SupportsFloat', None))
    elif isinstance(fdt, StringEventDataType):
        field['is_simple_type'] = True
        field['is_string_type'] = True
        field['field_python_type'] = 'str'
        field['field_python_instance_type'] = 'str'
        field['field_python_cast_type'] = None
    elif isinstance(fdt, BoolEventDataType):
        field['is_simple_type'] = True
        field['is_bool_type'] = True
        field['field_python_type'] = 'bool'
        field['field_python_instance_type'] = 'bool'
        field['field_python_cast_type'] = None
    elif isinstance(fdt, DatetimeEventDataType):
        field['is_datetime_type'] = True
        field['field_python_type'] = 'datetime.datetime'
        field['field_python_instance_type'] = 'datetime.datetime'
        imports.append(('datetime', None, None))
    elif isinstance(fdt, EnumEventDataType):
        field['is_enum_type'] = True
        field['field_python_type'] = 'str'
        field['enum_values'] = [
            {'enum_repr': repr(val), 'last_enum': False} for val in fdt.values
        ]
        field['first_enum_value'] = fdt.values[0]
        if field['enum_values']:
            field['enum_values'][-1]['last_enum'] = True
    elif isinstance(fdt, (StructureEventDataType, SelectorEventDataType)):
        field['is_struct_type'] = True
        ret_type = find_or_add_structure(
            field_name, fdt, structures, seen_structures, imports,
        )
        if ret_type.has_error:
            return ret_type.forward()
        field['field_python_type'] = ret_type.result
    elif isinstance(fdt, ArrayEventDataType):
        item_type = fdt.value_type
        if isinstance(item_type, (StructureEventDataType, SelectorEventDataType)):
            field['is_array_struct_type'] = True
            ret_type = find_or_add_structure(
                field_name, item_type, structures, seen_structures, imports,
            )
            if ret_type.has_error:
                return ret_type.forward()
            field['field_python_item_type'] = ret_type.result
            field['field_python_type'] = 'List[' + field['field_python_item_type'] + ']'
        elif isinstance(item_type, (
                StringEventDataType, BoolEventDataType, FloatEventDataType, IntEventDataType,
                EnumEventDataType, DatetimeEventDataType,
        )):
            field['is_array_simple_type'] = True
            inner_type: str = item_type.type_name
            if inner_type in ('string', 'enum',):
                inner_type = 'str'
            if inner_type == 'datetime':
                inner_type = 'datetime.datetime'
                field['is_array_datetime_type'] = True
            field['field_python_type'] = 'List[' + inner_type + ']'
            field['field_python_item_type'] = inner_type
            imports.append(('typing', 'cast', None,))
        else:
            raise Exception('Unsupported array field type: ' + repr(item_type))
    else:
        raise Exception('Unknown field type ' + repr(fdt))  # pragma no cover
    field['field_python_item_type_name'] = field['field_python_item_type'].replace('.', '_')
    return StdRet.pass_ok(field)


def normalize_structure_name(name: str) -> str:
    """Create a CamelCaseName for the structure."""
    next_cap = True
    ret = ''
    for i in name:
        if i.isalnum():
            if next_cap:
                ret += i.upper()
            else:
                ret += i
            next_cap = i.isnumeric()
        else:
            next_cap = True
    return ret


def camel_case_as_screaming_snake(name: str) -> str:
    """Transform a CamelCaseName to SCREAMING_SNAKE_CASE."""
    ret = ''
    found_break = True
    for i in name:
        if found_break:
            found_break = False
        elif i.isupper():
            ret += '_'
            found_break = True
        ret += i.upper()
    return ret


def create_import_struct(import_list: List[ImportStruct]) -> List[Dict[str, Any]]:
    """Create the import document fragment."""
    package_parts: Dict[str, Set[Tuple[Optional[str], Optional[str]]]] = {}
    for package, name, rename in import_list:
        if package not in package_parts:
            package_parts[package] = set()
        package_parts[package].add((name, rename,))
    ret: List[Dict[str, Any]] = []
    for package in sort_import_packages(package_parts.keys()):
        parts = package_parts[package]
        named_imports: Set[str] = set()
        for name, rename in parts:
            if not name:
                # import {package}
                ret.append({'plain_import': [{'import_package': package}]})
            elif not rename:
                # from {package} import {name}
                named_imports.add(name)
            else:
                # from {package} import {name} as {rename}
                ret.append({'renamed_import': [{
                    'import_package': package,
                    'import_name': name,
                    'import_rename': rename,
                }]})
        if len(named_imports) == 1:
            # from {package} import {name}
            ret.append({'one_child_import': [{
                'import_package': package,
                'import_name': ''.join(named_imports),
            }]})
        elif len(named_imports) > 1:
            # from {package} import {name}, {name}
            ret.append({'many_child_imports': [{
                'import_package': package,
                'import_names': [{'import_name': n} for n in named_imports],
            }]})

    # Could additionally properly sort the imports, but it seems fine.

    return ret


def sort_import_packages(src: Iterable[str]) -> List[str]:
    """Sorts the imports to prevent warnings from pylint."""

    def get_leading_dot_count(item: str) -> int:
        count = 0
        for i in item:
            if i != '.':
                break
            count += 1
        return count

    def compare(left: str, right: str) -> int:  # pylint:disable=too-many-return-statements
        if left == right:
            return 0

        # By local convention, 'typing' is always first.
        if left == 'typing':
            return -1
        if right == 'typing':
            return 1

        # relative imports shouldn't happen, but just in case,
        # they should be last, and ordered by number of leading dots.
        left_leading_dots = get_leading_dot_count(left)
        right_leading_dots = get_leading_dot_count(right)
        if left_leading_dots != right_leading_dots:
            # more should be later in the list, so 1 left vs 2 right means left is first.
            return left_leading_dots - right_leading_dots
        # Custom library items should be later than stdlib ones.
        # For our purposes, only 'petronia' libraries matter.
        left_has_petronia = left.startswith('petronia')
        right_has_petronia = right.startswith('petronia')
        if left_has_petronia and not right_has_petronia:
            return 1
        if not left_has_petronia and right_has_petronia:
            return -1
        # Both of the items are in the same category, so just sort them.
        if left < right:
            return -1
        # Already tested for equality, so the only remaining case is left > right
        return 1

    ret = list(src)
    ret.sort(key=functools.cmp_to_key(compare))
    return ret
