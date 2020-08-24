# Coding Standards


## Python

### Source Code Format

* The `pylint` tool with the custom extension `trailing_commas` must be used.
* 100% code coverage is the desired state.
* Spaces, not tabs.

### Threading Model

All Python sourced parts of Petronia must use the `asyncio` libraries without threading.  Threading introduces all kinds of potential bug states that are hard to track, and also unnecessary wait states for lock acquisition.  The asynchronous libraries allow for running the code in separate context states, without worrying about threading.

This introduces some changes to old styles of code, though.  For example, the standard polling thread mechanism:

```python
self.running = True
while self.running:
    self.fetch_data()
    self.process_data()
    timing.sleep(10)
```

No longer works.  Even an asyncio version (with its version of wait) isn't acceptable.  Instead, the code should listen for the heartbeat events, and act on those.  This allows the end-user to easily define the frequency of these updates in one place.


## Logging

The standard Python logging module is used for logging support.  Extensions must load up their logging module with the base name being the extension name.

Each launcher program is responsible for setting up its own logging configuration.  This is done through the logging configuration.


## Internationalization

User messages should all be localizable.
