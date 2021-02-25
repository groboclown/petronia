# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-24T16:41:12.282402+00:00

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
            'x': -5933565007976803814,
            'y': 3364922407795934928,
            'width': -7703496493274299632,
            'height': 5805477192337640469,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': 6365273730857380706,

            'y': -98198858055296585,

            'width': -3023443155004054449,

            'height': 1360716441796809995,

        },
    ),
]

class MetaTest(unittest.TestCase):
    """
    Tests for Meta
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in META_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.Meta.parse_data(test_data)
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
        for test_name, test_data in META_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.Meta.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


META_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='key', name='Meta'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='value', name='Meta'),
            ),

        ),
    ),

]


META_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'key': 'ʧǁ˷',
            'value': '\x87смƙßȑȑϯԋͼǐǛϷАʵAӞɘ\x8fȠ·ԫ\x93ˮѼЮȇ\xadǆ\u0381',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'key': '',

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
                dict(field_name='flashing', name='WindowState'),
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
            'focus': 8426,
            'parent_id': 'ңĭԀʛяzϷϖMͺēƦ¶ɌƩӈ\x85ţ˄ʫΨԚΧ$Ӡ˹×ƞΎҩ',
            'flashing': False,
            'location': {
                'x': 4706377749552496442,
                'y': 5327996159521009117,
                'width': -1434335108049153388,
                'height': 5656930893640439347,
            },
            'minimized': False,
            'meta': [
                {
                    'key': '¬ɽǕѡŻȟͼ˗ĶʨäтĩńɁĚ\u038dǓѫnвУ¸Ҡ)ԉҜƺɹѮ',
                    'value': "+ƧɐӷȰƘϙʹŘŢʝDҕ'ғγĶЛƮŁÍʳĮǤГʨӾǡҡϭ",
                },
                {
                    'key': 'ҎʸʴӯάŁȪɛӔΟƫĴ<ȧ˭ʅƣˁƦқĠ¡ƷǒǷʞ˖ϫ˛ʐ',
                    'value': 'ηȎϫ7ȰҌϹM\u03a2ɯӥĎŰáϐЙʕͽkĨ˦ìɄχҿӚкӫʐŠ',
                },
                {
                    'key': 'ɤȾûDɔԆΖǎě¹%ѶϞ·ӪƆƛ҉˱Ĉǂʊ](ʤŅȃ\u0379ӦФ',
                    'value': '˵т.ǂƩҕʵʏȎĪǷ\u0383țɍEȎ|ϐҊƛψȑԠƗüџǴԕɛ\x93',
                },
                {
                    'key': 'ˑƪ͵ғȤчӳүËʐ0ľӁƿ˴ԕȩӈȔƷξʫç\x93!ŒͽȢľԝ',
                    'value': 'žʁǕ˦ɿҡѣԅÒ,5HËåŘĞǔӥϬģɏѭͻҝYѵΎ\u0378Õł',
                },
                {
                    'key': '',
                    'value': 'ˡϣǶˡƚЮ˱\x8dńϽ\x9fһԬ˘ɍϛҵ?ɖѵθΝÇĩJʭԗͶgͶ',
                },
                {
                    'key': 'ҨŞǋƵҕÆÒҏɥưτʑʳХӘкϝаkǡɂϖКЈ{}Ν˘ƺӘ',
                    'value': 'ѠĕƶUʄʬVƏ˻ɘҤΖѸɃѩƇũ£ŊȴĢĕèИȯћ˩Ȟǟʀ',
                },
                {
                    'key': '¬ˎʵȓ˹Ѭʽ҅ćɯɈЛȠЁĚӱ?ϕǿϸȲ®ȩ°ȗʾɭњ˓ʩ',
                    'value': 'ΰҖОɛΜ˵ýˇƥˀW˚óԩҞ',
                },
                {
                    'key': 'ԭΞүİ˧кІΟʜǵԢɅϹ\x9b#кȚɹĳ1˟ƆȊƄϯɐ9\x85ɩѢ',
                    'value': 'ԇƲԚеʱҜӎãҾʏ]ǚǺ-řԒ¯ÓǖӹɼŭɮϟйȀŠɔʨƀ',
                },
                {
                    'key': 'ћǭÛɀ0ҏҒϙ/dÅɚΔüɻӨʐэ\x8fİӉʭԥǛŸқʑðϝӭ',
                    'value': '˘ҐϖϸȦ˥ҸƦЙ)Ο\x85Ȟԋ\x9fʁÄѽҚǲЧҥŸĿˍǋВaɒ/',
                },
                {
                    'key': 'ˬźν¼ώŭԚ˂Ǧіѻ˩\x94ʹʈЀȘĪξĊɺ˃ȎʙԕЛ\u0383Ƃ)ˇ',
                    'value': 'Ѩfåĵ½ɖΨ¤œϹƶɠΎҡϼŝoǴ˴ʌȖʐԍҍŽȓ}Á΄Ơ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': False,

            'focus': 5210,

            'flashing': False,

            'location': {
                'x': -2462158858556102923,
                'y': 5238322119685911320,
                'width': -8323831688797883736,
                'height': -5077218422051864104,
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
                'focus': 7926,
                'parent_id': 'ȘƎĊĢˮј\u0381ƍɸʦΕɖάʴĊ˙ƎɃˬƯòПХҷ˧ʾʩҲ½d',
                'flashing': False,
                'location': {
                    'x': 6499596618420003693,
                    'y': 8060067851908815090,
                    'width': -1295182991314054601,
                    'height': 2115412055301956274,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ËԔΞҐTƝʃфŁɛγɱύĂͱƮѮЎìъɑʤҦȪŖϡƿήѩ˗',
                            'value': 'ӹϘȱǫњѽŦĩιÿХɣʌnȫѲИΗш~ÕƅɑǺѐѿԥ˺ȹŕ',
                        },
                    {
                            'key': 'ѶıǕҰÍʑчõʂ\x990\u0382őÉ\u0381ϓɎ³ҾάɪɈӅ¢ƃʌϙ˖Ѿ±',
                            'value': 'ɤǺȪƇ˸đ¹tҦˆԟ1ǋԥŜҸѐѭŚÈɯҌŏő҉ϊѫɨǔǻ',
                        },
                    {
                            'key': "ǫ\x7fŖϋӎ/ɂΑ'ƁѲÊãӏ\x9dϰЎ_ƗҾ®ĔƄȸѸҁÔ¥ӣˌ",
                            'value': 'ĻͱО˒ћѝ²ǚѷ$ѲǣŦķЌйêĶѷ¶Ҳ^ˁʁЎǹŹYѽȽ',
                        },
                    {
                            'key': 'Ĺο¹έǟÇϠτǛǪĿŭRǢƧͻ5ļν\x90ɵò»Ӎҭ¤·ŐӁП',
                            'value': 'ђӦ[ΜÙFƛ',
                        },
                    {
                            'key': 'Īʷ\x81˪ȭ\x9eѤÅ˨ŃƦɅʹЕǒҕ˫ɖδƦӲƻӂƪШ΄Ѹџ\x9cC',
                            'value': 'ԓɞӈӓʸ3ϭїЎ˥Ѫӝ\u0379ӒJȚԈC˨ǽ±Ӯԟуʊʹlôɟ҇',
                        },
                    {
                            'key': 'ӸÜӑӣΘӹϤǃƐҩÌњʟŮ\u0381?ͿӃDŋѢîèȡ°ɿˎßһύ',
                            'value': '¢ɈЖ&\x83ͺŕ\x8eȬ˒˰Ⱥґ͵CZϴøȐХԍŸɆľɼųˉƭЬ¦',
                        },
                    {
                            'key': 'ūˤȎ˽ò\x7fk0|йÙÆʗɎSǆȽLù\x99ΛʜкƓ˝ŉƉðТѥ',
                            'value': 'ĩ²\x88ȿƧɇ϶хÌŰϙɪġȞԂƑԎѵѳΕ½Ȫѣ¼ˀqƟϢҭ1',
                        },
                    {
                            'key': 'ɪōϖɉЩПҦúˮʦϮ˭řƿ\x8aεɡЌ˂ȮšэͻϏfь˙Ӯ\u038dĬ',
                            'value': 'ӴЯî\u038dǓ˥ǒѢəʆƴӆг҈Ŏ£ҮɾïѶϬʿˡĉδfĹҶƗ+',
                        },
                    {
                            'key': 'ӈɣҊˣӯćDEѐʑ×ÇӳɚϐŦӠǀЇϲλɸ¼˄ȦЮɾӍϣÙ',
                            'value': 'ŎӲ&с˦ӪƌʨɩŖʾԨϔϴӰԦȎȕ×ı¥ĶƉĥѺӒ"èγѨ',
                        },
                    {
                            'key': 'ǜŤȩȘǻĻøҴͺɞ҈ОϠ҃ЖȾӐǜpĄҥȉйƫĒМľƩěĔ',
                            'value': 'Ţʡ\x97ÄϢåSγ4ƦŏȤǩÇþ\x97˨¼ҐŔǘŸȪσˬНñéşʬ',
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
                'focus': 4640,
                'flashing': True,
                'location': {
                    'x': -7398845387545402849,
                    'y': -5354052225021965468,
                    'width': 2996005067578885800,
                    'height': -2489740704499314044,
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
            'reason': 'ƢǑуˏiɲԀҀaҦ˼ԓ҄ɂӷĈŪʽȈ"ªĜŲeÔ\x8bǱϒѻЯ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'reason': '',

        },
    ),
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
            'window_id': 'ǚҝǓӳ_ǳŠ\x93ĽEĽěнʁҺŞӏˣԙеѤ͵²ҖɁƬkłИ˷',
            'location': {
                'x': -3111311870059531942,
                'y': 4390807759042300030,
                'width': -7862345844805896883,
                'height': 6863765350475668399,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ϣБϩˇҽ',

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
                    'window_id': 'цёЊ«ӁXѣҤ\x8b˓ɵԊOӝЊўЂǏгɗɝȈϲfǚɣԨĈȥʘ',
                    'location': {
                            'x': 8614434914323329869,
                            'y': 606909977999604486,
                            'width': -7230509197316555605,
                            'height': 2477904099548794896,
                        },
                },
                {
                    'window_id': 'Eˉ\x9cͲʹЄюƙПz єϓʬŸΟƊǎȅʣǽʩǕͱɀϡŮȬ¤˰',
                    'location': {
                            'x': 8688651159253358584,
                            'y': -1038297404590617142,
                            'width': 5568172818468537062,
                            'height': 832134739612555172,
                        },
                },
                {
                    'window_id': '\x8eҠȔ¡Ӓ\x90ԖƳƙůӉҬÞȣșΦЏ¬ҔӅ$ɒ¹$ÕÊ#ςρˤ',
                    'location': {
                            'x': 2235562047263240085,
                            'y': -7700870406214897510,
                            'width': -1827568157416858350,
                            'height': 8613152397176443514,
                        },
                },
                {
                    'window_id': 'ԕɯȦɄǑ˷ӄÕűǝQϲΠƇ˭ұԈȹȬΠҴȩ˵ŚӱĸŞÜʈȈ',
                    'location': {
                            'x': -3620648310425605314,
                            'y': 8258735382393174215,
                            'width': -4764403098827535908,
                            'height': 4690088916884688623,
                        },
                },
                {
                    'window_id': 'řЈΘҔϿ¶ΕαʻŒzȗÒѦȿȞS˗БЭʷơcˆʹϗƦƢӷʪ',
                    'location': {
                            'x': -798981691878042596,
                            'y': 5729626042759099324,
                            'width': -2945573901049604602,
                            'height': -2370546597022287365,
                        },
                },
                {
                    'window_id': 'ҊѲʟLҖλς\x93ȜӆҀ»7ǎѾϟɴĔİEƉνЛёȩӪ×ӿԋ˓',
                    'location': {
                            'x': 5127907880055115460,
                            'y': -2553762732154739577,
                            'width': 5199444912684988885,
                            'height': 7473973289477044589,
                        },
                },
                {
                    'window_id': 'ӱǙͿϬљǟѨљɅȤ§ɢvǮΜˊʽęξɟμɄιгřǓЕԍNɄ',
                    'location': {
                            'x': -3954077446097311357,
                            'y': 438354516114612225,
                            'width': -8593444496266152657,
                            'height': 3314591528845780639,
                        },
                },
                {
                    'window_id': 'ǸϧŚϢ\x9cȟӐԄǻAƂѤŠўƃӣǭǝ[ʖͽа-/ÁǌʳιŭЍ',
                    'location': {
                            'x': -3111624409193075955,
                            'y': -1024884580010751325,
                            'width': -7818005053944324508,
                            'height': -3803054621349104355,
                        },
                },
                {
                    'window_id': 'ɤƎɶȫŝ\x87ʺÍ\x94чƾơŤ˕ɬԚ\x9bōѸǪĘɚҰʉѩӼżFБӏ',
                    'location': {
                            'x': 4804658523091009858,
                            'y': -6471479840685502282,
                            'width': 4817106308246251707,
                            'height': -639395552218294559,
                        },
                },
                {
                    'window_id': '˪ƸʕЅűҤˑǑʶ˭hѪƗİчęџƑŵԁǂîƦΝςώϖȫɩƍ',
                    'location': {
                            'x': 3192983940100677024,
                            'y': 1102441493781669811,
                            'width': 1027287593260355797,
                            'height': 1574139981669634819,
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
                    'window_id': 'ҿӍҌvų',
                },
            ],

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
                dict(field_name='window_id', name='WindowFocusedEvent'),
            ),
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
            'window_id': 'áɀИҜˌЂ˔ɲΑӉȨŢɅʙԑþξЙˁǗǌPƕюưãфĺľҍ',
            'keyboard_focus': 7414,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ƍŹƤŚđ',

            'keyboard_focus': 3318,

        },
    ),
]

class FocusSettingsStateTest(unittest.TestCase):
    """
    Tests for FocusSettingsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in FOCUS_SETTINGS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.FocusSettingsState.parse_data(test_data)
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
        for test_name, test_data in FOCUS_SETTINGS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = window.FocusSettingsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


FOCUS_SETTINGS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='on_new_window_click', name='FocusSettingsState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='on_new_window_enter', name='FocusSettingsState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='on_window_event', name='FocusSettingsState'),
            ),

        ),
    ),

]


FOCUS_SETTINGS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'on_new_window_click': True,
            'on_new_window_enter': False,
            'on_window_event': True,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'on_new_window_click': True,

            'on_new_window_enter': True,

            'on_window_event': False,

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
            'window_id': 'KǠҸΑţԚԕҖӯª˄ˌͳd˜Ôh˫\x81ǯĭĂΗѕFȾŔ\x9fҰʲ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'o;ŮÿЁ',

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
                    'window_id': 'źӔǜƦŭͱ7ÜԤ҇ӣϰӋ¥ɃȄǋˈѹύԔE/-ӘԕϚàҒM',
                },
                {
                    'window_id': '£ǈȺЄΫĀƮɢĘô³ȓľ0ԁԊɂƟʑίμ\x8dζǙƶǳŇƞηű',
                },
                {
                    'window_id': 'ӄˠӂҳΓƸΧίƪΚуÖ!АχӚϊΉă΄ͼĘҨɇʜƬŞľǍø',
                },
                {
                    'window_id': 'Ϙʯŏ¼řăƨȖϻȴʱʻΪûǨƳГӮǀʟҿîР˻ǢѨĬ{ĢƆ',
                },
                {
                    'window_id': 'Ɔƾ˵Ɉ¼РʛȆgĢӮн[ˠԞųʌ\x82гΞϼŀδ(ʰʀӲìԑϧ',
                },
                {
                    'window_id': 'ȁÕ»ʓαешj£ΫҊѕ©ĀѵԈІrµ{\x9eϽȜèǋԩèĂѓã',
                },
                {
                    'window_id': 'ҭҾψɗɪȄʾӒ´őӴ\x81ϪƋʏʛɣɞƩƓɸΗÿёġSʙјφɼ',
                },
                {
                    'window_id': 'ƞō\u038bˣкƌņƭŌ,ђњρÈň\u0379ЪĀӑΩџďѡUҘ˃ӃɠȴΣ',
                },
                {
                    'window_id': 'СƃǵƙвԕяɤѷN\x96ȋɤɥϔҎϿϲɈĮӞĖŐ¼\u03a2ȭӽ*ƥʞ',
                },
                {
                    'window_id': 'ѓŕƴęţӁɱǏͺʈû\x97ʽŕϛ¢ΡUŏɊδʩĥŕǘǣєɰτɐ',
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
                'ϮҹҤφȦϫϝ\\ɩЃӰɬѳ]ӅʁҲMѕ˞˺ѝƁ~K҉ˠʽǭɀ',
                'ôӞ˩Β,ѯƄɘҙďǷɶǴιɇWjϞůíƜ\xa0ʅϳѰĎ˧ѳēÍ',
                'ΐӟnľôžhˌɲďųǚ¡ӥ¥ɤˤϑoƫχҀ˛ΓČćϙŢӦǨ',
                'ļжŘˤҘ¸ʇʩѠǑǿϺ·дιƴưѫô\x9d~ǳƙŘƖʶÏÌ0Ϻ',
                'ёÓđԓȼ˔ǩШħώźЅΐ%ēιOĉƩԮӫˀб~ˑӄŽԌϤм',
                'ηȤȃҞǷΰɌЃƛʹłΪÁìóЗōǽ@$ӛoďɋȓ\u0382þȉЏ˂',
                "ҞŰУŸѠ$Ƹ\\ѧGǢԍÀˋˬ'ƳĞɞЬƺ¡ĦɔȽϿ\x84ʋģƮ",
                '˴ʆϞʪϙǍ˖ПѼȱȈʗÝƞ[˧ѥēͼɺǁϙİԨʅͳǐɺŘԓ',
                'ÊĉψkƛӠи˯\x9fĨ˩ԏǃ¨ҥțӒĄƄԒƼƗͲ]тƈ\x85ѤȦτ',
                'ĶƋàɴѣ.θΤȝԣǬ\x99ǡφш\u0378қ¤ΗӴŷӀǈģЄ&ʚƜѥʁ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'ӅƀӗDƮ',
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
                'focus': 5846,
                'parent_id': 'ŴÈƵƙŚϤ\x7fɶ®ϮҒ˰ӰӦȞβȓĺӡyҡSʫӻԅ˫êɁǭƕ',
                'flashing': False,
                'location': {
                    'x': -2644374347157576203,
                    'y': 7253510316951574836,
                    'width': 3747112216383706906,
                    'height': 5656000642566806141,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ЎĤМѤЯǒŜá\x88ȚÞɁÀӊ\u0379ȉɤҽԋpЕȎќoǣɼƤ/Йѿ',
                            'value': 'Ƿ¥\x98\x87´Ǵ˺ȍˋŅШɚϽȄƒæɥɁÝʼ8İ˰Ϝʏ\\ɏΏ\x8eŮ',
                        },
                    {
                            'key': '^ԥξJϹЕЀíɉԎ҈ΧǸοvƶ\u03a2ǷлĔƝʤћҎʶӆŷdҮԪ',
                            'value': '®ϞĠʼӱє\u0380҃ψҟӇǏЍӖ±´ΈʞԗğȖҾ˘ʫ,ԥŜêԘу',
                        },
                    {
                            'key': 'ʃɄ˅ůʺˁѬӑѮĄ[ŰǄ˭ıǙȚɣшΗȿ÷ȍƖʹ˛Ƅӄћ\u038b',
                            'value': 'ʓ ïԠsћ(ŭƪǬʭÔ˻êʭЊđŐŚŻρȹȠŏš2ӕ˚ɈҮ',
                        },
                    {
                            'key': 'ʞωƮ˓ϿрѭӶϫ@ųʂϾРŒ҉җΡYˀ}ƗŜІȎʎǦηйȳ',
                            'value': 'Ή˨Ґͻ½жŊàԓɕӥѕ¿ҜҪpʊώϜ˙űҭƧҭ(ӁχÂϊƝ',
                        },
                    {
                            'key': '˧ӏѴľΈҨĻŗǤȟӀѤόѨǅÝϙćʌƇҳÃ8åʾƪӝʝ\x7f?',
                            'value': 'ӁƘʥÈξMΘŋηҫ;ʺƗͼĬXɛɿ\x80ҖġĞҸаAȬх΅ɬā',
                        },
                    {
                            'key': 'ȱцĺɅwϸҲѰ˯ѥɵŏɳZÏϢCϪȫƗ°ɳɉϽӞͻɛӶҿf',
                            'value': 'ůȭÿԡĵöȮµȁƼµ8ҕĤȎɴˀˇȤяǇGԚԛцӴȢӈԟƘ',
                        },
                    {
                            'key': 'ŖͰ(Ü¬ːϪÁâ%ƯɸƼǠʅ˕\x83˹ЁĶ˦ʼĻɦƩx˼ӋϖЬ',
                            'value': '҃ÕùҒāéʳ˗ԄɢƶµӾНhŕҖԙӝƷùѿ\x9aʮңɰéљԪɡ',
                        },
                    {
                            'key': 'яĩӴωϞȾʺφōΒĽЗƸʘӯ1űňԞɑҚƝ\x92ϝҽèÂʑV3',
                            'value': 'ӕӀ˔ԂцӘ',
                        },
                    {
                            'key': 'ҼЃɍʈҒԑZ˃φȧ¨KτҦşÇƌLŨʩɓǢʺԭƍ¤ѠІγĜ',
                            'value': 'ҖʣɹʤҊҼπ΅ӋƬӶ&[RȦґЉĤĻѕČŹϼůԜĞŤ¾ȶͷ',
                        },
                    {
                            'key': 'ȅʢРџĭ˜ӛɏưĄɯʸϱСԨǢԑéѧ-ѹżΛŀҞĈκůҏ|',
                            'value': 'ʌЫɠǿԅғȽƕƲť˞ɦfµÕӶɜ°ж\x95ǳ\x8fɚİŷÂѵȂǊԬ',
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
                'focus': 8006,
                'flashing': False,
                'location': {
                    'x': 3824289451783341471,
                    'y': -3700565963039961698,
                    'width': 1090887793611218727,
                    'height': -7215414197910094178,
                },
                'minimized': False,
                'meta': [
                ],
            },

        },
    ),
]
