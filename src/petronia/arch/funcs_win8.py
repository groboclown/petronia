"""
Windows 8 & 8.1 functions
"""


def load_functions(environ, func_map):
    if environ['system'].lower() == 'windows' and (environ['release'].lower() == '8' or environ['release'].lower() == '8.1'):
        load_all_functions(func_map)


def load_all_functions(func_map):
    from .funcs_win7 import load_all_functions as w7_load
    w7_load(func_map)


def shell__open_start_menu():
    pass
