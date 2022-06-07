"""Definitions from xcb.h and xproto.h.  Translates native names into local names.

And other xcb libraries, and cairo.

The functions are loaded into a class object to retain typing.

See:

https://xcb.freedesktop.org/PublicApi/
https://xcb.freedesktop.org/manual/xproto_8h_source.html
https://xcb.freedesktop.org/manual/xcb_8h_source.html
"""

from typing import Sequence, List, Callable
from typing import cast as t_cast
import ctypes
from petronia_common.util import PetroniaReturnError, StdRet, T
from . import xcb_types, xcb_consts
from .. import ct_util


class LibXcb:
    """The library of functions."""
    __slots__ = (
        '__problems',

        'xcb_connect', 'xcb_connection_has_error', 'xcb_disconnect',
        'xcb_screen_allowed_depths_iterator', 'xcb_depth_next',
        'xcb_depth_visuals_iterator', 'xcb_visualtype_next',
        'xcb_generate_id', 'xcb_free_pixmap', 'xcb_create_pixmap',
        'xcb_create_colormap', 'xcb_prefetch_extension_data',
        'xcb_create_window', 'xcb_map_window', 'xcb_create_gc',
        'xcb_intern_atom_unchecked', 'xcb_intern_atom_reply',
        'xcb_get_selection_owner', 'xcb_get_selection_owner_reply',
        'xcb_set_selection_owner',
        'xcb_get_geometry', 'xcb_get_geometry_reply',
        'xcb_setup_roots_iterator', 'xcb_get_setup',
        'xcb_get_property', 'xcb_get_property_reply',
        'xcb_get_property_value_length', 'xcb_get_property_value',
        'xcb_change_property',
        'xcb_change_window_attributes',
        'xcb_send_event', 'xcb_wait_for_event', 'xcb_poll_for_event', 'xcb_request_check',
        'xcb_change_window_attributes_checked', 'xcb_change_window_attributes',
        'xcb_get_window_attributes_unchecked', 'xcb_get_window_attributes_reply',
        'xcb_prefetch_maximum_request_length',
        'xcb_grab_server', 'xcb_flush', 'xcb_ungrab_server',
        'xcb_set_input_focus', 'xcb_configure_window',
        'xcb_reparent_window', 'xcb_reparent_window_checked',
        'xcb_change_save_set',
        'xcb_query_tree_unchecked', 'xcb_query_tree_reply',
        'xcb_query_tree_children_length', 'xcb_query_tree_children',
        'xcb_get_keyboard_mapping_reply', 'xcb_get_keyboard_mapping',
        'xcb_get_keyboard_mapping_keysyms',
        'xcb_get_modifier_mapping', 'xcb_get_modifier_mapping_reply',
        'xcb_get_modifier_mapping_keycodes',
        'xcb_unmap_window', 'xcb_destroy_window',

        # xcb variables
        'xcb_big_requests_id',
    )

    def __init__(self) -> None:
        self.__problems: List[PetroniaReturnError] = []
        xcb_res = ct_util.load_lib('libxcb.so.1')
        self.xcb_connect: Callable[
            [ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)], xcb_types.XcbConnectionP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_connect',
            returns=xcb_types.XcbConnectionP,
            display=ctypes.c_char_p,
            screen=ctypes.POINTER(ctypes.c_int),
        )

        self.xcb_connection_has_error: Callable[
            [xcb_types.XcbConnectionP], ctypes.c_int,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_connection_has_error',
            returns=ctypes.c_int,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_disconnect: Callable[
            [xcb_types.XcbConnectionP], None
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_disconnect',
            returns=None,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_screen_allowed_depths_iterator: Callable[
            [xcb_types.XcbScreenP], xcb_types.XcbDepthIterator,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_screen_allowed_depths_iterator',
            returns=xcb_types.XcbDepthIterator,
            screen=xcb_types.XcbScreenP,
        )

        self.xcb_depth_next: Callable[
            [xcb_types.XcbDepthIteratorP], None,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_depth_next',
            returns=None,
            iter=xcb_types.XcbDepthIteratorP,
        )

        self.xcb_depth_visuals_iterator: Callable[
            [xcb_types.XcbDepthP], xcb_types.XcbVisualtypeIterator,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_depth_visuals_iterator',
            returns=xcb_types.XcbVisualtypeIterator,
            depth=xcb_types.XcbDepthP,
        )

        self.xcb_visualtype_next: Callable[
            [xcb_types.XcbVisualtypeIteratorP], None,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_visualtype_next',
            returns=None,
            iter=xcb_types.XcbVisualtypeIteratorP,
        )

        self.xcb_generate_id: Callable[
            [xcb_types.XcbConnectionP], ctypes.c_uint32,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_generate_id',
            returns=ctypes.c_uint32,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_create_colormap: Callable[
            [
                xcb_types.XcbConnectionP, ctypes.c_uint8,
                xcb_types.XcbColormap, xcb_types.XcbWindow, xcb_types.XcbVisualid,
            ], xcb_types.XcbVoidCookie
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_create_colormap',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
            alloc=ctypes.c_uint8,
            mid=xcb_types.XcbColormap,
            window=xcb_types.XcbWindow,
            visual=xcb_types.XcbVisualid,
        )

        self.xcb_prefetch_extension_data: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbExtensionP], None
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_prefetch_extension_data',
            returns=None,
            connection=xcb_types.XcbConnectionP,
            extension=xcb_types.XcbExtensionP,
        )

        self.xcb_create_pixmap: Callable[
            [
                xcb_types.XcbConnectionP, ctypes.c_uint8, xcb_types.XcbPixmap, xcb_types.XcbDrawable,
                ctypes.c_uint16, ctypes.c_uint16,
            ], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_create_pixmap',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
            depth=ctypes.c_uint8,
            pid=xcb_types.XcbPixmap,
            drawable=xcb_types.XcbDrawable,
            width=ctypes.c_uint16,
            height=ctypes.c_uint16,
        )

        self.xcb_free_pixmap: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbPixmap], None,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_free_pixmap',
            returns=None,
            connection=xcb_types.XcbConnectionP,
            pixmap=xcb_types.XcbPixmap,
        )

        self.xcb_create_window: Callable[
            [
                xcb_types.XcbConnectionP, ctypes.c_uint8,
                xcb_types.XcbWindow, xcb_types.XcbWindow,
                ctypes.c_int16, ctypes.c_int16,
                ctypes.c_uint16, ctypes.c_uint16,
                ctypes.c_uint16, ctypes.c_uint16,
                xcb_types.XcbVisualid, ctypes.c_int32,
                ctypes.c_void_p,
            ], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_create_window',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
            depth=ctypes.c_uint8,
            window=xcb_types.XcbWindow,
            parent=xcb_types.XcbWindow,
            x=ctypes.c_int16,
            y=ctypes.c_int16,
            width=ctypes.c_uint16,
            height=ctypes.c_uint16,
            border_width=ctypes.c_uint16,
            window_class=ctypes.c_uint16,
            visual=xcb_types.XcbVisualid,
            value_mask=ctypes.c_int32,
            value_list=ctypes.c_void_p,
        )

        self.xcb_map_window: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbWindow], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_map_window',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
            window=xcb_types.XcbWindow,
        )

        self.xcb_create_gc: Callable[
            [
                xcb_types.XcbConnectionP, xcb_types.XcbGContext,
                xcb_types.XcbDrawable, ctypes.c_uint32, ctypes.c_void_p,
            ],
            xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_create_gc',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
            context_id=xcb_types.XcbGContext,
            drawable=xcb_types.XcbDrawable,
            value_mask=ctypes.c_uint32,
            value_list=ctypes.c_void_p,
        )

        # connection, only_if_exists, name_len, name -> atom
        self.xcb_intern_atom_unchecked: Callable[
            [xcb_types.XcbConnectionP, ctypes.c_uint8, ctypes.c_uint16, ctypes.c_char_p],
            xcb_types.XcbInternAtomCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_intern_atom_unchecked',
            returns=xcb_types.XcbInternAtomCookie,
            connection=xcb_types.XcbConnectionP,
            only_if_exists=ctypes.c_uint8,
            name_len=ctypes.c_uint16,
            name=ctypes.c_char_p,
        )

        self.xcb_intern_atom_reply: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbInternAtomCookie, xcb_types.XcbGenericErrorPP],
            xcb_types.XcbInternAtomReplyP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_intern_atom_reply',
            returns=xcb_types.XcbInternAtomReplyP,
            connection=xcb_types.XcbConnectionP,
            request_cookie=xcb_types.XcbInternAtomCookie,
            error=xcb_types.XcbGenericErrorPP,
        )

        self.xcb_get_selection_owner: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbAtom], xcb_types.XcbGetSelectionOwnerCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_get_selection_owner',
            returns=xcb_types.XcbGetSelectionOwnerCookie,
            connection=xcb_types.XcbConnectionP,
            selection=xcb_types.XcbAtom,
        )

        self.xcb_get_selection_owner_reply: Callable[
            [
                xcb_types.XcbConnectionP, xcb_types.XcbGetSelectionOwnerCookie,
                xcb_types.XcbGenericErrorPP,
            ],
            xcb_types.XcbGetSelectionOwnerReplyP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_get_selection_owner_reply',
            returns=xcb_types.XcbGetSelectionOwnerReplyP,
            connection=xcb_types.XcbConnectionP,
            cookie=xcb_types.XcbGetSelectionOwnerCookie,
            error=xcb_types.XcbGenericErrorPP,
        )

        self.xcb_set_selection_owner: Callable[
            [
                xcb_types.XcbConnectionP, xcb_types.XcbWindow, xcb_types.XcbAtom,
                xcb_types.XcbTimestamp,
            ], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_set_selection_owner',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
            owner=xcb_types.XcbWindow,
            selection=xcb_types.XcbAtom,
            time=xcb_types.XcbTimestamp,
        )

        self.xcb_get_geometry: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbDrawable], xcb_types.XcbGetGeometryCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_get_geometry',
            returns=xcb_types.XcbGetGeometryCookie,
            connection=xcb_types.XcbConnectionP,
            drawable=xcb_types.XcbDrawable,
        )

        self.xcb_get_geometry_reply: Callable[
            [
                xcb_types.XcbConnectionP, xcb_types.XcbGetGeometryCookie,
                xcb_types.XcbGenericErrorPP,
            ], xcb_types.XcbGetGeometryReplyP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_get_geometry_reply',
            returns=xcb_types.XcbGetGeometryReplyP,
            connection=xcb_types.XcbConnectionP,
            cookie=xcb_types.XcbGetGeometryCookie,
            error=xcb_types.XcbGenericErrorPP,
        )

        self.xcb_setup_roots_iterator: Callable[
            [xcb_types.XcbSetupP], xcb_types.XcbScreenIterator,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_setup_roots_iterator',
            returns=xcb_types.XcbScreenIterator,
            setup=xcb_types.XcbSetupP,
        )

        self.xcb_get_setup: Callable[
            [xcb_types.XcbConnectionP], xcb_types.XcbSetupP
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_get_setup',
            returns=xcb_types.XcbSetupP,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_get_property: Callable[
            [
                xcb_types.XcbConnectionP, ctypes.c_uint8, xcb_types.XcbWindow, xcb_types.XcbAtom,
                xcb_types.XcbAtom, ctypes.c_uint32, ctypes.c_uint32,
            ], xcb_types.XcbGetPropertyCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_get_property',
            returns=xcb_types.XcbGetPropertyCookie,
            connection=xcb_types.XcbConnectionP,
            delete=ctypes.c_uint8,
            window=xcb_types.XcbWindow,
            property=xcb_types.XcbAtom,
            type=xcb_types.XcbAtom,
            long_offset=ctypes.c_uint32,
            long_length=ctypes.c_uint32,
        )

        self.xcb_get_property_reply: Callable[
            [
                xcb_types.XcbConnectionP,
                xcb_types.XcbGetPropertyCookie, xcb_types.XcbGenericErrorPP,
            ], xcb_types.XcbGetPropertyReplyP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_get_property_reply',
            returns=xcb_types.XcbGetPropertyReplyP,
            connection=xcb_types.XcbConnectionP,
            cookie=xcb_types.XcbGetPropertyCookie,
            error=xcb_types.XcbGenericErrorPP,
        )

        self.xcb_get_property_value_length: Callable[
            [xcb_types.XcbGetPropertyReplyP], ctypes.c_int,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_get_property_value_length',
            returns=ctypes.c_int,
            reply=xcb_types.XcbGetPropertyReplyP,
        )

        self.xcb_get_property_value: Callable[
            [xcb_types.XcbGetPropertyReplyP], ctypes.c_void_p,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_get_property_value',
            returns=ctypes.c_void_p,
            reply=xcb_types.XcbGetPropertyReplyP,
        )

        # connection, mode, window, property, type, format, data_len, data
        self.xcb_change_property: Callable[
            [
                xcb_types.XcbConnectionP, ctypes.c_uint8, xcb_types.XcbWindow,
                xcb_types.XcbAtom, xcb_types.XcbAtom,
                ctypes.c_uint8, ctypes.c_uint32, ctypes.c_void_p,
            ],
            xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_change_property',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
            mode=ctypes.c_uint8,
            window=xcb_types.XcbWindow,
            property=xcb_types.XcbAtom,
            type=xcb_types.XcbAtom,
            format=ctypes.c_uint8,  # number of bits per item in data, either 8, 16, or 32.
            data_len=ctypes.c_uint32,  # number of elements in the data array, not size.
            data=ctypes.c_void_p,
        )

        self.xcb_change_window_attributes: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbWindow, ctypes.c_uint32, ctypes.c_void_p],
            xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_change_window_attributes',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
            window=xcb_types.XcbWindow,
            value_mask=ctypes.c_uint32,
            value_list=ctypes.c_void_p,
        )

        self.xcb_prefetch_maximum_request_length: Callable[
            [xcb_types.XcbConnectionP], None,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_prefetch_maximum_request_length',
            returns=None,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_grab_server: Callable[
            [xcb_types.XcbConnectionP], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_grab_server',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_ungrab_server: Callable[
            [xcb_types.XcbConnectionP], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_ungrab_server',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_set_input_focus: Callable[
            [
                xcb_types.XcbConnectionP, ctypes.c_uint8,
                xcb_types.XcbWindow, xcb_types.XcbTimestamp,
            ], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_set_input_focus',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
            revert_to=ctypes.c_uint8,
            focus=xcb_types.XcbWindow,
            time=xcb_types.XcbTimestamp,
        )

        self.xcb_query_tree_unchecked: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbWindow], xcb_types.XcbQueryTreeCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_query_tree_unchecked',
            returns=xcb_types.XcbQueryTreeCookie,
            connection=xcb_types.XcbConnectionP,
            window=xcb_types.XcbWindow,
        )

        self.xcb_query_tree_reply: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbQueryTreeCookie, xcb_types.XcbGenericErrorPP],
            xcb_types.XcbQueryTreeReplyP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_query_tree_reply',
            returns=xcb_types.XcbQueryTreeReplyP,
            connection=xcb_types.XcbConnectionP,
            cookie=xcb_types.XcbQueryTreeCookie,
            error=xcb_types.XcbGenericErrorPP,
        )

        self.xcb_query_tree_children_length: Callable[
            [xcb_types.XcbQueryTreeReplyP], ctypes.c_int,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_query_tree_children_length',
            returns=ctypes.c_int,
            reply=xcb_types.XcbQueryTreeReplyP,
        )

        self.xcb_query_tree_children: Callable[
            [xcb_types.XcbQueryTreeReplyP], xcb_types.XcbWindowP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_query_tree_children',
            returns=xcb_types.XcbWindowP,
            reply=xcb_types.XcbQueryTreeReplyP,
        )

        self.xcb_reparent_window: Callable[
            [
                xcb_types.XcbConnectionP, xcb_types.XcbWindow, xcb_types.XcbWindow,
                ctypes.c_int16, ctypes.c_int16,
            ], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_reparent_window',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
            window=xcb_types.XcbWindow,
            parent=xcb_types.XcbWindow,
            x=ctypes.c_int16,
            y=ctypes.c_int16,
        )

        self.xcb_reparent_window_checked: Callable[
            [
                xcb_types.XcbConnectionP, xcb_types.XcbWindow, xcb_types.XcbWindow,
                ctypes.c_int16, ctypes.c_int16,
            ], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_reparent_window_checked',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
            window=xcb_types.XcbWindow,
            parent=xcb_types.XcbWindow,
            x=ctypes.c_int16,
            y=ctypes.c_int16,
        )

        self.xcb_configure_window: Callable[
            [
                xcb_types.XcbConnectionP,
                xcb_types.XcbWindow,
                ctypes.c_uint16,
                ctypes.c_void_p,
            ], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_configure_window',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
            window=xcb_types.XcbWindow,
            value_mask=ctypes.c_uint16,
            value_list=ctypes.c_void_p,
        )

        self.xcb_change_save_set: Callable[
            [
                xcb_types.XcbConnectionP, ctypes.c_uint8, xcb_types.XcbWindow,
            ], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_change_save_set',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
            mode=ctypes.c_uint8,
            window=xcb_types.XcbWindow,
        )

        self.xcb_flush: Callable[
            [xcb_types.XcbConnectionP], ctypes.c_int,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_flush',
            returns=ctypes.c_int,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_send_event: Callable[
            [
                xcb_types.XcbConnectionP, ctypes.c_uint8, xcb_types.XcbWindow,
                ctypes.c_uint32, ctypes.c_char_p,
            ], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_send_event',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
            propagate=ctypes.c_uint8,
            destination=xcb_types.XcbWindow,
            event_mask=ctypes.c_uint32,
            event=ctypes.c_char_p,
        )

        self.xcb_wait_for_event: Callable[
            [xcb_types.XcbConnectionP], xcb_types.XcbGenericEventP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_wait_for_event',
            returns=xcb_types.XcbGenericEventP,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_poll_for_event: Callable[
            [xcb_types.XcbConnectionP], xcb_types.XcbGenericEventP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_poll_for_event',
            returns=xcb_types.XcbGenericEventP,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_request_check: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbVoidCookie], xcb_types.XcbGenericEventP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_request_check',
            returns=xcb_types.XcbGenericEventP,
            connection=xcb_types.XcbConnectionP,
            cookie=xcb_types.XcbVoidCookie,
        )

        self.xcb_change_window_attributes_checked: Callable[
            [
                xcb_types.XcbConnectionP, xcb_types.XcbWindow,
                ctypes.c_uint32, ctypes.c_void_p,
            ], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_change_window_attributes_checked',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
            window=xcb_types.XcbWindow,
            value_mask=ctypes.c_uint32,
            value_list=ctypes.c_void_p,
        )

        self.xcb_change_window_attributes: Callable[
            [
                xcb_types.XcbConnectionP, xcb_types.XcbWindow,
                ctypes.c_uint32, ctypes.c_void_p,
            ], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_change_window_attributes',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
            window=xcb_types.XcbWindow,
            value_mask=ctypes.c_uint32,
            value_list=ctypes.c_void_p,
        )

        self.xcb_get_window_attributes_unchecked: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbWindow],
            xcb_types.XcbGetWindowAttributesCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_get_window_attributes_unchecked',
            returns=xcb_types.XcbGetWindowAttributesCookie,
            connection=xcb_types.XcbConnectionP,
            window=xcb_types.XcbWindow,
        )

        self.xcb_get_window_attributes_reply: Callable[
            [
                xcb_types.XcbConnectionP,
                xcb_types.XcbGetWindowAttributesCookie,
                xcb_types.XcbGenericErrorPP,
            ],
            xcb_types.XcbGetWindowAttributesReplyP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_get_window_attributes_reply',
            returns=xcb_types.XcbGetWindowAttributesReplyP,
            connection=xcb_types.XcbConnectionP,
            cookie=xcb_types.XcbGetWindowAttributesCookie,
            error=xcb_types.XcbGenericErrorPP,
        )

        self.xcb_get_keyboard_mapping_reply: Callable[
            [
                xcb_types.XcbConnectionP,
                xcb_types.XcbGetKeyboardMappingCookie,
                xcb_types.XcbGenericErrorPP,
            ], xcb_types.XcbGetKeyboardMappingReplyP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_get_keyboard_mapping_reply',
            returns=xcb_types.XcbGetKeyboardMappingReplyP,
            connection=xcb_types.XcbConnectionP,
            cookie=xcb_types.XcbGetKeyboardMappingCookie,
            errors=xcb_types.XcbGenericErrorPP,
        )

        self.xcb_get_keyboard_mapping: Callable[
            [
                xcb_types.XcbConnectionP, xcb_types.XcbKeycode, ctypes.c_uint8,
            ], xcb_types.XcbGetKeyboardMappingCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_get_keyboard_mapping',
            returns=xcb_types.XcbGetKeyboardMappingCookie,
            connection=xcb_types.XcbConnectionP,
            first_keycode=xcb_types.XcbKeycode,
            count=ctypes.c_uint8,
        )

        self.xcb_get_keyboard_mapping_keysyms: Callable[
            [xcb_types.XcbGetKeyboardMappingReplyP], xcb_types.XcbKeysymP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_get_keyboard_mapping_keysyms',
            returns=xcb_types.XcbKeysymP,
            reply=xcb_types.XcbGetKeyboardMappingReplyP,
        )

        self.xcb_get_modifier_mapping: Callable[
            [xcb_types.XcbConnectionP], xcb_types.XcbGetModifierMappingCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_get_modifier_mapping',
            returns=xcb_types.XcbGetModifierMappingCookie,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_get_modifier_mapping_reply: Callable[
            [
                xcb_types.XcbConnectionP, xcb_types.XcbGetModifierMappingCookie,
                xcb_types.XcbGenericErrorPP,
            ],
            xcb_types.XcbGetModifierMappingReplyP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_get_modifier_mapping_reply',
            returns=xcb_types.XcbGetModifierMappingReplyP,
            connection=xcb_types.XcbConnectionP,
            cookie=xcb_types.XcbGetModifierMappingCookie,
            error=xcb_types.XcbGenericErrorPP,
        )

        self.xcb_get_modifier_mapping_keycodes: Callable[
            [xcb_types.XcbGetModifierMappingReplyP], xcb_types.XcbKeycodeP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_get_modifier_mapping_keycodes',
            returns=xcb_types.XcbKeycodeP,
            reply=xcb_types.XcbGetModifierMappingReplyP,
        )

        self.xcb_unmap_window: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbWindow], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_unmap_window',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
            window=xcb_types.XcbWindow,
        )

        self.xcb_destroy_window: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbWindow], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, 'xcb_destroy_window',
            returns=xcb_types.XcbVoidCookie,
            connection=xcb_types.XcbConnectionP,
            window=xcb_types.XcbWindow,
        )

        self.xcb_big_requests_id = ct_util.as_library_extern(
            self.__problems, xcb_res, 'xcb_big_requests_id',
            xcb_types.XcbExtensionP,
        )

    @property
    def problems(self) -> Sequence[PetroniaReturnError]:
        return tuple(self.__problems)

    def _setup_res(self, res: StdRet[T]) -> None:
        if res.has_error:
            self.__problems.append(res.valid_error)

    # -----------------------------------------------------------------------
    # Helpers

    def xcb_get_property_value_bytes(self, property_reply: xcb_types.XcbGetPropertyReplyP) -> bytes:
        data = self.xcb_get_property_value(property_reply)
        length = self.xcb_get_property_value_length(property_reply)
        as_bytes = ctypes.cast(data, ctypes.POINTER(ctypes.c_byte * ct_util.as_py_int(length)))
        return bytes(as_bytes.contents)

    @staticmethod
    def get_xcb_event_response_type(evt: xcb_types.XcbGenericEventP) -> int:
        if not evt:
            return 0
        response_type = t_cast(int, evt.contents.response_type)
        return response_type & xcb_consts.XCB_EVENT_RESPONSE_TYPE_MASK

    @staticmethod
    def is_xcb_event_response_type(evt: xcb_types.XcbGenericEventP, event_id: int) -> bool:
        return LibXcb.get_xcb_event_response_type(evt) == event_id


def load_libxcb() -> StdRet[LibXcb]:
    """Load the library."""
    ret = LibXcb()
    if ret.problems:
        return StdRet.pass_error(*ret.problems)
    return StdRet.pass_ok(ret)
