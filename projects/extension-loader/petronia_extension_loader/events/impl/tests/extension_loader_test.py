# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-28T02:46:04.481148+00:00

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
            'name': 'Ѥԡ҃ϵɷ\x8eʯʗԝϰӔˏҌ\u0382ҴȻ<ł϶ԎĵĆΪϙǦОeШƌѰ',
            'minimum_version': [
                -2511649879364293422,
                -2932664158905790477,
                -4572063698114911941,
            ],
            'below_version': [
                -277717291742164371,
                -3848575123055920010,
                -3969293456898579545,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ŖĝŔ',

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
            '$': 'ŜƠà"}ɺΊĉцҬСĴϦʏȞҊ˙ƒю\x82ҥӆǐϞŰІȵы\x98Ԁ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -5253274957169593917,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 245156.706989469,
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
            '$': '20210228:024604.413869:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'σ·˞ҡéͲΣ\x85ѪΏЭϏɏ:ΉɔʔTɧɍȠǳèÁԗа҇ѢԚƧ',
                '˹ŦĽЉЍȵКtǭǋѰǪЩŷǴ¶ҖƬӊŭѓѯХÇĮѾѠѹɲǵ',
                'ËҢHŞјʑΐľѡȠУȡʴԣƿÐȂϫʇÔɇԐʤѬҢrŝϲτҤ',
                'Ҁή˒ĕ7φƯɢȅҵɶҋӯƣӯѹȊ\x8fϡŰҗБЦţɹt\x96ϳôǰ',
                '³юʳYĝЪɎýL»ʒɅȅƊӜƭąʤˊ¶ưŌĶ\x9cϰѵŦʓƇЯ',
                'ҋ\u03a2˭ϕЍȒ§˲˰дΘ@ͳŕϴӃϳАʺñйȍǷǷĵƕԣ{\u0382Ƣ',
                '9Ԕ˼ĥʮӢȫѷĴЋɠϪ;ɿʍǐҁ\x85ҦǎԆǚͳҺӿiŋʂǬϳ',
                'δ϶Ŝљˆ¤ϱäǍԀŔҬŮҤӚöΠЗ\x99ɽǵ˘ȗ03ɓКɹØʞ',
                'Ғ\x8e\x9cГҥԬɋĎĵĞԚϫԗēѐʂӚԩ¶ǃʧɦЉˮӛ=ɜѽȩϚ',
                '˗ʦŅĉˉDǅ\x99ʑɦɠĲŤǋΎÏԍĄӃHġÿNȋӑǘҐ˶ŷʕ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -7058871333547901506,
                -1515509553830716515,
                8438938042121701600,
                7480553509171676536,
                -2576833404025897037,
                7713016538137552757,
                -1006083469824260453,
                7695520464123707811,
                -6959299412724488910,
                2279150624950658212,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                350311.41852489987,
                142536.3003418424,
                900148.4621487206,
                765965.1079734323,
                863382.2560195039,
                944621.7766745156,
                303294.65897225373,
                231827.1514804777,
                39816.63455750825,
                130690.4092916761,
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
                True,
                True,
                True,
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
                '20210228:024604.414770:+0000',
                '20210228:024604.414785:+0000',
                '20210228:024604.414793:+0000',
                '20210228:024604.414800:+0000',
                '20210228:024604.414806:+0000',
                '20210228:024604.414812:+0000',
                '20210228:024604.414818:+0000',
                '20210228:024604.414824:+0000',
                '20210228:024604.414830:+0000',
                '20210228:024604.414836:+0000',
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
            'name': '҂ӑт@ȈğɒάҵϵƚεеƨʿƳіȼłǷИвǑЏÏЗˆăԘɼ',
            'value': {
                '^': 'int_list',
                '$': [
                    7435097327291597978,
                    8644523642671957062,
                    6649229961360222482,
                    5421494056861029959,
                    -6934057440206744391,
                    -4865560551724448749,
                    5532340635996281990,
                    -6345467110399846234,
                    -721606644981248006,
                    -2155741749970893962,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ѿ',

            'value': {
                '^': 'int',
                '$': 3418150198040529625,
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
            'catalog': '?ҮɔҏȾїϳǈҾ;ΉǄšѴŶЛǕΩȶӒҮѱêѻАĈʙɂϞǯ',
            'message': 'ȸŲƸõǄȠSӒƐ[ċϷпѫ.ķԌҌŬĜ\xa0ύ˔ǔȱʹЭΉѤĬ',
            'arguments': [
                {
                    'name': 'ɪƶҤ',
                    'value': {
                            '^': 'float',
                            '$': -74212.94550138937,
                        },
                },
                {
                    'name': 'ʷȊmΆŌǕѮƳoƂ@ɒͷ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        4654668686591278815,
                                        -8882753772788523902,
                                        2976027520121954056,
                                        -4290505193552558905,
                                        4495732292966331645,
                                        2396317776144158703,
                                        3801599978101678860,
                                        2716980129756571530,
                                        6002217141586260314,
                                        -7680610224843990539,
                                    ],
                        },
                },
                {
                    'name': 'ѽu',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        False,
                                        True,
                                        True,
                                        False,
                                        False,
                                        True,
                                        False,
                                        True,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'MYʆÞ\x9eħяґôGәİúDƴ¶ΏЪĊ\u03a2ϙϽɜɐΩҶŘΏȱð',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ґѪ\x97ǂλϪƤԚҍ³хɖ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        8243037321761791935,
                                        -1462127539401063302,
                                        8194026492490396828,
                                        1987134775180169078,
                                        542320620877505726,
                                        8653069283893901047,
                                        1628170006128611813,
                                        4547622152321085995,
                                        486128989905851802,
                                        8445157331568467020,
                                    ],
                        },
                },
                {
                    'name': 'μЅăźť',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        8747432507530765598,
                                        4983509520283598581,
                                        622142464373317467,
                                        -7685706942539801664,
                                        -6404407538051373387,
                                        7212906413363524853,
                                        872745641861099681,
                                        759654759155767862,
                                        -6138894150974680702,
                                        -5790914320869249617,
                                    ],
                        },
                },
                {
                    'name': "˹ēÔ'Ϡ\u038bʧΫŖΜƤǈÈ",
                    'value': {
                            '^': 'int',
                            '$': -3162895881697403822,
                        },
                },
                {
                    'name': '"҄ě\x91QǵO~ńrżϛ=қũƿ˙ĲӡĊ¾щȖɱԍɻС',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ǗīјʜķȲŠʉùωіʨ(ʎЂӞɿхӀƓϨ˻Ï<ŒƘҩĞƈđ',
                                        'ªğ\x94зΌεɀэӎƴîʪΥƴíМɀĖУӂ\x91ˈҍˌҔͽō\x7fЗҬ',
                                        'ɷӷϻΧʆÄÃλϢԑ\x84ÒzϢÃПҩӫÔєƱƬò)êϦȚ!Vԋ',
                                        'ƪǥåԅҲ9˅ƃŇɑȶԩˡɍŨįȆZȦќƆѰƼӼΙƠԑқǴ?',
                                        'λη¶Ξ҅À\u038dԘǔԩĜʶĿĔžjҀ]ŵǤMԥQźԥӫ˲ȻĢǥ',
                                        'FɠϛɷŃӍҚǧƛЋљµɬ˖ΊQҊϊѯĩЖɄHӢοƠԟӊʃƐ',
                                        'ŜÍ˲қϐоĖЮě¶ΟÖҤξ+щѧȈƗȻƩʮгáʛʖĀʔã\x8c',
                                        '=ȊɐŶΓĥðϙƊÛúщψäˬǞ\x9fŌ϶нЊÿǕɌʲϟɦɖӸé',
                                        'żйŬʒĒ˦ʭΪ\x9eЈ\x91ŴҖʿ\x8eӺ\x9fοԭӶʘȜȃºˏԑ\x9d\x89tΘ',
                                        'ҥ\x8dˀũҮ˴ǆ˧ȀѵxӖƅӝӿͷɣĝӻƊΚiϸƋǴ˵ɣϞӖ5',
                                    ],
                        },
                },
                {
                    'name': 'аƊΒÉƦήҰ˸ѕıƮåӡȦϷɬˈɗ',
                    'value': {
                            '^': 'int',
                            '$': 4425652543191718509,
                        },
                },
                {
                    'name': 'ɱŅiß¨Ă Ǒû\x80ʬσӔ˼Ҝ-УѢʃ˝ōdǀϗηƦҹ\x9b@ʇ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'Ͳ´ʝ˕ϩϝďҺ±ǬȀøҟǮӷæȥȘXřϋ҅Ԧ΄;Лę7ņΣ',
                                        'ȞŮмĘЫʺӽżҴɤȧȑb˾ƟEҧƈӗſh\x86-ѱу´ŉόӒɹ',
                                        'ψхΥ~ɌĠˮƩҶ$Ɋ#ɘEżͱ҅ԉ҅ӅɻȻͿНңБўǮԓє',
                                        'ȕʬȤcʄ\x83вÍʊƖҕѲĹˋǫɺҺҷĜѮȄƳμʧĝсΪģЁĄ',
                                        'ϑĬ%Į˒ȄΠįǎӛÛΊŚūǚи˒ҷƪȎá˓шEԗȅΦǼЧϕ',
                                        'ɊϣʶȕѤҗѯԈӸ\x8fΗŵƼҨҤƑѨɈȉ\u03a2ӦҀðҼʥӘÀӎǛ0',
                                        'ǣӂϠʓ\x9dN˔ÃӜƷįȎӜɜΏ@ƦȰЍҨʨȑǸ˧ƶƉӞԨџ¬',
                                        'ΖʭӻŖÆЃǤËҹʇƮįѩԝ\x97ąρ[\x86҈˗m˜ǲŏ"ˌɉ˕ʣ',
                                        'ϮƛҒѣɦѽƍªԚϚҼǵʟʵ¤1ѶЂŧΌлǔȞʩΤϭēы˰ɝ',
                                        '\x94ŎŨʫКʟŘҏҋŌ¦=ҎǻͻԅŹɿòǱʬʦǬĀĖɚƪƂjǛ',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ԡţ',

            'message': 'ƞ',

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
            'identifier': 'ΜϧϠˈ҈ǮϽqѶĊӒȾĢĆņèTƬ\x8dʞ©QÃ¯ǛѶʯЏżԛ',
            'categories': [
                'internal',
                'network',
                'network',
                'file',
                'file',
                'access-restriction',
                'network',
                'file',
                'access-restriction',
                'internal',
            ],
            'source': '˟ЈøƄІƝҗФȳrnѺƛўьØГƯłʧ=ǃ8XҰΫƄÇѿǸ',
            'messages': [
                {
                    'catalog': 'ѻӗȕəӦǯýȈȆĢ;҇ȽΊӐǟđСɽӟΙɼˍˌƽТҟơŵˬ',
                    'message': "ɺ·àfѹөҶĽȫymĈЀШκ\x96ĭѩ҉ʹiıΓȘƷάϯǈ'ԧ",
                    'arguments': [
                            {
                                        'name': 'Ũ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˬҩӔϩӗѠXȻƝǅ˙DķбȢ!Ԍɭ˘JÈƗwʿҖȔƨΏ«ű',
                                                    },
                                    },
                            {
                                        'name': "ǛʔϚɴ˞¨ϓɔвġдŰȉ˼ƌ\x8bĔĂɩ\x93ПăƔȺ¬ʒ'ԛӷ=",
                                        'value': {
                                                        '^': 'int',
                                                        '$': 318984816249583553,
                                                    },
                                    },
                            {
                                        'name': 'Ѷ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024604.387045:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϺǑˢаȹ¦uÝкИһӠώӝǶ˶ȾHЮȸΘ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024604.387205:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ˈǩť5ǵľϞō´ʵиҦИĚϵcѧπ?Ś',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '.ηĒѿҎ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1256220602226644672,
                                                                            6619444141079633305,
                                                                            6633253995845431985,
                                                                            -8784695214089288733,
                                                                            8225976884037691360,
                                                                            -249300029292139930,
                                                                            -664315485611838562,
                                                                            3560298755964444021,
                                                                            -8156181132701206792,
                                                                            -9147147698033267238,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'O҉ʥ˛ȬԄΣƝϼ±ǰĳˀʨ#ЊuћpΣңþȮϳ϶˼Diɏ˪',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '»ңɏʱҷOūʝТʍ~?ԭ҄ґˇӼˌǖjҜâѰϚϦ\x93Ȅ\x93þе',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 504487.9522939039,
                                                    },
                                    },
                            {
                                        'name': '{,сђїɆΥҗÓ¯γͶϾö˽0ÊĈÖÉуʕҠŨÞɄǪɫȞӃ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2832618619242049581,
                                                                            -5439590737842449564,
                                                                            2146207646061446288,
                                                                            -6253216863010153402,
                                                                            9000610340362503722,
                                                                            8962672701890505964,
                                                                            -6219617306871877094,
                                                                            -619351394291588949,
                                                                            3353474791894972924,
                                                                            3454438744924235405,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʡ;ƄȌȷřʚˁѴǩəωԢaǯƴԫ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2316121837363723711,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ͰñȥΈΗȮĄ\x9bēλˌʃĢΐοЋϳſáƇtɀԐтĶȼQɕʪÖ',
                    'message': 'Х˺Ůȝ¡pʷļʓ¤ӥŋƵOΘċŗʲǙȪƝǳģǎЧɾƐԅ\x8eӖ',
                    'arguments': [
                            {
                                        'name': 'ϑǗōҙҌϿҫʅǽӱυ˯ȗćΥ˪Ё¾ʝ\u0378ѰʢʭƟa×ϵҭğó',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024604.388774:+0000',
                                                                            '20210228:024604.388789:+0000',
                                                                            '20210228:024604.388798:+0000',
                                                                            '20210228:024604.388805:+0000',
                                                                            '20210228:024604.388812:+0000',
                                                                            '20210228:024604.388819:+0000',
                                                                            '20210228:024604.388826:+0000',
                                                                            '20210228:024604.388833:+0000',
                                                                            '20210228:024604.388839:+0000',
                                                                            '20210228:024604.388845:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˚өɤ¢ӎÉϳϣƏÛҕƣ6ŶϳҵûαЧΨ\x8dĄāɥДë¾',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8009996061672575470,
                                                    },
                                    },
                            {
                                        'name': '³µŤ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ĶlΒʘǇȘЧā·ԟŶАɘʿԧɾ\x92γНũĖԅˤȢøʑKѱҦӯ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʽϪȞѠȨĲ¤ʨхгˮŋГ¬ȁˇѥǝĢɰϡү$фʶѕŠŨҊɴ',
                                                    },
                                    },
                            {
                                        'name': "ҦѼΛeʽҀǇŲ\x82ǇЪЮÂŇԎв˹Ģԡ?5§Ųřªϋ7\xa0'Ǫ",
                                        'value': {
                                                        '^': 'float',
                                                        '$': 549370.3658200777,
                                                    },
                                    },
                            {
                                        'name': 'ӷɻǍʮѕü`_ΔϬžǈȠ¦ȸøͰ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024604.389708:+0000',
                                                    },
                                    },
                            {
                                        'name': '\u038d?ȠԇǭΗ>ȫѩʿ˵óxψѻɖѳĨȸǇǸӬʀѪȖ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1077924909820871485,
                                                    },
                                    },
                            {
                                        'name': 'Ε',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȔΏHŤˏȢ\x8dӖīԎȌǏ˻ӷӺȩҫøɺ_ҵPȏ\x95Ґĩƍŗʲȸ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5354463222875050262,
                                                    },
                                    },
                            {
                                        'name': '˱ɟɓŧƺ\x9c\x85ҒȰſbōΏ¢ӕv\u038bFĈ˟ҌҐ\x9dӌȝѭʱǞΠɝ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 928067.8569194187,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'įԚϕÍ\u0382ΏĭɛԚŸĞϗϢҎӚȊ͵ϛ>ӖɅǀǂʷϖȸԏ\u0383ԜԔ',
                    'message': 'ˇÅÄϐӫŔӋŁȓρ\x8eϪ·ʼРњȵ˲,ίŃņ˲ҏƀç˼8ËӶ',
                    'arguments': [
                            {
                                        'name': 'Mfі҃ɠƮΤН³Ʈɐы',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': 'ȧǸțвƹʃΓĸЙġ\x8dңӷЃΚɅΦƯ&ǳĊcʍ˽ĝǘϸńˠ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024604.390999:+0000',
                                                                            '20210228:024604.391013:+0000',
                                                                            '20210228:024604.391021:+0000',
                                                                            '20210228:024604.391027:+0000',
                                                                            '20210228:024604.391033:+0000',
                                                                            '20210228:024604.391039:+0000',
                                                                            '20210228:024604.391045:+0000',
                                                                            '20210228:024604.391050:+0000',
                                                                            '20210228:024604.391056:+0000',
                                                                            '20210228:024604.391062:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'чǰîĪʪѴˢɲȈ˗ΡģʓȻӬљмΛўȯÓνиҫʘɍÃеΘѯ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -73854.35085707717,
                                                                            791061.2543706737,
                                                                            182416.77331773005,
                                                                            973642.9060901026,
                                                                            93596.07386037539,
                                                                            -53046.190099080915,
                                                                            -80023.21150553267,
                                                                            824562.6463684778,
                                                                            -46945.60665544196,
                                                                            378981.08845735755,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѺǼǨǛÍɡњѠʉǼǑƓǨȲͲĺЇ\x89ʶͷȎΑѸʷʹҧќƶ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 798779.4268878816,
                                                    },
                                    },
                            {
                                        'name': 'ҋǳǐ˹ɬȳǰѷÄǎύђ΅ʴԧ϶ҧ\u038bпɡˍʤÕͶίɳЗӝЀŔ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024604.391683:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϮɢяΤǬԩɓμɨƨԣПļ/ϰҼ!ʼԊ-ʳʬЛžђңà¿ԝs',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'έʌԍöž*ʯæΨʛΊУ˵ϼƟʡΜԗА¨К҄ʕOҺуӈӑϙƑ',
                                                                            'ˋƸѹͽŀɓτΝŰϺLѨ)Х˽ÀЋӎÁʗŊΥɽӱY˷ϰӁĤƠ',
                                                                            'Łˢʯ\x82ЍŗϊʵŰԃǏ˸ϰϵȝƗˮǥ\x89ȀЧĤ[пŎŹÏҦĚԅ',
                                                                            'ƑΊû\xadИHķŌ\u0382ǢΔ҆ЕлÁƃȂɍ½ŗӢҺˈ˕ȡҠ\xa0Ћ˙ԝ',
                                                                            'ɩάŔπÍ\x95ҹș͵јţɃ~ɄŶİԈԒȇ¦ЌӇÎЎ\x86ȢȣɟKЩ',
                                                                            'ɞʪʥӜʉâėÄŮɞȉɂ\x85ħɢ ǵҮÏԥəԓΉͻƊԃźΛȳˊ',
                                                                            '×ÛңԞшӬΗĆνǨŦƆƧϙ\x90ҥӈŲҍҥЍʀʒˡÒ7Ė\u0380¸˃',
                                                                            '˫8Ө˅ӏƸĻЏҀQԅņž¹ԙĞτȮğSÊħшbѭԈѻŪӊȿ',
                                                                            'ѳӜωȦ˯ˋƂ\x8bʛΚѱĲԬȊƁԚ¢жXӇĤвǖˤўѲŋүȇ±',
                                                                            'Θ˥ńīǸъǳ˕ψťІÿЖ˕ӠϰɉϵѤȋƸƽǋԬÞǲɟοȩҐ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϲ\x8dѾӏˌԠΤAăѬöӛΘӃˡ\x94ԇЙÍҩ\x95Mʤɲ˝EϴɺȃȻ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'V҅ӂͲϻD.ΚҪɶčüЭԐю˸ǘɇũˮŻ\x96ǫѼ=ļѣŁѬʬ',
                                                                            'Қǎʙʢ|ưЇԃòīĀӭŀˈ;ϽМǪǴѢ\u038dҀèʣԨƷŻǴʲȭ',
                                                                            '<ЈB\u0378ѝ¡ԂǏ˟ǜҶȹѶˤKАȞΦάǰȗʪѸɻqɛжЩȤӐ',
                                                                            'ȬвŻшϯњёǨŻĐӼ϶ҕɳыŨɛμǵӠæƍȏήΞdȮ\x88ЦĚ',
                                                                            '\x95*à`ȅ\x96Ɋ-ȀϛҌȕњɐΫΫН˩ǧƧā}ÈÓ˰ʧϒʓ˷Ô',
                                                                            'ȝˏȆҹȍħ˩ŏ¼ƓƜʪŖʙϟɀǩèͻ¥Ýүş+ʬƖԑǛ}њ',
                                                                            'ϴ҆єȎӏєæũѐӌıƤϚʈƎƗӧÙӢeƆϘ÷ǀďĔƐʼЌƧ',
                                                                            'Ŋbԫ9R˯ǧĽ\x99ĦέͲɣѵȽ˵ӮɩѢȦɣÓѐđǯһ\x8aĈÕ˞',
                                                                            '˾ϥ˳ȠϢҳϬȳЧƶǋЈҀ˅ɉŕ¬ӃɃҵЕ×ҥҮƤϻ`ԇðǉ',
                                                                            'ԏϝһƀІҥӣ£һɫΖйɋʘԭЭ"ӄѫ\u038d\x9eӰɍѴǗʑĄȢơĄ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ςѽ\x8bо1ϞđφwȥӯÔΪӢĽ;Šɳʾɭ\x97ӹğȖìɷѣƔѪд',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɪψșȬ7ǟćÜÇĩÇΥʓɡԭɾÀŰХŚѢ҇\x9aʢǣѽҔɷúč',
                                                                            'ąċӭùĚӇҰΓоȻŊĶΐŃҥ©ɹҳʹЦƥӚŰӮϞɽͿԟǃԙ',
                                                                            'λ<àҭʅԢдʨĪ,ş$lƺǵνЙ\x8fҌԉмβɔ϶ƺϘ)ӿžɜ',
                                                                            'ё7ƶΘäωѓf±tûǮԦǧʾ˾˔ϊġђӊƜ˙ŪΎ˥ѭƀʉe',
                                                                            '#QɃŶβξԊƘfĭɞҢӗƴς/ѪɐɔĖ\x97ϖҿ¼˩ӤҁȷwĘ',
                                                                            '\x86ŎɬǈıʔЄƺÏɢÍΟҊ\x93ɡΚƼsԕϳʇǂˉƇȥŝɦɹ\x96Ҋ',
                                                                            'ǉ|Ѫ\x9fΕ˦É\u0379\x85ɦ6ǕĦҷІϔŧsΝӡxƋξūϳȴϓΎ=\x89',
                                                                            'çňЅ˾ǢӉK£ÕѴͼʀБ^ҡӽʒÅӢΌҋñÉΈȒΟүҤđ\x89',
                                                                            'ŕLӗεԎγ˹ǫ ӏmѸȸȆÚǨáS\xa0˯\x90ŚʹáԦǈΐĸʰϚ',
                                                                            'ȟμ϶ŐSϘːn˯ƠYçŮˀӈ8ѷģʝƩʡˬ÷ωˬƍԙJ˻ˁ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҏş\x92ѶӶƱΠÐ\x96',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -138243303576356694,
                                                                            -3220960710007659102,
                                                                            -5981974880910832207,
                                                                            4693806531808918254,
                                                                            -1450415013322580816,
                                                                            7183378902902969032,
                                                                            -3073408704027105827,
                                                                            2698740112389962434,
                                                                            -4227570131670186349,
                                                                            7034720891171518740,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'TçɩěˬˆŴš6îѾɀҚ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5280393555048760374,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x8cżʻυčГƘƃ\x99Ùg?ɂʫϮԖѪôʇCřЍȄѷ˷ЀłʺԐɑ',
                    'message': 'ϬʂÀŲEƓϲɯʹɃАRĶƾ\x8cώҙÖȮѤ\x9cªӁŶνͻƃí¼Ε',
                    'arguments': [
                            {
                                        'name': 'Ɩʟė˂ѯԂԘưҭϋʐϬʸviЍʕћЯɹѬ^ԉЬˠƾ.ƹ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2842856972214175433,
                                                                            -1627471882446396228,
                                                                            -1147375730178561879,
                                                                            -1538270262507910362,
                                                                            -1869104612728022129,
                                                                            -1860269033260581058,
                                                                            -2447071892075296452,
                                                                            5412605235287758397,
                                                                            6620516704288411630,
                                                                            4367663039416458180,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԏ{ұόѫˏaԣˡӪĉЄɼà\x9eŭ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 817030.5939103573,
                                                    },
                                    },
                            {
                                        'name': 'ρRβ§ÕƏěЭы\x99IżåԔϔЪEm¬Ӧʵÿϗɩ«äǗĩ\u0381Ǭ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5267944946602871547,
                                                    },
                                    },
                            {
                                        'name': '\x84ϵҨϑҤҔġ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 888603.4738292386,
                                                    },
                                    },
                            {
                                        'name': 'ӜԟɣŹ[Ԋо',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǭӴʾǈϛИRȑɶ˟|¬ƶŏōĨŅԠίŧƘЀgȠǋϐІԜхƔ',
                                                    },
                                    },
                            {
                                        'name': 'ǎӞƵяӃ´\x86ȱʩψѬǙ§RΨέҤοƱƦΨǤùÅғɉȤ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԓήbҏӌҚ´ϱɛѠƖӍ\x93όŘʇϾ˾ѲǧĴґӮʀϔǦӠɃ/Ş',
                                                    },
                                    },
                            {
                                        'name': 'ˀŁ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʴ\u038d˗ԏɼўӛµ˫Ԭԣϕ\x7fɡ˽ҭЗƽŊǖԧȧ\x9fА',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5490878245583112534,
                                                                            2261423966402062246,
                                                                            -3519558733961264975,
                                                                            7366947278821952140,
                                                                            4118311277240613131,
                                                                            5725475760704948128,
                                                                            -2500071645147065038,
                                                                            -1526789071251873432,
                                                                            7461605588477837937,
                                                                            5560073290383026296,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΝɤЫжɠ9ϺɌӣ§χХǸƳɆÑ˰\x92˘ѲͱƁ˥Ӱĩ\x83ҔϽRΏ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '´ʾƋѶȡ¤\x86ǥӛ\x9eSԧѦӌ%ØƈƲЛzԍǬϓXбĜãCsŢ',
                                                                            'ΠůÌȴɟӟɥĒʒïqƺϦʴɟ҆¿ƉԗîҟΏóϹʹ-ɤБ<Ӛ',
                                                                            'Ňʵ˳ΪԏŝБɘƂѾϸ±ʆѲʙӖԦ˨ŧAʚӥŘѱоӮнơҕŌ',
                                                                            'ͳΎʥûƮ?`ȇĎǛʘƨӝŐѵɿxsҌʜƵÄɘӰ3өʈϊϓɽ',
                                                                            'Áǯҫ¦ȳϴ;¹ȹžϫɛӯȪҎϴŌěЅſʤХϖǟƀŭУӎ3ȕ',
                                                                            'Ãǻ˹ŉ˝ȝ\u0381ѷ\x99҈сҳ\x8aȚԩЯ\x7fƟǕӁͷXԉȜɬɻ¼\x98ɇМ',
                                                                            'ͱĉ\x83ԅÒʭƼʱӯЂŰʘŲLƠzͺŇáӼȣɸǴ-`ˡ\xadє*˟',
                                                                            'Íʎѣ0ϯжϫо˗ҍυьŷǂɅŽ°μƏĵÛ@ÍҨɤʮћ˫ѫε',
                                                                            'сūāʶń0Ãʋ#´\x88ԒσˑʱѽáǽɞҗǇȓňԏəϺҫʹȟӴ',
                                                                            'ϮσԖыăÜQŋћ(Ƈɦм\x87½˄ʐǙЉȱΙǋǎӬPǰφɇĞҳ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϸɝD\x99ˍ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -67383.35499635113,
                                                                            168304.2596442849,
                                                                            206732.3836795512,
                                                                            -93726.62527338808,
                                                                            271.6119866593217,
                                                                            107893.8277171212,
                                                                            142479.16433366496,
                                                                            886511.9571782886,
                                                                            235310.27790214436,
                                                                            570782.4875251221,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ÈŒŐµϿԞɕː\x85˽ӭƅϧңːёϨďǃƜÿԑ±ҝЮҏɪîԧˀ',
                    'message': 'ƸǼВ²ƷV˙ßȒƓʂο\u0383҄Ȯ|ǝÇȠɁв\x91īϿȺ˗ȍ΅ϯϜ',
                    'arguments': [
                            {
                                        'name': 'ăιҩȣɣӚ˹úЫʗԨ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ѯľѳϺψ˻ƜβÇȆŢӗÁ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 779969.7375407745,
                                                    },
                                    },
                            {
                                        'name': 'ȡΧɸ˦Ҕѷė˃Ǒϴ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'þ$ϭϨѓ\x95Ȑ҈њ³ʃǑʩҧʝʂßЖaʋԦҟԤЌŘҝаĥ˲Ϻ',
                                                                            'ӻвȃŧǝҭ˴ː+Ă\u0379˰\u0380ˍˠɗŽżɅȤЖѪϖʵρϑĬμ¡ӆ',
                                                                            'ȍѸ˱ҍүˡnɀϑϜͲ\u038dɹӏƅ˺ȳЧҞӓ˥ħ˓х\x84ĄɽԒмɃ',
                                                                            'ӰəϽƥ¶ӱĺԜƚХȳáʑʠǨʹͿϿӵ\x91ĥĤĥȨ\x92:˺ʡЕǞ',
                                                                            'ӸlȣĦӔaŻͷ3˼ʨɀǃ˷ƞ<υЖԖ\x90χйѷĨƪХėӐЮҭ',
                                                                            'Цɨ(´ʱʕĉɋѳӆϷӉуpУϬȇͼƒŽƿͽМƴŮѼƐíҙ*',
                                                                            'Èƒʰ\x90ϤŬǻЫӳǷԤӈÖºǻcǴͻϫйӬĽΙԟƋǾɢқ\u0378Ʊ',
                                                                            'ѯѼƳчƕԓϫǷ˶X˕ŒҽӷʰѿŽnԚϪ\x8eŠȆΏhƟЙҍʢ\x9b',
                                                                            'ɉʊɛ˹ƹƏEʜтҰʒÇƯŲï҅ČϒWwČδΑюԓĴȲʕˋа',
                                                                            'ÜMͳ©ǯƼŕŸтόʈƞÏπ˥ѽļ2ſГıĶүаɬʶŞϪкȫ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǄƱƫԀMЖ:δɽɧȀʱˠ\x86Ѐ҆Ù˘ȃӺʛ+ƩǂΑmɉ^ĮȒ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȼβːɔʜŚĀԇʺIƸ\x9fĿӾŞɦŤԑˊя\u038d±ѵ˷ťƙ͵ĳɩǕ',
                                                                            'Ǒ+Ԫдхӊ҆гȳĀԟȳĢϪCϠg˾ϧԓҖĹɟyǪɣƔзĩƀ',
                                                                            'ĆӍŲōфѲăÔŎȤ\x81´ҤʊėʙƷғ˨ǀηˮƙԓԙǨΥŜł\x80',
                                                                            'χƊϞȒǨʐƇóȃˆ˻ŲτǊţӰťӦȸуǟӘȸɳx°Ѐѐ\x8cɥ',
                                                                            'ϤΚ҆ΛǏȦѶӺӌѢҜёϳZѩ¢ΟӣŒơѧɂԇəДЋұэʎД',
                                                                            'Ξãϯъͻβь\u038bʀĲӳΫĐƨï\x96Ƣъ˝ɜåͺɚќ\x93ȠɋéDN',
                                                                            '@ӄц\x84\x85ɐϭ˗ȍȞƑѓҞЗԘϣŁżɻěÛĄƈҿʸAʿɜˢԐ',
                                                                            'ÆȔʌĒȔĤȠӿњ\x87ЛˋxϬʺѰˣυʌĩͺІɁŦЖȑʮӽӞɯ',
                                                                            'ƁčƞмȺЏɅãȅ\x8fύУŨΆЛɜŵɁĘӝęәǙҮʉkѦԙÒ\\',
                                                                            'ɣҚąăǭǲÆǴǿϖØӟ˅ƲǻѴʌȱδǲԊħHγˣύ˼ĕÞ\u0379',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'kеҪ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5109045181001619686,
                                                                            7292866597070184835,
                                                                            -270588302393055469,
                                                                            6858295192123495649,
                                                                            -7564849585015317618,
                                                                            -8309712630731760973,
                                                                            -3786718354948971858,
                                                                            -4833734971710227341,
                                                                            -2095868503654086625,
                                                                            4555199912197162948,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӿ\x9dёǃҡҮrȳ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'áʀȳц\x83ƝϮЩӱхƤŜԥȵċo6ϞȽ˲Ҭ˫Żѕ˜éΞ´Ǝ[',
                                                    },
                                    },
                            {
                                        'name': 'ϬѩԣӘĘхʁǩйɷÓȍȒŽŌӲƟДμˤʮǇϙȓƮѕÁѕŢć',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8263861353198420692,
                                                    },
                                    },
                            {
                                        'name': 'τ҉ξϷǭ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024604.398890:+0000',
                                                                            '20210228:024604.398915:+0000',
                                                                            '20210228:024604.398925:+0000',
                                                                            '20210228:024604.398932:+0000',
                                                                            '20210228:024604.398939:+0000',
                                                                            '20210228:024604.398946:+0000',
                                                                            '20210228:024604.398953:+0000',
                                                                            '20210228:024604.398960:+0000',
                                                                            '20210228:024604.398966:+0000',
                                                                            '20210228:024604.398973:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˲Ѓʰȷ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            142335.80398227865,
                                                                            746544.4247812344,
                                                                            215717.38460332336,
                                                                            991897.8668431188,
                                                                            248629.05233854894,
                                                                            393940.1179963507,
                                                                            225407.57856481278,
                                                                            391353.4968901485,
                                                                            579509.1917791644,
                                                                            481046.96276324615,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "ԓÍҔЩАČoɧЅυŎӞθѐХNˑǘӾȥŞǛĥ'©»ʹþΕ)",
                    'message': 'ɱѺҕΗć×œûЍŒ-Ϣȕ',
                    'arguments': [
                            {
                                        'name': 'tɱˡπ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ζƇξʚĢı˻ŢͳSΤøԅġӉ\u0383®ͰΔҜȄӋ}ʯδjφҀӞw',
                                                    },
                                    },
                            {
                                        'name': 'οςʘ×ĤҢȸԄĽŅх\x80˝',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7329349315491920036,
                                                    },
                                    },
                            {
                                        'name': 'Ω\x80Ŀ˦άϒѺ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\u0380ҕЃƉá\xa0ϡϐˈԌˍ_Ѳ\u0382Ͱőǰҽєэ$qçԡ!ɖÁɇ/˽',
                                                    },
                                    },
                            {
                                        'name': 'Эҗ˯ҥɲЌɧСĈǜԌ˘Iʈĉġ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ïśb~´˚Ƶ\\Ģ\u0378ѩǡÎ¨|ÙȰvĭɔˆӯόӛåƓӆɓȞǉ',
                                                    },
                                    },
                            {
                                        'name': '҈Ìáӄӡϋ.Ąσ~',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '*ҍҊϲЀ\x8cƴkűΊʮбԠ±ьʆϙǭEΚʇʙqűȭņӴɍҽҕ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6452227263018866266,
                                                    },
                                    },
                            {
                                        'name': 'Ӵˠș¡ѶƇď×ʝѯ΅ƪʄԌӤƸҀκǪƸ',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ĶϱǐԢЀϘ¶ԍƒϡȅОԦѼ'ԎįԀҦРʒѼ×ӿEң\u038b{ЃƯ",
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ę÷ϷoˮĚƿʌ.ƶŢӐMĺЊȧȢ˗ƢáõŘ\x8frǔŦ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            339025860422802502,
                                                                            2991102538237174146,
                                                                            74264977979310325,
                                                                            -2686645326175187437,
                                                                            -4268862650717455069,
                                                                            -5231366616177978020,
                                                                            -8473989803780295947,
                                                                            7407744734344397609,
                                                                            -2025004945472208672,
                                                                            1828865451256399366,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ľϖîų˷κʡǰɃЋɰƊϿɬɥΡǉδˌ=Ǌ(ҙȓƊÀсȍƱʜ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            985925424325377043,
                                                                            -1701651621825229856,
                                                                            -4740216917714598815,
                                                                            6670790502539449854,
                                                                            3366650191103031116,
                                                                            7650233980311804786,
                                                                            240419476371326750,
                                                                            -9157048559567748510,
                                                                            -5020973546875719354,
                                                                            6697599055659411737,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ͻρν˘œѱăϗҲҕșЈǦЮǘЩʉӌëUӆˇIҟÌÊŔʢҟΚ',
                    'message': 'ɕļɃΜȬ;χǜɄ¥`ŲËɶҪPѩģǁΒɎӜĴώʾɆˁԛóʨ',
                    'arguments': [
                            {
                                        'name': 'ĆΚöĞǬ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '}БĈҵǚ=əBʦФƜҶă˘ŻСΰѫFÿԫ4ÜԘѰơҽ\x8fÏɯ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "$ҟΤʙǕȗϵ6ӕ\\яѣĀƤӃƼŘё\x82ÖſĩΔԬđϑϦ'śб",
                                                    },
                                    },
                            {
                                        'name': 'Аŉǧųȑ\u0383ƨɹњӼƓӌ˾vέľђѴљʃ\x9fɳ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024604.402340:+0000',
                                                    },
                                    },
                            {
                                        'name': '˭ÆĳěΛȵÜԍÈĸȋ®ѕǈF}ȘǦĒ9ů~îȕ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024604.402489:+0000',
                                                                            '20210228:024604.402500:+0000',
                                                                            '20210228:024604.402508:+0000',
                                                                            '20210228:024604.402514:+0000',
                                                                            '20210228:024604.402520:+0000',
                                                                            '20210228:024604.402526:+0000',
                                                                            '20210228:024604.402532:+0000',
                                                                            '20210228:024604.402538:+0000',
                                                                            '20210228:024604.402544:+0000',
                                                                            '20210228:024604.402550:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '΄ѡӴÏϸNͷϲŜ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024604.402766:+0000',
                                                    },
                                    },
                            {
                                        'name': 'шӐɧ\x84±ЂǘŐƪœŮѴт˙ЙĝѵЈȲϣÕƽБЫɪŁƵΏŦȶ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 159798.92697129995,
                                                    },
                                    },
                            {
                                        'name': 'ŀ^αҽ¿Ά>ɌͷӚʉόѧɾƾıӻɌуϣȞΰ\\',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6692783438980312507,
                                                    },
                                    },
                            {
                                        'name': 'ɯԓã\x8a¯º˛Ͼʁɡф\\əϪ˖Ҧ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʤ\u0379ѣ©ŇμҿɵΆѮŭҴҒЍŕѿӵǌΜƔʏ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ʺ/ҡûƀÅͳʟƐ\x88{кÞДŨЈЏчцµŤ·īʂι',
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
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȻȨĄѵϭ]ϸҰǵӖέȔĲÑƟLІбūҥÀ°b˩˸ɶϨ>Υ;',
                    'message': 'ѮԜŶȈ΄ȨФϚϚӥԧϭöƁԓӰӏʙƋјĠǼѽǫУ\u038d±ƫɂ˫',
                    'arguments': [
                            {
                                        'name': '\x81ŉЦеWńċѶʼŠͰɲΗqОſЋɚ˷ҲԫԖƖΕӝЎѴς§Ŗ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɓǇ\u0379ƲĬ#ͽŧʓԣĉcs˝ӖɓҴ҂ʲɼ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ϟϫτ¾Ǜ\xa0ѻưǙȦӈƃ¹\u0379İʄ˱â˼s3ƶ³θҋėʲԥǶτ',
                                                    },
                                    },
                            {
                                        'name': 'ʏʸȽɐ¨϶ȗǙИǴ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8743162720378977998,
                                                    },
                                    },
                            {
                                        'name': 'ˠʹű',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': ':(хĢҝЖȎɇċų-ҦжȊ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȻυѿƝ˭ӫ\x80ƯʎӠĢȶSĊͿɄĶōʆɴʴʍɀȃѴ,ҲÍčѿ',
                                                    },
                                    },
                            {
                                        'name': 'ӝƒʠЧΤ˕!ĠϹȕҤи',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȲǅӲÇìơƕɤ˗TЯӛѽԤчŉ?Ќ¥ÈʲPĠś˥öʽѾҥ\u0382',
                                                                            'ƿ§˚Ɖ\x90ɬФѶǡǔ˨ˍІƤʒуͰŁûʙˤҦSάƉȊŹˁƪα',
                                                                            'ӇıξʐҤťƬМЪŐȇÆ|ȭ>ϸϦȣɀĭĽ\x98§ԞĔпǲĽďP',
                                                                            'ƷϓɨèƗłÓϻΧ\x88ƒҋªҀƃћǃʾњâȰЍϸϊ\x9aϬĕȦφȚ',
                                                                            'ƉʉӌΌϸÆ\u0379ȫǢrʨшƅŴ\x92ǋ\x94ͻπԧĐãҰѬѳʹҁʎрȭ',
                                                                            'ȚϏĉ0ľӗȃͺĵԛúĩdǶÕǀѡǲŞMʂĊҼҕВɜώOʫe',
                                                                            'Ѣќˆω\u03a2ɅÔŪʈҚЌƝҬǳѴЀǳgȿĤĚµ\x8aΉĈØӒʿёʀ',
                                                                            'Ǩʙ˙˸pɘϡģȬԞҩ¿ɸÖʨ<àɕшɘ\x81ȢЂӽаӫȄ\x8fǰҭ',
                                                                            'ύˆȏѱʍωǠȴѮɃˢ҇ќпǁϳĢδԍӒʰėҵċҍɡƟų˜ă',
                                                                            '˼lʃїɧƭˬƨſɁǂǙ҇ӦԧԩВΨԛΝÒğŃѫŁʢɛġĉң',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ąΙϠŽȊ˖ƪƅĞaΩҵǿmŁ˧ƂѰfƽҍӧ5ɵ±ҔʟΎ=Ȉ',
                    'message': 'ʚЈØԩɖǜДРʬӆɜϻЈԊҹѧʡԗǧțŨŞлŜҋɝŊλ]Ɔ',
                    'arguments': [
                            {
                                        'name': 'ŔШĿδѕĄϖ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            775045.2565009402,
                                                                            464874.2572613115,
                                                                            597451.7788605591,
                                                                            632720.6415689011,
                                                                            380906.748482063,
                                                                            -64747.81900799156,
                                                                            148145.60583159013,
                                                                            834543.483287797,
                                                                            870537.3067412019,
                                                                            212122.66502263251,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'їӈĜdѨ;ǒ:ШŦÌͷгƪŉĠƗϚǿȰĝʫÔʽŅ\u0380Ѐбҟҕ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ӕµɉǲ˚ƀś˧ɲӨЃûQϞǈɕèǂÊTˀ±ѫôӱÔҺ҂ыƭ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ΉʯűDƳąǝŧ˯ѵҳʵ˶Ƞкˬ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 46024.46271851947,
                                                    },
                                    },
                            {
                                        'name': '\u03a2ѯɨʈΑӠCůʚΣћӟĤĜcǤҩПФʺőɖԌĸĭιϰ÷Ʒο',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024604.406157:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĬÖƏɵŜąӟӯĂĒ˚ӾTȱ͵ƯΠƘѯԫҩBϲ҄ƘǯЎ\x9b˜˜',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                                        'name': 'ˇұԍˋϻΕâÜͰӉŽʅƍšÿ\u0381ҦΚJбЉʗÇҧȸ<ԒĥǸɬ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '·¿0җѨʤҾʏӖƟȁʶЬù˃ԫË\u0378·Љzӄ"ǪЈ˄ȷɇԣж',
                                                                            'ƶǂŮŅͽȊƷӇŞX®Ǝ˕ŌԗƦ|Ł\x80ѸӸǻ\x9dɼғ¸ǸƊ]Ӵ',
                                                                            'ȅζȄĤȞΈӰȑĒȑхшĨѧɩEΌχƚҰļȯ.μϛ\u0379ȶŷёǛ',
                                                                            'мƝӮƁˀƎ·Ń˧ˣҸ,`ѱͱ˃ѷӼŇ\x98ɢɏԫΤéšΔÙ÷Ɍ',
                                                                            'ǃť\u0379ĆΓΐɜ\x95˘ʒǘHцҚɈʉШ<˭ɑйХǱЖτғФ=¨ҳ',
                                                                            'Ϸ\x8dҧ˽Ǳħĸȓļ\x91ДǈʪӾĨ0^ġɱӥԧǌǈ<ǎΔqįѐɴ',
                                                                            'ϠЇХѭêͶʻŉşЧӸ\x87ɣȃəͱԂđ˱ʅүιœȐϞѸŰēͲ³',
                                                                            'ʐǇɝȠŅņҢԉùñɅʗĜƌŁʈˋɴ9ʮӑŵӒ҂ıӯªӾĸӴ',
                                                                            '˚ÂŇɸӜ(ʭʪŇԘι҃ɝͽƵэbӓˍʵƑϟψfĺɼɁөԗź',
                                                                            'Ҽ΅â]<ı¶НÞӁoȆԮƔΝƌԄȣ.ΖĉƆЫ¼ǡǜ҇ԎϾç',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҃ҬȴûΎ\x9dϚÿʌөÂÀнђȚІɼϒƝˋͷĝȠΰ×ÛѲʡϚǬ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4783430990395958,
                                                    },
                                    },
                            {
                                        'name': 'ӒhǐģђƤˎЎ\x88ƈƞќ\x95ϜԛӍчƀÖ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 780874.6896539961,
                                                    },
                                    },
                            {
                                        'name': 'ӽ˻˰ȍʛūԪΈČӓɗ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 286940.04466909333,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ˢѕǵҪf˙\x9bʱÿɤϢѦͻК',
                    'message': 'ȦƽV҆ȡFǵǟǱ\x8fʺʤŊüœː7αƼɤ{ŹԖɾғšÓǄćѽ',
                    'arguments': [
                            {
                                        'name': 'ξҢƦƪώҖěΙҫ@ϋˠжėӨәǇɥț¢ϲΊɛ\x9cǂu¬3ʖȧ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ԓʢ\x94\x92ϷųǋζȑύΪҬưɝʘʌ?άș˴ɆԖБμӗӫцĪ˶Ý',
                                                                            'οĂİйМǲԇȀˊӵȡèΣíϵȖɵФӬMǅΫρɘҒɾĎ\x9bІz',
                                                                            'ц\x80ɗʾoԩԌưӕȏ&҉gӔїɼѻ^Ҋʶă˴зEYʻ҃ěН\x92',
                                                                            'ЁȓǏŨɘjŬĠӬÞ˰ȅɌˑƊŋ[ɇǙÛʱĳ5ÎЌɮԔˍӲ2',
                                                                            'ƳŸƴΞŎëȬ£Zƛɪ?ǑȒȉɣƦǦʚӾҭʈήƿщȯЖ˔Ǒы',
                                                                            'ԛНɤǐҌʪŖԧүӎϤʵʴʈŋƙӛњɉϲȡʊɜǻԥЍύ÷ύ˲',
                                                                            'ϠЭZЉɓ϶\x88ʱǅ|ңϹɏϩǋõ,ņƺ³Ǉïҭ\x92ϑǐ˰ǝ˯ź',
                                                                            'ʃ˄oΛӒĚҕРӋҚҏƪU|ˤɐɜԢʳɿɚёѧҭƲͼ:ɸɻǠ',
                                                                            'ŢЇӽʍ2.ХÂʜ"сƶƁʾқђŸTРɮXę]вѮǢğϰԚϦ',
                                                                            'ѲўʮΧԬʪҔԏ¯ɑӌ*ԔƋȕӌ%ȖɹώʣƙәgңȚƱϩƜė',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӧĵ¸πȥϤҲЉѢһҩέ˄ĀťǞ\x82ƛðԫϘʇђјșíДÙ˅ӕ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3136040214089030643,
                                                    },
                                    },
                            {
                                        'name': 'µĳԙʅɢ,ѓ«Ӕӝ;ȟѳЦĸЃьǅ(Ͱɱ˙À',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024604.408164:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƌƆ˼',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024604.408298:+0000',
                                                                            '20210228:024604.408310:+0000',
                                                                            '20210228:024604.408317:+0000',
                                                                            '20210228:024604.408323:+0000',
                                                                            '20210228:024604.408329:+0000',
                                                                            '20210228:024604.408335:+0000',
                                                                            '20210228:024604.408340:+0000',
                                                                            '20210228:024604.408346:+0000',
                                                                            '20210228:024604.408352:+0000',
                                                                            '20210228:024604.408358:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԔÌñԏʟԓЯ΅ɷ°˺ȈЃ\x96ΗфхŠˀїʉЮƻлEəɁŦΤȯ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2581983324356174734,
                                                    },
                                    },
                            {
                                        'name': 'ʝ&ƍǁњ҃љ*ҿѤ˪ʦ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7232548923915178812,
                                                    },
                                    },
                            {
                                        'name': 'üƏӆӘȭșɿĞƐȝɐѬҨǊ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ÛƘюÓǲƮǂʶŲғӌNƌЅɔΏɊɁƸѬ˱лҿѺӶУϞ\x8eθʤ',
                                                    },
                                    },
                            {
                                        'name': 'Ά\x9dʷҀӯѷŚǏhǽ°ΕӗíӞ\u038dəƔԤҊ[śĉΒҝυɯɃįe',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            189608.06653294526,
                                                                            -95131.77217562594,
                                                                            986372.7510709937,
                                                                            341016.63014447,
                                                                            158103.6484718599,
                                                                            -79544.8365014114,
                                                                            463058.1176360301,
                                                                            874840.4130499181,
                                                                            303573.823690963,
                                                                            869820.097309297,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԤΕźŘĤЏ7ϓ:Ό|Xɕƥ+ǃŢӞҺˀτԤΎȬ˦Įʲxѳ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024604.409221:+0000',
                                                                            '20210228:024604.409235:+0000',
                                                                            '20210228:024604.409242:+0000',
                                                                            '20210228:024604.409249:+0000',
                                                                            '20210228:024604.409255:+0000',
                                                                            '20210228:024604.409261:+0000',
                                                                            '20210228:024604.409266:+0000',
                                                                            '20210228:024604.409272:+0000',
                                                                            '20210228:024604.409278:+0000',
                                                                            '20210228:024604.409284:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӶҩãʊÎȵĝƦPėѪϪиʍƗŗϴйҩΰĭŞӖɀʎʔȅ˼kǔ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
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

            'identifier': 'ωҼήΜȘ',

            'categories': [
                'invalid-user-action',
            ],

            'messages': [
                {
                    'catalog': 'Ů±',
                    'message': 'Ť',
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
            'name': 'Ƿʙǅ>үѨ ˼ыѫ«\x89ԁøʫќӵ\u038d',
            'error': {
                'identifier': 'ƴßʳŸɗϏȚmȣΌǭɬ˵řԮƙȦéťTң\u038bϊѢˬѲҦ҃ģǾ',
                'categories': [
                    'access-restriction',
                    'invalid-user-action',
                    'network',
                    'configuration',
                    'invalid-user-action',
                    'configuration',
                    'invalid-user-action',
                    'os',
                    'os',
                    'access-restriction',
                ],
                'source': 'ҞɷҵÐпņȨȯϏĳ˓ʲƤȚҥîғ҈Йȼґ_nӈjțŉɉҿҎ',
                'messages': [
                    {
                            'catalog': 'ӲӳɩԏōӭʪӗӿȘӵÀɚ´fЁAӻÞöξҫRœ\x9cϑȽн˒˫',
                            'message': 'ƎƪɃʡKȴĂ9µԦЦ\xadǤԟĪȖ϶ͳ.ˣн\u038b\u0378Ԁɢ҂ӬĻѩȁ',
                            'arguments': [
                                        {
                                                        'name': 'ɮEyʸϰɾЋ\x8eӨ\x97ʲηʇäι£ǋҳЎŨ\x9bʂ˔ʃ\u0380җ˔\u0380',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024604.366540:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ћɫ˭қԪǥӠγɊƈЋťЙǺϸЂǖλƲѣИŝųƼȐ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɑŜ\x8fŵùœċƑϲĪ˒',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȌƋǽЪαŏԓά˳®\x7fǆ\x9cϳōŎŎѶƗ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8924706668509759833,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƀє©ӈʄԢɛЧ%ӠѤǏà˵ђйǟԚɋʈRȽԬƦҀȚŬČԟʗ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8906206876584239724,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΩĥĶFƈ\x99ȘʃgʂƒдǬ\x9bИǗėĻʆȀ˹\x92ºńβʍʽЭӵ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7084998148029179424,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ćҰ˶ҭn9\x98ƯǏēĻ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ÁŸōçˑȚĝԪäħԈÓҺƻ˔ɑɕŁ҆Ұҍɼ´ƔВԃ¶ϰǛƬ',
                            'message': 'Δωå҇ΝkÃiýȊɐ˛ԏЋӡɵ+ê˥ϊǤϦԫœѓϣŚͳуq',
                            'arguments': [
                                        {
                                                        'name': 'ˀɝьӞҹţӍ±юͻġяķĶŕāϓϢ\x8dԐѤѧțʁɣŶġ҉ĄΛ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024604.368232:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɂ˂ƶƇҳЍŎƽѻȨǎ¨ƑΚīχҚѸͻνıʞ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '³ɗɡƟ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˕ɛöŬȎϱpӇĊɃҽӱΓIřǵʼέɻҲэǘ{Ӯ˶',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˎE',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǴјȊЗӉ!ɊϕɸƉºʎқʋϷǴĀȧɩȖːˌнԬ]˂дͼӵŗ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɹ¦zҀЭǋӔƙƞГŁ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĞÎıӲԣůҫ҄¨ɵΑĕШӗцɻǷˢǵ\x8d\\o˽ҊˉЙ}Ԑӌ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024604.369275:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x87ɴԮÒЏƓӆƦδϙϽҨƺŧϯ«ʚ\x8eƻΉҺгбҖ%Ӽϧѣ˟h',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӿġИƽӍdтШɊȨ\x8bʞλы',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÚȕÔӎ\x83ưĐӋÄĶΦȴϲ˪ŉÜ\u03a2ʪ҉ȳdèҾΗǆ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϔ ʺ.ΰΈ\x7f3-ȤʫeΊξңǵԂȕ\x95ɏ˲6ïΪǊȆԈɭƉ\x81',
                            'message': 'όԥгО+ˠԭ\x8e˚ЧˬҕӘĐďâƵΚȠНϽǾÅŘӕȡʷ˟øı',
                            'arguments': [
                                        {
                                                        'name': 'ȃ¬éĀҹɊóĽɦȹĐ¿ǹƟѭǟ}įӠƔϤǭ\x8cҦєԘŵ\x93ȴρ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǒ\u0382ζњӗ[ɋǶџϿыˏӣʷ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'әʭϨӁʮƿОʤƷƤǛӻuʈ[ȑþҏȉҺ҂ŕɗӷƃԝÒѥϣѹ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ÕдŎ(ȎЅŊԏǟʪ#˭4ΨȏɌ]τʇРΠˤŇȬʫřŉNȸă',
                                                                        },
                                                    },
                                        {
                                                        'name': 'pҴĞ\x88ɾƲЀǑϐЈҿżƙɅβªѷX',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԙѮʎΘëǰɔTäǀMɜӖ\x8cЁ\x82ĨȈԬèԠĈѴ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϒίфѷЅÓ|νбőʻ~яȪÀȾ҃ƍťőΝʲ˓ĸºΝ&\u0381ƗƱ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƉӼқȲʓϒȘ˭Ѳ|`ɹh',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˺ˢƻȰӜΡЫϯδʒΚДɠmʜƍеŇʟDÍâňΌ×ϲDԌʏʽ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024604.371127:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϲɠЄÚǏ˰ͻƸĉɝʋ¶Ѹ\x9bΖѱŚχ\\@ɷϼǧΆЀӁʃɟȋХ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҫ\x81þù^ѓèÜıOԘːˇԫȑǀƷӰԇҶƎɚʡͿȊȘ\x99ќ\x86ԝ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024604.371616:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÑõəˠЇ\xa0ƫͱ\u0379ęȑéʚÿēʑ}ңʵ0љ\x8cĳ$aÔϟж¼ͼ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2526378098353599201,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԁŎƋҢG-ėʺǱТɇ¼ʦȉЃSŐȱИŕȷ˚ȍƩȀ\x93ҏ×ɿō',
                            'message': 'ɱȖĭƢŝϑĦқσÑӱӆɋʺҳıβəϥďĢԕϞǹ҉=\x7f#Ԝұ',
                            'arguments': [
                                        {
                                                        'name': 'ʵǗ>ʂɗɍϡҪǑ˭ŭɭοʝϊʄІϟȦǝѸ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024604.372817:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʍèџԩ]\x9eğîƍɄßUӖʘǗȕ\x9aȵʊʥӘU¨rǂ\u03a2ƆȫȨ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӤćӜǜǗ>ɹʧэˢьȍјѮǒȽYËѾЂ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӦбͶƌԢʈӬȽƀʉН\xad˒Ӕʚ¼еєЕßѻƗѡϙӌҊʽӑĢÛ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024604.373500:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӪͷĢʷĤÁоɒǩҀόİϙήЮ7ɾӢ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -37913.956876013624,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ʋˡλ\x97юʖʰɂѲǟȷ˽˂ıΖϟ\x9dȈʚӱȜϋΙĎʠ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѥѻ˧\x90ˢѻ\u0379Т\u038bǦƣʆ\x83ʨŢȵӫңοǃùɐ[ͺҬԣ϶ϤnĐ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6342922704976071184,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u038bąϊʍĚŒѬѷĂʙԃѼ]ʯѢ\x92Ƙ^FԓΉЦƶΜԃԓ\x8dȦҿŴ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԋѠҢҲϓɹˢЄ˷Ӄ¥ǊΩ˰½ъɘϢ@ԌȲ¯ϢƏʝɣɶƊР\x86',
                                                                        },
                                                    },
                                        {
                                                        'name': '͵ČʃаɜϛЋϴ8ŰĲȨÿ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'тƔЌʭβЂҀЪȁɔİҞЀΦgˋ?ɨǯȱͶÃϝġԈʿϓŋӆȣ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӌÈƿɇđˤřȲǐщӔьϣȁƑԜȢΘєĽ˟ɕηĳӝ˶ǎ\xadҜ!',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ÛǕщȐΣʄƇJӪȚĘǎԢƧӵθˋǎȦȉǵÍŤ³\x90όӢOЭѤ',
                            'message': 'ǘŞĽʭÓĒ¹Ѐϧԛ¬ŮíȤƩĿхŃǀ.ϋңėϙЃЖȎαɪu',
                            'arguments': [
                                        {
                                                        'name': 'ɼĽ҉',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 234255.13043227186,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʝ«ĕӅӒӺƮҡ˱Ѳ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 623866.8357052407,
                                                                        },
                                                    },
                                        {
                                                        'name': 'цĞϵťƋĆŕTѢңο΅öĎ\xadӹʲǦ˗Ӯ˸Ťǳʧˑ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʚ´˗Ħ*ďǫˍͻ²ÛĆˊʖѰˇ˚Ωɷ҂ĥΙċӓɚδӲѴǐŋ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'qΣ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ưұěŐеʊƗ\x82ҡ\x92ȢũXӹ\x9dЄCŶɂˍϡ,ʹӠӆ\xadЍǕçá',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024604.375863:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȗа˔ыcËϒōҀĄ\u0380ѪŮ҂ȣЅdĴƢӽ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԝ\x88яSǕȼȬҨˤΆòН\xa0˦Ͽ\x9aθ6÷Ġ"ьҝʃǑã\x8cҬď²',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϩ\u0381ƋüĺΏӯИδôǘǼө{¹ӃΆ¤',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ФҁɒκԛѮѾ\x93ӉˏҺвȷȂҭǦІʺή΄ϊΦЋŐʩsұСXγ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'πťɺWΒЊѐ²łưÍАϠˣ8\x8fƏҽǔȐҘƂC\x8dŜӀę\x87ȯΤ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƈRΎüȋίȐÂӢġħ\x84\u0383ͻǼҚӸ\u0382GӚʦҚĴĝЁэË´ϣʍ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -23678.42751146792,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x81Ўшʉҷŉ©ΏƯΪŽǭβǊÎzƛϬɝιȴϤҊҮ\x97äōқƠщ',
                            'message': 'ƫЪĶšӤӥúȮǔϟқȾŭΓƵ[τѣʱґĝͿԡɡɕɽ˰ķˠƬ',
                            'arguments': [
                                        {
                                                        'name': 'зþϤˡҪæ÷ΙќAŇɵ0щӌΣҝʁʃʶ˛ѸϫɳԭΒò°ǁͷ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ªĎ҄ή',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĞǑЪӂɀǘ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҷ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'MʋҖĒˈɻʭ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɷ\u0381ìƧϖѦЅ*˾τǮҘΜ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3789990773309843124,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӯ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 191381.43693638517,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ê1έӂPΈ˫с\x83гɽ·ҕэԨΚǢɞѨɠǩˢ=©ЁʾƩӿҬϚ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˄ũЌд$ςĒξ Ж\x90ʾȖȴʰĂ!ϲHϕŴʨËӭǚϕͲѳʱʐ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѝˌѯ>ƤЋԞ\xadˋʨʳĄЪ³ļ\u038bϏȐ\u0379ѿ˾Ğ²',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2616885722980669030,
                                                                        },
                                                    },
                                        {
                                                        'name': 'źҕşӬ҈ӸǳΨ.ϯșƳѝ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΟîňȉΗˏãĶ˾ΪԣÈҡχΖQєnϟʹѾȁф¶ϣĕĽԍуț',
                            'message': 'ӱϟЄϖ²ҚȰãҶƗѱɪ|ʚȼʳǺöҫ¢ҖːΟǈÏ1ҐжŌԜ',
                            'arguments': [
                                    ],
                        },
                    {
                            'catalog': '\u0378ӊϕͿúξƬˑôҨǋΦӸӹɏĜ˲àŧʭ\x9bίʟяǤǸĂ˳żƌ',
                            'message': 'ƋƾɥƩÒИLѭŇҸȧϩӐǫöӏȨ˧ǐЁȍ3ϖЧ;ʥȓАʔƢ',
                            'arguments': [
                                        {
                                                        'name': 'ȫ\x8eȧӲİĈʌ£ȯʛōЖҶˍ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'πĔ˶ǧÎ˻ɳE\\҃ВŃяВφӀ(ˢԩòӅǒӁҶˀȥʜ˖ѽу',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϯ:ìҳ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024604.379361:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'φӸȬ¬ĩȝόӾƕб,.ơĠӭͲɫҥÙƣёļǘöʨȚʕҩX?',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҔҽýρҁɝԠЉŝ\x9bȝƒрĠӹɝ÷ӚϿɰɥPʒӏ8ԃ˂',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 171833.6690530533,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9aƁČΎ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˛ˠψҥɐӳ¯ǔǼ#ϰӲŭȟʣYA˩>ЌƜԍśɻɋЗɋ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ř˸ěƥqʲːϧҶͷƷƴԂĹǁӆǃЕМǙőºĢʙȈӟÔ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Уƅ+ŗψМɋǋȌ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'өÁҜ˝ȧӷпķΕЕ~\x8e[ƦʿÉï˄ÉʉϢYãɹҳȷƈѷ\x95ф',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ФȌˡĮɱǷȭԤǜƫłӝĒ\x90ЎӑĤζê\x91Ƈ',
                            'message': 'ɣȫîǵЂ˟ɔƄԛОԍËîoăҤĥɍ˳ɯƷǢȑ³ŁɎư$±Ĳ',
                            'arguments': [
                                        {
                                                        'name': 'ѽǵоǣѷ\u038b',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '¯ģҥϪǲǊÝ¶_ʸˀ\x96ҊδӒϘѮɝȎԀͳǲΏʥ˫ѱȏȢәƝ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024604.382292:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'εєì϶ʸӚöҜİk\x83',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024604.382470:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɒεϻѿѱЬ\x9cİǥŜΐŪљ£ͶĈѳOƾ«ŤʣӖ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'V˼ӵ¶ОȒΟ$Ӹʦύ˰ŏşԡӻӶǽq˄ʝƽ\\ĩ_ӫЄǧњǿ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŀˉ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'φϼȾĭjϮ,ɂґ҉ϴʏϡҁȎԃӮǍÑԦϘʜȅ¿ʰ!ǕʠԦ˓',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʏŎӋūїVáˎzјʜ˖ҺїКÌXҬAǚɵӔȪϾ˵Ðɝ-ѿ˩',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024604.383054:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɻʶɅϽΓξǈØȣԆʯ"Дп',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˗Ӿ)ΉξιҎϷʳʃuԃÒǒŌʒȸ\xa0HѩÒ±QɒȌůıЎɚӑ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʺ\x8dьĢґɸiвќɩɩӈĊ:ԐѕпЄ`ɌӗˡĆͽȶҫȐͲˉʹ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƌӢŭƚ˂ѤʱĜñϖʫŔǬɸѺFο(ĎȞΓàɋѓȀЉřɶϸɀ',
                            'message': 'Ԧ҅ͺrϦͼȞԐЮ+·XӐÍµԕӘʉ,Ԡ\x87ԇϡуģŸҴέӧɗ',
                            'arguments': [
                                        {
                                                        'name': 'Ƃ¯οȯΌɭʞЉëүӀǱЖÎǀҨҏŖуL®я',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɎќʛӬѭĵжƆǅQƂѢʼɛÊӊѧ¨ˠҚЯџɂϱêʥ±Ŋλȴ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '"ƫҙӊ ȁɓ˪˪Ң@Ԛϻӕ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¼Εѐ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'mӤ˚йOҬɩȚĭˡүҌǵčɆ˟ѠϭƲϟӈѷӃɟ~ЫǬɵπ˼',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƟѳŪǋ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ЖɛŵӚ¥ÛʥΕɷɰԊʌӣ³ǉǨѢҡřȅӮȪɷƐő\u0382Ǟȇƶ\x9d',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԞΧʟϓĊǢ˙ȦѶ{ǌ½ѤҵΊӛʿʈ\x9dϾʂĿщпĠƾΝI',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 21137.717430285426,
                                                                        },
                                                    },
                                        {
                                                        'name': 'AʲöǢęúӐĿďQбд\x9aϙњԥȜӇИƤ\x8fңáʋGō·Ǡȝԥ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɽ˅;Ƿ҃3λȲƵȱɛʽĠϽӱƗɠˢ˟ҰÜéԤќȲƕʄăȹƹ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƹϥňґ¬М˙ѩý',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
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

            'name': 'ɿʯɱ',

            'error': {
                'identifier': 'ħĸsϩԩ',
                'categories': [
                    'access-restriction',
                ],
                'messages': [
                    {
                            'catalog': 'ͻӂ',
                            'message': 'Ǜ',
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
            'name': 'ѝƢāŴÎŻ˥ǺӿɄΙȨťѐѯΔɳӸÆӞϏ˒ŌӚ\x8eȾȉɅĭǸ',
            'version': [
                -2467230111839257249,
                -6927685109361571529,
                -8591139770863041396,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ЏįѢ',

            'version': [
                -1012965670478834456,
                -9171226404803820497,
                -775314110740104162,
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
            'event_id': 'ņɶÃɶó\x95ʷɜ˓ӭԦҡөϨʧҊɣ\x8dѾȵХĘȿıЪʛǠ˔ɘʛ',
            'target_id': 'ˊȁԙӯԖȉ!рˤu˪ʢσɛρƈŲӀ҂ЎȪdø0Ƌ˹ɞдӾŁ',
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
                    'event_id': 'Ξƪ&Pkʻ/eɱœȃZϢƁҒɇґüm\x98Edɍ˰úˎЃɩ˄Ë',
                    'target_id': 'ƳĜǧsƾʏâѶͶȆɔȯȖҙƑ\x9c8ҔԨĉȮʪǀӜҐҍΚ\x84ѹӨ',
                },
                {
                    'event_id': 'ɼʹJкȪԜĭRԐʽɴю¯ͺʳϱȵϵφєþюԬ?ϞӆɨɂŪэ',
                    'target_id': 'Іӆvр0ªϖϦΔЩӫԉ°ѩǫƊĐaɦȾʥԏĽ˻8ʐԉŞʌў',
                },
                {
                    'event_id': '˨ҐʫϦĸʑ\u0383ΘѝXȌ\u0381mƑӬ8ʸ¸ӣ¢ҠãǛƝӖłФǈ<Ȭ',
                    'target_id': 'ψoЎȪζЄóӢщEƛχ¨˛ũ¯3VȬkЧԮħ˒ԢϏðưǾō',
                },
                {
                    'event_id': 'ǰǶȝЯˏԣǁПĺч˻Ä\x9c³ҝʱı)ħҎĳӕԀƺʙԑӗǙȺȍ',
                    'target_id': 'ȳфÆЙĔɐА|ƙѦeАğίђϷÒǞȜήУɕɟʱǖɆȚĀхԉ',
                },
                {
                    'event_id': 'ұϘƑáÁϜ+ΐůəīČ˖ñˬɡԂÕҼІ\x8eÈҠԇʎÞ\x87΄ȻЖ',
                    'target_id': 'ǱØ1O¹ҵˊԪʟϙcēӰȳӕΞăћҐǽɥưÚĮŭӞťɏчģ',
                },
                {
                    'event_id': ' ÐȦħ(ӾȦȶSӀԒ9ӠϪǿîңqğϐ˦ԓȚϞ\u038bǜçƵҥȽ',
                    'target_id': '˴ƿd˰Ģͷ¿ѽʞԫӟǟÍŏѰƚ©ԝʶī?ȶȃӛÛȝҩДQţ',
                },
                {
                    'event_id': '"ȉћʱˆ˱ѼЄϕ˧ѻǂԅƩͳȺăÛԐƁЊŠԐѼͿʰӤȂҝф',
                    'target_id': 'Ґǜʭ¼ɢÅ˅ӊŸЉ}ʊŴ2D҆ѱ˰ůPÄйưȅӵɊӍɂҬ˂',
                },
                {
                    'event_id': 'ӏ¬΄ƉɝԀûӜƿѯƋŜɱĆҎ˚xѢ¢ʀ҄ɐєʢ¸ˀѤ\x9bЁǳ',
                    'target_id': 'Ԭїš˨ϚďƎȎHǳŏҦɈͱǓϾŨʯǉԢϺҐҏĭĴUƕΥƯì',
                },
                {
                    'event_id': 'Α˔ƤƊ҈ŏԚӪҜΚҹфĭǰǋćӆяȫӕа͵ӾÐЫωˇϮӿȎ',
                    'target_id': '·ώӅυЦГѫҠĖҷʅЕĔ˛ʟмʼ˥ŀĭŠɼŠғÖƥӥǙАŃ',
                },
                {
                    'event_id': '\u0382ΐűȔɌѮ&ʟǝАĨӳˎŐ5ÀhɐоđϤɷ\u038bRϰ˾ϊʒƒЂ',
                    'target_id': 'ЙŷĥҘ+#ÎʇŀȶҖѢѨÅҟΰÓьӐκȽϑһџ_ʈ˸ɇfτ',
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
                    'event_id': 'ӵљΧѩɚѺ҄Ķӱ\x8c®Ѣǅŧс¤½ӛėĢΚwŌώŞҼҩʧTŐ',
                    'target_id': 'Тŋ.ƽ˜\x86ÝЋϔǶ~´\u038bθʸӢнŘʁЭϔĐŕĈŕĉǦ:´˨',
                },
                {
                    'event_id': 'άҿlɕİΩɳ',
                    'target_id': 'ΜҦÕãҲҿҞɳüωȇӄʔĮîŕΞӉͱĐǹҔΎʎаˏɉӄ9Ќ',
                },
                {
                    'event_id': '˟˙ϏļѺӴ˦Ôӣŗ½ɓŢ\u0380ɖ/rˇӽŤϰ\x85҂6ίǟǯϡЉΊ',
                    'target_id': 'ʦѡQЁȵǞØɗµДϢʧ\x9aοΠʳȵ7œƭZˇʾҏӱǳпȷǟʎ',
                },
                {
                    'event_id': 'ΌΑȁǛŻĕƴйϧȰϷǽŖӖґдĀċɿœҾӇȒԅъĹϸ@σ\u0379',
                    'target_id': '\u038bǺаʪ9\u038bȬҨ҉ɏÅ#˙ɼ\x8bɹω˘ϴĮƂл\u038bėƭſÇÎǭΜ',
                },
                {
                    'event_id': 'ʢ˙λǻԋтȳƎ˼ΫӾαƇőӞ˞Ƕ˳ĂǾkҐɎӪúɂɠǝȴȷ',
                    'target_id': 'ȥφŨsłӈƘʫԤӀ˞Ð˘Ťˢń®˛ИɠpGŢӷΧʾɀҢҦÉ',
                },
                {
                    'event_id': 'ƞĜˎό\u038dǬ[ųñǽˊŃԟʡñқƝ҈ŀǝϒ³Ҳ9<G˱ԪňԘ',
                    'target_id': 'ƉĊbиʚóҐʼƈǛ\xadαʴͼ\x9cϽϡєƓΪȰԋƏςԔý)ɸǻɇ',
                },
                {
                    'event_id': "Ȏԙ\x80x\u0378ȬĐҒ˥Ƴ\x97ČÞȃű'Η1ҟγÝƚЍŝ˼ȸуҲǆǾ",
                    'target_id': 'çʖǶõȔ˧6ԓαӔЁΨϗΕ¹кѩť/πŚL«θʟӲŶʺɮϋ',
                },
                {
                    'event_id': 'Ӏ\x8cɨȇʲǥЙԄβ~ЩϱМĵǡ_ϘŽӗƕM;ØӉǈϦеѓ<ʄ',
                    'target_id': 'ҶƐ˟ŉʴɵΡ×tӄʗȃҸґʱΝ\x99ǄΘġϏҾˎӪ#JÀЛʪϡ',
                },
                {
                    'event_id': 'ϷԤѠсŊɯ',
                    'target_id': ',ґŘƱƹČҼԣӮʾӶԎƪ˥Ҏ4ǦˍƶǗůʽȰҲ\u0383RZΩўħ',
                },
                {
                    'event_id': 'ƾӊǪùԍϏӪǗΉΙѳԢӑɘαÃ˯έ҆Ϯ<Ĝ\x9eνӾɀĕƛҹT',
                    'target_id': 'οƕǪƤХɞÙɮЀҀЪɗϖϼϯȁ5я®эɰĚMљХ%Ŧé¥§',
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
            'name': 'ɽĞ˾ϭғǂԨɗǠɥ҆Ѵǯ|ңˋÓͱԤʀȀɴɔ˗қŧτ҈Ⱥӝ',
            'version': [
                -4682616264655084649,
                -4509984453774609591,
                -4261887572058181056,
            ],
            'about': 'ó§ƘǢɚӯőɞηŇ©Ȑ϶ƤŚӴԮòӊ\x93ǪͽϯıóΌǲȫěԏ',
            'description': 'çȓμǥ|Ъª2:ǿǋɅř ˪âЏǟӀʉǩ%Ӆǰ`ŇnАѲʓ',
            'authors': [
                'Ñǫl9ͲϦϐͻńľҭ˩ɘǀØюԕћLӂɁěÊ˸ƾĪÊ˦ÃΒ',
                'SӸӅǟӛǊ=ϮэԙQоħǭʫŸѻŁӣŲ\x9dƚƕÂûȡƬvԫͿ',
                'śʅѰʗǪ\x89ԣΨ\u0378ɬÚJ!ˇE҅ĀΚȥwʅԦίʼӷʔǵ',
                'ĹŦKέЅĒҪτA§ɸ˶ϔϥĆҕȷһŤ9ωȩӮωƑ[ҜИӟҾ',
                'ŐɯƒǹΗŸξʈбʨʘЁÚ\x87ȗМ¹ґǧԟңϽϔȠȫӀʭē#ȩ',
                '˺>ɄǓϐɈZǏсΕFЋȌŢāƊƛЦϾԤӤ_ĒĀћȶĪʴ)Ԥ',
                '˓ȟŧǙǧ)ǀɺæе\u0378ƽĥ¾Ƴˤ\x9dǵӭļӱØʛ\u0379оѸҁϢΉÆ',
                'ԐȥΨǷŏ*ЮàʠƏԙɭđӁ˔\x9eˬͷUәϕЊǀɾ·ŗˢȦ×Ԡ',
                '\x9fͳԫ\x9fʦѯЗѵȣ˖ɊĬȇȘϑӏÌԉӾΦı\x8eãǵПҡҐїυђ',
                'ǆƅɎҪ\x80ϺюңǉǡÕʪȏӵҭ˘ӺӋ˄ԠƪιȢ˽ȮʌΘѕȘü',
            ],
            'licenses': [
                'ĢТĒǸ˚˽ӛѲҎЌεɊʔҤ˷ʇ\x80ĮǇǳҏӥʋ]ÑŚ˰Ϗʋʿ',
                'ŋǘ˲ʄȪÏũфҮӧΛÃ1\x81ŜȳĦïȧ҅ЖЧ˕Ȓҧҁ¹uʃЮ',
                'șƶƧҦҴ\x98ɉ˫ΦҖŒΛӺƠȸͷħˀđĻ\x9bѹɿѩǈ˗ʚˈѵÞ',
                'ʣѾʘſ~\x83ĖŊԥ%Ϫѥ\x83ƪiԅ˟ϭʹĎцʾȧӐλӗХ˦Ķ\x86',
                '÷p´ίǉѷѿϏɫϯǇмɛûώǤgЙЌӸȢ˗ȦǟR˗ЕƤҵѥ',
                'ĳÒЦǢЏDǊ[ӗӐҩŋϴȿ\x99ɛÞǦͻ˥ȗˀΠéɼͱǕÈʒS',
                'ђόǑӃʆŸ\u0378Яʙ˘δЈʹΤέҡ5ҍҡԡȩƫѾkΨ\xa0˚ǭԆƦ',
                'щKĘʟ$8ǸöŏÓɂӄȭӱƓеµԪʊȠ|ƨÁġ\x87ҠɉʰѵΟ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ȒѨý',

            'version': [
                -1448798598585985257,
                -1769354195002718297,
                -3449169221467898642,
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
                    'name': 'гƵʉϖȱ҄´őӼƞОÕКтоͽ\x94\u038bˬюљйϨĚѧϤЬӣŹs',
                    'version': [
                            -2300880257875958097,
                            -7245819407223304308,
                            -8897305662296294783,
                        ],
                    'about': '˴ƬÁԊ@3ȞĩĶĈͿĭɐөǤҮuŻ\u03a2Ӄɋ\x97ԃīˆуVԫȳӰ',
                    'description': 'лƏҕϣȶεэmĶą ɳѱĘȋњӓǳϙʑԚƑе?ȹļ\x88>Pѓ',
                    'authors': [
                            'ԞYȰ˳ʩˌǺӋȇƷΩψȒǉɡoύɕ˻ÇϨǰδĘ҈ɘѳʔҼч',
                            'ƇǠǕRʓˑЄ\x93ʵФǮǱĀ÷ԠˋēŪƆԎŵǌ˒ŭθȻnΔĐӟ',
                            'ҞѺѡɉχϭóҮӳĦƿԣƋ˒;\x81Ӏϱφ2ǆɞҧʥȭǡʉȑкʅ',
                            'ɘɒĪҴҷΔЖїÃÓƕȚԦԃȿƀѥƜɛŘͶåˎЯYȘķүɇś',
                            'ʗϵŎĆҘ7Ȣ˭ωп!ӰšʡʍŰŷoô\x81΅ӭӥ˜Шʶοɬøҭ',
                            'Ґаһ9ƲȺë&ΛЅΫ҄ăИğϦě±ӻ¦ˈʞѯȡϕļ©әYЍ',
                            'ǳљεȕ1ҫЀÄ˘\x9cƣĥĠÏȕčɫ\u038bҭȰ\u03a2\x82ʹȹŖDιĸ9Ԏ',
                            'ɏϚΘʼ\x9ecǈɲʹӼƘǕđҐĪ4\x8bΫӄ',
                            'Ü¶ʑʝϕ¸Ĩ)ýԂ҈ȇόԗʧΣŻ\xadԄɗҝωӅҼʰҁ',
                            'ҽͿќșďǤˬùЪǾϽưСʯҪƄĂʌд˙ŭΡŁΠХŤĀȡzа',
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': 'ԊӮɩҞвǜ˒ЗůɗÓʗȉÁpљѨҵΫƧȸеϜɾɎΔɔĢʝɠ',
                    'version': [
                            -4864413602905531961,
                            -2125981856817365837,
                            -2205226107184536738,
                        ],
                    'about': 'ǺБИǮ¶īƺɞȂűÆȊѭʟǜŦÕρȄϝƒÜFԅǼ\x89ҊŅƴӍ',
                    'description': 'ǓϒƑ\x984Ϙ˕ŉ«ŸӾĕ|ԋЈѐЍȲʨҺѢʴÃɜŤϥŊԮĝˀ',
                    'authors': [
                            'υԓ˗ѺƈґƠĘAʨŏŷyλēɜҰχРǽϸaΰіɬ΅ɷȥЬФ',
                            '\x7főɯӎňҶѺƌДțҠǩ;˼ԤŉφҡѣRŗȫƠèЎƤӭƺЁϯ',
                            'Ȧɴĩʍ˱\x85ԮǠƉɒɌӡǏľˈ/sĐĊͱʍ˲НϤѡɒĤM=ӈ',
                            'ɽϊγЪёΤŸØлĝʟʇʁΦěɢȶϪӲ¾dϮ)ľϓŐƛĉŉˏ',
                            'ʽmѢ@Ɣ\x83ԒʣȰˮÑºì^ƼɈȺѪǅϘɊȄǅ˙ʇʃβȈӷΥ',
                            'ò˱ŒҐ&ǁĎKԚŔÎ\x9bČ\x88є\x89ǷˢҊɫȋҕЮ^ԃҴZѱˆq',
                            'ȇʹ®˷ċǘҞҗɖǯ˾ěЃԥϕ.ˁȒϧĲxӡϤЀϗΟφȝ\x97÷',
                            'яˁӓŕЈԣ\x99хΡ²ќƒȩ҉ѲèÊȈɣʕȪΦЗJѐӺȋǋǘ]',
                            'ϢϷ҂`9ˏïӴɄĨζŐ\u038bҩ˄өȷ3οЖȒўňnȎ9ԦƋēƊ',
                            'ɡʐŊÏϡξŪǍ|ɶǤ¹\x91ьōтǁӀȉŗǂĹ˺ԐɜƒŶ\u03a2\x9fЇ',
                        ],
                    'licenses': [
                            'Fİ\x97҄',
                            'ĵЦȮ&àąÇŦħŒΣʄіҞҎĉԮ\u038bƗ˟ϧĐłЪȼʵǎʷʌ½',
                            'ʾҵҝbˈ˳®İ\x8d˭ηȲÄƝȪȢӓɱҙɥҿϑϸzӔ˫ϱaŸȎ',
                            'χɪΆͲ˃ѩǲвt˃',
                            'ѓƊґëȱǺС.ťҡрƉёҿ>ÅěзŰЙʝŰMÑŊŊʚŮƹƌ',
                            'яˆ\x85Ĺ\u0381åǻ\'ɗҒƮϤˠèɖǇkДϺΌєԃӽӦʯѿÁʓŌ"',
                            '±җɒÈӋƐӸ&ў\x8bƨɛÄӇɔȼ,6ôѓа%Äԫɓ΄ɺёҒι',
                        ],
                },
                {
                    'name': 'ϙГeˣͰЇԨΕѽΧyԏ\x91ҹГɹ»ȇȴȅĭ¦Àŧ4АƍӟϬϠ',
                    'version': [
                            -177801190387582790,
                            -6474866828586754965,
                            -2306577398269157175,
                        ],
                    'about': 'čΤǃľm@¯ȓȘǉǳѝϔhӿҐԨϵˉěƗĿϱɨΌ·Ҫːŝ@',
                    'description': 'ƱȦԡƑϠʊӌHŭăŷԅΰɎǽΡϜƩɶɣý¥РǏή8Ų"Ηѕ',
                    'authors': [
                            'ŌУ4OͽˋЗǽˀůĆŋǋˢӼÏ\x8cĩǀ\x7főɾīԋȢȠȯϽєã',
                            'ʘɐǲϸ\x92Ԛĺ1Ρ\x8bѵʶĀñĨЌκ\x82ǃЮΪЅÇ\x8bÃΓѕÂȩ˭',
                            'ȝγіȠāӚă\x98˝ʨӚҾŊ(ӂôȢǭ«ˇͲĴĂΗ\u0381Ɣêԗ1Ҳ',
                            'ɗWǕǘŎŭϔƐ\x91ŢǒÀʒвȭйȵčБӳǟ\x96TÕє³ȈҎѿʠ',
                            'ӣӠ¤ϗҥϾ/êɤĶʂȯɴϚȤұǗʩΎďҀŌĸűˣҙɱƪӲǭ',
                            'ҍ»Ȑ˺Ķøʈʿa˩¥ŇđǼ˙ǟ,ɛѴκĘ]ψƃæɇѷĴƷҙ',
                            'ԉƭɕ)ïǥһȨҀӥŉΝЭe\x88ĆøўǘȇЈQС{»͵ѵ˵Ӈԇ',
                            'АԅŐ÷ˁŐͶΈÍƘɢѩεɫuӆͳŷχĔƜĪàԨΚǏЯԝӻĊ',
                            'КĊцʜŖԮӤӷqUȇˢзƈuςwӺQїĻʖi҉ΰԏȩȼ˓ö',
                            'ɩřęˎį|ĭҲ"ӂɥҟÆzӀŵ0ӚǽΑɍʴͶӉΰƙǟųϙź',
                        ],
                    'licenses': [
                            'ăѯбđҺtӂѨӠ³҄īԠǿШɏ\x8cƑЮÿЧʶǌĹŕҿ˷ӎβ_',
                            'ЭçсˑӆЏxюӗàɒ«ӟǄʙѐdƿĶϒӶɕ˧Ĺ;ʹuσӐț',
                            'ӢȋÂ¨љжIНӏƘԅŽʳ\x91áєɭͲъСʐƐÏ\x91ӐƋѢȟ˓˥',
                            '_ϣ;ѦVУ,ſӸŜĔӔΟӺͲѶˡɍƓƊƎƟÄÝԪʕâƎл˸',
                            'zˌӹ˞ԠĮҨӲΩрɟӒҐ˗ȏA˾ҌԎ\x98ов҄îțŇƌǨǏΆ',
                            'ΜӘȻЂ',
                        ],
                },
                {
                    'name': 'šǫԅЕӄHʉĕǋ[ͷяхμŪņcʶϩѮ£\u0380ɓ²\x84Ĥˆҁƣû',
                    'version': [
                            -5533626214893779970,
                            -3019157523159291475,
                            -7720868267961702023,
                        ],
                    'about': '˳κЄƙіήϓҥҖώ˚°P(ƵψȔƧʹұнáˎ˛ғϪ6ѻbΏ',
                    'description': 'ΰȉʈɟȽҝэžñгҐѻ#ǺͳȅS«έһӐҬӏг¼Ǯ҉F[Ӑ',
                    'authors': [
                            'Ľϗԛϟ×\x90ӤЪĝӒӭҗƮҬªŭ͵˥çĨ\x8bȷ\x89ǷØҿˑºWl',
                            'âѣˠǛѾƫѓʋкΔǼӗ˪ҋѭǱʩϰҚžźҔʬƾǒ`(1Ґģ',
                            'ižšŵҸӀ[ŦΧǪюҭǋǠϱȩ2\u038dăɳ˂\x87ӹɭō\x9cȁɳŏő',
                            'Ĵa?ѤюɊϫɵπɒɖŪƦòǏƥΒˠɮїІβьÀпȱ:эΛÙ',
                        ],
                    'licenses': [
                            'Ȃϧǃ8ѹԋɸʣԋљʪƫлѫě\\ɇàHĳРӆǨĜәǝȳXдţ',
                            'αėȵͱ³\x8cҚɏ°Ƣ^ԣƹʌԄUĎņӛʿҪф½ѫ\x88!ǀӣƁ´',
                            'ɖ¤ȁѪŰҊ¨ѐ\u038dǦɬΉþɣŵŀʞƩͰΙǫѓͱԞɨƚîƇѪȻ',
                            'đȯȪљȦǦȁíǆɵşźˠɵTыΫӂɖТП˔¶fțȕўȼ;ɜ',
                            'қнӱˊӦΗĮőȋΪҸĥτʸǋŧƍ\u0378ɇ4ÎӺΛEŸƩˏūЎͺ',
                            '˞˧ˡκ\x80Јԟp˹ΕǐΕʕϫΨéфƔԙ®«ĳʡǿӮ;ĭЗUӣ',
                            'ǰǀԈɼÈňɰʊҵ0НʶZĎЅƢѓ]ʁN\u0382Ҏ˫ǔѱȰȻӈ¯Љ',
                            'ѦЍǞĩđϹľǳxɍwŶǰėƔ˄šƪơôĲ@ʙſҨľǱÒӘξ',
                        ],
                },
                {
                    'name': 'ƔЙ\x89Μѐӹë\x9b\x91%ώOʟдϾΣǲŰȒӋŒǽΕэʍɩъǿǵÖ',
                    'version': [
                            -34727814070619328,
                            -2142343044482780295,
                            -2137746139535070255,
                        ],
                    'about': 'оĩЀʭʢӆʍӜƠ;ίÐʹƾɞǤàúѯӾʡēǎƅɎʇО҄ϐd',
                    'description': 'Ҷӳǘύ÷ʂƧԢƮʦ҈ѝΏ˵МѤėҺfƸԀԍĄůƕʶцɧӬϗ',
                    'authors': [
                            'ţƎРФӂıƼ\x99ƵβͷυʸʩƂ˵ҔʱȃԞz\x82яӌɫґƵϬōʪ',
                            '\u0382ͷĖ=~ȪĲǍɆ¬ӒÊЭėÄΦМÍ\x91ϣȔɸȟE1ŀɐεȆψ',
                            'ѨɅ[ѣΦɰҁāԁҴѫӨʬРМʒȇŢʈŲƗäαǱĹ\x86ŇТėЂ',
                            'šΞŪ˧ѵԒӤǟ\x8cæ]*Į§ѼЪǑEÓɂAþŧɾĂɆɼ\x97\x89Ā',
                            'ͿǉÍȥӐɎɉѹЋСβǈļɁõςӿҩ˔Ł\x98Īϋ=xīȺҮ\x97ɗ',
                            'ƇʊȡȆϤάüȈƃλ¨Ɵӆɻɮ҅ƶʻϓӱχÙĩ©õľКҢ!m',
                            'ǇУНԈ·}ɇϲɅԝɃςαʤÚ\x8cɘӤüȟ˼њӃøύ¥ƿƔĄǴ',
                            'ɝϵȾϰΠЗӥΞѻӇ˘˪ӕ$у¼Ζƌ<Έ}Éĥõ7äïҏ\x97Ū',
                            'ƓЍƣřǴʸȷ3\x8bĨϏͰ×Ì¬ȏNǁʏͺϛŽƱўȋˆ"/щ\u0378',
                            'ıʋǧiҒүѪŀǂԔ=XѮΨ¶ӘȆȁ˱ўùсʃŁń',
                        ],
                    'licenses': [
                            'ԃn\x8fқˇŜȘϚqʷ\x93\x96ӈWԨɋơÕƌGėЊԭҧŁ\x85ʸŐӦҘ',
                            'Δ҇ҢıȡƼΌGWȐϹѸҖ˦ΓxЛɷΜΠɻǫΥʸūņʢQ˺ȱ',
                            'ÍϹʒȢѤіìɏ»ͼȴРʇƛĤɼ˼ӅʛƛˤʢưҳɗȝǑÂ\u0382ϔ',
                            'ÈԐҽŀ˓ϓʚǸ5ӲΒʡɀӧǕЋÝͷțgćbόɫϮ\x83',
                            'Ьκɓϳ=ΥĘѿƵķθЖӝșϮѷӵɷB\x87ŇӶȽɇĊоλ˩hɃ',
                            'ÈӎƤҡȓ|ȅъȻ\x95ЈưɆҜUɩƦɈțǢˣʶԣÿŝɈɻѠŃБ',
                        ],
                },
                {
                    'name': 'ˀƶʑʹȪԎɜƣțӇэЯҭͼʯÿѤДŻŰĲΣγӆǛd.MZϩ',
                    'version': [
                            -210393089873211783,
                            -780545658528519044,
                            -6112223369752796224,
                        ],
                    'about': 'ÎɨϹňϳèчſǃăTҿſĻӟʦ\u0382ϽǐϦnҋɨʼȭƚ*ŀð÷',
                    'description': 'Xƫѣ$ƏȃεɁǫ\x8bҚćΎ\x9bɢɒʍϙſŃɇ\u0381ɱ˹ԀǇҿθˠԬ',
                    'authors': [
                            'ȉ\x85șΙYňƱӡƪЧgǋҁʌŠѶϘÿtѽEӚΡҏǋNŬˊлϯ',
                            'ȮǣӀ˒ȠĠЧȹŠÍӍҋѳŻǒӬɪìҷ\u0383ґӥƸȔ2ĽӯŎʵĀ',
                            'ˑƷʕǝσʏѕʙðђҍʌÞ˚϶Ҡϥ¼ҖɳÕƋȻŖıҬɁʪǃą',
                            'a\x8bɼǨŇȇſѾӉȍʷΰ¬%ǨțʗÏѿӢͽʮƉώԔĕÞʗ\u038dϖ',
                            '˔ÔѹЋʵƪɃLǈİ3ɿ\x8bԂҢýԈͲ¢ȹ1ʾģĊ´ȑѽȃğƓ',
                            'ǿȾ\x85ʤŎɼʀӃӆΙќпӀԬϐ1ԆϖүZϟǜǵӅҟ˝˅Ȯǹŋ',
                            'ЂĉѕͶvʘşїϻɎåʕȗˀʨȮУOǣȐŖ\x7fȃӉθɼ-=ŗƤ',
                            'ʈҫѶзːºʧЦƿƫŎŶύÓрȫƓęʑȭ\x90ө˖яyˡϥˍΝԪ',
                            'қņÌȞþʣҽԘ¸ϷPɼoзӰͼɇ˱ϮӹԙԇŭΜͼʷφɓͽĆ',
                            'WʺɃӆ\x93ıɂˢȂĹрɕӗ\x9bǄʄҼːӮƃťwɻ¶ČҮцȖ˰ǝ',
                        ],
                    'licenses': [
                            'ŷʣǡѱâзˣҁ\x96ɒԦŭǴʣ\x89iüêӥӁӾœΝѧɇСÑȥˠƄ',
                            'ɃlƋbϴʘǑ=\u0380˛ЊŰɌİђӇ ˂ʚҨҮыԡζ\x87ÜԆҔӺГ',
                            'ŲӪ˳\x87ƌϻƚQǈƗȑӃƜҎ~½ȃưʀԎǃJЩΧĒşԔʈӋǾ',
                            'ǝŮԑ',
                            'ūƊȊɛɬӞԌоƄѱǕʺŤ\x9a\x92OьρԒÉϩƀɄ\x97ӪѭԕЪˡĄ',
                        ],
                },
                {
                    'name': ';\x93А˦жб»Ω¬ǁƇɷ˛\u0382ӫ˭Ɣ;\u03800ªԬҷΞɤIьʇЮİ',
                    'version': [
                            -7730157325103710788,
                            -3713637682174538475,
                            -7140849796032756313,
                        ],
                    'about': 'ΒԚҚɇύҠԑӵƘŁ¹Фӏ0˭ЁˣµÞɖԊįFȷvŭҧɽÓɜ',
                    'description': 'зƆƈҊЅĩԝȮ2ǡ$ƩȣĶó©ɺСΙӈФӕԢˑǇȼёΕɯŬ',
                    'authors': [
                            'ŝӫϧɠά»Ņǳ\x8cʫŚȢǺłРѦ\x9eοϺįɑţ˝ԒͺƍƓԎůҿ',
                            'ɹЫΫΑГЎųǾϼʶ˖ϻҨʼQʲώȤ˖ȁɜǟ-\x91¸Ʃοȱ\x90Û',
                            'ķɭVǼԚҒ·Ĝ\x8esҿԡ϶ˀĠѣȼɃǔĉУӰəͼɛłхĻđӝ',
                            'Üȡņӣ\x9eʇăԡoƸ¼»λΆҸСŽĐϿƱΘǐӋԠϼѣҷƉμΗ',
                            'й0ˈǔwźżԑЋЯʭӝВȍӡũѥ˥ѮΒѭљюǆƶƠяШԔÝ',
                            '>ΞɲѽˮǡӢáŬХƿȈ˭ƃѦǳýÇț\u0381uåŴиƘQӛ˾Û½',
                            'fѩ˥ԜʜčμΎ΄ҚɨǽϲҠyҎʃүқƚ˲бʕԧ6ΨөÂŢǰ',
                            'ϿåʏѪʪ˖ʇϯÈ]ŕƠƫЋȊŝ|1Ϟѓʣő©ЮŹǤϺǴΧĂ',
                            'Ă˱µѢƝʶΌӊāƯπќϟgΤҤ˰ӊθ3áԚʡ\u0383ΥČͺÇϏͽ',
                            'яѴźɻǅ',
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': 'ŬюƣϹpʐƬɎʂÙОԨ#=ɽȞɸƷȺИНәûˁšƙΜɹȏǺ',
                    'version': [
                            -8359977438537366207,
                            -2992876098318884211,
                            -3358804387099750094,
                        ],
                    'about': 'ƎʏҦɐȲѲ҄ǎǡЅЎȈћõƭėȹ˧ɕʒáB϶ɬьɸɹЬʗɞ',
                    'description': 'Ěίλƭϭĭƒϊҩњˑу\x84ĥĪΖα;ԔѱİƥυșɺӨŴƸϢҸ',
                    'authors': [
                            'ȝϼeƁΘʏŚ«ɿˡіžҋҀĶʶɦŕŭϊ\x8ffĞʼƎʙӅĤЯv',
                            'ҍʺĎ&ȕҪȨɊˏØǤŬ2ʇӝȋҡ%Ȏ@τɺǜʤ˧ԬÌø\x8aέ',
                            'ћЬЮҥϦɑΫȔɌɨŻĿӁθ®ʓЍϠОÕǹZʭǻıћЀ\\рʤ',
                            'ӫʕǮŲųƲӜ"˸ŪЪϨнǤ˳ϗåҠÊϸ\x9aēƘёČuɺèˀĸ',
                            'ȡ^ƘĜȒ:˙ȤҮqɡĻͽƭãϼ<ŗͶ^E¯ҭÌŠŗѡĞΊ\xad',
                            '¡ώάӿŞȜšŋȝϑԀĩĜԟОÙУʴӚĆĪɭɃŽ˦ÏáҬϽΥ',
                            'ѠöЙ',
                            'ȐӒѐ˛ҕʤļǒʓϒÀ҆ʇȿˉȡƁȪѬɱƭD˷ϝǩϿfǘVφ',
                            'ʔ\u038bɁ˴7ϨǦіúΩӵғѬлҙçʌРӟʷŒȰǣʵԏϴœǧū\x82',
                            'άЏ˚bҁƅˬѸҩƀҽϭԨhʩƲʉψǹºÀѦŪЫƀPčʇϢƏ',
                        ],
                    'licenses': [
                            'Жțǳȳ\x95ƿҾԣρǤñӼӺǵҘǨϦҎʟȴЃ.ƜNӨĨȱԢ\xadƤ',
                            '5˪bӑ\x8cȖÀӉv´ȫГЯӫj҈Αʸ˵x˽˯ΞӅʞԤŢČԝ͵',
                            'üһЫƲȖɗҸЎԤǋʿҫɺҠӯ˳х\x9dΤǭǵюʀsΊӖѣԉJȉ',
                            "Λѵ\x92xpPϪҭϧɊģΖ'˧ʕ¤ľʹѮ˃ͷԎԣýǷӭƏτǯˁ",
                            'ʸӗ\xadb\x93αȍɵӋM˂ҞŌцυѩħȿʴ',
                            'χ˴ąτƫҷЏѡəƂ_εЊҀȜʅʇ¡KҰ˕7ȬƙӹΝ˻|ǬΤ',
                        ],
                },
                {
                    'name': 'ѭӋȫɪѺÕŁяȷлčĦŕϭӹĲC<ǠЎҬЖƛłŚȕ?ıɦ˒',
                    'version': [
                            -7657039167810328803,
                            -8912990619751599859,
                            -144606482017225129,
                        ],
                    'about': 'ΞŴ\u0382ȣùԗ^DŸџĖçԥȈōvŪъǘ®ćЩĽƛǍƯбӹΫ.',
                    'description': '˒˻ԎƟ§ѧīөɌˆÉĉųӸДĞѐǈϋǑȼ\x82LčѶɆҙŅǛз',
                    'authors': [
                            'νϹȫ-ϔZ˄ϕԂ°ɷ³ҹσYʫý8Ӟ47ʸɭϼƐӁÉ·ϡЬ',
                            'ː¯ƎҝđԖɶΨӖ7зүŃQѡʤı;В˸ǹƒѿԋт\x92ѝųӂů',
                            'ýӴΧƅëĚÖйļ˘ЀňˍϨĳ˒Ѣ\x86ϳҥΡƨčĎf\x8d\x84юƷӆ',
                            'ţwЊϓ<ƮǉœДoSJԗΞŅңѭХƴÎБϲҼǙΒăϛϷʇϸ',
                            'ʣΒǊω.éŉę\x85Ѩ˖ʔΜŃάѿĽȠӡҀË˯Ӯu~ȍĈǲɂғ',
                            'øϭӧӑӄδ¹Цϧϖ\x9dГƜ;ҎɥƝӛɔp.ʽΕʄφMōŷƚƢ',
                            'ѩ\x8aҤʆϞ',
                            'AЇψ\x7fúʡǩϕĊȑʖӰϰĶ~ҕЪқ˓ԬȢǲ҈\x89ŀĂӺҽzʖ',
                            'ƪӼķлНяҁőǡϩƁŧƘѤĔͲӽԉdȒ˅ƹnϲǴƬĴȓļӃ',
                            'ҲԒķʮӺʵªƢβǩӏāЧӵκ˅ƇϞÄʹɫѴ˄ˉʻϥ[Ϫƕԓ',
                        ],
                    'licenses': [
                            'èĆɀÒӝё҉ĮʦɩơǴ\x9b6ΆϣˌʾуԇӃыʳïƧŘȱøƩϦ',
                            'y¨LѧΞȖí¥ˬtѬOʔɢʪǔϧІëĜΞÂҽгʍϫƛǯȤƺ',
                            '˺\u0379\x8dχÏĞѿнӥ!˸ɺĆïĹŶɎԅĔɋŀ©ɼȑӱȩ§ƅѿǑ',
                            'ǧҷƄѾ҅ɪȀҜԁӎĝǤϥѝƉSɖ˒ʊϻ¤άѡŉSбɹyЕÇ',
                            'ÛʆāѦğɗәʒɚƧʥɓԨϞԑϕҚƘǦġңǌӦɶҳҦŎԩJ˴',
                        ],
                },
                {
                    'name': 'pЭìɴԕnҚǅÍî÷ȬǴΥЬØЗҔφEңT˳Ɂť\x80ń\u038dvĶ',
                    'version': [
                            -1739621668550267927,
                            -1660481678936371866,
                            -9177190484470451792,
                        ],
                    'about': 'ĠҫΠϴgų\u03a2ǂҢķ˗ЎÝ\x9eǥƌŘʂҭɎȜϳα҇Ǵħш˜łć',
                    'description': 'ǊǴίˈҖƏċQƄʏįǹǺǒɎ˅ϵɻǔΨɼMȱγΈϿѥɢʡл',
                    'authors': [
                            'ӖȉǾԗΌƂŁϙϮɎɟәʥӂʏԌʞĻΛÞĘŠʄǰ˖ПˎğρѾ',
                            'K˹ƫąŁȕΘəNĀƺÙüӌʎƜìɴťz˨ҷΞѵ\u03a2ʯόȬɸʳ',
                            '¼ҋːγ҆Ҩїѕ',
                            'ήʛƬɩǬÇҌžӪͲϲěʼŝȂϞɵBϒāȺωӬɪɊҵҮW˗ŵ',
                            'Ƕ\x8aјZѐʌ~ӫУʴԉӆӵǝ˴ԟƊS˻ӋѿζͿƧӫıĐƐĽʽ',
                            'ͺÄҺǈͽВԡ_εÝŅԅʎРT\x9bΗҥϲ˰ãӲѰϨ',
                            "ĎŘ'<\u0378ȥŜь",
                            '˧ҏéÛγͺΆÑͲʽԬîͽӬǬ˦Ŧӵ8ƐѠԪӆԠέоȚ§ƙƟ',
                            'ȑAҌξ˝ӃЉӱöʾΧ,ʦɒž',
                            'ʣňɳȩЖҠȹvEłƬӬē\u0379ʹҞœʭHvҍ·ŒϕŨԮϒIϧʵ',
                        ],
                    'licenses': [
                            'ɹƽȉĂ:ȟФ҈ӹƗћγơ\x8ařÞźĻԟωѰТΞˇʅńǳ\u0381фN',
                            '\x81ǼƜзԦʤŮӇǁϝǇʯȤóӭķϪѓέÕɭѥƠĊ\x95ʏϑˈƵÍ',
                            'ȳϱӎ¼Ϡ)â\xa0ɂɦǢ?íШ˃ȥӚȽӤʆɭӁЩҾ&v[ʱϵƪ',
                            'ό*ҤĖ¹ԘСІ\x9dt˰ΡǎϏѶşБČοƺʱNҲRӑÚé;ϥ҃',
                            'ͺЄǶÊΎþӛĵʅύģѮÞԆĿã¯Ӿω˒ÉƌǤ¹ĭ\u038dŌԫƃǽ',
                            'ǄƭǃŸԀΗѼ\u0379öȊɌ˺ˇȴʫʋ͵\x81ǸhÆԨɎīȦ˹чΤԥҦ',
                            'τЋҢΡ]кʜϾǳύTȠā+ʝɇƚʛƝМϨɤY¯Ƚʄƛ\u038d`N',
                            'φЂǛҙ\x84îвǞ,біΑԗ\x80ѷʡʙѱȳ0ǡëǠɔԃԕӨӰń҉',
                            'ҴИӊ³ƙш˲ȚĎǛǏμĈ>ҼҖͳǈԪƎЃīϬŜƮȤşӥԩʌ',
                            'ʇƿƿ!ūǏŨĀҷėќȋѨӖˬʽ˩ѪÅ˼Я˕ԉ\x84ƈ]Ėʂpк',
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
                    'name': 'ĞɧŢ',
                    'version': [
                            -2732892738502283730,
                            -555168211943665933,
                            -6413800347570249318,
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
