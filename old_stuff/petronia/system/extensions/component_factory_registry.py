
from ...shell.control.split_layout import get_object_factories as layout_factories
from ...shell.control.portal import get_object_factories as portal_factories
from ...shell.view.render_text import get_object_factories as render_text_factories


def get_base_extension_factories():
    ret = {}
    for reg_objects in (layout_factories(), portal_factories(), render_text_factories()):
        for category, factory in reg_objects.items():
            ret[category] = factory
    return ret
