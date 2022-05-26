# GENERATED CODE - DO NOT MODIFY

"""
Tests for the hotkey_binding module.
Extension petronia.core.api.hotkey_binding, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import hotkey_binding


class SetMasterSequenceRequestEventTest(unittest.TestCase):
    """
    Tests for SetMasterSequenceRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_MASTER_SEQUENCE_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.SetMasterSequenceRequestEvent.parse_data(test_data)
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
        for test_name, test_data in SET_MASTER_SEQUENCE_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.SetMasterSequenceRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_MASTER_SEQUENCE_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='sequence_type', name='SetMasterSequenceRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='keys', name='SetMasterSequenceRequestEvent'),
            ),

        ),
    ),

]


SET_MASTER_SEQUENCE_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'sequence_type': 'sequence',
            'keys': [
                'ʧРĔɐɵҙʣӴðѧıĖϫѰйNDбšёɩ',
                'Ѵ˝7ǟέЁҰʕȟ«ҏɲŷɘ˖ˎѹСǰԍ',
                'ÔýʺуύϠҋӲɨáċRӄĆѥɮ¸МεȼyѼӮƳ¸Ǧυј',
                'ƘǽȦo˩ӋȜԝ\x8bεļϩϺÍϴƨԇˊˋѕҝ',
                'ɎȞǵŗɰȓıϟʠŨϋɑҭƿǂϘìҝ',
            ],
            'comment': 'ǣͻʰġ^ƻȿƪĉԦǛИǋƔȝԂБЯϢѩӑ4Ȕũβ\x9eΚ\xadûΛ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'keys': [
                'т',
            ],

        },
    ),
]


class BoundEventParameterTest(unittest.TestCase):
    """
    Tests for BoundEventParameter
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BOUND_EVENT_PARAMETER_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundEventParameter.parse_data(test_data)
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
        for test_name, test_data in BOUND_EVENT_PARAMETER_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundEventParameter.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


BOUND_EVENT_PARAMETER_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='key', name='BoundEventParameter'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='value', name='BoundEventParameter'),
            ),

        ),
    ),

]


BOUND_EVENT_PARAMETER_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'key': 'Ԟ¶\u0381ҞСõǆ\x8b˅˲ÑŕѣҜʆϾϸϊЪƧӬƖϴѨѡͺǜėҸξ',
            'value': 'ҚȎ\x9bЫƌǝџԩ\xad˙ɯƲʐɹΰʫʈŊŰɯқӁ˝ɀǬɇúζ˯Ӈ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': '\x8a',

            'value': '',

        },
    ),
]


class BoundEventTest(unittest.TestCase):
    """
    Tests for BoundEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BOUND_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundEvent.parse_data(test_data)
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
        for test_name, test_data in BOUND_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


BOUND_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='target_id', name='BoundEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='parameters', name='BoundEvent'),
            ),

        ),
    ),

]


BOUND_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'target_id': 'Ҭˠ΄ɘВ«Ǜˠʉԉ(βюŭЛǂÙОVŎŴʳҖǧԅÏϣиɌˤ',
            'parameters': [
                {
                    'key': 'Ǣˉ#ƊǱƬɁΨΧȖԋŰʵоԩ½èˑͷѝ',
                    'value': '!ԎêœέʯkӧÜʐҳͱǪ҇ϥǖηŚьӈŒӒӂѻ^Ð\u0380Ϯǽé',
                },
                {
                    'key': 'ųɥʠȷŅƃǳȸΑ\x8f\x81əüԟ˝ʼ˃\x94ҕӓȁ*ľ ќɗμԪҐͶ',
                    'value': 'ĂʥåϠΨȬDҡWŲˋ˜ĊđġʹīΆеԈˍŷԔφӦűˇǴ˯Ο',
                },
                {
                    'key': 'ѮǜȘҠѳ\x82ѕä˹ӾǃĻm¯ǚɔдŔ$<ϰλÕŒʮɕԬѹɣË',
                    'value': 'ϑдѼͷѢрǚ!ɏ\\ˊЛ[ϯʘɴÑѕҝҷюαΪΒƽȪɻʩʶɚ',
                },
                {
                    'key': '?ѻǽðåэÛĆĴ¨úƋɭĨήҢ˓ÉɟʲŲѩж\x8dʎɬΚǲҸƋ',
                    'value': ']ÅάЏ˜ǓΎѫɞҐǛűδǍѾȱΕҚːǷɓϴӑƠȟΐĨȆȡƾ',
                },
                {
                    'key': 'Ħύ¾ÕʱĻοԘ.љ¿ˉɾіӭ«\x84ÐKɢɑȗôέҌ>ȏϘǷó',
                    'value': 'ʖщҝȦfƓσøƭľbҠ¥ϗą˷ԝ2Ѹъ¤ʾәƩíӁǂ\x92đΎ',
                },
                {
                    'key': 'ɫԃғΎɢn_;ђɶϾǀˠӻAŸɎƱ\u038bʢąΝӸɌЌ҅ʹʤ',
                    'value': 'Ǝ\u0378ķɦѥіӶӉӒQćEүԛԀДʢ¦ÙÈŞЍ?ƋȢǱǭԟΝ΄',
                },
                {
                    'key': 'ƁͱϘǄʂȝνĉ',
                    'value': 'ʯ҆Ҿ§ʐǍƼӨɲΧΆТϟĝԖ˴ǺœʋѡӜԏдҠЪԒǻɦ3ň',
                },
                {
                    'key': 'ˢѣÐΙƠЖʝČŪrщŋVӌХűȿǣȔȇȧƙǌ\x84°jLòђ˰',
                    'value': 'бǶҍҪĦ˪ҙҼέɤ;ɋɨŘϘʾɎįÕʀѲʹͿѡʘϥԒ˴ӯg',
                },
                {
                    'key': 'ʶӮҲǟˬҏͱԊɋϋϊcФŘϻ¡Ŧ\xa0ƀϼȼááðˍɞċƨ^˹',
                    'value': 'ϬĳǋҲʵG\x93ˏШ#ɯǹĲȕŠĀġɲϝѱԡŬźŐ˜дʆҠŷ˹',
                },
                {
                    'key': 'ҋƃӤԟЄν¹ǛѨΉΦÕ;ɭ\u0382ɝЂʹϨΊǴԮ˴?ͷqҥ\x82\x80Ζ',
                    'value': 'ԣ®Ɵ\u0378ϨƿâДÕƼɤ˨ӗӈɦdҾʶԔεġЬƊĉʈ¸ѸѼżȥ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': '˶ϖԒĜɷ',

            'parameters': [
            ],

        },
    ),
]


class BoundKeyRegisterEventTest(unittest.TestCase):
    """
    Tests for BoundKeyRegisterEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BOUND_KEY_REGISTER_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeyRegisterEvent.parse_data(test_data)
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
        for test_name, test_data in BOUND_KEY_REGISTER_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeyRegisterEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


BOUND_KEY_REGISTER_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='keys', name='BoundKeyRegisterEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='event', name='BoundKeyRegisterEvent'),
            ),

        ),
    ),

]


BOUND_KEY_REGISTER_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'keys': [
                'ȑԔïқlĚzҐĊͱɅЍŒˍǾѐѫΪӭȒв',
                'ˊҁ',
                '÷Ѥ\u0381ɋʓǝѩЬʊϭԘˌȜҎмÙÛӮ',
                'ÈƯɿȆǤȌʹ¡τʃүǶĖ',
                'ЦүFɾũʼ˒ԙмɏ',
                'ǃҩѭЯϜǬ/ԌŗӇ´Ϳˠ',
                'ÂǜӭȫΒǍҳ˚ȲâpʂFaŊ',
                'ӚƉǎώȰљ˯ȒơѶ˫є˺lҙQǁǡϻЁ',
                'ʝʑәPǰԔÃċMƴŧ',
                "ѩԕĮЅȋȻӔʪƘˊȀ΅Ϣϳрѵʤӕm'ÿœɞ\x84\xa0",
            ],
            'comment': 'Œ·ʵbӊʼԩѲΓĨԈѿЭӛĜχ\x7fȪÜѝήƎСÈЋЕΑĽ»Ǣ',
            'event': {
                'target_id': 'ƪ˽ôʇƍmрʺӕҴŀԚĝΖҰĔħœрȹɞзƐ˸σЇƚȸ×ѝ',
                'parameters': [
                    {
                            'key': 'ºÉǄѻҥŖôɐɉħBӥԮm˅şҡĵÇŦȝPҟ\x93ԍƘɷǤБ®',
                            'value': 'ǉ1ӾȣɇҸāÏƊʾˑϱδǎƸƏМǥ\x9fŗŒԞɌWƻҍ!ҎþƮ',
                        },
                    {
                            'key': 'ʃкжɯҹɢmȁ\x82',
                            'value': 'ǤÆϧ˃ưѤӻȜЬRƓчϡѯ·рƶɞˢώʿûłȉҨƴǂ\u038bʉ˗',
                        },
                    {
                            'key': 'Ƽʬϵʔȍ˭Ŭæӣʹʳˇ\x81йĭ',
                            'value': 'ȒшʻӠӗԟјҬĻɣɈyʇјɇĥ˯Ϝҥǌҽ¢˩ʷѕ˗?Ӷxĵ',
                        },
                    {
                            'key': 'ѻ_љBϾ´ƴɖaҼƔҚŢ҈Ϝ˅ʫąȡοˌΩȍǮiβOİξϼ',
                            'value': 'ɛAȌĜˀαϚȧΔ\x9bѕκ\\Ɛȅȑʆ\x83ԂҚȅҘUКɯҝЧ1ɈԪ',
                        },
                    {
                            'key': 'Ƙь˂Ǚ³ˌԚ\x94қИ!ɂΕȣЂʀŰϴʽԘ\x87ʮӡ˛©ϳˈɘűˬ',
                            'value': 'ХşЋĚШĖʲБӞFÐŷÞÇɥZɚʣѬ\x96ҘԔŬƠΤѢУfЪЎ',
                        },
                    {
                            'key': 'γϏϿɤǖɦӒŠТԂÆ(ğƈҚ˖Ǻįƿ6ƕŲӰѹϦ˹ɼь¯њ',
                            'value': 'ӂ-ΝϽvŸüωΰƏϹŧ®ɱİ®χķҞѷúѻϜҍʩЯɰҖĭŸ',
                        },
                    {
                            'key': 'ɑ\x92˞×ť',
                            'value': '˼ßϫȀЧ˙ʃӛĝrǝѐɍ¿ʙҞӮʆǶӉȧ˕ČѱƘ¥åƢeΠ',
                        },
                    {
                            'key': 'ƙƵϦ˖<ҏĐʕʿƷόQ\x84ЋЍŤʉѽã˷2ȣͼœǵҙȮēρЭ',
                            'value': 'ҐñŊӵѽʣȋͽʨUӒškɍȑÎ?$ӫŷ϶ɕϮѧƝɞοǃљϢ',
                        },
                    {
                            'key': '_ԛeʢһʮϜ˷íşѕѱïɅɫʏҕњʰԮ\u038bƈŸȩƧįŧɘҞъ',
                            'value': 'њĈcӪΟƧůðÀȩșδԔňê˓Ϣ˂ư϶˟\x83ĀƲӌӹəфÙɓ',
                        },
                    {
                            'key': 'ƐεˏԜ\x8aÞŴʦϖʋȥʛ˙ӃǳќľɺɕϤѠЍєŗϰӻѦԌҥ˫',
                            'value': 'ԠżȯȲӲәͰǇÖ¾˰ȻŊĺŢћқȃԅҵCͶ\x97º˔~βǸĎ\x8d',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'î',
            ],

            'event': {
                'target_id': 'ȃҠ\u03a2ʽū',
                'parameters': [
                ],
            },

        },
    ),
]


class BoundKeyRemoveEventTest(unittest.TestCase):
    """
    Tests for BoundKeyRemoveEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BOUND_KEY_REMOVE_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeyRemoveEvent.parse_data(test_data)
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
        for test_name, test_data in BOUND_KEY_REMOVE_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeyRemoveEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


BOUND_KEY_REMOVE_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='keys', name='BoundKeyRemoveEvent'),
            ),

        ),
    ),

]


BOUND_KEY_REMOVE_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'keys': [
                'ʭșӇŞ˧\x85Ï',
                'ԖɣƟ˘η˻ĺqοƄτƅɶšĴӔÿFЅТǨi\u038bф',
                'іJ',
                'Ɓ',
                '3Żӿ0Ű',
                'ʒʭΎіŶˊϕɛΘͻ\x8dğɻáǉʹÇҼТђҎҨҎɕ',
                'ԍԪҠ·¬ѽɩìɌȮɦԒԆŚΉРşӆÒȑʫWчă»ĳŚȘ~',
                'ˑ Ëϟцïërˍҕ\x9eϱƶԙÝɌКçĺ˕',
                '϶',
                'Ƙ҃ӈXψɭȭǮřͻÏɁǩ\x84ВϋǐȝĔïчǱ\x97\x9eȠƭƜПƭv',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ŵ',
            ],

        },
    ),
]


class EventParameterDescriptionTest(unittest.TestCase):
    """
    Tests for EventParameterDescription
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EVENT_PARAMETER_DESCRIPTION_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.EventParameterDescription.parse_data(test_data)
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
        for test_name, test_data in EVENT_PARAMETER_DESCRIPTION_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.EventParameterDescription.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EVENT_PARAMETER_DESCRIPTION_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='key', name='EventParameterDescription'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='description', name='EventParameterDescription'),
            ),

        ),
    ),

]


EVENT_PARAMETER_DESCRIPTION_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'key': 'oȸ\x80ҨИѹƨƄ¨ΞÃāŮʊӲõӡCѴϳX˫ө˷ŕʾԜŕǍɣ',
            'description': 'ЌƖțǶƆΙ·ԜЁȪʑȎѢƼƅȁĢҏʐºϲΨʭǤĝЄ;lˮʞ',
            'default_value': 'ʨϚ϶ΦεЪïƀǚ\\ȗʧŪǷбʑό¼Ο\x9dřēȗɠƹӸϨ!\x98ý',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'â',

            'description': '',

        },
    ),
]


class ExtensionEventRegisterEventTest(unittest.TestCase):
    """
    Tests for ExtensionEventRegisterEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EXTENSION_EVENT_REGISTER_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.ExtensionEventRegisterEvent.parse_data(test_data)
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
        for test_name, test_data in EXTENSION_EVENT_REGISTER_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.ExtensionEventRegisterEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EXTENSION_EVENT_REGISTER_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='ExtensionEventRegisterEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='target_id', name='ExtensionEventRegisterEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='parameters', name='ExtensionEventRegisterEvent'),
            ),

        ),
    ),

]


EXTENSION_EVENT_REGISTER_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'Á\x9fΧɏйԀǱҨǰтŚҘǨŊhǹϑҐư',
            'description': 'ѺҎҠÌΓ¹Ê\x84ǰӁŃuęȍЋɗÈԌųɾеĐʩѲdœЩćјғ',
            'target_id': 'ɬƊŕҾIҸĳҲӳʹĽΌҶŧϝʨ\u03a2\x85.$ҨǾȅѳͼʧyԈƾʊ',
            'parameters': [
                {
                    'key': '¸Ӿ˷ˉȏĉҝǵЀ΄СΥέƊ҈˗¸ҟнʶę¸σ\x90οƙȋŬêʛ',
                    'description': 'ʌɫ3ƍȇʒƀҷƷxԏвƑǳȒʼǔ>ΠʮȑХʈuԣάƧʮŊÈ',
                    'default_value': 'ȺKͺύ˱ҤӜăљөºǽȶē.ŧȩʔҕԝ¢QŚ˚βƾŕǼȈȩ',
                },
                {
                    'key': 'Ʀ҃ŦȧΔ˷˩Dŵ',
                    'description': 'jǾĐɇÄӕĄȚϤɍʒ˚ŵƙҿΰ\x87K\u0381ơȌЯԚâÀΪӿƎ\xa0Ů',
                    'default_value': '³Ɵ҉ǱαԥПǜɫQăфɑѱ΄ĠϴʝʖĂɀѓԖҦƮћϴˮˏǼ',
                },
                {
                    'key': 'ːYπʾаŘњϥűӠɃŘŋ',
                    'description': 'ԩŶȁѕдůԍɟƣƧʃл˃#®ʙцџԕΝǆάҀÈȃ¦`в\x96Ǌ',
                    'default_value': 'ȠĎзӁʤ\x7f˭јόʻŢј¤=ǭʂΚ¸Ϗ"\x8bȕ˓čƦºŸȇĭt',
                },
                {
                    'key': 'өͿ˩ЏСԂϾѶȯ\x88ҹ«ȂŮŝƾѩʹϒƗǌÏϼЉͶœĵҫЕҗ',
                    'description': 'Ҙœс\x90Ο\x9eδҼҭӓӯК\x8cјƱқƲŊЗVɿО\u0382ƀģƭĵ\x86Ӯ˷',
                    'default_value': 'ӇǌɬɠůʮgУʞ\u038bˆΒΘ3ǎ)ɼ\x8aΑʙǨ\x99ˊЧιĎÑТƤϾ',
                },
                {
                    'key': 'еˠ;ҔҎƤÐІǾƝŭő5Ìәè\x80зʝͻŞӷǿÂυʲȮÕˇҼ',
                    'description': 'ΜGƍÌƽç5]"Ώj҇éRǨьԄ¥ϞԖϹǄ˽\x84ўЈŝӧίǳ',
                    'default_value': 'ɧνӜǶʑǗˇЪҢĆ˗ΕɑʥˊȔГҙϝıƲ\x9fӂ˦Ӡ\u038bÈĹӷɿ',
                },
                {
                    'key': '˼ɡɐBɾˆϘʧЬӛҺА˒ƓǟƤ˩ђ˔9ƪ/ȼέӆĵȽƹυɫ',
                    'description': 'Ҍϔҹ3ËȒ҃ԩϣμʓʈʐ˝лӵʠӷԠʴўȲİłƼȅ«źȉȀ',
                    'default_value': '˜Џž\x87/ĉӏȫąːθǧĩʶƨΝ˴Tǒ¨ПчƮ+ùԜΊԤƏɚ',
                },
                {
                    'key': 'ƚкϔҝԫСϵá&ĖӘВϞǶԗИԜә҄Ξѧʈ·šѸ¤ėõjʹ',
                    'description': 'ɣ½°Ƴ/ҽĂĀӁþɍŪƫгɶʒʩʶ¾nЋЁțɁΔ;ΈżԠϺ',
                    'default_value': 'ԚЖОʾӛо¦ѷ\x9dǬšӥǯǪϡɟɣl˺ӥѾϥÒ÷мöӒɀǟў',
                },
                {
                    'key': 'ɘ͵·Ϣċ¤mƣʖԒĉ\\ɚʃӼǊ)ӏœɬ',
                    'description': "ǶѕЂω'?ҐѐɳӨŬªʽЂȚȞȒюѐɯ¯ӻӀˌ{ˁťƔӕʞ",
                    'default_value': 'ˬÅƏ¬Ǔ\x90τҺιŹʋƦÚǃ˝˷;ҜɡΓԙ˲ɕӎˏʄż҄ů%',
                },
                {
                    'key': 'ԮӦӟȨK\x98ķʿТĄԏȕиƋTɲȸЧ˧бǛξLŻǝȈ\x9cíԩѷ',
                    'description': 'ͺȿŀƶέóɃǸɪȷÍʕњΉŊȥƉҪ¨nǺǤөɲЂÞӖƂːО',
                    'default_value': 'MЬύćΈ]ǥʚ¥\x96ŜӒĮИԑīĻȫНΧƺʱÝх˼ƪȍçӼӳ',
                },
                {
                    'key': 'đќûɖ\x9cҶ\x94@ʪЈ[yȵΝѸã0ʄԍŗ˲ϺƐҔΐпĴŗYң',
                    'description': 'ǎÖÜԑȅЙь\x98эƠόƧńÜЍзÜτӪɽǒђΈҰgųʧ˨ʗƞ',
                    'default_value': 'ȤΫӌİҳԛɧͱŇвãaΡ\xa0ȯɂƹбĔѝθѾŕLҞƌҏ˜ǻɖ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '6Â҇',

            'target_id': 'ɡȶĥӷԨ',

            'parameters': [
            ],

        },
    ),
]


class HotkeyFiredEventTest(unittest.TestCase):
    """
    Tests for HotkeyFiredEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in HOTKEY_FIRED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.HotkeyFiredEvent.parse_data(test_data)
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
        for test_name, test_data in HOTKEY_FIRED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.HotkeyFiredEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


HOTKEY_FIRED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='event', name='HotkeyFiredEvent'),
            ),

        ),
    ),

]


HOTKEY_FIRED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'event': {
                'target_id': 'ɜgϩżɅ\u038b1Ȕ{ęВƞήÅψЁж`ƺ\x8aԧǋԌҞůÅӜϩʭʭ',
                'parameters': [
                    {
                            'key': 'Ĕĺϒϫ',
                            'value': 'ʵŬԬțĴѠӠǚÚȱԫÆïɉˈûͽ;\x86ȞѽğͳͳϵÇ8ҪϔΠ',
                        },
                    {
                            'key': '\x81\x9eӪŒŰҁ˄Ⱥ5ɠΝҟƫҵŲʹȝϯфɲ¦ρђʫʊʵĔ´ſɸ',
                            'value': 'ǟːϞɨıĳfѱҚВѓɸŚяśŇïǦIɹО҅ĲǉʞЖʈԙʼϦ',
                        },
                    {
                            'key': 'Ƃ˸ÙїҩgĎΛ˭[ÃԝӖÅ®џĘӅ\x89ɋÇнďȭɎͽϦξ\x82Ý',
                            'value': 'ȇʬÒҴźŰȏ\u038b\x93\x9dҿ£ҫǩӣÆUҤʪЯӕƇʍφӋΰˀňȘÅ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'event': {
                'target_id': '[\u0382;ˈʲ',
                'parameters': [
                ],
            },

        },
    ),
]


class BoundHotkeyTest(unittest.TestCase):
    """
    Tests for BoundHotkey
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BOUND_HOTKEY_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundHotkey.parse_data(test_data)
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
        for test_name, test_data in BOUND_HOTKEY_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundHotkey.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


BOUND_HOTKEY_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='keys', name='BoundHotkey'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='event', name='BoundHotkey'),
            ),

        ),
    ),

]


BOUND_HOTKEY_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'keys': [
                '˰ѫӐLґĉǺΦŷʷԌnђϛŹ˪ɽΉΪɍŭ˱',
                'ΡÊ\x96',
                'ǐ˲ɄĽĹɋԗӾ',
                'ɍ¢',
                'ǯŢʦ',
                'ĂϯbͲЌµ',
                'Ĝʂǯ\x8dʚΛ"βҟĳғӕ\x8dˆȥȈЫ;ѰK',
                'ҙƅοĕϯqэŗҳɰŻη',
                'ÌǔʬѲȠȷť',
                'ǭϗλӘǞʘ҈ǖE\u0380ш˰ȵȑKǫȂșұԐəђ',
            ],
            'event': {
                'target_id': 'ʘNAͷ ЪҘɎűʅǖԭȉǞđ;ΥºƾΚȽț\x86ʛЖÕɠɱlɁ',
                'parameters': [
                    {
                            'key': '˝Č\x8cʕ҉үĲƿƢϠшŽǂƘșƗѴǯɒԑ˻ҭXÿȠʳˠńԄˏ',
                            'value': 'ʟɿ˖қǦɶЙƌпʆѕĖγüϕѷțе*ȴӪӼȫКÔǼʖQԫȇ',
                        },
                    {
                            'key': 'πѝʉFθ%ǔLì\u0382ȇŜØІ˶ЎΝȔƁԭЦӳ\x9fƛΕӧʮѰЗϣ',
                            'value': 'AÅηҎά\x93ǝЉ.ԟőԙɱCӈФԅʬ҈ӭӈˉÀͳΥĳãŉʫb',
                        },
                    {
                            'key': 'Ќҩą~ώûǢȠĎƏǵȿ',
                            'value': 'ŋћҢӅɰ҄ǒɎҩ\x86ˮêQǣʑ%ө˂\u038dƞͲϑŞĕϠӮʕƋЂƊ',
                        },
                    {
                            'key': 'ȯ şȬћÄțƛŊѰΒѵЪͷ"ÿӔҘϷŨΞȃФÎƮӐϿÃӾ',
                            'value': 'Ȁј-ϢԩīɶͶŋːɏȱƴĕњʶӞʉɺÕкƵЊ˃ɱ[d@Ȝ˙',
                        },
                    {
                            'key': "ВǵҵжűÉƮҙșPţǴƁϲǾŀ\x9būƵҰϨƽ'ƗŔƆâƨ",
                            'value': 'ƿźӎǤWȧΚѠԉϮԨFѦɲSˮFԫȚWʠȜ×Р¤Ȼҹ˓ѶƬ',
                        },
                    {
                            'key': 'Ӵʂ`ԓìt˛лķëϲӁ˝ƗӎР',
                            'value': 'ʊΎϴâį\u038dǤϒӆŘk\x9bŜɝΤԚ"Ǯ`ѥҐ\u0383\u038dɰǰӃіԄϜҺ',
                        },
                    {
                            'key': 'ũͷπȻ¸ĆӝԃɃ\x88«ʋˤȢËξωǂЬѶɟɕíǘԖE˟űΤí',
                            'value': 'ÓɶĵҰưҞԀȽɺНeӄ5ƚЄӤ\x90ӉŹϽԮʶ\x83ņϚ˕ӦȸҖɓ',
                        },
                    {
                            'key': '¤əӻӢ\x7f',
                            'value': 'ӹè˭ƕǅ\u038dɎŊӿįũɼȖΓȮʗƥΫé\x9aſеǀĹԍ˧ɀϜԊų',
                        },
                    {
                            'key': 'єϸҷƘɨϸęƶζщĭϊƪΏŕ´ɧĴǆУ˩\x92КƻĽǍýɾƇ8',
                            'value': 'ÖÙǍϑƫɄ·ԙСȡӅûятɲƯҪİĜϵȐĄçξȵśюǋ0Χ',
                        },
                    {
                            'key': 'Ϥ˧ӥϻ\x98ʠǗǘɽ˻ǇʔδќԝɾӷċέʹəѮȴƊ´ĻЂ\x89ƕί',
                            'value': 'Ş˶Ѓzӝ˰áŲŷɆQɹ˘˜ȮĶΊĲɮњˡ˵ďϚӋϠϖƱȶǑ',
                        },
                ],
            },
            'comment': 'Ɍ4ƅēǫԠĴϯěАAǳ˾ӏÈō͵\x87ѫ¸Ŷӽ\x95ԆΜͶ(Ȭуƈ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ѩ',
            ],

            'event': {
                'target_id': 'ʟȇȘїȪ',
                'parameters': [
                ],
            },

        },
    ),
]


class BoundKeysStateTest(unittest.TestCase):
    """
    Tests for BoundKeysState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BOUND_KEYS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeysState.parse_data(test_data)
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
        for test_name, test_data in BOUND_KEYS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.BoundKeysState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


BOUND_KEYS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='sequence_type', name='BoundKeysState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='master_sequence', name='BoundKeysState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='bindings', name='BoundKeysState'),
            ),

        ),
    ),

]


BOUND_KEYS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'sequence_type': 'meta',
            'master_sequence': [
                'ĵ˪҃Ǌҫ}ǼƬʨɕĦΎхƢ¡ƮˀȧøСȥΑ˶ˌ',
                'Ø·ԭmı×¦ȿҩ\u0380ƖɗÝ˛ѪӾт\x8aǒӌ',
                'ΓΦϔԊlЧƯɫңǼԤϑԜyɧҶʱəҨSԒЍӬȍʽН',
            ],
            'bindings': [
                {
                    'keys': [
                            '˞ÄԕӎϲʶúʍůӀÓĕĴ˝ÚŢ\x87ɵ[ȂΣԂƐɉȽ\x8eφƄЩ',
                            'ȨǮȷѻͼβ˔ψFΏԥȵÒǔɚάÁѨ2ԛț',
                            '˦ЭҳςмkϐǢβΆ˯\u038bӃӂЧ´¶әƖƚɕ',
                            'ӥĭ\x9cΡʂHӄʛԤΛÅԏ˨',
                            'ΏœʊѳƝˉBæ<ĮžͼǕɗѭ',
                            'ʖ±ȡ\x94ƎΪ_|ǹ˺Ͷ',
                        ],
                    'event': {
                            'target_id': ' ǋŌԆĿԙӲƨöҼƵŝļѢ\x89ŤԅӁčҹϥƃѸϝƦțˮȷ\x7f\u0381',
                            'parameters': [
                                        {
                                                        'key': 'ӔĲԓΨϲƺȴЇìØˌ?Ńѵт',
                                                        'value': 'Ɋτ·ŋŸÿӠϳӜƑ˳ÑƓ\x84ԆȪ\x95ȭԢбˎǜОǪΠƒуƩαɛ',
                                                    },
                                        {
                                                        'key': '\\Υ',
                                                        'value': 'vóԂˤӉԔǐǸԙ˶ӝÆŊƷЭρǲlϊIɈҍƜхā¾ˤȴŧɥ',
                                                    },
                                        {
                                                        'key': 'ĥѿ6ΙԦŇҩҸ>¬EǨʕ˭ҖžӀі˴M˙·ʃϞ¨ĻzǴËА',
                                                        'value': '£ԁƶʇ¸˾ЩΝJĢΆ\x91Л҆.ѱҨŋĕǛОЧħȍӜǭ(ԩ˼L',
                                                    },
                                        {
                                                        'key': 'ΒțYǏύӈЁÆūӖȥӐÍ\u0380ƨɅ_њϬӮǽӠԄˉΪΰͷűŕӱ',
                                                        'value': 'ЎȬΒϴԩŎÈáɑǚӐ˱ѽúӻÖГΛʛðˇĻӿBѬŋ©ǩӉe',
                                                    },
                                        {
                                                        'key': 'WÄˑԐǙΕ\x86ÕƆѕ\x87¸ʇş˄ĻæƲŢӮ˦ǳɠԪ˦>ѪȻξɁ',
                                                        'value': 'ɑДȜʖǡɈǼkЊˁƧȈǨ´GϔϒɾӸǮîϔЉĮȧβȘĈ˜ψ',
                                                    },
                                        {
                                                        'key': 'ӫԒʑӇ\xad±ƭːЫRɒć˒ϝКǠӲűĶѓʠɯƂɹȈЍѺȍĦŭ',
                                                        'value': '@ȫďĦχŶ/ЅʋʃǺʹʝÏ.ӊԀͿ7ӊšιİʸƅƃȐʹϦӫ',
                                                    },
                                        {
                                                        'key': 'Ȳ$Ǧ¿ĻïԂ҆ǉèʄΠaлӍɾ,˼ȆΨЧÉ',
                                                        'value': 'ɼЇƻťσԑżɥϽɄʞφζƫ˖ɪƕ˚ ÝʮԡӶА˾ȐϬɟɎί',
                                                    },
                                        {
                                                        'key': 'ϻϖϛȈԙžҎвȯҁΗӴρ}ȴȗƥ¥Iʠ,Ð\x86úUŗĴү\x82Ѹ',
                                                        'value': '˕З\x87ĊƦ+ƴŹƁ$ԓŀˡʭηǋѶԫɢʋřИξòΡӶ҂ЂƙɄ',
                                                    },
                                        {
                                                        'key': 'ўÖǛ˙İ\x89īƶɣśPĎ\x88˩ʀѝʻǿζ7і\u0382gãÅʼԉәŋǇ',
                                                        'value': 'ϖ\x92ɬόі˛ͶÅΪȼIѠрǽΠҧЋţ¯Ĳʐ\x96ͷʆƴĪӳѬώo',
                                                    },
                                        {
                                                        'key': 'ʛ˹Ój\x96\x82ʾӠѽǜԂʱӟžÀUĬ\x8eЊҲҞsʩϐЧ8ÀÐļȶ',
                                                        'value': 'ŜÝԭɬЋ_ŻΉʢˮ<ÁӥЃӟƄҶŽәӝłˬԐɦО\x8cϟţ\x8cҏ',
                                                    },
                                    ],
                        },
                    'comment': 'ŰyΆɁθӣŐːĀȏεřҵƸѷȟĖyÆˇĤʨ\u0382ӄţ˛aɆĩ\x90',
                },
                {
                    'keys': [
                            'әȿ\xadЖƗáзƇƗ',
                            'Њɀ΄ĸЩӊɮϯɇɾψƗçѴj˱ӹɕăȂΥМԗБȃʺ',
                            'ΣԑԙƔȱµ˟џԏɳθÈӷF',
                            'ƩԄzĠŹ½ͶҶҧɪѕ@ˆɮĸȣɵ˾',
                            'ȭѨʌϭ˒ƕѱ',
                            'ν¯ĻTі͵ɒuĈ\x81\x864Ĕěҿƿ',
                            'ˋˆοкӥˍȪЬк\x83šŶӄŎϹ',
                            'Ě)Ф,Ø+Ʊ >ɆǤҩɿч˲hӕ',
                            'ɥΪŵ\x88Х\x9cɡҮǞӂŢϕ\x9eʴюεԚвҵzҬǵėŹ',
                            'ӤǋÀ˯ˣўDӓΑ΅ҨĕӚ',
                        ],
                    'event': {
                            'target_id': 'әʝˌČ:Αxд҄3ΜĳËŌˉõ·ŚȘZ\x90ӆɣĜ˩ȏӘŊƑϾ',
                            'parameters': [
                                        {
                                                        'key': 'wŢĬΥȩʳЯΣҙűʉшȭ§żωһȵɢǫȶɮ˔+ЁȨӔȑ%λ',
                                                        'value': 'ƬһƴԨ¤\u0379иӻӏеɟєǬϼӀТԡͿɫ҃ƖӴ˅ǵҚЊ6rԤʱ',
                                                    },
                                        {
                                                        'key': 'ҰӖӹУМʅɿǊǊĢŅүǳϠρ˥kľӶ\u03a2ţhE\x8a=ѭǅѪ',
                                                        'value': 'ůѲϡԂǮϥ˪Ώǈ˙ӕԍоŶаӄϯϫҊƱŶp\x81\u0381ҡũӊҀɠК',
                                                    },
                                        {
                                                        'key': 'Ǌåƍŧ',
                                                        'value': '˔ʰÝķ·ā͵ǁуаӝŜÑʖͺ\x9aƿʓñzɺǚѹƤ¹\u0380ƞҕɼ΅',
                                                    },
                                        {
                                                        'key': '\u0378ΡĩƱƛōϽӬЊӥŕĝхȎӬŵӽ˯нƾˎщϘѤŜѤƱ˦Īζ',
                                                        'value': 'ʕνвǤāϣȍ˰ҷƒɿΨ]ʷԐū\x8aгП´ҭɺOжƨѧХÍ¸Ш',
                                                    },
                                        {
                                                        'key': 'ʵɔғ˽ԞЇń\x9aӬʼӧȡϣШґʚ',
                                                        'value': 'ΧȻÙXӧҦαȣѫʚĭҗ+ĦƠѿȉȺςͽŤǰǼǭɯӟўќǏС',
                                                    },
                                        {
                                                        'key': 'ӱЄ&ԧʒƸɆЅȉ˧Νʩҳę½ĂǿЉԚ¤:ˮ',
                                                        'value': 'ƿɌ)ź»ɡčÅψɄäΑґæʷƁ¦ʧГѼ˧\u038b_˳ɶǈÂăˁZ',
                                                    },
                                        {
                                                        'key': 'рЩ\x94сǹIӵŸȪüBђʿMǋɄљџΨϬϙӡӵʧǞ>Ȏҫʪ\x9c',
                                                        'value': 'āԔ˂ȸπ\x84ϯǋз¾ŘɭҘ\x8bɟá_\x91ƝŸΚjљСL˕ȒđҔʈ',
                                                    },
                                        {
                                                        'key': 'Ј\x96ƥRƊɶіДǻВэɑñ¶ķӉόŸͰӒǳŎԍ©˽ǧƈɦǻҍ',
                                                        'value': 'ҵŝĖƦΤьʈϞӕʕԢľӂxNʷżԀϢҵǒӊų³ԌϧȾѡҬͿ',
                                                    },
                                        {
                                                        'key': 'Ԅ~ΰʴѷAѫÞΈ¶ӘѰ_üǻȾùϛʣƒɇϸθѐҚѢǽҸǛ˂',
                                                        'value': 'ʻϜÜŢɬђңͺŧ\u038bϢξ˅ʩÝàƑ§ŶĒ{Ţ\x92γȣʖȡԆşЕ',
                                                    },
                                        {
                                                        'key': "˔xɇүХϗʮҹћȪʂȸƺάѼ'ҩl(ʤЋĉЧŗЀΨȪɮʩʵ",
                                                        'value': 'ӔĿÀʯſˋȬӾӿʧ·Ƙō˖ǈɬңĵ~϶öίԊϯŐ˛ǓwʛӦ',
                                                    },
                                    ],
                        },
                    'comment': '\x99UƀɎĪöύΒƣɧʧԐɆТѺΩ¦҂ËǗӵöŠΫɬϵŚɃȋē',
                },
                {
                    'keys': [
                            'ƙԙЛʯ',
                            'ƥӮɥʩƯҜʁȈЍɓ˂ȿγΪɅĤƲĥӊƦĸˀŗԍΚĕə',
                            'űҿŐӏӓËͲ\x8aˌѝΫXŶҮΠYғ',
                            'ȆȴˉáəÐͼʼɜƫ',
                            'ǴɞʊԜьwԧЫʰɑɪӱʅĘˌҲԈǀǓ3ҵ',
                        ],
                    'event': {
                            'target_id': 'dƻƲ·ʵҒӓѳȈ҃Ƶ®ВӉŴʋʠҸĺϔÚèſǸƟӌȢǝĦɏ',
                            'parameters': [
                                        {
                                                        'key': 'ԗӟëΣũȋâƈſ?ҬΫ÷!\x88\x86ЌϰѴɣĵBƒȌґĢаʮăӫ',
                                                        'value': "΅Á'ÅǍ]ľ2Ӣl\x9c·ӐʁȱR¾\x82>«ԊğҦ¯«ȫÞ˱ˀо",
                                                    },
                                        {
                                                        'key': 'ϮΪǩζEƬȤϷˢǊɔZΰΫŉƝԃʦˌҩ3ӚҒɪžӤЂҲϰF',
                                                        'value': '1ɗĨķōеϗæđɚĸwԓжȫϊѧÔҩŷԌɯӫũmĈbåéĻ',
                                                    },
                                        {
                                                        'key': "\xadҫˬҥÂõƮіѢӶԎɷʥ~ө'ĚɹʧӉЅ®ϡYϥƔСџǟ]",
                                                        'value': 'Ԅū҄Ķbƕш˛ҋ҃Ѣġ¿{Ōǔ¬ʋɿϞ¥γöğӿѼĚҫĺѹ',
                                                    },
                                        {
                                                        'key': 'Ĳӿsʛª[pϯԑеѦX\x96϶пÞϦǜʌ²ǬбŶ\u0383ə·ɘǢқϑ',
                                                        'value': 'Ζ˄ǽͳʞŲВȗƇȏԇȫìrͶɩȥºҬɂƬǿϝ;ƲŒʲÂӆ\x9e',
                                                    },
                                        {
                                                        'key': 'ϱЍÑ\x9e\x87Ԓ\x8bɘªҿĺM˶ω[ž¢ϋTғж΅ƞǺˠʇϢǊɰ˛',
                                                        'value': 'zƕɐǣʿˎέŭӫϾѩŠ\x91ŕϝƓ\x9c|ȎȯψǑ˼ʻҷVʒμћĐ',
                                                    },
                                    ],
                        },
                    'comment': 'ʠɢǛϥѻρиʧϮζǫȁƫȰɕ_ĝ¹ɣҤÐһɵǕъѻνΪԜƸ',
                },
                {
                    'keys': [
                            'ԃɁÐÒ>¬/ԎоёҰŐɄӈŮσˑ\x90ǻ˙Қ^',
                            'ΦͰȒϯ\x85ԡʟҴÏɮ˶Ûų˘Δ',
                            'š¶ʴҭэгЗdӕ0ŃŝμǶҙ',
                            'ȌԬȡÉѢΟ\x7fȢŤӣҀɝ˜+òͼʬΝΈɰĤ',
                            'Ňѣ?ǐәĦÆǝ˰ҠɾҼß ĹHÐӠ˱ćƒŀԣҐӕWm',
                            '4ѭ˜ʅǜΣ˙ƋùƉ',
                            'υIzӵ5ƍˆâ',
                            'Ǹ\x92ͽӖƗIЮȉҳ´ϙƪτϝěɛϛƁѢâō',
                            'ƈǹ',
                            'Ӓtà',
                        ],
                    'event': {
                            'target_id': 'dɷȴѱҙȵ˖L҆FԓƗȥˉϛЪʯǛĻ\x82āȲƅǼƚȾƍ\x82ҁx',
                            'parameters': [
                                        {
                                                        'key': 'ʞ\\ϬŃŭĿƯФѵӁгǐ$ļӬћѲʁһ˗Ӡ©ŔɈϣӣГ\x80S\x98',
                                                        'value': 'ңΩȯǷǼҏǩǟάƁǐɱо˱śЯ\u0379ĹώÙțϻuԤȗłȇҟ¤Ӂ',
                                                    },
                                        {
                                                        'key': 'Ąʨ˒āť˟Ю˱ӗ˼ß«Ы©ƩўȔƠ±Ȑi#ВÍˆ϶άʉɄɛ',
                                                        'value': 'ӡǔ˸Θ˖Įˏ\x9cż¦/¹ōŷœɑɥϳΥȬ˝ԌԑϚмЅƦğҙѰ',
                                                    },
                                        {
                                                        'key': 'ńүȝɨʓˤϹ\x9eӸćġɘ!εą˟ʼ\x95ԇζƻĝԒоʋʶŒëɁҜ',
                                                        'value': 'ѬȊɒȾƊ\x90ӪˌӄʈҳɆˆθǹӀ҄ȭϔϤЏâʟѬиΟζʡρÖ',
                                                    },
                                        {
                                                        'key': 'éѨѺƱЮԝϨéѺRҿ¶Ρ~ʑҪӝΙԜȈtϏȗĺ',
                                                        'value': 'ʺȘź˦ĹȪǿʶtѳ¡ʌϽXХăµɽĠɄԦƓĩɉ\x8d҂ҸԄѐ`',
                                                    },
                                        {
                                                        'key': '˕ѬԋŰďӦɹӼѹѐϨԙɠЪŊЈǋæƖɥġVʱΰɿʭ»Y\x91ҷ',
                                                        'value': 'ӺҗΓȤˤĥԧ#ӔÁ˙àϐҀǸӅ˰˱иҽ\x98àκӪǠ\u0380ęГσĿ',
                                                    },
                                        {
                                                        'key': '`ӁРӚҎƋԚѶȅҽϒϻТў\x8dʗƵ\x8cäɂʡ|ǘȭƬŒΤξŷɥ',
                                                        'value': 'ƫƤΚΘӛҾʪҴңӔñ\x80Ɉ!˨ѫȱԂţԧ˯ìӘǜϟǯū\x84ȧɶ',
                                                    },
                                        {
                                                        'key': '҇ĝʪɲȰģšєχ\x9dӹӡԈ\x9fԚVѿˬ~Ӊ˅áӘƝрƧɣȃ\u03a2ƪ',
                                                        'value': 'ËFЅЯӭöşόŇƑĞƐSȎˌѣкѱӗȆǗθňҘњ§љΣ҂Ʀ',
                                                    },
                                        {
                                                        'key': 'ϰû\x9faǍFƳ˶ΦĐʭϾ˶Ò˪˨Љș˳фϐʠ·ÿɝ6ӯͿȃʱ',
                                                        'value': 'ǬĞÁ)ŔùԫөιԤȌӆУӠϊӵʘʧƝ%ҏɽìƞĲӑʌ\u0378ʱЕ',
                                                    },
                                        {
                                                        'key': 'Ϛŷŀ',
                                                        'value': 'Óŵ\x80įҊрʤįɣ҆ǴːƖєп¼^ĊԧÇҫΐrҵƶˮǷǟӴӡ',
                                                    },
                                        {
                                                        'key': 'ņɈмԉɡΨӖϰӠ]ҳȃtШȯɆǰǦĐE\x84ŚњɄэȚz\x8b\x8dȼ',
                                                        'value': 'ҪċcˋΟʕѤÊǔԞԈĀφˀԥƀԄćȯ˫˹ӗŢČΞßԨ\x87ˎφ',
                                                    },
                                    ],
                        },
                    'comment': 'ǋӜų¯lσφ¦їԟåȵˋ$đҸљrµҏԔйǩԂԍð˽ӊĝƎ',
                },
                {
                    'keys': [
                            'å˹ԞЄ˰Ѝѕ',
                            'ѷԠnʰ!ďӚʈɮÀ',
                            'Ͽ\x8eʿɹԞɦƁ',
                            'ЮʁˆƲļӥȼԖcУƵȾƱßɇkЀǀ¬ǚѬҢм',
                            'ɒφҬŦƒÝɱ6ǟ˸',
                            'ˀҏѕ˾қԥ²ȷ\x95dϓҊíнǽ´',
                            '3ʢưǲ\x94ɨīӆǂӑŞƫǛʑzиӳɢɍъ',
                            ' ʗŷ?χҡҬ.Ǭ˓ǎ\x9bƯЌűØйԖǀŒ˧',
                            'ȲΞ',
                            'ł\x91ɔ\u0378ʃЯ',
                        ],
                    'event': {
                            'target_id': 'ШΓ+ȊҡԠѝɖĹ;ÅɋſTϜ˥ɀÑǽɇΓϬƤџ˩ӷϖȘƽŰ',
                            'parameters': [
                                        {
                                                        'key': 'Aҙ΄tÞϚҟ˖ĖԑɜĶǦӌΒ\x97ԂʦńӽϒĆOжłΈǩϲƂĤ',
                                                        'value': 'n\x9b\x96ϩńԈʣŲõ"ÃӒ͵ʠʦƉӔ´ЍԉȲǭɯʇżʠ7тĬɛ',
                                                    },
                                        {
                                                        'key': '¾ʘюəĂԅ\x9cґˠbƯyĿҪ\xadeˡϼPˮ_ҀłŨʡԮΰζĝā',
                                                        'value': 'țǔ˃ͰψдҴĎԬɁ\u0380ƹԗɁɃ˥εӬУǝ˭ѮȢĦ\x98іǬԍʆӑ',
                                                    },
                                        {
                                                        'key': 'ԧ"ʘŴƵð҂ʧ\x8fźΦ˳ήί(ʣ\x91Ŷʬ\u03a2ǫϐӎ>ƁЅõƤĕȰ',
                                                        'value': 'ԥAǎѣŰºǼʧɻ\u038bϭҦΉϞԫǇɌŕҋӄˇɻ~\x8cģҗĦēҥơ',
                                                    },
                                        {
                                                        'key': 'ѓŶɔȭɸϘξӘɻǮγǝȻɸǚʌ',
                                                        'value': 'ϩǃΦѤҒƩ0ī&ϊ˯\x9eɾʩϋˎτȁȅ&\u0379ſҢҁͼβϟɈļш',
                                                    },
                                        {
                                                        'key': 'ǮӕŧɆÇЙÌϚǀƒ%˪ϞҽѫΑȋ˚ԙĒ˚ȚșϥϜϟԅзӅǷ',
                                                        'value': "ҹʉ'ŭ{ҫ-ϋύ\x82ԨþƠfqɁӤЗνɼȪЃWҘφ®˻;ȼӕ",
                                                    },
                                        {
                                                        'key': 'Ŀ˂ɛŭΆ"<θū*˯ĽʻƅҶӈʙǭԮҙΉˮÚЍøƙɺĂЭǤ',
                                                        'value': 'ԭŝqɸˌϋҾӮȆтзŏĥVġƜȁȤϠ>ĒǑг}σԐØ\x82Ƽɗ',
                                                    },
                                        {
                                                        'key': 'ĈȤƢψͷǵéǴΎͶ:ȧ',
                                                        'value': 'ŴɴӐˈʷΗЌ#Мȯ΄ԜȉǹǘѡöˈҟĢŶұəΠƚŘϓəҏË',
                                                    },
                                        {
                                                        'key': 'Ș\x9eǫщӿŗʂЅŐċsӧѬҺƃŐώęǬӃτď¤ƖҌѷʬӹіĄ',
                                                        'value': 'ӳӳɐĀƋûĽѿѐѰƟω\x9eɽͼíҺ͵Ҙ\x8cҴȍΧϜĆҪ\x88ЫњҀ',
                                                    },
                                        {
                                                        'key': 'δʜҷƑǞxýχӫƠҼӱÏȦʆШɦ˰8ĤȍŁѴɀǖž¼ҪӘω',
                                                        'value': 'ŠѤĉ¶ƑѬ¼ϳԡȾȆΫÕbӓ˓ҶʅƦёŵāǗ˛ĊҀȑ\x81˩Ѥ',
                                                    },
                                        {
                                                        'key': '˼ëтћɏӐƣЮԄɭӱĕӪҲƱʤǳЀϣԗ˩ʒƤĽȏΖSйҀǾ',
                                                        'value': '~ԡ¢˒:ʵɗҪŁ\x9d*ϙјə\x98ÖɮE=ѭƻ}˨yҾѦşǲЌǆ',
                                                    },
                                    ],
                        },
                    'comment': 'α҃ΚȨǒźƁ±HĞѨåȲӷ\x84ɵӖ҆ӳ"ƐЪșŜŰȪĳŗӊǱ',
                },
                {
                    'keys': [
                            'ӷͿØ',
                            'Ǔã°ϲӔˬhċ/҃ǇϬт˧ӸŽ˴áɧįїÎюàӴFϔƒӜ',
                            '˚\x82лWƅ',
                            'ɳнGОƗʯÔϿə\x93ĳzķɨҵPʹĹӛΗɃϔƕťїӈХBϸ',
                            'ɱи®ƒɍůȩ[ЧŗϲΘ',
                            'ǣʶŐĤͼ',
                            'Ƕ\x88ˢLςȈȢ4³ѡЅѦ˶éҲɽrł˭Ë\x94ӔӸ¥ȥɼѤ',
                            '\u0382ĭƆϫԀҲΒ',
                            'ġѺ\u0379ΕθҨ8ș)ƳŽ.',
                            ']Ŀҟ.Ϲ',
                        ],
                    'event': {
                            'target_id': 'κµåʶľƐÈϰԏԢſ\x9cΜäʤӲϟlƍĬɭӘ˦ԒοϭӍò˧5',
                            'parameters': [
                                        {
                                                        'key': 'ǃǩǨʆɊäϿ҇',
                                                        'value': '҄ѕ?ϤƵĈҌƮ҅҃Ё ȵ\x87ɟÉϜʨ\x96рóĚіȲ|ԫźŃʝϫ',
                                                    },
                                        {
                                                        'key': 'єԔνÏÊѲȘӉUƄɜ\x94ĢƦŒϲǔΕωɹˇҫƩԋTЦĠɜщ\x9d',
                                                        'value': 'МQßÈúȀѷʥ\x9fˮɽəщ\x8aϗƉθʧԋˤѐGԓ˝ѳ\x90ʗΌ\u0378ˡ',
                                                    },
                                        {
                                                        'key': 'њȜ,ƏԘȰʴe˅ʝԫѹ˩ȚɔѵŎԇ˓ӐΝƅŧǭȉǼȖӻöq',
                                                        'value': 'ǖϋРĜȺΧ&ӿԜˆˈΦϸȠɍͷǠǪɾÝțȕҷ|ӾȶÞɏТ+',
                                                    },
                                        {
                                                        'key': 'Τѓ£ǲѾȔïεŏ\u0382ѪǮşă˗ʅѳϧ˷ɲԌďƱӑӠˡюȶϖĤ',
                                                        'value': 'ϑГҤ҇ȎȲw˅¬ΧĝCĹЫï¿µːţıȀЪЮΔχǢ(ĽƈԦ',
                                                    },
                                        {
                                                        'key': 'ʴɻƜфǍǽϒю',
                                                        'value': 'бǰ˝ĀǾLáˀʎġʿđ9Ţνű˳Ҕî¥ϢҕԨҫÙԃ˕Åʰ¨',
                                                    },
                                        {
                                                        'key': "Ʋϯ\x95UŮҹӝхɆ҆Åʇǀȵ'sƍΘїͷƍӂӽȨˤŦΠ&ıϦ",
                                                        'value': '˟ȺùȚǽʱí͵ɡŽ¢ǳ1ωΤΧʧɝԤŋѺȋŗΆԟϤġ\xad\x81Q',
                                                    },
                                        {
                                                        'key': '˸Æ*\x92ǋϲӷʡʢʎ˾',
                                                        'value': 'Éɡźt,òП϶ԞŁϬʌμӼ˲ɥ˰ǇчΉΫȀʧǧǑθҿҔϻʕ',
                                                    },
                                        {
                                                        'key': "÷ΫԡĜΗԧȎΏ'Ã˪āјԀʚŴʥÃˆͽě˭VӳΡǥKȵѺ?",
                                                        'value': 'ơӆľҿɵӹқЂРҦƾǫŊĥѵ\x96ҷŁtſǚƛӤͶ®ʛˠ˙ԟК',
                                                    },
                                        {
                                                        'key': "vӒ'ɐÙêџ`ԣdξ;ŭʿЍɣ˅Ҡȵԙ\u0381¹Ɩɨȇ˷ӭ˻вǵ",
                                                        'value': 'ǶǯčӃŐӿӖіɔЗɢőȊeƘԥԬȤӸǪK¥\x9bԘΌƾȊΒѶЉ',
                                                    },
                                        {
                                                        'key': 'æЮЄʊȿ·Ɏ˲ϐŲӥӝ»òЦÕȫлʱяʯҳƈϱΪNѨÿȵд',
                                                        'value': 'ςγϓˠʷʃʶǂǗƢ˻Ίɲā«øǦԁĳҲё/ˌƿ0ʉԧВňϓ',
                                                    },
                                    ],
                        },
                    'comment': 'ФNțҌĕѡФϏ\u03a2КϾ®ƨϏԌԀкшɈʱȖЅɱ\x89ɀĦɾɒЎ˼',
                },
                {
                    'keys': [
                            'üĻĸӕν˺ɝɟӪ˟ˀӃ\u0378Ӳ',
                            'ɠϱŅ·ƅJҎĳ?ǰҽǸɓĂɏҎëú˴',
                            'ѯ',
                            'Ň҈ϢĘžèѺ\x85ɺ',
                            'ǖȡʡÿѠVіӨΠʩπȺà\u0381aɏȢҖϾɄɟňʯгпȚȁͺ',
                            'ƻҭ\x85Ͳ<',
                            'ѵѕƬʚКрΘҪƍƾƧˋʀʓԫ',
                            'ƺϢ(РŬҧĳˊ',
                            '\x96dҾǛŸ͵\\ƔĜΙȲƺѪhˏИѪєҰ',
                            'ɉ˖ҭӛÞғфӫƯEʜԞɟ˸ρ\x98Ŧȩφaɓ,ηǿ',
                        ],
                    'event': {
                            'target_id': 'ѶƪķǢİɢǵϤЀƢӬʴļuŰѲˢκϓ\xadϡŌʽ;ˬԒīʆÝͽ',
                            'parameters': [
                                        {
                                                        'key': 'ƁʬǺƸˬʶҡłŶƔӖ$ңѡʷħǜőʴ\x83ӛίEÁһѴ5ȆŪ˴',
                                                        'value': 'ʼԢΦϭʺǞʄϙʿӦʓЉҩ6Ҍ\\˰ЯƵƶȻşǋ\x85ŭϵǀЀʂė',
                                                    },
                                        {
                                                        'key': "ӆɞȌřϭΛøԤÃIήȤĮɭӠ'ɰϑ҄ɓԋLϔÂ¾ġҐщ",
                                                        'value': 'ɻ҅ԙѧωЪ\x80ĐʾǇѻǴ¼ȇʯˬȂҖѧķŇǎȅΐѣyŕӍԂɻ',
                                                    },
                                        {
                                                        'key': 'ĹhǷʓľʣʫʏʹsɳԪçșdǢǺ5ҠĀ\x95їԀ\xadϸĄƖέÁǯ',
                                                        'value': 'рʚîүƉɂѴǛɦҟǆ\x81ÛƄȎӟʖϷ˜»˅ƝҴқƉ\x93{ԘӉ\u0382',
                                                    },
                                        {
                                                        'key': 'ȸѩȷǲҐȉӀЬʥ%ȸêӗȹǙӮ©Ƥ1џ΅ûԅǐνЁƜƭӭǿ',
                                                        'value': 'Ąǖ҄Ǎϭ¨ҽƈGϢӴԖϞʹƞƠWЍ\xa0£°ɱ"û\u038b\\ш¤Ȫǋ',
                                                    },
                                        {
                                                        'key': 'ɜАƼ',
                                                        'value': 'ıʪWϐϗȧϛӁʟδΆψ&ɖĨͺʏřӑŜȽl҉5ǃƋ͵˾LȾ',
                                                    },
                                        {
                                                        'key': 'ŧǻăζÿёԈϊǤΨӟɡм\x9a´Ѯ\x81р:żƏ·ʧҒӘҍ\x98о˯l',
                                                        'value': '9ǏϚҍӪɼҠïpƓȃ;\u0382āǖԕϠtӥƆԜŋȣȇÑęҘȘĽŮ',
                                                    },
                                        {
                                                        'key': 'ʈĿĶεǪξɋѼqεʝϕĞїŇөҭΆŐДλҩǬĜÉҹқŊѝȹ',
                                                        'value': 'wЄʨԨȲƂӒȈϯԆ˛СFϊǖԧžѠӶУΐӥ$ȕϽłρï0Ȱ',
                                                    },
                                        {
                                                        'key': 'ʋHB˾Ϟļ˱μĦ˙ˡɦ4ԡ\x9eϘӗӷѭǊϼȤбĭ´ĈҊɪ˾ч',
                                                        'value': 'ùƲʻ±ʖҿ0˒ÜҢÖƤλÁΉ¶\x9aҠ\x8aяχʼƩΏџϧв\x9fԕά',
                                                    },
                                        {
                                                        'key': 'ЏăƮдŌΘ˺řʿңϽЧș«ŘҎ˗ɺġ\x81ɖŞǥˮςӫʮӤԛ¢',
                                                        'value': '\x8cДȸӜþ\x9aϩśӛʮЩ˵ǅĚŪ˜Ԃɩǿ-ŹЖӋΠɠɖʫ¬ɥʭ',
                                                    },
                                        {
                                                        'key': 'ƉȶҹЬӈԄеӭȸpåŒжԐ҂xӦҳƆɽѠȔyлɛ˚ɬ&W5',
                                                        'value': 'ЏƬʹƗƌ\x80ш˅ɄeƞɅʭȗÚϫӌπйɟŨĦ˃ЈâȢИ"Ϳӯ',
                                                    },
                                    ],
                        },
                    'comment': 'ҵÛȷЍЅƄƲϡ˖ϥΝ\x92f˅ŌҲ¯ǔÏʓ҄ƓμƀğœѐŠ˃¥',
                },
                {
                    'keys': [
                            'łǌ',
                            '϶ĽΫҺҚǼɡȊȑɗ˻\x91ƫǩ<ɈӃ\u03a2ɼӽτč',
                            'ı]ĵӶüƸ˂ѻ',
                            'ǜϡӰћԠƢѣŝнȕηҦιƵȧĬћ',
                            'ªԥ&ε',
                            './џдƴШİԝìϧѿîҝѮʛ6ģ',
                            'ǻó5\x86ŷRǀ\x9fƸͷ˛ҩЖȆēϊȳΫȭȮɲÛɄӫ˘ώ',
                            'ʟƓľ΅ʥԇ\x9bӴǪμŁÅǽǣԕÞίΚΝ',
                            'Б¬Бʷ,ϰҺϸ',
                            'ɳǺΡЖϡԑïʯŪŨÄ-\u0383ˀˁϝ',
                        ],
                    'event': {
                            'target_id': 'ȒɿԬτŠԔǂʃțʾЮӹ[ӤѷʎŜ\x96\u0379ȟʌӽʍĠ¼ɃŉǉӀʌ',
                            'parameters': [
                                        {
                                                        'key': 'ŰþУϜɎéȮ"Ǔgʔ5¦ӽʔтǴɻ£Ьҥ\x82ÅbŜΪκȻȶӷ',
                                                        'value': 'ЁĮrǾϷӜ×ÿɉzѫƮǝіҞԠêĝԧіʜʀϒȺ\x83ʀoіѹƲ',
                                                    },
                                        {
                                                        'key': '\x91өӯҭ\x7fȼ\u0383ʈόʼȷŎЎŽYĨӫǻˇҮɲ«ȴԃХǞ\u038dҹϪȹ',
                                                        'value': 'DӠЍă¨ԢΕѪǃÙ¢зƜƜčўЋ$ɘҞt¿Іƾ ӱȹЃȃ\x96',
                                                    },
                                        {
                                                        'key': 'ÅͱáĳĥԠŊ¾òȿ҆Wҭ',
                                                        'value': 'ȸdˍѲҖɾ\u0378ңǪʮʒΉˤөρ\x87ҳΊ¥ΨΣřǷԨˌMˣҖʰˇ',
                                                    },
                                        {
                                                        'key': 'ΠԗТМ\x92\x8dӚƦťư¨ğƪӹˠ¦Ӻҥȝԉѓɀϵ\x9aΩϟȜǏ˺Д',
                                                        'value': 'ӽԈʫɳǅƉñΧчϰ˫ǾЄұʎƩDПǛΖǄĝЛӕȓҠºŒтϊ',
                                                    },
                                        {
                                                        'key': '¡)ӨzҸ\x86fʻÞɦЛϣƳɽ3ŀĳĳŪӢψχ˪ĢΠŞ˲ԒхǏ',
                                                        'value': 'RƖ˰ʥѼӦчDɱ\\ҚƟŝƛ®ŭЯоѺȮʦĤϑĆ¨ъΩ"\x84\x8f',
                                                    },
                                        {
                                                        'key': 'ʾ',
                                                        'value': 'үӰŇĝȎ,ĞҰɎϝξѡvѮӋӆӡҭҰ]ӰϱǿĚʥӔ\x9cӄõͼ',
                                                    },
                                        {
                                                        'key': '˕ԎǚʈϾëԣTĥҰӘ{ҔΖǭjȵϠƇЇʣǷ\x98Ϟԁ˕ѲѼƾɲ',
                                                        'value': 'ԎβĻѪџҬǶ©˶Ĕ\x90ѲԔϊлԓȭѫĊɁΚwΜŵЀ\x94þʥʧȠ',
                                                    },
                                        {
                                                        'key': 'ϘȹăӁŏƝĢɱѽѣōˢżуɣʡŸИȜӭә\u0381\x8c?˲D\x99m\x83ϙ',
                                                        'value': 'ːŸØџtɲфӺɺǂϮǥ\u038dΖıŷȿΙƛˏ˔ǿɥΡЅÌԘʢwǋ',
                                                    },
                                        {
                                                        'key': 'ɃǔњǦƎɻ˙;ŷŅȿϸºÄӚЉОЛĪˉɧ®ʝ\x98UÚ\x8bѼҸƮ',
                                                        'value': 'uéäļĹƾˌѴӹßԢ?ӄĐƼXǫ҅-ĭɵƩʳԗʮ\x91Ģɍϔó',
                                                    },
                                        {
                                                        'key': 'źñʝъȺθӘŚʂĚΐU',
                                                        'value': 'ĞȁŽĭĶԏӹÛɹԍȍӥòѭÊЂŹ\x8eфͶːԂщјԢЎĮΥԨф',
                                                    },
                                    ],
                        },
                    'comment': "ǛϠӦǍƽҘΏσǒ\x91ïĀɋϽŭǋϒЭĩǉ'ѮBȨŎӥˑ¶ӯε",
                },
                {
                    'keys': [
                            'ӤϦŚ',
                            'ȯɼȞƽCΥƨлʒҺͶШ',
                            'ϛǢ¥',
                        ],
                    'event': {
                            'target_id': 'ʸʧ˼%ʟϯ΅Āʘίχ\x9aŵȅѰԐӍƾǇҬǸľԛǳϾďȭPɟӾ',
                            'parameters': [
                                        {
                                                        'key': '%Ūȳǐͼ|\u0383Єʾўϔԍ҃ͳ',
                                                        'value': 'İ˾Ţ\x82ļȍːHɆƧÊў\x9dиԔœ,ǉǯ¥ĖҲǇήҨƍ\x9e#˘Ų',
                                                    },
                                        {
                                                        'key': 'ԃƩǰÒŰȊя˥ʪĲǚʣІûӗԜϥôuӥɯԣʜˊϧЎѱѫňČ',
                                                        'value': 'шȁČ>ф±ΙԃŬɄnɄҷ\x93Ǻ>уƭΏҚ҇ʰȝǊ҈ʊҞԓћÓ',
                                                    },
                                        {
                                                        'key': 'ɧ;ǒ!ºͳϒ˗ӧҽȎŏȏêП\x9cɑōѵ)ϠÅЬҽϹùԎǆӮҥ',
                                                        'value': 'ҞɨЃU\x8cѩͰȳΞї\x96ЈԃɛϋИЋЁҭŨ9ԮѪӂǥʿͶlˎĕ',
                                                    },
                                        {
                                                        'key': 'ɥʾ\x8fƌыĊɸȓǃяƱņϕͱʱѹìϑλŖNÛԡEΏΞͱǾўұ',
                                                        'value': 'ѱԃΚĉѡϢІѼŉÇʈΠҌƹЏγ{ȓҹѧƺҊĒÐ΅ľ©ŉƃϖ',
                                                    },
                                        {
                                                        'key': 'ҜO\x8fǢԨұԙҕρƷ˱Ӳ˼\x98ȻΘˌŹҮčԙɕøKȤȀȞʜѶǕ',
                                                        'value': 'ɆŖƽϽńӾɚoͽӢ_ɜҨМɛԕˬήч҄ѬӆѼҘ˽ºţ˂ӣʓ',
                                                    },
                                        {
                                                        'key': 'čϊȏϺϛӈͱ\x99қǓЉҔƨΡxӀΐ0JҮŹ÷σyӫХОǀɳɎ',
                                                        'value': 'ˋʤӪĖáɿ-ÙηƗƠùкłʆɡçҷшʱϹȰǚƥϞ\x8cȶɁȶӿ',
                                                    },
                                        {
                                                        'key': 'ǃȢЌΔЖ\x8eûԈP{λΚ¼јрöйѸXEĞˊХÆͻхɨțҟP',
                                                        'value': 'ҨØϝ˨¸кϬɼƜ˘Ǔǫ\x93ŗӃӮУщǜͺΪĘĖũбҀɹĔ\x7f\x93',
                                                    },
                                        {
                                                        'key': 'ύ\x84Ɏӎû\xa0Ҽ\u0383ӟЩӞízϪӱõҊ˚ʾƜɚȢɎ<ŵśīКԪ˅',
                                                        'value': '\xa0įЭ}ƦˌЫşѾýŖ϶ˏHӧɤҋўҏȵÛxȦԘˆҽƆѐÜÈ',
                                                    },
                                    ],
                        },
                    'comment': 'ƁѥЙđѝҦҗηУ_һĈǸ8ƦϡѵʲȞÝϧϕȨҾþȌ!\x84ʻɠ',
                },
                {
                    'keys': [
                            'ЂØӧɳӑ\u0379Η҇ͽΆ˵ΝʜǲʱGŤ',
                        ],
                    'event': {
                            'target_id': 'ʴªʘȳʋ´\x85ҊƷυǓʶMǧЫSӒƶʙ҃ɌȍӖŃԝĘȖƶɷϹ',
                            'parameters': [
                                        {
                                                        'key': 'ƚй\xadүҐª˜҂ɶĕˑӀǰ\x9eуӟȹчɡжÕΒɤĕĬФϧҎʮҟ',
                                                        'value': 'ӹǀáΦԭX˨`ȌЕƆЦѻˑÄǡˮƉԠǟЯѧƓƬɘӄϷɐţΙ',
                                                    },
                                        {
                                                        'key': 'ФƶǌѨҎ\x9aϹEÅÿ\x9dΒεҵϫʄǪʵʱ\u0382ďєƯӿԎɶҳ˯Ƥɷ',
                                                        'value': 'ԢτǞɲěɕŚȉɀϰͶő9ȥʭÀơǹѣԟǵӆʏΦԮ¡иƷȵΞ',
                                                    },
                                        {
                                                        'key': 'xǵǷяС\x88Иʅ˪BƭҒɾ',
                                                        'value': 'ǽɓӁɭÆДͿ«ƒƝĬѐ\x85ěѵǢŀdưŴƠSɢ\x9eʵӜҮȈǞ5',
                                                    },
                                        {
                                                        'key': 'ӝΎȽÅҖŲªαʿɱ+ҩȀҁҔ\x9aΔ҂Ѯ',
                                                        'value': 'ŐǏęơүǁƾȠʸώI\x81ʵŘΤǧɔϿ\x99%φӠЦρ˄«$Ϫœɧ',
                                                    },
                                        {
                                                        'key': 'ʊӢЄ˛ԣ³ƝŭͷǴø{ѪȨҬZ˵ԑԣШώѯӡ*\u038dÚǹЬиŤ',
                                                        'value': 'ĒѼБŵ¾ѝƆδȅɃƣӈӤƼɩѴŌʼƲfß\x82ʚĢªî҆ϿԨ˘',
                                                    },
                                        {
                                                        'key': 'ГŗËӪÈƬŘ',
                                                        'value': 'ǶΎӶǄĳȥҸά˶РԆʋĦǸˇФЙöǶĭɐnǆVɶŀǓȑɷӲ',
                                                    },
                                        {
                                                        'key': 'ϪęáҗƦîǎʘ҉ƥȖфӐĽʤЫƗЩ?ПМϢРѯƦПʺҾ3Ǿ',
                                                        'value': ')ќ\x97γ¯ɳмϗȩ2ԪƗωҾӜ\x82ЋӹſƳ¬ĳӅşӼ7ơԚùȿ',
                                                    },
                                        {
                                                        'key': 'GšѠҒӞυ|ϵȄnΊŃћŢҦóЧԉѭąԭ1ʯ\xa0Қʀ¢\x81τҐ',
                                                        'value': 'ŌɢȼҍɇǋӭѧƘ;)ľҏȶúÐ£ǶϘ˛ɶͶсԪƲЪĠКӓŪ',
                                                    },
                                        {
                                                        'key': 'ɄӬΞ϶',
                                                        'value': 'ǑǺˆʢґē ʫʹʃˏЧʡŃZΗĸƾʕӬҘɤɩϫƴєʥЕ£μ',
                                                    },
                                        {
                                                        'key': 'ʠԌńҌ<ҦĽζ',
                                                        'value': 'x]ʑҞŢα\x89ʑƨıEЅҡbʹ˃ЮԦʄѝ°HĊйҪб˫ǭāƦ',
                                                    },
                                    ],
                        },
                    'comment': 'dȌďƆɹЊнÜœІSΘӺˈûáγÐ\x86ԡɧ·ТȳпwѨ=Üϭ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'master_sequence': [
                'Ȑ',
            ],

            'bindings': [
            ],

        },
    ),
]


class EventsTest(unittest.TestCase):
    """
    Tests for Events
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EVENTS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.Events.parse_data(test_data)
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
        for test_name, test_data in EVENTS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.Events.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EVENTS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='Events'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='target_id', name='Events'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='parameters', name='Events'),
            ),

        ),
    ),

]


EVENTS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ηȑĀɅʁцԍыãʙ˞ĽŘϡԝǈ²ӽЩΨŒĥ\u038bǧӿ҆ЇќʤĒ',
            'description': 'ÁШɃΉȳӬюЎҡͳ˜ҰȺΟÞΕҦҧϦƕϱʎ˖\x8fǯцɩƴɩО',
            'target_id': 'ԓǘǎҕɔˡʠ\x89Ӂзώ§ŕƅЫŶ\x9eɨǱžʜϒРƺȩ\u0382ʖŸâx',
            'parameters': [
                {
                    'key': 'έA҃Т',
                    'description': 'ǔ-˚ЈɷѣȅѬŁÐǛʲ˨ǀʶǞ\xa0Ϡ\x86éԄԘĽɂϝβ˚Îәȝ',
                    'default_value': 'ȽκӽЫŦӖνϮψΩɺÜѪʍҤǭλɍ˹ҘҘ˷AҺʚ\u0382ÃƼ>ǫ',
                },
                {
                    'key': 'ЬϕȩоƦǰӤM\x8fԗõѪʒѕӸԬþ&ľ˞ђ˼ѴaǊŬȀђӄƓ',
                    'description': '˭ɳÍĩo\\ǖųJѪťʻŔԈӒңƤЌԎӿʠǽ˘ϩŠǂүçƝϫ',
                    'default_value': 'ӅˡŌ\x90ˇԨλӋȭѺ\u038bɜ΅ѤќͱѨώӛoþÎ#ԦL҃˃ΙɃş',
                },
                {
                    'key': 'ΉˋʳӲǠɷƧȼɌΝϞΎǂȝĕǱШеҼ',
                    'description': 'χēʎѦÏӛσ©ʘǩǆ҄±ÒѽơζƹЏʏs"ѥƔēɂĨʃɺǥ',
                    'default_value': 'ŶƇŔʩNӄǺþʴl±\u0383˷ҌԥÃʝӗÐɞŻƒЎΌĻӚ\x91ƬɫԐ',
                },
                {
                    'key': 'Ȳ?éоɾŰεϔҒȲǞΙ\xadɜŃ.DӃ˚ƺԂεʏȟǹˍѱӮӾź',
                    'description': 'әƘЦŵǿоӷȼƕΒЖӈqȞĕ÷˻ɊвKԝşŠЍԌҜɥ;3K',
                    'default_value': 'Ӏӆ;џЂªūơрˁʭҖȀԪӏсƟȷԇȩƘΠ˖ĕÁ.ǹǵʱĎ',
                },
                {
                    'key': 'ͳԝȕǑ»ŻÙʄϭoϢЏXПǔƪʚѣҬсȧлɴӝ`ҏǀϵԂɫ',
                    'description': 'сċɯџǹϭľǣŧÖ$ǱȸȾˇƵԫ>ʥĞϖҏƑЪѹɉʬüśʚ',
                    'default_value': '7ŝϤӬԌȿМШíƑȖĸӎЛƥ˕ɪɏө\x95ȁʥ҂ӪԈЭʤŷĦӌ',
                },
                {
                    'key': '҄',
                    'description': 'ΈʣͳӨʕѩЈøəXԆʑ©љӭΛȂѽĽâтӖҼǁΑȩӑʭÇʮ',
                    'default_value': 'Ц˒΅ӀǞҲϻƷ\x9cΆǳϐ«ȑƚçώˏDЊľƭZҋɽͽǝÍȞ\u0380',
                },
                {
                    'key': 'ǃɀ',
                    'description': 'ŋјӎɭΆɮɨÝԪǋüVңԣ\u0378Ş\u038dɠ\x94ǒƷϒļɡԞȣΪӕˠԍ',
                    'default_value': 'Ľż҄ʫҼ%ЩɋƚWɯɆď-Ʒ\x8fÈL˒ŁӏˎϭΨӻͱыǔƔ\u0379',
                },
                {
                    'key': 'Ʉ\x85ӔSԁƏĳƬ҆ƫŚpГũ˷ѠΕӿȔ\x98Sœ\x8fϼԥ˄ýȍλǼ',
                    'description': 'ȯüˉӲЯϋӭ\x95ϩȔƏү˫ȍʙ:επ˘ηɝϧњϿΑǢÓŶʜ0',
                    'default_value': 'Κӻ@ɊćЪ©ĲҲŒƚѽǧιÀɏͿ\u03a2¾ƏҶʻ˾ʵš\x99тÍӏƷ',
                },
                {
                    'key': 'ӉpơƭŔЯԮǁȻϿөEѧΞҒôƿȹĖːȻƐ˔',
                    'description': '\x81ðЊ;˼§ͼ˶ˀt\u0380ƀԮę\x92ϚͿ˹6ň;Şӂ\x81ҽăԙǷСҩ',
                    'default_value': '˚ɗґԂǫҗG\x9aËɮŃҶϒƹ˥\x9a˫Έ҉ŋ˩žɒʓ\x83Ϲеíǜá',
                },
                {
                    'key': 'ǭˆҰҫÁͷ\u038b9ÇмҩʭǟɃ\x81ǣǍïɵʙӎѬÍМɰîφȑʸӧ',
                    'description': 'ӱϷōͺҠǮɼΙеԭԩȯҫčĶӪҠø¨ŷѤŶϣ\u0380ǜԈЁΎŨŶ',
                    'default_value': '`ȣƅћұŃɤВȈӴяΠҪƷÜƵïмǆ\x8eɷ"Ϛïɕʩϐʡúȸ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ɴ\u0383_',

            'target_id': 'ǘҦГĮ˵',

            'parameters': [
            ],

        },
    ),
]


class ExtensionEventsStateTest(unittest.TestCase):
    """
    Tests for ExtensionEventsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EXTENSION_EVENTS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.ExtensionEventsState.parse_data(test_data)
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
        for test_name, test_data in EXTENSION_EVENTS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = hotkey_binding.ExtensionEventsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EXTENSION_EVENTS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='events', name='ExtensionEventsState'),
            ),

        ),
    ),

]


EXTENSION_EVENTS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'events': [
                {
                    'name': 'ˏԪΈҩĵɂ\x84C\u0379ҵӭҀļȗaƽӹȡǘƙ˝˟ʐ(КШǀԖϺǙ',
                    'description': 'kΟˑҰͽɈ9Ů҂ɻǃÓÊΤâω¿ґęˣώЇɅ\x81˟ԕΪҝKЮ',
                    'target_id': 'ҌǘƕѨŢě)ͺ˝N˖ŜҏˇƑÒЉρǼӃðȃҡÈˊΤŭr]ˣ',
                    'parameters': [
                            {
                                        'key': 'ʜѪŪ',
                                        'description': 'ʧ\x8b=ԪҡňųƪŰé\x85ǔ͵˔ɫд±ҷЩŦȜɴЭΟŗϜĞӅƳȟ',
                                        'default_value': 'Ҏ˛ΘÎНȚũψіϽԆ˷ĖˇƾѮƔǑϛˢɖǪҰʭǲʷђɶƏϋ',
                                    },
                            {
                                        'key': 'śǳȌʘ˹șρʁϑƇĹϰȡęĄϙ\x98ĳԮʅǻƔүӿÚәBɫƺ',
                                        'description': 'œѽƭϻϖʎD\x9d\\pӟȲɃ҇ҐЁʀѳ҆ʟ³ЖͲə¥ÚȕԝȾŒ',
                                        'default_value': 'ɜЋ)ԧʺŉό҄Ɋϕʌü҅ʩśʾȲġ¹Ǚ)ȀŊӍμȧЍǽšʃ',
                                    },
                            {
                                        'key': 'ҩȫԊʹώŲѵϛEŁӻGÝƘžҎr˗ԜĔǽҎȶеҢ˖˗ÉɾЯ',
                                        'description': 'ҵ\x99ʰ>ЫФυԡ\x9bƨ¸ɫə[ɆľȘNė|ԊЛɾ˘фƼҰī\x8cґ',
                                        'default_value': 'ŭǖǔԫØĥȜǰГδȮΤΎďīȢ˾ʏĮȧńìȮ(ǩˍћϭʇԭ',
                                    },
                            {
                                        'key': 'Ȼ!łÁ',
                                        'description': 'ƍċǕɱԢΘЛϪšƗϡĹҘӉХȨқƂӺбδǵЛ\u0380Ύ¹ˁ¿ʭɥ',
                                        'default_value': 'ϝѰĩàϩƠɷԭɸ҄рΩҿǪǃ\x94ӋϴˍЉұγǀȺɳѥíѩӼ%',
                                    },
                            {
                                        'key': '\x93ȫ˂ĈɠԃÇύѐ×ÎѫӅ˂ͷ·ǙԉҶƯ˃ÈηȘЂ',
                                        'description': 'ɕə&ѪȖҔа}\x8eʛɜӯɇƉėπσӎǀğŘˆÂ#ȃӲȃҏɓх',
                                        'default_value': 'ԗ˨,ǻÍÝϧĀƉӽǳΨ˖ϋŵȜǵȮɬǎ\x92XԨңqњšɓʞë',
                                    },
                            {
                                        'key': "ȀÊЫӚȳɅGƻљԇϑјΆĬ\x82'ǭ²úȜĨҳȒēʙ˷ĸѱ҈ʰ",
                                        'description': 'UƨĊȝ<Iʡ˂ʃӳʿØÀχ˪ˀ˴ɸāӾҫɒɅɘƚѢŠżѸÜ',
                                        'default_value': 'á˒ǿ#бŜЁô\u038bҤª˜ɹԀѢ\x9bӅĺη\x86Ϯ˃ɴȸ\\ȣŃҭӮͷ',
                                    },
                            {
                                        'key': 'ƇˊʟˌӴҚˋЕΛˍˇʻϣżϪӃƊ\x98VőͶ¤ɲѠʕЋɭҖ¥Η',
                                        'description': 'ɿ˵ƨƙɴіӪԩÝΊƄİ˴}ɓϜɭзƘ¡ˎØϤѿұƝĥMőŻ',
                                        'default_value': '\x93ӈαүγŎȭ˚ˏӢȃҵ˅ƴ҈ɽɃ8Fe˅ȹŒ˽Ǯ˼¹ƼԂí',
                                    },
                            {
                                        'key': 'Ӆȷɇȧ¾иſĩƬЬ"˧λĨȭ?ɒMńи\x95¤ɐ\x81ʤΩҪӨԬ^',
                                        'description': 'kȜбӨɲϼΐӧyƈцԢѕӃΡ¿ȰǗ\u0381ƺһƗůʺÂ{ǿϤҪд',
                                        'default_value': 'TԔŞÀϥʂȯϵҕҐʛË¢ϵѶȸĂҰ\x95ͷ\x8cȷҳǟɓуÆЋìƖ',
                                    },
                            {
                                        'key': 'ŹɷÏµɴ%π',
                                        'description': 'αΨƗԜԅўӄŞϜзӵΦʺñǾ/ԡ¸ϘμϼÜʹͰȳȈҮ˚ÇŠ',
                                        'default_value': 'Ï˵ƟʂñɔԠ\u038bđȥ\x8cчβʱϻőәŁ΄ǳʮфԖέӟʈ<]ϳĎ',
                                    },
                            {
                                        'key': 'ðƏӡňɷӫˤ»ҟƵƊʹ)ɹŚҒÀƦkȣČȇʥƠιÕ˻νǆӴ',
                                        'description': 'ʁȂџԇʲЪԉǜPȐ»˙ӥʹđɼęɋÄʇ\x86QåÙјɣԔ\x8fƦţ',
                                        'default_value': '˛ѿѸʠÉɯyɲ`ʬbèԛҾɶɟÀΚΡƱŞǴϋӃФɃ\u038dɄǪӘ',
                                    },
                        ],
                },
                {
                    'name': 'Ӯ˺Ԏmüγсδĥ\xadԄīЧӸÒĲɟl˗ėӚЂҶƺСȣ˻Ϸԑć',
                    'description': 'ӒӇɎтǐτЂϛϼϗƜ\u0381ťʁЮӆϕʺЈӍë˨ȿl+ɟϪ΄¼ί',
                    'target_id': '=Ȋёʶш_˖ЫɵĂ˕ѬȟϟΪ4ȤȜ͵eϕÖυȤЋБɿźƞĉ',
                    'parameters': [
                            {
                                        'key': 'đɔ\u03a2ɫúΝƬɫкȥάӟҔ҈ċυĽρŻҍ\u03a2úEјˎԔԑƀʃO',
                                        'description': 'ТӻŨҳѫ\x9c\u0381Ǳˉ\x90ӇŌ».ҤΦԡĕ§Ԋǔ˲ìΟ±ԣѬp>Ț',
                                        'default_value': 'Ǧ\u0382ˉŔћʣǨ)˻җûҞSϤǓуkĢҝǚåӌеȏĕÜɱԋ¨ԣ',
                                    },
                            {
                                        'key': 'ҒʷӻO΅ОȅʸżƧԋǩҘИeˠıĹ¸jȸĔăPƪҞqǘ˖ú',
                                        'description': "ƴԞXӗȎӻƁӥГ'ћŀјˏϱͷѩƪʎǳʕŕeбˊƱˮGŸ`",
                                        'default_value': 'ͲΪʻǵҢUѥѰλӾáϣūιkțшƲȧʶϷãϤ˼Ҫɺ4ϐȭ=',
                                    },
                            {
                                        'key': ' ͽ',
                                        'description': 'Ø΄ԡÃǱ˓@˞ʒҐ¥εѪώɴΩˍϺȲҴR\u0383ÇƮʠӲʎĜϹ\u0383',
                                        'default_value': 'JӺɼԊƠfЦѿ˘ӤъŭҚGɽ*ŚͲÜэɌɋôѶοдӝȉԞȜ',
                                    },
                            {
                                        'key': 'ЄɌːȬҲФӴʏǮЛƅѓ[ϹɑүǴԭȓҲ]¾1ƀХˉØԅ\x89\x9b',
                                        'description': 'ʝɄ˳Ϲ˦\u0379ͺĩΧɿǖȗϫӘǉȇѶΰͼʮӀ\x8fЃӹÒ˄ѕωʹϐ',
                                        'default_value': 'ƬvДϐÅŶӍϞȮΩПͻВԧѝӲζΑɸцǋRԞXǐʩPĲƫϻ',
                                    },
                            {
                                        'key': 'odʛīșƻgϐƫě+ǖȹǫϠåϙǰʟϷĨӮӵ¡ʨχӟ\u038dц',
                                        'description': 'ԗɉ¼ӪԜʀǓ˄6ԄƗϔϏҶԠ˦ϬӝсôΏîҜƐ˦»ѐ˨аĉ',
                                        'default_value': '#Ƶ\x81ɃϷЅȥ¬×пԖԀȕ҈ўёÂɥĴ˾Б˩ЅΟԚȅΏ§ÍԚ',
                                    },
                            {
                                        'key': 'Ԛ\x85ɶʇʨǰ_ѺʦдĴˍbІ˘ǀ¥ҿĬ˕όҀy˧ň·ԩ»Ǘˏ',
                                        'description': '\x9aҖ°˫ѼyǨ;ȚʵӖ˸ȤԧǦρʝҐÙĩ\x8fɬ˷љӤсʈĚӽƃ',
                                        'default_value': 'ƉώƛŬÌДǗ\x97є=ҳřŉ.ȪїȀͰśϊ[ϣԐΛŻ«ôéϜ]',
                                    },
                            {
                                        'key': "ϯʹƣµaӜǴàҗ˞ʫŉȟȧѠÉȁ\x9bʨǌġш'У\x7fЭȴύØ·",
                                        'description': '"ҎӸғšҵϓŨɯҵυǧ\x99gύǶɹ¹Ζ\x7fĿƑǸцШmЦµåԧ',
                                        'default_value': 'ӬƲēõǖԨɓĕÓԕԍвƟϰƉӂřÒϚÂƟΊ:ΒϙňϻȀӒƀ',
                                    },
                            {
                                        'key': 'ʨ\x95ʼʨӶȧ\x8bĳͼʆόŪĨӃʫҒʐЁԉ>ґȵϻhԄ[ϩȍώ"',
                                        'description': 'èӮξƺȄҞr\x7fýƿũĈҜʏ\x8b˽ȇʸŅƦ˼#ɦĈó¼mϬƘǅ',
                                        'default_value': 'ƺÍȔƉҤӞȄ϶ϣй\u0378ёǉȉ϶иіжάӄǥҎɍЛĀвƟơC¾',
                                    },
                            {
                                        'key': 'Ϡ˕Ŕҗ˰À5ȹѤŤʝĤŚԡȪ',
                                        'description': 'ǧҜ<ѾơϼԨǰʹϸҢ˝φǸЬξũ\u0383þԛѐ΅ӰɭƄΈƪÛ˞˂',
                                        'default_value': 'ҕȋɈƤȋCа¥ԂŮОŴʥʜϨ˼҅ɆӒȺ\x9bǟɾӉƕҷ/ȁȪǲ',
                                    },
                            {
                                        'key': '˜йɎyʥȦʏûɼǭβǀӒпʱϚŃǚǌǹϑĎΤĿ\u0380ѥϾʀЭʷ',
                                        'description': 'Ҙ»ϖɅ¯π҆ʓʘфʵʾʌŦ\\ӎʚҘº˕ЬʔѪϥЈώ#Ł˷ˁ',
                                        'default_value': '͵ğɭ®ȭĤхȈB@ʃњǥƮ\u038dѻʭŖ§ӾŐȘӤȊюĞΪŒϣϓ',
                                    },
                        ],
                },
                {
                    'name': "η÷Ǽ\xa0åΑӔ6'ʪêϨ˒ƔjôҰҋÆŨʨ1ҀҲэ9/ʠƉʅ",
                    'description': 'Ʒθǂыý<ӣҝƻƊΞʍчȈˍȅǋÎȹҶНȰӡƬϸǁȭЅњБ',
                    'target_id': 'ѷԁӯϏҮԤʆαưƫγĄÕԚΩʮʊȪϔɹu?ϾɬɪѝЭҼӷÝ',
                    'parameters': [
                            {
                                        'key': 'ūÿɅ1ƛӆҢƗɣѽӴŁ´еνͽŎ\u0383fÜ ӖŲƅѥӌǚèȄɜ',
                                        'description': 'АѢȷ˅ßǽ϶\x83άqˠ\x81ȂɔҊaʒѩÍjsѢĕ¬ώƧЍ¼2϶',
                                        'default_value': 'ȡЌǯʻϴТȻļɰʅO¯Α\xadɋŶђɭʓƪȝԢȄ3Ƣ,\x7fˎƃӦ',
                                    },
                            {
                                        'key': '[ƎοϗˬͿÁϚҶӲTċȎԭȴαҘİìȥѻ+ʘţѩDζǴШŽ',
                                        'description': '¾ͲшʂƺӚĸˡїҺɫӣФƂ˹ǧĬƽ{ɦԌƕøѽǒwϘҨŨϣ',
                                        'default_value': 'ɑʊĽХлԑȋ\u0378ĹtΏ҃ʊƋùˊϘùͲƳDŨȖӭǩäҼÀ|Μ',
                                    },
                            {
                                        'key': 'пΡƔЛͶŢ±ʔԌʅшѺҘϞ+÷ƶģɈ',
                                        'description': 'ӚìԬæ˚.ΤԎԢıƩǠŃɏеҏœ˨ēҀˏɚƩÐя§Γx¥Ϛ',
                                        'default_value': 'Ӯ˰ƘXтч)ƤҨԐ}ҭÏϯōȲʆўќƜːϛ"ʥѼҟɜˇƔ\x92',
                                    },
                            {
                                        'key': 'ŌϭÆȟÐéϴαѽǽȯɦňĚӜɤȑЮѹƾ˫ˁԀԍİEѪƽ¯ĭ',
                                        'description': 'ʹѸɖЫΩɛϘҥҧȎôŸЮ\x8fҎҋďʶÆuʔԡǉőЉ\x82ȕůʅ˹',
                                        'default_value': 'ӥ\x8fϚü0Òϋ˓щȦʒƃзɸǗʠϗĵǥ9Ė\u0378Ӈ˹ĖˈĜЛĭԇ',
                                    },
                            {
                                        'key': '˱ЍĒĳTΨ"˵õ`ӻϦƼԦģъɁԍΏΜǿДǎϰӢŉ(ǈ˜ŭ',
                                        'description': 'ʡξǓԒʝŵоŕǶϷɂсеș(ʫǣϘԊχɣAϐǬéŬè\u0379ˍ\x90',
                                        'default_value': 'ӨʥφvѺÔɒλԉŌǶ˱˪еʰΥɘǬ\x83ÿRď҉Ǻџ\x93˴ěгǽ',
                                    },
                            {
                                        'key': 'ǎмӴǕ}ʃĔ˒ΐїǧŚºDƋΞҷ÷ͻßşϼӡƬqʡťƝGǭ',
                                        'description': '«ӍӻɵªɧԖǃ»Ƨʁ˲˼ȫϘũɡǚͱ\x92σΉÄϠɋƀΘʜǸ;',
                                        'default_value': 'ǳ˵ӢǵĜǚĳѕïÝǵԟňï÷<ȰϜĈǪҦˢӂŃűСʘƺįѹ',
                                    },
                            {
                                        'key': 'ӯΤĔǔπŮ\x9eŵÑΨϺfăxʝƞǶЕϾĥЪeк˲ĶY1=ςЫ',
                                        'description': 'ťԧ~ҘλɁϐÍČŽӠÕÄƱѭӾȥ3҈τεʺΨqŜyӬϑӉ3',
                                        'default_value': 'ӝf}ˍӆƃÝҡɅΕшɬRΦϢȭɝӮ\x8dÀӣ\x83Ģ\x84\x98ź6Ɠˡʌ',
                                    },
                            {
                                        'key': 'Ιˠϧƫ\x8fȅǉ_ʽ˩ìʝ\x87&>ʼʹ˲ǎф҆ȤˁĎÌƺ',
                                        'description': 'ßʊˍ\x9fӱНƩˤԜǍƸǉˤĻǭȓǑwӬтϛдѵЊŢˇӓįáқ',
                                        'default_value': '#ȇ˦ϝƻӍԝƅƅԆ҅ǸН%ħȵѺҌСҕŅұ˨œĺʇÂͱÔИ',
                                    },
                            {
                                        'key': 'ӀˁБɤ#ƭx¼Ўƶңx¤\x83ʐˌCқҤѥΛĂ"ŖìѸµǚďɊ',
                                        'description': "˫ҊkĠʿӯʟůɊDԅϐЍԩÐ˷ȬĥͼҩѓҚɽƚϞļԊ'ҏ,",
                                        'default_value': 'ԘʀԎȥǲȆȓȡɩęƻ˯ÄȓĆʠ}Ȃ<đɓˍʲˏʡʍ¢ҲΒĹ',
                                    },
                            {
                                        'key': 'ɘӒƵeцӧӪǁȪŞʫӸœӕŦ\x8fɺЧGôͶɀңΝńʛЀɃˣǔ',
                                        'description': 'ϛĝϨϪƬȽчĎʮȥ¶ǷȢԁǕ˦ëɎņGБЬʩSΏӄωƫӜ\u03a2',
                                        'default_value': 'ʤ8˒ǠӄκȻʧΊЈνʉȀȦ˶ȳſӣȋϜϦŋĹΕĖɢҋΎ<Ӓ',
                                    },
                        ],
                },
                {
                    'name': 'ŷ-\u0383ĠӀϺʙ\xa0эŢ·ĝȬ˷¡ȐӢƘͳƀ\x84Ȗȳ\x99jV-\x90\x95Φ',
                    'description': 'ӝǒ˚ƴɷʟ\x9dĠЫМӞϓΤǥÈԞĽȸɧϢ˯ʽйΪȑԁ«ƛȽӚ',
                    'target_id': 'Ҕǋī˸ŧ\\˴ЙèʋѠɰ+ʌ8оШȰŝÆȤϘщ¹ǥȿͳƤäԤ',
                    'parameters': [
                            {
                                        'key': '>Hȿ^ЫЖč\x7fɞ\x96ȿԘ˖ˢђΉʻƾʕVрƏýҚҟ\x83ĵɨøѷ',
                                        'description': 'ɚƛŇxJȭҶĒȵҬƽŭǎԩЃƩƫx\x96ɻÜÏİŹϖЖƚќ±Ԏ',
                                        'default_value': 'ж¸mЩɢҖ¾҂ÏπǭȸϓJ˷ǹȻ©ѦɶƙӌϺоҎλΘ\x89Ѭʁ',
                                    },
                            {
                                        'key': 'ӫLӂđ҃άˀļϐы\x96¡НÒ\x8cӧǡѲ˷ΒӋ҇ӋƸϿɬ¶á˧ԗ',
                                        'description': 'ƚ£ӭÒǈХƭɼ˟ѹļӤ\x9cLǔȿƨbЩϭÁƧl\x99ľȍgīʍ>',
                                        'default_value': 'ϱыǷʄ¨ɍ˜ԇѠġѬcɣʅÜ\x91Ň6ІίҥӖƼ҉ʰ\x91ʡГЩÒ',
                                    },
                            {
                                        'key': 'ҩ\x91ǟɓšӼƸŝȴ|ЃS&ΌɞÏПԢȸɪ˳ʽ˥ƈαȭŚҾӑǓ',
                                        'description': 'Ϻª˘ΑϺɺɅԉҵѫǼƂʊɿ\x81ŭ͵Сȕŧ~Ҫ,ǗeɖпƣҐƭ',
                                        'default_value': 'βÕ©]ʘЫЩŪǎƏА˅ɇΦɣŀЬBʋӰf˛ԝÙ˞ϋ˩Ϻȇń',
                                    },
                            {
                                        'key': 'ʌȮмǁѲԒqͼÍ˶ƹȳŘɡʃ^Ǿ\xa0ʍϳǋӟʸҫΧcĉΖǊˁ',
                                        'description': 'Ќщɸχҟŵόɱ\x94mЍȯ#ãÏÈʄЁ¢ѠË&ϛΖʃɄѠʌÆɻ',
                                        'default_value': '˳ȒӑȼхҊҺŽ\x99ԊӨșʂсԣӽЮɹá\x81҅ҏī$śĊʷѻķԗ',
                                    },
                            {
                                        'key': 'ȼxӫÂ˳áҌhǨιѮµHФɟúӠЭƇɳșƳɋ§IɘǕÞɣƄ',
                                        'description': 'Ӻƭ˶ƠҦМϏoÙɩњГԈЃԜҲgɇĽǈϿƂЈȴś˃ԛɋŋC',
                                        'default_value': 'ӎҮҺщό<κѾеəͻӃ\u0382˱˽ũӨ\x880ðɳԘȁΞӑŅіԌƖϧ',
                                    },
                            {
                                        'key': '\x9aɁЇσʋΦӖʱӭ\x8aȾCԥҸ˽Ɋ˝ɬΡIӨ҂҈ßΉҳȀkΪѳ',
                                        'description': 'ƖʺŐŖӐǆЖМɬсM\x9cųԓԉїӿςŎΣϓҔÕҳǔȇȞÄ\u038b˖',
                                        'default_value': 'ͺǆȹ×\x86ƞҰԉѥο\x8aȺԉɺÙǬЦ|Ԭπʡǜԥ˔ãҊɓɐжh',
                                    },
                            {
                                        'key': 'Ӟˏ\x8aúάsхϠˉʽԊ,ԓǁϽ\x9fñɬΩɎͽŦŔĖ\x81ӄιнĤѣ',
                                        'description': 'ƅΑ\x96źҌY\x9eҲϨ˗ʶʬ϶ĺҮлЊжíťΔΘˌÃϵͿȢƅą¢',
                                        'default_value': 'ΕͱέоБɋȂɶ/ЛǬÍʶˣŠдԤʹ¬цȮˣɽӔƃӇȅɥǶљ',
                                    },
                            {
                                        'key': '{˰ЎѰЦǧưϨèȚFԚΨƘ;ɶʙp{ƨp˕īτĂǩÒùÔП',
                                        'description': 'Ҹ\x8eңϧʼ¼ÒДҿɲZɯұҋΆЬ\x9aːƅұФϞ˝êίτμŌζѮ',
                                        'default_value': 'ЬŰξrŖωYҥͿǸÅΜҩƴû\x84ŷÛӿƭԈɅϳ\x8b\x80Ӱeɰ½ю',
                                    },
                            {
                                        'key': '£ӲϬđɦϪɸӄȨΰ_GpíќǽǠʉІϧ˸ŭòȯӖ\x98ͼǹïǯ',
                                        'description': 'ǎӛҦ²ǆғÐ˴ǱǴїϘҼʩԈŖźҚԈԆӎʶ=ϷтǆªǬȸϓ',
                                        'default_value': 'ǞԦ1ѮӮЋƻêΫѭɘӸѺγҎżɟķƝ˭ɪнƭӟǯɣ¸ȥʳΟ',
                                    },
                            {
                                        'key': 'ϸǬӻί\x8a\x87ɤԮέ]ɲɮйrͳϡņĽқzëĜ',
                                        'description': 'ҮǓΠɈҡҴǣ˰ҳѬшĺϲǔӓќϸÓǷ ʲUçѼϘˠïÕɨҧ',
                                        'default_value': 'ȢԪԞԧ˹αÍʏʀɐƄźǰ˕VˠȴďGÁUÆɼѨӫɉΘдʳБ',
                                    },
                        ],
                },
                {
                    'name': '*ΡlȊҡԎҸͰΙÄƑӾƣșŕҲ\x96ǁňİ΄¹ſёʀҩБʭ~¡',
                    'description': 'Ąˈ|čӞДÄÔ˛ƕŌ\x88ҌţɶҴʧɍĳԟӍϒ˴ʗĨΦɳWƭƆ',
                    'target_id': 'ԊϋǌŜӗџƧĠӶɱŽţɯΘƼȈǩëǲćâ\x8dǆǻƁȾΑΤ¼ʹ',
                    'parameters': [
                            {
                                        'key': ',ăǏ҇ɡÙŅȘЄΖTԫÚǢã«ɏĈҷъŵŘʑѤϨӰ½ʤǿӭ',
                                        'description': 'ɕɶЏϠҺ;ːԐĿҚӋ҉ӮǨҨ/ŚԎǆχȬɜҜŃǙΪ³Ѭ«ʳ',
                                        'default_value': 'ȪˀԗőΉӑҏюɋhŭǳЋŏŊăΉңƬǯˉϿѼǒ\x9d˩ɮȃԤɀ',
                                    },
                            {
                                        'key': '\x97ĩ\x8dɇϩȒǟɦ\x91xǤϦģȩƚµ˧ΤӹɔȬѯ7ҙҵчû\x98Н˧',
                                        'description': 'éʏйѭƈГԙζΛöԪ"Èζ\x8aȏͲϱʙУ\x8cÖȫǯjIЮʐøʯ',
                                        'default_value': 'ĸʚ1ɢԔȇϓϦʘŦɬıɨΐĝӌέű\x87ԂƞƐĜπƱ΅(ËƀД',
                                    },
                            {
                                        'key': 'ӾҙɜĹǓҤðҬGȹԏeϛӦˠˬɦЖáɿÝΙÚƁÝǃ\xa0þ~˩',
                                        'description': 'ԈԎ҆ʠƨȻʖӏӌѯЙѴǂ˺ʻӀǝǹ>Ȇ¹ɡoX҇Ҷ\x84Ύԉ\u0383',
                                        'default_value': 'ӞƓ\u0383ơŌ\x82ǴϱċˑžҔĞ£и÷#AɃūɎÒEęӖϸíырc',
                                    },
                            {
                                        'key': 'ʥ\x82Ɠ\u0381â',
                                        'description': 'ΤҵҙʃťǓЩƫ˥ѕǈǊɉ\x9aƯͻØԮԤě\x85ѴԣƮɣʀ˪ɮ¶Ŕ',
                                        'default_value': 'ȍǛίĉʧǯҍȭ˂ʚ˙˻ўƖġԊnɊχćѨòfŊvʂįȉѬӇ',
                                    },
                            {
                                        'key': 'Ѥɿωʢ%\x80ȗҼϮŗŅҵǣԍġŃй\x89ӞĜȰ|ͱңȸȲĝӇҴb',
                                        'description': '˲ӛΚҪΡȈǄɜ҇ǜӌεɠʂ˲ɽBΉԀѷȖõӾμԑˑǕĥÜʈ',
                                        'default_value': 'ß!͵ÔӢјÎß¤ԝӆ',
                                    },
                            {
                                        'key': '\x95ƌơвХŌϻƏɥɥΧѓɾu҂ÏɩȀňĒώc¯ӎʪʤ\x84ӌ\xa0Ĕ',
                                        'description': 'ÉΕʁĈ¢ҳԉɯ\x89ŵŪҦw˚ӡRϿƾɩșʉǒĮΩҸϲTӌFq',
                                        'default_value': 'ҶĤΜĊԐđǧЋʰƎʽԞџϋӦŢς\x89ґΙ˖\x87ҝҳдȆύǸs˲',
                                    },
                            {
                                        'key': 'ƑżñŘÚʵdŚlϨkâöԩ ɓëΏξUѯϴԭi¨ңǩз˟ї',
                                        'description': 'ŧɬԒɪɥΟҒÊņҎϐĈȝǡoҽx\u03a2нjǗ҄ȱŌƵԑǭŏǳƝ',
                                        'default_value': 'Ŕ˧ӠЛȟɥѸ΅ȣĂĦUίƯÚԜ¡Ъυ\x87ƚ˖\x93ōё-aĹӕg',
                                    },
                            {
                                        'key': 'Ц\x81ǘǑ\u0380ˣԈ˒ĎŔɢИÑ˝υZϫxӪȖƝҢɀŜϨœҋȂäȫ',
                                        'description': "ϜШǋȽŹηϙțƪ˷šȞō'ŭѐĭǢv˵ӷӯxøћØǝâȭ˩",
                                        'default_value': 'ɺʾҾ\x90¿þhӈÊԮǇųÔġԪжΩǉʌӽƯ҅ԋĢӌĔөƝˎĻ',
                                    },
                            {
                                        'key': 'ɝ×ˊƨk\x98-иɴ0\u0379ŦӸӞҘȯɐ\x92AŚĮàóǽӹφøǣΉĄ',
                                        'description': 'ˬɨ×ƜɀȦʸљƐˠѫʄҊƇȔԦĝΆС\u0381\x89ǅ˓ƚɆӜԇͼԑɝ',
                                        'default_value': 'ĒѢūуɦšT˔\x9eȾ\x8eΡƇˡʿȅӼĜҜʪdӘϫ˾ÿϗíȆœƄ',
                                    },
                            {
                                        'key': 'Φ˯ɯɦYȢЍ\x80љÝő˥˰Ĥˣ2ī˟ƏӶ˺ϧˊϭǶ5ӝØ˂ѧ',
                                        'description': 'ōѤԒʡɜӅɌίҷMOҕĔŅƢ[oɆʳћƥÄșÄЛȹǭӷӤƙ',
                                        'default_value': 'Ț\x9aӳГɯ˸ʢɽȥ\x89Ⱦȃœ|ӐΖҬѦҸϴМ2Ԛӏǎů\u0383ɳ9ό',
                                    },
                        ],
                },
                {
                    'name': 'ʜȶʋ˓Ȣȧӝ"Ͽ\u038býɖ*ȅϼҝΝΎϝįæɡͲÀӗ\x9dǞǶĞϓ',
                    'description': 'Д|ƝƯϞϔԠңү|ɞŜ|ѹԁ;ͶÛΏӀқƉ҉Áɍ[ȯɿĬˇ',
                    'target_id': 'ì҃ƂȃҩԒβҢΟϱ˨қԝ±сƱ˸ο\\ɏˊµȒӑŌ\x80ӴǓȖд',
                    'parameters': [
                            {
                                        'key': 'νǼԊ˱ΎŰʆǜ',
                                        'description': 'ԩ˅πƾƍͼѳӪǴʡШǏƪѸʞɋӗšӏӒ©ɡӇɅȳːЈӉ˂\xa0',
                                        'default_value': "ϸЖ\u038d©®Ұ˷˯ѴнʹΥĘǺ«ҹңбČБЙӖӢԌ'ļŮĥУӸ",
                                    },
                            {
                                        'key': 'ĶɎɄҥΚÔʃýȿѶЌɺȌėԚŸòӿǰй~ŁЁ\x9dčʛ˛ƠĶŪ',
                                        'description': 'ɞϿӑɖώΡƛήҋþˆʣрҤЅļĻЪМƀȳÚ˂ÜĆĀiɵ·Г',
                                        'default_value': 'Ю\x8bȔΟɌoԕЀĳȥέЖNʆϹѢǣɰʟХǍȇͻԠѩӬWǲέ\x9d',
                                    },
                            {
                                        'key': 'ʉKʨqϩŬѨΌЎʮɝԃwʣ˝ͽŋʕԨėҌƛԡέĪйНХȌȠ',
                                        'description': 'ЬīɠƘĆǵǔϢΕĹчϏФЛȒҘñ*ǚùȳũϹӻĦŢǊțˌϫ',
                                        'default_value': 'Шʊԛú;ʚƆΞű$я\x98˶ŤĤҟίʀΟù҉ɢԫѬӕҵȵҫћƵ',
                                    },
                            {
                                        'key': 'ӁȡДˏė\x88ЧÝŶҴĉΙˈџϣЅ˓ʘӪʱŭЈʦŶżРłĻ3ì',
                                        'description': 'Ǘ˞ƞɵ\x87ɻÌĊw»ʷԋƕŋ¼ōԀί\x97ϯЊȐ˺˲ȪŔлŲɱҍ',
                                        'default_value': '\u0381HѴɝΓ˔ɼҁΆÔЮƵƴϑ\x91įĖʊǎĖɩӔʝӥɣçʲԊǿӋ',
                                    },
                            {
                                        'key': 'ιǡФÆǆǒɨ ðщÕϷʓɾƀʅωԢȵį˃ɻԠ\xadҜΥξϖӓЦ',
                                        'description': 'ȚҐǴ^όËʊτϐDηκʧМХҿfȩ\x9fʢЧ\x8aΌЄёŹљı΅è',
                                        'default_value': 'ǵňϹΥŦǍʜϼöљ¢7ξx\x9aǷʏ\x90Гс҄ʣҾʨɾˌºΜΠƩ',
                                    },
                            {
                                        'key': 'ѡǉ\x80ӀȺҁˡĦʍϫ҃ҩǉӾΰР˪ŦԎυȕÛȸǵāǆcʺĘz',
                                        'description': 'SĐɠČöF<ƁЧ\x84˨Ɍ¦Ɍ8ƯÜӱӶǪŤʤŞҘÇ6ϝȸǭŕ',
                                        'default_value': 'Í[p>şëĂ{LԒǹ˟ƇǾǄıΔүɤɎŪиWХǹ\x9czżĆά',
                                    },
                            {
                                        'key': 'ԦрԟЉɇйʱθǉȶìӞјǏZԜǫǧŊЪҷƏ\x8bҷØԜ͵ǣFȶ',
                                        'description': 'Ёʿţǆƛη\x84πӆʗʞƸʖøӀɥ҇ĎΐȐˮϩ˴2ғΥəİҍѬ',
                                        'default_value': '\x9eȴˉͳώӱɸѨЙ}ϋĮâ˺¶ҏƻ,ʶŕήèďԙʃԚÀϣʕŎ',
                                    },
                            {
                                        'key': 'ҘRrǪ\\óϋȮӭ˵˖ʗň7ҜÕϛđӰйb˽ԏȧħæǧԐΛƦ',
                                        'description': 'ŷϐϢįŕѿβƾʭԣ¢ÊoȤƭåĤ¬ӭњńȨsˢѣϋϒlƲϢ',
                                        'default_value': 'ԥкȂáнȾʹɭ˟ɪƣƵȐ¦ǥЏΣŅΌȡœ¥҂ΗȧĵʖƷņл',
                                    },
                            {
                                        'key': 'IĐÐеҬэɕΐӴʈKĦЕȃĭ1\x85ěÁƾӶȞʵоιφǫfŊȏ',
                                        'description': 'ѓÍ~Ӯ!·ѯӚѾôʂĞӆÞΉƅõϚѤ˕Ίӂϴ˼ѱΤҕϮ\x91Ƌ',
                                        'default_value': 'PҧǿӧӪ˰Çǝđ{˵˰ţĺѝӞ͵5Ùǽțªѷƚ˺УʐƁþi',
                                    },
                            {
                                        'key': 'zƅȋ',
                                        'description': 'ϵƓƤ˫ѵ>Ԑк¨ѸƠɐǀũѶ˰ԫʖƌұɖǾǤїĶȪƊЙʞŇ',
                                        'default_value': "ƴŰƩʬїÝёŕćѠш\u0383ǚ2в˥ƔʍÜú'ƭӢҀªΠҥѝȖT",
                                    },
                        ],
                },
                {
                    'name': 'ϧɛФɃ\x94ɾΦѲÈ\u0378Ǧ˅ɰӘƶэԪҖÇƏԭԢӚΟĝԩπWɄњ',
                    'description': 'ƯŀQʹȢɷ˅¤ǲʋÔζȶҢЉʺϣƗǯʓԇɻʺôŭ˺bɣѦǇ',
                    'target_id': 'ƣү¤ϝй-ͳιԄʲ\x97˒äžC×ԎƋʱÄѸ˧Ѣй҄ҌϵYȈΛ',
                    'parameters': [
                            {
                                        'key': 'ŪĩѪÙӭHġŉ˗˟Ѐ3³ўÈ˜ӝɌŏάҽ',
                                        'description': 'Ӎ«ѵɪț\x7fǹξźĨӀφɿұŜӴƪĨԌÔԓƋŊ\xa0ԣЌ϶џˬҞ',
                                        'default_value': 'ūӆ\x9cЖÜʤđǀϥøрȀˑɡˬȆҤћϏϜɉΌ2ƅɰɏϜԛӪԦ',
                                    },
                            {
                                        'key': '×ćίԥ΅Åe˘ӈ˄ǦȍnҲ˅҅ʽvɀϓι÷ҦЮȍɭԏȗӱ\x82',
                                        'description': 'ſ˖ɏȋƥŖЁЂԐүϝ\x9c\x8aͳˁêέ7ɔǑǩ°ƀϳяǴ\x94ɮљÎ',
                                        'default_value': 'ɱѿϰʐϩӌίǔӃǄgӻªǊdʣʘŒмΛӂBϒÑўȊԤȧç\u038b',
                                    },
                            {
                                        'key': 'TȎˁeŐřѣȭєĂîҺȝʎGЮ˳ɗюƨϋȖΎÈԢΨũұSđ',
                                        'description': 'ɭΎǖƗңˍǷʿʄҞƌˣαƅӨǫıρŨЇ&ǐƛ\x9eʷ\x99şÛѯ%',
                                        'default_value': 'Ъˉѡɂ(ЭʺĕżʣϡѼϯʽσˮÇЮõǇƲłȴЍÀрȸӛЙƓ',
                                    },
                            {
                                        'key': "ǿȷͷҦӝніЉΤӳОγŵƩ_õ7ҕёΣ_˻ԑ'ʦѽѥɻħҮ",
                                        'description': 'ӈďǗͲɄî˽Дʯ;ǨŹĭėķ˛Ҫɖ~ћҰĄȚ˚ʧŰԨfˏϞ',
                                        'default_value': '%ҢɧӾŐԚƒԧ\xad˞ɜƻВΏԜǷ϶Ѯуͻåˁюʟă+ΆϋђԄ',
                                    },
                            {
                                        'key': 'ɕŏˮůЯFZ\x8e«ѝ',
                                        'description': 'ǽɝÁҼǳˇƠ0ȍҕќʴҝmΙʨĻòΏ¶Ͻ&\\рƩ<ɫѪȠĦ',
                                        'default_value': 'ʕɓϬɋŔǘ\u0380үǰͺƵyȪßЅѵƕ5Ʈ*Ԝ˰χҩЩ\x8bΉοϏˊ',
                                    },
                            {
                                        'key': 'ԍЗĉɃ˞ȸю',
                                        'description': 'ȗ]Ϛ\x95˾ԇIҿQáԆ¦ʼŰŶϭϹЯțУ\x7fǪҌӧ\x7f\x81ӀXΨȈ',
                                        'default_value': 'Rϻ˃ʊʕӮˏhŻѐΛұɀПӈЕŴ(d¥ԋĺé¿ƕӗLǅ\x8bʣ',
                                    },
                            {
                                        'key': '\xadʶύϽɠИȱǟΪԏʆЪʘҕтƳԪϛėǴŠƖƅ\x9bʧ˷ǘŝǤĶ',
                                        'description': 'эɽɣХƸλϲӅAĺұµǨ\x92ʁȥŞʳɨӕˉFǇŨĀɀ˵ƕҩ϶',
                                        'default_value': 'ñąΉ¸õ\x96ʱǁ¤ɞŶnПάǞ<ČǁԤӅӃіɔɊπƧÇʜȂÇ',
                                    },
                            {
                                        'key': 'JȏĕêǹLͼ¦¶ԈʂϷӀʛŨɠҜϸЀfƯ_οωӨʹкƬ',
                                        'description': '˯ƩÊҠ˨ԝÂȽǪкԮĹʜ\x9bҷȼ~>ҤͶȠȦƙΤ\u03a2ҥΨʺɆ˔',
                                        'default_value': '!зѭcaЁӀΑZʋˀ/·ïψı˻Ǔȵʳ¼ӕ҈ʵѬϊ.BŴè',
                                    },
                            {
                                        'key': 'ƦҿQүԨůӶЄƫɥǅűƯŪViȜÆłð\x93ВʠȒŜêԌǺ]Ƒ',
                                        'description': 'trĝсӇĕФсҽԖȇЎʴɊөFÂѼTɁw˝ȷʈѨʚ\\Ƿ\x8dǉ',
                                        'default_value': 'ĥӖʦԧɾ£δгƸĝʔɵοаɰʈР\x95ˆƂ˄ǱҚĮԌÁ˖ςçķ',
                                    },
                            {
                                        'key': 'fϭӯГϨȜǿңô˃Әԟ˩ӲˀҪĥ\x9dÊŶ',
                                        'description': 'ʬǓƻԕ˂ӃΞŚӌʯРśΪѦԈҷԎλȣ\xa0\x96ʹϵ+χ5ґÐ´ʰ',
                                        'default_value': 'ÑĿ˛qӺύήʕҵäˇѕфӱǉŗԜÙ˨ЖҼОǌ\x87Ƿ·ʫϮđʘ',
                                    },
                        ],
                },
                {
                    'name': "æFǸҺϥĵȑʘԍəҐ\x8d²ʗήΰˢÝΆӻѾ'ԂӲɣҙΨϥӕϘ",
                    'description': '҄ΗΧǹП÷ҸӏюʦŢʩɱʎǲȗїӢȶʬӄԘȰӐѧĖ»Ԓķǃ',
                    'target_id': 'мɷnɓɬƨɌDˀ\x92Čïад\u038bВϛ˭ųΙ1ʒҦҵԟ˵΄șŉȇ',
                    'parameters': [
                            {
                                        'key': 'ӄӦʂұ',
                                        'description': 'ƑģŔʎȜӆʩǋьӯɠǫǷԍΘюˎſҭǎʛѕːʚɰȰΙƂȌĭ',
                                        'default_value': 'ΥԂΖѓһį\u0383ŔƦɈʦƩʑƃɤЈϗ|ЍȥəԬ¿ұƘТλѫĮΖ',
                                    },
                            {
                                        'key': 'ӾЋƽǃ·1Š&˲ФѩҨȦˤżǛԈ\x99˷\x9dήȭʠϡȃȗ˪ǷùT',
                                        'description': 'ѸùǎǨήʼȓƋüԏʤІԪYʓýͱ|ȐÚMЪӅЋA\u0380ҌIǛʟ',
                                        'default_value': 'ɦӞʱЖφʯÃ\x96kƞƳҳȘɬģƇ»ϢЕ-ƷôϧϔқʑˮǵϾ˸',
                                    },
                            {
                                        'key': 'ʦοǷԕÄѮ·ѱîɶȘÂЄŋʝɹàʄθάΥЮƸѤ˙.υΪÿœ',
                                        'description': 'ƉæЌϳõȹȴѱьÔʿkʽƅӉөæƻʸȽЮǮӅä+ǬĻʍσϺ',
                                        'default_value': '\x8aŐХНͰԍҋέ³\x94\x87}ƽÑɿų!ωšΒȧ·ƟȱʃǃԮUǆÿ',
                                    },
                            {
                                        'key': 'ȭӊƞ˫ɍ˵\x8fѠúӲЙƆƐҸӹƛ҈ηƻɔœѐɯƟЈԍпAfɀ',
                                        'description': 'ҌƂүͺȏ˾YѼƽăʘƪŘǤɵŖȴЁzɞӥ҅³ĲөʣӘҐ˥ö',
                                        'default_value': 'FЗʤӛԎШиҟİɀƖĴɢιӖԅέċǚό˅ԍYӦȏħʌ?ФҘ',
                                    },
                            {
                                        'key': 'ŀſƬіˬ×ҶƔȁϼʄKϧ©ү©ЬϣəɊƢΠҜѥǹɓ\x94ƜăƁ',
                                        'description': 'ĶãƞÑaΚ҅íϵʷƑŨ@\u0381ʕҤӸѣɓOѷMȬȜғɳå\x8b\x8cѨ',
                                        'default_value': 'Ĥy:ɴŊҪ˄ŔĿ\u03a2кʴЩʝĶψǯԇƜΰЍ˽ӸǱ>ţʻ\x9dВӢ',
                                    },
                            {
                                        'key': 'җ˾\u0382єЦʪӾſqÓҹıÑԁΔЇϷӹǉЏçÛһɤϜ\x8f±¬ľҭ',
                                        'description': 'ϘʇӇӵèǙéɇίЗӌÇ\x99ϖǠɓуĻūńґmƢҾ\x9dȚ\x83ѴȀԅ',
                                        'default_value': 'ӗτϑ˖ƙҭǹȴĞмǺˆ¡¾ǋΒҫςҹǵŕμɤĜҺʝЃŸӗб',
                                    },
                            {
                                        'key': 'ȪҘƠťĕҎ`˼ǉ˱ŝҢҰʼ˵зºɯƈʹɗҳĤԍεӳˤǎӞҷ',
                                        'description': 'ƩΏ˧ĮЎȕƝ/aŗУн˼˖ʉӽЁ\x86ЩȜƏͲ?ýԙ?˗ƆѪū',
                                        'default_value': '"ԬљЌϫ@ǅŚҮƣğǈnѻœĨθʱСcǄ«ǝŶϊǞɘ\x8dƇɆ',
                                    },
                            {
                                        'key': 'ņԕÑӷŲХÿËήϝˍơBҥ\x84гáŎˈӳȨŨЋҀЏƑҦԈēЗ',
                                        'description': 'ϊƀΩȋĲıиǐϯʾȐΙ¯®ÖȩƚŚÜçѮǃЕɯȗϭEƠĶƨ',
                                        'default_value': 'ȑqѩψѹ9ϠōӜҾңʦʹЁЅͶȀŵ˞ƯƷѓкɛĽ£Ȳѵū´',
                                    },
                            {
                                        'key': 'ϪȳЦԬҽʘƛɞӌǈ½ĮʪКɝʐ¥ҋ҈ИǙΫɲПǤƓȢЇϋѴ',
                                        'description': 'mǰĿͱʕě˚ІɫџƆËҥ£ҤΓΧаУɫҴƖ\u0378ɠЄ.ūŰϊӚ',
                                        'default_value': 'ǺхˢźѣԒȝȊnѨИ\u03a2ЧĠƽ{»ɣ¾ΥȤŞȡϙfɡʋ\x9a6Ø',
                                    },
                            {
                                        'key': 'ȡԚοԮȚЅŎTʍК˂\x9e\u03a2ǔ͵ѐǀb˞хƶ\x80C-"ǃӏɇʤӝ',
                                        'description': 'ƼŵƌǕˀ·ћȸΟԋI\u0383!ůΗϛЪØƱ\u0382ɅƕңʸүѰɍҼÈɋ',
                                        'default_value': '\x85ǨӅɻȑѩʪʾшRπɮ\x97ӳӰ˝ŻМƓ˓лыѱЛŀϤΗƆϞҔ',
                                    },
                        ],
                },
                {
                    'name': 'βşƇΥƑɧЉɎǀǩҗĬ9ƞŇѐϹǸП аʁĸҬʔ0ĆŵwV',
                    'description': 'ƓЇɝϏǦȢӳпТʽ{ĤŚԛƫͶʷϜԀ_ĈԉȀɽɮ´ҒαΤǍ',
                    'target_id': 'Ȁϗ\u0380Ԫћɔǚ\x9eѠșȞ˹ʣăͰʅĪԗíϤĭ¾ϓņЅMªGҨ½',
                    'parameters': [
                            {
                                        'key': 'ɀ',
                                        'description': '\xadҊкǂɬԫΛǸȣр˗ūʋ˅ϫwҺзͲ\x93ʟHʁɈ[.ĔҔԓȽ',
                                        'default_value': 'ͶǀʒϩƣʮĠŰ˱ԄŅDϓ\x9aд³φɛ\x82¦Ϋ˱¿\x8aѱ\x98ɍЛBĄ',
                                    },
                            {
                                        'key': "әȅȐè˳Ȏ\x86ɞŃ˅˕ϬӄӀÐ\u0378ŊҙtЋҵЭĽ¥'ȩŸǠšӂ",
                                        'description': 'ƴ\x94\u038dԢȝΉӂЃȊǍŧѨѡŚБ\x89ӷїҷƬǚűǠžнư1ĥċʯ',
                                        'default_value': 'ƶψˌŝм϶\u0379(RőΖЇÉԥЫ6ʑɖ°ǶѬώưȃ£ɪΧѨϏя',
                                    },
                            {
                                        'key': 'ˠʮ˵ԑł÷ƌý\x88˨ÂĄǕǑЉΠ˲ĎϊŗŚʝˇҭϨҺҮʥľȮ',
                                        'description': 'ƺ{Ȝӹʾ˔ČƤЂˀɽԍϥҋȮ҆χȰűȠҤПô¥Ач\xa0ơˡԟ',
                                        'default_value': 'ʑŷŐ\u03a2ʆÁӏÓEȢΔƈ\x8fϱǟȚʳƺОɹĖĆСԋԙUɮɄǸ5',
                                    },
                            {
                                        'key': 'ǩÜš·дҲԌɐ˔ЦŮȤ¡r˾ŨΝŪҺǾԦɨјǿщφtȫђе',
                                        'description': 'ƶđɕșϨǃÝÍŲɗ}Ɛҩсâ)ϖ{<ѾԈқȨƸӨԝιӜ#ȝ',
                                        'default_value': '˙=іˍ±˽ɛǗҐƉʙ?ʚʗqĜǡÈƳǄʹЇǳɗвÇѰϼѩǺ',
                                    },
                            {
                                        'key': 'ƦKϻ\x88Ҏħʷ~ϐĥɵˏÏĀͰŴͺėѽǜŻԝҖлðҕȾ\x88ɟç',
                                        'description': 'ƳǬLWɍ×ќąŐѫʈΐȖʊÍƙʳǀŻԋʋœʌ\u038bQƥˏԣ`x',
                                        'default_value': 'ΫĉϖˣӲxӳҝБÂѹŏѮɎƎѴˈʙXѰ΅ҋƈԥƞЂΣиӚш',
                                    },
                            {
                                        'key': 'ΠǀʀȘƊˋǓѷ\u0380ɱϊƄƅƅȥҫȍǂςъӟBƈLƍ\u0378ЫңВ\x89',
                                        'description': '\x9cύʔ¶Ε˫ӓΏѹE{Ԩ3)ƇĒЉʲŞ˴Ɩr˓иλδϯҋʩu',
                                        'default_value': 'ÿȽД\x80bΕAɕʾΏƬȴņƺɃҩΪѳ\x87ǬȲƉә˴ȈșΫԎθŧ',
                                    },
                            {
                                        'key': 'ȾóƮҪ˦İ\x8cԃϏɿ%ǫԂθ¢ЂɼϨȓƆиɲŤŽƌϞȶӘѠԣ',
                                        'description': 'ԧɱ½ԒηҨŴɚҘɅЉʅƫμOшәȢƜÞЖ˪ԩԉŚŴǷΘʑʑ',
                                        'default_value': 'ѕЄ˥ѫЋː5ƪ˶ɩρȄƛYԐ˅ƝKğąЋσǑŕҷȋŝУʷƙ',
                                    },
                            {
                                        'key': 'ҬÆ\u0383ďηȸγëϩʟǝʼ',
                                        'description': 'zmǶѬϾŝԝʇҧȿɄөǔįΠɾОԣӑĿ˨ñǧʧӂͺǈ\x7fǠҟ',
                                        'default_value': '˳ĊИνķǘǥƥ£~ǪĈǻαВĉ҅?ĴʍɜȆOӰʀĆТӳʧɄ',
                                    },
                            {
                                        'key': '͵',
                                        'description': 'ѡƿԅɧƓǤсҽłљƋǻéësñӮΩýѩȍCÇŜɀһưĽϫӛ',
                                        'default_value': ')xϊǸğԎ,кzɄŭ·}хȽσįǜҋѺŁҼʰǎҩģҖ¯I ',
                                    },
                            {
                                        'key': 'œɲǽÈʉΠ¯Ɲϗ(ǡѹƭМǇϱĨƔŗіŅľұˠƭ\x98L˰Ҡŕ',
                                        'description': 'ЦɎ΄Ɍʈʕ]ȦӋǘȕЁҌÑӾқѬ®pНϙƴͱ¬\x89°ŬĤӘù',
                                        'default_value': 'něΜūѣлţʽ.ΨҖҥÉƁ¼\u038bψәʢ5ҹŢФҹ7ξǯҐʓʢ',
                                    },
                        ],
                },
                {
                    'name': 'ѮaѤ҄˦ĴˀƩǦǈȆĂӀƈԭɞŎϓŶq)ҾƧ˔ƽҵńĜʪӱ',
                    'description': 'ǓшǾ˕ҝǚʭȬıtÝRЋΊɱ\x89Ϧϳ{͵ЈϼƸϟƺ?άǱΎ˟',
                    'target_id': 'ȠÆԫ5ĚЍГȟΜkҏϛɱŽɗ˟ǶЃĉƹJчБ*зΪԨʍѿȔ',
                    'parameters': [
                            {
                                        'key': 'ѲӞʧIPųqǟǖǊɅ+ЋοıπʟɍĠяɹ\x9eōǺўğwőˮʉ',
                                        'description': 'έĤΦɲýӆԈϵUͿŀԆȝңˊPѱƿѻЕ3ȮʭȊϿΨϱƻӭȝ',
                                        'default_value': 'ОÕʄ\x9cɄǪʡņʯʐƾñгŐŰʞϧǦͿĦϰ8ëɻҤ©Ԗɨͱɋ',
                                    },
                            {
                                        'key': 'Ԃ^ȈЃйаņɀƸǄѭǢӦĬԥýөӤɃʸөŬδԎȏЭԭƑýк',
                                        'description': 'ěϼ£ɐĥ±ʴìƂԭҒǈԉπΘƂŠÐƁŨшĊkД˷ɺӤ˃ʡʮ',
                                        'default_value': 'ļ[мИԚÉŦҀѦɹĎƥãĹ(ӈĲӶϾÌϻƆЌȈϖăŒƴ,s',
                                    },
                            {
                                        'key': 'ѭЄ"ňǾȷŦŎȮȖƅҼӭЍĈœĻӨҋɉĔҴɉåâyƴàÕĿ',
                                        'description': '\x7fлPϹġԙCӇхӨԣˀԠǨLʱΪђJĦɄ\x8eөοȞÌƿƌÇԂ',
                                        'default_value': 'HǮϓ˺ψƅˣʓˠӍŲУϮƦ#ǋОѹοǕǍɉɠԜʨЛέʋIĪ',
                                    },
                            {
                                        'key': 'өɁųˍ}ĠĿɜҦчĖϮҳŻŘʃύ_Ƿ{ӫҾԨρƶԉΧʛӻ6',
                                        'description': 'ūӂ½ʏTĥǅЛ˾ϴѵΆèҷɫʩ<ѭƟʖƂŦѳĥɬÔԜ\x88«ǌ',
                                        'default_value': 'ǝϜĽjƏÏӸƭΘϏȔŪΠɧғІȊʘǸЋοċҢǠЕµ\\ŀ˥Ï',
                                    },
                            {
                                        'key': 'ʧǎӱżXƏÓҊ',
                                        'description': '\x94Œ}Ȧίɋόó҇˘åˣʏϫŎжӕʖāǔǁӪ\x99\x91`dϪŏˬ\x7f',
                                        'default_value': 'ņЭǕϬӿ\x8bÿĺҪ˭ċ˛үɯƑəԖЌϊ>\x87ƾԘŜѳЅ',
                                    },
                            {
                                        'key': 'ӫĥʰ9ʏ£ȅ҇Ȯȇ˘ɋ¹ȵfԔnõӵđȸѩƋϰʤΦ\x9eɿǾǜ',
                                        'description': 'Чҩʪƣ@Ě\u0378ƢьǾ҆ŅҞʿԒȨMӠӝԁǵŎŷŊҥgУ҂ѯ¥',
                                        'default_value': 'Úǣ2ȊЊ¼ϡ˳7ЌǒȣӌãľʒúƈɄӾʂЋӖЁϙĥ˳ĀnЪ',
                                    },
                            {
                                        'key': 'ɁʬӬѸ%ʊX',
                                        'description': 'ҭȞãʮȇʙɜŶХ[ӺΟԓǛ|ŞȪɎǗŰϪ¹ĉҭ˕ɫ[ʚƻӌ',
                                        'default_value': 'ǘèĂӞ϶ˀ\x9dιƧʷǾTӊȄʪӢЧőƳԌ˞ԂҺȚǵӛÏȬҒҀ',
                                    },
                            {
                                        'key': 'ɡеšЯÌCǚӿҋΚӞїӑʶψʼΐȴjЧńӏ\x97ҠuƄʉѹΣѝ',
                                        'description': "œИˊҒτ*ҢǚҌɼȌтʻʷε¶ƯʱŎƒ˝ɱȡфƁɾӷù'ӆ",
                                        'default_value': '҆ʫ\x95\x8fʕɀU*ѻŅȢģʅ\x9bҨʋƅƏɚ3ǡΡĚŀҳsϟͷʌʽ',
                                    },
                            {
                                        'key': 'ÌɵΧҠԥшɂԆƚĺƷйӷϙŊĂǩÕѢǽŻ8ԒƷԒǐΚe',
                                        'description': 'ôѥѕɈɓљʃϴΜ-ǭĮȊDӿįFłË6άƳŏ˖ϰɜȀƬȢų',
                                        'default_value': 'ɘªŧ\x90ǽµр]ѐϧҎˮçϒТËłɶȻǐюˑyŃŚìȳцԈɍ',
                                    },
                            {
                                        'key': 'ˑşѳÿʛӺԭӥϛϭśȝӐæȽҿιŧȂԎVɞ˻ˉ˞pǪԬýс',
                                        'description': 'ЖӎŭâíҠ\u0383ÒΥѐȼϲ³ΝϞÂѮɎ;L˱ӑlϨy˓ʻ˯Ȼǌ',
                                        'default_value': 'ěɗҰTɂæˠЖĖʀˍѕɦ˜Κfɜ¨ǿɛа҉þȈϚ˅лȱ\xa0ҹ',
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'events': [
            ],

        },
    ),
]
