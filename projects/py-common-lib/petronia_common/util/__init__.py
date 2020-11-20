
"""
Common Petronia utilities.
"""

from .memory import (
    DelayedValueHolder,
    ValueHolder,
    STRING_EMPTY_TUPLE,
    EMPTY_MAPPING,
    EMPTY_TUPLE,
    EMPTY_DICT,
    EMPTY_LIST,
    readonly_dict,
    T, K, V,
)

from .message import (
    i18n,
    I18n,
    UserMessage,
    UserMessageData,
    SimpleUserMessageData,
    STANDARD_PETRONIA_CATALOG,
)

from .error import (
    StdRet,
    error_message,
    join_errors,
    join_results,
    possible_error,
    collect_errors_from,
    PetroniaReturnError,
    RET_OK_NONE,
    RET_OK_TRUE,
    RET_OK_FALSE,
)

from . import validation
from .validation import (
    enforce_that,
    enforce_all,
)

from . import yaml_support
from .yaml_support import load_yaml_documents, dump_yaml_documents, YAML_SUPPORTED

from . import type_support
from .type_support import without_none

from . import aio
