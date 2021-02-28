# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-28T02:46:15.003332+00:00

"""
Tests for the monitor module.
Extension petronia.core.api.native.monitor, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import monitor

class MonitorTest(unittest.TestCase):
    """
    Tests for Monitor
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in MONITOR_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = monitor.Monitor.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = {
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                }
                actual = list(res.valid_error.messages())
                # The parsing returns at least one of the problems, but not necessarily all.
                self.assertTrue(len(actual) >= 1, repr(expected))
                self.assertTrue(expected.issuperset(actual), repr(expected))

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in MONITOR_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = monitor.Monitor.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


MONITOR_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='identifier', name='Monitor'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='description', name='Monitor'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='real_pixel_width', name='Monitor'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='real_pixel_height', name='Monitor'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='dpi_x', name='Monitor'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='dpi_y', name='Monitor'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='supports_rotation', name='Monitor'),
            ),

        ),
    ),

]


MONITOR_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'identifier': 788232,
            'description': 'ǓϡvӶȻДԪã ūʉ˥ӹŤɒHǞˠȜя\x90҆ɲȓƆǓ\x97Ќˍā',
            'real_pixel_width': -256779677593905639,
            'real_pixel_height': -7443531051535690419,
            'dpi_x': 1775888675641642178,
            'dpi_y': 1539370525445618495,
            'supports_rotation': False,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': -882619,

            'description': '',

            'real_pixel_width': -7908563089186657752,

            'real_pixel_height': -1062650602856080038,

            'dpi_x': 7655465123840450762,

            'dpi_y': 52146330925881900,

            'supports_rotation': True,

        },
    ),
]

class ActiveMonitorsStateTest(unittest.TestCase):
    """
    Tests for ActiveMonitorsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ACTIVE_MONITORS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = monitor.ActiveMonitorsState.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = {
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                }
                actual = list(res.valid_error.messages())
                # The parsing returns at least one of the problems, but not necessarily all.
                self.assertTrue(len(actual) >= 1, repr(expected))
                self.assertTrue(expected.issuperset(actual), repr(expected))

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in ACTIVE_MONITORS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = monitor.ActiveMonitorsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ACTIVE_MONITORS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='monitors', name='ActiveMonitorsState'),
            ),

        ),
    ),

]


ACTIVE_MONITORS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'monitors': [
                {
                    'identifier': 5646025,
                    'description': 'ЬɕȢŪȳΜϪüɣʩˀĶҜȾҁӬӰԙǬиѓǽʼѐʻŋÁаĵ{',
                    'real_pixel_width': -646749275376390456,
                    'real_pixel_height': -7896246215426812081,
                    'dpi_x': 3906189323089882622,
                    'dpi_y': 2909552357632292580,
                    'supports_rotation': False,
                },
                {
                    'identifier': 4549021,
                    'description': '=Ȗ˂ƪӳŖҪҿnǀʽϦΘȖΦʐγÚЖǲē˯ɰ´˚γ˵Êͻȭ',
                    'real_pixel_width': -3206858534243097194,
                    'real_pixel_height': -6285929687484406030,
                    'dpi_x': 3389040006769700559,
                    'dpi_y': 8193540336549761553,
                    'supports_rotation': True,
                },
                {
                    'identifier': 4765136,
                    'description': 'ϝʃ˙ȲĴņгƸɩɓDƞөœĝҨǫƾ\x86ǉμƊǸю(Ѿůĵϋɘ',
                    'real_pixel_width': -7426480271025637871,
                    'real_pixel_height': -1457495638400484791,
                    'dpi_x': 4222925303125369031,
                    'dpi_y': 5087656430762543451,
                    'supports_rotation': True,
                },
                {
                    'identifier': 6068944,
                    'description': 'ћ˼ԍʪɷϔϰ\xa0şрŖŎ×Śϳû¥jκʿɁǏʙҋυԤАɼәƣ',
                    'real_pixel_width': -8459405937767592389,
                    'real_pixel_height': -7513416233981239408,
                    'dpi_x': 3784347029475395965,
                    'dpi_y': 273627560505358163,
                    'supports_rotation': True,
                },
                {
                    'identifier': 6498098,
                    'description': 'mĶѻІΟʘҨ˶ѝŲЁ\x9bƎʍқɌ¾ϛԍǦǑЭˠˮǩùvГϨԛ',
                    'real_pixel_width': -5462942001680497563,
                    'real_pixel_height': -6724175792037884971,
                    'dpi_x': 933582266323688973,
                    'dpi_y': 3572714453891427070,
                    'supports_rotation': False,
                },
                {
                    'identifier': 5117819,
                    'description': 'іƶNЗҢЈӜʜЂԊѳǒ\x9bǑƢѱǥνœ9ǽѼΔλKWτƟÂū',
                    'real_pixel_width': -5403623009812018796,
                    'real_pixel_height': -5158436449459803380,
                    'dpi_x': 4854525599973668789,
                    'dpi_y': 2075916235136012445,
                    'supports_rotation': False,
                },
                {
                    'identifier': 5908787,
                    'description': 'ǪȔȝҀŬ˅ƘŨƹάӶΟſƒӛÝȅÉŵЎηǷ§êēӾљŰЛҟ',
                    'real_pixel_width': -6116416263830077097,
                    'real_pixel_height': -3598058354366855086,
                    'dpi_x': 7531743683656497187,
                    'dpi_y': 8288967154813526821,
                    'supports_rotation': False,
                },
                {
                    'identifier': 4555168,
                    'description': 'ȅҒƣˊӹҽʟĊυЅƴɦĜҍÿӨǔҭʌϛӓνǸӀƷϡ˹ŠѣƉ',
                    'real_pixel_width': -3329363908293615422,
                    'real_pixel_height': -7096714646042577062,
                    'dpi_x': 4782741791066556508,
                    'dpi_y': 8275504582088351539,
                    'supports_rotation': True,
                },
                {
                    'identifier': 2387923,
                    'description': 'ƱZË7ɢίΚůұ˃zľˣɗĨŽҩ^îĄɢɇɯԓͳέȓщ\xa0Ø',
                    'real_pixel_width': -1757972641373490418,
                    'real_pixel_height': -2704072382471745891,
                    'dpi_x': 2857601747641467662,
                    'dpi_y': 5121708769873038249,
                    'supports_rotation': True,
                },
                {
                    'identifier': 1639301,
                    'description': 'óĵƤԌϭϚϾʢϥnɽ·ɢ&¢£ІҭȡԜϰƦβÎЫԅʾƤʹ΄',
                    'real_pixel_width': -3824959563838460572,
                    'real_pixel_height': -3911606547130569597,
                    'dpi_x': 2911520406403434820,
                    'dpi_y': 2085065583631520579,
                    'supports_rotation': True,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
            ],

        },
    ),
]
