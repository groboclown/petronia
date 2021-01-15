"""Finds the user configuration files."""

from typing import List
import os


def find_config_files(config_path: str) -> List[str]:
    """Find all the configuration files in the given configuration path."""
    ret: List[str] = []
    for item in config_path.split(os.pathsep):
        if not os.path.isdir(item):
            continue
        for fname in os.listdir(item):
            fqn = os.path.join(item, fname)
            if not os.path.isfile(fqn):
                continue
            fnl = fname.lower()
            if fnl in ('config.yaml', 'config.json'):
                ret.append(fqn)
                continue
            if fnl.startswith('ignore-'):
                continue
            if fnl.endswith('-config.yaml') or fnl.endswith('-config.json'):
                ret.append(fqn)
    return ret
