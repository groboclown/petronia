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
            'x': -1776643788247995421,
            'y': 5108836057910138422,
            'width': 7395846498946557597,
            'height': -6362659105808409001,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': 6613484750685741001,

            'y': -8520711594269064377,

            'width': 4623926053917645431,

            'height': -8645639438534036371,

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
            'key': 'ĵǍ˙ѴÍƩâʥȝøĆʚǻ§ԥƟσԍΕȂΊҜƲԀȫ·Ĵӗȇ=',
            'description': 'ͱ¯Òɱ˱ӀǩoŞćƥŚҜŮ9ʓʔQƯȋΟ_ȠԮʫ\x88ɞӤʦː',
            'value': 'ɫ=ѳ\x95ϗӀ˂ԢǦԛ˛ҢŠăȠϫ OЯ˦ӌԚ\x90҄Ӻ˄ɃɎĭҭ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ő',

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
            'focus': 1595,
            'parent_id': 'ơƯ]șЩu@҅ԭɨɄɶ5˸lʫƜH$Ä\x82ʇϹÐСҳš˖Ӌω',
            'location': {
                'x': -1839134705499181330,
                'y': 4878001377482640769,
                'width': -3485390863676544800,
                'height': 7890824843363503156,
            },
            'minimized': False,
            'meta': [
                {
                    'key': 'Ϟû\u038b\x92¾ʬł{ȌƴУƘԦ\x8fɸ\x9bцĞͶƛԢÕԖ\xadǳǺ÷ƲͿʐ',
                    'description': 'XʵĊНϻɖʄɥʌЅ@Ñ˨ζψǦŁƢŝИŅHʇҪϽë˥ʊΗͳ',
                    'value': 'Ӈиӆ\x95ˁѹРѻϓƏ\u038bϖˀͿǨ˳Ѕj˷M˧Þӏ V͵ÈʥǇT',
                },
                {
                    'key': 'ΞÍKǐԢү²ɽŇәѵŠŐgǅѯǈυԕ',
                    'description': 'ʝĄѹАӁԊʺŬʃǯ˸űʮѸƱǌъϚOӥϖ¿žƶѝċeʾ˸\x9d',
                    'value': 'ӀѽΩԊĪ˷ˋǞͶɩŜÔЎ ƌΌζɶ·Ӏǳ˧тɐ6ǳǦ҆ųɷ',
                },
                {
                    'key': 'ӓȋ\x94\x8fΘ˴ԗƆҼ˴\x99ǏÙ',
                    'description': 'Ҽ#Ȳő-иɛĢӕΙԅģYŨYШ˱ȆºНãΥ>ČΕƼӒϝЃļ',
                    'value': 'Џʝȭŭχːŗà?ȾȼʫϗȆǯƆ´Ñ~ҎŮƥ\x98\\ǷƱ÷ϻԜШ',
                },
                {
                    'key': 'їɫ-ʥӣʺӷʗʘ\x8f˱@Ӈԁ\x94˷ɝʵ:Ƴ',
                    'description': 'ķќ¤ɉӢѕ;ʟΨȖ˯҂˥˰ȐԕťΉѢɏϑЌʤ\x91ЌÿǸҚѲË',
                    'value': '7ȑɾɰÁΛњӑȯÛáòӺϰ',
                },
                {
                    'key': 'ʅƄɞǫѿLǦЋ2жƉę@ΪҴѴ˵ǄЕ\x9c˸ӲНʝӵɉýǒĸө',
                    'description': 'ȴƓΌxhʁӃηɈȮΦѽЕǭƸЭλƾşЛϪ˛ӊɜɮϭЀĝ\x98Ū',
                    'value': '҇ˈΑā(ӳɤҿԟƝӜɇʓ¯ъďчѝ˰ςČгɩԟ˷Ƨ\u038dȃ|Ѱ',
                },
                {
                    'key': 'Ȱˈђўɫϯʾ·ǳɝѕӵĺӲņŎɄÎԏӎ',
                    'description': '˝Ō±ϖ˭әrγϧϗҋϹÄɰ˲ԗbԚĵȾӥѻʗĤ6ί\x8fÔ¸ɿ',
                    'value': 'ӁŬªē¬҆ɓɚ˄ҁԭŞДН\x81avƸHŴğͽѽŏǏľÓӢѲɈ',
                },
                {
                    'key': 'ӍѣҊЃ¹ӅҘɛ\x94nɦʋ\x93ȴüɗ',
                    'description': 'ĞϼʴeҤьȴŪĻŀčƻĂ˯ӎϭҾӲюÃЗ\xadȅ˷ʴġȥљʅĲ',
                    'value': 'ɮăˉōɿлЯŹý\x9eƖȗǈԀ³ɽԈǊ«ΦǛZԩŊΔŠŃΛӭ2',
                },
                {
                    'key': 'ģȟȁɾ\x9f',
                    'description': 'ȓӞѷ\x8cўѪɣϠɥ˹ʋųϛʵГś^ʸЫ\x80\x7fɃùƈȺ҅ԙАǡC',
                    'value': 'І\x93ŒIʼγɂɚҵʏīҹЯƑ',
                },
                {
                    'key': 'ĭȪʏԉ«ΙƏӂO˳ŝ',
                    'description': 'ȒßáҶ¸ķ(ʧɺһ\x98ÇЉԆϜɗԘŻɵ¨ƊćѷƊÏ˅YѼǿм',
                    'value': 'ƗҰ©ƅȍ¹îѣƲŤ©ɰOΟʪƢШѝɷбàjłšŦќҠЌ˾ϋ',
                },
                {
                    'key': '1˥¨ЍʮҼˤňıӗ˂Ǳ\x8dȠž\x9c-ʑήпʂaӣȱƟªџϪƘԟ',
                    'description': 'ŎǨɉ˛ʚǫҙ&żĄԍaдѶľŵΞƅΊɫӹĶƦΪˌŭԝǧĒζ',
                    'value': 'ΈɈ҂ÌȓϨĨѶ˛\x8eɆĵôˣЇӿλΖ·ʠɱǿaɱѫб0hƑʕ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': False,

            'focus': 5374,

            'location': {
                'x': -7193451730543180252,
                'y': -5565596758605436532,
                'width': 4825789100637907758,
                'height': -1079722412907570890,
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
                'focus': 7550,
                'parent_id': 'Yʰɫη΅ΐдəӼӍӎЕBŇƒȋԓĺȡϰц҂\u038bʞ¬ҘѾρɣɏ',
                'location': {
                    'x': 2990330997387040459,
                    'y': 3155413874461344142,
                    'width': 963065223933820593,
                    'height': -8743657196538218832,
                },
                'minimized': False,
                'meta': [
                    {
                            'key': '˪ȩ΄οԐҧȌԁͱΧȜêˤƥ}ʧ҈ªźѿ\x85ϯÅѮƣШ',
                            'description': 'Ùɠ҅ƯȯǐԈ˾Ф8QΔģϯѫÖѬϞřƻәǻMͶˊЈҴǜϡԍ',
                            'value': 'дӟӼÌƝ\x98ȰǗҩ',
                        },
                    {
                            'key': 'Һ\u0383ҙɯͼńʏˤȚíӠҢ\x8cіӀѭʍŢЫшφˉњӦȐîƿϊˈι',
                            'description': 'ǶƖě¼ԔǔɟͻǨԊµ˵˳ȍʫ-ҝӍʩƈµ"ċяʋ˧ΙԆрá',
                            'value': 'ÛЫɠ\u0381èʉʜҼŔ\x84ƺӈ\x89Ǵɔɒ˯цЗΜϮΆʱźÏ\x95ȼƹǰȾ',
                        },
                    {
                            'key': 'Å\x81ԣ\x90ϾȦεƕ÷¤ƓŬγ˕ȰѤȥϭ',
                            'description': 'Әǡ)ѩʆũÕШӛĒ˫°ȺȤŻϺĬ;э\x8bíaΕԀǑɨʊҗ«Ԣ',
                            'value': 'ƤȰϏԥ\u038b\x98ӼΛȖӐ˭ùϟɞǍЍо\u0382ʲԖƃɸ˰҄˳їѶr¯Ů',
                        },
                    {
                            'key': '\x9dÅʑZϨԀȊҝȉЃ\x97μ4V\x96ѣΉɡÅÊɋÛʦ¿їǺǵΡɘʤ',
                            'description': 'ƝeɵҁŢΛËӡɖ\x8eBKϫj_ЇÓäÚĈĨ\x92ƸєѴҙƴҽǪǧ',
                            'value': 'ƑȊʺʂȳδϯȍɍȧȚ\u0383ͿǚԣȬΤΫӇū˗ˁǖŷГƳÎЋӌO',
                        },
                    {
                            'key': 'ƂͲѽžҜ',
                            'description': ',ԣӡƞԔčӳBԄʔʠlÊπńŎϯɊƷʴłǾż«ԈǻEǃˁѽ',
                            'value': 'ȗXõүԡс˾Ӂϰ³ӶĮӲԁϟЫ҅ȄˆȘ;{Ęȱ=ĊƲūƭù',
                        },
                    {
                            'key': '˛ӄǢИƤːͱ˜ΤſϡNΥȌȝČÄáŗɗ¹ѕǴķɴʺ˱ѥƘ',
                            'description': 'ǔËǌʕӐ˦ѿŸԟэϐńӒơƌҐiԪҩрˢɆǀʻĵn\u0381Çĝ¾',
                            'value': 'ȧɻʹҠ×ϴƑ΅ļ˝ϘВɅӰԥǜФž҉ґǣĂԉȾƺƨӘ½Ϡ1',
                        },
                    {
                            'key': 'ˮãэʋԗǇµɔ˙ʱƩ¥λ\x86ϼ˻+˚ɒ^äʆӞҧʿԊċǔǩЪ',
                            'description': 'ɏˬǒβƼÚνͲӬɟˇ\x93ТOƢȡϹǴòʰƫɃϞ5оϬνǱņȜ',
                            'value': '^ӞöԐˬŒҒϼĐȹӯɱȆԟΉ¦ԂB˪Ƨŝέzű˺ӧçѦиʡ',
                        },
                    {
                            'key': 'ϸ\x8aɹȎѪӂЁЩìͻҐо˽Ȍӷˌԋӯҹϲ^Łԋϊ2;њЗͼu',
                            'description': 'ςʥÅ҃ӆýǎϼã҂ѵŘ˫ȌĘĕԇītÜɫȃёǔɄâɊšsҕ',
                            'value': 'JҞųҴ[ĭǿƂVá\x9eӂɼBӈǺҜʋӁЂLζöѕƇԅˢŸ¢ɨ',
                        },
                    {
                            'key': 'ɗӮʨԋp¸ƻ΅ɤ·VѾӚΑԟѺϜƜѳьϷ5жˍ˘üΤЀŭğ',
                            'description': 'А\x92ŜÝǤƘȤ˪ħҶ\x97»ˑƂ\x82ΐфWξëȌ˴@\u038bʚĵѧǂ\x80w',
                            'value': 'ҽúƱɾӯ*ԓ˓ȣĹΝ]ӘǁДÍy.½Ɍ}ӊƥĆԈҭ[ǷiΟ',
                        },
                    {
                            'key': '\\oЋӦˤӀɧ',
                            'description': 'ʱ˟\x94a\xa0īԎȧɨүΏƝ\x87μƟӶѿ˪ƀˢ˰˯łϗǋεɖ=Ԟʱ',
                            'value': 'őɿ˳řɃҌüċӶɜɀɱЦʖԤѥмʄʼǋȎǾƸĤęǍŇʒѫԫ',
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
                'focus': 192,
                'location': {
                    'x': 7496906067989230955,
                    'y': 4847724710414350426,
                    'width': -8275701012817287956,
                    'height': -7228229028972990820,
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
            'reason': '˛ЫԣдđȮȾ˖Ͼʽ$ύЯХǨѕǿŲǒ5ѺȢΔʚηŃÔȢǂϰ',
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
            'keyboard_focus': 849,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keyboard_focus': 9687,

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
            'window_id': 'Ó\u0382ΞϪŋÈůʥ\xadĆӐìϚýƗЉȓÑǶϰȵͶӜĜĄŶū\x91Αȇ',
            'location': {
                'x': -1885481688133069945,
                'y': -6687432193889446007,
                'width': 8251209468599707956,
                'height': -8086953132032398030,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ԜĉЅҝˑ',

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
                    'window_id': 'ˬĸͲ;Ʈͽ\u0378ź{΅Ϥȡɩɂ\x87˨˵ʸыԡʕŷ¤ΞϜƎĊкҐҐ',
                    'location': {
                            'x': 4470902127023518495,
                            'y': 7230751390025990705,
                            'width': -8995624136370493347,
                            'height': -5332695779508620685,
                        },
                },
                {
                    'window_id': 'ԓÀŮʁĒÛ{ѱϵΖұȸҰԔĤԈñʏϱЉέӦӳлӛϪεEʆϥ',
                    'location': {
                            'x': -248304491538488813,
                            'y': 457735460393228435,
                            'width': -1734926429809820102,
                            'height': 6935115789652171108,
                        },
                },
                {
                    'window_id': 'ҜWыӔӱɔџӋӊӺғʝ˟ăýҖȦΪʥĴҐΟӀƪΓκūЀЁ˵',
                    'location': {
                            'x': -2539595238476368975,
                            'y': -4704403300411538466,
                            'width': 6987965652434074917,
                            'height': 8481085278071651160,
                        },
                },
                {
                    'window_id': '3ʲţɳӓƱ,ƐĆ҅\x86Ǝ˷ȏњҙʐ9ǹÂÐňҲmǐĞӣ˭ϓΑ',
                    'location': {
                            'x': 3679620516073207526,
                            'y': -5627719345862184665,
                            'width': 6920413956607613633,
                            'height': -1395229642386750571,
                        },
                },
                {
                    'window_id': '!ԀԦɼǢˊˏȳԏԈ¤âţǀűӈξɏȽӳцѓ҄ÐjºрąΛŸ',
                    'location': {
                            'x': -8129910558638333393,
                            'y': 3946209922433456461,
                            'width': -6397432399003934096,
                            'height': 3379866360009652473,
                        },
                },
                {
                    'window_id': 'Źęŭ%ӀŬĽΡŕļбÃɜXʽőɥM˛ÕƘ¶v\x99вʟȜрήί',
                    'location': {
                            'x': -1900543200489083808,
                            'y': -6617946628541386086,
                            'width': 5613098483746401920,
                            'height': -2176381925707942497,
                        },
                },
                {
                    'window_id': 'ŢԄZɱƙʹĆÿ˩˜њǥǁōGԎŠpҳ\x900˓ʄƙŹŉӻҹηƈ',
                    'location': {
                            'x': -4099013907676542759,
                            'y': 1534931034465082258,
                            'width': 136781759220313761,
                            'height': 3040098244402730445,
                        },
                },
                {
                    'window_id': 'ʸЦϰԐԊϴԋűғԝӏOŚӲʵпӽЌ˺χǂщǼїçϒěɰ˘İ',
                    'location': {
                            'x': -2048470092859249589,
                            'y': -6267640996876596852,
                            'width': -720610383791448136,
                            'height': 5707794693142019698,
                        },
                },
                {
                    'window_id': '%ӸǥѶΣίɴкƥKƻd\u03a2ơϓ¤ɁԚ\x9cҕÌȲɦȭcXȈΈʾȆ',
                    'location': {
                            'x': 6210061922834314340,
                            'y': -75602412585187166,
                            'width': 2852935021491930879,
                            'height': 3869503946918736554,
                        },
                },
                {
                    'window_id': 'ӀųҔűèǻȂɤȦƸȴɁǛ/ƫȌʌȜƲ\x83\x9aԁYùĂƒЅҚăƬ',
                    'location': {
                            'x': 4617157051834950801,
                            'y': 6389194906473185322,
                            'width': 2088381205736441101,
                            'height': 8630631707865867705,
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
                    'window_id': 'љʞσӓ1',
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
                    'key': 'ɱ˻ϤЁ;òÅº˕ҙı\x98ȳȟñϯ\u0380ƒ',
                    'description': 'вҝbSФκΏӨÕ\x985Ν˫ÖЂЧßΆʺāˈˍОʵ)ҭŀʶεӃ',
                    'value': 'ˀԓ°ԏӭŚEϴśęƉaƦDĴЀʏДӌTԩƓѰ\u0379ȖɴʋˡǕʎ',
                },
                {
                    'key': 'ԅʊÑυџźb½ʸĶӸϔԑǷ·ɣτӂоҦǼÄĖ¼ѵƃY˃ŵс',
                    'description': 'Ӏ;ԣѼ;ȅϋʟю¶Ԁ*ЊԭıԀͲ˱нéәĨҬǚķӬ»Έуž',
                    'value': 'ԤTДʡ¨ЪŪʉʰ²ӱˏ½Ʈɶѱτ\x95BԝѝҜɔ²ʙÍŗǕƏȿ',
                },
                {
                    'key': 'ԊΑʈĮ2ΏҜӛ˟˱ƙӶƈʽûӕįͱϹvџ\xadΰȗɤȺСϪӈ',
                    'description': 'йЯӶOҳĪӉȋΩʓʐԇµϬÆɣ\x81ŃʑԗâęØ˻ˣϓƒɓǈ;',
                    'value': "ϑν¸ҢǳÝĹҿ'¢ήΜǉÑ\x90aԢǙü",
                },
                {
                    'key': 'TӺæѢϷËŠϾŒƣғÞǉō˟Σ˼ԁκ^˺ǂ0Ӷнҽќɜʬ',
                    'description': 'ФҮӏɅǆzӵԞěƜӊьɮѽӄѤӭѯԬ_˼Íѡχкɉ,ȫ_Ǫ',
                    'value': 'цUʞ\x9dǊѩʯǺЯЗuȩʟċɖŲǹϬĳ£λȭˈњѰ(Ĝȳǩΰ',
                },
                {
                    'key': 'ԊӿɟZЈԘϖәŐȐżǚd#\u038dȄЇύїÔϰӸӛŧЏĲ',
                    'description': 'ӒП˦źҠìЊɗ½ʊ<½ϧύʛĀӯcћ~Ԓ˕ΞŅˠȳãѲβˣ',
                    'value': 'ȁѿ҈ӏӾjʒˠżƄҦϔџҩħφ[ɏӒÑ\x7fƌǈΫҫНƢ˟Ėɴ',
                },
                {
                    'key': '΅С',
                    'description': 'ȌƾѲ˷·ϹǓѻ΅ʏώɴͱŪҚıϦÅʰɣĂşЊҎұǮώīјӸ',
                    'value': 'ѿǛѲԬɣɩηԊƍżӹѲЭ˺\x87˜Ĳ,˳ȴ\x98ȭӜ¬ŒɕѯΆǯЍ',
                },
                {
                    'key': 'ҋȳ¾ҙºԖ΅ƵҜԃϔ',
                    'description': '/Ʈґơǿ\x8c³1Р˄˟шȮ{ϡȠҠ\u0380ÄÞɥɐE+őы°ĠԐԆ',
                    'value': 'ӨҚĪ_ξSΰмÑΤˮήҦҰ\x98ɉǕ\x8dϺ²\x8aӵʍ˷ºԢ˨ŽƝĨ',
                },
                {
                    'key': '҉тсϳΊśÛ҅ԋƿǋҦϦˀЋҌ',
                    'description': 'Ĕʠƿu˕u¡Ū¾ˆǚåѲRʊʕŊѨѱΗӣũʱįɭʕǜġϻЗ',
                    'value': 'ɵͽҎҚEÈʵӁųȢEƾίМΏϷʁĭǌќɆĕț҉ѹZϜѓÉŇ',
                },
                {
                    'key': 'ъϴȠŀӗûȒăÆӚ˫ӂѶĚʤɭŚ\x92ĖӦ¦ƨҫϹƒӃƼмӶϛ',
                    'description': 'ΐɢħɒâϐĥБӈҢ¯Ž+áǨGªнțǾтΎʞLƪӈ2ԂǾԣ',
                    'value': '\x8aƆŗǾѡѹϽǪʊĂÕɶԫАŚԔǈǐº|«ђŴДЀɠʋ΄ǉΣ',
                },
                {
                    'key': 'ɡґ˥ɓ˔ѾΛȬɌØɰвƦǮɚżűЭ Æʛ΅YρʉɱД²Ǹĸ',
                    'description': 'ƆķÿĈƵͼƹҿǌōƅԧƈmӿ˩¦ʯȮχ×Ԯ˽ā˺ȱϒɉЪӛ',
                    'value': 'Ȑњ¼ġŶѝˮǰ҅Ľңŏ\x84ԀŋϽĔȃЈͱīϞӔϣʏͿʓˋșü',
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
            'focus': 2434,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focus': 5635,

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
                    'key': 'ФŘӤ',
                    'description': 'ʐҊʶ}ȒÔԟи҈ǅŧųǀӱƴȏѿĮԧƆ³ȕӊʑӒȎƽӟWa',
                    'value': "Ķ¤ϐÄȦPĪϷǝ˾χ\x93ќԖӛʖσ˺Ҫʡ'ʁşǢɶ˸ɪ\xad\x98ǯ",
                },
                {
                    'key': 'ɡŁ˙҇ąѾùÿ˝ɰmɐ',
                    'description': 'ɰÜιɼāíƶϏĭϬáoÔȵʭйǞŸǶԮŮіɧΚĹϳđžϝǵ',
                    'value': '˗ѣѼ˓ƣƖʻҷȽƆӒȱɷΝϭ˒țƀƌKƉßȐʻǌԟЈɲԒɖ',
                },
                {
                    'key': 'ȚЩŽӄдϓƬ;Ǔ² μҟǶǻ',
                    'description': '˲Рҋà-Ĭ˾ҎŒAӍ3ǜȘţΨɓ˛ȕѐϷŻČԣɲßĥĩӑÇ',
                    'value': 'ɚҷ¯ӜʆʶǧʴAЬǐŒaήš¼Ӝ˫ŮÙϬ\x89Җԝǿ\x8c«ɫǋ;',
                },
                {
                    'key': 'ñΞ˞ƝȌЕʪ˫ƤҦԅӻ˩R',
                    'description': 'G×ԩѩjǉфƈԄğȺǆǆͷʾЩњÐќƪŒŪʔЪһʉ¯ƒȱ\u03a2',
                    'value': '\x9eȖƔJɻʍԢSҩƩ˟×iԆΠƕȬ\x92ӿЭ˜ȹ˂ɁѸħѲϡӅɴ',
                },
                {
                    'key': 'ĊѢĩȈќ˄ϩϚΗё˃ЦϷ\u0378м˦ӊŒͼǣѡƂʥąѴԈyɔǄȸ',
                    'description': 'җȷϝ\x90ӁϰǿʝǏɸҢŤΝ0ÃɸęŻΉІàßʧTʛϔί\u038bàӅ',
                    'value': 'SÑǥҚÊeίΈoФаȸБňςҟϳϻɯ¦ëӂƝǌǉċԪį҆ӥ',
                },
                {
                    'key': 'ЇʸCğΚǑԅ¬čȠȰмûɓŕȞu7ß±Ǌ',
                    'description': "˞λcξØǟΖˍÑ\x88%ɜηΡѼԗ'\x99ɊȍƕəӕëǽĺʪP˾ŷ",
                    'value': 'ǕϮɓvŧґϫϚċČȪУđ\x99ЛĝɌΘǊùӞɞҒϮĽѳΖϋ¼҆',
                },
                {
                    'key': 'ǊεӧӬνҾЕÖ3õuƴќȘηьҌЦϋǹԂ\x8eħì˴û9γЈҏ',
                    'description': 'ϒʯΓʣŹϼǙͳăЂσҚʤ\x84ěÜΝɍѭɰZԉЃ²Ȣϧ\x96tʩ\u038d',
                    'value': 'ʹËʩҵþΟ\x80ԝӲǉˍƉ҉ʪȹxЌΤ°ϑǾȤʞҚɃӢԝ~êӤ',
                },
                {
                    'key': 'ǂ\x88\x85Ϳӥѳ×\x90ӵԛɾʱºȬŠȓ ӗʏΕОŽȉӅ)ȪʝѼɴ\x9c',
                    'description': 'ˆϏϒӲǔɷʛҐɹьKɀΗƉ+ȿÒӜBϝЧɡŐȭNӝÚԝҁ©',
                    'value': '˄ΪϮĬƖƳŢȯîќҩȏǅҒĢɱɍЂҍeӷĒн˄ҔłҲΌƌ˱',
                },
                {
                    'key': 'ż\x8e˔ɠԘȐɟӕЏO3ѬƸƍǨԤɧ\u03a2ɦŬɇȇ(ȕźȰƿǸёҥ',
                    'description': 'ӔɵѷӰӃӠ\x97ФѠQԫɾșʐǍƥѼĤ҆įͿŤЅȠΫԝƲņ˺Ƭ',
                    'value': 'ȴƟϓǡTzԇʫş¡ȎŽǝϽǙӶҹӟvüʫ\x87ÎŽ҈Γԇȫħ˫',
                },
                {
                    'key': '\x89ԚƛҞɼ˕ȖƮÌœ',
                    'description': 'Ӕıŧɜ҇ǬĒˌϗɻӼȂ[˯ƐƽpԅǔɾɣΐхΛΆǙћӏЦH',
                    'value': 'Ǐϱ°ͽǫӐɥѝѠѸӑȞˎҍʄɹ˽ԛǍʇЈʽ,Ԇȵӟ;Ǐʍϕ',
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
            'window_id': '6ҤÜȟ\x8aǨƫ9ԛк)ɞøï\x93ҾɁ¼¦mȆÂжǑԇƶNӆ,˞',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ρņ\x9cӖè',

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
                    'window_id': 'ôɞ^â˚ИζűͲ,Ôώ©ȤЙӻΊȮť;ƱʺħБȿσѧʂÛĻ',
                },
                {
                    'window_id': 'īǞʛҋˊ¾ʏΓVȎǹȘČÛˏζɻDɷ',
                },
                {
                    'window_id': '¿ϴƉtʽGʎ˪қ˗Xġ\x88ƒĩǕȮοӴþΝ˚Ҧ\x97țSǩ§Ƈɿ',
                },
                {
                    'window_id': 'Ќ\x82ψƋϖ&ӫŶƮѶ|ÂЦϜđɵ҇ƞƹȎȽľѩ˥ʄςƂњͻ˴',
                },
                {
                    'window_id': 'ɳˏԔǭӔʀȡΧɱϤǯѵŁʭʋČƋϋíѐŦȂԅ¤ĜԔЃ\u0383YŎ',
                },
                {
                    'window_id': 'ƔÙƥώĸĊӒ+ΈνȋҷʐҿрϨиĔǢ˶ǌʂԒƪEΦ"˞ʜԁ',
                },
                {
                    'window_id': '˂ɼȸȉ\x8eǨѭ\x9aԟΐMӥăŰяdoц¯ѤǪϝƌӧΒĄʬ[pҰ',
                },
                {
                    'window_id': 'Ӗ҃ԙĻĕûϋÉ͵ȉѝ«ɨӣĿоԭ\x81ʊśƫ,7ÃɚΩŘ\x96Šǆ',
                },
                {
                    'window_id': 'ѱƴǷϟɒӋɗюӏʕƷRȫȖϭŽąЂ\x87ҕȶѱ¢ǥɥiȔΎӀε',
                },
                {
                    'window_id': 'ʆĦϾұ~ŗˊņĈκʙҭ\x8b\u03a2ϿϡÑъϸρīģӿˠƨΛņɷҙ˵',
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
                'ʝŏ\x8fйǛėŸѻĖȾПįǐӎíˠӐƨȨóɒɎΑˆý]ɻɢÜɶ',
                'ƩŊǩZпЁΦϫȖɬΛɤиɋϹƅЎɪäϝӶӋŉνŘ¯Õɴĥ҉',
                'Ũ\x83ӴԪѯӥɥБғԆЂϵəӶѱѯқ-ťϸϐɾӚѭʚ\xadƂҰИƀ',
                'ѭǣШΞͲѳìê-ҙәˁãөδęαɌN7ά˔ůɋӡǨΨ|ż҂',
                'ȗхȪїWɎʭΑƑѰū˘ːǿϤ˼ыʆɋНӯǎͲЬ;Кʗϝ©Ȓ',
                '˄ХːȻ\u0382\u0379Ѡĩ˰(KÃǩ\x9cбƨɁˇͺȿƧьԆόÈ\u038båΨ˓7',
                'ϲɘ¾ˤ\u0380Ĭϵ\u0383пʩɷ^ŅҟҝĿĊϣҨʧì˅΄ҁ8ʖǛČhȉ',
                'PϤēϧϨÞȗȫƺ˯ƦтĦѐƓЇȓϋЃˣƊƓͳþŧҡҾʤϝ˹',
                '·ƻSϑ\x91ѰҧǔзґǢtΛĒčĵ.ȼӰɯ˻ľʙÜľ8¹ƼΦЮ',
                'Ǝȍȁ½ǲ¨ӊʈюɷԬȓˍ˟кĢĄĠɡȑЖʹ\x95ϦĐϜΒЙЅͽ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'Ɇԅv\x98ø',
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
                'focus': 4229,
                'parent_id': 'ĥӖИ˫ƚԋţҏ@Ҕ\u038d¢ь˻ɘ˒ӑӣȕG[ũƣԏéƏƛɝÜT',
                'location': {
                    'x': -350215577625647913,
                    'y': 2015112186293302909,
                    'width': 6670607270429380936,
                    'height': -7087623281570160038,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ùСӼҩàβˤǞОѰӛʗĳ\x9bʮJүӡ',
                            'description': 'ώѧÐѷƮϋʰɇɪжѫѡӞ\x8aʚʎȤʲзǸjҁɶɡɴҢˬĸơϏ',
                            'value': '˴ӤȘɠЍūʝԥ¯ѻń˯ӂӋҵƤȘ·Јœȗ/·òҼƶЭОύҥ',
                        },
                    {
                            'key': 'ǾſũűƑÝђŧ\x90]ʡ˔åƵ\x99#ѰǙǨǨёǠȝǻZŬíϰʧǵ',
                            'description': 'ϢōЮФʐԖ\x9dԮƺБԞƉ\u0382ɳѯͺȓӉДϋŻӹȚŨԤŗČǧ˦ɟ',
                            'value': 'ӞǺӀэɐҜӁƉȝÿŜƏǩԆҐǤΡϷ΄ŐqΆρҹЇoɆũJԦ',
                        },
                    {
                            'key': '˸ΨДĘ\x9aͼHӞ³ÌuҪǱҋϖѺΑΝñ˾Ǖ˙Қ',
                            'description': 'ЇĞ˶ύɣ\xadѨȁÓй\x82Ң\xadƱʇφ\u0381Τϳϋ*ǜɞӵϣƗ҉Ą˻}',
                            'value': 'ӘŞԨʞˢyƿ\x9fȩЀ\x9aШǡÌѤѴɱYǽʍ҃ƑÃΘŮęʹλɏƆ',
                        },
                    {
                            'key': 'Ŷұҿм\x9aΕˉѧӓ˾ʙŠӺ-ţƹϘǧМÿ҆ӘĄ¤ËұlǠƞʿ',
                            'description': 'ӆлщûƎéЉ͵ȧГɂć˒kΘФԘ\x85Ρ¢ΆѻǱĥĸѰѺÌϤʰ',
                            'value': 'ц҉Ўˤϓңs˯ŧHϊγșҟĳѺŽ³ԑƾɉª˄ÙɼÚņɍ¤Ɗ',
                        },
                    {
                            'key': 'ƌȟľͷɮӀоǷΐʻƚѬϝƶžϰςą¨ǠʔƞѰѻ˓ԈȻѮsȯ',
                            'description': 'Ԭ}Р¹ϼΊ¤ΉƋԕɐʽϻɋϹƈɓnΆϴϬȪӮҘFǗʎʛЀì',
                            'value': '·ϜƆϼθҿБҊѧńπƐ*Ȥȏ˱ϣњӳdиһ˾ԡҽƣǁƲӊƤ',
                        },
                    {
                            'key': 'Ǜ\x91¢ƠԇӇԗеЖʟʃƗĄZF¨ҖҚƝ˦Ҋ\x98ϟ¦гҶȘҶ8',
                            'description': 'ИɖīX˩Ș\u0381ӺĤҖǰѧȸҤôŨˍő˷ԎüɴɤәɯâêÚ˴ɐ',
                            'value': '(ҼБˏЖʄƵɂ$ҜϋΚϚǉ˱Я\u03a2<ˡĬςȲïҚɆōYɤѦԊ',
                        },
                    {
                            'key': 'ɫοƎ',
                            'description': 'ʒ³³Î«͵ЫƢМŒΚҵҠʁҤÓʶĠɤ\x83ȭϔђҠũϯȆʸйB',
                            'value': 'Ӿn«ЇҐQƼϔөɑˍVԠɅϿ>ЕzӿΛCͻƞΝǀƑşcӪѳ',
                        },
                    {
                            'key': 'ЙȌʷͽɟТŖҿǶŞԀ',
                            'description': 'ўǁҖʱP(ƶǶ˨ƦđƬĵ˅ΌϺŢǐфđÖˣρϛҮ±шʖ>ů',
                            'value': 'нҪȫāƵɮĻ½ǺʱɌāɕώ˴Ôӽ5ѝ҂gˡʯÖʎſңɾŴ®',
                        },
                    {
                            'key': 'ˋʆѷΕ$ΡҸӀӟ˲χʿӮçͳ҃ΎшǽƄɺԃ҄ӴuɪӖƅÏ`',
                            'description': 'ҩŅÕÖӰŁʙʾΦĲғ]ŹχüøĎīЌƋüɠȨӯǮӫĀȔp˦',
                            'value': '˳Ӌ˲',
                        },
                    {
                            'key': 'ʊʼʐҴ˂ξǻƟƲś.ĉdłŻēĞˀˉпˋʪȗƗѺśƕ϶ʪӼ',
                            'description': 'ǻҥӸԀģ˾͵Ӻ\x92˓\x86ѧȋɮˡǁ϶ʮӳgªȟġdʱ˫ʳż˥ʔ',
                            'value': '',
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
                'focus': 5464,
                'location': {
                    'x': -1057990955188561510,
                    'y': 4591467693107374215,
                    'width': 3805239903843352441,
                    'height': -9171656672471838881,
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
                    'key': 'Х˘ќŊȌÑŜŽRԍϨĠƥw\u0378Ƽæԉ\x8fɓoǸɲmȖǔęŵԊӸ',
                    'description': 'ҮɡЊ˞ϛưʻĀы9ƻʌԊtȲтlbȒǛǥ˵pιāĕʔѕ\x87ǻ',
                    'value': 'ȗʷҥɝ҇ˋԥʿ˺ǻȴIĢϰì˰ơϽɍϡӾѦԓЁǶ\x88ӫҔ\x9dy',
                },
                {
                    'key': 'ȗ\u0382ˡĬҾεԝǢƫrǌίΐёË˜ī1ąɓ҆йγʴǿǀ&ʊәΉ',
                    'description': 'ŀŚūΤ°}ϑȾԠŹԪÿ>ҥӒɶдșƕˆĮҟɅыԪȫмȫƻǕ',
                    'value': 'ːΌɥуιǇΊrĂĮ\x8eʭRЬщlΤтǶŬĽѾ[ͺ͵ʘƃƲſ˯',
                },
                {
                    'key': '˚Ū҇\x9dɜ²ўϝȣЈѸ]Ͽ˩ɓ',
                    'description': 'ӍĭİɤäϝͰΡŵĮŏƎħ\x97Ҽ!˕ÍʾÂȑΉРɜG\x7fĪɵćӀ',
                    'value': 'ɠś5Ȁ\x7fЬЇƲЖ\u0380вƙӗ΅ʴӮд¨ʽƱſұ,Ȟӓď\x95òśľ',
                },
                {
                    'key': 'ɔȧĴƶɀаǥŋԋ',
                    'description': 'όȳоΘßҔǳAҲӢčdȜӧŚȃ7ԏ\x9fҭ˚ǂǫѶêӡёԞÄϞ',
                    'value': 'Ăµʿτʰҕη§ɃƮYŎҮɅϟϙȕūȀ˱ǃÈԨӁ˚òÜ¹Ԩǚ',
                },
                {
                    'key': 'yčҶϿǈЉ;AʹɠЉƾȉΦԍϑ\x95мҸõџ§ăȉƗͷ¥ӧǜţ',
                    'description': 'ԒФ%ƼӅԝ5ɏ˺Ї¿\x94ŠĒǑ\x81ϗľ>ɼЮʍ\x93BĢΤͶþкä',
                    'value': 'é˒MÀɥпϷпeeΓӘµ҉ɑʊĈ˔ħ˕ѓɦ¦˴ĕvȡ0ӥT',
                },
                {
                    'key': 'ĜǗʁØί9AϞ АƶřӊƽĺîǒǱѬГπЈżëӥ~ӬɩͱÏ',
                    'description': 'ӹƒΑѭлЧ\\ɷʸƀƷȣʈʳҲʄͼɰȹʖnӅчƉĽĄӞʩþӒ',
                    'value': 'ѲсԀÒԖѢĝǏӼ˃Ҍ\x96ŬąǬ]ͻ\\ί\u0381сѼǐѽӜΤӫ½Ŝ/',
                },
                {
                    'key': 'àǉƔ¬ưŮȺĹuɤ',
                    'description': 'ǿšɅƣœȔȲʟɨɚȺ°άɵ1ˉȞǑ¥ΫʹÁѦ¤ȲŋǍƸ\x94j',
                    'value': 'ҔҠҫ\x80ʠʏѴҜϓǻřʤ\x96öˁǉāåЈǈǂҲǢƑͺвƉЕ\x8fФ',
                },
                {
                    'key': 'ľƳК3Ɯҟδ˙Ζ\x8cѴƭ˟ė+2ʇҸΩʝԁĺϗU\x9c',
                    'description': 'ɓ\x8eǎѤɊΚʙԞ+ćÓɲɄʚ~мѷƈȬmÈфĶԑwɆїȨҤԈ',
                    'value': 'zɣΚфюýÐәĎ3ЄиҡƌʕϨӼ(ϝƉӿȔʟϋӆƚƇŶ[\x85',
                },
                {
                    'key': 'ǖѿÉӥЫLЬ҄ɗĒȑϔϺϣуԋӗɟżŚ˳;э_ˬѣЇǀŊü',
                    'description': '\x97ςʥ½\x92ʲΛԐΧΊʩŇɗϐΙѣӹъїϥ\x86LçѰŇɆуǔѧϔ',
                    'value': 'ȹ)ϩЃѴӼ5˸ŎϲâÕ®ԆΣ(Ųǣϡîƾoǟԝŝ˔\u0378Ъ©ƽ',
                },
                {
                    'key': 'ϧѮ7śȂԛʮћĈĚǜ!ɲǪʦͻtҐѢźɄҾϐ±ѶέźĲЗн',
                    'description': 'ϫӳŖƞ\x97Ơ\x96Ɯ°ƜғҾŦrțИˊӶЈǦʹѫ˻ΔӰфʋȽ8Ҹ',
                    'value': '±ÇӵÍϠҥѣ\x8aΡъА!Ҥćӄƨԕϰç¾LЅΧĚ\x7fÝӮÊ҅˥',
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
