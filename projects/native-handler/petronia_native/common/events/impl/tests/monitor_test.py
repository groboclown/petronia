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
            'identifier': 972787,
            'description': 'ѯȠĠɳųлԝЌƉÏǭ\x7fЙԟяŅÈЄҜÓǔRŃҺӏȣʕ¼@µ',
            'real_pixel_width': -9183518649896722818,
            'real_pixel_height': -1410142082430414401,
            'dpi_x': 6705179139959233294,
            'dpi_y': 3806612380185066808,
            'supports_rotation': True,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 2286371,

            'description': '',

            'real_pixel_width': -7070104239103696095,

            'real_pixel_height': -4470721042743481487,

            'dpi_x': 1045763791359478786,

            'dpi_y': 2742205387687178867,

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
                    'identifier': 4054343,
                    'description': 'ԫͶɿԧþΑĸł\xadEɸϵʗáԊɴτÙūҘƜВɪȞǬΦΞ˘тā',
                    'real_pixel_width': -6321240407811402219,
                    'real_pixel_height': -8871413189648833011,
                    'dpi_x': 5654991393584394089,
                    'dpi_y': 8366296896984976309,
                    'supports_rotation': True,
                },
                {
                    'identifier': -460530,
                    'description': 'ȾӹώǯʪǋɿƿёͰʱӺǾ·ӮŎԋͶɼȝҾ·Â҄\x96ԛŘƸ·ĕ',
                    'real_pixel_width': -5577464436376576219,
                    'real_pixel_height': -4942243805778241563,
                    'dpi_x': 6317279635229871622,
                    'dpi_y': 2888218810681270158,
                    'supports_rotation': True,
                },
                {
                    'identifier': 886143,
                    'description': 'Ɇϛũ¯ʛ\x83ɿϬΐʗɧȀϳvºʪɛȈĢϷʰʀЦʰȍ\x8bɽΰǰO',
                    'real_pixel_width': -7734367783140774808,
                    'real_pixel_height': -891131563564313430,
                    'dpi_x': 3938214389088560232,
                    'dpi_y': 1211119325471670914,
                    'supports_rotation': True,
                },
                {
                    'identifier': -102203,
                    'description': 'ҧоņ¼Ǽȑǘ\u0380ԂŭȔ$\x94φ]ʖмͱ\x7fĜˑѧȏȬȖҕΓÊĲá',
                    'real_pixel_width': -8393406436117433400,
                    'real_pixel_height': -4393759978841788157,
                    'dpi_x': 5712352565419467061,
                    'dpi_y': 5308335845835530044,
                    'supports_rotation': True,
                },
                {
                    'identifier': 6572128,
                    'description': 'áʍõɿŐҵѻ˶Ҏѽˢц\x86ƖȭРļųƓϙǍæ³ȲͿͻBʈ\u038bЎ',
                    'real_pixel_width': -1926695164978404578,
                    'real_pixel_height': -25646259077233826,
                    'dpi_x': 56480030950854863,
                    'dpi_y': 3318567749444310810,
                    'supports_rotation': False,
                },
                {
                    'identifier': 2294649,
                    'description': 'ɞϮƝùǼǒΞĖ»ʾХžɾOʾȌ\x97ѥѕʩҡЄʓϺʞɌðŏϖζ',
                    'real_pixel_width': -919026808048375873,
                    'real_pixel_height': -7355537037587043166,
                    'dpi_x': 5512245896021230878,
                    'dpi_y': 8614846239429100821,
                    'supports_rotation': False,
                },
                {
                    'identifier': 4533826,
                    'description': 'ơLMͳȮ2Ľԫƹ¢ΏҥфϏӫơŨŇǼåӼÜǷÈÞϣӞԜкӣ',
                    'real_pixel_width': -7053868573726791301,
                    'real_pixel_height': -4711505586672858644,
                    'dpi_x': 4430103642436011433,
                    'dpi_y': 7991858398587362592,
                    'supports_rotation': False,
                },
                {
                    'identifier': 8535295,
                    'description': 'ɟíżɀԗsъ2ʛӋŁÝ˟ȘӺʄƱ¨-°ЗͲӵԍћҥ˓Ѻ\\γ',
                    'real_pixel_width': -5674938121045220037,
                    'real_pixel_height': -8637101238704989444,
                    'dpi_x': 2012900907598003573,
                    'dpi_y': 6675867112216162927,
                    'supports_rotation': True,
                },
                {
                    'identifier': 584636,
                    'description': 'ΦŰθêΡƋżʃŷҁеGӑӣӱӝŗǶжѾīЯƇđи˫˶ѕ«ӗ',
                    'real_pixel_width': -5010007596000548495,
                    'real_pixel_height': -730786766351678039,
                    'dpi_x': 2337003416035541635,
                    'dpi_y': 2849684693743442760,
                    'supports_rotation': False,
                },
                {
                    'identifier': 8430865,
                    'description': 'ɹ˒ϘΪŃӛ~ɂҏ6ŁMJӸȔȷƘǍӟϖȿθ',
                    'real_pixel_width': -9162741469062177500,
                    'real_pixel_height': -3907249321232242011,
                    'dpi_x': 420914804819644130,
                    'dpi_y': 6389480136219162831,
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
