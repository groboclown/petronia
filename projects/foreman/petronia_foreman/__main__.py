
"""
Module entry point.  Just calls out to the main CLI function.
"""

import sys
from . import main

if __name__ == '__main__':  # pragma: no cover
    sys.exit(main.main(sys.argv))
