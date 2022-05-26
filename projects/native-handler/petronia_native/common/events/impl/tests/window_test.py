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
            'x': 2150585933746279137,
            'y': 3761749461656321459,
            'width': 8519592404805251247,
            'height': 4067421069318251370,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': -7709633148617492847,

            'y': 2216516068199802881,

            'width': -40583335624844039,

            'height': -2652016267390068861,

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
            'key': 'ƸБȂů˗Ӛǿ\x86×ҩc˥Ҽáҕˑ˗',
            'description': 'ӈʀZʅǩӃ˦ǉůѵÒǃ·ʁԤҔФԣǶ\x8fȌŇѵϢΣѷŭλȜЃ',
            'value': "ɋȰʲΊĻԦgЪѠƊЈӎˈĞɏʲѿьԩĮӯ¨ӲӺªĺҠ'ТЏ",
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'B',

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
            'focus': 8054,
            'parent_id': 'QːǯϭGӭӸҧŮ˷ȳϸмǧŕȏԩŇӏʣԙǑŢȚΩϷ\x94Ť_\x87',
            'location': {
                'x': -1301627850631637063,
                'y': -2667248440313590658,
                'width': 7326232529068128705,
                'height': 4350197787333775356,
            },
            'minimized': True,
            'meta': [
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': False,

            'focus': 3283,

            'location': {
                'x': -2995402768563698808,
                'y': 1867817635158039417,
                'width': -3325972576287290524,
                'height': -8088621865206786027,
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
                'focus': 3087,
                'parent_id': 'ĖȬCʱĜ\x7fϴơɀ¥ƜŖӿůȥľԬÞҤӯГƸүQĳϖπΩɷЭ',
                'location': {
                    'x': -7776988606378409189,
                    'y': 5045559968364711079,
                    'width': -3784258732161387138,
                    'height': 6105251911307482096,
                },
                'minimized': False,
                'meta': [
                    {
                            'key': 'Ņ',
                            'description': 'ɠѽɒϚʱɉǬԍĠҿÿnʶǁ҆EįϏͻ¬&ΪԌȖĞѮĉ\u0378ҹ.',
                            'value': 'ÎȜǅĥӈЄPǅ\x97Ӥ',
                        },
                    {
                            'key': 'ĸбĒ',
                            'description': 'їτƻʺгѪңτӲˉƠɝēџPõɆǯĭĠ҄nԢˈΖА˫ȓԂҜ',
                            'value': 'ϵTԡҫң΅Ӄɮƹӂπ;ǢqƔȄȰГ\x99aâ¦ĲҵǀéЌŷ˨Ͽ',
                        },
                    {
                            'key': 'ԝˇƦǎеԔǵѤλӷķ˝Ф',
                            'description': 'Čʐʾ{ҨǱМkΣȁӘíǅĢɝǰϽŀ\u0378E˹ʍ˧ʼĚӧ˦ƯĒŒ',
                            'value': 'Α¦ϒȫʯ\x90ĘtþǦɭˡΣơÏʧȏŔȇ˦ЈǍϜƧϒ',
                        },
                    {
                            'key': 'Ҹí¯ǘʦаŎҌΧÞĘßɻǙĠ˴Ɣsȱʍ˴ϥğѕLÞԕʤϚȿ',
                            'description': 'ȏŝуȤҶɍϠçӨĽÝʏĞÎȱс\u0383ҩʁǅĤŅЏӗ˷ћrʗ8Ƙ',
                            'value': 'ɴWǣϊġƜЊń˷ɋŴ˖ҊԦ˟ЛͶĭğɟwǄδ)ɇ˜ß˾ʳҵ',
                        },
                    {
                            'key': 'ŴκȧŷǞр<ʐĕî»ϻǾѫӡNǋ3эȸəʁLү%\x87Ɠӱăʝ',
                            'description': 'ɡëΟҦèĪθ=SК*µБȲ{ǪԦӈ˨ŴћřϢ\x84ӯūԥŎАҋ',
                            'value': 'Ёϴɑ%ϻȩˉ¢Š\u03a2Ӄʑ\x98ąĐ˻ǵ˱˅Ɩť|ϯȇyɲΕ˱\x81ѻ',
                        },
                    {
                            'key': 'IҏHЦŬДɇȩɅƢŘǤ3đϋȫɣŗѯϝ.ԡƭ˄ʞŭǘĊwˏ',
                            'description': 'ǎʥŁńIƗ¢PͲѯ΅ÂͳԅӎãϮ˳ϔҤҋΞ˸XΟìĽ њʢ',
                            'value': 'ϔÌäŴǘ˃,ƦɸʺҠ%\x86ĀԛʒǖƈӐǵǲĒТЪ\x87Ƣɜ´ʊ=',
                        },
                    {
                            'key': 'ůѽɎ\x89ҎʱɧǁŹķΙԓɱ\u038dʘЪũˍϴǓǣÔХΞчΰƣ\x8f©Ѹ',
                            'description': 'þϘµҼǧȲжƑʚԟϣ˪ƉԆƭСĜϖxђƽðýÊʎԑĒ\x9aϱª',
                            'value': 'ĎϪ\u0383½϶ЋҤцЬι\x82ưɩвъʜ¾Ɣ·ӘҨȻˢԇ˥ґůƣыԄ',
                        },
                    {
                            'key': 'Ъā1Ɏ',
                            'description': 'ώԅӟ\xadΰàʺөǢӪäҮľčȸΘʇϺќ\x7fϖǀŀŅͺĄ˒ΏǞņ',
                            'value': '¯НҁeõÚшƸTѮЛ(҈ǆͻʀԙȴɬөɦģѕӬӮ²˘ϥǫԠ',
                        },
                    {
                            'key': 'vϯŅφ{ƟӠ)ȰϲŰɷҲͻĻɀ\x9eǉɄΊʢԫѣÜ˾ЈЄǢҪǁ',
                            'description': '\x89ǎμGŎhя\u038dÔЊ$ѷʹόȐˀ҂˓ˡĹØ˻õĬzХˡǸƃњ',
                            'value': 'ѴȬ\x99ǨєΑƱˠԐ\u0383ɼ˹ȚƑаǈȡ"ġÁԣϿJʘҕǟɄÂȶƛ',
                        },
                    {
                            'key': 'ʔҤϨԜЃ˩˽ȐȞϾWƝӦθɶώӁϞηƏФlАȃ˱\u0381',
                            'description': "ÓȢ\x98ҨӰҦǨǧľȅԋ'ϑΎӪΨǰԘϣԈůðïƢžӉѱʙĭȽ",
                            'value': 'ďԗΝ˗жƘȥϐ6ԖЋȨχ҅1\x81Ƭı®Ӎģɜԁѭζ\x9bЙȻ)Ŵ',
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
                'focus': 9214,
                'location': {
                    'x': 2028799830021422413,
                    'y': -467275329631168030,
                    'width': 4299712251056947664,
                    'height': 5252385594321047896,
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
            'reason': 'Щ\x8dԭԍϓȝơƤшÞĕȩϑρ˂уқʮә^ǙƚоЋӂŨ£ǸМȋ',
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
            'keyboard_focus': 2359,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keyboard_focus': 6415,

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
            'window_id': 'SҞʞ?ҴĎӓǰάcӿĭȈìȳҪáǹ$ӿΖЂ˾^¶ˇʃ˓ӭȲ',
            'location': {
                'x': -8867813444785372158,
                'y': 8286437185831967224,
                'width': -4707493208679594129,
                'height': -1030408753463591233,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ҫIâΒԫ',

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
                    'window_id': 'ǷДΊΨōɁ¶ţɿѣ\x85тșрîǥχ˂ΨˊɀɁʞɹ3ӆрϗυ´',
                    'location': {
                            'x': -5897837235422268748,
                            'y': -1372764668765352597,
                            'width': 7175455833344624349,
                            'height': 664257346497484708,
                        },
                },
                {
                    'window_id': 'ʼмŢϜªӸҌĐžӲ\u0380ɇÊȪБɖҎƭЋŶ¦ČˣҍҙĻҖɔ7Ә',
                    'location': {
                            'x': 5881211964376589305,
                            'y': 8857452118478863846,
                            'width': 4541434669960219933,
                            'height': -8931773214262148893,
                        },
                },
                {
                    'window_id': 'ɻӗ5ϴԖʽ\x85ȩЀƨԉʯÞźӜƴßӟ?еЇġƸ©ҋõυʀαӸ',
                    'location': {
                            'x': 2101486718920849808,
                            'y': -249488702512311999,
                            'width': 5599717330347951088,
                            'height': -714954948864477942,
                        },
                },
                {
                    'window_id': '˕ϑP;ˣʿΨȃӑдPŰƤƾӧʰ\x80\x84ǙкɽȨ͵ɹнƂeDТЀ',
                    'location': {
                            'x': 2254829893388374742,
                            'y': 3763206949085625755,
                            'width': -4717408532231890433,
                            'height': -8233292343370849125,
                        },
                },
                {
                    'window_id': 'ŷIƭΕʮĦԞűNȺğіΘŔʽԌ\x87O@ɑ˜˞ʼȬʬĻŹԈ6˥',
                    'location': {
                            'x': 7869141759129865873,
                            'y': -850282292627994413,
                            'width': -8885044430519204741,
                            'height': 2912082066117783544,
                        },
                },
                {
                    'window_id': '×ԐʞӜ`ӛзVƙŒѬ\u0383\u038bų\xadˏˈϸǞƅǦΨʟԗʘȭɡŃȘԖ',
                    'location': {
                            'x': 7864681418939720193,
                            'y': 7632381234839948913,
                            'width': -6844137367357153622,
                            'height': 4916811581646450104,
                        },
                },
                {
                    'window_id': '³ͲDҫ˒ҩǋԩΈĊɁћŝ\x91ХŘΗҡQøЁȃиŽɶʶ\x97ɩŋ¦',
                    'location': {
                            'x': -5071329672650041601,
                            'y': 3687740271811099867,
                            'width': 361026923339821491,
                            'height': -293443256778548512,
                        },
                },
                {
                    'window_id': 'ƜқԫɘȢɅ¼˳ʹ˽¸ħǲҜҡʛӎ×ѶƂҌӒԈӖТƧƳҎɧ҆',
                    'location': {
                            'x': 974774302402439867,
                            'y': -1337909449573366341,
                            'width': -874699474813934157,
                            'height': -5920312316491946390,
                        },
                },
                {
                    'window_id': 'ØђȦ¿҃ɼӎҊξT\u038bԞĶƿʄ˃ɩɋüӰƤǮϫʵʻϣmӝĵʦ',
                    'location': {
                            'x': 67154364371342607,
                            'y': 7434522194575483336,
                            'width': 8929500777903442575,
                            'height': -972670257501421510,
                        },
                },
                {
                    'window_id': '¡ԑ˔ǝІѺϸѧǐ²ιǕŗˬɵʹԭʙǫçɓɓЌѯɶФȳɝχƸ',
                    'location': {
                            'x': -1663529645193697091,
                            'y': 5773329372819652864,
                            'width': -9097064585036351069,
                            'height': -656321420779176573,
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
                    'window_id': '\x8dǢ҈Ҹɀ',
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
                    'key': 'Ϗ΄ƠʲɄӀХɄɫϥλɟöʱ˄Ӊ˼ȿŝĠƲ\x8fÊɥʍȭʙΧԫ2',
                    'description': 'ďɘԢċӺŠγίxҭĮӎłЎȌö<ͼʋQĐΖŀtȹÐШжŏ\u0378',
                    'value': "ϻΧŎӔώȐʻ'ƢÑƫûǻĝǾӠƄӈěìѢԬɋҀɕӴŬŁʤФ",
                },
                {
                    'key': 'ҎԢНɞǁч͵ȥѽ˫δҥԂƐ',
                    'description': 'ɔЧʱĔǰҖĎиɦԙЮ;њſɴŻťːȁŃȏȉԚ\x94áϑǮЯΧν',
                    'value': 'XӉǥȑȣЃ\xa0ĢȹƊŲÚϤǓÕϻҭ˼ĆԀӢńӼӪψёӴϓғή',
                },
                {
                    'key': 'ȶǠĶ\u0379)ɗεȖJλ',
                    'description': 'Ɔҽʬη˵ӥӪǙƩ϶ɭˏļ˾Ϟңõ΅ąҚÄƖ˥ʿǾƁϫɛˎǽ',
                    'value': 'HˌЙңħpӶЛЉ',
                },
                {
                    'key': 'à˯΄ԕРӘϨˮč˳ʞŌWĂ¤ӟӃξʐūñϞӄϊϴЏƷОʷÜ',
                    'description': 'ßμСϰP\x96ώ˨\u0381ѥ˙\x99\u0380ӭӷԜĮ¿Ď¾¢Һҍљ,ӳϐͶǡϧ',
                    'value': 'ЄάĂņȓąúĬƝEЉГĩԥҲƂŤϨ˛ӝĺèтӗȩɥҁҫTɛ',
                },
                {
                    'key': 'ȍÁҢɌщɅͺPġϾ˵ɍʺ}ɭҢӷĨǼΈСŃǊ\u0383ψğƴԭѻЎ',
                    'description': 'εѝğɍĉñĕǆȬԟúԚĠ\x83ӎƯǰåöґĨƗʿѱŤƚ~о;Н',
                    'value': 'NӏƼåÈϻлȍҥΒЇPãģūΐʃ˙Ѧ˕CʚjϝʻȢřďǱȠ',
                },
                {
                    'key': 'Ή˺ĕΝə\x8fԏƱˉ\x84ҒſӆÅˋҰɇ˷ԢкŅȿˉɉwԩŘϥʖʘ',
                    'description': 'ƒҷ$ϬҳðӳĬԭ˄Ɍй¦YȱҳǂʕѸʚμÂņҒТʋȆԢѢҞ',
                    'value': 'ǜȔɱЛҸÃɡ::ěЉԖǏĕƫǾ˺ϟHxļǋƈ¾~ҠŢȖŧє',
                },
                {
                    'key': 'ǘʬjӷҝʏŠӱiϴĸˈÃēǱʩӛǡЬʣˁϨʴǉǒӌ\u0382ϬȐś',
                    'description': '\x9dȅƏɭʓ³Ѕ͵ӨλȁCɉԖЕѠȐ˴ѹΛĔͿŮЈǀ˛Ŋҫȱ0',
                    'value': 'ɩxСεӖʀÆʯyǾщȏņίύåйϊŽъ`ӦӬÚиӍЭŜЎΜ',
                },
                {
                    'key': 'ӟ',
                    'description': 'ӟɨʹȮ+ÂǨBōľģѠʬ˩ðϓİȎ\xa0ăʻʒpΐχǨŉě;Ĵ',
                    'value': 'åȡЊ¹ӌ8ʞԦµңҦƵƶԥƫ°ā˼ĸԮ±2ԁõІϊrщɟŲ',
                },
                {
                    'key': 'ěǝё˹ӲËƏHӡɰԅƪζȀϺKȔÕZȎΉʸΫ˫Ƞ@ļ˓Ҡč',
                    'description': 'ѩɡԈϵǹϝϋѓӻȜÿ\x96ɯɬ`ҦǕÆϵYйǙхͱїɫϙɅww',
                    'value': 'ңȓП',
                },
                {
                    'key': 'ƺǈɘ\x88ą£ȯļƽʏч\x90\x82ʮԐɚ΄ƂĂȡӷ˙Ϋӑºˢ',
                    'description': 'ұζľɝ\x89¼ÔũıDɑőҦҹҢʖǼ{ʝSĞƴàôӬŹёǯяȎ',
                    'value': 'Ɩʇhˍ`ќϨА҆ҭdŜɃʿӨPвҷǼϤάӅͿщӳɃɚąȣ˻',
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
            'focus': 8080,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focus': 1403,

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
                    'key': 'ǿ˥ѝɀȒз˩;ɼʷ¹ŬɭƺЃŤФҫГˌǺ˷ǡҝͺšƂØãѼ',
                    'description': 'Ӕҧɘ·ÐԚȀǀǉˤÙ\x92ҬȜ ѡ<љǡ˺ЊӐԠҷƪѱ\x87ғʤ\x91',
                    'value': 'ĈȢУĨҁ4Ŏӓ&ƃѰӉ \u038dҶīǾϟFǖԃϼҵňŌԣϗКŕȦ',
                },
                {
                    'key': 'ǩѽǏ7ɬ˲Ҋǚ=čʤˀǰЦѪ\x82ǤƦÎЌÅ/',
                    'description': 'ѲŗBȌПӀόĕґ\x94ìŋpƓƣǧϳȦԓɽήѝүʋǓǛ\x84ӠҌЇ',
                    'value': 'ʶ¯ȿɂԛĨŤʚƇŦѢȖßǆϒ˓ǲӋӥҸ',
                },
                {
                    'key': 'Ǩ<ƥĉȊϕЪѾӓFʙѶԛ9ȴϚ\xad+',
                    'description': 'ԣ˨a҅ϡ¾Ӂʀ_ϭ\x95ұǁиȢĿʼȡ\x95ƚ\x8aÕȧɓ°ЖϏͷӝɛ',
                    'value': 'мıďƉшŶϹЄȦȘҸźϊԅӥТȷЅÉɖȏҒЕÖ·+˪˧υǻ',
                },
                {
                    'key': 'ťɸҒНʕ˜ҧǊԢʻΠǘŃɓƇˣ˝ʶȥǪңȚª˴ɞˌȬϐ',
                    'description': 'įЈɎϪхӦȿΓŅΓǀɞŜ/ӶʋʁɜѡΔϐnʸYҰǠɓԜȽĵ',
                    'value': 'ԃǛԉǤǴȻåńƜĕӀϗ˵şΘ\x94ʧŔdӵЂƉɩҧӴѿЇʽǖǨ',
                },
                {
                    'key': 'ΏƢћҋԓŸӉƽƑ',
                    'description': 'ƮƭаԞ»ѧћƍŖ\x83ĚɣëȉșÚͿ)ӡ\x83ϭĕÚȌǑҤĚϫ\x93Ǣ',
                    'value': 'σϰԦϟϬΚǀʁΪȒɾƛЬѴɋɋÁξОͼǨÉĦԜȠěΈӒƺǜ',
                },
                {
                    'key': 'ȽEȓˆʎԄ\x7fɻϮЂȺӿʢіɢɗτ˘ƇΕąн\x8fţƊҮ[ɣʥˋ',
                    'description': 'ЄΊҶЀѣŝƶ³϶ʛΔюɕ\x9cǑʹԊíґƒѾѳįʏԑӦˊ΅Œ',
                    'value': 'QǈΪĢύ˙»ùÖϽ\x81ӃϾЋЀƑǄΈƢӖɎϮοɀƁȭ\x95)ɢĖ',
                },
                {
                    'key': 'Ȇӯ\u0378Ɍɼѣ',
                    'description': '\x8fΦʾžҴ-|ǡȑŌɏȜǣу·ʺʕ˚ɣƗȕμɟϊƑĀŊЯζɄ',
                    'value': 'ƋǄщ\x84ƃȀЕΏԁĕҹӢưάɩƂƉȤ rӵӫ\u0378ħԌҽ˰ûŜ\x96',
                },
                {
                    'key': 'ѽ}һŢӥƢ±yȗÙΧͽȕĠЏĐ˯ʀwȣɉ$ЀŪ',
                    'description': 'ΩŐϲюǦԜͷ˫ԭkѾԥƅ\u0380ʊȯɫʰěɲ;Ɨ\x8eϜѨԄц˗ǍФ',
                    'value': 'ͶϿ\x8eğʗΆ\x96ǹıњʱқʴѮ_εЭŞ\u0382pϙƚāȔ\u0381ŎĈȒʝ\x8f',
                },
                {
                    'key': 'јʡrυΨέӶƥϛЖϸХħСƛЈЗϛ˰Ļ˽\x9bǲхͲvÉʷĈͷ',
                    'description': 'Чɸ%єʟĹÉυӂȭūԓɹӅȣмȜϕǘʧ¤1ѝϊ@:\u0381đԜҕ',
                    'value': 'ҍήǕɡӬȐђΣ|˽ɬьǼǃ˺әΔčʇʬ\x86βʮȬh˱Ϋ˄Xө',
                },
                {
                    'key': 'ƔŰ¤НǋǼyśԆƺ-ͷǌĶбҠ˱ǹȻάǂfжčʾíC0ʧF',
                    'description': 'ǋ^ʘƵ˃ЏĦԙ\x8eǼū·ƄƌϋЮÍɽӁâĠԗŰԦԐǮŮɖƧȼ',
                    'value': 'ӹ»Ł˽ƚĘȏΟUԁͺʒԣģҪǤËȹҊͰOҺEȧϭƬĂәe˜',
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
            'window_id': 'Ƙĥ²ȩǓȍò˰ǣáȷҀȘƨӌԗŁɾƁŏʆӑʄңſϻіɇǺШ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'µʜȾlʮ',

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
                    'window_id': 'ғȨҧɘƥрΣ!ȥήԎѲӉпϒ\x90˃ђԖ\x8fҜôÁđʋȹѝƭǳԞ',
                },
                {
                    'window_id': '˴Ҋʭū˕қØӥș\x8fѠӥø\\ʁ§φɸӌʕƸ\u0381Ȅ˹ɤʈˠȲÛȠ',
                },
                {
                    'window_id': 'ͽūϰÚĵŗǨ\u038bњÿƵƳʮɏ×\x8c\xa0KӌɬоԞƹԅнəѨȉȏш',
                },
                {
                    'window_id': 'Ѩŏɲ¯\x96/ӡġӝκʯ6Č\u03a2ѨėӛɶΣÉüӉɤǼȮщͱϊȪґ',
                },
                {
                    'window_id': 'ƹΊΎĊӇņ҇ǓƱϥҖȧĲхÇ˹ȰƽԫƍА\x8cƍϓЦ´½ˑԈʌ',
                },
                {
                    'window_id': '˜ƙ\x8fƧ½¯ͺ¸ƱƏ4ǈ˗θʇӈŞŒѧǉѬͽњˠԚƑǬƆä¢',
                },
                {
                    'window_id': '9agˍιϫƬυȪɧʂŔϏøɦ÷şːɾӏĢџşΞЇδɓѣŻɪ',
                },
                {
                    'window_id': 'Ϯ˥ѷ|өMšπʨȉӞŌҦΨ¼¾Fƻ˗ҪʑǑнÜõǜʜɗ\x9b¢',
                },
                {
                    'window_id': 'ŉɕǮ\\ŁçӿüѤѴǴɻɅ\x87ԩǴόÖëQȍӭƄж\x97ƀʾ\u038bρМ',
                },
                {
                    'window_id': 'ɛƙʌѿβĩңöËƑϤșό\x89ǅʬ°α¡ӈǋ\x84DöΑѸҍқɟʙ',
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
                'şǺЗʠɬӫ\x82ʽʢƭʌȴѝő˔F&ȸЄ-˖λԫǯŔɛѽɛǻʠ',
                'ѣԄɇӃģԌ˞ɄɄɂňŬŭŬɶӞǄ\x8aœǳ\x8dƍԔҨGȾԝùāҫ',
                'BҍȚʸϘϢɜԖĦћ¢ҮŪƪϒ˞ѕ\u0380ΆˠűѠFǪϩĹΏŭԜȊ',
                '\u0378»СűʅˊɳɿʆґÙШŷϝÊˀ˻δʃńŌǇlťυͳ\x9fJàΔ',
                'ӠϣəɳʆѮôϑñˣӗɈʏiüіƿЕ¹ĀaӷҾʪʞƬǮѧӎĄ',
                '§ǜľҽĽɆňϣķЇ˔ЉˍɻфԦοĮ±˳§Oԩɿè\x8fΙӆȶɴ',
                'Њ£μçȇмXƉϐϺËUÚƨÂƺΣʊǚЙȄƾԎҗß˩ͻÁǙ¢',
                'ʰҘ´ԃǇѰоΞŽӖķʟӣЗȿԅȮ\u0383ǩмÔӨƅЮŰпƜǱ\x90ԃ',
                'ʈѮ҈ŇÎίÿȴңӔӲɍ%э˧ǐҢ҉ӄǢΒ΅ŚòˍҦӬĺ£\xa0',
                'ҬAщĢϞˀ˶˓ͲɚȔ˪ĶşԦʦϑËŽ˴ˋɓρьǥǯɦвξ·',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'ӯҭɭӖŢ',
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
                'focus': 2048,
                'parent_id': 'ΛŴΥԍłńɘ˟\x8dɚ˼ΊŬl»Ͽͳý\x93ђΒԗ˔ȤЯƼͷунӝ',
                'location': {
                    'x': -6120188442382158518,
                    'y': 3076263402236344914,
                    'width': 4400610557939623108,
                    'height': 4712683622533911736,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ΥΊӲΛѠјҠɛʷąМûȔҙәĹӤɞͼöƲ',
                            'description': 'ãϲѱԏѶӭӠʺϧ˛ЂÔ\\ȗƳȻԝłΔΓÎȉɾSе˽Š˲·˻',
                            'value': 'zƞç|ϚӫϭɃǬɵ\xa0СѕƾˬϲԍÙʹЗӈЖҏМϊɴō',
                        },
                    {
                            'key': 'ʓʚʤȑşƅȺĻ±ÙΤèхlґЋˡɩϘЪӶsʘѿ¶àԝŀžɸ',
                            'description': 'ƓƥUŷĶ΅Ʊ\x92Шɗӭ"ԡ҇Ϙʍʲ˹Юҹλʊ"҆ʹìMӫӰĭ',
                            'value': 'ʀʶŋĮŖ˺˻\x87˝ϺŸҬǸӲ˱˽ŰªWӔʿXȖˑǽЪӊӍ%ϵ',
                        },
                    {
                            'key': 'EvɗËϬʴȌġͱƃϵ҃[ӦԬϸѸњǑԫǿЫjπόȢn\x8bΦϰ',
                            'description': 'ƳԣʔԩŢχľÖӱɋÊҗϑ©ģȗԣĚːȀÍӌȎAĴѷӃѫɺʠ',
                            'value': '҂ƺмǆͶϕñ>ȎɋϙʁЎȼΡΊѬӣƬĤǳēƜϭΠφɣŐƇȏ',
                        },
                    {
                            'key': 'ɵȤ',
                            'description': '˓ġǤ5фӲɥ\x94éȌ\x8eɵсЖ½ԙАЊ^ѥ\x82ąӾθѕШŊŬѐŋ',
                            'value': 'ŉſĦѰӮӆÅ)ǾɚÉǌbȜˣQȿԅϺΧ҇°ώєţɰȗηҩϫ',
                        },
                    {
                            'key': "β§ƏƂŏɪԟ\x85ѻӠěόԅԙƑ'ǎ»Ğ\x9f",
                            'description': 'ǅң\x85όѨĢŇԈŘҜé®ΕȽԍȟʮұňԑɠıκҥěźʘМԒŇ',
                            'value': 'ЂӎƞƫӠоȜƇȕőZͶŁӚōͺԂϧ\x98ȌϳǨ\u0381Ɏǖɷ\xa0μΣ7',
                        },
                    {
                            'key': 'żӛҗȍɈԡѻψүŹŞҦșԒħɁίɥ¢ŅŉћϿӵúɽǒeŴU',
                            'description': '˸Ӥ&іʹWѺѡȳ\\ƁŖ×ΰɜϾʎ҉RΛvǗq\x96ǄЛytĉԚ',
                            'value': 'ɷɁӐ*ɛωѐэȏFϥˏU˔ĉʥėλΊ¹Ǉӛæ ƌƲǃʉ\x94ӂ',
                        },
                    {
                            'key': 'ѐԍĲɪӋȉԂҝYϥѬșͷѦWƞԌɆșʼԛįӶěġ',
                            'description': 'ԙŧʊʡԑȵ¢ţηњҵˤΏɀ˥ҢŦȞӦ=òѯˇůЫԀθ¾fĩ',
                            'value': 'Ƴԏŵ\x94ʍȷԀϻΟǩ\x8eˢёҽÞӏԢ.',
                        },
                    {
                            'key': 'ΚϾцҼͲχʩЎɛс\x82ėɻІɎ',
                            'description': 'ň˓έȋņÀҭʧЭâлёҧҾҸӉȉҟ0ʛáχȨŞˬр˒\x8f=Ғ',
                            'value': 'ɤԠѬԤǊ\xa0ɓs\u0381ԮƅʩǱŌTŪʯԅĽӵķɇĖɾϞɓìƬƱɫ',
                        },
                    {
                            'key': 'òџϔέƺʜĚÉѲÀҩȅ',
                            'description': ' ¯ŧώӢŅ\u0382ЙÍʹ÷Α¨\x82ƐҩϞǧ£è\x97ƥķɘЋ<œӻԆҘ',
                            'value': 'ɑʜѕ҂әӡxǁϖΛӆǠʥϿŗƀ»\x9eѮʸ;Ô\u0383âƍҵłƩ¨ǡ',
                        },
                    {
                            'key': 'ʏɸŋÒҬӦȂЎ',
                            'description': 'ʴӎ(ϫȨχǮñʸǵƫɲЂɥԦʹ¸қĺӼӌÇΉԙѯӊҘˍ?ȝ',
                            'value': 'ѝʨϾϔ˸ƣȪɝêџɌ΅ҡɢҞʼРљҽŤŖӚ\x84oɷ҇ǏŒ$˱',
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
                'focus': 5245,
                'location': {
                    'x': 6811209333162634353,
                    'y': 2908991115124918044,
                    'width': 5133744986538161300,
                    'height': 4693434144731852727,
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
                    'key': 'ČrЩƊɫ\x7fɅӾуÉƉɾԅԣѼ',
                    'description': 'ΒΤԓЭȣԪi˨ʍѮȦΧʆMʈXϻӆӿʭϭǌϾ3˶ŮƻԠ\x98ȷ',
                    'value': '\x86ϏÛǞŅë·ȡʣǒǖnzӭ|ēƿȂʫɴħӂɩԁҔƳũ-ȑԧ',
                },
                {
                    'key': 'ĨŰɦɮȪ˺ӈũЏƂŷǼ&τǹƌѬʳƶbӥѕЭԖ˶Ė9дʑ˷',
                    'description': "μ˩ˡӫВȵiɊОІ'ђĬŔϫҸȄǞʎр§ÌăʊϠ˭ǨёĶӘ",
                    'value': 'Ĕ¶ʤǅп²ɝСƼÁϸUӺѽәˤЬπ\x84ҊˑϸӬеŅŃӓ»˫ӓ',
                },
                {
                    'key': '\x8fΉŜѪɄčžǄȍƞӿӀȊѬ',
                    'description': 'Ǝʹ˜˞\x9dzϦʁĘʛL҃\x96ϚԋΨĊĵԩҴ˩ӾʄɛʝЌΆμӶƃ',
                    'value': 'ŮĀӸŠƥ*Ҷ\x96ІǂŘ&ͳɗ¡ƳϪȔ§Æʎ¥ˡɒϸJ˘ȩӈҔ',
                },
                {
                    'key': "˚ūƫ˼ԂÞ'ǞшƆ?ΟñƞњΖĸʝөҀϥǿȐȄϗǦȚ˔\x9bȇ",
                    'description': 'ȘЈɴХƥ\xa0ɥΦϗјƥiŇҀǡ>ȳӸ]xЂĿǵςѨʏΏ·õ§',
                    'value': 'ҷϨҠΘԭäŢǓǶȂgɡԭӫңԘũʪǺҶӇʘɮ+ʗāͲ\x82ʜɧ',
                },
                {
                    'key': 'èΦȡĂΛčқϛͲǗŚȃԔёӧ',
                    'description': 'ΙØˢȥˋǲʖɷ˼ȮǳƣɋǵƯǽ\u0383řƆҲĹƄǻõ\u0382Ŷ7çƻˍ',
                    'value': 'ƆϞϏԡϒ\x88ґ˃ͳ˨ϾƐѸȖǃԒĹѬ\x85ĲÖːŌœɠЫ·λ(¸',
                },
                {
                    'key': '¸ÓdȟʠωǜˠдӎцЭ\x84ҤˢγċѬѫ=΄Ƃ',
                    'description': 'ϑƁӺŮ¸±ЉKӺӔʸ˩ĥǔfӜɐМïЍ\x9b:¡Ц\u0383ǻɛĸϋÝ',
                    'value': 'ӂЮΒɄвɁ\x93ϚǢ\x8cϫԧ¹ʉԨȑ˽ёΒ˛ƙϒ˽ų¨ƟȝҬˆý',
                },
                {
                    'key': 'ċЇˮβҿȐǴүϋԅǭzưτô',
                    'description': 'ˤƅęƶÃƯҘǃ|0ϟϺПęɠɿɛѡӼöɧӝ\x8cǁϊµɖѝњȕ',
                    'value': 'ɨCһ˭ſȅ\x9e-ȆΈǝŕˣ®ɖ΅\u0382\x9aŤМŔĘѪɜјǣãȋǳƥ',
                },
                {
                    'key': 'ťǴ\u0378҈ǔÀ˹϶ϣͽǢƻё_ЏˬñѧƚόԑÐǩŖȃĘѿĽ-ǆ',
                    'description': '5˻Ȁʧ|ɲʜӬ&ŗ\x82ƚˤˊϰӻùԀҌʅҬΪԥɒўţ\x9côОl',
                    'value': 'UÙэʗ$əÃчÒɉԉȷҽÊǗěęɻÛοΕϲŤ_ŕĠ˵DƊé',
                },
                {
                    'key': 'ԅиŐҵǄɃ\x90ǮӷȠɓ\u038dũŕȹδã˭\x95ʑưĶÁƐYϮŔ˝ΐˠ',
                    'description': 'ʦĝʻǭʪӋбԋȟvԨȰǮʐƕ^ɚɭɛʏԂüƍƧŁ\u0379Ⱦ+ƞл',
                    'value': 'êΟЅȓ\x8cĎɼȡ\x88\u0380ΰӔϽďȈҖǼҝǣƊѸǬv҃ĂÄ\x8eϡҒǷ',
                },
                {
                    'key': '_ј˛ѐѾŰщпҞɻƌѩϲɀҬˣL<\x93ƻΩ˼ӬcѾҫН˴Zӌ',
                    'description': 'ӚґԥϝσҬưНƸàԤŕȕоΛˏѦ϶wźǯԞɖЮԘ˨Фϗƃʮ',
                    'value': 'ªЮӳԩÆϲӜǮφɫζѬ:ɺʗ˩ȴȄЋ(ˏƞõŀѫϴҶΎΓΎ',
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
