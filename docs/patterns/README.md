# Patterns for Extension Authors

Here are some programming "patterns" that have emerged while creating the Petronia extension system.  These help make sure that your extension follows the standard practices, and works well in the Petronia eco-system.

## Lifecycle Patterns

These help parts of your extension to live well inside Petronia.

* [Extension Life-Cycle](dispose.md) - how an extension should handle removing itself from the system.
* [Stateful Boot](stateful_boot.md) - how to start an extension that has dependencies that must be loaded before it can be fully loaded.


## Working With Events

A large portion of Petronia involves dealing with events from many different sources.

* [Standard Events](standard_events.md) - Standard Petronia events and when to use them.
* [Multi-State](multi_state.md) - How to use events to switch between execution states.
* [Event Chain](event_chain.md) - How to chain event signals and waits together.
