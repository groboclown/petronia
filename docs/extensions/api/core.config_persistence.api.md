# core.config_persistence.api (API)
**v1.0.0**

User Configuration Sub-System.


Configuration in Petronia is much more than some files.  It takes advantage of
the state storage mechanism and applies readers and persistence on top of it.


The internal participant configuration is handled through states. However,
whereas states are *pushed* from the owner to the system for announcing the
changes, the configuration is pushed from the configuration reader to the
component (backwards of states).


This configuration extension handles the different ways to read state and
persist it back.  Passing the configuration is done through the state system.

## Details


### Declared Events


### Event `core.config_persistence.api persist`

* Event Id: **`core.config_persistence.api persist`**
* Event Class: **`petronia.core.config_persistence.api.events.PersistConfigurationEvent`**
* Queue Priority: **I/O**
* Public triggering allowed
* Public listening allowed

which are called by this system "configuration collection".









### Default Implementations:
* [default.config_persistence](default.config_persistence.md)
  no version restriction


## Source

Authors: Petronia

License: MIT

*This file was auto-generated from the Petronia source on 2019-Oct-24.*
