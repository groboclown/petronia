# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-08T21:23:20.917727

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
            'identifier': 454272,
            'description': 'ҳ\x83đɗǞʒν\x83ƓɥΕΦǎʉҝȔ˻ƘЗ\x92çʝԃơğȃ<ӮԄ\x80',
            'real_pixel_width': -5173838612069778447,
            'real_pixel_height': -6715272541658104559,
            'real_pixel_size_ratio_x': 3666504489843062344,
            'real_pixel_size_ratio_y': -2488171434441216983,
            'supports_rotation': False,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 66786,

            'description': '',

            'real_pixel_width': -6014318571548575394,

            'real_pixel_height': -2244992330217939314,

            'real_pixel_size_ratio_x': 8414504863015766320,

            'real_pixel_size_ratio_y': 4768320864758068254,

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
                    'identifier': 667638,
                    'description': 'ŨȦİѩ˦ϓÐźɭʓѳϝŷǡѝƕbӰ˫ǢkŧγʜήϪӳŇʭÏ',
                    'real_pixel_width': -8827146028883318901,
                    'real_pixel_height': -4285032817950345715,
                    'real_pixel_size_ratio_x': 5532073823896900931,
                    'real_pixel_size_ratio_y': -2646211847205595905,
                    'supports_rotation': True,
                },
                {
                    'identifier': 134244,
                    'description': 'ßǪΰʡɐδʬɣǕΌŵТҩʊƄѧԌRQƈ˚dĒҸGɛǬȖµ\x88',
                    'real_pixel_width': -5625465245162589569,
                    'real_pixel_height': -3891029662687090028,
                    'real_pixel_size_ratio_x': 7064860275227206325,
                    'real_pixel_size_ratio_y': -6438730267072297014,
                    'supports_rotation': True,
                },
                {
                    'identifier': 5518635,
                    'description': 'Ӌ˱ƵқʊîǾѬΩƊPϡ҉ƿŨʹӕϬ҈҉ˡǗЇҨȿ@жhђИ',
                    'real_pixel_width': -9049791966157453653,
                    'real_pixel_height': -3596891868923023444,
                    'real_pixel_size_ratio_x': 771348674706824070,
                    'real_pixel_size_ratio_y': 661570633836091288,
                    'supports_rotation': False,
                },
                {
                    'identifier': 9701529,
                    'description': '\x97ƉƐƶŢԊϸәÔƵȬͽωҬѬφҖƯΛЖˬӀȘЂŵ҉·âƌҳ',
                    'real_pixel_width': -9152376085146982630,
                    'real_pixel_height': -4101153555464528820,
                    'real_pixel_size_ratio_x': -4603645633790988939,
                    'real_pixel_size_ratio_y': 7945406269932680569,
                    'supports_rotation': False,
                },
                {
                    'identifier': 8275794,
                    'description': 'ǂϗǭƆϭΝɴГ~ΝǶԭӜK͵ε˨ȓȒɩ\x8bíȼˀĂ¤˾ƱҐÚ',
                    'real_pixel_width': -2203681685299358242,
                    'real_pixel_height': -2627884217968731951,
                    'real_pixel_size_ratio_x': 714562096052561031,
                    'real_pixel_size_ratio_y': -8288318063675713533,
                    'supports_rotation': False,
                },
                {
                    'identifier': 3903470,
                    'description': 'Ѓүɭń\x88Íў]˯ԮϿӓԨƮȅƏӛǏОʑοʜčÏɵ\u0379Ďʣӏǌ',
                    'real_pixel_width': -6528836358565165078,
                    'real_pixel_height': -6722251202482988987,
                    'real_pixel_size_ratio_x': -4692025268602313493,
                    'real_pixel_size_ratio_y': 1951135141214842729,
                    'supports_rotation': True,
                },
                {
                    'identifier': 4997074,
                    'description': 'ӦόҴɓеŬ"ġӮѲɶѳѵ҈ϤзФʵžJԉҌԥ7ǎ˦ɽԥŢї',
                    'real_pixel_width': -5621909150683122594,
                    'real_pixel_height': -4733337615379960889,
                    'real_pixel_size_ratio_x': -8500074869644256998,
                    'real_pixel_size_ratio_y': 2185754071604103609,
                    'supports_rotation': False,
                },
                {
                    'identifier': 6880565,
                    'description': 'ŕöÅGΙʩϤӏ˭ΆǫҸŒϦ¨ȔРπʥŏϜƎĆ¥ȒɸѝҼҼћ',
                    'real_pixel_width': -6590620348809172242,
                    'real_pixel_height': -1324540808656383691,
                    'real_pixel_size_ratio_x': -6805732289290372511,
                    'real_pixel_size_ratio_y': 5179545154722790338,
                    'supports_rotation': True,
                },
                {
                    'identifier': 9855947,
                    'description': 'ǕˀʃǯɖДѯɮŐȭƬфȊѺƿӐɒk-ˑĉ˶ʄɹ˱ͱѻϬԚà',
                    'real_pixel_width': -5042234537429816016,
                    'real_pixel_height': -2567006585905250002,
                    'real_pixel_size_ratio_x': -65051974203521116,
                    'real_pixel_size_ratio_y': 5251746039335357589,
                    'supports_rotation': True,
                },
                {
                    'identifier': 5894689,
                    'description': "'Ȳ2ΑƝҥѕTͼðɻZϑɲΪŪƝԒҎҪҦǔʆҥȻрʬăӝ",
                    'real_pixel_width': -1435877072054631170,
                    'real_pixel_height': -6635535425556141827,
                    'real_pixel_size_ratio_x': -140910759760983796,
                    'real_pixel_size_ratio_y': 8312779834715088218,
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
