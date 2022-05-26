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
            'identifier': 5790397,
            'description': '\x82ƴǄŕŃȂЅЛгҷ˧\x98\x8e˘ԊōЗЇ˴0¼Ȯnnɨάyƕŏõ',
            'real_pixel_width': -5909248616355472222,
            'real_pixel_height': -5147134124400596702,
            'dpi_x': 7572174635588038441,
            'dpi_y': 2926302307284295379,
            'supports_rotation': False,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 1794168,

            'description': '',

            'real_pixel_width': -3787155823575606629,

            'real_pixel_height': -4314919297151165835,

            'dpi_x': 3422440720409702534,

            'dpi_y': 97962367885454673,

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
                    'identifier': 7643405,
                    'description': '˪˾Ńdǃ·\x8dƸ*ˋɟԚø»ɧϛĞŗ҅Ȱâı˾ҍҩШȈwÊʙ',
                    'real_pixel_width': -7634504704177012519,
                    'real_pixel_height': -2703213992097246064,
                    'dpi_x': 1079682958181226797,
                    'dpi_y': 89227576835759548,
                    'supports_rotation': False,
                },
                {
                    'identifier': 8211716,
                    'description': 'ӉҲ\x9bΰ˷˒ƎďԂ˩ƾýМɬȾƊΥ(ƹӡƵƛԜģǱnӰʷ҅б',
                    'real_pixel_width': -4801257035504040600,
                    'real_pixel_height': -2543589429153780165,
                    'dpi_x': 3467248336651250636,
                    'dpi_y': 5707331302147227394,
                    'supports_rotation': True,
                },
                {
                    'identifier': -850363,
                    'description': 'Ђşŷʎԛǯйǆӭ˶ǡ=2ĜόԖȿ~ȡȟѽâӯŧʞˉ\u0382ӁԁӶ',
                    'real_pixel_width': -7706746162308019799,
                    'real_pixel_height': -2392466229006348900,
                    'dpi_x': 8020178907398964259,
                    'dpi_y': 8879351789400365728,
                    'supports_rotation': False,
                },
                {
                    'identifier': 7917932,
                    'description': '˨ʮˎɤдõѰÊΚ¨ʁӚ.ĦЯɋƎѺҒͳyƞ˗Ɲ`ɕфŬś\u0381',
                    'real_pixel_width': -8395678401023164396,
                    'real_pixel_height': -3808402504648088792,
                    'dpi_x': 7438187283632099548,
                    'dpi_y': 4191573822098445332,
                    'supports_rotation': True,
                },
                {
                    'identifier': 4528254,
                    'description': 'ʍǭϼΪëҪ9˥ӥњňϔŵʨɬѷĝѱƛȱӸˣЀǰӄɨǕ϶ȮǗ',
                    'real_pixel_width': -3704926904472184902,
                    'real_pixel_height': -8705835910686986998,
                    'dpi_x': 7188288565531855825,
                    'dpi_y': 5344840596561215175,
                    'supports_rotation': True,
                },
                {
                    'identifier': 8907934,
                    'description': 'ɭÌùҷȜɇ\xad]ϖӄƭ˒ϯŞ˄ǊȡƶáɠRRѾЇͿΞћCȋ˯',
                    'real_pixel_width': -4976791648661010139,
                    'real_pixel_height': -3586542501790374291,
                    'dpi_x': 1687661430826481096,
                    'dpi_y': 2150621471239927418,
                    'supports_rotation': False,
                },
                {
                    'identifier': 3500239,
                    'description': 'Ǽ_ÊҝѾҟ+Čʎʜ˜ƙ#ōӍ˙ÞȆĔΣ}ДxyϢ&УͽŹɿ',
                    'real_pixel_width': -3995529986235711363,
                    'real_pixel_height': -9190090878932913602,
                    'dpi_x': 4241548953003518537,
                    'dpi_y': 6908488686319284484,
                    'supports_rotation': False,
                },
                {
                    'identifier': 9168431,
                    'description': 'ўȤ<ˆįİҨɝ;Ș҈ɢҏʸƇřж÷5зҨɝǥȤԒҳѥęɩѦ',
                    'real_pixel_width': -7531100453594393708,
                    'real_pixel_height': -622226377295855985,
                    'dpi_x': 2755030068633776260,
                    'dpi_y': 1610943316422888052,
                    'supports_rotation': True,
                },
                {
                    'identifier': -31684,
                    'description': 'ӓé\x92˒ĈƚğԬƞƚϦίoӉǡ\x9cǠŹʧįŠɏȭķΈЍȜ˰ϋƍ',
                    'real_pixel_width': -5388105059465573677,
                    'real_pixel_height': -3284009532135492788,
                    'dpi_x': 6640094460422640620,
                    'dpi_y': 8076624918186381589,
                    'supports_rotation': False,
                },
                {
                    'identifier': 3172203,
                    'description': '\u0383ȯɃǠȝ\x98ԑʰ˕\x90ǵΪčĤ\x81ʆ˘ҶѤŮԌ@˯ųƓɻʡӮ϶о',
                    'real_pixel_width': -6757282751042218164,
                    'real_pixel_height': -4605856291576069910,
                    'dpi_x': 6121566546493713370,
                    'dpi_y': 8811412185827008954,
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
