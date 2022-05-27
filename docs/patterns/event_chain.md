# Event Chaining

Some extensions will need to correctly respond to a series of events, here called "event chaining".  This is similar to the [multi-state](multi_state.md) pattern, but usually applies to life cycle changes.

Let's say we have a process that wants to listen to new native
windows, and when it is created, create chrome around it, then add a title bar
on it.

```python
my_id = bus.create_component_id('my-component')
chain = EventChainManager(bus, my_id)
chain.
# Create a new chain.
create().
# It will listen in the background, waiting for any native window
# creation events, to begin this chain of events.
# wait for the native window creation event.
when(
    EventHas(on_native_window_created).
        # keep track of the window ID in this chain.
        track(
        'wid',
        lambda event_obj: event_obj.window_id
    )
).
# After this trigger to start the chain...
# create a new number for event tracking, and add it to the marks as 'rid1'
create_unique_int_as('rid1').
# then perform the response
then_handle().
# send a create chrome component request, and send the response to my_id.
run(lambda bus, marks: send_request_new_chrome(
    bus, marks['wid'], my_id, marks['rid1'], Chrome()
)).
# wait for the generic component created event
then().
when(
    EventHas(on_component_created).
        to(my_id).
        # this specific event must have the matching request_id to continue the chain
        matching(lambda obj: obj.request_id == marks['rid1']).
        # matched event will keep track of the created_id in the 'cid' mark.
        track('cid', lambda obj: obj.created_id)
).
# now start the processing
then_handle().
# call the function to send the titlebar addition events.
run(create_titlebar).
# call the function to send the footer information addition events.
run(create_footer)
# Setup the events
chain.setup_ewmh()
```