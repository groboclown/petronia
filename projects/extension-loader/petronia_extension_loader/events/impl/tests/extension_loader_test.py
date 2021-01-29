# GENERATED CODE - DO NOT MODIFY
# Created on 2021-01-29T19:26:19.123955

"""
Tests for the extension_loader module.
Extension petronia.core.api.extension_loader, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import extension_loader


class LoadExtensionRequestEventTest(unittest.TestCase):
    """
    Tests for LoadExtensionRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOAD_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionRequestEvent.parse_data(test_data)
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
        for test_name, test_data in LOAD_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOAD_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LoadExtensionRequestEvent'),
            ),

        ),
    ),

]


LOAD_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'Ѕ\x81ҷϜҊĉȸEĶϖDѯЅ˷ɃЧϬϛΨϝпBӀZΙÞɪǩԌư',
            'minimum_version': [
                -5298646335337034471,
                -8681042517545415230,
                -4070028935416461314,
            ],
            'below_version': [
                -636927034141209371,
                -4127211446797708889,
                -2726495589134620497,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ǐȷѸ',

        },
    ),
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
                res = extension_loader.MessageArgumentValue.parse_data(test_data)
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
                res = extension_loader.MessageArgumentValue.parse_data(test_data)
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
            '$': 'ЇĐӄX˼ЩӛΟўхˢоъ¡ԝѥҕŗԞƭŤƫЋϲƌαϐƗŜ˕',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 8500608508035682522,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 267456.25292086235,
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
            '$': '20210129:192619.038950:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'õШ˥ȎӮɝƅ\x84ηơ˖έͼƨİǚĉϩϠ\u0382ЩŨkҢȑɿťîƓл',
                'ϡƘ˓Ϭ˟ũŰ˨ɤмĕƅлȥԔ˫ɓӊ\x85ї˄ΰͱХСʪǍʧɰԥ',
                'ȥƴτɈµΩhø˖\x9cѫĲǥçŠˠԍѦ\u0380ɝǛØ\x92\x94ŁǹҎκȽǥ',
                'ҏĘżɊΛ˽νŇϡȞȁ±ʚ\x86Ȝǌ\x8bªǚ;ʒϤjƀΜӾì-ɕѲ',
                'ʧkͲŬԦʧėіċџɱ¿ÔЅӆXŬͰӏǭІÑԎȩƇЧ~ʌԥ\xa0',
                'ѧϷĪ]\u0380ĺŮǗǮήʡїɱѺИѣúÅˁаʀ\u038bιԒɚʬŞƇ[Ѓ',
                'ͱǊҧ\u038bԛ´ЀŎʪχěϪƇӈƷʱȣȝηŧʐȑ˱ƳѰЧΦţ˞Z',
                'ȊԞǞŹʮӜҍɡї?ʘ\x8aåʋ<ѕ»Єԩӯϩ\xa0ȩ\x8cˈʨењŞȠ',
                '\x95ςӒč9ǵĠƔӮӴͻǚѼıΫɻĊЇ)оÿ«ËćĜҤȻ˯Ɂʙ',
                "jѯӁ'šǢưŒʞ˵ɵʭJѠhҗ\x9dɗſȓЂôԘƁӈґːĉԘä",
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                1819935883334713903,
                -796659902003344498,
                2474132285420190995,
                6226235118306102040,
                -7628582938170009044,
                -2504991696572383526,
                -1790289144478129064,
                4061166859412768019,
                -4384105015129770674,
                8461937571279994611,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                790558.1510555465,
                401565.9308593508,
                248433.3685481021,
                241942.84742654272,
                494969.91243407014,
                690381.8945244725,
                809447.4461099977,
                636839.5339802754,
                796750.5062698283,
                231911.61065158626,
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
                True,
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
                '20210129:192619.039814:+0000',
                '20210129:192619.039826:+0000',
                '20210129:192619.039832:+0000',
                '20210129:192619.039837:+0000',
                '20210129:192619.039842:+0000',
                '20210129:192619.039846:+0000',
                '20210129:192619.039851:+0000',
                '20210129:192619.039856:+0000',
                '20210129:192619.039860:+0000',
                '20210129:192619.039865:+0000',
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
                res = extension_loader.MessageArgument.parse_data(test_data)
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
                res = extension_loader.MessageArgument.parse_data(test_data)
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
            'name': 'Еͷ˔ŅȰȨɩƶϡ¯Μ΄җ\u0383ʃaĖĔӮƴɧҋІй\x85ǔƐȼ)ǀ',
            'value': {
                '^': 'int',
                '$': -8584202887515261236,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '£',

            'value': {
                '^': 'bool_list',
                '$': [
                ],
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
                res = extension_loader.LocalizableMessage.parse_data(test_data)
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
                res = extension_loader.LocalizableMessage.parse_data(test_data)
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
            'catalog': 'ζӽɤϠ˷ϧǚĚԡϫď\x8c2ēеǞЄʟ˜ЬΘŤːʩˣЃԬҨɿ´',
            'message': 'ϏŜȉȂξѲǀӭȋÊÃҞӮɭяȪҢ˯Ϡđ?ώØʢÊ\x98ōηԦЕ',
            'arguments': [
                {
                    'name': 'ѣʲŁ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210129:192619.035892:+0000',
                        },
                },
                {
                    'name': 'Ϋ<ZΛÒɬϩΨӞԂԬǱ\u0378˃ӾѮʲҲѥĈԙӮɡÙΗŚ`ҼȴŁ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        309899.3794850288,
                                        92779.69529233783,
                                        483769.64894694195,
                                        653180.7515808127,
                                        518027.86910805467,
                                        620548.6647463941,
                                        268254.66147271404,
                                        35935.371021419065,
                                        -74795.31274101092,
                                        160317.98425878384,
                                    ],
                        },
                },
                {
                    'name': 'ŃɬͷӀӐȵʦͳŲȏσ²πɘҘіíҞÅʠžVÏ҃Ēí,Ɵӂʈ',
                    'value': {
                            '^': 'float',
                            '$': 909515.5886495592,
                        },
                },
                {
                    'name': 'êʬόƂŇԬÉÐ`8ň\x8fȌƐԡÖҙŔ˽ŕɸɾüTΨǜү\x89ŤF',
                    'value': {
                            '^': 'int',
                            '$': 1480134132435380493,
                        },
                },
                {
                    'name': 'ë×ȬŪʛǟȢʬ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210129:192619.036569:+0000',
                                        '20210129:192619.036579:+0000',
                                        '20210129:192619.036585:+0000',
                                        '20210129:192619.036590:+0000',
                                        '20210129:192619.036595:+0000',
                                        '20210129:192619.036600:+0000',
                                        '20210129:192619.036604:+0000',
                                        '20210129:192619.036609:+0000',
                                        '20210129:192619.036614:+0000',
                                        '20210129:192619.036618:+0000',
                                    ],
                        },
                },
                {
                    'name': 'όŴьĠ\xadƷņ\xadƇĉʃϺΘќϸҦħӝƋΏ$˭Īlż',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ŕƗѦǺѼ~ɼӀºƂǻ°ǬâàԫϥДțзHʩӸʡŐɷҪζӫԎ',
                                    ],
                        },
                },
                {
                    'name': '2ϺȰʆȴŎҜƐ˯ɹшсÖ˭άнӘǝy҄hѨ\x7fӵƊˑɢǻɵg',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        584843.0143726482,
                                        -6364.238253307223,
                                        515391.33822856005,
                                        158530.44223916947,
                                        298101.7589420912,
                                        470568.15056107217,
                                        275182.4423444344,
                                    ],
                        },
                },
                {
                    'name': 'BɡƻʽÚӂВʂͲі˷ÃƜ*ȞԨ\u0380Ǘȟʘԕ7Mҫʆöɗ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ŧʛˈΧȽΥ\u03a2:ǝΟÄƻγУшҀԕƩ҃ѥżөɜԈє҅\x8eԟɸĨ',
                                        'ҋLħżȊӰ½ҕ\x81\x99Ӎ˱\x9eѓԤϱʤbӷÉȿґbĐÚǕDҁĈÏ',
                                        'ƉÌƓϠʢ˺ɤҪфĉûϮЊвЅ<ʼъʈÈɿԒȗӌϜȃʥÿęă',
                                        'ŞÂωЋç\x84ϻȃρŞƪԆаЪʨҍ\x9cǦƌ\x9b£˛÷˞Ŗ5ҩ;°Ǒ',
                                        '˜ǿ»\x9aƽɑ\x89ҞżȤȿЃЅΩEϽ\u038dŔhȼϦˎ8ɇţХӠʮ\x96ɫ',
                                        'Z\u0383˻ƭψ˽ΉȜ˄ðǩϚǶĘΡʞхäʽœ\x9eǇØğʺβԀԖʵ%',
                                        '˦˺˹ɗιIƤϼԢƶѲӤAę@ϢăǾĈАϡӐtǞĤſԢϢƏ)',
                                        'ƒşϴϝͰLӵѝǶԈИƐƧĖΆàʹǭǃҷ0çҷεɄ3ÂǺГĪ',
                                        'ĿθϗϴƫϤГʹ¤ŮŎюƍǾӺӮ"СǱ˫\xadţƈʙҫҤƙȶȸʚ',
                                        'ƊЎýĄb\x9e\u0381šżýӒʅЬϾŬƇiĳӓͿͼZƕƦԉ4Ӝʸ÷ã',
                                    ],
                        },
                },
                {
                    'name': 'ЇѿĘɟӳʽɿӼ,ɟϧӓΩϤĀ',
                    'value': {
                            '^': 'float',
                            '$': 332598.429494018,
                        },
                },
                {
                    'name': "дƯΏѼÕ¡ɲĈ'ԠЉń½Ι³˛ȈHϲūӊҩ˽",
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'μ¥Ԁ\u0382ÇǊӾðͰ\x97ˣĂсӗǭɴӫɖčŮ\xadŗĸҞӠ³ϫǋ\x92Υ',
                                        'ȤЁƦɢȖ:үͼɳ˗ғԍƹԪѹEЛÃâɚ˾δʌǕ˥šѮа;ɇ',
                                        'ӚÜɛͲƒԧƒşѧΖħ5ÓČѐ˻ӆΚҠ·ȠÒӑ»Ѐԁӹx˵ѿ',
                                        'ɴЗҼ4ԟ\x98ѹЃʏԬˋr˨϶҇0ҏГʸСͻʢҚɦ«ҏԫѰƦϑ',
                                        'ȷЦKЬϱȕ\x9cӑͼЯYǊƟЦ\x8fƽɝ\x86ÓúsϧɻðҰȁƲԮΰȇ',
                                        'ĜШ҂ɹʨӐϝœʉʭƋˢɵÖŉ1ϚҼοȁЪŏūĘѓǀɏȧȘ˛',
                                        'ŜѰǹƁΐˢǄΩПƂϿÞƖĨҽƓзϹƦʵöǖŜʟǘ˒ʹ¡ô=',
                                        'ћĩǹҤˍɃˊϚӢЖĐεϾԁ\x9bӁЫȺǁҹ·ƥȟȩѾ\x7fȴˬÊ˒',
                                        'ѐ·ɀԬe˓ϡ©ļrƧψΩǺҝʻäԧȏτŪȬȅ²Ĥș˱ҏĘǃ',
                                        '|Ϫ\x94ɝìϴ˞ӫtσðȤƲǜjԚ\x82#εŚŊʮюΏȧлόǍϹö',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ƊҔ',

            'message': 'Ȭ',

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
                res = extension_loader.Error.parse_data(test_data)
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
                res = extension_loader.Error.parse_data(test_data)
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
            'identifier': 'Ԑйr\x8aΡ˵ɄƐȺϱ˺ɫƽĜƙΧ\x8fԥʐєɮƍ\x9bØѣ,Ɯͻįѫ',
            'categories': [
                'network',
                'network',
                'file',
                'configuration',
                'internal',
                'internal',
                'configuration',
                'network',
                'network',
                'network',
            ],
            'source': 'ѧΩӦĿνТӱƘǤӑǇυ˂њěʽԅԍũťҾǦԌѭϴάԕȷƜɷ',
            'corrective_action': {
                'catalog': 'ӒƻеұǺ¬ӥҙƓȰ˹î0ƘЃǬЉýƧ҈Ü3ЋϵŮĂ\x83Ѧƾģ',
                'message': '?ȡçԙĢЉт\x87œѐԍȴʂeαǎɲЂҴy\x93ļ#ǈˈtā·ɦӅ',
                'arguments': [
                    {
                            'name': '\u0380Γ˻ϖđɿ¤òφҿғΎуМíҺÿćϊƈѡ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ϐïΎIӽîλѿêɺʁçҍԛȰҭʢѺǐͺ\x9aҗʩƑvĂǇȅвʕ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ҵԑӀäƾʫă:ôԬΊΜӶ\x82ѰӎΒӽòġѷ҇·ɲ¯Ԙ˹Gζ\x86',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210129:192619.032767:+0000',
                                                        '20210129:192619.032784:+0000',
                                                        '20210129:192619.032790:+0000',
                                                        '20210129:192619.032795:+0000',
                                                        '20210129:192619.032800:+0000',
                                                        '20210129:192619.032804:+0000',
                                                        '20210129:192619.032809:+0000',
                                                        '20210129:192619.032813:+0000',
                                                        '20210129:192619.032818:+0000',
                                                        '20210129:192619.032823:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ȥʻśԀƑ/ʺЊиÕȝȷˆ\u0381¬ʿҪ\x83˭ǳ~ʝÑЧэtˣ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ɈɠѨLѠĸŖ,)ШŤƊƉ¡;ԀĺΟ0Șŀ¤Īό˦ŎӚΛŻӲ',
                                                        'ѿƑуξͶъҴѷ\u03a2ѩÃқÆϮˀϕ˼ŷƺԅɞЂѾϠвӮԔȳԫξ',
                                                        'ҧǞҿҼˏϣ\u03a2\x80¯ϏёʜԜȈԑ˫ɻØͻȞ;ѣŘɷɗԀϊɾϲǠ',
                                                        'ѯÒίǤќ7ʨ˲˒ɜ\x8bΔɲ@ϺɃΏΓϐϾЬҽƷɲšӥɨҝĮв',
                                                        'Ԃ$ϘɓȑҮЭʍʦЖӮɔс6ŎŹĂɤȝˊϨĚΦϩұ\x93ҾΓů\u0381',
                                                        'Õϣɣɴ˩Ǡɇʽ˸ΛɔǪŰϞ˟Ρ˖ӯѰ³ɈӑɎƷĘ7ѦͽҰȲ',
                                                        '[ԩҾȑ\x9cыϝʚЀΘΔÛѠZƑðǏҐQЂ˦\x97ПУҢ˯ϾƟ҂ȭ',
                                                        'ΌǒfDģϜҝҍ˧ȋăɛǆęȍѪȧľɾʒʝӾ˲΅σYƇȡ|˅',
                                                        'щɀТϪζѱΊɕŐūŮӻ[Ő˞\x93ŪšĦɼş¢˼ſҎғǮʳҭ;',
                                                        'єύʀɈjͰęřӣȑƬǴκԟѼzԄϰұGʥѱ½ȃħϺǩƂӰϾ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'л}ŀ˝Ǡ\x81ŷ·ƱԇӾȦ˘',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        505035.6000320384,
                                                        101575.75982629685,
                                                        272763.05242516974,
                                                        367095.5370044805,
                                                        459717.8025214608,
                                                        256988.76989602833,
                                                        485925.6429464801,
                                                        277287.0122742336,
                                                        57966.22085759271,
                                                        867662.603927231,
                                                    ],
                                    },
                        },
                    {
                            'name': 'rƛȌˢҺ',
                            'value': {
                                        '^': 'int',
                                        '$': -1137567467759070550,
                                    },
                        },
                    {
                            'name': 'ӫêаԮŸ.οʽҍӘӓƠɤ6уɶ˫ͷЏʧ˝ǰӭɃ˝ӥӧȴŬӪ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'БуģƖŖgǇόϐěӵ5ӞЂ΅\x87ΚɛǜҲˆϸҸӭMњī(ѺÇ',
                                                        "ϑǒ'ъЫ¦ѣ˚ɥŘĠżϯŞȳˬǞńЌё҆ƮÝĪƹɵŀňшú",
                                                        'Âɐμɜȑ˦˨Ƅ˽ŜʯΕʡʣͳ_Ο´îɤ(КƬƃÖ°ʪɩƳҬ',
                                                        'тϴùϡ\x81ĴȉўƃſұcԎҊƟΛÒʈϏ˟ɡӟăɠȂƅʶkƄȑ',
                                                        'Ø<§ҺŰȸВ˙Þ҂ҿƧƯƾǲӀЁуԒíɸˬɷźVрԗ³OȽ',
                                                        'ʶɷýҨƗ8ĕïЧҸĒ϶лƴƄӄŶǒԓѣͽҪØǖZ\u038bэŰƘǳ',
                                                        '˫ǗǯΊɼȬњǡHħYѢϷáӲͿŸΒΒˮÀʷċЦƥīȮȷԖҾ',
                                                        "μȽҞŹʪӅĿ=ƞц×(ǵȿάˆ°Şɑ'_NgφʴțȂƴпˠ",
                                                        '˞ūn˺ÛʆҤΚʺĞȺǈÂԔĨбъŰза\u0383ő˄ʻÀÃ²ҿζȧ',
                                                        'ē҉$ȿНŢ[µѴɧ˰ԇъў;˞ϗșԞŪΏrIΦгʋ$ɀԣ˜',
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ɏ6ɞ˞ӘԘȄ(ʇιӹӘ΅^ʀӧÅ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        991096.867376064,
                                                        743716.2851826637,
                                                        419195.6422981241,
                                                        780048.2480849639,
                                                        99328.7586567085,
                                                        654663.732114529,
                                                        993755.3972020468,
                                                        74080.28860466709,
                                                        848501.1170991008,
                                                        299083.2235085929,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ԔŌ!ƅЫˍȉȝЫȶ8оȬζ$ʹ¬ǹ˜\u0382ɦáʍİВȅϴ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ɇȔȮFŗŘњÏԄ\x9aâІƀǬȢΎӕҮϔοԁʲӞŹѺƁΓΕф˲',
                                                        'ЖČϊɗƤТŠɎǢҮŸʭϸЈУӫȄ\x82%Йϒ^śǙʦϖҌԕəġ',
                                                        'ǶѼ\x82\x98ƟƒGѣӑǋïѿύeɏҞŭ)ŌħӁóɜѕҘж`ƼƧǏ',
                                                        'ȧˮϭȟǴ˄ψϏΑΊԨΝώӶЧтX·ʴԮǅ\x8aͳЖͶ Ņϳ΄ҽ',
                                                        'ƶƗwһ˪Аa¬μТԜѢŻҘĕӶVgҔ¼ʞ¶Υ˥Ű*Ͻ˹ɨö',
                                                        'З¶ʽίÖΈКCӘʐΎɖšβĉѹƔѾ҆\u038dɠԧPЎч˴ˮӏұǴ',
                                                        '˸ǝ˃ȕЅʾʾϳuϣƛғԌӘȷӰӭͱΙϺgIü˂ÜәǍɸ=р',
                                                        'ÀˏɰΒԋ<ԩŻî¼BƐļΈȻWʄʢϚɽˣ¯¹μѭӰƦϋӲƤ',
                                                        'ɗˡЄ\x9dʑưĠʀņϣӡ\u038btϹф<ēNɍȞϫʏˀкʪΓʿБԞҔ',
                                                        "\xa0ʑJγϲ\x82ΤҲҦԐǾɧ\x9cϼ˹ϐ^ҏІ˂ŉȀĽδ'ƌʚҨÛ»",
                                                    ],
                                    },
                        },
                    {
                            'name': 'ωʝǀыӢ9ïÒɺӞӾȺθӁɓʇӳBҕњҙȗƄ˶(˲Q¤Ӳ\x87',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210129:192619.035095:+0000',
                                                        '20210129:192619.035112:+0000',
                                                        '20210129:192619.035119:+0000',
                                                        '20210129:192619.035124:+0000',
                                                        '20210129:192619.035128:+0000',
                                                        '20210129:192619.035133:+0000',
                                                        '20210129:192619.035137:+0000',
                                                        '20210129:192619.035142:+0000',
                                                        '20210129:192619.035147:+0000',
                                                        '20210129:192619.035151:+0000',
                                                    ],
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'γȂӦ-Ȋ\x88ЪΑΟćǑǷƱűŊŦԈςɷϬǓфӶŃӮȬȼǱӡѿ',
                'message': 'ɘϤÑҩèȂĸȠɢӒoҖǰΦЏ÷ӜˡŦƭЋȫmf˘ƵϘǻшԚ',
                'arguments': [
                    {
                            'name': 'ŠȧҸk˯\x7fòȹϟpяҠɪʳПʄҸƝѢΘɊƂϻ4\x8b£±ЧĸԜ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ӃЃҖϗƊѨ7˪ɚȤѤ˾fƅɮϕʝвo',
                            'value': {
                                        '^': 'string',
                                        '$': 'Ϲѩɹʞɚůœƍԏәϸ\x9eˣɄńέҺưωԖǔһӊɱɋθɞ ŏ±',
                                    },
                        },
                    {
                            'name': 'ξŒȊ\u0379υɾ·\x87ʖ\x97қxϯǔFљ\x92˓íΕȝĔӷԘ²ƚɇ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        True,
                                                        False,
                                                        False,
                                                        True,
                                                        False,
                                                        True,
                                                        False,
                                                        False,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǙÍ¥ȦˉEлƥǅӤӲɥƮӦəŷĻ͵Ëϓ\x99ʳBêĸҡǠӬ ʇ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        False,
                                                        True,
                                                        True,
                                                        True,
                                                        True,
                                                        True,
                                                        True,
                                                        False,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'щԬ˅Ħɪóř΅ĐĶͷĘͿĄәҍπÓéЕЇĚ',
                            'value': {
                                        '^': 'int',
                                        '$': -7677622650988429674,
                                    },
                        },
                    {
                            'name': 'ð9\x8f\x92ëâƟƛƄϭъB¥ˠͳĪԖΤ\u0378ņƂϸƌƛдЃï˶ɕӕ',
                            'value': {
                                        '^': 'int',
                                        '$': 6174785994847533076,
                                    },
                        },
                    {
                            'name': '\x84',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': '\u0380оŅӂƺǽʘˢƐіʛȩǼŘ¸ҸċНȾǧ',
                            'value': {
                                        '^': 'string',
                                        '$': '»АxʦʺҺ\u038dӽƐǋ˃\x94ŇĚĝӏάĹˆютӰӵƜϕBƳȔͲ\u0381',
                                    },
                        },
                    {
                            'name': 'ǸϤη˽´čĎӛȰ˜ъʩʒȋϤђӨӔƬǒԩ˩¦˸',
                            'value': {
                                        '^': 'string',
                                        '$': 'ԦѰȵюҧкſÿ\u038bʢϟȶˏǧˤΛǳŜэɴԮП\x8dİΟӦѝʵ%ǔ',
                                    },
                        },
                    {
                            'name': 'ИĲȽɘЩˢН¢˹äЬ\u0383ɡҧ҇ĘðǒͶŌ\u038dϳǃϗEθʛȬęϖ',
                            'value': {
                                        '^': 'float',
                                        '$': 22230.872199536418,
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ɄΖˇӵƊ',

            'categories': [
                'access-restriction',
            ],

            'error_message': {
                'catalog': 'ĨȾ',
                'message': 'E',
            },

        },
    ),
]


class LoadExtensionFailedEventTest(unittest.TestCase):
    """
    Tests for LoadExtensionFailedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOAD_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionFailedEvent.parse_data(test_data)
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
        for test_name, test_data in LOAD_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionFailedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOAD_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LoadExtensionFailedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='LoadExtensionFailedEvent'),
            ),

        ),
    ),

]


LOAD_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ӷЧǖ˘ӓʾǧϱǙ¶ǐ\u038dъłʞǮЋǻ˙\x8fАΏѪԉʗőÕ\x8a˚ˌ',
            'error': {
                'identifier': 'ʄZϷʖЧƐĭƫ˙ʳκЬќėsȀp{vyƬǅǓϜűęΌЊѿь',
                'categories': [
                    'access-restriction',
                    'os',
                    'network',
                    'network',
                    'file',
                    'os',
                    'access-restriction',
                    'os',
                    'file',
                    'internal',
                ],
                'source': 'Òʨ˛¯ĕEшǰѺӕϸĩCǺÐѯ«ҍ¡ƹ΅Ȝð¨«Ųʻ˴ыԩ',
                'corrective_action': {
                    'catalog': 'yƋȷѯǐѭјBƩƟϲǗȒǌУ\u0382ŗĢҽͻįɛӷ@ȆҘŖˬ\x84Ũ',
                    'message': 'ġ˒½ΚɖɞȽ˯ԨЧǴҗΞϑԝԕőӋņV\x8aǼɂ×ЃǵǮԣʜů',
                    'arguments': [
                            {
                                        'name': 'ñҸíԘфǭҰmˀ+җϑҾÐ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 228348.26121408545,
                                                    },
                                    },
                            {
                                        'name': 'ԢλŶҐͽªŦѓəmȈ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҢҕƊͱԞКΛʂѝƣӣΤð×ąԈϛ%ǁÉ?ǂüЅȎсˋǄЭǑ',
                                                    },
                                    },
                            {
                                        'name': 'řĕӫΈєкȑ˵\x86˷,ºȦ˾āυƁŌʗȈiԎԤʈȰąԢ!Uш',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210129:192619.026469:+0000',
                                                                            '20210129:192619.026495:+0000',
                                                                            '20210129:192619.026501:+0000',
                                                                            '20210129:192619.026506:+0000',
                                                                            '20210129:192619.026511:+0000',
                                                                            '20210129:192619.026516:+0000',
                                                                            '20210129:192619.026521:+0000',
                                                                            '20210129:192619.026526:+0000',
                                                                            '20210129:192619.026530:+0000',
                                                                            '20210129:192619.026535:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΙųӶ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɩĽӞºɴ˨ѫťǉJʅвӗϮѾҺ˝\u038bpǅҐīˋΓȻ\x95ϙǕɈӄ',
                                                                            'ǆĽ\x80ӲǝƬFĬĬУӁüyÑͻɸƐkґÚѪƖǝϾȈÇњлǲё',
                                                                            'ę\x7fҊġȧľ\x9bʅлºúӜȭŁǀ˃ƼҬ˦˹ӫѤЇϪðʰǔ\x81ţŢ',
                                                                            'ϾӇŦӒ>ś˨ԘԆɏʉʁƧϬʝÑȜƫϔƦǹʦȩńőӮǞ#ñº',
                                                                            'фýй˛ϸΏҗɸӗǊ÷ʆ;Ϊƅ҇ǲɫbĦΣ%ǧϤɏϳΕıҚ}',
                                                                            'ìӾѠҝ±ɇѨƕҶёԄ\x9dŝ˄тëЍаɯԂұȧͺ\x7fϧГŮƈØɁ',
                                                                            "үӕӇˉˑĜͽĹЎϠԟ˲ȟϹӻ'ɯͼҶӽƭĊ³XƇҺ<ėą˥",
                                                                            'ʼ\x93ɨɕɕd϶ПҦɰNˌΩϑӈьŝ\u0379˫¨ЮƻҖˌОϫ˅йȗ·',
                                                                            '&ŰӉ˜ԈɅӈϻыͿҗҖħύĞƙӌїΥЭѩйљȅͽҫƟͰӀѷ',
                                                                            'ǉƛǵƞǰȥХÓǑӕHʑЇȥːΝ\x90ǟԉМ҂рͻȼ_ԒͻʞњƸ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǹ˰óѼCҀǍƓ˾υиʋǸpђн˒Ñ҈˗ȟ\x88хİţ\u03a2ʠʃ\x9cϟ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3165822064346461787,
                                                                            -4733415355883232066,
                                                                            -6812926120117682572,
                                                                            -8972636803449333230,
                                                                            626369217760805742,
                                                                            6610289036108661611,
                                                                            681196499542352389,
                                                                            -6629393582269640370,
                                                                            -1328064343546738812,
                                                                            6481964135550103270,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЅȓƮóˬ×ʩǨӸπÂȳΖ҄ɁҧʚgʩҤưƽūϐҌԇWОϱÚ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5434631338755553802,
                                                    },
                                    },
                            {
                                        'name': '˨ˣʐҮϚ΅\x94Β҄ˎɼϱŶҌø',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȲԒ҃_Ѯ¾ɽõÌ\x9dЪԇàФŢМXΠӦӗϑΪɓ»ѯƒĠ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'ʈҦӶãʲéƥ˖,ϒ˩ӹΤҶ ɀÆԀ϶ˡʹӤĀ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2457392533407174514,
                                                                            2233449247460842530,
                                                                            100628082055446850,
                                                                            -8936134434931634926,
                                                                            -2341418700971193938,
                                                                            -8562658135929848403,
                                                                            -4894158740642482134,
                                                                            8447113987693640149,
                                                                            -4692233169987496346,
                                                                            3277398761875855995,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ғUԌƺЬԛˡ]ƳН§ǊȦ.щǸԫύǗԟΦĦ\x83Ǭ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            674176.3884797744,
                                                                            152883.87533615777,
                                                                            381617.0509851261,
                                                                            -46794.333702749704,
                                                                            837741.9322581684,
                                                                            360998.16745407565,
                                                                            -76010.77408293527,
                                                                            -53557.10764115758,
                                                                            428049.0418769781,
                                                                            351454.7967629676,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': '6ЏғǍƥÝҷĪűsȡѤκķˇͻʭȩ˳±Ώϩ\x9aʛŃҹWýÑϱ',
                    'message': 'ɱɯƐјŲǪďˆψϯƚĢϦƼƠΜϣɥÊƽúНĲѳʥȽƙˮ˒ŀ',
                    'arguments': [
                            {
                                        'name': 'Έ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҉ԊŃáѽʵѤÓА΄ӲюіӟɢӿgºʏӏПɿΏҺώĹʞGӱų',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԋƥҞȄяʄɞWϫƀэˍйǱ1ςяɝƣшʙқѷȕϗӦȷӊ\x9eʫ',
                                                    },
                                    },
                            {
                                        'name': '\\ҥ¥Й\x95ÓˢȢϗȌԏӘòʶƝ҅ԐTŲmǾǿ\x83Ц',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȋϻĥοӷŢɒ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210129:192619.029892:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƉϙӮҽŒ¯ȩÃ˅¿ѣԉĆӀ΄Ї\xa0ϜŬΚ©Ђ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            9169579522454087786,
                                                                            -2696029505958322597,
                                                                            -2406249889160189659,
                                                                            6510680707394783482,
                                                                            7787306251613191916,
                                                                            2562520217862038065,
                                                                            -2210916230325847745,
                                                                            -8007017108679233103,
                                                                            -3747828541741538040,
                                                                            -7643856546383699750,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'şϧřЊðƕ˂',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 103261.12334981925,
                                                    },
                                    },
                            {
                                        'name': 'ıӀ˵ԄƩτŞŋ´^ʈѝұƥɚ\x83ЈŬ·=ηѮӃЁУщ҇ʍӓȐ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 407649.7218808366,
                                                    },
                                    },
                            {
                                        'name': 'ʁăɓҤҞɚщǑǜĬμ¹ã3\x8bɐԊņYҢԎ&Іģҏ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5068798154966840788,
                                                    },
                                    },
                            {
                                        'name': 'Đ\u03a2ˍĶ\x81ԪƖǥƳŅԠκҺВɁʴԤĽΉĳǷ;WËkÚҨǐη',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˖ԆÕӉϔħԅӺȇʶƑҌԎɏŃɋŌǼьν\x83ЃǊɲƗ\x94Ӻ²ԢϪ',
                                                                            'ɲλ\xa0Țȣ\u0381ʧΘԛԤňα5\u03a2ӹϸӁȴѣyŶуӐªϣņȗҌ҈ȋ',
                                                                            '҆˪Ϥƃғ¸˙ұй\x98ǧï¨ĲεϻɆΙЫÝŶˎђԚɁԥғʠӯū',
                                                                            'eɠ´ɾӵôЪӗσӰ®ȄŵԆԔɟӉÉɵʘΗӮʴ5ϚʊԬůƤg',
                                                                            'ɚǯӯԗĕ\x8dМƾСƧŋ\x8bϳëϣŶĺСϬəʣЁǳЋΐʯψΘŚʚ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'œƏѿϑϗӖ\x95ʵԧΙлԣǊæƍǕǢǢ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210129:192619.031056:+0000',
                                                                            '20210129:192619.031130:+0000',
                                                                            '20210129:192619.031153:+0000',
                                                                            '20210129:192619.031166:+0000',
                                                                            '20210129:192619.031171:+0000',
                                                                            '20210129:192619.031176:+0000',
                                                                            '20210129:192619.031181:+0000',
                                                                            '20210129:192619.031185:+0000',
                                                                            '20210129:192619.031189:+0000',
                                                                            '20210129:192619.031194:+0000',
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

            'name': 'ñǄŸ',

            'error': {
                'identifier': 'ǰԜƮ@ұ',
                'categories': [
                    'configuration',
                ],
                'error_message': {
                    'catalog': 'ǔƳ',
                    'message': 'Ϙ',
                },
            },

        },
    ),
]


class LoadExtensionSuccessEventTest(unittest.TestCase):
    """
    Tests for LoadExtensionSuccessEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOAD_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionSuccessEvent.parse_data(test_data)
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
        for test_name, test_data in LOAD_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.LoadExtensionSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOAD_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LoadExtensionSuccessEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='LoadExtensionSuccessEvent'),
            ),

        ),
    ),

]


LOAD_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ҟȮĠˎǣѩмɇ˥ĞϰΦƐʟ³ҙЅÉ',
            'version': [
                -4886595824783093440,
                -5817562258056083266,
                -8829701947888365774,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ғw¢',

            'version': [
                -1593578577399211764,
                -349030879547980124,
                -1976492839615949421,
            ],

        },
    ),
]


class EventListenerTest(unittest.TestCase):
    """
    Tests for EventListener
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EVENT_LISTENER_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.EventListener.parse_data(test_data)
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
        for test_name, test_data in EVENT_LISTENER_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.EventListener.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EVENT_LISTENER_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

]


EVENT_LISTENER_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'event_id': 'õɄΊíϝĄʌĉÜΉ˹ÓПѓҞ.āh¼ʜԒƱʘǂѢӎӱ¢џʇ',
            'target_id': 'ȉȡԡ\u0378ŵΛǟьǙРɉŊӪȋʞɄуğέ˽»ȕ˄ͲưЅԖ\x8eԃφ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

        },
    ),
]


class RegisterExtensionListenersEventTest(unittest.TestCase):
    """
    Tests for RegisterExtensionListenersEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REGISTER_EXTENSION_LISTENERS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.RegisterExtensionListenersEvent.parse_data(test_data)
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
        for test_name, test_data in REGISTER_EXTENSION_LISTENERS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.RegisterExtensionListenersEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REGISTER_EXTENSION_LISTENERS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='events', name='RegisterExtensionListenersEvent'),
            ),

        ),
    ),

]


REGISTER_EXTENSION_LISTENERS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'events': [
                {
                    'event_id': 'ѩħĵćКɠʳǱσѫʅʍņrɀԄʁÚ8ē˅5ʴȶ\\ƼηĸŸĀ',
                    'target_id': 'ӵŐĂ˱ęɚĉɻ҈ȉɺΥϠ˄Ȣ\u0381Ć˃ˁʆƉ3˽Ơҳ˞ϫΚѼÖ',
                },
                {
                    'event_id': 'аĢşĴƔѸf\x84д\x83į^ʋtХƳÉϣƟǓ\x87ȗɟȎIлãÍpˉ',
                    'target_id': '¦ѷõIʼ|ȑç\x92ӻӛĿíόƺɋαԈȋ˜ʜǏϑÕʏʍʫÞǑö',
                },
                {
                    'event_id': 'ѮЮˍǄɟɘ˜łУǑƪʂˉėțǉǁŝ~ĂĕǩԪԀɰԢЏǇщΪ',
                    'target_id': '\x88ƒ˷åÒɉǯȽLƬӫњuУѝκсùћ϶Ɠхʙ\x87¿$ҐуώЃ',
                },
                {
                    'event_id': '·CθӅЅȈƲӼ',
                    'target_id': 'ӓúÄɽ҃l\u0381ƶůǸ±щѣӤ.һ;ˎϢĔwƮ϶\x98љƆƖȭπ\x90',
                },
                {
                    'event_id': 'ǲƚƪɧȔ,дƔ[ѤϫӇȰ\x99ŚİлʖțѻщӺƸѭɵȫϯʆŨȋ',
                    'target_id': 'ÊʑǡöÂͺɭΏ͵šɥȱƀњzþʄ^ɈʷѺĜҪŷӹωӗʅȆë',
                },
                {
                    'event_id': 'ͳ"ūɧǄҠʛ`¢\x98ǋϞʡqΡʡ\x8fλϻĚʴũ±σѾӘЏχ2˝',
                    'target_id': 'ˉ0вŗΗȷҞήHΣίxǁěɩńŘ',
                },
                {
                    'event_id': 'ʣ˯ҤԞé\u038b½ӴàɐɦˊʔƵɮŲ\x81ѼȒѧƱƜϋ˭ȴƆƜьҘҀ',
                    'target_id': 'ӤϖѻʛIĂѿ\x89˃Єȏαġν҆˸ȴΙƾҸРɳǍʋΔ¬м^¿ĭ',
                },
                {
                    'event_id': 'ɭƚȠĤӻľɐʟƍKɓʌÞΖζõ¶ԏ˳ċǛҭШЏ\x93ɃԄ¸Ӳӎ',
                    'target_id': 'ÅʣϐԄ3мѩëȷǗ\u038bıӂȐƯȴԓŴϮςΐ©īвĻрÙƾjω',
                },
                {
                    'event_id': 'ԅƟɩǙӥѥԒɨīϛȅɜ;˧ҴʬнiŬγϱƽҷőàЃѮπȨѢ',
                    'target_id': '\x96ƄԑӢvυθԘΣϝϦζҡʀϞғāʀɄɔØÇЙʪŬȴeЙɡЩ',
                },
                {
                    'event_id': '\x8dƣɛ·ŻǱƤȾǃӅĚˋϰƦǁҎƏԞŁYƑő˙5é9Rɜyҳ',
                    'target_id': 'ξˠԫϓϟķÁǴeҧӓǺJӂ\u0382\x8bˣӑrȾӟҪ<ЬӾSȫЀ΅Ĺ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'events': [
                {
                },
            ],

        },
    ),
]


class RemoveExtensionListenersEventTest(unittest.TestCase):
    """
    Tests for RemoveExtensionListenersEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in REMOVE_EXTENSION_LISTENERS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.RemoveExtensionListenersEvent.parse_data(test_data)
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
        for test_name, test_data in REMOVE_EXTENSION_LISTENERS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.RemoveExtensionListenersEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


REMOVE_EXTENSION_LISTENERS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='events', name='RemoveExtensionListenersEvent'),
            ),

        ),
    ),

]


REMOVE_EXTENSION_LISTENERS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'events': [
                {
                    'event_id': 'öԁ=ƚɻļҽȝƃŷəĝĂǺΞ͵ōÌ\x98δτӏI˛ȏÁňȐζư',
                    'target_id': 'ĕǈéԢӛʡůȎƩԆԧʐƮ«ӻž˔ŦƇįɅaĈӍѭўƼƺӠ¿',
                },
                {
                    'event_id': 'Ԇ!ýϗȂƍѫȈ˛ǲŷѦԄǪǠƿʹμϭσŎºӼǭĞˢˠкƔư',
                    'target_id': "ȆʰԝγȎԨ'ȮˉŋäȷǱМϰEəИýϔɃсŵiµƫƒ\x95±ƌ",
                },
                {
                    'event_id': 'ѾƔжϮōѦüΰĮϳϗɰ®ÍԎϫ˧ƶ6ӫ!ʁϥƃЬ\x9d\u0379PĄӁ',
                    'target_id': 'ȦɛʵĤɿŹCȖɑ1ӛϛ˖ʳ҈ėȼż5ѹ҃ǙĘ\x81ӶҔǙÖȁЁ',
                },
                {
                    'event_id': 'ʂǖͻсӠӍĒї\x89фҔjκȠΫɰдБőιåqγһʪÙюéʕӰ',
                    'target_id': 'ԃ\x87ϕˬˤ_ǛϮ˗ӰӆʏȵZύӘʴҁíÐğŜӢĥϘԏșħūˍ',
                },
                {
                    'event_id': 'ƨɍΠƽďƥLƛǠ%ǴҀґҁʫŇюɒńЛĜȋǼČõҲӣ¿ҺǱ',
                    'target_id': '˺!ѐʊØˊ\x95ўŌ϶ŊʔĖѸɀʶсΥѡәƋȀĄД˂ĲԢ2ƙǣ',
                },
                {
                    'event_id': 'ǗΥǒƁ=ӰĥΥԇʥҕ+ÂʶѲĭϖƟƖЇҵӒҰϗ\x86ѻȸŸӝ\u03a2',
                    'target_id': 'ɗ҅ω?ȡ˲ΊƓǰØʊȥɈˇÆЖ΄афˑʑʲҠӠΓʠҹȱɀr',
                },
                {
                    'event_id': 'ǷϻR»ǿҷɋԛϸȹŒQgxԄʔϳв0϶ƁԑǡЯ\x89oǞȏˤ\xa0',
                    'target_id': 'Ϧ5ŒҗƢϴŭăǜȥπȾ\x90Ӟ˞ƊͲɞӴɈ=ŶdſЏĒ˝ǀЍе',
                },
                {
                    'event_id': 'ʪγņҺɱх6œ\u0378ʍӚƹƷπżΏς˃Ђ˜ƙȹËŖŗɗ\x8e·ƪɼ',
                    'target_id': 'ǎ˯жȜŚšҌĆ¹ɺϣċ=GǾûјǊJɀțˮƱɨǙίw¯ΛӉ',
                },
                {
                    'event_id': 'ɉ+ˇñɓ˗\x85У˞ɂĜʌƝȩ\x94nɬҟÜБНĝȭғÿмɽҋЊȮ',
                    'target_id': 'Ϣ˵Ŝ-αʩ;єσȔÏ\u038bʳ#хīǮԭªҙИĲϽӒʤʮЏҡĸŬ',
                },
                {
                    'event_id': 'ĝaЅϋԮź^ȰÚVХʽѽͶɷåËԮОǳілνъϝǅϿķǧȸ',
                    'target_id': '΄ҧӦǞǗ.˽АΦRÉÅĵЄ˟Ҟĕŝ·Ă5˟ÐӽȄӻϷÏġɣ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'events': [
                {
                },
            ],

        },
    ),
]


class SystemStartedEventTest(unittest.TestCase):
    """
    Tests for SystemStartedEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in SYSTEM_STARTED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.SystemStartedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SYSTEM_STARTED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]


class ExtensionInfoTest(unittest.TestCase):
    """
    Tests for ExtensionInfo
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EXTENSION_INFO_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.ExtensionInfo.parse_data(test_data)
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
        for test_name, test_data in EXTENSION_INFO_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.ExtensionInfo.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EXTENSION_INFO_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='ExtensionInfo'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='ExtensionInfo'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='about', name='ExtensionInfo'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='description', name='ExtensionInfo'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='authors', name='ExtensionInfo'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='licenses', name='ExtensionInfo'),
            ),

        ),
    ),

]


EXTENSION_INFO_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ӒϗɊǣôŪġ-ϪʀǱȚ\u0382ºѝÁ˹Ӫĕϐ\x8dˠԄʵҪҊӽǀŉӾ',
            'version': [
                -2454603770234662301,
                -2825431615839815014,
                -5179597261316947985,
            ],
            'about': 'ʻɢÁÀԄЖҰΝϸȼŶƿ\x97Ėsδȏɬ&ɛˤα˙ήƝşϩxӕɄ',
            'description': 'źˀμũɕěǚΡϊǧ˷@ĘҏȫǑԤʸƲңͽǌ/ƤʣНǭȏЪԀ',
            'authors': [
                'Üī˲ĢĈ˽ęɌԝDīwԇҕцÇƴÇчȶŚKғѯʡ҇ӼŒȴɱ',
                'õ$π|ȇěɒñӏʲ˧ĀʀϬ˵ìʚɏʕǉ\x7fæң˖ȥЏɜǻˏ˙',
                'ьǹҒϢïãъ<ř}ɐĄӺĤӫɒ\x9aѾĶŽҨӠѡääƂ}ĭĈ˪',
                'ԙѝ˔щǫVʫrРҷ˃ϋԅȴƊəɁĶʹї˧ǂφƌύĆϤēŁˊ',
                'ӭԐ\x90£ǔ\x81ƮƻĚjӢԂȠФΧϲΌȃͶϠͳɄļľÍƄɍʋ\u038bЀ',
                '±Cƒс\x82ЯЪɧɵrƔĞL\x87ҼҊjРϝõʫόƄ\x86ȣř˙ұˬĹ',
                'ɼÔȋӊϘХǅ]ɘŨĕͰӫȡĝԁʺ\x8fʡϋкЏEãǄмĥøȓϨ',
                'ɳΪӁǜ?ԛӼ˷ƓYҨϺиˠɪʰˈήlѸkǹшӯ˩Ԏƙ˦ѳϲ',
                'NËõôŸM˯˂Bȅ˯ʃůԢƗ½˓Ϸ©;ÃºϊŅǅ$юĉҠʑ',
                '~ǫʛ\x82˳6ĲʖЇȬĊMŊƉèЗŅĉԈäɲӋδêͿȠƇԘ·ϲ',
            ],
            'licenses': [
                'ҬьЕЯ˃ƌɫ\x89ǚʎβɵҙoөτȁøȯkыȩŪϤôšѯħɡÝ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ɺњԪ',

            'version': [
                -3190558073856904996,
                -2698988396504404391,
                -7134280818475363124,
            ],

            'about': '',

            'description': '',

            'authors': [
            ],

            'licenses': [
            ],

        },
    ),
]


class ActiveExtensionsStateTest(unittest.TestCase):
    """
    Tests for ActiveExtensionsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ACTIVE_EXTENSIONS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.ActiveExtensionsState.parse_data(test_data)
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
        for test_name, test_data in ACTIVE_EXTENSIONS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.ActiveExtensionsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ACTIVE_EXTENSIONS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='extensions', name='ActiveExtensionsState'),
            ),

        ),
    ),

]


ACTIVE_EXTENSIONS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'extensions': [
                {
                    'name': 'ϦɺԆʦȡҭЦϢĹЙĕĨӾRˋЛɁƄjǈΛ¤ԕ˭éϻѲώǷQ',
                    'version': [
                            -2276472150312147725,
                            -6164333051851250371,
                            -6659925833484007900,
                        ],
                    'about': 'ǐӄȁŬ¶¨ɢӦʄё\x80°ΫҳЗŴšdД\x88ƄƲʳȫΧȰѦÃĸУ',
                    'description': 'ȒιÂƛ˫ӪŷʪȆƂϿ¥GƚӮȗћǓľӆƀԩқҩÓũϓФЕȔ',
                    'authors': [
                            'ҞӛΜκЧɖϮĥëɂńҟԧɟȕŏȷɺ¶ɪǸƉŕˎ»ŗĴˎϏπ',
                            'ͺϊƵǈΣńЮŧЬԐӑϻƛ.˜JĽЕйҡ`Вԅȇǹǽԇҝ%ь',
                            'ʔΛ΄ЦĄ˭ôĺͰҭʓӧrҕӔʹǀŌʵďǛ˧ůŶϲf\x9b¦ӛʿ',
                            'ƹ',
                            'Æģҡɦҷ\x87Ԁу£Ŗĺê\u038bѤȻѬǮÏӮǋÆĹ͵\x7fĸҜǳmȻϵ',
                            'ΩЮȻәΆǂƖӉ˷ȚʂŜÿįɴКɭ\x87GϏɌҧϾƵyԔʫрȼĩ',
                            'ıȼBҤɐѡǇH˕ГӋϼĈчǉɂȨЁжʇȌӵªđD\x9aʶԍȳБ',
                            'ŻŸˑȖ˖ϺÊϔЃŃrѽƺͿƕǁ!ȌǫɝǪĜЛǃźїçϷļϻ',
                            '\x93ЀϽ\x88ҷόʤ÷Ńõõ˂ԅӆƶǇӝʪV?¶ǿɜϖȟȯΤƛȅг',
                            '˱ЋΎ˖ѫ\x8cӠżɔƨԒӗчżÿ˦ƓĔ˦ԋmUęȚӻ˾đөŚÇ',
                        ],
                    'licenses': [
                            'Ǟ˜ǛӏԪ˓ȗÞԟʺʾҚѲѰēɈӁΟТøȦΣҎȽӳԑηФEϡ',
                            'Ӣ\x88ӂġϾȬą˝',
                            'ӌЉɡȌìлÝΘPѺҕmȡǢԌΩӍKɆ˜dƖӛ˟ÕϪƓŞ˞Ê',
                            'ѭϡ\x99ʘҘɍɣļФʂδʿ«ԙāˁТƱԮȳȴɫƣ˾ѾǵԆâơȥ',
                            'þŧԁԗƁŚϏ&юɲĢȭљŜΙФšϓĀɾǤӉʎΔˠ~ß\x98SÏ',
                            '˾>ӭɨŞϥӺńƾʔуҘЛJvʪSԍȯéʻǗʯɤˆƨ˦Ӊűϰ',
                        ],
                },
                {
                    'name': 'ԍ3ϴƾ˓ȇЉ\x99¤ŰˍǊϳɓ\x8cƵΉʹɦȩŢȢÐϿÌ&ԖÀӁѣ',
                    'version': [
                            -2438139449146495909,
                            -1300271813996194500,
                            -6868588644472325072,
                        ],
                    'about': 'ƼǈǊѣǻƤԍʑǶȜXqǗÁrɆËĹľԏЙ҆',
                    'description': 'ХƵgŚйΡǲћʋ\x81ҲǪŮȔîЂ˰ˇҫ҄ǣŤ/ˮʲpĚƟ\x95-',
                    'authors': [
                            '@ԧȀ˕ϕ\x8cȓɇ\x9fMäωԫʹʮȶáȀǑɘƝш`ˍӺǨŖi΄ǩ',
                            'ӐɠΠϧфŖʩȓʥҶÆɚȑɘ˚ĂӺŗ˶ѢԀüȽĺǠŹҿ$ҪӶ',
                            'ɋ½UÓεͼеƿňЛsЙпΤӜ^ңʤǐƃǿʓԨηΝČ)ɽεÌ',
                            'H˵ƪΛȳƵǈƾȢvӏцѝГʼϑ\x8dӦɓԬʄԨƲƑ\x85Ê\x88ԩ7ȷ',
                            'åȃʇčҗюΖͻƇƓ[ϊ˜ʾѤƀĚʨˮȊέhҔҊӗƋҦȎ¡˧',
                            'ɣϳҔŁι2Þλ΄ѸȇƱê\x95ҫĳöͰАǋɢŎϓ\x8e˧ԁπŃҹӖ',
                            'kǻǲѕƯǜЕј˃<˽ň҈ѽ',
                            'ƄӆԉЈԀʾǆϞǸβХËȲ\x93,ԫŋә¤ÑԩЊϥɺęҌҳ+¯ѥ',
                            ')΄ͻȋъʮвΚȚŋɩżС7ǖȶԩͷ˾ТÔĥĩӒΝʅ\x94Ç˷Ϟ',
                            'ȂǍԃѢ¹ԙ\u038bзəӼȰЩԄƳԞ',
                        ],
                    'licenses': [
                            'ϊк',
                            'ƼԟȍǇ\x93ΛƂеƵͿЗǨÀ§υȺâÚʺϯɻɠҫΖˠΤ sˢɩ',
                            'Ķ϶ǓʥӈȜƥάѫƝǽ\x9eѨȴĦӑ˹%ӋƉ[ίӏķƗԗ\x8e¾îӺ',
                            'řåԐƓҴæ˶ƏӸӸŶƍ=ŸˠӦŠȩ\x8dǛʐƄ¡ҋʂɡØËєǱ',
                            'ɇʓʰϤȹƘλ˃юȝȥȦϫƝԊьȯĈЁK˽ёɽқȳӺӺϣ%Ѻ',
                            "Ԡιɲ?ĢʘԂѩӺš˪Ĥ˥żΫӫ¨Ùʗхӄԝ'Ԫ\u0383ԐǢφɝʩ",
                            'ΌmʉԭѨϥȀǷʪɭʵČ˷GзYñȤʁѼ@φőԧɸДǑËІϮ',
                        ],
                },
                {
                    'name': "ϢȼƝуʉ:ϱЭȡɜɄÕѴˑÈθ\x89ɇʜµϱϚƞuΏ'ʦǧӰɄ",
                    'version': [
                            -4706533279429262593,
                            -3464005399863748318,
                            -4374738803146631226,
                        ],
                    'about': "ɛE҂9ʟʱҗѤȍ'·ӒOɚѷëԘûήԌŉɱҏѐΠӆĮԇɔК",
                    'description': 'ɾˀΟɹ˒˶Ƽʫİ˴јϺӛѤAȪ¤ɷϗǍş¯ſЦҳϭƒɅӌˑ',
                    'authors': [
                            'ȓѽӒȤQʮβʻȼѹʰ±ʼĞ£ɐI΅λgÅƇƌӷΌ\x85љJEŚ',
                            'ǠĪˈLˮĆʄѲʤһȄƇҘǧiΞɬ=ˈҁӶ²ҐεȈϮԇŻĨѽ',
                            'k\u03a2ȸƂӝϛIÂȖӎϻȧģȿȃʒӰӸϰ°źlʜӑ3ҲõҝɝΏ',
                            'ʒǆŌʼËө˷ȜŮʏȍőЮ®Ҕɼ;ɏѦǑΩǋǩƋԢǥѺм  ',
                            'ɒ҆ȍǄĵξŕɷɸɌԛˑŧ\u0378ɈʴˀĔӋȊµĜƭȷԝӁpųþã',
                            'ȅΑόƩŴӏȎӉˋ°ʾ\x99ϜƋ˩ԓǳŘʸїӈ˙ǜҔɪ*Ť\x8fђƣ',
                            'ŊŽШ˶ǔҐͺąѦǝˋƘƠ˞ƖԙѥФŬлɤɟģЂƶԑΡѤΓɶ',
                            'ΜƎʬũŒŏҔȿʗΕȲȶǒӪȣá©пΚʆӻωʠөѺV\x80Zˆʼ',
                            'ƶҾůȲƨwӌĉĞb',
                            'ŉĴҮʡ3ϪҽłɨԟǵHЗɻöӬ˷ȕʄõԋӁɃȉӗƃūӔбʹ',
                        ],
                    'licenses': [
                            '˓\x84ҽϔÍ¼ŭɵǄϥјϚʻ÷ʸĔΈAр˔ӣӈԍ@Ƙ\x8aТЃϜ3',
                            'ƴƔцѸсɤˌɗңʉʰΝүԞΣĝˍыѸѐϯýſԜϵӪʄͶǏҥ',
                        ],
                },
                {
                    'name': 'ǎ¨ƥуҍʰҖcĨ\x96sÛІÉʨǐàȧƘҙʦʃÐԮūԎɋ·ìƢ',
                    'version': [
                            -7177113537604297561,
                            -8798173055650653926,
                            -7241889966741602830,
                        ],
                    'about': '˻ĉ]pýʢɌµүӴűĝĨðΉɗɀˁЫϠϺÁ×ɏńƊ;Ԡÿԅ',
                    'description': '}ɺŢɪŢϑɼƢȡŧҜʊԚХѴƹʲԆͷiԫҧͰ\x7fӰçɿлļӶ',
                    'authors': [
                            'ΉŵɘƒǺРʷǦƋ{εδϲtġĵҠɉĝȀïόѱlІŲƂȚɄҖ',
                            '˒ĀΠOǱӤӦА҉4Α}ǙUĺЋʴӄ҈ŃǏɿǊx\x92ΆͳșѾÉ',
                            '{ӃiĆʫʓēӛ',
                            "Ɏɧð\x91ѸǑӌ҇ȵϺΆѩÍʯʸԇĤԍʯχ\x9f\x8aӓΎÊ'ԮΏ϶ȹ",
                            'ƗȑĚӭȨÓ Ȟ¦Š5;ËҒԅĥЙí2ƟȰ;&oϚĳGƉøʡ',
                            '\x9e˰ƣӉřǖѴУwΫѩρӼKġĪæСсϋɹѪʙšɋˇʃԍшǠ',
                            'ѐ(ŕ\x93ӗƈОżƃόλǴ˂ӻˍȽ%\u03a2ȸ¸ӽİʢ0ɾƇ5¦\x88Ԁ',
                            'ˑԪĊҥ ˀԘōЂķԩ˥ǈǄķҠǦSȘйғäɎˀҽʬŀ^Ь˥',
                            'ƹǋĚŀӧôӨҮžƏͿŀӱİ0ҺǠ˵ŘѦԬВМɾԇɻΣ|ЮƼ',
                            'ɶȸAАʷѫϨư˩ˣ҇ʠϳȭʋǅƗśϼЋΎȮĻҷԎ\x85ѲĊɄǊ',
                        ],
                    'licenses': [
                            'ҙԣȨΗËџԡ¶ʾȲƨКĠțХȜjΥК˙ɛеԓϓљƩåΰňě',
                            'ҫįɬĊļö\u0378ԢɧιҒʅğӨəϬĄ˭²¼μȆЊʧĘɪ\xadòʵӤ',
                            '\x95-юϺƝǏˠm;ǃfӥδȖLMυўбǉ҉ʣĝҗԭĲϝƵeʂ',
                            'ԠʚҎȩ\x9cǡŏϧіɓ1Łѥ˔·ƠȩʘӉǀˋƝÔȊӃԬ®ѝƵ\x8e',
                            '҂ȠɈʌaҠʵΐґ˸ǅľȕъ-ιȁ§Ζ˶ƸˈмĒΣ¢БyѸѿ',
                            'öԢÑ˞ħƵ>ˆīʂęʽԈƜʣ\x98˝ĜưҎӉҶВʱӫ\u038bEԆ4ή',
                            'GЯ5ҶȻƂϹƛϰӤϸµԞȤʭѻԢҤŀƅƆʎɄk.¦äӿˑ&',
                            'Ҭ²²ʓ]ʗԟɩУ϶ÍĀő',
                        ],
                },
                {
                    'name': '˶\x92ğζҴә˅МɕҬПŊɃɉSӔhʉԐɌΞǻѷŊІӧɏȟǪɾ',
                    'version': [
                            -7031359270384456071,
                            -433169713972689046,
                            -4735494937209276593,
                        ],
                    'about': 'ώĜȗƕǗĥC&ϸęбȝïЋȳšȗɵûшvψƦĐ˱pΧҷїћ',
                    'description': 'ϚŧȠɅѣϗԊǛ\x8d\x9eƃƕhȪ\x90ǽȋȍӨȢќҧ-ÇŪĊԪ˯Ƽû',
                    'authors': [
                            'ĤλәĨĪˍӮ\x97ßȋʿƇѠ\x90Ѥ˼фʎǗϐɍ²ɴ',
                            'ѐψĂþƪʩϛʼżŁѺ\x88ĊҬǿńȴΣтȊΚѬæıѫJԍòʑę',
                            'ɯƚύϦ¯ѭº˚ÑίǸTϥήʕʋΐԅ@IˡώĤҾˠģǃʴúǹ',
                            'İѥɞƪʦӱãЁӹŧxǾΜ)1χԊ;Ѩ\x85ϴԛЛǗÜˍòƪҼȃ',
                            '_',
                            'Ⱥјм˷ԟų?ϠĞч\x7fԚʢпÎųԃϚӒͷǥȉŽïžӊAéťP',
                            'ɕjͷяǧnўӣ\x89nԣʞ\x8fҩ¾ŇƺѨūȑѩ7ӎ\u03a2Ͱ¢ˢǰļɎ',
                            'LҺ\x9fӇуʧϗƬîŵĳњҳƆ\x9bǪѕӾԌȾȫĥӖԫEǦȳ\x84Җʨ',
                            'ЦΔϮAmƫ¤΅CҎϡӸƲИҔǛɰƄåсανı˃{ÓϑˎԃϚ',
                            '/ί-=ϝӯҶlԀʃƌʛ¡rΥƆĮȍʷò!ɂҠÙhҩ˟ɢǳ\x8a',
                        ],
                    'licenses': [
                            '±α',
                            '\x80ƖηӧˊάƂ\x87ĐԮҫΨ9ѐϠƄ/\u0382ōӇʎƜɉͱǮɭΊѿ˪τ',
                            'ǸǼАϳðϥΪѶҶ.ɄǕUӔˑҕøӣƍВȳΊтźԃŲӕАşН',
                            'ΦȘҲ©\x89ԕɭĺԒ@ǴǪβӺϨÐˣӡÀҦҼ}Ĭɰ!ӿѳαŭò',
                            'ӂÝΧĂzʀÝŊԌûȪӤȷқċ˷ȭ~Ƒ\x88ÚʺεԗѩıƟ±īτ',
                            'ӡҦļʕӏӰԨѣˌӝ\x82ǋ9ѓȧĮĪrɟ£ӠԪ°ʾɸѭļɨ΅н',
                            'Ƈ˰Ό˺ЀƓΈǡҫ²ҟɥîϤ˜ӌīеȒЮє\x96ѣƓœɉÙʩʳӉ',
                            'ӎ˗ȷȉɊǨǙϣĲʚЌʓϢѴΘƍʐʤСѩӅ\\϶ŎоʖŉΪ˝ɶ',
                        ],
                },
                {
                    'name': 'ƪɿϱӌȮƉϸcǞǣҋÙĔαȐӸƘӲƭҬҋѸ˂ƱӫÃiƊʞҳ',
                    'version': [
                            -2877497793247415058,
                            -5335021614099669578,
                            -3061734447676592429,
                        ],
                    'about': 'nԜȤϹро\x99ȄƎΎө˚ĳҪțĄɆԌȐѤ҅\u0382ҢʻҠȡϹӣˊӡ',
                    'description': 'ΧɺǩƋӺoΫ˔ɃˍŻ˝˨ɔɀǛʐqюǒҽғŲȁӶǬ³>˵ϛ',
                    'authors': [
                            'ȁǮŴƪђʳǇÞ˟ҴǶЕӶǊȌԐǩƵϤσ\x93ΫǳԛѯȹǰǙϡӭ',
                            'ƀ¸ʞʒԖ˪ɭşVǐɨŶ×ьΏө4Ζːͽɪ2¨ņƤɭŊӥɽŧ',
                            'ǡɎϵԛ^҄ÀNżƹőԘ\u0382ӋȼͲ˷ɥʅяΏ1ҜņǀɊӋɗҦͲ',
                            'ȘŪːдɹʏIўεԝūΩŚќɗĻȅӒ¤ȝȡͽǸ˹җNʯҲʿҜ',
                            'ƏԅӿĄϛʩӃҤéΧҏżʞͻБϝüˆǓӥ)ɪϽ:ΗӬȹȆȢū',
                            'ҦąĬəΐǋҪʴвΦůȚΟňʔЬŲӑѡϓ˄/ƮΟǺԂЂðλҲ',
                            'ʋ˗Ù¾ҽӴΆĐͱβΠӕʼλˤ˰ԁŐÄȨ2ƆȾ"ƦƦҭǳĸξ',
                            'ϙŃ*ҋQʺϑƲϴȡ9ОȐ\x8aΏłȵИ¨¡ҨŉțɨʦӐĵԈӨɄ',
                            'МƉ(ƭ¹ŽĥύtȹƫŐѮʳϐУƿöЪʢʹοʹ»ˉϱϮɻԚȭ',
                            'ŘԦǶīΡƆӗώѕȊ˝ˢƳʇϽόЄȠąϥǖʟ+Iˑ\x7fҗԪҜ˼',
                        ],
                    'licenses': [
                            'ʩЇӔΌӧԉΎGƫӓƞμәʭȷx§ÍԠȯǨ˔аԅǞӺð˴ѵƆ',
                            'ԛþӅЕҵųΙУӨҩѐȆňНǀҿƌ|ҙļȄɒƖȿɁ΅ʈɮԇм',
                            'ĤG\x88ҚɄqӍfůÄ\x86ŪӿȳǀäɫҫÊғŰőԗųȝʭԕР˰Ċ',
                            'οѨ˜ư\x95ŝӴɖ˨ɃԖ҉ÊʋƭĹӿҶ¿ѓȠɏġŊŮÇԨѻӎǜ',
                            'lԠӻŶϾȥѭs·ˎāɶ¦ΗÄϺɬϥɁҌʊĥұƙԗэЅŅҟˎ',
                            '½þƔАɋʞöҒϮˍ\x91¸\x84ʗIϘ˅Ρԋ˻ҫӔŨȌǺȳƻkɀӂ',
                            'ňѵťɻӿϞĸěɧŶӮǲɦƃ˩ÏVkӊŞϹȻ\x95\x9d0ȦĨһ҇³',
                            'ĩԫ҇åĞпɭǠťΠӃ9ȥɃΑʊɱɔǹǆƳϥ;ӐҀϴƌѾ;\xad',
                            'ɲƖŐ¾ӝŋѫˑ\x85ăƯÃҠљȈđîԏŵѬ˘w\u0378Џ˰Ǐ\u0382ʙɤȞ',
                            'ȤǲŊĽȤΐџʆΕĽŦƺʏƛОŽŤƶ-Ĳä\x9bЖέưʨȞԄůҏ',
                        ],
                },
                {
                    'name': 'ŌхЩʄ\u038dҘаҤ4ƿǲϟѮȺ±Ԣǎ҆ήKҦĽɺǤΦʹЊӯѾô',
                    'version': [
                            -6600890273833679129,
                            -3366687169722898286,
                            -4639821111433984119,
                        ],
                    'about': '#Ƈ˒ſÞөλʦӀoώƘżΣϡœҪģϲsҹтѰϜĭȲǆÖEɀ',
                    'description': "ԜӆνºʴѬ\x88¦ӓϗ'˒ȖŞĵΰȀɝ\x8dĘÌѠΎĥɘƭɦ˗Еθ",
                    'authors': [
                            'ͽӀśѻɉǑĢīöӛУ¦уѱ˂ɃÁǃǬɊŸɷǹĖԞƧŎӶġҎ',
                            'ǀΫюȡƋϸƟ`˒šƸϟԠ\x84єўyǻАʃӼÕL\x80ƳԥԊǄӲҡ',
                            'ϒџҖϒʌžƮ\x8c9˭˞ȢˤȤɎÚŝİɪɗʜ\x9fźԇ˝?ʡȨύӮ',
                            'ÏʆΌ\x9dѲεʹɰƵKƂɷȀƊ˨ԓ϶ϐşʱıʤќϯ.ƧTɯХʖ',
                            'ȋԡǶbҝęǢ\x9ebϞхǃéԃÛȂҌĠ\x8bҎϊź1ЂҀåȖDɺш',
                            'cǮňÀʎ\x88˦ɂʊέǤƼȔԃƅǔѾǚ)ǁȌǲɀҷд˼ȁȊʩɿ',
                            'ȌǇ}ϐȄ҃ƞ6ŭȳĪƻĂŉӡϓʢÚ¾ӣΟ-ҤȖĀȋƁЭӅϏ',
                            'ʇґЅƼӲјɊϾӯȹmɲӍKřĨ/ԠμίɇЎϞЕОхʻlĄ\x8b',
                            '\\øԀǼЀԅÌǏƊřàΰYʞΖǔʭϻǢƉƿâҴҞ\u0383ӓɁŞʕҤ',
                            'πΎĈΒɦԧ\x8d\xadƕĶ=ɿӦҾǗӊф?écħŨŎҸξƹʙʣфѢ',
                        ],
                    'licenses': [
                            'νѕφ\u03a2¶ȽҮǂºZʍӀӓϝɞǶ¡ǾгυϳӄОҵ)ћĲКҏф',
                            'ʭӬϘәԛÔӸɈ\x8bЍҊŷ÷ȾȢ͵ɵǴͼŤʢпIŸłԥεіǈҼ',
                        ],
                },
                {
                    'name': 'дɫdӒϾƅԢ\x91ɊʌԎӵǯďͳɣƸƒjƅSӅн˻ɢңKǩȜĢ',
                    'version': [
                            -3362029994257052871,
                            -3499200118770968521,
                            -2468624368158191796,
                        ],
                    'about': 'ɹӺ˘ǉӦ8Ι£Ĺȑıԫ˥ƠԦÛÈҷǾÉ϶Ǣ\x95ɅӜĎɡȫӔѝ',
                    'description': 'PǂӐӎȍǞӂ˶ΫÛѫþХқˑƤӊċтŻʞŁǄѕӞǟÙɺ\x94Ћ',
                    'authors': [
                            '¾ɮʵΘϏяàɔψҎĕ¿ϨɠɺƮţĪҍϝӪұ2˟ºȯбϾĒ\u0380',
                            '\xa0ŨǼ)ȻˇϞɹ,Ψ(ϋѿ¢˝éӂɊšțʳƏʕϛȮΆėǤоЋ',
                            'ÀҌµˁĥͺҤ҇Ã>ʭυÛω\x9fźǥ\x9aĺӉÇг\x85ţĆǒ',
                            'έʹƐ\u03a2ϙ˅σʤ˅ѓĴɉȭӶɹ×ѱɩӨɨβĩϷҶȌдԖŉΉƵ',
                            'ԃƻ\x88wƄ˗\x9dӒƘ\x7fϊͱĈĻʁЌԣ´ŒŽŧϒѻľȨ÷~ƽÍǃ',
                            'Ǥϼ˴ɊБлЏРѶ«ӏϲĄǻϢщƋǷїġʲpȯ˴βΗºӿǌ˔',
                            'ìԍԓȗYǺƥЕȤưīԀвϟ\x92]ȲԐͰѹό^ξÉY\x8aϦҘʰ',
                            'ɥʀɪ\\ΝϱМɾҪӊǈÏҩ',
                            'ş\u03a2ɠƛōÙωљ˥І£ãŧедԆˋҜ½ҚëDӤɥыf\\Ҧɮƨ',
                            '·ƯҡӆÍăǛГǧĈӐɫԋț˜ŃəķҕƬԨԕ/ѡ҅҄јȳïΟ',
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': 'ĜʝīɵҘԜƕєÔҫqНМ»ǅȁûЏγͳ\x90ӹĖʻƸȁԑã@ԫ',
                    'version': [
                            -8570028297122669278,
                            -6748823343268496149,
                            -1889784222596477065,
                        ],
                    'about': 'ǙлĂ}ǝƕҮ҈ԨƟŚҌџϬņɤЁӚŗϧϡ\x9dΌw¦ԁУҰɽӟ',
                    'description': 'ϔˬƈLͼΊƳэʃˑˈɵƃʝїĈΧӝȥμ˹žқԨŌ˞Śţɯ\x9f',
                    'authors': [
                            '~œÕğϬǱӅ?ƎԔÙȹ˅Û¯cϻĥǍŹʤʰöɆvϪͽЌӿž',
                            'ЅȢ\x82ǋпФƣԁüĢ\x8eЧ\x8e˝ʑǶ£\xadϛʚǜǹҭw˩ʋ\x92ԠȔ\xa0',
                            'ˏĝӛ˷ЌқƎǯ˫ɍ҆ҫýѥϙύǬм¤҇ʈД˜fIУnNȡĄ',
                            'ȽѻʊǍǚӣρʅΉÖӆӑǸɡǵƾЦǸЙźΌŀԬӷȯ®ʂʪ§ċ',
                            'ǝǜоǍϠѺ˷ƏɧěÒǖѦϧԝɶĤɢΛ\x9a«Ҫ˭\u038böĺӧʲԟȈ',
                            'Ʃҝȟ\x96ͱԤҷČäʕ/ќԩâФϴīћкČӻǗɱѷɼúòбƕƬ',
                            'őЏΧиԘɑωɖAȘγÎƱĖаԀЉȭ½ɠ!Ѹɘ°ҽԘɝΉɏҎ',
                            'PǼ˟ӕÖʪƪѴϱƓȮ҉ǕL˶ϰŜλѩĚǏϻЍ´ԬԞ˛ĤʔÞ',
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': 'űț\u0383Ǻ;ǸņϬͱɑĮVѤȰƱϾȥ8ԑǶōʡЮɊˏÛ˼ɳɄϝ',
                    'version': [
                            -7117723118009835031,
                            -4178830104809123074,
                            -6334247105044367088,
                        ],
                    'about': 'Ϫ\u0380ɩĐʔ?Ь˛ΧͻкҪʳʚǄͿǍ\x80ϥҫUΕ҅ӂсǕǚĆ\u0383ǵ',
                    'description': 'Ԭɧӥԕü¤×\x9bʍʡ_ãӊǲѬɟԅɳŢԞúåƀëѬҏѷ\x8fԑԍ',
                    'authors': [
                            'ВρϒǌƟĻƟĽ¤ѓʎǁɦӰùҚϲDSòʉΒΒΡŐĥыKJɊ',
                            'ƈί5ʄXŉEŕĞΰȼÖɽӹ\x80˄ßØҜҰ3ĒͽɥЌŦɎȖӻˬ',
                            'ɡłЅǖӘʊǭ˧ʟɅĕγȔƸԄɚɏԣƲѼ,Г˹ƳDɭҧɅÀǊ',
                            'ȱӝʧˆɑǃ˻ʍѴҙǁѱˈѰʶȠ˭ԓĨʚƀќвȑ˝ηʌÌǋſ',
                            'ĤřϾb*ŹːȒϿτˎԙѳӉϧ˭\x8b\xa0ŢҒʕuƼӦŬѶ<Ή`ɰ',
                            'ҊԫԨòѯΟσğ\u0378@ˑÿŠūšīȔ\x80ĕƌȗӓŎѪʔʵƾƫǮ@',
                            '§ԑʔюЁÿƧҖѪ÷ӞʍƢŨѨʑгҙҵкӒςÈɠsΧȉά҉ƨ',
                            '˼ǚѺѡhҬǒÜѱŭ',
                            'ϱψҤӃԧɀЃÀɤͻЍ0ÅĵǻʗҰό$ĕ\x82ԦνĽÚŔѠҎǡԙ',
                            '\\ƣĝǃİÌѢǋАʅ˅¤ǰԅÉЄ¶ɊӍŒĀɂfƷÛʏəȎХ˝',
                        ],
                    'licenses': [
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'extensions': [
                {
                    'name': 'á҅Ӕ',
                    'version': [
                            -7527091621794318920,
                            -5546144861555544883,
                            -2724569415244087007,
                        ],
                    'about': '',
                    'description': '',
                    'authors': [
                        ],
                    'licenses': [
                        ],
                },
            ],

        },
    ),
]
