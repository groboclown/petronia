# About the Boot-Up Sequence

Petronia uses a combination of *configuration*, *launchers*, and *events* to start up the system in a well-defined and secure manner.

## Initial Startup

Starting up Petronia means launching the Foreman process.  Foreman has three responsibilities: loading the initial launchers as defined by the configuration, passing events between launchers, and stopping everything at shutdown.

The Foreman configuration should be a system-defined configuration that is dependent only upon the user's platform, and shouldn't be user edited.  The configuration includes things like location of translation files, and the launchers that should start at boot time.

The two main launchers that Petronia defines are the native and extension loader.  Foreman communicates to these through the event mechanism, just like all other launchers.

When the extension loader launcher runs, it starts a new process that handles loading extensions.  The launcher registers a specifically named channel that indicates that it is the only extension loader; anything else that later tries to register itself with that name will fail, and if the channel with that name ever ends while Foreman is in the "running" state, then Foreman enters a restart period.  The foreman process adds a special listener hook to the extension loader event stream, so that the extension loader private events are only processed when the extension loader generates them.

The extension loader will at startup begin the initial extensions.  When all of those extensions signal that they have started, the extension loader will send a `petronia.core.api.extension_loader:system-started` event.

## Launching Extensions

The extension loader sends requests to foreman to run extensions.  The process for loading an extension works like:

1. Extension loader wants to start extension XYZ.  The loader reads the meta-information about the extension, and determines the appropriate kind of launcher category to use for it.  This only matters for non-api extensions.  They declare a "runtime" section, which defines the launcher category and requested permissions.  The extension loader may decide, for security or other reasons, not to start the extension.
1. The extension loader sends a `petronia.core.api.foreman:start-launcher:request` event to Foreman.  This includes the requested launcher category and permissions.
1. Foreman receives this start-launcher request event, and maps the category name to a launcher implementation.  If the category is not registered, or the launcher refuses to use the permissions, then a `petronia.core.api.foreman:start-launcher:failed` response event is sent back to the extension loader.
1. The launcher category does its own thing for starting the "launcher", which is some processing unit that will load an extension.  That processing unit is assigned a unique "channel" for communication within the Foreman process.  This mechanism depends upon the launcher category implementation.  The communication with Foreman is done all in-process as part of the underlying Python code.
1. Success or failure of the launcher category channel creation is reported back as either a `start-launcher:failed` or `start-launcher:success` event back to the extension loader.  If it succeeds, the extension loader keeps going.
1. The extension loader sends a `petronia.core.api.foreman:launcher-load-extension:request` event to Foreman, using the same launcher ID that the success message included.  The extension loader has a window of time to send this after the `start-launcher:success` event is sent before the launcher is cleaned up due to inactivity.
1. The load extension request is passed on from Foreman to the launcher category.  The launcher category will internally communicate a success or failure back to Foreman, which will pass this in turn back to the extension loader as either a `launcher-load-extension:success` or `launcher-load-extension:failed` event.

If the request to load the extension came from a direct request from some other part of the system, then this event processing would be wrapped in the extension loader's own request / success / failed events.
