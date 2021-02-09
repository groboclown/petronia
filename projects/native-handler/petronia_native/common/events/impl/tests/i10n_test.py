# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-08T21:23:20.856259

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
            'locale_code': '˄Ϙ(\xa0\x9dԪЄӟ',
            'catalog_name': 'ĔΙȏŕ˪oԅũÑҋϳ\x8eϻѼ˱щО҃ЗXӂʁʵħå#ȭиüj',
            'message_file': 'Ћ>ųÿƺ,ӗкӡε;Ŧуӱˢпȝ´ȭŘϮƆŒӞãɡʦЛʣĺ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'Ș',

            'catalog_name': 'ϓʫΟ',

            'message_file': 'ůʴ',

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
            '$': 'ώGÈΞʀƨυòȳϓŃԋ)?;¶ƫӢԒƗºϡOұǲцȱӠΗӭ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -3135792105942555892,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 627676.0484658933,
        },
    ),

    (
        'bool',
        {
            '^': 'bool',
            '$': False,
        },
    ),

    (
        'datetime',
        {
            '^': 'datetime',
            '$': '20210208:212320.791165:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ĝRʮϽǾ5øȅȒ8ɻʣнŸA©\x87ϓȲσŮʽÖŢҜѳ˟9ÞѰ',
                'ýӾʮˁʠɍϷªЮ\u0379ˌІƥŪșӶ\x90ƷѺɉ¨Ǚс\x8a/ǠȲřΈа',
                'Ĝ}ĦǏļώÎ\x9bӮƕԣȔƹ˜\x85sňʡˉԛЛĕ©нȘƦĆȘɞɱ',
                'ĔëԫˑȔĮӚîƳāúΓĽÈƋɍӣ©͵Ň˂ʻъ»2ȬҠˣԜ§',
                '˳\x8fZɞѸßξɖңӐӋƾκΪƝƟĨΚŹ˴ҿǈΚö\u038bˡȢȫȔѪ',
                "IԋһtɐӄљɊ(ӭŔȌĈ'4ΜȡŶäňĄ6ͽԓȧÁΓ¡ңë",
                'kzʫКJԒǈҸ˭ǅ˔Ӊˬ\\ŦĶԘϳï¦C˓Ĵsƈ϶˽ўƒӤ',
                'Z$¾Òʖ˄\\ƌΫэЪӪԘӖ˽ӸӥIğΗπƆęȹӐȮϊǈgó',
                'ѱŤϫɮɤӓӡɹâœŻˎϪ˺ʽϵҥǩϧœԏƓÊ\x81ìƃφϔŝԩ',
                'ϧʛκЉ²˘ΧӅӃȾщǍщϏɑ¹ǆӠå҃҆όѢðÈГӝǐǯ\x9e',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -3691262977059222319,
                -1406663530395420752,
                -8204473574335137387,
                -2420201371127452154,
                5769167451260409920,
                -5637868149142805967,
                4949619939850686306,
                -3380268085533682851,
                8359818337656929228,
                5767584783921772166,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                792108.0967725393,
                522746.2781311129,
                273478.494294049,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                False,
                False,
                True,
                True,
                True,
                False,
                False,
                True,
                False,
                True,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210208:212320.792250:+0000',
                '20210208:212320.792262:+0000',
                '20210208:212320.792268:+0000',
                '20210208:212320.792272:+0000',
                '20210208:212320.792277:+0000',
                '20210208:212320.792282:+0000',
                '20210208:212320.792287:+0000',
                '20210208:212320.792309:+0000',
                '20210208:212320.792314:+0000',
                '20210208:212320.792319:+0000',
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
            'name': 'ΝϲϘʹțźΎӄŨÙԇΠŀ',
            'value': {
                '^': 'string_list',
                '$': [
                    '\x9eОɭ3ԬЪӕȓbΓǓ-ċӨӖίɣƫѼÒНÖчĀѤм¡ҳƥͰ',
                    'л͵ӂϟʬʃċʰϝ\x8bɢϿбѓōҶ\x87ƪϳёԌΜ˵ãÑžәəЪЊ',
                    "ºǌȲ\u0381ȭ'ΕɜЄΑҼԣζɕČЊÙϨȞйͶ¥ːΦǓǮ@ˋHƌ",
                    'ÔсźǃѐʀĨɸфȲ\x8b\u0378ǎ˕ÎƗΔȑŴԕæįӶóφÑ\u0381ǺÑг',
                    'ϫд˴Ѣ˩ҡ\\ʑ\x84ҧаԅϢѱϘΪňӭ˜ŀξҸӅхƕŇϥΓϘˇ',
                    'ƪƮΕɚǉԋɟԑþԧӉЗ˃ѪԨЖȉʙȵѴҹφŁҠˊѫmϘ҄\u0381',
                    'сʹԭţūǽ\x88ιǮƘуϭȰ҉Ѻ˽Ȏƙ˂ѲŶŨĞӘ\u0378ʺǝƄʾс',
                    'ԆˢЊȈӣҎǇбўʢҰѻ¿ɊțzgѶɇɟ\u0383ï\x94ÇÂӸɺΦνԤ',
                    'ċɣҠҼδȕЊ˱ҹ΄Ӝǯȧ)ӡҐι˴ƪiŜʠšȴũӘĝŵȏƐ',
                    'Ҟʾ\u03a2ӍłΒƦӥŨăύÌψɩѡ\x80ĨҹәƼœиеÐͱȠsшǒǰ',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʬ',

            'value': {
                '^': 'datetime',
                '$': '20210208:212320.790976:+0000',
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
            'catalog': 'śʟѥОÞÂ\x84Ԧǡ<@җ˔šʀºΝҾSÀȫȮԔѼɇȌR\u0381!І',
            'message': 'Ɩ\x83Ҙ\x97ʧȝćǑƃóȨþʀӯȩʽǍӃӥТͳĪưșɽϘʮӂӹƆ',
            'arguments': [
                {
                    'name': 'ϼѷOLӧãō»ɲiƴӂԩͷΣϡ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        41489.13935805514,
                                        284839.1146320553,
                                        952279.7083932201,
                                        917545.372258958,
                                        62363.36460904201,
                                        958816.1130617589,
                                        674632.5101891239,
                                        383687.51029714476,
                                        192597.5091752495,
                                    ],
                        },
                },
                {
                    'name': ')ƃıŽҩȘЁĐɝӌшʩðŏƯũϊøΆ+јɭù°Ē\x9f-Ȉɾю',
                    'value': {
                            '^': 'int',
                            '$': 681339475946216443,
                        },
                },
                {
                    'name': '/Ǎ϶ӽҥҺ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210208:212320.788076:+0000',
                                        '20210208:212320.788101:+0000',
                                        '20210208:212320.788109:+0000',
                                        '20210208:212320.788119:+0000',
                                        '20210208:212320.788129:+0000',
                                        '20210208:212320.788139:+0000',
                                        '20210208:212320.788154:+0000',
                                        '20210208:212320.788164:+0000',
                                        '20210208:212320.788169:+0000',
                                        '20210208:212320.788174:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ԣÉ\u038dʔͼȇϙαӦ˥Ƽ˧ĈƧjɚʦˣ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        True,
                                        True,
                                        False,
                                        True,
                                        False,
                                        False,
                                        False,
                                        False,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ҫѧԁƒѥȴ¡ƐҟΫγ҃ĳƞvґӮ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210208:212320.788899:+0000',
                                        '20210208:212320.788913:+0000',
                                        '20210208:212320.788924:+0000',
                                        '20210208:212320.788932:+0000',
                                        '20210208:212320.788961:+0000',
                                        '20210208:212320.788973:+0000',
                                        '20210208:212320.788979:+0000',
                                        '20210208:212320.788984:+0000',
                                        '20210208:212320.788989:+0000',
                                        '20210208:212320.788994:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ʒÓЛӈҞȴБʷТɰȀЂХÜɦΟ&ʅĀ,ˋўɴɤƻ',
                    'value': {
                            '^': 'int',
                            '$': -5006448407845075482,
                        },
                },
                {
                    'name': '҆ԡǈϲƱɅŹȽМ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ìрŧ½ǢŝŇɣțдΪѨèԣύӾĄCвȮΪʈʻĞŲЧĲͼʇ£',
                    'value': {
                            '^': 'int',
                            '$': -8454713465230031360,
                        },
                },
                {
                    'name': "Ţ'ΜˇӥȔѽʎǔȣ|ӆҜ",
                    'value': {
                            '^': 'float',
                            '$': 981454.8039147367,
                        },
                },
                {
                    'name': 'ƿӚȤЦӚȣ$ӕʶԭ',
                    'value': {
                            '^': 'int',
                            '$': 3241418844562336020,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ӯҁ',

            'message': 'Ȼ',

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
            'identifier': 'ř\x9fǂԙĔƟщФв\u0382ʱԧϰęЛǩ¦;äϦƙȆɗþӠǉҭrˏѠ',
            'categories': [
                'os',
            ],
            'source': 'ǗѽɲЀ\x9cԈεѠӛѐ\x90Ȟ\x8fУʚ΅гӷȡȳǛ',
            'corrective_action': {
                'catalog': 'Ϭ҉Ő˽ɷ˟aӅхČӞ1Ȣ2DƃӸ\x8aˌηƵӜίɭŽҎǴʞϢ\x89',
                'message': 'ŢӝuŚАcoŴɦćʼҺ~ͷŧÛδͼ·ˋ\u03a2нɾǪșŗϸųʾǎ',
                'arguments': [
                    {
                            'name': 'ӢɼȤƶȏÑ;њρͽӧˊʺЯťͰiκƚԬ˨"Ɇԭ§²ӫƓѯԄ',
                            'value': {
                                        '^': 'int',
                                        '$': -2746102721375193856,
                                    },
                        },
                    {
                            'name': '˟$ń˪Üˋ8ĹԛɺΫƜѱɻʟȔ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -3379985407872955975,
                                                        -7774717077312314164,
                                                        -7037640658856490337,
                                                        678971680738662993,
                                                        -4634884992463603514,
                                                        3758154316396546389,
                                                        2274508089924651279,
                                                        2082660341059877230,
                                                        3217032302546999318,
                                                        -6203312554633895843,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ȧˡŪʤѩ¸ŬϰЫϦȳšϵϓ¤˼ĄϢϯҗ\x89ˠюҶG˫ҏ»^ý',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210208:212320.784420:+0000',
                                    },
                        },
                    {
                            'name': 'ǁέJԠýҖѰˊęʰǲǭ-ùӄʔĻ\x8fŬ϶Ű˚ǀ˚Ě4ƣ',
                            'value': {
                                        '^': 'int',
                                        '$': -8602862601560228639,
                                    },
                        },
                    {
                            'name': '°Ƽҝˁ\u038b\x83ƺ\x98ѫŧӚÝɍȜΘʗ³ЖØѼҸɉəÙϘĦԅ˙ҹǏ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        176936.16776387172,
                                                        -99149.93247160676,
                                                        171703.9885857149,
                                                        723360.1742466695,
                                                        786524.4703889731,
                                                        745605.6017838168,
                                                        3981.5331632730085,
                                                        420250.0890647329,
                                                        449450.92542676826,
                                                        610351.4992290816,
                                                    ],
                                    },
                        },
                    {
                            'name': ' \x8dĹ¥ń²UɀľķϢкʒϫƀŠȖXф£ʷ',
                            'value': {
                                        '^': 'float',
                                        '$': 971546.9025303354,
                                    },
                        },
                    {
                            'name': 'NŶѫ˻ʟѓˮȝЂѿɐˈǶӢԣʦȂjɐʿ¹pŊтҕ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -3008967490141979546,
                                                        1730649519853746916,
                                                        -6176344655148669779,
                                                        8725501069427277624,
                                                        8261893995055708641,
                                                        -3877583465016286368,
                                                        2191952754256201744,
                                                        5820403311497891435,
                                                        -2974956380754329182,
                                                        -6364574483947073443,
                                                    ],
                                    },
                        },
                    {
                            'name': '˾ӾҬӅņҼ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ƀӶӚĭ˗ʹӠɲČǅȷΒҵŇʝʭԠŕʞɑzȭ¨ɿȧ×ѯ\u038dȹΰ',
                                    },
                        },
                    {
                            'name': 'ҚˬѺʶƤѱхξɢѻ\x81˷Ǒ.ԟϷĘǁμҊɧ-ĲǀћÌ¡)ƜҢ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': '˭',
                            'value': {
                                        '^': 'int',
                                        '$': 8037604497120148169,
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'уʡĕ~|r˾ϗʙюǽĩơê҅Dɜǉ҃ρȷƻnʓ ŻͲȫαŽ',
                'message': 'ӪʐɣƎƎȑ҉ƑԑђθğЮ_ԑǷɈӪЦ@ÅӅ\x84˾өƑÙякȣ',
                'arguments': [
                    {
                            'name': 'Й',
                            'value': {
                                        '^': 'float',
                                        '$': 634552.4169943826,
                                    },
                        },
                    {
                            'name': 'ωЗвӽɍиԠʂƼǦǔԚÚõѪѠƻҝήˇÛӏȲǥǺʨɋ˰=\x99',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ӊƈҷǃĝ-\x9c˟ǡǰεӤӇӄȮʕs',
                            'value': {
                                        '^': 'int',
                                        '$': -8812020665103152553,
                                    },
                        },
                    {
                            'name': 'чËÐΨɺиɰОÈĞĎӧƵ˛7ŭϣōӁююϵŷιҊГ¦ўӘĬ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210208:212320.793089:+0000',
                                    },
                        },
                    {
                            'name': 'җǾЅÊĶºÁϾŨόʹϴѥҧâ~ǨtɁ<Ͷ¡',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ǱЛˤԉÆǖ¥ҿˉǹǩӟԈӅɑʉ˒ōˀԛЈϹƳķ=ЫŃʐ{å',
                                                        'Ō͵lĲʂʄӐϿ˴Пü;\x7fǫˈŜƚ˝ӯǨӦʛˌϕʺĨǟήԬe',
                                                        'KƌҴ9\x9eˢĩtθ¦ɶВΠĄňσÍ%ńЂāȆġǥҗľQ\x92ĵи',
                                                        'ŽϏȺǔZïΛ\x82Ĳδ˛ҷǙϦæʪƃÝԝʙľӤǘ˕ǐ/ԟŤĩЅ',
                                                        'ȭγɿєϲѐħΓöΪôȸuЖԭǤа$ȗϱǐ¥©ïЕѭŲӨбϲ',
                                                        'ȣȾÇŶҐȓз¬ε)ϼĄнĲǏ˨ĕҺǊџ˜ӛʍųӎ҆Òѡ6ů',
                                                        'ҰС\u038dͺϱɋҨíL˼~BȚζяƤ%ƣ΄ǝЬɥ˕ƩиπǘßӺő',
                                                        'MȖ\x98ǝϾϴʵŊǊXƍλӝčøԆÿɨҽ¾ԛ\x94ʟʸÐßŋĤƨ;',
                                                        '×Ҽ9Ȳ˞ӉƷǍѱ\x84ѻò\x89ǅŧŵEЙәƷыæӼ³{ǼˬƺѴΚ',
                                                        'ԑlρŔѯP˧Л˃ȊІ9\u0381ѬʋŶȅĬƼ«˧ˢҟЮͻ\\Ãƍ·ӑ',
                                                    ],
                                    },
                        },
                    {
                            'name': '\u0383ĝΑûԐʨҾĝƖɢѓĸ~¬Φǉ\u0378ϠόϵÂGŴƮ\x82fҺӫυ\x84',
                            'value': {
                                        '^': 'string',
                                        '$': 'ѵ¾Ϡ\x86ŃʙtӡƧďӲϠΈŦ˲ˑsǞ\u0379ɰόƶĦΧǍ҈Å¬҈ί',
                                    },
                        },
                    {
                            'name': '\xa0Πҳ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        792174.8352903306,
                                                        -72507.78313964818,
                                                        254219.7310517297,
                                                        415061.38316804386,
                                                        661247.8839262464,
                                                        385958.8680026216,
                                                        509651.1617734735,
                                                        84367.23408802436,
                                                        606005.9878183814,
                                                        953979.5709068063,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӻ˵Y˝ˮӆѢȵӭ=ҫӓÇÈʧʞϷюɬȡƟàԠȌ\xa0ǴұӘіƸ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'Іɝӿи˞ШʀӵÑԫϳ˄ϩʁʎľ@ӑӞӆʵНɣ҂ăӦǙʷăʷ',
                                                        'ѐΜOԇϗņҝϫǛŠɁӡĿ\x80ħiπԔҩǶÅȈƞʲцQ\x92;ķm',
                                                        'Ԇƿ҆ĭόϴ\x9bHɆÔşӫѯӑȜӓ\x81ΥŶȗϚɧǋƋĳǻ˳ĥԍʡ',
                                                        'ʟÔ˅ëƨÙȅ?ћѧ"СʙѣϵǪƮϢÚоϳŸԝԇзɓнʽϖҲ',
                                                        'ʤӶŏϭѢ˲ȏ8ӼƢѕˣʐżǫЩɐԪʁҟTΖЃˬɆæĵΆʆɋ',
                                                        'Τȼƍ®ĭʾѠѰȮæҔŔϊӶƶʦŌĬԡȰŻԜΠɉǼuûȨƳж',
                                                        'εbЛƕРÎˬϊȡɲԈǌԬóтʕĶƦâҊӍŰɾǗď˙ŦψєВ',
                                                        '˘θү\x82ĉ;ˠļʚԉʕ¨бȼԃӣɞĴVѫуɝ´ń»ѾũӠϡŻ',
                                                        'ÑθҴȮЙžțløѡ´јɪӫƅ©Ϗʇǐӽ¹ÚœҐͼѢϖɖҰå',
                                                        'ѼҞƤʹʹϳ\u03a2ӫӒ˫ΪҀʌǳOőǋϳλЈƠȏąȉʹЍƔҶŃȮ',
                                                    ],
                                    },
                        },
                    {
                            'name': '+ԪӂϏľˁØ×ĐVƓ\x7fΉ˃aȦǒ',
                            'value': {
                                        '^': 'string',
                                        '$': '˂ӗǸǈ˨˗ĄӶȜˀɔҬԥýТ(ɥϴӒȄ\x9aԧʔσțȍ#έƪп',
                                    },
                        },
                    {
                            'name': 'tǼſʹɒÛōӗ\x9aŌӮ˄ȃϿ҅Ǳȍǂϟ˘їԁɯÁԂã¯дӽ\x99',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -6869126994253955695,
                                                        -7210906843965463891,
                                                        2227090786864786090,
                                                        6819853071846110149,
                                                        -575319174373785107,
                                                        172422062963554761,
                                                        -5570403838304408806,
                                                        2987502533750864160,
                                                        2414654875066261916,
                                                        5571700825398369449,
                                                    ],
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': ' ǝƇяЄ',

            'categories': [
                'file',
            ],

            'error_message': {
                'catalog': 'ŻϪ',
                'message': 'ƈ',
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
                'identifier': 'ǌыÈӽѪɃͷΉԥĀ˗ұĐЫЁǊԊƹƁÒʟţӄʛù˲\x95Ρƛȧ',
                'categories': [
                    'configuration',
                    'invalid-user-action',
                    'file',
                    'internal',
                    'internal',
                    'os',
                    'configuration',
                    'internal',
                    'access-restriction',
                    'file',
                ],
                'source': 'ÜļӶƚ˄ɗΒkңΟȈχ˩ԠˎӵƍЇͻņǇʅɐ©ƾ¿ԢћӋԍ',
                'corrective_action': {
                    'catalog': 'LφȣŒbө\x9dƣȈȣ˩ɩҾҪÆģŬAӰ©ɽÖǱҤӓqҲСÚϗ',
                    'message': 'ɧΩȏӑɢʶSԤŲɓɨɾȠńˢΛҍϫЌɟǏŢǎĵЪőȣØŅԮ',
                    'arguments': [
                            {
                                        'name': 'ѐϏҗʓЫΥǀӋĊǳ³ɼԔτÀŝқű\xa0ã˫}ȉĀΜƆέȸӜ>',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2994831995974145333,
                                                                            -8767978845228553131,
                                                                            4555870053198502312,
                                                                            3178962089325453856,
                                                                            6586614263346715447,
                                                                            3736150811263680338,
                                                                            -7696844125981222380,
                                                                            -1625088895665827027,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'åΈǎVǓɟ\\ȓ¸\xadǙ2әєѕ®ίЧ\x9fζȅƫӊēɪ;',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʩħȿͿ΄ʎӣҞǽЄƴĜ˯ȸфǠЯíЕγϤѪʦʪƌʷҭÍΥ´',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2872991508898095197,
                                                                            -77831672706160987,
                                                                            7137487810501429020,
                                                                            4841009602091371944,
                                                                            -6841321859170305371,
                                                                            -8410673380630769583,
                                                                            8629637689637731688,
                                                                            694246359288068601,
                                                                            -6340263756614552571,
                                                                            -1077515245497359124,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԑ\u038b҉ԩѸЭɡɋԩĖЩЫΗ°ŒҟdЇƄ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĢϞdɭêâŹRÙŊ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ΈžɔʰȚӸı=ϊûӒʠÓɥſʣħ+¶ЕċԋvòΐÿО"һY',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '΄ҀӜҙìʹʊЖƥӆÞĴӢƍͱŦǋőI˕æ\u038dĠȔҀʊЪX\x9cϾ',
                                                    },
                                    },
                            {
                                        'name': 'ĨŨΞAƝŎкѨɮѨʨÖcšҹȠğυ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ϡɚ˝Š҈ԜȲµÏδƊċÜϪѳѭ˯đúȧƼɶ\x8dlƱϲͱ˂т҈',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԀɲШϙǋůƨ˘ƌɬҏУҼǊũÉý˄ʌʏƵȩӥúɤ˙ϠпǖҔ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            837788.9104446238,
                                                                            21787.48864205247,
                                                                            486382.6950434963,
                                                                            883492.4891312431,
                                                                            206299.506745629,
                                                                            725433.6060691654,
                                                                            467214.19766139553,
                                                                            506185.61991044565,
                                                                            434163.3323073974,
                                                                            92905.39796800123,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͷОɹǸξДϼίхԥ˦ǈŎʝƨΉƈҜӸǀҴѹљ?ΥǮΘŲл²',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7697856543572797127,
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ċÒѱз3ȥ҄ԧżϧөӠѤˣƣԀθŃR8ԋ\x96϶ȾϾʙӿӝѫȏ',
                    'message': 'Ӷ·ǸҐяƸВʒΊŉшĕϥƥˡ>ƨȣѩęūéѻHҪɚɸԛ2ө',
                    'arguments': [
                            {
                                        'name': 'ψУͿԎȦ¯ÒЇǗҭĂОЅƌƴΥМƹЉŵǿ˝ӐəȎʻʵƁŠЦ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 796007.8046551407,
                                                    },
                                    },
                            {
                                        'name': 'џө˒ïΨƠÁ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Хưҵщ\x8cŻɣΛЯǥĞТĮÚō΅0ʢʓɷÑơĜɋΣʆ<ȧόV',
                                                    },
                                    },
                            {
                                        'name': 'ıΙԟȲϊѕ¶Ƀǆƾ˄`˵ȑɼʆǦ#ШκΗΘ˾ǪѾΡђӿ҃Ԥ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            67834.89852712059,
                                                                            324833.37723742856,
                                                                            615744.6665153048,
                                                                            728994.9202705264,
                                                                            884327.779315782,
                                                                            230725.57346140745,
                                                                            555961.4894618731,
                                                                            732393.58127666,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ËɟɉжƺÓԛɬѰ2ӫІþάɟ˞ʛɷ×ӰǕZɕ©νˍÏѮѭ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Лўȣӝ¬ϣӽƵǭөΠ´ƥнjĮqЉ\x91ǂǸφЯѲͰǿ\x910ņɪ',
                                                                            '˹ѹ˭\x93\x94эΊʎйѣԕӼβԫ˲ϒņÝЄʑԝͰҧAǨˎΘɯӓҭ',
                                                                            '\u0381ˮ˻"ȸ˔ãƱӐƻїѦɕϏƭϱψνĂʈƾЈĸŭŌ\u0382XɄŽA',
                                                                            'ŁѤψοϺǗ˖ɷ`ΡҔаюгԚƝђƵӔ˷ΎÍĆˇRkţÑϳ҈',
                                                                            'Ğğӻ˳η}ҌˢкǠSϵʩ¢ЅӟĀϖıШѽѾ¿ԓѹӥwнʲԀ',
                                                                            'ԌȖɺǺоËӂҳ}ҫʸԙ˧ɸлѭʤ.ΪђɅɫFĆѯϏƽљϘʽ',
                                                                            'ÑʷԄƷёznϠЅˁ\x8bʺÅΌńźѳɮԄǼƗ`Î҂ƬȥǗεˑξ',
                                                                            'ѸϫǖΖΠǮË¢ǴчҀưƊԏȕʾĒÊ\u038dǤȚӕ҅ŊĭCď\x88Ɲʉ',
                                                                            'ǕƼǽǨ\x8dǡÝ\x8a҈ŶҩɷϞ_z˟ǚȼ˓ӆLĿɀÕĥȡʹ¸ǋʂ',
                                                                            'Њϣ\x9fʆӕƫϯ©ɫğřϹ·ԣѦӶȠ\x99çϥʩĤмѲƳʺАǷ;Ъ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ąǅƃ`њĦҞĴѡ\u0380',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3585766105702229084,
                                                    },
                                    },
                            {
                                        'name': 'ϏȔȿУǹԀK\u0378®ϻԊКÍ˧ʢĭ]ŰŤпʢтǵ¨сΓiϝǛǠ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 721829.0405008019,
                                                    },
                                    },
                            {
                                        'name': 'ĜRә,ƛ\xadǖӴҥŚʭ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɳ\x91ÒЄЪˏ6ӢȈ1ȽŻǏļѡ\x94ǓǩĲȻȚĳӁĻƑȚ/\x89ÆϽ',
                                                    },
                                    },
                            {
                                        'name': 'ϻƧϨȼөƏҲЕ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2907032608413234601,
                                                                            -7156071160133994313,
                                                                            -8503882055575228280,
                                                                            2209809623692264204,
                                                                            5968141136517459126,
                                                                            735863404350471535,
                                                                            -2906708436006300456,
                                                                            -5526700327557568669,
                                                                            870826265195049875,
                                                                            -1904500852878418105,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǛԖʉŠдԎžӫ˪ͰƼȡǫȽЊŮǂǰӢƵйʳςҮȍΗҦǇƿǃ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԥҷ½Ƶέюƪ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 561092.2104569506,
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
                'identifier': 'ͺӎƻ£ѽ',
                'categories': [
                    'internal',
                ],
                'error_message': {
                    'catalog': 'ѷЀ',
                    'message': 'ѓ',
                },
            },

        },
    ),
]


class RegisterTranslationMessagesEventTest(unittest.TestCase):
    """
    Tests for RegisterTranslationMessagesEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_TRANSLATION_MESSAGES_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisterTranslationMessagesEvent.parse_data(test_data)
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
        for test_name, test_data in REGISTER_TRANSLATION_MESSAGES_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = i10n.RegisterTranslationMessagesEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTER_TRANSLATION_MESSAGES_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

]


REGISTER_TRANSLATION_MESSAGES_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
        },
    ),
    (
        'bare-minimum-fields-present',
        {

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
            'locale_code': 'ϧ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ň',

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
            'catalog_name': 'ūӕєӐiİҽӴþŋЪσѢǜϰΑʇîəɿˤ1χͰĽϹӂǾȡɃ',
            'locale_codes': [
                '˸ʷİԙӟ\x95',
                'ʬ',
                'ʬУ˔˒ʏ³ѳß',
                '˄ɝСĊFβ)ʳ',
                '˔˟ӖºʥǠØу',
                'ťǙơȏԑӃĊŜ',
                'η˻ʞОŸťɂ',
                'ΡЕѤϯҹӇңѮɾӘ',
                '˞XҎ΅ӭ ǢԙǊĒ',
                'ƿɞǅѬʆ-ϧ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog_name': 'Рİο',

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
                    'catalog_name': 'ўЛǚșɺ£2Ã҅vƜԇˎҋϧʀƮșǙЭΊӜķȬʁΑˉƟƦί',
                    'locale_codes': [
                            'ʻ',
                            'ƅҀԢǟĤʣƿ',
                            'ħȕɩɤӅЇȄҍƛ\x90',
                            'ǽӽɐɂҥʟ',
                            '\x88υĆ˗ϚԤˊʚº¡',
                            'Ά;ɱő',
                            '+ʠĸ',
                            'ƇɚͰǜɞа',
                            'Ӄ˩ţɩ',
                            'ѠȮÿƩĂʗˢ',
                        ],
                },
                {
                    'catalog_name': 'ˠʗɤЮıøɞξǝҙҞэƍſǊ¥Ϯͽĺ²\x84ƢʬÑˈŚǶίș;',
                    'locale_codes': [
                            'ҡɶ˲',
                            '˞Fŷ¨ȬɝЂ',
                            'ɄĂǧȦɑԉ',
                            'Řʪ',
                            'ÚÀĵćŃШΞ',
                            'ƋɵǡQӽ@Ӄр',
                            'ʱӁԗъßù^ѷȏ',
                            '҃ɞȜ',
                            '˖˜',
                            '´ʦҳƱśǡ',
                        ],
                },
                {
                    'catalog_name': 'vfʶƅұκɅǱ\u0381ӑ\x80ǽҟςeΝЖƟӊˉ΄\x91˱ɆҠӱƛҦďҹ',
                    'locale_codes': [
                            'Ѐˑ˜ƛȠ¯Эσɫ',
                            'ĥǫƄǤȮĸΗ',
                            '˦ҝǪ˚ҖК',
                            'U',
                            'ʴƔëƔHƥǆɠɧX',
                            'ʉ',
                            'ƾ',
                            'ƭåŴ',
                            '˳ΣʙǠ˾',
                            'Ǟ¼ȫŁ',
                        ],
                },
                {
                    'catalog_name': '(ƴ@ìцɼŰФţȓǲcҜˢ±ɛÉʮτɈŏӐԎгŚӜƕ5Ӻ˙',
                    'locale_codes': [
                            'ΡπʾЃѼʺƚԑ',
                            'ɍӪ,ˈ',
                            'èÅć',
                            'ҜԢ\x8aȝʾ¶μ',
                            'ƹȝÕ¾ƭԢƝ',
                            'ѠΗȟ˂ΛԩȂΨқ/',
                            'τ\x98ӆԦѲҐ',
                            'ʱƛѷŹΗȱԛˋ%',
                            'ʅûɼΉ˼ɳ',
                            'ßиƗÇ˄ʪӫŶөD',
                        ],
                },
                {
                    'catalog_name': 'íĐ҄ǐ˄ȸԈyБʛӆнѾеΪǒГɷӌˑˠԑήɷȫϠӴГ϶Ɉ',
                    'locale_codes': [
                            'Ɖ¨ćОϔÁ',
                            'ɭΞ<ӊȲÃ',
                            'řȸȔȲ',
                            'ĳ',
                            '˥\x91-˝ĕϒԒˉ',
                            'ǑӒűĳШƱ',
                            'уϠ˲ɽ',
                            ';\x86',
                            'ɝЇŨǣӲdʫȳǮ',
                            'Ĕ',
                        ],
                },
                {
                    'catalog_name': 'ɨ\x95ɒɼƇɢҲϟŌźșĨПÎВʆɫϹòԦȝȡӃϸƪ_ТϘ[ϟ',
                    'locale_codes': [
                            'ҴʹȔɾ5ч˧',
                            'Ʃ+ȇ«ǜɰ΅',
                            'ń',
                            'ȗʇήҦŻϓ\x80ȤС',
                            'ӧ\u0378ǁȾî¼Сˈ˨ȯ',
                            '¾кϯ',
                            'ƸҬ£ΓͻûӬ°\x8aґ',
                            'ҳɋΫŜDȸ',
                            'ʮɥҫ',
                            'ǎĳʐÅԚѮΞɓʲȬ',
                        ],
                },
                {
                    'catalog_name': '\u0379іͰo×ƿпWɨʚŎ΄ƗųɅ\x8aȽӱ΅ҏӴǟέą˅ä\x8aˊ\x8f@',
                    'locale_codes': [
                            'Ħӥҩ\xadΉʱƴƧϵ҅',
                            'Ҵƹ΄ɩӋʾ',
                            'àУΔґҕ',
                            'ԜɋȠϻǩǫ',
                            '1',
                            'ϓǡ',
                            'эʞўȏŭΞ',
                            'ҟςȩϗӝ',
                            'ƙ˞',
                            '·ː¶\x98ʕʕɄƛΠu',
                        ],
                },
                {
                    'catalog_name': 'ǞΛҏЋϧſІǐΏ8ûʃǄӮàΕƓ7ɒΠӄєƱϑ\x8aΪΝĮƚȸ',
                    'locale_codes': [
                            'ѥкJȱ',
                            'ǐҰϋƮԌ˾ƌЦ',
                            'ɽγǂ',
                            '»өɅάύbɲ',
                            'ęȁЋϲҜЫʕ˕țӅ',
                            'ˮ',
                            '\x84Ԯ',
                            'þ˷Øś',
                            'ԚИҞϞέцӶɖτ',
                            'Ͱ\x86ĶİʨŬ',
                        ],
                },
                {
                    'catalog_name': 'ϘĐӌɈǠǑѦłsцˣґÅ9ǟĻƎ°Ƴ]JʲJȢ˺ϭƵ',
                    'locale_codes': [
                            'ϨȡęƧƮŖϘφǋr',
                            'Һŏ',
                            '\x8c',
                            'ϩɯԨǣ',
                            'ќʈ:ςϙƇōѷ\x88ϥ',
                            'ȡиȧѪūѴ',
                            'îƚЮ;ũДȝȩ',
                            'ɾËίӯь',
                            '²£JȷǨŁŁ\u038b',
                            'ҦϒΠʟɹ',
                        ],
                },
                {
                    'catalog_name': '\u038b˪ђĹɅеÑś|ΧHʻӨgҰʪ¶ҩĔĄŋ.ЃұȦ\x92',
                    'locale_codes': [
                            'ǈĆ',
                            'ԋϽϠYˣЉΥ',
                            '!ϐ˛ÊȜӧaſZ͵',
                            '\xa0Ŵϡ',
                            'ʡщԎǆМíÑϐΑ',
                            'Ǉ',
                            'ȓ',
                            'D˭ǁƛê¯³ҙ',
                            'ĺЍѮˎɔĻÊϢ',
                            'Ԓ',
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
            'name': 'ɋĩϓÙ˖ʘπFŶ2ĄӶǜϙԢфæȠ?Ľ\x9fόˇǝïɢθtƃғ',
            'code': 'šή',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'X',

            'code': 'ˁ',

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
                    'name': "ʰȰŌӗʝ҄'|Ŵŉѩɡг¯ҭǣęjҬɌʙ·ȒǑʆƔśûƿĠ",
                    'code': 'mɤ˳ү÷',
                },
                {
                    'name': 'ŔƗɍϺp˴ϲҷСȘ±ʂʍđͽ˟ҧ˔ԓÌҽĦӯhΜȓԁӸɐϐ',
                    'code': 'ȳˇ',
                },
                {
                    'name': 'ŬWˑҾŃsˤŵɀŎоTƀsƜԏƸΑх´ҸӉɻǡιGӊуӜӑ',
                    'code': 'Ԯԍ\x9eʧ',
                },
                {
                    'name': 'ɀ>ΐˊ˂ӚDŔǢ ҰȴįíȮ\x7fкѰӒЍ,ĝɻą»ԦʺɹʐŤ',
                    'code': 'ιȊЅnŘ\x7f¿',
                },
                {
                    'name': 'дϣԥͼјͿ˵ʿӍǠƱ\u0379ӞЅŕ˔ƧȇОɲ˥Уǜʬɻӥ˂ĞέĢ',
                    'code': 'Ұӈ£әҫҴ',
                },
                {
                    'name': 'ϛϡӆБʦŭпԂ¸ʙȠϺ\x8aqϿȺɲīɮЮmϴ>Ď\x96ǌβɠѳι',
                    'code': 'ƇǗƏʫǸԐƸ˳',
                },
                {
                    'name': 'ɘų˖ĤОӍMŠnԭКÅBˣӧԒΌѢ\u038bΜ.ȓ!ԅ˓ѿӻǝӁɾ',
                    'code': 'ӗ',
                },
                {
                    'name': 'ǚƶʊвό˖ʠŬ|ЄħɃɆɐ˴ӝjĪ]бԠОги\xadԕγԡϑμ',
                    'code': 'ȑƈjѨҐȥ',
                },
                {
                    'name': 'ȳȨϓ΄ǲǛY8ѥ˃˶¤èеΐ¥ȘŅʕ˝ƀҷǠŘŴӤˮɒΤż',
                    'code': 'ĠС˟PM',
                },
                {
                    'name': 'ШѿŋɶsȩûИʚўʎЅʒφӛĔқɮŒřƽӍ\x9bĨʕӶłԗĨè',
                    'code': '\x9dêʤ˵ɀҊƤŀ',
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
            'locale_code': 'ρŗԀVŰδӗ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': '\u0381',

        },
    ),
]
