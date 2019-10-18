# default.timer (implementation)
**v1.0.0**



## Details

Extension For:
* [core.timer.api](core.timer.api.md)
  no version restriction


Runs in elevated privileges

## User Configuration

Does not provide any user configuration.



## Dependencies

* [core.state.api](core.state.api.md)
  no version restriction






## Listens To Events

* Event Id **`petronia.participant/request-dispose`**
  Target Id **`default.timer`**
* Event Id **`core.shutdown.api system-shut-down-finalize`**
  Target Id **`core.shutdown.api`**
* Event Id **`core.state.api updated`**
  Target Id **`core.timer.impl config`**



Authors: Petronia

License: MIT

*This file was auto-generated from the Petronia source on 2019-Oct-18.*
