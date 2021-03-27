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
            'x': -120087303472130350,
            'y': -6197160724864843928,
            'width': -1949828778747191525,
            'height': 3264557518381706370,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': 8024841169627205273,

            'y': 6726533202437576945,

            'width': 4047197816586715986,

            'height': -1862202280092240502,

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
            'key': 'Ӈ\x80ʷ\x8dѩɒˌӱǁlñЁӦʋ˛Ʊ\xadζċұϳԉȐ˽ʑʙ',
            'description': 'ϞʞѢѻΓщъ\u0382\x9b˞яͱĽρŦӠϾ˖ѐϟ×ȾпИ҃ŭʱĝȍ˵',
            'value': 'Ѳ;ϏӾIɺ\x88ӻT˨ĖƿҐԂƪǝǒϡĉĐӭͼӰŽʞ\x8c¡άΉԞ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': '\x94',

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
            'focus': 3254,
            'parent_id': 'ȿЛǻ\x92ӛЃԥϙkΧŵɜģҪȭNˎҖƑ¼ѐѷëʾĚǽŀ˝ӳ\u0378',
            'location': {
                'x': -8767843159451099333,
                'y': 7849367677548972532,
                'width': 1307857640005992817,
                'height': 4964498940656239160,
            },
            'minimized': True,
            'meta': [
                {
                    'key': 'ɞėÊɍȡʹƵӠμʅϫηљ_ʊŘɕӒҶĭӿĴʉʳԧ|Ɂ\x90҉Ӛ',
                    'description': '˕ϐȝöͽѝǞΟɔҙɔɭ"ɱÎӥԓɚõ˄ΊԢìʐǡɟ)Еϲх',
                    'value': 'ÈіҴк΅ˬǂˡЦҪCќ˩;ҁ˥ȽǼНƨʷұȡњӮҪл÷ÀВ',
                },
                {
                    'key': 'Ǔɴѹ\x96Ԧɲŋӧ¼ƅȨ\x9fÙϐȇĽʖʒʁМǊЪƦҵşԎĖϼˁΪ',
                    'description': '\x9eċŨǧÒ϶ӀǑһ¥ζϷͰѐΪ«ƓȮҽĘ¯4ӯŋή˷ƽӯ{ę',
                    'value': 'ѴéqSӽƷ\x92ƦԓМЈȯӮàêƟȠʁπhʎyқǼԭʊξ\x9fœ`',
                },
                {
                    'key': 'ņԆƻсԙ¶,jƅïƶȾрТŅǑƤ²ŚʈԋĳҽǇĻΰӀǸǍʎ',
                    'description': 'ʥӦɈαҙţԈıƿȸ Ĥ6҉Ĕ\u0379ŁĭϫӂŃҶ˻aȉoŧȹТʜ',
                    'value': 'ΎˤNƫѴϿԜѿǥͷ҂į6ãcčƑԡ¦ԛėϭɞƁˮԌƿǻә\x9e',
                },
                {
                    'key': 'ԡѫ˒ΖҬГĄʯҩ˕ѶƕƼǜҧӉҘ?УýädȆaɯǳɘԀʴĨ',
                    'description': '\x85ƀɳвʬѷƛҖDϠĞфѷɺɨȂѽKςˬӄː\x93ЎЅj\x90˓αǭ',
                    'value': 'ϔO˴ıѓԑʕђБǏ½ΣěˏԝsʶӫðQϤѶґ˨ӅѣɡKɠћ',
                },
                {
                    'key': 'ғˢџͶȟҨϕßkéЭü\x9cӭhөʹѕ',
                    'description': 'νͰƸҏӖӼϡĂŇϳȮў˂ӕԏϛχ:āȟĘɎǝʇWfȾ\u038bŞԖ',
                    'value': "΄΄əԜҭђҬśƙǲĸȸȏʕЊİO'ʂƵ˟ϏӦȐρҿ\x94ԞÔ˦",
                },
                {
                    'key': "ʂû'˫Ν˟ϡԎВɐƮγҨŕǴˎˈɈĿǗÐΚѨŊLţʭƾǉ͵",
                    'description': 'ȝҺț\x9bÞúЭgô˝Ʀĵf|nǈΨȷGЗ˙ǽȉˮѝˣ˼ƥˉż',
                    'value': 'φҎɴƳĕęØ6ϑЀĹʃх=άʭƔVЀŊŨіȠ\x8bяȰ\x87ӸͲέ',
                },
                {
                    'key': 'ɍ>ҥ˟ϋз',
                    'description': 'Ҏɾ\x91\u0382л҂ƾϨĎœˏÆČǛέĈ$ɶǻ\x88ƌ&ќѡЦ·ҪƎЙj',
                    'value': 'T¸ӁɯǱ¤ѹͷƙɐ҂ɱ\\Ίɭ\x96њȵҌίϧԬћɋŠ˯Ӏ¤ț͵',
                },
                {
                    'key': '˙ҵϰśӴ\x8dʥɎŜɜţБƽƀ_ˊæU\x91ǭƟſĖĚ\x9cŤт\x94ϪǇ',
                    'description': 'ӈɵÎǡӡŠIԐ˾~ΏŅθђўǜӰȮÊӖϱ\x9bԦɿҖǻhŕӓо',
                    'value': 'ƒTɱΎƂͳĆȥǬȴōÎ\x87ȊǜyƀƅЀşӚєȎʷ˭ԧÖ˺ҙǯ',
                },
                {
                    'key': 'ͷȽЧˤ\u0381ϕV\\˼ɭ',
                    'description': '5Ι\x87Ӑ҇ΫԭӯԧӺǢѷŽȒ˼ċȗӏӉǝћ£˵ʺͲΝӑ\u0378Ɛʄ',
                    'value': 'яδӁΗΤΚOҺͿ҄ӐԮӂFβɃӜ',
                },
                {
                    'key': 'Ԉˉѷ\x87Ҡˌ˞ˑ%ˍ/-ӮЯ˵ƩȕʇȄÚŉƁ҉BŅŧfԈӌԃ',
                    'description': 'Ӿ˲ǫʰ˵ǐҷ0\x91\u0381˟υ˪ΪҙÈ\x83ЭϝɤǜƻŽђǘsɌƙ·ʧ',
                    'value': '>ъȨȬǷ¡\xadǮʴ}йɚ\x9eʮ҉ǋɞǡĸāђˋƓȸƹԈΨϝӂϒ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': True,

            'focus': 8908,

            'location': {
                'x': -151722881079837295,
                'y': -8534406652157615405,
                'width': -7217587088291739537,
                'height': -7251826014966742587,
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
                'focus': 5936,
                'parent_id': 'ǧрӧпşūżȒ˸ŹҩșƷԜƔӂѧgщŝͶҿɁŒ\x84˳¥ĝuǓ',
                'location': {
                    'x': 7794211691227699670,
                    'y': 75129742595558217,
                    'width': 3854389657936627948,
                    'height': -4896792915077034550,
                },
                'minimized': False,
                'meta': [
                    {
                            'key': 'Ȃ2ȭ\x8d˚§ȇ϶ҞȧRӯԗѳmӯԈt·Õγʑȕʏ\x97Ī҈Ƞ8Ъ',
                            'description': '4Ϭ\x8dŲɍŻԁ#;Ң˒ȟiSƽЮĨŉΞǥƴ0ÒϚzó9ӟǉл',
                            'value': 'ҖƴҰ˼\x8dUΊiөл"§ϮϏƪ\x88ЄɸÄʟěҡѸҨ\x91ʶǐϞѓϛ',
                        },
                    {
                            'key': 'ʺƥˮŇҗĴBŏΚ˜ӿҬÕEØǮңƙÛȜʟӮѹªÆ\u0380ѱĆɾԭ',
                            'description': 'ƧNԃайȔЛϾ=ǴRɠͳǅӯ\x9dȃӋӰɬӥЋςĄʈφНӞΌƝ',
                            'value': 'үþЕUԚӟ~ǃȃϑʭ\x80ϴь£жĖǪʅω\x9eƄЩЦì˟ʢďôȠ',
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
                'focus': 5981,
                'location': {
                    'x': 1016617821301181465,
                    'y': 3061418033401141931,
                    'width': 4611523826891250452,
                    'height': 5252932361179183431,
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
            'reason': 'ŗUΠϊżТ\x80Ӫ΄r\x8bįӘƾиѺӘȌђΘΉҹĤųӞЗӨõ\x89Р',
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
            'keyboard_focus': 6495,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keyboard_focus': 2373,

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
            'window_id': 'Ŕ¨·LцΌưǑȷӿÔã0ƙǾǝΌέë\x87«ėˢйĉΝǄ©ʕ\u03a2',
            'location': {
                'x': -7670582947952902184,
                'y': -8856244491881729545,
                'width': 8481736630332503096,
                'height': 8970329119118366879,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ǐ3ċӣӏ',

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
                    'window_id': '\x7f\x93ҎˇӱÞρҗʪͷҮԆëͷҶǬǆɬǸͻ®Ÿ˔ɱԨĆҋŕƍà',
                    'location': {
                            'x': -5846164090253807906,
                            'y': 8219412212898741768,
                            'width': 6537908648534705189,
                            'height': 4979771283411743133,
                        },
                },
                {
                    'window_id': 'ӗчƀ(ƆïǻψȣɞǁәБ0\x95ǘǁŀˆ\x85}҃ȣұ\x88ÚƖǙȃĖ',
                    'location': {
                            'x': 7952778086546969524,
                            'y': -302433149176898763,
                            'width': -2264458927561988949,
                            'height': -3276364052074496068,
                        },
                },
                {
                    'window_id': '˟ԁɚÚΙ0ԋίӷͿѵ҈Q\x9eІСԌѱыҏѬӋ\u0380Ύ\\ˆϥĵɷÉ',
                    'location': {
                            'x': -1628833707458796669,
                            'y': -3583356482826233585,
                            'width': 6113244633588307927,
                            'height': -7382703634714275151,
                        },
                },
                {
                    'window_id': 'ΰϾ*ěӝ\x94ӶƲɓЪÑɸӡҩѧόhšˮͺőͲúu9ђƱͼ\x96ҕ',
                    'location': {
                            'x': -4622420929107725658,
                            'y': -6021795178557479177,
                            'width': -2412147234294905339,
                            'height': 8357755277084355970,
                        },
                },
                {
                    'window_id': 'ņϞÝǤʺԂ\x90˂сӉԑÉǑʓƊχơ˷?еϝҞƓΌˁ<ƒ\x87Ɋǹ',
                    'location': {
                            'x': -8454868134313344628,
                            'y': 6634653614260134459,
                            'width': 7319347102407843387,
                            'height': -4136881885828970901,
                        },
                },
                {
                    'window_id': 'Ԋ\x8dѣĥЋуЗVɫɥˠΖΓʴΓÿů¼FȴõȠП.ʣĒɂǏ˘ӝ',
                    'location': {
                            'x': 2122469762803778993,
                            'y': 5633362064106836097,
                            'width': -3628153512326936886,
                            'height': -5634492570050764647,
                        },
                },
                {
                    'window_id': 'ϼȵϕԪӳƼѣќ˫Ǳ¶^ǞҽÎdˡȞġщ:ɾѸ\x80ɓԑЕHҰP',
                    'location': {
                            'x': 3404018625091691307,
                            'y': 2275344710852347193,
                            'width': -5578467518804016541,
                            'height': -8019399734422332304,
                        },
                },
                {
                    'window_id': 'ĳУÏͷ\u0383˾WѡĴłЫԋΰěԦҐˊͿÚžЉžЌӄʓΩȫăɮТ',
                    'location': {
                            'x': -4454230770628437520,
                            'y': 3724481874013313657,
                            'width': 867796707245734018,
                            'height': -8037514212620631466,
                        },
                },
                {
                    'window_id': 'ʺԢǫ¬ÝɋӝżČа\x8e˸ӄňĪÙќÅѫԉáēȃϢͼѤВȾ҇ӕ',
                    'location': {
                            'x': 6403587452752347144,
                            'y': -2811318618246261185,
                            'width': -5432206734827825447,
                            'height': 2454172061532843043,
                        },
                },
                {
                    'window_id': '\x81ŔΒȢvɍÀŌԋЃ\x88ıɼԀʎɝɼəФs^\x93ýРʮг\x8cǷ˭½',
                    'location': {
                            'x': 5717069716596854123,
                            'y': 7586042746466117451,
                            'width': 7963282539468180261,
                            'height': 7937694299354018196,
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
                    'window_id': 'CʉώÌ҆',
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
                    'key': 'ԒԮцғҝЗЈԓϯ˔еyĕӥƇƏɉӹиӷɲ',
                    'description': 'ŠԖκʯ«V°è>ƠŮќǽҥˆˮòϫŝҳ\\\x8f\x9bЅĵϸĝˬĀѓ',
                    'value': 'ƬȅѾʴѾЖĂ϶PԏӃΑҩ®ѱȎŝҵӋǃǆЏίɬʘÙÈ΄уϳ',
                },
                {
                    'key': 'ƆĦĦ˖çӻ\u0383͵ӣȅјǀӇѳͺĥȭФ',
                    'description': 'ѣһǆϠĖȴŘŲϛĀʷʂӱƲȢŊȻʷҏНƜm\x90˒\u03a2ζο҉ԩι',
                    'value': 'lгŽҶȠ#6ÑԜʚĕϐǒă½ϯ\u038bңɏǥ±ōƊϬȕʱ\x93ȑϟĵ',
                },
                {
                    'key': 'ūϫ\x7fιoЊÏɃÿɘ&ǂéҪʥɆԖóŤÆėΚԭОӠ\x95ŹɌʹÒ',
                    'description': 'СóЋЉѱŚϗmȂȳόʑʳƓ\u0381ŷ\x99ɾŪѳɪÄ\x9f+ЖȠǟʨѣά',
                    'value': 'ÞʎԙƖ$ǌʴŵēŦΌɒјDăĬǁϘk\xadbΗŲѷϠÐmϭǬτ',
                },
                {
                    'key': "ԐâǾҫәȘԕȮȳÐȖҰʦҪʶи¥ЀЌЅĘҢӷɆĆǏɼ'",
                    'description': 'ϨʜˆWКǿvчȞőĝˑνȜүǹsˢTʞƻ˨ÀR|Ӕ$ϘчY',
                    'value': 'ϔSŉΡˆЌś˦ƴȂƩǦ\x88ԠõϪpϩɺĎĮ?ВԏϗͼʷƿΖΡ',
                },
                {
                    'key': 'ØƢѲǁ»ԬǄYΌɺ!ӛǥ\u038b\x9aӁӢδюҠîŇ4Ǆ˖\x84ŨŻƂõ',
                    'description': 'řЗΐ\x99ƽŔӺе&ѵʧqιϿӝƁȫĠӐÏҿω˔®ӮʳζѬƪz',
                    'value': 'Ţӌζɚ˒Űǽ+ʽRȰѲ˛ˡĄʊϯʜԐŜ~҇˨ǃôӄъӱˬӜ',
                },
                {
                    'key': 'ʪʗȬȱǆө´nŒѦ0ɡРˇ&˒ħ.ΥвǃεϑȤʚΨʰƘʓʁ',
                    'description': 'ǖŠƆнǐψJȭ<5éҫʯƒɘԫѵ.ћ1ǴɰчΎԌŐɒƕˢɹ',
                    'value': 'Ȣy˻O¶ϕȲƺÈźªǷΎʀ7ъ,ɼ-ǣĽ÷ȌҋĵśΖųɵϞ',
                },
                {
                    'key': '˛jǘʊԏȒJɍѦyҧĈưΗyʒĭ\x96ͻȻμʛˀ˼ʓ',
                    'description': 'Χ^ƶɆ˨ТVšǫ®ȷpǙ\x8fŮДʵуԒńяȄ˹ϛƅɅ͵ӰԊ¥',
                    'value': 'ъėʸŒӉ˂ъǒĶŶ\x93ϢØҘϑXxϒĉФƔγ³ɂҶԙӋϖ˖Ƥ',
                },
                {
                    'key': 'ʣǘßĨǜӺŵɆςƄȼ\x99ŐҼɥ˾ѬšŉðИз°ɟąԆưȶ_ŀ',
                    'description': 'ĲQϝ҅æͽ˸ӑϕǋњұŪƖ˞ѿÿȹµЗəюӾ\x93ž˖ƿѫƺʉ',
                    'value': 'Ѡ4ƯѩÐƣѯҚЋˣ7ĖаѕԄǀΟǃǼoÎϼѪ\x7fWƑEԓʙƯ',
                },
                {
                    'key': 'è×ʰņƜ5ēɸȷ\u03a2Ӝʺ˻˭ʇҟǵ',
                    'description': 'ſԐ˚ϺğY˦˗ÿɭĩŘўë²ԨšѦʕʝğĦԋĿӺǠŋȃȤ΄',
                    'value': 'ͼԜюҥϝ˅ƒźÖқ϶ʮέʚɔяʓӓɻʐӑP®£ЅσЫňʟԩ',
                },
                {
                    'key': 'ӫ҆ŌǮŒТˠԔΈǕƿȌxϛѿɞǰʇИ;«Ç˖Ӊǎʭźʦȥɠ',
                    'description': 'Ӈˋŏϰкĵ\x9dàЍHҘIԟǒȨӉƺ҂\x9f\x94əûʀūĲBǸϔe\x9a',
                    'value': 'ΫΊǽçƂαȕťȸàʜϥȐğêȉѥǔͷƃ\x8fXìĽɊńƛӽѭе',
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
                    'key': 'ʀԫ*!Άӱаɂ\x99ʞƠȖεҒô҄ηϳǆЩűҁŘʜӦŒЇĢσɢ',
                    'description': 'ȐξȮÏҳƺɣÊȓϪΝʮ&ϤΉͰϽԮȦɾìδmřϖ`ǪhχӠ',
                    'value': 'Ƞ\x9dːoҷ»čǶπԮϺθËɢʶŢΑʁСʵȳґɠ7ӍɨҴTԜ҄',
                },
                {
                    'key': 'ƄϲoҬʎÏϞӐҘ/¨HЍmԊˋǐʌңǧčҵӜҪʗ',
                    'description': "˘ђ҅ԉҝϧʿΫЉãʃÀ҉ѹӶ\u0378ǪҴï1ҲǑſƸα'ʅʪĢ˱",
                    'value': 'ÞІǹӻăǙɬӺӹ˓ľǹѯ҉ȑЕнЅΆӗӶđʵĹǲμ¨ҊϤӋ',
                },
                {
                    'key': '´ӔϪʦҦяșʴ˯Ȼś˪еьԂƞʿɛѠ%ʽǠә;Ƽ˪ŽǓӡς',
                    'description': 'SҖʴ*ʦƥӗԥøǌɖÈԑiӹѫƌʜ˟Ɯ\x88ËǑҭѣʁҳ=οϣ',
                    'value': 'ɩħћѽjȭĲĵЁΉ0мӀɎѯΰ}ʀʨÚĥŤǏŭɿҦЕœŝm',
                },
                {
                    'key': 'Ӿ˄ıЙӗǝȃԢη\x86ȀӃɐ',
                    'description': 'ϟ\x91ԛˇƽʁ.Ј¬ѨÆ˩\x98ЙȑʝЫtȟˠ:ωЉ\x8aʤқŹϺȴΌ',
                    'value': 'žϽǻĀ˽ƃƬӽқ8ѩϨΚâƩǕƢ҆ЙDƲϔ©ÂɋʫƔǉśѪ',
                },
                {
                    'key': 'ӛ',
                    'description': 'ǕŘ{Ѿ\x99ƪъȉɹԬψвɭԮϓʑǝ¹ĉфŤϙRŊǞΣҘ҂ŀƀ',
                    'value': 'żÏPwƬĐҽ˸ŲѓǛĨƚϏѻдŵ\x83RԄɱƏʺyʩžЄсЗ\x94',
                },
                {
                    'key': 'v˙ŧ˒ĢϳÐĹȡâЎĹɟ\x88έŶΜӬϞǡ˪ɿҾҫί%ʣаǋǧ',
                    'description': '#¨тҸɎΆӥѴWşԝiÎčϰӬԂήΔʥĬȂԜɂΦɶӺƿ¾Û',
                    'value': '҅А˸ʫĴ҅ΓϜԊԢkː˲ʹLj\u038bƺʻ\x90Ǆƻόв',
                },
                {
                    'key': 'ʽΏŶͻ0πѡӃɟ²Ű\u03a2ШDʂǪ\x9eͼȊуwЦ\x91',
                    'description': 'ƻʋ4ˢBη\x83ϵ\u03a2ԠϠͺѮš҈ϚΟɚˢƘЩ-ūʠΨɊœ|ɀʾ',
                    'value': 'ҍԕȒˢЋшɝЦ)ȠԤɃ΅ЏЄ\x8aԄу#кӛԟяţФ\x96βîťҕ',
                },
                {
                    'key': 'ĈВĚʠжʞҀˣôћ_Ǹ·҇ҺƿʒƮÖЙƏӝѶ\x9cõʞҿɌҟӬ',
                    'description': 'ԬMϐęЫǦƽǕvδòӦƮĕƯȢƉУϢ˸ҫҫҿ\x87\x8dϧŨΎҁЀ',
                    'value': '.҂ǁǽҳԘȫӠÙŽǝԔȊʪжV\x92҅ϣ£ϯú${JЅϼȸŦʋ',
                },
                {
                    'key': 'UÔԅ\x9aʋяљ˽Ǯ<äëёщƍgЀĉωȥɪ',
                    'description': '\x8dŕʹʬп^·əiɴ\x9aόʁăҐɊӐϫɔǭµWНÖɪøΎϮxÌ',
                    'value': 'ΧˠŨЛɇϮѾȞū(ʽƘɰɄ\u038bͳϘϗ˪ϤɔӮȹѢψ˃ϵʐəƼ',
                },
                {
                    'key': '>˚JϓȪũȒԊΌ?ǆѷõκϝΝӊȰʶ˖ƣȏ',
                    'description': 'ù\x93ʩĥϼ\x86ǒЪѠnҳäʪΧДуԌΖ˨»ȉ£ҞєÄѷϠȲԍЫ',
                    'value': 'дˢăȶĄԣʣѳʄƃʰҖΠαƉӟjȟӳðƟŢЂȰʰѬ',
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
            'window_id': 'ɧćšϨΤʔƗІʱɬaǓ×ӛƵҍѺ\x95ЇǊ˞ɜΨчȬ·ίĝԌ ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'Ł˧ƕΤ;',

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
                    'window_id': '5щϙòΠ\x9cϏΦ϶˥ǰѺͷɊȢϜγʞɾґėɘR\x9bˌɜѳÄ˱ʶ',
                },
                {
                    'window_id': 'ĎΔѸʚмӮЌĞÂÙƛİҺɞɾΔμʶɴԌԮ˜˕ʪÁɽȂλʍì',
                },
                {
                    'window_id': '\u0380Ѥˤ#ЪɔψϫԠēӢʭ¦ȚЏëӪЕϼӲάҳГѭ˯҅ҟ{Ȁ҅',
                },
                {
                    'window_id': 'ӻǁ҉fʶñΧґ¦ξ+đӨˎ҈ӯиƲӓâˤęĄɋƳǼԐÃӌƺ',
                },
                {
                    'window_id': 'ΑȍǕʱǵĜń²щǜïʩ˩ͻͱЀҾș´ĀVˡө\u0378ǸʩʾϪǮҩ',
                },
                {
                    'window_id': 'УʥчǒˍΟԬͻŞìɌvԦӤϺƵϐġÃ˼ħҶӚȓǄҢǹ\x8aƚó',
                },
                {
                    'window_id': 'ʵIϟϋʡʴeΊұƎȧɡ˺òσҠӒϽ%\x8dɦʑȮǢɮʭĠϗυӬ',
                },
                {
                    'window_id': 'Ǉѝ\xa0ЫϺ_ʜ˪ȳʈŴ[ƬҜԞÁĝԟԝhǲѶӴ\x88κcĤϐˡИ',
                },
                {
                    'window_id': 'ӄǖϭɪғʣς˃ǵԚԕҡЁƭȿǉөʂˏμ¢҅џǕԟĨ\x8a\x9cƯе',
                },
                {
                    'window_id': 'ʝżЭƌͼÁ˳Ϗ÷ơјůɢѹԤϮϞŦвϦâˌЖçȣрΪҡƏț',
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
                'ΛXѥΆǺż/ωůaъͱǮ\x94ΘОӾɰѰŔҡԣѧɆÛǬħú\u0378Ӥ',
                'ǿƹѲÒȫ¤φʴ¼˱ȡțӑ$ʯԀÉ_ӥʰ\x98ȎӡԙŴͳ҂Ўˁė',
                '˛ȲԎ<\xad˘Ȣ4ųҐӁȊɀɹƪǯϪ҅ŃɢҶđҪ\x9eϳƱҗôӁÉ',
                'ΡӹςǖҨЂө˂ҧǩŝʔȱͰZȈˉ˼˵ÂЯǝʂэǝюʛɑйɈ',
                'βǊԌʇɟ·ɰvȅʑʭǔǪɎkľЌӫҚ.͵ȢЄWŅŃѺѬƣȵ',
                'GΜƻťƠƷÔšzәҺ˻ЛУğĨϘωЖӌmϜɻǦԍӘɆD҅ί',
                'ϗ^\x9eΆȚǙßѝͷǤm˘Ӡ×ϐĴϧŨƁ˾Ț˼˯\x9cԖԍƍʵ9Ӟ',
                'Ђ\u0381вϿåͶœǭEƮ>фǪɑɼēˆƧџйҺϿµɾθǘӽ\x94шё',
                '˒ǙǺҳ÷ȚҦˡԭЍɌʈЯZΗ\x99ԝ\x86ԔƒΙRƕӧϓεȭIʏ\x9e',
                '8еŴ6ǦØɔȺˉlŰҐԢȼԨMӐωŊʌ±ɦɘƐīůɔԣΎа',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'ӉϝбȟЃ',
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
                'focus': 8904,
                'parent_id': 'ĖŬİí˱\\ɄӄɧӓŤѼȨɖŐčǖ\x8fӵʝʶϠΣøʯŖƢǬČͶ',
                'location': {
                    'x': -3437401661722063779,
                    'y': 5701192272749489052,
                    'width': 6559035652873319188,
                    'height': 7157878371360000064,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'πơϡˤʏYέΉŐǲ¶¢ğɋїǐ¨°ӾǫȼƁȬԅҁʫԂ½Ǘb',
                            'description': 'îϭȣǞˡȉɋш\x90ϡǀġϧɠɺξ@Αˎ/ɺ¥\x96ҡͿĩȄʍґ˺',
                            'value': 'ĮΫ˹7ȕΫѶaϱţўǺƲǋĢǤ˂ǈїƨ˷Шưϓъɲ\u0380Űˮӥ',
                        },
                    {
                            'key': 'ҍэџƴӬſÉǺԧ\x96ŖŸŁԮĺŭuĒ¹ĴȅďχѵyŚԏʿ',
                            'description': 'ѾƺϧԈǍЦƚπӥКŔʉ%ŋĝВƣѐtɛѓȅчƒʝÿӚҖˍě',
                            'value': 'ԉNӢ\x9f_ƒϐҰΆsŹĨ҈цϬĢԬGɉԤЉ˦ƾϹͱʘğϘÐӎ',
                        },
                    {
                            'key': 'ɵɀԍϟɭƬӚЏǮɁçǡɐӸșʃåҲ Ŧ',
                            'description': '˖ԮāÙ҆fʩÊäˠκӇ\u0381ӖTĞ§}ƒԓ˓ȵdҳԋйΦѣWï',
                            'value': 'ʶŚ6ԍӗїʆÝkɠӯάџ˺ãƉ˲ÈϜыϦʴΆ\u0383ͳɦˮɉш-',
                        },
                    {
                            'key': 'ǔҊǁ÷Ý©ζϩѽ҃ʚԪ®ʻýĦΥϔюȹOθȍψ\xa0Ŵh˓ӸӅ',
                            'description': 'ƼњΉʍȔϘɿԮϔňtРӸǝҟԙ\x9b\x9aǽíҿĭƥʀЌģЁơ˪x',
                            'value': '\u0383ΈƷ΅¤ԗӘԔ˦d¼Ҍѡʪ\u0378ȜӬĂʵѺԬӼпњ҄ΑͻϸŔǞ',
                        },
                    {
                            'key': 'ȱçÛğ҆č',
                            'description': 'ѧťŉυάrˏ¢Ҕ\x85ńϯêӶ˼ʟнØ¢˅ǟ˽[íʗʗȜԇΧГ',
                            'value': 'ϱέ¶ɿʅÓԂύ˕īĽÎǨȑӴ˻ĬѲɝҫԑÍʛ˜ŃңӇ\x9fƏӂ',
                        },
                    {
                            'key': 'ŧιȹʔТǨĬǉͻÍʹĚ',
                            'description': 'ѼЏцȿŢǊкǳîӾ¼ŷ½ʏɹŻˍÒċʁ2ˠ\u0379ˋҤź·ĢɴȀ',
                            'value': 'ӒʅƏ¸UgÍТЬͺ=ʈћŘșӑɟɣфƯγʙӁˡ«Ѵuϐɍŷ',
                        },
                    {
                            'key': 'ƫѤϨˣӓƈӚҘќ',
                            'description': 'ĪǲƑΕΩ\x9fԝҡƸʙʢ\x80˭ѷфǕ°ʞϒҾˢÝΝӇɤӒǻȢԠ\x82',
                            'value': 'ƥΨѪαǨʚџȪʯӤΝϾȾϽΜ@ϖʘ͵ȇǵяɕԭˀѹ¬Ӓñə',
                        },
                    {
                            'key': 'ŔøϩϋɈƪе\u038dĖѡЬƨ\u0382ҡώшԙŶ\x85ʅþЬƞ΄ǆĹƋåйƃ',
                            'description': 'İҜŗ˵ύ-ԇØΎcOϮ©ŉөǚǆҍəʢƪпϪøȤҗǙͲ©Ɲ',
                            'value': 'ЁȈʆԛù˟ϊȕɜ;ˆĻtĥӳ4ʶȑсҺƍhèѡоƁʢă\x9aʤ',
                        },
                    {
                            'key': 'ˌȵ\x92чԠÍǛƹŊϧ',
                            'description': 'ʙҕԣ!ϢӺʱΈГƍƌưǬɨΦϻԂ˺\x87Ŏǘ:ǉƃͿΓχŦǡы',
                            'value': 'ˍͱ\x9aϖϺΪƟəԦ{ҚƎjɮɇj7ԟԩѯɿĞνɧďŐЃԫʃ\x8e',
                        },
                    {
                            'key': 'ӊԐηŁйĬɳTƪɛȳȲſșӟϻЊ˰ĢˉęΦǝ',
                            'description': 'ϰȃɆƒľʄχҳɹēГΗ˰)ýέǚоΐËҭǄ˰Þʅ˜ɎÙīɁ',
                            'value': '\x9dƁľáņҋɺϔгʰѱҳ£ҿ:ŁʎƗɐƛ:ɷʤČŁȆЃģv˽',
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
                'focus': 7988,
                'location': {
                    'x': -7481083558414801,
                    'y': 6041093498285537050,
                    'width': -4978225830132972717,
                    'height': -8031959385550380638,
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
                    'key': 'ƈÔ?РŔЦěϋƝǫҞÒÚǽRëPȬөζҝȼ',
                    'description': 'ʣʥӦʤмÊɰƗĥӵ\xadΌѻČ\u0378ʛȿnѪӥӊľБŘ\x82\xa0Ǟŭͷʐ',
                    'value': '©ɥϸшԍÃŁ¸ʚԕҳϴǑѥԓԊƞǸʒąӬӐЃĥ˲θǷēƿˌ',
                },
                {
                    'key': 'љЧɧ',
                    'description': 'ȏƖƱγĵŧɾÀ°ĞɘӭȽ\x88îϭċѩЎÄӐÓƩŶӼɼĦЯɿҽ',
                    'value': 'ưˤєĲɽЉɑѝŶŋԨɴȯȅΤϭԣѾôˬʷɥ]þлҦƶƊЧţ',
                },
                {
                    'key': 'ȧŏϸҶãăţ\x84ÀѨɃЉȹ6äwьĠĥÀąχĭӏ˳0Ǿº\x81ћ',
                    'description': 'Ďԗʊŧо˕ҘίҒȞǄnĎлрŌϺԙЀŀưϙԎӓRӈeƭѯm',
                    'value': 'ёʧʠԊÚȮˣƌҤΉӊԐǸėűȟѼԥ˥ШĀʹȲΠĎŞɤǿԩĘ',
                },
                {
                    'key': 'ϿˮʃMЏƞуԁϦʣįϽѵʹIю4ԞǂκǘɾLδʙņԋӶȚҚ',
                    'description': 'ǪĎ\x8dѳϦĈ1ʧϊΫԝͺҡõȪȝ\x86ϺͱǢzʁɷΖEˏјԓˋԊ',
                    'value': '˼ϔʽ¾Ϭ˾ёΌшѡГ\x95ŨǋσӣҟЍ«ÊδP˾ɺϲȇбӤɁԝ',
                },
                {
                    'key': 'ҨҭʨÀťԛѣŁҥɅӟKğŎǶĝԒʂ',
                    'description': 'ϑмȸЊ4½ϙӥˮѶ1ĆʞƨƉӪѵǪϲϳѽĤ©ʀ?ҭǂђ˪Ї',
                    'value': 'ƌɲðĴƝтȺTɬǏΘϸȮ.Ȥǔ\x85ϥ\u0378ŊUŨǋ¸»ȌѲɳт\x83',
                },
                {
                    'key': 'р',
                    'description': 'һʰeυҿ\x90ӄʷӑ\x8cρΉӮǂŲǌ\x97ЋǪʂҵԑȕɷƼѧеϤȉԗ',
                    'value': 'åʯӴѱĂǦŵĆǀÕ.ŌҽŅĿȎϢņǵʉ.ʶǺȨǆϸӯϞ˗Ҭ',
                },
                {
                    'key': 'ԙ˘ŦʕʵFŤ˞ɞϤ҄ƔİӉͽ˵ɔŹ҄\u0383ìѧĞԔƛǍҳȯ\x9eӃ',
                    'description': 'ɳÈԒШӈϰυέѲĖ«ѮǲʌӈϱȀÃϘÿ£ʼŴɺԆHXҳөӬ',
                    'value': 'ƢǰÏ˫҅ǿƹӜˈэǡΉ\u0383Ͷɥ\x88Ťϣɵϧќç{˹˵О1ӃͷЁ',
                },
                {
                    'key': '·Ƥ,˳%ɺăkѦҽ)ƂҖ҇ƥψÃʔĝȀŖȮďǨͱæʙ·ʅΗ',
                    'description': 'ʮǫΊ¾ÎʹίҲŸǝОӁ΄J˯ԏϧĐϵϹˉľʟWԍʵԃɯΐԂ',
                    'value': 'ʘҦŪҥϞϞɊҋƟɣʷѨʧşίȳѵΩǼлцȔ\x9aӮ\x99ΒґԟҲԜ',
                },
                {
                    'key': 'ӯӅ˾ϫͰӊѬӖҰ',
                    'description': '#ļŰјжŐńԑɥЄӫơɍɶȞғӖ˱ϏcԅǞɌǄѴ\x7fȩЙŤĠ',
                    'value': '\x9bêҙȒȨȧѹҪƼŦ:ӼȂҎϢñöØɷɺЬ',
                },
                {
                    'key': 'ґÄģӎРĝȐɆ',
                    'description': 'ЇþMƻԗ~ʓɾˮȷhҖîˬϲüʽӤňȕ_һȝĸ\x86љшкϬˮ',
                    'value': '҉ӂԔ˪˴ɝǝ]0ǚˬůɳŭɱϥGҝʾƩcПɮЙɞΎˠħƒŊ',
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
