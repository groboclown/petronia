
from petronia.system.bus import SingleThreadedBus
from petronia.system.id_manager import IdManager
from petronia.system.registrar import Registrar
from petronia.system import event_ids
from petronia.system import target_ids
from petronia.arch import funcs
from petronia.script.read_config import read_user_configuration
from petronia.script.script_logger import create_stdout_logger

import sys


if __name__ == '__main__':
    """
    Checks how the layout will spread across the screen.
    """
    if len(sys.argv) <= 1:
        print("Usage: arg 1: the user configuration file")
        print("arg 2 (optional): the layout for the selected work group to use")
        sys.exit(1)

    layout_name = None
    if len(sys.argv) >= 3:
        layout_name = sys.argv[2]

    config = read_user_configuration(sys.argv[1], create_stdout_logger())
    config.init_options['layout-name'] = layout_name

    bus = SingleThreadedBus()
    id_mgr = IdManager(bus)
    registrar = Registrar(bus, id_mgr, config)
    config.register_components(registrar)

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

    sys.exit(0)
