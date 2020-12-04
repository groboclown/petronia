
"""
Handles writing packets to a binary asyncio stream.
"""

# This file is an exception for many of the "code simplification" rules,
# because it is a big state handling tool.
# pylint: disable=R0911
# pylint: disable=R0913
# pylint: disable=R0914

from typing import Union, Protocol
import json
from . import consts
from .defs import RawBinaryReader, MarshalledEventObject
from ..util import StdRet, enforce_all, RET_OK_NONE, STANDARD_PETRONIA_CATALOG
from ..util import i18n as _


class BinaryWriter(Protocol):
    """A protocol for what the event writer needs.  Just a simple
    write method that takes bytes.  The writer doesn't need to be
    an async writer or any other fancy thing."""

    def write(self, data: bytes) -> None: ...  # pylint: disable=C0116  # pragma no cover


def write_binary_event_to_stream(
        stream: BinaryWriter,
        event_id: str,
        source_id: str,
        target_id: str,
        binary_blob_size: int,
        binary_blob: Union[bytes, RawBinaryReader],
) -> StdRet[None]:
    """
    The rigorous event writing routine.  It strongly enforces the
    stream writing rules.

    :param stream:
    :param event_id:
    :param source_id:
    :param target_id:
    :param binary_blob_size:
    :param binary_blob:
    :return:
    """

    if isinstance(binary_blob, bytes) and len(binary_blob) != binary_blob_size:
        return StdRet.pass_errmsg(
            STANDARD_PETRONIA_CATALOG,
            _('binary_blob has {real_size} bytes, but requested {expected_size}'),
            real_size=len(binary_blob),
            expected_size=binary_blob_size,
        )
    try:
        encoded_event_id = event_id.encode('utf-8')
    except UnicodeEncodeError as exp:
        return StdRet.pass_exception(
            _('event-id UTF-8 encoding problem: {exception}'), exp, event_id=event_id,
        )
    encoded_event_id_len = len(encoded_event_id)
    try:
        encoded_source_id = source_id.encode('utf-8')
    except UnicodeEncodeError as exp:
        return StdRet.pass_exception(
            _('source-id UTF-8 encoding problem: {exception}'), exp, source_id=source_id,
        )
    encoded_source_id_len = len(encoded_source_id)
    try:
        encoded_target_id = target_id.encode('utf-8')
    except UnicodeEncodeError as exp:
        return StdRet.pass_exception(
            _('target-id UTF-8 encoding problem: {exception}'), exp, target_id=target_id,
        )
    encoded_target_id_len = len(encoded_target_id)

    ret = enforce_all(
        'write_binary_event_to_stream',
        (
            _('event-id length must be within [{id_min}, {id_max}]'),
            lambda: consts.MIN_ID_SIZE <= encoded_event_id_len <= consts.MAX_ID_SIZE,
        ),
        (
            _('source-id length must be within [{id_min}, {id_max}]'),
            lambda: consts.MIN_ID_SIZE <= encoded_source_id_len <= consts.MAX_ID_SIZE,
        ),
        (
            _('target-id length must be within [{id_min}, {id_max}]'),
            lambda: consts.MIN_ID_SIZE <= encoded_target_id_len <= consts.MAX_ID_SIZE,
        ),
        (
            _('binary event data size must be within [{b_min}, {b_max}]'),
            lambda: consts.MIN_BLOB_SIZE <= binary_blob_size <= consts.MAX_BLOB_SIZE,
        ),
        id_min=consts.MIN_ID_SIZE,
        id_max=consts.MAX_ID_SIZE,
        b_min=consts.MIN_BLOB_SIZE,
        b_max=consts.MAX_BLOB_SIZE,
    )
    if ret:
        return StdRet.pass_error(ret)

    packet_envelope = bytearray((
        consts.BINARY_PACKET_MARKER_1_INT,
        consts.BINARY_PACKET_MARKER_2_INT,
        consts.BINARY_PACKET_MARKER_3_INT,

        consts.BINARY_EVENT_ID_MARKER_INT,
        (encoded_event_id_len >> 8) & 0xff,
        encoded_event_id_len & 0xff,
        *encoded_event_id,

        consts.BINARY_SOURCE_ID_MARKER_INT,
        (encoded_source_id_len >> 8) & 0xff,
        encoded_source_id_len & 0xff,
        *encoded_source_id,

        consts.BINARY_TARGET_ID_MARKER_INT,
        (encoded_target_id_len >> 8) & 0xff,
        encoded_target_id_len & 0xff,
        *encoded_target_id,

        consts.BINARY_BLOB_CONTENTS_MARKER_INT,
        (binary_blob_size >> 16) & 0xff,
        (binary_blob_size >> 8) & 0xff,
        binary_blob_size & 0xff,
    ))
    stream.write(packet_envelope)
    if isinstance(binary_blob, bytes):
        stream.write(binary_blob)
    else:
        remaining = binary_blob_size
        while remaining > 0:
            data = binary_blob(MAX_READ_SIZE)
            if not data:
                # fill in the rest of the packet data to avoid
                # stream errors
                stream.write(b' ' * remaining)
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('binary blob data less than requested size'),
                )

            remaining -= len(data)
            stream.write(data)

    return RET_OK_NONE


def write_object_event_to_stream(
        stream: BinaryWriter,
        event_id: str,
        source_id: str,
        target_id: str,
        event_object: MarshalledEventObject,
) -> StdRet[None]:
    """
    The rigorous event writing routine.  It strongly enforces the
    stream writing rules.

    This does not strictly need to be async, but it is done so for
    symmetry with the other writer.

    :param event_object:
    :param stream:
    :param event_id:
    :param source_id:
    :param target_id:
    :return:
    """

    try:
        encoded_event_object = json.dumps(
            event_object,
            separators=(',', ':'),
            sort_keys=True,
        ).encode('utf-8')
    except UnicodeEncodeError as exp:  # pragma no cover
        # Due to the "dumps" method, this shouldn't ever be reached.
        # But, just in case...
        return StdRet.pass_exception(  # pragma no cover
            _('event object data UTF-8 encoding problem: {exception}'), exp,
        )
    except TypeError as exp:
        return StdRet.pass_exception(
            _('event object data cannot be marshalled: {exception}'), exp,
        )
    encoded_event_object_len = len(encoded_event_object)
    try:
        encoded_event_id = event_id.encode('utf-8')
    except UnicodeEncodeError as exp:
        return StdRet.pass_exception(
            _('event-id UTF-8 encoding problem: {exception}'), exp, event_id=event_id,
        )
    encoded_event_id_len = len(encoded_event_id)
    try:
        encoded_source_id = source_id.encode('utf-8')
    except UnicodeEncodeError as exp:
        return StdRet.pass_exception(
            _('source-id UTF-8 encoding problem: {exception}'), exp, source_id=source_id,
        )
    encoded_source_id_len = len(encoded_source_id)
    try:
        encoded_target_id = target_id.encode('utf-8')
    except UnicodeEncodeError as exp:
        return StdRet.pass_exception(
            _('target-id UTF-8 encoding problem: {exception}'), exp, target_id=target_id,
        )
    encoded_target_id_len = len(encoded_target_id)

    ret = enforce_all(
        'write_binary_event_to_stream',
        (
            _('event-id length must be within [{id_min}, {id_max}]'),
            lambda: consts.MIN_ID_SIZE <= encoded_event_id_len <= consts.MAX_ID_SIZE,
        ),
        (
            _('source-id length must be within [{id_min}, {id_max}]'),
            lambda: consts.MIN_ID_SIZE <= encoded_source_id_len <= consts.MAX_ID_SIZE,
        ),
        (
            _('target-id length must be within [{id_min}, {id_max}]'),
            lambda: consts.MIN_ID_SIZE <= encoded_target_id_len <= consts.MAX_ID_SIZE,
        ),
        (
            _('event object data size must be within [{b_min}, {b_max}]'),
            lambda: consts.MIN_JSON_SIZE <= encoded_event_object_len <= consts.MAX_JSON_SIZE,
        ),
        id_min=consts.MIN_ID_SIZE,
        id_max=consts.MAX_ID_SIZE,
        b_min=consts.MIN_JSON_SIZE,
        b_max=consts.MAX_JSON_SIZE,
    )
    if ret:
        return StdRet.pass_error(ret)

    packet_envelope = bytearray((
        consts.BINARY_PACKET_MARKER_1_INT,
        consts.BINARY_PACKET_MARKER_2_INT,
        consts.BINARY_PACKET_MARKER_3_INT,

        consts.BINARY_EVENT_ID_MARKER_INT,
        (encoded_event_id_len >> 8) & 0xff,
        encoded_event_id_len & 0xff,
        *encoded_event_id,

        consts.BINARY_SOURCE_ID_MARKER_INT,
        (encoded_source_id_len >> 8) & 0xff,
        encoded_source_id_len & 0xff,
        *encoded_source_id,

        consts.BINARY_TARGET_ID_MARKER_INT,
        (encoded_target_id_len >> 8) & 0xff,
        encoded_target_id_len & 0xff,
        *encoded_target_id,

        consts.BINARY_JSON_CONTENTS_MARKER_INT,
        (encoded_event_object_len >> 8) & 0xff,
        encoded_event_object_len & 0xff,
    ))
    stream.write(packet_envelope)
    stream.write(encoded_event_object)

    return RET_OK_NONE


MAX_READ_SIZE = 64 * 1024
