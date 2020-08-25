
"""
The CLI entry point for the foreman process.
"""

from typing import Sequence
import argparse
from petronia_common.util import i18n as _
from .user_message import display, display_error, translate
from .configuration import SUPPORTED_PLATFORMS, read_configuration_file, detect_platform


def main(vargs: Sequence[str]) -> int:
    """
    CLI Entry point for Foreman.

    :param vargs:
    :return:
    """

    try:
        # TODO Still need to translate the argument text...
        parser = argparse.ArgumentParser('petronia')
        parser.add_argument(
            '-c', '--config', type=str, default=None,
            help='configuration file to load.',
        )
        parser.add_argument(
            '-p', '--platform', type=str, default=None,
            help=translate(
                _(
                    'force running on a platform type, rather than auto-detect it.  The supported '
                    'types are {platforms}'
                ),
                platforms=repr(SUPPORTED_PLATFORMS),
            ),
        )
        args = parser.parse_args(vargs[1:])

        platform = detect_platform(args.platform)
        if platform.has_error:
            display(_("Problems found discovering the current platform:"))
            display_error(platform.valid_error)
            return 1

        foreman_config = read_configuration_file(args.config, platform.result)
        if foreman_config.has_error:
            display(_("Problems found reading the configuration file:"))
            display_error(foreman_config.valid_error)
            return 1

        return 0
    except KeyboardInterrupt:
        print("Halting due to user interruption.")

        # TODO shutdown child processes.

        return 1
