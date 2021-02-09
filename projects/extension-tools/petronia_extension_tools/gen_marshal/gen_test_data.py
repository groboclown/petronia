
"""
Create the marshaller Python object source.
"""

from typing import Dict, List, Any
import random
from petronia_common.util import StdRet, tznow
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
from .template import load_template, templatize


DATA_SELECTOR_TEMPLATE = 'data_selector.mustache'
DATA_STRUCTURE_TEMPLATE = 'data_structure.mustache'
DATA_ARRAY_TEMPLATE = 'data_array.mustache'
_LOADED_TEMPLATES: Dict[str, str] = {}

MAX_DEPTH = 6
ABSOLUTE_MAX_DEPTH = 20
MAX_ARRAY_LENGTH = 10
MAX_STRING_LENGTH = 30


def create_field_data_sample(  # pylint: disable=R0911,R0912,R0914
        fdt: AbcEventDataType, fill_all_fields: bool, depth: int = 0,
) -> StdRet[str]:
    """Use a template to create sample data for the field value."""

    if depth > ABSOLUTE_MAX_DEPTH:
        raise RuntimeError('Data structure is too deep.')

    if isinstance(fdt, IntEventDataType):
        # This isn't cryptographically strong.  Which is fine for generating test data.
        return StdRet.pass_ok(repr(random.randint(fdt.min_value, fdt.max_value)))  # nosec

    if isinstance(fdt, FloatEventDataType):
        min_f_value = -100000.0
        max_f_value = 1000000.0
        if fdt.min_value is not None:
            min_f_value = min(fdt.min_value, max_f_value)
        if fdt.max_value is not None:
            max_f_value = max(min_f_value, fdt.max_value)
        return StdRet.pass_ok(repr(
            # This isn't cryptographically strong, which is fine for test data.
            (random.random() * (max_f_value - min_f_value)) + min_f_value  # nosec
        ))

    if isinstance(fdt, StringEventDataType):
        str_ret = ''
        if fill_all_fields:
            str_length = max(
                fdt.min_length,
                # This isn't cryptographically strong, which is fine for test data.
                min(MAX_STRING_LENGTH, random.randint(fdt.min_length, fdt.max_length)),  # nosec
            )
        else:
            str_length = fdt.min_length
        for _ in range(str_length):
            # This isn't cryptographically strong, which is fine for test data.
            str_ret += random.choice(CHARACTER_CHOICES)  # nosec
        return StdRet.pass_ok(repr(str_ret))

    if isinstance(fdt, BoolEventDataType):
        # This isn't cryptographically strong, which is fine for test data.
        return StdRet.pass_ok('True' if random.randint(0, 1) == 0 else 'False')  # nosec

    if isinstance(fdt, DatetimeEventDataType):
        return StdRet.pass_ok(repr(tznow().strftime(
            '%Y%m%d:%H%M%S.%f:%z',
        )))

    if isinstance(fdt, EnumEventDataType):
        # This isn't cryptographically strong, which is fine for test data.
        return StdRet.pass_ok(repr(random.choice(fdt.values)))  # nosec

    if isinstance(fdt, SelectorEventDataType):
        # This isn't cryptographically strong, which is fine for test data.
        selected_key, selected_type = random.choice(tuple(fdt.selector_items()))  # nosec
        data_value = create_field_data_sample(selected_type, fill_all_fields, depth + 1)
        if data_value.has_error:
            return data_value.forward()
        return run_template(
            DATA_SELECTOR_TEMPLATE,
            {
                'selector_name': repr(selected_key),
                'selector_value': data_value.result,
            },
            depth,
        )

    if isinstance(fdt, StructureEventDataType):
        fields: List[Dict[str, str]] = []
        for field_name, field_dt in fdt.fields():
            if field_dt.is_optional and depth > MAX_DEPTH:
                continue
            if fill_all_fields or not field_dt.is_optional:
                data_value = create_field_data_sample(
                    field_dt.data_type, fill_all_fields, depth + 1,
                )
                if data_value.has_error:
                    return data_value.forward()
                fields.append({'field_name': field_name, 'field_value': data_value.result})
        return run_template(
            DATA_STRUCTURE_TEMPLATE, {'fields': fields}, depth,
        )

    if isinstance(fdt, ArrayEventDataType):
        ret_val: List[str] = []
        if fill_all_fields and depth < MAX_DEPTH:
            length = max(
                fdt.min_length,
                # This isn't cryptographically strong, which is fine for test data.
                min(MAX_ARRAY_LENGTH, random.randint(fdt.min_length, fdt.max_length)),  # nosec
            )
        else:
            length = fdt.min_length
        for _ in range(length):
            data_value = create_field_data_sample(fdt.value_type, fill_all_fields, depth + 1)
            if data_value.has_error:
                return data_value.forward()
            ret_val.append(data_value.result)
        return run_template(
            DATA_ARRAY_TEMPLATE,
            {'values': [{'value': v} for v in ret_val]},
            depth,
        )

    raise Exception('Unknown field type ' + repr(fdt))  # pragma no cover


def run_template(template_name: str, data: Dict[str, Any], indent: int) -> StdRet[str]:
    """Run the template."""
    if template_name not in _LOADED_TEMPLATES:
        ret_template = load_template(template_name)
        if ret_template.has_error:
            return ret_template.forward()
        _LOADED_TEMPLATES[template_name] = ret_template.result
    raw = templatize(_LOADED_TEMPLATES[template_name], data)
    if indent == 0:
        # This is done because of the recursive templates; for the child templates,
        # the straight-up indention is fine, because they will be embedded in outer templates
        # which will themselves be indented.
        indent = 3
    str_indent = '    ' * indent
    ret = ''
    first = True
    for line in raw.splitlines(keepends=True):
        if first:
            first = False
        else:
            ret += str_indent
        ret += line
    return StdRet.pass_ok(ret.strip())


# This should be sufficient...
CHARACTER_CHOICES = ''
for __i in range(0x20, 0x2ff):
    CHARACTER_CHOICES += chr(__i)
for __i in range(0x370, 0x52f):
    CHARACTER_CHOICES += chr(__i)
