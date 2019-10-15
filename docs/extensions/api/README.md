# Extension Documentation

* [base](base.md) the core engine.
* [core.config_persistence.api](core.config_persistence.api.md) Configuration in Petronia is much more than some files.  It takes advantage of the state storage mechanism and applies readers and persistence on top of it.
* [core.extensions.api](core.extensions.api.md) (no documentation provided)
* [core.hotkeys.api](core.hotkeys.api.md) The API acts as a broker between applications that use hotkeys, and the low- level platform hotkey registration.
* [core.hotkeys.binding](core.hotkeys.binding.md) Defines the hotkey action types for core actions the user may want to perform.
* [core.layout.api](core.layout.api.md) (no documentation provided)
* [core.platform.api](core.platform.api.md) API that the platform components must implement.
* [core.shutdown.api](core.shutdown.api.md) (no documentation provided)
* [core.state.api](core.state.api.md) (no documentation provided)
* [core.theme.api](core.theme.api.md) Nearly all things that want to interact with the UI should do so through the theme, rather than through the platform directly.  The platform supports very low-level UI interaction, while the theme allows for much nicer looking components that the user can mildly control through configuration.  This means that the component interacting with the UI doesn't need to concern itself with the user definitions.
* [core.timer.api](core.timer.api.md) (no documentation provided)
* [core.validation.api](core.validation.api.md) (no documentation provided)
* [default.config_persistence](default.config_persistence.md) (no documentation provided)
* [default.extensions](default.extensions.md) (no documentation provided)
* [default.hotkeys](default.hotkeys.md) (no documentation provided)
* [default.state](default.state.md) (no documentation provided)
* [default.timer](default.timer.md) (no documentation provided)
* [default.configuration.file](default.configuration.file.md) This extension will wait for the `platform_state.PlatformConfigurationState` state event, then start the process of loading the events.  This will help ensure that loading will only happen after the state extension has started.
* [default.layout.tile](default.layout.tile.md) It allows for:
* [default.logging.console](default.logging.console.md) (no documentation provided)
* [default.shutdown.timer](default.shutdown.timer.md) (no documentation provided)


*This file was auto-generated from the Petronia source on 2019-Oct-15.*
