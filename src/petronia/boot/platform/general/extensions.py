
"""
Basic extensions that should be started by default.
"""

# Need to add stand-alone extensions that are always on by default.
# These need to load after the initial core list, because that will
# mean a state definition.  These must be loaded after that list.
# So, it may be split into a pre-boot list and a boot list.

# configuration.file
#       needs special setup to load its config from the platform.
#       That will pull from the ini files and defaults.
# default.state
#       should be in the pre-boot list, and is configurable.
#       Not part of this list.
