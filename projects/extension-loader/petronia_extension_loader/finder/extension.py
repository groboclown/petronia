"""
Searches for an extension.
"""

from typing import Sequence, Iterable, List, Tuple, Dict
import os
import re
from petronia_common.util import StdRet, UserMessage, load_structured_file
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
    r'^([a-z0-9]+[_-])*[a-z0-9]+-extension.((yaml)|(json))$'
)


def find_extension_dirs(data_path: str) -> Iterable[str]:
    """Find all the extension directories in the data path."""
    for data_dir in data_path.split(os.pathsep):
        if os.path.isdir(data_dir):
            for subdir in EXTENSION_SUBDIR_NAMES:
                fqn = os.path.join(data_dir, subdir)
                if os.path.isdir(fqn):
                    yield fqn


def find_installed_extensions(
        extension_dirs: Sequence[str],
) -> Tuple[List[ExtensionInfo], Dict[str, List[UserMessage]]]:
    """Find all installed extensions.  Rather than returning a StdRet for errors,
    the parsed errors are returned as a separate structure.  This is because
    we don't want Petronia to fail just because some munged up file is stuck
    into the structure."""
    errors: Dict[str, List[UserMessage]] = {}
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
                    errors[name] = errors.get(name) or []
                    errors[name].append(UserMessage(
                        TRANSLATION_CATALOG,
                        _('Errors found in extension defined in {filename}'),
                        filename=fqn,
                    ))
                    errors[name].extend(res.error_messages())
                else:  # pragma no cover
                    # uncomment this no-cover when the extension loading is supported.
                    ret.append(res.result)  # pragma no cover
            elif EXTENSION_DEF_NAME_RE.match(name):
                res = load_extension_from_yaml(extension_dirs, fqn)
                if res.has_error:
                    errors[name] = errors.get(name) or []
                    errors[name].append(UserMessage(
                        TRANSLATION_CATALOG,
                        _('Errors found in the yaml extension definition file ({filename})'),
                        filename=fqn,
                    ))
                    errors[name].extend(res.error_messages())
                else:
                    ret.append(res.result)

    return ret, errors


def load_extension_from_zip(filename: str) -> StdRet[ExtensionInfo]:
    """Load the extension information from the zip distribution file."""
    return StdRet.pass_errmsg(
        TRANSLATION_CATALOG,
        _('zip extension found ({name}) but zip extension loading is not supported yet'),
        name=filename,
    )


def load_extension_from_yaml(
        path: Sequence[str],
        filename: str,
) -> StdRet[ExtensionInfo]:
    """Load the extension information from a yaml or json file."""
    docs_res = load_structured_file(filename)
    if docs_res.has_error:
        return docs_res.forward()
    docs = docs_res.result
    if not isinstance(docs, dict):
        if len(docs) != 1:
            return StdRet.pass_errmsg(
                TRANSLATION_CATALOG,
                _('Extension file ({filename}) invalid; it must be a single yaml document'),
                filename=filename,
            )
        ext_res = load_extension(docs[0])
    else:
        ext_res = load_extension(docs)
    if ext_res.has_error:
        return ext_res.forward()
    return StdRet.pass_ok(ExtensionInfo(path, ext_res.result))
