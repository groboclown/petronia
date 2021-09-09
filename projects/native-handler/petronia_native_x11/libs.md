# Notes On X11 Libraries

## Destkop Standards

* [freedesktop.org](https://www.freedesktop.org/wiki/Specifications/)
    * Autostart
    * Desktop directories
    * Desktop entries
    * Desktop menus
    * File manager / DBus
    * File URLs
    * Media Player
    * Icon Themes
    * MIME database
    * Startup notifications
    * Trash
    * [Extended window manager hints](https://specifications.freedesktop.org/wm-spec/wm-spec-1.4.html)
    * [PyXDG](https://www.freedesktop.org/wiki/Software/pyxdg/)
        * Python library to access the standards.
        * Under GNU LGPL.
* [D-Bus](https://www.freedesktop.org/wiki/Software/dbus/)
    * [PyDBus](https://github.com/LEW21/pydbus)
        * Under LGPL 2.1
    

## Multi-monitor usage

* randr
    * [xrandr](https://www.x.org/wiki/Projects/XRandR/)
    * [arandr](https://christian.amsuess.com/tools/arandr/)
        A native Python 3 tool, so could be "easily" integrated.
* [xinerama](https://www.x.org/releases/X11R7.7/doc/man/man3/Xinerama.3.xhtml)
    * Simple library.  randr should be used to interact with it.

## Graphics Rendering

* [Cairo](https://www.cairographics.org/)
    * [PyCairo](https://www.cairographics.org/pycairo/)
    * [PyGObject](https://wiki.gnome.org/action/show/Projects/PyGObject) includes Cairo bindings
* [HarfBuzz](https://www.freedesktop.org/wiki/Software/HarfBuzz/)
    * Text shaping library.  Not really useful, especially in light of BiDi text.  Might be necessary in some contexts, though.
* [Pango](https://pango.gnome.org/)
    * Text layout and display.

## Window Interfacing

* [xcb](https://xcb.freedesktop.org/)

## Testing

* [Linux Desktop Testing Project](https://github.com/ldtp/ldtp2)
