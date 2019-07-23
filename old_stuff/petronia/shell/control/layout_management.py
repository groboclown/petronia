
"""
Classes that handle the user's layout management requests.
"""

from ...system import event_ids
from ...system import target_ids
from ...system.component import Component, Identifiable
from ...system.id_manager import Parent


class LayoutManagementController(Parent, Identifiable, Component):
    """
    A control that explicitly handles the layout management mode.
    """

    def __init__(self, bus, id_manager):
        Component.__init__(self, bus)
        Identifiable.__init__(self, target_ids.LAYOUT_MANAGEMENT_CONTROLLER)
        Parent.__init__(self, id_manager)

        self.__selected_layouts = []

        self._listen(event_ids.MODE__CHANGE_TO, target_ids.BROADCAST, self._on_mode_change)

    def _on_mode_change(self, event_id, target_id, event_obj):
        pass
