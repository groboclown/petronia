
"""
Constants defining the known event IDs.

Only constants defined here will be acknowledged as event ids.

Event ids that end with " Notice" or start with "Request " will
be run in the background.
"""

from importlib import import_module


EVENT_THREAD__USER_REQUEST = " (Request)"
EVENT_THREAD__NOTICE = " (Notice)"
EVENT_THREAD__LAYOUT = " (Layout)"

# "Now" events are the equivalent to a straight-up procedure call.
# They happen immediately, without going into a queue or another
# thread.
EVENT_THREAD__NOW = " (Now)"


# Wildcard - matches all events.
ALL = "*"

# ---------------------------------------------------------------------------
# System related Events

SYSTEM__QUIT = "System Quit" + EVENT_THREAD__NOTICE


# ---------------------------------------------------------------------------
# Bus related Events
BUS__LISTENER_ADDED = "Listener Added" + EVENT_THREAD__NOTICE
BUS__LISTENER_REMOVED = "Listener Removed" + EVENT_THREAD__NOTICE
BUS__USER_GENERATED_ID = "User Generated ID" + EVENT_THREAD__NOTICE


# ---------------------------------------------------------------------------
# Registrar Events
REGISTRAR__ID_ALLOCATED = "ID Allocated" + EVENT_THREAD__NOTICE
REGISTRAR__OBJECT_REGISTERED = "Object Registered" + EVENT_THREAD__NOTICE
REGISTRAR__REGISTER_OBJECT = "Register Object" + EVENT_THREAD__NOW
REGISTRAR__OBJECT_REMOVED = "Object Removed" + EVENT_THREAD__NOW


# ---------------------------------------------------------------------------
# Marshaling Events

MARSHAL__SAVE = "Marshal Save" + EVENT_THREAD__NOTICE
MARSHAL__SAVE_TO = "Marshal Save To" + EVENT_THREAD__NOTICE


# ---------------------------------------------------------------------------
# Logging Events

# LOG__DEBUG = "Log Debug" + EVENT_THREAD__NOTICE
# LOG__VERBOSE = "Log Verbose" + EVENT_THREAD__NOTICE
# LOG__INFO = "Log Info" + EVENT_THREAD__NOTICE
# LOG__WARN = "Log Warn" + EVENT_THREAD__NOTICE
# LOG__ERROR = "Log Error" + EVENT_THREAD__NOTICE

LOG__DEBUG = "Log Debug" + EVENT_THREAD__NOW
LOG__VERBOSE = "Log Verbose" + EVENT_THREAD__NOW
LOG__INFO = "Log Info" + EVENT_THREAD__NOW
LOG__WARN = "Log Warn" + EVENT_THREAD__NOW
LOG__ERROR = "Log Error" + EVENT_THREAD__NOW

LOG__FATAL = "Log" + EVENT_THREAD__NOW

LOG__LEVEL_SET = "Log Level Set" + EVENT_THREAD__USER_REQUEST


# ---------------------------------------------------------------------------
# Worker Thread Signals

WORKER__STOP = "Worker Stop" + EVENT_THREAD__NOW
WORKER__QUEUE = "Worker Queue" + EVENT_THREAD__NOW
WORKER__STARTED = "Worker Started" + EVENT_THREAD__NOTICE
WORKER__PROCESS_STARTED = "Worker Process Started" + EVENT_THREAD__NOTICE
WORKER__PROCESS_STOPPED = "Worker Process Stopped" + EVENT_THREAD__NOTICE
WORKER__STOPPING = "Worker Stopping" + EVENT_THREAD__NOTICE
WORKER__STOPPED = "Worker Stopped" + EVENT_THREAD__NOTICE


# ---------------------------------------------------------------------------
# Configuration Events

CONFIG__UPDATE = "Config Update" + EVENT_THREAD__NOTICE
CONFIG__REQUEST_RELOAD = "Config Reload" + EVENT_THREAD__USER_REQUEST
CONFIG__REQUEST_SAVE = "Config Save" + EVENT_THREAD__USER_REQUEST


# ---------------------------------------------------------------------------
# User requests outside of standard use cases.

USER__SAVE_SETTINGS = "Save Settings" + EVENT_THREAD__USER_REQUEST

"""A command sent by the user.  It has been translated by the
hotkey into an actual command."""
USER__COMMAND = "Key Command" + EVENT_THREAD__NOTICE


# ---------------------------------------------------------------------------
# OS events

OS__WINDOW_CREATED = "OS Window Created" + EVENT_THREAD__NOTICE
OS__WINDOW_DESTROYED = "OS Window Destroyed" + EVENT_THREAD__NOTICE
OS__SHELL_WINDOW_FOCUSED = "OS Shell Window Focused" + EVENT_THREAD__NOTICE
OS__WINDOW_FOCUSED = "OS Window Focused" + EVENT_THREAD__NOTICE
OS__WINDOW_MINIMIZED = "OS Window Minimized" + EVENT_THREAD__NOTICE
OS__WINDOW_REDRAW = "OS Window Needs Redraw" + EVENT_THREAD__NOTICE
OS__TASK_MANAGER_FOCUSED = "OS Task Manager Focused" + EVENT_THREAD__NOTICE
OS__LANGUAGE = "OS Keyboard Language Changed" + EVENT_THREAD__NOTICE
OS__SYS_MENU = "OS System Menu" + EVENT_THREAD__NOTICE
OS__WINDOW_FORCED_END = "OS Window Forced End" + EVENT_THREAD__NOTICE
OS__WINDOW_REPLACING = "OS Window Replacing" + EVENT_THREAD__NOTICE
OS__WINDOW_REPLACED = "OS Window Replaced" + EVENT_THREAD__NOTICE
OS__WINDOW_MONITOR_CHANGED = "OS Window Monitor Changed" + EVENT_THREAD__NOTICE
OS__WINDOW_FLASH = "OS Window Flash" + EVENT_THREAD__NOTICE
OS__APP_COMMAND = "OS AppCommand" + EVENT_THREAD__NOTICE
OS__RESOLUTION_CHANGED = "OS Resolution Changed" + EVENT_THREAD__NOTICE


# ---------------------------------------------------------------------------
# Interpreted Windows Commands

WINDOW__CREATED = "Window Created" + EVENT_THREAD__NOTICE
WINDOW__CLOSED = "Window Closed" + EVENT_THREAD__NOTICE
WINDOW__FOCUSED = "Window Focused" + EVENT_THREAD__NOTICE
WINDOW__FLASHING = "Window Flashing" + EVENT_THREAD__NOTICE
WINDOW__REDRAW = "Window Redraw" + EVENT_THREAD__NOTICE


# ---------------------------------------------------------------------------
# Layout Change Events

LAYOUT__SWITCH_TO = "Switch Layout" + EVENT_THREAD__USER_REQUEST
LAYOUT__SET_RECTANGLE = "Set Screen Rectangle" + EVENT_THREAD__NOTICE
LAYOUT__REMOVE_OBJECT = "Remove Object" + EVENT_THREAD__NOW
LAYOUT__ROOT_LAYOUT_CREATE = "Root Layout Create" + EVENT_THREAD__NOTICE
LAYOUT__ADD_WINDOW = "Add Top-Level Window" + EVENT_THREAD__NOTICE


# ---------------------------------------------------------------------------
# Focus Negotiation Events

FOCUS__MOVE = "Active Portal Move" + EVENT_THREAD__USER_REQUEST
FOCUS__PORTAL_ALIAS = "Portal Focus By Alias" + EVENT_THREAD__USER_REQUEST
FOCUS__MAKE_OWNED_PORTAL_ACTIVE = "Make Portal Owning Window Active" + EVENT_THREAD__USER_REQUEST
FOCUS__SET_FIRST_WINDOW_FOCUSED = "Portal Focus First Window" + EVENT_THREAD__NOTICE


# ---------------------------------------------------------------------------
# Layout Selection Events

LAYOUT_SELECTION__CHANGE_SHAPE = "Layout Management Selection Change" + EVENT_THREAD__USER_REQUEST
LAYOUT_SELECTION__SET_BASE = "Set Base Layout Manager" + EVENT_THREAD__NOTICE
LAYOUT_SELECTION__JOIN = "Join Layout Selection" + EVENT_THREAD__USER_REQUEST
LAYOUT_SELECTION__SPLIT = "Split Layout Selection" + EVENT_THREAD__USER_REQUEST


# ---------------------------------------------------------------------------
# Z-Order Window Commands

ZORDER__WINDOW_SHOWN_CHANGE = "Change Window In Portal" + EVENT_THREAD__USER_REQUEST
ZORDER__CHANGE_TOP_WINDOW = "Change Top Window Z-Order" + EVENT_THREAD__NOTICE
ZORDER__SET_WINDOW_ON_TOP = "Set Window On Top" + EVENT_THREAD__NOTICE


# ---------------------------------------------------------------------------
# Window Movement Commands

PORTAL__MOVE_WINDOW_HERE = "Move Specific Top-Level Window Here" + EVENT_THREAD__NOTICE
PORTAL__WINDOW_MOVED_TO_OTHER_PORTAL = "Top-Level Window Moved" + EVENT_THREAD__NOTICE
PORTAL__MOVE_WINDOW_TO_OTHER_PORTAL = "Move Top-Level Window" + EVENT_THREAD__USER_REQUEST
PORTAL__MOVE_WINDOW_TO_DESTINATION = "Move Top-Level Window To Destination Portal" + EVENT_THREAD__NOTICE


# ---------------------------------------------------------------------------
# Portal Activation Events

PORTAL__SET_ACTIVE = "Set Active Portal" + EVENT_THREAD__NOTICE
PORTAL__DEACTIVATED = "Portal Is No Longer Active" + EVENT_THREAD__NOTICE
PORTAL__ACTIVATED = "Portal Is Active" + EVENT_THREAD__NOTICE
PORTAL__REDRAW = "Portal Area Redraw" + EVENT_THREAD__NOTICE


# ---------------------------------------------------------------------------
# Direction Negotiation

DIRECTION_NEGOTIATION__BEGIN = "Begin Layout Direction Negotiation" + EVENT_THREAD__NOTICE
DIRECTION_NEGOTIATION__DISCOVER = "Direction Negotiation Discover" + EVENT_THREAD__NOW
DIRECTION_NEGOTIATION__DESCEND = "Direction Negotiation Descend" + EVENT_THREAD__NOW
DIRECTION_NEGOTIATION__TARGET = "Direction Negotiation Target" + EVENT_THREAD__NOW
DIRECTION_NEGOTIATION__COMPLETE = "Direction Negotiation Complete" + EVENT_THREAD__NOTICE


# ---------------------------------------------------------------------------
# Alias Management

PORTAL__CREATE_ALIAS = "Current Portal Alias" + EVENT_THREAD__USER_REQUEST


# ---------------------------------------------------------------------------
# Mode Change

MODE__CHANGE_TO = "Input Mode Changed To" + EVENT_THREAD__NOTICE


# ---------------------------------------------------------------------------
# Requests to get Windows to do something

TELL_WINDOWS__OPEN_START_MENU = "Hey Windows, Open Start Menu" + EVENT_THREAD__USER_REQUEST
TELL_WINDOWS__FOCUS_WINDOW = "Hey Windows, Focus This Window" + EVENT_THREAD__USER_REQUEST
TELL_WINDOWS__MINIMIZE_WINDOW = "Hey Windows, Minimize This Window" + EVENT_THREAD__USER_REQUEST
TELL_WINDOWS__MAXIMIZE_WINDOW = "Hey Windows, Maximize This Window" + EVENT_THREAD__USER_REQUEST
TELL_WINDOWS__INJECT_KEYS = "Hey Windows, Inject These Keystrokes" + EVENT_THREAD__USER_REQUEST
TELL_WINDOWS__LOCK_SCREEN = "Hey Windows, Lock Workstation" + EVENT_THREAD__USER_REQUEST


# ---------------------------------------------------------------------------
# Lists of all the event types

EVENT_THREAD_NAMES = (
    EVENT_THREAD__USER_REQUEST,
    EVENT_THREAD__NOTICE,
    EVENT_THREAD__LAYOUT,
    EVENT_THREAD__NOW,
)
EVENT_ID_TO_THREAD = {}

# Populate EVENT_ID_THREADS with all the string constants with only upper alnums and underscores in the name.
__MODULE_KEYS = list(globals().keys())
__current_module = import_module(__name__)
for __k in __MODULE_KEYS:
    if (__k != "ALL" and not __k.startswith('EVENT_THREAD__') and __k.upper() == __k
            and len(__k) == len(list(filter(lambda x: x.isalnum() or x == '_', __k)))):
        __v = getattr(__current_module, __k)
        if isinstance(__v, str):
            # print("Registering {0}={1}".format(__k, __v))
            registered = False
            for __et_id in EVENT_THREAD_NAMES:
                if __v.endswith(__et_id):
                    if __v in EVENT_ID_TO_THREAD:
                        # Note: outside of a bus, so have to use "print"
                        print("SETUP ERROR: {0} already registered".format(__k))
                    EVENT_ID_TO_THREAD[__v] = __et_id
                    registered = True
                    break
            if not registered:
                # Note: outside of a bus, so have to use "print"
                print("SETUP ERROR: {0} is not classified in a thread".format(__k))
