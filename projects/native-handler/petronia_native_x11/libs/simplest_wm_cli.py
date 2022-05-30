"""An experiment to create the simplest window manager setup.  Used for reference."""

import ctypes
import time
from petronia_native_x11.libs import (
    libc, ct_util,
    libxcb, libxcb_types, libxcb_consts,
)


def main():
    # Setup
    xcb_res = libxcb.load_libxcb()
    clib_res = libc.load_libc()
    if xcb_res.has_error or clib_res.has_error:
        return
    xcb = xcb_res.result
    clib = clib_res.result
    default_screen = ctypes.c_int(0)

    # Connect
    conn = xcb.xcb_connect(ct_util.NULL__c_char_p, ctypes.byref(default_screen))
    error_code = xcb.xcb_connection_has_error(conn)
    if error_code != 0:
        print(f"Failed to connect: {error_code}")
        return

    # Get screen
    screen = xcb.xcb_setup_roots_iterator(xcb.xcb_get_setup(conn)).data
    colormap = screen.contents.default_colormap

    # Become the window manager & capture all the events we want.
    cookie = xcb.xcb_change_window_attributes_checked(
        conn, screen.contents.root,
        libxcb_consts.XCB_CW_EVENT_MASK__c,
        ct_util.as_uint32_list(
            # Just one value, masking together all the events to capture.
            ctypes.c_uint32(
                # This one makes us the window manager
                libxcb_consts.XCB_EVENT_MASK_SUBSTRUCTURE_REDIRECT

                # All the other things that are interesting.
                | libxcb_consts.XCB_EVENT_MASK_SUBSTRUCTURE_NOTIFY
                | libxcb_consts.XCB_EVENT_MASK_ENTER_WINDOW
                | libxcb_consts.XCB_EVENT_MASK_LEAVE_WINDOW
                | libxcb_consts.XCB_EVENT_MASK_STRUCTURE_NOTIFY
                | libxcb_consts.XCB_EVENT_MASK_BUTTON_PRESS
                | libxcb_consts.XCB_EVENT_MASK_BUTTON_RELEASE
                | libxcb_consts.XCB_EVENT_MASK_BUTTON_MOTION
                | libxcb_consts.XCB_EVENT_MASK_KEY_PRESS
                | libxcb_consts.XCB_EVENT_MASK_KEY_RELEASE
                | libxcb_consts.XCB_EVENT_MASK_KEYMAP_STATE
                # | libxcb_consts.XCB_EVENT_MASK_POINTER_MOTION
                # | libxcb_consts.XCB_EVENT_MASK_POINTER_MOTION_HINT
                | libxcb_consts.XCB_EVENT_MASK_BUTTON_1_MOTION
                | libxcb_consts.XCB_EVENT_MASK_BUTTON_2_MOTION
                | libxcb_consts.XCB_EVENT_MASK_BUTTON_3_MOTION
                | libxcb_consts.XCB_EVENT_MASK_BUTTON_4_MOTION
                | libxcb_consts.XCB_EVENT_MASK_BUTTON_5_MOTION
                | libxcb_consts.XCB_EVENT_MASK_BUTTON_MOTION
                | libxcb_consts.XCB_EVENT_MASK_EXPOSURE
                | libxcb_consts.XCB_EVENT_MASK_FOCUS_CHANGE
                | libxcb_consts.XCB_EVENT_MASK_PROPERTY_CHANGE
                | libxcb_consts.XCB_EVENT_MASK_COLOR_MAP_CHANGE
            ),
        ),
    )
    err = xcb.xcb_request_check(conn, cookie)
    if err:
        print("Failed becoming window manager")
        return

    # Event loop
    running = True
    while running:
        event = xcb.xcb_poll_for_event(conn)
        if not event:
            # No more immediate events.
            time.sleep(0.01)
            continue
        response_type = ct_util.as_py_int(event.contents.response_type) & ~0x80
        print(f"X event type {response_type} (raw: {event.contents.response_type})")
        clib.force_free(event)


if __name__ == '__main__':
    main()
