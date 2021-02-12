# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-11T17:55:54.986989+00:00

"""
Data structures and marshalling for extension petronia.core.protocol.logging version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods


from typing import (
    Any,
    Dict,
    List,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    collect_errors_from,
    not_none,
    STANDARD_PETRONIA_CATALOG,
    StdRet,
)

EXTENSION_NAME = 'petronia.core.protocol.logging'
EXTENSION_VERSION = (1, 0, 0)


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
