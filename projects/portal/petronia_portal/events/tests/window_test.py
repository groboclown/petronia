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
            'x': 6174530046666794220,
            'y': 1504701799727108980,
            'width': 8964041881289199841,
            'height': -8369389700362880480,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': -2745056205754344570,

            'y': -129584473263163216,

            'width': -4570575248321411361,

            'height': 9193200610567497859,

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
            'key': 'ǲΐ?ӞϭϡƌҚ\xa0',
            'description': 'ϧȅƀɌӋƎȡǷҕȼwũH˷јԁȨ ͼʄɬŮ\x98p˥aԑţb˞',
            'value': 'ҫӑÒȕɺԧƧōȚȲǨοԈǡдϔҮõҜé©H6ѸϺΛˎȻΆÔ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': '\x89',

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
            'focus': 5026,
            'parent_id': 'ѦӠ>Ӳѵ%ăƺ\x8dɂʃƈΧӽYĬȩθȑ~ϙƉфɓ ǋʾdЊ®',
            'location': {
                'x': 8668535837096744452,
                'y': 5037031097609749840,
                'width': -2535793781866052419,
                'height': -1880766188616436039,
            },
            'minimized': False,
            'meta': [
                {
                    'key': 'дˑϾT˙ƧϗΔȗB^ζŝ҅',
                    'description': 'ĨʆӓjĜŦǉѧȫЈ®E¹ʠāʃǃеDШӣ]H˧ЃGƂǌżϑ',
                    'value': 'ϖΣϲ˛ɼϫɩѡ˰øXːɻȶɍÙȃέƪ\u038d½ϙǃƆůχţξĥɆ',
                },
                {
                    'key': 'ЎʼîVʵӇ/ԑԂѥʋҝͺʪȜ|ӕʾԘĘҽƍƳƙԧǬºԦԀа',
                    'description': 'ǅ˛ɀӾПɍĥȢ˫ǕȮ"лʭͲä2ƕΒƹЕҍғȃ}ԀȇЫӑӁ',
                    'value': 'ǚɮ\x7fȹŉ\x9dӰϗȘȬΨ˞ԬіøȮĂøGϨɂµѫҌӮˠ˚ξǂ%',
                },
                {
                    'key': 'ѫʠдЍÉƕɁϔұˡǌόɶȵũωʚĽ',
                    'description': 'ρºɿðЛ±ӗЭоЉӶȌψWϵ~÷ŗќͷˇѨņǄЖҡd\x99%ȯ',
                    'value': 'ɴԚƕ5λβ6Ȳʾϣe!ҖӕѮʧǰĽҶϳԈϡŶȠȮϊ¿ǪΌψ',
                },
                {
                    'key': 'ĂǴϼΗʯàЏ',
                    'description': 'ҫºұ«ș¸ÖȁÝңǎЭӟӅȨ˫ʔј³ʇҋǖċȝЁ͵ҘǆmH',
                    'value': '\x97ɬΤɍ©ȵŵϏɃϽǊŵԗʇΙәΛqǃ҉ίљόƃԣǜӪȽЊΥ',
                },
                {
                    'key': 'ξŽȑƦ˅ÛԙƵqʷМЋ7ϫ˩ԕ\u0381ϱơ',
                    'description': 'ÏʭɱǶͰƬĤ:ԭAņļэʧΧg\x9bԩԏŐȚ\x8dʠȶϐяҪˡɊ\u0379',
                    'value': 'Ė\x88Ҩiɉʱ¦Ǒʟ9ɩǋȲ˳Ъȿ\x86ԂΎγͻ\x83˓ϫQǞңɴǚӒ',
                },
                {
                    'key': 'ÐԋӟӖȃƅӡңґ\x9c\x81Ĵ҇ҰŗÙԭȘŖχ',
                    'description': 'ɴƔNëňʍʹϝѵƃĤĕǟМȖдϖӶƟԃϽӅʁƉҙϗXɏԢͻ',
                    'value': 'ΔЏʟʹѮэԈųœҨ΄҂\x88ƙǧǊąũȷʊ\x90˽Η˺ɌÏөЈǯƹ',
                },
                {
                    'key': 'ҞȬãҿ\u0381ήлˣΦԅϽñƖхĮӼ',
                    'description': 'ԊчƂÏǞɓ0ǞƂьcßÔŃčƤȂӸάʄǴ˴ɬʜѠÖԏąΛӂ',
                    'value': 'áЍkȍ¸ϛĻ\x86ʴ˺ЎŎƵЯǦȋѳͿʼѻɳ*ɡǉƵňʯǉ®Ʋ',
                },
                {
                    'key': 'ųӱώƕʈҹɃʞ/ȰǒӅϵʾºŷ',
                    'description': '҂ψȜȶѳýʗφƲƍʩ\u03a2ΗWŴɵω¿Ӧµ\x84(ɶʻɳoʣИϋɪ',
                    'value': 'ōſωˀǠuҽȨϬаʷƒԮ˥ρdńФ\x8cǈϩƦ˝řԨɺΎҫfȭ',
                },
                {
                    'key': 'ƥҼ¥ǋѐˈʭŘ˘*ʿЍōСēˉ\u0381[jԣˆȧWӷİŧҟƧʒ\x90',
                    'description': 'ǒȔԭӡʑȓʵɅļЅϵʤ*\x9eʙЮƥ˽˅ΟȚȀʿŦЙӯĊфɗЗ',
                    'value': 'δδŚԑ#өņɆăЌ¸ЇͱȤҐг"њɏĚʅǋ˶ŝϭċ\x99ÕǨš',
                },
                {
                    'key': 'Ԡͼ\x81ӑӢϚφӈ9ɠɅǌʝŁɏΙĉ)',
                    'description': 'ёҕƜǣɡĄìǈхõˬήʭЀƈѧ˚ϔ¶ɭƪǿĉǸ5ё\u0378Ňİʏ',
                    'value': 'ȴÌɢӺƏʡȅϒȂµǚ˺˙ńZЃЇ΅ïƈnʛŕ˅ȲϢįϾȮĐ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': True,

            'focus': 637,

            'location': {
                'x': 6135118565851852620,
                'y': -7977229385298628220,
                'width': -464422511395721312,
                'height': 8449328346090351391,
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
                'focus': 9752,
                'parent_id': 'şΉɄԆƐÞĝ±ЛƷĢf˵ǊKŔφÒӣþʣλԐ,ǂҦ˰ĽǴǖ',
                'location': {
                    'x': 7921977294603498034,
                    'y': -7629497241732590589,
                    'width': 7168483751959331681,
                    'height': -5739693642839018897,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ƧʗÄMη8˥ƛΒʸ\x83жϜĈπЫƴ]ьɷΝҖԈӁ˛ҬϱǱȐǺ',
                            'description': '1ȍϙ˜ã\u0382ΘŸԖϙńƒˈвő҃ȊĀĸ<ѷϭĉÙǣʚŚȇɃϷ',
                            'value': '΄ЧŸ\x82ҽηǙƊ\x88ɺǣsǬɏ˯ϒǪǷμ\u0382ˈӱĨȼ|рπȿƚǂ',
                        },
                    {
                            'key': 'Ĥԅ/ʲψ9Åsĝ\x98JȺѳҐuеɜ!ŌӉĶ¼ʭǮԓɻOʖƁ¬',
                            'description': 'ʨʯɵȽϲθ7оӄϺCĦ^ĨϰКɭ\x87ҶÂŀƇĭϤʄѾǖǰŻ\u0382',
                            'value': 'ӹƋƐӍɺϭļǦԍΧ§ӳΩǶΥѵԏіºҍC˃ǑkκRӠǑʺȇ',
                        },
                    {
                            'key': '$Ħυ9Ӎɘ\x9cҹʭųԖÂǈ҆ԞǳʈΦӳȮȪÿ˅õȾZʥÎȺǴ',
                            'description': 'ŽSȦŢǶóđ˘тŧɒ]kғɛŕǘȇϵϏʣȟкĪˉ˻ԭ´ɫЭ',
                            'value': 'ĊÉǠȭʑĭϏʹɥşѪΣΪɎǼÓп˹ɜȉϱԣ£ťү\x95π˼ņƨ',
                        },
                    {
                            'key': 'пʜӒxnѫ˙˾Əŵɳ¯ЭԍʤʰǎҙƷyǅΔЄΘȨʤDӶŻԆ',
                            'description': 'ɠǤќʊΉӨƭӰɇЗŜѮҫǷƵǛø6ǯǎҤԎԗѮȑǾĹĹǁL',
                            'value': 'ɧѠèƊǣǠǧԂǲƈˎƹȽχʊҗˮŮŗ(¤ӴΧңƴǳɬҼÇɮ',
                        },
                    {
                            'key': 'ȓȦͲ҂ВԒЃQЃłϑǵӐΓ>ӼDҀ˖',
                            'description': 'ɻԡɸʕ»ƫsÐǮ˩ɌņНŴȡѤΚ7ÞíʻȀƧʤҳƝ˲Ƣԡȝ',
                            'value': '˘~ÐϾ\x9aɆĆƊȬŦѾԕǙʚȑɣ˪ǿϹĳіÀÊǐӻƿѶÈѻӠ',
                        },
                    {
                            'key': 's·àł',
                            'description': '\x80ѕΐӭƪĦǳϬΆɆϽӚɀѴ3Ӎ˔ʂNΊȿԞȦөũΒɥŏɠӟ',
                            'value': 'ϹʚCӗȁŽǭРҔǿњ%úZʫťƂƊŉɃ˥ĒʔϔԔ´\x9cѳԐȹ',
                        },
                    {
                            'key': 'ȘҞ%ϒςQƹ\x9dѲǹǹ\x96ıҽҽòҾÀЯɐšΔǖ',
                            'description': '*ȄàͼǇƦэĝü\x9eԧЋǩΥðӶŽ\x8aԭĺƶ\x94ɯϠυΎ!ёҚǕ',
                            'value': 'Ÿ\u03a2\x9bŭĘ©ɶŮʈǟɤʔҋȡңӼўǓSʀĢΐŎŵώȢıŜ\x80ʴ',
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
                'focus': 9846,
                'location': {
                    'x': 3134895763240941199,
                    'y': -917257025016022215,
                    'width': -5251850467571774629,
                    'height': 2709614689542384556,
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
            'reason': 'ӡĢͶԦǌҝʬ=čÙ˵άƲɨӂʸɞ;ґȚ˹Íˬԫȫδ~ˤˈ\x9c',
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
            'keyboard_focus': 2650,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keyboard_focus': 4740,

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
            'window_id': 'ϻʷ˗ɣ0Ϛ7ɠƑ{ºɫʵ¢^\u0378ԀοƦ¾ǛȪΩ\x8eʅѦҥƩԅл',
            'location': {
                'x': -4164343855811090403,
                'y': -3696182064758122531,
                'width': -4293918979316664670,
                'height': 7761326759445457565,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': '\x91ǼƑЉͿ',

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
                    'window_id': 'ɩƔǡ\x9c˂ÖʐϓŋØƧеѰȡʀÙÅʕο\x93ȖƍÎÄɴӘȝҡӌɟ',
                    'location': {
                            'x': 43226413538474934,
                            'y': 3520336679833691479,
                            'width': -5672411391912312640,
                            'height': -6515980489335345751,
                        },
                },
                {
                    'window_id': 'ʄ΄ʔʏϹœǜϷ\u0380Ï҃ȎjӧʆҚ1˽u¶ӇҏľҎφэˍеʍñ',
                    'location': {
                            'x': 5907363067876692242,
                            'y': 871576119637931283,
                            'width': 4140086332359484243,
                            'height': 5998640101156481825,
                        },
                },
                {
                    'window_id': 'Aĺ˯Ӧ˱\xadӦǡΘ²nŖɾȵӂΥƩ\x8cώǭϯɑ˰ĳҧ˚˟ĒǵɆ',
                    'location': {
                            'x': 8060165608804448421,
                            'y': 1132707032796187249,
                            'width': -9054886920288374364,
                            'height': -972608949251881408,
                        },
                },
                {
                    'window_id': 'Ϩa˫φÇĖ°˒˟\x86ѵìы\u0381ĠлιĴ\x83%~ʪ˸ƣªϋ΅Ǘч˹',
                    'location': {
                            'x': 161495241444318281,
                            'y': -3495780857539004322,
                            'width': -8571919520401151716,
                            'height': -3402874458776588362,
                        },
                },
                {
                    'window_id': '¿ÒӻӞ#ĐÑzƓӸ\x92˺ǙϭҞûȋśΠŦ˛ОĕѺȟʀύΉ¶N',
                    'location': {
                            'x': 5926801697813255120,
                            'y': -5345036189185678906,
                            'width': 1753649221368762458,
                            'height': 9114627292800349232,
                        },
                },
                {
                    'window_id': 'ƀɏMƀңӛΕȜРԛƜǑҏʇeƽƳŻаǴЊ«őς\x87˻ǴĘ[à',
                    'location': {
                            'x': -9010207443971251680,
                            'y': -4955017307579412322,
                            'width': -7139174834748145631,
                            'height': 3593272680115372109,
                        },
                },
                {
                    'window_id': ';ΆɤϢѝĺĬ\x96˦ǔßƠĈ©љĹËAԠґǽΖϢ$қÑƑҹѩ÷',
                    'location': {
                            'x': -7376118849543277950,
                            'y': 5193675997575844946,
                            'width': -187560512136347155,
                            'height': -5973557957823681458,
                        },
                },
                {
                    'window_id': 'ÓʙґǳӚʂàȆƚӻёΡŧ˕ԅԧȢ˼ɝ\x86Ǒæ®ą¤ŧӺҁƱŪ',
                    'location': {
                            'x': -3431305605120622080,
                            'y': 217574200607808710,
                            'width': 4273909596351458012,
                            'height': -217219444147255062,
                        },
                },
                {
                    'window_id': 'ϵɓƑƺÆөѓX˥ΖцĞо¦ыȌĻӈVϙøӚƌcүӋϱʗЮҍ',
                    'location': {
                            'x': 1303170080092182134,
                            'y': 7870385014087225597,
                            'width': -5461033284575156522,
                            'height': 3622845163248628023,
                        },
                },
                {
                    'window_id': 'ĨЏ˴ѪΜ\u0383>ЧβѬʓɄπӇĘǗɂiҡʓλΈӮэГŪgτπx',
                    'location': {
                            'x': 5840052638425393833,
                            'y': -9179142056060117393,
                            'width': -3895231487540348444,
                            'height': 7890660241612680569,
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
                    'window_id': 'бЖ҂\x9dӦ',
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
                    'key': 'ǭĔŵҕLȦŹȼхˇгǠ?ʦ#ˆƮņɸМƟѪˈоϞèǱι\x82ɯ',
                    'description': 'ȾϏħÇ\x7fʫєӫʸ<ǘӔöҧԓïȘŨ0Ѿ\x9bԧsÖΪԧƏЗЎɥ',
                    'value': 'ǕćǷшɭ\x9d˟Ěх*(ǹԆώ˒Лӄ1ăԡ\u0379УHc\x8bω×і<ȟ',
                },
                {
                    'key': 'У½ν³µą\u03815WĔӘӴɴȣёħÝÌғʶ',
                    'description': 'ŔɬәĪȫϺ\x82¬Ȧɭƾ¦ԝ҆ȉž΅~\x81ˏѤƉ§ԐƄķǘčĬɝ',
                    'value': "ςЊϧȣϡӚ°ȚԦʡǮΪTĮ˾ʿˠʦí)ˡ\x97Ĉī'űϐǞ˳Ȁ",
                },
                {
                    'key': 'ӭ',
                    'description': 'Лѽ³ϸŒjΣʬʤαǣȀǦϸӐýұ&YʈƽȭҦǱ+sґщƥǉ',
                    'value': 'ѥƴ˱ȫҹ4ǤԦçÌѡ1ӴʺӸҜώÑґȺĕĆԙ˕ɆѩҐVÞƌ',
                },
                {
                    'key': 'ȖзŌȷȳιӫÎǂ}ςŌϝđ˻ɷɪ˙˝˟ɠԫ',
                    'description': 'ɘˉǳҹőӧЖ΄ъϛǤʄĨ\x96˗ȣȺӋŧ±ɂȐŁǔȦšѧΟіԜ',
                    'value': '³\x9bËyıДώΟĥΒϒƘӶǟȉɹ9ǤҞɋɑ!ʓлȰѽϱǬԛ\x8f',
                },
                {
                    'key': 'ψɵҪ',
                    'description': 'ĤԮ9/ïWzǷ\u0379шкĄϲ\u038dџȸȞМǘЌҖпǸOΓ҄υÜϻƿ',
                    'value': 'ÀІȬŜ˭ɫлƌδМԣɕȌԢ\x9e8εѝʺĹ\x82Ùсĥň\x85˲ĴĎқ',
                },
                {
                    'key': 'ʟɁƖƝКяҼǄ˫ϛ',
                    'description': 'ʕŜɾˉȱ¢ʉҫԡƀţõρʲʫ?ʖǜß',
                    'value': 'IЕƀȊӓωƸùΦԇɍΗǚ;ɧѓŨčѵƋ҆ЬԍѤӰЀӾΉǌͶ',
                },
                {
                    'key': 'ʿҔôԃĩɅɴ¢йΛҹÆzƵзV˅ʮŰvƐςϿ%ҰǖƫÖԟ˷',
                    'description': "Ϸ÷ěʧϕЫɣʣӆȑʬԄ˧ŋɘ_ЖѶɜƇϙϹƒƒ'ϕӂʳͻǴ",
                    'value': '\\ʃѤǕ˂˒ψŅТʂȟɽȹGҎԪӕтĕǑциȻĆŎĄĆÓПѶ',
                },
                {
                    'key': '>;ͼҢх˫ɭҠķO>Ɓ',
                    'description': 'ʕ˭\x83ӣбŧѽϕӿ˝Ŗʊĭ¸ʴʦκŃнÎíƱäћʆ\xa0ºɀWɯ',
                    'value': 'ϳ˯ĭz΄ԣЈ',
                },
                {
                    'key': 'ӈȰԘЦœÁ˂˩ǯáʵƪ',
                    'description': 'ÇŐԀǫąǰΆµ˚$§ŒȀΈƱҖȽ¹ΛÈΩҳмðюņҰȒǢԂ',
                    'value': '7ƯӶ˥Ǎ˭ĂɞİʹӦǽЅΙĠҰȀǱԫЬҰѫԄȈǯ\u038bʕћ˦ė',
                },
                {
                    'key': 'õӛΊĀԥ',
                    'description': 'ƪӍĶ\xadʭ_\x92ӑ3Ԣʮ6ӴÅɱɯƸџʐӨӷӬӴ˞ԥʿƊ˰ѓԁ',
                    'value': 'Ԧ\u03a2ŲĦ˻ǛΓƾ҈\x94ɺĈȻʕčĴҌɭ\x87ԥ\x82ăČ\u038d˒ͼȵ˴ȌԞ',
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
            'focus': 8258,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focus': 893,

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
                    'key': 'ҁҞԓ©ѯĥ\u0379ÿŬȷńƖԔmЯϳüѐzȅɶӤǼ˵±ɼл&ɨ§',
                    'description': 'ϪĻĭʝѳȿ=ЗŧÝǃ§\x9aЏƈ\x91ȹˁČъYƲŶҿҏҬНɕģ˺',
                    'value': 'ԐǙӼɮ2Ӫħҙ˴Ӣ үȍϠɐʹİєüȅơʱłɗё*WYěÞ',
                },
                {
                    'key': 'ΥJğ˳ȏjȈƃpӝŠhƵϲ@сƉϏ5ʋЛȷʮĭΠȸΠҷлϗ',
                    'description': 'ԉƫɵʻÑ˽ɊɓӾUʴȇӷΕχ\x91ÿ\x9fϣ!ΦīTǃŵWԙΚoȂ',
                    'value': 'Ɨԇ/ĜѮεƼϰЂ҂ѸȠȫɹŅϗЮɯɪĭ\x95ЃМϘϺÍƫƶūɊ',
                },
                {
                    'key': 'ɭǍĥȚѓҴϮƳ4ʟԕȴŬ6ąŏđÆϒҨXіϟƗʥ\x88ʱǚƊҿ',
                    'description': 'Ǝɡ\x85ӤЪƞϊȞĺz\x80ѓǎ˟ҝÉ\u0379ĝÍуӡқ\x95ѽ҉ѥюǖĻv',
                    'value': '\x99ɩ\x8fҼƋɲȎӉʳoňľŊ˃ȡӞϽĕЇԑ~ǟϽÂѬľԆҢԧԑ',
                },
                {
                    'key': 'šÀҾȀɒԎԧӔɼəʐќǸƿƊƁԁ\x89čЭ\x8bȖѩϞһӋщľǷʒ',
                    'description': '~ò;ʹ÷ËŮêґѲƯ©őцǡʇȕl\x84ȫgшϺǷʍżȷwψþ',
                    'value': 'ʥѭcϋʌǺɉѨ×ԥ\u0381\x94ЕԆ',
                },
                {
                    'key': 'ҝͿͽį¹һҲ;ҪҶ˭ʫЮȅәЬæſćϻьӤыƀʟʳ˩\x93ԣΏ',
                    'description': 'ÎҠϢĖ_ǣҿµwʒΞϺҊŉӤĚĨň˶ЈiʤҰўǲƺӿоšƳ',
                    'value': 'ɟʿοǬƏĔʒťʠӴāǫΡƢȋѪǦӁʏϷűҎïԭ}ѩƇ҈òµ',
                },
                {
                    'key': 'ʒќͳʍґŏzԤɆͲӓō˗ȴŲɫӬɜԮϸȖˇ¬ѐ',
                    'description': 'ɮ\x9dʅΘį\x90дҫCϱԗƨǨΟǰČʑѭɡƕџȃÐǙFЩҁЃлζ',
                    'value': 'Ȓíʫ©ǧɖƸÜƲ˦˒μ˵Е˻ǙϒʳԀǍļƬ1ҽȊϹСБƫŁ',
                },
                {
                    'key': 'ОNͳ˅ҕĴ˯ɳӉҴȍƒǂϝͷ*˂Ƌ@ѓԐpӑ\u0381Ɉ^0ϐĒɃ',
                    'description': '½ұ¡ÿɠʑ\x80Ϸǁ҈˪ѫŶɒŪƒʁҬЀǟɽѴĚĽνԖǻʩƘŉ',
                    'value': 'ĶЙÄ¹|ʙ҇ÖƯ_aԛӕӿѨ£҇Ǵ͵ȫҩмʀʣѮʯĺåλО',
                },
                {
                    'key': 'ξÜkƿ\x9fťϾ',
                    'description': 'όōæǾŞρ¦ӬϡɉΨǁ\x8cĒ˂δ[ӎƀͽґǞȝũьԃɚ´ѐӄ',
                    'value': 'лêӏӢқŔίѸʫǏŞAԠǿϔʭȠ\u038dūбÛxԎĀѶɑnȽ©÷',
                },
                {
                    'key': 'ӻǳɭǞѿϦǀԍǥг;ξΓӕ',
                    'description': 'Xκ˘ΙһЀǢǁűìӊŬ˕ǼũĤρĳ2ѶĴǘŉ9ВȇǏˌɲƥ',
                    'value': 'ÝĻԧӝϒƊƩ\u0381ŁҍMƟőŊΝôѭӆxAӞɥȓɭ\x85ˎҋQ\x7f˱',
                },
                {
                    'key': 'ęĕºѫӶ];ĪƠηӀӓˡʮ@тȼԁʲĨϢӳѩʢӄҦОǢӮĈ',
                    'description': 'øӃƩ(ІΜˆȶŦǽɺbңńØ϶ÈɱҵǘѬĽƫ\x9eϽǗщԈҡ҄',
                    'value': '~Ƥ˟лԫ΄ƪѫó҇ʅʢȼҬāήGʚÏƨƪźȵСįÎԔԪΗӴ',
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
            'window_id': 'ȹ\x81-ԀƤϲԂƾʁɹϿк\\Ȱ\x99ўŋҳʻ˳˗ÓDè\x95ɚ˙Ŋаǚ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': '\x8aѴϧό"',

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
                    'window_id': 'άĬϗɚďȸȉԉǝϖȍǜаĨPľѮϸϟϔԍjǧӬ˸ʆ2ơɀʹ',
                },
                {
                    'window_id': 'ôǧЃˡ;ƣғʥTŧҸǹ¶ƐƙjƁ\u0383һͰ8ӠԗҊƧʉǁșËʲ',
                },
                {
                    'window_id': 'Πη9Ώ\x82«Ǆ˭ȡҁʡƂɊǘ΄φŉƊӍdɊˋĚҿѻķ ʓĐҫ',
                },
                {
                    'window_id': 'ӒĉƁöÏȆԜáƙˉƼӜѐοǗѩ˸ÉʛɘĆӚ˙҅ǸĀўȤӖѳ',
                },
                {
                    'window_id': 'ʒϯΖ¡γʳɤѹӛԘӂĶӘϑpɀT\x7fʂӪиφҸ\x8dƫ\x9eƉʑɫϸ',
                },
                {
                    'window_id': '*\x94ԄōĥÐчȶŜȄӧÊŦųƝȍ˜&ѷ#ʅԕԍɪΥͷ˰϶Ҕʁ',
                },
                {
                    'window_id': 'ґǧƨЁ\x8aϻцħĥҧ±ҷϞŋƈƙʧħ˲ɞīŘЂ҈ňāԦԙ¾ˤ',
                },
                {
                    'window_id': 'ΈƄƱτƙÿ ËҦšҧʘνAĐЏЙϲщǪťǢʏűԉǤϔƎΓϿ',
                },
                {
                    'window_id': '\x96ˬϕƭΖĴ@G˃ϩϽϯά#ˬ¨μLÄҠӨӕǔ˲ΥųЕ\x86ʹ,',
                },
                {
                    'window_id': 'ЛÍǼч˖ӈʍĜȕāMөϺшЩƣ˯ƈЇ\x8aǫKѳαЌ҃ɕȠ˯Ѐ',
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
                'χîΙɧгЄɜԆԄĐˇ҈¢ζȗȂлиј2ȱ%˸ΎʈЋǲćԉҗ',
                'ɫ}ϜĵʝɚʍŜҫӖ/ȢуƄȔʓǦMαȖ˕ǶåÐӡҹʨňĭ\x84',
                '˂ďǑԝΫ\x8c˜ԝŵͽФŢυˏ˙ǄȥȗώЪΥɫîȂҖɠÐ¸ëɬ',
                'ѳƇԒϚɴӹ˧Ɂ҂ыÛ·ʟɆӑ\x7fȝь§Ԁǟǋɰw˘҃Ĝȑɩ\x95',
                '˰ԇȨжBƵǾÁԬӁĦ9ХFѦ5ɽʯюʑ҉őΰԐ+џˣˎΌͱ',
                'ɇÎψ\x8fƃ˥ŖȠи\x94ĸʛɢç\x93҈4ΖԡĊʖӓ~ÉϪьЄ ÆÞ',
                'ʒԜѺ8ЪШ¥ʣϱ\x87˂ƲƾŲçǑιȡɘФβ\x85˂Ƞ\x9f÷ʆҚϞД',
                'Ϩsǟ˔ǻÃ\xa0Ϝ\x95\xa0ułźађɭɩӿӱúʎΕс;Ӟ|®ӓǀϓ',
                'гȣ×¨οʁèгŪΖňȨťԑϙԢҕҗХХȦƤ΄˜ǭѥt·ȷʹ',
                '˂ΊŭґήmˈžqͳԮ`¸ο%ǉэō®άТȐƊұ˧ϱłĦÀɃ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'ьςМˢɌ',
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
                'focus': 3342,
                'parent_id': 'ҹʺŸŜĽǁǲţ&Ûóșƨ1ȍɤǎѱÌхŔіүǹʳƠˬ\x80Ŋʴ',
                'location': {
                    'x': 6234098150172261229,
                    'y': -8096501511013282063,
                    'width': 7346519122877312488,
                    'height': -6901500565699874865,
                },
                'minimized': False,
                'meta': [
                    {
                            'key': 'қϚѿ',
                            'description': 'АUϣҙ˘ώЁĂOѿԊǶÆʔĚЊă\u0382ƸҭЪˁӧwƹĦƶ\x81ӊʼ',
                            'value': 'ɸ¢ɉжŹʬlԀĘɉǩzΘӾКʁҐӧ\x9e˦Ӆd˧ӀʞϙƒԨѪƮ',
                        },
                    {
                            'key': '+ͻʢˣºҬşˬϜʔҡӤǐʬɘɰơϮŲ\x8bѡƔ}ѓϘņ\x9fËǬо',
                            'description': 'ԤɃӃąѰԋʯÙʿӊҴʞ˳Ӌ7ʻʮԥŊʁЂʀƌӮɩȑ҉ʱӣʊ',
                            'value': '\x96ŀ¾ùҝԕɓˮƤѢʫ£õ˕ǻƓŜ\x80ҾтdÍЫƒÂ˾OηԨ˜',
                        },
                    {
                            'key': 'ȭҍҎ]ĢŸƽĥԍɠŸĵɟűȄɯΘǇLʣƗSșѵoә\x94',
                            'description': '˷бƵ҈ČʹԠĶȶÉ5ƅΰԛɄӄa¤łfyǈʆƜƁ¦ԊӉʱӊ',
                            'value': 'äЋцŚáŌʜѽͿѣčˆπXǠŽmϥҳfȆјö(ЂɶЎɘZ˹',
                        },
                    {
                            'key': 'өωŔƄн`ƴ\x85Ȧ¾ģӢɂԅʀƢ¨ћιȈеʷЏΝŢoŇөŵè',
                            'description': 'ȧ͵ȬњʠΤɹԋſʫɛxéԊŦňȞ˙ǣˀķҠňћԎцĉ"ΪӖ',
                            'value': 'Ӱ^»-ǪŏӧҚӽÊұɦȴ£dІ˒ϝŋɇϭtɭϝĭˇǼȟİŶ',
                        },
                    {
                            'key': 'ÅН´ƩzОΣĺ\x93ȞˎʻʃœȸӋЁğŲҗѻԠ',
                            'description': 'uƥˇ˺ЍҹʋȚϴǀϜԞĒĒҁ¾ΘňӜïыˌ˙ԭ5϶мҋΜɋ',
                            'value': 'êƕè˒ϖˢԎɓ[ÌƣԧňΑȝƐɢӎɷɊӓșПǐǪӴĐӘĞϴ',
                        },
                    {
                            'key': 'ԛҒŸӹͼÓԘÃ\x8aɁǥȽƭáʥӡɰˑԀƫόӺ˾Ђƪу£ȚƫN',
                            'description': '}˂ͼǪԭ˷ΡŚmϢƭԞəǤŞƺΘŹХǃɠ϶ƦuΎшвћȉϨ',
                            'value': 'F\x9aϝӭϡȑӯȲțOƿʌЙ;ųеGȋԓʺ·ɲҒҘƕζҟĤȥλ',
                        },
                    {
                            'key': 'ƈ\u0378˲îԥˉyӂYʀԛƗŶEȞśϭɦDĄ',
                            'description': 'ӂͺ΅ĵԏ½łɶ\x95SзͳȢϵƩ͵ļϗЉƵű\x99кW¨ҰôĆɘѹ',
                            'value': "юcБ]ҹńŐǡϨʊfӽȅɄ\x90ӞԅʧҰүŒ\x98і'å´ȺӮԐѲ",
                        },
                    {
                            'key': 'уīΆʇҞχʇήԣʭѬӉѿbӜ˽Лѭ҅uƚȶˆȜ\x99ɿ\xa0ȇÔҞ',
                            'description': '\x9dҾȥƏǞíʈ²·ԞȻĝǆҿqнɘӳ\u0381ɪɌˡѦҝş$YĜɾΉ',
                            'value': 'ёǅđӍ\u0381Җɱ÷ʇȬŞӽΊĔӆҩĹ3ӍύˠӈȃƝǵЋűĒĆː',
                        },
                    {
                            'key': 'ʽǔϚΪΆʝʘ:˴ƲÚԀ\u0381ŪȤŀЖǋϛ',
                            'description': 'ʹɩ^ǔǥҊƮΌŽǨӠґȞѮƧ\u038bɸ\xa0ϘԩЖŅĵčѡǜϞӻӨe',
                            'value': 'ɺ˅ƫdˢϗÚғԒʹӠϔʅҙϬԉϓѩʰƻʮϰλɖÝɸŨΛUȍ',
                        },
                    {
                            'key': 'ɛΞԩˠůǔӒŶ',
                            'description': 'ѣęǥǥӛýͱwƞRΣҔǀΊǠѾɗ\u0379ɳê˱ӫ˫ӱÜϤǫЪӅӡ',
                            'value': 'ʺȻҹăСț.ҳǇ·ŔӬ\u03a2ɮ§ЩȆӳԅҏɦūƙϝԅVȶʩ҉П',
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
                'focus': 5179,
                'location': {
                    'x': -4418237146261107408,
                    'y': 6866310203201045269,
                    'width': -4459819578989167787,
                    'height': -1359601947788850069,
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
                    'key': 'ѵưq',
                    'description': 'όϷ²ҟԔϿȻƭþ¹ƖäɜȬƪíЩиǽɄȎ˜ĆӞ\x9eǮɨɰƃū',
                    'value': 'ǡѲїɹϑєɅưaƫИȐěƝ˖ςЫӧǢǬɁĻӏӢ˱ʝ˙ŗũҴ',
                },
                {
                    'key': 'ĹԢԨʊúʀϬvΧĄǕ%ƠƋâҪɦϊЛŏЄҭϝWӍӚŐ\x98ȑ\x86',
                    'description': 'ЯÒӿʙˢћγƥйĂ˛ō˳ÊšӆҧƒͿĔ.θ+YѢφȁɃϥА',
                    'value': "ҍɚŽΔɉϿӾϪӪȲДћȳЍΥăԃͰȞъοѱ˜ðԍʯʵ'ɄÚ",
                },
                {
                    'key': 'ӂԆ\x87ƃκѯҿΊѷžĂβφɴζŭ\x9dʘ',
                    'description': '/ӂӗӶȁŵщΉțȿȏЮͳɏɭрӨѫʤζǬʋŎЎӭҜɸ©ΚÂ',
                    'value': 'ћµ\x9aԋъʲŅУϋԆѮάӼ"ƙPȳɛmή9ŪόӇΒ7\u03a2ӦΒɑ',
                },
                {
                    'key': 'ҁÒɛ*ѽʘӤͰˬû\x80ŤҿȬƈӤłÚǚ\x82ȯɢ˚ԩӽɽÜӫԚ#',
                    'description': 'ɣψӱӤȩćĞĚΐ\u0383ǃȠýɫʌǃЁʢ¿ʮNȃВhǲWѹĩnʡ',
                    'value': 'Ԛ҈Äīҡԥɜħ˂ɛЕєʴѬϝá\x8cѶђԧöɲ=ƮɑƲŇưʌУ',
                },
                {
                    'key': 'ʗøȌ\u038b°΅ЯǟƁ˘ϮΑпəäȪ)ɜƮșľƕЗĂū˃ʄσκˊ',
                    'description': 'ęĎҬĄВƚʉԜȩÐҙȷȵʲǗalҝМZǯ˚ÚoŪϯ¦ΡҀΤ',
                    'value': 'ԊԁԔϾεŋҖ˹ŭįȜƹԬɣƋӟӧԧЏáԦ¬ȉΥǥ»ĄӥǊȠ',
                },
                {
                    'key': 'ɹƗĮǓɖӉtõƂÇ¬ѽɧιϩҭҒѧΈ.¦ɘ˞Ӻѧ\u0382ԊȚƒʉ',
                    'description': 'Ȅϫ°ҝчҡÝɋчпъεüӧʠҘ4ǚϷӣ˛ȑЂ]VηȗÍӧ˒',
                    'value': 'Ġ\u0380ȏăWȿƺ{ϲʎϳҍɼİͲϫ˕ˆ єϞ\u0381˧ǸŭѺǦЇƌΕ',
                },
                {
                    'key': 'Ưͳώ҈Øʏѻ\x83ąĸą\x91Ⱦ˔ƗʫҰĸʥТвɽϟϕ',
                    'description': 'ԞƑĩ£ĆÉ\x93ԣҘҥĹȯƛɾӟȒҦѭÓě³У',
                    'value': 'ФĵҺbɳңŰûʹͺɅÃƮо\xadϘǜԁʑȔɓ!ģãĖͺÇͰŞΘ',
                },
                {
                    'key': 'Őŉś\x8fÇӷ.ϖӅ1ӾӀѾ',
                    'description': 'ͶͰʸġԎ¡ƧѨƔ"Ⱥĸӑ\x93ƠҮɤǦњ\x86ɺΔȹςҕĽȦѧԟǄ',
                    'value': 'ļɦų\x91ΓœЯ˟Ƭ\u038bƸΫʶ˫Fʫ7ӭҊ1ɧӀҀϕ|;\x91;ζԪ',
                },
                {
                    'key': 'ΚȋѥÐϕ˪ɂƟǹɯѮΧΣ˽',
                    'description': 'ʰŲǴǳIϋǩҤūԘľˋĞЄӈƗԗŵǪɊUÊЋǧɐɮĦӕĂø',
                    'value': 'Ķ ӄíϏǙрÚˢȪӧɿяˍӒɭШϫЈíʯĚǇѵyÙʨǭʉ˚',
                },
                {
                    'key': 'ƋñaɆЎȵѡԟϥҭæӜ\x84ƇŸ˨ǉɃ҄ˇŎǱȲ',
                    'description': 'ӠТ\x99зħεǀɅɣҪҵˀ˟!)ɶçΏҗϖ˂Д%ґѸJʟĦľӧ',
                    'value': "˜äȄʀ`ĽìϔìKєŐſɥ'ԇҒǰїԙѠѥȫ>ӜʞÀҎˬ(",
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
