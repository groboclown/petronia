
"""
Basic UI theme support.

Nearly all things that want to interact with the UI should do so through the
theme, rather than through the platform directly.  The platform supports very
low-level UI interaction, while the theme allows for much nicer looking
components that the user can mildly control through configuration.  This
means that the component interacting with the UI doesn't need to concern
itself with the user definitions.
"""
