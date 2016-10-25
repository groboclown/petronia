# Some TODO Items

## Layout

Layout is good enough for now.

## Navigation

*Priority: **EXTREME***

Navigation isn't working right.  This needs to be fixed up.
The classes participating in it are:

* root_layout
* tile
* layout
* portal
* split_layout

## Windows Integration

*Priority: **HIGH***

It's handy to have the taskbar minimized.  However, in this state,
you'll need to have a pixel or so of buffer space at the edge of
the screen where the taskbar sits.  Add a way to either detect this
situation (hard), or just allow the user to indicate that a
monitor should have a margin.

## Portal Window Indicator

*Priority: **LOW***

In each portal, it would be nice to have a bit of chrome that
indicates the windows in that portal, and their flashing status.

I don't know how this would work with floating portals, though.
Maybe they would only show the chrome if they are the active portal?

## Configuration

Configuration requires working Python coding knowledge.
It'd be nice to make this easier.

## On-The-Fly Layout Manipulation

It's been designed, just needs the UI and navigation
watcher.  Navigation direction needs to be worked out
first.

## Custom Task Bar

*Priority: **FAR DISTANT FUTURE***

A custom task bar would be neat.  This is lots of extra coding,
potentially, though.  Especially if we want to add in our own
notification tray.
