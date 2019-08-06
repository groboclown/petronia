
"""
The initial Petronia execution setup space.

This is split from the main `petronia3` module to allow clamping down of child process access.
"""


if __name__ == '__main__':
    import sys
    from .main import main
    sys.exit(main(sys.argv))
