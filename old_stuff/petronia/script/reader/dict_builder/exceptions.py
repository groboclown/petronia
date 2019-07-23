

class ConfigLoadException(Exception):
    def __init__(self, section, msg):
        if len(section) == 1:
            section = [section[0], '(root)']
        self.config_file = section[0]
        self.section = section[1:]
        self.message = msg

    def __str__(self):
        return "ConfigLoadException: Problem loading configuration {0}: {1}: {2}".format(
            self.config_file, self.section, self.message)

    def __repr__(self):
        return "ConfigLoadException(\"Problem loading configuration\", {0}, {1}, {2})".format(
            repr(self.config_file), repr(self.section), repr(self.message)
        )
