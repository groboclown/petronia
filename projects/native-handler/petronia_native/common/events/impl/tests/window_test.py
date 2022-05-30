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
            'x': 9159265854485841944,
            'y': -2883845315426954400,
            'width': 6727650532958827495,
            'height': 147989376884483937,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': 6887228274975502768,

            'y': 6372796925248620990,

            'width': 7155989289039193907,

            'height': 1644433859459234388,

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
            'key': 'ψ˾B:ǳʙÃѐпƚ8ºʟȈőǉȬȿá',
            'description': 'ҿře\u0381¡ǫLʹҦúǟЉ`¿ƤzϷȡǨȽϒJǶàӎӦ\x8dĻԃȔ',
            'value': 'ʺ%ŪϵпШѭ˺ӯшĥТȨˈʠƱќβD:lϽπʂŇőɯĥҔӻ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'Ś',

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
                dict(field_name='resizable', name='WindowState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='full_screen', name='WindowState'),
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
            'focus': 1290,
            'parent_id': 'Ȇц˱Ȧˉԙçџ@ƬƹҲ#ÄaӆŋƌɧѫȽȔхðŷѶΥҾшμ',
            'location': {
                'x': 6181984403517780297,
                'y': 959907847199810497,
                'width': -8345425868748019029,
                'height': -7900777860898711637,
            },
            'minimized': True,
            'resizable': False,
            'full_screen': False,
            'meta': [
                {
                    'key': 'ҶҦǏӕιҳϏňĲɧˏσТƟʥ]Ԍ;жʤпʤʩÿƗϕ*Ƒ',
                    'description': 'ΔgʬǪǅѠĢƚђԈëɠԝ˱үǰЛƯÖē\u03a2҅ȟÜǇѥʻȟӶВ',
                    'value': 'ʼԓˇǵFóđуˉʗȽ˱Ӆ\x9fƜƒвσͳƲҬӤi2ӠүӈӶȦԍ',
                },
                {
                    'key': 'ѡԍ҈їôȂĊͿɅӹ˞ԉ\x80ΐɯԝϟ',
                    'description': 'ǤŻМ2Ȩ;ξ¥ʡӞԌŰˈƕƦ²ĝҞɼы\x9fCȅƭ\xadƩѮĎΕȗ',
                    'value': 'ұÛɶ˻ɯľİûΗōrƴͻKӃ˺Ʒ˨ίʺĨΘлτФÊ˦ʁɆӒ',
                },
                {
                    'key': 'áЧʕƔ_Ь3ƸƻƂƷԡĉϊԈҏәУ',
                    'description': 'ћҭBӒϡҗүɭЖƪƑƯȈĀҩʟǮ\x87ǶǅkƋòŪûҦʽѠы˴',
                    'value': 'NɃʒ\x92ʐȥҡ\x8dϏ:Ԑ˃X\u0381ɑҮΒ¿ƈƇҴ¥ǵπʙ˔ǐǞπň',
                },
                {
                    'key': '=ӂɍɍŬӲBÒˉȰĻʶӖǒzoÏҍǐ˾ƾ}ӵȧ¸ɲĲɑƀ&',
                    'description': 'ǬϦԞйХȅϞʫłϠɫтś\x9cÅЏpǓȕŖN\x86ҊГɀӱǃ²ˣТ',
                    'value': 'ҼǦ\x7fӣ˼£ġ\x95SҗɎòԗDƐŵ2Ӽ˰ğ¹ŎʭɡȆҎǛ¥Gǔ',
                },
                {
                    'key': '\x8eȯЛƒøłkĵüÛΙ_]´БǭΠƌ\x80Ƒ+ΗчɺƾȭѳˍԉҴ',
                    'description': ';ȢбБŪû`ŏҟæ¼Ȑ]\x8bώГğƣʏÚӪԟÏīω˪ƵПөǱ',
                    'value': 'Ȉ˩ӌǺØˠșƖƮ˞ĿĖìӑɅжǷ¢ѷԓĥә˧Ғɱ-2ȕѼӐ',
                },
                {
                    'key': 'ōįǧїͻУSЄŢͶȀlŤǈ҈Ʈ±×\x9eѢ˘ΠЧӧȖήŉ^ʪΙ',
                    'description': '΅ɋӄ6ȀϦԭЂԩě\x85ŗźѽѣɟ˃ȷāќñ҄śҊШőңŌÑѳ',
                    'value': 'ǰψ;ĬνǼʞϫҍɉͷÆЕɍԫџΐӥƝȍƲ#Ωӌ²шȚҶțω',
                },
                {
                    'key': 'Ťӏ\x97ɐӺ',
                    'description': 'ҪːϮӥşΛƔIԁUҪϯĔя\x81ĒÜ7νşűąӷƞ˨3ԡҥɺƽ',
                    'value': 'þӺӔЊµ_Ԗɍɋϋ\x96ӈƨʗN\x90Ĝƪ\x92\x84:Ұ!ɕːÜʅθǵŅ',
                },
                {
                    'key': 'ǣìϭӹΆʓ',
                    'description': 'ȝҟʹĖϥČХүńŚȃɎѤζӪϫɦÑȆǢɤΉȪœηϽʥԗȴţ',
                    'value': 'Ð˅Ӄǔ;ǧ\x9bϋɦkԇчǴ˱Ʀȱ°ǀʖĠʳ϶҃˖ϖÃĶλΈФ',
                },
                {
                    'key': 'ǲΛȋӾ¸ϓƄCКУǑǫCgȄȟ£РϬėͶ¾ӍɵˏĮɪάϱϙ',
                    'description': 'ĺԌЯȼԄ{ĖÑ(ǜ˳\x9cȆОƑŒϰχɟӾϟʈɫēΕĕɀǟЎǋ',
                    'value': '¼ѣƿηΤʱǶ˺¥ŵɐļ\x9dңËЖŞӰÈƉǙǡӤyʮԒϗώАǕ',
                },
                {
                    'key': 'Ǧ\x96¨\x90½ҋ2ԎϬѯԮâй',
                    'description': "ʬІӚːŝƚʜrӾЦ'Ţ§6SĭԐȵВ˥˲6ӱђʰ1˩˔ɖơ",
                    'value': 'ʉҰυјɅҖȟŶǁѸɓϓ/üԉԞʥȅϤǛɯ¢ӬƆʹ\x87ЅшͿч',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': False,

            'focus': 3727,

            'location': {
                'x': -7461145237447813282,
                'y': -2358223509429358542,
                'width': 3531840109843443694,
                'height': -5860549172286813234,
            },

            'minimized': True,

            'resizable': False,

            'full_screen': False,

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
                'focus': 7915,
                'parent_id': 'ǜϵȊĭˉԧʐμoȝяːŴҖҭmɂçЃȟѸүĸҡBǁĻShĺ',
                'location': {
                    'x': 7248842342090713779,
                    'y': -5874997138305889318,
                    'width': 1921901437291673842,
                    'height': 5023469605285380562,
                },
                'minimized': False,
                'resizable': False,
                'full_screen': True,
                'meta': [
                    {
                            'key': 'ƖɅҋ\u038dʀӸΕĦϻĪÌјƌҕǯåԟѹ',
                            'description': '˼Ǖƕ¡ɺ÷ƺĩ\u03a2ȌŅέǐˊІęȼԔԘϩʭҀιaԁǮôϋ˨˸',
                            'value': 'ӫÛɾǮԚ,:пēћЫR6§ǌœȥϟ\x8bŅʞҋßȍȔӧmǏĀź',
                        },
                    {
                            'key': 'ȝ\x86σŃӾɤВąҽĥʠϜҤtͺȲγĉќƮ¹*Щːв\x99ǝ',
                            'description': 'ќIŴ\x9eԢƴŦŋ\x83ç6ʍҵѱѤǘqɺȓөZȖƢ˰ʚβȳϣwӖ',
                            'value': 'ƝЎ˾ŃǸҏ×fӯʼΣʧ˸ʝөʣϙ\u0379*ΊŒʩ˼ˢӍͺν\u0380ϙѓ',
                        },
                    {
                            'key': 'ā҉ΗϘӱƜΕ\x93ŖЛÐǶԡґ˹ƎşĲІƢʉ\x7f˦ͼ\x9fԉƛ)',
                            'description': 'ġӨ\x97Û\x92ȣMїO\x8b}ƶіʝĞͺǕźǹªж҄ƟƄ˽ϮfζϝЦ',
                            'value': 'ȧǱvtтũ.ĞͼӋ\x81ɗӁăȇЬɰΣ;ΟʭΆƘ0ӽ4IŁўԧ',
                        },
                    {
                            'key': 'ίĖȋЉƥǸ',
                            'description': 'ēŦĬxǹʽɋƦ\u0378ԅıĿO0ȰʡӊʗáӝȥχUż˥Ͼ҃˓Ɉ´',
                            'value': 'ҷĹԢϒƕɕďĉ˸¹ӧЙʄ¬ēЎҧĭҡʉдÿ_ǯѢˢ3Ɗҫъ',
                        },
                    {
                            'key': 'ҩҟĩҬѱǗý˷ũԠѫ˴˘ş˾ȨȸЄϐǋӁ1ŅұÂu',
                            'description': 'У)ӈ˷ˈԀ˙!ĐɓӕτѥђǸ\x8bǪ<ѺϘʝʗ:SζΎҚŚҒƒ',
                            'value': 'ƾȼұϻǺªԪĨ7ԅʷͻĝϑӄЎɢYӑ҄ӊ½Ņ҃ʈЂ\x97и¦Ŷ',
                        },
                    {
                            'key': 'ɮ8\u03a2\x98ʁmƛƵϑҕʆɔюŘԕýŘԀҁ,Χ˧XđɱҧˠŸŗU',
                            'description': 'ʿɟȯπĎƼɼłćԥϣ˹¡șź\\˄fϽŋɂɟҬΑĎƂǡŘĬʔ',
                            'value': '˅ώƒŀΩ-XVϯ\x8ag3ӡχƌĀ҆ѾӄŸƓǇǀƇӜñĉ˄Ǘϼ',
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
                'focus': 4328,
                'location': {
                    'x': -4701154276158441009,
                    'y': 3097980541227898493,
                    'width': -2662217815027173780,
                    'height': -4984458464690785203,
                },
                'minimized': False,
                'resizable': False,
                'full_screen': True,
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
            'keyboard_focus': 7982,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keyboard_focus': 2523,

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
            'window_id': 'ʃюģ˝\u03a2`ЈҁƦƶЄ˵ϧǤђɌĂЀȅӸӂԑVƯǫȒóҝԊӮ',
            'location': {
                'x': 1036692422658634362,
                'y': -173347527243807089,
                'width': -4872231218476778480,
                'height': -2037326697102227836,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ҞԓԪ°͵',

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
                    'window_id': 'Ĉğ.ԪҠƛ\x85ƫŪʝĈĿϬëʻÒϳÿ˸ѷ˚ǁǼԢ҈ҔƩνҶ¡',
                    'location': {
                            'x': -2700274680438728864,
                            'y': -4259184269829310833,
                            'width': 2484593343043378681,
                            'height': 2117438067055309376,
                        },
                },
                {
                    'window_id': 'Ǣȋ·ƗķӃʃ\x90ʄшƊȅҳǸеȱˤį²тĻûǱƜ;ӈʀ\x9cІΕ',
                    'location': {
                            'x': 3255479323144942585,
                            'y': -4385414188404081443,
                            'width': -8737950622446309733,
                            'height': 8977963747792696254,
                        },
                },
                {
                    'window_id': 'áÑœӬʋήlζ|ӓƥǛkɞѱϩЏԗл˯ӿǲƂӥ͵\u0382ʐ\x92ιԁ',
                    'location': {
                            'x': -5856070080314352328,
                            'y': 1915777317597041164,
                            'width': -1248257828469305768,
                            'height': -8273299186287375672,
                        },
                },
                {
                    'window_id': 'ȕǽϫҺ¥ҚFЋÇʂ\x90ƋХ¢éҌʊŗЕM~ҳΖϏ_ΒƘѸˠХ',
                    'location': {
                            'x': -4348498861064422107,
                            'y': 6283126293195287463,
                            'width': 7518262850642916720,
                            'height': -8160639361194452239,
                        },
                },
                {
                    'window_id': 'ѣюҭɭΕήѤɗѪˁ0вǡԥôɟөòӥӳZТʿ˃ȭuАӣÑĲ',
                    'location': {
                            'x': -2754882583253684515,
                            'y': -8495245208881487554,
                            'width': 4838688010180038547,
                            'height': -6340027054316783222,
                        },
                },
                {
                    'window_id': 'ϓǹ˽лӂƶƒлƨҽ',
                    'location': {
                            'x': -1444028424992213669,
                            'y': -8439287973138032930,
                            'width': 878390303073597332,
                            'height': -5909934904847420813,
                        },
                },
                {
                    'window_id': "ѡɘũѺĎͿěʏɀľʍűˢʠƽòºш¨'ŉĺI\u0382Ȝˆ/ɶѣȇ",
                    'location': {
                            'x': 4594620850232978589,
                            'y': 7284411890584735341,
                            'width': 7162586168935427441,
                            'height': 1050320766362495116,
                        },
                },
                {
                    'window_id': 'Ǆȃ¾Òκ΅\x8dѿš˃ǭʙҍ\x8aΏǇˎÜͼōÝÉÍĐ\x8cőŢϮȢѸ',
                    'location': {
                            'x': -8369714106827174594,
                            'y': -1784692126729606386,
                            'width': 3476752596743928786,
                            'height': -2420187256114917568,
                        },
                },
                {
                    'window_id': '·˖ЗВТŹфѽɂʀӜ;ƑȗǎĂÓӬÉʰŪŏұ˃ǳĄ˳ʘԌХ',
                    'location': {
                            'x': -8706290498105317979,
                            'y': 4461089117797819567,
                            'width': 2404238756960731562,
                            'height': -3315887672193834885,
                        },
                },
                {
                    'window_id': 'ϕCɅ¿ĀªψaŸ˦ĮϸѠΠӒʪ˒ҠӥƥžϬӟïѰѸʀʽӚӳ',
                    'location': {
                            'x': -488989032567248855,
                            'y': -5854210701644975198,
                            'width': -2131044949088360585,
                            'height': -697778833883486046,
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
                    'window_id': 'ðȿǺË҉',
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
                    'key': '\x8eϤ҃ƱІįԠ˛ƪӢѮĀͰGūjĘŰӴԨǖ˱ǸӗÆрkμɉɴ',
                    'description': '«ћɁҖȇƚũëwЙԃїɶӷɮãѩӖǑΎҊ҃ԑĆÐƮъ҄ɵΩ',
                    'value': 'ЗǡʙЂԥĻƤƜǺΞ˵ϹŘ\x82зЁ¢ƟǢҢУѓȇɑŎӜҫyC»',
                },
                {
                    'key': 'ԄԆɚΙЇƞŉŉÊ\x96y\x97ČԘгāӔʰ÷Ȝв҃¤ҘһǈҦ˰ϧЎ',
                    'description': 'ȭнÑǱԘVūʹёyіĭԔǿЕŠLϴӏ˳ʕɣѡɜȄNҥ¦ΈƔ',
                    'value': 'ӐъïԨԢўġќ˔ўȇȺɌӈδěɛʴ˘ĂϋΩʣӅԦś;Ӽϕj',
                },
                {
                    'key': 'ɓİİĜȴʌœҐӼ,ǢҎǌå\x92Жǁͽ˧ÓǱ˘vƴԍԙ~GǦ°',
                    'description': 'ªpŐåĚ\u0380ҴŐȋ§ȣ{ʨЙӥџļ°ĤгȺГѫƵ7ˉǙȈЕg',
                    'value': '!ѤŮολѢҡ³ɢƄŞґƵ\x9eL<щÓӕҹʎѭĞġΈ&ˈƿ\x82Ŀ',
                },
                {
                    'key': 'ŧʓ>ϬԈӥǟүϏǣÙДͼŞΠǳˢʻǻʟIЍνӢВ˜ӱҊαԭ',
                    'description': 'ǰɨϒȲϚӤŊѪê\x80ғ˧ƺъĂϦΩŲΰƨǋǁ(ȒǁϊhÄȵȼ',
                    'value': 'ƋйȔ˰8\x8fρӘ˜Ǵ-ϕԒĜӒĕҵȆůӺƣöϟҶ¥Ѥˑϡēӝ',
                },
                {
                    'key': 'ɾЊˇȒ˫Жӥˊӂ[ԑӪ',
                    'description': '\x88Ε˾ȍT|\x9d\x80ϳ\x85˽ӭԫżˀҽɣɫrǸɁЃΘê@ӐˆǒȔɚ',
                    'value': 'ËÖ\\L>ǎŸP\x95˸Ӱʤ˘ˠǬɬӝʬȅԍˉĩÏ[ЀӔǨҭȻþ',
                },
                {
                    'key': 'Ū$ĀȀ˃kçɸҊRhдƵʪʜϸ',
                    'description': 'ЈМͶӠΦ¡\x8f®ǠˍĜӺ˔@Mҥ҉ȺȓĮǷˤŹʴƳϜысǰɟ',
                    'value': 'Ϭӿǡ˶\u038bЮϼԇʁʉμқН°Êǥ1ћĜȲӃ˗Üɥï(ǲìҌŠ',
                },
                {
                    'key': 'ƹѐdΘԮXǀɦΪ»Ļūͽ',
                    'description': 'ЏƆɍzĮҬʙǝ+ԚȬ²ɫǆӟŀƜˇŞǐěκÓǙțӟϽӄԃR',
                    'value': 'ĉDʆǦ҃ʒɾӌˑιǢŪοɣ\x8aɐņÒϸˤǾĝσ˴ɾҍӣɀӘϥ',
                },
                {
                    'key': 'Žӡυ\x82Ӡ˻!ʺϧђƽˢ4ȼҘ',
                    'description': 'ũдʨȪӦȊ˘ҏӕǏșňfɒǥȨltƶѾχʁФҿ»ǒԛҏ|Ŧ',
                    'value': 'üʊйʺτɒàЄ˭ĝзԆȧʚоԭȰɿóхѻЙŤЯǗЃƁÁ5Ɖ',
                },
                {
                    'key': 'Ƌ;ūҳԤŘƃɽʬĒӎAǻǞɼƸʔ˕ϵÅ\x94ҜŧҬÌҁ\x98¯ɭĪ',
                    'description': 'ͽŠόɕ˄\x8fHѮӧɶŽŒrʗϴǽsΣώϡҿȊɦĶѾƚĭέǾ*',
                    'value': '\u0379ϦɨҚʈθѿӪŬсϗ\x8bҽσeԕƋҽțӤƯϡıǈÓЯǨʘ\x89v',
                },
                {
                    'key': 'ȈϘϯǼĿўíҽɦԇ˨ȝř¥Èϊʰ˒˂ӕȐũϔș¼Ȕ˲O˗Ϙ',
                    'description': 'ɟʒ×җºρħϒʝϢȡɀ˘ņ[ӾӺťӋŠÌîÜÚj\x85ƀǆο3',
                    'value': 'Ͷ',
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
            'focus': 1633,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focus': 8053,

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
                    'key': 'ɄΐĈɺĜˆA6ћŃĨЈ˱в\xa0ɮǽӔŉʿͼĊά',
                    'description': 'ʣѵŠ©пӵɡϰиØϽɡɪƤѦĤFҚàԎŨȅ\x82˔Hԧұˀʊƻ',
                    'value': 'ǛơŧƣνрϴĈ˚\x8cЃԌ×дƵŉA?ʑ\x92ɻŐxѠ\x9aˠƑŋėk',
                },
                {
                    'key': 'Ǉ',
                    'description': '1ůҡȬ˃Ѵѓ\x98ІСʽӖoʁѐʹƿˊЀȢ7Ω\xadˌ7śßǼҥʟ',
                    'value': 'ΦĈ΄ǛɰǖңˏҐHVʵĤҐБŋćВҟħɪѯѻΕмΒĂbΗ҉',
                },
                {
                    'key': 'ǁџҸǏӏԜЉӕoԦNʜh^ʼsѰŨƣɢƖĔԧ]ȏɈлɚȊЯ',
                    'description': '˙Ыа˅ǧūПԏԦǥШѵӞŀ\x82ˑƠԚĩЂϜЮӡйͼλѝˈʄʆ',
                    'value': 'ѽÛяԙȿĠ\x83ΑԅʰV΅ǊÅ\x89øя#\xadțɶHʭʼΣ\x96Ǽɳʥψ',
                },
                {
                    'key': 'UœěȤ\xa0ѠӔÑєÞԐҼЍǫɟ',
                    'description': '¹ơŵƭɑÙ\x91ԩҀԌƨԈѨԫП˰ŀIŮˀИɊ˒ѩ\u03a2ƖȫưҬͼ',
                    'value': 'ǽ҂ĆҞȃӪÔԈƃԉϠ(ͱʩˬǍȞuȅ˭ưϦ˜äд¹Ӊȁɧ҅',
                },
                {
                    'key': 'υԐΏ³ƾԂȏΉǖɽȯmҝđͷЩɻ',
                    'description': 'ŪȚσϦŃԒϻǥԘ˩ǻˀ˸Ԁ˪ĺΈŬ¹!Ć\x9a,ћӿё¯Ɛ\u0382i',
                    'value': 'Δл\u03a2ϸ4Ϗϟ˙ƉԉĮ]ΊСʈǼY@Ήіǂԍʂ˘ʫȯɋDĭɠ',
                },
                {
                    'key': 'MvԊɜҸбßʗЌâűʤЈ',
                    'description': 'ťƥĿәΝǕɤӀ˂Ѧ;Bѓʿѹɧ×ǴΰĻӵƪӁдƓ©ðжġǧ',
                    'value': 'Ѵѽäƺч\x8eәȷǵÝϿқÔϖЂӢĵɤƉХыOʝȘТ˗ĮȢɯ\x8e',
                },
                {
                    'key': 'ʮ\u0382ɀ˄п\x9cΤʄƋӤԍƌɷ}ƞ',
                    'description': 'ʥ˚ť×1ҿʜЋȴԮԛɑЊʛĞі\x825ĔÖɥĕ´ȏʂӿ®ьÎǷ',
                    'value': 'ǌȗѝ·īÝHϓʂeˈˣʘàʎżҎǠҜbӥŒƌǿDԘhԡƴĶ',
                },
                {
                    'key': 'ˉϘǭä\x9dϭƅҔƐϺʍƵŝπɕȍɰŀԭ7ĨĦ\x95ÈѻЬʘʙрœ',
                    'description': '¥ǧƱҁɪϛзԬʿΙ˳ӭүQˮЫёȷǽσоӞΩrЖΦԦΪßə',
                    'value': 'ÐΎӳ\x82ѣ¹нɨηЭ¿ŨѣȤƣĂЖƦϕ҆ĔŴɪӢȧͿ˵áϖπ',
                },
                {
                    'key': 'ɫȢӹƩƕɭRɜÒҤʻȳđ3ȀC',
                    'description': 'ϺǳˤʇʒŇȟņ<ʕ<2ʍʢƽΔӠъɫўѮȾāʮƈȦʬǢ˘Џ',
                    'value': 'ɖΌΓÄĿϸĀȌȒåҁúˏÛĺнǠд=ǵЧЍå$\x97\x87ǆwˆʟ',
                },
                {
                    'key': 'ɃΡº\x94ΚӐӾҢĈǇçǠƆқϹ˪ϔȌ=ѳÏɕŅʌŇԣȴǆj9',
                    'description': 'ĀӄȵƉжòØʩ_ϿÉĩĥüΏѢȶƉɏΆ,ЗHƭ˜\x9aă;ȗӱ',
                    'value': 'ϭҾŉͿø\u038dľʧ˦Ă\x98Åa\x95ґԦҺȻҠԓ˳ĉҶś6ϴ˦ĈϋϮ',
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
            'window_id': 'ΆǛяȷњυȤŗƢ\x9cЦ\x91Ʉʨ˨ĠʂĂ˭ӣê3ȉ\x82Ȇιʆӿºʢ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ӆӵ×ӕĈ',

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
                    'window_id': '~ǺªšăǪ¬9ȖӞ×ǚ\x82\x87Тɚʭŋ҂ҨEsѻɷ/ӥģ·ŕT',
                },
                {
                    'window_id': 'Ʃѥͱ\x84ΛϻʆɭȮ\x9cõ»ɹЈɗŊ\x84ӂ_ŋÏ·\xa0ґʩѾԜ\x9eŢƐ',
                },
                {
                    'window_id': 'ӧґ˕дȨ@\x9bϩǫ¯ˍʼˠ˥ҿ҃ӺñǌåԭŇȵʹmэdɎϳȃ',
                },
                {
                    'window_id': 'Гӛ\x85ÁϝŶԭΎƟĘǦƑ\u038b˚ȗʢ\x91ƺԪХ`ϡ˵Ŝ$ԒŅҊŔπ',
                },
                {
                    'window_id': '˕҇Łɺ҈ȺιŎƎɫǒҭѵüΉ\x8eχҷѢǡϠ\x89ԐMыѤɭзÔĿ',
                },
                {
                    'window_id': 'ŧɜÝҘʍǞmȃҦ[ńʨʵԠμɲǟԇʲũɔϞɨ\x8bÁˬȴˤМϞ',
                },
                {
                    'window_id': 'ƎӄpĠˁʔҨҪÂǆҌГɃS\u0383ŜćѠСΧύыҖ\x87šЊӌǷʩ˽',
                },
                {
                    'window_id': '\x94ϧɠć˱ǺƌҦȝƀcɁ¥ȐϜǛ˝ӂϖĠЀǣԁúÔЪĆ6ʚӪ',
                },
                {
                    'window_id': 'ÈÀEԭɢ\x7fˌȔǀӯ\x80Ͽ\x9cMΣʑ˛ˡßŲ˘ƂȀɃŘ¹ԜʄʀΚ',
                },
                {
                    'window_id': 'ÚԦˁɫҌԤҤԒюɌĬСª\\ɑιơѩͱƷʋɞǞĥѳϑŸŭөӱ',
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
                'ɓāƹͷȫĮȸʆ˝юȆſΥɕҒƏӌïλǸпѢуͽ_ǚƕĿ]˴',
                '˱ȐĪЅϽ˺N΄ğԭ_ΩǪ˻ϦнюɸɟϸϝĊ˛Ʊ×čǴȌΨª',
                'Īµ˚ˢDÒȏМϝƛ˅ųҨĵͻËђнўȬϤçșÕͱQ®ÌҸӺ',
                'ćĶĪ/ʰȳŦʯχг\x97`ȴéԛϊūϟɋѡ\x81Ǡ˰ǑÊÎ]˵ȔΝ',
                'ΰь҂ѕɩӵөĬɺСęƟʾǔӅ\x9bϠѐǗɡǙїν˼ŲІˊ\x84ÅÅ',
                'İƫŖ҅¾ɧɨлΓӂӖʉɛōWŴНɍ6ƽǦҖFˋвŵsѵъԦ',
                'ǆňҡϲϴŶΫμϕǡǥŒ\x9cȳˊĖъĢ҇ǭѴ϶\x83GǪΝȴѯïΏ',
                'īқұčţƎV˼˼ƽЯˬ0ģĲfΛ#£ϑçӥϢŽΪϓʥƗЪy',
                'ҘǤƗȾĺД\u0381ɡǅӊџ4оȧгΉθс[¦ѦɅҁŐ҂lԉәπϴ',
                'ŔjŉΝȧȸʫбҲâ±ʎҭAԉ³φѦжÞԈˤ\x99Ĥ˸\u0378ϳȨƿͱ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'өv\x8eέϳ',
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
                'focus': 951,
                'parent_id': 'ˏ˻ēϖÄʐĴСȃϑȚΫȎɷӃ\u038dǛȗѱǑǐəȪɿѬýɑͼʆǣ',
                'location': {
                    'x': 3964907285493300417,
                    'y': -409482674962841451,
                    'width': -4221998467768922898,
                    'height': -2975305143672213512,
                },
                'minimized': True,
                'resizable': False,
                'full_screen': False,
                'meta': [
                    {
                            'key': 'ҶҬԫ\x86?ʋ!ɴ¡Ǚ',
                            'description': 'LӻβҴƷҞȻċʞ¹ӱѷɲ\x9bїůóÙˁξŋ\x8bƥƩѳ˷βǧʩɻ',
                            'value': 'UʫÎΑαɅΙ˻гӖǽйI˺ʔƿCǠȹD\x87ѼʈҎмΜϪƒʒʸ',
                        },
                    {
                            'key': 'ϝȘŤ\x8a>ԇҴʣȒƁӳўH ƃ0',
                            'description': '˷çӪЏgӼԈǾӣ9χˇΙĲɳå҃ԬѨ˾Ɠ˞ŞţҐԭʓ˂ϕ÷',
                            'value': 'ϖӎϊ{ŪԬѨ\x9dĐϑ˚ӇŋMˤӉÞтȶŌϑȝԈˆӔǯʾʥöȯ',
                        },
                    {
                            'key': 'èǡð7ςϔɍ1ԖʖĎ\x7fſɯ\x91ïАӊƔӄ',
                            'description': 'ǫɀЬŮǔχɉеʿМͽΦũм\x86đԊcøƣƄýΰˌϲќϼäÇŊ',
                            'value': 'ʑΕǯıH;SηƓɚћ4P2mԐԄGӤ\u0380ȢĲҩӣј҄лOĥѹ',
                        },
                    {
                            'key': 'ÁΟǭlï\x9fάҧƲȞ\x83§ĞԃÐŴЍ=Ӫˆ',
                            'description': 'ʻǃЕ˛ϫлӁhŸžĩƱ(ЯӿтҨκΥћɑŭΔͳЈ˾НʆɏĚ',
                            'value': 'áΗгθĔ¿äǎςżħԛĒӽơҫƏʿƒԮ\u0382ҧбɳ˂ϛѯ˔ɩå',
                        },
                    {
                            'key': 'ǻ',
                            'description': 'ĹϦȋөǜǦϪѮӺǡǸĸtІғƎÏнΧ\u0378ж\u0378ѭώȗǗʖʶk˵',
                            'value': 'ΏӣɁίkUԏЏPtԃЋňŚƄѓҮӌшОÊ\x8aȯћΩӐѶFǚА',
                        },
                    {
                            'key': 'Ҙ˸éғʗ҉ѥ»Ț˸ЪҕΏԙȋ²҃ї',
                            'description': '&ΟőѷƀΒƻ\x83V<ә¨ԅ˵Υ˺=ϟԒŀ¿ʘŵBѨʴсȊˌ˝',
                            'value': 'ҨҽÓȃѮͰȣϠˮɓҿĄȃˌªщҋɜ˟ԌϻɃĕԊʏȄҼԢ\xadŗ',
                        },
                    {
                            'key': 'IϱƂД',
                            'description': 'ˑбϢ%ƶͰҶĝȉCµҴόû˧ɍћϡÂŠĘϩӖæýľɪԇҀѯ',
                            'value': 'ҵԜǌƢͽʒʀЙɗǞбŁˋ˵ӠҨǏɮπșıӟҭԔ¸ИѼʭǖI',
                        },
                    {
                            'key': 'σ\x93ИϬӔË)ƓΚП@Ɔ¡ҽӪ˰ǯN\x85!?Cˡҿчü\u03a2ϗͱ#',
                            'description': 'ǺωȔӢˑ8ӟΐɏԜђ\x97ŶΘȪЪуТѰíԑµҖѥǥȴ\u0381˖Ѿʧ',
                            'value': 'ϵʈȈѐȉϺ˨\xa0ԧâͺ.ʎśȰķƨΑϲˋFȽǰϨ~ЈFҭʘѷ',
                        },
                    {
                            'key': 'vɞɷɠѹȥϕƆӵЄӟĪƚп*\x99ƹмɷѺ>ƒϕjʹĦж',
                            'description': 'Ż˶ͼɣȁӾ҇ӣАτͽī3ŁŽѶğɸƮƹΕβʃЫѣӕň҆αό',
                            'value': 'ҸúёƣКȊ˥ĂԡɨӋЅĴIΨԣ˗жƑӑũʏɗτɦ;ˑÓǽɚ',
                        },
                    {
                            'key': 'ȚӒʝăɿ\x85д˵ЮŒʠѵΝȣôЯ_ӇùŹƵ˨¼З¿ȸŭԓż4',
                            'description': 'ніԜчŌіМӪ4ǎŤȹÛǶ\x84ӾǡŔąbʘɺǆʶѻĸԘ;џĿ',
                            'value': 'ϛňđȪɱ\x8fΘӉGÐїυҫʹ*ʼфШç҈ǃ\u0380ĿӛƳǯϿĕ\x83ʈ',
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
                'focus': 7968,
                'location': {
                    'x': 2281812622636905207,
                    'y': 2077186751782813033,
                    'width': 1830762179230946029,
                    'height': -6157595869221273397,
                },
                'minimized': True,
                'resizable': False,
                'full_screen': False,
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
                    'key': 'Ƙ!ϒ˕ʑϴҹ',
                    'description': 'Ԓӛ>ɠ˛ƽ¢ȍƠĨƂɑǾѝԜҹѥҀùҟƫƦѡȀҤ˟ǽӞ˸є',
                    'value': '˔ƌЊɀ5X˖ϞQй\x98ǒ7Ř˪ѥǮϻϱ,Ȁǹ¨\x92ǸͱԄȘÙǾ',
                },
                {
                    'key': 'ήԀįŌȯư:ɩ!ЇʛGŬμӅ',
                    'description': 'åɜòџϡϹѮФҿĭƗͺȞЃ¥ʥƞǙԥ\x9aҺŁӃĸ\xa0ӲƫПϣ"',
                    'value': 'ĊуϢ͵βΜʬǚ®łʗĹӂÏѼǡȎȻӯғҠʅȺΝоӱÖʖ\x96Ӧ',
                },
                {
                    'key': 'Ɯϲ϶˞ȓʂK_сɡϽҍȥȎξúɼқԡßӞπӄíǷѲūŎʙΎ',
                    'description': 'ȃĲ¿ʷúϽȌŒҾɝƩŔÇΧ,ȾĚ҇ҢҜŕƞ˒ǒƌŮʴƑίƴ',
                    'value': 'ҔԈӽaΣʔϐřӦŮΓΘŲǩҋǄ\x95јȵҰśϟ/\x91ԝźɥǣХő',
                },
                {
                    'key': 'χиǱҬčΜɄɠțÞϷǟȪʔɋөƨɭ\x8aåΚ\x9fɓėѻʨƈϧłӮ',
                    'description': 'ȊДÔŖӰԬԇʳń\u038bѲėҥ\x7fɐ°èȦ_ĮЕzȀ\u03a2Ƶ\x83?UˌƝ',
                    'value': 'ҧґ?Ô¶ƯО˒Ȓ{Ϛȸ¥ȐˠҒ\u038bȯĚřĞŌʋԁɵăȍΊɩ¿',
                },
                {
                    'key': 'ɽϏ-Äɘ`ϑҜìǸѶ˻ƌȒƮ_\x84џјǣDҁ˜\x8aǣ§ϖń(ʏ',
                    'description': 'Ϣ˅ƣΊǩ҉ɥ7ʖǊĤˋƠϼҠʰҢȍϾUňҢҥԫͼȷӀ\x82ƱѼ',
                    'value': '\x8bĀ˅¹Ǽȷ0ÂïҤ˴ȔϑΒϴǌUԣƖΚӾȵ\x83ǐђҏȝʄHŲ',
                },
                {
                    'key': 'ƣ҆Җ˽ԕÉϚbű',
                    'description': 'ĖЖΆēЌĺʽŸːʢƞ¼аϪƓԌЇԔƾĳԨОûđѧ Ġϣ¥«',
                    'value': 'ʕǺ\x7fƫʁҞUԋþѬUˑʠʷӌ&ӠφÝϡΰÚѧ 2ӹӸî\u038bŲ',
                },
                {
                    'key': 'ÇɡˌˢYˬȾѹƖԟѽ8њĄɽ˦ĕӼæЧ%ŵ˪ҧѯNљCŌ҃',
                    'description': 'ŮԅŹɆǴϦʟТɸγƞεʝB˳ɣξ\x8dҚԎEó',
                    'value': 'ѳ/ƺ˽ӆѸ\x8dѭ|ВТIņ©ͿˤϒK˟ȲИÅǅǈȠ҇τıčȰ',
                },
                {
                    'key': 'ӝǄұ*Ҿϭˮӣ\x98ԎԇвΌɝìȣ˥зу¾l',
                    'description': 'òÓŌĩԛàӻ÷ǇiԀЂȗ·ТĤɸԎћίżoɀπ\x89ˀԑ˦°¢',
                    'value': 'ˋSðˡȜѰϛǿӅӶpɱѰЦƼӴѪӗΞ˨Ɯ\x92ѹ˳UˢҨȔθ˄',
                },
                {
                    'key': 'rͳЯ=˕ɩԨ¼ԩˏƚĄǬ˝³жŪɒ',
                    'description': 'ЭŘƑӐҩѶƛęӾȢпĄи¹ƷΘƲʅʓưȅΐҀſWǞҕťʽǝ',
                    'value': 'ĩ˦дԧɤӅƃ\x9fɞɬŦɽɄǓҤЄѕзIĽz_«Ĭ\x93i\\Ȭȝˣ',
                },
                {
                    'key': 'Ŀɣ7ϴ˩ҿФɡӘΒ9ӵ]ҶşȞӣϹїǂʦӰ[˖ÚŲԇɰʁ',
                    'description': 'ƨцɠӖϜɼȥӅԃѪР±TŚƺӲƫ҉ЀɡʕɪʡѲ²˰ǂGőη',
                    'value': 'Ҥ²ɿџȩ·ǛПʰԤѪ˦π\x9aˉ-ҰɞӤŭ\x99tƤˊсƃåұĈɒ',
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
