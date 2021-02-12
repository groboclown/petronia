# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-11T17:55:50.481567+00:00

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
                dict(field_name='dpi_x', name='Monitors'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='dpi_y', name='Monitors'),
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
            'identifier': -322853,
            'description': 'ɓΚ3еΘøИǴɴßǅцǉϵԡʜʀɖԨİĠιāXƁŋ˽ǥöƤ',
            'real_pixel_width': -7931428217582481050,
            'real_pixel_height': -9189160859954427283,
            'dpi_x': 2499220797258195911,
            'dpi_y': 7550344538779925151,
            'supports_rotation': True,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 3235591,

            'description': '',

            'real_pixel_width': -3790372290716295131,

            'real_pixel_height': -4311920662671119246,

            'dpi_x': 5112997597883769730,

            'dpi_y': 1590314644419596584,

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
                    'identifier': 4098253,
                    'description': 'öĶ²Ͻɞɇ\x8f§ҥδ˃ǚȕˣĒǤǬΣͼӐȗ˵ԩӝŜϒĠȅ\x9aʾ',
                    'real_pixel_width': -6940239251467998368,
                    'real_pixel_height': -3404774507342364620,
                    'dpi_x': 6875058981905361646,
                    'dpi_y': 890858859583127682,
                    'supports_rotation': True,
                },
                {
                    'identifier': 612991,
                    'description': 'yǀҟ˽ɮɇΑԕuû\u0382ӀҒЛWͼĉ˺ЖϿɭŔvΫџǵƠʾ͵İ',
                    'real_pixel_width': -8199213164593697043,
                    'real_pixel_height': -1526124351150773772,
                    'dpi_x': 3985760193735528999,
                    'dpi_y': 1147122972301304739,
                    'supports_rotation': True,
                },
                {
                    'identifier': 8237437,
                    'description': 'ϝƣӁ\x9d¯νǙӶ\x8cͼ΄Ɠȡ<ķɏҊ(ӤӠÙȷƆ0ѕÒюȑӋʶ',
                    'real_pixel_width': -4127684070208016050,
                    'real_pixel_height': -4936836240410833726,
                    'dpi_x': 1179154999918662628,
                    'dpi_y': 8008538414004015022,
                    'supports_rotation': False,
                },
                {
                    'identifier': 8060112,
                    'description': 'ƿϓ\u0382ºŗЍȕІȲ|Əʭˋ°ʣǮȃБя˝vŨԚϓ\x94',
                    'real_pixel_width': -8623608956114973399,
                    'real_pixel_height': -8103007994781068896,
                    'dpi_x': 3781663718292051452,
                    'dpi_y': 2210395665537197267,
                    'supports_rotation': False,
                },
                {
                    'identifier': 8017040,
                    'description': 'ўʂӐƕκ\u0382ȕĆôƱԅĀƓǷǻВĄдɻфύУѠÛúȕʤȵЭʜ',
                    'real_pixel_width': -3690696606702245095,
                    'real_pixel_height': -227446835887084466,
                    'dpi_x': 2951574627208275946,
                    'dpi_y': 3521238537590529944,
                    'supports_rotation': True,
                },
                {
                    'identifier': 8810004,
                    'description': "ŇӗИÑȶĈ'μѿǲ˗˛ӑԢ1ǊέƊάǃʛбȬ҂оȨƸǗƺɜ",
                    'real_pixel_width': -2215937885460481767,
                    'real_pixel_height': -405564313108977947,
                    'dpi_x': 5070018250864044827,
                    'dpi_y': 6688320652475544204,
                    'supports_rotation': True,
                },
                {
                    'identifier': 7896340,
                    'description': 'æ˯öǭгˎҬɃDһƩҜϏԈҤϭƊӢ\x97˧\x96ЮƌǴʾ\x95әɹɎ±',
                    'real_pixel_width': -9021882179973750997,
                    'real_pixel_height': -1142666132597406868,
                    'dpi_x': 7836118980378747515,
                    'dpi_y': 2655990695430202686,
                    'supports_rotation': False,
                },
                {
                    'identifier': 4352463,
                    'description': 'ɨÆʆ\x8f˙qœεaΰҖĊȐК\x9cɝŁ˳ʳԋВ\u038b¯ΣƎʵɊҴŀʀ',
                    'real_pixel_width': -8051669988158439537,
                    'real_pixel_height': -1670714286380847070,
                    'dpi_x': 452890180084904792,
                    'dpi_y': 3434412189119550114,
                    'supports_rotation': True,
                },
                {
                    'identifier': 5592350,
                    'description': 'b5ȰÓǒͰңƯ¹ќΥʷʶǈƇӈóΑŒ£ɐǿʑϤҦθпʴѮj',
                    'real_pixel_width': -5130245061228236815,
                    'real_pixel_height': -5309209244363058532,
                    'dpi_x': 5726483246212349016,
                    'dpi_y': 4524417963826554108,
                    'supports_rotation': True,
                },
                {
                    'identifier': 1385658,
                    'description': '¾˺ʬʚƲ\x99јɧДɆjǧΜӧ˯ЛɈϘΗʠš¥ȿĊ\x83ʹӏÿƗԝ',
                    'real_pixel_width': -1178337815619831738,
                    'real_pixel_height': -3323130912367990261,
                    'dpi_x': 6304176997598077589,
                    'dpi_y': 5998333188126934115,
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
