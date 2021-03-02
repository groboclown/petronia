# GENERATED CODE - DO NOT MODIFY
# Created on 2021-03-01T15:28:50.682950+00:00

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
            'x': 2445350951560220955,
            'y': 1635930407134517988,
            'width': -883140456381414249,
            'height': 3846197494682898373,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': 2556667276273731382,

            'y': -1507598795250355718,

            'width': -2472926867441257015,

            'height': -7290876884953616982,

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
            'key': 'ʙ҇Ņ\x9b%\x8aħҌ˕ďӅ\x9cϘ®Ȧӡ',
            'description': 'ȞԦʹ¢QřřƣƹŧʹΖӌҮʕµϧπňɖȍϚԗ˦б8Ȗʺɱȟ',
            'value': 'ʴӗʯ_ųҥї¯еΏьɿzϧˬӕŐźфǁáҫҲ;ƙ˷ШӼʘԟ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ѿ',

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
            'focus': 4969,
            'parent_id': 'ʤKģӊɐԗҭż¶Ɲ˩ˀҙʷӴιϡbζ˘ӊϔ˾\x8dӱǒҠħɫʲ',
            'location': {
                'x': 5896639654708668925,
                'y': -7873633741477204092,
                'width': 5991220673116771132,
                'height': 6342476105724492082,
            },
            'minimized': True,
            'meta': [
                {
                    'key': 'ƤӀ\u0380ǆɹ;υВЯҺƹɉƐЂʃɏǣðŲƧćСшƿþ©ϫʀȌǋ',
                    'description': 'һ¬ɑЂʚĴʪǊˍdűˬʕʏҸǂʒӞҽӮˈҡ΅ŬȽŏ\x82ǹӈѺ',
                    'value': 'ȯчğʿǜ{˲Ǥ\x8bƯЁēƆŷŔǮþ5Κʲ˜ÜІǸNōяˍͳԄ',
                },
                {
                    'key': 'Ɓǧͽ_ӷьҤвҡŧǜʥƢӇʠŘ',
                    'description': 'ƃ\\ǂŃbƬ\x99ѦƢƂҦ˘\xad_ӐԥӇÔлā°ЛȢѲțӿԬ&Џʴ',
                    'value': 'ю®Ś\x93ɶļòCД\x98ӻ͵\u0382ƮƊɊµɳŌǯѳ˛Ħ\x9daʝԎɆѲȼ',
                },
                {
                    'key': 'Ӗ˄',
                    'description': 'ǤȑƗǀýǙӀҩƩѳȸ˩ЭԜԞ!АȫҐɴºϬўŁˋŴЈӷˠɁ',
                    'value': 'ĶΤəȳԝүĳɌʡ҆ûҗΜӻ"ÙψӗǄΠ\x9cBôǴǫƂȶф&ҭ',
                },
                {
                    'key': 'Ȩ;Āɍӗϡ\x96˩ȃ¿ӷƮРȪƉѫìȅŐ.ė҂\x85яĜȲ',
                    'description': 'ԡɊĺĩ\x91%\x90г\x8aӠӆɰXĺÒԏĞǽDҲǡЈҒӇӬԒĚВťȭ',
                    'value': 'ҌÝŴÀɫ΅bʂÊ˵ǡȏǉǟʙκӴˇлɿʠˮ\x9aϵýκԮƜȉǑ',
                },
                {
                    'key': 'ҴϧnҐ',
                    'description': 'ҠǽѹƀѲқ¬ȒΥǾɘкŨȈ\x90\x99ҧȋǇǺͿӶъӏԚʷƴśϓϨ',
                    'value': 'Ļ\x83ēҜśҴŕЭοȻωǛȀİϥɔȡ˕еÜĄθxƅǫѺюǤӔϬ',
                },
                {
                    'key': '½ҼʭѷĘ˗đȘѩǸ¥ǢѭͻǯŏҤҡЬЛĄ3ÊӤ\x92ԌҖzϿА',
                    'description': 'ԗ#ĖϟѤ\x80ΦѰñА1ǛԊƃ˫?Ъčʭ;ȣdЍȖħÀſǞʺ˼',
                    'value': 'ҋҰӧпɤдѸҹҼчŚwӂůȍǃNҦſεѪ\u0378ѧͻ´ÆžʵǿҌ',
                },
                {
                    'key': 'ǉƻŪń!ΆƕĥȤ¤.UϪԭġƑɋӏϰԋýԪ;ťϜ\x86ƔҺË˱',
                    'description': 'ԫɯ\x88лʥ\x8f˴ƗԤМ7ȫѻ\x8aπ;ϐáŸéĦ²Θ\u038bџóɲФϗǹ',
                    'value': 'żĪ]}ͰǷǓ,˄ҘӯҊĜƉΪĐŶƓÈϲϵӌ-ϦğŰƞѶԉȘ',
                },
                {
                    'key': 'ԃƵ˗Ĥυěјσ²ÒƏŕԂƝÀXʝ¼ɅӵϰþĐýÐÙʹοƶ\x9a',
                    'description': '\x9bҀƻÞ҃җʠ<ǉ*ɺʕХˮǹMǑЮʃԁЄó˺§`2ӬωĲИ',
                    'value': 'ØϬįΏʮҫͰ˗Ǆ\xa0`сњÎ®Ǿ\x88Ʈͺ˳б˔ȐbŔȹϓӨïǔ',
                },
                {
                    'key': 'ƞԨɀƔˢɐ{Ζ\x81ĸɝÜӅǍάʒƒêÌԈ@ɞ˘ȹКǀϳχЃ',
                    'description': '6ҵŀÝŉĚΑª\u0378BϋʒƸŊЏê˨ǝºϹ˃ɴƇ\u0380ЩĂˇāˠɻ',
                    'value': 'ɻҨɠ¸ΫȉȅǱsξʩͼ˫З˦ïϩéãį\\ù¡șϢϫʻŪɲƆ',
                },
                {
                    'key': 'Ύ˛-˒ǟ˸зėϛԬƋɤȵ²ίРҧ҃ϷǍǁδ\x87ˉʼ',
                    'description': 'Ћѻ_ĞUʃӵǒӗÏ˗øɨ\x8fӪϦ²ư¼ԏҘʝ1ʈ38nӿЀͲ',
                    'value': "V'ҊȀɵ˄ʀυ;нԇΡ˫Ӯӆ½϶\x8aŴЅҰɺƆӆԣӸѝ\x8dÿµ",
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': False,

            'focus': 991,

            'location': {
                'x': 3125094686764197327,
                'y': 4605287159334146348,
                'width': -4877383477455108991,
                'height': -8882722464458529620,
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
                'focus': 4520,
                'parent_id': 'Ӎø\x86ĒũëʸΨIξůʖŪȻȢͱŶӍ\x86UÉԣ¢ӺˡȆȽЋŨԂ',
                'location': {
                    'x': -1971018547670220665,
                    'y': -5520569132405664320,
                    'width': -4366528188193322648,
                    'height': -6690134600469966093,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ŸӚƈƷԪĆȘϬпĬвѢ[Ȓ8p\x80L˛\x8fěʮ˂ȆԎ',
                            'description': 'ǳ¨ùņīӁάºrƸȺĆѬяĂԚeϴʪſӳξțάӭƘӎȁλĸ',
                            'value': '͵ѷЛѝ˸ԪӾϹ+ҩŃϝŖԇԞˀƈ˨Ⱦ\x84ԆЍ˕υˋÛŎԉǩϟ',
                        },
                    {
                            'key': 'ҮӉʞɼІɦˉºʓ',
                            'description': 'ѹ҉ǗĻϛÞÖԎʿ\x7f1\x92ȍɲςŕtĬҍҗγË\xadϺӮŖƗτҞӥ',
                            'value': 'ҐϺѵгзɁɲȬàˉ`\x8e»ӰԐ0ɊLiҦɭΫă˓ØÅΊ˻˻ˑ',
                        },
                    {
                            'key': 'ϗьĭ§ƂǶә\x82ı',
                            'description': 'ȤĠϴάŒҐʖѴɨ-\x93ìԞ\x81ƴ©ѶĒȏГԇ˺ÿԠĐșʟō@Ρ',
                            'value': 'ӆӋôćȹЧȢˆƿǨѸҠҩˏɳȂФӥŽͰʯŌʫ҄ƽȚӭ˞ϊf',
                        },
                    {
                            'key': 'ä\x84ʪµӤ҂ȺХΨԖŁ˻ƕЈ=ή\x99˽Э+\x83άȢɕ\u038d`ǒƯΞ¹',
                            'description': '˯ǽʬ©ɊxϧUԬţİʝԐBЦΉɺʴӬ~ɆBȗʔű½ϋнѴʞ',
                            'value': 'ʭõѧǠ\x99\x8aʶӗİӜԣϦ|ÚΞ\u0382ȅ\x85ўԤѽîɕƳ¶ϽЊǻҍ\x94',
                        },
                    {
                            'key': 'ǟ3©ÒƂ',
                            'description': 'ȞØȶҞƷÀΚŞĩһ˥ә҇\x8eНУÈƩӛ¡iƷ˶ˡΚȽϯƪϗɋ',
                            'value': 'd҂ϓƦˑυžʾϮɮ˙ȏϼǴ$ˍė˹ͲӋѐɥΈˣҥҙCѠiȝ',
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
                'focus': 173,
                'location': {
                    'x': 1918386699333565854,
                    'y': 4971241038930373504,
                    'width': 7020375678402706129,
                    'height': 9050441267690457791,
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
            'reason': 'òɣȓύǾҹЩɡƶ\u0380цƨРŕҏзŗωÖȮʱǍFřȎЎш\x9eś˜',
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
            'keyboard_focus': 2339,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keyboard_focus': 5410,

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
            'window_id': 'ƅ¦ĩǌŻҖ(ϳ:ӫȀһȒ˘ьй\x85˷ǙώӶʾχΥϥѧФԕͶƴ',
            'location': {
                'x': 2071271802973259344,
                'y': -6094124585236483661,
                'width': 1647673007637047887,
                'height': -1501851389423969442,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ɥΨҌ\x85ʷ',

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
                    'window_id': 'ŗǶҭǐƢsҚƒİ*Ϸȣ²ǆÑĴĹ¯¹ǘÚԠūǗĉɑƗɖЯï',
                    'location': {
                            'x': -7299079081032517810,
                            'y': 283037596459656212,
                            'width': 2934456575265585105,
                            'height': 3885960901622281391,
                        },
                },
                {
                    'window_id': 'ӧ\x98ʩ\x81Tʤ¹ԟѣʤȒɗǈ§ȣ¶ŰѨʯ˝ŒԏTȘɖЩ(ϮΞ\u038b',
                    'location': {
                            'x': -9141680885676517553,
                            'y': -5746495950206174962,
                            'width': 2795402990645598170,
                            'height': -298328462587170101,
                        },
                },
                {
                    'window_id': 'ѡĠ˚\u0383и˝ίƵ^ȻǹѐГąȗɻǃ%ŎʇìњȂǁ\x86уÞɒͺʡ',
                    'location': {
                            'x': 9035351652709280118,
                            'y': -7470070345642002050,
                            'width': -4258242146544865183,
                            'height': -2940759886667056658,
                        },
                },
                {
                    'window_id': 'Ԋ˗ěåüǊȏїˍ\x8aȻüъŜԢѲԨѡɲΤԇ°˵ҁјҌhƒҏˮ',
                    'location': {
                            'x': -5928844153020458768,
                            'y': 1663601159340843735,
                            'width': -2211479391505008243,
                            'height': 6981732745864243987,
                        },
                },
                {
                    'window_id': 'Ӭǥ_ӱɿ°ĽðWū\u0382ǔèþɐƅʨ˹ƗʄРЍˋĿǣӵʉˆіğ',
                    'location': {
                            'x': 1114284265404895688,
                            'y': 4241255261359759697,
                            'width': 3404248979132953018,
                            'height': 2778185780902718943,
                        },
                },
                {
                    'window_id': 'ҽŜȺʁчȪӀį҃ԧЮӾыгɔǜЂ˥śˢȉŨXjʔкBȶÉĹ',
                    'location': {
                            'x': 1143802681860219614,
                            'y': 436462695821824018,
                            'width': 5945483961399994411,
                            'height': 3730852654384928765,
                        },
                },
                {
                    'window_id': 'ŃΎČςѸ?ɮюϭȿ҄ÀӠȰƢĝͲɦ\x8aΦʐɠȀ1όэӽȭǣΑ',
                    'location': {
                            'x': 3063123258424523478,
                            'y': -2016009930577613823,
                            'width': 1671843464733874362,
                            'height': -242167172296662583,
                        },
                },
                {
                    'window_id': 'Ȧ´«{ԐАʫèфԞp˖ǋǮȬÚ\u038bԎӿƍŔEӆʉғŋҠлεN',
                    'location': {
                            'x': 5132460219314076136,
                            'y': 2972234646010566184,
                            'width': -2235681093460159084,
                            'height': 1146030294490265194,
                        },
                },
                {
                    'window_id': "ǬҷǿмюϩȍЍϮɛ²͵Ͼʎɨзċ'Ɓϩ©ĎȷѰɘN",
                    'location': {
                            'x': -7162178962600172386,
                            'y': 5473977616959015088,
                            'width': 8012771393197358934,
                            'height': 6220627645640030172,
                        },
                },
                {
                    'window_id': 'ԮҁǷÎҽɭӹBÙΏШЎϊ,ůҟţϱ_ϲ\x8fǁnǯǵɉɺ\x80Ϯǿ',
                    'location': {
                            'x': -7178569745099971964,
                            'y': -6135175047772336954,
                            'width': -3139690682420062820,
                            'height': 4402129036586866117,
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
                    'window_id': 'wњˆТǼ',
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
                    'key': 'βʅÒxȕМǓƻEӻʇȏ\xadԣӆηҸåӖΩ˴Ұ|£Ԧžǆώ΅Č',
                    'description': ',˧ǅ˝ҏĪҡͷԆϓǏ˂Ϥǡԩϭΐ\x832ԥҜΓ\x83ːăǶΩ6Ţ2',
                    'value': 'ɣïԜƽφǆöϞσíƪʰϏӾˋǹΡҋИƑшţſŬʵ˗ǦӉΒӀ',
                },
                {
                    'key': 'ʱΒʱαȌʦʣʇǴ\x8bɹɽ',
                    'description': 'ԇӾŭ\u0378άϮǘμΞƷѐǒɣĆ\x96ƲȫϩɞȤċſҞX°χƿЍ˺Ӑ',
                    'value': '×đ¯πȧ/ҶĊ÷ťœʹіąԌÙɟÝâб˙ӈ¤ƯϮͿ=ƟĀţ',
                },
                {
                    'key': '"ϴӵȽÕÅŞƻҿȅԕǆȪ\x90Ǯ#Χӡ',
                    'description': 'çϛʵ\x8cðѾΊİʆӒѧ"ȀĨƹyƄĞΠǮǠтЯųуϗӬқ\\Ŗ',
                    'value': 'ΠØļŔɂʔԆȳӴǩ@˶#\x96ѡę\x9bέǴєtƳĤȍÑӉŉɎɉȝ',
                },
                {
                    'key': 'ϸϨҌʾʪ\x92Ō1Н҄ЎȬѰtƬśϭɔˈ§ǍɹȝʓåƂēԢǚ#',
                    'description': 'ũ˺рEǿĒҳĲȊɏbԃŴүĬ¬ȼсƓШǘҟôӃð\\ɭ\x7fȯ8',
                    'value': 'ΞϽәŌŭ,ǋñȲȏаЦȾyĸǏԁҠ\u0380ˬЏӔɂеϘ\xadү4ѹ\x8c',
                },
                {
                    'key': '\x97ȋɑйΠΒӕWԬȅəϒԂΕ˙¡ċЦЛӔœӉҙʂĕŉˣӉŞɜ',
                    'description': 'x»ǊүW϶ѺĶҎŭŭƱ\x86¼х\x9aȧ˷˼ǴԩБÞӵɁŘΤɗSǭ',
                    'value': 'ҸƌƋԇȍԁqѻѴ΅ϝįʯ³ȏȕƌŋгɭXǆʴĕņɣӤžFæ',
                },
                {
                    'key': 'ŕРƙ\x96ŧІʝ¶ʜR\x96ɥО\x83μŬǋԮϕϰƦē˅ѴȤԇäсƼ\\',
                    'description': 'ҿωůˢʂǪүÀƊЍƭîхɶɶΞ\x8eԊʹǎɊɠ\x91ȵǃԈşӧ҅ń',
                    'value': 'ɵ\x85ӬѴ΄ļȕŵÃӛíϣ\x9cѫÜʯ´ͻǧϺ2ǗÅ=ʹ\x94ӷǣȃ',
                },
                {
                    'key': 'ēžřкϗ҄ʩҁ`ϸҼʪˋҡԆwқ',
                    'description': 'ĄάҥЃŴȖĸэő˔ҡȂŬλ°ʺӯұĩҽǖӪęÅpΔǊКȔҤ',
                    'value': 'вǱ\x8dƧҷhєğęƔԨIɁƅѲRE\xadҠƤʭԪǗȌʆӾ˨\x8dȷƐ',
                },
                {
                    'key': 'ɫґʆ÷ѩźӉҭ¯бӽħ"ťϿŲŵɼБЖäЂțԢԂƶ˭WǺ(',
                    'description': 'řȄӬȧËƨΝ\x87ΤķlҲȉȪīĂѭѿĢƒӗɽЩˎΣ',
                    'value': "ϱ\x8eƬϥ¸Ѐ\u0381ǜӁÜǅÌМƨɛ`ϩύǔґмϸ¼Ʉ'ƈ",
                },
                {
                    'key': 'εÌ9ςșËϖʲ¬ЬˋήǫгłώŲҶяɽȚӃԇͲʪʃlԝǮȍ',
                    'description': 'ƓΟ²ȭ&ƘѣŐËɟÓĂԠSÄҮkԤϚÛȪɆЂΓĹkЀƦ҄ӈ',
                    'value': 'ԔȕƸŏÖ°ȁ͵ʇŷ\x9cЅɰʍǐİЄù˂ĈфɹħΟч\x90Ïì`ç',
                },
                {
                    'key': 'σC\xadƬ\u0380ϣϨȊԈԟΞ˗ѽСĺôҗɸ\x9aӻԫ~¾CҺƕĽϟ²˴',
                    'description': 'ͳɂʕkƿƱwɑϾѾǙÃ´\u03a2\x92ӢӾĝЦԔɽȓҷϛŖăƚОЅƇ',
                    'value': 'ɳўīƞŠҖҊŭzź˅ҭŅkѻǪȯӜӠ¢ҊȁϒŔˁȢūƩІź',
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
                    'key': 'ϜИˌȼYʕӅĂ\x87ԗϖԍǙ˴οђŤ˹˟А³ʇƠĐӪѸŤԗϾђ',
                    'description': 'ÿҟғZeʉˆԞЊɖǁɔțiԮfÁɊɚι˅Фϒ`4ʩȼƋґщ',
                    'value': 'ҳЇţ\x9fěӋγ\x8aԡѠ˔çȹӶïȭbԐԡxšĝƲɢjԠɞŵӁɗ',
                },
                {
                    'key': '¸ƇѸ\u03a2ŭ˵ӋWȰԠĤS«А˴FąʁʈǟȧɘϝȨŐȓҍƎҬ·',
                    'description': 'ǀĻ˕ˊ˨ϠƸӱ@ìРþцÔɮƾҡʭTȆҌ¬æȝѠíȢԕĔȧ',
                    'value': '˩űϔ˛',
                },
                {
                    'key': 'ЮʜȮǈǩÊȧʌİ\x83Ƭ!Ʀʧǥ³ѰѬĚȊʥ¯jЎmѶϮɸ\x99à',
                    'description': 'ѓȨҩĥƟqˍ\x8eXΔі+ґ\xadӕԞ¤јπʆIӅƍʻĳӜǷԝӇҽ',
                    'value': '˖мҁ˲İʩǽѠɩƩľƆčąĺƋˁϭѐʒуӝ\x8aГǪрόώƨľ',
                },
                {
                    'key': 'ӧǶЬўԇлѲϢȐҌЬԝ\x9dҁȢˉϐ˸\xadԠƺ˘ėˣȵǧǯγȾÇ',
                    'description': 'ǻӉŌиµî΄ѐʺȨϷѢȎσЇȐ˓m\x9fѻʔΓɇȝô¯ȗŋƻ6',
                    'value': 'ƺɵǦǅőĳɻ}ѠʑδԃғĺŃɅ˶ʘԛӆҙеͰMЧϙ\xadċЭ˼',
                },
                {
                    'key': 'ӄԅƙԖЬ³ЋҚɣɐԓҭ\x9a˽ή:oӚ\x80īҝʗӅЈοҩƚÙĂz',
                    'description': '˸ӎĖеĻɓԐÇϡШѹѢ-h8Ӡ¡¦ǙȳƂͻǓЬǄɽƊͰƍˉ',
                    'value': 'ĄǸѠ˶ÎėƍΧΚӮŎѦͲҾɋҧĽ\x9dԕқјȢАʢƹɾ42ŝ\\',
                },
                {
                    'key': 'qЧԨҖϗԙɝѐйЮ4ʞˏơɭӬĦСԖĴǥЄȗͱԮǛЄкϰҸ',
                    'description': 'ƉγӰ:ǼťŬгĜ(Q',
                    'value': '϶ϖƄƀѺ˒αҮҿҙʰԝÒ\x90ӟ\u0380ƆƴċǨϠӬǪ¤ǪbcҘѠʺ',
                },
                {
                    'key': 'YȨʈíá\x99ǫ¯ρЬԭӞįȎδ˷ʽЊƤǯʾѝҔǨ',
                    'description': '¶ʦǓʁрǚ_ȁ\x85ƍɡάŰ\x86ТԥϷˍŋƆǐӾƃņϊӈӝΰęʢ',
                    'value': 'ўȩİâÂěŜ0ԙӵΒòęμƾjҘ˭;ŊȻ\u0379wˮҰʗǬҤԂ˝',
                },
                {
                    'key': '\x94˟Ɉѕ˵ӀϑœΒп\x8dΚBɇ',
                    'description': 'ǵϝł˼Ԇ˃ɆѤÇσԨãñƚϞФŽĦĝţцŐoɇԂηį/ʴƛ',
                    'value': '¿Ƕжһ˭ȍԌ¼Ƕǔԟǿó҂@Ӂƒ\x8dʈκCӠіÝϰϣċьˇʿ',
                },
                {
                    'key': ')ʿ\u03a2źǉöɱʟɁ˥ς\u03a2҆;мÛ϶ΧˌɿʕҿŁӎҥˈţѲҔс',
                    'description': 'êƴ\u0381ƙd7ҬȒѬμ£Ťρ\x95×Ğīκҿɓԭ\u038dіŰɧƻˇ!Ƨō',
                    'value': 'ɕВϒͽ\u0378ʐӟʭЁӉҋŞÒɲOЂöҹφĲý\x85ȦűП˪ƘϖfԆ',
                },
                {
                    'key': 'ĕЃϢĝʩʌ¯$¶ґĊ',
                    'description': "\x820ѼĴ˺ҔͶбӎɃӴÓâ'ХˇҀˑӀҪѥī\x98χʿԬВЧǛ˙",
                    'value': "țƢģ7ŴǪðǻ\x89ѹΆʹϬ'оѨаοͰ-hŚΘЇ°ϽϿєĉԃ",
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
            'window_id': 'ɘϕ˼n\x9cдΆȹөӄĵΜdρϴʇ®ŖÏȸŋȾΌƽˣΫʀʶĨǙ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'џOӧǔϏ',

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
                    'window_id': 'ŌʮπͺJýϖ\u038b÷Pǒ˕МɯɆˡϦЂͻɅVԃɆԅķüƱ\x85ҼІ',
                },
                {
                    'window_id': 'ÄƘęȏǛӖΓƸԭ{ˤʣô҇ҾėŔȔϼӪÑӄ\\˂ÀğҪ³ɚō',
                },
                {
                    'window_id': '˷ӞȸѳЏ$Іԝʨ¶ŔҾɀĄ·Ӏǖ˼ƷɛψλǿүОӴ!˜ŰŜ',
                },
                {
                    'window_id': 'ΜƐԌљϛΩXɁϯȟɹȶŝǏãνƭʚΘȾÄ]ΦǷǂŋțѢȓǺ',
                },
                {
                    'window_id': 'ύѐԤҹ»ІϧҼƹŶΒːå;ƮγйĴԂɑƾ`әҔɨΧ[Yӳř',
                },
                {
                    'window_id': '\x93˼[ýɽʐӿ\x9cQ˫ƺѨίʽ½ƓťıGʝʛΕȲxǎʣ˄їɕϺ',
                },
                {
                    'window_id': 'ΧΧʌΊίЀĀėϫăϤʮÇ%ą,ӈЄΌҤAͽԃê+řçʷŔů',
                },
                {
                    'window_id': 'ȯƕƼҵɜƪ`Ԇ҆ȱǁʯ\x82ͷǷλΒ\x85ѮʃɢϦΝӅƮʕԊʖɻv',
                },
                {
                    'window_id': 'ӠþάȇǙжʏӋβМЉȅěǭΆʽζʏȧ§ɓПǔʃёCƻǉƟc',
                },
                {
                    'window_id': 'ȏЋç\u0382šǆǳȰėΦЅʮΊɶъˍԓӏǜőÕӺӇ\xa0КɑyĶϏƧ',
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
                'Ŷ\x8dөΉ¤ԪſǤѲɧïtǥΡƤҹԡҾЉ%SķʦΏǁ¦ʆǎƺϱ',
                'ԢӾ.Ъԩ{ȇ&ӜʀεȲЈВôӽǳʚ?ϸ˃ſÎѣɻOͷÒƒ\x88',
                'ΖńӄƕΧцɢӈĂΪԞʗӭԐʳǟǆ«(ýȇѻΆǭǜģ%ɴŦљ',
                'ӪȇʜԧͶßЎ;ӵԓѱȺ~ӔʚƕБѺȼȽ˟Őσʀό\x8cұНnʚ',
                'ʺ\x88ƁσҋƓиÁΡʗÁ"īΫԎˮӶ&ԎєTǜΊΑ®ϙͷј¡Ƹ',
                'ψε¿ȅ\x7fǼҤ)үǇȊɋİ\x8bĝХǜÁžɺϳÁyӇΔЀ÷ȡʩƓ',
                'ŏĉuкǻȽԔˬϙѐŜϗkԛηȫöЍǽϼŎȦďԉɁӃԙʊ˃Ƌ',
                'ӸǽĂЦѴʲʺΘĺǭԋIȎˠҔƺʧ˷ÚшžϢ҃ƊахϪbфЉ',
                'ѫɳθƷƨұϒãʪѪҽȒȈưͰĈԧЭÒŐԀͱ҃ǚҟэɹͷҽғ',
                'ĦƬZßȑƇȷѦΧͻ\u0382ÇȺ˞ʣǣӾ\u0378˽МӹǗӱӕОǴΡʵ£_',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'ǲŗѸ\x89a',
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
                'focus': 8084,
                'parent_id': 'ϥȃĚȖx҇ҠȦǧžɴϪˢρ²Ӕ΄ΎŕǋύЊ϶aʧϲƂȹůí',
                'location': {
                    'x': -685314486929626447,
                    'y': 4251975311082184551,
                    'width': -5209383625833165313,
                    'height': 1430712880381555362,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ӟўʹǟϰŚ]ҏΊ\x9aΒċӤȮFfȎƀDҩɼ҆ǱѿШȱɨȻ\x8bk',
                            'description': '˱ΎƢȨԮȲXɀòȧǯЧӬâŅɜЙˬиβ\x8cʫҒзѨȎÝGгť',
                            'value': 'ŊŐ·ǤΰΩ{ľrɈҏӓ˃ӏӮԘ¢ǧŸʛƒǸ¹\x8cгЖ.ɈĮΊ',
                        },
                    {
                            'key': '\x86ίВı°&˙ŮƔ\x9fŵȆ_ЄӐϘǁŜһӽWҞƎҋƭO˂ʹΌµ',
                            'description': 'ԞΎƉιJsȓqɟ.ÊƸɶJэʮӎ˲қuŎȧ˚ϩȮѭĖ˦Ѿҕ',
                            'value': 'ԝәŎÐφɰT\x81˳˛þǟ˶҇ҵɞΞɾϰУŖιđіȺ\x86Жąōǭ',
                        },
                    {
                            'key': 'ŬsҺʝ҆Їɧ\x9aμǑŕKŋΠɬĶѰƬϓư½ІǠӳ',
                            'description': 'ǐʗäŵ\u03a2ϧјϡʁƈ\x83¶ĺϩ{ԃ\x89§ˡDŤȁϦѵԓӐҲθȝā',
                            'value': 'ΟѾˉɭǤԣѮΩ˪΄ʡÑǈмÓ\u038d@ţϚȷȱƬɨVF΅Ȧ-č\u0383',
                        },
                    {
                            'key': 'ȪĤXѨЖɔ',
                            'description': 'ѣîҢ҆Ǵ˛ÍɢуѺʄOӣ˵\x91êƋéкǯϤZoҤύ~ÑДԟϏ',
                            'value': 'ƺȈЉ˖V\x9dːǸíѫƳҐӢʸѢɉƝŉǼ¤Ú˪ïΕʛӼȒ¿ʀŬ',
                        },
                    {
                            'key': 'ȅ;ɘ{ЛɵҒćǰԎİЉ^ěԍšӲҒφWζơğπIȧĜϘ:Ӂ',
                            'description': '˚pƔǾƐɉɃ˲ϣЏ1ЕšīӅŪȌɇ"\x98ȻƖǷĀ˝ʺĜǈɆХ',
                            'value': 'ǾŜѴһΔɅ˾\u038bïΖͶ˅\x92ҾūNʌРȾĚоԪȖ˹ϗщӁƸȪ˓',
                        },
                    {
                            'key': 'ʣд˴Į\x82ж\x8c\u038dΧ¶X)ǟАTјǃ',
                            'description': 'ϧЈҞɼћʇɡя˔ѫƎŎ\u0378ԓкҔőɓгʘĵrɔÎéÂȅȚ8Ҍ',
                            'value': '\x9fÇҒʬҚɂ#ˀӌиӀˇɔЭ˅Ċ3£ѧћԗȧВ°ʖɑ˹Ӝӡφ',
                        },
                    {
                            'key': 'ыĘɯˁȥϓȹŰӛǓԨԝ\x9aЯюϫ͵/ǉ\x87<Ҽ7ˋЌɲ',
                            'description': 'ɂнӃɝËyŕӨёάǠÍɨЃϩӈԊĺѸѢϢСԬ²θӿʭΔΡӳ',
                            'value': 'ǆˋǏƶ˨ʀ\x8cŗɬћáƾԓƃʅȏg˄Ѹç{ӖČͼΥÒ\x8dσɻБ',
                        },
                    {
                            'key': 'ҦW\x98Όӏυàɐţǀ\x9e+',
                            'description': '˪ҋběȅУ(ǹλԊhȩťƄǻƀņ3\x86ɓQǤМʰÁΚĵθ$˦',
                            'value': 'ҋϋӶÀя\x8fǭʈͶрҳĹТ\x98ѷóɚ\x93ѽΰʉʄԡƙѺǁңʯ§ʈ',
                        },
                    {
                            'key': 'ęҶ˥˄ԭҸZӹɽżôҒϥӹ͵ϵǌ',
                            'description': 'Ύ©ʣǶňǖ\x97ʿşƓϺ5СҠÐħq\x86ȆΡƉΆøǜɟʂēƼƑˊ',
                            'value': 'ϨǕƙĪǋʆƱo·œϋшΎΆľ^ŝľ҅ɯԇˠәрƆЯӖ˶ӧ\x7f',
                        },
                    {
                            'key': 'ǔ˩ҏ',
                            'description': 'ɇϖ϶',
                            'value': 'мxʵѢлŶδь\x90ҍ\x92ϵѠλӕσώʀâƋˤԪžӕГӏό^źϬ',
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
                'focus': 9073,
                'location': {
                    'x': -2114080508592327269,
                    'y': 6398143148425021522,
                    'width': -8528526693864980868,
                    'height': -7689661349164838834,
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
                    'key': 'ЂĨȖ˙ѽŝό',
                    'description': '\x84ȤӚǝŻν¶șǽΆ',
                    'value': 'ԨAĵ\x7fЩŹũȴ\u038bʭСɈϐбӿЍĉӼÉѼ¿ˀƓRēԎϮԀьӞ',
                },
                {
                    'key': 'ЅˣϖéŝѿγӻŗЭЩяΨɞƔкЄɀњͷЂӸɶďʀƦ²ÜӰÌ',
                    'description': 'ԍǾkťŶ Ϊ˳ĔԎá`ŚǚңĐƧЁĿ÷±ЁӥŌѳŊЈ¿ѫʑ',
                    'value': 'ΞǘɥʫԋЀԨέѳϳшƞǄŚԬұũѮ˔ZьƓά\x8aТкЅƤÙɝ',
                },
                {
                    'key': 'BфȅЍ҉àӃŠBүˇΕʓŎʝϾӠʊМϋϣɝ\x9dɩ',
                    'description': "ɟҹč'Ǥ\x93Ԑƞѭƙnώҡƭǁԇ¿\u03a2ԄѼϙǗɬňђʋр˯ņѸ",
                    'value': 'ůˇλԫƵғ_ˮ҆\x7fǓ˸ÎÛ˒6ʦƺȠπʹиɞϗϩԥȨЃ\xa0˷',
                },
                {
                    'key': 'ȡɘӲzӵĂτцѩ³û˥ҧƺŖ\u038bбΑ',
                    'description': 'ɭγϰӓ˫ӦӋȐԏӫğϵϨѿӵξңʥӹЛÙǇ\x91¨ɉŢƵӿӂɾ',
                    'value': 'ĳ7¦÷Ǳ¤Оŭǉο²\u0382˥ȊŮŞxӐЊҝŚњѢϡсήϞìʈǳ',
                },
                {
                    'key': 'чɽϲçɛΈϒǓďҝňȞŘʾǦѲԀƱԓɝɒİƊʐҥǱÏ',
                    'description': 'ӘӹԈ7ȶʫ;\u038dл43ȨéˊҀñXϸȝƂıÊΫȿĿT\x9aæљά',
                    'value': 'ӊʵśǙŐ$ϚÀԙɊčĶͳȜ\x99cӆˉ;ųC˥¸ʶËюӺΗԏƭ',
                },
                {
                    'key': 'ъӰ\x98ϝ˾CŢČҖʳĥȸú>ʋ\x82\x84ɏěǨωԊ2ϡӏȽƹĔҶ\u038b',
                    'description': 'Đ΅ėϋĘǎɉÅɑˋɡȳφхʉE\x97ǒѸa҂ˁ+ӱԛƝќћΛ˅',
                    'value': 'ąѴʷӗş\x8eÞĐSϟͶƈ§ƈȋɷ˘Öȧ\x99Ґˇǰɕư´Јόϼ*',
                },
                {
                    'key': 'ЂŕþАҫƉrǸŽ΄ɧґăѢ',
                    'description': 'џӲ¥ΘɼѯēҏïƨΛƷÙŶѩы\x80ӏ¹ӌΌãӉʴƝуϋϔӯǎ',
                    'value': 'Ўůćȿũơ˟Ĥ˫ÑΩϔӿ·ҁϴЇϖůûԠϱïуҺԇϴԐβʷ',
                },
                {
                    'key': 'ʨeѵŬȴCԫ\x9dġϤɝ',
                    'description': 'ʧɴûĀʦūŲʨΫéǗӤїOʟτĉҾȓȖϦƚ\x82EƑЃϢâӤĶ',
                    'value': 'ɿ&ӌȭį\x9cԠѽǻǛ˷\x9d?a\x92҈ǦъѢʂ˖ҶĴȍȒŊŭÿѩȋ',
                },
                {
                    'key': 'ͶǕƬɐźώͽƥФľ5ĽΆΜwȸ_ϜÃ',
                    'description': 'δаÛʯȩȨÕpԠÏǍȎňʌΜˆҿʔƗ\x92ˮ\x9eѮΣŮŏŸɤȇ˩',
                    'value': 'e˲#Ǫцьħ͵ҎɢţƞϒčԬϽѲĲɚϭĺϢɎ\x87¸ʺԖĳУå',
                },
                {
                    'key': 'ҺʁƠўǵ·ѻ\x8bǞѪΐѩǚεžǭȍϜϘ¹\xa0ӚΩʼȜŵüʈˑЬ',
                    'description': 'ʲ҇ζřʨӍΤϧƳȒɒāΎŭøӫúʤӥ΄ҘōâΡȸӨɴ6åį',
                    'value': 'ƕˆҹѝ7ӽхԡ\u0380ʖǽ\x9dÉǊѶE˝ŊʀōʈōgΕʷÜ˖ӄǎ¯',
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
