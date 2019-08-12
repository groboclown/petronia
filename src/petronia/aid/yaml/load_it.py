
# mypy: allow-any-expr
# mypy: allow-any-explicit
# mypy: allow-any-generics

"""
Simplified access to the yaml library.
"""

from typing import Sequence, Iterable, Any, cast

try:
    from yaml import safe_load_all, dump_all

    def load_yaml_documents(data_str: str) -> Iterable[Any]:
        return safe_load_all(data_str)

    def dump_yaml_documents(documents: Sequence[Any]) -> str:
        return cast(str, dump_all(documents)) # types: ignore

    YAML_SUPPORTED = True
except ModuleNotFoundError:
    print("You must install the PyYAML Python package to use this.")
    YAML_SUPPORTED = False

    def load_yaml_documents(data_str: str) -> Iterable[Any]:
        raise ValueError('yaml not supported.  Check YAML_SUPPORTED first.')

    def dump_yaml_documents(documents: Sequence[Any]) -> str:
        raise ValueError('yaml not supported.  Check YAML_SUPPORTED first.')
