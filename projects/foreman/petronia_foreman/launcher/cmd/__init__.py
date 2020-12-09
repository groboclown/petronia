"""Command-based launcher.

This launcher category runs an arbitrary command as a launcher
channel.  If the launcher is expected to run extensions, then it
the command launched must be listening to standard event stream,
but also with additional extension-specific events (TBD).
"""

from .cmd_launcher import create_cmd_launcher
