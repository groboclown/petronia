# default.platform.windows (implementation)
**v1.0.0**

Windows platform API handler.


Low-level Windows API should be restricted to the `arch` package.  Those
functions declared in that package can be used elsewhere in this API.

## Details

Extension For:
* [core.platform.api](core.platform.api.md)
  no version restriction


Runs in elevated privileges

## User Configuration

Does not provide any user configuration.



## Dependencies

* [core.state.api](core.state.api.md)
  no version restriction






## Listens To Events

* Event Id **`core.state.api updated`**
  Target Id **`core.platform.api/hotkey-config`**
* Event Id **`core.platform.api/move-native-window`**
  Target Id **`*`**
* Event Id **`core.platform.api/focus-native-window`**
  Target Id **`*`**
* Event Id **`core.platform.api/close-native-window`**
  Target Id **`*`**
* Event Id **`core.platform.api/set-native-window-style`**
  Target Id **`*`**



Authors: Petronia

License: MIT

*This file was auto-generated from the Petronia source on 2019-Oct-21.*
