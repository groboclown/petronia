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
            'identifier': 4509605,
            'description': '\x94ԃҝѲƘ\u038bҲXβŖŔԒŢġɧWˣŨѷ\x8aDÂԡз,ºӕҰзǦ',
            'real_pixel_width': -7066638704910782465,
            'real_pixel_height': -5184368772404153181,
            'dpi_x': 7869047937177695093,
            'dpi_y': 6779707277064902071,
            'supports_rotation': False,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 8393374,

            'description': '',

            'real_pixel_width': -5886107904995219189,

            'real_pixel_height': -9219139188365748825,

            'dpi_x': 1360360314325524714,

            'dpi_y': 602879164847699259,

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
                    'identifier': 6961753,
                    'description': 'ëƚɞȜ΅ů˔ǆǣʔ͵ǻԩĉϴĻӡЗNҖǔʜɟͿчѶ}ī;Ӱ',
                    'real_pixel_width': -6281977432260843540,
                    'real_pixel_height': -6249012245796327312,
                    'dpi_x': 3179112391296377994,
                    'dpi_y': 4234779340905211868,
                    'supports_rotation': False,
                },
                {
                    'identifier': 8188497,
                    'description': '9х\x97қϔǡʽͳȿβ¦ѧöұӅČĘCӔ˩óҚѷюЏʃиҨȃ\x88',
                    'real_pixel_width': -1637490032057873939,
                    'real_pixel_height': -7958643121635424955,
                    'dpi_x': 4579117919474997898,
                    'dpi_y': 4033880170579443291,
                    'supports_rotation': True,
                },
                {
                    'identifier': -206415,
                    'description': 'ɢȐѨΩеέѿǆˢΆĂϓѐˮʌǾпΪȹŨɶ\x8aÍЂϥϳˍ¥р˹',
                    'real_pixel_width': -5004181598682908780,
                    'real_pixel_height': -6568483068482449392,
                    'dpi_x': 3816808976194346465,
                    'dpi_y': 8113696464748380984,
                    'supports_rotation': True,
                },
                {
                    'identifier': 8915621,
                    'description': 'Ƙ˄\x8cɃԧȗɠ˄ʎßȧƓŷĦљӿǾ\u0381ąɔ˹ԜǳӘҤźΐǡ\x90ŵ',
                    'real_pixel_width': -3769537442460132222,
                    'real_pixel_height': -1949668189677603097,
                    'dpi_x': 3182252135252171897,
                    'dpi_y': 5987129692312575757,
                    'supports_rotation': True,
                },
                {
                    'identifier': 3901730,
                    'description': 'ɋ^їĲԉĬ9ÙʶǕ@Ͳ҃ι\x91ѧ\u038dʕɷȫȎҘ˥ƏЅҧȯϴȍϒ',
                    'real_pixel_width': -8101897522375179582,
                    'real_pixel_height': -93353519737985558,
                    'dpi_x': 7571246117376654123,
                    'dpi_y': 1834432421985490360,
                    'supports_rotation': False,
                },
                {
                    'identifier': -277702,
                    'description': 'ҧ/ϹȩзɝЍıϮԒɱƌ#śɚ\u0381Ɵùƛţţ×ƊÞ\x87čËßѝĿ',
                    'real_pixel_width': -4167267801044370821,
                    'real_pixel_height': -5323632315245432034,
                    'dpi_x': 4666867050563553720,
                    'dpi_y': 6483697209653545580,
                    'supports_rotation': False,
                },
                {
                    'identifier': 4101422,
                    'description': '˼ΣàАģˤΒ©б-џ˽ҐώѴчŕƑ҄ʞɪɉ½ȁӪɆЋĆʭ\x8c',
                    'real_pixel_width': -335695575919069707,
                    'real_pixel_height': -8545094342262269540,
                    'dpi_x': 5684177189469372519,
                    'dpi_y': 4166933849377194359,
                    'supports_rotation': False,
                },
                {
                    'identifier': 2026471,
                    'description': 'Ŝ{ԣ\x9cěąͶŘƍĭϿϪÌƹȜȤɳòΒӴЇėùÖɭӍ\xa0â˛ӫ',
                    'real_pixel_width': -680898874717109423,
                    'real_pixel_height': -6746141851927897814,
                    'dpi_x': 4809828399149767597,
                    'dpi_y': 8770788743900317046,
                    'supports_rotation': False,
                },
                {
                    'identifier': 9076371,
                    'description': 'Xƭ4ϨӒʫěљҭГбоˡĮ\x9dћ\x90ЂЈɇ˳\x8bʺșҿ˥ЧϾɉʸ',
                    'real_pixel_width': -4242872548968958613,
                    'real_pixel_height': -5102829604211112336,
                    'dpi_x': 8433270726999366174,
                    'dpi_y': 1508452960215202398,
                    'supports_rotation': True,
                },
                {
                    'identifier': 9274480,
                    'description': 'ԒУǯхѥˇϾȭÈюĪˎĖĕè9^EҵȵϬДѳΈӌѦķǦǏȨ',
                    'real_pixel_width': -7154643717984091044,
                    'real_pixel_height': -5458983425201946143,
                    'dpi_x': 6071063818777931000,
                    'dpi_y': 7306716993284782214,
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
