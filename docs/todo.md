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

It's not working well on multi-monitor setups.  Single screen seems okay.

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


## Future Notes if this ever becomes a full-on Shell program

To close Windows Explorer as the current shell:

1. Press <kbd>Ctrl</kbd><kbd>Shift</kbd> while right-clicking on the task bar.
       This will bring up a context menu that lets you stop Windows Explorer.
2. From the context menu, select **Exit Explorer**.

To restart Windows Explorer as the current shell:

1. Stop Petronia.
2. Press <kbd>Ctrl</kbd><kbd>Alt</kbd><kbd>Del</kbd>, select "Task Manager".
3. From Task Manager, select **File** -> **Run new task**
4. From this new Create New Task dialog, enter "explorer", and click **OK**. 
