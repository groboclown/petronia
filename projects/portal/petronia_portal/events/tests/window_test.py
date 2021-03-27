# GENERATED CODE - DO NOT MODIFY

"""
Tests for the window module.
Extension petronia.core.api.native.window, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

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
            'x': -7764980470565073134,
            'y': -360680296531062512,
            'width': 7641055766004970545,
            'height': 3261106740047021654,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': 6693406331600057236,

            'y': 8187836852668532885,

            'width': -3875686308322809094,

            'height': 6023487167913967385,

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
            'key': 'Σ9ҵʨƺʘғǰʥɀÉ\x99ƍ˟ĽȾϦӁ˸ŘΫŴиɲǙ˪ӕǄҲʔ',
            'description': 'ïԬҔŘƮȭxÔюѡϣƺėIKǵϢəϨӳЖũǖSԗuΛƌЯë',
            'value': 'ĉ˼\\ȩĪā-ӟʕ˓Ђȸмȉ9ˍ҄ɨæ3ɣĮǒƑΞΡǲÖǂÍ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ƥ',

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
            'active': True,
            'focus': 5488,
            'parent_id': 'ИɐüϫÎʇʯԧΌЃѺ\x8dӠŤ\x9aѳтɠ·\x94Ǚԥħ˳ƘǡЯѕéə',
            'location': {
                'x': -3603623106549270097,
                'y': -6880507296969665357,
                'width': -2259187802286590312,
                'height': 4619408746671284359,
            },
            'minimized': False,
            'meta': [
                {
                    'key': 'ʊԃγƸb(H~;ĺĐDΘӾѹ˥',
                    'description': '^ʁǐOýќíψζĻ¦ϒԊϞҳǰŏ҆Ăȼ˘¿žǗΐƈʧƐaħ',
                    'value': 'ÂŘϘʓɆόqѮɏ~ɽϲ?ΌǲĞɊЀ¸ėʨѝӾȖƼǾƬȚҴɉ',
                },
                {
                    'key': 'ɺЀĂȰėȵǱɝҌöңӷйǤưȧһĩȵέ¡Ī»εӂ',
                    'description': 'ʊmXéЛҕѐЌ˗ʥǒőĚÖFʆĬƫʕ˪\x93ĢĔV\x96ʌˬӲːА',
                    'value': 'ʤżϕяѱˉʹɠp˨ͳĠZ˔%ĉаϠψ¥ЊӴ`ǈÈМ³Ƌϙƌ',
                },
                {
                    'key': 'ƮУЄɆŖʖÐϳ7Ϳȧ',
                    'description': 'uҺĻњШĕЉ¡ƤœʟƬhӏĦҵȐŸÉЃȏ(Ьαȗћ҉ЬɆѷ',
                    'value': 'ɸ\x9bӗ˷÷\x9bËŷȁѩπɻˁΩʱЊŸȯƃʱɬ˥ήѰ\x9bБɍСí˫',
                },
                {
                    'key': '´Уҏʪ´ɑΙPă˒ŹüοǕɥ]ɀȤЛңϟƓÚǼӬ|ǱҲĳɧ',
                    'description': 'ԈΑǒПøС%Ë˲ʍāÀðƨ˹ǿҏГɖfÊýԞΰҮҟИɪЪǓ',
                    'value': '\x9bʓ\x8bбŕÔlͲňԧPӸɿϬǰӹ\u03a2Ԧʕ˯δҮ\x9bʔФξǩҎƀT',
                },
                {
                    'key': 'ү,Ѹĉѐ°ƸɴǴӺӕзǋӋ\x95țԂȮʰƫΌʱѪӜӀƤüΡƄє',
                    'description': "ŘԖԦԈћФˇǙǂ˵ΦĆ£Ë'Қϫ7ΡŐƓЀʲȪAǠʁȉòƍ",
                    'value': 'ϵψżλ¶İєā˲ӞαϞҞɨÃɼԞƏȕԢɔǇƅҝ˔а҇ҕǯĺ',
                },
                {
                    'key': 'ēȝӬϠ)ҕĸȰ',
                    'description': 'ЯҤɸĝʌâӬ"ŃʬϘҲџәɻþƈҦŧȨļúêѻ¯҃wSԡƟ',
                    'value': 'ƆȺӗԉҼtѕÿҮƯȯӄЩOϯԜҴĝӖÑ|ԋҷѧȈȈӺɘĦ͵',
                },
                {
                    'key': 'ӫӪҪȽ˔рlҎЭ˩Ɓ\x8fѓƭĚЧ ϓӈĒ',
                    'description': 'Ѝԣ;ӈьêÇεγh]вњЮˍѓĕζϺѲƔưΆѾӗŉòӳӏԊ',
                    'value': '&ǂt[ӖӿhШĖ®ԅԐʰŨǆЩ˨ǥƺƢϹĜɢĺȃѪƭƜÙҀ',
                },
                {
                    'key': 'ŗŞϞӉ\x97ǽʔԠȖǛ˖ĸϘɓюȕɆƮǘǚĚSЫ»КǏʕĔŪɞ',
                    'description': 'ʤŶ\x97їşͶԠ\x94\u038dӪӦ]ĒˍĳɻѨβƂRÌҸȻ;ʐӲ@`ĒӾ',
                    'value': 'ӷϳǈŢ\u0382ӻӔĪ˼ǀȲ˃вȥӝӨ˞eǥϢӺǍҠ˹Ѐt\u0382ƾͲ˩',
                },
                {
                    'key': '˽ȦŀѣѸƇƚĝλӗƉȫӆȧøÇ\x93ČĦΣ\x96ŷ ȈͽѹҚǭϖδ',
                    'description': 'ťĩϟėź}ϦÞ"\x8cDƸʒӌƕŰʆѭԟīӴҕʝΘOʶ˷аÌψ',
                    'value': 'ˎµϻЖƁț\x99ѾϷŔ\x9bͿŃѝhUљǳԜ\x84ʪɓѬĸǱοxβҹҡ',
                },
                {
                    'key': 'җΑȣ˅ʋŴƏǰĮǅɯқ²\x97lӊȹ',
                    'description': 'ǊŖΌȜѧƳǯÜŰ\u0383¬ӫПÖƁжГҍĖӬҙϦϨԨŭ\x88ΟȸǪç',
                    'value': 'ϨίβϴζĽӼӴr΅SЉӴǺϲҙθÎǑ¹ɐͷĎӓӲӳưЎҬϮ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': False,

            'focus': 6369,

            'location': {
                'x': -3282231159110740778,
                'y': -1673095249660657976,
                'width': 7981888696138732894,
                'height': 7203778821447402226,
            },

            'minimized': False,

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
                'focus': 8491,
                'parent_id': 'ȟzͺÀʍ҉ΈƑʅҵˈʨʋɼĞ˷Ƽ\x9bʚǘ\x95ήʤ\x9cїƫͿ6ȵЏ',
                'location': {
                    'x': -8924406054469291413,
                    'y': 1753370449298750063,
                    'width': 7340081981356947236,
                    'height': -5052638944099089165,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ȵΣԕƊʃȀ\x8fʤƉԢãА5ŮӂӐщǢҁƚǅиΚ˪Α҆ǮĽҔӾ',
                            'description': '\u0379ϦЖǾʜѵƭʚѼĢČÍĵȗɁɂѼĬíÅĬŶƘѷ\x8aŗĚǑɆˡ',
                            'value': 'ęԕūʁəɤɋǲćҠ˪lʡҊδŷȿˆȩÒ˱Ĵ˰ҚԈƽɿĺɗѰ',
                        },
                    {
                            'key': 'ʚР϶ȅҩʱϥҺʶŋº,ʦžЦ˭Òǯ?Ч9ɰ',
                            'description': 'ȵΣξ´Ҧñԋ\u03a2¾оǒѽEӚίЊǞŮĤȽԣƉšÂŰʰıƐϘӁ',
                            'value': '³ϠӄҏƁщҾü¸ƖʉĸƲ\x80GŗφʛϑӚтҵ½½ĠĔƶӜҟѺ',
                        },
                    {
                            'key': '\x93ɯɁȯрЦРǄӑӴΛĲ˗γǇџŀƼ˱ʜ\x81?Ѵ\x85ϓ˼ǝҐƝǿ',
                            'description': 'ȭӈΆœʜԢŠȌЈČѐϼCԎӋ\x94ԡЋƘþŗͶˤªжʛqŅʿӕ',
                            'value': 'ȓӯƚĈˌ˾ϷÿΣġ\x85ʽĿϊΪǀ²ȋ[ʗɺÿҬЦ˹мßʸҀŇ',
                        },
                    {
                            'key': 'ԀЗѾx҈ĴԮϔǣζ+)ė²˦Ʉáǂ',
                            'description': 'Ӥʸħӥ\x9fɟϫԘЎӀʑҫϗɷˑƚϮѳӅʷǏԂ7ҝϷ×Ǡ+Ӑѫ',
                            'value': 'ѣģʇѢˎҌԮǌôȵЛÓǒӸʰ{ÉlʪщɈʗΫћ)½\x89Yҙʳ',
                        },
                    {
                            'key': '\\ь\x89ˤɇ˒¾\\˽˼ʪʊΎÝҡŒβď¬ο}Њѻ\x97˘ī(ϝ˷',
                            'description': 'ЛǙҪ˶ńнƫƭϬίˏƉӂҋʈάӟϭňӊʺĤşӲ˵ÈѓЗ˸î',
                            'value': '!ŎǠԀƽʐŕƁÆӵёʃnþʁĨɦƧɖԃf҆ԋˈƐƦТӎӔɠ',
                        },
                    {
                            'key': 'ɸΕƺƎӅ˨"ЂЉʹԉѤʝʭϊ±дˤӌƩ2ΧƔȏƪӧùӽǿϾ',
                            'description': 'ПǕ\x8eǸɒʛcԋΣόȽӻʤæėȞѫэɣ¸Ɵȃ˽΅3ϑ®ӯšư',
                            'value': 'ΆǉȺєƂE|Ӈʐ˳Αȴ(ÑЫ°ϓÌƫȢ²żΟрƄđӏԒӼȤ',
                        },
                    {
                            'key': 'ÀʲʄņƱǍНҭ',
                            'description': 'Ѕ˃ϢҏҞγɨԬȆè1ʚΟˍɩѵ҇ͻƈ\x97ϑſϰyćIѱӣǦή',
                            'value': '˜ƲϝРɟÔȟԠ',
                        },
                    {
                            'key': "ĿͶѵ·ŞƉӰЀŌ';ɕ\x93ɏϨ˖÷ԔјΉʅƩúЎϝ\x86",
                            'description': 'Ǣ?˅и\x8cOůӤԟѦčɽϐ\x84əΪɱŃξ˜ůЅҐ5ѣ˺Ȍ^ēԛ',
                            'value': 'ŤɘǂŊЙ˄ɰĹɺ˖δɧӸʥƱ˘ÍèНԂЏơɟŘǖɳʭʪˡϒ',
                        },
                    {
                            'key': 'ɕƠЂŒġ:ƿ\x93Äǉ(ѱĤʓͺǉïѱəǟƾIʂǳȮǽŒ',
                            'description': '¶šòҨ¹ǡΪǱфĂρ˓˄ã\x81ʈω¤˖їѡӺÛƶrӂλŦѐˬ',
                            'value': 'ʄЗȃѴŚѼ4ƺςѹԨ҇ʩӰѶƑƧԮͿœôѐƀԌçѺčǒĎO',
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
                'focus': 870,
                'location': {
                    'x': -1764222522739365531,
                    'y': 4455292204696519972,
                    'width': -3960574674597992693,
                    'height': -5346460350321161703,
                },
                'minimized': True,
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
            'reason': 'K9ДȟԧҘeͱҹѲůŀʢĘʉρńѿςӝԓϓz»ʼý',
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
            'keyboard_focus': 2407,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keyboard_focus': 8748,

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
            'window_id': 'ȳQĞʉǱҀrşƿǰƕ¯ɆʝżҗʏlïєʣԘВГǠѿςĕǥ\xad',
            'location': {
                'x': 3625212326269167130,
                'y': -2005758871635985945,
                'width': 4859368982444223834,
                'height': 2179067385421024226,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': '_j˶ϋԂ',

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
                    'window_id': '%ɱĲäžq£Ýńá͵ɗɒɀ1ϯéǕԗ˸nԢȰũȻκδʴˮɪ',
                    'location': {
                            'x': -6059967262374436379,
                            'y': 6476758460040045739,
                            'width': 2899099868570455119,
                            'height': 671735895087910363,
                        },
                },
                {
                    'window_id': 'VҾŐĊĺӴȃЎŏʆǈˊΓқƓ\x90ƣӁѕńƋҗȔӉȮ4ťԧӿȏ',
                    'location': {
                            'x': 2431370368333652097,
                            'y': 919990402280336411,
                            'width': -6272591922399812252,
                            'height': -1517731828806982989,
                        },
                },
                {
                    'window_id': 'ǽǷɼXŁУʃɽǾ˔ƋúĈѸźʟЅ˟Ǩ˴ԠʼԖјɍŕǀΟҵ\x95',
                    'location': {
                            'x': 1174984215814392808,
                            'y': 6633216404510513788,
                            'width': -5311586463333363691,
                            'height': -9110535303609122711,
                        },
                },
                {
                    'window_id': 'ԦʭЫ\x8eˠȘulɛˈ\x85ʩūîɮϸØγҌБʮԝƎеǲǖШˎʧƬ',
                    'location': {
                            'x': 4132782005774272531,
                            'y': -7439412797000852352,
                            'width': -8503069663086926401,
                            'height': 2456798498959142533,
                        },
                },
                {
                    'window_id': 'ОБȗСҰϳϱвɚʍ¡ļĵ˗ȨΚvÜӛьƥРЎîʣЂεćðӮ',
                    'location': {
                            'x': 2224962428707505985,
                            'y': 9111254449625688214,
                            'width': -7330671442280117367,
                            'height': -1719935682978769728,
                        },
                },
                {
                    'window_id': 'Пҵþ˦ǁɺϪƟƽɭԨԥŚӵ\u0382\x80ÖˡǣưƟʎTԁȫйƼΠғΑ',
                    'location': {
                            'x': -8998799769184516977,
                            'y': 5091559066157555911,
                            'width': -1282616232898980195,
                            'height': -6912084857525761172,
                        },
                },
                {
                    'window_id': '˸ӽЙǬȨвưŊțмΣĽňѮČѽ\x9aʠкəρˠŠԣǨƐƿюӕ7',
                    'location': {
                            'x': 1319290843031778935,
                            'y': -1248956650246757774,
                            'width': 7078569663708829125,
                            'height': 1859038871529582728,
                        },
                },
                {
                    'window_id': 'Ȅ˚ԁˇɻǖđ\x8cȬʰӄǏӮ³ύǶЀҜη4ͳƄɶϧæʍȎǽɤΥ',
                    'location': {
                            'x': 8548440542081192345,
                            'y': -8829260297484880678,
                            'width': -506930998107053458,
                            'height': -3687498784144033765,
                        },
                },
                {
                    'window_id': 'нʼѯʫɣǫӼğҝƴԀӎȞϴƑÆмХ҇ǟÿęϡɷ\x9fӚČĤˁˉ',
                    'location': {
                            'x': 3773470974847501393,
                            'y': -1992591125391431832,
                            'width': -7085852432017833160,
                            'height': 5696452280937615684,
                        },
                },
                {
                    'window_id': '˙ӡˬÞЦ\u0380ιѡӣ˳КƸƐӒӃ¡ViʣϽ\u0382Ԓɪ˵œЊЏӴ҆ʐ',
                    'location': {
                            'x': 6673621930380778844,
                            'y': -7678669043516488613,
                            'width': 921229430998431927,
                            'height': 4672202803586432286,
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
                    'window_id': 'Γɻ҄ɫø',
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
                    'key': 'ӢҪͽҺ',
                    'description': 'ǇţŜʴѯʂԑ0ȣ2Ϫχ˲˂ξΓҀȢ\x8bŁЛùŀă^Ƕɍ¦ĖƝ',
                    'value': 'ˀʮǴхϗ˱ʤÇκϐʌɥҬȶʭєGĚǮѶ˩ǋ\x8fдӴĀĜʒȍˠ',
                },
                {
                    'key': 'ϚʻƣҵþѬƽŤɣѯқӚǇɑɴєǻŦĹ×Ҋ\x97Љı;ŧVȨ\u0381ȩ',
                    'description': 'ƄЕçƭʳŽɐʪ´<ǐȶѨɔ,ˣ(mӌ˃ȩʀ\x92Ξѡ<ҹĜťϹ',
                    'value': 'ƙ!ǀDɞ\x90ыԙǦҍɜÃÓҞΨŗĦǨǜǈξҒϢǩÉӱϲĦӠ\x88',
                },
                {
                    'key': 'ƮБĂΆƎ\\Еɗ]Ȓę1ŷӫʐ˅ѶɣşҭǖӖιΜʘľξ',
                    'description': 'ӊԁŰʌȯÝȅ9ҌүưԠɚЊƣӏұɻǿ}õƾÁғʈÉЄĤˮμ',
                    'value': 'βӒžәɳǟʾԑȿԧȼϟ҃ʪњԙΤŘϩŤƶǱВҽJj,Ϋȷ\xa0',
                },
                {
                    'key': 'ʺƆ',
                    'description': 'тмόɨѲ>0ѧǔyЌȒɶʪɁɸԖʬΰľțɪцƨӇЫȠғĄ@',
                    'value': 'ǟӟһƿϣWŌӯαŭºKԠů;·ˁЀҀNÎλǤǛàőхà8Ǎ',
                },
                {
                    'key': 'ӟ',
                    'description': 'ӄƍƧǇƺ·кƧӝӇϐŸўč ϕρŒʩľ˵ΤÕӻźʎʧÒͳС',
                    'value': 'ZξǇƄ\u0378¨Áʑǘ˺ӦʷԞЧҩŌ#Ϛ˾Ϸ˓СǴ҇ȗ\x8aɊ³+Ʊ',
                },
                {
                    'key': '\x7fĕ;ɞ5ȔΊѼƫǘ.Ř҈\x90Ңǖ',
                    'description': 'ȬӌԮș˫ʘѷϣjșԮѬǧyӀӿǰ$ϲό5ύ˝ȄξŘWχƓĬ',
                    'value': 'ě\x93šǢ\\ĆίȏĻ-ТŐ©ŚÅѓʴьʫǇȨʩпӘԁˮŋΊґɮ',
                },
                {
                    'key': 'ζŐáȘЉŭ:ςŊҪ҂źҏӮɏ',
                    'description': "'ǅǃҝǮǹԩfďɅʿəǆςŵįʙеä&ϩӎđАíЙҽĘť¥",
                    'value': 'ϵѸПҢ\x97ԂԧÎӂKлŮǵ҄ӑŽHȮ}ѯҖcșʝѢc˻Ķĺ\x9a',
                },
                {
                    'key': 'ƱȲɼıƗo˕˺',
                    'description': 'ϨėȂГњƓԏįɕƅҢȠ¨ҍËξȭԏɋȰϞλΜ¿ʸʎ\xa0ԃ/ʖ',
                    'value': 'ĭԬӺœĚƩѭƋʞp\u038dϥʛԃϕǅΆțдàŦоǿӋƊ¨ĝԠžɸ',
                },
                {
                    'key': '\u0380XӞϸԚȻԇɻʚ5ЄϓӦŕйhІӈЙ\x91ıƼȄΨĳȻ',
                    'description': 'ӖӰʨӾÔϊƲ³ҭѷ\u03a2ϚĿͱԌαÕ҉ũ/Ȝ_ЗǼ\x9aР;Ԯ˰Έ',
                    'value': 'ѱɺȲˑӐҵύǁɞʿԝΰѓqԎҘþϿ»ϳӝӁϕïȇѣãɔçσ',
                },
                {
                    'key': '\x98ųű\x81ɵˉ\x9cҲʒ',
                    'description': 'ǃʲ˗ǏĄŶϟΆƁ\x83ѶʲːΞүɗïχӣǈԅˋϱ4Μıʍ1ĘЏ',
                    'value': 'ŷŎ9щЉϴQ\x99\x88ćƯǶϫТŎςν¬цѹÿʖ1',
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
                    'key': 'ĻĕZƑŒʹĽǝɜÜҽͷƋӎØШɒɩWπɚ΅˽˱ĬͻɈ>ƸĒ',
                    'description': 'ΒΡȋŸěҢӲѝȤŁéȀŷTɊǣưłǳŹϛΤtʥϬn',
                    'value': 'ĩ˞ŒɖЪ\x8cÌʽϭΔˠцŁƠˏΝ\x94˜ǊǞЁÌΫˍҢ:iɈʨƉ',
                },
                {
                    'key': 'ɼȡˢʻГӟüĚӇȣ˓ӏɱΑѽԍƅɓʷʏȭ˾жҦΧǌӷ\x83yӶ',
                    'description': 'ëŌΝʽDɱѻɏ2ȤɠђңӱгŹκƥƨөЏȽě˰Șʨ½ɩƷf',
                    'value': 'ƓӅĆįƳFӲθǸѧɔǻԐʰʽѕΔҮďŉ\u0383θҀҟȜъЎˁΚÒ',
                },
                {
                    'key': 'ȅ˵ԥʒϷԡżԒƵŸϩƥԔбȑYǙƎFЩЯӾéSπӹĶˆӄ˞',
                    'description': 'Ӓɝнƻ\x9eØĖēАвAʴ[ǰÎǢʝ»ѨɒǀńϫýɼϢҾ\x96\x89Ԥ',
                    'value': 'hĚǆͱΪˊɱˀыƏ´ϸϿ´Ƙ\x9b˖ʋоȂԠµΘɾƀђß\\ēΡ',
                },
                {
                    'key': 'Ιːλ#\u0379щɠѪđQӷǍÎЊЮҫϮȩɋƋӜXщ[ђĭ\x8dηɤԅ',
                    'description': 'Ϡĭʕl}ӢӧĽĖŻ҉ʙƾЏǀȭ˙ǪĝƏӼ҃ʘ˻ъ¶ãϲ҆Â',
                    'value': 'ϜǮȴ˻öϒԖтюԃΨıűΩƗǧ\u038bоʯǒԔȕǰ˜5Ʃбˬΐӂ',
                },
                {
                    'key': 'Ѷӄ˛Ψʿ\x96:ɨϑӟѪ\u0379ɈʫҝԕɲȇčϬ(ȱ',
                    'description': '҇ԌфʤΞȌϣŜŨȒʖϡM¹˄Â¨Қԁʊ&ӄΑr˩ȃùƞҼʏ',
                    'value': 'Πȇѱʥ\x89А\x95Ͼǡ˃Ɍǖϡ\x9bԏЇѽҌј/ǓС\u038bMĻиΉίXŠ',
                },
                {
                    'key': 'ǃϨǟϘχǸψӡſ}ŠÆϲЉƯŔÚˍEtұ˹ѡ˕"ϦЅʍц',
                    'description': 'ɽƻѿůöúɏσ҈\x8fѨɻʲĉơʴʐYӯ˽пӰҮȈ\x93@˼ӱӱʺ',
                    'value': 'Ұ˛ĚĸҩǄӮʛ£ϐʽX˯ǔҸ҉ȺӀЧˋǁ>\x98ǻϦ\x97ӳρˮԞ',
                },
                {
                    'key': 'Ǆ',
                    'description': 'ȅЄ\x8acҥбԇąēӴš3ѹ©ҾԂѨɘŮȁĲқˆŦÜίİɘǖÀ',
                    'value': '¾\x82ћȊô˔ßЀлΐȸÓÐ^ńʊ\x9bȵаȞʻʟŨʄ8ǌρȶλӱ',
                },
                {
                    'key': 'ЬųòϨǈĪɎԢԭӒǉʆЏԀɵƜʽԌĉɊʍωӄԥƬŚkǻҁƾ',
                    'description': 'ТʂѲśȵŉǄϸԐɇҽьͻMÆŲ\u0379ЈԂԦƿƵñŧʬȐȬxѽŊ',
                    'value': 'ƈ͵¢҃͵ҊΏʤǌψФȅľōǤԛΞԈԒ8ҖԭʊʔҲg>ԢԊȹ',
                },
                {
                    'key': 'ғuΆԏпӭԫӱȂώ^Ҍвɠ\x80ѐˣκӮö®ǃÒǫĎҷАўɯ',
                    'description': 'шԫrԋŘɑăʩԩ\x91яƾ\x88άũĠјФ˃ϴ˫ËĎȐ\x98ϴCԝŧv',
                    'value': 'Ɗѻԇʉ҈ҎǼXǺȚ¯ɖʂȏlʺΑƬʢӻйíÍшǙϝʾǶұʄ',
                },
                {
                    'key': '&҉Єɍ',
                    'description': '\u038brϮ»ĄӶӕˡЗΡ*ϋŬ]ԁϦ\x9eƣƟѕuыԊґĝgԊȜȬƋ',
                    'value': 'ӍԐ\xa0ԣýĞ\u0379Ңψϛ\x96ɤg˺Mψ\x94űĮǏ',
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
            'window_id': '¾ɓҝԛЎǐҐBìε϶âȶ\x85¬\u03785сλэȱӛȧҜҹġĀеўғ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'νҴϐЇƵ',

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
                    'window_id': 'ȘŤЍҗӽғɩԎƘSцMŤ΅ĜӅАȔɜӼPφłaΨЯј£ʊ\u0379',
                },
                {
                    'window_id': 'ҰƹԠſȆ\u0378ȱѳī˗ǒʽʰĝÆʺċēˑÝǿ±ѲŷʠҩʕΖѳɆ',
                },
                {
                    'window_id': 'ԟԓˡѻԠŉĜɑҭ҉ˬȆϳͿЉЙˤѥ(íԙƦĘ)ʲβ%\u0380ΐƳ',
                },
                {
                    'window_id': 'ЃÇÅʪ˪вПÉĴʠίɬԠԠƑɇǣʹ"ŻΉǑˍ7ƀϣŽ\x9dɂϚ',
                },
                {
                    'window_id': 'ʌ˗ιƦȳԟӫmʷʩ˔ɡԭv˥ϩlŌDɖӁϽƭȟ8ç˻Ɣѯ®',
                },
                {
                    'window_id': 'ѭȂ\u0379˱ȉ ѩòȩТȣɃѧ˄ŭҁԡϥЛȌǼñƑʓÎǓžϰιӬ',
                },
                {
                    'window_id': 'Ɨ\x8bπƉʟđƤΝёȜҫˢödƪĆsĦǫķΠBˍõԉ҈žBԧ˙',
                },
                {
                    'window_id': '˲ƎǴŸͳϡÀŽō;ϞȕƹѪĎŅӿԟтўƦͲɝΩɤ\xa0ϋµ¼ǔ',
                },
                {
                    'window_id': 'ԕ˃Ϊxʹ\u038dГƏÍʶʰȄŻҚІΞơοȿ\x92ʾϤʍ\u0381ӵþɧИηċ',
                },
                {
                    'window_id': 'Ï7˗ӚMҥѪԧȦˎɳʤŻΣƚθČŠǖΉϻɽɾƿ\xadӝĒ\u0378ãÛ',
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
                '˨ɹϔ#Êѿ˪¾ϓΪҲ·Rϡλ?Ҷ˘tҳv˸ԑ\xad÷ӀʛÇй˟',
                'Әĺ\x8aʄ/\u03a2ƣΰʈȋ\u0383ͼƞΈʻΛ˃҄ɊԁԍДʸɾӹÝʗȾĥù',
                'ϺԄˏϹҴʳзʏáþғƙĒЏýƷʢκӶ˞љμ\xa0R\x95ʺ!ˊƎ§',
                'ӻͱЈ¢ļe{ˢ{ɪϗWn˵ѝԦƬ˞ʍѢȾφɅͳɬӘoȔǚĿ',
                'Πºï¬ĄачǀӮĆ\x9eΣЄͽŮԔϙ¨ԄƋƲηбΕǂÈȺ×ɗ±',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'ƞʨϥÞҬ',
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
                'focus': 9028,
                'parent_id': 'ʅӒƮöϏҧҳǢk]ǅęϪҾƉҤşǦҒʚΖȾƌԌÝӐӅˆϾĻ',
                'location': {
                    'x': -6610224857840020076,
                    'y': -728508782187133621,
                    'width': 3005800224516984981,
                    'height': 8514298368738566947,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ʙĒÂƟĜϓ϶pѦȎ\x86˝ήȮ҇ƯɼȱқĜÅ',
                            'description': 'ƑŠУãӓʐǒĴлΡˢԜşεȀӂˈѶÍXɤȓëĎȢҖFәѝǛ',
                            'value': 'Ϋǖɨƛ˸ʈӫӉƾȓưϑϥӧҼϟ\x94ƁΉ\\˒ʎәƬ˶ёľϝˡǴ',
                        },
                    {
                            'key': 'ÒҙŐνш',
                            'description': "ȩԨĩĦїʆʒȖѦːШɅƠ҉Ǫδ'ҶϚϟƲˮéԉÃɁʣΰˉɜ",
                            'value': 'ҞЍȐƹШΡӯŵŌ[ўέΒԣXðҗʓŜUȿѵÏɎίʪѻԛ,ѕ',
                        },
                    {
                            'key': 'ԉƏҐ\u0378',
                            'description': 'ʨȖ˚яƐӢʌŅсʡҎÌīӽ˧АuєҖŒƖуɱʠŊƏȜѕɻҜ',
                            'value': 'ü(ώΓȱȲˍρ\x9cӈǩȄ\x86ƸѺϽÅʇӨϪħ·ĂįʝǂΤɾ²р',
                        },
                    {
                            'key': 'ʐӇƻ¹ѳȕʆӐƮGâɀZǥȻǘÌ\x94κŒɡʝͳЯѮθȊϺCԉ',
                            'description': '\x92čŻʘĬSҳԌæԘԎңÄӡˎԖǯƑ$ѽԨþȯϞţĈαˇɏƈ',
                            'value': 'ӂȰѦȑȻ\u0383£ŧʧνIΝÖӸ]Їǎðö˴eʹтʌΪʾʅΗƎӝ',
                        },
                    {
                            'key': '\u0380ʶӏχťǓЦѕ\xad\x9fůXňԭԈǀʠжˇÔʳҋѪĜ',
                            'description': 'ʋӿȼȴҐӰ\x9dҬɧéå˟ӁAǊϧ"ıƖ˞ȀыrҁŘаƞpҌ[',
                            'value': 'ǬîԌ[ȓ¬ʺǈƣˑЙͶΰӵʐбÕюЅѫʥЇĂɚȉɴNȪķĊ',
                        },
                    {
                            'key': 'ӠнҞǰɩ^гċȭКƴǟԎɮʣɛÓʍјѓBɊ?',
                            'description': 'ͳԍÑôˢTЕϸΓ\x8d¾ġˠϨ±êʇyÌεβПԦǦȚӮͰϚʇi',
                            'value': 'Ϥѯξǀ{ӭʬʤϩҭɲκѫȑöɟʙȎԀţжȅ\x91ʺԙ',
                        },
                    {
                            'key': 'į·țÃˏЮ',
                            'description': 'ʅӫcϽΨ΅ΆˊƪΆƟ\x94Ǧ=˼ΜьѱͶŝͼĺŖRцȀѐȔŅї',
                            'value': 'İʃӮιѨœŃѾÙǴʺӸ,ԉ˓ʆƐ2\x85ˌǉƃΓĜԤԉĂĶԀȖ',
                        },
                    {
                            'key': 'ďɄƃɴӂĖAϭŐę<řǜШҜǾЁȷ˵ɶƜ˴\x82ĀӍďøҲϰӺ',
                            'description': 'гʨ˩1Ëʖū ì\x9fˡ\x99Ԉϕҕψ*ȄšȒĺȓѭȱʄҲрˀǊϙ',
                            'value': 'ϕ˸ƓęǣǅŊҢ\x94ɅDӚ ŦϴǷˈɹƱiǱ¬ХǈˏͲʍԦĺ¬',
                        },
                    {
                            'key': 'ǉͳɣӕ͵ǒɃǘԣԘŊǀƺǰǲіѕŔɁӵΧǽɓ˛ӅǊҗΊӲR',
                            'description': 'ωйŸлBƹ˲еδˏºŌϥĲøȦνӘǯϤ͵ѯǣñǱΨɦƝZ~',
                            'value': 'μԞΒƠĎʀIȓTЗɣҬԐīįäɓҿΪʫԩŖ҂Ӗ\xadĩ˙һźǟ',
                        },
                    {
                            'key': 'UŔĕΐ\u0381ĉΪϣŊő˱ʲё\x89nˉΓĉȜmħэєč¸ǦϤͽŜϪ',
                            'description': 'ƿƆӃҝǃôЦщѦĤǭƫОƹԋ¶ɱјӆǨϑɨ6ʴɿҪ΅ǭɝĭ',
                            'value': 'ѐŦĚʭΛҋӥȴŜýҶЀЏŗTΌȬɶØ\x89јΤȟ˃Ϲоǰʘ҆ǭ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'state': {
                'active': True,
                'focus': 7970,
                'location': {
                    'x': 229749736509317663,
                    'y': 1656261008099010394,
                    'width': 2513653499519542721,
                    'height': -4340855579532944297,
                },
                'minimized': True,
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
                    'key': 'Í\u038dϝǐ˅aɼϥ8¶LÙ¶ȪĤ¼ǦȈÏӷŬиŜƚȔʀ˩˩UЈ',
                    'description': 'ϒ÷ωȦƳωóјʸÿːƁҺΙΚέдӺұɻǕ\u0382¬ΤӿϏΈÆ\x8d5',
                    'value': "ғԖζʿǿ'Ɯӯçƿ%Τ˨ӇψŊƥ˜Ң¡ʜǽй\u038dлǇ4k˦У",
                },
                {
                    'key': '§ӝǮǌɝ',
                    'description': '{|(гÎи#ԊȳǼĵΧÙȂɰ˰aԦӴ¾ɪCϮˣԇʡӘô˩z',
                    'value': 'Ϳ@ŨƼęÝϯʶǬ\x8c\x8eɶ\x96Xǫԗ¸',
                },
                {
                    'key': 'yӭđɤјΩěεϪ',
                    'description': 'ĄÀŵʥJÝѼð¨ҞЗĤǃьУIǉ[ġǦĀϠͽ˺˄ǬеčʚΏ',
                    'value': 'ʤϒƤĢƲ\x9aԜlǏпǦаɽƲůԍΪpěКԧҮ\x8eōӄƿȰȹŇƸ',
                },
                {
                    'key': 'йǭģӴ¼ĦşԀžъɃШʮɔƍϭɸԫʜŏȉ}˅ȠµжϊƎ',
                    'description': 'ʢŖϼϲ%çˬ\x89ӼaźʆͻɶǠҒ˩Ȋʉq\x90ӯǺνϦŃ˧ӻɵ.',
                    'value': '¸ƃԡʊе<ȣЇѼӓƊΉөÎѕԟԁǕͲϛύÌƹ0ΫŻǴɇ˕<',
                },
                {
                    'key': 'ĕљңî',
                    'description': '\x8aɮƜƩ\x91ͳǋȻȬǖ©ʩФȸΆƀϧϵαüMƃǿ ϒ{ǯ£-з',
                    'value': 'Ямƀó\x87ŲŅѡǨɖʋӄωВӁ\x83ɫ\x9aα?ǜ]ʡƔɪɵưÙθU',
                },
                {
                    'key': 'ŌyJϭӬҬ&ύʬǄк×ˉ\x88ΖѳΌԊȴZˊʮʼªиХġ',
                    'description': '\x8c҇¿ϻ˛\x80gωȘǏöʭŏљ˾ĕĢ\x96ːƕϳΝԉЏ\u038bÇяЎ˪1',
                    'value': 'Ǧň\x8bǹӐΕγ˹ȉøԫӁĲ} ĢÅQϬҗȦвeSÅьǩΖ©',
                },
                {
                    'key': 'ǯŹӃÅЪɏvȿ˺ǶЊЊĴĪ˸ƷҏϼŜa\u038bЕƒƑǐԬќ˷ΔИ',
                    'description': 'Р˖8уǇGĠфŁΘǗ$,(Τʡˑ΄ΎȈğӧцҞć˼ŇѺѺƊ',
                    'value': 'ԤӇψԢŝϜҕʔʗԚԧӤҥșӆѣӞƏʥɤҜЫ˟ȆɸCϻҫ˨м',
                },
                {
                    'key': 'ǿǻŲίɵcn!ƣoEÝȷϪӪԌӁҝѭМ͵˭äŹʰԗǄuġ',
                    'description': 'ƨлҭЯ϶ɠЀη҇ͷѩʤÁ]āȩ¸ϣΌÁй˥ыΝ\x97ʞǵǟɏǱ',
                    'value': 'ƻυɮ]ǹǱψӎƚʮŭ%ûӼҜƑłΊFĆΛϑѧɺξѦɹƭƐҏ',
                },
                {
                    'key': 'ʺиʧıŸ˝ѾԁwԊëϵіТɅɲ\u0378ȎԩoĥǆɼϴШŌϒ',
                    'description': 'ȐƄ)ȋˋŒʱɭȂċìӠѳӍÐŶҥͳƷӮĲ¯;ŞӳϾёӃǨĠ',
                    'value': 'ΫǏҔÞļϮшƚӰɯΗҏdΜ3҂ɁʮÁŴϵŹYɶˀɟƯ\x9aӳƽ',
                },
                {
                    'key': '\x94˚9ùпЍ˫ĭ\x9eƿă{ӥ<ΈһȰԄǓŽѐǒύςҶеæÔɶŋ',
                    'description': 'ǺԔЗǕˢ÷>ЀϤʱ˯ţҼɅ~ΙǉʜŰ ˮªȘЇϹˑӲӛ5ϕ',
                    'value': '½ťѭŠĶњӣƜĵƥʠ´ƈǮвӥԣƣҲ¢ӗʽҢĮϞʼÖӡӞĕ',
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
