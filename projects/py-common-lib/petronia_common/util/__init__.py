
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
)

from .error import (
    StdRet,
    error_message,
    join_errors,
    possible_error,
    PetroniaReturnError,
)

from . import validation
from .validation import (
    assert_that,
    enforce_that,
)

from . import yaml_support
from .yaml_support import load_yaml_documents, dump_yaml_documents, YAML_SUPPORTED
