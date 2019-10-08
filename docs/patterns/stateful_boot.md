# Stateful Startup

Some extensions, or parts of extensions, require the state to be loaded before starting itself up.  Without careful bootstrapping, this can lead to an object which has many unnecessary `if x is None` checks.

Instead, include a bootstrap that waits for the states to be registered.  The `StateWatch` class helps with this.

```python
from typing import Optional, Any
from petronia.aid.simp import (
    EventBus, EventId, ParticipantId,
    StateWatch, ListenerSet,
)
from some.extension import (
    STATE_ID_STATE1, State1,
    STATE_ID_STATE2, State2,
)

def bootstrap_component(bus: EventBus, listeners: ListenerSet):
    state1 = StateWatch(listeners, STATE_ID_STATE1, State1())
    state2 = StateWatch(listeners, STATE_ID_STATE2, State2())

    def check_startup(state: Any) -> None:
        if state1.is_set and state2.is_set:
            StatefulHandler(bus, listeners, state1, state2)
    
    state1.set_listener(check_startup)
    state2.set_listener(check_startup)


class StatefulHandler:
    def __init__(
            self, bus: EventBus, listeners: ListenerSet,
            state1: StateWatch[State1],
            state2: StateWatch[State2]
    ) -> None:
        state1.set_listener(self._on_state1)
        state2.set_listener(self._on_state2)
        ...
    
    def _on_state1(self, state: State1) -> None:
        ...
    
    def _on_state2(self, state: State2) -> None:
        ...
```

In this way, each state update is cached until all the states are ready.  Once the states are ready, the extension can begin.
