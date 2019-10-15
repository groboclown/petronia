# API Extension core.layout.api v1.0.0

(no documentation provided)



Default Implementations:
* [default.layout.tile](default.layout.tile.md)
  no version restriction



## Declared Events


### Event `core.layout.api/layout-changed`

* Event Id: **`core.layout.api/layout-changed`**
* Event Class: **petronia.core.layout.api.events.LayoutChangedEvent**
* Queue Priority: **normal**

Triggered when the current layout on the screen changed.  This does not necessarily always get called when a new window is created; for example, a one-app (always maximized) layout would only send this event when the layout manager starts.

### Event `core.layout.api/request-resize`

* Event Id: **`core.layout.api/request-resize`**
* Event Class: **petronia.core.layout.api.events.RequestMoveResizeFocusedWindowEvent**
* Queue Priority: **normal**

User request to move and/or resize the currently focused window.

The interpretation of what a "change" means depends greatly upon the implementing layout.  See the specific layout's documentation for how to use this.

If the layout decides to accept the change request, it can trigger window move and layout change events.  It can change multiple windows and other parts of the system.

### Event `core.layout.api/request-shift`

* Event Id: **`core.layout.api/request-shift`**
* Event Class: **petronia.core.layout.api.events.RequestShiftLayoutFocusEvent**
* Queue Priority: **normal**

Request to shift where the layout is focusing.  This could be moving to another virtual workspace, switching to a different tile in a tiling system, flipping to another window in a full-screen layout, or any number of other options that are specific to the layout manager.

This super generic event takes a "name" and an "index", to allow a number and string input.

### Event `core.layout.api/request-visibility`

* Event Id: **`core.layout.api/request-visibility`**
* Event Class: **petronia.core.layout.api.events.RequestSetFocusedWindowVisibilityEvent**
* Queue Priority: **normal**

Request to change the window's visibility.  The layout may minimize or move off screen or in some other way hide the window from sight.  Making a window visible will restore it to the window's previous visibility setting.  Following the successful request, the focus should be the same as before setting the visibility. So, a separate request focus event may be necessary.




