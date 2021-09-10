
"""
Perform templatization operations.
"""

from typing import Dict, Any
import os
import pystache
from petronia_common.util import StdRet, STANDARD_PETRONIA_CATALOG
from petronia_common.util import i18n as _


def templatize(template: str, data: Dict[str, Any]) -> str:
    """Process the template."""
    renderer = pystache.Renderer(
        escape=lambda u: u,
    )
    rendered = renderer.render(template, data)
    return rendered


def clean_up_text(text: str) -> str:
    """Strip off trailing whitespace, and ensure there's only 1 EOL at the end."""

    # Ensure that there isn't extra whitespace at the end of lines.
    ret = ''
    for line in text.splitlines():
        ret += line.rstrip() + '\n'

    while ret[-2:] == '\n\n':
        ret = ret[:-1]
    return ret


def load_template(name: str) -> StdRet[str]:
    """Load in all the template definitions from the files."""
    template_file = os.path.abspath(os.path.join(os.path.dirname(__file__), name))
    try:
        with open(template_file, 'r', encoding='utf-8') as f:
            return StdRet.pass_ok(f.read())
    except OSError as err:
        return StdRet.pass_errmsg(
            STANDARD_PETRONIA_CATALOG,
            _('could not open template file {name}: {err}'),
            name=template_file,
            err=repr(err),
        )
