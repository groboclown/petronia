"""Generated list of atoms."""

from typing import Dict, List, Tuple
from .atomlist import ATOM_NAMES
import ctypes

from petronia_common.util import StdRet
from . import xcb, xcb_types
from .. import ct_util, libc


class AtomDef:
    __slots__ = ('_vals',)

    def __init__(self, vals: Dict[str, xcb_types.XcbAtom]) -> None:
        self._vals = vals

    def __getattr__(self, item: str) -> xcb_types.XcbAtom:
        """Fetch the value, if known.  Otherwise, raises a key error."""
        return self._vals[item]


def initialize_atoms(
        xcb_lib: xcb.LibXcb,
        c_lib: libc.LibC,
        conn: xcb_types.XcbConnectionP,
) -> StdRet[AtomDef]:
    """Initialize the atom list."""
    refs: Dict[str, xcb_types.XcbAtom] = {}

    cookies: List[Tuple[bytes, xcb_types.XcbInternAtomCookie]] = []

    # Make the request first
    for name in ATOM_NAMES:
        chars = ctypes.c_char_p(name)
        cookie = xcb_lib.xcb_intern_atom_unchecked(
            conn, ctypes.c_uint8(0), ctypes.c_uint16(len(name) - 1), chars,
        )
        cookies.append((name, cookie))

    # Then check responses
    for name, cookie in cookies:
        reply = xcb_lib.xcb_intern_atom_reply(
            conn, cookie, ct_util.as_null(xcb_types.XcbGenericErrorPP),
        )
        if not reply:
            # Error occurred; get the next atom.
            continue
        try:
            atom = reply.contents.atom
            name_str = name.decode('utf-8')
        finally:
            c_lib.force_free(reply)

        refs[name_str] = atom
        # Strip off leading '_' because of python naming.
        while name_str.startswith('_'):
            name_str = name_str[1:]
        if name_str not in refs:
            refs[name_str] = atom

    return StdRet.pass_ok(AtomDef(refs))
