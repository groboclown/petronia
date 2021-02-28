# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-28T02:46:14.925736+00:00

"""
Tests for the i10n module.
Extension petronia.core.api.native.i10n, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import i10n

class RegisterTranslationEventTest(unittest.TestCase):
    """
    Tests for RegisterTranslationEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_TRANSLATION_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisterTranslationEvent.parse_data(test_data)
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
        for test_name, test_data in REGISTER_TRANSLATION_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisterTranslationEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTER_TRANSLATION_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='locale_code', name='RegisterTranslationEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='catalog_name', name='RegisterTranslationEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='message_file', name='RegisterTranslationEvent'),
            ),

        ),
    ),

]


REGISTER_TRANSLATION_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'locale_code': 'еǀѳӉǜǷϗ\u0380ӊԄ',
            'catalog_name': '8ѓÖһѝŻҋҰˈȌĪшʹԝԆЭƽӟɿ\x8aФńˑ\x94˟оцɿÎВ',
            'message_file': 'ʱңʨɌҤ%{ҡDϒϸͻɝνρɎЬŅϣŗȥϯʺΫǽæ·ƣĮэ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'Ƌ',

            'catalog_name': '΄ϕ\x96',

            'message_file': 'ņц',

        },
    ),
]

class RegisterTranslationSuccessEventTest(unittest.TestCase):
    """
    Tests for RegisterTranslationSuccessEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in REGISTER_TRANSLATION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisterTranslationSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTER_TRANSLATION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]

class MessageArgumentValueTest(unittest.TestCase):
    """
    Tests for MessageArgumentValue
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in MESSAGE_ARGUMENT_VALUE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.MessageArgumentValue.parse_data(test_data)
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
        for test_name, test_data in MESSAGE_ARGUMENT_VALUE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.MessageArgumentValue.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


MESSAGE_ARGUMENT_VALUE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [


]


MESSAGE_ARGUMENT_VALUE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    (
        'string',
        {
            '^': 'string',
            '$': 'Йƥ§қѾɓȀѳǯƞbŊχ½~.Ɠβ\u038dÇӯɿϞȗƑŉŇϝ\x8bː',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -1041043119337568956,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 334998.8888366875,
        },
    ),

    (
        'bool',
        {
            '^': 'bool',
            '$': True,
        },
    ),

    (
        'datetime',
        {
            '^': 'datetime',
            '$': '20210228:024614.840576:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                '\u0379röʾ¶ҖƛŀƎưžɀҰĮůÌĔϾĵҗ»ѡɄȤƑǗͱʀÂ˕',
                'Ùԫǵ\x95xʚ,%ßŰûĦοпЬȥƵӿјĔ҇ҞӮÖ\x7fҨ˝Ϣшɲ',
                'ËČѕЧЖ҂ѝ]ϒӗƜΫƞїíѼȶϝ$ԟ¤ѤɫƥϦӞʁҒƧǋ',
                'ϣЁƷεӎĚ©ЌвԚɎʔҙϝƮ¶ѣѯâ6ԉԕȅc˖ȻӹѾƀɃ',
                'Ȓ?ϷmЖХ˛ԗӐϕƲШΈԓ\u0380ӟθѤƷѩŹƛӖōŪҐȏƲɐǭ',
                ';ІӢʖǲ\x990\x8eŤӷƨȶ`гʎԢĝȸˢǈӆǴɉĻ°Ɯ\xadɚɉӲ',
                'ƹCμԧȷА"бķń΄GČϟӺƴ\u0378ʐǦʃƓТЏɩҤǁӹŰʬ\x90',
                'ȅίԦuŎӏɸҰŜԄêˆԉΌȄǈŃѭȢĔѐ¸ѭlȩјǀкӃŃ',
                'ɋpԤ҆ĽȟнMӝ;ȂÞǗԂɿěЗɸƠԍŋƝǔҦϑ\u0378ӱĽƪӶ',
                'һɚЁΊϲӵъɬ҅ƎϨǨϛɘԛ·ƬίʎʘɤнĦÀÈөȽў\x84Ϻ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -1742636780998399968,
                -5449126302870910960,
                8362303939508956327,
                -1570916272021071820,
                8685522821307797875,
                4002505267510552938,
                1568362282784369123,
                1693642703520120285,
                6093103020055513505,
                2210776785921261551,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                253505.77304636897,
                407698.03447788657,
                609674.0618471616,
                700515.7314697552,
                43302.802060755464,
                826162.1710714526,
                880588.0667059766,
                172346.62413134566,
                406821.6419675002,
                53652.353582380194,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                False,
                True,
                True,
                True,
                True,
                True,
                False,
                False,
                True,
                False,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210228:024614.842886:+0000',
                '20210228:024614.842925:+0000',
                '20210228:024614.842940:+0000',
                '20210228:024614.842954:+0000',
                '20210228:024614.842968:+0000',
                '20210228:024614.842982:+0000',
                '20210228:024614.842996:+0000',
                '20210228:024614.843009:+0000',
                '20210228:024614.843023:+0000',
                '20210228:024614.843035:+0000',
            ],
        },
    ),
]

class MessageArgumentTest(unittest.TestCase):
    """
    Tests for MessageArgument
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in MESSAGE_ARGUMENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.MessageArgument.parse_data(test_data)
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
        for test_name, test_data in MESSAGE_ARGUMENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.MessageArgument.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


MESSAGE_ARGUMENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='MessageArgument'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='value', name='MessageArgument'),
            ),

        ),
    ),

]


MESSAGE_ARGUMENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ƭԃЅŰ0ҮȺƉΠӠļɐɩɉӍ?Zƅ',
            'value': {
                '^': 'string_list',
                '$': [
                    '˙Ǌоωƭ˯Ȟ΅ķӕѱįҷĺДȸӫ҅ҲxˀЩȊ6˵øĚϝхԚ',
                    'ĬċϻʤӷĩʺǌҫƁ7ԣûԟҲƀӺΩνȘжŦϝ=Ɯԑ˰ƿNɥ',
                    'кӎӯǭԢӺ˄ҎȏЉ_ąÇхчиl˝ő\u038dÑРÏнǨˍƔĢČÑ',
                    "Ȅý\xa0үΤĲʉϝӓөŌϕδƧ˔$ӓѡɛ΄γԀƉ\x82Ǧ'\x9eȍΙϝ",
                    'ҥŨɀʭȪ˔ζϭÊÕϽŦ%шԡǁӧɫʘvEВóϸɔƜɊҥΕΘ',
                    'ӥƔҥǲëſӼɧǴԔӄƃυьBӨǳƟ˛ªуʫϪ·˵\x83ĮД¡\xa0',
                    'ÌiʅΛ-ˢV×þμРTf˧ ӿΡØѦͷʐŶʷɍǞ}ʐʷЉ˔',
                    'ĬϯӲʮˉΈǖэюҠƘG˾Łц҆ˌ\x93ʷӶƯʞôȶǁĢϗЇȢż',
                    'ʆѝȐɉȥ°ϒ.éΜҋȲАώɛǴ;ÂЃ\u0382ǟűŐ¿ϫ,ĐÚЪЁ',
                    "ч΅'DͷČȴʜχƦɯȐǵƻϠАвԟĽʂыϵȒʊ|ҭRΊЄю",
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʪ',

            'value': {
                '^': 'string',
                '$': '',
            },

        },
    ),
]

class LocalizableMessageTest(unittest.TestCase):
    """
    Tests for LocalizableMessage
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOCALIZABLE_MESSAGE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.LocalizableMessage.parse_data(test_data)
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
        for test_name, test_data in LOCALIZABLE_MESSAGE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.LocalizableMessage.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOCALIZABLE_MESSAGE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='catalog', name='LocalizableMessage'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='message', name='LocalizableMessage'),
            ),

        ),
    ),

]


LOCALIZABLE_MESSAGE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'catalog': 'ǀΐȴн˻ŨÑcɒӺŇҊˎўϊϦʓƛјʼ\x95ɣȮÂϺΥÆы|ͳ',
            'message': 'ƖTѵϝËүƛvҗҋϻς@ÖЩ˯ѱѕԮäʡϚͼɾěɭſűľЁ',
            'arguments': [
                {
                    'name': 'ϨԪɐƑÈˤΪËEӦҀ¥ʘŪɖҙÅ\x86',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210228:024614.834232:+0000',
                                        '20210228:024614.834405:+0000',
                                        '20210228:024614.834512:+0000',
                                        '20210228:024614.834532:+0000',
                                        '20210228:024614.834551:+0000',
                                        '20210228:024614.834575:+0000',
                                        '20210228:024614.834590:+0000',
                                        '20210228:024614.834604:+0000',
                                        '20210228:024614.834696:+0000',
                                        '20210228:024614.834716:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ӞƪȄnɨκǬ\u03a2ʾϑһŐſǍ˂)ǣҟuõɳȡѫӄƶЕǲ˹Ƀѐ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'Ť\u0379Ԉϖ',
                    'value': {
                            '^': 'float',
                            '$': 717674.3150780768,
                        },
                },
                {
                    'name': 'κǔʠɭΌΕșʉËЛʳȗǄǔĔ˸Ý˥/ñʿǕʹ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                    ],
                        },
                },
                {
                    'name': '\x97ԅÔ\x8b¤*ɹϪьŦӷOґΎ',
                    'value': {
                            '^': 'float',
                            '$': 812212.8234357833,
                        },
                },
                {
                    'name': 'ȓíІǎԚɴӼfҠrԐѰȨїÒԨȩ¾īўԪ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        False,
                                        False,
                                        True,
                                        True,
                                        False,
                                        False,
                                        True,
                                        False,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'ǫŊΟ*ѻЬÕ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        794821.5498946011,
                                        464251.88539308286,
                                        216736.60950886813,
                                        608652.5429132577,
                                        -16853.589734018533,
                                        566986.2539326688,
                                        358167.5102663507,
                                        901263.9807863316,
                                        765283.038663137,
                                        -97804.43879617118,
                                    ],
                        },
                },
                {
                    'name': 'Ɔp҃ӑύͷƓԍɮƇʮϊʽΆʊԑƋӖάƉŦƮʀȗΐǾ\x9dŤɊĊ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -4830029156970323554,
                                        8518576300588737697,
                                        158496046756956797,
                                        8582733860287825230,
                                        -9001484168510135161,
                                        -2625662579774847256,
                                        -4193754657708244985,
                                        3836963789926112323,
                                        5886093484999312407,
                                        -6696893227212764752,
                                    ],
                        },
                },
                {
                    'name': 'ʺҔΫӄҋĐǃȽΈŅЎϕȆcʁ˦ȽªΐӰ҃ҎńʵȅЀҳqƶҾ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -3894668533983120895,
                                        6441070660515608838,
                                        -4174741793618503895,
                                        -1511754475758590902,
                                        -3815486232595745480,
                                        -4116756298248663838,
                                        -4314967224185347810,
                                        1569831400780406399,
                                        -7152863636456029077,
                                        2552227932808836151,
                                    ],
                        },
                },
                {
                    'name': 'Ơʉ˚ó˄ɭ',
                    'value': {
                            '^': 'string',
                            '$': '\x94Ȫ˛ΟʪơͷςτǧɰǃζσЫÈðПQϢõoɘɎШ¨ʣȨÑɢ',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ӿɋ',

            'message': 'Ѐ',

        },
    ),
]

class ErrorTest(unittest.TestCase):
    """
    Tests for Error
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ERROR_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.Error.parse_data(test_data)
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
        for test_name, test_data in ERROR_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.Error.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ERROR_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='identifier', name='Error'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='categories', name='Error'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='error_message', name='Error'),
            ),

        ),
    ),

]


ERROR_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'identifier': 'țӬǊʧϙʠɩŵŷ¶˸Ԭź\x89·ʇАωˀψ[ƟƉJˏŤJŤǖ˼',
            'categories': [
                'file',
                'access-restriction',
                'access-restriction',
                'configuration',
                'network',
                'file',
                'network',
                'invalid-user-action',
                'invalid-user-action',
                'os',
            ],
            'source': '¶ǎԋҎύҝŒ±Ȱßɽ\x84ɨÛț(уŰҽЯїĀțňρĎ¸ĸкį',
            'corrective_action': {
                'catalog': '\x85ԝТӰΚMјȥűǨĳ\x81ŃҙмΝԒȘîƅ\u0382ťŤĘСɂƘǎVγ',
                'message': 'ҷϬԫĴЂШίˆРͳʚҶȲҁµҦ,ǞѲ´ҬŁɢΔɿІ˂ҿϺӱ',
                'arguments': [
                    {
                            'name': '˸ĲȈ÷ňŰԩΘǡÞˇӬ\x9aҹӔӌӬԣɐƾƍϢķĝӾr',
                            'value': {
                                        '^': 'string',
                                        '$': '\x97ʴǖïԩʠűїŴʿƿȇПɸ¶ӥŴЗÙåȂҽϦжЃǠ\x91ΪǒѬ',
                                    },
                        },
                    {
                            'name': "Ӣŝԭ,=Ҳ'\x91ͿӷԍǄЂӝëȬǉӇӸɅʜʗņ£ӚҢőҰ҅C",
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ɕțȹӍʵɸĶʤʮ}ΐЃΦʝuÌɜǎĊŬǕƬòcŔҢϠ҄ςҵ',
                                                        'ЖȨɲы\x8dԭĜтÊ¤гϜɈwȠӘrӝȼ҃ƙȒΓəԟЯöκҹB',
                                                        'ȞµÿʍŅ÷Ԟ\x90ѺʷһϾ\xa0ҋџǓɅͿ·rӼРŶƏҶ\u0380ÎqΝҏ',
                                                        'ǱXίŜ҆Η\x93\x86ăцĭȯDǋVϺɂÓƊɖmƾʝWԕò³ӧǂΓ',
                                                        '¦ћϑΩɟǁɔџӨȭɶìЈŧԅė\x85ƞ\x9eȺˑaʗњv]:ӪȠÝ',
                                                        'ЊΊӤťɷΒǼİō\u0378˔ɇƸһŦŶæȉԉȘа΄ɲЬƻƻƤѰӆĞ',
                                                        ')ӳOƋбΐªϳŴёƷПbЯ\x95˖\x82˺ԣϭˑοԆŻԋ¾Ѩ˯±\x8e',
                                                        'ʽӘŏ²òѦdЍʘԊgƬнÛ˩˄ӁɒώҧτʰŲkǶȊдєLѦ',
                                                        'ӳљԘӘʪό\x8b~ɦ˲\u0378őͼȒԬȼҞ,Ӹˁ¾ɑŽзѤηʑǡƃȑ',
                                                        'ӽƀΚĢЛНǈӓΒЕǥȍʪΧ¿ҮЖȡѧџЕ˲ȉΤǓ¢г\x83ʴ˻',
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ϗήʒʺ˽ŋɪƐ˪ŔԣƾҠуяϣ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                    ],
                                    },
                        },
                    {
                            'name': 'BԇƅıÎ\u0378ŞɆЕ\x9a¤~ʔӹƆƇʰʜÅGaɏŁĖӋÛřϋūˮ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210228:024614.830765:+0000',
                                                        '20210228:024614.830779:+0000',
                                                        '20210228:024614.830787:+0000',
                                                        '20210228:024614.830794:+0000',
                                                        '20210228:024614.830801:+0000',
                                                        '20210228:024614.830807:+0000',
                                                        '20210228:024614.830814:+0000',
                                                        '20210228:024614.830820:+0000',
                                                        '20210228:024614.830826:+0000',
                                                        '20210228:024614.830832:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǚΆѥœ',
                            'value': {
                                        '^': 'float',
                                        '$': 553589.0348912497,
                                    },
                        },
                    {
                            'name': 'Ɉæû(ɥìѓв ҆ӯTΔådʮ˴ӿéƀKѲ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ÕѪÂџ\x85ƑҵƱɑÃ5',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ЊдΣ[ϐҧǗǌuЄĕ\xa07Ğ3ȉЬШǭ˶òÐĹňΈŒ<ĥЉΒ',
                                                        'äěţӀɣ˪Ƚ\x8a˅ӿɳ\x95UӱųĬVσʊωÃƖþșҬԇŭȖſĶ',
                                                        'ǾЍ×˭ˆƏҳѦӇЁОɚƇόǿɈ˙҄х˅\x87ҡ$Εŉ\u0378ɪͽϯĹ',
                                                        'ϐΉЏΑ˛ġϰЁŖԇKjϳǎŊˣɎЙϱїƹʡ΅ŒϝӀԤ\x8fʬі',
                                                        'Iҍǋ˵ÒӴήΛȍýϮȴҨAЍȆщŻˈĝқԌÄӞʖʮǅ΄ɇĭ',
                                                        'РªzºсӶӌоӘʨÖ\u0380ÕϿыӒўīƈƿœƝƍEЌȒΏΦƦ0',
                                                        'İѤĤgėÖԝÇ0RĢԓȅʡȏĆʝΏъũ˵YŚl\x9a΄ʃŨȦa',
                                                        'Г>TȕīӅćҧØƭĔόԈӛɯҌ\x86ҎͰȑˏҝǀČ˅ѻѺǲˎI',
                                                        'ʍƹ\x9fŠɹЋϏΕņˋϟɚʿƱ{ǛŐİʟǏѐ\x91ΗΗӘǓȂ\x94ϩϔ',
                                                        'н\x85ɧέƝŶ˼ȆЖ˴ɨþ·Ϻ\x90ƍʀ˪Źʹυ\u0379ΕŧƜԙŦѣԢ\x92',
                                                    ],
                                    },
                        },
                    {
                            'name': '(ȸðɯˎCȝГ҃ҁȈϟʑτ\x80İӡѾӔʳŲʷλƍŽaĭʞɶґ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ĲԌ&МĹɿɿśӭƃƼԀŏΎ\x90āɱϾδɇѸηȓ!ɥǂŚƗ\x87Ł',
                            'value': {
                                        '^': 'int',
                                        '$': -2105333253913388647,
                                    },
                        },
                    {
                            'name': 'ÝŤŰӚəŔҥХƊź͵ѓŕǓZгɹǠSʝȕӧɢΕʚʞĽI',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'Qȉ\\щɥΦ˯\x81ϱѡǞɆɶԊɑ.ІáҼ½жʝϖԣúғ,Àʈơ',
                'message': 'ĆҺΜɏ`ͿïǿΆӺȯ>\x93áІάϗ8ɒуţҀǟйϽ£ēәӌѧ',
                'arguments': [
                    {
                            'name': 'ɪҏȼƣÐt¼ǉȔӭвŵ',
                            'value': {
                                        '^': 'string',
                                        '$': 'Ēʷϭ˲ųÌʓǞʪіŽЩ˚ҎΏlȏèȜѲŏѩɑɗTӴŬͰϲi',
                                    },
                        },
                    {
                            'name': 'ȮÎ4bοʎϛ˨ʸČ',
                            'value': {
                                        '^': 'string',
                                        '$': 'υJgơɇ9ԬŒɿΞЩϾɤʅˍԐPƔƝʝƎНмНϳ\xad\x8eðƙϒ',
                                    },
                        },
                    {
                            'name': 'ϧǊήьĚɐƩÅâҘҢ\x8dѨ1ƿϚʃȨάʩkҎҼƅĸ˨ҘɅ',
                            'value': {
                                        '^': 'int',
                                        '$': -8696805386922799648,
                                    },
                        },
                    {
                            'name': 'ē˞ΖŷȶϞ}˕ԟԫҼӼȼ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': '~њƈҩ˚ȹłѬԐѸκґơΘǹŕĖıѳ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ÁѠё˖ɤÏƙσ.ҿ͵ɰǍԚȽВ.ȺɑŬǨĄ0ʰĸʊʊý(җ',
                                    },
                        },
                    {
                            'name': 'ɫˑƳʥżʹɋ˒ӉǍ҆ǹČΘŵ\x9cҌʅȌǬƒҝĭҹɄәʱƑ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        5012570957837494072,
                                                        -5328619486136249442,
                                                        -5528093153808234553,
                                                        -2889755009711308514,
                                                        -2588807385024174170,
                                                        -3465358220794099754,
                                                        6518210886327240555,
                                                        4264578559814818188,
                                                        1434172623659495446,
                                                        -3202053361495680003,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ŵΟ\x8aШҾѤ˛ɦ\u0378ɉ\u0383³şѐʵмɊPЗØΞƯɘŕԭšǤęɲķ',
                            'value': {
                                        '^': 'int',
                                        '$': 5116483638505902188,
                                    },
                        },
                    {
                            'name': 'ǲͼјϰǰȹˋъoɞʝг/ʘ;кĵϲҍ!ώϒПƻȰнɾӽҊҢ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        150395.08319172118,
                                                        158178.74548231717,
                                                        803304.2181395935,
                                                        552682.0403058763,
                                                        646397.1688384123,
                                                        682864.974180929,
                                                        119244.10451885825,
                                                        999582.364932168,
                                                        972962.7080537963,
                                                        813322.5731082949,
                                                    ],
                                    },
                        },
                    {
                            'name': 'TҊøĨ\x9b˔ʻ˧',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210228:024614.845983:+0000',
                                    },
                        },
                    {
                            'name': 'ǮƖрúʆʺѝНɀʺʸaǂBӌҋѿƑ\x87ʳʄȢнɿĿΡґǰϴӆ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ԍÇ\x88*Ό',

            'categories': [
                'configuration',
            ],

            'error_message': {
                'catalog': 'ƽ\u0383',
                'message': 'Ý',
            },

        },
    ),
]

class RegisterTranslationFailedEventTest(unittest.TestCase):
    """
    Tests for RegisterTranslationFailedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_TRANSLATION_FAILED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisterTranslationFailedEvent.parse_data(test_data)
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
        for test_name, test_data in REGISTER_TRANSLATION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisterTranslationFailedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTER_TRANSLATION_FAILED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='RegisterTranslationFailedEvent'),
            ),

        ),
    ),

]


REGISTER_TRANSLATION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'error': {
                'identifier': 'ҩьȤЃĥƷЛȷΰ\x9cǇÝƖŻȇɖ͵ѾŋĞҸѰѸǾԓЂԐγÿ;',
                'categories': [
                    'access-restriction',
                    'configuration',
                    'file',
                    'file',
                    'invalid-user-action',
                    'configuration',
                    'file',
                    'file',
                    'configuration',
                    'internal',
                ],
                'source': 'ɿNΆҨ˭J˜ɛΉΧͱлƶMф˴ЉÙȜʫ˱ûДŧȸƅԟʽɿΓ',
                'corrective_action': {
                    'catalog': 'Ͳɓπ˥ҶϮǭҺʫЪέŘӌà¡ɳ¨\x87ȷ5ͺʦϩкCʥϫӊ˚ˬ',
                    'message': 'Ҧī˸оҩĂ\x9cйºήƂÁèҀƭ¹ĶϪśĨƬ\x83ԪϢȬΟϬƉϮЮ',
                    'arguments': [
                            {
                                        'name': 'ɼ\x80ȶˑˣƓԝͳŔʧəãзӃìȲηΐ˝ǠȮƔʾѐУĩς\u0383ϛđ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            9012716893605097033,
                                                                            4576374101301327549,
                                                                            -3525479965421049685,
                                                                            -4817255394329284312,
                                                                            7399920798295029589,
                                                                            8621904952813424563,
                                                                            -8756272118348303882,
                                                                            121803561345468579,
                                                                            5252193661165419214,
                                                                            2884995591532916244,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԑǀGłBƋ"ƟԢ˷ƀmPѓρ\x8aɌĊȭΕƮsǺʱɎƻ\x99ǰɩǮ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '£ƉϠӪ=ӒϫƑʐɉʭÌ¨1˪5˨ѡϪЙË§Ş{ΖŪ©ϼҚ\u038b',
                                                    },
                                    },
                            {
                                        'name': 'ʧ¼ĺÂ\u0382ϔЧҝȞǏʹӜʀƨŹÍ!тȊ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024614.823215:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x88ƯΆΕӿeӝӰ϶ЙǷǉȶȝÐΪŝԇəоҠΩӔ˷ҝҪӚĖ\x95í',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ѧǯĉ\x96ǽΙӑɫҗϨʪïν%˩ЙҍӶāАʻПˎˣOƾßĲпΙ',
                                                                            '˺ѕZƩǾҲǲӿˍɩNŃÆяΏγÕªѳɁ͵ɯêŴҵÜËĩОк',
                                                                            '[¬О°ƔÜͶuӅһb҄˄ɺʄòƙЉkɾӆΝķķƊĜȁ\u0382Ŏǐ',
                                                                            'ɴŰӤŖŸχ©Ӵӻˠ°ϭɢłԀԖΦńĔÙÚĢѐӔԝμΚĬǰÀ',
                                                                            'ΒЅǛʦΡүaҹ\x9fӌήВԋҳʀÑϘƮόƤ˩ѭҞɻБϿhWϣϯ',
                                                                            'ȌǊǫѴŲľǢʯĆҜĸōԚԒяƅƧ¨ǢŜϪǗɋȝɛǍǚŷ7ƅ',
                                                                            ')ѯ˝ɹͱЊņßÀǱɩżɳ\x9fУŚμԧJêʅʃҼ÷҂ɆªÎ\u0378ŗ',
                                                                            'ҍʤџƜÏǗѐΗίƻ·ЊЊϿˈӇӄûӄʁɰʅәқΧЮҟǼѝԔ',
                                                                            'ΌҼîʂáɖ\x88đŻ·ҪıÖȬȢұӲtЬɱŠǓдӸϮԦЋҔå]',
                                                                            'ɹ,ҿɹƙŖҒ÷ЛƳ¤ΚˬÚĆ҃ȹΘķѹČʗʓҩˮ;ɶƭơƽ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ûʃƁ¹˷ȥĬӛ˘´·΅ѫϢÌɝιŝƴ¼',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3372270364064152386,
                                                                            -2948243391629409344,
                                                                            2743993087649494200,
                                                                            -8464153508969330039,
                                                                            5243272825170591535,
                                                                            3564564121577387718,
                                                                            -3550884454158803509,
                                                                            6425982873858552760,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӫ˩ԙ\x89ҩíģεɃΐӺŲ˯Д˅у,ƉȨÆϒƅǈĮɽΏʦԑǌǫ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 771977.8920217147,
                                                    },
                                    },
                            {
                                        'name': 'ҁɏѤΧ\x85\x93їӓäΉ͵ԟˈӫìҧ҉ĂͰ£¼ΠǄΚǙ˕',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            646569.6062156081,
                                                                            97612.26784764201,
                                                                            -2876.16876485158,
                                                                            -53653.14730459378,
                                                                            417308.6731620315,
                                                                            641623.3923380057,
                                                                            353618.3293209468,
                                                                            282.4091812634433,
                                                                            903356.6953934961,
                                                                            659443.5711494361,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʉЌǱνȊOРЅȟϹƟҲʠ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'eɰΨҿEɪΓː\x89ȇźȝԔɅǽϹʵķjύɜʭƣƝԖϹЍԓѣɭ',
                                                    },
                                    },
                            {
                                        'name': '¡˲Ÿġѕʓvԓ҃œͲȄõΈ\x98Ƣȋ~ћλБƺΔ;Ǭ\x88Ц',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            583930.2835211925,
                                                                            645092.8000705817,
                                                                            371530.20469081844,
                                                                            205140.26860383863,
                                                                            37348.08196330565,
                                                                            975747.1691513432,
                                                                            80310.33300223085,
                                                                            282287.06111771317,
                                                                            880965.0328773882,
                                                                            38942.94612006459,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÃÄØǔÅɧŅԉćä;żv\x96ѫŉФñʊф\x85҂ԇΉθ©Ѝ˝ԙπ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7607381296493712988,
                                                                            5936461193349247944,
                                                                            2719501571013234730,
                                                                            1229049202738456292,
                                                                            -7238362972378899231,
                                                                            -1303190791804128063,
                                                                            5164367177112151653,
                                                                            -3411480891083412076,
                                                                            -5396930181631720057,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': '!ǐƅіșѽҽˮԉƌȐ½ǘƇͶӓӪŸО´χǹɌӨюЉʏʚǧЯ',
                    'message': '\x9bɾ˵ҰÆγϔ×ȫǫυµ\x83áZѳПӉҤНѕǃȋțЕ\x8eǭʅ˛ː',
                    'arguments': [
                            {
                                        'name': 'ϐĜƭ¬8ҎϵͽåЈʠÖ˛',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'XˎÎӁϬʈŀͿͰԤМѹ÷ƢƜǖѪȐѽ\u0380ǆ˗\x8bӇьϰ£ēɾÞ',
                                                                            '˫hӓɉȟ\u0380Ӯ!\x8eцΠxҞϿǐΝ&ϑɇҲ\x97˜-ĴӊµōĞӍȬ',
                                                                            'ȢԐΪҙЏʚʨʂЕ\x99ǀϒϐΌűӖŔŞƜΛHĔӣĩ\x81ǙǹˎӴæ',
                                                                            'ϐĜ˦ȔϳӘČǪb\x99ϕæˆ\u038bÁхŎѷǯĦ͵ΫĮϷƆƲœīѤЫ',
                                                                            'ʴ˦ύćȞψŸĲʸǇӭΏäϮΞ:Лʈ˞6\x81ŕРӁÌ¯5Έƃɣ',
                                                                            'Гňoɢ0о˓\x88ǽкʫµ´ƉɛčƮƳЖ\x8aáӀpӕҼѻƤЉѴ˜',
                                                                            'ÉƺҷrΨʍԄ"ĭРˠǫˉλŽɉź˱¤öʓǩDļt¦/Ҟ¨Ѯ',
                                                                            'FǊǌӚȜкŶЎ˦łǄ6ʙȍĒҩɑΉǝ҃ѥʳВ\u0379ҀôˬЧԉȹ',
                                                                            'ȆŁ#ē½ȐM4ÒĻǡʳ˓ʖļ[ɟŖɚͲɦäʩφɗȅԫ±β\u0378',
                                                                            'UʎЧʄɒϥk\x98\x95Ţ³GӰĽʹЕӕȽЀôǖɳȖǊɞªÜҏaɑ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˎťˇӭñV˕сȬǪ˦ҥøǪЪJӃ˫ȺϐŐˊ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 734947.1132498797,
                                                    },
                                    },
                            {
                                        'name': 'Oĵȫ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8443606335277418344,
                                                                            6487124400828752886,
                                                                            693854956959525619,
                                                                            -9135573582356302448,
                                                                            -1235802085242896667,
                                                                            -6129038567907216992,
                                                                            -5369046226010979634,
                                                                            -840255977120339030,
                                                                            -8207482013792432703,
                                                                            -3431059918634655334,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʤϱΊҲ˂˶',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ƿƺˣь×ϧǁÞLӰȹȷ˽ɰŧÁūʥҤčɥ\x95ӷ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024614.827495:+0000',
                                                                            '20210228:024614.827523:+0000',
                                                                            '20210228:024614.827531:+0000',
                                                                            '20210228:024614.827537:+0000',
                                                                            '20210228:024614.827543:+0000',
                                                                            '20210228:024614.827549:+0000',
                                                                            '20210228:024614.827555:+0000',
                                                                            '20210228:024614.827561:+0000',
                                                                            '20210228:024614.827566:+0000',
                                                                            '20210228:024614.827572:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƥѷӅћEԡҌςʪŎдŗԐ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7350918255754392642,
                                                    },
                                    },
                            {
                                        'name': 'Є\x9b$Xѝ×\x86',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԗŗо˂kуƏҷȊҨҝÍƠɳЩŘɩȗԞʆѣϰїł\u0380ԔԞȃťƶ',
                                                                            'ҹЩɎӬ˫\x83˹ǍĲЈˁʴȣɋГ˹°Ӏ°ōȚӌǾϭˀӠƐǮʸρ',
                                                                            '˨ȫʼˤȗ\x96ДΚ:čȄςѳˡϢ_Ҁůц˜˘ǧǿ°4˻ŬПŢĝ',
                                                                            '-ƟύϗǝǗәΠίËðцҸȾӤɿđҹǶӇɇSɬƳӹϿЩɍ°ɏ',
                                                                            'lϐʋ\x8aìɷơŭЅɴ5ʶñǻΣԘȸ\x85ʜƁʲǘοљҕ˝Ť\x90Ĩ@',
                                                                            'ʲҳϟ˪ȿ΄ϥ¢șƬŻҬ9ŽӤěЂś¢ʞ\x82¡ʧ҈ŪɜǗʛȧ˹',
                                                                            'Ėʤϩҷc\u038bΉґ¨\x9f\xa0ȷРҩνЀЅ±SʠʡǕŴĄȰ¹ԜǾҼ˰',
                                                                            'ˈ˧θԀΖԏѩϘƂċϜԏ˻ȇĻĉνʪ\x8aįЏҥàͷͺȺͱӨϑθ',
                                                                            'ȫÒɁњϡJűǢɔȜѢ\x81ƶRƑʦ¤Ä]ϹЇиɄǤʕǹβâͼŇ',
                                                                            'ϤǖΟcȤΡˊ4ΜԄÐŏ\u038dԋЂыΗȌɛ»ҞμMіӎXʰMθѧ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӥэʟӪЮԊÌǆŴîҁɯ\x82ȨµˊϋȀǎцϱЦʅƵЂŦһϘ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024614.828336:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȗНlÅŖçԟ\x9aĿʺͻȃƴíģáÂҲԄ=ԅȸKԂʫ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '=Ǔ˜ȗÆϸšͱ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024614.828623:+0000',
                                                                            '20210228:024614.828636:+0000',
                                                                            '20210228:024614.828645:+0000',
                                                                            '20210228:024614.828652:+0000',
                                                                            '20210228:024614.828659:+0000',
                                                                            '20210228:024614.828666:+0000',
                                                                            '20210228:024614.828672:+0000',
                                                                            '20210228:024614.828679:+0000',
                                                                            '20210228:024614.828685:+0000',
                                                                            '20210228:024614.828691:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'error': {
                'identifier': 'ȠʽŲҸ˅',
                'categories': [
                    'configuration',
                ],
                'error_message': {
                    'catalog': 'łċ',
                    'message': 'ɑ',
                },
            },

        },
    ),
]


class SetLocaleEventTest(unittest.TestCase):
    """
    Tests for SetLocaleEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SET_LOCALE_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.SetLocaleEvent.parse_data(test_data)
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
        for test_name, test_data in SET_LOCALE_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.SetLocaleEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SET_LOCALE_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='locale_code', name='SetLocaleEvent'),
            ),

        ),
    ),

]


SET_LOCALE_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'locale_code': 'ĨȽĆ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'Ӑ',

        },
    ),
]

class RegisteredTranslationCatalogTest(unittest.TestCase):
    """
    Tests for RegisteredTranslationCatalog
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTERED_TRANSLATION_CATALOG_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisteredTranslationCatalog.parse_data(test_data)
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
        for test_name, test_data in REGISTERED_TRANSLATION_CATALOG_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisteredTranslationCatalog.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTERED_TRANSLATION_CATALOG_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='catalog_name', name='RegisteredTranslationCatalog'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='locale_codes', name='RegisteredTranslationCatalog'),
            ),

        ),
    ),

]


REGISTERED_TRANSLATION_CATALOG_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'catalog_name': 'ʊʔғʛѵŚʪɁȪҵʹɉԮ\x89\x7fÇ',
            'locale_codes': [
                'ƶǲȪƔҚǺҩ',
                'ӃϤ',
                'ɸ',
                'ѢƖлѷΓΑ',
                'ưҥ˳Θ',
                '´ƱƩ',
                'ŦϵƘӳ9Θεҧɮ',
                'R˦vω',
                'ɶā',
                'ɋYЇ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog_name': 'Ǧ˾ϥ',

            'locale_codes': [
            ],

        },
    ),
]

class TranslationsStateTest(unittest.TestCase):
    """
    Tests for TranslationsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in TRANSLATIONS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.TranslationsState.parse_data(test_data)
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
        for test_name, test_data in TRANSLATIONS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.TranslationsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


TRANSLATIONS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='catalogs', name='TranslationsState'),
            ),

        ),
    ),

]


TRANSLATIONS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'catalogs': [
                {
                    'catalog_name': 'ûɦΊȌɛ®ӜνǸҹԛӶЗѪӌԨʙҏЇҚȸϖҘϢ<ϥ˜ӃŬʨ',
                    'locale_codes': [
                            'ҕͲ',
                            'ү¨ɒ\x82',
                            'śĴÿ˹îͱ8\x86WĚ',
                            '/N',
                            'ˉŷϮчʌçςӇZ',
                            'л\x92ȖϿī½ǩ',
                            'ʐҩϸĆƴˎԟƥϿŭ',
                            '$Эӯ¶ŢЌȍŁ',
                            'ϜΉҒʂΌҺ',
                            'ϔѼ',
                        ],
                },
                {
                    'catalog_name': 'Ήœǒá˧ƨʌϞқÕӥ҈Ο@ҍ\x96ʸĶɃԭƝɇ*ʵǸǹ˂ǘхԨ',
                    'locale_codes': [
                            'ŨӔϵĲ¶ф',
                            'ťΖ',
                            'Ćˤą`ɡ',
                            '˼ Þō',
                            'ǃԠϾŒӰϳèȘƘϧ',
                            'κȉԉҙƈʛӂ',
                            '\x87ΝʒѵԪ',
                            '˹gҽǖō',
                            'ȜӨŉśʄǫƧŬ˝',
                            'ΈѺїІr',
                        ],
                },
                {
                    'catalog_name': 'ѷӱÛaΤЉѓӂ țԐУ\x8fԓĔйñìӻϩɅÑ5ʸ˖ġŇҦҝƎ',
                    'locale_codes': [
                            'ȓòY\x9aѠȊǸʏȱ',
                            'ʤӿԊȷϴўӪį',
                            'ɖϬҧԓɽѱį\x82Ρҟ',
                            'ϣͱр´ʐӉɡ˪\xadÒ',
                            'ωśGßǏ˃',
                            'ƮŉƳȘӆӉìι',
                            'ȕɿ¥.ǀÐ',
                            'ӷѦв\x90Ҁɽ',
                            'ҡŹў',
                            'Ӓ\x85Ƹ',
                        ],
                },
                {
                    'catalog_name': 'ҴϙѐχԅЮ1ʨѾ-Ϸƞƾ\x9bͶҗ˾ǝƆ\x85ʲǰ\x94¿ŒʻƣӆǙǴ',
                    'locale_codes': [
                            'ӨÁÏëɆӹɶ',
                            '\x99ɞ>ӿ',
                            '8ƭʑʊȘԤѯ',
                            'ɍȐ',
                            'ӲƴŮѹÿǊŒӇЪѕ',
                            'îȶƕȍĦʱ',
                            'ŤӝȖԦ',
                            'ǟǯŘl\x90ΰ',
                            'ˮ\x94ԑ(ȝɿѵ',
                            'Ê» ˺ûǯ',
                        ],
                },
                {
                    'catalog_name': 'ΈӴ\x9aƜɸŉѦ',
                    'locale_codes': [
                            'ʘԂ',
                            'ůѯŽōΡ',
                            'ɡÈǶzɔƕķв',
                            '\x97ԪԡÄ',
                            'ѵǨɓѩƥԁřβϊ\x82',
                            'Ǟ_ŷ',
                            'ϣθжȬƵ',
                            'Ƹ\x95ʜΌȁ',
                            'ǮúƳ˦ȼɮƖśϫÄ',
                            'ͻРʼʄl)¥Ą',
                        ],
                },
                {
                    'catalog_name': 'ҸӷʈC\x81ϘšŭΦ˂ʎÝԁő\u0383Τʈʓłй˪žњ˴öӇÊʈҫɀ',
                    'locale_codes': [
                            'ƫȱ\x95',
                            'Ԃ˝Δȟл',
                            'ΚӨћҧǞʳ¨',
                            'ԮɚǤOG˵ʵĴљ',
                            'ǤǫťХɹ˔Ԕ˭ʳ',
                            '˗ʧԤźҜjʐȌϺΣ',
                            'Ӊň',
                            'ĞԢ',
                            'L',
                            'Ԙʹȉɉ¼ȸɿĵ',
                        ],
                },
                {
                    'catalog_name': 'áƔвõÝʵ˻ǜƆǂȶӲʪ\x98ȯԌ˅ƶԟϊνȱǅŃˡYiԭұʧ',
                    'locale_codes': [
                            'ɶǡєӴԡʈѺӲˆ',
                            'жҰƳҮ',
                            'Ҫʃԑѐ',
                            'ƇΞä',
                            'ϖȧwΟƹÓяΗ',
                            'ɊˠÁ',
                            'ƱėԕѮԩ',
                            '˯ҟ',
                            'ŏ ɓ]ӏΈΫΛ˖',
                            'ӆɇӈȷcԂ҈Ĳžҵ',
                        ],
                },
                {
                    'catalog_name': 'Ѓɤԣs ҦӁÊŅǱ˥ʶ{ƮƙIğÍϿȠ\x89À\x90\u0378\u0379ΕЧ\x7fɠϔ',
                    'locale_codes': [
                            'ӠĞȫĨƶǣύ҆ѐϬ',
                            'ƩΛȞԅɄÛώÍѳ\x96',
                            'γĆүª',
                            'ȑʑɊвӘ',
                            'ƚιƜтеĽŔˍ\x91',
                            '˼λԆ˷eӚҏŽǕҚ',
                            'ϽԠϸőĠɳ',
                            'ϵ',
                            'М\x85ʜʅĝΗr\x98',
                            'ȼº:ω\x8aɾ',
                        ],
                },
                {
                    'catalog_name': 'ʜфjήÁMԋā˕јɉ\x92[ʩȻ˖ɮѵ˅SԥԤԏŹ\x8eȀЛϣɚŌ',
                    'locale_codes': [
                            '9хĄȋ',
                            'Ȁȴ',
                            'ňԔǴ',
                            'ʫǉȰɊɺ',
                            'vъα',
                            'ɵȼFҨ',
                            'яőѠŜ¹Ƙч',
                            'ӽіˀԕѓȋª',
                            'yķ',
                            '¼ӐӽҰÙĂ;ӏ',
                        ],
                },
                {
                    'catalog_name': '(wШɠ]ɔӇԃüƠĤϲ¤£ŐʌɈԪòʈĽŋΊФŤΊtȴʵȀ',
                    'locale_codes': [
                            'ɾʝŸGΰƃʼǮ',
                            'ĴƏϵ΅',
                            'cϔʮӦōӌԓЏ',
                            '˪I˷ԡ',
                            '\x9cʪъҸ',
                            'ɂòȪ˝ʓΡ',
                            '\x7f\u03a2ĚѪ|҂˅іϼJ',
                            'ΐ',
                            '\x89ϽŜǣȼ˺W',
                            'ҕŏĊУҒ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalogs': [
            ],

        },
    ),
]

class LocalesTest(unittest.TestCase):
    """
    Tests for Locales
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOCALES_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.Locales.parse_data(test_data)
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
        for test_name, test_data in LOCALES_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.Locales.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOCALES_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='Locales'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='code', name='Locales'),
            ),

        ),
    ),

]


LOCALES_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ƌѧ˷ѿɨ2ÀϓɁǡƻδӲŜˊΗäʶƭԌĴɜѐγӸγӶʁ\x87¨',
            'code': 'ϊ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ɵ',

            'code': 'Ʀ',

        },
    ),
]

class LocalesStateTest(unittest.TestCase):
    """
    Tests for LocalesState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOCALES_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.LocalesState.parse_data(test_data)
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
        for test_name, test_data in LOCALES_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.LocalesState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOCALES_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='locales', name='LocalesState'),
            ),

        ),
    ),

]


LOCALES_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'locales': [
                {
                    'name': 'ǎËΐҢԕʐaūɛѫԐ¾¼ˡ\xa0ӒƺǎБӱĺňˈлɶÉ',
                    'code': 'ǯÿ°ЮĹϞӇĒÍ7',
                },
                {
                    'name': 'ζoΪȜɷ\x94Ҙ¨ƑΏЭӬЈŎĈϜϝɐŅ×ъɝԌњңԎʱϕԔц',
                    'code': 'щʁŞ',
                },
                {
                    'name': 'ţԤƉɒ\xadǀϣү˻ʐȜ˟ĺғ[ӗηуɸɺ-ĀɦƩҶʀʼșϽǞ',
                    'code': '˵ΧP',
                },
                {
                    'name': 'ѠîıʲҺ\x87ӃțįϤŎҔѓѓɾңɣȺŒƉѭ¯ğņ\x83ӊʖԣèЄ',
                    'code': 'цӢԕħЦѷιЖ',
                },
                {
                    'name': 'ȀʼǉĹ\x9cӝ2§ŗ¼ͰJǫѤĜ8ÌҠҭcªϬϗƎσ\x9dMμɁԮ',
                    'code': 'ʽÍɌȋƅȾϑí5',
                },
                {
                    'name': 'ʮԙ4иԉϚԑņӱɗžҚ=юҖƎȆѳбʾӦͰʎέϖђŪ@șʻ',
                    'code': 'ɰƛϵ\\ōƲʣʅƨ',
                },
                {
                    'name': 'ԍǍùÁƎǔAŌϋl\x8bȚª¦ÐԈӤϹŒʋˍȧˤԎ\x8bӻ)˯ÖÄ',
                    'code': 'ȶҝ˃ɥЇI',
                },
                {
                    'name': '˅ԟVџЄ\x8aYшǙɐӐŘ¿˚ò·ĔϗѬŽԨŔБΖɔɖŞȠÐЉ',
                    'code': 'вȨ',
                },
                {
                    'name': 'ƖϸɕαЙʚӜ|ӱvʼă˰ĘӹƮц8¼ҎϸРӈһȰǀ¾\x9fæ\x89',
                    'code': 'ſѭι͵ȫǬȔˡԌ',
                },
                {
                    'name': 'ȴгˠӓѫÔ˧ҿѱϞѕƖѭąƔǱȐʚǇФrԌȅƶƢТͼ§Ĺΰ',
                    'code': '?EϞ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locales': [
            ],

        },
    ),
]

class ActiveLocaleStateTest(unittest.TestCase):
    """
    Tests for ActiveLocaleState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ACTIVE_LOCALE_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.ActiveLocaleState.parse_data(test_data)
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
        for test_name, test_data in ACTIVE_LOCALE_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.ActiveLocaleState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ACTIVE_LOCALE_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='locale_code', name='ActiveLocaleState'),
            ),

        ),
    ),

]


ACTIVE_LOCALE_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'locale_code': 'ÀȉɷōFʚϢɡ¶ϖ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'đ',

        },
    ),
]
