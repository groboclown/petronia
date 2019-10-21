# Base Petronia

The base Petronia design attempts to keep the core engine as small as possible.  The engine provides only the minimal events to run the engine.

## Events


### Event `petronia.bus.event-registry/listener-add`

* Event Id: **`petronia.bus.event-registry/listener-add`**
* Event Class: **`petronia.base.internal_.bus_events.EventListenerAddedEvent`**
* Queue Priority: **normal**
* Only instance triggering permitted
* Public listening allowed

Information about the added event listener.


There is no event triggered for removing an event listener.



### Event `petronia.bus.event-registry/register-event`

* Event Id: **`petronia.bus.event-registry/register-event`**
* Event Class: **`petronia.base.internal_.bus_events.RegisterEventEvent`**
* Queue Priority: **high**
* Public triggering allowed
* Only instance listening permitted

A request to add an event to the registration.



### Event `petronia.participant/dispose-complete`

* Event Id: **`petronia.participant/dispose-complete`**
* Event Class: **`petronia.base.internal_.dispose_events.DisposeCompleteEvent`**
* Queue Priority: **normal**
* Public triggering allowed
* Public listening allowed

Notification that a dispose completed.



### Event `petronia.participant/request-dispose`

* Event Id: **`petronia.participant/request-dispose`**
* Event Class: **`petronia.base.internal_.dispose_events.RequestDisposeEvent`**
* Queue Priority: **normal**
* Public triggering allowed
* Public listening allowed

Request for a participant to dispose itself.



### Event `petronia.registrar/component-created`

* Event Id: **`petronia.registrar/component-created`**
* Event Class: **`petronia.base.events.component_events.ComponentCreatedEvent`**
* Queue Priority: **normal**
* Public triggering allowed
* Public listening allowed

Reports that a component was created.



### Event `petronia.registrar/component-create-failed`

* Event Id: **`petronia.registrar/component-create-failed`**
* Event Class: **`petronia.base.events.component_events.ComponentCreationFailedEvent`**
* Queue Priority: **normal**
* Public triggering allowed
* Public listening allowed

Reports that a component creation attempt failed.



### Event `petronia.registrar/request-new-component`

* Event Id: **`petronia.registrar/request-new-component`**
* Event Class: **`petronia.base.events.component_events.RequestNewComponentEvent`**
* Queue Priority: **normal**
* Public triggering allowed
* Public listening allowed

to allow the called-back target to know which component was created.



### Event `petronia.participant/started`

* Event Id: **`petronia.participant/started`**
* Event Class: **`petronia.base.events.participant_events.ParticipantStartedEvent`**
* Queue Priority: **normal**
* Public triggering allowed
* Public listening allowed

ready to begin normal operation.  This should happen after configuration.



### Event `petronia.system/started`

* Event Id: **`petronia.system/started`**
* Event Class: **`petronia.base.events.system_events.SystemStartedEvent`**
* Queue Priority: **normal**
* Only instance triggering permitted
* Public listening allowed

running, and the system is now safe for end user actions.



### Event `petronia.system/halt`

* Event Id: **`petronia.system/halt`**
* Event Class: **`petronia.base.events.system_events.SystemHaltedEvent`**
* Queue Priority: **normal**
* Only instance triggering permitted
* Public listening allowed

Stop the system immediately.



### Event `petronia.system/error`

* Event Id: **`petronia.system/error`**
* Event Class: **`petronia.base.events.system_events.ErrorEvent`**
* Queue Priority: **high**
* Public triggering allowed
* Public listening allowed

anything.


This allows for localization of an error message, and to broadcast the issue to
different extensions that may have custom ways to handle the message.




*This file was auto-generated from the Petronia source on 2019-Oct-21.*
