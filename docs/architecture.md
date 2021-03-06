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
* API vs implementation.  The API for Petronia is the event bus, the event IDs and singleton IDs, and the event classes.  Everything else is implementation and should be registered separately from the API.  Extensions should have an API and implementation portion as well.  Users, if they really want, can swap out all the implementations, starting with extensions, all the way up to the core system setup at bootstrap time.
* All non-local memory must be accessed in a thread-safe manner.  For this reason, global memory must be restricted to just a few places.  This applies to singleton objects as well.
* Internationalization is a must.  Petronia uses the built-in `gettext` module for the application.  Extensions should expect the localization files to be added by the platform, and should produce files that can be integrated into the localization paths.
* Threading must be carefully handled.  Use `petronia.base.util.pthread` for any threading.

### Security

Need to understand security concerns with plugins.

#### Keyboard Capture

This can be abused in terrible ways.  The core system needs to restrict the keyboard shortcuts to a global key combination + user-defined combinations.  The "capture all" can't be used, but instead need to support input fields.

#### Screen Overlay

Cannot allow for arbitrary screen overly.  Instead, these need to be well contained and defined.

Abuse vector is masking a part of the screen to make the user think they're interacting with something they aren't.

### Extensions

The system allows for the user to install and load extensions.  This has inherent security implications of running untrusted code on your computer.  By default, extensions run in-process with Petronia and so have the same restrictions that the Petronia process has (very few).

Due to the issues with [Python sandboxing in CPython](https://python-security.readthedocs.io/security.html#sandbox), securing extensions requires running a separate Python interpreter in a child process with highly restricted access via OS protections, and have it communicate to the event bus via reading and writing from `stdin` and `stdout`.  This can be achievable through the extreme decoupling architecture and lack of a global data store.  Additionally, this means that a form of event trust is required for these remote events to prevent a malicious one performing actions it has no rights to; or, it could just be limited in the bus-interface to the child process.

Extensions themselves require support for signing and integrity verification.

### Trusted Events

Some events may request major changes to the system that should only be done by trusted members due to the possibilities of malicious extensions.  For example, loading extensions should only be done by very specific parts of the software.

The system supports adding a trust layer between an event generator and the event listener by cryptographically signing the event.  Additional effort can be made to encrypt the data in the event, if the data itself should not be read.

Due to the inability to truly lock down Python extensions in-memory, this only has impact when dealing with remote events.

One additional approach to help with this is the API vs. Implementation vs. Standalone aspects for extensions.  APIs should declare event types, and which ones are public vs. generated only by implementations; they must not register any event listeners nor generate events (other than event registration).  Implementation plugins must not declare any events, but can listen to and generate events.  Stand-alone plugins act as implementations that cannot generate private events.  Additionally, each API can have at most one implementation registered at a time.

### Untrusted Events 

One enormous weakness (from the security standpoint) in Petronia's current design is the use of classes as the event type.  This may not seem like much, but it introduces a dependency upon loading an extension to be able to transmit or receive an event.  This means that, using traditional methods, a package must be loaded, which means that it must have some of its code executed.  If this is untrusted code, it means it must be loaded in the trusted space, which is a break in the security guarantees.

However, we can recognize that Petronia has a wire-transmission form for its events, and there is no part of Petronia that requires the transmission of events while knowing the event contents.  Additionally, an extension must declare which events it is interested in receiving, which means that it declares to have access to that event.  On top of that, events (and thus the event class) are only declared by the API extensions.

This means that event objects only need to be generated and interpreted within the security context that directly uses them.  The parts of the system that shuffle events between senders and receivers only need to store the wire (marshalled) version. 

### Super Secure Petronia

With the extension execution in a separate process, this enables Petronia to be able to run in a highly secure environment.

The main process would need enough permission to be able to start processes that have all the permissions they need, but it would only be in charge of:

* Finding platform-specific information about the install, to know where to look for configuration files and extensions.
* Loading the most basic parts of the configuration, enough to know the basic deployment landscape.
* Launch sub-processes by permission grouping.  Platform UI manipulation would be in one process, execution child process would be in another, and so on.

This web of processes would listen on a local network port (could even be SSL with a once-per-load time self-signed certificate) for events.  The locally running event bus would translate "added listener" to include the listener's port number before sending it to all other processes.

This setup is a long term goal, but should be kept in mind when writing extensions and the core system.

To work around this 

## System Parts

### Base and Core

The "base" parts (put under the `petronia.base` module) provide the global, top-level core parts of Petronia that allows it to work.  Everything else is an extension.

The "core" parts are extensions that are expected to always be active for most extensions.  They are separated out, because the Petronia system could theoretically operate without them.

#### Identifiable Participants

Everything that wants to interact with the Petronia system needs an identifier.  Identifiers can either be *singletons* (hard coded, well defined values unique per singleton) or *components* (one instance of a class of participants).

These identifiers can cover a wide range of life cycle types, from lasting forever to being a one-off thing.  It can include the global state of a component separate from the component or be the component itself.

The nature of the singleton identifiers means that construction of them is done through the global function.  Components, though, require a synchronization across the system to properly ensure unique identifiers.  To allow for flexibility in the construction of these identifiers, it's abstracted out into the event bus, because the implementations of both will usually be linked (remote busses will need synchronization across all busses).  Singleton names and categories should be name spaced according to the extension's module name, to avoid collisions.

#### Logging

Logging is a global function made as flat and simple as possible.  It allows for registering "hooks" that can be fired for different source prefixes, and just triggers those on logging.

Thus, logging is highly configurable, allowing many different kinds of systems to integrate into it.

#### Event Bus and Base Events

The heart of Petronia.  It allows an extreme amount of loose coupling and extensibility by sending messages between components using only the identifier and a message.

Unlike the other base and core parts of the system, the event bus is passed between callers, rather than being a global variable.

The event bus incorporates several components:

* The bus itself, which sends events to registered listeners.  Events should be read-only.
* A type-safe layer on top of the event bus, which allows for registering event categories and a definition for events.
* A basic set of lifecycle event definitions.

The event bus' standard events are:

* Message sent whenever any listener is added.  Note that, for internal memory purposes, the corresponding de-registration does not generate an event.
* Messages sent to register an event type.
* A request to remove a participant from the system.  All non-core participants must be aware of this message.
* A notification when a participant completed its removal.  All non-core participants must send this message when completed removal.

Events run through the event bus can be one of several priorities.  These indicate a suggestion for when the event should run in relation to other events.  There is never a requirement that events run in the current thread or process, and instead events should be always thought of as running outside the thread of execution from the source that triggered it.  Likewise, there isn't a ordering to the events, as the event bus can make decisions about when to run them.

* HIGH - the event should run as soon as possible, before other events of a lower priority.  Event listeners for HIGH priority events should not run long operations, and instead delegate those to other events.
* NORMAL - the standard event processing priority.  Event listeners should not run long-blocking operations.
* IO - dedicated for long running, possibly blocking operations, such as reading from a network for file.  These almost always run in a thread separate from the others to prevent locking the event threads.

A special exception should be made for the `register event` action, because this must be handled before any other event to avoid a race condition where an event is registered, then delayed in a separate thread to run after the next event.

#### Events

Events are simple objects passed through the event bus.  Events must conform to the following restrictions:

* They use `__slots__`.  Event objects that show signs of anything in the hierarchy not using slots will not be registered.
* They do not allow `callable` types stored in the data.  This is strictly enforced for events that travel across the process boundary, for security purposes.
* They allow for serialization through the `petronia.base.util.serial` API.  This API dictates that all public properties can be passed as kvargs to the constructor, and no callable values are serialized.
* They should be read-only.
* Events that should not be transmitted across the process boundary should include a `disallow_process_transfer=True` property on the event instance.


Each event is registered in the system using an event id, which *should* be in the form "extension.name event-activity" to prevent name collisions.

### Components

Components are instances of a category of participants.  These have a specific lifecycle that must be adhered to, but that must be enforced by the extension that creates them.

Due to the possible remote event capability, the actions for a component may execute in any process, so the only way to request creation or communicate with them is through the events.


### Standard Extensions

Additional aspects of Petronia that aren't necessary for core operation.  Though these parts are considered "extensions", most are so basic to the underpinnings to the operation of Petronia that they are most always running.

#### Extensions

A definition for how to find and load modules into the Petronia system.

Extensions are implemented as Python modules, where the extension name matches the module name (including `.` separators for paths).

There are two types of extensions - extension API, which define events and data structures, and implementations.  Extension loading only defines the implementations to load.  Implementations can only depend upon API.  If the configuration does not define the implementation to load, it will default first to the internal definition, then to the external implementation if only one is found.

The extension module does not define the version, instead this is defined in the distributed extension filename.  The file name is in the form `full.module.name-v1.2.3.zip`.  If provided, PGP cryptographic signature files end with `.asc` and exist along side the zip file.  All extension zips must provide hash files with extension `.sha3-256` (for SHA3-256 hash) or `.sha256` (for SHA2-256 hash) or both.  This means to use the extension extension, the sha3 libraries must be installed in the Python distribution.  For version 2.10.112 of extension "extension.name", a fully defined file structure is:

* `ext-dir/extension.name-v2.10.112.zip`
* `ext-dir/extension.name-v2.10.112.zip.sha256`
* `ext-dir/extension.name-v2.10.112.zip.sha3-256`
* `ext-dir/extension.name-v2.10.112.zip.asc`
* `ext-dir/extension.name-v2.10.112.zip.asc.sha256`
* `ext-dir/extension.name-v2.10.112.zip.asc.sha3-256`

Note that core modules (those distributed with Petronia) have an implicit version number that matches the version of Petronia.

The extension zip file must contain a `manifest.json` file that defines information about the extension:

```javascript
{
    // Required information

    "type": "impl", // must be "api" or "impl" or "standalone"
    "depends": [
        // dependencies are ONLY for API.
        {
            "extension": "other.extension",
            "minimum": [ 1, 0, 0 ], // minimum required version; required
            "below": [ 2 ] // must be a version below this one; optional
        }
    ],

    // If type is "impl", then these MUST be provided.
    // If type is "api" or "standalone", then these MUST NOT be provided.
    // Note that an extension can implement multiple APIs.
    "implements": [{
        // API name that this implements.
        "extension": "that.extension",
        "minimum": [ 1, 0, 0 ], // minimum API compatible version; required
        "below": [ 2 ] // API must be a version below this; optional
    }],

    // If type is "api", then this MUST be provided.
    // If type is "impl" or "standalone", then this MUST NOT be provided.
    "defaults": [{
        // Ordered list of default implementations for this API.
        "extension": "my.extension.api",
        "minimum": [ 9, 100, 4 ],
        "below": [ 4, 0, 0 ]
    }],

    // Non-zip distributions MUST provide these.
    // For zip distributed extensions, the extension name and version are
    // implicit in the zip file name.  This means creating the distribution
    // file doesn't need to modify the contents of this file, and these
    // values are ignored.
    "name": "extension.name",
    "version": [ 100, 2, 0 ],

    // Optional information
    "description": "A long description for this extension.",
    "authors": [ "author1", "author2" ],
    "homepage": "https://my.url/home/page",
    "license": "MIT"

}
```

Extension modules must provide the function `start_extension` which takes a single argument, the `EventBus` instance.  This function must register event types and add listeners as appropriate for the module.  If the module adds event listeners, it must also add an event listener for the `RequestDisposeEvent` event, to allow for the module to be removed.  The `petronia3.ext_help.module_bootstrap` module can help with this.  Events to dispose the extension will be sent to the module name of the extension.

If an extension allows for configuration setup events, these are sent by the configuration setup extension to a default state ID of `(extension module name)/setup-configuration`.  The configuration state value will be the raw JSON-like decoded values, without any object wrapper.  The extension can listen for additional configurations, all must start with the extension module name + `/`

For core and local extensions, the module must provide the `EXTENSION_METADATA` value set to a dictionary in the same format as the JSON above.

#### State Store (Singleton)

Some aspects of the system are a global state that rarely updates.  For example, the screen resolution.  These states need to be made available to all participants of the system, but due to the loose coupling, the state itself cannot be put into an accessible place.  Likewise, participants may need to be aware of updates to those states.

The state store solves this problem by having a two-phase approach to state storage.  A participant announces the request to store an updated state, which the state store then uses to update the state storage, and, upon successful saving, it creates a "store update" event.

The state store has an interesting global data problem.  Specifically, how to make the initial state of a value available to a new listener.  The state store does this by listening to events for new event listeners of the state store itself, and sends out state updated events when they are added.  This means state update events can happen when no actual state change has occurred.

##### Configuration

Configuration in Petronia is much more than some files.  It takes advantage of the state storage mechanism and applies readers and persistence on top of it.  Each component can make itself configuration aware by adding a state store object (will need to be a singleton) and listen for changes to it, and send events for its own changes to the configuration.

From the configurable component perspective, configuration is a *push* operation - the configuration extension loads the configuration and sends out the configuration state to the state store.  The configurable component loads a default configuration at startup time, and listens for the configuration state changes.

Another possible state is a *session*, which is for intermediary states.  For example, a tile split and pixel position could be saved in the session, so the user can resume the previous setup when the UI is restarted.

If an extension allows for configuration setup events, these are sent by the configuration setup extension to a state ID of `(extension module name)/setup-configuration`.  The configuration state value will be the raw JSON-like decoded values, without any object wrapper.

The `default.configuration.file` extension loads configuration information from the file system, using a state created by the bootstrap.  Each loaded file is either a `json` or `yaml` file that defines the extensions to load, and how to configure them.


#### Platform (Singleton)

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
1. Event `SystemStartedEvent` sent.
    * TODO how do we know when to send this?  Will probably require a new extension
      that listens for created events from the extensions, and when certain ones complete,
      it sends out that event.
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
