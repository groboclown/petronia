
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
        create_focus_last_flashing_window(),
        create_move_window_to_other_portal(),
        create_change_layout_management_selection_shape(),create_join_selected_layout(),
        create_split(),
        create_minimize(),
        create_maximize(),
        create_resize(),
        create_change_layout(),
        create_load_config(),
        create_lock_screen(),
        create_inject_keys(),
        create_exec_cmd(),
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


def create_focus_last_flashing_window():
    return Command("focus-last-flashing-window", command_helper.focus_last_flashing_window)


def create_move_window_to_other_portal():
    return Command("move-window-to-other-portal", command_helper.move_window_to_other_portal)


def create_change_layout_management_selection_shape():
    return Command("change-layout-selection", command_helper.change_layout_management_selection_shape)


def create_join_selected_layout():
    return Command("join-selected-layout", command_helper.join_selected_layout)


def create_split():
    return Command("split", command_helper.split_layout)


def create_minimize():
    return Command("minimize", command_helper.minimize)


def create_maximize():
    return Command("maximize", command_helper.maximize)


def create_resize():
    return Command("resize", command_helper.resize)


def create_change_layout():
    return Command("change-layout", command_helper.change_layout)


def create_load_config():
    return Command('load-config', command_helper.load_config)


def create_lock_screen():
    return Command("lock-screen", command_helper.lock_screen)


def create_inject_keys():
    return Command("inject-keys", command_helper.inject_keys)


def create_exec_cmd():
    return Command("cmd", command_helper.exec_cmd)


if __name__ == '__main__':
    # Create the 'user-commands.md' file.

    __FILE_TEMPLATE = """# Hotkey Commands

All the commands you can run with hotkeys.

See also [custom commands](user-custom-commands.md).

Reference: [command_builder.py](../src/petronia/script/command_builder.py)
<!-- that file generates this file -->


## Built-In Command List

{0}
"""

    __COMMAND_TEMPLATE = """### `{name} {args_list}`

**Arguments**: {args_desc}

{help}

"""

    __ARG_HEADER_TEMPLATE = "({0})"
    __ARG_DESC_TEMPLATE = "* `{0}` - {1}"

    __cmds = []

    for __cmd in create_all_commands():
        __docs = __cmd.describe().splitlines()
        __parts = {'desc': [], 'arg': None}
        __args = []
        __mode = 'desc'
        for __line in __docs:
            __line = __line.strip()
            if __line.startswith(':param bus:'):
                __mode = None
            elif __line.startswith(':param '):
                __mode = 'arg'
                __parts['arg'] = []
                __name = __line[7:__line.find(':', 1)]
                __line = __line[__line.find(':', 1)+1:]
                __args.append((__name, __parts['arg']))
            elif __line.startswith(':'):
                __mode = None
            if __mode is not None:
                __parts[__mode].append(__line)
        __arg_headers = []
        __arg_descs = []
        for __arg_name, __arg_desc_list in __args:
            __arg_headers.append(__ARG_HEADER_TEMPLATE.format(__arg_name).strip())
            __arg_descs.append(__ARG_DESC_TEMPLATE.format(__arg_name, " ".join(__arg_desc_list)).strip())
        __cmds.append(__COMMAND_TEMPLATE.format(
            name=__cmd.name,
            args_list=" ".join(__arg_headers),
            args_desc=len(__args) <= 0 and "None" or ("\n\n" + "\n".join(__arg_descs)),
            help="\n".join(__parts['desc']).strip()
        ))
    print(__FILE_TEMPLATE.format("\n\n".join(__cmds)))
