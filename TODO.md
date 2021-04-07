# Running To-Do List

This is the to-do list for Petronia v3.1.


## Implementation Improvements

These are desired, tactical changes to bits of already written code.

### build

* raise the minimum coverage percent back up to 99.  It was dropped to 90 to get an initial good build.


### core-extensions

* finish shutdown extension design.  This needs to borrow heavily from the v3.0 notes.
* hotkey-binding needs de-register for extension events.
* the timer extension needs to have a configuration protocol, and listen for changes to the configuration for the timer interval.
* the timer extension needs to send timer events at an interval.


### native

* once the extension-tools are fixed to have improved test coverage of the events, take out the exclusion from the `.coveragerc` file.
* for the ui extension, it must have absolute position for the outer window, but the inner components must be relative, because text display is dynamic (it looks up translations).  On that note, text must also be rotatable, and notes should be made that implementors *should* support BiDi.
* `native-hotkey-extenison.yaml` defines `bound-hotkey` as a structure containing an array.  This is due to a limitation in the generator.  If the generator can eventually deal with this, then it should go back to being an array.
* Running lint on the generated events tree takes minutes to run, so these are currently omitted in the `pylintrc` file.
* `native-ui-extension.yaml` produces a cycle, which is fine, but the generated data structures don't appear.
* Turn back off the `func_*.py` disabled in the code coverage (`.coveragerc`).
* Remove the `fixme` that's been disabled in the lint config (`pylintrc`).
* The `monitor_screen.py` common function `store_virtual_screen_state` should take into account the real dpi + screen mapping distortion.  Right now, the ratio is hard-coded as 1-1.
* `virtual_screen` config matching updates:
  * needs to take priority on user configurations, and include default ones if no user configuration matches "enough".
  * add a limit to config matching; if a match is not above a certain value, then it isn't used.
* Windows:
  * test out running the loop with monitor change detection, attach a second monitor, ensure the monitor detection happens, then move the relative positions between monitors, and ensure that the monitor change detection happens again.
* Hotkey chain requires meta-characters that are still pressed after ok should then be passed again; the hotkey chain forgets meta-characters one the action is completed.  This shows itself as a bug where pressing a hotkey requires releasing then pressing the meta-keys again.


### py-common-lib

* extension event schema doesn't capture the event description for binary events.  This is an artifact of how the events collect their data by using shared code.
* add unit test coverage on `petronia_common/extension/config/event_loader.py` (lines 83->96, 96, 389->390, 390)
* add unit test coverage on `petronia_common/extension/config/event_schema.py` (lines 870->874)
* add unit test coverage on `petronia_common/extension/runner/message_helper.py` (lines 58, 63-65, 70-72, 79-81, 95->97, 97)
* Create asyncio versions of read & write events.  This essentially forks the API, making duplicates of all kinds of things.  However, only Foreman should be using the thread version.  *This may not be needed.  It could be that most things are single-threaded.*


### py-extension-lib

* migrate the extension library parts out of py-common-lib into this project.
  * `petronia_common.extension.runner`
* once the extension-tools are fixed to have improved test coverage of the events, take out the exclusion from the `.coveragerc` file.
* increase coverage.
* look into making the tools here use asyncio rather than threading.


### extension-tools

* improve test generation to have full coverage of some categories of events, such as data-store.
* binary event unit test classes should not exist.  Or should be made differently.
* random number generator should have a seed based on extension information, so that regenerating the tests will have consistent test data.  Maybe a seed can be set in the yaml file?
* after the change to allow cycles, the source generator is horribly slow.  Need to figure out where the slow-down is happening.  Probably in the cycle code ;)
    * Checking the runtime performance, it looks like the majority of the time comes from creating the structures.
* some generators include `cast` import when it isn't used, which causes a pylint error.
* the generation of child object parsers needs an added check for is-dict.  If it's something like an array or number, then an exception is raised.


### portal

* minimum portal size is hard-coded to 10, 10

### extension-loader

* once the extension-tools are fixed to have improved test coverage of the events, take out the exclusion from the `.coveragerc` file.
* enforce the requirement that only one implementation of an API can be active at a time.  This should be added to the `order.py` file, `add_pending_extensions` function.
* complete the `request_listener_change_handler` functionality, and wire it up in the `event_router`.
* document how the extension-loader searches for configuration files
* document the file format of its configuration files
* document how the extension-loader loads boot-time extensions
* define the access permissions required by the extension-loader.
* code coverage improvements


### foreman

* once the extension-tools are fixed to have improved test coverage of the events, take out the exclusion from the `.coveragerc` file.
* add extension name requirements around the in-memory loader, so that it denies loading an extension if it does not match the glob pattern.
* code coverage improvements
* document how the foreman process loads configuration files
* document the configuration file formats used by foreman
* change up the event router so that tests can have better insight into the status of the connected channels.  This may not be practical, but some method for gaining this insight can help eliminate the sleeps.  Perhaps some kind of spy into the internal buffers?
* `cmd_launcher_test` doesn't work well with Windows on Travis builds.  This could be a timing issue.
* foreman currently has a build dependency on `py-extension-lib` in order to share some very targeted behavior.  Should this be moved over to `py-common-lib`?  Currently, `py-common-lib` includes the arg-handler logic that is only used by extensions, so either move that arg handler over to extension lib, or move the foreman dependent stuff into py-common-lib.
* should there be an implementation file for foreman?  It should never be started by the extension loader, but it may need it for completing its graph.


### py-extension-lib

* data event listener needs to include a carefully designed listener.  If it's really nice, it can take the event object class and extrapolate all data from that.


## High Level Ideas

These are ideas that need clarification and implementation.

### General

* Extension and launcher error reporting is now ad-hoc, and just sent to the stdout.
  * Where possible, this should be redone as logging events.  This should be moved into the py-extension-lib project.  If sending events fails, then the logging should be a consistent output that doesn't spam the user.
* Allow for an additional data field type for events - zlib compressed object data.
  * The maximum size for the underlying data should remain the same.


### on-the-fly configuration saving

* Create an extension that will, on a send event, store all "configuration" data store items to disk.  This will use a defined directory that should be in the override directory that the extension-loader reads.  The process should go like: the extension listens for the save request, when it's received, the extension first gets all active extensions (from datastore), then requests datastore to send out all `(extension-name):configuration` data objects.  The ones that are returned are saved to disk under `(extension-name).json` in the override directory.


### extension-loader

* Should an explicit unload extension event be allowed?  If so, this will down-stream to foreman to add the corresponding event.
* The "extension-dirs" should be better implemented.  It's kind of weird now.  It was originally designed with the idea of absolute paths, but relative paths would be better.  There's a sort-of okay work-around now by being able to use DATA_DIR and SYS_PATH values.


### foreman

* stdout from launched processes should be redirected to the logging fd.
* due to the memory launcher, normal stdout should also be specially handled.
* memory launcher needs to add an extra requirement to have full initialization, including resetting module data, on extension loading.  This allows restart actions to be more consistent.


### portals

* migrate the older portals extension into this framework.
* it needs some improvements, add in portal component id, along with adding portals to the lifecycle.  Even though the portal creation call doesn't make much sense by itself (nothing outside the plugin can explicitly request a creation), the portal component ID and destruction do matter.
* portals use the theme for drawing borders.


### theme

* an API extension for the theme, which sits on top of the native-handler to make common UI element creation and manipulation easy.
* allows for appearance choices to be made once for all extensions that want to create UI elements.


### hotkey-bindings

* mapping between hotkey combinations and an action to run.
* registering key combinations here indirectly performs the registration of hotkey actions in the native extension.
* "actions" for the binding should be public sending events.  This unfortunately means that the extension needs to be able to send any event, but the extension loader security restrictions prevent this.  What other approaches are there?  Datastore may be one, but that's not a good match.  Could also have a hotkey binding API notification system that means extensions must be explicitly hotkey-bind enabled; this would be forward compatible across user configurations, and give users a consistent configuration, maybe.


## Longer Term Improvements

Things that would be nice to have, but aren't necessary until more basic infrastructure is in place.


### build

Now that pylint supports Python 3.9, look at migrating to that.


### extension-loader

* add loading extensions from a zip file.
    * When this is added, uncomment the no-cover bit from the extension code.
* add PGP and checksum validation to the zip loader.


### foreman

* add docker launcher.
* add [sandbox](https://chromium.googlesource.com/chromium/src/+/master/docs/design/sandbox.md) launcher.  If we eventually go with OSX, then Blastdoor would be another option.


### native-handler

* It may be useful to have the handler be multi-process rather than multi-threaded, to have better performance on the main UI loop. 


## Old Code Carryover Improvements

## Tech Debt

Early development that caused rethinking of how things are done, but that code needs to be revisited to do over again.

* All state providers should also provide a `create_(state)_state_watch(ListenerSet)` function which returns a `StateWatch`.  This allows encapsulation of the state ID and typing.
* Unit tests everywhere.


## Clean Up

* Remove the old v3.0 and v2 directories once the old code has been salvaged.
