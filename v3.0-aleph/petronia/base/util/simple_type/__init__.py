
"""
A type system for storing JSON-like simple data.
"""

from .defs import (
    PersistType,
    PersistTypeSchema,
    PersistTypeSchemaItem,
    PERSISTENT_TYPE_SCHEMA_TYPE__STR,
    PERSISTENT_TYPE_SCHEMA_TYPE__FLOAT,
    PERSISTENT_TYPE_SCHEMA_TYPE__BOOL,
    PERSISTENT_TYPE_SCHEMA_TYPE__ANY,
    PERSISTENT_TYPE_SCHEMA_TYPE__REF,
    PERSISTENT_TYPE_SCHEMA_TYPE__ID,
    PERSISTENT_TYPE_SCHEMA_NAME__SCHEMA,
    PERSISTENT_TYPE_SCHEMA_NAME__DOC,
)
from .copy import (
    readonly_persistent_copy,
    readonly_persistent_schema_copy,
)
from .parse import (
    collect_errors,
    as_persist,
    required_dict,
    with_key_as_dict,
    with_key_as_list,
    is_key_true,
    is_key_false,
    list_of_maps,
    optional_bool,
    optional_float,
    optional_str,
    optional_int,
    NO_ERRORS,
)

EMPTY_PERSISTENT_SCHEMA = readonly_persistent_schema_copy({})
EMPTY_PERSISTENT_DATA = readonly_persistent_copy({})
