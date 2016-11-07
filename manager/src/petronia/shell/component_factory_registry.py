
from .control.split_layout import get_object_factories as layout_factories
from .control.portal import get_object_factories as portal_factories
from .view.render_text import get_object_factories as render_text_factories

from ..system.registrar import Registrar


def register_factories(registrar):
    assert isinstance(registrar, Registrar)
    # TODO this factory declaration needs to be extensible.
    for reg_objects in (layout_factories(), portal_factories(), render_text_factories()):
        for category, factory in reg_objects.items():
            registrar.register_category_factory(category, factory)
