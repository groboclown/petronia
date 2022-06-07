"""Constants for xcb (and xproto)"""

import ctypes
from . import xcb_types as nat
from ..ct_util import as_py_int, as_null


# Consts
XCB_COLORMAP_ALLOC_NONE = 0
XCB_COLORMAP_ALLOC_NONE__c: ctypes.c_uint8 = ctypes.c_uint8(XCB_COLORMAP_ALLOC_NONE)
XCB_COLORMAP_ALLOC_ALL = 1
XCB_COLORMAP_ALLOC_ALL__c: ctypes.c_uint8 = ctypes.c_uint8(XCB_COLORMAP_ALLOC_ALL)

NULL__XcbGenericErrorPP = as_null(nat.XcbGenericErrorPP)

XCB_WINDOW_CLASS_COPY_FROM_PARENT = 0
XCB_WINDOW_CLASS_INPUT_OUTPUT = 1
XCB_WINDOW_CLASS_INPUT_ONLY = 2

# window class
XCB_COPY_FROM_PARENT = 0
XCB_COPY_FROM_PARENT__c = ctypes.c_uint16(XCB_COPY_FROM_PARENT)

XCB_NONE = 0
XCB_NONE__c = nat.XcbWindow(XCB_NONE)
XCB_GET_PROPERTY_TYPE_ANY = 0
XCB_GET_PROPERTY_TYPE_ANY__c = nat.XcbAtom(XCB_GET_PROPERTY_TYPE_ANY)

XCB_CW_BACK_PIXMAP = 1
XCB_CW_BACK_PIXEL = 2
XCB_CW_BORDER_PIXMAP = 4
XCB_CW_BORDER_PIXEL = 8
XCB_CW_BIT_GRAVITY = 16
XCB_CW_WIN_GRAVITY = 32
XCB_CW_BACKING_STORE = 64
XCB_CW_BACKING_PLANES = 128
XCB_CW_BACKING_PIXEL = 256
XCB_CW_OVERRIDE_REDIRECT = 512
XCB_CW_SAVE_UNDER = 1024
XCB_CW_EVENT_MASK = 2048
XCB_CW_DONT_PROPAGATE = 4096
XCB_CW_COLORMAP = 8192
XCB_CW_CURSOR = 16384

XCB_CW_EVENT_MASK__c = ctypes.c_uint32(XCB_CW_EVENT_MASK)


XCB_EVENT_RESPONSE_TYPE_MASK = 0x7f

XCB_EVENT_MASK_NO_EVENT = 0
XCB_EVENT_MASK_KEY_PRESS = 1
XCB_EVENT_MASK_KEY_RELEASE = 2
XCB_EVENT_MASK_BUTTON_PRESS = 4
XCB_EVENT_MASK_BUTTON_RELEASE = 8
XCB_EVENT_MASK_ENTER_WINDOW = 16
XCB_EVENT_MASK_LEAVE_WINDOW = 32
XCB_EVENT_MASK_POINTER_MOTION = 64
XCB_EVENT_MASK_POINTER_MOTION_HINT = 128
XCB_EVENT_MASK_BUTTON_1_MOTION = 256
XCB_EVENT_MASK_BUTTON_2_MOTION = 512
XCB_EVENT_MASK_BUTTON_3_MOTION = 1024
XCB_EVENT_MASK_BUTTON_4_MOTION = 2048
XCB_EVENT_MASK_BUTTON_5_MOTION = 4096
XCB_EVENT_MASK_BUTTON_MOTION = 8192
XCB_EVENT_MASK_KEYMAP_STATE = 16384
XCB_EVENT_MASK_EXPOSURE = 32768
XCB_EVENT_MASK_VISIBILITY_CHANGE = 65536
XCB_EVENT_MASK_STRUCTURE_NOTIFY = 131072
XCB_EVENT_MASK_RESIZE_REDIRECT = 262144
XCB_EVENT_MASK_SUBSTRUCTURE_NOTIFY = 524288
XCB_EVENT_MASK_SUBSTRUCTURE_NOTIFY__c = ctypes.c_uint32(XCB_EVENT_MASK_SUBSTRUCTURE_NOTIFY)
XCB_EVENT_MASK_SUBSTRUCTURE_REDIRECT = 1048576
XCB_EVENT_MASK_SUBSTRUCTURE_REDIRECT__c = ctypes.c_uint32(XCB_EVENT_MASK_SUBSTRUCTURE_REDIRECT)
XCB_EVENT_MASK_FOCUS_CHANGE = 2097152
XCB_EVENT_MASK_PROPERTY_CHANGE = 4194304
XCB_EVENT_MASK_PROPERTY_CHANGE__c = ctypes.c_uint32(XCB_EVENT_MASK_PROPERTY_CHANGE)
XCB_EVENT_MASK_COLOR_MAP_CHANGE = 8388608
XCB_EVENT_MASK_OWNER_GRAB_BUTTON = 16777216

# Event IDs
#  key_press is supposed to be 2, and key_release is supposed to be 3, but
#  that isn't what is happening here.
XCB_KEY_PRESS = 2
XCB_KEY_RELEASE = 3
XCB_BUTTON_PRESS = 4
XCB_BUTTON_RELEASE = 5
XCB_MOTION_NOTIFY = 6
XCB_ENTER_NOTIFY = 7
XCB_LEAVE_NOTIFY = 8
XCB_FOCUS_IN = 9
XCB_FOCUS_OUT = 10
XCB_KEYMAP_NOTIFY = 11
XCB_EXPOSE = 12
XCB_GRAPHICS_EXPOSURE = 13
XCB_NO_EXPOSURE = 14
XCB_VISIBILITY_NOTIFY = 15
XCB_CREATE_NOTIFY = 16
XCB_DESTROY_NOTIFY = 17
XCB_UNMAP_NOTIFY = 18
XCB_MAP_NOTIFY = 19
XCB_MAP_REQUEST = 20
XCB_REPARENT_NOTIFY = 21
XCB_CONFIGURE_NOTIFY = 22
XCB_CONFIGURE_REQUEST = 23
XCB_GRAVITY_NOTIFY = 24
XCB_RESIZE_REQUEST = 25
XCB_CIRCULATE_NOTIFY = 26
XCB_CIRCULATE_REQUEST = 27
XCB_PROPERTY_NOTIFY = 28
XCB_SELECTION_CLEAR = 29
XCB_SELECTION_REQUEST = 30
XCB_SELECTION_NOTIFY = 31
XCB_COLORMAP_NOTIFY = 32
XCB_CLIENT_MESSAGE = 33
XCB_CLIENT_MESSAGE__c = ctypes.c_uint8(XCB_CLIENT_MESSAGE)
XCB_MAPPING_NOTIFY = 34
XCB_GE_GENERIC = 35

# Error IDs
XCB_REQUEST = 1
XCB_VALUE = 2
XCB_WINDOW = 3
XCB_PIXMAP = 4
XCB_ATOM = 5
XCB_CURSOR = 6
XCB_FONT = 7
XCB_MATCH = 8
XCB_DRAWABLE = 9
XCB_ACCESS = 10
XCB_ALLOC = 11
XCB_COLORMAP = 12
XCB_G_CONTEXT = 13
XCB_ID_CHOICE = 14
XCB_NAME = 15
XCB_LENGTH = 16
XCB_IMPLEMENTATION = 17

XCB_PROP_MODE_REPLACE = 0
XCB_PROP_MODE_REPLACE__c = ctypes.c_uint8(XCB_PROP_MODE_REPLACE)
XCB_PROP_MODE_PREPEND = 1
XCB_PROP_MODE_PREPEND__c = ctypes.c_uint8(XCB_PROP_MODE_PREPEND)
XCB_PROP_MODE_APPEND = 2
XCB_PROP_MODE_APPEND__c = ctypes.c_uint8(XCB_PROP_MODE_APPEND)

XCB_ATOM_NONE = 0
XCB_ATOM_NONE__c = nat.XcbAtom(XCB_ATOM_NONE)
XCB_ATOM_ANY__c = nat.XcbAtom(0)
XCB_ATOM_PRIMARY__c = nat.XcbAtom(1)
XCB_ATOM_SECONDARY__c = nat.XcbAtom(2)
XCB_ATOM_ARC__c = nat.XcbAtom(3)
XCB_ATOM_ATOM__c = nat.XcbAtom(4)
XCB_ATOM_BITMAP__c = nat.XcbAtom(5)
XCB_ATOM_CARDINAL__c = nat.XcbAtom(6)
XCB_ATOM_COLORMAP__c = nat.XcbAtom(7)
XCB_ATOM_CURSOR__c = nat.XcbAtom(8)
XCB_ATOM_CUT_BUFFER0__c = nat.XcbAtom(9)
XCB_ATOM_CUT_BUFFER1__c = nat.XcbAtom(10)
XCB_ATOM_CUT_BUFFER2__c = nat.XcbAtom(11)
XCB_ATOM_CUT_BUFFER3__c = nat.XcbAtom(12)
XCB_ATOM_CUT_BUFFER4__c = nat.XcbAtom(13)
XCB_ATOM_CUT_BUFFER5__c = nat.XcbAtom(14)
XCB_ATOM_CUT_BUFFER6__c = nat.XcbAtom(15)
XCB_ATOM_CUT_BUFFER7__c = nat.XcbAtom(16)
XCB_ATOM_DRAWABLE__c = nat.XcbAtom(17)
XCB_ATOM_FONT__c = nat.XcbAtom(18)
XCB_ATOM_INTEGER__c = nat.XcbAtom(19)
XCB_ATOM_PIXMAP__c = nat.XcbAtom(20)
XCB_ATOM_POINT__c = nat.XcbAtom(21)
XCB_ATOM_RECTANGLE__c = nat.XcbAtom(22)
XCB_ATOM_RESOURCE_MANAGER__c = nat.XcbAtom(23)
XCB_ATOM_RGB_COLOR_MAP__c = nat.XcbAtom(24)
XCB_ATOM_RGB_BEST_MAP__c = nat.XcbAtom(25)
XCB_ATOM_RGB_BLUE_MAP__c = nat.XcbAtom(26)
XCB_ATOM_RGB_DEFAULT_MAP__c = nat.XcbAtom(27)
XCB_ATOM_RGB_GRAY_MAP__c = nat.XcbAtom(28)
XCB_ATOM_RGB_GREEN_MAP__c = nat.XcbAtom(29)
XCB_ATOM_RGB_RED_MAP__c = nat.XcbAtom(30)
XCB_ATOM_STRING__c = nat.XcbAtom(31)
XCB_ATOM_VISUALID__c = nat.XcbAtom(32)
XCB_ATOM_WINDOW__c = nat.XcbAtom(33)
XCB_ATOM_WM_COMMAND__c = nat.XcbAtom(34)
XCB_ATOM_WM_HINTS__c = nat.XcbAtom(35)
XCB_ATOM_WM_CLIENT_MACHINE__c = nat.XcbAtom(36)
XCB_ATOM_WM_ICON_NAME__c = nat.XcbAtom(37)
XCB_ATOM_WM_ICON_SIZE__c = nat.XcbAtom(38)
XCB_ATOM_WM_NAME__c = nat.XcbAtom(39)
XCB_ATOM_WM_NORMAL_HINTS__c = nat.XcbAtom(40)
XCB_ATOM_WM_SIZE_HINTS__c = nat.XcbAtom(41)
XCB_ATOM_WM_ZOOM_HINTS__c = nat.XcbAtom(42)
XCB_ATOM_MIN_SPACE__c = nat.XcbAtom(43)
XCB_ATOM_NORM_SPACE__c = nat.XcbAtom(44)
XCB_ATOM_MAX_SPACE__c = nat.XcbAtom(45)
XCB_ATOM_END_SPACE__c = nat.XcbAtom(46)
XCB_ATOM_SUPERSCRIPT_X__c = nat.XcbAtom(47)
XCB_ATOM_SUPERSCRIPT_Y__c = nat.XcbAtom(48)
XCB_ATOM_SUBSCRIPT_X__c = nat.XcbAtom(49)
XCB_ATOM_SUBSCRIPT_Y__c = nat.XcbAtom(50)
XCB_ATOM_UNDERLINE_POSITION__c = nat.XcbAtom(51)
XCB_ATOM_UNDERLINE_THICKNESS__c = nat.XcbAtom(52)
XCB_ATOM_STRIKEOUT_ASCENT__c = nat.XcbAtom(53)
XCB_ATOM_STRIKEOUT_DESCENT__c = nat.XcbAtom(54)
XCB_ATOM_ITALIC_ANGLE__c = nat.XcbAtom(55)
XCB_ATOM_X_HEIGHT__c = nat.XcbAtom(56)
XCB_ATOM_QUAD_WIDTH__c = nat.XcbAtom(57)
XCB_ATOM_WEIGHT__c = nat.XcbAtom(58)
XCB_ATOM_POINT_SIZE__c = nat.XcbAtom(59)
XCB_ATOM_RESOLUTION__c = nat.XcbAtom(60)
XCB_ATOM_COPYRIGHT__c = nat.XcbAtom(61)
XCB_ATOM_NOTICE__c = nat.XcbAtom(62)
XCB_ATOM_FONT_NAME__c = nat.XcbAtom(63)
XCB_ATOM_FAMILY_NAME__c = nat.XcbAtom(64)
XCB_ATOM_FULL_NAME__c = nat.XcbAtom(65)
XCB_ATOM_CAP_HEIGHT__c = nat.XcbAtom(66)
XCB_ATOM_WM_CLASS__c = nat.XcbAtom(67)
XCB_ATOM_WM_TRANSIENT_FOR__c = nat.XcbAtom(68)

XCB_INPUT_FOCUS_POINTER_ROOT = 1
XCB_INPUT_FOCUS_POINTER_ROOT__c = ctypes.c_uint8(XCB_INPUT_FOCUS_POINTER_ROOT)

XCB_GC_FUNCTION = 1
XCB_GC_PLANE_MASK = 2
XCB_GC_FOREGROUND = 4
XCB_GC_BACKGROUND = 8
XCB_GC_LINE_WIDTH = 16
XCB_GC_LINE_STYLE = 32
XCB_GC_CAP_STYLE = 64
XCB_GC_JOIN_STYLE = 128
XCB_GC_FILL_STYLE = 256
XCB_GC_FILL_RULE = 512
XCB_GC_TILE = 1024
XCB_GC_STIPPLE = 2048
XCB_GC_TILE_STIPPLE_ORIGIN_X = 4096
XCB_GC_TILE_STIPPLE_ORIGIN_Y = 8192
XCB_GC_FONT = 16384
XCB_GC_SUBWINDOW_MODE = 32768
XCB_GC_GRAPHICS_EXPOSURES = 65536
XCB_GC_CLIP_ORIGIN_X = 131072
XCB_GC_CLIP_ORIGIN_Y = 262144
XCB_GC_CLIP_MASK = 524288
XCB_GC_DASH_OFFSET = 1048576
XCB_GC_DASH_LIST = 2097152
XCB_GC_ARC_MODE = 4194304

# Key / Button masks
XCB_KEY_BUT_MASK_SHIFT = 1
XCB_KEY_BUT_MASK_LOCK = 2
XCB_KEY_BUT_MASK_CONTROL = 4
XCB_KEY_BUT_MASK_MOD_1 = 8
XCB_KEY_BUT_MASK_MOD_2 = 16
XCB_KEY_BUT_MASK_MOD_3 = 32
XCB_KEY_BUT_MASK_MOD_4 = 64
XCB_KEY_BUT_MASK_MOD_5 = 128
XCB_KEY_BUT_MASK_BUTTON_1 = 256
XCB_KEY_BUT_MASK_BUTTON_2 = 512
XCB_KEY_BUT_MASK_BUTTON_3 = 1024
XCB_KEY_BUT_MASK_BUTTON_4 = 2048
XCB_KEY_BUT_MASK_BUTTON_5 = 4096

# Configure Window Requests
XCB_CONFIG_WINDOW_X = 1
XCB_CONFIG_WINDOW_Y = 2
XCB_CONFIG_WINDOW_WIDTH = 4
XCB_CONFIG_WINDOW_HEIGHT = 8
XCB_CONFIG_WINDOW_BORDER_WIDTH = 16
XCB_CONFIG_WINDOW_BORDER_WIDTH__c = ctypes.c_uint32(XCB_CONFIG_WINDOW_BORDER_WIDTH)
XCB_CONFIG_WINDOW_SIBLING = 32
XCB_CONFIG_WINDOW_STACK_MODE = 64
XCB_CONFIG_WINDOW_STACK_MODE__c = ctypes.c_uint32(XCB_CONFIG_WINDOW_STACK_MODE)

# Stack Mode, enum in the Configure Window Request stack mode value
XCB_STACK_MODE_ABOVE = 0
XCB_STACK_MODE_BELOW = 1
XCB_STACK_MODE_BELOW__c = ctypes.c_uint32(XCB_STACK_MODE_BELOW)
XCB_STACK_MODE_TOP_IF = 2
XCB_STACK_MODE_BOTTOM_IF = 3
XCB_STACK_MODE_OPPOSITE = 4

# typedef enum xcb_set_mode_t
XCB_SET_MODE_INSERT = 0
XCB_SET_MODE_INSERT__c = ctypes.c_uint8(XCB_SET_MODE_INSERT)
XCB_SET_MODE_DELETE = 1
XCB_SET_MODE_DELETE__c = ctypes.c_uint8(XCB_SET_MODE_DELETE)

UINT_MAX = 0xffffffff
UINT_MAX__c = ctypes.c_uint32(UINT_MAX)

# typedef enum xcb_gravity_t
XCB_GRAVITY_BIT_FORGET = 0
XCB_GRAVITY_WIN_UNMAP = 0
XCB_GRAVITY_NORTH_WEST = 1
XCB_GRAVITY_NORTH_WEST__c = ctypes.c_int32(XCB_GRAVITY_NORTH_WEST)
XCB_GRAVITY_NORTH = 2
XCB_GRAVITY_NORTH_EAST = 3
XCB_GRAVITY_WEST = 4
XCB_GRAVITY_CENTER = 5
XCB_GRAVITY_EAST = 6
XCB_GRAVITY_SOUTH_WEST = 7
XCB_GRAVITY_SOUTH = 8
XCB_GRAVITY_SOUTH_EAST = 9
XCB_GRAVITY_STATIC = 10

# xcb_map_state_t
XCB_MAP_STATE_UNMAPPED = 0
XCB_MAP_STATE_UNVIEWABLE = 1
XCB_MAP_STATE_VIEWABLE = 2
