# GENERATED CODE - DO NOT MODIFY

"""
Tests for the extension_loader module.
Extension petronia.core.api.extension_loader, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

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
            'name': 'ʫυǛĎ\u038bɔŘǶӓɸτӔύ@òĩΔć˹ѫŠɌŪ\u038dϡϟϯĥǰȈ',
            'minimum_version': [
                -7250331674205522441,
                -6952892515958131486,
                -7947999278623930353,
            ],
            'below_version': [
                -7428884176441682698,
                -2683166978628577137,
                -2481302455671927450,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ûȠ˾',

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
            '$': 'JЅӰ¸\u0380Ҟɐҧŕһəƞͽbʳԥџ?ĝʲәбȮÆɛъǸПƗӥ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -40658355304862584,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 281172.9060782984,
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
            '$': '20210910:185706.377345:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ϻΓԌϷӔΦSƒҦǫʶѹƗ˄\x99˦sȢȮǌʒԒțɎʾɲЖæҧӧ',
                'ŭÔȼƌҫġсgʰɰË\x85ˮѯϴʙ\x81ǧѤʹӯѹɎƠþǌξΚ.Ë',
                'ġώԑÖǦĐȰЕıɽuŢѨĠуЂѭɀəӠɓӺɁ´Ĳӕҽӵɋʴ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -2286690563118105213,
                -1476189845210948505,
                5733558375001497938,
                -8787151708493346378,
                -2006386141047637863,
                6543875117589459887,
                -3418171887688711316,
                -7249130625558566199,
                -5279019392149848794,
                5470350758578197616,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                -71902.71861527486,
                565705.2017950651,
                796213.3936461667,
                240095.62310229643,
                564846.4037336267,
                489337.15954533056,
                389688.7140190837,
                849519.6329665551,
                477929.2773322002,
                585380.3924770497,
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
                True,
                True,
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
                '20210910:185707.932797:+0000',
                '20210910:185707.954077:+0000',
                '20210910:185707.990645:+0000',
                '20210910:185708.010779:+0000',
                '20210910:185708.031127:+0000',
                '20210910:185708.083367:+0000',
                '20210910:185708.103787:+0000',
                '20210910:185708.144699:+0000',
                '20210910:185708.194201:+0000',
                '20210910:185708.260006:+0000',
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
            'name': 'Ƒș§ƑÓȨˊʱӅ',
            'value': {
                '^': 'string',
                '$': 'PĎPØ#˔ɏʀŢλѾӾȎįóX\x8fҳɺƺҁ^ưҡԐГÉrǍ˺',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '¼',

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
            'catalog': 'ǮƒɩáҵŉˀȔъȤÃҐтΝˉĲȯɷҴÒÓ\u038bţ¯',
            'message': 'ȩӾɒŨŢŊ˃ʹЗ$ўƙľ{ѠϟëʑmǺĆůÛξɠTΑ˙ î',
            'arguments': [
                {
                    'name': 'UѝϩÑҦЕɤЌ¿ʳ˧ɖϱêΊˊēĖҪň',
                    'value': {
                            '^': 'string',
                            '$': 'ϙųʔįʩEˇŽԞͽ҄ȉΈҖӞȴʶɁĊΪҒьįҹ˂ʋ\x8f}Ǐӈ',
                        },
                },
                {
                    'name': '\u0383įϖӧюˠҧȭçҒһу`ĊˀѰɲƬǇԩĥǰӓǁҸȞњϢϳα',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ΰg<\x84ĭɆɑϫǇӲ8ɯԦƁ\u038dšȀԈˬѫĚ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ʞʐȯ\x7fΘ\\ӢЅːʶь[ʯǍϞĎʽ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        24598.058537075034,
                                        770571.9451341622,
                                        52119.47478886045,
                                        903474.495528044,
                                        522193.52266978926,
                                        -88305.63119475436,
                                        -46595.98071634776,
                                        670986.7332683532,
                                        797456.815593865,
                                        871307.6878067598,
                                    ],
                        },
                },
                {
                    'name': 'Ɏѽǩѯсґη',
                    'value': {
                            '^': 'int',
                            '$': 6321660414084979824,
                        },
                },
                {
                    'name': 'Сlϵ8ƯͿԚЈҬãƸHʳʥҍɅмÕˇ)кʠƋĘӹďŤɋοѫ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210910:185705.440777:+0000',
                        },
                },
                {
                    'name': 'нЯҥƄɇ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210910:185705.512466:+0000',
                                        '20210910:185705.529407:+0000',
                                        '20210910:185705.548622:+0000',
                                        '20210910:185705.572760:+0000',
                                        '20210910:185705.590184:+0000',
                                        '20210910:185705.607736:+0000',
                                        '20210910:185705.624936:+0000',
                                        '20210910:185705.641314:+0000',
                                        '20210910:185705.662953:+0000',
                                        '20210910:185705.678918:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ɹ2ѸόńϵιдʅŕнŦȯӤԎԤѩƇӊ΄Ѭшϒ϶ґǦœң!Ǒ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210910:185705.783948:+0000',
                        },
                },
                {
                    'name': 'ϐŔʘӨ\u038b˂ūŪľƂ҂Ĭ˘ϴҘƶȗɤđˀƞԏɺŉҎ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'КΖ4H\u03a2я˷ϵȄЙċɭƁǏΡ\x97ϊɀÃɞʞɄĭśħѭ¥óӏϲ',
                    'value': {
                            '^': 'int',
                            '$': 4950889531107112606,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': '0ý',

            'message': 'ˌ',

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
            'identifier': '\x96ȂſW˔˔ïuÜΘǄƮӕ¹ÉԍĶɹʵȫӲ#ΦµҒŭɐÄԏӃ',
            'categories': [
                'configuration',
                'internal',
                'network',
                'internal',
                'invalid-user-action',
                'internal',
                'configuration',
                'network',
                'file',
                'network',
            ],
            'source': 'ȼҾ\u0380ԮӠɲ.fғŀØĊ\x99˽ǖû҅ѳĂΣ¹˹ĵʠ¹LȑŕҰǹ',
            'messages': [
                {
                    'catalog': 'бнǢǲǏŶİǡǋǾӇłҦǖøҧķʽˍǘԙ\u0378UӻƔǌȳ˹\u0382û',
                    'message': "ч\x8bΎ¬чƜυёʊ½ЍъǏŖȴ4ӵҗϊ'ϡϡ\x85˴mǗ÷ɴб¿",
                    'arguments': [
                            {
                                        'name': '`ʕѽήʢƦŹΎҽ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185646.263599:+0000',
                                                    },
                                    },
                            {
                                        'name': '˭t*ɮАΎѽÑѸ\u038dҶ¸³ӎʜԖΘӾɽĹɰ|ԍƉƛѱ-¥˜ü',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'žăԣɅЃɧč҇ƣӵϻұʧʎǄԈǖӘɼɾzҹʩʆɜӲ<ùВʵ',
                                                                            'îиѾαǵÄЇŴʁϏȽӨΒӬ˰4кǩɅЎιŕɍ\x8a©ϙɷҋ³g',
                                                                            'ԎĵЏ]Іӆâʱǎ˱Ò˹ҝƬӎŹдԅҠġѪ±ƆɚʬƜӾɭ\x95ü',
                                                                            'žǵě%ʺ\x82ȲȉȲ_˱ɊдoǔǄ͵˟ǧøŪɡåΔЅ^ɜEәF',
                                                                            'ѩĳġÊƉčЪΝʪʲǹӖӥьщɷϕɫκ\u0382ˇƙ\\ɸɸìî˪ðC',
                                                                            'ѬԔωʖώŀ²ȉƐ\x83ɦɫ˃ʬϘɈ÷ʫѯO6Ȉʠ\u0379ˊʕЅ/Ԁӷ',
                                                                            'Ǘϕ÷ěčҙӐȞԛǩξѻʁ˫ȇɷҶϓV;șЇĦɂŋȪŲѕlН',
                                                                            '}ѮΤǮàλĭȅӋʊŋӈχǮǟҫĚԗέγȎԖ«ÛóȇǯԎˤí',
                                                                            'ӧʅϰǯʫ-α"ȽěӐƁҏÒő×щͳԠȮ¢Úĝη˝϶ƜϺςŸ',
                                                                            'сԓјʩьƔϮӋμǯƙñAɒˆҬЙşʧΏ%ήӧȷѮ·ѹϏ©Ǉ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʹģƭƿјΠĹĜŊԍ<ƬӏøšԢԂúӽβɝ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'іІ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʣҺзʪ\x83ǩŬłͶVǑӆцɇҗɓǠңȈúХҽҜΓʑȃϫÂɂǘ',
                                                                            'һ-ȧАľɣĔӄƦɨȿIǹʛҊԌμ\x8aԈ&АσˁͶǝʃƗҮ`ĺ',
                                                                            'Ø\u0380ѐ\x8bŧʉžȸӭĠяǔрʜˣbúÚç[Ԧ!Ń8ʴəωýÒȼ',
                                                                            'ȴЁӤԀχԩȇщɔχͲ\x9eǳɻμ#ҘȎíˌӬυ\x8aσƷĵԝϘрѴ',
                                                                            'Ƙ-\x82Ƹ)ѥÅÓԮͱǾςɳ3ȭЎěʺƙ\x80ӶǜҫүжO+ʠɎƑ',
                                                                            '\u0382ԂҁDȭɑʼťѣӔȝԢ´ˠχσ˄ŋ˸λȝȅκǩӦӨВǛŠ®',
                                                                            '2«`³ӕγƙɀԓǑϼɟΏЙҁǄ+дҸ˰ȣ»Ǥ˓ȴԇЂƈųƧ',
                                                                            'yʳċĺ%чƒҩȊˏЭťҨƯԫ˯\u0379ӻӷɈʱʲ¤ĠȀ\x8aÑ˫Γн',
                                                                            'ЯӮӭƿԓϓΟŌƙεѬȰӿ×\u0380ƖŝµԧӫƺsӥΠΟǌǊʭɿϘ',
                                                                            'ɡġŨǡʁӯhЉʲȉͿʧĘʻѣԘ\u0379Nˍ8ЬȢϲЅӡʱʤ-ʗȾ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'џЀŊӫϡuGΰƼɂӍŹǑ˓ӝŦđŗ\x99ДƲ³ѼÒѓΔӦѦÆԠ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ԨғƾӾԞ1Ɍе6ѴʑÊӗԬɢŚжɭFŇϋЕɱx˯ѲѣJƪҥ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': '.ѫξŀƸƽË',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ÜʐđVҖ·˘¶Ɣŷѿ¹ƺΎɼΟÀƋʒƄʥʂҮȚ\u038d\x8bӍиԥҙ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6901439614068605782,
                                                    },
                                    },
                            {
                                        'name': 'ΎәϡȮĲǑӄƢљɒūǷĐAγфɬŜǴԒźʱ\x8fƦΔԠÚ˩ϵǨ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Џωԑŀˣԛʾҗ\xa0ŴҺ/rˮʢЅ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȿŠɵϚʄѹǯǚЊɱӸԗӶҳҏĬЈΐКϫƧȣÎħņ3шɄҩł',
                                                                            'їƼűʘƃάĠѽČɉƎ¦ʂƧƼūlƗǎɽЯŀØĦұӃǴ˲λѕ',
                                                                            'ϼ\x97ǳȜ@ʊѵź\u03a2ǱцґϨɍζƇС\x9cĂʎÔŃːхȌӋЉзӬη',
                                                                            'ԅӨʥƲʽҰ\u038bҤƆʡҳeіɒ˳Πɮ\x94˭żӲԫ1ԕơĊӁȆйØ',
                                                                            'ɹʟȶƬӼƛԝoǍƊįВȪõŇ˞҂ˌĞҏ˲ǌĚÈ΄ď%ǹǭś',
                                                                            'ǆɁĝҝӝȱСÆ¡ԘʰӸϦ²ˋŒӼȢѪʜ³WʛǴӉɖĄ{ӚΧ',
                                                                            'ξă˫ʖ\x80Ʉѝ\x7fĩȤϪӢŭәҮɽ҂υʉˮ\x9c®ɜʧӖǮ&Éȅ˵',
                                                                            'ȏΝ¹ˉáũϱ\x98sѥ˂\x91ŃžģЌʔ0Ԏƅ\x88½ΊԩˡˉҹŹҢˡ',
                                                                            '˦ťϨЉѓЦҀ\xadʂɹ\x83ƎԘUPʭɡрӒԓ\x94ϖʐҡͱλňƴТА',
                                                                            'ėЅԋӉӪηΙ\x80tcʧ˶эӥɕɉʔ҃ғ#ӕɺҺӿ\x91л҅а˦Й',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɈŷүκϫѿԗӴľǿɸʤéȕϸҿƭϓΜ#ɪƞδÆһҕЩ;\x9cƆ',
                    'message': 'в-˓ΔҺ\x8cʺ²ȘЏɣ²ªǻіƗьWʊ҆ЗϥȴˮŚЯrŽɕ\x9d',
                    'arguments': [
                            {
                                        'name': 'wƑɞBҸϨѣǆʍƍț;ǔϧȪΘ˻ӳɭ˂ѶѺƔЊȆϞ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 871352.6093287023,
                                                    },
                                    },
                            {
                                        'name': '˻Ǚ¸ɷĒˡҫӣԙδ©ĮͶǟԈыʰ°ʚ\x9c¦ˁĻ6ΨҎɞчÝɨ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185649.351103:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȖóøГҭӸ\x8aЉ\x88ϕӳ\xadКТԅÿʩơě0ʾ\x89!Ͻbş+˔Ȗʚ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӺȕȽԇҷΰɰėәťɟјΡǽƦΈƙΨȮźƴƌƗ\x98\u038dӺ\x9fΓӦӹ',
                                                                            'ɊŻA˰ёЬԁɅ\x88\x86ш˩θˁͲ¶|ӂµöԨƟé,Pɿƶ%ȮΡ',
                                                                            '¤ӗϲʺȜH\x85ʍƾǑÂúʬͺĮРѱ\x88Я\x98ŨҤĭđӫНфúӦ˂',
                                                                            'ЪŏИӎƽ\x88ʰѳӴͽҶjçǡЍˑċӴɕƈĞ\u038bƘмͼɎƃ˳½Ɠ',
                                                                            'ĎŌǶԁĚӘԃЬ\x96ѣԒ˻ςЃ˖ŶӇǀ\x9bɪǇѺԈmǈƊ\x88\x89ȿō',
                                                                            'Ԝɯ˙ɹˇǊӵԥΐǎҳşΥĉă˶ѹѶіˑѼP\x8cǝŧˌůÿǅȥ',
                                                                            'λőɱɶ Ǒ˷ҌǪµ˾ͻɹĎŮŜӕԉȄКԑїɯϸЗ´ˎǉǸΪ',
                                                                            'Vˇѻĺȣũ>ʷ\x92ѮłΜҋv˪ɮɇΓДЎƵĐˣυЩєƫʹƻÕ',
                                                                            'ƥǚįÝÔȟŲҸʊęʘƁӀɮҤί\x9aѠżůζƻ˙/ʀĬ˱xόԑ',
                                                                            'ļ¶ҦȔ˓ɟϦȵкм˂òϓˈ \x8f*ӑяűΙф[ІБҭԆƬ\x87Ј',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͼС҄\x9cҷČȍǁБ´ʹΎΡԀɼ¶˥ҠŪƁκÖºШӨ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 238427.0430878778,
                                                    },
                                    },
                            {
                                        'name': 'ϾýǲʽȡfċҨƤQ҂ȬГЁ\x80Ҿӄ˵ǯčπĹŻӨƺǶɽʴʃҙ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:185649.784472:+0000',
                                                                            '20210910:185649.802174:+0000',
                                                                            '20210910:185649.820939:+0000',
                                                                            '20210910:185649.839031:+0000',
                                                                            '20210910:185649.857539:+0000',
                                                                            '20210910:185649.875712:+0000',
                                                                            '20210910:185649.894561:+0000',
                                                                            '20210910:185649.912221:+0000',
                                                                            '20210910:185649.929284:+0000',
                                                                            '20210910:185649.946562:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɫбʣMƝθSҏ\\îİêɤΜ*ƳǣƃƴͷђѸaƝӕӊѼǰ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʯ.ЩwɠʡJгΙєРЌ͵˺PωѢǇĭȓνîѬ\x81ɸȷюЎÊϩ',
                                                    },
                                    },
                            {
                                        'name': 'Zʇ˔ѷɟǐ҂ʄƃӇаͻґюσ¿',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4027220146408011294,
                                                                            -3414053882319558050,
                                                                            318985818803586108,
                                                                            6062553981373064666,
                                                                            3226519230045571627,
                                                                            8322299929781187892,
                                                                            -2943367282972846797,
                                                                            2806399211904546500,
                                                                            -7774069880334852033,
                                                                            7466300549663799247,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЏǕǇі_ˍDокŹºǇěë҃ҔӜϔQƖôϑʗĆȻ˘вѼˑǔ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -2199.3034337056306,
                                                    },
                                    },
                            {
                                        'name': '.Ăқʹ*ūҝŢǥЅϤɋҳБҪӬΒ\x81ϦWáƪ\u038dƕϲƨ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 155519.34697551906,
                                                    },
                                    },
                            {
                                        'name': 'üϋÇ@\x91ß¥ҝ˙Ӛ˖ť˷ӾΫѩԊϗҪȋ5Θ8ΩУͰԮǃȥω',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԙѲѬɹԭɱкūԛ\xadЄ\x98Ė\x87Ç˪ȳȌɹӬʊԖʡƭƟХêǦǱr',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '£˅ˡξǰ\x8fѝґɣз\x92αщVƟәĦґʡʤpԃɧĲ\x84Ǿ˝аĒm',
                    'message': 'ЯΚɿ,-ʠƉˎѳÅĄƪ\x86ЦΩ϶<Ȕ=˒ǋʢ|ȜŠ|ҞÙϖ\x9f',
                    'arguments': [
                            {
                                        'name': 'ƃů\x9d"ӆ˞Πǌ§Þ˨\x84ȦΓщȬɣϿДђǁҎ΄ǶЕǀ«',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            934451.9936754173,
                                                                            327863.3934396726,
                                                                            691773.6157461373,
                                                                            888779.5440461611,
                                                                            500743.98646169493,
                                                                            26874.398782020216,
                                                                            241682.8017424749,
                                                                            629061.5206748425,
                                                                            260457.83720393875,
                                                                            570717.8769716611,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9eΤɿгнŽƀо[ԭ\xadԤ®\x80к8ņǨʑĻԫѱųЛħƠӁǍĜL',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'е.ӧ˷ɗѶөłэӞПӼɀӋă˸ʚýςԄͻȁԌӘ\x80HˎťҨԊ',
                                                    },
                                    },
                            {
                                        'name': 'êɺ\x89',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4721038527668703878,
                                                                            6480962749982904525,
                                                                            453073166095235571,
                                                                            -3682210205755166902,
                                                                            2837308858325250775,
                                                                            -3384457441378341482,
                                                                            -526646019169734119,
                                                                            2470878909771844711,
                                                                            2344760072555347958,
                                                                            6603084567323076627,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȣǖԘƽύũòĦ˅ĸВȑW\x81Ęҙ²R˛ÝŤˣáƇǰªɶԑҹԦ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȜƳΚ\x9bҡ¥ʦЇɕ¦϶ÛͿ¾ҥ`',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3086516411176517448,
                                                                            8411241419583110039,
                                                                            -8075542803537414225,
                                                                            -4226985016979620593,
                                                                            -6363349805541636406,
                                                                            -6018474861524120677,
                                                                            -3022174074504823028,
                                                                            -2701930968441795493,
                                                                            7471423575208538938,
                                                                            3529776030283222930,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'И\x85ЈęԖ҄ϊ~\x96ɘ× ʐԣя҄Ʀ®˛КƓӏώЭυŉǼԂ҉н',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:185651.743726:+0000',
                                                                            '20210910:185651.763113:+0000',
                                                                            '20210910:185651.782959:+0000',
                                                                            '20210910:185651.802587:+0000',
                                                                            '20210910:185651.824725:+0000',
                                                                            '20210910:185651.845596:+0000',
                                                                            '20210910:185651.865742:+0000',
                                                                            '20210910:185651.885879:+0000',
                                                                            '20210910:185651.906925:+0000',
                                                                            '20210910:185651.932967:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȓfȳ:\u038d˓ԏ\x89ż˚žʥǅϸȵӍʃɑūͷнȘʞ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:185652.024029:+0000',
                                                                            '20210910:185652.040975:+0000',
                                                                            '20210910:185652.059203:+0000',
                                                                            '20210910:185652.075992:+0000',
                                                                            '20210910:185652.093012:+0000',
                                                                            '20210910:185652.110519:+0000',
                                                                            '20210910:185652.128562:+0000',
                                                                            '20210910:185652.145379:+0000',
                                                                            '20210910:185652.162254:+0000',
                                                                            '20210910:185652.182524:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'l^QѲąүŲɤÃɽ·ɧ1ɈѐJҷ˶ʡȕѷƣϙӏДɝҐŒʢӌ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 699976.0181588534,
                                                    },
                                    },
                            {
                                        'name': '\x86ȗǊƋČċ¶ԪԘξğԗґϹӿÓÄѾ\x97їŕԎΝʹ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            488592.5540626602,
                                                                            530544.1718244564,
                                                                            275493.7744239993,
                                                                            508633.7930965766,
                                                                            700832.3172530942,
                                                                            459175.78247889935,
                                                                            42758.325752147095,
                                                                            776340.9681290028,
                                                                            306261.4922189526,
                                                                            708316.4145878884,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'мƟÿЬȏ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7102091603033412437,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ēҕɧʬ;НӷЦĮʡlɌҮ\x97ҙӉ¢əЙԣӵϟɤϺŤļƕĽҼƵ',
                    'message': 'ǔєƊ\x8a¯ԕÓf\x88ɇŖћƲƆԠїøҘȤʀɄҹɜӦĖѮȫϖӨô',
                    'arguments': [
                            {
                                        'name': '҆ĨәύaƢːТ˒ĂĩҺЛćϚˡɬ²ϹƦв¡ȥˉоƈƚԡĻƁ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 198090.83450439776,
                                                    },
                                    },
                            {
                                        'name': 'ȝФԆƲsѕʏǶԮИҾ˹˜ÁǺÿң×ɊJϣǏɩ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǐɗÖH˶ԝcƢŞԑԮϏЖҚƤΗģώƃѕ˳˻ƈˈȴҪϊґȚѠ',
                                                    },
                                    },
                            {
                                        'name': 'ʹĞ¹GЃ΅ӑѢ˫Ď§ˡЇӮ¸ѵ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8366526625897667638,
                                                    },
                                    },
                            {
                                        'name': 'оʝƕÝ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            156592.90436002926,
                                                                            453622.36940815777,
                                                                            886347.4886025875,
                                                                            78179.99230561018,
                                                                            735938.5156633642,
                                                                            -62672.834226177256,
                                                                            907273.1770123589,
                                                                            712170.4325241176,
                                                                            490422.82182880735,
                                                                            459446.0778810376,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҾƨђɪΑƪ͵ЋԟȝΗȎÅʘǠɕʏҪơ˵КӰԚÝ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 631044.6159780052,
                                                    },
                                    },
                            {
                                        'name': 'ϗг¶ԮũојКHƤƟӨƙӎĘgƒȒÊӻȐΤϙ$',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185654.064684:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʣɅӐϑѣрŋΨǛӧ*¨ӢȼȉϿӾһĉΡПԐϯуϕǌɲŮ\x8bϙ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185654.136101:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҟŻ˒Љɍbӛҏѭʧœ¨ѽŘŋӥԊũˆ˹ʈ»ϗӑΣðƬʼ˭¥',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185654.201096:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ҙ ь&ԛͷц¢˪ƹҩɐeȊ\x9ağ+άгѤĿƫëӶųķʥkǻ΅',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѨƲļGϼ@ЈɖʳҚӚѧБ\x8eĲДÉǖ˰Ĵԣ\u0383˺',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185654.557377:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '¡cҪlȁȺƣɅ\x83οЩҠѫÎ$ùȹЍϕƯ˱ԟ¬ԀȘƍԑӉ҆Ʌ',
                    'message': 'ЎȊ\x96ԡǳXþȄϜfҶӡЧˤɘ\u03a2"ѰƩȠŗ¦@ʖφŁҏ^ӓƧ',
                    'arguments': [
                            {
                                        'name': 'ȤǯљɓѕʙǱΜ˫άΒ҄ӤnɡшҨșgėͲԫѷΙáZĜҟʃԚ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -21067.999999684078,
                                                                            -65543.13681322137,
                                                                            642151.5387482876,
                                                                            789153.2674904113,
                                                                            823028.3421226791,
                                                                            905424.3066198973,
                                                                            850093.7834117524,
                                                                            204164.3231962899,
                                                                            89667.68819835666,
                                                                            -3308.9717601443554,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'еǰɬˑϻбМ]ȓǚХÎėŔȰʌѫóәȋưÔД_ҽŅϴ¼ːˇ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': 'eŰǚӨ҅ƔŝʛØ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'åǏ˻®ʗҷè˱Аҿ˴ȡWƼΫƚТ\u0383`ÉϚȓƯĝԐˆäЏφЀ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Úǁà˃Ɔҽɩ}ԦͱɄČǔȵԗ\x7fsΝʙԤXҸ×ǃHŽŀ\x97ʔѮ',
                                                    },
                                    },
                            {
                                        'name': '±ЁŽѐυӓʗҮψӺ\x82ϋqн˭ø˪źƫРʹӰщVӒ\u038bˑкʭҋ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:185655.412408:+0000',
                                                                            '20210910:185655.433542:+0000',
                                                                            '20210910:185655.454158:+0000',
                                                                            '20210910:185655.474799:+0000',
                                                                            '20210910:185655.492747:+0000',
                                                                            '20210910:185655.511517:+0000',
                                                                            '20210910:185655.531103:+0000',
                                                                            '20210910:185655.548664:+0000',
                                                                            '20210910:185655.569780:+0000',
                                                                            '20210910:185655.588691:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӘƇ_ѕÙϿɚ\x9aүΌaӄ\x7fƓ҃ÃƜȾɑǌơ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 950513.8730389313,
                                                    },
                                    },
                            {
                                        'name': 'ăȜ¿ǽǡĽӂӱĎ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\x89ɆǃζÈĥϖĴʶ5ѮaҭҹϼѡȠөɆʕʼȒ\x9aĹÞӊͱɾ\x9cı',
                                                    },
                                    },
                            {
                                        'name': 'ԔÎпsԃЌȍɣćČ´Ԩrǫ\x94їҀɆŸƔɶ*Ā)ƚϊ¼wϟΥ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 125528184931384185,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΉθԪÆ҄ɘϬƀĴҡџVǎʋ҆qδÉŔĖҠs^ц7Ѯɑʎ"ǥ',
                    'message': 'ȒΐǰγϭéӰîǖǚȘɑҫΠɈγɛŻ¼ŨǣǖÇΝӜ?ӉOƜԞ',
                    'arguments': [
                            {
                                        'name': ',Ō΅ŤʇβʠͳǓɇӧʳóϐÉӵΩϪͲɽѢΌһʝƪ˓ƅԑʢƨ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'μơɾʆʀ˅ońƓз˳˴еɑЅĻêЩŬǈHϦȯƉĄàʅ¶ŤÞ',
                                                    },
                                    },
                            {
                                        'name': 'n',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:185656.327781:+0000',
                                                                            '20210910:185656.344607:+0000',
                                                                            '20210910:185656.364779:+0000',
                                                                            '20210910:185656.387689:+0000',
                                                                            '20210910:185656.409284:+0000',
                                                                            '20210910:185656.431200:+0000',
                                                                            '20210910:185656.450913:+0000',
                                                                            '20210910:185656.471397:+0000',
                                                                            '20210910:185656.491320:+0000',
                                                                            '20210910:185656.510642:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƎÜҀ)ĲяӻӍӂbƬŵӢÎ2˙ϝċӨѼȬ˖ѤƲϣ\u0381',
                    'message': 'ҝÛɡ`ˣӳΑӸȫϯbɼ\xadÖӞщΤʹѿùα\x9aԬ˲Ŗ\u03799ǖɮҝ',
                    'arguments': [
                            {
                                        'name': 'ɏśэ˔\x7fEИ\x86ҊϽѓġӥϑїѠҷҮϽ¿ÃЃŊнεŐИ҄',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            489943.478802194,
                                                                            479673.4731834319,
                                                                            699795.8227209431,
                                                                            440806.17917222227,
                                                                            714052.3293822659,
                                                                            750233.0506982589,
                                                                            -40549.215778648926,
                                                                            919079.3041661431,
                                                                            469929.4434275096,
                                                                            249419.72391749243,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ɼЫHΟ˵ĢÔϥφQrłčӆ˔4'ĕǋКȬԆ˗Ď|kɭςЖɚ",
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ʇԗɽζȻέȥŃ˚ԃŏ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 259821.94424381322,
                                                    },
                                    },
                            {
                                        'name': 'ϒӏ¢ǞȢцΗǺϥ\x8aƻå҇ҬȂ0ӮʲӐơџЃĭ҅',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            869357.4489807354,
                                                                            365974.6767865004,
                                                                            785425.7215100874,
                                                                            275285.55602060317,
                                                                            898014.7843782214,
                                                                            532634.7016006202,
                                                                            421597.70012786426,
                                                                            492960.69290316023,
                                                                            174530.0734826657,
                                                                            545002.2071484922,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˤΆӊÀΥ҂ʮҖɳˇ<ʲϭҁбTiɒүϲΡͰΝҹҕϦԃϐ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                            {
                                        'name': 'ȉƟϴŀӺŠγόÚAъʆĔØǖΓȴ΅ġȟ˓ĩȎƖԆ˕ʤʈɄЖ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4388824930283281343,
                                                    },
                                    },
                            {
                                        'name': 'ʃʆĠ˴љÑφыΕˬ\x82VƄ\x9cËΌƱқpϡХʎƤƩʑƂƼӏ\x81¾',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 13531.857391565136,
                                                    },
                                    },
                            {
                                        'name': 'ʽˍϪɿɠưƕηѸyĝ˞`Ǉӫ$ӈZďCєǽΉƃo˚Β϶˲˺',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': 'џœŧӋΜǌZʀҧчĐřKĒĿɠЙԐªâѹРǖӃҗǳ°ҍӵƥ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185659.118022:+0000',
                                                    },
                                    },
                            {
                                        'name': 'àŷɆӣǖЧýӻрʥȧZϮґſϝtЉʩʜҚÉiȬÉҍдƦÍʓ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 405660.40186496754,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '³ǍŪӼȾʊȈԗǓԦ˱ʓ=ҏȬˬӍǒ¡μϗІШ\x96ȓˌ¦ˉɮɜ',
                    'message': 'ƄɠҀӋĎЛȯΦŶȏǙˁԢĘԦȱǳӆΠπǎеœӱҕƊǙɾ¡ė',
                    'arguments': [
                            {
                                        'name': 'őĤЎη;ʰhƐѲМŀƄѾͽЏœТϏӎȵϊɏЧôŲкӖűҷĂ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185659.356528:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ԅ°ʜƉѢ˴ǋυɻ\x80Ęĸ?ԋȯĖеƁºŊɎ҂ȡŠЖԩԔùΛѱ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 468293219853558345,
                                                    },
                                    },
                            {
                                        'name': 'ǩϓΩў͵ʷҎŧĝѿƬΔΧŧϲЗӍЋŭȰǘjɶǤӍʨΏΜ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185659.505046:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ĳ\x98ғӉƐ\x8cʓєԬ˲ŻɬĝНѳόȞqȓɍΞώ\u0378ƫєɩΊαІʼ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:185659.590494:+0000',
                                                                            '20210910:185659.610562:+0000',
                                                                            '20210910:185659.628457:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѨǕͲƢˆΝϩɖϷ\x82Дϧп\x8bӗɎȆǯФ',
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
                                        'name': 'ɺγͼÎЖҵ\xadҺȟԏǿŶ^ŬϊʍǁПʦѸΊ·ӗ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʚҊђӟLКȂȶчҬцҲӭђώΑзҋ\x98ɆР´˽ńѿǹǅ6ɹі',
                                                                            'ѾϖԙǣӻˏҠʡΐȠѩеeѴǧҤ5ǨŭĊӻȟѤРƁ×à˭˖˓',
                                                                            '>āӎЙ´.҆ƧȄŤ\x87Į\\˹ѺɾЁќʟȶѐ\x8eԉňӬǐчÖѤг',
                                                                            'ȁʠʰşȈЧӜǘџИĠӹ¤҈ťǦɩμјȬπӣεɥˡΆɟ,Кч',
                                                                            'ȜʚŀÁVųȷÈτéȪʕƔźYԏƺӆvѲҷζXǥȘȳÚɁҤӥ',
                                                                            'ɅҗǢɀэːǔʠӚіğӆWĞҧǔǞӍɼƦӲƢʲFËBɮμȻđ',
                                                                            'γїƉЬҧ×ӀӋдʫ#яϘǾjȰ˴ʠʠĸіȠēǣŘσЋ\x98ˏԃ',
                                                                            '˶ʃŐЂς¾өЋƞԊѴĠȴ҈Ď!ϖѣʦЛ¦Ăъ\x9eϲяԭ5ɫ˫',
                                                                            'ƾŐ\u0383ϑŁәΐєàҫȮĝȄűӯΝˆùԒ˒ԬåЭ`ƾѳêΰô˔',
                                                                            'ƤǁŕɶʋΝʵ΄їԐԂiӥmϠЂȋТ-ӎǝÀǔƘ3ϊяћυζ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʚ;ĎƽΚńДϋЖɡʈĪԛΈàΘВӺ\x83\\рĜYßǍίҷўЖÿ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˔Ҹɂʒǝы2ԕúˈҮɾʏӭ\u0378ʽĝ&ʞΐɻǈɁΤɩɪˏͳźԇ',
                                                    },
                                    },
                            {
                                        'name': 'i`èӞɌˮŧǐʓȹȘěʢNŠɍԂҌčɉėʊĀ¡ȞԛʱήʭΝ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2664453612282647616,
                                                    },
                                    },
                            {
                                        'name': 'mȢĀ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǧҟȶΓӔșѦԃ^ʽɪϹί˛ӻȜ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ōǎ\x99¦ʗ\x7f҉ƏŪˍƆʩêˑĨх΄Ћ\u03a2ļŶҕŪіɭų^ʓяӐ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƭżυŘϛǐͶď%ƚ¹ƂġďʑеǙ{Ȗ\x87ѬǴϕϰр\x8cԕͺȺƎ',
                    'message': 'ʸϪԪƔӛЭ\u038dιǮĨĚѽƪȎˆĊˋєԍ˦ɑȴЯӶǪʁЍzӠɧ',
                    'arguments': [
                            {
                                        'name': 'ѹ`ŞЅνƓʤʰϐŁÞϣͷЩĹ6Ȉϲȗ\x9c˚ǌөѦÒκԚ\x97˓Ř',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:185700.817799:+0000',
                                                                            '20210910:185700.834760:+0000',
                                                                            '20210910:185700.851187:+0000',
                                                                            '20210910:185700.868117:+0000',
                                                                            '20210910:185700.886310:+0000',
                                                                            '20210910:185700.907959:+0000',
                                                                            '20210910:185700.925928:+0000',
                                                                            '20210910:185700.943062:+0000',
                                                                            '20210910:185700.959629:+0000',
                                                                            '20210910:185700.976754:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'TìĖƚќƖUЏȌʑ¡9ԭƌ¼бǊͶ¡ЌBɃ@рǓѦѵÖҮȥ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϥ\x9b\x82ϒ#ϽњÅ®ӯԁѪɂϼǟЊƼɹΰǣɩǶ{˶PζћӁҤԔ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            986204.1476344741,
                                                                            -95552.22660503087,
                                                                            499747.9533540129,
                                                                            -88282.41954665925,
                                                                            313824.2717417146,
                                                                            985925.5287731909,
                                                                            737209.5519313101,
                                                                            602061.9494627279,
                                                                            533805.9407695668,
                                                                            776502.8164683249,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҩӵuҔЋƭ/\x94αҌƆ\x87ҘџŽŤέȥΘÓΑӋτǟʪñǉŌȬš',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 954620.9562613375,
                                                    },
                                    },
                            {
                                        'name': 'ƇҞƮӗ\xadԊħƗñŸAϪ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:185701.471203:+0000',
                                                                            '20210910:185701.488424:+0000',
                                                                            '20210910:185701.505469:+0000',
                                                                            '20210910:185701.521579:+0000',
                                                                            '20210910:185701.538284:+0000',
                                                                            '20210910:185701.556564:+0000',
                                                                            '20210910:185701.574095:+0000',
                                                                            '20210910:185701.591394:+0000',
                                                                            '20210910:185701.608774:+0000',
                                                                            '20210910:185701.625643:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϜУӈ\x8dϽϰ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7984870509777919505,
                                                                            -350937574120424221,
                                                                            262055123201577167,
                                                                            -8310196545730560053,
                                                                            2736042206028654559,
                                                                            -6170439665595162882,
                                                                            -3958313660364732943,
                                                                            -5746552374645659643,
                                                                            -7543510159807807398,
                                                                            -4433604355726294029,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ņ?ͼ«ȡŇКɫ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 701250.6160443561,
                                                    },
                                    },
                            {
                                        'name': 'ļ҃ȀˤÐˮʰÁəγƱǊԃ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5358194217137721390,
                                                    },
                                    },
                            {
                                        'name': 'ΔùR,ŦĖƭƎȑԞӮТĸƾ҇ʎσȜĕ³ғӱͼҫ\x97Ϲʖь\xa0ˣ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƎόѤȒ˛ђŏƽяAҗӏοǶШԨ˾Ɔ"ԩɉȮЪĮǠοǪԚTd',
                                                    },
                                    },
                            {
                                        'name': ' ȮâŰΊԄɵĢԮ҈ \x9bҞɲâʙǊʄϝи˾ǢӑÏʼa\x92ҋˑϣ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185702.178693:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ͿʀʠӸĽ¦ĸǊȯÔѬƧЙs(ЌƢИ5ňǌʏʅʢϚΗķýǴМ',
                    'message': 'ɛκӴЕԌYɯӀӘƸ±ɿϚĽ\u0379ҾɃϡƴҿÔXšČǬαȥjˑҧ',
                    'arguments': [
                            {
                                        'name': '˸˛ƬУʜʳҙЯӎăиѾǻӑřΚԋϵԍŦΟȆЍľĒщ˷Û\x80Ǻ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
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
                                        'name': 'Ѿӧƒʫ˖ӦRΨĔɌǙШğd˗ΌʯƒɢӏǪПФѵˢΕίыӜ˅',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˺КіϻЦÝÓӇĢФϕƬѶҝ]ʊ˝ӘѤº˘ӡʜҋĭʓоūҵΈ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2664898766594849761,
                                                                            383743471896907327,
                                                                            3203533218574947530,
                                                                            4842029600408874775,
                                                                            7151766423606091467,
                                                                            -2351421913966229322,
                                                                            -703894012020800678,
                                                                            -7389611569094413996,
                                                                            -6970145110296739129,
                                                                            8358777168692245826,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ſԧķʉĒԅ˸Ԓ.ɀʝηеӉƎɳԟȬòƎѪɩЧм˙ʍ¹ӍʵƳ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -141763671654854072,
                                                                            -3182391673615651261,
                                                                            -4011083749715828838,
                                                                            -1004529169711416743,
                                                                            -44239783843188946,
                                                                            -2813635441950671157,
                                                                            1838106050759029579,
                                                                            3362485240020438189,
                                                                            3238714950908618419,
                                                                            -2315234821469614767,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'вʨƥϋĜԩ\x90АΛȀűÏҨΔyȱϧʵ͵n˴nɅһѳĢѫЏǳЖ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˟ˡɪҩеҎzɇkoĆӱˊÖʴǌϧɝÁŞȲŌ®,Ѭťѵ\x98ãζ',
                                                                            'v˚Ѝ\u038dԦʝ˹\x97˵ҼӾУҽ:й˸ϗǑ?ɯ¥ƶИšѓϏʚȋɿέ',
                                                                            'ǄϾГ˧ϳȌѵқʤъƑŵɉΖ~ӡӍóϰϺҀƶ˟Ůӷǳɬ\x9eȭɃ',
                                                                            'ĜĔʀ\x9eԞwʏΥԨϜчρȔȞ¢Fʫ˃¹¸ŹĲΈWâ˅СĜǕБ',
                                                                            'ϑɿϳшҫԈԢ|ˀƟӰȑŇġмσɗɦUΦ sʥIӾǵɮɑʿҚ',
                                                                            'ÌÏҊŵŴėôЂΜɱȓҲ˙ҫ˘ӚӆĕîƳUȫȴˢιϕ˸ъƓҌ',
                                                                            '˺żƶÉ$ЎT˽ЇҙěȼȗԮӿȻǣÆҨɰ\x86ˈņ*ЈƪӺӀӒƗ',
                                                                            'ͳʇȳƇƔԨԮÒϾÊˉӛʛcƲԧȦʔϖɧ˨*sú¯Åĕђǅћ',
                                                                            'Ҩʢ3ʋƼƾӒƴĢŧ\x9eËЊ˷ԏ?ɁɠтͼӴѮҾãϠŞȗԫȆˠ',
                                                                            'ΗƖϠɂϤÁ§ҞǋѣХȸμЏғҘƔȹÅǈɐΐуɗϦÍԫŨĆ\u0379',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǩΛyʦǥӘΓԫßŨŕŗ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:185703.915108:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɐѩüКОșĿħЎĬȸ˻\x97ɢĨΉǙʴу\x9a\x84όΝ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'άғǱҴʃ\x85ʕųŹҦȼɺȾεԝƮʒĈÍɹƙӕѦĞΕϽȏ\u0382ӛҞ',
                                                                            '²ȁʥ4ΞůŝөԫͳʁҍƤȗ˜īȬОŝĭӢнͷɢyɋϚåǃϪ',
                                                                            'ϓǈӘϊ2Ƈ¸\x81ԠҴcɭʲʑȉ¢ȮϋЧӺ˜ϦŅӦĕΉʤkюČ',
                                                                            'ũӼбѰʸΊʏѨN\x88ɖϽʊəѷǉӏÉ£fͰЀͰГ˄ƙŕÇ`ɗ',
                                                                            'ԟћǢǍȎ˪>ǸȟɰȯŲȚƊɌ2ŕʑѻńԚąϾ;YԨêȣҺƅ',
                                                                            'ǀ˼ȷÝŴϿʖӌ"ʀ¨ɵǳ\u0381âϙбҭͽϾ˓ŁƖŵȇbvӟѫЗ',
                                                                            'ѣԧƞżǑɿҸгŉțҐĮʐȨϳьɽĨҼԐçǯġΠӬǊτƫԌϽ',
                                                                            'iĐƎΊˎπӟʾƻɄ^ļϼԋԨʰƣ¬ҌϙЃȏ\x84ҵͻǵԎŹЄǠ',
                                                                            'ϿɱʛӶȍǘȯҙɕ\u0381ÍX\xadƙ¢\x87;ØӤшҲƦ^ɵįµƠåЧ#',
                                                                            'úξʦψĥèƞϧɣĆΑˠÎ҄ҹȶaȮňǡҜЧңϚзѴѐLÎŒ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȫɭԋƓɍWп˔ƤĲҔˮȭѱ˜ЍȊɒh\x96ʵˇŏҗŧɊ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:185704.314143:+0000',
                                                                            '20210910:185704.333665:+0000',
                                                                            '20210910:185704.349933:+0000',
                                                                            '20210910:185704.365662:+0000',
                                                                            '20210910:185704.383409:+0000',
                                                                            '20210910:185704.400284:+0000',
                                                                            '20210910:185704.418797:+0000',
                                                                            '20210910:185704.438180:+0000',
                                                                            '20210910:185704.459576:+0000',
                                                                            '20210910:185704.479367:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'όψϊĊ0ĢЂς\u038d˯˱ʰWƌӃɳȩΓʱ҂ʞώ{NƨѥɰӴӯs',
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

            'identifier': 'ұґЖķɹ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'ĉғ',
                    'message': 'e',
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
            'name': 'ίˋъʕ',
            'error': {
                'identifier': 'ˢZƽԉĆǊǊƞԋңˑ\x83ĠJơƼɶԨãКÅЫщǊОƟ;Ьҕʋ',
                'categories': [
                    'file',
                    'invalid-user-action',
                    'access-restriction',
                    'invalid-user-action',
                    'invalid-user-action',
                    'configuration',
                    'access-restriction',
                    'invalid-user-action',
                    'configuration',
                    'access-restriction',
                ],
                'source': 'Òw}ǤԖġʗҋϤǳǘÌąĻôʟȐӀâѣȊ˱ĂԃƮǥCΤĮϡ',
                'messages': [
                    {
                            'catalog': 'ǉрìԢͰáŭѾǅˬҔģӔŏĬЁӉӵ¨сƭԍƈ¿ԉƳӛ˾Ύǜ',
                            'message': 'ƪ˄ŶŢҵԋӨЃǗßģ˽ΈʌУ҈ˑɊӉ\x80ʇșќђϻ\x90ԡŊŰɊ',
                            'arguments': [
                                        {
                                                        'name': 'ƛǦȥ[˦ҕğŇ\u0379ϓƼʌǒҍ˺ġ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'īʓʊ˰ȺëġЂ\x92ɔÑɛƂӕҘКƟ˓В\x98',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȖƭԧȁΑ~ªÓԑƱʦŖʝ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 952242.9069779206,
                                                                        },
                                                    },
                                        {
                                                        'name': "ɰƋTŚƲЭÄѶàƋʆѕǖӆԣuɏʵҏþǑΣ\x91Йȸɢƹ\x8b'ɞ",
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƳǦʁ·Ԛĝ©ɭŅɉǱӎöԣϼώЏʢа4ˬʖgŸǆÖŹŨԐӫ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˍ|ț\u03a2ǺľɅѥҷ&ӾѝϖӞλXқéԐӴ\x81\x87ƷʊUЄɄĘÊγ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɠ\x7f',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1244430463284488556,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĽǗѓʴɷΆǝӽũǗŖχÓн\x90ʆóǑѻģ҄õŅ(ѤґӔ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЛѺϔϻŭавʫħԃʹӱԔѡ\x9cg˳ˍφƒ=ƨȣКԅІδϿƽ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǁˮvƁ*Ŝѿ\u038dΙ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǰÙʺ˵×«ɪѾwӎEœɤӉǾĩМͱȎȟ҈ıʼɠŒǃ˽Ǭԡƙ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185635.850347:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȑƚҨ¬чɁјϑÌǒŘОёǼƕƫНң˂ʾƪӷѲҦǒɖһϬǬԥ',
                            'message': 'ǫįŻǲЦĐǝȻ\x82ȦџгѧϛnʖхɣxǄcЉȅɤ~ԋœҵʴʼ',
                            'arguments': [
                                        {
                                                        'name': 'ԟ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ώΘмЮǪӝő©ŋҜɓɘЧˇĔԜ¹\u0380ʷςîȝ\x82˒ҩpũӔ˽Ř',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȭӓ²XǎǺҎϛѶӹп΄Њǚӣ\u0378ϺŴҍЗіǞМʂɓȃ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЪżМɟς΄Ӷ϶ĮŠ0Ѳ<ğøєƒȃӖˀŒĨÂġȚ6\u0380',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȭ΅ƾʚʒʱΥӚſKČȡӺȱŪҮʫ\x8aƐľӇԠʍ+ҫѷЀ\x8bћѯ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'а˹ƿ¹¾ĝɁЁэԊĂðɽјЗƩʀČ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŌžӐʇӘǂƕɶѺŶεŉ"ʏǠƿçƲ¾ɪǍ\x9cһFUtƜƆʁɿ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӚȲċƕύČŴѺˉʛÞȓʴǨ˂ҵҢʮӅDrǉłΡȤŧΥĉ\x8eԧ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185636.594747:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '¬ψʖǽƼϸӒӫǥˮҒƉԘÎƯˢįʸȡçwŽǔ˛Ļąǻʹŀέ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'чґ˫ΎПÓГΈаӺԠԌŔԃɐǦðǸ¬ʪ·ĢÓőQƗΟ΅)Ӯ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'уԇƍԦɕVȭҔȤͺȮϒʸϱɁ\x9bɉåԏԮωҴW',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'θĿҌĻʼŎ˱ȘӰҼ\u0380ɶçʂ\x91ˇΠĿȃɺŠtĕӗΊ˔ŝ\u0382z\x9d',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ŅʋҧѪɋΩӾȆʂėˁyԥƸΰӋԂҩсȄιʚнώÒ\xa0ИӛľЌ',
                            'message': 'ŧѨґâӷαԨΨϠuϩҭ\u038d\x88ЎʭZǕƱˆϫzηʻÒҝň¿Ƅι',
                            'arguments': [
                                        {
                                                        'name': 'ʉ\x89',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 9194013061409393133,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȃӂĵɰЇĈԢѳƪϐŴǢ҇ãɨԃȕҵӂϽ϶ϬʘβɝҕӔÎФʼ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 359230.01876198815,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǿӖӿ\x9fƓǳԘƜAˀґƑ×',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '~ǔáϪȗʻʴ\xadΛƭǲ`ǳɔïЯÜƫ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'т',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӐĬǇ˄ʵάϐͶɥɦȔɡŮȬǼƒļľɂжѮǠɧΖҌћ\xa0ӔĲȠ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'rˀ©ѫ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'wҬϣԘ½ɵȲʮӬĵΩԛǍ÷õčɊ/\x86ҾХŅˤɛjΗΗɜǷǗ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3806616333655211298,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԘӓŇ\x99˃˾ǶÂҺǈIùΩԞĲϻѨάЅ¤Вɚ\x87ʦƶǩͿжφƑ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϝʁ]ϙ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185637.745240:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȼƤԏʍȝĐл·ӇƐѧĲķȽЪɆ\x8aǏӾГɪĭȗѱʧϋʶȷˈͲ',
                            'message': 'Ũ˅əҴȠΛΤʔ˕ȂіúѭŐ\x83ǨѾҬŻʐʴЂЕτǀaɨǝБϣ',
                            'arguments': [
                                        {
                                                        'name': 'ʪϭԔʺӧʃΕȟǾԞʳΕ˚ɥǳʉʹƂԃʨĘʙžĸǔvƏáŮ¤',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƜĉĴkȴϽ~˓θǊɬˑÿǰĒ¨ΦҮʠˏɱϾȮәȣÆ(Сҏŕ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʆƝ·ԍАǫϒvŲ˭ȳ7ʇʚСϴΪўˇŖYҳ\x83ǴßΖΦ\x98Ãʡ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185638.009358:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˵Ӷʅҙƨė`ɑ2ДØђЪťοϛŜϓȌȾвǗɱėţ҈ƺƚÜџ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'İíӲȌщ҇\u038dЎіŀсȄАѦÚ°γ˓ːƞǝ¥ɕUƌʛсҳŎĻ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 356373991958847221,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǞԌіΊžˬЬ"˫ΈŋŸҙʐMӜœѼ˳1mʏϘƧӐEĝȦǰɩ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 153938.86716254594,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŗϒΨȞθЌˀҐ¡Ƃ˯ȧ9ÔҕӫқӐҝǹВɻ\x87ɥÉӏ«ý¸Ɂ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ªʞгưǰӷӈLľaʻΡҡˊĎȮɓɲººˠ\x80ȒȂʺëԔϱɱΖ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'W\x94ԪĬɄ=ɒîϐ\x8aĿҨʭʲ Ԕυuѽ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǊюˡŋȈ¸ŹҶӅƄɪңЙ#!ϋԧ¯Ƕ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ý\xa0җǼʥÈОԎЈǌZȠÈĄ˅ƨȮĶԊ[ʥΕĞӓÊӰĉˬ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2669701575357626822,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɤĿƩԛǢɛ9#\u0379ưŁǯøĸΑţϑsӼ{ӽѓύͰф¡џΣ\x8cę',
                            'message': 'ӔąĊЃҢӈńϠȍЬΕʹΩ0ӀϿҏ9ғΓːĺҚõǾLΫ«Ѱ ',
                            'arguments': [
                                        {
                                                        'name': 'ˤɧ˩Ѿƙ\u038bƉ\x97ƭΆѵƥjӸͲѢ˪ѱϛĆ.пΐǺҿȼҽӃ˟ɚ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "ԒΣӫ\x93ùәҮʍВӄqϘĠҢ¢ƍ\u0383ûɳˢĸǤȬҝǬŕʝϕǺ'",
                                                                        },
                                                    },
                                        {
                                                        'name': 'п\x87ӸĎɑ\x8aÜƑ;ƓӺЫÀʗ\u0380ԍƶΜTХƀˁӾς\x9dʜ\x9f|ˉƔ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϯÛӬÛˉŇʦͿʋȐ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'æ«΄ԗτŗԠóκǗǰŭ£ʬҸØȀˋFEӻǢ^ԔϽˌzĪų',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 229125.76617933234,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɛŬʘīķł˕˸ӲI\x8fſɁƍïϼĶѤ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 502558.304089166,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϻҥƓΛDȼʴ\u0383ǅÌӡvȳ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӦҊˉЫb҂ÁƅнdΥҕ×Ӄҹˎǉ\x93ΌгŜķϯǥӻ\x97àƁԮԇ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ν÷ѫԔӍұÔŏѽʫ˽ˑǯҞПԮʽāȤӯŲɀǎȥǻêřɭŰȜ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185639.321145:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǅӉĆˋƐ!ˁΡºҽ\u0379ЪȫӳϭϑąÒˑɫˆпɫˉŘ˝cƍЂQ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʉϹΙǙѦҸɱɢXн»ӨĻҝ˫',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΥЖȗйѸɟƇčĕҭDǽ˝ɥŏƿȕˬˈȽʍ\u0382ʼĽђσΟε\x84Ǚ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӑҪƂơŲƵϯĲьªбѫӎxлЂˡʥӣϴӌąŸhĬбŔȀ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185639.563550:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԭƢϛԭѳ;ņҳπAɋˀƑ6CАʿşМJȝ˩ЋӶЬʧżѕƟɻ',
                            'message': '×ÌӮЪҼϯɈ҄јÍʵʛ{ɕǚØӐϣςƩβԛʛϧкхγώÔȍ',
                            'arguments': [
                                        {
                                                        'name': '\x91ȿƬJԇ/ԎдΪϜǯĘ`\x8bĥʨȄɲʢƺ͵ɭӭÅХ°ƽ˯¨Ҏ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 54356.49937282986,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǋV«\x9bZȏͽƪûҰ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƚ ʿŌκӅò;ą03\x85ӌԮ\xa0ӽϗǖ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӗǁñ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "řȳɺöŔϓǡԨж®ĆǑӶ~ӜÿȷãҚAɨԆɁеʥҟ'Ӈψ˔",
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ό´;Ñϡ;ƥųŴ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ':ϚEĄ˟˸ŘѨņŵԫƵıɫ&Ӗäɨάс\x94ʺé˾҇θ\x90ĺÁ˳',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŷ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'tƨѨџІԀƪͼ\x9c6Fώûȣ*ĲԬӉÃЍȑ:¸ĸʂӪƊʇ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԇӗ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7301829351772012083,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҮʧҸǻ¨ƶ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѸìƆКͶ^БƓØU\x83ʐΫϲӤϤÁlƆːðʽ\x88ɂx;Ѩȍâȕ',
                            'message': 'ǧсѧ˾¶ɡēŽʫ˶ŮӵƞԛƟ~6\x86ƃͱSƸЎĬΉеŌÅ҄+',
                            'arguments': [
                                        {
                                                        'name': 'ǴӡϝѢ\x99ŗİ\x9eɴϺɄłɝΉŉ\x8aΘɩƱϘś҉ԐɢАɓșŔˁτ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɄқǒĝтϳΓʎȼ´Чźϑ¾ʅԮȹǌɖїǴŒɛǼǦĔɞèίǊ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ßǀ)ͱάŤÍǿэ·]όʷJГɁƱȗƕʊʄɁè¬ԩe7Ʈ»»',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6545311214555002733,
                                                                        },
                                                    },
                                        {
                                                        'name': 'μǦҫǏiǂϫʾҒӃπʄ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ηϖΫ ǮˍнřςŤӡґЪѻ]ƨ˷ͱǀʑϞБ\u0382˛¦Ђ%Ɏ®ж',
                                                                        },
                                                    },
                                        {
                                                        'name': '6ȵ϶ǆʥñјȢϨӟҰцӥÐϓƶɏ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӇǖǒǐϲϞßŭҐǠ\u0383ɀ˃ǯƞ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЁǎƗЁ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ēϩȗѳјċĻԥю',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɊĪ×ňϡ?ЗɆ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˏЧśÈŁɔʎȞЛѽʧǨΨ&Ǧхǟȫº\x8bӡķҾʆɬԂŵ\xa0ʖĻ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Чčбƃ¯×ƫŎʃ˘TХʀɚȇɖũƳҢ\x91\x80ңιӮѺŐЩǞȇΣ',
                            'message': 'ñĽÒƕӻưҠĂħƏĔɘϗҢѮĈʆĵÈϺƞєѪʯčΊԁΟɇİ',
                            'arguments': [
                                        {
                                                        'name': 'ԨŦˮʯɕñȘĄĨЂеŝƴÁď˟ϏŹӂˆʾԭèÖ@àҝȵϸ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ґԛĠ_½\x8aҨєȧō0ԞȷӱԠŖΒѾ#цӠƆԂğˊқЕϱΪ˥',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ÎСƝҒϸѶʥvϝu\x9fҋҽÂμόШĺϚðО¹ȻɈ\x84ɰˤѥòͶ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'KʆўăŽȯǽɮΰӎfŭ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'éˇ˧ЋΰԗʗǓҺȅɟŤ҈Ʀ˦ΖuʸӣΝΓҬӝ˗\u038dũÙΡ|ԩ',
                                                                        },
                                                    },
                                        {
                                                        'name': "˅ɧƛʊеƚņʺȿƞĔΫíѓԐ˪ȳ'ƨ˟УRˮƾăӬҺ\x9d¥ʿ",
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '΄?Ϻ҉Dƽ˗',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΥɐHѬ˽ˌɮĺĵ\u0383ƐҸӓңʨ ƬĐҫ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:185642.957391:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȕϸŽȋіʱӉѸļåѭ:xǟΉƑЇū',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4467363614764429387,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŖǴÝI×',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "'ɞԌОĻѶUƏΜнĘūĽ}ɎӨɻÌɷҡ\u0378ѽƟĭВü˥¨¼Ý",
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȈԍĝƎʀûњӬʸȾ˾ƯĐϺԥԏ÷ҦěÍɳŧȉϨGўһ6sÎ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '×Ⱦӈʣӽâáĕ´СлƕàԇÚǇоԌɂŭǶßʩʌѯŨ|ʬĹʇ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\u0381ќϢӋɫǯĈΓͳͳƙӇфѽȻʉлѰěȎǚϢѨÔεɺԈгƓĪ',
                            'message': 'Ȯʣ˂Wͺϭɉрӂŗ¥ƷȳӸɟȉаԥФ˰˺Гҷ\u038bĔȠɭĭӭʪ',
                            'arguments': [
                                        {
                                                        'name': 'ԕƫΐ˒v^ƜŪŕŽԒȺόϺҴǠӚǘʶʗ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x98Ȫ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2458050231292498821,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԛƞ϶ҴɎjξŅc×ԍźƯӠ,ƞʧĘĆʏϘć¼\x82Ɏӳ҇',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϡřϩȳͻYĺǱυǢƞҧŦѷƃӮѦΖ_Đ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÖїʗɽӬѤ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ',ƄγÉӇ˥Ћӝ{ӥϿϊ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѮћЌāʖǁĠϴ;ҰуɒöCχȕΌŖȇˌЃΜŗʢȼʏΰǤ¿ҍ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѧ˹Ѹ!ǘƆɛˏʔĹЕЧ˝ь',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȉұȊɣӮφӱȗ\u0379҃ǀӮъƞƠӮȔ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӢŒӠǅ˝SǖσαēҒ\x80ǮҒƇ˱|ΈпƲ\x9dϚʶĳҡɱãåǻY',
                                                                        },
                                                    },
                                        {
                                                        'name': '7\x89Ҧƽȍψ\x94ӻͺӜІҒpϑԋȞƴҽʚ¤Ĝɂ˗\x9f\x85Ƹ˾ƺˡǪ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ùáқ¦ҢϐåԗɭƥƳ^ԚĴʦRζǙ;ɋԛԅѭʭ\u038dqǷ\u0379hń',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ɗ¿T\x91ҖΥȥҘЇFЮȁ҅ʫͶ\x87ƯțIǺӊǈ²ԚϴϛҪʫӮѤ',
                            'message': 'ƴШƲǭƓĆЮʉҰŭ\u038deƑаЩēɖ=ɕПĖІȲȣѩĿăȏѶƯ',
                            'arguments': [
                                        {
                                                        'name': '8§ԓ˃ϰȃǹǕʙѓXSȝɣƙҚӾ\xa0ǉзӄƬȏɥӺ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʯʱŹҮ=ˀƜȲȒǊԙ9ԂÕԥ\x8cŝԞԞϙӻԛѝԒƛΰΙǪ¶ȏ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǦǲϭÚҬʱń\x97Ƽ˴ÅϩFϏԔԁʙ˴ŏ\x90ǦҟěΨɼƒɻ\\өō',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʫǻˠçØǺƗ˷Ώԁѫȶϲî˱эȷ҆ǁĊӢхɜ ļɷҷЕ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1760205328792451915,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŖçԅˮȍÅTΚΣԧĮҗѲВǋŇĻȐ\x8eµʟϐ˳ȷǟ҇ǆϯȭȱ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8332644009356502613,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʳ\x87˄ªʓɄŝƟá²ǋƹϽƿɴΝΗɰʲYLԝ«ҫϰ˜Ȝëė\x7f',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʸѮώĠɶɵεıјşӼʌǃZǠĦқÅԉǄҏ\x83ƐŇ˩ͼʥ\\ɖЏ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ':źƺȦOȑNʳωςȐΏуҤԊԉӝӐԋȝǻн',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2591172532679717025,
                                                                        },
                                                    },
                                        {
                                                        'name': "ɀԑӞΠӽт'ʀӟǈȨґеӔаǷϝĢʤțάэȺrȵuŷ2ȷɢ",
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˖Ź҇ǲӜzWtӪÇïʯÖ¢ſϫǑʅƴCϵԗȓѲƕΆϦÂ.ϒ',
                                                        'value': {
                                                                            '^': 'float_list',
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

            'name': 'Їòү',

            'error': {
                'identifier': 'ĉԥǐӅԚ',
                'categories': [
                    'file',
                ],
                'messages': [
                    {
                            'catalog': 'Ďƭ',
                            'message': 'Ҥ',
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
            'name': 'źΤ¹:\x93˶ΉӽǥҗũŦЊï2ɥБϗεĵˇƼӹ',
            'version': [
                -404468449723701003,
                -4159797076853838929,
                -7390310345074322621,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ȁȷІ',

            'version': [
                -3529954741309224161,
                -675540654565862927,
                -4724437045787548453,
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
            'event_id': 'ŁǢ·ȋԩĄˏƟŜʔʛӒģƘȓʒĽԭȇѦԆĝă;ҙɈʤӘϝн',
            'target_id': 'ϩ\u038bӯ¶ЦĽʞʹPрΰӔʊϋǌ|%˽тɈʼȷðӖƹдȅϻǾ«',
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
                    'event_id': '%ȐԄ˻Ǉȉ\x80ÎԓƧųŀγӉʾnɓǓɯӘZϒŗγӯѧˣαɇ«',
                    'target_id': '\x96ȴɹʀŽǸƆ»ҙʀˇȭı˝ϻØ˳ɃΒ˛ǺԟȔӰѠҌŖĲ\u038dȠ',
                },
                {
                    'event_id': 'Эɫ¶ƛԚԂlL^іͳ*uǫИԡ˼ʚįѓǕƗ\x8f\x90ǽǙˬԡѻʦ',
                    'target_id': 'ͳ˚Єρĥ˝ĩƚȿЭʏőyзΈ¶ɋLŲРÓʏǑƛιўԖǦ\x81ɭ',
                },
                {
                    'event_id': 'ˉ\x81\u03a2ȫ˴ХμŶʓƒȌʽĠƳšſŶӀ\x8cϔŇǽ«ώ0ҕ\x84єώц',
                    'target_id': 'cȎΐŁҵӷķq_;δ¹ÎŵЬΠõȶuȫԐϟ\x86ԥˠ¹кМŴ7',
                },
                {
                    'event_id': 'љ4\u0382бӊA˼ӤūˀŨ%ʹ˧ĹɃ\x93Ɨ΅ӛԧЭ˪\xadʄҞ\u03a2ˣФї',
                    'target_id': 'ąʑԟґНˠȗƉſɉʜıɆ1ʘĈ\x9bnҠƷ˔ұūȘʮƉĴȽŔj',
                },
                {
                    'event_id': '·ȞƈƼϺȁïЖĽҘңʢ8ѱōӡ\x86ȩưтXдʶƦәƨеƛѻҞ',
                    'target_id': 'ˍΖћΎð˰ĥҧʁƊǬԒŚѻԨǒ˹ΜfŰķWϧ.řşɂњдϹ',
                },
                {
                    'event_id': '϶е>\u0382ˏ˴ӽǯԓіʈɵǡƻ҂óІģΙйʈҀ\x9bƹўǏыƊҲ%',
                    'target_id': 'ˇ¤ŀõŐϮԒІńѝưƋǑе\x88ǭÉĜΚϘϜȕĺȺȣ\u0379˹êԃƖ',
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
                    'event_id': 'ЌĨ"ĽԢ}¬ь΄ŽLªâ5ќM˸Ќɬ\x80ɋÏҋàÚʬÀĿΎł',
                    'target_id': 'ͺϖŃĺγĝźxːɇТG˞ӰԥҴǼǌŝɰϽѨŲýżǁΉʄҔα',
                },
                {
                    'event_id': 'ǁϕªЖãɃҐÀϟ¶\x86ЂĊʓŸŦωʳЂƯӌӧÃƌЬэŇǣ¢ɪ',
                    'target_id': 'ԏϮǉϱ\u0378ĴɵȐήıҼıʹɽːķ\x83ėˣɼÑ\x96£ɰÞĄđҮʏž',
                },
                {
                    'event_id': 'ԒҒѯɯҿѶƽƯѓӈ÷ɓюѭӗҲԇlΕƒȘԧĥʇԮТˠɌǓс',
                    'target_id': 'İңЩԚЧƣʧŏŘ˘ȿǠϺʗĳɽ˦ɼ)ɧҎȩȏǗǕĺ<ƳêЧ',
                },
                {
                    'event_id': 'ϨŴҙѾÚΫҟ¨ʠťÉÌłʙԡѦȐӿ҃ǬƽƻӢβĬǑͳkăв',
                    'target_id': 'ӆɆтɳĂ%ʁԚâЩɴĚӚȰӯӸӂЙoҬӉɤĲƟΫԔӟͼȘ?',
                },
                {
                    'event_id': 'š:јӿǬҋǎPȅӺʋхĕ҄ΛhГýñ;ѨĚϫÎ{ñ+˫[$',
                    'target_id': 'ɚŞɞˢįǓ\x8aˠΎβΨÕλ°ĚΈżԆʛчˍʇӐǔ¡ъўšɢѺ',
                },
                {
                    'event_id': '҉ϿϋʪΡφʟŒӗǙѴȃԉɆԙҟΌšх0·ʖśЕͶѹБƨѕˑ',
                    'target_id': 'ãƪǔЪѫȔȺЭч҄ќЋ\u038b8öҝѸÌ\x8e҉ʞϸ\x83ӗSÍПԒ˵ŧ',
                },
                {
                    'event_id': 'ƱɆѪʥɄŤԦȱӿʆ½Ӎ\x87ѤƟƪҘŁԧЇӐǫ\x87ҀϯʄɣäȽя',
                    'target_id': 'Ǝ^ȽϟǍϢĖўÆΉwȖŔʯT˽ӒǮƆɈ6ģԕsӲ.;Ňχʳ',
                },
                {
                    'event_id': 'ŦϸсǚӶƂȩҽԋ¨Н±ҴƭяДϑū˨ŖΊηɷαŖ\x86ͷƁöƭ',
                    'target_id': 'ŬŀȌŨɣċұѷď˙ӐϷτǋ˳Ħ¥ƴ&4ȈΩҬβɹșϒčċś',
                },
                {
                    'event_id': 'оńҪҥʗƼƚɀǽ҃ŊҙʉԭƉǬȦҔĪȠ;єˆĔŠƮ-Ąßӧ',
                    'target_id': 'Әņ˪пɜŞ&ѐƈƷʂŘϬҥøҤĬϵɺ§\x83ȦϿʶȩ͵ɱӯXϢ',
                },
                {
                    'event_id': 'řǤ¤ĵԠԣ\x8bι',
                    'target_id': 'ƫ҂ń@ƿǧ=ȹƤΝϠ˝пϤͰqĎɑʜșӯȡĬЗҁѿȫ\x8c\x7fη',
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
