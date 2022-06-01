"""Native Library Interfaces

This provides ctype integration with native libraries.

General conventions:

* Every library has at most these files:
  * "lib{name}.py" (required)
    * Contains the Lib{name} class, which is a wrapper for the API calls in the library, plus
      possible helper calls.  This sets up the library functions using the ct_util calls,
      and provides a "problems" property.
    * Contains the function "load_{name}" that returns a StdRet[Lib{name}].
  * "lib{name}_types.py" (optional, if it has custom types)
    * Type structures and aliases for native library types.  These should be Python-ized names
      based on the library's c types.
  * "lib{name}_consts.py" (optional, if it has custom constants)
    * Constants for the library, which should be in SCREAMING_SNAKE case.  Python native
      values should be as-is, and native explicit versions should end with "__c".  Exceptions
      are the null aliases, which should be "NULL__type_name"
"""

from . import libc
from .xcb_library import xcb_types as libxcb_types
from .xcb_library import xcb as libxcb
from .xcb_library import xcb_consts as libxcb_consts
from .xcb_library import xcb_atoms, atomlist
from . import libcairo_types, libcairo, libcairo_consts
from . import libxcb_cursor_types, libxcb_cursor
from . import libxcb_icccm
from . import libxcb_randr
from . import libxcb_shape
from . import libxcb_util
from . import libxcb_xfixes
from . import libxcb_xinerama
from . import libxcb_xtest
from . import keys


"""
Example of how to find functions and static constants in libraries.

import os, ctypes
libnames = []
for f in os.listdir("/usr/lib"):
  if (
        f.startswith("libxcb")
        or f.startswith('libcairo')
  ) and ".so." in f:
    libnames.append(f)

libs = {}
for libn in libnames:
  print(f"loading {libn}")
  try:
    lib = ctypes.cdll.LoadLibrary(libn)
    libs[libn] = lib
  except OSError:
    print(f"failed to load {libn}")

def find_id(nid):
    for name, lib in libs.items():
      if hasattr(lib, nid):
        print(f"{nid}: {name}")

"""
