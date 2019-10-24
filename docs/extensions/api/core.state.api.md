# core.state.api (API)
**v1.0.0**

Standard API for the state.

## Details


### Declared Events


### Event `core.state.api request-update`

* Event Id: **`core.state.api request-update`**
* Event Class: **`petronia.core.state.api.events.StateStoreUpdateRequestEvent`**
* Queue Priority: **normal**
* Public triggering allowed
* Only instance listening permitted

The state in the store is updated.

### Event `core.state.api updated`

* Event Id: **`core.state.api updated`**
* Event Class: **`petronia.core.state.api.events.StateStoreUpdatedEvent`**
* Queue Priority: **normal**
* Only instance triggering permitted
* Public listening allowed

Reports that a state value was successfully updated.









### Default Implementations:
* [default.state](default.state.md)
  no version restriction


## Source

Authors: Petronia

License: MIT

*This file was auto-generated from the Petronia source on 2019-Oct-24.*
