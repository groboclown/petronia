# GENERATED CODE - DO NOT MODIFY

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
            'identifier': 1812640,
            'description': 'ΏҰϵЃãʇ',
            'real_pixel_width': -4504007942398759685,
            'real_pixel_height': -7916409894870659801,
            'dpi_x': 588947617069146448,
            'dpi_y': 5610288083915012106,
            'supports_rotation': False,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 2527991,

            'description': '',

            'real_pixel_width': -7117860542527688128,

            'real_pixel_height': -2653885708215166982,

            'dpi_x': 2203280059995270805,

            'dpi_y': 7696862256369239023,

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
                    'identifier': -58512,
                    'description': 'ЎщɲΔ҃ˢΪĞȏȑԏԏȪƟīµǌ˯',
                    'real_pixel_width': -7769930924330013444,
                    'real_pixel_height': -8227415900533039276,
                    'dpi_x': 6930458274503785390,
                    'dpi_y': 75869433497419994,
                    'supports_rotation': True,
                },
                {
                    'identifier': 9358699,
                    'description': 'йİʡÇйÇӸȌȲ¶ӼƉªĔҭĐɶѫԓҐăôȺ\x9fņхÔΙƈů',
                    'real_pixel_width': -988813342982509202,
                    'real_pixel_height': -4261448047088924867,
                    'dpi_x': 8175991641635200892,
                    'dpi_y': 7755899065848831969,
                    'supports_rotation': False,
                },
                {
                    'identifier': 721997,
                    'description': 'ԦʩʂӍˠƯpҠĝ\x9bDȩʹēӓʼ\x84ѳӴΠŰéʡĕΛϺȢѺΌh',
                    'real_pixel_width': -3786665954293019912,
                    'real_pixel_height': -2925443998263517830,
                    'dpi_x': 4813659272621986861,
                    'dpi_y': 5895697573783343493,
                    'supports_rotation': False,
                },
                {
                    'identifier': 9213009,
                    'description': '\x84ϋ.ųoωѠƃ\x82һм\x96ƝϰҐρϼʖґĢΐӋʞɫƆƴԉԩʌĊ',
                    'real_pixel_width': -4530807472490137386,
                    'real_pixel_height': -3881866884441415926,
                    'dpi_x': 4411491399541251786,
                    'dpi_y': 2677140768745992811,
                    'supports_rotation': True,
                },
                {
                    'identifier': 2833446,
                    'description': 'ǧԀʶǹ\x97Ϡёű\x9dƖŕҫĠҿƌƻуԒҼȈʭ\u0383ӬUѤʆÖϩʫͺ',
                    'real_pixel_width': -7855557644126938758,
                    'real_pixel_height': -6895301883720798654,
                    'dpi_x': 517551403502787539,
                    'dpi_y': 5737109201712683505,
                    'supports_rotation': False,
                },
                {
                    'identifier': 5003336,
                    'description': 'ЩЬ|¸ѻˠªȌ7ΧĞƷЉÓĴбƷԄҘϟºӷ*ϠěěȵÕƻƜ',
                    'real_pixel_width': -820588226248583575,
                    'real_pixel_height': -7641922149876121785,
                    'dpi_x': 8184392748141546623,
                    'dpi_y': 8432243955220062191,
                    'supports_rotation': True,
                },
                {
                    'identifier': 620591,
                    'description': '҅ÿ\x94ӁӤЫüɷȒѐÐʔɨǫǇ÷ΦІИƜ˘˒łͻНùęйɝ˱',
                    'real_pixel_width': -5318011887849645957,
                    'real_pixel_height': -3584649187957818990,
                    'dpi_x': 4669012074786702206,
                    'dpi_y': 5748553734726286154,
                    'supports_rotation': True,
                },
                {
                    'identifier': 2439623,
                    'description': '˸J˸ԌʹˤƶȼƉȯӵ¥ҢÒˏō˄ʪ˛ÿ\x9cʢϪƠŘĊҏʢϋ˞',
                    'real_pixel_width': -8175598544196479645,
                    'real_pixel_height': -1008326611151868837,
                    'dpi_x': 5608144005538951713,
                    'dpi_y': 7270329202150142176,
                    'supports_rotation': True,
                },
                {
                    'identifier': 2280622,
                    'description': 'ŠϔӤ˥АȦʳԀʎȻȲUӔÐ1ҠƀxμҪō6ҙǾǖǹǨǆʘ\x9b',
                    'real_pixel_width': -1549033618830905496,
                    'real_pixel_height': -1475187564432789036,
                    'dpi_x': 5056404721364710195,
                    'dpi_y': 8634218615998266544,
                    'supports_rotation': True,
                },
                {
                    'identifier': 7072081,
                    'description': 'E0ӆǎƟkҶӖ±јԣƎÂŋśɢƙþгƮʤɀҴԂćʿȏӨ|ǒ',
                    'real_pixel_width': -3949651218840080664,
                    'real_pixel_height': -7538865940847657851,
                    'dpi_x': 2345295337275909082,
                    'dpi_y': 5937689444695251650,
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
