# Petronia Projects

Because Petronia is split into executables, the major parts of the program are split into individual projects.

* [py-common-lib](py-common-lib/petronia_common/__init__.py) - Common Python libraries.
* [foreman](foreman/petronia_foreman/__init__.py) - The boot program, program launcher, and centralized event router.
* [native-handler](native-handler) - The native interface for handling Petronia requests and sending OS actions into the Petronia bus.  Currently, Petronia supports these native handlers:
    * [Windows](native-handler/petronia_windows/__init__.py)
    * [X11](native-handler/petronia_x11/__init__.py)
* [extension-tools](extension-tools) - Tools to help the extension author.
* [extension-loader](extension-loader) - Primary extension loader implementation.  Handles requests to load extensions, and communicates with Foreman and the caller with the correct event protocol. 
* [extension-runner](extension-runner) - Command run by a launcher to execute a Python-based extension.
* [core-extensions](core-extensions) - The core Petronia extensions.
* [integration-tests](integration-tests) - Tests for the integration of multiple projects.

In the future, Petronia may be split out into its own major project group, in which case these may become their own top-level projects. 
