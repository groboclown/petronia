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

VisualClassType = NewType('VisualClassType', int)


class VisualClassValues:
    STATIC_GRAY = VisualClassType(0)
    GRAY_SCALE = VisualClassType(1)
    STATIC_COLOR = VisualClassType(2)
    PSEUDO_COLOR = VisualClassType(3)
    TRUE_COLOR = VisualClassType(4)
    DIRECT_COLOR = VisualClassType(5)


EventMaskType = NewType('EventMaskType', int)


class EventMaskValues:
    NO_EVENT = EventMaskType(0)
    KEY_PRESS = EventMaskType(1)
    KEY_RELEASE = EventMaskType(2)
    BUTTON_PRESS = EventMaskType(4)
    BUTTON_RELEASE = EventMaskType(8)
    ENTER_WINDOW = EventMaskType(16)
    LEAVE_WINDOW = EventMaskType(32)
    POINTER_MOTION = EventMaskType(64)
    POINTER_MOTION_HINT = EventMaskType(128)
    BUTTON1MOTION = EventMaskType(256)
    BUTTON2MOTION = EventMaskType(512)
    BUTTON3MOTION = EventMaskType(1024)
    BUTTON4MOTION = EventMaskType(2048)
    BUTTON5MOTION = EventMaskType(4096)
    BUTTON_MOTION = EventMaskType(8192)
    KEYMAP_STATE = EventMaskType(16384)
    EXPOSURE = EventMaskType(32768)
    VISIBILITY_CHANGE = EventMaskType(65536)
    STRUCTURE_NOTIFY = EventMaskType(131072)
    RESIZE_REDIRECT = EventMaskType(262144)
    SUBSTRUCTURE_NOTIFY = EventMaskType(524288)
    SUBSTRUCTURE_REDIRECT = EventMaskType(1048576)
    FOCUS_CHANGE = EventMaskType(2097152)
    PROPERTY_CHANGE = EventMaskType(4194304)
    COLOR_MAP_CHANGE = EventMaskType(8388608)
    OWNER_GRAB_BUTTON = EventMaskType(16777216)


BackingStoreType = NewType('BackingStoreType', int)


class BackingStoreValues:
    NOT_USEFUL = BackingStoreType(0)
    WHEN_MAPPED = BackingStoreType(1)
    ALWAYS = BackingStoreType(2)


ImageOrderType = NewType('ImageOrderType', int)


class ImageOrderValues:
    LSBFIRST = ImageOrderType(0)
    MSBFIRST = ImageOrderType(1)


ModMaskType = NewType('ModMaskType', int)


class ModMaskValues:
    SHIFT = ModMaskType(1)
    LOCK = ModMaskType(2)
    CONTROL = ModMaskType(4)
    V_1 = ModMaskType(8)
    V_2 = ModMaskType(16)
    V_3 = ModMaskType(32)
    V_4 = ModMaskType(64)
    V_5 = ModMaskType(128)
    ANY = ModMaskType(32768)


KeyButMaskType = NewType('KeyButMaskType', int)


class KeyButMaskValues:
    SHIFT = KeyButMaskType(1)
    LOCK = KeyButMaskType(2)
    CONTROL = KeyButMaskType(4)
    MOD1 = KeyButMaskType(8)
    MOD2 = KeyButMaskType(16)
    MOD3 = KeyButMaskType(32)
    MOD4 = KeyButMaskType(64)
    MOD5 = KeyButMaskType(128)
    BUTTON1 = KeyButMaskType(256)
    BUTTON2 = KeyButMaskType(512)
    BUTTON3 = KeyButMaskType(1024)
    BUTTON4 = KeyButMaskType(2048)
    BUTTON5 = KeyButMaskType(4096)


WindowType = NewType('WindowType', int)


class WindowValues:
    NONE = WindowType(0)


ButtonMaskType = NewType('ButtonMaskType', int)


class ButtonMaskValues:
    V_1 = ButtonMaskType(256)
    V_2 = ButtonMaskType(512)
    V_3 = ButtonMaskType(1024)
    V_4 = ButtonMaskType(2048)
    V_5 = ButtonMaskType(4096)
    ANY = ButtonMaskType(32768)


MotionType = NewType('MotionType', int)


class MotionValues:
    NORMAL = MotionType(0)
    HINT = MotionType(1)


NotifyDetailType = NewType('NotifyDetailType', int)


class NotifyDetailValues:
    ANCESTOR = NotifyDetailType(0)
    VIRTUAL = NotifyDetailType(1)
    INFERIOR = NotifyDetailType(2)
    NONLINEAR = NotifyDetailType(3)
    NONLINEAR_VIRTUAL = NotifyDetailType(4)
    POINTER = NotifyDetailType(5)
    POINTER_ROOT = NotifyDetailType(6)
    NONE = NotifyDetailType(7)


NotifyModeType = NewType('NotifyModeType', int)


class NotifyModeValues:
    NORMAL = NotifyModeType(0)
    GRAB = NotifyModeType(1)
    UNGRAB = NotifyModeType(2)
    WHILE_GRABBED = NotifyModeType(3)


VisibilityType = NewType('VisibilityType', int)


class VisibilityValues:
    UNOBSCURED = VisibilityType(0)
    PARTIALLY_OBSCURED = VisibilityType(1)
    FULLY_OBSCURED = VisibilityType(2)


PlaceType = NewType('PlaceType', int)


class PlaceValues:
    ON_TOP = PlaceType(0)
    ON_BOTTOM = PlaceType(1)


PropertyType = NewType('PropertyType', int)


class PropertyValues:
    NEW_VALUE = PropertyType(0)
    DELETE = PropertyType(1)


TimeType = NewType('TimeType', int)


class TimeValues:
    CURRENT_TIME = TimeType(0)


AtomType = NewType('AtomType', int)


class AtomValues:
    NONE = AtomType(0)
    ANY = AtomType(0)
    PRIMARY = AtomType(1)
    SECONDARY = AtomType(2)
    ARC = AtomType(3)
    ATOM = AtomType(4)
    BITMAP = AtomType(5)
    CARDINAL = AtomType(6)
    COLORMAP = AtomType(7)
    CURSOR = AtomType(8)
    CUT_BUFFER0 = AtomType(9)
    CUT_BUFFER1 = AtomType(10)
    CUT_BUFFER2 = AtomType(11)
    CUT_BUFFER3 = AtomType(12)
    CUT_BUFFER4 = AtomType(13)
    CUT_BUFFER5 = AtomType(14)
    CUT_BUFFER6 = AtomType(15)
    CUT_BUFFER7 = AtomType(16)
    DRAWABLE = AtomType(17)
    FONT = AtomType(18)
    INTEGER = AtomType(19)
    PIXMAP = AtomType(20)
    POINT = AtomType(21)
    RECTANGLE = AtomType(22)
    RESOURCE_MANAGER = AtomType(23)
    RGB_COLOR_MAP = AtomType(24)
    RGB_BEST_MAP = AtomType(25)
    RGB_BLUE_MAP = AtomType(26)
    RGB_DEFAULT_MAP = AtomType(27)
    RGB_GRAY_MAP = AtomType(28)
    RGB_GREEN_MAP = AtomType(29)
    RGB_RED_MAP = AtomType(30)
    STRING = AtomType(31)
    VISUALID = AtomType(32)
    WINDOW = AtomType(33)
    WM_COMMAND = AtomType(34)
    WM_HINTS = AtomType(35)
    WM_CLIENT_MACHINE = AtomType(36)
    WM_ICON_NAME = AtomType(37)
    WM_ICON_SIZE = AtomType(38)
    WM_NAME = AtomType(39)
    WM_NORMAL_HINTS = AtomType(40)
    WM_SIZE_HINTS = AtomType(41)
    WM_ZOOM_HINTS = AtomType(42)
    MIN_SPACE = AtomType(43)
    NORM_SPACE = AtomType(44)
    MAX_SPACE = AtomType(45)
    END_SPACE = AtomType(46)
    SUPERSCRIPT_X = AtomType(47)
    SUPERSCRIPT_Y = AtomType(48)
    SUBSCRIPT_X = AtomType(49)
    SUBSCRIPT_Y = AtomType(50)
    UNDERLINE_POSITION = AtomType(51)
    UNDERLINE_THICKNESS = AtomType(52)
    STRIKEOUT_ASCENT = AtomType(53)
    STRIKEOUT_DESCENT = AtomType(54)
    ITALIC_ANGLE = AtomType(55)
    X_HEIGHT = AtomType(56)
    QUAD_WIDTH = AtomType(57)
    WEIGHT = AtomType(58)
    POINT_SIZE = AtomType(59)
    RESOLUTION = AtomType(60)
    COPYRIGHT = AtomType(61)
    NOTICE = AtomType(62)
    FONT_NAME = AtomType(63)
    FAMILY_NAME = AtomType(64)
    FULL_NAME = AtomType(65)
    CAP_HEIGHT = AtomType(66)
    WM_CLASS = AtomType(67)
    WM_TRANSIENT_FOR = AtomType(68)


ColormapStateType = NewType('ColormapStateType', int)


class ColormapStateValues:
    UNINSTALLED = ColormapStateType(0)
    INSTALLED = ColormapStateType(1)


ColormapType = NewType('ColormapType', int)


class ColormapValues:
    NONE = ColormapType(0)


MappingType = NewType('MappingType', int)


class MappingValues:
    MODIFIER = MappingType(0)
    KEYBOARD = MappingType(1)
    POINTER = MappingType(2)


WindowClassType = NewType('WindowClassType', int)


class WindowClassValues:
    COPY_FROM_PARENT = WindowClassType(0)
    INPUT_OUTPUT = WindowClassType(1)
    INPUT_ONLY = WindowClassType(2)


CwType = NewType('CwType', int)


class CwValues:
    BACK_PIXMAP = CwType(1)
    BACK_PIXEL = CwType(2)
    BORDER_PIXMAP = CwType(4)
    BORDER_PIXEL = CwType(8)
    BIT_GRAVITY = CwType(16)
    WIN_GRAVITY = CwType(32)
    BACKING_STORE = CwType(64)
    BACKING_PLANES = CwType(128)
    BACKING_PIXEL = CwType(256)
    OVERRIDE_REDIRECT = CwType(512)
    SAVE_UNDER = CwType(1024)
    EVENT_MASK = CwType(2048)
    DONT_PROPAGATE = CwType(4096)
    COLORMAP = CwType(8192)
    CURSOR = CwType(16384)


BackPixmapType = NewType('BackPixmapType', int)


class BackPixmapValues:
    NONE = BackPixmapType(0)
    PARENT_RELATIVE = BackPixmapType(1)


GravityType = NewType('GravityType', int)


class GravityValues:
    BIT_FORGET = GravityType(0)
    WIN_UNMAP = GravityType(0)
    NORTH_WEST = GravityType(1)
    NORTH = GravityType(2)
    NORTH_EAST = GravityType(3)
    WEST = GravityType(4)
    CENTER = GravityType(5)
    EAST = GravityType(6)
    SOUTH_WEST = GravityType(7)
    SOUTH = GravityType(8)
    SOUTH_EAST = GravityType(9)
    STATIC = GravityType(10)


MapStateType = NewType('MapStateType', int)


class MapStateValues:
    UNMAPPED = MapStateType(0)
    UNVIEWABLE = MapStateType(1)
    VIEWABLE = MapStateType(2)


SetModeType = NewType('SetModeType', int)


class SetModeValues:
    INSERT = SetModeType(0)
    DELETE = SetModeType(1)


ConfigWindowType = NewType('ConfigWindowType', int)


class ConfigWindowValues:
    X = ConfigWindowType(1)
    Y = ConfigWindowType(2)
    WIDTH = ConfigWindowType(4)
    HEIGHT = ConfigWindowType(8)
    BORDER_WIDTH = ConfigWindowType(16)
    SIBLING = ConfigWindowType(32)
    STACK_MODE = ConfigWindowType(64)


StackModeType = NewType('StackModeType', int)


class StackModeValues:
    ABOVE = StackModeType(0)
    BELOW = StackModeType(1)
    TOP_IF = StackModeType(2)
    BOTTOM_IF = StackModeType(3)
    OPPOSITE = StackModeType(4)


CirculateType = NewType('CirculateType', int)


class CirculateValues:
    RAISE_LOWEST = CirculateType(0)
    LOWER_HIGHEST = CirculateType(1)


PropModeType = NewType('PropModeType', int)


class PropModeValues:
    REPLACE = PropModeType(0)
    PREPEND = PropModeType(1)
    APPEND = PropModeType(2)


GetPropertyTypeType = NewType('GetPropertyTypeType', int)


class GetPropertyTypeValues:
    ANY = GetPropertyTypeType(0)


SendEventDestType = NewType('SendEventDestType', int)


class SendEventDestValues:
    POINTER_WINDOW = SendEventDestType(0)
    ITEM_FOCUS = SendEventDestType(1)


GrabModeType = NewType('GrabModeType', int)


class GrabModeValues:
    SYNC = GrabModeType(0)
    ASYNC = GrabModeType(1)


GrabStatusType = NewType('GrabStatusType', int)


class GrabStatusValues:
    SUCCESS = GrabStatusType(0)
    ALREADY_GRABBED = GrabStatusType(1)
    INVALID_TIME = GrabStatusType(2)
    NOT_VIEWABLE = GrabStatusType(3)
    FROZEN = GrabStatusType(4)


CursorType = NewType('CursorType', int)


class CursorValues:
    NONE = CursorType(0)


ButtonIndexType = NewType('ButtonIndexType', int)


class ButtonIndexValues:
    ANY = ButtonIndexType(0)
    V_1 = ButtonIndexType(1)
    V_2 = ButtonIndexType(2)
    V_3 = ButtonIndexType(3)
    V_4 = ButtonIndexType(4)
    V_5 = ButtonIndexType(5)


GrabType = NewType('GrabType', int)


class GrabValues:
    ANY = GrabType(0)


AllowType = NewType('AllowType', int)


class AllowValues:
    ASYNC_POINTER = AllowType(0)
    SYNC_POINTER = AllowType(1)
    REPLAY_POINTER = AllowType(2)
    ASYNC_KEYBOARD = AllowType(3)
    SYNC_KEYBOARD = AllowType(4)
    REPLAY_KEYBOARD = AllowType(5)
    ASYNC_BOTH = AllowType(6)
    SYNC_BOTH = AllowType(7)


InputFocusType = NewType('InputFocusType', int)


class InputFocusValues:
    NONE = InputFocusType(0)
    POINTER_ROOT = InputFocusType(1)
    PARENT = InputFocusType(2)
    FOLLOW_KEYBOARD = InputFocusType(3)


FontDrawType = NewType('FontDrawType', int)


class FontDrawValues:
    LEFT_TO_RIGHT = FontDrawType(0)
    RIGHT_TO_LEFT = FontDrawType(1)


GcType = NewType('GcType', int)


class GcValues:
    FUNCTION = GcType(1)
    PLANE_MASK = GcType(2)
    FOREGROUND = GcType(4)
    BACKGROUND = GcType(8)
    LINE_WIDTH = GcType(16)
    LINE_STYLE = GcType(32)
    CAP_STYLE = GcType(64)
    JOIN_STYLE = GcType(128)
    FILL_STYLE = GcType(256)
    FILL_RULE = GcType(512)
    TILE = GcType(1024)
    STIPPLE = GcType(2048)
    TILE_STIPPLE_ORIGIN_X = GcType(4096)
    TILE_STIPPLE_ORIGIN_Y = GcType(8192)
    FONT = GcType(16384)
    SUBWINDOW_MODE = GcType(32768)
    GRAPHICS_EXPOSURES = GcType(65536)
    CLIP_ORIGIN_X = GcType(131072)
    CLIP_ORIGIN_Y = GcType(262144)
    CLIP_MASK = GcType(524288)
    DASH_OFFSET = GcType(1048576)
    DASH_LIST = GcType(2097152)
    ARC_MODE = GcType(4194304)


GxType = NewType('GxType', int)


class GxValues:
    CLEAR = GxType(0)
    AND = GxType(1)
    AND_REVERSE = GxType(2)
    COPY = GxType(3)
    AND_INVERTED = GxType(4)
    NOOP = GxType(5)
    XOR = GxType(6)
    OR = GxType(7)
    NOR = GxType(8)
    EQUIV = GxType(9)
    INVERT = GxType(10)
    OR_REVERSE = GxType(11)
    COPY_INVERTED = GxType(12)
    OR_INVERTED = GxType(13)
    NAND = GxType(14)
    SET = GxType(15)


LineStyleType = NewType('LineStyleType', int)


class LineStyleValues:
    SOLID = LineStyleType(0)
    ON_OFF_DASH = LineStyleType(1)
    DOUBLE_DASH = LineStyleType(2)


CapStyleType = NewType('CapStyleType', int)


class CapStyleValues:
    NOT_LAST = CapStyleType(0)
    BUTT = CapStyleType(1)
    ROUND = CapStyleType(2)
    PROJECTING = CapStyleType(3)


JoinStyleType = NewType('JoinStyleType', int)


class JoinStyleValues:
    MITER = JoinStyleType(0)
    ROUND = JoinStyleType(1)
    BEVEL = JoinStyleType(2)


FillStyleType = NewType('FillStyleType', int)


class FillStyleValues:
    SOLID = FillStyleType(0)
    TILED = FillStyleType(1)
    STIPPLED = FillStyleType(2)
    OPAQUE_STIPPLED = FillStyleType(3)


FillRuleType = NewType('FillRuleType', int)


class FillRuleValues:
    EVEN_ODD = FillRuleType(0)
    WINDING = FillRuleType(1)


SubwindowModeType = NewType('SubwindowModeType', int)


class SubwindowModeValues:
    CLIP_BY_CHILDREN = SubwindowModeType(0)
    INCLUDE_INFERIORS = SubwindowModeType(1)


ArcModeType = NewType('ArcModeType', int)


class ArcModeValues:
    CHORD = ArcModeType(0)
    PIE_SLICE = ArcModeType(1)


ClipOrderingType = NewType('ClipOrderingType', int)


class ClipOrderingValues:
    UNSORTED = ClipOrderingType(0)
    YSORTED = ClipOrderingType(1)
    YXSORTED = ClipOrderingType(2)
    YXBANDED = ClipOrderingType(3)


CoordModeType = NewType('CoordModeType', int)


class CoordModeValues:
    ORIGIN = CoordModeType(0)
    PREVIOUS = CoordModeType(1)


PolyShapeType = NewType('PolyShapeType', int)


class PolyShapeValues:
    COMPLEX = PolyShapeType(0)
    NONCONVEX = PolyShapeType(1)
    CONVEX = PolyShapeType(2)


ImageFormatType = NewType('ImageFormatType', int)


class ImageFormatValues:
    XYBITMAP = ImageFormatType(0)
    XYPIXMAP = ImageFormatType(1)
    ZPIXMAP = ImageFormatType(2)


ColormapAllocType = NewType('ColormapAllocType', int)


class ColormapAllocValues:
    NONE = ColormapAllocType(0)
    ALL = ColormapAllocType(1)


ColorFlagType = NewType('ColorFlagType', int)


class ColorFlagValues:
    RED = ColorFlagType(1)
    GREEN = ColorFlagType(2)
    BLUE = ColorFlagType(4)


PixmapType = NewType('PixmapType', int)


class PixmapValues:
    NONE = PixmapType(0)


FontType = NewType('FontType', int)


class FontValues:
    NONE = FontType(0)


QueryShapeOfType = NewType('QueryShapeOfType', int)


class QueryShapeOfValues:
    LARGEST_CURSOR = QueryShapeOfType(0)
    FASTEST_TILE = QueryShapeOfType(1)
    FASTEST_STIPPLE = QueryShapeOfType(2)


KbType = NewType('KbType', int)


class KbValues:
    KEY_CLICK_PERCENT = KbType(1)
    BELL_PERCENT = KbType(2)
    BELL_PITCH = KbType(4)
    BELL_DURATION = KbType(8)
    LED = KbType(16)
    LED_MODE = KbType(32)
    KEY = KbType(64)
    AUTO_REPEAT_MODE = KbType(128)


LedModeType = NewType('LedModeType', int)


class LedModeValues:
    OFF = LedModeType(0)
    ON = LedModeType(1)


AutoRepeatModeType = NewType('AutoRepeatModeType', int)


class AutoRepeatModeValues:
    OFF = AutoRepeatModeType(0)
    ON = AutoRepeatModeType(1)
    DEFAULT = AutoRepeatModeType(2)


BlankingType = NewType('BlankingType', int)


class BlankingValues:
    NOT_PREFERRED = BlankingType(0)
    PREFERRED = BlankingType(1)
    DEFAULT = BlankingType(2)


ExposuresType = NewType('ExposuresType', int)


class ExposuresValues:
    NOT_ALLOWED = ExposuresType(0)
    ALLOWED = ExposuresType(1)
    DEFAULT = ExposuresType(2)


HostModeType = NewType('HostModeType', int)


class HostModeValues:
    INSERT = HostModeType(0)
    DELETE = HostModeType(1)


FamilyType = NewType('FamilyType', int)


class FamilyValues:
    INTERNET = FamilyType(0)
    DECNET = FamilyType(1)
    CHAOS = FamilyType(2)
    SERVER_INTERPRETED = FamilyType(5)
    INTERNET6 = FamilyType(6)


AccessControlType = NewType('AccessControlType', int)


class AccessControlValues:
    DISABLE = AccessControlType(0)
    ENABLE = AccessControlType(1)


CloseDownType = NewType('CloseDownType', int)


class CloseDownValues:
    DESTROY_ALL = CloseDownType(0)
    RETAIN_PERMANENT = CloseDownType(1)
    RETAIN_TEMPORARY = CloseDownType(2)


KillType = NewType('KillType', int)


class KillValues:
    ALL_TEMPORARY = KillType(0)


ScreenSaverType = NewType('ScreenSaverType', int)


class ScreenSaverValues:
    RESET = ScreenSaverType(0)
    ACTIVE = ScreenSaverType(1)


MappingStatusType = NewType('MappingStatusType', int)


class MappingStatusValues:
    SUCCESS = MappingStatusType(0)
    BUSY = MappingStatusType(1)
    FAILURE = MappingStatusType(2)


MapIndexType = NewType('MapIndexType', int)


class MapIndexValues:
    SHIFT = MapIndexType(0)
    LOCK = MapIndexType(1)
    CONTROL = MapIndexType(2)
    V_1 = MapIndexType(3)
    V_2 = MapIndexType(4)
    V_3 = MapIndexType(5)
    V_4 = MapIndexType(6)
    V_5 = MapIndexType(7)


# ------------------------------------------------------------------
# Aliases

Cursor = NewType('Cursor', ctypes.c_uint32)
Pixmap = NewType('Pixmap', ctypes.c_uint32)
Colormap = NewType('Colormap', ctypes.c_uint32)
Atom = NewType('Atom', ctypes.c_uint32)
Font = NewType('Font', ctypes.c_uint32)
Window = NewType('Window', ctypes.c_uint32)
Gcontext = NewType('Gcontext', ctypes.c_uint32)


# ------------------------------------------------------------------
# Structures, Events, Requests, Replies


Char2BStructPacket = DataPacket((
    ('byte1', FixedDataPacketField(MARKER_UINT8)),
    ('byte2', FixedDataPacketField(MARKER_UINT8)),
))


class Char2BStruct:
    __slots__ = ('byte1', 'byte2',)

    def __init__(
            self, *,
            byte1: Optional[int] = None,
            byte2: Optional[int] = None,
    ) -> None:
        self.byte1 = byte1
        self.byte2 = byte2

    def as_dict(self) -> Dict[str, Any]:
        return {
            'byte1': self.byte1,
            'byte2': self.byte2,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'Char2BStruct':
        return Char2BStruct(**Char2BStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return Char2BStructPacket.pack(**self.as_dict())


class Char2BStructCType(ctypes.Structure):
    """xproto CHAR2B"""
    _fields_ = [
        ("byte1", ctypes.c_uint8),
        ("byte2", ctypes.c_uint8),
    ]


PointStructPacket = DataPacket((
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
))


class PointStruct:
    __slots__ = ('x', 'y',)

    def __init__(
            self, *,
            x: Optional[int] = None,
            y: Optional[int] = None,
    ) -> None:
        self.x = x
        self.y = y

    def as_dict(self) -> Dict[str, Any]:
        return {
            'x': self.x,
            'y': self.y,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PointStruct':
        return PointStruct(**PointStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PointStructPacket.pack(**self.as_dict())


class PointStructCType(ctypes.Structure):
    """xproto POINT"""
    _fields_ = [
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
    ]


RectangleStructPacket = DataPacket((
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
))


class RectangleStruct:
    __slots__ = ('x', 'y', 'width', 'height',)

    def __init__(
            self, *,
            x: Optional[int] = None,
            y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def as_dict(self) -> Dict[str, Any]:
        return {
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RectangleStruct':
        return RectangleStruct(**RectangleStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RectangleStructPacket.pack(**self.as_dict())


class RectangleStructCType(ctypes.Structure):
    """xproto RECTANGLE"""
    _fields_ = [
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
    ]


ArcStructPacket = DataPacket((
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('angle1', FixedDataPacketField(MARKER_INT16)),
    ('angle2', FixedDataPacketField(MARKER_INT16)),
))


class ArcStruct:
    __slots__ = ('x', 'y', 'width', 'height', 'angle1', 'angle2',)

    def __init__(
            self, *,
            x: Optional[int] = None,
            y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            angle1: Optional[int] = None,
            angle2: Optional[int] = None,
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle1 = angle1
        self.angle2 = angle2

    def as_dict(self) -> Dict[str, Any]:
        return {
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'angle1': self.angle1,
            'angle2': self.angle2,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ArcStruct':
        return ArcStruct(**ArcStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ArcStructPacket.pack(**self.as_dict())


class ArcStructCType(ctypes.Structure):
    """xproto ARC"""
    _fields_ = [
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("angle1", ctypes.c_int16),
        ("angle2", ctypes.c_int16),
    ]


FormatStructPacket = DataPacket((
    ('depth', FixedDataPacketField(MARKER_UINT8)),
    ('bits_per_pixel', FixedDataPacketField(MARKER_UINT8)),
    ('scanline_pad', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(5)),
))


class FormatStruct:
    __slots__ = ('depth', 'bits_per_pixel', 'scanline_pad',)

    def __init__(
            self, *,
            depth: Optional[int] = None,
            bits_per_pixel: Optional[int] = None,
            scanline_pad: Optional[int] = None,
    ) -> None:
        self.depth = depth
        self.bits_per_pixel = bits_per_pixel
        self.scanline_pad = scanline_pad

    def as_dict(self) -> Dict[str, Any]:
        return {
            'depth': self.depth,
            'bits_per_pixel': self.bits_per_pixel,
            'scanline_pad': self.scanline_pad,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FormatStruct':
        return FormatStruct(**FormatStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FormatStructPacket.pack(**self.as_dict())


class FormatStructCType(ctypes.Structure):
    """xproto FORMAT"""
    _fields_ = [
        ("depth", ctypes.c_uint8),
        ("bits_per_pixel", ctypes.c_uint8),
        ("scanline_pad", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 5),
    ]


VisualtypeStructPacket = DataPacket((
    ('visual_id', FixedDataPacketField(MARKER_UINT32)),
    ('class', FixedDataPacketField(MARKER_UINT8)),
    ('bits_per_rgb_value', FixedDataPacketField(MARKER_UINT8)),
    ('colormap_entries', FixedDataPacketField(MARKER_UINT16)),
    ('red_mask', FixedDataPacketField(MARKER_UINT32)),
    ('green_mask', FixedDataPacketField(MARKER_UINT32)),
    ('blue_mask', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(4)),
))


class VisualtypeStruct:
    __slots__ = ('visual_id', 'v_class', 'bits_per_rgb_value', 'colormap_entries', 'red_mask', 'green_mask', 'blue_mask',)

    def __init__(
            self, *,
            visual_id: Optional[int] = None,
            v_class: Optional[int] = None,
            bits_per_rgb_value: Optional[int] = None,
            colormap_entries: Optional[int] = None,
            red_mask: Optional[int] = None,
            green_mask: Optional[int] = None,
            blue_mask: Optional[int] = None,
    ) -> None:
        self.visual_id = visual_id
        self.v_class = v_class
        self.bits_per_rgb_value = bits_per_rgb_value
        self.colormap_entries = colormap_entries
        self.red_mask = red_mask
        self.green_mask = green_mask
        self.blue_mask = blue_mask

    def as_dict(self) -> Dict[str, Any]:
        return {
            'visual_id': self.visual_id,
            'class': self.v_class,
            'bits_per_rgb_value': self.bits_per_rgb_value,
            'colormap_entries': self.colormap_entries,
            'red_mask': self.red_mask,
            'green_mask': self.green_mask,
            'blue_mask': self.blue_mask,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'VisualtypeStruct':
        return VisualtypeStruct(**VisualtypeStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return VisualtypeStructPacket.pack(**self.as_dict())


class VisualtypeStructCType(ctypes.Structure):
    """xproto VISUALTYPE"""
    _fields_ = [
        ("visual_id", ctypes.c_uint32),
        ("class", ctypes.c_uint8),
        ("bits_per_rgb_value", ctypes.c_uint8),
        ("colormap_entries", ctypes.c_uint16),
        ("red_mask", ctypes.c_uint32),
        ("green_mask", ctypes.c_uint32),
        ("blue_mask", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 4),
    ]


DepthStructPacket = DataPacket((
    ('depth', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('visuals_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(4)),
    ('visuals', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['visuals_len'], 0)),
))


class DepthStruct:
    __slots__ = ('depth', 'visuals_len', 'visuals',)

    def __init__(
            self, *,
            depth: Optional[int] = None,
            visuals_len: Optional[int] = None,
            visuals: Optional[Sequence[int]] = None,
    ) -> None:
        self.depth = depth
        self.visuals_len = visuals_len
        self.visuals = visuals

    def as_dict(self) -> Dict[str, Any]:
        return {
            'depth': self.depth,
            'visuals_len': self.visuals_len,
            'visuals': self.visuals,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DepthStruct':
        return DepthStruct(**DepthStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DepthStructPacket.pack(**self.as_dict())


class DepthStructCType(ctypes.Structure):
    """xproto DEPTH"""
    _fields_ = [
        ("depth", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("visuals_len", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 4),
        ("var_data", ctypes.c_void_p),
    ]


ScreenStructPacket = DataPacket((
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('default_colormap', FixedDataPacketField(MARKER_UINT32)),
    ('white_pixel', FixedDataPacketField(MARKER_UINT32)),
    ('black_pixel', FixedDataPacketField(MARKER_UINT32)),
    ('current_input_masks', FixedDataPacketField(MARKER_UINT32)),
    ('width_in_pixels', FixedDataPacketField(MARKER_UINT16)),
    ('height_in_pixels', FixedDataPacketField(MARKER_UINT16)),
    ('width_in_millimeters', FixedDataPacketField(MARKER_UINT16)),
    ('height_in_millimeters', FixedDataPacketField(MARKER_UINT16)),
    ('min_installed_maps', FixedDataPacketField(MARKER_UINT16)),
    ('max_installed_maps', FixedDataPacketField(MARKER_UINT16)),
    ('root_visual', FixedDataPacketField(MARKER_UINT32)),
    ('backing_stores', FixedDataPacketField(MARKER_INT8)),
    ('save_unders', FixedDataPacketField(MARKER_UINT8)),
    ('root_depth', FixedDataPacketField(MARKER_UINT8)),
    ('allowed_depths_len', FixedDataPacketField(MARKER_UINT8)),
    ('allowed_depths', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['allowed_depths_len'], 0)),
))


class ScreenStruct:
    __slots__ = ('root', 'default_colormap', 'white_pixel', 'black_pixel', 'current_input_masks', 'width_in_pixels', 'height_in_pixels', 'width_in_millimeters', 'height_in_millimeters', 'min_installed_maps', 'max_installed_maps', 'root_visual', 'backing_stores', 'save_unders', 'root_depth', 'allowed_depths_len', 'allowed_depths',)

    def __init__(
            self, *,
            root: Optional[int] = None,
            default_colormap: Optional[int] = None,
            white_pixel: Optional[int] = None,
            black_pixel: Optional[int] = None,
            current_input_masks: Optional[int] = None,
            width_in_pixels: Optional[int] = None,
            height_in_pixels: Optional[int] = None,
            width_in_millimeters: Optional[int] = None,
            height_in_millimeters: Optional[int] = None,
            min_installed_maps: Optional[int] = None,
            max_installed_maps: Optional[int] = None,
            root_visual: Optional[int] = None,
            backing_stores: Optional[int] = None,
            save_unders: Optional[bool] = None,
            root_depth: Optional[int] = None,
            allowed_depths_len: Optional[int] = None,
            allowed_depths: Optional[Sequence[int]] = None,
    ) -> None:
        self.root = root
        self.default_colormap = default_colormap
        self.white_pixel = white_pixel
        self.black_pixel = black_pixel
        self.current_input_masks = current_input_masks
        self.width_in_pixels = width_in_pixels
        self.height_in_pixels = height_in_pixels
        self.width_in_millimeters = width_in_millimeters
        self.height_in_millimeters = height_in_millimeters
        self.min_installed_maps = min_installed_maps
        self.max_installed_maps = max_installed_maps
        self.root_visual = root_visual
        self.backing_stores = backing_stores
        self.save_unders = save_unders
        self.root_depth = root_depth
        self.allowed_depths_len = allowed_depths_len
        self.allowed_depths = allowed_depths

    def as_dict(self) -> Dict[str, Any]:
        return {
            'root': self.root,
            'default_colormap': self.default_colormap,
            'white_pixel': self.white_pixel,
            'black_pixel': self.black_pixel,
            'current_input_masks': self.current_input_masks,
            'width_in_pixels': self.width_in_pixels,
            'height_in_pixels': self.height_in_pixels,
            'width_in_millimeters': self.width_in_millimeters,
            'height_in_millimeters': self.height_in_millimeters,
            'min_installed_maps': self.min_installed_maps,
            'max_installed_maps': self.max_installed_maps,
            'root_visual': self.root_visual,
            'backing_stores': self.backing_stores,
            'save_unders': self.save_unders,
            'root_depth': self.root_depth,
            'allowed_depths_len': self.allowed_depths_len,
            'allowed_depths': self.allowed_depths,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ScreenStruct':
        return ScreenStruct(**ScreenStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ScreenStructPacket.pack(**self.as_dict())


class ScreenStructCType(ctypes.Structure):
    """xproto SCREEN"""
    _fields_ = [
        ("root", ctypes.c_uint32),
        ("default_colormap", ctypes.c_uint32),
        ("white_pixel", ctypes.c_uint32),
        ("black_pixel", ctypes.c_uint32),
        ("current_input_masks", ctypes.c_uint32),
        ("width_in_pixels", ctypes.c_uint16),
        ("height_in_pixels", ctypes.c_uint16),
        ("width_in_millimeters", ctypes.c_uint16),
        ("height_in_millimeters", ctypes.c_uint16),
        ("min_installed_maps", ctypes.c_uint16),
        ("max_installed_maps", ctypes.c_uint16),
        ("root_visual", ctypes.c_uint32),
        ("backing_stores", ctypes.c_int8),
        ("save_unders", ctypes.c_int8),
        ("root_depth", ctypes.c_uint8),
        ("allowed_depths_len", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


SetupRequestStructPacket = DataPacket((
    ('byte_order', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('protocol_major_version', FixedDataPacketField(MARKER_UINT16)),
    ('protocol_minor_version', FixedDataPacketField(MARKER_UINT16)),
    ('authorization_protocol_name_len', FixedDataPacketField(MARKER_UINT16)),
    ('authorization_protocol_data_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(2)),
    ('authorization_protocol_name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['authorization_protocol_name_len'], 0)),
    ('pad2', AlignedPadDataPacketField(4)),
    ('authorization_protocol_data', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['authorization_protocol_data_len'], 0)),
    ('pad3', AlignedPadDataPacketField(4)),
))


class SetupRequestStruct:
    __slots__ = ('byte_order', 'protocol_major_version', 'protocol_minor_version', 'authorization_protocol_name_len', 'authorization_protocol_data_len', 'authorization_protocol_name', 'authorization_protocol_data',)

    def __init__(
            self, *,
            byte_order: Optional[int] = None,
            protocol_major_version: Optional[int] = None,
            protocol_minor_version: Optional[int] = None,
            authorization_protocol_name_len: Optional[int] = None,
            authorization_protocol_data_len: Optional[int] = None,
            authorization_protocol_name: Optional[Sequence[int]] = None,
            authorization_protocol_data: Optional[Sequence[int]] = None,
    ) -> None:
        self.byte_order = byte_order
        self.protocol_major_version = protocol_major_version
        self.protocol_minor_version = protocol_minor_version
        self.authorization_protocol_name_len = authorization_protocol_name_len
        self.authorization_protocol_data_len = authorization_protocol_data_len
        self.authorization_protocol_name = authorization_protocol_name
        self.authorization_protocol_data = authorization_protocol_data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'byte_order': self.byte_order,
            'protocol_major_version': self.protocol_major_version,
            'protocol_minor_version': self.protocol_minor_version,
            'authorization_protocol_name_len': self.authorization_protocol_name_len,
            'authorization_protocol_data_len': self.authorization_protocol_data_len,
            'authorization_protocol_name': self.authorization_protocol_name,
            'authorization_protocol_data': self.authorization_protocol_data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetupRequestStruct':
        return SetupRequestStruct(**SetupRequestStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetupRequestStructPacket.pack(**self.as_dict())


class SetupRequestStructCType(ctypes.Structure):
    """xproto SetupRequest"""
    _fields_ = [
        ("byte_order", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("protocol_major_version", ctypes.c_uint16),
        ("protocol_minor_version", ctypes.c_uint16),
        ("authorization_protocol_name_len", ctypes.c_uint16),
        ("authorization_protocol_data_len", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


SetupFailedStructPacket = DataPacket((
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('reason_len', FixedDataPacketField(MARKER_UINT8)),
    ('protocol_major_version', FixedDataPacketField(MARKER_UINT16)),
    ('protocol_minor_version', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT16)),
    ('reason', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['reason_len'], 0)),
))


class SetupFailedStruct:
    __slots__ = ('status', 'reason_len', 'protocol_major_version', 'protocol_minor_version', 'length', 'reason',)

    def __init__(
            self, *,
            status: Optional[int] = None,
            reason_len: Optional[int] = None,
            protocol_major_version: Optional[int] = None,
            protocol_minor_version: Optional[int] = None,
            length: Optional[int] = None,
            reason: Optional[Sequence[int]] = None,
    ) -> None:
        self.status = status
        self.reason_len = reason_len
        self.protocol_major_version = protocol_major_version
        self.protocol_minor_version = protocol_minor_version
        self.length = length
        self.reason = reason

    def as_dict(self) -> Dict[str, Any]:
        return {
            'status': self.status,
            'reason_len': self.reason_len,
            'protocol_major_version': self.protocol_major_version,
            'protocol_minor_version': self.protocol_minor_version,
            'length': self.length,
            'reason': self.reason,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetupFailedStruct':
        return SetupFailedStruct(**SetupFailedStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetupFailedStructPacket.pack(**self.as_dict())


class SetupFailedStructCType(ctypes.Structure):
    """xproto SetupFailed"""
    _fields_ = [
        ("status", ctypes.c_uint8),
        ("reason_len", ctypes.c_uint8),
        ("protocol_major_version", ctypes.c_uint16),
        ("protocol_minor_version", ctypes.c_uint16),
        ("length", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


SetupAuthenticateStructPacket = DataPacket((
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(5)),
    ('length', FixedDataPacketField(MARKER_UINT16)),
    ('reason', SimpleListDataPacketField(MARKER_INT8, lambda d, c: (d['length']) * (4), 0)),
))


class SetupAuthenticateStruct:
    __slots__ = ('status', 'length', 'reason',)

    def __init__(
            self, *,
            status: Optional[int] = None,
            length: Optional[int] = None,
            reason: Optional[Sequence[int]] = None,
    ) -> None:
        self.status = status
        self.length = length
        self.reason = reason

    def as_dict(self) -> Dict[str, Any]:
        return {
            'status': self.status,
            'length': self.length,
            'reason': self.reason,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetupAuthenticateStruct':
        return SetupAuthenticateStruct(**SetupAuthenticateStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetupAuthenticateStructPacket.pack(**self.as_dict())


class SetupAuthenticateStructCType(ctypes.Structure):
    """xproto SetupAuthenticate"""
    _fields_ = [
        ("status", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 5),
        ("length", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


SetupStructPacket = DataPacket((
    ('status', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('protocol_major_version', FixedDataPacketField(MARKER_UINT16)),
    ('protocol_minor_version', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT16)),
    ('release_number', FixedDataPacketField(MARKER_UINT32)),
    ('resource_id_base', FixedDataPacketField(MARKER_UINT32)),
    ('resource_id_mask', FixedDataPacketField(MARKER_UINT32)),
    ('motion_buffer_size', FixedDataPacketField(MARKER_UINT32)),
    ('vendor_len', FixedDataPacketField(MARKER_UINT16)),
    ('maximum_request_length', FixedDataPacketField(MARKER_UINT16)),
    ('roots_len', FixedDataPacketField(MARKER_UINT8)),
    ('pixmap_formats_len', FixedDataPacketField(MARKER_UINT8)),
    ('image_byte_order', FixedDataPacketField(MARKER_UINT8)),
    ('bitmap_format_bit_order', FixedDataPacketField(MARKER_UINT8)),
    ('bitmap_format_scanline_unit', FixedDataPacketField(MARKER_UINT8)),
    ('bitmap_format_scanline_pad', FixedDataPacketField(MARKER_UINT8)),
    ('min_keycode', FixedDataPacketField(MARKER_UINT32)),
    ('max_keycode', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(4)),
    ('vendor', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['vendor_len'], 0)),
    ('pad2', AlignedPadDataPacketField(4)),
    ('pixmap_formats', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['pixmap_formats_len'], 0)),
    ('roots', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['roots_len'], 0)),
))


class SetupStruct:
    __slots__ = ('status', 'protocol_major_version', 'protocol_minor_version', 'length', 'release_number', 'resource_id_base', 'resource_id_mask', 'motion_buffer_size', 'vendor_len', 'maximum_request_length', 'roots_len', 'pixmap_formats_len', 'image_byte_order', 'bitmap_format_bit_order', 'bitmap_format_scanline_unit', 'bitmap_format_scanline_pad', 'min_keycode', 'max_keycode', 'vendor', 'pixmap_formats', 'roots',)

    def __init__(
            self, *,
            status: Optional[int] = None,
            protocol_major_version: Optional[int] = None,
            protocol_minor_version: Optional[int] = None,
            length: Optional[int] = None,
            release_number: Optional[int] = None,
            resource_id_base: Optional[int] = None,
            resource_id_mask: Optional[int] = None,
            motion_buffer_size: Optional[int] = None,
            vendor_len: Optional[int] = None,
            maximum_request_length: Optional[int] = None,
            roots_len: Optional[int] = None,
            pixmap_formats_len: Optional[int] = None,
            image_byte_order: Optional[int] = None,
            bitmap_format_bit_order: Optional[int] = None,
            bitmap_format_scanline_unit: Optional[int] = None,
            bitmap_format_scanline_pad: Optional[int] = None,
            min_keycode: Optional[int] = None,
            max_keycode: Optional[int] = None,
            vendor: Optional[Sequence[int]] = None,
            pixmap_formats: Optional[Sequence[int]] = None,
            roots: Optional[Sequence[int]] = None,
    ) -> None:
        self.status = status
        self.protocol_major_version = protocol_major_version
        self.protocol_minor_version = protocol_minor_version
        self.length = length
        self.release_number = release_number
        self.resource_id_base = resource_id_base
        self.resource_id_mask = resource_id_mask
        self.motion_buffer_size = motion_buffer_size
        self.vendor_len = vendor_len
        self.maximum_request_length = maximum_request_length
        self.roots_len = roots_len
        self.pixmap_formats_len = pixmap_formats_len
        self.image_byte_order = image_byte_order
        self.bitmap_format_bit_order = bitmap_format_bit_order
        self.bitmap_format_scanline_unit = bitmap_format_scanline_unit
        self.bitmap_format_scanline_pad = bitmap_format_scanline_pad
        self.min_keycode = min_keycode
        self.max_keycode = max_keycode
        self.vendor = vendor
        self.pixmap_formats = pixmap_formats
        self.roots = roots

    def as_dict(self) -> Dict[str, Any]:
        return {
            'status': self.status,
            'protocol_major_version': self.protocol_major_version,
            'protocol_minor_version': self.protocol_minor_version,
            'length': self.length,
            'release_number': self.release_number,
            'resource_id_base': self.resource_id_base,
            'resource_id_mask': self.resource_id_mask,
            'motion_buffer_size': self.motion_buffer_size,
            'vendor_len': self.vendor_len,
            'maximum_request_length': self.maximum_request_length,
            'roots_len': self.roots_len,
            'pixmap_formats_len': self.pixmap_formats_len,
            'image_byte_order': self.image_byte_order,
            'bitmap_format_bit_order': self.bitmap_format_bit_order,
            'bitmap_format_scanline_unit': self.bitmap_format_scanline_unit,
            'bitmap_format_scanline_pad': self.bitmap_format_scanline_pad,
            'min_keycode': self.min_keycode,
            'max_keycode': self.max_keycode,
            'vendor': self.vendor,
            'pixmap_formats': self.pixmap_formats,
            'roots': self.roots,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetupStruct':
        return SetupStruct(**SetupStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetupStructPacket.pack(**self.as_dict())


class SetupStructCType(ctypes.Structure):
    """xproto Setup"""
    _fields_ = [
        ("status", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("protocol_major_version", ctypes.c_uint16),
        ("protocol_minor_version", ctypes.c_uint16),
        ("length", ctypes.c_uint16),
        ("release_number", ctypes.c_uint32),
        ("resource_id_base", ctypes.c_uint32),
        ("resource_id_mask", ctypes.c_uint32),
        ("motion_buffer_size", ctypes.c_uint32),
        ("vendor_len", ctypes.c_uint16),
        ("maximum_request_length", ctypes.c_uint16),
        ("roots_len", ctypes.c_uint8),
        ("pixmap_formats_len", ctypes.c_uint8),
        ("image_byte_order", ctypes.c_uint8),
        ("bitmap_format_bit_order", ctypes.c_uint8),
        ("bitmap_format_scanline_unit", ctypes.c_uint8),
        ("bitmap_format_scanline_pad", ctypes.c_uint8),
        ("min_keycode", ctypes.c_uint32),
        ("max_keycode", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 4),
        ("var_data", ctypes.c_void_p),
    ]


KeyPressEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('detail', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('child', FixedDataPacketField(MARKER_UINT32)),
    ('root_x', FixedDataPacketField(MARKER_INT16)),
    ('root_y', FixedDataPacketField(MARKER_INT16)),
    ('event_x', FixedDataPacketField(MARKER_INT16)),
    ('event_y', FixedDataPacketField(MARKER_INT16)),
    ('state', FixedDataPacketField(MARKER_UINT16)),
    ('same_screen', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
))


class KeyPressEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'detail', 'time', 'root', 'event', 'child', 'root_x', 'root_y', 'event_x', 'event_y', 'state', 'same_screen',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            detail: Optional[int] = None,
            time: Optional[int] = None,
            root: Optional[int] = None,
            event: Optional[int] = None,
            child: Optional[int] = None,
            root_x: Optional[int] = None,
            root_y: Optional[int] = None,
            event_x: Optional[int] = None,
            event_y: Optional[int] = None,
            state: Optional[int] = None,
            same_screen: Optional[bool] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.detail = detail
        self.time = time
        self.root = root
        self.event = event
        self.child = child
        self.root_x = root_x
        self.root_y = root_y
        self.event_x = event_x
        self.event_y = event_y
        self.state = state
        self.same_screen = same_screen

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'detail': self.detail,
            'time': self.time,
            'root': self.root,
            'event': self.event,
            'child': self.child,
            'root_x': self.root_x,
            'root_y': self.root_y,
            'event_x': self.event_x,
            'event_y': self.event_y,
            'state': self.state,
            'same_screen': self.same_screen,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'KeyPressEvent':
        return KeyPressEvent(**KeyPressEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return KeyPressEventPacket.pack(**self.as_dict())


class KeyPressEventCType(ctypes.Structure):
    """xproto KeyPress"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("detail", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("root", ctypes.c_uint32),
        ("event", ctypes.c_uint32),
        ("child", ctypes.c_uint32),
        ("root_x", ctypes.c_int16),
        ("root_y", ctypes.c_int16),
        ("event_x", ctypes.c_int16),
        ("event_y", ctypes.c_int16),
        ("state", ctypes.c_uint16),
        ("same_screen", ctypes.c_int8),
        ("pad0", ctypes.c_uint8),
    ]


ButtonPressEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('detail', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('child', FixedDataPacketField(MARKER_UINT32)),
    ('root_x', FixedDataPacketField(MARKER_INT16)),
    ('root_y', FixedDataPacketField(MARKER_INT16)),
    ('event_x', FixedDataPacketField(MARKER_INT16)),
    ('event_y', FixedDataPacketField(MARKER_INT16)),
    ('state', FixedDataPacketField(MARKER_UINT16)),
    ('same_screen', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
))


class ButtonPressEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'detail', 'time', 'root', 'event', 'child', 'root_x', 'root_y', 'event_x', 'event_y', 'state', 'same_screen',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            detail: Optional[int] = None,
            time: Optional[int] = None,
            root: Optional[int] = None,
            event: Optional[int] = None,
            child: Optional[int] = None,
            root_x: Optional[int] = None,
            root_y: Optional[int] = None,
            event_x: Optional[int] = None,
            event_y: Optional[int] = None,
            state: Optional[int] = None,
            same_screen: Optional[bool] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.detail = detail
        self.time = time
        self.root = root
        self.event = event
        self.child = child
        self.root_x = root_x
        self.root_y = root_y
        self.event_x = event_x
        self.event_y = event_y
        self.state = state
        self.same_screen = same_screen

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'detail': self.detail,
            'time': self.time,
            'root': self.root,
            'event': self.event,
            'child': self.child,
            'root_x': self.root_x,
            'root_y': self.root_y,
            'event_x': self.event_x,
            'event_y': self.event_y,
            'state': self.state,
            'same_screen': self.same_screen,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ButtonPressEvent':
        return ButtonPressEvent(**ButtonPressEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ButtonPressEventPacket.pack(**self.as_dict())


class ButtonPressEventCType(ctypes.Structure):
    """xproto ButtonPress"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("detail", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("root", ctypes.c_uint32),
        ("event", ctypes.c_uint32),
        ("child", ctypes.c_uint32),
        ("root_x", ctypes.c_int16),
        ("root_y", ctypes.c_int16),
        ("event_x", ctypes.c_int16),
        ("event_y", ctypes.c_int16),
        ("state", ctypes.c_uint16),
        ("same_screen", ctypes.c_int8),
        ("pad0", ctypes.c_uint8),
    ]


MotionNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('detail', FixedDataPacketField(MARKER_INT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('child', FixedDataPacketField(MARKER_UINT32)),
    ('root_x', FixedDataPacketField(MARKER_INT16)),
    ('root_y', FixedDataPacketField(MARKER_INT16)),
    ('event_x', FixedDataPacketField(MARKER_INT16)),
    ('event_y', FixedDataPacketField(MARKER_INT16)),
    ('state', FixedDataPacketField(MARKER_UINT16)),
    ('same_screen', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
))


class MotionNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'detail', 'time', 'root', 'event', 'child', 'root_x', 'root_y', 'event_x', 'event_y', 'state', 'same_screen',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            detail: Optional[int] = None,
            time: Optional[int] = None,
            root: Optional[int] = None,
            event: Optional[int] = None,
            child: Optional[int] = None,
            root_x: Optional[int] = None,
            root_y: Optional[int] = None,
            event_x: Optional[int] = None,
            event_y: Optional[int] = None,
            state: Optional[int] = None,
            same_screen: Optional[bool] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.detail = detail
        self.time = time
        self.root = root
        self.event = event
        self.child = child
        self.root_x = root_x
        self.root_y = root_y
        self.event_x = event_x
        self.event_y = event_y
        self.state = state
        self.same_screen = same_screen

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'detail': self.detail,
            'time': self.time,
            'root': self.root,
            'event': self.event,
            'child': self.child,
            'root_x': self.root_x,
            'root_y': self.root_y,
            'event_x': self.event_x,
            'event_y': self.event_y,
            'state': self.state,
            'same_screen': self.same_screen,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'MotionNotifyEvent':
        return MotionNotifyEvent(**MotionNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return MotionNotifyEventPacket.pack(**self.as_dict())


class MotionNotifyEventCType(ctypes.Structure):
    """xproto MotionNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("detail", ctypes.c_int8),
        ("time", ctypes.c_uint32),
        ("root", ctypes.c_uint32),
        ("event", ctypes.c_uint32),
        ("child", ctypes.c_uint32),
        ("root_x", ctypes.c_int16),
        ("root_y", ctypes.c_int16),
        ("event_x", ctypes.c_int16),
        ("event_y", ctypes.c_int16),
        ("state", ctypes.c_uint16),
        ("same_screen", ctypes.c_int8),
        ("pad0", ctypes.c_uint8),
    ]


EnterNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('detail', FixedDataPacketField(MARKER_INT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('child', FixedDataPacketField(MARKER_UINT32)),
    ('root_x', FixedDataPacketField(MARKER_INT16)),
    ('root_y', FixedDataPacketField(MARKER_INT16)),
    ('event_x', FixedDataPacketField(MARKER_INT16)),
    ('event_y', FixedDataPacketField(MARKER_INT16)),
    ('state', FixedDataPacketField(MARKER_UINT16)),
    ('mode', FixedDataPacketField(MARKER_INT8)),
    ('same_screen_focus', FixedDataPacketField(MARKER_INT8)),
))


class EnterNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'detail', 'time', 'root', 'event', 'child', 'root_x', 'root_y', 'event_x', 'event_y', 'state', 'mode', 'same_screen_focus',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            detail: Optional[int] = None,
            time: Optional[int] = None,
            root: Optional[int] = None,
            event: Optional[int] = None,
            child: Optional[int] = None,
            root_x: Optional[int] = None,
            root_y: Optional[int] = None,
            event_x: Optional[int] = None,
            event_y: Optional[int] = None,
            state: Optional[int] = None,
            mode: Optional[int] = None,
            same_screen_focus: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.detail = detail
        self.time = time
        self.root = root
        self.event = event
        self.child = child
        self.root_x = root_x
        self.root_y = root_y
        self.event_x = event_x
        self.event_y = event_y
        self.state = state
        self.mode = mode
        self.same_screen_focus = same_screen_focus

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'detail': self.detail,
            'time': self.time,
            'root': self.root,
            'event': self.event,
            'child': self.child,
            'root_x': self.root_x,
            'root_y': self.root_y,
            'event_x': self.event_x,
            'event_y': self.event_y,
            'state': self.state,
            'mode': self.mode,
            'same_screen_focus': self.same_screen_focus,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'EnterNotifyEvent':
        return EnterNotifyEvent(**EnterNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return EnterNotifyEventPacket.pack(**self.as_dict())


class EnterNotifyEventCType(ctypes.Structure):
    """xproto EnterNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("detail", ctypes.c_int8),
        ("time", ctypes.c_uint32),
        ("root", ctypes.c_uint32),
        ("event", ctypes.c_uint32),
        ("child", ctypes.c_uint32),
        ("root_x", ctypes.c_int16),
        ("root_y", ctypes.c_int16),
        ("event_x", ctypes.c_int16),
        ("event_y", ctypes.c_int16),
        ("state", ctypes.c_uint16),
        ("mode", ctypes.c_int8),
        ("same_screen_focus", ctypes.c_int8),
    ]


FocusInEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('detail', FixedDataPacketField(MARKER_INT8)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('mode', FixedDataPacketField(MARKER_INT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class FocusInEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'detail', 'event', 'mode',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            detail: Optional[int] = None,
            event: Optional[int] = None,
            mode: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.detail = detail
        self.event = event
        self.mode = mode

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'detail': self.detail,
            'event': self.event,
            'mode': self.mode,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FocusInEvent':
        return FocusInEvent(**FocusInEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FocusInEventPacket.pack(**self.as_dict())


class FocusInEventCType(ctypes.Structure):
    """xproto FocusIn"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("detail", ctypes.c_int8),
        ("event", ctypes.c_uint32),
        ("mode", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


KeymapNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('keys', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 31, 0)),
))


class KeymapNotifyEvent:
    __slots__ = ('response_type', 'keys',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            keys: Optional[Sequence[int]] = None,
    ) -> None:
        self.response_type = response_type
        self.keys = keys

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'keys': self.keys,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'KeymapNotifyEvent':
        return KeymapNotifyEvent(**KeymapNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return KeymapNotifyEventPacket.pack(**self.as_dict())


class KeymapNotifyEventCType(ctypes.Structure):
    """xproto KeymapNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


ExposeEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_UINT16)),
    ('y', FixedDataPacketField(MARKER_UINT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('count', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(2)),
))


class ExposeEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'window', 'x', 'y', 'width', 'height', 'count',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            window: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            count: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.count = count

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'window': self.window,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'count': self.count,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ExposeEvent':
        return ExposeEvent(**ExposeEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ExposeEventPacket.pack(**self.as_dict())


class ExposeEventCType(ctypes.Structure):
    """xproto Expose"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
        ("x", ctypes.c_uint16),
        ("y", ctypes.c_uint16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("count", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 2),
    ]


GraphicsExposureEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_UINT16)),
    ('y', FixedDataPacketField(MARKER_UINT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('minor_opcode', FixedDataPacketField(MARKER_UINT16)),
    ('count', FixedDataPacketField(MARKER_UINT16)),
    ('major_opcode', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(3)),
))


class GraphicsExposureEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'drawable', 'x', 'y', 'width', 'height', 'minor_opcode', 'count', 'major_opcode',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            drawable: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            minor_opcode: Optional[int] = None,
            count: Optional[int] = None,
            major_opcode: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.drawable = drawable
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.minor_opcode = minor_opcode
        self.count = count
        self.major_opcode = major_opcode

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'drawable': self.drawable,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'minor_opcode': self.minor_opcode,
            'count': self.count,
            'major_opcode': self.major_opcode,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GraphicsExposureEvent':
        return GraphicsExposureEvent(**GraphicsExposureEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GraphicsExposureEventPacket.pack(**self.as_dict())


class GraphicsExposureEventCType(ctypes.Structure):
    """xproto GraphicsExposure"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("drawable", ctypes.c_uint32),
        ("x", ctypes.c_uint16),
        ("y", ctypes.c_uint16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("minor_opcode", ctypes.c_uint16),
        ("count", ctypes.c_uint16),
        ("major_opcode", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 3),
    ]


NoExposureEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('minor_opcode', FixedDataPacketField(MARKER_UINT16)),
    ('major_opcode', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(1)),
))


class NoExposureEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'drawable', 'minor_opcode', 'major_opcode',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            drawable: Optional[int] = None,
            minor_opcode: Optional[int] = None,
            major_opcode: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.drawable = drawable
        self.minor_opcode = minor_opcode
        self.major_opcode = major_opcode

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'drawable': self.drawable,
            'minor_opcode': self.minor_opcode,
            'major_opcode': self.major_opcode,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'NoExposureEvent':
        return NoExposureEvent(**NoExposureEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return NoExposureEventPacket.pack(**self.as_dict())


class NoExposureEventCType(ctypes.Structure):
    """xproto NoExposure"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("drawable", ctypes.c_uint32),
        ("minor_opcode", ctypes.c_uint16),
        ("major_opcode", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8),
    ]


VisibilityNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('state', FixedDataPacketField(MARKER_INT8)),
    ('pad1', FixedPadDataPacketField(3)),
))


class VisibilityNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'window', 'state',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            window: Optional[int] = None,
            state: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.window = window
        self.state = state

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'window': self.window,
            'state': self.state,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'VisibilityNotifyEvent':
        return VisibilityNotifyEvent(**VisibilityNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return VisibilityNotifyEventPacket.pack(**self.as_dict())


class VisibilityNotifyEventCType(ctypes.Structure):
    """xproto VisibilityNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
        ("state", ctypes.c_int8),
        ("pad1", ctypes.c_uint8 * 3),
    ]


CreateNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('parent', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('border_width', FixedDataPacketField(MARKER_UINT16)),
    ('override_redirect', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(1)),
))


class CreateNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'parent', 'window', 'x', 'y', 'width', 'height', 'border_width', 'override_redirect',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            parent: Optional[int] = None,
            window: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            border_width: Optional[int] = None,
            override_redirect: Optional[bool] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.parent = parent
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_width = border_width
        self.override_redirect = override_redirect

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'parent': self.parent,
            'window': self.window,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'border_width': self.border_width,
            'override_redirect': self.override_redirect,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateNotifyEvent':
        return CreateNotifyEvent(**CreateNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateNotifyEventPacket.pack(**self.as_dict())


class CreateNotifyEventCType(ctypes.Structure):
    """xproto CreateNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("parent", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("border_width", ctypes.c_uint16),
        ("override_redirect", ctypes.c_int8),
        ("pad1", ctypes.c_uint8),
    ]


DestroyNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class DestroyNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'event', 'window',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            event: Optional[int] = None,
            window: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.event = event
        self.window = window

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'event': self.event,
            'window': self.window,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DestroyNotifyEvent':
        return DestroyNotifyEvent(**DestroyNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DestroyNotifyEventPacket.pack(**self.as_dict())


class DestroyNotifyEventCType(ctypes.Structure):
    """xproto DestroyNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("event", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
    ]


UnmapNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('from_configure', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(3)),
))


class UnmapNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'event', 'window', 'from_configure',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            event: Optional[int] = None,
            window: Optional[int] = None,
            from_configure: Optional[bool] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.event = event
        self.window = window
        self.from_configure = from_configure

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'event': self.event,
            'window': self.window,
            'from_configure': self.from_configure,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'UnmapNotifyEvent':
        return UnmapNotifyEvent(**UnmapNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return UnmapNotifyEventPacket.pack(**self.as_dict())


class UnmapNotifyEventCType(ctypes.Structure):
    """xproto UnmapNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("event", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("from_configure", ctypes.c_int8),
        ("pad1", ctypes.c_uint8 * 3),
    ]


MapNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('override_redirect', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(3)),
))


class MapNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'event', 'window', 'override_redirect',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            event: Optional[int] = None,
            window: Optional[int] = None,
            override_redirect: Optional[bool] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.event = event
        self.window = window
        self.override_redirect = override_redirect

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'event': self.event,
            'window': self.window,
            'override_redirect': self.override_redirect,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'MapNotifyEvent':
        return MapNotifyEvent(**MapNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return MapNotifyEventPacket.pack(**self.as_dict())


class MapNotifyEventCType(ctypes.Structure):
    """xproto MapNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("event", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("override_redirect", ctypes.c_int8),
        ("pad1", ctypes.c_uint8 * 3),
    ]


MapRequestEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('parent', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class MapRequestEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'parent', 'window',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            parent: Optional[int] = None,
            window: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.parent = parent
        self.window = window

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'parent': self.parent,
            'window': self.window,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'MapRequestEvent':
        return MapRequestEvent(**MapRequestEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return MapRequestEventPacket.pack(**self.as_dict())


class MapRequestEventCType(ctypes.Structure):
    """xproto MapRequest"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("parent", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
    ]


ReparentNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('parent', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('override_redirect', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(3)),
))


class ReparentNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'event', 'window', 'parent', 'x', 'y', 'override_redirect',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            event: Optional[int] = None,
            window: Optional[int] = None,
            parent: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            override_redirect: Optional[bool] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.event = event
        self.window = window
        self.parent = parent
        self.x = x
        self.y = y
        self.override_redirect = override_redirect

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'event': self.event,
            'window': self.window,
            'parent': self.parent,
            'x': self.x,
            'y': self.y,
            'override_redirect': self.override_redirect,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ReparentNotifyEvent':
        return ReparentNotifyEvent(**ReparentNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ReparentNotifyEventPacket.pack(**self.as_dict())


class ReparentNotifyEventCType(ctypes.Structure):
    """xproto ReparentNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("event", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("parent", ctypes.c_uint32),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("override_redirect", ctypes.c_int8),
        ("pad1", ctypes.c_uint8 * 3),
    ]


ConfigureNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('above_sibling', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('border_width', FixedDataPacketField(MARKER_UINT16)),
    ('override_redirect', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(1)),
))


class ConfigureNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'event', 'window', 'above_sibling', 'x', 'y', 'width', 'height', 'border_width', 'override_redirect',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            event: Optional[int] = None,
            window: Optional[int] = None,
            above_sibling: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            border_width: Optional[int] = None,
            override_redirect: Optional[bool] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.event = event
        self.window = window
        self.above_sibling = above_sibling
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_width = border_width
        self.override_redirect = override_redirect

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'event': self.event,
            'window': self.window,
            'above_sibling': self.above_sibling,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'border_width': self.border_width,
            'override_redirect': self.override_redirect,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ConfigureNotifyEvent':
        return ConfigureNotifyEvent(**ConfigureNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ConfigureNotifyEventPacket.pack(**self.as_dict())


class ConfigureNotifyEventCType(ctypes.Structure):
    """xproto ConfigureNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("event", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("above_sibling", ctypes.c_uint32),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("border_width", ctypes.c_uint16),
        ("override_redirect", ctypes.c_int8),
        ("pad1", ctypes.c_uint8),
    ]


ConfigureRequestEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('stack_mode', FixedDataPacketField(MARKER_INT8)),
    ('parent', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('sibling', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('border_width', FixedDataPacketField(MARKER_UINT16)),
    ('value_mask', FixedDataPacketField(MARKER_UINT16)),
))


class ConfigureRequestEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'stack_mode', 'parent', 'window', 'sibling', 'x', 'y', 'width', 'height', 'border_width', 'value_mask',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            stack_mode: Optional[int] = None,
            parent: Optional[int] = None,
            window: Optional[int] = None,
            sibling: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            border_width: Optional[int] = None,
            value_mask: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.stack_mode = stack_mode
        self.parent = parent
        self.window = window
        self.sibling = sibling
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_width = border_width
        self.value_mask = value_mask

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'stack_mode': self.stack_mode,
            'parent': self.parent,
            'window': self.window,
            'sibling': self.sibling,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'border_width': self.border_width,
            'value_mask': self.value_mask,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ConfigureRequestEvent':
        return ConfigureRequestEvent(**ConfigureRequestEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ConfigureRequestEventPacket.pack(**self.as_dict())


class ConfigureRequestEventCType(ctypes.Structure):
    """xproto ConfigureRequest"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("stack_mode", ctypes.c_int8),
        ("parent", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("sibling", ctypes.c_uint32),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("border_width", ctypes.c_uint16),
        ("value_mask", ctypes.c_uint16),
    ]


GravityNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
))


class GravityNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'event', 'window', 'x', 'y',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            event: Optional[int] = None,
            window: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.event = event
        self.window = window
        self.x = x
        self.y = y

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'event': self.event,
            'window': self.window,
            'x': self.x,
            'y': self.y,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GravityNotifyEvent':
        return GravityNotifyEvent(**GravityNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GravityNotifyEventPacket.pack(**self.as_dict())


class GravityNotifyEventCType(ctypes.Structure):
    """xproto GravityNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("event", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
    ]


ResizeRequestEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
))


class ResizeRequestEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'window', 'width', 'height',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            window: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.window = window
        self.width = width
        self.height = height

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'window': self.window,
            'width': self.width,
            'height': self.height,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ResizeRequestEvent':
        return ResizeRequestEvent(**ResizeRequestEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ResizeRequestEventPacket.pack(**self.as_dict())


class ResizeRequestEventCType(ctypes.Structure):
    """xproto ResizeRequest"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
    ]


CirculateNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('event', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(4)),
    ('place', FixedDataPacketField(MARKER_INT8)),
    ('pad2', FixedPadDataPacketField(3)),
))


class CirculateNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'event', 'window', 'place',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            event: Optional[int] = None,
            window: Optional[int] = None,
            place: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.event = event
        self.window = window
        self.place = place

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'event': self.event,
            'window': self.window,
            'place': self.place,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CirculateNotifyEvent':
        return CirculateNotifyEvent(**CirculateNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CirculateNotifyEventPacket.pack(**self.as_dict())


class CirculateNotifyEventCType(ctypes.Structure):
    """xproto CirculateNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("event", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 4),
        ("place", ctypes.c_int8),
        ("pad2", ctypes.c_uint8 * 3),
    ]


PropertyNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('atom', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('state', FixedDataPacketField(MARKER_INT8)),
    ('pad1', FixedPadDataPacketField(3)),
))


class PropertyNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'window', 'atom', 'time', 'state',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            window: Optional[int] = None,
            atom: Optional[int] = None,
            time: Optional[int] = None,
            state: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.window = window
        self.atom = atom
        self.time = time
        self.state = state

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'window': self.window,
            'atom': self.atom,
            'time': self.time,
            'state': self.state,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PropertyNotifyEvent':
        return PropertyNotifyEvent(**PropertyNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PropertyNotifyEventPacket.pack(**self.as_dict())


class PropertyNotifyEventCType(ctypes.Structure):
    """xproto PropertyNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
        ("atom", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("state", ctypes.c_int8),
        ("pad1", ctypes.c_uint8 * 3),
    ]


SelectionClearEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('owner', FixedDataPacketField(MARKER_UINT32)),
    ('selection', FixedDataPacketField(MARKER_UINT32)),
))


class SelectionClearEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'time', 'owner', 'selection',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            time: Optional[int] = None,
            owner: Optional[int] = None,
            selection: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.time = time
        self.owner = owner
        self.selection = selection

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'time': self.time,
            'owner': self.owner,
            'selection': self.selection,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SelectionClearEvent':
        return SelectionClearEvent(**SelectionClearEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SelectionClearEventPacket.pack(**self.as_dict())


class SelectionClearEventCType(ctypes.Structure):
    """xproto SelectionClear"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("time", ctypes.c_uint32),
        ("owner", ctypes.c_uint32),
        ("selection", ctypes.c_uint32),
    ]


SelectionRequestEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('owner', FixedDataPacketField(MARKER_UINT32)),
    ('requestor', FixedDataPacketField(MARKER_UINT32)),
    ('selection', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
))


class SelectionRequestEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'time', 'owner', 'requestor', 'selection', 'target', 'property',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            time: Optional[int] = None,
            owner: Optional[int] = None,
            requestor: Optional[int] = None,
            selection: Optional[int] = None,
            target: Optional[int] = None,
            property: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.time = time
        self.owner = owner
        self.requestor = requestor
        self.selection = selection
        self.target = target
        self.property = property

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'time': self.time,
            'owner': self.owner,
            'requestor': self.requestor,
            'selection': self.selection,
            'target': self.target,
            'property': self.property,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SelectionRequestEvent':
        return SelectionRequestEvent(**SelectionRequestEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SelectionRequestEventPacket.pack(**self.as_dict())


class SelectionRequestEventCType(ctypes.Structure):
    """xproto SelectionRequest"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("time", ctypes.c_uint32),
        ("owner", ctypes.c_uint32),
        ("requestor", ctypes.c_uint32),
        ("selection", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("property", ctypes.c_uint32),
    ]


SelectionNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('requestor', FixedDataPacketField(MARKER_UINT32)),
    ('selection', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
))


class SelectionNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'time', 'requestor', 'selection', 'target', 'property',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            time: Optional[int] = None,
            requestor: Optional[int] = None,
            selection: Optional[int] = None,
            target: Optional[int] = None,
            property: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.time = time
        self.requestor = requestor
        self.selection = selection
        self.target = target
        self.property = property

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'time': self.time,
            'requestor': self.requestor,
            'selection': self.selection,
            'target': self.target,
            'property': self.property,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SelectionNotifyEvent':
        return SelectionNotifyEvent(**SelectionNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SelectionNotifyEventPacket.pack(**self.as_dict())


class SelectionNotifyEventCType(ctypes.Structure):
    """xproto SelectionNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("time", ctypes.c_uint32),
        ("requestor", ctypes.c_uint32),
        ("selection", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("property", ctypes.c_uint32),
    ]


ColormapNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('colormap', FixedDataPacketField(MARKER_UINT32)),
    ('new', FixedDataPacketField(MARKER_UINT8)),
    ('state', FixedDataPacketField(MARKER_INT8)),
    ('pad1', FixedPadDataPacketField(2)),
))


class ColormapNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'window', 'colormap', 'new', 'state',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            window: Optional[int] = None,
            colormap: Optional[int] = None,
            new: Optional[bool] = None,
            state: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.window = window
        self.colormap = colormap
        self.new = new
        self.state = state

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'window': self.window,
            'colormap': self.colormap,
            'new': self.new,
            'state': self.state,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ColormapNotifyEvent':
        return ColormapNotifyEvent(**ColormapNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ColormapNotifyEventPacket.pack(**self.as_dict())


class ColormapNotifyEventCType(ctypes.Structure):
    """xproto ColormapNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
        ("colormap", ctypes.c_uint32),
        ("new", ctypes.c_int8),
        ("state", ctypes.c_int8),
        ("pad1", ctypes.c_uint8 * 2),
    ]


ClientMessageEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('format', FixedDataPacketField(MARKER_UINT8)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('data', FixedDataPacketField(MARKER_UINT32)),
))


class ClientMessageEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'format', 'window', 'type', 'data',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            format: Optional[int] = None,
            window: Optional[int] = None,
            type: Optional[int] = None,
            data: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.format = format
        self.window = window
        self.type = type
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'format': self.format,
            'window': self.window,
            'type': self.type,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ClientMessageEvent':
        return ClientMessageEvent(**ClientMessageEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ClientMessageEventPacket.pack(**self.as_dict())


class ClientMessageEventCType(ctypes.Structure):
    """xproto ClientMessage"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("format", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("data", ctypes.c_uint32),
    ]


MappingNotifyEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('descriptor', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(1)),
    ('request', FixedDataPacketField(MARKER_INT8)),
    ('first_keycode', FixedDataPacketField(MARKER_UINT32)),
    ('count', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(1)),
))


class MappingNotifyEvent:
    __slots__ = ('response_type', 'descriptor', 'sequence', 'request', 'first_keycode', 'count',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            descriptor: Optional[int] = None,
            sequence: Optional[int] = None,
            request: Optional[int] = None,
            first_keycode: Optional[int] = None,
            count: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.descriptor = descriptor
        self.sequence = sequence
        self.request = request
        self.first_keycode = first_keycode
        self.count = count

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'descriptor': self.descriptor,
            'sequence': self.sequence,
            'request': self.request,
            'first_keycode': self.first_keycode,
            'count': self.count,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'MappingNotifyEvent':
        return MappingNotifyEvent(**MappingNotifyEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return MappingNotifyEventPacket.pack(**self.as_dict())


class MappingNotifyEventCType(ctypes.Structure):
    """xproto MappingNotify"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("descriptor", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8),
        ("request", ctypes.c_int8),
        ("first_keycode", ctypes.c_uint32),
        ("count", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8),
    ]


GeGenericEventPacket = DataPacket((
    ('response_type', FixedDataPacketField(MARKER_UINT8)),
    ('extension', FixedDataPacketField(MARKER_UINT8)),
    ('sequence', FixedDataPacketField(MARKER_UINT16)),
    ('length', FixedDataPacketField(MARKER_UINT32)),
    ('event_type', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(22)),
))


class GeGenericEvent:
    __slots__ = ('response_type', 'extension', 'sequence', 'length', 'event_type',)

    def __init__(
            self, *,
            response_type: Optional[int] = None,
            extension: Optional[int] = None,
            sequence: Optional[int] = None,
            length: Optional[int] = None,
            event_type: Optional[int] = None,
    ) -> None:
        self.response_type = response_type
        self.extension = extension
        self.sequence = sequence
        self.length = length
        self.event_type = event_type

    def as_dict(self) -> Dict[str, Any]:
        return {
            'response_type': self.response_type,
            'extension': self.extension,
            'sequence': self.sequence,
            'length': self.length,
            'event_type': self.event_type,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GeGenericEvent':
        return GeGenericEvent(**GeGenericEventPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GeGenericEventPacket.pack(**self.as_dict())


class GeGenericEventCType(ctypes.Structure):
    """xproto GeGeneric"""
    _fields_ = [
        ("response_type", ctypes.c_uint8),
        ("extension", ctypes.c_uint8),
        ("sequence", ctypes.c_uint16),
        ("length", ctypes.c_uint32),
        ("event_type", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 22),
    ]


CreateWindowRequestPacket = DataPacket((
    ('depth', FixedDataPacketField(MARKER_UINT8)),
    ('wid', FixedDataPacketField(MARKER_UINT32)),
    ('parent', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('border_width', FixedDataPacketField(MARKER_UINT16)),
    ('class', FixedDataPacketField(MARKER_UINT16)),
    ('visual', FixedDataPacketField(MARKER_UINT32)),
    ('value_mask', FixedDataPacketField(MARKER_UINT32)),
    ('value_list', BitDataPacketField(lambda d, c: d['value_mask'], {
        CwValues.BACK_PIXMAP: FixedDataPacketField(MARKER_UINT32),
        CwValues.BACK_PIXEL: FixedDataPacketField(MARKER_UINT32),
        CwValues.BORDER_PIXMAP: FixedDataPacketField(MARKER_UINT32),
        CwValues.BORDER_PIXEL: FixedDataPacketField(MARKER_UINT32),
        CwValues.BIT_GRAVITY: FixedDataPacketField(MARKER_UINT32),
        CwValues.WIN_GRAVITY: FixedDataPacketField(MARKER_UINT32),
        CwValues.BACKING_STORE: FixedDataPacketField(MARKER_UINT32),
        CwValues.BACKING_PLANES: FixedDataPacketField(MARKER_UINT32),
        CwValues.BACKING_PIXEL: FixedDataPacketField(MARKER_UINT32),
        CwValues.OVERRIDE_REDIRECT: FixedDataPacketField(MARKER_UINT32),
        CwValues.SAVE_UNDER: FixedDataPacketField(MARKER_UINT32),
        CwValues.EVENT_MASK: FixedDataPacketField(MARKER_UINT32),
        CwValues.DONT_PROPAGATE: FixedDataPacketField(MARKER_UINT32),
        CwValues.COLORMAP: FixedDataPacketField(MARKER_UINT32),
        CwValues.CURSOR: FixedDataPacketField(MARKER_UINT32),
    }, 0)),
))


class CreateWindowRequest:
    OPCODE = 1

    __slots__ = ('depth', 'wid', 'parent', 'x', 'y', 'width', 'height', 'border_width', 'v_class', 'visual', 'value_mask', 'value_list',)

    def __init__(
            self, *,
            depth: Optional[int] = None,
            wid: Optional[int] = None,
            parent: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            border_width: Optional[int] = None,
            v_class: Optional[int] = None,
            visual: Optional[int] = None,
            value_mask: Optional[int] = None,
            value_list: Optional[Mapping[str, CwValues]] = None,
    ) -> None:
        self.depth = depth
        self.wid = wid
        self.parent = parent
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_width = border_width
        self.v_class = v_class
        self.visual = visual
        self.value_mask = value_mask
        self.value_list = value_list

    def as_dict(self) -> Dict[str, Any]:
        return {
            'depth': self.depth,
            'wid': self.wid,
            'parent': self.parent,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'border_width': self.border_width,
            'class': self.v_class,
            'visual': self.visual,
            'value_mask': self.value_mask,
            'value_list': self.value_list,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateWindowRequest':
        return CreateWindowRequest(**CreateWindowRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateWindowRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int, Mapping[str, CwValues]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateWindowRequest.lib = library.xproto_createwindow
        CreateWindowRequest.lib.restype = ctypes.c_uint32
        CreateWindowRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class CreateWindowRequestCType(ctypes.Structure):
    """xproto CreateWindow"""
    _fields_ = [
        ("depth", ctypes.c_uint8),
        ("wid", ctypes.c_uint32),
        ("parent", ctypes.c_uint32),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("border_width", ctypes.c_uint16),
        ("class", ctypes.c_uint16),
        ("visual", ctypes.c_uint32),
        ("value_mask", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


ChangeWindowAttributesRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('value_mask', FixedDataPacketField(MARKER_UINT32)),
    ('value_list', BitDataPacketField(lambda d, c: d['value_mask'], {
        CwValues.BACK_PIXMAP: FixedDataPacketField(MARKER_UINT32),
        CwValues.BACK_PIXEL: FixedDataPacketField(MARKER_UINT32),
        CwValues.BORDER_PIXMAP: FixedDataPacketField(MARKER_UINT32),
        CwValues.BORDER_PIXEL: FixedDataPacketField(MARKER_UINT32),
        CwValues.BIT_GRAVITY: FixedDataPacketField(MARKER_UINT32),
        CwValues.WIN_GRAVITY: FixedDataPacketField(MARKER_UINT32),
        CwValues.BACKING_STORE: FixedDataPacketField(MARKER_UINT32),
        CwValues.BACKING_PLANES: FixedDataPacketField(MARKER_UINT32),
        CwValues.BACKING_PIXEL: FixedDataPacketField(MARKER_UINT32),
        CwValues.OVERRIDE_REDIRECT: FixedDataPacketField(MARKER_UINT32),
        CwValues.SAVE_UNDER: FixedDataPacketField(MARKER_UINT32),
        CwValues.EVENT_MASK: FixedDataPacketField(MARKER_UINT32),
        CwValues.DONT_PROPAGATE: FixedDataPacketField(MARKER_UINT32),
        CwValues.COLORMAP: FixedDataPacketField(MARKER_UINT32),
        CwValues.CURSOR: FixedDataPacketField(MARKER_UINT32),
    }, 0)),
))


class ChangeWindowAttributesRequest:
    OPCODE = 2

    __slots__ = ('window', 'value_mask', 'value_list',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            value_mask: Optional[int] = None,
            value_list: Optional[Mapping[str, CwValues]] = None,
    ) -> None:
        self.window = window
        self.value_mask = value_mask
        self.value_list = value_list

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'value_mask': self.value_mask,
            'value_list': self.value_list,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeWindowAttributesRequest':
        return ChangeWindowAttributesRequest(**ChangeWindowAttributesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeWindowAttributesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Mapping[str, CwValues]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangeWindowAttributesRequest.lib = library.xproto_changewindowattributes
        ChangeWindowAttributesRequest.lib.restype = ctypes.c_uint32
        ChangeWindowAttributesRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class ChangeWindowAttributesRequestCType(ctypes.Structure):
    """xproto ChangeWindowAttributes"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
        ("value_mask", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


GetWindowAttributesRequestCookie = NewType('GetWindowAttributesRequestCookie', ctypes.c_uint32)


GetWindowAttributesRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class GetWindowAttributesRequest:
    OPCODE = 3

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
    def from_data(inp: BinaryIO) -> 'GetWindowAttributesRequest':
        return GetWindowAttributesRequest(**GetWindowAttributesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetWindowAttributesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetWindowAttributesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetWindowAttributesRequest.lib = library.xproto_getwindowattributes
        GetWindowAttributesRequest.lib.restype = GetWindowAttributesRequestCookie
        GetWindowAttributesRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class GetWindowAttributesRequestCType(ctypes.Structure):
    """xproto GetWindowAttributes"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
    ]


GetWindowAttributesReplyReplyPacket = DataPacket((
    ('backing_store', FixedDataPacketField(MARKER_UINT8)),
    ('visual', FixedDataPacketField(MARKER_UINT32)),
    ('class', FixedDataPacketField(MARKER_UINT16)),
    ('bit_gravity', FixedDataPacketField(MARKER_UINT8)),
    ('win_gravity', FixedDataPacketField(MARKER_UINT8)),
    ('backing_planes', FixedDataPacketField(MARKER_UINT32)),
    ('backing_pixel', FixedDataPacketField(MARKER_UINT32)),
    ('save_under', FixedDataPacketField(MARKER_UINT8)),
    ('map_is_installed', FixedDataPacketField(MARKER_UINT8)),
    ('map_state', FixedDataPacketField(MARKER_UINT8)),
    ('override_redirect', FixedDataPacketField(MARKER_UINT8)),
    ('colormap', FixedDataPacketField(MARKER_UINT32)),
    ('all_event_masks', FixedDataPacketField(MARKER_UINT32)),
    ('your_event_mask', FixedDataPacketField(MARKER_UINT32)),
    ('do_not_propagate_mask', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
))


class GetWindowAttributesReplyReply:
    __slots__ = ('backing_store', 'visual', 'v_class', 'bit_gravity', 'win_gravity', 'backing_planes', 'backing_pixel', 'save_under', 'map_is_installed', 'map_state', 'override_redirect', 'colormap', 'all_event_masks', 'your_event_mask', 'do_not_propagate_mask',)

    def __init__(
            self, *,
            backing_store: Optional[int] = None,
            visual: Optional[int] = None,
            v_class: Optional[int] = None,
            bit_gravity: Optional[int] = None,
            win_gravity: Optional[int] = None,
            backing_planes: Optional[int] = None,
            backing_pixel: Optional[int] = None,
            save_under: Optional[bool] = None,
            map_is_installed: Optional[bool] = None,
            map_state: Optional[int] = None,
            override_redirect: Optional[bool] = None,
            colormap: Optional[int] = None,
            all_event_masks: Optional[int] = None,
            your_event_mask: Optional[int] = None,
            do_not_propagate_mask: Optional[int] = None,
    ) -> None:
        self.backing_store = backing_store
        self.visual = visual
        self.v_class = v_class
        self.bit_gravity = bit_gravity
        self.win_gravity = win_gravity
        self.backing_planes = backing_planes
        self.backing_pixel = backing_pixel
        self.save_under = save_under
        self.map_is_installed = map_is_installed
        self.map_state = map_state
        self.override_redirect = override_redirect
        self.colormap = colormap
        self.all_event_masks = all_event_masks
        self.your_event_mask = your_event_mask
        self.do_not_propagate_mask = do_not_propagate_mask

    def as_dict(self) -> Dict[str, Any]:
        return {
            'backing_store': self.backing_store,
            'visual': self.visual,
            'class': self.v_class,
            'bit_gravity': self.bit_gravity,
            'win_gravity': self.win_gravity,
            'backing_planes': self.backing_planes,
            'backing_pixel': self.backing_pixel,
            'save_under': self.save_under,
            'map_is_installed': self.map_is_installed,
            'map_state': self.map_state,
            'override_redirect': self.override_redirect,
            'colormap': self.colormap,
            'all_event_masks': self.all_event_masks,
            'your_event_mask': self.your_event_mask,
            'do_not_propagate_mask': self.do_not_propagate_mask,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetWindowAttributesReplyReply':
        return GetWindowAttributesReplyReply(**GetWindowAttributesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetWindowAttributesReplyReplyPacket.pack(**self.as_dict())


class GetWindowAttributesReplyReplyCType(ctypes.Structure):
    """xproto GetWindowAttributes_reply"""
    _fields_ = [
        ("backing_store", ctypes.c_uint8),
        ("visual", ctypes.c_uint32),
        ("class", ctypes.c_uint16),
        ("bit_gravity", ctypes.c_uint8),
        ("win_gravity", ctypes.c_uint8),
        ("backing_planes", ctypes.c_uint32),
        ("backing_pixel", ctypes.c_uint32),
        ("save_under", ctypes.c_int8),
        ("map_is_installed", ctypes.c_int8),
        ("map_state", ctypes.c_uint8),
        ("override_redirect", ctypes.c_int8),
        ("colormap", ctypes.c_uint32),
        ("all_event_masks", ctypes.c_uint32),
        ("your_event_mask", ctypes.c_uint32),
        ("do_not_propagate_mask", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
    ]


DestroyWindowRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class DestroyWindowRequest:
    OPCODE = 4

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
    def from_data(inp: BinaryIO) -> 'DestroyWindowRequest':
        return DestroyWindowRequest(**DestroyWindowRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DestroyWindowRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DestroyWindowRequest.lib = library.xproto_destroywindow
        DestroyWindowRequest.lib.restype = ctypes.c_uint32
        DestroyWindowRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class DestroyWindowRequestCType(ctypes.Structure):
    """xproto DestroyWindow"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
    ]


DestroySubwindowsRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class DestroySubwindowsRequest:
    OPCODE = 5

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
    def from_data(inp: BinaryIO) -> 'DestroySubwindowsRequest':
        return DestroySubwindowsRequest(**DestroySubwindowsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DestroySubwindowsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DestroySubwindowsRequest.lib = library.xproto_destroysubwindows
        DestroySubwindowsRequest.lib.restype = ctypes.c_uint32
        DestroySubwindowsRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class DestroySubwindowsRequestCType(ctypes.Structure):
    """xproto DestroySubwindows"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
    ]


ChangeSaveSetRequestPacket = DataPacket((
    ('mode', FixedDataPacketField(MARKER_INT8)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class ChangeSaveSetRequest:
    OPCODE = 6

    __slots__ = ('mode', 'window',)

    def __init__(
            self, *,
            mode: Optional[int] = None,
            window: Optional[int] = None,
    ) -> None:
        self.mode = mode
        self.window = window

    def as_dict(self) -> Dict[str, Any]:
        return {
            'mode': self.mode,
            'window': self.window,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeSaveSetRequest':
        return ChangeSaveSetRequest(**ChangeSaveSetRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeSaveSetRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangeSaveSetRequest.lib = library.xproto_changesaveset
        ChangeSaveSetRequest.lib.restype = ctypes.c_uint32
        ChangeSaveSetRequest.lib.argstype = (ctypes.c_int8, ctypes.c_uint32)


class ChangeSaveSetRequestCType(ctypes.Structure):
    """xproto ChangeSaveSet"""
    _fields_ = [
        ("mode", ctypes.c_int8),
        ("window", ctypes.c_uint32),
    ]


ReparentWindowRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('parent', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
))


class ReparentWindowRequest:
    OPCODE = 7

    __slots__ = ('window', 'parent', 'x', 'y',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            parent: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
    ) -> None:
        self.window = window
        self.parent = parent
        self.x = x
        self.y = y

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'parent': self.parent,
            'x': self.x,
            'y': self.y,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ReparentWindowRequest':
        return ReparentWindowRequest(**ReparentWindowRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ReparentWindowRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ReparentWindowRequest.lib = library.xproto_reparentwindow
        ReparentWindowRequest.lib.restype = ctypes.c_uint32
        ReparentWindowRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16)


class ReparentWindowRequestCType(ctypes.Structure):
    """xproto ReparentWindow"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
        ("parent", ctypes.c_uint32),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
    ]


MapWindowRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class MapWindowRequest:
    OPCODE = 8

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
    def from_data(inp: BinaryIO) -> 'MapWindowRequest':
        return MapWindowRequest(**MapWindowRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return MapWindowRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        MapWindowRequest.lib = library.xproto_mapwindow
        MapWindowRequest.lib.restype = ctypes.c_uint32
        MapWindowRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class MapWindowRequestCType(ctypes.Structure):
    """xproto MapWindow"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
    ]


MapSubwindowsRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class MapSubwindowsRequest:
    OPCODE = 9

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
    def from_data(inp: BinaryIO) -> 'MapSubwindowsRequest':
        return MapSubwindowsRequest(**MapSubwindowsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return MapSubwindowsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        MapSubwindowsRequest.lib = library.xproto_mapsubwindows
        MapSubwindowsRequest.lib.restype = ctypes.c_uint32
        MapSubwindowsRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class MapSubwindowsRequestCType(ctypes.Structure):
    """xproto MapSubwindows"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
    ]


UnmapWindowRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class UnmapWindowRequest:
    OPCODE = 10

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
    def from_data(inp: BinaryIO) -> 'UnmapWindowRequest':
        return UnmapWindowRequest(**UnmapWindowRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return UnmapWindowRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        UnmapWindowRequest.lib = library.xproto_unmapwindow
        UnmapWindowRequest.lib.restype = ctypes.c_uint32
        UnmapWindowRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class UnmapWindowRequestCType(ctypes.Structure):
    """xproto UnmapWindow"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
    ]


UnmapSubwindowsRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class UnmapSubwindowsRequest:
    OPCODE = 11

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
    def from_data(inp: BinaryIO) -> 'UnmapSubwindowsRequest':
        return UnmapSubwindowsRequest(**UnmapSubwindowsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return UnmapSubwindowsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        UnmapSubwindowsRequest.lib = library.xproto_unmapsubwindows
        UnmapSubwindowsRequest.lib.restype = ctypes.c_uint32
        UnmapSubwindowsRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class UnmapSubwindowsRequestCType(ctypes.Structure):
    """xproto UnmapSubwindows"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
    ]


ConfigureWindowRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('value_mask', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(2)),
    ('value_list', BitDataPacketField(lambda d, c: d['value_mask'], {
        ConfigWindowValues.X: FixedDataPacketField(MARKER_INT32),
        ConfigWindowValues.Y: FixedDataPacketField(MARKER_INT32),
        ConfigWindowValues.WIDTH: FixedDataPacketField(MARKER_UINT32),
        ConfigWindowValues.HEIGHT: FixedDataPacketField(MARKER_UINT32),
        ConfigWindowValues.BORDER_WIDTH: FixedDataPacketField(MARKER_UINT32),
        ConfigWindowValues.SIBLING: FixedDataPacketField(MARKER_UINT32),
        ConfigWindowValues.STACK_MODE: FixedDataPacketField(MARKER_UINT32),
    }, 0)),
))


class ConfigureWindowRequest:
    OPCODE = 12

    __slots__ = ('window', 'value_mask', 'value_list',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            value_mask: Optional[int] = None,
            value_list: Optional[Mapping[str, ConfigWindowValues]] = None,
    ) -> None:
        self.window = window
        self.value_mask = value_mask
        self.value_list = value_list

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'value_mask': self.value_mask,
            'value_list': self.value_list,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ConfigureWindowRequest':
        return ConfigureWindowRequest(**ConfigureWindowRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ConfigureWindowRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Mapping[str, ConfigWindowValues]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ConfigureWindowRequest.lib = library.xproto_configurewindow
        ConfigureWindowRequest.lib.restype = ctypes.c_uint32
        ConfigureWindowRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_void_p)


class ConfigureWindowRequestCType(ctypes.Structure):
    """xproto ConfigureWindow"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
        ("value_mask", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


CirculateWindowRequestPacket = DataPacket((
    ('direction', FixedDataPacketField(MARKER_UINT8)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class CirculateWindowRequest:
    OPCODE = 13

    __slots__ = ('direction', 'window',)

    def __init__(
            self, *,
            direction: Optional[int] = None,
            window: Optional[int] = None,
    ) -> None:
        self.direction = direction
        self.window = window

    def as_dict(self) -> Dict[str, Any]:
        return {
            'direction': self.direction,
            'window': self.window,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CirculateWindowRequest':
        return CirculateWindowRequest(**CirculateWindowRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CirculateWindowRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CirculateWindowRequest.lib = library.xproto_circulatewindow
        CirculateWindowRequest.lib.restype = ctypes.c_uint32
        CirculateWindowRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class CirculateWindowRequestCType(ctypes.Structure):
    """xproto CirculateWindow"""
    _fields_ = [
        ("direction", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
    ]


GetGeometryRequestCookie = NewType('GetGeometryRequestCookie', ctypes.c_uint32)


GetGeometryRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
))


class GetGeometryRequest:
    OPCODE = 14

    __slots__ = ('drawable',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
    ) -> None:
        self.drawable = drawable

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetGeometryRequest':
        return GetGeometryRequest(**GetGeometryRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetGeometryRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetGeometryRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetGeometryRequest.lib = library.xproto_getgeometry
        GetGeometryRequest.lib.restype = GetGeometryRequestCookie
        GetGeometryRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class GetGeometryRequestCType(ctypes.Structure):
    """xproto GetGeometry"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("drawable", ctypes.c_uint32),
    ]


GetGeometryReplyReplyPacket = DataPacket((
    ('depth', FixedDataPacketField(MARKER_UINT8)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('border_width', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
))


class GetGeometryReplyReply:
    __slots__ = ('depth', 'root', 'x', 'y', 'width', 'height', 'border_width',)

    def __init__(
            self, *,
            depth: Optional[int] = None,
            root: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            border_width: Optional[int] = None,
    ) -> None:
        self.depth = depth
        self.root = root
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_width = border_width

    def as_dict(self) -> Dict[str, Any]:
        return {
            'depth': self.depth,
            'root': self.root,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'border_width': self.border_width,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetGeometryReplyReply':
        return GetGeometryReplyReply(**GetGeometryReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetGeometryReplyReplyPacket.pack(**self.as_dict())


class GetGeometryReplyReplyCType(ctypes.Structure):
    """xproto GetGeometry_reply"""
    _fields_ = [
        ("depth", ctypes.c_uint8),
        ("root", ctypes.c_uint32),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("border_width", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
    ]


QueryTreeRequestCookie = NewType('QueryTreeRequestCookie', ctypes.c_uint32)


QueryTreeRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class QueryTreeRequest:
    OPCODE = 15

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
    def from_data(inp: BinaryIO) -> 'QueryTreeRequest':
        return QueryTreeRequest(**QueryTreeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryTreeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], QueryTreeRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryTreeRequest.lib = library.xproto_querytree
        QueryTreeRequest.lib.restype = QueryTreeRequestCookie
        QueryTreeRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class QueryTreeRequestCType(ctypes.Structure):
    """xproto QueryTree"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
    ]


QueryTreeReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('parent', FixedDataPacketField(MARKER_UINT32)),
    ('children_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(14)),
    ('children', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['children_len'], 0)),
))


class QueryTreeReplyReply:
    __slots__ = ('root', 'parent', 'children_len', 'children',)

    def __init__(
            self, *,
            root: Optional[int] = None,
            parent: Optional[int] = None,
            children_len: Optional[int] = None,
            children: Optional[Sequence[int]] = None,
    ) -> None:
        self.root = root
        self.parent = parent
        self.children_len = children_len
        self.children = children

    def as_dict(self) -> Dict[str, Any]:
        return {
            'root': self.root,
            'parent': self.parent,
            'children_len': self.children_len,
            'children': self.children,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryTreeReplyReply':
        return QueryTreeReplyReply(**QueryTreeReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryTreeReplyReplyPacket.pack(**self.as_dict())


class QueryTreeReplyReplyCType(ctypes.Structure):
    """xproto QueryTree_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("root", ctypes.c_uint32),
        ("parent", ctypes.c_uint32),
        ("children_len", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 14),
        ("var_data", ctypes.c_void_p),
    ]


InternAtomRequestCookie = NewType('InternAtomRequestCookie', ctypes.c_uint32)


InternAtomRequestPacket = DataPacket((
    ('only_if_exists', FixedDataPacketField(MARKER_UINT8)),
    ('name_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['name_len'], 0)),
))


class InternAtomRequest:
    OPCODE = 16

    __slots__ = ('only_if_exists', 'name_len', 'name',)

    def __init__(
            self, *,
            only_if_exists: Optional[bool] = None,
            name_len: Optional[int] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.only_if_exists = only_if_exists
        self.name_len = name_len
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'only_if_exists': self.only_if_exists,
            'name_len': self.name_len,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'InternAtomRequest':
        return InternAtomRequest(**InternAtomRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return InternAtomRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[bool, int, Sequence[int]], InternAtomRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        InternAtomRequest.lib = library.xproto_internatom
        InternAtomRequest.lib.restype = InternAtomRequestCookie
        InternAtomRequest.lib.argstype = (ctypes.c_int8, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_void_p)


class InternAtomRequestCType(ctypes.Structure):
    """xproto InternAtom"""
    _fields_ = [
        ("only_if_exists", ctypes.c_int8),
        ("name_len", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


InternAtomReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('atom', FixedDataPacketField(MARKER_UINT32)),
))


class InternAtomReplyReply:
    __slots__ = ('atom',)

    def __init__(
            self, *,
            atom: Optional[int] = None,
    ) -> None:
        self.atom = atom

    def as_dict(self) -> Dict[str, Any]:
        return {
            'atom': self.atom,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'InternAtomReplyReply':
        return InternAtomReplyReply(**InternAtomReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return InternAtomReplyReplyPacket.pack(**self.as_dict())


class InternAtomReplyReplyCType(ctypes.Structure):
    """xproto InternAtom_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("atom", ctypes.c_uint32),
    ]


GetAtomNameRequestCookie = NewType('GetAtomNameRequestCookie', ctypes.c_uint32)


GetAtomNameRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('atom', FixedDataPacketField(MARKER_UINT32)),
))


class GetAtomNameRequest:
    OPCODE = 17

    __slots__ = ('atom',)

    def __init__(
            self, *,
            atom: Optional[int] = None,
    ) -> None:
        self.atom = atom

    def as_dict(self) -> Dict[str, Any]:
        return {
            'atom': self.atom,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetAtomNameRequest':
        return GetAtomNameRequest(**GetAtomNameRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetAtomNameRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetAtomNameRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetAtomNameRequest.lib = library.xproto_getatomname
        GetAtomNameRequest.lib.restype = GetAtomNameRequestCookie
        GetAtomNameRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class GetAtomNameRequestCType(ctypes.Structure):
    """xproto GetAtomName"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("atom", ctypes.c_uint32),
    ]


GetAtomNameReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('name_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(22)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['name_len'], 0)),
))


class GetAtomNameReplyReply:
    __slots__ = ('name_len', 'name',)

    def __init__(
            self, *,
            name_len: Optional[int] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.name_len = name_len
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'name_len': self.name_len,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetAtomNameReplyReply':
        return GetAtomNameReplyReply(**GetAtomNameReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetAtomNameReplyReplyPacket.pack(**self.as_dict())


class GetAtomNameReplyReplyCType(ctypes.Structure):
    """xproto GetAtomName_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("name_len", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 22),
        ("var_data", ctypes.c_void_p),
    ]


ChangePropertyRequestPacket = DataPacket((
    ('mode', FixedDataPacketField(MARKER_UINT8)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('format', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
    ('data_len', FixedDataPacketField(MARKER_UINT32)),
    ('data', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: ((d['data_len']) * (d['format'])) / (8), 0)),
))


class ChangePropertyRequest:
    OPCODE = 18

    __slots__ = ('mode', 'window', 'property', 'type', 'format', 'data_len', 'data',)

    def __init__(
            self, *,
            mode: Optional[int] = None,
            window: Optional[int] = None,
            property: Optional[int] = None,
            type: Optional[int] = None,
            format: Optional[int] = None,
            data_len: Optional[int] = None,
            data: Optional[Sequence[None]] = None,
    ) -> None:
        self.mode = mode
        self.window = window
        self.property = property
        self.type = type
        self.format = format
        self.data_len = data_len
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'mode': self.mode,
            'window': self.window,
            'property': self.property,
            'type': self.type,
            'format': self.format,
            'data_len': self.data_len,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangePropertyRequest':
        return ChangePropertyRequest(**ChangePropertyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangePropertyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, Sequence[None]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangePropertyRequest.lib = library.xproto_changeproperty
        ChangePropertyRequest.lib.restype = ctypes.c_uint32
        ChangePropertyRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8 * 3, ctypes.c_uint32, ctypes.c_void_p)


class ChangePropertyRequestCType(ctypes.Structure):
    """xproto ChangeProperty"""
    _fields_ = [
        ("mode", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
        ("property", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("format", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
        ("data_len", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


DeletePropertyRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
))


class DeletePropertyRequest:
    OPCODE = 19

    __slots__ = ('window', 'property',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            property: Optional[int] = None,
    ) -> None:
        self.window = window
        self.property = property

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'property': self.property,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'DeletePropertyRequest':
        return DeletePropertyRequest(**DeletePropertyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return DeletePropertyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        DeletePropertyRequest.lib = library.xproto_deleteproperty
        DeletePropertyRequest.lib.restype = ctypes.c_uint32
        DeletePropertyRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32)


class DeletePropertyRequestCType(ctypes.Structure):
    """xproto DeleteProperty"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
        ("property", ctypes.c_uint32),
    ]


GetPropertyRequestCookie = NewType('GetPropertyRequestCookie', ctypes.c_uint32)


GetPropertyRequestPacket = DataPacket((
    ('delete', FixedDataPacketField(MARKER_UINT8)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('long_offset', FixedDataPacketField(MARKER_UINT32)),
    ('long_length', FixedDataPacketField(MARKER_UINT32)),
))


class GetPropertyRequest:
    OPCODE = 20

    __slots__ = ('delete', 'window', 'property', 'type', 'long_offset', 'long_length',)

    def __init__(
            self, *,
            delete: Optional[bool] = None,
            window: Optional[int] = None,
            property: Optional[int] = None,
            type: Optional[int] = None,
            long_offset: Optional[int] = None,
            long_length: Optional[int] = None,
    ) -> None:
        self.delete = delete
        self.window = window
        self.property = property
        self.type = type
        self.long_offset = long_offset
        self.long_length = long_length

    def as_dict(self) -> Dict[str, Any]:
        return {
            'delete': self.delete,
            'window': self.window,
            'property': self.property,
            'type': self.type,
            'long_offset': self.long_offset,
            'long_length': self.long_length,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPropertyRequest':
        return GetPropertyRequest(**GetPropertyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPropertyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[bool, int, int, int, int, int], GetPropertyRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetPropertyRequest.lib = library.xproto_getproperty
        GetPropertyRequest.lib.restype = GetPropertyRequestCookie
        GetPropertyRequest.lib.argstype = (ctypes.c_int8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetPropertyRequestCType(ctypes.Structure):
    """xproto GetProperty"""
    _fields_ = [
        ("delete", ctypes.c_int8),
        ("window", ctypes.c_uint32),
        ("property", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("long_offset", ctypes.c_uint32),
        ("long_length", ctypes.c_uint32),
    ]


GetPropertyReplyReplyPacket = DataPacket((
    ('format', FixedDataPacketField(MARKER_UINT8)),
    ('type', FixedDataPacketField(MARKER_UINT32)),
    ('bytes_after', FixedDataPacketField(MARKER_UINT32)),
    ('value_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(12)),
    ('value', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: (d['value_len']) * ((d['format']) / (8)), 0)),
))


class GetPropertyReplyReply:
    __slots__ = ('format', 'type', 'bytes_after', 'value_len', 'value',)

    def __init__(
            self, *,
            format: Optional[int] = None,
            type: Optional[int] = None,
            bytes_after: Optional[int] = None,
            value_len: Optional[int] = None,
            value: Optional[Sequence[None]] = None,
    ) -> None:
        self.format = format
        self.type = type
        self.bytes_after = bytes_after
        self.value_len = value_len
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {
            'format': self.format,
            'type': self.type,
            'bytes_after': self.bytes_after,
            'value_len': self.value_len,
            'value': self.value,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPropertyReplyReply':
        return GetPropertyReplyReply(**GetPropertyReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPropertyReplyReplyPacket.pack(**self.as_dict())


class GetPropertyReplyReplyCType(ctypes.Structure):
    """xproto GetProperty_reply"""
    _fields_ = [
        ("format", ctypes.c_uint8),
        ("type", ctypes.c_uint32),
        ("bytes_after", ctypes.c_uint32),
        ("value_len", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 12),
        ("var_data", ctypes.c_void_p),
    ]


ListPropertiesRequestCookie = NewType('ListPropertiesRequestCookie', ctypes.c_uint32)


ListPropertiesRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class ListPropertiesRequest:
    OPCODE = 21

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
    def from_data(inp: BinaryIO) -> 'ListPropertiesRequest':
        return ListPropertiesRequest(**ListPropertiesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListPropertiesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ListPropertiesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ListPropertiesRequest.lib = library.xproto_listproperties
        ListPropertiesRequest.lib.restype = ListPropertiesRequestCookie
        ListPropertiesRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class ListPropertiesRequestCType(ctypes.Structure):
    """xproto ListProperties"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
    ]


ListPropertiesReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('atoms_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(22)),
    ('atoms', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['atoms_len'], 0)),
))


class ListPropertiesReplyReply:
    __slots__ = ('atoms_len', 'atoms',)

    def __init__(
            self, *,
            atoms_len: Optional[int] = None,
            atoms: Optional[Sequence[int]] = None,
    ) -> None:
        self.atoms_len = atoms_len
        self.atoms = atoms

    def as_dict(self) -> Dict[str, Any]:
        return {
            'atoms_len': self.atoms_len,
            'atoms': self.atoms,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListPropertiesReplyReply':
        return ListPropertiesReplyReply(**ListPropertiesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListPropertiesReplyReplyPacket.pack(**self.as_dict())


class ListPropertiesReplyReplyCType(ctypes.Structure):
    """xproto ListProperties_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("atoms_len", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 22),
        ("var_data", ctypes.c_void_p),
    ]


SetSelectionOwnerRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('owner', FixedDataPacketField(MARKER_UINT32)),
    ('selection', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
))


class SetSelectionOwnerRequest:
    OPCODE = 22

    __slots__ = ('owner', 'selection', 'time',)

    def __init__(
            self, *,
            owner: Optional[int] = None,
            selection: Optional[int] = None,
            time: Optional[int] = None,
    ) -> None:
        self.owner = owner
        self.selection = selection
        self.time = time

    def as_dict(self) -> Dict[str, Any]:
        return {
            'owner': self.owner,
            'selection': self.selection,
            'time': self.time,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetSelectionOwnerRequest':
        return SetSelectionOwnerRequest(**SetSelectionOwnerRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetSelectionOwnerRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetSelectionOwnerRequest.lib = library.xproto_setselectionowner
        SetSelectionOwnerRequest.lib.restype = ctypes.c_uint32
        SetSelectionOwnerRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class SetSelectionOwnerRequestCType(ctypes.Structure):
    """xproto SetSelectionOwner"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("owner", ctypes.c_uint32),
        ("selection", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
    ]


GetSelectionOwnerRequestCookie = NewType('GetSelectionOwnerRequestCookie', ctypes.c_uint32)


GetSelectionOwnerRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('selection', FixedDataPacketField(MARKER_UINT32)),
))


class GetSelectionOwnerRequest:
    OPCODE = 23

    __slots__ = ('selection',)

    def __init__(
            self, *,
            selection: Optional[int] = None,
    ) -> None:
        self.selection = selection

    def as_dict(self) -> Dict[str, Any]:
        return {
            'selection': self.selection,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetSelectionOwnerRequest':
        return GetSelectionOwnerRequest(**GetSelectionOwnerRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetSelectionOwnerRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], GetSelectionOwnerRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetSelectionOwnerRequest.lib = library.xproto_getselectionowner
        GetSelectionOwnerRequest.lib.restype = GetSelectionOwnerRequestCookie
        GetSelectionOwnerRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class GetSelectionOwnerRequestCType(ctypes.Structure):
    """xproto GetSelectionOwner"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("selection", ctypes.c_uint32),
    ]


GetSelectionOwnerReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('owner', FixedDataPacketField(MARKER_UINT32)),
))


class GetSelectionOwnerReplyReply:
    __slots__ = ('owner',)

    def __init__(
            self, *,
            owner: Optional[int] = None,
    ) -> None:
        self.owner = owner

    def as_dict(self) -> Dict[str, Any]:
        return {
            'owner': self.owner,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetSelectionOwnerReplyReply':
        return GetSelectionOwnerReplyReply(**GetSelectionOwnerReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetSelectionOwnerReplyReplyPacket.pack(**self.as_dict())


class GetSelectionOwnerReplyReplyCType(ctypes.Structure):
    """xproto GetSelectionOwner_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("owner", ctypes.c_uint32),
    ]


ConvertSelectionRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('requestor', FixedDataPacketField(MARKER_UINT32)),
    ('selection', FixedDataPacketField(MARKER_UINT32)),
    ('target', FixedDataPacketField(MARKER_UINT32)),
    ('property', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
))


class ConvertSelectionRequest:
    OPCODE = 24

    __slots__ = ('requestor', 'selection', 'target', 'property', 'time',)

    def __init__(
            self, *,
            requestor: Optional[int] = None,
            selection: Optional[int] = None,
            target: Optional[int] = None,
            property: Optional[int] = None,
            time: Optional[int] = None,
    ) -> None:
        self.requestor = requestor
        self.selection = selection
        self.target = target
        self.property = property
        self.time = time

    def as_dict(self) -> Dict[str, Any]:
        return {
            'requestor': self.requestor,
            'selection': self.selection,
            'target': self.target,
            'property': self.property,
            'time': self.time,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ConvertSelectionRequest':
        return ConvertSelectionRequest(**ConvertSelectionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ConvertSelectionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ConvertSelectionRequest.lib = library.xproto_convertselection
        ConvertSelectionRequest.lib.restype = ctypes.c_uint32
        ConvertSelectionRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class ConvertSelectionRequestCType(ctypes.Structure):
    """xproto ConvertSelection"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("requestor", ctypes.c_uint32),
        ("selection", ctypes.c_uint32),
        ("target", ctypes.c_uint32),
        ("property", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
    ]


SendEventRequestPacket = DataPacket((
    ('propagate', FixedDataPacketField(MARKER_UINT8)),
    ('destination', FixedDataPacketField(MARKER_UINT32)),
    ('event_mask', FixedDataPacketField(MARKER_UINT32)),
    ('event', SimpleListDataPacketField(MARKER_INT8, lambda d, c: 32, 0)),
))


class SendEventRequest:
    OPCODE = 25

    __slots__ = ('propagate', 'destination', 'event_mask', 'event',)

    def __init__(
            self, *,
            propagate: Optional[bool] = None,
            destination: Optional[int] = None,
            event_mask: Optional[int] = None,
            event: Optional[Sequence[int]] = None,
    ) -> None:
        self.propagate = propagate
        self.destination = destination
        self.event_mask = event_mask
        self.event = event

    def as_dict(self) -> Dict[str, Any]:
        return {
            'propagate': self.propagate,
            'destination': self.destination,
            'event_mask': self.event_mask,
            'event': self.event,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SendEventRequest':
        return SendEventRequest(**SendEventRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SendEventRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[bool, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SendEventRequest.lib = library.xproto_sendevent
        SendEventRequest.lib.restype = ctypes.c_uint32
        SendEventRequest.lib.argstype = (ctypes.c_int8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class SendEventRequestCType(ctypes.Structure):
    """xproto SendEvent"""
    _fields_ = [
        ("propagate", ctypes.c_int8),
        ("destination", ctypes.c_uint32),
        ("event_mask", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


GrabPointerRequestCookie = NewType('GrabPointerRequestCookie', ctypes.c_uint32)


GrabPointerRequestPacket = DataPacket((
    ('owner_events', FixedDataPacketField(MARKER_UINT8)),
    ('grab_window', FixedDataPacketField(MARKER_UINT32)),
    ('event_mask', FixedDataPacketField(MARKER_UINT16)),
    ('pointer_mode', FixedDataPacketField(MARKER_INT8)),
    ('keyboard_mode', FixedDataPacketField(MARKER_INT8)),
    ('confine_to', FixedDataPacketField(MARKER_UINT32)),
    ('cursor', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
))


class GrabPointerRequest:
    OPCODE = 26

    __slots__ = ('owner_events', 'grab_window', 'event_mask', 'pointer_mode', 'keyboard_mode', 'confine_to', 'cursor', 'time',)

    def __init__(
            self, *,
            owner_events: Optional[bool] = None,
            grab_window: Optional[int] = None,
            event_mask: Optional[int] = None,
            pointer_mode: Optional[int] = None,
            keyboard_mode: Optional[int] = None,
            confine_to: Optional[int] = None,
            cursor: Optional[int] = None,
            time: Optional[int] = None,
    ) -> None:
        self.owner_events = owner_events
        self.grab_window = grab_window
        self.event_mask = event_mask
        self.pointer_mode = pointer_mode
        self.keyboard_mode = keyboard_mode
        self.confine_to = confine_to
        self.cursor = cursor
        self.time = time

    def as_dict(self) -> Dict[str, Any]:
        return {
            'owner_events': self.owner_events,
            'grab_window': self.grab_window,
            'event_mask': self.event_mask,
            'pointer_mode': self.pointer_mode,
            'keyboard_mode': self.keyboard_mode,
            'confine_to': self.confine_to,
            'cursor': self.cursor,
            'time': self.time,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GrabPointerRequest':
        return GrabPointerRequest(**GrabPointerRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GrabPointerRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[bool, int, int, int, int, int, int, int], GrabPointerRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GrabPointerRequest.lib = library.xproto_grabpointer
        GrabPointerRequest.lib.restype = GrabPointerRequestCookie
        GrabPointerRequest.lib.argstype = (ctypes.c_int8, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_int8, ctypes.c_int8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GrabPointerRequestCType(ctypes.Structure):
    """xproto GrabPointer"""
    _fields_ = [
        ("owner_events", ctypes.c_int8),
        ("grab_window", ctypes.c_uint32),
        ("event_mask", ctypes.c_uint16),
        ("pointer_mode", ctypes.c_int8),
        ("keyboard_mode", ctypes.c_int8),
        ("confine_to", ctypes.c_uint32),
        ("cursor", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
    ]


GrabPointerReplyReplyPacket = DataPacket((
    ('status', FixedDataPacketField(MARKER_INT8)),
))


class GrabPointerReplyReply:
    __slots__ = ('status',)

    def __init__(
            self, *,
            status: Optional[int] = None,
    ) -> None:
        self.status = status

    def as_dict(self) -> Dict[str, Any]:
        return {
            'status': self.status,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GrabPointerReplyReply':
        return GrabPointerReplyReply(**GrabPointerReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GrabPointerReplyReplyPacket.pack(**self.as_dict())


class GrabPointerReplyReplyCType(ctypes.Structure):
    """xproto GrabPointer_reply"""
    _fields_ = [
        ("status", ctypes.c_int8),
    ]


UngrabPointerRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
))


class UngrabPointerRequest:
    OPCODE = 27

    __slots__ = ('time',)

    def __init__(
            self, *,
            time: Optional[int] = None,
    ) -> None:
        self.time = time

    def as_dict(self) -> Dict[str, Any]:
        return {
            'time': self.time,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'UngrabPointerRequest':
        return UngrabPointerRequest(**UngrabPointerRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return UngrabPointerRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        UngrabPointerRequest.lib = library.xproto_ungrabpointer
        UngrabPointerRequest.lib.restype = ctypes.c_uint32
        UngrabPointerRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class UngrabPointerRequestCType(ctypes.Structure):
    """xproto UngrabPointer"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("time", ctypes.c_uint32),
    ]


GrabButtonRequestPacket = DataPacket((
    ('owner_events', FixedDataPacketField(MARKER_UINT8)),
    ('grab_window', FixedDataPacketField(MARKER_UINT32)),
    ('event_mask', FixedDataPacketField(MARKER_UINT16)),
    ('pointer_mode', FixedDataPacketField(MARKER_UINT8)),
    ('keyboard_mode', FixedDataPacketField(MARKER_UINT8)),
    ('confine_to', FixedDataPacketField(MARKER_UINT32)),
    ('cursor', FixedDataPacketField(MARKER_UINT32)),
    ('button', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('modifiers', FixedDataPacketField(MARKER_UINT16)),
))


class GrabButtonRequest:
    OPCODE = 28

    __slots__ = ('owner_events', 'grab_window', 'event_mask', 'pointer_mode', 'keyboard_mode', 'confine_to', 'cursor', 'button', 'modifiers',)

    def __init__(
            self, *,
            owner_events: Optional[bool] = None,
            grab_window: Optional[int] = None,
            event_mask: Optional[int] = None,
            pointer_mode: Optional[int] = None,
            keyboard_mode: Optional[int] = None,
            confine_to: Optional[int] = None,
            cursor: Optional[int] = None,
            button: Optional[int] = None,
            modifiers: Optional[int] = None,
    ) -> None:
        self.owner_events = owner_events
        self.grab_window = grab_window
        self.event_mask = event_mask
        self.pointer_mode = pointer_mode
        self.keyboard_mode = keyboard_mode
        self.confine_to = confine_to
        self.cursor = cursor
        self.button = button
        self.modifiers = modifiers

    def as_dict(self) -> Dict[str, Any]:
        return {
            'owner_events': self.owner_events,
            'grab_window': self.grab_window,
            'event_mask': self.event_mask,
            'pointer_mode': self.pointer_mode,
            'keyboard_mode': self.keyboard_mode,
            'confine_to': self.confine_to,
            'cursor': self.cursor,
            'button': self.button,
            'modifiers': self.modifiers,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GrabButtonRequest':
        return GrabButtonRequest(**GrabButtonRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GrabButtonRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[bool, int, int, int, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GrabButtonRequest.lib = library.xproto_grabbutton
        GrabButtonRequest.lib.restype = ctypes.c_uint32
        GrabButtonRequest.lib.argstype = (ctypes.c_int8, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint16)


class GrabButtonRequestCType(ctypes.Structure):
    """xproto GrabButton"""
    _fields_ = [
        ("owner_events", ctypes.c_int8),
        ("grab_window", ctypes.c_uint32),
        ("event_mask", ctypes.c_uint16),
        ("pointer_mode", ctypes.c_uint8),
        ("keyboard_mode", ctypes.c_uint8),
        ("confine_to", ctypes.c_uint32),
        ("cursor", ctypes.c_uint32),
        ("button", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("modifiers", ctypes.c_uint16),
    ]


UngrabButtonRequestPacket = DataPacket((
    ('button', FixedDataPacketField(MARKER_UINT8)),
    ('grab_window', FixedDataPacketField(MARKER_UINT32)),
    ('modifiers', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
))


class UngrabButtonRequest:
    OPCODE = 29

    __slots__ = ('button', 'grab_window', 'modifiers',)

    def __init__(
            self, *,
            button: Optional[int] = None,
            grab_window: Optional[int] = None,
            modifiers: Optional[int] = None,
    ) -> None:
        self.button = button
        self.grab_window = grab_window
        self.modifiers = modifiers

    def as_dict(self) -> Dict[str, Any]:
        return {
            'button': self.button,
            'grab_window': self.grab_window,
            'modifiers': self.modifiers,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'UngrabButtonRequest':
        return UngrabButtonRequest(**UngrabButtonRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return UngrabButtonRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        UngrabButtonRequest.lib = library.xproto_ungrabbutton
        UngrabButtonRequest.lib.restype = ctypes.c_uint32
        UngrabButtonRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8 * 2)


class UngrabButtonRequestCType(ctypes.Structure):
    """xproto UngrabButton"""
    _fields_ = [
        ("button", ctypes.c_uint8),
        ("grab_window", ctypes.c_uint32),
        ("modifiers", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
    ]


ChangeActivePointerGrabRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('cursor', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('event_mask', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(2)),
))


class ChangeActivePointerGrabRequest:
    OPCODE = 30

    __slots__ = ('cursor', 'time', 'event_mask',)

    def __init__(
            self, *,
            cursor: Optional[int] = None,
            time: Optional[int] = None,
            event_mask: Optional[int] = None,
    ) -> None:
        self.cursor = cursor
        self.time = time
        self.event_mask = event_mask

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cursor': self.cursor,
            'time': self.time,
            'event_mask': self.event_mask,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeActivePointerGrabRequest':
        return ChangeActivePointerGrabRequest(**ChangeActivePointerGrabRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeActivePointerGrabRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangeActivePointerGrabRequest.lib = library.xproto_changeactivepointergrab
        ChangeActivePointerGrabRequest.lib.restype = ctypes.c_uint32
        ChangeActivePointerGrabRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8 * 2)


class ChangeActivePointerGrabRequestCType(ctypes.Structure):
    """xproto ChangeActivePointerGrab"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("cursor", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("event_mask", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 2),
    ]


GrabKeyboardRequestCookie = NewType('GrabKeyboardRequestCookie', ctypes.c_uint32)


GrabKeyboardRequestPacket = DataPacket((
    ('owner_events', FixedDataPacketField(MARKER_UINT8)),
    ('grab_window', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('pointer_mode', FixedDataPacketField(MARKER_INT8)),
    ('keyboard_mode', FixedDataPacketField(MARKER_INT8)),
    ('pad0', FixedPadDataPacketField(2)),
))


class GrabKeyboardRequest:
    OPCODE = 31

    __slots__ = ('owner_events', 'grab_window', 'time', 'pointer_mode', 'keyboard_mode',)

    def __init__(
            self, *,
            owner_events: Optional[bool] = None,
            grab_window: Optional[int] = None,
            time: Optional[int] = None,
            pointer_mode: Optional[int] = None,
            keyboard_mode: Optional[int] = None,
    ) -> None:
        self.owner_events = owner_events
        self.grab_window = grab_window
        self.time = time
        self.pointer_mode = pointer_mode
        self.keyboard_mode = keyboard_mode

    def as_dict(self) -> Dict[str, Any]:
        return {
            'owner_events': self.owner_events,
            'grab_window': self.grab_window,
            'time': self.time,
            'pointer_mode': self.pointer_mode,
            'keyboard_mode': self.keyboard_mode,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GrabKeyboardRequest':
        return GrabKeyboardRequest(**GrabKeyboardRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GrabKeyboardRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[bool, int, int, int, int], GrabKeyboardRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GrabKeyboardRequest.lib = library.xproto_grabkeyboard
        GrabKeyboardRequest.lib.restype = GrabKeyboardRequestCookie
        GrabKeyboardRequest.lib.argstype = (ctypes.c_int8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int8, ctypes.c_int8, ctypes.c_uint8 * 2)


class GrabKeyboardRequestCType(ctypes.Structure):
    """xproto GrabKeyboard"""
    _fields_ = [
        ("owner_events", ctypes.c_int8),
        ("grab_window", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
        ("pointer_mode", ctypes.c_int8),
        ("keyboard_mode", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 2),
    ]


GrabKeyboardReplyReplyPacket = DataPacket((
    ('status', FixedDataPacketField(MARKER_INT8)),
))


class GrabKeyboardReplyReply:
    __slots__ = ('status',)

    def __init__(
            self, *,
            status: Optional[int] = None,
    ) -> None:
        self.status = status

    def as_dict(self) -> Dict[str, Any]:
        return {
            'status': self.status,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GrabKeyboardReplyReply':
        return GrabKeyboardReplyReply(**GrabKeyboardReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GrabKeyboardReplyReplyPacket.pack(**self.as_dict())


class GrabKeyboardReplyReplyCType(ctypes.Structure):
    """xproto GrabKeyboard_reply"""
    _fields_ = [
        ("status", ctypes.c_int8),
    ]


UngrabKeyboardRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
))


class UngrabKeyboardRequest:
    OPCODE = 32

    __slots__ = ('time',)

    def __init__(
            self, *,
            time: Optional[int] = None,
    ) -> None:
        self.time = time

    def as_dict(self) -> Dict[str, Any]:
        return {
            'time': self.time,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'UngrabKeyboardRequest':
        return UngrabKeyboardRequest(**UngrabKeyboardRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return UngrabKeyboardRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        UngrabKeyboardRequest.lib = library.xproto_ungrabkeyboard
        UngrabKeyboardRequest.lib.restype = ctypes.c_uint32
        UngrabKeyboardRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class UngrabKeyboardRequestCType(ctypes.Structure):
    """xproto UngrabKeyboard"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("time", ctypes.c_uint32),
    ]


GrabKeyRequestPacket = DataPacket((
    ('owner_events', FixedDataPacketField(MARKER_UINT8)),
    ('grab_window', FixedDataPacketField(MARKER_UINT32)),
    ('modifiers', FixedDataPacketField(MARKER_UINT16)),
    ('key', FixedDataPacketField(MARKER_UINT32)),
    ('pointer_mode', FixedDataPacketField(MARKER_UINT8)),
    ('keyboard_mode', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(3)),
))


class GrabKeyRequest:
    OPCODE = 33

    __slots__ = ('owner_events', 'grab_window', 'modifiers', 'key', 'pointer_mode', 'keyboard_mode',)

    def __init__(
            self, *,
            owner_events: Optional[bool] = None,
            grab_window: Optional[int] = None,
            modifiers: Optional[int] = None,
            key: Optional[int] = None,
            pointer_mode: Optional[int] = None,
            keyboard_mode: Optional[int] = None,
    ) -> None:
        self.owner_events = owner_events
        self.grab_window = grab_window
        self.modifiers = modifiers
        self.key = key
        self.pointer_mode = pointer_mode
        self.keyboard_mode = keyboard_mode

    def as_dict(self) -> Dict[str, Any]:
        return {
            'owner_events': self.owner_events,
            'grab_window': self.grab_window,
            'modifiers': self.modifiers,
            'key': self.key,
            'pointer_mode': self.pointer_mode,
            'keyboard_mode': self.keyboard_mode,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GrabKeyRequest':
        return GrabKeyRequest(**GrabKeyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GrabKeyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[bool, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GrabKeyRequest.lib = library.xproto_grabkey
        GrabKeyRequest.lib.restype = ctypes.c_uint32
        GrabKeyRequest.lib.argstype = (ctypes.c_int8, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8 * 3)


class GrabKeyRequestCType(ctypes.Structure):
    """xproto GrabKey"""
    _fields_ = [
        ("owner_events", ctypes.c_int8),
        ("grab_window", ctypes.c_uint32),
        ("modifiers", ctypes.c_uint16),
        ("key", ctypes.c_uint32),
        ("pointer_mode", ctypes.c_uint8),
        ("keyboard_mode", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 3),
    ]


UngrabKeyRequestPacket = DataPacket((
    ('key', FixedDataPacketField(MARKER_UINT32)),
    ('grab_window', FixedDataPacketField(MARKER_UINT32)),
    ('modifiers', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
))


class UngrabKeyRequest:
    OPCODE = 34

    __slots__ = ('key', 'grab_window', 'modifiers',)

    def __init__(
            self, *,
            key: Optional[int] = None,
            grab_window: Optional[int] = None,
            modifiers: Optional[int] = None,
    ) -> None:
        self.key = key
        self.grab_window = grab_window
        self.modifiers = modifiers

    def as_dict(self) -> Dict[str, Any]:
        return {
            'key': self.key,
            'grab_window': self.grab_window,
            'modifiers': self.modifiers,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'UngrabKeyRequest':
        return UngrabKeyRequest(**UngrabKeyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return UngrabKeyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        UngrabKeyRequest.lib = library.xproto_ungrabkey
        UngrabKeyRequest.lib.restype = ctypes.c_uint32
        UngrabKeyRequest.lib.argstype = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8 * 2)


class UngrabKeyRequestCType(ctypes.Structure):
    """xproto UngrabKey"""
    _fields_ = [
        ("key", ctypes.c_uint32),
        ("grab_window", ctypes.c_uint32),
        ("modifiers", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
    ]


AllowEventsRequestPacket = DataPacket((
    ('mode', FixedDataPacketField(MARKER_UINT8)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
))


class AllowEventsRequest:
    OPCODE = 35

    __slots__ = ('mode', 'time',)

    def __init__(
            self, *,
            mode: Optional[int] = None,
            time: Optional[int] = None,
    ) -> None:
        self.mode = mode
        self.time = time

    def as_dict(self) -> Dict[str, Any]:
        return {
            'mode': self.mode,
            'time': self.time,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AllowEventsRequest':
        return AllowEventsRequest(**AllowEventsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AllowEventsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        AllowEventsRequest.lib = library.xproto_allowevents
        AllowEventsRequest.lib.restype = ctypes.c_uint32
        AllowEventsRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class AllowEventsRequestCType(ctypes.Structure):
    """xproto AllowEvents"""
    _fields_ = [
        ("mode", ctypes.c_uint8),
        ("time", ctypes.c_uint32),
    ]


GrabServerRequestPacket = DataPacket((
))


class GrabServerRequest:
    OPCODE = 36

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GrabServerRequest':
        return GrabServerRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GrabServerRequest.lib = library.xproto_grabserver
        GrabServerRequest.lib.restype = ctypes.c_uint32
        GrabServerRequest.lib.argstype = ()


class GrabServerRequestCType(ctypes.Structure):
    """xproto GrabServer"""
    _fields_ = [
    ]


UngrabServerRequestPacket = DataPacket((
))


class UngrabServerRequest:
    OPCODE = 37

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'UngrabServerRequest':
        return UngrabServerRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        UngrabServerRequest.lib = library.xproto_ungrabserver
        UngrabServerRequest.lib.restype = ctypes.c_uint32
        UngrabServerRequest.lib.argstype = ()


class UngrabServerRequestCType(ctypes.Structure):
    """xproto UngrabServer"""
    _fields_ = [
    ]


QueryPointerRequestCookie = NewType('QueryPointerRequestCookie', ctypes.c_uint32)


QueryPointerRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class QueryPointerRequest:
    OPCODE = 38

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
    def from_data(inp: BinaryIO) -> 'QueryPointerRequest':
        return QueryPointerRequest(**QueryPointerRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryPointerRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], QueryPointerRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryPointerRequest.lib = library.xproto_querypointer
        QueryPointerRequest.lib.restype = QueryPointerRequestCookie
        QueryPointerRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class QueryPointerRequestCType(ctypes.Structure):
    """xproto QueryPointer"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
    ]


QueryPointerReplyReplyPacket = DataPacket((
    ('same_screen', FixedDataPacketField(MARKER_UINT8)),
    ('root', FixedDataPacketField(MARKER_UINT32)),
    ('child', FixedDataPacketField(MARKER_UINT32)),
    ('root_x', FixedDataPacketField(MARKER_INT16)),
    ('root_y', FixedDataPacketField(MARKER_INT16)),
    ('win_x', FixedDataPacketField(MARKER_INT16)),
    ('win_y', FixedDataPacketField(MARKER_INT16)),
    ('mask', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
))


class QueryPointerReplyReply:
    __slots__ = ('same_screen', 'root', 'child', 'root_x', 'root_y', 'win_x', 'win_y', 'mask',)

    def __init__(
            self, *,
            same_screen: Optional[bool] = None,
            root: Optional[int] = None,
            child: Optional[int] = None,
            root_x: Optional[int] = None,
            root_y: Optional[int] = None,
            win_x: Optional[int] = None,
            win_y: Optional[int] = None,
            mask: Optional[int] = None,
    ) -> None:
        self.same_screen = same_screen
        self.root = root
        self.child = child
        self.root_x = root_x
        self.root_y = root_y
        self.win_x = win_x
        self.win_y = win_y
        self.mask = mask

    def as_dict(self) -> Dict[str, Any]:
        return {
            'same_screen': self.same_screen,
            'root': self.root,
            'child': self.child,
            'root_x': self.root_x,
            'root_y': self.root_y,
            'win_x': self.win_x,
            'win_y': self.win_y,
            'mask': self.mask,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryPointerReplyReply':
        return QueryPointerReplyReply(**QueryPointerReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryPointerReplyReplyPacket.pack(**self.as_dict())


class QueryPointerReplyReplyCType(ctypes.Structure):
    """xproto QueryPointer_reply"""
    _fields_ = [
        ("same_screen", ctypes.c_int8),
        ("root", ctypes.c_uint32),
        ("child", ctypes.c_uint32),
        ("root_x", ctypes.c_int16),
        ("root_y", ctypes.c_int16),
        ("win_x", ctypes.c_int16),
        ("win_y", ctypes.c_int16),
        ("mask", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
    ]


TimecoordStructPacket = DataPacket((
    ('time', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
))


class TimecoordStruct:
    __slots__ = ('time', 'x', 'y',)

    def __init__(
            self, *,
            time: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
    ) -> None:
        self.time = time
        self.x = x
        self.y = y

    def as_dict(self) -> Dict[str, Any]:
        return {
            'time': self.time,
            'x': self.x,
            'y': self.y,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'TimecoordStruct':
        return TimecoordStruct(**TimecoordStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return TimecoordStructPacket.pack(**self.as_dict())


class TimecoordStructCType(ctypes.Structure):
    """xproto TIMECOORD"""
    _fields_ = [
        ("time", ctypes.c_uint32),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
    ]


GetMotionEventsRequestCookie = NewType('GetMotionEventsRequestCookie', ctypes.c_uint32)


GetMotionEventsRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('start', FixedDataPacketField(MARKER_UINT32)),
    ('stop', FixedDataPacketField(MARKER_UINT32)),
))


class GetMotionEventsRequest:
    OPCODE = 39

    __slots__ = ('window', 'start', 'stop',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            start: Optional[int] = None,
            stop: Optional[int] = None,
    ) -> None:
        self.window = window
        self.start = start
        self.stop = stop

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'start': self.start,
            'stop': self.stop,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMotionEventsRequest':
        return GetMotionEventsRequest(**GetMotionEventsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMotionEventsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], GetMotionEventsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetMotionEventsRequest.lib = library.xproto_getmotionevents
        GetMotionEventsRequest.lib.restype = GetMotionEventsRequestCookie
        GetMotionEventsRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class GetMotionEventsRequestCType(ctypes.Structure):
    """xproto GetMotionEvents"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
        ("start", ctypes.c_uint32),
        ("stop", ctypes.c_uint32),
    ]


GetMotionEventsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('events_len', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(20)),
    ('events', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['events_len'], 0)),
))


class GetMotionEventsReplyReply:
    __slots__ = ('events_len', 'events',)

    def __init__(
            self, *,
            events_len: Optional[int] = None,
            events: Optional[Sequence[int]] = None,
    ) -> None:
        self.events_len = events_len
        self.events = events

    def as_dict(self) -> Dict[str, Any]:
        return {
            'events_len': self.events_len,
            'events': self.events,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetMotionEventsReplyReply':
        return GetMotionEventsReplyReply(**GetMotionEventsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetMotionEventsReplyReplyPacket.pack(**self.as_dict())


class GetMotionEventsReplyReplyCType(ctypes.Structure):
    """xproto GetMotionEvents_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("events_len", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


TranslateCoordinatesRequestCookie = NewType('TranslateCoordinatesRequestCookie', ctypes.c_uint32)


TranslateCoordinatesRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('src_window', FixedDataPacketField(MARKER_UINT32)),
    ('dst_window', FixedDataPacketField(MARKER_UINT32)),
    ('src_x', FixedDataPacketField(MARKER_INT16)),
    ('src_y', FixedDataPacketField(MARKER_INT16)),
))


class TranslateCoordinatesRequest:
    OPCODE = 40

    __slots__ = ('src_window', 'dst_window', 'src_x', 'src_y',)

    def __init__(
            self, *,
            src_window: Optional[int] = None,
            dst_window: Optional[int] = None,
            src_x: Optional[int] = None,
            src_y: Optional[int] = None,
    ) -> None:
        self.src_window = src_window
        self.dst_window = dst_window
        self.src_x = src_x
        self.src_y = src_y

    def as_dict(self) -> Dict[str, Any]:
        return {
            'src_window': self.src_window,
            'dst_window': self.dst_window,
            'src_x': self.src_x,
            'src_y': self.src_y,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'TranslateCoordinatesRequest':
        return TranslateCoordinatesRequest(**TranslateCoordinatesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return TranslateCoordinatesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], TranslateCoordinatesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        TranslateCoordinatesRequest.lib = library.xproto_translatecoordinates
        TranslateCoordinatesRequest.lib.restype = TranslateCoordinatesRequestCookie
        TranslateCoordinatesRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16)


class TranslateCoordinatesRequestCType(ctypes.Structure):
    """xproto TranslateCoordinates"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("src_window", ctypes.c_uint32),
        ("dst_window", ctypes.c_uint32),
        ("src_x", ctypes.c_int16),
        ("src_y", ctypes.c_int16),
    ]


TranslateCoordinatesReplyReplyPacket = DataPacket((
    ('same_screen', FixedDataPacketField(MARKER_UINT8)),
    ('child', FixedDataPacketField(MARKER_UINT32)),
    ('dst_x', FixedDataPacketField(MARKER_INT16)),
    ('dst_y', FixedDataPacketField(MARKER_INT16)),
))


class TranslateCoordinatesReplyReply:
    __slots__ = ('same_screen', 'child', 'dst_x', 'dst_y',)

    def __init__(
            self, *,
            same_screen: Optional[bool] = None,
            child: Optional[int] = None,
            dst_x: Optional[int] = None,
            dst_y: Optional[int] = None,
    ) -> None:
        self.same_screen = same_screen
        self.child = child
        self.dst_x = dst_x
        self.dst_y = dst_y

    def as_dict(self) -> Dict[str, Any]:
        return {
            'same_screen': self.same_screen,
            'child': self.child,
            'dst_x': self.dst_x,
            'dst_y': self.dst_y,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'TranslateCoordinatesReplyReply':
        return TranslateCoordinatesReplyReply(**TranslateCoordinatesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return TranslateCoordinatesReplyReplyPacket.pack(**self.as_dict())


class TranslateCoordinatesReplyReplyCType(ctypes.Structure):
    """xproto TranslateCoordinates_reply"""
    _fields_ = [
        ("same_screen", ctypes.c_int8),
        ("child", ctypes.c_uint32),
        ("dst_x", ctypes.c_int16),
        ("dst_y", ctypes.c_int16),
    ]


WarpPointerRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('src_window', FixedDataPacketField(MARKER_UINT32)),
    ('dst_window', FixedDataPacketField(MARKER_UINT32)),
    ('src_x', FixedDataPacketField(MARKER_INT16)),
    ('src_y', FixedDataPacketField(MARKER_INT16)),
    ('src_width', FixedDataPacketField(MARKER_UINT16)),
    ('src_height', FixedDataPacketField(MARKER_UINT16)),
    ('dst_x', FixedDataPacketField(MARKER_INT16)),
    ('dst_y', FixedDataPacketField(MARKER_INT16)),
))


class WarpPointerRequest:
    OPCODE = 41

    __slots__ = ('src_window', 'dst_window', 'src_x', 'src_y', 'src_width', 'src_height', 'dst_x', 'dst_y',)

    def __init__(
            self, *,
            src_window: Optional[int] = None,
            dst_window: Optional[int] = None,
            src_x: Optional[int] = None,
            src_y: Optional[int] = None,
            src_width: Optional[int] = None,
            src_height: Optional[int] = None,
            dst_x: Optional[int] = None,
            dst_y: Optional[int] = None,
    ) -> None:
        self.src_window = src_window
        self.dst_window = dst_window
        self.src_x = src_x
        self.src_y = src_y
        self.src_width = src_width
        self.src_height = src_height
        self.dst_x = dst_x
        self.dst_y = dst_y

    def as_dict(self) -> Dict[str, Any]:
        return {
            'src_window': self.src_window,
            'dst_window': self.dst_window,
            'src_x': self.src_x,
            'src_y': self.src_y,
            'src_width': self.src_width,
            'src_height': self.src_height,
            'dst_x': self.dst_x,
            'dst_y': self.dst_y,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'WarpPointerRequest':
        return WarpPointerRequest(**WarpPointerRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return WarpPointerRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        WarpPointerRequest.lib = library.xproto_warppointer
        WarpPointerRequest.lib.restype = ctypes.c_uint32
        WarpPointerRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_int16, ctypes.c_int16)


class WarpPointerRequestCType(ctypes.Structure):
    """xproto WarpPointer"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("src_window", ctypes.c_uint32),
        ("dst_window", ctypes.c_uint32),
        ("src_x", ctypes.c_int16),
        ("src_y", ctypes.c_int16),
        ("src_width", ctypes.c_uint16),
        ("src_height", ctypes.c_uint16),
        ("dst_x", ctypes.c_int16),
        ("dst_y", ctypes.c_int16),
    ]


SetInputFocusRequestPacket = DataPacket((
    ('revert_to', FixedDataPacketField(MARKER_UINT8)),
    ('focus', FixedDataPacketField(MARKER_UINT32)),
    ('time', FixedDataPacketField(MARKER_UINT32)),
))


class SetInputFocusRequest:
    OPCODE = 42

    __slots__ = ('revert_to', 'focus', 'time',)

    def __init__(
            self, *,
            revert_to: Optional[int] = None,
            focus: Optional[int] = None,
            time: Optional[int] = None,
    ) -> None:
        self.revert_to = revert_to
        self.focus = focus
        self.time = time

    def as_dict(self) -> Dict[str, Any]:
        return {
            'revert_to': self.revert_to,
            'focus': self.focus,
            'time': self.time,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetInputFocusRequest':
        return SetInputFocusRequest(**SetInputFocusRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetInputFocusRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetInputFocusRequest.lib = library.xproto_setinputfocus
        SetInputFocusRequest.lib.restype = ctypes.c_uint32
        SetInputFocusRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32)


class SetInputFocusRequestCType(ctypes.Structure):
    """xproto SetInputFocus"""
    _fields_ = [
        ("revert_to", ctypes.c_uint8),
        ("focus", ctypes.c_uint32),
        ("time", ctypes.c_uint32),
    ]


GetInputFocusRequestCookie = NewType('GetInputFocusRequestCookie', ctypes.c_uint32)


GetInputFocusRequestPacket = DataPacket((
))


class GetInputFocusRequest:
    OPCODE = 43

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetInputFocusRequest':
        return GetInputFocusRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], GetInputFocusRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetInputFocusRequest.lib = library.xproto_getinputfocus
        GetInputFocusRequest.lib.restype = GetInputFocusRequestCookie
        GetInputFocusRequest.lib.argstype = ()


class GetInputFocusRequestCType(ctypes.Structure):
    """xproto GetInputFocus"""
    _fields_ = [
    ]


GetInputFocusReplyReplyPacket = DataPacket((
    ('revert_to', FixedDataPacketField(MARKER_UINT8)),
    ('focus', FixedDataPacketField(MARKER_UINT32)),
))


class GetInputFocusReplyReply:
    __slots__ = ('revert_to', 'focus',)

    def __init__(
            self, *,
            revert_to: Optional[int] = None,
            focus: Optional[int] = None,
    ) -> None:
        self.revert_to = revert_to
        self.focus = focus

    def as_dict(self) -> Dict[str, Any]:
        return {
            'revert_to': self.revert_to,
            'focus': self.focus,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetInputFocusReplyReply':
        return GetInputFocusReplyReply(**GetInputFocusReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetInputFocusReplyReplyPacket.pack(**self.as_dict())


class GetInputFocusReplyReplyCType(ctypes.Structure):
    """xproto GetInputFocus_reply"""
    _fields_ = [
        ("revert_to", ctypes.c_uint8),
        ("focus", ctypes.c_uint32),
    ]


QueryKeymapRequestCookie = NewType('QueryKeymapRequestCookie', ctypes.c_uint32)


QueryKeymapRequestPacket = DataPacket((
))


class QueryKeymapRequest:
    OPCODE = 44

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryKeymapRequest':
        return QueryKeymapRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], QueryKeymapRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryKeymapRequest.lib = library.xproto_querykeymap
        QueryKeymapRequest.lib.restype = QueryKeymapRequestCookie
        QueryKeymapRequest.lib.argstype = ()


class QueryKeymapRequestCType(ctypes.Structure):
    """xproto QueryKeymap"""
    _fields_ = [
    ]


QueryKeymapReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('keys', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 32, 0)),
))


class QueryKeymapReplyReply:
    __slots__ = ('keys',)

    def __init__(
            self, *,
            keys: Optional[Sequence[int]] = None,
    ) -> None:
        self.keys = keys

    def as_dict(self) -> Dict[str, Any]:
        return {
            'keys': self.keys,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryKeymapReplyReply':
        return QueryKeymapReplyReply(**QueryKeymapReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryKeymapReplyReplyPacket.pack(**self.as_dict())


class QueryKeymapReplyReplyCType(ctypes.Structure):
    """xproto QueryKeymap_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


OpenFontRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('fid', FixedDataPacketField(MARKER_UINT32)),
    ('name_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(2)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['name_len'], 0)),
))


class OpenFontRequest:
    OPCODE = 45

    __slots__ = ('fid', 'name_len', 'name',)

    def __init__(
            self, *,
            fid: Optional[int] = None,
            name_len: Optional[int] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.fid = fid
        self.name_len = name_len
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'fid': self.fid,
            'name_len': self.name_len,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'OpenFontRequest':
        return OpenFontRequest(**OpenFontRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return OpenFontRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        OpenFontRequest.lib = library.xproto_openfont
        OpenFontRequest.lib.restype = ctypes.c_uint32
        OpenFontRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_void_p)


class OpenFontRequestCType(ctypes.Structure):
    """xproto OpenFont"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("fid", ctypes.c_uint32),
        ("name_len", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


CloseFontRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('font', FixedDataPacketField(MARKER_UINT32)),
))


class CloseFontRequest:
    OPCODE = 46

    __slots__ = ('font',)

    def __init__(
            self, *,
            font: Optional[int] = None,
    ) -> None:
        self.font = font

    def as_dict(self) -> Dict[str, Any]:
        return {
            'font': self.font,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CloseFontRequest':
        return CloseFontRequest(**CloseFontRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CloseFontRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CloseFontRequest.lib = library.xproto_closefont
        CloseFontRequest.lib.restype = ctypes.c_uint32
        CloseFontRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class CloseFontRequestCType(ctypes.Structure):
    """xproto CloseFont"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("font", ctypes.c_uint32),
    ]


FontpropStructPacket = DataPacket((
    ('name', FixedDataPacketField(MARKER_UINT32)),
    ('value', FixedDataPacketField(MARKER_UINT32)),
))


class FontpropStruct:
    __slots__ = ('name', 'value',)

    def __init__(
            self, *,
            name: Optional[int] = None,
            value: Optional[int] = None,
    ) -> None:
        self.name = name
        self.value = value

    def as_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'value': self.value,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FontpropStruct':
        return FontpropStruct(**FontpropStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FontpropStructPacket.pack(**self.as_dict())


class FontpropStructCType(ctypes.Structure):
    """xproto FONTPROP"""
    _fields_ = [
        ("name", ctypes.c_uint32),
        ("value", ctypes.c_uint32),
    ]


CharinfoStructPacket = DataPacket((
    ('left_side_bearing', FixedDataPacketField(MARKER_INT16)),
    ('right_side_bearing', FixedDataPacketField(MARKER_INT16)),
    ('character_width', FixedDataPacketField(MARKER_INT16)),
    ('ascent', FixedDataPacketField(MARKER_INT16)),
    ('descent', FixedDataPacketField(MARKER_INT16)),
    ('attributes', FixedDataPacketField(MARKER_UINT16)),
))


class CharinfoStruct:
    __slots__ = ('left_side_bearing', 'right_side_bearing', 'character_width', 'ascent', 'descent', 'attributes',)

    def __init__(
            self, *,
            left_side_bearing: Optional[int] = None,
            right_side_bearing: Optional[int] = None,
            character_width: Optional[int] = None,
            ascent: Optional[int] = None,
            descent: Optional[int] = None,
            attributes: Optional[int] = None,
    ) -> None:
        self.left_side_bearing = left_side_bearing
        self.right_side_bearing = right_side_bearing
        self.character_width = character_width
        self.ascent = ascent
        self.descent = descent
        self.attributes = attributes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'left_side_bearing': self.left_side_bearing,
            'right_side_bearing': self.right_side_bearing,
            'character_width': self.character_width,
            'ascent': self.ascent,
            'descent': self.descent,
            'attributes': self.attributes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CharinfoStruct':
        return CharinfoStruct(**CharinfoStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CharinfoStructPacket.pack(**self.as_dict())


class CharinfoStructCType(ctypes.Structure):
    """xproto CHARINFO"""
    _fields_ = [
        ("left_side_bearing", ctypes.c_int16),
        ("right_side_bearing", ctypes.c_int16),
        ("character_width", ctypes.c_int16),
        ("ascent", ctypes.c_int16),
        ("descent", ctypes.c_int16),
        ("attributes", ctypes.c_uint16),
    ]


QueryFontRequestCookie = NewType('QueryFontRequestCookie', ctypes.c_uint32)


QueryFontRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('font', FixedDataPacketField(MARKER_UINT32)),
))


class QueryFontRequest:
    OPCODE = 47

    __slots__ = ('font',)

    def __init__(
            self, *,
            font: Optional[int] = None,
    ) -> None:
        self.font = font

    def as_dict(self) -> Dict[str, Any]:
        return {
            'font': self.font,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryFontRequest':
        return QueryFontRequest(**QueryFontRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryFontRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], QueryFontRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryFontRequest.lib = library.xproto_queryfont
        QueryFontRequest.lib.restype = QueryFontRequestCookie
        QueryFontRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class QueryFontRequestCType(ctypes.Structure):
    """xproto QueryFont"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("font", ctypes.c_uint32),
    ]


QueryFontReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('min_bounds', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(4)),
    ('max_bounds', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(4)),
    ('min_char_or_byte2', FixedDataPacketField(MARKER_UINT16)),
    ('max_char_or_byte2', FixedDataPacketField(MARKER_UINT16)),
    ('default_char', FixedDataPacketField(MARKER_UINT16)),
    ('properties_len', FixedDataPacketField(MARKER_UINT16)),
    ('draw_direction', FixedDataPacketField(MARKER_INT8)),
    ('min_byte1', FixedDataPacketField(MARKER_UINT8)),
    ('max_byte1', FixedDataPacketField(MARKER_UINT8)),
    ('all_chars_exist', FixedDataPacketField(MARKER_UINT8)),
    ('font_ascent', FixedDataPacketField(MARKER_INT16)),
    ('font_descent', FixedDataPacketField(MARKER_INT16)),
    ('char_infos_len', FixedDataPacketField(MARKER_UINT32)),
    ('properties', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['properties_len'], 0)),
    ('char_infos', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['char_infos_len'], 0)),
))


class QueryFontReplyReply:
    __slots__ = ('min_bounds', 'max_bounds', 'min_char_or_byte2', 'max_char_or_byte2', 'default_char', 'properties_len', 'draw_direction', 'min_byte1', 'max_byte1', 'all_chars_exist', 'font_ascent', 'font_descent', 'char_infos_len', 'properties', 'char_infos',)

    def __init__(
            self, *,
            min_bounds: Optional[int] = None,
            max_bounds: Optional[int] = None,
            min_char_or_byte2: Optional[int] = None,
            max_char_or_byte2: Optional[int] = None,
            default_char: Optional[int] = None,
            properties_len: Optional[int] = None,
            draw_direction: Optional[int] = None,
            min_byte1: Optional[int] = None,
            max_byte1: Optional[int] = None,
            all_chars_exist: Optional[bool] = None,
            font_ascent: Optional[int] = None,
            font_descent: Optional[int] = None,
            char_infos_len: Optional[int] = None,
            properties: Optional[Sequence[int]] = None,
            char_infos: Optional[Sequence[int]] = None,
    ) -> None:
        self.min_bounds = min_bounds
        self.max_bounds = max_bounds
        self.min_char_or_byte2 = min_char_or_byte2
        self.max_char_or_byte2 = max_char_or_byte2
        self.default_char = default_char
        self.properties_len = properties_len
        self.draw_direction = draw_direction
        self.min_byte1 = min_byte1
        self.max_byte1 = max_byte1
        self.all_chars_exist = all_chars_exist
        self.font_ascent = font_ascent
        self.font_descent = font_descent
        self.char_infos_len = char_infos_len
        self.properties = properties
        self.char_infos = char_infos

    def as_dict(self) -> Dict[str, Any]:
        return {
            'min_bounds': self.min_bounds,
            'max_bounds': self.max_bounds,
            'min_char_or_byte2': self.min_char_or_byte2,
            'max_char_or_byte2': self.max_char_or_byte2,
            'default_char': self.default_char,
            'properties_len': self.properties_len,
            'draw_direction': self.draw_direction,
            'min_byte1': self.min_byte1,
            'max_byte1': self.max_byte1,
            'all_chars_exist': self.all_chars_exist,
            'font_ascent': self.font_ascent,
            'font_descent': self.font_descent,
            'char_infos_len': self.char_infos_len,
            'properties': self.properties,
            'char_infos': self.char_infos,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryFontReplyReply':
        return QueryFontReplyReply(**QueryFontReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryFontReplyReplyPacket.pack(**self.as_dict())


class QueryFontReplyReplyCType(ctypes.Structure):
    """xproto QueryFont_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("min_bounds", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 4),
        ("max_bounds", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 4),
        ("min_char_or_byte2", ctypes.c_uint16),
        ("max_char_or_byte2", ctypes.c_uint16),
        ("default_char", ctypes.c_uint16),
        ("properties_len", ctypes.c_uint16),
        ("draw_direction", ctypes.c_int8),
        ("min_byte1", ctypes.c_uint8),
        ("max_byte1", ctypes.c_uint8),
        ("all_chars_exist", ctypes.c_int8),
        ("font_ascent", ctypes.c_int16),
        ("font_descent", ctypes.c_int16),
        ("char_infos_len", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


QueryTextExtentsRequestCookie = NewType('QueryTextExtentsRequestCookie', ctypes.c_uint32)


QueryTextExtentsRequestPacket = DataPacket((
    ('odd_length', None),
    ('font', FixedDataPacketField(MARKER_UINT32)),
    ('string', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class QueryTextExtentsRequest:
    OPCODE = 48

    __slots__ = ('odd_length', 'font', 'string',)

    def __init__(
            self, *,
            odd_length: Optional[int] = None,
            font: Optional[int] = None,
            string: Optional[Sequence[int]] = None,
    ) -> None:
        self.odd_length = odd_length
        self.font = font
        self.string = string

    def as_dict(self) -> Dict[str, Any]:
        return {
            'odd_length': self.odd_length,
            'font': self.font,
            'string': self.string,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryTextExtentsRequest':
        return QueryTextExtentsRequest(**QueryTextExtentsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryTextExtentsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], QueryTextExtentsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryTextExtentsRequest.lib = library.xproto_querytextextents
        QueryTextExtentsRequest.lib.restype = QueryTextExtentsRequestCookie
        QueryTextExtentsRequest.lib.argstype = (ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p)


class QueryTextExtentsRequestCType(ctypes.Structure):
    """xproto QueryTextExtents"""
    _fields_ = [
        ("var_data", ctypes.c_void_p),
    ]


QueryTextExtentsReplyReplyPacket = DataPacket((
    ('draw_direction', FixedDataPacketField(MARKER_INT8)),
    ('font_ascent', FixedDataPacketField(MARKER_INT16)),
    ('font_descent', FixedDataPacketField(MARKER_INT16)),
    ('overall_ascent', FixedDataPacketField(MARKER_INT16)),
    ('overall_descent', FixedDataPacketField(MARKER_INT16)),
    ('overall_width', FixedDataPacketField(MARKER_INT32)),
    ('overall_left', FixedDataPacketField(MARKER_INT32)),
    ('overall_right', FixedDataPacketField(MARKER_INT32)),
))


class QueryTextExtentsReplyReply:
    __slots__ = ('draw_direction', 'font_ascent', 'font_descent', 'overall_ascent', 'overall_descent', 'overall_width', 'overall_left', 'overall_right',)

    def __init__(
            self, *,
            draw_direction: Optional[int] = None,
            font_ascent: Optional[int] = None,
            font_descent: Optional[int] = None,
            overall_ascent: Optional[int] = None,
            overall_descent: Optional[int] = None,
            overall_width: Optional[int] = None,
            overall_left: Optional[int] = None,
            overall_right: Optional[int] = None,
    ) -> None:
        self.draw_direction = draw_direction
        self.font_ascent = font_ascent
        self.font_descent = font_descent
        self.overall_ascent = overall_ascent
        self.overall_descent = overall_descent
        self.overall_width = overall_width
        self.overall_left = overall_left
        self.overall_right = overall_right

    def as_dict(self) -> Dict[str, Any]:
        return {
            'draw_direction': self.draw_direction,
            'font_ascent': self.font_ascent,
            'font_descent': self.font_descent,
            'overall_ascent': self.overall_ascent,
            'overall_descent': self.overall_descent,
            'overall_width': self.overall_width,
            'overall_left': self.overall_left,
            'overall_right': self.overall_right,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryTextExtentsReplyReply':
        return QueryTextExtentsReplyReply(**QueryTextExtentsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryTextExtentsReplyReplyPacket.pack(**self.as_dict())


class QueryTextExtentsReplyReplyCType(ctypes.Structure):
    """xproto QueryTextExtents_reply"""
    _fields_ = [
        ("draw_direction", ctypes.c_int8),
        ("font_ascent", ctypes.c_int16),
        ("font_descent", ctypes.c_int16),
        ("overall_ascent", ctypes.c_int16),
        ("overall_descent", ctypes.c_int16),
        ("overall_width", ctypes.c_int32),
        ("overall_left", ctypes.c_int32),
        ("overall_right", ctypes.c_int32),
    ]


StrStructPacket = DataPacket((
    ('name_len', FixedDataPacketField(MARKER_UINT8)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['name_len'], 0)),
))


class StrStruct:
    __slots__ = ('name_len', 'name',)

    def __init__(
            self, *,
            name_len: Optional[int] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.name_len = name_len
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'name_len': self.name_len,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'StrStruct':
        return StrStruct(**StrStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return StrStructPacket.pack(**self.as_dict())


class StrStructCType(ctypes.Structure):
    """xproto STR"""
    _fields_ = [
        ("name_len", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


ListFontsRequestCookie = NewType('ListFontsRequestCookie', ctypes.c_uint32)


ListFontsRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('max_names', FixedDataPacketField(MARKER_UINT16)),
    ('pattern_len', FixedDataPacketField(MARKER_UINT16)),
    ('pattern', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['pattern_len'], 0)),
))


class ListFontsRequest:
    OPCODE = 49

    __slots__ = ('max_names', 'pattern_len', 'pattern',)

    def __init__(
            self, *,
            max_names: Optional[int] = None,
            pattern_len: Optional[int] = None,
            pattern: Optional[Sequence[int]] = None,
    ) -> None:
        self.max_names = max_names
        self.pattern_len = pattern_len
        self.pattern = pattern

    def as_dict(self) -> Dict[str, Any]:
        return {
            'max_names': self.max_names,
            'pattern_len': self.pattern_len,
            'pattern': self.pattern,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListFontsRequest':
        return ListFontsRequest(**ListFontsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListFontsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], ListFontsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ListFontsRequest.lib = library.xproto_listfonts
        ListFontsRequest.lib.restype = ListFontsRequestCookie
        ListFontsRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_void_p)


class ListFontsRequestCType(ctypes.Structure):
    """xproto ListFonts"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("max_names", ctypes.c_uint16),
        ("pattern_len", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


ListFontsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('names_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(22)),
    ('names', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['names_len'], 0)),
))


class ListFontsReplyReply:
    __slots__ = ('names_len', 'names',)

    def __init__(
            self, *,
            names_len: Optional[int] = None,
            names: Optional[Sequence[int]] = None,
    ) -> None:
        self.names_len = names_len
        self.names = names

    def as_dict(self) -> Dict[str, Any]:
        return {
            'names_len': self.names_len,
            'names': self.names,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListFontsReplyReply':
        return ListFontsReplyReply(**ListFontsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListFontsReplyReplyPacket.pack(**self.as_dict())


class ListFontsReplyReplyCType(ctypes.Structure):
    """xproto ListFonts_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("names_len", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 22),
        ("var_data", ctypes.c_void_p),
    ]


ListFontsWithInfoRequestCookie = NewType('ListFontsWithInfoRequestCookie', ctypes.c_uint32)


ListFontsWithInfoRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('max_names', FixedDataPacketField(MARKER_UINT16)),
    ('pattern_len', FixedDataPacketField(MARKER_UINT16)),
    ('pattern', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['pattern_len'], 0)),
))


class ListFontsWithInfoRequest:
    OPCODE = 50

    __slots__ = ('max_names', 'pattern_len', 'pattern',)

    def __init__(
            self, *,
            max_names: Optional[int] = None,
            pattern_len: Optional[int] = None,
            pattern: Optional[Sequence[int]] = None,
    ) -> None:
        self.max_names = max_names
        self.pattern_len = pattern_len
        self.pattern = pattern

    def as_dict(self) -> Dict[str, Any]:
        return {
            'max_names': self.max_names,
            'pattern_len': self.pattern_len,
            'pattern': self.pattern,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListFontsWithInfoRequest':
        return ListFontsWithInfoRequest(**ListFontsWithInfoRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListFontsWithInfoRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], ListFontsWithInfoRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ListFontsWithInfoRequest.lib = library.xproto_listfontswithinfo
        ListFontsWithInfoRequest.lib.restype = ListFontsWithInfoRequestCookie
        ListFontsWithInfoRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_void_p)


class ListFontsWithInfoRequestCType(ctypes.Structure):
    """xproto ListFontsWithInfo"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("max_names", ctypes.c_uint16),
        ("pattern_len", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


ListFontsWithInfoReplyReplyPacket = DataPacket((
    ('name_len', FixedDataPacketField(MARKER_UINT8)),
    ('min_bounds', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(4)),
    ('max_bounds', FixedDataPacketField(MARKER_UINT32)),
    ('pad1', FixedPadDataPacketField(4)),
    ('min_char_or_byte2', FixedDataPacketField(MARKER_UINT16)),
    ('max_char_or_byte2', FixedDataPacketField(MARKER_UINT16)),
    ('default_char', FixedDataPacketField(MARKER_UINT16)),
    ('properties_len', FixedDataPacketField(MARKER_UINT16)),
    ('draw_direction', FixedDataPacketField(MARKER_INT8)),
    ('min_byte1', FixedDataPacketField(MARKER_UINT8)),
    ('max_byte1', FixedDataPacketField(MARKER_UINT8)),
    ('all_chars_exist', FixedDataPacketField(MARKER_UINT8)),
    ('font_ascent', FixedDataPacketField(MARKER_INT16)),
    ('font_descent', FixedDataPacketField(MARKER_INT16)),
    ('replies_hint', FixedDataPacketField(MARKER_UINT32)),
    ('properties', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['properties_len'], 0)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['name_len'], 0)),
))


class ListFontsWithInfoReplyReply:
    __slots__ = ('name_len', 'min_bounds', 'max_bounds', 'min_char_or_byte2', 'max_char_or_byte2', 'default_char', 'properties_len', 'draw_direction', 'min_byte1', 'max_byte1', 'all_chars_exist', 'font_ascent', 'font_descent', 'replies_hint', 'properties', 'name',)

    def __init__(
            self, *,
            name_len: Optional[int] = None,
            min_bounds: Optional[int] = None,
            max_bounds: Optional[int] = None,
            min_char_or_byte2: Optional[int] = None,
            max_char_or_byte2: Optional[int] = None,
            default_char: Optional[int] = None,
            properties_len: Optional[int] = None,
            draw_direction: Optional[int] = None,
            min_byte1: Optional[int] = None,
            max_byte1: Optional[int] = None,
            all_chars_exist: Optional[bool] = None,
            font_ascent: Optional[int] = None,
            font_descent: Optional[int] = None,
            replies_hint: Optional[int] = None,
            properties: Optional[Sequence[int]] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.name_len = name_len
        self.min_bounds = min_bounds
        self.max_bounds = max_bounds
        self.min_char_or_byte2 = min_char_or_byte2
        self.max_char_or_byte2 = max_char_or_byte2
        self.default_char = default_char
        self.properties_len = properties_len
        self.draw_direction = draw_direction
        self.min_byte1 = min_byte1
        self.max_byte1 = max_byte1
        self.all_chars_exist = all_chars_exist
        self.font_ascent = font_ascent
        self.font_descent = font_descent
        self.replies_hint = replies_hint
        self.properties = properties
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'name_len': self.name_len,
            'min_bounds': self.min_bounds,
            'max_bounds': self.max_bounds,
            'min_char_or_byte2': self.min_char_or_byte2,
            'max_char_or_byte2': self.max_char_or_byte2,
            'default_char': self.default_char,
            'properties_len': self.properties_len,
            'draw_direction': self.draw_direction,
            'min_byte1': self.min_byte1,
            'max_byte1': self.max_byte1,
            'all_chars_exist': self.all_chars_exist,
            'font_ascent': self.font_ascent,
            'font_descent': self.font_descent,
            'replies_hint': self.replies_hint,
            'properties': self.properties,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListFontsWithInfoReplyReply':
        return ListFontsWithInfoReplyReply(**ListFontsWithInfoReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListFontsWithInfoReplyReplyPacket.pack(**self.as_dict())


class ListFontsWithInfoReplyReplyCType(ctypes.Structure):
    """xproto ListFontsWithInfo_reply"""
    _fields_ = [
        ("name_len", ctypes.c_uint8),
        ("min_bounds", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 4),
        ("max_bounds", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * 4),
        ("min_char_or_byte2", ctypes.c_uint16),
        ("max_char_or_byte2", ctypes.c_uint16),
        ("default_char", ctypes.c_uint16),
        ("properties_len", ctypes.c_uint16),
        ("draw_direction", ctypes.c_int8),
        ("min_byte1", ctypes.c_uint8),
        ("max_byte1", ctypes.c_uint8),
        ("all_chars_exist", ctypes.c_int8),
        ("font_ascent", ctypes.c_int16),
        ("font_descent", ctypes.c_int16),
        ("replies_hint", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


SetFontPathRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('font_qty', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(2)),
    ('font', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['font_qty'], 0)),
))


class SetFontPathRequest:
    OPCODE = 51

    __slots__ = ('font_qty', 'font',)

    def __init__(
            self, *,
            font_qty: Optional[int] = None,
            font: Optional[Sequence[int]] = None,
    ) -> None:
        self.font_qty = font_qty
        self.font = font

    def as_dict(self) -> Dict[str, Any]:
        return {
            'font_qty': self.font_qty,
            'font': self.font,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetFontPathRequest':
        return SetFontPathRequest(**SetFontPathRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetFontPathRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetFontPathRequest.lib = library.xproto_setfontpath
        SetFontPathRequest.lib.restype = ctypes.c_uint32
        SetFontPathRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_void_p)


class SetFontPathRequestCType(ctypes.Structure):
    """xproto SetFontPath"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("font_qty", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


GetFontPathRequestCookie = NewType('GetFontPathRequestCookie', ctypes.c_uint32)


GetFontPathRequestPacket = DataPacket((
))


class GetFontPathRequest:
    OPCODE = 52

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetFontPathRequest':
        return GetFontPathRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], GetFontPathRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetFontPathRequest.lib = library.xproto_getfontpath
        GetFontPathRequest.lib.restype = GetFontPathRequestCookie
        GetFontPathRequest.lib.argstype = ()


class GetFontPathRequestCType(ctypes.Structure):
    """xproto GetFontPath"""
    _fields_ = [
    ]


GetFontPathReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('path_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(22)),
    ('path', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['path_len'], 0)),
))


class GetFontPathReplyReply:
    __slots__ = ('path_len', 'path',)

    def __init__(
            self, *,
            path_len: Optional[int] = None,
            path: Optional[Sequence[int]] = None,
    ) -> None:
        self.path_len = path_len
        self.path = path

    def as_dict(self) -> Dict[str, Any]:
        return {
            'path_len': self.path_len,
            'path': self.path,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetFontPathReplyReply':
        return GetFontPathReplyReply(**GetFontPathReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetFontPathReplyReplyPacket.pack(**self.as_dict())


class GetFontPathReplyReplyCType(ctypes.Structure):
    """xproto GetFontPath_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("path_len", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 22),
        ("var_data", ctypes.c_void_p),
    ]


CreatePixmapRequestPacket = DataPacket((
    ('depth', FixedDataPacketField(MARKER_UINT8)),
    ('pid', FixedDataPacketField(MARKER_UINT32)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
))


class CreatePixmapRequest:
    OPCODE = 53

    __slots__ = ('depth', 'pid', 'drawable', 'width', 'height',)

    def __init__(
            self, *,
            depth: Optional[int] = None,
            pid: Optional[int] = None,
            drawable: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
    ) -> None:
        self.depth = depth
        self.pid = pid
        self.drawable = drawable
        self.width = width
        self.height = height

    def as_dict(self) -> Dict[str, Any]:
        return {
            'depth': self.depth,
            'pid': self.pid,
            'drawable': self.drawable,
            'width': self.width,
            'height': self.height,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreatePixmapRequest':
        return CreatePixmapRequest(**CreatePixmapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreatePixmapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreatePixmapRequest.lib = library.xproto_createpixmap
        CreatePixmapRequest.lib.restype = ctypes.c_uint32
        CreatePixmapRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16)


class CreatePixmapRequestCType(ctypes.Structure):
    """xproto CreatePixmap"""
    _fields_ = [
        ("depth", ctypes.c_uint8),
        ("pid", ctypes.c_uint32),
        ("drawable", ctypes.c_uint32),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
    ]


FreePixmapRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pixmap', FixedDataPacketField(MARKER_UINT32)),
))


class FreePixmapRequest:
    OPCODE = 54

    __slots__ = ('pixmap',)

    def __init__(
            self, *,
            pixmap: Optional[int] = None,
    ) -> None:
        self.pixmap = pixmap

    def as_dict(self) -> Dict[str, Any]:
        return {
            'pixmap': self.pixmap,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FreePixmapRequest':
        return FreePixmapRequest(**FreePixmapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FreePixmapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        FreePixmapRequest.lib = library.xproto_freepixmap
        FreePixmapRequest.lib.restype = ctypes.c_uint32
        FreePixmapRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class FreePixmapRequestCType(ctypes.Structure):
    """xproto FreePixmap"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pixmap", ctypes.c_uint32),
    ]


CreateGcRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('cid', FixedDataPacketField(MARKER_UINT32)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('value_mask', FixedDataPacketField(MARKER_UINT32)),
    ('value_list', BitDataPacketField(lambda d, c: d['value_mask'], {
        GcValues.FUNCTION: FixedDataPacketField(MARKER_UINT32),
        GcValues.PLANE_MASK: FixedDataPacketField(MARKER_UINT32),
        GcValues.FOREGROUND: FixedDataPacketField(MARKER_UINT32),
        GcValues.BACKGROUND: FixedDataPacketField(MARKER_UINT32),
        GcValues.LINE_WIDTH: FixedDataPacketField(MARKER_UINT32),
        GcValues.LINE_STYLE: FixedDataPacketField(MARKER_UINT32),
        GcValues.CAP_STYLE: FixedDataPacketField(MARKER_UINT32),
        GcValues.JOIN_STYLE: FixedDataPacketField(MARKER_UINT32),
        GcValues.FILL_STYLE: FixedDataPacketField(MARKER_UINT32),
        GcValues.FILL_RULE: FixedDataPacketField(MARKER_UINT32),
        GcValues.TILE: FixedDataPacketField(MARKER_UINT32),
        GcValues.STIPPLE: FixedDataPacketField(MARKER_UINT32),
        GcValues.TILE_STIPPLE_ORIGIN_X: FixedDataPacketField(MARKER_INT32),
        GcValues.TILE_STIPPLE_ORIGIN_Y: FixedDataPacketField(MARKER_INT32),
        GcValues.FONT: FixedDataPacketField(MARKER_UINT32),
        GcValues.SUBWINDOW_MODE: FixedDataPacketField(MARKER_UINT32),
        GcValues.GRAPHICS_EXPOSURES: FixedDataPacketField(MARKER_UINT32),
        GcValues.CLIP_ORIGIN_X: FixedDataPacketField(MARKER_INT32),
        GcValues.CLIP_ORIGIN_Y: FixedDataPacketField(MARKER_INT32),
        GcValues.CLIP_MASK: FixedDataPacketField(MARKER_UINT32),
        GcValues.DASH_OFFSET: FixedDataPacketField(MARKER_UINT32),
        GcValues.DASH_LIST: FixedDataPacketField(MARKER_UINT32),
        GcValues.ARC_MODE: FixedDataPacketField(MARKER_UINT32),
    }, 0)),
))


class CreateGcRequest:
    OPCODE = 55

    __slots__ = ('cid', 'drawable', 'value_mask', 'value_list',)

    def __init__(
            self, *,
            cid: Optional[int] = None,
            drawable: Optional[int] = None,
            value_mask: Optional[int] = None,
            value_list: Optional[Mapping[str, GcValues]] = None,
    ) -> None:
        self.cid = cid
        self.drawable = drawable
        self.value_mask = value_mask
        self.value_list = value_list

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cid': self.cid,
            'drawable': self.drawable,
            'value_mask': self.value_mask,
            'value_list': self.value_list,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateGcRequest':
        return CreateGcRequest(**CreateGcRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateGcRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, Mapping[str, GcValues]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateGcRequest.lib = library.xproto_creategc
        CreateGcRequest.lib.restype = ctypes.c_uint32
        CreateGcRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class CreateGcRequestCType(ctypes.Structure):
    """xproto CreateGC"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("cid", ctypes.c_uint32),
        ("drawable", ctypes.c_uint32),
        ("value_mask", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


ChangeGcRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('value_mask', FixedDataPacketField(MARKER_UINT32)),
    ('value_list', BitDataPacketField(lambda d, c: d['value_mask'], {
        GcValues.FUNCTION: FixedDataPacketField(MARKER_UINT32),
        GcValues.PLANE_MASK: FixedDataPacketField(MARKER_UINT32),
        GcValues.FOREGROUND: FixedDataPacketField(MARKER_UINT32),
        GcValues.BACKGROUND: FixedDataPacketField(MARKER_UINT32),
        GcValues.LINE_WIDTH: FixedDataPacketField(MARKER_UINT32),
        GcValues.LINE_STYLE: FixedDataPacketField(MARKER_UINT32),
        GcValues.CAP_STYLE: FixedDataPacketField(MARKER_UINT32),
        GcValues.JOIN_STYLE: FixedDataPacketField(MARKER_UINT32),
        GcValues.FILL_STYLE: FixedDataPacketField(MARKER_UINT32),
        GcValues.FILL_RULE: FixedDataPacketField(MARKER_UINT32),
        GcValues.TILE: FixedDataPacketField(MARKER_UINT32),
        GcValues.STIPPLE: FixedDataPacketField(MARKER_UINT32),
        GcValues.TILE_STIPPLE_ORIGIN_X: FixedDataPacketField(MARKER_INT32),
        GcValues.TILE_STIPPLE_ORIGIN_Y: FixedDataPacketField(MARKER_INT32),
        GcValues.FONT: FixedDataPacketField(MARKER_UINT32),
        GcValues.SUBWINDOW_MODE: FixedDataPacketField(MARKER_UINT32),
        GcValues.GRAPHICS_EXPOSURES: FixedDataPacketField(MARKER_UINT32),
        GcValues.CLIP_ORIGIN_X: FixedDataPacketField(MARKER_INT32),
        GcValues.CLIP_ORIGIN_Y: FixedDataPacketField(MARKER_INT32),
        GcValues.CLIP_MASK: FixedDataPacketField(MARKER_UINT32),
        GcValues.DASH_OFFSET: FixedDataPacketField(MARKER_UINT32),
        GcValues.DASH_LIST: FixedDataPacketField(MARKER_UINT32),
        GcValues.ARC_MODE: FixedDataPacketField(MARKER_UINT32),
    }, 0)),
))


class ChangeGcRequest:
    OPCODE = 56

    __slots__ = ('gc', 'value_mask', 'value_list',)

    def __init__(
            self, *,
            gc: Optional[int] = None,
            value_mask: Optional[int] = None,
            value_list: Optional[Mapping[str, GcValues]] = None,
    ) -> None:
        self.gc = gc
        self.value_mask = value_mask
        self.value_list = value_list

    def as_dict(self) -> Dict[str, Any]:
        return {
            'gc': self.gc,
            'value_mask': self.value_mask,
            'value_list': self.value_list,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeGcRequest':
        return ChangeGcRequest(**ChangeGcRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeGcRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Mapping[str, GcValues]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangeGcRequest.lib = library.xproto_changegc
        ChangeGcRequest.lib.restype = ctypes.c_uint32
        ChangeGcRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class ChangeGcRequestCType(ctypes.Structure):
    """xproto ChangeGC"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("gc", ctypes.c_uint32),
        ("value_mask", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


CopyGcRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('src_gc', FixedDataPacketField(MARKER_UINT32)),
    ('dst_gc', FixedDataPacketField(MARKER_UINT32)),
    ('value_mask', FixedDataPacketField(MARKER_UINT32)),
))


class CopyGcRequest:
    OPCODE = 57

    __slots__ = ('src_gc', 'dst_gc', 'value_mask',)

    def __init__(
            self, *,
            src_gc: Optional[int] = None,
            dst_gc: Optional[int] = None,
            value_mask: Optional[int] = None,
    ) -> None:
        self.src_gc = src_gc
        self.dst_gc = dst_gc
        self.value_mask = value_mask

    def as_dict(self) -> Dict[str, Any]:
        return {
            'src_gc': self.src_gc,
            'dst_gc': self.dst_gc,
            'value_mask': self.value_mask,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CopyGcRequest':
        return CopyGcRequest(**CopyGcRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CopyGcRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CopyGcRequest.lib = library.xproto_copygc
        CopyGcRequest.lib.restype = ctypes.c_uint32
        CopyGcRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class CopyGcRequestCType(ctypes.Structure):
    """xproto CopyGC"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("src_gc", ctypes.c_uint32),
        ("dst_gc", ctypes.c_uint32),
        ("value_mask", ctypes.c_uint32),
    ]


SetDashesRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('dash_offset', FixedDataPacketField(MARKER_UINT16)),
    ('dashes_len', FixedDataPacketField(MARKER_UINT16)),
    ('dashes', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['dashes_len'], 0)),
))


class SetDashesRequest:
    OPCODE = 58

    __slots__ = ('gc', 'dash_offset', 'dashes_len', 'dashes',)

    def __init__(
            self, *,
            gc: Optional[int] = None,
            dash_offset: Optional[int] = None,
            dashes_len: Optional[int] = None,
            dashes: Optional[Sequence[int]] = None,
    ) -> None:
        self.gc = gc
        self.dash_offset = dash_offset
        self.dashes_len = dashes_len
        self.dashes = dashes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'gc': self.gc,
            'dash_offset': self.dash_offset,
            'dashes_len': self.dashes_len,
            'dashes': self.dashes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetDashesRequest':
        return SetDashesRequest(**SetDashesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetDashesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetDashesRequest.lib = library.xproto_setdashes
        SetDashesRequest.lib.restype = ctypes.c_uint32
        SetDashesRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_void_p)


class SetDashesRequestCType(ctypes.Structure):
    """xproto SetDashes"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("gc", ctypes.c_uint32),
        ("dash_offset", ctypes.c_uint16),
        ("dashes_len", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


SetClipRectanglesRequestPacket = DataPacket((
    ('ordering', FixedDataPacketField(MARKER_INT8)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('clip_x_origin', FixedDataPacketField(MARKER_INT16)),
    ('clip_y_origin', FixedDataPacketField(MARKER_INT16)),
    ('rectangles', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class SetClipRectanglesRequest:
    OPCODE = 59

    __slots__ = ('ordering', 'gc', 'clip_x_origin', 'clip_y_origin', 'rectangles',)

    def __init__(
            self, *,
            ordering: Optional[int] = None,
            gc: Optional[int] = None,
            clip_x_origin: Optional[int] = None,
            clip_y_origin: Optional[int] = None,
            rectangles: Optional[Sequence[int]] = None,
    ) -> None:
        self.ordering = ordering
        self.gc = gc
        self.clip_x_origin = clip_x_origin
        self.clip_y_origin = clip_y_origin
        self.rectangles = rectangles

    def as_dict(self) -> Dict[str, Any]:
        return {
            'ordering': self.ordering,
            'gc': self.gc,
            'clip_x_origin': self.clip_x_origin,
            'clip_y_origin': self.clip_y_origin,
            'rectangles': self.rectangles,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetClipRectanglesRequest':
        return SetClipRectanglesRequest(**SetClipRectanglesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetClipRectanglesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetClipRectanglesRequest.lib = library.xproto_setcliprectangles
        SetClipRectanglesRequest.lib.restype = ctypes.c_uint32
        SetClipRectanglesRequest.lib.argstype = (ctypes.c_int8, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_void_p)


class SetClipRectanglesRequestCType(ctypes.Structure):
    """xproto SetClipRectangles"""
    _fields_ = [
        ("ordering", ctypes.c_int8),
        ("gc", ctypes.c_uint32),
        ("clip_x_origin", ctypes.c_int16),
        ("clip_y_origin", ctypes.c_int16),
        ("var_data", ctypes.c_void_p),
    ]


FreeGcRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
))


class FreeGcRequest:
    OPCODE = 60

    __slots__ = ('gc',)

    def __init__(
            self, *,
            gc: Optional[int] = None,
    ) -> None:
        self.gc = gc

    def as_dict(self) -> Dict[str, Any]:
        return {
            'gc': self.gc,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FreeGcRequest':
        return FreeGcRequest(**FreeGcRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FreeGcRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        FreeGcRequest.lib = library.xproto_freegc
        FreeGcRequest.lib.restype = ctypes.c_uint32
        FreeGcRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class FreeGcRequestCType(ctypes.Structure):
    """xproto FreeGC"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("gc", ctypes.c_uint32),
    ]


ClearAreaRequestPacket = DataPacket((
    ('exposures', FixedDataPacketField(MARKER_UINT8)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
))


class ClearAreaRequest:
    OPCODE = 61

    __slots__ = ('exposures', 'window', 'x', 'y', 'width', 'height',)

    def __init__(
            self, *,
            exposures: Optional[bool] = None,
            window: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
    ) -> None:
        self.exposures = exposures
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def as_dict(self) -> Dict[str, Any]:
        return {
            'exposures': self.exposures,
            'window': self.window,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ClearAreaRequest':
        return ClearAreaRequest(**ClearAreaRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ClearAreaRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[bool, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ClearAreaRequest.lib = library.xproto_cleararea
        ClearAreaRequest.lib.restype = ctypes.c_uint32
        ClearAreaRequest.lib.argstype = (ctypes.c_int8, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint16)


class ClearAreaRequestCType(ctypes.Structure):
    """xproto ClearArea"""
    _fields_ = [
        ("exposures", ctypes.c_int8),
        ("window", ctypes.c_uint32),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
    ]


CopyAreaRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('src_drawable', FixedDataPacketField(MARKER_UINT32)),
    ('dst_drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('src_x', FixedDataPacketField(MARKER_INT16)),
    ('src_y', FixedDataPacketField(MARKER_INT16)),
    ('dst_x', FixedDataPacketField(MARKER_INT16)),
    ('dst_y', FixedDataPacketField(MARKER_INT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
))


class CopyAreaRequest:
    OPCODE = 62

    __slots__ = ('src_drawable', 'dst_drawable', 'gc', 'src_x', 'src_y', 'dst_x', 'dst_y', 'width', 'height',)

    def __init__(
            self, *,
            src_drawable: Optional[int] = None,
            dst_drawable: Optional[int] = None,
            gc: Optional[int] = None,
            src_x: Optional[int] = None,
            src_y: Optional[int] = None,
            dst_x: Optional[int] = None,
            dst_y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
    ) -> None:
        self.src_drawable = src_drawable
        self.dst_drawable = dst_drawable
        self.gc = gc
        self.src_x = src_x
        self.src_y = src_y
        self.dst_x = dst_x
        self.dst_y = dst_y
        self.width = width
        self.height = height

    def as_dict(self) -> Dict[str, Any]:
        return {
            'src_drawable': self.src_drawable,
            'dst_drawable': self.dst_drawable,
            'gc': self.gc,
            'src_x': self.src_x,
            'src_y': self.src_y,
            'dst_x': self.dst_x,
            'dst_y': self.dst_y,
            'width': self.width,
            'height': self.height,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CopyAreaRequest':
        return CopyAreaRequest(**CopyAreaRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CopyAreaRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CopyAreaRequest.lib = library.xproto_copyarea
        CopyAreaRequest.lib.restype = ctypes.c_uint32
        CopyAreaRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint16)


class CopyAreaRequestCType(ctypes.Structure):
    """xproto CopyArea"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("src_drawable", ctypes.c_uint32),
        ("dst_drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("src_x", ctypes.c_int16),
        ("src_y", ctypes.c_int16),
        ("dst_x", ctypes.c_int16),
        ("dst_y", ctypes.c_int16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
    ]


CopyPlaneRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('src_drawable', FixedDataPacketField(MARKER_UINT32)),
    ('dst_drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('src_x', FixedDataPacketField(MARKER_INT16)),
    ('src_y', FixedDataPacketField(MARKER_INT16)),
    ('dst_x', FixedDataPacketField(MARKER_INT16)),
    ('dst_y', FixedDataPacketField(MARKER_INT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('bit_plane', FixedDataPacketField(MARKER_UINT32)),
))


class CopyPlaneRequest:
    OPCODE = 63

    __slots__ = ('src_drawable', 'dst_drawable', 'gc', 'src_x', 'src_y', 'dst_x', 'dst_y', 'width', 'height', 'bit_plane',)

    def __init__(
            self, *,
            src_drawable: Optional[int] = None,
            dst_drawable: Optional[int] = None,
            gc: Optional[int] = None,
            src_x: Optional[int] = None,
            src_y: Optional[int] = None,
            dst_x: Optional[int] = None,
            dst_y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            bit_plane: Optional[int] = None,
    ) -> None:
        self.src_drawable = src_drawable
        self.dst_drawable = dst_drawable
        self.gc = gc
        self.src_x = src_x
        self.src_y = src_y
        self.dst_x = dst_x
        self.dst_y = dst_y
        self.width = width
        self.height = height
        self.bit_plane = bit_plane

    def as_dict(self) -> Dict[str, Any]:
        return {
            'src_drawable': self.src_drawable,
            'dst_drawable': self.dst_drawable,
            'gc': self.gc,
            'src_x': self.src_x,
            'src_y': self.src_y,
            'dst_x': self.dst_x,
            'dst_y': self.dst_y,
            'width': self.width,
            'height': self.height,
            'bit_plane': self.bit_plane,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CopyPlaneRequest':
        return CopyPlaneRequest(**CopyPlaneRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CopyPlaneRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CopyPlaneRequest.lib = library.xproto_copyplane
        CopyPlaneRequest.lib.restype = ctypes.c_uint32
        CopyPlaneRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint32)


class CopyPlaneRequestCType(ctypes.Structure):
    """xproto CopyPlane"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("src_drawable", ctypes.c_uint32),
        ("dst_drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("src_x", ctypes.c_int16),
        ("src_y", ctypes.c_int16),
        ("dst_x", ctypes.c_int16),
        ("dst_y", ctypes.c_int16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("bit_plane", ctypes.c_uint32),
    ]


PolyPointRequestPacket = DataPacket((
    ('coordinate_mode', FixedDataPacketField(MARKER_INT8)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('points', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class PolyPointRequest:
    OPCODE = 64

    __slots__ = ('coordinate_mode', 'drawable', 'gc', 'points',)

    def __init__(
            self, *,
            coordinate_mode: Optional[int] = None,
            drawable: Optional[int] = None,
            gc: Optional[int] = None,
            points: Optional[Sequence[int]] = None,
    ) -> None:
        self.coordinate_mode = coordinate_mode
        self.drawable = drawable
        self.gc = gc
        self.points = points

    def as_dict(self) -> Dict[str, Any]:
        return {
            'coordinate_mode': self.coordinate_mode,
            'drawable': self.drawable,
            'gc': self.gc,
            'points': self.points,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PolyPointRequest':
        return PolyPointRequest(**PolyPointRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PolyPointRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PolyPointRequest.lib = library.xproto_polypoint
        PolyPointRequest.lib.restype = ctypes.c_uint32
        PolyPointRequest.lib.argstype = (ctypes.c_int8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class PolyPointRequestCType(ctypes.Structure):
    """xproto PolyPoint"""
    _fields_ = [
        ("coordinate_mode", ctypes.c_int8),
        ("drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


PolyLineRequestPacket = DataPacket((
    ('coordinate_mode', FixedDataPacketField(MARKER_INT8)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('points', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class PolyLineRequest:
    OPCODE = 65

    __slots__ = ('coordinate_mode', 'drawable', 'gc', 'points',)

    def __init__(
            self, *,
            coordinate_mode: Optional[int] = None,
            drawable: Optional[int] = None,
            gc: Optional[int] = None,
            points: Optional[Sequence[int]] = None,
    ) -> None:
        self.coordinate_mode = coordinate_mode
        self.drawable = drawable
        self.gc = gc
        self.points = points

    def as_dict(self) -> Dict[str, Any]:
        return {
            'coordinate_mode': self.coordinate_mode,
            'drawable': self.drawable,
            'gc': self.gc,
            'points': self.points,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PolyLineRequest':
        return PolyLineRequest(**PolyLineRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PolyLineRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PolyLineRequest.lib = library.xproto_polyline
        PolyLineRequest.lib.restype = ctypes.c_uint32
        PolyLineRequest.lib.argstype = (ctypes.c_int8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class PolyLineRequestCType(ctypes.Structure):
    """xproto PolyLine"""
    _fields_ = [
        ("coordinate_mode", ctypes.c_int8),
        ("drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


SegmentStructPacket = DataPacket((
    ('x1', FixedDataPacketField(MARKER_INT16)),
    ('y1', FixedDataPacketField(MARKER_INT16)),
    ('x2', FixedDataPacketField(MARKER_INT16)),
    ('y2', FixedDataPacketField(MARKER_INT16)),
))


class SegmentStruct:
    __slots__ = ('x1', 'y1', 'x2', 'y2',)

    def __init__(
            self, *,
            x1: Optional[int] = None,
            y1: Optional[int] = None,
            x2: Optional[int] = None,
            y2: Optional[int] = None,
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def as_dict(self) -> Dict[str, Any]:
        return {
            'x1': self.x1,
            'y1': self.y1,
            'x2': self.x2,
            'y2': self.y2,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SegmentStruct':
        return SegmentStruct(**SegmentStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SegmentStructPacket.pack(**self.as_dict())


class SegmentStructCType(ctypes.Structure):
    """xproto SEGMENT"""
    _fields_ = [
        ("x1", ctypes.c_int16),
        ("y1", ctypes.c_int16),
        ("x2", ctypes.c_int16),
        ("y2", ctypes.c_int16),
    ]


PolySegmentRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('segments', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class PolySegmentRequest:
    OPCODE = 66

    __slots__ = ('drawable', 'gc', 'segments',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            gc: Optional[int] = None,
            segments: Optional[Sequence[int]] = None,
    ) -> None:
        self.drawable = drawable
        self.gc = gc
        self.segments = segments

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'gc': self.gc,
            'segments': self.segments,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PolySegmentRequest':
        return PolySegmentRequest(**PolySegmentRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PolySegmentRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PolySegmentRequest.lib = library.xproto_polysegment
        PolySegmentRequest.lib.restype = ctypes.c_uint32
        PolySegmentRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class PolySegmentRequestCType(ctypes.Structure):
    """xproto PolySegment"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


PolyRectangleRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('rectangles', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class PolyRectangleRequest:
    OPCODE = 67

    __slots__ = ('drawable', 'gc', 'rectangles',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            gc: Optional[int] = None,
            rectangles: Optional[Sequence[int]] = None,
    ) -> None:
        self.drawable = drawable
        self.gc = gc
        self.rectangles = rectangles

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'gc': self.gc,
            'rectangles': self.rectangles,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PolyRectangleRequest':
        return PolyRectangleRequest(**PolyRectangleRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PolyRectangleRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PolyRectangleRequest.lib = library.xproto_polyrectangle
        PolyRectangleRequest.lib.restype = ctypes.c_uint32
        PolyRectangleRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class PolyRectangleRequestCType(ctypes.Structure):
    """xproto PolyRectangle"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


PolyArcRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('arcs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class PolyArcRequest:
    OPCODE = 68

    __slots__ = ('drawable', 'gc', 'arcs',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            gc: Optional[int] = None,
            arcs: Optional[Sequence[int]] = None,
    ) -> None:
        self.drawable = drawable
        self.gc = gc
        self.arcs = arcs

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'gc': self.gc,
            'arcs': self.arcs,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PolyArcRequest':
        return PolyArcRequest(**PolyArcRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PolyArcRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PolyArcRequest.lib = library.xproto_polyarc
        PolyArcRequest.lib.restype = ctypes.c_uint32
        PolyArcRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class PolyArcRequestCType(ctypes.Structure):
    """xproto PolyArc"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


FillPolyRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('shape', FixedDataPacketField(MARKER_UINT8)),
    ('coordinate_mode', FixedDataPacketField(MARKER_UINT8)),
    ('pad1', FixedPadDataPacketField(2)),
    ('points', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class FillPolyRequest:
    OPCODE = 69

    __slots__ = ('drawable', 'gc', 'shape', 'coordinate_mode', 'points',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            gc: Optional[int] = None,
            shape: Optional[int] = None,
            coordinate_mode: Optional[int] = None,
            points: Optional[Sequence[int]] = None,
    ) -> None:
        self.drawable = drawable
        self.gc = gc
        self.shape = shape
        self.coordinate_mode = coordinate_mode
        self.points = points

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'gc': self.gc,
            'shape': self.shape,
            'coordinate_mode': self.coordinate_mode,
            'points': self.points,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FillPolyRequest':
        return FillPolyRequest(**FillPolyRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FillPolyRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        FillPolyRequest.lib = library.xproto_fillpoly
        FillPolyRequest.lib.restype = ctypes.c_uint32
        FillPolyRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8 * 2, ctypes.c_void_p)


class FillPolyRequestCType(ctypes.Structure):
    """xproto FillPoly"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("shape", ctypes.c_uint8),
        ("coordinate_mode", ctypes.c_uint8),
        ("pad1", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


PolyFillRectangleRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('rectangles', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class PolyFillRectangleRequest:
    OPCODE = 70

    __slots__ = ('drawable', 'gc', 'rectangles',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            gc: Optional[int] = None,
            rectangles: Optional[Sequence[int]] = None,
    ) -> None:
        self.drawable = drawable
        self.gc = gc
        self.rectangles = rectangles

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'gc': self.gc,
            'rectangles': self.rectangles,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PolyFillRectangleRequest':
        return PolyFillRectangleRequest(**PolyFillRectangleRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PolyFillRectangleRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PolyFillRectangleRequest.lib = library.xproto_polyfillrectangle
        PolyFillRectangleRequest.lib.restype = ctypes.c_uint32
        PolyFillRectangleRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class PolyFillRectangleRequestCType(ctypes.Structure):
    """xproto PolyFillRectangle"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


PolyFillArcRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('arcs', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class PolyFillArcRequest:
    OPCODE = 71

    __slots__ = ('drawable', 'gc', 'arcs',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            gc: Optional[int] = None,
            arcs: Optional[Sequence[int]] = None,
    ) -> None:
        self.drawable = drawable
        self.gc = gc
        self.arcs = arcs

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'gc': self.gc,
            'arcs': self.arcs,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PolyFillArcRequest':
        return PolyFillArcRequest(**PolyFillArcRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PolyFillArcRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PolyFillArcRequest.lib = library.xproto_polyfillarc
        PolyFillArcRequest.lib.restype = ctypes.c_uint32
        PolyFillArcRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class PolyFillArcRequestCType(ctypes.Structure):
    """xproto PolyFillArc"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


PutImageRequestPacket = DataPacket((
    ('format', FixedDataPacketField(MARKER_UINT8)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('dst_x', FixedDataPacketField(MARKER_INT16)),
    ('dst_y', FixedDataPacketField(MARKER_INT16)),
    ('left_pad', FixedDataPacketField(MARKER_UINT8)),
    ('depth', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('data', SimpleListDataPacketField(MARKER_INT8, lambda d, c: 1, 0)),
))


class PutImageRequest:
    OPCODE = 72

    __slots__ = ('format', 'drawable', 'gc', 'width', 'height', 'dst_x', 'dst_y', 'left_pad', 'depth', 'data',)

    def __init__(
            self, *,
            format: Optional[int] = None,
            drawable: Optional[int] = None,
            gc: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            dst_x: Optional[int] = None,
            dst_y: Optional[int] = None,
            left_pad: Optional[int] = None,
            depth: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.format = format
        self.drawable = drawable
        self.gc = gc
        self.width = width
        self.height = height
        self.dst_x = dst_x
        self.dst_y = dst_y
        self.left_pad = left_pad
        self.depth = depth
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'format': self.format,
            'drawable': self.drawable,
            'gc': self.gc,
            'width': self.width,
            'height': self.height,
            'dst_x': self.dst_x,
            'dst_y': self.dst_y,
            'left_pad': self.left_pad,
            'depth': self.depth,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PutImageRequest':
        return PutImageRequest(**PutImageRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PutImageRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PutImageRequest.lib = library.xproto_putimage
        PutImageRequest.lib.restype = ctypes.c_uint32
        PutImageRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8 * 2, ctypes.c_void_p)


class PutImageRequestCType(ctypes.Structure):
    """xproto PutImage"""
    _fields_ = [
        ("format", ctypes.c_uint8),
        ("drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("dst_x", ctypes.c_int16),
        ("dst_y", ctypes.c_int16),
        ("left_pad", ctypes.c_uint8),
        ("depth", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


GetImageRequestCookie = NewType('GetImageRequestCookie', ctypes.c_uint32)


GetImageRequestPacket = DataPacket((
    ('format', FixedDataPacketField(MARKER_UINT8)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
    ('plane_mask', FixedDataPacketField(MARKER_UINT32)),
))


class GetImageRequest:
    OPCODE = 73

    __slots__ = ('format', 'drawable', 'x', 'y', 'width', 'height', 'plane_mask',)

    def __init__(
            self, *,
            format: Optional[int] = None,
            drawable: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            plane_mask: Optional[int] = None,
    ) -> None:
        self.format = format
        self.drawable = drawable
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.plane_mask = plane_mask

    def as_dict(self) -> Dict[str, Any]:
        return {
            'format': self.format,
            'drawable': self.drawable,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'plane_mask': self.plane_mask,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetImageRequest':
        return GetImageRequest(**GetImageRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetImageRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int], GetImageRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetImageRequest.lib = library.xproto_getimage
        GetImageRequest.lib.restype = GetImageRequestCookie
        GetImageRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint32)


class GetImageRequestCType(ctypes.Structure):
    """xproto GetImage"""
    _fields_ = [
        ("format", ctypes.c_uint8),
        ("drawable", ctypes.c_uint32),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("plane_mask", ctypes.c_uint32),
    ]


GetImageReplyReplyPacket = DataPacket((
    ('depth', FixedDataPacketField(MARKER_UINT8)),
    ('visual', FixedDataPacketField(MARKER_UINT32)),
    ('pad0', FixedPadDataPacketField(20)),
    ('data', SimpleListDataPacketField(MARKER_INT8, lambda d, c: (d['length']) * (4), 0)),
))


class GetImageReplyReply:
    __slots__ = ('depth', 'visual', 'data',)

    def __init__(
            self, *,
            depth: Optional[int] = None,
            visual: Optional[int] = None,
            data: Optional[Sequence[int]] = None,
    ) -> None:
        self.depth = depth
        self.visual = visual
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        return {
            'depth': self.depth,
            'visual': self.visual,
            'data': self.data,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetImageReplyReply':
        return GetImageReplyReply(**GetImageReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetImageReplyReplyPacket.pack(**self.as_dict())


class GetImageReplyReplyCType(ctypes.Structure):
    """xproto GetImage_reply"""
    _fields_ = [
        ("depth", ctypes.c_uint8),
        ("visual", ctypes.c_uint32),
        ("pad0", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


PolyText8RequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('items', SimpleListDataPacketField(MARKER_INT8, lambda d, c: 1, 0)),
))


class PolyText8Request:
    OPCODE = 74

    __slots__ = ('drawable', 'gc', 'x', 'y', 'items',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            gc: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            items: Optional[Sequence[int]] = None,
    ) -> None:
        self.drawable = drawable
        self.gc = gc
        self.x = x
        self.y = y
        self.items = items

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'gc': self.gc,
            'x': self.x,
            'y': self.y,
            'items': self.items,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PolyText8Request':
        return PolyText8Request(**PolyText8RequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PolyText8RequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PolyText8Request.lib = library.xproto_polytext8
        PolyText8Request.lib.restype = ctypes.c_uint32
        PolyText8Request.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_void_p)


class PolyText8RequestCType(ctypes.Structure):
    """xproto PolyText8"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("var_data", ctypes.c_void_p),
    ]


PolyText16RequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('items', SimpleListDataPacketField(MARKER_INT8, lambda d, c: 1, 0)),
))


class PolyText16Request:
    OPCODE = 75

    __slots__ = ('drawable', 'gc', 'x', 'y', 'items',)

    def __init__(
            self, *,
            drawable: Optional[int] = None,
            gc: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            items: Optional[Sequence[int]] = None,
    ) -> None:
        self.drawable = drawable
        self.gc = gc
        self.x = x
        self.y = y
        self.items = items

    def as_dict(self) -> Dict[str, Any]:
        return {
            'drawable': self.drawable,
            'gc': self.gc,
            'x': self.x,
            'y': self.y,
            'items': self.items,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'PolyText16Request':
        return PolyText16Request(**PolyText16RequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return PolyText16RequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        PolyText16Request.lib = library.xproto_polytext16
        PolyText16Request.lib.restype = ctypes.c_uint32
        PolyText16Request.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_void_p)


class PolyText16RequestCType(ctypes.Structure):
    """xproto PolyText16"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("var_data", ctypes.c_void_p),
    ]


ImageText8RequestPacket = DataPacket((
    ('string_len', FixedDataPacketField(MARKER_INT8)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('string', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['string_len'], 0)),
))


class ImageText8Request:
    OPCODE = 76

    __slots__ = ('string_len', 'drawable', 'gc', 'x', 'y', 'string',)

    def __init__(
            self, *,
            string_len: Optional[int] = None,
            drawable: Optional[int] = None,
            gc: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            string: Optional[Sequence[int]] = None,
    ) -> None:
        self.string_len = string_len
        self.drawable = drawable
        self.gc = gc
        self.x = x
        self.y = y
        self.string = string

    def as_dict(self) -> Dict[str, Any]:
        return {
            'string_len': self.string_len,
            'drawable': self.drawable,
            'gc': self.gc,
            'x': self.x,
            'y': self.y,
            'string': self.string,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ImageText8Request':
        return ImageText8Request(**ImageText8RequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ImageText8RequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ImageText8Request.lib = library.xproto_imagetext8
        ImageText8Request.lib.restype = ctypes.c_uint32
        ImageText8Request.lib.argstype = (ctypes.c_int8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_void_p)


class ImageText8RequestCType(ctypes.Structure):
    """xproto ImageText8"""
    _fields_ = [
        ("string_len", ctypes.c_int8),
        ("drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("var_data", ctypes.c_void_p),
    ]


ImageText16RequestPacket = DataPacket((
    ('string_len', FixedDataPacketField(MARKER_INT8)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('gc', FixedDataPacketField(MARKER_UINT32)),
    ('x', FixedDataPacketField(MARKER_INT16)),
    ('y', FixedDataPacketField(MARKER_INT16)),
    ('string', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['string_len'], 0)),
))


class ImageText16Request:
    OPCODE = 77

    __slots__ = ('string_len', 'drawable', 'gc', 'x', 'y', 'string',)

    def __init__(
            self, *,
            string_len: Optional[int] = None,
            drawable: Optional[int] = None,
            gc: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            string: Optional[Sequence[int]] = None,
    ) -> None:
        self.string_len = string_len
        self.drawable = drawable
        self.gc = gc
        self.x = x
        self.y = y
        self.string = string

    def as_dict(self) -> Dict[str, Any]:
        return {
            'string_len': self.string_len,
            'drawable': self.drawable,
            'gc': self.gc,
            'x': self.x,
            'y': self.y,
            'string': self.string,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ImageText16Request':
        return ImageText16Request(**ImageText16RequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ImageText16RequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ImageText16Request.lib = library.xproto_imagetext16
        ImageText16Request.lib.restype = ctypes.c_uint32
        ImageText16Request.lib.argstype = (ctypes.c_int8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int16, ctypes.c_int16, ctypes.c_void_p)


class ImageText16RequestCType(ctypes.Structure):
    """xproto ImageText16"""
    _fields_ = [
        ("string_len", ctypes.c_int8),
        ("drawable", ctypes.c_uint32),
        ("gc", ctypes.c_uint32),
        ("x", ctypes.c_int16),
        ("y", ctypes.c_int16),
        ("var_data", ctypes.c_void_p),
    ]


CreateColormapRequestPacket = DataPacket((
    ('alloc', FixedDataPacketField(MARKER_INT8)),
    ('mid', FixedDataPacketField(MARKER_UINT32)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('visual', FixedDataPacketField(MARKER_UINT32)),
))


class CreateColormapRequest:
    OPCODE = 78

    __slots__ = ('alloc', 'mid', 'window', 'visual',)

    def __init__(
            self, *,
            alloc: Optional[int] = None,
            mid: Optional[int] = None,
            window: Optional[int] = None,
            visual: Optional[int] = None,
    ) -> None:
        self.alloc = alloc
        self.mid = mid
        self.window = window
        self.visual = visual

    def as_dict(self) -> Dict[str, Any]:
        return {
            'alloc': self.alloc,
            'mid': self.mid,
            'window': self.window,
            'visual': self.visual,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateColormapRequest':
        return CreateColormapRequest(**CreateColormapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateColormapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateColormapRequest.lib = library.xproto_createcolormap
        CreateColormapRequest.lib.restype = ctypes.c_uint32
        CreateColormapRequest.lib.argstype = (ctypes.c_int8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)


class CreateColormapRequestCType(ctypes.Structure):
    """xproto CreateColormap"""
    _fields_ = [
        ("alloc", ctypes.c_int8),
        ("mid", ctypes.c_uint32),
        ("window", ctypes.c_uint32),
        ("visual", ctypes.c_uint32),
    ]


FreeColormapRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('cmap', FixedDataPacketField(MARKER_UINT32)),
))


class FreeColormapRequest:
    OPCODE = 79

    __slots__ = ('cmap',)

    def __init__(
            self, *,
            cmap: Optional[int] = None,
    ) -> None:
        self.cmap = cmap

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cmap': self.cmap,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FreeColormapRequest':
        return FreeColormapRequest(**FreeColormapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FreeColormapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        FreeColormapRequest.lib = library.xproto_freecolormap
        FreeColormapRequest.lib.restype = ctypes.c_uint32
        FreeColormapRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class FreeColormapRequestCType(ctypes.Structure):
    """xproto FreeColormap"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("cmap", ctypes.c_uint32),
    ]


CopyColormapAndFreeRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('mid', FixedDataPacketField(MARKER_UINT32)),
    ('src_cmap', FixedDataPacketField(MARKER_UINT32)),
))


class CopyColormapAndFreeRequest:
    OPCODE = 80

    __slots__ = ('mid', 'src_cmap',)

    def __init__(
            self, *,
            mid: Optional[int] = None,
            src_cmap: Optional[int] = None,
    ) -> None:
        self.mid = mid
        self.src_cmap = src_cmap

    def as_dict(self) -> Dict[str, Any]:
        return {
            'mid': self.mid,
            'src_cmap': self.src_cmap,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CopyColormapAndFreeRequest':
        return CopyColormapAndFreeRequest(**CopyColormapAndFreeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CopyColormapAndFreeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CopyColormapAndFreeRequest.lib = library.xproto_copycolormapandfree
        CopyColormapAndFreeRequest.lib.restype = ctypes.c_uint32
        CopyColormapAndFreeRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32)


class CopyColormapAndFreeRequestCType(ctypes.Structure):
    """xproto CopyColormapAndFree"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("mid", ctypes.c_uint32),
        ("src_cmap", ctypes.c_uint32),
    ]


InstallColormapRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('cmap', FixedDataPacketField(MARKER_UINT32)),
))


class InstallColormapRequest:
    OPCODE = 81

    __slots__ = ('cmap',)

    def __init__(
            self, *,
            cmap: Optional[int] = None,
    ) -> None:
        self.cmap = cmap

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cmap': self.cmap,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'InstallColormapRequest':
        return InstallColormapRequest(**InstallColormapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return InstallColormapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        InstallColormapRequest.lib = library.xproto_installcolormap
        InstallColormapRequest.lib.restype = ctypes.c_uint32
        InstallColormapRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class InstallColormapRequestCType(ctypes.Structure):
    """xproto InstallColormap"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("cmap", ctypes.c_uint32),
    ]


UninstallColormapRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('cmap', FixedDataPacketField(MARKER_UINT32)),
))


class UninstallColormapRequest:
    OPCODE = 82

    __slots__ = ('cmap',)

    def __init__(
            self, *,
            cmap: Optional[int] = None,
    ) -> None:
        self.cmap = cmap

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cmap': self.cmap,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'UninstallColormapRequest':
        return UninstallColormapRequest(**UninstallColormapRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return UninstallColormapRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        UninstallColormapRequest.lib = library.xproto_uninstallcolormap
        UninstallColormapRequest.lib.restype = ctypes.c_uint32
        UninstallColormapRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class UninstallColormapRequestCType(ctypes.Structure):
    """xproto UninstallColormap"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("cmap", ctypes.c_uint32),
    ]


ListInstalledColormapsRequestCookie = NewType('ListInstalledColormapsRequestCookie', ctypes.c_uint32)


ListInstalledColormapsRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
))


class ListInstalledColormapsRequest:
    OPCODE = 83

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
    def from_data(inp: BinaryIO) -> 'ListInstalledColormapsRequest':
        return ListInstalledColormapsRequest(**ListInstalledColormapsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListInstalledColormapsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ListInstalledColormapsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ListInstalledColormapsRequest.lib = library.xproto_listinstalledcolormaps
        ListInstalledColormapsRequest.lib.restype = ListInstalledColormapsRequestCookie
        ListInstalledColormapsRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class ListInstalledColormapsRequestCType(ctypes.Structure):
    """xproto ListInstalledColormaps"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
    ]


ListInstalledColormapsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('cmaps_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(22)),
    ('cmaps', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['cmaps_len'], 0)),
))


class ListInstalledColormapsReplyReply:
    __slots__ = ('cmaps_len', 'cmaps',)

    def __init__(
            self, *,
            cmaps_len: Optional[int] = None,
            cmaps: Optional[Sequence[int]] = None,
    ) -> None:
        self.cmaps_len = cmaps_len
        self.cmaps = cmaps

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cmaps_len': self.cmaps_len,
            'cmaps': self.cmaps,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListInstalledColormapsReplyReply':
        return ListInstalledColormapsReplyReply(**ListInstalledColormapsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListInstalledColormapsReplyReplyPacket.pack(**self.as_dict())


class ListInstalledColormapsReplyReplyCType(ctypes.Structure):
    """xproto ListInstalledColormaps_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("cmaps_len", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 22),
        ("var_data", ctypes.c_void_p),
    ]


AllocColorRequestCookie = NewType('AllocColorRequestCookie', ctypes.c_uint32)


AllocColorRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('cmap', FixedDataPacketField(MARKER_UINT32)),
    ('red', FixedDataPacketField(MARKER_UINT16)),
    ('green', FixedDataPacketField(MARKER_UINT16)),
    ('blue', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(2)),
))


class AllocColorRequest:
    OPCODE = 84

    __slots__ = ('cmap', 'red', 'green', 'blue',)

    def __init__(
            self, *,
            cmap: Optional[int] = None,
            red: Optional[int] = None,
            green: Optional[int] = None,
            blue: Optional[int] = None,
    ) -> None:
        self.cmap = cmap
        self.red = red
        self.green = green
        self.blue = blue

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cmap': self.cmap,
            'red': self.red,
            'green': self.green,
            'blue': self.blue,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AllocColorRequest':
        return AllocColorRequest(**AllocColorRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AllocColorRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], AllocColorRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        AllocColorRequest.lib = library.xproto_alloccolor
        AllocColorRequest.lib.restype = AllocColorRequestCookie
        AllocColorRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint8 * 2)


class AllocColorRequestCType(ctypes.Structure):
    """xproto AllocColor"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("cmap", ctypes.c_uint32),
        ("red", ctypes.c_uint16),
        ("green", ctypes.c_uint16),
        ("blue", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 2),
    ]


AllocColorReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('red', FixedDataPacketField(MARKER_UINT16)),
    ('green', FixedDataPacketField(MARKER_UINT16)),
    ('blue', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(2)),
    ('pixel', FixedDataPacketField(MARKER_UINT32)),
))


class AllocColorReplyReply:
    __slots__ = ('red', 'green', 'blue', 'pixel',)

    def __init__(
            self, *,
            red: Optional[int] = None,
            green: Optional[int] = None,
            blue: Optional[int] = None,
            pixel: Optional[int] = None,
    ) -> None:
        self.red = red
        self.green = green
        self.blue = blue
        self.pixel = pixel

    def as_dict(self) -> Dict[str, Any]:
        return {
            'red': self.red,
            'green': self.green,
            'blue': self.blue,
            'pixel': self.pixel,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AllocColorReplyReply':
        return AllocColorReplyReply(**AllocColorReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AllocColorReplyReplyPacket.pack(**self.as_dict())


class AllocColorReplyReplyCType(ctypes.Structure):
    """xproto AllocColor_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("red", ctypes.c_uint16),
        ("green", ctypes.c_uint16),
        ("blue", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 2),
        ("pixel", ctypes.c_uint32),
    ]


AllocNamedColorRequestCookie = NewType('AllocNamedColorRequestCookie', ctypes.c_uint32)


AllocNamedColorRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('cmap', FixedDataPacketField(MARKER_UINT32)),
    ('name_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(2)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['name_len'], 0)),
))


class AllocNamedColorRequest:
    OPCODE = 85

    __slots__ = ('cmap', 'name_len', 'name',)

    def __init__(
            self, *,
            cmap: Optional[int] = None,
            name_len: Optional[int] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.cmap = cmap
        self.name_len = name_len
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cmap': self.cmap,
            'name_len': self.name_len,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AllocNamedColorRequest':
        return AllocNamedColorRequest(**AllocNamedColorRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AllocNamedColorRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], AllocNamedColorRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        AllocNamedColorRequest.lib = library.xproto_allocnamedcolor
        AllocNamedColorRequest.lib.restype = AllocNamedColorRequestCookie
        AllocNamedColorRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_void_p)


class AllocNamedColorRequestCType(ctypes.Structure):
    """xproto AllocNamedColor"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("cmap", ctypes.c_uint32),
        ("name_len", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


AllocNamedColorReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pixel', FixedDataPacketField(MARKER_UINT32)),
    ('exact_red', FixedDataPacketField(MARKER_UINT16)),
    ('exact_green', FixedDataPacketField(MARKER_UINT16)),
    ('exact_blue', FixedDataPacketField(MARKER_UINT16)),
    ('visual_red', FixedDataPacketField(MARKER_UINT16)),
    ('visual_green', FixedDataPacketField(MARKER_UINT16)),
    ('visual_blue', FixedDataPacketField(MARKER_UINT16)),
))


class AllocNamedColorReplyReply:
    __slots__ = ('pixel', 'exact_red', 'exact_green', 'exact_blue', 'visual_red', 'visual_green', 'visual_blue',)

    def __init__(
            self, *,
            pixel: Optional[int] = None,
            exact_red: Optional[int] = None,
            exact_green: Optional[int] = None,
            exact_blue: Optional[int] = None,
            visual_red: Optional[int] = None,
            visual_green: Optional[int] = None,
            visual_blue: Optional[int] = None,
    ) -> None:
        self.pixel = pixel
        self.exact_red = exact_red
        self.exact_green = exact_green
        self.exact_blue = exact_blue
        self.visual_red = visual_red
        self.visual_green = visual_green
        self.visual_blue = visual_blue

    def as_dict(self) -> Dict[str, Any]:
        return {
            'pixel': self.pixel,
            'exact_red': self.exact_red,
            'exact_green': self.exact_green,
            'exact_blue': self.exact_blue,
            'visual_red': self.visual_red,
            'visual_green': self.visual_green,
            'visual_blue': self.visual_blue,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AllocNamedColorReplyReply':
        return AllocNamedColorReplyReply(**AllocNamedColorReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AllocNamedColorReplyReplyPacket.pack(**self.as_dict())


class AllocNamedColorReplyReplyCType(ctypes.Structure):
    """xproto AllocNamedColor_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pixel", ctypes.c_uint32),
        ("exact_red", ctypes.c_uint16),
        ("exact_green", ctypes.c_uint16),
        ("exact_blue", ctypes.c_uint16),
        ("visual_red", ctypes.c_uint16),
        ("visual_green", ctypes.c_uint16),
        ("visual_blue", ctypes.c_uint16),
    ]


AllocColorCellsRequestCookie = NewType('AllocColorCellsRequestCookie', ctypes.c_uint32)


AllocColorCellsRequestPacket = DataPacket((
    ('contiguous', FixedDataPacketField(MARKER_UINT8)),
    ('cmap', FixedDataPacketField(MARKER_UINT32)),
    ('colors', FixedDataPacketField(MARKER_UINT16)),
    ('planes', FixedDataPacketField(MARKER_UINT16)),
))


class AllocColorCellsRequest:
    OPCODE = 86

    __slots__ = ('contiguous', 'cmap', 'colors', 'planes',)

    def __init__(
            self, *,
            contiguous: Optional[bool] = None,
            cmap: Optional[int] = None,
            colors: Optional[int] = None,
            planes: Optional[int] = None,
    ) -> None:
        self.contiguous = contiguous
        self.cmap = cmap
        self.colors = colors
        self.planes = planes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'contiguous': self.contiguous,
            'cmap': self.cmap,
            'colors': self.colors,
            'planes': self.planes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AllocColorCellsRequest':
        return AllocColorCellsRequest(**AllocColorCellsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AllocColorCellsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[bool, int, int, int], AllocColorCellsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        AllocColorCellsRequest.lib = library.xproto_alloccolorcells
        AllocColorCellsRequest.lib.restype = AllocColorCellsRequestCookie
        AllocColorCellsRequest.lib.argstype = (ctypes.c_int8, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16)


class AllocColorCellsRequestCType(ctypes.Structure):
    """xproto AllocColorCells"""
    _fields_ = [
        ("contiguous", ctypes.c_int8),
        ("cmap", ctypes.c_uint32),
        ("colors", ctypes.c_uint16),
        ("planes", ctypes.c_uint16),
    ]


AllocColorCellsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pixels_len', FixedDataPacketField(MARKER_UINT16)),
    ('masks_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(20)),
    ('pixels', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['pixels_len'], 0)),
    ('masks', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['masks_len'], 0)),
))


class AllocColorCellsReplyReply:
    __slots__ = ('pixels_len', 'masks_len', 'pixels', 'masks',)

    def __init__(
            self, *,
            pixels_len: Optional[int] = None,
            masks_len: Optional[int] = None,
            pixels: Optional[Sequence[int]] = None,
            masks: Optional[Sequence[int]] = None,
    ) -> None:
        self.pixels_len = pixels_len
        self.masks_len = masks_len
        self.pixels = pixels
        self.masks = masks

    def as_dict(self) -> Dict[str, Any]:
        return {
            'pixels_len': self.pixels_len,
            'masks_len': self.masks_len,
            'pixels': self.pixels,
            'masks': self.masks,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AllocColorCellsReplyReply':
        return AllocColorCellsReplyReply(**AllocColorCellsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AllocColorCellsReplyReplyPacket.pack(**self.as_dict())


class AllocColorCellsReplyReplyCType(ctypes.Structure):
    """xproto AllocColorCells_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pixels_len", ctypes.c_uint16),
        ("masks_len", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 20),
        ("var_data", ctypes.c_void_p),
    ]


AllocColorPlanesRequestCookie = NewType('AllocColorPlanesRequestCookie', ctypes.c_uint32)


AllocColorPlanesRequestPacket = DataPacket((
    ('contiguous', FixedDataPacketField(MARKER_UINT8)),
    ('cmap', FixedDataPacketField(MARKER_UINT32)),
    ('colors', FixedDataPacketField(MARKER_UINT16)),
    ('reds', FixedDataPacketField(MARKER_UINT16)),
    ('greens', FixedDataPacketField(MARKER_UINT16)),
    ('blues', FixedDataPacketField(MARKER_UINT16)),
))


class AllocColorPlanesRequest:
    OPCODE = 87

    __slots__ = ('contiguous', 'cmap', 'colors', 'reds', 'greens', 'blues',)

    def __init__(
            self, *,
            contiguous: Optional[bool] = None,
            cmap: Optional[int] = None,
            colors: Optional[int] = None,
            reds: Optional[int] = None,
            greens: Optional[int] = None,
            blues: Optional[int] = None,
    ) -> None:
        self.contiguous = contiguous
        self.cmap = cmap
        self.colors = colors
        self.reds = reds
        self.greens = greens
        self.blues = blues

    def as_dict(self) -> Dict[str, Any]:
        return {
            'contiguous': self.contiguous,
            'cmap': self.cmap,
            'colors': self.colors,
            'reds': self.reds,
            'greens': self.greens,
            'blues': self.blues,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AllocColorPlanesRequest':
        return AllocColorPlanesRequest(**AllocColorPlanesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AllocColorPlanesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[bool, int, int, int, int, int], AllocColorPlanesRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        AllocColorPlanesRequest.lib = library.xproto_alloccolorplanes
        AllocColorPlanesRequest.lib.restype = AllocColorPlanesRequestCookie
        AllocColorPlanesRequest.lib.argstype = (ctypes.c_int8, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16)


class AllocColorPlanesRequestCType(ctypes.Structure):
    """xproto AllocColorPlanes"""
    _fields_ = [
        ("contiguous", ctypes.c_int8),
        ("cmap", ctypes.c_uint32),
        ("colors", ctypes.c_uint16),
        ("reds", ctypes.c_uint16),
        ("greens", ctypes.c_uint16),
        ("blues", ctypes.c_uint16),
    ]


AllocColorPlanesReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('pixels_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(2)),
    ('red_mask', FixedDataPacketField(MARKER_UINT32)),
    ('green_mask', FixedDataPacketField(MARKER_UINT32)),
    ('blue_mask', FixedDataPacketField(MARKER_UINT32)),
    ('pad2', FixedPadDataPacketField(8)),
    ('pixels', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['pixels_len'], 0)),
))


class AllocColorPlanesReplyReply:
    __slots__ = ('pixels_len', 'red_mask', 'green_mask', 'blue_mask', 'pixels',)

    def __init__(
            self, *,
            pixels_len: Optional[int] = None,
            red_mask: Optional[int] = None,
            green_mask: Optional[int] = None,
            blue_mask: Optional[int] = None,
            pixels: Optional[Sequence[int]] = None,
    ) -> None:
        self.pixels_len = pixels_len
        self.red_mask = red_mask
        self.green_mask = green_mask
        self.blue_mask = blue_mask
        self.pixels = pixels

    def as_dict(self) -> Dict[str, Any]:
        return {
            'pixels_len': self.pixels_len,
            'red_mask': self.red_mask,
            'green_mask': self.green_mask,
            'blue_mask': self.blue_mask,
            'pixels': self.pixels,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'AllocColorPlanesReplyReply':
        return AllocColorPlanesReplyReply(**AllocColorPlanesReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return AllocColorPlanesReplyReplyPacket.pack(**self.as_dict())


class AllocColorPlanesReplyReplyCType(ctypes.Structure):
    """xproto AllocColorPlanes_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("pixels_len", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 2),
        ("red_mask", ctypes.c_uint32),
        ("green_mask", ctypes.c_uint32),
        ("blue_mask", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * 8),
        ("var_data", ctypes.c_void_p),
    ]


FreeColorsRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('cmap', FixedDataPacketField(MARKER_UINT32)),
    ('plane_mask', FixedDataPacketField(MARKER_UINT32)),
    ('pixels', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class FreeColorsRequest:
    OPCODE = 88

    __slots__ = ('cmap', 'plane_mask', 'pixels',)

    def __init__(
            self, *,
            cmap: Optional[int] = None,
            plane_mask: Optional[int] = None,
            pixels: Optional[Sequence[int]] = None,
    ) -> None:
        self.cmap = cmap
        self.plane_mask = plane_mask
        self.pixels = pixels

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cmap': self.cmap,
            'plane_mask': self.plane_mask,
            'pixels': self.pixels,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FreeColorsRequest':
        return FreeColorsRequest(**FreeColorsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FreeColorsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        FreeColorsRequest.lib = library.xproto_freecolors
        FreeColorsRequest.lib.restype = ctypes.c_uint32
        FreeColorsRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)


class FreeColorsRequestCType(ctypes.Structure):
    """xproto FreeColors"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("cmap", ctypes.c_uint32),
        ("plane_mask", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


ColoritemStructPacket = DataPacket((
    ('pixel', FixedDataPacketField(MARKER_UINT32)),
    ('red', FixedDataPacketField(MARKER_UINT16)),
    ('green', FixedDataPacketField(MARKER_UINT16)),
    ('blue', FixedDataPacketField(MARKER_UINT16)),
    ('flags', FixedDataPacketField(MARKER_INT8)),
    ('pad0', FixedPadDataPacketField(1)),
))


class ColoritemStruct:
    __slots__ = ('pixel', 'red', 'green', 'blue', 'flags',)

    def __init__(
            self, *,
            pixel: Optional[int] = None,
            red: Optional[int] = None,
            green: Optional[int] = None,
            blue: Optional[int] = None,
            flags: Optional[int] = None,
    ) -> None:
        self.pixel = pixel
        self.red = red
        self.green = green
        self.blue = blue
        self.flags = flags

    def as_dict(self) -> Dict[str, Any]:
        return {
            'pixel': self.pixel,
            'red': self.red,
            'green': self.green,
            'blue': self.blue,
            'flags': self.flags,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ColoritemStruct':
        return ColoritemStruct(**ColoritemStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ColoritemStructPacket.pack(**self.as_dict())


class ColoritemStructCType(ctypes.Structure):
    """xproto COLORITEM"""
    _fields_ = [
        ("pixel", ctypes.c_uint32),
        ("red", ctypes.c_uint16),
        ("green", ctypes.c_uint16),
        ("blue", ctypes.c_uint16),
        ("flags", ctypes.c_int8),
        ("pad0", ctypes.c_uint8),
    ]


StoreColorsRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('cmap', FixedDataPacketField(MARKER_UINT32)),
    ('items', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class StoreColorsRequest:
    OPCODE = 89

    __slots__ = ('cmap', 'items',)

    def __init__(
            self, *,
            cmap: Optional[int] = None,
            items: Optional[Sequence[int]] = None,
    ) -> None:
        self.cmap = cmap
        self.items = items

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cmap': self.cmap,
            'items': self.items,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'StoreColorsRequest':
        return StoreColorsRequest(**StoreColorsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return StoreColorsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        StoreColorsRequest.lib = library.xproto_storecolors
        StoreColorsRequest.lib.restype = ctypes.c_uint32
        StoreColorsRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_void_p)


class StoreColorsRequestCType(ctypes.Structure):
    """xproto StoreColors"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("cmap", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


StoreNamedColorRequestPacket = DataPacket((
    ('flags', FixedDataPacketField(MARKER_UINT8)),
    ('cmap', FixedDataPacketField(MARKER_UINT32)),
    ('pixel', FixedDataPacketField(MARKER_UINT32)),
    ('name_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['name_len'], 0)),
))


class StoreNamedColorRequest:
    OPCODE = 90

    __slots__ = ('flags', 'cmap', 'pixel', 'name_len', 'name',)

    def __init__(
            self, *,
            flags: Optional[int] = None,
            cmap: Optional[int] = None,
            pixel: Optional[int] = None,
            name_len: Optional[int] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.flags = flags
        self.cmap = cmap
        self.pixel = pixel
        self.name_len = name_len
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'flags': self.flags,
            'cmap': self.cmap,
            'pixel': self.pixel,
            'name_len': self.name_len,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'StoreNamedColorRequest':
        return StoreNamedColorRequest(**StoreNamedColorRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return StoreNamedColorRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        StoreNamedColorRequest.lib = library.xproto_storenamedcolor
        StoreNamedColorRequest.lib.restype = ctypes.c_uint32
        StoreNamedColorRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_void_p)


class StoreNamedColorRequestCType(ctypes.Structure):
    """xproto StoreNamedColor"""
    _fields_ = [
        ("flags", ctypes.c_uint8),
        ("cmap", ctypes.c_uint32),
        ("pixel", ctypes.c_uint32),
        ("name_len", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


RgbStructPacket = DataPacket((
    ('red', FixedDataPacketField(MARKER_UINT16)),
    ('green', FixedDataPacketField(MARKER_UINT16)),
    ('blue', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
))


class RgbStruct:
    __slots__ = ('red', 'green', 'blue',)

    def __init__(
            self, *,
            red: Optional[int] = None,
            green: Optional[int] = None,
            blue: Optional[int] = None,
    ) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    def as_dict(self) -> Dict[str, Any]:
        return {
            'red': self.red,
            'green': self.green,
            'blue': self.blue,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RgbStruct':
        return RgbStruct(**RgbStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RgbStructPacket.pack(**self.as_dict())


class RgbStructCType(ctypes.Structure):
    """xproto RGB"""
    _fields_ = [
        ("red", ctypes.c_uint16),
        ("green", ctypes.c_uint16),
        ("blue", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
    ]


QueryColorsRequestCookie = NewType('QueryColorsRequestCookie', ctypes.c_uint32)


QueryColorsRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('cmap', FixedDataPacketField(MARKER_UINT32)),
    ('pixels', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 1, 0)),
))


class QueryColorsRequest:
    OPCODE = 91

    __slots__ = ('cmap', 'pixels',)

    def __init__(
            self, *,
            cmap: Optional[int] = None,
            pixels: Optional[Sequence[int]] = None,
    ) -> None:
        self.cmap = cmap
        self.pixels = pixels

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cmap': self.cmap,
            'pixels': self.pixels,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryColorsRequest':
        return QueryColorsRequest(**QueryColorsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryColorsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Sequence[int]], QueryColorsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryColorsRequest.lib = library.xproto_querycolors
        QueryColorsRequest.lib.restype = QueryColorsRequestCookie
        QueryColorsRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_void_p)


class QueryColorsRequestCType(ctypes.Structure):
    """xproto QueryColors"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("cmap", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


QueryColorsReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('colors_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(22)),
    ('colors', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['colors_len'], 0)),
))


class QueryColorsReplyReply:
    __slots__ = ('colors_len', 'colors',)

    def __init__(
            self, *,
            colors_len: Optional[int] = None,
            colors: Optional[Sequence[int]] = None,
    ) -> None:
        self.colors_len = colors_len
        self.colors = colors

    def as_dict(self) -> Dict[str, Any]:
        return {
            'colors_len': self.colors_len,
            'colors': self.colors,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryColorsReplyReply':
        return QueryColorsReplyReply(**QueryColorsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryColorsReplyReplyPacket.pack(**self.as_dict())


class QueryColorsReplyReplyCType(ctypes.Structure):
    """xproto QueryColors_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("colors_len", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 22),
        ("var_data", ctypes.c_void_p),
    ]


LookupColorRequestCookie = NewType('LookupColorRequestCookie', ctypes.c_uint32)


LookupColorRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('cmap', FixedDataPacketField(MARKER_UINT32)),
    ('name_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(2)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['name_len'], 0)),
))


class LookupColorRequest:
    OPCODE = 92

    __slots__ = ('cmap', 'name_len', 'name',)

    def __init__(
            self, *,
            cmap: Optional[int] = None,
            name_len: Optional[int] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.cmap = cmap
        self.name_len = name_len
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cmap': self.cmap,
            'name_len': self.name_len,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'LookupColorRequest':
        return LookupColorRequest(**LookupColorRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return LookupColorRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, Sequence[int]], LookupColorRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        LookupColorRequest.lib = library.xproto_lookupcolor
        LookupColorRequest.lib.restype = LookupColorRequestCookie
        LookupColorRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_void_p)


class LookupColorRequestCType(ctypes.Structure):
    """xproto LookupColor"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("cmap", ctypes.c_uint32),
        ("name_len", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


LookupColorReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('exact_red', FixedDataPacketField(MARKER_UINT16)),
    ('exact_green', FixedDataPacketField(MARKER_UINT16)),
    ('exact_blue', FixedDataPacketField(MARKER_UINT16)),
    ('visual_red', FixedDataPacketField(MARKER_UINT16)),
    ('visual_green', FixedDataPacketField(MARKER_UINT16)),
    ('visual_blue', FixedDataPacketField(MARKER_UINT16)),
))


class LookupColorReplyReply:
    __slots__ = ('exact_red', 'exact_green', 'exact_blue', 'visual_red', 'visual_green', 'visual_blue',)

    def __init__(
            self, *,
            exact_red: Optional[int] = None,
            exact_green: Optional[int] = None,
            exact_blue: Optional[int] = None,
            visual_red: Optional[int] = None,
            visual_green: Optional[int] = None,
            visual_blue: Optional[int] = None,
    ) -> None:
        self.exact_red = exact_red
        self.exact_green = exact_green
        self.exact_blue = exact_blue
        self.visual_red = visual_red
        self.visual_green = visual_green
        self.visual_blue = visual_blue

    def as_dict(self) -> Dict[str, Any]:
        return {
            'exact_red': self.exact_red,
            'exact_green': self.exact_green,
            'exact_blue': self.exact_blue,
            'visual_red': self.visual_red,
            'visual_green': self.visual_green,
            'visual_blue': self.visual_blue,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'LookupColorReplyReply':
        return LookupColorReplyReply(**LookupColorReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return LookupColorReplyReplyPacket.pack(**self.as_dict())


class LookupColorReplyReplyCType(ctypes.Structure):
    """xproto LookupColor_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("exact_red", ctypes.c_uint16),
        ("exact_green", ctypes.c_uint16),
        ("exact_blue", ctypes.c_uint16),
        ("visual_red", ctypes.c_uint16),
        ("visual_green", ctypes.c_uint16),
        ("visual_blue", ctypes.c_uint16),
    ]


CreateCursorRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('cid', FixedDataPacketField(MARKER_UINT32)),
    ('source', FixedDataPacketField(MARKER_UINT32)),
    ('mask', FixedDataPacketField(MARKER_UINT32)),
    ('fore_red', FixedDataPacketField(MARKER_UINT16)),
    ('fore_green', FixedDataPacketField(MARKER_UINT16)),
    ('fore_blue', FixedDataPacketField(MARKER_UINT16)),
    ('back_red', FixedDataPacketField(MARKER_UINT16)),
    ('back_green', FixedDataPacketField(MARKER_UINT16)),
    ('back_blue', FixedDataPacketField(MARKER_UINT16)),
    ('x', FixedDataPacketField(MARKER_UINT16)),
    ('y', FixedDataPacketField(MARKER_UINT16)),
))


class CreateCursorRequest:
    OPCODE = 93

    __slots__ = ('cid', 'source', 'mask', 'fore_red', 'fore_green', 'fore_blue', 'back_red', 'back_green', 'back_blue', 'x', 'y',)

    def __init__(
            self, *,
            cid: Optional[int] = None,
            source: Optional[int] = None,
            mask: Optional[int] = None,
            fore_red: Optional[int] = None,
            fore_green: Optional[int] = None,
            fore_blue: Optional[int] = None,
            back_red: Optional[int] = None,
            back_green: Optional[int] = None,
            back_blue: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
    ) -> None:
        self.cid = cid
        self.source = source
        self.mask = mask
        self.fore_red = fore_red
        self.fore_green = fore_green
        self.fore_blue = fore_blue
        self.back_red = back_red
        self.back_green = back_green
        self.back_blue = back_blue
        self.x = x
        self.y = y

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cid': self.cid,
            'source': self.source,
            'mask': self.mask,
            'fore_red': self.fore_red,
            'fore_green': self.fore_green,
            'fore_blue': self.fore_blue,
            'back_red': self.back_red,
            'back_green': self.back_green,
            'back_blue': self.back_blue,
            'x': self.x,
            'y': self.y,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateCursorRequest':
        return CreateCursorRequest(**CreateCursorRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateCursorRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateCursorRequest.lib = library.xproto_createcursor
        CreateCursorRequest.lib.restype = ctypes.c_uint32
        CreateCursorRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16)


class CreateCursorRequestCType(ctypes.Structure):
    """xproto CreateCursor"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("cid", ctypes.c_uint32),
        ("source", ctypes.c_uint32),
        ("mask", ctypes.c_uint32),
        ("fore_red", ctypes.c_uint16),
        ("fore_green", ctypes.c_uint16),
        ("fore_blue", ctypes.c_uint16),
        ("back_red", ctypes.c_uint16),
        ("back_green", ctypes.c_uint16),
        ("back_blue", ctypes.c_uint16),
        ("x", ctypes.c_uint16),
        ("y", ctypes.c_uint16),
    ]


CreateGlyphCursorRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('cid', FixedDataPacketField(MARKER_UINT32)),
    ('source_font', FixedDataPacketField(MARKER_UINT32)),
    ('mask_font', FixedDataPacketField(MARKER_UINT32)),
    ('source_char', FixedDataPacketField(MARKER_UINT16)),
    ('mask_char', FixedDataPacketField(MARKER_UINT16)),
    ('fore_red', FixedDataPacketField(MARKER_UINT16)),
    ('fore_green', FixedDataPacketField(MARKER_UINT16)),
    ('fore_blue', FixedDataPacketField(MARKER_UINT16)),
    ('back_red', FixedDataPacketField(MARKER_UINT16)),
    ('back_green', FixedDataPacketField(MARKER_UINT16)),
    ('back_blue', FixedDataPacketField(MARKER_UINT16)),
))


class CreateGlyphCursorRequest:
    OPCODE = 94

    __slots__ = ('cid', 'source_font', 'mask_font', 'source_char', 'mask_char', 'fore_red', 'fore_green', 'fore_blue', 'back_red', 'back_green', 'back_blue',)

    def __init__(
            self, *,
            cid: Optional[int] = None,
            source_font: Optional[int] = None,
            mask_font: Optional[int] = None,
            source_char: Optional[int] = None,
            mask_char: Optional[int] = None,
            fore_red: Optional[int] = None,
            fore_green: Optional[int] = None,
            fore_blue: Optional[int] = None,
            back_red: Optional[int] = None,
            back_green: Optional[int] = None,
            back_blue: Optional[int] = None,
    ) -> None:
        self.cid = cid
        self.source_font = source_font
        self.mask_font = mask_font
        self.source_char = source_char
        self.mask_char = mask_char
        self.fore_red = fore_red
        self.fore_green = fore_green
        self.fore_blue = fore_blue
        self.back_red = back_red
        self.back_green = back_green
        self.back_blue = back_blue

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cid': self.cid,
            'source_font': self.source_font,
            'mask_font': self.mask_font,
            'source_char': self.source_char,
            'mask_char': self.mask_char,
            'fore_red': self.fore_red,
            'fore_green': self.fore_green,
            'fore_blue': self.fore_blue,
            'back_red': self.back_red,
            'back_green': self.back_green,
            'back_blue': self.back_blue,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'CreateGlyphCursorRequest':
        return CreateGlyphCursorRequest(**CreateGlyphCursorRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return CreateGlyphCursorRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        CreateGlyphCursorRequest.lib = library.xproto_createglyphcursor
        CreateGlyphCursorRequest.lib.restype = ctypes.c_uint32
        CreateGlyphCursorRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16)


class CreateGlyphCursorRequestCType(ctypes.Structure):
    """xproto CreateGlyphCursor"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("cid", ctypes.c_uint32),
        ("source_font", ctypes.c_uint32),
        ("mask_font", ctypes.c_uint32),
        ("source_char", ctypes.c_uint16),
        ("mask_char", ctypes.c_uint16),
        ("fore_red", ctypes.c_uint16),
        ("fore_green", ctypes.c_uint16),
        ("fore_blue", ctypes.c_uint16),
        ("back_red", ctypes.c_uint16),
        ("back_green", ctypes.c_uint16),
        ("back_blue", ctypes.c_uint16),
    ]


FreeCursorRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('cursor', FixedDataPacketField(MARKER_UINT32)),
))


class FreeCursorRequest:
    OPCODE = 95

    __slots__ = ('cursor',)

    def __init__(
            self, *,
            cursor: Optional[int] = None,
    ) -> None:
        self.cursor = cursor

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cursor': self.cursor,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'FreeCursorRequest':
        return FreeCursorRequest(**FreeCursorRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return FreeCursorRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        FreeCursorRequest.lib = library.xproto_freecursor
        FreeCursorRequest.lib.restype = ctypes.c_uint32
        FreeCursorRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class FreeCursorRequestCType(ctypes.Structure):
    """xproto FreeCursor"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("cursor", ctypes.c_uint32),
    ]


RecolorCursorRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('cursor', FixedDataPacketField(MARKER_UINT32)),
    ('fore_red', FixedDataPacketField(MARKER_UINT16)),
    ('fore_green', FixedDataPacketField(MARKER_UINT16)),
    ('fore_blue', FixedDataPacketField(MARKER_UINT16)),
    ('back_red', FixedDataPacketField(MARKER_UINT16)),
    ('back_green', FixedDataPacketField(MARKER_UINT16)),
    ('back_blue', FixedDataPacketField(MARKER_UINT16)),
))


class RecolorCursorRequest:
    OPCODE = 96

    __slots__ = ('cursor', 'fore_red', 'fore_green', 'fore_blue', 'back_red', 'back_green', 'back_blue',)

    def __init__(
            self, *,
            cursor: Optional[int] = None,
            fore_red: Optional[int] = None,
            fore_green: Optional[int] = None,
            fore_blue: Optional[int] = None,
            back_red: Optional[int] = None,
            back_green: Optional[int] = None,
            back_blue: Optional[int] = None,
    ) -> None:
        self.cursor = cursor
        self.fore_red = fore_red
        self.fore_green = fore_green
        self.fore_blue = fore_blue
        self.back_red = back_red
        self.back_green = back_green
        self.back_blue = back_blue

    def as_dict(self) -> Dict[str, Any]:
        return {
            'cursor': self.cursor,
            'fore_red': self.fore_red,
            'fore_green': self.fore_green,
            'fore_blue': self.fore_blue,
            'back_red': self.back_red,
            'back_green': self.back_green,
            'back_blue': self.back_blue,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RecolorCursorRequest':
        return RecolorCursorRequest(**RecolorCursorRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RecolorCursorRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        RecolorCursorRequest.lib = library.xproto_recolorcursor
        RecolorCursorRequest.lib.restype = ctypes.c_uint32
        RecolorCursorRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16, ctypes.c_uint16)


class RecolorCursorRequestCType(ctypes.Structure):
    """xproto RecolorCursor"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("cursor", ctypes.c_uint32),
        ("fore_red", ctypes.c_uint16),
        ("fore_green", ctypes.c_uint16),
        ("fore_blue", ctypes.c_uint16),
        ("back_red", ctypes.c_uint16),
        ("back_green", ctypes.c_uint16),
        ("back_blue", ctypes.c_uint16),
    ]


QueryBestSizeRequestCookie = NewType('QueryBestSizeRequestCookie', ctypes.c_uint32)


QueryBestSizeRequestPacket = DataPacket((
    ('class', FixedDataPacketField(MARKER_UINT8)),
    ('drawable', FixedDataPacketField(MARKER_UINT32)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
))


class QueryBestSizeRequest:
    OPCODE = 97

    __slots__ = ('v_class', 'drawable', 'width', 'height',)

    def __init__(
            self, *,
            v_class: Optional[int] = None,
            drawable: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
    ) -> None:
        self.v_class = v_class
        self.drawable = drawable
        self.width = width
        self.height = height

    def as_dict(self) -> Dict[str, Any]:
        return {
            'class': self.v_class,
            'drawable': self.drawable,
            'width': self.width,
            'height': self.height,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryBestSizeRequest':
        return QueryBestSizeRequest(**QueryBestSizeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryBestSizeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], QueryBestSizeRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryBestSizeRequest.lib = library.xproto_querybestsize
        QueryBestSizeRequest.lib.restype = QueryBestSizeRequestCookie
        QueryBestSizeRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_uint16)


class QueryBestSizeRequestCType(ctypes.Structure):
    """xproto QueryBestSize"""
    _fields_ = [
        ("class", ctypes.c_uint8),
        ("drawable", ctypes.c_uint32),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
    ]


QueryBestSizeReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('width', FixedDataPacketField(MARKER_UINT16)),
    ('height', FixedDataPacketField(MARKER_UINT16)),
))


class QueryBestSizeReplyReply:
    __slots__ = ('width', 'height',)

    def __init__(
            self, *,
            width: Optional[int] = None,
            height: Optional[int] = None,
    ) -> None:
        self.width = width
        self.height = height

    def as_dict(self) -> Dict[str, Any]:
        return {
            'width': self.width,
            'height': self.height,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryBestSizeReplyReply':
        return QueryBestSizeReplyReply(**QueryBestSizeReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryBestSizeReplyReplyPacket.pack(**self.as_dict())


class QueryBestSizeReplyReplyCType(ctypes.Structure):
    """xproto QueryBestSize_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
    ]


QueryExtensionRequestCookie = NewType('QueryExtensionRequestCookie', ctypes.c_uint32)


QueryExtensionRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('name_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(2)),
    ('name', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['name_len'], 0)),
))


class QueryExtensionRequest:
    OPCODE = 98

    __slots__ = ('name_len', 'name',)

    def __init__(
            self, *,
            name_len: Optional[int] = None,
            name: Optional[Sequence[int]] = None,
    ) -> None:
        self.name_len = name_len
        self.name = name

    def as_dict(self) -> Dict[str, Any]:
        return {
            'name_len': self.name_len,
            'name': self.name,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryExtensionRequest':
        return QueryExtensionRequest(**QueryExtensionRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryExtensionRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Sequence[int]], QueryExtensionRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        QueryExtensionRequest.lib = library.xproto_queryextension
        QueryExtensionRequest.lib.restype = QueryExtensionRequestCookie
        QueryExtensionRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint16, ctypes.c_uint8 * 2, ctypes.c_void_p)


class QueryExtensionRequestCType(ctypes.Structure):
    """xproto QueryExtension"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("name_len", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


QueryExtensionReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('present', FixedDataPacketField(MARKER_UINT8)),
    ('major_opcode', FixedDataPacketField(MARKER_UINT8)),
    ('first_event', FixedDataPacketField(MARKER_UINT8)),
    ('first_error', FixedDataPacketField(MARKER_UINT8)),
))


class QueryExtensionReplyReply:
    __slots__ = ('present', 'major_opcode', 'first_event', 'first_error',)

    def __init__(
            self, *,
            present: Optional[bool] = None,
            major_opcode: Optional[int] = None,
            first_event: Optional[int] = None,
            first_error: Optional[int] = None,
    ) -> None:
        self.present = present
        self.major_opcode = major_opcode
        self.first_event = first_event
        self.first_error = first_error

    def as_dict(self) -> Dict[str, Any]:
        return {
            'present': self.present,
            'major_opcode': self.major_opcode,
            'first_event': self.first_event,
            'first_error': self.first_error,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'QueryExtensionReplyReply':
        return QueryExtensionReplyReply(**QueryExtensionReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return QueryExtensionReplyReplyPacket.pack(**self.as_dict())


class QueryExtensionReplyReplyCType(ctypes.Structure):
    """xproto QueryExtension_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("present", ctypes.c_int8),
        ("major_opcode", ctypes.c_uint8),
        ("first_event", ctypes.c_uint8),
        ("first_error", ctypes.c_uint8),
    ]


ListExtensionsRequestCookie = NewType('ListExtensionsRequestCookie', ctypes.c_uint32)


ListExtensionsRequestPacket = DataPacket((
))


class ListExtensionsRequest:
    OPCODE = 99

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListExtensionsRequest':
        return ListExtensionsRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], ListExtensionsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ListExtensionsRequest.lib = library.xproto_listextensions
        ListExtensionsRequest.lib.restype = ListExtensionsRequestCookie
        ListExtensionsRequest.lib.argstype = ()


class ListExtensionsRequestCType(ctypes.Structure):
    """xproto ListExtensions"""
    _fields_ = [
    ]


ListExtensionsReplyReplyPacket = DataPacket((
    ('names_len', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(24)),
    ('names', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['names_len'], 0)),
))


class ListExtensionsReplyReply:
    __slots__ = ('names_len', 'names',)

    def __init__(
            self, *,
            names_len: Optional[int] = None,
            names: Optional[Sequence[int]] = None,
    ) -> None:
        self.names_len = names_len
        self.names = names

    def as_dict(self) -> Dict[str, Any]:
        return {
            'names_len': self.names_len,
            'names': self.names,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListExtensionsReplyReply':
        return ListExtensionsReplyReply(**ListExtensionsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListExtensionsReplyReplyPacket.pack(**self.as_dict())


class ListExtensionsReplyReplyCType(ctypes.Structure):
    """xproto ListExtensions_reply"""
    _fields_ = [
        ("names_len", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 24),
        ("var_data", ctypes.c_void_p),
    ]


ChangeKeyboardMappingRequestPacket = DataPacket((
    ('keycode_count', FixedDataPacketField(MARKER_UINT8)),
    ('first_keycode', FixedDataPacketField(MARKER_UINT32)),
    ('keysyms_per_keycode', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(2)),
    ('keysyms', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: (d['keycode_count']) * (d['keysyms_per_keycode']), 0)),
))


class ChangeKeyboardMappingRequest:
    OPCODE = 100

    __slots__ = ('keycode_count', 'first_keycode', 'keysyms_per_keycode', 'keysyms',)

    def __init__(
            self, *,
            keycode_count: Optional[int] = None,
            first_keycode: Optional[int] = None,
            keysyms_per_keycode: Optional[int] = None,
            keysyms: Optional[Sequence[int]] = None,
    ) -> None:
        self.keycode_count = keycode_count
        self.first_keycode = first_keycode
        self.keysyms_per_keycode = keysyms_per_keycode
        self.keysyms = keysyms

    def as_dict(self) -> Dict[str, Any]:
        return {
            'keycode_count': self.keycode_count,
            'first_keycode': self.first_keycode,
            'keysyms_per_keycode': self.keysyms_per_keycode,
            'keysyms': self.keysyms,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeKeyboardMappingRequest':
        return ChangeKeyboardMappingRequest(**ChangeKeyboardMappingRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeKeyboardMappingRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangeKeyboardMappingRequest.lib = library.xproto_changekeyboardmapping
        ChangeKeyboardMappingRequest.lib.restype = ctypes.c_uint32
        ChangeKeyboardMappingRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint8 * 2, ctypes.c_void_p)


class ChangeKeyboardMappingRequestCType(ctypes.Structure):
    """xproto ChangeKeyboardMapping"""
    _fields_ = [
        ("keycode_count", ctypes.c_uint8),
        ("first_keycode", ctypes.c_uint32),
        ("keysyms_per_keycode", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


GetKeyboardMappingRequestCookie = NewType('GetKeyboardMappingRequestCookie', ctypes.c_uint32)


GetKeyboardMappingRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('first_keycode', FixedDataPacketField(MARKER_UINT32)),
    ('count', FixedDataPacketField(MARKER_UINT8)),
))


class GetKeyboardMappingRequest:
    OPCODE = 101

    __slots__ = ('first_keycode', 'count',)

    def __init__(
            self, *,
            first_keycode: Optional[int] = None,
            count: Optional[int] = None,
    ) -> None:
        self.first_keycode = first_keycode
        self.count = count

    def as_dict(self) -> Dict[str, Any]:
        return {
            'first_keycode': self.first_keycode,
            'count': self.count,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetKeyboardMappingRequest':
        return GetKeyboardMappingRequest(**GetKeyboardMappingRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetKeyboardMappingRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int], GetKeyboardMappingRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetKeyboardMappingRequest.lib = library.xproto_getkeyboardmapping
        GetKeyboardMappingRequest.lib.restype = GetKeyboardMappingRequestCookie
        GetKeyboardMappingRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint8)


class GetKeyboardMappingRequestCType(ctypes.Structure):
    """xproto GetKeyboardMapping"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("first_keycode", ctypes.c_uint32),
        ("count", ctypes.c_uint8),
    ]


GetKeyboardMappingReplyReplyPacket = DataPacket((
    ('keysyms_per_keycode', FixedDataPacketField(MARKER_INT8)),
    ('pad0', FixedPadDataPacketField(24)),
    ('keysyms', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['length'], 0)),
))


class GetKeyboardMappingReplyReply:
    __slots__ = ('keysyms_per_keycode', 'keysyms',)

    def __init__(
            self, *,
            keysyms_per_keycode: Optional[int] = None,
            keysyms: Optional[Sequence[int]] = None,
    ) -> None:
        self.keysyms_per_keycode = keysyms_per_keycode
        self.keysyms = keysyms

    def as_dict(self) -> Dict[str, Any]:
        return {
            'keysyms_per_keycode': self.keysyms_per_keycode,
            'keysyms': self.keysyms,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetKeyboardMappingReplyReply':
        return GetKeyboardMappingReplyReply(**GetKeyboardMappingReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetKeyboardMappingReplyReplyPacket.pack(**self.as_dict())


class GetKeyboardMappingReplyReplyCType(ctypes.Structure):
    """xproto GetKeyboardMapping_reply"""
    _fields_ = [
        ("keysyms_per_keycode", ctypes.c_int8),
        ("pad0", ctypes.c_uint8 * 24),
        ("var_data", ctypes.c_void_p),
    ]


ChangeKeyboardControlRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('value_mask', FixedDataPacketField(MARKER_UINT32)),
    ('value_list', BitDataPacketField(lambda d, c: d['value_mask'], {
        KbValues.KEY_CLICK_PERCENT: FixedDataPacketField(MARKER_INT32),
        KbValues.BELL_PERCENT: FixedDataPacketField(MARKER_INT32),
        KbValues.BELL_PITCH: FixedDataPacketField(MARKER_INT32),
        KbValues.BELL_DURATION: FixedDataPacketField(MARKER_INT32),
        KbValues.LED: FixedDataPacketField(MARKER_UINT32),
        KbValues.LED_MODE: FixedDataPacketField(MARKER_UINT32),
        KbValues.KEY: FixedDataPacketField(MARKER_UINT32),
        KbValues.AUTO_REPEAT_MODE: FixedDataPacketField(MARKER_UINT32),
    }, 0)),
))


class ChangeKeyboardControlRequest:
    OPCODE = 102

    __slots__ = ('value_mask', 'value_list',)

    def __init__(
            self, *,
            value_mask: Optional[int] = None,
            value_list: Optional[Mapping[str, KbValues]] = None,
    ) -> None:
        self.value_mask = value_mask
        self.value_list = value_list

    def as_dict(self) -> Dict[str, Any]:
        return {
            'value_mask': self.value_mask,
            'value_list': self.value_list,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeKeyboardControlRequest':
        return ChangeKeyboardControlRequest(**ChangeKeyboardControlRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeKeyboardControlRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Mapping[str, KbValues]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangeKeyboardControlRequest.lib = library.xproto_changekeyboardcontrol
        ChangeKeyboardControlRequest.lib.restype = ctypes.c_uint32
        ChangeKeyboardControlRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_void_p)


class ChangeKeyboardControlRequestCType(ctypes.Structure):
    """xproto ChangeKeyboardControl"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("value_mask", ctypes.c_uint32),
        ("var_data", ctypes.c_void_p),
    ]


GetKeyboardControlRequestCookie = NewType('GetKeyboardControlRequestCookie', ctypes.c_uint32)


GetKeyboardControlRequestPacket = DataPacket((
))


class GetKeyboardControlRequest:
    OPCODE = 103

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetKeyboardControlRequest':
        return GetKeyboardControlRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], GetKeyboardControlRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetKeyboardControlRequest.lib = library.xproto_getkeyboardcontrol
        GetKeyboardControlRequest.lib.restype = GetKeyboardControlRequestCookie
        GetKeyboardControlRequest.lib.argstype = ()


class GetKeyboardControlRequestCType(ctypes.Structure):
    """xproto GetKeyboardControl"""
    _fields_ = [
    ]


GetKeyboardControlReplyReplyPacket = DataPacket((
    ('global_auto_repeat', FixedDataPacketField(MARKER_INT8)),
    ('led_mask', FixedDataPacketField(MARKER_UINT32)),
    ('key_click_percent', FixedDataPacketField(MARKER_UINT8)),
    ('bell_percent', FixedDataPacketField(MARKER_UINT8)),
    ('bell_pitch', FixedDataPacketField(MARKER_UINT16)),
    ('bell_duration', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(2)),
    ('auto_repeats', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 32, 0)),
))


class GetKeyboardControlReplyReply:
    __slots__ = ('global_auto_repeat', 'led_mask', 'key_click_percent', 'bell_percent', 'bell_pitch', 'bell_duration', 'auto_repeats',)

    def __init__(
            self, *,
            global_auto_repeat: Optional[int] = None,
            led_mask: Optional[int] = None,
            key_click_percent: Optional[int] = None,
            bell_percent: Optional[int] = None,
            bell_pitch: Optional[int] = None,
            bell_duration: Optional[int] = None,
            auto_repeats: Optional[Sequence[int]] = None,
    ) -> None:
        self.global_auto_repeat = global_auto_repeat
        self.led_mask = led_mask
        self.key_click_percent = key_click_percent
        self.bell_percent = bell_percent
        self.bell_pitch = bell_pitch
        self.bell_duration = bell_duration
        self.auto_repeats = auto_repeats

    def as_dict(self) -> Dict[str, Any]:
        return {
            'global_auto_repeat': self.global_auto_repeat,
            'led_mask': self.led_mask,
            'key_click_percent': self.key_click_percent,
            'bell_percent': self.bell_percent,
            'bell_pitch': self.bell_pitch,
            'bell_duration': self.bell_duration,
            'auto_repeats': self.auto_repeats,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetKeyboardControlReplyReply':
        return GetKeyboardControlReplyReply(**GetKeyboardControlReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetKeyboardControlReplyReplyPacket.pack(**self.as_dict())


class GetKeyboardControlReplyReplyCType(ctypes.Structure):
    """xproto GetKeyboardControl_reply"""
    _fields_ = [
        ("global_auto_repeat", ctypes.c_int8),
        ("led_mask", ctypes.c_uint32),
        ("key_click_percent", ctypes.c_uint8),
        ("bell_percent", ctypes.c_uint8),
        ("bell_pitch", ctypes.c_uint16),
        ("bell_duration", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 2),
        ("var_data", ctypes.c_void_p),
    ]


BellRequestPacket = DataPacket((
    ('percent', FixedDataPacketField(MARKER_INT8)),
))


class BellRequest:
    OPCODE = 104

    __slots__ = ('percent',)

    def __init__(
            self, *,
            percent: Optional[int] = None,
    ) -> None:
        self.percent = percent

    def as_dict(self) -> Dict[str, Any]:
        return {
            'percent': self.percent,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'BellRequest':
        return BellRequest(**BellRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return BellRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        BellRequest.lib = library.xproto_bell
        BellRequest.lib.restype = ctypes.c_uint32
        BellRequest.lib.argstype = (ctypes.c_int8,)


class BellRequestCType(ctypes.Structure):
    """xproto Bell"""
    _fields_ = [
        ("percent", ctypes.c_int8),
    ]


ChangePointerControlRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('acceleration_numerator', FixedDataPacketField(MARKER_INT16)),
    ('acceleration_denominator', FixedDataPacketField(MARKER_INT16)),
    ('threshold', FixedDataPacketField(MARKER_INT16)),
    ('do_acceleration', FixedDataPacketField(MARKER_UINT8)),
    ('do_threshold', FixedDataPacketField(MARKER_UINT8)),
))


class ChangePointerControlRequest:
    OPCODE = 105

    __slots__ = ('acceleration_numerator', 'acceleration_denominator', 'threshold', 'do_acceleration', 'do_threshold',)

    def __init__(
            self, *,
            acceleration_numerator: Optional[int] = None,
            acceleration_denominator: Optional[int] = None,
            threshold: Optional[int] = None,
            do_acceleration: Optional[bool] = None,
            do_threshold: Optional[bool] = None,
    ) -> None:
        self.acceleration_numerator = acceleration_numerator
        self.acceleration_denominator = acceleration_denominator
        self.threshold = threshold
        self.do_acceleration = do_acceleration
        self.do_threshold = do_threshold

    def as_dict(self) -> Dict[str, Any]:
        return {
            'acceleration_numerator': self.acceleration_numerator,
            'acceleration_denominator': self.acceleration_denominator,
            'threshold': self.threshold,
            'do_acceleration': self.do_acceleration,
            'do_threshold': self.do_threshold,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangePointerControlRequest':
        return ChangePointerControlRequest(**ChangePointerControlRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangePointerControlRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, bool, bool], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangePointerControlRequest.lib = library.xproto_changepointercontrol
        ChangePointerControlRequest.lib.restype = ctypes.c_uint32
        ChangePointerControlRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_int16, ctypes.c_int16, ctypes.c_int16, ctypes.c_int8, ctypes.c_int8)


class ChangePointerControlRequestCType(ctypes.Structure):
    """xproto ChangePointerControl"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("acceleration_numerator", ctypes.c_int16),
        ("acceleration_denominator", ctypes.c_int16),
        ("threshold", ctypes.c_int16),
        ("do_acceleration", ctypes.c_int8),
        ("do_threshold", ctypes.c_int8),
    ]


GetPointerControlRequestCookie = NewType('GetPointerControlRequestCookie', ctypes.c_uint32)


GetPointerControlRequestPacket = DataPacket((
))


class GetPointerControlRequest:
    OPCODE = 106

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPointerControlRequest':
        return GetPointerControlRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], GetPointerControlRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetPointerControlRequest.lib = library.xproto_getpointercontrol
        GetPointerControlRequest.lib.restype = GetPointerControlRequestCookie
        GetPointerControlRequest.lib.argstype = ()


class GetPointerControlRequestCType(ctypes.Structure):
    """xproto GetPointerControl"""
    _fields_ = [
    ]


GetPointerControlReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('acceleration_numerator', FixedDataPacketField(MARKER_UINT16)),
    ('acceleration_denominator', FixedDataPacketField(MARKER_UINT16)),
    ('threshold', FixedDataPacketField(MARKER_UINT16)),
    ('pad1', FixedPadDataPacketField(18)),
))


class GetPointerControlReplyReply:
    __slots__ = ('acceleration_numerator', 'acceleration_denominator', 'threshold',)

    def __init__(
            self, *,
            acceleration_numerator: Optional[int] = None,
            acceleration_denominator: Optional[int] = None,
            threshold: Optional[int] = None,
    ) -> None:
        self.acceleration_numerator = acceleration_numerator
        self.acceleration_denominator = acceleration_denominator
        self.threshold = threshold

    def as_dict(self) -> Dict[str, Any]:
        return {
            'acceleration_numerator': self.acceleration_numerator,
            'acceleration_denominator': self.acceleration_denominator,
            'threshold': self.threshold,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPointerControlReplyReply':
        return GetPointerControlReplyReply(**GetPointerControlReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPointerControlReplyReplyPacket.pack(**self.as_dict())


class GetPointerControlReplyReplyCType(ctypes.Structure):
    """xproto GetPointerControl_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("acceleration_numerator", ctypes.c_uint16),
        ("acceleration_denominator", ctypes.c_uint16),
        ("threshold", ctypes.c_uint16),
        ("pad1", ctypes.c_uint8 * 18),
    ]


SetScreenSaverRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('timeout', FixedDataPacketField(MARKER_INT16)),
    ('interval', FixedDataPacketField(MARKER_INT16)),
    ('prefer_blanking', FixedDataPacketField(MARKER_UINT8)),
    ('allow_exposures', FixedDataPacketField(MARKER_UINT8)),
))


class SetScreenSaverRequest:
    OPCODE = 107

    __slots__ = ('timeout', 'interval', 'prefer_blanking', 'allow_exposures',)

    def __init__(
            self, *,
            timeout: Optional[int] = None,
            interval: Optional[int] = None,
            prefer_blanking: Optional[int] = None,
            allow_exposures: Optional[int] = None,
    ) -> None:
        self.timeout = timeout
        self.interval = interval
        self.prefer_blanking = prefer_blanking
        self.allow_exposures = allow_exposures

    def as_dict(self) -> Dict[str, Any]:
        return {
            'timeout': self.timeout,
            'interval': self.interval,
            'prefer_blanking': self.prefer_blanking,
            'allow_exposures': self.allow_exposures,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetScreenSaverRequest':
        return SetScreenSaverRequest(**SetScreenSaverRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetScreenSaverRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetScreenSaverRequest.lib = library.xproto_setscreensaver
        SetScreenSaverRequest.lib.restype = ctypes.c_uint32
        SetScreenSaverRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_int16, ctypes.c_int16, ctypes.c_uint8, ctypes.c_uint8)


class SetScreenSaverRequestCType(ctypes.Structure):
    """xproto SetScreenSaver"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("timeout", ctypes.c_int16),
        ("interval", ctypes.c_int16),
        ("prefer_blanking", ctypes.c_uint8),
        ("allow_exposures", ctypes.c_uint8),
    ]


GetScreenSaverRequestCookie = NewType('GetScreenSaverRequestCookie', ctypes.c_uint32)


GetScreenSaverRequestPacket = DataPacket((
))


class GetScreenSaverRequest:
    OPCODE = 108

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetScreenSaverRequest':
        return GetScreenSaverRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], GetScreenSaverRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetScreenSaverRequest.lib = library.xproto_getscreensaver
        GetScreenSaverRequest.lib.restype = GetScreenSaverRequestCookie
        GetScreenSaverRequest.lib.argstype = ()


class GetScreenSaverRequestCType(ctypes.Structure):
    """xproto GetScreenSaver"""
    _fields_ = [
    ]


GetScreenSaverReplyReplyPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('timeout', FixedDataPacketField(MARKER_UINT16)),
    ('interval', FixedDataPacketField(MARKER_UINT16)),
    ('prefer_blanking', FixedDataPacketField(MARKER_INT8)),
    ('allow_exposures', FixedDataPacketField(MARKER_INT8)),
    ('pad1', FixedPadDataPacketField(18)),
))


class GetScreenSaverReplyReply:
    __slots__ = ('timeout', 'interval', 'prefer_blanking', 'allow_exposures',)

    def __init__(
            self, *,
            timeout: Optional[int] = None,
            interval: Optional[int] = None,
            prefer_blanking: Optional[int] = None,
            allow_exposures: Optional[int] = None,
    ) -> None:
        self.timeout = timeout
        self.interval = interval
        self.prefer_blanking = prefer_blanking
        self.allow_exposures = allow_exposures

    def as_dict(self) -> Dict[str, Any]:
        return {
            'timeout': self.timeout,
            'interval': self.interval,
            'prefer_blanking': self.prefer_blanking,
            'allow_exposures': self.allow_exposures,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetScreenSaverReplyReply':
        return GetScreenSaverReplyReply(**GetScreenSaverReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetScreenSaverReplyReplyPacket.pack(**self.as_dict())


class GetScreenSaverReplyReplyCType(ctypes.Structure):
    """xproto GetScreenSaver_reply"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("timeout", ctypes.c_uint16),
        ("interval", ctypes.c_uint16),
        ("prefer_blanking", ctypes.c_int8),
        ("allow_exposures", ctypes.c_int8),
        ("pad1", ctypes.c_uint8 * 18),
    ]


ChangeHostsRequestPacket = DataPacket((
    ('mode', FixedDataPacketField(MARKER_UINT8)),
    ('family', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('address_len', FixedDataPacketField(MARKER_UINT16)),
    ('address', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['address_len'], 0)),
))


class ChangeHostsRequest:
    OPCODE = 109

    __slots__ = ('mode', 'family', 'address_len', 'address',)

    def __init__(
            self, *,
            mode: Optional[int] = None,
            family: Optional[int] = None,
            address_len: Optional[int] = None,
            address: Optional[Sequence[int]] = None,
    ) -> None:
        self.mode = mode
        self.family = family
        self.address_len = address_len
        self.address = address

    def as_dict(self) -> Dict[str, Any]:
        return {
            'mode': self.mode,
            'family': self.family,
            'address_len': self.address_len,
            'address': self.address,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ChangeHostsRequest':
        return ChangeHostsRequest(**ChangeHostsRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ChangeHostsRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ChangeHostsRequest.lib = library.xproto_changehosts
        ChangeHostsRequest.lib.restype = ctypes.c_uint32
        ChangeHostsRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint16, ctypes.c_void_p)


class ChangeHostsRequestCType(ctypes.Structure):
    """xproto ChangeHosts"""
    _fields_ = [
        ("mode", ctypes.c_uint8),
        ("family", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("address_len", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


HostStructPacket = DataPacket((
    ('family', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(1)),
    ('address_len', FixedDataPacketField(MARKER_UINT16)),
    ('address', SimpleListDataPacketField(MARKER_INT8, lambda d, c: d['address_len'], 0)),
    ('pad1', AlignedPadDataPacketField(4)),
))


class HostStruct:
    __slots__ = ('family', 'address_len', 'address',)

    def __init__(
            self, *,
            family: Optional[int] = None,
            address_len: Optional[int] = None,
            address: Optional[Sequence[int]] = None,
    ) -> None:
        self.family = family
        self.address_len = address_len
        self.address = address

    def as_dict(self) -> Dict[str, Any]:
        return {
            'family': self.family,
            'address_len': self.address_len,
            'address': self.address,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'HostStruct':
        return HostStruct(**HostStructPacket.unpack(inp))

    def to_data(self) -> bytes:
        return HostStructPacket.pack(**self.as_dict())


class HostStructCType(ctypes.Structure):
    """xproto HOST"""
    _fields_ = [
        ("family", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8),
        ("address_len", ctypes.c_uint16),
        ("var_data", ctypes.c_void_p),
    ]


ListHostsRequestCookie = NewType('ListHostsRequestCookie', ctypes.c_uint32)


ListHostsRequestPacket = DataPacket((
))


class ListHostsRequest:
    OPCODE = 110

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListHostsRequest':
        return ListHostsRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], ListHostsRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ListHostsRequest.lib = library.xproto_listhosts
        ListHostsRequest.lib.restype = ListHostsRequestCookie
        ListHostsRequest.lib.argstype = ()


class ListHostsRequestCType(ctypes.Structure):
    """xproto ListHosts"""
    _fields_ = [
    ]


ListHostsReplyReplyPacket = DataPacket((
    ('mode', FixedDataPacketField(MARKER_INT8)),
    ('hosts_len', FixedDataPacketField(MARKER_UINT16)),
    ('pad0', FixedPadDataPacketField(22)),
    ('hosts', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['hosts_len'], 0)),
))


class ListHostsReplyReply:
    __slots__ = ('mode', 'hosts_len', 'hosts',)

    def __init__(
            self, *,
            mode: Optional[int] = None,
            hosts_len: Optional[int] = None,
            hosts: Optional[Sequence[int]] = None,
    ) -> None:
        self.mode = mode
        self.hosts_len = hosts_len
        self.hosts = hosts

    def as_dict(self) -> Dict[str, Any]:
        return {
            'mode': self.mode,
            'hosts_len': self.hosts_len,
            'hosts': self.hosts,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ListHostsReplyReply':
        return ListHostsReplyReply(**ListHostsReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ListHostsReplyReplyPacket.pack(**self.as_dict())


class ListHostsReplyReplyCType(ctypes.Structure):
    """xproto ListHosts_reply"""
    _fields_ = [
        ("mode", ctypes.c_int8),
        ("hosts_len", ctypes.c_uint16),
        ("pad0", ctypes.c_uint8 * 22),
        ("var_data", ctypes.c_void_p),
    ]


SetAccessControlRequestPacket = DataPacket((
    ('mode', FixedDataPacketField(MARKER_UINT8)),
))


class SetAccessControlRequest:
    OPCODE = 111

    __slots__ = ('mode',)

    def __init__(
            self, *,
            mode: Optional[int] = None,
    ) -> None:
        self.mode = mode

    def as_dict(self) -> Dict[str, Any]:
        return {
            'mode': self.mode,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetAccessControlRequest':
        return SetAccessControlRequest(**SetAccessControlRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetAccessControlRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetAccessControlRequest.lib = library.xproto_setaccesscontrol
        SetAccessControlRequest.lib.restype = ctypes.c_uint32
        SetAccessControlRequest.lib.argstype = (ctypes.c_uint8,)


class SetAccessControlRequestCType(ctypes.Structure):
    """xproto SetAccessControl"""
    _fields_ = [
        ("mode", ctypes.c_uint8),
    ]


SetCloseDownModeRequestPacket = DataPacket((
    ('mode', FixedDataPacketField(MARKER_UINT8)),
))


class SetCloseDownModeRequest:
    OPCODE = 112

    __slots__ = ('mode',)

    def __init__(
            self, *,
            mode: Optional[int] = None,
    ) -> None:
        self.mode = mode

    def as_dict(self) -> Dict[str, Any]:
        return {
            'mode': self.mode,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetCloseDownModeRequest':
        return SetCloseDownModeRequest(**SetCloseDownModeRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetCloseDownModeRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetCloseDownModeRequest.lib = library.xproto_setclosedownmode
        SetCloseDownModeRequest.lib.restype = ctypes.c_uint32
        SetCloseDownModeRequest.lib.argstype = (ctypes.c_uint8,)


class SetCloseDownModeRequestCType(ctypes.Structure):
    """xproto SetCloseDownMode"""
    _fields_ = [
        ("mode", ctypes.c_uint8),
    ]


KillClientRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('resource', FixedDataPacketField(MARKER_UINT32)),
))


class KillClientRequest:
    OPCODE = 113

    __slots__ = ('resource',)

    def __init__(
            self, *,
            resource: Optional[int] = None,
    ) -> None:
        self.resource = resource

    def as_dict(self) -> Dict[str, Any]:
        return {
            'resource': self.resource,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'KillClientRequest':
        return KillClientRequest(**KillClientRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return KillClientRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        KillClientRequest.lib = library.xproto_killclient
        KillClientRequest.lib.restype = ctypes.c_uint32
        KillClientRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32)


class KillClientRequestCType(ctypes.Structure):
    """xproto KillClient"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("resource", ctypes.c_uint32),
    ]


RotatePropertiesRequestPacket = DataPacket((
    ('pad0', FixedPadDataPacketField(1)),
    ('window', FixedDataPacketField(MARKER_UINT32)),
    ('atoms_len', FixedDataPacketField(MARKER_UINT16)),
    ('delta', FixedDataPacketField(MARKER_INT16)),
    ('atoms', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: d['atoms_len'], 0)),
))


class RotatePropertiesRequest:
    OPCODE = 114

    __slots__ = ('window', 'atoms_len', 'delta', 'atoms',)

    def __init__(
            self, *,
            window: Optional[int] = None,
            atoms_len: Optional[int] = None,
            delta: Optional[int] = None,
            atoms: Optional[Sequence[int]] = None,
    ) -> None:
        self.window = window
        self.atoms_len = atoms_len
        self.delta = delta
        self.atoms = atoms

    def as_dict(self) -> Dict[str, Any]:
        return {
            'window': self.window,
            'atoms_len': self.atoms_len,
            'delta': self.delta,
            'atoms': self.atoms,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'RotatePropertiesRequest':
        return RotatePropertiesRequest(**RotatePropertiesRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return RotatePropertiesRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, int, int, Sequence[int]], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        RotatePropertiesRequest.lib = library.xproto_rotateproperties
        RotatePropertiesRequest.lib.restype = ctypes.c_uint32
        RotatePropertiesRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_uint32, ctypes.c_uint16, ctypes.c_int16, ctypes.c_void_p)


class RotatePropertiesRequestCType(ctypes.Structure):
    """xproto RotateProperties"""
    _fields_ = [
        ("pad0", ctypes.c_uint8),
        ("window", ctypes.c_uint32),
        ("atoms_len", ctypes.c_uint16),
        ("delta", ctypes.c_int16),
        ("var_data", ctypes.c_void_p),
    ]


ForceScreenSaverRequestPacket = DataPacket((
    ('mode', FixedDataPacketField(MARKER_UINT8)),
))


class ForceScreenSaverRequest:
    OPCODE = 115

    __slots__ = ('mode',)

    def __init__(
            self, *,
            mode: Optional[int] = None,
    ) -> None:
        self.mode = mode

    def as_dict(self) -> Dict[str, Any]:
        return {
            'mode': self.mode,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'ForceScreenSaverRequest':
        return ForceScreenSaverRequest(**ForceScreenSaverRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return ForceScreenSaverRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        ForceScreenSaverRequest.lib = library.xproto_forcescreensaver
        ForceScreenSaverRequest.lib.restype = ctypes.c_uint32
        ForceScreenSaverRequest.lib.argstype = (ctypes.c_uint8,)


class ForceScreenSaverRequestCType(ctypes.Structure):
    """xproto ForceScreenSaver"""
    _fields_ = [
        ("mode", ctypes.c_uint8),
    ]


SetPointerMappingRequestCookie = NewType('SetPointerMappingRequestCookie', ctypes.c_uint32)


SetPointerMappingRequestPacket = DataPacket((
    ('map_len', FixedDataPacketField(MARKER_UINT8)),
    ('map', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['map_len'], 0)),
))


class SetPointerMappingRequest:
    OPCODE = 116

    __slots__ = ('map_len', 'map',)

    def __init__(
            self, *,
            map_len: Optional[int] = None,
            map: Optional[Sequence[int]] = None,
    ) -> None:
        self.map_len = map_len
        self.map = map

    def as_dict(self) -> Dict[str, Any]:
        return {
            'map_len': self.map_len,
            'map': self.map,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetPointerMappingRequest':
        return SetPointerMappingRequest(**SetPointerMappingRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetPointerMappingRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Sequence[int]], SetPointerMappingRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetPointerMappingRequest.lib = library.xproto_setpointermapping
        SetPointerMappingRequest.lib.restype = SetPointerMappingRequestCookie
        SetPointerMappingRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_void_p)


class SetPointerMappingRequestCType(ctypes.Structure):
    """xproto SetPointerMapping"""
    _fields_ = [
        ("map_len", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


SetPointerMappingReplyReplyPacket = DataPacket((
    ('status', FixedDataPacketField(MARKER_INT8)),
))


class SetPointerMappingReplyReply:
    __slots__ = ('status',)

    def __init__(
            self, *,
            status: Optional[int] = None,
    ) -> None:
        self.status = status

    def as_dict(self) -> Dict[str, Any]:
        return {
            'status': self.status,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetPointerMappingReplyReply':
        return SetPointerMappingReplyReply(**SetPointerMappingReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetPointerMappingReplyReplyPacket.pack(**self.as_dict())


class SetPointerMappingReplyReplyCType(ctypes.Structure):
    """xproto SetPointerMapping_reply"""
    _fields_ = [
        ("status", ctypes.c_int8),
    ]


GetPointerMappingRequestCookie = NewType('GetPointerMappingRequestCookie', ctypes.c_uint32)


GetPointerMappingRequestPacket = DataPacket((
))


class GetPointerMappingRequest:
    OPCODE = 117

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPointerMappingRequest':
        return GetPointerMappingRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], GetPointerMappingRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetPointerMappingRequest.lib = library.xproto_getpointermapping
        GetPointerMappingRequest.lib.restype = GetPointerMappingRequestCookie
        GetPointerMappingRequest.lib.argstype = ()


class GetPointerMappingRequestCType(ctypes.Structure):
    """xproto GetPointerMapping"""
    _fields_ = [
    ]


GetPointerMappingReplyReplyPacket = DataPacket((
    ('map_len', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(24)),
    ('map', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: d['map_len'], 0)),
))


class GetPointerMappingReplyReply:
    __slots__ = ('map_len', 'map',)

    def __init__(
            self, *,
            map_len: Optional[int] = None,
            map: Optional[Sequence[int]] = None,
    ) -> None:
        self.map_len = map_len
        self.map = map

    def as_dict(self) -> Dict[str, Any]:
        return {
            'map_len': self.map_len,
            'map': self.map,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetPointerMappingReplyReply':
        return GetPointerMappingReplyReply(**GetPointerMappingReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetPointerMappingReplyReplyPacket.pack(**self.as_dict())


class GetPointerMappingReplyReplyCType(ctypes.Structure):
    """xproto GetPointerMapping_reply"""
    _fields_ = [
        ("map_len", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 24),
        ("var_data", ctypes.c_void_p),
    ]


SetModifierMappingRequestCookie = NewType('SetModifierMappingRequestCookie', ctypes.c_uint32)


SetModifierMappingRequestPacket = DataPacket((
    ('keycodes_per_modifier', FixedDataPacketField(MARKER_UINT8)),
    ('keycodes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: (d['keycodes_per_modifier']) * (8), 0)),
))


class SetModifierMappingRequest:
    OPCODE = 118

    __slots__ = ('keycodes_per_modifier', 'keycodes',)

    def __init__(
            self, *,
            keycodes_per_modifier: Optional[int] = None,
            keycodes: Optional[Sequence[int]] = None,
    ) -> None:
        self.keycodes_per_modifier = keycodes_per_modifier
        self.keycodes = keycodes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'keycodes_per_modifier': self.keycodes_per_modifier,
            'keycodes': self.keycodes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetModifierMappingRequest':
        return SetModifierMappingRequest(**SetModifierMappingRequestPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetModifierMappingRequestPacket.pack(**self.as_dict())

    lib: Optional[Callable[[int, Sequence[int]], SetModifierMappingRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        SetModifierMappingRequest.lib = library.xproto_setmodifiermapping
        SetModifierMappingRequest.lib.restype = SetModifierMappingRequestCookie
        SetModifierMappingRequest.lib.argstype = (ctypes.c_uint8, ctypes.c_void_p)


class SetModifierMappingRequestCType(ctypes.Structure):
    """xproto SetModifierMapping"""
    _fields_ = [
        ("keycodes_per_modifier", ctypes.c_uint8),
        ("var_data", ctypes.c_void_p),
    ]


SetModifierMappingReplyReplyPacket = DataPacket((
    ('status', FixedDataPacketField(MARKER_INT8)),
))


class SetModifierMappingReplyReply:
    __slots__ = ('status',)

    def __init__(
            self, *,
            status: Optional[int] = None,
    ) -> None:
        self.status = status

    def as_dict(self) -> Dict[str, Any]:
        return {
            'status': self.status,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'SetModifierMappingReplyReply':
        return SetModifierMappingReplyReply(**SetModifierMappingReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return SetModifierMappingReplyReplyPacket.pack(**self.as_dict())


class SetModifierMappingReplyReplyCType(ctypes.Structure):
    """xproto SetModifierMapping_reply"""
    _fields_ = [
        ("status", ctypes.c_int8),
    ]


GetModifierMappingRequestCookie = NewType('GetModifierMappingRequestCookie', ctypes.c_uint32)


GetModifierMappingRequestPacket = DataPacket((
))


class GetModifierMappingRequest:
    OPCODE = 119

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetModifierMappingRequest':
        return GetModifierMappingRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], GetModifierMappingRequestCookie]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        GetModifierMappingRequest.lib = library.xproto_getmodifiermapping
        GetModifierMappingRequest.lib.restype = GetModifierMappingRequestCookie
        GetModifierMappingRequest.lib.argstype = ()


class GetModifierMappingRequestCType(ctypes.Structure):
    """xproto GetModifierMapping"""
    _fields_ = [
    ]


GetModifierMappingReplyReplyPacket = DataPacket((
    ('keycodes_per_modifier', FixedDataPacketField(MARKER_UINT8)),
    ('pad0', FixedPadDataPacketField(24)),
    ('keycodes', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: (d['keycodes_per_modifier']) * (8), 0)),
))


class GetModifierMappingReplyReply:
    __slots__ = ('keycodes_per_modifier', 'keycodes',)

    def __init__(
            self, *,
            keycodes_per_modifier: Optional[int] = None,
            keycodes: Optional[Sequence[int]] = None,
    ) -> None:
        self.keycodes_per_modifier = keycodes_per_modifier
        self.keycodes = keycodes

    def as_dict(self) -> Dict[str, Any]:
        return {
            'keycodes_per_modifier': self.keycodes_per_modifier,
            'keycodes': self.keycodes,
        }

    @staticmethod
    def from_data(inp: BinaryIO) -> 'GetModifierMappingReplyReply':
        return GetModifierMappingReplyReply(**GetModifierMappingReplyReplyPacket.unpack(inp))

    def to_data(self) -> bytes:
        return GetModifierMappingReplyReplyPacket.pack(**self.as_dict())


class GetModifierMappingReplyReplyCType(ctypes.Structure):
    """xproto GetModifierMapping_reply"""
    _fields_ = [
        ("keycodes_per_modifier", ctypes.c_uint8),
        ("pad0", ctypes.c_uint8 * 24),
        ("var_data", ctypes.c_void_p),
    ]


NoOperationRequestPacket = DataPacket((
))


class NoOperationRequest:
    OPCODE = 127

    __slots__ = ()

    def as_dict(self) -> Dict[str, Any]:
        return {}

    @staticmethod
    def from_data(inp: BinaryIO) -> 'NoOperationRequest':
        return NoOperationRequest()

    def to_data(self) -> bytes:
        return b''

    lib: Optional[Callable[[], ctypes.c_uint32]] = None

    @staticmethod
    def lib_call(library: ctypes.CDLL) -> None:
        NoOperationRequest.lib = library.xproto_nooperation
        NoOperationRequest.lib.restype = ctypes.c_uint32
        NoOperationRequest.lib.argstype = ()


class NoOperationRequestCType(ctypes.Structure):
    """xproto NoOperation"""
    _fields_ = [
    ]


# ------------------------------------------------------------------
# Unions

ClientMessageDataUnion = {
    'data8': DataPacket((
        ('data8', SimpleListDataPacketField(MARKER_UINT8, lambda d, c: 20, 0)),
    )),
    'data16': DataPacket((
        ('data16', SimpleListDataPacketField(MARKER_UINT16, lambda d, c: 10, 0)),
    )),
    'data32': DataPacket((
        ('data32', SimpleListDataPacketField(MARKER_UINT32, lambda d, c: 5, 0)),
    )),
}

