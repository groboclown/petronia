
from petronia.system.bus import Bus
from petronia.system import event_ids
from petronia.system import target_ids


def log_events(bus):
    assert isinstance(bus, Bus)
    bus.add_listener(event_ids.ALL, target_ids.BROADCAST, _log_event)


def _log_event(event_id, target_id, event_obj):
    print("{0}->{1}: {2}".format(event_id, target_id, event_obj))
