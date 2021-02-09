# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-09T22:28:54.882929+00:00

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
            'name': 'Țёƶİ\u038bjʧɡϏ#ӉǭȌοnу\x9eU%ȈϏ\u0382<Ϻ˓H˩ˣʷo',
            'minimum_version': [
                -6418594934711382591,
                -715296489808329610,
                -7361717192072203596,
            ],
            'below_version': [
                -4412971638159671546,
                -4681385412495809831,
                -205343670913921821,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ҚԪљ',

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
            '$': 'ȿæѲΞH¨ĚžǞűϛɔˈƇēϟƣʫɆª2ΌΏɽҔ˖mʏ£р',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -322627304228994203,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': -83062.24676801037,
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
            '$': '20210209:222854.804257:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                '\x85ͿǏаΧҟгǠӴ¤QŦ\x96Ϸ˱ѿȍӻС\x91ЋȆƅʺ϶ԉӟHӅĽ',
                'ԘӳőÂĠÓϥʙ\u03a2ҍʹͰϿ_ǂŐǠӗˉɩǏȴƠϾʿˉԧҾӕű',
                'ґEp]ӂ-ɘϝɻɇПҫƥӴϼìѴԟʪԞ˰ГˮɿˉΤȤʡϠɖ',
                'ɡӆϏşƊќɂХ,ϿҔŭԝѺӱ\xa0ȪϼМɳԆҊЪɡ«ӄśØǔӂ',
                'ʮӤԊѥʪȿŚ˰Ƽ\x8aƨǘˈ\x9c1ӅъɷΊΈ\x80ȧЪdҧԨüнėɯ',
                'ƶʛԏǹɔðƼϢ˼kü\x84ˎýϦҽʎύÚәәƩ˂ÅЙϩȇȶЇ\u0383',
                'ğѳԥéÑϮŐ˂҈ϷȍbQӸʚƥƮΌăĤԮːċûӖS=˝Ũσ',
                'ƸǤoĵċɧȡѻ¦lσɜˠҸɠɟйǧjʰüţƆĘǖ˱ԕņ\u038dż',
                'ͺĤԝƥΧǸΓǮɨԤƺ\x90ΧƖƏѾ˟ʘĖҶśʎƃӅʠėˈ҂Рϻ',
                '˺ǸǚϪҞ¡jЭ˶ý\x87ѲЇƽʷʇщɚȽ˄ӯĖ£κˬɘϏҲԡ\x99',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                618488659443873826,
                -8760088466649673378,
                4298939753885737888,
                8590959401059532305,
                8736001781393419037,
                -2061016690817051111,
                7875814860043993567,
                -9033505044983861515,
                -7616625217602201766,
                6705212380029469134,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                630574.8587804765,
                12200.229383908023,
                878296.7351721134,
                110550.13939411496,
                152867.52947702594,
                2707.9766772416915,
                397678.938104062,
                811772.4109088548,
                974218.9541662345,
                10246.393800085745,
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
                False,
                False,
                False,
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
                '20210209:222854.805187:+0000',
                '20210209:222854.805204:+0000',
                '20210209:222854.805213:+0000',
                '20210209:222854.805292:+0000',
                '20210209:222854.805302:+0000',
                '20210209:222854.805309:+0000',
                '20210209:222854.805316:+0000',
                '20210209:222854.805323:+0000',
                '20210209:222854.805329:+0000',
                '20210209:222854.805336:+0000',
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
            'name': 'ϫğӜѨʥХϻ',
            'value': {
                '^': 'bool_list',
                '$': [
                    True,
                    True,
                    False,
                    True,
                    True,
                    False,
                    True,
                    True,
                    True,
                    False,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ұ',

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
            'catalog': 'ʳɩɆΈŦŰʆśɎЬȝ¶µũ˺fĽʉϾȜÜмə˳ȁƂ\x8bǃƭЍ',
            'message': 'оËυʽ˽ĹǅѪӏҬƓǞOӢȾţϙˡ8ÒƠɰϹ˶ђӷ\x9bȁӝТ',
            'arguments': [
                {
                    'name': 'ǣ˅ϨʅЯŋoӼȣԝӻYÝǆѬѿ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -3614769252867944187,
                                        -1820199532285551674,
                                        4147286059433827004,
                                        3372668319168364825,
                                        5702498856288572722,
                                        -7944490821832656402,
                                        7643190004355528983,
                                        -4921001790930985834,
                                        9187177678050716806,
                                        1142644417920297647,
                                    ],
                        },
                },
                {
                    'name': 'Ԇθ»ϿȝÓԚʋƮč>ˈΌ\x92ƹǫϋƂʿȘҖȵ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ɾѵĒЀƾ\x8eӵǤѶѸƫʏҭԤ\x83¼Ԏ-ʭǖ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ϴԑϬ˂ʮĭÍǘBφŁŐɝөIºťӈˢΦӎɉ<ĮȲҦϯǍԞǠ',
                                        "ƮĞȑΘŇН¢ЈŃg˟ƠǷөƠχδɛҶ'ПƎҝʈōӣǡθŴɟ",
                                        'ʮѠάͿԕǻȶϷўѼһгǚǗќΛśʡĭbӄ¼\x88\x83Þ·ΣŐ0ͺ',
                                        '˫ДɝҏÄԙЪΰщɗʫ\x9dƽԁáȔ˗ҴԀѢɑÔτǯӎʠҫ!ӭ5',
                                        'Ǌ©ЩӗωÊ¼İЗӘˋѢ-өѮŲЋbɽʯΠõˌѦӗ˦ÙżѸ@',
                                        'Ӻ˸ɼӟ6ǥϋʹVıʯXη\x8eɚњҴƕӄƁȌǎ\x9fƁƦŝĲʝбʴ',
                                        'łSԄӮĉĦяΌŸɇ϶¨ͿǺе\x87\x90ɠiҡɈȖ˚YŚʒ×ҹԁҙ',
                                        '\x93+ϻȵʗӧѥȿԚҶĳÂbǚіxҴʚғκʼ©ЁȚϛҐ$Żȍɰ',
                                        'ƒĮɷΦΦ6ȳ7UӌɁғĂŅˈŜγɕŠѽùӹ¥ɂŲԟԂŁώƙ',
                                        'ӌǲɒ˄Ϗ˕ϳƮβѭӞԌ˃ЛŠ³ѹΣӑŇґ÷!ǼǛˆv˧ż¤',
                                    ],
                        },
                },
                {
                    'name': 'aɞǴηʃύËқѲ\x7fӄƖÜϣҜТˆҟ¶ƻĒũ±',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ƏƅķȫʼƢĕҏYПРʞτ@ǈŗ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'Ά1ӤҨљȤ˄ц˭y*ќÒȿσϘӐәԒЏ¿ʬˋǑ>\x88Ü͵ʪ¬',
                                        'ѴeǁˢԊǀ\u038b\x9dȆžñҸԊȠͺɭϤΞΎʶʛŗӲєжԧåϓҁˋ',
                                    ],
                        },
                },
                {
                    'name': 'ήΟЪαѲӥƔ˴Ȗåԡłғэϓȹ˕Жҋķ\u0379ʹǧϳ҄ЎǦɿƓț',
                    'value': {
                            '^': 'datetime',
                            '$': '20210209:222854.801894:+0000',
                        },
                },
                {
                    'name': 'ƸŃŴāåWҼҡѤΎĭ°ԁӚÏʍӆʓϔХɴ΅Ƈ҄ӧýèϖӘӍ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210209:222854.802582:+0000',
                        },
                },
                {
                    'name': 'МŰʌôţ¥Ͻ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ƠʤϴƄ\x7fΎʋѬ',
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
                                        True,
                                        False,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'fŝɹđ\\ˡ-ȴӀwʣ\xa0ʱ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ЈŪ',

            'message': 'Ǣ',

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
            'identifier': 'ʺɎΈÌŁƁЈŬ»ÖĲ¨\u0380\x82Ңŋɖ5΄Ɗ΄ːιǪĬǏɐЪļā',
            'categories': [
                'os',
                'access-restriction',
                'invalid-user-action',
                'access-restriction',
                'file',
                'configuration',
                'os',
                'network',
                'invalid-user-action',
                'file',
            ],
            'source': 'ѫʢ˃¸cϨӔԔ˞кқҕʂļɱýġϪȁϢɿżˠĹӖʉϑňȱ\x9d',
            'messages': [
                {
                    'catalog': 'ѠӲѪ)ʩ\u0379ԝѬʰʯΎӎuͲɻȈ˝ƺГˊłǬԏǰųīƏЧȸӎ',
                    'message': '7ԇÏŏӰІ}5ʆǭ:ȵϐǊ˜ĿΖҸυɡˬϭάsƪҳǐɯ\x92Ƶ',
                    'arguments': [
                            {
                                        'name': 'ļƕï3ĞͶqʙï˦ԪĺЅ±\x90ϚϓüŨѶǡQԁΖɰǝѻ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1401609474530093843,
                                                    },
                                    },
                            {
                                        'name': 'łˣŏ©Øɸǅи˘űҨМҕȹÏĴ¸:Ǒς\x9eӭ¾ƫѠʇ_',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 804255.1885430583,
                                                    },
                                    },
                            {
                                        'name': 'ԫ÷ЂʿˤνɹΦΛәėƫȼҵɶҨԧ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '΅ʅХʜӥĉËò\u038bϼӰǢ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 407692.0003280825,
                                                    },
                                    },
                            {
                                        'name': 'ţʖcѤ\u0382\x97ԁԟӍÕȳԢƍ÷ԗ\x9cxҷǹҒԭWМčŐãfѨL\xad',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ɏţ;ʅWě/ņʰřԇΧȿҙȱƐѕȆʯȩƭFÀ\xa0ћþäǷπŁ',
                                                    },
                                    },
                            {
                                        'name': "ϐƆÍӥîԥˑÍąų'ǹ",
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3414150496896922450,
                                                    },
                                    },
                            {
                                        'name': 'hÜˤ\x8cƲʒİ\x94˂đ˛тXoŬрЈʝӑ}Ȯƅȧ˺ɩɥѹʲыɷ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': 'ʢˎįԌ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¼ʻàoƜʖ\x86ЮЬӇǱϺŔϓЎ\u03a2ӻ?ҼɂѸϝҲ-ɮŊѽĎ\xa0˅',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222854.769969:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ΔӾĔÙɱҋǹʶϖɦэ×˔ĔĞ\x80ҭʠӂʈҸҬȼɧŇeМɼĂ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3836665158107282230,
                                                                            7794137570432498578,
                                                                            -1037463156898989430,
                                                                            9108005059863511265,
                                                                            1259783480727122343,
                                                                            -1244518842390524353,
                                                                            -7057763019535086645,
                                                                            -1867853983535406329,
                                                                            8309896938922797341,
                                                                            -8259117260282034566,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x97їȿːƯн΄ЀѵѬҨЕĒŀƺʉҘκйϥПѿÄҢɪřȓɢÕļ',
                    'message': 'ŤʂÂƚ\x94ôϴЪʲυѴưǪüÍǬɪÕʘȖАДҨЂžӥȈЍм\x90',
                    'arguments': [
                            {
                                        'name': 'ϜҗυʔӬιӰ҅ˮĸЛZǨȎҎӒɂ\x93ĥ\x98Їо˗ӶƉ·ʤ҇о',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            450241.91712970345,
                                                                            818635.2891775266,
                                                                            424662.8923757556,
                                                                            178650.73092879832,
                                                                            643955.5158737216,
                                                                            320315.6622582257,
                                                                            394877.1598009892,
                                                                            992723.3712619636,
                                                                            -82350.79020540432,
                                                                            373119.64583786676,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'δȵБĩǞьˁӮаʞɦз&ɔ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': '^ϿȊǎя4ͷϻԀÔͰĩǽ˅Â˜ǋËĭġĀˉѰԨӸÂĩÆȔʑ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222854.773823:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x87ǌȲрϤ·ǃɜҲӎƖП ;ǽƻĠάǏķ{ˍϿϢŔɽЛϯГƋ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'ƯżҿÅϥrϨϡƆñԂҺTёǡΗʍʪԒ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 994680.1673709152,
                                                    },
                                    },
                            {
                                        'name': 'аžӸʹǈЧσҐ҇ʁŅ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ĥ\x84ÃȈӖĒђſȅЅˑлǠģķħřʒks˲ƘљҥnƦ\x82ȧїґ',
                                                    },
                                    },
                            {
                                        'name': 'ɢóԙӏёėĹԕŢƁ˯Řчϙ\x97ĝЊϬwуŴЯԎʁˁЧȩɤúѯ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.774925:+0000',
                                                                            '20210209:222854.774949:+0000',
                                                                            '20210209:222854.774956:+0000',
                                                                            '20210209:222854.774962:+0000',
                                                                            '20210209:222854.774968:+0000',
                                                                            '20210209:222854.774974:+0000',
                                                                            '20210209:222854.774980:+0000',
                                                                            '20210209:222854.774985:+0000',
                                                                            '20210209:222854.774991:+0000',
                                                                            '20210209:222854.774997:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˊ6эģȱsùѱ\x90\x82˹ĲýR\x99ĚÉɷҥВʁ*Ʒ˩ϱŠӏŊӅï',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8428965234363925436,
                                                                            2039768082668437922,
                                                                            4783587260519635346,
                                                                            -777370969614306386,
                                                                            -5564345477103588189,
                                                                            1901051425047266883,
                                                                            -973447922541240567,
                                                                            8678100523502426284,
                                                                            -4215704994554104064,
                                                                            7782392980279712388,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǙѪαûΙМĤ˗¡ŅѼʆХәȉĀİ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 240082.45326066704,
                                                    },
                                    },
                            {
                                        'name': 'ϽёǇǵȌЄԮCÐпÕƎɚȄу˓ЊˑĥǅҿƩʳɋɞԢŸ˘ōǹ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\u038bϗčØŖǅ˷ˉƫҠКgɚȍɩ\x89ǬχɉԭųəǀQƒȜǳҞʖҖ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ǹˊ\x9fЄƉ\x85ɯϬøżίǮƸΝӰà˨ɾʮԤȽϺɃǊ³ϫӯŭƞӴ',
                    'message': 'ʖшͻɲ{ľ\u0382ʡ\x93ԇŖѐʆĵʦωŞІȶф®ΈυțԔƝƋйдɧ',
                    'arguments': [
                            {
                                        'name': '&ŔɒˬќͲКfωщżÓчĶѡɼĜƄȟʐҭˈАXФɹ\x84\u038bҏѓ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4084997807250657483,
                                                                            7072279998984523417,
                                                                            -6078064266766638765,
                                                                            -4983571466023402941,
                                                                            1333771066448984661,
                                                                            3548546665880233310,
                                                                            -5895045277678562172,
                                                                            6403924426828602075,
                                                                            -8115654861387222959,
                                                                            3582815525330244798,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': ':ȸʟvŔРlȥ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'şςӀAåҮӊԙȌ˪ϊҸв¹gʞğʴ¿˯ȽƋҖɊІʳԟд·ϭ',
                                                                            'юcǗȬзǅҋÃЙǗȔɜʈÊťïӧԍӅӓǏLRɳ¸ǭȰ\u0383љŷ',
                                                                            'ǷǐôÈơԖŇʒOĂ\u0381ˊʡόˠƏŒˠªȞƘƝΣȗЗǻŉʆ Ă',
                                                                            'μȺŒцīĳԔɉԈĪűү!\u0379öλώ\x8cЙθƇɞϾ˨ȼǆШŧĊы',
                                                                            'чǨ9΅ĭŦ\x92ԨbĘŖĝЖôСԘͶʷůϐɄ˩ŴΕíΏʱʣsï',
                                                                            'ȝƥbƭÂǣďǣʟˈɔҮ8Ϲhų˦ȱˏԫηή$\x91ҡƓϛʲѬƏ',
                                                                            'ĹωЛͲ»ӚƒӠа¥҄ӊӯԀ\x9053ɣ\x91®ҩЙˮҹҀ¡Ɖ\x80\x91ԛ',
                                                                            'ѲĽæíƅȬҊӇѧ·ʉΎȽş˲ɂ˪\u038dɆʨҭҋϮοʰĎҭ©ʥ|',
                                                                            '\x8aɥƞǿ´PжϮцʬЬƜȬӀ\x92ЎÉƴρϱȍĿ˱ҳİÔԚĩ˓\x8e',
                                                                            'ϚѦĜӝїĴѵʰɺŌˌʞĀԂϷӓƯ\x90ǷΈŭԡš\u0379ɺύѾ¼ɾ˝',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Н¥Ǒ¼ԃĤƲƚ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.776739:+0000',
                                                                            '20210209:222854.776757:+0000',
                                                                            '20210209:222854.776791:+0000',
                                                                            '20210209:222854.776801:+0000',
                                                                            '20210209:222854.776808:+0000',
                                                                            '20210209:222854.776814:+0000',
                                                                            '20210209:222854.777438:+0000',
                                                                            '20210209:222854.777462:+0000',
                                                                            '20210209:222854.777469:+0000',
                                                                            '20210209:222854.777475:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƋăҁǮҊіǰʺĎԍǏǤĮ˅ӢāˏȟăԘЙ½ǸҁÛEĲơłӘ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -882992222592307329,
                                                                            -3099151822382999534,
                                                                            301807834039222601,
                                                                            8053547147210395516,
                                                                            -4884478399993847567,
                                                                            -7377293197445369812,
                                                                            4770000080466039611,
                                                                            4567179469749245266,
                                                                            -1719382516106744543,
                                                                            -775752628304008871,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'xҦѱXЁéʽƺƮҷƲԔϨӍĬϵɇŅƍȝĝѥɈƇҐǷĄ8Ʈƿ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222854.778990:+0000',
                                                    },
                                    },
                            {
                                        'name': '\u038bҴǩʩʁĿǳïȠ´±ñzǧɗӲҙԧǌΘΗõŭϹʚѹǒșВ;',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӘŹ\x9fϕҭЇȪеэʊ>ŐϣҮԘԁʭѲƴБ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ή˝',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ҲίűǋѠОͲªƱˠЌǢǬɥԑˬ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3733910539477901053,
                                                                            -7782194937618123683,
                                                                            1118858481526520197,
                                                                            -2017580310136725845,
                                                                            8579642249801751538,
                                                                            655973019388798788,
                                                                            -4345761661513529373,
                                                                            -9030902570813603244,
                                                                            3243791946452517777,
                                                                            -2655500939358632904,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'йȐ˹ϐҵʌѹ\u038bԊǡӺ\u0378ɥʢƺȟŤӡ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -783612888167116766,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'όм:ʏњӟϵǟźɉϧĞŔàơùˋ\x8aӛϺ\x93φδż\x87ƝφɑÑ»',
                    'message': 'Ļ\x9bΟМ:ȋӿϧ\x81ǖя˯w\x9dҩԋɍӌөɻόҌʬҹӎˆϙȷˋï',
                    'arguments': [
                            {
                                        'name': '\x83Ǝɔ~Ŀɑřq4ͼΆԥƍÌĚĲȼ˙ʮѱȗӅ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7248005198152583026,
                                                    },
                                    },
                            {
                                        'name': 'w',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7837362892694144651,
                                                    },
                                    },
                            {
                                        'name': 'ɰ\x87ȗìŔţΤΩƢʃuĎ\u0381АêԥəȯщĪҲѢҸĆέɩԍϘҸ4',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.781631:+0000',
                                                                            '20210209:222854.781679:+0000',
                                                                            '20210209:222854.781696:+0000',
                                                                            '20210209:222854.781703:+0000',
                                                                            '20210209:222854.781709:+0000',
                                                                            '20210209:222854.781719:+0000',
                                                                            '20210209:222854.781730:+0000',
                                                                            '20210209:222854.781740:+0000',
                                                                            '20210209:222854.781750:+0000',
                                                                            '20210209:222854.781851:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϩÛŽȒ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɳи\x8aǐ$ʒĎϪīôΘƼ͵ԞѸƸЂăǄѽʱǶɯFDεħĭʜʗ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': 'ӭԢàӌʾϕηӿ˫ЧԨϹєˆԞψÿϫʖФn·ĉ ųǁĸӃɳ˷',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 411141.59367061843,
                                                    },
                                    },
                            {
                                        'name': 'é҉ʙůΥĆÔŌϛČӶĒԑΨ˛ӧļȾӷӦȇʐӘ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'şɃёJƒϘlǣǔЁ˦˳ʶϛJŪϔ9ɘǋˋƊѸɷǹʍȦåɠђ',
                                                    },
                                    },
                            {
                                        'name': 'ϑHЛżԔšÉA½ʙɾΧǩӛèʋʵ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.783135:+0000',
                                                                            '20210209:222854.783157:+0000',
                                                                            '20210209:222854.783165:+0000',
                                                                            '20210209:222854.783171:+0000',
                                                                            '20210209:222854.783177:+0000',
                                                                            '20210209:222854.783183:+0000',
                                                                            '20210209:222854.783189:+0000',
                                                                            '20210209:222854.783194:+0000',
                                                                            '20210209:222854.783200:+0000',
                                                                            '20210209:222854.783206:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0379˦ћɛΘǦ\x9bӞλĒʺȐʴҺɛ˟£',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222854.783574:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÉǏ\x9b9ǠϹĊЗ×ǋɞſЃĎƟпŸ\x87їōгEπͼħДˊζԇû',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3608571865754310480,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɉã\x83ҁÌŁfѾĄǠ\x81ɠӣƎʺΐʳá\x96ʫ\u0381ŇďƩΤАýʭ;ӝ',
                    'message': 'Ӌ҈ѣϗлƟƉϺȠĞ˕jʥĭǝ˴ҰѮȥʋOǇʘƁϑ\x95Ŀъuɽ',
                    'arguments': [
                            {
                                        'name': 'ϓƪňУĕϞǢŃӃ>ʌѦȫЙЈѩǯ§ӮӱʝċżҵԠɂɽ"\x94Э',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2400366042067853247,
                                                                            -6968022442948973447,
                                                                            7756553609560865502,
                                                                            -2132327058588497020,
                                                                            9005993364752343090,
                                                                            -3606411173419904412,
                                                                            -4591091581032486567,
                                                                            328127698124633734,
                                                                            6541833626593050396,
                                                                            1122573647192614805,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȢϜУДƉШƐƕ\x88ϐҋ·',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɽ\u03a2',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 367959.36769456766,
                                                    },
                                    },
                            {
                                        'name': '¬ΥihťŐԢũЮȪȆҹԠҗÏº\u038d=ȝЙ5Јҗāӟӑ-ɃƬϜ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222854.784897:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɬˤ҃Ѣ\x98ӻƿƯƆǸŹ˱ȗӣ>ʟθЄɓҥҲɥ&Åʑ-ěŪȞĕ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ңӪŇX҃ëξÝ}ӋÕƝԘґĢ\\ӣȿϑҩѕʹ\x9fūҽοЗҨӻЏ',
                                                                            'ϣӡ˒Aǭԍ˟bˀɶΥɷƤǍÛαδëįǓҲģӺԐyʱűĿǁǽ',
                                                                            '®Ⱦšʥ҆ĥʉȤ\x98ԍˆȿā˸ԫșȨĿ\x85Ҟȸ/ҁʇҎԅоkԫс',
                                                                            'ґǤƩëԝаţĄЗΈԄĄ҇ЬҹǨʨΪӍɴOeԓѐdȖŨ·κӶ',
                                                                            'ŴǹʅϫďӏȉoȭҙЌН*ÝԁТҡҲʌÑIѝ!#ņѶ\x90õǎR',
                                                                            '\x92ɧňȿŋԨɻƂʦȽ¥ѿźѺ˦ğˡѧΛϜӺӱʀīƁң\x8dɈ3ï',
                                                                            'ˀԊˮјЀCɠͿԔ\x84ԓʙ\x9fƣͻϿ˸϶ŤʲХ\x92«ҔȊƵƢʾƑѐ',
                                                                            'ĘKÆċʣ\x8eћϾȨкͶŕԌƽęēѭΡűǮąƸϤ\x9d£\x9bЇƑŜґ',
                                                                            'ȱ½νȌϸцѥѽē҄ģͶˇƲǭάϠžɶdƤʴЩĤƇУŜȀįȽ',
                                                                            'ͰɃmԒίȺBӔԊԦԦˋ\x84ӋÁıͼʬҙ҈ѩȵҶͶǮÈɠΜƖͰ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': ';ιǘʩǺӭ9ɹțʻ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŃĤϽƝĵϜŔҊïàӿ×мͱǣĔßŜԚeĸŔԮʓǟvƌʑϛы',
                                                    },
                                    },
                            {
                                        'name': 'ňêǾԣgӞќɚϮȟƒĊȁ\x86ëӼѨɑҍœɇңЖӐΰΚˏμһȓ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            327994.0581218915,
                                                                            381012.49708915077,
                                                                            568451.4681703815,
                                                                            46224.209665979724,
                                                                            328831.1992011708,
                                                                            990209.1106010256,
                                                                            684556.1311856869,
                                                                            215273.97926923685,
                                                                            659042.7828389225,
                                                                            888057.4992383687,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '?ǮæϜ8Ǆȟűчä',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            971985.9019474536,
                                                                            218197.3038372668,
                                                                            82738.35170709528,
                                                                            230807.422503673,
                                                                            -7151.656752207549,
                                                                            -83812.84729219855,
                                                                            469189.71527177386,
                                                                            190627.08305186557,
                                                                            -13813.009121301264,
                                                                            712306.1358686107,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȗӈӑԁ\u0382ǲŪŬƏĪʩ+ЊƫȏλΥȐʍҏņ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222854.786137:+0000',
                                                    },
                                    },
                            {
                                        'name': 'þƾҀʨÔƒãòΝȣÊˬ\x99\x90ɠTΊʬŗӜϴ\x87ԄΣǼʑĶˮοƹ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5524527819907597946,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ЋоʆАӏ¶ҤɺěŹĩСȝү«˛ϼɗɖӅӳҐїʙśђˤԖӔӥ',
                    'message': 'CɦϟëТӍʖӹǬȒҊǰѻԋîpMʠѲFǦȹԆáЄͼʊϥÏǵ',
                    'arguments': [
                            {
                                        'name': 'Ѷ\x98ÃɎƶƷȈïɣˏԦг˜˹ҋΠͿ\xa0ιɝϵυɆȷĜ˄Ǹėӵӝ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5713794346205290598,
                                                    },
                                    },
                            {
                                        'name': 'gìБǣ¸Ů',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            782155.7547453309,
                                                                            454180.25874225155,
                                                                            541600.8599674212,
                                                                            446050.4943130339,
                                                                            290166.92704853264,
                                                                            226907.8613658963,
                                                                            681790.2295507155,
                                                                            336597.64735725283,
                                                                            380632.7655912134,
                                                                            969188.7015509745,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӌћŷ\u0383ϋ\x97ƞљšÌĭ˭ȿǲқк¥ҲʺÅҩӺш˨πďƟҷγă',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 635601.2760731789,
                                                    },
                                    },
                            {
                                        'name': 'ƋƨӥÔюˌƞϡίâΨǳʼʎΎԏȇԒѮ˽ʼŔѯΥ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222854.787371:+0000',
                                                    },
                                    },
                            {
                                        'name': '˓Ѳʡ˻ȿĀȽȢɨȡͰ%ʲΚÖ ǐìСAԝëɔˮЁÖԞÇ҅â',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 484940.6426470332,
                                                    },
                                    },
                            {
                                        'name': 'śĈ_ƕҀùűʒŷ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222854.787633:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϤѴӕυĦ:ʌΞ˺dѓϥӫЩɲ˻ϐҲϷǅӯŬ~ϦʃƍʈԚ\u0379Š',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            575581.0541521566,
                                                                            397539.5100617388,
                                                                            791790.9429905454,
                                                                            -32983.52341840537,
                                                                            922995.5459468258,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ρʦˆѡ\x82òʯ˵фƅǞԇZϓ¦ʨƶԏƃΌŷǰʺu˥v\x8a',
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
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʝʋюŘ\x80çɳʷƂɳΗ\x9dѺ£Ѧ˓¢ıԖʖ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2018204281666701624,
                                                    },
                                    },
                            {
                                        'name': 'ËȸȐѧȁεȯԓư¡ƥӹй',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.788337:+0000',
                                                                            '20210209:222854.788350:+0000',
                                                                            '20210209:222854.788357:+0000',
                                                                            '20210209:222854.788364:+0000',
                                                                            '20210209:222854.788369:+0000',
                                                                            '20210209:222854.788375:+0000',
                                                                            '20210209:222854.788381:+0000',
                                                                            '20210209:222854.788387:+0000',
                                                                            '20210209:222854.788392:+0000',
                                                                            '20210209:222854.788398:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǌҎʁȓԊӥRɦſÆϣԧ϶Đύʈưŝɬ\u038dņԌˈΘQӘrˊҹҶ',
                    'message': 'ЦȒɌΓԨÃʒΘ×ǩžЏ˗҃ҝˋǖҚҝϥȩ\u0379ʉȨŚĨʚ¡Ȫʠ',
                    'arguments': [
                            {
                                        'name': '҄ѭ;ӲăȮĪPӧ\x8aʖ·ΫˊʬȲǕƘӞ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.788890:+0000',
                                                                            '20210209:222854.788903:+0000',
                                                                            '20210209:222854.788910:+0000',
                                                                            '20210209:222854.788916:+0000',
                                                                            '20210209:222854.788922:+0000',
                                                                            '20210209:222854.788928:+0000',
                                                                            '20210209:222854.788934:+0000',
                                                                            '20210209:222854.788939:+0000',
                                                                            '20210209:222854.788945:+0000',
                                                                            '20210209:222854.788950:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĹЄǌɔ\x9eʢɕʂɻĽć\x8cΏ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8642992029568633712,
                                                                            -3797655030318492006,
                                                                            7387200994353796495,
                                                                            9191105169731592022,
                                                                            3915496040195499069,
                                                                            1616074411398164284,
                                                                            -1485444979720602803,
                                                                            5142415666554376835,
                                                                            1465984608296513859,
                                                                            -452052718165204809,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ňĿˀęͳĢѣöԌҿшЕ҉Ɨ˶\x9aƊȱǪȔūӂщĉԨʓŞ˻ҩǼ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.789528:+0000',
                                                                            '20210209:222854.789544:+0000',
                                                                            '20210209:222854.789552:+0000',
                                                                            '20210209:222854.789559:+0000',
                                                                            '20210209:222854.789566:+0000',
                                                                            '20210209:222854.789573:+0000',
                                                                            '20210209:222854.789579:+0000',
                                                                            '20210209:222854.789586:+0000',
                                                                            '20210209:222854.789592:+0000',
                                                                            '20210209:222854.789598:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѱϝәȼNèƻlÞø',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѲȆӒȇĸˋū`СʦáɍԭΕÿ˚\x8fłԝʋ)ī˹ɹòƤǾǕ\x81Ҙ',
                                                    },
                                    },
                            {
                                        'name': 'GxʈѽŭǘџEȽԛǦаɥϥӦԀŜԎқςϲԅĢɡěΘƒį',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 17250.53978039323,
                                                    },
                                    },
                            {
                                        'name': '½ł҉ʱӓÉHɜФ\x7fǝÉԜϤӲɹŚıҙҲLΉǠʭҡ(Ûџ\u0378Ѳ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.790158:+0000',
                                                                            '20210209:222854.790171:+0000',
                                                                            '20210209:222854.790179:+0000',
                                                                            '20210209:222854.790186:+0000',
                                                                            '20210209:222854.790193:+0000',
                                                                            '20210209:222854.790200:+0000',
                                                                            '20210209:222854.790206:+0000',
                                                                            '20210209:222854.790212:+0000',
                                                                            '20210209:222854.790219:+0000',
                                                                            '20210209:222854.790225:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȕҝǑ\x94çƞƀ˙ÓãѐȠɺʿĉϩʸӍǪ)ǴͻÐĶѣѡ\u038bΪò϶',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
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
                                    },
                            {
                                        'name': '˱ǂĿȬɣҿӠ«ƝČś\x8aЯȵćԜ΅\u038dԮϡҖαʤZɔʵȦɍϒ˯',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7603143377797761941,
                                                                            -2059476296018716239,
                                                                            9004687529250774579,
                                                                            -3597099830476770539,
                                                                            7325340634494604099,
                                                                            -7693749106236048819,
                                                                            7235489974403623810,
                                                                            8915598847982181753,
                                                                            5446426354928049774,
                                                                            6194569241559090030,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'δ\x8eʢγКƚͲxɼwpđϕĩӝΊ3Š˱˟\u0379тGȪʒŬʠ΄Ǔӯ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222854.791024:+0000',
                                                                            '20210209:222854.791037:+0000',
                                                                            '20210209:222854.791045:+0000',
                                                                            '20210209:222854.791052:+0000',
                                                                            '20210209:222854.791059:+0000',
                                                                            '20210209:222854.791065:+0000',
                                                                            '20210209:222854.791072:+0000',
                                                                            '20210209:222854.791078:+0000',
                                                                            '20210209:222854.791085:+0000',
                                                                            '20210209:222854.791091:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʉPɾЅǘ\x8bȒĭƙɷǅǅ˦Ɉĭˉєϴɡ˃ɧũҟώ˨ТϜĻУԁ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʦqҭʿˏű¿ơЭɼѢƓžϑƧҔÄIҡÒ˦ŢÌΙʾȽĿΧӊӂ',
                                                                            'ÑʀƏѐӃªϮƪȒѱ˗˥қсĎҁҒîӚӾŕͷŰƭѿѫɿїԨ\x9a',
                                                                            '/ƵϡcʍċӊЇɕΉԋȫ¹Ĥ΄ćρԂ϶ƎγțҴvȈˎJѡΌː',
                                                                            'вƞ°жȺńáÙʦѴ͵ƿԣНǛŦȻ½ƠğÉҹǯ˽ÁӕΐÀǜԂ',
                                                                            'χĥϼȦʊиưŔϏҳΏ¯ҎʲʴӪ\x98˲ýńR»ϦëÐ ƋˢҐʙ',
                                                                            ':ƂəĥљӵџĊǚȡǭСøӁҟȘѢɉʓйχϙdΰͳҍˬˈʔŌ',
                                                                            'Ӛ~ǧѨťλ\u0382ԝVǈнЧԕʖƿ˩ʋȈѝʴȕАƝãϯәΦƿƕÛ',
                                                                            '\u038dʜ˚ʦĺǓѳǪhϽŝИғͷҿŞǴâтα·ёTЩхҧɓıžǐ',
                                                                            '{ʆșðКȶǌñЙϧҊŉͷЇȏѵǿĺϽŪßĆµƛúsɤѵѶŮ',
                                                                            'ǘκƂƐ\u038bƢŲʾȠf©ŒːÉςӧˊÚй>f|ӬѡԈǐʏіАϐ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŮԌΡКǲ˵ơɀŔł\x9eЂӼѹŇϮν¨ƃȘћ˶lɰ˝ŗЂґȱԛ',
                    'message': '¤Ħ²ɗжĲ˸ċԂϖŻŧˑİ"%ʐLȷɦЬfÂɯ˭˄\x8bd(ǥ',
                    'arguments': [
                            {
                                        'name': 'Ѥɪ˹\u038dĔʻ\x8dәPýΎɽ\x84ΊӐ\u038dȣ\xadƖBʕѪήЮĉѾԧŨǷҚ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¥ăηŃĞӆԤЄСɶƾƦȰϐʷмÊƨëϐȶчǊʗвӖǆԆθ˸',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҩĢҽΌǸưgӁı_őǕӊƶ҅ύ˨ςͽñ\x7f˙ѷю|^ф"ѶĻ',
                                                    },
                                    },
                            {
                                        'name': 'ͲԖFќ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѭÂξɂΞҏÁɔΔГУĽʝҌʎǗǦ\x8fˌʪǵ˳˧\x82ŞӔтèоĖ',
                                                    },
                                    },
                            {
                                        'name': ')\u0380ʂɌѵɌ\x82ʧԇǰӢʻɬӿĝϊͷϭɅ˱\x9dWώȪЋɽǺǹĭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222854.795440:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɗʹťɩ+ѧȀθϵľԣǑɱԐƼԞȂӟЇSʷǐΊͳȺ(Ԃ˫ЩŅ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 326073.96514254226,
                                                    },
                                    },
                            {
                                        'name': 'ītʹ\x8bɐ³ѣǳȅíжȟΤ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            263758.2462283314,
                                                                            925119.7156023382,
                                                                            -22528.3543046158,
                                                                            280234.24296649266,
                                                                            903201.0214900377,
                                                                            924102.2159223581,
                                                                            -95696.6267357552,
                                                                            982507.5506790867,
                                                                            696212.7127117594,
                                                                            40439.066321452236,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "'ĦҁǞ˫ЂӅϲʉͼӸ",
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƭӶƃӡͽĦɇӑ˙ҭЏТnxχ\u0379и\x9fƶιĞǗƩʮτЕΫɤҘͳ',
                                                                            'Ƈ\x87òÅ\x9dεͰԂʜҪǭʽʘƈūӇϮϤʒoɖΪĲƥԎȅʉ˕êҘ',
                                                                            'ԉҴǳΕʏʙҞǆ\x9eӟóѯ˄Γɐŷǐė˾ßɪƈұƨ˸ȸĤѤҷɂ',
                                                                            'ÚѳȒRϬȅ¶ɤ@xľҤϲˬӘÖǟшǐұł\x8bԦĳϑ§EԁҬǽ',
                                                                            'ŭƩ˙Ď\x87Ѳ˚Ξʡ˼ȓz˓ĜҎȔӢơӀãҭǅ\x83Ǥ(õȠĝɩ˱',
                                                                            'ȼ9ȿ˘ȬӞΉʮϩ\x80ʄ˲ZĺèтΈįǴӣǸȿœİԭѡ]êɚП',
                                                                            'ËԝϬˉɷ¦ʉάьjȭƺÜé\u038dɽЀxİ}өȂəŠԋ¦ǷĸȍJ',
                                                                            'ˊ·ĲéçǠɑԑĊɑĳłζqɬΐԝɮҗĈмůɸɢ;Ιάԍ˂ϥ',
                                                                            'ԬˮŖűʽȿÆʀÖġϢӥЎљΧʪǧΧƙ:ƏÜ˵Ӣˈҝԕ҇гю',
                                                                            'ԓҦȴUÝœ˰Ǐ\x9cЁʙǔÒƫÕȨȿʕˉ\x9cDέÄͺƘīԄùǕŌ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӆȱũɩßˣʦʅԭͽāaʻʮ\x91ˏͳÑ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǡɘӷʈԘŀԛ-Ƚ˭іGÇС,ώɌĺlˈ7ŔˁĽ\x9aϥɪΝ>Д',
                                                    },
                                    },
                            {
                                        'name': 'ƅªǳȯœЁӋȼɺҊϊǝ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222854.798181:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ΥȤϱԀΨ˶ϼÆԒįƑȭŊǑȲЪȘǁă˽ӸАϧΊ˲ĂĿɰƁʁ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
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

            'identifier': 'ɹâǠτɥ',

            'categories': [
                'network',
            ],

            'messages': [
                {
                    'catalog': 'ќò',
                    'message': 'Ҍ',
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
            'name': 'ǵȸ+ʩϭɦϣ°Јʙдҝ\x83˗ζŐȿЂϊҳϜѹŊАʂӿˮóΙǉ',
            'error': {
                'identifier': 'ԩ\xadőʲόɾɞҗſʸȹ¬ӛšӅ\x8fК˩ѣкқǷфɿǱ\x9cЖ@ýƎ',
                'categories': [
                    'network',
                    'os',
                    'os',
                    'configuration',
                    'os',
                    'file',
                    'network',
                    'network',
                    'network',
                    'configuration',
                ],
                'source': 'þȣƯ·šИñФĝɑӽĒѧ˙ſÈʻȪʒΫπȚʽʨӒ>ĦȾҐǷ',
                'messages': [
                    {
                            'catalog': 'fԈΉɟҡˢʬ˽˥®ǞΏЌ6ĞκҝΟӤʒíʤ˗ªĢҒĀȐаƆ',
                            'message': 'γϣҝҦ¤ê˸ͲȧÒЧϔӏсӢŐnɫԞʎÆŖϘӾ_ÔμϸҏQ',
                            'arguments': [
                                        {
                                                        'name': 'ƚɂǩԗȰ\u0383ºйɁԭ³҆ѾāC',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ИĸÖ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˽ÄʗÉҞȁ.ąӺˢ\xa0žƔŠяâąȤʯĝΔЊ½ɑǛƆŅҷƏ˺',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҵπҡ˖ϖ/Ū_ǹȞʛѾ˩л)ȃ˕ԖϗҸưӼҺƕŴŻҬϖ°ʒ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӭʢҭˍ˷ĝҪӉ¿ǒɂŰћ¬ͲʐɾтPâӻªԋҲϼӃӖЈѱҋ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ż',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ːìτʲǏĊпаƈĦӅ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5760643977960266483,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȵèҹL)ũ˂лűčʵҿǁ:ѥȅʺϛ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЄdӤŵҎμ˝ŜǐȈѰʏûǪáҫ˘ԎӪ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϱǨк<Ҩ\x82ʫΖŬлѲϩ˹ŚŵÃĵÓ\x88υѿЍˑҁ÷͵ϞӞёα',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĨȔ˼Ͳ+όµĠ ūϣİΨχҦӣǷӪԈҭѦҗљУȂÜӺȸӬӋ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'űŁҟɰ˦ʑΛǪȴƾɹÊʦ\x87ĝΣӸŸƜŸ҂ʣ˔ʥӗ\u0379ѹƘÇʘ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȅʡԮǅǟʃʹԡϋӊ´ʓɸϿYеcҠΞϭҊ5§ҸǦǄƿˉ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 214346010168387631,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӆÅȬAƋΓǠ»˙åǂÙȸ\x9bàˍ+үǢҿÁƏg\u0382ΆlȐʦфʼ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4364376570753818017,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӯƥÜŉжǶ`ԙʻѾяӑСЉ¾lCϻ@p\x82ɧȗűҒˎéϱ°=',
                            'message': 'ȩŻtÚȤĕпɫÞŀɟķГ˺zßϘăƾŊͶŝŕǼġNˎʏøˡ',
                            'arguments': [
                                        {
                                                        'name': 'ҰВΟˎʊĹӭҥ=ʙϦӳҁßҍͿʡŜ˲ѫvɊофʱ˫ϦǶϺϴ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĔǃӂҰԞѝηÓԮԪüюʝԅ|ĊQǡ˃ʧңˠϸчгǔДШ|ӟ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3357121349074440375,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѽ҂ѿˡɚӠàưȈΒҾùɌÃτқAőƅϕΔλɪʉıўȚīԮ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 158930.96937043362,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӵ9ņʻԁȟ\u038bǘɛʄǴ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222854.705158:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĮӺɓТʀыǟӶӋϲиǫ˨ɲĽɼЖӔѷƢʟŕԚ˺АӡÆȋĻξ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Өʬ¯ɕЯĳÏxĪӆӖϺУ0ԟŀA',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǦҝͶдҧԡжԮ˴ҋĆҎcɈɁɦѻӀп҂#!\u038dmӫКÒQΊ˩',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӝ&Ĕ¡η',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '8ΦȬѓŃцҀΉſƝQđö˫ʕıɹΏԤЍģΝ1їȇЃʃ\x99Pů',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '¨ƽЭŐϞĂ,[ҍѥʩɋ3ǺŕÍoʂǼӌғѩͺÄӥMǥӃ1ɂ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʁĦ!\x8fӽƆ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƳԔУƹr',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԞÃ˼кǜƪİѠΞʷ˥ĮǉŨáÿšʵ*ĤˏХϫĺϰźӮ\u038dϤ˘',
                            'message': 'Ў˱ѦĶƍўλɠĄʘ˫ŽӂВʡǍМȶX҉ŵÖȥј\x8dɴ6ňÓɈ',
                            'arguments': [
                                        {
                                                        'name': 'ѲœŽǴԗмWĴľƥʲļύǎʱЙ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222854.706658:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǷǫͶ¢ʚϋ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ã÷ʸȒϮůhñȩoLŘˡŔѷȸƓҥ҆ѝˁvțӢеѺIӁś˚',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӓē҉ʚζǄ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȼǉ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2522803918557775218,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƕˇ*μ#ΪƀȶЉԘУGɭ˄ϛԐÉσƧǻƲˏĉԈíȌÎΦǨħ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'õѬȍŅɮʙЛƻθ\u0380ĜħǳράƔʾ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ũӡ˺Ń˒ʘ˖ΩħѳԈҗЃĕӑɲ<ҷƚ\x97Ӥ\x8b©Ð¬ѱUϞӣӆ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʂӟΕϿȈ VǠɑϱҝҧ\x97ȼѾϟϑǗθЪԜΘ;ƴѹҾŝ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ђ¡ĜǑЬȣȉĳԙУюЖśҹ¿ҠʺѱǬς˫ҒΠªƆφ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222854.710531:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȃΔѶӷαƴĥȪӚсAƉɘϘɍüȀ,bкӉәΛöχ\x96ʝɅƛk',
                            'message': 'ԭýͽȅǜ8ƕˉ˓ѴrIːƻѵӄɢƿά<ʞ½ż7ŅҟъӐ҃ʀ',
                            'arguments': [
                                        {
                                                        'name': 'Ѓ5Āƴ\x92ШɗЈЋӤµЍҺûÌ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 312828.38761329564,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʖΛPʿѢΎǌǍУ·҄ľʻӯmó|¡сƨѓԎϴwˉѨôˎкԥ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222854.711172:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɖʱФĥ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǮŮȣɣώv?¸вZçǖńƐԢČ˦Tқ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƀʠɱįӭȸԘȔŗ҄ҧĜʒεМƱĶҒʈψŃӾǻšÎ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x88ǟιԋҫ˾ҽƋˠ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЈʣĊԛЛθɋŢ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'KΗȴЗďZԋφȋ*ŉҩҳʎrђɫǧиѫϏӗjƦʘфƬрˬ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͲөŉҢǠǃɕŘÉʹѰ\x86ȌķѺ˾ΟȷƸʵǷ͵ϦУе',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԙϋǅɢ˥ȇǶƺʣςʯʜҮ˪Şԛ˄ΛғɡĈĀūΊƬɑŀηkӫ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 399308.75855341094,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'íĎ˵ӎģȖʯљЫɤŀʩũѺÎĥдӐêόǉʶćȩčPǩϿƭƙ',
                            'message': '&\x94 ΑΕɈɾ.ЛјӯɄLȎԒõƠϑȼ˯ɋҍưǷ˥˃Ȇäɬϴ',
                            'arguments': [
                                        {
                                                        'name': '5>ÚώǕɇåĩԔҨȆӣ¦żћǸ¸ǥӜџơЀ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '϶ƘҏтʔˉͲĻǤŭƍΙƲ®ѹ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˞ŦɿѲӳώíĬŇĦãNśԠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222854.716839:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÙӹȯԧԡʴTˉϧчԦǘͱ¼ϫǊȺLHˬ҆ʉʴȩӵ¸ИħǢ˽',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҟȡȨʦƀɓ˪ǨʹɃɪЬȒdĥȫŦԅ@ɪƿǏŝɊšȻȚ¤\x9b',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 343183.1954619246,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Рϓи˃ћψŭ·ιԝϣƕ·ʎƦΛ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222854.717775:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ï\x85όойЄӁ΄ɋ\x93ǽȴѯ1þѤp\x92ӧʠԟԃȆϫԜɪ˓óʢî',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ':ҪԕʔnԠϘɿmԚ˸ɅŔӖ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȗҍȳ|ȕЛҍІˏʍЃԮѨӔĘɓҋ¤nљʺҷ҂ɮčʷΞνɍϕ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƝӔ®qѾҌȅƄϲ˘Ϊē҃ԫ҆\x9dɮ¯ԗыgφԞɁ˼҇·ѝҘƸ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222854.718825:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϙäѣ1қϫӝ3ȬύŇúɾҝśӣ\x84еѻϒɗWͼƕӀьӅ˵}Ơ',
                            'message': 'ӠȧǜcӁʰɱʴǬĐ«ɼƨĬѾϒiҥƉѰ˽ÞЙɛϠϺӨїӱƵ',
                            'arguments': [
                                        {
                                                        'name': 'ňǔϺơɭūѷϭӸˡȞȾȐ˃ӣөȉӿŞʅʄԒѮôîʧΕķĔЬ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ÒшѡҩyǰπѮό˻Ӿ\u03a2Ϭ˚ѹŦԁƐƂȌɫӗԄ7ЙнǩþӮӚ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӾԫȔȗʜĝ\x92ȬʪҦ\x8aȼѨϻ˼ѲNΈƆ˴ˀƺţėúsмɀҵĔ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÊӉҁ\x81°.Ċƣҕ˭ǟΌȸƿϿЊѽɜΝԝчϗĎΤĊĊԣáǑú',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222854.720188:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӗȂӿɒǟƄŠʰǴǅӍԑ҈ԦƃЃĘQԑ1ĔЂʛМΌɖ£Ѱ˨',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'aΙԘìƢ¼Ӛ\x85ӨŠ˄χˁѿʧďȿɡҮиҞʉŪɎɺúӸЅԑԬ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ŵǣѭNʥ§ʨĶӶYȡ:ǧǁ-'ɤɟȧѷȅyʍDˁ\u038dӎʕьȻ",
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԛŇʽ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222854.721544:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '҄АϥY',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'kƬ½ϳԜιΜͱįnѱиıƑː\x87ƯĨϡŘǦKқčª\\ԒȢ˙ђ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¾шΈҍ&ƘĀŽжï˝ӧɣҘԊƺ\x9dчѐ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɪʛńȹƅԫѶή¼ӆʫƀЊҲą҄Ɂp\x9fԜĵπ',
                            'message': 'WЄΩȖǚӵ˯ȁǍѧÊԩȨΛ@\x9dϚ¼БɌN\x8aΆôĈѬȆƹ,ƒ',
                            'arguments': [
                                        {
                                                        'name': 'ҵĲɺʃ/ɃύƂȻÞJoЫьˑǏʫΕηˀј',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҥԗ1œЬÇ˱ίˍЂ´ɥņ¥ѶςӯͶɡɣħ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѹʈӓ\x83ɠњŨϮұмʰčʺVЫϡϪɘǱй§ȩѴ\u038dʧȸ}Ĉӗӌ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'VӟΑ\u0383Š+\xad˜ŷ˽ěŇm˕&ЗƛŀȂүĲ˄ѐҦĒǼȳˏѾǓ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222854.725158:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'WΊʟҞŅʀƫʡӪ3xɢǀ΄2ȝѰлĵ&ŠĐПɏÿ+ȏ¼ө',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɲ÷µјÖǆ\x83ь4ċ¦ƜѧӹϿˊңơтОрŭҕϯÊҒɓǤӦԝ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɆиǶǯԮЀt\u03a2ĵҮήҧĨʞηѭƛϝ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'BƊȔ£ƃųîЏѥ¾ĉ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʌԛɡŪwˍλoɱϹɘŸϘϏƏ˱',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 676031.9678931811,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÎϞҫԫǱ\x80ЭĠ˶ӡ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϥҖ{˟žǚˣкѐ|ԙaϚʷğrɑЍ˃λ\x97FΏǛņηԬʨĺ˂',
                            'message': 'ԮίǎÍγ˟ː¾тѢӚɋŨɑϔӕŐӒǙΛŋNɪƂπϮǚŰ˞ġ',
                            'arguments': [
                                        {
                                                        'name': 'ΦƟƈѥ×',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5400646815807372731,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ìƶˋG±ȉʸ˥ϩԑӹͷЎԣЉϦĘũԃ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '=ģ\x83Ϧӝ\xadҐɫˠˎǤˢ&ƣʗΓϾϰҬnϒѲ\u0379ͳ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƓŬа˳ɯФўάѷɗ.Ϙӛϓ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -63019.61562997141,
                                                                        },
                                                    },
                                        {
                                                        'name': 'âКΗõҖʿyԍӬȡŘƂϕ\x7fǽϨ˰ѯѪêę˱πɠǞȈɟҸɩß',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 366744.5812713999,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʽπҽȓǟҰxɼĴǇŶ\x8aϢӆӄɦИ@+ϣ¾уºūԈģÄn\x85İ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˞Ŝ½ɟəǑäѶΒɦϼЦōνӼΣ\xa0ʝƥµ-ʋЖԏȨŠԂBʬæ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӊʿǯљ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ћ˃ʰå±Ӡ?',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɽԘ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˸ʮѥҪΜɧϥ/úѦӕИђԔоəԈӝʨ0ІĲɁԂő(Ϸʴɦþ',
                            'message': 'КʟќўНΆłү\x81˜ӞǡǑШǕǻ[A˲ӋƹǺѠ{ɕϔҭ϶ǘҽ',
                            'arguments': [
                                        {
                                                        'name': '˃ȟâѲƚМ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɑѿӿŻԖΐƸƌȃˣđĆһɘǬ+ԅХƬŵϨQѢӊЃΑªԄҥĳ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҂3˼дƦǆϴÎӀζÅȩʵɄ÷ȢÇҊñӛʝҞ˸Î˺ђəтϪх',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 614945.5298056063,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϣϊʊLĞɡŘҲϖƊѵŅŢǬ\x8fđwЍ¯Ň',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҨԊѬЬǽɣÃƙɵǶyԈ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'тɤâѸφЛƵŦΡ϶>ͺÀʐӊςӘɟ˯÷ҴжɧԢʘԝɇȮß\x9d',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222854.738127:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƟͶė\x9fȵdʂ"Ԣϡ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΦĺͶɉɯ·ʤԆŵȜɟάєƶчƼϸԖȏȻԚӥ˗ɡŰȡzJщC',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѨӿȁƸԄŷйłȓŜʡ˗AVľƭԃʫЕϪƿƀΔŖɚ˕ŸХƽ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'óųɼʁЀͽͻÐɄ±ȥȰĎɕȋǰƪϦΐЅʥφļΖ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƧƑΊɫ˔ҍ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 807031.2547728154,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ðάĮȾˢɎƽĎĝ\xa0Ç҇˭\x80фʺɥ˟ð˴ôΒӪΞҦ\x83ģͻ-Ԕ',
                            'message': 'ȯÒѮɏ®Ӫƿþǎś˦§ԚɨǣǓŰĤьӤѶѹЗҾȩөԝɋɻӉ',
                            'arguments': [
                                        {
                                                        'name': 'ȁ&˘ħƀӷŕʙ\xa0Ưʀ˔ѵɝ˶ƃǣȤδΣКƵа°ԍ´ǸǶϟχ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӠőʇЪʾǎƌψƷ\x94С˩ͲƾњӦȫȓǘʧɈƕԚɟˤͱǂg³Р',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɝȆ\x9dӼŗΨǇӴNéӴǤȢѮ˭ʍǊ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5131495652193976552,
                                                                        },
                                                    },
                                        {
                                                        'name': ';ɸˑϸΠӦ\x87пŝѸʃƼ\x9fϥġɰɹ4ſōӂԢёʌǽŇȵǿ҆ӎ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5690693876565659211,
                                                                        },
                                                    },
                                        {
                                                        'name': 'мӊʇҏЇȩΘςƉʊϠԬ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Őŷl\x8dҿϰɻӖ\x83\u03a2W',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҽТĺѬʪǊӅ²ʌ\x84ʧЎˑВ\x9bʲñŷЭʈîŭċԊ˄~тĶŲŕ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɣҖ\x9dʜØ˄ґгәʦȡҫϱȗũƤȞ3ѩқьʇνТ?ɧĈчȭʕ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԧπӿѦϖЛԒĐЗĄɳԇĭ\u0383ҠŷɋȂњʰŏɓƪҍүӢIɠǎӀ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222854.753071:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˎВƜ#кĔ·ŗęȹƚƠˌӏ\x8c',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӏʿh½˨ɝԖҸΐ϶ǛϖǍȐʫϠ˖',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˽јҋ˼ӄϼǻȳȳªЅΡÆƌǓĿХƫӖԂʨęŚѸ˨ƵЕáӳŉ',
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

            'name': 'Ƿ7·',

            'error': {
                'identifier': 'ζƠԄȂʪ',
                'categories': [
                    'access-restriction',
                ],
                'messages': [
                    {
                            'catalog': 'ĩř',
                            'message': 'Ȍ',
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
            'name': 'čɰɻʲ˛\x96ÐɱǈǛxĢȕɫ˳ӖAА£άњȆѨĄȚɫ˄ƥƈ˄',
            'version': [
                -4677230383630728872,
                -3417136715625468148,
                -235162804955993159,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '¥ΜЬ',

            'version': [
                -907121126407819646,
                -1064819214753218449,
                -633204822377255626,
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
            'event_id': 'ȯ˧ƃ˕Έ$ĉɲȍψ\x8aɟ¹Ȑ,ȿÇƄ¡ğƦǇϻǵŬŅɅϘˋƃ',
            'target_id': 'ґиŮԩԖNь˰\x89ΔӃѝôyĤɕѨХɐϞʐҦЯХ҇Ƀ˯n\x9a҉',
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
                    'event_id': 'ѬĻɬʢȧáķßӍêӄĸζԄǅԄȺԇɏЙńaŜҿǐ˔ҙĬ·Ʒ',
                    'target_id': 'ÃƹζƔџѵʢҏĆԑѷΜι8ʅ+ѫ´ȗRіǎ_уÍтЦǐ7в',
                },
                {
                    'event_id': 'ƷӎǁƷõĺƀĶҢĩĮΫʦőëģöâ»ćɎӌĢϣďXíŁԡń',
                    'target_id': 'ωӢȜďȸ˓ӜʹʌǫȧƾʒИßΜΡĀpƛŐȿϔŕƂΉŲɤƨΉ',
                },
                {
                    'event_id': '5ˋΗÛ8ӏgЊθδӑUƢ\u0383ıҁˉ\x81ʅʸ\x86§дϏӵʚĜҺɲ˳',
                    'target_id': '˦ɛɆˊȐӬΚΟȗԝǐĄȪʂdГǬʡѺнѩӁХˡȴIλ˗ы7',
                },
                {
                    'event_id': 'ʜίɡƏ\x90Ԉӂ˶éɥδԉʝӃѼΒӗɜүҹȽȧÂӈ´ƼЩɆӶʈ',
                    'target_id': 'ȫŧFɳζɗ!ĒʶƲ\x9eƴӜ\x96ѡɦ΄ɀӆǭϪŵɃбЍԇҩǒ¦ˌ',
                },
                {
                    'event_id': 'ξǺȴѥȯϯǻΤҹ\x87ȤԡŊ;ҬԛИȜÐtÄĚŽΩj\x87Ǥ˓ҷ[',
                    'target_id': 'ЧŷĀ\u038dɳ˺ЏĈԘȠ³ȫoʇђԑĕϻA;ƎԕĊ^Ҟұҍûǜӈ',
                },
                {
                    'event_id': 'ĈϳƗ%\x9bҠ¾sūϙűЬҕfɉŰͼψƥтҷ\x86Ō\x9fԮʨ+ÚȃĬ',
                    'target_id': 'ɛԧяЌ\u0381ȪҬɽMцπśΪɹƂȋӹғˁƐӨ@ϗЧΜȏ°ȀǯĴ',
                },
                {
                    'event_id': 'Ҫ(\x90(ѳϵԓɪԌɘɶF7ċˣ2ʢӟ£ɏ\x8eɔüɳʊ¨źǣҝс',
                    'target_id': 'вƹ\x8aӬ\x82\x97ѕYʸ˷ϲϑʞȝͲʪȴʳў ʼΤǊɁéƿʳtȫє',
                },
                {
                    'event_id': 'ҸǃЉǟӆ\x94ȩғϔԎǚô½ȾʐԨLԄz˸ѩǫԆĉсӒɒΫӟ!',
                    'target_id': '+ƩІгƐИθΏϿϰ#ŨŇϮɬӶҘȠїȧǽ¤ѭġșȰӅғԎҪ',
                },
                {
                    'event_id': 'ĨƱɐʌπuΓʍҖôěʄѐӹǣǭЩӆҟϜ¾Ї~жΒŧϛ¶ȯĵ',
                    'target_id': 'ȸԡĘϹ˴ӣŃƑ\x84ƓƀϕΗƅѺƓҹʜȐ¸ϟqϸφиΨмӑíÏ',
                },
                {
                    'event_id': 'Ϥ=ȨІǁČ҆ƀёϢϓŠϮԇʁЕԫǤѳјƚΚгʹ\x89kťǉкǧ',
                    'target_id': 'ɐ@ʋшӢʰԮĭόԞʫяϾĺλˉθǵɓԗÓż±ʘω҈ʝŪԔž',
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
                    'event_id': 'úѩƓƲě˻ȊҷÑÚŴёɓ˅țԆ°\x83¸ũŨζԋѓћɢǍИǷâ',
                    'target_id': 'ʼǠɗɚџѰɿ¦ңϳ"ȱ8%ԡ\x81ÐԮøԧ˂ЌĵρҲ˧¨ũЩ³',
                },
                {
                    'event_id': 'ҏӛ˘ȀӒɞʸʻĔΥwʎ£ʨʐ;ЍК˫\x97ѽŪϦ1ƫâȂʬƻÏ',
                    'target_id': 'ʢΖķʠUңҲȘхŹȘčҞћ¸ΆϐЕȩǈіʯLˎй·ŶƺǷʑ',
                },
                {
                    'event_id': 'ɋ\x9fæƫϯɁʕͱϤҪUÖ#ɉҌԟǥлȳøŸĮŝÆȥƀĺ\xadҶ>',
                    'target_id': 'ãʅˌϽ¡Ӑі>ŖĥÓʉąƒΘӃŝŜτōӜΦˇ˩ǧӤΩȮ-ʐ',
                },
                {
                    'event_id': 'ΏˑͷηϪ\x9bÜѝǈöʇē(ϖϧзĄԞș',
                    'target_id': 'âȚı\x8eӆ(ŃɜД\u038dΓǏǹȫγʕϨȢиΝȞº²ЧUͷˡиũΣ',
                },
                {
                    'event_id': 'ɮӑͻ\x9eȜԊIϫ#ϤâŰ˓˶ơŨvƲĮΈƋљ˨Ѱύʽ˫ĭԆԊ',
                    'target_id': 'җÕvЃƴʒ˚ҟрҋƇǲǤHϤҾɞǖʇуøęȲ"ѮŜ,ʉқ\x88',
                },
                {
                    'event_id': 'ƫÚŐƉßœΩǷғςλBЦśїыƟϦɑЇ˼ʛȋĎхϜΌȮω\x85',
                    'target_id': 'lԚșϑϤГӝŞˠȫȿŵƃ§ÔѺǲĝŵĝùϽп˹·\x8eĔĈǽ»',
                },
                {
                    'event_id': 'ϨȇCөЍˆѺ\x96ҕѿϠɔpүŔο˟ǐ¥İƸĔǛ¦˯Ƌˬ\x9fΛċ',
                    'target_id': "Ġʕăȡɦ'ŜBKȧ\x99ʲʓѤ",
                },
                {
                    'event_id': 'ºƠǃɭӬŧυϺǼàǞ\x9eΖӴͿҫùҝ9é¢ſɀǫΆӚŰWɵɽ',
                    'target_id': 'ϣǓі¡\x80ΤԋyĦѵˣэÁƞή\x96#Ԃ˒ǇЖÚŴşʆñӿǟӤѢ',
                },
                {
                    'event_id': '\u0382ӵǟѴеʔ\x9eϸƫԧФўʠ»ƱҝÒβ\x92ö΅ȣω½ɏǈː΅Зǂ',
                    'target_id': 'аԟуЋ¢БƚʲÖHҵĥÜÇгǂYɮƣЭʧɢ.ŝŻʠȫ\\џj',
                },
                {
                    'event_id': 'ǳӕǞĞϱ®ŖӧԩǋӄĴȺɭԗИƖʏ˥ʁԚЭԉǲʽȹ˩IԛΆ',
                    'target_id': '>фǣҮǧ5ύɜĮûпfэƾԅɹŐӰӄο\x89ɹØǱ\x83ȄԏɣҬӅ',
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
            'name': 'ʱȽȩҀđźʪƙ\x98ŖɁĜƥvƴ#DîҜ\u03a2КÉԦɷƨǺːɹȆϔ',
            'version': [
                -5434151906734177015,
                -714959414269243728,
                -4920297970238764383,
            ],
            'about': 'ƧӀ˱ʝˮĿɈϫүIΛŵҹœλƬʡҐũ˙ɈХǟɓÒĽȔʽƚȳ',
            'description': 'ӞчԌϩѻƗɶǝ?^ӼȂő®Ȥđ\x86ӿţʴaēŗʧоǆεϔÿŎ',
            'authors': [
                "Ͱҋ˧%ɏŨŎԈňѕͲį_їɯЀȏѭŀˉĻԛȻОČŲ'ʱґɢ",
                'ӓĬʡŪԢҩȐƌӠʁʿѧЦ˘ԛ(˙+ƶÈÑŋʓˍѹɗԮʨǷђ',
                'ӓȧ\x84ƤҏƴύH§ΕҪ\x8a\x8dΗ˻΅ԑȺǧŸƇÜĖ˃ѿԩ;ϯ˶р',
                '\u0380BΌƏςǢзr϶ѠDÉЪ\u0378ԙͰ\x8cȕƇΜɤsǟȡȣγŴτŸ¯',
                'ЋÂʤҹʜɃűΏΐʱ\xa0AƷЯҢæҩ˒ԝЏϜȗчѱ˃ÄāüƸb',
                'ɉŪϙÓĶɸ\x9eȍǙʢBπĕτқРЦŤŃʄȺΊɼԭĘ¤˕°aӎ',
                'ҳ§nʾϵҶ˒ΐĎÂǳӣü¤ɜԕȮϨӋЌɊȿѹԉӟŷNǶ»ģ',
                '\x87ˇɴҎлƀz·ҦϽuǝĔҳѭʳĮ¬@Ȋ\x8aĉÂѽǒ˼\u0380ʀӳь',
                'Ӯͺ\x8bЈŢͷ˽ԨԅŵζʊԍĀƷ¬üěǹÍθļҺͼ҄ɲŢλĺǰ',
                'ŖƋdʝ¿\u0378ŧɣ\x94Ԭɻ҃ȘȃϬ¤ʈlţҬğüűӝĴ˰ӄԢƽë',
            ],
            'licenses': [
                'ǪϔZԈʫԆǴԨ\x90',
                'ĥӳŒҿɓӆĵŠŦ҃ȈȱÔҝˏѥðŌΐǗɥʯɈҽ_%Ϣʸʟƪ',
                'ȏƁΫŚɖð%ɝԟƪPɇҶɜd\x8bʂΗ^оµźөĔˊҁÐʷԡƸ',
                'ǛwϾѕσϳϒô|ǵѐϸπƪӲɫļМǝȁΖĪ',
                'ʿ˃ʮΣǃʍ\x9dΧиƃäH҅ʚsΜĲ\x8dȧѿӮ±Г;ą¢ԎӐȞǑ',
                'ԋͱPșȧőĈъӑӊұłɊҺʖ¯ЊĵϝѢЊƁҬNaËƨҞϥ˝',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '*ɿЈ',

            'version': [
                -2658503398360939240,
                -5643023675996302516,
                -6590466174476501116,
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
                    'name': 'ȄʓпУŉ\u038dǭÑȚȅſ=ȀȩӲÃέКҀѝ\x8f˚ǄȐλ\x92ɔȔǗԮ',
                    'version': [
                            -604873438478340090,
                            -5026924485230895339,
                            -1939940436060397964,
                        ],
                    'about': '\x9aӋȠаĠΑѪҍӟ\x80ԡӇjПɓǘΞ\xa0ο/ʢɩʟąɻ\x82ʟ˹ŕӬ',
                    'description': 'ˎīϛԓЬɗŦѷώȐɶɅǟ\x8a9ΪϼȕϦΝ\x7f˴ƋϾϻӌʸʣ2ȃ',
                    'authors': [
                            'ƙμƬМӍͶДШ˹ϖȺЕĚ®-Ф˞Ҥǣǫ˰[ԋЇҡȦӗ1ͷƂ',
                            'ͲŜ3ßȷ×ǫʈϭԇԗєҬ˹ŝ˨5¶Һ¹ϴʤ˙˗цҫѽ"ґț',
                            'ϋϠƇԬ\x97ǯΤԟ˧MϩлvŚѻуƏ\x99_ŁӑĂε҃ȊbzɼЄÖ',
                            'ČͿØ˞ȡЀҥ¢Rӟùɦīħéġʱ',
                            'ɝËǽˤ˪ɶ+Ͳ\u0382ŲѣŔˀν/Ҙ˚ƭɜÀѯʤĿϙWɰǍ«ԏЧ',
                            'Ô\u03a2Nӷ\xa0ɝ³ТɌƆҨȃj5ɿƌҤƱɣ`ԗјͿ˴љԂĀѪƴμ',
                            'ĊЋěԃҟqҢӂˮFʚѡÑɒĲͳŜϖԨ\u0383{ѝƍ\x92ĲǭӐŰϋâ',
                            'őȁоѾʰӪȀҨ¤ўTшԂЯȁéδŤ.ʺυ0ӃɥҮʈϝгƅť',
                            'íŲӱĺΓϟǮͷϙĸřӳśǑ%ϯʬĠѤиʥŵcΘɇбǍȷȱŚ',
                            'тϼЭÐһȩɭКɞɢʚƿӼŪǧ҉Ӧɰ2ΔѰҮʷϤϵɁѩŝкU',
                        ],
                    'licenses': [
                            'ɁΎʣѧѧӆƐѕϞҰŬŏ¢ãCҕǁǡŪƖɶġϴԝ\x96ѷĚОԡԐ',
                            'dȆы;΅ҷοӷ5\xa0ĪÈěԇȶʚƠλŕЌĚƹäʿЩӍwòƥb',
                            'ıqҬӮ¾ĳрĲ9ͷοѬOҟԐшǽϐīȨrǁӑ`Ѳť\x83ǹȋ҈',
                            'әͻȍʅ\\ǦДЂĜҞŧzǃсɎˌʟɋѩǝԬԧӄҲӼ]ӊĞsť',
                            'Ƙ\x83ȨЇӺΤӯķƀԪdcͳǲΝĵҩÜˊƃӧȹͻ\x89ÙØϷdӁӗ',
                        ],
                },
                {
                    'name': 'č҉Ԭȯe\x86ȖӁfɵɅԞɓʨӟĀóЯmʶԔ©\x8a\x93ÎʑДѿ\x8aˬ',
                    'version': [
                            -1540778766481705753,
                            -1180407528065410669,
                            -7646166948272127647,
                        ],
                    'about': 'ń˳ҬȗŖƷϣʗԎ¼«ҷĕЀҔÒђӐ\x83ɗŧԣЏʽʗʃҎНĵµ',
                    'description': 'ëЁϵϫӢБӉ˳рʫЃʬ·Яķϫ˼ЅǷв4ȩ\x87ӊĥȱӿӶËӤ',
                    'authors': [
                            'õǞņӴϧvԗѭԋÜ˰ΈΏҥѰͱſǗƼ˳ɑѯʭ΅ӓʬ΅ʉØǀ',
                            'ԖӕЌӄĳŋ§ΌȒѶʼΤϋƾПӮΞƦȵϣ\x9fӧˠūќ3Ϣťɞă',
                            'ġЀЌϑĐӉԧbΗ,ӨШʄ\x7fǀ\x9fɘǗŚĬǿӲŚĂôϳίǮɎǺ',
                            '´ƚ¼χрːŊŚƉɱĝєMЮÞ}ʃЏç¶үԠцӼгöğΧʘˆ',
                            '~ҽ\x93ȑ®ÈΠӃ#ϒö"ЭϾʩҶѓ\x97ЪӒǪʯėìÆƄƵԚѣʕ',
                            'ƭˁнѶΘ¬˵ɁЮнȖɲEZǘԋâőȳ˟Řƾ҆ηˁǳлɷëϘ',
                            'ǿԞмˌĸˣψϒĕŧǲʣ\x90ϲǪңȠǵĢǪÁϝВϜÓʊӬυŋӢ',
                            'èŷ˒ыҶȥЌӗјЦȁÔ\u0381ĠŰ\x9bǸ,uǿƉДΪѪҤͰǎƗȿЧ',
                            'ǌ$ȲћĲ½ԘԔäϙʦӲǨɀԐсžìǏЮŋ\x9dǒȭùƆŀѤƴů',
                            '˦ӄΖÎš҂в˩ŏdǣɃӾĖʹɈ˄ΟѠŰϳůǲΆӆӞԕΤ¤ō',
                        ],
                    'licenses': [
                            '\x98ҽґдҶҸʳ&˸ϬbơΈØѳǵŃÚΣԣΘЌɠѮ˽ЙϺˁ\x80ɉ',
                            'ĿәǞΊȭȜҙ˾eöţȳҞΕϙɃҜ\x91¬Ȏĕ)ӌ5ŁJϭŪqM',
                            'üYäΒĶʹŽɴΌʣ\x93˓Ԉ˵˳Җ8ʠǆʰҟŚӝǷǕśÔÌϿĤ',
                            '3Ǜʪ;ҫԍ%ԓÒ˹ȥԪ˄ԔρƸѺ¦ȫɩƴŽвʁʉĵ˦ϥӇϞ',
                            'ɋΏӵX҄ΊǶʸɍȕƔҶͱİŞ\xadπ«ÁʞЮþԬӔМιô˃ҁ\x96',
                        ],
                },
                {
                    'name': 'лѱ˧ѸЪцİˊǫɄ\x91ˢȜ£\x8eʊȀʜёȥ˚ϒ}ςɞmĦġ«Ȝ',
                    'version': [
                            -3030668381801705853,
                            -7711465773679009416,
                            -8728435799840389363,
                        ],
                    'about': 'ƞщɣΆϧѴāйɀhЫȯǂμфɰèԩԭԩӻιБǄӚҲӀБҜҺ',
                    'description': 'EЄAԉĿϪԎѪ\x95Ȳ\u038dƨƆKĢǌėƾӴӨˑÛԔ˵ÆçϨɂ\x8aA',
                    'authors': [
                            '5Ɵʌɾ¨ǰԜԬJЈӤЎƋÆĝЖ\x9eǋҍŃϴΕұȧҳǎӘμǜӆ',
                            'ғ˧ӚLŒ˝ʞԠǜŧĻ¾ɅԙϨȹøԏÝ͵ãӗȓŇź\u0381ƾΡÁª',
                            'БрȐԙɕɶ¤ÚҊ˒¾ԎҁF½ʕŒƓИŤϬʼŪҿƇӦȗǂҋǿ',
                            'ѣѭʾȷԩʆɿuˮ˼©\u0381ЪӮħȮŇɺͼÿɘІê;31Пƚǘ#',
                            'ԝʜˋĆǃɞνɣЇƽɨÃɸŗɎÂж\u038bʘѤϋʣԔ5ңİʍƕǇӜ',
                            '³!ɍǳлƓăʉȶªŢ*ʂçӴ\x9f˝ýӊ·ΐҚӷ¬ʭҩԉė&ć',
                            "'ГԫƆњ/ɁшЊ!ɼ\x8eӫѿμ\x86ɲХɏҴşȢ\u038dԀØЌǦƝȠЧ",
                            'ʼԪ\x95\u038dRɳˬȜoӌǕбōϴԗƽʙʫȃȈǀȤŘЩΧÐüϽƫX',
                            'ԋ4xЙ\u0378ӈЈΧϖȡĞЍЍôҡƆʟǢ\xa0ðŪĪЈӪ\x92ÝȲӔěЏ',
                            '\x8cԮΘѰѬќВÓdҨѥͼЧϋ¦ʞɁÁήз·ӝ²ȓǓÚѠȍvɋ',
                        ],
                    'licenses': [
                            'ԖȑϟъȾΛԓϧ˃ʡɮɊсͽƘԜǙ_іы·Ƚ§ǵĢĊȣϩ˅ę',
                            'ӟɑųοϊʡÜϥǮǔèҢз˘˓ÏĊqЭɡSԜȫЃѣĿ\x95ѵİМ',
                            'ыȯǠǪҿƺÛЃϗɌҰцiϤχĴΠeȢ˥\u038dЩӆɿ˶ħĊʗһЕ',
                            'ͻҿԍʇˬӟÑʅq˱Ŵ±ѶŽeШȝˆŅύБnĴïϤƨΎRѰǂ',
                            'ȷԇÈAΆ2ĪűӚ=ӤȻ3фˈ\x88ȐԋчώɊДȜ\x7fʤȧħʺŃ˞',
                            'ÑѱȪˁґ\x86\x86ŵρȊзˀϡǯɑͶˤԪǽϓʃΨȭ˝]\u0382ƥʲPȣ',
                            'ӪȆ|Æˣʲ\x9cɹµфЂȉŝΥǄʐШ\x86ҁˣˠƒ\x89ƷӍ˃ɳų1˓',
                        ],
                },
                {
                    'name': 'ʍώĝɧ˟ӓɢǔũт;ϭǧьӥѫ\u0379ѹеӂÔȖʞ\x9f˯҆˵Kȣʯ',
                    'version': [
                            -1189694209370191416,
                            -4174105334352436803,
                            -6644449270913010405,
                        ],
                    'about': 'ҟͺĘŨˤҊǅǼȂ±ѪͷǟсɊuцǋ,¥\x96ϐҵȰѠˮǱȔƪ˅',
                    'description': 'ĭ±Ѭ.ιȈԜΟхũζΜº\x98ϹJюӉŊăч&яĢңʁԕЬóȄ',
                    'authors': [
                            '҂ԗԄӈҌԦÅğˌȑˏʘǂЇȎѼȟҵϲӇǲ\x9eőɽˮԇЙ\x9cЎğ',
                            'ĲɠĆԙï˸ħĪ´҅',
                            'ѪÓС÷їĠͶĒԔϫvʺԥϲҰȞЩǱΰҷҐԍϩХưkԁĈŢ¿',
                            'ҤŘŁʿ\x9aƔ4ðӌȭҶKȍНԍ˟ŊλҞˬԄΛІҵƍˤ',
                            'ȍȪΏЗˀ/2ûĿɗԜƪ\x7fǦ.ϜΗǇčΥæϣTȑĶÎˆҽԄҴ',
                            'Ӫɨѧī˱ȿѯŚŴҤÞ¦ĹҼʖʧ˔Ԏĝɤ(ƫ;ǰεʲőȫ˨\x95',
                            'ԈөӇƠˍ˃ǣɀԃ˂еЂɤÑdВйћʸɘȼнĽҮǮĩԔҼӥ˦',
                            'ЮԣҎ҆łǥҽΰȌ;ƗʬmԉŤΨϼοáσοΩƥϕЌá\u03a2øєȆ',
                            'ĈӞǃȸԥЍӞЙȄӜʷĝɵ΄ʽSкȾϟ',
                            'ȼˎϟάíήBҔpŮāʬˁԔҠӾĸ',
                        ],
                    'licenses': [
                            'Ȭ\x86,ǪĨɳóӉǀʬѝҖÚΜʁԪă\x81ƋΎǬū\xadОќėәϱOŝ',
                            'ǊŻčӾˡɅȍҹӤӁЖͱф¥ȲƁƯɥӳJƜ˺ǎéżӀơЎƗá',
                        ],
                },
                {
                    'name': "ԬƑϚɶЖëƶ˔ĂОБԀ'ѯ§˝ίȁ2ŸΥĳγÂѬϤďёÐǶ",
                    'version': [
                            -8922430881297410602,
                            -5753727412341515169,
                            -4733173777709334834,
                        ],
                    'about': 'ǧҸϻŜàІƏҜ0×ʞԥ\u038bϴ©҆ӁҾȶª·Γςê»ɐӦœҳȶ',
                    'description': 'ìʘ\u0381˼ĦξʃɿʎŴȼȢТчуȃѥƿNɽƬӹԖʵŊɵɤƆ`ʄ',
                    'authors': [
                            'ҖѸ´ƀȔłӎŬўΏӍӕɦӃҸˉѹӬ·Ϯĺ?ßŻҫɟϗйѕѲ',
                            'ϰǱΉąӚʺЯξƅHȑʲϢÑиЬŠĘѧщԥɋˀʞˣяŘǴȀ#',
                            'я|ӛtπƘϮԓköȨãʙňưîâ(Ҍ+хʊШѬāĖńǺΓ\x9b',
                            'ɞɨɲǬσćʢʙȨԋҴćĤωгF§҃Ԑ\x9fƶĘǊŠøЁяӪlљ',
                            'ѥʓӘǎюǄ;˰υ˷ĺŭԗËÑҶ',
                            '҃ʭɷÚϋĉТҊӓΈЛ˼ļϬѸЇƣΥĐεϛ\x9eƗ˹ÊϹБæͺΩ',
                            'ΊԆƚѺҴʗǷΝ˷ɳˢѯҏ˒ɽäěŭĞ¤ĻΣђǺˤɄ¥ъaΘ',
                            '6ҫʷŤɣŤɔ§ϲƝϏVјʣаЁƑϰĩэ^ɷȐӺ˻\u038dȗ²ƴҷ',
                            'Ɲīȍà\u0378ҘĖ\x94ŬŧѢΓбȮƉ\u0378˟kĽ0ʺƩΓ˂ŭǱʘǈӠǘ',
                            'ľĳҶƀ\x8b˲ƂҕɝφԠßé¾Ĉʭȭ˦μԓ',
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': 'ʚŘнȏзΫ҉ʀ˟ʈ\u038bJǱ¨șʦgʝɗƯǄϹ}\x9bҳȑƅѝ+Ǘ',
                    'version': [
                            -598848178924867455,
                            -5685692384279468406,
                            -180452230931117960,
                        ],
                    'about': 'ԤŗΒ|ŮҏҭЇ6ЇoɞņљǤʈ˖ĲυƧѮНɠϻʵƩƽΒJѝ',
                    'description': 'ĠΧɛ×)ƂԮάÌÑ˼ϖŠ@Ė˕ư§ӵ\x8fǽɂЖВʩȲǡŎ˜ģ',
                    'authors': [
                            'ΰϹ\x82hҎƈ',
                            '˛ÖӨҍӓ˕ɴϴďɇÛϴҼɇʪ4ǟc2;ϷǺųʟɅɖŴΎêӔ',
                            '/мrΩʼĹΪɼŐɪɱ˵xКұǝʥ҇°ĀƜʅ˫»˹\u0379ȰЎ\x90ø',
                            'ϼĒȾзϢԞԄœϥӐ6ŋĘțƆ#\x9eΟưІɈCŕǣɿBƸѢáэ',
                        ],
                    'licenses': [
                            'џ_л>ǠȞĚҸzӐűĈšΠȿФʖģċԬѻŸĊʝŻq˚η˟ɶ',
                            'mɟϕϱһҿſдѼɏεŔҊϛı αԛЁÅҭждͳшҚљЛďԧ',
                            'ħѡӯľʥ\u038dµй˅ίϣÔʸˈ\x9dнŔāҁЫҌ˻ˤɐλǒͲӑŔϴ',
                            'ƮÐѿˬҸ¡˯ĆӱƂ²ˍɀğǇϻњß˕ÆƗѪ¨ҭњǷѕȍÝ%',
                            'ĝɩЩfɄżϑſ˩ċНхƵϽҍ(ƐńϭðƑƝҸ}ҁґΡԞĢÁ',
                            'Ïšϯ4',
                            'Ȍ\x97ЗőұŌȓÌϰЙbļҧзϖɀTρϰÖрѴүйǿɐҡΌώΡ',
                            'бɭ˸ԕȸϡŻʹĖȔӿƱŕʯ\u038dˤɟӓƾȆhӣҵѹŁ҅ĄӽԌţ',
                            'ƲқϹӨ¢ʍǋťɐÁЂО\x8bÿƆķƸǐǻԢ',
                        ],
                },
                {
                    'name': ':ʡèʁǐˊĝңӫӄƼҜѻӤƜ˟ǿуǴʀȯʥǛϵϨ˷góȴǇ',
                    'version': [
                            -5759808156849120548,
                            -8113967794857609582,
                            -3371927787708094350,
                        ],
                    'about': 'Ԓơʰø{yԦ˃ѪͿƨǃоɶӝčԟҒŕ`ϽγӐА%ž-Ĩņϟ',
                    'description': 'λ6ɁƸ¤z\x96εǮϵɬŨXӌǡ˪\x87ǛКҸрȷXуʵѩƿœˢƢ',
                    'authors': [
                            'ЮăʦƬl˛ԢʨĻТəĆɌɔnƃԎВŃǼʥÍэǲцˮԨʮϲμ',
                            "ĂϬТ'ҡkΚİƒѷūМŇÄԚʋØʃńґīɻβïǤˮɿē\x99ʶ",
                            'Ǧ˨Wϱ©ûÎˇұ8ԏѫģŢȁɽƊǾɸΗǲǏđʕÜЧȝϦԩÉ',
                            'ɉɱǱʲ\xadӒΩʁϭßƑӽÒʍӘŇŧКΩҦˎpҵDDΌƦС\x83ϓ',
                            'ʐӴҚNͳӀɂӡĩϓ˳ǤЖĤǞĊ®ŴϭƵҐԋǻњӬßĮȄϕƖ',
                            'ԬͰ/ʛˁģЏɨЧǏȱʒ˯Ȼ˹ńϑΝѨЊŉЌʕQɷ,Ҵϐв-',
                            'ҼůƀŨɜ˽ӅѬωЂ\u0380ÞҧþGƐ.ԡȕϦҘԭʹŇҜˉјшϋӁ',
                            'ѭƟşϼǦMЯҴӧ\x86LŶΊϴʖɤɻŚ¡ȟį\u038dęòҵҢ\u0383Ěɝŉ',
                            'ɻиä˷ɣ©W[ԥųOǼ˱{ΨɬУԔʐΚʟʾ˭ѭųѶ/2˳Ӝ',
                            'ĴƄƫʱķǭîŸǹѽ\x99ŊӛӲ)єЖ¥ƍȀƻ$6ƐԃØұкʗʉ',
                        ],
                    'licenses': [
                            'ʛΔʘǄĢÒǂțɍɱˎΈɰкͻŤʃϖGϛҢ¢έţŚȬҔĮӿӰ',
                            'Ȓʊæ\x92êӶ{ʠϠӈԥӭѵ\x9eɺ˥ƧɘȆ ʡӆΆЁɋɆƗԌēČ',
                            'ΥЦƕŏ!ʵҌŅɵÿЙʍԆ\\£ϮԮÁ\x92ʀ\x91˯Ĉϓ1˗Òǭɋѣ',
                            'ġʳɁıΜѵЫμϤϮƹˍǂõѕӹöǘȝɳȴεƲΘȀӬ&ˮϥӹ',
                            'ąˠʠ˒\x7fƬȬ\x94Âләʱô˱ҸťўƔѵȚûȦ˞ůЏÉ3ÎѰǢ',
                            'ƆˌкϽŴǭӬ˩ˎ\u03a2Ԝȓö:ȓҼӼӢɋ\x83ȚѵÅ¡JϑЪŨšč',
                            'ψǊӗЇˊƓԎЧ҃ұ,ɉѳĨȼəӯйĎΏ*ȮϙƑΉмԍJǔϝ',
                            'ВЮ\x8fѢȌśĚϺҋȒɈϛŞλԠ\x99ԃǙ%\x8bɷәҘΚĐnΑύΏˈ',
                            'ӗƎǎѷɒͺҔǓĪǝûӕʌʦǶɛӱ®˃ȯ\x82¡ƍϩƖҘϽ\x7fΉſ',
                        ],
                },
                {
                    'name': 'ӘΑϲȽ©Ĳ˩ˌ\u038bɏ`ɔńұ@ƫÍҐɯŒǣȆԊɊȲыƷϪЧҗ',
                    'version': [
                            -414705675508748047,
                            -4133443607561184477,
                            -8822846795274997574,
                        ],
                    'about': 'γĿŇĿȄ˙ȡл×ӌÍɾ˒/Þ¼ȡĉίӋĈƳȏӥŵҝԭǗӂĸ',
                    'description': 'іΡ>ü҈˸FĂàѩԅ¾ΤǕҪ¯ħЃĘҪӹϊʧЦԊÞƲĲŚԚ',
                    'authors': [
                            'ȷɹĜΧ1\x9fПŝͶμϕͿƅбŅȆҢ',
                            'Ǥ±ōÎԅҋʨȃ¢\x9eĦǃė˝ОȞ°цśǩȿ\u03a2όѲȀȆÖx',
                            'ÛҺ҄ɡ\u0381Ȥ\x8cіŧĀæ+ԙЁѲѶ˜ʹѸɨƞ',
                            '÷ŘĂ˵ɪÎĚfҥ_ȎƜŀɿĤͱϮOӸΣќǾ˚}ЕFƁπƨȊ',
                            'ÒέЖϊǍȢǋmɴ½ıGµţҚǻ',
                            'ŇɌɰɜӇˁϘɒtΥӅсҫüϚЧǻҽ½СƚϏűσΕƽΖϝÈŒ',
                            'ͱǥˎԙʜёьĲßɨŷxРďԬˇҦьθԈ˖ɻŶԟМȳQɷȶЩ',
                            'αɢņ*ÞҔјaŐҗђ8˷ʳʢӧϷÍџŴǐӇŭԣĲǠҁ¾ʉ',
                            'ţШҨȈþώǮ˅ȳԒʺǝОԟʦ¥ӮǋҟĿŚҲȅϴ͵Ȃ˞ɭөи',
                            'ʓýӰϑœ\\ʕЕĨʬћεӟæȥԢӵȞϑϳΉɈѬђΫʄɭӁȫä',
                        ],
                    'licenses': [
                            'øԓĪɲ(ɆǾѓ\x9f\x8bIίҬqϷȌϘ%ȟʣ϶Ÿφ\x93ȣǣѻAѷķ',
                            'зѝ˙ǭ|ʔҭΪOƫόԬ˝ȺƯ˶ӹҘżʒɕʟGƱƻŭŪĪÛҬ',
                            'ɡ4ǪʫȚɵǫģϖǇ9ĄӕƑŬƧ҂ZȊͰĸӫȒŷҳϴƏƆԊҼ',
                        ],
                },
                {
                    'name': 'ȋňĨŖЯԙ\x88ӕôŷϋӇȍàԡ',
                    'version': [
                            -7965813541503241806,
                            -361772521484181353,
                            -175843320478902256,
                        ],
                    'about': 'ÖǛӊÝ¼ϼ˻ϤʍʐĘӏԃɓ¹ÛϘÚͶí6\x99Л¼¾ѸȘóʮÜ',
                    'description': 'Ѣ\x89ϹŨƓ҇ȾӳϠ\x99ԃˣɑËǼŦ˳ϬѓƣȦ¢ϗϚСҨϵ˜ŕƈ',
                    'authors': [
                            '\x93ōÍώůǩƽήΌʹ\u038bԔŗҿ҃ȚǝnˍƧϥӱǘҲɑǋиŞãϲ',
                            'ȜϺаϫǥƾǾӠҮȒӝşˠÆɼ\u0378Ѩӎиɂї˪ĈŃԩԡϠҭќ}',
                            'ȰƷƚȱҥ\x9fŏϬęкѥѱɁɰ:RϸǧϊĮʑʿʙӥЫЫҍɫʍԁ',
                            'ѩđ˫¶˶Ǫҫ˺Ă÷ѵƉ˝É·ǆί˔ÝǥĹĦȇđǥɏԌϬR»',
                        ],
                    'licenses': [
                            'ҪG!ͱAͳґ҉jĒŢδȸ9µԉ϶ͽӍӿеҝ»ǖԢʺ¬Ŕɣʻ',
                            'ϧçϸlɎΫϹȸǍӷЬԂʲ(\x9dǏ\x88Ͽе4щΰÇӢfˑѡŴȿғ',
                            '\u0383ƅʟȫɘоDԤĢ¼ŨҡҸ\x8cÔϕʔȃųѓƋλτҸìǇɭԩǛƈ',
                            'ӅӛҁӽʰџƩâϹċԥϻĂάВΏĞЇĹѪҊ\x8eЃ\u0379',
                            'Ǔ$šǌ}ŅƕҩǺϭъůΖͲƂťʙȟMĆ3˙ͽҥӠџϪʙƌџ',
                        ],
                },
                {
                    'name': 'Ѫ˂\x80Ѧ҈҃ƼȃUčýűǒҰïњӑ\u038dɫɠρΤЗаťĂД˲ѶΜ',
                    'version': [
                            -168986738466143976,
                            -2119883751829646152,
                            -953452754763696946,
                        ],
                    'about': 'īωƛˑҀñϪa\x95ϝѶ',
                    'description': 'ǏȳΓ[ʸғˋĬøǴơӝӚƑé˪\u0383ѼѣҥρІ\x87ҽμɟӔƫК:',
                    'authors': [
                            'ӔϫʌΌ\x8dƠ˓ӶǜʽɕͱҒĤɂʴϯƣФˈ$Ʒ˳˨ЏǰƢ\x8fͰ΅',
                            '\x9cSѩСЗ\x9eːǾуӀҗǪΣοăǄ',
                            'ҞȝmʖȨ҃Ő\x98ȈԮĹ¹Ţ˵\x96Ǖ˅å±ǙĦ¥ƊЃӢĜМëϨ(',
                            'Ǣƃǳ¯ƜβΣˢƯɼMҳʒөŞȀŴˏЏǖҀǚ.\x86,ȶҕȶ϶ǉ',
                            'ҒʏŋŚŎѐβƺZ˃ĐѱȔ˨Ş\x80ƍƀ¥ƎːЁӧ˻ĢЕԑшɬĀ',
                            'ЗҼŨŝwŁɫѽƀϰрƢȜȄƄtϝӨҚ¿°û˻đĦ¸tѓ¹Ͻ',
                            'đ#ӓɂŁӈƌǫĖ˪¶sԧČîÐЀàԬƱύƄ¯ǯčȣШ\x94ƥʨ',
                            '˫ϺґšƆȎƪɣȦϬ\u03a2ϧξ˷ǹʯäŗRĵäš˝$ҷЛ)цΈÓ',
                            'ʏԏΧͳǼªŹшaрӦ*ӨƸў³ȜԐŌҕΊǙĝүàȘşĭЬϺ',
                            'ҼҿΓƿϺǅɇӻӖ\x9eɂϹОдīƪAώŭѓH?ƵѷϵƀƧÔɃƘ',
                        ],
                    'licenses': [
                            'ƪǋÅȿèÁbҩ҇ˇ¢ФȘȞzŞͱɭÆƑŬǋѷ\x844ˣӎƢʷ˦',
                            'ɻȫҔЌųʜČςϗѼĽʉŠúЍе0ɢԦ҆ȱАӱϷ\x97ķđԚUι',
                            'Ĕυ)ҡƑҰƏТ\u0380яФʤӹŢȊϔƽ˔ϐӓѬƍҘŷ\x8c_ѲʍȊȠ',
                            '4ˬњuɤǉɵɘFƜȚͺȪӊɭ\xa0ǾϗӆºԨȐ\x9dԣ.ʮҐцϫ÷',
                            '.ύӁɝηøµПŰԠãèaȚҥˀYч»ǤʝϓŸȆHĵԃгʽК',
                            'iϚɷҖʏĢԃĤɨЋӆӈȺ5ҀѠ»UÏ\x83ǭƎƫǋή/ÌĻпē',
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
                    'name': '\u0382кӗ',
                    'version': [
                            -4960591432506455607,
                            -2910006346045411822,
                            -3602384556788059924,
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
