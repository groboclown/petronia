
"""
The Petronia "foreman" process.

Responsibilities:

1. Read the boot-up configuration.  This contains the basic configuration necessary to
    get Petronia running, and to configure the operation of the foreman.
    a. Find the user and system configuration directories.
    b. Find the program launch capabilities.  This is mapping the "runtime" extension
        attribute to a method for running that extension.
    c. Find the security permissions for the launchers.
    d. Find the initialization processes to load.  These may be marked as "critical";
        critical processes are not killed on reload events.  No other processes can
        be marked as critical.
2. Start an event broker.  This will include security to verify that the sender has
    sufficient privileges to send the event, and that the target has sufficient
    privileges to receive the event.  This will not decode the event data further than
    ensuring it is valid JSON data (even this requirement may be lifted in the future).
3. Start the initialization processes.
4. On "reload" events, kills the non-critical processes, then reruns the non-critical
    initialization processes.
5. On "stop" events or OS signals, stops the non-critial running processes, then the
    critical processes, then itself.

A note on the launchers - the request to launch an extension process
originates from the launcher process itself, which runs in a trusted context.
The security definition sent to foreman is therefore trusted.
"""
