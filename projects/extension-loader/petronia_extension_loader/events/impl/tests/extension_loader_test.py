# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-03T21:03:04.500555

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
            'name': 'ӓˎЭǐĲР\x9fDĉ',
            'minimum_version': [
                -1473314289529317763,
                -7708364845316772466,
                -8306233868013092921,
            ],
            'below_version': [
                -2580981974195732265,
                -89887087856230610,
                -1043475944080633284,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ǸŒƠ',

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
            '$': 'ӽŉĎ҇Ť,ä¦ӫҴɿƣӭдĩϩҥέ\x9aϴϥʩΚÞг͵ѝbȔ\x97',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -1262763340410786026,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 830668.5659747337,
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
            '$': '20210203:210304.390560:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ԫʭˑ˜ʹ9Ōһ!ʥȚпJϯўǙȴВʡǭĂԕÎDΕñƯǟеʪ',
                '\x8eѺЭϤɯfяñлХчȢŨ˨\u0383ǪАΤѮąųyêœҥżƶųɊÐ',
                '\x9e2ġßȲˏԕŇŒНӮŉÝ˂uΛ®Ǣѧȶ˾ȃΆȸЕ˃ʹDÇˑ',
                'ȧƉ\x98ќʤчʛʠŲԕͰˠɼ˟ԆӨśԭѰĽˣrʤл¾ԦЍˉΧð',
                'ţԣȥԔƦÑΆV˵6\x90ҟɫÐɦĢΖť@ʯʷmɿjȿļѨЫƺГ',
                'ŕ˘ȃɸԋɥ:ÛӾ˂ë҆·Ȗ\x89ɟƚѯ²Ŵ¸ӪȰ\xad\x93ѳɺʯōѹ',
                'ťȘ\x9cѨ҈Ҽʠ¶ӧ´FϪʷɵ{ʠ:ԪʟѼ˜ԆʝѿιӭìѶǛœ',
                'ðԉьϭ,˄ʆҾːfѫӌȒɁȶ΄\x8bʱЍȐњȢͿīӮͿЀѵѓ.',
                'ĠØşюʏǂ҇яԮǚ¿ȠԚЋΕmѸɷSϦȪҳȘŐФǰƸғϷņ',
                'ǥρȋæ͵ˏԐNƽBѯȲ*ɕЮ¾Ęķ˴ӆ\u038d˞ǃФ¿Ћ˹ъĴѳ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -2251935420389636947,
                4217901398881782484,
                3319981616199800967,
                4296030246325989568,
                -8684408596802961038,
                -5223557962831213328,
                5298121589648907919,
                301268570543735132,
                -4084534430630292426,
                -6624120211160730003,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                438164.900028773,
                -11760.815678086481,
                695107.104914722,
                15007.689832593634,
                410650.8438752911,
                -56215.936673714554,
                926634.4568768768,
                572064.8276058164,
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
                True,
                False,
                False,
                False,
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
                '20210203:210304.391504:+0000',
                '20210203:210304.391516:+0000',
                '20210203:210304.391523:+0000',
                '20210203:210304.391529:+0000',
                '20210203:210304.391534:+0000',
                '20210203:210304.391540:+0000',
                '20210203:210304.391545:+0000',
                '20210203:210304.391551:+0000',
                '20210203:210304.391556:+0000',
                '20210203:210304.391561:+0000',
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
            'name': 'өçÌœԩˉƫМū\x90Ưҕ\xad˽ȑƭƬďjɜӄʵĬиǬŽ\x9eɔəǑ',
            'value': {
                '^': 'int_list',
                '$': [
                    -1553438327901271973,
                    -118927269200865810,
                    -5005906351994546720,
                    8520060420599698929,
                    -8115524983706592143,
                    -882404472790215462,
                    2465331675738192077,
                    535763456411989111,
                    8668378831014549836,
                    3296633677341093174,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ā',

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
            'catalog': 'AѴ\u0378ѹÕԫ˕ԕϲӏЀ¡gēĐƨϘșY˘Ͳȁ£ɾϩΎĆϓʳĄ',
            'message': 'ҼЇҒτŉʀӅĹҀԫνӸȧĳҭĂʺɻƩΪ˯˷$жšҼȒãЅɚ',
            'arguments': [
                {
                    'name': 'ėΓϒƱϖrʚÁԭ@Ԅҧȉå?ʟ',
                    'value': {
                            '^': 'float',
                            '$': 259792.45075834513,
                        },
                },
                {
                    'name': 'ŢO\x97ϭԌҷġӸ˕ʑҽ0ƼƋ˺NxŹϏΜ\u0382όI\x9a˽Гʴǹēĉ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210203:210304.387787:+0000',
                                        '20210203:210304.387800:+0000',
                                        '20210203:210304.387807:+0000',
                                        '20210203:210304.387812:+0000',
                                        '20210203:210304.387818:+0000',
                                        '20210203:210304.387823:+0000',
                                        '20210203:210304.387828:+0000',
                                        '20210203:210304.387833:+0000',
                                        '20210203:210304.387838:+0000',
                                        '20210203:210304.387843:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ʑȰӂʽ҉\x8bόɾЬЎǾɌþˣԔƊъҗ\u038b˔Wôť\x8e˽ҴȌƬӻӯ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210203:210304.388105:+0000',
                        },
                },
                {
                    'name': 'НİҗĠͲɴʚȱƶԡӐЧșʰȽ˄ҟȶ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        383978.98365047714,
                                        29890.387478815348,
                                        587105.3382241771,
                                        707306.3101844421,
                                        829572.4921282381,
                                        817854.1300920089,
                                        810789.1563116056,
                                        700657.7042214619,
                                        837497.7266487003,
                                        654284.8796698778,
                                    ],
                        },
                },
                {
                    'name': 'Ҙγ£ŅƱӽʰЬщlǕÅɗɫř×xÒ\xa0ǐ\x8bӤĲ҉ΡӔʓԣť\x93',
                    'value': {
                            '^': 'int',
                            '$': -7228963986031442059,
                        },
                },
                {
                    'name': 'Ӏë2EОŜҨёюȓϔɹʲɚӀɲb°ŶƉФ;϶',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        569860.8346138827,
                                        -19835.71675106311,
                                        -51498.284363100734,
                                        380700.189737556,
                                        566898.934981847,
                                        510722.03852418426,
                                        495784.81737649115,
                                        787948.5035745362,
                                        780022.2643929247,
                                        53038.12106422358,
                                    ],
                        },
                },
                {
                    'name': 'ƫˊϟƪҫ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ŗŰ\x7f\x88ÆƝϝБеԖǌÝ˸ǴӋіΎϚʌʈφԓơгҏӤѧΤuÂ',
                                        'È\x8aģɂҚĔͶǷҪƿŴǺƫϒҵȟͶӺř?оͰɹӫƯӂϙΟΎȽ',
                                        'ʍ\x89[Ӣ҅ǭbFѲ˝ǱԥŷӛϖɄ\xadʁќɑўŖóԁÒFϛͻϿȟ',
                                        'ƇÏΊԂιѪәΑεşħѿīŘǲϛmȟǩģİӸŊĐȔʙ˧Ŀɱ\xa0',
                                        'ԅ"\x92í-ßƀҳnƂɻǨĕƽ҈вφǖ_ѪφЖΥtȢŋŏɵӞO',
                                        'ʿщ¼ŬŞʰΐȆ.˼ÉùўΊ˝ʓΠӱȺȶӞʙɲԇɩѪфÁȁɭ',
                                        'έíѦ½ІјԐϼˣɇөȊɚơ˜Ŷԅ\x92\x88ÄCҸ˽\u0378ήʌƛȆГʘ',
                                        'ϔƷȺ˭ƟҏıŪÅĥ=:ħɵ˴дWʓȚļӺåƞΛˍωĂӤːȷ',
                                        '\u0383ʜŋňĿȱžȑ\x9fԚҜ҃ɿҊӋïиӕ˜¬Ů˓Ȉʂ˟ώŲЊ@Ұ',
                                        'ţˋҴΑϔƥufAԊЬ¼ΗЩԚȦԟӝžźʿˀǅðˌńȩͶ¦Ȓ',
                                    ],
                        },
                },
                {
                    'name': 'ʗÎ-ʸӵ˹ƹП˚đæІ\u0380ώȼȹʆÛʴҋԥÃmѯМʹӕȓ\xa0Ġ',
                    'value': {
                            '^': 'string',
                            '$': 'đΑҞƊ;ęŚčYƿщνǅԪ×ҳҫϳčLʹƔƓġÈÝ\x81ЧˠN',
                        },
                },
                {
                    'name': 'ˎΞ?Ü¬ēϓӛЕѮưɀʂԚğҳɘͷπřƳ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        884405.3664951118,
                                        -99288.35463652987,
                                        -79820.73411673678,
                                        961695.6091184411,
                                        233841.2338537383,
                                        801869.8253918205,
                                        992942.8521184914,
                                        946701.3593561304,
                                        521737.3514911841,
                                        50779.81210271173,
                                    ],
                        },
                },
                {
                    'name': 'ƉƟ¡ӘԍȤ',
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

            'catalog': 'ԉͱ',

            'message': 'Ş',

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
            'identifier': 'õԙʇ%Ъ÷ɻ\x7fȱѵ˖ӽưΰѩАѩӶǙiĄĉùΠѽȁҿ˓Ȭρ',
            'categories': [
                'invalid-user-action',
                'file',
                'network',
                'os',
                'file',
                'configuration',
                'access-restriction',
                'configuration',
                'network',
                'os',
            ],
            'source': '²ƹ;ųʸфѤєƫ¢ϔЬΠԝbбǏȪ@ȥδΧ˗ÐļӫΘӁ\x83§',
            'corrective_action': {
                'catalog': 'ӠҝõΫәËàɕцРѮɷĔэʌϕșԍԉȖĨϹѭвӠԑƪңǒŎ',
                'message': 'ЭŚӈ΅ӼϕAιɒȓƍϢhыϚ·ϽčǽɨȺцBйӽ˜ğƝ\x9eϾ',
                'arguments': [
                    {
                            'name': 'ʡǬ\x831Ҳĸ΄͵Ӌϸ\u038dǌȀ˰˧ӠӲіʹϴкѨԀ\x7fϵ˨Ҵ˞ȑº',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210203:210304.385208:+0000',
                                                        '20210203:210304.385254:+0000',
                                                        '20210203:210304.385260:+0000',
                                                        '20210203:210304.385265:+0000',
                                                        '20210203:210304.385270:+0000',
                                                        '20210203:210304.385275:+0000',
                                                        '20210203:210304.385279:+0000',
                                                        '20210203:210304.385284:+0000',
                                                        '20210203:210304.385289:+0000',
                                                        '20210203:210304.385293:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': '\x85ӔчѼǠ˂ěԕ˂ЅǘҼήґđ^К5ϩłȼƌͳ˓ī˔˫Ƕ͵',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': '÷гЇҧӣ˘бЊαҮƕЩΓɠ˔ӰҔſ\u0382µӖ@ťǡҟёњĈθҧ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        False,
                                                        False,
                                                        True,
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
                            'name': 'қй˓ҷʌʊåǥĦъȫЗǸřȈвíԨҡŴŁɇӲɚɀĥ',
                            'value': {
                                        '^': 'int',
                                        '$': -4870358544643510755,
                                    },
                        },
                    {
                            'name': 'ϺȯſʕƓʐĨ˱ŀīƗǈĒȾÏʡʞΟħĸдԥѽɑ˕Œǂ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        781664.2561771929,
                                                        322636.50725048746,
                                                        259143.58291319804,
                                                        886325.4868356066,
                                                        937226.8498413704,
                                                        595986.5868074204,
                                                        193599.52170983306,
                                                        818906.4636463759,
                                                        83875.64393107439,
                                                        -37493.65921306171,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ɹ§ǐνͺƯӦǵêZĨԘƦ\x86χʖФњȭůy\x9d\x8bσіǔҐȻǌҐ',
                            'value': {
                                        '^': 'int',
                                        '$': -6507073121454360907,
                                    },
                        },
                    {
                            'name': 'ěνɟǯȃФԎϩʬϝ˩ơjўџŵžͼА',
                            'value': {
                                        '^': 'int',
                                        '$': -5777707324259382142,
                                    },
                        },
                    {
                            'name': 'ƚĩĵʯюѢőÏЌ\x9chϵʀ΄ʇϘЎԕљļɜҰŨ˶ŽʚȌ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210203:210304.386782:+0000',
                                    },
                        },
                    {
                            'name': 'ɗЭʗùҢȀů',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -7790536965766086494,
                                                        -4482910724407744452,
                                                        -169453344416651113,
                                                        3187147272776816943,
                                                        8490396122090545694,
                                                        -8836064229181648355,
                                                        6083996085074582779,
                                                        6175077818516949793,
                                                        2775582322094222738,
                                                        -7860681670434834083,
                                                    ],
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'Ҕхƪɟɒϖ˳[ҏƚ˴ǟ˺ϤĆ\u03a2\x87ˉɕƸѥθΏԈǵΆÂҠʗ˦',
                'message': '\x90oȽ\x9dȑķΪ\x85îЬ\u0382ʃҐ˥ҋQҐйΊȸzƑԛԣ˔ʜσŖ\x9eŨ',
                'arguments': [
                    {
                            'name': '\x82ƊЀԕǗͺÙÏʢȸȼ҇ʪjɟǔͽƝЖɐÝүԇÂʽрџȝфϛ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210203:210304.391825:+0000',
                                                        '20210203:210304.391834:+0000',
                                                        '20210203:210304.391840:+0000',
                                                        '20210203:210304.391845:+0000',
                                                        '20210203:210304.391851:+0000',
                                                        '20210203:210304.391856:+0000',
                                                        '20210203:210304.391861:+0000',
                                                        '20210203:210304.391866:+0000',
                                                        '20210203:210304.391871:+0000',
                                                        '20210203:210304.391876:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӱ˴ԑÃǺϯіÌҮμϛӤɜɿʯȾåӒ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210203:210304.392415:+0000',
                                    },
                        },
                    {
                            'name': 'ʟΟʾͶ˅]șүщɾ)҂ģЭɣԃ|őĮ˚ĳӪéćљƏҶʦºԧ',
                            'value': {
                                        '^': 'string',
                                        '$': 'çĚϼɌϰ˃Ӻȝ\x80˧ĨƸȗǇӋ˜ѯʥȊ\u0380IјǓӲɡī\x7fҹȓɦ',
                                    },
                        },
                    {
                            'name': 'ƑƸϝɿŰ΅ƭǃď2˜ɋȹϨΨǑɫǌљ0ɲΈǤư:ӞǃĻǱԚ',
                            'value': {
                                        '^': 'float',
                                        '$': 538073.4087349444,
                                    },
                        },
                    {
                            'name': 'ΖϿȯ#ѧȢĉ$λ\x9e˓ОʍĉɟˍAБЅβyŹƙǭҼɪ¿ЬЊΗ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ЫɕɡƏԬˌàĚėӒpӕ˧äϻɚĹИʶEӾӍʘ\u03a2үmӼƙǒʯ',
                                                        'ѫČɢөӹºțЧбԦªҩʊѬ¹Ҁғ˥ѳмӚ˔ʘʤʶ¦ǶżԦè',
                                                        'мʼ˹ſÁцǎҞΛǦӂhӡˈȁ\u038dНJԄpРͽаÉ\u038bӔ҉+iҥ',
                                                        'ϋƊ~ԭЊǓιʜ˽fŤяҳŴh½ˇќÛƽҡß®ȵɅćʁѐɐŨ',
                                                        'ƜўƜʘ?ѹνńӳΛȗŅЫϡʄѶȗԫOϷѯĂҭӄƔŮГǘϻϙ',
                                                        'ӝɎn\x9cľНϺоЅητБҧʂБΟϕǷӰÄǁĠщîҦLƖɳ˂Ɗ',
                                                        'ıҏʵҐiş҄xë÷Ǻ\u0383ʚѾҖHÖ%\u0379ԧx]ĄөΰɕȟΉƯӐ',
                                                        'ӧʚНɊԩȶqʥϢHʹʮ˹ǌςӹʳÕǭɴȄӸÙªȶʭbºԂσ',
                                                        '±2Ċπм\x8dŗȆЊ\x8cǔήßʈĦϯˇ<Řȣ˔ҨфÂ˞ΡːAҏʨ',
                                                        "í~ʸ˪ϏŽ˔ǘʹðŷЙǳ'È˝{ǖђŒȷƖɸȭƏӐΠäĵн",
                                                    ],
                                    },
                        },
                    {
                            'name': '\x9dƭƓѳǴ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        769310.260788014,
                                                        223256.3919483404,
                                                        844367.7383371958,
                                                        710541.5031212833,
                                                        949263.7431448221,
                                                        -45718.690751139,
                                                        614918.8344253623,
                                                        378847.82414087094,
                                                        538450.7421609015,
                                                        159320.5426518454,
                                                    ],
                                    },
                        },
                    {
                            'name': 'À˾żșǔĦҜɏĮɇà\x91ϕӱӋȈŦѝӹNZӹɲн҃˽˪Џҙԅ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        True,
                                                        False,
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
                            'name': 'ōĊ\x80ŐϣɀǤӐҪ˹ɷCԭѨ;Ɉ²\x8fĠѮʘΥ˃ûÎͽbԌԧǃ',
                            'value': {
                                        '^': 'int',
                                        '$': -8773171728006663906,
                                    },
                        },
                    {
                            'name': 'Ļ?gōž˲Ņ˳ʆʳӚÖ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210203:210304.397408:+0000',
                                    },
                        },
                    {
                            'name': 'ҾɹӲŎWĢԅģϵăĨǹʿԡеӂАOɝªщϐŋSЧɵӷɓ\x84đ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        815542.3964805279,
                                                        829077.4788621857,
                                                        722289.6408275408,
                                                        908814.1600620765,
                                                        -87259.92961131052,
                                                        703952.9404253551,
                                                        599626.2038832402,
                                                        533360.6936249313,
                                                        608900.353302407,
                                                        516162.4557882993,
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

            'identifier': 'ЗȼѳѠˊ',

            'categories': [
                'os',
            ],

            'error_message': {
                'catalog': '˱Ӿ',
                'message': 'Ѻ',
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
            'name': '\x97\x8dѴѷĞшǚԜőϼwҰơ&ʹğ)ԦØŪTìǖͶĂ˘ґӠó\x9c',
            'error': {
                'identifier': 'ʦΩϧǕɰʹ˴\u0379ɶɷΙЂƥʫŷoʥʈƒļ˔¼ĒƬгóИςI\x9a',
                'categories': [
                    'invalid-user-action',
                    'configuration',
                    'network',
                    'file',
                    'network',
                    'invalid-user-action',
                    'file',
                    'invalid-user-action',
                    'invalid-user-action',
                    'network',
                ],
                'source': 'FȾõĈªѿЪѽĞεǂщŖêʔȟԠŮ˓ŷДǨԏЮҎЅЍʩʊČ',
                'corrective_action': {
                    'catalog': 'ԝηǆɟʯ°ԀӜ5ƇϺʜИƃ\xa0ʎӴǲƨӫ\x82ʤpȨъяѫ"Ʒƨ',
                    'message': '/ӁȱÃΦƜЏϱĘ҃Ӛ|όǅɜƴӞDԡřɲǡЕϕțȾыźϳɞ',
                    'arguments': [
                            {
                                        'name': 'ǺԛӣϋʹҐëÅųƘŒȬɑϛǂ_Ԑȅ˂ìӐΘĒӟЄм\x9bԭǛ˝',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210304.375800:+0000',
                                                    },
                                    },
                            {
                                        'name': '7ҷ_ϷϲԫʋʖŴѤƇ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ξɢт˽ġɴuϼЇűЭÞɹªҔҷΣӆǁǮϴʗʿσѷǷƽ˩Űρ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            921646.3589162235,
                                                                            624400.8395806564,
                                                                            892057.460512353,
                                                                            268139.9199513306,
                                                                            611295.8102564055,
                                                                            784834.1148854957,
                                                                            826563.0351003496,
                                                                            901077.7147900823,
                                                                            -16604.21000386469,
                                                                            789336.1735577942,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΊёИОɡρ!ɵЍźYц',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ġęϿdʼϮρŉnэҔ_ΆƂЦǙƗΫɚȏӠƲǉҚÔѧʹ҉ͼϠ',
                                                                            'ɾӫћѥ\u038d˩ȵƶʅЁʗ/\xa0ÓΜʒМү˙ŹυÉŕɷШ&˂TąК',
                                                                            'ƬҸpѭЮѧĺwӹѾԫɄȣēǞєʷӜӖƔƷɝiς\x80Ԡ\xadʲǘӛ',
                                                                            'ǫƖɍ˜Ƿӿ®ԔËTBǆnϟŧ\x9c¯ԭлԕʌƘԜҴċē҉ɛԡҒ',
                                                                            'ŽҜτȈНĹĠ&Ӗ¼Ŝ\x9ać\u03a2ɭЙλ\x80őʧпÌҌ\x8eЧǑEӴÛЉ',
                                                                            'ΞѴ¤ңɨԩУ\x86ʻ<ņàҸŞŦԁћвO\x85ѨΖɼШƧĆшɍMӃ',
                                                                            '4.ZóҦρʙʍу˅ŖѿΪӖȓӈԑϫȟʹΑƷòSҐѬͰ\u038dƙЍ',
                                                                            'ԥǊзһӛОơƐЦ\u0378óÒƂ˫ǯҼԖ>ƄΖїȼϧѴȠŬѭӡ+ԑ',
                                                                            'ҍʂΠåČĎțϻǥɽϙĤοƞчɓҏɭѮΛǚȇ˸˚ȫƱƿџŀӮ',
                                                                            'ȸѦ0ϬХģηvԒʮΦӕg˺ʐƸɻġ°ǴcišӇŷѯČǻȽʌ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƌ˂˯ΥɊϿҢ΅ѝįƟЭ±үǥņʺĥĄǘȵґțȆμA˝ÖŅÇ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:210304.378004:+0000',
                                                                            '20210203:210304.378026:+0000',
                                                                            '20210203:210304.378032:+0000',
                                                                            '20210203:210304.378037:+0000',
                                                                            '20210203:210304.378042:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'üȁкȦјÆæź\u0380ǬϻɚǙơҖԔόΩ˂ǟԧϮɘґҔ\x92ӧǻȐé',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ξťƎ!ʛμɚãȝ\u03a2˞',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 611776.7125550959,
                                                    },
                                    },
                            {
                                        'name': 'ĄɬʐϚӜʈȺwïˈȖЉˮΌϺɟґΊƀÓӁ˲Ȫǀњ8ƥ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ǳñ˫£ˉʫŚ*ƖоÍȩʏʞʢGɱšә˂Ž',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            790011.5001738963,
                                                                            233182.5738090921,
                                                                            64133.087238420005,
                                                                            821646.9946067822,
                                                                            595443.9229722401,
                                                                            486046.72513114125,
                                                                            858199.689928996,
                                                                            295875.6855418772,
                                                                            704316.6256445043,
                                                                            478210.8643588037,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȥʯĻҘʱѣƎӊӕŋΎ¼ӚЎƈʉťѺ_ʻcΆŞŞȫ͵ͿZҕѫ',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'Ǡ)ʺшѯīǆȽ¾ºϝéѷҬ-\u0381ӐʠɃęŨhε\\¹ąǵJΖћ',
                    'message': 'ΠǾϵӳϷȉ\u03a2ƎԂɲұɈǟĖҧĄ=˦\x97ť\u038bȈÊѶŏȬЈɏťѤ',
                    'arguments': [
                            {
                                        'name': 'ˋΗ˸Ʌбϒάý»ņӶɆǱȒ˥ȌóŠԇȈʄǛѯϾͲŭҜϯ˞¦',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƢƪŇʃ˙ęǔŻΒ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            152959.09571900876,
                                                                            575578.9147366709,
                                                                            167875.89242005668,
                                                                            649410.2961498151,
                                                                            649922.0719139356,
                                                                            646161.221834273,
                                                                            990988.5479579126,
                                                                            32757.176489604666,
                                                                            718538.0867592132,
                                                                            852178.8755474176,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x97ɠÝ\x88ͿЕħMÐƼϏɔ˻ПŶчȾę÷ɻǥʳԧ˰gĿΤύЧđ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '҉ѯƅĘč˟ǬɶɐȥʶɅňʑвјf¡ÔҼԔѽƅЭϾ$[a\u0382Χ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            392082.8657579275,
                                                                            650038.295714116,
                                                                            465168.64153644093,
                                                                            823652.8704894105,
                                                                            532674.3828479784,
                                                                            555262.1293065922,
                                                                            960713.5346809784,
                                                                            840067.258328781,
                                                                            70044.75879047968,
                                                                            747041.8813858934,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɨ\x8aϾÇÚüӓˌĒԖȠ§ĎŚ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
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
                                        'name': 'ЧѲŧ»ǞˊҿͶǦ¯ԁ¿\u0381ƫϡӈęȍіŵħόЊԤƌťČƨéƹ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210304.383085:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʴ²Mӎǡϳě˦Ћȑ¤ȱYçɉԚŽ@˕τҟƍӁǪͳƲɐɈĹĖ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ͱɴǒǃ\x8cσƗð}ЙǽȋΧҪȓʇɧ5Ҟł¿Ō´Ӓ\x98¥ɂ˴',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:210304.383383:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ðʊƆӍȀƢ˅э³ғʎŉкīЖ҆ԢԝϦρώƻÂɮɷԖΝ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            730366.1713824535,
                                                                            -34128.57279092971,
                                                                            981429.8626427643,
                                                                            314221.1578786371,
                                                                            6739.861594088812,
                                                                            708613.9597346233,
                                                                            817929.3687983252,
                                                                            151225.207084873,
                                                                            293880.1714507611,
                                                                            530169.905684236,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¨',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ʋʇůˠ\xad˅ʄӬÆ\u038dōƥчȖөŃŘ˷÷ͽʒǐĨȔ@ϔű©ԛʪ',
                                                                            'IƷϘʔΉʁӹ±ǯʇʿȔȵ\x8eīA҄ŬƃȺlѼӧ\x85ʜӏСË\x91Ҥ',
                                                                            'ǖƎʮɿΖ˅ĝŪҫÇžʼͶеϡμҏζųӀҢҫ˷ɗȲӪģŕÎ=',
                                                                            '˃ʈƄϨxԖҹҠŏҏı˭èнΊΎXЩŁŦѿÓʰӴäџдhԂӹ',
                                                                            'Ϥǖь˺ɳҏԔĿI\x9cZƳƫºтΤə˫¤Ѭ˶Ċ»ȝŞӱцơǲѧ',
                                                                            'ʰЙЙѶϝǞЋW˓ͱѠӋϙ\x87ԃY3.ǿԖǄʘwĈ\x91ӳ\x90īÖǅ',
                                                                            'ȿvҐǂæɁӔΙèԊ˫0ΨTԪӶѠȒεƛȡȝĻϤюґԑУЅƵ',
                                                                            'ĶˠԆɬÙйÎСЅйЮǳdōȅ\x93ȯѝǃƱӲœʾBУμÚĊ3b',
                                                                            'ӫϊОғǤ˜ƱʲŅҩ:ŀшĆȃɲнŠʧгТAїЇ\x98Ā\x87үЄЯ',
                                                                            'П\x8fќϝ҅ʩҼ˷҂Ԗӗ½ϜƼάţ¡˕þǑ҃ǡимΓєʫŸҰ˞',
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

            'name': 'ƵɟÊ',

            'error': {
                'identifier': 'ûȥʹǔȩ',
                'categories': [
                    'network',
                ],
                'error_message': {
                    'catalog': 'ǸŹ',
                    'message': 'ө',
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
            'name': 'ύǗԏ\x7fɛҹʪɝ˽ȆšêΡшҳҚԢƦӰѥ+ɷŽɝǀěȨCńϔ',
            'version': [
                -302185488205547585,
                -6009799575843743592,
                -8825031400247599730,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ƳĈV',

            'version': [
                -6515779455635299096,
                -7594584927723385966,
                -22186603231882590,
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
            'event_id': 'ŔҲŵ»qҐΨǬӘƎШ˚ȫ\x98ԁЫӪdӥ\x8bgͻʥŃΡÙôѺЉɿ',
            'target_id': 'ņƇËьđʑ˦ϙԟѺјгЛơŶ»ĴԣϮӴĩŧĔ\u0378ɞѳѐѧĨV',
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
                    'event_id': 'Ͽ\x85ʾͷq\x90ȼѻΩѥұПҝ˸|ȩtǸǯʔ¢ĨѓөзʂûɏΠИ',
                    'target_id': 'ʽ©\x90\u0378ɍϢǝǯɬѱ\x9cǐԉʪ\x93NϏ΄ҝ˒ǽӚƲмӼƵѬ҃ѧȼ',
                },
                {
                    'event_id': 'ʗÂԚˁ\u0381ƶѽʼȂќχ˄ʰŭýĞҔсĀ˟ӫzˌ҈і\u0383ŚІȶѢ',
                    'target_id': 'ғˁԡďѤǀҋơŌŁ\x84жŘƆ\u0379˭ȲˇČΐ˂wɰϻǣǱʮǆĊҽ',
                },
                {
                    'event_id': '^jїƨœϯϕǘĭҿ\x86\u0380ԭɍ?ҥʉъԋҢԧΕż2UƒşҙŐӗ',
                    'target_id': 'ȹɠҒƨȊђŚӓҬжĵҗơɪ,\u0379ƥҠҰ˂\x81˛҃ȉЈ\x90ʋ¢ɰР',
                },
                {
                    'event_id': 'ƚãԧƏ\x9a\x8d%Ч®Ѡ<ĤĦɄЉƢťҩĦȂԊĞǼȩϟƿǬŐ#ɯ',
                    'target_id': 'ϻɛӞ˧ϛțæʨΚňЕƛɎƌєˀϟÄϮĉčЌǛӺłwωӺ@Ή',
                },
                {
                    'event_id': '҉ȵҌȕɍϼ¼βЧЦˌԘJѧ-Сʓ®ȘѤ¨ϊPʢϨҀ˵˛шў',
                    'target_id': 'kӭqҤĕѥƑȧ˷ǣsÿХcĐê«ԍɭͼʉˑ^ț_ĠӂǛ\u0380ӹ',
                },
                {
                    'event_id': 'хϠĻĸβȘҩЧȵŅęԦЗрļχHν\x94ȄƩԐΞӠζҧL˖×Ҝ',
                    'target_id': '`Ȃʢԣϗ˗ɨƅɖcӎȆĉŲоơʒȁøԠƏǰʂ˶/˃ҴԧǔӾ',
                },
                {
                    'event_id': '҆зϥϳѯǖӖˊӖ\x8f\u0380\x8bõ½˩ǂȶҏӐӾǳϱʲԞΩϒЯѨǑͳ',
                    'target_id': 'Ĩ|ʁoεфƏO8ӴĶ;WǘɼÁ\x92)њˋРҝbʶɼӁŎαŊԗ',
                },
                {
                    'event_id': 'ɶΜ±Ȓǻ˃˱ŠC˕TщĤƕʝΝӂ\x84γŎžԠ\x9fŔÍПʊυ˄\u038d',
                    'target_id': 'ѵVɭÉӻwĝ®JůvɤǀŗєÃ˖ҹ\x81ίϐφѴJҶʷ˝ȬǛϩ',
                },
                {
                    'event_id': 'Ѽϧ\u0380ƫȔˬЎɛӰǕ_ŇǬmΉǂɴƂÊδ˽Βϟ˂ͽǉ˒ͼʎϬ',
                    'target_id': 'ȓχÅԪфõ\u0383ĩѨʤȺSġ\u03a2ӂǧǾq\xadŚˎɷùԕEѕPȁҸŶ',
                },
                {
                    'event_id': 'ѵǽȇğΛң˾ƳĻɀȫĊКԪĿңξ-ϦŴѽиҲ]ҳˇǤӆňΕ',
                    'target_id': 'ҼүĺȂӨ^ѫ\x8e×Ƨ˄ԛȯ\u0383Ɂ҃Һ!˲ʑόŶМƔȏӤʛҺâƷ',
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
                    'event_id': '$Ϯýôϔѷ2\x8bу\x9fŤϤɞƥпІяɛłʮˑũѢ˔ŧзσҸ3j',
                    'target_id': '\x85ϽǢˊ˒ӓ¢ČщЉΈМĈϳɢȑʈǃĨϔL1ʌȮUqқˡϛŠ',
                },
                {
                    'event_id': 'ӫʣöǎӗŒϠQ˷ȴ˾ſȿȪǲӿԀɃЕ±ҶƋО"ŋАęɳ˓Ƚ',
                    'target_id': 'ϩӪΘűήěҰȅӛԊ}ŘΜѲθςåоĀ8υҵԉщIԝȤӕ(d',
                },
                {
                    'event_id': 'ɫԃϝǞЊϽǹƳȣϻvңȚɼƊѬǧˏÎşOːȑӰҷƉϕĢΧҶ',
                    'target_id': 'ȘŹԨǎѿɧǖ\x85ɱŘΪɿРƨÐȲђƑӇț˷ҝҠǴ|ϠÈΚӓŘ',
                },
                {
                    'event_id': "ǐԣЕ'Ȱɲѡċǳ\u0378ӴǠвVɟ\x91Uԙϻǖҵȸ˱ǉGŤԝǕ\x9d\u03a2",
                    'target_id': 'íƗήɶ҆l\x9cpӈвǂЏȍєķʃӱϖȈΊ˽ƖԫӬɤøɝOΫɧ',
                },
                {
                    'event_id': 'ˏ\x9dʩʊ҉\x86Ԟ:ĬȴǢʘƴæҞԙ˽ʈKϥʛɲ˸Ӑ®ƛϡβʳƢ',
                    'target_id': 'ǥҵҨƱåıϨRɪƜˍЪŷľȰġçЩΤ΄ǈƎ҈ƺǚЉĭιŜ\u0381',
                },
                {
                    'event_id': 'ьɖǑ˵ɯȖ»FҺĢЮøүRћʪѫҪүʢˮ:ѫïtĲЀӵˋԟ',
                    'target_id': 'ˉƇзӗ%ϕǨҖТūȨνɒľӑƨɃɤʣȑÅЇȯũɮɽϺƝɘƁ',
                },
                {
                    'event_id': 'IΕψ[ЦϠȈӜҘͲȟªвҽģ¬ιRF\x8fÀӛ!В²ѺћӴ҂×',
                    'target_id': 'ƫƇŌηǚϥƒеӓǋɏɘӦØķ÷ӸɃʉΐyεĭdȉīȢͿɇЎ',
                },
                {
                    'event_id': 'ĆѲÐĆŻ)ԓʷЖ-ɇʘ˸\x9fǉ2ԅʾӒȀÞƣѭҦӪƇɩσǟɫ',
                    'target_id': '8ʚȌӜЛȊϛѫêʬʦδĖýɉ¢Äё>ơΗ´\u0383ĻÝőʰȢӚϧ',
                },
                {
                    'event_id': '\x9aø\x90ΏϲòΖцγ˲ѱD\x88ůҸЋґqŉɞŝƄ«ѯϻİĞғƈŇ',
                    'target_id': 'ǋɁ8ĩˑԈÊļ˂ȺôˋžȎαϯ¥҂ҪǗΟ˩ɀԒәɝ÷Ԙɾ˖',
                },
                {
                    'event_id': 'ȜŦĴҙѹҬˠƥŞѶɄƺÑњɕмǁҏȏҺ˹\x9fӬ\u0378ΤîǝhȕЯ',
                    'target_id': '}ɤ˶ψɸ/ΒñԛΠËʦ¥ʊҙƳыŇәȲőǫΛŻ˨ҙÚǤʆӤ',
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
            'name': 'ǅҠΰÕ9ɣΰǢѽĪǾӎ¡ÀÈόʁӹȲħ˔\x7f\u0383J]ʀɮЍâҦ',
            'version': [
                -5020861793316262580,
                -6221747588714794346,
                -8258186473718582858,
            ],
            'about': 'ϓȶŻɧͰѓÊ˔r²Ǚ«˦˯ѽ\x7fƫɢǰǂӮƉĮǧϽҧȉʠǕҙ',
            'description': 'ɾƨÙ˫{ɊɇӪĲԎ\x97ËĉӠş\x93ɨȩΕǊš¹ĨȃѾʮǍºǤл',
            'authors': [
                'Ғþ®ң˦ǐŞșѼƗȰΑЙҝώғƄȰєīΝɫǳӴƸŖӫǋ\x83ʞ',
                'ʓŕγŠΡҥǷҾŕԗŁӒɒţԥϊȋɇʉƈȁƯ}ѿɓоıʐҵĸ',
                'өζAҏĘӪʜżϝʇѶǭȀËԢӜƔ˩ӍÆП0ćȔϕ˒ҹƲсȩ',
                'ϙo,ʫƭ˧Ŏɐý\x80ԨϤǊÀȫӉϒɞŵǞӊȚñϗϑđ¶ƖΉԠ',
                '¾ƔˏÔɍӫʻɨÄяƱѫЬԠ\x89ƝͿЂ˰ǫÀǻҪ}\u0381ǹϒԀƬȧ',
                'ƼȎóf>Ħåƥw҆\x95Ōî\u0379ȊšȲѨҾûԭ\xad\x84Ԃ˗ѽƲʀӉð',
                'äӪĔƀƛćǞʇʐÂƭʈǕǘԋxªӧʇТȬ\x7fĬèǞ˾ÝȲǠĬ',
                'ʔȃØ,ƍжɨǬÄǒǪɠɢ˸ëĤɗǞtчǎԉȿƅĸ˟ѺȟӚͳ',
                'тИɃӭǧńϯʇŞɋԃӺӈ%ǏμƗϿ\x90ƨġ\x8fͺиtƻ\u03a2tюҝ',
                'JǯmƄ¨їӮ:ҌцʨĭϦԕаɴɒ4ɦΡ0ƞɛҠÿѕɤԋҿѩ',
            ],
            'licenses': [
                'ӻͲϗŕʱαÉQԐžȬCǨˍĄ҉ԤáǂˋөǗɁԋЈŇӼ\u0380žѤ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ѣ˯ǝ',

            'version': [
                -6995427359419472329,
                -2608389610974191502,
                -5254020306349229782,
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
                    'name': 'Ҧ\xad\x8c˜˅Ӽ4ʶЫ²Č!ӘĥÐBԇȔĺѡӵď',
                    'version': [
                            -6520328060783151103,
                            -7413436351494271016,
                            -6058484031850240484,
                        ],
                    'about': '-ÒŵÛϝξίΌͰлҍśЌÏϺΡӞʣǺӽÑɱĕ',
                    'description': 'ӳʷɘƿ҃˞`ϮɈЦӚǓɈƨnӥȞϵԘɬÞԆђӻ˶ʭЭȥƾʗ',
                    'authors': [
                            'ËĤӧȝͳҥĜӶѹǄϔΞő?[ҨɯӾɁÕŤӄаȺѱѫНӿʈѶ',
                            'Ϥӝң˖ţ˓ԀʜȦÝԟӮŢãÊąÄ˱˗ͱʱŨӭǻþ\x88¼Ƚ5ź',
                            'ϪƷҙǢ\x93ǿͿљ|ЗÍʃȆǞİ×ȁȪΰɥӵĹҽҕҸͲƚ˖ț˃',
                            '/˄˯ʎŉԄȫ%ˎȬŖ8àʹˤĥѝх',
                            'ǊϭǵӑƅЧįȄӉтĔѽћɤѭGи˽ð\x90ȘъʺǗϦ\x82\xadɠє\x9c',
                            '»ːȋ\x86\u0380ʘͳ(|Έɫbâ&ѿʩʌ6Ȫлі˺ӵĆҝǵўӁȝE',
                            'Ƹ˘όŵ9ΚӭϟĬǚ\x98sǥũàƓВԤӥƑĶ½ÕĲ[ŀΝųǷa',
                            'ӅŬȚ\u03a2ĳɳŲųԫВĶќӇԂрǧѲǣΟȊƯԚďµϙƜЛ˲ƣΰ',
                            'Ǯƕ#Ƀҿӛǡƥʐ\u0381\u0383Џ\u0380ҚšȑԄϏѓцËѺϷнҺҢЉƍŭ\x8f',
                            '<Я+ѭͲ\xa0ӬɉȤɜьНʗѸ\u0382ƼҽŤmҫŤǝĢЪʹӎьĘѥǰ',
                        ],
                    'licenses': [
                            'ɺöÇƊĈɠzɘңԦӪɴlҧųȚȉФZɃʃˣȮƂȋĊŻ\u0383ӬͲ',
                            'kĳȇ˴șĀɃǙSԑЃ¯ɾÓЄϩɘϹϙâàµԚЗĞ\u03a2ΧˮΧÏ',
                            'ҎԉɊР\x90ǪкʗơӝόǏɩƥąΑɼƠ(ʲǍȷίÕҫƪ\x95ӣȍ·',
                            "ϫдʥͻ\x91ԓ'ǹΥȼ\u038bÔδȂВηґӤËеβНȈѽΞɶĒůȆ҇",
                            'И\x93ʓ«Ѷǐ\x8eͳɛɎđŲҮǖłůӵɜњȷκ˘ŵΗƛǑmӻŚ˵',
                            'Аɿ˵_ЎƠƺƴǋƲϤΎƝs҄ŔјϵѥWɋЁԮ˓жǕĂλΞȣ',
                            '˖ȦºIǐȶΆǼЫïΦùұǞҳӥaäнγԙʜʿѝψӊʂĂϊϔ',
                        ],
                },
                {
                    'name': 'Ą!ÄԣɥϞϠИÐӱʘƎJÓґΎɋøңsӥHΪ\u0383ƞ>îЌǾΏ',
                    'version': [
                            -6236327487303493860,
                            -3863034043480124475,
                            -9105078083620242782,
                        ],
                    'about': 'ȋӼќ\u038bγˈЏ÷TҰǋțùCĳӨҖʑ7ɲǨ§ˏĿũΜʵǡLȁ',
                    'description': 'ȄԓÉŧ˅β\x96ƀƜԁțźԖзŘяіΏƿʎđŊſҚԋ|ǙѮɛǟ',
                    'authors': [
                            'їέѴbҳʊ\u0382©ʀƓªɝśʪӂжSӊ¹˼µÝĝϞTɋΤХÔԉ',
                            'ƐўҞ˱¨ĔҞԥ*˃čǶÒΠļûΥöƀ¶ҭûºƁųԭʺȾӦQ',
                            'sϬӟҺıʥΆ ƭŸʒ˳¢ъζҙȍϴϬvӭǌͽˡѿЉж˱ʇҀ',
                            'ƈɺӥ&őǨƽħԨ·zțя\x85ģтͼɇɑtЊϺҴƍȿЕŲүĀѢ',
                            'Ϻ`\x8cѱđǸƧǇԫǩ{ǽΐԥȭљʻϣҕ;ҿ\x8dӬȫɘšƂӥ±',
                            'қΜΞдѤɿіɷϙȻïǇŤӱːϹLһͲŊǵ4ʋКΠˑӱΗýЙ',
                            'пҙҐҨɃӟŸМʟı΄Әԇ ˚ϖɉDӛƾŌϲ\u03a2ʈŢЉҌȂЊî',
                            'ϼͻþϤҲƍñяſҋƆʑ˧ʗǛ&ӱÞЈǏɲǽηȾÔҧďĂҿƮ',
                            'ōO˹ǻŉԁėȝŪeʝȕʡʫeɇԇǗǄ1GȔђϒƀαŦѬԥӝ',
                            '¬Ȯԛ\x8eƑьð·ΊɝʭҌӾʜУҌÓіɳǉӧŜʴˇŗМӣϹԙϑ',
                        ],
                    'licenses': [
                            'нɤǋòΊǤӖČʝɢʻȠěЊĽΫŝФɹԅǝˑз˥p¯§«ΣԈ',
                            'ΧӘɶƭŝƗĔшҞ$Hёʭ˹јӞZʃĠöЂǻԝŶщˎ˾Дјļ',
                            '϶',
                            'ӶѻҊƯЗŗvĝ+˱ƈͶȅȽǨlӡǇϽˤ8[ѱʪν϶¦ȣȈ˛',
                            'ρԮԡ\u0379œɋҼȋͺʕÎʘɚ}ъ˧ĽлȑΡ\x9d×ӸʈĪϺӣӄą˜',
                            'ɕĩϑϠ\x87ĒҲӲɋʴǔƇԚӖќƳƉǬԝѸɜǹ\x9d˭҆\x97ҞǁūҲ',
                        ],
                },
                {
                    'name': 'ɴєƕѿŇƻƙĒ³ɺԨѺŐΙʢOÞǖҋɴƹ\x84ȴРІЌɍƓˉȠ',
                    'version': [
                            -2634133626148109135,
                            -9036871512397127090,
                            -2644480852881308624,
                        ],
                    'about': 'ʢƃҋκԐύɑлɯԔŊOŶ[ɎˀŔǥ\x9fʋʊΙƅӌ¿Ũǋ8е˲',
                    'description': '@ΤԎ{Ȥǧˢͻѻ/ɉϟKŒӢʅƆ˓ŜͺεљԕԄѧɜлԪԑħ',
                    'authors': [
                            'ʹΌˀӿΞΆʺiЮ˴ԤɷҴ˂ŔɧŏċÉ)-ӘΊåǰпƃǠ҅Ɋ',
                            'ǵάa϶ɊĐ;ɹл\xad\x81ƫƒˡμjƁЃ϶ʋñӻШɴƃүąǉҵҡ',
                            '˶Ϥɓǟοƚ˽ԅϤӏz&ѪæӃ\x95ԃөǒҨÚ¹ɂCϨźϫ\x83ɖS',
                            'ǮϳǎȀџwϥ˚Ǉώϟ7Ӕеλӛ˞ԌʝDǧĺιÎҎęɇϳЧĐ',
                            'гӧ+ΌɥʺѧЀɥў®x/ѧΧ\x82ȅȲ˥˳ӯʆĮʔƖǹθȩſҭ',
                            '˅ɤƑҳΩǄȉōѦȄȒϬÞҳмԉEҒǟĿ~ɄċƩҊζЩԞҡʓ',
                            '<ȭлƂϠƠˠʉƯ',
                            'ˆȹΒōјтҭ/ӂǃ˨ҀȞ¨\x84ġɐЧǤÉĒͻĜŎƠf˪ΌâǴ',
                            'ЛĴȝӆɡ\u038dǧԄȊ\x81ΓϰdѦ¿ϫƥÞʵѱ őȽðԂGё8΄˥',
                            "ԮźɞÊɚ'ΧѨӨеĴϩNÇϼҨ\xa0ΎАʤɟҬˑŝɺЕ҆Lƶҋ",
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': 'ғɈŷũΡƾ8§ȅÆʊÐΌѨц×ɧϨуʔĴˣԒxɵӢȰɾԠū',
                    'version': [
                            -7937398668959878215,
                            -2187531116863915946,
                            -1389371788537392073,
                        ],
                    'about': '\x97ÐνM2ɍԞԍˮ¥ľьϓӻ\x8a×ȃĜӘн˶Ž˓üȸӥiǳəΗ',
                    'description': 'ÌșũåΓΣǨΑǘ-ũɐʠɁѥńǻǮҕԧɅ¹ƵʰXǺԞčȞż',
                    'authors': [
                            '|ƻӶ¯лʱҎğɟ½Ƽǌ҈ƱȴĽӕɡs>\x98ɍǑϒҊ5ȄʛƆŭ',
                            '|ɤș΅ǖҝˮɐŭ˝hӃ҂ĭŕӯԦŨlƀ˪ԏɲ®ȭȏЃƏϼÔ',
                            'ʿ¢\x88ҥɈόðɘɹÄϿ²ʼһɌτΟ½ǷӹϘÔф˰ǳ°ʦӕ½Џ',
                            'ƸÂʕÜÆғ÷ϰʢȔ©Ǔԗ\x9dũȇħǑʘʑÍ~оԧѷқʄnԍκ',
                            'Ŀ\x8aˣԐжӐҞѱɉʹҙĘЀȐЃˤԮΨ£ҁή',
                            'ñ',
                            'Ĭ\u038dĂѲŽzӿɅҤʰÄƢвӮʽӓϖѯϧ\u0380ϕɦҶҜXʇ\\ȫĮº',
                            '˞ЭһѧʋԤȆú˶ßԋҭңï҉ɽѩѲԓɌʧҸɍыМӖνΫ˕Z',
                            '˗Ŧ҈Ȋƈň3\x96Ͱ˹ϧPАĴ˽Ƭ\x7fú΅ë\u038dŢӖδĕÅ˜ȧĚϓ',
                            'ʥаȏɔ,ȽxģӀŐě҄ƀ,ӲʡȞʪʬʐŋѥӑ˽ΎűώĹϐǛ',
                        ],
                    'licenses': [
                            'ΞϨ˒ěǕɍxȸλфҿώĬϏōȥ·ƥìű\x9eЌӐû\x81ȱәñͲм',
                            'BʝѵΘѫΌɏɥͿ\x9fςǫ¶Кԋʧ˒ўԝ˞@lѠÉɾȤҲĸϽɆ',
                            'ȍҕǓѓæӯґϻћ«ɋϬ)Ɇɼƃўϴ˰ĨΒπҌђωưÝӖЫә',
                            'LǍ¥Ӕϫʿə"Ƴ%ўʑνσkιыϺÊӥuӍŲѼbͺĉҍœһ',
                            'ҧнԌ!Ǘˌ˔θ\x81ЄӶӜПƀkɋǡ\u0378zɚΕyȫŪȃǌҧˬʵϴ',
                        ],
                },
                {
                    'name': 'ϤŘÜԦ?ƿѹɫsӭѰѲčǛ¸ѱӠūΊ*˳\u0383&ƭϡ˓Ĳº˟˙',
                    'version': [
                            -4874314762371893044,
                            -4423498001121353836,
                            -1456412478308238590,
                        ],
                    'about': 'ТƋĀtϟϡćԇĈΕϖȔʒŠԈԈɽĶү\x90ÅıҗȠӧ0ӑɺӟ҇',
                    'description': 'ȤȰpɣÛЧǜt˜ʟȤԢҗҖ\u0382˛˞ϥ\x88р҉ȀÉƊɝ˨ԔҘψʬ',
                    'authors': [
                            '\x83ȣŉsїɓӢǻМчϠғģȣӑҊёʨ\x85ąǘкȟӪŔˤźѡӖЛ',
                            'ȇˢԕʂǃrӭŋb¢\x8bȍˉȒϊ\u0382҂ĊŭΣɤ\x84ŨˑȽԨФШȫŨ',
                            'ĸƑɰ/ӑǐшјԬӒңԋʤУÐhǛӁΙĐӫXĔϐμИҒеʻħ',
                            'ĶӜȪПƼȝ©ˌԮӅ\x9aηϗ\u038dɀɿŅǇÝˏКљŌŲóƩюǓ1ʲ',
                            'ЀƷʮӇƨѼǐpǓҨԁ҆ѳĞȼȀѪǖҨǿǉʰĒτЄɝ[gӫÃ',
                            'ѼɴÓ˄ǹǶ˾',
                            '΄ú³ԊȜΪΛɯύҚìŒÚĊǽîȇƊǦļцқԓЉɲǞǲҪěÇ',
                            'ǼϜǃОÿȗʦ',
                            'Ǫ\\iҎӓΐыΛƧΕͻȫҶԤϑĻ˩ъ¦ԛĘϻȶɕҗѪ˾řӶ\x96',
                            'ҭԔνƠԔe˙³ņϩ5Ȅ˜Βɲ¸êŎ¬ҟҢԩĲ˱ͻŽЮ&ƨ\x8d',
                        ],
                    'licenses': [
                            '1Ď˘ԩӴľԝӿƴԨͼ',
                            'Ίҷˑʥ{¬ɹƨԠκɭȨΥКȳ½ƨʮ-јЉԇèԤıβƧcԭӘ',
                            '°МŕĈʈυǬôĎǯԐƸԍƀěѹCÈ\x92Xҭҷ8ˤɀϝɤɅкL',
                            'ȤƤ\u038dʁ\x80ԘҳȨ\x8eʯήԌĻҏɿɆŉДԄŜéИēеѴǎéНĊ#',
                            "ŜԥΫӑŴҽŌπ'\x9bͲўõŽ\x9c%ˌE\x99jƼ¸ŉ˟ӏáϼĉˬƈ",
                        ],
                },
                {
                    'name': 'ɏɲǆϘĖƥ˪ʲǟŶɏō˗ǸǐПҗ\x9eɜїƹɞҕˆȼ}ӷҞĸΔ',
                    'version': [
                            -2357592912894751064,
                            -7506024124746452845,
                            -8784069073122891903,
                        ],
                    'about': 'ƔАёÙѺƞƮÕ˚\x87ӾơuҗҳќnҁϤĻɄίɀҨЅ\x98ʙιâԖ',
                    'description': 'cʎɪEѦӳŲϑΘӖεÇȜȳŰ\x96;ʯ\x96бɀ.ȑҞʇƦŢɞ͵ҡ',
                    'authors': [
                            'ƲӮѰǥ˳vΠ÷ǳԑóTËСҺÆєǱӑǽБ˪¼ҕ4ģνȢпM',
                            'ƤԎȵ¦ˁωΧ\x8aςȮʄʊƫҏɋʺӭKӻХƽȱΕ/Ñҥԟh',
                            'ſũПρĲҤѷɵǀǲȢǨɯȱǖрЖɞɦǓӦ\x8eΰZ0XŽȾѳɴ',
                            'ЎϝťѝƠáÞρȺΕȇˊɓȠ;üϱvǋŇĎϽɃӧșƥ®Шlӆ',
                            'ħÎĠǽ˄ŀ҈\x887ĭ»ѩҷМΜѢǛˏӫϚǜдǳΕѢJҎԖқʕ',
                            '+ϫʔ\x9dʭʬŚѻ҄ȇх)ӽɭǓəIǰȽԭɌƤиԧŬǆȄƚҫЊ',
                            'ҏЅӱȖόʨˊŅʡğӍ&ӧ˩ӬɿžɈЄчÜˮǶбʱŜӳӂǸш',
                            'ȝˠˈlљʮŶѐəĘϳ\x8dƠΝDƾԐѼԧďǵ˾ӹАŧŜФыͱԢ',
                            "ҏ-ŝϤɵŝǖǘàÒ\u0383İùчãĘďǱ'Ïф˾ΈвĠСɣˏˎê",
                            'ϗŅ\u038dĪӈɆſĂàǄĩьƈ_ʡʢ\x9dӽśыȊˇπǞӒДūӜĆˬ',
                        ],
                    'licenses': [
                            'ŌüΌŬʺˇéɬʝɼȚéȣԉΣӐɶФԬдϋϙpɘÔŭȂʈ"Ŏ',
                            'ЋΚϓӡҥξǏ\x80ÛæĚÛіƠĕǵӋk˛ǜҬɰĶzǕɕͳÚΓԞ',
                            'ñ\x88Ѷ³¤Ƣѷ˗Ј˂ɈӧȪҟϔ\x90ӥǃõѩ҈ɎρҦҡФȟ·ʗǜ',
                            'ĬˍƭǧДǑß\u0383ȉ\x82üɠǋ/åѷϟѯɧȄ¹үӎéͶoӈñȁƜ',
                            'ǔƯʏӑʹɭŞԚŮÛѠПџўҍǯΩȠƙĦʸҾɺ§ƵˣςЬӍǁ',
                            'c}ϰԒͺӁgæÅƍҫɵԡħˠ+ԎȋɟáИԉУčƾŚǘǎƥȇ',
                            'ƔƚɛȤʳгIĲЯʹГǐȥz¬ĩΌҊƷѳÁŲĢȦϓȢѷȠʝѼ',
                            'ȇӾɡȓ˾hѳӷ|sΥBLýЁƺ^ʔÔӡѓÉ˄ĳĈƈљѹϩԊ',
                            'ђ\x8fϹAѾБ˫ǩт҉Ǳ¶ȯʪƄЌԟʲѶƹĊ\u0381ȼ\x86ǸʷƬ\xa0ƧϬ',
                        ],
                },
                {
                    'name': 'ĺԦϩƕɇϥРȫôЭƢȆȄBɝzńʔɃ˛˙ĊĮƃ˾ʀ=ɑɃɭ',
                    'version': [
                            -2344720323093523078,
                            -6538645098696692346,
                            -381734007667864879,
                        ],
                    'about': 'Г҃ːƍԁШҁźĶłȘԮΐȭӏс˰сԉЍγ4cҐͿđǸӠқѡ',
                    'description': 'ˢŇʖЕ\x8c/1ǐNĹǾҊԠӛРίˤҶɁÇпҕȢƄȊӡʨԨȍӋ',
                    'authors': [
                            'ѡɬȕĝùԋ\x88ĿʥǖŽŦʷ¾ǋ˽\x9fʌ°Ӣʻséi',
                            'ӒѵTοɠƘңͱ¼˹ƶԥ¥!ӵʥǀȖǯɒ˛ȼȨңɃŴӫҢ˯ѕ',
                            '\\Ϲɑͷ\u038dǮҊŨSӍʔ\u0382˰ЏǝЊēŷΌД8ϻӏҭ˛ǥ[ԥÌӧ',
                            'ư\u038dЪ˻НóҏÇѵƍˆgȤɐϺЦƕ|ƽԌ\x8bӐϪȖȴӒλˍZЗ',
                            'ŴӂЊҁӮǕѣ˚βȥ`ұϝ\x89βϸ;ɼɖÉ˓ǂ\u0380Ęч\xadѧTέͲ',
                            'řμ˾҇ьo\x99ϴ´ԚȎ¯ˡεșþȅѣΊѯƲѼßѪ\x9aҽѡÊϐ\x98',
                            'ўӰȘӂ7ҁԁҢϘҲ¥˶Ȯʄ{ЁҭHХɆ±эпɌĞāöʸϒˡ',
                            'ɻĂЩ\x86ϬъľƲЭӟȭзʑɨFčͿ°҈ҲŦP˫~ʈΟҡǀɎʡ',
                            'Сİтӑüз²ҿӽԙҬʄÕȘh×Ş˓Ŀ\x93ȵɟǎ¿ΰˋѪϡƛʋ',
                            'ɒӗƚ˵ӬÛӪɛΫƝɑθԮÒǭIɚӑˮЬĻʉƵG¯ѤŻȈӎē',
                        ],
                    'licenses': [
                            'ӴԀȋϫȌЙóˆ\u03a2ьԞǚ%є¸ƖŝȊȃăΗͷȰƼş\u0379óBҺԃ',
                            'ʚβλϣɀϸȘȱąɀЀ3ʃӪ°ԨʶЁ˚ʅПɷԩːǇ×ӎˏϽʿ',
                            'Ȋɹц˘υͲ¹ʛМεüԛĺǼǿȏϪαɚÏþĿ΅В=ʨ˶ϫȴв',
                            'ЍʞƣЖY\xa0υʭҲβȎǿȮͲӑĨΦԫͽǌӟƶÑʓ=Ɍȩ\x90ȊØ',
                            '3Ñȝϓ[ˤǚФʷϡɺʝ\x8eˤIÒʍƦʡɛĈʍӚҫʃОά$ʹʇ',
                            '©Ǚ#ɛъo\x83ʄътŽӝȰѸĬͼʵŝsцυѵгҲčĚhȋͼɊ',
                            'ҙǗƜҠӚγăǏŲϕЂ˻)ҹΙәĠɱǅķdʡϘϘrđҙƭX¶',
                            '҅ʗȘҘϘǯʙÕϐϜǎѶ\x8a˖ġϙРΚƁȅόϸɺӈӿ±üǮȥЯ',
                        ],
                },
                {
                    'name': 'šɃüƦȎ5ȆTȮ;ƃȜ˗ôϧŋɊǭӨтĻ˗¦Ӹ\xa0Ьʹӯɟk',
                    'version': [
                            -8730243763161864458,
                            -1558891224572687910,
                            -3252250713389392697,
                        ],
                    'about': 'ǜϼUӜϙȿǀӍƘΥȎ˦]ΠˁєίƼ˗ʇķ˪żŜˋT¶ŮȂѫ',
                    'description': 'ɴŽ\x90ғǢĴĸɰïΦɉҊ˄ӱӽβɑȻ·Ҕˠόȭԝɏ\x84нӟЎǵ',
                    'authors': [
                            'ԛȞIɭˤʋɵ®MҙНȱεą\x93Ȥ^E\x7fːȀrҊĤ\x83Yԑ\x91ѢХ',
                            'ǔοüʤȯϡјЌ:ȌΕØÚĐӣʂŎ\xa0\xa0ωŬ¿ŪƘŘɮɃ9ǆʖ',
                            '˭ƤȓӕƕĴȅφ\\5Ѹēªí\x93˧эȃ\x89ł\x87ΆЫǢǎÝͼҁ˭ѧ',
                            'Ъ\x8aĐơĕȊ',
                            'ХǁŪԑѸjπɬϲ7ȩҐǓЗѦѷǺΒİƓΫƳ˴ҹƒʟЛʳӄɜ',
                            'ʨîӇʁБԌä˵ĦƃƆҌѺȇԄΰŨԣȹŘȇ\u0382ʷѾ\u038bԑʥиƐÿ',
                            '΄ƔбÈϰԓąԗԎƟ\x81åRӀ˩ƴȷΰ˔\x85ƁѷΤɫűŁŨŉћ`',
                            'ЩÚ˔Ëŵ·îҸˡȲɛï´dʛЙӪ˼ħǯҁҿμøĸϿϮȦŽė',
                            'ƍΎј\u0382ɱ8ËƹǃԢεˎɅ˖˹ƹ¿Ԙ¶ԓƥ{\u038bʄӺ҄ΰSκá',
                            '\x8fćϯŒͿɳԍʛʰȋʵƦɤKŨ˪їҳԂ2ӓϛ×ŤеѴʹ\x90ǂǟ',
                        ],
                    'licenses': [
                            'ƌ͵ēИĦʈǴʦϏǗ¢ѱљηE\u0379ǜɱкԌη¨ΣȗȑÎšҽǠǐ',
                            'ÉxɩƮӝЄŐ¤ƁƔ˫ȜȥԑɕϞ\x96ʢ\x94ɁˍʢЈĕ\x9eʤИҕƩӋ',
                        ],
                },
                {
                    'name': 'Ƅpҝ;ɿðԝΖ*Éҵƙ;Ѫˆ\x8a\x80ЅŲ;ʁҦġӥ$8ϜԂϩɼ',
                    'version': [
                            -7632296359156103224,
                            -4672519882406573741,
                            -5593165250652169073,
                        ],
                    'about': 'Ĭњõ\u0381ŕΈƣЅǫϞЪЄʈȩϻӱʸТƜЇÄΔĜʗĂw¼ąψʠ',
                    'description': 'ʡҪпǸӴpƤ˔Ύԁ$ʢçͼӄłɍԫǲŨωÓķҖΉųѧkҌĈ',
                    'authors': [
                            'ɾӐȚ}ѩ˺qϛѶǖϟȀϚʧɎɜɹHcВΊuŇөҪƮʍҘɲƆ',
                            'γϔjĆӜÔ\x7fƼƙӫηçɆ}ĜůƖnқυs˽ÜΌϰΌƚùΜŐ',
                            '\x93ԡĝƠȨƶώʠċѩӚ$ԗƵHBϮʟhʇ\x9dҗȞɱˣѦɄÿƠu',
                            'wŕĊǕЌǴǧеЍʪƂϻӰϼĆKˍǪЌҎ0ғГɴ˔ƢϡNɗŇ',
                            '×ǐϨʸĠЙ˕ʹϽ%ȥыʳу˵ħOІ\x99αҽͶЇOĉȨÊǑχȉ',
                            'ŷˢȑѾȊ_ǭьϻӼǌЬê\u0379ӑZTзɲiLʠϬʚɹʖ\x86Ыφв',
                            'ГĢÐɁԋЙζÓԎɈʨ3hΈƻԔԡȔЧкˇύϊʟȦ\x92ϕőòʓ',
                            'Žʓ·ȹϝ˼ɳԚM¡ěˋԓπţǨ\u038dϢˎӳơQЭȧ˸ʂ>фNϻ',
                            '=ôĜV\x88ҪІŌŘлǲҞŒѠˣûƭĕ´˥Ʌǘν\x87ĭԚӎϪȤȾ',
                            'ŵǹɉǯǥʼъȳP/ϬεσÅgƊȽ\x9bȱдÕÍЇȘʄ)£ӺČ˪',
                        ],
                    'licenses': [
                            'ŹϙˆƕӎʖɮÓНӌ&R˟Őɘ\x9bȔ/ǹѰȔҿŪV˧ęŗ=М¢',
                            'țÏʹʚȩ˜\\Ҳ\x82ФÔӿБɞԏήѐұȰɾzɥӔʟ£ӛΩΆʏ˽',
                            'ȋԈē˭ɧͱƬʅĞ˦ќ¯ц1\x82ʖϳəȀǝКϝĤȖʭԑΧн&˝',
                            '˯Ӗѯėʫźȃ÷;țƮȦȪѮПѧӡŁ\x7fĈЅцЌÒϘøƬѱЊĨ',
                            'ȻϾP}ˌѬϊŢºĦӪǵɥ\x94ʖʴɣɱʑѻǃǗĮųԦԉΠÄžΚ',
                            'NѻUʪКςěŕǎY\u0382ѕŊʨǣƝÿƑЃБȹɸˋīL7ʸ#Ԁʁ',
                        ],
                },
                {
                    'name': 'KćʃǟûȁӠʻ҃Σ*\x99ĤɆɘƍȩŜĽ˘ЀӖȶ«ȲˇϚȰ?Є',
                    'version': [
                            -9086177480506297597,
                            -734486816391052855,
                            -1297560764402940790,
                        ],
                    'about': 'zҳɟҡѳşǲűŚѵȳ¬\x9dʦǹŭȧɅήːɅ¬Љ\u038dɤӗƎ¸ʖŰ',
                    'description': 'SÔΫśċԚɄ\x82ÇųΑϫΊǘ¨ˏņź˦ȌяӜŦ\u038d˻ӡ͵ҜϔǱ',
                    'authors': [
                            'Ԉ҇źѱӗӽхҬѷϓƝЎʽʳж\x98ԝƤϷЯLшǆàğƊ\x88ɟƒʕ',
                            'ϨˆɖƂ\x83ʼūƽß˒ȰŔϴƜˊġҟȮÑƼѨȠŭȌϱȻԉдΌʌ',
                            'ΰ\u038dσӷŀɃҔȦˬӬ±ɜŜĝЃǦĄ\xadғ\xa0=ɒȟļɞſşŨŮ˹',
                            'ӤϬ\u038bӼʃҘхIıʥɟ\x93˰ÕĈϡͰ\u0383ɆɵLӄБSδ˗ϠӦɣȈ',
                            'ϪȏѐзʵǧѵíJƜϲȗόɕƽĴҶʋԆœǑώùɃҔψđ˯Āљ',
                            'ԁŞŻϮѦȂѦӕÇNѢ˗ɢ6ЂýПŹɹɪƹųÚ˚Ƅѩɷѐīȓ',
                            'ʑѣìCȷЌÆ҃ϥVĚӐ©ƫĶhʂЦȱĬ¿ȼčϱsѳƣƠɴҨ',
                            'ҽ3\x8e¢δѐņ˲υÅbõƉ÷ʦęȭϚʥüүď˵ū+Ϗ˜Ț_Ɓ',
                            'ĝҟĻΐӵΆ\u03a2ĤįǭÐŲҫώɒƊìѼ˳ƧϩӫŦǙϿй¾ыcɆ',
                            'ΩҼɎӀťͲƍʧ ýńќȄƶɟԭǏĩˬǜɡĻӮȢӑҾŦȲΗԢ',
                        ],
                    'licenses': [
                            'ęԄǤВӨΙԎЇçѻɀϿô\x899ЁфΧbΠˆþÏɴϊǅɪpʫȌ',
                            'ʺяĹϽӚƮ˴àЫȑʸ<ӱҁˢԂƹҌʺ˥ˢśxĵԘӄќ®ðƻ',
                            'ōɏтϸŦӰȀѨӖҏɹ͵ԡʺҶԧˌІюӜmtˋΣĶɲȧм˛Ł',
                            'ҵčɾͳ,ĭɂʗ6]ÃûýȮ£ӉȪˉ˚ŎҾάӞЂӀÑΛϯԛ˝',
                            'NЁÍʷ\x96ɎӌAɓʹ\x90ˠЇŅȐΖоİϖӐȻԬί҇ǕĵЃԄԊv',
                            'ѹ҆ӨϛКѾϤɄѺȵĴĪʣƦӚ§ͻʕЎÕΐΏˬĒ΅Ӫ˅ҜԬβ',
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
                    'name': 'ЧЂƤ',
                    'version': [
                            -1862197886429576126,
                            -4624376610190888678,
                            -6010850609370573284,
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
