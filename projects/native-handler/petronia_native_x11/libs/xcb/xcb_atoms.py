"""Generated list of atoms."""

from typing import Dict, List, Tuple
from .atomlist import ATOM_NAMES
import ctypes

from petronia_common.util import StdRet
from . import xcb_native


class AtomDef:
    __slots__ = ('_vals',)

    def __init__(self, vals: Dict[str, xcb_native.XcbAtom]) -> None:
        self._vals = vals

    def __getattr__(self, item: str) -> xcb_native.XcbAtom:
        """Fetch the value, if known.  Otherwise, raises a key error."""
        return self._vals[item]


def initialize_atoms(
        lib: xcb_native.LibXcb,
        conn: xcb_native.XcbConnectionP,
) -> StdRet[AtomDef]:
    """Initialize the atom list."""
    refs: Dict[str, xcb_native.XcbAtom] = {}

    cookies: List[Tuple[bytes, xcb_native.XcbInternAtomCookie]] = []

    # Make the request first
    for name in ATOM_NAMES:
        chars = ctypes.c_char_p(name)
        cookie = lib.xcb_intern_atom_unchecked(
            conn, ctypes.c_uint8(0), ctypes.c_uint16(len(name) - 1), chars,
        )
        cookies.append((name, cookie))

    # Then check responses
    for name, cookie in cookies:
        reply = lib.xcb_intern_atom_reply(conn, cookie, ctypes.cast(xcb_native.NULL, xcb_native.XcbGenericErrorPP))
        if not reply:
            # Error occurred; get the next atom.
            continue
        try:
            atom = reply.contents.atom
            name_str = name.decode('utf-8')
        finally:
            lib.free(reply)

        refs[name_str] = atom
        # Strip off leading '_' because of python naming.
        while name_str.startswith('_'):
            name_str = name_str[1:]
        if name_str not in refs:
            refs[name_str] = atom

    return StdRet.pass_ok(AtomDef(refs))
