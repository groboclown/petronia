# About Extensions

Petronia gets most of its power from extensions and the event bus for shuffling events between them.

Extensions are broken into these categories: 

* Protocol: define events which can only have public send/receive permissions.  These extensions only provide metadata for data sharing between extensions, and provide no code.
* API: defines events and declare a default implementation of the API.  API extensions declare events, but provide no code.  Each API extension loaded must have one and only one corresponding implementation extension loaded.
* Implementation: Provides code for an API extension.  This allows for switching between different kinds of code that is supposed to perform the same general operation.
* Stand-Alone: Provides code but does not implement an API.  It can declare dependencies on protocols and APIs to allow it to participate on those extension communications.
