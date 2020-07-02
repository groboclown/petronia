
# mypy: allow-any-expr
# mypy: allow-any-explicit
# mypy: allow-any-generics

"""
Simplified access to the yaml library.
"""

from typing import Sequence, Iterable, Any, cast
from ..message import i18n as _
from ..error import StdRet

try:
    from yaml import safe_load_all, dump_all, YAMLError

    def load_yaml_documents(data_str: str) -> StdRet[Sequence[Any]]:
        # Note: this executes the generator to discover errors early.
        try:
            return StdRet.pass_ok(tuple(safe_load_all(data_str)))
        except YAMLError as e:
            return StdRet.pass_errmsg(_('Invalid YAML format: {e}'), e=repr(e))

    def dump_yaml_documents(documents: Sequence[Any]) -> StdRet[str]:
        try:
            return StdRet.pass_ok(cast(str, dump_all(documents)))  # types: ignore
        except (YAMLError, TypeError,) as e:
            return StdRet.pass_errmsg(_('Could not transform documents to YAML: {e}'), e=repr(e))

    YAML_SUPPORTED = True

except ModuleNotFoundError:  # pragma: no cover
    # unit testing will never reach this code, because unit test
    # requires a bunch of modules.

    print("You must install the PyYAML Python package to use this.")
    YAML_SUPPORTED = False

    # noinspection PyUnusedLocal
    def load_yaml_documents(data_str: str) -> Iterable[Any]:
        raise ValueError('yaml not supported.  Check YAML_SUPPORTED first.')

    # noinspection PyUnusedLocal
    def dump_yaml_documents(documents: Sequence[Any]) -> str:
        raise ValueError('yaml not supported.  Check YAML_SUPPORTED first.')
