"""Standard event listening handlers.

The native handler is expected to be multi-threaded, because the main loop should have its own
specific handling routine outside the event listeners.  Handlers are called in-thread, so the
implementation must manage the multi-threading explicitly.
"""
