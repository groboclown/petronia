"""An experiment to create the simplest window manager setup.  Used for reference."""

from typing import Dict, List
import ctypes
import time
from petronia_native_x11.libs import (
    libc, ct_util,
    libxcb, libxcb_types, libxcb_consts,
)


def main() -> None:
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
    # depth_data = xcb.xcb_screen_allowed_depths_iterator(screen).data
    # visual = xcb.xcb_depth_visuals_iterator(depth_data).data
    # default_depth = depth_data.contents.depth

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

    window_frames: Dict[int, libxcb_types.XcbWindow] = {}
    generated_frames: List[libxcb_types.XcbWindow] = []

    def setup_window(window: libxcb_types.XcbWindow, on_startup: bool) -> None:
        attribute_cookie = xcb.xcb_get_window_attributes_unchecked(conn, window)
        geom_cookie = xcb.xcb_get_geometry(conn, window)
        attributes = xcb.xcb_get_window_attributes_reply(
            conn, attribute_cookie, libxcb_consts.NULL__XcbGenericErrorPP,
        )
        geom = xcb.xcb_get_geometry_reply(
            conn, geom_cookie, libxcb_consts.NULL__XcbGenericErrorPP,
        )
        try:
            if not attributes:
                return
            if ct_util.as_py_int(attributes.contents.override_redirect) == 1:
                # Do nothing with these windows.
                return
            map_state = ct_util.as_py_int(attributes.contents.map_state)
            if (
                    (on_startup and map_state != libxcb_consts.XCB_MAP_STATE_VIEWABLE)
                    or (not on_startup and map_state == libxcb_consts.XCB_MAP_STATE_UNVIEWABLE)
            ):
                # Not displayable
                return
            # ensure when we exit it's restored
            xcb.xcb_change_save_set(conn, libxcb_consts.XCB_SET_MODE_INSERT__c, window)

            # TODO ALL BELOW HERE ISN'T WORKING

            new_frame_id = xcb.xcb_generate_id(conn)
            window_frames[ct_util.as_py_int(window)] = new_frame_id
            generated_frames.append(new_frame_id)
            pos_x = 0  # ct_util.as_py_int(geom.contents.x)
            pos_y = 0  # ct_util.as_py_int(geom.contents.y)
            pos_w = 800  # ct_util.as_py_int(geom.contents.width)
            pos_h = 600  # ct_util.as_py_int(geom.contents.height)
            pos_bw = 2  # ct_util.as_py_int(geom.contents.border_width)
            print(
                f" - putting window {window} at ({pos_x}, {pos_y}) sized "
                f"({pos_w}, {pos_h}) border {pos_bw}"
            )
            xcb.xcb_create_window(
                conn, screen.contents.root_depth, new_frame_id, screen.contents.root,
                # x, y, width, height, border width
                ctypes.c_int16(pos_x), ctypes.c_int16(pos_y),
                ctypes.c_uint16(pos_w), ctypes.c_uint16(pos_h), ctypes.c_uint16(pos_bw),
                libxcb_consts.XCB_COPY_FROM_PARENT__c, screen.contents.root_visual,

                # Value Mask
                ctypes.c_int32(
                    libxcb_consts.XCB_CW_BORDER_PIXEL
                    | libxcb_consts.XCB_CW_BIT_GRAVITY
                    | libxcb_consts.XCB_CW_WIN_GRAVITY
                    | libxcb_consts.XCB_CW_OVERRIDE_REDIRECT
                    | libxcb_consts.XCB_CW_EVENT_MASK
                    | libxcb_consts.XCB_CW_COLORMAP
                ),

                # Values
                ct_util.as_int32_list(
                    screen.contents.black_pixel,
                    libxcb_consts.XCB_GRAVITY_NORTH_WEST__c,
                    libxcb_consts.XCB_GRAVITY_NORTH_WEST__c,
                    ctypes.c_int32(0),  # override; set to 1?

                    # register for key events on F and event window.
                    ctypes.c_int32(
                        libxcb_consts.XCB_EVENT_MASK_STRUCTURE_NOTIFY
                        # | libxcb_consts.XCB_EVENT_MASK_ENTER_WINDOW
                        # | libxcb_consts.XCB_EVENT_MASK_LEAVE_WINDOW
                        # | libxcb_consts.XCB_EVENT_MASK_EXPOSURE
                        | libxcb_consts.XCB_EVENT_MASK_SUBSTRUCTURE_REDIRECT
                        # | libxcb_consts.XCB_EVENT_MASK_POINTER_MOTION
                        # | libxcb_consts.XCB_EVENT_MASK_BUTTON_PRESS
                        # | libxcb_consts.XCB_EVENT_MASK_BUTTON_RELEASE
                    ),
                    ctypes.c_int32(colormap),
                ),
            )
            reparent_cookie = xcb.xcb_reparent_window(
                conn, window, new_frame_id,
                ctypes.c_int16(0), ctypes.c_int16(0),  # relative x,y position in the frame.
            )
            if xcb.xcb_request_check(conn, reparent_cookie):
                print("Failed to reparent")
                xcb.xcb_destroy_window(conn, new_frame_id)
                return
            xcb.xcb_map_window(conn, new_frame_id)

            xcb.xcb_configure_window(
                conn, window, ctypes.c_uint16(
                    libxcb_consts.XCB_CONFIG_WINDOW_X
                    | libxcb_consts.XCB_CONFIG_WINDOW_Y
                    | libxcb_consts.XCB_CONFIG_WINDOW_WIDTH
                    | libxcb_consts.XCB_CONFIG_WINDOW_HEIGHT
                    | libxcb_consts.XCB_CONFIG_WINDOW_BORDER_WIDTH
                ), ct_util.as_int32_list(
                    ctypes.c_int32(pos_x), ctypes.c_int32(pos_y),
                    ctypes.c_int32(pos_w), ctypes.c_int32(pos_h),
                    ctypes.c_int32(pos_bw),
                ),
            )
            xcb.xcb_flush(conn)

        finally:
            clib.force_free(geom)
            clib.force_free(attributes)

    # Could at this point probe all existing clients and add them.
    screen_tree_cookie = xcb.xcb_query_tree_unchecked(conn, screen.contents.root)
    trees = xcb.xcb_query_tree_reply(
        conn, screen_tree_cookie, libxcb_consts.NULL__XcbGenericErrorPP,
    )
    window_count = ct_util.as_py_int(xcb.xcb_query_tree_children_length(trees))
    tree_windows = xcb.xcb_query_tree_children(trees)
    for idx in range(0, window_count):
        setup_window(tree_windows[idx], True)
    clib.force_free(trees)

    # Event loop
    running = True
    while running:
        event = xcb.xcb_poll_for_event(conn)
        if not event:
            # No more immediate events.
            time.sleep(0.01)
            continue
        try:
            response_type = ct_util.as_py_int(event.contents.response_type) & ~0x80
            print(f"X event type {response_type}")
            if response_type == libxcb_consts.XCB_CREATE_NOTIFY:
                # Don't need to do anything.
                print(" - create; ignoring")
                pass
            elif response_type == libxcb_consts.XCB_MAP_REQUEST:
                map_evt = ctypes.cast(event, libxcb_types.XcbMapRequestEventP)
                if map_evt.contents.window not in generated_frames:
                    print(" - mapping request")
                    setup_window(map_evt.contents.window, False)
            elif response_type == libxcb_consts.XCB_UNMAP_NOTIFY:
                unmap_evt = ctypes.cast(event, libxcb_types.XcbUnmapNotifyEventP)
                if unmap_evt.contents.window in generated_frames:
                    continue
                window_id = ct_util.as_py_int(unmap_evt.contents.window)
                frame_id = window_frames.get(window_id)
                if frame_id:
                    print(" - unmapping")
                    xcb.xcb_unmap_window(conn, frame_id)
                    xcb.xcb_reparent_window(
                        conn, unmap_evt.contents.window, screen.contents.root,
                        ctypes.c_int16(0), ctypes.c_int16(0),
                    )
                    # should remove from save set...
                    xcb.xcb_change_save_set(
                        conn, libxcb_consts.XCB_SET_MODE_DELETE__c, unmap_evt.contents.window,
                    )
                    xcb.xcb_destroy_window(conn, frame_id)
                    del window_frames[window_id]
                    if frame_id in generated_frames:
                        generated_frames.remove(frame_id)
            elif response_type == libxcb_consts.XCB_DESTROY_NOTIFY:
                dst_evt = ctypes.cast(event, libxcb_types.XcbDestroyNotifyEventP)
                window_id = ct_util.as_py_int(dst_evt.contents.window)
                frame_id = window_frames.get(window_id)
                if frame_id:
                    print(" - destroy window")
                    xcb.xcb_destroy_window(conn, frame_id)
                    del window_frames[window_id]
                    if frame_id in generated_frames:
                        generated_frames.remove(frame_id)
            elif response_type == libxcb_consts.XCB_CONFIGURE_REQUEST:
                cfg_evt = ctypes.cast(event, libxcb_types.XcbConfigureRequestEventP)
                window_id = ct_util.as_py_int(cfg_evt.contents.window)
                if window_id not in window_frames:
                    print(" - config - allowing change")
                    # Not managed yet, let these pass.
                    value_mask = ct_util.as_py_int(cfg_evt.contents.value_mask)
                    resp_mask = 0
                    resp_list: List[ctypes.c_int32] = []

                    # Note: order of bit checking is extremely important.
                    if value_mask & libxcb_consts.XCB_CONFIG_WINDOW_X != 0:
                        resp_mask |= libxcb_consts.XCB_CONFIG_WINDOW_X
                        resp_list.append(cfg_evt.contents.x)
                    if value_mask & libxcb_consts.XCB_CONFIG_WINDOW_Y != 0:
                        resp_mask |= libxcb_consts.XCB_CONFIG_WINDOW_Y
                        resp_list.append(cfg_evt.contents.y)
                    if value_mask & libxcb_consts.XCB_CONFIG_WINDOW_WIDTH != 0:
                        resp_mask |= libxcb_consts.XCB_CONFIG_WINDOW_WIDTH
                        resp_list.append(cfg_evt.contents.width)
                    if value_mask & libxcb_consts.XCB_CONFIG_WINDOW_HEIGHT != 0:
                        resp_mask |= libxcb_consts.XCB_CONFIG_WINDOW_HEIGHT
                        resp_list.append(cfg_evt.contents.height)
                    if value_mask & libxcb_consts.XCB_CONFIG_WINDOW_BORDER_WIDTH != 0:
                        resp_mask |= libxcb_consts.XCB_CONFIG_WINDOW_BORDER_WIDTH
                        resp_list.append(cfg_evt.contents.border_width)
                    if value_mask & libxcb_consts.XCB_CONFIG_WINDOW_SIBLING != 0:
                        resp_mask |= libxcb_consts.XCB_CONFIG_WINDOW_SIBLING
                        resp_list.append(cfg_evt.contents.sibling)
                    if value_mask & libxcb_consts.XCB_CONFIG_WINDOW_STACK_MODE != 0:
                        resp_mask |= libxcb_consts.XCB_CONFIG_WINDOW_STACK_MODE
                        resp_list.append(cfg_evt.contents.stack_mode)
                    xcb.xcb_configure_window(
                        conn, cfg_evt.contents.window,
                        ctypes.c_uint16(resp_mask), ct_util.as_int32_list(*resp_list),
                    )
            else:
                print(" - config; ignoring")
        finally:
            clib.force_free(event)


if __name__ == '__main__':
    main()
