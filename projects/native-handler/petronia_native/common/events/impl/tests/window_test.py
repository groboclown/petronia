# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-28T02:46:15.305939+00:00

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
            'x': 800740904613907326,
            'y': -4844580933679434310,
            'width': 5812860711515869945,
            'height': 921393359080297383,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'x': 8840827512776384819,

            'y': -7887398670006555832,

            'width': 3293626775761455410,

            'height': -6594590910547344093,

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
            'key': '®ːƸ\u0383ɣόҘǫΞŕвνʦӗȢȨ˷˺ԝѣɷsʈͳςɤɣšӛ҈',
            'value': 'Ͽͺϥӝ˭ȨñȅŪĳô\x8bøӭă4\x8eζχȡΝǅƻѰú©Ġëˣʛ',
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
            'focus': 1148,
            'parent_id': 'ŌŪЪѓϬΗ\x8bϻΙ\x87Ţ҈ɔϼʄĂ³\x90τҌƫ¾\x9b\x9bôˤøÙŚԕ',
            'flashing': True,
            'location': {
                'x': 9171058961302081159,
                'y': 5169693088545200885,
                'width': 3252803616187300812,
                'height': -24867060726289516,
            },
            'minimized': True,
            'meta': [
                {
                    'key': 'ʾČϼӅɼњʸȾǡøЋȠǣҫШУßԮѰМϡїǝɮ»р9',
                    'value': 'ŗɖ҈єʽŞ7ѰɜƠӾ©°ЈˡǗʑϽʸтԫ:ӒԚêřĭҨуϬ',
                },
                {
                    'key': '˥ӿĘƎõϺǰÿҵǔɖҢѪξɄĩȾ˸ϗȂƴÃѴΕ·ҢĦʫŠŤ',
                    'value': '˖υȜČϛƆŢҪƂѶˢв°ɾӰΑɣĞƴӓʖYǕʟɇͺĶӛҶ',
                },
                {
                    'key': 'ӡiȦҽØźЊ,ġu±ɘQùĐ\x97Л\x84ɍ\x81Eӳ˄]ʙɖŰǬħǤ',
                    'value': 'ԖÌƒʺǬɳːɿΪԍÍҿȿ˱ɾ0ωǜƕǛõ˲¨GvȦєʐ˝ǃ',
                },
                {
                    'key': 'ǲ˛ɒɽѶɴӖ"ǣҨɾ҈ƒʬɅǀʍ)\x87˚ӞÇƦ0ӭКƍáԋԆ',
                    'value': '҃ĮώęɤʑʳÑ/ʡʒ[ϹіԘϕҗҍԪŅȺќЛӾȻÂǱȇɥŸ',
                },
                {
                    'key': '×Ô\x92МɈ,Ŵō~<ŬЫҭVʠϯɀєƊɛеӞȧȟԓ\u0381ǻƽʆ',
                    'value': 'ϕΏ\x97ǯʘͶ§Йǲҫm\u038dĵ\x8bОϏƈԊΦV˻Ѷдőғħ¥ɆƔ`',
                },
                {
                    'key': 'ЧňĤźӺěѐȹȾԆmơԣ˻ĖΜɜǮǊͻԄӂҺ҃ƼˌȆĝђб',
                    'value': 'Ιȹȡԩ˽һЉƃ½ˮМѐФ·ƫʹΐɞʜѯǶԓѼÏӗ\x86ĪцҊP',
                },
                {
                    'key': 'ϚȗЁȋtÏ$lԏўѽʄХQ΅нɓƍΗeѥġ3ŻӲ&ҽ8Ƈƪ',
                    'value': 'jћñɭԈӤŀϬΑӦ\u0378ѝÔǌȇɊӼņ`ǣҞǐĖѽȑňԒō˧Ԋ',
                },
                {
                    'key': 'ƮӣԛмћÎθҀɣȨψЎǷǔSУƼǃцŷĖ|Ĭ˨Də"î.\x82',
                    'value': 'ǤƎ˹ѕήϋɸИЅѫBȭ¢2ùȓΐβѻӽτĕɍ˞Ӻɛ˨ǊНü',
                },
                {
                    'key': 'ŅҚĳɮƊӁıʨ˵ΐӟӇӶèӸˍˆДƗϻů\u038dѬϧɓÑɨǱΥͻ',
                    'value': 'ĹͿԓћ¸ɔɴɾCʚψɇVǳӵѱĮяÈɧʴ\x98ЯßΑǕ¦Ŕ;Ğ',
                },
                {
                    'key': 'ɰԝªҺΗũҟӚѭ˺иwФѶɀPрϻđӑӄǂțΔƧΫнϺΔů',
                    'value': 'ěѬ҆ĞAη¬н.ʿʑ;тĜƀůӢȨ\x91ˡ:ŗΛːҲg6ĭìБ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'active': True,

            'focus': 3897,

            'flashing': True,

            'location': {
                'x': -8458622404849870331,
                'y': -4923028491809466062,
                'width': -5710850213102664265,
                'height': 3469408142106928763,
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
                'focus': 4983,
                'parent_id': 'ӽǂșѧʌȑ˦îԉşĈƀΘʌƐͿʉ0ɘĕ~ŋĬаΒĝư©ʽϘ',
                'flashing': False,
                'location': {
                    'x': -4852395463184874038,
                    'y': -1892882458236128201,
                    'width': 2547117630991179096,
                    'height': -4656196798285787606,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ÚÁкȸ\x9bȥҷӌԖȤѮɦĭҡŇǞԍƧȉĶ¡ǩʮԅϻΛòΊԦǊ',
                            'value': 'ÅϚƜ\x84ЃΐΰԎ?ǫӸˮѭ0ы~«ñþ҅ë˾ʘВūϞʫɓŪӦ',
                        },
                    {
                            'key': 'ęҁ͵ҽзȽӀϰˤʦέάѭȢƹЛγ\x82ҔϥÔǛš`®ҖѱϞ\x89ʞ',
                            'value': 'ԬϣhǎĄАʙɣƱНǚӹХƒлӇɛƽԧǝƐјɿԩͲƘșғǨ@',
                        },
                    {
                            'key': 'ʲǍμщǞԫƅg˻Њ\x96οϺĲώƉµΐǵ˄҅ɁÊԄȬɂďɆ$ϱ',
                            'value': 'ɿϜǖӷĖƮϱīϻʽȿэ\x83\x94ϔӘ\x9cԏ\x8dцͱѼȻ\x7fĹǌʮήmХ',
                        },
                    {
                            'key': 'Λǜ\x9fƹζͶ)ÈŋǤъʈāԄΦҶƚƑԜǏΟʭкǔ\x7f½Ⱥɐ˙І',
                            'value': 'ŕ\x8aГӛеͺȧƳć·ÆɥΚ=ɆϙyƅȚсȝ\x83ʔΜоF\x97αңԒ',
                        },
                    {
                            'key': 'Ė1ԋɈӛʾԂӜȻsĚǔϻрƴ¤ˇxù˶Aʿ=(ѪЌŋÀаq',
                            'value': 'юʫÀί¹ǧʐвĖ\x87áƶψűɲΰЌͿƬєіȶɣҮІ\u0379҆ǽԦЩ',
                        },
                    {
                            'key': 'ϑ˸Ҭяˮц¤ΆˍGċřǟӞ\x8f¤΄-їŲɕұ΅˰ǖӆkʛeˠ',
                            'value': 'o҃ːȅǿϳEƋӛ\x89ƉÌ#ћǪσөɏΠƼßϔ\xa0ĺЍϛҩτ˞ҝ',
                        },
                    {
                            'key': '˥ԝƅ˲˂ʸΩӸȇ҂ɚȋȪ˫ʘЧтѣ˲ǏȂ¯ɥʊɹ\x80ĊƴȈƼ',
                            'value': 'ÃǼϣǏèĘʝƗϡʔԜСŮƻãȀӗĢȈӶSÂʶÁϰͱĻαЬп',
                        },
                    {
                            'key': '«˝ȶūÑǕҳ\x8d\x95\u0380:żӯ˟ԟĂƈñ[МɠӅˋ҇ƿˋáϨƠɦ',
                            'value': 'ЙРˁќÑ>ĮԋԨĲǪɞʆԪʐх˞ŸЗψО҉ɨбŤҭőϑɮƹ',
                        },
                    {
                            'key': '˛дƿĘϰʓĊӃ"ǢǰȎ˳ʩ҃т˙ıʊĊʄȌĖр˄šĨһÙĒ',
                            'value': 'ҟØʣŁŷ\x97ȸű_Ǚϸ˘Дҝ˘ϼɎСӆśфjлх˘ӄ$ɀ»H',
                        },
                    {
                            'key': 'ҡGĨɄӿЀĎӥ!ãwͽȲʎҵΞИΞťÛǭϞϭέǌʕҲωϓ҃',
                            'value': 'ϷǞ͵ȱѰʡȰ˶ѮǝӤĞȼɥԄӫƬȭ8TӜхȢʵhеСν\x89ǥ',
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
                'focus': 7870,
                'flashing': False,
                'location': {
                    'x': 8834648259259036118,
                    'y': -95366180761229674,
                    'width': -4104062624072085672,
                    'height': -6294904168670451213,
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
            'reason': 'ɦƊɄѕѲǤ¾ƤæӺʗVǣԬĉǩǴƇŰ\x87˲Òλ¯ʽØöԧԇϡ',
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
            'window_id': '¾Ϣ\x9a\x84ɵ;ʌȚȂ΅К˰ţӌѹʮÌѺϠŇҚˑĳл cýӝѿɯ',
            'location': {
                'x': 7613932527508466860,
                'y': 4580892650226600011,
                'width': 2840537788093478351,
                'height': 5666462939302248021,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': '˛Ǎƫ³Ɩ',

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
                    'window_id': 'ƨƙ϶»Ǧв"Șѓ\x8dˀΌ\x9cTŻɀ\x91ÚĦϷϦǺóϢġ\x90їȱȢ·',
                    'location': {
                            'x': -7405130838426688290,
                            'y': 627009817947455365,
                            'width': -155124173143994528,
                            'height': -8127885312183747140,
                        },
                },
                {
                    'window_id': 'DǑ\x96˦\x8dҐЯ˞ԙǡ®Ćŧ˹ҨԏȔѯԅˇ\x80ʓΙȚрʋHĶ\x90˜',
                    'location': {
                            'x': 8672094064689293908,
                            'y': -8694097697742450383,
                            'width': -7770297908546359875,
                            'height': -7301610184582967429,
                        },
                },
                {
                    'window_id': 'Ǐ˷Ԥө\u0381Ç~ԏЉºĠŤϰήӳǊ\x8d1&4ԅ¶ʪŨóːȬʭ¸S',
                    'location': {
                            'x': 7076503490947234782,
                            'y': -6502897995815447535,
                            'width': 7141673334660999725,
                            'height': 1306797958974734351,
                        },
                },
                {
                    'window_id': 'ԃ΄ЉrxċʏǱƧ˹ǡ˗Ҏ҃~ſǙІȋϖґҸĆϩžʎǵҴˤӧ',
                    'location': {
                            'x': 7461843982489014864,
                            'y': 9012982871518824265,
                            'width': -6080683031537832130,
                            'height': 3631767008774309813,
                        },
                },
                {
                    'window_id': 'я\x84Ӫɬή»şiǅôҾȿŭɹ˴\x89ġXВԌӵĲΩӑ΅Ζ\x90·ɶʁ',
                    'location': {
                            'x': 7577603599700772964,
                            'y': 4651286154083788860,
                            'width': -3173735620119870064,
                            'height': -8728378811424830549,
                        },
                },
                {
                    'window_id': 'DàńыҿӀƫώЌ,ԣσВïГ˘Ȗęǁωȟ\x8dZȚεӬĊΥɝƛ',
                    'location': {
                            'x': 836523147640641872,
                            'y': 6300515719041092949,
                            'width': 7963836483088264837,
                            'height': 2359429983360538959,
                        },
                },
                {
                    'window_id': 'ԔƪΫѠͽÔz҆ˑϰҎҹʘ;ŨɆҒʂҠԪӺǋѪͶĜϩҟ£ДA',
                    'location': {
                            'x': -3752879901202457548,
                            'y': 8224009445225303350,
                            'width': -2262499047885586676,
                            'height': 3049916217966383528,
                        },
                },
                {
                    'window_id': 'ɓΉøϐȋԎi3ЄıѽċȀΙƶҭʣҸԕZǊϙϡħŞ2·ЧtΚ',
                    'location': {
                            'x': 8078873528050374517,
                            'y': 3047486209777782847,
                            'width': -7479638101365877571,
                            'height': 3436924043224573996,
                        },
                },
                {
                    'window_id': 'ěҗ·ȤʭдλГĥΜɶ§ʾ΄ӻА˔ǜˮӡҙŵѥѓӇeӎüƨϕ',
                    'location': {
                            'x': 1293641267770395996,
                            'y': -693167453501847013,
                            'width': 269383039444291713,
                            'height': 4965191624283337434,
                        },
                },
                {
                    'window_id': 'œ˟ʩԀ\x8bŭύXˋȢʿɱӍƊĥԇǜӔЋԥԕҗԠƞӝЂƭÑˈĄ',
                    'location': {
                            'x': 9040010746747453336,
                            'y': -910800552239471021,
                            'width': 8998019154618854667,
                            'height': -8470388882794645892,
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
                    'window_id': '¢ѫ˲Ξŷ',
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
            'window_id': 'ŀȂÖŻΤħάͶЎŝПň(ķēžǔΜјҠçǗȡӣʤɶęɋǎÊ',
            'keyboard_focus': 9410,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ɣVϹҧȥ',

            'keyboard_focus': 6543,

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
            'on_new_window_enter': True,
            'on_window_event': False,
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
            'window_id': 'Οɼ\x88ʧъ˦ȷǖ\x84Ýиҭǂ\x9eÀÛWҩ\u038b\u0383ʪˈ®ʙŖžȿɞьД',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'window_id': 'ȮИӑϦӟ',

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
                    'window_id': 'OҜϷŕƚžʬΕyȁßÿ\x95ǉЙԑѤņέƢԊʤϠȸĿůǰԎ ɜ',
                },
                {
                    'window_id': 'ΰʨȰьȩ,ԤŇĖɲԢŏƱÑӉϐƌɖÒҭԦ!ɁѨɒǱɹŌËˣ',
                },
                {
                    'window_id': 'ЀШʬӌƽΖǪĺӰł\u038bŀ[ĢдрMŧ˦ͰуɜȬŷϞϤΜѿ͵ԫ',
                },
                {
                    'window_id': 'ɗԜˈêƔͳŲƬŅňαɵӏӺÛɱԋΐ˗$Ǻˁґɺŉԫ\u038bÏɟЌ',
                },
                {
                    'window_id': 'ƾςųå˕ԦϜɯԥχҹęȵҽɗԓѽûƁʲ_ԦʩʡʷİǫΗҠϣ',
                },
                {
                    'window_id': 'ΆȒ˟˻ƁđrŒ¾ҫŪõtĀɤΒͷŭΓҶɨҭƃKΙйӀ+ɯ\x96',
                },
                {
                    'window_id': '˱ƋŖʀĻżǬϸѢƽФԐ\u0382ѓ ˾ʍĩҎϤҳҩЅɓƎӵĺʻѴǺ',
                },
                {
                    'window_id': 'ӎŏХ\x87>ϦJ\u0380ДʭЩbʢ\x9eԖфĹΔͽПԠčƋӦˉSĀƿ;Ƚ',
                },
                {
                    'window_id': 'Ƌ˽¨ЀѣЈƹɴθӠјԅķӞьҽƬϟ¢ҽ˜ǷȐѽˋɴҐȣȊˤ',
                },
                {
                    'window_id': 'ҌǽԖуƤхɩ\x85ѨŐЩɑΈĝԧȽKԛљǒХŢΞÔј\x80ӼƤɌǵ',
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
                'ǌʋ˼НФЪ҄=ѷаʄЄѵƞсχŵӨҞΞŸӳϱïȃʨůɥӾЄ',
                'ӐƆΦȟ¢Ȥ¤҄¢ɛҷ\x87\x93ɯĀȥџʋѦSƩè}˽ԓƀȩ ʃЍ',
                'ċǭǊРȟюϱ˖˰nćëǯƝĻѱΊƈҪKŵˆѬňΐŀµŭʗς',
                'ƔȴԨdʆǿҨϐφʝ˩кčҶǖӒɡͻȧH˩ƫӤӁ^ʝ:ȸʋȀ',
                'Ϋς\x85Ìt@ƊˬϒʛȇĳΟŗɹìƋѨҴѸɒǽǣҚɔȸ;ĴÅŻ',
                'ƈЈϋǋˑωͷƪЀкśқŻȋƮǩȉмҼȡ?ѝoŞƄĂϿzɖ҇',
                'ʝ.ӓ3щǻѰ:Ӑȯ˝2ɉƔүPѿЮҩIљɔϔˆĞɤӖ˟Bʹ',
                'ǎԒŞʳàÒҮfԭʆɂ˵M&â ',
                'ӆjѴϮʅÚaOԜӦӨǪƤƴ\x9dѯAËŉɅ[ԩϠǷ*ХɍǏќė',
                'ɽ²ȥȢƻɐАҘɢɏǉkɟɏƲʪ˂ɖԇύƻcЖӊӆʓ\\Ќ@ҧ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'focused': [
                'GѤӎӱA',
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
                'focus': 120,
                'parent_id': 'ʲǩϸȥъӇҘүí,ʀѕʹYИɖσϐΡДČƮгç%ЗԓÝӓź',
                'flashing': False,
                'location': {
                    'x': -1542208407158826501,
                    'y': -8035781052812326265,
                    'width': 9094759380440864102,
                    'height': -1084276561567970364,
                },
                'minimized': True,
                'meta': [
                    {
                            'key': 'ϛǝҜȊɃĲаĝΉɟƦȼʆӀŵ҃ҙѰGΟĤŎ˻Ƨ¯ÏâϘϚ3',
                            'value': 'ϳƱΣѺǭǏӹӵxɼþWÞ£å\x8bˇˇӕ²\x9aʦĭƨťīǄ\xadǨʎ',
                        },
                    {
                            'key': 'ѡƵŵDԘ¥ĕ1ӟҍɅʎŷϲhпåΧϡ˪Ȍ˔KŎúʳίCЂҼ',
                            'value': '˰ӑηȓºӮ\x89(!ɁЇЋȴŪŝ¯ПӅ\x8bµԂѫĽǣδ.ӪʄƕĶ',
                        },
                    {
                            'key': '³Ƿķ͵ʉ\x85ξȣĽȞѥÇ˧3SѳҐǕǼĚg ȻƬ÷ɩǡĈį˰',
                            'value': 'ĔɤӊӋvǸкAл˩ӓ7˰҄ļмÞŉĔмЩƬŇϑԠ\u038dƐȧɮʵ',
                        },
                    {
                            'key': 'ˎҭɴȩɋʤiӣɓɶ\x88¯ƙӡ˸ȋÒδɌǵ\x95˜wЀͰϱԇȅЩK',
                            'value': 'Үǩɢ˒ӳǕ\x8bѴԒShќ\u0381ɴϚΉόћðÀѹкӏƺԥǼ¡í˻҃',
                        },
                    {
                            'key': 'ďȊǃĄ͵ɇ҅ìȧà҄ĄŦgƔāґəҭǇκʹԚβ²ȺʚTТԐ',
                            'value': 'śʙѦƍƐǾӉȤýȗǙИģκÒΓǠĮťůȕýϘaˣǂǠқƊƞ',
                        },
                    {
                            'key': '҂ɓΘƟ҂˻ÊJͱʞɊčƨŖȴԬ˸ŧŀéӓӧә\x96ćŚĴЏыǫ',
                            'value': 'ˍʴǐˋåΧͼ˶ǿōоǅǗж҇δ϶²łɇϰ_ӞZąӴψǅ˫0',
                        },
                    {
                            'key': "ɽͿɪĸ¿ȯҁʎϫѨ´ƴβ!ɎʴƄƺϧ˅˫ӧԋ?'Ͻϯ҇XЎ",
                            'value': "ӉÄ\x92ѵĂιŜÚƟȺԗǨгȨƫ\\'¶ɰЂƽȐȗўɆpǗƵЧF",
                        },
                    {
                            'key': 'ωƓÿ\x90Ԩ\x8fǞϫȍ\x86ԩºÙȽŋǣ\u0379ĥ½ψƓπæе˄п\x9dёҟǤ',
                            'value': 'yмĂӯҖ',
                        },
                    {
                            'key': 'Ѭi˕ȺϝŸԟɨʄȖƩϳǊɵǨϞȜˉɡы˼ĠȄȽȰȼϮф\x8bԣ',
                            'value': 'Εɟ\u0378.şǍȀŦӢȄζжъʾÞӉӕ҄ЍϼȔt\x91йǼǯĮђГҀ',
                        },
                    {
                            'key': 'ÉǆėҲ˾ƤЍνºŷѣɗ',
                            'value': 'ɾνжӤDИˊӟɗΙzΎ|&ɔƌ\x8dмǧДųɄ\u0380ӱǽ˩úѯŹΫ',
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
                'focus': 9080,
                'flashing': True,
                'location': {
                    'x': 6661546861929470097,
                    'y': 5368507414155889437,
                    'width': 5752877757637141638,
                    'height': 7713713404683671427,
                },
                'minimized': False,
                'meta': [
                ],
            },

        },
    ),
]
