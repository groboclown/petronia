
from typing import Optional
import configparser
from .foreman import ForemanConfig


def read_configuration_file(filename: Optional[str]) -> ForemanConfig:
    parser = configparser.ConfigParser()
    parser.read(filename)
    raise NotImplementedError()
