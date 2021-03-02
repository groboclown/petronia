# GENERATED CODE - DO NOT MODIFY
# Created on 2021-03-01T15:28:50.364361+00:00

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
            'identifier': 5149591,
            'description': '˚nĖ\x81҄\x92ЈɱŁɍҫΗΘȑHӘΓлԮқȭÎӡӯ\u038bǏ\x9dͼǇȹ',
            'real_pixel_width': -9131852859471339076,
            'real_pixel_height': -2931900252912019086,
            'dpi_x': 7094662486113966523,
            'dpi_y': 4764691063548969174,
            'supports_rotation': True,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 4744636,

            'description': '',

            'real_pixel_width': -1703098764714046079,

            'real_pixel_height': -4606741421940375066,

            'dpi_x': 7962996110150198417,

            'dpi_y': 8722445714662696603,

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
                    'identifier': 3079900,
                    'description': 'q]υӁõÍȾ϶ÂӮı5ÛʿѲԒŵҶҨũLϼκӰ҉{ϓιGǧ',
                    'real_pixel_width': -8758209381749573450,
                    'real_pixel_height': -588063378929992071,
                    'dpi_x': 3686583613409540874,
                    'dpi_y': 70316779411539296,
                    'supports_rotation': False,
                },
                {
                    'identifier': 1223749,
                    'description': 'ǈȥʲÛƃгϽΆèίTžkǋ:ΡĹҔ\x9dЧęӡԄѠ˦ǷƻԃԀˀ',
                    'real_pixel_width': -5395655724910456082,
                    'real_pixel_height': -8363064200086999584,
                    'dpi_x': 6352202412767057518,
                    'dpi_y': 4407747269277205673,
                    'supports_rotation': False,
                },
                {
                    'identifier': 1416351,
                    'description': 'ʭЈԂňʂԂȶҎδřӢſǉтέ-єК\x8fƸ\x89vқƧˢÕ\x88\x8fЄά',
                    'real_pixel_width': -9085619839125468845,
                    'real_pixel_height': -2240136320213330436,
                    'dpi_x': 1253113461079597826,
                    'dpi_y': 6655384446466731439,
                    'supports_rotation': False,
                },
                {
                    'identifier': 2946795,
                    'description': 'ç϶н҆Ҷҳºȓφ˸ːƔſǴhԠԭԕӷыǁϡ˦įʦȵԕϔјҖ',
                    'real_pixel_width': -8115069174618487759,
                    'real_pixel_height': -3776079505126331516,
                    'dpi_x': 8847120657882953268,
                    'dpi_y': 8905454030001325895,
                    'supports_rotation': False,
                },
                {
                    'identifier': 2310958,
                    'description': 'ҢӽΪʔʎҙːмӄKӮGƏΐΞӠˮŬςÞƎԣːӂ˧~\x97Ǎԙ[',
                    'real_pixel_width': -8812806008097715093,
                    'real_pixel_height': -585866200249649669,
                    'dpi_x': 4947020693171050126,
                    'dpi_y': 8467515843847039877,
                    'supports_rotation': False,
                },
                {
                    'identifier': 817133,
                    'description': 'щǫǀӄҩŐμćϣΨȡԊưѫɆӣҩԒ˩ӜˠԦı˂ğҁѿʇÍƤ',
                    'real_pixel_width': -4170700294487120849,
                    'real_pixel_height': -7486856133749272216,
                    'dpi_x': 5472369267561677241,
                    'dpi_y': 3094268928353039980,
                    'supports_rotation': False,
                },
                {
                    'identifier': 4389646,
                    'description': 'ūϐłƨϿǎËŏĐłʚğҤȗļŨÐϬ˓ϩǘΰùʤ{šнϺó˼',
                    'real_pixel_width': -580175435335453513,
                    'real_pixel_height': -3587386345331453840,
                    'dpi_x': 5894898497878451968,
                    'dpi_y': 7272808526780301190,
                    'supports_rotation': True,
                },
                {
                    'identifier': 6227428,
                    'description': '\u038dӆӰєԩө˪ҨǍɀөd;ѳʻɕ\x9fӄ\x7fɤ\u0382\x82ǦkđȴȤҝʅ;',
                    'real_pixel_width': -2572811904686779023,
                    'real_pixel_height': -4445145296086206183,
                    'dpi_x': 5198984670725823813,
                    'dpi_y': 2178291762560207435,
                    'supports_rotation': True,
                },
                {
                    'identifier': 1340979,
                    'description': 'ʺÒˁ0ɶҹˈԀŋ˭Δ²юОԨ˓ǶǪω҅˱ǜP˓ԔʀӷȆӡ\x92',
                    'real_pixel_width': -1218320188411241719,
                    'real_pixel_height': -8706769225743367927,
                    'dpi_x': 7270580568588231125,
                    'dpi_y': 2599542369461686073,
                    'supports_rotation': True,
                },
                {
                    'identifier': 2925943,
                    'description': 'ȸЭÜ˦ҏéŐĺкΉ\x8eύѹƾʟҿΘVǣȮђƣͽƫƚͳ.Ԏɘж',
                    'real_pixel_width': -904605354151545498,
                    'real_pixel_height': -2937319914282296968,
                    'dpi_x': 8316183935633315922,
                    'dpi_y': 5693269801120193411,
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
