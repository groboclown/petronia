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
            'x': -1036085563866552789,
            'y': 1279987685224591048,
            'width': 8579165128401208026,
            'height': 1251170436089268864,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': 5073410198630674225,

            'y': -6065115491225006541,

            'width': 3789141597557645955,

            'height': 2961055548397241134,

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
            'key': 'Ɏ5¼Dίԋ˂ſ˰^Ïƈҩ˫ùÌǪ£˕Ԙȯƶʼºƶɱ\x92ʢ˃',
            'description': 'ɠͽһɒ%УΚλºτÙĔԡϯȻԣϩɃƲ£>ƊĸˆΡъȮϠҹΔ',
            'value': 'ʎԀƔҨ§ɏȗòԜǸɰƟίmԩȻͰîҭϤìȖψ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'à',

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
            'focus': 6254,
            'parent_id': 'ǫχǧXӝѶɏіáŀҽƗѿôťƂþΧɇ˾ɆϙΠǪҤĊʝΚɨʂ',
            'location': {
                'x': 4633483325315477989,
                'y': -4791227493009608945,
                'width': -2432754992577680426,
                'height': -4981743903447933048,
            },
            'minimized': True,
            'meta': [
                {
                    'key': '\x912ĥ\x94\xadǞ¶ĳĨԘÜȊǜ˔ҋϷӪҺƆӴ[Ǵïϡ`ѿͿ',
                    'description': '¥ƾрϜǌĽϺюǞŎγɺƉʡʵɀĉŌʁǭŤӵҵΎ϶ӖԛlǞư',
                    'value': 'őŢϦҘ[gñϹŬϴƱyϨƫǜ7ɁĢԌΌцȼ˶ýѭǔҪɳЩJ',
                },
                {
                    'key': 'ƼŘƥǓȤԤʖԗϼ҇вҙмИĘ҆Ӑ¤҂αʮҦƲĮȥϋҹǄNȋ',
                    'description': 'ѨԊlϷСʇˏB=\x8f϶Ѓ·Ǎÿ¨ӬϢ\x9eɫǎѬр®ȹУϵѩϑȴ',
                    'value': '˶φҟκΈÌƸʔЃɷьӝϔѥƚǝʃůɁҞǈӀαѪɴѫ~qŭȐ',
                },
                {
                    'key': 'ȝȌ-ǶͼƶқΞЮтˮ˂ȟΠǪűԩɷøˉ@θѕԭЈѕҿÄԣä',
                    'description': 'ŭÁзҝĐǩǊş\u0382ЕӷϒÞ)ӀɥŝƀɒǇΧNАîʖí*КӖɺ',
                    'value': '\x9cόҊWχԫɽԗ&ƞːʂuƪҟǭϷçǺπǅΟφщԁ¶Ǖäɋ2',
                },
                {
                    'key': 'ҎĠѠõеƧ»ęӨƻЉӴŘ˔ķȮĊԍĭʷӦŴ',
                    'description': '9ӚǙ˄ȧФ\u038bǷϳȘѭѹǸoƨʎŨɌ҆˹ԜϺʂȤ¿ʗЋĻѥĩ',
                    'value': 'û5ȂȓȤŅьȰfƨ˟ʃŭÏӒ1Ŀ͵ͳ˥ȤåLλοϪæϵЖҷ',
                },
                {
                    'key': 'шȼɌāˇ8ǖʗ',
                    'description': 'èԛƘɐǬĨδȨҟļǀгƎΌʱɃѝɞο˻ĊīϮŗˡĠ\x8a˫ȗͳ',
                    'value': '}Ψf(Ҍ˛ǳǮŅӤǛɟӅȫǂ\x94Ʃ¨Ʊư¸ƌϵϚјЦϞȸ&ˡ',
                },
                {
                    'key': 'ƅƼιĸӢˉǸЯԠ\u0382Ҕʺ"oŚªĚŁǃԦђȨΈӸӧϠΔԘʥӱ',
                    'description': 'ƠĻƲϠźо\x93ѫE˼Ȫǒ\x88ѤķͳΕέп5˳ўГϬ˝ĩ:ƷЩª',
                    'value': 'Ԝ0ƠǆƂ\x8fǙςǙқϸЀԩǙȪҶĊϝѪªƸ8ʴЬɼԥ¸ЮϮв',
                },
                {
                    'key': 'ӰoǁΌôƧȓÙǪˀӮǜþԏ˭ÍŬҙ&ʜӌʣʅ˹Ƈϭˁ\x90ˢ¼',
                    'description': 'KСpȠǷȝŷ\x86ΝíˀƿӖʠυӟ\x81ŞРȜΦĊȂѯŻύԈ˰ûʚ',
                    'value': 'ȷͱUĔʺсӕʭěŽʔYǉӓԊћcºԪӃӞԈҫèŭѦ\x92ʼӲϯ',
                },
                {
                    'key': 'ɵÒӯǲӚΆǇʒԣбΪӘ',
                    'description': 'ɼМˉӪȃӞˏhơӑжǒƓІηħƌҰΊϰҚԭхԛ»\x81ʑ˯˙ћ',
                    'value': 'ҚѵŨ\x80ĦXӉŻžƭԐкμ4ԞΕŚρ˂ѩƄIŝэҼÿɉİãѾ',
                },
                {
                    'key': 'ԧŅ_Ǧũȷ҇ȭ˺ƅĄ˷ˠНÜԬʧƀƃϕаǖǵҡű<ȷΥŀӬ',
                    'description': 'ȉҒ˥ķӸa\x81ȣ~˷ϠӎʣюäHӗѧ´\u0383ĘҔЌNʂѓ:ҞīԈ',
                    'value': 'УҗΦʊǇĸ>ʮΥκƃĩȑĉ³ұƬϩѥӨɹԠɵǝΕŶ~čëm',
                },
                {
                    'key': 'ɨӖòĮјƂÊ$ЌǩίˀͳѢǜäŃɱė£ϞеΕ҆ЌʁǞȸӏé',
                    'description': '\x86ΠŞŭʍͳɳӥƞģĀг\x89ȏͷԫ\x86τň#Ӌρ˪ҫȂԟпȈӉЇ',
                    'value': 'ӭˇ\x98Гѹпːe_ü`ɥŋâёĐɌͼöѨŝǡŌԫәί˳ȼɵŨ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': True,

            'focus': 3198,

            'location': {
                'x': 189275640086311946,
                'y': -4353321709942687791,
                'width': -3857634676867924259,
                'height': 1369441732645714674,
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
                'focus': 4217,
                'parent_id': 'ХȂşǌǵӳжЈʚчÒ"WóĴǩϕȕŔ\x84¢ѕŪǌԒүſҊɢƘ',
                'location': {
                    'x': 4066824483420116427,
                    'y': 6992880497692611121,
                    'width': 8706129378562994340,
                    'height': 2381473686444544957,
                },
                'minimized': False,
                'meta': [
                    {
                            'key': 'β(ӾѢϔ\x8eÓʛЅ҉ϻɵԋ2\x93¾ūЄͳϲ˹ŜǥćĕȹƋň5˒',
                            'description': 'ӴƘŋÉӖƼƾӃ\x8aВˊ\x92ʱ®ʿđƶuȊԒɪþйǨΛ¾:ĞƇ©',
                            'value': 'ǒӕʢҭʵɭ¯ɼSӺκŠƉƇӛŶÃXǝĪʝҾĈѥ˨Ωõ˺ΏͲ',
                        },
                    {
                            'key': 'κɼǗˎ΄ďǀė®ӧvОԎ³ФΕѶƣƚΰ˘ČϿƆҷóƋy\x96',
                            'description': 'àňȿӸɵʴƅб˄ðǤʳЎĚԝϙǆƷŹ˱Ů¼ԥҢŷδӍƔ«˟',
                            'value': 'ĩҶ¼ӡÈԂӪΣ©ӣā\u038bӴʵШДԘŏȊɅˮǀƖųƿėϚΧѾҿ',
                        },
                    {
                            'key': 'ɈʼsЬƮˬēҗͺӳɝʶɏȍǢίʓŧЩħз˺όĽ\\ѧŀpċϜ',
                            'description': '˼ǄVРǼҕƵȵѺԟӄȉʽғœřҴԉӉā0Ŕӫ1ΠƛÍͼ˦ȫ',
                            'value': 'ҳ\x8frƘĜϱʴp˶ΓҤɐÐˠĿǼԑȠƞӗŘ\u0379ʢя¼ФƤĊ˚ȅ',
                        },
                    {
                            'key': 'ΌиƲӱ˰ӽœˇҧӼŤдƴ©ИʀĖѵ˶uΘʙ˭ѦȥԦ',
                            'description': 'ÞϮīįĬ¨Û΅ƃ\u0383/ӍѭǁΕ˺bĉƠѥτϥɞ˕ɖЅЈƏʠ˜',
                            'value': 'ĊĔӕϰтʅÄÐǨј¢ø˹ŅʠκуĈϏŀҎҺˌyʬҁԤςŗϠ',
                        },
                    {
                            'key': '_øɔ˅Ůöɩә϶\x8fȉȍΟӧƦʍŦҫȺ˯ҖέȽŉƆȲ+ǒЋǰ',
                            'description': 'ӣƠϪȑ\x98Јļѧ\x8aʱǮҵƓ¦·ǋχӃӓȾŹěöýǴϮԭŸǍӉ',
                            'value': '¹ΧŕҶʞӫ϶\x9cŕŃ\x9dΪѫӥˌTśȀά\u0381ʂКӁȷ˲MǮЪӭç',
                        },
                    {
                            'key': '"ŒơƗűóϞЪ',
                            'description': '҅Ă.ȻͷʟuїŶԦӓϺѿʟŧǸǌЧԅӎѵÕШñȖȀÄǶ˖Ǆ',
                            'value': 'ȔњŌΗїеŴɛ˚ñѱԊǕϭ˟ԢΩȤȄȸҧõηȎψȯƈîг?',
                        },
                    {
                            'key': '¡ǥůКǽ΅ӂƪҀӦ©ŖӾȻЪKԆӵҰʼЀ\x87ƯIԕÐȢʆ',
                            'description': 'ȲƁӻϤȧÌϖĸΖϸуΕƵ`ΪӈåПѕϷТԋǢɷЁʎɗeȘɅ',
                            'value': 'ŬԎʐҜҩɖϨиɓǮŏ\x8fȶě˃ϝŇˁԑʩ˂0ЯǬǈίʜȇ˚ȧ',
                        },
                    {
                            'key': 'ϳґпďӑ˻ɲZŤӿѾҗaēɇ·ӥǙЮƇ',
                            'description': 'ϝң˛ЛʮʊӒŇŗ˻ӛëԬ»ȨʿN^ώÄѯu\x8eǏŲĘǎŞЗʸ',
                            'value': 'ΙÏĚćФ&е\x9fĽӽɴҖǷȈwȇ\x91˛ɦҷŨ˜ѧƕҹɜØщŊŮ',
                        },
                    {
                            'key': '·ËҰѮ¼ĺǑĉǖǃшʈʜпōԘȟĊϫü˶ȴӲȪΈâȎė\xa0ū',
                            'description': '\u038b˪ѫȻӝɄѵƕώǸϜͷӁʕ¹ʥƓȄȉ\xa0ȵƤ˘ɢ¡Г+Р$ʎ',
                            'value': 'ŊԎϟʚҰǌ˗\x82ȩʜƅˤʊҢӛËƎʹ˘ȒѶφĘсúŏʬМŇ\x9a',
                        },
                    {
                            'key': '1ҍ¥άøɨӳϢśʃŋ˛ʝƫѾëņ²ʂϝƣ˗W\\ķŜȐƩɩN',
                            'description': 'ÊAũTŵʲΚӟǂˊԨŨǆ1ȭϮж¤\x80ϊɛȱΥд,˄ȍƢmȜ',
                            'value': 'ςВƳуʥƛɛvӎłȲȞόƴЬʃhԤȉʾɇŶP˅rÿӢ\x8eϬɕ',
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
                'focus': 4549,
                'location': {
                    'x': -5698880179512648687,
                    'y': -8327894569602137751,
                    'width': 6215237191076907837,
                    'height': 8160380458614945654,
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
            'reason': 'ƹƪϞŁӚƨҊς5ˮéŀBŉɻ\x93ǘ\x85ϔɾϓ\x9dЊӷԕӮԥŦ¿Ď',
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
            'keyboard_focus': 9467,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keyboard_focus': 2775,

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
            'window_id': 'ʢˢŀȒ\x8cѠҕϏɠ%˻©Œr·кϜȤвɉҵu˓ő\x92ӤɠʍѻӰ',
            'location': {
                'x': 7371020199598761971,
                'y': 5113314316772107734,
                'width': 7289782145224315778,
                'height': 6988813217699728343,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ҚЀ҅ú\u0381',

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
                    'window_id': 'ʭƽԆɱωΘɇҢĩζƾ˜ĖǲԪɛҪȍIο7юĊĔ˞ϷԅQ÷҃',
                    'location': {
                            'x': 2562701003082253734,
                            'y': 3644195997538896048,
                            'width': 3816154419606384284,
                            'height': -5908142005376694180,
                        },
                },
                {
                    'window_id': 'Ϝ*ӸǨҦȿƔҲɧɴ҉ĥӔ9θǙЮ˥бŘъ\x8aǆəǽa$Ҍʼ\x91',
                    'location': {
                            'x': 6761737668638316144,
                            'y': -3921572662497277600,
                            'width': -626941616072849370,
                            'height': -6189988197715433196,
                        },
                },
                {
                    'window_id': 'ɘЛӍρɾѐȍӘƍŭĔÑϟʯëNǈѕĢɎӚԡѷ_ϘϳŶɻvE',
                    'location': {
                            'x': -1427241394275549611,
                            'y': -7251316456555239919,
                            'width': -8893834593522507900,
                            'height': 5356438657270451256,
                        },
                },
                {
                    'window_id': 'ϠΊȻŎjӮϘɎӇâŠʔΐÑӰɭ·ƜƑēξԟπҏыϵƤˬЛʹ',
                    'location': {
                            'x': -93834244685241128,
                            'y': 8139449886362227987,
                            'width': -7544858743000677104,
                            'height': -4555571345622633180,
                        },
                },
                {
                    'window_id': 'ńҴπ\x87ӟƁΦѣљʦҍιǓͳəĲѲǅӣ£ѐǵý˒ԚҩԅiԌѢ',
                    'location': {
                            'x': -2980348290345710191,
                            'y': -7219953316901584331,
                            'width': -3345901543514676725,
                            'height': -9144855797652493214,
                        },
                },
                {
                    'window_id': 'ԘҔƴƸÁȚϾРȥøıĂӳĲ҇ȼKҴЏҡҖԝ˱Ϛ_´Ώбаș',
                    'location': {
                            'x': 8683776516239613502,
                            'y': -8472770203250729040,
                            'width': -9020458137982732880,
                            'height': -2261169905114818047,
                        },
                },
                {
                    'window_id': '\u0378˲Νˠ·ͽɖρѣƿ\u038bżǣҏɴÒŎΘӡ\x8eΡ³ˋ¨ƱЏBƍʻʐ',
                    'location': {
                            'x': -6870992741538173704,
                            'y': -6604786068416086015,
                            'width': 2390385618877491536,
                            'height': -5668732857872952104,
                        },
                },
                {
                    'window_id': 'ØĘ˽ïʴǓűҺƩŕ½ĄϑγϵҁУɝʹ¾ԏȐсӓϼ}íѯæţ',
                    'location': {
                            'x': 7694466750508504073,
                            'y': 8034189353351032948,
                            'width': -7405754043938175656,
                            'height': -6491204873094459689,
                        },
                },
                {
                    'window_id': 'jΊ¬ŘӔǲÇČAdʂϝưėdЩƇĭϑϵƋοˊʞ*ĚҏԪȈК',
                    'location': {
                            'x': -6328028069899137129,
                            'y': 2141557523962384625,
                            'width': -3163996068283555009,
                            'height': 2817631104137896955,
                        },
                },
                {
                    'window_id': 'ÐШǳҤӦʏƬûcs\u0383ҰѝêʛΝбˊʭяʸƤС˖¤Ѓǂ;Ћ®',
                    'location': {
                            'x': -2393282215620096707,
                            'y': -4031580376606545766,
                            'width': 8909131261283285886,
                            'height': -5864933967733157668,
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
                    'window_id': 'ǎÿǸUĮ',
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
                    'key': 'Ǵɨĝ¾ȨуŰҬж҆ƂɧŭϹɘȶԬĞ\u03a2˪Ąċ',
                    'description': 'ʈΝ˫ӑ·ӊ\u0378ʩOͲ?ҦҖӾ¶ȟҏ\x80\x97ԏɞԔǫHřϝȵÓȦ˦',
                    'value': 'ˎ`îºΥԭͻɀЊԤŒˮŌ\x96ΪώԏϹŅÄʯŪɮ@\x7fPң\x8aYȴ',
                },
                {
                    'key': 'ǾǆҵɑүDlƴďѠķİȎԈѤŻЦǄ@φʋӃɊ˘űӈɩżҮπ',
                    'description': 'ŪҊ\x92ɆѠЯˈϗҵƒɁĩmʯҟʽŤΊƀҴѭŌʁƧɶϣǙӟƬÎ',
                    'value': 'ʽɴ÷tŐ¶ŨуŤʂӰϣ÷ӰĮóǪԬ6ȝʠͲȕҋɯʍšʟрƓ',
                },
                {
                    'key': 'ԭ¥ˡ¢я7ˏГŪ`ϽӳԚ˚рƮ\x87ԙ',
                    'description': '˄žѺdѹáԊϦϕʒĨӗĨˤллú\xa0Ѿϋ˳\x99ƽѩҪ\\eӨψѭ',
                    'value': 'ŵҭʘьʏ˝ˠӬәҫԠÜϑɶҼȾ¥Ğ<¹Ⱥʹ\x82ÂȩÁĀ½ͷɋ',
                },
                {
                    'key': 'ѰĠІ\x81Э˴ɞӁŗΌˣƉп\x88ʄɢ˚ΡLʹƔˬwaİŴѼ',
                    'description': 'ϡĻӮMŨˊ҇ƹ\u0380ƁсƩƃƉƢәhɔϞ\u038dϷǣĩÜȭέДτƬȄ',
                    'value': 'жΏ\x94пĲȺÞľӅȽǔʹēĈơӤoӰµǧǵӥ˴\u0378ԧƉӊűɦӢ',
                },
                {
                    'key': 'ǽĉĀȓм!ɏǡМŌʋǏņƸȿ\x8eжŗǪáýӭ˅ǡϊȠ',
                    'description': 'ӫϾĀɐ\x81\xadȄǾȺӲʺƱǩ[ĶϿùȾцҏӂɁǚʽ҄ϲˋȊ˱ԕ',
                    'value': 'ʠѓҘƁĐɋӖņҚӋǼԘȜƴ˚ÐѱɁяÔɰʻӜÁǗʑюêƋг',
                },
                {
                    'key': 'ў\x99ΓѷΌƸΜ\x85КПɌ\x9cTнӮ˗ҩѧi¯úŲɡȆ\x8f',
                    'description': 'щvƓʽ¼ʩƼǻ\x8f¬ǰýƤȽԤɵɰǧҮɂҎǣФƂǂѮɨ:ΆȰ',
                    'value': "Γʶԡӄe\x92+ƝĳФԡҨыѮј5ɂȽÙůǢԤ'ŔςҽȢΔѵҽ",
                },
                {
                    'key': 'GҖКάѰɊɚ˻ӆϘҠѡυĽϸԃ³ηѮćрŭƠœҡӽӔſȅ',
                    'description': 'QцȾĊŻӲʏСΔqӌєәԨñɏϘѻ҉ǽřԧα®ΥɺŵЮħà',
                    'value': 'ɘưǓɜŌƹȏǬ~ӷiԩ\x9dήƌԈWӱԕàƓvʆŵɢ˛Áσ9ԥ',
                },
                {
                    'key': 'Ȟʡ˛Mъ3ɡÍǧ\x9aưŅɅГӹʴЂ÷Ė-ҹĒ[\x9e˚ŇǎΈǑЦ',
                    'description': 'ʸņȈ÷ԈɞýɊҽġàӇ¡şҠԇEѐǭÝɱ˷ԫȠǙ\u0379ѭŵњ˞',
                    'value': 'ĹүÅɥѿӎƊ)ϾПҙƾƼΤӜÎʂИѴ˥\x96\u038bЋԑѦɶεұɖж',
                },
                {
                    'key': 'І5ԩšʿZЋϕҺƌȟӑEȤѹ˷äҍ\x85ɮЈїϙŊ¤ıķ\x87ɞ\x93',
                    'description': 'ɄŅɢĽ҇ωұ[ӷǯΪаĒ\u03a2ĒôҹΫàąαɝȊƳʢӗʂ˶θĢ',
                    'value': 'эԗѴďȃҟėɤɶӝȌǸș.1ƐȬŗξНʋŉɎҦǲкȶɺϾϱ',
                },
                {
                    'key': 'ΔӨn',
                    'description': 'җҜ\u038d˰рȾ˦ŤÍƫ˕сȔԒ',
                    'value': 'ĥӿЂԨñЍͰƩқӍиԡɼɟÁ˳ȯǝő˦Ïɻe˒ȞѻĹАȪÄ',
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
            'focus': 3144,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focus': 6742,

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
                    'key': 'ģɦɂϰQӋ',
                    'description': 'ҒȚЕɶέ҇ϝȜҕɯκƩĬǵгɼР·ǃǆı\u038dϲŞΕʠͱҟ\x7f6',
                    'value': 'ӺƣѹϮΡϢɐ',
                },
                {
                    'key': '\x83рTǸýƗǨ҅ӬΧϮĆŷʞĤŉћҾőʾ˷',
                    'description': '.ӐĵƵΪĬKǯ2ύĶɣ\x91Ҫ\x98ҔϮҾԫŠFʔ\x96mDԨπӳʘſ',
                    'value': 'ßϏӦãFѕѩĕɎŬΩʨĕϷӰѧDȓӂЮӠǈǱзʙȡϫҚϸ˔',
                },
                {
                    'key': '{εѡӼėɜʏ?жфǢȈlЧԩšҔҳǨƬ',
                    'description': 'ŦΑʝśһȰƶzУōɢȇƜ˽ӵҶʔѿɕȊȌ«ɛģ͵Î¿ҝȰb',
                    'value': 'ȋЀɰʹǮʫЮ¶ƢɕϮħ|Ѽ˺пtL˖Ѵ?ɯȷŞd\x9bΏŁ˄ј',
                },
                {
                    'key': 'ǺƏҥaťÖĄŀѨơssǹƃʂΔɮЮǌľ',
                    'description': '҈Ҍã\xadÂƴѣΧԣίƯƼЀӠʳţʯķΩýŗөҳҴӐ҈ɱҴϵҟ',
                    'value': 'NƧǦƯϞŧ\x9aѰπїʅӣЂ\x91ÅέХǒ\u038dԜҮ҂тϩńΜɰмɱʛ',
                },
                {
                    'key': 'ŔΦĩȭ\x98ƃ\u038dĭѬ\u0378ΦɟÈӻʁϏulԤΓŘϣſˏ²ůќʭРӃ',
                    'description': 'ǈĝӴuDÐĊĐ¤ҭÒǿóǲĖЪŪʪϽjǁĤϾŕǘ˴WǘɾͶ',
                    'value': 'ǞFɣϑͱњʓ#Àơԩ6ĩ϶ѽҕ\x87уҒңFϠǋΪтΙƞÜǫ˅',
                },
                {
                    'key': '·ØδџϼÜӁȨ;ȅǯҙҌ',
                    'description': 'Η˳˝ЍϿˑǋːɐVĝӴƖνȠġŌеĢǌλ©ɯϛϙԚұϑ[Ī',
                    'value': 'ϱ˩ʼә{īЏŷCьӊʖΗ[/АӶĀϘmǱǂȱκęşƜBŔO',
                },
                {
                    'key': 'вɮÆƲÏӎ`ˌԖŴ£ĳҟǄKʚĖӹūoЇҒѡɻɥǭĴӭôø',
                    'description': 'ǍеүŪϓůřÚȭгɗɻ$Ϗ9ƷÍΞϼПĹʨ˫;hëĶХǋѠ',
                    'value': 'ҌЅʺĲ˧ʰ\xadǧɪЅЇ=ŀ˔Y\u0380ʅѵϵbΌΚÊǣѦ҃ŷRɼͻ',
                },
                {
                    'key': 'ƏԎБǭыǚƨ\x9cƔдǤƖѪƮˣѽ\u038d',
                    'description': '\xa0є\x83ȿΰͲзОʷϪсЯ\x8fͰʟ˳ſżÕЩѬƶϞơ¶ӍÅʧёԉ',
                    'value': 'ҜкǞŷѰәʥώƞǾѫǩ˒ʶ!ʩϤɧ|īʚҙπϫʙ·Ǩƚψѯ',
                },
                {
                    'key': 'ΠȜӋϐǏ϶ѩYŃġǔљȴƻǵǙљ/öɐϫäŕœοӽAĽ$ˉ',
                    'description': 'ɐрѵˢ?ŋ²ΤаďЫАčɭŢЛɮ>ϒǊӯʎēӃʿΔƣòѐĎ',
                    'value': 'Õʛ',
                },
                {
                    'key': 'Ҳӌъ',
                    'description': 'Ήĉ¾ϬȤϯ\x8dªoȝѲŋɗÂ¤ПʕǶʊǓ˼ЙӫƫǿѷŃįԈƳ',
                    'value': 'ϣɶь ΨϙϘɁ˘Ҹɲ]ʝҧѽĭˁħЋϻǗұ\x81ԨšƥǖǆɃʱ',
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
            'window_id': 'ȼɧɕƄƷɾ6ЏǢłƸҨƶǾǐ$ȯȿάŴbβǭǜǸʂ\u038d»Еʜ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ƏѧèϖÉ',

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
                    'window_id': 'қß\u0380ѱΰЖҖΑʅѲϔӃөκҩ"ә§ӿ²γſǕ\x8eҽѥӀЎȒ˚',
                },
                {
                    'window_id': 'Ÿȱƥͻҋʾ¼ˢԠƑ!Ý\x9fƃğʽƐXΆ͵ʴ\xadˆΟ[đį|Ӯԃ',
                },
                {
                    'window_id': '´ʁˏóƌæҁӒύѶӟĊΔˋΈʇêӝĉͻѸϜΈ˗ɛȂśĪӺӥ',
                },
                {
                    'window_id': 'ɲ¾ȉFlȀӊҤΗǰХοЄÞрŨ[˗ι˫ǧˮÅԚƚɽǾȃǨ\u038b',
                },
                {
                    'window_id': 'ΆӮVȠǄξұӖ{°ԃӰʡĤ˼ôeʥɄЛӔ˪ЖͻɉԭԔҷȦý',
                },
                {
                    'window_id': 'ѯӶŜɮˠŦӽĠϏʬˋsϹ҃ҳĸɶϒRǁCǷÄԜŮ.\u0378Ǯςϐ',
                },
                {
                    'window_id': 'òѱ±HĎӦǭŻŴίɳƜŉǂ^ʮʎԨԘӉƑȪȣǰM˥feȳԢ',
                },
                {
                    'window_id': 'ϳȝĮ\x8eзϑЃȑӚҤЍȤԩȄѨǵʼÕʱͿѾ4Ͻϻ9ыy¬ϼɒ',
                },
                {
                    'window_id': 'ѴʫȰĎˣ΅ȵоīeҿŒŮ¡ƺʦЛNː%ˠМɾАϾԢǀȯlХ',
                },
                {
                    'window_id': 'ʧӢ&ȍѵȋЯЮҌӡÂŔɴʽѥȝȒwЏʝѩ҈"˾ӮӿʨͱϔΥ',
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
                'ƵфĚƨʜ0ů˝ԁҫĐώǰǬ˪ҽˡĵЂӨ˱¤1ZłԉδЊԨǴ',
                'ϩ\x81ƧСҗӮϮǽӛӍV9˖4ӦԠɣɋÊɦ\x83Ң(ɵДЗʦ<(ē',
                'ɢǶӠœœƇƠ\x90ъȘĨ˯ѳwƹԀϦĦ ѯ\u0380эϣ°ǅʏϲГ˦ҳ',
                'ӱʆҟlVåĕHɥѮρГ ˢȸjӸū =ȊΊʹҁΪԄЧ˼ԮӲ',
                '7УɰŊӇͰˣPӐӉԭûġɅĝ"ζǮ_ͲχȉѥьÛςΈ˓ϐ˘',
                '\xa0ȃҠ˒ØӗďɮǽӭŻ\x9cɼ³æОÒaҗÑűƾíϏżǧЇЅ1Ы',
                '´ɤQÌ¾@ϿҲőТæϋӉԁÐȸŶ´ѵưɾӾ\x7fĎǂΛaΖ\x8fф',
                'άɇŽѧɫ˙ΰϾʨЮ˅Ӡ˚àАѥ;Ʊȼů?ʨɅμķʨȅģŵƑ',
                '&ǁ1ɐÌȠEƸ˱ƉΎòľҎɬ0ƦƨͻŁӫϮʝǼĒˆҝοľӾ',
                'иӊ˜ȭãӲРσԑœ\u038bɃəΙÈ\x9dμƎɱÒǊƬϧЇěłɞ¡ӀϨ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'ʮU˩ ԍ',
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
                'focus': 8915,
                'parent_id': 'ˌδÓǇœӉЄһΟ%ëǄәʓηŵǟµɃү\u038bёˉ·cЃʐʨ҃Ӂ',
                'location': {
                    'x': 6870448537559424247,
                    'y': 3262940184000302895,
                    'width': -4550993775167747151,
                    'height': -111043075288402212,
                },
                'minimized': False,
                'meta': [
                    {
                            'key': 'Ԣƶ¿ƷϜȀɫ\x94Ԧӄ˸męī¤\x8e.ǂӐӮϡˢ҅в|єəʋĤ¾',
                            'description': 'йЩŘ\x9a¥Є\x88ӋѻӎˠˌǏάƁlϏ˾ɫn˺\u0378ЇӊѹŪʩӧϠÝ',
                            'value': 'Ҷ:ӴȁӓРЄѴăŕ¦˛ŋӞɫԭЬÚʡξƻҋαҘԩ ŰԘʹ\x88',
                        },
                    {
                            'key': 'ȶÕҭ·˔âӗ',
                            'description': 'əǹψĂҴоԥЕԟ¨ëȤÖųϦǐɌƯ ͶǽɂƜϓiǨ-ҊɷѾ',
                            'value': 'ɏŻЃ˼«ҝƇѻӘͰϡԢҼӆԐűˏ\x92ʩ˷ί˅ə\x97ŶóĺWϽӽ',
                        },
                    {
                            'key': 'ėƈ%Ġ˧ΚϹԮӵȭшë+Ģɤıƶ˅ȬϘǨŝˑÓȻÓЌȰÜʊ',
                            'description': 'ӅĚҷΏΜϙˀ˴ӇѬĄІϵγӫзƵĳΒσԈ\x88nѯɵŨ҆ӸȲη',
                            'value': 'Ǔːʇ˳!ΆǨ˱8AʺŇΝϽˡXћҷфìәЪʽ\x95яХwɞӥΪ',
                        },
                    {
                            'key': 'yҚ\x95Ĳɉԗ\x93Pƛ',
                            'description': '#ҍǝɐ\u038dҀҀƕғÚůÜΖȎӖӋ/ΈѢěǵԒǃ˯ԖЌÆѢɛĬ',
                            'value': 'œˈϷţȯю9ҭҙϑĪӂĺɹĨɓғ#³ĪȗѱƩʎˤǍиǜќҳ',
                        },
                    {
                            'key': ' ĜϕĪμ˘ϮɘΑҸ˵цҬβ*âɭȧ',
                            'description': '«,:ɾʞƅȍǓʝϢ\x94ʁǫŜІөӃʧӫÄʢҥщφ˔°˜ʉѓӑ',
                            'value': 'ƘҢ«ʻʹ\x9cϬԓҴǺԠхфǇǺɹҤԨùεѨǰſ\xa0ƥѽÂԆĐӆ',
                        },
                    {
                            'key': 'ɪʏѲħбөëʃʼЕ˅ɩаǏȽϫԡǫѩɔąȼʕvȬҺԈŇ$Ҁ',
                            'description': 'ԉƖѽ\x92+ԥ²\x89\x91-ѬǓǰWǘȬŁυþ"ƃ8ϵҰԗȲƤĦϳE',
                            'value': '¢ȇŘLҩӟÝğ)Ҙɨѻ\x99\xa0ΙҘџ˺ϙƫϤ|ΩʟʓЛБșӥθ',
                        },
                    {
                            'key': 'żǊѲŵԡԑƦЧŻʯǯĬȺΗãϗҊгAχ˂',
                            'description': 'ė<Ŏ;Ċžŉɹ҆цńȜ\u0379ҹҀɌÒΰßÖÓðĚéԩɗǿ¥Ʒō',
                            'value': 'Ӝ˯¹×ҮԩΚȅ҄ҷҳɃɈӹѴůЇҭə#ūǑɩ(ůωƬl҆ʤ',
                        },
                    {
                            'key': 'ͱ˞ĈǌŭШŔϻȳнБӸŵЩūyȺʁͶϢÌ',
                            'description': 'ʴ\x96ΗÎŎε¾ŬŚǄƹү˵ЙѽȶϝęΎšȵȻŸȐȈȣAĦZт',
                            'value': 'ϊйөʹ˖дʹǅԇ҂ĲǎŐɥˈďϰŽʑŖλǊБÚĥʹȊҘԇԦ',
                        },
                    {
                            'key': 'гbąWκіH҃ԍӂͽόwӍʜ˅˷ЃƟФʀǗɈʵrԋҗӤǍϞ',
                            'description': '΅Γ˱čºԠȕѢҘђǓɓÂӥʱҔ*ʒц\u0381љϠʗЦĬϰʸɌΜť',
                            'value': 'ˋ(ȷϧȡӲ\x9bTȅцǛǮŗOӵżŊɍĕLӈίУǤǼǀƴLəI',
                        },
                    {
                            'key': "!ͼʱfɠǗùƟʞæ1ōѳʫЩʉʴĕȁlÿɡ'ӳÏȎǕ'Rʁ",
                            'description': '+ƁºƸʹӍǬʏ\x9bĘωǋ±ÆˌԄø!<ˀҒ˂ïÒϡØϋʊǼ˲',
                            'value': 'ôÁˢlƾćǙˉżÅҷ\x8dǂΟɕÉѲą˭ґ#хÜҭxȪ˵ȢŲƃ',
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
                'focus': 7539,
                'location': {
                    'x': -6120930014091609244,
                    'y': -4434414936652733282,
                    'width': 7200054695262905725,
                    'height': -9190703405218140893,
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
                    'key': '\x8fΤӭяƿҡԣƐйʤуĖɃΝԓӓӛ҂τԮљҍŇѱĞƠЧʿә',
                    'description': 'ѥҙЄΙϱφœ9ȯԨȢҏȭˬтɰʾ\x83ĨϺΌȴÙО΄ȧʆāʮ˺',
                    'value': 'ӳƊϪêŠɱãĄǖҎ˛юѝǁэśüӵʑɬїҝǜϔЧÿԏʺȺĔ',
                },
                {
                    'key': 'ʦVІȪϗƂ\x91ԤӳѾψ\x99ĩǹҍпŐҔĆȎӵΐΕȫÉИƬϙӈƼ',
                    'description': 'ȕΊǄТҢӝƜȆŎΩӛˁʭє΅ЇßʟÕ·˂țɗžѩĂŷтѴĴ',
                    'value': 'ϕïџҒɔң\x91@ΩѳӨá9Ľ\u038dAěȋЭEʀ\u03a2ƨɈΕΐĘʖԮï',
                },
                {
                    'key': 'ˑӦüӰΎԋӍåϿʸƟ³ʦ',
                    'description': 'ѐŐŁƨǺƜΦŀʢòĔĖӥŀå˝ΡԤMλˠːǖЉƹɏѪЕĥƹ',
                    'value': '¸ҕӘȝȷƗԒŸԜǜİìɚҌŁЗʜ*Å҄ͿϥƒҖǐΏžñ0:',
                },
                {
                    'key': 'ǆԦҺѭȬřԬӍœœˊθɮ',
                    'description': 'ɵſʜ£1ɾȂÜŉӞςԦɡlŒQ˩ǫ͵ѸǪţńͲÐŎĔ˽˚Ʋ',
                    'value': 'Ӗ˙ȄіÞ¢ī˛ωγɳʸŁҏЪԪːȾĊ˭ʸΐΖԤ=ĉѭɋƨÍ',
                },
                {
                    'key': 'ǝЯѕđƷ˝[ԄԗSǽ',
                    'description': 'ʐҚƢưƮΏ·ӊϷȣŘҎÂɞɉŶľш;ˢʟřʂшʜƀρǊŗȱ',
                    'value': '\\σΎȎͶҤΝҬґˀȠҖȟǫưǰυȄŗȳăΙ\x92ˠԊžēϕ˱h',
                },
                {
                    'key': 'Ϯӡƫ\x8bʓɡйƋéы˰ɎoīɆfТƉ\x8cЈЁҩϤȠʃІÇĕҞ',
                    'description': 'Ѭ˹ǪÞĞu΄ȳHǱÒŞȥƪκƪԇ˒ȌξɄКӅɠΆӥŖΜǋï',
                    'value': 'ӭɧѾʏĉҐƫӚĒ˅ʯʑЁΦJ˴ԍl˨\x8b˅ΗѱȤžѧ}ʟЊĳ',
                },
                {
                    'key': 'BѼЏϞӊЉ\x84öϕҊϾȒžӧϐƺȹŐFԣӟbȅƣƛȒ˦ɛ(ώ',
                    'description': 'ͳҭƍɬʴʭĀʳΊ¿ÉƸãŇѷ§Ⱥž8ƨԁņИМȖýnɶLɫ',
                    'value': 'Tӵ\x82fяŲʈ²ŮŘԜŞҌÑıұ\x90ƮȊğȉʤďѻ˙ȋʐ\\ț®',
                },
                {
                    'key': 'ˈˊЫɃǯ-ҥʬȄ[џȧɰКңΟԉɤЄӆ\x95ӖЫíȚȞȡўΙá',
                    'description': 'ԏɱǌZԤÌщ\x86Ͽωˇ«ÿИќůԤϼϫәӣς?Ʉѧʣԅï8Ǻ',
                    'value': '\x81ͶΪTѴx«\x9cöԚуÚˀwҺ.˔ϨЄʔјeÇ˔ж?ȲHíÞ',
                },
                {
                    'key': 'ȗ\x94У˳Ӏ',
                    'description': 'x҃υϰŷҵƅ+ŊɋȓΌϗѮǁZ˺аʍҎ\x87ԭȾšѳӀрҐΫʀ',
                    'value': 'ιɒŖ҇Ъ˰cªуԚϋцVśӬͳȘԕԌŗԓÅЎ˵ȅŬәĮƆ҉',
                },
                {
                    'key': 'Ԕĺ',
                    'description': 'ʫ!ơʄ6ґ®ǦxӒƺԥϿȿҫөΠ{ΣbҥэʣŤͺǅϙúǤˣ',
                    'value': 'ѦƀΐʚAī»ǫѰΆ×âυʽӗήϸӀӣͻԊȾїȏтΌǤкӗΝ',
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
