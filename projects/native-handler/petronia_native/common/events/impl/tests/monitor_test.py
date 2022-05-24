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
            'identifier': 9494631,
            'description': 'ȿ\x7fѸç)å˭\u0378ɖĒΜȔńԡwđȑӟǉǴyԛȝӾǑɷ\\ʆԓЎ',
            'real_pixel_width': -1791900750408908638,
            'real_pixel_height': -6641201260583801741,
            'dpi_x': 1642410805902610273,
            'dpi_y': 5598142766754709689,
            'supports_rotation': False,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 4620199,

            'description': '',

            'real_pixel_width': -897684257193840930,

            'real_pixel_height': -8717767539920428153,

            'dpi_x': 5020223761107026895,

            'dpi_y': 3123411390747082091,

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
                    'identifier': -959799,
                    'description': 'НϳÇʡčϪѽȝɥɹȘǆŻӉʲÕЗ\u03a2˹Ů\x90έҋƜ_ѯϙUӻç',
                    'real_pixel_width': -7094223170372820492,
                    'real_pixel_height': -8225813865351061779,
                    'dpi_x': 457866834961108280,
                    'dpi_y': 6025039656477265375,
                    'supports_rotation': False,
                },
                {
                    'identifier': 4063635,
                    'description': 'ұƈǦłΰȝ´ѣœʶ7ϺəҙƈŸȅӛΘЛɀǉ¸©ʼ\u038b,ҶμҀ',
                    'real_pixel_width': -2602800725779870836,
                    'real_pixel_height': -6969820484632287456,
                    'dpi_x': 8628281536241382795,
                    'dpi_y': 4513549811206001241,
                    'supports_rotation': False,
                },
                {
                    'identifier': 8181024,
                    'description': 'ήŋƄϺҽČҎ΅şїϖԣ҇ΧQ΄ԚϷvʗЏҹžѣɈϨ7ӝϪʚ',
                    'real_pixel_width': -3295862697845287922,
                    'real_pixel_height': -1795874887171350427,
                    'dpi_x': 7369348837320540544,
                    'dpi_y': 6090806695236633382,
                    'supports_rotation': True,
                },
                {
                    'identifier': 6594614,
                    'description': '˅í˥ǐļÏѴȽñΫӦӈιȧԘͳȉǯѢӺақŔ˜Ѥ\x8aƿ˅Җ\x9d',
                    'real_pixel_width': -4679057858708111185,
                    'real_pixel_height': -6335418951606279121,
                    'dpi_x': 9100734669523129041,
                    'dpi_y': 7547629428516750936,
                    'supports_rotation': False,
                },
                {
                    'identifier': 9585833,
                    'description': 'Ҙ˩\x8eκӽΌĺQɐϮĚs-DǿуӟĦūĽþʣɺȟǭҫɒϭҼɐ',
                    'real_pixel_width': -1478566234228213474,
                    'real_pixel_height': -2297314714468926032,
                    'dpi_x': 5362337819088681270,
                    'dpi_y': 2377348484651306075,
                    'supports_rotation': False,
                },
                {
                    'identifier': 1283302,
                    'description': '\x85QϳҫÎе·Ёυʲπ½āúЬɮђԖΟ\x7f¨ҿҒͼȨğʰҶԛw',
                    'real_pixel_width': -4233277670557767664,
                    'real_pixel_height': -3499846476218713514,
                    'dpi_x': 3225408310145040118,
                    'dpi_y': 8828133295863628631,
                    'supports_rotation': True,
                },
                {
                    'identifier': 6998693,
                    'description': 'Ϲ\x80œьlÄɵ\x9cɭƅȬƝϋǸΤĆvȑĒ\u0381ζř§ɍɐёĎͻʻǋ',
                    'real_pixel_width': -2725206975476961861,
                    'real_pixel_height': -8695039562384754,
                    'dpi_x': 5427018040543109412,
                    'dpi_y': 3314007219461459138,
                    'supports_rotation': True,
                },
                {
                    'identifier': -976243,
                    'description': 'ӽɴʧʙƊʩáқȻѭɮòÀĴїĀĢœĿIƽĕ˔ɠѭČŚ·PÄ',
                    'real_pixel_width': -9198989931101536931,
                    'real_pixel_height': -1268549407207433677,
                    'dpi_x': 4227814706742530263,
                    'dpi_y': 5606791281519197582,
                    'supports_rotation': False,
                },
                {
                    'identifier': 6421156,
                    'description': 'тһеǌ!уðɎǱƝgʁϲҊӎԓ£ȜҵύƈϖĊʃƶǂˍϣ˲ż',
                    'real_pixel_width': -2717218999944425634,
                    'real_pixel_height': -5460272716970725164,
                    'dpi_x': 4583905477886855294,
                    'dpi_y': 7205550377777503367,
                    'supports_rotation': True,
                },
                {
                    'identifier': 4622762,
                    'description': 'ġĳҘʥßʬɢʉȩȱҤƅ«ћγũƧęǨԓ҆ϭ\x97ˢȰųÈΥǢȉ',
                    'real_pixel_width': -3960625205472574812,
                    'real_pixel_height': -2554871541902437510,
                    'dpi_x': 2532041005494013873,
                    'dpi_y': 4354959663704521754,
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
