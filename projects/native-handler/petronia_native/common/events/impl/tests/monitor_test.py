# GENERATED CODE - DO NOT MODIFY

"""
Tests for the monitor module.
Extension petronia.core.api.native.monitor, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

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
            'identifier': 2555709,
            'description': '\x85ʸҸԒӰӨϋӫƘ2ҚŒҕͻѬƼū,ԩЖdϞŋɜҽɝ`Ϊųқ',
            'real_pixel_width': -8242780288418843479,
            'real_pixel_height': -9053211879511934323,
            'dpi_x': 6683540757714899301,
            'dpi_y': 5505689734598886054,
            'supports_rotation': True,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 9343018,

            'description': '',

            'real_pixel_width': -4937432403918615311,

            'real_pixel_height': -5695178087504488149,

            'dpi_x': 1462725564547467243,

            'dpi_y': 6947542232356599769,

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
                    'identifier': 2528809,
                    'description': 'ĒãђÅĳΤʦ΅¼Ȃ¶"ѐ8Ζϊ37ЪѥббƘӬЃȘӅŀŶЂ',
                    'real_pixel_width': -2007512501638056758,
                    'real_pixel_height': -7856516578453809156,
                    'dpi_x': 7557640705199593351,
                    'dpi_y': 5696865856973872066,
                    'supports_rotation': False,
                },
                {
                    'identifier': 3140848,
                    'description': 'ʩƲũҿүäӤӎӭҖĄӢģӉǭЯ\u0380ϊϟƚӕǝdҔǓѦԛҠӄʡ',
                    'real_pixel_width': -512423468543602642,
                    'real_pixel_height': -8635168955565354982,
                    'dpi_x': 2309353461170395223,
                    'dpi_y': 469712882582335617,
                    'supports_rotation': False,
                },
                {
                    'identifier': 2884126,
                    'description': 'ťҍˌɇĦԑúŊϡëĜԞȨȭԬӸʕ½ŠΗŮʑѸŎԮіāƴч˦',
                    'real_pixel_width': -1598335869260060290,
                    'real_pixel_height': -1079372790816069963,
                    'dpi_x': 1148236701856305504,
                    'dpi_y': 1195470952056574234,
                    'supports_rotation': True,
                },
                {
                    'identifier': 4432362,
                    'description': 'ǚ$ωϰ¢ʇj\x94ɽΏ´ӓ,Ћɪ\u0381ԡUҫ¶ьǾŰĸѥϯɶǍΩϒ',
                    'real_pixel_width': -2228331286058274827,
                    'real_pixel_height': -1069752034538015604,
                    'dpi_x': 5397572193318475130,
                    'dpi_y': 8422733095503108252,
                    'supports_rotation': False,
                },
                {
                    'identifier': 8231115,
                    'description': 'ҵԉƅɠɔʆˍȮҜѧˍԗɸєƷϷ\x90ɞͲɷБʂƗǛх\x7fϘ¯ȱȌ',
                    'real_pixel_width': -2049294714974014333,
                    'real_pixel_height': -9150049745403679887,
                    'dpi_x': 5500202871501113192,
                    'dpi_y': 7838661719410385021,
                    'supports_rotation': False,
                },
                {
                    'identifier': 327674,
                    'description': 'ԓŴώζŝΜȃȁʾÀƋ&4ϒ÷Uˢ\u0379ėźűûćҶǯʕŋԂǖͷ',
                    'real_pixel_width': -4341517370369261219,
                    'real_pixel_height': -3109121242596389064,
                    'dpi_x': 1504537864004880630,
                    'dpi_y': 8820706168763714919,
                    'supports_rotation': False,
                },
                {
                    'identifier': 3940161,
                    'description': 'AɚІКНӫ\xadƈҏėЁıѳ΅ΕӧΨѳѼХˎϡȔϓʹϱϺ\u0381вń',
                    'real_pixel_width': -6769325652962220308,
                    'real_pixel_height': -194406280496182701,
                    'dpi_x': 7995055744317554738,
                    'dpi_y': 7465406803116445229,
                    'supports_rotation': False,
                },
                {
                    'identifier': 6132448,
                    'description': 'qÓEČÞϫя¾ƞȥTԜϒ2ΪωΙϓĆʶЋЋҭ·Ě\u0381ϵϩ2ϒ',
                    'real_pixel_width': -1699268794293218257,
                    'real_pixel_height': -1762214039094900980,
                    'dpi_x': 7053128639287540453,
                    'dpi_y': 7461555038045103805,
                    'supports_rotation': False,
                },
                {
                    'identifier': -642534,
                    'description': 'ѨɧΩe\x85LǋƸâʻҕɑӡ®ˌƐ\x94ʬƓƾр҇ΙWųΓиӔά²',
                    'real_pixel_width': -3970765035089668460,
                    'real_pixel_height': -6171056148438259340,
                    'dpi_x': 1774792918581746570,
                    'dpi_y': 3866417336382674290,
                    'supports_rotation': True,
                },
                {
                    'identifier': 2650196,
                    'description': 'ƤŁwʅ,ȬӺƉԛԟԭō\x8aʂQjĶˇ\x99ԐđzéԑÒŠƸŌμG',
                    'real_pixel_width': -4475384952148781554,
                    'real_pixel_height': -8195713785481376708,
                    'dpi_x': 6894542732954406812,
                    'dpi_y': 2428523880296266222,
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
