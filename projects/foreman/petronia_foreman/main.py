
from typing import Sequence
import argparse


def main(vargs: Sequence[str]) -> int:
    parser = argparse.ArgumentParser('petronia')
    parser.add_argument(
        '-c', '--config', type=str,
        help='configuration file to load.'
    )

    args = parser.parse_args(vargs[1:])
