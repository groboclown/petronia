# API Extension core.config_persistence.api v1.0.0

(no documentation provided)



Default Implementations:
* [default.config_persistence](default.config_persistence.md)
  no version restriction



## Declared Events


### Event `core.config_persistence.api persist`

* Event Id: **`core.config_persistence.api persist`**
* Event Class: **petronia.core.config_persistence.api.events.PersistConfigurationEvent**
* Queue Priority: **I/O**

A signal to persist a single configuration piece.  Only those write-enabled participants need to listen to this, and those that write a complete unit of configuration (for example, a configuration file or a registry sub-tree), which are called by this system "configuration collection".




