
from .system.bus import SingleThreadedBus
from .system.id_manager import IdManager
from .system.registrar import Registrar
from .system import event_ids
from .system import target_ids
from .arch import funcs
from .shell.control.root_layout import RootLayout
from .shell.control.split_layout import get_object_factories as layout_factories
from .shell.control.portal import get_object_factories as portal_factories
from .script.read_config import read_user_configuration

import sys


if __name__ == '__main__':
    """
    Checks how the layout will spread across the screen.
    """
    if len(sys.argv) <= 1:
        print("Usage: arg 1: the user configuration file")
        exit(1)

    config = read_user_configuration(sys.argv[1])

    bus = SingleThreadedBus()
    id_mgr = IdManager(bus)
    registrar = Registrar(bus, id_mgr, config)
    for reg_objects in (layout_factories(), portal_factories()):
        for category, factory in reg_objects.items():
            registrar.register_category_factory(category, factory)

    sizes = {}

    def set_size_listener(event_id, target_id, event_obj):
        sizes[target_id] = {
            'x': event_obj['x'], 'y': event_obj['y'], 'width': event_obj['width'], 'height': event_obj['height']
        }

    bus.add_listener(event_ids.LAYOUT__SET_RECTANGLE, target_ids.ANY, set_size_listener)
    root_layout = RootLayout(bus, config, id_mgr)
    bus.fire(event_ids.OS__RESOLUTION_CHANGED, target_ids.BROADCAST, {
        'monitors': funcs.monitor__find_monitors()
    })

    for cid, size in sizes.items():
        print("{cid}: {width}x{height} @ ({x}, {y})".format(
            cid=cid, x=size['x'], y=size['y'], width=size['width'], height=size['height']))

    exit()
