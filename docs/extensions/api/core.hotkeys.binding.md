# core.hotkeys.binding (stand-alone)
**v1.0.0**

Petronia Core Hotkey Bindings.


Defines the hotkey action types for core actions the user may want to perform.

## Details

Runs in elevated privileges

### User Configuration

Does not provide any user configuration.



### Provides Key Bindings

To bind a hotkey to an action, use this in the hotkey bind configuration:

```yaml
bind:
  - key: "ctrl+shift+a"
    action: "name of the action, which is in the title"
    parameters:
      example_parameter: "value"
``` 


#### `shutdown`

None




## Dependencies

* [core.hotkeys.api](core.hotkeys.api.md)
  no version restriction
* [core.shutdown.api](core.shutdown.api.md)
  no version restriction
* [core.validation.api](core.validation.api.md)
  no version restriction






## Listens To Events

* Event Id **`petronia.participant/request-dispose`**
  Target Id **`core.hotkey.binding`**
* Event Id **`core.shutdown.api system-shut-down-finalize`**
  Target Id **`core.shutdown.api`**
* Event Id **`core.hotkeys.api/trigger`**
  Target Id **`core.hotkey.binding`**



Authors: Petronia

License: MIT

*This file was auto-generated from the Petronia source on 2019-Oct-24.*
