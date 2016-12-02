
# Custom Commands

The hotkeys allow for running commands, but these commands are limited to
the built-in set of commands provided by Petronia.  However, it is possible
to write your own commands.

Additional commands are added to the configuration, and can be referenced
by the hotkey configuration like any other built-in command.


## Adding Commands through Plugins

If you're using the [components](user-components.md), you can add in a
singleton component that registers new commands.

The plugins themselves would add in the command to the configuration object
passed to the `get_factory` function, as `config.commands.add_command(cmd)`.


## Adding Commands through the Python Configuration

*TODO* This is described below, but needs to be restructured.


## Writing Commands

The *command* configuration object (`CommandConfig`) allows for registering
custom commands.  Each command must be a `petronia.script.command.Command`
object.

For example, to have a command that changes the output logging level, you
could write it as:

```python

from petronia.system import event_ids, target_ids
from petronia.script.command import Command
from petronia.config import CommandConfig

def change_log_level(bus, level):
    bus.fire(event_ids.LOG__LEVEL_SET, target_ids.LOGGER, {'level': level})

base_config = CommandConfig()
base_config.add_command(Command('set-log-level', change_log_level))
```

Then you can write a hotkey definition:

```
"alt + shift + f1": ['set-log-level', 'debug']
```

If you're writing a command that interacts with the inner workings of Petronia,
then you'll have to send signals through the event bus.

If you really want to get funky, you can reach into the bowels of the winapi
calls and directly query or interact with the windows.  However, this API is
very much use at your own risk.

Otherwise, just use the standard Python API.  If you install custom packages
into your Python installation, then you can use those, as well.


## Writing a Hotkey to Directly Run Something and Bypass Commands

Not supported, and not planned on being supported.
