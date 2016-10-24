
from .command import Command
from . import command_helper


def create_all_commands():
    return [
        create_quit(),
        create_open_start_menu(),
        create_move_focus(),
        create_switch_top_window(),
        create_switch_layout(),
        create_create_current_portal_alias(),
        create_focus_portal_by_alias(),
        create_move_window_to_other_portal(),
        create_change_layout_management_selection_shape(),
        create_join_selected_layout(),
        create_split(),
    ]


def create_quit():
    return Command("quit", command_helper.quit_shell)


def create_open_start_menu():
    return Command("open-start-menu", command_helper.open_start_menu)


def create_move_focus():
    return Command("move-focus", command_helper.move_focus)


def create_switch_top_window():
    return Command("switch-top-window", command_helper.switch_top_window)


def create_switch_layout():
    return Command("switch-layout", command_helper.switch_layout)


def create_create_current_portal_alias():
    return Command("create-current-portal-alias", command_helper.create_current_portal_alias)


def create_focus_portal_by_alias():
    return Command("focus-portal-by-alias", command_helper.focus_portal_by_alias)


def create_move_window_to_other_portal():
    return Command("move-window-to-other-portal", command_helper.move_window_to_other_portal)


def create_change_layout_management_selection_shape():
    return Command("change-layout-selection", command_helper.change_layout_management_selection_shape)


def create_join_selected_layout():
    return Command("join-selected-layout", command_helper.join_selected_layout)


def create_split():
    return Command("split", command_helper.split_layout)
