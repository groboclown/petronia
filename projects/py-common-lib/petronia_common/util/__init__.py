
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
    T, K, V, T_co,
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

from . import formatted_data_reader
from .formatted_data_reader import load_structured_file

from . import type_support
from .type_support import without_none, not_none

from . import aio

from . import input_buffer
from .input_buffer import StreamedBinaryReader, StreamReadState, select_reader, single_reader_loop
