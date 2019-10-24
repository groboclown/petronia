# default.layout.tile (implementation)
**v1.0.0**

The Petronia tiling extension.


It allows for:
* splitting the screen up into sections;
* having different splits depending on the monitor resolution;
* virtual screens;
* dynamic splitting, based on per screen settings;
* overlapping windows.


The UI is split into "portals" and "containers".  A portal is a place where
zero or more UI windows are stored.


Make sure you define the configuration for this extension in order to customize
the layout.


**Key Binding Guide:**


The layout API provides generic key bindings, which, for this layout, have these meanings:


* `move-active`: Adjusts the size and position of the active portal, if possible.
Only one of `dx` and `dy`, or `dw` and `dh` need be specified; the layout will
use the correct one for the owning split's direction.
Moving a portal (dx or dy) means resizing the sibling tiles so the active portal
keeps its ame size.
The `dz` has a special meaning - it flips the active window within the portal.
* `shift-focus`: Changes the currently focused portal.  Uses the `name` to indicate
the direction, and `index` to indicate the amount of move.  The direction names
recognized are 'n', 's', 'e', and 'w'.  An index of 0 will be interpreted as a 1
(this is due to the way Petronia handles the index if it isn't specified).
The layout configuration defines whether the focus will wrap-around to the other side.
FIXME add an option to move focus to a named portal.
FIXME add an option to move the active window to a different portal.
* `set-visible`: if `visible` is True, then it minimizes the currently active
window in the currently active portal.  If `visible` is False, then it restores the
currently active window; explore what this means on your own!



## Details

Extension For:
* [core.layout.api](core.layout.api.md)
  no version restriction


Runs in elevated privileges

### User Configuration


(no documentation)

```yaml
# Top-level item is some name the user prefers.  Here, we call it "Configuration".
Configuration:
  extension: default.layout.tile
  enabled: true
  properties:
    match-windows:
      # one or more of these types
      -
        portal: "text"
        position: "text"
        key: "text"
        match: "text"
        type: "text"
        matchers:
          # one or more of these types
          -
            key: "text"
            match: "text"
            type: "text"
    layouts:
      # one or more of these types
      -
        name: "text"
        screens:
          # one or more of these types
          -
            resolution: "text"
            name: "text"
            direction: "text"
            target: (true / false)
            splits:
              # one or more of these types
              -
                # Sub-Schema Definition: split-layout
                target: (true / false)
                name: "text"
                size: (some number)
                splits:
                  # one or more of these types
                  -
                    (a "split-layout" sub-schema value)
                  -
                    name: "text"
                    size: (some number)
                    default-position: "text"
              -
                name: "text"
                size: (some number)
                default-position: "text"
      -
        resolution: "text"
        name: "text"
        direction: "text"
        target: (true / false)
        splits:
          # one or more of these types
          -
            # Sub-Schema Definition: split-layout
            target: (true / false)
            name: "text"
            size: (some number)
            splits:
              # one or more of these types
              -
                (a "split-layout" sub-schema value)
              -
                name: "text"
                size: (some number)
                default-position: "text"
          -
            name: "text"
            size: (some number)
            default-position: "text"

```


**Configuration.match-windows[].portal** : name of the portal that the window will go into by default

**Configuration.match-windows[].position** : corner to align the window (fill, ne, se, nw, sw, n, e, s, w, and r- variants),
            or not set if it is resized

**Configuration.match-windows[].key** : window property key to match

**Configuration.match-windows[].match** : text to match against the window property key value

**Configuration.match-windows[].type** : type of matching to use: glob (default), partial, exact, or regex

**Configuration.match-windows[].matchers[].key** : window property key to match

**Configuration.match-windows[].matchers[].match** : text to match against the window property key value

**Configuration.match-windows[].matchers[].type** : type of matching to use: glob (default), partial, exact, or regex

**Configuration.layouts[].name** : layout name, for logging purposes

**Configuration.layouts[].screens[].resolution** : screen resolution to match against, in the form WIDTHxHEIGHT (e.g. `1024x768`)

**Configuration.layouts[].screens[].name** : screen name or index to match against

**Configuration.layouts[].screens[].direction** : Initial split direction.  Deeper splits will alternate.

**Configuration.layouts[].screens[].target** : TRUE if this is where the user-triggered splits will happen

**split-layout.target** : TRUE if this is where the user-triggered splits will happen

**split-layout.name** : An optional name for the portal, for use with matching or quick focus on key bindings

**split-layout.size** : Proportional size of the split, to its siblings

**split-layout.splits[]** : split-layout

**split-layout.splits[].name** : An optional name for the portal, for use with matching or quick focus on key bindings

**split-layout.splits[].size** : proportional size of the area

**split-layout.splits[].default-position** : Position for windows inserted into the portal (fill, n, e, s, w, ne, nw, se, sw, and r- variants).

**Configuration.layouts[].screens[].splits[].name** : An optional name for the portal, for use with matching or quick focus on key bindings

**Configuration.layouts[].screens[].splits[].size** : proportional size of the area

**Configuration.layouts[].screens[].splits[].default-position** : Position for windows inserted into the portal (fill, n, e, s, w, ne, nw, se, sw, and r- variants).

**Configuration.layouts[].resolution** : screen resolution to match against, in the form WIDTHxHEIGHT (e.g. `1024x768`)

**Configuration.layouts[].direction** : Initial split direction.  Deeper splits will alternate.

**Configuration.layouts[].target** : TRUE if this is where the user-triggered splits will happen

**Configuration.layouts[].splits[].name** : An optional name for the portal, for use with matching or quick focus on key bindings

**Configuration.layouts[].splits[].size** : proportional size of the area

**Configuration.layouts[].splits[].default-position** : Position for windows inserted into the portal (fill, n, e, s, w, ne, nw, se, sw, and r- variants).





### Provides Key Bindings

To bind a hotkey to an action, use this in the hotkey bind configuration:

```yaml
bind:
  - key: "ctrl+shift+a"
    action: "name of the action, which is in the title"
    parameters:
      example_parameter: "value"
``` 


#### `set-window-position`


Allows to, on the fly, change how the active window sizes itself within the portal.

```yaml
# Top-level item is some name the user prefers.  Here, we call it "Configuration".
Configuration:
  extension: set-window-position
  enabled: true
  properties:
    position: "text"

```


**Configuration.position** : The same value for the matcher is used here (n, s, e, w, ne, nw, se, sw, and the `r-` variants).



#### `name-portal`



            Gives the active portal a name, so that other hotkeys can reference it.  This is useful to, on the fly,
            change the destination for a common collection of hotkeys.  For example, you can name a portal
            'run', then have a series of hotkeys to move a window to 'run', and quickly move the focus to 'run',
            then have an accompanying series of hotkeys for 'edit', to enable quick navigation between the two.
            

```yaml
# Top-level item is some name the user prefers.  Here, we call it "Configuration".
Configuration:
  extension: name-portal
  enabled: true
  properties:
    name: "text"

```


**Configuration.name** : The new name for the portal.



#### `add-portal`


Creates a new portal where windows can be added.

```yaml
# Top-level item is some name the user prefers.  Here, we call it "Configuration".
Configuration:
  extension: add-portal
  enabled: true
  properties:

```




#### `remove-portal`


Removes the active portal, unless it's the last portal in a split.

```yaml
# Top-level item is some name the user prefers.  Here, we call it "Configuration".
Configuration:
  extension: remove-portal
  enabled: true
  properties:

```




#### `move-window-to-portal`


Moves a window to an adjacent or named portal.

```yaml
# Top-level item is some name the user prefers.  Here, we call it "Configuration".
Configuration:
  extension: move-window-to-portal
  enabled: true
  properties:
    direction: "text"
    name: "text"

```


**Configuration.direction** : The direction to move the window - one of `n`, `s`, `e`, or `w`.

**Configuration.name** : Portal name to move the window into.  If this is not given, or the portal with the given name is not
            found, then `direction` is used.






## Dependencies

* [core.platform.api](core.platform.api.md)
  no version restriction
* [core.state.api](core.state.api.md)
  no version restriction
* [core.theme.api](core.theme.api.md)
  no version restriction
* [core.layout.binding](core.layout.binding.md)
  no version restriction






## Listens To Events

* Event Id **`petronia.participant/request-dispose`**
  Target Id **`default.layout.tile`**
* Event Id **`core.shutdown.api system-shut-down-finalize`**
  Target Id **`core.shutdown.api`**
* Event Id **`core.state.api updated`**
  Target Id **`default.layout.tile/setup-configuration`**
* Event Id **`core.state.api updated`**
  Target Id **`core.platform.api/screen-state`**
* Event Id **`core.state.api updated`**
  Target Id **`petronia.core.platform.api/windows`**



## Source

Authors: Petronia

License: MIT

*This file was auto-generated from the Petronia source on 2019-Oct-24.*
