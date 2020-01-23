# Layouts are a Beautiful Thing

Petronia allows for an extensible design, and this very much includes how window layouts work.  In Petronia, the basic design behind what is usually considered the layout's job is broken into many pieces, designed such that they can work together while solving very different problems.

1. The **tile** portion computes sections of the screen to store Windows.  These can be floating, they can overlap, they can be non-overlapping tiles that completely fill the screen.  The tile portion handles resizing and moving and creating and removing tiles.
1. The **window** portion maintains native OS windows assigned into tiles.  It handles moving windows between tiles, and telling the OS tiles where to go depending on changes to the tile positions or the windows in the tiles.
1. The **navigation** portion manages changing the active tile and active windows by turning relative commands like "move the active tile east" into a direct instruction to move window X into tile Y.
1. The **bindings** portion defines a series of hotkey commands that turn into commands for the other parts of the layout.
1. The **configuration** portion reads the end-user configuration, and uses that to communicate user preferences to the layouts.  It can also manage window placement when the windows are first created, and define borders or backgrounds for tiles.
1. Outside of the layout is the Petronia widgets libraries, which allow for creating UI components in a cross-platform way to be used for the borders or backgrounds of the tiles.
1. Other extensions can take advantage of the published events and call out to the layout.

This breakdown allows for swapping out small pieces of functionality with others to suit your particular layout needs, without needing to have a major software update or swap that can make getting just the right mix hard.
