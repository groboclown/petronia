# GENERATED CODE - DO NOT MODIFY

"""
Data structures and marshalling for extension petronia_core.datastore version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods,unused-import,invalid-name,consider-using-f-string

# Allow forward references and thus cyclic data types
from __future__ import annotations
from typing import (
    Any,
    List,
    Dict,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    not_none,
    STANDARD_PETRONIA_CATALOG,
    collect_errors_from,
    StdRet,
)

EXTENSION_NAME = 'petronia_core.datastore'
EXTENSION_VERSION = (1, 0, 0)


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
