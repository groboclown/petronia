
from petronia.arch import funcs

if __name__ == '__main__':
    # index = 0
    # for monitor in funcs.monitor__find_monitors():
    #     print("{0}: [{1},{2}] to [{3},{4}]".format(
    #         index, monitor['left'], monitor['top'], monitor['right'], monitor['bottom']))
    #     index += 1

    index = 0
    print("[")
    for monitor in funcs.monitor__find_monitors():
        print("{0}'left': {1}, 'top': {2}, 'right': {3}, 'bottom': {4}{5},".format(
            "    {", monitor['left'], monitor['top'], monitor['right'], monitor['bottom'], "}"))
        index += 1
    print("]")

    index = 0
    print("[")
    for monitor in funcs.monitor__find_monitors():
        print("    config.MonitorResConfig({0}, {1}, {2}, False),".format(
            index, monitor['right'] - monitor['left'], monitor['bottom'] - monitor['top']))
        index += 1
    print("]")
