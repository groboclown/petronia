# Version 3

Petronia Version 3 is a rewrite to attempt to support multiple operating systems.  We'll start with Windows 10 and Linux X-based UI.

This will build on some of the lessons learned.


# Goals

## Focus on Usability

The first versions were "what can we do"?  Now that this is better understood, usage patterns must be the focus for this version.

The major missing functionality in the previous versions were around live-portal manipulation.  This mostly stems from a poor understanding of how to tell the end-user what an action will do.  Because of the recursive portal system, the user would need to be able to select which part of the tree to inject the split.  In most use cases, though, the portal tree won't be too deep.  In extreme cases, the end user could configure the part of the tree that has the split.

## Easy Extending

Based on my research with other shells, it's important to allow the end-users to be able to pull in additional functionality (e.g. download something off the Internet) and use it in their configuration.

This means we need to be able to split things apart into separate files, if desired.

For example, layout trees are easily shared between people, and are independent (fairly) of the rest of the configuration.  These can be split into their own file.  Likewise, key maps to commands can be their own configuration.  It may be helpful to allow directly specifying the command in the key map (one less indirection for people to keep in their head).  Utility functions for those key maps are also helpful to be independently packaged.

## Abstract Away The OS Where Possible

Wherever possible, the interactions between the OS and the user side should be abstracted as much as possible.  Note that this puts restrictions around what can be done by the end user.

## Cross-Platform Configurations

The layout functionality, for portals, chrome, keyboard commands, and "most" command scripts, should be cross-platform.


# Architecture

## Platform-Specific

All platform specific code is in the [arch](src/petronia3/arch) source directory.  Each supported platform is in the top level directory, and must conform to the spec laid out by the [generic](src/petronia3/arch/generic) tree.

The platform acts as the main program.  It knows how to start up, shut down, and mingle itself into the running OS to do what needs to be done.  The platform calls out to the rest of the Petronia system on operating system events.


