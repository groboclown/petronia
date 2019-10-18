# core.layout.binding (stand-alone)
**v1.0.0**

Petronia Layout Hotkey Bindings.


Allows for adding hotkey binding to the standard layout events, so that the
different layouts don't need to re-implement all the bindings.  Instead,
they can just listen to the layout API events.

## Details

Runs in elevated privileges

## User Configuration

Does not provide any user configuration.



## Dependencies

* [core.hotkeys.api](core.hotkeys.api.md)
  no version restriction
* [core.layout.api](core.layout.api.md)
  no version restriction






## Listens To Events

* Event Id **`petronia.participant/request-dispose`**
  Target Id **`core.layout.binding`**
* Event Id **`core.shutdown.api system-shut-down-finalize`**
  Target Id **`core.shutdown.api`**
* Event Id **`core.hotkeys.api/trigger`**
  Target Id **`core.layout.binding`**



Authors: Petronia

License: MIT

*This file was auto-generated from the Petronia source on 2019-Oct-18.*
