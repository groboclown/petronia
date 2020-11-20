
"""
The CLI entry point for the foreman process.
"""

from typing import Sequence
import argparse
from petronia_common.util import i18n as _
from .user_message import display, display_error, translate, load_translation
from .configuration import SUPPORTED_PLATFORMS, read_configuration_file, detect_platform
from .foreman_runner import ForemanRunner


def main(vargs: Sequence[str]) -> int:
    """
    CLI Entry point for Foreman.

    :param vargs:
    :return:
    """

    # This is a bit of a chicken-and-egg problem.
    # The configuration file must be loaded to find the translation files
    # in order to populate the argument list, but the arguments must be
    # defined before the configuration is loaded.
    parser = argparse.ArgumentParser('petronia')
    parser.add_argument(
        '-c', '--config', type=str, default=None,
        help=translate(
            _('configuration file to load.'),
        ),
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

    load_translation(platform.result)

    foreman = ForemanRunner(platform.result, foreman_config.result)
    return foreman.run()
