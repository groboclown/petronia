"""
Searches for an extension.
"""

from typing import Sequence, Iterable, List
import os
import re
from petronia_common.util import StdRet, UserMessage, join_errors, load_yaml_documents
from petronia_common.util import i18n as _
from petronia_common.extension.config import (
    load_extension,
)
from ..defs import ExtensionInfo, TRANSLATION_CATALOG


EXTENSION_SUBDIR_NAMES = (
    'extensions',
    'plugins',
    'plug-ins',
)
EXTENSION_ZIP_NAME_RE = re.compile(
    r'^([a-z0-9]+[_-])*[a-z0-9]+-\d+\.\d+\.\d+.((zip)|(tar.bz2)|(tar.xz)|(tar.gz))$'
)
EXTENSION_DEF_NAME_RE = re.compile(
    r'^([a-z0-9]+[_-])*[a-z0-9]+-extension.yaml$'
)


def find_extension_dirs(data_path: str) -> Iterable[str]:
    """Find all the extension directories in the data path."""
    for data_dir in data_path.split(os.pathsep):
        if os.path.isdir(data_dir):
            for subdir in EXTENSION_SUBDIR_NAMES:
                fqn = os.path.join(data_dir, subdir)
                if os.path.isdir(fqn):
                    yield fqn


def find_installed_extensions(extension_dirs: Sequence[str]) -> StdRet[Sequence[ExtensionInfo]]:
    """Find all installed extensions."""
    errors: List[UserMessage] = []
    ret: List[ExtensionInfo] = []

    for ext_dir in extension_dirs:
        if not os.path.isdir(ext_dir):
            continue
        for name in os.listdir(ext_dir):
            fqn = os.path.join(ext_dir, name)
            if not os.path.isfile(fqn):
                continue
            if EXTENSION_ZIP_NAME_RE.match(name):
                res = load_extension_from_zip(fqn)
                if res.has_error:
                    errors.extend(res.error_messages())
                else:
                    ret.append(res.result)
            elif EXTENSION_DEF_NAME_RE.match(name):
                res = load_extension_from_yaml(extension_dirs, fqn)
                if res.has_error:
                    errors.append(UserMessage(
                        TRANSLATION_CATALOG,
                        _('Errors found in the yaml extension definition file ({filename})'),
                        filename=fqn,
                    ))
                    errors.extend(res.error_messages())
                else:
                    ret.append(res.result)

    if errors:
        return StdRet.pass_error(join_errors(*errors))
    return StdRet.pass_ok(ret)


def load_extension_from_zip(_filename: str) -> StdRet[ExtensionInfo]:
    """Load the extension information from the zip distribution file."""
    raise NotImplementedError()


def load_extension_from_yaml(
        path: Sequence[str],
        filename: str,
) -> StdRet[ExtensionInfo]:
    """Load the extension information from a yaml file."""
    try:
        with open(filename, 'r') as f:
            docs = load_yaml_documents(f.read())
        if docs.has_error:
            return docs.forward()
        if len(docs.result) != 1:
            return StdRet.pass_errmsg(
                TRANSLATION_CATALOG,
                _('Extension file ({filename}) invalid; it must be a single yaml document'),
                filename=filename,
            )
        ext = load_extension(docs.result[0])
        if ext.has_error:
            return ext.forward()
        return StdRet.pass_ok(ExtensionInfo(path, ext.result))
    except OSError as err:
        return StdRet.pass_exception(
            _('Failed to read contents of {filename}'),
            err,
            filename=filename,
        )
