"""Common constant values."""

import ctypes
from ..libs import libxcb_consts

# All the events that the root windows will need to listen to.
ROOT_WINDOW_EVENT_MASK__c = ctypes.c_uint32(
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
    | libxcb_consts.XCB_EVENT_MASK_POINTER_MOTION
    | libxcb_consts.XCB_EVENT_MASK_POINTER_MOTION_HINT
    # | libxcb_consts.XCB_EVENT_MASK_VISIBILITY_CHANGE
    | libxcb_consts.XCB_EVENT_MASK_EXPOSURE
    | libxcb_consts.XCB_EVENT_MASK_FOCUS_CHANGE
    | libxcb_consts.XCB_EVENT_MASK_PROPERTY_CHANGE
)

CLIENT_WINDOW_EVENT_MASK__c = (
    libxcb_consts.XCB_EVENT_MASK_STRUCTURE_NOTIFY
    | libxcb_consts.XCB_EVENT_MASK_PROPERTY_CHANGE
    | libxcb_consts.XCB_EVENT_MASK_FOCUS_CHANGE
)
