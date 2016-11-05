

from .render_text import RENDER_TEXT_CATEGORY
from ...system import event_ids
from ...system import target_ids
from ...util.hotkey_chain import vk_to_names


SHOWN_KEY_ACTION_CID = "Show Key Action"
_SHOWN_ACTIVE = False
_TEXT = []
_DOWN = []


def toggle_show_key_action(bus, text_color, outline_color, text_pos):
    """

    :param bus:
    :param text_color:
    :param outline_color:
    :param text_pos: relative position (left, top, bottom, right, top-right, etc)
    :return:
    """
    global _SHOWN_ACTIVE
    if _SHOWN_ACTIVE:
        bus.fire(event_ids.REGISTRAR__OBJECT_REMOVED, SHOWN_KEY_ACTION_CID, {})
        return
    listeners = []

    # noinspection PyUnusedLocal
    def on_remove(event_id, target_id, event_obj):
        global _SHOWN_ACTIVE
        for callback in listeners:
            bus.remove_listener(callback)
        _SHOWN_ACTIVE = False

    listeners.append(on_remove)
    bus.add_listener(event_ids.REGISTRAR__OBJECT_REMOVED, SHOWN_KEY_ACTION_CID, on_remove)

    # noinspection PyUnusedLocal
    def on_keystroke(event_id, target_id, event_obj):
        global _DOWN
        vk = event_obj['vk-code']
        key = vk_to_names(vk)[0]
        is_down = event_obj['is-down']
        if is_down and key not in _DOWN:
            _DOWN.append(key)
        elif key in _DOWN:
            _DOWN.remove(key)
        # print("DEBUG firing key action {0}".format(" + ".join(_DOWN)))
        bus.fire(event_ids.RENDER__UPDATE, SHOWN_KEY_ACTION_CID, {
            'text': " + ".join(_DOWN)
        })
    listeners.append(on_keystroke)
    bus.add_listener(event_ids.OS__KEY_ACTION, target_ids.ANY, on_keystroke)

    bus.fire(event_ids.REGISTRAR__REGISTER_OBJECT, target_ids.REGISTRAR, {
        'cid': SHOWN_KEY_ACTION_CID,
        'category': RENDER_TEXT_CATEGORY,
        'arguments': {
            'color': int(text_color, 16),
            'outline-color': int(outline_color, 16),
            'outline-width': 4,
            'lines': 1,
            'width': 30,
            'title': SHOWN_KEY_ACTION_CID,
            'text': "",
            'pos': text_pos,
            'font': "Arial,24pt,bold",
            'class-name': "Show_Key_Action"
        },
        'registration-events': [],
    })

    _SHOWN_ACTIVE = True
