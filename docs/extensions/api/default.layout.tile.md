# default.layout.tile (implementation)
**v1.0.0**

The Petronia tiling extension.

It allows for:
* splitting the screen up into sections;
* having different splits depending on the monitor resolution;
* virtual screens;
* dynamic splitting, based on per screen settings;
* overlapping windows.



The UI is split into "portals" and "containers".  A portal is a place where zero or more UI windows are stored.

## Details

Extension For:
* [core.layout.api](core.layout.api.md)
  no version restriction


Runs in elevated privileges

## User Configuration




```yaml
---

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
              -
                name: "text"
                size: (some number)
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
          -
            name: "text"
            size: (some number)

```


**Configuration.match-windows[].portal** : name of the portal that the window will go into by default

**Configuration.match-windows[].position** : corner to align the window (ne, se, nw, sw), or not set if it is resized

**Configuration.match-windows[].key** : window property key to match

**Configuration.match-windows[].match** : text to match against the window property key value

**Configuration.match-windows[].type** : type of matching to use: glob (default), partial, exact, or regex

**Configuration.match-windows[].matchers[].key** : window property key to match

**Configuration.match-windows[].matchers[].match** : text to match against the window property key value

**Configuration.match-windows[].matchers[].type** : type of matching to use: glob (default), partial, exact, or regex

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

**Configuration.layouts[].screens[].splits[].name** : An optional name for the portal, for use with matching or quick focus on key bindings

**Configuration.layouts[].screens[].splits[].size** : proportional size of the area

**Configuration.layouts[].resolution** : screen resolution to match against, in the form WIDTHxHEIGHT (e.g. `1024x768`)

**Configuration.layouts[].name** : screen name or index to match against

**Configuration.layouts[].direction** : Initial split direction.  Deeper splits will alternate.

**Configuration.layouts[].target** : TRUE if this is where the user-triggered splits will happen

**Configuration.layouts[].splits[].name** : An optional name for the portal, for use with matching or quick focus on key bindings

**Configuration.layouts[].splits[].size** : proportional size of the area





## Dependencies

* [core.platform.api](core.platform.api.md)
  no version restriction
* [core.state.api](core.state.api.md)
  no version restriction
* [core.theme.api](core.theme.api.md)
  no version restriction
* [core.hotkeys.api](core.hotkeys.api.md)
  no version restriction







Authors: Petronia

License: MIT

*This file was auto-generated from the Petronia source on 2019-Oct-15.*
