
"""
Helpers for extensions internal to Petronia.
"""

from typing import Dict
from typing import cast as t_cast
from ...base.bus import (
    ExtensionMetadataStruct,
)
from ..util.memory import readonly_dict


def petronia_extension(base: Dict[str, object]) -> ExtensionMetadataStruct:
    if 'version' not in base or 'name' not in base:
        raise ValueError('built-in extensions need to define the name and version.')
    # This is one version.  It's long, intensive, and only necessary when developing
    # the extension.  It's better placed in something else, like a unit test or the mk_docs.py file.
    # ret: Dict[str, Any] = {
    #     "license": ("MIT",),
    #     "authors": ("Petronia",),
    # }
    # for key, val in base.items():
    #     if key in ('name',):
    #         assert isinstance(val, str) and val
    #         ret['name'] = val
    #     elif key in ('version',):
    #         assert isinstance(val, tuple) and len(val) == 3
    #         ret['version'] = val
    #     elif key in ('type',):
    #         assert isinstance(val, str) and val in ('api', 'impl', 'standalone',)
    #         ret['type'] = val
    #     elif key in ('depends',):
    #         assert isinstance(val, Iterable)
    #         deps: List[Dict[str, Any]] = []
    #         for dep in val:
    #             assert isinstance(deps, Mapping) and 'extension' in deps and 'minimum' in deps
    #             rdep: Dict[str, Any] = {
    #                 'extension': deps['extension']
    #             }

    base['license'] = 'MIT'
    base['authors'] = ('Petronia',)

    return t_cast(ExtensionMetadataStruct, readonly_dict(base))
