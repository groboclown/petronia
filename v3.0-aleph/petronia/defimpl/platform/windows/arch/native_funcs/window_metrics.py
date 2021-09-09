
"""
Some basic types, to replace dictionary usage.
"""

from typing import Optional


class FontMetrics:
    __slots__ = (
        'height',
        'width',
        'escapement',
        'orientation',
        'weight',
        'italic',
        'underline',
        'strikeout',
        'charset',
        'out_precision',
        'clip_precision',
        'quality',
        'pitch_and_family',
        'face_name'
    )

    def __init__(
            self,
            height: int,
            width: int,
            escapement: int,
            orientation: int,
            weight: int,
            italic: int,
            underline: int,
            strikeout: int,
            charset: int,
            out_precision: int,
            clip_precision: int,
            quality: int,
            pitch_and_family: int,
            face_name: Optional[str]
    ):
        self.height = height
        self.width = width
        self.escapement = escapement
        self.orientation = orientation
        self.weight = weight
        self.italic = italic
        self.underline = underline
        self.strikeout = strikeout
        self.charset = charset
        self.out_precision = out_precision
        self.clip_precision = clip_precision
        self.quality = quality
        self.pitch_and_family = pitch_and_family
        self.face_name = face_name


# class LOGFONT(Structure):
#     _fields_ = (
#         ("lfHeight", LONG),
#         ("lfWidth", LONG),
#         ("lfEscapement", LONG),
#         ("lfOrientation", LONG),
#         ("lfWeight", LONG),
#         ("lfItalic", BYTE),
#         ("lfUnderline", BYTE),
#         ("lfStrikeOut", BYTE),
#         ("lfCharSet", BYTE),
#         ("lfOutPrecision", BYTE),
#         ("lfClipPrecision", BYTE),
#         ("lfQuality", BYTE),
#         ("lfPitchAndFamily", BYTE),
#
#         # Even though we use the W version of the call, we
#         # still are expected to use CHAR, not WCHAR here.
#         ("lfFaceName", CHAR * LF_FACESIZE),
#     )
#


class WindowMetrics:
    """
    Python-style access to the window metrics.
    """
    __slots__ = (
        'border_width',
        'scroll_width',
        'scroll_height',
        'caption_width',
        'caption_height',
        'caption_font',
        'sm_caption_width',
        'sm_caption_height',
        'sm_caption_font',
        'menu_width',
        'menu_height',
        'menu_font',
        'status_font',
        'message_font',
        'padded_border_width',
    )

    def __init__(
            self,
            border_width: int,
            scroll_width: int,
            scroll_height: int,
            caption_width: int,
            caption_height: int,
            caption_font: FontMetrics,
            sm_caption_width: int,
            sm_caption_height: int,
            sm_caption_font: FontMetrics,
            menu_width: int,
            menu_height: int,
            menu_font: FontMetrics,
            status_font: FontMetrics,
            message_font: FontMetrics,
            padded_border_width: int
    ):
        self.border_width = border_width
        self.scroll_width = scroll_width
        self.scroll_height = scroll_height
        self.caption_width = caption_width
        self.caption_height = caption_height
        self.caption_font = caption_font
        self.sm_caption_width = sm_caption_width
        self.sm_caption_height = sm_caption_height
        self.sm_caption_font = sm_caption_font
        self.menu_width = menu_width
        self.menu_height = menu_height
        self.menu_font = menu_font
        self.status_font = status_font
        self.message_font = message_font
        self.padded_border_width = padded_border_width



# class NONCLIENTMETRICS(Structure):
#     _fields_ = (
#         ("cbSize", UINT),
#         ("iBorderWidth", c_int),
#         ("iScrollWidth", c_int),
#         ("iScrollHeight", c_int),
#         ("iCaptionWidth", c_int),
#         ("iCaptionHeight", c_int),
#         ("lfCaptionFont", LOGFONT),
#         ("iSmCaptionWidth", c_int),
#         ("iSmCaptionHeight", c_int),
#         ("lfSmCaptionFont", LOGFONT),
#         ("iMenuWidth", c_int),
#         ("iMenuHeight", c_int),
#         ("lfMenuFont", LOGFONT),
#         ("lfStatusFont", LOGFONT),
#         ("lfMessageFont", LOGFONT),
#
#         # Windows Vista has this extra parameter
#         ("iPaddedBorderWidth", c_int)
#     )
