# GENERATED CODE - DO NOT MODIFY

"""
Tests for the l10n module.
Extension petronia.core.api.native.l10n, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

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
            'locale_code': 'Ћ˙ȴ',
            'catalog_name': 'АҔıʍ\x81ѹ\x93ƔƛхҷǰÐϰǞɠԣǴѳĖĤ\x9aƛФ˔ȫĪԮмχ',
            'message_file': 'Ĺū\\˅ѰӸƤϩǦˁſҍјŅžȧŨˀμŢĢȣ>ǄɨŀʮϐԍҮ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'Қ',

            'catalog_name': 'ĮѰ;',

            'message_file': 'Ӱ1',

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
            '$': '˟҈ćɈ=ŜϽƿŏԙϦЫπҗԉςɟ2ԇ˭ÛɅȱzǚʟƀʽͼј',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -5044050044208373180,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 239215.60561704403,
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
            '$': '20210327:032022.663395:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ˌȽǉŐʙқνʃɠΆʂŕλˌƸч\x88ѾŏҵƹÌΕ\x9d¬ʄӲϟӶѳ',
                'ȔƷȐʃƈѸÆʋϴўіЊѫÓЙ\x80hÅ\x9cˌkùȜЍ˒ƑΜƩӗƄ',
                '2ǌĻZι\u0383\u0378¿Ǘǹ΄ɭƿnʡүϱԈԌǸӞҪΠÍҮɁɀʮɂɋ',
                'Ӧ«ȄϴҽȫЁ҉ǋ×6Əԍ˼ˍ҄ƳѤʥԏζκ×/ɓдк˓ȮӃ',
                'Ηԡʒ\x87вɻ\x87ňǐĠ&ΕĩTtúrʞˬ1Ǔȹ΅ÍÀ˗òƓԦǇ',
                '\u0379˽ѩmžðУЖȂǵǕJȠ\x85Cʥƫöȷϔ:Ǎ©ƠӁƪҹȉԦʄ',
                'ýεӶl`ħԁô;Ϣȅh\x8d¹ŢˋǔˍȓԂцΞҡКĺŸ˔ŴУˍ',
                'ɲ«əќһȞÐӂæő%ЌΆѕύϵӳ¹ҨʦɞӳŬʬЊ˓\x86˜ңƬ',
                'ȈӰюˍʳÎŀˇƎԪӾƞš˂Йχ˕ǦƝ˞ɱÙΚȦǕŶǌЏяˡ',
                'Ő˒*ɤÃԋȃҥҭέԡĥѣǑɮ/ԟΓӠõЯȪđ.ӳ³ÔǚԪ}',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                4925702263954697462,
                -3360892935094441115,
                5203253702825340076,
                -2942950278331320533,
                -4804192431774700891,
                -2674442614278721006,
                -2385190314143757714,
                -863083158750470689,
                -2807729856691947797,
                -2718480572945555340,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                504401.4796832494,
                771393.7843877159,
                953230.5747066934,
                -28795.817396967832,
                509031.5021149218,
                8816.008260958872,
                564161.0500061564,
                366823.2021211304,
                666784.7802631822,
                134975.50674982314,
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
                False,
                False,
                False,
                True,
                True,
                False,
                False,
                False,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210327:032023.652575:+0000',
                '20210327:032023.670470:+0000',
                '20210327:032023.690852:+0000',
                '20210327:032023.710724:+0000',
                '20210327:032023.727930:+0000',
                '20210327:032023.744792:+0000',
                '20210327:032023.762325:+0000',
                '20210327:032023.779331:+0000',
                '20210327:032023.796982:+0000',
                '20210327:032023.814268:+0000',
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
            'name': 'ŕԡԒ',
            'value': {
                '^': 'string',
                '$': 'ҬȹʦОщ˃ϻÒУƇȜкĦӝŹ˴Ӄћ\x7fΤơһ¯ŪˌȀƗȒ˼ɗ',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '˪',

            'value': {
                '^': 'string_list',
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
            'catalog': 'ɇèɂĨЦţȂIéΐПMӥwћͺҎхҵϾǕh˕ƓíϩжÚÝƩ',
            'message': 'ӬԠȹΏӡіӥҩшƦ5ԫǼАчōЈ҈Ԩůá.ХѼΐČԂψѳʙ',
            'arguments': [
                {
                    'name': 'ƲɤǤǅЧǐĚԡɥԄΣ˛ъё',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210327:032021.184984:+0000',
                                        '20210327:032021.203538:+0000',
                                        '20210327:032021.221865:+0000',
                                        '20210327:032021.240135:+0000',
                                        '20210327:032021.259641:+0000',
                                        '20210327:032021.279032:+0000',
                                        '20210327:032021.298711:+0000',
                                        '20210327:032021.316288:+0000',
                                        '20210327:032021.334183:+0000',
                                        '20210327:032021.352623:+0000',
                                    ],
                        },
                },
                {
                    'name': 'хɑ',
                    'value': {
                            '^': 'int',
                            '$': -1654312003857557637,
                        },
                },
                {
                    'name': 'ċǟʎ<Тԕ\x9aįӝȑǇӆɇЫƍΪԑÓ#',
                    'value': {
                            '^': 'float',
                            '$': 652289.9381517137,
                        },
                },
                {
                    'name': 'ΞȼøԠŖөȠ[ϼԡŐbξuǎђǂŴ8ѵnɣɒʦʓ˘ʽԥԒ?',
                    'value': {
                            '^': 'datetime',
                            '$': '20210327:032021.585326:+0000',
                        },
                },
                {
                    'name': 'ʜǖʩʯκĉ˜ѬˌʯОɁħmęȥʊԓƏΩ\xa0ƔΘ²˭ȐTȤӉ\u0380',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'hʰԛ°ʹũĝϰŦȳӁoѤηʙͿ\u03a2ЈƇƽȄƀϐĲʟaѱÃʨӂ',
                                        'ӆ\x93ΐÈʺϢǢͼǝɑÙѼƳҰЎ˷ӍêŐƄȆ@ϧĕŉ˙ʢӛϷЮ',
                                        'ԑǚÍĸϧɱD$Ȉ\x8fŰʼǷїƱQĿК\x9e\x9aˤЖóˑвƩϐͿğɊ',
                                        '7ƉқƇдб˴ȁҫÐćΟŮәώϫ\x95¤\x9bAҖůƬϘӣˬӉɟƋϱ',
                                        'ǉ҇ɜģʭZƨԡɣЭŴГʽțӹԡӸȸȘӵыυŞ_ϟήκӠƉϋ',
                                        'ƓƎԚѓäɚªԍІʇcΏүʖͷԋŜ˩ĠʼÃŻϻӣşǜѯв˓ӌ',
                                        'ȱіčȮȦWÃȄԐĖ¢зÙȲȈ\x89\x8aπɂјθжĈɔƻȴҳǈǤǿ',
                                        'ȍţ\\ÊˌϕȚҙÒƧʤý÷ѯ\x81ͶϓȆƀģĕťѪ˄ˮϕĴƎЅź',
                                        'ӰԦɱƕŸеȖɝČɺŋ˲Ϲ\x9cʀ¼ҊɅɛĔùʚĒчSȘο7јΣ',
                                        'JҠ^˶ҙ½wѾϏˉĠϦʭϹѳŅ"ŌΓΓӞѲ˯ɨɦЛӖùɷƵ',
                                    ],
                        },
                },
                {
                    'name': '\x88ãVˬӓїхƃӵʵ҃{ϵĂʣąϸëџ˸ϮԎȞŰ˟×öɰĵҬ',
                    'value': {
                            '^': 'string',
                            '$': 'èǔϹԢýƇȡˇĝƩѢŋїƺÑƤň\x81¡ƇƋφҴӰóŔŎβÊӗ',
                        },
                },
                {
                    'name': 'ИśǐҝԠWΩѝδ|άΑϠҩɜÎԑԇŒԠ«Юѿе˫΅ɲζʴұ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210327:032021.987579:+0000',
                        },
                },
                {
                    'name': 'ʁđȿũӶɡӓ7ɺɹxǔʛ҅ƨɷɳɇ˞ϼyȮԫʆ˅',
                    'value': {
                            '^': 'datetime',
                            '$': '20210327:032022.044970:+0000',
                        },
                },
                {
                    'name': 'ɗ4Íɟ°Ɲ\u0378Ũ¾ǆӠɮƅԆǖ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        False,
                                        True,
                                        True,
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
                    'name': 'МϖLǔŔҽφϒɶƌǇӵ˜HƘɖǽαѫ\x86ñƄΖťȀŨλȋɉθ',
                    'value': {
                            '^': 'string',
                            '$': 'ϋһԆжʽǢÛΤϢσ҂ГȜίÆ\x86ʤαƐϬɸќĒːƂ\\ԧȥ·Ɯ',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ʌӕ',

            'message': 'ł',

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
            'identifier': 'ӼԮȌϷɩԬԮʭĕ|Ϩɴį҈u¿Ҏˮԫ˽ŗΊџеɃњȝϊʺ:',
            'categories': [
                'access-restriction',
                'internal',
                'invalid-user-action',
                'configuration',
                'file',
                'configuration',
                'access-restriction',
                'invalid-user-action',
                'invalid-user-action',
                'internal',
            ],
            'source': 'ЍόԗѝέľϷơҧƧŷӡɯηіҝЁѵʵEGĆӡiɊͲљҧќğ',
            'corrective_action': {
                'catalog': 'țȜĞɤȁyѱЛԂǗћkӇρȱ҃¡үаcşTÏӅҋѳͳӒӪß',
                'message': 'nѫєʏϚϥԫіцйǙʽϽѡʧůŻԈϿԑÅʹΦσjӉIѓˌ҉',
                'arguments': [
                    {
                            'name': 'ǛÐȣѻɷʀҟХӪчǣТǛΤÖӔҙʹѰϽƌɨȯӼĴ҈ѭҎȧӔ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210327:032019.116756:+0000',
                                                        '20210327:032019.129937:+0000',
                                                        '20210327:032019.143083:+0000',
                                                        '20210327:032019.158924:+0000',
                                                        '20210327:032019.173642:+0000',
                                                        '20210327:032019.186643:+0000',
                                                        '20210327:032019.202639:+0000',
                                                        '20210327:032019.220749:+0000',
                                                        '20210327:032019.238181:+0000',
                                                        '20210327:032019.255721:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ԘѴԘʆҳЍЏЌԏǆХ˨ΐʝѕϿÌ\x81ÚɐƬλ',
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
                                                        True,
                                                        False,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ɍŰĤʃʖŽ\x89ʨÿɀƲǖөұʱǆвɛԙ¢Ȩȟăƿ Ѱӏˏ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ҹҧȇ˫ǒbēˠϕΎʜŹәƥѶѠӵǚƲ3',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ŭԕӚȐ\x9bԔȍɜΑŲˆ˲ˠņƴѥҲúʛˉȕnɬĭСĸ.ʢͶу',
                                                        '·қşȈԝʵʰDȵЎńѵÛӄɅȔѦЂϡϵѓҥϟˮɋPѳ\x86Шѕ',
                                                        '˄ͺͽͳ\u0380ɢ\x8fҷβƿjǝž,ƴƓ΄ϕλ˗ҽȑζ\x87ђ˛ӭΥǲЯ',
                                                        'РѦ\x8fԒīVӾіӯ\x89ɭɳȲԠ҆а¥БЕҚʀɽӪӢęуўкѿϝ',
                                                        'ԁťӗΈºǠЀӵ˳ʞԎϘǬӃÊšUӪȍƊƸwǈɱиʤ˂ȡяʖ',
                                                        'Ͱѯѣűь\x96Щ¦ÖҜӠɼϨƙċŽԖļʾƪƮƙ@˼Ų˸ѮҡŤˡ',
                                                        'Äɷūɐ˨ĶąʨɷϲÿʅĴίμķѩхҘªľѭ|ҶБ)ƃԠ&\u0378',
                                                        'ÐЫӼĀɪѣǙɺʚȎӎʈ¯\u0379ɶ˱ĆДĘӒхļБ®ǳҪFǪŉ˖',
                                                        'Ǟӯҙъ\x9dƥϠłυʚƴ²ƻάӤϩÓԑӬȝˡĊ˻ģĚɛdʇɡā',
                                                        '§ćсĘӪΚΫЀˆƢƑ˫сŝáĕпə͵µßӳˁβҏӔoԈЫǣ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'яΩEȢϔ˟ӻÅҬõȣӴZí˭ɻԧԜɪԨÈƿß˄ĩǤ\x9fĲʞÈ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ŊȕƸόƸykΖ\x8cġϵԋɌŇςʿ¤ͶϨȓ/ːĖ˧ˋ´м%ӟе',
                                                        '®ϖJɋЮц\xadӝ҉³ȮϚʻÌτȌжǶĴĴϣх§ż(\u0378Ώɋ˄Ǘ',
                                                        '´ӷ«àÄ˯~ŵȬҖɏΩХCϲʇơ\\ϻ§ҹÖƳɰǁǊZŚɆļ',
                                                        'ȼǽʆ\x94ŦҳδµΉҠʲɪʰǒȧșɥ6ãʤėѻƨƃƴӮӮɉλѝ',
                                                        'ƹεϸǓΊӢ˧Ȼ˹rрсӄƟ4ΑЮԆ˙ȃǴØǱԚѐR;ǗʈȺ',
                                                        'сϼȜ´ƢŲıΡ¾£ǤЁȭ\x94ԏ±ʦȗӘÑɟǗƹѤҦ҈ѯȞʤș',
                                                        'ɪȭÚɱ˸űϗɔӔˡˏƆԟϺÓҦԪʏPЦĠŤȥťҐ˜˄ϜБî',
                                                        'ŗʄΠПŶ\u038d\x8aΙ˘҉ԍǤȴɌχˏĴΎΧѕǭƠʊʪßþǫǉŹ\x99',
                                                        '˥¾ӛ¥îɎє˯˱ŜŚðōӋġƞȨţĴӝͽƹ˩ΫͺԃĹʇҥʓ',
                                                        'ɗǺӡƖҦɜ\x99҉Ɗ\u03a2ԂėʸWтԦͿΠˌǉсѶҁϖjȆѝǑҷҾ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ˌϖPπƐҪЈЦЗ9bf',
                            'value': {
                                        '^': 'int',
                                        '$': 6847813679996256930,
                                    },
                        },
                    {
                            'name': 'ȃɽʍϐYҋÎɁȜҾӍ\x9aȒɖô˥ȋԄʖҦС',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        88286.1803140195,
                                                        44838.19466120063,
                                                        380409.5757443238,
                                                        7698.473924983366,
                                                        850372.2292986157,
                                                        271381.5988690738,
                                                        658320.4644513523,
                                                        -32331.613425286283,
                                                        368591.8708503377,
                                                        233971.1640779327,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ҶpӏHzΞĕїѓѪqѭȆѳԬѻȍǯҊβˡʣʤ˂}\x83қԗȢӸ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'π¨7ĹβƴIǞ9ƔӫΤʽƼŴԗù\xadȿӱӮhŶOƙľ˫ˬʁϤ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210327:032020.650789:+0000',
                                    },
                        },
                    {
                            'name': 'ͺдϓԮśЧӧˎ-ǤhȨҀɵ\u038bІюĝĐвɣȭŤĖʖʉι',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        '¿ȍԒƻ˧¼ԨΉΫ˗ӚøШǴќͼѮɍѲϻʿʉһōӀäȓUН˲',
                                                        'ԞѿHǝј%XΟͿϩΡĝʴύƨŉŶʶɞƴϚ˱\x89˕ïͷЯĮǣȔ',
                                                        'ǉǃӧӹȐťәӺρИʡEŴS£üҎТȶ6ӍΜʅ\x8cʆȏШȟːŭ',
                                                        'ɉҍËǙΓ3Ч[D˅ͿȂҾԣԥÎΤ˭μɝoaǘǚXʟ×ňǠɱ',
                                                        'ԈˮĎ\x9cɽўѰӼԍЁǛѱɿɺÝʞȌž\xadĂÔԄΨŝȃǐɶϽǦk',
                                                        '˼ǳԨjѳ1ÂΌОƧхʍˉЂ\x9c\x92ƪɴӅ^қѐȂ|ΐːsnгȸ',
                                                        'ǈÜоϬԬːԢԫәƩϚЬƧР˕}ЭĞĒ\x8dĦұѓΕҧӰτ˔ñȘ',
                                                        'ζМÍѐāwǏ¹%ÇИ˹ɻԮŘƽɒ(ɿ\x9bӽĖƿƚĢǤѐ^ѹӕ',
                                                        'ːΡȅӂ\u0381ãϰŤȺξ~ИsÝĹкƬĿҧ˂Ĕ˾ϯeӑƔ',
                                                        'ѧtȭţϗɝТƠ\x9fҕţтȮ˔Ρäиӊ҅ƕ\x99Ěāĥ Ʈ҉ʼkĔ',
                                                    ],
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ėЏɚȾӋFƴ{\u0383ЁƅʓđϮȗƽÿЮԉΥĤӴȺlƉАSɡӾǹ',
                'message': 'BʫŋԄ¾ѧ˨ű=ÀĝAȢƏłńȴәđ£҈ũɦԆZϭVԍσľ',
                'arguments': [
                    {
                            'name': 'ͺ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        850754.723200144,
                                                        68881.39016740516,
                                                        527338.6213156374,
                                                        332009.9322114274,
                                                        504907.3433619231,
                                                        824467.5041587225,
                                                        279732.04396685894,
                                                        81627.93541285896,
                                                        791524.6856203185,
                                                        534299.3582638217,
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ȁɺϫ:Ûªҡԓćϳ',
                            'value': {
                                        '^': 'int',
                                        '$': -357694540056371101,
                                    },
                        },
                    {
                            'name': 'ѱÒƔϱųҸ҃ʯƚB=ѾһɷԪăȬ³Ñέ=ƴМǮYā˧\x9eϢ`',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        788608.608115419,
                                                        885410.7592364971,
                                                        765319.0230506245,
                                                        958410.1241484073,
                                                        892078.2518319666,
                                                        284827.60729425796,
                                                        973039.49479898,
                                                        956809.1645472152,
                                                        694176.2211473796,
                                                        612666.8790152845,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǃэβĝԒʲġЈĘûϋʥˣɁQɯɺČý{ȎԐΰԁÍêĩʼŮϡ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ъŤĺҠÏɞJǾIϐІkϨøǇǚʺċʁάȕӮ(ȪS`ÕǗԌȃ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210327:032024.785028:+0000',
                                    },
                        },
                    {
                            'name': 'ӫɏbҽtĥιȶſ0Ԙйк',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                    ],
                                    },
                        },
                    {
                            'name': 'ƞϝԣġӰІԥɋǗũɫӡћӹõʫŢЄνчҟӫH¢ʞɦ˪ˇԑԡ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        791067.0902457525,
                                                        893791.7100099808,
                                                        26147.386775030827,
                                                        262076.8312515177,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ϧǻǶԣѱĐϔ˧˳ʕ:ŠȬǲDê¯ʴќɈԫѸԈċƽûҷ©ӄЪ',
                            'value': {
                                        '^': 'float',
                                        '$': 519061.23456858145,
                                    },
                        },
                    {
                            'name': 'ˁèĵƓπ«ƾƘԖȣ)Ɔʑ\u038bə°ÅĒȑƵӵ',
                            'value': {
                                        '^': 'float',
                                        '$': 914954.6414614293,
                                    },
                        },
                    {
                            'name': 'fӻ¤ÌˊʝͳӋÃϽŏҌɄɳҐłÅ',
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
                                                        False,
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

            'identifier': 'ԋԭƥЈТ',

            'categories': [
                'access-restriction',
            ],

            'error_message': {
                'catalog': 'Ñв',
                'message': 'ś',
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
                'identifier': 'X3ҹčϜƩЁȒž҉˧ǮǞ˫ƺҁ\x9aʌʒϵз˖ПѺ\x9fßЈʂȱ#',
                'categories': [
                    'os',
                    'access-restriction',
                    'file',
                    'file',
                    'access-restriction',
                    'internal',
                ],
                'source': 'Ңϖşc£ʢ\u0380R§ˌǞǁǹƐ',
                'corrective_action': {
                    'catalog': 'ӼɞÃϑʟӘӝÁӸdʭŜˊǨǘĶΝΣѱƥҼ˚ľάàӜȰҖˏФ',
                    'message': 'ѥɒǫĸѺŤбƁɜʮñɲӉѥ½?\x9bnŞư˰Fĉ\x9aΕhԐИʳƂ',
                    'arguments': [
                            {
                                        'name': '&Ԯ«θηɘǮѸϳ×ɟҮOӯϡŴś)"ЮҎŤEˇӝˡǟȬƘÛ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'БεҽşŝʕҡfƹңвŖɳōͿě˪ͲżèıƑʍ˫НȘȧʟўĻ',
                                                    },
                                    },
                            {
                                        'name': ';ƵΎɉӅʑǰÌˋйǶĄάȞĳ*ȗ)ɔ˟ȵK˘ϿΐЋАŧȰˉ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ԓҦĹȗP˾\x91їѬzɌĚəȞАǖʏȣӭɾʦʖʗʅѦ˧¬ϲѺΡ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2167099859889343988,
                                                                            6981719634940437008,
                                                                            -3947538043949077914,
                                                                            4661210371553042335,
                                                                            8546722415739649171,
                                                                            8070662662049805842,
                                                                            5449007134620693422,
                                                                            -5167483844167753339,
                                                                            8106521594439719941,
                                                                            5192196635068353810,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8eӖɞβŊӸ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 165675.244145861,
                                                    },
                                    },
                            {
                                        'name': '«ъ˻ӤȒѿҜʸѕƩ϶Ð',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032016.233755:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ν[ǮƋȱШΈzɮʚȈԢȾͱсĊԓŎŤȆҧˎʿDΌưˇDƙѡ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032016.320048:+0000',
                                                                            '20210327:032016.341588:+0000',
                                                                            '20210327:032016.360784:+0000',
                                                                            '20210327:032016.379576:+0000',
                                                                            '20210327:032016.400672:+0000',
                                                                            '20210327:032016.423741:+0000',
                                                                            '20210327:032016.444693:+0000',
                                                                            '20210327:032016.465236:+0000',
                                                                            '20210327:032016.486303:+0000',
                                                                            '20210327:032016.508568:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЍȤ˒ʦʭΈЂ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '1Ĉh˓їǺϢ7҅˜ʒɟ%;ˑȸЏßӜ²ʉӒҤöѥɼэ1ɆÐ',
                                                    },
                                    },
                            {
                                        'name': 'ҼφȿХĈг\u038bӉƆСľɂˮ)Ԣčˣ˻áϒHă',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            291902.9029950924,
                                                                            956426.4027084925,
                                                                            825395.9795961939,
                                                                            640268.0147091221,
                                                                            18927.460473951156,
                                                                            751220.5562318441,
                                                                            852074.6405447412,
                                                                            668294.4850710034,
                                                                            138205.60887237245,
                                                                            993849.3133582394,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɕȧӰəŭǰҾȡíЦǆʠŎ˒[Ϯū˒ȄŏÚζƑԐ\x9aŞӇ1Ǐѵ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7073323808982934525,
                                                    },
                                    },
                            {
                                        'name': 'ŋʜԚĭϹԆƞȇΓЙӝ×ȞѶ˺˩ˎ/ԂǬӌcʭ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 925135.8728684069,
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ʔɑȽʣ^;˨ƞʛȸĠҺ$ʅҴϷɊǔЁʖŠh\u0383ЧǆˣġŨҬ\u0383',
                    'message': 'Φš\u0382ǔ˃ęIĉƩҒˍ͵ϢʹӉӕΔƎ\x8aĒĴЭȚґŤȿƦ2ǘԚ',
                    'arguments': [
                            {
                                        'name': 'ӾѪɓӺǸŋ҃ӺԖt˗ƔʵÌѪȧƮɣƢǚ΄ŰӁ\u0382ΩМΣϴ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032017.165302:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x8aɆǎŖϑΏïǘRȮʐѫyє˦Ƣ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 485015.60273304034,
                                                    },
                                    },
                            {
                                        'name': 'ύлҒʙưˀôɯѝԅԪé',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'nӷʬ\x89ǐɅ˂ɂòţ\x87ĢŶʴňȽƎӥÕЂцŦʮѴΌƨҪтĆɻ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6704255457546513715,
                                                                            -6145155360079658068,
                                                                            -5125578312923301655,
                                                                            7824906232620244872,
                                                                            3649869225422415986,
                                                                            3237069424232699419,
                                                                            8178318024105557797,
                                                                            -5780299173104638501,
                                                                            7482441105576368324,
                                                                            -2991992095617514004,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȌǼʸƺ\x87˲ƺìԅΪҸϢ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032017.624240:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȆԈӎѹąӟѐӀkΣѩ¢Ĳ\x97ȟǀϯɕЬɥӹŪώƘ=\x84ʎϜ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032017.692612:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǺEѤϽ3¤Ǖ\x91ɒȺγµųԛ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '½ǌƊѡѪȧ˞ûӵ˂ǉĤĭÄɜɑΣ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0380çНə',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            112816.76493103866,
                                                                            -96888.22701229446,
                                                                            446951.1763400256,
                                                                            -10219.159382367565,
                                                                            372172.48470899,
                                                                            697639.5000879267,
                                                                            -18186.35897550454,
                                                                            518283.2759497162,
                                                                            -91296.68993882333,
                                                                            440473.7342673405,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɷɾӢԇŧWR˝',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '×¦b˴ʽYΦǫԩΫ˃Ɏίѵ͵ÀϞѮϤђϻ\xa0ЈŮєѲđ\u03a2ʰ»',
                                                                            'ҮȘήҘÜȗþǦˢԙƂҌǮҟǾǬ\x9fȳǐȷǱұɢƛɰ˟>ƥǬD',
                                                                            'ϺЂŮϦ»ΗŴϵFĤpƚ҈ԁχԙ҆ц\u0383ҢҽįƌʲǤЌƮ¶Ќѳ',
                                                                            'ƩўøȦƻҰӡ/κØԉБѯġĈľ#˾ɈʩϬүɁ\u038dѓѿΕŀҌǒ',
                                                                            'ǁΜӱ_ȰƚɠʒŠųӻË ǫãş·ƽż®ҶˣϨ΅ɡŀĻкɲʫ',
                                                                            'ȲΙ\x84ϷѴ\x93НζΙBƇČӠ\x99Ï\x86ԪĽȊҌKÏѺø˃ʮ\x8dŘΎΠ',
                                                                            'Ưѻʤǽ¾\x91ќŻ<Е¯ŒϋÆҝɞҖοĿʹͻƽҙеƭ\x94Ԉĺɣľ',
                                                                            'âǔ\x95ƶƆ¡˷ӊɖиĭԧӜìǫEҦұ˶Ҋ˱\x8a2ȲǈӒȕԧ\x8cΉ',
                                                                            'ɪЃ^ϗӘҺƸҍȶÓʧǂυǬѓ½ġǥэЧ?\u0378ьЕșТфǉƹʢ',
                                                                            'ęZǜÆ\x94ŽӓƟřΆʣәҋÂԝ¡ŵšʝљþϕ´\u0378I΅ŉЅ\x99ʥ',
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
                'identifier': '\x97σΥƕӓ',
                'categories': [
                    'internal',
                ],
                'error_message': {
                    'catalog': 'ˌ҈',
                    'message': 'Є',
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
            'locale_code': 'ĢΡąΊĜwÓʀ\x97Ј',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'ƶ',

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
            'catalog_name': 'ǬvӅϝԢЫʐɵǘюӁfƊȰðϷ˫ҫӖ˖ČʇϮʍ˲ɱȾӷ˫ɖ',
            'locale_codes': [
                'Ͱˡɲ',
                'ɮȓȚцΌ¨',
                'ȷ',
                '(\u038bʗɡ˵ĄΑӰҢǀ',
                'ȦϩȭǸ˨',
                'ǅԛœ',
                'ƉĻљ\x98rùξ˰Ďě',
                'ǀѧɍþӜ¢',
                '\x85ğˈ',
                'αƻzˣω\x89ŝȓȁ¬',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog_name': 'ӋŨʹ',

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
                    'catalog_name': 'ŅÍԍƲˤ8ϝjźɪӈВгʳ\x96ŏĂ˻ÒʇșƺҜөŀɷѠҘșҧ',
                    'locale_codes': [
                            'ѐ',
                            'ч',
                            'ӓҐɔΚҩƞñЏĳ',
                            'Ƥ"ŷ\x87ϱ϶Ό',
                            'ȯȨҁGŻrɛҩ',
                            'NҐɅӀƘƐǿΏ',
                            'ŁΥϲ\u038bļȡ',
                            'ΤяЖƸӕ˃ʫŪ',
                            'zϦ',
                            'ʦŻԧʈҶ',
                        ],
                },
                {
                    'catalog_name': 'ЏУȵȯԏˡѝ˲ĎZɱœ\x86Mŀo˓ʢİɒ˴ԙǺȒԂɺɆÂwζ',
                    'locale_codes': [
                            '¦\x8fЂŧĕ',
                            'Хƿʉґɞ\x8c˦',
                            'ȥėʬǇˋ',
                            'ͺ',
                            "ȖæŒ'.Ƙ",
                            'ĳǁҶÎń',
                            'õɝѪǵǍԗV\x91',
                            'ĖƷԐƄδƺǐԉͰѾ',
                            'ǹÑ',
                            'ȎɑϢʰ',
                        ],
                },
                {
                    'catalog_name': 'Ǭ҈ɿ\x9eq^˗ÃƅúͽҜԂʔ˃ԬѓԖҍu\x7fԇҵϞ\x87ǝƏ˃Ѩʁ',
                    'locale_codes': [
                            '9ȏɔɘ¨Řϩ',
                            'ʧԀ҆җƣʺ˝O',
                            'ԗű˘ƀśŗǾӊ',
                            'mǠ',
                            'ӷtãçдÄb',
                            'ͺϻ\x85äӒϧńµ®ǳ',
                            'ɋИ',
                            "ԆЍĽ'ĵV",
                            'rĬ',
                            'ƞʣԇ˘ҟěɝʪ',
                        ],
                },
                {
                    'catalog_name': 'їƲ˷ϷԝûϲʯҐÇĂŐɅҞÝÛøˁñǽЫͺϾț\x9bǄАȡԍʙ',
                    'locale_codes': [
                            'ÿʨäǋΞ',
                            'ōą˗͵ǈӸЎƁ·',
                            'ɘù',
                            'ȭ?Ǯ<',
                            'ѲǸͺԢԆʁС',
                            '¯Ξ',
                            'ǯȔ:ȘƙÙ#',
                            'ĻЍ҂ȭĀĦԂǂŬ',
                            'ȉ',
                            'ûҤԧòҭϞƠӓ',
                        ],
                },
                {
                    'catalog_name': 'bȩʙɊŖ0ĢТлņ˘\x94ҒçȾѠGˑŀΏςŮ>š.\x8dӴɗҠ΅',
                    'locale_codes': [
                            'ϣʈ',
                            'ɝϰĒѶžƐЬύі',
                            'Őԇ',
                            '£Κ',
                            'Ǵ˪Ƣʖ',
                            'ʯɄÊ',
                            'ҜJĐґøƤ',
                            'Ϟʪ`\x91Ɵі',
                            'ʣ',
                            'Ɵʣd',
                        ],
                },
                {
                    'catalog_name': 'DӿΩȹǴϟÃ˯ѽɤԤԢԎŽ0ϣƛǓǡϪĆƸΔпʿÞǃΌȇŝ',
                    'locale_codes': [
                            'ћ%',
                            'Ʀξϲ',
                            'ӱƟ',
                            '·т',
                            'ƐƛϵÏҖıǶ',
                            'ƻ©ԈƳѥňǖЈ',
                            'ԑӥĖȥǘĎ',
                            'ʛµĉ',
                            'Ɠԍä',
                            'Ơ',
                        ],
                },
                {
                    'catalog_name': '¬ǅͱ¹ʀК˷Ò\x85ҎӍȿЅHȒŹʹɏYͰLǹʦǧ˖ȡ˄ʢ\x9cƻ',
                    'locale_codes': [
                            'Ǆ\u038bПĳǓьjο',
                            'ƽЩҼмˉ',
                            'ԠÌ',
                            'ūȸȉ\x83Ĺ|',
                            'ИӑȱɆΈӳv\x99',
                            'ȴ',
                            '˲Ď',
                            'ʂȝԌҠxŴԢǵ',
                            'Ɋȗʇ',
                            'ϵ',
                        ],
                },
                {
                    'catalog_name': 'сóѳƕЁN˳ίTBԟЎёƷȄβƿ',
                    'locale_codes': [
                            'ũНЍśӻ',
                            'ϪÀǊ4ȢѶεъǟ',
                            'ŁɫѼĳʪǺ\x87ǚҶ',
                            'хĠѤϣΌ',
                            'Ǟ\x8fѿЯөŴащ',
                            '\x81Ц¶Ɯ',
                            'ӛϓȦ¸',
                            '*ÿ',
                            'ʣϷ',
                            'ɭЀйђӄ¾\x8cǁϹъ',
                        ],
                },
                {
                    'catalog_name': 'Ђ+º\x8afIԐǮ˼ʤϐχĖԂ\x879ΕԅљόΑϜȢεʐпѸǃfϦ',
                    'locale_codes': [
                            'В\x8a˳ʼ˝«ïĥ',
                            '˔ƪїӁȍХň',
                            'Ј\x9fЯ',
                            'WХҵˍǈǞ˽ȵ\u0379',
                            'ļǉÆȞҲåǖĴ',
                            'đξ',
                            'ˠЊȈİCί;',
                            'ЦȓÈÌâ',
                            'bϓ\u038dǤΓȯϪDȐȬ',
                            'ʜӧȲʂûҬΨǑ',
                        ],
                },
                {
                    'catalog_name': '˝~ԉ]ȏdΨ\x9eԑĴҪѰɄʵɇёыˇюȓ˝ϑǢНɭʁʮӧŎĻ',
                    'locale_codes': [
                            'фԌ҈Ӽ3ϿƝ7ʑ',
                            '˶âơƄǱх',
                            'ԓ˝Ѡƌї?ź',
                            'Ӑ',
                            'ŘңϊʿϹ',
                            'ÜЙ',
                            'Л\x87\x82ƃ',
                            'ʪ˾ıԅ҆ҫĥΰѨ',
                            'dôѿ',
                            'ԃ˹Kπй',
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
            'name': '˵\x93ɉȻѫʇ˃ʳрǹˆϋэʗ\x9eßνȰÌĨœuxğ&ˎώκӏV',
            'code': 'ӽΚ\x97ʷ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ҍ',

            'code': 'ʩ',

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
                    'name': 'ͻʜƠΔɼ\x85ƳȽüȇˡЭȵʨκǽÙƿŋ˃ӝ«Ϳӭƌӿϝȧ˨c',
                    'code': 'ŀϪ',
                },
                {
                    'name': 'ɌæϼϐΆǪɸԟɭϼŢосœíУиǴʁθřŮί\u0381ŬȖDɑäR',
                    'code': '˟\x8ať\x9cдΛӵҦʿ',
                },
                {
                    'name': 'ϖȴʴʅκĴŎ«ɩ0ҙĨΖ$ˁÊ˚õŏ\x80\x98Ӫ®ƫͿӉ˺çԇх',
                    'code': '6ÉĨ',
                },
                {
                    'name': 'ɺɸĭЁŰHƐЭɱɜŭ\\²ĥĈǧювΟӦ\x91ӭөљ˶ˋяғȫϝ',
                    'code': 'Ŕ˸M',
                },
                {
                    'name': '(öаҹчʂϫĝϨѝã¢)z΅kѝΈψɴˉ҂щȰԏэ6ľoԤ',
                    'code': 'ɩƦrӷĬ˃ҨԪþ',
                },
                {
                    'name': 'ǩƹ^ϫĔҰϣѺϮȱ8ʔҶЁōДǏȾЈɢѴǀӐѥԀӤΕԞª9',
                    'code': 'ȹЙ҇ԝbtΘΊԓ\x80',
                },
                {
                    'name': 'ȕ_ϗšͲӆ˔ƙü#ÌîǬǧĔԃħkJƫɹσϙҗ+ӡǭ[ȘE',
                    'code': 'æǌӣϤ',
                },
                {
                    'name': 'óΌİӳ\x82ȸʡ˶ԕŒ+ӳǾ˲-Ƒ\x9b\u0382ӷÑәΧ@ƻˉɔԕhȽĿ',
                    'code': 'ÔɤǪѠÚƩɣ',
                },
                {
                    'name': 'ӟ´ƶ"ѕ)ӏѧ\x9eσёǺҸʬӬкԨ/ѻ°ТӼƱҗ\u03a2\x94ѿΧЫã',
                    'code': 'Ϫӑӭѽ/şѡŁ',
                },
                {
                    'name': 'ӣúƞ˥CŇ\x8açНȖϫðЊΕѮӠ҆ķȾnȍ\x94ӪɖќӈȢɆѿз',
                    'code': 'ŞŞнΩ7\x83\u0378˲ʐș',
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
            'locale_code': 'Οɪ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': '˳',

        },
    ),
]
