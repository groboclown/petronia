
"""
Loads the extension documentation.
"""

from typing import List, Sequence
import json
import collections
from petronia_common.util import load_yaml_documents, StdRet, join_results
from petronia_common.util import i18n as _
from petronia_common.extension.config import AbcExtensionMetadata
from petronia_common.extension.config.extension_loader import load_extension


def load_extension_file(filename: str) -> StdRet[Sequence[AbcExtensionMetadata]]:
    """Load the metadata from the extension file."""
    if filename.lower().endswith('.json'):
        with open(filename, 'r') as f:
            ret_data = json.load(f)
    elif filename.lower().endswith('.yaml') or filename.lower().endswith('.yml'):
        with open(filename, 'r') as f:
            ret_data = load_yaml_documents(f.read())
    else:
        return StdRet.pass_errmsg(_('Invalid extension metadata file type: {name}'), name=filename)
    if ret_data.has_error:
        return ret_data.forward()

    data = ret_data.result
    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, collections.abc.Iterable):
        return StdRet.pass_errmsg(
            _(
                'Extension metadata file ({name}) must contain a dictionary '
                'or a list of dictionaries, found {data}'
            ),
            name=filename,
            data=repr(data),
        )

    ret: List[StdRet[AbcExtensionMetadata]] = []
    for item in data:
        if not isinstance(item, dict):
            ret.append(StdRet.pass_errmsg(
                _(
                    'Extension metadata file ({name}) must contain a dictionary '
                    'or a list of dictionaries'
                ),
                name=filename,
            ))
        else:
            ret_ext = load_extension(item)
            ret.append(ret_ext)
    return join_results(lambda x: tuple(x), *ret)
