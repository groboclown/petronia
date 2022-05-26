# GENERATED CODE - DO NOT MODIFY

"""
Data structures and marshalling for extension petronia_core.file_logger version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods,unused-import,invalid-name,consider-using-f-string

# Allow forward references and thus cyclic data types
from __future__ import annotations
from typing import (
    cast,
    Dict,
    Any,
    List,
    Optional,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    collect_errors_from,
    STANDARD_PETRONIA_CATALOG,
    not_none,
    StdRet,
)

EXTENSION_NAME = 'petronia_core.file_logger'
EXTENSION_VERSION = (1, 0, 0)


class LogfileSettings:
    """
    Settings for a single logfile.
    """
    __slots__ = ('filename', 'message_format', 'categories',)

    def __init__(
        self,
        filename: str,
        message_format: str,
        categories: Optional[List[str]],
    ) -> None:
        self.filename = filename
        self.message_format = message_format
        self.categories = categories

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'filename': self.filename,
            'message_format': self.message_format,
            'categories': None if self.categories is None else list(self.categories),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['LogfileSettings']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('filename')
        f_filename: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='filename',
                name='LogfileSettings',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='filename',
                    type='str',
                    name='LogfileSettings',
                )
            f_filename = val
        val = data.get('message_format')
        f_message_format: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='message_format',
                name='LogfileSettings',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='message_format',
                    type='str',
                    name='LogfileSettings',
                )
            f_message_format = val
        val = data.get('categories')
        f_categories: Optional[List[str]] = None
        if val is not None:
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='categories',
                    type='List[str]',
                    name='LogfileSettings',
                )
            f_categories = []
            for item in val:
                if not isinstance(item, str):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='categories',
                        type='str',
                        name='LogfileSettings',
                    )
                f_categories.append(item)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(LogfileSettings(
            filename=not_none(f_filename),
            message_format=not_none(f_message_format),
            categories=f_categories,
        ))

    def __repr__(self) -> str:
        return "LogfileSettings(" + repr(self.export_data()) + ")"


class ConfigurationState:
    """
    Configuration for the logger files.
    """
    __slots__ = ('files',)

    UNIQUE_TARGET_FQN = 'petronia_core.file_logger:configuration'
    UNIQUE_TARGET_REL = 'petronia_core.file_logger:configuration'

    def __init__(
        self,
        files: List[LogfileSettings],
    ) -> None:
        self.files = files

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'files': [v.export_data() for v in self.files],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ConfigurationState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('files')
        f_files: List[LogfileSettings]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='files',
                name='ConfigurationState',
            )
        else:
            f_files = []
            for item in val:
                parsed_files = LogfileSettings.parse_data(item)
                if parsed_files.has_error:
                    return parsed_files.forward()
                f_files.append(parsed_files.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ConfigurationState(
            files=not_none(f_files),
        ))

    def __repr__(self) -> str:
        return "ConfigurationState(" + repr(self.export_data()) + ")"


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
