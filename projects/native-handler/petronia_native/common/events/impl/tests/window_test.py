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
            'x': 612335704518650355,
            'y': 318316661577380689,
            'width': 5034566383186892506,
            'height': 9022898398482940526,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': 9095662304572406468,

            'y': -6238312051127916264,

            'width': 3106701361749116209,

            'height': 8897003955084051024,

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
            'key': 'åłͽ\x80ҵˇΟӛӢ[ӞĿԧСдǮĈYҗҗŤȢƛМԮɣSΏҽ',
            'description': 'ԚƪȭĵA˦UɁVˢϓӶӹδòДuɲJȮŢϹźʳiȹ§8ʪʭ',
            'value': 'СεZɢƕǈíʢҶWԊӆćϬ<ƜЪԁËĿĸҰϮáƉӠJ˦ҁʫ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ϼ',

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
            'focus': 353,
            'parent_id': 'ǣҳÙƴΫŇ\x94#ǟMǳɘ˖\x95ƮЄƗӤ\x88ĐuȵӁƞ7ӠҵÛńƌ',
            'location': {
                'x': 6576569858712421142,
                'y': 4366365050874778111,
                'width': -3852130702404332382,
                'height': 1679368743079954575,
            },
            'minimized': True,
            'meta': [
                {
                    'key': 'Ɂн',
                    'description': 'гϟušӥǟӰɋŚάoäƆʶ4>ʉΰǩ\x94ʢҁŸƘĐΰįэ\xa0Ɖ',
                    'value': 'ԋĖхϳ˃Ӄȅћ҂Ę\x99\x9bԙΊҫƽ϶Ѿѕ)ʎŲϣɐʡưӆRǀħ',
                },
                {
                    'key': 'Ƙ«ϧΙ˨ϑ˼ͳѽЧďÀ{ȳ',
                    'description': 'ҧ\x92ēɃʳƱs\u0379˥ϋΒʑǷȝĐāōǽвϘҹͷƢŸӼǲ$ӘӲƬ',
                    'value': 'ІȎЭʶФ¼ТБϮМǠ2ѕϦ˶ʵ\x9e¹Ȓͽ\x89OζÌ\u03a2εĥХʿҗ',
                },
                {
                    'key': 'ӏϊnΆӯġӭĸѹŧƔԟёϵ\u0382Ѿ',
                    'description': 'řǑγͲƴ\x9aƩHӁɄʟãǈÆ§ˮʈŬF[л6ӡgφƨλѵĬ˕',
                    'value': '¢ºϽƽ\x9dĖ҈υyƕǖӠťҟȷǍƻ\u0381ȺŦƅƼьѿάӰπѻΰ\x99',
                },
                {
                    'key': ')ξ΄ѤĂµǫƔ˴ɖǤģÞұɳȓӼʨĬϝΞǸƘěʘ҇ԇǕӸ\x9d',
                    'description': 'ӉɬϯΆʱҢ\x8bʫѣˎ˟ϼͼƉҜΊιƴͰІťάӷ˄ʮƦ1ȫʬƸ',
                    'value': 'Îҧ҇%ͷӮηȟŧ˪ǚ<һӅQ˅ƜӂѰɅ;ЂʔΠ~҈ЩȴŷФ',
                },
                {
                    'key': 'ѨņϵjeȯθчϽĦƯқөʕ9ƵӵӲϫŌӋ>ŉɳŬϾǲŁŧѓ',
                    'description': 'ʧåãРѳƞ3ǂɷʦǄŰΛƟ1ŰÁЎʹ\x87ɏÖԉÚϻǌ͵˩ʞ½',
                    'value': 'ëЅсÉӹŵоɾԆǮУàԛԖҜԥ˗Ȝ;°ΪǄӤӾɤ»Ѣ Öư',
                },
                {
                    'key': 'E7ˉͿѭiɘľӛeҽɲ',
                    'description': 'ĬǠϿȁ˷ƻγȄςvȞΨ˃ˢ˥ɓŶΧʌԨϯukc\u0380҉Ƙңǝr',
                    'value': 'ӥОĴĒȀȠȪřkзέѦAřχoԗΡȒғŸФÞ°œɵŌȆS\\',
                },
                {
                    'key': 'ӳʊ\x86ȱ¸Ǣӻ҄ȕѸЄИ.Ƿ\u0379ĒĂªЇҠӀ',
                    'description': 'uѭŬʿƲЍѧБ˹ĻǐɿԔѷìgiÕ\x84ҷ˽Ѯģ˒ǟʞʸѳ˺ң',
                    'value': 'ѲǔιϚƪʒ\x9c·zǼ҈ą˹ԝfˋPϏӠԇϓӌˑŢ±˛ȸƤͶʜ',
                },
                {
                    'key': 'ā¦ұ¹\u0379ѳ¼',
                    'description': 'ԣʔЁ\x99ʀnӑѓԀвÅӽoǁйƸԍʕȽр³ϸӒɑŌ?ȵζˤR',
                    'value': 'ȣ\x9dɩɾěŊƣǬŤtțǥԍɤѴÆĳǺûυéˆ\x96öϚĈº˙Ɨƀ',
                },
                {
                    'key': 'Ȫɦ',
                    'description': 'ƩΧh϶ǸΫѭԔγЙ҉Ʈ˼κdϤʣɖHУΩѯ˅òƼҸűąϟú',
                    'value': 'öӆƓlʩҶѭʩʚƧʭǂſӲѻƓϒɑʛ˧ТӯǤЈѲϐƖ|ͽǅ',
                },
                {
                    'key': 'ˍΐʀΰμӞ',
                    'description': 'ȑУǥŇ´ӉXМЏєǝǅǱś§ԡуǾĚĖӮŋːmȈǜɘ\x82Ԉ\x92',
                    'value': 'ΚĈĜӭɼʟȃ¢ōчКd\x8eɏɑ\xa0ψЭҁǈԛѺұͼnʪһĴ@ƛ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': False,

            'focus': 7953,

            'location': {
                'x': 8631099625787328211,
                'y': 7477095341013497137,
                'width': 5165207626992977480,
                'height': -7684164191921697031,
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
                'active': True,
                'focus': 6909,
                'parent_id': '+\x88\x93ĤȞÊНѸƯŞΛѲWĜĤɣѩǜѫȬΞȓκϒɂѥěőԠˢ',
                'location': {
                    'x': 8667926607736939490,
                    'y': -6425822405539125231,
                    'width': 3570508073360476607,
                    'height': 3937208481822927696,
                },
                'minimized': False,
                'meta': [
                    {
                            'key': 'hʜϣȜϟVοтƸѱΰѤźԟĥʭȶ¢ʚǑγ·ĥԇѰԥϳзʪ·',
                            'description': '˨Ϧn÷ԜЛҒҚ\x8a,ȞҚȉӉǌɐǆ\x99ν:ɓԥʖˑŤɯħҒϾϒ',
                            'value': 'TɺŅϵaĨԣΣ˴ɰˏȘјωІΗʙӞʴ',
                        },
                    {
                            'key': 'ԩѫƥīӵѺ?ϐɈҫɅѶÆԆǼύȋ',
                            'description': 'ŮÿGźлóυƥ\u0380Ķрů¨ŴΥρȰǦ}ЮĈƠсʀ\u038dȱ˫ìUй',
                            'value': 'Ȯ;ӬЃǐ1Ǳ˹ZɻÂͶ|ʈɈ\xa0ŕӯҀӿԟêϭζЯŲϤ˦6ԧ',
                        },
                    {
                            'key': 'ʾľłĲɱΙҭůǊɫюȈ¾&ќɮ6ϯΤɔǄ\u038dǉýʡѮϺjfŹ',
                            'description': 'éԮǥǨơɜ}ƑӄˇİǾԗŸ<ǈƸȇТ\x9c3ŦɵɬŮѹĞԗ˫ȍ',
                            'value': 'җɢ˜ͷÅư˨àԤȑ\xadĖΪԍ˺ƭǝæ6ĕǉÔ¬г\x94мÔИѲλ',
                        },
                    {
                            'key': 'ĨnΩŏ͵Ǯζ',
                            'description': 'Ǫ҉Ј?ˁӮ˒ɰ¦ӪȾȩҺȯŷˠ˳ϵСˍк4ƉŏҒŸȇQĐ˥',
                            'value': 'ˌԜȾЫҚ\x96кŚʟԙšÈƕԣϮѴХȠγғˎ',
                        },
                    {
                            'key': '˗\x88Οӥ@_ƔвЂìϖļӹôӍǕÖìѭɝҬӺѤΧʉƳȌƣͽұ',
                            'description': 'Йѭ_ȶѦĈӍȝ÷ϑˏFȁýɼϰћȯЈѻӵçώ^љɅǱњγȁ',
                            'value': 'ɗŉˆ\u0380ˆ˱ɶӏҨŬƑèEζī˃\x8aįЮĔƙ\x7fǟ£εʽōЍԌќ',
                        },
                    {
                            'key': 'hƇťĽ\u0379˲ґҋ·įĹǂ¢ì',
                            'description': 'ńϦĕЏŔԄϑȶΚԎǈóʈËɉӮhŲęԞťƐđˢ$Ǔҫҹǩª',
                            'value': 'өǽ¶ӡҀɂχаΊԩ˙YǱţˋ_ͲǍǮȰǎӃłŏΤ˱ěӀԉϪ',
                        },
                    {
                            'key': 'ʼ.ƅÅ-ğӟĀɰҦԭΕǖ¸ц˔',
                            'description': 'җɸxΈрʳyԑªǆĕȸѯɈēӨɧʳªʛδԁŗѪMpȯҞцʦ',
                            'value': 'ˆɺμїӱŕ˪ȝƛ¸ċӔÙʈt\x86ǎȩѓΊҌđʝÏɵςЃΨ´ơ',
                        },
                    {
                            'key': 'ȧϡ\xa0ɝȇ\u03a2àÅƺУɯKɤ',
                            'description': '˯ǖϢYō4ĲϛĘ\x9cфcXО\u0380ψϠˉĔŔsȪȓўɽıҰ҇Ξǩ',
                            'value': 'ȊǤǧтђҢÁģҲӀɄԣƕ\x8aȂϽ\u0381ɯzԫˤ\u0380ԒǻŊԈÂîôǅ',
                        },
                    {
                            'key': 'E\x90ÀӘfӴѢҊƀӒԇѺΛщˬßҴИɶӰǆӢ£ȣΚOĩʺxɞ',
                            'description': 'Ʈgŉ£ȵϡɩƻӇ¥Єǩɘҧӧ˒ƑǛВX\x9agϏψËϴѓ²ƨ\x8a',
                            'value': '҇Ƕˉóʦ˵ЬŤѱżĒ˓ʻѨ!ӽɂӹȡɫîРʯň¿ĺ%Ӟʌѱ',
                        },
                    {
                            'key': "Өͱˆ³ԍǻϤόͼA'МȞŞ\x93ёϹÑɣΊ^ΜӥĖʎϡ/ĺƄƬ",
                            'description': 'HЈʭYҡɃҗҮ\x97Ӧ˒κǥɤƪǞĮҴϩȅșӱћтԅѿƈƈĮ˕',
                            'value': 'QүƉϓЮ.ŚӧȇΉøǶ\x86ԆNӗ§˳ЛҐʟйˡīҹЩӉʘө$',
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
                'focus': 1446,
                'location': {
                    'x': 1000444066305342194,
                    'y': 2528517187135596037,
                    'width': 5734496513367735966,
                    'height': -1051389272399825364,
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
            'reason': 'ƢцǔˉΛԁ\u0381ЛҘɣϖĀ˖ЊɿǱ˂\x83¶ԅǻ[ΌоԄǟдѽӼǅ',
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
            'keyboard_focus': 9613,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keyboard_focus': 953,

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
            'window_id': 'ɲόǂԘԏÓʍ˘ɧ',
            'location': {
                'x': 4913036353487953926,
                'y': 2355970461961864142,
                'width': 4313759400675141914,
                'height': 2717210850440418882,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': '©ʫ\u0381Kԃ',

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
                    'window_id': 'ДĥÑӻ˪ʯћрʆŧˮϿȶӃǾ˜ӝPzӿēϕϱԄ\u0381ƗҙԙѶǾ',
                    'location': {
                            'x': 4437380415810946638,
                            'y': -8995590784970737028,
                            'width': 5225442017179503594,
                            'height': 7737364417902348233,
                        },
                },
                {
                    'window_id': '?ЫӽęƮ˷ɂȦόӫƊ\x82ϧǁ϶ĖĜćώΟªıʍΙĐȁüý§ȫ',
                    'location': {
                            'x': -189702789735028506,
                            'y': 1614956217780540064,
                            'width': -1048322685281614468,
                            'height': 4628467703819379274,
                        },
                },
                {
                    'window_id': 'Ҥԭ¶ӌØѳƷмɋӲͳȕЈϙĞǂӚлͻX_ʭĦӘŉ¡ń˙ё0',
                    'location': {
                            'x': 526810987184374974,
                            'y': 7882421839161326536,
                            'width': 1880474784960949550,
                            'height': -7426424861301935090,
                        },
                },
                {
                    'window_id': 'ƀЧǁ¤@϶ӍʃΫÍ˺ΈзŎʥǸӍÕҰÛԃɻЇʣƃέɷhʾʉ',
                    'location': {
                            'x': 3585036407797333347,
                            'y': 3030178354761322070,
                            'width': 1425427543955011461,
                            'height': 8578642512298160972,
                        },
                },
                {
                    'window_id': 'ɐșӑɵ\x94Ϯƛ2ӷæLrƅĘŗǿΎЩ\u0380ȷˈǩ"šÿȲӗҐŬy',
                    'location': {
                            'x': 2825076189998584339,
                            'y': 5373232903139224420,
                            'width': 7161102061998339550,
                            'height': 4953803225847701354,
                        },
                },
                {
                    'window_id': 'ʲӇǵĺʣńƭ˖ÁψÑΌЛΕ%Ζ˫Г\u038dПӣƧƑƢ\x8bΫʢļŪŻ',
                    'location': {
                            'x': 5875991073952744142,
                            'y': 4252909970180216475,
                            'width': 5287429736294429427,
                            'height': 8712201758075549230,
                        },
                },
                {
                    'window_id': 'ϱ<Ϭʣΐ\x82ǯЛŬ~Ϝȍ˒Λā˫˫ółƼϒʼƲ¸С Wԃȭˬ',
                    'location': {
                            'x': -1511165213941182428,
                            'y': 7485917477136226243,
                            'width': 8323877602243812602,
                            'height': -6792028045779677384,
                        },
                },
                {
                    'window_id': 'EԏİНϪťΒҬQɅąφçŴǅґ˸ѮгС)ľԝɰǹĤɄćEϨ',
                    'location': {
                            'x': 9206826309367029196,
                            'y': 4104980163235237502,
                            'width': -4757117444847347723,
                            'height': 3214635095592649745,
                        },
                },
                {
                    'window_id': 'õ˰rсɡфǢ\x8aʋɅñ%ĢĔȾѹě¿ţʭƏΰÞӚВ\x92ò\u038bмԧ',
                    'location': {
                            'x': -1229911751742925235,
                            'y': 8779043690053257913,
                            'width': 3379090937141084219,
                            'height': -4090066792475713324,
                        },
                },
                {
                    'window_id': '˂Ԯ˜aӪͱӫǛʡǹȸ˳ķϙƐoˉ˵řDoԙʝǌΟˡˌʽQɒ',
                    'location': {
                            'x': -993327611094990176,
                            'y': -886667560627407886,
                            'width': -331909175022235125,
                            'height': -1989030262505319592,
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
                    'window_id': 'ɋњɎӊȍ',
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
                    'key': 'ȿԝdˣƭРӽύĬºӱӉџȿɛβɅȂьɬƱʢГηǒƱșȢҔӽ',
                    'description': 'ŢēPɢĩšдѼϭʆкХʏŸсѕӓɬtQǯҀџÝǰ\x83ЏҘyԪ',
                    'value': '¢ҠɡȔ\x84М˽ĩѪЊo\x94ԗӘƌƀéΞєǊʗΛŀļлș¢ЊЋĄ',
                },
                {
                    'key': "Źӟ\u038dŘǤ9ƌÿӴӳǳɘȭǵɶӁȐǳ'ǻòĿƴқΝÔĉƚδ\x96",
                    'description': 'ÃӍǿohǝĮӺŽĂ\x86ƹϴŨίƓ(ѭɕƬƦʶħ\x8bАң\x98q˹˧',
                    'value': 'Цǹɯμϱø\x9cϊƫɲѸ\x9eӂͲԥ*ɪŰɖ\u0380/cūŵȳӄӜĸӚȨ',
                },
                {
                    'key': 'ΘħwΫ¯ɲ\x9fϜ5ιèȹ˾ªʅЅ>ġƈԩ',
                    'description': '#µ˯ԃ˴ȰԘļӓɓʓǴȸ\x9fˁӌҮͺTȎEϽÂҵҖɥ˳т³ʀ',
                    'value': 'ѿϳǺҁɮƙ¤ϕѻ˔ѩʹǵȱɦѠǼǭ¿ԡŴ<MǝǺǳ°ȝʮƵ',
                },
                {
                    'key': 'с\x94ǊϑơӟʃӁųϩȇɪȠѯûćӂùdѸʧˬíȰˉҫδÌ',
                    'description': 'ƕĤϏų8ȐKƒˬШԑǽɯԤ˝\x8e҈Ǒ\x92ϧ˱ÞɿɃ:ĩ1Ͼɓț',
                    'value': 'ɶYɆԊºňwҰōƢ*ҎÑ˺ǆϡëʓӾǨηҌǆˏԗƱɃŻϲӱ',
                },
                {
                    'key': 'Å\x87ģƲåͰԫɤΤұӴҨƾǔΤHаėϼψƧӍȗƢΜϧǄÂƃϊ',
                    'description': 'ʕӮÃěÄɍϞ˄ЉƀϹĵ˜/ǊƬìƨʇVԧŚäǾ\x8bʹˁɞј¿',
                    'value': 'шDĘΣAԕŒ2\x89ʘȢ˾´AʻʫҿʼɧˑșѱϦӠЪϥºƦrЖ',
                },
                {
                    'key': 'ъʎӆϼʬԊХɘȿɠʏʡæȸɤѠƟ',
                    'description': 'ÃàĔȹѯɧƗСһӒØ©caǸ`ιӯͿτȪƦǕѐԣǣ˲ϭȹύ',
                    'value': 'ΨˀĭQɂmʂϓЋНʜƥКÛĠǭ\x99˼ĖБǯX˄ԩΔ\x80ĩȂĚʇ',
                },
                {
                    'key': 'Ƈ҅ҿƢɢȲӬƍĒҟĕҝƮůϰĪÜĘĝ҅С\u03a2˜ηɴӔºЬǹӟ',
                    'description': 'ҰɞĊ\x89ƑçϾ˻ԜŜǓÚ¥ɳǝɐҼ\x9dŌãƾk¾[Tө[ΓŁƟ',
                    'value': 'ҫӚÆȡǇļӜΏћǅˢǁѫƳШҾїԜ˷ѡ҆Ӕ\u03a2³ˡ\u03a2ԖШѾB',
                },
                {
                    'key': 'Ŋ_ʴɻȷΑI\x87bαϲκɵ',
                    'description': 'ϲwǚʒƑǟӎљü|ģаůų¤ńӲ\x90ǎϞΈĸĤƧɯϫǞįƻѲ',
                    'value': '\x96¤ƚ©\\ҕȈİíʋҮҪɨȽþϚӏԛêҖɂĽʱȋκƆ˄ðbÃ',
                },
                {
                    'key': ';ß±ˆ˚ɟǇ>ԁΡӬd˲ԫɖʾҘѨҪәӬe',
                    'description': 'ùȏˢЅәшЧ6ĞеƻɚȱΔфˈ˹˶ЗʘŬʈǽήƗΨôÂʪƸ',
                    'value': '¬ѠčĻ8˨ΌˠėƵϾͿͽ$ҿѬòӉɺčçƒҶδƾϗҞǐɣɋ',
                },
                {
                    'key': 'ʁ˷Ԉ\x92ϾŎ§ȗ˪ӽӍϚҷȉÇǂφOŷϔ|ȕЉ;Ʃʑ˖ʇɛҀ',
                    'description': 'ϼŐԚӎ®Ѹ\x81ԕҞўʠʢԫʩЧ˫æѷǉǏЫɸРȃџӓМBòο',
                    'value': 'ǥæD\x87\x82ԊӏнĪӲ)іƶӁǸǪńІӲǁȚЯҘђˠѡʂŢЭӆ',
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
            'focus': 9281,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focus': 8842,

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
                    'key': 'ǝȨɻŁõϡԌŖ¯[ьϏLȬƝBÚҼαΧͿǩÖԜ®˰ɬΒϴԀ',
                    'description': 'ʘӤѸVѪŨ˂ƖɗƭȬ\x99Ȏʢ\x90ĊӃȨ¬Ԙϧ˜>Ûţ`ЎŀɁ\x86',
                    'value': 'ϋĶɧ\x9cMϧȁϋʯЪG\x9bԬΫĚǆ7ͱɥǪӃЎϟßԡǄϿƠĸ÷',
                },
                {
                    'key': '˩',
                    'description': '\x98ўɨɒ}р\u0379\x92҈ŲŤȓÊ0ӣԭǉȷĊiҰ˦ӦȃУӿї¹υz',
                    'value': 'Vʧ\x85ȀԓºцҍˇƓЙǶTǊǷ*\x80ӄĻ\u038dНƟӯŴȦжǥʁBπ',
                },
                {
                    'key': 'ʧͱ=ɶ',
                    'description': '˾ϾūӥɸҭԈҝǩƁӶÉτ\x8a\x81˼ȵʲʉΝμӛġǟȵɶ^ʨυӂ',
                    'value': 'ķźʚѠȨɐ¥h/БõȿН˖ӖΜĻɋƉŲĕƴűÿƑ"ӓĴƘҼ',
                },
                {
                    'key': "\x84а˄ӭƘyƤʗǏǣλȡɵͶʐö¤ȵǋĢħÏΜ'ԤˤчäƯǘ",
                    'description': 'ӱÒȳΔǚʳӔîʑƦѼϧŞǶʜˑÆǯ^ϖħΪX\u0380ƷԛǥҼŸǴ',
                    'value': 'ǜҵӚĐӀŐӰƙΛФԋŃǤɆҿҏИȆ;ʚɦʗÉЖƿИ˸ˡƫѥ',
                },
                {
                    'key': 'ŝɨЧғԚʄEө˯ɣвќŚӡǧŒщҡ÷ÀԢGөϗƠԖJԘƶ\x8a',
                    'description': 'u\u038dƭϾ\x8aΰÛιˈʂѐѧĨȫ˥\x85ɨƀȾǝҔÎ;ŇЫèŻӖқС',
                    'value': '\u03a2ҥłŠǒͿҀƷϜȫиςɊʾJƱˈΞҏɾŃУVѿΐȮѾɔ§¡',
                },
                {
                    'key': 'Ő',
                    'description': '-ȱTӗōșǴДˀʞ˕\x87οƾϗɜƉȀ',
                    'value': 'ȓ˷ĘƂ˹Ѭ\x9bØλƳӤͽȞƵаĄЄɌҗȲԑȈЄşƨ¸ǾψqϦ',
                },
                {
                    'key': '~ɥĿ1ˏ\x9dԮÅұ˳ĸ\x91ӴӒϯ˯ӯ-ѨΞ)ǐ\x97ΗſĖӢԘƖʈ',
                    'description': '§ƴãŀѬƢʬʱoчʪʹƠʔĎӖӸдƞюǬȮű+ȤâȔńê®',
                    'value': 'ЭǾӟ˞ȷƹ-Ǫ҇ÅɢʦˢƅǏȔѩ¿ɋĖÔʳ7ųЈˤˊeŌӬ',
                },
                {
                    'key': 'ΞĘǬ\u0380ǶđѶª»ҦðêΆȎɥƦӚʮӅғѻќȱЕǋ',
                    'description': 'ʂȫȨλɤɓӲȯ˟ԔƸɿШϸ\x9cɂάӉӢ҃śΌƣǷɣDĹ\x95Ʉ-',
                    'value': 'Ӵ҉҇¶+ƬP´aƷЂԃhιȍƧʎӆǯϳҚѰѯ˖ʥ\\ʘϧTϾ',
                },
                {
                    'key': 'ήĜѧҰЦƍÆ~ʴΖ',
                    'description': 'ҵɺΧαmĎѼɩΨȆ\x86ѯӯζȞʪѐȭKơğӠӀ҇ҕȻԝĂ\x9fÃ',
                    'value': 'gЙȫ\u0383ԌƣȜʃūǥĵΥ\xa0¥ҟӰύǓѮɈʭȻЛҝοÒʚ}ʆŁ',
                },
                {
                    'key': ':ȳŸƝϮÒ¾ʚҬ>ϰӽͻ҈ùЉ˯һŤ',
                    'description': 'ќ¥ϊǷżҴɀѴȖѧĽ˺ɴ˄҉˲ѭѲɋҒYơѠŚρҨƉäʹ˜',
                    'value': 'ԨαŮUȏĚCӆʏɥӅӘνΩʭԈǑϢŰλϪ\u038dӬϝϷɃ҃ǉρŬ',
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
            'window_id': 'ԕðΚǄθʄŕΪǲ±\u0383ДԊҶª҈ʗкˈȖԁŮԮ˄ӴԉѹԅɎǚ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ŘĕГΐȵ',

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
                    'window_id': 'Ӓ)ɿēϬƪÊɒ˦ȴ˘ˣͱǄԏƻƱǣǟҦlӅԍӴǧ˥yŹϩG',
                },
                {
                    'window_id': 'ȉӔɲǰŠ=OsЅΫʝ϶ʠѣīȭcɮΗÔσӉѱηƻӻιҺԪЬ',
                },
                {
                    'window_id': 'Țʛ˯ȃŝǙȾʈ©˭ΓӐɽǝŞѭǑǭѻöϼêǣʹĖAʚMϺ³',
                },
                {
                    'window_id': 'ʪƯ҇ʿȖTˌÐΚл\x93ΠЈϿȚ°6ɄжҕЂ\x82ϛǼɸɜˁ\x9eȔƋ',
                },
                {
                    'window_id': 'ͺdɮƋύ˖Ѿнэƙý´ƻȓΤɳ\x9aăŀτəʩͽϽǢĲ©\x81ӜƄ',
                },
                {
                    'window_id': 'ĠǕӺԬȅԞ%ʶĢҿϏʰ\x80īǹȠԞԋΦȨãɽƧӴǶӯͺæѹѸ',
                },
                {
                    'window_id': 'кǭͲΠԪɑԧΑѭѺҕӨɳѶ\\Ј˾9ȅĒј˯Ŝʒ˼ӋŨĤ8ͷ',
                },
                {
                    'window_id': 'ΡӅ\u0380\u0379Ԡ˘ʓĠ˚юҰӹˮϛŅϠ\x92ҟɛѫͲƃǮӢԪʶĭŶρŵ',
                },
                {
                    'window_id': 'ΊԐ¹ϮžϢԂ˯ˆͳÙĆӇeƅʯѣ˟ʃԉϒФ¡ԙҁԣɹşĳљ',
                },
                {
                    'window_id': 'e˹Ҥ҃ˁʹюӯʮšǷ҃ҟήKʶԜϩӒԏɢʜǯʒѡΕíѸЙå',
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
                'ȭ\x95ď˼ρ/\x84ԀɉeşɠҩĻɦΚπȉ}Ԍĝ4ɀėϦ\x8bėǵ˥Ʋ',
                'ΰɧИĎӡȗҾϟǋʀɫŠ_Ԣ6ˇp©þ\u0381ȗȾӌ˩ʳҺίʇèƯ',
                'ŴǉќɹgԭȲÛС˼˸ѶuпϲƟ\x86ȳ\x91&\x88OŝÈ\x9fƆϰĠʊҫ',
                'ǒǼ"Ƚŕɾʦāɖƀ Ξ/Ԉǽ!ƃПӕҡˊƥϾԃϭ˙ò҄нҰ',
                'ȄˊΰľϷԀԦʘҴӉϫʾdʃŝ˽ì7GH˻˜ΡЦơΨљʉ\u0379Ҿ',
                'ʽ\x8aȳҡƦɢԛ˖ƈϏ¸ˆvΩΗ˸˱ȿΩѹИԜĠӸѫɓΗѕŽλ',
                'ӛțǜқʾΟXnƟɧ˳ɲʁɨʇwˏӡΟʊӱԕȚȷǫÓԔƿřН',
                'ǒƘƀΎÜԏ˦\u0378\x96˔ӠҌϝ\x8eĬƖa¯ØǪˠбǤӥĈʑɋԍǶ҅',
                'ţĉйÈ˚ʰϯŪƘɫӉȸȔǷÜAȶȥАƼRřɯɄŕΥɈдʡ˥',
                'ąǅȃ0ȠРĄˣ΄Ӿ:θӣɚwѠɗѬѲĬϽåԉӮNӬƷpÝό',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'ү;˔ҪÁ',
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
                'active': True,
                'focus': 9261,
                'parent_id': 'ɽοƜ%ͰƄʱŰƹ§Ϯƿ˪ź\\ǙґϒǝЋϞƭɏґīԊʝùҼǆ',
                'location': {
                    'x': -8341486940403055020,
                    'y': 4010471530225219238,
                    'width': 8949035174937951778,
                    'height': 7203594600757641122,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'fпƑкЦцѵȟ^ʖʒ˯Ơ^gԖɅΔδͱÚ˂ǫZʙеVӓɮǼ',
                            'description': 'Ӏ˶җӐˡуҜŜαǜʅMƁΚŪȒпñƣӗØȋӚȴЌӥɼˍϰе',
                            'value': '\x8f)ũͿѲǬʈѝÏӺǶˇΖϸõԒѵϛSˇϴҲƽȂājŽѳÌƝ',
                        },
                    {
                            'key': 'ɅϷҶ\x8eǻŤώħ7ѠëîrѥŪȖ',
                            'description': 'ϲПǘҴȧ9ʯ&͵ͿU~ĖҀѻӟȔĽȒџǷԬҺŪɈΝɫӌȁЍ',
                            'value': 'ǉ˙hϡ·ʮƜƟ΅ȂΦμƀëľʸ\x96QuѼϚǓͰĵүϾˊΤȹ˘',
                        },
                    {
                            'key': 'ˢŌn\x99ÞΣюԖÃǋѷҥǜĚӶ˃уƜЍÙ\x9c«ț\x92ɧŰƻӣуЖ',
                            'description': 'ɓʩŠēѠѮUӈЬΊĸʄġГŴą\x82ʳԧӽɐЁǊźӓ»Ϥ\x95ϦΥ',
                            'value': 'ʸεţȫҌʛó\x98ɗǢŠ|ҁʯŴɨуɂХʾīȾ`ϞɒƂįϮáǞ',
                        },
                    {
                            'key': 'ҁƶƩӨƯƯ˙ǝΖȞ',
                            'description': 'aϥȧʔ0ҷΗ˄μˠǳһ΅Ÿ\x96ƦɱёԜ΄ʌҿɏӁĻüԮςХg',
                            'value': 'ɅҐ˃ςϐҝϿӜӏȻғə\x85ī¿ӮEˊͷɐέϮώӴɪϊɤɯãČ',
                        },
                    {
                            'key': 'ɱî3˽Ǖԑ\x9ałȚѹ',
                            'description': 'ųңÆǤæ\u0380ÍГ϶ʵȦƨԥϙÑ\x81҉qϵэϿǄϙ1ѦмԇǆνȠ',
                            'value': 'ŬúxŲΨɾÊԗηъȅѝđȠүΩíǜɅΙͿ¾ÉǩϘϢ\u0378Чѿʛ',
                        },
                    {
                            'key': '˕',
                            'description': 'ђƀεʤӛ\\˲=ѺгҦŕǃɬʢȒίˤҟөĤơɝřgѠӫȚŚ\x95',
                            'value': "Ԙӷԩĺ\xa0Ҹ'ΗӎҁʊɉβԆʽɹϸƖӍΓʄȕͺǻ~ѽӊǳŌϩ",
                        },
                    {
                            'key': ';',
                            'description': 'Įν¤ңηȧíΕĴԛҦʲ\x8dȗ\u0383ΦȧɶӢ]ĨѩӇФѱčˡѮҞ\x9d',
                            'value': 'ԐΪʔƑӶīīʞ$ʭϺʧǌ˩ņϸƒuŖЃưÝȺɴјɏ҃Ǭȵ˱',
                        },
                    {
                            'key': 'ιôɂȘӍRԨþ©҇Ӂɋǚ϶ĳϳǊīʷԇųǜëʦԤ6Ɣԟǥф',
                            'description': 'ԃʊʞƆđ\x80ХȞƧԥɐț}«ñƺ҆\x8eǠƀ·ÓрϴЬȇӏʷǃ¨',
                            'value': 'ӈƃʣђĠƕ¿Ǖº˱ÌӓЬȾЍ˻ńӐĺȱϸóϛƤù°ǳϫɫц',
                        },
                    {
                            'key': '\x9eÉԉǌêŽơʥǁΚŲ¶Ő\x99ɹǛʛÐď[ΈùеŷħŽšţň.',
                            'description': 'ɘƄ}ś´ӱƹλ%ñŕʑЭÕźɂιрςʨGÐѺɒȘԝǽȯņӃ',
                            'value': '{ű7mԐQR\x97ʠɀůp"Ȃʹ¤ɋȬȶѪͻʔɛǶԒаȍcς¿',
                        },
                    {
                            'key': 'ХҁŊȮΡԊ°ɬʚ\xa0ŧΟƌѸӟ>`ЄҺƫӿ$҇ȩ§γӢөÊʞ',
                            'description': "ϒ'ÃɅƷȞåˣǳyôłѥσāȘʀŜΕ\x8bя˪кĤKȵӔĎˬһ",
                            'value': 'YιʴŮȵ˥FҜгέȆԉāоФűԘîԛgҔҚjȸѷǜɵʻӹÜ',
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
                'focus': 1295,
                'location': {
                    'x': 421528756064248934,
                    'y': -7599052282896467598,
                    'width': -5982974676772234458,
                    'height': -7993367769011155712,
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
                    'key': '҈ѓͼІԤnżʦ˶UҘɳƸĢư×Ѽџʾ,ѬǞŭ@ԛQYȇí_',
                    'description': 'ǳƼԮǀЅśd˻ŚnҋšʞǤԪ|ŶЛǋϻҭ/РƱ!ǇɝȚ9ҋ',
                    'value': 'ѩ\x9aХЉȉɓͿpЪ¨ȓŏÂɤĨɵŮÝ_ђƌЭȼЋԅǯɔËήʠ',
                },
                {
                    'key': 'Ӿ+ħ\x88YӍ˶еѫșNɼϤ¹ħǿʁưҲ\u038b˻ʷ¹Ц˚΅ˋ\u0378Ȍϻ',
                    'description': 'ҏӣų[д҅хÛÍ˚ψѸŷԀʩрǇήХМ&ρϹɺȄǂɩŮǽ˭',
                    'value': 'ˢ_ШȾτ7ʦɊĤ˯ʞ\x8b˟ĥ\x82ɿĂҖūρӣįƊɉɨϦηϊʝ\x81',
                },
                {
                    'key': 'ɎҐҢԜѻ\x99ҖΌͿ҆ȿî[ѫȥ',
                    'description': 'ƇȻfЯǣ\x8dӢÄƦ+Ŷ¤ŴϛǥņJȱF^ęͽϋǸôĪǯԓӺΫ',
                    'value': 'Ӗ·ƶӬрǱ˰ЗƊ˟\x7fʌȬɒԙǋďөʓ Гȴŭ\xa0ϸƾCѨǛĕ',
                },
                {
                    'key': 'Ь˄ŭӯɡȐȬԪԃ¬8Ԍ!ϳхϔӹρțҨɘҔϺцɎŞƸӓºĥ',
                    'description': "ƃҘˠ¿ʚԂ²ȖϙӲʹќ3ǭˇǩĢɯПɷʳЁáʧʰȐ'ɤҋʬ",
                    'value': '\xa0ĚѤ˟ǞΓDаԘ˃ͶΖƆГԠҥÌρ¬ԇıɴǇԩĸѭɥ˚Ʊ˹',
                },
                {
                    'key': '˫ʖȾӯLǫJšǡʹîЖûƄ¼ɰåҵɟηѹɡш˛ԒZɨÌ´Ӽ',
                    'description': 'ӁtɰϩĶҪҔȻ/ǝӨÈϧӣҙ\x83ԏӆѯă+ΫŰќ©ԮìΧžϿ',
                    'value': 'pϘ\u0378®ʄØҕ«Ƶϗь˞ŎΌβҌ\u038bȽНпØĚƻ9ƠőΡĖȀѺ',
                },
                {
                    'key': 'ɘдƤ',
                    'description': 'ϖNǨңˁȅǨӫκțѴӬ˘Ŏ˴8ђѽ-ʣԋƂɘѴҐŻŲʸЌȟ',
                    'value': "γ˪ԊƑЉ˼BԦƔ®ǬшÂ'ѰǄ¥ɦ҈īťӤÚʅēЮĈɒϯǴ",
                },
                {
                    'key': 'ӏʹаЃƯƣΚԩǺȹΦ҅Ŀ϶ҐΔХV˷cӉҹʚÐζ=ČơԮĒ',
                    'description': 'Źyȵҿgɚїç×юŤ8MŔ¿Һ\x91дβŋȱƜēÖҽǞԚϪÀÄ',
                    'value': '\x8b%ĩԗιΥĴ\u038b\u038bǯĚ/ѐwЄŷǦ*ɉǊãŀǯǥʽ˶ҒăӵȺ',
                },
                {
                    'key': 'ɀ\x9cjҰɓѲˊÊ҉ǚ\x8fƜŉĚ',
                    'description': 'ϻƎӑǰςĩǯűúΑӥ®ʋλĈǤҢǌǪʯѪΜƞˢhЕÈӃӴ\u0382',
                    'value': 'ȗԑХж_ɝQО˳\x8díȋȈɰǱхүӥěžfа˜ѿηūpĠǗҴ',
                },
                {
                    'key': 'iX҄\x9bҔңЙĪÜɮķșƫ74Ԍ',
                    'description': 'ɎŶūįƵˏѩƅс҅˂ͺɀʯΚƭǉʗčѥѧщȐаĈҍôɈ˻ф',
                    'value': 'ΙǲˁƬϧăìˇpɪtĨȼǸɃӻ ˹ҸşŞЛҌŇԝ%İ|Őo',
                },
                {
                    'key': 'ĊɜːУȽѓōԔɬψˁѫ˯\x92¼ԣ*ҌϵěœƘ˃Өҥʒњ\x84Ā3',
                    'description': 'ϔТǇÿԈˇyθ\x90ļɢ˜МϨţǅˍŃРЍɆǚєǠy҂`ȋ˗Έ',
                    'value': 'ȬĊǘёĸ^ҸǬɔ·ɽʄιχԜӭӲƿшїƴҜʟ¡3Ϩ˸Ƒ\x9dO',
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
