# Proposed Extensions

Extensions that could be added to the system.

## Remote Access

### Event Access

Event broadcast can be sent through a network connection to allow for external programs to participate in the event bus.  It can also allow for viewing the stream of events from the system.

In order to make the system secure, it should have a "code" that is generated for a connection, which is removed once attempted to be used.  The code should only be made available through the UI, and not through remote access.

### Logging

The logging system should be replaceable.  It could ship logs to some external system (unlikely for a UI thing), or make them available through a socket, for something akin to having a console that shows all the logs.

## Console

Utility program that allows interactive manipulation of the system.
