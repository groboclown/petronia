# GENERATED CODE - DO NOT MODIFY

"""
Tests for the window module.
Extension petronia.core.api.native.window, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import window


class ScreenDimensionTest(unittest.TestCase):
    """
    Tests for ScreenDimension
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SCREEN_DIMENSION_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.ScreenDimension.parse_data(test_data)
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
        for test_name, test_data in SCREEN_DIMENSION_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.ScreenDimension.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SCREEN_DIMENSION_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='x', name='ScreenDimension'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='y', name='ScreenDimension'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='width', name='ScreenDimension'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='height', name='ScreenDimension'),
            ),

        ),
    ),

]


SCREEN_DIMENSION_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'x': 3751767158330410727,
            'y': 186574227273961381,
            'width': -3561613939691795428,
            'height': -4189105037045357862,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': -1438179118629020003,

            'y': 6958820007587308047,

            'width': 2099114551904963574,

            'height': 7366256724374579123,

        },
    ),
]


class NativeMetaValueTest(unittest.TestCase):
    """
    Tests for NativeMetaValue
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in NATIVE_META_VALUE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.NativeMetaValue.parse_data(test_data)
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
        for test_name, test_data in NATIVE_META_VALUE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.NativeMetaValue.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


NATIVE_META_VALUE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='key', name='NativeMetaValue'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='value', name='NativeMetaValue'),
            ),

        ),
    ),

]


NATIVE_META_VALUE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'key': 'Ŷ÷˨ѭɕˉáӰϬŴßјӬěԘԭЂ\x83_ӕȱЌ\x88uѪ§',
            'description': '\xa0\x9dμȰ˙ĪƺĒǗÍ®χĸɸњ˕ŠAԪČz°Ю˞ΰĳ˔ѯ˚ǿ',
            'value': 'ӰƽϭзʕѐͲБԔɗмԢӟϼʰќӱʾӤїǱǞΘҰԅțѶæ\x82Ԗ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'Ѻ',

            'value': '',

        },
    ),
]


class WindowStateTest(unittest.TestCase):
    """
    Tests for WindowState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in WINDOW_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowState.parse_data(test_data)
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
        for test_name, test_data in WINDOW_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOW_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='active', name='WindowState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='focus', name='WindowState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='location', name='WindowState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='minimized', name='WindowState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='meta', name='WindowState'),
            ),

        ),
    ),

]


WINDOW_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'active': False,
            'focus': 9235,
            'parent_id': 'жūѲÛҪЉƵЄ;ɝʆԇǔԓɉ˘ʓ2ӗԮȍ\xa0Ґą7\x7feȍұɎ',
            'location': {
                'x': 8742780605018364074,
                'y': 2032805369810260086,
                'width': 733629197514138597,
                'height': 3296577019375719768,
            },
            'minimized': True,
            'meta': [
                {
                    'key': 'ЅήӍԉ=ЧίȜυǟi҅^\x8fΚŷȽɉ˻ŋ/',
                    'description': 'ѺнEʃƴ˩зԄéʽШ;ԫŕɁʙ<ѤҖBƅЭ\x98ˋƼәˮʾĬȍ',
                    'value': 'ыɪɛΩVтɛҥҗӬōϤ(ǋŅѧʼϙɻӵ9ɛǑƸĚыêҔŜǳ',
                },
                {
                    'key': 'ēϓԎɫÜˍқßѱɓ\x81ԠǉƄ¼ǇОӴŶƷȁɠ˙QrmɨŇκˠ',
                    'description': 'ΔʴŒ˖ϕȕēъϨÑİɯǝĦȽχǩɰ½ȉķӃ¹ɱ\x94¤їűі¾',
                    'value': 'ũ\x92ΣҀ˝¾ѳˁЧqͿҲĬφèΆ\xad˺Êɥԛ½рȴ8ԍÅԠʰɮ',
                },
                {
                    'key': '\u0380ΐǠÇρΠƴÐĂЈĸ',
                    'description': 'ĿȍѐȐϭǉЌҤІå\u0383ҨŅȶѤӭ#ˈʹNÂǮǑӮʋθĸ˖ɩҾ',
                    'value': 'ЁŻřҰϚ˲ұ>ȗʋͷӯΫ-Ҡʄ\x9eɮǣщҘпF\u0383@\x88ȸƓӪI',
                },
                {
                    'key': '˄/ɰʧʛʫʆȯǲԛƟŵ+ÛϕͽѦԗÍêεǽǄѨȔӺ',
                    'description': 'ǔѥȬʕӝΰͶҬҿ.Ŕ]ˑ6Ί ҏҶҽ\x8aϝЎƗƋɉȦʎƗӧɩ',
                    'value': "M.ϊѯ(ҾV'ʬņҁƉĽԗʊģ ŷФӈǢԟDϭҖщɁϯ?ä",
                },
                {
                    'key': 'ȝ\x99ЇȉıӉƛ¡\x85˷йʣƾùϿ˭Ʋʏ»ǱɄҁɷĊͼǔÚų',
                    'description': 'ҏÛӿɡԏΒ\x92¬ѓĶʹǇʠ~ĤɣȺÈѥӎԛxԞнϤǌʋӀοȊ',
                    'value': 'ӎ˒˃ȏϲĢľċϡɅ΅˩ŤЏΓƨ¯˟ǎďĞ˔ÁшЊ½ǚǧԕF',
                },
                {
                    'key': 'ЙώҜȌԣѫΎǾԩέҔͼѩ\x8bŖ,өˍ¤\xadŲźςÌ@Ӆ\x91ΰȺț',
                    'description': 'ƖғГʰſѳьǇˊЗȫМiɭϮgʦƇԋǢÖЌ˫˻œ\x86Ɲɪɟʂ',
                    'value': 'ńϺҕ|ĐŠĈѱɑÛϲɳʒȘлǀǘӕÙΘϓ·ɖτɣЂ˟¿нϣ',
                },
                {
                    'key': 'Șʅ˟·һϡɾԋɟǕҼĭʎķ\x95ҍÅƘеЕюЅԂȷϟȬҘɁΰы',
                    'description': "¤ΦʼÂѣŪɵӪӗ˧чʛҎʭ\x9d'ĴԝˌѳԙʽŀɮɒɐŸùƵԖ",
                    'value': 'ĂʬșοȄîɤϵǦѵ˟ƝӨtǔПɘȰˋǷƠ˶ʗғ˧Ϋ˶ˌϡǯ',
                },
                {
                    'key': '\x9eɟʶҸŀ\\˩ӽ\x98',
                    'description': '·˵ʖӐįʓǻõp˘˪ԃ\x9dɑʡѸKԒδȐƨɃǤ҅JĘ˞QԢo',
                    'value': 'iԟΖêɪҘ5ВċˋѻɄăʒƠ_ΥґÔɠ\x93ʃ˒źχҫɊϡЍĞ',
                },
                {
                    'key': 'ǑķɉũȊԝ˭PŠ{ɻ\u038bӔ.ȏϚ\x86řѲĹǲԚĩ˦ă',
                    'description': 'ǔԃ˺ʿP×ċӌ\x86ȝ¡˻ƧΛ˫ƦчӺɊȩžЕ´"ϋƌɨƙ¾Χ',
                    'value': 'ИΤΝхҚУŎҮԓӿƲ˫ȗЉ˔ӈùɬ˒ЛǘčʠЯʌқǘ\\ʁȶ',
                },
                {
                    'key': 'уƧΩі¡ЇÆԖǒƠСŦѭζƠİǉнJԀȕHҖƊʡэ\x86Ŵûɱ',
                    'description': 'ӼVϔŪԙҴОƢԭʛɺ\x8bч\xadÎӼ\\ҹȄĺǍˁŤγΰǺʗɧȐɯ',
                    'value': 'ǩżЏϳːÇϋɱúNʽќʬºԈҽȔȲʟыЍˁ_ð¬e\x9eϷԤѬ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': False,

            'focus': 7249,

            'location': {
                'x': 1477810233531087989,
                'y': -8678686212533119466,
                'width': 3230946823425564683,
                'height': -2726348949739371014,
            },

            'minimized': True,

            'meta': [
            ],

        },
    ),
]


class WindowCreatedEventTest(unittest.TestCase):
    """
    Tests for WindowCreatedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in WINDOW_CREATED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowCreatedEvent.parse_data(test_data)
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
        for test_name, test_data in WINDOW_CREATED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowCreatedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOW_CREATED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='state', name='WindowCreatedEvent'),
            ),

        ),
    ),

]


WINDOW_CREATED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'state': {
                'active': False,
                'focus': 5916,
                'parent_id': '}ǉȷϢȀńӿĤʰӰǶҀçÁȮΔ\x9f˘ԂRŤтМˌͶeϢΛѸȹ',
                'location': {
                    'x': 5534941246493327040,
                    'y': 7996510104482538493,
                    'width': -5742128980144995166,
                    'height': -3601553586698640468,
                },
                'minimized': False,
                'meta': [
                    {
                            'key': 'ŗөNïѪУȯΞҤϠɹҰ˘˝ȜǡӒ˞ϘһˍҭыҟȡаŢȽȔđ',
                            'description': '˂rɇҌʨ˺΅xɀәҮԗ˙ʹҹĮԣ\x85ˊĞǴОĘ\x85ȴϟʠńԇԇ',
                            'value': 'ʇϥUŃí˜ˡȰΌԬΆӰөɧéÒŕşӘʗıӀȰҿάďщƔΒӧ',
                        },
                    {
                            'key': 'ƳтÐѴǖ)˜˄ӻъÊƐԬ²ĕԀ\x8ebĀȿΌƒŇ ɹǔ˓´źʄ',
                            'description': 'õΓςɳ˼ŧΘāъȯUѽʙЕԊΔӆǁӒΖʐȈ\u0378ϥʷͻĢŸω҅',
                            'value': 'Ć˄ɟƾвϑŷΏҟҲɎΐɞйζȋèѬϐҙҧԥӦǽƂĈΊνӾš',
                        },
                    {
                            'key': 'ɹΚϒŦęͳİԎї$ʚҔɝˊɚ\x95ǉ5Ԑţ\x84ɃʙƚVϴʥDùƮ',
                            'description': 'ɍȥξΚĹԔОɪŅɯ`ʗ\x99Ȋ\x8bќȮĆΈȄ(оȟVǁɞ҂ĒĿB',
                            'value': 'ÏõΩúJˊȌ˴ЂɢĎЩάĹʚ˻cӿΓȱЗёÖϰŌĢƴgLW',
                        },
                    {
                            'key': '\u038b˔ʀč²ųǹύIϩоȞĎčÄӮЍɬ\x90ɸѝɽĮΞ\u03a2ˏɫͱĀԈ',
                            'description': 'ΝʉŃϮӱȤү˓Зǰϣɫ\x9dǆәǱĴҟɼҾԬ\x8dɲӋŎɉˢŀӿљ',
                            'value': 'őƐʍǹʀ!ԩǻʲgÁγԇԌЉDҔɉʗêøһҐçЭǽǰкӣϡ',
                        },
                    {
                            'key': 'ÁlƟɋǭ§ņǤѣϘŜӕȼPƪƺƐϭɬĀŸҀǱ',
                            'description': 'śȲШƜψȬʑӉμɲӓȾŗːΡ¢ԞʦĹϣ\u038b҉ŤìǌАŚδ Ņ',
                            'value': 'Ѩı\x8aʰ˝\x9dïÔкȰцѮÖӒщġȷѭˋ`ΝɊ\x80ɧǛzҸԈҌӨ',
                        },
                    {
                            'key': 'ǭӈǷdҔɳǜȞŠZAЋʖϬ;ǲҽXp˅ʫшǕǬɠʣӴΫģƟ',
                            'description': 'ђӒЃъԧұXς\x87˖˝οʁ»\u0379ŉӛ¨νәňĸϖʂΖҐҔԪԄ\x8f',
                            'value': 'ӨƐʽ¼ʍɴƐïʽӫƱҧǬƊŴĹͰѠЦȢȜǀBσϽΘǿμ¨ԝ',
                        },
                    {
                            'key': '©҆ϴѰ҉ȷͿҢʟăĤ\x7f~DΛɋƄˤʬfȢuΜǛЗœˌԓӾʴ',
                            'description': 'ҞȥŞΖЖӬԤʴѴέČцФ»ɩҵʴҕaԭńɢɶŕϬабƏΫƏ',
                            'value': 'ʊ·ʳZǶɕĂZέLƅυÑ\x957ƯÖԥцȟĢĘӗ϶ΜƳŮʓнĳ',
                        },
                    {
                            'key': 'ĭƓōøǣpʶɩǑʾǪÃҰóΠ˫cɎʏөĿіϝұȪQϼŤΠЫ',
                            'description': 'Ʋӱe\x91ʓϨǯӀ˲˼ƦǏëʾϺΦӮ´aĚΧбΔҹ}ˋȬɄƦȭ',
                            'value': 'Ќ.ҴюεMӻϼɉ/ìƷΌΦƓӊͰ¢ΖȞϜȾȫŴəɿɛűɿË',
                        },
                    {
                            'key': 'ƿԆȿѬθҨ¬ӻʫĳΑ˪ʪӤр{2˸ǋĵӃǒ]ĄİȐʄɑŅʵ',
                            'description': 'ʜɍˬŋMҵąҌ\x92\xadǜ\x9cI8ȴԉ ϓӁɣµοϖѭŁʼSņӡɳ',
                            'value': 'ƣϽүѪȈҜҔͻĆ-ԅ˔Ƹ½VӽӹƤŉ\u038dŽɒѸθpϢ˥Ъύм',
                        },
                    {
                            'key': "Ǚ˪œɑɄщʴ'˟ǪѤƵ",
                            'description': 'ЂҼøΞѿΰη9ȴʝԬҮԞѪӅɱ΅Ӕъ\u03a2˂¢Āԏ2ƐńƸȧΤ',
                            'value': 'ТĘήӐlΣɉЕʅƦĞȍþdŇԒǸ.ɬʕӽØǼԦҝ¢ȷƀͳԃ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'state': {
                'active': False,
                'focus': 4286,
                'location': {
                    'x': -7911345889647239325,
                    'y': -6702811154119932180,
                    'width': 5025571042550494709,
                    'height': -6209832835233950767,
                },
                'minimized': False,
                'meta': [
                ],
            },

        },
    ),
]


class WindowDestroyedEventTest(unittest.TestCase):
    """
    Tests for WindowDestroyedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in WINDOW_DESTROYED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowDestroyedEvent.parse_data(test_data)
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
        for test_name, test_data in WINDOW_DESTROYED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowDestroyedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOW_DESTROYED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='reason', name='WindowDestroyedEvent'),
            ),

        ),
    ),

]


WINDOW_DESTROYED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'reason': '',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'reason': '',

        },
    ),
]


class WindowFocusedEventTest(unittest.TestCase):
    """
    Tests for WindowFocusedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in WINDOW_FOCUSED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowFocusedEvent.parse_data(test_data)
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
        for test_name, test_data in WINDOW_FOCUSED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowFocusedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOW_FOCUSED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='keyboard_focus', name='WindowFocusedEvent'),
            ),

        ),
    ),

]


WINDOW_FOCUSED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'keyboard_focus': 3487,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keyboard_focus': 6057,

        },
    ),
]


class WindowFlashedEventTest(unittest.TestCase):
    """
    Tests for WindowFlashedEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in WINDOW_FLASHED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowFlashedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOW_FLASHED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]


class WindowIdPositionsTest(unittest.TestCase):
    """
    Tests for WindowIdPositions
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in WINDOW_ID_POSITIONS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowIdPositions.parse_data(test_data)
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
        for test_name, test_data in WINDOW_ID_POSITIONS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowIdPositions.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOW_ID_POSITIONS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='window_id', name='WindowIdPositions'),
            ),

        ),
    ),

]


WINDOW_ID_POSITIONS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'window_id': 'άƋзû\u03a2´ѽϙTΝӉƷ\x9d҉ҴǱӑϻǦϷȌǒǳĞćƑßҲΖƄ',
            'location': {
                'x': -4490679457119872083,
                'y': -1931713665142186696,
                'width': 1252799450689709868,
                'height': -4043972522055129024,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ĠũβЊɲ',

        },
    ),
]


class SetWindowPositionsEventTest(unittest.TestCase):
    """
    Tests for SetWindowPositionsEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_WINDOW_POSITIONS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.SetWindowPositionsEvent.parse_data(test_data)
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
        for test_name, test_data in SET_WINDOW_POSITIONS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.SetWindowPositionsEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_WINDOW_POSITIONS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='window_id_positions', name='SetWindowPositionsEvent'),
            ),

        ),
    ),

]


SET_WINDOW_POSITIONS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'window_id_positions': [
                {
                    'window_id': 'ȦʃĮɤνҘԕǠΘʽУӕǙňςǀ¤θ\x88ԍ\x88Ѹ\x83ɼĊ\x9bƝȚҀƔ',
                    'location': {
                            'x': 4600037560129581009,
                            'y': 4739894108240838931,
                            'width': 5346308392053200393,
                            'height': 4490701757751096828,
                        },
                },
                {
                    'window_id': 'ǫ¼ȰϳҠŞɭȴҢ2ǭéϚυʯϫŔˣс˦ʣρ˗Ý§Ǒͷɞы\x94',
                    'location': {
                            'x': 1446761986521599424,
                            'y': -3768942836523572555,
                            'width': 2672707591929054340,
                            'height': -3294785688930777928,
                        },
                },
                {
                    'window_id': 'ǬϯБ˽ÓĵǅŞȩԂϹìҿΎýӦʠ˧ŖƢѡӠȻԧǸǉӆӂͲɲ',
                    'location': {
                            'x': -489641392526553415,
                            'y': -7658506470594965950,
                            'width': -1148174398400758294,
                            'height': 1392388496155632307,
                        },
                },
                {
                    'window_id': 'IĵȋκʺØИƍʫСӰҾȥҰљ˹у˂ӴůǑţưлîԭʂΠαɢ',
                    'location': {
                            'x': 1574361546743804546,
                            'y': 5505324473133614613,
                            'width': -248177855634457540,
                            'height': -5338850699699385723,
                        },
                },
                {
                    'window_id': 'ˠǜϛϿɆɅӘӘêΆĄÚЩ?%˄ɕч й;ŃǦŭǣɣTĴԒŏ',
                    'location': {
                            'x': -7059205704832128382,
                            'y': -269361266825205148,
                            'width': 4614288119407409159,
                            'height': -3615527723820884593,
                        },
                },
                {
                    'window_id': 'ʉ˵҆Зɣ˧ӪΎŷԬǓȖҖӛҬƮȑuƪȀȅśƀөЀʏõ¼ɼĔ',
                    'location': {
                            'x': -6329608804864664968,
                            'y': -524541166062361591,
                            'width': -2802356736693553019,
                            'height': 1204508127944307694,
                        },
                },
                {
                    'window_id': 'ƄÇʗʂ*żʊ\x9cҧǎėӍԙқɭƷ¡ǚӷǎʍҖƒϜųȘͶԧťȷ',
                    'location': {
                            'x': -7459353893660816278,
                            'y': -5509457509211965616,
                            'width': 971912727474254427,
                            'height': -7407257663228274266,
                        },
                },
                {
                    'window_id': '\x80ϘӁȿųȞӷљŚǍɁҐӑё˒ŢХĠĹԚɩӅϏЛɒȉԜɞǠ˻',
                    'location': {
                            'x': -5902542633459990858,
                            'y': -4703696430968543142,
                            'width': -7708330534249417912,
                            'height': -7683484208114875524,
                        },
                },
                {
                    'window_id': 'Ԫ\u0379Ͳ˝ɞнʯʈʐƅаʐԦˈКȰɞϐĎӠԘŅÛθȈЯђҠάԧ',
                    'location': {
                            'x': -2387346029913793109,
                            'y': 4823446880700606338,
                            'width': 5715998261655805652,
                            'height': 3319177704366131819,
                        },
                },
                {
                    'window_id': 'nĐ\x86ԫƝßʐ҅£ɷĆɥŴȮβãΜϷȗɝфȚȬԇȵ\x7fβҋԄΩ',
                    'location': {
                            'x': 4599592669944305076,
                            'y': 5928221568516001285,
                            'width': 1756701616198575278,
                            'height': -1034384098721465303,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id_positions': [
                {
                    'window_id': 'ρЇ˙үǈ',
                },
            ],

        },
    ),
]


class CloseWindowRequestEventTest(unittest.TestCase):
    """
    Tests for CloseWindowRequestEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in CLOSE_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.CloseWindowRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


CLOSE_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]


class MinimizeWindowRequestEventTest(unittest.TestCase):
    """
    Tests for MinimizeWindowRequestEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in MINIMIZE_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.MinimizeWindowRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


MINIMIZE_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]


class MaximizeWindowRequestEventTest(unittest.TestCase):
    """
    Tests for MaximizeWindowRequestEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in MAXIMIZE_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.MaximizeWindowRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


MAXIMIZE_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]


class RestoreWindowRequestEventTest(unittest.TestCase):
    """
    Tests for RestoreWindowRequestEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in RESTORE_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.RestoreWindowRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


RESTORE_WINDOW_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]


class SetWindowSettingsEventTest(unittest.TestCase):
    """
    Tests for SetWindowSettingsEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_WINDOW_SETTINGS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.SetWindowSettingsEvent.parse_data(test_data)
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
        for test_name, test_data in SET_WINDOW_SETTINGS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.SetWindowSettingsEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_WINDOW_SETTINGS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='settings', name='SetWindowSettingsEvent'),
            ),

        ),
    ),

]


SET_WINDOW_SETTINGS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'settings': [
                {
                    'key': 'ɇШϙʕɡǸϤԂ',
                    'description': 'ϦΠ˛ΠʵăӜ҆\xadЮƉʐϤ˭ҒɍƧнǬ\x99ɜӬIɅðĤȕςӴ\u03a2',
                    'value': 'ķқǔšγŻĬqǤдѠêɄԨÎĒНέļ\x9dŌФɕƌ\u038dβȔʄÕ΅',
                },
                {
                    'key': 'łˬӰѓиҢûƖǗ΄ƣ҅ӔȢҁѷϴȻԤԪüԑїë}ȱ)ψӀϩ',
                    'description': 'ӌʄͻǄNӜȢĽλ\x9dҔ¯ӊӳϸƉԆЂҰɋǭĊʫƊǮɵȃɀԘв',
                    'value': 'aϫ҃Ңˢћўoɓ\x99ŷҨӴɛ¬ʹҳȮġϦĮИȍПѧƬŶȅÍӟ',
                },
                {
                    'key': 'Ƀ˖ȔˉӾͲˏФĪԭRfɻӛǍщ˳ˣҔɲıËΛ¹кԠǟУʤʳ',
                    'description': 'ĻϤϷ¼ơȒ6ˠQʳє@ãfȰѢʏéǌΜʩɰϚʔź˨Mǃșɒ',
                    'value': 'ΐϒΉФԄȣɏǹͱeĤÊúʑŔhѤ·ŨˇЃ҂ЪǠ.͵ʍζȪƑ',
                },
                {
                    'key': 'ɵϺʪƤɿC«ÖˤŻѡăɃǪīñʃ˘ːˣƈƣшΆόʻӝМȝЍ',
                    'description': 'âҹǩ·,ξzάńéʡǭΓԟӓȲǭŔƅ¿ʘʊӬaǭǘŻͽł\x83',
                    'value': 'Ȇűбŧµ˹ǐнfԝ®ЎҫƻǅʴϲǦΦӚʦ҆Ѱɾ÷ǃѕΦ%˷',
                },
                {
                    'key': 'Ʊкľſʦ',
                    'description': 'ӻϹѹϫıˆ\x91ĽŃԠʎ©ϲPʳ˔ЧšˣǑθKɍïΚɥɝρϮа',
                    'value': 'ˣƵȴëʅϓsǛҶ҅˙Ǧŝˏ˵˶;õ\\ojѓũȾЈæƅɉɛč',
                },
                {
                    'key': 'ˤʵ',
                    'description': 'ʂҸҒǩϝŹӯŪѺĖʶӍԀĐȨʷ(ïԥӛ£уωÇ}ҡȽǤξɵ',
                    'value': 'Ķ˾ԀǂâjˮŞðƾ°ü',
                },
                {
                    'key': "ҡӕɚ_ԄēdƂʪşӔIěƪѯȊ˅ʴȖԌ˜'ɰ҃\x94π\u0383đШԪ",
                    'description': 'ЪϡӵϸͽɘöΕ4˪iǕǵˍǖŊѓȻԗrWĳȷʛȦʌȊЂÄƗ',
                    'value': 'λгǖɝɺȎţ˖ǙȖʉϩŉԔɈƞʘЫŏӳ÷þИƶόȋʏјҘɂ',
                },
                {
                    'key': 'S³ü',
                    'description': '˴ϗǹ©эàÚ\xadȸȲǥҎѥҝǫøʰ}ϡȹӌ͵Ԍ! ˈƠӶѧѤ',
                    'value': 'ǴǊƝϒБэȡ^ЙӞƂҤmҙрʏŞMϙѠͿË˘ңč#ŨԞҲʌ',
                },
                {
                    'key': 'ѭħěēαӱöϐԍȢȦԇǿwдȵҨ»Ыͷ%șӷyƲȟ®ɾԍъ',
                    'description': 'ƐǅʗМΈԏ·Ǟȕԙ¯¨Ƨ·ȚʛŽєƯēҾzΨȟȓЂŰɸѤȏ',
                    'value': "щ'ƣӱЅЫ\x97OQөĺĤҽǧOЎɑԮӬ*Čѕ˪ƣŵȆčԡΘλ",
                },
                {
                    'key': 'ΚQ,ҥȢӑɟҝӧΕGbҶĪȗԆƬƝ¯Υϭӣλϓ\x81',
                    'description': 'ģҎÃѶlƆӻɺԙԫŎLӪϏˋʂ7ɩɖ@ԆҩƭӊQҠ,6ȨӍ',
                    'value': 'őȴёиȕÉş˘ðǑǔĢͱ$ԧõɗʡϱĎ\x8bӈk9|ŢЯɀƺʳ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'settings': [
            ],

        },
    ),
]


class SetFocusedWindowEventTest(unittest.TestCase):
    """
    Tests for SetFocusedWindowEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_FOCUSED_WINDOW_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.SetFocusedWindowEvent.parse_data(test_data)
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
        for test_name, test_data in SET_FOCUSED_WINDOW_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.SetFocusedWindowEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_FOCUSED_WINDOW_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='focus', name='SetFocusedWindowEvent'),
            ),

        ),
    ),

]


SET_FOCUSED_WINDOW_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'focus': 3674,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focus': 1786,

        },
    ),
]


class SetGlobalSettingsEventTest(unittest.TestCase):
    """
    Tests for SetGlobalSettingsEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_GLOBAL_SETTINGS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.SetGlobalSettingsEvent.parse_data(test_data)
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
        for test_name, test_data in SET_GLOBAL_SETTINGS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.SetGlobalSettingsEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_GLOBAL_SETTINGS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='settings', name='SetGlobalSettingsEvent'),
            ),

        ),
    ),

]


SET_GLOBAL_SETTINGS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'settings': [
                {
                    'key': 'Ɋ\u0380ˠɡÒįϪφӔѤǎĤԚӚ\x9d˦ӯŲk\x98ѻϯfʷʺȽːƾǽ',
                    'description': 'ŶЪʷӅ\x85ǝԥʨ¦ŏϕͰƳҐΣ¤Ŏӟϋɔ\x99ƼчӇǏѼͲ<ΫЃ',
                    'value': 'ŅǵΣȓ˾Ϟ»Џ¦ƣϹʂ9ʇŸʝ҂łϧаĭӛҁǨϞƦƑœͺƑ',
                },
                {
                    'key': 'ЪωԖéǸѤɞƋūɟRȐҌǰǊΘϼȵԠҔϟŽľϸƵхΒɵЏǭ',
                    'description': 'ďñʣΌӨӲDфΛӡæũ=´ІΔɘҀ҅шͺ\x80\x9cqS˶ɇɽϘѾ',
                    'value': '҉·µɅʥʅȷȮÇéάðғg\x94ȔɦȭĦЪ:ėŶҢŦƚƅƣ\u0379Ѥ',
                },
                {
                    'key': 'ȼЈŽӵӗсϺӶ\x91ˈ˨νóԍrǅœјɀʖɦɛiҫ^ǢѢΨǪ\x9d',
                    'description': 'ϘҒÜ~ŞƆψХ˄ÂЙ\x99ɊĚԃУ\u038bɨ˘OςϼEƁӸΚČϬΙş',
                    'value': 'Ǧƹ˙љȴ\u0382ĤƠ·˔ΰӒbӆ˧ƐӗȨȓʊͷӌɵƙР"ʔȯǧ˼',
                },
                {
                    'key': 'ʒɾŏңһòҠ˧ӟȇũӑԓ®Ӫ×ѡÄԂҿԫɚɪƅcΰӃÚ:Ϧ',
                    'description': 'ƣɉόƪϟϯлɠФəθӔ\x97͵ЏĸǼӿʧǓțsŢÒԭԋ£Φˎ˹',
                    'value': 'âҭˌ҅ʔĽ\xa0ͶӐˈΚƲÇďЎо˶\u0380ʅЪГϪˆâɮǜϤɹǨͽ',
                },
                {
                    'key': "'Є\x94âёɨÈǤéǬӯ4ǑÉԔȵʦµƲɕXżĢÉЛȏʉłɋũ",
                    'description': 'ąʾŶΈƪņȺCŃecͶ Ȍɭ;аǠ|\x8dкÆŗͽǃҗϺÎҀѓ',
                    'value': 'ѥТϪʰùΏƓ6Ɩ¼ѩЀԨǵΖʚʔӏMωĈʃŶɜӋкŢƟ˂\x9e',
                },
                {
                    'key': 'ҪʴΏƬΩӥìҊĉ¨ƭ˭γ@ʛӈyқ|΅Р˹ǳ¶ʻǛďkϒԖ',
                    'description': 'жԔiӓƋҜŇzϺԩʁģƥȉ˛HΥŤ¨љˢƥƗþчЖµĦĠʕ',
                    'value': 'ʙͼPȑę҇δƾϯΤѳȾҀԃџȸJɑȾϒ˲pʺlǥҸďšԀŎ',
                },
                {
                    'key': '·ʊθӨǔɲʼČĭę\u03a2ӠςŠʰωѲϧˢɿhǃäӿƖşҕӃÔ',
                    'description': 'ɉͷŸSϞѨǗƿC0ƀŰɶӚŖɉҨŌѵ҂ůȕĞϺ\x99ŋœɺѦ»',
                    'value': 'ĩɑüƒ1ȭț\x8dȅ\u038bą˙ѹĪĊʹǋɐšЖҔɮӛԅşǫҠąŲϤ',
                },
                {
                    'key': 'ʴ',
                    'description': '[ДúĘƘόԣ\x9cѬώʿȳԄŋѮϾŉ\x90ʈOιȝcʭǢβ¿ƿђL',
                    'value': 'ǜӵЯԐaӞǊfĦʪƼŶ?ǢƇƔҌŧ΅ΞԇЅtҗԇʮYΦêа',
                },
                {
                    'key': 'ɭƿƠĆɯӂ˵ψϜχǌ¸k',
                    'description': 'ƬLȜԛѾŭ\u0382ԟŇɡ\x92˙ɸ˅ΦȆӲǤΩϡǁҹ˸ЁюɃʋҺɟш',
                    'value': 'ϳΪϮȺȷΤͻӼǣ|Όҍʹǿȟәӂzˑ\x96ԍȴȰ:ΩȵȒ\x83ʓj',
                },
                {
                    'key': '\x84УʬͿ˧ǸϭĉÿłœҴǺʬ˴ǱƴɘӬԁñʥȶШͰԒƌϓ҃Ѯ',
                    'description': 'ГɀϘŭêӵӞïϸÃɟѵяҰdŪѰǸ˴ÿΩӬßΊȣҬԏEʭӍ',
                    'value': 'πΤȱǲѲ\u03a2ɍʉ§\x81Ǵԑʚ6ДԞόĦp\xa0Őɥϸӗ\x98ŶӒǂ˘Ȗ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'settings': [
            ],

        },
    ),
]


class ActiveIdsTest(unittest.TestCase):
    """
    Tests for ActiveIds
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ACTIVE_IDS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.ActiveIds.parse_data(test_data)
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
        for test_name, test_data in ACTIVE_IDS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.ActiveIds.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ACTIVE_IDS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='window_id', name='ActiveIds'),
            ),

        ),
    ),

]


ACTIVE_IDS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'window_id': 'ǘOʹ©˅ӵȐËRJùƟЁɑρŰԅNɲҧВXѢԫOǾ\x8fÊĿʪ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'įԁʗʙҔ',

        },
    ),
]


class ActiveWindowsStateTest(unittest.TestCase):
    """
    Tests for ActiveWindowsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ACTIVE_WINDOWS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.ActiveWindowsState.parse_data(test_data)
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
        for test_name, test_data in ACTIVE_WINDOWS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.ActiveWindowsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ACTIVE_WINDOWS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='active_ids', name='ActiveWindowsState'),
            ),

        ),
    ),

]


ACTIVE_WINDOWS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'active_ids': [
                {
                    'window_id': 'Ϫ=˲ΖȢҭʖǤƏъƄǠɡɄQţ˯ȐκAѶ½ΊԐ˭ǷǛ\x9a˥Μ',
                },
                {
                    'window_id': '¢ǮƔϤ\x98ώŢƚƉĈ҅ŽȎƮσϼѦԝ˄ʉ\x9a)ɚΗңӣ{ŊŨʨ',
                },
                {
                    'window_id': 'ԙƫÉɦÔ;ԃùȦŊЯ˸ƈʠȑ§ϼҊÞ÷İʥϹԝǝӛԎŷMI',
                },
                {
                    'window_id': 'ɺ/ϋΞʀëҍԬØбˑˣÆѴƶɴγ(žˉɽʯĭҗʴ˲Вʎ˜H',
                },
                {
                    'window_id': 'ũӋMȾҁҼř\x83ėȢƹ҇ԕѰȨ˾ӖƶʥņǄ҄ѲұƸźȂϳȘ¨',
                },
                {
                    'window_id': ']˻ǕÙÍҵӪƭ4ҫɜɬōƌƂǟʸʝƞʑӼуШʄiͿϒõɕʏ',
                },
                {
                    'window_id': '(Χѯùōкƨư=ҽлŐÐ˶ŏĈ¤Іɭ¤\x80ȡėԮȨҸ˔ŉɄy',
                },
                {
                    'window_id': 'Ȉ˔ψʒƏгʁǎϵѿ\x99ǨZҽɻʜ\u0380΅ĝŃ¯ʹÔ˘ұƯȍ҉ӯҒ',
                },
                {
                    'window_id': '.İòѱȦYǽч˒Ԁ\x8a˄ÒқɌǇƷſθѷԭƤċƈĐWëԀϜώ',
                },
                {
                    'window_id': 'жǛѱxƅƣӣæԂHʂˌƪϯжͲʒɚͿıȨǋҞԑ"ˈĜҷЪџ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active_ids': [
            ],

        },
    ),
]


class FocusedWindowsStateTest(unittest.TestCase):
    """
    Tests for FocusedWindowsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in FOCUSED_WINDOWS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.FocusedWindowsState.parse_data(test_data)
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
        for test_name, test_data in FOCUSED_WINDOWS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.FocusedWindowsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


FOCUSED_WINDOWS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='focused', name='FocusedWindowsState'),
            ),

        ),
    ),

]


FOCUSED_WINDOWS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'focused': [
                'ϋʶ"ͻΛӻҽĕйЖ˫ӊĕӹÚΜˉѵΣѩч˩єèăũ;ҒȵѦ',
                "ΎʡČИƈҭɂӹÝʺȩ϶ҧǎʰӃŢЉɫɱı\x8eĎ\x88ŌζѨѯ'ύ",
                'ŕЪԇȰЩ˶ûńԘӭӦ\u0382˃ӎćѤҚĖҌϏԒȷώЃѬʮ\xa0ĆɺȎ',
                'лόØŭŇϣgɄрєͿƲƴѻǬŲ¡тǉōɳ˪ĔȤƱɢʓʭΑц',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'ɘϑÍİʎ',
            ],

        },
    ),
]


class WindowDetailsStateTest(unittest.TestCase):
    """
    Tests for WindowDetailsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in WINDOW_DETAILS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowDetailsState.parse_data(test_data)
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
        for test_name, test_data in WINDOW_DETAILS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.WindowDetailsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


WINDOW_DETAILS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='state', name='WindowDetailsState'),
            ),

        ),
    ),

]


WINDOW_DETAILS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'state': {
                'active': False,
                'focus': 4323,
                'parent_id': 'ƍӈϬÞҧ˵ˣǎŉıʤɺӼƜɛŊęȧķšɖǋϿɘˣϵʟςɒÎ',
                'location': {
                    'x': 1278532541040171213,
                    'y': -8664592575139957252,
                    'width': -8332315348341802910,
                    'height': -8621633904368575258,
                },
                'minimized': False,
                'meta': [
                    {
                            'key': 'ƀ',
                            'description': "ɝŕȶ\x94ƔƋȤзƋƦѰѾ\x94ø¢'ƭɝǌʇѣԔʹƗ<˚ҤԢӻӏ",
                            'value': 'ȎdíĵηӦɊǿͷԩёӜӘϦ!)Ȃ΄ґÇʚʟQԊԍϞĨŤоԏ',
                        },
                    {
                            'key': '>ү˽ɗԬ7ƴ ɓêǽǆ=ϑĩ¼ӎφЫGǸ(ͼÜªҋЊŁ˨¥',
                            'description': 'ʅʪҸřĄ}ӕŎ˃ҋ]ǌǧŁ9΅ʹʤƠɘ_ƟӅƇιľĚΉӢĶ',
                            'value': 'ƺңĨ\x94{ӸĚӌȁҐѳ¶ΗαͰñÔĂʋʈrԋӅӫӐʩŏР\x90ѝ',
                        },
                    {
                            'key': 'Ԯʩ˽ȈʦŬűȪңġМʟƲӂēΧǳŖˉϫɳɭ¬ǎŉǈӱƴĿѱ',
                            'description': 'Ӕ˵ʿơÑѽ˒Wϋб\x83ŧȴȯǥǳͽɣӀȳщĖԖƹƇӦəʐϮȽ',
                            'value': 'ҊͻнÿȾȫΥƞϪ-ώӷГƏѴĘĔ\xadҹŀ|ȪѸʹ»ҳΪƄѫю',
                        },
                    {
                            'key': 'ѪˢɶʞƬɡ9Ӗç¿ɣȜԁ\x92ЋČщ\u038dұĝӥɮτʿ',
                            'description': "\x93$\u0381J_ҦĿ§ǛӒ˼ӱəŎƎȣ΄ϹȩϔЦљ'ĄӱʎʱЇƔЂ",
                            'value': 'ƸʡΣqЋĄΫȧǛӿώͼg\x81Ԡʠʡшśʉ]ҋŚϻ\x82ӭ¯ÿȞ˂',
                        },
                    {
                            'key': 'ͶӥшɢÑãçŖ',
                            'description': 'ϓµίɮĲƌeɺřоśʫͿďǍŅԙϪ˃ŋˍ¸ȋљŮOҟƗȚǓ',
                            'value': 'ǔƴңçХɌśͰӮ˜Ԍԭɪѕђyĳǝ;Ӣη\x88ɺ',
                        },
                    {
                            'key': 'Ӆ3ϴé˶>|ʥǊФͺԋҘȲҪΦΙɞʲԟ¦ĖÂ',
                            'description': 'ʵηԘƍԇϸɜѭДЫdȖЁŉӸÂɡХӬϺȌѩ˕Щɮ3ӿϻ·H',
                            'value': 'ˤѓʂ%ěѢξʼВͼ˗ȅѴҞŎǧ˯ΨqϳчϛåλǏ&ųγ҉ʉ',
                        },
                    {
                            'key': 'Юъψ\u0380ΏɜţƹАϊɩƢǍȂҸ_ÐǸиˆƩʲɚǊπɼʷȭɰȗ',
                            'description': 'HѱΤϋӟ°т\x7f\xa0ӋƩvŷǈɕѿƦԂ˦ǹǅƂӦňŽɄϿʨȬ\x9b',
                            'value': 'ѩV˼ю˷§ĶχϾϣˏ5ќгëǸӨˇԋțҢǱ?w«íƼũ҆č',
                        },
                    {
                            'key': 'ЧţѐЩȾƅÉy',
                            'description': 'ʶɽѬʲˡǄѩǏŸԁʎʷŦȀžǣǐ\u0380ԃ҃ήЕϏ_аɫȯԉΪѹ',
                            'value': 'ϱÏџ:ɿșʮӉӰ˨ɐôЀѪÎȁƲѷÓǾƭǹĸˎӹͳеɷҔҰ',
                        },
                    {
                            'key': "fҕȑ÷ԘќǢșԁ©ԆӌŸŰʿһd'mԭГɺԘј\x9eʢθƤѳ]",
                            'description': '\x87ÔЧ˖ҲɄȮºӸӠŉΰʪяτĥȓ˭҈ȂɔːоώΥǡκЕ¥ě',
                            'value': 'δΆчмAfԤ\x8eϒȃ˼Ѳ\x89ɭʥ+ƈAί¶ąŵҌ1ѯRȇǤĒЏ',
                        },
                    {
                            'key': 'bԏѸǪð%Ђ',
                            'description': 'ӤyȌɧƧΊǞϕ¹жķǋʅϗĂдnƿβΰӊҲǢȩҧҐԋ˽ʏԕ',
                            'value': '¸Ļȟϖ\x94ÊЈѺӒԛʯƜӵϦ˔˩ƠЦӴ(˴ћʅũÔʟēЕ˭Ů',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'state': {
                'active': False,
                'focus': 5300,
                'location': {
                    'x': 3438632876282479827,
                    'y': 1293725173551378861,
                    'width': -7269210533478687756,
                    'height': 2653254131600262921,
                },
                'minimized': False,
                'meta': [
                ],
            },

        },
    ),
]


class GlobalSettingsStateTest(unittest.TestCase):
    """
    Tests for GlobalSettingsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in GLOBAL_SETTINGS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.GlobalSettingsState.parse_data(test_data)
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
        for test_name, test_data in GLOBAL_SETTINGS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.GlobalSettingsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


GLOBAL_SETTINGS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='settings', name='GlobalSettingsState'),
            ),

        ),
    ),

]


GLOBAL_SETTINGS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'settings': [
                {
                    'key': 'ѷұĴʽÃȼɈȄӺΘӒȧЫΊǏªΫŋ\x95ȈҢȃêǴȹξύͲξΡ',
                    'description': 'ƹɐϢԤÃЪǖVΊ1LŕԪԞх>kιϩϏԪȇϒє˻Ӣɜƛӑ\x8b',
                    'value': 'ȾHЂǇɤŐʿɕĨÌ\x9bȎԬͱӄȻƩϷþƇȽ·҉ӋŝάˁÒυϤ',
                },
                {
                    'key': "ǠϹʚ'ľӉԓɄGΊρɶȑѵȌûǐƄϖ\\ͺ8ϫȦӒџ\x8cįúȾ",
                    'description': '\u0378\x8b˕ϷʽȋіȕɰдʻȃyӕʏF{ӐϩӺӪԠї\u0379˹ԝĒ#ϛĬ',
                    'value': 'ʼǝ¿ԎȸʬΌDǓʅņШӤŢѓԬȖƷ~½ʉТ¥ЩƧlrɀ^Φ',
                },
                {
                    'key': 'ΜӔӐɓĴєӴҢƀǇɎåў˒ҡĀ',
                    'description': 'ğІǟ˪ũĔҸ\u0381ћԑˍªЩIƖƈʤƂ\u0379YίŬĄ[҆ʣԧβĤǹ',
                    'value': 'ѻʎƏη˛l҃±ǖƁ\u03a2ϗіȗҲ$ӉѱPӰуǁԘϩƓΎǳ>чâ',
                },
                {
                    'key': 'Ť',
                    'description': 'τƭțϕҞѡəˈҍ\\K\u0382·ưúFʇȴǛ\u038bŚ˺μȫıs҅é˞ɹ',
                    'value': 'з²ɼ4ʪԪˑŔƨǪĿĺϻɟԆӅϭǞѤ Ǯϼ;ѦóʻόɤtϮ',
                },
                {
                    'key': 'ѓӋǲ¡è˂ΒːԣƇӁɦɆѠʍ\x9fрĬѦGǃËɘǆѾʱʉВ\x97¾',
                    'description': 'æҧåʾȐˤзɊͼĦʚɗЄǱͰ\x97\x96ҼƬθäİӶϽʻʏôƒԓƷ',
                    'value': 'Ŭ\x9eԞ˝҄ÏЀ\u0378ȞäƜˠԧ\x8aӺOʮÀұǚE\u0381ʊƭQĦϓёϳЅ',
                },
                {
                    'key': 'İԪΨΙʨͻӯЭΧ_jǷȏŨϛˡλԃϫť',
                    'description': 'KӃРШÊŕˀƠķʹ˔њɆƶǾɁž˺Τ¤ǆŋҊǅŰʿˠåCҼ',
                    'value': 'SŋŏҲoҒϊXPѴëǤȒƥǧоŝ˺йȀ˲Τţ\x7fŴʉиuӐͷ',
                },
                {
                    'key': 'џǪŷζѕǞ¿ÒÃ\x8aƾӽ1\u0378ĔĦҴ\x97',
                    'description': 'чǗΐƍćRȗͺͽĺȥÅƙː˩ӘҬåǢаԙԞÛ\x8eYӆė+¥γ',
                    'value': 'ȯDɤɓόӢŒŮʕԕ2ǨǒзþҋȕҺ˄ѓƏʲҲǉĭťЦάņҡ',
                },
                {
                    'key': 'ɵƠǶĕŪ~ŌĮкÏ˨ӈ˔ԩŒΚϭ\x95і\u0382ĝ',
                    'description': '˧˒Ȟǔ¼ɥҸȓ˾ζĭĸʃĆȔ\x9c·Аė<бĜΗԊѕţҌ¤ĤѾ',
                    'value': 'AƅØŌɸ(ӸһØԕĨɎȘͺ\x8bƈǄjɻ˲ȺHԮ¸-ɨӮBԚw',
                },
                {
                    'key': 'ѧŧЂϐҀǖƒϻ',
                    'description': 'pҘƜˎɲŠãƅǰȆХĢӨ\x90ŰʗӈӵȋˆЅʂɓƉǣѾɺȝýŸ',
                    'value': 'ňÍȅțццȑҼĮźkҀ1ϭмԣ¢ǔˈ˰ƏPZʻϞίЉșʑЪ',
                },
                {
                    'key': 'Įơ҂ϪҘ϶ϖЌȉЁӗЬφǱ¸\x8cЫ҉ƘҵɥıѯεЀʒɩëҪЇ',
                    'description': 'ȺвќgӤČѝΐĊɨΕƁʩЭ˩ȋГ&ԜȱéȖŖ<\u03a2°ǖʍǯΕ',
                    'value': 'ҳҿΞš¢Ӟʐ¾nˀ"ώɘАˏҩú²ªÚĲЦŵĿǄV¿ԓɅυ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'settings': [
            ],

        },
    ),
]
