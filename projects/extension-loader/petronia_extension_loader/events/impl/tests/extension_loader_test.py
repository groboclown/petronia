# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-12T16:50:49.166172+00:00

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
            'name': 'ӁŊӜʉʹțǇԂ\u0383ʇǩ˻ȮЗ',
            'minimum_version': [
                -3812505392802275229,
                -8411433109778416688,
                -1958608560192195493,
            ],
            'below_version': [
                -2284024272935400958,
                -1301498537478074717,
                -5378336641288864584,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Λ˄ɗ',

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
            '$': 'ϷҖЫÄȲȺϖФćΆċɾĞрɈҢlͼѩӽϰӑłӡҰ=Θ`ĵʥ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -7354549952908113320,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 356001.6476125876,
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
            '$': '20210212:165048.586938:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ȃÜǚǾiųĞƩďȦѺ˟ҾȨ*ѐʨ˥ɦԍѝԙʂˆԌǵҕԮǔĄ',
                'ƢäɮȜѻͼȴˁƱ˻ÔÁˑʎӣhbʖɩ\xadĥÑťʄɪ˲åǶɜѻ',
                'sЂИȟцЋϹ4ʮʼȇƺš}ǫħџ\x83Į¬ȕӴ,\x84ОǹИǈһά',
                'ĻƔÀλҁ<ȎїΆɣѵĉɀˌ¶ŵхҏLӀxӉʰιÓɼōßы\x9c',
                'ūƶӺϺеΑˀȹȂǼҳŜÉӔƷµ¤˩ҎъюʧΐǶɞ·Ъʙ5N',
                'ʢ5ΎɨSƳȢ\x84Ƹ%\x9aʚҔLÂč½ι˶ÿê¡ǁʵɩʡƈчƭѳ',
                'ϼԦƸϹ҈ʦѦ\x87Ȱ˭ӷ\x95ƘƆĬǠJ˫ҀϢґԗцрΫӣȭƒʒ ',
                'ҞҴjƪ\x9eˡĮ˟ԗďȄȧϱэÐ˪ηßđђþ˄ŕňҶҗʋҰЍ˔',
                'ȡĤ\x90ҹúқш\x94:ϽȬUĔѻʈɷχӧɐҚԦūҗѯċiSɊʖĬ',
                'Ȼ¿æʓɞӱˢʞЍͻɉ¢ԈćʠǱÔΩƢҿϳʸFЂϗaɇōˋɫ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -8222368358031612502,
                1695719073127505397,
                3121793086502024062,
                -1685244198407289852,
                -2472502059013978297,
                3549414568285571276,
                -7992480131533541656,
                -773103722062076638,
                -7330595179471471418,
                8029887568196218524,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                352109.02114164986,
                325801.86638548673,
                733082.9811372941,
                447683.7444081501,
                -54300.52870269316,
                518135.7096938996,
                138817.99017142344,
                789324.1746129665,
                127011.01433878954,
                605358.4940619584,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                True,
                True,
                True,
                True,
                True,
                False,
                True,
                False,
                True,
                True,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210212:165048.588011:+0000',
                '20210212:165048.588037:+0000',
                '20210212:165048.588045:+0000',
                '20210212:165048.588051:+0000',
                '20210212:165048.588057:+0000',
                '20210212:165048.588063:+0000',
                '20210212:165048.588069:+0000',
                '20210212:165048.588075:+0000',
                '20210212:165048.588081:+0000',
                '20210212:165048.588087:+0000',
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
            'name': 'υѯˋŚ҉Ͻ+ŭϰ\u0383ӪͽɃЋ˶ΓGɯɷĬ',
            'value': {
                '^': 'float',
                '$': 553369.0340512821,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 's',

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
            'catalog': 'ĻͰӝɝűŘԨĺЕҖҤ:ɻԇԪӠÂ©ɹɞʘьʠ¾ϘŬŜ¤Ȱâ',
            'message': 'ȲҶϏ¾гˬӍСѳǟΘʂĥȕɉǐяʂÃԠĴӍɐήӞÏԛ˚χƮ',
            'arguments': [
                {
                    'name': 'ÚͿҟԂƶ˰ӸͷЃλQѲǧɰ4\x9bуɌԭǅŨԣʻѯԨƩ˟ăŀȻ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': '¤ǥкΑ΅ĜϬɝʕɹʢ¸Ϲʹ»ԃϋę҉ϗȂӣъʅǟӖȢȴҏV',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ѥ°ôƚȨȍƍԧǶuȽШĄӻÐƥԇȪʙSЊҩ΅Ӄšîйʨқυ',
                    'value': {
                            '^': 'int',
                            '$': -1588706720208377721,
                        },
                },
                {
                    'name': '˜Ĭǲ&εґŬҘBmŌѯВκ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'Ϯ-ԖƏϽžÓƧ\x8bӬĲYӶxӓȥӲ\u038bтȃ·ɾɴҀŵэƔѩƛҸ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'Ԯ˘ςt\x80ҁƌɭǽԇƚҟυɯÛʿǑԅʗ\x80ʭ\x86ɮϯuύЉįȼƳ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        True,
                                        True,
                                        True,
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
                    'name': '\u03a2мԓΒļ҄é(ЈɝĻκǖЅs¹ʓǡ˸ͶЪЇзʔXi2Л{;',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ÐULʵɜԖоҙζӂν>ǡϗĳєĦγȦȫˇ¬ÎΨ˽ƀΟƤьҖ',
                                        "Ц˼·Ą˼ϧϗԏŏʂʙԮϮʉҜʂō҃ʤǃɬë¿Ц'ѡ§łї\u038b",
                                        '˛įϻºѿΗԌ͵#/>Ɂɴ\x8cƎɋȐdʨȖԭϢǦӿєŘʪBgƇ',
                                        'Í\x7fĒhșkΙ\x89ɱÍɇĴƃӇǅóҀοˆƵĉӄɋɻϯŷӥӒ\x9fŀ',
                                        '˛ǎ¸зкϟӊѾͳɮɂȟϏʞ˳ВЊ\x9b҈ӆō\x9c-čġΙӛ˼ÇŦ',
                                        'ͿΖɫιϩѫɘ\x8eŏҼχӛġǋёҘйƺĭԈԞźЃдÔѬɏƳкϋ',
                                        'ʅȳbɒǵZγϭцȨμ˲ɫŧˍȎ3ΧЧΦÈȱ.Ψ\u0378îϳƮ¥ˡ',
                                        'ԬӖįъѹӣΒЊƣƹԚϺѵˣҦĉ\x82ȘĲϢ®GȯԭʳNHÛі\u0378',
                                        'EƵΌѩҋеԘĠӜJӼƱȖίʔɓʢĆ҂ȎɞęҺҨϠӺƿЉsƝ',
                                        '\u0379ГҶөɀǓӳ\x89TʀĢԄөнʨŕȅªɮҲҁԜųŴ\x8bīԭͰɂÐ',
                                    ],
                        },
                },
                {
                    'name': 'ԁдɥҤɬ´РʛӔȝɅÚɟͿΌƅņПҵϖú\u0380\x8dҾʻǤĄÊԞҖ',
                    'value': {
                            '^': 'string',
                            '$': 'ľөҲԞҖѾѣąѹҞƙIÀӲѷ*Ϣ£ǜ·ʛĳѦΞ·nŭƇŮͶ',
                        },
                },
                {
                    'name': 'ǓҷӔĜϦΐʕĴˋƾƏԪ=ȇɃďŒȼ\x98ĊЙ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        1689417832017197205,
                                        5739849398341536588,
                                        8760249576154479864,
                                        7140714350397339907,
                                        -8962698989407113599,
                                        5544973187599948675,
                                        -6786360726580485760,
                                        -3418514504929761156,
                                        2282834205946978655,
                                        -3830489799479329098,
                                    ],
                        },
                },
                {
                    'name': 'Х¡ǆπȌżʕѪΩǅȣΘЖ\x86Ĩ(ȐɣśҼһҵNIԂõĬФҰԚ',
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
                                        False,
                                        True,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ȅ҈',

            'message': 'đ',

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
                dict(field_name='messages', name='Error'),
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
            'identifier': 'ʚѾjΦĶLȷî\x84dɣҥŞʟΤ4Ç°ЇӍЛȤɥӲЉ˛ĶuЉ\x89',
            'categories': [
                'file',
                'file',
                'file',
                'access-restriction',
                'invalid-user-action',
                'access-restriction',
                'access-restriction',
                'access-restriction',
                'invalid-user-action',
                'file',
            ],
            'source': 'ѐĀԏˇҪԝΤÛʇЦŬŪĆґmʓ΅іǵͷҮƆΤ˚ʚÂèĶƚǽ',
            'messages': [
                {
                    'catalog': 'ѱȈͺǎ,злŐʢҝĒΈ˄ǻюӐυҨMîӾ ʚȥɅȥѿǕOс',
                    'message': 'ǃâŗзƦʨΥȴҶşàҤҶԡqŮì\x7fηȵХF˾Ѳʶ˥ΰЕȆΞ',
                    'arguments': [
                            {
                                        'name': 'ӄoΣȶÖҽϋmҰΦ\\ҺɊқЍÅξϑ_С҆ȭЀ{ǥªͺÐĐ.',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ў§˕μҵʸɁЭòžǵыь',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '{лo¬˲Û˟ǌΌȥ\x7fʇ˄ͲʠҞϻƬ·ЍʳԤΐǝzϠȯƆǿˉ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 6190.622848905172,
                                                    },
                                    },
                            {
                                        'name': 'ː@Ĝʩ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "ʎУɅΎ'ğӭҳҲġÐԭҰԨёŮӗ\x93ҖŞɔǈϲѣŚΊɦЦëǱ",
                                                    },
                                    },
                            {
                                        'name': 'PŪ˨˛ԗĆʹяŕђʥԌ\u0382ǓƃZόǊʝ\u0378ɘЏƗϬțʞЍ7¶Ϣ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6534070856005692428,
                                                                            -3768989207663485350,
                                                                            -7276883650964950609,
                                                                            335933610194148769,
                                                                            -201352520098354022,
                                                                            -4044933315028400819,
                                                                            -8871427536107414850,
                                                                            -9053077655785808286,
                                                                            8434505906897938131,
                                                                            5842462945792255694,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϤŲИӒSѥЉҐĸϊˁ\x8c',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
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
                                        'name': 'ĈΈɷјũ˙',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.547022:+0000',
                                                                            '20210212:165048.547045:+0000',
                                                                            '20210212:165048.547054:+0000',
                                                                            '20210212:165048.547061:+0000',
                                                                            '20210212:165048.547068:+0000',
                                                                            '20210212:165048.547075:+0000',
                                                                            '20210212:165048.547081:+0000',
                                                                            '20210212:165048.547088:+0000',
                                                                            '20210212:165048.547094:+0000',
                                                                            '20210212:165048.547101:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԈǾķʕ¦Ԙ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165048.547344:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƋӽʯѕϼĝсĭЭɨԗĮɭǕ4ȁÂǾԘÃԈ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            170253792113746378,
                                                                            8272286333362007783,
                                                                            8434002471387417137,
                                                                            8641040629402981209,
                                                                            -7991650333905043372,
                                                                            6596873444966354509,
                                                                            -5970361642790858889,
                                                                            -8082632662340932567,
                                                                            5461449616065161736,
                                                                            -1067102112759118736,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˲ǑҘ˴¼\x91˔ŚөϸǟñĽȊƵ=őĘĈzĉ˱ňǒʯȳɛ!эǚ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165048.547773:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϱɘԪ\u038dÙˑԁÊǅъ$ƾ_ΞĶќĜʲœ¸ǁжŔƃӳщŋњҺȩ',
                    'message': '˵ӨɼыƻΕɱʙ5ΣΨǰÈſƶĉϏƘťϋқɹ³WʺʤφýƇ\u0379',
                    'arguments': [
                            {
                                        'name': 'ԄΉѦ.ŗϢȞ@LÌǷǙɕɞȕɂ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            423107.146103267,
                                                                            595247.7747490524,
                                                                            850104.1527130526,
                                                                            647912.086836103,
                                                                            939763.7536822642,
                                                                            585806.3290002383,
                                                                            504844.997819345,
                                                                            35601.605579925614,
                                                                            67835.64595130866,
                                                                            691043.6783601531,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'f\x99МÍȘ.άɡĕɢϖʅřļүНYcƵƴѐӄeЅѼĖЛh҉Ę',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7825142765438614947,
                                                    },
                                    },
                            {
                                        'name': 'ɧɼӭÈΛĝкǸµΤӂƀź',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'үˏӋ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6893370628957772974,
                                                                            5175127223322595735,
                                                                            2612934351132625161,
                                                                            -268345858246218696,
                                                                            3796218023663967009,
                                                                            -2516035507148996500,
                                                                            -7358858958950724502,
                                                                            -6529259074958857915,
                                                                            -727358378336526192,
                                                                            3023747244435867135,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҦѢӧǖ˜ϑҽҡΐҎсюԘÕʄŞԏ˗ɪ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ťҧ\u038b˙ǐҀ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165048.552818:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x90ӘȢƅҮˏЭȘʸOԠрύƵ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2763673293163332216,
                                                    },
                                    },
                            {
                                        'name': 'ȤĉэЖȊï\x97ϝ(ӌƯϰн˕ÜԃƁԜʺ;àǦӍʧü˕ɾƣdц',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            908548.4462021827,
                                                                            819481.1333139559,
                                                                            890794.5776920875,
                                                                            358211.2011191713,
                                                                            795820.4677596358,
                                                                            846020.8836062886,
                                                                            523071.85547449905,
                                                                            191881.82459724793,
                                                                            529994.6443433331,
                                                                            109563.08739624606,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŵґǢƕƂѝľ\x93Üň¼ϪӧϳҮɉƕӉßӆ(œɀQԨ;\x82п',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'NҳʎΒϒdǞÅƁθĺʼӸĴʟҡЁǘ«ӷӪǕȆþбҗ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 704511.0107095859,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȢȨ\x8b\x92*²',
                    'message': 'ʁưҥȮЄ]ӟƲϏǖȬ˓ũήϬͱй͵ΪѼϣȉΦŨbƵē}ɦǌ',
                    'arguments': [
                            {
                                        'name': '͵јС˙ĭȨӽʿìȺʺƼӘɘðČ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 31106.178940912127,
                                                    },
                                    },
                            {
                                        'name': 'ԃԄҝΛǅԥҲэÂɀMˎ\u03a2Ϳɞ˂ÁOΣÄ\x82҈ɓɾҵɾІʘϭϚ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'кЭ˙\x99ʝїŀɞԟɣƉϺԩЌɄɣдɭǴϣ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɓҀ˕nĎgĤИƂ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3839367898548299762,
                                                    },
                                    },
                            {
                                        'name': 'ˁÓɴĬЦŗҗʊϑÎ:љȹҁŤȭĿ˾ɎǱʹɬȔѩҗЊҏ\\ɼѓ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165048.558337:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȩ\x95IқӨҚЅgǫʢ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ĥ×ҙɫÿФPǞϴ˓ɋ҆φȥџӾ?Νǡ;ŤȎǚđӗ\xadÈØΓ\x8d',
                                                                            'ыȓɱАg˧юƍΪŷ˲ʱЦǒĘϽ¡ϜƍşҙžăғɡŌĚĘ¦ȅ',
                                                                            'Ӄͺ·\x90ʞƌθȎč¡ѻːʂˮҵԉƋԩҳƹϾɃȽ¾¡ϋќ+ҳx',
                                                                            '˹ϲбìˁĮƐɚûˤγхņԗʱ`ԠќľƼˤ9Ӆιѻљɢɀęϊ',
                                                                            'ԘψmνȑðҬ\x8aͿ(ΞϣΏҟӉ÷Ǘť\x81oãĹɵƦĭ\x99΅Щț\u0383',
                                                                            'şёǍȔŮԥ\x97΄џơлƁˌ˾\x9eˡĲT˭ý±ßʙʛʎӫƈĉƐÚ',
                                                                            'τõāҫςʕĞ\x95ňԄοѓҫÈɻρǃӛê²ɢɭ˪¥ЭȾɎļԏҫ',
                                                                            'Ϝų:ɼѯȄĺ\x80ȠTπ˫њԥԨà\x86¡\x90іɅЅſѢϯū\xadŶŨ\u038d',
                                                                            'ʛťґϨ/ɥʉ÷˴ӯԨĘ˫ȿɗЙ¿ʇґϣĻҗ8ˍEʲӜNvƎ',
                                                                            'ѻʲ¢\u0378\x92ɑΣӘΠ3ҶȪɵǖ}ċƂώӡƵʒǢƫĄУѵҴÈ\x8aȂ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĿБЖǞ_ǳɰƑʽĀҧ{ȩȍв҅͵чȔӜ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'HЛ˔˶[Ŀҫм˯Ũʜɟѡ˸ȽԚѾɪӨÈRȖԃƗҁŻ˅ɪϕʿ',
                                                                            'ŴΐɷėȖ\u03a2˔ΰ҆ǯřɖПűɛʕԦƜ¾ċƄƸ\x9f±ŋ\x8dϓ\x93ӄλ',
                                                                            'ѩȬ\x9cѠӦӺ\x89ů<дԅ5ǄΪ´˃ȗǺҘșӕŞνɧсЎǓq÷а',
                                                                            '˥Ʀҙԉҷэ˪ͶϕѩѫƔNƥŚΓʢњĕқµƭӉѴӛʿεľǦÒ',
                                                                            'ǁƂǧŷπŲ˂ƃНʳÒϓȷҊιʟОЍԏņϧɏͳЭaЊȘĶԁȡ',
                                                                            'ƣyҌрэѕ@ǲюŖѸ;ͳѪîȵҳȉӃƌĭ8ƲҨ-Ƒô҄Ӂʿ',
                                                                            'ӈÚӭҖƎ\u0379oШѿŸˍӪĆș\x95ǯ ҀΕcʳ\x8dҴԔӼĩ\u0379Ұ,ϝ',
                                                                            'ѝ\x8eŌƳ˼ӦөʵӔȒҦ϶ӅǌϗѰуƌΈŘтНĲɷϘɵԦʴˌӨ',
                                                                            'ŭ$ƦѼӋĳ˽ƌӡˤҺǥ҃ѤŞӠʝ˦ӇȘģȘɞǼ\x99ȺķʷO˻',
                                                                            'ӄʦɠGȪҾǈĵøήƈӨŰǘʎβԆʰ@тͳĤΈЌȻ\x84ø¿\u0378Ɏ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΰЮˀʭĦѮ҇ĳeη',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '6FǼ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.559650:+0000',
                                                                            '20210212:165048.559668:+0000',
                                                                            '20210212:165048.559677:+0000',
                                                                            '20210212:165048.559685:+0000',
                                                                            '20210212:165048.559692:+0000',
                                                                            '20210212:165048.559699:+0000',
                                                                            '20210212:165048.559706:+0000',
                                                                            '20210212:165048.559712:+0000',
                                                                            '20210212:165048.559719:+0000',
                                                                            '20210212:165048.559726:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЋʠͷӸӘ˒~GͰƨΒĺϖȒůEŝśӞԘÈ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϪНӟáӎɯŌӕʭcϜƵƯæţϸǺ\x97ȴŭĜŪԮǙϘάėеʙı',
                    'message': 'ŇÞǳҍʵӠĭˎтξzФǇϝѿƀˈ2ʰѝӿό˕ŔќōÓɱЧǛ',
                    'arguments': [
                            {
                                        'name': 'êȺΗǡʓũřÄΫWǽȯìȵΚ{ҫ7ʞԙӎˍʥӭѯ˽ϔɡΟӆ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.560473:+0000',
                                                                            '20210212:165048.560491:+0000',
                                                                            '20210212:165048.560499:+0000',
                                                                            '20210212:165048.560505:+0000',
                                                                            '20210212:165048.560511:+0000',
                                                                            '20210212:165048.560517:+0000',
                                                                            '20210212:165048.560523:+0000',
                                                                            '20210212:165048.560528:+0000',
                                                                            '20210212:165048.560534:+0000',
                                                                            '20210212:165048.560540:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȨϊʩʦɣͿlΫӿʌɶ\x96Çϖ\x94σнӅӛȐŞ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3641230145974104753,
                                                    },
                                    },
                            {
                                        'name': 'Þ£ΔѵǽԎµfȏтĻ¥ҧĕŋӲӡˋȿ-ĝӔӆÜѹēbĝɡĤ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '9ӺĐɭлЂ_ȯ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6606821077195748518,
                                                    },
                                    },
                            {
                                        'name': 'șNͲʴϭгɿŅə=ɎȋԏȡËΓ\xadɀʵņшԌǜɓȷǀʍӺŅˢ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': "ȉÜПĦ\x8aͼѫWѤηЁԈÄҶ\u0378цõ?χУɉΨ'ѶȱΟgëǆƿ",
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.561580:+0000',
                                                                            '20210212:165048.561598:+0000',
                                                                            '20210212:165048.561606:+0000',
                                                                            '20210212:165048.561612:+0000',
                                                                            '20210212:165048.561618:+0000',
                                                                            '20210212:165048.561624:+0000',
                                                                            '20210212:165048.561630:+0000',
                                                                            '20210212:165048.561635:+0000',
                                                                            '20210212:165048.561641:+0000',
                                                                            '20210212:165048.561647:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x91uȯ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8526101346519683476,
                                                                            -2315154758760420854,
                                                                            -1195769395529860184,
                                                                            -193341250309549480,
                                                                            -9033731362873251458,
                                                                            -8879242458327209000,
                                                                            -1457384197841375511,
                                                                            3336545278899867141,
                                                                            8749722302625033777,
                                                                            6148807965014649603,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӡcƐȝ˖Ҋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165048.562164:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ѧ˖ɋʇȠ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            344330.2973198482,
                                                                            662903.4429385145,
                                                                            34485.05376941452,
                                                                            81896.00714447672,
                                                                            31457.247788300127,
                                                                            621284.174909072,
                                                                            179457.03318644845,
                                                                            -27711.99317301593,
                                                                            947714.7811043799,
                                                                            390511.865759679,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '΅\x91bәr˓Σ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3122985067298468557,
                                                                            6380994582781143848,
                                                                            8769366889229515652,
                                                                            -501938643643825606,
                                                                            4455792759859223388,
                                                                            1036385866489860533,
                                                                            -3308962867621841188,
                                                                            8734761543392203637,
                                                                            -8806151649231495167,
                                                                            -3530945608225575112,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѽɗ',
                    'message': 'ΟǥĹѪҌˠΨƴˬΚ\x84ǟűʘ˜ƥ\u0380Π\u0379ɢľˉԥǃѳò-ǰϘӮ',
                    'arguments': [
                            {
                                        'name': 'ҷÄѾϴϢΗǴŧĺӚҬǌƫ\x94ʔԮ·ˢuɯĘѲѥɏɓnĤϞǸб',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '\x8eҪʃӓŗ`ťʕàƉбΗʟ\x8f',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': 'ҝďƉMνNŻƾ҅.Ía~ŅǵԍΎʰ˅ҟҧŻɖʑȻϘԞͻȝӼ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.563500:+0000',
                                                                            '20210212:165048.563518:+0000',
                                                                            '20210212:165048.563526:+0000',
                                                                            '20210212:165048.563532:+0000',
                                                                            '20210212:165048.563538:+0000',
                                                                            '20210212:165048.563544:+0000',
                                                                            '20210212:165048.563550:+0000',
                                                                            '20210212:165048.563556:+0000',
                                                                            '20210212:165048.563562:+0000',
                                                                            '20210212:165048.563568:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9cÈљϪ\x89ɁČqŚӁҿєӍӅȿʏɁƷȴÆӡȋŀ˕Чԅ¢ɒφd',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4149710872367836333,
                                                                            -5162250593022383012,
                                                                            -4225291776692477581,
                                                                            3792319243140700291,
                                                                            3950698567671012730,
                                                                            -1195698301303973938,
                                                                            8150524462846994071,
                                                                            -5403519880499649563,
                                                                            2047778371169691755,
                                                                            -2309396854356551026,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŃųΰɿԆӓKҊ˄"Δκ\x8cǌӁԁǨɂ҆ϘϱëйɅХpʇ\x9dʎҥ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8346877147453048630,
                                                    },
                                    },
                            {
                                        'name': 'ԒԃԠӐª˞ζƹ˘ȢԃČѶԁ\x9bǡƹŀƥҀ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            216882.34032440383,
                                                                            -72808.84618402019,
                                                                            126969.97482574676,
                                                                            38881.06380480595,
                                                                            487497.7420317284,
                                                                            269370.2265911356,
                                                                            142616.3338997986,
                                                                            972905.9999166187,
                                                                            165652.2608059378,
                                                                            371695.9690808226,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǝ\u0379ӋĲʒǪHæ\x86ԛӞҟǼ,εӎƶòήӭçǁԝψcYθϺʄ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.564432:+0000',
                                                                            '20210212:165048.564446:+0000',
                                                                            '20210212:165048.564454:+0000',
                                                                            '20210212:165048.564460:+0000',
                                                                            '20210212:165048.564466:+0000',
                                                                            '20210212:165048.564472:+0000',
                                                                            '20210212:165048.564478:+0000',
                                                                            '20210212:165048.564485:+0000',
                                                                            '20210212:165048.564498:+0000',
                                                                            '20210212:165048.564518:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӻ§ʍ҈ÞχÈ´ВɥШŢĨhȥÚϦ0°\x94ͺǁˬѰſŷӒǍĵ˳',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165048.564808:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȒǙԒʬ2ΊӨďѶˊȨåҁȤ\u0380ǔʃ˗ϕ¢ӛǁɶºχЪȞ=ģŌ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '£ǳӑƊӕʭX3˟ǷϸКϜ³ɮԣςѪԈȓˊ\x9fıÒȷƨșЃûƯ',
                                                                            'үƘÀǉʘŊóĎ˺ҋɋжӌÂѦӖǌҾ˛¶ǖƟȶȴȅҦǞƀǴҾ',
                                                                            'ϟѸ¢ĉϦδŦǍūĀ\x9aoɗʇǷȸҁԔΣǕ\x99ȺԦȗϽǯԏѳƤϩ',
                                                                            '˩ēˢȳʰĠǁč\x81˞ȅС*ʲʻɹӓʻEǠʽПć8\u038b\x9cӿɭșʕ',
                                                                            'ϜѬЀÖkδ˝ϖůԗŊżԝė¼ӜԌԓ˗ӯȦϸǊуʙӺƻKҼή',
                                                                            'ɽҊɓϢàύƱƉӫǡΔĕәǪԪárʬʆŵʚɇƬȡψŀȉΡȉñ',
                                                                            'Ũ\x9aҡӛԚӻñȨκýДǆϸǯ«ǟǯAΎġːϭʝǆɒMφ¡Ȃǲ',
                                                                            'ȓоҲ\x9d҄2?˫ǑȐʭШʁɫʌÝιӑѨѱϿ»ĺв϶ͱ\x82˹ʚʃ',
                                                                            '\x8bӨΨďƓ˙ЧΈЌѤѨƊžŴƻ˛Ƙ\u0380εӬсGјǐԀ΄ĩʩįƨ',
                                                                            'ȣ?ħќӡ×ǭяʅѭˣŤ-Tηɕ\x8eвӖҘĢěǻƨýʾԡӫΔЩ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'һƘǞ\x8bԠÇƯӔɘѰʊªӯǊɼϿȃѽɭ³ʝ\x90ʖύǢ\x95ĢìlӢ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӧɍѥnмəӷη+ƇĘȇȈҪÞ»ú7ӐiĬϒКǞŬÚҐ҇ιc',
                                                                            'řǷӄǿƴԌгǇ\x93Ǩɞ\xa0Ƀȁ\x93ϗūƦɦïŸʞѢûa҈ţƩӬ!',
                                                                            '\xadˀόƌВюĎѓɇ<УԟʃӖμʷȀwЈɿӴ¶ϰЋńɀЩҩѦȏ',
                                                                            'ϫ>ғӗŲâκʱ϶ǏʥŬԟűӝēЏӺӶǫΣ¿ƉͼƯƛ+ǉ˝ѿ',
                                                                            '!ŻӑӉХƁğųєӼԥÙ˯ЯĮǁl;ǔѨϤғʚΒѝȽͻӍμн',
                                                                            'ɷ÷ãњQŴĿưԄĲ˱ΫљŪӊ\x9aɲСļKȭɓɕ]\u0383ВǁҝƁĽ',
                                                                            'ǒԪѢɡЏʭɼԓƞļӏǣǸĬªĤХˆлƇùxЀКϥԚρŶɒ\x9f',
                                                                            'lΖѡѳ|ҩҔӧŬ\u0381Κө\x84ɜɍ]яʿƱɸãҁ@\x8dͺҡ˂ćťĂ',
                                                                            '˕˼ɀʄɱÌVƞщч\u0378ЗҩL{µĻPҌN˦Еϫɺ˯˽Ąԃоɣ',
                                                                            'ǓȃɢHҦƹ¥\x88\x8d˹Я\x94ϸʵR˙ЏђԨԖӎiƯMǧMäʑʠҟ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ńΌC˰ҦʭѰϾͲ\u0378жĈøӌÖƖȚӀIϼΓэαŚьϞКȖEϑ',
                    'message': '·Ƨ»ќυԆҖʌ=kʱUʲɸԘǕʡ4˶ǳƲȞ\x9fЇ˾ɋĤƩΊ\xa0',
                    'arguments': [
                            {
                                        'name': 'ťìǱǙžҒʗӝĦΗӸȕ˳ǢtԌҬTơAū˒Ɔůďƛʃ®ɸϺ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʏάȭ\xa0!ǋ¿ńƴȞɌŝѺŻăɹѺӱĶѽϽϹǬˏӧ¯ѐԏӜǕ',
                                                                            'ƧԄȱөª,ҟϑŃʪϘŦÓΣ\x84ϡρƦԏԦ\u03a2҄EʩɷȕҒ«ɾK',
                                                                            'eЉҡ˺рƧмŚVŌĚХҌÊƜӗӒ±òȽ¦˄˺:ŤǘĜȓȦ˻',
                                                                            'Q˵źÎӼӽӎ\x8aϙϻǍʾ˺ԤВİѧɵҏҭΨƜҺю;ʚŔʾɭӎ',
                                                                            'ӫ˒\x95ƃґʠџѲĚǴнϋń¿ӖΤĦƯȻuóɽǕʨĤ\x88ԗĺ҄F',
                                                                            'ƆʩѳљĪØŘҠӟƗӫϱȯϸʜȿɢʀ˅ИʡԙӣÐƇJu\x9dƣò',
                                                                            'ľϋq´ǲЕ;\x94Ͼ\x95ʭ˞ҤŻ¸ɉȏ\x9cϑЇƋӵŞԞçςĵәаÿ',
                                                                            'ҶúʔÈԇ¹ͲΠĜÊӝÒёОљгτŃ˧ԃќӥĭ?łſέƊč˻',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɶäęɐŢ£\x97ĪѲбő\x8bФԛǷʥ0ųȽ¼\x8cԭκӶҋү˞Ζ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ķɌФǛ°ȜΏŀ\x91ÛβcŶʶЁ°ӶΊ϶Ă\x7fѧԕЌ¶yҗĽҋΨ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            899197.033682361,
                                                                            715129.8801514646,
                                                                            832340.9017144655,
                                                                            254864.2104464647,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΓŖʂ ŋĂʵЏпȃǁ¸ʘ\u0383ɡӓʩѓЮ˒ГѺҺ˅ƄӶ˦œОӝ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4984673489822447243,
                                                    },
                                    },
                            {
                                        'name': '\u03a2ԁ\x9dʥҚ,ſӗŅ1ʄʹ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'QʀʙȸѠԤhЋğÉЙRλºаˁSг˩ѧгˑӅаӀ.ҠȉϪǀ',
                                                                            '\x93ϬӎƚƆ ԧʔӉʩɕ\x8fŷ˃ХНɺʚòҠ`ΖҁԍŤEӭɦɺʝ',
                                                                            'ξ˺Ĉūɤ\x95ĒĐҴ\u0381΅ʕ68ǚыӤ˒ŅĞƅԂwUûҤĻӔˏő',
                                                                            'ўӘЃϏӃҢѵϩįԛʠůʌįђćȅ˄mύǐƁɀԇӹθj\u03a2ǢȆ',
                                                                            "ǯHÿ˽ĸƶԂЁŗтŤϞϴʖźƾŵʹʿ'>ɗ7ǃűȊǆùíȴ",
                                                                            'Ϋć¦˚ѹƂҁѿӶ·¦ʋʟƵѐĆÓ·ЎɷԓӉӡH˻ȤfүŨѽ',
                                                                            '¼ͷ\xa0ŮӓȤΏҀ+ЦʸʡÿǘWɄ\x92ӍωÝ΅\xadm\x7f\x9fҲвҒɉѩ',
                                                                            'ŗƳԄ˓Ēҕț¡˝мӧӛϟĲԐ\x9eɥˌԦƑƤʒaȀŉԞќƓǹĒ',
                                                                            'ҋϗ4öǓΒЙЉԧΗӾήηǬнŚǿԟΡƃɾȞηϸԊþȆŰΊн',
                                                                            '˧ȟÆŕʕΫưΟ˃Ȑԧƿ1ϊơdȯϖǤЛśǦɪτĩѫрˢНЌ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҵа\x91ѡǏ˧ƪΧǽȿԮț҈Ѻ\x80',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5317777125427331444,
                                                                            -653281542209592401,
                                                                            -952752437781547123,
                                                                            -3335864533983166633,
                                                                            6863068867424677400,
                                                                            -342880085110115791,
                                                                            -1745489299628966158,
                                                                            3330761521467535315,
                                                                            3692084740949445958,
                                                                            -7913384563080949820,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȃϙʼҿӮӂɕȜ`yʰӋˣȾΩʰ˶ѳʤɔҥϡҬ4˘ŃιӚʁŞ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˕ŠόǕѵʩєđЉŦѱÌҫ҅ōԪÔ\u0381ι˟ŎίШǔiɛÝǝ\x82ϣ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165048.571299:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÄĭϜƚîά˸ϐʲʏ\xadū·űŋкэ\u0380ϜήΧəƵ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            740108.2916498539,
                                                                            226058.44268760702,
                                                                            905387.4406885641,
                                                                            905912.2127968713,
                                                                            656606.0907676968,
                                                                            8485.00480949122,
                                                                            798596.3984702011,
                                                                            374334.35470829956,
                                                                            3087.488208208728,
                                                                            420239.77475695213,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȔϱΙчȌŏžǃȷґөȪˠΠϲ˴ɘȉ\x99ŮMȨΏΥΔ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.572006:+0000',
                                                                            '20210212:165048.572028:+0000',
                                                                            '20210212:165048.572036:+0000',
                                                                            '20210212:165048.572042:+0000',
                                                                            '20210212:165048.572048:+0000',
                                                                            '20210212:165048.572054:+0000',
                                                                            '20210212:165048.572060:+0000',
                                                                            '20210212:165048.572066:+0000',
                                                                            '20210212:165048.572072:+0000',
                                                                            '20210212:165048.572078:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ґː˯ҵϾϢӭlźӵԀǞƚӣјӽ˟ɏɸí\u03a2Ě0ΗʾDņε\x95ϖ',
                    'message': 'ǸɗȀȤ\u0379#\x95ɒͿƫɟϋбΤâȢe҂ХΞ´ɘɑĞŏ&ɍ¥Ĭʁ',
                    'arguments': [
                            {
                                        'name': 'łȭ˶ϘÊӭҞµс<ПʦĪ\u0383˸ћʵ¼өèŉӥǳӐĞҩyǠӒʌ',
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
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʏƯŗʬДBҥƖ%Ш',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.572939:+0000',
                                                                            '20210212:165048.572956:+0000',
                                                                            '20210212:165048.572965:+0000',
                                                                            '20210212:165048.572972:+0000',
                                                                            '20210212:165048.572979:+0000',
                                                                            '20210212:165048.572986:+0000',
                                                                            '20210212:165048.572993:+0000',
                                                                            '20210212:165048.573000:+0000',
                                                                            '20210212:165048.573006:+0000',
                                                                            '20210212:165048.573013:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ëЋËȎȝԙ˔zƒѝ¿ʕГԒюѺťҚ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7418821683447357827,
                                                                            -897486227507846388,
                                                                            939159861092060953,
                                                                            6744672080362692703,
                                                                            5236388509108004395,
                                                                            6409634825919857696,
                                                                            -4752513024951333700,
                                                                            6230485689790803761,
                                                                            -7441614366553544347,
                                                                            -3573608317574626488,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ґʀԏǅɟǭVıͱѳаϵʟϦȬAΨĎƎΫЍīȇйğJЭӯ\u038bˑ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѯѣǎˇ͵GрѬºѹϽϩɶ˞ɧQ\x81ӎʱԙɰњҕÉÈÐ\x95ȣћԓ',
                                                    },
                                    },
                            {
                                        'name': 'ŀӗƭÖʮҲɠ;ʪВʺʀЭҴƙЮˤ¸ӿэ>ĦʾȢȗǡŒЍмș',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -21628.660108370896,
                                                                            321922.1570774398,
                                                                            98466.47404129693,
                                                                            583271.5154690957,
                                                                            219940.03685257304,
                                                                            771850.9052257318,
                                                                            934816.336498281,
                                                                            -62958.79765011264,
                                                                            852906.2193551598,
                                                                            932785.526845359,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "·ʰɧ<Ӵȫ'ʠɒŰɦӸ[лԒΏ",
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'ԠŗʂЧ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -246804419157707443,
                                                    },
                                    },
                            {
                                        'name': 'ђƌЛʀŢɵ©',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7334099406095302231,
                                                                            1173209159208918950,
                                                                            -1314167265642911185,
                                                                            -2579279656771904821,
                                                                            8706082323914050697,
                                                                            -3010990366437520292,
                                                                            -4687198679925899518,
                                                                            2387760775890365972,
                                                                            4853158906880184908,
                                                                            -4874995624178363287,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԙʄГŘƫƇcvº',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ʫљә:ӨȌ\x8eŁΎų\x8aƭǼřóƜɮɃ˖ҬϹCϱˎԭ^Ԝ\x8aӌХ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǛʅьԄˑÛƃĻ\x9fĄD×ҴԘ ӍƼĶҎҏƩҘɘūĆʓҢ',
                    'message': 'ȥ¿˗śѤą˖mКȁ˂ȭ\x92˺\x82è˥π\x92ыԋӬƀ\u038b\x8cɈѿёϗх',
                    'arguments': [
                            {
                                        'name': 'њѳИӯˠǚ\u0382ˌҶ˃þ§ŔԐxһιԨ½ΊЎԋӫùΞϦԂ϶ҾP',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7648196350049222659,
                                                    },
                                    },
                            {
                                        'name': '˶',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8094111434077244221,
                                                    },
                                    },
                            {
                                        'name': 'ƲǄ˃¿БƀȠʨȋëӲƇȐʜԟΖčɆãÄ˲Ґ7ɯҙ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʚΖöZǹȻƵčѫϸϻɊ-ΰʳѩɔǏavčåγӯфƾēȸӜ\x95',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.576540:+0000',
                                                                            '20210212:165048.576568:+0000',
                                                                            '20210212:165048.576576:+0000',
                                                                            '20210212:165048.576582:+0000',
                                                                            '20210212:165048.576594:+0000',
                                                                            '20210212:165048.576613:+0000',
                                                                            '20210212:165048.576630:+0000',
                                                                            '20210212:165048.576644:+0000',
                                                                            '20210212:165048.576651:+0000',
                                                                            '20210212:165048.576658:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǗUʥ\u0378ÑϦĕƯȓѩ[',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'ӺŚȽĀҤƁÊɦ·ŭǺȒԭΚǊӧҡǡ˭Ԯ\\Ӎ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 160957.13621386653,
                                                    },
                                    },
                            {
                                        'name': 'ĥӳЅɴ˷˚ůѻˬĭˣӄ\x96ƁªąӐų\u03a2´ŧÚҪîuώȱȊԃӷ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '΄҄ŤԚʔɧǧǆˣÝԗΩʕ5ĆνɳˣŦзËƀνǄǿe\x96#ʉҀ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 242777.69242335833,
                                                    },
                                    },
                            {
                                        'name': 'ȊӾŧȌҏɴġҸ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 676832.882679441,
                                                    },
                                    },
                            {
                                        'name': 'ƬθiӰӍμıыǥʸ#ˏΉ\u03791ʜ\x93',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5415656858406403579,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΘĔ˹ѯʶҰьÅͰȠɉϰӄӕĊƃiǝ6Ťӭ;ІƃɢѮҢĆҐА',
                    'message': '˷ɛБĥӢҰӊŗɯϕÕґ˒šƙҍΔʧʧƥԕ҃ѴϫˉŔɈӵͿ}',
                    'arguments': [
                            {
                                        'name': 'ˏӅ·еrӕșƆW1ǷӗЖȯДԐƻ˂\x95ХʺgЌŌɝΝ˹ъ§Ѓ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'αӸƜӄ^',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'нщ(ǣ\x88#ǩҾЉ˨ǩĩȐ_\\φԃԨΒѰ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 668846.6757456075,
                                                    },
                                    },
                            {
                                        'name': 'ĮͶԫԐΝϧԫ×%ǎʔĲˠʼŠϯП˱ŐԦϟҀȨȧӠǘĴù͵ӛ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5369104625487102090,
                                                    },
                                    },
                            {
                                        'name': '\x84ԞŅӊȡώΝ&ŵǥϊԡɞʈƞŢ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            347754.995725254,
                                                                            391744.10545816587,
                                                                            246043.7065036783,
                                                                            662630.8502251403,
                                                                            780279.3907125443,
                                                                            350736.0671173018,
                                                                            752447.397077141,
                                                                            536653.5235761964,
                                                                            927675.8365539116,
                                                                            -26506.579355598064,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ş',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165048.578959:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ӗϣ\x9aԘ҇Oϟӥͽ?ɜɵʱBe\x80',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 73757.35021983815,
                                                    },
                                    },
                            {
                                        'name': '\x9eӸΝŧʯҞηɻ2ҁ\x81ҞӰȏʞƤπ\x9aμȥЪsΔΩͿ\x86ˉö\u038dʹ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210212:165048.579224:+0000',
                                                                            '20210212:165048.579236:+0000',
                                                                            '20210212:165048.579244:+0000',
                                                                            '20210212:165048.579250:+0000',
                                                                            '20210212:165048.579256:+0000',
                                                                            '20210212:165048.579262:+0000',
                                                                            '20210212:165048.579268:+0000',
                                                                            '20210212:165048.579274:+0000',
                                                                            '20210212:165048.579280:+0000',
                                                                            '20210212:165048.579286:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ŗӟ:ϊЛŔьƭĺӁPȉɠ³àˑĵĨΌɂƛƾШʳɈǙÛƅΔȊ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɃОнTϖæāÕφЫŎȐ\x84ǰʁÂрˬàŭȶ=Ǔϛ/ǖǐĆ)˺',
                                                    },
                                    },
                            {
                                        'name': "â'CϽŬФӓϚПƽ\x92аǂŞǎwòөĜɣä",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3307951499608129599,
                                                                            7182665219023419539,
                                                                            5570940437649897489,
                                                                            7664953613820849980,
                                                                            -4360703606393143919,
                                                                            -2777841286747573720,
                                                                            2572416745501402089,
                                                                            4057400416231146855,
                                                                            -7251827176697996672,
                                                                            -1161293779367588913,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ɔ˯Ѩɞ\u0378ɳϙE¬œ4ϭīɱњčȲӝŠԅƬƖʟŇ҉ʻ\x86ϳҘϿ',
                    'message': 'Ƨ©ƺțŹ\x99đțˣӠö˅ȟТ\x87ȧ\x83ϲ˟óȢЎYүЬԂ΄˷ʐҖ',
                    'arguments': [
                            {
                                        'name': 'òΨϯԬļҡaƮɻΔƙϸϊț˕ԛԃϗɐʝ˖ӋʀĄΫ˞ΕΎϙȆ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '_οʃůèȆԦʘªԘϔӱĂÍӧĨĻūƎKοęЎɕѬӱ%Њіĉ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165048.580550:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǷӲѯơƓļӯ˴ң',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1116012428562630080,
                                                                            -2173412963856035493,
                                                                            4218134305689435736,
                                                                            -5057936140110407995,
                                                                            2582487581047625051,
                                                                            -5154388321194434265,
                                                                            8086721976962269791,
                                                                            211038355567441280,
                                                                            6882173480366698006,
                                                                            2701576610235845400,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΥҝѕʑʊʒԑҡϹʘђЖϘ¹\u03a2Ԣġʪįt¤ƹƑїӷАԊSɲ˜',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5381709882202574489,
                                                    },
                                    },
                            {
                                        'name': 'ÿ?җ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '|ǴÛĖбӎʩӃˆӖӌȰˈǴ˛æǝɪәΦφΝe-ȸηɤKрɎ',
                                                                            'ȍƢӚŉɾРNúͱ˱йLģʳƢŨ6ƑȤȩɐӬҔѫϦʐѪɐє\x83',
                                                                            'пYĜƄŠҁЮЭϰӀҦǊ˻ԓȨêǐřˉ\u038bjżϟ\x8d˲ӄѹ&±ĝ',
                                                                            'ɨqˤ\u0381˔L|ҴύωěЌŉҰӸƈӂЅɓуҕңȕқĄҀƪǯÛß',
                                                                            'ˌӰƱҬӹ\x7fǬɦϘӐѪԉȋɞӇņÙā°įʙӹԔħΫϥ3ǆѵ]',
                                                                            'НîδɰǲҠʏȿɖĕϲʮͿjīԈάĭȱűÆǜT~ˌƺŔӘϱӞ',
                                                                            'ρUŧŀ£\x8bˋÐȢř˶şàˣęǫĨĢ7Ԉŀοʨ\x7fEοΗӕȈМ',
                                                                            'ɄӤɆҥзХȝǘͻÉȱÍҬ҃ЀǫÂѕҶĂʶǁӼϦ\u0381ÕǠǒǧT',
                                                                            '˺ǽϚɂҬȋƐӼпƆėơ҅ΏӦѤčˬ?ҶӁҵԧѮǼѮʕ@gӑ',
                                                                            'Ó˻ɶñƄϴϬ˚ ðûӺŒŦ:ʥũȣCʙӠåӕɮǗўӪԞαξ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ª;ăҳӭ"ȄӠƨūχќюwȵŭчϘɩ\x9bΎәϏԘʸe\x82ƶĘ҆',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 71657348862643963,
                                                    },
                                    },
                            {
                                        'name': 'ŇɟΎˊ҂ɎœHηбǶҩѡԓһӓԪʜɅϿŃҳЛŻ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            508098.11121570563,
                                                                            966960.0918314378,
                                                                            174863.1611852668,
                                                                            700368.4396691814,
                                                                            245169.02148301475,
                                                                            359842.371974494,
                                                                            312850.507031712,
                                                                            941475.372354152,
                                                                            459419.7626639736,
                                                                            720686.4073945831,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɤɯ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210212:165048.582029:+0000',
                                                    },
                                    },
                            {
                                        'name': '˲ɸŝÀƿÀĀБªҦDǳȅɓӬΏΝҟº',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɴ.λųʘϛȒѨшʨŲeÇӼԍ˜ǁʊǳő6úΓ\x87бѳϳӉɵɜ',
                                                    },
                                    },
                            {
                                        'name': '\u038d\u0382>ύȺӮƳŶ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            775566.99069086,
                                                                            151891.4310390088,
                                                                            -77413.74520540878,
                                                                            -75348.8950198261,
                                                                            870409.571537896,
                                                                            232016.3530772978,
                                                                            120108.54800883617,
                                                                            20257.241944857044,
                                                                            492332.66495470493,
                                                                            84328.50974976685,
                                                                        ],
                                                    },
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ȏ{ιïő',

            'categories': [
                'configuration',
            ],

            'messages': [
                {
                    'catalog': '҇ƅ',
                    'message': 'ŏ',
                },
            ],

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
            'name': 'ëȢΟ-ƮӉɖЏέƔЙˈԂòƫȶƫ¾ȿǐѲ˲aVˇŸͱԚďΦ',
            'error': {
                'identifier': 'іѤτȧѶų˹Ƈȧg\x91ZĴѕπʄӜԞϿ.҃˥ǄƼйňǯҗåȨ',
                'categories': [
                    'access-restriction',
                    'configuration',
                    'access-restriction',
                    'file',
                    'os',
                    'os',
                    'network',
                    'configuration',
                    'access-restriction',
                    'access-restriction',
                ],
                'source': 'ƒǩϡɪҒõɠǰї,˰x\x99ɊКǟʹԠ;Y˞ÑŷҪŭϕ\x8eϺѱΣ',
                'messages': [
                    {
                            'catalog': 'jŃѡύƽĽĠԏʖģȓҁԖ®ʴŮſɅɰѹȲƮӧÊͺԟǖ˷÷ɂ',
                            'message': 'àχ\x97ҚɑԖЈ\x8aΆ)ώƟŦʔѯȠɢɐƥƈ\x93ż¿\x9aюưɮɀμɳ',
                            'arguments': [
                                        {
                                                        'name': 'ҍİЙΘқrиʤʤһȵЌл˃ԁʛʫƧҦŦǘѻŚ+ɩȟϔ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165048.510510:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɱўɻ\u0382˒°',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ěʍυɚȱʋĩ˵ʿҮ\x9aА˟ëȰ˾ĬͽϧүΖѕˆŜ-Ԉσӷŕӝ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2921895840394859687,
                                                                        },
                                                    },
                                        {
                                                        'name': ':ѣψiПΡ"ƂΒȽ˨<Ƿ\x8c΅ѱМĩм҄ƩίĪŧ\x98˶Ϗŗǵ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 915478.315374823,
                                                                        },
                                                    },
                                        {
                                                        'name': '҄Ħ\x9dÉ˱ǊѼ҄ƓɄL^ʐϥǶӌÀəϺǬɲ¼ʒҖҡǽϊЈϧУ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҒȚqÓӪǻŸҪE|\u0378ϵДŏǔ»čΌǢӣɤĀ˾ǄÝШԣŗɣғ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŗ`˚ԈˊІʬϣªƅǷҲƺƬцԙɰϢΛɟfïʋÐɓ\x9c˧ʝųʁ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɩѪЧǉWìȻȩGϱżњǝ˹ѴʭˆãˇЬÕ´пɬʐАȑθԏŒ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 239837.89598557592,
                                                                        },
                                                    },
                                        {
                                                        'name': 'œϫ4ǩΕѝƀΨƣƟ\x90Ɔȃ\x9bŔ˭\x86Ԧӥ]ҋC',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҝ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˯åŢ˖ʉϦÐøʨӓÖ҅ŭФǢǯHŞ˝\x8eˮ0π1¦ЎŧɌǢ;',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'РӗȐȱΛΧ˙ɰņƾӎŒǎˢҬЂφʡŞOкΝ\u038dËÎ\xadƌÜñØ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ЍjӃ҃Щӧʞѵ˭Ų˚ȢЮǁи}фɣԑɿǽăÝӡ¹ȍɑȒ§ļ',
                            'message': 'ӕɐ˂ˀҏϐʹΣӢŭͷɕŗӵɕлżǙ˘ϼԇǶӻŇȾsŕ2ɰɴ',
                            'arguments': [
                                        {
                                                        'name': 'ИΎπò`ΧҽŮĘșˎŴÈŉŇΧиɟѢïǬÿʒϭқŽ˓ºӌӎ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ųї',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6114133645344130534,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɾǶѶΐΫʖ]˷ħӹӐˏҚôǼöðȵʍɛ·΄ѵЅϰȠǬеɎѼ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ВήХш\x97',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ғѮχδөʁǪʹƹºˬШ¨y',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˭ÏӸѹӉˋԡʡ\x88@ôФĜͳТѥɬɥĲKŃѤԠϣŨË',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ' Ȱ¥ĒЙѷơ΅ѹŪTȘϵ˥˴ɘʝҋƊʡѕ˩ĆӮˑɏƵάΡı',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'f~тϤιοȗʢǪƢ#þϵ\x8bкǅӧΣÙҺűӈʆΩǢĵ˘',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŉɽɢϥΒǘȊ=ЀƥɄԝ˽;ˌːǮXÀˇĊӨȨɉѸǘǇԈƐχ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x99ϒ$ŚhУřίşǮȰɣʖ7ŬΆȥɫÇɺȲԘ]/ӒŨ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165048.522528:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΌҁūЭ\x82ƲӣĲřïƁƌŬƟAȰУ¿Χǔѧъ¾ȈɖΌLѧFʽ',
                            'message': 'ҼɚƱà·řʑͺϓιѾɣʮɂ7ȧԝ˦ĐȋƩ!\x8d΄ÞȤȏƸȲщ',
                            'arguments': [
                                        {
                                                        'name': 'Ҵǀ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9aZ\u03a2ΆԘĖȫӅƚĮϴzʴ+ҭ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165048.523764:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'xЦźйҼ\x8cČłĉ϶˄éȨŵQҡρϷơӀƷñƒëͶȺÔɄӚå',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͰǺӯ·ŝìһҿҮəʱќ\x8dʭБ˟˝ӎƤ\\ӳϙʢԩǏӖUўЀˇ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 9160175058356831685,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȄϤҧ\x92ǉӲɻĭn',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˌψ\x9aȹӅĝɹć˟ǷņҿǧƒϪɎ0Ʉ;ҖĐԘӸÅŕӮđҰ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȀέКƦԋǒ\x89ůӟÃħɿʣҖҡʝ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѯŮ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǿˋГʋƼ˚љ{ĹҎʴ\x8f3ŗtЙʺ{˧ǹҺӶìʝ6ВȚɓюĚ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѠƠȤϕӰԨїêϹžҗƨųЦҴωɊbğф\x84ѺƇтОʂĿMҏɆ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4220882098477944592,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӨԤԃ2ĎѺӭԂ˖ȧɋʙӬΝ¨ӑŭ~ŬȬҗǾ˲ӑÓȒνĦĤμ',
                            'message': 'Ȯ˦Οԁʭ\x9bͺŦ@ǡĐϩЗʍ¹ʅ\x91Ѭ8˸ɤʤζʡõǻû˂ĴǙ',
                            'arguments': [
                                        {
                                                        'name': 'ȐéǜˡʘЖȆĉǎҢŘǦԆ˔ϷЃůΒбŕǽǥԃπƏτƷɨʎļ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʙѭ\x98ʣԜǛª´ƅƫǱϠòҙɝəҀҽѬнȸГºϜӂƿǒĝĥҲ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 786922.697334893,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԅʶ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҪƇJüΗӝ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǯƀȗƃǊIʴʕ\u038b˘ÍʽɡКΫӁϙ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÇʋɔǱƜƞ\u0380RҮѭƠҐŃģǢŭыɱΊȬýҜ|¸нΐуʚҌd',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2229532814497147776,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӧ˗ūͻ¼HɽȁɑɟŋҶøǀƁʠЩǽԀωӧĕɹ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165048.527039:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȱɻκгǁϋÏў',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'pҪʨ˘НńЖǵȷ\x9aɀ÷ϮѾѹɪ>śžû^ƙɓ\x8b˒ǁԜ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ZRƭҏξϭӦˆÚĢʓÙӈωɎr',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ŨƄ\x86ǴȳʹſΊӉǭƾˈΟŭɈтҍǽɨɠǠӉǦƃƅ,Ƴĕͺξ',
                            'message': 'ӝԘʫΣѳѩ҈ŧʰİɜϡsȯï\x9a!ƍbģԁȿӵǬʄҰǣ˻ӵϔ',
                            'arguments': [
                                        {
                                                        'name': 'ʶŘкƅÃëеГJ˂Ǌʬ²І˺ʿдş;Ĥ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3065179366781709411,
                                                                        },
                                                    },
                                        {
                                                        'name': '˜·ԄжĕÇÍѹCҵZǿєӷƬʏ\u0383ȎˡǴƎфɊԕҫȾnqĘΪ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˘ϕĠɳɇ§ÆЧˀД',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'χʈĮØѣHΫƒ+Ǎ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'AЊ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѽҵӾƭÞ%\x82ƽL˽ývćʻϫ½ɕ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǿι˸ǜ҆ɜҝ\u0382ˈѥʩϴ`ɅƞϋѶEäĪҔÙ5äþйĳǎʁĐ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 602352.9761506813,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʹjΚҕ°Ȳé',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˏǲѩεĭ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '/ǏΖЙƽǅȲƸΠȏǧϼхȩðώщ-ćƚČѦӊρ*ƒ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165048.532068:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '¤ѐȮӑɷîҕ\x90ύǧğ\x9eɻƱ"ʹǅĠҷý\x98ƓdĄªĺɺЖΗʓ',
                            'message': '҂ǬĘ\x9aˏѦʓƯÝǖǧųŧОҎƃǜƢIʌā\u038bʨͰǮϟΗɮԦȑ',
                            'arguments': [
                                        {
                                                        'name': 'ɣǿʉɩϰʃԆңΈˍ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȣϫ˟eʔҗ)ɘʉƾʻɄʤñь¥Ӓ÷ē*ɢ·ēƁ4',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¦Һǆʟ\x84Ǵτź\u0381АʱǄȆѦƜeƿгʔ¢ϒπɥхο˻ӀǑǻϰ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ũħĿ·Ũ>ϔϋ҅ԅԀ\xa0\x94ˎƸŹңñҺǗˤ\x82Фê\x8dπěÉАɾ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϋÜ7ȧŨoԮӷѻ˒ŚÙřαԍ˥ӺΎϟȰˤʍŚ\x8aǑʩȉJƸś',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ћͷŔ҂ͱ˅ˣʃ˜Δ˴Ǔ¬;ÕįƕҧԑȞŔǈŠƧӪôʥпȈ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӤӭȋЫϥΔ·Ǿ˩V*ΧŌ×˅źԫʇǏɊҪ¢ɋȆ$ԤAïʐŗ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɽʿƷ8еŷϺȬĪ²ԭΕϏЛήǷƞȵ>/сfÜѺí-¨šƤɳ',
                            'message': 'ϝфјǑʤƃ҆\x8eʑů˺Л§ӗǛʉ˘\x8fÉ˙ϸӇΨˈƾɔɰŲŪʏ',
                            'arguments': [
                                        {
                                                        'name': 'Ĥ˰ːћʘȴӗɛɹ)ŐwǢţəřƾ¡ќ#ϭѠ÷ӌγӇɎ¡ǵ8',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ө»ӧӧ˱Ʋ\x96ǔο4ҁ҇ÌιɄʘɿ&ȋeǔЮȻΟťɔ\x8cѺѪʞ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˍ+҂ǾЕӭӉ˜јƏʦ\x92Оʹˬ2',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȂѳϘ˺εťŢ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĸŅĈΘİԖÎǘϟψX\u0383¿èχ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165048.538356:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˻\x8aȻ\x9e¶ȗЬǇτ¤×ЗUʻǮӃɿĘGʴƠʾԐûƿϕɏƏԌӐ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 764895.0488825816,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԓÏриǻʷĪϘɶȯŵǉȀАȧ2ѨēǩӔХ¼ɵ˫˅ǡЊ]ӈҕ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 725368.7764046646,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ξē!ŷ\u0378ĈЎҳāћ҄ҴЀ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ZДȕҫʩɄùΘȜǴľǐċӒӀ˖ěĦΟɦһңі-ԈήŦθϝѼ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ºˉħ˚ÓοĀ&ʰЄŏϙɔҝˢѬŴ\x83ɝѝĵԝȘ˼ӚѾʎȠ˩Ԫ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -2659.209219013952,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƫ»ħ˭ºȨ\x8aΩAȜτΓӢЊԆͱ\x96˂\u038bžȶɓƦŝHǻМǽѭѸ',
                            'message': 'ӝ\x83ɲԚ;ȒǓБZ˽öΜ§ŊԀұΰǚưϱӲŘdùGôɃĎѰҳ',
                            'arguments': [
                                        {
                                                        'name': 'Ũ˜ɻгѾЙǜþRЉЅǣӻ˃ £ЭǊΊ|\x8aƍȄϙԈʫҽaЧɜ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϜRԏ\x92ŻѤϔ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĕ\u038dҦŚπ˶~ο˖',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165048.540622:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӐŏɊțƼ҅ЯЦͿѰƵ¨όʧҮψѦ\u038bɈ¯ζ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Μυŭџ!ԛҁ˶ʇϪƹҾѐѫȏșάʺӳþ\x97åͻɨɓ˴¶f?Κ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'w\u0379Ð\x9bνԝȰԇRƎҧ˦ʂȶ½ȧØЖɎWҏΡƼÓҀκӉęʉǸ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΐǁєʭ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8851067028706713039,
                                                                        },
                                                    },
                                        {
                                                        'name': 'б÷Țѧ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĖҵǋѽԓюԢϾè@ϓ.Єη\x90шÖȑρ϶(ҤƧǯϻѧвȂÆ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƞòԞԅѽϭ>ƅ\x80ȬФ¨ǋȫΔǞ˂ρζʤʪļɺ÷Þˮӳ-˒³',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5045604556708189939,
                                                                        },
                                                    },
                                        {
                                                        'name': 'űѕƩʞmξҪχςůűQԥͺԌ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7295423068902028264,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΪƀþɞȀɻÖϵwƊ¥вɨŃΡϿŽɧǐåҀŒͷԍǃɕҧɐВɤ',
                            'message': 'ŅΜԍҡɑЩǙ˽zԔGɞčˠŪɔȲȪnΡΕԠҿŞÑƜĊĳǞҠ',
                            'arguments': [
                                        {
                                                        'name': '¹',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҵԇӽ*ǭlǻȎè\x90ҭȟžƖňŜьɦƮΥǲѫĪȡłԀɟɥȤѽ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165048.542267:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƅɯҾʁȧàȖ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΩΖԄŵӵʊˈΗϒҼ\x84ƪНɇʨ/ϫҰɩ\u0382˱ŀҪ\u0382}˺þȥЄҬ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˋŮǠΐЉαƐΝԮ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Θȱ\x97Ρʙ˵ӰlǼ%ŉǡςъҊŮӗΒˢɋ˔ìѬ¹Ǖ˛jЉſ°',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɄͱҺ\x81ĞΫ˕ʈʇΑǠǔϮUϸŘ\x8c\x93ɇ{',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɉ+ǟБɡ¥üčFԭϝӜɞӿȳƐƜ·ϥŪƴýȹɇΎƕ˳Ì/ҳ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȌɖǖɅ¥ĥŅ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 582429.0130803236,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʖƣƋҥ\x9dŃ\x87ɅĢϑĶҧȆӼʑԢÐ˯ĻРˏɸӇԇɋħ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȨOҕȭʙYєюǩҼ«ËʺĢμ9ŁҬĒÛѨԀÀȭŦƍΈoˬӿ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210212:165048.543559:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'CҳɢȦϱҲ˞ȟоĖÑ£ͽ˯Ζ҂ʰʓ\x8fϲɟʘҳϵɍϢơėŁƯ',
                            'message': 'ƤϱʛSϊÁ\x85ŞΆ;ȈН:ɶʍ¯΅˺¥ѲΣҔɇӾԦ·к˦ƌс',
                            'arguments': [
                                        {
                                                        'name': '˯ϨʇƑŞsΌΫʙԭЈҥ4ʯɋ˔ÊƹȜąȈҦΡÚϬŭɢӀÑ¢',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 480147.09694063256,
                                                                        },
                                                    },
                                        {
                                                        'name': 'āØЀӓ\x93ҏƋ¿ǇeүCӀʬȽǗƂэ\u0378żӶĹĿҳĜJ´Žӂˢ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ƭ¯ӝ',

            'error': {
                'identifier': 'ЛăȀĶĆ',
                'categories': [
                    'internal',
                ],
                'messages': [
                    {
                            'catalog': 'ΫǴ',
                            'message': 'Ӭ',
                        },
                ],
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
            'name': 'ŮІӓǄĭȥГĬī',
            'version': [
                -303588537910326886,
                -124043989099995785,
                -1110730119208884003,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ϣОң',

            'version': [
                -2453378628838072793,
                -7333767950841155758,
                -6537565673880450204,
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
            'event_id': '\x8dѼĴýӰʻҶNίФϊӏ¥\x9fӝmƖНįҖʁuʼșԅœ;˺Ӯж',
            'target_id': '%ҋgƃ»őlǬĜ',
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
                    'event_id': "Ɖ/ϔȆЊɢěɁПεą'ϠǎżäǟªŇуӾűԫ?ĈҨԓӛ§Ċ",
                    'target_id': '϶΅ĥϼ˔ǘñǵƇĻf҈Áʺ\u0381ѲŽǢШʢ˼пȂĀ˳ЩćÉ\u03a2Ĩ',
                },
                {
                    'event_id': 'њ\x88ϤˤɱʳґκèɆăÃłϏӕӷԫ\x85ÒЈ¦ӊ˲ԏ϶ԓ_ϲɇх',
                    'target_id': 'ҝwеͰʩЛµƮČӸ$АЗØŉøƜƂ7ЏʶÞѺðѝɂĸǍˈC',
                },
                {
                    'event_id': '˴щɿkҩŝs\x98šԛхǖ\x92ʖ҈ЦӡχϠ0ϥʷ҅yɜЩʺȉӁϽ',
                    'target_id': 'Ÿ˒ÓƧЯä˱дCИʁξȎȁКɅȚȄβӴĝǑѱ\x9dɃɧţɀæþ',
                },
                {
                    'event_id': 'ҜƆҡÎƦǢ҃ɅҫuČŬӶӯÍͷǜӔ˽\x8bΔȞλƳӪnǆǾɆ\x91',
                    'target_id': 'ԃϘɐҐŽċȋӺȂŇtѠcĶӠæúԫĎюƟúҚPß²_ˆѴŤ',
                },
                {
                    'event_id': 'ԈόΒԓпĕЏΩҙëлʃȎ%ѦԈ\u0380˽ї΄ƇӠEѺőLΡȞťÍ',
                    'target_id': '˕ìʮԈŞÞԣŋԀʰĘʶх¨űɽˆьѦ¢ҮѬœëԣӣNȔЮ',
                },
                {
                    'event_id': 'Ԓҝǌӥ˧ȮśǗξϋŝѲɠʟП˘ӻϓƆџmАÉȊyƄбåϔǞ',
                    'target_id': 'NїΌƧƷĒ\x88ºȖŃlӀӀѓĩȇӧ˭ĥöˉҕкŶδίǵǚԜ«',
                },
                {
                    'event_id': 'ãЮɱŎ˜ϊλХԋԠHƤˤώʦƄѫѢɎӍĤԏɦαǷțÌӕЕʹ',
                    'target_id': 'ϾTʢʹӡçҔŵkөχҕɼ4\x9aΜÀӈΙϐҷI\x98ȟʵеӇδьѷ',
                },
                {
                    'event_id': 'ƢЧʈ÷ĐҕʹōїØӁŢҽϕìʝȶzÛmŪĖȻʪӋҢȰҵˮś',
                    'target_id': 'џӗŮԕʈM\u0381ԟɧӾʦϐ˥ϟǶөϋϫ˲ӸШӏʴήӄΔĹӋӘɛ',
                },
                {
                    'event_id': 'b¸πƦ2ȔΔӌӔǔ\u038bğͲԏ\x9dӟd\x8eơԧ˩Ǹñ\x82×ÃԦέțʏ',
                    'target_id': 'ˣүOƺơӘΨЀĪӼŦmˁÄӥÃϻˤѝ@ıɐǺ҃\x89Ȧˉѯӽϳ',
                },
                {
                    'event_id': 'ԈЏ#+ΓȕžǸ:\x83bǠЮǪǕśҺ*ŃǗԄ\x84œȧИƲφѾŪö',
                    'target_id': 'Џ¹¥ǉѦȄćȺ¬ɵǊĮú¤ʒƍά:¤ĲȻwŕːÖЌχØͺľ',
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
                    'event_id': '˨ƦȿȠІлϔĺîФǅĿ\x88ԮÁЌΎ˲Ñ4чÅϧƖеɾɚōȪҿ',
                    'target_id': 'ϴљѼʩƶŚȩΕʽҀ˲˒ȄƯƩοҠĉѯȇȿԦŅӰ˭дȲԉöӃ',
                },
                {
                    'event_id': 'òѰφȠЃŌΒҝѬƎ\u038bԞʭ¡ӽ-ԩˬʸѪÓˋѥўǳ\x90ɲѴҭΉ',
                    'target_id': 'ЬťhЬҜȥɯʧʌЁұTЏĤ҄ҳзҋpʯΞɐǇTβƒԥʳэԤ',
                },
                {
                    'event_id': 'ȚрȠýȣȮEΣпºΜʨĘÜЗ!6"ԝƞκ˞ˊʣΔǓýOŌԕ',
                    'target_id': '\x9aè˾άτӐІķËƗУɔȂҌwēʚ¬πɌ˂ƆƟ3ÆȚΏZ\u0381Ã',
                },
                {
                    'event_id': '˸ΨϡџɛєќϚ˯ěǶιͼӷϥCЏʻŒä˼ōǾѮȒҟ˵-Ѷ˘',
                    'target_id': 'ȐˢǉԂϛÿЭɰUɧŚ¯ʞΥԉӮˌ˰Ҍ·ЋŻùøǖȘ˽ͳ҇Ɏ',
                },
                {
                    'event_id': 'ƘțҪʒśжӲkӨѹ±ŹǽǞκƉĞ»ҝʩҽj\x87ƭǷѵȼԃЈк',
                    'target_id': 'ȸΈĈдȘƙӟ\x8fdËƙ5ĜѠΰɒɓԅΧԗŵ\x81Е?ʃȅӹ¤ţӬ',
                },
                {
                    'event_id': 'ʍӲZґ4˞Ì6ɦK£ʱđԡѯůƞƤ\x89ɃǬҢČŶԙаȋ˖˛ˢ',
                    'target_id': 'τс¼ͱ˽ȘƦìϨžƆ\u038bԢԝ¶ƈ´Ɠơȁ¸˄čńȗɩϯԡzœ',
                },
                {
                    'event_id': 'Ϲů͵Ρȷ}zɶҒӰŜԞΝυ\x9f˦ɚȷȭўυѮöϊǏǷTԂӰè',
                    'target_id': '\x8bcР˙ȅѽɳȁеȒĳoˈʑҫçǚɰӼӟɶ˵фԄʓ¹ęԜăŰ',
                },
                {
                    'event_id': 'ǣ×ĭͱʬԤюƮэšDĥŘɨjӕËȭɩʭҒ¼UӝȊoɧ˻ғҤ',
                    'target_id': 'ҝȍϜћȮɝĬƎȲҝ8ȹó©ǀҒАљŧ˰4Πìυѻ˟ǈʵ\u0378΅',
                },
                {
                    'event_id': 'ŇõƉǳӈĹʞ»Ǆųɛөŕƶñ˦БɽŝҜѷкϕ!Л\x9c\x94ŝ\x94З',
                    'target_id': 'ʌʔ\u0382ѴԋӊоɞФ¹ɏЖѲϡԬǘ@$>н˾ѕˀӤӿȎʯͿƳԦ',
                },
                {
                    'event_id': 'ȡȹηơ˗pѓ\x99Ȃ΅ƜɥѨǗʳȻώЭӃϽü˲©B×ƺě˰ƚϽ',
                    'target_id': 'ЕǪϣǰκ҈ԁ\x80ɟπԠĥʵýΥЁ˙ʦRƶƌĄɩCұȱɿďɝo',
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
            'name': '΄ԆFϬÉ1CӴԠŻzôiȥјħǷω|ЎɏȑňɌFƒԠӝāΆ',
            'version': [
                -1548133421853813502,
                -3020008749394123286,
                -4995083762648315189,
            ],
            'about': 'ȑΠķŒΘʢʷӻɀΘşΞ#ǆǜξȅ͵·)АàĩбƩ˦żƤĐΖ',
            'description': 'ƅѦБ\x80ʕΈԀåҔȀљӉ˄ïįĔΖԄDƔʉ˹ǭӣƙÎƋ˅Łэ',
            'authors': [
                'ðƠЕӇčқɄĪʫǡͼƶжӃϪğävԤs!αŐŗıűėÜ\x8eͶ',
                'ˀϓɵɎ-˳ҩΦĊ´ȆιɐıƹĽŦѴȫɳSńЪƾVʀ˔ÒôŊ',
                'ФĨπ¢˽άȃ!Ӑſ',
                'ƓĵǉһюӢ\u038d˪ѮϝǿϐǣρϰԀ\x98ψϯVҫУѸ{Τω\x8bįˮƄ',
                'ȗӘǉˍƖƓş°ɴҠžǟрȀÿͷЕѨɛџÅǔ§ӆаŗʾϮąЖ',
                'ǞʪзÉ\u0378ӖƾºƓʀºюÚЭƥõҺ˭ƹ˟ëУͳƾѸ£\x81ͶUÀ',
                'ĩ˟ήɚʚӼ\u038dȲĿё4wѩǱƪɣĒϊŞʄʣèɬÍȘĔţǗІҸ',
                'ԏѽƙʩūћθѪӱʬȫĦҋσӗȶƻг˄ΪɐӁӼΡ\x95·і˼hǂ',
                'Í\x86џ\x9c×˓ПѡԝǀMƌûãͿçȇǠǳè˻ѠzšȏћƐЉȞƠ',
                'ǾУƁƼɄņϏTÚӾΈӶĸѺűĖԭ4ǐ\u0383ŦȢҡԡяċζϩʐώ',
            ],
            'licenses': [
                'ϲеҤΎ˯ΕȜЄǦɌùƓԐДǔϯóšƭЙW·ѠŎѯӒÍ\xadӛҥ',
                '³ѡϋß˛ƸáʿЉ½ǋȿcĿ˄ЗӍϐ)ţƕϥԋGŜұфӼƹΗ',
                'čΰŦ\xa0áŖ˃Ώͳ҄ҸÂԅ˸˚ȈσРτʁѻǍǑ]ϯpмα˘ʕ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʳϙɞ',

            'version': [
                -194168013266913952,
                -1365521498865726938,
                -2722716973388645873,
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
                    'name': 'hĴȈ\xa0ɘĒӬ-ϸΈTћͿĝɊŗȾŮԑƒJƂɄȏĎЃ«ɿ\u0381˜',
                    'version': [
                            -7020659174189354619,
                            -2799485723114733929,
                            -7442455728110213142,
                        ],
                    'about': '¡ɩÕϨԝϞĳļ÷ĠzÏŚϗѐŸΊ?ѻЇKĮхԟ0Ԡ҆ɰӷȎ',
                    'description': 'Âǽ"ΒȪuŗƇK®σΙ\x92ˎɉԊ)\u0382ĒǃŝӿǤԥɓîȞÈƂ³',
                    'authors': [
                            'ĩ˙ɺΣʫ˓ʥҁΧƁ;ЩӀÙҘμŽʚĹȣԥˣLИ\x7fмΗӑͶҸ',
                            'ÒɢϔϗȵΡΚǮĳ\x9bɬưδѼȆΩCȔ˴ϛӦө˗Q˖ΰǼȉʈǺ',
                            'ɉɫȸˍTƋϾӓĤ;ǻΔɈюӼ\x83ɻѰΣ²ҹѥИƝ·ӠʝϩȄ~',
                            'ҁҶжҿΘĔ˚3ƧZƝȈ˺кŋуſ÷ԚÎ˴ǮɛөĜĞɦȇӷN',
                            '`ȁӻώȗǁ˲ҶǇʝǵø·þɏ$ӂԀҽѨӜϗ¼ϼĻʨvӀĩʅ',
                            'ďȌ9ϏԚ-ǷҎӄ£Ģӑΰ϶ΥƁ\x87ҰϮϙɕˁʱÏǀ҂ʙϠ-Ʊ',
                            'ӚɝϮʗ¥ԊϭƛǧВ3Ĳҡö¾ʑ϶ĺŃʑ˸ѳЀʱţɉӢȝȉ҃',
                            'ĘԟʿЀ\u0382дӓϦǔAυʭЧÍòƩϏŘ¬ũκǻˣмqϵӣɥ҃½',
                            'ԕɪόôĤɏЈWŽŢѩɀѣəâǘҮŵҤ2ҐˢκΆȕ҂ϵȣѤЌ',
                            'ӤɫŚѤȯ˴kϢ',
                        ],
                    'licenses': [
                            'RѢҚɆϾĆÚͳƶ:ĆԅŭŅАΞяΓТӲʞĝӇ¨ԛ¾ʬʘͲʄ',
                            'ű\x84²ÙǟθǙʘˀƻωϴɑΏǐƤϑƟƴʛԟşӅЯѲљũԑɌƇ',
                            'ʁԠ%ǢɌӗȲȚпԔȷĂȆ˧ʳƭɬʡŜԣİъԘ\x90ǔϘŒԔJɩ',
                            'ӝ9ȄԏγɑOıҪĥĂìAʴ½ΦæǊӥчƚȅӳ˚\x8atҶņȼѳ',
                            'ʾǄœӡ@ѺҖʊȞӞϜ\x9dçʋʟ҃\\ƢӼŵʺӢɀӚмŃΣ˥ǆÒ',
                        ],
                },
                {
                    'name': 'ȿȷ˭éԩӨŻ½ʨȰԡƦlɓ\xa0ǵþɝҊʹŶɎ\u03a2ÎʀіΦŭфШ',
                    'version': [
                            -2846719232419829169,
                            -6059927656060536779,
                            -4241947336104874746,
                        ],
                    'about': 'ĪˢțЩϋʵ(ůΌΜɌĖǄ-ɳ÷ɅǳӹáϘÞř˨άЁBķȴҥ',
                    'description': 'όТȢ×ҎƼΰ\xa0ɭĈҘв§ǟʫ\x97Ʃѯ_˱пɏѕͰЃœǗƩӽ\x8a',
                    'authors': [
                            'Ή¦ϖԎ\x85ӟοϭ΅ӣƻƔ^ƽˈϺʘҎȪ8ʺčРΣ{ҒцŴƋї',
                            'ž2ʋԤԋõǥԇ˛ʹщыƵÔΟˌʐƤāӮΏԂKĎ˸rƱ˜ΞD',
                            'ѐř˪Ϥʵ˩ˑƲӂԙϘȡƃʉҵbҫҲÿǟӅ҉ѸҼҫÅʴфɑϭ',
                            '\u0382?μȏѝ,ʻɬ®Ɔѷ˛İӕǱϗчӒɛȁӓʥ҄ʢȣМЎŨнӏ',
                            'ЙÆԭǕɃóȓņη|ҪΪϡġѶȘӼ8ΉɏңoæñґňӝƥШä',
                            'šǴӱȳʽÏĀѨˑ÷ăɻȐǩʬ\x92TȪϘҨʅȹҠ"ɱȃԟԌfǬ',
                            'ӁӣСӖΰιļɈnǀvΎŌԥǮϜӳИȠĐ\xa0ϮЋжъΑɗЄſę',
                            'ȋō)\x82xȁԚҴΔʮҐ˖ɽΞáUňģʇϪȝ\x92ƔʠǄӤͻϕŠԎ',
                            'ƇѧѪϷɥŤĄʟҺʉĶњĝtҕɠОК˰ǽɡ³ӻӘȼŕeЅƆŧ',
                            'ΡβȮάčʱʸЩθǾ\x8eþ\u0383ƗӢȷƻӰФŝ4қƽеΆļğӿƢΆ',
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': 'Ϛ.˛űɥVŦͺП\x9bέMȂRȹ҃œΤæҸϫȉҩҙǰӔӥΕǸ\x85',
                    'version': [
                            -1916463065646865934,
                            -5485638992071960500,
                            -1333428835697454813,
                        ],
                    'about': 'ɚЊƣХąӕΊŽΩÚΉЊμϝӧηŚЁ^ϢĥӪǤÜŷҖʻǇ˳',
                    'description': 'jŠțѰŁ\u0382ɛşԨȫ¢ɵɞѪӑħĹ\u0383ѠŀҴԠ>°ĝȆƖ˂ӪР',
                    'authors': [
                            'ɁФԏԜ϶ʝɛʟ˙ȏω¡ǆԎΰƖӛлř˭n\x99Ҷɉ\x88ŉʑϋϴƳ',
                            'əɜҨ˩cҬǜȣΧΏˏÑʸƼŻΰӸɺJɩϲ\x9eГаʈӂ²Ǹ˴¹',
                            ')ðюϴОӈ\u03a2\x9dΐđԗӫӅǒŜØ&Ǿ',
                            '¼ʿ˭˅ђ˩ˊ\u038bşϳԒϲƆђǗÈѹѪϕԑӃјɶӲşʽʘӴɗú',
                            'Λ6Ĭ˷\x89ѐˊͳǁΙӛƨkȈѲџЁ2d0¹\x96үªţшĲƗˣ$',
                            'ϱӒѧнÀ\x94ŁĊǙOВɲхpЪMўȼĬαǟĖϛîĊҮ¡Ėǝκ',
                            'ːŴƃϿӣʙεɮ¼ƈùǰҸɻћȤŃǤɃTaƢ',
                            'ϫʶȪųĶÒëͿҧҺδЙχƸ\x8eÆǳΞˠƱÖˠǸԞʑÐї®ɌĘ',
                            'FʙӜDǂƟɁıÐҌɜzɏcŐƼϼɲqɕЯϏɁȥЯϢÁY\x89\x7f',
                            'Ðǁˇ\u038dǙҰʰʕgÀƈʼħŔÌõRѩЫ\x83e\x8fɲӶƶˏ,Ƽΐі',
                        ],
                    'licenses': [
                            'Ӯ͵ȐҾɡȖİƎ҈O/*˞ү',
                        ],
                },
                {
                    'name': 'ħҰԦďԜǒɲńßӦԮ҇ˈŷƪƬɑǼҪӄʃô҂ӃʕŘώƹƟ\u0382',
                    'version': [
                            -458540071268125824,
                            -1517346014468049349,
                            -8006338551941669416,
                        ],
                    'about': 'Ĥȯίǣɾ\x89ʟϱäҝ¦',
                    'description': 'ÔŌҷӆĖԕ\x93ҎЁĹѰľԚ-ӍǊƓ\x8dĻӦϓȰϏώ\xadԈΨçŧő',
                    'authors': [
                            'ϊӀɚϤǍȝѴąČěėі%τʓ˞ıɋȌԚǕѲĎьmʁӊūϋӄ',
                            'ŷˇɅѠϔîφӖr\x8aΏтύīϵVïōҚвƻȐљĲĮӓWë˩ż',
                            'ü˥МҠјЊɢϡҔԍцȺνҚψˤĀʯΞǁĎҰѓ¯Ҹжp&šˑ',
                            'ґŨȉаµȄǫγϦʥŢCн˗ҮԃϊGB¹ӷǉǱǚˊ/ʫаȁŶ',
                            '£ӑѣ˛ѴԣγŨRǒͱοΩ\x8b;ūÁԐѸˬҗĘɘԐʣǤҊЕ$Ƀ',
                            'ҖоҰĸЏ´˽ǎҲ*ƫɭЎǮјӐΜѢőҾːҷαЎϯʷƢǌɿǢ',
                            'μÊčʮǖŮvӱ͵ӐɽІĐě\xadƱňˏŬɌͶĩ2ȲķΨ+ԟ҉Ü',
                            'ҪDдμáІɯõºĚԗϡϋǔć¼ȟΤҊ;ƂþńӈȕǼɿΚΦk',
                            'Ԙl«ϭȭҼʬǈɁǂŅÖę˪ΛĻw¼ǧƸȻҁĳ',
                            'ʷωο˭яǲȥыʜß»ѩӧƪϭȵҙʇԦʁ½Ԅ±ӏԕ˻ѣΑ˵¾',
                        ],
                    'licenses': [
                            'ˎŞȶǓϸaƪӎҶԕ2ǆƐƲΟˡĀϙҷЍϲôӺҎϺƩѤȺÖ\x99',
                        ],
                },
                {
                    'name': 'ӔěÇʽķυȒªСƶĝӠΌѪΈʋŬԛǦƧvaЬƏƊ~ȘȬÂӄ',
                    'version': [
                            -9160302621681100836,
                            -5947094289238603008,
                            -6086539294477843164,
                        ],
                    'about': 'в\x80҄ϭÄİӐǗс\x8f\u0380ήԜ˼Ԡуɭ˘|ԁĂҪқθʰИӗ҉ǡЂ',
                    'description': 'ЊƇë\x8c\\\x8cɕʘӬӦӹԭº\x85ІĨǜӲҙˇȽ\x8cȗйѦɔЊɥ·Ӽ',
                    'authors': [
                            'ӇɾԆǡѠ×ӱĤΝҋҪŝӫΦſ\x82ĦʸjҞԐǼǠťɶѳҤЄǿƥ',
                            'КοÞԢѿұϾÕņb҅±4УιcӨѥʠmĤԠЈ\x97ӫ»Dˌŀƶ',
                            '±Νő½űþÇɐʉσŲԂϞʮŏģƘ»ŇѫŃ^ċ?ǊpǣөÇŶ',
                            'ǊǙǄǺĂĨ·ӱиъˋƥ\x91ͻǘБgȄЍŀΡɠѸЗΨƔĵƢѴǭ',
                            'Ƣö+ϵѲϫĢČϏƗʲÓ?Ӥ#ҝˬʊŻ˹ĸͱǎɷȅх`Сˢà',
                            'ЎźȣÜĈŜ\x84RÜӣƏѪѭÚƜΡКҗζ\u0382\x8aώЊŋëўȲ˶Ͼɒ',
                            'IȗԗϜЭʌɬÓ҆ÑÞȶȨɾͷ;ʝȮҢ»βH°yľɐÜгҥԏ',
                            'ɳҙ\x81сѵԝңԑȼ˷ïδƈӓ΄ʍ-ˠфĻʄ×SʖúόǠȃʓѸ',
                            'ԗήv2ßǌΨ\x90ͼǧϖѰ˒ӶѡʭġľŇˀЁԄ\x9dš',
                            '\u0381üɯ҈½˳фΙэ=Д˜ŇDƇԙЎςԪҖѡɠͰ\x91\x82¥ȕ3ϳ\u0381',
                        ],
                    'licenses': [
                            'Ԗ|[\u0381ÛҔ¤ǈԑҸĺʁŲǇϴʴpųʕʗӾΨPȣʫΧΜҿ\xa0·',
                            'ǉԞπŐɝОʮҳàʵχԥуѝђѿђȑʈèÁȻȃЏԓƆǁӊ˯ƕ',
                            'ӊĉƧШԔȝӾԍĂӭԐϖbǊ£ϷύΛҬԛΆ˄˴ʋƎΈӅл\\ͽ',
                            'ʕ\x87ɒɑҠAáèƳĽʍĒʽƼ0тȉЎҸш_ʨʝűΆВɶĝPb',
                            'ӏɱșĘɮӱӒZβŻʔҙѵ҉¥ԏΣƧÍʓ˘/ŲeϭΏɴѥԑA',
                            '[¸ǁĺΒЕȑ¯\x88Вı|ÊƭǗѳЀѸЀϬѵůɀҼøˏɃßʪƚ',
                            'ԍÅ˦ϥΟôї\x87ѵȷßæԞ¦ǅθɾFƷ\x97ˡйMҟɷxʿ+nƀ',
                            'ԓĳƱŭ$ďɛĊƼƨȘƥXǘԦ¦"Ǫ˫ŽȳĒЯЃԊťĎЀŀѳ',
                            'Ïӊ\xa0ĭƁ"Čųβɜǖ[ơ}ɘǛǔм<˥ʌȳƹʲԉɤԏƵʝƄ',
                        ],
                },
                {
                    'name': 'ͱҹǔwіƝȼȓȭԬ´ɸ)ΞГҘųİΙӞǞϑȟʰΖκŊӡÄҏ',
                    'version': [
                            -3559300085916350191,
                            -8352812810811408772,
                            -311540800208419247,
                        ],
                    'about': 'ƺԭˍҦäƞĻѡŕ҉~õ[ύāαҢ\x8aÎǀîҎϪ«®ƥԡɫPƒ',
                    'description': '\x9fʚèʣëϧЬѮÜęíǆvŅŉ\x87Ɋνĥ°ΕĞͷķӉ©ԃűњ\xa0',
                    'authors': [
                            '/ʤǤԠͰȍϯ\x87ӇѨ6ƧϽəӸƳȻ\x98ćήǵĉ»´ȠıϯώѭŒ',
                            'ʁӧЄɃϱɓԛëрʕĂ6ӹ½ЎĖɧ]˘ŭɜɠӶƞŨйAáϳǂ',
                            '϶ɑ˭xҤҾϫϡŪ҄ǶȶŤŅŊɰǯǼAϽňșυэĽʰΗ,Ϙԍ',
                            'ŤΡѼ\u038bɫȟљȏєĘǢȯшAżӾ˅Ѧʊŵѱơʘ¤ϐťƽɒɨŸ',
                        ],
                    'licenses': [
                            'Ʀɤǰӌ˒ѵȴҹǆӾȍū\u03a2ҭѬĻҖBӖɛЊΛһƷŲʚûÒѨϖ',
                            'ǔЦжԇ\x97sʗ$ϠȡЮƊχѐψȋ\x80˞ŧķɕԭθуºηKԐŒυ',
                            'Ӽ˛ѡĶҙѶĶǼɢБʹԏ˪ʫǺσɸӘRҦ҃ʇҔöƕӸ¦ʎƔГ',
                            'Gӿρͼfу˭ΛȺȗƿĹҪʐԭú˞ȎŹӀԅŵˀ\u03a2ˣҢÚ4щƙ',
                            'ƒķßҼ˥ȑ2ј˷ÍЈѽĻѫΗϥʆ2\x98ĎƟΛȵїб Ѓʣӯͺ',
                            'ΏϹѿŊŇьԇЉ*ɍɋԇ]ҖЈӃʉҠąDϑʄ¤оԖȌƶʱ°ӕ',
                            'ҕМϻԀE\x98ԐǟǀҐͷӽƈбάĭ҅уѼ˕ҥč\u0383Ę²ô\x86©ΜӇ',
                            'ǭˣɔŹв\x97ϙːƩǒÛѱʡӝ˼ɢ҈Ҝʬɽ¦ǫДϋˆҜҐЩϒÖ',
                        ],
                },
                {
                    'name': 'ҰιúԆâΥŶ˺ȍӜʜɉ˅1ǃɉϲӓhƏ§ɦύǷѦīŗŅϢ˽',
                    'version': [
                            -2270732302014238644,
                            -5217836955903671827,
                            -3490458402353307904,
                        ],
                    'about': 'śΕҌωΎ"UΓЉũ˛ЬȱˋlоȷšѮŭϡȂҾΐĀ˒Ӵ°ɡ½',
                    'description': 'ȍ˔҆˴ɰĄђ²<\u0382ŉ҉ţџϴÅͰӇƒёЇ<Ҡŷ"\x9cɩÖВӛ',
                    'authors': [
                            'ɞɏϡ˭φiǊŔϚδfʫÈóț\x91ɧɿɀϗgпӝöŧΤǟǃӢĦ',
                            'Ԩ˽Ȩ;Ȩ(ӟɈӟ\xa0\x99\x90ʽӎЄЭ˜ґǆ˨ɷƔγйɥͼԧȤĜǄ',
                            'ʮҼǟ%\x8eưǖœҔÒHŝŪôȂҬрϴgӖиłӋͱ˙ӏľĝԃǑ',
                            'ģəĂϺˎŊǹӖʺĈƏB@\\ԋ\xa0)ɥϩԨś\x89ĞһӯľʭĐʁԗ',
                            'ӻԂɗÞÉÅéдÿˉʖҘ˸ОҼϜ)ƳϝˀΌέ˨ϫſ˝ÜӉ˱r',
                            'eȣёĜM\u03a2ŲʰȾŜҋ҂UɲțƍɀǲĠμҏKĞ\x90\x8fʣˠɘЧе',
                            'ǶʠԂςӖěΥРǧ\x9fɕΤҵƿ˄ƛR˫ɉǓɧÔȀˑҚįʨɽʁ\x7f',
                            'Ǝˮ˩ÏʃʼτЯϹýιΖұЯˀπцUʊōҐǺ.ǈĘˡƷ}ɨѦ',
                            'ÿѼ^Ρпӎю¥Ʒоʈ\x85ŒʣǊƌΛ\u038dɛҰ0æǬЎӍƷɺԈƞ΄',
                            'ϰɷďʌтʏӰȋɯˍ3ҾEȢ#ɹӍ\x96Эч҄\xadśʜ˭ȖŋƘ˛Ǹ',
                        ],
                    'licenses': [
                            'Ƶϩ˂Ɔļ\u0379łǮĝųʳƃǮΆʿǅ˅ƱʂиЊǳ¨ɳ҂eʌ˂ɗɚ',
                            'aųӮŷ\x9eΪȱ˳˚«ЙΡӱ@ǖʸЬ',
                            'ϰʬȉϤȈǽЀϫȂǵΙȵҺʃáͺIˏȟǹЫϟдȡĎѣЀ³ãƼ',
                            'ǃϘɆʚńψȗϣҬ¬ѷ`\x91ɺΛŏӬ`͵˸ĹʺɦӓͰ\x94ʪǒƒɶ',
                        ],
                },
                {
                    'name': 'ЏσuӰ˨òĠ˩Ðˮ\x90ǢЋʘȫПZưΉ\x87¼ɲӂҍżуȜѦҶN',
                    'version': [
                            -4167649856591522763,
                            -8965828884074588790,
                            -2093468247336349317,
                        ],
                    'about': 'ȹӖǽŋǹ˓ʅ\x99øĎΐԉѤâ¹!ɐlʱ˪˪ϨӥӳŭЪӛϊԣѢ',
                    'description': 'ΏɰâƗѤŌɧ2˥\x93ʔςʘмĭʒσūȾȧiӷфǦƐΉD˾Ӕˏ',
                    'authors': [
                            ';^϶ЧŌzӇґżƶBɘǏ»±СђѪяʿ{ǱņϞ+ʊGŠȯņ',
                            'ΠkÁͿɁȫ\x82ͽɝǘЉѼӹq˩әҙXӀĈ%ӠzͰtЖƫȫЦ˒',
                            'Ƀʡuˁԏ/ȉƤƿ˃ѩƿүřàƴӥЗ˄ӎ±´˥åĞѰƢɼϊĻ',
                            'ԙ҇ÙЭӲ˺ѠɟŎĿ˦ѤϟӝƓг·°ϊ«΅ɢªϨԗŶϣĢԋʪ',
                            'Ƀ¿ÙČиʵƬȭ\x91ҋaюŴћ˴Ȝ?ωƞšϥ_{vȱɘσśɐ\u038b',
                            '˟ϋӷӶŭǷɐϧԝ\u0378ˤѩɋ\x93ϵҥʏ˖ąуϰ&ǂʂǁīЍİӅι',
                            'ӼĻĦДљƔЖʒνÞ҃џΌȚɌΫçʗşbЁ\u0381ȑĮҺȅұžѣǮ',
                            'ÞȘņɑӱŝ{ŋӈЖɣŁƿNʺҞȜ:ƻƵƭʍưԧГ\x82Ŕʒ\u0383S',
                            'ɵ\x86сНǊӿƯȈʒȴȩȏ˛бϐɶҌԌĂΏǲóɷǉƪƶǕÐϣˇ',
                            'ƘԓөȨðŰɾϦȹψωӊёƒŐƶӐĈRíѷeУǠɾ˖҆ϰˮЕ',
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': '΄гùԗıΦĳđԕÙΞϑο\x9aŷã5˒ђʮӾοĲ/ШϘИˁįԦ',
                    'version': [
                            -5424538963284334088,
                            -9086005406629984274,
                            -4041911429831016461,
                        ],
                    'about': 'ʦǕȪʋєāҥǿFůҥśțϻЪU˃jȹçÛӑɖūƭɥƎǐũ˅',
                    'description': 'әǨ˸Mҟȵųɢԙ\x9a$ȫºϑƣӪʻ˰ȰÀӫË˄²ϓƧȡіɯΞ',
                    'authors': [
                            '\x92Ѣ˻ÞдҪʀˌšɋЀĴʠÏɀˬͻȏϐȎĕӮԡƜѮȜķɽɨ˹',
                            '\x92ϊǚ3ӀҤΏԮ\x94ȝύĘƐV\x80ɑȐˉ\xadȘԋəѺɲäҏрūɩч',
                            'ŊÝӢ˷ϫȕȾ\x84ÿӲτȠǃӴҖĆ!˰ɫ˒ȥÛƱρȘ\x9aΎͶą˙',
                            'ҘȪX6ʦJҔȘǣΔΐϝFuČ˲ŁҹзĨӃȦͿō˶ĹȪɋ·ԫ',
                            ';TɿéǑӗԝŜĻŷ϶?ƞнȃɱȣтȒУӕ\x8f',
                            'OŨАŶȑσΜÎ·fŮҩʩҒˠϿȟувӧ\u0379ǭҤ\x8aĤíќɞȈë',
                            'ˣŐɓĂðѦÀΠǴʬĺѽȵʕϴʇҿĪѺƔΗȝ·šοτÐʇ´ʞ',
                            '˭βŧ',
                            'ɑɅҧŵϋ¥»ТȺӜɝηƹˣӕːЩ!˙Ŕ<\x96ŭˆ҅ȪɝĐІ\x91',
                            'ŅÑ.\u0382ɍάɣҞɋj?ȉΜĹɘźϺԢoԭӶñψėwƯҀōʺǝ',
                        ],
                    'licenses': [
                            'ʫƣΡ\x96ҥcjȆЛѺˀĔӣϩҕ˼҉ǃғӑċķ˝ӯ͵ӢӷԮâí',
                            'ōϤʻʁ\x99Aԥ>г7ʱȞÜβƟÄŀȥʨ·ÏԓŒaΌȲϯЉЎс',
                            'Ӓˆ½Ȇӏ˻ʪѻzώȩƳȯӨʴҸ Җ\x92ĺɃʹ8ȋ˥ȥīÜɓʐ',
                            'ŎӨͷӹԢũǜǘɃʼ\x85εʽýʕҊʐҖfʱЋ˥ȝҍЂǶґǔ2Ɖ',
                            '¼ҦӔИÃюμ¨ǚѭ˴ŭӣРӇѹƕҁԒīϐÊʕȑŮªӤГǈ7',
                        ],
                },
                {
                    'name': 'ƘҿȎЃȢΨʌdҔԣùʏ\x91ӺjҾЛˑЋȺȼɞ\x8fƭҢNΟОΐˊ',
                    'version': [
                            -1653988667483029767,
                            -1810864321585796962,
                            -4544762976714878834,
                        ],
                    'about': 'φЮǽΣĽϓÊҏΰѳĂǮԢďǾPϾаҔɡęԫˑĚĐ˟ĜØȿɈ',
                    'description': 'ʖ҇[ƏòӾ=Ȅǜư\x8aCӓƕӅ²ĂɖśøɛȜ;\x8bŇ¥ÒŇɱĲ',
                    'authors': [
                            'ìʾʤÛДơҜцɃδ\x8eаѰÊUϾӼʾǁӻ\x97ǃŮϐĽѸƍī¼ӫ',
                            'ϹүhŀӬӄʣҴƲ˾ҴΟȈƉ˖җήÎɛӾϊʴϣȰЫʖÕēęԗ',
                            '˰ҲĄİЫĨƫ\x9fЯѬσȒɮђƲƱӢƗ\x81ˢ\x97ȍҚ£ьѢƞȕϴφ',
                            '²˽ўˤfăѭдԜȎчŎʼӢ¼ơνκεǩԜϠ˗½ƑʦǝѵƌŊ',
                            'yŘʹҘ£ђțɤԞȁůŃϼĨ˾ʺ2ģ҄ɗɁɍԃр\x8cӻýʜ˙ԡ',
                        ],
                    'licenses': [
                            '¬.ԨȩлϞ˛έвÙ×уLʔҴҏɵƷÔȉĜ·§ĥĬ΅čԜƟð',
                            'ĺѣʍͷʗҽϤӢȰжӵŗșҪԖОf\u0382âʳҫοξǇ҈ȰňʋѡĆ',
                            "»еϗǀҤłˇǟҥԅťɯÈ'ŏѷʕǕȂΔɁ",
                            'ǔÕ _ЬшÉ\x80ȊЉȲϯʉǫĂb\x91\x91ʕНϨҤωԞŎζɍԎԎѼ',
                            'Ӯ˵žϣ˶ΩΙÍōҀǉɋЂȣǓʗŁɜļЖpȂEˬΣɢΝÒвq',
                            'ӡϪƱһô¯ʡɌƊĳ˲ɽӀɝƾǉɶ\u0379ɯˍŴɒʸʕ\xadǃŹNæʔ',
                            'пϯˈÛġɓЂȤXǞԣЯʐšǌ?ˮϷƜȻϑɘûŕƭʫƃƵǺН',
                            'ʿˇ҃˓Ǭ<Ӓ@ǒˤϳРĠķ\x83Ңǌ1ңΚȴŢǍ\x96ƪǴΘ˧Tǧ',
                            'Ƈ҇Ϋź=ɴƧʁˑѪýʷφ#ЫҖɱхėɚӡХʑʉĦǢƾŢʕԬ',
                            'ϵКӪĻɌəɆ=ȼőǷʹ',
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
                    'name': 'Ӑǃ®',
                    'version': [
                            -8550403374780036291,
                            -4448641897309262716,
                            -6616952645729939312,
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
