

from typing import Mapping, Dict, List, Iterable
from typing import cast as t_cast
from time import struct_time, strftime

from ....aid.std import (
    TRACE, DEBUG, VERBOSE, INFO, NOTICE, WARN, DEPRECATED, ERROR, FATAL,
    LogLevel, readonly_dict,
    ErrorReport,
    ResultWithErrors,
    create_user_error,
    EMPTY_TUPLE,
)
from ....aid.std import i18n as _
from ....base.util.simple_type import (
    PersistType,
    PersistTypeSchemaItem,
    readonly_persistent_schema_copy,
    PERSISTENT_TYPE_SCHEMA_TYPE__STR,
    collect_errors,
    with_key_as_list,
    optional_str,
)

LEVEL_NAME_MAP: Mapping[str, LogLevel] = readonly_dict({
    'trace': TRACE,
    'debug': DEBUG,
    'dbg': DEBUG,
    'verbose': VERBOSE,
    'info': INFO,
    'inform': INFO,
    'informative': INFO,
    'notice': NOTICE,
    'note': NOTICE,
    'warn': WARN,
    'warning': WARN,
    'dep': DEPRECATED,
    'deprecated': DEPRECATED,
    'deprecation': DEPRECATED,
    'err': ERROR,
    'error': ERROR,
    'fatal': FATAL,
    'die': FATAL,
})

FULL_LEVEL_NAME_UPPER: Mapping[int, str] = readonly_dict({
    int(TRACE): 'TRACE',
    int(DEBUG): 'DEBUG',
    int(VERBOSE): 'VERBOSE',
    int(INFO): 'INFO',
    int(NOTICE): 'NOTICE',
    int(WARN): 'WARN',
    int(DEPRECATED): 'DEPRECATED',
    int(ERROR): 'ERROR',
    int(FATAL): 'FATAL',
})

LEVEL_NAME_5_UPPER: Mapping[int, str] = readonly_dict({
    int(TRACE): 'TRACE',
    int(DEBUG): 'DEBUG',
    int(VERBOSE): 'VRBSE',
    int(INFO): " INFO",
    int(NOTICE): " NOTE",
    int(WARN): ' WARN',
    int(DEPRECATED): 'DEPR',
    int(ERROR): 'ERROR',
    int(FATAL): 'FATAL',
})

DEFAULT_FORMAT = '[{LEVEL}] {msg}'
DEFAULT_CONTINUATION_FORMAT = '        {msg}'


class FileLoggerConfig:
    """
    Configures how the logging is generated.
    """

    __slots__ = (
        '__file',
        '__format',
        '__cont_format',
        '__category_levels',
    )

    def __init__(
            self, filename: str,
            log_format: str, continuation_format: str,
            category_log_levels: Mapping[str, str]
    ) -> None:
        self.__file = filename
        self.__format = log_format
        self.__cont_format = continuation_format
        self.__category_levels = readonly_dict(category_log_levels)

    @property
    def filename(self) -> str:
        return self.__file

    @property
    def category_log_levels(self) -> Mapping[str, str]:
        return self.__category_levels

    @property
    def log_format(self) -> str:
        return self.__format

    @property
    def continuation_format(self) -> str:
        return self.__cont_format

    def get_category_levels(self) -> Mapping[str, LogLevel]:
        ret: Dict[str, LogLevel] = {}
        for cat, level in self.__category_levels.items():
            log_level = LEVEL_NAME_MAP.get(level.lower().strip(), WARN)
            ret[cat] = log_level
        return ret

    def format_message(self, when: struct_time, level: LogLevel, src: str, formatted_message: str) -> str:
        return '\n'.join([
            strftime(self.__format.format(
                LEVEL=LEVEL_NAME_5_UPPER[level],
                LONG_LEVEL=FULL_LEVEL_NAME_UPPER[level],
                level=LEVEL_NAME_5_UPPER[level].lower(),
                long_level=FULL_LEVEL_NAME_UPPER[level].lower(),
                src=src,
                msg=line
            ), when)
            for line in formatted_message.splitlines()
        ])

    def __repr__(self) -> str:
        return (
            "FileLoggerConfig(filename={0}, log_format={1}, continuation_format={2}, category_log_levels={3})"
        ).format(
            repr(self.__file), repr(self.__format), repr(self.__cont_format), repr(self.__category_levels)
        )


LOGGER_SCHEMA = readonly_persistent_schema_copy({
    'filename': PersistTypeSchemaItem(
        "File path to write the log to, or '-' to send to stdout.",
        PERSISTENT_TYPE_SCHEMA_TYPE__STR
    ),
    'format': PersistTypeSchemaItem(
        """Log line output format.
        
        The format allows for these symbols:
            * `{LEVEL}`: 5 letters of the log level, in upper-case.
            * `{LONG_LEVEL}`: the full log level name, in upper-case.
            * `{level}`: 5 letters of hte log level, in lower-case. 
            * `{long_level}`: the full log level name, in upper-case.
            * `{src}`: the source of the message.
            * `{msg}`: the logged message.
        
        If date or time is required, use
        https://docs.python.org/3/library/time.html#time.strftime
        for the formatting of the time when the log was recorded.
        """,
        PERSISTENT_TYPE_SCHEMA_TYPE__STR
    ),
    'continuation': PersistTypeSchemaItem(
        'Format for when a message continues over several lines.  It follows the same formatting rules as "format"',
        PERSISTENT_TYPE_SCHEMA_TYPE__STR
    ),
    'default': PersistTypeSchemaItem(
        "Default logging level for everything.  If a message does not match a category, then this log level is used.",
        PERSISTENT_TYPE_SCHEMA_TYPE__STR
    ),
    'category-levels': [{
        'category': PersistTypeSchemaItem(
            "Name of the category level to log.",
            PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
        'cat': PersistTypeSchemaItem(
            "Name of the category level to log.",
            PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
        'level': PersistTypeSchemaItem(
            "Lowest log level to allow reporting for this category.",
            PERSISTENT_TYPE_SCHEMA_TYPE__STR
        ),
    }],
})


def parse_config(data: PersistType) -> ResultWithErrors[FileLoggerConfig]:
    errors: List[ErrorReport] = []
    category_levels: Dict[str, str] = {
        # Default level
        '': collect_errors(errors, optional_str(
            data, 'default',
            lambda: create_user_error(parse_config, _('`default` must be a string'))
        )) or 'warn',
    }
    filename = collect_errors(errors, optional_str(
        data, 'filename',
        lambda: create_user_error(parse_config, _('`filename` must be a string'))
    )) or '-'
    log_format = collect_errors(errors, optional_str(
        data, 'format',
        lambda: create_user_error(parse_config, _('`format` must be a string'))
    )) or DEFAULT_FORMAT
    continue_format = collect_errors(errors, optional_str(
        data, 'continuation',
        lambda: create_user_error(parse_config, _('`continuation` must be a string'))
    )) or DEFAULT_CONTINUATION_FORMAT

    raw_categories = collect_errors(errors, with_key_as_list(
        data, 'category-levels',
        lambda: create_user_error(parse_config, _('`category-levels` must be a list of key/values'))
    )) or t_cast(Iterable[Mapping[str, str]], EMPTY_TUPLE)
    for raw_category in raw_categories:
        cat = collect_errors(errors, optional_str(
            raw_category, 'category',
            lambda: create_user_error(parse_config, _('`category` must be a string'))
        )) or collect_errors(errors, optional_str(
            raw_category, 'cat',
            lambda: create_user_error(parse_config, _('`cat` must be a string'))
        ))
        if cat:
            level = collect_errors(errors, optional_str(
                raw_category, 'level',
                lambda: create_user_error(parse_config, _('`level` must be a string'))
            )) or 'warn'
            category_levels[cat] = level
    return FileLoggerConfig(filename, log_format, continue_format, category_levels), errors
