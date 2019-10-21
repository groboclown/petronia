# core.extensions.api (API)
**v1.0.0**

(no documentation provided)

## Details


## Dependencies

* [core.state.api](core.state.api.md)
  no version restriction




## Declared Events


### Event `core.extensions.api request-load`

* Event Id: **`core.extensions.api request-load`**
* Event Class: **`petronia.core.extensions.api.events.RequestLoadExtensionEvent`**
* Queue Priority: **normal**
* Public triggering allowed
* Only instance listening permitted

Request to the extension loading mechanism to load an extension.


If the extension has already been loaded, then this will not generate a
corresponding ExtensionLoadedEvent.


Requesting extensions through an Event means that the version is up to the
extension API to determine.  Likewise, the extension can be loaded as an
insecure extension (forced into restricted access).



### Event `core.extensions.api loaded`

* Event Id: **`core.extensions.api loaded`**
* Event Class: **`petronia.core.extensions.api.events.ExtensionLoadedEvent`**
* Queue Priority: **normal**
* Only instance triggering permitted
* Public listening allowed

in the order that they were loaded.







Default Implementations:
* [defimpl.extensions](defimpl.extensions.md)
  no version restriction


Authors: Petronia

License: MIT

*This file was auto-generated from the Petronia source on 2019-Oct-21.*
