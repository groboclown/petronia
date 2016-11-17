
# Automatically included in each script as "helper".

from ..system import event_ids
from ..system import target_ids
from ..shell.native.shutdown import shutdown_system
from ..shell.navigation import DIRECTIONS, ROTATABLE_DIRECTIONS
import subprocess
import shlex
import re


# noinspection PyUnusedLocal
def quit_shell(bus):
    """Exits Petronia.  Currently, this is the only way to quit Petronia
    (besides running task manager and killing the process).  This means that you
    need to be sure to include at least one hot key to terminate the program.

    :param bus:
    """
    # This should really be a signal to something else,
    # but due to the nature of a 'quit' command, this
    # needs to happen NOW.
    shutdown_system()


def open_start_menu(bus):
    """
    Forces the Windows Start Menu to open.  If you have the task bar minimized by
    default, then the start menu will appear as if the task bar is visible, but
    the task bar may not show itself.

    Especially handy if you've disabled Windows from processing the Windows key.

    :param bus:
    """
    bus.fire(event_ids.TELL_WINDOWS__OPEN_START_MENU, target_ids.WINDOWS_HOOKS, {})


def move_focus(bus, direction):
    """
    Make another portal have the "portal focus", in a relative direction to the
    currently focused portal.  The focused portal can be setup through the
    `ChromeConfig` to have a distinct border color from the non-focused portals.

    :param bus:
    :param direction: one of `north`, `south`, `east`, `west`, `next`, `previous`
    """
    if direction.lower() in DIRECTIONS:
        bus.fire(event_ids.FOCUS__MOVE, target_ids.ACTIVE_PORTAL_MANAGER, {'direction': direction.lower()})


def switch_top_window(bus, direction):
    """
    Switch which window in the currently active portal (the one with the "portal
    focus") is on top.

    *Not implemented yet.*  The code for this is at `active_portal_manager.py`,
    in the `_on_window_zorder_change` method.

    :param bus:
    :param direction: one of `north`, `south`, `east`, `west`, `next`, `previous`
    :return:
    """
    if direction.lower() in ROTATABLE_DIRECTIONS:
        bus.fire(event_ids.ZORDER__WINDOW_SHOWN_CHANGE, target_ids.ACTIVE_PORTAL_MANAGER, {
            'direction': direction.lower()
        })


def switch_layout(bus, layout_name):
    """
    Switches the currently displayed layout configuration to a different
    configuration.

    :param bus:
    :param layout_name: `layout name`: one of the work group layouts.
    :return:
    """
    bus.fire(event_ids.LAYOUT__SWITCH_TO, target_ids.TOP_LAYOUT, {'layout-name': layout_name})


def create_current_portal_alias(bus, alias_name):
    """
    Gives the currently focused portal a specific name.

    :param bus:
    :param alias_name: alias to call the currently focused portal
    :return:
    """
    bus.fire(event_ids.PORTAL__CREATE_ALIAS, target_ids.ACTIVE_PORTAL_MANAGER, {'alias': alias_name})


def focus_portal_by_alias(bus, alias_name):
    """
    Returns the portal focus to the previously aliased portal.  Can also refer
    to the original portal name, as specified in the layout definition.

    Also, sends that portal's "top" window to the front of the other windows, and
    gives it focus.  This allows for quick focus swapping between apps, with more
    configurability than the standard Windows <kbd>&#x2756; Win</kbd><kbd>1</kbd>
    (and other digits).

    :param bus:
    :param alias_name: alias of the portal to focus.
    :return:
    """
    bus.fire(event_ids.FOCUS__PORTAL_ALIAS, target_ids.ACTIVE_PORTAL_MANAGER, {'alias': alias_name})


def focus_last_flashing_window(bus):
    """
    Make the last window that "flashed" (blinked in the task bar) focused and on top
    of the other windows.  This works on windows which are managed and not managed by
    the tiling system.

    :param bus:
    :return:
    """
    bus.fire(event_ids.FOCUS__SWITCH_TO_LAST_FLASHING_WINDOW, target_ids.BROADCAST, {})


def move_window_to_other_portal(bus, direction):
    """
    Moves the currently active window into another portal adjacent to its current
    portal.

    :param bus:
    :param direction: one of `north`, `south`, `east`, `west`, `next`, `previous`
    :return:
    """
    if direction.lower() in DIRECTIONS:
        # print("DEBUG firing move portal " + direction)
        bus.fire(event_ids.PORTAL__MOVE_WINDOW_TO_OTHER_PORTAL, target_ids.ACTIVE_PORTAL_MANAGER,
                 {'direction': direction.lower()})


def change_layout_management_selection_shape(bus, direction, change):
    """
    Change the current layout selection shape.

    *Not implemented yet.*  This will be part of the future feature to allow for
    the user to alter the layout shape while Petronia is running.

    :param bus:
    :param direction: one of `north`, `south`, `east`, `west`, `next`, `previous`
    :param change: one of `+`, `-`
    :return:
    """
    if direction.lower() in DIRECTIONS and change in ['+', '-']:
        bus.fire(event_ids.LAYOUT_SELECTION__CHANGE_SHAPE, target_ids.BROADCAST, {
            'direction': direction.lower(),
            'change': change.lower()
        })


def join_selected_layout(bus):
    """
    Combine the currently selected layouts into a single layout ("un-split")

    *Not implemented yet.*  This will be part of the future feature to allow for
    the user to alter the layout shape while Petronia is running.

    :param bus:
    :return:
    """
    bus.fire(event_ids.LAYOUT_SELECTION__JOIN, target_ids.BROADCAST, {})


def split_layout(bus, orientation):
    """
    Split the currently selected layout in the given orientation.

    *Not implemented yet.*  This will be part of the future feature to allow for
    the user to alter the layout shape while Petronia is running.

    :param bus:
    :param orientation: one of `vertical`, `horizontal`
    :return:
    """
    bus.fire(event_ids.LAYOUT_SELECTION__SPLIT, target_ids.BROADCAST, {
        'orientation': orientation.lower()
    })


def minimize(bus):
    """
    Minimize (to the task bar) the currently active window.

    :param bus:
    :return:
    """
    bus.fire(event_ids.TELL_WINDOWS__MINIMIZE_WINDOW, target_ids.WINDOW_MAPPER, {})


def maximize(bus):
    """
    Maximize the currently active window.

    :param bus:
    :return:
    """
    bus.fire(event_ids.TELL_WINDOWS__MAXIMIZE_WINDOW, target_ids.WINDOW_MAPPER, {})


def resize(bus, adjust_x, adjust_y):
    """
    Resize the currently active window by the given amount.

    To make a side bigger, use a positive number.  To make it smaller, use a
    negative number.  To keep it the same size, use 0.

    :param bus:
    :param adjust_x: integer amount to resize in the x (horizontal) direction; may be
        negative or 0.
    :param adjust_y: integer amount to resize in the y (vertical) direction; may be
        negative or 0.
    :return:
    """
    bus.fire(event_ids.TELL_WINDOWS__RESIZE_WINDOW, target_ids.WINDOW_MAPPER, {
        'adjust-x': int(adjust_x),
        'adjust-y': int(adjust_y),
    })


def change_layout(bus, layout_name):
    """
    Switches the currently displayed layout configuration to a different
    configuration.

    :param bus:
    :param layout_name: one of the work group layouts.
    :return:
    """
    bus.fire(event_ids.LAYOUT__SWITCH_TO, target_ids.TOP_LAYOUT, {
        'layout-name': layout_name
    })


def load_config(bus, config_file=None):
    """
    Loads the given configuration file to become actively used.  If no config
    file is given, then it reloads the current config file.

    :param bus:
    :param config_file: (optional) If given, the name of the config file to load.
    :return:
    """
    event_obj = {}
    if config_file is not None and len(config_file) > 0:
        event_obj['config-file'] = config_file[0]
    bus.fire(event_ids.CONFIG__REQUEST_LOAD, target_ids.CONFIGURATION_LOADER, event_obj)


def lock_screen(bus):
    """
    Lock the desktop.  Equivalent to <kbd>&#x2756; Win</kbd><kbd>L</kbd>, which
    will always be active anyway.

    :param bus:
    :return:
    """
    bus.fire(event_ids.TELL_WINDOWS__LOCK_SCREEN, target_ids.WINDOWS_HOOKS, {})


def inject_keys(bus, *key_commands):
    """
    Injects a series of keystrokes into the operating system.

    The arguments must be a series of "key name" "press type" words.
    "key name" refers to the name of the key on the keyboard to
    simulate pressing (equivalent to the name used in
    [the hotkey definition](keys.md)).  "press type" must be
    either `up` or `down`, to indicate whether the key is pressed
    *down* or released (the key moves *up*).

    :param bus:
    :param key_commands: series of `key name` and `press type`
    :return:
    """
    key_pairs = []
    for i in range(len(key_commands) / 2):
        key_pairs.append((key_commands[i * 2], key_commands[(i * 2) + 1]))
    bus.fire(event_ids.TELL_WINDOWS__INJECT_KEYS, target_ids.WINDOWS_HOOKS, {
        'keys': key_pairs,
    })


def exec_cmd(bus, *cmd_line):
    """
    Executes an external process using the given arguments.  Note that the
    backslash (`\`) character must be escaped, because they are within a Python
    string, so a total of 2 backslashes to equal 1 real backslash.

    For example, to run a command prompt with fancy colors and start it in the
    root of the file system when you press <kbd>F1</kbd>, use:

    ```
    'f1 => cmd cmd.exe /c start cmd.exe /E:ON /V:ON /T:17 /K cd \\'
    ```

    :param bus:
    :param cmd_line: The command-line string equivalent to run.
    :return:
    """
    # The cmd_line is a space-split set of arguments.  Because we're running a
    # command line, and should allow all kinds of inputs, we'll join it back
    # together.
    full_cmd = " ".join(cmd_line)

    # We won't use shlex, because, for Windows, splitting is just unnecessary.
    print('CMD Running `' + full_cmd + '`')
    # TODO look at making this a bus command, or at least a bus announcement.
    proc = subprocess.Popen(full_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    bus.fire(event_ids.LOG__INFO, target_ids.LOGGER, {
        'message': '{0}: {1}'.format(proc.pid, full_cmd)
    })
