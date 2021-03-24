
# mypy: allow-any-expr
# mypy: allow-any-explicit
# mypy: allow-any-generics

"""
Simplified access to the yaml library.
"""

from typing import Sequence, Any, cast
from ..message import i18n as _
from ..message import STANDARD_PETRONIA_CATALOG as STDC
from ..error import StdRet

try:
    from yaml import safe_load_all, dump_all, YAMLError

    def load_yaml_documents(data_str: str) -> StdRet[Sequence[Any]]:
        """Load 0 or more yaml documents from a single source, safely."""
        # Note: this executes the generator to discover errors early.
        try:
            return StdRet.pass_ok(tuple(safe_load_all(data_str)))
        except YAMLError as err:
            # Use str instead of repr, because it generates a cleaner result for end-users.
            return StdRet.pass_errmsg(STDC, _('Invalid YAML format: {e}'), e=str(err))

    def dump_yaml_documents(documents: Sequence[Any]) -> StdRet[str]:
        """Store zero or more simple structures as a yaml-formatted string."""
        try:
            return StdRet.pass_ok(cast(str, dump_all(documents)))  # types: ignore
        except (YAMLError, TypeError,) as err:
            return StdRet.pass_errmsg(
                STDC, _('Could not transform documents to YAML: {e}'),
                e=repr(err),
            )

    YAML_SUPPORTED = True

except ModuleNotFoundError:  # pragma: no cover
    # unit testing will never reach this code, because unit test
    # requires a bunch of modules.

    print("You must install the PyYAML Python package to use this.")
    YAML_SUPPORTED = False

    # noinspection PyUnusedLocal
    def load_yaml_documents(data_str: str) -> StdRet[Sequence[Any]]:
        """Load 0 or more yaml documents from a single source, safely."""
        raise ValueError('yaml not supported.  Check YAML_SUPPORTED first.')

    # noinspection PyUnusedLocal
    def dump_yaml_documents(documents: Sequence[Any]) -> StdRet[str]:
        """Store zero or more simple structures as a yaml-formatted string."""
        raise ValueError('yaml not supported.  Check YAML_SUPPORTED first.')
