# Disposing Services and Extensions

Each service that installs itself into Petronia must be able to remove itself.  Petronia provides events that all such participants must be aware of to conform to this standard.

## Quick Win

The rest of this document describes the events and what extensions need to do to correctly handle them.  However, Petronia comes with a helper to make this easy.

```python
from petronia.aid.lifecycle import create_module_listener_helper
from petronia.aid.bootstrap import create_singleton_identity

MODULE_ID = create_singleton_identity('my.extension')

def start_module(bus):
    listeners = create_module_listener_helper(bus, MODULE_ID)
    listeners.listen(TARGET_ID_OTHER, as_other_listener, my_callback)
```

The returned `listeners` object will correctly dispose all registered event listeners and hotkey descriptors when the module is requested to be disposed, or if the system shuts down.

Optionally, you can pass an additional argument to `create_module_listener_helper`, a call back function that is invoked when the disposal executes.  This allows for hooking in additional shutdown behavior beyond what the listener set provides.

## Required Dispose Events

### Request Dispose and Disposed

The system can send a "request disposal" event to the participant.  The participant must then finish what it's doing and clean itself up, then send a "disposed" event back to indicate that it is removed out of the system.

One trick to this is making sure the memory is properly cleaned up.  If the service runs in a shared process, then extra memory could leak and take up end-user resources.

### Shutdown Started

For normal applications, a shutdown started event means that the user wants to stop the system, and applications need to stop themselves.  The user can still cancel the shutdown at this point, so if an application requires extra user input or isn't stopping, the user can inspect why.

If the application can get into a position where it shut itself down, it should also listen for `Shutdown Cancelled` events.

### Shutdown Finalize

This event means that, at this point, cancellation requests won't be accepted.  If you have a service that should stay active during the entire execution, then it should stop itself at this point, so that a shutdown cancel doesn't put the system in a state where some services are closed.

When the final Halt event happens, then the system has stopped and events can no longer flow.
