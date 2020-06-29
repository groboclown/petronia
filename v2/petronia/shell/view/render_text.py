
from ...shell.native.gui_window import GuiWindow
from ...system import event_ids

RENDER_TEXT_CATEGORY = "render-text"


def get_object_factories():
    return {
        RENDER_TEXT_CATEGORY: render_text_factory,
    }


# noinspection PyUnusedLocal
def render_text_factory(cid, arguments, bus, id_manager, config):
    fill_color = arguments['color']
    outline_color = arguments['outline-color']
    outline_width = arguments['outline-width']
    line_height = arguments['lines']
    character_width = arguments['width']
    title = arguments['title']
    text = arguments['text']
    pos = arguments['pos']
    font = arguments['font']
    class_name = arguments['class-name']
    return RenderText(
        cid, bus, class_name, title, fill_color, outline_color, outline_width,
        line_height, character_width, text, font, pos)


class RenderText(GuiWindow):
    """
    Draws text on the screen.  Does not have a background or border.
    Is always on top.
    """
    def __init__(self, cid, bus, class_name, title, fill_color, outline_color, outline_width,
                 line_height, character_width, text, font, pos):
        sample_string = "\n".join(("M" * character_width,) * line_height)
        width, height = self._get_text_size(sample_string, font)
        pos_desc = {
            'relative': pos,
            'width': width,
            'height': height,
            'monitor': 0,
            'padding': 100,
        }
        GuiWindow.__init__(self, cid, bus, class_name, title, pos_desc, font, True, True)

        self.fill_color = fill_color
        self.outline_color = outline_color
        self.outline_width = outline_width
        self.line_height = line_height
        self.character_width = character_width
        self.text = text
        self.font = font

        # TODO margin?

        self._listen(event_ids.RENDER__UPDATE, cid, self._on_render_update)

    # noinspection PyUnusedLocal
    def _on_render_update(self, event_id, target_id, event_obj):
        if 'text' in event_obj:
            self.text = event_obj['text']
        if 'append-text' in event_obj:
            self.text += event_obj['append-text']
        if 'fill-color' in event_obj:
            self.fill_color = event_obj['fill-color']
        if 'outline-color' in event_obj:
            self.outline_color = event_obj['outline-color']
        if 'line-height' in event_obj:
            self.line_height = event_obj['line-height']
        if 'character-width' in event_obj:
            self.character_width = event_obj['character-width']
        if 'pos' in event_obj:
            self.pos = event_obj['pos']

        # TODO until the rendering is working, just print it.
        print("<< {0} >>".format(self.text))

        # This isn't working right.  Apparently, something is
        # preventing the paint message from doing anything.
        # Need to investigate what the window is actually doing.
        self.draw()

        # Even this doesn't work.
        # self.draw_now()

    def _on_paint(self, hwnd, hdc, width, height):
        # Get the last line_height lines.
        lines = "\n".join(self.text.splitlines()[-self.line_height:])

        # print("DEBUG drawing text [{0}]".format(lines))

        # self._draw_outline_text(
        #     hdc, lines, self.font, 0, 0,
        #     self.outline_width, self.outline_color, self.fill_color, None)

        self._draw_text(hdc, lines, self.font, 0, 0, width, height, 0xffffff, None)
