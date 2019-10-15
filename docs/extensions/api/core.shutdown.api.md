# API Extension core.shutdown.api v1.0.0

(no documentation provided)



Default Implementations:
* [default.shutdown.timer](default.shutdown.timer.md)
  no version restriction



## Declared Events


### Event `core.shutdown.api request-shutdown`

* Event Id: **`core.shutdown.api request-shutdown`**
* Event Class: **petronia.core.shutdown.api.events.RequestSystemShutdownEvent**
* Queue Priority: **normal**

Request that the Petronia system stop running.  When the system is ready to shut down, the SystemShutdownEvent is triggered by the event bus.

### Event `core.shutdown.api request-cancel-shutdown`

* Event Id: **`core.shutdown.api request-cancel-shutdown`**
* Event Class: **petronia.core.shutdown.api.events.RequestCancelSystemShutdownEvent**
* Queue Priority: **normal**

A request to stop the shutdown.

### Event `core.shutdown.api system-shutting-down`

* Event Id: **`core.shutdown.api system-shutting-down`**
* Event Class: **petronia.core.shutdown.api.events.SystemShutdownEvent**
* Queue Priority: **normal**

The system has started the shutdown phase.  The system will decide when to shut everything off.

### Event `core.shutdown.api shutdown-cancelled`

* Event Id: **`core.shutdown.api shutdown-cancelled`**
* Event Class: **petronia.core.shutdown.api.events.SystemShutdownCancelledEvent**
* Queue Priority: **normal**

The system shutdown is cancelled, and the system is back to normal operation.

### Event `core.shutdown.api system-shut-down-finalize`

* Event Id: **`core.shutdown.api system-shut-down-finalize`**
* Event Class: **petronia.core.shutdown.api.events.SystemShutdownFinalizeEvent**
* Queue Priority: **normal**

The system has finished the application shutdown phase, and it can no longer be cancelled.  At this point, system services must shutdown, and after a quiet period, the system will send a HALT event.




