"""Definitions from xcb.h and xproto.h.  Translates native names into local names.

And other xcb libraries, and cairo.

The functions are loaded into a class object to retain typing.

See:

https://xcb.freedesktop.org/PublicApi/
https://xcb.freedesktop.org/manual/xproto_8h_source.html
https://xcb.freedesktop.org/manual/xcb_8h_source.html
"""

from typing import Sequence, Callable
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
        'xcb_prefetch_maximum_request_length',
        'xcb_grab_server', 'xcb_flush', 'xcb_ungrab_server',
        'xcb_set_input_focus', 'xcb_reparent_window',
        'xcb_query_tree_unchecked',

        # xcb variables
        'xcb_big_requests_id',
    )

    def __init__(self) -> None:
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

        # connection, depth, wid, parent, x, y, width, height,
        # border_width, class, _visual, value_mask, *value_list
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
            xxx
        )

        self.xcb_map_window: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbWindow], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        # connection, context id, drawable, value mask, value list -> cookie
        self.xcb_create_gc: Callable[
            [
                xcb_types.XcbConnectionP, xcb_types.XcbGContext, xcb_types.XcbDrawable, ctypes.c_uint32, ctypes.c_void_p,
            ],
            XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        # connection, only_if_exists, name_len, name -> atom
        self.xcb_intern_atom_unchecked: Callable[
            [xcb_types.XcbConnectionP, ctypes.c_uint8, ctypes.c_uint16, ctypes.c_char_p],
            xcb_types.XcbInternAtomCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_intern_atom_reply: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbInternAtomCookie, xcb_types.XcbGenericErrorPP], xcb_types.XcbInternAtomReplyP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_get_selection_owner: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbAtom], xcb_types.XcbGetSelectionOwnerCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_get_selection_owner_reply: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbGetSelectionOwnerCookie, xcb_types.XcbGenericErrorPP],
            xcb_types.XcbGetSelectionOwnerReplyP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_set_selection_owner: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbWindow, xcb_types.XcbAtom, xcb_types.XcbTimestamp], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_get_geometry: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbDrawable], xcb_types.XcbGetGeometryCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_get_geometry_reply: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbGetGeometryCookie, xcb_types.XcbGenericErrorPP], xcb_types.XcbGetGeometryReplyP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_setup_roots_iterator: Callable[
            [xcb_types.XcbSetupP], xcb_types.XcbScreenIterator,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
        )

        self.xcb_get_setup: Callable[
            [xcb_types.XcbConnectionP], xcb_types.XcbSetupP
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        # connection, _delete, window, property, type, long_offset, long_length -> cookie
        self.xcb_get_property: Callable[
            [
                xcb_types.XcbConnectionP, ctypes.c_uint8, xcb_types.XcbWindow, xcb_types.XcbAtom,
                xcb_types.XcbAtom, ctypes.c_uint32, ctypes.c_uint32,
            ], xcb_types.XcbGetPropertyCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_get_property_reply: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbGetPropertyCookie, xcb_types.XcbGenericErrorPP], xcb_types.XcbGetPropertyReplyP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_get_property_value_length: Callable[
            [xcb_types.XcbGetPropertyReplyP], ctypes.c_int,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
        )

        # void * xcb_get_property_value (const xcb_get_property_reply_t *R);
        self.xcb_get_property_value: Callable[
            [xcb_types.XcbGetPropertyReplyP], ctypes.c_void_p,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
        )

        # connection, mode, window, property, type, format, data_len, data
        self.xcb_change_property: Callable[
            [
                xcb_types.XcbConnectionP, ctypes.c_uint8, xcb_types.XcbWindow, xcb_types.XcbAtom, xcb_types.XcbAtom,
                ctypes.c_uint8, ctypes.c_uint32, ctypes.c_void_p,
            ],
            xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_change_window_attributes: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbWindow, ctypes.c_uint32, ctypes.c_void_p], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_prefetch_maximum_request_length: Callable[
            [xcb_types.XcbConnectionP], None,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_grab_server: Callable[
            [xcb_types.XcbConnectionP], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_ungrab_server: Callable[
            [xcb_types.XcbConnectionP], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        # connection, revert_to, focus, time -> cookie
        self.xcb_set_input_focus: Callable[
            [xcb_types.XcbConnectionP, ctypes.c_uint8, xcb_types.XcbWindow, xcb_types.XcbTimestamp], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_query_tree_unchecked: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbWindow], xcb_types.XcbQueryTreeCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        # connection, window, parent, x, y -> cookie
        self.xcb_reparent_window: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbWindow, xcb_types.XcbWindow, ctypes.c_int16, ctypes.c_int16], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_flush: Callable[
            [xcb_types.XcbConnectionP], ctypes.c_int,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        # connection, propagate, destination, event_mask, event -> cookie
        self.xcb_send_event: Callable[
            [
                xcb_types.XcbConnectionP, ctypes.c_uint8, xcb_types.XcbWindow, ctypes.c_uint32, ctypes.c_char_p,
            ], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_wait_for_event: Callable[
            [xcb_types.XcbConnectionP], xcb_types.XcbGenericEventP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        self.xcb_poll_for_event: Callable[
            [xcb_types.XcbConnectionP], xcb_types.XcbGenericEventP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        # xcb_generic_error_t *xcb_request_check(xcb_connection_t *c, xcb_void_cookie_t cookie);
        self.xcb_request_check: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbVoidCookie], xcb_types.XcbGenericEventP,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        # connection, window, value_mask, value_list -> cookie
        self.xcb_change_window_attributes_checked: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbWindow, ctypes.c_uint32, ctypes.c_void_p], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
        )

        # connection, window, value_mask, value_list -> cookie
        self.xcb_change_window_attributes: Callable[
            [xcb_types.XcbConnectionP, xcb_types.XcbWindow, ctypes.c_uint32, ctypes.c_void_p], xcb_types.XcbVoidCookie,
        ] = ct_util.as_typed_call(
            self.__problems, xcb_res, '',
            returns=x,
            connection=xcb_types.XcbConnectionP,
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
