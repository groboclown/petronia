# core.shutdown.api (API)
**v1.0.0**

(no documentation provided)

## Details




## Declared Events


### Event `core.shutdown.api request-shutdown`

* Event Id: **`core.shutdown.api request-shutdown`**
* Event Class: **`petronia.core.shutdown.api.events.RequestSystemShutdownEvent`**
* Queue Priority: **normal**
* Public triggering allowed
* Only instance listening permitted

to shut down, the SystemShutdownEvent is triggered by the event bus.



### Event `core.shutdown.api request-cancel-shutdown`

* Event Id: **`core.shutdown.api request-cancel-shutdown`**
* Event Class: **`petronia.core.shutdown.api.events.RequestCancelSystemShutdownEvent`**
* Queue Priority: **normal**
* Public triggering allowed
* Only instance listening permitted

A request to stop the shutdown.



### Event `core.shutdown.api system-shutting-down`

* Event Id: **`core.shutdown.api system-shutting-down`**
* Event Class: **`petronia.core.shutdown.api.events.SystemShutdownEvent`**
* Queue Priority: **normal**
* Only instance triggering permitted
* Public listening allowed

shut everything off.



### Event `core.shutdown.api shutdown-cancelled`

* Event Id: **`core.shutdown.api shutdown-cancelled`**
* Event Class: **`petronia.core.shutdown.api.events.SystemShutdownCancelledEvent`**
* Queue Priority: **normal**
* Only instance triggering permitted
* Public listening allowed

The system shutdown is cancelled, and the system is back to normal operation.



### Event `core.shutdown.api system-shut-down-finalize`

* Event Id: **`core.shutdown.api system-shut-down-finalize`**
* Event Class: **`petronia.core.shutdown.api.events.SystemShutdownFinalizeEvent`**
* Queue Priority: **normal**
* Only instance triggering permitted
* Public listening allowed

after a quiet period, the system will send a HALT event.







Default Implementations:
* [default.shutdown.timer](default.shutdown.timer.md)
  no version restriction


Authors: Petronia

License: MIT

*This file was auto-generated from the Petronia source on 2019-Oct-21.*
