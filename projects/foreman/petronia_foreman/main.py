
"""
The CLI entry point for the foreman process.
"""

from typing import Sequence, Optional
import argparse
from .configuration import read_configuration_file


def main(vargs: Sequence[str]) -> int:
    """
    CLI Entry point for Foreman.

    :param vargs:
    :return:
    """
    # TODO properly translate the information sent to the user.

    try:
        parser = argparse.ArgumentParser('petronia')
        parser.add_argument(
            '-c', '--config', type=str, default=None,
            help='configuration file to load.',
        )

        args = parser.parse_args(vargs[1:])
        config_file: Optional[str] = args.config
        foreman_config = read_configuration_file(config_file)
        if foreman_config.has_error:
            print("Problems found reading the configuration file:")
            for msg in foreman_config.error_messages():
                print(msg.debug())

        return 0
    except KeyboardInterrupt:
        print("Halting due to user interruption.")

        # TODO shutdown child processes.

        return 1
