"""Types for xcb (and xproto)"""

import ctypes

# typedef uint32_t xcb_window_t;
XcbWindow = ctypes.c_uint32

# typedef uint32_t xcb_colormap_t;
XcbColormap = ctypes.c_uint32

# typedef uint32_t xcb_visualid_t;
XcbVisualid = ctypes.c_uint32

# typedef uint8_t xcb_keycode_t;
XcbKeycode = ctypes.c_uint8
XcbKeycodeP = ctypes.POINTER(XcbKeycode)

# typedef uint32_t xcb_keysym_t;
XcbKeysym = ctypes.c_uint32
XcbKeysymP = ctypes.POINTER(XcbKeysym)

# typedef uint32_t xcb_atom_t;
XcbAtom = ctypes.c_uint32

# typedef uint32_t xcb_drawable_t;
XcbDrawable = ctypes.c_uint32

# typedef uint32_t xcb_gcontext_t;
XcbGContext = ctypes.c_uint32

# typedef uint32_t xcb_pixmap_t;
XcbPixmap = ctypes.c_uint32

# typedef uint32_t xcb_timestamp_t;
XcbTimestamp = ctypes.c_uint32

# typedef uint8_t xcb_button_t;
XcbButton = ctypes.c_uint8


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

# xcb_get_keyboard_mapping_cookie_t
XcbGetKeyboardMappingCookie = XcbVoidCookie

# xcb_get_modifier_mapping_cookie_t
XcbGetModifierMappingCookie = XcbVoidCookie


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


class XcbGetKeyboardMappingReply(ctypes.Structure):
    """xcb_get_keyboard_mapping_reply_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('keysyms_per_keycode', ctypes.c_uint8),
        ('sequence', ctypes.c_uint16),
        ('length', ctypes.c_uint32),
        ('pad0', ctypes.c_uint8 * 24),
    ]


XcbGetKeyboardMappingReplyP = ctypes.POINTER(XcbGetKeyboardMappingReply)


class XcbGetModifierMappingReply(ctypes.Structure):
    """xcb_get_modifier_mapping_reply_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('keycodes_per_modifier', ctypes.c_uint8),
        ('sequence', ctypes.c_uint16),
        ('length', ctypes.c_uint32),
        ('pad0', ctypes.c_uint8 * 24),
    ]


XcbGetModifierMappingReplyP = ctypes.POINTER(XcbGetModifierMappingReply)


class XcbKeyPressEvent(ctypes.Structure):
    """xcb_key_press_event_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('detail', XcbKeycode),
        ('sequence', ctypes.c_uint16),
        ('time', XcbTimestamp),
        ('root', XcbWindow),
        ('event', XcbWindow),
        ('child', XcbWindow),
        ('root_x', ctypes.c_int16),
        ('root_y', ctypes.c_int16),
        ('event_x', ctypes.c_int16),
        ('event_y', ctypes.c_int16),
        ('state', ctypes.c_uint16),
        ('same_screen', ctypes.c_uint8),
        ('pad0', ctypes.c_uint8),
    ]


XcbKeyPressEventP = ctypes.POINTER(XcbKeyPressEvent)
# typedef xcb_key_press_event_t xcb_key_release_event_t;
XcbKeyReleaseEvent = XcbKeyPressEvent
XcbKeyReleaseEventP = ctypes.POINTER(XcbKeyReleaseEvent)


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


XcbClientMessageEventP = ctypes.POINTER(XcbClientMessageEvent)


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


class XcbExposeEvent(ctypes.Structure):
    """xcb_expose_event_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('pad0', ctypes.c_uint8),
        ('sequence', ctypes.c_uint16),
        ('window', XcbWindow),
        ('x', ctypes.c_uint16),
        ('y', ctypes.c_uint16),
        ('width', ctypes.c_uint16),
        ('height', ctypes.c_uint16),
        ('x', ctypes.c_uint16),
        ('count', ctypes.c_uint16),
        ('pad1', ctypes.c_uint8 * 2),
    ]


XcbExposeEventP = ctypes.POINTER(XcbExposeEvent)


class XcbButtonPressEvent(ctypes.Structure):
    """xcb_button_press_event_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('detail', XcbButton),
        ('sequence', ctypes.c_uint16),
        ('time', XcbTimestamp),
        ('root', XcbWindow),
        ('event', XcbWindow),
        ('child', XcbWindow),
        ('root_x', ctypes.c_int16),
        ('root_y', ctypes.c_int16),
        ('event_x', ctypes.c_int16),
        ('event_y', ctypes.c_int16),
        ('state', ctypes.c_uint16),
        ('same_screen', ctypes.c_uint8),
        ('pad0', ctypes.c_uint8),
    ]


XcbButtonPressEventP = ctypes.POINTER(XcbButtonPressEvent)
# typedef xcb_button_press_event_t xcb_button_release_event_t;
XcbButtonReleaseEvent = XcbButtonPressEvent
XcbButtonReleaseEventP = ctypes.POINTER(XcbButtonReleaseEvent)


class XcbMotionNotifyEvent(ctypes.Structure):
    """xcb_motion_notify_event_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('detail', ctypes.c_uint8),
        ('sequence', ctypes.c_uint16),
        ('time', XcbTimestamp),
        ('root', XcbWindow),
        ('event', XcbWindow),
        ('child', XcbWindow),
        ('root_x', ctypes.c_int16),
        ('root_y', ctypes.c_int16),
        ('event_x', ctypes.c_int16),
        ('event_y', ctypes.c_int16),
        ('state', ctypes.c_uint16),
        ('same_screen', ctypes.c_uint8),
        ('pad0', ctypes.c_uint8),
    ]


XcbMotionNotifyEventP = ctypes.POINTER(XcbMotionNotifyEvent)


class XcbEnterNotifyEvent(ctypes.Structure):
    """xcb_enter_notify_event_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('detail', ctypes.c_uint8),
        ('sequence', ctypes.c_uint16),
        ('time', XcbTimestamp),
        ('root', XcbWindow),
        ('event', XcbWindow),
        ('child', XcbWindow),
        ('root_x', ctypes.c_int16),
        ('root_y', ctypes.c_int16),
        ('event_x', ctypes.c_int16),
        ('event_y', ctypes.c_int16),
        ('state', ctypes.c_uint16),
        ('mode', ctypes.c_uint8),
        ('same_screen', ctypes.c_uint8),
    ]


XcbEnterNotifyEventP = ctypes.POINTER(XcbEnterNotifyEvent)

# typedef xcb_enter_notify_event_t xcb_leave_notify_event_t;
XcbLeaveNotifyEvent = XcbEnterNotifyEvent
XcbLeaveNotifyEventP = ctypes.POINTER(XcbLeaveNotifyEvent)


class XcbKeymapNotifyEvent(ctypes.Structure):
    """xcb_keymap_notify_event_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('keys', ctypes.c_uint8 * 31),
    ]


XcbKeymapNotifyEventP = ctypes.POINTER(XcbKeymapNotifyEvent)


class XcbCreateNotifyEvent(ctypes.Structure):
    """xcb_create_notify_event_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('pad0', ctypes.c_uint8),
        ('sequence', ctypes.c_uint16),
        ('window', XcbWindow),
        ('x', ctypes.c_int16),
        ('y', ctypes.c_int16),
        ('width', ctypes.c_uint16),
        ('height', ctypes.c_uint16),
        ('border_width', ctypes.c_uint16),
        ('override_redirect', ctypes.c_uint8),
        ('pad1', ctypes.c_uint8),
    ]


XcbCreateNotifyEventP = ctypes.POINTER(XcbCreateNotifyEvent)


class XcbDestroyNotifyEvent(ctypes.Structure):
    """xcb_destroy_notify_event_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('pad0', ctypes.c_uint8),
        ('sequence', ctypes.c_uint16),
        ('event', XcbWindow),
        ('window', XcbWindow),
    ]


XcbDestroyNotifyEventP = ctypes.POINTER(XcbDestroyNotifyEvent)


class XcbUnmapNotifyEvent(ctypes.Structure):
    """xcb_unmap_notify_event_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('pad0', ctypes.c_uint8),
        ('sequence', ctypes.c_uint16),
        ('event', XcbWindow),
        ('window', XcbWindow),
        ('from_configure', ctypes.c_uint8),
        ('pad1', ctypes.c_uint8 * 3),
    ]


XcbUnmapNotifyEventP = ctypes.POINTER(XcbUnmapNotifyEvent)


class XcbMapNotifyEvent(ctypes.Structure):
    """xcb_map_notify_event_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('pad0', ctypes.c_uint8),
        ('sequence', ctypes.c_uint16),
        ('event', XcbWindow),
        ('window', XcbWindow),
        ('override_redirect', ctypes.c_uint8),
        ('pad1', ctypes.c_uint8 * 3),
    ]


XcbMapNotifyEventP = ctypes.POINTER(XcbMapNotifyEvent)


class XcbMapRequestEvent(ctypes.Structure):
    """xcb_map_request_event_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('pad0', ctypes.c_uint8),
        ('sequence', ctypes.c_uint16),
        ('parent', XcbWindow),
        ('window', XcbWindow),
    ]


XcbMapRequestEventP = ctypes.POINTER(XcbMapRequestEvent)


class XcbReparentNotifyEvent(ctypes.Structure):
    """xcb_reparent_notify_event_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('pad0', ctypes.c_uint8),
        ('sequence', ctypes.c_uint16),
        ('event', XcbWindow),
        ('window', XcbWindow),
        ('parent', XcbWindow),
        ('x', ctypes.c_int16),
        ('y', ctypes.c_int16),
        ('override_redirect', ctypes.c_uint8),
        ('pad1', ctypes.c_uint8 * 3),
    ]


XcbReparentNotifyEventP = ctypes.POINTER(XcbReparentNotifyEvent)


class XcbConfigureNotifyEvent(ctypes.Structure):
    """xcb_configure_notify_event_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('pad0', ctypes.c_uint8),
        ('sequence', ctypes.c_uint16),
        ('event', XcbWindow),
        ('window', XcbWindow),
        ('above_sibling', XcbWindow),
        ('x', ctypes.c_int16),
        ('y', ctypes.c_int16),
        ('width', ctypes.c_uint16),
        ('height', ctypes.c_uint16),
        ('border_width', ctypes.c_uint16),
        ('override_redirect', ctypes.c_uint8),
        ('pad1', ctypes.c_uint8),
    ]


XcbConfigureNotifyEventP = ctypes.POINTER(XcbConfigureNotifyEvent)


class XcbConfigureRequestEvent(ctypes.Structure):
    """xcb_configure_request_event_t"""
    _fields_ = [
        ('response_type', ctypes.c_uint8),
        ('stack_mode', ctypes.c_uint8),
        ('sequence', ctypes.c_uint16),
        ('parent', XcbWindow),
        ('window', XcbWindow),
        ('sibling', XcbWindow),
        ('x', ctypes.c_int16),
        ('y', ctypes.c_int16),
        ('width', ctypes.c_uint16),
        ('height', ctypes.c_uint16),
        ('border_width', ctypes.c_uint16),
        ('value_mask', ctypes.c_uint16),
    ]


XcbConfigureRequestEventP = ctypes.POINTER(XcbConfigureRequestEvent)


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
