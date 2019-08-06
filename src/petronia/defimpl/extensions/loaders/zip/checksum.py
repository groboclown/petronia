
"""
General checksum / hash digest functions.
"""

import os
import hashlib
from typing import Tuple, Sequence, List, Dict

# length, hex digest for each hash algorithm, in requested order.
HashResult = Tuple[int, Dict[str, str]]


HASH_SHA2_256 = 'sha256'
HASH_SHA3_256 = 'sha3-256'
PETRONIA_HASHES = {
    HASH_SHA3_256: '.sha3-256',
    HASH_SHA2_256: '.sha256',
}

_MAXIMUM_HASH_SIZE = 1024 * 10 # 10k
_BUFFER_SIZE = 1024 * 10

def load_hashes(
        filename: str, hash_algorithm_names: Sequence[str]
) -> HashResult:
    """
    Load the size and hash hex digests for the given file.
    """

    # See https://github.com/python/typeshed/issues/2928
    hashes: List['hashlib._hashlib._HASH'] = [] # type: ignore

    for name in hash_algorithm_names:
        hashes.append(hashlib.new(name))
    size = 0
    with open(filename, 'rb') as inp:
        data = inp.read(_BUFFER_SIZE)
        for hashf in hashes:
            hashf.update(data)
        size += len(data)
    digests: Dict[str, str] = {}
    for idx in range(len(hash_algorithm_names)):
        hash_name = hash_algorithm_names[idx]
        hashf = hashes[idx]
        digests[hash_name] = hashf.hexdigest() # type: ignore
    return (size, digests)

FileHashResult = Tuple[int, Dict[str, str], Dict[str, str]]

def check_file_hashes(
        base_filename: str,
        hash_algorithm_extension: Dict[str, str]
) -> FileHashResult:
    """
    Load the hashes for the file, just like load_hashes, but also find the
    contents of the corresponding hash storage file.  For example, if
    base file `a.zip` has file `a.zip.md5`, and the hash extension algorithm
    contains `"md5": ".md5"`, then the `a.zip.md5` contents are loaded into
    the returned third argument, and the base file's md5 hex digest is loaded
    into the second argument's data.  If the digest file doesn't exist or
    couldn't be read, then the corresponding entry in the content is
    an empty string.

    To see if a hex digest doesn't match compare returned `[1][x]` against
    `[2][x]`, where "x" is the digest name, not the extension name.
    """
    algorithms = tuple(hash_algorithm_extension.keys())
    loaded = load_hashes(base_filename, algorithms)
    file_contents: Dict[str, str] = {}
    for hash_name, ext in hash_algorithm_extension.items():
        fname = base_filename + ext
        if os.path.isfile(fname):
            try:
                statinfo = os.stat(fname)
                if statinfo.st_size > _MAXIMUM_HASH_SIZE:
                    file_contents[hash_name] = ''
                else:
                    with open(fname, 'r') as inp:
                        file_contents[hash_name] = inp.read().strip()
            except: # pylint: disable=bare-except
                # We're okay to skip error reporting, because it's an
                # acceptable state.
                file_contents[hash_name] = ''
        else:
            file_contents[hash_name] = ''
    return (loaded[0], loaded[1], file_contents)


def get_mismatched_hashes(
        actual: Dict[str, str], expected: Dict[str, str]
) -> Dict[str, Tuple[str, str]]:
    """
    Returns all the hashes that didn't match up.  The returned value is the
    hash algorithm name mapped to the tuple `(actual, expected)`.  Any actual
    hashes not in the expected list are ignored.  Any expected hashes not in
    the actual list are marked as an error, with the actual value set to an
    empty string.  If the expected value is an empty string, then the actual
    value is ignored, even if it doesn't exist.
    """
    ret: Dict[str, Tuple[str, str]] = {}
    for hash_name, expected_digest in expected.items():
        if not expected_digest:
            continue
        actual_digest = ''
        if hash_name in actual:
            actual_digest = actual[hash_name]
        if expected_digest != actual_digest:
            ret[hash_name] = (actual_digest, expected_digest,)
    return ret
