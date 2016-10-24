"""
Windows 10 functions
"""


def load_functions(environ, func_map):
    if environ['system'].lower() == 'windows' and environ['release'].lower() == '10':
        load_all_functions(func_map)


def load_all_functions(func_map):
    from .funcs_win8 import load_all_functions as w8_load
    w8_load(func_map)
