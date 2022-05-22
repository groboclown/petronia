
"""
Create the marshaller Python object source.
"""

from typing import Dict, Set, List, Any
import os
from petronia_common.util import StdRet, RET_OK_NONE, tznow
from petronia_common.util import i18n as _
from petronia_common.util import STANDARD_PETRONIA_CATALOG as STDC
from petronia_common.extension.config import AbcExtensionMetadata
from .load_definition import ExtensionDataFile
from .structure import (
    ImportStruct,
    create_structures, create_import_struct,
)
from .template import load_template, templatize, clean_up_text
from .performance_timer import PerfTimer


EVENT_TEMPLATE_NAME = 'event_file.py.mustache'
EVENT_INIT_TEMPLATE_NAME = 'event_init.py.mustache'
TEST_TEMPLATE_NAME = 'event_file_test.py.mustache'
INIT_SRC_FILE_NAME = '__init__.py'
SRC_EXTENSION = '.py'
TEST_DIR_NAME = 'tests'
TEST_SRC_EXTENSION = '_test.py'


_TEMPLATES: Dict[str, str] = {}


def create_api_marshal_source(  # pylint: disable=too-many-arguments
        output_dir: str, event_module_name: str, data: ExtensionDataFile,
        language: str, generate_api: bool, generate_internals: bool, generate_states: bool,
) -> StdRet[None]:
    """Create the marshaller source file."""
    if language != 'python':
        raise ValueError('Only supports Python output at the moment.')
    timer = PerfTimer()
    ret_data = create_structures(data, generate_api, generate_internals, generate_states)
    timer.report(f'create_structures({event_module_name})')
    if ret_data.has_error:
        return ret_data.forward()
    structures, imports = ret_data.result
    timer.start()
    res = mk_init(output_dir, event_module_name)
    timer.report(f'mk_init({event_module_name})')
    if res.has_error:
        return res.forward()
    timer.start()
    res = mk_event_marshal_src(output_dir, data.metadata, event_module_name, structures, imports)
    timer.report(f'mk_event_marshal_src({event_module_name})')
    if res.has_error:
        return res.forward()
    timer.start()
    res = mk_event_marshal_test_src(
        output_dir, data.metadata, event_module_name, structures, imports,
    )
    timer.report(f'mk_event_marshal_test_src({event_module_name})')
    if res.has_error:
        return res.forward()
    return RET_OK_NONE


def mk_event_marshal_src(
        output_dir: str, metadata: AbcExtensionMetadata,
        event_module_name: str, structures: List[Dict[str, Any]], imports: List[ImportStruct],
) -> StdRet[None]:
    """Create the marshal source file."""
    ret_template = load_template(EVENT_TEMPLATE_NAME)
    if ret_template.has_error:
        return ret_template.forward()
    event_src = os.path.join(output_dir, event_module_name + SRC_EXTENSION)
    try:
        with open(event_src, 'w', encoding='utf-8') as f:
            f.write(clean_up_text(templatize(
                ret_template.result,
                {
                    'extension_name': metadata.name,
                    'extension_name_repr': repr(metadata.name),
                    'extension_version':
                        f'{metadata.version[0]}.{metadata.version[1]}.{metadata.version[2]}',
                    'extension_version_repr': repr(metadata.version),
                    'imports': create_import_struct(imports),
                    'structures': structures,
                    'now': tznow().isoformat(),
                },
            )))
    except OSError as err:
        return StdRet.pass_errmsg(
            STDC, _('Failed to write to {name}: {err}'),
            name=event_src, err=repr(err),
        )
    return RET_OK_NONE


_INIT_CONTENTS: Dict[str, Set[str]] = {}


def mk_init(output_dir: str, event_module_name: str) -> StdRet[None]:
    """Create the init file."""
    ret_template = load_template(EVENT_INIT_TEMPLATE_NAME)
    if ret_template.has_error:
        return ret_template.forward()
    init_src = os.path.join(output_dir, INIT_SRC_FILE_NAME)
    if init_src not in _INIT_CONTENTS:
        _INIT_CONTENTS[init_src] = set()
    _INIT_CONTENTS[init_src].add(event_module_name)
    # Append the "import" statement.
    try:
        with open(init_src, 'w', encoding='utf-8') as f:
            f.write(clean_up_text(templatize(
                ret_template.result,
                {
                    'modules': [{'name': n} for n in sorted(list(_INIT_CONTENTS[init_src]))],
                    'now': tznow().isoformat(),
                },
            )))
    except OSError as err:
        return StdRet.pass_errmsg(
            STDC, _('Failed to write to {name}: {err}'),
            name=init_src, err=repr(err),
        )
    test_dir = os.path.join(output_dir, TEST_DIR_NAME)
    test_init_src = os.path.join(test_dir, INIT_SRC_FILE_NAME)
    try:
        if not os.path.isdir(test_dir):
            os.mkdir(test_dir)
        # Even if the file exists, overwrite it.
        with open(test_init_src, 'w', encoding='utf-8') as f:
            f.write(clean_up_text(templatize(
                ret_template.result,
                {'now': tznow().isoformat()},
            )))
    except OSError as err:
        return StdRet.pass_errmsg(
            STDC, _('Failed to write to {name}: {err}'),
            name=test_init_src, err=repr(err),
        )
    return RET_OK_NONE


def mk_event_marshal_test_src(
        output_dir: str, metadata: AbcExtensionMetadata,
        event_module_name: str, structures: List[Dict[str, Any]], imports: List[ImportStruct],
) -> StdRet[None]:
    """Create the marshal test file."""
    ret_template = load_template(TEST_TEMPLATE_NAME)
    if ret_template.has_error:
        return ret_template.forward()
    test_file_src = os.path.join(output_dir, TEST_DIR_NAME, event_module_name + TEST_SRC_EXTENSION)
    try:
        with open(test_file_src, 'w', encoding='utf-8') as f:
            f.write(clean_up_text(templatize(
                ret_template.result,
                {
                    'extension_name': metadata.name,
                    'extension_name_repr': repr(metadata.name),
                    'extension_version':
                        f'{metadata.version[0]}.{metadata.version[1]}.{metadata.version[2]}',
                    'extension_version_repr': repr(metadata.version),
                    'imports': create_import_struct(imports),
                    'structures': structures,
                    'module_name': event_module_name,
                    'now': tznow().isoformat(),
                },
            )))
    except OSError as err:
        return StdRet.pass_errmsg(
            STDC, _('Failed to write to {name}: {err}'),
            name=test_file_src, err=repr(err),
        )

    return RET_OK_NONE
