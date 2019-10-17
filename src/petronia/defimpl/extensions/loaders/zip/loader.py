
"""
Simple directory path loading.  This supports local development modules or
local unzipped downloads.
"""

import os
import re
import zipimport
import datetime
import importlib.util
import importlib.machinery
from typing import Sequence, List, Optional, Tuple
from .....base import (
    log, WARN,
)
from .....base.security import SandboxPermission
from .....base.util import (
    in_or,
    STRING_EMPTY_TUPLE,
)
from .checksum import (
    check_file_hashes,
    get_mismatched_hashes,
    HASH_SHA2_256,
    HASH_SHA3_256,
    PETRONIA_HASHES,
)
from .signing import (
    file_signature_state,
    SIGNED,
)
from .metadata import read_zipfile_metadata_contents
from ...defs import (
    DiscoveredExtension,
    ExtensionLoader,
    ExtensionVersion,
    SecureExtensionVersion,
    ExtensionStorageCache,
    ANY_VERSION,
)


class ZipExtensionLoader(ExtensionLoader):
    """
    Loads zip files from directories.  Inspects the internals of the zips for
    the package properties, and checks the encryption and hash code of the
    files.  The directories are not recursively inspected.

    If permissions is non-None, then the paths are considered insecure, and
    run in a sandbox with only the granted permissions.  If permissions is
    None, then the paths are considered to be secure, and are run in-memory
    with the current extension loader.
    """
    __slots__ = ('_finders', '_cache', '_allow_secure', '_permissions')

    def __init__(
            self,
            cache: ExtensionStorageCache, paths: Sequence[str],
            permissions: Optional[Sequence[SandboxPermission]]
    ) -> None:
        """
        :param allows_secure bool: If True, then the extensions can be marked
            as secure if and only if the zip has an verified PGP signature
            file.  If this is False, then even if the PGP signature is verified,
            it will be marked as insecure.
        """
        self._cache = cache
        # Allow directories to be created after the fact.
        self._paths = tuple(paths)
        self._allow_secure = permissions is None

        # TODO use the permissions
        self._permissions = permissions

    def find_versions(self, name: str) -> Sequence[SecureExtensionVersion]:
        # filename pattern is "name-1.2.3.zip"
        find_prefix = name + '-'
        ret: List[SecureExtensionVersion] = []
        for path in self._paths:
            if not os.path.isdir(path):
                continue
            cache = self._cache.get_sub_cache(path)
            for fname in os.listdir(path):
                if not fname.startswith(find_prefix):
                    continue
                filename = os.path.join(path, fname)
                cached = _get_cached_data_for(filename, fname, cache)
                if _is_cached_valid_format(cached):
                    version = _get_cached_version(cached)
                    # Only allow the version to be secure if it's marked as
                    # secure, and this loader allows them to be marked as
                    # secure.
                    ret.append((version[0] and self._allow_secure, version[1]))
        return tuple(ret)

    def find_extension(
            self,
            only_secure: bool,
            name: str,
            version: ExtensionVersion
    ) -> Optional[DiscoveredExtension]:
        fname = '{0}-{1}.{2}.{3}.zip'.format(name, version[0], version[1], version[2])
        for path in self._paths:
            if not os.path.isdir(path):
                continue
            filename = os.path.join(path, fname)
            if not os.path.isfile(filename):
                continue
            cached = _get_cached_data_for(
                filename, fname,
                self._cache.get_sub_cache(path)
            )
            return _load_cached_extension(filename, fname, cached)
        return None


# Cached Index value meaning.
_CHI_CACHE_VERSION = 0
_CHI_ZIP_LENGTH = 1
_CHI_MD2_256 = 2
_CHI_MD3_256 = 3
_CHI_SIGNED = 4 # "t" if signed
_CHI_VALID = 5 # "t" if everything checks out
_CHI_NAME = 6
_CHI_VERSION_0 = 7
_CHI_VERSION_1 = 8
_CHI_VERSION_2 = 9
_CHI_JSON_METADATA = 10
_CHI_CHECKED_YEAR = 11
_CHI_CHECKED_MONTH = 12
_CHI_CHECKED_DAY = 13
_CHI_CHECKED_HOUR = 14
_CHI_CHECKED_MINUTE = 15
_CHI_CHECKED_SECOND = 16
_CH_INDEX_COUNT = 17
_CH_CURRENT_CACHE_VERSION = "0"

def _mk_cached_sequence(
        extension_name: str,
        version: ExtensionVersion,
        file_size: int,
        md2_256: str,
        md3_256: str,
        signed: bool,
        valid: bool,
        json_metadata: str,
        checked_date: datetime.datetime
) -> Sequence[str]:
    return (
        _CH_CURRENT_CACHE_VERSION,
        str(file_size),
        md2_256,
        md3_256,
        _bool_as_str(signed),
        _bool_as_str(valid),
        extension_name,
        str(version[0]),
        str(version[1]),
        str(version[2]),
        json_metadata,
        str(checked_date.year),
        str(checked_date.month),
        str(checked_date.day),
        str(checked_date.hour),
        str(checked_date.minute),
        str(checked_date.second),
    )

def _bool_as_str(v: bool) -> str:
    if v:
        return 't'
    return 'f'

def _is_cached_valid_format(cached: Sequence[str]) -> bool:
    return (
        len(cached) == _CH_INDEX_COUNT
        and cached[_CHI_CACHE_VERSION] == _CH_CURRENT_CACHE_VERSION
        and cached[_CHI_VALID] == 't'
    )

def _cached_check_date(cached: Sequence[str]) -> datetime.datetime:
    year = int(cached[_CHI_CHECKED_YEAR])
    month = int(cached[_CHI_CHECKED_MONTH])
    day = int(cached[_CHI_CHECKED_DAY])
    hour = int(cached[_CHI_CHECKED_HOUR])
    minute = int(cached[_CHI_CHECKED_MINUTE])
    second = int(cached[_CHI_CHECKED_SECOND])
    return datetime.datetime(
        year, month, day, hour, minute, second
    )

def _get_cached_data_for(
        filename: str,
        entry_name: str,
        cache: ExtensionStorageCache
) -> Sequence[str]:
    if cache.has_cache_for(entry_name):
        cached = cache.get_cached_data(entry_name)
        if _is_same(filename, cached):
            return cached or STRING_EMPTY_TUPLE
        # otherwise refresh the cache.
    evinfo = _get_filename_extension_version(filename)
    if evinfo is None:
        # Cannot find out accurate information.  Return
        # without performing the full check.
        log(
            WARN, ZipExtensionLoader,
            'invalid filename format: {0}',
            filename
        )
        return _mk_cached_sequence(
            extension_name='<invalid filename>',
            version=ANY_VERSION,
            file_size=-1,
            md2_256='',
            md3_256='',
            signed=False,
            valid=False,
            json_metadata='',
            checked_date=datetime.datetime.min
        )
    extension_name, version = evinfo
    now = datetime.datetime.utcnow()
    file_size, actual_hashes, expected_hashes = check_file_hashes(filename, PETRONIA_HASHES)
    if not expected_hashes:
        # Not enough expected hash digest files.
        # Cannot use this.
        log(
            WARN, ZipExtensionLoader,
            'not enough hash digest files for {0}; expected at least one of {1}',
            filename,
            ', '.join(PETRONIA_HASHES.values())
        )
        return _mk_cached_sequence(
            extension_name=extension_name,
            version=version,
            file_size=file_size,
            md2_256='',
            md3_256='',
            signed=False,
            valid=False,
            json_metadata='',
            checked_date=now
        )
    mismatched_hashes = get_mismatched_hashes(actual_hashes, expected_hashes)
    if mismatched_hashes:
        log(
            WARN, ZipExtensionLoader,
            'mismatched hash digest(s) for {0}: {1}',
            filename,
            ', '.join(mismatched_hashes.keys())
        )
        return _mk_cached_sequence(
            extension_name=extension_name,
            version=version,
            file_size=file_size,
            md2_256=in_or(actual_hashes, HASH_SHA2_256, ''),
            md3_256=in_or(actual_hashes, HASH_SHA3_256, ''),
            signed=False,
            valid=False,
            json_metadata='',
            checked_date=now
        )
    signing_state = file_signature_state(filename)
    signed = signing_state == SIGNED
    metadata = read_zipfile_metadata_contents(filename)
    # NOTE: "valid" here doesn't ensure the metadata is valid, only the
    # rest of the stuff around it.
    return _mk_cached_sequence(
        extension_name=extension_name,
        version=version,
        file_size=file_size,
        md2_256=in_or(actual_hashes, HASH_SHA2_256, ''),
        md3_256=in_or(actual_hashes, HASH_SHA3_256, ''),
        signed=signed,
        valid=True,
        json_metadata=metadata or '',
        checked_date=now
    )

def _load_cached_extension(
        filename: str, entry_name: str, cached: Sequence[str]
) -> Optional[DiscoveredExtension]:
    # Because this extension might be insecure, do not actually load the
    # module into memory yet.  Instead, just load the metadata.  The
    # returned object will perform the right invocation to optionally run
    # it in a remote process, or load it in memory.
    # It will also need the snadbox permissions.
    raise NotImplementedError()

def _is_same(filename: str, cached: Optional[Sequence[str]]) -> bool:
    """
    Is the current extension file `filename` still the same as the cached version?
    This is a quick check on the checksums.
    """
    if not cached:
        return False
    if not _is_cached_valid_format(cached):
        return False

    # TODO implement
    # Without this, the cache is useless.
    return False

def _get_cached_version(cached: Sequence[str]) -> SecureExtensionVersion:
    """Assumes "cached" is a valid formatted cached sequence."""
    secure = cached[_CHI_SIGNED] == "t"
    ver0 = int(cached[_CHI_VERSION_0])
    ver1 = int(cached[_CHI_VERSION_1])
    ver2 = int(cached[_CHI_VERSION_2])
    return (secure, (ver0, ver1, ver2,),)

_FILENAME_VERSION_PATTERN = re.compile(r'^([^-]+)-(\d+)\.(\d+)\.(\d+)\.zip')

def _get_filename_extension_version(filename: str) -> Optional[Tuple[str, ExtensionVersion]]:
    """
    Extracts the extension and version from the file name.
    """
    name = os.path.basename(filename)
    match = _FILENAME_VERSION_PATTERN.match(name)
    if not match:
        return None
    return (
        match.group(1),
        (
            int(match.group(2)),
            int(match.group(3)),
            int(match.group(4)),
        ),
    )
