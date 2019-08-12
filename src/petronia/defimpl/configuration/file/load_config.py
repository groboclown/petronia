
# mypy: allow-any-expr

"""
Load a configuration file.
"""

from typing import Sequence
import json
from .contents import (
    ExtensionConfigurationDetails,
    deserialize_contents,
)
from ....aid.yaml import (
    YAML_SUPPORTED,
    load_yaml_documents,
)


def load_config_file(
        filename: str
) -> Sequence[ExtensionConfigurationDetails]:
    """Load the configuration file, if it's in the supported format."""
    if filename.endswith('.json'):
        with open(filename, 'r') as inp:
            val = json.load(inp)
            return deserialize_contents(val, filename)
    if filename.endswith('.yaml') or filename.endswith('.yml'):
        if YAML_SUPPORTED:
            with open(filename, 'r') as inp:
                val = load_yaml_documents(inp.read())
                return deserialize_contents(val, filename)
        return (
            ExtensionConfigurationDetails(
                filename, '(file format)',
                err='yaml file format not supported; please install PyYAML to use it.'
            ),
        )
    # Don't use the file.
    return ()
