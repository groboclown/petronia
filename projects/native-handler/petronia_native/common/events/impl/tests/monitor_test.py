# GENERATED CODE - DO NOT MODIFY
# Created on 2021-03-02T16:58:22.625367+00:00

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
            'identifier': -719036,
            'description': 'ƀҠӟШǱɫǚѼƄͼv˳Șɿ҄ɹĸŷ͵ӄĻίU\x84\x82ɔȶїΨԃ',
            'real_pixel_width': -5144079236843475497,
            'real_pixel_height': -5459568710683701673,
            'dpi_x': 3322125102672400662,
            'dpi_y': 8432776313020495774,
            'supports_rotation': False,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 6187775,

            'description': '',

            'real_pixel_width': -7581291983021214134,

            'real_pixel_height': -4358482597565432132,

            'dpi_x': 6514823842716510174,

            'dpi_y': 1806778125847923722,

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
                    'identifier': 7744403,
                    'description': 'ɦÝĘɛǛųǴԒ5ǦǘШԞϤǀɪӱĪėѭԐƸǄΗЋƥƎpòѷ',
                    'real_pixel_width': -6070640912157899269,
                    'real_pixel_height': -8094384427104210340,
                    'dpi_x': 3780294934492416315,
                    'dpi_y': 4592709280677742037,
                    'supports_rotation': False,
                },
                {
                    'identifier': 70790,
                    'description': 'ЭӶȞƎΎʯȣԊˬĳǍşïЗӑÑҐǨƽĐлȈʐÌ\x9dүʛɜȶϯ',
                    'real_pixel_width': -5628968167036198590,
                    'real_pixel_height': -2042381799934398679,
                    'dpi_x': 2518376414462186783,
                    'dpi_y': 6790173291417880571,
                    'supports_rotation': True,
                },
                {
                    'identifier': 2463492,
                    'description': 'ßƑBβɯеԒ˫ƣЁGϚʶŧÏŤǣ÷ˀþ˚ȐNɔӚεƟťNʏ',
                    'real_pixel_width': -6601010203288491019,
                    'real_pixel_height': -8046810656893776938,
                    'dpi_x': 798695872685383605,
                    'dpi_y': 6258969950498355931,
                    'supports_rotation': False,
                },
                {
                    'identifier': 6505109,
                    'description': 'ӱŤƥғˉɛӿήω[ʧӏǱӆсvʵũӋӸԎ$˕ĠѤʀ˽ҦƀƐ',
                    'real_pixel_width': -3469312767635136547,
                    'real_pixel_height': -5321710913222706938,
                    'dpi_x': 1326901002016559115,
                    'dpi_y': 5937935259915008421,
                    'supports_rotation': True,
                },
                {
                    'identifier': 2316530,
                    'description': ';ӏΥӠVΚͿЗɖѵΫͱ$˞ǤǦʵɝ\x80ϥѲĒѰԜƴĀĘeƑʏ',
                    'real_pixel_width': -3379283713573873757,
                    'real_pixel_height': -7675897451187972120,
                    'dpi_x': 3857945138613058080,
                    'dpi_y': 1208239009465031240,
                    'supports_rotation': True,
                },
                {
                    'identifier': 1573278,
                    'description': 'ӝŢөϗƯɿYƵȿ\x89Ñ˵Ӷћy\x8cŅeίɓнɆʂĲψ˶Гõ\u0378½',
                    'real_pixel_width': -3330473745799732882,
                    'real_pixel_height': -8876289039804540952,
                    'dpi_x': 8038631296869174257,
                    'dpi_y': 3115318299979576788,
                    'supports_rotation': False,
                },
                {
                    'identifier': 1571588,
                    'description': 'űσ\x94ƷԈӺЖ\x95ΚԒĤʐιźʇȵΩØʁȉѤЈӸ\x9džļƍɖȅҵ',
                    'real_pixel_width': -8460648205979109028,
                    'real_pixel_height': -8050924464307618153,
                    'dpi_x': 2702908039040069761,
                    'dpi_y': 726328753839511344,
                    'supports_rotation': False,
                },
                {
                    'identifier': 988541,
                    'description': 'ΨéГgҡѰąԙҡʦϰϖЄÝαƌǻФРYԌë˛΄JѩˋәɧҰ',
                    'real_pixel_width': -7735541927957738915,
                    'real_pixel_height': -8329074757096858895,
                    'dpi_x': 3689437768026811306,
                    'dpi_y': 5622038564072111943,
                    'supports_rotation': True,
                },
                {
                    'identifier': 5016892,
                    'description': 'Ϡϊβʨ˛ɴϹ΄Ԋĕˋňʾ˝ ɵʣːԮ0ʍ˺ȼҐќɣĶ[҄ϒ',
                    'real_pixel_width': -3095876725680172285,
                    'real_pixel_height': -6559059580211920153,
                    'dpi_x': 7937282569155575652,
                    'dpi_y': 5266500405186697543,
                    'supports_rotation': False,
                },
                {
                    'identifier': 7037140,
                    'description': 'ҝÜíĺ}ĜųʿɩBˠяȒĈŷĢΊȆӥѪРǔϜȇɋѩӤĮʮӒ',
                    'real_pixel_width': -7901585313734568945,
                    'real_pixel_height': -3196194318422670750,
                    'dpi_x': 1499852991851742071,
                    'dpi_y': 7611233213938121195,
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
