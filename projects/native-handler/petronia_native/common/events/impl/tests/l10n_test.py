# GENERATED CODE - DO NOT MODIFY

"""
Tests for the l10n module.
Extension petronia.core.api.native.l10n, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import l10n


class RegisterTranslationEventTest(unittest.TestCase):
    """
    Tests for RegisterTranslationEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_TRANSLATION_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = l10n.RegisterTranslationEvent.parse_data(test_data)
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
                res = l10n.RegisterTranslationEvent.parse_data(test_data)
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
            'locale_code': '҂ȊõӬΌŔҟƋ\x8d',
            'catalog_name': 'ΤĞƣӋҒƃƉɌμɒ\x82ѭ\u0380НМÝεӳƷʥРх>ТǍΘĞӢɩɁ',
            'message_file': 'ÁǹƌцŸɒбʂǀƀԙȨȚԃ˅ʯҷнŪíəɌåō7ˢĐϐСԪ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ǆ',

            'catalog_name': 'ɨͶң',

            'message_file': 'ДŨ',

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
                res = l10n.RegisterTranslationSuccessEvent.parse_data(test_data)
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
                res = l10n.MessageArgumentValue.parse_data(test_data)
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
                res = l10n.MessageArgumentValue.parse_data(test_data)
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
            '$': 'ÕЯԙҶņǽ\x7fc˒Ŧ)ŃΛҩӶһĹÌˑӕʡɔȊы˖ϣͻϸXĿ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -7018693041665500752,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 176446.39894801943,
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
            '$': '20220523:220036.140753:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ɧЋԍљʎÅIҎ\\ƈŸJ˪ұЦ\x95ðǽҰģў÷4lҤзӜґWү',
                'rƒТϜдΒÄΔƕİРǸπĦɍǏӎǦԝ\x9eԉѱɘʘFԨŜҧɋ\x8d',
                'қʪȋƂȮȐʏȁϰá¶ǓҸԈɅÑȮɦŋεϽŗʜ·WԐÈʂͷӏ',
                "\x82ÏPªΛκȜȼщŨÝŀ'гБӿȅƆҀÖŜɸόьǚČΛǃȫо",
                'ÊɷʜĭɏˎYоǑѴɰϺǄ\x91ˊЫȖϋҿŎ˘жоѲƻũӴыĎȬ',
                'ұ}ҐȎʍǀǍѿĄӎϪҖƱʊΟхʃ¥ΤϾχĒΘщbβĘК˧X',
                '¾π˓ΟƨËȈ˳ŸȊȑԕɸ±ěѫĥȉҲǶȗɱĈĽʄɲȸɥʀԮ',
                "РЙɋȤЇΐ\x94υԤǹф\x8cъɉӲ'ѧϱΑÝŜŦÞĀĠҐɣȦʭ˼",
                'ϭˍώΤϽč\u0382ϚųǴƟȧȿǅŐɗҋҸǨӭƋєԨ[οЫȉҡɫa',
                'ҾmӓԤϱȅd>ҫͷͶ\x9bǡдǳЊÃɾƔѺ^`δԟ¡ϝcӛӧЋ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -225989464159782490,
                -2038019757365237042,
                6260317208781626288,
                3114558785207941468,
                -1231553567156402703,
                -2328305787161072840,
                -3781966372009550136,
                6511151544866457108,
                -7380004328459060609,
                1481316476089419288,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                332515.36251120316,
                735917.1677762811,
                610878.4622807225,
                456455.5348124027,
                651857.1592510226,
                201568.86201875808,
                211678.66653194214,
                781631.6221244171,
                561175.2332115857,
                511806.5841621009,
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
                False,
                False,
                True,
                True,
                True,
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
                '20220523:220036.145789:+0000',
                '20220523:220036.145881:+0000',
                '20220523:220036.145970:+0000',
                '20220523:220036.146064:+0000',
                '20220523:220036.146152:+0000',
                '20220523:220036.146239:+0000',
                '20220523:220036.146327:+0000',
                '20220523:220036.146414:+0000',
                '20220523:220036.146548:+0000',
                '20220523:220036.146646:+0000',
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
                res = l10n.MessageArgument.parse_data(test_data)
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
                res = l10n.MessageArgument.parse_data(test_data)
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
            'name': 'єĊϫŸư\\ӉәΦ˾БğӧȩȠQγгʰ',
            'value': {
                '^': 'float',
                '$': 371287.50652287673,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ɸ',

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
                res = l10n.LocalizableMessage.parse_data(test_data)
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
                res = l10n.LocalizableMessage.parse_data(test_data)
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
            'catalog': '¬PĥԄūɂƕȧȔǊəˀ',
            'message': 'ƿŕѼбΎԇúѯȩčмȓĹFȆЄ1ŠźǧƀÃʍͽÑӝƕʅŜǙ',
            'arguments': [
                {
                    'name': 'ƥȣȽàύòѳӪϻҗJФùȱļÆÕÎӊ\x88ѾɩëŏÇɔʦ¢Ӽ˂',
                    'value': {
                            '^': 'float',
                            '$': 84126.64916624746,
                        },
                },
                {
                    'name': 'ʪAнɶʦûçέřβѶљ8ʹȬʵëƜÌŮѧÁЃ¼ɀƢ[Ӈ\x8aЎ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20220523:220036.131622:+0000',
                                        '20220523:220036.131747:+0000',
                                        '20220523:220036.131834:+0000',
                                        '20220523:220036.131917:+0000',
                                        '20220523:220036.131999:+0000',
                                        '20220523:220036.132080:+0000',
                                        '20220523:220036.132161:+0000',
                                        '20220523:220036.132242:+0000',
                                        '20220523:220036.132323:+0000',
                                        '20220523:220036.132404:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ǦàΈȬәӰґΔɥǿ3ѣŃǤëĕөʯ˚Ѫҙ(ϐŏȸ¬',
                    'value': {
                            '^': 'int',
                            '$': -1209933893496006108,
                        },
                },
                {
                    'name': 'Ĥ\x95˖eȉŕʟfѱγ\u038d\u0378½ρа²˽ĿӿѿүΈɒϳӛμɺĶϸʵ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ђƗӐÍίKöϰϠ˩ĊъËåĸӥЎʷүϣѱŽ1§ϝΣԀƝȶӳ',
                                        'ƻΦˉзȲ˲Ⱦ¥\x94϶ѭȼͱлƏύ[мɠœяǆѧōΉɩǲɟęʿ',
                                        'ґχЯǧЕŷҳȏwˆE)ΎʪǘƥҀӯĂĚӽѪŮЙǉŦ\x99ШyΓ',
                                        'Ɵҏ_άȻɿ7ΰuΊŖäŌӠyɓδǯhƙõҎӀŲˆȟɒͺɤˮ',
                                        'BҠĬҴĨēü5˄)ĄĲΖíˣЈʴĈŧΈP˫χƒ\x8e;ˏҬîΖ',
                                        'Ǌѓ<\x97ԗî\x98ҥΒϨźIϴǜΛҼʋnјѥεɀɮ˥Úłʳ\u03a2϶ɟ',
                                        'φʞ^͵чƒЋν҃fӺȝ¹҉х˰ӷЊǹȕǓεŚñŷǛĭѭϤɾ',
                                        'x\x9eɣ¦ӎ\u038dȚЀʮ\x87θĶѨфɲʲХƿʴɘ4˴Οәß¦ќλǿЗ',
                                        'ψεÇɷʞTɯοǕЗɴԕƀͱ˶©\x9dńҏʐԥŎͺǣɌΨ0Ώĩϱ',
                                        'ɕʞƧɞŶ˛ƍЄяŤʓmȞəċʙģҒγ˞ƛ\x8bǘ>ɰŔSŵɦd',
                                    ],
                        },
                },
                {
                    'name': 'ϿƂγĩ£¥ǎΞϽш˜ŏćÇpͺ˘ľȵӃƫ͵Ӛц¼ƬɌǥϲӳ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        False,
                                        False,
                                        True,
                                        False,
                                        False,
                                        False,
                                        True,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ԧˮɹ\x8cΛɎūˤɚđ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        True,
                                        False,
                                        False,
                                        False,
                                        False,
                                        True,
                                        False,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ǕӷԠЂǹųīŜҙʞАԤǉ˺æɰÔԀ',
                    'value': {
                            '^': 'float',
                            '$': 558276.9304311504,
                        },
                },
                {
                    'name': 'ͰԨɂ˧ƈӍ',
                    'value': {
                            '^': 'string',
                            '$': 'ĹǨǗыйâˇƁ·кĴƶžдӚԕȡѫÉѱǷӀԔȀϽқϖρΓК',
                        },
                },
                {
                    'name': ';Řк\x94ҍ˼˹ĭʆž\x8c˷ʠπǎƺԧ',
                    'value': {
                            '^': 'datetime',
                            '$': '20220523:220036.138098:+0000',
                        },
                },
                {
                    'name': 'Ў*ȈӻӢҽӁłԧ/ŒƍǷLǻ0ĵҺғѶaϲҀϾɴɜρһˤЈ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ϸѡ',

            'message': 'ӵ',

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
                res = l10n.Error.parse_data(test_data)
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
                res = l10n.Error.parse_data(test_data)
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
            'identifier': 'ϴ£@JԐѪ)\x84ʬ',
            'categories': [
                'internal',
                'file',
                'configuration',
                'invalid-user-action',
                'internal',
                'internal',
                'os',
                'os',
                'configuration',
                'internal',
            ],
            'source': "4˪ʬ˓ȏģҼȻуɨн¼ƛяěǀΰϸΞð'ǽӡΤʾÜӎӣʐˁ",
            'corrective_action': {
                'catalog': 'ĩχ£Ϡʯ\x7fȞǃȾѲÜ˧ΌȅŗˈŜ¡˭ũʊӿʬđØɑ\x9fљǢŽ',
                'message': 'ɗ[ίїŸÍДԂд˘ăΜķSȚo˄ĥ\x98ôņчƘǰӖɐķԘ ʪ',
                'arguments': [
                    {
                            'name': 'ŗɅǳΊЌBʴҚ҉ƚѿʘŅͽϰǰƨī$ĈţѴ»ȰӠ˳ЪѾ˶҃',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20220523:220036.120820:+0000',
                                                        '20220523:220036.120903:+0000',
                                                        '20220523:220036.120982:+0000',
                                                        '20220523:220036.121061:+0000',
                                                        '20220523:220036.121139:+0000',
                                                        '20220523:220036.121216:+0000',
                                                        '20220523:220036.121313:+0000',
                                                        '20220523:220036.121391:+0000',
                                                        '20220523:220036.121469:+0000',
                                                        '20220523:220036.121546:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': '(ϛȔέ*ө˃ԄԂŤӟϴņȌ˙%ӚɳǬ\xadƦľϴ°ǢɮıϤÀХ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'Ƶ˓ҕКȒʑҦǾѝ\u0379Ȱ˫d¦wͳѢZÕȞϒΖхțөѣ}ʦϹM',
                                                        'ёȱČʴƫϕӢкӋ°ӳIҢ\x89žűŉǍĳǨѰϐÃŤ%-xŇΥϤ',
                                                        'ϡɲ¶ͳԉɨ\x8dфџĲʕРу$ҶϐԆуф\x9aɞƤЎľ³ƌǫдéō',
                                                        'ѠҮʀʊśҰЉʂŧɘԟĻáșƌBʮϮЇ^ͿàξȠÚҤĭʡ҉ʹ',
                                                        'ˀǀҬɱǯј҈Ɂȴ\x9aˊԌҀѓϏʹҼƫӸƇ˷ͿΊ7ɳӹӮϧǛз',
                                                        'ƾ\x9dŤ¼ƬÃԠȍŎ¿ŗȲÆRŧćӸĳŢͰÍ.FĝɄŁBəɺÈ',
                                                        'ǸͽĂлϑ\x9aҧ\x86Ϛϥ¨ԦʈˍвÓϲĽOŕʇҔŰĤʴ«ŵN~Ʌ',
                                                        'ҵόǝ^ЀŤϣMȫчʅʐiYѸѾǷϕ˂ł˼oǜ\u038dƨʬŲϧIѶ',
                                                        'ԅҹǒǓŬѧӭƴǬМИÞŻĂ\u0378ʥǜɚʍŽѱқԝƚΟƁƢRөѪ',
                                                        'ǣțȤÏÐëǕHaɟɩð˽ō/ЧҾԧ\x8cĚʁǑԒʽǵ\u0382ʤˀƒѓ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʟ0Ģĳˬɋ~\x8d\u0383QρĝΥʣԡ˅ƯɅЃľˠĨĎΏƔĢԢ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ɉȒЮȚӇȉ˔Ƽǲ\x90ғȶŬʢǱQɣӪʕČ+ЫɊÔĠîƘΫԍφ',
                                    },
                        },
                    {
                            'name': 'pĎǽѠȻ7ǧĊÃ\u0379ʞаΰv\x8fǞ˗ʊðЖɲˏ·ɕƷʣŶёϊţ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ƾđȁɛӉΰϹ_ϟƋƢɡÕȑ˰ǞςӘŧѡƎӨčΕʞЋŁӥҭҏ',
                                    },
                        },
                    {
                            'name': '˖ɇθǹ%ůўӌɾ˜ɖ-ɏà˗үƅҨǚŜFѸъΫəÿ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'əуҿʕŔªӼЃÏӎѲƶŦǐŚИ΄ԟĎҲˢğҾԜвύƷɛȣk',
                                                        'ӡØʫƅӒѣҊȕƈÖƜǓǖԔԘ¶Ϧԭϡ҅{ԈL$Ԝ,«ʦиҏ',
                                                        'tǍĿ˃ǒ£ж0$Ƣ¾ӥэˑˬəʁǳԀϛϷʞҏǴƝ¦җʵҘx',
                                                        'Ρђ0ɒΈZʞˁʳ\u0378ЈʴˋƅȖğˮ·Ɗ\x8aЧŏҥӚʅͰ\x96ƔάÙ',
                                                        "'ˆӮƝıˎ˺ļŕ˘Ԃƹǎî˷Ǩʐ˺ϠSďɛĳ$ÙĖΡ3ƱŅ",
                                                        'ɡШÑ˃˨ηĸӐ^тǙºÉƑÜԥԒSӢӽӉƳǜͼӳǝbåƪЅ',
                                                        'Р$ӡ˙ʞ҂ͳȣ¢ÃȅЋ˩\x8eɶˇΣϓªƤкЙҟϺɵüǷȼɑΠ',
                                                        '\x96\u038dB˅ƎΑġǮѭϏč˯ɦƾ҃ӭ΅ŁәƞȡʕͳƌAѼĂþƸǽ',
                                                        'Ư҈ʤÝ ĥȏϮĢ͵=ɨŭϫŸ˩ΦȚ˔ȄºҟϜ>ŹϨ\u038dʃçĀ',
                                                        'DŪʈ\x91ǉЙʩԋɦѸƉġ҈ºъəǑҽҦȱĊȀ\x94ʖǭßĢ˳ˌǛ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ÜǢɌӱТ϶ɓȳӐ҂íНθÿ˴ȜȜЇЩˇѸxʁӆѻʙɺѿ',
                            'value': {
                                        '^': 'float',
                                        '$': 844328.4545502631,
                                    },
                        },
                    {
                            'name': 'ÍζʕɋϊƟČȫθs\x8aÝĉá-\u0378Ωó˳ĞŴЧξƸΤƐÚȅҗώ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        838139.3182011094,
                                                        -48998.25367398636,
                                                        877102.4473617733,
                                                        592005.4509276174,
                                                        129843.24951793632,
                                                        587479.4564436696,
                                                        377140.44409096765,
                                                        996562.6133578925,
                                                        161010.24691823308,
                                                        545680.9085137352,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ΡȂ\x85Ⱥӂȧx˔ҧ-ψʦǀʯÚ˜ѮÈĦǵЏʙҚѶÄǋƓӒþΩ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'Ñ\x9bƪɉBźǏ˙ʻнˌʌȳɉƕſϹȌӼ_ɥɧǹƳōƶɿ\u0380ҭҐ',
                                                        'ШôӆɶЏӹӾ˜ρAЍƈǻɭi¿ШѺ÷Ěʴ\x92įżǇ)ҙň¦q',
                                                        'Ġԟ&kÕƶ\\ŨӡЩɡΊ˶ʫ?ęoϻʙƕʗâńӂ\x97ьΤ˲Ʌǰ',
                                                        'ȷԉԩҎʵ˳ҺʛŤʈÖ˷Ʉ²ɌȲɶ¬ЃȅӹɠɛʾćÎхƀѫȑ',
                                                        '¨ѶʚɁBĠƍȥȚȃϦɒўЕˮɾəǍҹДq(җɜɘ\x8aňǻɧҖ',
                                                        'λĿɼɺǑƋ/òƝȐпƒùʘϕɏƄQќ°ǏɥʵӘĀԧњƌùʀ',
                                                        'ɋʓʂʫªӊpδЏƑɸǭӼϓΏăтûɺҽ\x84Âgͳ˚ʊɠδƔƲ',
                                                        'ɋȻЕ\x90[˟7ά\x8bԏÊҍɻʍÙЁ\u0381Ƃì\x8aʀǩ\x84ÜǛӪԒȬƕÊ',
                                                        'фЅйʹȱʭѳħŊMȎƹȞϔμΤɇыZʪƿæĩǏȎüőӊŵѐ',
                                                        'ɝΒƖ\x83²\xad«HҪř΅ϔӆǠѿŚЗǩǝԔƟȥÓΤǁˎɡǦxͽ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ɷΰʯķƊÀA\x87ϱ\x83ЅȾʞŹ\x9b˳@ӠũʊĨʦʘȨϯʉ˹ɢϕԓ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        False,
                                                        True,
                                                        False,
                                                        True,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ƝϯÙɣ8ϛ9ĻˠļѦÊ˒ʫҡԕɅԮBЕΜϳƫԙѽӲ',
                            'value': {
                                        '^': 'float',
                                        '$': 813148.4431920765,
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ѷÜϻëˌ˙cӌ˗ƭʔ·ʕðԃƀҶԋҗðȱʋѱǶЗĺɚěɏЬ',
                'message': 'šԨϹƖ˖óҏjğƞʌӸΓƛɂěϞĄſ҆ϷŞɇҟçҹϊсЄӨ',
                'arguments': [
                    {
                            'name': 'vѾ',
                            'value': {
                                        '^': 'int',
                                        '$': -5224081270578781965,
                                    },
                        },
                    {
                            'name': 'ԭçͱ¨İ΅9@ƲɅȁИŮDǋ®ðǞÜȐʰƙʦ\x92ʺŌƥʫđҗ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        True,
                                                        True,
                                                        False,
                                                        False,
                                                        False,
                                                        True,
                                                        True,
                                                        True,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ǻӎʕϒ¦ѮȻѐǢιſҡĢíόЏŃđғσSíǒĎќΞұǶ\x92Т',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20220523:220036.149479:+0000',
                                    },
                        },
                    {
                            'name': 'ʵũƊ¢yΎŚȈƟǴYП³ɮïʁЍȃĜӂ\x85ʷŶҋϿˇƲsӴϺ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        True,
                                                        True,
                                                        False,
                                                        False,
                                                        True,
                                                        True,
                                                        False,
                                                        True,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ɃýʘӽЈѐëӾÓѳҹԃȨĺѵҏ˱ϙĘТÛwԄτB}',
                            'value': {
                                        '^': 'string',
                                        '$': 'ņÄƂΟċɹǻƽĦѧǵ\x81ǹӿǜŪȦaўǇǜӮɸùƫΫǀǋ˼ϖ',
                                    },
                        },
                    {
                            'name': 'А×ˑũǠǌ\x92\x7fχԣɓĒʯљȍһwҷșŴɉÊÐơȃϓØǆ#Ǡ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ӳªnȩŨƚŷГǧǅýƃȞҪԡzыЃ¸čʶƥǚǷȟʙœΙЪȍ',
                                                        '\u0380ǵҷȽʷΦ\x89ɬŅѿӛͳ\x99ҵ҂ůśƲüōηЃʖʹͶ¤ƳҭӜМ',
                                                        'ƚȾɻѝ9˞²ȅϧ-ɦʨӮϒʚ˘ӕЇÍʽӼ҄ѱǪĈů¥ΚȱǓ',
                                                        'Ϫѱ~Ŀė\x91ŽƔDέĕd˜ϣŘɉƸǰѵâ\u0378ЇɕӒͱˑϣ}ΈϘ',
                                                        'ņȯԀʑүĪЁaйŰҷˬǱЄԃєʢ˹ĮυоԡТȓΚÎ\x97ȾőӞ',
                                                        'lxьѓɁʃʠ\x98ÙmλҦΞƮӒΌĨêWεɉтːͰāҰ\x9fʼʶԅ',
                                                        'ȍąΒȏΘйçÌǂ҇ҊǎѷǣȦɿϪɖÇВ˘ӈщŎ~˩ĸ\x8dЃs',
                                                        'ϥǽȈ˩Ϥϸıǒ\x98ʛɪ²ǪiΌςΘԟǧɏ¥yϘǏϭɠԖԋ˘;',
                                                        'ΕΗǭɩϢȐɘ˯ѐĄЄʧђϻɜҽѰҏԝʅ\x8bɵӶVщ˼μI\x89Ң',
                                                        'ϔΌ=ĎԅЫȟȔϣʅɡǕǺģǁø4Ǵ\x88йÈǼ\x95ɭѱӎϡПƣɢ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ŪǉҦƿʩϡX¢ʋҗǕƊ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -3904765327198803516,
                                                        -3360551406858320087,
                                                        7683234530639852787,
                                                        3336361014929178066,
                                                        1234014820083541428,
                                                        -526269933698814806,
                                                        -1961011920517572207,
                                                        -8211880218628596010,
                                                        -4058480069303536972,
                                                        -5467589465155974124,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʬ˩ŁúЬϏϾƿǶUɐʊβʏ}ƬưѶǛ\x9dɔԝжȒ-Ѕζſˍň',
                            'value': {
                                        '^': 'string',
                                        '$': 'ɡȱΝɏêȼ\x92ѓЮϜϼЍΛΠ$ЯʰʳşˆȢԅBҀǃȲ¦qɼɳ',
                                    },
                        },
                    {
                            'name': 'зΤIśǧɥȁtɇѱԙćԏǠȩԙҲa',
                            'value': {
                                        '^': 'string',
                                        '$': 'ȠԐœɼǯƏɯƿру˛ŊȐϬљӪʼ¼Ӂ\x8aʇоϦƈԆ\x92Ђ÷>Ѩ',
                                    },
                        },
                    {
                            'name': 'ʇҶӼʐ˧ƔŃÓřϵǆʊȇƳѣӞɾȁƧʋ\u0383ϭ˝ԍю͵͵Ď]Ԛ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ԤĤϭŏˎϴȾȴËˌĻɷΏȃԑѱДˡƮƐѶGUˉȠƧ«ËĔİ',
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'PӂȄ˳ƪ',

            'categories': [
                'internal',
            ],

            'error_message': {
                'catalog': 'Ȝǌ',
                'message': 'ü',
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
                res = l10n.RegisterTranslationFailedEvent.parse_data(test_data)
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
                res = l10n.RegisterTranslationFailedEvent.parse_data(test_data)
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
                'identifier': 'ɼǈ_ӴԕоѨҩSƼǜ*\x9aʔԡԚōԤԫΨķѝŖęʻБh˝³Ʈ',
                'categories': [
                    'internal',
                    'configuration',
                    'access-restriction',
                    'file',
                    'internal',
                    'os',
                    'invalid-user-action',
                    'internal',
                    'network',
                    'configuration',
                ],
                'source': 'ɦɾɮҶԦƤЮɢҔԘΥǬʇöɂӞԔȄÄԐŹ\u038dδΦќ˄s˶ÈЎ',
                'corrective_action': {
                    'catalog': 'ҸҥϱƟѠɮԖʏʮķǆӵʼєćνƫϷrɣȝҋ\u0381ͺ˨Ñ˅ұǁƩ',
                    'message': 'ĎɬÆù˧Ƴ«ЪèŎϑȘГȽɋ˽ӣΘöʁѮвƝҎFԖʠʿĴӞ',
                    'arguments': [
                            {
                                        'name': '˸ҏťϐǰǫк\x90āӯӡκƏȂЧćӨ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220036.099259:+0000',
                                                                            '20220523:220036.099383:+0000',
                                                                            '20220523:220036.099464:+0000',
                                                                            '20220523:220036.099541:+0000',
                                                                            '20220523:220036.099618:+0000',
                                                                            '20220523:220036.099695:+0000',
                                                                            '20220523:220036.099771:+0000',
                                                                            '20220523:220036.099847:+0000',
                                                                            '20220523:220036.099923:+0000',
                                                                            '20220523:220036.099998:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'yʅΉ҇ˋÀʬɚƥӺE¥ŬҫĉυÏ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'gȈΪԪӿǒԨ¨sPӼȲ.ʈʢϻӗӈύϟ˼О´ΛӉИğ¬Ѐɣ',
                                                                            'Ȏ?ˇȸКVʇФӞϫʣӗ˕ɺӠŭÌņŠʨȍǨЭÆɽѣϖΐƼđ',
                                                                            'ÊȞάӊϔøȦγǥԓʴ\x9cαеϵӪǧґԘʍłΓǃʁÛԛȚÓɆʉ',
                                                                            'ԫϸʌ͵ѹʌӒZ¹бòŪŖēԝɞʖŒгaeҝɜώӋʺʦЂΗҩ',
                                                                            'ЕюǔȬѬЍԊǌğvǇŀõZΣ¬ЖȩϐƘϊ\x91ȑ˩ÔȧҮǏϕӍ',
                                                                            'Ƽ@ӌΒĶʫĳİʟ%΅˲ũ·˼ԧʛ˼ɶ˷ѳȟȦƴƜԛȡaўΝ',
                                                                            '{cpмǑѪ×ТÿюŸȜξĚѿѶöΉҩӵњËƨӶ\x90ҪǪΖƶþ',
                                                                            'ɍĮχīδ(ǎѩoЉȠĻθǱК˯ѠĲяÚ˺ÖϢxƔÚāѵѩŪ',
                                                                            'ʹµҔʅϠǼƏғҗԃǰǙС(ƃaЎʯœԄЗɄSʹԮƦϕƯȫÉ',
                                                                            '@˪ʧҤǁ\x80ÆʿѫɂΠǡҬ҃ȹ¾ϏÉɉƔβHȧҴƱƔîĀʃҗ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u038bŖǢʜƓϪĤӸT΄˕ΛƬЋЀñGқ˳ɚĄΛ÷ǟƗ\u0378ҬȨЌ҃',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѥűÄϋΥԦƠ˫Ӛƫϝ\x9aȏȔˉÕÈюɨȹˢИҝùÃӑФ˩Ӷ\u038b',
                                                    },
                                    },
                            {
                                        'name': 'ʿĊºƢΑŁj\x91ɰɕΖѡĦʜ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '2¡ΈюĚɕˁæÐΡĀţôɏԡǂ\x8b˅шȩɁȲѴΘsǧǍǵӶȔ',
                                                    },
                                    },
                            {
                                        'name': 'ҩʌ',
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
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʒѠԀüįӈƒʻ\x98%',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            166079.13307529868,
                                                                            -73323.02738603075,
                                                                            -52039.20103652102,
                                                                            342520.39310695394,
                                                                            723710.4679651308,
                                                                            412633.1060825294,
                                                                            427929.00490540883,
                                                                            801071.3159593071,
                                                                            72919.15240552602,
                                                                            113229.52200570473,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'œ˓ԢʃзƵʮϐҐѥВǬ)ȡθкǶɭөȜŊӔɕҭɪðХӃĢɬ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220036.105005:+0000',
                                                    },
                                    },
                            {
                                        'name': '͵ǩҦʋыжԞ˅ΓҒУ\x88҆šŘїǌÝ҃˂',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӜΣ˛ĬĠwǣӭ.Ðɏäœč1ǦǈʙЮή˻ɕƽǨҤԠϢȉŨ¢',
                                                                            'ȐӗʳҨōʯǏ˫<ȕƌ˪˶KƁż.ϚCӃȢ\x85ƊˢĺРʡҫӛʣ',
                                                                            'ѺРå)ƾ÷ɥĜθùǹĢϪ=҅Ć1жǲϳʞˉǜ˳һ˸υ¶"ϓ',
                                                                            '_όåŎĸІP`ɞĎ\x89ŬÀvƴѬɤԪΩ,ɦÝ˽Áҕ÷@˖ғɎ',
                                                                            'ɼРƧǻœ˜ŅРüͲʻÖÐȤȍþЭʞúSŖñ\u03a2b¡ǉѬΥԧҌ',
                                                                            'ϠșȌϕӂːŅʞŗ1īŲɞɱҨ˪˽i\x84ȗКȭʊгκϕȉúȢƁ',
                                                                            'Ȣìǖá˥ӅӏǉgȈѽбȘя,rǕčˀЂ\u03a2ĬkʦęςǗ)Õū',
                                                                            'ӛʜԜӀˢZơИä\x97ψUҝƾӅƜѕήДǑҲɖʀ҂ǔǕʣŹƻɍ',
                                                                            'ƔʱŊӍŋMŃаҲŦӋԂǠĭĹ&e˄ɼɜȍɑԐʋαӲ\x9fļηΧ',
                                                                            'ɍɰӇӥέӴ-ɚӟÆүʹ°αŞɹǱνĹȫҸƺǱҒɼГ҄ӿʬԣ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʇĥĬ;ÎҸ˪ȔʄĝϢҺ˞ȣʦԜ²˰®\x93Ѝlˇ\x86ɲuƃǏԐћ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ԥЀҽŠ˘ɊF¾@ɼͻә',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3416194316895100790,
                                                                            2877494088033067215,
                                                                            -8630451482625972850,
                                                                            8547268129504994622,
                                                                            1494563012735452121,
                                                                            -7595634937135605749,
                                                                            -207712750779093874,
                                                                            6937730582072798772,
                                                                            -2456521054893449720,
                                                                            8186452022990883117,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': "Ŏ΅ǹɅʣȦԘȠ˅ĜћƻȈˈ\x89ѴüY'ȿҘȷɣҋȾķoЦϦ*",
                    'message': 'ĈwͱӾĨ\x9eϡ(œԣĪsҺҜīʝԙâԡқƻύǗѣ¤ǟǢϘјӺ',
                    'arguments': [
                            {
                                        'name': 'Ξóŵđ˙\x94ΣìǩɒΝˈƗJʌИ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4575198873337715297,
                                                                            -489412983751971152,
                                                                            1602421137014503513,
                                                                            -7897441762743712741,
                                                                            -8052058254740749788,
                                                                            -4474659758823519152,
                                                                            3342484442520398083,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˶ś`ǇʧώӨȊхðǱŰʕŊcϳӕұĩҫ\\\x81n;œʞѕҍāҼ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220036.109746:+0000',
                                                                            '20220523:220036.109824:+0000',
                                                                            '20220523:220036.109900:+0000',
                                                                            '20220523:220036.109975:+0000',
                                                                            '20220523:220036.110049:+0000',
                                                                            '20220523:220036.110123:+0000',
                                                                            '20220523:220036.110198:+0000',
                                                                            '20220523:220036.110272:+0000',
                                                                            '20220523:220036.110346:+0000',
                                                                            '20220523:220036.110421:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'şǅ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220036.110975:+0000',
                                                                            '20220523:220036.111051:+0000',
                                                                            '20220523:220036.111126:+0000',
                                                                            '20220523:220036.111200:+0000',
                                                                            '20220523:220036.111274:+0000',
                                                                            '20220523:220036.111348:+0000',
                                                                            '20220523:220036.111422:+0000',
                                                                            '20220523:220036.111496:+0000',
                                                                            '20220523:220036.111569:+0000',
                                                                            '20220523:220036.111643:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȞҒ͵ѷӐԈhɥʏȹ¥\x83үŃ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƩԜǈxϸƢӷ\xadǩˎˠȝҡűǡǿĩǚNԦ҂˴ѴÀʼҿмŎ˲ƌ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 742815.9645991339,
                                                    },
                                    },
                            {
                                        'name': 'ԧԘɑ,ÂӱʽӽѐÝтҚΣƻԁɓĴЁ:;ϮŐħ˕ȳ\x97ԙýǯϷ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            820575.3381981703,
                                                                            292156.4903788706,
                                                                            864052.9429724964,
                                                                            24433.59611971033,
                                                                            169719.68748494977,
                                                                            466162.0949461061,
                                                                            -40750.13354944459,
                                                                            495474.7488302408,
                                                                            614311.6679565912,
                                                                            764808.5974466843,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ќǮġ´ƀɴ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'YiÙĀ Ӱҟ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2788114253998166382,
                                                                            -1975370506530316370,
                                                                            969398899158672858,
                                                                            -4228092623037882481,
                                                                            779900226271113516,
                                                                            -7523671279051687116,
                                                                            1881910662848462893,
                                                                            2035924058553429784,
                                                                            -7933376390730544884,
                                                                            8508774480139221778,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʦƶˈ³ӧǌ/Ҧ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 786152.7612332872,
                                                    },
                                    },
                            {
                                        'name': 'Ӣ˻Ҷҹ#ƶđĉѡ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220036.116693:+0000',
                                                                            '20220523:220036.116771:+0000',
                                                                            '20220523:220036.116847:+0000',
                                                                            '20220523:220036.116922:+0000',
                                                                            '20220523:220036.116997:+0000',
                                                                            '20220523:220036.117071:+0000',
                                                                            '20220523:220036.117145:+0000',
                                                                            '20220523:220036.117218:+0000',
                                                                            '20220523:220036.117292:+0000',
                                                                            '20220523:220036.117366:+0000',
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
                'identifier': 'Ԣƭ_ʊɧ',
                'categories': [
                    'configuration',
                ],
                'error_message': {
                    'catalog': 'ʠ\\',
                    'message': '˞',
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
                res = l10n.SetLocaleEvent.parse_data(test_data)
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
                res = l10n.SetLocaleEvent.parse_data(test_data)
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
            'locale_code': 'иŪøϚʱ\u0379ώƒŝ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ϲ',

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
                res = l10n.RegisteredTranslationCatalog.parse_data(test_data)
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
                res = l10n.RegisteredTranslationCatalog.parse_data(test_data)
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
            'catalog_name': 'ưӳˍñǹҫ^\x8aŲіͻ˦ȂͿƢͷƝɸɢϭƈȂӊǤʔӪӽԛǘĢ',
            'locale_codes': [
                'ǈơˢȖǠ˺',
                '\x99ƃėțɼ\x82҈ѣĤ',
                'įɪГӎɼ',
                'ΜϦϮӯ͵¢Ӫ˥',
                'Ųƒƻи',
                'Ɂŋ',
                'ɠ',
                'īϏıĻҥ',
                "·ĕ¢]ɞ'",
                'ӲʳӍў',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog_name': 'ΠʝѴ',

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
                res = l10n.TranslationsState.parse_data(test_data)
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
                res = l10n.TranslationsState.parse_data(test_data)
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
                    'catalog_name': '˵+ίçrƣɅòύŀ˶ьƉғǒάčƩŅèѩ΅IӣǛ¬ғϟԧѪ',
                    'locale_codes': [
                            'ĺљӔ\x8d',
                            'rԞǫΘ\x90Űʢʗ',
                            'čöɣÆˉ',
                            'Ѧǈ',
                            'ŪƭŹΛбºūˮR˽',
                            'ˤ',
                            'ɩ:ΜχǏĜàŒ',
                            ';Ȏ',
                            'ȡӂ÷ʽǌČ',
                            'Ǻ·ӛŗһǚ½',
                        ],
                },
                {
                    'catalog_name': 'ιΫȨʢǽyҳKɜʾëизϿLҋΣξČϧ,ɑĘŰȭψмұӼæ',
                    'locale_codes': [
                            'ͶϐӫσʁҳԦ',
                            'Ԉьϼ\x87ʍԦϼγцК',
                            'ɍҸӧӟȟζџԅ',
                            'ӬС˝ȣ҆ŊǦϏɆ',
                            'ԉɨ\x85Ő҇ȵîɍς˺',
                            'ϹʽɷΝȺ[ȼȨӊŷ',
                            'k\x95',
                            'Ƨΰ\xadƢȋǿшȮ',
                            'ԭ',
                            'ǳΣ˪ǽþԓScĳ',
                        ],
                },
                {
                    'catalog_name': 'ѯmԡ3ǐ',
                    'locale_codes': [
                            'XГ',
                            '͵ԮӗĮŋВԫҘťĵ',
                            'ϿЌˀΝҡӈҿ',
                            'ӺəхȺ˻ŌʛӀӇ',
                            'Ҭиɷʏǐ',
                            'ѳтЋÿńǿΪ',
                            'ǄƦϛ˃',
                            'Ԍ˾ǈʛ',
                            'ɪ',
                            'ΟЁ5Ʋ˭ŴѩĘԧӉ',
                        ],
                },
                {
                    'catalog_name': 'ƐӤɀȁұ#ӌ\x84\u0383ϳԊʵƦ+΄˘ĵǞƎç\u0380ƓȈӰϙˠΝҨœϣ',
                    'locale_codes': [
                            '͵ΟƤéɧ',
                            'ɉЙΥοӮϗoԞ',
                            'ҟ',
                            'ƙʿŬѢ',
                            'ίҢӓ',
                            'ɩˊԛϙAƥ^аѷĮ',
                            'ȪԑbͼŇȢȸǿ',
                            'Ğ',
                            'ũī',
                            '³ҏŁ˄˯',
                        ],
                },
                {
                    'catalog_name': 'ӂ7ǚǄ¼ıј҅ӅʡЇɉĒǆҧŮƲӨČεˏ¹ԎNǘҿƖӕ\u0379ɉ',
                    'locale_codes': [
                            'Ƀ',
                            'Ƚ˩ҐĻΚûЦ',
                            'ʽ',
                            '$iǯU˻ЗπһԙŰ',
                            'ѕ?ўѵ˟',
                            'з¢ŷёͼёхqκǤ',
                            'esѷũǴľӮȨˁ',
                            'ԒňѼʳ',
                            'ԜρȚ˾Τő',
                            '9ǌʐɧͽĿӣԥԇ',
                        ],
                },
                {
                    'catalog_name': 'ΞҡʁƥŏáӰǰέöёåCύјѼӲӔʸМѢɶșˍʴУҔL×Ѻ',
                    'locale_codes': [
                            'ԐŚĆɊɓǄńˬϕ',
                            'ѳыУYF©Ž',
                            'ˋ¡',
                            'ʨаƩѢE\xa0қɧǖ®',
                            'DÛж\x95',
                            'Ԓԛе',
                            '¨6Ѣ',
                            'Ȝ\u0379ŮϼĒ',
                            'ʇҷɒǦƔXΰ\x8e¼Ĳ',
                            'ƹʙļҦĤŐʮ',
                        ],
                },
                {
                    'catalog_name': 'ϭϦƯšƚЅԮԩ0ǆˋnȓˢƲ҆϶ǦӖȔӣŃǑԋҰÑʤʡӳŊ',
                    'locale_codes': [
                            'ҕ\x90ϷʮʫЃ½ĞѪđ',
                            'ʁŇ˄KŒ',
                            'Ӵ\x8aӐҊƥђ¡ɨĈ',
                            'ż',
                            'ùʫ',
                            'ʬĀӍ˙ǫХ\x85',
                            '˒ӌҷωɳЭʪр',
                            'ʳ\x81ȩ',
                            'uöɶԗ',
                            'ˤӹԖñʂưřϫ',
                        ],
                },
                {
                    'catalog_name': 'ɈƞҦǴ\x99ƂpɍɺԩϿѽƤԜЙɩĠƑϕϖɴƻ=ΛţGϰȔҫϣ',
                    'locale_codes': [
                            'ɭ˥ЊʮАˤĄǑъ',
                            'ДЎѧ˳өԆι҈ϟɡ',
                            'ĠEɶ\x85оBňJ\x84ˉ',
                            'Š',
                            'ϐƯÙŐſ=ĻXӦ',
                            'ĔӘǆфˉȱċ˂ӭƇ',
                            'ϚʶλƯϫйĨɕƣɛ',
                            'ʥѤҌЭϑϢɚ˧ʻ',
                            'Ϩ\x9bĭɱ˪Ļе',
                            'ɮр',
                        ],
                },
                {
                    'catalog_name': 'ĉĬĚ`˽ԝӰŏԋŲ˶˺BгԭǝїԆƗˁҗҊ=\x86ņѠоȃΣϔ',
                    'locale_codes': [
                            'ƛθȢ8ʹßң',
                            'ӣĮʏϏϛȁƧȿ¡Ȑ',
                            'ԥϖãС',
                            'ˑ',
                            'ҭ\x95ϸӏ˃ɔ',
                            'ȭЃΕҊ',
                            'Δ',
                            'ɱӊϟ',
                            'îʊ',
                            'җȚǴѾƤΈԌ\x93Ѕß',
                        ],
                },
                {
                    'catalog_name': 'ͿчͱԙƥȯvΗ\x85ԭТΎǘ˖ɈԁӧΕВ˱ʿȈӬʛ3ˈɤɲїȞ',
                    'locale_codes': [
                            '¦СǪҼΗˆ',
                            'κȊЮx',
                            'BԭȧѺòǞȐºԣ',
                            'ǀ¹',
                            'Ӏҁɋa',
                            'ҼˇѢ\x8cæťĕȔɕ',
                            'ƦȹѮȓӉ\x99F',
                            'ҒĭǏҀȪŋѥőʙǷ',
                            'ʰӔɖǃ',
                            'ȍѧ*џʇΩPȨ',
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
                res = l10n.Locales.parse_data(test_data)
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
                res = l10n.Locales.parse_data(test_data)
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
            'name': 'ҳ\x81ϔϢļ¹gƻξǻЦƹƎϘɷ\x9cΘʥ˔ſƱˤёҙѝɫɏίÝŇ',
            'code': '˧ζӐРŉЇλ҄',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ԉ',

            'code': 'ʖ',

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
                res = l10n.LocalesState.parse_data(test_data)
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
                res = l10n.LocalesState.parse_data(test_data)
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
                    'name': 'ðɖŇŨjʿʓǹϏҬŞҠпҴϝēΡȮǕ\x87ԀʘԃȫÖóКȄ\xa0σ',
                    'code': 'қX',
                },
                {
                    'name': 'ĴùćцĆƧȘӄȞѰͶ˦ѦίЛͻˮŨэю¶Ά˷n\x8aщӐǮ´Б',
                    'code': 'ɹʞŷʴάȊͺϾǸȳ',
                },
                {
                    'name': 'ѓʸǱȪ<ȆưêŊ\u0382ЌĞˁČȸʃсńωìƾҪмļƷɟŲžͶϖ',
                    'code': 'Ɩǖ"ϥ;',
                },
                {
                    'name': 'Ӏħp\u0383ǈςǤʪȋоôʨ͵¦˞óǎΥɄО/ӈĥ\x85һґȀѾ˔ŏ',
                    'code': 'ʣҧȊԂԁūѕ',
                },
                {
                    'name': 'ʬЛƙʾǮe½ɚ\x81ϘèŖлʚĄuԥÀYԄĿb]ӗËюͼaĂǎ',
                    'code': 'Ȕéдʋ',
                },
                {
                    'name': 'ĵǧÖӏԫɼɜΩËɎ{ɓϥϖƘƣυнѸι;ǌԀ˳Γ\x82˫#Ԗю',
                    'code': 'ŤˀĪЩ',
                },
                {
                    'name': '}ɄΣȃrHʛӲ˕θ!ʷȇǫӄɚӇľͷçɧɸŉϿΐҪӒԡŴԛ',
                    'code': 'T/ĝνª',
                },
                {
                    'name': 'іpҥ(UɶɂϪǻϘÌп`ƤũƩθϻДɏȖİĶԉ\x9c˫ɇrСγ',
                    'code': 'ӲɅĥӰʶʴӐ',
                },
                {
                    'name': '_ǨЁțϐǞɠǍ:Вɺ«đәȣŶȚъ\x7fʙѺγnȼÚɔƕʜΆƑ',
                    'code': 'ÛȜ',
                },
                {
                    'name': 'ϰɼ<zωΞҹȹɮЍę˷ʸіȄЮ»ϤɌ5ſ˭ʵНҥЍɦ}ˎ\x9b',
                    'code': 'Ͳ˙ϧʊʊ҉˳\x94YŮ',
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
                res = l10n.ActiveLocaleState.parse_data(test_data)
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
                res = l10n.ActiveLocaleState.parse_data(test_data)
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
            'locale_code': 'ąӁ˝ĳTξȆ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ý',

        },
    ),
]
