# GENERATED FILE.  DO NOT EDIT

from typing import Dict, Mapping, Sequence, BinaryIO, NewType, Union, Callable, Optional, Any
import ctypes
from ..packet import (
    DataPacket,
    FixedDataPacketField, SimpleListDataPacketField,
    FixedPadDataPacketField, AlignedPadDataPacketField,
    StructureDataPacketField, ListDataPacketField,
    BitDataPacketField, UnionDataPacketField,
    MARKER_PAD, MARKER_INT8, MARKER_UINT8, MARKER_INT16,
    MARKER_UINT16, MARKER_INT32, MARKER_UINT32, MARKER_INT64,
    MARKER_UINT64, MARKER_FLOAT32, MARKER_FLOAT64, MARKER_FLEXIBLE,
) 

# ------------------------------------------------------------------
# Enums

GetDocType = NewType('GetDocType', int)


class GetDocValues:
    FINISHED = GetDocType(0)
    SECOND_CONSUMER = GetDocType(1)


EvMaskType = NewType('EvMaskType', int)


class EvMaskValues:
    NO_EVENT_MASK = EvMaskType(0)
    PRINT_MASK = EvMaskType(1)
    ATTRIBUTE_MASK = EvMaskType(2)


DetailType = NewType('DetailType', int)


class DetailValues:
    START_JOB_NOTIFY = DetailType(1)
    END_JOB_NOTIFY = DetailType(2)
    START_DOC_NOTIFY = DetailType(3)
    END_DOC_NOTIFY = DetailType(4)
    START_PAGE_NOTIFY = DetailType(5)
    END_PAGE_NOTIFY = DetailType(6)


AttrType = NewType('AttrType', int)


class AttrValues:
    JOB_ATTR = AttrType(1)
    DOC_ATTR = AttrType(2)
    PAGE_ATTR = AttrType(3)
    PRINTER_ATTR = AttrType(4)
    SERVER_ATTR = AttrType(5)
    MEDIUM_ATTR = AttrType(6)
    SPOOLER_ATTR = AttrType(7)


# ------------------------------------------------------------------
# Aliases

Pcontext = NewType('Pcontext', ctypes.c_uint32)


# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


PrinterStructPacket = DataPacket((
    ('nameLen', FixedDataPacketField(MARKER_UINT32)),
    ('name', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nameLen'], 0)),
    ('pad0', AlignedPadDataPacketField(4)),
    ('descLen', FixedDataPacketField(MARKER_UINT32)),
    ('description', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['descLen'], 0)),
    ('pad1', AlignedPadDataPacketField(4)),
))


class PrinterStruct:
    __slots__ = ('namelen', 'name', 'desclen', 'description',)

    def __init__(
            self, *,
            namelen: Optional[int] = None,
            name: Optional[Sequence[int]] = None,
            desclen: Optional[int] = None,
            description: Optional[Sequence[int]] = None,
    ) -> None:
        self.namelen = namelen
        self.name = name
        self.desclen = desclen
        self.description = description

    def as_dict(self) -> Dict[str, Any]:
        return {
            'nameLen': self.namelen,
            'name': self.name,
            'descLen': self.desclen,
            'description': self.description,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrinterStruct':
        return PrinterStruct(**PrinterStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrinterStructPacket.pack(**self.as_dict())


class PrinterStructCType(ctypes.Structure):
    """xprint PRINTER"""
    _fields_ = [
        ("nameLen", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


PrintQueryVersionRequestCookie = NewType('PrintQueryVersionRequestCookie', ctypes.c_uint32)


PrintQueryVersionRequestPacket = DataPacket((
))


class PrintQueryVersionRequest:
    OPCODE = 0

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintQueryVersionRequest':
        return PrintQueryVersionRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], PrintQueryVersionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintQueryVersionRequest.lib = library.xprint_printqueryversion
        PrintQueryVersionRequest.lib.restype = PrintQueryVersionRequestCookie
        PrintQueryVersionRequest.lib.argstype = ()


class PrintQueryVersionRequestCType(ctypes.Structure):
    """xprint PrintQueryVersion"""
    _fields_ = [
    ]


PrintQueryVersionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('major_version', FixedDataPacketField(MARKER_UINT16)),
    ('minor_version', FixedDataPacketField(MARKER_UINT16)),
))


class PrintQueryVersionReplyReply:
    __slots__ = ('major_version', 'minor_version',)

    def __init__(
            self, *,
            major_version: Optional[int] = None,
            minor_version: Optional[int] = None,
    ) -> None:
        self.major_version = major_version
        self.minor_version = minor_version

    def as_dict(self) -> Dict[str, Any]:
        return {
            'major_version': self.major_version,
            'minor_version': self.minor_version,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintQueryVersionReplyReply':
        return PrintQueryVersionReplyReply(**PrintQueryVersionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintQueryVersionReplyReplyPacket.pack(**self.as_dict())


class PrintQueryVersionReplyReplyCType(ctypes.Structure):
    """xprint PrintQueryVersion_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("major_version", ctypes.c_uint16),
        ("minor_version", ctypes.c_uint16),
    ]


PrintGetPrinterListRequestCookie = NewType('PrintGetPrinterListRequestCookie', ctypes.c_uint32)


PrintGetPrinterListRequestPacket = DataPacket((
    ('printerNameLen', FixedDataPacketField(MARKER_UINT32)),
    ('localeLen', FixedDataPacketField(MARKER_UINT32)),
    ('printer_name', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['printerNameLen'], 0)),
    ('pad0', AlignedPadDataPacketField(4)),
    ('locale', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['localeLen'], 0)),
))


class PrintGetPrinterListRequest:
    OPCODE = 1

    __slots__ = ('printernamelen', 'localelen', 'printer_name', 'locale',)

    def __init__(
            self, *,
            printernamelen: Optional[int] = None,
            localelen: Optional[int] = None,
            printer_name: Optional[Sequence[int]] = None,
            locale: Optional[Sequence[int]] = None,
    ) -> None:
        self.printernamelen = printernamelen
        self.localelen = localelen
        self.printer_name = printer_name
        self.locale = locale

    def as_dict(self) -> Dict[str, Any]:
        return {
            'printerNameLen': self.printernamelen,
            'localeLen': self.localelen,
            'printer_name': self.printer_name,
            'locale': self.locale,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintGetPrinterListRequest':
        return PrintGetPrinterListRequest(**PrintGetPrinterListRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintGetPrinterListRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int], Sequence[int]], PrintGetPrinterListRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintGetPrinterListRequest.lib = library.xprint_printgetprinterlist
        PrintGetPrinterListRequest.lib.restype = PrintGetPrinterListRequestCookie
        PrintGetPrinterListRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)


class PrintGetPrinterListRequestCType(ctypes.Structure):
    """xprint PrintGetPrinterList"""
    _fields_ = [
        ("printerNameLen", ctypes.c_uint32),
        ("localeLen", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


PrintGetPrinterListReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('listCount', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('printers', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['listCount'], 0)),
))


class PrintGetPrinterListReplyReply:
    __slots__ = ('listcount', 'printers',)

    def __init__(
            self, *,
            listcount: Optional[int] = None,
            printers: Optional[Sequence[int]] = None,
    ) -> None:
        self.listcount = listcount
        self.printers = printers

    def as_dict(self) -> Dict[str, Any]:
        return {
            'listCount': self.listcount,
            'printers': self.printers,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintGetPrinterListReplyReply':
        return PrintGetPrinterListReplyReply(**PrintGetPrinterListReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintGetPrinterListReplyReplyPacket.pack(**self.as_dict())


class PrintGetPrinterListReplyReplyCType(ctypes.Structure):
    """xprint PrintGetPrinterList_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("listCount", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


PrintRehashPrinterListRequestPacket = DataPacket((
))


class PrintRehashPrinterListRequest:
    OPCODE = 20

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintRehashPrinterListRequest':
        return PrintRehashPrinterListRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintRehashPrinterListRequest.lib = library.xprint_printrehashprinterlist
        PrintRehashPrinterListRequest.lib.restype = ctypes.c_uint32
        PrintRehashPrinterListRequest.lib.argstype = ()


class PrintRehashPrinterListRequestCType(ctypes.Structure):
    """xprint PrintRehashPrinterList"""
    _fields_ = [
    ]


CreateContextRequestPacket = DataPacket((
    ('context_id', FixedDataPacketField(MARKER_UINT32)),
    ('printerNameLen', FixedDataPacketField(MARKER_UINT32)),
    ('localeLen', FixedDataPacketField(MARKER_UINT32)),
    ('printerName', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['printerNameLen'], 0)),
    ('pad0', AlignedPadDataPacketField(4)),
    ('locale', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['localeLen'], 0)),
))


class CreateContextRequest:
    OPCODE = 2

    __slots__ = ('context_id', 'printernamelen', 'localelen', 'printername', 'locale',)

    def __init__(
            self, *,
            context_id: Optional[int] = None,
            printernamelen: Optional[int] = None,
            localelen: Optional[int] = None,
            printername: Optional[Sequence[int]] = None,
            locale: Optional[Sequence[int]] = None,
    ) -> None:
        self.context_id = context_id
        self.printernamelen = printernamelen
        self.localelen = localelen
        self.printername = printername
        self.locale = locale

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context_id': self.context_id,
            'printerNameLen': self.printernamelen,
            'localeLen': self.localelen,
            'printerName': self.printername,
            'locale': self.locale,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateContextRequest':
        return CreateContextRequest(**CreateContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, Sequence[int], Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateContextRequest.lib = library.xprint_createcontext
        CreateContextRequest.lib.restype = ctypes.c_uint32
        CreateContextRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)


class CreateContextRequestCType(ctypes.Structure):
    """xprint CreateContext"""
    _fields_ = [
        ("context_id", ctypes.c_uint32),
        ("printerNameLen", ctypes.c_uint32),
        ("localeLen", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


PrintSetContextRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
))


class PrintSetContextRequest:
    OPCODE = 3

    __slots__ = ('context',)

    def __init__(
            self, *,
            context: Optional[int] = None,
    ) -> None:
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintSetContextRequest':
        return PrintSetContextRequest(**PrintSetContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintSetContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintSetContextRequest.lib = library.xprint_printsetcontext
        PrintSetContextRequest.lib.restype = ctypes.c_uint32
        PrintSetContextRequest.lib.argstype = (ctypes.c_uint32,)


class PrintSetContextRequestCType(ctypes.Structure):
    """xprint PrintSetContext"""
    _fields_ = [
        ("context", ctypes.c_uint32),
    ]


PrintGetContextRequestCookie = NewType('PrintGetContextRequestCookie', ctypes.c_uint32)


PrintGetContextRequestPacket = DataPacket((
))


class PrintGetContextRequest:
    OPCODE = 4

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintGetContextRequest':
        return PrintGetContextRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], PrintGetContextRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintGetContextRequest.lib = library.xprint_printgetcontext
        PrintGetContextRequest.lib.restype = PrintGetContextRequestCookie
        PrintGetContextRequest.lib.argstype = ()


class PrintGetContextRequestCType(ctypes.Structure):
    """xprint PrintGetContext"""
    _fields_ = [
    ]


PrintGetContextReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('context', FixedDataPacketField(MARKER_UINT32)),
))


class PrintGetContextReplyReply:
    __slots__ = ('context',)

    def __init__(
            self, *,
            context: Optional[int] = None,
    ) -> None:
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintGetContextReplyReply':
        return PrintGetContextReplyReply(**PrintGetContextReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintGetContextReplyReplyPacket.pack(**self.as_dict())


class PrintGetContextReplyReplyCType(ctypes.Structure):
    """xprint PrintGetContext_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("context", ctypes.c_uint32),
    ]


PrintDestroyContextRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
))


class PrintDestroyContextRequest:
    OPCODE = 5

    __slots__ = ('context',)

    def __init__(
            self, *,
            context: Optional[int] = None,
    ) -> None:
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintDestroyContextRequest':
        return PrintDestroyContextRequest(**PrintDestroyContextRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintDestroyContextRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintDestroyContextRequest.lib = library.xprint_printdestroycontext
        PrintDestroyContextRequest.lib.restype = ctypes.c_uint32
        PrintDestroyContextRequest.lib.argstype = (ctypes.c_uint32,)


class PrintDestroyContextRequestCType(ctypes.Structure):
    """xprint PrintDestroyContext"""
    _fields_ = [
        ("context", ctypes.c_uint32),
    ]


PrintGetScreenOfContextRequestCookie = NewType('PrintGetScreenOfContextRequestCookie', ctypes.c_uint32)


PrintGetScreenOfContextRequestPacket = DataPacket((
))


class PrintGetScreenOfContextRequest:
    OPCODE = 6

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintGetScreenOfContextRequest':
        return PrintGetScreenOfContextRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], PrintGetScreenOfContextRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintGetScreenOfContextRequest.lib = library.xprint_printgetscreenofcontext
        PrintGetScreenOfContextRequest.lib.restype = PrintGetScreenOfContextRequestCookie
        PrintGetScreenOfContextRequest.lib.argstype = ()


class PrintGetScreenOfContextRequestCType(ctypes.Structure):
    """xprint PrintGetScreenOfContext"""
    _fields_ = [
    ]


PrintGetScreenOfContextReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
))


class PrintGetScreenOfContextReplyReply:
    __slots__ = ('root',)

    def __init__(
            self, *,
            root: Optional[int] = None,
    ) -> None:
        self.root = root

    def as_dict(self) -> Dict[str, Any]:
        return {
            'root': self.root,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintGetScreenOfContextReplyReply':
        return PrintGetScreenOfContextReplyReply(**PrintGetScreenOfContextReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintGetScreenOfContextReplyReplyPacket.pack(**self.as_dict())


class PrintGetScreenOfContextReplyReplyCType(ctypes.Structure):
    """xprint PrintGetScreenOfContext_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("root", ctypes.c_uint32),
    ]


PrintStartJobRequestPacket = DataPacket((
    ('output_mode', FixedDataPacketField(MARKER_UINT8)),
))


class PrintStartJobRequest:
    OPCODE = 7

    __slots__ = ('output_mode',)

    def __init__(
            self, *,
            output_mode: Optional[int] = None,
    ) -> None:
        self.output_mode = output_mode

    def as_dict(self) -> Dict[str, Any]:
        return {
            'output_mode': self.output_mode,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintStartJobRequest':
        return PrintStartJobRequest(**PrintStartJobRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintStartJobRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintStartJobRequest.lib = library.xprint_printstartjob
        PrintStartJobRequest.lib.restype = ctypes.c_uint32
        PrintStartJobRequest.lib.argstype = (ctypes.c_uint8,)


class PrintStartJobRequestCType(ctypes.Structure):
    """xprint PrintStartJob"""
    _fields_ = [
        ("output_mode", ctypes.c_uint8),
    ]


PrintEndJobRequestPacket = DataPacket((
    ('cancel', FixedDataPacketField(MARKER_UINT8)),
))


class PrintEndJobRequest:
    OPCODE = 8

    __slots__ = ('cancel',)

    def __init__(
            self, *,
            cancel: Optional[bool] = None,
    ) -> None:
        self.cancel = cancel

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cancel': self.cancel,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintEndJobRequest':
        return PrintEndJobRequest(**PrintEndJobRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintEndJobRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[bool], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintEndJobRequest.lib = library.xprint_printendjob
        PrintEndJobRequest.lib.restype = ctypes.c_uint32
        PrintEndJobRequest.lib.argstype = (ctypes.c_int8,)


class PrintEndJobRequestCType(ctypes.Structure):
    """xprint PrintEndJob"""
    _fields_ = [
        ("cancel", ctypes.c_int8),
    ]


PrintStartDocRequestPacket = DataPacket((
    ('driver_mode', FixedDataPacketField(MARKER_UINT8)),
))


class PrintStartDocRequest:
    OPCODE = 9

    __slots__ = ('driver_mode',)

    def __init__(
            self, *,
            driver_mode: Optional[int] = None,
    ) -> None:
        self.driver_mode = driver_mode

    def as_dict(self) -> Dict[str, Any]:
        return {
            'driver_mode': self.driver_mode,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintStartDocRequest':
        return PrintStartDocRequest(**PrintStartDocRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintStartDocRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintStartDocRequest.lib = library.xprint_printstartdoc
        PrintStartDocRequest.lib.restype = ctypes.c_uint32
        PrintStartDocRequest.lib.argstype = (ctypes.c_uint8,)


class PrintStartDocRequestCType(ctypes.Structure):
    """xprint PrintStartDoc"""
    _fields_ = [
        ("driver_mode", ctypes.c_uint8),
    ]


PrintEndDocRequestPacket = DataPacket((
    ('cancel', FixedDataPacketField(MARKER_UINT8)),
))


class PrintEndDocRequest:
    OPCODE = 10

    __slots__ = ('cancel',)

    def __init__(
            self, *,
            cancel: Optional[bool] = None,
    ) -> None:
        self.cancel = cancel

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cancel': self.cancel,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintEndDocRequest':
        return PrintEndDocRequest(**PrintEndDocRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintEndDocRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[bool], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintEndDocRequest.lib = library.xprint_printenddoc
        PrintEndDocRequest.lib.restype = ctypes.c_uint32
        PrintEndDocRequest.lib.argstype = (ctypes.c_int8,)


class PrintEndDocRequestCType(ctypes.Structure):
    """xprint PrintEndDoc"""
    _fields_ = [
        ("cancel", ctypes.c_int8),
    ]


PrintPutDocumentDataRequestPacket = DataPacket((
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('len_data', FixedDataPacketField(MARKER_UINT32)),
    ('len_fmt', FixedDataPacketField(MARKER_UINT16)),
    ('len_options', FixedDataPacketField(MARKER_UINT16)),
    ('data', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['len_data'], 0)),
    ('pad0', AlignedPadDataPacketField(4)),
    ('doc_format', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['len_fmt'], 0)),
    ('pad1', AlignedPadDataPacketField(4)),
    ('options', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['len_options'], 0)),
))


class PrintPutDocumentDataRequest:
    OPCODE = 11

    __slots__ = ('drawable', 'len_data', 'len_fmt', 'len_options', 'data', 'doc_format', 'options',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            len_data: Optional[int] = None,
            len_fmt: Optional[int] = None,
            len_options: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
            doc_format: Optional[Sequence[int]] = None,
            options: Optional[Sequence[int]] = None,
    ) -> None:
        self.drawable = drawable
        self.len_data = len_data
        self.len_fmt = len_fmt
        self.len_options = len_options
        self.data = data
        self.doc_format = doc_format
        self.options = options

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'len_data': self.len_data,
            'len_fmt': self.len_fmt,
            'len_options': self.len_options,
            'data': self.data,
            'doc_format': self.doc_format,
            'options': self.options,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintPutDocumentDataRequest':
        return PrintPutDocumentDataRequest(**PrintPutDocumentDataRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintPutDocumentDataRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, Sequence[int], Sequence[int], Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintPutDocumentDataRequest.lib = library.xprint_printputdocumentdata
        PrintPutDocumentDataRequest.lib.restype = ctypes.c_uint32
        PrintPutDocumentDataRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)


class PrintPutDocumentDataRequestCType(ctypes.Structure):
    """xprint PrintPutDocumentData"""
    _fields_ = [
        ("drawable", ctypes.c_uint32),
        ("len_data", ctypes.c_uint32),
        ("len_fmt", ctypes.c_uint16),
        ("len_options", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


PrintGetDocumentDataRequestCookie = NewType('PrintGetDocumentDataRequestCookie', ctypes.c_uint32)


PrintGetDocumentDataRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
    ('max_bytes', FixedDataPacketField(MARKER_UINT32)),
))


class PrintGetDocumentDataRequest:
    OPCODE = 12

    __slots__ = ('context', 'max_bytes',)

    def __init__(
            self, *,
            context: Optional[int] = None,
            max_bytes: Optional[int] = None,
    ) -> None:
        self.context = context
        self.max_bytes = max_bytes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
            'max_bytes': self.max_bytes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintGetDocumentDataRequest':
        return PrintGetDocumentDataRequest(**PrintGetDocumentDataRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintGetDocumentDataRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], PrintGetDocumentDataRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintGetDocumentDataRequest.lib = library.xprint_printgetdocumentdata
        PrintGetDocumentDataRequest.lib.restype = PrintGetDocumentDataRequestCookie
        PrintGetDocumentDataRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class PrintGetDocumentDataRequestCType(ctypes.Structure):
    """xprint PrintGetDocumentData"""
    _fields_ = [
        ("context", ctypes.c_uint32),
        ("max_bytes", ctypes.c_uint32),
    ]


PrintGetDocumentDataReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('status_code', FixedDataPacketField(MARKER_UINT32)),
    ('finished_flag', FixedDataPacketField(MARKER_UINT32)),
    ('dataLen', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(12)),
    ('data', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['dataLen'], 0)),
))


class PrintGetDocumentDataReplyReply:
    __slots__ = ('status_code', 'finished_flag', 'datalen', 'data',)

    def __init__(
            self, *,
            status_code: Optional[int] = None,
            finished_flag: Optional[int] = None,
            datalen: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.status_code = status_code
        self.finished_flag = finished_flag
        self.datalen = datalen
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'status_code': self.status_code,
            'finished_flag': self.finished_flag,
            'dataLen': self.datalen,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintGetDocumentDataReplyReply':
        return PrintGetDocumentDataReplyReply(**PrintGetDocumentDataReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintGetDocumentDataReplyReplyPacket.pack(**self.as_dict())


class PrintGetDocumentDataReplyReplyCType(ctypes.Structure):
    """xprint PrintGetDocumentData_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("status_code", ctypes.c_uint32),
        ("finished_flag", ctypes.c_uint32),
        ("dataLen", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


PrintStartPageRequestPacket = DataPacket((
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class PrintStartPageRequest:
    OPCODE = 13

    __slots__ = ('window',)

    def __init__(
            self, *,
            window: Optional[int] = None,
    ) -> None:
        self.window = window

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintStartPageRequest':
        return PrintStartPageRequest(**PrintStartPageRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintStartPageRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintStartPageRequest.lib = library.xprint_printstartpage
        PrintStartPageRequest.lib.restype = ctypes.c_uint32
        PrintStartPageRequest.lib.argstype = (ctypes.c_uint32,)


class PrintStartPageRequestCType(ctypes.Structure):
    """xprint PrintStartPage"""
    _fields_ = [
        ("window", ctypes.c_uint32),
    ]


PrintEndPageRequestPacket = DataPacket((
    ('cancel', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class PrintEndPageRequest:
    OPCODE = 14

    __slots__ = ('cancel',)

    def __init__(
            self, *,
            cancel: Optional[bool] = None,
    ) -> None:
        self.cancel = cancel

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cancel': self.cancel,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintEndPageRequest':
        return PrintEndPageRequest(**PrintEndPageRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintEndPageRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[bool], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintEndPageRequest.lib = library.xprint_printendpage
        PrintEndPageRequest.lib.restype = ctypes.c_uint32
        PrintEndPageRequest.lib.argstype = (ctypes.c_int8, ctypes.c_uint8 * 3)


class PrintEndPageRequestCType(ctypes.Structure):
    """xprint PrintEndPage"""
    _fields_ = [
        ("cancel", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


PrintSelectInputRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
    ('event_mask', FixedDataPacketField(MARKER_UINT32)),
))


class PrintSelectInputRequest:
    OPCODE = 15

    __slots__ = ('context', 'event_mask',)

    def __init__(
            self, *,
            context: Optional[int] = None,
            event_mask: Optional[int] = None,
    ) -> None:
        self.context = context
        self.event_mask = event_mask

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
            'event_mask': self.event_mask,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintSelectInputRequest':
        return PrintSelectInputRequest(**PrintSelectInputRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintSelectInputRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintSelectInputRequest.lib = library.xprint_printselectinput
        PrintSelectInputRequest.lib.restype = ctypes.c_uint32
        PrintSelectInputRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32)


class PrintSelectInputRequestCType(ctypes.Structure):
    """xprint PrintSelectInput"""
    _fields_ = [
        ("context", ctypes.c_uint32),
        ("event_mask", ctypes.c_uint32),
    ]


PrintInputSelectedRequestCookie = NewType('PrintInputSelectedRequestCookie', ctypes.c_uint32)


PrintInputSelectedRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
))


class PrintInputSelectedRequest:
    OPCODE = 16

    __slots__ = ('context',)

    def __init__(
            self, *,
            context: Optional[int] = None,
    ) -> None:
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintInputSelectedRequest':
        return PrintInputSelectedRequest(**PrintInputSelectedRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintInputSelectedRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], PrintInputSelectedRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintInputSelectedRequest.lib = library.xprint_printinputselected
        PrintInputSelectedRequest.lib.restype = PrintInputSelectedRequestCookie
        PrintInputSelectedRequest.lib.argstype = (ctypes.c_uint32,)


class PrintInputSelectedRequestCType(ctypes.Structure):
    """xprint PrintInputSelected"""
    _fields_ = [
        ("context", ctypes.c_uint32),
    ]


PrintInputSelectedReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('event_mask', FixedDataPacketField(MARKER_UINT32)),
    ('all_events_mask', FixedDataPacketField(MARKER_UINT32)),
))


class PrintInputSelectedReplyReply:
    __slots__ = ('event_mask', 'all_events_mask',)

    def __init__(
            self, *,
            event_mask: Optional[int] = None,
            all_events_mask: Optional[int] = None,
    ) -> None:
        self.event_mask = event_mask
        self.all_events_mask = all_events_mask

    def as_dict(self) -> Dict[str, Any]:
        return {
            'event_mask': self.event_mask,
            'all_events_mask': self.all_events_mask,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintInputSelectedReplyReply':
        return PrintInputSelectedReplyReply(**PrintInputSelectedReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintInputSelectedReplyReplyPacket.pack(**self.as_dict())


class PrintInputSelectedReplyReplyCType(ctypes.Structure):
    """xprint PrintInputSelected_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("event_mask", ctypes.c_uint32),
        ("all_events_mask", ctypes.c_uint32),
    ]


PrintGetAttributesRequestCookie = NewType('PrintGetAttributesRequestCookie', ctypes.c_uint32)


PrintGetAttributesRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
    ('pool', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class PrintGetAttributesRequest:
    OPCODE = 17

    __slots__ = ('context', 'pool',)

    def __init__(
            self, *,
            context: Optional[int] = None,
            pool: Optional[int] = None,
    ) -> None:
        self.context = context
        self.pool = pool

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
            'pool': self.pool,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintGetAttributesRequest':
        return PrintGetAttributesRequest(**PrintGetAttributesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintGetAttributesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], PrintGetAttributesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintGetAttributesRequest.lib = library.xprint_printgetattributes
        PrintGetAttributesRequest.lib.restype = PrintGetAttributesRequestCookie
        PrintGetAttributesRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8 * 3)


class PrintGetAttributesRequestCType(ctypes.Structure):
    """xprint PrintGetAttributes"""
    _fields_ = [
        ("context", ctypes.c_uint32),
        ("pool", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


PrintGetAttributesReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('stringLen', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('attributes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['stringLen'], 0)),
))


class PrintGetAttributesReplyReply:
    __slots__ = ('stringlen', 'attributes',)

    def __init__(
            self, *,
            stringlen: Optional[int] = None,
            attributes: Optional[Sequence[int]] = None,
    ) -> None:
        self.stringlen = stringlen
        self.attributes = attributes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'stringLen': self.stringlen,
            'attributes': self.attributes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintGetAttributesReplyReply':
        return PrintGetAttributesReplyReply(**PrintGetAttributesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintGetAttributesReplyReplyPacket.pack(**self.as_dict())


class PrintGetAttributesReplyReplyCType(ctypes.Structure):
    """xprint PrintGetAttributes_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("stringLen", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


PrintGetOneAttributesRequestCookie = NewType('PrintGetOneAttributesRequestCookie', ctypes.c_uint32)


PrintGetOneAttributesRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
    ('nameLen', FixedDataPacketField(MARKER_UINT32)),
    ('pool', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('name', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['nameLen'], 0)),
))


class PrintGetOneAttributesRequest:
    OPCODE = 19

    __slots__ = ('context', 'namelen', 'pool', 'name',)

    def __init__(
            self, *,
            context: Optional[int] = None,
            namelen: Optional[int] = None,
            pool: Optional[int] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.context = context
        self.namelen = namelen
        self.pool = pool
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
            'nameLen': self.namelen,
            'pool': self.pool,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintGetOneAttributesRequest':
        return PrintGetOneAttributesRequest(**PrintGetOneAttributesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintGetOneAttributesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, Sequence[int]], PrintGetOneAttributesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintGetOneAttributesRequest.lib = library.xprint_printgetoneattributes
        PrintGetOneAttributesRequest.lib.restype = PrintGetOneAttributesRequestCookie
        PrintGetOneAttributesRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8 * 3, ctypes.c_void_p)


class PrintGetOneAttributesRequestCType(ctypes.Structure):
    """xprint PrintGetOneAttributes"""
    _fields_ = [
        ("context", ctypes.c_uint32),
        ("nameLen", ctypes.c_uint32),
        ("pool", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("var_data", ctypes.c_void_p),
    ]


PrintGetOneAttributesReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('valueLen', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('value', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['valueLen'], 0)),
))


class PrintGetOneAttributesReplyReply:
    __slots__ = ('valuelen', 'value',)

    def __init__(
            self, *,
            valuelen: Optional[int] = None,
            value: Optional[Sequence[int]] = None,
    ) -> None:
        self.valuelen = valuelen
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {
            'valueLen': self.valuelen,
            'value': self.value,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintGetOneAttributesReplyReply':
        return PrintGetOneAttributesReplyReply(**PrintGetOneAttributesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintGetOneAttributesReplyReplyPacket.pack(**self.as_dict())


class PrintGetOneAttributesReplyReplyCType(ctypes.Structure):
    """xprint PrintGetOneAttributes_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("valueLen", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


PrintSetAttributesRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
    ('stringLen', FixedDataPacketField(MARKER_UINT32)),
    ('pool', FixedDataPacketField(MARKER_UINT8)),
    ('rule', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('attributes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class PrintSetAttributesRequest:
    OPCODE = 18

    __slots__ = ('context', 'stringlen', 'pool', 'rule', 'attributes',)

    def __init__(
            self, *,
            context: Optional[int] = None,
            stringlen: Optional[int] = None,
            pool: Optional[int] = None,
            rule: Optional[int] = None,
            attributes: Optional[Sequence[int]] = None,
    ) -> None:
        self.context = context
        self.stringlen = stringlen
        self.pool = pool
        self.rule = rule
        self.attributes = attributes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
            'stringLen': self.stringlen,
            'pool': self.pool,
            'rule': self.rule,
            'attributes': self.attributes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintSetAttributesRequest':
        return PrintSetAttributesRequest(**PrintSetAttributesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintSetAttributesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintSetAttributesRequest.lib = library.xprint_printsetattributes
        PrintSetAttributesRequest.lib.restype = ctypes.c_uint32
        PrintSetAttributesRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8 * 2, ctypes.c_void_p)


class PrintSetAttributesRequestCType(ctypes.Structure):
    """xprint PrintSetAttributes"""
    _fields_ = [
        ("context", ctypes.c_uint32),
        ("stringLen", ctypes.c_uint32),
        ("pool", ctypes.c_uint8),
        ("rule", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


PrintGetPageDimensionsRequestCookie = NewType('PrintGetPageDimensionsRequestCookie', ctypes.c_uint32)


PrintGetPageDimensionsRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
))


class PrintGetPageDimensionsRequest:
    OPCODE = 21

    __slots__ = ('context',)

    def __init__(
            self, *,
            context: Optional[int] = None,
    ) -> None:
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintGetPageDimensionsRequest':
        return PrintGetPageDimensionsRequest(**PrintGetPageDimensionsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintGetPageDimensionsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], PrintGetPageDimensionsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintGetPageDimensionsRequest.lib = library.xprint_printgetpagedimensions
        PrintGetPageDimensionsRequest.lib.restype = PrintGetPageDimensionsRequestCookie
        PrintGetPageDimensionsRequest.lib.argstype = (ctypes.c_uint32,)


class PrintGetPageDimensionsRequestCType(ctypes.Structure):
    """xprint PrintGetPageDimensions"""
    _fields_ = [
        ("context", ctypes.c_uint32),
    ]


PrintGetPageDimensionsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('offset_x', FixedDataPacketField(MARKER_UINT16)),
    ('offset_y', FixedDataPacketField(MARKER_UINT16)),
    ('reproducible_width', FixedDataPacketField(MARKER_UINT16)),
    ('reproducible_height', FixedDataPacketField(MARKER_UINT16)),
))


class PrintGetPageDimensionsReplyReply:
    __slots__ = ('width', 'height', 'offset_x', 'offset_y', 'reproducible_width', 'reproducible_height',)

    def __init__(
            self, *,
            width: Optional[int] = None,
            height: Optional[int] = None,
            offset_x: Optional[int] = None,
            offset_y: Optional[int] = None,
            reproducible_width: Optional[int] = None,
            reproducible_height: Optional[int] = None,
    ) -> None:
        self.width = width
        self.height = height
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.reproducible_width = reproducible_width
        self.reproducible_height = reproducible_height

    def as_dict(self) -> Dict[str, Any]:
        return {
            'width': self.width,
            'height': self.height,
            'offset_x': self.offset_x,
            'offset_y': self.offset_y,
            'reproducible_width': self.reproducible_width,
            'reproducible_height': self.reproducible_height,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintGetPageDimensionsReplyReply':
        return PrintGetPageDimensionsReplyReply(**PrintGetPageDimensionsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintGetPageDimensionsReplyReplyPacket.pack(**self.as_dict())


class PrintGetPageDimensionsReplyReplyCType(ctypes.Structure):
    """xprint PrintGetPageDimensions_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("offset_x", ctypes.c_uint16),
        ("offset_y", ctypes.c_uint16),
        ("reproducible_width", ctypes.c_uint16),
        ("reproducible_height", ctypes.c_uint16),
    ]


PrintQueryScreensRequestCookie = NewType('PrintQueryScreensRequestCookie', ctypes.c_uint32)


PrintQueryScreensRequestPacket = DataPacket((
))


class PrintQueryScreensRequest:
    OPCODE = 22

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintQueryScreensRequest':
        return PrintQueryScreensRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], PrintQueryScreensRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintQueryScreensRequest.lib = library.xprint_printqueryscreens
        PrintQueryScreensRequest.lib.restype = PrintQueryScreensRequestCookie
        PrintQueryScreensRequest.lib.argstype = ()


class PrintQueryScreensRequestCType(ctypes.Structure):
    """xprint PrintQueryScreens"""
    _fields_ = [
    ]


PrintQueryScreensReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('listCount', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('roots', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['listCount'], 0)),
))


class PrintQueryScreensReplyReply:
    __slots__ = ('listcount', 'roots',)

    def __init__(
            self, *,
            listcount: Optional[int] = None,
            roots: Optional[Sequence[int]] = None,
    ) -> None:
        self.listcount = listcount
        self.roots = roots

    def as_dict(self) -> Dict[str, Any]:
        return {
            'listCount': self.listcount,
            'roots': self.roots,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintQueryScreensReplyReply':
        return PrintQueryScreensReplyReply(**PrintQueryScreensReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintQueryScreensReplyReplyPacket.pack(**self.as_dict())


class PrintQueryScreensReplyReplyCType(ctypes.Structure):
    """xprint PrintQueryScreens_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("listCount", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


PrintSetImageResolutionRequestCookie = NewType('PrintSetImageResolutionRequestCookie', ctypes.c_uint32)


PrintSetImageResolutionRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
    ('image_resolution', FixedDataPacketField(MARKER_UINT16)),
))


class PrintSetImageResolutionRequest:
    OPCODE = 23

    __slots__ = ('context', 'image_resolution',)

    def __init__(
            self, *,
            context: Optional[int] = None,
            image_resolution: Optional[int] = None,
    ) -> None:
        self.context = context
        self.image_resolution = image_resolution

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
            'image_resolution': self.image_resolution,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintSetImageResolutionRequest':
        return PrintSetImageResolutionRequest(**PrintSetImageResolutionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintSetImageResolutionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], PrintSetImageResolutionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintSetImageResolutionRequest.lib = library.xprint_printsetimageresolution
        PrintSetImageResolutionRequest.lib.restype = PrintSetImageResolutionRequestCookie
        PrintSetImageResolutionRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint16)


class PrintSetImageResolutionRequestCType(ctypes.Structure):
    """xprint PrintSetImageResolution"""
    _fields_ = [
        ("context", ctypes.c_uint32),
        ("image_resolution", ctypes.c_uint16),
    ]


PrintSetImageResolutionReplyReplyPacket = DataPacket((
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('previous_resolutions', FixedDataPacketField(MARKER_UINT16)),
))


class PrintSetImageResolutionReplyReply:
    __slots__ = ('status', 'previous_resolutions',)

    def __init__(
            self, *,
            status: Optional[bool] = None,
            previous_resolutions: Optional[int] = None,
    ) -> None:
        self.status = status
        self.previous_resolutions = previous_resolutions

    def as_dict(self) -> Dict[str, Any]:
        return {
            'status': self.status,
            'previous_resolutions': self.previous_resolutions,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintSetImageResolutionReplyReply':
        return PrintSetImageResolutionReplyReply(**PrintSetImageResolutionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintSetImageResolutionReplyReplyPacket.pack(**self.as_dict())


class PrintSetImageResolutionReplyReplyCType(ctypes.Structure):
    """xprint PrintSetImageResolution_reply"""
    _fields_ = [
        ("status", ctypes.c_int8),
        ("previous_resolutions", ctypes.c_uint16),
    ]


PrintGetImageResolutionRequestCookie = NewType('PrintGetImageResolutionRequestCookie', ctypes.c_uint32)


PrintGetImageResolutionRequestPacket = DataPacket((
    ('context', FixedDataPacketField(MARKER_UINT32)),
))


class PrintGetImageResolutionRequest:
    OPCODE = 24

    __slots__ = ('context',)

    def __init__(
            self, *,
            context: Optional[int] = None,
    ) -> None:
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintGetImageResolutionRequest':
        return PrintGetImageResolutionRequest(**PrintGetImageResolutionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintGetImageResolutionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], PrintGetImageResolutionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PrintGetImageResolutionRequest.lib = library.xprint_printgetimageresolution
        PrintGetImageResolutionRequest.lib.restype = PrintGetImageResolutionRequestCookie
        PrintGetImageResolutionRequest.lib.argstype = (ctypes.c_uint32,)


class PrintGetImageResolutionRequestCType(ctypes.Structure):
    """xprint PrintGetImageResolution"""
    _fields_ = [
        ("context", ctypes.c_uint32),
    ]


PrintGetImageResolutionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('image_resolution', FixedDataPacketField(MARKER_UINT16)),
))


class PrintGetImageResolutionReplyReply:
    __slots__ = ('image_resolution',)

    def __init__(
            self, *,
            image_resolution: Optional[int] = None,
    ) -> None:
        self.image_resolution = image_resolution

    def as_dict(self) -> Dict[str, Any]:
        return {
            'image_resolution': self.image_resolution,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PrintGetImageResolutionReplyReply':
        return PrintGetImageResolutionReplyReply(**PrintGetImageResolutionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PrintGetImageResolutionReplyReplyPacket.pack(**self.as_dict())


class PrintGetImageResolutionReplyReplyCType(ctypes.Structure):
    """xprint PrintGetImageResolution_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("image_resolution", ctypes.c_uint16),
    ]


NotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('detail', FixedDataPacketField(MARKER_UINT8)),
    ('context', FixedDataPacketField(MARKER_UINT32)),
    ('cancel', FixedDataPacketField(MARKER_UINT8)),
))


class NotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'detail', 'context', 'cancel',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            detail: Optional[int] = None,
            context: Optional[int] = None,
            cancel: Optional[bool] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.detail = detail
        self.context = context
        self.cancel = cancel

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'detail': self.detail,
            'context': self.context,
            'cancel': self.cancel,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'NotifyEvent':
        return NotifyEvent(**NotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return NotifyEventPacket.pack(**self.as_dict())


class NotifyEventCType(ctypes.Structure):
    """xprint Notify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("detail", ctypes.c_uint8),
        ("context", ctypes.c_uint32),
        ("cancel", ctypes.c_int8),
    ]


AttributNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('detail', FixedDataPacketField(MARKER_UINT8)),
    ('context', FixedDataPacketField(MARKER_UINT32)),
))


class AttributNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'detail', 'context',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            detail: Optional[int] = None,
            context: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.detail = detail
        self.context = context

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'detail': self.detail,
            'context': self.context,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AttributNotifyEvent':
        return AttributNotifyEvent(**AttributNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AttributNotifyEventPacket.pack(**self.as_dict())


class AttributNotifyEventCType(ctypes.Structure):
    """xprint AttributNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("detail", ctypes.c_uint8),
        ("context", ctypes.c_uint32),
    ]


# ------------------------------------------------------------------
# Unions

