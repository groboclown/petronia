# core.hotkeys.binding (stand-alone)
**v1.0.0**

Petronia Core Hotkey Bindings.

Defines the hotkey action types for core actions the user may want to perform.

## Details

Runs in elevated privileges

## User Configuration

Does not provide any user configuration.



## Dependencies

* [core.hotkeys.api](core.hotkeys.api.md)
  no version restriction
* [core.shutdown.api](core.shutdown.api.md)
  no version restriction
* [core.validation.api](core.validation.api.md)
  no version restriction






## Listens To Events

* Event Id **`petronia.participant/request-dispose`**
  Target Id **`core.hotkey.core`**
* Event Id **`core.shutdown.api system-shut-down-finalize`**
  Target Id **`core.shutdown.api`**
* Event Id **`core.hotkeys.api/trigger`**
  Target Id **`core.hotkey.core`**



Authors: Petronia

License: MIT

*This file was auto-generated from the Petronia source on 2019-Oct-15.*
