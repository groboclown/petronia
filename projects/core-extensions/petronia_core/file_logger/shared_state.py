"""Shared settings."""

from typing import Iterable, List, Dict, Any
import os
import sys
import datetime
import collections.abc
from petronia_common.util import StdRet, RET_OK_NONE, STRING_EMPTY_TUPLE
from petronia_common.util import i18n as _
from petronia_ext_lib.events import logging
from .state import file_logger
from ..user_messages import TRANSLATION_CATALOG


MESSAGE_TYPE_USER = '*user'
MESSAGE_TYPE_SYSTEM = '*system'
MESSAGE_TYPE_LOG = '*log'
STDOUT_FILENAME = '-'


class LogFile:
    """Configuration for a single log file.  "covers" should be either "user" or "system".
    This has no lock, because it's intended to be run from within a single-threaded
    event listener."""
    __slots__ = ('all_categories', 'one_categories', 'filename', 'format')

    def __init__(
            self, filename: str, categories: Iterable[str],
            format_str: str,
    ):
        self.all_categories = set(filter(lambda x: x.startswith('+'), categories))
        self.one_categories = set(filter(lambda x: not x.startswith('+'), categories))
        self.filename = filename
        self.format = format_str

    def write_message(
            self,
            source_id: str,
            categories: Iterable[str], messages: Iterable[logging.LocalizableMessage],
    ) -> None:
        """Write the message.  Message type must be in the covers group."""
        m_cat = set(categories)
        if self.all_categories and not m_cat.issuperset(self.all_categories):
            # m_cat does not contain all the required categories.
            return
        if self.one_categories and m_cat.isdisjoint(self.one_categories):
            # nothing in m_cat is in one_categories
            return

        message = ''
        now = datetime.datetime.now()
        for msg in messages:
            message += try_format(self.format, {
                'text': format_message(msg),
                'now': now,
                'source': source_id,
            }) + '\n'
        if self.filename == STDOUT_FILENAME:
            sys.stdout.write(message)
            sys.stdout.flush()
        else:
            # Opening the file on each write is excessive on I/O time, but it
            # prevents the file from keeping a persistent lock on some OSes.
            with open(self.filename, 'w+', encoding='utf-8') as f:
                f.write(message)


_LOGS: List[LogFile] = []


def clear_data() -> None:
    """Clear the shared state data."""
    _LOGS.clear()


def load_configuration(data_dirs: str, config: Dict[str, Any]) -> StdRet[None]:
    """Load the configuration data."""

    parsed_res = file_logger.ConfigurationState.parse_data(config)
    if parsed_res.has_error:
        return parsed_res.forward()

    for setting in parsed_res.result.files:
        fqn = os.path.basename(setting.filename)
        if fqn != STDOUT_FILENAME:
            # Only create the log directory if a log file is requested.
            # This should only be called once, but for now this is fine.
            log_dir_res = get_log_dir(data_dirs)
            if log_dir_res.has_error:
                return log_dir_res.forward()
            fqn = os.path.join(log_dir_res.result, fqn)
        _LOGS.append(LogFile(
            fqn, setting.categories or STRING_EMPTY_TUPLE, setting.message_format,
        ))

    return RET_OK_NONE


def write_error(source_id: str, message_type: str, error: logging.Error) -> None:
    """Write the message to the registered logs."""
    categories = {message_type, *error.categories}
    for log in _LOGS:
        log.write_message(source_id, categories, error.messages)


def write_messages(
        source_id: str, scope: str,
        messages: Iterable[logging.LocalizableMessage],
) -> None:
    """Write the message to the registered logs."""
    categories = {MESSAGE_TYPE_LOG, scope}
    for log in _LOGS:
        log.write_message(source_id, categories, messages)


def format_message(msg: logging.LocalizableMessage) -> str:
    """Convert the message into a string."""
    args: Dict[str, Any] = {}
    if not msg.arguments:
        return msg.message
    for arg in msg.arguments:
        name = arg.name
        value = arg.value.value
        if isinstance(value, (str, int, float, bool, datetime.datetime)):
            args[name] = value
        elif isinstance(value, collections.abc.Iterable):
            args[name] = ', '.join([str(v) for v in value])
        else:
            # something else.
            args[name] = repr(value)
    # Should look this up in the catalog, but this extension does not have
    # access to those.
    return try_format(msg.message, args)


def try_format(message: str, args: Dict[str, Any]) -> str:
    """Attempt to format the message."""
    try:
        return message.format(**args)
    except KeyError:
        # key not found in the message.
        return message + ' (' + repr(args) + ')'


def get_log_dir(data_dirs: str) -> StdRet[str]:
    """Get the log directory."""
    data_dir_list = data_dirs.split(os.pathsep)
    if not data_dir_list:
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG,
            _('Could not find a log directory from data path {data_dirs}'),
            data_dirs=data_dirs,
        )

    # Find a "user" directory to stick the logs into.
    # Otherwise, this can be non-deterministic.
    log_dir = os.path.join(data_dir_list[0], 'logs')
    try:
        os.makedirs(log_dir, exist_ok=True)
    except OSError as err:  # pragma no cover
        return StdRet.pass_exception(  # pragma no cover
            TRANSLATION_CATALOG,
            _('Failed to create log directory {log_dir}'),
            err,
            log_dir=log_dir,
        )
    return StdRet.pass_ok(log_dir)
