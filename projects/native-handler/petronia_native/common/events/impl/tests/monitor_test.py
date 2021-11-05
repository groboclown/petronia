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
            'identifier': 160560,
            'description': 'ſƩǲϴŖƃ¦ϊ\x97ĩҥ¼ʰǜΏˎӖİƋӹΥӋê҅ɶêłӸǚę',
            'real_pixel_width': -728312609604528261,
            'real_pixel_height': -1817870167162879968,
            'dpi_x': 2193676788515348777,
            'dpi_y': 7256537556217097677,
            'supports_rotation': False,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 3825112,

            'description': '',

            'real_pixel_width': -2590175268454430356,

            'real_pixel_height': -1408823530052394766,

            'dpi_x': 4615872869718012803,

            'dpi_y': 2959753172018689760,

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
                    'identifier': 3465944,
                    'description': 'ɇ3ΩŒӖτԦЭΠɳ\x91ǤϜ\x8cƲÉΓoɞŀˏƖ\x97ԬŷԡʷȤъӾ',
                    'real_pixel_width': -4037717440815776780,
                    'real_pixel_height': -9038815015797263875,
                    'dpi_x': 3176209879420886377,
                    'dpi_y': 3616713316678397786,
                    'supports_rotation': True,
                },
                {
                    'identifier': 2260344,
                    'description': 'ЍϥʽɝǖȍȇʷώǨ\x9aˀ½˗ЛëЪư\x84¢úшƫӑϩšӃ˪чԑ',
                    'real_pixel_width': -4305485664737131735,
                    'real_pixel_height': -131732382554517658,
                    'dpi_x': 2018562973414594854,
                    'dpi_y': 5460972468627109122,
                    'supports_rotation': True,
                },
                {
                    'identifier': 7074702,
                    'description': 'ήХƧπԥˌͶǖ\x96ʲЄfĴӵ˄ȏéȜӲo\x84Ł҆\x88ȱгǝϤˉƣ',
                    'real_pixel_width': -1293453423009336121,
                    'real_pixel_height': -1113257068861268573,
                    'dpi_x': 8240014330107632588,
                    'dpi_y': 1031641470881247712,
                    'supports_rotation': False,
                },
                {
                    'identifier': 6397545,
                    'description': 'ͼſRʊӰ҈¿ʱ¹ө\x85ʺʼŋȮɫѻТԟqǴҊȥАıȲϲъξω',
                    'real_pixel_width': -4202919489156964494,
                    'real_pixel_height': -7429280478762721376,
                    'dpi_x': 6813829007400939670,
                    'dpi_y': 6775291469270180478,
                    'supports_rotation': True,
                },
                {
                    'identifier': 5968501,
                    'description': 'ĳ;ŁĕǣrρɫΣȬΏɰĩœÊТТϬţϴѝϨĽϕȭѠċωΌʹ',
                    'real_pixel_width': -7649316331500840835,
                    'real_pixel_height': -3697080984824071375,
                    'dpi_x': 8003695739130702482,
                    'dpi_y': 6318985331399124843,
                    'supports_rotation': False,
                },
                {
                    'identifier': -93482,
                    'description': 'ЬS»ţǌѢЖƥʒ*҃ɃˈҙĿӻβŊЪǆĬҍхaԘɉʛʅhɳ',
                    'real_pixel_width': -7626622728933508163,
                    'real_pixel_height': -4161845881861867132,
                    'dpi_x': 3345026935863357726,
                    'dpi_y': 4170762409168833373,
                    'supports_rotation': True,
                },
                {
                    'identifier': 3407108,
                    'description': 'ԞɠʓԮɁ;ӎʉüUˀԉϏӶԟŰйșūζǾȓǟŨ˟ŀťɧɞ¬',
                    'real_pixel_width': -7798822229873067773,
                    'real_pixel_height': -5322496254532023305,
                    'dpi_x': 1330156679401903142,
                    'dpi_y': 7269003996335090334,
                    'supports_rotation': True,
                },
                {
                    'identifier': 8332260,
                    'description': '˔ғŒӻη˵ӓѢКɬӅ?Νӽҧʒ\x7fө[ιɍɼѣŋѻԪŵΠȰʎ',
                    'real_pixel_width': -8265181577932077997,
                    'real_pixel_height': -4115012403702937713,
                    'dpi_x': 7682151636334207106,
                    'dpi_y': 4115250079077237747,
                    'supports_rotation': True,
                },
                {
                    'identifier': -497976,
                    'description': 'ͲũʇΒřјnžэҰȗǪѩʕӆԜϲϸ˾ҼкΖʍȖĳ҉çɷϝɞ',
                    'real_pixel_width': -7249464821618941277,
                    'real_pixel_height': -4896239321291676184,
                    'dpi_x': 7501811466345850315,
                    'dpi_y': 7476137059016462465,
                    'supports_rotation': False,
                },
                {
                    'identifier': 3887738,
                    'description': 'ŀƛɟȏÓƵôÿмŇӁċD˙ӭ\x92ʤɾʩʝϼĬ¢ěӉϓ˦øΉӺ',
                    'real_pixel_width': -7360279253407672553,
                    'real_pixel_height': -673174099660483786,
                    'dpi_x': 4769143485709057771,
                    'dpi_y': 7275080838953080036,
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
