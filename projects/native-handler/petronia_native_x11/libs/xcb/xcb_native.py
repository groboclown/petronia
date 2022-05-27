"""Definitions from xcb.h and xproto.h.  Translates native names into local names.

And other xcb libraries, and cairo.

The functions are loaded into a class object to retain typing.

See:

https://xcb.freedesktop.org/PublicApi/
https://xcb.freedesktop.org/manual/xproto_8h_source.html
https://xcb.freedesktop.org/manual/xcb_8h_source.html
"""

from typing import Callable, Any
from typing import cast as t_cast
import ctypes
import warnings
from .util import as_py_int

# typedef uint32_t xcb_window_t;
XcbWindow = ctypes.c_uint32

# typedef uint32_t xcb_colormap_t;
XcbColormap = ctypes.c_uint32

# typedef uint32_t xcb_visualid_t;
XcbVisualid = ctypes.c_uint32

# typedef uint8_t xcb_keycode_t;
XcbKeycode = ctypes.c_uint8

# typedef uint32_t xcb_atom_t;
XcbAtom = ctypes.c_uint32

# typedef uint32_t xcb_drawable_t;
XcbDrawable = ctypes.c_uint32

# typedef uint32_t xcb_pixmap_t;
XcbPixmap = ctypes.c_uint32

# typedef uint32_t xcb_timestamp_t;
XcbTimestamp = ctypes.c_uint32


class XcbConnection(ctypes.Structure):
    """The opaque type xcb_connection_t"""
    _fields_ = []


XcbConnectionP = ctypes.POINTER(XcbConnection)


class XcbExtension(ctypes.Structure):
    """The opaque type xcb_extension_t"""
    _fields_ = []


XcbExtensionP = ctypes.POINTER(XcbExtension)


class XcbAuthInfo(ctypes.Structure):
    """The xcb_auth_info_t structure."""
    _fields_ = [
        # length of the name field
        ('namelen', ctypes.c_int),

        # string containing the authentication protocol name,
        #   such as MIT-MAGIC-COOKIE-1 or XDM-AUTHORIZATION-1
        ('name', ctypes.c_char_p),

        ('datalen', ctypes.c_int),
        # interpreted in a protocol-specific manner.
        ('data', ctypes.c_char_p),
    ]


class XcbVoidCookie(ctypes.Structure):
    """The xcb_void_cookie_t structure."""
    _fields_ = [
        # Sequence number
        ('sequence', ctypes.c_uint),
    ]


# xcb_intern_atom_cookie_t
XcbInternAtomCookie = XcbVoidCookie

# xcb_get_selection_owner_cookie_t
XcbGetSelectionOwnerCookie = XcbVoidCookie

# xcb_get_geometry_cookie_t
XcbGetGeometryCookie = XcbVoidCookie

# xcb_get_property_cookie_t
XcbGetPropertyCookie = XcbVoidCookie

# xcb_query_tree_cookie_t
XcbQueryTreeCookie = XcbVoidCookie


class XcbGenericError(ctypes.Structure):
    """The xcb_generic_error_t structure"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('error_code', ctypes.c_uint8),
        ('sequence', ctypes.c_uint16),
        ('resource_id', ctypes.c_uint32),
        ('minor_code', ctypes.c_uint16),
        ('major_code', ctypes.c_uint8),
        ('pad0', ctypes.c_uint8),
        ('pad', ctypes.c_uint32 * 5),
        ('full_sequence', ctypes.c_uint32),
    ]


XcbGenericErrorP = ctypes.POINTER(XcbGenericError)
XcbGenericErrorPP = ctypes.POINTER(XcbGenericErrorP)


class XcbInternAtomReply(ctypes.Structure):
    """The xcb_intern_atom_reply_t structure"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('pad0', ctypes.c_uint8),
        ('sequence', ctypes.c_uint16),
        ('length', ctypes.c_uint32),
        ('atom', XcbAtom),
    ]


XcbInternAtomReplyP = ctypes.POINTER(XcbInternAtomReply)


class XcbGetSelectionOwnerReply(ctypes.Structure):
    """xcb_get_selection_owner_reply_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('pad0', ctypes.c_uint8),
        ('sequence', ctypes.c_uint16),
        ('length', ctypes.c_uint32),
        ('owner', XcbWindow),
    ]


XcbGetSelectionOwnerReplyP = ctypes.POINTER(XcbGetSelectionOwnerReply)


class XcbScreen(ctypes.Structure):
    """xprotocol screen structure."""
    _fields_ = [
        ('root', XcbWindow),
        ('default_colormap', XcbColormap),
        ('white_pixel', ctypes.c_uint32),
        ('black_pixel', ctypes.c_uint32),
        ('current_input_masks', ctypes.c_uint32),
        ('width_in_pixels', ctypes.c_uint16),
        ('height_in_pixels', ctypes.c_uint16),
        ('width_in_millimeters', ctypes.c_uint16),
        ('height_in_millimeters', ctypes.c_uint16),
        ('min_installed_maps', ctypes.c_uint16),
        ('max_installed_maps', ctypes.c_uint16),
        ('root_visual', XcbVisualid),
        ('backing_stores', ctypes.c_uint8),
        ('save_unders', ctypes.c_uint8),
        ('root_depth', ctypes.c_uint8),
        ('allowed_depths_len', ctypes.c_uint8),
    ]


XcbScreenP = ctypes.POINTER(XcbScreen)


class XcbScreenIterator(ctypes.Structure):
    """xcb_screen_iterator_t"""
    _fields_ = [
        ('data', XcbScreenP),
        ('rem', ctypes.c_int),
        ('index', ctypes.c_int),
    ]


class XcbVisualtype(ctypes.Structure):
    """xprotocol visualtype structure"""
    _fields_ = [
        ('visual_id', XcbVisualid),
        ('_class', ctypes.c_uint8),
        ('bits_per_rgb_value', ctypes.c_uint8),
        ('colormap_entries', ctypes.c_uint16),
        ('red_mask', ctypes.c_uint32),
        ('green_mask', ctypes.c_uint32),
        ('blue_mask', ctypes.c_uint32),
        ('pad0', ctypes.c_uint8 * 4),
    ]


XcbVisualtypeP = ctypes.POINTER(XcbVisualtype)


class XcbVisualtypeIterator(ctypes.Structure):
    """xproto xcb_visualtype_iterator_t structure"""
    _fields_ = [
        ('data', XcbVisualtypeP),
        ('rem', ctypes.c_int),
        ('index', ctypes.c_int),
    ]


XcbVisualtypeIteratorP = ctypes.POINTER(XcbVisualtypeIterator)


class XcbDepth(ctypes.Structure):
    """xproto xcb_depth_t structure"""
    _fields_ = [
        ('depth', ctypes.c_uint8),
        ('pad0', ctypes.c_uint8),
        ('visuals_len', ctypes.c_uint16),
        ('pad0', ctypes.c_uint8 * 4),
    ]


XcbDepthP = ctypes.POINTER(XcbDepth)


class XcbDepthIterator(ctypes.Structure):
    """xproto xcb_depth_iterator_t structure"""
    _fields_ = [
        ('data', XcbDepthP),
        ('rem', ctypes.c_int),
        ('index', ctypes.c_int),
    ]


XcbDepthIteratorP = ctypes.POINTER(XcbDepthIterator)


class XcbClientMessageData(ctypes.Union):
    """xcb_client_message_data_t"""
    _fields_ = [
        ('data8', ctypes.c_uint8 * 20),
        ('data16', ctypes.c_uint16 * 10),
        ('data32', ctypes.c_uint32 * 5),
    ]


class XcbClientMessageEvent(ctypes.Structure):
    """xcb_client_message_event_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('format', ctypes.c_uint8),
        ('sequence', ctypes.c_uint16),
        ('window', XcbWindow),
        ('type', XcbAtom),
        ('data', XcbClientMessageData),
    ]


class XcbGetGeometryReply(ctypes.Structure):
    """xcb_get_geometry_reply_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('depth', ctypes.c_uint8),
        ('sequence', ctypes.c_uint16),
        ('length', ctypes.c_uint32),
        ('root', XcbWindow),
        ('x', ctypes.c_int16),
        ('y', ctypes.c_int16),
        ('width', ctypes.c_uint16),
        ('height', ctypes.c_uint16),
        ('border_width', ctypes.c_uint16),
        ('pad0', ctypes.c_uint8 * 2)
    ]


XcbGetGeometryReplyP = ctypes.POINTER(XcbGetGeometryReply)


class XcbGetPropertyReply(ctypes.Structure):
    """xcb_get_property_reply_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('format', ctypes.c_uint8),
        ('sequence', ctypes.c_uint16),
        ('length', ctypes.c_uint32),
        ('type', XcbAtom),
        ('bytes_after', ctypes.c_uint32),
        ('value_len', ctypes.c_uint32),
        ('pad0', ctypes.c_uint8 * 12),
    ]


XcbGetPropertyReplyP = ctypes.POINTER(XcbGetPropertyReply)


class XcbGenericEvent(ctypes.Structure):
    """xcb_generic_event_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('pad0', ctypes.c_uint8),
        ('sequence', ctypes.c_uint8),
        ('pad', ctypes.c_uint8 * 7),
        ('full_sequence', ctypes.c_uint32),
    ]


XcbGenericEventP = ctypes.POINTER(XcbGenericEvent)


class XcbCursorContext(ctypes.Structure):
    """xcb-cursor xcb_cursor_context_t opaque type"""
    _fields_ = []


XcbCursorContextP = ctypes.POINTER(XcbCursorContext)
XcbCursorContextPP = ctypes.POINTER(XcbCursorContextP)


class XcbSetup(ctypes.Structure):
    """xproto xcb_setup_t structure"""
    _fields_ = [
        ('status', ctypes.c_uint8),
        ('pad0', ctypes.c_uint8),
        ('protocol_major_version', ctypes.c_uint16),
        ('protocol_minor_version', ctypes.c_uint16),
        ('length', ctypes.c_uint16),
        ('release_number', ctypes.c_uint32),
        ('resource_id_base', ctypes.c_uint32),
        ('resource_id_mask', ctypes.c_uint32),
        ('motion_buffer_size', ctypes.c_uint32),
        ('vendor_len', ctypes.c_uint16),
        ('maximum_request_length', ctypes.c_uint16),
        ('roots_len', ctypes.c_uint8),
        ('pixmap_formats_len', ctypes.c_uint8),
        ('image_byte_order', ctypes.c_uint8),
        ('bitmap_format_bit_order', ctypes.c_uint8),
        ('bitmap_format_scanline_unit', ctypes.c_uint8),
        ('bitmap_format_scanline_pad', ctypes.c_uint8),
        ('min_keycode', XcbKeycode),
        ('max_keycode', XcbKeycode),
        ('pad1', ctypes.c_uint8 * 4),
    ]


XcbSetupP = ctypes.POINTER(XcbSetup)


class XcbPropertyNotifyEvent(ctypes.Structure):
    """xcb_property_notify_event_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('pad0', ctypes.c_uint8),
        ('sequence', ctypes.c_uint16),
        ('window', XcbWindow),
        ('atom', XcbAtom),
        ('time', XcbTimestamp),
        ('state', ctypes.c_uint8),
        ('pad1', ctypes.c_uint8 * 3),
    ]


XcbPropertyNotifyEventP = ctypes.POINTER(XcbPropertyNotifyEvent)


class CairoSurface(ctypes.Structure):
    """The opaque Cairo cairo_surface_t type"""
    _fields_ = []


CairoSurfaceP = ctypes.POINTER(CairoSurface)


CairoStatus = ctypes.c_int


# Consts
XCB_COLORMAP_ALLOC_NONE: ctypes.c_uint8 = ctypes.c_uint8(0)
XCB_COLORMAP_ALLOC_ALL: ctypes.c_uint8 = ctypes.c_uint8(1)
NULL = ctypes.c_void_p(None)
NULL_c_char_p = ctypes.cast(NULL, ctypes.POINTER(ctypes.c_char))
NULL_XcbGenericErrorPP = ctypes.cast(NULL, XcbGenericErrorPP)
# CAIRO_STATUS_SUCCESS: CairoStatus = ctypes.c_int(0)
CAIRO_STATUS_SUCCESS = 0
XCB_COPY_FROM_PARENT = ctypes.c_uint16(0)
XCB_NONE = XcbWindow(0)
XCB_CLIENT_MESSAGE = ctypes.c_uint8(33)
XCB_GET_PROPERTY_TYPE_ANY = XcbAtom(0)

XCB_CW_EVENT_MASK = ctypes.c_uint32(2048)

XCB_EVENT_MASK_NO_EVENT__i = 0
XCB_EVENT_MASK_KEY_PRESS__i = 1
XCB_EVENT_MASK_KEY_RELEASE__i = 2
XCB_EVENT_MASK_BUTTON_PRESS__i = 4
XCB_EVENT_MASK_BUTTON_RELEASE__i = 8
XCB_EVENT_MASK_ENTER_WINDOW__i = 16
XCB_EVENT_MASK_LEAVE_WINDOW__i = 32
XCB_EVENT_MASK_POINTER_MOTION__i = 64
XCB_EVENT_MASK_POINTER_MOTION_HINT__i = 128
XCB_EVENT_MASK_BUTTON_1_MOTION__i = 256
XCB_EVENT_MASK_BUTTON_2_MOTION__i = 512
XCB_EVENT_MASK_BUTTON_3_MOTION__i = 1024
XCB_EVENT_MASK_BUTTON_4_MOTION__i = 2048
XCB_EVENT_MASK_BUTTON_5_MOTION__i = 4096
XCB_EVENT_MASK_BUTTON_MOTION__i = 8192
XCB_EVENT_MASK_KEYMAP_STATE__i = 16384
XCB_EVENT_MASK_EXPOSURE__i = 32768
XCB_EVENT_MASK_VISIBILITY_CHANGE__i = 65536
XCB_EVENT_MASK_STRUCTURE_NOTIFY__i = 131072
XCB_EVENT_MASK_RESIZE_REDIRECT__i = 262144
XCB_EVENT_MASK_SUBSTRUCTURE_NOTIFY__i = 524288
XCB_EVENT_MASK_SUBSTRUCTURE_NOTIFY__u32 = ctypes.c_uint32(XCB_EVENT_MASK_SUBSTRUCTURE_NOTIFY__i)
XCB_EVENT_MASK_SUBSTRUCTURE_REDIRECT__i = 1048576
XCB_EVENT_MASK_SUBSTRUCTURE_REDIRECT__u32 = ctypes.c_uint32(XCB_EVENT_MASK_SUBSTRUCTURE_REDIRECT__i)
XCB_EVENT_MASK_FOCUS_CHANGE__i = 2097152
XCB_EVENT_MASK_PROPERTY_CHANGE__i = 4194304
XCB_EVENT_MASK_PROPERTY_CHANGE__u32 = ctypes.c_uint32(XCB_EVENT_MASK_PROPERTY_CHANGE__i)
XCB_EVENT_MASK_COLOR_MAP_CHANGE__i = 8388608
XCB_EVENT_MASK_OWNER_GRAB_BUTTON__i = 16777216

XCB_PROP_MODE_REPLACE = ctypes.c_uint8(0)
XCB_PROP_MODE_PREPEND = ctypes.c_uint8(1)
XCB_PROP_MODE_APPEND = ctypes.c_uint8(2)

XCB_ATOM_NONE = XcbAtom(0)
XCB_ATOM_ANY = XcbAtom(0)
XCB_ATOM_PRIMARY = XcbAtom(1)
XCB_ATOM_SECONDARY = XcbAtom(2)
XCB_ATOM_ARC = XcbAtom(3)
XCB_ATOM_ATOM = XcbAtom(4)
XCB_ATOM_BITMAP = XcbAtom(5)
XCB_ATOM_CARDINAL = XcbAtom(6)
XCB_ATOM_COLORMAP = XcbAtom(7)
XCB_ATOM_CURSOR = XcbAtom(8)
XCB_ATOM_CUT_BUFFER0 = XcbAtom(9)
XCB_ATOM_CUT_BUFFER1 = XcbAtom(10)
XCB_ATOM_CUT_BUFFER2 = XcbAtom(11)
XCB_ATOM_CUT_BUFFER3 = XcbAtom(12)
XCB_ATOM_CUT_BUFFER4 = XcbAtom(13)
XCB_ATOM_CUT_BUFFER5 = XcbAtom(14)
XCB_ATOM_CUT_BUFFER6 = XcbAtom(15)
XCB_ATOM_CUT_BUFFER7 = XcbAtom(16)
XCB_ATOM_DRAWABLE = XcbAtom(17)
XCB_ATOM_FONT = XcbAtom(18)
XCB_ATOM_INTEGER = XcbAtom(19)
XCB_ATOM_PIXMAP = XcbAtom(20)
XCB_ATOM_POINT = XcbAtom(21)
XCB_ATOM_RECTANGLE = XcbAtom(22)
XCB_ATOM_RESOURCE_MANAGER = XcbAtom(23)
XCB_ATOM_RGB_COLOR_MAP = XcbAtom(24)
XCB_ATOM_RGB_BEST_MAP = XcbAtom(25)
XCB_ATOM_RGB_BLUE_MAP = XcbAtom(26)
XCB_ATOM_RGB_DEFAULT_MAP = XcbAtom(27)
XCB_ATOM_RGB_GRAY_MAP = XcbAtom(28)
XCB_ATOM_RGB_GREEN_MAP = XcbAtom(29)
XCB_ATOM_RGB_RED_MAP = XcbAtom(30)
XCB_ATOM_STRING = XcbAtom(31)
XCB_ATOM_VISUALID = XcbAtom(32)
XCB_ATOM_WINDOW = XcbAtom(33)
XCB_ATOM_WM_COMMAND = XcbAtom(34)
XCB_ATOM_WM_HINTS = XcbAtom(35)
XCB_ATOM_WM_CLIENT_MACHINE = XcbAtom(36)
XCB_ATOM_WM_ICON_NAME = XcbAtom(37)
XCB_ATOM_WM_ICON_SIZE = XcbAtom(38)
XCB_ATOM_WM_NAME = XcbAtom(39)
XCB_ATOM_WM_NORMAL_HINTS = XcbAtom(40)
XCB_ATOM_WM_SIZE_HINTS = XcbAtom(41)
XCB_ATOM_WM_ZOOM_HINTS = XcbAtom(42)
XCB_ATOM_MIN_SPACE = XcbAtom(43)
XCB_ATOM_NORM_SPACE = XcbAtom(44)
XCB_ATOM_MAX_SPACE = XcbAtom(45)
XCB_ATOM_END_SPACE = XcbAtom(46)
XCB_ATOM_SUPERSCRIPT_X = XcbAtom(47)
XCB_ATOM_SUPERSCRIPT_Y = XcbAtom(48)
XCB_ATOM_SUBSCRIPT_X = XcbAtom(49)
XCB_ATOM_SUBSCRIPT_Y = XcbAtom(50)
XCB_ATOM_UNDERLINE_POSITION = XcbAtom(51)
XCB_ATOM_UNDERLINE_THICKNESS = XcbAtom(52)
XCB_ATOM_STRIKEOUT_ASCENT = XcbAtom(53)
XCB_ATOM_STRIKEOUT_DESCENT = XcbAtom(54)
XCB_ATOM_ITALIC_ANGLE = XcbAtom(55)
XCB_ATOM_X_HEIGHT = XcbAtom(56)
XCB_ATOM_QUAD_WIDTH = XcbAtom(57)
XCB_ATOM_WEIGHT = XcbAtom(58)
XCB_ATOM_POINT_SIZE = XcbAtom(59)
XCB_ATOM_RESOLUTION = XcbAtom(60)
XCB_ATOM_COPYRIGHT = XcbAtom(61)
XCB_ATOM_NOTICE = XcbAtom(62)
XCB_ATOM_FONT_NAME = XcbAtom(63)
XCB_ATOM_FAMILY_NAME = XcbAtom(64)
XCB_ATOM_FULL_NAME = XcbAtom(65)
XCB_ATOM_CAP_HEIGHT = XcbAtom(66)
XCB_ATOM_WM_CLASS = XcbAtom(67)
XCB_ATOM_WM_TRANSIENT_FOR = XcbAtom(68)

XCB_EVENT_RESPONSE_TYPE_MASK = 0x7f
XCB_PROPERTY_NOTIFY = 28

XCB_INPUT_FOCUS_POINTER_ROOT = ctypes.c_uint8(1)


class LibXcb:
    """The library of functions."""
    __slots__ = (
        # xcb
        'xcb_connect', 'xcb_connection_has_error', 'xcb_disconnect',
        'xcb_screen_allowed_depths_iterator', 'xcb_depth_next',
        'xcb_depth_visuals_iterator', 'xcb_visualtype_next',
        'xcb_generate_id', 'xcb_free_pixmap', 'xcb_create_pixmap',
        'xcb_create_colormap', 'xcb_prefetch_extension_data',
        'xcb_create_window',
        'xcb_intern_atom_unchecked', 'xcb_intern_atom_reply',
        'xcb_get_selection_owner', 'xcb_get_selection_owner_reply',
        'xcb_set_selection_owner',
        'xcb_get_geometry', 'xcb_get_geometry_reply',
        'xcb_setup_roots_iterator', 'xcb_get_setup',
        'xcb_get_property', 'xcb_get_property_reply',
        'xcb_get_property_value_length', 'xcb_get_property_value',
        'xcb_change_property',
        'xcb_change_window_attributes',
        'xcb_send_event', 'xcb_wait_for_event', 'xcb_request_check',
        'xcb_change_window_attributes_checked', 'xcb_change_window_attributes',
        'xcb_prefetch_maximum_request_length',
        'xcb_grab_server', 'xcb_flush', 'xcb_ungrab_server',
        'xcb_set_input_focus', 'xcb_reparent_window',
        'xcb_query_tree_unchecked',

        # xcb variables
        'xcb_big_requests_id',
        
        # xcb-util
        'xcb_aux_get_screen', 'xcb_atom_name_by_screen',
        'xcb_aux_sync',

        # xcb-xtest
        'xcb_test_id',

        # xcb-randr
        'xcb_randr_id',

        # xcb-xinerama
        'xcb_xinerama_id',

        # xcb-shape
        'xcb_shape_id',

        # xcb-xfixes
        'xcb_xfixes_id',

        # xcb-cursor
        'xcb_cursor_context_new', 'xcb_cursor_context_free',

        # xcb-icccm
        'xcb_icccm_set_wm_class', 'xcb_icccm_set_wm_name',

        # cairo
        'cairo_xcb_surface_create', 'cairo_surface_status',
        'cairo_status_to_string', 'cairo_surface_finish',
        'cairo_surface_destroy',

        # libc
        '_free', 'strlen', 'memset',
    )

    def __init__(self) -> None:
        def get_lib(name: str) -> ctypes.CDLL:
            print(f"Loading {name}")
            try:
                return ctypes.cdll.LoadLibrary(name)
            except OSError as err:
                raise OSError(f'Could not load {name}; is it installed?') from err

        xcb = get_lib('libxcb.so.1')
        xcb_util = get_lib('libxcb-util.so.1')
        xcb_xtest = get_lib('libxcb-xtest.so.0')
        xcb_randr = get_lib('libxcb-randr.so.0')
        xcb_xinerama = get_lib('libxcb-xinerama.so.0')
        xcb_shape = get_lib('libxcb-shape.so.0')
        xcb_xfixes = get_lib('libxcb-xfixes.so.0')
        xcb_cursor = get_lib('libxcb-cursor.so.0')
        xcb_icccm = get_lib('libxcb-icccm.so.4')
        cairo = get_lib('libcairo.so.2')
        c_lib = get_lib('libc.so.6')

        self.xcb_connect: Callable[
            [ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)], XcbConnectionP,
        ] = xcb.xcb_connect
        self.xcb_connect.restype = XcbConnectionP
        self.xcb_connect.argtypes = (ctypes.c_char_p, ctypes.POINTER(ctypes.c_int))

        self.xcb_connection_has_error: Callable[
            [XcbConnectionP], ctypes.c_int,
        ] = xcb.xcb_connection_has_error
        self.xcb_connection_has_error.restype = ctypes.c_int
        self.xcb_connection_has_error.argtypes = (XcbConnectionP,)

        self.xcb_disconnect: Callable[
            [XcbConnectionP], None
        ] = xcb.xcb_disconnect
        self.xcb_disconnect.restype = None
        self.xcb_disconnect.argtypes = (XcbConnectionP,)

        # connection, screen number -> screen info
        self.xcb_aux_get_screen: Callable[
            [XcbConnectionP, ctypes.c_int], XcbScreenP,
        ] = xcb_util.xcb_aux_get_screen
        self.xcb_aux_get_screen.restype = XcbScreenP
        self.xcb_aux_get_screen.argtypes = (XcbConnectionP, ctypes.c_int)

        # base, screen
        self.xcb_atom_name_by_screen: Callable[
            [ctypes.c_char_p, ctypes.c_uint8], ctypes.c_char_p,
        ] = xcb_util.xcb_atom_name_by_screen
        self.xcb_atom_name_by_screen.restype = ctypes.c_char_p
        self.xcb_atom_name_by_screen.argtypes = (ctypes.c_char_p, ctypes.c_uint8)

        self.xcb_aux_sync: Callable[
            [XcbConnectionP], None
        ] = xcb_util.xcb_aux_sync
        self.xcb_aux_sync.restype = None
        self.xcb_aux_sync.argtypes = (XcbConnectionP,)

        self.xcb_screen_allowed_depths_iterator: Callable[
            [XcbScreenP], XcbDepthIterator,
        ] = xcb.xcb_screen_allowed_depths_iterator
        self.xcb_screen_allowed_depths_iterator.restype = XcbDepthIterator
        self.xcb_screen_allowed_depths_iterator.argtypes = (XcbScreenP,)

        self.xcb_depth_next: Callable[
            [XcbDepthIteratorP], None,
        ] = xcb.xcb_depth_next
        self.xcb_depth_next.restype = None
        self.xcb_depth_next.argtypes = (XcbDepthIteratorP,)

        self.xcb_depth_visuals_iterator: Callable[
            [XcbDepthP], XcbVisualtypeIterator,
        ] = xcb.xcb_depth_visuals_iterator
        self.xcb_depth_visuals_iterator.restype = XcbVisualtypeIterator
        self.xcb_depth_visuals_iterator.argtypes = (XcbDepthP,)

        self.xcb_visualtype_next: Callable[
            [XcbVisualtypeIteratorP], None,
        ] = xcb.xcb_visualtype_next
        self.xcb_visualtype_next.restype = None
        self.xcb_visualtype_next.argtypes = (XcbVisualtypeIteratorP,)

        self.xcb_generate_id: Callable[
            [XcbConnectionP], ctypes.c_uint32,
        ] = xcb.xcb_generate_id
        self.xcb_generate_id.restype = ctypes.c_uint32
        self.xcb_generate_id.argtypes = (XcbConnectionP,)

        self.xcb_create_colormap: Callable[
            [XcbConnectionP, ctypes.c_uint8, XcbColormap, XcbWindow, XcbVisualid], XcbVoidCookie
        ] = xcb.xcb_create_colormap
        self.xcb_create_colormap.restype = XcbVoidCookie
        self.xcb_create_colormap.argtypes = (
            XcbConnectionP, ctypes.c_uint8, XcbColormap, XcbWindow, XcbVisualid,
        )

        self.xcb_prefetch_extension_data: Callable[
            [XcbConnectionP, XcbExtensionP], None
        ] = xcb.xcb_prefetch_extension_data
        self.xcb_prefetch_extension_data.restype = None
        self.xcb_prefetch_extension_data.argtypes = (XcbConnectionP, XcbExtensionP)

        # connection, depth, pid, drawable, width, height -> cookie
        self.xcb_create_pixmap: Callable[
            [
                XcbConnectionP, ctypes.c_uint8, XcbPixmap, XcbDrawable,
                ctypes.c_uint16, ctypes.c_uint16,
            ], XcbVoidCookie,
        ] = xcb.xcb_create_pixmap
        self.xcb_create_pixmap.restype = XcbVoidCookie
        self.xcb_create_pixmap.argtypes = (
            XcbConnectionP, ctypes.c_uint8, XcbPixmap, XcbDrawable,
            ctypes.c_uint16, ctypes.c_uint16,
        )

        self.xcb_free_pixmap: Callable[
            [XcbConnectionP, XcbPixmap], None,
        ] = xcb.xcb_free_pixmap
        self.xcb_free_pixmap.restype = None
        self.xcb_free_pixmap.argtypes = (XcbConnectionP, XcbPixmap)

        # connection, depth, wid, parent, x, y, width, height,
        # border_width, class, _visual, value_mask, *value_list
        self.xcb_create_window: Callable[
            [
                XcbConnectionP, ctypes.c_uint8,
                XcbWindow, XcbWindow,
                ctypes.c_int16, ctypes.c_int16,
                ctypes.c_uint16, ctypes.c_uint16,
                ctypes.c_uint16, ctypes.c_uint16,
                XcbVisualid, ctypes.c_int32,
                ctypes.c_void_p,
            ], XcbVoidCookie,
        ] = xcb.xcb_create_window
        self.xcb_create_window.restype = XcbVoidCookie
        self.xcb_create_window.argtypes = (
            XcbConnectionP, ctypes.c_uint8,
            XcbWindow, XcbWindow,
            ctypes.c_int16, ctypes.c_int16,
            ctypes.c_uint16, ctypes.c_uint16,
            ctypes.c_uint16, ctypes.c_uint16,
            XcbVisualid, ctypes.c_int32,
            ctypes.c_void_p,
        )

        # connection, only_if_exists, name_len, name -> atom
        self.xcb_intern_atom_unchecked: Callable[
            [XcbConnectionP, ctypes.c_uint8, ctypes.c_uint16, ctypes.c_char_p],
            XcbInternAtomCookie,
        ] = xcb.xcb_intern_atom_unchecked
        self.xcb_intern_atom_unchecked.restype = XcbInternAtomCookie
        self.xcb_intern_atom_unchecked.argtypes = (
            XcbConnectionP, ctypes.c_uint8, ctypes.c_uint16, ctypes.c_char_p,
        )

        self.xcb_intern_atom_reply: Callable[
            [XcbConnectionP, XcbInternAtomCookie, XcbGenericErrorPP], XcbInternAtomReplyP,
        ] = xcb.xcb_intern_atom_reply
        self.xcb_intern_atom_reply.restype = XcbInternAtomReplyP
        self.xcb_intern_atom_reply.argtypes = (
            XcbConnectionP, XcbInternAtomCookie, XcbGenericErrorPP,
        )

        self.xcb_get_selection_owner: Callable[
            [XcbConnectionP, XcbAtom], XcbGetSelectionOwnerCookie,
        ] = xcb.xcb_get_selection_owner
        self.xcb_get_selection_owner.restype = XcbGetSelectionOwnerCookie
        self.xcb_get_selection_owner.argtypes = (XcbConnectionP, XcbAtom)

        self.xcb_get_selection_owner_reply: Callable[
            [XcbConnectionP, XcbGetSelectionOwnerCookie, XcbGenericErrorPP],
            XcbGetSelectionOwnerReplyP,
        ] = xcb.xcb_get_selection_owner_reply
        self.xcb_get_selection_owner_reply.restype = XcbGetSelectionOwnerReplyP
        self.xcb_get_selection_owner_reply.argtypes = (
            XcbConnectionP, XcbGetSelectionOwnerCookie, XcbGenericErrorPP,
        )

        self.xcb_set_selection_owner: Callable[
            [XcbConnectionP, XcbWindow, XcbAtom, XcbTimestamp], XcbVoidCookie,
        ] = xcb.xcb_set_selection_owner
        self.xcb_set_selection_owner.restype = XcbVoidCookie
        self.xcb_set_selection_owner.argtypes = (
            XcbConnectionP, XcbWindow, XcbAtom, XcbTimestamp,
        )

        self.xcb_get_geometry: Callable[
            [XcbConnectionP, XcbDrawable], XcbGetGeometryCookie,
        ] = xcb.xcb_get_geometry
        self.xcb_get_geometry.restype = XcbGetGeometryCookie
        self.xcb_get_geometry.argtypes = (XcbConnectionP, XcbDrawable)

        self.xcb_get_geometry_reply: Callable[
            [XcbConnectionP, XcbGetGeometryCookie, XcbGenericErrorPP], XcbGetGeometryReplyP,
        ] = xcb.xcb_get_geometry_reply
        self.xcb_get_geometry_reply.restype = XcbGetGeometryReplyP
        self.xcb_get_geometry_reply.argtypes = (
            XcbConnectionP, XcbGetGeometryCookie, XcbGenericErrorPP,
        )

        self.xcb_setup_roots_iterator: Callable[
            [XcbSetupP], XcbScreenIterator,
        ] = xcb.xcb_setup_roots_iterator
        self.xcb_setup_roots_iterator.restype = XcbScreenIterator
        self.xcb_setup_roots_iterator.argtypes = ()

        self.xcb_get_setup: Callable[
            [XcbConnectionP], XcbSetupP
        ] = xcb.xcb_get_setup
        self.xcb_get_setup.restype = XcbSetupP
        self.xcb_get_setup.argtypes = (XcbConnectionP,)

        # connection, _delete, window, property, type, long_offset, long_length -> cookie
        self.xcb_get_property: Callable[
            [
                XcbConnectionP, ctypes.c_uint8, XcbWindow, XcbAtom,
                XcbAtom, ctypes.c_uint32, ctypes.c_uint32,
            ], XcbGetPropertyCookie,
        ] = xcb.xcb_get_property
        self.xcb_get_property.restype = XcbGetPropertyCookie
        self.xcb_get_property.argtypes = (
            XcbConnectionP, ctypes.c_uint8, XcbWindow, XcbAtom,
            XcbAtom, ctypes.c_uint32, ctypes.c_uint32,
        )

        self.xcb_get_property_reply: Callable[
            [XcbConnectionP, XcbGetPropertyCookie, XcbGenericErrorPP], XcbGetPropertyReplyP,
        ] = xcb.xcb_get_property_reply
        self.xcb_get_property_reply.restype = XcbGetPropertyReplyP
        self.xcb_get_property_reply.argtypes = (
            XcbConnectionP, XcbGetPropertyCookie, XcbGenericErrorPP,
        )

        self.xcb_get_property_value_length: Callable[
            [XcbGetPropertyReplyP], ctypes.c_int,
        ] = xcb.xcb_get_property_value_length
        self.xcb_get_property_value_length.restype = ctypes.c_int
        self.xcb_get_property_value_length.argtypes = (XcbGetPropertyReplyP,)

        # void * xcb_get_property_value (const xcb_get_property_reply_t *R);
        self.xcb_get_property_value: Callable[
            [XcbGetPropertyReplyP], ctypes.c_void_p,
        ] = xcb.xcb_get_property_value
        self.xcb_get_property_value.restype = ctypes.c_void_p
        self.xcb_get_property_value.argtypes = (XcbGetPropertyReplyP,)

        # connection, mode, window, property, type, format, data_len, data
        self.xcb_change_property: Callable[
            [
                XcbConnectionP, ctypes.c_uint8, XcbWindow, XcbAtom, XcbAtom,
                ctypes.c_uint8, ctypes.c_uint32, ctypes.c_void_p,
            ],
            XcbVoidCookie,
        ] = xcb.xcb_change_property
        self.xcb_change_property.restype = XcbVoidCookie
        self.xcb_change_property.argtypes = (
            XcbConnectionP, ctypes.c_uint8, XcbWindow, XcbAtom, XcbAtom,
            ctypes.c_uint8, ctypes.c_uint32, ctypes.c_void_p,
        )

        self.xcb_change_window_attributes: Callable[
            [XcbConnectionP, XcbWindow, ctypes.c_uint32, ctypes.c_void_p], XcbVoidCookie,
        ] = xcb.xcb_change_window_attributes
        self.xcb_change_window_attributes.restype = XcbVoidCookie
        self.xcb_change_window_attributes.argtypes = (
            XcbConnectionP, XcbWindow, ctypes.c_uint32, ctypes.c_void_p,
        )

        self.xcb_prefetch_maximum_request_length: Callable[
            [XcbConnectionP], None,
        ] = xcb.xcb_prefetch_maximum_request_length
        self.xcb_prefetch_maximum_request_length.restype = None
        self.xcb_prefetch_maximum_request_length.argtypes = (XcbConnectionP,)

        self.xcb_grab_server: Callable[
            [XcbConnectionP], XcbVoidCookie,
        ] = xcb.xcb_grab_server
        self.xcb_grab_server.restype = XcbVoidCookie
        self.xcb_grab_server.argtypes = (XcbConnectionP,)

        self.xcb_ungrab_server: Callable[
            [XcbConnectionP], XcbVoidCookie,
        ] = xcb.xcb_ungrab_server
        self.xcb_ungrab_server.restype = XcbVoidCookie
        self.xcb_ungrab_server.argtypes = (XcbConnectionP,)

        # connection, revert_to, focus, time -> cookie
        self.xcb_set_input_focus: Callable[
            [XcbConnectionP, ctypes.c_uint8, XcbWindow, XcbTimestamp], XcbVoidCookie,
        ] = xcb.xcb_set_input_focus
        self.xcb_set_input_focus.restype = XcbVoidCookie
        self.xcb_set_input_focus.argtypes = (
            XcbConnectionP, ctypes.c_uint8, XcbWindow, XcbTimestamp,
        )

        self.xcb_query_tree_unchecked: Callable[
            [XcbConnectionP, XcbWindow], XcbQueryTreeCookie,
        ] = xcb.xcb_query_tree_unchecked
        self.xcb_query_tree_unchecked.restype = XcbQueryTreeCookie
        self.xcb_query_tree_unchecked.argtypes = (XcbConnectionP, XcbWindow)

        # connection, window, parent, x, y -> cookie
        self.xcb_reparent_window: Callable[
            [XcbConnectionP, XcbWindow, XcbWindow, ctypes.c_int16, ctypes.c_int16], XcbVoidCookie,
        ] = xcb.xcb_reparent_window
        self.xcb_reparent_window.restype = XcbVoidCookie
        self.xcb_reparent_window.argtypes = (
            XcbConnectionP, XcbWindow, XcbWindow, ctypes.c_int16, ctypes.c_int16,
        )

        self.xcb_flush: Callable[
            [XcbConnectionP], ctypes.c_int,
        ] = xcb.xcb_flush
        self.xcb_flush.restype = ctypes.c_int
        self.xcb_flush.argtypes = (XcbConnectionP,)

        # connection, propagate, destination, event_mask, event -> cookie
        self.xcb_send_event: Callable[
            [
                XcbConnectionP, ctypes.c_uint8, XcbWindow, ctypes.c_uint32, ctypes.c_char_p,
            ], XcbVoidCookie,
        ] = xcb.xcb_send_event
        self.xcb_send_event.restype = XcbVoidCookie
        self.xcb_send_event.argtypes = (
            XcbConnectionP, ctypes.c_uint8, XcbWindow, ctypes.c_uint32, ctypes.c_char_p,
        )

        self.xcb_wait_for_event: Callable[
            [XcbConnectionP], XcbGenericEventP,
        ] = xcb.xcb_wait_for_event
        self.xcb_wait_for_event.restype = XcbGenericEventP
        self.xcb_wait_for_event.argtypes = (XcbConnectionP,)

        # xcb_generic_error_t *xcb_request_check(xcb_connection_t *c, xcb_void_cookie_t cookie);
        self.xcb_request_check: Callable[
            [XcbConnectionP, XcbVoidCookie], XcbGenericEventP,
        ] = xcb.xcb_request_check
        self.xcb_request_check.restype = XcbGenericEventP
        self.xcb_request_check.argtypes = ()

        # connection, window, value_mask, value_list -> cookie
        self.xcb_change_window_attributes_checked: Callable[
            [XcbConnectionP, XcbWindow, ctypes.c_uint32, ctypes.c_void_p], XcbVoidCookie,
        ] = xcb.xcb_change_window_attributes_checked
        self.xcb_change_window_attributes_checked.restype = XcbVoidCookie
        self.xcb_change_window_attributes_checked.argtypes = (
            XcbConnectionP, XcbWindow, ctypes.c_uint32, ctypes.c_void_p,
        )

        # connection, window, value_mask, value_list -> cookie
        self.xcb_change_window_attributes: Callable[
            [XcbConnectionP, XcbWindow, ctypes.c_uint32, ctypes.c_void_p], XcbVoidCookie,
        ] = xcb.xcb_change_window_attributes
        self.xcb_change_window_attributes.restype = XcbVoidCookie
        self.xcb_change_window_attributes.argtypes = (
            XcbConnectionP, XcbWindow, ctypes.c_uint32, ctypes.c_void_p,
        )

        self.xcb_cursor_context_new: Callable[
            [XcbConnectionP, XcbScreenP, XcbCursorContextPP], ctypes.c_int,
        ] = xcb_cursor.xcb_cursor_context_new
        self.xcb_cursor_context_new.restype = ctypes.c_int
        self.xcb_cursor_context_new.argtypes = (XcbConnectionP, XcbScreenP, XcbCursorContextPP)

        self.xcb_cursor_context_free: Callable[
            [XcbCursorContextP], None,
        ] = xcb_cursor.xcb_cursor_context_free
        self.xcb_cursor_context_free.restype = None
        self.xcb_cursor_context_free.argtypes = (XcbCursorContextP,)

        # connection, window, class-length, class-name
        self.xcb_icccm_set_wm_class: Callable[
            [XcbConnectionP, XcbWindow, ctypes.c_uint32, ctypes.c_char_p],
            XcbVoidCookie,
        ] = xcb_icccm.xcb_icccm_set_wm_class
        self.xcb_icccm_set_wm_class.restype = XcbVoidCookie
        self.xcb_icccm_set_wm_class.argtypes = (
            XcbConnectionP, XcbWindow, ctypes.c_uint32, ctypes.c_char_p,
        )

        # connection, window, encoding, format, name-length, name
        self.xcb_icccm_set_wm_name: Callable[
            [XcbConnectionP, XcbWindow, XcbAtom, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_char_p],
            XcbVoidCookie,
        ] = xcb_icccm.xcb_icccm_set_wm_name
        self.xcb_icccm_set_wm_name.restype = XcbVoidCookie
        self.xcb_icccm_set_wm_name.argtypes = (
            XcbConnectionP, XcbWindow, XcbAtom, ctypes.c_uint8, ctypes.c_uint32, ctypes.c_char_p,
        )

        self.xcb_big_requests_id = ctypes.cast(xcb.xcb_big_requests_id, XcbExtensionP)
        self.xcb_test_id = ctypes.cast(xcb_xtest.xcb_test_id, XcbExtensionP)
        self.xcb_randr_id = ctypes.cast(xcb_randr.xcb_randr_id, XcbExtensionP)
        self.xcb_xinerama_id = ctypes.cast(xcb_xinerama.xcb_xinerama_id, XcbExtensionP)
        self.xcb_shape_id = ctypes.cast(xcb_shape.xcb_shape_id, XcbExtensionP)
        self.xcb_xfixes_id = ctypes.cast(xcb_xfixes.xcb_xfixes_id, XcbExtensionP)

        self.cairo_xcb_surface_create: Callable[
            [XcbConnectionP, XcbDrawable, XcbVisualtypeP, ctypes.c_int, ctypes.c_int],
            CairoSurfaceP,
        ] = cairo.cairo_xcb_surface_create
        self.cairo_xcb_surface_create.restype = CairoSurfaceP
        self.cairo_xcb_surface_create.argtypes = (
            # connection, drawable, visual, width, height
            XcbConnectionP, XcbDrawable, XcbVisualtypeP, ctypes.c_int, ctypes.c_int,
        )

        self.cairo_surface_status: Callable[
            [CairoSurfaceP], CairoStatus,
        ] = cairo.cairo_surface_status
        self.cairo_surface_status.restype = CairoStatus
        self.cairo_surface_status.argtypes = (CairoSurfaceP,)

        self.cairo_status_to_string: Callable[
            [CairoStatus], ctypes.c_char_p,
        ] = cairo.cairo_status_to_string
        self.cairo_status_to_string.restype = ctypes.c_char_p
        self.cairo_status_to_string.argtypes = (CairoStatus,)

        self.cairo_surface_finish: Callable[
            [CairoSurfaceP], None
        ] = cairo.cairo_surface_finish
        self.cairo_surface_finish.restype = None
        self.cairo_surface_finish.argtypes = (CairoSurfaceP,)

        self.cairo_surface_destroy: Callable[
            [CairoSurfaceP], None
        ] = cairo.cairo_surface_destroy
        self.cairo_surface_destroy.restype = None
        self.cairo_surface_destroy.argtypes = (CairoSurfaceP,)

        self._free: Callable[
            [ctypes.POINTER], None,
        ] = c_lib.free
        # self._free.restype = None
        # self._free.argtypes = (ctypes.POINTER(None),)

        self.strlen: Callable[
            [ctypes.c_char_p], ctypes.c_int,
        ] = c_lib.strlen
        self.strlen.restype = ctypes.c_int
        self.strlen.argtypes = (ctypes.c_char_p,)

        # pointer, value, size
        self.memset: Callable[
            [ctypes.POINTER, ctypes.c_uint8, ctypes.c_uint], None,
        ] = c_lib.memset
        self.memset.restype = None
        self.memset.argtypes = (ctypes.c_void_p, ctypes.c_int, ctypes.c_uint)

    # -----------------------------------------------------------------------
    # Helpers

    def free(self, ptr: Any) -> None:
        """Free memory."""
        if ptr is not None:
            if isinstance(ptr, (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_wchar_p)):
                self._free(ptr)
                # ptr.contents = None
            elif isinstance(ptr, object) and ptr.__class__.__name__.startswith('LP_'):
                self._free(ptr)
                # ptr.contents = None
            elif isinstance(ptr, (bytes, str, bytearray)):
                warnings.warn(f"Tried to free a {type(ptr)}")
            else:
                raise ValueError(f'Not a pointer: {ptr} ({type(ptr)})')

    def xcb_get_property_value_bytes(self, property_reply: XcbGetPropertyReplyP) -> bytes:
        data = self.xcb_get_property_value(property_reply)
        length = self.xcb_get_property_value_length(property_reply)
        as_bytes = ctypes.cast(data, ctypes.POINTER(ctypes.c_byte * as_py_int(length)))
        return bytes(as_bytes.contents)

    @staticmethod
    def get_xcb_event_response_type(evt: XcbGenericEventP) -> int:
        if not evt:
            return 0
        response_type = t_cast(int, evt.contents.response_type)
        return response_type & XCB_EVENT_RESPONSE_TYPE_MASK

    @staticmethod
    def is_xcb_event_response_type(evt: XcbGenericEventP, event_id: int) -> bool:
        return LibXcb.get_xcb_event_response_type(evt) == event_id


"""
import petronia_native_x11.libs.xcb.impl                                                                                                                                                                                                                                          
xcb = petronia_native_x11.libs.xcb.impl.Xcb()

import os, ctypes
libnames = []
for f in os.listdir("/usr/lib"):
  if (
        f.startswith("libxcb")
        or f.startswith('libcairo')
  ) and ".so." in f:
    libnames.append(f)

libs = {}
for libn in libnames:
  print(f"loading {libn}")
  try:
    lib = ctypes.cdll.LoadLibrary(libn)
    libs[libn] = lib
  except OSError:
    print(f"failed to load {libn}")

def find_id(nid):
    for name, lib in libs.items():
      if hasattr(lib, nid):
        print(f"{nid}: {name}")

"""
