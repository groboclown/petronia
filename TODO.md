# Running To-Do List

This is the to-do list for Petronia v3.1.


## Implementation Improvements

These are desired, tactical changes to bits of already written code.

### build

* raise the minimum coverage percent back up to 99.  It was dropped to 95 to get an initial good build.


### py-common-lib

* extension event schema doesn't capture the event description for binary events.  This is an artifact of how the events collect their data by using shared code.
* add unit test coverage on `petronia_common/extension/config/event_loader.py` (lines 83->96, 96, 389->390, 390)
* add unit test coverage on `petronia_common/extension/config/event_schema.py` (lines 870->874)
* add unit test coverage on `petronia_common/extension/runner/message_helper.py` (lines 58, 63-65, 70-72, 79-81, 95->97, 97)


### extension-tools

* make binary event classes generated better.  Right now, they are generated just like object event classes, and as a result they end up failing on lint and code coverage checks.
* improve test generation to have full coverage of some categories of events, such as data-store.


### extension-loader

* once the extension-tools are fixed to have improved test coverage of the events, take out the exclusion from the `.coveragerc` file.
* enforce the requirement that only one implementation of an API can be active at a time.  This should be added to the `order.py` file, `add_pending_extensions` function.
* document how the extension-loader searches for configuration files
* document the file format of its configuration files
* document how the extension-loader loads boot-time extensions
* define the access permissions required by the extension-loader.
* massive amounts of code coverage improvements


### foreman

* once the extension-tools are fixed to have improved test coverage of the events, take out the exclusion from the `.coveragerc` file.
* add extension name requirements around the in-memory loader, so that it denies loading an extension if it does not match the glob pattern.
* massive amounts of code coverage improvements
* document how the foreman process loads configuration files
* document the configuration file formats used by foreman
* change up the event router so that tests can have better insight into the status of the connected channels.  This may not be practical, but some method for gaining this insight can help eliminate the sleeps.  Perhaps some kind of spy into the internal buffers?


## High Level Ideas

These are ideas that need clarification and implementation.

### General

* Extension and launcher error reporting is now ad-hoc, and just sent to the stdout.  This should be redone as logging events.  However, those low-level errors, like failure to send a logging message, requires even lower level logging but in a common way.  Here, that low-level log fd may come in handy.


### extension-loader

* Should an explicit unload extension event be allowed?  If so, this will down-stream to foreman to add the corresponding event.


### portals

* migrate the older portals extension into this framework.
* it needs some improvements, add in portal component id, along with adding portals to the lifecycle.  Even though the portal creation call doesn't make much sense by itself (nothing outside the plugin can explicitly request a creation), the portal component ID and destruction do matter.


### theme

* an API extension for the theme, which sits on top of the native-handler to make common actions easy.
* allows for appearance choices to be made once for all extensions that want to create UI elements.


## Longer Term Improvements

Things that would be nice to have, but aren't necessary until more basic infrastructure is in place.

### extension-loader

* add loading extensions from a zip file.
    * When this is added, uncomment the no-cover bit from the extension code.
* add PGP and checksum validation to the zip loader.


### foreman

* add docker launcher.
* add [sandbox](https://chromium.googlesource.com/chromium/src/+/master/docs/design/sandbox.md) launcher.  If we eventually go with OSX, then Blastdoor would be another option.


## Old Code Carryover Improvements

## Tech Debt

Early development that caused rethinking of how things are done, but that code needs to be revisited to do over again.

* All state providers should also provide a `create_(state)_state_watch(ListenerSet)` function which returns a `StateWatch`.  This allows encapsulation of the state ID and typing.
* Make key-down metas have a timeout.  If too much time between keystrokes elapses, then the hotkey combo is canceled.
* Hotkey meta-characters should be passed as still down after hotkey is processed.
* Unit tests everywhere.


## Clean Up

* Remove the old v3.0 and v2 directories once the old code has been salvaged.
