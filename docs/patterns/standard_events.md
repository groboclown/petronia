# Standard Events and When To Use Them

Petronia comes with many standard event types that can be used in many flexible ways.  This guide can help you find the right ones to use, without needing to re-invent the wheel.

* [Lifecycle Events]()
* [Timed Events]()


## Lifecycle Events

WARNING: THIS IS OUT OF DATE.

This section refers to Petronia 2 APIs and usages.  It is here for development reference at the moment, and should not be used.

### Item Creation and Removal

The basic Petronia pattern doesn't have concepts of "objects", but that's a nice metaphor to use here.  Petronia calls these things "components", which it classifies as things that participate in the event system and where multiple of them can live.

Some extensions have need to allow the creation of their own, managed items.  For example, a tiling window manager will need to create and maintain the tiles wherein the windows position themselves.  Rather than devise your own set of events to manage these, try to take advantage of many of the existing Petronia lifecycle events.

Petronia components have a general category.  You may find it useful to define a singleton with the category name to define the manager of the components.  In some cases this may not be needed (for independent components that can be distinctly referenced), but in other cases it can be helpful to allow outside extensions to make bulk requests to the components through the manager.

Let's get down to nuts and bolts here.

#### Example: File Monitor

Let's say you want to make an extension that monitors directories and sends events when their file contents change.

Extensions can request to listen for changes by calling `send_request_new_component` to the file monitor component category with the name of the directory and a request ID, though they will generally use one of the helpers.

```python
from petronia.aid.lifecycle.create_component import create_component
from petronia.aid.std import (
    EventBus, UserMessage, ComponentId, ListenerSet, EventId, ParticipantId, log, WARN
)
from my.file.monitor.events import (
    TARGET_DIRECTORY_MONITOR_FACTORY,
    as_directory_changed_listener, DirectoryChangedEvent
)

def monitor_directory(bus: EventBus, listeners: ListenerSet, folder: str) -> None:
    def register_folder_listener(folder_monitor_id: ComponentId) -> None:
        listeners.listen(folder_monitor_id, as_directory_changed_listener, on_directory_changed)
    def create_failed(msg: UserMessage) -> None:
        log(WARN, monitor_directory, msg.debug())

    # This performs the send_request_new_component call, with the proper handling for creation answer listening,
    # failure handling, timeout handling, and shutdown awareness.
    create_component(bus, TARGET_DIRECTORY_MONITOR_FACTORY, folder, register_folder_listener, create_failed)


def on_directory_changed(_event_id: EventId, _target_id: ParticipantId, event: DirectoryChangedEvent):
    pass
``` 

The extension would declare the necessary events and usable values (`as_directory_changed_listener` as a `EventSetup`, and `DirectoryChangedEvent` as the event object).  It also adds in the event creation listeners.

```python
import os
from petronia.aid.std import EventBus, create_singleton_identity, ListenerSet, EventId, ParticipantId, UserMessage
from petronia.aid.std import i18n as _
from petronia.base.events import (
    RequestNewComponentEvent, as_request_new_component_listener,
    send_component_created_event, send_component_creation_failed_event
    
)

CATEGORY_DIRECTORY_MONITOR = 'my.file.monitor/directory'
TARGET_DIRECTORY_MONITOR_FACTORY = create_singleton_identity(CATEGORY_DIRECTORY_MONITOR)
ERROR_MESSAGE_NO_SUCH_DIRECTORY = _('directory does not exist: {dirname}')

def bootstrap_file_monitor(bus: EventBus) -> None:
    listeners = ListenerSet(bus)
    
    # general monitor event setup goes here

    def on_new_directory_monitor(_eid: EventId, _tid: ParticipantId, event: RequestNewComponentEvent[str]) -> None:
        if not os.path.isdir(event.construction_obj):
            # Tell the requestor that the component could not be created.
            send_component_creation_failed_event(
                bus, event, CATEGORY_DIRECTORY_MONITOR,
                UserMessage(ERROR_MESSAGE_NO_SUCH_DIRECTORY, dirname=event.construction_obj)
            )
            return
        # Create the new component ID for the new participant in the bus activities.
        file_monitor_cid = bus.create_component_id(CATEGORY_DIRECTORY_MONITOR)

        # add monitor work goes here

        # Send the notice that the monitor is now created.
        send_component_created_event(bus, event, file_monitor_cid)

    listeners.listen(TARGET_DIRECTORY_MONITOR_FACTORY, as_request_new_component_listener, on_new_directory_monitor)
```

If the monitor has additional work that it needs to perform before completing its setup, then the creation should be delayed until then.


## Timed Events

The Petronia standard uses a concept of a heartbeat to drive timed events.  This helps keep extensions running within the Petronia system.

The alternative to using the heartbeat would mean implementing a polling thread.  This uses resources in a way that Petronia can't manage, and can lead to inefficiencies.  It also puts the polling time outside the hands of the end-user.

