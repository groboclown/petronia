"""Shared state data."""

from typing import Dict, Tuple, List, Sequence, Optional, Any
import os
import shutil
import datetime
import tempfile

from petronia_common.event_stream import RawBinaryReader
from petronia_common.util import tznow, StdRet, RET_OK_NONE
from petronia_common.util import i18n as _
from .state import datastore as datastore_state
from ..user_messages import TRANSLATION_CATALOG


_STORED_DATA: Dict[str, Tuple[str, datetime.datetime]] = {}
_STORED_BINARY_FILES: Dict[str, str] = {}
_CACHE_DIR: List[str] = ['']


def load_configuration(config: Dict[str, Any]) -> StdRet[None]:
    """Initialize the data store."""
    parsed_res = datastore_state.ConfigurationState.parse_data(config)
    if parsed_res.has_error:
        return parsed_res.forward()

    clear_data()
    if _CACHE_DIR[0] and os.path.isdir(_CACHE_DIR[0]):
        shutil.rmtree(_CACHE_DIR[0], True)
    if parsed_res.result.cachedir is not None:
        try:
            os.makedirs(parsed_res.result.cachedir, exist_ok=True)
        except OSError as err:
            return StdRet.pass_exception(
                TRANSLATION_CATALOG,
                _('Failed to create cache directory {cache_dir}'),
                err,
                cache_dir=parsed_res.result.cachedir,
            )
        _CACHE_DIR[0] = parsed_res.result.cachedir
    else:
        _CACHE_DIR[0] = tempfile.mkdtemp()
    return RET_OK_NONE


def get_data(data_id: str) -> Optional[Tuple[str, datetime.datetime]]:
    """Get the data associated with the data_id."""
    return _STORED_DATA.get(data_id)


def get_binary_file(data_id: str) -> Optional[str]:
    """Get the binary data associated with the data_id."""
    return _STORED_BINARY_FILES[data_id]


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


def store_binary(data_id: str, reader: RawBinaryReader) -> bool:
    """Store the binary data."""
    updated = data_id in _STORED_BINARY_FILES
    _del_bin_cache_file(data_id)
    try:
        temp_f = tempfile.TemporaryFile('wb', delete=False, dir=_CACHE_DIR[0])
        try:
            temp_f.write(reader())
        finally:
            temp_f.close()
    except OSError as err:
        # todo report error
        pass
    return updated


def delete_data(data_id: str) -> bool:
    """Delete the data. Returns True if deleted."""
    ret = False
    if data_id in _STORED_DATA:
        del _STORED_DATA[data_id]
        ret = True
    if data_id in _STORED_BINARY_FILES:
        _del_bin_cache_file(data_id)
        del _STORED_BINARY_FILES[data_id]
        ret = True
    return ret


def clear_data() -> None:
    """An internal accessor to clear out the shared data."""
    _STORED_DATA.clear()
    for data_id in _STORED_BINARY_FILES.values():
        _del_bin_cache_file(data_id)
    _STORED_BINARY_FILES.clear()


def _del_bin_cache_file(data_id: str) -> None:
    if data_id in _STORED_BINARY_FILES and os.path.isfile(_STORED_BINARY_FILES[data_id]):
        try:
            os.unlink(_STORED_BINARY_FILES[data_id])
        except OSError as err:
            # ignore.  Should this be logged?
            pass


def stored_data_ids() -> Sequence[str]:
    """An internal accessor to find the stored data IDs."""
    return tuple(*_STORED_DATA.keys(), *_STORED_BINARY_FILES.keys())
