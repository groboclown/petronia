# Coding Standards


## Python

### Source Code Format

* The `pylint` tool with the custom extension `trailing_commas` must be used.
* 100% code coverage is the desired state.
* Spaces, not tabs.


### Python Standard Lib Dos And Don'ts

* Python's basic `datetime.datetime` does not include timezone information by default.  Petronia has a helper function `petronia_common.util.tznow` to make sure you get the current date-time with the timezone. 


### Threading Model

(This isn't true anymore; current asyncio has hard limitations on Windows which causes this not to work.  Threading is, unfortuantely, the only way to go if you really, really need parallel execution.)

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

The only section that is allowed to use a threading model is the `foreman` project, and only that is due to Python asyncio support on Windows when dealing with child processes and I/O communication on those processes and OS signal handling.


## Logging

The standard Python logging module is used for logging support.  Extensions must load up their logging module with the base name being the extension name.

Each launcher program is responsible for setting up its own logging configuration.  This is done through the logging configuration.


## Internationalization

User messages should all be localizable.  Custom extensions need to register their localized message catalogs with the user message catalog extension point.
