# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-24T16:41:11.975052+00:00

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
            'identifier': 6020938,
            'description': 'зΒĭʑÇǕеŊËǚʠȄ˸ȪԚ·ͳśɑϤɼӄɽǴĔŨƞǦӫС',
            'real_pixel_width': -3769435829523365812,
            'real_pixel_height': -6699403016561817076,
            'dpi_x': 237920237263383342,
            'dpi_y': 3477373194239660235,
            'supports_rotation': False,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 8979524,

            'description': '',

            'real_pixel_width': -8066745897621122644,

            'real_pixel_height': -6451482319990103846,

            'dpi_x': 5045211240840765406,

            'dpi_y': 2861896971569168647,

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
                    'identifier': 411043,
                    'description': 'Ѕӱ2ȱϚʖӪԓŦőǆƕҗaҦͻϰϙłȝĳɬЪͽǌТ£@Ϭʾ',
                    'real_pixel_width': -218794257076484655,
                    'real_pixel_height': -1117647737281355086,
                    'dpi_x': 3283362896635544547,
                    'dpi_y': 4103460996420764603,
                    'supports_rotation': True,
                },
                {
                    'identifier': 6981998,
                    'description': '\x8e\x99ЭȏĞ¦Јҋ{ʚђǑáԞŷ\x9dȖЊ±ŤȲôĿȳǎȻϖō˂ó',
                    'real_pixel_width': -2977722916191870799,
                    'real_pixel_height': -6462066757529768407,
                    'dpi_x': 5545469967436353657,
                    'dpi_y': 5028862052302346083,
                    'supports_rotation': False,
                },
                {
                    'identifier': 9825749,
                    'description': 'ԃѝǂҊĻż$ĬȁԗkȭӐӹйͻЁӺҴ\x85ȼȈŰ\x86˅ô{Ɏщȅ',
                    'real_pixel_width': -149627726185150052,
                    'real_pixel_height': -1606249603376072538,
                    'dpi_x': 1043333297983317471,
                    'dpi_y': 6758194617847847685,
                    'supports_rotation': False,
                },
                {
                    'identifier': 7778876,
                    'description': 'ɻ\x93ұơǥ*Ȓɕ˟ӁӤ˽ʭсɈɴ\x9bȗňǐƧԡ˳Ǌӄ\u0379жҬƕȆ',
                    'real_pixel_width': -6643951095695356640,
                    'real_pixel_height': -7459328650242488315,
                    'dpi_x': 6474915006576182618,
                    'dpi_y': 6362958276064607403,
                    'supports_rotation': False,
                },
                {
                    'identifier': 3066415,
                    'description': 'ɐgϮuҗšåŵɩӫǞŽΑФĔ\x8bëD0ѼзДǕ',
                    'real_pixel_width': -2651350292887303993,
                    'real_pixel_height': -1676173245829259804,
                    'dpi_x': 9205821107760075812,
                    'dpi_y': 7864046338074030319,
                    'supports_rotation': True,
                },
                {
                    'identifier': 8193481,
                    'description': 'ҽŖϹј_\x9eЗϓɱųƶίȾңƛʛ1ѰʄȰƳѠȩɪѕɞҘΗÎ\x8f',
                    'real_pixel_width': -5968535323782706329,
                    'real_pixel_height': -8096018295671037998,
                    'dpi_x': 8346340403501996721,
                    'dpi_y': 8713221909301501763,
                    'supports_rotation': False,
                },
                {
                    'identifier': 1998782,
                    'description': 'ъŖńƕʋ˪ҺԈӕʴÐĺВҙЅϠɕfȣˋż£ɦζΖƑλ\x7fĒò',
                    'real_pixel_width': -6430908493783677973,
                    'real_pixel_height': -7089348409033462229,
                    'dpi_x': 5721149245055090557,
                    'dpi_y': 2380516338449061861,
                    'supports_rotation': False,
                },
                {
                    'identifier': 9553489,
                    'description': 'ҹҷќΥɄӪΫ$ĊĂʱӸĝҎξͽҍȣ҃əƷѯГӑδȕčʋºӿ',
                    'real_pixel_width': -1541190425908651087,
                    'real_pixel_height': -6101954003884478392,
                    'dpi_x': 5232189234608002611,
                    'dpi_y': 2341312894929529556,
                    'supports_rotation': False,
                },
                {
                    'identifier': 5580717,
                    'description': 'МϼǠӑшԒ˟αǗǣΓşɎˋ˝ϊ˜џˤǭŴƗnҒҚŔȌ΄ҪŦ',
                    'real_pixel_width': -4269262966140215831,
                    'real_pixel_height': -7887637383708902565,
                    'dpi_x': 6232874365116086069,
                    'dpi_y': 2729748924447411525,
                    'supports_rotation': True,
                },
                {
                    'identifier': 3438349,
                    'description': 'Ω\x92·ŲїzƍRԁƤƹɏʙΖśνщ8ѻЩжҧӺΞȕϼӨȚƮӀ',
                    'real_pixel_width': -3606854703109524257,
                    'real_pixel_height': -2762564302396107848,
                    'dpi_x': 3045325424257235034,
                    'dpi_y': 5984060781641927536,
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
