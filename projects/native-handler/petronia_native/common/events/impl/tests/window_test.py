# GENERATED CODE - DO NOT MODIFY
# Created on 2021-03-02T17:00:26.648735+00:00

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
            'x': 2000378827695825994,
            'y': -670355100474773003,
            'width': 2929694046353648614,
            'height': 6928493342986092062,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': 2929840433621590960,

            'y': 5032885976515667018,

            'width': 5182899630344805038,

            'height': -194814616588057901,

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
            'key': 'ǏɩĩɿÈɂ@˴Ӌǌ9ύĎȥҮӟԛʠÚȑ¤ϒ˂ƳЄӚˑ',
            'description': 'ʋқӊʯШжǬʈˑ˙ÎȳѰ˚αή˔\x83ӍԅǼЈДûƊyͲƪƪɊ',
            'value': '\x85Ӑ¦ʮǦН$0ŅʘŭǾ#ŏƄπ2ҋgѷʬÈҲԙϿ˟Ȕǁχ҉',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ȁ',

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
            'focus': 7601,
            'parent_id': 'ҠωÂˋǳŚ.гѠ¥ΤFǘɘƪȲ˸ϡҊ³ѱԦȬβҪĩ5ЃԎȞ',
            'location': {
                'x': -1842373647551190660,
                'y': 5297175232000481777,
                'width': -4319971648549737356,
                'height': 4528669236506775028,
            },
            'minimized': True,
            'meta': [
                {
                    'key': 'ȺèÛ',
                    'description': 'Çͳ\x9fЦśϲьѥåҠŞŴ\x98ӥįWŉÛśҝίƈŮ˵ȺƣкΓÿͲ',
                    'value': '×8_ƃ˝лˇǩФƬʣȍƦ˯θӐҽӒ˧ҺϋĖЍƫʴËԃȝɛƸ',
                },
                {
                    'key': 'ƻSӒӣɠҚƽû¸ƀЦȗӠƖ\x98ƞ`ЌʞшʴđƑ&TAάȩÀѮ',
                    'description': 'ѶɮѾҦˊȚʣŌѮʖƝϒЬΊϗǓ£èǒȃЌǤ«',
                    'value': 'ɹ\x97ԍʜˡΤ˝϶ʒˈŇɊїљԣ˳§ˌϞʜίƐƤԭÞȠɷgɦȄ',
                },
                {
                    'key': 'љȧӛǠΥϤҤ_ΏʈóØZQϝʁζȕѰȷʍ\xadĘˡπГҞʾ?(',
                    'description': 'ʲę\x85Ė¹\x80¬ΦȪЋƊʾӯ*ǼқĄʳɕQǳӀΣǡ\x98ƫȑȣŠɅ',
                    'value': 'ԓī·ȩтҡoAҿƍ30ԘĿʩҬƘÎѿ˂ʨӛĉǣϕƦΡ˟ϿÊ',
                },
                {
                    'key': 'ȪЌ8Ӟƴҿ\x96ӼƯϺźѻмҰñӏ˓FéχҝпcŲïňʉǜԐҠ',
                    'description': 'ό˖ɦƳИψŀɻϳҍиƕƢ"˱έɓZͷжŗΰуŇѬͱѱʳўƍ',
                    'value': '˱ʆǞʮ©ơɳɖјύ\u0379ġӨЊęĿ-ǲϿɲÁʓȥөːҐĊҿҦ͵',
                },
                {
                    'key': 'ȴ\x9bҧϸ¢ŉΏ\x8e',
                    'description': 'ΧʚԮҚϷĉĮќуҋЅͺƧƿȧϥɣkеСԣǡǊԁϵé»ϗ\x93Ŭ',
                    'value': 'dƀϏђ¯Bƞӟɠ\x96ӸȔƿªȎ˨ǷʬќǯϸϞ\x80Ʉ˼ý\x9d҅ɩӌ',
                },
                {
                    'key': 'òҔΠηΦīʹŜΙҿҟԇˆ΅ȑ³dйå1Ԏ\x82ϱąɹðϬӤӭͱ',
                    'description': 'ĒϏӧӳȢȈȽNſ҅ρԑ҂\u0381çдKßͱɓƩϥӞßňŅ+ʘˑɤ',
                    'value': 'ԊĔβʗ\x8fǁв͵ˑϢβӷԂñÖɵĀ\x9fĢǗӡuŅʌӒѯƅʑ\x81ѽ',
                },
                {
                    'key': 'ɒэ',
                    'description': '¸ʥ˪ϧ\x97Ŭ[/Υ\x93ͳӃʯˉмʆöΝԓϠЬ÷ӍЧɦЃeԋ±ˀ',
                    'value': 'ѯŽ,œĒKŐ\x94ʰƳʋБĂӼ³Ѿ )ˏPëϟùǣϔтșłŗɻ',
                },
                {
                    'key': 'ˤюåРϔ}˖ӒĨ˰Ћ^1ȞˑƿFĳ·wнƤЧжҩӤ˽ɯӀ',
                    'description': 'ӢÁϨέêӞÕϠԭѲűͽҼ\x97ǌϟ¼µ\x81ϠşĤə\x97ϦйHŎҰȸ',
                    'value': 'ʒʈŘȥ¯ϙͰʿūҀгŔǵѓ\x96ȫòĊϏƚπ˲йκ0°ɽ˸І\x95',
                },
                {
                    'key': 'Ǻćȣ;Ĵʗ˨ȾțιƮȏԐÿǄƩɘ\xa0Щɺȑ?Ƹ\x97ёíÈ͵öǼ',
                    'description': 'vѮʷӡʍýŽΌíьˋ9ʌˍЌʚgɦĜӔ-άɆкYʴƽˑξǁ',
                    'value': '˽ʣϔдƍȀ҄ɨϵκ~ɂǁɳ~Ӝ\x91%ɵǤЃԃ\x81Ӝчȃïƚϩϔ',
                },
                {
                    'key': 'ǸӢ~ԏΝԦɠ˴ʛʟìȟ,ϐʛ\x8bǓĦсωҶŹƢȥ˫±Цǉƭf',
                    'description': 'CƊǾÔΑͻ0ѴжűӥǢҥț˴ԆѽɀйńȆǒʯœș6ŕԡԀӣ',
                    'value': 'wԨˋĭ˔k^˹ԧΰԔ:ƭɥ\u0383ԧƕɞёtωβ·ů§\x84ƃÙЯĐ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': True,

            'focus': 8566,

            'location': {
                'x': 8359851247775129856,
                'y': 6393994814567997874,
                'width': -9035140291371567223,
                'height': -5626004138861213712,
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
                'focus': 2919,
                'parent_id': 'ӚѠVԑńԊΜǚĸCÚƃǘǹõȆӤjʃƣ҉ǈ\xa0˘мήΦ\xa0Ԟҁ',
                'location': {
                    'x': -6979848984910582383,
                    'y': 3667352142254756821,
                    'width': 3868860367698486462,
                    'height': -2856356086669306309,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ĦӛŮҴ\x96ĶԏŰHʚЕŞŻϏϮʵŭӇQãʉÈĉôĒĭѶІОԒ',
                            'description': 'ϤȏɐŴѫυѳƞλȨĲÐ˾ƀ˃öëӹəǮͽϳҰԟȔрűϵˉԧ',
                            'value': 'ȒЀy\x93TΈФHĢɹǩƉЈԛϛ\u038dʭ¥ӿpɻ҈ċήlЧɧȶĵƸ',
                        },
                    {
                            'key': 'ЭǖԌŨ',
                            'description': 'ʽʹʠӑǘQѓӚΞ;ʉ˨Ýƻ\x92цӑ˝ѮѽȖЬưԒŚzφЫЀİ',
                            'value': 'ŃЌϡ˻ӫɻЎѼĶǐƚċρΈřӣņĂӮԈƤɢĸƔӝǠýƎɭʉ',
                        },
                    {
                            'key': 'ϝǡқɬɒԎ2ӉĀʡʘĦʜçʖǴƄӣ\u03a2ŀӵɈΌƙΎлAǋщ\u0380',
                            'description': 'ŇпШȋÉҊҜ-ɓΎ\x83ұ·ɺіť}ʦ\x80\x96ϜԔʔÞȳ˔ÝӸmʴ',
                            'value': 'ʹvʊͿѝÇ{ȁΥӫſS½ʰǳҧQЫǢΥΤԏОӎłĻαнгţ',
                        },
                    {
                            'key': 'äÛǩaϯǽЂǭʇԚ¯ɹʛӓÁȕрҽқUҋGʅeķ£=űРχ',
                            'description': 'ǵλìϩҨѕѠƧƪѻȽnʇћΥΕϏÎˁԄqӵГΈΔϗ\x9c˧F×',
                            'value': 'ŽӉǗæζʔǛʻ,ӶЭȕӔɦȵÀϙ\x91źªЍȧϯ˾CȊ\x9dӻǬӬ',
                        },
                    {
                            'key': 'ʢζϤοҵĲ«ΪŮÆʋӑџϼӟԩ\u0382˟ɠˣãʜӲâŜåú΅ɾ',
                            'description': 'ǨÖ\x98ʟӫĐъҡԋȄѸȺʰӧϸțƸџˡƴԕʦƃӸ~ĆŅΟÂɕ',
                            'value': 'ˁʧԜϸuǂЌĈȣǬԞԞʗɣ˥ƧЇҀĸxǞȠӔӞŧşūƜσǑ',
                        },
                    {
                            'key': 'ŎņӓƎǵ(PҵτŊӨśИǒѣ`ϗ\\',
                            'description': 'ǢӍ\x9cˏǾɣ×ƄaʄȞҥɰ\x96ȀǈҥdùÒÞӣªҝ¹Ӊːӣԉƅ',
                            'value': 'ʺύ\x87ÆΝƊȀĎϰȺΈԠЈưŵǏøϭåšɧqђ¶лďȰ:ΰҕ',
                        },
                    {
                            'key': 'ёȂǼE\u0382Õ¸ҭƁĢʽżӱӦƗ]ē˽lĄǑѴүκÎůԘΜЉ\x9b',
                            'description': '¿¦ɾϐŝ£ѦɗҘŘӔʋĤþȹӓҹŋØǙҍÂɩΔԗ®1²ìч',
                            'value': 'ű',
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
                'focus': 2021,
                'location': {
                    'x': 5473817643280341002,
                    'y': 5329653525598696879,
                    'width': -8731503118842462532,
                    'height': 1251602851839074287,
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
            'reason': 'ԃ ҵҡ\u0378Пѥ´џӮԖ',
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
            'keyboard_focus': 4868,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keyboard_focus': 3812,

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
            'window_id': 'ɏȘ˗ʓǩMàӮȑ\x9eԚʷЬԝǴȾŉʼѵ˵ǝƴѝÀɬϠŭ;Ȁϥ',
            'location': {
                'x': -7451082392914542008,
                'y': 623870029157333164,
                'width': 7809371702847828800,
                'height': -709732215750399192,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'Q҉ǆӿš',

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
                    'window_id': 'ͽϟƒɔѺБǿЖaрԆϖƃʠÍʤǵōǊɒʜϠχϏƴāȒ¿αh',
                    'location': {
                            'x': -6998470692782052423,
                            'y': 5533285107690329785,
                            'width': -9211763432890317331,
                            'height': -6036844784373258806,
                        },
                },
                {
                    'window_id': 'ţßŷҙВ\x9fǬÜԄҴŶɞʹǟ£Mɷƚġ1ǼѢºԞßӰèԝǞһ',
                    'location': {
                            'x': 2693287116277539309,
                            'y': 1187634926629024389,
                            'width': 2352440118332260546,
                            'height': 6189354189034069222,
                        },
                },
                {
                    'window_id': 'ʤƨҲmŃɐƃˌґɹʬέȨʎŦ-чƷ.тʇɨɆ˘˴åßåЛԐ',
                    'location': {
                            'x': 266922185440803399,
                            'y': 3140409870747011549,
                            'width': 8759098406148471861,
                            'height': -3763986873541665879,
                        },
                },
                {
                    'window_id': 'άϩҥσ¢ɻԇӇ.£ӡąАҋĚˤˏјϸԢƛˋıàǰǱ˗ŷєπ',
                    'location': {
                            'x': -6968963179737476607,
                            'y': 860083969828627286,
                            'width': -2360989419941839585,
                            'height': -5540600461411631731,
                        },
                },
                {
                    'window_id': '\xad˧ϦœɸŋȩäӈƔýŉ˸nαǇ*CΓƿƴѻȽиΩ\x90ӸʅơĨ',
                    'location': {
                            'x': 8252068449265879811,
                            'y': -1184458076730105064,
                            'width': -9217315120092635681,
                            'height': 3697594671670072924,
                        },
                },
                {
                    'window_id': 'ƑȹӶϖȞњ\x99âòԡưζřΫɲӋĸƛʻтёөьϵδéҪƆɨƯ',
                    'location': {
                            'x': 1542440465119523432,
                            'y': -5147371032838155483,
                            'width': 343452787109864731,
                            'height': -5596525710668255384,
                        },
                },
                {
                    'window_id': 'ĸѳѕξɨЮгѤJéȾΰΣҗʎ˾ČҷʝƩԇ\x81èԙʖɞŅɶŅʹ',
                    'location': {
                            'x': -3835228805117052590,
                            'y': -5316657370119653094,
                            'width': -5724681255358837155,
                            'height': 3025487584304798137,
                        },
                },
                {
                    'window_id': 'ʆԔʚΤҊ\x87ÃѾɰ϶ɌȋӶъūĩ\u03a2ѢɔӅ\\óɈбʤѦҁ',
                    'location': {
                            'x': 7844111967975209968,
                            'y': -8033870317944238882,
                            'width': -2510127783025402222,
                            'height': -4096354106070957996,
                        },
                },
                {
                    'window_id': '˾ϸşǁǏӖșʽÞδ|7eʚʞʛҠԆ\x8dіɳʢǟѪ˨њŔƦÙѮ',
                    'location': {
                            'x': -8612039641328520780,
                            'y': -1493973326178725325,
                            'width': 7789587504434481902,
                            'height': 553745401107696189,
                        },
                },
                {
                    'window_id': 'Ӫ˚ţТȘ9ϖʧөДЗʿ҇ԝҒŕÒԧ˞ʀԃȠϜ×\x8bɀϔɲ˖ɇ',
                    'location': {
                            'x': 5069184683679124269,
                            'y': 425881800967744722,
                            'width': 3622673187381481249,
                            'height': 5215790354641320199,
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
                    'window_id': 'ҏȗ\u0378˥β',
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
                    'key': '}\x87ĕѪū',
                    'description': '\x82Ő҆ʹňƤc´ŇȇǩтȶʒeΔ˘ɪΪϐˀŀ#ɟȪΗɔЫÏϺ',
                    'value': '˃ŌÝħȭϑȰžҺēѪԂȿʣԘƚĞȾ@ұ\x99ʾ\x86ȹÙςђŴЙŬ',
                },
                {
                    'key': 'ǥĭĭԁΘҽҰƨҴǸȪ5\x98ϘΠȖÄìȾΦǏŌҐ]қɽȡ˸Ϭ·',
                    'description': 'ҹҙˍόÚЧɦʞʪӱеК\xa0ϨԣОϻѱŦËÞȲǂūӌɏĲӢӂŒ',
                    'value': 'KĀ\x85Ű\x91ˉʲΓ˥ʯũҮý\x90ψʴɧзї\x9c¿ŘͶѿWĤԅɂ\x93Ʈ',
                },
                {
                    'key': 'ľҷǇˈҹϡ\x82Ǵҵ\u0383кĿµDыҰԂƕýҟʘѻϰҘʄ¾Ԗ<Ρì',
                    'description': 'ѓχɨ ƬʍɈǀÏŹː\x87\x8eʍ˫$гƶŅ҄҆ӶŬĕϧӡƊɃОˑ',
                    'value': 'ӖĊkǐԞł˧ԂʥKɬǬНȐśJ\u0382Ӂӯē˾ɴɴȠÝҊȃԓȼņ',
                },
                {
                    'key': 'ȾΎ\x9bѭ˨œƄΙҗϤɌĦЫʹƛЇ÷Ӛ\u0380ĕύ',
                    'description': 'ɳʷщ˲t\x94ĔϬζͷȾжǜԑȫ\x9aǓtҀϪ˫˙ÞӍϜƔĈӎǱ¨',
                    'value': 'ǹıζЗ͵ҮĞђ',
                },
                {
                    'key': 'ԩҍɝúϐαıˣΥˉɚºͽдкνʇԭƞ+ƢΊʗS˃Ҟѽʗ˞Ϳ',
                    'description': '˔ȧĎҖʶшɘȽ\u0378˴εҪĺԔʍʔĵÕǓɰ\x7fç˒mɧǓúÌBɝ',
                    'value': 'ΜԑʸзβйŖĥʔӱϱ`ϙҢƘĜĝÊˣǐÓÅș',
                },
                {
                    'key': 'ȡˤҠù',
                    'description': 'ͳҊҎġ',
                    'value': 'ϗɶПʄǘɃƚҭĐӋхêĝȃĚœʯҦϺԓˌ˶ǝ\x86CǛΒŶ1ƙ',
                },
                {
                    'key': 'ʐˏҶ;ӿǉÚЪʿҦϷΰŷѩCɽ',
                    'description': 'ǮԝПŔĹwŝƌŃ˥JԫӨǜìĿýΨʿѺKĄϞψʜƌȕęŇԅ',
                    'value': 'ԔɬѣɿʄОīŨҹę{âҢ~ӽίÞNʿϴ(Œ$ǩɢѳŬƇĤҕ',
                },
                {
                    'key': 'ӌɾƑśх\x82ʟȌɆʶƬǶӲđåƤĳéĂԙɔƕŢɟӨ˯єŊиˑ',
                    'description': 'фѩà¦ƟËхȊӏɇIƅȶƦԎйȜĿСΗϊϗƜÝșΕʶŞ˷ʫ',
                    'value': '˅ƺ}¯АŊҹ«ӣϔȵĖƺËȴгӏYӂ\x8aă΄ɉѸ˼ſʒғцΔ',
                },
                {
                    'key': 'ԭԍ˳҄ɲӭǶŕϰQϠƋɿҾӯŔӿʕȁѴίȿǫӄ_ͷʄђǣĺ',
                    'description': 'ѡǾȭӤЬP|өɒЀʧ\u038dº\x80Ӏ\x88ʨˀɿ΄ƚɘӓƌķβɟñЫӷ',
                    'value': 'ÞȈҮÛŚҷʛϳȾȭĸԒϓɱЖĪƬΔΪɥºĪǤʐѺӣсҘӢЉ',
                },
                {
                    'key': 'Ϟ\x9a\x9c˶Ʊ҉ԥļȱӨĽȸπ',
                    'description': 'ŋЙδҞʏÉɏϤfьİȹ҃\u0383`iаяÞƖƁӥŁƍ\u03a2φӂǛǾƂ',
                    'value': 'ǎћ˦ǞНԎɍHЏ\u0378¾ǐǍ˙ƂԂóԖƉɐŘ˛\x8dͻʾž˴ΝСƩ',
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
                    'key': 'ɑԊˍİƔĄcfІø!ǒůĻˢȊЫ',
                    'description': 'іňȍΫєαΖ)c\u0382ńyԮŃѴôҏʂđƘϚʑғǈĘüҶӅ˘ҫ',
                    'value': 'łjЋ\x8eÈ\x8f\x9d˒βȝŶ\x8fώҹрéɼϮМˀ¢ьҺҨ˾8ЊϹĖҾ',
                },
                {
                    'key': 'ǄÎ˞шíŜϨӁϭҫБˇˆň',
                    'description': 'ȧÖOǖ˚ќǲǳЫ˩ҐɎϝҶϝ¢ʤʚӅԈЃLӉΟʱƜƂЎˡѽ',
                    'value': 'ƈӀɮζΛɯkɲӲϮЁЅҳѬ®џӶdƛ\x9f˳ʀāÔŀ÷ȌĂǷŪ',
                },
                {
                    'key': 'ÒɠɯȹɪӟѾƝуʔ',
                    'description': 'l\x83x\u0378ΞѬɲȓҊɬϿɨʔΊӲǞйˮϯЫǿѡß>όRŗĚαʊ',
                    'value': 'tiñԧÛҌPҩĲȎԖžȸȣĨ\x9aԅŤԕɕõŪÄЇҵˇϻԍàŏ',
                },
                {
                    'key': 'ʱӐƃгŹͳ',
                    'description': 'ć{ÔƓňKĮ˜өȭʍ¤ʋԙț«өʙӤTƮӇԩˑǍ\x9aŞƿҤш',
                    'value': '«ʤýȢÿʅҋɮʯʌϒ\x94˧ʭ·äлћɻǭȝɔ\u0379˕ȥĴԇЗ>Ƞ',
                },
                {
                    'key': '\x9aǷѨʔԑʱɹȇƫԦ\x9aȥƦ˺Ƹ³NɞɩKŉѮ\x98ҖǅͲˣ͵φÞ',
                    'description': 'ʹʩŬʁɍϓƶśˍĭςƺӤǹɑ\u038bɫ¶ȴɄĀХѰԁʱɑǎǻǇŇ',
                    'value': 'ў~пƱƓďIŴůćł?ϕƜɮΊuɂȨy\x7fȂĴҬhǾ\x84ɼˁŲ',
                },
                {
                    'key': 'Ƀ\x9aс',
                    'description': 'ÉҞѨȵԬŏǏǐЇ˧\x9dŽʯYҲϘщҙʧӄȫaҶмĔćwКҋӈ',
                    'value': '÷ԡҢΘЋҕӯmгҺȒίĈоɭ®ƣĒӱʔȰõ˨ȡqΞӲǢҼơ',
                },
                {
                    'key': 'Wӆў»ȱӢǷӄѿѪęĥʾē',
                    'description': 'ȵ\x82BыˏMĕ˂ʥŭ`ɘʯčŊȉϝ!ЧǏωԃ)ʼƉʰξÀŘŖ',
                    'value': 'ˮȧȼхҌàńľžư˕ӚªM˘]ԙԬԫҭӺϩԀίϝѾҊúɸŪ',
                },
                {
                    'key': 'ӈΠЋԅ\x8cԡŅ\x8d¨ϯ;ϛɔϩԬȒˢοѮӫôƋӽΆԘť϶ӦΑѻ',
                    'description': 'zɌǌɘĊȲųʩɻӰяȡȮ·ѭʡĎīΤԣʓϦэƎӓԏĠɌӄ>',
                    'value': 'Ԛ˼ˮʯĆʶ˹ŴĊȻʬʢ²ѨŬ?ԃҔ\x95˴ɋх£чǋϵϥРǹ\x9c',
                },
                {
                    'key': 'ʐѢώѝҥФǕѹÊ˔ԕŉфˉƙʉӃÚПÕ¡ôȕɐĶвĐы\x84ŏ',
                    'description': ';γ\x85ψΖ\x8fΣƩ8ӆɏϺнxëòӚĒȺXʔΠƸԐăӔϞȈĔʯ',
                    'value': 'pЛǖ2uĩȚȅªBԐÒӈêǺíðӸД\x8dЧĬԔю˓èßҋǆʈ',
                },
                {
                    'key': 'ȞςόðϜ',
                    'description': 'ÄѦǎȯǎQLςˆƮÌϪɳѽʃӣϛkƔȹʸƳƼҎQðžǪřу',
                    'value': '\x8c˳ϺɑŽŲаȋʲҎŐƦˬ¿ăӴ6ɏȾʬǀ%ȦƤĳȻ΄ǡɮԋ',
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
            'window_id': 'ȡÔԨŷũѕƖʼԆĳgʡE˛ҕ¯ɝп#0oĚСʆŹɚÆƴɽĊ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'Σӈîӈԑ',

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
                    'window_id': '-ύϼčͿ\x9aљƩӁĴĦʹȘÇǈ҈ƞǠ%ϴͻ˾ńÃԧџҟɬ˙ˊ',
                },
                {
                    'window_id': '҂ϰɠʱͷλƒuƱӞŴ˻ԦЦΗʴПƞCԞϕѲöïѬȑμȰѩŪ',
                },
                {
                    'window_id': 'Kԕ\x94ȄБαӁԠĄĻķǹ³ʿʹĖÝǍcˬʶȌoӀԓ\u03a2ĦƺQϗ',
                },
                {
                    'window_id': 'ƞǏ\x9eľĩîÌĥЎȓ¾ѐǢ4ǆÓһĚͲі\x81ΠǑЏӀ\u0381ԝ\x80ҮТ',
                },
                {
                    'window_id': 'ƄλɺϞ\u0380˪ɯшͼƠԎΖϲɣZƽлźɕ\x81ɧȔőŚІ&Δg\x90ɛ',
                },
                {
                    'window_id': 'ЀӸ˳śõuҍŧˆФ&ɕΖңϓa»ѰöĤѸæԄ\x93ƩΖˇSŧύ',
                },
                {
                    'window_id': 'EɻɺÌҗŏȢӋυԊ»Ӗͼ8/Ϫ+ʲѯтɢÓϰ\x86ѬϋAŅΈ˘',
                },
                {
                    'window_id': 'ѷԤ<ÁϮԣŷȿ˃ȾԙЃǊfƈћʐɿҡʼǴƆƳƙĬЃвӂϨф',
                },
                {
                    'window_id': 'Їtȡ½0οǩģѕǉzҗʒɱх=ǚʊκaёXċӃʳʌʃϷÜĕ',
                },
                {
                    'window_id': 'ѪūʮŽұJζ˶Ҍ\u0380ӶʀȮц]рmӝķϹǋΦԅ\x8f\x93ʦЗΕЭÓ',
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
                'Ǽƣ˷>Q\x9aǺ˲˼ȟеǳΆʨƥȭJȱӏȧ¤oˡӜͽǐХƂƓҳ',
                'ӃԦΐÇїɇ\x85ωĻĘҰǔѯƌȔҊŭҶƋ\xadԐɁʱϤЏЯɬӵȉΕ',
                'ː`ˍѾƸБŲƝ3ɷŪ\u0381īɵˋǁҠŐӏɦGmėƭӘѺ¬țȎɚ',
                'ӱкўȻɌɂʂůԛĭeѥˀĳƠZҥǓŧʉŜâȸƯϝʜ\x91ԦʯϢ',
                'ϧɞʗу҉Ԁ˝ȿЅúƚЁȣѰӊˌ˦ӯ\x80Ӵ2\x97ҭʏŒɧЎĺɼϏ',
                'ĖϐΗυҪĞȌǲҘɞѺȾȯɢĨȽlϛɆ\x85ćћĉʸϛҁɛɛΤљ',
                '˝ĺǂ˟Ϛȿ\x86ǐhώΚ;ӑӅ\u0381ѶγɨǦˊԩӹĕĠăμƍӟϝķ',
                '¥ʹѫğʲĶΕҺϣƿА>ȍϽǧ>ѿɼɮǴъζˍɒӹˢΏғȫ5',
                'θΚȊțĊρФɾʫŹ˺ȸžΧɮºzĘΠœ¨ʏƳʬˬϿſвÂ҉',
                'ӘӍЎ¥áϹЂǨ҅ɠƢSɮ%˹+ĎҏɏɅЍĴ~ƚ϶ŅҰЊȥð',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'ԫǅӠŲϓ',
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
                'focus': 2182,
                'parent_id': 'ȮƈӃƜ\u0379˞ȾԐȡƐϯϒț+ҦϠĉϜǚˋĠɢБʁѥǠǔϟЅȠ',
                'location': {
                    'x': -8730926852143615769,
                    'y': 8105938414961940121,
                    'width': -887943851044360826,
                    'height': -1788174191729485066,
                },
                'minimized': False,
                'meta': [
                    {
                            'key': 'ϮɟѼȶƅδӈӑɔÂҤ_άȍ<ɆºΙˑŚѬȗќ˂Ϳ@˦Ԏʱʇ',
                            'description': 'ǣӮƀΐʾͱҼ˾ѲǣОȚćӨӬɊϷÄӡ\x8fϖș˷ԣѲϴψƊКΧ',
                            'value': 'мЁĕa\u0378ҶƈѢˁēԁӍԟ˧ɡΟϰЕʺǭɴƽЊɶǡρƫãȒ˴',
                        },
                    {
                            'key': '\x9dʟʠӦԭϜԎǍѹҪΩǋɕƸ˔\x90Ԑȯ',
                            'description': 'ďйĀɞʸǳа³ĢŀãϮʈ¹Ǐ˦VXñǈүƭɕɅɑʟϊǻȂ¥',
                            'value': 'σʞŊ\u0378ƏОɒšĎҹȌƦ˪ҳͳÐĳӵԎԤӇΉώeӽȑԈІŒŽ',
                        },
                    {
                            'key': 'ϗёŪĜVɸşɀѴ(&ǣ×ʉҹԕʺΫӕȯ`яЛΰѐ˴ÑϠ;ȷ',
                            'description': 'ʂȆŬʣĽҰ@ѧҷҚΤȀͶɌƥĂҮЗ±˔¬ſǼÊϟѬлɍ\x93ș',
                            'value': 'υ\u038bʟΉʝ\x83åȔΑԋ\u0383~ӦΜԆțƥ\x92ͳϴŚ´b\u0380ƥ\x92ƷȽȊϔ',
                        },
                    {
                            'key': '}цҥȱѲź÷е˽îşx˛ӐŕųƫċԗɇIůƩΪЋҳҐĥҾȝ',
                            'description': 'ëɚо҈˙Ś¿ěӥӥ¿ÁɦĝҢɠþ˄ȕ?\x91ˏɿ+ѿͳȖǐŉԎ',
                            'value': 'y,Ō\x80ӒÊɏǹԛ˾Ԥ˻ъϊѡћʘ\x94š7ǺӰƋΓԧȉCґȕÆ',
                        },
                    {
                            'key': '˔Ԉɣ˹ujѫƋǚӃǙ·úέ®νũ4Əĵήϑˌԝ΄΄ˋçY',
                            'description': '\x91ьϲÄU¢ѩȑǏ]ϸԇĝӍγƩǅЬǙκͰ4ɐԬÉ˅Ď˚ϵΫ',
                            'value': 'țǛėʳĆɏԘĤˮӖΦĭŞͷ˳ǮϴȜűΆЁѾπʖңǚǞҝΰ˶',
                        },
                    {
                            'key': 'ϧбЅԙѤǛ\u0383ŬΉĞʢȄƤŊʬζҠЉǊьӡĝźˑŻҥщ˂ҳʼ',
                            'description': 'ċΧȨ˸ƼԫѓҚˆ˰ćύѦǈĝŌҰҥǤǮΦÛʿE˩ǟūкƶϬ',
                            'value': '˹ΰӮɻͱԪˍʾʆѯԋΘщĢɴǄ\x80ĨʵɹдǸ˭HʫÁѕѹҾʳ',
                        },
                    {
                            'key': 'ϵıƓƋ',
                            'description': 'ѸɦΈƴϯκеѝʮʁѧ˳.ǎHϙҐԁ©\x99Ҝ\u0380ӔƼ¸ĥɓĦĺk',
                            'value': 'ԔʆϒΚǕɺ˂ȼʻÕȕĠҦȫΟӃĉúɽǗȂɏϪƯˡ<Ñyбϣ',
                        },
                    {
                            'key': 'ǒ³҅ЯгʄȪ҆ӏŎÁҏǵĸɺ˼ʳåԥņ\x90γ\u038d\u0378',
                            'description': 'ŒƐʩԥҦͿĒ\x8eÛӝϩєùƹíԧȻӃӚʀǬΌΚɌϴƕŝͳ°ҍ',
                            'value': 'ҿӷԏйiŽ;ЖǐʁЀɔѱƹÛ\x98ǈ!Ѥʞ҅Ҁҡ˃έШÈƛbǧ',
                        },
                    {
                            'key': 'ҺĤǳŴЏF¶ʐƢšхКϖʬѴ´ƬǦĮԃДe>А˂ӵѦƵ\x8dù',
                            'description': 'ˑ&¨СƽĞǠΝȥǀƛʲȸaϹʔ\x88ėͺȈXƴ˜ŭҪítũƲT',
                            'value': 'śн˱ǄξџůɇƎȂǲΚ˚ǲλϵƁ΅ɻȗtαѐӪ˵ŮÍϩĥʡ',
                        },
                    {
                            'key': 'ӂϙ;ũôɕĄ˜lėϜƔǝ˦ĒҮ!ɻle4ʡ·ϽtΞ\xadÊȩǑ',
                            'description': 'ĐƬǽ`ԇȦӈȷԦďʺHʣ~ÄĐʓˈǏбƹЀєϒЮȳɩɊƍП',
                            'value': 'ΡȣԒҽҭƀț!,éɅLΟæīй˞ğуɮþȳʦҵȬҸ\x92',
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
                'focus': 3077,
                'location': {
                    'x': -7493573487976040958,
                    'y': -2892683850620010385,
                    'width': -3648533214705403015,
                    'height': 2815323595712024061,
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
                    'key': "ӧȭ\x96YќwɐThȲѱ·ºɓ'!\x94ƶŦЁΞϳŤ",
                    'description': 'ъ\x8f\x88Ėũξ¡\u0383Ǣ0ŦͰǅǀϗʚҬȀǉáюӆҽгýǼʿΫʴǕ',
                    'value': 'чȩԭxӣāϹҝŦpѯЃəȁӚÉεbΏϻԟ\x81ӈčŷÆŤРҡÙ',
                },
                {
                    'key': 'ȶϡӶҿĺ˶ϘːɪƃƺЦϤϨ*ȖȴĄҝԚōˋҫΈŇˆȯƕŃт',
                    'description': 'ÇɗǱơƞʜȣԎOĝ҅ŚØǺщУҏŦ\x9cȰǜƃгʏǺĮ˷ĩμ*',
                    'value': 'ѸӈǎɨҙʻƜϛńЕΘˡʥЭȷŧȫЈĮƤȋ΅6Ȇ(ĤƜόȣϳ',
                },
                {
                    'key': 'ƾƿҏѼ˫ЩƁǤǩʛƸФǩ',
                    'description': 'Ɉ8ɅɯRĺөpĬԨǦuʷɲɢ\x82ʙТǳҰíӲTʾƌѰ>ȮķѰ',
                    'value': '¬«ЀъѥϥĮ±ǧŷΟȎϡƿƦƫˤȵǡÑŐĜȩƴA!ғһӱө',
                },
                {
                    'key': 'ҽΟǢ\x8bфӢ\u0381ǩȺːϡ%þпΝĿȉЉϪϚ',
                    'description': 'ÔlвȟĞƷƂ\u0381Ǘˮɥџѐ˸ˑǂ$ǪTȌԕάԥ\x92˾ˤǿĮӏŬ',
                    'value': 'ƷΓԁӸΛŰś\x84ѪŉˀõɖɬȒүȗѼԝ\x86ύԮƠʧĨɄȭ\x9dΩŢ',
                },
                {
                    'key': 'ˤìӇǊBΛUǊſ5',
                    'description': 'ĺʒεЕϐн˰ƄʸµÔ"ĢСȮԢ\x9aӐóфɋΈͶыЮιԅǬʢƵ',
                    'value': 'DҌŪʊƦĲ@Ͻǂʼ.ʆԌ=ɱƝĩϚРá1˪ıǿʮǐоģOŪ',
                },
                {
                    'key': 'ŀ\xad\x9cӁʇȼțɭїʋ˔ѮǃʣѐԬϘŋĄåXȅƖƍ҇ƘѬɩî\x99',
                    'description': '˸ԑəŢuɶÁƐцϮʢ˶[\x7fƻκºПȮԇ\x870ЛîԄ9Ԇё\x80ʒ',
                    'value': ':\x9eұFӅǸËЉȤʝԭ9ˮ/Úғť1ρŲϭźȼǱ;ҩҁͿõЎ',
                },
                {
                    'key': 'ĠƎ9ȅΐƦӲ\x99ϛǜЦԣΘ',
                    'description': 'f˧Ǎ\u0383ӯψƽƅΩŐqϖ4eĤɼˈЛԓɏǳωľǶʍЀэδ\x99ʺ',
                    'value': 'ʳȎȘȸŁ_ȭǆưԫȑԊ\u0381Ћј\x97йҋЍʶȠӝκϘ\xad#ѥʯɹҜ',
                },
                {
                    'key': 'ˈôϲȉυ',
                    'description': 'ʨʗɢȳˬҲѷĤȷ°ΆͶЉѺɖԔӨ\x7fƘΓνҞīсΞÈбƲίС',
                    'value': 'ĸҧ˵ːȻӜӏӆƸτӦĖҬ×Íɒ@ԛʜˇäƱȔțд¤ԧʘǹƶ',
                },
                {
                    'key': 'εE\x86ƾ\x88ȺǈȢӫϹԓ',
                    'description': 'Ϻ÷þ҉ǆĢûӺˣƻ,ӟ¬ǝКѮºJ³\x94ƲϪǝ\x92ŋѷӅӠàƹ',
                    'value': 'ɪœŜѧƟɋɤӊǢƛ˸áŶГɲĿûϥĬͲѪёΪ˭U\x8cǔAʓԭ',
                },
                {
                    'key': 'ʢǏǐ΄ºɲ\x86çĩԄƶûɀӉλɍĴm;ЙɯɖӘÇοƮ',
                    'description': 'ĕΑ8ŸϏЎԫ¢ŞæӯǽƱӌЊɰŻѵЯԝ°¦ĵǙʴӁҙ-ʋ\x88',
                    'value': 'ć˂Ӯ˙vɿ˹ŞμʼΘǫû˞ŸԞӅ˰ΊмΘΗƕèόϻӿҒҰѵ',
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
