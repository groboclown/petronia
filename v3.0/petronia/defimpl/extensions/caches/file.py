
"""
File-based cache.
"""

import os
import json
from typing import Dict, List, Sequence, Optional, Any
from threading import Lock
from ....errors import PetroniaFileError
from ..defs import ExtensionStorageCache


class DirectoryExtensionCache(ExtensionStorageCache):
    """
    Stores the cached extension information in a cache directory.
    """
    __slots__ = ('__dir', '_sub', '_indicies', '__lock', '_top')
    _sub: Dict[str, ExtensionStorageCache]
    _indicies: Dict[str, str]

    def __init__(self, cache_dir: str) -> None:
        if not os.path.isdir(cache_dir):
            raise PetroniaFileError(cache_dir, 'is not a directory')
        self.__lock = Lock()
        self.__dir = cache_dir
        self._indicies = DirectoryExtensionCache._load_index(cache_dir)
        self._sub = {}
        self._top = self.get_sub_cache('__top__')

    def has_cache_for(self, extension: str) -> bool:
        return self._top.has_cache_for(extension)

    def get_cached_data(self, extension: str) -> Optional[Sequence[str]]:
        return self._top.get_cached_data(extension)

    def set_cached_data(self, extension: str, data: Sequence[str]) -> None:
        self._top.set_cached_data(extension, data)

    def get_sub_cache(self, sub_name: str) -> ExtensionStorageCache:
        # NOTE: file I/O + thread lock = really bad idea.
        with self.__lock:
            if sub_name in self._sub:
                return self._sub[sub_name]
            if sub_name not in self._indicies:
                fname = self._unique_filename_for_sub(sub_name)
                self._indicies[sub_name] = fname
                self._save_index()
            sub_file = os.path.join(self.__dir, self._indicies[sub_name])
            sub = FileExtensionCache(sub_file, self)
            self._sub[sub_name] = sub
            return sub

    def clear_cache(self) -> None:
        # NOTE: file I/O + thread lock = really bad idea.
        with self.__lock:
            for sub in self._sub.values():
                sub.clear_cache()
            for fname in self._indicies.values():
                name = os.path.join(self.__dir, fname)
                if os.path.isfile(name):
                    os.unlink(name)
            index_file = os.path.join(self.__dir, 'index.json')
            if os.path.isfile(index_file):
                os.unlink(index_file)
            self._indicies = {}
            self._sub = {}

    def _unique_filename_for_sub(self, sub_name: str) -> str:
        index = 0
        fname = DirectoryExtensionCache._encode_sub_name_as_file(sub_name, index)
        while fname in self._indicies.values():
            index += 1
            fname = DirectoryExtensionCache._encode_sub_name_as_file(sub_name, index)
        return fname

    @staticmethod
    def _encode_sub_name_as_file(sub_name: str, index: int) -> str:
        ret = ''
        for insp in sub_name:
            if insp.isalnum():
                ret += insp
            else:
                ret += '_'
        return '{0}-{1}.json'.format(ret, index)

    def _save_index(self) -> None:
        index_file = os.path.join(self.__dir, 'index.json')
        with open(index_file, 'w') as out:
            json.dump(self._indicies, out)

    @staticmethod
    def _load_index(cache_dir: str) -> Dict[str, str]:
        index_file = os.path.join(cache_dir, 'index.json')
        ret: Dict[str, str] = {}
        if os.path.isfile(index_file):
            with open(index_file, 'r') as inp:
                contents = json.load(inp) # type: ignore
            if isinstance(contents, dict): # type: ignore
                for key, val in contents.items():
                    if isinstance(key, str) and isinstance(key, val):
                        ret[key] = val
        return ret


class FileExtensionCache(ExtensionStorageCache):
    """
    A single cache that's used by the directory.
    """
    __slots__ = ('__index', '__parent', '_data', '__lock')
    _data: Dict[str, Sequence[str]]

    def __init__(self, index_file: str, parent: ExtensionStorageCache) -> None:
        self.__lock = Lock()
        self.__index = index_file
        self.__parent = parent
        self._data = FileExtensionCache._load_data(index_file)

    def has_cache_for(self, extension: str) -> bool:
        with self.__lock:
            return extension in self._data

    def get_cached_data(self, extension: str) -> Optional[Sequence[str]]:
        with self.__lock:
            if extension in self._data:
                return self._data[extension]
        return None

    def set_cached_data(self, extension: str, data: Sequence[str]) -> None:
        # NOTE: file I/O + thread lock = really bad idea.
        with self.__lock:
            self._data[extension] = data
            self._save_cache()

    def get_sub_cache(self, sub_name: str) -> ExtensionStorageCache:
        return self.__parent.get_sub_cache(sub_name)

    def clear_cache(self) -> None:
        # NOTE: file I/O + thread lock = really bad idea.
        with self.__lock:
            self._data = {}
            if os.path.isfile(self.__index):
                os.unlink(self.__index)

    def _save_cache(self) -> None:
        with open(self.__index, 'w') as out:
            json.dump(self._data, out)

    @staticmethod
    def _load_data(fname: str) -> Dict[str, Sequence[str]]:
        data: Dict[str, Sequence[str]] = {}
        if os.path.exists(fname):
            # Note the "exists" here.  In this way, we check that
            # it's a file (and not a directory or pipe or something else)
            with open(fname, 'r') as inp:
                contents = json.load(inp) # type: ignore
            FileExtensionCache._parsed_contents(contents, data) # type: ignore
        return data

    @staticmethod
    def _parsed_contents(contents: Any, data: Dict[str, Sequence[str]]) -> None: # type: ignore
        if isinstance(contents, dict): # type: ignore
            for key, seqval in contents.items():
                if isinstance(key, str) and (isinstance(seqval, list) or isinstance(seqval, tuple)):
                    dval: List[str] = []
                    for val in seqval:
                        if isinstance(val, str):
                            dval.append(val)
                    data[key] = dval
