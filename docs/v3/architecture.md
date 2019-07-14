# Architecture

## Goals

* Loose coupling between components to an extreme.  Rather than owning other objects, objects contain references to them.  Communication between components happens in the event bus.
* Separation between system state and components.  Things that other components may need to query (e.g. screen size, keyboard layout) are stored in a centralized state store that is event aware.
* Safe coding practices.  Type safety to prevent incorrect usage as early as possible.  Defensively write the code.  Even though formal types may not be always the right way to go in Python, inspection is necessary.  If this becomes a performance issue, it should be a configuration option set at start time.
* Memory reduction.  The code will naturally want to use a lot of memory due to object proliferation.  Upfront work to make easy reduction in memory leak mistakes and simple memory reduction should be done.  Performance intensive tasks will naturally lend towards performance over memory, but these should be inspected carefully.

### Coding Guidelines

* Functions over objects.  Lifecycle controls should not be handled by the object itself, but by the framework that injects the object.  In this way, lifecycle is enforced.
* Slotted data objects over dictionaries.  Slots are faster to create and access and use less memory, and have better type safety.
* Convention over subclass.  Rather than enforcing type hierarchies, we'll enforce method existence.
* Enforce read-only attributes through `@property` methods.  This may be a bit of a performance hit, so switching this will be on an individual basis.  Critical system parts will need to enforce read-only everywhere.
* All non-local memory must be accessed in a thread-safe manner.  For this reason, global memory must be restricted to just a few places.  This applies to singleton objects as well.

### Security

Need to understand security concerns with plugins.

#### Keyboard Capture

This can be abused in terrible ways.  The core system needs to restrict the keyboard shortcuts to a global key combination + user-defined combinations.  The "capture all" can't be used, but instead need to support input fields.

#### Screen Overlay

Cannot allow for arbitrary screen overly.  Instead, these need to be well contained and defined.

Abuse vector is masking a part of the screen to make the user think they're interacting with something they aren't.

## Participant Types

### Identifiable

Nearly all participants in the system must be uniquely identifiable.  These are marked by the Identifiable class that provides an `id`.

### Component

A *component* is a participant with a lifecycle shorter than the application, for which there can be many of the same category.

All components must belong to a *category*, which is a named factory for components.


### Singleton


## Components

### Event Bus

The event bus handles communication between components to maintain loose coupling.  It is the most critical component of the system.  Its behavior must be well understood.

The event bus is the only part of the system allowed to store references to objects outside itself.  Unfortunately, because it is critical to getting everything to talk to other system parts, it must be shared between parts.

#### Event Bus Sharing

To better control memory usage, system parts are given a proxy object to the event bus.  This controls basic lifecycle usage of the bus.

* Event firing is done through the proxy.
* Event listener registration is done through the proxy.
* Deregistration is handled through events calling out to the component

### State Store

Some aspects of the system are a global state that rarely updates.  For example, the screen resolution.  These states need to be made available to all participants of the system, but due to the loose coupling, the state itself cannot be put into an accessible place.  Likewise, participants may need to be aware of updates to those states.

The state store solves this problem by having a two-phase approach to state storage.  A participant announces the request to store an updated state, which the state store then uses to

The state store has an interesting global data problem.  Specifically, how to make the initial state of a value available to a new listener.  The state store does this by listening to events for new event listeners of the state store itself, and sends out state updated events when they are added.  This means there can be multiple state update events 
