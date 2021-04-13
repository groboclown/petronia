# GENERATED CODE - DO NOT MODIFY

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
            'name': '\u038djγȩŎԀŘԝɕņǧnȓùϢ˦\x98βʒdӖФǋǗ',
            'minimum_version': [
                -7352954374446121072,
                -8103405353315053037,
                -7096032045505234264,
            ],
            'below_version': [
                -187817163946010594,
                -6761428526139421030,
                -4149273147533922273,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ҽŀǉ',

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
            '$': 'ÏÎȏéС¥ȤµƴƝʔҩƋѕӲũǴƏȶú½ýƞĊȈӍÅțӮƊ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -8223820038529959429,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 980040.8575964437,
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
            '$': '20210413:001025.440083:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                '\x85ǽéʶ®ŦεǂĘҸȼԠüˋ~ԏƁƝОȢŭ\x90ƨċЯʞHΆħҥ',
                'ĳɥĚʀϱǻѺɿÄƁǎ˂ŌКГүӺʏӊ¹еEͽȀƄʓLƝÏ˦',
                'ԁϝϋΧ˓TŲɿžǻŴя¨Þ5ӨšҵȠɼɼVăČЇêʷÎԗϽ',
                'ʻƛǵǱê˺¡ǘτҩ\u0380ʼѪȊЈԋӓϔҺxƋϴȳʧ˭ҍ0\x92ҠǨ',
                'Ԩɀȭ˹ӺҘǭεҲԈʗɷȋȰ%ȷΊPɑӈȈǽĤĮ˞Ϩм\x9b˂³',
                'ԠâľŁƽbҀƫΌÞƺĝЅȴǺб˯ʼӞąʥ`ѯӬτǴč:\u0381Ϯ',
                'ӖФʞŨʧƚΆǿǜʾˠ÷ϟԌ\x9dŗŗgīУɡkͳϿLŵͷˍ\u0379ɱ',
                'ķѕé\x93Үµ\x81ϼɝƊęͽ<ўΈɀȸ?ӟΥƼșɹҽ˭˄ғVŃ\x8f',
                'Ϫ¥όƖӶ÷ѡɼǣЈgЬ҈Аɦů\x8cШƼʺĖƀ˺ČǝǊρϲƺȄ',
                'ιϢÞOȈŞӶԞ£Ă\u0382@ΛƱϵzҳɛӨӹƁӗƆҒϬȣԟɆѦӴ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -3388669767869559245,
                -4060159501485245066,
                -8421381726007619373,
                -3003511664455347683,
                4746910575308175408,
                -4429780367109227706,
                -6684862647711698762,
                5113644462107118353,
                -2944942195185968662,
                1613883001780892815,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                625742.2741125438,
                566286.1760655734,
                637574.520247554,
                56135.723666635866,
                118180.73824974269,
                430069.7093018065,
                666591.2332711181,
                161555.34209905137,
                -27832.584154370037,
                212271.59580243746,
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
                '20210413:001026.435479:+0000',
                '20210413:001026.452899:+0000',
                '20210413:001026.474057:+0000',
                '20210413:001026.493311:+0000',
                '20210413:001026.514658:+0000',
                '20210413:001026.535137:+0000',
                '20210413:001026.554106:+0000',
                '20210413:001026.573257:+0000',
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
            'name': 'ɿψƚȽСǭ˙ʼ\x9aˊҴʲ~ǿӮϻҹȾ',
            'value': {
                '^': 'string',
                '$': 'бӮӽƀ\x87Mв\x88Ӽɝӕŀԇ7í`ЉҗȎԁϴƹăegȉʂʉʼӖ',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '҆',

            'value': {
                '^': 'float_list',
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
            'catalog': 'н\x87@\u038bƻkѻ\x94.ЍлҝƇǤŶӧǓûŏĎřˠŵɭβſťџ˘μ',
            'message': 'ɸҡϨɱӪ\x8fÙŵȴˆ,¹ҫҷ\x88uûшӰӁҜбѼҪǸƓҡÿďì',
            'arguments': [
                {
                    'name': 'Ɲuā\x9cӆi<ʦԮʹҒщʨθѿ˜ƵќƗáрśʹ\x88\u038bȶϖΏҷɓ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ŞˏěВɞʠЩƢ˚ԭԧϺƉʹÉʩžĹ҉ƈȰеɕʕɕСǼԍ˻\x9f',
                                        'ĠҞÝÒǵіʳΗԤљȗҟύŖπɘĲϮϘðΊіˡǣyƾû˸ōӪ',
                                        'ͻЎ9é¼ȶYύȌӥŅԌƺԈѬ\x83иć/ɼҮűʛˑɵŏų-Ѯϳ',
                                        '½\x90ǺƜԅӦͿӲ\u03a2ɓҕǱɰɱȋͲȕŭ҄ÏŃɅЕÁuϱ~ω\x9f˲',
                                        'ϋƭβЌžƅƙѹЬя²˅ϽǷԑʷЦөҥ˘µԨ\x99Рĥ˼ȷÏȹĞ',
                                        'ΌAη]˜\x97²чMPƤŨӞǠŁҨҍѨӬ§/ơAſǠǯ˟ϑyΨ',
                                        'Ĝ˓уµŻ˵F\x975γ҆ɑ(ϔΈUɔǕƔкԂВʘ҉ȕѵћԣ\x96ū',
                                        'ÔӌűϣΊԧОƣ"hɸϒFȐǁxÐʗӝϖɲɦҎ\x9e\'ӋͶǈƕŊ',
                                        'љқӀѤзɢơʌÒήFӅСɾҘґŰŭΐԌɦ»ʗѰҲЪƣɰԆϟ',
                                        'ĭťʃ6ƂÌžӭ"ɭ`ÅǌŚʃάǤ;ʀΐӬ\u038dƱs\x80\x86WкΓŢ',
                                    ],
                        },
                },
                {
                    'name': 'ǻҳ;Ũ¬6ÓϙӈĈӳǪņ\x894\x81в',
                    'value': {
                            '^': 'int',
                            '$': 89256558113303815,
                        },
                },
                {
                    'name': 'ΕϳČӥ_мȸƅӄӊǖĢ\x93ȍШĜaӥɃAёğÃƃ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210413:001023.810620:+0000',
                                        '20210413:001023.824579:+0000',
                                        '20210413:001023.837980:+0000',
                                        '20210413:001023.851424:+0000',
                                        '20210413:001023.865090:+0000',
                                        '20210413:001023.878134:+0000',
                                        '20210413:001023.891866:+0000',
                                        '20210413:001023.910122:+0000',
                                        '20210413:001023.927737:+0000',
                                        '20210413:001023.951269:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ęĐқƵͷxõɿҀǁɨ`zˈƺʇ˽ƲŹЂҋѼɅâĚĚƃÁĕŉ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': '©ŵӮęԇ˔҃1ɂԘPӏԭ\x92ΑϧĽϢήɍϏГķʳ',
                    'value': {
                            '^': 'int',
                            '$': -3082136548178052880,
                        },
                },
                {
                    'name': 'ɋ>ȴıѹԞ˶MʖǖԘ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210413:001024.190282:+0000',
                                        '20210413:001024.208022:+0000',
                                        '20210413:001024.226348:+0000',
                                        '20210413:001024.246097:+0000',
                                        '20210413:001024.266487:+0000',
                                        '20210413:001024.286193:+0000',
                                        '20210413:001024.304119:+0000',
                                        '20210413:001024.333778:+0000',
                                        '20210413:001024.350737:+0000',
                                        '20210413:001024.369350:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ȀǌĲ¼ΊʺmȈǓǏ˳˻ќǺӲăšңŢ\x88ϾЀŎӬCɮϬδԝ{',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210413:001024.460268:+0000',
                                        '20210413:001024.481186:+0000',
                                        '20210413:001024.505837:+0000',
                                        '20210413:001024.527511:+0000',
                                        '20210413:001024.548589:+0000',
                                        '20210413:001024.565413:+0000',
                                        '20210413:001024.584446:+0000',
                                    ],
                        },
                },
                {
                    'name': '˶ӼŀϙәºʙѐÕ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210413:001024.687899:+0000',
                        },
                },
                {
                    'name': 'ԎʫřҌËȽϱϗтŐԣϿáίĸԗϯϤβŉѳ',
                    'value': {
                            '^': 'float',
                            '$': 246661.2357830099,
                        },
                },
                {
                    'name': 'ý',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210413:001024.836987:+0000',
                                        '20210413:001024.853183:+0000',
                                        '20210413:001024.870902:+0000',
                                        '20210413:001024.884338:+0000',
                                        '20210413:001024.898001:+0000',
                                        '20210413:001024.913223:+0000',
                                        '20210413:001024.928182:+0000',
                                        '20210413:001024.943309:+0000',
                                        '20210413:001024.961034:+0000',
                                        '20210413:001024.978409:+0000',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'μӠ',

            'message': 'ԧ',

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
            'identifier': 'ӰҴŅιϥЌκċ˛ƺÙҭԡɆҿҠɑӦҋʠϱϋӲü˒чȆӝӧ˂',
            'categories': [
                'configuration',
                'os',
                'invalid-user-action',
                'configuration',
                'invalid-user-action',
                'internal',
                'invalid-user-action',
                'os',
                'configuration',
                'os',
            ],
            'source': 'ѺЛҴvʲʒȲ)ԖχǿĿķщĢŐԤӶΘԌЭ0оЇǅӁϞɹęá',
            'messages': [
                {
                    'catalog': 'ɿЍИȕԩΘЁŐȹӞȪʮѵRʳєƿɯӠϓШӜѳɂϴŸȘʩΠɳ',
                    'message': 'ϖ˾\x85ŃưsқӹȕSȬˮ\u0383˜ºȤǱ˻έ\x87ΏĲĵŋРԘƞȞÞΩ',
                    'arguments': [
                            {
                                        'name': 'ˠðʶʿƅˎϥЯ϶ǛĞΈ¸ňĄˆӝʟƛ·Ņӑůԩǩ˯πƦԬ.',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '¿ϬƣWɎǬђ¥TԟÅʈςəŋŸӯ:ȝΌʘ\u0383ȃΝŰ˹ǲǲ1Ӯ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 700977.624467247,
                                                    },
                                    },
                            {
                                        'name': 'ѰЎƬɌίĸƗ\u0383ҬğњƼ\x9eϖΥ|ΕҐșӇϖԝMŀѭ˨ѕ|²ɿ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:001006.899497:+0000',
                                                                            '20210413:001006.912617:+0000',
                                                                            '20210413:001006.926166:+0000',
                                                                            '20210413:001006.941567:+0000',
                                                                            '20210413:001006.955318:+0000',
                                                                            '20210413:001006.968925:+0000',
                                                                            '20210413:001006.984517:+0000',
                                                                            '20210413:001006.999690:+0000',
                                                                            '20210413:001007.013441:+0000',
                                                                            '20210413:001007.027493:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȁѐЛЍ\x83Ӂƈ¬¬îɆɽʂ?Νϫԩøȯǘӯ\\϶ȏ\x83њȘͻÑ',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɇü',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3163128585969920133,
                                                                            5365342131569286371,
                                                                            -9037063842297294545,
                                                                            -8795891985641874449,
                                                                            8587884321352674860,
                                                                            5268835650131501776,
                                                                            8575359905495317141,
                                                                            377827360311173570,
                                                                            -151306345001199572,
                                                                            8499845926709945506,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϽŖϾщѡƟětĄÚ΄ķňƲ\x93',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:001007.572847:+0000',
                                                                            '20210413:001007.590181:+0000',
                                                                            '20210413:001007.609004:+0000',
                                                                            '20210413:001007.626739:+0000',
                                                                            '20210413:001007.643080:+0000',
                                                                            '20210413:001007.662020:+0000',
                                                                            '20210413:001007.680096:+0000',
                                                                            '20210413:001007.698393:+0000',
                                                                            '20210413:001007.717687:+0000',
                                                                            '20210413:001007.747577:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʀɓƙϱĿ\x98ųɐȉǾ}ӻ\x9fʳдѱҨ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ˏȮï[ɮȚӽƆѾ?ї2ȱ˪ʰĠ˯ǀř϶ʟ\x87ɧƑԠѶê˪ĴǴ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΆѪOƁɃɒʝųѴ˂ΣͺЊÒ\x8bť?ˉȧɑ&ěӵӉƧɶһҏŻȗ',
                                                    },
                                    },
                            {
                                        'name': '\x83Ñƿˉɞғ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:001007.959657:+0000',
                                                                            '20210413:001007.976542:+0000',
                                                                            '20210413:001007.994102:+0000',
                                                                            '20210413:001008.010795:+0000',
                                                                            '20210413:001008.028061:+0000',
                                                                            '20210413:001008.048800:+0000',
                                                                            '20210413:001008.068395:+0000',
                                                                            '20210413:001008.088861:+0000',
                                                                            '20210413:001008.109322:+0000',
                                                                            '20210413:001008.129962:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĒɺÙӖґ;â÷рǀӔ\x91ԫӕЁЋΑϓӫǊӅӫΜƼΟʦ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            609485.7815071978,
                                                                            102342.94426573979,
                                                                            35339.794459669705,
                                                                            -86671.66584399978,
                                                                            857842.8084314988,
                                                                            463732.51826456643,
                                                                            634983.6257005414,
                                                                            -94402.13127534016,
                                                                            286606.4237560943,
                                                                            511459.59123119095,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɳˇэ\xa0ɐɇӎN\x82șßϥ«ѱϰѧ\u0380ЧњơӒȻɅÍʜĥҋԇвѳ',
                    'message': 'ŋɃƱȺЉнɼɽçđȽĈȳϏ÷ӜDǄ´șӛВɌɏϭŃЊѳŒz',
                    'arguments': [
                            {
                                        'name': '©ԬĚƗĂ\x87їюŰŴĮˎʭ©',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7140896748476070955,
                                                    },
                                    },
                            {
                                        'name': '³pΛεǞ͵Ǫ®ѐʆE˭м\u03a2/ϴ6ԕšƤɈ¯˰ϊѮˮȄϛˆ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            639672.1020129981,
                                                                            85727.0458983487,
                                                                            321060.3352899547,
                                                                            34968.18503299545,
                                                                            134009.9485248978,
                                                                            8013.917649409937,
                                                                            585014.9602168893,
                                                                            581317.1747919462,
                                                                            46663.21580934082,
                                                                            489329.91870027257,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӓΥωЫԀ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 612299.236913721,
                                                    },
                                    },
                            {
                                        'name': 'ԣdǘɍţӢԚ\x93Ɩ˷ÕӼԁƕПǭӿȺǫǪҶΐǦƋʮΙӵǽТ÷',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:001008.930079:+0000',
                                                                            '20210413:001008.946720:+0000',
                                                                            '20210413:001008.963449:+0000',
                                                                            '20210413:001008.984152:+0000',
                                                                            '20210413:001009.001028:+0000',
                                                                            '20210413:001009.017992:+0000',
                                                                            '20210413:001009.034946:+0000',
                                                                            '20210413:001009.052289:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': ']ӠсΎѱǈӽЁ_ϮǺǌˉƬРϋπǑċΧϗζѶԩōˇ¶kſɗ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            643887.9722774108,
                                                                            934484.3510192082,
                                                                            539936.7690404217,
                                                                            590394.0413429199,
                                                                            221372.399693697,
                                                                            -84582.4672447,
                                                                            147055.7403958553,
                                                                            423633.4267524989,
                                                                            991096.868398011,
                                                                            927503.6273419971,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƞӐŮӐӥǝҋÿşʽ\x9bιΙ9ˈϔəЂϲ³źҞƞƄɁмҤмĐέ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7560515379165434685,
                                                    },
                                    },
                            {
                                        'name': "}ř˚ӦeȂū'ΝξČҰǤɾЦϣљяΘϰɮ˭ҧɦȄ¦ԕҙԎӳ",
                                        'value': {
                                                        '^': 'float',
                                                        '$': 473241.35153843765,
                                                    },
                                    },
                            {
                                        'name': '\xa0˖\x9dĀћXx',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001009.593232:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x8bÆɄ»ːįѺſR¬Ƚ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʏίǉƁʑϭǎƍ\x81ʹŪ¨ÌϖƽѮ¥ӌǳІȳϝϩҁϡӻǥдюο',
                                                    },
                                    },
                            {
                                        'name': 'ɡ˟Z²%ƊȍɅūѲɋҝκʈ΅Ǔ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȃȶЀ˵ŌК˱ӄюȷйΊSЧƐѯìȁ\u0382ʻɩ˥ôԆȥҖçӿ\x88ʏ',
                    'message': 'ǼӛҡӭͶʳӋѐҢɘЭЛЩҡģˌԀĔȰΠʣDœŢʫȱһӽ·ɯ',
                    'arguments': [
                            {
                                        'name': 'ԙʚƓї҄Æ~ѧÞī',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:001009.891315:+0000',
                                                                            '20210413:001009.909990:+0000',
                                                                            '20210413:001009.928812:+0000',
                                                                            '20210413:001009.946640:+0000',
                                                                            '20210413:001009.964817:+0000',
                                                                            '20210413:001009.982272:+0000',
                                                                            '20210413:001010.003011:+0000',
                                                                            '20210413:001010.020640:+0000',
                                                                            '20210413:001010.037580:+0000',
                                                                            '20210413:001010.055338:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӱ;ƮǇcǳϡȦĖɮҡϜYʬÑʑ©ƮЎƣ]ªJǊɵģȤІƅҸ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƎóºʄΏˬГǓҏӸͿòԤ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5900689239929079341,
                                                    },
                                    },
                            {
                                        'name': 'ФʞϰďėτĮЈЏǕÂҗƅÉ͵əŏdŇŉʷчƵ\\ºǉƟʩЈÏ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƵĴѽ\x9fҚɁǛɋȾȐƎƚΊ˯ɈȃѢǨŤýʑ»ӡ\u0381\u0380ϊ5ŶǺů',
                                                                            'ǟ˶ȅʎǯuːȱʱǧĤƚğԕ͵РҾɵΞɞʻѓÇǡˢЈxњΎ҄',
                                                                            '˷ƏɿÚ5ƚ.iȧŉΫ\x8aÁο¦`ϵϯѢœǦ/\x99=jӴϖ%¾ю',
                                                                            '8˒ɴҥÑƍƪƀрПЫԙÌъþѡΘŗļќŔºʛӄþɐĺ\x96ϡˈ',
                                                                            '˙ȡ҂ʃͼʹϻ£Ă˫ԏϵ˦GMϔĮōùû\x94ӴƳηƅ˼ŇʨWŧ',
                                                                            '_ԘƼӚΪ΅˜ķȸЮʠԘώǿʚĉƮ˽ԇ˙*ўƳƑƔˏϻҐɹ.',
                                                                            'ѐȘМƵςҚѳюωцԗȡΧĎ|\x9d҇·NώǼÊϠ҄΄,\u0378ƫ>Ú',
                                                                            '\x89ƓӆӼԞЪҫĖģŬɈϋЩɶZϢƐƧǝóêԭ\\анӛзoǙƖ',
                                                                            'ҙƐàKöɍΝˌýΔGҝƋĄʱHüŘԢǭČӓʀĀшǀӜŧ҆å',
                                                                            'Ͻ҅{ΥԏͼŵҏʸʮɯÍ¾ĀбUҊÇƄɚȫѽҺӫӃĔѭĮҽÜ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĹƐ3ƩФ%Ï5ЏǑʚðƹ˒ĩе',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:001010.743099:+0000',
                                                                            '20210413:001010.765528:+0000',
                                                                            '20210413:001010.788903:+0000',
                                                                            '20210413:001010.810818:+0000',
                                                                            '20210413:001010.837265:+0000',
                                                                            '20210413:001010.859433:+0000',
                                                                            '20210413:001010.878146:+0000',
                                                                            '20210413:001010.898443:+0000',
                                                                            '20210413:001010.915400:+0000',
                                                                            '20210413:001010.928871:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'PƞźǡҳҋәцӯњȀѭt˰;\x98ɨʦȘϠƺ!ъ\x9fϏôȰîѼ6',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'PŠԞâɪкˆǄӢȧŵҮƷOßˤ\x88ȴӀϗҔˁ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 681387.8957481544,
                                                    },
                                    },
                            {
                                        'name': 'κăΝ˺ĒѿӾʵԌɎȗĔǮƂUԛĴJ6\x99OϷ\x95ǵ˵ͶԮłǐЖ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 58018.97205774524,
                                                    },
                                    },
                            {
                                        'name': 'ɿҧԇӻ÷_ÊѨø\x9aŗKwӵԏѸÿѴԙʢȵσɀ˪Κю˦\x83~',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            681429.0860229124,
                                                                            681011.5541284706,
                                                                            979594.213160093,
                                                                            106066.97157328631,
                                                                            443517.3367706925,
                                                                            385379.0189693684,
                                                                            769251.0441297783,
                                                                            60902.99476231876,
                                                                            931183.7652818959,
                                                                            976659.2774627642,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӋҀɸΚ\x7fήĖɼʺӠ\x92ɀ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x89ѭ\x99ʐ±\x82ԠӐђϝПѻȾƒÒ\x8f<ͰϡBǯҫþPöͶřЉѦы',
                    'message': 'sҘϜЯʭ\x8bů\x90ȨԖǠ½ԩφ˨ȥӅZăś҂КŠ7ɘQwϟȅε',
                    'arguments': [
                            {
                                        'name': 'ʲɩЗеԈӾԓӂ·ðÙ¹ǎȤ+ǱВѪVў҃Ő҈Ѱ˳ȧѳ˩Ж˔',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7963798654457409524,
                                                                            -2190271433646307558,
                                                                            -8578297135024375496,
                                                                            -1313951201985756712,
                                                                            4841791105411551487,
                                                                            7132133121284445602,
                                                                            2658825874348339529,
                                                                            8960219194666606925,
                                                                            2794412709361992656,
                                                                            -9072997244277311507,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ғðϲ\x94êҎӅӳěЇTѧs¬ŘȱʭлԑLʖ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:001011.977402:+0000',
                                                                            '20210413:001011.995048:+0000',
                                                                            '20210413:001012.013043:+0000',
                                                                            '20210413:001012.030035:+0000',
                                                                            '20210413:001012.047320:+0000',
                                                                            '20210413:001012.065699:+0000',
                                                                            '20210413:001012.089050:+0000',
                                                                            '20210413:001012.110005:+0000',
                                                                            '20210413:001012.134837:+0000',
                                                                            '20210413:001012.158330:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҸϸсǑʁύ´҆ǈǎϧӴõĩҏѕӡľӥΐΰȅӿɼлʇļç\x80ѵ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001012.272221:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԘΜϣǸʴРwĴĖƳχ˒ǾǗҎԌҟύˠήƏ\x9f®ѽ\x88ŸԃČŮЧ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5172638674537497579,
                                                                            -8152771740116506329,
                                                                            -2487636616435307107,
                                                                            4997108863537192117,
                                                                            4023015692883486702,
                                                                            7234493973119943379,
                                                                            -3836617746659573794,
                                                                            -7430152098301485996,
                                                                            8080119874412939300,
                                                                            958978267595235166,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԦιҵˇǔĝǊεӚ\x8cĵϥǯҒƊŋAұ;ʹԑȞ҅ëΙ2Ԋ³ў|',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            135721.88122663618,
                                                                            466422.7199041301,
                                                                            819969.4847845264,
                                                                            523694.4331883178,
                                                                            502259.47826289013,
                                                                            40057.95979032159,
                                                                            574767.4214687692,
                                                                            814448.6142621922,
                                                                            484932.64953711757,
                                                                            38807.82024291725,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ο©ŪΧӡʣǾǳ˗ˈϚI',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԟʘҪɭŒǚѳʂÉ\x81+ƟΔ϶JɽѐŏʬģơXӸϞɗŷӯƔȥ»',
                                                    },
                                    },
                            {
                                        'name': ' ±ӶƻϚԮɤBɱΉКƮʄƒÂґĮϔ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7322915221917745846,
                                                                            -9061114901567706903,
                                                                            2171663979878796559,
                                                                            2579425094476969198,
                                                                            6458506813282568532,
                                                                            8980198106174519698,
                                                                            -2649136578237242823,
                                                                            -8474065709280887957,
                                                                            8072777899112390593,
                                                                            3338865756477552168,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΗĜӋŨїC0ƼӲ˰±ѨƖиҸϘºȅ¹ǵԑϊʡӇˢͽ\x95ԃ˙А',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȯƵǔmĩŕҮƍʄʝ\u0380Ŭ¦ȹ\u0381õŝӱӫŭɝάԇ¼вԊˮϨƬθ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3716378541840889127,
                                                    },
                                    },
                            {
                                        'name': 'ӯȵͷкϼЄŬЁʫЦ`',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:001013.452968:+0000',
                                                                            '20210413:001013.470302:+0000',
                                                                            '20210413:001013.485133:+0000',
                                                                            '20210413:001013.499880:+0000',
                                                                            '20210413:001013.623635:+0000',
                                                                            '20210413:001013.648759:+0000',
                                                                            '20210413:001013.671389:+0000',
                                                                            '20210413:001013.694427:+0000',
                                                                            '20210413:001013.716581:+0000',
                                                                            '20210413:001013.739840:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '¡ˊĀȟӷĺʃΞ4ɻΖɓ\x83\u0382ԇˮӸĽҖсǇƢʖD\x81Сȫˣ\x9dŮ',
                    'message': 'ΙƟƂŲǵӾċь°ȠȂΌǆӔ\x86ǔѬŰƲиʸүԞƁ˷ǈƁ"Ӄӿ',
                    'arguments': [
                            {
                                        'name': 'ńԪȈ˷cӤ˓ńÒσϙĆɟαƱϏ[ĎůƜĠЕ˳ӊвчbǇʑэ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            251865.56719739357,
                                                                            864915.3001864145,
                                                                            39200.62346278888,
                                                                            485348.3075081293,
                                                                            769402.420567654,
                                                                            410884.81706456986,
                                                                            461934.3834519468,
                                                                            281297.9287657227,
                                                                            825348.2661731404,
                                                                            879407.1789869699,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʄ\x94ōѷÖȋ¨хҐжθ\x95Ԇá\x80Ԋо˄Ȱ˥ĜӞ(ÂʋІ[őɆ˥',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -82019.3556281322,
                                                    },
                                    },
                            {
                                        'name': '҄ԞԌƔβƞӈƋĸщ˧ҢSǒʸшʞӁi{Гѧɍ5',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 100469.67531324882,
                                                    },
                                    },
                            {
                                        'name': "ɓҳΛ;ǉ\x8bōÁçǍԫҀǏıMKӿϩŭ'ѦƦϲ¥ÜǌȁâЙ",
                                        'value': {
                                                        '^': 'int',
                                                        '$': 564291859374661518,
                                                    },
                                    },
                            {
                                        'name': 'ͳ;Ƞ\x7fɃΜĈˇĨ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001014.445209:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϹӬ´ϯ%ǚŶӐКhÓſϙÓǞѢƻɇÄ%\x7fӱɔѷϛм',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '§Ԋү@rщϟϥ·Ӈ\x91RŽΊϒ¦ƣŦ±',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8273339981045423193,
                                                                            3368007088232282090,
                                                                            7435181230866692391,
                                                                            -7626652935509337738,
                                                                            2173078823299553569,
                                                                            5206042487852836558,
                                                                            4172945668413172075,
                                                                            7642138158543648068,
                                                                            -5774205728488449156,
                                                                            5428703836076970659,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѷ˾φ¸ʎԓÛӠԝԑuϰԚϞхүʇȨɭşѧпͰʆWƪĸ(˜I',
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
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': ')ʃD³ġǧ˜ČӒĹÁƷҾǝѡk!МБН\x7fŷƦɈ)ÝзȲѦʊ',
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
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˲˟ѰƧÚʩңҲ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ôңӌˍΣƾŦƆJüĉͺΤƺңԧͰúțϿưʎԘ˯гԕťВΦʛ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x9dľЦ\x84ɧȻҞ\x92Ġũ"ƻӢԅєƸ±ͽęѪІŅƙ˖ęΔ\x8aϔͼǼ',
                    'message': 'ƶÝøƠŧɸ<\x81+ѣǶŊƓҕδěȊŴҟĆ\x92Ӝ\x9e΄ʺϵϫɜҌҨ',
                    'arguments': [
                            {
                                        'name': 'ɇԧӹӬʤЖ0ϖϑʑïȮǾ˞ˑм',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -9116980528198341419,
                                                                            1617475561013724940,
                                                                            -7552677082902500249,
                                                                            -3903726833683457077,
                                                                            -2574296272447532266,
                                                                            1564948431642970848,
                                                                            948711391785740791,
                                                                            -2487839936417080448,
                                                                            -4347671640673359174,
                                                                            -1715357068276036909,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ə\x9bΉɟǀԆĴɁЦѰԉùáōξŝYǢʫԓˎ˄\x80ĵʇƦʨ\x8c:J',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:001015.933582:+0000',
                                                                            '20210413:001015.952895:+0000',
                                                                            '20210413:001015.974058:+0000',
                                                                            '20210413:001015.999417:+0000',
                                                                            '20210413:001016.019128:+0000',
                                                                            '20210413:001016.040705:+0000',
                                                                            '20210413:001016.060059:+0000',
                                                                            '20210413:001016.078316:+0000',
                                                                            '20210413:001016.097072:+0000',
                                                                            '20210413:001016.116160:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѾˏΘϟʉɯЯΫ˥Ǿ)ĢҕźͺïÊŶԉҰΤИɼ&ƌ˛Фō&2',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            837787.9946090141,
                                                                            467957.8644232602,
                                                                            724122.3754364168,
                                                                            652941.1582160335,
                                                                            370633.69220364175,
                                                                            227457.11504235736,
                                                                            457188.0709093263,
                                                                            526139.0431008856,
                                                                            274211.2652537743,
                                                                            327577.0919557896,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȱҁ\x9bι҆Çº\xa0Р<ͻѐδl˵țɱ˗КˊȠӟˏԥӈј',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            862144.1176913934,
                                                                            152661.53269506575,
                                                                            -24321.009188108146,
                                                                            259716.76993544993,
                                                                            258096.16535986075,
                                                                            115920.55725860904,
                                                                            740351.5650366908,
                                                                            -59571.409765741664,
                                                                            366299.6490390352,
                                                                            52781.58401195024,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ñ\x8bѷ҇Ӊӫ˪ÂŪԕÞ\x96²Ý˻ƢΦĸƷıЈ˛ţҪŨӗЎє',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ėĢįұӄ˔ƲĹƔÜ»˯ˬԈӔѳŕѫǔ˻ǱʋϦƀϓŐ¼ǵqө',
                                                    },
                                    },
                            {
                                        'name': 'ԭ\u038dӴҏȺϓĽҠ\x90',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001016.871103:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Μ˙\x95ϭӹЧŇԮ¸ˤ¥cҴʟȟȗrЍЖͲ\\ӵ^ó\u0380ǘι¡Ƚʹ',
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
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'PԗǦʣȀ˒ԁϦŮѸ·ЫέǍϳʓӜȸ\x87ƤȡʒǋłӬıÊ1',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001017.217427:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӏӨѱƗòɪυҧŦԆà3ɥͲ\x9dĥͷȇЕu',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -57372.28459997935,
                                                    },
                                    },
                            {
                                        'name': 'ё\x91˘ŗӭɮōhϭŊ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            166015.99466655584,
                                                                            499560.7032840677,
                                                                            608610.0096109917,
                                                                            67715.70233624897,
                                                                            40518.01859267219,
                                                                            889922.5733429283,
                                                                            920777.5113599634,
                                                                            913833.1075664867,
                                                                            896523.210207541,
                                                                            749439.4724356907,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '҈ΓƜĀɗµcȵʔͱϭˮǮ$й˱ǊaƿΙĢ˺ӥ˵ªԭЂһоˍ',
                    'message': 'ҙƀM½êϱϝÀкǰʐŃĝɍҲǋͼМ\x95ĎśˆκүĦíϘ²¥đ',
                    'arguments': [
                            {
                                        'name': 'ў_',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:001017.807974:+0000',
                                                                            '20210413:001017.824856:+0000',
                                                                            '20210413:001017.846019:+0000',
                                                                            '20210413:001017.860885:+0000',
                                                                            '20210413:001017.875997:+0000',
                                                                            '20210413:001017.892132:+0000',
                                                                            '20210413:001017.908638:+0000',
                                                                            '20210413:001017.924747:+0000',
                                                                            '20210413:001017.941247:+0000',
                                                                            '20210413:001017.959955:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x94PɫŮȐ϶ϘѳФūӧƒM\x8fƋ8ňĺϻQǌԃџÀƓɏãҫ˛ʹ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '·ȕʷƜҷ˽Ύзiϙžɯ²Ӛ˖ЩǶӔBœШҫŲРӘΈϩϛǬ˽',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 710833.2733860068,
                                                    },
                                    },
                            {
                                        'name': 'ρõӐҳsʁƶřДԡ˜ѽȳһҘҁĜьрГҧȻȸɷӶ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4196192337005676745,
                                                    },
                                    },
                            {
                                        'name': 'Ԛí,ȜӛϔÑƍϳӖH',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '+ΈɌēϺήΘϣŷӿқϖӱ\u038bэңџɲӁƂÉ¦ˤ:Ͱа\u03a2Ǟʪƿ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'βΧÔːżюыχ4ÝМҀēʸӤĽϖИȸʫPϻ҅ԐɬʡʗиŴӋ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 836846.1572447128,
                                                    },
                                    },
                            {
                                        'name': 'ɋԓʑļ·щ˄ȧʥˍȐиљεȡѐeъå÷Ӏ×Ɖ˵ЇҦʉ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'KǵӗωϵËøźКŨȖĭɱƮɍϙ¾˞PļhԎШυǛùѲ9\x95ƨ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3529002609391501354,
                                                    },
                                    },
                            {
                                        'name': 'ʹ:ʗɐìūϞϛ»ӺԌèȴЩ˥ҔϠԓϥ³ʫ\x98ѦσĒʔ˚ŠR¼',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 567122.1654070698,
                                                    },
                                    },
                            {
                                        'name': 'ȓȤ ɉ$·ҥЧӑӷΞӆòҵƽϣϩĘƞÑеŜʹҺцʈ˒˯ɧЖ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
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
                        ],
                },
                {
                    'catalog': '°ɯҎӘы0ԃĥϪήƎшñíϳϟÅǳѣϸǘΟВǁʆΉΏŌåӠ',
                    'message': 'ҼƊӶʧϲĔ˖°ǲƞŉɳɨ°\x91щӎӗεԖΡŹfɾ\u0380UƘЫÅɋ',
                    'arguments': [
                            {
                                        'name': 'ɌćʨїьùʒĒ3ɥԨêɥͶȚԝĀ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001019.143147:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ΙϤÞ˵ǪѿK\x90αŚ˷ƜͱƒƆƚˣɶʚтҪʉĵϙʶϹѓƚџ\x90',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԥưӗ1ΞõЕԬɃ·ΐƻԝҊ\u0382ȋЌσʔɕͱϛ˺ɗŽдȀӿηѝ',
                                                                            'ǃѷŞӥČÅìѲɏ҈ï{ȷ¿ӍѼАӥ½ɟҘϑĚžԐʟЙÂͼɮ',
                                                                            'ɗӤˠñӈǥϤȀώЫǙШǋƼϸʟ\x93БɗɨͷȌđˀэɃт\u0383Öȥ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĀЉԒăƳıʳͷɘïąɉÜΞПƿȧеӗ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001019.326356:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Й*łŘǨ«Įљ`ňʖĿúєΩ΄ˑŢԔÉˈęЉ¢εӧɧǠʏɨ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                                        'name': 'ǈĕ΅ҩтȺWͳεźȰ˭ρN˗ԅȭɛʝ?нʎ\x7fҬҲdΰ\xadҚң',
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
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƲfӋŠőŵɐкԟǰйǱăǶΈҎ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001019.940225:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƤѦ͵ōţéƨǮ8ßԌˊˣˮǀɋrʕɃƓԏ\x8fb',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ҷɪʏĩʧӍĮÙ\x9dЍǹ˫ŚċɳϺщłʥʖ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'QʮљлɬčǴÖιƃѾhɄŪɺȷʂŜĦʾʄҙƏ\x96љɾҳӰ¾ʌ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '²¹ʦǣ°\xadǓԢʯƲӮǿĦÅɷҵȢͻƾпԄĞɉ\x94ɃȁͲӻ\x94ǚ',
                                                    },
                                    },
                            {
                                        'name': 'ћ ԓΏǈÙȀвѮřǡĘˇʢьTJӎԨҏ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -336967337743657936,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɄȻԛěŦǜнʕˠΪçŒѶҍĀĚǈʒȩϺ\u038d®ÉђLĀЪб,ɴ',
                    'message': 'ӺȨǤӖϋѓǽЦԦФӪŎ|Ʃ";˫VήӂԜӵɂǂ µʘ°ȼϲ',
                    'arguments': [
                            {
                                        'name': 'ҩĒĆх#п˺óɥʿѢ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȏѲȑӗāιщšɌ˟ѷɝ"ҬӌҘĮЭӝǾƯʎӑɻΟπŹʲƎˏ',
                                                    },
                                    },
                            {
                                        'name': 'ӡŃŬɗ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'æÚ¦ǔǚӊΝơ>',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȪʹμøŅΕɯѽǶǩѱ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4580126491866256473,
                                                    },
                                    },
                            {
                                        'name': '!ӏƏȉԅ\x8a˴ǋˠ˖©ʳҌă΅ʝӁņңρˡҗăËбŀíɿЌм',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -997953658990912129,
                                                                            3259903006989263973,
                                                                            -6105943432695847406,
                                                                            -1246531327151387226,
                                                                            -7326321429319521035,
                                                                            -3108444616081980432,
                                                                            2041446296279658918,
                                                                            -2116960441555690980,
                                                                            5277664445481762082,
                                                                            -5118726749336868250,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӻΝΛ\x85БЫӳѶЋслÆÁХǐѬŒѽһϼнsȴϤƙɴѲƏѦƅ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210413:001021.181371:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϽҍЗ2ҵЙĨ͵\x84˃љӸ˓\x8cςžÛíϹΖó\x80ӛҦƉҢưԠӼǼ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            749303.9225352702,
                                                                            491089.2263427066,
                                                                            29436.627114528645,
                                                                            194708.72102286667,
                                                                            474659.617462007,
                                                                            701573.4039098823,
                                                                            755181.8431202187,
                                                                            629553.0721127653,
                                                                            455003.1705262059,
                                                                            73620.78435978442,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÐҋȖÚπEŃӽіӴӭɴҾψ\x84',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 368359.72684704873,
                                                    },
                                    },
                            {
                                        'name': 'ÁˌѤ]dзХ3',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5824344170418381717,
                                                                            -532019568120620848,
                                                                            4024472192407911326,
                                                                            -1634465187720766425,
                                                                            4427113679534830392,
                                                                            -7271853756891006569,
                                                                            4644278921192526465,
                                                                            4462736487707134921,
                                                                            -2174840252489740517,
                                                                            -4207245763591487325,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǟwȘ϶ìæôƱǲµӶВҬʦϡӿͿӷˆǧŃbҁȑϩԐΈģЦy',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԝ^Ҧã\x9bʋѩω2£\x81ĭ>nĹΞ¯ϓ¾ӹɇŇҮҊϓÊ\x8bºSͺ',
                    'message': 'Ąν;°ԎµԛǻѯԁȚͰЮ\x99яӉԩͲ\x94˘ψ¯źƟV˳ȾԠɷA',
                    'arguments': [
                            {
                                        'name': 'ȾԠaɂѨǮϷЕɢЫ˵ԕ\x95ŧɊȕɔǹ\x7fӫȫҎυʩ"ЮґțMƨ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ÙҤųTƯûҠѤȥ¶˼ǹʶͻԨ\x81ϹζǺŅcмÅĔ©ϒȒɵ˚Ǳ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'vѧΣ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4073032668209445635,
                                                                            -6977543359416874452,
                                                                            -5921407685130371689,
                                                                            2904444748315797470,
                                                                            -7118389018927400666,
                                                                            4487250465346549335,
                                                                            6896733951640603598,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¥Ӫͽ]ǎ3¼ԞȟԫТŉȔʲʕΞʽR˛ёΜkԧñÀȍư\u03a2ɡҫ',
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
                                        'name': 'ŶJˑũůϬӌԮ9ʼƪéсɏʅ`ƆʘϮ¸»',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210413:001022.561069:+0000',
                                                                            '20210413:001022.578368:+0000',
                                                                            '20210413:001022.595904:+0000',
                                                                            '20210413:001022.614739:+0000',
                                                                            '20210413:001022.631604:+0000',
                                                                            '20210413:001022.649135:+0000',
                                                                            '20210413:001022.666891:+0000',
                                                                            '20210413:001022.683793:+0000',
                                                                            '20210413:001022.701008:+0000',
                                                                            '20210413:001022.718046:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ł\x8d\\˲ЧƇѪ˖ęͻãÁƲá@ɣʕԖ¡ɘʚgСԩΗҷҗ˸DЭ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ӊ¯ǁι\x93ƌ\x8cԞԓɺŐҘ\x91ɽԣɀs˼$џŭҰħʅϱβӂ\x81ʀʎ',
                                                    },
                                    },
                            {
                                        'name': 'ӌƵ=Ѽ˒\u038dħ˙ж\xadϰϳʣ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1061426403257602470,
                                                                            -1814387347610656103,
                                                                            5676064294149706760,
                                                                            -1268026481156502765,
                                                                            -7686881660535883691,
                                                                            -5895043794119733421,
                                                                            5669552704245488448,
                                                                            -5955788834217936305,
                                                                            885260307101514363,
                                                                            -4306905824805275482,
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

            'identifier': 'ǙκҞzґ',

            'categories': [
                'network',
            ],

            'messages': [
                {
                    'catalog': 'Ųϑ',
                    'message': 'ˁ',
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
            'name': 'ҪɐΑҳЫļАчÌʲǇ8ɑԜύƉ҃lÔΫτΩĢǙǓŞ_ԩŏĆ',
            'error': {
                'identifier': 'НŪǈèȵ˄ȥ%˗Κ˷ԎίȤÎńƃYғѦI;˖ţ˰ӱԤĬƢˌ',
                'categories': [
                    'internal',
                    'internal',
                    'file',
                    'configuration',
                    'access-restriction',
                    'invalid-user-action',
                    'access-restriction',
                    'network',
                    'internal',
                    'internal',
                ],
                'source': '2ɋť\x9erҟƷ˘ˌďˁҨƘśôcͳͳЫ÷ͰȹϻLȫŰƢƋkÈ',
                'messages': [
                    {
                            'catalog': '±ѯ҇ɩΔɰĈĺǜ\x85Ξ9˙ċúʞѱǩρүǏ;ˡõ˜υѽ˃ǁW',
                            'message': '͵Қāůĸǈ(Τˁ10ϴ\x84ȼĈǋŘοԪɐηӲ-©нЅĨȜ.&',
                            'arguments': [
                                        {
                                                        'name': 'ɨ\x9dҫфϚ£ãǫë±ΡƎԡȈƌHҮɁċ˩Ɂ\x97пĹÃŀŒĞҧʺ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 363430.0170606765,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǑзȲĸõĈϛӘӶƠ˗ǭǰ\x92л',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɭˑϣŷӭмÛɔĞ҆ØƖʅŔ˗˭ė;ƛƓӵϫԒÒHȺñȪǩ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȍϷƁ˂Ә<ĠǏͲ˻Ӣ˻áҳӢ²ĭӟˤАѶўƥęƊҋǯԬÓδ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˧Ǜ;',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӝ\u0378ɱ\x7fҶǽWȃԎǼʲ˔ȑԍèƟφ÷',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˔æҢnϑ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЬӍΩʲˏӕÚϬӛƐЇȻɊ>ł¥ŏŪԁЏǠͶZƫˡZцʏҢǲ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 464212528681308354,
                                                                        },
                                                    },
                                        {
                                                        'name': '˴NΑ#Ϋ˱ƘχƫέñȄlȸ"<òƺҽӜǖHȸ4ƚ\x8cԢ§Ϙƕ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 747195.2428136643,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԂØ\u038b˼ŪѣɺҝͻƮřʶqƢ˖',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5934134040164277676,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ԋҕʋӄ%ǐǁɜɤΰӨƌƆ\x84ŗБȽLƐʓɯȷ\x81\x84ӬĐǚҭˤÄ',
                            'message': 'ʮŸ҈ΣǩϊыȹΖțƲњôЁҷ˺ΩŮψͰΌӉɃȻĝȈ\\ӈϲͷ',
                            'arguments': [
                                        {
                                                        'name': 'Êӄwԏƭ\u0379ϒԈϽϼҠ³ǧǦίĸƑԝόәȌЧвϕʙԟƮ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ћҢɬ³ʤǲ\x89ǂƟȯĻџвӝϗ҂ϬÅʡϛ]ЗАĕʀҘşǪƢА',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԁǩ҇ɭН\u0379ʪγ\x80ɹɹԋʅԮЎԘÛϕρӑѢDʄӌ϶ŨÂƠɉƼ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '҆ԁ\u038dǗƞȪʻѨĔȤǅŻͿ΅\x88҉ǂƒƀǪҖ«Ƅ͵ĬˆԒȰ5Ǐ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ψ˹ӢʨŏŤҸщĚԉÐȗAÖϊȽЌ˖dӒƸȳ˸ǚӬ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '>΅',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ýΛЭ¼ŸͻθӋĘˋȢƨƃĴ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5461921739111311690,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŞõӊԎ4ʰĞ\u038dҫɋёԊҿÿѨԒƿȗǪΨmƊƯĠ:Ԫӟȏ˄Ӯ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ļԃĔνԩœεǆЪ\x81ʓŁԅԉƉӗгуȼΌĞҥÞųғѵԨþʢ¡',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʇ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϐ¢ϓΣԏǄϻ<Єҹ˫Ӛ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 973924.1725596366,
                                                                        },
                                                    },
                                        {
                                                        'name': 'üţɊԙœĉӃАϮԎўʷŐ#Є',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ðԣкĵźǡʼʓ˲ưΪLɑʷΟʤ',
                            'message': 'вĖБƗǓʉɤ˙ЉԎʼҒfЮˍȐȨѫ˴;¿γőŸуʥ\x9cŗȋӋ',
                            'arguments': [
                                        {
                                                        'name': 'Łĺ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɳȷǧ&Ԁɮ4ѺµͶʺ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĸþ,',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɲ6fєʝʐıĉɍɕΈƷӏʢÂƲʑјҽҝSȧ×nԝƳҹӣͲû',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƟXӀΚӫ˄Ѱ¿ЄɺȁŻ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2751313396868873352,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': "ľǉęхӌԧQĖźȒìʿȮӲêԍǜŵƥÓŷҫǻžӞʫВ'Ѱɠ",
                            'message': 'ȍ÷˯ŬßǐŎ)ʝЬˮɇƟΆԎѦǺBӏɑv˅ӑ͵Φ\x9dÏΗ\x96˗',
                            'arguments': [
                                        {
                                                        'name': '\x94ъ҇ҳǡȾɳʡŋ˶КȇɁοʾͶөőȝʽȈҢˎɬΗƻϐϔĨɱ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ķ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɱ\x81ʕˣԨXɤήǠǨҟȍƕͺɕê\xa0nƁĄӅóѾɭǁńƆԟˤǸ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ĺїxɺ˩ĳԉҨʥ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϑϲƛҨ2јɮƕ\x81ԕɋθŇŠц_ɝҾм˯кǉ>˾Ɛː˛ʧяÁ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˵ѽӫY˛PӌԊӁг\x9dǣ˱εьđʟѕκ3ӋřдΨRƿѥȨˌ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɱȺʆӈ˹\u03837Ǣʊ»Ρ\x82Yǥ҂UрʼȇǦjȄǬ7ÆǝĀѭŇ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 75005.4303764196,
                                                                        },
                                                    },
                                        {
                                                        'name': '&ĦӁȽĂБмŪИŒҮэҧņ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 692143.5041886616,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʕėɟRˑ͵˶ГƆ¤ҕƽźĖ\u0379ӰԞʓ;ȑԂΞƷԍǄBԓʊΔЉ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7853647491751946573,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÚƯ~÷0ΟћΟ³ϡӲǥЎƫ_ķƟǼұƵɨҙƛϻϖƙѧȴ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʼӲӶƜ-ʵˌвˈǄҦԦѶλʱĸӛԭĸЦȗТҺ˺jΩȉɲƩȐ',
                            'message': 'ҌБ΄ԢÄåÒȌ˾\x9daŢʿśϷěҪф\x7făΩҼƭǜʤɋϖæūɣ',
                            'arguments': [
                                        {
                                                        'name': 'ӆXƓ:ϕǃҞΥƎѳ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȏɤːƬïɈҍōԟʮ\x89ΣHΟμbýҿé',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 418158.9112299125,
                                                                        },
                                                    },
                                        {
                                                        'name': '҄ðǉԬƒȚԘǕˣȩϩϩʨċΨԬϟʝ¸ԞџЈϩӏҰǒǩȑҰŀ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 638722.8231806242,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÚǬ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÓÍθ˞ǟЈķǕxԐ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'è÷҂Ŋ˥Ñ˜ΝŒ!Ö˖сȷˎ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ůûҒlҶӁpTϹǋȳĖˀѷ*RȊŌз˘Ōā!ȄȦ˟ΔȼÆТ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4655597661599591922,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӟ,ȮƻӋĀӎɘƳЧžѱ¯\x90Η˶ӻμҔʛʪ[\x9fŰ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ť\u038bдɮϛĭͲӍχOēΟϒf˚ɞɊÙϟ|ǹnΉʞìϪȔϖÑ6',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҽȎӔϨȯąɿΥĹ½fűτɺõϥҽfËЗԁ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƆŶϡϕԓŵêǁƕ#ǉ\x8dȉ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:001002.177891:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԅΙȂȼĭůԬԭʪFчΤϺσ\u0382Ɓ\x90tӠɻϲȚʕ5ԅʄѩ˳ʽû',
                            'message': 'ӭfʬƷƑήʂ@Ҟѽԟŵʸјҫʾ¾7ĻкϝjӾ˺\x88ЌЧǱ϶ҹ',
                            'arguments': [
                                        {
                                                        'name': 'Kªш%tíƷ͵ίͺǛ6ĞŁ!\x8cȯѼɦrхŘҶγɛûȻRƱϰ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЪǍԃȭҐӛƧĨөʠʨǧŇw¶ÄԠw҇Oǳ\u0381\x89ϠӐď˓Ԁ¶ӵ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӷԏB҇Ѹ<Ԍò\u038bɕКəͿǹYjŷ\x87ґӠ˝ơԃќŝHоɼ\x88Қ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǝΧĥđ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɇÎмɐÂƇϙ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϧґЖͽȱӱϺӮ-VӸЍЀцλüǅщyʲԪѺΆɁ\x7fǻψϾгο',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:001002.551234:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѳ\x9fɏðνϑɼϾȩHʟ&҂üӠŸΜ1ɛCEȋ¨Ԓųχô',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԁʐѓθȹ=ɬͻхč¾ǤȑǛ«Éȥʻ{',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 763285.43219931,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ż>ԑԪ˱Љ¹ƯНůđԉ\x9eɗɾʊЃќͻ¯ÙӆÙʐÓßʤҦШƺ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '1¡ɭ˻\x91ӤЖϕvДƻ\xa0βƧ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 935087.9959331992,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƨУřŷӊ\x93źЃɣʪɢҠ³ʀŊˤ\u0381ϩ³¸ǞϜƒƧÖ\x89\u038dϢɊϫ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'СΕʙԆζ\x9a´\x94ɖfӃř\x91ƱоӄȾƫʝÝԑȇ½ʈ͵ʴőɚ˛ž',
                            'message': 'ɜԈƂŘġ\x9aΫ\x80νϣЖΪʖ˔ʇςҎǙ@˯ćïӛPˣưÿϷҚm',
                            'arguments': [
                                        {
                                                        'name': 'қ˻Җ´ЂƼƘԇ=ɩВŴ\u0380ќŐÖԊɻʲÕАĹĝMŏƀŴӟςķ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3502549098470969790,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԉ¢ĻҢǓɌŁӂőчӭЂѝɳnЖĬˢǲǓOӣРEǎIǺӖäƣ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'âѴƴɶɉȍɧÃǏŔ´àDĹϱÏȩñÛҗǳƄΘ͵7ʅϞɲѕѨ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Gѷ˥',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ťO˗ʢ\x8cűɕ\x87˘ƨ>ɝΉȌƨÐȦ͵\x92ӒǥįϋӨǑ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:001003.206467:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĔˍԋǮŲ@ɩ\x96ӏxN\x9dʸӘϣ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ſǨ˃ʇȹϐȇϦƥɘЊÌŔѽƼkъùͶɗ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "%İ'ƺǓĈġ¶\x85ȾōŀĹчĮŝѴ9ϫьɝĝӧUͼ",
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1262961883900034877,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ċXѭĪˍӅЀ£ԧҮяӿDˇ˯\x8aΆ˘Ⱥ¨wJήƱɡ·šέЭǌ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ưxŴΜ˴Πӳ6ԉ\u03a2ʭ¡ɔʊѠÏҐŁѷɩn\x82áуʉҽͳϏǍğ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Đǿω˷à҈ȢǡÌɣÚˈǦ\x93ıǈί˨ħÐȵ\x8eƶԑæɍϯџӮɒ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ˉ϶ͳӈ_ĥȦӗөԛɕRϨňôȢÆϐ˄϶\x90ɞ˝ĘƼȍҋ\x88Ūя',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȉ˛ҽ҂ǿӡз`ËĽǯˈŠɺ¥ʯŗȣ\x93˷ѧȅӻҥÉɎǺҶԇϧ',
                            'message': 'ʬМ"ǲҋɛҖŘǰұҗʿÀǇɻðśœčѱώƄѴƿӦԍʶˌЇѕ',
                            'arguments': [
                                        {
                                                        'name': 'Ѳ\x9fFӔǁΝҷͶЏԔёϴǹϻѮӣʅПĪÐ"ϺЧģћжѢǂʻ˯',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': ']Ħ×ӌāƢʸɹФđϐĵɛӃіѶχάԔңɍʃƮӆűКWjҫΦ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǀ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʽġɞ ƕƽȚȊȭ\u038bɻIxϿԧĆǾçˉԩͻ\x9eǇʹʰƴðâłƛ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ª.İƔßжǭͺʶԨЫρ\x8cRΙњċѳͽsrǽǾ\x94Ȃ\x8d˭ǌӾα',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѐ<ьıȟѓ˫ϼͻў˵ɢŠưŤԁі˨ћɺ·ɥӬȸĸлΕѫǼN',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'κƓ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x94ҿƇӫƳϐ\u0380ҙ˒Ģʃ³²ðΦϓƯ\x8cG/ѠȁϞÿǖMЍ˞ϗ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 847818.8679481748,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʢɈҥŁƼҊҰҏȦ΄ʺɡʩȧʱ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210413:001004.365965:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԥҭϾŊʢԡ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 762776.2713407857,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0378ӣ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4417345968247643299,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƤȀыд:×΄Џ©×ηˡӃ(ʚВЬǝЧЊɓϾȎ\x82˽ɔƂȷŎ=',
                            'message': 'ϷĭÏʓÕÐʺɤԏɁ/,ӑе ɿƏˁ÷ǺmįˇǴљóɥѭҥҜ',
                            'arguments': [
                                        {
                                                        'name': '˲ԛ>ҬӂϋӍƔĪЏɐyцn˴ΠS}',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȚΛĝéɬЖƦĜġӕϭʜěɅҏǽ˳ϖʲN˃ГѿɆřл*ˎ§5',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 88732.34917836325,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x90ԀƓÚϽЗɯ\x8dɂҤˠŕөǧfŦÌԦäƼƠƌҚњƣɐӬċЗ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4583968540306800406,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȓʪʹқЍìH·ӏɁƇϫÀͼňøʩӺ#Ӓ8әÎÛʁřЃǺđЇ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1456510877838845202,
                                                                        },
                                                    },
                                        {
                                                        'name': '«ȣԌӡԒɨȃћŜƣҿ˟шзҫόнÛԙʄÔæÁOԇϷȲΤ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ţɜΎÝfьɳÕиɹԔđ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӰǃÚƐԘƉ·xƨɫÜαǇƽϔĨҹΏƍА5čŠСҤɶ»\x8a˙Ȳ',
                            'message': 'ĜӁ\x9fόʵΡ\x8fӹƭ¶uҚĔԋɴЋąӷƷǟpПȯȅnĎԤśʔv',
                            'arguments': [
                                        {
                                                        'name': 'ϻūπ@ҾԀüǯ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'GƱˉҸȺÕƐ÷ӄς\x90Һǉʕ˙ĊƳƪ\u0382ҠǟřȒІž¦ğǎGҢ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'χóȀƵǱĠþǔψЅ«ӿԪ@×',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΕњȜçНҩѭƔԌńtΤƘԜɑǝԥѯͲΎ×ƅșјˀҦH\x84\x95',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĤˌŒą˼Ӻ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8568521907099056848,
                                                                        },
                                                    },
                                        {
                                                        'name': '&\x8fȀϡ\u038bʽˋȘŢϷ7Ѐq\x99>0φǍӇɐȱœAęɿοʳȣʳы',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӕԝːҪ˾ĳȽɂʿԅˡˇ8Ǥō#˨1ȉϿŪǯțɯƹԘ\x97ԫЍ¿',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɗˇæ<ьđːɷΔѺɨзӘļӜϱòԧҝΜ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӿΚƠӴ7ćĿƗÇɲEԪъќȱк',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 213355.15567633684,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԓЬʻ\x8dҥ\u038bӷйϒÌɿç˸\x9aǢЉҷjʊŗҶӅƯғʲӖԩϓӛ\x87',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4845076991401478564,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǹǬӧѠÐhĶŌ\x97˓ЮƻҕԒ¬ˎϒˬ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
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

            'name': 'ØĹҢ',

            'error': {
                'identifier': 'ʡÈzԆϨ',
                'categories': [
                    'access-restriction',
                ],
                'messages': [
                    {
                            'catalog': 'ãŦ',
                            'message': 'Ə',
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
            'name': 'эmЅԫʿ}ǓТƲҩƨҽɆӼΎτƵӰӇԢâĊʲłҦҁˀ',
            'version': [
                -250456221386765741,
                -6553243925469278993,
                -9033110024582630127,
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ÞƝԙ',

            'version': [
                -9208219698890575824,
                -1167966430408462787,
                -6049368508202780099,
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
            'event_id': 'Ư҃ɇԀ˳ϒͳұɁ ЄĳӨԏÉ˕τǵǞԊǘТ˟ȇɦǜԊ˰ҰЖ',
            'target_id': 'ξϐÞŒΘ~ʑҩʾĪ˃:ħƈфъǀǠǎɨɘzIʜȽɛřbĸɲ',
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
                    'event_id': '˅jҚƱ\x8bѩюĨϨιŮƀјŋӌӄ\x8dϛҁɞҒΧΎţƱϼǬǛʯˀ',
                    'target_id': 'ԞγȼԟΛɤôąӍϊѮ˹ɬÈˣǞͰμŞˮΫɮƑвʶԧƐʉтΏ',
                },
                {
                    'event_id': 'Ōŵǭ˓ϴʞѩҠƂ¦\x81ȝtєўğ϶ъă/ԐʻłĚƀϒÂòǅˀ',
                    'target_id': 'ɚĿαǇŌũϖİ_ѡѵӡΥÓġ͵ŞØȋĕ҇92ѡʧɤχũ$ő',
                },
                {
                    'event_id': 'jǴƵȹη˲4ÉʑӖȔҺȥЧΛΙoƄͺʀӠʑҡщĤęČ²\x83ȸ',
                    'target_id': '\u038d˲ƋʜӵŲ˃ƚ¡ƱϡϢӓ˖Π5ӴԢΙɒ~ťîƠ7ύɴǴđ͵',
                },
                {
                    'event_id': 'ƽŽ(ҾŧЏțοҦӯϜȟʵˣԜʤϿʫѿŒϐԟԖӍĶ˚ĲӶϧǂ',
                    'target_id': 'ôϽ҃οӪ\x8cҾŹӍƤҖ\x9dȍғŎͺʳŒеōѨʴǸcԭÞǤΝ0ƞ',
                },
                {
                    'event_id': 'ѩĬĹқ\x86˚Κ!%χĭӸЪʣЕһӃ*ЛѶ˼Ğ\x7fήԁɃύgͿȰ',
                    'target_id': 'ѹŏ¨\x99ǥǙτζԡĎЂѯvЩӳĠίюИЧƎΡ8ԕѡŗɆҸǳΪ',
                },
                {
                    'event_id': '˔ИɠѠϒʙҕïӭȲɫțȔΘЎ˥Ǚ(¼,ǏǼҀӒͷϮʛЅԟѝ',
                    'target_id': 'ΎƸ˶ͼΆΙҢ§ǯ\u038dҋіҞɡȍǏԤĀÚьƈɋ]ʖfȢʦҌԔɠ',
                },
                {
                    'event_id': 'ˠȤоĹЇ˪ҘȕĨϨMÒȌҲƇЦğҭ˼ŜҤŅӋˀҷ;тϑұϗ',
                    'target_id': 'ю˭ѾԀϮĀώʙЄƊƷǰɒŋÎΩÓƶѷԕ^ɉҳìȢŒȗȽѽ˓',
                },
                {
                    'event_id': '¹ӣШмʋŦιҨӥɟŞǄƂ1hǒ\x9c$ԜǑӍĤ˙Ǳȥеřɖӹ#',
                    'target_id': 'Ȕёϡkć)ĝÛОϜʀӜϚɚ\\fëďʬ\x90Ҹ҂ԗѵĖӧŔƣνώ',
                },
                {
                    'event_id': 'ˉŻķеϭщЫ\x92˼ϥQԙʣЕFԓĎʛ\u038dѵƇлƣ?џԩÌǾӁĽ',
                    'target_id': 'Ҷ˻VԡӨ!ɁˠɮʏǹǠŻÞлʱҠ˗ԎĄȅж£ͷɦÌʶбӓ\x9f',
                },
                {
                    'event_id': 'ŏʅƌŎǰԐ˓ƨS\x84ӫŧqǧΐӯĺ˅Ɗӧјҗɪҥýǋϑ\x85Ӊɨ',
                    'target_id': 'Єĭ˻÷ŉҸҊұɵ\x94œϑȬa˄ɧѓ\x95ȊϠWѝХѸϪʢҏɫĪˠ',
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
                    'event_id': 'ԋӛĿŜėùϰӉӚˎʤҗ˹ǕĤËʗӠȆĹΫɈŃҖȢͼПˑ\x8aƇ',
                    'target_id': 'ǽΤ=ĎˁԞԞȤʗԡǗƱƑŁ҄+ƒlφˠЫʫň\u0382ѺǁɟΞΝʗ',
                },
                {
                    'event_id': 'ʋϲɬǄԦӽɻЈ´Ǻȥџ/ɪʋ˷ОԦԫŉǪҝƗõʝԮşȭ҈ʡ',
                    'target_id': 'Ғȁξ\x8bˉȯĹѾ\x99ȶɒ˷ǟʹήʟӁϓȀeȯϓɌũĞˉƠȚșŅ',
                },
                {
                    'event_id': 'ƭƩӖШɫΖϵΡѽĚwêĘ˥ŒÙRφҘ$ʉʙԡÄΟӎśǶʺȿ',
                    'target_id': 'ĩŅӷЖΕЃ/ͷїыʕΤəj&&Ѳһʅϛ\x9aȎ\x81ѓ˗ŠȐҖΰæ',
                },
                {
                    'event_id': "ѻǖ³ξńГSŀbŜŏcŬʣΉӋʩάǯйԋӉҴԛʎϼʼ'9ȿ",
                    'target_id': 'ΌӿXÁҨˀ˺ӷ҇ǏίоԍġСДѥ˱Ńа˷ҭιɶŌʯηʹσҖ',
                },
                {
                    'event_id': '˻ǭèϜʽϬͻ҉˔ɸЭ˚¯ΥōSӘњѰмЃԓƢʇԜǛèŋÍƗ',
                    'target_id': 'άƸ˻ΆʥěʈſŰЪŎ˝j/ϥɕīāѡɨÐξǿɓˀˮжőʶ˻',
                },
                {
                    'event_id': 'ėI;ȾǤǓϳͰǹˏøЖʋÉûǵӇӤԐǖSļĥĕŅǚƻƧŔӷ',
                    'target_id': 'ˡN`s;ĨȭʖÕƴƇsƑ{¸ÉҟϘĦðźӝԣЇԤ6εɂŔî',
                },
                {
                    'event_id': 'φҼўʂŧÃòόZʧ˗ȔϦҟɺ\x9c\x9d\\ʙЀеάûΙЩBʌАԆщ',
                    'target_id': 'ȿŞʺҫГѐľë\x9dȖŦųĪЇz«ʱɰәɪpÞ҉J\u038bӁȉĸΤ$',
                },
                {
                    'event_id': 'ӛÍЂʷґĻxǧӪІғѺƦÀƿʴΊɂƌĘƴ\x85ϫΗ)ӯÍӳ',
                    'target_id': 'Ϣнǈ˙ɭžбKnCÜҧˋҤʝɟǯoЃԟƂԨəŒѾİ˚ӜǨƣ',
                },
                {
                    'event_id': 'ϒӧñԪśƎ˼ȜоʬŽqǩ¥Ǣʑл²˛ˑĽéc҆MųѱŇ¹φ',
                    'target_id': '\x8cb˅ϠѣʖȷƈĴэƵʧVЛӺ\x90ħɿμЛËѹӺƐϰãĨųƱт',
                },
                {
                    'event_id': '\u038bōϹ˱ҫ©ƣřfԅ}ɽɮōɣɮɕ;ÃŗǒӤÏќȘӜȚDȔ˟',
                    'target_id': '\x83ƜĬԡ½ҍȓͳƤƳ˻øƠ\x83ŭɍΤNѣʜtӧǾňˮoÈĹĽȃ',
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
            'name': 'ҼϞʁǷӲҪϟ˵ʦнǃδЈԔӄčä˘\u0381ʉʔäȵĲXώӣ҉ԡԦ',
            'version': [
                -7441965706719856213,
                -103892867132528506,
                -930494020715254022,
            ],
            'about': 'ԕ\x97ОԧοūѽΊԎǏШҲ˒ўӄ5ʼɞƜȀ˔μũˈҍԮ˧҅ζƣ',
            'description': 'āǙőȝʖšʠǈӂΐķԠå¡ƔÒǦъӘŔEɳΨЩПсоE1ѵ',
            'authors': [
                'ĨΤӠӦ\x9aӢǷʈɏ+k˲ĬĄЅʃӘϞɕѬʒŜlӉÒԩ\u03a2ӂӹ˙',
                'ɱ\u0383ȕϕ#йü1ĆˣҟˮЫȫӎԔΣÀîŕ_ʷǜι¨ψƌVΨЖ',
                'ˡȠЇӱɶӇȖȊʓͳъȟϑŝʎʛΉĹӷȚԠȌ\x96ƂʙҸӕǲ=\x91',
                'űԛӨǓʨ˶Į˥дҀӪ˧ɫ΅ӺÙїǚ¯ӱʐőɝ\x8cɋ',
                'ʋμԞ\x8aЇǪшƦԧƑʴ¯ˈӼζÚԕԩϝԒɀЯͽăӊ',
                'ƍϓҮĴ/йѢʷƟҁ˸˗ˤϵk҂ƐсμÑԌʌˋʆˁɑIŨɤ\x99',
                'ɂƝɌΰţҡѾцӲ˓ȤӚƖʤʛԊ˥&҈ŦȧƫŊǊñŅʀуӛɡ',
                '¤Ʀʆ/ʻŢѻɉǤĞƙϔӇŀɇ҃ʠäѥ:ѯ˹¯įÎĒѾȲюĤ',
                'ѼȸѐТņѣҠƨя˫ӏ·ŹŸǴ6ɍрƕω¸вϓьʏūɸͶҚG',
                '·ǰɁЉэѶɨPʢНǌó҃ȬҢǈˋěƅΛӎǕʮѡƸ;ǋԁȸĆ',
            ],
            'licenses': [
                'ƆҦ˗ķԇҊϭӎҵÍԤƝƪϡ¢җűςœӇɟΡ@ҽĝů˦ʉɩˣ',
                'ɗƒ]Ìυʄē¿ƷȽԀSъ˷ԆԋǐÂНüġϖĊЈϯ±ŽʘРҔ',
                '\x95ž´Ʌŷɸςӎòшè˺Ǜίԧ+cԠƸӞi',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Īƥŭ',

            'version': [
                -8998833180445014645,
                -6250741493166651217,
                -310161233710963330,
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
                    'name': 'ʻϓӋūӪ\u038dͳľhŖԟʿţ\x84ҩŲǆ˳ҔėԅƮАȿԠΕ3λɐź',
                    'version': [
                            -7199599420066930471,
                            -2171121395498967966,
                            -6979543792122207219,
                        ],
                    'about': 'ɝԃɃɠÜƲˉЁЋϳwǎůń˵]ǍÑƢӤԢν¾С˫ŒӲŴҠÕ',
                    'description': "ƍϪȁѵ˄Ҥ˫©O@VvŁǬӲΈύ'ĵȠ°Ù_Ы\x9a[ʄ\x98ϧŃ",
                    'authors': [
                            'ԢʃPĩŤɱĜȵĔҧ:ϔΑҜӋșыıʈЯУьлʻŽźʋϣÓ\x88',
                            'ф˸ъɲHҕхĶЮǅǧѿζȚӃÿʢшȋБЭѕɁђ˝Ń*˖Ϫń',
                            '˷җԉ¬Iȟ˄Ҋ˸űǰȺǸȞˮөҠͽ]ȂʆɁ˧ӍØəęЍŧ˛',
                            'ˋҺ\x9aŷ©ϫʻ×ÜӯɉљΕӬ\x85ÓΎȸѵњ<ʄəƑģ\x8aԙǙҿ¯',
                            'ºΣΧγѯĲîēëĝ˄ԌgҐʘɊҢƪɘƹȷЃˢәůϮΙɀԊ\x8d',
                            'ȍůѡΰɊʍhЖǼˇѴR˒\xa0ӑΎҖɇʰûϦǜ˹ɁpӝÐȢ˻ã',
                            'ЍʎġԧӆƒǒįԒΓʏø\xa0țʑД%ɞϣ¯ĕȿ8ΪňΣΑ˓ÿȡ',
                            "'1ʱ¼ǝgƬѯԡǙņϚӊ=ħӴӡӾǕÙ®șɷǉȂIФaʂĭ",
                            'ҎĽέΪƐàϿ\x8aȦǔ\x9bºЫɣŊʴıԞľǋH&ԌǂB',
                            'ҝυ˥ɠˇϝώч{ƱэßӪԧʲTƿmȔԆɭϠЊѰц͵ʵԏZμ',
                        ],
                    'licenses': [
                        ],
                },
                {
                    'name': '\x95@ǮΚӠͲȧĩŨѕԨԎϛĘλӖȶɌŬϵ˕ǻºъʠŲӥǺЭƷ',
                    'version': [
                            -157765845142745352,
                            -7475152843958696604,
                            -2879850038055384989,
                        ],
                    'about': 'ęƞљҩ\u038dȬȢȷÞҦˏȹϴҊΚƼˮŶƄɄϵ·ԊӾƊƚƷӧˮŗ',
                    'description': 'ҴȈίĺȂԟĹϚіΆϷȄNԀ\x83ŀǗςφ°Қķǚб¡\x92\x91ǂŷɊ',
                    'authors': [
                            'ҥДʊшǩҜϸ˅\u0381ǘŀϐүȾƺ\x83ŖɥϾԨìΤǢɈŔŰ϶Нŵʱ',
                            "ĺпƱ˦ȇΗƭɁˌĪҸ¹ÓϫīҏάŮĉνō˄ǛŝΑȄ\x8c'ĳp",
                            'ϐWǱǩÌǌч\x81ġł\x8bhīϬęҁö˲ϹҔɣ\u0382ɍʭϝԪԦĩÌΪ',
                            'qʐӶĽƣN¨γϨƢɅЫDÏ&Ȅ',
                            '¨ċāϡĺиѥԝϼɒϐЀĸϚªʉŪѣ˶ԘǕíԑ҂үö˨&ȹΚ',
                            'ҎЎ˱ǗȹɽэҿǼƍȺʮӳǞϤ҆ʷɓӇŐɬ|ɸ,φˤǑƲŜɝ',
                            '%ήIʙσˤ˓ϙ˪ˣѸãŢѺǠˡȒɜǢôơǠϼƤņžąȗʵԞ',
                            'Ӛ\x91ňγÕЖƓmʗД˺gȧæºɠírэŐ§\u03a2ʏЌ\x8cҪǆԄċȼ',
                            'ʧϙǒŒӪũϾȏʧĞӍAƨǕƘˎȂ҆ϵϮɮːӥϫƿđLɋӾž',
                            'ɖϡїӿ\u0379ɱũ8ӒŎрђsͻʗ҈ɖƯƯӭķЗѕ˜ӲȰӫǛ7ƃ',
                        ],
                    'licenses': [
                            'ë\x87ӖŢӶρƏS¤ѢѽҠȎŚμʘ\x91ЂҶʯýҦ\u0381ȗ¹ưβĴǶŗ',
                            'Ǭә\u03a2QǉӸіϾѵƵЯЗǝǐȚƉԦ˕ɘΚżúˋʏȪҫҬӐʰŶ',
                            'ʫȹΒԪӔӷʝҙΠïԖҘ\\ϭƎԃǆȧΝűŴ΄ʏԧϺπÅǓǯǏ',
                            'уηʣʾ|ыɔϿԐˡͷ¼ʂϫǬȖˁʮ[β·\x92ƌӬϝϱĔ˄ЖÉ',
                            'ê˨жʕ˜ˊǳɒŔ+ßŤʈǨɣѠ˦иʆʺнĘіƃƢ\x86ƹRĩϤ',
                            'âϥɞȩaԡҎә\x8cÃˋâҙʭÜɓе£ȃśƥӂРƀɟӃӹђ˵ˀ',
                        ],
                },
                {
                    'name': 'рúҴϪʉεǶԁěѵȑɬÌȇ=ϪNԂӆϘŗƉԄǻƝ˝ϖn¬ӭ',
                    'version': [
                            -1115449341744764532,
                            -7249650491237690779,
                            -8731666699177926197,
                        ],
                    'about': 'ǗʭÁηЪĒǽɇLċʳӋƧŅӚò҈ʁвϿɯ±Ę\x9c\x87Ƨǋј',
                    'description': 'ǊϔԚAÅΓǮɯȺ)έƭϨŽ\x89Ƭ~ӟқϑӽѳšԔʦʦǷФIͶ',
                    'authors': [
                            'Rķ\xa0ȟȐŁʚӅ˽˘ίÝϣÇʹƫѝͷґ˻ĮAëûpŔgыңİ',
                            'ǆřatžȲWИėǱȜǒɤΤϒӡԫœȫҴѱϻʸƹ˜ԨӅȉʉł',
                            'ǋёԡĢϬԎɩεòӱĮӉ˞ƄȀ6ϋ\xadūӽɫϟϒҧԠФρʄҞʜ',
                            '˸˴ũā%ʗљԑѮǬ4ҋ3êԘӘįӥϫʿΟŁį\u0379ĈĝɫӐԒʥ',
                            'ĘƁͽѐöОӏˇʚçҕǕϼ?ԜƼnľӆŶÁ˧ĐǚПμԖ£\x89Ѽ',
                            'àƄ%Ǖƫˆ˱ԬӠ7ċȒǾҎȦîÚΓӺú\x97øΜνƹƕΥƺԏх',
                            'ӎaӛˣы\x94ɒͿȝðӎǵ_ȇǓ˒ɠ϶ѬϼŜҩʄΤϬ҂_ǯһã',
                            'őũý4ӶΣ\x8bЪϲЬ\x99ƕĉ˄ǈɅӡ҈τǝѕʛǡöɁǴ҅ҠĊn',
                            'ǇώЃƤԧJƸǙžҫ¹ŚgѪņƮɘЋφǾƍp(ìɰЧоϒԍɶ',
                            '˸ўƃéĒ·»Ƽиѻҋȝʇέq\u03a2ψƠʿɜoÜӝ҃Ϭ\x86X:ϊð',
                        ],
                    'licenses': [
                            'ԟĺġͷͼͱӲҪҤȂҏɆʰʅŁȲόȔĒТŇϕ˂˲ÑǶЌҎľÌ',
                            'Мù˲˧ʀʙ\x94?ώʲºłăMӮçȽЫ\x94ƫɢǥϖҗɎʩƒʣŻɫ',
                            'ΒƶɯΘӣßªǉԁƾ@\x87ҨўƟӻѸʣҳÉԦҦҝԘPāȵ˲\x9aQ',
                            'ɖ\x89ƈԒƐϓӪʗϸҥȾgѪɿˀњʨ\x87¼\x93ϱϖϓɷǱɵãΨѪƝ',
                            'ɊǮԒʧΰԈǄϱʬƛȕηӬĴ¹ʫΠһǶƘ´ɶʥǴэ#ӣǵёΉ',
                            'ԄZɷñ¶ӉȞДԕǦ\x83ҨѶϱχEʂчʯåĸŷ˭ϺǞŷɭǭƓԃ',
                            'ӎƸɳ³ɓίԅѐԥĹ˩®$ȂʭɢĐΕæŬWӳў҇εҞϘӷƐΓ',
                            'oѵŞéҡˉ\x8f[Ȍ¾ϐǆʪʀɑ˻҅aÃƚǜѺɼ·ѹғƁҮA;',
                        ],
                },
                {
                    'name': 'ȜλӉśěƈϥʯӥ¿ȮǹϘɖƕ-ϾϬȭ\x9eϏƇʕ)Ҁȝ:ʍȈĎ',
                    'version': [
                            -7825064881146433272,
                            -6399990834020106606,
                            -1435563032818177983,
                        ],
                    'about': '²ԔȶК҂±˘Шē¨\x86ĒԊĵŦԩ\x82ŶĪıƒԣ£˼ǙɦԍЦŪҒ',
                    'description': 'ΦǦԈĖġΟĸѩ1ɵ΅ϜΞƍ*ɫɖԕϵͿʨ%ԕ҉Ŀřƥш«Μ',
                    'authors': [
                            'őE~ǿԟΦEƁ\x95ƽNɣѧǑσ\x96˺Ϗ]ŠԅҋɣȊυҵΌ\u0380\x83Ԍ',
                            'Ʉˌ\x9cƀŭːmӳĎĻҲʢ˄ѓdi˄Sρ\x9eʩl҂ȡ#ɨƽ\u0382ɭƈ',
                            'ЍЯ˳ȥҏȱņŏɣ˄',
                            'ƃˏWǆʊƏˠͲıǧ~ԒƾƊжЋƄLǢɵΗƍԀiѱӲʠØƛǃ',
                            'Ҋ\xa0ɼо\x8eΩțцSΆȮŶΊ˼åԁЃϳӝõʦҡӀ\x88ÎȜǑϭƑϩ',
                            'ӆϱуτɏɓĿǍAȷ¦ɞhшлŉΝȍӕ˞(ǟ˦XȆćх\x9cōɦ',
                            'ГԏƄԝƽŀϒЗɍӨ˛zӂǭ|Ѝ·Ԧϧé¹ԥxÞѼӰʑƇĉɇ',
                            'ʦˑkӺԑ˼ƒ\x99ƕɪŰ©¯χÒҧȥˢӄʭʁǏΞ×ў\x83ȘʍŎх',
                            'ȠӶmƚʞʐƬĪʃɾηӻjѰ*˙Ɣʀeȇȣԕ˱ǲǍ6ȵťӹБ',
                            'čɾȌʹ\x83ÆϷ9ρʒƞУȱӤȲɩňŁŊžЀĚȹ=nAȬ³ɡh',
                        ],
                    'licenses': [
                            'Ӿ˪Å\x8eΖΤňҀѾ',
                            'џŽa¸ǘşŉһŨǦҳŸ˞ъϮŦԐƽҚɷŮ˰ǎʹʩҀġ4ɬ҈',
                            'Ϸǿҹźȩ˃ĢԪ\x98ʯƥÎʸӻƮǐMŏϷʴϟƳĝϟĖǡ\x8fǷȓǄ',
                            'Ǘӵ\xadҧTðʕƒȎϧ˦ʱԟɀԧ˶dͰǝ>^ñѣÀωΗҴ9Ѣμ',
                            'PȓłӿÛXɵϝ^ɟƅƍБϓxĬѮЄҊÅϱҎԪθȣѠǪĢѢį',
                            'ʣҲǾјП9ЛӽԭəΦ;Ƃ҆ķ҄тʓȡнʬǀıŬǞԃӇΩïϱ',
                            'ŶȳĉŁЭϤ˨ԍλī\x8c\x99ʟҹЊx©ќ\x85řϾžäŦ^оĻƀ˫\x92',
                        ],
                },
                {
                    'name': '\x9d˥ƝƄіɦξʡˀсCϡϷɜȦԡɧΦЗӱrͻӏҤͰžc\x85´ʦ',
                    'version': [
                            -2758128962430682262,
                            -258291634858178857,
                            -1277834977523931408,
                        ],
                    'about': 'ĻϼŲʿ˥\u0381ʉþʃȓŭҴ˾-ҁvɻϊ˷Ȓͻ/>΄ǥǹƺƯȅϸ',
                    'description': 'ΔȘ¬\u0383ŕØ\x86ӤŃӔŋѯGңŊ/ɋˆҸϒҟGѭĽǈѳɅӌ\x91ɖ',
                    'authors': [
                            'ƥϠϺŮ\x90įЕËǄŧԐΆſ±ϖѩ·ʹǼ\u0379ƿòϱǓƢϢ\xadŲȅȊ',
                            'ύ\x93љłӁϘ\x96mңПȬˊӰ\x9fϟʜԤʷ#ťƾǮɥŇêˮȿÈı\x90',
                            'ĐѓǴÎ?˰ʵ>*ԬlΜƞǂӫԖǬB·ǦřӸȝθ',
                            'Oӈ,ęˠ²ȇʾÜÕƎǬќk˧nYɗǡ˘ɚHгÂʑĿƲФѥʵ',
                            'ԭ˥!ѼӰ\x89·ʖ§ӺƤǓɇ8ɆϓŀƽУЪ\u0378ԨѧĮȡРùƀ°ӥ',
                            'ŶȐˎς;ʅǹĆЙϨ°ƘҜɱʹҖɄӠȸǯĐ ŹRȸƑȤ[Ѷï',
                            'ĮԘŗˤȋӿƔҁ\x8e©SӷȿʊƂŜϝТԨǓˍПGǪ|WΚίǳԆ',
                            'ʏʧȌī8ʥҺӃʽ·˱ʞǹԬМǻ#źïȳԋѐq\x99Ҽʩ ˆԔ\x89',
                            'ÛӰƢԀņˍƕ\x95ӆƜЏȯԙƜиΜǚеɰԤŽȼËKӮòŃӀ',
                            'Ћɒȋī\x8fԖϗЗ҆ũɜі;æʼǴǎǕͶ˽\x98ϯǠŪԍϐůNθȁ',
                        ],
                    'licenses': [
                            'ȲϳźҀӮǙƫ˞ǲÔή\u0382˸GɆ˯4¯ԄԆɋԫäȅɟιʲԎQԔ',
                            'ϛƆÔʂū)ɩѠšͼΜХШЗʦgӱȊԟԘɪǜʃҸχŸJX\x8eʆ',
                            'ːȰɥ)ѷͱē\x7fҙƞҀϸRӈҟŢƴĻŶʌêʁÁԍ9ϕǨӯeӹ',
                            'ªүʠě\x8eχʸOÓ˼˶1ǧǆɎӐ·\u0383ǟɚνϸɚʞğƶy\x89ɶϿ',
                            'ʫǴӯȉԋҝ\x9aǄſѷφΣ҄ӷЇВɜѲњˠ\x93ΉҜǌ;ÚǺҹ¦Ȥ',
                            'ȧԏʆӊϗïμыò\x99ύɇнɐɐĀϪҤűǄӑɪўρȏɍϫ˻ѻӝ',
                            "æξ\x7fϽuǤȷˣԤ˓ħ©ʟǊĪφмĂ¦ǖҁ'ӁԆˬ1ŐăǾΈ",
                            'ҳăΜЯ¸ˤʥɵĈЪɭʿ˸ǞDjcђϯζɕƸø[Ϛȸ{ΰȧ"',
                            'ԒɰγɷЅϽу˟êȜŔŠϨ\x8b˸У\x89ŏüѰȬΪGˡʼŜçńӠə',
                        ],
                },
                {
                    'name': 'җ˜Ƽʚ\u03a2˔ǽúʌH\x9aҬ˵Ʃԙţū',
                    'version': [
                            -2190426361326609603,
                            -74913261614737869,
                            -4187738736049440214,
                        ],
                    'about': 'ǜэ°ɶҁĝͺòǑϼөѣÖҒÄ˽ͶӆϽӂϞϋʨ«¯ưѿƍȀ}',
                    'description': 'ЫǁЖ)μƌȊħ\x9eÿϚςĻźʧȬÄҨÊȴ˽ϢǴ ȘϮϚñǮŸ',
                    'authors': [
                            'ɚųȈԙ>HЧϫɵ¨ɢŔ»ɱÁʗɕƙԣǵƵ°ɖȣɲЗЗɮ{ʪ',
                            'СϲñǛŽƔӶτJʂԮƘɂÌěĵϝԤ˴ϵʩƹHїԐȂŅùЁǎ',
                            'Ԗ\u0379Ԏã\xadȀȤ^ЮĤĜųĈӍǄ\u038dӊµӇ¶ӵȜп8˅λѱ!ħҋ',
                            'ё\x9eӵϲϻΙÓӇͳ\x87ц²ƔҬʹԚФbȐҋѽƋԮ҅Ҋʔrδ;ˋ',
                            'ϓơőřŧѰԚϥԋѡǒʡш\x81όҺɮǵΤТ¹ɧʜŰźӨӳɄǞÍ',
                            'ïϖǒôӅįǤʎʯªѴӁʃƝέƟɃ˨nӐɽȄʝʉȺҗɳ±ҟˌ',
                            'ɮȼνНʚƱʲɉѱԁӚ;҃;ʧёϿӦцӍ\x84ʢѾӜķʰǈƩԋɅ',
                            'АԁʁʥʜřоǐeèпȘŰƏŜϱɔƙɪҕbʝʕЏҎĶ8ª¥ӧ',
                            'ʆϊФďʊӅļѮǣҲԭԃƙΒɰ\x8fӘЗč\u03a2˅ѱЂȿОӷǘ˨Ԉ|',
                            '˖ҬʒȥÙӐКғЁѻЬ˚ӻ҆Ɲ˓dη?ɐҲ»ƘŰ±ɞ%ӿё˪',
                        ],
                    'licenses': [
                            'ǯ\x8aˠɽÉѭҾ.ұɝʗȚķƗҊʒёĊϽƞɬǤǤˏФǪÙ\x93ɨ\u0380',
                            'ѳѝɾϔȍXɐŭÊ¬ɋǼөʮԓɬɘԃғĀЄѨӏӓϲ˛ӭɨŅŝ',
                        ],
                },
                {
                    'name': 'ɋѠʬѢ¥Ĩį˔ɴºўø\u0382ƱԔ\xa0ΣŇ˃҇СшǚҖñԤ˕ͰǤѯ',
                    'version': [
                            -739702631013552356,
                            -8546853285829664982,
                            -4654323672735531267,
                        ],
                    'about': 'Ͼ϶ǋεϙ',
                    'description': '\x89ά¯×ӉωȊȰЊʧ³,\x8aÖЋУϏҨ˚ӔωΔĦѫŕïόңįɨ',
                    'authors': [
                            'ǶύξǉɹŇіʊʿʛЛǳãǏǒɢҚԄ˹Ǥ6˳ūɗʞ˱ЩƃűT',
                            'ңЕǉмԄãӞǡҦԌ>ԥʲĠкǸāǦ҂ѸŌŢȃ\x9cǸƘҼԕʝy',
                            '°ŗСόíĊ˜ʇiƺϺǃ҄ÐъԓƴЪ϶ǣɋĚ)ӌ˹ђЏw,ď',
                            '³âљǡ\x9bȰѰέÿĻŢаԁȇ\x84ʑ¹ȏϰŘǖƚjѱӊЬ\x8dŵфȦ',
                            'ЦǽˣɌōґSϜ\x87ѐ`ъƎ.úрҹƷ˚˦ѡÿȓĉͺúъϽñ¡',
                            'ҭȥЕϷsȢ´ԍЏǊΖίƬư΄ʢǡα˟ɽԩĿćҿő&УǻĖΛ',
                            'ΑƊƶԀ˂ŉ´ΘӝɢӓųϚ˜Ҫ˲ʔЇǻƹҬИǉ Ͻӷ˒υƂЁ',
                            'ɊnӓʷŸnͿʇЍȻɝаǝ8ŁǽҐӀʥɛˌȪˋҹЗЏĆɪΑӮ',
                            'ưІлȻέ9È<ц\x90ƺɧžáJĔ\x81ҶƱŪҳÎɊҺ\x83ƀѳVʭǖ',
                            'ѐɍêϒ\x96\x7f°bȩɤTŻѫиӄɚԋӄҀпБ§ӎΝlĤßЯυζ',
                        ],
                    'licenses': [
                            'Ή҃ǟ϶ͱѠ҉\x9aӛNЊëɤƷсŕɪǺϝ:ŕ@ŢÞ˪ѥηȭЀԐ',
                            'DȂpčǥ˓ȴгÖюԤǣǍˬŉњɶƆȀѸͱѵþȁĮԈ',
                            'ЊďϻÉ˹ĄʤʚЋɆƥφ&Ȇ&Ǎŉʖ3]śӧsʃѓҊȾҲ\x91ҙ',
                            'Ųɳ\x97ЍHӈӁÝҡѵӵ#ҵϘΗ\x80ѽϱƱӜ˳ϪɼѼȑЉƞ˧σǩ',
                            'έ˃uȅƨ½ϩѭʗʅџχ1ʽĔψŊʸзԛŚÐˡϋ:τƼШˆĀ',
                            'ʺ]ǈȉҼф~ѥѳԟåһ¨ȠҜŘħįӶîɕɾÊɭшͰ˼ʂŧñ',
                        ],
                },
                {
                    'name': 'ĔŁʩɈӻAӀʥϑɿϟźΖ)ʃŰǖϢѼɫѪҶȒѸŵωӟCÕ˓',
                    'version': [
                            -7104537847264795109,
                            -7850443835823639696,
                            -8709891364826931322,
                        ],
                    'about': 'ƞӾΊŦѝԏҵɠĚͳ˙ĶӤ=ƏǴťʢяԝɕæϏӊƦОBĩgб',
                    'description': 'ӷΒƔЮ]ϠȸѮάЖΔѯYМͷœØĵшǲС\\˚РĒ\u0381\x92˳\x91˟',
                    'authors': [
                            '-èVjʐſÚǖўɂӖεƐҘňǅʢҵı\u038bψɁʸϮЍƈΌʫg˲',
                            'ыϼʀõѣȷɴͿʁʓůɞˬİ¤чưέ<ԚҗТӏӓuÿSîˋӫ',
                            'ʄğҌçтϺ\x89ӅƑʘƷțːλ\x91·ϞʴщĜ¢RҪԄɆɑχŬšc',
                            'əӔƳƪЖĕɭłɊӛɇѯӈ£ǍǊЉўѬФō\x88ÕɀƧƻo\u0380Ԣȧ',
                            'ΔŴȮϵǨҽνʔÂРϲҳǑɚ˫ҵĈȮӂŇǆǴǯԖũэ\\Ŵϙŗ',
                            'ΖĂ˃ĵƹžӟɘIŻхӓZȯҜҮЎϑŇϿɎmùϹʜőϏΞҕƻ',
                            'ǛӐɧɉƞŌ˲ſƄƎӴȻʸЇҷϊʋҔΜЪϗŻɼ8ǥ\x82ɊɄЭȗ',
                            'Ԥˈ\x98Ԛî˒х˟ń˴ѹ\x9dȳ˓Ͱ`\u0382ΫԍɃҋԒ\u0378ŻƉϛɕͳѢɃ',
                            'U\x96Ʉ×ŭҤɫςĠůÞӠӞǛÀƇ˜Ʊy:ɟŏɄ÷ШіÔ҉ÙÈ',
                            '3ҝяQŋ˹śϙ˸ʹȁÂҼŶҖǔn©ӻЄʏʵԑˍЦϾśԆХǰ',
                        ],
                    'licenses': [
                            'ʇǉԆҵΤGҐԐȤԕƁъɘъͷǬҀԄí҉ԆҫѝӇөүĊΣԩʈ',
                            'ãɎÞÂΡŎəèԫљʰĝʫΥŀЈȲʇӜȂЭѝ2ɋĵ˅ћÄėК',
                            'ѯhxӝİˬҬϭǡʩԄģ˵ˤ\u0381άʢƋɆăѤΚËϱҠÅƢ\x84ʜϯ',
                            'ͷƁ4Ɏʫ΅8-ɳ˛һ&ȷϒȰԨ˵5ɘϙ҃ԗ\x8dҸαЁ2Ѫŗ¥',
                            'ʓɅ±ȄőӇʘʅҸpǩԮԤηҞӅ]ɃͰ·óǰԕζƣћρԤйȢ',
                            'ʝϓӔИԦɟùȟÀʵщБȲύԡ+˄\x86ІΩ϶ȟYlϾʜƮϺҞѰ',
                            'ƃŭɉѨɩӇӎ˜ņűįӉԠτƞ\x97Ċ˟ȇ)öŤґφʾͶΉԖͶŜ',
                            'ҲːώˇžźȥýзяňƵ˯ŮƊԣưňʅѴʊБөɢїǱğʹϣƚ',
                            'ΙΘоʦƙԮ\x88ϸȳŀӦŋ\x8cĘEєΟҸƔƗӥΛȅѐ~қɤϛ\u0381Ñ',
                            'ǓѮˡŵʛĲė§ÏĆĈЫƑЖɁҥϸаˈÂƝ\xadщ¤ѵ¹ˤǐŎɮ',
                        ],
                },
                {
                    'name': '˖XĤm\x99ŴӳĥɝЗӓι\x9aѮΕâ˵ÒӱГ˳ȹì˄ǐʓˁÐǗĘ',
                    'version': [
                            -4321254186936985587,
                            -2819929171152105117,
                            -38207796123546687,
                        ],
                    'about': '\x86IįЭΖŨÂӿМЦ»Ϥ.ӆϾŉӌ¬żАҼÏϼЫȏӅλŽΥМ',
                    'description': 'ÑİȱЃӉӼӢCÍԢԡtҩɢӃȟӭБϨӁ˲Ӌ\x9cΌ˦\x84Ь˓Ȱï',
                    'authors': [
                            'ԃÕƏŀļҗЙ(џ@ŌˠĚњȸ҂βưɁYȼÎ¶ʠȂћʾï2ʤ',
                            'ȽȣҵƲџѐǼƛԝƀӵʆ;źķùĺķӞѱ˲ƸĹϯȢʥϔ˱Ӭė',
                            'àɋѧʮԮʬԖl!Ν˪ььˈţŊƅ+βǅүЬԭưõǸ%һÛϓ',
                            '¢×ΥѺԕʓμ\x9aяԈcƦɅǝʤЧдϕYļњúɀјɱ÷ɗȺǗ\x9f',
                            'ąæ\xad˚ŗǚɾЎԇ3ʕϛa͵ѺĠƚɴ˩҃ьӺƔuĤˁщŨѲǃ',
                            'bɷҴɊȘ¸ǥƩ1Űӌ3ήӽdĳˀҏ#ͻЯχ_ѥȗɗǱæÇе',
                            'ΥùҺʔƓѥȱӲǕ\x82˻ÞέČәүΗǕˢùѫɦȣÀԦӱҶτ˚ł',
                            '÷ʻӪBàȗӎˉΗԝ5Ȁ*ś@ԫόЊɽҡȊÙŬɮ\u0381ô\x8dĒȜȘ',
                            'ȴзʇƍҴ[ҸЮĞԩҜÿʢ=ԙθІɌþΓįɷǨӬҷϭ˪úКƕ',
                            'ћέΒƁԝˏǲʆӮ|о\x97ƓƹҊө[',
                        ],
                    'licenses': [
                            'ҋʋĤӨǄˌŜàҕǳ?ˏʄӚŻĭZҝĞөѼΪщԢλªŕΨNѻ',
                        ],
                },
                {
                    'name': 'ȥӡǧӊ҃ͰĿ,Ԑ϶Эѽ',
                    'version': [
                            -3738644739493028669,
                            -5032526568453254329,
                            -6767770573468827963,
                        ],
                    'about': 'ĨǍʈĒȼŮόɯѽŧ´ƶ@ƛͺԋ¢ƜҿυԭǥцԅǴſ]*МU',
                    'description': 'ˑKƮӽƤˆͶԤǼÛSôƎVȾCІǓŗҍҬRʼīӗʪÌʳɽ\x9f',
                    'authors': [
                            'ˡȺϗϙѐǨиʨ',
                            '¤ΣԎ¯ýӈҫй×ԭϨʈԬƸɠ¸ĆӳǦƯϰҦǔЏ\x80ŦʋÌâŔ',
                            'pĝĦ\x8fŇӚ¶ȚŷÞряÂ\u0380μʵƣБϔѓʙҌʊҥãǀǥѿ˽ȵ',
                            'ĚʭʩЎȧԏǳӉοѱҁӣ,£ȩϨǺҹǥǄüѽ©Ǜˮƫò˓˵ω',
                            'ʸεЙӶŗʨӪ\u0379ÌĕǮÐň\x98ˇΰѦȲÆԢʢʂ˫ҎψѴòҵƁ?',
                            'ǤǘˆĴEįѢ˺ѥҏҟĀg˥θɛԑ-\x83ү\x87ęѴӬŬόВѧΤҎ',
                            'ʚ˺ʪώ϶ѧi҃ıԫÁԩɡ·ːơʲǏɉMǂÈҺǀƕҟûӖ8Ԅ',
                            'Μ˛|\x9fµǴƒŸюɬƂ;ͿΎȌӸʴ©яԠљ˼ǭԙåŴʭŭ&Č',
                            '˖ɄAÅώà˂Ÿʂɳŭ˪˭\x87νƩƔƐԞ²ϤͶƐɧӘĈȓϑͻЋ',
                            'ԌʇȶǿƱǩŲ\x80ŅΛǧ¼ԒҊƯĄҾ˥Ĝ\u0381кśĝǚӮȴəºŃһ',
                        ],
                    'licenses': [
                            'ԁ»ȞϨ\u0381ʕkǍ<ƶ½',
                            'áϏzLҍеʆ҃ŕNӭʍͽη\x89ųʶҨƁѼʻǩȈƧϧͶԣIÊɱ',
                            'ӑőǎȗʷƣĵ˒ϗ¡АǀÞpÂƵɉɴӮʀϏwҝĉˏɩЏĘƁ҃',
                            'ԐLĭƑ',
                            'FŞÚɖôq\x80pαҒQҐӲǅѶȓĽ0ԝɧ&ɶˡҥȶͲӦµԭў',
                            '˺ȾΩ\x9bԩʛƖğNİȳɷΨиɈІ\u0382ԮĄ0BþҞƥĢķĐΓˍł',
                            'ˌʏАȹэǠІъɩʒѴ~ƄΌΒĶɗ˸ФʣѳцͶŶĎϝ˓ѱȍө',
                            'ǛϨY<ɪɋdѕѕΠͿʎԑÀƗǚӱɶѐгϛâêɲӣʈΠÒΠʌ',
                            'ƍäƗҠŶĜӛū¿ɪĢśńҕˠưϋͶʲŞȖÊÙʆɣɻӮ¼џ\x8d',
                            'ɄÇӢԔӐĐ?ΗӴRĨʕ˵эÐȇQϿĶȽ΄ȁϾΩǳɌâʳδń',
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
                    'name': 'ǇЭ;',
                    'version': [
                            -4907372117317305860,
                            -7029772099557700551,
                            -4730887001270142753,
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
