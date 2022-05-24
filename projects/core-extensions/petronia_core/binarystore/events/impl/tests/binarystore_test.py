# GENERATED CODE - DO NOT MODIFY

"""
Tests for the binarystore module.
Extension petronia.core.api.binarystore, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import binarystore


class StoreDataRequestEventTest(unittest.TestCase):
    """
    Tests for StoreDataRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in STORE_DATA_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.StoreDataRequestEvent.parse_data(test_data)
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
        for test_name, test_data in STORE_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.StoreDataRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


STORE_DATA_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='mime_type', name='StoreDataRequestEvent'),
            ),

        ),
    ),

]


STORE_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'mime_type': 'ΨфҼdʮЪʚɰǆ"κɞĻâϔȥǕȹӁгȟ.˪\x88ҵтɚÌĠL',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'mime_type': 'Ӓϳȷ',

        },
    ),
]


class StoreDataAllowedEventTest(unittest.TestCase):
    """
    Tests for StoreDataAllowedEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in STORE_DATA_ALLOWED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.StoreDataAllowedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


STORE_DATA_ALLOWED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
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
                res = binarystore.MessageArgumentValue.parse_data(test_data)
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
                res = binarystore.MessageArgumentValue.parse_data(test_data)
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
            '$': 'ʕÜ˯јΗϑǴЍсʲǎΧGϓҺ6ԏҺΟɄŮљҒʀȅҽ¸Ҝƿƹ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -1891927098019114270,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': -57721.32695156699,
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
            '$': '20220523:220032.674413:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'Éϊ΄ђԛϤƨȎ)ĳҞSϕÞʲĹ\x91ǷƜűϴĴчӭЁ΅ѫ˽ѴҞ',
                'Ӓěѡ҄ϵÖéȬʆ1ȳҷҀˤŋ6ҕҁ˟ʜƫȳ8ȳʍŬǋǂЉӭ',
                'ҏbѴӼɨ«ƀAɡԁǲϖĳҢҮΣǥýaƪŞȥќƅ˫Œͷζˊ҉',
                'Ϧԣ<ǦρˆЈΌ«ġŖϼӰñɒоΨԎÂǖΩ\x82ҰŽŕ\x81ұ§ˇĽ',
                '\x91ZǱ\x855ǷǅŪˆ\x98ђʕŭΓȓƶэ -ʍĐ%ɟρÀʼˏ§Ĥӧ',
                '.ǿǝӾҀ¯ӇȗΠӘ`ϲʯХϗŶÔñϯРľΝЛƊĿ˴Ѵĳ"ð',
                'ƈҐŸǾʄΆǀ(ʹȡŽ4ɛƖŔʁҷ\u0382ȊΙѼʛgƟϣ˒Еƍһә',
                '8ҼʶҢƁ\xadɝνƪýʢÇ`Ŷ\u0378ѾĪ˺¼ԘͰN¨ͶȐʎϘ¡Ł2',
                'ҒNa{ȒƗæҸќѯԏ¡BѲӞ҂ǵЫĢȅВ´øѵԧǚҁ҉îы',
                'ĿҷęļjԐɌΌɖĭӱƮωүӹʧKeԚǋұы˟XϞіǢĜљԐ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                3478104774786986378,
                -3153386627653569613,
                30954963179430338,
                -4943063041333459044,
                2873684409988664009,
                3367009772502392354,
                2578546868807272829,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                727514.496951691,
                899721.7606930512,
                758180.4993256158,
                576942.9257287943,
                895518.4684967013,
                779755.7502363473,
                762782.299678643,
                904230.5937165773,
                839923.7565005611,
                801069.255154821,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                True,
                False,
                False,
                False,
                True,
                True,
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
                '20220523:220032.679042:+0000',
                '20220523:220032.679129:+0000',
                '20220523:220032.679213:+0000',
                '20220523:220032.679295:+0000',
                '20220523:220032.679394:+0000',
                '20220523:220032.679478:+0000',
                '20220523:220032.679560:+0000',
                '20220523:220032.679643:+0000',
                '20220523:220032.679725:+0000',
                '20220523:220032.679807:+0000',
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
                res = binarystore.MessageArgument.parse_data(test_data)
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
                res = binarystore.MessageArgument.parse_data(test_data)
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
            'name': 'YɈŖ¾ƹǙǓƊYǰ\x9aˊ ӨҀøηϊ=șʥŷҫѮӃʿδļқɃ',
            'value': {
                '^': 'float',
                '$': 101742.4186566202,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'љ',

            'value': {
                '^': 'float',
                '$': 667155.9162730258,
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
                res = binarystore.LocalizableMessage.parse_data(test_data)
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
                res = binarystore.LocalizableMessage.parse_data(test_data)
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
            'catalog': 'ϭŃɽáҏЌѸʏˆǧǈhiŇƚ`!ϾDŻK/ҏӣ\u0383ҡрˇтƪ',
            'message': 'ʇϦĚ҃ΧЉŜңȑɚӢɞ˛ǭ˩ҎÀNԋļ\x92Ј)ËԒЬìʭζĖ',
            'arguments': [
                {
                    'name': 'ǸҙƯϔԛϞʩ˧ð°ѷȕĀ˺\x82ȔȰčóʝɓ',
                    'value': {
                            '^': 'string',
                            '$': '"ʭθʜ˲ΏҎɿJ҅ƪӵҵǵ\x92˸Ʉŉɥîßɽ\x88ȫƗ{˫\x89ζƕ',
                        },
                },
                {
                    'name': 'Eʀҥίҥĵҏю]ǂΕǐsοӢƟŗȮ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        False,
                                        True,
                                        True,
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
                    'name': 'φԭĩˀƊЩʊѯӤίγƛɝǕçʾζǕ|ϑнȻ%ȏ¾ħ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ɉѠ(ľξŷϚƙРӑѪҾүҸ\x81žɶŃ҇ˑТ\x9fХ\x83ѫЎǘý',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ҍ6ŌĂîϸĂѬӀʖɢҨӁİ҃˄ɼÃFŻûɃ÷ĳʐƯʵǏӌȖ',
                                        '\x7fγ3ҟÂԓİ)ÅĠǠʇҖЛÙʠΎȓoԤʀcҋʹmӻ!ƅʘԛ',
                                        'ĘѥƍΏƖƍώ.ΠŵŽҚï¤ȧϷȀ<ͽΜĝǸʩђωԕ˙ϋҭl',
                                        'пƄ$}ΆȻǳʃφФğäғΚʟƢԋΌҫɿ˼ƫӧſС\x83ĹˎԜ\x96',
                                        'ɳɟ´цzЦӸČΗŶͱнɁѿҘͲҺã\\ɨϪr!ГśȸˮԐЁ˪',
                                        'ʷôɣӱӞҌUҒôʏƅ˱ŪƼɠӑ©ʎ҉\u0378ӤǛЅƊϱƄr\x81ǾѮ',
                                        'ƗlʂҞӷǹƙȠϮ{ӈͶǋԥ˱ŢǱԑӥӛ¬їǩҖ\xadŉZ\u038b?×',
                                        'ƽŐƫɹȥʖŕҷΑο»\x96ΥšƆÊĥ\u0382ˈǭԏʼѺɕЊ{\x9eĂӱʵ',
                                        'ɧƧŁNΘƱґġźȞϯʷuͻƢ\x99ԄԔ¤ɓeЯŝɱŬbϭΆ·±',
                                        'ɆбΙʙԬǇӱԈσӣŏȇ£ǗïЮƽ\x88ЩцȢԬкӪǶ\x82ǭȣѪӊ',
                                    ],
                        },
                },
                {
                    'name': 'ȠкÑѠԊÏȍǾηˋûƥɕĹ?\u0379ų',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        610891.78035508,
                                        623353.653794696,
                                        385187.0149153691,
                                        323641.09088924713,
                                        -25600.86315146151,
                                        225458.5435793224,
                                        746172.397128206,
                                        504896.8178126422,
                                        34572.064044678584,
                                        506364.3897742467,
                                    ],
                        },
                },
                {
                    'name': '˓ɍԝдҋɩ£ŉɞѼϣϺʠĠΌͿ\x95\x86y҉ӑɠЛԅĸʈɤ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        907884.4860075625,
                                        700947.4518943002,
                                        65801.34521384741,
                                        397551.769342192,
                                        295998.14164945233,
                                        418767.84946879995,
                                        486302.8214448963,
                                        955824.9357007609,
                                        204920.26282938296,
                                        788526.5280391655,
                                    ],
                        },
                },
                {
                    'name': 'ÝɕҚ/üЦϥļԚӍѠЖԊ\x99Гǿӽ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        -49563.48688417895,
                                        124105.06382790793,
                                        -67440.22989089588,
                                        103441.42827648658,
                                        285622.0980834467,
                                        102245.82417317125,
                                        933139.0682664358,
                                        69334.36213813623,
                                        351917.6806279671,
                                        712538.8155395921,
                                    ],
                        },
                },
                {
                    'name': 'ұԭӱҕҪØΥԃʸϱŦIĩΦʹͽκъˉϬ\x8dɁ²ԝӤŋűƲʴ',
                    'value': {
                            '^': 'datetime',
                            '$': '20220523:220032.669374:+0000',
                        },
                },
                {
                    'name': 'ǠҮȚԗŵǭԏǍœɜÔƦȌ\x90єѶҘԖ˄ԮЎҗнȕʓĪƷWҦʎ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        '\x80ÎθԅLɣʿȸȕ6°Ͷ˄\x83ӿʔ\u0383ËāΝſɥΤŌ\x94ΓǯǭĤӋ',
                                        'ҴƦȵ]£ǋңϼԍƘԪńʇo\x8bAįѢҤǋʧұƾ\x91њ˧˫ÃƞҴ',
                                        'ǑțĦßГƲ\x85¤ӂЋðɎȅƋӌӭ˙A9ɪQѥԊҩŬґ\u0382\x96ӦĊ',
                                        '˨ǋɶʁʼû˦ƮƴάȬɃҢMɫđϢё«˨Ò\x98҅ƱýЖЏӚʠȳ',
                                        'ƀȇӺԛƞҡӀ\x8dϊӆЊƢ5ѐΒƥĖ©Π7ςfεǜӶI˲ǊȊѹ',
                                        'ѠΐÛůɫćƬʸȏѧΞӳȭāϊsѥѨϐ·İӝȒ,ƯźҙƩϝƋ',
                                        'ω³ΔɓȨK¯·FʚǠ˂ΥǵоҌΐ%=ɳг˧Ӵʓ#lÕ\x94áΒ',
                                        "ҜɥϽɺċĂǰ˰Ğǉ(\x84˷»ĚðɅǾıϺ'ÈȵʫʐЈҙƏƞŻ",
                                        '¢ʟѼǝӹѷɟy\x81Ȟˣ˽ȞҵʫɾęDsΞ]ǎѴˆΤұοѬÍǍ',
                                        'ŁĂˁįüˎЂ¶ҎΖҢкȯƺ¸\x80\xadŠǗПӠΨɃ2ǡȴϰǷȪǦ',
                                    ],
                        },
                },
                {
                    'name': 'ŐʂßǼ,',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'Ɗʝ½ǑȯĦáАΨ\x92ԧĿˋśȤ˚?ơÜRоȅ.ƾεӱԦǏԘΈ',
                                        'ԬпǺţƳɾљ΅ӞҢ~þӇËŦ\x98ХÏóϔ˱ȒϞȲ\x86ɤxҿîÛ',
                                        'ƨӇûʢͻͲŞ˜υǅʓʡʑțάĖԈĺºăÊ˴ªʍ\x9eňŝä°Ⱥ',
                                        'ǠƏ\x90ϙƭŎǈ˻ǀи²ӆ¹˃ŰͽƦǏоɳɒ\x98ɅțʍĻЙSѧś',
                                        'ԅǦǽÁӥҠåЊɇɓŜſǏʒɶΠ*ȨФǅξȐʆȦс?иƭό`',
                                        "҄ѽӝ'ĶɷąϮҏşԆѺғ¥¦Ϲф*ђĖӌʛǆˈӂĀϵʗ|ǃ",
                                        'əкïЙƶ˓7ŸȨҀɈ´Ľà¥ΞѡϖĎjǖϲčʼЧʈӃϪς¥',
                                        'æοҍ˔ɸʉԊŵƷʫńČøїDӄøΣԥȾgVƆĶάѱϠќό¼',
                                        'хͷHƼņԂҠǡĶӏĤ\x88ҙXe\x90ЫɋϚ˽˦˵ɮƴǑʃȊ¦ѷΧ',
                                        'Ɍ˫ʟɔӓ|ʦûґιФěʣȩЄѿĘǜʃ¸ϲҙϨͺέʘ\x80ɨĸĝ',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'EЭ',

            'message': 'ĝ',

        },
    ),
]


class StoreDataRefusedEventTest(unittest.TestCase):
    """
    Tests for StoreDataRefusedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in STORE_DATA_REFUSED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.StoreDataRefusedEvent.parse_data(test_data)
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
        for test_name, test_data in STORE_DATA_REFUSED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.StoreDataRefusedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


STORE_DATA_REFUSED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='reason', name='StoreDataRefusedEvent'),
            ),

        ),
    ),

]


STORE_DATA_REFUSED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'reason': {
                'catalog': 'ŷԛȓѐOκȞΠ\x90ɇŶ˗X˴ʨɭɨšӛȽѨѮƮʫ˴\xa0ŬҗфǠ',
                'message': 'ƭԇʌĥӰȟѕaοȥԈӢȨӃǙ˛ųϰɻĹҢћɛԍϕǲԦğˬβ',
                'arguments': [
                    {
                            'name': 'ˆƾғ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ǥkƥк˱d\x9dιǙɺ϶уɁƪԤƢԏǯΝʀǱ8}ӗĪžʏζǮY',
                                                        'Ŷƈұѭť˒˸ӉǏ®lωȠWӦÑ\x87ѸԭÖμƖЩ҅F±ы\x8c©м',
                                                        'Ȼ4ʴʢҊҫѡɨѾɟP\x90ԑőԝŖӪzŚɗɇӖɮɿ ¹ԆʣŊԫ',
                                                        'ȣŨǜҝ\x9eǄӓŦɤHǡˤƋ\u0381ǷʵɁҦtyӔΫʫʅʠьϱӊǔĊ',
                                                        '¥Τͺϼ˄˫˥ԢŽ˭ŉɌхħҷŻIЮЦ˄ŸҺȐԮͽͽ©ʲЂƼ',
                                                        'ұ\u038dȔǅŮʋυ˪ǺҍɈˏƵ¦ˠβԛΒҲΊƊşȪўŐѿǽĮyԮ',
                                                        'ƈԖąЄȇºǉԣV\x8dþʌȣԎǾѣ³ʔ\xa0ƚ˧ŚɞƗ˪˯˔ƈІα',
                                                        'юзÍ7śΞː\u0383tƁϸ\x96˰ӘÓΝԓʻŗÉƷ\x94˔ɊΞѮЇϬȱШ',
                                                        'ˑðƌӽчǠЇ¿\x97ӽ³Ƶ/ȩξMȹӑʖς\u038dįҞ\x84\u038dр˞|ǕӚ',
                                                        'īΑԀјÐȾӾ-Ͳºѣιũüј\x8cŔϤӼǯÍŽƏƑΪKƟԒ˪˪',
                                                    ],
                                    },
                        },
                    {
                            'name': '\xa0Χ_ƀɉĹҳ˱Ѳ¨ҁҪɋ;iӆ~Ӂιƙdӂͺ¶ϩƮÉЗхǞ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ӡσԔƑȟӭ®ԛʽųƎǖСΙ\x9bˣʹʸӿҌǨ\u0379Ȯ˩ƙϡʱ´Хr',
                                                        'ǉ[Ԃăˑӹώͻɒ÷ϔ\x85Ǭ[ƽ϶ЌҔʨү\x9cȄʪЊǜ΄Ǉϩ!ϝ',
                                                        'DåơƜúď¤мӳ˨\x91ͳÜɟȰ¥ės˦ѕðȤķkуĴɥѢпҨ',
                                                        'ϙĔʽťɵŉĐʝ\x96ˊЀŴʷŤΨȭӈҘϢƻ\x82ƐǂƏҀʯɜϥɞ\x9a',
                                                        'ȵΩҦȺIԦԥŏǽǺɌōԋВ¨/ˁċĔӶÙ\x86ӂҲţÄԓį\xadF',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӥ¥lʃ1źeÇtцηǾǼλДwԎЁΫʄ҈αҽǳʎĉȄО;Ӵ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        False,
                                                        False,
                                                        True,
                                                        False,
                                                        True,
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

            'reason': {
                'catalog': 'Ȯĥ',
                'message': 'Е',
            },

        },
    ),
]




class DeleteDataRequestEventTest(unittest.TestCase):
    """
    Tests for DeleteDataRequestEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in DELETE_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.DeleteDataRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


DELETE_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]


class DescribeDataRequestEventTest(unittest.TestCase):
    """
    Tests for DescribeDataRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in DESCRIBE_DATA_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.DescribeDataRequestEvent.parse_data(test_data)
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
        for test_name, test_data in DESCRIBE_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.DescribeDataRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


DESCRIBE_DATA_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='store_id', name='DescribeDataRequestEvent'),
            ),

        ),
    ),

]


DESCRIBE_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'store_id': 'ЩŰ˺ɡǕƎˀcȍѬФϻҷéήϏψGɻ\x91ˡ҈1čʤϤӷıͶç',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'store_id': 'ĨʣƆʀǹ',

        },
    ),
]


class DataDescriptionEventTest(unittest.TestCase):
    """
    Tests for DataDescriptionEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in DATA_DESCRIPTION_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.DataDescriptionEvent.parse_data(test_data)
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
        for test_name, test_data in DATA_DESCRIPTION_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.DataDescriptionEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


DATA_DESCRIPTION_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='state', name='DataDescriptionEvent'),
            ),

        ),
    ),

]


DATA_DESCRIPTION_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'state': 'active',
            'mime_type': 'ŸΗƧҪpљǏʐЇǱÊ?ԇʊǆΜŉԍĵ\x8eӈī°ǒΚøZӘ҆÷',
            'sha256': 'šťǵΛЏђjӦŎҜɵǛЅѸӤͰЙɣԇӵЉӴҿз÷ǑʳҚȂъ»B˟Ӻ\x8eυлɨÉŜɩƛаσŝώƂǁ»ҫʞԙȁҐƏϑŃeĵΑƅΑʰˎ',
            'size': -4402973616303542702,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'state': 'deleted',

        },
    ),
]


class SendDataRequestEventTest(unittest.TestCase):
    """
    Tests for SendDataRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SEND_DATA_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.SendDataRequestEvent.parse_data(test_data)
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
        for test_name, test_data in SEND_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = binarystore.SendDataRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SEND_DATA_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='store_id', name='SendDataRequestEvent'),
            ),

        ),
    ),

]


SEND_DATA_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'store_id': 'вЃɐɤGϳҖȹԃ;EҲҷœ͵ʠΆу*ʏȮʣʕҴôUΗ˂Æĵ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'store_id': 'ӆĄƚǑϜ',

        },
    ),
]
