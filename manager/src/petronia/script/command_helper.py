
# Automatically included in each script as "helper".

from ..system import event_ids
from ..system import target_ids
from ..shell.native.shutdown import shutdown_system


DIRECTIONS = ['north', 'south', 'east', 'west']
ROTATE = ['left', 'right']


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
    if rotate.lower() in ROTATE:
        bus.fire(event_ids.ZORDER__WINDOW_SHOWN_CHANGE, target_ids.ACTIVE_PORTAL_MANAGER, {'direction': rotate.lower()})


def switch_layout(bus, layout_name):
    bus.fire(event_ids.LAYOUT__SWITCH_TO, target_ids.TOP_LAYOUT, {'layout-name': layout_name})


def create_current_portal_alias(bus, alias_name):
    bus.fire(event_ids.PORTAL__CREATE_ALIAS, target_ids.ACTIVE_PORTAL_MANAGER, {'alias': alias_name})


def focus_portal_by_alias(bus, alias_name):
    bus.fire(event_ids.FOCUS__PORTAL_ALIAS, target_ids.ACTIVE_PORTAL_MANAGER, {'alias': alias_name})


def move_window_to_other_portal(bus, direction):
    if direction.lower() in ['north', 'east', 'south', 'west']:
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
