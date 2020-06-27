#! /usr/bin/python3

# mypy: allow-any-expr
# mypy: allow-any-generics
# mypy: allow-any-explicit

# See docs/patterns/extension-spec.yaml for details.

from typing import Dict, List, Sequence, Any
import os
import sys
import yaml


class ExtensionDef:
    def __init__(self, data: Dict[str, Any]) -> None:
        self._data = data


def load_extension_def(filename: str) -> ExtensionDef:
    with open(filename, 'r') as f:
        data = yaml.load(f)
        assert isinstance(data, dict)
        return ExtensionDef(data)


def create_event_boilerplate(ext: ExtensionDef) -> str:
    pass


def create_state_boilerplate(ext: ExtensionDef) -> str:
    pass


def create_bootstrap_boilerplate(ext: ExtensionDef) -> str:
    pass


def create_extension_files(extension_def_file: str) -> None:
    root_dir = os.path.dirname(extension_def_file)
    ext = load_extension_def(extension_def_file)
    with open(os.path.join(root_dir, 'bootstrap_boilerplate.py'), 'w') as f:
        f.write(create_bootstrap_boilerplate(ext))
    with open(os.path.join(root_dir, 'events_boilerplate.py'), 'w') as f:
        f.write(create_event_boilerplate(ext))
    with open(os.path.join(root_dir, 'state_boilerplate.py'), 'w') as f:
        f.write(create_state_boilerplate(ext))


def main(args: Sequence[str]) -> int:
    for arg in args:
        create_extension_files(arg)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
