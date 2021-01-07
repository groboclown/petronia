"""CLI Entry Point.  This is intended to be as minimal as possible, because it
is not tested."""

import sys
from . import main
sys.exit(main.main(sys.argv[1:]))
