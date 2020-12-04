"""Shared utility test stuff for the event_stream code."""

from .. import consts


class ConstSizeChanger:
    """Helper for changing the max size constants.  It allows tests to try out
    reaching those limits without needing to make really large test data values."""
    def __init__(self) -> None:
        """Constructor"""
        self.max_id = consts.MAX_ID_SIZE
        self.max_json = consts.MAX_JSON_SIZE
        self.max_blob = consts.MAX_BLOB_SIZE
        consts.MAX_ID_SIZE = 10
        consts.MAX_JSON_SIZE = 60
        consts.MAX_BLOB_SIZE = 10

    def tear_down(self) -> None:
        """Restores the values."""
        consts.MAX_ID_SIZE = self.max_id
        consts.MAX_JSON_SIZE = self.max_json
        consts.MAX_BLOB_SIZE = self.max_blob
