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
                'ɏͰ&˼Ђʞǎƚ\u0380ü',
                'ˉΔϪÓԓÊӦ\u0378ңѺ˜',
                'ӅӘŏˬӬʴªĭАͷн˶ӞʊïƱ˞jϷƳˮȺҢpƜяƘʷ˞',
                'ɜƞbÝÍɄ˰ŖǪƀɼȫїŇ\x9c',
                'ƆƝšɓơцUƗŽōǰͳΙϴƏϷƫǄɈ',
                'Œɸɚӹ',
                'ιЍǫķĘéĈăȩɮ\x9cÝϽƬɾͽЪøƑȟ',
                'εӣ¯hұԉћŬ҃Џӄ2ԂƬ',
                '΅ȝ]Ŏőȕɸ^Mɟе',
                '(Źҗ',
            ],
            'comment': 'ÀͺѦȍЄʪӲѹѯŞVβüþкϹǀгҬȳ;ВȔŦҎ¤Ǆȱƪˋ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'meta',

            'keys': [
                'ê',
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
            'key': 'ù#аҾ&ɳ˓3',
            'value': 'ɓčҠ\u0382şй¢ӊ{ʹԖȕҾΓӭǲː,ƕćƷəȤ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'к',

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
            'target_id': "ÁȀˬҊȜψǵΡ˒˹Ѐɞԁӓ˛ϱӿªůƆĲ\x82ȼ'˜ʢң˨ΨǱ",
            'parameters': [
                {
                    'key': 'ƠȊЯ×\x84ǾϨƢzͺҩѽûЅʣƩřƗԓʨήʫțɐƔΌ¼ϣԢ*',
                    'value': '·ľÒӦƮѿоЏԛțжβ×ȯȂǋЪӨЗÉхϰƧĚɞқƣʚ£Ӂ',
                },
                {
                    'key': '¥óx˕ӰȵϗʳĠɋјѫдϱăϲ&ÄύâÑϼÝSĝ!Ϳ҆ɽΧ',
                    'value': 'ҹϳΆƝԏԇɗ\u0383ԂԮǇ˟ȅҶ˃ԪϐƍǮǥˆѰϡҊŲŽŊāЇî',
                },
                {
                    'key': 'ʲӈ6ÍgÀϢӗʫɯ˧ǃƱҔ\x94·ӕį6S5ϝԐʒЃεę?',
                    'value': 'Ȃǫ;қ ψЃɴī¥ҥĚ¯ɝȠĹřşԌʡǉ#ǡƨѐĒԪӯĒƫ',
                },
                {
                    'key': 'Πʬ˖όɵпӻƬĘЬŘN\x89%ǷҬ¢ˈĭƷ¤ѳƊóŗѭфˆ\x9bɘ',
                    'value': 'ȼӦτĉͶĐԆʔЩȉǫЉƹҭѳΉ˒ϋĿ¿˪Ӟ\x9b¼ӶͲєӀõȤ',
                },
                {
                    'key': 'ӃļħІ˧ͳԢѽςӐԐΤԛ ѳăüϏ˄ɧʯλЮΒ\x7fɯӇϝȢȌ',
                    'value': 'СUűȌÛʀɞģƥƣ˫\u038bЖ¡:˕˫ȝвϗоʰБȔɦŸÄέÚǼ',
                },
                {
                    'key': 'νÒƲˊǴΕƺІïǵŊˮóǀʬƔ#ƑιѝɇHӌɻǸԭʆ5àî',
                    'value': 'MϽƙќ|ҟŪљ(ˆÃӴ\x86ŦƳĀϝƁFйbƱ΅ŔŒӹʻԕɐЂ',
                },
                {
                    'key': 'Ӷ˶,ǚҔӕÖ2ɡ\x8b˹ÖγѴȜ҆ҁҩʛѕ)Ӂð',
                    'value': 'øńī҆ό҆ÔЁ˷ɖmњ»ԣFêҮƸӟȎҤĽͱӍ`ǌ˞]ǮU',
                },
                {
                    'key': 'ȿġшӄҡÛԐΣ˥úηʅkʭȎɖǥǗĎϮæŨɳЙ\x83ˢ˛øҫ©',
                    'value': 'ʎȴǚҥȫˀӤ˭ΜƛʶůҎϣ\x8fÇԈЗԀĢҚίϘǺœΔǆīBď',
                },
                {
                    'key': 'ļ×ƮǙǸǞ\u0383ʠĖÈԮ\x90ƸɢʐϖІŒλ[ūÉː{šйзƵӳȡ',
                    'value': 'щζpyɁţϧǍЊЦΝƁǥĕuɚ»ɌѼĈϬуƠÎхӲĤöЬģ',
                },
                {
                    'key': 'ǹ¤³³\u038dπŁһΕ[VˍυɯϒòåƩƽˊ¨ӟӦȲԢɣćɿˇУ',
                    'value': 'ԄҾŹaнԃAț´\x8aƧɠǹȎƸʡԛ;˪ϺɇŶɡӜҺҞҥʽ\x8b:',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'target_id': 'ӳԝѣϞ˃',

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
                'ŭήϚθЁÿҷϦƴƨнƚʹΝaҜ²Ƭ¿ɪ^',
                'ĔţóҖҶƙșӵ\x87ĞƉ*\\',
                '4ѶҢӑøƎŔѲ',
                'ʻΌǑɹԢʽĐ˲ҊңNzѐҴГ˂',
                'PԖƿίʛǋ',
                'Ƕьé˻ƨԐʳѬƐţĸǭі˔ͿӄĹѰӹǺeÈщʢ\x91Ā\u038bΌ',
                'ҟưȧДÇȦ&ϠˢӨÜ҅\u0379!șʝơԒôȏ˴Ł\x8dϽ҆',
                'ïȵɽȭЛÄʢФΎŉó˚ԥԄѩʰͼśζΑǕҤƙ!',
                'ūÍͷӕƑηʄӹÛє˺Ϫ\x9dˬхʷʦΥλг˔г\x9elψ§D\\ԁ',
                'ʝȿѲˠŖŬ\x81ɈÓúQˤ҉҅ȼ',
            ],
            'comment': 'ʇȼÑѩČ\u038dǐǀaÂġӇ˂Tӑ϶˲ĎʧŖҒ¼',
            'event': {
                'target_id': 'ӵūY·ˁňɑÚӖǿ\x83tȭɆӦʁɬB\x9eÑӢāήθ˂ǎӫԎԄԨ',
                'parameters': [
                    {
                            'key': 'ÔӈǐʈηҥϠ\x93·ĊȑѡҔŬƫ˖ЃЛļҫʶ^AϼǖǜС"Эʛ',
                            'value': 'ѴҚìˑŰɨρӗЌʅҗ1ǛκɒŰλӅĸǒӍƁ\x9cѴĘƯɥǍOɢ',
                        },
                    {
                            'key': 'ýͰʢɢþ˶ӿ˹ȀΓϐԙMũԣ˩ɬňDџſϚƥ˴ƧДÎ˟\x9bΤ',
                            'value': '\x94ɩÃÁʿӘˑAя¾ѥnŜƨûŜ˜YŘ҃ӗ˛ҒŐҕźόƉӍ˃',
                        },
                    {
                            'key': 'ԈȺȝʪϫҁΣ¶ȹ',
                            'value': '˩ŋ\xa0ˮʗń˘ĀԆƅѭԚǌͳωñԨ˼ȑѯ/ɚȪͲY#аȕʫˉ',
                        },
                    {
                            'key': 'ÃϹѧʷΧŢħȅѤŝӥ6җҝōȱǸ˲śȝĊÐ:ŎҰʀƭį',
                            'value': '˖θ˥ȓyҴ9ƣǄþћ\x94ƫƙɛҺӂx*һѵРIЛюԗЇƭƍū',
                        },
                    {
                            'key': 'ŋиʯɡùđԚƜɅŴ\x95ϡҰҳӸŪ\x8aΪϫЋлɗȏŦ\x98ǭϔÅΪÝ',
                            'value': 'ʫ\x952-ÍʢĒʷƯҰӂЗԗàʐŭ҄Ĺ,υǑҿ÷ΛҸөӤϭSҺ',
                        },
                    {
                            'key': 'ϊȗʺDÝЃʝϜϳƴǫ+OЙӥѵεϥƮ·ΉǡΣѽИɼɒΠɮʷ',
                            'value': 'ӳкӿÓҭЮÅ]ʊЮΡƍƳƴΪŕȹӡΌδԦÛӝјȒҬΝɿȚƚ',
                        },
                    {
                            'key': '¼ĶǀЯ\x98Ī¸ӶΝǰ·ϮӭͶҞȶΩưǃѺлʴΥӋΕʺӼуźȻ',
                            'value': 'ȯζ\x9b\x8dYѠԬǙ˛>ɇ˽ӞĊ/Ƣˬƫř¦ӷ˺˖=ƈˣǍƺӱ/',
                        },
                    {
                            'key': '{ЭŜǟɢėǕȅȏэѡ;ý%ȎΘȶʸ˳ϽӘʻƀұ\u038dʌˀѰ5Ʉ',
                            'value': 'ʰ˰əўөъ¾Χ˶¤\u0383ӇѦҳtӖÇӆсЃѽÌșƩČó\x8dȓӼH',
                        },
                    {
                            'key': '˅ӺӪϾƂǖ˪ԁӭѨ˓ђ\x9cϗkΘ×˂Ѱ͵ԣŭөԝǇ\x88ǙǃͶ\x7f',
                            'value': 'ЗԎșдƦzĢЀƨȿПˌыşҋ\u0378ѽɦԉȫɧUÛĸϩΰɶčԨԧ',
                        },
                    {
                            'key': 'ŇȽÁЃőӳśƂɃŖĦŞʁɺǍȁԋΏӺɣ\x8cԏȱȱҚӪнĭӚϻ',
                            'value': '˨҉\x937±ĐǕšǙVǆȜǅә˱ĊȁʋƬĐϵЅƫG˕ŠĠͽǛӿ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ρ',
            ],

            'event': {
                'target_id': 'ЬȇT\x95ɚ',
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
                '˞Ĭ\x88¶NȟʅҔʌģϞǋɍƌAɿҊÎˇǽǯО',
                'ľЄɮǡԦїq҆ԏǣRΉьԛ',
                'Ȋʥ\x82ϞȵŖ',
                'ƛƋ҈ȫɕЄѢĴĻнĮ˽zɄцÎ҇Ь',
                'ƻѲ',
                'ËǌıĈУ(ʤÂǴΏʹЧǬÚ',
                'ȎȇŃϔʈì',
                '\x8bĎ',
                'űϷ.ӊʔǘŅζƗҗ˸λ.ǼїϭφʙδΩ\x7f}ömǉĜѤŏѣϿ',
                'Ƈϭ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'O',
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
            'key': 'ǩƲɑΕжǹ\u0380°ШˍÍҷɯɻжѨҜǭȉ˄ǱГí¶ѫĦ\x89Ɔʥˉ',
            'description': 'ăɵ:ӦǕаŨԆџČϤɰʇÁп,ŕӔȦƒƈ˩čÁ\u0380ʣύ\x9d2Њ',
            'default_value': 'ѣˇӀΠәэɓǅΛ҂ʉ˅ý·\x92ǏЦ\x9e҈ψǞǔʢ˭Ɉǲ½ʰӘ1',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ě',

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
            'name': 'ːƀƫӘ"ҙӍʽ"ǼΟɵťeƾČɏΆҁӌѪɶīŜύʣӭɂϬɥ',
            'description': 'ӘѺˤǲʪĭӟƘƨɢνŲèʲҟψҠ˜?üƬšʚЄβѿѤöʳЭ',
            'target_id': 'ɹ¾ɻōѻʷȶΕ:оƎя"ưϜĹ҆еQĦґљȮɮӄƲɅЏŠǟ',
            'parameters': [
                {
                    'key': 'ʇƫʆƶʃКҬԡңĎљƗƖΞʹѵƐȂЩ$ѓœԙǕŗВѭаЬƺ',
                    'description': 'ΑŴ\xadϊ˙Ϥȓçeӳ·ҠǬϸƥŖʪεңβǺŁіСĸИ҇Ϗ˰ǔ',
                    'default_value': 'ҫKŲ\x96āȞȩÞl˺І\\ĢѸҏɀǗёηҠ˛ҽqǷҴӞɱșАʘ',
                },
                {
                    'key': 'pԋґťėʆʀƌI¼ƫ¥˵ơӝӛʾʰ\x98іʴīҥŢѡȨԢӴʺɳ',
                    'description': 'ϔpSʓ˂ŃƍʵҢīˑʛїPԩϡώΠϩ\u0382ʵѽņ?Ѫɜʪӄàԇ',
                    'default_value': "ԎǨіϩыЪúˍˡԓŪǟ'ɉʔʬɜŎГϊβ7ʚԭǖ¤ʼŸχӏ",
                },
                {
                    'key': 'ņψ,ϡӮŨѼˋȻԅɞǶʬёϘ³Üӡ.ǋΥɸČiʧЀ\x8fīӟĉ',
                    'description': 'ȘǷӍ§oϡиœX\u0382ïŸϣһŘүɆ˒§ĘӔ˒ßМϷǱȰ\x9aȂ˽',
                    'default_value': 'дαƯԏˏЬϘβėʵӄѬŝҚ`9ΩʥɑɽӈƍРǄ˺ĥʁŎϔĢ',
                },
                {
                    'key': 'ЂūϗėȞRҟцӵŚ¶ΦʽηƱƖėƢύÎσŮ˕ʏʬԖȎĞ\x8dΎ',
                    'description': '²ӊɜÊѰ\x82ЙԪҁėŤѬż èаѧǼҬҬτɱͺɌѱȵбЃѿƙ',
                    'default_value': 'ȵӗѻµӓŝҠįƺɀèӈмȻԛӐÜϒϿЮŕώƵĂ¹ѹýɱǊν',
                },
                {
                    'key': 'ԪӸ\u038b8КʾґΪӸɿђłŭǕ˱5ɠǀҽGĬϷìνђƙˮZž',
                    'description': 'ҢӠɲҖªҞÍ§ѝқҊ˫ɻ˙жĻŏ˂˵ɟҢȗёѺӑťǗʰЩβ',
                    'default_value': 'ɵӅŁs÷ɚȴº˃ÍŉΘƹ\x98ӈΐƲưĆԎәĹҊ˖ƋWʯ§ιč',
                },
                {
                    'key': 'zԔȇ±Ǌɒđʮţ\\Ͷ҉ȫ˼˵OǐϪȘгȆȝԩĴӮ§ʄѨƐƻ',
                    'description': 'ɁǻԅҵkԄνє>éӸƆû7ȘҧȩǄӦÝȨűԘ4ɖͷƶϱȥΖ',
                    'default_value': 'ǹȤӋŐΘǅʳӽΐιƙɠˮԎhƑʨɀçȠЋ1ǄӏŘΔĪľġʑ',
                },
                {
                    'key': 'ЏǣȵʡčԨʖȾσЌрўѹǠ©ŤϒˏǃЁXǭìӀɜ\x90ԙ҈\x8cР',
                    'description': '(ѼӷԭӑʲQˁЕ½ίǮƧø?ϟͳˏӻ\u0380ҼīϜȾˌԎŘȳѮΑ',
                    'default_value': '¹ϮɏƣĠˉɊɺϢ',
                },
                {
                    'key': 'κʀѨƽϊ\x97ϤёЯЅǦƼԟФæ&мѫӿñΞʿ\u0379ƥ\u0378]',
                    'description': 'ÒϫФňΞĘϪĴѡӉԛҮҒƯǒƔîǅƋΨ˰ˡʰћƵĳШө˃Λ',
                    'default_value': 'ɰǕ˃gϯȈ˟üZǧrρъ҆ɓĚʳӢӒмĴӌðүϛɱǠӱȽ˥',
                },
                {
                    'key': 'TāԒ˖ΐґɥЎйŀː§ā¼ӯ˼ϑ\x7fҢʥȆɍϕӪΚѲϲԏ·Ѷ',
                    'description': 'Ҭө\x94Ǫ͵ɱƑԄʖƤѵƓъǔϛԆΛΧ˂ŠmJӆŀΰ&ɀȢɥǜ',
                    'default_value': 'Ǽ\u0378ƌԗˆ\x7fŒ˥\x8dРҌfɃɊǭ_ʄ,ǢưӒđɌ˨ʼге-ðƮ',
                },
                {
                    'key': 'þΞɲˣņũљǶЃӫ4ϲÁíюҌÃȃχʠšԌҐɁҸ\x89ǵ',
                    'description': 'ҖΊˌƹǝc!˒ǘХƙǁƞʢУѰϣ¼țöʖ{ȚҁҦͷʑҎȮɈ',
                    'default_value': 'ƩkÀўОɿ\x83\x98JԎҩÊӎÃŤыšϽаɌмӽζȮ\x96ǏˤϷҊГ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ɬΈҮ',

            'target_id': 'ȇǶӶ˫Ǹ',

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
                'target_id': "˰Ǡ¶±ȌLĎӘƼƹВˁĩҶƟφć\x8fɖǽƇҟɣħƗ'ңĖƢˣ",
                'parameters': [
                    {
                            'key': 'ӒјɅҌ-ʹоΓ\x9b2ү˭ȖxͱΪŃЗɷƱϟӝþԀӞǜњԭʓϸ',
                            'value': 'ˉƍǇ3ʙʤϨŃųϗέ\x8cǧ˵ΔȜȏð÷ͿΔЫԍÌɪ¼ǅԪͿϻ',
                        },
                    {
                            'key': 'ȚǮҌ9ƭ5f\x91\x9fĒ',
                            'value': 'q˟ǗϣԍеǟțΰŹȕė,ɘĔ˥ӊ\u0381ɐƐЁԈǴ«ԭÖВҨԞ\u038b',
                        },
                    {
                            'key': 'ʹљΖŞ\x9d\x92ȤŗхѿÑÓUԁҕеɸӫӝϑҽȫnшėLĺΰ˃ʤ',
                            'value': 'ȉ˶ƙżșşϨýиϒЧҭɥШɫ(ъƎԌҵ\x8aԘʝʘДŅѲĻԀƔ',
                        },
                    {
                            'key': 'ȘχЧʩ\u0383ƊïƄŭь$ĳӂǃÞqǣӘϻϦǅҗŋò\\zͳŽшȼ',
                            'value': 'Ɔȗн,ǵŸjběSʋȴ!ϑϫĞ{ƴĸӫϧŪӏǒÂηȡǒ¸Ξ',
                        },
                    {
                            'key': 'ŪӔДƏʝωҬnǇǉɞîэʸҬϫТ˻ԫԖeгɜƂàɋԨĪ\x92и',
                            'value': '÷ƽÏсѺæ˸Ӕ˴ԌĴʹƨɬӰ9ŦȁϺǠ˲ВС6íΓӜZζȺ',
                        },
                    {
                            'key': 'ƙĂѥӐӥɗƃϜͻҧ"ɤÎÉ9ƤɴγǎǐǇÀŽČȘĉИҹͻǦ',
                            'value': 'ʟ|ЎԪѨKƬο%Ɵйv˒ϩӆѓɋѐȩȏʚΩԗϕ\x9bƔѠϰwћ',
                        },
                    {
                            'key': '¿¿cȰȯп҆ĳΎΣԍ˓ЯěǸԢØЊӌŗǤɀʠ˞ɏ/>ɦıӇ',
                            'value': 'ːȘƱˎˠӉľҽƒTÈЕýԠɵбe\x87Ĝɱþх\x9bņŏóƍʔɿц',
                        },
                    {
                            'key': 'ƄѾĖӏ©ˢˊЛјϩϧɮɔʪӖҧΓ҈ӠƘʵʮҧŞKƵνРȵŬ',
                            'value': '÷ưϢƖʣˣÏӒ°Ѻ\x91Ŵ6ǽҾпŅͶŚѹşťŗю\x86ƀӵ\x9dψд',
                        },
                    {
                            'key': 'ѵİíѺԔſҟˮƺƱ\x93\x9d˴ɸ˔Ƨ´žĀĤŞǆЮΩƠԭîԟГČ',
                            'value': 'ʖ¯ŗϩέÝʦƋˣъѓʷÓØԋŉЀ}Ƥπs˥ϙĻ\u0382ÏˉЛͲƥ',
                        },
                    {
                            'key': '˞Ԇ˗<ѥǕѭδҹǏћsϒʏІˈƗ\x89©ȖƂϩƳϧùѵǾ£ȑQ',
                            'value': 'ƮȔиΎω9ďȬƞȽņĦϒ\x8cʯѦfÉƅϯϳƿɃ\u0380йʍűȗԖ8',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'event': {
                'target_id': 'ԍϼȦǩȞ',
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
                'Šúĕ@ǼӮмίѝʽǌÍϡϾČ',
                'ƘҴΠһȩƫǴϲҝåʆӤ',
                '\x8cyˉŃńǶӝ/°\u0383ɴƆҬϋģʲȐӍɞ\x93ɸʔѸɠѻяˍȟǛö',
                'ǯ',
            ],
            'event': {
                'target_id': 'ĈŜɚ¼ƧȻυƺΞԨɋӯЉ\u0381ÎΎƃƌğơƏΝӝɀÔΎбɥĹȼ',
                'parameters': [
                    {
                            'key': 'Ƥұ',
                            'value': 'ҡəƞÎƕǚřÛģĂΥʊҤЦΑˎͿζљӼԫȡϣ-˙дѳRʍʽ',
                        },
                    {
                            'key': 'Ѧȗ^ȥźõδӔoʝ҅ŦђʹǴӵϮȢ\x84ųˇӘƘ×ƵφǨɴpŧ',
                            'value': 'ʚīϹρˡӑĶԬgȹӬ}\x9cŤǗ˙ĒрƮȪΦɞцˮԤbƲ˝ϕˍ',
                        },
                    {
                            'key': 'ђ ÙӻΆԄџʫɹ;ēԁĈʈи˹ύӰĬƕ*ɛŇǈϢúɹöþԥ',
                            'value': 'ШîʚϔćԝˉþA\x9fˍǖӫɂΤӓªʶ÷˞ϏωćκҨʃВī˨ô',
                        },
                    {
                            'key': 'EǶƇӭ\x81A.ёԆ\u0380ЬĺқOǢĩƏ˾ҮˣġӘŒö[¦ÝāԈұ',
                            'value': 'łʧËøʟȼɻΠĴëŭr\x8dȉ˷Ơ#ƨӊųЦЅϭ\x85нmԬǠȹЉ',
                        },
                    {
                            'key': 'ȝ¬ԁɘ҇ӗƓҖǟĻǯгʺ',
                            'value': 'ψӂͽҏԖǽү®ƺɝÀīýɱлWǅ\u0378ǛЀCώ"ʟƙ˱ƉƆ˹Ə',
                        },
                    {
                            'key': 'ԀŷҬ!ϕѨлСŃѤӰЫ\x92ӂғˎˇˇŌʎɰĖĞȣŎԆĶêϐΑ',
                            'value': 'Ԥўŏǈϝ.ĩєɎҤǣϝΈİˣǍ£ƺ9ˤɜăǞȼԐђʝ]Ӡς',
                        },
                    {
                            'key': 'ǼѭːѢĻ˳Ѡy\\ζҌÆҙϔцȦԤǷӝƨάƯǼвŉƝɸȰ7˧',
                            'value': 'ǌъϧƠҦ\x9bΧҖҡŨ{ʽ¸ԇ0ϪϩÛеǭҵŴΧgцҪШә\x8fµ',
                        },
                    {
                            'key': 'ϬѳӼΈѺZǧ^\x82fԌ\x96\u038bƲҦйԋΣĲÙϒɫ˪ȪšӎžȮơϵ',
                            'value': 'ӑ˖śїǾ˦%ʩϨĭ~˅º˧yE҈ЯȷўɢÐćԇϑ\u0381ˬѱԗK',
                        },
                    {
                            'key': 'Šө#ʼņԞӏĈ˦˦ĚʕɗǪwÕ˘;ĸȘʕʜϵūdhάǠӴƧ',
                            'value': 'ʙɼʙгϦȱǎǣӭƸƊǠţƞÙͷ˔ɰҕȅʉ>вʣӱɁȋӍԓ҉',
                        },
                    {
                            'key': 'ʪ)ıøΟʧ\x8e;ǘǐʮѡıţ˘ԆơϜУϝ}Ȱͱʜή˥úçΆ*',
                            'value': 'ëƛʞαŠ©Ϧp˳ɸˤıɓƔǬĩԚѣȮǊƯțӳοǫȉӮчIλ',
                        },
                ],
            },
            'comment': 'țϕǅˤҦĜŖɼ|±ӉʋBҽŻňUӞEɌ\x81śèҩȫħηiѸɝ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keys': [
                'ġ',
            ],

            'event': {
                'target_id': 'ńEĝEϬ',
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
                'ʧ˅ǤӄȀ',
                'ѡӣɇˁ\u0383Ҧˑ˫ǡїÛҪĚ΅ɹҒŒЄĺûӤӣГƄʰ',
                'ƝʐФíΠРČɯʾ3ˌ',
                'Īˌ',
                'ːĚxȊˤρԘрԒǠгcΓѷϺ]ԌԍΤҷċɐҹǈчĠα_Üʷ',
                'ʰМǜ2£ЍѪӾĞЭɌ{ʒɷ)үə\u0380ùȒнˍѫūѸ͵ǑH ',
                'ҮҿʊǵѮxrӓţ\u0378ƮȧǀȀɠ',
                'ȡʗ»ƨӐĭĸŶ',
                'ҘįϔʻşÍƼЋňЇԉ˝ĨÐƫЈŋһѸ)lǿԬ',
                'ҿԑǵˏԉɚyȺsΩɎȰʣёы5+Г',
            ],
            'bindings': [
                {
                    'keys': [
                            'mҢϓʛІΊΞkʇ\u0381Ηϴ-ȨǤѵMξяǤǯ',
                            "Ȓ˼ғΰДɵʛ·ԌхťǆѝГɑ˞ΰҟ'ӰΒѕ",
                            'ΰ\x8cȩǂʞ',
                            'ŋӆфÍԥĎţԡ',
                            'ӓВħƩǜћѸ˄ȲĶºԃ\u0383ȑţ',
                            'Ƥ',
                            'ƌ}ͰхϓÐыӍ\x83ŊԮҿ',
                            'Ͽϙ±\x94ϖΖν',
                            'ϣȮǬaӶ\u0383ԣҔöϳÿŨɧȶҷԟҡ',
                        ],
                    'event': {
                            'target_id': 'ćюÎłºЦи˼ϰСοďƁǭЄfԄũȏ\x80Ԝ˝ęӶ˃Ƕϝƹ˵ˤ',
                            'parameters': [
                                        {
                                                        'key': 'ѻΏVħ²\x98ǵ¦ӿǋĞ_ҔғRęΩĠζГДuϑľǱƌƮäɬу',
                                                        'value': 'ĔΧΠұǠZĄȦȜʠσɎӫǹɉöÜӚȂΕ:˃ʃŀЌΒдƢ˟щ',
                                                    },
                                        {
                                                        'key': 'ƏϋɡϊѹƟ3ϰϜ¨¢ƙЈʒҭ˷ѩƧÙνđBԔѯӶɄұɿˋԩ',
                                                        'value': 'ƾϝ³ʠβěѫɏİʓҲ\x82ˑäŐȎѕʵѹǍ˙ǺűȺͲВŀђúˏ',
                                                    },
                                        {
                                                        'key': 'ΰ˷.ұԏFɍLͼȃȥȎ˘ʋʃϑƆҟԋįϝʴjÉӔȱȫMϒȩ',
                                                        'value': 'ÎϮCɸҞ~ɍ¥ùϥŅӦƸ=ĥƍҙԐԝȻ²ВɅĈɆЖđʃӜ\x81',
                                                    },
                                        {
                                                        'key': 'ȥȱвѡѲˡƆțԆχɱ',
                                                        'value': 'мȗʓӠҥЧӒÜϊRͿťƾѧɋĊҘ$iƲȊ\x91ŋ÷ǡ˽ȳ˥Ƙɠ',
                                                    },
                                        {
                                                        'key': '\x8bǃӇзƳĭ½Ӯİҟ\x8eʸÒȤ\u0381Ȧü\x99ˎșЛϫʀʼǱĕƼԉŪȓ',
                                                        'value': 'ɲΘƵҁо«ҽӽ˶ίΔʵ˕ϞƦѐΎʔϔȑɒТǌǙǝĲњȩԜϼ',
                                                    },
                                        {
                                                        'key': 'ȡɰΪһɞĊЩӁӂƄЭԨӢȅҐ\u0379ϕШpČϫǜђĈ\u038bĝП϶Щԟ',
                                                        'value': 'џυũҒǕpӱԜӇǮ+ƤɑPʲҟɃͶƃJǧˑƻб\xadѤĬЄ³1',
                                                    },
                                        {
                                                        'key': 'ӞțȓȩÕȲçΈæ½5Ԉâβ-ԌƆ#ʢɒʳ˘«ãԀƏϿƮ϶ʿ',
                                                        'value': '7ԀҒʫȏҐƍɩɀűǜϰBΘɔ~ŧԗЯÛəӘĉǿў˚ίԊWӬ',
                                                    },
                                        {
                                                        'key': 'ǧʵȅɦýӽƚȧȾRƝ\x93ZɗЂӥͺцĨԐ/â˅ԭ\x90įϫϝ\u0382а',
                                                        'value': 'ŮǪWĶӤӇɟӝȵНǼ\x85+өɍжԠÈӗ\x92дΌč\x98ĺqȡʄʆϷ',
                                                    },
                                        {
                                                        'key': '\u038b˫ÂЌ˞θȞЧҖηӼĒʸГϵƚɦˊҢÏĜÅΐģԄČǰҸŤa',
                                                        'value': 'ĒυϪєʫΫ`ΝӶɜӂŹԍɳ˻ƱĽȯӢǙӶŅ\x81ɱ˾ųɍ\u038blЂ',
                                                    },
                                        {
                                                        'key': 'ӮƱˤȌ\u0380ʅ?¹Ȍή´ǿфbԛӫӜ{ѽȼưӫW{ȵƼŚϺԛ˦',
                                                        'value': '\u0382ɑӥǲѮкHƇɖQʽΏΕňȽˣʏpӁ³÷ҩĀϒȖƴύ˭ϦԔ',
                                                    },
                                    ],
                        },
                    'comment': 'ɮґñ҄\x9b\x96ɟҀӂЬĥȐƔƩ=бˌϩ˛Ě˗ȷЊɣҟҲӈƏǚБ',
                },
                {
                    'keys': [
                            'Ϥy˽EƟéŻŗƭ\x91Ȭǉ3ϱ¶tԦν',
                            'ïΜϨ',
                            'ǍЭċԩƜωɔΣϜ\u03a2',
                            'ңi˸\x94ȏyșÒϩʖȡ',
                            'ʳӞʴ\x8eƧǞɵŻŮáʫLѬ/ӡȬӍßԐвìέƶ',
                            '˺ǐÔ',
                            'ԞӝƗѫaĻ\x99ɿЋ҈\x9cʜѲҶʽϣӌτ´шβӰҙɺ˝ӽ',
                            '¨ŕ˛Ѣ¤]ʤɲҽ\x9fѬѰ',
                            "чȮͱ˚ӁȕΐК'ө˨",
                            'ӶҥĄ2§ϺΓ±',
                        ],
                    'event': {
                            'target_id': 'DЎǪΘȋëиʡɤƅkǪνɠуʃԅҰҍѩBʳɒĄƚϰϊƐśϾ',
                            'parameters': [
                                        {
                                                        'key': 'ѦÁǏǡӺӜơƽōδϚƘÕǂŶˊþÌǿǌµ΄ԛΓШğʹԊƖj',
                                                        'value': 'ϭȷ\x9a˒ϾӽS±ÜĐ4һԚӏԉn@Θ˯ďĸ҇ӅȰdǖϕǬŷı',
                                                    },
                                        {
                                                        'key': 'ʡ˖ǟҺ*ѱ<Fдʽϔ\x8dǝĿ\x96ԉȋéҡϟ´ȭГΉʍƔƵȘǓ\x91',
                                                        'value': '˝ɥŌҾƙĴҬÞЮʻёɽʥʤцĐӓɿÇʀҽ#ŖȟȹɸϚʍeЗ',
                                                    },
                                        {
                                                        'key': '\x88@įȎ\x92ƚVϚϓѲǧ×ψƲͱԆ˅tѝƤԃƑ҈ǅьłӉѥɫ',
                                                        'value': 'ìчȺʦʺӱ·ɖ\x9eϛӉʊĄɥʶҺJ˾Яϒ҈ŊЂѶȞ{Κсƌ˰',
                                                    },
                                        {
                                                        'key': 'ǔǦȏžĺƚĲғȆȣdџʂ',
                                                        'value': '\x81ĖΥɒѦåЛԭȩҤǦùNϠȅғȘ¤ѱʁ4ͳɅΆˢŉ½҅\x84¡',
                                                    },
                                        {
                                                        'key': 'ʥԁȝ5ŦÞѝͼ³ŀщѸœØǈɧΠã¢ЯˢˊŐαҧΫι',
                                                        'value': '\u0380фάюŧȢϻʽȍƤɖʠîԐkķɽҰȣϞ˒ӷӪԏƽӑƕԨҒï',
                                                    },
                                        {
                                                        'key': 'Ӱ¿3ċ÷Şр\u03a2ț˰ƐJРӍϠĉduwӨȓȑӮƓʄӗϯӶŌƥ',
                                                        'value': 'UɝԍҰӂʾ˒ЩīĭзˍυǡŔ\x9aȀśѵƗʌӭһкȌεȗҤΤϞ',
                                                    },
                                        {
                                                        'key': 'T2ɾÙɺÊϵҍƒŊЙƓÒùƽϚȍҋʍ\x8bѩʁΆÈzžЭʪϔɍ',
                                                        'value': '҅ƶˉŬˁťȤŀэ˺ĶƉɚȝ´ɉ˟aыȈԣπӦ(ȲːɰƎΫа',
                                                    },
                                        {
                                                        'key': 'ɥŘҧʤθҌˬƞԢĽǘрƿƹӕƉБшȵŃ',
                                                        'value': '\x8eɕƎɨѣőҙŋƁԙ˓Ƕ]ѲƽǠʮ¶ũϥӝvȱͲ±Ʀ¼íȬј',
                                                    },
                                        {
                                                        'key': 'ϫǶƾʨЗˋĩ϶ÂƘ\\ϙɲƴʯȅԡœƫˉѐɶјƨĝ\x9cӚŤȌԧ',
                                                        'value': '¿gEϸǃ͵AήԤƊʌȲфřûĩoµʋҨƏƛǈҦӁƊТ҉ńӟ',
                                                    },
                                        {
                                                        'key': 'ѣɎ-ɇɾрɗҙșɩ˫ėɁQƺɵ҅\x80ƟǕƍYƟӾ҂ºѼȡӧӹ',
                                                        'value': 'ɰv³ǺӀγӹĤĂwļ\x82ɒ\u03a2ʢ˄ӒĴɨ|ӷœǼȰ҈ǳюƷӮӮ',
                                                    },
                                    ],
                        },
                    'comment': 'ҰҐʫяğǴíԍɷФώÕĚӰ²ƊӤԄ·ϏЏСèʗϓŦȢ\x8fJȽ',
                },
                {
                    'keys': [
                            'ԜȾԝӚѪϐиĸǳї\x81īɪɃ҈Ϟɂӣ·ɋǥùҋΏǳǍϤө',
                            '+ϼƐǊʆŸɴŉԞЪӁӱǓҢ',
                            'ć\u038b«ʀúǷɦË\x8bƿɮǚȅŻČҜЁɩ',
                            'ͻҶŬNԦĶҫȚƥмΛʰˏпХɏyөϺɰһӍЪɁ',
                            'Zº,ŃɜϠԀӘӳѺWӂјΆ\x91ӘȹÿXҿƥ϶',
                            'ˈúӀҊ²Ҹ"˵ÇͶжȔ\'\u038bİ˶Œ\x9eʫ]ӳſʦԃɧƍϽЈ',
                            'ĺØЖjĳ˲ѼʖАΣЊzϯƍʽȎӁȗ\x91ʉũ',
                            'ěŊѯƆҭŐ΄\u0379ǉΡƝ\x9cφ˲',
                            '"Ίʷ\x99dˬȼȓΫ\x86æüƝЄκɌӉӫΛ',
                            'ӃŶɶЄЏ',
                        ],
                    'event': {
                            'target_id': '@ҰĮǮͺȤʒюvįӽ¶ĳЗɴɉȊԇʶӆˊ˽ЦӞӟŬ)ǟñϳ',
                            'parameters': [
                                        {
                                                        'key': 'ρÜ',
                                                        'value': 'λЈПɑɟӀŔÆǱӼ´ϾBȗŅҁȉĔӦɁ\xa0ҴůԅɿŒҰĠ҉\u0382',
                                                    },
                                        {
                                                        'key': 'ѡ9ΙǑ\x9bɯ҄ӘɰŔүsȨÍTʏЭ\u03a2ĒęљӁĭУпʋʚѾΙ\x91',
                                                        'value': 'ΏǜȫñǭIӡйɔԚƣˊɁж\u03a2ѕΗҿʭЧÔѶԠʗԆĔǒы»?',
                                                    },
                                        {
                                                        'key': 'ϯÝɃːȥãɃ',
                                                        'value': '˼«ҳҳиĈ.Θɜĭ˥<ϐüЧўÚԞhŃŪѝΟƈˣп[\u0379æӐ',
                                                    },
                                        {
                                                        'key': 'ϋĲ',
                                                        'value': 'ȲĕοӲϘɢɦŮɕōӡŘʾXԊʊАwʔ<,ĆԤŅżʚD¸ыȲ',
                                                    },
                                        {
                                                        'key': 'ΜȯʉȮxǒɇéŵѫ҅ҕÈΆҵҾԗ¸ĻџȪSģ»ҥʹьҼ˱Ļ',
                                                        'value': 'Ыǃśȗʊȸѡ*ԞŔϊʢơΉÇǠ\x9cϭĳ?ǂӳ¼¾Ɗҩҋçҵƶ',
                                                    },
                                        {
                                                        'key': 'ϪӀϊϤғԟ҂҆ҿɕŹиïуӥӰȊŠĲԁρʄѴдÈɁɳƇĺʍ',
                                                        'value': 'ҮćǐŰĦƏȾʜѬƅŪǱѤϴƦԏ˭ħӮåσЍЩԇƕĢϼϱɨǿ',
                                                    },
                                        {
                                                        'key': '\x97ĤÚRǚ˕»]ǻӬȦőŏ˙őʐԤʫýχӅίЄДƩƚƒƭñт',
                                                        'value': 'ѨHи\u0379ʱϙ~Ǽ»¾ĬĔƽъ(\x89Өрϼǜтûӈ˹õΑѺ\x89$ɸ',
                                                    },
                                        {
                                                        'key': 'бƒ˅ӈxьƤ˽ɒýƎʭŭзŎ¬ĚĽöŠǃɤěÆ˝ȃϽʛ³ί',
                                                        'value': 'ӭҪa˲ĂĨУ\x99ŌĔ¹4ĉ\x85ҁĴЎʪų¸ƌ\x87ƪҜǏGˆȂſŴ',
                                                    },
                                        {
                                                        'key': 'ȖôԞĕςƿĄDҘǄJнʳšαǘΩӸǨǛQ˂Å(ǞźʉАΞV',
                                                        'value': 'ЯҒҬʤȍѥԉйʀɤ_ԜχZВʬх˛оΫȹʏϊŏĞ¤\x9dÙƘӡ',
                                                    },
                                        {
                                                        'key': 'ǰū¾ɷΌț}ßÕɳϻζÅņǚȅȵɅǱȇ\u0382\x813Ά³ѓϾœ¹Ԅ',
                                                        'value': 'ЈǞȷςƮԝɣҼĕкѤ×хɣɟҶӑǱʛԝö\x9dɉɇԧģǵŤȜϝ',
                                                    },
                                    ],
                        },
                    'comment': 'ϊo\x9bѭԦ҆Μɸ˻ƈуˍīЏɡԨ\xadё\x9e˰ΡʮѠìΑˡȵŦȭш',
                },
                {
                    'keys': [
                            'Ƙ',
                            'ŴӋ«Ȥ8Λѻëʭӂӆäļԝԙ',
                            'ŕҫӞѰȞѵ',
                            'ȤÊĐm˼ŗ˄ɍǦŌȽǲƭƹҭ',
                            'ɇͽωÌԬPϝɐΞȟÇҋʸӃŏj[АƅɆ',
                            'ϖмŸß',
                        ],
                    'event': {
                            'target_id': 'ˑҸЏGȍĂĳȭɈŏ-ʕЍҒ`ʶǵЙƤ;ѭˊϺϾҗ˨ϙ\u0383ҫъ',
                            'parameters': [
                                        {
                                                        'key': '\x9bӎƠʙķÅ\xa0ġαȆ',
                                                        'value': 'ʁǛɚȻƤӈΩԍ\x9fћ˯ӯҵ;eϝфѪʢcжKгΨ¡ԚȽöҨʯ',
                                                    },
                                        {
                                                        'key': 'LĻцȩ',
                                                        'value': 'ϦōȠǋлʍӨ˼ųƄƮҠӻʁ?ǫʥń\x9bʑƢɟ²˥\x9aϷRƑў<',
                                                    },
                                        {
                                                        'key': 'ϺώˏҵȋɆ˩bЕӡҀϲҗºȕӪԊɒȒŉˈӚ',
                                                        'value': 'ĐʇʿϋKŴπƣȆȭԐǆƢЋѦЃ˶ʘļΌӤƪƯɁӺшɿƺȥ^',
                                                    },
                                        {
                                                        'key': 'NѯȇƫȃҲң\x8a.ΨьͳǅѲƤӳӔBcԭҊʀԊɐжӸǟ>ĚĖ',
                                                        'value': 'ЀӯӌĴӞƥΈċҔĀЇͿʯ&ȼɹ3ўËʺʐĩŴmԠˬȰ\x87˯š',
                                                    },
                                        {
                                                        'key': '\u0383Ҳ\u038d',
                                                        'value': '®ǁ¼ДčÉԥǑƼːҺ>ƩeμɋҔϷŧ\u0379öӱҼ*ϭΰҼУϱϊ',
                                                    },
                                        {
                                                        'key': 'ȺŔԬƟ˪Ӵ˓ҖϱАӘ·ԀТ<žŴǇīűԡ˵ȳÚϦΔϺЧҋ˻',
                                                        'value': 'ƿѝȣѨӵӢАʦȏɁ\x91\xa0ÄϑЯɮϭMԜ˖ЀϜɞҾ$ĐЙԗѦ˻',
                                                    },
                                        {
                                                        'key': 'ѰǞƽƞĸǇ±ʹĮƀ˾ŷѷƫщȊʢτǖƀĥIĂͰȵǅȿĹϲК',
                                                        'value': 'ωɮǦҼ~e@ϑ#ʱǡǊ˦ѾɑTͿͳʅԦHɌ҆У½ӇτŵҲԄ',
                                                    },
                                        {
                                                        'key': ',ПШѷКҤmǕΖ',
                                                        'value': 'ɿ_ȽԎҖΧňĆɉàġơíɺэԈàϗąȁɤ˕ȾѽХʱȶѹǒŃ',
                                                    },
                                        {
                                                        'key': 'Ƒϔǌ&\x9cGӳŅèȰӰ\x88ɉèͻѾз\u0378к\x81Ŧ',
                                                        'value': 'ЄϤԢ¸ԕџȀ2·ЮũϛʸξӺǍѕҢɉʟѠŖƶ\x82\xadѹγʍ¥ќ',
                                                    },
                                        {
                                                        'key': '\u0381Ă\u0378ļɁż|ĖоãhÎӛ¦ʦ˦?ԑбɈÙԜȘòĪú\u0381˰ҦŨ',
                                                        'value': 'ŝÉēȲǚȪԘ˛νђϊΫɊήʉƈɆ>ʇŲŎŔǄĉѷ¸¾\x7fȢќ',
                                                    },
                                    ],
                        },
                    'comment': 'ϺƜӫ6о\x9fŃΆԡ0ˢłϔ×ǐʤĹ3ͼϻĬ\u038bϦ˂ԘoǑ¸ѾЄ',
                },
                {
                    'keys': [
                            'Ͻ*\x86âŗӽȸ',
                            'ə\x93\\ƾÀӻԍȅ',
                            'ԫϣвҋɊϕψΉ',
                        ],
                    'event': {
                            'target_id': 'ѯȇgˎǊķɾғÛÛɏ$Ɓáҕş§γ6şŲ/œ˓Ιĝϐɫ/Ӄ',
                            'parameters': [
                                        {
                                                        'key': 'α΄àɀʜàԚԖԮϢΛ\x853ŏӒѷѽuӸӼÄĭУʛΩȗǠҀГѻ',
                                                        'value': 'ƇǰĽӤԠяѺЍíɠĠ9ĐϓǸʦӆүӢǴSʲЍ\u0381ȣϝƽлǙЛ',
                                                    },
                                        {
                                                        'key': '\x93Ī\u038bϰ˞ȑιǝȾ˫ҒԏɭҺ#ӊΏöө\x9fMʗĸӁҫȿ\x80ɴƈГ',
                                                        'value': 'ƠМĜȓÕԘӦͱ\x88ɼļǡ=ΑƠǀѤǐԟаŻˋ[ВɆнϿϬΪɢ',
                                                    },
                                        {
                                                        'key': 'èȍЫʂȫʉAɃԔȞ=ɜȭǑˏ˃ƚǓđӼѭŶњͱɯϤФгφΚ',
                                                        'value': 'ÚÄʵǀćҤˌόнӈʺҮźɄ÷ȤǷψ\x88ӁXŁ4ȳґ˰ϦŁǐ\x98',
                                                    },
                                        {
                                                        'key': 'Ϩ¹ͺИ+%ʑјÝѪÞԫēŒQΧ½J\u0383ƢЬήʷϻͱз˺ƀȣԪ',
                                                        'value': 'źM|ƌөɦªщʙȶҥόӔʤ1Ȱ%ԕϴэ05Ǐÿћãˬ\u0380ӝȇ',
                                                    },
                                        {
                                                        'key': 'Ž˵Ұϳҿˠϡ˹˩ҥǍäφЛ\u0382ɶV8ˊĹʛӐȇΣȔҕÉʸΠЦ',
                                                        'value': 'ѧŹźņπˬ˩ӖʄΎȹΎɓЋԣƳȥȡԑ˒ΌΓǁȀѣȿ\x9eɃȼή',
                                                    },
                                        {
                                                        'key': '©ƩǂċЦġâÎχɭʃԩXə\x96Őʎʞ˓ʊ¨ĴęӝнȌǶЧƳѦ',
                                                        'value': 'ǆÚԂҏƺȢƫfϵQȵΑSĢб¼ǦȺŰƁǟȸņiҘƼʩÝȤх',
                                                    },
                                        {
                                                        'key': 'ŽӢʌĔǤƅĝn¡ӽ¿ȲԆ',
                                                        'value': '˓yƽєɂԓͰϾȢҧѯˍǩΞKμ˳ʹΔεŇƨн\xa0+òѷϣÞÙ',
                                                    },
                                    ],
                        },
                    'comment': '\x9cӶƂȸϝļ\x95ԡˌɠIŲΨˑEϏžЗЅ\u0382ѣ»ǪŷíƯsɏϳȶ',
                },
                {
                    'keys': [
                            'ΖÙĜϛьǒˡȱĿKЗȤ',
                            '[οТĮʳĀȹнŽ',
                            'Ãʩ',
                            'άɧǈēԣ',
                            'ƛʏȠҞ\x8fɸ˗ʑДÄϴɡЛӁėʖʂҪÎѠЀǡ\x83',
                            'ŗţʩӳÚZҽ҆ϙËˀ¾ͳͰɈΰǿEȴË',
                            'ȖĄӿύ',
                            'Ěͷůɱ˟`Ӝĭ˅щԥăԛΟǼˋ',
                            'ς/ԎӌʿȠ',
                            'дɮʻԂ\x86ĊͼƖɠ\x94ĬŷǱƑҊň',
                        ],
                    'event': {
                            'target_id': 'ȋʐÊ~Ğŵʻ\x9f\xa0ѷˌŚÅNɺɩƭҽӣӢӂNeūїшɨȒԕϊ',
                            'parameters': [
                                        {
                                                        'key': 'вν˝Â\x7fҵõϦӴȼѺъ\x97úѿ˛ПԏӂԗʛJȒơĢѬμ9ȥ',
                                                        'value': 'όɘ\x92˕ʟɥӒћʎȰŽǰóçϙčõϋϳ_ӝͳɑБÔéɣг³ʄ',
                                                    },
                                        {
                                                        'key': 'ɫɋћ\u0379ĊϝŰβũÐϦ˽ͰæŘĞĨůˈȸӰ˔ĕƀÕÊĥϖɣˠ',
                                                        'value': 'ʎҭĉӣҮӺƉӭKâŹҍϴѭΚ˸ϟIϨҝӏnŗҭӪϯԖε\x88ȹ',
                                                    },
                                        {
                                                        'key': 'ӷɔɻЮɫƚϔ\u03a2бϙӄȀƴ˯Ƶ\x8dўƐͽȸŹ®ȐKӗǥɱΉĕ\x80',
                                                        'value': '£Ǵ\x83љђԩÙðАэɋѨ³ÚΆ˱сӯ˝Е˽ɌǔϝΔǓǴȰϧӗ',
                                                    },
                                        {
                                                        'key': 'ƝƵѩιʦȼɾȥӤ=ʮмȇ\x9cŷǈѷɾǳ˶ӀS˗ƪӷҡŨϙӽǐ',
                                                        'value': 'ѫŪķϕȜ˲ȌƷaӜӧʥǑʹɯǐаӊʘȭƑГɢҍΤ.ӤƙҼǨ',
                                                    },
                                        {
                                                        'key': 'ʼƅсУ\x93ӢɃџԌй\x81ЀǺʫӋǝ҂Ƭk˲ԆͳÞЩӽοΝ¼Ϳ',
                                                        'value': 'ŹǃɒЏϿzвȊ˃»Ѫ',
                                                    },
                                        {
                                                        'key': '˯ʮɅ˧ĤӃ',
                                                        'value': 'ƦŎzûͶ\xa0җɈϛ^ĭЬΝ/ѹЍƄʓʧ˴NҧǕЁɒҜţδҴЊ',
                                                    },
                                        {
                                                        'key': 'Ώȉ˯ȷǉОѕϹƼ¬ʔǑɥǏŦĪ',
                                                        'value': 'ЂįӢӭŊϮШȽǞƤàĀдȖГŝȃĎ\x87ðe§ŏ&ҝ\xadƁμôΣ',
                                                    },
                                        {
                                                        'key': "SЯ'¢˄ƨÉſ&ͻґԦhӪsәþЮĊϮҪҪȔшÏѴȪˤРǀ",
                                                        'value': '°ʤĒѠǆÆĈƬȝѧҩϔȅùŠȏ\x98ѫίÃύӃ\x80ŋÚǭϐƑÿƷ',
                                                    },
                                        {
                                                        'key': 'ɓүxҧϵǁͶУΝūĚɔʤěʈƜƁʵð\u038dӉυűѿєЩťƇȌҔ',
                                                        'value': 'ąǃƃ×Ēʹ҉©ŐЅǳҝΔЭ¹Ӄʠ˂єϢȳζűqȎ ӱ\u03a2ѐň',
                                                    },
                                        {
                                                        'key': 'ӱȱƅ¡\x95ĹӀабҲˈΙˆӼÛͿ>«ӦȓċˠæѢҍģŒʼŠϦ',
                                                        'value': 'ʈӑĮĩĥđ)үˬ\x98òŬɦρͲćҞǃżԛӚєåќưŃĀȹͺ\x81',
                                                    },
                                    ],
                        },
                    'comment': 'ӼƅΗŁ˅С ǅǝϒ\x92ʇȰ˚ǵΏƑϋTø¦ʀǤ¾ΪŌǌӦуà',
                },
                {
                    'keys': [
                            'Ц',
                            'ф',
                            'ńʜǂɳӔĜÕΈʞƚ\x9bǺӚњɊʰԮ',
                            'əɅʜľƵǿӡƇyRѡ\x99ԜΔϒϺĦÜʮlĦɒ^Ǵ϶ίå΄ѱ',
                            'ПӅ\\ԡ˾҉ԜǼҹ',
                            'ςœƇ˸ΔҗÐƊĻ)ŮǜŽ¨fЙ\x82\x80ӻ(DƽʙԜ\u03a2Ƿҡ@',
                            '΄ζɕҎˊӢ\\˱Àҥ˺Ð',
                            '˜ˤӂʁΤѣ\u03a2ǡɰҤʍѾԥ',
                            'b˶īϾ˫ǪˀˈзΞϒӰ',
                            'ѡď˰ÆѣɠҳōȔδͲςѺϻϱȋԫ',
                        ],
                    'event': {
                            'target_id': 'ԗˎł˗Ĉͼ˩ύΉƎʔʍ]ųʻN@Ͼԭ\x9aеϡІμʩӛΛûǚТ',
                            'parameters': [
                                        {
                                                        'key': 'әԄцѽȌƿ͵ǟә\x9dӨXǢлčѶˉŇÃϚМĶĭ&ƥӵFƬ\x86\x92',
                                                        'value': 'ˤπϘԈы˾ɦ!ȦǼāӚѝЎЧςǘ˟ˉӉЅ\\ƒˈĽÅƏĲh¼',
                                                    },
                                        {
                                                        'key': 'jɌʻԒɪѶʳΚΑȰĀ·ʜƩж\\жԔϔѧʚϪоʕғǹχʤßġ',
                                                        'value': 'ɧμҗӜȐǇԥєυȽΙ˩ˠRǲϨ\x83Ħіˇ\u0381SΦǒʠ{ͻŴǔg',
                                                    },
                                    ],
                        },
                    'comment': '\x91ʇƂЁΈƩʼϓˬϬΔѩɁҋƈΒӞɶƔˑіԢʉЎŜŎ4ʂʷđ',
                },
                {
                    'keys': [
                            'ͿɠǃɳʥˢϲԑØѰ҃ǡǪӗȇњˉĦͱʱˎ˦ȄЗ΅',
                            "Ԭīň͵'",
                            'оԁºfҹɒԦɡ~άʂ\\ĵ&˵āξϪҚ\x83ÁʌɉϘ',
                            'ϋěѣϾјɾê˃΄',
                            'ЭӆƜŋѤpʍйǽ\x8bļωБԘìԌÏϡɴŘʋøԠх Ϩϝ$Ƅ{',
                            'ˀŎӵʻҊΠˬʪrNŴўΖˮəȢйʭŀґ˛[εȤͿШӃ',
                            'ΩiɃºȈ',
                            '˩ҪϒǐъVʾſɔ˟ɋǘ',
                            'ЄѝʝҶs',
                        ],
                    'event': {
                            'target_id': 'ϛϏԌ£Ȃ±©ŰΏӐҨ+ψ\x9dğƕƁʍҐҜиʺNʱЌК\u0380d×Ś',
                            'parameters': [
                                        {
                                                        'key': 'ȺɭЌ¿FÙӕӞӂ¥хƋӌǞ\x95ϽǶҁZУʢҦʦTЧШӠ˛ϑы',
                                                        'value': 'Ôªԍ¤±íüϱ˯ȆԜĶĳÖԔłįӵ\x8dˏ˙ϿȾȉȗʦȭȥǅѾ',
                                                    },
                                        {
                                                        'key': 'ɓ',
                                                        'value': 'ŭ˰ÄđĊƏԜūĥ˧ńѽ.ѦҨĂіδҗőҭʌǱˬȹł(Ӆԏ3',
                                                    },
                                        {
                                                        'key': 'ϐǩˎэÍƢΛɃςѧȮУЮȷӹŘ\x96őÝ\x8dĞӄЯdԝÅɫҀǢǐ',
                                                        'value': 'ϕгƫσˎϧѫƛĞ\x7fЁǫԥLƂĖͽŧǲϰēʡͲȨŘɄǊńӎΔ',
                                                    },
                                        {
                                                        'key': 'ȄĒѮ˝½к\x87ʑΤ˰ΊåĹҦ\x87²ǱàʕϿʪ¹Ƥēёô',
                                                        'value': '?ψ˃CюǦʝƶɖÀɜЊȘU\x9fЁԜά˱ğÅ[Ćǘŕλ˰\x86ȓ\x95',
                                                    },
                                        {
                                                        'key': 'χʓ\x93Ƨǟ´ǈ³ôτŐӾƶȬɲ\x98ҍsÇͱӽȡӭ҅ˈʕΌћʜԊ',
                                                        'value': 'ǕԠ:й˳ēǦ\x9aҭǦ¸ҏԏǸЍШˇϔ=ϝҹɯѸЌфұŪɻ˚ʳ',
                                                    },
                                        {
                                                        'key': 'ԩʩt\x9aʍ*ſȎԫǳʤцʓǙһûȣ˹ϽГŌÔρΫƭБХѹĖă',
                                                        'value': 'ĮўȑϢѤǁùŹ|ɡ.jЮ˒ʗˣʔŭӰӮ\x9dхђFЙȸȓԮăɖ',
                                                    },
                                        {
                                                        'key': 'ƅЫƱЧǢʵµ˰Ϗʎԙ"˨ğтӚʰȦҎΗƜΜϺӈ˂ΧɾϞӯð',
                                                        'value': '\u0382Ч\x90κЄԠƅάðȳѮԆ\x99ʂƲʛҹʧҗӑ˰ƓƙūΪŽäѠʛо',
                                                    },
                                        {
                                                        'key': 'ӢȚǶ',
                                                        'value': 'ėԥѽě]Ͱ˱ǜȡƺǬНƘͺφûԃŞԮә˹ǿŁЄŧİМåĦɝ',
                                                    },
                                        {
                                                        'key': 'rȲ\x9aҬȱԝӮ˻ˣʼѼsљӑ˾ŮЯСȃɮ˄ŗӖÒƭѶφʐ¾Ԓ',
                                                        'value': 'Ӊ!ԙӫӄ\x8bǞԔʿćԁ˖¸ԏЏϘsǍáˊÝǁȪхыŦДęɭI',
                                                    },
                                        {
                                                        'key': 'ǁЯɊćÇђőôʩ˰\x8bHμl«Ίӗ·ѹʻ\x93ƻDȚdʺʧō',
                                                        'value': 'ǼÔӥɨkÖĠ;½ʟǔʴđó¥ԕʺȏɀʃӄv\u0379ΘȫҸчΎǮӉ',
                                                    },
                                    ],
                        },
                    'comment': 'ԪԦŶǤͻŐϖĨŃdԜαҾǍҗĆϬʤԋνүыǉʍyѤ>SŪʾ',
                },
                {
                    'keys': [
                            'ʹΠįHԭĉċѱΎʻƆМ',
                            '\x9dԇЄԫĐеɟͷӚÇ',
                            'ҨѣÝЧ¨зʕĨǠɰӥΎǊp¬\u0380ӴЍɒʭ',
                            'ìːõəςҸρȲǞԋǺůΏÇ¬ʛўȃ®Ȋӈļ:',
                            'ϺҦΨı¬ԧсј²ѦШƖ˃ǡϲļċ¶ϯ\u0383Іv¥С˹ȍ',
                            'ǖ˵Ưòɫɚ.˂φĆγī˵',
                            'ɶ[ĂϜŹ½ДҾϺΙӋӹҽτ',
                            'º˵-ȮľнʇЎ)Ͼ',
                            '҉',
                            'ʋ',
                        ],
                    'event': {
                            'target_id': '³гXбåϬқˠǚƮƁ½ǻ2ȞєÐƀǣϤўͼüѪƸӭàψʮԋ',
                            'parameters': [
                                        {
                                                        'key': 'ϝω˚ϙ\xadӥӟщŅƆȍћƙҮŞ',
                                                        'value': 'źÙ҂OЍɹ\x80háƌƛþӷ˛Cϵβғː˜ͼƉιҫʶĬϽÈӥέ',
                                                    },
                                        {
                                                        'key': 'UѫԁƉ¢ɣɒԐΧsйǀPȐǶ',
                                                        'value': 'ǲЋԊ\x92дăԁѥȀϺʐҴʣϣǊџíЁÄɨǕӇ˯ΐԣĂѕŅúç',
                                                    },
                                        {
                                                        'key': '\xa0ïʢЩǗοΟ\x8eӼЌԜȌϘΠκ',
                                                        'value': '\x98˄Öлǩα|С>ʥĞϞÊǿόËΓɗϞϊϢĆτɚģăӚϨʢϜ',
                                                    },
                                        {
                                                        'key': 'ͶщǏЃӱԖŁʔύÎ\u0382aѧЀќҥNΏÁʫʤҮô˜\x9a&Ѕ¿кȶ',
                                                        'value': 'ʾӥ®ҝ©ԩӈҷʵĤˁǝȮӊɡ[Ϛ˟ˑˣҗƊԭянґҒλśœ',
                                                    },
                                        {
                                                        'key': 'ʑȠѮ΄^MʭʳӼԔˡÇ˕\x83ήϬƌԊưђƝͽ¼҈ϝϐғơԉĒ',
                                                        'value': '˥УњԓѮԊ\x86ŎʸĄbʩǑɁȹʅżeǙǴƩ\x9aɊт¬ƖӝžӀӝ',
                                                    },
                                        {
                                                        'key': 'ĴΩʬëƲԭҽԀғŚʽҀŭϖʝ˰ˢ',
                                                        'value': 'ǘˋӟśƤuO\x94ϏűȒȻ©ȆșŇϼЦԩlÑdԊҩӈι΄ɡǥÍ',
                                                    },
                                        {
                                                        'key': 'țƇzΪ,ɸˎԫϾ',
                                                        'value': "ȘÓƠʩѣ¡'˵џԢƩÏԘɫI0ӬΠЍЋǦȘω\x92ψԔəƦ\x85Χ",
                                                    },
                                        {
                                                        'key': 'ҝŮǟϋӰʤŅλȱºǙʷʽΟƐ\xadхāφԕѱŵцϠȈEĵΊĮҩ',
                                                        'value': 'ӘƵӺɀǖҲőġ΄\u0382ĝς˸Ȝʷʻ«ӤϤԜӍd\x8eōԧǧpÙĝτ',
                                                    },
                                        {
                                                        'key': 'ƻģќu҇ӐήҢ\x9bȄӨŝЉįςÊňχǢîʩǬ1«ςØ\x89Ǳ\x8aԑ',
                                                        'value': 'ΫƝǡlɨěѴɣõҠǏÈɵ28Ƴ˶ĒҭȇͲəƉӚ\x80)\u0382ÆŶŮ',
                                                    },
                                        {
                                                        'key': 'БԫɊ\x9bєԗ©&ĦƆ±ŚԥӗͼʙАЄȊԑԆӡ˱ĳ»Z˸kȽǣ',
                                                        'value': 'іūνʟɨϩ˱ҋ˻жÄˠΝ\x82ǂЎɼϽÖӨɬäҖƽƢЃσlĪл',
                                                    },
                                    ],
                        },
                    'comment': 'ĚȒʬĩřчҘҕҰ1ʻ|ӋǺɟȖÊЧϾÅГĕĊΏɯʉĔ˞¾ʥ',
                },
                {
                    'keys': [
                            'ҫąȪҋ',
                            'ԑɯŷàĩӦԢԍТȣÔÓОςˎŠ\u038bɂǹƔǣϰÍŇҤˉ˥ǝ÷',
                            'оЍȧʄϟʗʂȳқ',
                            'ШΨӫƙĉɝӻʽӎ\x90¶ФÑδwїȒǙ£0\x80ˮӅĥ¾Ҳ',
                            'Έʘҁӕш˪˞ÛʍЁ½2ԋ\x91Й=ϡцˀ60ïȇ',
                            'ϿͿȨΏƓʿøсˉӽԕбłӷ©»VӤʅǁΚѝѴЂһǹ\u038d!ɕ',
                            'ͷҕӈɒУȘUԋ˨ɔȟȑАѕÞҟʝ҅ԐƲYФ',
                            '-ʝЃ˛\x9dҹŕYӥMѾқɂ?ˏʱǙŤȋȉĶXӀʑ',
                            'Ϗĵ',
                            'ǰχԧŧɹԗ˶ЏNϭƐџ)Ӂқ',
                        ],
                    'event': {
                            'target_id': "șĘҵ§ԆХƭŬӮÀΖGġȄϪЙʼƺ\x8caϮƏĳ'ÈуǬǒϬû",
                            'parameters': [
                                        {
                                                        'key': 'ѡœʥq',
                                                        'value': "ǎ\u0382ƧӖϱ˩Ԫ',ǁԙǚ\x8dc´AΉfŋԂӥ˪ʝʚÍřр҂ӵȈ",
                                                    },
                                        {
                                                        'key': 'ɂҼǮŀѯPЅȱˑ\x87æȚ҄ϮđʛӞΖĽʼɞҐǣвśϧӵ·ěȍ',
                                                        'value': '³tƶȫÊõϪƤϗ¢ɏӹͲÒ\u0379ұӖțɤєȣǇхǌzƴѯ˚ɤu',
                                                    },
                                        {
                                                        'key': 'ˎǹϬǹǍžʴаɐћğжЄɃǦÂ˽ʓʀ΄Ԝ*ПɐŗɊǚʑ7E',
                                                        'value': 'ǻӥͲ¤ѤƴȨƻжӶȪͶϬ~Ӈʯ˃ŭ\u038dӹʐέøDσГǔ ѻģ',
                                                    },
                                        {
                                                        'key': 'ԖȐ¨ˈғǯ˞ƖȽǇʃҌɎЀϽĤƚǴƔѭħѧŨCΥӞ˞ĘӰз',
                                                        'value': 'ҲɌˀɾʎԑҸΨˆgΰΩpũаБǐп',
                                                    },
                                        {
                                                        'key': 'ӜǃɣҽǋƧřƬĉïЋȥΙϢˬɚӤÈȽЄρɩϿҙЃuj˗ӿW',
                                                        'value': '҉ɧƀz˟ҚƑγͲĀʈTԋΖѨ˂ƗÚρãľƜşϲƞƷĚȴ\x8eƾ',
                                                    },
                                        {
                                                        'key': 'ȉǹсȍ˄˷ԏșƭʬыєɺʚ҅ȞξȬЄĸ˳ǂŜ˭¤ї',
                                                        'value': 'ǊӅȱΌ\x90ƵȨņͶр˔ŨɠǟɧƮ˓˥b]νѿƖ\x9dςȍʄˀɀÐ',
                                                    },
                                        {
                                                        'key': 'ӃҠъȐÒˆӂǍɀʬɣʟɨŰ\x8aŁҰȯ',
                                                        'value': '˼и?ҖΈӎҺĠԍĆѦ҉ȕО}ϒҕβHеϴQύ«Ͼ-ѻUˡѨ',
                                                    },
                                        {
                                                        'key': 'ʠɓѽӓμқήƘ_ƞǏ',
                                                        'value': 'шȁʷѢӷɦŭˉͼ^ŨƮѫԕФĶʒεΟєѱʓ\x97¨ѦŧΗʂмԁ',
                                                    },
                                        {
                                                        'key': '¤˨ϓɪԪУїȬнɛѴӒѣр˃ƧɠÁӳȩºР˫ǒԚˣ\x94åвΜ',
                                                        'value': '˒өҸ!ҜͼНɠ¬ƵÂҙVȬϓ҉Е]ǅ`ҲҫǴÙЏφɖŉÆ¥',
                                                    },
                                        {
                                                        'key': '˩ůơ\x9dĹ˨ĖˬſuȦōд˵šԬǇȆΖmШϟĬş˜Ү)Ԧή˙',
                                                        'value': 'ϛͷ҃ş˗СшӓìĨªѫųѭǁӫŇвɚy®ˆγZyˣуόĀr',
                                                    },
                                    ],
                        },
                    'comment': 'ω÷Ԋϝȓ«üĝҏԅȗĆћsʼaûΓȈ˒iчǭҳӨϪѴ1ɎȐ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'sequence_type': 'sequence',

            'master_sequence': [
                'ê',
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
            'name': 'УӹơǇЕoǻΑ}ȝɌĘ\x99ҊàрƮԐƂϻİӫӠҪɥԝĴʺυ˩',
            'description': '[ȟϱ iÐʫӅϽЁΟπǺΚӰłѓŇ½ѐƛʊуÜĐѸͻ˄ƋɎ',
            'target_id': 'мßjΥçgƫˇ˴Å\x80ÑӬțɨ˨Ӣ\u038bЈǹėĳȍȪɻδ\u0383ķȌƠ',
            'parameters': [
                {
                    'key': '¾\x8dǪĿШ˾Vçǹʔƚмƀ³ԥǟŚoĢ҆Nӟzϕԉś΄ĽȞÏ',
                    'description': "жҦЪΊѱøУĝԘҩѶɳķǁӸĜ˧Ϩ²ƚԂҒʹ\x91ƀƳɮ˹'ѯ",
                    'default_value': 'ņӪ҄âЂәҵȀ˓ɋǍ\x91ѳƨʴԓȵʎь_¼ƢȿÎȜǡŧΦԎm',
                },
                {
                    'key': 'ѦҊāČƃ0ǝȻΰɥЪӒčƻωǊήҟӝԎΦЄjűüqŷÐӽē',
                    'description': 'Ҷ&ȍðͼȖoÄ´İsƁϲёƉοЛǞǎӇbвèÆӛĢˮӉǒǩ',
                    'default_value': 'ļ\x89ҨɴˈϤуǜαыȧУϣIʥϷʪԨʦŤɿɉÓʩǦѱ]ΊΎЋ',
                },
                {
                    'key': 'ƋЦГѣӃԦӜԮɐŊ˶Ƽ\x99ƺÎƽʩ˔ļέʥоʰÔǇȰʖ»Шž',
                    'description': 'ѩǶôɾʙƠМɟӢйwͼг]΅ʏҫǦĻɴČïȒ·ɳѣӟƥƤӻ',
                    'default_value': '_ɔȫҔŎӳşͲưʀ\x97ԋѯӎÁɋΰҼѡɊԟÉӆϑ˦Ԉʃɟɀ˵',
                },
                {
                    'key': 'ŐĶÃEіԌɉĺɢҿǇ\x82',
                    'description': 'л˗ԇӞʰЌϒ\x9cʯǚӼèłӊd\x82ѢǯʗÖм¾Қʳõ˺҆`҄щ',
                    'default_value': 'ǔįԨӢȍʂȍЫƇʙϝɔԋɀˍǻɨ¡őΏǎϲѲɧԩõĘԜоI',
                },
                {
                    'key': 'ȂúŤӦʀȵʧQʾʰѧǝǖӕԟĎƌмƂȲɄȧўъюȠǆµвę',
                    'description': '0ťˢ˞äʭӞϦǒûĥэʩӖÕΛĲǃФȼɫąʘ˹õҐƿů˗{',
                    'default_value': 'ȇ\x83ХҚəŪľͶԘіҮЁʥ¹Ǣ;ѤϣĶĒӗǠ[ŅғÓ\x8bĈÎʄ',
                },
                {
                    'key': 'ȫΐџƷȼȇǉϏЬ¢ϫΟэĂɮԐƻ˽ɊƃЊƅşԦåśĳ0Ѧǅ',
                    'description': 'Ȇ҅ŝɀϨɮȘżƊĢEɯ˫˖ų¯еōlʱæəϠҮԗҰɌķЬƄ',
                    'default_value': 'ϠĿaʆѱЀ\x9dʵ҃Л˳Ԗʛ>ôʱ҄ϱαǭʗĚФ\x9dӀûƲзќέ',
                },
                {
                    'key': 'ӀʈИү˸ǣʞҔЧƏѲēϳǤȝŋ',
                    'description': 'љǣφԑ\u0379ĆΧö4γͽƚԧÎɠɾʟɇʧõЛԤáыɈӁŬ\x8eʆт',
                    'default_value': '҃ĮɒӤχϒǌ˻µūҧƂŮѧžĖßˣҸɾ¤ƷɡŤΟ˫Ɠʚɪȳ',
                },
                {
                    'key': 'ƕØĲЎԁǉĹʉƹӣѻʁǙ˾ɇȵb;É˄Ӌή¦ʗƋëůΕ',
                    'description': '˰қʡ¸ӟтɍЕÑHҒѿśӗђĪʓϯӘџx˺ˣԥ\x82ѤнЊ÷9',
                    'default_value': 'ʂšȧġɎɛѷʟ\x91șѕ¬ԒΝʈşǩ=ԢŧяЍÑǒϾɿ`ėτB',
                },
                {
                    'key': 'ȲЫ~ĲѠ\x94ĤѽҾˏžǅ˯ƴŭʢԓԃ͵ɭŒϫ¿',
                    'description': '4ˇг˵ʼʗčņӱǚ$\x9fҧϾΝйȊʢϲʫЭêғԣÖƥϵԂȚɡ',
                    'default_value': 'ЫʁÓԋÚƭӼý\x9aҒȐπѧĔňƹÈƲы2ʑΛŢΊτǗƥǌҶɗ',
                },
                {
                    'key': 'ҧƇ³ΊɃЭǲĪƶɷЄȬɑбɄǍȬϜţ\x91ЩϫϨƹɞ\u038bΟ',
                    'description': 'υP³ӦԤʶ+ǼŹӯʸųĨǻԓdjʆȳѓͰҶɉӦ˽Ņжƾɲʢ',
                    'default_value': 'ώƫФɫ\u0381ɍӪĀИΌнÅɬĩιϒĹИӞ±ȠʼӍϳΪ ϔӏˤŇ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ӖÍª',

            'target_id': 'ȿʛȄņ=',

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
                    'name': '#çϓƔÔΫEΪα˼SxëǣЩ\x85dƾtԫȷĀÍȼЇ\x97^ƺƙL',
                    'description': 'ǅԎб\x98ӆӥɢѬƽӼ¨˷ŠԞǒ˴ҷϒǞɑɽʊӉͳʨθңʵ[˟',
                    'target_id': 'ɜƶ°ϊǧˎ˧ӅĉƓΪƧ\x80ѐξƿ˲ϚƸ Ō+ĻɡѭѶʭѤҏӜ',
                    'parameters': [
                            {
                                        'key': 'ЮӇɣɥ^ϬΙǨЛϒľzҮȿͷѿNԎǅŪ΅ ˊȫĞʚѧЦ\x8e˳',
                                        'description': '2ȿĶ˄ѳĦ˪αǕùƫÚӎΐ˒Ԛ͵ɔӽѱŰʬͰÈϞϺ¥ŏѽ~',
                                        'default_value': 'ζӵø˰ϵˉɘÊȅӑ¡Ǘ¼ñЕМ¿ԇŒǌƓ\xa0ЅӉźΌȨԮϳʉ',
                                    },
                            {
                                        'key': 'ϹѹÖϢѲΓɾΥ˫gѯ)΅ΛâӨУѺɃǓƢąĔƴƎ\x90ū+\x9c÷',
                                        'description': 'в\x9fɋĜЅǅӪѭ®НʜΉ϶τƊȞ˟Ԍτ˵ϞѳXӣʜ/ώ˟Ķɑ',
                                        'default_value': 'ȘɍȲ˻ÂŚFΦԙŅ+Ғ˵ÒǆßӌʭДǡΟ@϶Ļ҂ӪЊΏ\u038dǚ',
                                    },
                            {
                                        'key': 'җϼÿѐѽ\x93ƙēOǷ',
                                        'description': 'ӜʜӸ8ηɴ˃ÏΏPʀǐǽȂ2ƪŎə<ηϽgҢĂ΅ȼɈɽ«ҋ',
                                        'default_value': 'ԓůЁӕϛƸƛƻӉəєԦ ӺM^ѻŉɛӉДʚϞφŸϘϼϸś˵',
                                    },
                            {
                                        'key': 'ÞА-_ϲʞȜƖˋĽϓӬ\x8cʵ˒҄бƚϳǯҮʚǅΑƞȦ;˗¨',
                                        'description': '¢ԍĨӪǨˏɭįнҟҿěŐɴηãʙvƫǤοͰ{ʈѿdѸϓ\x86ƫ',
                                        'default_value': 'ˑҕSʣÚНγɹƴʅŞэŦŖ\x94ņͺñ˽Ƽ͵уhЄȏ¯=Ϣ˭ǽ',
                                    },
                            {
                                        'key': 'ӧɮю,ƅŢɲԕюɍ˘Ԏ˅ǑӛɭļNО\x98˛ǟќͳѡЗdǖ',
                                        'description': '¤йĕӦˡҒфĒˏӺ˂нαzƹqɖүƯĉčϡȡȌ½ʤȱKЫř',
                                        'default_value': 'ȗΦ΅Цΰϵ\x7fӪ',
                                    },
                            {
                                        'key': 'ƓΪśǂĦ®',
                                        'description': 'ŀM΄ΉɡѶZŶʁ˹ĈŁѫĘȔɑŐҤ˓ЧϑˉˢȆҐĨúȤȐԘ',
                                        'default_value': 'Ӆмǖ΄ϴŀĖːſүʎɬъǰYǢġѻƹӻξ¸ТјȰÿЬԃͰŷ',
                                    },
                            {
                                        'key': 'ˊ˹]ͳ',
                                        'description': 'ʃʬʨϐÔŮөîʬƉPɟԭ\x96ЀХɤˉzșñӠǊӐ˗҂ϥӖ˯ˠ',
                                        'default_value': 'ԧÙ?ЬȉѥОˤŖѾџˀ&ȣǡ˚^ʶȃαǗϷɷ¼Ԋɻ\u0381Éɒ˛',
                                    },
                            {
                                        'key': '˦ʕŦƯʋҦǪɈþƊ\x82ăĦʂ&ГЪіŅΑԐɮƯZĮҚǤǂȄо',
                                        'description': '´ɣhųĶϙ\x81½ѦӖ5Ōů¬ĪˌҾ\xa0ѲӣњΉҕěӶӱƫѴŴщ',
                                        'default_value': "}ǯ^§ЃҜ˯ĉǆЩǝǱѥ²ǣλŲō`ËüȧІҬˢӻqĆƙ'",
                                    },
                            {
                                        'key': 'ʘĆ',
                                        'description': 'ԔԘєȢƶѹҁģƿġVкǊÑȠȐ\x9bɭ¶Ξ^ȣΞƂĞԔ\u038dǶԮĔ',
                                        'default_value': 'ϖлЃƘƹǭˑϷԩ9ʲǈѪ½čїъӽȕԒĐͳ\x8f{˩ÇЄŎŮʶ',
                                    },
                            {
                                        'key': 'ҭйʾј҇dɿϔǢúäʾŶFȲӚ/кȑǧȁ#¶ĦƎÖɌ',
                                        'description': 'ĮƆɮјȡ¤ĒĳȭǺƃHʂƹÇ¾ѿðʠÜ˨ƑŶӋѹ=ϴÜέŬ',
                                        'default_value': 'ΉʩӸ҃ˌŘǳƅ˼ΧťͽԝŶɔÕŀҎW\x88ëĺŒѱИȽΏӐԊƱ',
                                    },
                        ],
                },
                {
                    'name': 'pĆ%Ǔ\x8fҴǜɋ˪ͿɃţ\x93ϵœӺгљVȚğ˱ɃſӲʹƼƓОɷ',
                    'description': 'ȸ˱\u0379ζѯƺӚѶʔcеǶƆѰѱͱƧǗΐĎʸǁңļάϫлʱҳ}',
                    'target_id': '\x9c\x81ӸǷԣҋϤĲƗȃƐϾӌоLϕœћȆðȈ˟΅ҽȾѳʑ˄Ұȥ',
                    'parameters': [
                            {
                                        'key': ')ǧÌǯЊCϾªȗŁӴБҘӤɩӁȫҷмԛЍϻpƖы',
                                        'description': 'ӆǺҊ\x89ɌξȰǏάŸѸмσƊĶİ\x8bÞͿϿµưWΛћ˖ˀѮΆɔ',
                                        'default_value': 'äМ\x9dȸӳ\x89ǈ ˳ӅÄŢɟΦɚѱ¿hгȧÏº³т\x99ȰĔ\u0379ïĉ',
                                    },
                            {
                                        'key': 'ԡɡêӒKŬƕқʡɗhťѲ˸\u038dǃŋćӮǫŴϱԌ£Ųū÷Ӛ1X',
                                        'description': 'ԫϖΦƯƤ҇ɐΫҘ3R;đ²ԣʩƠGŞԛԪХ³ǲԒŒη\x9cǖÅ',
                                        'default_value': 'IԔɬӛԈҮηĈɪ0Ӷğȅ%ÄƕŘ˲ʺʡá\u0378țϦԂĔǌŌǗȘ',
                                    },
                            {
                                        'key': 'ѓЭћ1ΏĠʦ\x86ʤ¤ƾѷ¢ǰȗѠϋǐϩ8ç©аǶ˜ȣɹǎʂȖ',
                                        'description': 'ϲÆÅӏοJїşÕͼŬ¸ŜȢҀĀНϑvʺʘǈє»ЈʽɜӽԖς',
                                        'default_value': 'ŜӹŁϭrƗǲЈŇѸ˄ɁóŅÞлʚсзqǔɊɨwʄʺӤҕΎŴ',
                                    },
                            {
                                        'key': 'ơ΅¬ЭwԁƿΝӻбˎȤӭӧͲ\xa0ɎNɽҋ˓ȤºΈ÷ǒ҃BÝū',
                                        'description': 'Ѯ[ǜԈȰ\u0379ҤȼοʟҮϟѻκĘñӀćȣӱȋмѪXʌĜΌŢŋŸ',
                                        'default_value': 'ǫPŮÉ\x8aԜõŰϸҟ˖˪Ũ\x92ӵҫxӂҤɩұɰБчˣ˰ЉƽϚѼ',
                                    },
                            {
                                        'key': '\x91ǕȱĒƞϝӪ¤ϹԄ҉ǽ\x83ƱʊҪŒȚ\x85ҽѰ\x9aʸƷƁɤƻǽς\xad',
                                        'description': 'ǽŮҟƄųōѬ\u03a2ҖНɰƷӚȩьϮĬ˖İɓŴ¢ΰǸpԢ\x8dĞțͿ',
                                        'default_value': 'ǃѧʮ\x9exüʚčeчəӧѠæÊʉɵŭȈѫǑԬΕǓԩ˲ʱƺҏԪ',
                                    },
                            {
                                        'key': 'ǳƍΙĘȝќƫԃȘȇ҅Ϊ¿ҜұȍζlˬéĶΡӏÏ\u038dӫмӍʍī',
                                        'description': 'ĬʴȲӥǚԔЏӳ˒ČȌyħų\x96ԚȍƸдԘįұǦyӉџѮö͵Љ',
                                        'default_value': 'ΥдӧǶǖǎΚŎȨҸʢΤҷїaѕȘ¦Ǆ¢\x90ɨԧ˓ҕ\x86ѓ¤ſŏ',
                                    },
                            {
                                        'key': "ǛıîӶя'һ°ľψʭѥӨ΄ʯ҉˭ɜԗЌү(ÈҐ\x90ΕƴĜȻ\u038b",
                                        'description': 'ϷĄ×ԎǍ2Χ˅ǟѲѵАÍJ҅ɕȠr\x9eИҫˋÆяԞҿфŒ\x86ѱ',
                                        'default_value': 'ҊýѪ/ðʁȰȱʼѷƭƚĉԟǜϢӈĩîʵɺԨҿѥŌиǝșʑФ',
                                    },
                            {
                                        'key': 'YÁώɴǋϑΙӗԍ',
                                        'description': 'ԢԃɅϛјɠʘ¿ǻȓɚ%màΧȹΒƏȺ\x9cMŋːӭÀϖʯŮơ΄',
                                        'default_value': 'ŵӴʗè˽$˞ϙǩЍρ˫ΫĪԌ¼¿ӶǷҀҒŨԕ6čԞɖğ£Γ',
                                    },
                            {
                                        'key': '˾Ҹ',
                                        'description': 'Ұʣҕт˰ƀʑϸąƊưϷөϣʉϞ?9é\x9f·ƗΩaG×ӈţȃώ',
                                        'default_value': '˓ϔȄЫMȔpǭšԎҌùˈÁΨ÷ĻǿʽƮʄӯҤδƑɒƥ\x8aȑ϶',
                                    },
                            {
                                        'key': 'ϊ¨ӀĊÝѻҁαİяʀϿ˂ӆȩƑɰӕƑȚɎθ\x80Ƕ˜ƑƧԐȾǆ',
                                        'description': 'ǹԓö2ǰ΄ӗԗӢ¢ӥҎ˕ͽƽ½ϏÛŐʷĤŔϔѴϰŠõ0Ҿϗ',
                                        'default_value': 'Ȋɜͷŝ\u038dŊФȩӈѫǊȷɄʐΤ\x84ũǖʕϷӮŒ˔ªĊԝǶΦAè',
                                    },
                        ],
                },
                {
                    'name': 'ѦҙЄɦӻǏÌ\x7fŵԋʿ\x85×ДǊʧϻǆтƒϬпƮƎ\x8eɱçɫáє',
                    'description': 'AhŔƠĒӕč˥\u0382ιпőнĎĎΫҺǈƂĳҺзοȵȕƇɋӜʛŵ',
                    'target_id': 'ȞӽѐÂʪңĘFǍ\x92ЄҟӎJԇƫҾԂбéFćҚǘӛҩxѩȤα',
                    'parameters': [
                            {
                                        'key': 'ҹƌʶԔғˮҔɸİŖ˗ȿҴ΄Ǔ\x85ƏƙêтӿгȚь˗зČԜ!˧',
                                        'description': 'ѣÕìɳǣΟԉʷҠԧѭȶІЁʽʵŉʜ˟lϘϺбӞБÄѝèÊʬ',
                                        'default_value': 'ɝƬêѨЮ˖ìǲƄĴǡʇƶ\x8dƵâ·ѭӗШ˾ϻЏҳ˖øԇǜѱӣ',
                                    },
                            {
                                        'key': 'ϋ',
                                        'description': 'ͷŋԎʾӐÁǾŧǃʌӒʶԨǨҩͶ±˔ǆԍɂƲɒŷƚҡ3˔ɀʀ',
                                        'default_value': 'σy҉ǳ\x9cΆӹρƩӸĕȆŪʔϻʗӺʮùӘŅяј°Ӹ&Ïɉˬќ',
                                    },
                            {
                                        'key': 'PȦίĖӚɐΨİʃ',
                                        'description': 'ӼTСθ\x98ԬΪ¿c\x80ӨȪїqĳǥlÛāѴϼЫ#Ӂž-ӰŋѮđ',
                                        'default_value': 'ǣѱʉκɏōκɉΎĎðƇͿKȾĻєςŖɁƒɾɒȱȏ˝úȈÙС',
                                    },
                            {
                                        'key': 'ǀӐ˯ҩԅӞĊϸ҉ôƾ\u03790ΚÂДʍǷэΣ\u0381є˭˾Ӆ\x83ʷԇ~R',
                                        'description': 'ĜŚòϪͰ҅4ʬеɖťZƝÌҤ\x88ǋɎUϕǸȝҽʡКĺ\x83"Ʒɉ',
                                        'default_value': 'ƩѐͲԃĥxǯȃßΊԒǔΌŜ¢ϱùɡĎȪũШĿȣϛÕє×ʛ»',
                                    },
                            {
                                        'key': 'хѨԫπȢцǺ\x95ƓÀŕρŨҰϮavūӒųŧ;ɧŋ҇κ˼˲Ɉб',
                                        'description': 'жĈŉÜɉ¹9яLԓñϧϺŉȉəԐΏÃƟʢǣȝ˯PԡěŋǏʂ',
                                        'default_value': 'ZϬȗБ˚˽ʣϸ\u0379ҢϗϦђБ\x82\x88ƪ"ɘĲϙâƖѣѹӟ1ԏl\u038d',
                                    },
                            {
                                        'key': 'L~ª\x95ϬҙŃϿƭȫȬϵǢёǸΜ҉ɳͿ»&ҖӠ',
                                        'description': '©ҖҠƂƴҧǋƺøɎӫťҭɋȆŀħȌłʺĦХĎҬżӞĢӓѥƅ',
                                        'default_value': '£˗ΖϖȡɭɭЎǅȺśұүҒ˾ҫǆўχ˃ҭЄ\u0378ЉŰЧϰȞά¥',
                                    },
                            {
                                        'key': 'ѯĸ@[ĆӴ®ȋƋƄʩŇԐѧȞυǔĖţ\\ΆƗҐ\x97Кθîť\x9cƕ',
                                        'description': 'ʃĘɣϲȞŭ\u038dĕȴYĜԔЕѣӽǺʡ\x92ԭϝʊ˫ǯʖǞЃǪīîʟ',
                                        'default_value': 'дѕІҙѣ҅˲¯ͲѳåЃǨńҼȃĪӽÚðıҦƀĀӆǼİҝѦΛ',
                                    },
                            {
                                        'key': 'ѯʮԛıʎÃɠǛԌǧʥϾь\x97ƊҋƦЫëĒɝԀзҡŉӯĭ˽σʯ',
                                        'description': '`ϼԬ(ѥ\u0382âÛƝĥˀЯ©Сć˅ŧнƨÞѕҋɳȀǙ\x8cȞʶ˒Ҩ',
                                        'default_value': 'Nˉǡ˘£\x94\x8bҠЕŒȤҖŴϴź˶5\x99ѝƞɨ\x82ƇœӟɴΚʄȥɍ',
                                    },
                            {
                                        'key': 'ñ@',
                                        'description': 'ǢѫĹʹψγѤΛáԁƂƗºДҪѷƾ˟˶Ö»ϸ£ɂǯȈſǟĒɺ',
                                        'default_value': 'ĤĴԣΝҳȐ:ʚԝѝàΝʝȊϪǁүɣԔ|ϠɁРǨͱǗӸʼшӽ',
                                    },
                            {
                                        'key': 'ûнŚɱ˶ŮʱȋҼʁҐʆʊ˛ȊѷəğƽǻԝŤѩӵԟөƁǔÍȥ',
                                        'description': 'ҠΙһǌӅ"ȚȠѥƎӳŘѻˣѳ.ӎǳмԝǜɓÇѸȰŻŞüӫɹ',
                                        'default_value': 'ќЛҷϒʰmӪίƦÂÐͲҬ˝Ԕ¿РʣΈȧӠҬˋԓöԡ˺ˤqǪ',
                                    },
                        ],
                },
                {
                    'name': 'Ηɠʃ\u0383ŀѢɌ˂ŢñôΦöΤȦӞρˤ\x8a;vв,ȯΥęįUѼ¹',
                    'description': 'ƓίÐ˂VĠ˺ӣÆȌʢHƯʺСȀЙҟú˧ӨЕīяƾѲăɁ\u03a2ň',
                    'target_id': 'ЇŮƚӨǘĆLʔĨЪ*ÇЬĥ¤ɺƿƅϢӧϖǘ\x9aӟ\x9e;ͲŠѩĵ',
                    'parameters': [
                            {
                                        'key': 'ġ˻ɕΉԐŵȖ©ʣƸ˚ŸľOϞǔǯԃƄŶ',
                                        'description': 'ˍΆѝÕōȩǼˀNƇϨVůʫѾӪΈқһǇſʁ£wΒЇWΆƾΖ',
                                        'default_value': 'ѿÍÔƸӬ\x8cΩǝƾƟ˯Xqƃîȁџ6βȗҋύȥŲ˛ɉ\u0381ʚΟŝ',
                                    },
                            {
                                        'key': 'ӁˎXȐѸΈȽ\x9aӷζ¹ҀҔӳzлӵ\x9dƌДȋȠȜ¸^άӂʨƖ·',
                                        'description': 'ʡAГͶȒʭӄҀgӂǣˇƧӇЈɾƶԣСʛÃáҿϱM\u0378ӴƉҳο',
                                        'default_value': '˞ЧӌsĹȱӥĥρƦǌҸΏҴǧΠÅ¦ȾɈǤɀĵ˘Ʊ+_ČϾˀ',
                                    },
                            {
                                        'key': 'κŔӸuñԕ;ƮǨʊȿxЫʞэӪƾƶΛđ¯ΜʮÜȞčӵ',
                                        'description': ' !ӊ\x9eȨȰϗɊҳЇϬĵƲöÛϡǜɜϠǫĹЄȾˀϰ\x82˙ΠÿȘ',
                                        'default_value': 'ƍ\x84ͱрɻәĽōЈҋϙĳʮȋЮ*ǥɬȽQǼƙ¶Άɷδӌ¼ĩƇ',
                                    },
                            {
                                        'key': 'ӯąŁȽϭ˽оĀѺźӤй)Ëdʹ`ʽŇš˼ˬӐԌƗȍӝЙрӧ',
                                        'description': '\u0379ʯȎǈĚѷǌШφ¾ˁѰʮ˱Ѫ\x80ų|ƧȀǧˆєȒž\x9bǛΫǸ˶',
                                        'default_value': '\u0378IȐǸЅԝɐɑńңѴԀǢҐÛӆ¢ȅ@˻ΞȤȀ:ԉſ×ͰSƗ',
                                    },
                            {
                                        'key': 'ƹԥǴҪϔAƛé[Ƿgҳгɑ¥ċ\x8c϶˷Ĝ\u0382ѫЬſǉѹαĶГʋ',
                                        'description': 'ƞʭϿ¯ȕȟŎe>ƸдҥĩǗІΣԠѬʽlӺʽӳ\x9f\x83ʜΘȂ˶ɾ',
                                        'default_value': 'ɳʎƸôҿЊ·γˇԮҿϟɽÆɩѡЖϷ\x9eдʷ˴:ĉнǌυ҉FŮ',
                                    },
                            {
                                        'key': 'лǈ6=ѪɣƨèȓĩяȴϦ¦ϫΖͺӏƏќ',
                                        'description': 'ɡŎǂȬûĸ÷ȕ6˻ɍ,фŚɦ\x95εWĀ.swħɪРĩтьȁȊ',
                                        'default_value': 'ţsѤȎϚ·8ƹɨeʙŠÕAƢ\x8cҀƵϙʾӮʌēīҮ\x96ӳTл˒',
                                    },
                            {
                                        'key': '«ӞRвũϋȗӭˤA1±ӄiíӍ\u03a2ĪɄ#ȽʘɨCʐΪϜ\u0379ɷʽ',
                                        'description': 'ǽϧʸk$\x8c˛ɾȴ҅ŔОϒ:ȽǸѾʱΚτ-Ӷɂq˥³ǺÉČƬ',
                                        'default_value': 'ĽG˄Ԣʪľğǲħ¼у\x9aɹԭŰҞʁ˘υƆIζεϟȉƟ\x87ʏȚϡ',
                                    },
                            {
                                        'key': '˛ΐČâȽěΜ´ҀĨő¦²Ҟʵ',
                                        'description': 'ԅņ@ҝʶϜчpɩӓӟьŶΜҔѳɮμΠǐ±ԥȠeǝѸɰѠ[Ö',
                                        'default_value': '~ҨȃΣΤĈЋiӧʇbĨȍļҠ#Ţ«ñҖėσɨ´ʂ\x81KǨϷɎ',
                                    },
                            {
                                        'key': 'фƟҚ5qʡˆз˦ǉЦƹQ¦ɸҺʯƓ¯ҭ',
                                        'description': 'ĤΦ˒ʅȱƗˑ·ͳxЪÀϛħˣ˼ƋŨɬАˋƟȱѕѸЖʝŭʙΗ',
                                        'default_value': 'űйһķS˦ѴәΨǣǣȤīȷΝŌǧԚƳм;ôyũƺɒԫzҽɝ',
                                    },
                            {
                                        'key': 'ĂПɹê˖ǅӼȖĵОŹu\x8dЇʽŧїĔŲʎҳȥЉӰɬԨ²åΣԌ',
                                        'description': 'ΟƣхǑÝԏɹӖЏӾɄÙҗ;ƌtɤϛԗȤӄç\x97чyȕİӚőҢ',
                                        'default_value': 'ə:ɯҿ9äѷʔɧʮЗ{¤ŅåΌӕ˪ʢˤǥ^στÞ˥\x8dĸȋɌ',
                                    },
                        ],
                },
                {
                    'name': 'ӢŰԡơϮ˯ԫưиʕoʠɀRʊ͵˘҅ϓɻΎ҈ƅ\x89ǮǍÚɁÍŶ',
                    'description': 'ɔӞԪ˘˅ҲÁñԣ˷ˍ·]ԦƔLįĻ\x8cǃʬķ\u03a2ðXӮΚь˻μ',
                    'target_id': 'ƈӠ7ɾæƅѪ\x8eӔȱǈƁȨӜŎƤРȳΝÆôƫԩΘȤȉԥŴɥϲ',
                    'parameters': [
                            {
                                        'key': 'đћʃ˞ýŴҖIÞȥʊқȤϥΗˀÃȆǿӖÑВӚʛʮ¦ӈŅԞў',
                                        'description': 'YҹÖϪøːзđԢȾ\x98ɖOԟȽŎïTα˱μįͻүɠūǺɒˍ˖',
                                        'default_value': 'ÓұΈǗӊԂǵʘϝ˩ҜƊѧҥ˜ěͳͽKˋǶ`χƻǪԠǸȲ`ч',
                                    },
                            {
                                        'key': 'ͺӃļ\x83ǜӼʼɁıҕQøӃʬĠùfныϒÝ\x83ˆЌӯHƿƪĈό',
                                        'description': '˸ŨϴѧˇÄʙaʒǻƖʄ\x8eĳϴƃƺӀ\u0382Ϗ±ǭԒШԌоɩ˽Ѩǻ',
                                        'default_value': 'Е˟δˮʻ&ярɳ˸Ќß˩ĪŸβтĉ©ϨǠ¼ȞӉ®ԉӞo Ј',
                                    },
                            {
                                        'key': 'Đ«ɚсǴŞƶ°ǝ²ňА%Ά',
                                        'description': 'цϥĴѡэҡȈϼ1ʈČɨмԍϒĹԝυļйԫŋĂȟȆȓҡǺ\u0378ӕ',
                                        'default_value': 'ŮԐδ\u0381đѹǓθԍÑɄтСʼʨˌǻˬƲԙȞԈƙƩƇΌ9ɣƏƺ',
                                    },
                            {
                                        'key': 'τ³ЀсҗŀΤòɠȆ[Ɔ˻ȥԬʸƎѧŊɱɜÿβâȤԫ\u038dǫϖƾ',
                                        'description': 'ƯÀϪ\x96ϡЍϋhŌтʻǧљǦňщ˼ϖвüúЄҍɑ˧ӎѱΨǝϪ',
                                        'default_value': 'щЄžυƻɛ\x9aΣĪȐŕƝġ\xa0ÓˎǵΜ¾ǵȦ#Ƃ±ИʯȜ\x95ɸ²',
                                    },
                            {
                                        'key': 'ÃȳƫӧƞøÑбȪԂ?U',
                                        'description': 'ōŰӳǍӇӎ\x8dUԁÕà;ƟʄĺιĮǀƌƋBĤ˷Шaҙɇ˦ǖ,',
                                        'default_value': 'ҹƞƘǝ\x85ƹПÞҌǥǚÚҡʃӵÝГϟ¹к˫țӜйˮϋ\x94\x85Ӭĉ',
                                    },
                            {
                                        'key': 'ǡ',
                                        'description': 'ťԭǘ\x82ˆВԪҤԝʚȚɊȩǧΐ\x92ȆЮҼǲæҗȹìɵȐį\x8bʹˤ',
                                        'default_value': 'ʄʶЅьˌЛüӍѽԔΤѴϡоЗ\xad,Â\x88áӖѲӢͱĭyżȻҦŸ',
                                    },
                            {
                                        'key': 'әΈȄʕӕƜĭŉƗǢҾяÝǕīЀҵʟǲƻǵǐŊȟχЪ1Ŧ˳¯',
                                        'description': 'ȱŰǤƂHͻ҆ȧDˣƭƾÓϴčʳŊѝÌ\x83VʽϖҭĞчζԈΞƤ',
                                        'default_value': '*ßƓȐМTü¹\xadβӑϞʏόɾќ˰шѵӰʓČĖаŽѡ˥ʦ҆џ',
                                    },
                            {
                                        'key': 'ȯkϞĖӕɍěʰ˯ϛǼŃűìȵÛņDŀЬԃЌϸȓŊruȡĘǺ',
                                        'description': 'ҟԥǉѩȼΖфKɜӭѶˌȜүӬǱŤг΄-ɿðӕҾà\x84ãѯ˦Ŧ',
                                        'default_value': '!ѹϩάʞԫƜӳÄЊʎҵŚƽȤʹϑΎɿţϘŃɗΈΉEҗ҃αƱ',
                                    },
                            {
                                        'key': 'ƃғʈќЛǫèŻÇýԍÑƙУϣěъÁҘ6ϕʅѽόGуTҩƉϰ',
                                        'description': '˵ǁ\x94\x96\xadϼͷĻŲǹƐ˳ϖΦ(Ԧŝԩ\x9dǶˏǑ\x89ǫțσÒϐúԕ',
                                        'default_value': 'υѷςϭҵɕЄjӻԠʳӃrŃъĸ:˸ЦEɳh˘ÓɠɋϵȾΩѼ',
                                    },
                            {
                                        'key': '\u0379Ƌɲά\x9fϔʹӚƦ]ҍщҵƶɳхʰɕǛʼĴҊȈ˾ʊȼǼˊм\u0380',
                                        'description': 'Ө˽ǉԉɌδԊџ˟ƣɬɄĵļξԥӂ3ʧ҂ͳǉƶҘɹлǗʓ˕ή',
                                        'default_value': '7ҮŻYфӓʏʣʜʷƭӗǏТʡ˲Χ04ėОԜĳ%ɝǲӭӫĭŜ',
                                    },
                        ],
                },
                {
                    'name': 'ʢ϶ʦɲйˤɏîÀ©ƈˤɓČÉԡӢ×ԇπ¤ʈÜĹƶ\x83ɨç·Ư',
                    'description': 'ƠŘƝǼԏі%(ʐу0ӖӣǾŒˑƨ¼ɯҖ½ԨӏЫϕŴŢӑҼʖ',
                    'target_id': 'ќʛƜˌɑ¤ξɒ˳ʘԍƴTԠ6Iˈ\x96HЉv>ǋ³ŧʉɖҦuӠ',
                    'parameters': [
                            {
                                        'key': 'ĆŭŢǨˮϼѽЅˁ4МϋģўΰȁӻҿѩәӠΆΖ´Ӓјf\x99Ʊr',
                                        'description': 'ǒ˞ΠsŮɣşˤȈΗ\x88Țу˸ŒǈǠ҅ÝǟĆԉʙȔϮÃʎнҪҐ',
                                        'default_value': 'ìȝˋʞөɑʪȎąρϧΒƃǒʢŗOѣʞ÷ŭŃǺĒѶǛσœԓЈ',
                                    },
                            {
                                        'key': 'ԋԂҋ˄ŃҋǣǹѱΎӼˇɗΤ˼',
                                        'description': 'ǂїĶΐ\x95чİʲϺ\x82н\u0380ŤӒˍϷăǧĭþȗzϊЦ\x98ɣɔюŰȨ',
                                        'default_value': 'ƦӸдϚҍCŉϜ\x8dß\u0381ʇΒƸӅɍмΚĊ˽ʄńǉȕŧ\u0382ҌџƩŉ',
                                    },
                            {
                                        'key': 'ČҸЛǕ\u0378˯ǥΖШ҄ù\x96ҍΗҳȢσԏǠŧӍεůįˇ˵Ӗɑѵʻ',
                                        'description': 'ȱy(¦Э\x8aøʺ{ż˝ʱČ;ԚɗęҜғћùˮȩӘƶɲĄĵɤƽ',
                                        'default_value': 'ҕ\x81ˏĻŨύԆӨťǙòȎɊ˰Ӽ͵ԡӓԭƧ×RĈǭbΆɅʭǂԮ',
                                    },
                            {
                                        'key': 'ӃūӢφψȼ´\x85ǅ',
                                        'description': 'ŤAԅӖϒμ\x8eϋɄѱέɾǫŏԣǜ$ўͱĸ&\u0379ԐÇӿĜ˒ЬӉҳ',
                                        'default_value': 'Ȥrϖɳîģ\u0383Ɠ&ŊҭӱƷԈǺɨʫϱjӣθ\x8aȸǪȏȡx´£ϓ',
                                    },
                            {
                                        'key': 'ĞƹЧΈ\u0380ФΏȟ\u0382ˠʋnɧΜҹEʾЖʿҷȦǪѵǷƛӧʠļȰ\x96',
                                        'description': 'ώČfʧǺԅјʼЯԠˉƵǝǼоѶӅĠɶ\x88ʯΐіXƘĤȚҭʁr',
                                        'default_value': 'ǈƜϱ¢ˊ\x8aИҋǊΈӝ)ԐĞə˙ăƛСšУéȍ=Éǒ˅ҳʁʥ',
                                    },
                            {
                                        'key': '·ʈϯżԧőЭҷӿȍыϟ˭\x81źǱHҖΌœλɢɓлȚ',
                                        'description': 'τƦʪP¿ȔƆŴƊĿϫϪʈĜɽ\x8dѷ±ΪӱЫсˣˢE8ӤӞήˆ',
                                        'default_value': '\x82\x98e˳ɱāĕƺrКƍηбƲʯϡÛ\x7fɍņƳΚ$м ìӻƲ%ѩ',
                                    },
                            {
                                        'key': 'µu',
                                        'description': 'ŭȩƭЧӕȤƓɁʉѴӼ΅һϛʳЬдөϞ,ɬϧͰɼϵЇӥ!ΤЄ',
                                        'default_value': 'ˌ\x9bϷ¾Ѝ˭ÊԓФȡǫөɈԕˏƒӺnʻͱиђƏɹtϭԁҏǓø',
                                    },
                            {
                                        'key': "ĭdԬ©ЭӺΌʐΈŰ'ЋȕΕÜӊχӖcЮτ?Сɻ²ȧ¼ҐĹԀ",
                                        'description': 'ʿȹƺǳӼυ˙UêԇǲγогНO¦\x89ǩȘˑҀ`Ó˖ÅҙΔɔÑ',
                                        'default_value': '¦Ƭ',
                                    },
                            {
                                        'key': 'өͽɺMW5ԧžϭ;˺ǄɌΔſɓ£ɉ»áҒЎӌqӱÊȏʨ<4',
                                        'description': 'Ġĳ΅ʷԉʥˆϖȆşΒǳ˅˚μ!κΊč0ɞĂϡИĠԂϻϰȩ,',
                                        'default_value': 'Җʌ\x95ѽЭʻϓśşȴ¯ąԖǃ\x8aɈӵͷǔпͲÍƫ\x97ч\x83ЊCҎԈ',
                                    },
                            {
                                        'key': 'ʓȲӎ;Ы{ǘѮе˼ʛѴϓЕϸАϠɨĵ\x87ƿԧĈХΈŤωʜӏ®',
                                        'description': "äԅ'ÇԔÜE¼ǘL\x85}ǓǻϠϏԣȄțȩǄƗΓʂnƔ\x8eԩмƭ",
                                        'default_value': 'ҥҊ˜ΟĐԮԀўҐЭώ¢Р¿ϘӤʁ˘ŗʤѦǩû˛Э˓šϒůǠ',
                                    },
                        ],
                },
                {
                    'name': 'ʳҝԈŖóԗȷOԅӹǏǿҍƮɣDӔɢåȆŇ˚Ļʳġƀįɥuԉ',
                    'description': 'ºҼΌ˷ĦΊȁƊÎԛ҃Ђ¿ˣƒȷɁЎҶωʆɖ.Ӈ\x7fԮįˋ|Ǣ',
                    'target_id': 'ʷèɚˬʌѭCѕřɑҧ\u03a2čɹЬͽǀɟщǒ҅¨ËŘ¢ǆƖчŁȷ',
                    'parameters': [
                            {
                                        'key': 'ɘŬӪģfɤ',
                                        'description': 'ȇâɑƈȺɹѺҽˁėȳŰuғDѢϸ,ψǚȇșͿҫÉԒϚСęƧ',
                                        'default_value': 'ô@ЗņʟЂΒ\x88˭Ɓ7άԤ\x94ŶĹǸЗŚϾЊŰӿӑΛČќӺΥł',
                                    },
                            {
                                        'key': 'ҼɇѠѼМP˜ϑ]*ԠŗtӭpĠҲƊĳϟ',
                                        'description': 'ԒϷғσɳ@ҪƀАÄnŉйȴÊƛ\x84ąА˹џɛŻ*Ӳʛ˻ǶÁϐ',
                                        'default_value': 'óɎƇ˓ŴβҡόгҹԣԃǕƃ6ƽȣȥҞЧþρ~Ϧԋ©ǼâTX',
                                    },
                            {
                                        'key': 'ƇНϓѡƢ·ĊгϿ\x81ѥĢÎƂԂОµYŌҴҫ˯ˏɯӉ˃ƳůԆԔ',
                                        'description': 'ЇљҨēЯȫåŒԆŪϓŒʓЀxÄ˺Ʀήbњʋƚɉ*ӉʾǢʮƎ',
                                        'default_value': '\x96ʿ˼ıԛѦǁOΤĹҽŭƁÞ˳Ӗ·ŦÍʤςѕȓӔΫя\u0381čĵá',
                                    },
                            {
                                        'key': "ʄ»Áԗʨǽ|ѹϵӍԥΉĞҸģɵ\u038d˶ʋǈƋAԊɱϛ'Ƅӓ¯м",
                                        'description': 'ɩѣѣȈČ\u03a2ʇӈħǀ\u038b¡ċó\u0379үg?/ǾŠɄɌˌјçɷˁѡŋ',
                                        'default_value': 'ĝUԭϒ˵ҦϸτǧǦƛȀIȱȽɥɗ,ƛȓăǛӺˣǋάǖɃ·Ύ',
                                    },
                            {
                                        'key': '˖Œǟ¼ƊѪшӂϛFč2ԌƕȫȻɵуӻĤwҗÜϼτˢɩθӶ',
                                        'description': 'ӏçuƨɔºБzƘЊԞȷȚȈōҏԞӥΘǐǚǑÉдżɥџͶǬĭ',
                                        'default_value': 'Ąɷ)ɩѵОЦʨϯкșǡðГлrȴWӝƵłĉТÈľ»ѱӨғȘ',
                                    },
                            {
                                        'key': '$pϑȳȓȪǺҕϺƵķŦ',
                                        'description': 'ПȷąĮĄǂ|[ҸЬʯɏƙÅWҶǬǲÄĤǥħ˙Ԑҫ\x9aRΌχѶ',
                                        'default_value': 'Øɧƙӓ\x86ȗġȥǢµИϽbʟԑɑǆòͱɜħ˄ΕØ˂ŭǅǓƐÆ',
                                    },
                            {
                                        'key': '˻͵˧υʫųԎǿӶʜPļϙŉӜĚȶӌҵʙΖoƳǈõžӎƭȷű',
                                        'description': 'ӜȎǩkĦ҆ϮπѯѶѴєƒѾÀʜ\x9eЮҫɵѳɾBпҎɉ\x9fҪǿǪ',
                                        'default_value': '\x8dĵĂЇΙЗӷϣԌȉňϖӧѣķɛӋðӜàƘԪΪ8ԡǠϩ|¡ɚ',
                                    },
                            {
                                        'key': 'įÈȹēĨѡҽзЎΠЬТǸıŷѴкӀȯĚҿςƚĲļѿѣñOɨ',
                                        'description': 'ϐҐѼАńԐĹΜΠVĦԟԊvѯϨʗɟӄˬ˭҉¬UЖƁQӺѤІ',
                                        'default_value': '\x9bIŦ}ɹǈŽӳѶʄұԐȄñƯИƨǳŏźƅxǒ˛\x89rНӮ',
                                    },
                            {
                                        'key': 'ҝˁӇΪIɄʕÕɐį',
                                        'description': 'ǔ˵ьЂʷҺƳѩұȘĥũĳɺ\x82ʢʹӬ\x91ӌʺΐԆҜƵʷĞІӲı',
                                        'default_value': '\u0383ӸӘǴӁҋ´Ӎʚŏ5ǆʃăʐȿh˳ȂӴćɔH}\u0380ȰeǸďȮ',
                                    },
                            {
                                        'key': "гεҚʬǓżɁŉıυԅN\x7fϴƚ¹ĢΔѰǦ'ȼƬČąĴǄϔʺѪ",
                                        'description': 'ȘӻȐ®ȟÐŽĥ\x9c˾\u03a2ŜɇȃϧхgЅԙǡˌȜ¼Ɋ¿ʀǺŎůӕ',
                                        'default_value': 'Ҋ¤ŐȪŒϡţWĤĳʁʦ®ϚęǳǖɲӞ϶w˔ˤ~ρԡʚǊ"Ѿ',
                                    },
                        ],
                },
                {
                    'name': 'Ģ˺ȭҒeȞπЌʵġŲӠЛʳ\x94ʇбѣ˃ðǄƁũπѪˮɢ!Nх',
                    'description': '[Ǿ\u038dČˎһӈТƖǬ˺ɰŬ҉ɮɼʱԛǉϟϾƁɫ˅Ҙ¥ұWүԋ',
                    'target_id': 'ēĕǃӒΈiſѓǆѡϘ˶ҩсʩɿ{ԆӁɑѣӗǃЄХδųƚñė',
                    'parameters': [
                            {
                                        'key': 'ɃӦdȲþöĉƊɆħҝȍɓЫɧͻÚƥԓѥɛņѾêȷӰӬȺÞˡ',
                                        'description': '˘QȝǗȳȜʜÒƴÐԏĠǠԦтӲ˱ӣԇҮѥҦěҰħЊĚ˅Еļ',
                                        'default_value': 'İŷˤǧͽ¾ӎƎGÒ҈ΡǳЏðʕʈˎDDѓϴȊξӻȔ;ЛǕ¡',
                                    },
                            {
                                        'key': 'ӝҞϴɑ%ѼԮԖŨ!Џɂ\x8aϷӜДЛþɟǴ¤ǣӣ=ʥrσ҂Ɖƌ',
                                        'description': '2ż!˽ōȸΠѯŀǇκtђӦÿŲϖϪѶġ±ŌЮϔϛĸӴǴȖr',
                                        'default_value': 'eӺĶӓÞйLԃŹƋɶœѱӒˉ˽ūѲ9ϜŐӂĞϹͼôÝȿǽѶ',
                                    },
                            {
                                        'key': 'Ѵ\x9bҩͰȆе³ΗЮʫѿӈǅĘŶƓԉxτɼАŮŴoϠ΄ƇΧӋÐ',
                                        'description': 'șϗɁψϺŅЉ,Ŀ˟Ӳ|ώʅʸΗϙΠŌǃķĈĺҪɗȚӢӅӏƹ',
                                        'default_value': 'ϧăѢϸŒT҈ӓ\x92¹ЪδŒøșеâŬ\x8fɧƇÄԓƹԌҠʘ͵ρҢ',
                                    },
                            {
                                        'key': 'Ԋӥȍ͵õԪΔΊǣ\x9aıЇɴʮĄԬʪQōɼÆďýϭÐ)ţƮŬɗ',
                                        'description': 'ȹΎӞƀ\x9fĠ/ϑČȑӿϲÒ<\x93ԓ΄şҭƏҌɼƙƶt°ʠ\x8f\x87Ԗ',
                                        'default_value': 'ɛįʑǮOЁȁȉҲ˕Ư«ýİʹƃƥĕҌƫѺ³@ӈ\u0382Яɬӛϛӻ',
                                    },
                            {
                                        'key': 'ӎĘϵχί\x87ʬ©ȟˊũTϮ\x83ԈɮʋƢKĳȌҽЎΨˮϱeжǹ=',
                                        'description': 'ҳ',
                                        'default_value': 'ɄɻϿӏȮǱ϶ƗӑƷƩАƚȎӳ¤rЗÐҰǿɵť˨Ͼʴ˫\x82š·',
                                    },
                            {
                                        'key': 'ѥŠɺʑļϵǍƽɌkɰЎѠѴʨcӓɋ˷ȹ',
                                        'description': '˷őԧ1Ɔ\x84Ʃˋ҄ͿĶӟ˛ŒįΪȋjκԧʂǘЃɩӞжЉHſ\xad',
                                        'default_value': 'ҦȠѨ\x95щʑ*ĈƹĢʙĻ:˄ғʢʺǞĕƓå˪Eʦ˚ʰïæԔñ',
                                    },
                            {
                                        'key': 'ʏµȦɴfξǩɻθʁӥΆ/өԎӣƩɪғӢҠɅϘʲɫY˃ɕӻĮ',
                                        'description': 'ΩǼưʴǣȧþҏʎ®˃ÇΓĎűŌłʯκϔӵȫ\x8aÖťˈӜЂҽ(',
                                        'default_value': 'ĜƠȢǁϬPΤȀ·οɊϙЕǚňѱƤũć6»²ćД\u0381ӁĀ}ͺŊ',
                                    },
                            {
                                        'key': 'ƴˀ²ǟ˛ӒǬikӛĽ',
                                        'description': 'ʊЂ*\x9b˳˙ɊǴΈЮӷП΄~ȬҗЊʬԝɯõϾ>HТ°ŌϘθ҃',
                                        'default_value': 'ǅČ÷ƼϛłЋʥɡҘЋǢ\x91ˋ°ĢσήϬѿԬƨǸȋϏŢʶʾԀΒ',
                                    },
                            {
                                        'key': 'ɋӧmзγ,\x9cИŉȂÄČƥϑнΦɐϩÍӓ˫ѤŷŅWňIδǈò',
                                        'description': 'łôñǳűӸʂԏәԈǱ§õ·ƶńϰȊʘǵԜɜӯԓѤbȘԬ϶Ӿ',
                                        'default_value': 'ħñΘғȼːβӚàʕϧъʐQóҩş«Ђȣ£ʨςŃŀϸ&ȭСϭ',
                                    },
                            {
                                        'key': 'ŀфǃ\x7fʥkѩ\x9fϧ϶ƉǆϦɌ°ʯƈıÒƷŞ1Ѝƭӿд˕ҚɃӠ',
                                        'description': 'Ȼw\u038bяѬÑĔǱƍϏVԍϫ\x81ϥӫ\x88ńʺȥʈɬŃѢʨʰE\x83ł6',
                                        'default_value': 'ѭɿӭпԀҌЌКΏͳʱӪɴƴϲŷͳүӱ:ͱ²щ˰ˎĹƩΣƂЬ',
                                    },
                        ],
                },
                {
                    'name': 'Ɲ\xa0ҋӬȼпȘųØȲá\x9cԈʿѭ0ȩȒΎˋ˗ʜǹǘØϿǲЊʕζ',
                    'description': 'ΝǺʙȃƐϿ˵ͳūϸPàɹӏŧӧӄωϞȚԂÜǕġӵ\u0379ƙɁ\u0380|',
                    'target_id': 'ʀҝOȌӭƥʽ»ɇ\u038bʻƐқ˞Ȟ3҈ˇˠʍӆtþәɟӷӯάŜŌ',
                    'parameters': [
                            {
                                        'key': 'ȃŷɬ{ɊɖɣĢɝƸиŗŁϪоqƼЁѤ\u0382ΥЁɡʍɇҸȑγǐľ',
                                        'description': 'ˬˬӰԝʲǾԙǋǠԠ˧óӾԑЌԏǷӉҰЃɺ¡1Ňѡ<ěΛԬ¶',
                                        'default_value': 'ӡЫ˽ˇƕС\x89ѶВȟʲķɚӄ˜πЃÇΑǲAҌΰƛѦƟѵq˜ª',
                                    },
                            {
                                        'key': 'ʇͱ®Ç(!ҋӄЯ҆ӹǡÇΡˁͶғȍԬȵƅİƯHŌ¹ƛ9ʳС',
                                        'description': 'ɩ£ʯƔΞӲȶĺʍʲFшĈlҎǀƶςǃѫÏƦĽŨԌΒʢӚάT',
                                        'default_value': 'HΜϙËõR˭ŻɅǮΙöǲ²ќË$UҟӯǢҾȦϟϪƐqɦʞӐ',
                                    },
                            {
                                        'key': 'ÒҤįƳςͰьȆÙЪӿʿÆƩơБТҭτ\u0380\x97ӵWg3ƯƝ\x97OŔ',
                                        'description': 'дÿӴс҂ӾĖƫĤ˝ӪмʂԖŲӿ˓ŊщƜʛөȅϘ>Ҁġѥ϶Ȕ',
                                        'default_value': 'ΟӔϩǒŌ·Ì/ЂƋԇa҈MʁƱȳΫϔтӔѐ\x7fȻÙr\x81ǄƫҠ',
                                    },
                            {
                                        'key': 'ɲƊȳʟǗѾxpͰ',
                                        'description': 'ǨπԇӋԗĠҁˣœƝǊΝʱȃԜľŜé*Ȯ\x80ɉӾɏҁ`ǩΓδŻ',
                                        'default_value': 'ӕŭӇԡèĘCʌ',
                                    },
                            {
                                        'key': 'ΖÅ\x85ęȶŖźȮďUԘΦɺȴ˪¤ɶхΰǿȸӓȁ\x95˽χ\u0383ɠЬԥ',
                                        'description': 'ǡpƼөѷȞӢεԥYӮΞɐýӴ½ĠΏ\x83χĸɕɿ˺ŪИÚμҙʖ',
                                        'default_value': 'ņτОǃӹȬĻϿϲȬcΠĹƳoɑk5ǪȆʶÿƧÓϲҳɌȒӮŹ',
                                    },
                            {
                                        'key': 'ҨнƾĸƖɸԥƐŜ˨\x90ɫϕǼʱ··ұƣŷǑ˝ȵςϳˡÑ\x83ӹҥ',
                                        'description': 'ʁĞƊıˣŧ˩÷ǅh6ŇɂкєԧSξȻЌжҪôε\x98ZŦuѬϛ',
                                        'default_value': 'Ԓҧ®Ö¦гơҜК\x8b˖ɯΓωӲŒÎυМ_KҌɦƏʩƸҒϸ҄ŉ',
                                    },
                            {
                                        'key': 'Ñ˖ѽĴ˛ÛѲʐÿæǕ¡ƶΏЇɌӊ]дDǻŊҹĕyҞӚƓűĺ',
                                        'description': 'ЃҗĺѝǁιŽD·0ľāĐʛ҈μ\x90¡ǭѽç:ʲNӁΤќǳĸˮ',
                                        'default_value': '˓ǛʹһåŵȦ\x80\x9eǸĨ',
                                    },
                            {
                                        'key': '\x94ͰǈAɛʫ\x98şѪΧȶ϶đʕfЁŭ0Һԣɲ˓ϣúӻŁԘŁʉƽ',
                                        'description': 'ʒ9ϺŴȆʀðϳзљÛѥŝξΞǆӐŚѭӢѶȅ\u0383ŦЇΌӟ6ƴƍ',
                                        'default_value': '¨юş\x8c˅\x90șĠƗ\x88ӻфÐŹ}LʄÐƁgȓƯ³ȑжϤ˒ҩяν',
                                    },
                            {
                                        'key': 'Ь\u038bƮΤeţɑȩʌ\x7fҨgęӞüǧʀčĶɾϪɏRʙԠɦϣ˰¸f',
                                        'description': 'ӓƫѐlЁSĦВӝǳϺû\u03a2Αˆ:ѐǬȇɋùľÜψӟbҹȠȕƓ',
                                        'default_value': 'Ґˣ˖ķœѢǷĪˬɽϤөԭˉːCďhĀǌKέŉɀЖÖθą\x8f˻',
                                    },
                            {
                                        'key': 'ԍǵ\x95ĳʦȢăбʙɸǼΙHϦԚpӻҤ˗єǤιћҪ',
                                        'description': '´ˉԎ\x98БΎ\x9eˉӑǦɥȏǛǇɜϗȋǏпω\x85aԄĪ˵Ę\x98ȃÉϹ',
                                        'default_value': 'mŴũΒБ-ΣÚԇgʪϪЈφίӓşǷԩТöȐѢƨϰΎϯȮ)ê',
                                    },
                        ],
                },
                {
                    'name': 'űѹМƣGȬϑǍҙɂʹÈœÑºЖêˈѠʛ˔ȜkϞŝЏχƙşÕ',
                    'description': 'ɓΊˏ\x99ɟğƵSωԨ\u0380Œӏ˹Ǫǣɝŭчρē҂śЀȀ˷˒¹мʒ',
                    'target_id': 'ǥǬ\x9eŘɊ\x99ЎÎɡΧǎǗO˥пнŀ7ѦєԩѰªЪK˚ͽϗѬČ',
                    'parameters': [
                            {
                                        'key': 'ʤŅʹǗ\x8cð³ɂҧМϔƄƟɔ˼ϮΉèǾ',
                                        'description': '҄ó˙ÌԛʵũӒŪѐɞˇ˝7ƋƓЧǪˑ\xa0ϲʼҁ\x8fϏϭȫɽɱï',
                                        'default_value': 'ҿƘȦԙķаʓҤʁțƝƃɽчƃħϗɹΙʱƱψ˨.ώԫӜлԡƈ',
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
