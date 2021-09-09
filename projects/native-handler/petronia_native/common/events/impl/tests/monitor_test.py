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
            'identifier': 7618897,
            'description': 'Ȝ¹ШӫΝϧϔǇǨєƓŝǷʐőʐύљUɭǙȯȑͷ\x9dʕӸʱȤЯ',
            'real_pixel_width': -8698693768416960067,
            'real_pixel_height': -7702064626598884595,
            'dpi_x': 7729416007550524468,
            'dpi_y': 413195097931368228,
            'supports_rotation': False,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 5206082,

            'description': '',

            'real_pixel_width': -2186890934483868728,

            'real_pixel_height': -8496745327440431028,

            'dpi_x': 2535829551466422444,

            'dpi_y': 6668862001199507673,

            'supports_rotation': False,

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
                    'identifier': 6966723,
                    'description': 'ÍҨ4īüě±ԢƴȐĦϳëŷ%ԬƐȸ\x98Đа*эǢþǅƳӢʼĵ',
                    'real_pixel_width': -8925250972696735581,
                    'real_pixel_height': -5237005974678877822,
                    'dpi_x': 7060783081854108877,
                    'dpi_y': 2513599504133612356,
                    'supports_rotation': True,
                },
                {
                    'identifier': 478844,
                    'description': 'Ιˌ\u0378ˤѻʙϑŰή˚ʆǍʯӈšɈȋȵφķМr˼tQǜƂνӗ\x94',
                    'real_pixel_width': -9186822821771667802,
                    'real_pixel_height': -2030960392742702347,
                    'dpi_x': 2292478865707062952,
                    'dpi_y': 3270339360523668113,
                    'supports_rotation': False,
                },
                {
                    'identifier': 7656878,
                    'description': "Ú¬˪ƠˆϑѠϋ'.FѪͶȗF!ѬѽъǰʏγӻGƵſрðˢƒ",
                    'real_pixel_width': -2514764436432599081,
                    'real_pixel_height': -8166162885360879089,
                    'dpi_x': 2954491599357457513,
                    'dpi_y': 3605945077461967588,
                    'supports_rotation': True,
                },
                {
                    'identifier': 5116424,
                    'description': "ΑξӀǵñ#ȡ'Љүʄ˺ЕnӷÃ\x91˗ɣȦďʷM-ϚӇҁЅҼŃ",
                    'real_pixel_width': -2286625773793953014,
                    'real_pixel_height': -3786642763468891094,
                    'dpi_x': 4989397265855877038,
                    'dpi_y': 1555803243452198912,
                    'supports_rotation': False,
                },
                {
                    'identifier': 6357062,
                    'description': 'δùĤƢΕϷΊŜӨԙĔ\x92ɢ˻ƆľCСŮ®ǈȧÖlŪķТ\u0379ʝ!',
                    'real_pixel_width': -272394471902256010,
                    'real_pixel_height': -7778293685261459135,
                    'dpi_x': 2299784417711757779,
                    'dpi_y': 1537109666012172590,
                    'supports_rotation': True,
                },
                {
                    'identifier': 131002,
                    'description': 'ˈȄ±³҈ƂѥƲɗÃӦӶ˂ċ)Ϸēʹϟ˩%ɛȅǚԏ}μ1˹Ѷ',
                    'real_pixel_width': -3917241590528527684,
                    'real_pixel_height': -415839024651798611,
                    'dpi_x': 5329307225394061327,
                    'dpi_y': 6934263697018387494,
                    'supports_rotation': False,
                },
                {
                    'identifier': 1538622,
                    'description': 'ȗΕҁϫϡǼ¡ĶƎКˋŢЈБˣʴɡͽƸªƶƪ[ѺʓŦΙǾÇĶ',
                    'real_pixel_width': -5426604915516916338,
                    'real_pixel_height': -8007163614691203399,
                    'dpi_x': 5981694915899110994,
                    'dpi_y': 3690806660406117330,
                    'supports_rotation': False,
                },
                {
                    'identifier': 1866055,
                    'description': 'ʠºԫÝʻԬʅʋώ«~Ͻx˾ш"ʃњʃԄ\x88ɇіǣЈɊŧˍòƅ',
                    'real_pixel_width': -3969361067282196814,
                    'real_pixel_height': -9094099271210588441,
                    'dpi_x': 8675539808871673304,
                    'dpi_y': 1055172120487349876,
                    'supports_rotation': False,
                },
                {
                    'identifier': 8860778,
                    'description': "ƕƇɑ\x9a'ǊŽϟɍδGŠЫƹ҇җѣȧҙŅӋPŠοӿΗɼӑѬđ",
                    'real_pixel_width': -2872971720213314060,
                    'real_pixel_height': -3599230643374076939,
                    'dpi_x': 4691982907096296486,
                    'dpi_y': 7794413044408404723,
                    'supports_rotation': True,
                },
                {
                    'identifier': 7722005,
                    'description': '\x84\x80ёǔ҅5İCҸӓǥ!ǎ͵ȺɅв\x8cΥƨʤʓõπˌηӢťēǣ',
                    'real_pixel_width': -958847662422970342,
                    'real_pixel_height': -1855651398232506557,
                    'dpi_x': 4689634761242905297,
                    'dpi_y': 6978223652458923380,
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
