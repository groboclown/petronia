
"""
The main execution for Petronia.
"""

import sys
from typing import Sequence
from .bootstrap.args import parse_args
from .bootstrap.all import bootstrap_petronia, run_petronia

def main(args: Sequence[str]) -> int:
    """
    Entry for the program.
    """
    user_args = parse_args(args)
    bus = bootstrap_petronia(user_args)
    return run_petronia(bus, user_args)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
    