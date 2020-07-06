
"""
Loads extension information from a simple data structure.

Simple data structures means list, dict, int, float, bool, str, None
"""

from typing import List, Dict, Optional, Any, cast
from . import event_schema
from ...util import StdRet, collect_errors_from
from ...util import i18n as _


def load_full_event_schema(
        raw_event_schemas: Dict[str, Any],
        references: Dict[str, Any],
) -> StdRet[List[event_schema.EventType]]:
    partial_parsed_references: Dict[str, event_schema.AbcEventDataType] = {}
    for reference_name, raw_reference in references.items():
        if not isinstance(raw_reference, dict):
            return StdRet.pass_errmsg(
                _('references must be a dictionary of event data type dictionaries'),
            )
        ret_reference = load_event_data_type(raw_reference)
        if not ret_reference.ok:
            return ret_reference.forward()
        partial_parsed_references[reference_name] = ret_reference.result
    ret_parsed_references = update_references(partial_parsed_references)
    if not ret_parsed_references.ok:
        return ret_parsed_references.forward()
    parsed_references = ret_parsed_references.result
    ret: List[event_schema.EventType] = []
    for event_name, raw_event in raw_event_schemas.items():
        if not isinstance(raw_event, dict):
            return StdRet.pass_errmsg(
                _('event schemas must be dictionaries'),
            )
        ret_event = load_event_schema(event_name, raw_event, parsed_references)
        if not ret_event.ok:
            return ret_event.forward()
        ret.append(ret_event.result)
    return StdRet.pass_ok(ret)


def load_event_schema(
        event_name: str,
        raw: Dict[str, Any],
        references: Dict[str, event_schema.AbcEventDataType],
) -> StdRet[event_schema.EventType]:
    # Note: must perform update_reference!
    # Note: must not perform type validation!
    ret_priority = load_event_str_value('priority', raw)
    ret_send_access = load_event_str_value('send-access', raw)
    ret_receive_access = load_event_str_value('receive-access', raw)
    ret_data_type = load_event_structure_data_type(raw)
    error = collect_errors_from(
        ret_priority, ret_send_access, ret_receive_access, ret_data_type,
    )
    if error:
        return StdRet.pass_error(error)
    ret_data_type_resolved = update_reference(ret_data_type.result, references, [])
    if not ret_data_type_resolved.ok:
        return ret_data_type_resolved.forward()
    data_type = ret_data_type_resolved.result
    if not isinstance(data_type, event_schema.StructureEventDataType):
        # This is an internal error...
        raise RuntimeError(  # pragma no cover
            f'Incorrectly re-formatted structure to {ret_data_type_resolved.result}'
        )
    if ret_priority.result not in ("high", "user", "normal", "io"):
        return StdRet.pass_errmsg(
            _('`{priority}` must be a valid priority'),
            priority=ret_priority.result,
        )
    priority = cast(event_schema.EventPriorityType, ret_priority.result)
    if ret_send_access.result not in ("public", "implementations"):
        return StdRet.pass_errmsg(
            _('`{send_access}` must be a valid access'),
            send_access=ret_send_access.result,
        )
    send_access = cast(event_schema.EventAccessType, ret_send_access.result)
    if ret_receive_access.result not in ("public", "implementations"):
        return StdRet.pass_errmsg(
            _('`{receive_access}` must be a valid access'),
            receive_access=ret_receive_access.result,
        )
    receive_access = cast(event_schema.EventAccessType, ret_receive_access.result)
    return StdRet.pass_ok(event_schema.EventType(
        name=event_name, priority=priority,
        send_access=send_access, receive_access=receive_access,
        structure=data_type,
    ))


def update_references(
        refs: Dict[str, event_schema.AbcEventDataType],
) -> StdRet[Dict[str, event_schema.AbcEventDataType]]:
    """
    Replaces all "reference" types with the actual value.

    :param refs:
    :return:
    """
    for ref, data_type in refs.items():
        ret_updated = update_reference(data_type, refs, [])
        if not ret_updated.ok:
            return ret_updated.forward()
        refs[ref] = ret_updated.result
    return StdRet.pass_ok(refs)


MAX_REFERENCE_DEPTH = 20


def update_reference(
        data_type: event_schema.AbcEventDataType,
        refs: Dict[str, event_schema.AbcEventDataType],
        reference_depth: List[str],
) -> StdRet[event_schema.AbcEventDataType]:
    if isinstance(data_type, event_schema.ArrayEventDataType):
        ret_internal = update_reference(data_type.value_type, refs, reference_depth)
        if not ret_internal.ok:
            return ret_internal
        if ret_internal.result is not data_type.value_type:
            return StdRet.pass_ok(event_schema.ArrayEventDataType(
                data_type.description, ret_internal.result,
                data_type.min_length, data_type.max_length,
            ))
        # No replacement needed.
        return StdRet.pass_ok(data_type)
    if isinstance(data_type, event_schema.StructureEventDataType):
        new_fields: Dict[str, event_schema.StructureFieldType] = {}
        changed = False
        for key, value in data_type.fields():
            ret_internal = update_reference(value.data_type, refs, reference_depth)
            if not ret_internal.ok:
                return ret_internal
            if ret_internal.result is not value.data_type:
                changed = True
                new_fields[key] = event_schema.StructureFieldType(ret_internal.result, value.is_optional)
            else:
                new_fields[key] = value
        if changed:
            return StdRet.pass_ok(event_schema.StructureEventDataType(
                data_type.description, new_fields,
            ))
        # No replacement needed.
        return StdRet.pass_ok(data_type)
    if isinstance(data_type, event_schema.SelectorEventDataType):
        selector_types: Dict[str, event_schema.AbcEventDataType] = {}
        changed = False
        for key, selector_type in data_type.selector_items():
            ret_internal = update_reference(selector_type, refs, reference_depth)
            if not ret_internal.ok:
                return ret_internal
            if ret_internal.result is not selector_type:
                changed = True
                selector_types[key] = ret_internal.result
            else:
                selector_types[key] = selector_type
        if changed:
            return StdRet.pass_ok(event_schema.SelectorEventDataType(
                data_type.description, selector_types,
            ))
        # No replacement needed
        return StdRet.pass_ok(data_type)
    if isinstance(data_type, event_schema.ReferenceEventDataType):
        if data_type.reference in reference_depth:
            return StdRet.pass_errmsg(
                _('cyclic reference `{reference}`'),
                reference=data_type.reference,
            )
        replacement = refs.get(data_type.reference)
        if not replacement:
            return StdRet.pass_errmsg(
                _('unknown reference `{reference}`'),
                reference=data_type.reference,
            )
        new_depth = [*reference_depth, data_type.reference]
        if len(new_depth) > MAX_REFERENCE_DEPTH:
            return StdRet.pass_errmsg(
                _('reference depth too deep ({depth})'),
                depth=reference_depth,
            )
        ret_internal = update_reference(replacement, refs, new_depth)
        if not ret_internal.ok:
            return ret_internal
        refs[data_type.reference] = ret_internal.result
        return ret_internal

    # It's not a reference-able object
    return StdRet.pass_ok(data_type)


def load_event_data_type(raw: Dict[str, Any]) -> StdRet[event_schema.AbcEventDataType]:
    data_type = raw.get('type')
    if data_type == 'string':
        return load_event_string_data_type(raw)
    if data_type == 'int':
        return load_event_int_data_type(raw)
    if data_type == 'float':
        return load_event_float_data_type(raw)
    if data_type == 'bool':
        return load_event_bool_data_type(raw)
    if data_type == 'enum':
        return load_event_enum_data_type(raw)
    if data_type == 'datetime':
        return load_event_datetime_data_type(raw)
    if data_type == 'array':
        return load_event_array_data_type(raw)
    if data_type == 'structure':
        return load_event_structure_data_type(raw)
    if data_type == 'selector':
        return load_event_selector_data_type(raw)
    if data_type == 'reference':
        return load_event_reference_data_type(raw)
    return StdRet.pass_errmsg(
        _('unknown data type `{data_type}`'),
        data_type=data_type,
    )


def load_event_string_data_type(raw: Dict[str, Any]) -> StdRet[event_schema.StringEventDataType]:
    ret_description = load_event_optional_str_value('description', raw)
    ret_max_length = load_event_numeric_val_with_default(
        'max-length', raw, event_schema.DEFAULT_MAX_STRING_LENGTH,
    )
    ret_min_length = load_event_numeric_val_with_default(
        'min-length', raw, event_schema.DEFAULT_MIN_STRING_LENGTH,
    )
    error = collect_errors_from(
        ret_description, ret_max_length, ret_min_length,
    )
    if error:
        return StdRet.pass_error(error)
    return StdRet.pass_ok(event_schema.StringEventDataType(
        ret_description.value, ret_min_length.result, ret_max_length.result,
    ))


def load_event_int_data_type(raw: Dict[str, Any]) -> StdRet[event_schema.IntEventDataType]:
    ret_description = load_event_optional_str_value('description', raw)
    ret_max_value = load_event_numeric_val_with_default(
        'max-value', raw, event_schema.DEFAULT_MAX_INT_VALUE,
    )
    ret_min_value = load_event_numeric_val_with_default(
        'min-value', raw, event_schema.DEFAULT_MIN_INT_VALUE,
    )
    error = collect_errors_from(
        ret_description, ret_max_value, ret_min_value,
    )
    if error:
        return StdRet.pass_error(error)
    return StdRet.pass_ok(event_schema.IntEventDataType(
        ret_description.value, ret_min_value.result, ret_max_value.result,
    ))


def load_event_float_data_type(raw: Dict[str, Any]) -> StdRet[event_schema.FloatEventDataType]:
    ret_description = load_event_optional_str_value('description', raw)
    ret_max_value = load_event_optional_numeric_val('max-value', raw)
    ret_min_value = load_event_optional_numeric_val('min-value', raw)
    error = collect_errors_from(
        ret_description, ret_max_value, ret_min_value,
    )
    if error:
        return StdRet.pass_error(error)
    return StdRet.pass_ok(event_schema.FloatEventDataType(
        ret_description.value, ret_min_value.value, ret_max_value.value,
    ))


def load_event_bool_data_type(raw: Dict[str, Any]) -> StdRet[event_schema.BoolEventDataType]:
    ret_description = load_event_type_description(raw)
    error = collect_errors_from(ret_description)
    if error:
        return StdRet.pass_error(error)
    return StdRet.pass_ok(event_schema.BoolEventDataType(ret_description.value))


def load_event_enum_data_type(raw: Dict[str, Any]) -> StdRet[event_schema.EnumEventDataType]:
    ret_description = load_event_type_description(raw)
    if not ret_description.ok:
        return ret_description.forward()
    raw_values = raw.get('values')
    values: List[str] = []
    if raw_values and not isinstance(raw_values, list):
        return StdRet.pass_errmsg(
            _('enum values must be a list of strings'),
        )
    if raw_values:
        for raw_value in raw_values:
            if not isinstance(raw_value, str):
                return StdRet.pass_errmsg(
                    _('enum values must be a list of strings'),
                )
            values.append(raw_value)
    return StdRet.pass_ok(event_schema.EnumEventDataType(
        ret_description.value, values,
    ))


def load_event_datetime_data_type(raw: Dict[str, Any]) -> StdRet[event_schema.DatetimeEventDataType]:
    ret_description = load_event_type_description(raw)
    error = collect_errors_from(ret_description)
    if error:
        return StdRet.pass_error(error)
    return StdRet.pass_ok(event_schema.DatetimeEventDataType(ret_description.value))


def load_event_array_data_type(raw: Dict[str, Any]) -> StdRet[event_schema.ArrayEventDataType]:
    ret_description = load_event_type_description(raw)
    ret_max_length = load_event_numeric_val_with_default(
        'max-length', raw, event_schema.DEFAULT_MAX_ARRAY_LENGTH,
    )
    ret_min_length = load_event_numeric_val_with_default(
        'min-length', raw, event_schema.DEFAULT_MIN_ARRAY_LENGTH,
    )
    raw_data_type = raw.get('value-type')
    if not isinstance(raw_data_type, dict):
        return StdRet.pass_errmsg(
            _('`value-type` must be a dictionary of a data type structure')
        )
    ret_data_type = load_event_data_type(raw_data_type)
    error = collect_errors_from(
        ret_description, ret_max_length, ret_min_length, ret_data_type,
    )
    if error:
        return StdRet.pass_error(error)
    return StdRet.pass_ok(event_schema.ArrayEventDataType(
        ret_description.value, ret_data_type.result, ret_min_length.result, ret_max_length.result,
    ))


def load_event_structure_data_type(raw: Dict[str, Any]) -> StdRet[event_schema.StructureEventDataType]:
    ret_description = load_event_type_description(raw)
    if not ret_description.ok:
        return ret_description.forward()
    raw_fields = raw.get('fields')
    if not isinstance(raw_fields, dict):
        return StdRet.pass_errmsg(
            _('`fields` must be a dictionary of field data type structures')
        )
    fields: Dict[str, event_schema.StructureFieldType] = {}
    for field_name, raw_field in raw_fields.items():
        raw_optional = raw_field.get('optional')
        if raw_optional is None:
            optional = False
        elif not isinstance(raw_optional, bool):
            return StdRet.pass_errmsg(
                _('`optional` must be `true` or `false`')
            )
        else:
            optional = raw_optional
        ret_field_data_type = load_event_data_type(raw_field)
        if not ret_field_data_type.ok:
            return ret_field_data_type.forward()
        fields[field_name] = event_schema.StructureFieldType(ret_field_data_type.result, optional)
    return StdRet.pass_ok(event_schema.StructureEventDataType(
        ret_description.value, fields,
    ))


def load_event_selector_data_type(raw: Dict[str, Any]) -> StdRet[event_schema.SelectorEventDataType]:
    ret_description = load_event_optional_str_value('description', raw)
    if not ret_description.ok:
        return ret_description.forward()
    raw_type_mapping = raw.get('type-mapping')
    if not isinstance(raw_type_mapping, dict):
        return StdRet.pass_errmsg(
            _('`type-mapping` must be a dictionary of data type structures'),
        )
    mapping: Dict[str, event_schema.AbcEventDataType] = {}
    for key, raw_type in raw_type_mapping.items():
        if not isinstance(raw_type, dict):
            return StdRet.pass_errmsg(
                _('`type-mapping` must be a dictionary of data type structures'),
            )
        ret_type = load_event_data_type(raw_type)
        if not ret_type.ok:
            return ret_type.forward()
        mapping[key] = ret_type.result
    return StdRet.pass_ok(event_schema.SelectorEventDataType(
        ret_description.value, mapping,
    ))


def load_event_reference_data_type(raw: Dict[str, Any]) -> StdRet[event_schema.ReferenceEventDataType]:
    ret_description = load_event_optional_str_value('description', raw)
    ret_ref = load_event_str_value('ref', raw)
    error = collect_errors_from(ret_description, ret_ref)
    if error:
        return StdRet.pass_error(error)
    return StdRet.pass_ok(event_schema.ReferenceEventDataType(
        ret_description.value, ret_ref.result,
    ))


def load_event_type_description(raw: Dict[str, Any]) -> StdRet[Optional[str]]:
    return load_event_optional_str_value('description', raw)


def load_event_str_value(key: str, raw: Dict[str, Any]) -> StdRet[str]:
    raw_value = raw.get(key)
    if not raw_value:
        return StdRet.pass_errmsg(
            _('no `{key}` found in event definition'),
            key=key,
        )
    if not isinstance(raw_value, str):
        return StdRet.pass_errmsg(
            _('`{key}` must be a string value'),
            key=key,
        )
    return StdRet.pass_ok(raw_value)


def load_event_optional_str_value(key: str, raw: Dict[str, Any]) -> StdRet[Optional[str]]:
    raw_value = raw.get(key)
    if not raw_value:
        return StdRet.pass_ok(None)
    if not isinstance(raw_value, str):
        return StdRet.pass_errmsg(
            _('`{key}` must be a string value'),
            key=key,
        )
    return StdRet.pass_ok(raw_value)


def load_event_numeric_val_with_default(key: str, raw: Dict[str, Any], default: float) -> StdRet[float]:
    raw_value = raw.get(key)
    if not raw_value:
        return StdRet.pass_ok(default)
    if isinstance(raw_value, (int, float)):
        return StdRet.pass_ok(float(raw_value))
    return StdRet.pass_errmsg(
        _('`{key}` must be a number'),
        key=key,
    )


def load_event_optional_numeric_val(key: str, raw: Dict[str, Any]) -> StdRet[Optional[float]]:
    raw_value = raw.get(key)
    if not raw_value:
        return StdRet.pass_ok(None)
    if isinstance(raw_value, (int, float)):
        return StdRet.pass_ok(float(raw_value))
    return StdRet.pass_errmsg(
        _('`{key}` must be a number'),
        key=key,
    )
