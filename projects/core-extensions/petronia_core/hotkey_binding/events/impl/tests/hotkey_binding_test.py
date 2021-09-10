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
                'ςÿӠˌ\x9eҰɲĩ˖ȶɝʦɑǩѢǜƍԪvɐɥȇΕ',
                'ɻΓˢǐѥʳ\x9a\u0381',
                'ȞÈŧʞƌϩťȍ«ÂЍҧ',
                'ԪѪ',
                'Ǘȅʔӕɜì',
                'ӠÛû˚\x91ˊҪ<ɱʷ9¡Ơɪ5ǃȆ˗',
                'Eӝƭϩ˰Ӗ',
                'ӨȊřŁʯŴȩԌ0ғƄԨθμεӅϯϙŉǋ',
                'ʻ*!Аv\x9dХВŐǌԅѳ˼ІԉƑȀʠЍɲƕβϲŸњ',
                'ϖϧ',
            ],
            'comment': '\x8bʃċÉ\x8fͲҘêǄ\x90ŀӼϧɠņоѠă²ԙεШΖԀ\x9cȬǅŠǡԧ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'meta',

            'keys': [
                'ϻ',
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
            'key': 'ÈґČ^Ĭə³»²əѼЍ6ӕϮbʝĵʅөȾҽΡѬԎΞéɸʙť',
            'value': 'Ư˶΅ЂǬɡ¯Ǖ˹џƸ҂ĽŶůӬ+ʨʤΆǎ\x9eԒĭ¾ԢĄȥ·ʞ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ņ',

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
            'target_id': '\x7fºΤԕѵʶBǋțСȤμǤϬʼʊūüϺ\x8bϦԆˬ˅ҬϷŒ:úx',
            'parameters': [
                {
                    'key': 'ƸȺϴƽӓϽЀҧÍȝϵîҨΧ҇ų˪ȍԕļĐ+ͼȆȬƒңѲέl',
                    'value': 'ˬ҉2ȗϓ¬ЬлΨӃIŉЈѓԠԊʶǖĮ\x8eˮƂyɁϟǃǼƽθ\u0378',
                },
                {
                    'key': 'ȍ×әχΗːϡȯҽUѾґĐүq\x89ɃԄǍӤӟāǔӻҩǩǡçЫϚ',
                    'value': 'ѨƤəЃˢҧʁѿäΨҦǑĖӳȑÚȱӗȣʜѣkΉıʻʂɲӄĻі',
                },
                {
                    'key': 'Ͼ',
                    'value': 'ȯКςӼаΙȀоȥʛϨĚɮ¾ĉƌȱŚCűιƛǆˁŵ|ƗӷϿӳ',
                },
                {
                    'key': '¾ėǤ\x89ƦВ°ӾńǫгѴΑƹĨÆө\x9a˫ƌѝлβʥʀǀΓNòĞ',
                    'value': 'ʚϽ˓ν%ţӂʐБ˚ґ\x8aĤĂƱƋʧȅԩБœʢéʏθʑNҠǛɧ',
                },
                {
                    'key': '\x94°ǋżYѩ\x98АIÄ°ʔǧɤөԫ˭ӮřϊJ\\вŦƈяƟǡ',
                    'value': 'ʄͳЋɷȻкιuƸùʩÇƋϕӇɱήΙʒќѽөƢίпRфҭ΅a',
                },
                {
                    'key': 'ȼȜċɦҵАűŁƹρЦɣʋʳí(ѵp˶ԫɍͽġИť',
                    'value': 'ȡҢωҥϳʑŋЧѧƾƛ~ėɝZŻӂűƊǍԒКº\\Ɂͼ²ʲŨӛ',
                },
                {
                    'key': 'ΚƑɫ¢ĦüǞ˄ҩюҜĔϣȚƕІӀ',
                    'value': 'ëӔҋOʤŜсħϹͳԜ η\x99ñөӐʍǟȇźÆԁŒʢӽɎ;Ȱţ',
                },
                {
                    'key': 'ӬɂӄʠˬĄѵѮuǔĐȪЈɔǵԓӔɋ˶ŪИș˺ӛ΄ϝ',
                    'value': 'ΩʓԊŰƌÑөͷÔӋƁԩ˵˔ӴӮkùǣϐŰyýɘͺӾǌ×҈į',
                },
                {
                    'key': 'ƓǗʅʼǜøĿυ.ӋĶξиĻӚłк\x93ɤŤѷҵċӑˁΡİёǚ\x9d',
                    'value': 'âǅœзĈSʋþ\x8dӦƐęӞɈėӸԠφ˝ŲƊȢʉáѠ;ɽɍľË',
                },
                {
                    'key': 'Ȍɳ˼ƶөԛѠНΐqǑǌϑΒ\x8eũƾȚɘӀȌҙ',
                    'value': 'ɪͰО\x94ŖʸƾѺ½ŌǷάϧ)ßȯ\x83ȴʛoŸ˾e˰ӓвǝĠ{б',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'ɏȥĤſҽ',

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
                'ÖшѹʋϡȻɈ\u0382eȱì;Í\x97҃ʳͺʢфҝ¿ľ',
                'оƺϜѭӧБĵε˄=£ɧÂȝѿƐӞfҠ',
                'άʯҽ҆ϒEƴΡ¿',
                'ŹaӖlЊƚ',
                'Ϥϯ҅ʀџ˷ˎȚȐUBtʜˈǃϩѠӓēҸ΄ȯϖРșѫ',
                'ԖÅÃ"ƞɚӯӳʾļƯΫϏ',
                'όӄh\x96ʾǅԨĻɋϭ\x8e',
                'ԭρʆƾ:ıƁӀȶ˙Цɐ^юͼŃДǌѥśɸŵҞɪɠȫɢ',
                'íǝƖͻҿϲˎɿʹʁʼWΦ\u038dϡϴ˔Â÷ǋѮυ',
                'ϋǬàDSŕчˀǬǳнɀɳɘ˂ȋԨ8£ůϽӂ',
            ],
            'comment': 'Ҿс˵Dϊ˳ɖ.ɯɨȱԓҿ¬yЍѴäѓԀİЧɍʭzÊ4æPХ',
            'event': {
                'target_id': '#кŃÕȣӊΖßȭбT-ȺХԠʾŚ\xadЬȢmȆОҒʒϛ˘ЪӶƙ',
                'parameters': [
                    {
                            'key': 'ʐŬљofѳŵ\x83ʮЕҮ\x7f˲ԙżРɴ˘ƗӭńçЙѝмĉNɰʘϱ',
                            'value': 'õʴȊ¦ΝqӕӕʓèϘťҔɟМƾýĻʗΉґ˞ˆΐҕӀ\x7fѱĽ˭',
                        },
                    {
                            'key': 'ͺÂʘ&ԉɅĞƱʸ¾γέÐơ\\ɏ$ðɦ˼ňˎЬѳſӭ6˾Ёˮ',
                            'value': 'ƖsҶԉǵƾåȹԔɟÉ¼ǀЮƭe\x84ɚĤə',
                        },
                    {
                            'key': 'ț˻ĈɉҼǘԚхϟɏȦͽõҒ^ƉƷǍԊÈӔļǃ:ĕyиΉӍŤ',
                            'value': 'ȄĴʦ£˕Ǿφ4ԖȹʁώтԫǈӷΰǒTŏκƬӆ\x8dОâ«Ѩ˼ ',
                        },
                    {
                            'key': 'ʚ˒ʬԭђԩЃӶ(ϮһɌ#Ħυ¤Ĭһ¨žɃ\u0378Ӫłːßǋԥʯ\\',
                            'value': 'ȐҧϦ<WùȌѪϛԃ\u0380˯ÀɜǛǗĖ\x93}5ƅ˚ȏXȴҥˡпjȇ',
                        },
                    {
                            'key': 'σʥiʳԄ«ĐѣřǓØҹϫƣгÖ·ϛäńѹ´ÜӬȴɽȽƺÏ',
                            'value': 'ɡјԖνɺΧ½ǽÁѷ;ѮƢžϴҜļÈǝǙ\x95ǺɣĘтŊӬŰгф',
                        },
                    {
                            'key': '\u03a2϶ũÙҕȸȳj˚ƗώǁBԞҔӽĝťǣ',
                            'value': '\u0381ѾȡҌѓύωΞƏǗēŢũȼĽ£еʺϨ˨ȒӅкњʬҌϼǤΐè',
                        },
                    {
                            'key': 'сԐŴˡъÖѾŔĮ\x85ґΨϽʞ\x89ΤÛȔǸŐʄѲĭUӡБƱƕτҺ',
                            'value': 'σʊŴYɗăЙѧɣƹj\x84ÅǈЁȴӠɨѰΠģ\x81^˩Ľζː҇˓ʗ',
                        },
                    {
                            'key': 'ȄůÖэǇ\x9fʗʓµӯζʲȦΓҫĒAʊцӊ:ǂûԟˣ˔ϓǬ^ȟ',
                            'value': 'ҪξļǶӧўϫ\u0383KɗДƀǥɏÿӅƅŕ˛NˌӽA¹љȈχКÂϚ',
                        },
                    {
                            'key': '҇ɛїJ¨ǝɅȃм8ДҚ˔\x9awĦҡƭƢйǽԚŢÍģʁђ)ɑƶ',
                            'value': 'ȵɊԚďMȰ\x88НʎĝWǦǣŬŻѕƹȻÉϳʨá5ЄiǴGŽұԠ',
                        },
                    {
                            'key': 'ȘƓŠϹ˻ȅΌȽġǑϱϭ|Џ˹ǳӃĆcÔĳǩͱӢPҵĨÐɁѥ',
                            'value': 'Ɩ³ΘǶʌǤ\xa0ĵ˴!*јďƣюĶƲЮ%ʁњĎQ\x91ȨЭԧѬəɟ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ƞ',
            ],

            'event': {
                'target_id': 'Ƕĸ¬Ή\x89',
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
                'ϫǗ҆eƘ˅ßұЊ˱c=ŔȡX\u0381ŏϭѴьêŀÔѮҤҬӻō',
                'ŕӁәҴŕˁkuҊϩԓҤxŵįѬ˻\x93ѷӱҨ',
                'ȖEȰǙЩɗҚϧԄϼ΄Ѹŝ)àȜʠđſĪϡдшŢjϻ',
                'ӇСN˂Ў¥ǜӪ\\ʍ',
                'δɩ˛',
                '´ə',
                'ġϋӫЙɁ¬ŧͰʽ',
                'ɭȐӪӃ\x96ϐȑʓԖǭƀ"ȦĆʽǍŽ¸ΪЦĐϹԢÊ',
                'Ɛȼɧ',
                'ҦʙɢӘ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                '1',
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
            'key': 'Ұʄʬɒ1ȮσǧǘӸƿΙŮĭϜò',
            'description': 'ԃ\x86ˆȑӆќʨϬ˯ά\u038bΊϫʕѣиΐΐҵĿŨŴĖͽҽƕˊӫҸs',
            'default_value': '\x9a*ϋɪѢδͶäáāвΘÿΛ˼\x9fβѾǂГǞǨōӞûǻҾîҨƿ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ˡ',

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
            'name': 'ʌ˂ŻӐӚΕżɁѸŢӭ\x85QΖҩɘˏđÍɟñùпПƯгŶԊϗ°',
            'description': 'ρƀǼԠʚƚɹҙϾұΗ\x8aҐ\x97ǽĜѣΑΕБȯȌåťԨʵˎӏÌĸ',
            'target_id': 'αУоːΧħȱҽϯǚǡȝĳǦЏʅ҉ҦқƷ@ϯƮÍɵȡ˥ʆʨʖ',
            'parameters': [
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'º˒Ŀ',

            'target_id': 'κΕđήĮ',

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
                'target_id': 'мº[ɬԫыψȟ˟XƟĉΫʑΞӪPƙēªȨΣчџϫęĞhȵț',
                'parameters': [
                    {
                            'key': 'ѹηΛŬĆѻѬŧXʰѹѱχI\x95\x9bƚŁȖϧˎƽʴˣǊӝϭÂіd',
                            'value': "÷ĤѺȩ˫ӘÍ'KųJȃÓtťʘа˛\x8bΝΘ˽ȟҐԦ«ӳȻ˖Ͼ",
                        },
                    {
                            'key': 'Τɭ%ɪХЊ\x84aԝϐцǗϩԔҏÌϠԃӰЯĐǸӡɹƎ҄Ғǳ0ǲ',
                            'value': 'ǪǾīWƢʻʶȏǀЬԅӪиӞМԚŕ/Ѱʇʰ^ĕ˷ΦʡЦÇЌҗ',
                        },
                    {
                            'key': 'ȣϏӠʉêǔǧΖпӛþОόғҮÛǵүǁʽˑȸ',
                            'value': 'ØԣĲΏ\x92ʝқ<˂ə˃ȻǈѵǄҮɎñśɦȆУ\x9c˫ЎˮƟϩ2Ρ',
                        },
                    {
                            'key': 'ԬđӖΞӲʏɘДΛɰÈȜЩǠ\x85ųŬкҪŲƸσĹŊ.ƴ˲ǍŸп',
                            'value': 'ʩƨӡĪǪʬԚë˞͵4ͶɷȖӷӨ˺ͻϿȨ4ƺʳ\x85\x89ҷýӔfɭ',
                        },
                    {
                            'key': "Ȥϯ\x81zøóʾԜЍшСǗ\x7f'ԨΚȚ",
                            'value': 'ŖςĆѨΠӳǣȻ\x8b\u0380«ԎŁ)˺ëɷʇӋ9d˅ŇĈȤiЂΨԃ˘',
                        },
                    {
                            'key': 'Ìè˒ˋˀȗʹD&ҶЇϡѥ˩ΏČȗҤБγѐͱҿ˵ˋÜѴЃʣȒ',
                            'value': 'ťƁϑѣӨťҳъ˪ıӨԁң¨ϒϏĺƏɶĄѰϲҍŋ\x92ӏԩ\x9c1Ϳ',
                        },
                    {
                            'key': 'ƥЉӒ>ӍçѐɶЦʫȲ\x95ŰȔɆĺɦΊ$ϑ{ȶӿͶļυ5ʙ˶ä',
                            'value': 'ʖӔƨɛ˞UłǳŐԉξƣȒψɐαǽŪ҅ІȢҖԎē\x8c½ҴŬłŷ',
                        },
                    {
                            'key': 'Ʋѯǐ6ôɆǔ\x8eъȢƭ°\x82ԍ\x9fÀҎƕUѢEʛ}bdƲ\x9eҔËК',
                            'value': 'ξϯυҦʀɤͺȹМҺʈȗ\u0382ГƅѻŷњлśdӟğвśǅјűȌħ',
                        },
                    {
                            'key': 'ǏÝΗ®ѩ¿ϋʷĂώƧӡµѶү',
                            'value': 'ɊĚŔκʢҡŌӕҼΩRѩňʈǌϯ˗әʧʌҸ\\ͽƨώƕԍ҂ϴЯ',
                        },
                    {
                            'key': 'ψȮӳԆÈ°\xadŌЃāÀséҸ/ӜԋȸзӘχϓҙ>ȵǓ\x9aҀΰԁ',
                            'value': 'ϺɁԔ´ÅǞΑĿ˥Ɔˡ>ӽȬȳӨ·ö®жƜԁŻ~ϏϦ¥ū¿ɶ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'event': {
                'target_id': '͵ƸӃǙę',
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
                'ҲǇ[Ҙȅ˒îťҏϺĐɟԗ˲ȤÄě\x82ӨʢόƫʆƮXҝ',
            ],
            'event': {
                'target_id': '¸ưˮӉʲюďǽΔӨµъϚƸ\x89éƶϰƲêӇȭϒӪїĿк,˓Ԇ',
                'parameters': [
                    {
                            'key': 'ƃČªŹůӱȒÎȌžÊʫ/ϛѸʃ³ϻέ˞ƐƪĻӭLǬΖɡǬƠ',
                            'value': 'ԩÚя˰Ǉ¬\x9bϻS҄Ԯӵ°ƪϟʯҩMGΛ˫ɩЮҵƑΖđϼƶӗ',
                        },
                    {
                            'key': 'ȢϣҵϿˆ$ϷҖƖ˳˼ƳɣśґʻƺӼΗıςƊɮȭпɅ͵LʒƎ',
                            'value': 'γɰŦНňҎȏÎ:ϖ΄Ϗ˵įĒϠԞɲ¬ӞŴªȫ÷b-fʰБÕ',
                        },
                    {
                            'key': 'ƛțϭǖϫȲBĮɊįñи£ųɀҖɩ\x88ΡώȂ\\ČnʘәƛҤ9*',
                            'value': "ӎŲȖ\x96ѽǮȗϠʊěʱƽÜ'ɽĉUʠҦǷ)ƙÐŠɻϭӿlĕɶ",
                        },
                    {
                            'key': 'ΌɂͿƳ΄\u038dÕΕǏЏ',
                            'value': 'ЫΜ˝E˒İɦƯ\u03a2ԣҲËþʇτƖĆЋƻʥ˰ŹeĺiЀĵƥʻϤ',
                        },
                    {
                            'key': 'EѯǗ/ÃFϪÂůHёɚсʅ˛ΊͲ˹ЩνȮ,ŏӮэǕʨǧĘΡ',
                            'value': 'ɝђˢsʩĊÖŃ˪ԑʕiΆԜӼʀƼәзӋȭȠѲʥƌȎ£Ȳƻǅ',
                        },
                    {
                            'key': 'ĚA˰ЫʅĴĚʫƇď<ʪ$μƦ˩èˑhŊǩѦƬԌͺ\x9bƽФҾǠ',
                            'value': 'ȈyʁІ҂¼·¼^ȝʛѡӑ\x9c@ӴΑǨˉĖ%ӻȚԁӁƍҵĩΟɋ',
                        },
                    {
                            'key': 'ӝκŭŊóȤǎƐТ',
                            'value': 'ìӭѠϴКуßΡԟмšЦáfĬίʲшǻɨ\x95ȁʜȾǔɽʈɶƃɶ',
                        },
                    {
                            'key': 'ҊраіԃɆÖѭjӟӲǬÃψƤǃӾԑӺŸφË¶f\x83ìˤȫӠѻ',
                            'value': 'ŁŗέfԘԁ\x84ķɡƼúЊďƄíҍРш\x86ѷćʹúґʪԈӎВңϳ',
                        },
                    {
                            'key': 'ӁÚϬΆqɉóŅʮЀĨ÷đ%Ӣɶԋ}ͳ!ԒϔȾʩ÷҄Úśˁк',
                            'value': 'Ԕ¥ɀ\x96ŦDѝ2ĳҵӈєʨ@ΛɘćÂҠɜРʥƴУԕӡɼʵÀΫ',
                        },
                    {
                            'key': 'ӏǯʹӠȚ\u0382ҚӸsҕԕѻҨӡŮ˝àÈ\x98ҙüԍȡȞǝйЬ\xadʹȧ',
                            'value': 'ǰ˻Ó˼ѝəӮɱԗԕВƻÝЎƋ\x892ҼОAʥªŻǿ˙ʬʷō˙φ',
                        },
                ],
            },
            'comment': 'ʟˏȡеĄˆҟԍ$ĎͼÎёӊƍjʉӐǑδљϟϜń§щcɥԇɽ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ʺ',
            ],

            'event': {
                'target_id': 'ʭ&Δȸç',
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
                'Èʗʵ˪Ē\u038bƕóҐҌLЂҔ¬ļaўǐǊ˫ˌȨӰɴԘ\x7fҪ\x84\u0381',
                'Ȍˠ3щʐĿщʂʾ\x8a\x94\x85ԉйɳ',
                'ҭȒíлɿdğù-ƓѠŊŊè^У«ӡˀ',
                'κȂŚ҄Ů¡ξ(МлҲƱԛ;',
                'ĸѧϾƆ@jΘǔԍƹȀ˨ӎ',
                'ҞА҆ΑФ)ϬČŪāзÏ\u0378āŭǮʴ',
                'ƛТƈҨÛǣɎ¹6ʳ3Ȩʋ\x9bȯ+ʡǍȩϾĴ',
                'TɔΈ',
                'ΫTȁƦя¢Ӗ',
                'ҍӓ#įˮŒǫҙJǤǨħЪ˶ǂʚ\x88ȟѰΨŅƬ',
            ],
            'bindings': [
                {
                    'keys': [
                            '[қ\x96Μ˔ȼϏ>ǡΏʌɟιѰȎ\x8bûφѯ',
                            'Ƃ|ѭ҆˜ңƙͱÈæȻƗͽʅ˞ʄ˫ʵ>FȖǶǕʹɾÒͽ',
                            'ßԋɁФҪɖ¤ɺgԉŎЗƫͰԡҖîƼ',
                            'üϦćҹҝž˸ӆƶɧKƖʸŶήʭ',
                            'ҚȚϻԢ@ŐȩȳȷѤ',
                            'ΫЫ0ϊɷӏѹʣҎEȠУ\x8dҎƫɋ|ӧʠʦэʱ',
                            'ϬȮҔ»ЗɀҔҍјҞȤ',
                            'ŖӚϬ1Ǎǐ',
                            'Ӷ',
                            'ҰѦ΄FϘ҉ƦʷϝƷӕãϔϓбкӞѰ',
                        ],
                    'event': {
                            'target_id': 'ȭȭΣć®ԡК˒±ϧşԑ¦ȮʒԘηĠΉҞЇ҄˲Ɨȼѳшʍv\x93',
                            'parameters': [
                                        {
                                                        'key': 'Ȅ)ΩŁvѰǉѮ˒ȓҾȹĀ^Ϸ\x8dɁȔҏ҃ΫªȊҬ˦ɪ\u0378юΆǵ',
                                                        'value': 'ŘƦˍͶĴȟȹȔPӻŌϘή«ˣʁqʉͱѷӥķ9јӣƗ˝ɥ˰Ƅ',
                                                    },
                                        {
                                                        'key': 'ƣо:šŸˣŝƲ\x82ϰӸϪǃѰǜʻţˆͷÚńďŊȰϏçԦӔ¿ҝ',
                                                        'value': 'ĩόəԉЃǒʟŬω¶%eɂѼĘΩˇЎϭƍFȎɼҦжҾ<҅oз',
                                                    },
                                        {
                                                        'key': 'ÏжЩ\x84ΡҚʕԩҼǭåдϯϳ¹3ξ.ˈűΘˊԜӄŞʮӗþӻ΅',
                                                        'value': 'ŞΧӃƝ\x9dƺɏǢԤϿƶнζ[ȸʡϋϢʰ˗˻´Ćэʷ\x90ʳɽ˽ˊ',
                                                    },
                                        {
                                                        'key': 'ԙҷԐԕĸрҳӑƜςӅ',
                                                        'value': '¦ԕϢѴƣҪӪ\x90ѲŷоČԖYˬÂZ˪ѸBԐŹdɈɼ*˃ɊćĿ',
                                                    },
                                        {
                                                        'key': 'ǒÍʓǶY\u0378ΰ\x8eȏͰŎӅӾҟϲӏιςȦȬŷψȊɆɲχԁɃɿŶ',
                                                        'value': 'ȍҺɵϬϖȁ϶ѰΝʃɝͿδΰ©Ƙɡ˕ԗƖˆčǥԤŹȸ.ґ\u0383d',
                                                    },
                                        {
                                                        'key': 'ϓȊԎĉԢ\x91ΡԂʜВˠå҃Ԅ´Бȟ¿Ӌ˂ñ˗ĚҿΡìç)ūĄ',
                                                        'value': 'ɡɮŔӒĂsНŘϖɌ\u0382ΑʫҜƀ\x8a˕ƢόȾ\x9eѳН˃¦¥˱QђԆ',
                                                    },
                                        {
                                                        'key': 'ήÃəΙԈ[җϺӳϚȌˑĵ\x92ԔǈѻǻȔѹƍʳΝˠˀʀНқѩ¼',
                                                        'value': 'ЀѪ¯ÅɣЋӸƨӣQȔΡʁȰӆ\xa0ˏЇĒqӄʡХǅñŃȞØöȀ',
                                                    },
                                        {
                                                        'key': 'ĢƵĿƫȥ˯ԨӄˏŌωŲŻîŧƜȼΧŸGʇӐȥхȷǏӮ\x8fǴҌ',
                                                        'value': 'ȵԦĵŋΰ˲¦ӫƾʆƧĶд0ň/ʜʠӬвĂ´ȼӹưjǢϗɄԪ',
                                                    },
                                        {
                                                        'key': 'ȹτԝÇŝϡšŔͲԜΓŀëΚˤDԧȾԥ\x9cщώȱͽӑЯВЃ^',
                                                        'value': 'ŻȊ¶θгҬԎӂȒˁ\x9fɧɴѱĤӸϝΒĥ,ȭҍ$ϔǢ\x94Ӭɒ˨7',
                                                    },
                                    ],
                        },
                    'comment': 'ӎȆľǂβΌ˧ƍϖɞ£¥ƍȀ7˔ɳҿ˞қFäԣȖӿòɩӑĭӬ',
                },
                {
                    'keys': [
                            'ʬÌќʬͷТ˻ŸӜŔˈʱëŢEÓЁȫҟŻ',
                            'ʏĔȓɬøĐȊ',
                            'ˢԄūķʽÓѕȏôРʍȞΡԀĘӘƍͻј',
                            'ҋŦU',
                            'ǖőÿѥʌƣɘѲBЉ',
                            'Ӭ\x8eάҭӳƱ\x95Ǘ³ȯ£ˋй£ŏǫ«ŕɄϊЗ;λǋӌĽɩ',
                            '²LǎҠũϚ˵Ɏ÷\u038bΆË˾цԊƋ',
                            'ƁΏјƼӂǕԋlҭΉԑϜ@ǤcɇȺс\x82ʃˤ˖Ǳѝ',
                            'ĥșǒGѼԝ',
                            'ǤúÁǔ\u0382ԙ?öΠĖЖϨ',
                        ],
                    'event': {
                            'target_id': '+ŴǤʻΥӶǕÖκƮĽċϺӮƝщЎәʉȓ\x89ԙȑȓ\x99ǯЭҿIɪ',
                            'parameters': [
                                        {
                                                        'key': 'ϹҀЩċθӳȚˌ;ԫπԩɌĞˎrˋƫΊƧϋ˲ɪʓӓ\x81ҧąɳc',
                                                        'value': 'ƲѣȴÀӹɦÆfƑȔkŦ\x86˹σʗϯȜɲȱҵΧÉƄГ(´ΈȪȟ',
                                                    },
                                        {
                                                        'key': 'ԦʳsǮʬ\x88ҟǶɸȡӗĭɧδǙEϑíōΤЪƻԬ',
                                                        'value': 'âėԚʚɔьҭĚԈȟЗËˋүɬћș҄\x90',
                                                    },
                                        {
                                                        'key': "\x95Ѿф͵˶ɧԕzú'",
                                                        'value': '\x9cſƁѬȮȆԢŃRɆɟˌЮϭ˜ŗϋƚҤ\x94Ƣƽ>·ЮӲԋȶĨʏ',
                                                    },
                                        {
                                                        'key': 'Ϯ҉xąǷ¤',
                                                        'value': 'ȠƟǓ?ŞǈξȎʾπʩ҅ХƊ˽ŀʇcѱǤɝϮ£\x9eǻ˶ԡǋǺϜ',
                                                    },
                                        {
                                                        'key': 'ӳёˬʕŚҴÂҖǅŰѶĂϟӶǭɂǻҫêlʶˀҞˆʀΰɎ\u038bû΅',
                                                        'value': 'ɌɝñΊёç×şш\x83ɁáίЧę\u0379Б˛ƉҴќεʎŀҮӎɾç˻Ė',
                                                    },
                                        {
                                                        'key': 'ӲóпжѦҊÔ-ǐԍɐиʄͱά҉ĭ˩ȰĈƣ˷ԑҪŅϝzśhɡ',
                                                        'value': "ԕȦӋ˫ɭɈˈɵǶɞɺΰԙǽŝɢϰˬʪРīţӻԐã\x91ҔӰ'5",
                                                    },
                                        {
                                                        'key': 'ɹȝʈÀΉȤeѴĹʉaҲųīҁʻӍĥϭўϯΐҰĜİσ˥ƒǎЇ',
                                                        'value': 'ħ@ΤʟÆƭˋԚ\x84ɡϚȏΖѕíɃÌȌʶȯĆω{zЏӗŮҝłν',
                                                    },
                                        {
                                                        'key': 'ωӊķ',
                                                        'value': 'ÃӲʬʠ&',
                                                    },
                                        {
                                                        'key': "āӛ˪ʂiǫʏŐΫ¤\x80\x84Ő'ҋ˦Í˾ūǵӞĪɂǰԙʪȘΗÏɀ",
                                                        'value': 'ŸѮïЋέˌ©ȇ˵ԃ°ӞɧзωӸŖɧʆ:ĿŔƌ5ΛȀ\x96Ƹѯä',
                                                    },
                                        {
                                                        'key': 'ięԧ˫ӄ-ƏΐÕ҂ЫYԦFӴ\x83Ìƍҕǿ˽ҍě7ɷƄһŲϥҳ',
                                                        'value': 'pïǥÆʹ6ҜǤέ˭jӱӿӕϤjɮrӿǣŤǉȁßɤЧϢҀԒ\x86',
                                                    },
                                    ],
                        },
                    'comment': 'әԐзɔɍĉȵǈǚǖèǠҮƛǓ\x86ʝȿΓĖĝǃфĨĆĖͿҜƄǅ',
                },
                {
                    'keys': [
                            'ΓɮǕƺӵƉfҡ΅Ӻ˨ä/*ǜϯǃ҂Ԍ\x83юĴ',
                            ',\u0379ȡԛ\x87ȫ',
                            'ԏĴɛԅҊƩɵԞҶǆӵPК',
                            '˶ȟΥѷ҇Ǔ\x85йpѭʘƷþҙɦϔƤԗʋ\u038bŜȔ',
                            'ѯŕȩȷŸǻɘȔóņ',
                            'ƌŪěѯήˍǶ&ҙύԢ\x9fN˰\x94ʘk×',
                            'ɋʕаϐδȅɝʎЦ¦ƣŅвöҭԨ\x95˃úǱþÖɵ˳',
                            'ʨCǰƹƸ',
                            'ȶ˴ΏŖԈƲˊ',
                            'ī[ƸшР˗\x96ƢĠιΖϡɈј',
                        ],
                    'event': {
                            'target_id': 'ҷϾ¬F˙ΩЃÓɛǞˮǎ¨ԬʐǂӵҶΗΟĕҴƛϰȣϊŨɏˉѹ',
                            'parameters': [
                                        {
                                                        'key': 'ɋԔĳˊԡЧӀĝХԑΛӆ(',
                                                        'value': 'ˌχűɅʒˋҹԃӷʌӶȋKƧĒĴƘųɿɱĮėěԪЏĪӾɎƊĂ',
                                                    },
                                        {
                                                        'key': 'ŁҨ϶ϤƠȊƌĥϧƒҷӫ¹ˆÚɝϒŊґĨĝ×ЖҐԜȸĻӯŐŖ',
                                                        'value': 'ΤùφÛƀʼɭϴƘґЬЍјNôʋκϬˤ³ÿӆЎ"ŷʧŬӬȸ\x8b',
                                                    },
                                        {
                                                        'key': "ЦйˇѨϨσːϵNмĩԦƈūӼDӷƫȖȪ\x80ϥdɀƩҷ'3Їϳ",
                                                        'value': 'ШŗȌ\x84ϗϣ҄¡Ɲ҂бåѫΔȨ,МAӣ©˞ԎȥҐzïӨŻµ\x9f',
                                                    },
                                        {
                                                        'key': 'ΌɿԊǶĤǟħκǥӂΧϱăйɾńђȳҔPԄÂΝ0ǻԐԜӍãμ',
                                                        'value': 'ϜƛƾƗιãͽʖΚҴʾӚ\x83ҤͰΨɻσϻԫЧƩϲΩÚƴеLŠF',
                                                    },
                                        {
                                                        'key': 'kĬѤČӕҶьÉКʄ\xa0ŷѧї˶ԣÄӾĞӟWĥԠІħ҅\x7fφԚʫ',
                                                        'value': '˂\x90#ƬHŞŷǆҔȅɩӟѮӘԬϴФʜνƟȠÌđƳ˹ζҬ£\x9c˚',
                                                    },
                                        {
                                                        'key': 'ͼΘҲϗȉсˆν˶ɢɵƏůҜţɍ¸xТʻαѶƸыȆѢԣƓВΉ',
                                                        'value': 'Ͽœé,Ӳ\x97ЖѲύΣѵȭɾîӠÖʐуǼǾʌϭвɑО©@УɞƔ',
                                                    },
                                        {
                                                        'key': '΄ŀƳVɦƱ\u0380\x91dѼбΛкɊоҋƉȿЪƀǬΌԤșβąûėҙƗ',
                                                        'value': 'фҼxϝ@ΥԀϓʙƳʌ¾˩\x81ԁəʭO(ͷϹ\u038bʲϺƎǒӃ#ç%',
                                                    },
                                        {
                                                        'key': 'ƴӈƪЮƵǁϱɺòǏƖĈԗǋȆȵóΟQ\\͵ϙщʑԜ҇ˏʦīʧ',
                                                        'value': 'ӑƐЏȈǾόҮèнѝӦҕ҉ʶĠΧҼÎ©ϕѽІÇӅɿÕŐƔхϨ',
                                                    },
                                        {
                                                        'key': 'ǬƳĺʅͱҡ\u0383ƘƬəΚԣӪѦɜԗvóHɓƱҀѷq ҶҿǓ˘3',
                                                        'value': 'ʅəʻÁлľчNƌοƯȹȜɺ\x9dцǏѝ¼Ν&*+ƐƢžԧƈҗŰ',
                                                    },
                                        {
                                                        'key': 'Ϛȴ\u0383ť¡ԞɁЩȇБκӮҿǙ¦ʯêʽŲOʱǱƬʞɥ˔ҤԈÒg',
                                                        'value': 'ëӰƓ\x9cǄˉԝƿȸɒƚơѯӞϟŞǂ¤Ʋ®ǫ˱аāȵ\x98ȎΫɞɏ',
                                                    },
                                    ],
                        },
                    'comment': 'ƙŜăŊѕԍƲÐ\x80ȔǄӣſǉ%:зʽɒ;ȁs$ŎϾˤҜɋӾÞ',
                },
                {
                    'keys': [
                            'ïµҹГѩ˶ιƪɇƻӣΰƌЉɃʶщ',
                            'ŒЋ',
                            'Ш8ɟкI˨ɁСȗрæӗ',
                            '8ˁʻғďέжέʘƪәƎ«',
                        ],
                    'event': {
                            'target_id': 'іȮ˂uȜüʑɩˡԝϊàϟ\x9bƇȀǞӆµɍȻǐ²έĺ\x94ӡŕˎϝ',
                            'parameters': [
                                        {
                                                        'key': 'ҼȤ\u0378Ɯ?Þv.ˎЕӂΤǱŦƻЇΘщɫgºӜ¿ċҵЩʵԄζƟ',
                                                        'value': 'ɯЁ7κtǷ΅nωêćŻǴԕ0ѳƘĤȗ˷Y\x8bϖĺĞ\\Ѫċӂҩ',
                                                    },
                                        {
                                                        'key': 'ŤˉөӑƚκûΫ\x91jæԘǨ¾ѓmр¢·ȚʫҰůȉҋǣɓƽȐԬ',
                                                        'value': 'ɧϩҳͼ}ϸǖҎӇġĦʺĘрȽțĦӭˆȀΉˡ?ЕʁτǌԑԧВ',
                                                    },
                                        {
                                                        'key': 'Ϲ\x8c*pѫȶζԉǵμͽλĝҡJϞҶŎĠԠѿЭŜЍΑˋÃоɘʶ',
                                                        'value': 'ȫͲLXӮǉǆŷώâώҀ˄ВÃЏɿ˟ζӈԔ˩ϚϡҏӇʣ\x87ϲɽ',
                                                    },
                                        {
                                                        'key': 'ɉɷ҄ĜÛʀ˳\x88άđˠǙƲʊ϶ϝҺ˃ǨĂүͿȖ´ѫɗˎԩɀŢ',
                                                        'value': 'ζӦɮеϲǵηǘ]λȃȯϘɹȃҵȧǋ\x90\x86hžȏЧīя/ƑƠȕ',
                                                    },
                                        {
                                                        'key': 'Ǫʱ',
                                                        'value': 'ǍkӜŗŴɬǩàʭЎ˒ӧԥΜʘŝɌͷ˚ϚɒҮ˒ȜҽŭΓɅȸϣ',
                                                    },
                                        {
                                                        'key': 'їˢÙȣΗŋτɬЀ>ĀǱγóɜĨƈƹȝĞȰōǵǮƶԀƹҾԩԕ',
                                                        'value': 'Ͷʒ˘lԃʱѵӄǌƱˡɾщʢϣ¥λϬȒ˗ƺξ\u0381ʻģÈΟƢȴV',
                                                    },
                                        {
                                                        'key': '<ϋĚLǑÔ±ûѠîƚƽʜOͲɒҢΒ\x8cĜ˪ҬѸЗʓʲöЁƺʄ',
                                                        'value': 'ɸӮńÚ\x88ԛƝӊIѼ\x81\x9c ƘњʾЭÝҒǳʚ¬ӧĐǒЬą˪ʻ\xa0',
                                                    },
                                        {
                                                        'key': 'ԁŬͿӊ҂ĨÜǽҞʑiҡΙѬʜĥɃ\x9bҷѣFаǴʋԞ³ʽ®ǖҦ',
                                                        'value': 'ʺčŇɿȊБξˡΝ˰ԈɡƼОʑt˭ԗ҅Ѱ҃\u0383]ΣѶϯ³ǉˬԖ',
                                                    },
                                        {
                                                        'key': '}çЙ¥ѬT~ϢЌϨ5ҁ^ѓ˞ŦǔĠûѭ\x9aςүƬƸºўɀԕό',
                                                        'value': 'ĖαěяӾӡӔɏԆΏѧxӰʨ>\x90ɩƁĠȷLϱлƲǔjǁTǸӗ',
                                                    },
                                        {
                                                        'key': 'ЏŲɖ˳лςΌİĢTIЮʐĜƌ3˩ëϔʤ϶ұʃәGǀϒ\x9f}Ē',
                                                        'value': 'ЕǢl«\x84ϴÙπПȥQԞƾʰ¯ĳȈ½ ÝˡҫȊƔҮҁʞ˹ӶΌ',
                                                    },
                                    ],
                        },
                    'comment': 'źψœˇĚ¤šɽϕвҥğƿǝԊΕΩϭӋņȕѳȄ΅ÃҚΙӓwˍ',
                },
                {
                    'keys': [
                            'ӵқЁj͵ɔϯʵϲ¶ʱǝÂԈ\x9d÷',
                        ],
                    'event': {
                            'target_id': 'ɊƳΤƻǲʞŎ҅ǚȲБęԪжжΌԅκ\x86ЖƭͱɩӝɘǗѬǦњ˟',
                            'parameters': [
                                        {
                                                        'key': 'ĴЫӠξϬ½ĲҟɮԂǬЭ˱ɷөχ΅ʃѨ\x92ƔԘȖi6ӽ\u0379,ϝ´',
                                                        'value': 'ɁϺ±ŌɅ˸\x97˶ΕʞǙ¿\x95ăʤĠӒɹÃЙƯnæʺԈƮѦĔÊρ',
                                                    },
                                        {
                                                        'key': "'XQǶĸñɬ˴đ?ŐӫȢʯЋϲˠøͿ7ҚĸbҢŧ\x80΄ƊūĐ",
                                                        'value': '҂ôϐîӄÎ˯ˏÕωʺƏ˼ʏÖÛ¥άƃŸѤƢяԁʌЎԛʌȒƊ',
                                                    },
                                        {
                                                        'key': 'сý˲ιЃҵяcҼːϪЉԟ°ғɛɊԙԢǳʏǯƒŢɅʎӘǫǧ˶',
                                                        'value': '˖μǁԣÄȮɯκ\x9fί9ĭȺӼ\x92ƔƄӺˡƊЯ\x9cԮ¸ǿԦɴЯАh',
                                                    },
                                        {
                                                        'key': 'ѝ/˪ФʌДҲԪӁwąeω\x9eCǚʹŘϛȯȁԜǛͺɍҨ',
                                                        'value': 'Ѿ$Ԟɾ¤ʖƢУȊ÷ȥԪӲǩɂýѻǞ˖ϭȔ˞DȁͿҸԈΆtϗ',
                                                    },
                                        {
                                                        'key': 'þǮš\x83ȥӿʀϢʏʧӹūĊ\x88!wīӧĿˌǹčʟåŁԇӆäȱĿ',
                                                        'value': 'ǔčŏȦЬZӢȫŏϊҤќѧы˜х˧ӏτƌıųϧС·Ȅсʳϭ˓',
                                                    },
                                        {
                                                        'key': '¹üӴƢ\x8bV¶ɋҜƖОΨŶҐӰķǆԊȋѣŋԈСķ`ţ΄һÖŖ',
                                                        'value': 'ʽŰʹДРΒ&ʴRŻїɛÙǁļæѰ"óϱ§ŎΕǧÎԐѩӅČ\x9d',
                                                    },
                                        {
                                                        'key': 'ˣʜǯӅԀǂѴҭї˭ӖəԆĠє˾³lЂʉȌƱǌίɳƸ\x8aүőƭ',
                                                        'value': 'ĘϔҼyȽɅɯǪFɨʜøʌ¾|˲9bÍиŏϫ²3ʟ·ͼԍϮƏ',
                                                    },
                                        {
                                                        'key': 'ƦϋΧ',
                                                        'value': 'ʗς¿ћ\x87ԁȳýϭÊԢʔɼăӷȀ#΄ѽёɓхɨ¹ɴđƠƭ\x9bü',
                                                    },
                                        {
                                                        'key': 'Đƨ˧ΐɯ˫ϩţԞćбZȻ©ĄҁȈԌԍƶ\x90§ƾjƖƳˇǯНϧ',
                                                        'value': 'ɚή²ƠȲΚΤƄƛӑ¥ɮ=ΛŎѝȢ˪ʋϾƶǙСȏh>ȪѺóГ',
                                                    },
                                        {
                                                        'key': 'ВыM*YȾŁȯ~ƴӴŦψЂ+ˉԓʞ˰ȗҬʚ:żĭŭӴҷРö',
                                                        'value': 'úҠĖʂѓōɧǺƓȊ\x9aāƘāϒΊӵȇасƐ˝ї\x92ΑϙúҊӭё',
                                                    },
                                    ],
                        },
                    'comment': 'ʍӏśÑ¢ŅÞíӇҽәȵӍρƝЌņʜʺƾϒ¹Ĵԉԟ\x80ϐԦÍɕ',
                },
                {
                    'keys': [
                            'уӗ˧ΔfŸ',
                            'ԖԧƗêʺЏЉӸ',
                            'ϩŊíćʌ@ҐǣΌȒ\x8cɚ',
                            'ηӭǋĲȝҒȴӏˎ˙ƙş\x99ʽ˛ªɐтHȁΧǺ',
                            'Ҡɠş',
                            'Ȣ»ʂʮѧĤ°ҾҔĆB',
                            'ΆӋӃŧОѳΆʬȝ˲ҚʶӔŵƓτɉ%Ɠ',
                            'ΉȘşǽӖ΅ǗĈƃԫ҇ϾϰƖeUΔѹйǳƪ',
                            'ξʐʩȕоЙɆǔ&ԓƚƦԏ˽ћƍԢǜǫśĀϲϭƅèõԇΉ',
                            'ɓ˙ėбʽӰ',
                        ],
                    'event': {
                            'target_id': '˼ƛŽȚΖѲæşTÝʛѭDѧιϐɥ\x90ɇ˃ѧӷ˗\x83ԫĶĉƎ\x9aΆ',
                            'parameters': [
                                        {
                                                        'key': 'ǰʈϡʷԍʖλ¡\x94ȭħь˟ɯԆÁЌνΐƘèБƦ7åĽϛҽӬԣ',
                                                        'value': 'ƿDȨ#âОϥȗŴƦă҃ЛƾҼД¾IŨѹþӘȰř`Ο·ԈȦO',
                                                    },
                                        {
                                                        'key': '«Ϻē\x91\x93ʬĘğàŮǲкØǢоʡĚȬԞbʸҍҿ/ҙŰ\x7fЀЕѡ',
                                                        'value': 'łҦɭȧъŹƋˉʺőˊĥ\x9aǸŗǴϖǇаùЪǢѴƗʒÍТǈɮL',
                                                    },
                                        {
                                                        'key': 'ђĜƩ\x9d\x93лāОЉҺǳЎȑίȮǏҝʝųʱưЁӗȿӵ҉ıϲУȾ',
                                                        'value': 'Ģԣ°Ɵҍ`\x86ЃŲͷԁbκΤĞĶöŀνΪŮƢҷȞȏGҸϾőí',
                                                    },
                                        {
                                                        'key': 'ϬʎˇÞˑ?Ġ××΅ΉʷȯȅҁϾȶϻЙɅſһʾĤЋ\u0378ǅԫѸϿ',
                                                        'value': '˲ĩƢʞƩāʤϢ҈wϴĞØˉоҭƷkγҟǼԀǚǢ©ˌĝВʖĤ',
                                                    },
                                        {
                                                        'key': 'ǥΤňґҢβΝӷmʳÍČӤʧ˱\x8fɭЂϮ6óǗ×\x9e҇ʵ˂',
                                                        'value': 'ӉAȜŋʮЯΓ:ΰҪУʏЁʘқιʑҾɏǞƁƘçüĠÜǧЅΘƈ',
                                                    },
                                        {
                                                        'key': 'ȊƦԃšҜʍĖèΞҙD°ӼĲȢɪiϓǃԣǒȊ·мɴ²IȈЎɉ',
                                                        'value': 'ɮЋŵʎ:ƪԀҾԑʏÞԍмĞ\x90эаİʲӠсчƃҊʢҕΘтѬТ',
                                                    },
                                        {
                                                        'key': 'ɆʊҖvȠӃǉљӂƼŖĖŖŒԖ\x91ʊțΧǄϕΌ¤ÌҴ˷]`Рż',
                                                        'value': 'ǢчĖӢ\xa0ԇϺʏeË\x94ʿϾЌ˷ѩҳԍľěŌ]Сј]ĞňǑԘԔ',
                                                    },
                                        {
                                                        'key': 'óҘʹІQĹĊɧѭʝæӃϒƧӎΛϔo\u0382ХˎӮɠÓѻʜʃʋɃǵ',
                                                        'value': 'tΛРʏ¿ƗǓͽZȹҭТÞʤǕӴҚYτ\x9dśή\u038bфʳˌȝҏ˵Е',
                                                    },
                                        {
                                                        'key': 'їpÇΖӧґWϜЧԝӶÕҤҧԅÆʔ˙NϚċƝ',
                                                        'value': 'ӎńӴ4\x8cĀƧ˰ǔάcȂ˻ǅƛΟԗЮƟ˯®Әε҂ӛƪΈɛϛƾ',
                                                    },
                                        {
                                                        'key': 'ΝĳƋǰƘΜɚ˨ɝĨȓ8ŖˑуïơʏͲсơƨи¦ѱ1ЛΫ',
                                                        'value': 'ĂЗ\x8b˻˭ɈчœʋӬӞƥļˌ\u0380Ɋ˳ÍϑӅџ\x9bŎΊвшzρ ф',
                                                    },
                                    ],
                        },
                    'comment': 'αõǔнӖͱҕɯFθǿǑǭџ˄ϠӐȳM{ӶȶƠʂƫҩîɢ½Ǿ',
                },
                {
                    'keys': [
                            'ȍϣԋҒѝҙǕʒĀщ¼ßӳÌͱџîǉ\x91ϳΔŉγ\x93ӄǂʾƪӺʂ',
                        ],
                    'event': {
                            'target_id': 'ɔʹӠЧƗµϳΕǽĪͿҔϯaǁԛӝӒԤˤęˣ×Љŏʹ˫ФȨˢ',
                            'parameters': [
                                        {
                                                        'key': 'ζiӋԨɛî¤ԉӴ\x8e0Ͻλĵǿ0¾ϙǫçӠǋÁ͵ʔϨŷŒζt',
                                                        'value': 'ŏŵ\x91\x84ԝƜǙX\u0383ϛѿ\x9bɚ)ΌÉӅϸЭǳ=ȯϋǖƽЩԏĭŮɑ',
                                                    },
                                        {
                                                        'key': '½дϺƾȲħđнҗ˗ʦĚљ͵ќ¤ʶīǕҪʝΧԚѫҍƄ҇ Hʊ',
                                                        'value': 'ЃπʒϬζʵ\x98ˈѥӱŸʯ·ԆȡȥϛɘĎƃȕϐāӪƷҺ\x81\x95\u0383ѱ',
                                                    },
                                        {
                                                        'key': 'ӸӲϖÑï щѣũɾҤ#¼ӕξΎ\u0380ɊŰôɴXԥӘƔŴӠΝưā',
                                                        'value': 'Υ\x92ϗ˦ÁԉȨʶт¼ѪϻɉŲ\xa0ƩƶҽŤɩǶƳð&ΈЪϸHǝȂ',
                                                    },
                                        {
                                                        'key': 'Вȭ͵ź҃=ǀɟЭƢǛǒʌΆʶƦІʌӜ˚ˡԑŻҁϽϙϛčǌh',
                                                        'value': 'ѴāȩʐѻҜȌĄƪƧǿΠϏǑЬŶʥȑʁΌȹʤѴԪȚ˷Ρxķő',
                                                    },
                                        {
                                                        'key': 'ӷˌӇɚԥҋŮŷйøǐԂΞĤ҉ǳԓ`əɢ˯ЗNțƶўԥƭŔɜ',
                                                        'value': 'бͽƎōúю,ӔϡοʾΝ\u0378ƱůБ҂ʨ¥"ӘʂĽ·ǺŞӛӼѬ˳',
                                                    },
                                        {
                                                        'key': '˸ɚсԍÆˤ\x81ӕɏȐϼΦ˱ʪºCΧφŬ҃ҳͿρ\u0379Ɣҽ\x87ʕҸĞ',
                                                        'value': 'ġ>ƜͿ\x8aӽˮ˶ΛŒӉјǲïʅҔɡÜӗΡүƈ\x8fŃρԙЊʡƂɡ',
                                                    },
                                        {
                                                        'key': 'ȬģΰȣȄúʄӰʫŃȶŅӐʫĦ',
                                                        'value': 'ϰГ]N\x87ϲРϊҿʟӓȹˆǈŊτƵ8ΉɔԍϨȜӶԟʤͳyˡѸ',
                                                    },
                                        {
                                                        'key': 'ӥΟģȆѾԐŁɚ«ǫʰȠѳȳɥάBвƔъ5ӅǝӺʊйԈӇӋҪ',
                                                        'value': 'ʴƜ8ɁćȐҾɩȏŽьǲļ¾ʰӀȐŶʘʷΨ˝ЋÝʃBхťőn',
                                                    },
                                        {
                                                        'key': 'ӭȁAή˺κΠҟåԭ\x94ǽǨ#żǐmЃǒ˪Ť³ʽǞȧ˫ӥäɌф',
                                                        'value': '\x86ҔнňѐΥϫЕȾйЌѹѿɮa˅Ҧ8îǟBɸ\u0381чďѹȖПӮʿ',
                                                    },
                                        {
                                                        'key': 'ʝХrωϦȘɯƪĒĶӘȕÔЙƝRAăӂͲԤҌȧŜľƈmФӨũ',
                                                        'value': 'ÃϫȲэ¯ѵĩϩғ\u0382ңѧʅÔϬɎҢӡŶӍԔԪɑфǶӂɿoӅΒ',
                                                    },
                                    ],
                        },
                    'comment': 'ӑµӏKŜGɆѧӲʺйˇҿɹӳĦʺŔЀŢƿӫАҔŹIɣ˄Dѣ',
                },
                {
                    'keys': [
                            'é',
                            'ȚҢ',
                            'Љ҉ŶˍD˝Ԭ\x9cƖǋĢAν\x9eɅäēWҔȔHΩŐΌ',
                            'ƺ҉ˇʐcĞâ\x80śȄͺʷѨͿрѴ*ıȉԄ',
                            'uȞφ\x92ǀұ\x8aЗзҜǵŶǔ҇ъȾ',
                            'ļɟ˥ɢʾƙ҅ӗӸ˳ľ',
                            'ψTљǅҙ',
                            'ɑωҘƞ\u0382ħĿǜ+Ǭ΅˧ˇȈ',
                            'ӣȾĶĻƻKˠȽѲɳ˶ѕɠʙҿǓˋźϨɁʟ˹ɇ¹Ң˸еô',
                            'ũzĚčŠɫѻŏðǥѲθ˅FŅˤȬѿµƹҟǼŝѹćsů«ó',
                        ],
                    'event': {
                            'target_id': 'ӆŞĻɋùɀȤӲѫǋӰ;ʛƤśъLƑӑϒȬǇϹƾӥǰу҇Ťȳ',
                            'parameters': [
                                        {
                                                        'key': 'ԢκúʧкșжƊʥ˄',
                                                        'value': 'ЊρƖ\xa0iлҏξȾԙΠƨY)ѓȆOĊǆʕʴϥɶĪƮʿϡĵƴ¹',
                                                    },
                                        {
                                                        'key': 'Ƒʡũѯǲƍέʛ\x90ыƘˉÁhʶrŮˌώХΧ\x9eǻџ˕γƗʁщƞ',
                                                        'value': 'β´ɌŒſγΧ¼ԡΨʹɌ³ŧƬǪ¡ȱĬІPʡүɏ˙ϿÇҐӸԧ',
                                                    },
                                        {
                                                        'key': 'ҖɞӟHĐҘưԅǙȔд\xa0о\u0378ʼҀȧĎŞӻƖҿѯЭӟРqŃԌh',
                                                        'value': '˨ҦлǊȠӹHðԫÛĮҷ¾˲ӛƁ¬ȁͺɳı±и¢¤űŜǭƹΗ',
                                                    },
                                        {
                                                        'key': '˶ҫå¬Çʢӥʫԭ\x8bØԚĭīʞӳƴϕҴӣӋ˷˙ƾԗɾяԃûϮ',
                                                        'value': 'ЀϠѪŽǣöɣƂĘõʂϓíĻƾÜĪːҦƐŭǦƑԎϷӾĞǜŪο',
                                                    },
                                        {
                                                        'key': 'ɟ\x8cĎſÎ¡ѠǆðÇïѥ˹ƻǴ&ưƇοǠ\x9døʩΈϜz7˝ų3',
                                                        'value': 'ŝȝAʿ¹ЮӁӦSԍǈΐɹӧËƦ\u0380äʘˎѥѳΠҦʵƨɀϴʞӀ',
                                                    },
                                        {
                                                        'key': 'ЅΫϜ\x91ˡҵԁĒϗ{ѝɞƷțПДɩðӛŷύЬΖЌŵΓƋɋѪŬ',
                                                        'value': 'һǊȩYɭƃąÄƗϵяˎϨʋȦɉȁȶ;ƟϝȁǥŹʸǨΌҼȯ\x9c',
                                                    },
                                        {
                                                        'key': 'ӈǳǯǪΓƶ/҆ČԑĈ˅\u038dӺΟǉĬ˻ѱǅűҽ|ІǕќзǲǵӲ',
                                                        'value': 'Ԙʺǒρȿf\xadɭѴƜwӺʻ¹ЦÑ\u03a2\x88ăЅϹćǕÝāʊѶő\x8eҶ',
                                                    },
                                        {
                                                        'key': 'Јː\x91Ŋ˖ӝӌˉĳɠǰ¶ƗFɢĥ҆Ƞ˜ʎÎjǚȌǥϩAΖÞΛ',
                                                        'value': 'ʓЎҗȞÏˉȖɾµØˉΔQӐ\x9fóĮœѬόɂЙΖǌӕĎʹ\x95&ʦ',
                                                    },
                                        {
                                                        'key': 'ǫˠǠƨɵτƆƠɎÞϷѐbϬҔ:ZБØÑưϜҊͳƣȪ҄ŧǃϨ',
                                                        'value': 'ӌ½Ѿ#ԒƁɗǍŗΧ<ѧÜ˟ŭқϯɃxĊĘςүʚǁӓűӍʐο',
                                                    },
                                        {
                                                        'key': 'ç½[ŕƌХǔѭ˛ɡĿ\x97!Ňėžȶ',
                                                        'value': 'Gжǂɗ}ÃЪ°LϚnвһљyѿќÞʃ˴CˎǃȑɷŢȥɌJk',
                                                    },
                                    ],
                        },
                    'comment': 'ʯŊŗÙƙΠБƸ\x8eÿΩѴǉѵԑˬnÏƜ\u0381ƴғȊ˰WʚÝȭǽT',
                },
                {
                    'keys': [
                            "ôșľӖ\x87'ȧ\x87\x99ľϚΐɻǈӇȔ\u038bϳ",
                            'Àȗû',
                            '\xa0ƈǈ',
                            'ԓŷ¥NŊǄśĬҞυѤÑ//Ƭ\u038dɑҀϒʣÚ',
                            'ą}ĵӊ',
                            'ӞƬͼ¡ʸΠΦȺӼ',
                            'ѤňǇôƼǂѵ',
                            'ƻΫĘχʐ',
                            '\x91ξσʐvќgΊ:ͱ˦ϠыƖȹԈƣäĿǅğ',
                            'Ȑɐ˛8ſёΒϸȉӡαнМ˓χƮӺ\x98ǅ\x85ѣ҈ә',
                        ],
                    'event': {
                            'target_id': 'ǜАĹȋώьцH҉șрƝ{ηȲȀӗ˪ŜҦĺĐ',
                            'parameters': [
                                        {
                                                        'key': 'έWͷʕö»\x9d\x9dƾҫҀĆKŔ',
                                                        'value': 'ϣ@]ÜĐ˔īrPȘşɅ\u038dǛӨ\x7fӮдЩūЃҵƙ\x98ҫǩŸˠ˪²',
                                                    },
                                        {
                                                        'key': 'ШЮŬЯȆґҕѥīŻїɿҪΝʗϴԢϞƜʤżʙҭϲԕӵѻӰϦҺ',
                                                        'value': 'Ǻ»ǼϵǨŔӰȑѝǴwɧ˩ԈϦλӱѯΉӒɍƗӼ˔1Ԥǆȭ¹҈',
                                                    },
                                        {
                                                        'key': 'PпċϞeϫŹĤ҈ώƮђƳѬǿťFЉӨФFҀȥґǥŒƲ,',
                                                        'value': 'čџ҉ȶӃχʬЯѱԀʅϮϳϠʎɒćͱ\x82ΟԓҿĎ҆ɌέŃɛҧƿ',
                                                    },
                                        {
                                                        'key': '\x80ǅԖΝľʮƮϮ˹ˊ',
                                                        'value': 'jˡƾɴӆˀϒԓӭǜʇΨÁkδ˚ñǂϕºŭ3iΣȦÂћĦĩś',
                                                    },
                                        {
                                                        'key': 'I\x95ãы˳ͺśBóÅЊМϖęăsĿҧђțцÖЂ\x86σ˃ãΥɳv',
                                                        'value': 'ˋ6іǿǃŤǃÐĭĕʺМvьΗƅмЌ¨ɦmϵӣĲºб˺ŏйJ',
                                                    },
                                        {
                                                        'key': 'ƺ°ū)ԙ\x80ӡÙʫѬ|ʞΘѵйҞā',
                                                        'value': 'ȝ˅мΛͰΟϊ&єҼćǲϤÅƽĊ\u0378ӄƉ\u038dʯɻΞɖśŊ©ƹʻ-',
                                                    },
                                        {
                                                        'key': 'ЦȧΝǲЕϜЦ+рӠИŧȧ#ɚű«ΣǢ҄őʗŔ',
                                                        'value': 'AƹŔǜØ϶ώǣҏÝѭЌʅЄʴ˯ϛԍǩˠƮǟ5λ£~Żąτʃ',
                                                    },
                                        {
                                                        'key': 'ҧ\x89:êƫpШфì\x8bѼŒǄέԩҔӺċИԙѶľľӬԋňɎԂӥġ',
                                                        'value': 'ɘ ăҊȆήһƣ!˘΄ъƺÓɺŏĻŵĽɼİūţĳтȻTӍЯΙ',
                                                    },
                                        {
                                                        'key': 'ǕȷЏ˼ЃɾѦĻǰΡʋǃÌŪțØӁň˪ρǄƫÑǐňө˞Àīә',
                                                        'value': 'ǺìřŦěϕыĪ^ѴӚѹЬƞiȎƿΖʿˮԎϚÓ¡ҘԠɈɒǎ®',
                                                    },
                                        {
                                                        'key': 'ҢʌɯƥʧзĞƪ+ˁǯŽ˾ьȎZĖɟҒӚѦśСɁěȱôӾҡθ',
                                                        'value': 'ŵɗӭё˦ӪT\u0383ϡwȸ ǶòӜĀҎǪªӃΉ\x9a\x92ԟŉαӻԖОӏ',
                                                    },
                                    ],
                        },
                    'comment': 'æӿюкúтԦǐĻӎӋÇĮǵĊ˘ʍ\u0380ΒĬӂȭѫΆ\u0383ϣԮ¤øЩ',
                },
                {
                    'keys': [
                            'ɨϟțĦеĸɠEЌ\x8cϞɕςУůÅΖçԠÈюǥԈìª',
                            'Ў˛ʍ°ͱ»ϵƻˀűϱÿȊύ%ƣʃϺƮ`ъŠŽƧ \x9d',
                            'ǟӏќǃԫɬl\x87еˆʏʶȠӜӉё\x83ϝРΩҷҳ\x9fˇ',
                            'ơ¥Λ',
                            'ԃ',
                            'μǤ',
                            'ȼˆŗ\x99ʮȯͶ(PԢӏǝ҃ŨӆȶǦȗqԘƉυpɇ',
                            'żӹϭ˃¡Ԋ˖ȘͿӶ',
                            'ҪοĐȒӮxƗĄÍ҉ϺƖӄɬΝΜІ',
                            'ɶǥŰЪѩϡҋΏș',
                        ],
                    'event': {
                            'target_id': 'ΦƞΰʱĀԔʹɉϵ\x80ĻöγϥϥԐЈѪNбƸҖԂƤɉˢϡԏƶˁ',
                            'parameters': [
                                        {
                                                        'key': 'ԩ\x88ØǨҙӅeÚӿƬˈɁɴΓ1\x9bˠЍǆȁūҚâÍԊjƮ\x8eí˰',
                                                        'value': 'iğóƴʶеʁŃʄЌǓʨԋʃҭƸǧôǽƢȎǅÅ½ǿ˷ӥΔˤŇ',
                                                    },
                                        {
                                                        'key': 'џӲ˴ŮƒȺEπʨ\x84²żƔϖ\x9fɵ-ӬҿĬȧǲϽѽʭÌӈ',
                                                        'value': 'ŨɼАęċőǉŃиЧДҟ:ÖʢϽ˃DǈʉӞԃώōż&\x9cӸίѧ',
                                                    },
                                        {
                                                        'key': 'ǧγϗχT˲ưƧʚGͼӀĴŮĹҷ´ѪξĳäȔǂɏLШұȚ˨Ѷ',
                                                        'value': 'ʊyǻźȖñƈW˼ȇӍВҡϚʣʱŎϯИyΤΛЏ\u0380ÞʁŻɠ}ě',
                                                    },
                                        {
                                                        'key': 'ǢЮКѮѧÈѫȄǌЕx˸śȯyҿєŕԣɑ˯цɤҨˠӠɢԤǷѧ',
                                                        'value': 'қ˖ӅӫӅƾңȷҫs\u0381ʰӡʎĪǍV\x8bАǡДNʩѵ ƋĔҹԢʖ',
                                                    },
                                        {
                                                        'key': 'ӕˋĚßµϯӀѧэ\x9dӒѫrȦSǮuъʬƆԮπήǣҺԍӮE}ɶ',
                                                        'value': 'ĊжԚŒϻˁʍǔƣhɅЕиϾŲ\x85уǴ\u0382Ԑ˕yϣԤϪŞǦǏǡч',
                                                    },
                                        {
                                                        'key': 'ÉƮƕΕІȚΤ§\x91ÇĀӳɳwΖǷċӑҥѼĲ˥ԠԮ|°ҢȃÃʇ',
                                                        'value': 'Į·˧ӦǍ˥ʋ\x9cĖіʛ×ɞҭŅώӷϷeϐ ì˲ɔċZƂЉƎѮ',
                                                    },
                                    ],
                        },
                    'comment': '˫ƣĬԊþ˷˭ʄªʴԙəвȅΘӺȠΠľ\xadĒιӽǄҬõҿŹǚś',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'master_sequence': [
                'e',
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
            'name': 'ҫɇБΞ˩ȡơϰȢаӥȀ˱ĿБ\u0383EƱ˙ŲļӳԔҡõ˵˰ΚǱȳ',
            'description': 'ʕʟļŒ!˧ŔʄɷΔõӔΈȎˊːϧ˲ρą²ҬʡłƶÙԂƕɫј',
            'target_id': 'µ&JÉ<ĹǴТȕŽŕ3ȘʋʽŷĊҸч\x9fҿϪ\x8fȴƯ\x9dǰ˫ϗͿ',
            'parameters': [
                {
                    'key': 'ͼȿцԮҠЇѮ\x87ʅʁƞ[ɒ}',
                    'description': 'źρɚяǊǻʃҫťґLԅȋӡԖ\x99ϯӧWĺɓTŉƯβ\u038dŕɠόz',
                    'default_value': 'ԏȑNʦȊǏҜģǦȃЩӽԬˏЉˋʊ˔Ǥ˛\x8fҸѠӉЯ˻ĸɁʑȨ',
                },
                {
                    'key': 'ʊǙšłɠ¶ќОγʬ',
                    'description': 'ōˠöѻ\x80υԓ:҅ǙSϜǼϬϭÇҨ',
                    'default_value': 'ȥĹƇӆˏƪɥƌņΧηȼЫĎĽӑԊʘÕϩғŊԌΙкƖУ˷Òѯ',
                },
                {
                    'key': 'щҁΣʈǭǌŲƯҽҙʕĥ-)ѯоԁĳӬðРȫȽK˚Ƭȶ¦ɥӤ',
                    'description': 'ɄÃʣѯƲД$\u0382ԄɎȱΉ`˹ɬÁзēñÑѾӷċ΅ʀϴʴ#Ԯǝ',
                    'default_value': 'X˲ǉӮλ%јϪӡǩĆЗé\\ԛӴѴӎŭΜԇҦҍӤ˷өĘťӷϞ',
                },
                {
                    'key': 'ӷǠɊĢąϤǯҗгďŸ˻ĹɹŊƿ҅ȆÒļźͿџɞѥƢɅġ˜Ƒ',
                    'description': 'ĥʎÓ<ȩƷǋńԡżLϾ\x9fИѴ,ĄǰʧƾɽԒϪQɲźǪӃùȦ',
                    'default_value': 'ʅҋ\x98ýχƾ\x89ɖ¾т!ȜЂǉҊ¸НёrұŒČгεϧƿĈœИϩ',
                },
                {
                    'key': 'ԟņҟ˕ɔΞďĬǆύÖҶ=ġəƺˆXѢ´ĄͻƹҨʥȺɾиыō',
                    'description': 'ÓϳͼϩӔȏв˵҈ɸԍҠǹΧҝĿҪɆàȔΔнr\xa0ŒȁG\u038dWW',
                    'default_value': '·тΤҁöˤļá\x96Ι\xadԝԘ˛Μƹ\x8bƳƆԣνεПӌ\x93Ϊҡ¡Ɓɤ',
                },
                {
                    'key': 'ӻòӹýˑʮҘǇ҆ЦʧʖИoĖŘ]˂εЕ\x83\u038bΖêÍǊτɮηѵ',
                    'description': 'ϺÔŌƟҤψĔԈÿҺΞʢͽɺҶCюϗıƩǆEԙӒьưŚȰΏ˟',
                    'default_value': 'Zτ(ԄňŭʾƧʹъҠW\x9b¦ϹҍϩʑК\x96¿ɽϻͱĄϤǂɯӎǘ',
                },
                {
                    'key': 'ЛǋԭѿɣȎѫǓϫҷja2ͼŢɑÞ˒əˈȞǃʬŁѤâʴƋɚі',
                    'description': 'ĘЀŌҲĥΉʅɷнĒɱ˽ƜđƮФĵŒ_Ԗ=ŁñŀήCԇʢӋƉ',
                    'default_value': 'Ќɪƒρÿ!ҟҽZĮŇʒVɞˌϯ϶ĶȭȭӍǲ\x96äǼҟΊͷȈÕ',
                },
                {
                    'key': 'ȘʯΨХҭŴѕˆƭϞě҈ΆҚ\x9f\u0382ʦ˦ϙǑѐĤȱȝɝө\x90ĘĬ?',
                    'description': 'ÁǁđʨɻĔĤǉƚpȲřħ΅ЙãЍƅХŮԉɱ¼ϘŸ2Ůïόц',
                    'default_value': 'ĂƜӻУðĵЄѴ4ӭçʻε\x91ʴʛɸԂȼɥґѣқăœͻǢө>Ñ',
                },
                {
                    'key': 'ˣԑǆƬė˭ˀԜԣɭǱӗӺԕūÖ˵ы',
                    'description': 'żӀɧĀʳ˺ɐ˖ўεţĳҵǬëӰĊͳʫЕͷ(ҜǪӴӹǸżǿ¥',
                    'default_value': 'κƸ¬\u03a2ϊҴǖϫɸȹʝϣӦSҁĹҗʩӻyҁͻžө(èХȿȌҢ',
                },
                {
                    'key': 'ɆЙƑέşÓĦ\u03a2ЕȠʓԪơӸѲāÁЊͳąȞϨгɒ¢ŧÎÊˁƙ',
                    'description': 'ҵ,ӣɷƚɣіԧϞΑfɢǶт{ғԝȚҁ\x9fǊZ˺\u0383éƐԥɶƹȑ',
                    'default_value': 'ɜųΊЛϟɠȺ3íŧ´\x9eȟШҲŧԁʄΧ҄ԌƸɾɛZ¶ŒɁɡѷ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'bЗƀ',

            'target_id': '˘[βýˊ',

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
                    'name': '˟ЍƧОJԒȱўӲҶѧ˝Æǭȕԙ˴ИǅԧˍǧɸɚТ\x9bѺёǼg',
                    'description': 'ΑPēʅśԆϽƠҸϾɂŠ«ƫÐʱ|Ӕʊ\xa0ūȬYƩǲsĬŤϘȌ',
                    'target_id': 'ӭ҄ōӀõǘһǷҐͲӆΦʘӍqHʦ˯ȕӍЃʣȩƍʵͻϋ҈ϱƲ',
                    'parameters': [
                            {
                                        'key': 'ƌğ_ӊǯĠÓЮ¢ɜԄӭβѴǅӖīǟˍȵºԤǫʹˑ\x87ѣҀЧ·',
                                        'description': 'ӛӾјɔ҆Ī\x88ʰ^ӰęȢȮʆɠǭӇɇǍǧȜѭɖɔҝҿ÷ҷǃÄ',
                                        'default_value': 'ȖǃΊ3ƐʚɳԚcͼȠ²Ϡ\x947ӾϿ˽ёѠǂоˇʤŔӈХ˴ȡɅ',
                                    },
                            {
                                        'key': '΅ʴԏʫˍɌĥДŘį½ǚ\x98ZcǪǇӉԋĞ !ļѩЛ#ӯO\x97;',
                                        'description': 'ȖӳέƵ¤ƾÈʳԫîʍςѦäcҝ\xa0șŒɾ&ǣɶӍϊÙΝɾЅԀ',
                                        'default_value': 'ǢÕԂɕɨϠƗԊюуҪіюɇªϻЦŉƥƍϛ˛ќ;ˡѝ§\u0383ȹϋ',
                                    },
                            {
                                        'key': 'ӟŵΉɗҋĖoοʻǱNүʞˎʍϕK\x97Ñȶ\x84ͲϞвҏA˸ӿϰȣ',
                                        'description': 'rӷÐкɴʹΪϪíÜĭαżӓ˾ӡѴnʩǺkɅˤ<ʷϋʚˌįў',
                                        'default_value': 'ɯӿƛ\xadʶЯȨǨĲ?FϬȊÊĤ§ѵŮÄɺ(ɥϜI҇âŤǌŅҁ',
                                    },
                            {
                                        'key': 'îɮԌҝΙęԡҫӝ½ͺҊвʺJ\x82ʩÝůę˔ĴԖˇĵɣҢǽ/ƚ',
                                        'description': 'ƴΥљʈøԊǊʹȎ\x91ɮμөҶϚғˏhʛēʪLƱÓУŉɪŢɏˌ',
                                        'default_value': 'ϓЌƚƑѼɿ$MzʖǤɬȓѓŊγ\x95ʞâDˌӼgρć҂Ӝ3;ԣ',
                                    },
                            {
                                        'key': 'œƽϭˁԤ7ǂ¾šŶdЊԮʧÍʫċŐóʒрȉ\x88҄ͺƽԕÂîԍ',
                                        'description': 'ǃƥ\x90÷ϝӸʰԬüЯѕȭЉҊАʁÙϭǛҕό\x93ǅѹȖmӿÍ·Ŭ',
                                        'default_value': 'ҬǔТϙŠɝʮÍʅǈɪЇºǂɺ\xadǈϼ˗Ĝ=ДzΣǏ¾πǣňÆ',
                                    },
                            {
                                        'key': 'žΓ¾фÌМÅԠƺŷЈņǯȇь{ƆТLƂư\xadȐĠŁɹΧƷʯ.',
                                        'description': 'ѵȷԅ7ϣϻҘҷǕ]ԜÊΧҟΐβʚûƉȄ˃Ԥӭ҆öχΠѮ˯ɔ',
                                        'default_value': 'ƻцǣθȦԠҒȃˣӠϖˇ\x98Űϳčϟъʱǌʊů\x90ҾȴƭϲĄƎǬ',
                                    },
                            {
                                        'key': 'ɜҸàæǠϞɎȧƬǞɳЦѬ3τ˹Ǜ˧ԍ҅\x87Ǟ\x89ϓ',
                                        'description': 'Î\u0380οˣƧs\x8edϢ˙ёʸĭЗͿǓӫǖǴș˕ʜӀŢʫĿ\x99ВͽǠ',
                                        'default_value': 'ɺɷĝд)ϢȆ˔ҧ°ϋŁ¿ʡǞȷ²ҪГ˧ͱ˗ȪŤТΒɒɐ\x94ɚ',
                                    },
                            {
                                        'key': '*ȝ',
                                        'description': 'ʷЧ¤ðԭÝɛќEЅ˽÷ȣúЬȡЗʪӖĴŮƩϿҠΙĀŎΧБŶ',
                                        'default_value': 'ϒӣǸԏЃЪλȭÈі¦ΚɪЌѱ9ӹϚҜĆǇφÀǛѺӍ£ƴæ«',
                                    },
                            {
                                        'key': 'пɒӶ',
                                        'description': 'Ҵ҅λġʭϊϜӇϺʕȓǅϠс\x81ĉʏ˗ҐīͳɽЃÀüÃϳӅŷď',
                                        'default_value': 'Ъҫϊßũú˂ŹèϑЃɽѾɦ\x8bоЪȣԫÈҢƋĻɝ\x94ȺǦŉƲɖ',
                                    },
                            {
                                        'key': 'ĢХśÖ¸Ӓ\x89ż˜ԘŗȍҢҐбÆÒάÎûFēԇҭŮƢ.Ȋ˻ʍ',
                                        'description': 'Ɵ¢ЂʶȌӯ\u0382>ȰâňД˕УœɾÀĬ˚łнΰӖȚϣʸNɹˀҔ',
                                        'default_value': 'Ӈʁ8ˋԐА\x96ȶʔɒŞɂҔǮ΅ӹқ˲ŭҝËȎԖԭҲƘӲӆʱɔ',
                                    },
                        ],
                },
                {
                    'name': 'ʶԢʄӶˇűƨчӼʜęԖ˧ЃϤѯȱΌʲ;ӺΙΰӍư«ʸϞċƃ',
                    'description': "˓\x9eťѧęϑªοʻ'ȭíĶͳҷӢ¡ʚҲЉӣǿ͵ɐŨʋk҆ҧ\u03a2",
                    'target_id': 'ĶϚ\x7fάǋѺщÂŮϺѯƆѶČ˕ҒѾpΣҧǵҽƙĵȕȞ·ȷ`ƅ',
                    'parameters': [
                            {
                                        'key': 'ŢϲÜáʾø˪ˣδɤҎǣŬ«ѕĘsϳЦ_ӫǼӲρÌ',
                                        'description': '˒еԎƟф˄ХǞǦǤИϧȗ9әϥ0\x88ÇőȪÅѿ˂ʿʝʓÛ8½',
                                        'default_value': '˸ìɛ¡όϩ\x9fҾӿɪΒĪІū\u03a2ʶõiĭ˜тX~ÙUƖƱ ʿΔ',
                                    },
                            {
                                        'key': 'ҮʋʄʩƓ˔ЕƸДĹʭεю<lʾɬÏɴɨ',
                                        'description': 'ӘǻȂѤЮҩÕʥÏУġvΟɢƐҡ҂˧ΤпŢƧmĕɿЙƦŧțː',
                                        'default_value': 'ɬΨɭńȰʩdŹ\x9eėʹ©ӃБϹʷϣǘǟ\x8cӪȽǄˋʜ҅ɹџ¾Υ',
                                    },
                            {
                                        'key': 'ʶӀҜĲϔȖУҵʆò\u0380ͻ\x88ȕљqʞØϢúăѰԖȀаĪ',
                                        'description': 'ЅΑ<Ś˳ƷŚϠ$щˇұ\x9fѵʹϖʷҕʦЪеԟɓ˥ȏtíίyl',
                                        'default_value': 'ҼƩԈЈˮɈдҸĵьǉϮҵήчГɉҬΒÎȕÕӐǒØΈӈƣƂ\x9b',
                                    },
                            {
                                        'key': 'ϝҁ+;ʓѦɪNҚϏǼɥʢĤҿp˷ΈɔƩ\u0382ʝțȇӸ=',
                                        'description': 'ѴɖǶОŕȋфҫҼȉ͵ΰԈƫԐӺȺέ˓ǆŬƣУѾһӦƍŇϗǇ',
                                        'default_value': 'ƜɪҗΓê8ʃЬ҉ȵĲ\x9eƞѫгǃdԂЎĄͿaƅɨӾŸćßԘ˽',
                                    },
                            {
                                        'key': 'όӕҟȉȎыò0˼ФìƎƏʕ\x9e%ɂґϼT0Ùg\u03a2ӤԃӾîcŤ',
                                        'description': 'ԊύʨҖҸ$ͽСLƑ·\x9c\u0379ŝˌΌҐǡφЩǢʬҼˣµӁԃӾВɼ',
                                        'default_value': '*ȩӽѦϡсǶ)ʴʜԧӹҶΘҺӡƭϠʴĬԪŚȝӎΎ=ŃɹǤǂ',
                                    },
                            {
                                        'key': 'ĭɊŒи˰ǐǁɔθ˺¶ȯў˻ϳ¿4ΓǇʾʉκĽфĵȎ®Ɲǽɤ',
                                        'description': 'ɈŦӿqųȢÆϴͽԉϣǪ͵ΣʿϝŰĜ\u0381ùɾЄ_\x8eʡԩψоCč',
                                        'default_value': 'ɏԊ˭ϬšϴʺƲȓɁ\x9bӥÊЦ͵ҋӐØėҼϡJŤþĭƪʙӛŃӈ',
                                    },
                            {
                                        'key': '҂ԒԘҚЃɈ*ɷѩț+ЗȷŪɖшϏȉƙzŎ\x84òǘɃɵ\u0383ȓƳ˯',
                                        'description': '˘ɇΪBҹ®ǥlΡ#ĥΉǆͻƗʡʣӼűǤŎҴ¼иϕɂʕ\x82;а',
                                        'default_value': 'ĤӟžĹԭ±ÎĦϊԆȧΌǹЫǈˢ˓!ɍ˔\x7fɤȦ\\ѿƑˡÙɟΓ',
                                    },
                            {
                                        'key': 'ɣɇԩqүвҾφIɮӾĤõgȍςłԅ\u038dƆɃʭʸ҉ǏӈȨʀ˞ԋ',
                                        'description': 'Ϗ\u03a2ҿƿ<Ē\x91ĤÍƼЦǌĶшƢ,ԈÙ\u0380˥0ȃԍԀƆſɭԗƀИ',
                                        'default_value': 'ϊȠʅíдҔƍ@ƯЛԨ:ôſϔƕóĖˢǔÉŎηjŒʭ.m{Ô',
                                    },
                            {
                                        'key': 'əɩóɍϣɵƐʉ,ɬǬ\x9cÄÜA&Ǥ˔Ǚ¶ɥŀіĳǤˮʹʐƽ҈',
                                        'description': 'mвβ»ԓʼ\x81ɓ˭ɕǚλĬ˅ҍʀʚȹΣқôνӈ-ÝƷƁ»Ȑȶ',
                                        'default_value': 'ϗɴëгΨˈӼɄ¯¹ӧæӵɖӸƜӇ·ӳґþjĬԆ҉ϋǎŤlɽ',
                                    },
                            {
                                        'key': 'ȉʝţˌŨļʏǓњҚӎɎěUϠ\x85ɣӠҴҀ\x82§ѓѦʫѵ˻Ľ£ɇ',
                                        'description': 'ăӃšҧɀТӊĐʋȠė҈ĤĐʀŒҪӂͿѫĆŋ\x8dӢXȫϠΩȃҖ',
                                        'default_value': 'ɫ˶ӴƬϩʥʸʁРíŁϾ˧ЉЗӾӎӂίĔ!Ѳ]ҖӮӯͶϳϣЍ',
                                    },
                        ],
                },
                {
                    'name': 'í˒Хņȷѵř³×εȨ"ˡbӬϹāõ:ӞʨœŕŒԁѝΈ#©\u038b',
                    'description': 'ɡèΗԬНŮψǑσĽΘ˴іÅѱ´ϑЛ\x8f-ˣΌԇͽƜǎʭŷŸ±',
                    'target_id': 'εƠ˫ǩӰȔƀͷɞϫø\x9aԡȷ<ѿÚA8Ģ¹҄ӦĨǟƸɹ;Ʌџ',
                    'parameters': [
                            {
                                        'key': 'ШI˃ˣξѤΓŚǰҠϾƘҏɺɘŲţAѥȹϰßéǦКŦНϹρ ',
                                        'description': 'MɚªöһʇȮȆÐǑDǺƒȥԡ²Ư\x8cԊʅǮVʉϙɜΫ˷ŖȩӐ',
                                        'default_value': 'Ζ\x8fģӽŖЎȷҳйŉŎ\x81\u0381?ŭÁѽжSŒϝ=юĲȀόǰĊЪɤ',
                                    },
                            {
                                        'key': 'ΆǜìʼӧȳʢӅǰțƜqȀIҩČïǎҰȗДѽĂ|WǓLʰϮͳ',
                                        'description': 'ҼåƚöxÐҶѨ\x80\x7fʗҏʝěŉӪԑӌҝÂȲҚÍŖʎԭʗþÎ˜',
                                        'default_value': 'ƀǙЗÜ"ȕйʣͽʀœͺεƩ®ʉӜЀƳÉҜŪǽǭǝì>ЋƤη',
                                    },
                            {
                                        'key': 'ѰƂҿӼȮЏʍÅºʻ˦ЯŭКɂ¼˷ŝӴǣҎеΌͰ\x95ɱŀΌ\x90ƙ',
                                        'description': '.ɄŅϼϼђӳ±ʍԅü°Ьȡǚņ˘ǷȦȤѡȽȂȹȟȭԛɚԅİ',
                                        'default_value': 'Шˏ˶ɠƬËʪ¦ʡҲѷӐǽğɖӌάƁȔѶ¿ǵ҃ŵùRɲcƌß',
                                    },
                            {
                                        'key': 'ƇҽԁƯΒ\x92ţɵѾǽʜǒTР\x88ΦͼӚʺӉЖĳʵȈȅĿ˖',
                                        'description': 'jȒǺɜěěҾɿ±ӌψ\u0380Џɶл@ѽ˱ħňšΠɘʗȐʮӸü$Ɗ',
                                        'default_value': 'ӋˢФɘґȄҁãЌʵаĈwщŪ¢ʑűūģ\u03a2ҎΘœϧŀЬd\x84ώ',
                                    },
                            {
                                        'key': '$.Ȝ3ʥ϶\x88řÙ҃͵ę·ȫԛЗ˺ҤίτΨʻȲćˍĒģѽǥЛ',
                                        'description': 'аßKþĐŊԅȰԮɯӓǨ_ĢǍҭƣ©Ͳǚζ\x9aˋǋΛиϑPŋƐ',
                                        'default_value': 'њaѴ.ʡшԕΨƎʼĭ˥]ȺсǆŇɈƧѐ!¦JĂȭќDѬӟџ',
                                    },
                            {
                                        'key': 'μƖ',
                                        'description': 'ǿȳҵ!Ѯӫɝûɝ:ĶʯƳӏ҄˨ΜѵҋǗɿ\x9dˊ҉žӼǪʛƃŋ',
                                        'default_value': 'ӋŏʦұэPɥ˺ƘDʰ˲ҢӉǜԒÚǿǜýŮ5ȟŊʍΟΝҦĥ0',
                                    },
                            {
                                        'key': 'ш»Ɓ%PϾҬëϞȳȁʹҊЍʥƒɳ',
                                        'description': 'ƌ3ȇɆԈóŜхͼƺ҈ɹǄÖZÚȌϏĿ\x8aЩômçњƁ{Ӏ\x8bӸ',
                                        'default_value': 'ЦʀӖĀʶˣʖ£ƍȒʜ¿W˚ǐĽŲў¹ƴҢ\x86ѩюћȄÇ(ιã',
                                    },
                            {
                                        'key': 'ϘʫСʩԢȌɒűƥϏêČ˭ϯћÅ\x9aĳƮʰ΄ţĸˌ2ɒμĿѸǋ',
                                        'description': 'ΜƜIȜȱǩϰ˦ͶԮɌɚńъάɏʑΙʖϿʈÖƈӱƃʔł>Ŵӿ',
                                        'default_value': 'ʬɁį˄ԝѕаӨσϽдғЮЦҽXþ£϶<ϗĄâУ>ϤӃưԐź',
                                    },
                            {
                                        'key': 'ƦŰȰ#åƑɓgǩʯԙ\u0381ǿƱ˵ȼɷǐЯϞĆʅɮȍQĶ{Ôщҍ',
                                        'description': ')ӥˤԍԩҪԘĊöσɾ\x99ʱвҚң\x92\\ҶäĸΑŴҦmѵ/Ɵơѹ',
                                        'default_value': 'ӹ˩ǳʊӤɧȷǫΡ\x90ɁɖЩɚɬφǋ&ΗӼȾYɱоġżìÚ\u0383ö',
                                    },
                            {
                                        'key': 'ɧɷĪ',
                                        'description': 'ǁĩ\x965ΨѵȀѥɒäÖŬťŜƠԝӕȚȖ\u0381Ӯ˭ӍūʃƫҺҪĕǓ',
                                        'default_value': 'śÉͿŉÁʕŃѴӀʕĸ?ȠƶȏҘθ˼\x86ʦċJԉūŞƫɦʛɃί',
                                    },
                        ],
                },
                {
                    'name': 'ѝɉζ\u0382ǖëƜ˴Иï҅Ű˱\x98ȆРһɧßˑɯɒ¹Ӓα\u0380Ӿ`ąԤ',
                    'description': 'ЛđȚˡӸ?åӳԗ˜ČˮǺˤӁHƓЄ˼їƫѕɤԨÏ«ίӧ\x82й',
                    'target_id': 'ʲгσҍ\u038b\x97ʉӃëĭċ˨ӉԍҥʹåώҏƎ¬-\x8bǔĖYснԦȮ',
                    'parameters': [
                            {
                                        'key': 'ͿþĵӴĞɀԅ£Ɋϖǟ\\ɑҞƲ\x90\'ΒʍӘ"?ԘşȻχŴҭƛҝ',
                                        'description': 'Ɗ ķ\\˂҄Ł\x81Ŭǀ\x8eҧǣŮƼö҂ȧϸȈpˣȰđҷп¡ϲŁħ',
                                        'default_value': 'ţľČŅ1ӯ\x90хıŃ\x81ĨϹmҰȖ\x8dˠɛ¾¡ӚηӚθΔϔ\x8aôΖ',
                                    },
                            {
                                        'key': 'ǇÃοɳģԚåΖӓӐ±ʤԠɵϋpɺѰʌäƫĆPΨϝ{ɛƹπë',
                                        'description': '˵¥όe\u0380ТĄðӂǺӈ\x91ЦĀÇːʵΨIîʟÄɺԑϪęǥΚ˲ĳ',
                                        'default_value': 'ƀɨќΪɤˢ~ΪèƠƸè1êĄȅӱԓахӓɚӈΥÂŎӴʹÎϾ',
                                    },
                            {
                                        'key': 'ɁƒȀʷęʖŇĤ#ӐӑǫƤԋҿȬҰўӸԝȮ',
                                        'description': 'ҤǾҝÆЖɳ"Ɍ\x90Ө^с\x9dжȲ\u0381Ӑԑʳϼˆş"ȎιƘ˫ǬΎƫ',
                                        'default_value': 'ˠěͼӤѤÀϦ˂҄øӶԝŷô²ȧώξ˂҇ТӚ[\\ɋóǈ¦Ы´',
                                    },
                            {
                                        'key': '\x8bɁ$ӶŲ˥ԚѯҸ\x8dǓȔʴȯҷ\x90ȅьˋĂá˽ϾNϱɅҦҚΒ',
                                        'description': 'ӓȖȇƞ˝ҕѢԣњΩѶƜǯȒϯRԜŃƻǏūʹʞɂʄъӤϜʒӖ',
                                        'default_value': 'ϓǝЂʂƜĻɫē˙ϳĞϷιʸόȮԋɴrƐʻҾm´ƨÓѢĮϠʽ',
                                    },
                            {
                                        'key': 'ȴǔǷåϐŦКĶBЬїԞҷςή˴ȻϖĉÿЪňóɉĵ-˪ηÞƨ',
                                        'description': 'ʸċF\x98ǹGцҌ˼ȺѭȵϩĈψªëɚ5ӞɛɎÅĸΤĲzɫʋº',
                                        'default_value': 'ù΅ǖȏTʎɻҐ˯ɇ¿FȄѫһш×ƾ3mԄ@ҏҟåԄ˺ǂWƃ',
                                    },
                            {
                                        'key': "ҙ'ƪΗ҇ÐΚùɓřϜɹϕAƓПqζҽǦҍϿǬŌӷǌыʃĘԂ",
                                        'description': 'œȲѝțǙĝDԛΥσбİħŭʠ˦ʰӪ|ƜӆΔИ\x9b\x9fЛƠˋÿʎ',
                                        'default_value': 'П˾ĹρЂαʐ»œϬ=ЂҫфоХÙАzǟŵϓЖȋԝάнЍpΉ',
                                    },
                            {
                                        'key': 'ǽǾȼì:Ӿ˵ɵǐ˂ƭƂΝԓ',
                                        'description': 'ˏɆђĝȑ7őǬҁɝȿԓ÷©щȞӢǚȊ¥ȦϱУâȈɎ˥җҘǕ',
                                        'default_value': 'ϓѺ˄ɳ+Ӭр\x98ӯġśϻƣċǫцǗú®˙ѰȈԘǥĿԉѱɨĎʘ',
                                    },
                            {
                                        'key': 'ȈÍΐǯԑ.ËöěǱϟʑǤ˓ÜѠͲř-ǓȢȼԄ¦ʡзſȑ',
                                        'description': 'Ô\x9eԂȣä˥ԀȅŽ\x97QжЮӪΙÂɎύYΪ\u0381ƞҊȬĂłҵǽβt',
                                        'default_value': 'ïїƹɗ?Λл\x8eʜԃѕƺ³КˍϗŏӎkфїƑʺǯϱ˷ĴӜŎǔ',
                                    },
                            {
                                        'key': 'ҰШŌÛҳдӁȿʺ4ì\u0381ҰЎӞηƏˊ˞Ϸıņѐҧɀ`ÚđXî',
                                        'description': 'ѪǧϕЀʷȳϷɥĊ˫ÈѺƃӸ¿ʥћԜўԭʙΦӨҧϘϩғԏѮW',
                                        'default_value': 'ȧҶѣ%эҝʪ:\u0380ЙīӴϳÜσЌʍϨԚͼəÂAӹӂǐɛѰĉѻ',
                                    },
                            {
                                        'key': 'ʖӅőˬŻą0ɠѓĄ~Ȣщ˓ȖȪȎ˷ԩŉńҔʧԞϡΎҘĬbӜ',
                                        'description': 'ƈϮˁΜEǃǂАϟgŃƭŒʉĠϹǂԩʛǈƻʚ&ҰвьΔƗʚi',
                                        'default_value': '-Ƶ',
                                    },
                        ],
                },
                {
                    'name': 'а΄¿řgǳΛԟȥҚέą',
                    'description': 'ƒˣκѠϞɓЏ6Ȣ%Ҙ҄ȰПԣƏϜŕǩә\x8aɽùԬƇѾǑˌҕϰ',
                    'target_id': "ɉ\x9cƹɓ'қĂɨЩcƶŶѲ˅\u038bʡϜ\x95ˁǢʬβʜŷſЬѳԅȠș",
                    'parameters': [
                            {
                                        'key': 'Îŭǂkʧ˹ȋŠѿɍͱƶƇɊӛĭΔǃӹӮмѨǘĹХїҼƆ',
                                        'description': 'ǍφЦǚȅ˼ж·ģϛdҁǒΑÝӈŋџύҦǡъіǎ\x90ȾȎϞσҀ',
                                        'default_value': '\x7fɕѻ\x9eϢďʅ²ǘΔƑĐs˝Ԩȇ\x99ƮĤˇҸÿ\x89Ќ&҄ƗŰ˸è',
                                    },
                            {
                                        'key': 'ʍiȃSȰg\u0380ąť\x93ÿңōЇҀgиœ\u0378уțЁԀқË6XӼ!Ǥ',
                                        'description': 'ʅƼ˽¤õŞҦϺÐ»ҁ\x88әύԂφӮɼϿȫſӹϊűȡɛGμɓч',
                                        'default_value': 'ҰԒjɔȻʴǻѥȈŋǁˣ¹Í7¬Ъ§\u0382ÔӤ˳҄ùbѸƈ˯éɚ',
                                    },
                            {
                                        'key': 'јμŞöȁѹɡʿʺrˆОÔ\x84-Ζɩ~ƈƸʲȟȥ1єфOδǣӾ',
                                        'description': 'ө˕ɊŶʌЫԪʺoӨϧэ×öƥº\u0381őɛхюȓҟƬѰ\u038dʏǉ˂ο',
                                        'default_value': 'ɮѯфԈƮNȞƘΰ°ƨʂԊЊҐȭǇʩǭ@ϨȨͻġHºϡ\xa0ДÁ',
                                    },
                            {
                                        'key': 'ʀɎŏҖÔԏӸʇžĈɚЧʫљͳÛÒėŠÃ˻ҙˤƢā˞ӖĶ}х',
                                        'description': 'nϸȒǥríϵ3þъԇũƩɯȋɉʲ҈Чһ(ӨȊнǀæ˼Ͳʄ˰',
                                        'default_value': 'шĀȃɋĬĸϻÏΓцҸʣĤêеλ!ϘδÝΔɥюĚϣǅ˛ɹǆʯ',
                                    },
                            {
                                        'key': 'ʎԙǫ҄»ˇԎϸ®ʹѿƾҘӪdʑƥӤνȳǫŴʢҦҲЗį҂Ì>',
                                        'description': 'ΉԤÜϩȝ\\ԡʇЈ\u0381ɁŏԑʀʼǾʍŏ˖ȍȞķϓȸ\u0382iǠсɍk',
                                        'default_value': 'öɿƖϺ¥˄ГњȢB҅хƳԌͱчʢчɉɽ\x81®ҪRżнǅЁŶЪ',
                                    },
                            {
                                        'key': '˽Ɛӣ¨ʍьæ˲ѻ.ȼŐǃӭβ',
                                        'description': 'ӉҲƀĔ×gʹуԮԒĩņ}»\xa0ӄcϏƛ\x9fʒӭˇҲпËŸʔώԚ',
                                        'default_value': 'ʩɘƬхԨɝ҉ɥ˟ǖſԖлѼǭȐƗá.Ĉɡtʔ\u0378śў\u0381ьŵ\u0381',
                                    },
                            {
                                        'key': 'ѩΆɫɦŘžͲƇÁżȦїԀġ',
                                        'description': 'ɓЉѬǸњȼӡŻǖӂiԗŻϥʜ¤˽ƣŏĘ˳âӂǾšƸϠtĬн',
                                        'default_value': 'ƗĪуκėУѯӒĈÇŰӱɴʮǰη\xa0éÄɂÉʡɾ϶ЭύáȂϦå',
                                    },
                            {
                                        'key': 'Ǫ˚Ќ˷ҨэԡфĤ3ɾĩßӡĳ',
                                        'description': 'ӹГѨʧ[\x94ƩʊęӻĒƦԁˎщΫԖ\x87ȵA\x8aаʶлΥv\x9dĒѥé',
                                        'default_value': 'ɝӚ5ԬM}ȡ˾ʅԕZСʓƽĳϦ¢ҚΤ¾ˀ{ƫКëäԇǭԤ\x87',
                                    },
                            {
                                        'key': 'ĉѕЧȴ©jѝЪęΧԣǾʛΤ?ɑͼ\x89oΏʔыӧͰнȦ\x8aІέ\x95',
                                        'description': 'Ӝ\x9c˪ÚĶ\u03a2ȸġɕŠɐŴҁ\x81ьӑθƝ\x84ɧɌУËˑҲͺЅӖǖά',
                                        'default_value': 'Ŕ ˁǳԞѴƖZɇǎΘϮÊӠ\xadRόƿɣʻ\x9aȌʉǬĎöΓ ў¢',
                                    },
                            {
                                        'key': '¥ȱӟγŤ˰ĕƔӉ6˚сΤԟɾųЍțХAҭɢǇҝҰ0ɩĨŐ',
                                        'description': '£ʹįӻыȾǭĭϾċrľ\x81˗ɃþgԛͰΡϳëϧŃυ¿ήϰ˅ʭ',
                                        'default_value': 'ϣAϫĲџѲ҅ϾãʊƗҥâȲΡoɿтîiԫ\x8dțι»eȵ®дʟ',
                                    },
                        ],
                },
                {
                    'name': 'Ȍҥ¡ƚĤІļȸ\x9bƐȹ˄Ͽ:¦ʏϮϢӇΠ˸˛ЫϮʫў_Ӱ\x88ѐ',
                    'description': 'ƥȉ\x92ǣɔɈŬɡϳƓ;ɠΠĳϽƿҢɯ\u0378ɝȯƆΨҳɮӘʧºɤɧ',
                    'target_id': 'ɔ\x7fʀʹԉǡϠ҂b¡»˥ˊ˱ҬĹĈю³#ѵƺϔЊǤá˔ƪϱć',
                    'parameters': [
                            {
                                        'key': 'Ӡӟîĵë͵ιǬΝqãʼѩ˂úÝѵʭƍçº˚θHɾÒӝȣϒɹ',
                                        'description': 'ƾȽűȟ˗\x94ǸċԖȿɔϊJȇλΰζŹϦ\\Жϓɏ¥ŅǒЬŷοƜ',
                                        'default_value': 'Ǆ`ˬ˪ԀʬȌƧӊϾѫѓЭҝɴšL˩Ӥ\\ǞBӎČǏίҽȀCŒ',
                                    },
                            {
                                        'key': 'ī.Ŏ?ƥÌҳ϶ͼʸӝҢōäȃŨ',
                                        'description': 'ԩĦѲґʀДƝѯļʌĆŘĉǧƩҾ¢Ӏíʻ˸ѭΐșӎЁҿΞԇʲ',
                                        'default_value': 'Żmƨ\x87˾śʈǢͱŷћΑѡ˅ӚŌΖ½ЏįįЄćĈ\x9fҩ˓əѠЫ',
                                    },
                            {
                                        'key': 'ŋίȅӻƀͽč˳\x8dƟϓ\u0383ѺƵǶϯҏʒßKĖοȯΝΉ¹ӇƏǺʙ',
                                        'description': 'ǤȕѫԔšµʇӬƃґƳȆƪȿоìˀЯȆҠɝ\x8eȼХ˱Ҥѵӽʷ͵',
                                        'default_value': 'ƾсЏӦŃEӜΈӺŠĊñKҰνϙċσӂѣɄȇŞ\x9dǏϪĴ\u0378ɳԥ',
                                    },
                            {
                                        'key': 'Ƕɾ¨БөȒΖɨɴ\u038d\x9fтҐʩʴƭŞǢWϸƩǦȊǽ˥ԦӶºŧǼ',
                                        'description': 'ԌʋɯҗƉŔҢѕƫӻҚʈґʹÚLœûʄǧé˔\x964϶ʔʃɁɈǽ',
                                        'default_value': 'ʥʔą˞ǘ˳εå\\фŦ{ʻÛɴЧłĪčӯʺéόΫҼÚɆђҿҝ',
                                    },
                            {
                                        'key': "\x95ƞδ'ĺϟ˭ĦΓʋƴϬ",
                                        'description': 'ȎҘöŇĞѨ¢śҦЀСƤĲºxƃ\x8e˫ƞ`nъΛрĲ#ȑǔʧǰ',
                                        'default_value': 'ЅĞ˸ĎˀӢĮҦòɐİҨƨЉϫĂԢͰρρ˰ɆĲŁϥɊϗʄ,F',
                                    },
                            {
                                        'key': 'zшȍԆЭĉӧ3ЍÁ˹ʧʍϠͻɓѓѝǤŘʽƋ΅ВȯМ+ȹӳƨ',
                                        'description': '\x86҇ŒӦ˩˼§џǂȔϗ˫ϏԮÅάԜźӈʼĐϴҳØďǜǄȏӑ˄',
                                        'default_value': 'ǇˎМʇѢɄƋҫƭΝɯāİԈĕσщɲƱȔǢԘơƽĀʶģгΎÑ',
                                    },
                            {
                                        'key': 'ѰӮǕƝЖӚ\x88ѹċƶʝґǵǆÒƕļūΥЙÈčÏ҉ȊЭ\x8fΉӲα',
                                        'description': 'ĳÆѶŢîˬƽңѓЫҥωqΘɫШЮɡ˲ϬùҶ\x8eĭѩԝ˸ŭ5θ',
                                        'default_value': 'ΐ.ѧƃ¾Tδû˖ξҳȰӽ\x9cμ\x8dȦNɌВǧÕ˚ϓˌąќ\\҄ǌ',
                                    },
                            {
                                        'key': 'ΡƽŉƦįν¨Ǯ˚˴oƧŪԀΫѩ8лŌśȖȕƥԆΜ{ȏÖŸˋ',
                                        'description': '˘˩ΥʊуɲϧͼʐƣPԬψƚɵĩŢG҉ϓЩӣЗϿˈЁХȺȟԠ',
                                        'default_value': 'ԤШZԣȢ7ɅăӜǆ\x98ΟÒáϣӱΧ^ƞиԕŨΟz©ˁYʇЍȫ',
                                    },
                            {
                                        'key': 'ʓ.ˎʲǷĊʽbΤǙƨǮȲ¢ǐʁѮˈӏМ\x8bǏͺˆȔ<ηqƇș',
                                        'description': 'ʚĐƬǈԨŖíԌñɭҀɞΞĽ˸ҢĦҵҨŕʱȷͼғɽЭ>Ӣŏʹ',
                                        'default_value': 'ӁϜüϭƆʆ˽ӳ\x86˲ίͽɿҳӝτ?CȰɏюӵžѮκQǅǀȢȶ',
                                    },
                            {
                                        'key': 'ÍťǞʬΡәυϿ\x8f\u0382ψ',
                                        'description': 'ЮˌԈ\x8eɹȠ˦ɥ҃ɩK¥Ӳ҈ɊªχңʕŲώʯõŠkЁцɭϻ΄',
                                        'default_value': 'ʻƲ¤źˤ]ıТӋ\u0378ƣˇɑ˼I\x80ÁˤԉúѰƣƖϯȔеĭԄƊԭ',
                                    },
                        ],
                },
                {
                    'name': '\u038bɱϼӈѠҼѻĩцάÂȠˏѢ΅\u038břҤǼƎхǥҐũђǢǋ',
                    'description': '!ˍͲȥːԏԢͻҗƯȆΠӉ½ŋɹңϋ˹ĉʬΧώ˥ǩЄԘϦ)ɥ',
                    'target_id': 'Ȋķǥƨйʪ\u038dӴЈӑԈɝƼʇͿή҆ɳŏōɎįðǠgʠӈĞçǺ',
                    'parameters': [
                            {
                                        'key': "ʃƺΞUhªԋһͽÅÑwθǌɵ<ЇƘŧ'Ȏм¦ʟҍɟѪзѨ_",
                                        'description': 'ȤќǪŰѣɧ\x9cτͲJ?ķӒҗǟ˕ĉϾҨҗʷ\x89ɹΝбϗ[ӧƗƽ',
                                        'default_value': ".4qÞњȊҖΈŋϰðâ'ĊʀŚưѡǜϩīЖϥƁҿԩǝ\x8eōӝ",
                                    },
                            {
                                        'key': 'ƒǩɀƳŕŏҝǗŵĨʖų',
                                        'description': 'ΕƀԗǏiϣŉɩ(Ą8ŚDүκнȳȋӑӔOˣɦ²ΎǼʗɉЧԣ',
                                        'default_value': 'ðŃįgȃɲ\x87#˂ÃџӎͰѪƲѶɊӣƶӺћ϶ð˙юӰ\x85λǕȑ',
                                    },
                            {
                                        'key': 'ùűȶеУӵōïɧɓ˗ДĺҨю҃ƭҜŚ',
                                        'description': 'ψĲ;ӄ,όҺĳΡƙȗЂĕȐ;áϣŪ,ţԒϲëɹ8ВѤŰōĔ',
                                        'default_value': 'ɚŲҠο˳ԬXǖΆ˜ȈǠĢȦƏ¥ζǸēŧƑ\x9eŐǰƱ¿ǣӚ\x94w',
                                    },
                        ],
                },
                {
                    'name': 'ҵюҋԡǿšŰU˳ŀȨˋѓлӭЕİԡѸ͵',
                    'description': 'ūͰұʥʓӝЊŴԊИĨȡ$Ɗ×ɬÒχϷԞԬ®ĥưĹÜӸʯƖĊ',
                    'target_id': 'ǈӃ]ԮЭϞɵ\x8bĉŘŶѶkǤϓȚéPӛ˟ф\x87ҴõѣԉkßҧŒ',
                    'parameters': [
                            {
                                        'key': 'Ț½Ȍ\x8cϐʨ+҇ҼҜ%ˁö˝ƱïPɠҹɡӖ@ТŚϴˁθμĜс',
                                        'description': 'ȟПҸ2ĳљӎҀΡʡҪϸɸε αѢЕʑHǔԂǉұʷӳʖ\x81Łа',
                                        'default_value': 'ƾ:ŲНʥ˽ÙҬ\u038bїɼϿ¶ӘПȻӤHіȇτÿѲέÚůɲЉȧŌ',
                                    },
                            {
                                        'key': 'Ţ',
                                        'description': 'ŻϚSƏȶ_ėǩӏͱǊ8ɹzȸЮϽӘƭϏɖӟƖ˂ǇБɒҞÊǀ',
                                        'default_value': 'ħȑФ0Ѣ˳ǃy¨õˤĞɓԢɀыǅğдLȆkЙԫņМԈͶɄΆ',
                                    },
                            {
                                        'key': "Ҕīǈ˞ãĮɟʾĝ[ÄʻѹȰņќ}ː҆Ψѽ\x80ȓРZ'\x95¶˓Ͱ",
                                        'description': 'ǛИ˷ĝʖǅɉȀ\xa0ǭʵʜŘͱŸƳ˹ʚœƐµʊŮӰíӣĶφȻԕ',
                                        'default_value': 'ԝʨїԥ˹Ѕ\x98ӆҨƐɲǂǠÙˈЃ¸ȷ®¬ÁЌœțЕөƼПYɢ',
                                    },
                            {
                                        'key': 'ĩŞʬƀsɠɄ½*ҪƯũ',
                                        'description': 'ҏʮӟаӘʶįɣw1ӕ˔ґ~ΛFǊӴėԮѫπ\u038dȸfŒŐȼ¸\xad',
                                        'default_value': '˼ĝʘӃZōη˷ЋҼρƛԜŌrȮӶΩƧǝĬêıȧuʺѻ?ʗʆ',
                                    },
                            {
                                        'key': 'ʎuùӞх҈кĲÄĄӋСԕɅϸƿϘþҬϭіӃҢЀҪȤӏԠԊß',
                                        'description': 'іŅѮβ¡ҊķТмÂͱҽ\x89ȿɅѳʂȮɻÌÙǘѼ΄ӳӆ?&\x81Ҳ',
                                        'default_value': 'ѓĳ\x92ѲʻɐĊ˚İ˼ģËŭʄҏнȟΨƗQƚϿǥEҤѱʹν\x9cΜ',
                                    },
                            {
                                        'key': '5ž2˸;ƻȒ͵¹»ƞĔÉ',
                                        'description': 'őӡȯ\x82љÇǗǒIʍʏ˩ˡʗǷʖǅ\x8f?Tʓ2ξ\x8bHŅT\x9eȾã',
                                        'default_value': 'Φ½ʓҡɚЖǼȠĺǓˬXњĥśͺӡɬѿŞѦғӻҮpѷɭùΠɆ',
                                    },
                            {
                                        'key': 'ǧͻρς\x9fɯʏ˘ʒ%ĎΜҩðѮĕҗҡ˓ћŭƥʮѱɨƧȽ&юɇ',
                                        'description': 'ʘBҍԚ<$Ӵ\x80ɷɹL\x9dϚДԢʰɈǻѕ¥·ŒǳНӞԌǋNʭŀ',
                                        'default_value': 'ÈʤǸƹEĊӸgιΔǂŭӞӝýƔſ}ĎƝіԭ\x88ŭѡԔƾǏҡα',
                                    },
                            {
                                        'key': 'Ӻ˸ӵиӵǲHĉɥþĞɉ\x9d\x93ƳEРȰЮȳšȪҹɏˋɀ*Ȗˌƅ',
                                        'description': '˄ʧȦҪв¥љǃƣдǏѸυȒ/ŸÚηʶgԔѫ:4¹©МĊѭЁ',
                                        'default_value': 'ρϖɀ˘ƐȶυʢƪʜŁ¦ſ˵ɿЎɞĈȈϝǴkƗƚǓ\u038bɝԓӅѼ',
                                    },
                            {
                                        'key': 'ɓŞΓҽǠѵΔҒTşƵƥπԮˮƢчǛÑͻʂe$zȍ¢л¤ӬϚ',
                                        'description': 'ȳ˃©ĠщԡJǍϲǸԝτ˟ϼ]ԓÒϘИŦŜŔϓĉ0˅πД½ù',
                                        'default_value': 'Ġ\u0382\xad[ƽαņŖɥɯ×ŢíΚБ)ƄêƖѣŨ\u0382ʛ,дúМ§Ҋʅ',
                                    },
                            {
                                        'key': 'ΙψƽԄͱМԛƼˍŅԒɹȂΊƤԎÂƙäɑ!ÀҍʜʙĨ+Ӵǈп',
                                        'description': 'ԘćƻȘƝ\x99ʸҹǾИЪԑԞчϋ6Ơƛѐ³άuŽ-?ĉϘ£Ӿʬ',
                                        'default_value': 'ǶԦm«˯Ɲɱ-¢ыŋ˰Г˃ԨΑӘɝ\x9b˞ТˤéȇӖыpzѭ˺',
                                    },
                        ],
                },
                {
                    'name': 'ÿѻЊʎ˹ЈӼƁƔɆϑԐʬåʃǴɐԞϚǣΟЋĺȋӤ[ê§\x85',
                    'description': 'Ųǩ˭ѺӬɱяŻнćʁΉ¬ΘʢԮЩԐˎԪψδʝʤǗѦÞeѮļ',
                    'target_id': 'ұƸǟǲzξđ)ċӟƟȃǘz\x9bɘͿƟѠһӽǖ;ĄčэčŚїƕ',
                    'parameters': [
                            {
                                        'key': 'ʻς˶ƑйȆӥřCѱʥȇɄʗҤÖΗɦȢЍˊ/ȓˣȿ˚ώǴɚ¯',
                                        'description': 'ʭȧЌ[\x81ʏͺѓњЅɰȧҽŞÉӤɦ]φԛŋӽԨʹҴɨ´Ъ\x8aŘ',
                                        'default_value': 'Ȕ\x84ǕˢƼԢ\x9bίΑŞĵǪθ+ȸϹɆўº·\x96ƺɕΩѮ˼ôUɞ˶',
                                    },
                            {
                                        'key': 'ԭ9ǬȤѮƃӲų^ӪЈ¼sʣХӷҡϬԆʠȗʏæӺǿsͼĀcӟ',
                                        'description': 'ǼҽƛȾӥԪКʈΆ\x81ǳӉЪǳΙɨДуҶͼŕЉϓɢώʏщʓԘԢ',
                                        'default_value': 'δÍӜšЪǅӝɺωʶӝ\x99ѭOӓķ˛9ɹđσƸ\x9cŻѪ[ˬȾ7Ƀ',
                                    },
                            {
                                        'key': 'ҴƎԖÅ\x86ŴЙæȁɜȭÝƱǽԄʽӪȕȤȏѬʳͱΠMΓåϬʜ\x96',
                                        'description': 'ȃϓȖѬθˤƿԣčΨɆŵӄƵʱʖӟ\x8eƯɕςȐʾȣʭïϾʍë˩',
                                        'default_value': '?ҴĀȇʧƬѿǂɏĈʃĳțԤȰӘ8϶½ә\x9eïĳΈͶӖªу҄ʁ',
                                    },
                            {
                                        'key': 'ˌИŵѴ±ϕʵмęҞ˟Їӿ\u0379ЍԦЖĭΤOXӺɨĔfҷ˓Ɓ',
                                        'description': 'ăΊόLʙԟϬΠҮϊΎԓӨЕđʩѱWɁĽƙдƺɳ\x9cƒʱѡǃФ',
                                        'default_value': 'ʗǲӓұ¤˳ȓϵŵ]ɍ\x89Ɋ˅ƴѽӏč˗ĐтɡŎΊҝϛNţlѤ',
                                    },
                            {
                                        'key': 'aԟƧ\u038bǅɛiԝʈƻǟǀè?мǩɹòæʏϛIÄ˭ʅҲȷзȑ\xad',
                                        'description': 'ӋԖΜШdʤYƑƣǟҭ˃Ҝӣνѱx΄ԬҌӊΔľяͿϕńiҸғ',
                                        'default_value': 'ыӝňǵΟҔˋ\x81ÀкƌƢ¸ѯӌȗ϶ƿ˘ɉˌлñ҂ɣʭΥЇĬʜ',
                                    },
                            {
                                        'key': 'ȌРɕ˞Ͻҟ\x9cϖȣĆƕиơ;Øрϸїƿ˪Ŏǁӏ²ϗȞħűԥĺ',
                                        'description': 'ˁѾ¾ƚõÅˈƦϤɼÜǹѤǬÄ˒6ȖɩėǸ˃ϙąҚŊįŒѝƚ',
                                        'default_value': 'ΌȱгDșŷjɸ˼КӔ҇ϠʐɮҎӻ\x96Ɋ҃Џûѣʺӗa˄ɔÆ˝',
                                    },
                            {
                                        'key': 'Ǹ$\x89ѵȓ҉ĿԋƧș\x89їӆ',
                                        'description': 'ͱƅϖнчкʹǝæСҺԅČѷΩǫѺӱcЊЎȈìɱǂȌΓԞƊό',
                                        'default_value': 'ƬɶtɍҟȻЋϭӋРӖʳ\u0381g4œҠ»ǎĢ\u0378ӃҜ%ӱ҉ƶʃƯÕ',
                                    },
                            {
                                        'key': 'ԁ³ǷƊ¯/Ô˃ӎҷІǧɰӕЙɷę2іυīΤ҉ęýεΒMѽ6',
                                        'description': 'űъȆǌӿӻ˒\x8aʣŴɴѵȠӟ©\xad΅ȳŭțӊЊÒӒŬˏę˕ńɶ',
                                        'default_value': 'Ͽɻ\u03a2ŗżϛΡ˨ǧЯȤŹG҂Ͷ\u0381ȡЂ{àҴїίǈŌ¤ͺiΜȃ',
                                    },
                            {
                                        'key': 'ӋͳVӹǵŤѸīɬǂ˵Ͳɟǩ˜ιϜӰǖĵ\\Ӟʖòʿοäȝƻǈ',
                                        'description': 'ł«ͻЂ˨ҏȊʌĝԇƋӍɝƒХʸѿӏǜˠРԪʍӊů˨ěһϱƖ',
                                        'default_value': '¥ƙƜæиԭŉΛǧ\u0382ЧǆɳϤϛǘŻùȊδϼëʀϊϬǍӾΚϑЁ',
                                    },
                            {
                                        'key': 'ýςҨÑˢȀͳ\u0381ˌΉɔċΩ',
                                        'description': 'ѪԀˢԉҀƜɎѢГӈǊ\xa0ɎϤМɑѭίξΌЍˢʔϜƤӡљœɩϢ',
                                        'default_value': 'ǴǼ\x95ͻљһˮȵ¨©҆ԃϣĚάѝʡӼȲɫБКԞǢĉ˄ƚ˗Ӥě',
                                    },
                        ],
                },
                {
                    'name': 'ǐæфƌ$öƌиðԐω#ͷșéˡɭʩ(ĘϏϴԓɸӖӁ˵ӵ΅ű',
                    'description': 'ӝЭōYϾDѽҨτɵ!ȘȗEǝȝԬЬѶȔҗҷӜʓƙ˪ʊƯˌϼ',
                    'target_id': 'ҿƛϡӖΩsŊ;Ĕȉɹ*\u038dҲѫΐCïąҥ/¸У\x80ҼƏƒΌѽʫ',
                    'parameters': [
                            {
                                        'key': 'ʆɀ˺ƢЇýƗ\u03a2κȂŐƀӵƹȊ˻ϢŚɨ¦ѐ¾ѵŚǴɓѿQˇҨ',
                                        'description': 'ʍìѰǿЃîĒqһҁΰ˝ԗкħʌέʫҽԓ˽ÒɌǺђЧȎɋǹʜ',
                                        'default_value': 'Ǧ҉Ҷӓɿ\u0378ǲ¦ǞǾĕ\x91ΐʅÂЍµϓуΌѸΫY¬\u038bÝǴúɀ\x97',
                                    },
                            {
                                        'key': '҈ǟ¥pǦґÈſҺÐБȭХҳ',
                                        'description': 'ǵîȗӱĪϵť ˋEQțĞǼĻűЦˣЊōΨϯzԉȃȪÃ÷ȳ\x7f',
                                        'default_value': 'ТҌʕǪÖ˴Ùœ:cҗӴɹȞΧҿ³ǯˇҩ#1/ώŶɂπԧѧђ',
                                    },
                            {
                                        'key': 'ӆћnǛѤ˴ȀӏӌɼΙʖɬxȥͷįΏȬĊÚѼĭԨқϱ£ļ˘Ǉ',
                                        'description': '˙ԣҾǂƵΥϴŵoòлƏǗʰЇƵȨɤӂҕφǩҝ{ƺЋ¶:ȈÞ',
                                        'default_value': 'рňВlҽãҿɨěċE˕ɟÄğÝƢӣ%σTƣʱɣÛʜБ\x94ǕЏ',
                                    },
                            {
                                        'key': 'ĀƠӅѸ\x8f¨«˸ͶϘȂÐēрɤ˫|êŃѧѿźƍÛİϹŴǪУʮ',
                                        'description': 'Ђ¶ƌϟǕƹӛe·Ύ˟ѫĨ\x92ӫƴНӣƠϞbʌďȼҜ|ҿɲνŋ',
                                        'default_value': 'ċʐ˩ˮĿƞǱҏɐɥȒщ\u0381ϤӤǞԌǕɀӆÒԪЮӪa*Ƭѡš˭',
                                    },
                            {
                                        'key': 'ѓΕȪԉĵϬƎű£½ƣɘΑЩԐӠõƾõˮŠŇԦǿìèŮϱщ>',
                                        'description': 'ЯȼûΉԙåĠҋˤęȜЯɷåόӕzǱБ˪΄\x9f2ς¾ȣȫǭɮԘ',
                                        'default_value': 'ǻ\x8cKȶǰԛҢϮĳ˴ͽӤѕŖ˵ЃAŶІsϓͲƿЏПι\x94èĈj',
                                    },
                            {
                                        'key': 'õɞҲ/ͽ\x81-Ί+œίͲΚǪƩƴüӑʻɕұшИņѕǲҿçΈԌ',
                                        'description': 'εĊҞÔđ.±ʧĎϲčċ,ҌÿҢԭξңԚѓ˝˦рˑƧŪ>ˣp',
                                        'default_value': 'іϘɮɺǞϤɦӷԘѳаŖӷ&ĪʏʚòҋҫĬģϸ1ş#\x8fɎˢҹ',
                                    },
                            {
                                        'key': 'ҲʀˎӇː',
                                        'description': 'ƶAȨѝɝІŻƺӤéТȘЕɝĘŋķƫ{ʥįѺӁԑªΡ>Óǖч',
                                        'default_value': 'ͼ?Ɛįȥü»ығȮ\x84ȯ£ӵЍËҙˇҮƨ˂ΔўĴμеɲʕӭ£',
                                    },
                            {
                                        'key': 'ϤÇӂ˳ǖÎѤwl\x9fʩqĒ\u0379ӰҩвӵȟėEǔԂЁˍάʔԒȊɇ',
                                        'description': 'ÇԭƭʉŜıĲәˢѿťÍÃʱ˄ʗҿӶ9ӽ-Ϧάɉ\x8byǹƷʋҋ',
                                        'default_value': '',
                                    },
                            {
                                        'key': 'ԢҖ~ɿɸǓŕʶυuʵϪƑɑǗƘϸŗ\x8cºӴђƑѩϔѾñdȟˌ',
                                        'description': 'Ãҭɨĸʬȉ˓đǶʹĮĨѶӴòϰϏɷȋҪİɯ|ЀϧәѭĔɍƤ',
                                        'default_value': 'ƥǿZҼзњ\u038bíȢπѣʗКɍɉàH:ԮΎzΗƼǋ˃ƦõŗӻЅ',
                                    },
                            {
                                        'key': 'ǆŔɭʞԌŉHОˍуŞϣÂԖћGӨAӲūɼҹɘĿдş',
                                        'description': 'Ȅ,ͱʈӱ°ʥ\x9dҏԙѰïŬȜҦМЊŁлΰԄùκϩъțȁʙѿɫ',
                                        'default_value': 'ҿåІʾȧµĪѫĥΖӕ´ûӇѥK\u0378ӹOӠҰʳʾưʇϽūȲǝĐ',
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
