
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

    # TODO allow a second argument to select the work group
    # in the monitor selection to test.

    config = read_user_configuration(sys.argv[1])

    bus = SingleThreadedBus()
    id_mgr = IdManager(bus)
    registrar = Registrar(bus, id_mgr, config)
    for reg_objects in (layout_factories(), portal_factories()):
        for category, factory in reg_objects.items():
            registrar.register_category_factory(category, factory)

    sizes = {}

    # noinspection PyUnusedLocal
    def set_size_listener(event_id, target_id, event_obj):
        sizes[target_id] = {
            'x': event_obj['x'], 'y': event_obj['y'], 'width': event_obj['width'], 'height': event_obj['height']
        }

    monitors = funcs.monitor__find_monitors()
    index = 1
    for monitor in monitors:
        print("Monitor {index}: ({width}x{height}) @ ({x}, {y})".format(
            index=index, x=monitor['left'], y=monitor['top'],
            width=monitor['right'] - monitor['left'], height=monitor['bottom'] - monitor['top']))
        index += 1

    bus.add_listener(event_ids.LAYOUT__SET_RECTANGLE, target_ids.ANY, set_size_listener)
    root_layout = RootLayout(bus, config, id_mgr)
    bus.fire(event_ids.OS__RESOLUTION_CHANGED, target_ids.BROADCAST, {
        'monitors': monitors
    })

    for cid, size in sizes.items():
        print("{0}:".format(cid))
        print("    size: {width}x{height}, pos: ({x}, {y})".format(
            cid=cid, x=size['x'], y=size['y'], width=size['width'], height=size['height']))
        index = 1
        for monitor in monitors:
            if monitor['left'] <= size['x'] < monitor['right'] and monitor['top'] <= size['y'] < monitor['bottom']:
                print("    Monitor {index}: size: ({width}x{height}), pos: ({x}, {y})".format(
                    index=index, x=monitor['left'], y=monitor['top'],
                    width=monitor['right'] - monitor['left'], height=monitor['bottom'] - monitor['top']))
                print("        Portal's position relative to monitor: ({x1},{y1}) to ({x2},{y2})".format(
                    index=index, x1=size['x'] - monitor['left'], y1=size['y'] - monitor['top'],
                    x2=size['x'] - monitor['left'] + size['width'], y2=size['y'] - monitor['top'] + size['height']))
            index += 1

    exit()
