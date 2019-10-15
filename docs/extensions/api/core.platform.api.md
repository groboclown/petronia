# API Extension core.platform.api v1.0.0

API that the platform components must implement.


Depends On Extensions:
* [core.state.api](core.state.api.md)
  no version restriction



Default Implementations:
* [default.platform](default.platform.md)
  no version restriction



## Declared Events


### Event `core.platform.api/component/request-create-chrome-wrapper`

* Event Id: **`core.platform.api/component/request-create-chrome-wrapper`**
* Event Class: **petronia.core.platform.api.component.events.RequestCreateChromeWrapperEvent**
* Queue Priority: **high**

When the theme (or anything else) wants to create chrome around an existing window.

If the chrome already exists, it is rejected.

If the chrome does not exist, then it should be created; creation works and is accepted, then any reference to the native window ID will go through the chrome.  This means extensions don't need special handling for chrome handles; the platform invisibly handles it.

This is why there is a special creation event, rather than going through the normal creation lifecycle - the created chrome will not be directly callable.

### Event `core.platform.api hotkey-pressed`

* Event Id: **`core.platform.api hotkey-pressed`**
* Event Class: **petronia.core.platform.api.user_input.hotkey.HotkeyPressedEvent**
* Queue Priority: **high**

(no documentation provided)

### Event `core.platform.api hotkey-progress`

* Event Id: **`core.platform.api hotkey-progress`**
* Event Class: **petronia.core.platform.api.user_input.hotkey.HotkeyProgressEvent**
* Queue Priority: **high**

A hotkey sequence is being processed.

For limited use; specifically, a helper tool to display your progress in entering a hotkey combo, and listing different next-key options, and what they will do.

### Event `core.platform.api hotkey-progress-cancelled`

* Event Id: **`core.platform.api hotkey-progress-cancelled`**
* Event Class: **petronia.core.platform.api.user_input.hotkey.HotkeyProgressCancelledEvent**
* Queue Priority: **high**

A hotkey sequence that was processed, is now cancelled.

For limited use; specifically, a helper tool to display your progress in entering a hotkey combo, and listing different next-key options, and what they will do.

### Event `core.platform.api native-window-closed`

* Event Id: **`core.platform.api native-window-closed`**
* Event Class: **petronia.core.platform.api.window.action_occurred.NativeWindowClosedEvent**
* Queue Priority: **high**

The window was closed.  The corresponding state is removed.

### Event `core.platform.api native-window-created`

* Event Id: **`core.platform.api native-window-created`**
* Event Class: **petronia.core.platform.api.window.action_occurred.NativeWindowCreatedEvent**
* Queue Priority: **high**

A new window was created.  Its state is stored with the window_id. Behavior such as the window moving or gaining focus are associated with state changes for the window.

The state information for the newly created window may not be fully defined.  Later state updates will fill out missing information.  State is included here to allow for early inspection of the window to allow for quick style or other updates before the window has much time to render.

### Event `core.platform.api native-window-flashed`

* Event Id: **`core.platform.api native-window-flashed`**
* Event Class: **petronia.core.platform.api.window.action_occurred.NativeWindowFlashedEvent**
* Queue Priority: **high**

The window sent a request to alert the user about it.

### Event `core.platform.api native-window-focused`

* Event Id: **`core.platform.api native-window-focused`**
* Event Class: **petronia.core.platform.api.window.action_occurred.NativeWindowFocusedEvent**
* Queue Priority: **high**

The window was given focus.

### Event `core.platform.api native-window-moved`

* Event Id: **`core.platform.api native-window-moved`**
* Event Class: **petronia.core.platform.api.window.action_occurred.NativeWindowMovedEvent**
* Queue Priority: **high**

The window moved or resized or changed visibility.

### Event `core.platform.api/close-native-window`

* Event Id: **`core.platform.api/close-native-window`**
* Event Class: **petronia.core.platform.api.window.action_requests.RequestCloseNativeWindowEvent**
* Queue Priority: **normal**

Send a request to close a window.

### Event `core.platform.api/focus-native-window`

* Event Id: **`core.platform.api/focus-native-window`**
* Event Class: **petronia.core.platform.api.window.action_requests.RequestFocusNativeWindowEvent**
* Queue Priority: **normal**

Set the window as focused and optionally raised to top.  Some platforms may ignore the raise-to-top value.

### Event `core.platform.api/move-native-window`

* Event Id: **`core.platform.api/move-native-window`**
* Event Class: **petronia.core.platform.api.window.action_requests.RequestMoveNativeWindowEvent**
* Queue Priority: **normal**

Request to move or resize a window.  A value of < 0 means that it shouldn't change.

### Event `core.platform.api/request-visibility`

* Event Id: **`core.platform.api/request-visibility`**
* Event Class: **petronia.core.platform.api.window.action_requests.RequestSetNativeWindowVisibility**
* Queue Priority: **normal**

Request to change the window's visibility.  The platform may minimize or move off screen or in some other way hide the window from sight.  Making a window visible may alter the original size.  Setting a hidden window to hidden, or a visible window to visible, is a no-op; setting a window hidden then hidden then visible will restore the window to visible.

### Event `core.platform.api/set-native-window-style`

* Event Id: **`core.platform.api/set-native-window-style`**
* Event Class: **petronia.core.platform.api.window.action_requests.RequestSetNativeWindowStyleEvent**
* Queue Priority: **high**

Send a request to set a window's native style.  The keys and values are highly dependent upon the underlying OS and windowing system.




