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
            'x': -1030366850697275472,
            'y': 1552180814302619908,
            'width': -6561746268071168725,
            'height': 2498993015310330971,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': 844105682795948190,

            'y': 8072080144740246849,

            'width': 4359930221192686794,

            'height': 1032003569434804360,

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
            'key': 'ԅƓϧŒ´Ρʿ\u038dԐíēȉ˸ǟùǉԚȄѷҫԁY\x7fD*ԁ-RŒӇ',
            'description': 'îъĩϸȼǭϧ˛ƿϐŭ©ԦŊēӯӲLƞëƸ&ƲєǭѥгʴЃŧ',
            'value': 'ҘȧĞϋ\x94ǀӶTû˻ԉοêάˀsͼԗȌΠ÷О/ѨŃƺ\x8dҫѳ\x95',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': 'ǈ',

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
            'focus': 9567,
            'parent_id': 'ȫˁȊɵǕҋđԣӖӹʈί˛ŚʻãéԨƀПҿʭPΝQʐÁƳǅɵ',
            'location': {
                'x': -3699036442318306668,
                'y': 5865642597487013623,
                'width': 2419461749972689019,
                'height': 7595083483190747511,
            },
            'minimized': True,
            'meta': [
                {
                    'key': 'ȼɂȫҎŏДūҁŗɗŭҗ',
                    'description': "ԙƟπŋʩÇİȼ\x8cҒʞҼžƘαѓȮ˓×ԗцΩλ'ųbȴ˸ːц",
                    'value': 'ʤǖԂΫӜȘùƄTӠӄ҇ʀЎƢĩǿͻ2ůɐľÇQλ˩ŷȇ$ȇ',
                },
                {
                    'key': 'ʥɀŮ"Ş\x8bǫԓ',
                    'description': 'ƓϾ|қϤÕѦĄӲҌ˃ùϛǦΨɁҪʮӞǻÛЖ\x83ѡĺ¦Ƥϡζ×',
                    'value': 'ŉдϧ`Ȯ½·ξґ',
                },
                {
                    'key': 'аƝҨѸԈYˍɢŃԛɪҋҹ˩ŏ΄\u038dC˵ԃŸәҪӼ҄ɀĴϹńф',
                    'description': 'Ʌª҆ҝƹśĹҝƴύɛѢǽϠe«\x82ӨʊŤ\u038dǣ!đƒłǏʤĩˮ',
                    'value': 'ɩĺʬƝxɲŭϗ)ȡȍǣɃhҥϊϠϼpˉΟĤȱ½ΓÄӏъ%ō',
                },
                {
                    'key': 'ʐϊɗÃvÕśӃ',
                    'description': 'ĩϒÔщȜĽ3ͳх[ʤɩǺĉ\x81iФԇҽЂŲѯ˓ɕΓӓƙȥҼӞ',
                    'value': 'ӠҼǖ˸ѭĴ˂\x82ʺζhuΖҌƕЍӋSζҕǥӛȑɨȰDʔӄ\u03a2Ш',
                },
                {
                    'key': 'üŴȮ҇˭¼\x8dɹѬɇ¯απňԫĶӷĀ/ļĥʅСʀзїǶāВǽ',
                    'description': 'şϋðĞ\x96ȆǘŘɱԔӥȉĹÚĸҗwΠǼƁȴĹͲѪ¼ƽ˥ʾϊǡ',
                    'value': 'ƏƳȘÒҿ˧φʠ.ɖãɤſРӤʓЦ\xadŢԧmҫȫɱIҳλ%õÇ',
                },
                {
                    'key': "ҴΓ×ΝѩʉϚ=Ϣ\x98'Dϙүcʞ˖đʊ",
                    'description': 'ˊƝˍʥŜʽтʰĆˎ¼ͿρƞƸҌҙАɍϙҊΜгăŅΚ΅ʾϣǮ',
                    'value': 'ˉΝüΜ˔˜ʌŊϮ˱ǈÄ˥ʩɛƵѱńҼηȌɋJ˄ɐŢċǶ͵ɕ',
                },
                {
                    'key': '\u0383ӮΓӞ\x87Ԡ¸ǩǶȢ\x9cԕ˛ǁʐ',
                    'description': 'Çϑа˹ZpĸГύӝŞĊĻϏ˟ΠαĪҴɹҢġƉʝˑƔİʫЇ0',
                    'value': 'ģȎƸΰǴΨϼďĜǎЂϗɂÔ˞ʶŻ^MԁʊɼӰƖ4ΆǕāmĈ',
                },
                {
                    'key': 'ƀΉƾȒԒЖьƹ\x94τ·ѢҎРϋƨ¿˙ӃȚ½ɔʧʭŏ҅ΌΰƝѐ',
                    'description': '˧e\xadðҵΐ҅ģƼƞʡΆøβϱŵNƎȖ\x87·@ɶÙɚŜҰūɂ˙',
                    'value': 'ӄʭɥЎŚłǰǫƃņӈˁ\x8cLӼӕǷǕ˩Юʔd\x87˛ԉȋμώìȫ',
                },
                {
                    'key': 'Ɉҽ',
                    'description': 'Ѧk˶ƐťǿҵӇͲӐ6Ï\x91ͷ΅ȺʣƺЏԟ˹ҌӰʵƑň$ădО',
                    'value': 'ѿҷҵˎǅ¦¢ƜŹČù˃θЫœ\x91ºĝơƽ¯ɑëɾɲҴă˜ƌƪ',
                },
                {
                    'key': 'êǄ˹ʹʗǢžbΥҴĬȶϑϐȝȳJźҼ˄JʳƑѕϼ¿vȖɤC',
                    'description': 'ˤÆœҐ\x88ǽҦˤǮďĸȟ\u0380\x9eƟԨшӘǀ¾ĳř϶ʥÏѯƜҚǫŜ',
                    'value': 'šӓѵ\u0383÷ϙϱɕ$ʖƂӈ΄ϔ˟ίːΩvñ\x93ɻӻʯςūȧĲϏϹ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': True,

            'focus': 7169,

            'location': {
                'x': -6980485686876250387,
                'y': -938973448314634999,
                'width': -3048163934545515423,
                'height': -2945777008059408128,
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
                'focus': 9978,
                'parent_id': 'ҭͷӹ}ǣѺӂѩ\u03a2ϥǉƃҷĝĺȆɻɐ®ŪʠεГΤʹϽԭбŉ)',
                'location': {
                    'x': -7651304388995014914,
                    'y': -297723948170786010,
                    'width': 758566630245996820,
                    'height': 3139309952566704612,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ɕӹ˼ĥʷƭ˙!ϓ˞ШǭŅȘǟJĤҲ˔ʈТгƉɝ',
                            'description': 'ȜɭˍɖЂԠЏΖ\x96ԞїĩρѸɇ˛ʓǚˑƉȃʂԥůņфΑ\x96ЪƜ',
                            'value': "ɗĩéÆ¨\x92ʑӚζάʂ'ØŚ\x89ϳɉɍ\x9fíÖ1κӡҰɒQқǮη",
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
                'focus': 7338,
                'location': {
                    'x': -8280831455684730733,
                    'y': 4378158517217911265,
                    'width': 5104301011325447081,
                    'height': -9096495281433966070,
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
            'reason': 'ȵѳɺŴюѸ\x81ĢϱɫʳӇϞǺɱ ЅʑRɁ˰»ѨȫƜ/Җéư~',
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
            'keyboard_focus': 1055,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'keyboard_focus': 1524,

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
            'window_id': "ǙŐʣŋӪğȷ˽Ɉʍ1ɣ'EщнҭҪ¥ǓƋʏEϨǍëԛɔӅ)",
            'location': {
                'x': 1296754266705966839,
                'y': -5303778947840875881,
                'width': 7761496380419771722,
                'height': -1357559758445432890,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': '\x95ӾҜÞũ',

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
                    'window_id': 'iɯɍӚ˾ċyfƫr\u0379ӴЇжѩƢĊʞҢŗÐʌɸөǕύʏœˠı',
                    'location': {
                            'x': -7319987041895437638,
                            'y': 9002900189077621057,
                            'width': 4308621448573967199,
                            'height': -8440901876745006569,
                        },
                },
                {
                    'window_id': 'ʠ˖\x87ґŦɍƱҋ˽ʒύҩƗȨ\x8aɔɦϝÉϛK\x91ʌѡ¤ҮԪȴ¼\x82',
                    'location': {
                            'x': -77394860593526959,
                            'y': 2646686491121819763,
                            'width': 1483793231870136624,
                            'height': -6316440626606079181,
                        },
                },
                {
                    'window_id': 'Ċ\x9eŽ°ΈǼщóʷϟ\u0378ƍшőĸϺ#ˮɸÖŅRŚˑƵΎҜƧҮ˼',
                    'location': {
                            'x': 7576170123682652255,
                            'y': -5390392270892564080,
                            'width': 4152770024252817850,
                            'height': -124960789870937471,
                        },
                },
                {
                    'window_id': 'ņŉÖϟԒͽŰӱGȠϋ\x92\x91ˈ$ѴMʈùӳҸ\x90цƁȋɟϻˢϗ҅',
                    'location': {
                            'x': 5618734853643672799,
                            'y': 2447628950049985111,
                            'width': -9170820838515381161,
                            'height': 6105844931757672190,
                        },
                },
                {
                    'window_id': 'öŬƴ\x8aҰȸ˧ɮњ)ΖĸʦЇȐƣԟǥЗмПǛњҭηʑПǩϷʘ',
                    'location': {
                            'x': -6939628571043468273,
                            'y': -5053323131870111641,
                            'width': 980228904251146772,
                            'height': 3772824641152768043,
                        },
                },
                {
                    'window_id': 'ŐΔhǴХŜіAҼŚĖŃĤŁ\u0380ЄҷͱԮ$ǸǤҌѸ˒\x97ԚÏɏǗ',
                    'location': {
                            'x': -550522940924831300,
                            'y': -1899514150950359719,
                            'width': -490792816767643378,
                            'height': -8132433571453535605,
                        },
                },
                {
                    'window_id': 'ӱϧϛǁӑӘđуƿʣʴɛЊwÿ\x8fRѼŰԘĐʓ.ˏÎѲж˅³Ȥ',
                    'location': {
                            'x': -3063014268089264924,
                            'y': 5817000793366499037,
                            'width': 4294597860332923995,
                            'height': -6522914474677002147,
                        },
                },
                {
                    'window_id': 'ΎȺ:ŉ[³ɭʌ¹Ѻ¼Èяmsžΰũ˷ԇŮʹ˼ǧ϶ѰАŽеǸ',
                    'location': {
                            'x': -5031480679941761905,
                            'y': -128898552487110507,
                            'width': -3247391803437620339,
                            'height': -874353718013032376,
                        },
                },
                {
                    'window_id': 'ĴȻƉѴȌƞǪŦˆЊƛԍ˂ҫӹ\u0378ƓŇЕшÙӪüƋŊԤè»Ψʸ',
                    'location': {
                            'x': -4831707795093181246,
                            'y': -3723366396914284496,
                            'width': 5772951382136836957,
                            'height': -6580046268789324691,
                        },
                },
                {
                    'window_id': 'Ǎьѓǰƺ\x97ȁȀ˺ŲΖŉҕуͽĦÈС¾ʅÖΆƳƂφυ\xa0ӥΖ±',
                    'location': {
                            'x': -4876343596910163487,
                            'y': 6453943880451705792,
                            'width': 6195981869970576401,
                            'height': -7383575864696001014,
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
                    'window_id': 'ҨȁҼϫȂ',
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
                    'key': 'ѼТ˘tǛɕ',
                    'description': 'ęŐÈӟƅ=Я\x8fϦūόĺŁԪͱиȪѦĻ˵șѐÖ˂]Řρȕǃτ',
                    'value': 'sͰͰǰЊҗjŁƬ\x9dͿӣʤϴ˝˧Ơǫӏː¿\x90ϟΝϗΞρǡѩѸ',
                },
                {
                    'key': 'ɵǪ¼дǣϑīǚҜʅîѢ2ͰҷҜϱ¬ѪС\x8eϬYɍ˨ʛˮӹВΐ',
                    'description': 'GļЀąɲʣͼɇ\u0378ÂȏÑϒţʍʖǱў¿ԍӪÃʓđˀƯңѰYƼ',
                    'value': 'iΥ',
                },
                {
                    'key': 'ԁʹʼаĶӥˉɾɅ',
                    'description': 'Әǘ\x83ə®ǲ&ϐѐΦšԉɗːÞɗєчѵˉԠĳſpӄÎѮ2˳_',
                    'value': 'ͻјÂӾӘȏŋƃӺǫѕĲǜ\x90ϴmÆȖԝíϊҵʚ\x82Ґː˭ɲƐ?',
                },
                {
                    'key': '0Ȗ`ԞĚʡɄҬʽûȻϫĲăƘɺѠ\u0378čšД\x9fќчӡ',
                    'description': 'ƗãαǡӅҳƼҌϠŠ=ΐЦԕϾƒΦƄaľϷ˩\u03a2\x7fƇҝȑǠԫ¥',
                    'value': 'Ǎўʫǘ˄ԓ°ԡгΜȅÇƮÄʰЪѿľŚИѾɢ}ĒÞƩԅû˾ϊ',
                },
                {
                    'key': 'ŊѐĘ)W',
                    'description': '˂·eʌϒӖÍĠЏԬȓӭ»κΗȴĥԨϥ"ĲbȭÜʑŮõlԓɾ',
                    'value': '\x92ɞßġɹЭ8Ĉ\x82ԭɌњˈҕЩƦԒʛǊҗɟŒŋőƶʚǥѱӂʦ',
                },
                {
                    'key': 'YϋďҩŸǍ˫ϋήӾϐηįʦ',
                    'description': 'šͶɖѯǇSЅfέӭɒ\x8d\u0381\xadԒ҉Ӏ>Ӹ\u038dâНĺξA4ҜĬĂҭ',
                    'value': 'ūͲғȒÔǚƖЬū҆ʝĆÚυǩϺґłǊǈԅɨ˨ʧҐɜΖãԆƕ',
                },
                {
                    'key': 'ǘΥΤ\xa0ψÜϿɚ\x80ʧƃsʫOr´ѸΑǀҧǝзƈƽˆ{Ț˼ƠǍ',
                    'description': 'ľӃ\x8bРʩƋŨϱĺxЮѻöŇβʨгȴĶ\x95oҸЊ]ǦάXŪžѢ',
                    'value': '¸ˡʹƪԤʚĔĶäǖ\x8d<\x9dʤƣ\x91æǨˏԃMſ|Ɵ?КӝлŢá',
                },
                {
                    'key': 'рĬȋӸêόƘǰċ_%Éȿɚ',
                    'description': 'ȏӱĔɜ˫ɁˡȘυķŔнԞӪʑĵцҼ\x94ʝ\x98ƷѻƦѝĿϧ\x97qё',
                    'value': 'Pgɯ˨˳ԤӦʉθ˵Ψ˶ìŵǱʹʆ˾ǠǁЎԆз+{çšǣȤš',
                },
                {
                    'key': 'АɎʲƟӘӢӳ\u038dԮȉ',
                    'description': 'ŧǋɝϾ2ʶ÷Íњτ¥iФϲЄжӃϒĚ³ɏξҫоɂϣϣϸӛď',
                    'value': 'ŧºÆϔȋүǶкөɠ҃ӭGκҾϫdŌϒЭȣƁɁԆӯɳԦŮ¿ѳ',
                },
                {
                    'key': 'ù$ԟƖŹԆȜƦΰӏʷԩˡҔǛǃƄԂĞԙŜƏŲƦʷʣŔӞbɽ',
                    'description': 'Ȭ?ˀҾÆѯ¸Ȕνǥ϶ϊƑ4Σ&ħӝГȮȃɌСˉƂѳ¦έZѓ',
                    'value': 'ºͼΥ҇ĴşԗƠκǔξɺ˹·Ԛ6тˠϾӇřӲ˛ҩǬ҄ʫiˁŽ',
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
                    'key': 'ǐȲ\x96ĶÚɈϴӼśľϨӝˏìԈԄ˅ϡ¤ǳí',
                    'description': 'ΞzņĳƆԨȤǴѶӸѯТǂÂ˦ѭϫѱȌ´ƠëŪŃ˘Ɵɑϥлá',
                    'value': 'ɫʑӣιӚ\x7fęТǬľ\x84ȰʛϔɛȂгπҴˇŊǘǗҝ˟ϹӾKͱ˰',
                },
                {
                    'key': '²ґ\x91Ǫ˶ɰɲ\x87˔щЕɤż«ԄʀΰҵƃʽvҿƤĹpҋ+?ʑǋ',
                    'description': 'йðѴkÕӚƤңėЊǛmӯ¡»˶]ƕ\x99çҥʟĘВ\x8eԮβЪʁҰ',
                    'value': 'џƞΉ˥ѽЭ\x91pаŀɋʹϷ˾ǚȒуÍӑαЕһɐЂӚǿćŁϼl',
                },
                {
                    'key': 'Ŋ«ӵӝϴΞò}ς\u0378ӇɹҠȹƾѫj',
                    'description': 'ǁ\x83\x9eȀˢkҍĈӥҜ°£ҀЃԨҞŦҮAȽʥąʰÙѴNƔ¥ƀɮ',
                    'value': 'ϨʢͶҖÛқƙ±E¯ǅįˍҡ\x81ҵйɖTs+ϟɳΘŮөӾҬѰҢ',
                },
                {
                    'key': 'ȓ"мőÞɶËʍơĞԌ',
                    'description': 'ƹǓŨ¼ɰ ǊͺҲ˔ĄЉųϟÓ\x87Ӽʆ˺ǓşǤό˄ǅǇϊĉЛ҄',
                    'value': 'ǤǛƭĉЫɇͰьȡr˻qȱВ}ҙĝҨΦҚ^˙ΧźȽȚӢĬ~ς',
                },
                {
                    'key': 'ƫPńϴ¤Lϭǚ\x98\x81϶҃Ĳұϸз5ǢЭθЋΪςѳӃΣ',
                    'description': 'Ǽďϫĕó[ʿʨϏɆɫȥɔNХǩӨ҄˄ЩȲ·ɹЕӭɎӉKʳÇ',
                    'value': 'ŠϴŐʟİΫʩҶΟƬǂ҉ɷѠΰȠ˟\x85ˊ҃ʢтʗɟĀАʨѫǵԐ',
                },
                {
                    'key': 'ÑƾңȭˁʍЭԋͺϑÌТаáүHԤĲΌƋʲ\x9aҰШїéǗҍϯѦ',
                    'description': 'Ň\u0379ѤҷϔћҬɜԀԖȖűƺЃӮʑЉΟоĆ>ɅЌƜőƖɰ϶ƍˍ',
                    'value': 'ͱml˙ԣBBǼɭŪʂҏĥǭːӪȋ\xa0҅ҿѬĢβʞFƉIŻĨȤ',
                },
                {
                    'key': '(ŴȕΥƾƑӽϰȒɤɧͶЇsĈȣŁ',
                    'description': 'ȻмƿҘϟʋëӏśżӼЉ˄ҊƿӒdƕƇ϶ҠҏϫԆɽƇȲӛЖĈ',
                    'value': 'ΦˎEʝϖJӜũҳʩvlϏÜӆ»ӳʝΌơȧ{à\\ѧǇҍǜ҉Ӣ',
                },
                {
                    'key': 'ɉ\x8bƂȁʆî˧ĒĄɞ˄ǍŌɝЪӪĀϕEԬƵ˩ΑѭFӼӣ¥Юˆ',
                    'description': 'ӿԅζр0ЦԇΎÏЛѯϓҹ΅ˁђоӷИǒӊҨкˮˮӷͻΣάƃ',
                    'value': 'WUƮӼĬ\x90΄ƄƛϳӔѰ˕ŭϔΔӝȓ˩˕UϟӄςѿӺǎЗѩʘ',
                },
                {
                    'key': 'θҨΈĦԞ˵ǜŹҟӏǫДͺYͷǘΓӡŨĨѫћЂҨÙɿŏȥψÅ',
                    'description': '·ĥιӮґôÎтίĿɨӽǵƼȔȔҳӯĈȩŌŭȅѥť϶ŀʼʩƺ',
                    'value': 'šȜ~ʻǙ˵˛ɔ˫Ǵ°ѤļʂҭÛсÛÁɴˣБκη3BсЪȁӨ',
                },
                {
                    'key': '\x8fЦϗ ϶сĴOϥPõЌБώǚÄʻ˕ΫӴŜ',
                    'description': 'ϴ\x85+ʾƩҔąЯƾЩɻԔŐʻ˓Đř÷˱ɾŊ˛˂ʮɉ\u0381ħø¥ѓ',
                    'value': 'ǉőϔŰцϷ΄УʐԎ\x8eʼˡ:ͷdԆҕԋɜӿ\x96ŤôѴʦNͼ`Ѽ',
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
            'window_id': 'ɓÞϴήщTcżӞȭѦŜŖӺĕǂ/^ʉΣ\x93þџ±ȩϽѼĝȬǼ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'Ά;ºԂ³',

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
                    'window_id': 'ªȶԍҚŪĒ\x91ȲΣʝɫð_1уʮԤ҉ɀ9ПҵȚŀ˹ʽӆ˼ѵΚ',
                },
                {
                    'window_id': 'ʕˑÔùƽëǣԃÕˉφҹαpÊӗʋǅɂΑɬɆόȍтνͳǲŞ˗',
                },
                {
                    'window_id': 'ԫтŪĶќҒgʣι˗őϱǳԡˡѝȆɁЖӜ΄\x97ӭϟϦïǽǒǳĂ',
                },
                {
                    'window_id': 'ԐӣѶЄʻŝаĞчƷ\u0381ЇŚŃЄԙŉʞ4ӚɪʯʣҴłɨϕͲƣ',
                },
                {
                    'window_id': 'ƍǱˀȈʶ϶ϴʚŊƀΏĻҌBɕϪӷęыk°ΕƜŃмԊųǩǩѺ',
                },
                {
                    'window_id': 'ÖȰʋӎΞƑɜfȍ²ƃĒ˟¸yȒ£ĴƖƙˍZ\x8cȉѕԤӔѡǝɿ',
                },
                {
                    'window_id': '΄ò˳\x7fjȘŅ˪ӹíʖҿΟ˳҈ҐɃҼ@ԢňɉϱаїԒɶ`ɟЁ',
                },
                {
                    'window_id': 'ҴĘ҇ԮɎÏąе˙ǀӱʭŻϷʍʉɳ~ƀҕԠϽˬ>ǞɶȃÓɋż',
                },
                {
                    'window_id': 'ԪȀƐ°ӐŠŸѯÂȃӓȣƇԐĕ+íʷëѡφʣѝңдǣBǺͺɆ',
                },
                {
                    'window_id': 'ĵÁʪԢԭз?ÅζŔɿрɱħхɿˑԊηėʰҫǀʳĘˏϙ\x89\x99Ͳ',
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
                '\x9bӛǚʻά£ԗúѦɺʏɟ˘ҭĘΉ÷Ӻ˫Ϳłʟ҈ĢɣÉ\x9aǱÆǝ',
                "ӈԡɎҀӟϋӒǢģчӺȝ'Ѯςӳ˷ɼSŤǖԒ\x85ŝұБԨрˆƱ",
                'ǹȉƸ\u0378ƁѼf]ɶ¥˜ǗМþĂͽĈϤŗǵƺå2ǽȐ,Q$ΰΐ',
                'ɨ0ЙҗŰíŔҏϗƞяԆɴҌѶλԖ·ЄǕÀțŤÂê\x8cԔȮɅǶ',
                'ǂвӯϮƚųȇ\u0379ПͿϥəïɉМȬöƼʹĞЖȔȜξҗѯ\x95΅ίҤ',
                'Ѐ\x90ӱҶÊԦԘ\x7fʊƁÐͰЛ¼ˀ\x7fȹɑХңƸƬ\\ϧŃҢêǎɯz',
                'ȖǰĩŤΔӤ¿ӑʳѡШҽ˻ϜĻʙ©ȴǙѣ˩Ωԙ¬ĸƗѵηƻ\x80',
                '\\жϣмǌ>ɘþӀͳєϷΝþǗӁ[өBɖ͵?ě\x88E\x8fЈͰȞğ',
                'бγ=ʥʹΪĮʘш®˲VɭǍ=ҪȄ΄ҚʀʰУʾνӑÁϒËωW',
                'r\xa0ϐģЭƜӾŕкďȳǮӌΝŞ˲В˜®Ќ\x88ŋӼƣϢϗҠԏDУ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'îʎϢɧȮ',
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
                'focus': 843,
                'parent_id': 'v$ӣsςНLŨͼĉŪΞçșνϔшҏγ"ɮĆƧȒ&Ƭζʹ\x96Е',
                'location': {
                    'x': -5336085618469355301,
                    'y': -8644068163842469993,
                    'width': -6324077046082635065,
                    'height': -1304434247459660636,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ІÓæǊȳӛƶνԇßJԔƤΥ˹Ң\x88ԧ˅˩ӵò˱ηɊőБ(ƶԟ',
                            'description': 'Ȯ<Ѝë˲Ȭ\x88ŋǲ˦ȕ\x90Wҭμӯɱϟćԟ˽ŵI\x8e\x96ӹ͵ЩȝӜ',
                            'value': 'ąό:ԛ˚ͽϫêɨѣǘɸȀѨƾЃíƗŎпѹǴȜѶΩɺσʎҌͻ',
                        },
                    {
                            'key': 'ɮҢǭÖŝǉͿČȅ)ɗȾƫȟʈʈʽʦŒȎҀбԗŶǛЬфʇ"ŝ',
                            'description': 'HȏζχҘ¤\x96\xadǕËƳűɗʙӋUͿѨƺɟʀÐǤȏȨƀ϶´Йˇ',
                            'value': 'ĶҾʑȞȭȿԣ˰ȟJь˕ƴχĵƒƄwҚȐғÐ˫˕ӜʋѾљѩ˾',
                        },
                    {
                            'key': 'ӵΙ\u038dǑǺҴďɶӢ',
                            'description': 'Ɍʑșfԝɗѐȓ(Ϛ\x97νʛɓΩǉ˻ʔˋƒŞǂӒҹЭGΩȯϵý',
                            'value': 'ΚƍзιĿđȼƬӌɨpӞ7Ⱥ˱ʥɵӗ˾ЮǵƵɸѱΨʲӭҠÌě',
                        },
                    {
                            'key': '¦ϻоӐһ\x83ǸΩǪżη®ϦƢԎҷӻåɁŜίӾǸŒ\x9aɹďǝĦň',
                            'description': '\x81ζQŕÿǜèɞĢǓϿůȁŉŽ.ĵȹĈƲΓѵәӭѫťɽ˶Ԏԕ',
                            'value': '҆άϙ҈˘ŷeæӱǖҽѲˤҖɏÅŅɈĳέϛ[њϥ«Ǩȫʹ·ƌ',
                        },
                    {
                            'key': 'ʒԡӦͿˇԞɿʯĄҚˡǻ>ρ\u038dĵǿнΖұʻϙҖʨîӮɖӅԫȄ',
                            'description': '҈ʹцҢәʦǠ*ɟɭĄ;ӭ˔ǀԡοҜȆ¦ƩЕҟКZƯҨϤǴƶ',
                            'value': 'ѳЋIɽҩǁ´ɋǶыļ\x9cĕÀҹƧѸBǌԖʹЌ>ſό3ӗϩӉș',
                        },
                    {
                            'key': 'ĭĳΨŖ\u0381·ƍӽƜtԇjųӯϦō˫ӥƦĄϢ"ΊŝіĐѢҒșҿ',
                            'description': '¼®ϖǙÔ\x89åҍӯƕɋг҉ǳԜEӍүĉxǏjǗӫ:ŖӛmŻʝ',
                            'value': 'ʒͳЯžҐДǈȨϢ\x9eЉƬЫðz˺Ţ!~ХŗǆϾȣƥԅωƿĸ˙',
                        },
                    {
                            'key': 'ϑĥϊʎȔȬ҈ѧʰԔԫӶãǝȐХБÊȄǱƦЬѧϥҸw7ĸѦƬ',
                            'description': 'tэπʬlҳōʥϦë˽Ʌ\x94ȨȚƈϽ\x88RvԮÖЖǄп\x98ʊΗėŻ',
                            'value': 'Њƺƴ˱џԂɁҍлʎѧÞɊϹǉԞӫʀŒķɨJӇʐȞϱ\x8eI5Ǘ',
                        },
                    {
                            'key': 'ĔԚӋΦĝÀԖѠӌɔɷ',
                            'description': 'ȭʳ˭ÎʿĽԙǋ¾ҮΒҕҥԨҹѠи§ơǥ\\ÆnϰѝԂҢ4үɵ',
                            'value': 'ζĭɞñĐWȉǏͽηȝđŝХʯ\x9a¿īəѮƐ\u03a2ϔɂ×˂˯ʉȟԐ',
                        },
                    {
                            'key': 'ȾƈʬͿƑņϽįӉȹǻķǤƑȑдʧɛѓʭŖԬԑăeȯιΨ',
                            'description': '˧ǊΙʒüҩǊӏfŜƂūȇēαʹǟҦKǯχӺŖ\x98ОѾ`˵ȉ˳',
                            'value': 'ăȬȑŦt˵ĻµҌǙǡěƲģΣrӧȟΖɛϡНøԖѐьԚʆŨӎ',
                        },
                    {
                            'key': '¾҄Бw\x8dρ¨ƎɬϙΉʈӌƩɂťhɱϺЌé\x85ɚńϖWНɎ1Ҙ',
                            'description': "ĝʲȀ˖х˃\x97Ȭ\x9f˚ƑПȓ\u0382ǏӳЀΝEЌƂȖр'YŶΠԓΠđ",
                            'value': 'ɶгǖǖÉɈʜVȿšŝ1`÷ƃɽ\x83ȼɘǷ¹ЃƤıƉϠԏǽиυ',
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
                'focus': 748,
                'location': {
                    'x': 5083800717882699995,
                    'y': -1050413271453304255,
                    'width': -4474069120902611946,
                    'height': -6101425506167551151,
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
                    'key': 'ίҠ',
                    'description': 'ИҋŏŔƅȀŰ¹ǊǘɚǊŕʎИͿʠñF«ԍ˨åȰɬǧŷȏvͺ',
                    'value': 'ŐΎǨƘι',
                },
                {
                    'key': 'ԞпzҬ~ӈÐ¾ԩЏùʱŮԁƗǛĮÿ\x95ӊǟ@ĀƞӈƠŗʙKԡ',
                    'description': 'ÅŃʼ\x8bЫԞĉѪwǫƺ%@ҙԅȊςϳˮǉтHvmȺϯȍƞŃђ',
                    'value': '¡ñȽ7ǶԮ˖ãūČ\x9bѾæ˷$ҦÈǕwŶǥʅǇɃ1ϧđ¸бŽ',
                },
                {
                    'key': 'Ćˠ˅ĞӁйΦ°ıʘʷӜƠnǆ˘ƾ',
                    'description': 'Ű\u038dΑΉÓʿȅwӔǢǞǷҳĸŽ˯СΏК[ˤіˮǺfʃëȌŊ%',
                    'value': 'Έύ˴ʾůÂѕϻ%ϡŰХаǟBԢCBфʏ\x99ǎ˝ŵϹȡһçİǵ',
                },
                {
                    'key': "ĆšԚɫΙϟʙâͶŘăϏϹӭâŒϼɗ'σ",
                    'description': 'Ȯ˖u˸ő!ЩϞԤҫЕсLɠРΚʖӒaҵƼɢɶӍΦëпȓ҄Ǡ',
                    'value': 'ЮɯæҔъ²ТһĜȂ\xa0ϫѽϱlÃĺǫ҃ɺΛ\xa0q\x9aЈѭϬ҈Əϟ',
                },
                {
                    'key': 'Α×Ìρϟρƻwϳ',
                    'description': 'xúƝӣÙə\x7fȯԀɋаєƷơʑĂÐӽ#ǩvѦάеШϲŽҏ\xadӆ',
                    'value': 'ĥĀόЯϻԥ҇ʼȦ±Γ\x93ӞΆPԞ½ԨԢŻ\x8cЬϙлηӍӬЊҩ4',
                },
                {
                    'key': 'µɧƷïɺˎ×ÎȌʖΎЛщ¸ÕȻѰђ`Ь9Αέ',
                    'description': 'ɒ°,Іˑ\xadΈšͳXˣРƎǲϼКԑҐҵŲŝɉŋԚ`jҲʴɺЏ',
                    'value': 'ӑӴēhɚҴԄÇϖӖФůӖZϽύˮͳʥήȨЅƠǫϰӂǋǦԪϿ',
                },
                {
                    'key': '\u0381ˡȞYĐƯŗҋǇƕԧɷūƩЯʪº˄\u0378ӿϓŚ]ʳӿӺҲɫȮԝ',
                    'description': 'j\x8bӐѨƅЎҠԒѱΐΓŔҺΚƗȓ\x9e˧ϴҦˡʓɦь΅ҿ ӴȩƎ',
                    'value': 'ʹ`ӒǓѱqԎӬƮhӭрŻσɄҬӝԑŔŊ¸Ѕɴǡ§ωȘğΘŪ',
                },
                {
                    'key': 'ɳƼǓeΜʆơϖƝǡϝȌÅρϋű0˫ǄЖ',
                    'description': 'ǠѶɥϒȃÝӦχϖõ˲Ηϕ˴²ƍJјÑӟơǪЙћǥáӧωT˨',
                    'value': 'ĬȟҪǏʜəWɛƶǌ҇īԟɧш\x9a϶˹ȍ;˃ТΝ\x8d·қ¸ӬʦȈ',
                },
                {
                    'key': 'ʶЂ(dKÞ',
                    'description': 'ŶӠӄӋȳǏͼԂѬΙʂGНǊƑҙŁĉǹȲҜɜBɈąϩÔƦ¢ϟ',
                    'value': 'ɪȟϪԂϞΚԣż\x8cɭѩЂǂɈЬÌêİƾ˜ӎӕɏɠǵǼŴ\x8aÁn',
                },
                {
                    'key': 'ĸϏѡĕ',
                    'description': 'ǀԋӉЋɉŪіíΎǛӗʡӂνOʀĚÙËǄȺҊϱ΄Ԫьȭӈɲū',
                    'value': 'ȦοϓҜǯҜѵтŐʐ¡Ƞő˽ĤԪɷĨòǧʅѯϫǦ҅Υǐʫ%ɭ',
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
