
# Usage: python3 -m unittest petronia.tests.layout_navigation

import unittest

from ..system.bus import SingleThreadedBus
from ..system.logger import Logger
from ..system.id_manager import IdManager
from ..system.registrar import StatefulRegistrar
from ..system import event_ids, target_ids
from .. import config
from ..shell.control.root_layout import RootLayout
from ..shell import navigation
from ..shell.control.split_layout import get_object_factories as layout_factories
from ..shell.control.portal import get_object_factories as portal_factories

# from .bus_logger import log_events


class NavigationTests(unittest.TestCase):
    def test_root_init_state(self):
        root = RootLayout(self.bus, self.config, self.id_manager)
        self.bus.fire(event_ids.WINDOW__CREATED, root.cid, {
            'window-cid': 'window-0',
            'window-info': {
                'cid': 'window-0',
            }
        })
        self.assertEqual(self.registrar.created_objects_by_cid, {})

        self.nav_events.clear()
        self.bus.fire(event_ids.DIRECTION_NEGOTIATION__BEGIN, root.cid,
                      navigation.create_direction_negotiation_start_event_obj(
                          root.cid, navigation.DIR_NORTH, navigation.LAYOUT_TYPE, '0', '0', {}
                      ))
        self.assertEqual(len(self.nav_events), 3)

        # Root never sends complete negotiations.
        self.assertEqual(self.nav_events[-1][0], event_ids.DIRECTION_NEGOTIATION__DESCEND)

    def test_hv_split(self):
        # Horizontal split w/ 2 kids, one is a portal, the other is a vertical split w/ 2 portal kids.
        self.root_layout.category = 'split-layout'
        self.root_layout.orientation = config.ORIENTATION_HORIZONTAL
        self.root_layout.child_splits = [
            config.ChildSplitConfig(1, config.LayoutConfig('left', 'portal', None, None)),
            config.ChildSplitConfig(1, config.LayoutConfig('right', 'split-layout', config.ORIENTATION_VERTICAL, [
                config.ChildSplitConfig(1, config.LayoutConfig('right-top', 'portal', None, None)),
                config.ChildSplitConfig(1, config.LayoutConfig('right-bottom', 'portal', None, None)),
            ]))
        ]
        root = RootLayout(self.bus, self.config, self.id_manager)
        self.bus.fire(event_ids.OS__RESOLUTION_CHANGED, root.cid, {'monitors': self.monitors})
        self.bus.fire(event_ids.WINDOW__CREATED, root.cid, {
            'window-cid': 'window-0',
            'window-info': {
                'cid': 'window-0',
            }
        })
        self.assertEqual(set(self.registrar.created_objects_by_cid.keys()), {
            'portal_0', 'portal_1', 'portal_2',
            'split-layout_0', 'split-layout_1'
        })
        # Ensure we know the position of the portals
        self.assertEqual(self.registrar.created_objects_by_cid['portal_0'].size, {
            'x': 0, 'y': 0, 'width': 500, 'height': 1000,
        })
        self.assertEqual(self.registrar.created_objects_by_cid['portal_1'].size, {
            'x': 500, 'y': 0, 'width': 500, 'height': 500,
        })
        self.assertEqual(self.registrar.created_objects_by_cid['portal_2'].size, {
            'x': 500, 'y': 500, 'width': 500, 'height': 500,
        })

        self.nav_events.clear()
        self.bus.fire(event_ids.DIRECTION_NEGOTIATION__BEGIN, root.cid,
                      navigation.create_direction_negotiation_start_event_obj(
                          root.cid, navigation.DIR_NORTH, navigation.LAYOUT_TYPE, '0', '0', {}
                      ))
        # print("Created CIDs:")
        # for cid, obj in self.registrar.created_objects_by_cid.items():
        #     print("  {0}: {1}".format(cid, obj.size))
        print("Events: {0}".format(self.nav_events))
        self.assertEqual(len(self.nav_events), 3)

    def setUp(self):
        self.bus = SingleThreadedBus()
        self.id_manager = IdManager(self.bus)
        self.monitors = [{'left': 0, 'right': 1000, 'top': 0, 'bottom': 1000, 'width': 1000, 'height': 1000}]
        self.root_layout = config.LayoutConfig('default', None, None, None)
        self.config = config.Config(
            config.DisplayWorkGroupsConfig([{
                'monitors': [config.MonitorResConfig(0, 1000, 1000, False)],
                'workgroup': config.WorkGroupConfig({'default': [self.root_layout]})
            }]),
            config.ApplicationListConfig(),
            config.HotKeyConfig(),
            config.CommandConfig(),
            config.ChromeConfig())

        self.registrar = StatefulRegistrar(self.bus, self.id_manager, self.config)
        for reg_objects in (layout_factories(), portal_factories()):
            for category, factory in reg_objects.items():
                self.registrar.register_category_factory(category, factory)

        Logger(self.bus)
        # log_events(self.bus)
        self.nav_events = []
        self.__persisted_listeners = []
        listen_navigation_events(self.bus, self.nav_events, self.__persisted_listeners)

    @property
    def navs(self):
        ret = list(self.__nav_events)
        sorted(ret, key=lambda e: e[2]['when'])
        return ret

    def __init__(self, *args):
        super().__init__(*args)
        self.bus = None
        self.id_manager = None
        self.config = None
        self.registrar = None
        self.monitors = None
        self.root_layout = None
        self.nav_events = None
        self.__persisted_listeners = None


def listen_navigation_events(bus, event_list, listeners):
    # "listeners" required so that the methods stick around and actually listen
    # after the execution exits this method.

    # Stoopid limit of listener methods
    def navigation_start(event_id, target_id, event_obj):
        event_list.append([event_id, target_id, dict(event_obj)])

    def navigation_discover(event_id, target_id, event_obj):
        event_list.append([event_id, target_id, dict(event_obj)])

    def navigation_descend(event_id, target_id, event_obj):
        event_list.append([event_id, target_id, dict(event_obj)])

    def navigation_target(event_id, target_id, event_obj):
        event_list.append([event_id, target_id, dict(event_obj)])

    def navigation_complete(event_id, target_id, event_obj):
        event_list.append([event_id, target_id, dict(event_obj)])

    bus.add_listener(event_ids.DIRECTION_NEGOTIATION__BEGIN, target_ids.ANY, navigation_start)
    bus.add_listener(event_ids.DIRECTION_NEGOTIATION__DISCOVER, target_ids.ANY, navigation_discover)
    bus.add_listener(event_ids.DIRECTION_NEGOTIATION__DESCEND, target_ids.ANY, navigation_descend)
    bus.add_listener(event_ids.DIRECTION_NEGOTIATION__TARGET, target_ids.ANY, navigation_target)
    bus.add_listener(event_ids.DIRECTION_NEGOTIATION__COMPLETE, target_ids.ANY, navigation_complete)
    listeners.extend([navigation_start, navigation_discover, navigation_descend, navigation_target,
                                  navigation_complete])


if __name__ == '__main__':
    unittest.main()
