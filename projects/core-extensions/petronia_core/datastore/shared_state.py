"""Shared state data."""

from typing import Dict, Tuple, Sequence, Optional
import datetime
from petronia_common.util import tznow

_STORED_DATA: Dict[str, Tuple[str, datetime.datetime]] = {}


def get_data(data_id: str) -> Optional[Tuple[str, datetime.datetime]]:
    """Get the data associated with the data_id."""
    return _STORED_DATA.get(data_id)


def store_data(data_id: str, value: str) -> Tuple[bool, datetime.datetime]:
    """Store the data, either overwriting or creating anew."""
    if data_id in _STORED_DATA:
        updated = True
        now = tznow()
        if _STORED_DATA[data_id][1] == now:
            # Updating the data requires the times to be different.
            # Note that this is super, super time sensitive, so chances of the
            # code coverage reaching this is low.
            now = datetime.datetime(  # pragma no cover
                year=now.year, month=now.month, day=now.day,
                hour=now.hour, minute=now.minute, second=now.second,
                microsecond=now.microsecond + 1,
                tzinfo=now.tzinfo,
            )
    else:
        updated = False
        now = tznow()
    _STORED_DATA[data_id] = (value, now)
    return updated, now


def delete_data(data_id: str) -> bool:
    """Delete the data. Returns True if deleted."""
    if data_id in _STORED_DATA:
        del _STORED_DATA[data_id]
        return True
    return False


def clear_data() -> None:
    """An internal accessor to clear out the shared data."""
    _STORED_DATA.clear()


def stored_data_ids() -> Sequence[str]:
    """An internal accessor to find the stored data IDs."""
    return tuple(_STORED_DATA.keys())
