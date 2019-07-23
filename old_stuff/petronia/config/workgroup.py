"""
Manages the user configuration.
"""

from .base_config import BaseConfig

# How the panel splits its children.
ORIENTATION_VERTICAL = "vertical"
ORIENTATION_HORIZONTAL = "horizontal"
ORIENTATION_CENTER = "none"


class DisplayWorkGroupsConfig(BaseConfig):
    """
    Contains all the work group configs for each display setting.

    Groups: list of dicts:
        * 'name': just a name.  "default" is special.
        * 'monitors': list of MonitorResConfig objects.
        * 'workgroup': WorkGroupConfig object.
    """
    def __init__(self, groups=None):
        super()
        if groups is None:
            groups = []

        self.__groups = []
        for g in groups:
            group = {
                'name': 'name' in g and g['name'] or 'n/a',
                'monitors': list(g['monitors']),
                'workgroup': g['workgroup']
            }
            # Setup the monitor indicies
            for i in range(len(group['monitors'])):
                assert isinstance(group['monitors'][i], MonitorResConfig)
                group['monitors'][i].update_monitor_index(i)
            self.__groups.append(group)

    def get_workgroup_for_display(self, monitors):
        default_workgroup = None
        best_match = None
        best_rank = 0
        for group in self.__groups:
            if group['name'] == 'default':
                default_workgroup = group['workgroup']
                continue
            current_rank = 0.0
            for m_index in range(len(monitors)):
                if m_index < len(group['monitors']):
                    assert isinstance(group['monitors'][m_index], MonitorResConfig)
                    current_rank += group['monitors'][m_index].find_match_rank(m_index, monitors[m_index])
            if current_rank > best_rank:
                best_rank = current_rank
                best_match = group['workgroup']
        if best_match is None:
            if default_workgroup is None:
                # TODO better logging
                print("<<CONFIG ERROR: no default workgroup; creating one layout per monitor>>")
                layouts = []
                for m_index in range(len(monitors)):
                    layouts.append(LayoutConfig(str(m_index), "split-layout", ORIENTATION_VERTICAL, []))
                return WorkGroupConfig({"default": layouts})
            assert isinstance(default_workgroup, WorkGroupConfig)
            return default_workgroup
        assert isinstance(best_match, WorkGroupConfig)
        return best_match


class WorkGroupConfig(BaseConfig):
    """
    Contains all the configurations for the current monitor set.
    """
    def __init__(self, groups_of_layouts_by_name=None):
        if groups_of_layouts_by_name is None:
            groups_of_layouts_by_name = {}
        assert isinstance(groups_of_layouts_by_name, dict)
        self.__workgroup_groups = groups_of_layouts_by_name

    @property
    def layout_groups_by_name(self):
        """
        dict where the key points to a list of layouts
        :return:
        """
        return self.__workgroup_groups

    @property
    def default_layout_group(self):
        if len(self.__workgroup_groups) <= 0:
            return LayoutConfig("default", "split-layout", ORIENTATION_VERTICAL, [])
        if 'default' in self.__workgroup_groups:
            return self.__workgroup_groups['default']
        # print("Getting first workgroup item from {0}".format(self.__workgroup_groups))
        return list(self.__workgroup_groups.items())[0][1]

    def get_layout_group(self, name):
        if name in self.layout_groups_by_name:
            return self.layout_groups_by_name[name]
        return self.default_layout_group


class MonitorResConfig(BaseConfig):
    """
    The configuration for a single monitor at a specific resolution.  Used by the
    DisplayWorkGroupConfig to map a monitor setup to a workgroup.
    """
    def __init__(self, res_x, res_y):
        """

        :param res_x: monitor x resolution
        :param res_y: monitor y resolution
        """
        self.monitor_index = 0
        self.res_x = res_x
        self.res_y = res_y
        self.id = str(self.monitor_index) + "x" + str(res_x) + "x" + str(res_y)
        self.show_bar = False
        self.top_panel = None

    def update_monitor_index(self, monitor_index):
        self.monitor_index = monitor_index
        self.id = str(monitor_index) + "x" + str(self.res_x) + "x" + str(self.res_y)

    def find_match_rank(self, index, monitor_description):
        """

        :param index: monitor_description's index
        :param monitor_description: the dict from the OS event
        :return: rank of how good a match this is.  0 == bad
        """
        rank = 0

        # Monitor position match: 2 points
        if index == self.monitor_index:
            rank += 2

        # Width match: 10 points, based on ratio of the
        # actual monitor vs. this monitor.
        rank += (
            10.0 * (
                1.0 - (abs(self.res_x - monitor_description['width']) / max(self.res_x, monitor_description['width']))
            )
        )

        rank += (
            10.0 * (
                1.0 - (abs(self.res_y - monitor_description['height']) / max(self.res_y, monitor_description['height']))
            )
        )

        return rank


class LayoutConfig(BaseConfig):
    """
    A single panel that can contain children and/or applications.
    The panel can either show the child panels or a single application
    at a time.

    child_splits:
        Array of descriptions for each child, each is a ChildSplitConfig.
    """
    def __init__(self, name, category, orientation, child_splits):
        assert orientation in [ORIENTATION_HORIZONTAL, ORIENTATION_VERTICAL, None], (
            "bad orientation: {0}".format(orientation))
        self.name = name
        self.category = category
        self.id = str(name)
        self.orientation = orientation
        self.child_splits = child_splits
        self.snap_vertical = None
        self.snap_horizontal = None
        self.is_main_layout_sibling = name == 'main'


class ChildSplitConfig(BaseConfig):
    """
    To make a child "floating" (some layout types are floating), set the
    child split "size" to 0.
    """
    def __init__(self, size, layout_def):
        assert isinstance(size, int)
        assert layout_def is None or isinstance(layout_def, LayoutConfig)
        self.size = size
        self.layout_def = layout_def
