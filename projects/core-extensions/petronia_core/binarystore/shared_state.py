"""Shared state data."""

from typing import Dict, List, Sequence, Set, Optional, Literal, Any
import os
import shutil
import tempfile
import hashlib
import datetime

from petronia_common.event_stream import RawBinaryReader
from petronia_common.util import (
    StdRet, RET_OK_NONE, RET_OK_TRUE, RET_OK_FALSE,
    join_errors,
    PetroniaReturnError,
)
from petronia_common.util import i18n as _
from .state import binarystore as binarystore_state
from ..user_messages import TRANSLATION_CATALOG


class StoredData:
    """Cached data values."""
    __slots__ = ('__sha256', '__filename', '__size', '__mime_type')

    def __init__(self, filename: str, mime_type: str, sha256: str, size: int) -> None:
        self.__sha256 = sha256
        self.__mime_type = mime_type
        self.__filename = filename
        self.__size = size

    @property
    def sha256(self) -> str:
        """sha256 of the data"""
        return self.__sha256

    @property
    def filename(self) -> str:
        """Location of the temporary file containing the data."""
        return self.__filename

    @property
    def size(self) -> int:
        """Size of the data"""
        return self.__size

    @property
    def mime_type(self) -> str:
        """Mime of the data"""
        return self.__mime_type

    def get_state(self) -> str:
        """Get the state of the data."""
        if os.path.isfile(self.filename):
            return "active"
        return "deleted"


class PendingStoreData:
    """Data that's okay to send"""
    __slots__ = ('__mime_type', '__request_time')

    def __init__(self, mime_type: str) -> None:
        self.__mime_type = mime_type
        self.__request_time = datetime.datetime.now()

    @property
    def mime_type(self) -> str:
        """The mime type of the pending request."""
        return self.__mime_type

    @property
    def request_time(self) -> datetime.datetime:
        """Time the request was made (local time)."""
        return self.__request_time

    def is_expired(self) -> bool:
        """Is this request expired?"""
        return datetime.datetime.now() - self.__request_time > _MAX_REQUEST_PENDING_TIME[0]


_STORED_FILES: Dict[str, StoredData] = {}
_DELETED_ENTRIES: Set[str] = set()
_PENDING_STORE: Dict[str, PendingStoreData] = {}
_CACHE_DIR: List[str] = ['']
_MAX_REQUEST_PENDING_TIME: List[datetime.timedelta] = [datetime.timedelta(minutes=5.0)]

DataState = Literal['pending', 'stored', 'deleted', 'unset']

VALID_MIME_TYPES = (
    'image/bmp', 'image/png', 'image/jpeg', 'image/svn', 'image/svg+xml',

    'audio/ac3', 'audio/aiff', 'audio/mp4', 'audio/mpa', 'audio/ogg', 'audio/flac',
    'audio/wav', 'audio/vorbis',
)


def load_configuration(config: Dict[str, Any]) -> StdRet[None]:
    """Initialize the data store."""
    parsed_res = binarystore_state.ConfigurationState.parse_data(config)
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

    if (
            isinstance(parsed_res.result.request_timeout_seconds, (float, int))
            and parsed_res.result.request_timeout_seconds > 0.0
    ):
        _MAX_REQUEST_PENDING_TIME[0] = datetime.timedelta(
            seconds=float(parsed_res.result.request_timeout_seconds),
        )

    return RET_OK_NONE


def get_data(data_id: str) -> Optional[StoredData]:
    """Get the binary data associated with the data_id."""
    _clear_expired_pending()
    return _STORED_FILES.get(data_id)


def is_deleted(data_id: str) -> bool:
    """Check if this data is marked as deleted."""
    return data_id in _DELETED_ENTRIES


def add_pending(data_id: str, pending: PendingStoreData) -> Optional[DataState]:
    """Mark a value as pending storage.  Returns None if the add worked, otherwise returns
    the state of the request."""
    _clear_expired_pending()
    if data_id in _STORED_FILES:
        return 'stored'
    if data_id in _DELETED_ENTRIES:
        return 'deleted'
    if data_id in _PENDING_STORE:
        return 'pending'
    _PENDING_STORE[data_id] = pending
    return None


def store_binary_data(
        data_id: str, size: int, reader: RawBinaryReader,
) -> StdRet[Optional[StoredData]]:
    """Store the binary data.  If the data is already stored, then this will return False and
    not store the data."""
    pending = _PENDING_STORE.get(data_id)
    if pending is None:
        return RET_OK_NONE

    # Remove the value before error checking.
    del _PENDING_STORE[data_id]
    _clear_expired_pending()

    data = _create(pending, size, reader)
    if data.has_error:
        return data.forward()
    _STORED_FILES[data_id] = data.result
    return data


def delete_binary_data(data_id: str) -> StdRet[bool]:
    """Delete the data. Returns True if deleted."""
    _clear_expired_pending()
    data = _STORED_FILES.get(data_id)
    if data is not None:
        # Mark as deleted before file delete / error checking.
        del _STORED_FILES[data_id]
        _DELETED_ENTRIES.add(data_id)
        return _delete(data)
    return RET_OK_FALSE


def clear_data() -> StdRet[None]:
    """An internal accessor to clear out the shared data."""
    errors: List[PetroniaReturnError] = []
    for data in _STORED_FILES.values():
        res = _delete(data)
        if res.has_error:
            errors.append(res.valid_error)
    _STORED_FILES.clear()
    if errors:
        return StdRet(error=join_errors(errors=errors), value=None)
    _DELETED_ENTRIES.clear()
    _PENDING_STORE.clear()
    return RET_OK_NONE


def known_data_ids() -> Sequence[str]:
    """An internal accessor to find the known data IDs."""
    return tuple([*_STORED_FILES.keys(), *_PENDING_STORE.keys(), *_DELETED_ENTRIES])


def active_data_ids() -> Sequence[str]:
    """An interior accessor to find the stored data IDs"""
    return tuple(_STORED_FILES.keys())


def _clear_expired_pending() -> None:
    """Clear out expired pending requests."""
    expired: List[str] = []
    for key, value in _PENDING_STORE.items():
        if value.is_expired():
            expired.append(key)
    for key in expired:
        del _PENDING_STORE[key]


def _delete(data: StoredData) -> StdRet[bool]:
    """Delete the value.  Returns True if it was deleted, False if it was already deleted."""
    if os.path.isfile(data.filename):
        try:
            os.unlink(data.filename)
        except (OSError, NotImplementedError) as err:
            return StdRet.pass_exception(
                TRANSLATION_CATALOG,
                _('failed to delete the cache file {filename}'),
                err,
                filename=data.filename,
            )
        return RET_OK_TRUE
    return RET_OK_FALSE


def _create(pending: PendingStoreData, size: int, reader: RawBinaryReader) -> StdRet[StoredData]:
    """Create a new StoredData value based on a reader."""
    sha256 = hashlib.sha256()
    remaining = size
    with tempfile.NamedTemporaryFile(
            mode='wb', delete=False, dir=_CACHE_DIR[0],
    ) as temp_f:
        try:
            while remaining > 0:
                next_length = min(4096, remaining)
                data = reader(next_length)
                sha256.update(data)
                temp_f.write(data)
                remaining -= next_length
        except OSError as err:
            try:
                temp_f.close()
                os.unlink(temp_f.name)
            except OSError:
                # ignore error
                pass
            return StdRet.pass_exception(
                TRANSLATION_CATALOG,
                _('failed to read/write data'),
                err,
            )
        return StdRet.pass_ok(StoredData(
            filename=temp_f.name,
            mime_type=pending.mime_type,
            sha256=sha256.hexdigest(),
            size=size,
        ))
