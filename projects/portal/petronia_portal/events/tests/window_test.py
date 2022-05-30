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
            'x': -7474366024281945625,
            'y': 4203808678249236881,
            'width': 6250275484760992589,
            'height': -5237059543769025040,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': 5190648585265526610,

            'y': 2069692455640427113,

            'width': 5067531503808791075,

            'height': -5108142077110013899,

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
            'key': 'ԠǏӌO\x83ЩºԄȃԡʣ¡ʰ\u0383ƖɈђәС˪ϵȓΫөѧǥӻъχ',
            'description': 'Ĵ+hĚȇнԒӆÌϮʲϖͺ˖ҪѡԆҸҵvÆ҇ȬχҒŁŷφǟș',
            'value': 'іȌϝϷƕԥȕȭˑĿàКæпϩēƖϜӬʲȴҗɷҫΓǬĕŅїҟ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ȗ',

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
            'active': False,
            'focus': 4322,
            'parent_id': 'ϳҘрҦζÿŦ}ľŗЯĝѴӲ6ϰſƸ˜ŞˍϏǬǌǐċΌɥӏə',
            'location': {
                'x': 3617147995635421403,
                'y': 5087591218433278907,
                'width': 4470505164494386155,
                'height': 2248968551564610999,
            },
            'minimized': True,
            'resizable': True,
            'full_screen': True,
            'meta': [
                {
                    'key': '˷Vń}Ǿ@ǔԋǒƬPΚҀӘӓħ˄ŧΕқҒԡ\x8fß˚ȅ˵ЭѦκ',
                    'description': 'ėӜфԎІĳȔѲ˺ȹΑ\x8fȝΜƴЅĮѭЭǻρϤҚɐм˲JǷѹĘ',
                    'value': 'ϥӈΐ\x87ÌӈΧ\x96\xadźȜЉҔϩǮí\x89сϢʇгʦЉѼИˌ³Ӣёƣ',
                },
                {
                    'key': 'ԉɧͰʫӥΒɉĭ˴Б',
                    'description': 'šǢЧƹtљȌ/фΗġóɞ҄ψɲҼԮτӣÇƖйźƇҥˊѤɞΞ',
                    'value': 'ĥӂ}[ұ\x9eĕҢļѼáɂˬѬśOčҊǺǈіγŷΐε҃˓ƁѰǅ',
                },
                {
                    'key': 'ψǄˬԬӘ˲ɯͱʡГ1;òǝ/єȀ',
                    'description': 'ƇҳɐF\x92ӊÂŒ\x9eĥȹϲɛ˕мíЅ˚ћª:ӢǇ0ţІΒȐÉŪ',
                    'value': '҄жĸĥʽρҙ=ɯΥԉԓһ%ǲ<ҋξҝɈĔчҫȱ',
                },
                {
                    'key': 'zҋӻҊˡ',
                    'description': 'ԊȦ5ѸϢѳ˵ˁІώƊѽҼªɍҴɳδŰÞźğõӡļ\\ғΈȨУ',
                    'value': 'ѷЇɢЩƈιßЀӭǤЃґ˩˰ԩŒҹFÉҀ¼ĔȣΨÆԋɇÂŶԋ',
                },
                {
                    'key': 'Ӳː\u0380ĕǊɫ¹fȕ¸Β5ЗƆYϓĉΐѻ¤Μ',
                    'description': 'ϠĳҭŊұȵѭɛԙȳ˚ƦѱӝΠҙˠϥˣ¸ϊԟŊčԐɉ\x9dȩď\x9a',
                    'value': 'Ϊ9ʈӨɺƃ˽ϭӭłǛӸӃς\x86ƾȕљǪϛïǘ˷\x95ɊİУbȬM',
                },
                {
                    'key': 'ŧɪȸ¡Ʒϰ˦˘ǷʆкёɺɮάҽûͷĢјnŒ\x9aÙɎʆËˌŮ3',
                    'description': 'ȞҤ·ӏ²bɽ\x96ú҂ķÏϑȮΧфǁǡ\x89ùϿ%ǅӰȴÈZѷɎǋ',
                    'value': 'ԍɹΉŅÂʹ_VӪȖˌЫ\u038d\x9dƀƳ˶Ô¯Ӹκ˨uǙƷгѽǣҗѽ',
                },
                {
                    'key': '\x86_Ƚǈ3ł¸§|ʲҀʹ\x9cӧkÆӒѱŞP˧ɯҷҰΊΦƃΏ˽ş',
                    'description': 'őĬˤǈЇɏǷҨҭR˃ØűОZӁȁ\x83ˁʣӓ҉ʆȧɧӹƔ˜ыԊ',
                    'value': 'ķ϶ϷbѯȋʑȷәұŌiǫwОŏʃȏÀʙӠяѧēӪşÈвǑ¨',
                },
                {
                    'key': 'џĝƙԌΰƾʜĺѯӁЊɺȝӭĭ',
                    'description': 'дΧˇӚʭҶțΛʱĴџɘūɂñǒϸGϨϜѢǈ¼ЛԙϫʪʪΠ\x90',
                    'value': '\u0378ǖІђѺόŻψʷʤŁȓʶwӜÕˣȜԢԄȄѽ҃ɠқȳǷ˙Œ˲',
                },
                {
                    'key': 'đӿӐbΓ±giɕ҈ɝԍ>ϙ',
                    'description': 'ǖǣїˆ8Џ҉ѬӠȽνЕƄʀ\x9bԕ\x9eˎқĩɭԟƢǹӲԂѩϙĮɘ',
                    'value': 'КǝhҞɍǰҏѵ҅ɒлɯѭŨȮȟ5ĘǷśƱĵӆчªҼЧĸĎӇ',
                },
                {
                    'key': 'ˇҢƱýΜ',
                    'description': '\x95҃ΰηȲɾ¥ɇ\x95Чºã:\x89ʊǜАëΚԈǦӁTԆ;ӃěWĶЊ',
                    'value': 'ɷ˴&ŕԠʆ³ĜŬϼУ\x8fѢұUҀӫʐΣíɣȟώϗйћθʯʎǒ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': False,

            'focus': 3052,

            'location': {
                'x': 7630572892323903581,
                'y': -2950231569586171007,
                'width': -3831646667882011166,
                'height': -2057776435526089898,
            },

            'minimized': True,

            'resizable': False,

            'full_screen': True,

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
                'focus': 28,
                'parent_id': '\x83ƭ¯¸Ȕ¶Е3ѫšѝ&ÌЙϲ\x9e\x9dΥªβΆѭҫǪХҷƨ˜ĒН',
                'location': {
                    'x': -7499722791252748087,
                    'y': 5357403414504578243,
                    'width': 8140435829592440980,
                    'height': -2749692156225727535,
                },
                'minimized': False,
                'resizable': False,
                'full_screen': False,
                'meta': [
                    {
                            'key': 'ԏ¥\xa0ӱAӐϞÙȸӂѝΠяżЗhԐϔЊѳҵҷÏԫϔ˺İ',
                            'description': 'AÄҶʁǃțƲӻȀ2ëīˋbҪĺʢqƠƔ*мɮ˕ʹсϕϐţμ',
                            'value': 'ӷӧǈΛƭЙ9ϡŽ˵ѤӱӴϵЊŮǾӶʬɡµőLȣǪϼїȈǎʊ',
                        },
                    {
                            'key': 'ȌѪș',
                            'description': '҇νˀǒΈųè˻оĮƨʈʖϲĢɱԮƏđ˥ΎӾӫȨΔ˓ӛΔӜ#',
                            'value': 'ΖʏĆѬƫÓǀɵɕѕҎOSƶԮïŝʄqҕÝƜΗƸԉǅїӈ϶ā',
                        },
                    {
                            'key': 'ӠԗąʜӦԠǔҟ',
                            'description': 'wÂλϔӝԛЏԇϟϚǮΩǂʼҖʽԔƀ˙ͺѽғpϼ˚ʜ˨ĆÇɓ',
                            'value': '\x81Ιòʒԑƽ|£ĘȋԁϢԦϩȇ?ӴότɓźӢĒ\x82ҮдҐŵŭʿ',
                        },
                    {
                            'key': 'ʾϏӊԆɱ·гįӔʘŔǔӑΧˀņѫӛþз',
                            'description': 'ѪξыȝΏζȏ˽ԔåҞϭЄĨFŵĬҹ˙ʟgόϯǾʹЦ˩|ño',
                            'value': 'ϜƆȄϓç¹ˇƋƤȒǸǂɳȖǾʖÜ˔Ӱɒ\\ʧǊįȲϜ¬ǁЊä',
                        },
                    {
                            'key': 'ԘȋɚӹԚƟʲ\x9eǔпѧШǼëʼȢЦġŚ¶å}!Ȓ҈ҷα˲˛ԍ',
                            'description': 'ʟҊΜIˠșǡɋЛʦɯȥѺѷɐQҘǙ$ѿҭҜʇǒѭɄΓѩ"\x8b',
                            'value': 'ŃɢƆzǓ/Ӭȸ/ƘƴжěÐΰѵśɹЃ°ƃγ˫˻˕ȖҔđѴĊ',
                        },
                    {
                            'key': '˒ʽòѪM\x8aˣԔșǃ\x9aǿ¢ȴ',
                            'description': 'тǿzįȾƨćЍ˥ɉƭԖδĚŗgĀȄǾƸϛƥҭϲǮΔ½Ͽƾʞ',
                            'value': 'ñȹΌʟєԚ\u03a2Ņť-҆īѯōΧʐАPSeNʦР:ӝџƲĘʌР',
                        },
                    {
                            'key': 'Ԡċ\x89ſТʉΙȌƚƐů²άά˦ūϨЭǣ:ƎŸϪϘJʗ',
                            'description': 'ɦɣԠƮѿūbǾӹΠҝÕԍДeЙÈәЛęǉă҅ɽӦѩΰŁфǠ',
                            'value': 'ŰßЉӟȻȌˣņˋƁʉ£ϦçСůȧʎѱēȿԍǺĊϳČïӑ\x89ɧ',
                        },
                    {
                            'key': 'ͼ6εɶvђ«ǡƣUәԔҠƧòӱ7ҬИ7øǐͳŉǑҷЯПǧǣ',
                            'description': 'ГЛ\x9eƒӍΈšӕ\x8e΅Ğ\x92ƝƙĵǋӢӀ˞§ɀfȷ\u038bӎɁ\x95ǄҥϠ',
                            'value': 'ėϔҚԡƮƉƲҢǀі\u0383ÝǹԄŹǶҹӿЛȗĄƼɗρѓʳPęϛ˪',
                        },
                    {
                            'key': 'жӛͰԨʒВȣƦʿϹȵΏѬƜԔȮɗÁѩ\u038bÏ\u0379~\u0379ȅѓĬʢǦϼ',
                            'description': '9ŠϓɆөҊ\x93ȓџʠţѷҖČȼԏҘ҅¾ÉȏЖŪʲџÐưĤ\x8b4',
                            'value': 'ӥʙǵØȂɿέĀћ˵φϧƃ¡ǲϾʶЭѩ°Ī²Εȍ´ӍхԚiǣ',
                        },
                    {
                            'key': 'ӤĵǶʆËȎҐʜԇԁѱ',
                            'description': '\x9cų2ńȷȼ҇ǖ|ѼԈå\xadяɠĩɧСƚ˩К҇ċ]ŒϪWжīГ',
                            'value': 'ҵѵȡŮƢʳSqӴШƈʂҤӣҳ\x82ƾȜϰɀЛ˼ʚȉdѹѺʹҾζ',
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
                'focus': 7333,
                'location': {
                    'x': -3490737555823855970,
                    'y': 5843574795106243341,
                    'width': -5341516688515512692,
                    'height': 7725911778555063338,
                },
                'minimized': False,
                'resizable': True,
                'full_screen': False,
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
            'reason': 'ǋɽɆɞʇLԚˏĒĦӖŨƘȪғӸąɏϩˮɔƄƗанϞɮË6Γ',
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
            'keyboard_focus': 5286,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keyboard_focus': 851,

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
            'window_id': 'ΜΗƕϼʼ\u0381Ą×їʢaƒȹ',
            'location': {
                'x': 4610229632996571898,
                'y': -5094194555852571604,
                'width': -6898095739042112934,
                'height': -4163706961927194606,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': '˹ȅ-ʧw',

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
                    'window_id': 'ʝġ˒ťÈƥ¾ΓƺԒ¯΄ГԘδȟԔʡɦ*ѕ\u0383ǯʊƅlǽͼӈɵ',
                    'location': {
                            'x': -149323886724454367,
                            'y': -1636804416104970452,
                            'width': -368581247519204995,
                            'height': 1562994265645982864,
                        },
                },
                {
                    'window_id': '˭ǒƟѷàɒʺ˩ʤӃӫb0җΤǷ9ӂӢü¡ықĀԬɆØÅРВ',
                    'location': {
                            'x': 4703436963032240901,
                            'y': -5145371170539377870,
                            'width': 4004314247421263246,
                            'height': 6597639299622649333,
                        },
                },
                {
                    'window_id': 'ԏίҧԟȸ½7Ͷ~ɉĜuи҇ȑӘŘζџƤQɨѩԆɥ˚ʥўŦÝ',
                    'location': {
                            'x': 6538967836180832157,
                            'y': -3755380879692645231,
                            'width': 8691296847834568573,
                            'height': 2617360262916470868,
                        },
                },
                {
                    'window_id': 'ÕƸƗƾÚҴˁƻЗҌļǂƘқŪŻƮ\x8cƽõӫӫɏћæҽӎӟӜǱ',
                    'location': {
                            'x': -5152425635320441257,
                            'y': 6326693894895598648,
                            'width': 236348416768631568,
                            'height': -7901843463053230371,
                        },
                },
                {
                    'window_id': 'ђCԑȀ?ЩӜірÅϲɒ\u0379ɑɺ\u0383čˠφȪҁζ\x87iБſɤːɀи',
                    'location': {
                            'x': -2928337092905929279,
                            'y': 5491416720310372283,
                            'width': 7845021226404865322,
                            'height': -4022336082695794002,
                        },
                },
                {
                    'window_id': 'ԔǲǕѮӘǃťŗӂҁЗҁҺҿMӭӵȂ<ԭȲ+¶Ì˨ǽʟӹŠ´',
                    'location': {
                            'x': -5370009764902575262,
                            'y': -6196977559116555693,
                            'width': -2871469757054953018,
                            'height': -9070885746186105309,
                        },
                },
                {
                    'window_id': 'ÕɩØʇʕ˜ʷ\x81ѷйϨˌώęӻϠWư\x96бŧϡӖυƘѻϝŬȪȬ',
                    'location': {
                            'x': -6637571690856499725,
                            'y': 4583598444874735472,
                            'width': -3203041803544126009,
                            'height': 9137405361835192784,
                        },
                },
                {
                    'window_id': 'ѹѪ/\x95kǧ˘ƏŔφ°ĂɕЙȿ4ȢШϗĎʢΕІ˵ȀȢҘаӯҮ',
                    'location': {
                            'x': -115066750136222506,
                            'y': -8813655063046612016,
                            'width': -7762754053676151014,
                            'height': -6170123910316758064,
                        },
                },
                {
                    'window_id': 'ӞƣжɎȏĝņLʵǖĎȡÜƅ»\x97ҍїƣԟáӵԄȗăƊѮ˱ɖ˒',
                    'location': {
                            'x': -4443458105918814951,
                            'y': 9058635120098214148,
                            'width': -819207000094355182,
                            'height': 7287695722185418900,
                        },
                },
                {
                    'window_id': 'ǆEԑЁĜҋϿeʣϻˌԙҺĺ҅Ȇ϶ѠpĊӽŬТȈԅƞБ\u03a2\x9dʅ',
                    'location': {
                            'x': -9128631496105899,
                            'y': 4489360053859759617,
                            'width': 63517294140251271,
                            'height': -665987295536191057,
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
                    'window_id': 'ϨʊǄdɜ',
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
                    'key': 'ҋѝцȜԩǓȫӍǛΪť\x94ƌ҅ƃŴBȟaσδŮfҨƢʓӁΕЈȸ',
                    'description': 'ѴŴœǻãɾЦÎκ˻α±ϊѠЕΑƴ˗ӑӤɕӮɅÈȸщ\u038dЗĆĮ',
                    'value': 'чƃƃϩβӂЕȖʚƳɛ҉\x81цѽ˝ĬңǹӼӅΦӹԫɷƩ*ѐ˃Ɍ',
                },
                {
                    'key': 'ʲć\x9e',
                    'description': '˦ɶʴn˱Ҕ\x91ɐ˙Ҭȴ\x85Ź\u0381´ˋȳçҎɣЮЎÂӵӿƷΏǉgі',
                    'value': 'Ăԓ¤\x81τґϮзƠϠέĲтXԦˎƖƝАҺʭaŷΔȧȟǍ[Źϱ',
                },
                {
                    'key': 'οѝԍϷйȝЍɆЍБʚʏвфϡ\x8dæơʇʹ',
                    'description': 'ɣƲϱћƘ&ƅ=ˈ϶ĒњƓq;ѲȉĤΦѡɕðθǩϸϭѝLԧĔ',
                    'value': "ˆűӦ\x94͵˯ӝı¼ɂΰ'ȐԖʰӯģдԉАǪLΰ¡\u038bŐЁӀʀÎ",
                },
                {
                    'key': 'ř»ӳùҮďԋșʳŝѭǧaƿȤ\x8fΞìƎԙƛȾАӇʙǦуŦĄЕ',
                    'description': 'ñ\x8f҇\x82ɻ\x7fâˏӔûϴѧУɳ ΔϡųӈIȢƔʐɏʥˮӠdԡ҃',
                    'value': 'ˍλҞɭПƌŝЕ7\u0383ǹҌƻӴřǯӮҐґάŔLΏЗː\x82Ƕû$\x83',
                },
                {
                    'key': 'юʨʮƉʞƾȹ˂ѸъÜ˝ʂΝɘҞĽȳϋţҦƁϣƻƨĥҊúǦļ',
                    'description': '˺є¯ĦƛϲφҥеǤψȕόűϯťЩҵDԙĭȩϝӢŀ\x87ИъͲ˟',
                    'value': 'Яȼ҄ȻǴЉӣρ',
                },
                {
                    'key': 'ÐŖѮӔĦҤΎˇлîɨȀ',
                    'description': '¦ĲĈϊ°ćȩªѝãIȝǤùԬӤӴǘȉǸZҍώƳдƁѺĐԟȔ',
                    'value': 'œԣԞƨ˾ȈȆúϥϔΤϷĬΖãе',
                },
                {
                    'key': '˼ɄĳˈŬĥҼʱ\x90ŤΤƃʗȹ϶ҀīӇԓΤӾƎοϖӏӟāɩųh',
                    'description': 'əϠ\u0378ĨSϨԕšĔξkɫѼΩɛɆƛԪǁˢ\x96\u038bǟ˯Ē`ƚɜ\x9fĢ',
                    'value': 'YΌ˪ΙЏƻˌҼʑӭӛƋϙԘЖɆʌ\u0378ÎԩѣҰ\x98ǥеӟƽѣ\x8cĉ',
                },
                {
                    'key': 'ɤԮˊËȼп¨ʡΰÏʟϳϝȽΥȀγɈ\x9dȞϋɂԅÜГʋǪ',
                    'description': 'òΟ¬˟ǗɘϮРˆsɑӊƵ\x8aq҆ԋѰĿϙƭӜɴŐΘ˫ʄΙȡʽ',
                    'value': 'ɶąǧɌΠҙɮЕӿ˒ɳ˚ňǹӅӪoыÕæмĤϥxΤΈ`žΈТ',
                },
                {
                    'key': 'Ҝ',
                    'description': 'şƨӑʎɽϰѷ#ϮƮ\xa0ɲ\x88Ȝа\u0383ҏΨÚ˰òƥƬM÷Ŏ˭ϒЯӀ',
                    'value': 'РzеΦΛAǿŧ˄ˉÆˈ\x9bҘҺӛҾÃŁŦўgӦ҆ύϡԉĽ҅ǚ',
                },
                {
                    'key': 'ƽʚĹŶӳɽĸΉƩɲӽ',
                    'description': 'ӽďĥŕȯԍƦơΊčцǀҦǂ2»ҬҏϛȘʽƲĈOϋϝЙņʮY',
                    'value': 'ɏ¿ɟlŚǮȀˏŃӧpʠЌӛĉɨр0Ƞ<·fԫҭ£ҤҮǟČʍ',
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
            'focus': 6503,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focus': 8965,

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
                    'key': 'ŝӯӲЕĝŉǐȶїSϬ҇ӈЄʚΦ\x7fΠɕāè˷ʼҊэнǱŠЅɻ',
                    'description': 'ǏԧĀӐŷŏƼɴƨцĻҢӠƢĹȤВȤҺӲԘιБȚȢ΄ωβ˹Ȩ',
                    'value': 'ˊĮʴ\x93ƀԔм˝ǜΘĊΨĞӉλҔÇθГËEƆ҆ўŨέɹїǘФ',
                },
                {
                    'key': 'ĞϫǞűҸгÄ³ÕģȊʤʇʴͷҢBǢӬƂӥД\x82Ƈє˄öФ°û',
                    'description': "'Ģʅ«ʣԖϫµͷӡХΩƼƧc\u03a2î\x84\x94ɲzҹәҕƒɚˍɚưы",
                    'value': 'ҁƂșűùȫˤŜđі\x84¹ʆΫµ\x86Ӓγҥ¬ҕ¼ɾE¹ƭγϓñƋ',
                },
                {
                    'key': "еţȡʏԑԮӻӭĩӇWԙťτǎƄӿľ'ÒБӡ˕ȄɾƘHțȌǇ",
                    'description': 'ɟћ!УѻÆ҄ɆǊюēɋ\u0379Ûп\x87µʆƵ8ɶƻơƺ"xЁԇɂc',
                    'value': '\x87ɍКƯҦЈťΛϣɉьƟέр˵ͳŧɇԚԠ҉ӥš\u0380ĦɲDͻ]í',
                },
                {
                    'key': 'д',
                    'description': '˴ҢȡǪĠҐǗƀ҆ǚɬŰǁɩщιҫǍ\x88ʥѫоːӃϲȝɿʧԃȢ',
                    'value': 'ɡ@жҺӒҊėǩӻӀūˊǩőƃѼӝЈ˲ΦǓВŝŊͱΌɠύb(',
                },
                {
                    'key': 'ÐҜŲΣɞɉ˵őПôŇˑЍđßҦ&ҹɼáΌɴкƭϲɋ΅',
                    'description': 'җοʑˀɐϑbЬ\x86Ĳ˪Ϣҳ˞ƫƫǕӸǏÄÎќǐӦ΅ΕʘgԂǡ',
                    'value': 'кҔЁˁʠμǉ\xa0ӡƃǉǆʱ˽ҪƒήЊ\xa0ҼƀƙȎļȼ',
                },
                {
                    'key': 'ЀƂʣʰĥǄњеψΰ!Ȟǿʻ¬҄ϰġĉ5Ŧ҇?ǼΨҋөӢ©',
                    'description': '˄ДϞʥū¸â˴ԘčɲȖӠ҉ƒҨė¸ɥІŋʘѯ7ȻīȁԓŽɆ',
                    'value': 'ŌѸԐŌˌжőκЬҜŧy)ǽ\x9aӾĵƁÀɰʔӹȊțɰ}ʃ˓˚φ',
                },
                {
                    'key': 'ʨϢτұüˮҢČtԑΪΘϴ\x94~',
                    'description': '˄˧ƴÂÜĎˡŉɚıÑ`˸ңҔƊΚˣЀW<^ԡȭҫĖWЈԬԍ',
                    'value': 'ǑΟб\x83ϐÝ\x97ԞГԑϗƐźʉáЈşѳԐ²ΎȶŪӦǵíΥ͵ђď',
                },
                {
                    'key': 'ψ',
                    'description': 'ΧƃɻĕӑӒϫ˟zǓǎѥȴì҆ҏӐ\x84\x82\x9aʝ\\ѧʴԑ½΄ɍɱ|',
                    'value': 'ɗŏɅ˚ƱKϧЭĥȆǛǡǭԉ°ӼĔ˄ǒаdтɸˍȶ˖чǋķƑ',
                },
                {
                    'key': 'ËɅ+ҌΤǶęǘĀνʴЇ\u0381ͻϲQÕȫɶΗɡǒӻƨ±ԖĚ˭ɑС',
                    'description': 'ǆèЪІĹɒĵϣȅϋǦнӈЊɸƇԅȢΤȐΚӫǺŞɜ\u0380Ťʓê˳',
                    'value': '½¡Ȝɸκ8\x8cԛӌɓǽƴǟθĐMǜλ\x86ĈȑĔňѬϸ˔ʿаʓƑ',
                },
                {
                    'key': 'ҍɡ¬ЎҏҔPºΡ\\ĉ¯³ʜ\x85zȖƦňǅşӷá\x97˔b\x86+ďʱ',
                    'description': 'ÇԓǁIƇǵȍ\x86мæӂñҒƳďӱöHáҟɛƳɪϪ\x82үϹMϦȜ',
                    'value': 'ƨӼ͵КѭȋκȲ+ЅOΔȍMЅɳƃs˨ό6ƧəσюŸζμԢĥ',
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
            'window_id': 'ʁķҪȁͰҰРӚǈЈЌͳŃÔΗʭɸӼђɵǟɓ:ǨϿΨɥŘЄқ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'éȻ/ǐğ',

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
                    'window_id': 'ӐãäÏΦ6MȎΖųѿʡčӨΟ˺ӭѼɰǼĭϷ=ʡЪћˊƓ¬ͼ',
                },
                {
                    'window_id': 'ΖǞ1ӷɈƘǳÐěǅùτīǎēԏԆƉнҼȈжȤĚӡʛ»Ӛαę',
                },
                {
                    'window_id': 'UʪЁΖɉњӻԭțǫѷΧ4ϹҭӸȼΒɚȓĴОйΆˀŹɺˀƤʕ',
                },
                {
                    'window_id': 'ѸӇˋ˔҂ІʊăɶҤƒɞЖөêιĽҍƳЪҟԚ˳ӵɔȪʮ',
                },
                {
                    'window_id': 'ʖа˫Κ\x8c˯ɈʹěӛѤξҔ3Ǘ`з\x7fĚϐʌĥϚϻűɲīҭɠ˔',
                },
                {
                    'window_id': 'ӧŘ˘[НʅѩǙʪԑѻ\u038bыϸєʯΆǻӍʡıӐҩ\x7fBǠ-ƁͼǪ',
                },
                {
                    'window_id': 'lѵʺRЗҾԉƫ,҃ӿќΒĝŃÁӝɸШăӼҊŸӷbϖʭɒӱ6',
                },
                {
                    'window_id': 'ˠ;ǂʒϚαҢǃØªӵƺɹĢĽϩӋƚȴȄЯɢϳǗͺɈͻýҸĘ',
                },
                {
                    'window_id': 'V΄˥ːʲ9ϹĴӨ˅ǴŃÏϕǓɡƨʧŏȎΐÉүӸǓŊ˩˧ȋӈ',
                },
                {
                    'window_id': 'ĸНȿȰ\x88Ǐ\x8bɊʼ˘ɓ-҇ļмÙůӺȨȃʒӜĻȣФηφÈEǳ',
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
                'ɧKѿΕё˃νҢϣϞǰûħƭӄyӗԃѕĺÑǜŵԕÇҘƝƅŃ5',
                'КΛΠαƈԚɾȗԣ҇ΗɫφǒҤ\x95ɂļΐЧъЮɢԠѹˏ²',
                'JΑƤhɮьԓh˵Ŭ£°Å\x89Ƅχѓɶƌ¤ʛHϻ·ОӋŌѩ˾å',
                'Ŕȕ˲ʪ¤ϬʁԏˀӂǙǢȩ\u03a2ȭǯ\x83\u0381ҷ˩θĿƁҎ˶ƮҠȪǫФ',
                'k҇Ϥ7ɯÈӭŁНˊʇƆŘďʊƲgϗʞɨ΄\x89ƿĢΒҠҭѢαǻ',
                'ʍŏЅͷř˻ȺǥuϣǗÔʮǤԎƿԐΕӎԏʏ8\x84ĞҪȥ|Ҙ\x9dŎ',
                '\x839ρΓϹɶ-Ńȗú\x9aƄóŻȯīÒƭ;ӸɵˎƟԊǪѤŏѐċJ',
                'ÙԧUyŹʗөҰɭϳcҔFʂѝԬ҇ɫ˺ɮĒԂɶſȅѸ\x97UΘł',
                'eη˘ɊFԈêΛʘçϺВ˾ɻσɒƢӺ5£ʏĤ¦Ʈŷ\x94\u0378\x8fȓ-',
                'ѹ}őДƿˢӗͼĜ2Ӛ]ȶ¨¹ŘǜѰTέɨαК˘ѯaƶӏӗҔ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'hԞҎųҚ',
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
                'focus': 6519,
                'parent_id': 'юGȣƧŘɁҠҊҸɥžӺſү?ԂϮęԉĴųǶ;ԃƘˑ¸ȨŎƪ',
                'location': {
                    'x': -1472035434194284877,
                    'y': -4346782204060858765,
                    'width': -6733249172978321596,
                    'height': 8488079976223983058,
                },
                'minimized': True,
                'resizable': False,
                'full_screen': True,
                'meta': [
                    {
                            'key': "'ʀŐҩɮӽŎ",
                            'description': 'ЅŁОŲӊƖЈɕq\x93іѻ(à§ȓȯЙǗɺӛλb΄ϹЌǈѵɏǇ',
                            'value': 'ő\x87ŘŪźȧô˝īҐҸƿӒ¢ΐƼϑ\x90«ƙťʓуåʮƌӷ©ɓÌ',
                        },
                    {
                            'key': 'ñ¿ѷēʏƝʫ\x99³І©ɑǓѢУŬµҮƑЧļÞôΑ8',
                            'description': 'ѾЕ\x9dşΜνȞôÄĤ\x9f',
                            'value': 'ΐ±˰ʗӪ\x8fŬƖȚˑƅΦǻˬѣǡȺƅȖɅ˖ǤʃŘŋԐʠʽґʃ',
                        },
                    {
                            'key': 'ʢúȲБŢŚQʠӬǱŜаˊфœѪØ˭Ѿˀǻķ\u0379\x88ҫҩʽɭȂ<',
                            'description': 'uçîʽЋ\u0383ӫσĘȬԇ0ƙ˴ІǻĂˬŪҦҦˆeȲЊʺ°ɮӞɳ',
                            'value': '\u0381Ó˾ӜǍǗǧӤϠҩƠȋΊĭġćĩҡ"eȯИțÅˀӓqˠǲҞ',
                        },
                    {
                            'key': '\x96ӚϳǑ¸ӍǦïʪˇŁ\x8fҚӿdʐƼ',
                            'description': 'ěντ\x9b\x89ĳ§\x85ιĴ˲ӌтJwϨįΟӫɢʉнͿTӊĚɑԂēǣ',
                            'value': '`ӻΔŌЁzͶμþǋŦŘӂ˻ȦЂӝŎǒɮ´ųŃō/ӄς\x88ßʟ',
                        },
                    {
                            'key': 'ȜМͽѦдБΙȽƋƔ\x91Ŀ\x93λͲơҖǄŻeâϜr˹Â,ϮσӍί',
                            'description': 'ɪȯҀɄǤЩʦƃȕϢǙЯσνȧўҔЃҺʣȵȆǮÛˠĠ˴ǜƳĩ',
                            'value': '$6ĬÚԋȱƠСʨ˸JĺӃѾІԦƎÓ\x82ҡӫǋĔȳĩ˔ȀԔϊá',
                        },
                    {
                            'key': 'ӘԐѳƘ>лӝǆі~уҝǺϓǯԮж҆ȺýҦЗ¡*Ҁɷρ\u038bӠҙ',
                            'description': 'ĵ˨Ң<įϴͶȅ}ЊŊɋňѐ=ҪȧӤ˵ȥ˄ʖζμɍˢɹӱǽɜ',
                            'value': 'ʮүӨϞΗӌӷĐф9ӌϧƂʳёŧи\x8dҢʊĲ¼Z˗ʆǍ˶Ůɓ?',
                        },
                    {
                            'key': 'ƤдǀV˘ϳȘѨāƛ\x96ғŞÎӑĹ˹ɰԎl˥ӫ½Ɵǿ˧ȉˉΉҨ',
                            'description': ')юөԥŎƑҹӦӟҍȌѵΥɜǟ¥ѷ?˦\xa0ŬПɲԛȈxϔÔΝŠ',
                            'value': 'ǣӦĒŹѓӉŅц^Ѯόҝʡ\x97ΙCԔӝțõʣΟ÷ǣCì˙ȯʼӈ',
                        },
                    {
                            'key': 'ŘПԇǽκƹґв',
                            'description': 'Ҙы˖ˣԡĠ˱ɨϡƵҶǄpϼмӁđҥʿÍС¨ϳҋҪAƩ«Úщ',
                            'value': 'ťрÉ,ӽǔә[Éžřʹϓɠ\x89оӊɃΉʴğǮʾкРûeÊɩ0',
                        },
                    {
                            'key': 'оЕɶƷ˥ʣɵ˒ӵɕõӋɥ\x81ıĚ×ϳȴȀƥþ͵ʰк˶ƪйϰʝ',
                            'description': 'ҰιɰƶϙΚǻæϒ×ΥѶӹБΡʎ»ԣшԭÓ˞ʾųȷ«ӷӧӛR',
                            'value': 'ɞĦÍψΤ҆Ȁbϋ<xȭҐɨȎTğȊЦɽ˶Ӓ%Ž˘ГγǠѱʷ',
                        },
                    {
                            'key': 'ȓ.qΞ¶ʧɓǌ˘ǕÂҠŮ·ÌǘɑϛˑoåɆ϶Wȥς͵\x7fʥč',
                            'description': '\x9fkȗųHǖѷčӏӵԖīсϝҝϢʠƷ˟ɵΨÛҶɣQOѺŹÈӣ',
                            'value': "ʰ҇7ĺ´ǜΩʐƣ=ϯʓӔƪɲʰ~ΒƞУ'ǈg˺҂ŗĵѫғĎ",
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
                'focus': 3172,
                'location': {
                    'x': -6699846386253486931,
                    'y': 4750121572353996880,
                    'width': 6606443288849864179,
                    'height': 2691158201509216420,
                },
                'minimized': True,
                'resizable': False,
                'full_screen': True,
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
                    'key': 'zœӟϚäυѴͲ',
                    'description': 'ŕƢϧˋ\x9aɬҠ^Z҇ƐÙƕӢѥǩÊʬģÒǲԞ·\x80ź¸ÅОԔȗ',
                    'value': 'a˄Ъˀǯίϧһϒç2ϞƐнĸœs$ɓΨ˒¾5ĒѥԜϣԎ\x81Ŧ',
                },
                {
                    'key': 'ˋ]ιʝǭ҆ƸȮšɠǗZϪ\u0378ŖСҮҐɉҫȡʹͻʂƾέLƐhƚ',
                    'description': 'ʧ҇ťɩŁΙƙԆΏϺųӢʍѲɭϺЇ˗ɬúюwĀůſŢȷԛҼҭ',
                    'value': '˟ҁҔ˴ѩƹ҃ɼ¢ΏʞɩӱͺΟΈųҪðѰʄφӯѻɨϚɩǪʭР',
                },
                {
                    'key': 'ǳӴҪBʯԙЫҳń\u038bƨΟϭӑǢˠŚĖùƪѨһʕĊΔĭйĔŶʴ',
                    'description': 'ɠȦԅӪӃљҚҁϣȊΝеѬŵĭУϒǰΣǛlħ҆jѥШҤqӥѽ',
                    'value': '~ǗӓШɈʺſũŮΆɆʰKӔЄǭȋӍȥҠԟʡÓÇǸЊŌφԃʴ',
                },
                {
                    'key': 'λKΫҷʨɜɉӉϾΔo˙éË$ĦʓɍöĭԄŦɏԇӬŗ}ƥ',
                    'description': 'ԊӡȟȍţǛЀлΉɥϪķȷȵŤPĩ±ЧȹƾϬȌѻzÒϼαӖȌ',
                    'value': 'ɮʖ±ҬåҜӼ͵ȓ\x9dQȟӭТ|аѤƸӄɣˮ\x90ǋĵ˹ӹđǉIи',
                },
                {
                    'key': 'Ū^ƋΏǝҬЦ΅˻Ôű҈LкġϣMĊĬƻтȀҶ',
                    'description': 'ƛҎзśŃʴ˙ęȶƞԎЇŀυӆϐ÷ӊŦ˭ȨǓҎ˴\x8cӣrӛѮn',
                    'value': 'Μ¦Jԉ˚ӒçˋÔӏӦĆ\u0378ųӼϹŌϷӲӧԑ˵ɼԚsɄɘ˫ȪǺ',
                },
                {
                    'key': 'ŁƮ×7ɮôЗȀɟѤʴқƵ_û',
                    'description': 'ɰ˂ΊΈü\x9cʩȷчʝϛǝɒȹӤѸĄђЁӝɐKѭԆɻɸƉӂϻΊ',
                    'value': 'Kο\x90шɤP@ǆǣĺƆͽ\x85ȩњƭϾʌʄͱƞЉʣȿ\x8aɐǐ(©Ǯ',
                },
                {
                    'key': 'ϢˀѮąТƴ[ƩSŊ%śʫoТ\x9eBʾĞȿЋνɞӑ˻¾ɌŸŉİ',
                    'description': 'ӢƬɀʵˮϰӝԏŶӿƀӘ˧ŪıĐÏnſŻҲȩɋρ΄ӻŞǓӧӬ',
                    'value': 'Ɖ\u0381ɴо\x98KɚʀȘ1ҼJґùԞ˹ƯҤѕћҷȝӮȮʦѵ˻Pȶ\u0378',
                },
                {
                    'key': 'үѡȬǛî˽ѮΧ',
                    'description': 'ȉҴͼÏϢԔǃǕˇԑΝŨȘĢ\u0383Cˊ@ƛʓʜӸɦ4Ĉӧįԏҥ҆',
                    'value': 'ʂǂ҃ѡҥǟĭѳɋͿűͳÓ\x8ag}ß\u0379Ǣӫȵ4ϫǊƗƻ˻ɴ_ϳ',
                },
                {
                    'key': 'ϬӇ`ƝÙȥˢſӂƃӆʫҕ˩ӈҠƄÑȽċ˱ǦwϮǊА(ɨƵˍ',
                    'description': 'ʄǸĻЈҦѱнɍԋÄ˖çԗɰёԣǶɑƴȫŞˠűɾΤɼԚɕȪ\u0383',
                    'value': 'θʧɜÐõ˖ѤʭӡȌ҃Űǳϕ\x9aƶŜŐ·ι\x82ҩͽƤĺΦЏԤâ˫',
                },
                {
                    'key': 'ʆCˬƪlɬϱǙ˙Ē\xa0ð£ѐϨȺԉ˶űƖǁėƂ6ͰοÝςʹ8',
                    'description': 'ί)ɻƚůĶ\x9aѧʖ\x8fΖÎÍԙСƏ:чңƓțөƶϔΟ×Άț)\x87',
                    'value': '\u0380ǩòȇ˭кɿŅ·Ɛψ\x93ϠŔŠӌҟʊҌŎ?əFĀĕqԈѠMӐ',
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
