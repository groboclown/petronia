# Petronia Projects

Because Petronia is split into executables, the major parts of the program are split into individual projects.

* [py-common-lib](py-common-lib) - Common Python libraries.
* [foreman](foreman) - The boot program, program launcher, and centralized event router.
* [native-handler](native-handler) - The native interface for handling Petronia requests and sending OS actions into the Petronia bus.
* [extension-tools](extension-tools) - Tools to help the extension author.
* [core-extensions](core-extensions) - The core Petronia extensions.

In the future, Petronia may be split out into its own major project group, in which case these may become their own top-level projects. 
