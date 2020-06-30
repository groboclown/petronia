# Locations of Installed Files

# Location of User-Specific Files

## Windows

On Windows computers, Petronia will search for files in the `%HOME%\AppData\Roaming\Petronia` directory.


## Linux

From (freedesktop.org)[https://www.freedesktop.org/wiki/Specifications/basedir-spec/]:

* There is a single base directory relative to which user-specific data files should be written. This directory is defined by the environment variable `$XDG_DATA_HOME`...  `$XDG_DATA_HOME` defines the base directory relative to which user specific data files should be stored. If $XDG_DATA_HOME is either not set or empty, a default equal to `$HOME/.local/share` should be used.
* There is a single base directory relative to which user-specific configuration files should be written. This directory is defined by the environment variable `$XDG_CONFIG_HOME`...  `$XDG_CONFIG_HOME` defines the base directory relative to which user specific configuration files should be stored. If `$XDG_CONFIG_HOME` is either not set or empty, a default equal to $HOME/.config should be used.
* There is a set of preference ordered base directories relative to which data files should be searched. This set of directories is defined by the environment variable `$XDG_DATA_DIRS`...  `$XDG_DATA_DIRS` defines the preference-ordered set of base directories to search for data files in addition to the `$XDG_DATA_HOME` base directory.  The directories in `$XDG_DATA_DIRS` should be separated with a colon ':'.  If `$XDG_DATA_DIRS` is either not set or empty, a value equal to `/usr/local/share/:/usr/share/` should be used.
* There is a set of preference ordered base directories relative to which configuration files should be searched. This set of directories is defined by the environment variable `$XDG_CONFIG_DIRS`...  `$XDG_CONFIG_DIRS` defines the preference-ordered set of base directories to search for configuration files in addition to the `$XDG_CONFIG_HOME` base directory. The directories in `$XDG_CONFIG_DIRS` should be separated with a colon ':'.  If `$XDG_CONFIG_DIRS` is either not set or empty, a value equal to `/etc/xdg` should be used.
* There is a single base directory relative to which user-specific non-essential (cached) data should be written. This directory is defined by the environment variable `$XDG_CACHE_HOME`.
* `$XDG_CACHE_HOME` defines the base directory relative to which user specific non-essential data files should be stored. If `$XDG_CACHE_HOME` is either not set or empty, a default equal to `$HOME/.cache` should be used.
* The order of base directories denotes their importance; the first directory listed is the most important. When the same information is defined in multiple places the information defined relative to the more important base directory takes precedent. The base directory defined by `$XDG_DATA_HOME` is considered more important than any of the base directories defined by `$XDG_DATA_DIRS`. The base directory defined by `$XDG_CONFIG_HOME` is considered more important than any of the base directories defined by `$XDG_CONFIG_DIRS`.
