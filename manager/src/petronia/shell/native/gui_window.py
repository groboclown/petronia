
from ...system import event_ids
from ...system import target_ids
from ...system.component import Component, Identifiable


class GuiWindow(Identifiable, Component):
    def __init__(self, cid, bus, title):
        Component.__init__(self, bus)
        Identifiable.__init__(self, cid)


def window__create_display_window(
        title,
        message_handler,
        style_flags):
    """
    Create a viewable window, to do stuff to it.

    :param message_handler: the handler procedure created by shell__create_global_message_handler
    :param title: defaults to the class name
    :param style_flags: list of strings within WS_STYLE_BIT_MAP
    :return: hwnd
    """
    global _REGISTERED_DISPLAY_WINDOW_CLASS

    # A persistent pointer to a handler.  Must be persisted so it isn't
    # removed when we exit this method.
    window_proc = WNDPROCTYPE(message_handler)
    hinst = GetModuleHandleW(None)

    if not _REGISTERED_DISPLAY_WINDOW_CLASS:
        window_class = WNDCLASSEX()
        window_class.cbSize = c_sizeof(WNDCLASSEX)
        window_class.style = CS_DBLCLKS
        window_class.lpfnWndProc = window_proc
        window_class.cbClsExtra = 0
        window_class.cbWndExtra = 0
        window_class.hInstance = hinst
        window_class.hIcon = 0
        window_class.hCursor = 0
        window_class.hBrush = 0
        window_class.lpszMenuName = 0
        window_class.lpszClassName = _DISPLAY_WINDOW_CLASS
        window_class.hIconSm = 0

        if not RegisterClassExW(byref(window_class)):
            raise WinError()

        _REGISTERED_DISPLAY_WINDOW_CLASS = True

    style = WS_OVERLAPPEDWINDOW
    ex_style = 0
    if invisible:
        style |= WS_POPUP
        style &= ~(WS_CAPTION | WS_SIZEBOX | WS_MAXIMIZEBOX)
        ex_style |= WS_EX_LAYERED

    if always_on_top:
        ex_style |= WS_EX_TOPMOST

    hwnd = CreateWindowExW(
        0, _DISPLAY_WINDOW_CLASS, title,
        style, 0, 0, 10, 10,
        None,  # HWND_DESKTOP,
        None, hinst, None
    )
    if hwnd is None or hwnd == 0:
        raise WinError()

    hfont = None
    if font is not None:
        hdc = windll.gdi32.GetDCW(hwnd)
        try:
            hfont = _get_font_for_description(hdc, font)
            windll.user32.SendMessageW(hwnd, WM_SETFONT, hfont, 0)
        finally:
            windll.gdi32.ReleaseDCW(hdc)

    pos_x, pos_y, width, height = _parse_window_pos_details(position_details, hwnd, hfont)

    if always_on_top:
        windll.user32.SetWindowPos(
            hwnd, HWND_TOPMOST, pos_x, pos_y, width, height,
            SWP_NOACTIVATE)
        ex_style |= WS_EX_TOPMOST
    else:
        window__move_resize(hwnd, pos_x, pos_y, width, height, False)

    res = windll.user32.SetWindowLong(hwnd, GWL_EXSTYLE, ex_style)
    if res == 0:
        raise WinError()

    if invisible:
        res = windll.user32.SetLayeredWindowAttributes(hwnd, wintypes.RGB(0, 0, 0), 0xff, LWA_ALPHA)
        if res == 0:
            raise WinError()

    _CALLBACK_POINTERS[hwnd] = window_proc
    return hwnd


def _parse_window_pos_details(pos, hwnd, hfont):
    pos_x = 'x' in pos and pos['x'] or 0
    pos_y = 'y' in pos and pos['y'] or 0
    width = 'width' in pos and pos['width'] or 100
    height = 'height' in pos and pos['height'] or 100

    padding = 'padding' in pos and pos['padding'] or 4

    if 'text-size' in pos and hfont is not None:
        text = pos['text-size']
        lines = text.splitlines()
        height = 0
        width = 0
        size = wintypes.SIZE()
        hdc = windll.gdi32.GetDCW(hwnd)
        try:
            for line in lines:
                res = windll.gdi32.GetTextExtentPoint32W(
                    hdc,
                    create_unicode_buffer(line), len(line),
                    byref(size)
                )
                if res == 0:
                    raise WinError()
                height += size.cy
                width = max(width, size.cx)
        finally:
            windll.gdi32.ReleaseDCW(hdc)

    if 'relative' in pos:
        relative = pos['relative'].split(' ')
        if 'monitor' in pos:
            monitor_index = pos['monitor']
        else:
            monitor_index = 0

        monitors = monitor__find_monitors()
        if monitor_index < 0 or monitor_index >= len(monitors):
            monitor_index = 0

        if 'bottom' in relative:
            pos_y = monitors[monitor_index]['bottom'] - height - padding
        elif 'top' in relative:
            pos_y = monitors[monitor_index]['top'] + padding

        if 'right' in relative:
            pos_x = monitors[monitor_index]['right'] - width - padding
        elif 'left' in relative:
            pos_x = monitors[monitor_index]['left'] + padding

    return pos_x, pos_y, width, height
