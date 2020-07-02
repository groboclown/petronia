
"""
YAML.

Correctly manages yaml library importing, and using safe document load and write.
"""

from .load_it import (
    YAML_SUPPORTED,
    load_yaml_documents,
    dump_yaml_documents,
)
