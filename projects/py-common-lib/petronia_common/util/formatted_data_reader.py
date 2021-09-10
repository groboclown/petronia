"""Helpers for reading formatted data."""

from typing import Sequence, Dict, Union, Any
import os
import json
import collections.abc
from .error import StdRet
from .yaml_support import load_yaml_documents
from .message import STANDARD_PETRONIA_CATALOG
from .message import i18n as _


StructuredFileData = Union[Sequence[Any], Dict[str, Any]]


def load_structured_file(filename: str) -> StdRet[StructuredFileData]:
    """Load a structured file."""
    if not os.path.isfile(filename):
        return StdRet.pass_errmsg(
            STANDARD_PETRONIA_CATALOG,
            _('no such file {filename}'),
            filename=filename,
        )
    f_lc = filename.lower()
    data: Any
    if f_lc.endswith('.json'):
        try:
            with open(filename, 'r', encoding='utf-8') as r_f:
                data = json.load(r_f)
        except (OSError, json.JSONDecodeError) as err:
            return StdRet.pass_exception(
                STANDARD_PETRONIA_CATALOG,
                _('failed reading json file {filename}'),
                err,
                filename=filename,
            )
    elif f_lc.endswith('.yaml') or f_lc.endswith('.yml'):
        try:
            with open(filename, 'r', encoding='utf-8') as r_f:
                res_data = load_yaml_documents(r_f.read())
        except OSError as err:
            return StdRet.pass_exception(
                STANDARD_PETRONIA_CATALOG,
                _('failed reading yaml file {filename}'),
                err,
                filename=filename,
            )
        if res_data.has_error:
            return res_data.forward()
        data = res_data.value
    else:
        return StdRet.pass_errmsg(
            STANDARD_PETRONIA_CATALOG,
            _('unknown structured file format: {filename}'),
            filename=filename,
        )
    return checked_formatted_data_type(filename, data)


def checked_formatted_data_type(filename: str, data: Any) -> StdRet[StructuredFileData]:
    """Ensure the formatted data is of the right type."""
    # Shouldn't be a string at the top level, which can be considered an iterable.
    if isinstance(data, str) or not isinstance(data, (dict, collections.abc.Iterable)):
        return StdRet.pass_errmsg(
            STANDARD_PETRONIA_CATALOG,
            _('structured file must contain a list or dictionary at the top level: {filename}'),
            filename=filename,
        )

    # This is more for MyPy purposes.
    if (
            isinstance(data, collections.abc.Iterable)
            and not isinstance(data, (dict, collections.abc.Sequence))
    ):
        data = tuple(data)  # pragma no cover

    return StdRet.pass_ok(data)
