
"""
YAML.

The old Petronia included a copy of PyYAML, but that was really old.
May want to continue including a really old version that has just
simple yaml support.  But PyYAML is really good...
"""

from .load_it import (
    YAML_SUPPORTED,
    load_yaml_documents,
    dump_yaml_documents,
)
