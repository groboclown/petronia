
# Automatically included in each script as "helper".

from ..system import event_ids
from ..system import target_ids
from ..shell.native.shutdown import shutdown_system
from ..shell.navigation import DIRECTIONS, ROTATABLE_DIRECTIONS
import subprocess
import shlex

# Actions that are already implemented.
from ..shell.view.show_key_actions import toggle_show_key_action


# noinspection PyUnusedLocal
def quit_shell(bus):
    # This should really be a signal to something else,
    # but due to the nature of a 'quit' command, this
    # needs to happen NOW.
    shutdown_system()


def open_start_menu(bus):
    bus.fire(event_ids.TELL_WINDOWS__OPEN_START_MENU, target_ids.WINDOWS_HOOKS, {})


def move_focus(bus, direction):
    if direction.lower() in DIRECTIONS:
        bus.fire(event_ids.FOCUS__MOVE, target_ids.ACTIVE_PORTAL_MANAGER, {'direction': direction.lower()})


def switch_top_window(bus, rotate):
    if rotate.lower() in ROTATABLE_DIRECTIONS:
        bus.fire(event_ids.ZORDER__WINDOW_SHOWN_CHANGE, target_ids.ACTIVE_PORTAL_MANAGER, {'direction': rotate.lower()})


def switch_layout(bus, layout_name):
    bus.fire(event_ids.LAYOUT__SWITCH_TO, target_ids.TOP_LAYOUT, {'layout-name': layout_name})


def create_current_portal_alias(bus, alias_name):
    bus.fire(event_ids.PORTAL__CREATE_ALIAS, target_ids.ACTIVE_PORTAL_MANAGER, {'alias': alias_name})


def focus_portal_by_alias(bus, alias_name):
    bus.fire(event_ids.FOCUS__PORTAL_ALIAS, target_ids.ACTIVE_PORTAL_MANAGER, {'alias': alias_name})


def move_window_to_other_portal(bus, direction):
    if direction.lower() in DIRECTIONS:
        # print("DEBUG firing move portal " + direction)
        bus.fire(event_ids.PORTAL__MOVE_WINDOW_TO_OTHER_PORTAL, target_ids.ACTIVE_PORTAL_MANAGER,
                 {'direction': direction.lower()})


def change_layout_management_selection_shape(bus, direction, change):
    if direction.lower() in DIRECTIONS and change in ['+', '-']:
        bus.fire(event_ids.LAYOUT_SELECTION__CHANGE_SHAPE, target_ids.BROADCAST, {
            'direction': direction.lower(),
            'change': change.lower()
        })


def join_selected_layout(bus):
    bus.fire(event_ids.LAYOUT_SELECTION__JOIN, target_ids.BROADCAST, {})


def split_layout(bus):
    bus.fire(event_ids.LAYOUT_SELECTION__SPLIT, target_ids.BROADCAST, {})


def minimize(bus):
    bus.fire(event_ids.TELL_WINDOWS__MINIMIZE_WINDOW, target_ids.WINDOW_MAPPER, {})


def maximize(bus):
    bus.fire(event_ids.TELL_WINDOWS__MAXIMIZE_WINDOW, target_ids.WINDOW_MAPPER, {})


def resize(bus, adjust_x, adjust_y):
    bus.fire(event_ids.TELL_WINDOWS__RESIZE_WINDOW, target_ids.WINDOW_MAPPER, {
        'adjust-x': int(adjust_x),
        'adjust-y': int(adjust_y),
    })


def change_layout(bus, layout_name):
    bus.fire(event_ids.LAYOUT__SWITCH_TO, target_ids.TOP_LAYOUT, {
        'layout-name': layout_name
    })


def load_config(bus, *config_file):
    event_obj = {}
    if len(config_file) > 0:
        event_obj['config-file'] = config_file[0]
    bus.fire(event_ids.CONFIG__REQUEST_LOAD, target_ids.CONFIGURATION_LOADER, event_obj)


def lock_screen(bus):
    bus.fire(event_ids.TELL_WINDOWS__LOCK_SCREEN, target_ids.WINDOWS_HOOKS, {})


def inject_keys(bus, *key_commands):
    key_pairs = []
    for i in range(len(key_commands) / 2):
        key_pairs.append((key_commands[i * 2], key_commands[(i * 2) + 1]))
    bus.fire(event_ids.TELL_WINDOWS__INJECT_KEYS, target_ids.WINDOWS_HOOKS, {
        'keys': key_pairs,
    })


def exec_cmd(bus, *cmd_line):
    # The cmd_line is a space-split set of arguments.  Because we're running a
    # command line, and should allow all kinds of inputs, we'll join it back
    # together and split to allow quoting.
    full_cmd = " ".join(cmd_line)
    args = shlex.split(full_cmd)
    print('Running "' + ('" "'.join(args)) + '"')
    # TODO look at making this a bus command, or at least a bus announcement.
    proc = subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    bus.fire(event_ids.LOG__INFO, target_ids.LOGGER, {
        'message': '{0}: {1}'.format(proc.pid, args)
    })
