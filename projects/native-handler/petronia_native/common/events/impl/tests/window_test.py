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
            'x': -8772755534804786612,
            'y': -2587708940243071834,
            'width': -7553851532397778366,
            'height': 5684250680709180895,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': 2221380968565496678,

            'y': 8194021148811209634,

            'width': 4323303124229109077,

            'height': -143586936311629942,

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
            'key': '˽ҺɞńұɲʹˉΠBùʇăɻȨЅ˹ǠРΧȐ΅¯ŽŧǄƥňң;',
            'description': 'éɦƧӁǥ¡ǔō¥ϫЙҐɸһ\x82ӔщЮ\x85˶ӰΟѱʾÆ\x88ƌŕǆӯ',
            'value': 'Ʉʹʩȷέдϗ·ʕʉʐ\x9aÿͳɡБϿãѼѽґШμӊ[óҫǌßƅ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ҳ',

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
            'focus': 5967,
            'parent_id': 'Ϙ\x99ƁΞЪϑГҝ˾Єǎ\u038dʞυƩ\x96ÜɻɌѶʇʘɆˑſƼΉКў¾',
            'location': {
                'x': 994493144905235906,
                'y': 8084461253478827030,
                'width': -7141970234717467593,
                'height': 7371551779130440948,
            },
            'minimized': False,
            'meta': [
                {
                    'key': '\u0382ȆǋԤČʯн˽ȗϸǢϵ®ʀǠĝӭӬÄƩķY˨ѰŭЛZеĽ³',
                    'description': 'ǠəȊÞsĴƀ˔˼ӢґEĹбďåɭɟǃȞɁũмżȩȉÔçɬʿ',
                    'value': 'KġɉǢȾӳĸİρθƬÂʈσӄƎʤϔ˭Ғ˕ćȂӴѫƫϼҳɶG',
                },
                {
                    'key': 'Ι¦ƣӤƎ˦ƇӝĲÕÿƫɌʵƱǷǊ˓ˌǷӭ¢ӹɹŽǋä\u0379Я',
                    'description': 'ЀŎͶćɓŵūɧʯ˟н\x90ҝčŭӗ¾ѳ\x91ҀŰɀȨϓĀʔýƼϟĎ',
                    'value': 'ͿʠŴ҂ĿãęщѲϺÈԐҽđʌɎşǮȃˍԇѓΥʞåUѭэO5',
                },
                {
                    'key': 'ÌӱҞԏǍъӳӸĖţΐl0Çљ',
                    'description': 'ƭϊɷŰȋHĔЯĊĭɩ˴rˬʸӁËĵЮɃϔљ˓E͵ԭœӾc,',
                    'value': 'óˋΩˋƒñ?}цҪɂƌԕЮľԟźŠĀԖҪӘŭ7\x7fȂңʔƝ\x86',
                },
                {
                    'key': 'Ȥqʽ˫ƫȖƻǏȑћȫ҄1ĻɁҘƻϟǬǭӛ\x89ĞŞˤăȪΊ',
                    'description': 'ҸtǸ`sƆѳԇӝˣN\x8dWИϥǡêîɢӿʟοӈÃȜδѩǲŅβ',
                    'value': 'ɿŌŎΠğЎľΦ˱Ъӿ´NʹĜάƯӛ˼ԮDˬПʃɭ͵ͿȚћÇ',
                },
                {
                    'key': 'ǮȰŕӳƷóĥưˈõ',
                    'description': 'ԆԡϤʈԊŅҽǯƓʑ˥ЁÙĴÔȲʟˁʡж\x85Ⱦ˞ŵĘӯіѽΣΩ',
                    'value': 'ФİӮ\x92ӣϡˤː\x96ċӑăƮ*þԭϝÎԋʙƍɏСƺΟŠЍʹϊŹ',
                },
                {
                    'key': 'ҨѦΕʭÚТϗԨǒͲʙӑō҅ː',
                    'description': 'Ӯ˾ΆŹŁɢ±ůѫĥÊ.=NŬӯ\x8bҁͼɿϴ\x8fo˂˚Ђ˺˭ɳΦ',
                    'value': 'ɀ¥ǈϝ6˰ɠӔƣτ2ʌѭǧϔʢƍˁfӱѫė]Ә¬ӜIЮѷȔ',
                },
                {
                    'key': 'Ӽ',
                    'description': 'ѧю4ͱ˛ä]ņ\x99\x89˛oѵӄѶnˬԘԬї҉ÇΤѳɒҞ|ԌԍÂ',
                    'value': 'ϘʨΐӼмќѫϨ]',
                },
                {
                    'key': '˅ȏJϞiʈŪßȧǎŮƻӫÞϫ˳ѝȋϴƪʖȠ˹\xa0ȀØҘ\u0380ƪʕ',
                    'description': 'þҟЁДĥēϳləɽҬШԈſȽ϶ҩԊϵȹ˕˹[ɍǸΔȂʍЎƖ',
                    'value': 'Cķϴ\u0381υǍѨЁʜƹǪϖ˚ǺͶЍгž6đ\x89ʊͱɣɘʩȇ҃҂ɷ',
                },
                {
                    'key': 'Яǎϙ6ĠþʺςԧѩƕбǐÖӻȐȳƿĩMϐ\x8eƊĢœˈūʡ˟ǡ',
                    'description': 'ГφљΉAӱˏɩɠыԁɠÐůχĲчςéʪ9Ʀ҃ÊųýʮȹƗŋ',
                    'value': 'àϦʀ˟ɵőԮ\x88Ǚ,άфʸЎȒ҇Ȍǟ§ϘϚ˅õƧӖĹЗ¡Щϵ',
                },
                {
                    'key': 'ѼϞ\u0382˫vҺʖǭϹ',
                    'description': '\x88˪ńӸΣˡƏϧrπǏЁӗȼȢƳҲø£ˀȌϋǕn\x93Ǩ?ŏбȅ',
                    'value': 'ԕǙʒͳԮϻ˃˯ŁAӇu\x99ǰԧpÞәɐϹˮӱA\x85ǁˮϳČОҕ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': False,

            'focus': 3318,

            'location': {
                'x': -2853619405177516277,
                'y': -5617211003846312283,
                'width': -30207743301352687,
                'height': 1120371521002837016,
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
                'active': True,
                'focus': 8075,
                'parent_id': 'ɗȢйӾвȷԧ\x99ԫÏĔÈԩȇцȿȷɀŜ5ϳʱȷźѼǣӉ˜ȚǤ',
                'location': {
                    'x': 8501873908940844301,
                    'y': -6516152240449665270,
                    'width': -8797041974200720099,
                    'height': 1152577386715813413,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ǧРɴ͵IvΚƺȾΠıė',
                            'description': 'ŀãˊшș^ƕñƚ\x92ώ·lͻķԟĞІ\x88ɬǋҐƖɡǓĻƉĈʱԗ',
                            'value': 'Ѐ˼\x95ʕ<ȟÎxˍƧЀǓƦЖ˵Ǭ\x9dŁλǲрīʘ9ίъϏÚ\x83ӣ',
                        },
                    {
                            'key': 'ѫΩѽӋəȣĵĬѽʲбǬδКѠԋ>ӟқõΒŢùȘ\x9cż\x94¤',
                            'description': '΄уԐɫάҵĝӉԛ\u03a2ǓȅιɜɢϰϪҺҮƜɌƀϠЙ§ć˳Ȧ\u03a2ԑ',
                            'value': 'Ȧɖ˅SíǭZˁʈѺʻŧ\x99οʔҚŁє҃\x98ϓӥҹζ϶ԭ½˛Þť',
                        },
                    {
                            'key': 'I|˸ŴР=ƘԇͰй˯ƨ˽',
                            'description': 'ИДǴӈӾ\x9cǯԀάǫʂǚƼƨǑΊўŜͽ\x9eǫʛƳȒˉͺOÃԨħ',
                            'value': 'ƃѾ˴ƙº\x90ĠԗŜ\x83ÃƎƄȶƀu\u0381Ɔ?Ýɿr´ӬùɵҲҿԙa',
                        },
                    {
                            'key': 'iyŊŴ%ххŴˡϳòϟ',
                            'description': 'ρŸҦIўǒĴȊŕ%ҡʠDθАØĿkƙ¹ˡҍьoԉ\x9fĝɼԪѲ',
                            'value': 'ńђˀ®ΒЋ˺ȵƂ˳ѦāђѯȈȍʏĳĹΐɁͷЗÆҪӂǏȒpˌ',
                        },
                    {
                            'key': 'ĹѻδŒϫƔиąұèӌϮȿɯѻϩќԉӴ9µҥλӎɾԏǥʾŐѱ',
                            'description': 'ƞ˶ÛȀň\x9aԊ˳ÙӂźŽȥ҅ӰҁĞƌϏ\x87ͻ˧ĒΚЬǯԙǥÈЇ',
                            'value': 'ɗ\x84Юþ˰ǹÝζȬхFǕ\x8dҪMʹԞoЦɵǈ\x8aԮCǅƺӠѥʾϹ',
                        },
                    {
                            'key': 'ĳ',
                            'description': 'Τ\x83@\u0378ϪЙƭҌǼнh˛ǿiäГēŬҶƒȗÙǠĿԊҳɽǻҁï',
                            'value': 'Ͳ˞ƶї\x91ɲӓ\x95ťƏѕʞЁкž˅¦ƬZG\x91ϥʦ˞',
                        },
                    {
                            'key': 'ˬěġƚȸα°˷\x80˂ď',
                            'description': 'JзfƂ϶>жӄΕ\x97\x8cΖɲϥYϣѕɩν\x8eӽģëʔȶҒϫȱńƅ',
                            'value': '\u0380ǜFv§ʡԈ`ϞĄȗŤӘʇGƩҋԞȁ:EGӚņ¹\\ʤÂЄҺ',
                        },
                    {
                            'key': 'ϡŇˎûҾ˳ǥŷż˶ϗ\x9dʘЋ\x9cҥДЃ\x82Ғ®ьӲҝ΄RǀȕΈХ',
                            'description': 'аɷǊɠЬт˄\u03832ԅҋÂԔΦЌÛЀ˖E˾Ҫʇ{Δ҉ǯʫҍŪϡ',
                            'value': 'Ϧςӛǿĭȧκ˾\xadɈώĚπ\x81πƠœӿǣòһĞƝɽˍ2ЧқӞС',
                        },
                    {
                            'key': 'ȔŁʻZώʱcÉшӦƵɚȪȮϻΗʢѐǖ\x98ʃвϭϸɯЌßλџŪ',
                            'description': 'őРϡΎÝBǳĉͰяң`ϰЫŕӃȤϯ°³ǘϧћ\u0379·пΎčӼǅ',
                            'value': '҃˞¼Ǧ\x82ĮŅԤ\x96ʝΰΐƁѮ\u038b',
                        },
                    {
                            'key': 'ǇЅѯɃǻǝʃɝΛМνʍʨʒ\x9eƕʛþ\x83ʗыʎȡ˕ŮέΎхʑĂ',
                            'description': 'ԑŽɫҮθǫ§ŕΐƏгyѺÅ˾İΠήǵʒǟҗҗθȅϝŉɢϓ\x98',
                            'value': 'ɒĭҗȳɓҿȳÖʉ˕ˑѝԇŢƒԍ˖йѷύ˞Η:ΝϲĪǺήʳĂ',
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
                'focus': 4933,
                'location': {
                    'x': -3585532725913223002,
                    'y': 2198963353546099523,
                    'width': 834410955491721470,
                    'height': -7758186575669442304,
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
            'reason': 'ɅĽĔӞάϻ',
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
            'keyboard_focus': 8631,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keyboard_focus': 7355,

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
            'window_id': '>ĒҹЫҧΥϫ\x89Ŵ·ŃҙͺӸŝ\x99ҀɝѴ¡[ȶԜԕŧΌǹ©ŻĦ',
            'location': {
                'x': -2082729952014238901,
                'y': 507608482648171611,
                'width': 6631034255624344634,
                'height': -5368980853551159939,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ȕѠӆƗӤ',

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
                    'window_id': 'ŠбȱȯθԘǛϣŐѫӈ·ȋ˶Ҭ\x9dȼӱÔĠӊʖ#åҷϤξϻЁџ',
                    'location': {
                            'x': 8887213573642287018,
                            'y': 2429720575779316149,
                            'width': 4606898940673587425,
                            'height': -5203446767911360990,
                        },
                },
                {
                    'window_id': 'ФĨêҚņѶɿΝȭʰȹ˕ĎƀƏΰƨӧϻƴϺŋʐ˓ԂéĝҌΆ>',
                    'location': {
                            'x': -625924857220011499,
                            'y': -6947863804468974270,
                            'width': 33121696503836411,
                            'height': 90368025753972168,
                        },
                },
                {
                    'window_id': 'ơҵĢ*\x84ήʻƬĦȭƾǷ\x9cԙѺǟʯöʢθјӐ@˴Ƥ\x80ӾĔѦĊ',
                    'location': {
                            'x': -3772900507760030054,
                            'y': -7112408846185583171,
                            'width': -7472401992663572399,
                            'height': 1765180071514311519,
                        },
                },
                {
                    'window_id': 'ǅ°ȳλϧЕӮƔʂ\x7f¿ҤҀҲɛ+ŢІӶҞƘƅĒкęҎoбӆĻ',
                    'location': {
                            'x': -3256148928249860214,
                            'y': -2328220374629610245,
                            'width': -8758603716778374937,
                            'height': -7258111304006838691,
                        },
                },
                {
                    'window_id': 'ǌÙæҐԜϷΗϪӅ˪λӔ¤ԥȫРɖH\u0378Ԛȋʪœҷ©\x7fйʉϖà',
                    'location': {
                            'x': -9213374923462198082,
                            'y': 6812472111039082738,
                            'width': -2236700457387490932,
                            'height': -687443800928643503,
                        },
                },
                {
                    'window_id': '¡³ӃǯϊɖІԀÏŹ@ǵ\x9cвơϬ\x950ӡӵӁcʚ˒μĵȵ˂ԙȋ',
                    'location': {
                            'x': -5510505823128357711,
                            'y': -371340086602964435,
                            'width': -4197570867867191773,
                            'height': -1696237977506157472,
                        },
                },
                {
                    'window_id': 'aεǆτɂʬўǨӧƚtɀƭѵγǔ˔Ƅ´~˩ŎӏЈƿ\x9aˏДíȮ',
                    'location': {
                            'x': -5123256105129319567,
                            'y': -8588069187323701421,
                            'width': 8858946789691158167,
                            'height': -8498809415792589285,
                        },
                },
                {
                    'window_id': 'Ìҍԅ\x9cΕӦϖԥȁҭʬɽӜӳɦǀ@ӰԋΌʒĥ°ǥǃʲǵӸѶȡ',
                    'location': {
                            'x': -9086582174598687265,
                            'y': -1865886981190073522,
                            'width': 6275213518646072257,
                            'height': -9043855196283265359,
                        },
                },
                {
                    'window_id': "Ϧ¸˩ȫӥıkӬȕǗɺŦPœ'ҕȒƍϴϪԤʔѡBɅˬĎ^ƽн",
                    'location': {
                            'x': 131186311920540447,
                            'y': 2076226149563607071,
                            'width': 8257721344256191612,
                            'height': 6796096212024948478,
                        },
                },
                {
                    'window_id': 'ʺȲʀҷ¤ъӇӸͿμӛҔϧҗ¹ȠɟˣǐтǅǟԥӛʨˇʈПȯˬ',
                    'location': {
                            'x': 552442698599483442,
                            'y': 532764695368263193,
                            'width': -2371022428514155482,
                            'height': -2403365644182820661,
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
                    'window_id': 'ρΠ°˖ε',
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
                    'key': 'ΛuąгĶã©Ǣʀ',
                    'description': 'ȥˠ\x9fΙҘШӋԭўӃÁǅ§ÿƮHҾBǸ\x94ɮ˥ˬҖCIБϫ;Ӛ',
                    'value': 'Ȏn˰Дʰ\u0383³Ȥȱ΅ëҢЁЦԐ#ҭǯҠǈҜԦƬ(!ƀѶѤɩ\x7f',
                },
                {
                    'key': 'Ιɘ',
                    'description': 'ĉʳԆуʺџɿS˗ҟΕ΄˗×ŸĻ˫GǸ˨ԕRӦ\xad˽Ҷoųêǅ',
                    'value': 'ɾЙƾ҈ƍǺȏϼŘǄϪb\x8cҲǗɻƢĈɎԑóĕ҇ҠÊǭϖȁ4˔',
                },
                {
                    'key': 'ƪЭ\x9cßɞ˧ɇɱЭ˽ǹӟԣˁ>',
                    'description': 'ȠҺѷĬѴʳɃүǶЌ˥ͳЗǑ˔åʼјΌʡʧZøǩƬ\x91Ʋˆʮĩ',
                    'value': '\u0380ɽҿ?ȒǦěƇПАʮbͻʴƵʏϽ\x90ЂʓԔЍɰ]ԃΊԘΦ^ɞ',
                },
                {
                    'key': 'ʸ§міȤγ҃ƅƺȃ',
                    'description': '\xa0ΏΪ˭ũūԇKώʹʦȗӤϒӫѰäѠŇƶδʼЀTɏѫǩśŔ˙',
                    'value': 'Ҏʞİď˪ȄƇƮμΕьМȑʦΙǠ˥jғNŅLʅӱҽċЂԦ9Ƿ',
                },
                {
                    'key': 'ŊüȌͳDԉɓсЗʫ\x8a',
                    'description': 'д¹~˺ϼfϵӮŦғʄĂƦƲǛҴ˸њȿȻΉʹžѓҒСĊʄҳв',
                    'value': 'ƾЈÛөǼЄǏ¨\x8fíʓԑ2ЅӼŕ҅³Ǖчͻ҉Гɗǡϭ·ǀҸǇ',
                },
                {
                    'key': 'ԈԏǙȠŏѤԮέȽɋΪԞŴ¶сѕǓλѯðӁӢ',
                    'description': 'wůĥÆJŭʯµӖCхԦԫXџ\x87ʣͽаѲȖΧɌқҦҬʛȽωҶ',
                    'value': 'ȶɓҝЃҨξȞѡЍ¢Г¬ʫÀʐĿ\x81ϔԬOȏāɊȔĺèƟʏÀȣ',
                },
                {
                    'key': 'єȴȏμΩʹƥȅ¥\u0379Ɋюӓͳƅâ»Ōɢȴĸ¼Ǉ.É\u0380ӑǤВѺ',
                    'description': '<ʻӥЪĥǔɁN1ǇƳ҈ҫ\x9cѲгӼєӚǖȂё\x8dɔˀԅЮ\x82\x81Ƭ',
                    'value': 'ƉɵӤɘÖЄ˂ȥнŐМӑɄȗһΑГÄυӎ˯ŎȥΏĨЖŃԓȕҲ',
                },
                {
                    'key': 'ӄpˎŇƜzȂϿȑІɧҹЩжҝґӇȃ\x9dӈɞѥɏ',
                    'description': '\x85ϝàɉ\x8cRɚIɞԏϐʽԚçҕҒӀϥ(ϞµοӓÞąÞĥȍŁԥ',
                    'value': 'ɸȷȱϠ˓Ŵи˩Э¬¯ϝЃĺčˉŢѻˮǀԏȭăʯóѤЃȴ\x86Ί',
                },
                {
                    'key': 'ѐ˵ϼŦÏΌҩΝҴÑg͵˽åɵĵËцȦ\x90ƾ\x85\x86ʘÍǚҵӮȎӶ',
                    'description': '\x81αģӂĄϪӇŰϕ;ʖjĒԠʊʸƌǕӁΑʐʜȢӕǔѮŧŧđκ',
                    'value': 'ǔÜǀņҗӻԁǍκȟξƧгιñСW¸ǻĭΰζΛԮζr˓ŧΛԏ',
                },
                {
                    'key': 'ǛþHкŕʪцȂǂʹ/ǮɮʳŻg³ƻ½ԇʀШɞԟψϝʛԈΑt',
                    'description': 'ϲŁшʤ$Πщǈ?ţǜԗ˯ϸϘҏǟǥ«ȫӭѴЉ΅ȷ\x99ϯӱӓώ',
                    'value': '˓ӷҗNñςьĹҰRư˖ҕ<\u038b0ǼĉσǁԌưђǒőƳУϞҘу',
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
                    'key': 'ӿɞ',
                    'description': 'Ȝ\x92ǜĦĜǟщʱϛӜËȶł˚г¹мǏŲΐӘïfɬÙ8ȚhΐΑ',
                    'value': 'ԕƘЭɪɱҲЭňäʉÓŲ˂ĨˏϿӴɣNΰԡԛјʯƝϛ˶ǑŲʗ',
                },
                {
                    'key': 'ǨȅмқԍƵǈʷѵƅϩѿԡĀʿƅ·ĝӤKӽĸӔP§һ',
                    'description': 'ɑѱɊ¥àšċɬ·ҢЖƿϊɡƗɶçʛǣѻƷӻŇÜș˟Ȑɓ_Ė',
                    'value': '˩˨ƭͻˉϜǿāˢɝԎƑɒ˽ǲĺƛԑɯҝƳɺ҃;ʗƆǚћ˞ԓ',
                },
                {
                    'key': 'ƞЃӕӷʄӫдӮӧҔŬƓþͷѹɯɝɘŷƥşĆ¥ӥο˚ϋҙӰȂ',
                    'description': 'ǢƯ}ùʨӰˢʜʉƤ^ĴТ$įӄǉŜɋ±ƜгʔͳÜǎċ˜ɉΔ',
                    'value': '˥ǺŰϺůƃҞο¶ŲʙʭќӅƧ˓eЎƪʾİѾ˺ \x94ӄӸΓȁЅ',
                },
                {
                    'key': 'ʋ\x83ǹʬϚȫ\x8aŘәʚƸρҟɓʆ˅\x82ЙÛū˟ӻνNǗϖ\x99şȄĲ',
                    'description': 'ҟcή˺ǂ{UʱіĎоԚі&ąWӅ˱ňҼǙÑӕѼ´СԇŘӘȢ',
                    'value': 'ǆɹҔӼǱӀУӌӥǋԥūӰΉɉҡϿ\x82ʊòҖɴӥӜɽИ|ʔԞз',
                },
                {
                    'key': 'йOѪΈѴŁđԭʞӾРʰԩ¨ϲƯԁԈʀШǔοϞȫLɷļÒѨώ',
                    'description': 'ѐз\x94Тҋ¤ìϖОǪŨŎϜ\u0383Ю!ɩÓ;ϧʓ&ωЫƹϷŤȘ]˵',
                    'value': 'Ϡěӕȉ҉ԫԀӶù\x81ǱҔǽɇŋĂψƤŕӍόʋϥӐɉƸƷ΅Ȝf',
                },
                {
                    'key': 'ѫĽϷÀŲԄʨˢСԉSȊΛȺ²Ж\x92ȳĉĦÿY[Ԕʚ҆ó3ԨĤ',
                    'description': 'ĸCӽԜʯêУƳȣǪƼҺϱҌÆǾӗķҸѾƤԢ¯ϣïƝө¡ҘĔ',
                    'value': 'ҫ?ŵ<(ҠЭČǜȆŭºҥϞӝԐįțĆԐHϟӤΞнǎѶѽҧҧ',
                },
                {
                    'key': '&ͿʛŅɊĠŏķǣȱȉǐˢŅӐҤӆ˯Ǩыћ˴ή£Ƙ!!ƋÿƊ',
                    'description': 'ʥғƏW˟яüɗϽ"ƳǌƠʙǿʷŧäҙÑѷˏŵˉŉѦ\x98ԍā˗',
                    'value': 'ȽȣÊȸҘĊПƈҽÄU\u0382ŭɻȏ¤Ҋ\u0383ǳC҈ɓƧίɮƐʢΈW¸',
                },
                {
                    'key': 'ΘͿƽʯǘӒȞī˰ЮđɫӆϽҏʾPĖȈЍǧ˅ĠƓ\x8dϯŸoǌȳ',
                    'description': "ǒҰƟ¦9ХӑðɵϷεѼ͵Ï˃ġЖ'ʩӼĸ\x85\x97҄úƾ\u038bЮϨå",
                    'value': 'ΰӢЉȋӑÞǂĤҒфӳƬ',
                },
                {
                    'key': '_ɖðȆӒìҌʰŁѐ҄ǱȍώКЙȆѲ®uԀǦɨÇ϶Ӣňgʶ',
                    'description': 'ҫłгηǊʎ\x84ϷäϴαU˸ʽµϮúɼʴ8ŊŢΝΐƏƽĔǇŪԘ',
                    'value': 'к=ēЅӣƣƣϼȗѡКȹd҅ŞѰɡѮ;\u038bPԀͽȘǗŝƐϽǃԄ',
                },
                {
                    'key': 'ЪԂ\x8aӡĺƉәĞZЛҶȐȵ˯±Ç˪ƒϏ˯ˢΰ',
                    'description': 'ŊƼʳ\u0381ңҺȋѐ)ӝɟɄлŚԠϻѕ\x87ȏϯЈĪæҶ¶ǛӭæϺȜ',
                    'value': 'Ӡ\u0381ѬϾϻШϢȷ\x9dĶĸӬ҄ǝӪˇԐҐϱȠ˻ǭԝəŲ¾ţԢĄь',
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
            'window_id': 'ȴƝӁЄѢʠΎ˪ƭРɉӁ²ϬͰʰĆʱ¹ŉΡсβүŬŪѧ\u038dŐѾ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'cϽҒ{Ҵ',

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
                    'window_id': '˘Ϸ,ϭ\xa0ɶʱΆÃ˥əƜʻ·ӿƄ҆\x8bƹ˄ϛɛ4ÏԆơƝĭјˑ',
                },
                {
                    'window_id': 'ˋΘРĔ\x80ҟ¶ŶÆĢϜщƢƺʐƗԈƢƆɔˢȹЫġƌɋѿęƆƵ',
                },
                {
                    'window_id': 'őjӎɺōƒȹӖEkԃǹͿѴĉÞϰѾѥϤĿƠҘӳòƽʕʃΈ.',
                },
                {
                    'window_id': 'ȤЎͷωśӒɬЖĭǮŜǝſɟ¤dԐtĝȃɖѕȠϨԀɰԎ}ĶΓ',
                },
                {
                    'window_id': 'ĿĶӀ˘ǝΪÿÁ<ҽOþƴӇΡǈΟİǑĔѢȄɅʥƵнӸΠŕƿ',
                },
                {
                    'window_id': '˺ФʩʅЯϕҀӢY·XӶXѯcѥлȭȔŖı˚¾ƾԧԚǲ\u0378žÈ',
                },
                {
                    'window_id': "¿ʢȽȋÕ\u03a2ƆʓϢȘӤ½ʡǸqĈωӢăÎȚƘԌȨ'ÌѡĿØƋ",
                },
                {
                    'window_id': 'ϢŉĆņæRżçʓùɘǴ,m2ǃˊ˜Ɖԛ°ҕˎ҉Ǻʦ΅±Ȼȯ',
                },
                {
                    'window_id': 'ˍɬʈѯ˸ЮǙΨƁĂǾĶƬθƕђɧŐˎҬʷĩəƴЗȈͺҕ¬ϸ',
                },
                {
                    'window_id': 'ȿĻн5Ǵ\x9cӰûWȇӶΊRȹüȉȒ˛bĬΧȂŅіԉӎȐЪƒҚ',
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
                'ȄжӝÍčЋҸȳǆĻБ+цǄ¡ʄϐǭҦȩϋһԑЅҫAūVεʢ',
                '˯˷ϣ˳ӺЮӔηŕѶŁԁÔʴǤҞͽÂ˅EÒҭʾǗ\x9bӛȊӱſ\x86',
                'ƞɳҩͱѪȩƚˤ\x9bҘфƧʒέɄǊƩΖ«őӠԫѣz\u0383÷Ҏʹҩ°',
                'ʎԘ\x8eѨƊ˃7ñԑǋўĈ˘ÇȑͲѽ\u0383Ҹϊʥèƒ2ĜʵЋȾӤŌ',
                '7ħϦʐͳBľƂȝȿԪǻүĶҺѥҷ*ҍŷц*ɺĘΥъǂ˼ƐĨ',
                'ұҁӊŘ(ґщċȰʮśƥйɇҀћȵĬ(ѫðĤϤ÷ϱϿѾʅϋϒ',
                'ԑҰ\x98ǉʧɀďИɖTȶƀđʮИ³ŽʫϢŷͳДҠτėˤѿвњɤ',
                'ǂσӎҡ˅ʴýӚфŚԑˊΤʆЇfέ\x81Ů\x84ΑǥſЀƊ$Řĵеԛ',
                'Ȅ#ϝʶςԩƈыʃГɎ7ӦӢǯιsʞˀΟŘȦɇӛŌǍȧɿ\x86ж',
                'ѦȐċȉǄġԟǔЉɬ˂Ӱī.ŧҌɋQҡêȱӹ¸˗Ǚ΅ȥƌȁȖ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'kΉ@ƫҿ',
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
                'focus': 1307,
                'parent_id': 'Ő͵ǄǨʌ˙¸@ң£ǶϽȷúªèűҡѠНM\x8bÃǟğʞ\x93˶lX',
                'location': {
                    'x': -150815330273012927,
                    'y': -5640443018440322090,
                    'width': -1325851680000532500,
                    'height': 5921057796291334342,
                },
                'minimized': False,
                'meta': [
                    {
                            'key': 'Ɇʄɫśԓ',
                            'description': 'ѨӟŸΪϴɣȬȒηT\x9fåФŜʉƛʤԃжʮŖϹɱøОѝԁҿʮ\x9e',
                            'value': 'ǗчԢѿƬ\x90ǡӠыӶŹп˯œӒzпAUэίȓōñοëʖˎǶϳ',
                        },
                    {
                            'key': 'ɌЦ˞ƝáÆҥÿvơԅɣΝǢˆèıԈʜ˹ʝńżόĨɽ',
                            'description': '\x84чЫΐйʛͰԔǳлУĲҡ\x90ôƅȿԈѻЏӔ÷ӤΦĹmѾ\x8bзɻ',
                            'value': 'ϐжιӤ˧ǪЦ\x89ȷÑѫŐϳгfΖгʅԤѣĪўôWԁ±ҹǱmɠ',
                        },
                    {
                            'key': 'ΥʜʜЯƒǊϩɏЙʙȘ˯ѣБʾýȼϮ˦ЖpЌ',
                            'description': 'ƯӖ\u038bƍ´ʵӝӂȘŷûТ˧ΦϾ¥ˑʩѷԆɾϜpϚѸƑǴýӰЃ',
                            'value': 'ɏψŋ%өĠ҆ϣƦ΅ʸʃǆ˚»ϢԬ\x87ӫːŪĿŀͷÕҵʾɂӗā',
                        },
                    {
                            'key': 'ȤÐ²ǹ´˷˫˵ʂЦ˔\u03a2Ҭɻɿ',
                            'description': 'ʇҼǲʙ÷élϯԮǡЌOcƧЦ΄θɎϸļʌƿʿȈʤŁ\x9dǚкƫ',
                            'value': 'ž7ɗãˈԌà ԝΖˎʉȯǫ«ԤͲmхʖĀɉӄϝɒǤǀΓȯϛ',
                        },
                    {
                            'key': 'ȉŶȎ',
                            'description': '\u038dśӸˇǕŝʽkԒVŰӱɷѠzπ˓ԡѪŵĄѯ˶ЦŨ0]ʁĐ˥',
                            'value': 'Ŏʺ҅©øƃś',
                        },
                    {
                            'key': 'ɶƱɂҬԠYʺ˴ŲǄȋԦςԄœȢ?ʺğ\u0378ƈÏ}ԩʁµӁɕŻƕ',
                            'description': 'ҒԭǲÁрԍʲϐδ\u038dȝӢȥԌ;ƍw˩Νģȱŧɹű҅Ǡûp҂˽',
                            'value': 'ΉÙЕÍQЈԨŔԮ\x8diȿbûŨɄnДǯӹѐȖяʢΘâҪБӍʫ',
                        },
                    {
                            'key': 'В\x8fŪǘƋϤӣԣԂG҈ԦϻӳüԔɯ͵íϣȾȐǂ\x8fΧӗbɐʖQ',
                            'description': '\x96ˇǜңԣþȝ\u038dеӟλ˥Ƅ\x9fϬОШϣҨпÒёɨĠȕɿѾϤɎɸ',
                            'value': 'âκѝŴ¶ҭɶǸϿɴΕĜϖѲ˓\x83тŻʖжȟҕˑƌ\x84ˀΜğԄ\u0380',
                        },
                    {
                            'key': 'xäxɁȢѳɐʂʰϕЕŰΘļĠɟľϒ\u03a2ƞϏϝʜN',
                            'description': 'µϝаƱԮǳǟˡñȝϗϬԛΑ˳ɼ҃ʄԞƐɴƲƈаªŤȶǤȈĭ',
                            'value': 'оu\u0381ƫ¤¤ɈȰȇԬŴōӺȯԭǀ҆ĨŁʫˉѫӾԇɑƵӀҏȗ£',
                        },
                    {
                            'key': '˺҂ӕѶȱӵƢ˚ǟŞÈіƗЕƏԖӸͻϷġԞʩ˵˨ϓҧ΅xĽƳ',
                            'description': 'ưҗɩΧ\x81ªʐï҄\x85Ҟĩ˴ҔȷѿČǢͼŏƫűʚrǱӤʾ%ɤʣ',
                            'value': 'ʙzƟʊνīҙʖÜNPLҎĉÜќэǱʟиЪ÷RѭɥʿӴ\xa0Ŀά',
                        },
                    {
                            'key': 'цϠʯѸʒÉӠSŤéSÝԒªρV9ʮ©ØԪưѦμ²ʪӭıċʋ',
                            'description': 'İĻɒġŅêԥȻ÷ʉΖӇþЉɚÒєʹľÜŅ_ϔĚΫPȮέ˰¡',
                            'value': 'ѫʾяɯÕɖLїӨɪżӽØ\u03a2Эѵ˾ɥԥ`ÆɃҢӴGƧͽƄҫ˅',
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
                'focus': 4230,
                'location': {
                    'x': -4434385989303099731,
                    'y': 7737794048150027942,
                    'width': 9079167715579328796,
                    'height': 9172415813737006337,
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
                    'key': '>\x82ɓrķǴҲÐԭѠ0ҊӭϰӗρԞΝĄæɈьǵožģ҉ԧǿУ',
                    'description': 'ԌьǮѝɢӫʆčÖģмψǕʦҎȿǀԤŹ¢ȵЛЃиÊϔÓʗҴ¼',
                    'value': 'ύ|ǸöØяŋòғĠÃҥҫįеGƣƆƓ\\ǫӿõа͵ӗѮҞ\x82ʽ',
                },
                {
                    'key': '\x8dЂ',
                    'description': 'ϾűȝĔӼù\x86ŪOýšӜŴʐÞɡƌʏԕƔĊ9ԫ\u03a2ˉǽӹƎě\u0380',
                    'value': 'ӡũ}Ȇɡσ˧¯ԁϠˋ93ԭӆÂүȁ`҂űӕƍýɋӭʰǨ\u038dρ',
                },
                {
                    'key': '\x95ҦŔ\x8aʿʒƯəSħǹ҆èҲ~K˻ӎȊȖɵѰƩÁ',
                    'description': 'χҁЋĂʣƿϚǢÚ\x88ńǖĺĿʫԗҙϓМә\x9f\x97ƚÖЖ˓ɞӝηɷ',
                    'value': 'LӿJƑÙƚѩѤlļCѰаȴѳѡë\u0380ȪȝêÌӺȿԡćƀϘlϿ',
                },
                {
                    'key': 'ʏҭĪƩȃŅӏѕSʞ',
                    'description': 'ԥļєӁԂäΔ\x85ˉÇϚ\x93¿îʯʖҿɞ¦ɳӎԗÕҎƕҥʵͰéѨ',
                    'value': 'Ҕ[¡ˍƙöҎӑǊ\u0382ƆѨFȸȁƹԒԍȒȉϝ˱÷ʢ˳ҰdØѱӺ',
                },
                {
                    'key': 'ҐǌŉÕԣ΅ӄʽϚςϋОϨң|ӅĻҙЙɗˆҁЃǌǸНΦİU\xa0',
                    'description': 'ėћ*ʧϘǏƄԘЉ·ʿѧhĸÁʯӤȖʆưȏřRǐȒʶΠľ+Ǚ',
                    'value': 'ʬþӟѡƴ+їMϑЇНΕXѺƙЊɤыӫǎx*Ͼ\x8dʕùƃ˞књ',
                },
                {
                    'key': '[ӌ\x94Ʊ\x8eŚǘƒķʸ˞ДԍәņŐSƧǬʎЕӚģ˒˓«',
                    'description': 'ИŷʇЕʰǤ;ǨЕǤӣQѕҴ¼ȝ\xadɑǘĿúɼҗȕƵƹѧͱĞУ',
                    'value': 'õțŏÆeѠƃΦɛъëƛɎ\x9cĶʫʜƂ΅vзӡȹ4ӬпҼÚɶ\u0380',
                },
                {
                    'key': 'ԬΥʧÃϦƒ9ӊΞԉӲӶʏԁȾ\x86ʼξ',
                    'description': 'ɀӡ˯jԑǕƍҢѭƼЬɠҚȜξљʓƵʱΌȅQĸþӘ¶ʻ˦ɯѥ',
                    'value': 'Ԥäϝƫţ˥ˎǪœàƆȑȄŞӓуˁԉҊӍǦƐfűŧǰt°Ȼ˳',
                },
                {
                    'key': '˙ÓȹŶʹПȄҏ\u038d϶˰ƄĆԍȝϻЖџҨѬɝêbћУ',
                    'description': 'ʏÇęǷíϼˢɛӻҵЗ)ɩƬЈҊǏƗ¸ˁҬũ҇Ћ÷ӦЋўāǝ',
                    'value': 'ԌЊʚǚWͰӕǗΥ\u0380=pȯ@Ψǖґƀϭ\x92ϵĳCϕbԆΆƢнʶ',
                },
                {
                    'key': 'ʐȔˤ?ћ',
                    'description': 'ѷȡˬқӈʯǪπˇӴҊɩɂύΐ~LǐѸҖ¶/ϛĥǇɐгƅΉҡ',
                    'value': 'ҠОұІĕżҖϚɧ\x95үãđьшЋЌűҤȧÙǙƧ/ȨRƦÕĸ6',
                },
                {
                    'key': 'κӰǙыŗ˳ȒÒиΆˎӰЦɽȉϱÉþөԛӶжɥύʓɦɰ9μ',
                    'description': ')Ǿ˅҄щʠʩƁʩΘúөėǔ[ϳ\x86ͼѣĂϼϘŠІ\x87ȊдóʚҘ',
                    'value': 'ɚМҬέǐҝӥʹѸùǩιY\x9dǃҮһǒǵҐϯϱѷπsЀѸԁŁϗ',
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
