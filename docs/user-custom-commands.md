
## Custom Commands

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
alt + shift + f1 => set-log-level debug
```

If you're writing a command that interacts with the interworkings of Petronia,
then you'll have to send signals through the event bus.

If you really want to get funky, you can reach into the bowels of the winapi
calls and directly query or interact with the windows.  However, this API is
very much use at your own risk.

Otherwise, just use the standard Python API.  If you install custom packages
into your Python installation, then you can use those, as well.


## Writing a Hotkey to Directly Run Something and Bypass Commands

Not supported, and not planned on being supported.
