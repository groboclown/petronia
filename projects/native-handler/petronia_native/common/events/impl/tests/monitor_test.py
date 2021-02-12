# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-12T16:50:56.820119+00:00

"""
Tests for the monitor module.
Extension petronia.core.api.native.monitor, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import monitor

class MonitorsTest(unittest.TestCase):
    """
    Tests for Monitors
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in MONITORS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = monitor.Monitors.parse_data(test_data)
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
        for test_name, test_data in MONITORS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = monitor.Monitors.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


MONITORS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='identifier', name='Monitors'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='description', name='Monitors'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='real_pixel_width', name='Monitors'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='real_pixel_height', name='Monitors'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='dpi_x', name='Monitors'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='dpi_y', name='Monitors'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='supports_rotation', name='Monitors'),
            ),

        ),
    ),

]


MONITORS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'identifier': 9500088,
            'description': '/çΛ\x8cʪɟĺǶ/ԍ«ʇӹϓşǫÃәͶ÷U΅ԆȪΉɎňωҫɄ',
            'real_pixel_width': -6584820642337145709,
            'real_pixel_height': -5705056206004034687,
            'dpi_x': 925531995527785563,
            'dpi_y': 9217610629856042685,
            'supports_rotation': True,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 546904,

            'description': '',

            'real_pixel_width': -843527287101333512,

            'real_pixel_height': -7630889560823689988,

            'dpi_x': 5275925131239675061,

            'dpi_y': 6874416231894763649,

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
                    'identifier': -782826,
                    'description': '˶Ν',
                    'real_pixel_width': -5174983917240452273,
                    'real_pixel_height': -5660467485554992616,
                    'dpi_x': 4447690704329167654,
                    'dpi_y': 7622713616401423657,
                    'supports_rotation': True,
                },
                {
                    'identifier': 3904846,
                    'description': 'ÌӳɹԒRԤũΰʳФʪΥpŮɲҪƂļtӢΈпΣǎʇюƝшѦʯ',
                    'real_pixel_width': -5152273860295222857,
                    'real_pixel_height': -717777945541006960,
                    'dpi_x': 6136964183531836337,
                    'dpi_y': 1525284811070993937,
                    'supports_rotation': True,
                },
                {
                    'identifier': 5177181,
                    'description': 'ӉҾ6˗8ȣϔѿ\x8dɌӚүˉϖҫӘ9:ӲĬʟШКÆ\u0379ԎǷ=ӮԬ',
                    'real_pixel_width': -2527805501626032399,
                    'real_pixel_height': -7554225026701286120,
                    'dpi_x': 1110544958934235606,
                    'dpi_y': 3425738011363792755,
                    'supports_rotation': True,
                },
                {
                    'identifier': 8520481,
                    'description': 'ϸʺcǺгʋʖѳнȮϧϓʁđƏȪӞҏǥˌæiϥИπΉ×˯ʠč',
                    'real_pixel_width': -1874173591012383690,
                    'real_pixel_height': -8983429614881512149,
                    'dpi_x': 7962774965166640854,
                    'dpi_y': 8850913382587880547,
                    'supports_rotation': False,
                },
                {
                    'identifier': 9252081,
                    'description': 'ɵwϧҫɅƋ«ŤˬʙìØԨǴŘƌҩǿġĐħѯˈԧ-\x82ҹTԓИ',
                    'real_pixel_width': -6984135902601960333,
                    'real_pixel_height': -2762169275820160207,
                    'dpi_x': 753221004975990473,
                    'dpi_y': 8275349669366211733,
                    'supports_rotation': True,
                },
                {
                    'identifier': 473346,
                    'description': 'ʏơ˛Xč\x94Ƽ2ҰÂǜҳǘЄΪƅѡľ¾ŔÉ΄ғжҦ\u0381ͻͰȯ&',
                    'real_pixel_width': -3597107650912350028,
                    'real_pixel_height': -8029606905554746055,
                    'dpi_x': 4132133375478276863,
                    'dpi_y': 802902262466039481,
                    'supports_rotation': False,
                },
                {
                    'identifier': 5622438,
                    'description': '³ŻΟɲŕԙʚӃţÙ 7[ŵțȜóĐĉΕΖǛɽǰÕ¡ǙϮ8Ǻ',
                    'real_pixel_width': -6760611742624059830,
                    'real_pixel_height': -5221342096479597415,
                    'dpi_x': 4691533071423256518,
                    'dpi_y': 3455385928361461193,
                    'supports_rotation': False,
                },
                {
                    'identifier': 8821052,
                    'description': 'ȝȀɁʁͶхȠàЩ҇ʨϷȜāȌțϗUПЁҁȔͼҚщДĢ˄ѨǇ',
                    'real_pixel_width': -3488977928233891789,
                    'real_pixel_height': -7170876156046898063,
                    'dpi_x': 3100824143145288387,
                    'dpi_y': 3399717393859392516,
                    'supports_rotation': False,
                },
                {
                    'identifier': 9755439,
                    'description': 'µʹϣѭìͶӵê\x83҇łϡ˕\x86ìĵσ\x93l;ыȖȗ\u0382>ЛɾʂΩʗ',
                    'real_pixel_width': -2666855230069743600,
                    'real_pixel_height': -723395193900354539,
                    'dpi_x': 4525263092302112636,
                    'dpi_y': 2179488638662359539,
                    'supports_rotation': False,
                },
                {
                    'identifier': -856038,
                    'description': 'ǪϛłȮd҈Ьÿɜ]ӞRЀ˦϶ҡΐƟύԚǏҬк?ѼѫgΝˤď',
                    'real_pixel_width': -4138687802016554426,
                    'real_pixel_height': -7309697410752437211,
                    'dpi_x': 5139078751069955375,
                    'dpi_y': 8211587352472907649,
                    'supports_rotation': False,
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
