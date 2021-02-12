# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-11T17:55:50.416272+00:00

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
            'locale_code': 'Ʊϰ¹',
            'catalog_name': 'ȭ.:ҬМѡ\x7f¢ƧΒχɡѸƈ]\x95ˡʇ\x886\x83ӮЛīԝ˪Țú˅ы',
            'message_file': 'ȫԞ˪Ӳˣϥ˼ǮǤԆÿϦǤɹѾŅǞңõ˵ӎҚ<¤ȂӥӫŰ)J',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': '˅',

            'catalog_name': '΄ ¿',

            'message_file': 'ƶò',

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
            '$': 'Ӵ\x8eƢǵǧƲàɧʁЂǘЭДƿŽшʓěΦ#ήó$ϿΈϓɆϵ\x91I',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 3466967115009274311,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 866116.7655806236,
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
            '$': '20210211:175550.301529:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'бΏЗӭʺ¥Ŀ˽ӍϩˌϬȓϊƳGӮќѧǣaõjԚԆ˹ïӾўϊ',
                'ѷżчԧκΐǨ;ίōҽ\x98ǰŵIЯêĺÅ!ʣǱ³ǾàҦҹЃЖͶ',
                'ϭĖɘϵҹYӈǀȡ\x8b˳ѫAö\x8fϻSƔÒӕȗɡѡĎӆɁǫ\x86ƗϚ',
                'ǅӚϾҏΟǘŚíŉɷӔҒ>ͱĔЅ˻ĴŇɏнϾƌóͲŶ˭ҳȴƭ',
                'ͷǀɨЁɇϖYɲћʢȨ!ӭŦͽ\u0380ҾӿMɓɴϪŽΪκˬ?°ʣ¬',
                'āҀ΄ю¿ұԓӼǚ\x87˅ƿǹčҤҽÓ\x99\x93ɠϥǚЭЄҼ˸ȱīʉ8',
                'ȭӓÇӘʆư ŮđҭϘǹƷƋґŖʖӸπȮ2ȶ\x89іԀЎβ҅λш',
                'ĤʩЇ"Λ´ʑ\x80Ӊɜͼß%ŷѠѳȏʹēϊȵˋ¶ ħƲȋǩŭί',
                'τ\x7f»Ĉ˾\u0380ˁцӬѕǌŔŰ\x8bˍȒʶЩƺœѭűƂӤǥȤҲѥΰ·',
                'ϖ\x90ƨԨψэ҇ɀ˵ѪĀɋ˚ǟĻɧ1ӦТЦφΈΝқȐҁѐºʧΣ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                3703168653244511000,
                7897499296397950214,
                4499060969464444017,
                -167514221212592066,
                -7645245465267742024,
                -5228379664320167048,
                -1531791056305922498,
                2981985510505083825,
                -1801022995448410189,
                2727838630340114186,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
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
                '20210211:175550.303748:+0000',
                '20210211:175550.303781:+0000',
                '20210211:175550.303802:+0000',
                '20210211:175550.303821:+0000',
                '20210211:175550.303840:+0000',
                '20210211:175550.303858:+0000',
                '20210211:175550.303876:+0000',
                '20210211:175550.303894:+0000',
                '20210211:175550.303913:+0000',
                '20210211:175550.303931:+0000',
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
            'name': '?¶\x91τЋ˥ŪӧåˠͿЏӛȲȑʃÔҬ',
            'value': {
                '^': 'int',
                '$': 918285413477930122,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ȋ',

            'value': {
                '^': 'float',
                '$': -65600.75191829946,
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
            'catalog': "˽Ǿ\x9eŠҖúпėʿԤϼяʭHÖȯʥԠӦ'ȨǓаζĚԠɡҐǄŔ",
            'message': '4°ΥʥĜĹѳӸӛѰƹœнσāƚӐʆԄђɥ҈ԁЉďқ1ʨЕё',
            'arguments': [
                {
                    'name': 'ЩůЃΪҷϓѤρ˄ȑσȫƵҬСA˔ǜӛϓѵҪ˵ΟÂ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ƺѻǈăЫƲԄӢәŲӟq¾ӎaΠïåȟΓ·Ԭă',
                    'value': {
                            '^': 'int',
                            '$': -5677074507161111079,
                        },
                },
                {
                    'name': '\x83\x8aԛʘǗ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ѝͳĎɕʨɇʉӿһöѝɁȘ\u0380Ӝβ˯ӼĆİϟæý)ʼRЈϵəÞ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        False,
                                        False,
                                        False,
                                        True,
                                        True,
                                        False,
                                        False,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ĄŚҨңɁϒЬǵ˥¸',
                    'value': {
                            '^': 'datetime',
                            '$': '20210211:175550.297115:+0000',
                        },
                },
                {
                    'name': 'ƦϙyьӬή\u0379ȩχ\x83Ѯ³ԚĹaӾġʴ˓_ƨTϢоʝҠě9Õɓ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'äȧԟ>ŅʼЄ˘ӶԞΣɔȂԃŇĠûǾǜƙӨëȒНѹțѯӇϒϽ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210211:175550.297630:+0000',
                                        '20210211:175550.297658:+0000',
                                        '20210211:175550.297666:+0000',
                                        '20210211:175550.297672:+0000',
                                        '20210211:175550.297678:+0000',
                                        '20210211:175550.297684:+0000',
                                        '20210211:175550.297690:+0000',
                                        '20210211:175550.297696:+0000',
                                        '20210211:175550.297702:+0000',
                                        '20210211:175550.297707:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ҏДԨǇЌˀĿ϶î¬ˈΝҏƽƄ½ҲȄѼ¨ɕŔǽʆƾБµЖēʥ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210211:175550.297987:+0000',
                        },
                },
                {
                    'name': 'ȏĔŠΪ˜҅ͻdÓϨCbΰйˮîԊӈµҳӑȊ<ï˗¬ҠϪϠА',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'T˪ȧ_υ-\x89\\ˡˢƅԫҬΨΗßϫѧăǜԖӅШˋÊŨаɥҜʲ',
                                        'ČɞбΆˬЇɞΌǪǕ҆ЈQ\x85ő|ȞҲԋͱΠ¬¤ҔǱJϧѠђG',
                                        'Ү·іƷƓǚ_ȭʶϕƪ`ѷˢƑțɔƥТɟРŜ˭Üʨ˱ɄWƂǕ',
                                        'ĖǁƯϢɮõϔ¸ϦӶǋѭτ\x8eΜϳĭΧƹǮɞǸ˜ӉCŠЬƇª·',
                                        'ɳҚǄѨӯɒΆąѲҍƸѵfʿһǚûŧͲ÷ÿїȏɶӎԎšňҞӯ',
                                        'ě*һíԉļδΝхCЁſХɠϦĎϱƆзaԜxѹɜlŃʪ҈Ϯ˕',
                                        'ʓbΨƾͱςΑӮżȸζǚßŖ7Ϲı\x94ˋϜBљrŎɟƧ\x90"οȷ',
                                        'ϣӆү˓˧ƴ°ϵƚ¢Ȓ\u0380ЯĞOâʜ\x7fѓԘųӗˁŹʋʊԒɲӐ7',
                                        'ĦӍӸѦʩͿҜ\x99pԇ\x9eɩÀуԘlӄĩ˷Α¥Ͽ>τʻØΈӬɠ³',
                                        'λ\x82зёʮ3,Ŋş\xa0˺yɸƐȽ¸ӯʅөɹǫfƃγĺнӁΞǨɞ',
                                    ],
                        },
                },
                {
                    'name': '\x9fl΅ďľЩѪŬ΄ԕȜʋæğ;ŗҦɘɥʫqёɓñĶʤƋƁʕʶ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210211:175550.299655:+0000',
                                        '20210211:175550.299690:+0000',
                                        '20210211:175550.299711:+0000',
                                        '20210211:175550.299729:+0000',
                                        '20210211:175550.299748:+0000',
                                        '20210211:175550.299765:+0000',
                                        '20210211:175550.299783:+0000',
                                        '20210211:175550.299801:+0000',
                                        '20210211:175550.299817:+0000',
                                        '20210211:175550.299833:+0000',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ƀӭ',

            'message': 'é',

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
            'identifier': '×\u0382ԁҸȒǑǻ˒p҄ƹđ7ĸԮ>\xadÚэȂ˭ƾȔυϽ´ҢLЖ\x95',
            'categories': [
                'file',
                'file',
                'access-restriction',
                'os',
                'access-restriction',
                'os',
                'internal',
                'file',
                'file',
                'internal',
            ],
            'source': 'щԛïӚºwʤǩǪʩȁԊʪJǇΐƑĺ\x9d\x81C:\x84ЖʳÉÓˮÏю',
            'corrective_action': {
                'catalog': 'ǾӲ',
                'message': 'ÉđþҁϽĵ~˽ѲѤΙ·äѯȯӆ\x98NΫҸ©ŢvĲУϔʎǩӑÛ',
                'arguments': [
                    {
                            'name': 'ʶáǕѷKрFƕӉʫѕŐǗϹǠͷËõϘĦʛ\x96ӢǓϰȶθӥЁ',
                            'value': {
                                        '^': 'int',
                                        '$': 2051814220206427869,
                                    },
                        },
                    {
                            'name': 'Ǖǳ˚ɡϕ\x90ŅǺӘѴκǯΓƴӍuŰͱӺԬØӻɵҳˬȬѫŶԣ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ȾӮΥ\xa0ώҏ\x92ԢҨž½ԫϵԝӈе:ɏĔτʤ¼ȷĳźЂ5ȚӮѰ',
                                    },
                        },
                    {
                            'name': 'ѠŬȘѕίңӾYŶʍʼԫЮcɆȱˮӻӨΕ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210211:175550.291689:+0000',
                                                        '20210211:175550.291737:+0000',
                                                        '20210211:175550.291757:+0000',
                                                        '20210211:175550.291774:+0000',
                                                        '20210211:175550.291789:+0000',
                                                        '20210211:175550.291808:+0000',
                                                        '20210211:175550.291824:+0000',
                                                        '20210211:175550.291837:+0000',
                                                        '20210211:175550.291854:+0000',
                                                        '20210211:175550.291873:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ȧˈϲ\x87ĩԣҮʙȔʬƫϗȨ˶ȢȬ´ʸƬ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210211:175550.292416:+0000',
                                    },
                        },
                    {
                            'name': 'ĳ«ʇ\x98ȶʷˎˏѽȳɛӌϮͿ·_ŭŚƘҡȟμԨƉȵ',
                            'value': {
                                        '^': 'float',
                                        '$': 604336.5475162494,
                                    },
                        },
                    {
                            'name': '\x94&˷ʴǼԓƅ÷ţčúþ{ʤӫǊǾɯɽ\x8dȫȠӜƅԞ\x81ėƴLǻ',
                            'value': {
                                        '^': 'int',
                                        '$': -6404967797453157504,
                                    },
                        },
                    {
                            'name': 'ęȰʒ',
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
                                                        False,
                                                        True,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ŀщҲʎǌѢɠƹʐϼԙêǖ<ʀEӻϒӕȴȓǹƗԜѾŃМ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210211:175550.294530:+0000',
                                    },
                        },
                    {
                            'name': '8ąЛˊŰ.ƌɱȭѩȎΒſ\x80ĕΟˇȜɆEʀǠ ɣϪЦ°½ԂƧ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        959806.086687845,
                                                        237484.27130412875,
                                                        390327.5368913964,
                                                        190557.61451793177,
                                                        262810.33405182295,
                                                        612448.128685903,
                                                        379316.7204464278,
                                                        555530.4349790968,
                                                        822048.9498733891,
                                                        315403.00226286374,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ԪҖӣĉʭŠǅƛϕӕ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210211:175550.295445:+0000',
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ЩÕԗȵ˩đƪΫʘԆҌΞ˙ЙмҖξҢιΰTԨωǖўнěƹɸ\x8f',
                'message': "'ˁі҅˓RˋνсƖʕ˼ԍcƶ°Ӵ¿ӲÕǷó˩ѳZŪɱКȗʒ",
                'arguments': [
                    {
                            'name': 'ǩˣĹʔҍˮ¸˺Ü\x87ʛ҈ӷВӳϽ˳Ç^ӘȢҚӣχŷȳ<řЖĄ',
                            'value': {
                                        '^': 'float',
                                        '$': 564079.5191751334,
                                    },
                        },
                    {
                            'name': 'ѭěгЕǉӞśϟđъɽѵƩһΐSȄ˨\x9eǚʓĳǟ\x97ģНӳ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210211:175550.304949:+0000',
                                                        '20210211:175550.304983:+0000',
                                                        '20210211:175550.305002:+0000',
                                                        '20210211:175550.305016:+0000',
                                                        '20210211:175550.305033:+0000',
                                                        '20210211:175550.305052:+0000',
                                                        '20210211:175550.305071:+0000',
                                                        '20210211:175550.305080:+0000',
                                                        '20210211:175550.305104:+0000',
                                                        '20210211:175550.305115:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'Һ˱',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        True,
                                                        False,
                                                        True,
                                                        True,
                                                        True,
                                                        True,
                                                        True,
                                                        False,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'đĒђΟƾ˳ȗŋõθǠƣƪѾҗ˽¶ԃѝȡ\x94ͽĉДǻʫÅФϺі',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210211:175550.306357:+0000',
                                    },
                        },
                    {
                            'name': 'ʔҔѭ}ԬƖÃѡJƺʰƜ.\x97(ԐâǰǂҴώŰ}ѤñкӰȱϫƷ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ƈϙăĜҫʧӳɽщ¯ʀȴҖïӲǖͻѢиʲзԭÜƞǲżǦȌĽΰ',
                                                        'ęȔ˼²\x93ƻ{ϞǱǾ{ҟШ\x97ŗɪяԋѝ)Ϫʕ}˗ÁŠYǿѮp',
                                                        'ŤѽǆȄ\x84ӮэĔʹȰƨǀʇǣÀԡ\x99Ο=ǞӇǟ>ѿʈȠðͼDӽ',
                                                        'ĐʐΖĸÙșʙżĦϠÔʘΐ˹ɻǐ5ĖәӃΗԐ\x81īΒ\u0378Ζіȭԟ',
                                                        'ǅԜ¥ʀӍɀŖȥӽϥȽŐˍ˒Ƴӟξҟ\x9fŗǬʓɴѝѼ˥ˈŰԞʏ',
                                                        '\x88ɓåǐίıxϴТCˬʿBσΟ\u038bρӼˡԓˆʢÊƄÞҫpƌӼ|',
                                                        'ԓȧɤÓѶXΗωҠ®ˁĀĳˀӇёʼ»˫яƶȽƉμόʰɼԟÛŁ',
                                                        'Ȟ˓ϜˌÀѦǡȳʊŗɺӕ¯:ҳħ7ŪȉĔŮ¡ÜÃèȎɴƟų˨',
                                                        'ԈϕΟʶǋϋǡ\x98ƨüXƊΒǞȺɻŏdГ¼ʇƽԐӔþѼΕӏyԗ',
                                                        'ǩɧЂȯ2ͱȘәԨԡɭӷқҾǷɡǝƪѓÅˍĳģԥԥ˄ǣ\x8bөĵ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ĥƳǼáĳҧōĦΎ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        True,
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
                            'name': 'Ǯ¢ɟv\x8dʱ:]ǙԉЌɪ˸zɔӱɺɽđϜĿӘǚ\u0380ʵЩԎ\u0381ћƖ',
                            'value': {
                                        '^': 'int',
                                        '$': 1464627529178106335,
                                    },
                        },
                    {
                            'name': '!Ǚȑ\x90ȲƷθо4СΥ\x9fϝ;ǉ\\ѥˡnсƚ´Ƀз˦\x82',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        425538318833546610,
                                                        2320201412358478158,
                                                        3461201876162584010,
                                                        -4677221819847304687,
                                                        -8703715741292522282,
                                                        -4585811263275453079,
                                                        1543783021653348501,
                                                        -3715489761275469325,
                                                        -2827868830053752030,
                                                        -1415521084113468880,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ҒŢȁςϥΟ#B¼фϻԘә9ŝϜϔțmýȉϞˎєȦĨÏџқɢ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210211:175550.310010:+0000',
                                    },
                        },
                    {
                            'name': 'gÊԏćͼœʆѴɣцҧ\x84ԚńȀɫ˒ҩMÓϙЛΝˈÊɷǪҵѮǵ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ĈηͻʚϽԕ«ʡǞӓ¸Ԁѹѽê;7æŲӉγҵǪѴż¥}Ӌ\u0379Ї',
                                                        'ӲʗŃǑԙЎƗǼOͺóªˑњьǱёΟ˱ˀƣД£ʛЖɳȅŜŎ_',
                                                        'в\x96ȒǜїϴҠĈ¾ĈΈƳɛ҂ʠÖȝʓÞǏ϶ɆǒʤȀѕʻǶƟǛ',
                                                        'ɏʈʌĪȞҊЏ/ԩȜˁƉԕ )xɢ`ųĤҎŵȎўʀn6\x9cƼñ',
                                                        'НưЋƮѯƃǵϘżҴɮȏ҇Ń¹˃ˤǡX^ˋȠ\x8exΰ&ɹǭӶǸ',
                                                        'шȆҶΝșLǲÖӡϻŪĲλʉŕƖʒıţ˙ǹԙӺÐϻŠ˔ԡȈȵ',
                                                        'ϓΙғѭ˞ʝԘ\x8eʹŚѾȂȽӾіēįǼƗĝ˰KԍǳίθԬʨͿΠ',
                                                        'мăО@^ɔϥӱԠħɷʛ˰\x9aʀåҧƝȆnÑϻѧіʟѫԤɴǮϱ',
                                                        'ԪΠşɹʭӼј+qÒӧLʗҕУΡңвèÿŖʘσиĩ\x85ȻǼȶѨ',
                                                        '˪hԇѴѤѭƢгӓĀüЅˇ3ɯԥЈԄʉɍԋɀĠȧϘǥυƼæǂ',
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

            'identifier': '¾ÓЋЫǃ',

            'categories': [
                'network',
            ],

            'error_message': {
                'catalog': '®Ɓ',
                'message': 'Ċ',
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
                'identifier': 'ˊìѩϔмƧƒŐϒǸğӅȅŦrÙȮΧ҄\x82â3ɿΤνϹǯÜґϿ',
                'categories': [
                    'file',
                    'internal',
                    'network',
                    'configuration',
                    'os',
                    'os',
                    'file',
                    'network',
                    'configuration',
                    'os',
                ],
                'source': 'ҊҢ\x82Űþ\u0378ƘѧÓΐϕłҽηÙԄɥӈϼѻ͵ȅƩȇθ˥ąy\x9fʎ',
                'corrective_action': {
                    'catalog': 'ɤӂ\x99ÏȃЄјĹ˨ƵӍ\x9aˁƊĎҴ˼˞í\x8fΦĚ˺ķ˞ѾËBɪɘ',
                    'message': 'ɐ\x8aƔуƻ(ĕďгŷūɀӾǌͿɗѝΦǀҳϚҠʨV˽вʨǷĂʦ',
                    'arguments': [
                            {
                                        'name': 'ϢʝEÍΑЈǇǗҺǆӻӈƻѾďϾǩȕ?ԛŗϒŉύĀԒưЬН\\',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175550.277175:+0000',
                                                    },
                                    },
                            {
                                        'name': 'őԦŕª8ӴϜ¿ǞůŪɦӶɞŐŉϜϴѰөԈϵҗƽˍǐӻŤΤË',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 894039.1816490403,
                                                    },
                                    },
                            {
                                        'name': 'эϡϥɛԡʍԥėΎϓӭÝњԉ8ɻ˥ѬД˄ˏфzņҧšʍʶаѱ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8717484520885281448,
                                                                            -7474440562241687525,
                                                                            -1727759586261231461,
                                                                            3760785404345815160,
                                                                            -4332025232967450877,
                                                                            9073827188535159493,
                                                                            -4864188219113037546,
                                                                            9176696085421866488,
                                                                            6988397124066073685,
                                                                            8396948212791634043,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԔșˡķΆƩǒΙѷϼ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175550.279291:+0000',
                                                                            '20210211:175550.279337:+0000',
                                                                            '20210211:175550.279353:+0000',
                                                                            '20210211:175550.279365:+0000',
                                                                            '20210211:175550.279375:+0000',
                                                                            '20210211:175550.279386:+0000',
                                                                            '20210211:175550.279396:+0000',
                                                                            '20210211:175550.279406:+0000',
                                                                            '20210211:175550.279416:+0000',
                                                                            '20210211:175550.279426:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ª\x80ӲӫɓϗɥͺEőЏϵ¢ʐѰːϵǰǼΊ¯Ģ-Ϸγ˳ӰЂԈƱ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -9107515476667525390,
                                                    },
                                    },
                            {
                                        'name': 'ˤ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175550.280258:+0000',
                                                    },
                                    },
                            {
                                        'name': 'âȴǲͳϟşǠќαѰǆǹ˲łǜ@Ы',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҭУΏІȓȑћ΄ϧϼØøѣB˹ʾþıèкӠŤƃӹίѴŤʸФѲ',
                                                    },
                                    },
                            {
                                        'name': 'ȄɤȠǂˋƧ»ɠˢ$\xadЏт¶',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -343319053163827301,
                                                                            -5507860405815372737,
                                                                            -1621537558611749281,
                                                                            -2634364550930494808,
                                                                            8419167600141161150,
                                                                            8319808286293773599,
                                                                            7858470555446240375,
                                                                            -2089669784329663607,
                                                                            -3321322878587422117,
                                                                            7890660207517083224,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȅэġǵǃљȳ\x8aǧΑҋΝӤʽěμΎʅȾĴɧҝқϣϦ\x91ƏҐΓ˨',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '\u0380ӳƺϼuФҦʵģWÎãӛЋǺϝΏĥȗһΚѧˆΎʍϒƚ˭äӧ',
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
                                                                        ],
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ф\u038bĚʸӈ7ˑєԌ˴ʋ"ʠìӝȀèɴΤɇCȊϭƻӴƨȜÀб\x9d',
                    'message': 'μʎβïɡŬ$ƓĊʆϢ\x82ðÃɕȉǥϡϸӤƎǋU҇\x89ͷуώČ˔',
                    'arguments': [
                            {
                                        'name': 'ύÔƼӟˣˢ¦é˫Ƌǐůӥўғѕ×ӦƔԌҴԍvũǵǜҧΖˤN',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'gҎвţʗȕ\u0383čÎЩǜSǌȴҰjʧԘˁ>ǑѰǉDΊɨ\\¨ѵͿ',
                                                    },
                                    },
                            {
                                        'name': 'ʶ4ˠǗӬΜƲΐǀϭĬεʄŨËΦ˟²ĸтԢʆȧsԟÞʪ=ҞԈ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƽkğɇYʛ˨',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "ùёҗѷȩò?ŚʽеʞōϢϤʠ'\x90É\x84»ϞοsƩϷԭŕŗȿȧ",
                                                    },
                                    },
                            {
                                        'name': 'ǄɓìWԢī\x90ϻӄƝӲ6зҚҿǠĭDԧҕ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '¼ɷБͷĪ˙ԪTƉɜţǷ',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЦϦŘ¡Ąѣø*Ĝŝ˭:Ϡɽ˸Ȋŀ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -18407.854671842302,
                                                                            234981.16402777453,
                                                                            979243.9269601235,
                                                                            150161.18752052286,
                                                                            539901.1749251253,
                                                                            811934.91719254,
                                                                            217579.40320936008,
                                                                            842666.0199601941,
                                                                            133184.93872166978,
                                                                            -72056.14063956928,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӠɶԨƉʬԫ΅űɒТПȅEʰωͰtÉ=Ҳ×ЬÅЏǂρE҇ӀǇ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4888343073683770008,
                                                                            6182521282822751009,
                                                                            6395150734773625361,
                                                                            -1821176573424652354,
                                                                            8216220570962843310,
                                                                            -8147877027447415732,
                                                                            -3307791518879621395,
                                                                            2766233962595398859,
                                                                            2210703231811881571,
                                                                            7403734175953097256,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӆ΅ѹʳЕlõϺħЯӫſҷ\x8eӊǥv$ʝҺĢǎ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 230702.51405639848,
                                                    },
                                    },
                            {
                                        'name': 'FѤʋ҄\x99ѬӲƕ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'KӞȤȭƖӋԒвʝЙ7Ԃ΄˕ӺΠʦ˚˼',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175550.287514:+0000',
                                                                            '20210211:175550.287572:+0000',
                                                                            '20210211:175550.287595:+0000',
                                                                            '20210211:175550.287615:+0000',
                                                                            '20210211:175550.287632:+0000',
                                                                            '20210211:175550.287650:+0000',
                                                                            '20210211:175550.287669:+0000',
                                                                            '20210211:175550.287686:+0000',
                                                                            '20210211:175550.287704:+0000',
                                                                            '20210211:175550.287719:+0000',
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
                'identifier': 'ǍǞӝȎ4',
                'categories': [
                    'internal',
                ],
                'error_message': {
                    'catalog': '\x9dă',
                    'message': 'Ĺ',
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
            'locale_code': 'ýʷ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': '·',

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
            'catalog_name': 'ӚʑčɠþԁПȗtéɴЇˑƢƒǋǃÞɴ9jг\x9f2ЧїǛŴЭʖ',
            'locale_codes': [
                'Ǉʼ=ӵӕ¹',
                'íΞĒԣŠ˃Υǜ͵',
                'ŲϺȳ',
                'Ə$ɦöϢĆūԊϚ',
                'YʷĽ\x7f',
                'ÉȊ',
                'ʩӱƠЕ',
                'ƟΝƢdʶý',
                'όƛ',
                'ǂϾАĒťʄмΆĘɶ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog_name': 'ʪёʜ',

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
                    'catalog_name': 'ʈÆѬĠӑ',
                    'locale_codes': [
                            'ӥɶ&ҀǌƐBω',
                            'ƻ',
                            'ɚΈ\x92Е',
                            'Ԛ\x92ϩ',
                            'ЏЈěę',
                            'ØͿmςź',
                            'ЛŪҩƿ2ϔǳÜͳŤ',
                            'ȁĨәƆҐŌ',
                            'бͿȝȌґ\u03a2Ľ',
                            'Ϸů',
                        ],
                },
                {
                    'catalog_name': 'ĨŇńϟѣÁQͶ\x82ǈĪ\x8e϶HƥŠЃŇɿRԒʼϐDFűƪ˦Ȗũ',
                    'locale_codes': [
                            'ΌɀҚCҊƓǗԤ',
                            'Ƚ',
                            'ǻˈ',
                            'ɓЋȘ×ԨĽĘɬԣӣ',
                            'ɾҋœ',
                            'Ҁȑ',
                            'ʨӦϻσϟƠ҅϶ȪȺ',
                            '˙Ӣƽξ\x80b',
                            'ЫȷƥԚɉ˭IʔѪ',
                            'О˭ϗϑƠӜͶЇԝΑ',
                        ],
                },
                {
                    'catalog_name': '2\x82ϡЂȌџɞΙЬŐɂ(\xa0˔ΏЬþʋϨƉ˯˟λÈāχzĩɦǐ',
                    'locale_codes': [
                            'ˇþ˳',
                            'ľԎ',
                            'ÇҤĲΕұĜ$ǤȾâ',
                            'ЙƆτîΘuғҩ',
                            'ʯ/Ӓ',
                            'įʄȚwӐ',
                            'Ҿѵ«ϔ',
                            'ϲЕˬ.ʦѡˑВͲ¯',
                            'ЉƾϜǃҰ',
                            'ɉǘˁуΚξ˟Ͳ',
                        ],
                },
                {
                    'catalog_name': 'ЭʤǍƁ˜Ѱ˗ĲŞѩΨӑǖʖӉԈɘǯeʙ¿ӹûȱŊЕЗſ\x92Ԛ',
                    'locale_codes': [
                            'żƞˁȁ',
                            'Ѫůfǜ',
                            'ɝĞ',
                            'Άˡ',
                            'ʳтфň˖^ҧ',
                            'ŔǥµȕЧԒ',
                            'ǐɀƪʟԝҙɜΩ˜',
                            'ҪѻӠѹįԅϥЌ˘',
                            'ԡǔÀЖȷďњЈÃ',
                            '\u038dã˦Ҳ˯',
                        ],
                },
                {
                    'catalog_name': 'ІǊӎĳÿӔ¹ӼƇʀƾĪǲΩɘɐȹ˭q\x98ƧЪҋҬΖǽPʤ˟ԇ',
                    'locale_codes': [
                            'ԎɄƏϏЇΉӤ',
                            'řГ͵ºоԟǈƹϖ',
                            'µ\u0379ӌµ',
                            '\u0380kШιˁӥƙ¾',
                            'Їʆˮ',
                            'Mƍ.ˉĕ',
                            'ȳɯԥŽ',
                            'ƍЄзƌ',
                            'ШƹǤ',
                            'ţѤǨĦ',
                        ],
                },
                {
                    'catalog_name': 'ȞϟΓ\x92ʤ\x9d˵Ñ£āˣқȱӻďǚҭɨΘΫï\xa0_ҏԇvsŐӁӁ',
                    'locale_codes': [
                            'ӃйаɐƩ×Е',
                            'ʵ˯èš˒Ȅ',
                            'Һ',
                            'ԘλήǛɓ',
                            'ŧ˕Ωà',
                            'Ø',
                            'ľÓ',
                            'ʢΪ˽¦\x9cě4ԋƦ',
                            'ΌǝǬѱԤ',
                            'қ',
                        ],
                },
                {
                    'catalog_name': 'Ńщɿ˧Ȱ»2³˱Ɲďқ\x80IыȂɾŜΠĖԘԬƀB˅¨\x9dέиȯ',
                    'locale_codes': [
                            'Ъȉǅ',
                            'ЉɔǇš',
                            'ǺǞʚƩŝкϲ',
                            'Ćԇ',
                            'ΚΥӘԅșΦǿ',
                            'ϺӬЫȋ*\u0381\\ÅŲӂ',
                            'Ӱǂ˫ό',
                            'Ϣ\x96ϧ~',
                            '҂ÊХϣϽ',
                            'ćҼºoɂм',
                        ],
                },
                {
                    'catalog_name': 'Ҩ˒ʽоԥÎԙɘǘÅƿǥοʜ\x9cĤŅĳАӱјŶkΟxӞˣ˾Ӭȇ',
                    'locale_codes': [
                            'ѝŅÆ\u038dТÚѩ¶',
                            'Ǯ¸ЀɒſŋґШЂ',
                            'ƞőƊïӬ',
                            'ħď\x81',
                            'ӴҍľQ\u038bТɸƯ¨ƴ',
                            'Љ',
                            'Ϯ',
                            'ˊɱ',
                            'ʦcä',
                            'ʪəƼҗЗȥʁ˰Ǯ',
                        ],
                },
                {
                    'catalog_name': 'ɚ\x89ӕϪÓƽ˰úɠʹȎ\x81άG˲ρWцϘƵӫĲүƼҳжʛѐόF',
                    'locale_codes': [
                            '¦ѭɮ˟ǗƓ˄ȟҟ7',
                            'Ω',
                            'βԡԞȗƜɻžĒ',
                            '\x88ԛǑLί',
                            'ғƯȅЍ',
                            'ѥΥѽѠ',
                            'ԗΚ',
                            'ɧʓǩƘðӮʇ',
                            'KԜɵϝҶ',
                            'ėѩЩϡș\x85ҏá',
                        ],
                },
                {
                    'catalog_name': 'Ƣ\x83ȝҲ÷ΣñuɈΞёɳЂЀĺΚ¸Ǳũ:QǢԊ\x8dȫǂǾǍϡу',
                    'locale_codes': [
                            'ĜшǓѦԚцѠ:ŋ',
                            'ƋѯΠÁ',
                            'ќĕζ/',
                            'өώ',
                            'ȲʪMɵưĭҚ#ҙД',
                            'zʴóϘǑ',
                            'ӖОұҬłGε',
                            'ƢςҝÈʂ',
                            'ԓ\x9b',
                            'мǺ',
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
            'name': '7ƬϩϏʝɬҜÿÇԔζЭͱ¤6ҳгԬЉc&˷Ǎў:ȉҳЦρ\u0379',
            'code': '´ϥʶã\u038d°ȭӭϊ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'q',

            'code': 'Ϫ',

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
                    'name': 'ψяÇŘƟЈɯɳeǌԫɥɪΖȯǬàҮѭ"xγʦʦύŅɼǶƑˆ',
                    'code': 'ϋǍʓ7ӅŊαȁ',
                },
                {
                    'name': 'ËĵʠȷԔ\x7fÊsOГ®īŚϜźԈ%ԥςЌȷăŒ\x83>ˀ\u038bƣϗĽ',
                    'code': 'Ɖ\x95',
                },
                {
                    'name': 'ɌЬ½ϦƅЪŖēυӦy\x85ß͵1ɃԠļԑɬԐƣжǀϽҢҹҭǬу',
                    'code': 'ǐɽưãЌʏ\x9f˛ϳ',
                },
                {
                    'name': 'ҿ\x8fΐ\u038dҦŹ˹^ΥҐ˸ÍҎҚҚŶϣЋϱ|QƢ\x99ΨʆőͶ[ӝÓ',
                    'code': 'Ǥ˘Ңγƚ˷ô×˙',
                },
                {
                    'name': 'ǷӕиçϮvӇÚԊɉǄάӔӑҗ҆ɟ¤ʌӈǕœρ\u0383¿aƞƬđӹ',
                    'code': '\x9b҉ÐĠòʧ$',
                },
                {
                    'name': '¥ϣ˅оѳ)Û+БΩ·З±ƶюəҎ½ûпƴá\x98ϛΌѰɂύМǴ',
                    'code': 'ČÀИÇÓǝ',
                },
                {
                    'name': 'ƎYɂˎƣʇ=Сɫ\x97˛Ŏɐŝс`ʠƿԘҲƚѤȈӪƊΙuБɣϖ',
                    'code': 'ɉǸɖπɄ',
                },
                {
                    'name': 'ԝ\x93ćҒ\x83ӊʶӞЛËįA íŌÌɱϽҸ\u0381ŤǡψҾjǍÒ\u0379Yƹ',
                    'code': 'Ʀ˨ЄſϨҿԊϛ®',
                },
                {
                    'name': "\x91ŐʏΚʸӳ\x8aÛӟ˴Ģɡľ҈ȽŊ˷ҳГӡˊЭ'ņΕƭ.ȦȬ΄",
                    'code': 'Ъ+Ȳ\x8e',
                },
                {
                    'name': 'Тӭ¸ʞВJʸfũŚЯƀυгɋ\u038dʊȷƤЮςԉnľϠ²υаǂʵ',
                    'code': 'ʰԁŕǥ',
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
            'locale_code': 'СшҠϟϯǷǊ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'locale_code': 'Ǽ',

        },
    ),
]
