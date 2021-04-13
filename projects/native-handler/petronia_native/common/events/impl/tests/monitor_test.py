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
            'identifier': 2581690,
            'description': 'ӏǽȎŇӊҹ¹ιʙȞϣʅԎ\x85CǦʨӖϷ-ϭЋʈʩ˘ЗҒſӣϹ',
            'real_pixel_width': -3649939035807273136,
            'real_pixel_height': -3212026298242424761,
            'dpi_x': 662902663639341471,
            'dpi_y': 8902541549676224322,
            'supports_rotation': False,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 3469861,

            'description': '',

            'real_pixel_width': -7182041651108308004,

            'real_pixel_height': -1665073718989692710,

            'dpi_x': 5941948418461106638,

            'dpi_y': 4474523016133917570,

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
                    'identifier': -898930,
                    'description': 'ЃšɲɀĕόXƭӳōˮƵҺΖŞԥ.ϓtϐμɅā\x89ĭǘМ´UǦ',
                    'real_pixel_width': -2243559622226658297,
                    'real_pixel_height': -6245350222250200609,
                    'dpi_x': 8994728000353391229,
                    'dpi_y': 7239857707155403026,
                    'supports_rotation': False,
                },
                {
                    'identifier': 6308293,
                    'description': 'ƗșģŨє?ƄӢЗs˻ӞϷԊŅЈӢʬĚ҆Ⱥƙ˵Jӻ˥әˬƶ;',
                    'real_pixel_width': -1500971936302001928,
                    'real_pixel_height': -6213952359097001020,
                    'dpi_x': 911962260668907358,
                    'dpi_y': 2350145337396031076,
                    'supports_rotation': True,
                },
                {
                    'identifier': 3025483,
                    'description': '¦bʬǡæ¶ΔԗȮǋ\u038dәϵөıљӼ\x89ƻԚѬƜŉТԍŜăɸüϳ',
                    'real_pixel_width': -2032035315787125725,
                    'real_pixel_height': -4358275652476176413,
                    'dpi_x': 7207857221321161070,
                    'dpi_y': 5824119606814640814,
                    'supports_rotation': False,
                },
                {
                    'identifier': 6645555,
                    'description': '҅fɕȠѦ˯˄ԎӇџβҝȗĆȃŴʲҳȱ³\x9cƮƚʝŎћԓ»кě',
                    'real_pixel_width': -253311783221257890,
                    'real_pixel_height': -8545580383843939804,
                    'dpi_x': 8499933590596834551,
                    'dpi_y': 2133921972739394335,
                    'supports_rotation': True,
                },
                {
                    'identifier': 2003055,
                    'description': 'ͷķæԑӊĴƑԨƹ½эȻʏǿŊƤѳΔǠҔ`ԓƐμ¹\x90ȗǣʶɭ',
                    'real_pixel_width': -8967884010627475429,
                    'real_pixel_height': -4805046784422089069,
                    'dpi_x': 587741666912825796,
                    'dpi_y': 1273174981645562108,
                    'supports_rotation': False,
                },
                {
                    'identifier': 4461237,
                    'description': 'ϭɲϖвηǶпƱd\x837ʬVѝ˾ÑīśҺӃʋ`ĭӖɆƤ\x9bŷģđ',
                    'real_pixel_width': -4987865934280508496,
                    'real_pixel_height': -1935961008398807948,
                    'dpi_x': 340769002788948552,
                    'dpi_y': 4933490184191637408,
                    'supports_rotation': True,
                },
                {
                    'identifier': 2090833,
                    'description': 'vɩϊǹԆĉʵБɅŌ£іÚӒ͵ȱĭϰԈӕʳȯ˸$=хҺ\x9eѹƃ',
                    'real_pixel_width': -6098838118173975886,
                    'real_pixel_height': -2688451618403398096,
                    'dpi_x': 8738135892577873904,
                    'dpi_y': 772635912419398975,
                    'supports_rotation': False,
                },
                {
                    'identifier': 146407,
                    'description': 'ԫԜĐπТԕŵΙǟǯƞſċƄүіĘɪӺψɊŪΝȷȵʍӌțӜ˔',
                    'real_pixel_width': -6036137173497771283,
                    'real_pixel_height': -350176323605695231,
                    'dpi_x': 867955613855698671,
                    'dpi_y': 1258489478962993518,
                    'supports_rotation': True,
                },
                {
                    'identifier': -159120,
                    'description': 'ŗʇ˓Sǹƫu\x7fɻŬψɰϣЏ¬âˬtӅɈɸЊƷϽβЄǍʃеː',
                    'real_pixel_width': -3152986383317598517,
                    'real_pixel_height': -8657069947700631142,
                    'dpi_x': 1525075642245138941,
                    'dpi_y': 8802038110278378706,
                    'supports_rotation': True,
                },
                {
                    'identifier': 3411525,
                    'description': 'ȲʕѬęǊԮƁ3Ъϕ\x97ǖ\x84Ĩʃԝ\x8aу\xadżяȺŔ\x82ϦåÔȪȧȦ',
                    'real_pixel_width': -5873997534894553812,
                    'real_pixel_height': -3142720771614339098,
                    'dpi_x': 1800496487760339577,
                    'dpi_y': 6637341716573520613,
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
