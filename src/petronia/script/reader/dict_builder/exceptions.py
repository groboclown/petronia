

class ConfigLoadException(Exception):
    def __init__(self, section, msg):
        if len(section) == 1:
            section = [section[0], '(root)']
        super("Problem loading configuration {0}: {1}: {2}".format(section[0], section[1:], msg))
