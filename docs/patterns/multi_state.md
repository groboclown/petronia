# Multiple State Service

WARNING THIS IS OUT OF DATE.

This document refers to old Petronia 2 API and related concepts.  It remains here only as a placeholder for what documentation should be. 

A common pattern in services is a *toggled state*, where, with one event, the service enters a state, and with another event, switches over to a second, and so on.

## Approach

Split each state into its own object, and have a controller object that the state objects call into for state changes.

Each state object provides a function to install the event listeners that the state concerns itself with, and a dispose function to uninstall those listeners.

Use the `petronia.aid.state_swap.StateSwapController` class to register those state setup/teardown functions.

When a state encounters a swap event, it calls the controller's `switch_state` method to perform the necessary operations.

## Disposing The Service

Full disposal of these objects must be done outside the swapping.  The service itself, not the states, must listen for dispose events, so that a full service disposal can happen.
