# core.theme.api (API)
**v1.0.0**

Basic UI theme support.


Nearly all things that want to interact with the UI should do so through the
theme, rather than through the platform directly.  The platform supports very
low-level UI interaction, while the theme allows for much nicer looking
components that the user can mildly control through configuration.  This
means that the component interacting with the UI doesn't need to concern
itself with the user definitions.


Note that a theme is not a layout, but the two work together to create a
user experience.  The theme allows for choosing how the border and title bar
appear on drawn windows, while the layout figures out how to arrange it on
the screen.

## Details








## Dependencies

* [core.platform.api](core.platform.api.md)
  no version restriction



### Default Implementations:
* [default.theme.wrench](default.theme.wrench.md)
  no version restriction


## Source

Authors: Petronia

License: MIT

*This file was auto-generated from the Petronia source on 2019-Dec-20.*
