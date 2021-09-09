# Architecture

## Goals

* Loose coupling between components to an extreme.  Rather than owning other objects, objects contain references to them.  Communication between components happens in the event bus.  On top of this, the bus events are well-defined structured data packets.
* Separation between system state and components.  Things that other components may need to query (e.g. screen size, keyboard layout) are stored in a centralized state store that is event aware.  Components do not have direct access to system state.
* Safe coding practices.  Type safety to prevent incorrect usage as early as possible.  Defensively write the code.  Even though formal types may not be always the right way to go in Python, inspection is necessary.  If this becomes a performance issue, it should be a configuration option set at start time.
* Memory reduction.  The code will naturally want to use a lot of memory due to object proliferation.  Upfront work to make easy reduction in memory leak mistakes and simple memory reduction should be done.  Performance intensive tasks will naturally lend towards performance over memory, but these should be inspected carefully.


### Coding Guidelines

* Functions over objects.  Lifecycle controls should not be handled by the object itself, but by the framework that injects the object.  In this way, lifecycle is enforced.
* Slotted data objects over dictionaries.  Slots are faster to create and access and use less memory, and have better type safety.
* Convention over subclass.  Rather than enforcing type hierarchies, we'll enforce method existence.  With MyPy, this means Prototype declarations.
* Enforce read-only attributes through `@property` methods.  This may be a bit of a performance hit, so switching this will be on an individual basis.  Critical system parts will need to enforce read-only everywhere.  *May switch to using more Named Tuples*.
* API vs implementation.  At it's core, Petronia is a simple method for managing the execution and communication of different programs between each other through the event bus.  As a window manager, all the functionality is in extensions.  Any extension that can send data 
* All non-local memory must be accessed in a thread-safe manner.  For this reason, global memory must be restricted to just a few places.  This applies to singleton objects as well.
* Internationalization is a must.  Petronia uses the built-in `gettext` module for the application.  Extensions should expect the localization files to be added by the platform, and should produce files that can be integrated into the localization paths.
* `asyncio` over threading.  Threading is only used when Python makes it really difficult to use asyncio.  Unfortunately, this means forking behavior if threading is ever used, because of the underlying "async" vs non-async calls.


### Security

Petronia, as a kind of Window Manager, has access to many parts of the system which are sensitive, even if it's not running with high privileges.  Because of this, we must take care to ensure a rogue plugin can't cause harm.

#### Forking Model

Petronia splits its processing into multiple processes, to gain the aid of operating system controls to limit execution rights.  A few core processes has elevated privileges, but only in limited ways.

#### Extension Restrictions

One aspect to the security model is limiting which extensions can generate which events, and which events can be received.  Some very critical infrastructure events are highly protected.

The process spawning (performed by the *foreman* process)allows the creation of processes with different security permissions.  The event that requests this spawning can only be allowed by the *extension loader* process.  The events that register the allowed event producing is also handled by the *extension loader*.  The extension loader process is locked down and performs the necessary security inspections.  See the [lifecycle](lifecycle.md) document for more information.

#### Keyboard Capture

This can be abused in terrible ways.  The core system needs to restrict the keyboard shortcuts to a global key combination + user-defined combinations.  The "capture all" can't be used, but instead need to support input fields.

To help limit this, keyboard capture is also only run by the os handler process, and should be disabled in all other processes.

#### Screen Overlay

Cannot allow for arbitrary screen overly.  Instead, these need to be well contained and defined.

An example of an abuse vector includes masking a part of the screen to make the user think they're interacting with something they aren't.

### Extensions

The system allows for the user to install and load extensions.  This has inherent security implications of running untrusted code on your computer.  By default, extensions run in-process with Petronia and so have the same restrictions that the Petronia process has (very few).

Due to the issues with [Python sandboxing in CPython](https://python-security.readthedocs.io/security.html#sandbox), securing extensions requires running a separate Python interpreter in a child process with highly restricted access via OS protections, and have it communicate to the event bus via reading and writing from `stdin` and `stdout`.  This can be achievable through the extreme decoupling architecture and lack of a global data store.  Additionally, this means that a form of event trust is required for these remote events to prevent a malicious one performing actions it has no rights to; or, it could just be limited in the bus-interface to the child process.

Extensions themselves require support for signing and integrity verification.


### Event Protection

Some events may request major changes to the system that should only be done by trusted members due to the possibilities of malicious extensions.  For example, loading extensions should only be done by very specific parts of the software.

The system uses restrictions based on extension metadata to declare permissions around event sources and targets.  The Extension Loader tells the Foreman process the acceptable event permissions per extension, and the Foreman process enforces the permissions between extension runners.

The extensions themselves only allow for event declaration from the API extensions.  Events define the scope of the receivers and senders.  Events may allow for any extension to generate or receive the event (`public`), only the API implementation to generate or receive the event (`implementation`).

An additional component to Petronia is defining the event as a binary stream of data.  This prohibits highly sensitive parts of code from accidentally running code loaded from an extension.


## System Parts

### Extension vs Core Platform

The core platform for Petronia is a system for passing events between processes and the management of those processes.  This is made up of the Foreman process and the Extension Loader.  A detailed account of these two is described in the [lifecycle](lifecycle.md) document.  This basic setup allows for the rest of Petronia the Window Manager to work in an extensible and secure way.

Extensions are launched from the Foreman process and are granted permission to send and receive events.

There are four types of extensions:

* Protocol: define events which can only have public send/receive permissions.  These extensions only provide metadata for data sharing between extensions, and provide no code.
* API: defines events and declare a default implementation of the API.  API extensions declare events, but provide no code.  Each API extension loaded must have one and only one corresponding implementation extension loaded.
* Implementation: Provides code for an API extension.  This allows for switching between different kinds of code that is supposed to perform the same general operation.
* Stand-Alone: Provides code but does not implement an API.  It can declare dependencies on protocols and APIs to allow it to participate on those extension communications.

The extension loader discovers the installed extensions, parses them, and tells the Foreman process to run the implementations and stand-alone extensions.

Extensions can be stored in a distributable zip file.  The file name is in the form `full.module.name-v1.2.3.zip`.  If provided, PGP cryptographic signature files end with `.asc` and exist along-side the zip file.  All extension zips must provide hash files with extension `.sha3-256` (for SHA3-256 hash) or `.sha256` (for SHA2-256 hash) or both.  This means to use the extension extension, the sha3 libraries must be installed in the Python distribution.  For version 2.10.112 of extension "extension.name", a fully defined file structure is:

* `ext-dir/extension.name-v2.10.112.zip`
* `ext-dir/extension.name-v2.10.112.zip.sha256`
* `ext-dir/extension.name-v2.10.112.zip.sha3-256`
* `ext-dir/extension.name-v2.10.112.zip.asc`
* `ext-dir/extension.name-v2.10.112.zip.asc.sha256`
* `ext-dir/extension.name-v2.10.112.zip.asc.sha3-256`

Note that core modules (those distributed with Petronia) have an implicit version number that matches the version of Petronia.

The extension zip file must contain a `manifest.json` file that defines information about the extension (see [extension-schema.yaml](extension-schema.yaml) for details).

### Events

Due to the forking model of Petronia, all events are formally structured data.  This means they have a structure defined through a schema, and can be transmitted across the wire.  This allows for extensions to be written in any language.

The events are transmitted as either JSON formatted data objects or a simple binary blob, for transmitting images, which may be much larger.  See the [events document](events.md) for more information.

Each event is registered in the system using an event id, which *should* be in the form "extension.name:event-activity" to prevent name collisions.

### Processes

The *foreman* process has two responsibilities - the management of all the processes, and passing events between them.  Note that the process management includes the finalizing of the shutdown process.  If processes die, the foreman can restart them.  The event passing can enforce access rights, ensuring that a process that sends an event has the privilege to send it.

The *os handler* process manages the window management, keyboard handling, and other OS low-level events and actions.  Because of the extended permissions this requires, it runs independent of the other processes.  This also forces a nice separation between extensions and low-level graphics code, to make extensions more portable.

The *extension loader* process loads extensions and their configuration, then requests the primary process to start the corresponding process.


### Standard Extensions

Additional aspects of Petronia that aren't necessary for core operation.  Though these parts are considered "extensions", most are so basic to the underpinnings to the operation of Petronia that they are most always running.

#### State Store (Singleton)

Some aspects of the system are a global state that rarely updates.  For example, the screen resolution.  These states need to be made available to all participants of the system, but due to the loose coupling, the state itself cannot be put into an accessible place.  Likewise, participants may need to be aware of updates to those states.

The state store solves this problem by having a two-phase approach to state storage.  A participant announces the request to store an updated state, which the state store then uses to update the state storage, and, upon successful saving, it creates a "store update" event.

The state store has an interesting global data problem.  Specifically, how to make the initial state of a value available to a new listener.  The state store does this by listening to events for new event listeners of the state store itself, and sends out state updated events when they are added.  This means state update events can happen when no actual state change has occurred.

#### Native Handler (Singleton)

The platform must define a series of integration pieces to allow the system to start.

* Set up `gettext.install('petronia', '/usr/share/locale')` but with the appropriate paths for the platform.

#### Timer (Singleton)

A global timer (or "heartbeat") that generates an event at a configurable interval.  This allows for a user-defined global time to trigger things to run.

Components that rely on the timer should allow configuration to set how often to run based on the number of timer heartbeats (e.g. once every two heartbeats).

## Lifecycle

Different aspects of the system have their own way of interacting with Petronia.

### System Lifecycle

The standard Petronia lifecycle is:

1. The end user launches Petronia.  Normally, this is something equivalent to `python -m petronia_boot`
1. Pre-boot.  The main function discovers basic information about the current environment.
    * boot main method.
    * platform pre-boot implementations.
1. Boot.  The platform and core systems are started.
    * core extensions.
    * other fundamental extensions determined by the boot function.
    * extensions specified by user configuration and platform.
1. Event `petronia.core.api.extension_loader:system-started` sent.
1. System is under normal operation.
1. A component in the system sends a `RequestSystemShutdownEvent`.
1. A shutdown implementation extension takes over the UI and begins shutdown.
    1. Sends a `SystemShutdownEvent` when just before the UI switch.
    1. This is the equivalent under Windows of the "Shutting down" initial screen, where the end user can force programs to quit, or cancel the shutdown.
    1. Components need to register themselves to listen to this shutdown event, and begin termination.
    1. If the user wants to cancel the shutdown, then the interaction aspect sends a `RequestCancelSystemShutdownEvent`.
    1. If the shutdown extension cancels the shutdown, then when the system is returned to a normal operation state, it sends a `SystemShutdownCancelledEvent`.
    1. When the system has sufficiently finished the user part of the shutdown process and cancellation can no longer happen, the shutdown plugin sends `SystemShutdownFinalizeEvent`.
    1. When the shutdown implementation detects the applications and extensions have sufficiently stopped, it sends a `SystemHaltEvent`.  This must be a secure message.
1. When the Petronia kernel detects the `SystemHaltEvent`, the event bus is terminated, remaining threads are stopped, and the process exits.  Don't expect to have a plugin listen to that event and do something.

This assumes that the `shutdown` extension is installed by the boot system.


### Extension Lifecycle

Non-core extensions have a specific way for integrating into the system.


### Component Lifecycle

Because Petronia is loosely coupled, new components are created through the owning extension's factory, and events are generated to request the creation and to inform about the creation.

1. Source that desires the new component generates `RequestNewComponentEvent`.
    * Target ID is the extension factory ID that owns creating the component.
    * The callback target ID is an ID that the source listens to.
    * The request ID is a number that the source uses to distinguish this component creation request from others.
1. The extension factory attempts to create the component.
    * If the component can't be created, then a `ComponentCreationFailedEvent` is sent to the callback target ID of the request, with the request ID and error information.  Life cycle ends here.
    * If the component was created, then a `ComponentCreatedEvent` is sent to the callback target ID of the request with the request ID and the ID of the component that was created.  Life cycle continues.
1. If the component is aware of configuration, it will register itself to the configuration state, which will cause the state extension to send out the configuration.
1. When the component finishes initializing itself, it sends `ParticipantStartedEvent` with its own component ID.
1. At some future point, something may desire the component to be disposed.  That starts the disposal process.
1. The participant wanting to dispose the component send `RequestDisposeEvent` to the component ID.
1. The component removes any registered event bus listeners, and performs additional tear-down actions, then sends `DisposeCompleteEvent` to indicate that it completed the tear-down process.
1. The component may be involved in the user shutdown process, in which case it needs to listen to `SystemShutdownEvent` and `SystemShutdownCancelledEvent`, and handle those correctly.
1. The component listens to `SystemShutdownFinalizeEvent` to tear itself down.  It will send out the correct `DisposeCompleteEvent` events when it removes itself.


## Platform API Implementation Auto-Detection

One aspect of Petronia that needs some figuring out is the auto-detection of the Petronia platform.  The boot-time stuff is fine, but after that, it gets weird.

Windows is easy to detect.  Figuring out the Windows version is straight forward using standard Python tools.

For Linux, there are two separate standards at the moment - Wayland and X11.  This is compounded by Wayland compatibility with X11 protocols.  The work-around here is to force the end-user to select one or the other.


# History

* v1 - Early prototype
* v2 - Attempt at more structure, while understanding the needs of the system.
* v3.0 aleph - Switch to an event bus style, with well-defined event schema.
* v3.0 beth - Enforced forking model with event registration security.
