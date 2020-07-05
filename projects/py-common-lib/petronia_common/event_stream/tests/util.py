
from typing import List, Tuple, Optional
import unittest
import io
from .. import reader
from .. import consts
from ..defs import RawEvent
from ...util import PetroniaReturnError


class ConstSizeChanger:
    def __init__(self) -> None:
        self.max_id = consts.MAX_ID_SIZE
        self.max_json = consts.MAX_JSON_SIZE
        self.max_blob = consts.MAX_BLOB_SIZE
        consts.MAX_ID_SIZE = 10
        consts.MAX_JSON_SIZE = 60
        consts.MAX_BLOB_SIZE = 10

    def tear_down(self) -> None:
        consts.MAX_ID_SIZE = self.max_id
        consts.MAX_JSON_SIZE = self.max_json
        consts.MAX_BLOB_SIZE = self.max_blob


class CallbackCollector:
    actual: List[Tuple[Optional[RawEvent], Optional[PetroniaReturnError], bool]]
    event_responses: List[bool]
    error_responses: List[bool]

    def __init__(
            self,
            event_responses: Optional[List[bool]] = None,
            error_responses: Optional[List[bool]] = None,
    ) -> None:
        self.actual = []
        self.event_responses = event_responses or []
        self.error_responses = error_responses or []

    def execute(self, data: bytes) -> None:
        reader.read_event_stream(io.BytesIO(data), self.on_event, self.on_end_of_stream, self.on_error)

    def on_event(self, event: RawEvent) -> bool:
        self.actual.append((event, None, False,))
        ret = False
        if self.event_responses:
            ret = self.event_responses.pop(0)
        return ret

    def on_end_of_stream(self) -> None:
        self.actual.append((None, None, True,))

    def on_error(self, error: PetroniaReturnError) -> bool:
        self.actual.append((None, error, False,))
        ret = False
        if self.error_responses:
            ret = self.error_responses.pop(0)
        return ret

    def next_as_raw_event(self, parent: unittest.TestCase) -> RawEvent:
        parent.assertTrue(len(self.actual) > 0)
        next_actual = self.actual.pop(0)
        parent.assertIsNotNone(next_actual[0])
        # mypy requirement
        assert next_actual[0] is not None
        return next_actual[0]

    def next_as_error(self, parent: unittest.TestCase) -> PetroniaReturnError:
        parent.assertTrue(len(self.actual) > 0)
        next_actual = self.actual.pop(0)
        parent.assertIsNotNone(next_actual[1])
        # mypy requirement
        assert next_actual[1] is not None
        return next_actual[1]

    def next_as_eof(self, parent: unittest.TestCase) -> None:
        parent.assertEqual(len(self.actual), 1)
        next_actual = self.actual.pop(0)
        parent.assertTrue(next_actual[2])

    def is_empty(self) -> bool:
        return len(self.actual) <= 0
