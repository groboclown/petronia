"""Definitions from xcb.h"""

import sys
import ctypes

# This should be the opaque type xcb_connection_t, which is always used as a pointer,
#   but because it's opaque, we'll just reference it as a void pointer.
XcbConnectionPtr = ctypes.c_void_p

# This should be the opaque type xcb_extension_t
XcbExtensionPtr = ctypes.c_void_p


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


# typedef uint32_t xcb_window_t;
XcbWindow = ctypes.c_uint32
# typedef uint32_t xcb_colormap_t;
XcbColormap = ctypes.c_uint32
# typedef uint32_t xcb_visualid_t;
XcbVisualid = ctypes.c_uint32


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

        # uint8_t pad0[4];
        ('pad0_0', ctypes.c_uint8),
        ('pad0_1', ctypes.c_uint8),
        ('pad0_2', ctypes.c_uint8),
        ('pad0_3', ctypes.c_uint8),
    ]


XcbVisualtypeP = ctypes.POINTER(XcbVisualtype)


class XcbVisualtypeIterator(ctypes.Structure):
    """xproto xcb_visualtype_iterator_t structure"""
    _fields_ = [
        ('data', XcbVisualtypeP),
        ('rem', ctypes.c_int),
        ('index', ctypes.c_int),
    ]


class XcbDepth(ctypes.Structure):
    """xproto xcb_depth_t structure"""
    _fields_ = [
        ('depth', ctypes.c_uint8),
        ('pad0', ctypes.c_uint8),
        ('visuals_len', ctypes.c_uint16),

        # uint8_t pad0[4];
        ('pad0_0', ctypes.c_uint8),
        ('pad0_1', ctypes.c_uint8),
        ('pad0_2', ctypes.c_uint8),
        ('pad0_3', ctypes.c_uint8),
    ]


XcbDepthP = ctypes.POINTER(XcbDepth)


class XcbDepthIterator(ctypes.Structure):
    """xproto xcb_depth_iterator_t structure"""
    _fields_ = [
        ('data', XcbDepthP),
        ('rem', ctypes.c_int),
        ('index', ctypes.c_int),
    ]
