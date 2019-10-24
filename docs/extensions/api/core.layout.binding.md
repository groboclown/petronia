# core.layout.binding (stand-alone)
**v1.0.0**

Petronia Layout Hotkey Bindings.


Allows for adding hotkey binding to the standard layout events, so that the
different layouts don't need to re-implement all the bindings.  Instead,
they can just listen to the layout API events.


Layout implementations should depend upon this extension.

## Details

Runs in elevated privileges

### User Configuration

Does not provide any user configuration.



### Provides Key Bindings

To bind a hotkey to an action, use this in the hotkey bind configuration:

```yaml
bind:
  - key: "ctrl+shift+a"
    action: "name of the action, which is in the title"
    parameters:
      example_parameter: "value"
``` 


#### `move-active`


User request to move and/or resize the currently focused window.


The interpretation of what a "change" means depends greatly upon the
implementing layout.  See the specific layout's documentation for how
to use this.


If the layout decides to accept the change request, it can trigger
window move and layout change events.  It can change multiple windows
and other parts of the system.

```yaml
# Top-level item is some name the user prefers.  Here, we call it "Configuration".
Configuration:
  extension: move-active
  enabled: true
  properties:
    dx: (some number)
    dy: (some number)
    dw: (some number)
    dh: (some number)
    dz: (some number)

```


**Configuration.dx** : Change in window x position (move)

**Configuration.dy** : Change in window y position (move)

**Configuration.dw** : Change in window width (resize)

**Configuration.dh** : Change in window height (resize)

**Configuration.dz** : Change in window z-order (focus)



#### `shift-focus`


of other options that are specific to the layout manager.


This super generic event takes a "name" and an "index", to allow a
number and string input.

```yaml
# Top-level item is some name the user prefers.  Here, we call it "Configuration".
Configuration:
  extension: shift-focus
  enabled: true
  properties:
    name: "text"
    index: (some number)

```


**Configuration.name** : Layout focus shift name

**Configuration.index** : Layout focus shift index



#### `set-visible`


So, a separate request focus event may be necessary.

```yaml
# Top-level item is some name the user prefers.  Here, we call it "Configuration".
Configuration:
  extension: set-visible
  enabled: true
  properties:
    visible: (true / false)

```


**Configuration.visible** : True to make the window visible, False to make it hidden






## Dependencies

* [core.hotkeys.api](core.hotkeys.api.md)
  no version restriction
* [core.layout.api](core.layout.api.md)
  no version restriction






## Listens To Events

* Event Id **`petronia.participant/request-dispose`**
  Target Id **`core.layout.binding`**
* Event Id **`core.shutdown.api system-shut-down-finalize`**
  Target Id **`core.shutdown.api`**
* Event Id **`core.hotkeys.api/trigger`**
  Target Id **`core.layout.binding`**



Authors: Petronia

License: MIT

*This file was auto-generated from the Petronia source on 2019-Oct-24.*
