
from typing import Sequence
import argparse
from .configuration import read_configuration_file


def main(vargs: Sequence[str]) -> int:
    parser = argparse.ArgumentParser('petronia')
    parser.add_argument(
        '-c', '--config', type=str, default=None,
        help='configuration file to load.'
    )

    args = parser.parse_args(vargs[1:])
    foreman_config = read_configuration_file(args.config)


    return 0
