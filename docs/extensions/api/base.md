# Base Petronia

The base Petronia design attempts to keep the core engine as small as possible.  The engine provides only the minimal events to run the engine.

## Events


### Event `petronia.bus.event-registry/listener-add`

* Event Id: **`petronia.bus.event-registry/listener-add`**
* Event Class: **petronia.base.internal_.bus_events.EventListenerAddedEvent**
* Queue Priority: **normal**

Information about the added event listener.

There is no event triggered for removing an event listener.

### Event `petronia.bus.event-registry/register-event`

* Event Id: **`petronia.bus.event-registry/register-event`**
* Event Class: **petronia.base.internal_.bus_events.RegisterEventEvent**
* Queue Priority: **high**

A request to add an event to the registration.

### Event `petronia.participant/dispose-complete`

* Event Id: **`petronia.participant/dispose-complete`**
* Event Class: **petronia.base.internal_.dispose_events.DisposeCompleteEvent**
* Queue Priority: **normal**

Notification that a dispose completed.

### Event `petronia.participant/request-dispose`

* Event Id: **`petronia.participant/request-dispose`**
* Event Class: **petronia.base.internal_.dispose_events.RequestDisposeEvent**
* Queue Priority: **normal**

Request for a participant to dispose itself.

### Event `petronia.registrar/component-created`

* Event Id: **`petronia.registrar/component-created`**
* Event Class: **petronia.base.events.component_events.ComponentCreatedEvent**
* Queue Priority: **normal**

Reports that a component was created.

### Event `petronia.registrar/component-create-failed`

* Event Id: **`petronia.registrar/component-create-failed`**
* Event Class: **petronia.base.events.component_events.ComponentCreationFailedEvent**
* Queue Priority: **normal**

Reports that a component creation attempt failed.

### Event `petronia.registrar/request-new-component`

* Event Id: **`petronia.registrar/request-new-component`**
* Event Class: **petronia.base.events.component_events.RequestNewComponentEvent**
* Queue Priority: **normal**

Asks the component factory to create a new instance.  The target of the event is the component factory, which will be called with the request_id to allow the called-back target to know which component was created.

### Event `petronia.participant/started`

* Event Id: **`petronia.participant/started`**
* Event Class: **petronia.base.events.participant_events.ParticipantStartedEvent**
* Queue Priority: **normal**

Event to indicate that a participant finished initializing itself and is ready to begin normal operation.  This should happen after configuration.

### Event `petronia.system/started`

* Event Id: **`petronia.system/started`**
* Event Class: **petronia.base.events.system_events.SystemStartedEvent**
* Queue Priority: **normal**

Event to indicate that all the basic systems at boot time have finished running, and the system is now safe for end user actions.

### Event `petronia.system/halt`

* Event Id: **`petronia.system/halt`**
* Event Class: **petronia.base.events.system_events.SystemHaltedEvent**
* Queue Priority: **normal**

Stop the system immediately.

