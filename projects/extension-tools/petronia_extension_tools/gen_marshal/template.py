
"""
Perform templatization operations.
"""

from typing import Dict, Any
import os
import pystache
from petronia_common.util import StdRet, STANDARD_PETRONIA_CATALOG
from petronia_common.util import i18n as _


def templatize(template: str, data: Dict[str, Any], r_strip: bool = True) -> str:
    """Process the template."""
    renderer = pystache.Renderer(
        escape=lambda u: u,
    )
    rendered = renderer.render(template, data)

    if not r_strip:
        return rendered

    ret = ''
    for line in rendered.splitlines():
        ret += line.rstrip() + '\n'
    return ret


def load_template(name: str) -> StdRet[str]:
    """Load in all the template definitions from the files."""
    template_file = os.path.abspath(os.path.join(os.path.dirname(__file__), name))
    try:
        with open(template_file, 'r') as f:
            return StdRet.pass_ok(f.read())
    except OSError as err:
        return StdRet.pass_errmsg(
            STANDARD_PETRONIA_CATALOG,
            _('could not open template file {name}: {err}'),
            name=template_file,
            err=repr(err),
        )
