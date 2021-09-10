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
            'x': 6912909478335002823,
            'y': 5492305195228891568,
            'width': 9070570133295191419,
            'height': 7843593420522731376,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': -7813531404260540503,

            'y': -7326035832955421312,

            'width': -3427418703245988824,

            'height': 3201467729294206623,

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
            'key': 'Ыθѳ˪˱˂ˬíʓ¯ϷƘGўӻ˭æϬɫԗɯþͱȽ˄ԏќи»b',
            'description': 'ɈƙŸҀвѵʄЬǘrČɦӟƊћӌìŎˋɡԨ˨Ӄύ×ˏЏΗʹƓ',
            'value': 'ѷˎʲɊЀ\u03a2ňҥˁɉˑοɐӧ\x8cƗӝҘzϹè?ǇɐµʾC:ĉк',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ù',

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
            'focus': 9965,
            'parent_id': 'ΚéV<ɢƓΡӛȷ˟ҼӻŌˢÖУƝΥӔǔĠЅǺ(φȝ͵Ęʫ˟',
            'location': {
                'x': -8891439916510000271,
                'y': 4320499996542093612,
                'width': -7267856104784746601,
                'height': -8169241250285564787,
            },
            'minimized': True,
            'meta': [
                {
                    'key': 'ʊԬ«ƚȸŚ˴ǊϝĎ˕ǣm}В;ʝѣɬÝ',
                    'description': 'λĽƥΚϛ`Т˫ѧӸʐȦЖǹɲǵAԖȉӫěǎɝ;đϿɱ¡ΆȄ',
                    'value': 'ï4ϋƋĩԕҚρʆұÈŔ˖ʳƯŔïӦСʳöѾˮ÷ŤӽȠЕӇȕ',
                },
                {
                    'key': 'ήćƞ˔*ԀψŽͷ˚к˔ƌşß',
                    'description': 'ƘӻŞɝѨӥ¿Ԍˣ\x92Ӯȕɱ©+зŦǦŰyþϫ\x8fӫϜӱǂҠťϏ',
                    'value': '҈dbӌͽǈɑӯ˛НӡΙˈȰɾѺ˰IеɋЪûγĹ\x9aӖǹӴÈϧ',
                },
                {
                    'key': 'ȶ˘ϝʋɩǆĉnħƠӜϻ<г\\ĻidůҫӔЈѪ3żƬȘĐϪǔ',
                    'description': 'ǍԗϯԁԊȧŔŮİZ×Ùʔυi<ъϋǳûњӯʝ҂˃іʤİģԝ',
                    'value': 'ˑǅΌǡoϦȄӳʊԑԪЩơȭüɋʶ˯əǬɴȨǬϿϓƹϡйªŉ',
                },
                {
                    'key': '×цȹ´ʅʋЕ¼ĪŶ³ҒОüϡгϺĵЯİ¹љɫ\x95҄',
                    'description': '˫˙\x85ȇ˨İьӕȞ)ě:ӹʛ\\Ъʩ¯ҪǽǎɨǐʽʼʞАǔŞ\u038d',
                    'value': 'šĨƷ%gϟΗÈ҈ΧʫȐʧŦƷ˛<ɐƪҷАȼυÓόĻєǲ',
                },
                {
                    'key': 'ǠKƈ˜˴',
                    'description': "ÙĶҧΧϨӬѝЯӋă'ҐʕȴȇӫțҔЈǇǦΡ˨ŔԦŶɣ϶Јǈ",
                    'value': 'ĀˣŀƆχƔ¼Ü˸βϒ˴ϩӣçœ·ӑЮǜ\xa0\x87 Ĥ]ƤРƵƖØ',
                },
                {
                    'key': '\x9fÞčȺ`ѢtЊөӨЃ\xadLĹщƙ°ŖɎȊŘ',
                    'description': '"½Ϟҥ\x81ԡé?ȉɿ¶ʭėԟӓùÆǅРǑҁѣǟȇ\\Ţıίрҿ',
                    'value': "Ͱg'ĪӾҺƺέΜçѴшŖҷʤŦÅLĐΤтͼʟ½ˣ'ϩȀԩ\u0380",
                },
                {
                    'key': 'ɠ˲ӧǨ»ǌȐǅư\x80˺ȬőоȻćÈʒϽǊϭєÙɉүŷӦά҄º',
                    'description': 'ѹƧǊӭΝ˽ȒʼÚʹΝɠӈЋň҈\\ΑɞŧѠ\x7fӁ˶pӿ/\x89_ѱ',
                    'value': 'é/aġÄˡԞХөɹƶʪȕвÖɼԗiο˚ƇāҨʨɐŮԦƉǩō',
                },
                {
                    'key': '˦ӨĹʛƎѤʩóϋǢӓƣШН!êɞæͿŰŜϡщ',
                    'description': 'Ä.ǷљÞmεӑµȌҚÑ9ɔ\u0381ҢɁɛӑӚǉǐƷЕzěн˗ɚȤ',
                    'value': 'ȏɋƧƮĆŎѠʓΏ\x8eдΦҒ¦҉ȲɌЊɧÞ\u038bӅԬņņԇĐŉӰŷ',
                },
                {
                    'key': '½őԌ˗ñО',
                    'description': 'ЍčɮĊʭѨиӀ4ӣǅΓҏʢ½¬ɭǰʨɣbàźȶѽȜǺХͲƀ',
                    'value': '˰ʣɡǣԄVάϾΑɺ\x87ȟ¥šĹñ÷ѧ\u03a2ŗρ\x8a#ʣρǬõԟĬƒ',
                },
                {
                    'key': '\xadӢ«ϵηЍЊϼҌķȝƇĩņ¸ϗˎɼiԪλӧŸČ',
                    'description': '²ɅƆÒ˚ϵҩԨͿ҇И˂упʈ\x8bˉ˽ϨˡѪˌĺͰɮǄҩíĈϭ',
                    'value': 'ȴ;Ϧǹƽӌѐήʫ+Ƚ˄Ϯ\x87˻˗TɳˈÝуƊƜUʭʹȲѣʑƶ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': True,

            'focus': 5349,

            'location': {
                'x': -6717665628499785299,
                'y': 4856516978837218462,
                'width': -5982692189660573662,
                'height': 8799086481953830869,
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
                'focus': 1320,
                'parent_id': '|ϚǗȕǽ˔ξÜǑǵțϋŊϩЫ;ͱͲɻʿɁǙѲ|ъуʞљP?',
                'location': {
                    'x': 7623196501001064358,
                    'y': 3234821364858060736,
                    'width': -2502969526490328598,
                    'height': 3478601840060948908,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ʄƑŢõϹГЀƕҹʮʣϔ',
                            'description': 'ϖьȪǞ\x86ŕФѦɵӼ˳ȥ#ɷʙч˝öȪɃlȅɆńɘčʑƗŰҬ',
                            'value': 'ȾӦɝĽɮʀ˖/ѯ\u038dԔўÿȪȩȕѝ¤˶ҫυѭɿƅȼΆǏɴȶė',
                        },
                    {
                            'key': 'ЬȷʏȗͲԛӧϵċʴµĜ',
                            'description': '®Ǉʌɹ҇ǚҕԢЈҀǁҴѩʐӏӕѵӿƕГšюhδĤΓN?ә]',
                            'value': "ӦιɞɮҗҜ'ǕɫƟЄ˄ωȚnǄéҀ\xadąřʴʔиҤӂøbϼĐ",
                        },
                    {
                            'key': '+ΔpӨдȌϝáТʶ=҅ŪΤԨƀȜȴºɌēûϘŴŻˍе«É9',
                            'description': 'ÕЋÉ\u038b΅ҕЗɉԮȂȑ;hҏƉ;ҠұΡʒȨфºƟʱӈԔö\u038dʜ',
                            'value': 'Ɇ˦8ӇȮʀčǳŎӯʴ=Ⱥ҉ɸӳϿ`Ï\x8e\x82\u0379õǙ˫ӎϘўɫÖ',
                        },
                    {
                            'key': 'ӠϏҙӭ"ϡăî҂lҭȼġщģΞѰƤƝʷǬć҂ŞĚ\x9bЪ½Ċ˺',
                            'description': 'ƟѴɱȠǷŴ7ǼůǬ;MĴ-V\x85ƠŒĻ˫ǈʯʖǼѫûʦÖФ6',
                            'value': 'ȡæʒʈăȟЖϒŕoIӑaíĉʿŶÈƂȟӘͲғӒ\x8aÉѮZьƦ',
                        },
                    {
                            'key': 'ąOŀCĵƇ',
                            'description': 'ɚјˀŦрѯşŇȔӇҏĄэдηƢƿԃ4RГʑëʪӨŖК\u038bђñ',
                            'value': 'ϋ҇ĠoɱЖ¢"ȥϴԝϮŭξϧͼiŪұĤ-έԜӧşˑĚЕÿӋ',
                        },
                    {
                            'key': 'ѽίϘÚђ\x99ȒǮÕJЦX(ȤʎӤϒ',
                            'description': 'ƻůĴƱ`ƟÈȝǃǇΆʸǃǯϽͱҺ+Ӊ\x8aȓǧ\x8fҩђ҆ҾӪfŎ',
                            'value': 'ŴǏʎʊɢʅԎѨȯĴİĹԚԛəXŀѷŋȳǃ·ɧÑҒμтӅˊŐ',
                        },
                    {
                            'key': '\u038b',
                            'description': 'ЮĹӔɢƅґOŷĮ|ΓǎѦӄɨαǣĢΘӨȕıˇȒ;úŰӭҀҝ',
                            'value': 'ĴқͷҚҫ\x8aďˉРӯҟũʧ˰щ\x9b˱ЫԀaȰÊȊƜƲŏ˥\x90%Ę',
                        },
                    {
                            'key': 'žĜ|»Ƕ˂ҽʓˌϚԥӧȂЩĭʹĦƀƝкÉÄѬ˂\x86Ð\x81ԍђА',
                            'description': 'ʰ$˓ҘƘǇґģȧҥƃҞr@ʠǡЁϝȕǊ˘αӣÄɁÔӧιҫѱ',
                            'value': 'Č4ҮϮºˤĉȞşʂ\x8amUƗ\u038dƳψˈΕǦl˒˸ǰ ȴʺɖѿɧ',
                        },
                    {
                            'key': 'Ȉĕ¤Ӱ҅˨ʶϙʾğʂ8Қȕɝɜ',
                            'description': 'EʗбҨȭöƍ˦ĽѷТɣˠȝšØcɥºГ˧jňΤǩɩы˔ТӔ',
                            'value': '_ǝϽu΅£ǅŁϪҎǍĄгЛԓȚφʺӍÑΥʱ˞ńӗǏʗҒ2ƞ',
                        },
                    {
                            'key': '˴ҌȊҳТ',
                            'description': 'ƦёҜс*¹џԏӂѵûҠ»ΨрҀúˣѮǍ΅ûͱηɩӺ×Ŏĩʏ',
                            'value': 'ѳɫ˨ǤʕϧéϑӟπӸȚɋõǖүKЃΏȧϜƀπº͵Ќ^łơŏ',
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
                'focus': 9757,
                'location': {
                    'x': -5866105358446467217,
                    'y': -4196500607478616592,
                    'width': 8618078713326273426,
                    'height': 5005559401284090186,
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
            'reason': 'ϜЗкǛ˩\x99ɑƣю˪ǸӁЇIЯЦˁӗФ»˕Ū\u0380Ιϣëʖӝ˖ʿ',
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
            'keyboard_focus': 4370,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keyboard_focus': 2106,

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
            'window_id': 'őąĻΎT\u0383λɹԧϡȸэǘˋǳɲғƆ<¿ԋĄηοԂӠӍԟǙӞ',
            'location': {
                'x': -6072944057634594417,
                'y': -6653967255131967668,
                'width': 4084280937080603384,
                'height': -5039354462191659080,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'Ç¿Ō˽Ѝ',

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
                    'window_id': 'УѠҚÔʧрӮӊȴψǫ\x94ïV5íԇҋĝӠϟ˨ȚñʦҕΫǮʗӜ',
                    'location': {
                            'x': -8386986090813331314,
                            'y': -7032128343118788100,
                            'width': 1824927223219169813,
                            'height': -1596937511575309581,
                        },
                },
                {
                    'window_id': 'ë˱ԩ/ʤF˟eƂĢQƑȓ=ԗͻȍζ˪ƕԇɸ˙ҦƏɲûĤўǿ',
                    'location': {
                            'x': -1533676059080653133,
                            'y': 5954832022837511897,
                            'width': 2418839602580447759,
                            'height': 8245719006750393936,
                        },
                },
                {
                    'window_id': 'ЋӈКнƠó˞ʹǔƕţƸȽӄёlɎѠñÌą˒Ѻǰ˚Ѓ§ɘњʜ',
                    'location': {
                            'x': -5189292124843809281,
                            'y': 2064106770610831204,
                            'width': -2719089979874334183,
                            'height': 921223133106851540,
                        },
                },
                {
                    'window_id': '^Ζʡ\x9cΡϠ˶HѨϗȫԈγΖƐт˛ͼƹΡ\u0378ԅς¾ÍŤѭÉʶ\u038d',
                    'location': {
                            'x': -4648601180544998586,
                            'y': -5058136612346864291,
                            'width': 1548154859921191268,
                            'height': -8700748237558270610,
                        },
                },
                {
                    'window_id': '҆ʃ¦mҍϝǌțĭюȻҊϖ\xa0\x7fҿnȝƙ˨Їžļþʊ<Qxɚч',
                    'location': {
                            'x': 5329895127424372428,
                            'y': 3242145789612428233,
                            'width': -3683285503468679830,
                            'height': -7198301723683623102,
                        },
                },
                {
                    'window_id': 'ʕѣʝǼʣұňɓ\\ҵЯˤúǳѰ˒ÖψҼӤ£4ɕȣҘƏĜјǣʗ',
                    'location': {
                            'x': -1990855352676779457,
                            'y': -4347632097999253968,
                            'width': -6961367567031779661,
                            'height': -3966157919819581332,
                        },
                },
                {
                    'window_id': 'ѰȽСrǞΘ˲ИϛиϒҳRĴƊˏǷƩЅƷ¹ӉǾ˥˃ŲΣ\x92ɋТ',
                    'location': {
                            'x': 3932839346458546321,
                            'y': -7079802506050423873,
                            'width': 5047262070526784927,
                            'height': 4318899729175985170,
                        },
                },
                {
                    'window_id': 'ÄΌ¥ǈqпųRśïҵɍѠыʙФʡʸƙϜ҄ӭÛÏƖɨԕ\x9cӚΘ',
                    'location': {
                            'x': -4593191511087509319,
                            'y': -1814627376472820660,
                            'width': -9015308477274588339,
                            'height': 61001754429989254,
                        },
                },
                {
                    'window_id': 'ȳѓѭŕĵѝьŹƍƒŉ\x9d˹ʱȕħѐŞƴƌʉRȉΰÇˍήȲ¿ӫ',
                    'location': {
                            'x': 5296314969540878884,
                            'y': 2115484885946314509,
                            'width': 843069790577907674,
                            'height': -8701378046575465944,
                        },
                },
                {
                    'window_id': '˪ҊǘȞXΌŤ^fӺèƙԮƯΩɦƂ˽ÒŁкАɕɟˤ҉Q͵Ϻ/',
                    'location': {
                            'x': 9084845894190045718,
                            'y': 6704912675139566071,
                            'width': 2955735087453767964,
                            'height': 489067775927466591,
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
                    'window_id': 'ԛѳːÇȽ',
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
                    'key': 'ԙƘ˞\x9cǤȭrΝƛħгԞīШϦђȱŪѩƸŸрԥK\x99ǩďϓϟѭ',
                    'description': 'UЁӢŶҪőɺȰĉѧʦʷ}ͳǖƄãŌuΠμɂ\x95ţ>яʉßӧè',
                    'value': 'ǈîËǦѢˁ\x83ùȗҔώŊӓºȻƩƨȈ.ŸȚǫƤӠ\x8auǲÌЏӿ',
                },
                {
                    'key': 'Ί¯ϒdþȭǬҊҚӸĳϋ47ÙзͳʗϻδΊҠИѼрɏԌѰќH',
                    'description': 'ϸВ7Ϊ˞ȷȅʣѬӲϳБæȣʴųϛ\x7fơșĸ_\x8eűϜɣ§ӈa4',
                    'value': 'ˡǎӊ_ԓV˟ŉΌ\u0383φσĀӫiҎΙƚÉå0Ԓ\x96%АůǇŐʇǣ',
                },
                {
                    'key': 'υœÛѡϼǜŸô',
                    'description': 'ƋįĺҾ\x95rМʱѶμʷӴνʹ҃ӕʦǪɿҍСԖŲѲɱîѻćϸö',
                    'value': '˟KӚɪàɁϪĺӼ@ЛӿxȈ϶ӽӾӗ>ɤŭǖԇа\x81¸эéҘĉ',
                },
                {
                    'key': 'ƟĄЀЉáѻѾӊѲßќӷӇϫ˒ӡƩЃǻS˫ǑҖŜӟĐŬΝҚЯ',
                    'description': '\x8fəâӤτΚ§ˈ\u0379ҥǇʩθҦ\x8eєȍњηӷ©јx|ņƤʀјƸæ',
                    'value': 'HÙԤðvѶԖʼ5ӘʅӰķǰӱĀèѳЂ½ɵˍϺ˂m9ɷ§źͷ',
                },
                {
                    'key': 'ǡƽӂӎҝǐȼҮïϨϭʶhҋN\x98ċŢɮĮΕԢŅǿý@ʒȟԜʧ',
                    'description': 'ұŁҿűȽùʯgԫ;ˠƃӂГ¾˟ЎƉěԑʫӮӕϦȩХͼйʃą',
                    'value': "ʥHҧˁʬ¼œ'îǉϨȟ\x83ЇƭΗǑп\x9aĂǧҌМȝљѧ˷ČåƂ",
                },
                {
                    'key': 'КйѲħȯԍʿƺσˑ\xadƽӁĿӏŢѯԥΟҭȶԊ',
                    'description': 'вɔʝ=ΠɄίю˒ɵƹ¸Ҹϛ˗˓êNҊȲȂƙԀϋҀăƇвʟŮ',
                    'value': 'êφ(ϛβʉǼȒԔÕȞ҆ЫθüƚƠƒΫϠ\x80ʮ҉Ʒ¦ҕƵͶүë',
                },
                {
                    'key': 'ӳ˱ԈԥѷæцӎɄѽɮǒԇԅqɅӝʉРƘ',
                    'description': '\x92ø˵ē\u0382ĠšҞɦ"ʦΗŒԆ͵ƦWſǺƨʬ±ŠùɒиϣȿƂӓ',
                    'value': 'ϲӊȬ°ȝƓXȢʟɑϴԖиĎΝӾʭąйƑЙƘκϊвԡԝϧʠҡ',
                },
                {
                    'key': 'ot´ĭǬҔ\x99кУϐŪȤżĎЅÙɬºф\x7fU?ԑʖŚǈ',
                    'description': 'ӤõˢϵÃӒΌȎĤИӵӈɧÃщ˾ƺħӱУȣģїщďӧİ`ȥ\x9a',
                    'value': 'ʁÍѾ\x94\x95ϵӊhωȹŎïӝ+\u038dŜʕȴˢτǦɊҨǝ˯ǥƧÏΞӭ',
                },
                {
                    'key': 'ÒҪʃñȐǓʴ^ĘȰĹİÙ(i\xadғԮǽЀ˲¦',
                    'description': 'ф\u038d˚ʘųĊȱҦųϢ?ϷϰӃ\x90ɂɈÑ˱ӻю˼ÀԮ\u0378ύðԮȂР',
                    'value': 'νɗĈɰƢѠ¤њͺ\x9aĄīӢɾǱȫЊьVǏŦÙҶ(ɀʗ\x9fĝ´ȩ',
                },
                {
                    'key': 'wȔ\u0382˛˗ŵ\x97ҪÎϢĥĠˢɪчȏΘƜʹϖĖʆȂȡ@ɥBͱσ0',
                    'description': 'üʽȥΏҙƠьӰǦƔȟήĩǵƶў\x83ҭɲԣơΓΉкȚΥЕԠůç',
                    'value': 'ЂџťŞªΞˢԧÝɒȵʹǫ.ɱôȨЀʙ\u03a2^łŚhʥΡҡÇӥΓ',
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
            'focus': 5474,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focus': 3493,

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
                    'key': 'ˏɚϯ¿',
                    'description': '\x90ϺɅҀÁϰĎʑîϜΔȢԌEß!ʃԩϤԧYƵ\u038dǹ˫uНɣм³',
                    'value': 'ªΖüaμƆĐҞǑϘɆ',
                },
                {
                    'key': 'рўɍQϢJ4ÌΧɼϮϭfɾϮ҇ǯ/Ȋ\x94ǜЇaίȦӺϩǉ',
                    'description': 'ŢHҡЇшҍҀːȇΕƵу7Ҍʻǫɏ"Ҿɇ¤ʹЬľѲäȁӈ½ң',
                    'value': 'ʒΆ»ЗȾήʌͻƋηʢцwԎҟÁ\x7fΞ¯\x84ʷØȑ˾лȬƥˏјϪ',
                },
                {
                    'key': 'ΛɦϚС\x80Ԟ¢ҊϕҝDђɊɈȚƼʋɾŐ¾ӽɢ/',
                    'description': 'ņӺʟȰ\x92ПÔѮѷΰȇȏЍĪȥȢƤǩΨŜɚǃќ˘ɪ[ɽcԞ˔',
                    'value': 'аʬƨʋʒ˵šˋϡʚǙӛԒԒУĐЍƥϵϸȲ»ƂȤϠѣƷȾß2',
                },
                {
                    'key': '0јȔύΦҊƔǍ`ȷʤʧϾЮ˫ˋĬď\x87Đʎ΄òˌ´ƀҵͱ\x8aѱ',
                    'description': 'ǫˁȵƙӡƵȨϙ˱ҪȔÅŞ\u038dĄȧҲ\x9dēϙǝǀńǭȇҐҤģūȂ',
                    'value': 'ғ]҈ʇÂŗȕũAȥŲ0ӎù˗ҽŬ\xa0ѓʸĽƢ˜ΆѶ±ȫɡ˙Ş',
                },
                {
                    'key': 'ԂŰЮʣȼhӂʺφʡ\x99ɼԉȦ',
                    'description': '˻ëŲзʣΊʩ{ŻaΉЉƺҪɜәȅҽӋđǶпʱȣ2ўÚüūÅ',
                    'value': '˨ƧҤê϶ȡΑ3TѺ[ȞɕδŭϢҏ®űΣɓ˗ϋȠ˓ťĪ9kԞ',
                },
                {
                    'key': 'ˊǍʷħϝČ\x8eȺӎyĵʠȱ\x99ѫ\x9bƉ˻ʈԐ˨χԌëҤАǪƭ˥χ',
                    'description': '\x81©Ϣʚœ@ÁƿĮűЛђɈǚςƭϽÆħ¬ӡŴҟ¬@ȝǋ˒Ɖť',
                    'value': 'ȆʟʓϲǆҖԬƎԗѭŃЌƛО\x8b;œɥǘђҍвˏƨħϛɛÅÈH',
                },
                {
                    'key': 'ͲɊũчãʹѮʯǪÝðϴȤђą',
                    'description': 'іԦ҄ǑͲǐ¡kνɪţӉӘ\x85ψ\x9eȹԂǚǳͼШɠоЈ˹ȆԐўх',
                    'value': 'ΧÈҾԘҠǸ®xǨ˯ǌ¦Ѥҍ¢ďӦŽέԡҋԣȜŵ×ѾÃәƷȐ',
                },
                {
                    'key': 'úҴºчЎË¡3\x96ͱȪʊƇʢơɢҟБºѧɢУįʚʠʌ£SŊˏ',
                    'description': '£ϨͻΌΓԕƐƹчˁɛӍȮϭҮmǷʨùԮэŴκёɋѺ˻λˢԌ',
                    'value': '!Ѿ\x90˦ɹʹËäíùӟıӭҡԠСɸƔƒўʫɯƊǻBӤȖ7TϤ',
                },
                {
                    'key': 'ÒǛĜҠ@ԐîƤӏҨ´dϐʒȷŮϔĒ˸áϾХϥԓʿƾԞ^ρ\x8e',
                    'description': 'ӘČԗȤƱɧA½ύЅŨǀǘɂˈːʗԒʩɺɇńѩΩӉʣӼoǃҖ',
                    'value': 'ĔϻɛϿΥтb[0˹ȳΒźѾӕЊŒ϶0\x8b˻ѳЦÝѨАƫú¦Ɇ',
                },
                {
                    'key': 'ɘʡìʜͱɰ҇!˗ωЮμŚɊϚȥ˛\x9fǧžȼ˖şǻ',
                    'description': 'ɠĈɡȾĢR¤тdУ˫ȾЃɯ϶ΥѼҩƺвΝäҾʎӋɭńӂ#ʆ',
                    'value': 'Їÿѻáøғ˚ѺϺ.ʹupÚӺ˪łëѤʪǍʥѸ¶\x99ΨŇϏü%',
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
            'window_id': 'îȄԩʣƠ˱ʿвԨJ½ЍџĊȳʧŨчĜ¿ϜКĮŋģӐYɈƫϺ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'Ó˙ŚVɁ',

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
                    'window_id': "Ñ'ÆƺνҡÿT˟ƣKıĝ-ҟˊϘΨҨʤӬxíӍӒȫԇӑǪĤ",
                },
                {
                    'window_id': 'ɢ$ǓüӪŉ҆Ų˻ϲРÎӨȴƨҟґ\u0382ӸăďѤþƀОɤGӣÏǖ',
                },
                {
                    'window_id': 'СӻΏНǎĶȾөϋҨȂӍѷưSƝŝшńűьɧӢҭѰ#ɾĖŚˎ',
                },
                {
                    'window_id': 'Ӳǝ\x93ΫӪƈđʿҠƂɖɧəə`ƟʯʒЀȦҡȅɬʜɏӸљ×Πτ',
                },
                {
                    'window_id': "ЛɫƚɯπӑƎķЃˡɿ\x93г-TͲĔԥƆǣ'ïɉɰǸÓȖÝbϧ",
                },
                {
                    'window_id': 'ЁԛµҷЁ{ķκ͵ǄɞЌȈӜӨҘŪτƨȎϘΗΦ#\u0380\x8fƐΣD¾',
                },
                {
                    'window_id': 'ȘȳТËʵϹóʠΊөĦ\xad\x89ҪA3ω,Вç?ͺΌδӗXǫΪ·ƒ',
                },
                {
                    'window_id': 'ȂéϥǹҠO҄јƬqșӱǁɋ²¬3ˢΎĨ}ѝQѭăԁƵr˕϶',
                },
                {
                    'window_id': 'š\x80˥ŀƮсʲԓ˼϶ǜоЇҁơŨӮġҔεɗƆѽǐƠ\x9a¥Ũȭǡ',
                },
                {
                    'window_id': 'ųͰҍƖÑϧϾňӜXǥ\x8a҉\x8bƠ\x99ήɺԠΩˏіǑɼԣȊϜӢҪϯ',
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
                'ѸQîƜſŕÙєƷОӾόiĖПɆыǄ˓ŧɆʷҏȷƷVӿѧïƩ',
                'Útƶɍ\x9aУǗ1ѡкɨʻйҥôӍʛýˬʰTĞʊFϤЌáͰĪЮ',
                'ӈћéǱɺɨѻԠƵŒӡʓ8ϪԒmĸԈˉƇӁ;єʣ¾ʵəЂňƄ',
                'Ĕū˄ŊγĶδɺō˃ƐŲԆȦʱҍϤĒŜǪǍ¾>´c\x9bǺӖŕ˶',
                '\\ÓɶΕȥÜһѹӧ¦ȑКρϭƦϛȼP³łÉƻ\x8dЎѪŇ\x9cĿAE',
                'ƾ*ȉͰ҉Ɉ\x8cƓˈɱԋφÕЭӊщğ¨ӥϽſG˩ҩԀ\x8dƘӝ˦ą',
                'ėƾɻҼɶѧ\x8bʇӴƺ\x89СAǾßʩǟɕũĉ2áҋщȻӊ\xadÐ\u0382ŝ',
                'ԇʯìɎϝƌnĪ˾Чʧ¾ȫғνӀИҢǧ±ʠӅԬǾϻȀʵċфɬ',
                'ϑΜΤѰ1ԝАϊμŰƔ`Ƴó\u03a2ΘЫҘþ\\Р˯iȲɒлȚӜМǊ',
                'ȬҡԄÊ\u0381ѶŖнɎЇѧȺЀѿцԅʇӤϡ˵ɐ\u0382ÿȋɦӿӄáɮσ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'Жи˶ŚƟ',
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
                'focus': 8897,
                'parent_id': 'ǦΐZӴŅĨШΊÌСηçӑҚɫѱЧφţԉ5ǀʼӒѓϝȨȃƸА',
                'location': {
                    'x': -4631069318058240244,
                    'y': 3310668177569519107,
                    'width': -2606299175322002516,
                    'height': 2345519819690157241,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ǼŀÜӱӧԘ95MǳԤ\x86ĴʯԢΟϯΕˣɜǍɸŇŦϯǺǔýΞϚ',
                            'description': 'Ƒ\u0378ǷOʂž҄ʏĆǌŘԟĵОɐͰǻԃӝƫʞ\xad»λԙǫϰƥ4ψ',
                            'value': '{\u038dƙȮPӗыŹԒѮӪԪtňƣңʉŁѩ˯ҟʀŠǢɘ§ҥ\\ǿ\x80',
                        },
                    {
                            'key': '¸ЖʎҰAá˃ЛĶіɚΞǑѪҺ¯ĻԒɘť\x89ÿМ',
                            'description': 'ͽȔή°іƎŬӄλsҢЗ[ȅϪԫˇҦ}ÇԔӬǪ·)ȄƄΦÅƋ',
                            'value': 'ҸʀʸFΣκśƔʄʀÂ@ÞȯĔΠʷҡσƔƸˠ¡ϴϗԆĿȣZ\u0379',
                        },
                    {
                            'key': 'ѬΕƢɱĴŔǔĆȟіʬҐɏƟ¸s\x87ʖҚ¿ʷÔ˰ӳ\x8fϨČϥǂ',
                            'description': 'Νȧζ¤ɸÈͽeАз]ƳБǣ2ǈԒҘɫШ˗Ƭ˓õԇѵЊ\x97Г˝',
                            'value': 'ÄPЦȦ\x99u_ҍǞÍĆĸh˞ҁ9Ï˪ĖƜ\u0379ɠ˧ЇKƇϓӤȲ|',
                        },
                    {
                            'key': '˯ҤTȫҢΖŧЛ',
                            'description': 'ˣӦКľˢǷʔФȨˏǢɸƼѪѣί\u038d+CԇʵέŝӘЇѫѐҝɓã',
                            'value': '>ǩǂăΞФԕҤȔϋkƉ:gȭԦХѲʏ\u0378ʙҳõÈƘǒMЁҸȴ',
                        },
                    {
                            'key': 'ŤНёͷŠӳǹȍ',
                            'description': 'ρ°=Ϛȸmу˙ЄĪȀбʃѕє˺Ύ˕ȖÁņўğѬÐ˹Ɂ˥Ѣū',
                            'value': 'ˢķǟϦ·ĳʂ\x8fǩɚĖњǈΐӔȄʘӴĬć˗þέŎѭɋΫƟю˶',
                        },
                    {
                            'key': 'eΫƞŢɤžӒƒпΦôÜйЛ',
                            'description': 'кͳбпԠӅώɔԕ©ԩ\x9aǭtWБѬ\x80ΪΝQ΅Җˊ¯ϩӅʎƴˬ',
                            'value': 'Ɖèϊ¾ǟўҟŨ\x8dўHϖ?ҍԑƀŨőӴ\x93ς҉ǰɞƌǌrìѿЏ',
                        },
                    {
                            'key': 'ϰѱөѧ\x96ƔŪʵąĲǪńΜ˙ŨǅɾŢbаĀȮˢ\x9fɒԕÓQʐԦ',
                            'description': 'ûЙҖҵΦӉ˳ӨѯůʐԜ\x89ɒȝӍ6ӧѡțʊĳӍ©Đ˛œǈǠ½',
                            'value': 'ͷƋ>˖ĕԓƏʶʓѲǹѡЫԒïɪŸʞвƥҭǳșӍǵˣ[Ĥ˘_',
                        },
                    {
                            'key': 'ÏѠɥшǾΰȇƤҫНьԉŌΠοĠS´³éқˠԦѻҤTʮÌҒɻ',
                            'description': 'Ι\x85ŗςǡǻˊŌ˙ӍϕųΏ͵ʌϝƀƉӰƟǴӀЇ\x88ɛˢΉŋˣΫ',
                            'value': 'ʄMцР˘ϞƷˮĐlŢәӿʂӟċ÷įÁεӤĀΫϱϧs˼ɨÚ˙',
                        },
                    {
                            'key': 'NԜѸ/Ϫ\x9bȊЮĎϨʨfȖXgʍΘėΣȾŔˮžðƷÉʇůҘӡ',
                            'description': 'ÊΚʲŝʓʊԁíѕʐĚȗεʤЦΑѼƎ£ѝȃ¯ҫǶОӟʟêҊң',
                            'value': 'KĂʀХǋɹӴϞúŁϮÃәԇɟѸ;ϹѕūŕïѥÄә\x8aǯʞǚǉ',
                        },
                    {
                            'key': 'Ӥѵʿ:Ўәyɳ\x80Ùіς˖ǒĤ_ѾɟϞǈӤģ',
                            'description': 'ǁ»ҵрuɷƅђ3ҽс˷ŮεҖ+ȑԣяÅUş=҈ÍC·ʦҪБ',
                            'value': '˞ȌϢhƚѠ×ΔһьϩųrpŬǚԁǐOɻɃɋ˔ЭǢŃΉӽʍ˹',
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
                'focus': 9120,
                'location': {
                    'x': 7668748832035649984,
                    'y': -8079704856843543822,
                    'width': 3283977825309638741,
                    'height': 6284904102698160356,
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
                    'key': 'ȎϨϖȩTώ',
                    'description': 'Ɇ҈БдϠʭеêʚͺ\x99ȑſHɒ¹ҢлŬĬūȕǰɢƹ\x93ѥˁɹʱ',
                    'value': 'ƝĽǋќӡêĨ˥͵Čγ%ЛίʘĂɿ˖ÓψˌÔɲЕ˥ʘӝĐҪŇ',
                },
                {
                    'key': 'ԢĎžљɏλңИǉԌГǰѡΕВŃ2ύŔǻԚØ|ˬтԇΕ¢ԔȬ',
                    'description': ')ҖøȭԐMŏҹˋ\u03a2ɻˆVɽȐ˪ҖϳλЅќϵʌԪ\u03a2İ˘ʡѴ3',
                    'value': '5ʜԏȽD;П,ήzҕƆǀ\x8cʺ˾ĬƀǟИŁ/ӓЮ\u0378ĜǝƜȃɹ',
                },
                {
                    'key': 'LǛʗÂɒҮΠÜȠϬǬΩûəˎWɞGԕ]óʝΰȆЭϝϏкǙƆ',
                    'description': 'μįҨӏ)\x9aäҳиȂɐŐϊԆƨθįȊſϔéΦǥ¹»\x93șƓBҍ',
                    'value': 'ʒńΓѿ}ϺϝѯžǳĺʊǡTİzʼŕЍưŁɱƕˊң°ŠƐĀǱ',
                },
                {
                    'key': 'ҹГǇуˀcӷţRŸŹ>ȰþØd$ŧǖǫ¸ȣнԣϥ˲т˺өԗ',
                    'description': 'ȖӺ˃ĻЇˑϧѶ΄ǃӷɍҚЩ6ĥĝɿ^)ȒǬÒīǡƍ\u0379Ǭϵn',
                    'value': 'яʵȏюȃћũŊѭѡʕƕΌγЙФƹҖñöΞϩŜΡ÷ΗúˈҫТ',
                },
                {
                    'key': 'Ȍѫ\x9eˇœĝĥËƓ¹ǧ´ά|«ϿҖіčǧõ ŭªɇ\u03a2ǰćПī',
                    'description': '\x82Ϸ<ΔPȚÙҩҮѬÊԀ˚δ\u038dȎJЀɮóĸґŗśԖηżȉ;§',
                    'value': '˻Ηę ϙɰ¾JCTǚċʫԒ^êsԓ\x9bɇхҶΦҀøǩʍѾѯû',
                },
                {
                    'key': 'υΌǛįǴ\xadʕºҔΐĝĀеӜÜƨ]ӎwҘЃӢÞćϭÿϻ,ϞӶ',
                    'description': 'ǣņҕ\x8dҡЖǠ˽ƝɡɸĴȼ%ǋōºƯԭЌʫČǨτЋǣɥɋ¡ȿ',
                    'value': 'ԅ҄}ɾƨԓύʋ˨ȯϘЍp',
                },
                {
                    'key': 'ƌŨБγ˒ǀӞǬƥϯąĵӶ¹ȲжÎѼѭư',
                    'description': 'вѿƃԟɳѬκӷ˒ȟȵǖb\x89\x9aʝ҈Ϗ ԖԉÅ\x8bЧѐǬƖҦԭ´',
                    'value': 'ԦЉÎĊ˩ɐ\u0381ӚϢʽИζĝƅŝȋԖǦƺǣўƽŁЍԀќёкτO',
                },
                {
                    'key': '҃ӭə¤ǽӞԀ\u03a2',
                    'description': 'ƶΠƽӉǿҌÈɮ˦ѕѸĎ˧Īʳт˅ȟÂʩѝȡʝĦɖȉɵ΄fԇ',
                    'value': 'Ȯ¡ˎі¢ōԘŮԛ\x82ɦȫԍӱ˄ӾʺȦƮԂďɴɊ˂ɮҤĻǳԭӏ',
                },
                {
                    'key': 'R;*ԍιƾɛǥ¨ɂƙ4ƶΈŇ˝ԋѸȓΦǢΞʋШʈ^ѫ',
                    'description': 'ґȥÒԁŠρęѕ\x93ОіȬʦ϶Ԛ¨ȺюˊőŘȍBȹҳuȔ˥ǼΞ',
                    'value': 'ҪкǥԏȥņȬʎľԋ\x9b\x9c¢˹ϓё˹ǑΫϾϨҟʛҔ˓ȶΆĭΠұ',
                },
                {
                    'key': '·ϹƎóфdюAɳӨɵƊ\x97µѣʰ',
                    'description': 'ͽBM¯ώԆʠҠǪȒЀ YΣȒĬ϶ЊěԋȃӧǐƟμ',
                    'value': 'ʾΨãҺζǗʟźӜ˰ìӊň˺˅˓ł\x96;2ѾȶϧřʼƕΦ¯҆Ȭ',
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
