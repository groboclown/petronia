
from typing import Sequence


class ExtensionDetails:
    def __init__(
            self,
            name: str,
            generates_event_ids: Sequence[str],
            listens_to_event_ids: Sequence[str],
    ) -> None:
        self.__name = name
        self.__generates_event_ids = tuple(generates_event_ids)
        self.__listens_to_event_ids = tuple(listens_to_event_ids)
