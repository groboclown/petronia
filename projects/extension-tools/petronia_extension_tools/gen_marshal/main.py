
"""
Entry for the event marshal generation tool.
"""

from typing import Sequence, List
import os
import argparse
from petronia_common.extension.config import AbcExtensionMetadata, ApiExtensionMetadata
from petronia_common.util import i18n as _
from .load_definition import load_extension_file
from .create_api_marshaller import create_api_marshal_source
from ..user_message import display_error, display


def main(cmd_args: Sequence[str]) -> int:
    """Entry function"""
    parser = argparse.ArgumentParser(
        prog=cmd_args[0],
        description="Event marshal sourcecode generator.",
    )
    parser.add_argument(
        'extensions', metavar='extension-file', type=str, nargs='+',
        help="Extension definition file.",
    )
    parser.add_argument(
        '--implementation', '-i', action="store_true",
        help=(
            "Generate implementation (private) events.  Without this, only "
            "the public side of events are generated."
        ),
    )
    parser.add_argument(
        '--language', '-l', choices=['python'], default='python',
        help="Generated language.",
    )
    parser.add_argument(
        '--output', '-o', required=True, type=str,
        help="Output base directory for the generated code.",
    )
    args = parser.parse_intermixed_args(cmd_args)

    generate_internals: bool = args.implementation
    language: str = args.language
    output_dir: str = args.output
    if not os.path.isdir(output_dir):
        display(_("Error: output directory ({d}) does not exist."), d=output_dir)
        return 1
    extension_files: Sequence[str] = args.extensions

    ext_metadata: List[AbcExtensionMetadata] = []
    for ext_name in extension_files:
        if not os.path.isfile(ext_name):
            display(_("Error: file does not exist: {n}"), n=ext_name)
            continue
        loaded = load_extension_file(ext_name)
        if loaded.has_error:
            display(_('Error: extension file not valid: {n}'), n=ext_name)
            display_error(loaded.valid_error)
        else:
            ext_metadata.extend(loaded.result)

    for metadata in ext_metadata:
        if isinstance(metadata, ApiExtensionMetadata):
            validation = metadata.validate_type()
            if validation:
                display(
                    _('Extension {name} metadata has validation problems'),
                    name=metadata.name,
                )
                display_error(validation)
                continue
            ret = create_api_marshal_source(
                output_dir, normalize_name(metadata.name),
                metadata,
                language,
                generate_internals,
            )
            if ret.has_error:
                display(
                    _('Encountered a problem while generating the source for {name}'),
                    name=metadata.name,
                )
                display_error(ret.valid_error)
            display(_('Generated {name}'), name=metadata.name)
        else:
            display(
                _('Skipping {name}: only generating events for API extensions.'),
                name=metadata.name,
            )
    return 0


def normalize_name(name: str) -> str:
    """Turn the extension name into a file name."""
    ret = ''
    for i in name:
        if not i.isalnum() and i not in '._':
            ret += '_'
        else:
            ret += i.lower()
    if '.' in ret:
        return ret[ret.rindex('.') + 1:]
    return ret
