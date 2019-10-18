# default.hotkeys (implementation)
**v1.0.0**

(no documentation provided)

## Details

Extension For:
* [core.hotkeys.api](core.hotkeys.api.md)
  no version restriction


Runs in elevated privileges

## User Configuration

Does not provide any user configuration.







## Listens To Events

* Event Id **`petronia.participant/request-dispose`**
  Target Id **`default.hotkeys`**
* Event Id **`core.shutdown.api system-shut-down-finalize`**
  Target Id **`core.shutdown.api`**
* Event Id **`core.state.api updated`**
  Target Id **`default.hotkeys/setup-configuration`**
* Event Id **`core.hotkeys.api/master`**
  Target Id **`core.hotkeys.api`**
* Event Id **`core.hotkeys.api/register`**
  Target Id **`core.hotkeys.api`**
* Event Id **`core.hotkeys.api/remove`**
  Target Id **`core.hotkeys.api`**
* Event Id **`core.hotkeys.api/announce`**
  Target Id **`core.hotkeys.api`**
* Event Id **`core.platform.api hotkey-pressed`**
  Target Id **`core.platform.api/hotkey`**



Authors: Petronia

License: MIT

*This file was auto-generated from the Petronia source on 2019-Oct-18.*
