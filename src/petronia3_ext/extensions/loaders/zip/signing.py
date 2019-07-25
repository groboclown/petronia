
"""
Helpers for checking the PGP signing of files.
"""

import os
from typing import NewType
from petronia3.system.security import is_file_signature_validation_available
from petronia3.system.logging import (
    log, WARN,
)
from .checksum import (
    check_file_hashes,
    get_mismatched_hashes,
    PETRONIA_HASHES,
)

SIGNED_EXTENSION = '.asc'

SignatureState = NewType('SignatureState', str)
SIGNED = SignatureState('signed')
NO_SIGNATURE = SignatureState('not-signed')
SIGNATURE_FILE_BAD_DIGEST = SignatureState('signature-file-bad-digest')
SIGNATURE_CHECK_NOT_SUPPORTED = SignatureState('signature-check-not-supported')


def file_signature_state(filename: str) -> SignatureState:
    signed_filename = filename + SIGNED_EXTENSION
    if not os.path.isfile(signed_filename):
        log(
            WARN, file_signature_state,
            '{0} has no signature file; expected it to be named {1}',
            filename, signed_filename
        )
        return NO_SIGNATURE
    file_size, actual_hashes, expected_hashes = check_file_hashes(signed_filename, PETRONIA_HASHES)
    if file_size <= 0:
        # empty signature is just as good as no signature
        log(
            WARN, file_signature_state,
            '{0} has an empty signature file {1}',
            filename, signed_filename
        )
        return NO_SIGNATURE
    if not actual_hashes:
        log(
            WARN, file_signature_state,
            '{0} has signature file {1}, but no digest for the '
            'signature file.  At least one must be present of {2}',
            filename, signed_filename,
            ', '.join(PETRONIA_HASHES.keys())
        )
        return SIGNATURE_FILE_BAD_DIGEST
    mismatched_hashes = get_mismatched_hashes(actual_hashes, expected_hashes)
    if mismatched_hashes:
        log(
            WARN, file_signature_state,
            '{0} has signature file {1} with mismatched digests for {2}',
            filename, signed_filename,
            ', '.join(mismatched_hashes.keys())
        )
        return SIGNATURE_FILE_BAD_DIGEST

    # The signing file exists with valid hash digest files.
    if not is_file_signature_validation_available(signed_filename):
        log(
            WARN, file_signature_state,
            '{0} has signature file {1}, but signing is not supported '
            'for that signing type.',
            filename, signed_filename
        )
        return SIGNATURE_CHECK_NOT_SUPPORTED

    # Checking the signature isn't supported yet.
    raise NotImplementedError()
