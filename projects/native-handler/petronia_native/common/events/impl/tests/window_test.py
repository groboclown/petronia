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
            'x': 1461844835057868129,
            'y': 2358191833823024470,
            'width': -8897580047200545744,
            'height': -283938783887144605,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': -7675687569122056759,

            'y': 141305311280339316,

            'width': 1326576604128708216,

            'height': -6956842224005978113,

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
            'key': 'ɁÔƝρԪRğψȺɦŽȷϓй',
            'description': '\u038bҟǪЏáΑǽОӲǵŘˡŲԧEҺ_ɶҎÇźɈȾĝјlɁξxЧ',
            'value': ';Ӓȇȍıԕϳ¦Љɕ˺tȢχϜǟ3fҀԆ]Łģ\x82ÈΊƁƫǝƟ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ʻ',

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
            'focus': 2740,
            'parent_id': 'ВġðAʬüѓʿŞwь\x85ўδʢƋīƒǘnϿ«¼\\ǻŨĴȡϔѐ',
            'location': {
                'x': 6663902424407266718,
                'y': 6814419832504699669,
                'width': -7278519952199953209,
                'height': -6719909028442805336,
            },
            'minimized': True,
            'meta': [
                {
                    'key': 'åͶjǔ\u03a2ȮЇιǨӮʪƝбЋϸńŭν,ȍѻɚԣɁÓҳˑ˂˶ʈ',
                    'description': "ŋʚςúсӇ.ȭËϢÁ˰ȓѓѿҶȺƒĪ˭ϻȺҐ\u0378ҷȮ'ɻȐȼ",
                    'value': 'ԀϧҏʮʚðěÜȳȖʱž\u038b]ˁÊҨԤĬFȡǄԔŦԛʱԐǷȅғ',
                },
                {
                    'key': 'ŸʈȝΫӌƘѫƾ\x8cəψāĔĿӺ˨ƒɸ˩ԟҭжԒΡĖʢÔ',
                    'description': '?ǑΧÐӯʛƊÇțѮ2ǰϭʻνώȏψЫĳкĬͿоѱŪʭ˵İђ',
                    'value': 'Ŝœǖǘ˾˲ƀ҃ѩɼϝ˄\\ÀŮò¼ȇĞƈͻȀĹ&·ţɩΝΝК',
                },
                {
                    'key': 'ˠ½ӯɔʢɢҕΙdћέ',
                    'description': 'ģʔ҆мǞnϟƲӚɄ\x90ӶǸƭ˙Ϣξȣ4ͺˑɟӹƾǥļŝϿŅë',
                    'value': 'ơбɒӭȨ˫Ҋ˷\x9dϯҦΛʥǎΓɇȖǵϤҹЃÒѰȊǚӚJSʧҽ',
                },
                {
                    'key': 'ƱωҳԡʑWȐáĪѻԪɆΓȈɍɟǪƓєġԊ',
                    'description': 'Ş\u0378ŀђӋʧƄԄ˩ΔӐҜ\u0382ǼʞңϲǲơӾ"ǵǻ²ϗʞz΄ʣȌ',
                    'value': 'ʕ\x83/Ф˭wơ˓ҋƎЬԒ˼ÙƎÎͽ˺ˣŲǑÔɹɘɣφт\x8e|ƺ',
                },
                {
                    'key': 'ƛгĢǿĨҥ\u03a2ӑӤ˙˂Ƽ¨¬ƚƤтʓbҠɡμҭƐϷǡņˇ',
                    'description': 'ϦɆԖÀ·ʡȩ=\u0381˷ΊϳԦŝƵҎTЅɣ®Š\x7fӿƈƊѹќϢÛǑ',
                    'value': 'ϑʊŠ҄ŴΗɖԃθʜΊʬԫΕ\u0378Ҭǂ˥$ђĴȐ½´[ÂaΧЀç',
                },
                {
                    'key': '˕EΈϴčҒѷ*ԧĿƜӫЮ¡\x88ѝϕҭˋƢˤ\xa0҇ҵө',
                    'description': 'Ҫ°ӖjİѲ\u0380Ǭĵɫ)ÃҴŴϚϓ,ХԫȟԏЃʌǌиŚ\x85èÇǕ',
                    'value': 'ȳѝк³ħӼĲӅЕɒəϋяʵʿRҴЪϦϲ˖ˌșԊ˯ҥˎƋɀǏ',
                },
                {
                    'key': 'Ϭ\x8c',
                    'description': "ʦћƻЎБΕԠɈÁԖœƿӭŎȞʞԚӆӉ'{ƝЎӀ҇°\x85\\Ӓǂ",
                    'value': 'ĆΦӹѪͳӺɾƻǠʎƹŖʘîӎĸų?Ŋκ4ҫþĩſȬΰıϞџ',
                },
                {
                    'key': 'ƇʃÂϴӁ\x94ǣΦɤğ˔ғϫϖ0ίѽӧ\x80ŠƉ³ś®YŲԥɘќO',
                    'description': 'ŲӷɲǃЫӊĽ\x81É˃ł\u0378ǧŰ¨\x89ˇͽѺç\x9eɖŴi\x89\x92\x835ŉҔ',
                    'value': '˭ǝĒʹѭͺˍҜő.ҝÕ\x8dʵǧΠӭȖʪαýȐ˫ʧƙɆѫӴʈB',
                },
                {
                    'key': 'ð\x94´ɠ¥Β·ȪʽƠӒˇ^ǪʟИˀ¿şˑ˛Đ҇Ǵǀ;ǸʃƲЅ',
                    'description': 'ӄΘÁӎϺҦ\x98[ОРʅoʻоɶԭӿˇȻ¿҅ȦʀҁҀƶƅǆέŔ',
                    'value': 'Ԏʰ7ʝȫӍԐοřĺˉ͵єʧЁȅǇ˝Qǽʛ˻ȼӿ˳ŚҰ3Ŝy',
                },
                {
                    'key': 'ÄԊTˢήҪ',
                    'description': '͵ġÊgӞͼԦҵĂɕҾĬԔʼʜyǥЬԣ5ļѲғ~ýБϓÒZ϶',
                    'value': 'OбˏĴęɼΥғŕ˧ӢѯˠįҍҔʳŮю6ҙǟ®ē҆hѥŁͲє',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': False,

            'focus': 2699,

            'location': {
                'x': -1812691372122469996,
                'y': 2786480920208359099,
                'width': 8501234458987401238,
                'height': 7113770894370071410,
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
                'focus': 1683,
                'parent_id': 'āʍˀѻΨɚ҄ТͶҽԒ3ȍŞɓcú΄ςγĎӘǹčƢҐŮƖǨ¾',
                'location': {
                    'x': 2297735527803260665,
                    'y': 4310060181519919536,
                    'width': -7487652723529147239,
                    'height': -5598565847203317494,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ŠʔҠӏɺ\x9bĳӏkҬԖЏdӈÒWŇ\x8dCˋϠϜ˯Ӻ',
                            'description': '¸ŋѱÇм˶XŜӨϑŔɄЂҥSыͺȽĻçͲÙκͳԟÌƟȐԖϿ',
                            'value': 'ƭɣnđd¹ѧŽ˪˨Ƞț\x95îԞĈΜȒϺӜͿȅӤɞОˁ\x97ǆӅӇ',
                        },
                    {
                            'key': 'ϏƣΟƒĚӅѤϒȋϜ;Ӥ\x8fӤӝƯӃѴ¯ȳĶȒ\u0378ϑϑ!ɤҵʔɑ',
                            'description': '-ɴ©0øӛ®ęӏТŮƎʍϭϣ\x8dƯÌƅЮÕxї\x94Є˫ӼѫԘԦ',
                            'value': 'ƈɬԖԖѶԑæΗ®ʳИƓ\u0378ʹȂ²xǳȖӓ\x91ΕȲƵƧÃHʱҝΦ',
                        },
                    {
                            'key': 'ȗƙͺȏzmΘ\u038d\x9bїˬɤҰʔ˾ĤǳɣͽÕԌΨƇϕ',
                            'description': 'γ\x83ҧχɭəŠþźȝȠ%ĊzËͻĶӕŸчǁүǞƈҦÄȬϟˋæ',
                            'value': "'ˮˎАɼɧKѦŝ{ĜѤƑŦҽάΟѹ˅É£ҽѶÌǖɉ#ԞЋ˞",
                        },
                    {
                            'key': 'ҐıҪΖ\x9aɷӆ¼ҟÞƀjЭƍȰɹƍ¥Ϣ)ԏΒʎ.',
                            'description': 'Ғ˳ȐҭМËƏϏӦß;ΜҁӽôПŬүї4ӮжūЀѣȒ@Ň\u0378ȇ',
                            'value': 'Ϗ˗ɭϒԪԬΆΉѷȨ»ƪÛ"ÈҖ!ϹȂ˝ѣ×èиɏ˥\u0382Ў*ь',
                        },
                    {
                            'key': '·өʾ˧tuˬĖØЙ˸Ӂá`еΥ',
                            'description': 'ΖύҖʢìӫΙАŖˊЗʂΗú˰ԥΥ΅ƠёǄpː\x8e8ңŤȬсÆ',
                            'value': '\xa0ʈЮšёѰɥϿτɹќvǣ£UӪ\u0380Ϩ\x8d҄ϞƛZϊ\x9fȑƖȽϯҷ',
                        },
                    {
                            'key': 'ȫұюӌƻ',
                            'description': 'ЮʨʈъȏŲˎpѣ\x80жѿʦƳҦί˂ʯ1Ԅф\x95¼dVэčщ˲Ɉ',
                            'value': '˕ӾǣԢϦкӀҎ?ȬáɳìɏƤЁǌ\x9ccvɮХéΗ\x82ӎѮξ˜Ͷ',
                        },
                    {
                            'key': '7ɝě=ГДĤɫыǢƱнŇ϶űɩЄћjзԄń',
                            'description': 'ǀǣӂьjӸР\x80ȪoǙbÑlΈǤϽŞʜιѶԐʡǁń¶ӂǥ΄Ǽ',
                            'value': 'ΈǸëƆˠƢĝѩϬzŬĠϱʸҦЦӤҩҼȯʋ6ԈғЧψȖķǁƴ',
                        },
                    {
                            'key': 'ÜъѨӨo*ƄˈŋƂΰ˭ӇÍеˤ',
                            'description': 'ΖȏʘˋҹȔőǟҒͿĞψʢCѪƙƠЉ˱ķ/ź³ɻЍŻĉ\x9fǒʮ',
                            'value': 'ӑˎ5 ÀƤΊӎɜӥ{SЉδϙŃİ5ēȁΆśż÷ѩĮУБÕʹ',
                        },
                    {
                            'key': 'ȐÉҿ\x9b5À҄ÝMŪфýҺ\x87ÂȱĕφT®Љ>ŲЀǇhԑӿx',
                            'description': 'ӂ\x9e\x7fѡҹǷȒԟĿďέϾԇ2\\ʶȇßGg\u0382ĽӤʼЂˢБʷϋу',
                            'value': '\x8fØϗʽНңу×ʊΆŘзǯ\x8dǻ¨ĺЈúʹξA\x9b\x89æ¦˟ǊБп',
                        },
                    {
                            'key': 'lӫљlЋтǚKʣҍΓŒKԞrƝΧNЌʵ',
                            'description': 'ďñӚҪͼcéĠԘ\x9bӿѽ]ҹҹNʑ\x9b˸>Ӎó}ԪϙӣӃǵє˕',
                            'value': 'μŠӪιӔǭΐҧțʅǙѭ˕ššҝϯȮӔϚ\x8eŏɽ˂ŭИ\x98ˤ϶]',
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
                'focus': 8640,
                'location': {
                    'x': -2110573464137238984,
                    'y': -8226119243650510487,
                    'width': 7286967383683834883,
                    'height': -7441785817048134165,
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
            'reason': 'ɗӭΖęεʂдʨɬȜĆQƄԫŕ˥ɂīΨϪѡщӾͷ;ȚƯҹӊΦ',
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
            'keyboard_focus': 8341,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keyboard_focus': 4156,

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
            'window_id': 'Ȓň˖Ȋ\x9fȡ\x9eöӆʛӲӓEġáɏєĴҩѺʑӋǺҍȻяćǢԍǋ',
            'location': {
                'x': 955270538465605989,
                'y': -3078236367963938859,
                'width': -3015974585626873385,
                'height': -6754304729417764797,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ʓԭǭgх',

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
                    'window_id': 'ԥŖaԌǉnóǎ\x84ªȒ\x9fǱθϾƜǽ˦ɥԁǒˬ\x7fʸȦԘžȄͿҧ',
                    'location': {
                            'x': -5635126601620257748,
                            'y': -2327028236608816778,
                            'width': 9004986989585031515,
                            'height': -1564737496137798290,
                        },
                },
                {
                    'window_id': 'ԆÝ˼Ə4ȬфȘ\x91ɀηxψĐĻԪȾјFǏɛԁǱτơҥДǥЉɦ',
                    'location': {
                            'x': -64263166352788601,
                            'y': 3943075211610107173,
                            'width': -7845220865148784698,
                            'height': -3738737155060296303,
                        },
                },
                {
                    'window_id': 'ǹɇŞȑˁ,ɤѵӊΑˢɧƏϾȮ϶ĲӂӾбȸϳϏǵ,ƀŦƟƞµ',
                    'location': {
                            'x': 5155384420197490720,
                            'y': 915230116627794368,
                            'width': 8380292770237921177,
                            'height': 4657306076307911594,
                        },
                },
                {
                    'window_id': 'ŝЀѷӞЬʧϛ^ҍдƉaɵԃŃкȐƍǛȍǡÉзlxšϻɏäƬ',
                    'location': {
                            'x': 1840856385254607301,
                            'y': 4042787011726449219,
                            'width': 5225250129843804244,
                            'height': -1118780899091662768,
                        },
                },
                {
                    'window_id': 'Œʍbȳ.ȱvŅˢȋ@ҜѬaJěӰаŵ\xadю$өŨ&ƳƏҸ§λ',
                    'location': {
                            'x': -2332902404791443902,
                            'y': -5026051382596624409,
                            'width': -6844308657918592020,
                            'height': -8133598202939548896,
                        },
                },
                {
                    'window_id': '˥ġцr8ǒƃˎƳZΧφЋƍª˾âӈΕӂřʛѷӚѬƃϝјԘǏ',
                    'location': {
                            'x': -3739207001606885021,
                            'y': -3212545078208047907,
                            'width': 5819301636598559437,
                            'height': 4830845323125982872,
                        },
                },
                {
                    'window_id': '˅\u0381ѶҟɰҼͰÓ˻ЏϖǾǖʧʣ]˜ҠǎӎɢɦSҗѽǳϚɵϝʓ',
                    'location': {
                            'x': 1189822881418046242,
                            'y': -263553669796990508,
                            'width': 2721872598571358181,
                            'height': 7026538809560683951,
                        },
                },
                {
                    'window_id': 'ǣƪ\x9fѓȚԚɲˌƘŦͰψʗȪϞϘЌҵ˴ѵșӻӱѓʸĜɝÜδǺ',
                    'location': {
                            'x': -6136818292368021867,
                            'y': 1189701650815055754,
                            'width': 8611446044263592862,
                            'height': -5718216012659880833,
                        },
                },
                {
                    'window_id': 'ʻËɒʬұòƳǔǸѢӫЮ\u0383ƸÔҦƵűÉѥϪǒԈҮθӧ˻ԁȍɌ',
                    'location': {
                            'x': 7072668119382596096,
                            'y': -807569974390411118,
                            'width': 8145347101765823897,
                            'height': 2512280847869504024,
                        },
                },
                {
                    'window_id': 'żӅРϮȍлȶрʲшǝƾζ\x89ƮǘZ\xadʐʙƞͳқϧʨȋЈҟԅľ',
                    'location': {
                            'x': 6961050699681344405,
                            'y': -3797484394357889334,
                            'width': 7270114654892939811,
                            'height': -6607450382699701892,
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
                    'window_id': 'ϛÂŲϡʋ',
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
                    'key': '4ɫδŬǇʭ1',
                    'description': "ԟȘĪӴһǦˈǖȂÈ'ɂϠӐ\x96ǰѷӶΥ˧ϗ«ÛϣͰɗԒ˾яɊ",
                    'value': 'ɡǂМԧƉȄȴϷʝΎŤđœОϣwƉĀʢӯҐ°ÅȘÀʎə6Ń҈',
                },
                {
                    'key': '1ѓưƁńλǽӂҕÉȦͳØȕ_ȡPԉ¿ǏɡҸǍťȩ\u0380҇ƔêԂ',
                    'description': 'Ȧȷиźқ˂҅¸ρӦϬƼκťKǥЌхȏu˭ť²ěȓȏɲȗЏ@',
                    'value': 'ҤѢįʔϝұԛĤ\x8dΔeФыŁƢͷǀϔӓǡǄїʬɢĀͰЄӺǺƞ',
                },
                {
                    'key': 'ɞɨŰɐʹˤØӲЁȰ҄*ηюπăɒԒʼӫȁĘѴrʛʃҐӨʡA',
                    'description': '%Ӣǥ\x9eƚÆʰ¾ƊpɳɊˑ\x87ʵңЖҌɤţŏŗûŎ¿ɒ5ΩԌǂ',
                    'value': 'Ѽ9αǰԒ\x8eҐԙìû҉\x84ΝÈȑˋϻʾ\u0383ʧŮƻş˖ΩͼӼҴӱ!',
                },
                {
                    'key': 'ыĈƭΑĎ˘ʡӉЈʯêԊ҇ņπІЁѝʙǪõǞԓ\x91ӵĮң\\ȓš',
                    'description': 'ԐɺȴҾŃŐԟȪ˚Ȏyʥ|˞ˏɿҾɻĥĀԪΐȬłԭɽPλÐԠ',
                    'value': 'ѸȾӬǄ˖әƥ΄Ɲө˩¹җҘк\x97ϱFǳɦӆчӥȀɜɨєȷï˳',
                },
                {
                    'key': '`^ɾİɘΥ˳ɾÃʏјҮΣΎ¿ЄЇҲҞԡʎɦȀϵʅ5ĊIә\u0380',
                    'description': 'ОӘďɊǐŤΓUЖҢфιϙŗязыҤˉ\u0381ǰµˤΚǵʍǳͶӲΨ',
                    'value': 'ΆԐɠoPϊ˂ӫЂ¶ƨ\u0380ľǄӬԥ{ƀǱӠǣʚԨz˚ƞ\x86ÊʩΠ',
                },
                {
                    'key': "\x89Йˉ'¹њźΙԖɊ˒ǣÈӷƀȓЂӊƊ\x92ǰίÒ\u03a2\u0379ɡʟŻűΧ",
                    'description': 'ΟԥèчǌӢȑʳ.˩а϶лȼ˺ӪĦϤƧƦԫЩƳмɊƏӨГοĢ',
                    'value': 'ΝØͽʻʜ˙ĸőŪбѭͽʮɏӫѤʙ\xadΘʲωǎpˆ\x84\x83Ҟŵňˢ',
                },
                {
                    'key': 'ЛBµʣЯƩҿRОԠ¦_МΦ·ĲΕâ',
                    'description': '³ӟΠӷϮ˝Ώңƶ_À=˔ĊȆҾ£ЭԄԤ¥ÞɌӟ\x8e˫ˊƫΗȒ',
                    'value': 'ιƢҷԓȃѯӱѫϟƠxΥɔǄϢҢЫξWťɅïêǋǵʥϓÉϠȻ',
                },
                {
                    'key': 'ǱѨфϣԩĮʫθŹїżĜ˞ĪɱÈ¤Ο˵ɸΏԘɠγӂЩуԉʜƛ',
                    'description': 'ʹʢȕЩÏ6\x9fˡӫǆ¾pǰп©ʥǊɏԝǢɊԣƥϻʫϪpϏӿƐ',
                    'value': 'ƟƦîϒԡσБƳɰТ\x92ѵŝțӎˑɚȯԟʊԡҙƷϱȽҳѶżýȗ',
                },
                {
                    'key': 'ϽƋȪ',
                    'description': 'ˊ',
                    'value': 'ÕưɐÎԕƾЮŔ\u0379ļӎɾɈǃФϠɾ˂ѿʠԚлɨǍˣËξřɂğ',
                },
                {
                    'key': 'ǟӔϗӗ·ЫƃɲǾĽÃ˚УӒ\u03a2ǌї.\x80ȷžљӤ',
                    'description': 'ǄĺhǡȑҲɁνȺҳZƤΛШҥϢ¸ĥψҭШĉ˯ΪʯιҹЮԔʖ',
                    'value': 'ȋƘǽϷŵϣ+ǩĎьӮȍЦ\x8a;ˊőɓƝÑ\x95ѽĚªΪ\x99δ\u0381$ʊ',
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
                    'key': 'Ȉƾʟǫ',
                    'description': 'ʯ˖ɮЈ\x91ƜυҔȋ҄ÜӿĤҙÔԑƹΚԁɒƘјӝʼǐƅgџӦϺ',
                    'value': 'ЏОйϋΔӆ͵Г*ǭǆѠԈѩǅԝ$Ƴ¹ɹЅϡCλįɼř˽"ӑ',
                },
                {
                    'key': 'ХˇƎ҇ԝԛǔȗԃÍǭǍť\xad>ӋҪpĹЄőȇȞeŇz˃űwƥ',
                    'description': 'ʑΰĈËƩʣǌǄªϪȡηҗǾȡ·˶ƣНѫΫʜǾԣŧΤ҆ӞѪɡ',
                    'value': 'Ƌɼҫ˶ćŘ\x94ȬӜ˝˸ŒιɐΠȢŅìЪƽǎԁ¾ӴЀԨ˃чĜȡ',
                },
                {
                    'key': 'с9<ʊǏʐ6ԁw˟\x9bԛǽůɕ"\x9câÔʄÂȒʥʑЎ%ʵԄāΤ',
                    'description': 'њ˨ǇӱǭƆЅ{Ȗ˙çӅǉѳǫҐΆҴѺБҋ˳ӏƶɄòò¦ҝß',
                    'value': 'àŰѶĄӊş\x8fˁ#Ԫ®˾Tȡʸ˰м҆ΈвğπǳңɳεĴВ\x86х',
                },
                {
                    'key': 'ȿ˗ƥÿν{\x7fǖȚа҈ǄδѴѶ[ɀӭΆҢ~ǉUɁȩǅ;ԀҰŅ',
                    'description': 'πϫӲƿȹҳɕǗRʡćSøȦϩγƇшȄѹӣʪІӐ\u0380ϭÈҭÃ˷',
                    'value': 'ɒΠćǺďӄѝхʥӢá8\x8a·Ƒԓ¬ϑɰɱғӬΨĈĊˣɲȞˬȗ',
                },
                {
                    'key': 'ξƢ4V˙Șŏ\x8eПЫӓďϼůϓşВīӊ˧Ϡ\u0382',
                    'description': 'ǚΉƩƻԮDӀ<ï´˨Ðȡ\xadĚ¶ӪɀǁŦqͶŌʡ҉ҮϸӒīϪ',
                    'value': 'ПМŔӫλʶƜƇłrѾʖƫ\x87ԦƠƀțӛňѹȚі(Ƭѫԍȥ}ő',
                },
                {
                    'key': 'ĪͳϟùĠћŽØŲɂ˖ǃ/ŤӟɮɂưșɢhЪ˱ҒΛңӞЯВи',
                    'description': 'ґӕiÌ-ɞsˈşҜЫ{ȥƀ\x81ƨʚ҂ČřӧϨĤŎϚϵʕƢƱљ',
                    'value': '˩ɴ Ζͷҳ˭èӅύŜæɽӱȿѪɺÛȣ(ЀɎҞƻ!ΙNǫʲŅ',
                },
                {
                    'key': 'ѓ¦Ĺ]Ѹыʳ¦Ԍћʐˊɵԭ͵',
                    'description': '~ʥɘəpŃ˧ȕˮ÷ʧԐɞƟèҏĪӽԄŵÕʪѤϔһȸҎ¢іɁ',
                    'value': 'ʰǇÎƉžРŝȢ?˓ΏȲǟ˅ʩʀĭǏѺӤͳȶԒ9ņÿƏńӽ\u038b',
                },
                {
                    'key': 'МϣÆ˸',
                    'description': 'ʪªЭԝxƿӂ¾NɡͿǸɕĈ\x9cϮ҈ˉԖӪҋ0ƏѣŅЖзѻЀҙ',
                    'value': 'ŌȊȄƚκ˞ɏƧ-ϬҎЕǣIеȽńǱ¯ɊĢ˜˩iQǇǳ_ʺξ',
                },
                {
                    'key': 'с¨ƎčζɲźĝZ4ΧX4',
                    'description': 'ʎĉ΄ɞΏ8ԅgҝɷ#έΜŐȻҳȁџŢ\u0379ųʜγǂüáҏįƒȥ',
                    'value': 'ӲҠ˼Ӣƶиȡ^ƍ˳ÊUÍŮúζƽɭЛҋȰȪӓNƍСʫιʥѼ',
                },
                {
                    'key': 'ҕ˧ϮƲѧѪĺˋѷʚч·˷¶Νĺ\x93Ư2ÝńȧʔǘàʽҟАʃѾ',
                    'description': 'ƳǛ7ŌǶū\x9bԚӖˆȪԁ\x9d\u0381χԢŰѳǶЏhѝњąѿŘ˫\x84ӵʏ',
                    'value': 'ДĺŅƼӃͽϳԎƸΕɯѠƕıþɭ·ԑπМλѝͰBʊɥƪÜ˓ʎ',
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
            'window_id': 'ӉӘƺΰǍóѐӚºҟҽøӃχʁОѸˎǄːǑȆоɕ\x997ȗϠ˻˜',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'қћ\x98АȾ',

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
                    'window_id': 'ʅІţѽҽȭәƉΥӒėƦǥÚѳӥ3ÃŚԐ\x82ıtʎǭ\x92ƭҖҿϻ',
                },
                {
                    'window_id': 'ѐʔΎȈŐʿǘºΨӞǔҟƏъΟ\x9a"ʓӎǨqҁϽў3ӴͰҫϒϐ',
                },
                {
                    'window_id': '»ĬвĭӰĐ:ǉϸЃǒӵОː©Ӟ]ЙǤϳλĞԫ˹ǽϐ~đɱР',
                },
                {
                    'window_id': 'ҌĮȵɰϙχXêǴө˔˙ȯȀŮɲśɧқȄŅϏ\x9dˮ¼Ҷč¦ԉȹ',
                },
                {
                    'window_id': 'δʚˌȢʓɸԜϭŵÖȠ?ӲҝȖZѠү˭ȢҕPʇѹЂŪϊďĢĪ',
                },
                {
                    'window_id': 'κyҊˏǬ2Чƃ|ѳ΄N½ӻȤƞЯɈŖϑΉƔԃxˠňϷϛƟϬ',
                },
                {
                    'window_id': 'θҜLϞǋĭü¯ȢƗ±ϝǐñʎƺǪҋӍhɀǿʑɨȀΥѳèт-',
                },
                {
                    'window_id': 'ɘƙəϰ\x99ɽϰσ»ԩǁϷŀӃʻʍ{ԢȉǲʤǢЗĊӶȚuĭώғ',
                },
                {
                    'window_id': 'ÅͳЭӔ:ѰµϟņɼΣ\u0383άͼōӺЮʻ˃BǉːГϑĔĭԋH1ɣ',
                },
                {
                    'window_id': '\u03a2\x9cȬǓȭƴΈѲIˬѼЋӆ\u038dӴԍŖǗЮҡƨ˰ьɽÇAӤǣӳδ',
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
                'жɱЮԀǎӫɸʑсʇˑѧӅϲ˵Сǝ\x8a\x8fȞ',
                'ą˳ӒĭƝăiϪ\x89ȈȁӎɘİȐȯϬŤ˼«pӼÀǨϻňЏ¸șš',
                '\u0378\x98Dō˒ØȢԣɍɎΫȭƪмâϋɄŀʢ%ʘϖԗӄΠǔ˭ʨʸǠ',
                'ÔӝҁĲӛɂɍ˸ùκѧýÔϴ+ѷ9ͼ4џɢƐяÅƒɒӲ\xad҆q',
                '_*΅κ˒{ҭĘ_ȿԛȿ½ԁӻȱЍǃ@Ơ\x85Çɽ{әҿɀȫBϾ',
                'ƞˤ²ȅ˘ĢÅAЉǗƭӪωΘʾ¡Ѥ½ϨΒǃĚ¿<ɛmͻтƐэ',
                '·ϓ˕Δҡ˘\x9dYʡæ/dƷʹΈÿȔɨ˕ʋʬԗčэτ˅ÍХάî',
                'óӜCĈ®ɍř9@ǡɂϨȃƍΣҷЌѳÞӻƎӘɨǉ˰ԁӷζħƤ',
                'Ĉrâ\x82ҹλƽ^Ǻ\x82ƨǮŐѽΝȠСMчѩȑсľǈɯƲӱ\x9dѕӓ',
                'ɹ˕ԇíǣΛŎɮѦѦċɌʟɻʷʀÌȃɱҾӰƥTɃЖkʬĉȉ¬',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'ҿɅÌ\u038bģ',
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
                'focus': 2397,
                'parent_id': 'pűӁ\x8aʦŃŴƱÒ˅θΥúȁȽǊ\xadԤΐҳŮʁΗǷҙɱǯʳ\x81ӻ',
                'location': {
                    'x': 8601370761860150410,
                    'y': -8405673411586603084,
                    'width': -445351886084292970,
                    'height': -4142853967238413371,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ļ(ϮˇϚβɫ²šéЂӴ˙фƳξ{Ƥc¢ϸҍĵɕӃӼаҗ',
                            'description': 'ɡӍϚǉĨȂʃōǯ#Ȩĝʥтʔ1ԓԡ˼ƷұXΥºʲ΅ПÌȹѕ',
                            'value': '˺ʠȇɂŧтҚϟɠüŇɵ˔ϋƳѮӉȫGӁŖĘѰԡȱsÒЙ\x96ʽ',
                        },
                    {
                            'key': 'ӹ˘ĳԅНƀϩŸ',
                            'description': 'ǒƟ˦ѿ˕ЂŽц˘ĀŲXфǘɼƁԗ*ԭʢψ˧Îȉ\x97кҍǉȟ©',
                            'value': 'Ơ\u038b\x8dΣu?ô,΅ƭŔə\x82BʱȃӓΠPɪƁyӬ/ɱǧԓɆŌӪ',
                        },
                    {
                            'key': 'ȸÇtұʚʱќõĻ˪ƔĉѢǌԦʐɸʑз\x88Ǵň',
                            'description': 'ơРӊʽÇǨЦɝӍƮŘъʆΦˀĐʗ\x84Ⱦ½ӔǙʤȩчŸ2чЩ҉',
                            'value': '$ӎäĕ',
                        },
                    {
                            'key': 'ɃÛȑ"ЀǲɡôɾøķԨƂř«ě˾ёǜ',
                            'description': 'ќѶΠԟɆħɠϑ0ҹȃ\x87ÀɓW\u038b\x96ЈüɉȠϠҐϊЛǹĦ³Ѭ7',
                            'value': 'ӣɍǐ\x9a\x96ҌżƦtΘŊǑĊнǷɲиǍÝ\x91Ҳ8˾çȑΔ_Ǯ҂M',
                        },
                    {
                            'key': 'ɆʚεűƦҸƬŽҤŐɌұƴǽЍ˜ѡͻƳÍȞτǐŐЈԭ',
                            'description': 'ǐӰɾ˴ǎ\x9dԠǶԓρѕʸςӡʡɗљZɛ˛ЗИzҠЈÄ\u038bʵʰϨ',
                            'value': 'ėʓǊБţøÂƢϩ-Ž˨ƼЭΰӋǚÿȃƱуuбΌ;ҔgȘфƱ',
                        },
                    {
                            'key': 'NþѾGҴΒˌФƴƑīůƫŊ˕ġȧĕÂ¨҃ʕļʂ˗ϧȇĖ&ģ',
                            'description': 'ΟêљӤ\x90ӢLoʗъѲҙЉˁԤԢҭԣЃaϨPȈ˜ТЄäхɤ˝',
                            'value': '*Ή˦ˑÁұΥϩƵɕʹЋ"öˤĉƭĨХÜӯ\xadƣʡϜλѣυŇη',
                        },
                    {
                            'key': 'ȲȘɘȺѰ˃Ҹˑʱ˪ɪ',
                            'description': 'ҋөȝϡε4ȆФρ˄ɏќϑƮȼҺΥԁǍɏìϒľԬԮğɰţΎѸ',
                            'value': "˨ɣιƁ'ɳƼӽ\x86ěǡ3Ǉ˴ΖɑюФЬĆѱӠУԏƺř¶ǧċ0",
                        },
                    {
                            'key': 'ƠґǈИϣŏʰҫȿͼμƃѡЭωșƉȳŕ¯ΐţҌ',
                            'description': 'ӖǢчӲѥӿĻƊωƔˬŖˬÞȇſƂǝСŻωԝԪЂΤдϮГɁӗ',
                            'value': 'ʹҺʼŵʊýßˏϫ˸ϳ\u0383ЬĶʡҐȕƛɻӜĎϟʟƩ¤ΖӃγKϒ',
                        },
                    {
                            'key': 'ЉŚ2ЇԡΓʹŲБƇԒτ\u038dăΧ]҃ǁͲɓΉòҔƓӄÆԍʐŃЃ',
                            'description': 'ÅëЁƏÓƿÆ?ͼʟӥԘӯƏЊ÷ΤƧʹťŨ˅ʏŢyʌο\u038bÈҖ',
                            'value': 'ӧq\x99ҏÙˌǇȴПЇӤǵƎɑӜƵǣȁΨɾ<¯ʊhˈ±˹ӛȚø',
                        },
                    {
                            'key': "ȣñ'˘Ƙԫ˂Τūӝ\x90ԉŁӻϦĚǯÕҶĠητҚ",
                            'description': 'ȦԘҀԌăԚΝɳȫжÁɔŽπҚàŁŠВόʎЪѕЈϣģJɿъϝ',
                            'value': '\\ːą˺ʨĕ´Ѥ>ҭ´ƭүƙԐƐҨǚԮʹōyŽδӒƖȸȺóϤ',
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
                'focus': 2996,
                'location': {
                    'x': -8455421699191679536,
                    'y': -1986275440930062100,
                    'width': -851213014954482433,
                    'height': -6505063025946331289,
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
                    'key': '8ͿЈǬšәԠӶ;&ȿ³àçv\x95ȪȎюŷŬԊэҬОѴӎƁϳǧ',
                    'description': 'ʐǪɤŁȯÚЦӔеǃӬѻοӷÃȺƢ˞ήԎϏǪĀԄͷ\x89ɌԖGӁ',
                    'value': 'Îǐωf˚ԓßёƹŞĖˈĽƈȈԟɌџԤϣɛŋɯӦhԑɽӨԔ|',
                },
                {
                    'key': 'ǀԙΜЁӴŋ҇˹Ӗ\x84ԅš',
                    'description': 'ѧ˥ϵŢʃǸGԭΔǜΥÛ\xadßԁÆ҂ԕфВҟɏÐƸΪɑǻƀӈԀ',
                    'value': 'ЈǓԉųΤ˖-åԝ\x84ж·ǏʗħСƼѧ˂ÁȊіϘԣƩӥÁΠвѤ',
                },
                {
                    'key': 'ZыţʎųȻӰнЅƅӈˀɄ˅˷ØлfìѤȲǊǣǗµʈҶ˼UG',
                    'description': 'ȝ\x92ЌѨýŚǟ˒ƵˏȇKǤɌ˹đҮмǻԨVËɁʢΪ˻ŇЬĺј',
                    'value': 'ƗѱķŦĚɒ\x89ҟģ¢нǫgϭ©nκÍÄП=ˉʄɏħȀԤʢîҖ',
                },
                {
                    'key': 'А',
                    'description': 'КӈϦдΊɎÿİˠʆȥԖҕâ˸ӱąѫǶƴȬӛǠЙhʦíԉ\x8bЏ',
                    'value': 'ƻТİѡQҜӊʹʕʦǌʫΪˡ˛īĚ˕ӓӶſͱɤξǚȠоʺҫČ',
                },
                {
                    'key': '˭˃г',
                    'description': 'ǜȹǃΝđҖ»ЦБńŦė˚\x95ʹɆ¨ưϚȾďȮσϔȆʔÀңĎҦ',
                    'value': 'жʠŶşɅi\u038bΨЖ˸Âĵ|\x80ӤƏКˮҵѾ˖˪ʎđƳ˻ºϝԌĆ',
                },
                {
                    'key': 'һ<^ɬжϰВ˥ǊɥɑōȻÎąÏ!ǔLҬпв˼ϦǸɢ¾άȦϽ',
                    'description': 'ɬč²ØȏǂȪlѝ7ȏ\x85ìԁțμɑhӺƳԜΑь\x83ÙýӖåѮӶ',
                    'value': 'ӶŗĉϾŵİШńʁԁҒХ\x81Č½ͻΖɼŚӈǼ,șҫiϲͰҠΎΖ',
                },
                {
                    'key': 'żȌǣΔʇŬżͰѠм\x83˦ƃŤӻΎԡɎKƚӢĞϼɩҏƶƆɴ8ù',
                    'description': 'ǂ˙ƪ\x9fҹƠǯȃŉʄЪŲÿ\u038dϘѲҠɄҹɅϽ\\σʘΫÇżǂñ"',
                    'value': 'Ï\x86ź@',
                },
                {
                    'key': 'ҲҎȴƱЌwʹǍԨ,ʩ˓ĴʝÎĂʑλǄŮ',
                    'description': '҄ԋϤ˭ǪҰʲǒʕάЗ·Ɗ3ľ¦ӪпѐѸ\x9cӆĤſϧÇîкğȱ',
                    'value': 'ÖûȥϰѻʑЍ˝қɆ³ѼçҏüŁȬƮѣȪəϓΡć/ĖϔЏ\x85Ǭ',
                },
                {
                    'key': 'ĮΩÞėξШʧűŶ˒ĸëЉǵ',
                    'description': 'ϯԁʗǆҚΏˌȎĻҴţʨ˶Ʀɹҟԣ©pjĐˤɄØƖ"bƞǵ÷',
                    'value': 'ƻƢԐlє·Ȃcƴή3Ȫā®ɑƛȏ[ϊɳ˰\x90ʹ×ː˜˺Κǉʹ',
                },
                {
                    'key': 'ƝpΓïͻǯƜЂʜʊŢÌƬǴƧĔѿĭ\x96ɾ\x87Ӕɇ˾WɸΠӏ˭ԩ',
                    'description': 'GɾƟȎ-˛ˊϽʍ£0ϚϩČЯмǥƑԔΈźɖʯϩˡΛз˫Jľ',
                    'value': 'șéԝħǏȱ˂ѐуѡϨɶ\x91ɛƝʃœıӢȻ˦ωɹƦǧԨ3pјʪ',
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
