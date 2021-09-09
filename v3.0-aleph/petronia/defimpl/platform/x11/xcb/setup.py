"""
General connection and setup functions.
"""

from typing import List, Iterator, Optional
import ctypes
from .xcb_types import (
    xcb_lib,
    xcb_auth_info_t,
    xcb_setup_t,
    xcb_screen_iterator_t,
    xcb_connection_t,
    xcb_screen_t,
    XcbConnection,
)

# Static setup
if xcb_lib:
    # xcb_connection_t *xcb_connect(const char *displayname, int *screenp);
    xcb_lib.xcb_connect.restype = xcb_connection_t
    xcb_lib.xcb_connect.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)]

    # xcb_connection_t *xcb_connect_to_fd(int fd, xcb_auth_info_t *auth_info);
    xcb_lib.xcb_connect_to_fd.restype = ctypes.c_void_p
    xcb_lib.xcb_connect_to_fd.argtypes = [ctypes.c_int, ctypes.POINTER(xcb_auth_info_t)]

    # xcb_connection_t *xcb_connect_to_display_with_auth_info(const char *display, xcb_auth_info_t *auth, int *screen);
    xcb_lib.xcb_connect_to_display_with_auth_info.restype = ctypes.c_void_p
    xcb_lib.xcb_connect_to_display_with_auth_info.argtypes = [
        ctypes.c_char_p, ctypes.POINTER(xcb_auth_info_t), ctypes.POINTER(ctypes.c_int)
    ]

    # void xcb_disconnect(xcb_connection_t *c);
    xcb_lib.xcb_disconnect.restype = None
    xcb_lib.xcb_disconnect.argtypes = [ctypes.c_void_p]

    # int xcb_connection_has_error(xcb_connection_t *c);
    xcb_lib.xcb_connection_has_error.restype = ctypes.c_int
    xcb_lib.xcb_connection_has_error.argtypes = [ctypes.c_void_p]

    # const struct xcb_setup_t *xcb_get_setup(xcb_connection_t *c);
    xcb_lib.xcb_get_setup.restype = ctypes.POINTER(xcb_setup_t)
    xcb_lib.xcb_get_setup.argtypes = [ctypes.c_void_p]

    # int xcb_setup_roots_length (const xcb_setup_t *R);
    xcb_lib.xcb_setup_roots_length.restype = ctypes.c_int
    xcb_lib.xcb_setup_roots_length.argtypes = [ctypes.POINTER(xcb_setup_t)]

    # xcb_screen_iterator_t xcb_setup_roots_iterator (const xcb_setup_t *R);
    xcb_lib.xcb_setup_roots_iterator.restype = xcb_screen_iterator_t
    xcb_lib.xcb_setup_roots_iterator.argtypes = [ctypes.POINTER(xcb_setup_t)]

    # void xcb_screen_next (xcb_screen_iterator_t *i);
    xcb_lib.xcb_screen_next.restype = None
    xcb_lib.xcb_screen_next.argtypes = [ctypes.POINTER(xcb_screen_iterator_t)]


def connect_to_display(
        socket_fd: Optional[int] = None,
        display_name: Optional[str] = None,
        display_number: Optional[int] = None,
        authorization: Optional[str] = None,
) -> XcbConnection:
    assert xcb_lib

    auth: Optional[xcb_auth_info_t] = None
    if authorization:
        parts = authorization.split(':', 1)
        if len(parts) != 2:
            raise OSError('authorization must be in the form "name:data"')
        name_part = ctypes.create_string_buffer(parts[0].encode('utf-8'))
        data_part = ctypes.create_string_buffer(parts[1].encode('utf-8'))
        auth = xcb_auth_info_t(
            namelen=ctypes.sizeof(name_part),
            name=name_part,
            datalen=ctypes.sizeof(data_part),
            data=data_part,
        )

    display_num = ctypes.c_int()
    if display_number is not None:
        display_num.value = display_number
    if socket_fd is not None and socket_fd >= 0:
        connection = xcb_lib.xcb_connect_to_fd(socket_fd, ctypes.byref(auth))
    elif auth:
        connection = xcb_lib.xcb_connect_to_display_with_auth_info(
            display_name,
            ctypes.byref(auth),
            ctypes.byref(display_num),
        )
    else:
        connection = xcb_lib.xcb_connect(display_name, ctypes.byref(display_num))

    connection_error = xcb_lib.xcb_connection_has_error(connection)
    if connection_error != 0:
        raise OSError('Could not connect to {0}:{1} ({2})'.format(display_name, display_number, connection_error))
    try:
        setup = xcb_lib.xcb_get_setup(connection)
        # The setup pointer references data inside the connection object, so it
        # won't be garbage collected unless the connection is invalid, and must not be freed.
        return XcbConnection(connection, setup)
    except:
        xcb_lib.xcb_disconnect(connection)
        raise


def disconnect(connection: XcbConnection) -> None:
    assert xcb_lib

    xcb_lib.xcb_disconnect(connection.ptr)
    connection.was_disconnected()


def is_connection_valid(connection: XcbConnection) -> bool:
    assert xcb_lib

    return xcb_lib.xcb_connection_has_error(connection.ptr) == 0


def get_initial_screens(connection: XcbConnection) -> Iterator[xcb_screen_t]:
    """Returns the screens known at time of the connection creation.
    The randr must be used to get the dynamically changing screens.
    """
    assert xcb_lib

    root_count = xcb_lib.xcb_setup_roots_length()
    screen_iterator: xcb_screen_iterator_t = xcb_lib.xcb_setup_roots_iterator(connection.setup_ptr)
    ret: List[xcb_screen_t] = []
    if screen_iterator.data:
        ret.append(screen_iterator.data.contents)
    for i in range(1, root_count):
        xcb_lib.xcb_screen_next(ctypes.byref(screen_iterator))
        if screen_iterator.data:
            ret.append(screen_iterator.data.contents)
    return ret
