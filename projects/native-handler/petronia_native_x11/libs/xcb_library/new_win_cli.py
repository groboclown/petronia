"""Executable to try creating a window using these libraries."""

from typing import Sequence, Tuple, List
import ctypes
import time
from petronia_native_x11.libs import ct_util, libc
from petronia_native_x11.libs import libxcb as xcb_native
from petronia_native_x11.libs import libxcb_types as xcb_types
from petronia_native_x11.libs import libxcb_consts as xcb_consts

MASK_NAMES: Sequence[Tuple[int, str]] = (
    (xcb_consts.XCB_KEY_BUT_MASK_SHIFT, 'shift'),
    (xcb_consts.XCB_KEY_BUT_MASK_LOCK, 'lock'),
    (xcb_consts.XCB_KEY_BUT_MASK_CONTROL, 'control'),
    (xcb_consts.XCB_KEY_BUT_MASK_MOD_1, 'mod1'),
    (xcb_consts.XCB_KEY_BUT_MASK_MOD_2, 'mod2'),
    (xcb_consts.XCB_KEY_BUT_MASK_MOD_3, 'mod3'),
    (xcb_consts.XCB_KEY_BUT_MASK_MOD_4, 'mod4'),
    (xcb_consts.XCB_KEY_BUT_MASK_MOD_5, 'mod5'),
    (xcb_consts.XCB_KEY_BUT_MASK_BUTTON_1, 'button1'),
    (xcb_consts.XCB_KEY_BUT_MASK_BUTTON_2, 'button2'),
    (xcb_consts.XCB_KEY_BUT_MASK_BUTTON_3, 'button3'),
    (xcb_consts.XCB_KEY_BUT_MASK_BUTTON_4, 'button4'),
    (xcb_consts.XCB_KEY_BUT_MASK_BUTTON_5, 'button5'),
)


def name_modifiers(mask: ctypes.c_uint32) -> Sequence[str]:
    names: List[str] = []
    i_mask = ct_util.as_py_int(mask)
    for mod, name in MASK_NAMES:
        if (mod & i_mask) != 0:
            names.append(name)
    return names


def main() -> None:
    """ """
    libxcb_res = xcb_native.load_libxcb()
    if libxcb_res.has_error:
        print(libxcb_res.valid_error.messages())
        return
    xcb = libxcb_res.result
    libc_res = libc.load_libc()
    if libc_res.has_error:
        print(libc_res.valid_error.messages())
        return
    clib = libc_res.result
    connection = xcb.xcb_connect(ct_util.NULL__c_char_p, ct_util.NULL__int)
    screen = xcb.xcb_setup_roots_iterator(xcb.xcb_get_setup(connection)).data
    window = xcb.xcb_generate_id(connection)
    mask = xcb_consts.XCB_CW_BACK_PIXEL | xcb_consts.XCB_CW_EVENT_MASK
    xcb.xcb_create_window(
        connection,
        ctypes.c_uint8(0),  # depth
        window,
        screen.contents.root,  # parent window
        ctypes.c_int16(0), ctypes.c_int16(0),  # x, y
        ctypes.c_uint16(150), ctypes.c_uint16(150),  # width, height
        ctypes.c_uint16(10),  # border width
        ct_util.as_uint16(xcb_consts.XCB_WINDOW_CLASS_INPUT_OUTPUT),
        screen.contents.root_visual,
        ctypes.c_int32(mask), ct_util.as_uint32_list(
            ctypes.c_uint32(screen.contents.white_pixel),
            ctypes.c_uint32(
                    xcb_consts.XCB_EVENT_MASK_EXPOSURE
                    | xcb_consts.XCB_EVENT_MASK_BUTTON_PRESS
                    | xcb_consts.XCB_EVENT_MASK_BUTTON_RELEASE
                    | xcb_consts.XCB_EVENT_MASK_POINTER_MOTION
                    | xcb_consts.XCB_EVENT_MASK_ENTER_WINDOW
                    | xcb_consts.XCB_EVENT_MASK_LEAVE_WINDOW
                    | xcb_consts.XCB_EVENT_MASK_KEY_PRESS
                    | xcb_consts.XCB_EVENT_MASK_KEY_RELEASE
            ),
        )
    )

    xcb.xcb_map_window(connection, window)
    xcb.xcb_flush(connection)

    try:
        while True:
            # Note: signals like ctrl-c aren't interpreted until an event comes
            #   down the X wire.
            # event = xcb.xcb_wait_for_event(connection)
            # if not event:
            #     break
            event = xcb.xcb_poll_for_event(connection)
            if not event:
                time.sleep(0.1)
                continue
            response_type = ct_util.as_py_int(event.contents.response_type) & ~0x80
            if response_type == xcb_consts.XCB_EXPOSE:
                expose = ctypes.cast(event, xcb_types.XcbExposeEventP)
                print(
                    f"Window {expose.contents.window} exposed.  Redraw location "
                    f"({expose.contents.x}, {expose.contents.y}) sized "
                    f"({expose.contents.width}, {expose.contents.height})"
                )
            elif response_type == xcb_consts.XCB_BUTTON_PRESS:
                bpe = ctypes.cast(event, xcb_types.XcbButtonPressEventP)
                bp_detail = ct_util.as_py_int(bpe.contents.detail)
                if bp_detail == 4:
                    print(
                        f"Wheel button up in window {bpe.contents.event} at "
                        f"({bpe.contents.event_x}, {bpe.contents.event_y})"
                        f" with modifiers {name_modifiers(bpe.contents.state)}"
                    )
                elif bp_detail == 5:
                    print(
                        f"Wheel button down in window {bpe.contents.event} at "
                        f"({bpe.contents.event_x}, {bpe.contents.event_y})"
                        f" with modifiers {name_modifiers(bpe.contents.state)}"
                    )
                else:
                    print(
                        f"Button {bp_detail} pressed in {bpe.contents.event} at "
                        f"({bpe.contents.event_x}, {bpe.contents.event_y})"
                        f" with modifiers {name_modifiers(bpe.contents.state)}"
                    )
            elif response_type == xcb_consts.XCB_BUTTON_RELEASE:
                bre = ctypes.cast(event, xcb_types.XcbButtonReleaseEventP)
                br_detail = ct_util.as_py_int(bre.contents.detail)
                print(
                    f"Button {br_detail} released in window {bre.contents.event} at "
                    f"({bre.contents.event_x}, {bre.contents.event_y})"
                    f" with modifiers {name_modifiers(bre.contents.state)}"
                )
            elif response_type == xcb_consts.XCB_MOTION_NOTIFY:
                mne = ctypes.cast(event, xcb_types.XcbMotionNotifyEventP)
                print(
                    f"Mouse moved in window {mne.contents.event} at "
                    f"({mne.contents.event_x}, {mne.contents.event_y})"
                )
            elif response_type == xcb_consts.XCB_ENTER_NOTIFY:
                mee = ctypes.cast(event, xcb_types.XcbEnterNotifyEventP)
                print(
                    f"Mouse entered window {mee.contents.event} at "
                    f"({mee.contents.event_x}, {mee.contents.event_y})"
                )
            elif response_type == xcb_consts.XCB_LEAVE_NOTIFY:
                mle = ctypes.cast(event, xcb_types.XcbLeaveNotifyEventP)
                print(
                    f"Mouse left window {mle.contents.event} at "
                    f"({mle.contents.event_x}, {mle.contents.event_y})"
                )
            elif response_type == xcb_consts.XCB_KEY_PRESS:
                kpe = ctypes.cast(event, xcb_types.XcbKeyPressEventP)
                print(
                    f"Key {kpe.contents.detail} pressed in window {kpe.contents.event}"
                    f" with modifiers {name_modifiers(kpe.contents.state)}"
                )
            elif response_type == xcb_consts.XCB_KEY_RELEASE:
                kre = ctypes.cast(event, xcb_types.XcbKeyReleaseEventP)
                print(
                    f"Key {kre.contents.detail} released in window {kre.contents.event}"
                    f" with modifiers {name_modifiers(kre.contents.state)}"
                )
            else:
                print(f"Unknown event {response_type}")

            clib.force_free(event)
    finally:
        xcb.xcb_disconnect(connection)


if __name__ == '__main__':
    main()
