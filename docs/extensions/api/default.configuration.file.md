# default.configuration.file (stand-alone)
**v1.0.0**

Extension configuration through files.


This extension will wait for the `platform_state.PlatformConfigurationState`
state event, then start the process of loading the events.  This will help
ensure that loading will only happen after the state extension has started.

## Details

Runs in elevated privileges

## User Configuration

Does not provide any user configuration.



## Dependencies

* [core.state.api](core.state.api.md)
  no version restriction






## Listens To Events

* Event Id **`core.state.api updated`**
  Target Id **`default.configuration/platform-state`**
* Event Id **`petronia.participant/request-dispose`**
  Target Id **`default.configuration/platform-state`**
* Event Id **`core.shutdown.api system-shutting-down`**
  Target Id **`core.shutdown.api`**



Authors: Petronia

License: MIT

*This file was auto-generated from the Petronia source on 2019-Oct-18.*
