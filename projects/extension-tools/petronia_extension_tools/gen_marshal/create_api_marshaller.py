
"""
Create the marshaller Python object source.
"""

from typing import Dict, List, Any
import os
import datetime
from petronia_common.util import StdRet, RET_OK_NONE
from petronia_common.util import i18n as _
from petronia_common.extension.config import ApiExtensionMetadata
from .structure import (
    ImportStruct,
    create_structures, create_import_struct,
)
from .template import load_template, templatize


EVENT_TEMPLATE_NAME = 'event_file.py.mustache'
EVENT_INIT_TEMPLATE_NAME = 'event_init.py.mustache'
TEST_TEMPLATE_NAME = 'event_file_test.py.mustache'
INIT_SRC_FILE_NAME = '__init__.py'
SRC_EXTENSION = '.py'
TEST_DIR_NAME = 'tests'
TEST_SRC_EXTENSION = '_test.py'


_TEMPLATES: Dict[str, str] = {}


def create_api_marshal_source(
        output_dir: str, event_module_name: str, metadata: ApiExtensionMetadata,
) -> StdRet[None]:
    """Create the marshaller source file."""
    ret_data = create_structures(metadata)
    if ret_data.has_error:
        return ret_data.forward()
    structures, imports = ret_data.result
    res = mk_init(output_dir, event_module_name)
    if res.has_error:
        return res.forward()
    res = mk_event_marshal_src(output_dir, metadata, event_module_name, structures, imports)
    if res.has_error:
        return res.forward()
    res = mk_event_marshal_test_src(output_dir, metadata, event_module_name, structures, imports)
    if res.has_error:
        return res.forward()
    return RET_OK_NONE


def mk_event_marshal_src(
        output_dir: str, metadata: ApiExtensionMetadata,
        event_module_name: str, structures: List[Dict[str, Any]], imports: List[ImportStruct],
) -> StdRet[None]:
    ret_template = load_template(EVENT_TEMPLATE_NAME)
    if ret_template.has_error:
        return ret_template.forward()
    event_src = os.path.join(output_dir, event_module_name + SRC_EXTENSION)
    try:
        with open(event_src, 'w') as f:
            f.write(templatize(
                ret_template.result,
                {
                    'extension_name': metadata.name,
                    'extension_version': '{0}.{1}.{2}'.format(*metadata.version),
                    'imports': create_import_struct(imports),
                    'structures': structures,
                    'now': datetime.datetime.utcnow().isoformat(),
                },
            ))
    except OSError as err:
        return StdRet.pass_errmsg(
            _('Failed to write to {name}: {err}'),
            name=event_src, err=repr(err),
        )
    return RET_OK_NONE


def mk_init(output_dir: str, event_module_name: str) -> StdRet[None]:
    ret_template = load_template(EVENT_INIT_TEMPLATE_NAME)
    if ret_template.has_error:
        return ret_template.forward()
    init_src = os.path.join(output_dir, INIT_SRC_FILE_NAME)
    # Append the "import" statement.
    try:
        if not os.path.isfile(init_src):
            with open(init_src, 'w') as f:
                f.write(templatize(
                    ret_template.result,
                    {'now': datetime.datetime.utcnow().isoformat()},
                ))
        with open(init_src, 'w+') as f:
            f.write('from . import {0}\n'.format(event_module_name))
    except OSError as err:
        return StdRet.pass_errmsg(
            _('Failed to write to {name}: {err}'),
            name=init_src, err=repr(err),
        )
    test_dir = os.path.join(output_dir, TEST_DIR_NAME)
    test_init_src = os.path.join(test_dir, INIT_SRC_FILE_NAME)
    try:
        if not os.path.isdir(test_dir):
            os.mkdir(test_dir)
        if not os.path.isfile(test_init_src):
            with open(test_init_src, 'w') as f:
                f.write(templatize(
                    ret_template.result,
                    {'now': datetime.datetime.utcnow().isoformat()},
                )),
    except OSError as err:
        return StdRet.pass_errmsg(
            _('Failed to write to {name}: {err}'),
            name=test_init_src, err=repr(err),
        )
    return RET_OK_NONE


def mk_event_marshal_test_src(
        output_dir: str, metadata: ApiExtensionMetadata,
        event_module_name: str, structures: List[Dict[str, Any]], imports: List[ImportStruct],
) -> StdRet[None]:
    ret_template = load_template(TEST_TEMPLATE_NAME)
    if ret_template.has_error:
        return ret_template.forward()
    test_file_src = os.path.join(output_dir, TEST_DIR_NAME, event_module_name + TEST_SRC_EXTENSION)
    try:
        with open(test_file_src, 'w') as f:
            f.write(templatize(
                ret_template.result,
                {
                    'extension_name': metadata.name,
                    'extension_version': '{0}.{1}.{2}'.format(*metadata.version),
                    'imports': create_import_struct(imports),
                    'structures': structures,
                    'module_name': event_module_name,
                    'now': datetime.datetime.utcnow().isoformat(),
                },
            ))
    except OSError as err:
        return StdRet.pass_errmsg(
            _('Failed to write to {name}: {err}'),
            name=test_file_src, err=repr(err),
        )

    return RET_OK_NONE
