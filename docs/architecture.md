# Architecture

## TODOS

* change "movement" style events into the layout direction negotiation
  event chain.


## Layouts and Portals

The system supports 2 primary interactive pieces: layouts, which split
the screens into multiple tiles, and portals, which show zero or more
top-level windows.  A layout contains one or more layouts or portals.

The system supports storing a configuration for each set of screen
resolutions.  A "screen resolution" is the collection and ordering of screens
and their resolutions.  This allows a computer to switch between setups,
say remote desktop or connecting to a docking station or presenting on
another screen, and support different setups on each one.


## Loose Coupling and Messages

The system is designed around as loose a coupling between components as
possible.

Additionally, by keeping the communication done through a message-passing
intermediary, messages can be run in the correct threading model.  Some
messages, such as logging, are not priority and should be done in a
separate thread.  Actions which have high I/O latency can also be done
in a separate thread.  UI behaviors, which may have their own ordering,
can be run by themselves.  There is also a benefit where some messages
can be optimized - for example, several events to move the same window
can be compressed into a single move event.

Due to the way in which the events work, events must always send information.
They must never wait for an event to complete (note how the Registrar has
an interesting work-around for this).  As a side effect, events don't
return information to the event generator.  Don't try to be tricky by
making an event include a callback or something!


## Objects

### ActivePortalManager

Keeps track of which portals are currently highlighted during layout
management mode, and which has the active effect in window navigation
mode.

### Layout

Contains child layouts and/or portals arranged in a specific way.  The object
itself only maintains a list of child IDs.

One kind of layout is a Top Layout, which is specifically the very top layout.
It has one job, which is to react to events which initiate layout negotiations
(such as create new window).

### Portal

Maintains a list of Top-Level Window handles, and which one is currently
displayed.  Responds to requests to switch to another window within the
portal, or to set the current portal as focused.  Additionally, reacts
to the shell setting the currently focused window (WINDOW__FOCUSED event).

### Registrar

Creates new objects upon request (event) and adds them into the system.  This
has an interesting work-around for the don't-wait-for-event rule, because
some tasks require the object to be created before sending it events (otherwise
the object could miss some important events).  The event object passed to the
registrar will include the ID for the generated object (so the requestor can
know what it created), and a list of events to trigger after the object is
created.

### Bus

The heart of the system.  Events are passed through the bus, on to the
listeners.  Events can be funneled through different threads, depending on
the event ID.  Some events are marked as happening *now*, meaning that they
must be on the originating thread, while others are forced into specific
threads.

### IdManager

Remembers what IDs have been allocated, and generates new IDs.  Does not
maintain any association between IDs and other objects.

### CommandHandler

Executes the commands, translated from user keys or other actions.

### LayoutManagementController

Keeps track of the current layout selection for the layout management mode.
It generates the correct events to the layouts to tell them how to change
shape.

### Low Level Interfaces and Renderers

The low-level OS interaction is performed by the native classes.  These
handle registering for and monitoring OS events.  They also include
renderers, which respond to certain messages to draw on the screen.


## Modal User Inputs

User input is *modal*.  The user may enter different states, which allow
for different sets of input to perform different actions.

### Common Commands

Some commands are common across all the modes.

#### User Events

* **Enter X Mode** - Request changing over to another input mode.
    Command: `change mode [(mode name)]`
* **Switch Layout** - Request a change in the current layout to an
    alternate layout.  Command: `switch-layout [(layout-name)]`
* **Save Layout** - Requests that the current layout be saved.
    (Future feature) _**Command Skipped**_

#### Generated Events

* **Remove Object** - see below.  Used when switching layout, and clearing out
    the old layout.
* **Register Object** - see below.  Used when switching layout, and adding in
    the new layout.


### Window Navigation

The primary mode is navigating between windows in a portal.  In this mode,
user input directs the portal to switch between windows.

The ActivePortalManager maintains which portal has the focus, and directs
the window actions to that portal.

#### User Events

* **Change Window In Portal** - Request that the current portal
    switches to another top-level window.
    Command: `switch-top-window [left | right | next | previous]`
* **Focus Window In Portal** - Request that the shown window in the portal
    ("top window") has the user input focus (in windows parlance,
    _activated_).
* **Window Focused** - Sent by the OS to tell that a window has become
    focused.  This could be due to a user action (say, <kbd>alt</kbd>
    <kbd>tab</kbd>), or a window launches a new window.

#### Generated Events

* **Window Focus Accepted** - Sent by the portal who accepted the focus to
    tell the low-level code to send the specified window CID events to make it
    have focus.
* **Change Top Window Z-Order** - Sent by the ActivePortalManager when the user
    requested changing the window shown within the panel.
* **Set Window On Top** - Sent by the panel when the shown window changes.
    The corresponding window should be on top of the others in the panel, but
    not focused.
* **Portal Move Window Focus** - Sent by PortalFocusManager to tell the active
    portal to move the window focus elsewhere.
* **Layout Move Window Focus** - Sent by layouts and portals to navigate
    the next portal to take focus.
* **Window List Updated** - The list of windows in a portal, and which one is
    focused, changed.  Sent by a portal, and received by the portal renderer.


### Window Movement

The second mode is moving a top-level window between portals.
*This might be joined with the window navigation, but for now
is separate.*

#### User Events

* **Move Top-Level Window** - Requests that the top level window
    that's currently displayed in the focused window will be moved in
    a user-specified direction.  The PortalFocusManager listens to this event
    to pass along the event to the currently selected portal.
    Command: `move-window-to-other-portal [north | east | west | south]`

#### Generated Events

* **Move Active Top-Level Window Direction** - Tells a specific portal to move
    the currently displayed top-level window to a relative location.
    The portal sends this on to its parent.
* **Move Specific Top-Level Window Direction** - Tells a layout to decide
    how to move a given top-level window from a direct child ID in a
    direction.
* **Move Specific Top-Level Window Destination** - The direction negotiation
    end event, received by the ActivePortalManager.  It then sends a
    Move Specific Top-Level Window Here event to the final portal.
* **Move Specific Top-Level Window Here** - Tells a layout or portal
    that a top-level window is to be moved into this location.  For layouts,
    the layout will determine which child will receive the window, and send
    the message to that child.  Portals will send an acknowledgement
    message.
* **Top-Level Window Moved** - Sent by a portal when it receives a window.
    The portal that originally owned the window will need to listen to this
    message, and remove the window from its ownership.


### Layout Management

The last mode is managing how the layouts are spread out on the screen.
The active selected panels are owned by a single layout, and that
layout handles the actual actions.

#### User Events

* **Layout Management Mode** - the user requests a switch to
    the layout management mode.  This triggers the ActivePanelManager
    to start listening, and to send a Render Layout Management Panel
    Selection event.  (Indirect: actually part of the "mode change" command.
    The mode name *MUST* be "Layout Management")
* **Layout Management Selection Change** - the user changes
    the currently selected group of panels for manipulation.  The selection
    change can be adding to the selection in a direction, removing the
    selection in a direction, or setting the current selection in a direction.
    These events are sent to the layouts, and the active selected layout
    handles the request.
    Command: `change-layout-selection [north | east | west| south] [+ | -]`
* **Join Layout Selection** - the user wants the currently selected
    panels to be joined into a single panel.
    Command: `join-selected-layout`
* **Split Layout Selection** - the user wants the currently selected
    panels to be split into multiple sub-panels.
* **Enter Window Navigation Mode**
* **Enter Window Management Mode**

#### Generated Events

* **Set Base Layout Manager** - Generated by the focused panel when the mode
    changes to this mode.  It is set to the parent layout.  The parent layout
    takes charge of the layout management.
* **Remove Object** - sent by a layout or portal to remove an object.
    The request must include another object ID which will be the new owner
    of any top-level windows that are now orphans.
    This event is also listened to by the PortalFocusManager; if the object
    removed has the focus, then the PortalFocusManager will need to transfer
    that focus ownership to the new owner ID provided in the event.
* **Add Top-Level Window** - sent by a portal when it is removed, passed as 
    part of a Layout Direction Negotiation (it's the final triggered event).
    Additionally sent by the ActivePortalManager when a new window is opened
    and it must be assigned to the active portal.
* **Set Screen Rectangle** - Sent by a layout when a child is resized or
    moved.  The child could be a portal or another layout.  The receiver
    decides on the correct behavior, but must respect the request.
    The ActivePanelManager should also listen to this to see if any of
    the selected panels have changed size; if they have, then another
    Render Layout Management Panel Selection should be generated.
* **Register Object** - sent by a layout manager when a split request
    cannot be directly handled by itself, and must instead create a child
    layout to handle the request.  The register action will include a
    set of other events that will be fired after the object is created
    and fully initialized.  These events will be things like Add Top-Level
    Windows, Set Screen Rectangle, Set Focus, and so on.  Note that the
    generator of this event will provide the new object ID for the
    registered layout.



### Portal Navigation

Navigate between portals, and assign quick keys to portals for faster
navigation.  The events in this can be merged with other modes, but for
clarity, they are put here by themselves.

This takes advantage of the ActivePortalManager, and uses it to store
the active portal, and direct events.

#### User Events

* **Portal Focus Move** - Requests that the focus for the portal moves
    to another portal.  Command: `move-focus [north | south | east | west]`
* **Change Window In Portal** - Request that the current portal
    switches to another top-level window.
    Command: `switch-top-window [left | right]`
* **Current Portal Alias** - Request to mark the currently focused
    portal under a specific alias.  The PortalFocusManager records these
    aliases. Command: `create-current-portal-alias [(alias)]`
* **Portal Focus By Alias** - Request to switch the focus to a
    portal with a specific alias (marked from a previous event).  The
    PortalFocusManager listens to these events and sends focus events
    to the corresponding aliased portals.
    Command: `focus-portal-by-alias [(alias)]`

#### Genrated Events

* **Portal Focus Accepted** - When the destination of the direction negotiation
    event chain completes, this event is triggered to tell the
    ActivePortalManager which portal is active.



### Layout Direction Negotiation

This synthetic mode is a chain of events intended to have the portals
and layouts negotiate what the "direction" means in an event.  When
the destination object is discovered, it forwards on the event.
If no destination is found, a cancel event is generated.

Valid directions: "north", "south", "east", "west", "first", "last", "next",
"previous", "parent".

Valid types: "portal", "layout", "any"

* **Begin Layout Direction Negotiation** - This is directed to a specific
    portal or layout.  It includes the forward event information, the
    direction, and the kind of target the destination should be (portal,
    layout). The target figures out the next course of action.  It also
    includes screen coordinates for more complex negotiation analysis.
* **Direction Negotiation Discover** - The source selected the parent cid as
    the next area of investigation for where to find the destination. Along
    with the original event information, it includes which object was the
    child that gave the message.  This allows the parent, when processing the
    event, to know where the "origin" to determine the next event should be
    sent to.
* **Direction Negotiation Descend** - The source selected a child cid as the
    next area of investigation.  The parent has decided that this node tree is
    correct, but the final object is in a lower (or same) level.
* **Direction Negotiation Target** - Sent by a child or parent when the given
    target is where the negotiation should end.
* **Direction Negotiation Complete** - Sent when the negotiation is completed.
    Sent right before the forwarded event is generated.

The object which determines that it is the target of the request will send the
initial event object, along with its own cid as the source, and its parent cid
as the source parent.


### OS Hooks

These are events generated by the parts of the code listening to OS-level
events.  By the time the event happens, the OS-level hook has completed
processing.  That is, the hooks are intended to be as low-latency as possible,
so the execution of the event system is done in another thread.

#### OS Events

* **Key Command** - The user entered a key combination that triggered a
    hotkey to generate a command.  This command is passed in the event.
* **Top-Level Window Focused** - The OS has switched the focused window to a
    specific window.  The OS window handle should have already been converted
    to an ID.
* **Top-Level Window Destroyed** - The OS has removed the window.  Information
    about the window needs to have already been fully gathered before the
    event is generated.  When the event is running, the state of the window
    is indeterminate (it may or may not still exist).
* **Top-Level Window Replaced** - The OS has changed out one window for
    another.  This should eventually trigger a resize of the resulting window.
* **Resolution Changed** - The OS has changed the screen resolution (including
    possible monitor changes).  The layout will need to be updated to reflect
    the corresponding new resolution values.
* **Quit** - Exit the program.  Can also be generated by the user.
    Command: `quit`


#### Generated Events

(*TODO*)
