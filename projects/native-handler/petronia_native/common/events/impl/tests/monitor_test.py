# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-09T22:29:05.173184+00:00

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
                dict(field_name='real_pixel_size_ratio_x', name='Monitors'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='real_pixel_size_ratio_y', name='Monitors'),
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
            'identifier': 5713693,
            'description': '˔ȶ҅RɯɅˢȓҶÒrҳѻĈď\x96ȎаƂƠԋmnɎŴŷǊğѲŦ',
            'real_pixel_width': -1715133876962353630,
            'real_pixel_height': -2432216593971556617,
            'real_pixel_size_ratio_x': -3718873564209659983,
            'real_pixel_size_ratio_y': 1988352925260875254,
            'supports_rotation': False,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 3908152,

            'description': '',

            'real_pixel_width': -683266644150852158,

            'real_pixel_height': -4624194123081318025,

            'real_pixel_size_ratio_x': 8756073727448751928,

            'real_pixel_size_ratio_y': 8229499795789889118,

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
                    'identifier': 4076768,
                    'description': '6ĬĞ҄Źûƅȶŭ˕êʾ[ΈшФˁϭəʭvȨӺ¼ɰѵ-mǋñ',
                    'real_pixel_width': -7819361189334770642,
                    'real_pixel_height': -3125856847104394262,
                    'real_pixel_size_ratio_x': 1351907248482233933,
                    'real_pixel_size_ratio_y': -3513489059505309977,
                    'supports_rotation': True,
                },
                {
                    'identifier': 9698208,
                    'description': 'ӹʚћȷɓ\x90ʹɝЮĎ˄+ӫҼȄѱƧĭĔҖɆϲȫ˥˺˧\x80ͷѠȟ',
                    'real_pixel_width': -5364154892414821209,
                    'real_pixel_height': -4029486763125658064,
                    'real_pixel_size_ratio_x': 8972541733931520045,
                    'real_pixel_size_ratio_y': 5372679582873556416,
                    'supports_rotation': False,
                },
                {
                    'identifier': 5165896,
                    'description': 'ϚƿŌϐi˚ǷĻыбͳжȰ˰Ȉfԓɤţ\x8aŀʩȒ ¹½ѽȬưç',
                    'real_pixel_width': -5278801859826959663,
                    'real_pixel_height': -2022172933955094687,
                    'real_pixel_size_ratio_x': -4935768002292009237,
                    'real_pixel_size_ratio_y': 7422971742889788729,
                    'supports_rotation': True,
                },
                {
                    'identifier': -199757,
                    'description': '˜ϋԖʶҌӻ\x85ƔѪˍҖàšœųɎ)þӴĨ҄π]ӣŠūԑϾĔӇ',
                    'real_pixel_width': -5331184787080699705,
                    'real_pixel_height': -4657570806105799416,
                    'real_pixel_size_ratio_x': 2462642867803276213,
                    'real_pixel_size_ratio_y': 8855815352100163064,
                    'supports_rotation': False,
                },
                {
                    'identifier': 3396087,
                    'description': "҄ɻҲ[ƀ\x88\x84(ιǐzǬØ$ʸϦȄkԬ'ˤwʢʝàɅɢˉŲϭ",
                    'real_pixel_width': -134418100884540109,
                    'real_pixel_height': -7186833392968760499,
                    'real_pixel_size_ratio_x': 4657079163419785838,
                    'real_pixel_size_ratio_y': -3067480077751670124,
                    'supports_rotation': False,
                },
                {
                    'identifier': 6596241,
                    'description': 'ˋɒϱą҃Ƽ\u0383ЩѤŁАǿRáҥκ\xadη\x88ѪӘpȬĂΣǋӽŰУʓ',
                    'real_pixel_width': -2053756628957660731,
                    'real_pixel_height': -1838001140668586747,
                    'real_pixel_size_ratio_x': -2167131128978735360,
                    'real_pixel_size_ratio_y': -5788150506236335200,
                    'supports_rotation': False,
                },
                {
                    'identifier': 7893380,
                    'description': 'ӧҼШϲ-ɲѺȃˑ]˥БɷӗɓѲũƲϭϿҠɎΤĠΰʵˀӀΒϹ',
                    'real_pixel_width': -2737081455879813064,
                    'real_pixel_height': -8360208537595407241,
                    'real_pixel_size_ratio_x': 7493322251733092497,
                    'real_pixel_size_ratio_y': -2035234008465022410,
                    'supports_rotation': False,
                },
                {
                    'identifier': 3295628,
                    'description': 'Ǣʦ_БǵİļȲØˉʙҖӷҘȱļ',
                    'real_pixel_width': -4655905764525439910,
                    'real_pixel_height': -2962648642391141103,
                    'real_pixel_size_ratio_x': -3945584153590129876,
                    'real_pixel_size_ratio_y': -3080958279511472052,
                    'supports_rotation': True,
                },
                {
                    'identifier': 1928063,
                    'description': 'Ǯ҉θaщ˹ɹɑ£ЖɈÔǢJЍҕķхƳҟʰфÂ¹ĈεӣʡΒą',
                    'real_pixel_width': -6826755720756903223,
                    'real_pixel_height': -3090928954016869806,
                    'real_pixel_size_ratio_x': -2062989325494167170,
                    'real_pixel_size_ratio_y': -4542641003834893351,
                    'supports_rotation': True,
                },
                {
                    'identifier': 2864552,
                    'description': 'ԜȩȡϠύ½θːŊԘчσǙΆѺ',
                    'real_pixel_width': -2309244653618961409,
                    'real_pixel_height': -794653637725173466,
                    'real_pixel_size_ratio_x': 5312096957528579071,
                    'real_pixel_size_ratio_y': -1644126491453246205,
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
