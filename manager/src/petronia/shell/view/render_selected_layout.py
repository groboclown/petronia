
from ...system import event_ids
from ...system import target_ids
from ...system.component import Component
from ...config import Config

# oozing of Windows functions
from ...arch import funcs


class RenderSelectedPanels(Component):
    """
    The displayed monocle view with name tabs for each internal Top Window.  The top window itself is
    updated via the top_window.TopWindow class.
    """
    def __init__(self, bus, config):
        Component.__init__(self, bus)
        assert isinstance(config, Config)

        self.__config = config

