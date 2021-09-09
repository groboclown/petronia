
"""
GUI components managed by Petronia.

The goal of these components is to provide primitive elements to allow the
Petronia system to display toolbars, window dressing, notifications, and
trivial dialogs without bloating into its own UI toolkit.

Widgets are created using the standard Petronia create component
lifecycle events.

Usually, the end-user doesn't directly ask for the creation of the
low-level widgets.  This is usually some extension that creates
the higher level widgets (such as the layout).  The higher level
creation usually has a flow like this:

    1. If the widget lives in its own top-level window, rather than,
        say, in the chrome of a window, then that top level window
        must be created.
    2. Send a request to create the container.  This needs the
        owning window CID (ComponentID).  This generates an event
        indicating the component was created (or that it failed),
        which includes the container's CID.
    3. Add one or more widgets inside the container.  Each widget
        created generates the widget's CID, which can be used to
        add user input response actions.
"""
