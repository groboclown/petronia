
from typing import Dict


class ForemanConfig:
    launcher_mapper: Dict[str, str]

    def __init__(self) -> None:
        self.launcher_mapper = {}
        self.native_handler_extension = ''
