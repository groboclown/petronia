"""Test the module."""

import unittest
from .. import window_metrics


class WindowMetricsTest(unittest.TestCase):
    """Test the functions and structures."""

    def test_font_metrics(self) -> None:
        """Test the FontMetrics structure"""
        ftm = window_metrics.FontMetrics(
            height=5, width=6, escapement=7, orientation=8, weight=9,
            italic=10, underline=11, strikeout=12, charset=13, out_precision=14,
            clip_precision=15, quality=16, pitch_and_family=17,
            face_name='foo',
        )
        self.assertEqual(5, ftm.height)
        self.assertEqual(6, ftm.width)
        self.assertEqual(7, ftm.escapement)
        self.assertEqual(8, ftm.orientation)
        self.assertEqual(9, ftm.weight)
        self.assertEqual(10, ftm.italic)
        self.assertEqual(11, ftm.underline)
        self.assertEqual(12, ftm.strikeout)
        self.assertEqual(13, ftm.charset)
        self.assertEqual(14, ftm.out_precision)
        self.assertEqual(15, ftm.clip_precision)
        self.assertEqual(16, ftm.quality)
        self.assertEqual(17, ftm.pitch_and_family)
        self.assertEqual('foo', ftm.face_name)

    def test_window_metrics(self) -> None:
        """Test the WindowMetrics class."""
        wdm = window_metrics.WindowMetrics(
            border_width=2,
            scroll_width=3,
            scroll_height=4,
            caption_width=5,
            caption_height=6,
            caption_font=_mk_font('face1'),
            sm_caption_width=7,
            sm_caption_height=8,
            sm_caption_font=_mk_font('face2'),
            menu_width=9,
            menu_height=10,
            menu_font=_mk_font('face3'),
            status_font=_mk_font('face4'),
            message_font=_mk_font('face5'),
            padded_border_width=11,
        )
        self.assertEqual(2, wdm.border_width)
        self.assertEqual(3, wdm.scroll_width)
        self.assertEqual(4, wdm.scroll_height)
        self.assertEqual(5, wdm.caption_width)
        self.assertEqual(6, wdm.caption_height)
        self.assertEqual('face1', wdm.caption_font.face_name)
        self.assertEqual(7, wdm.sm_caption_width)
        self.assertEqual(8, wdm.sm_caption_height)
        self.assertEqual('face2', wdm.sm_caption_font.face_name)
        self.assertEqual(9, wdm.menu_width)
        self.assertEqual(10, wdm.menu_height)
        self.assertEqual('face3', wdm.menu_font.face_name)
        self.assertEqual('face4', wdm.status_font.face_name)
        self.assertEqual('face5', wdm.message_font.face_name)
        self.assertEqual(11, wdm.padded_border_width)


def _mk_font(name: str) -> window_metrics.FontMetrics:
    return window_metrics.FontMetrics(
        height=5, width=6, escapement=7, orientation=8, weight=9,
        italic=10, underline=11, strikeout=12, charset=13, out_precision=14,
        clip_precision=15, quality=16, pitch_and_family=17,
        face_name=name,
    )
