# core.platform.api (API)
**v1.0.0**

API that the platform components must implement.

## Details


### Declared Events


### Event `core.platform.api/component/request-create-chrome-wrapper`

* Event Id: **`core.platform.api/component/request-create-chrome-wrapper`**
* Event Class: **`petronia.core.platform.api.component.events.RequestCreateChromeWrapperEvent`**
* Queue Priority: **high**
* Public triggering allowed
* Only instance listening permitted

existing window.


If the chrome already exists, it is rejected.


If the chrome does not exist, then it should be created;
creation works and is accepted, then any reference to the native window ID
will go through the chrome.  This means extensions don't need special
handling for chrome handles; the platform invisibly handles it.


This is why there is a special creation event, rather than going through
the normal creation lifecycle - the created chrome will not be directly
callable.



### Event `core.platform.api hotkey-pressed`

* Event Id: **`core.platform.api hotkey-pressed`**
* Event Class: **`petronia.core.platform.api.user_input.hotkey.HotkeyPressedEvent`**
* Queue Priority: **high**
* Only instance triggering permitted
* Public listening allowed

(no documentation provided)

### Event `core.platform.api hotkey-progress`

* Event Id: **`core.platform.api hotkey-progress`**
* Event Class: **`petronia.core.platform.api.user_input.hotkey.HotkeyProgressEvent`**
* Queue Priority: **high**
* Only instance triggering permitted
* Public listening allowed

A hotkey sequence is being processed.


For limited use; specifically, a helper tool to display your progress in
entering a hotkey combo, and listing different next-key options, and what
they will do.



### Event `core.platform.api hotkey-progress-cancelled`

* Event Id: **`core.platform.api hotkey-progress-cancelled`**
* Event Class: **`petronia.core.platform.api.user_input.hotkey.HotkeyProgressCancelledEvent`**
* Queue Priority: **high**
* Only instance triggering permitted
* Public listening allowed

A hotkey sequence that was processed, is now cancelled.


For limited use; specifically, a helper tool to display your progress in
entering a hotkey combo, and listing different next-key options, and what
they will do.



### Event `core.platform.api native-window-closed`

* Event Id: **`core.platform.api native-window-closed`**
* Event Class: **`petronia.core.platform.api.window.action_occurred.NativeWindowClosedEvent`**
* Queue Priority: **high**
* Only instance triggering permitted
* Public listening allowed

The window was closed.  The corresponding state is removed.



### Event `core.platform.api native-window-created`

* Event Id: **`core.platform.api native-window-created`**
* Event Class: **`petronia.core.platform.api.window.action_occurred.NativeWindowCreatedEvent`**
* Queue Priority: **high**
* Only instance triggering permitted
* Public listening allowed

state changes for the window.


The state information for the newly created window may not be fully
defined.  Later state updates will fill out missing information.  State
is included here to allow for early inspection of the window to allow for
quick style or other updates before the window has much time to render.



### Event `core.platform.api native-window-flashed`

* Event Id: **`core.platform.api native-window-flashed`**
* Event Class: **`petronia.core.platform.api.window.action_occurred.NativeWindowFlashedEvent`**
* Queue Priority: **high**
* Only instance triggering permitted
* Public listening allowed

The window sent a request to alert the user about it.



### Event `core.platform.api native-window-focused`

* Event Id: **`core.platform.api native-window-focused`**
* Event Class: **`petronia.core.platform.api.window.action_occurred.NativeWindowFocusedEvent`**
* Queue Priority: **high**
* Only instance triggering permitted
* Public listening allowed

The window was given focus.



### Event `core.platform.api native-window-moved`

* Event Id: **`core.platform.api native-window-moved`**
* Event Class: **`petronia.core.platform.api.window.action_occurred.NativeWindowMovedEvent`**
* Queue Priority: **high**
* Only instance triggering permitted
* Public listening allowed

The window moved or resized or changed visibility.



### Event `core.platform.api/close-native-window`

* Event Id: **`core.platform.api/close-native-window`**
* Event Class: **`petronia.core.platform.api.window.action_requests.RequestCloseNativeWindowEvent`**
* Queue Priority: **normal**
* Public triggering allowed
* Only instance listening permitted

Send a request to close a window.



### Event `core.platform.api/focus-native-window`

* Event Id: **`core.platform.api/focus-native-window`**
* Event Class: **`petronia.core.platform.api.window.action_requests.RequestFocusNativeWindowEvent`**
* Queue Priority: **normal**
* Public triggering allowed
* Only instance listening permitted

may ignore the raise-to-top value.



### Event `core.platform.api/move-native-window`

* Event Id: **`core.platform.api/move-native-window`**
* Event Class: **`petronia.core.platform.api.window.action_requests.RequestMoveNativeWindowEvent`**
* Queue Priority: **normal**
* Public triggering allowed
* Only instance listening permitted

shouldn't change.



### Event `core.platform.api/request-visibility`

* Event Id: **`core.platform.api/request-visibility`**
* Event Class: **`petronia.core.platform.api.window.action_requests.RequestSetNativeWindowVisibility`**
* Queue Priority: **normal**
* Public triggering allowed
* Only instance listening permitted

hidden then hidden then visible will actions the window to visible.



### Event `core.platform.api/set-native-window-style`

* Event Id: **`core.platform.api/set-native-window-style`**
* Event Class: **`petronia.core.platform.api.window.action_requests.RequestSetNativeWindowStyleEvent`**
* Queue Priority: **high**
* Public triggering allowed
* Only instance listening permitted

highly dependent upon the underlying OS and windowing system.










## Dependencies

* [core.state.api](core.state.api.md)
  no version restriction



### Default Implementations:
* [default.platform](default.platform.md)
  no version restriction


## Source

Authors: Petronia

License: MIT

*This file was auto-generated from the Petronia source on 2019-Oct-24.*
