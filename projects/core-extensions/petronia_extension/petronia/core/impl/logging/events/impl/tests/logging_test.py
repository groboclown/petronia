# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-03T18:04:45.311323

"""
Tests for the logging module.
Extension petronia.core.api.logging, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import logging


class MessageArgumentValueTest(unittest.TestCase):
    """
    Tests for MessageArgumentValue
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in MESSAGE_ARGUMENT_VALUE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.MessageArgumentValue.parse_data(test_data)
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
                res = logging.MessageArgumentValue.parse_data(test_data)
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
            '$': '9ǯӃǘǑӚёзŵϥƴƖPǰН6ûǶǚÙΓτʗ-ƣ8эϓђĞ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -7740949405974342982,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 160838.19326617895,
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
            '$': '20210203:180445.232479:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ǊƠӇŤÓ®іУ\x81İ<đßĕóȋųЌöҧȠӃ_һѩГÕԄ±ҹ',
                'Ĝ˰áϘѠŵʑ\x8eʔÚƗӷàȷɵǻxƔЯԝɥMȄʌʩӔǃмǛȋ',
                '\x89еʸɋEǸЪΜɕ˰ĕ¸γǒ¬ƪ˥ɶȕțʑ\x7foˢљȉʩ8ЕŰ',
                'ҟĿĆҕɓ˽Ϫv\x88ʓσǂɰұҁǋǎέ`ʹ˥ϒǣŅѠњķ´϶У',
                'ӼԂˡ˕C˥mԞɼBƍЍѫɜ¸\x9bǖғŁȍȶxϞӴYˢ©\u0378˕Ԟ',
                'жƭҚ<ϻҨ˸ŔįŌSéѽɚÓȥ\x7fĒ\x80ʍрóҴѴ°ÖĹӒЯԮ',
                'ǁϳ\x84yԠōˈǅũƠӊΨͽϜӤɀĖÃĮɬǈ˯ӱʕԝǈǭΐМϬ',
                'Ǯ҆ǚѳǢʔƥ˾Ƒ»ɢ΄ϔƾԀПЯчӁұ¥σƢ\x89іʉʒu±ԣ',
                'Şɹ;ɐŎ®ß˨ōҠëр³ĴŢÇ¡ðŪ£ǚϰ\x9cǯҕςΕ\xa0кЪ',
                'îǧМ҃Ň\x83ȗσζқƕʭ-ƗϼɘϩɨŝӪƄЯГŰ·ȋԪΖз¶',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -3997081084169231862,
                8289456378314814687,
                2327844007147572099,
                -6729723317788628887,
                -7830031232089226266,
                5441612560330614276,
                -1805526040763271981,
                5051927362062132162,
                2974638242631776346,
                9133059600082517563,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                39239.96965700216,
                511980.4004923095,
                543733.9169506201,
                897760.5438817529,
                720927.1512320224,
                863711.094482121,
                977658.6185630169,
                822354.0771768804,
                715038.2998489309,
                312077.9186769426,
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
                False,
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
                '20210203:180445.233370:+0000',
                '20210203:180445.233381:+0000',
                '20210203:180445.233387:+0000',
                '20210203:180445.233392:+0000',
                '20210203:180445.233397:+0000',
                '20210203:180445.233402:+0000',
                '20210203:180445.233407:+0000',
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
                res = logging.MessageArgument.parse_data(test_data)
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
                res = logging.MessageArgument.parse_data(test_data)
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
            'name': 'ҰǑ¢¶қȵСƹǺ)ȮӄdΡļˇ[˄ĜēȊŐ˒ɾźԨβлӹǙ',
            'value': {
                '^': 'int',
                '$': 7385405267643207814,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ğ',

            'value': {
                '^': 'bool',
                '$': False,
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
                res = logging.LocalizableMessage.parse_data(test_data)
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
                res = logging.LocalizableMessage.parse_data(test_data)
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
            'catalog': 'ŋԤΩϿāˮƸ\x8dȩȍʘџɇ\x83ɑϧ5ȎӾƳȓыȐòɷѭɣœ˴ҩ',
            'message': 'ģηЖӼɅҬȘҋӪƢһǏйßĊд¿ˑѼȉөıЏŅɾєћъrƉ',
            'arguments': [
                {
                    'name': 'ЏҧԏВό˙ˋǝсχΓΑʨǨ9ԜΘɇʖɲϊяˣǲÏӕċϪԑ\u0379',
                    'value': {
                            '^': 'string',
                            '$': 'OЋ˒ιĳȀȼϩŇÂ;ΡëǢǙĲ˚âŹǛЁƾșdüԙӶϞ\u0379ϼ',
                        },
                },
                {
                    'name': 'ê3ǽȌҕȎʡԅȲʊĀėɰҼԤϘԅ\xa0ώ\x80ȋϮʃαԅŦśľŦĥ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        399501.33620652795,
                                        610060.5635482193,
                                        407214.8100255313,
                                        -90520.75419204176,
                                        301138.694606049,
                                        721564.2253801995,
                                        681499.7939214912,
                                        -78266.98256966707,
                                        561634.2330742977,
                                        911107.0382179056,
                                    ],
                        },
                },
                {
                    'name': 'ɲȍЧƚҿ˅ΗҮʭɛŕӠΞʷԔԖÅďÈʊ ʹɢ˨\u0378ínӧ҄ï',
                    'value': {
                            '^': 'int',
                            '$': 9040441447765678128,
                        },
                },
                {
                    'name': 'ąМzǲϚгɅ˛ĳәǦáƟwfγ,ĒǚʵТ/ԌYˀӸįɩϙА',
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
                                        True,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'ϏāˆϔżƝ\x8dӉƾŹƳ˰ʵ{Ë˙éȟǜȔ˷ŗɽȢϷж',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210203:180445.230925:+0000',
                                        '20210203:180445.230942:+0000',
                                        '20210203:180445.230947:+0000',
                                        '20210203:180445.230952:+0000',
                                        '20210203:180445.230957:+0000',
                                        '20210203:180445.230962:+0000',
                                        '20210203:180445.230966:+0000',
                                        '20210203:180445.230971:+0000',
                                        '20210203:180445.230976:+0000',
                                        '20210203:180445.230980:+0000',
                                    ],
                        },
                },
                {
                    'name': '˫ӻю\xa0Ͻʑ ћλ΅ʴ҃óӣ\u03a2Ҵʼɼ',
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
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': '\x9dǬԕˤгɍˁɫΘӏÕ£ùȦŐҏö\u0378ŮɳйЙΙɢӁ˧ȫǒ\x94ǣ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210203:180445.231419:+0000',
                        },
                },
                {
                    'name': '¤ГҳёÜӃӤåω˳ӏĕЛ\x89ЫұεʂÚΜǑǋǶ˩Ё[ԓ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'қҚgѻӨƨ˷ҕӵԡ\u038dǽϱÕŃIɛĘξЀД\x92ʚŨɞʌɏԈ<я',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        False,
                                        True,
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
                    'name': 'ЮğĆϔɬкƀӍǴΔȧìĹ>ƕˡΐƑρӅšƝЅĜϘЯ$ˢ',
                    'value': {
                            '^': 'int',
                            '$': -8204056954950089562,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ԅƭ',

            'message': 'î',

        },
    ),
]


class LogEventTest(unittest.TestCase):
    """
    Tests for LogEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOG_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.LogEvent.parse_data(test_data)
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
        for test_name, test_data in LOG_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.LogEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOG_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='scope', name='LogEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='messages', name='LogEvent'),
            ),

        ),
    ),

]


LOG_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'scope': 'warning',
            'messages': [
                {
                    'catalog': '¹\x9aȷ¦˾˳ΙȣϷε\x90ǿĕȂʱȗԜϖĄӟПVҴɂĬѿʣˣɏǘ',
                    'message': 'ѓƧƏĴк˾ƉіѷȟʃγɀƻҠ,œôĉȸǷÖʖƝӉĀͲμlʱ',
                    'arguments': [
                            {
                                        'name': 'ʹȣωɨ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 113509.25244044757,
                                                    },
                                    },
                            {
                                        'name': 'өԃИϢɯүƩпIƐʴ!ÇʏİΘɃĺɫŷԂϫШęϽǫƑҮŨԃ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŌȤɝϲӳşϰҌɗƯӞɋǳ¬ϰͻгǵԡ¿ťƋ˷ŚҺύ@˕s\x88',
                                                                            'ɌpJƊʒôпĿ˗ƜͲɡĄНĿŠǤD˔ҲŠҸΖϿʊuǆȲQ\x9c',
                                                                            'ϵ|φ˄љǹʓĉɇ2ȬʓǓβѨƍ`цǸɳӂкԊĚŕϧ(ΚѤȂ',
                                                                            'ҵЮȑƑ҃*ƇæIŖêӜԤƿȑѹӠ8ð\x97ʻͲӑ\x81ɑӸϕʕĚϒ',
                                                                            'À£ʦĭʨĆЄŊЅ|ʪτҎaԉЯ˗ÔÒӱƃ÷Ұăǫ˞ͰʲҾȅ',
                                                                            'ȂӨӁέҧºӯŏʹύɡ0КЀо·Ϊǎ¤˪ˤēӣȗáΜƎȖ)ʭ',
                                                                            'ђŧŁԊʋҶʩȿthӳ®¡яŀ=ѝĠФÈʇ\x92Ȱ`ƩϦƭҼӥʧ',
                                                                            '˙˂ɨʅϞӳѽН϶Qʶ3ȁyјг#ҩ$ТΏè\x88žҸēȠϞɓƨ',
                                                                            'ĶãâģkҪТȸƗ\x85ϞƼɓ¹\x97Ϲɲ˴ԦԢȰ´Q¥ȵŪϔ=ϋЎ',
                                                                            'ҖȜŸњΰÆБȃĎǆƅǐΝ˒ѪɢȗҲΖԍ\u0383ҫԧîʌ˩˲˚Ԁ@',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÄѷǙ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȉɤιɅǂ%ǞǢĘÌȷÚĸȵĀÔùǓҟƮk÷ЄţӑҨҫϵӨδ',
                                                    },
                                    },
                            {
                                        'name': 'Šԣǂț',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            650144.7394167793,
                                                                            462120.7345236322,
                                                                            454146.8840990489,
                                                                            818659.2391383804,
                                                                            269107.52238941065,
                                                                            627747.3312411973,
                                                                            549615.4246832873,
                                                                            843989.8900052634,
                                                                            76336.55628230597,
                                                                            -31028.1088126979,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x82ΧΕƠȄοјҏãźγƸǼͷЏЩϮLȶŅêāЪǿŮ˛$˭ʩϝ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:180445.208052:+0000',
                                                    },
                                    },
                            {
                                        'name': '˴ǢȤѐԂМӔ˚ҠÛʊЗêО&Ԗϟʪ϶ÑВЀćɩƄƏҋĐƖé',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1267101530837350755,
                                                    },
                                    },
                            {
                                        'name': "ЬВθGѫƠjԊʴͶŏϩ©ʘҌӽӾąӵü'ʜΰϞƉҕɉʛʖʱ",
                                        'value': {
                                                        '^': 'float',
                                                        '$': -90841.00998266583,
                                                    },
                                    },
                            {
                                        'name': 'Åҫʚ\u0383~вo½ʽѡƄͿȊѵ~ӬψːͲʟʲǐȀӔӊŠlʲκ@',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
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
                            {
                                        'name': 'ȼ£~ΎğÂЬјãǓΓҙÌƨ\x81ѪÐǧИΛиΣˮSǱȍŠͿȖӿ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8252106101483536561,
                                                    },
                                    },
                            {
                                        'name': 'ҸǂЉ\x8c',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1375367193272956630,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҢđĕÎˀТҺȻɵϔϪƤ˳èƭԉΫҊǧȈ´ҤЮяŒћɓĳjҫ',
                    'message': 'ӇƮ˟)A\x84ƖŏƃΙϬʇϐˠƭԨtɦГɫĘ}úAŌӎ9Ŭϐӽ',
                    'arguments': [
                            {
                                        'name': 'ԥiǳ½ȫГЌİӕϯʌǳнӠӓŤèŰŗƠв',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -82083.31438560845,
                                                    },
                                    },
                            {
                                        'name': 'ǟӛĢҏЀVǈɟģwʣƗ\x8dſҳ\x9cːӟVЈΗыѿ\x7fȽvԑùϳ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˗)ӴÍģŲДʭĔ҈φĀɱȀԪ˅ǷȈŧƅɕĸʱΏǷçɥϝ«Ȃ',
                                                                            'OȗԁԃξϙÚjâɣTʗǅҠϓЁҫɎˍȭЖɍȐɃЬȱƦɾõΔ',
                                                                            'łѳԙ˨ʹԣӣŴǧÒǑȟɼưФȃ͵ćѲɪϣŠҬϛ˥ЪʓpыÉ',
                                                                            'ӶŏȩȗƑƒΨЈ1ЗșөлѦ\x8eԘьʂēΈɴ˻ҍİƆĖӆ\\ǆť',
                                                                            'Е\\\x9bˮȷΜƛɢƴЂ£ţƑtőΕʤȝїѳ¶;ΰԩÆԠϒʉƈƘ',
                                                                            'ҦԈѦѿȍӿ\x8eƶʷŪÌĲÀǼǫʅuӽǲƯɋԏӞ˶ǄŜ˓Ȏтϖ',
                                                                            'ȖЈQʐ΅ӍAcԏ˹\x86ӱΒʷ˄Ïϊҭʅ8φŇʱʸ\x98ŕΆŬʅΡ',
                                                                            'ºĀÇΪӈȐөзѧyɑÈ`Л£Z\x8cwҸ˱ЭʔΪúƱӈιРϚИ',
                                                                            'sʂѭҖɤƪӌǀĲĘ¹^\xadћðҞ˕ҲɆşŻƅȸ#¦\x9eҤϸөƨ',
                                                                            '҇ԚņAåҶƇћƦǳõÉʹɍɐӠ ʦɂƵέтʘuƲԇʁǕЎœ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'аǫЖºǮХQȡӗʣxҞŜԇъѽҼɒǉѨӌ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': '©ƻȼќұòҴǥɛƩtЧĮǠǗӘ˭rǌPǩҝѵ˜ġY',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ϯҗƎƻ˅ќԋӿϐмƓǒѽȃ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˈԣΈƮŐ˽ʁf¯ӶѭøɒÊ/Ѷą˖Ԣ\x9eɔÁ΅˅ȂϭӚÍϐó',
                                                                            'ɶ9ƱԢ˷ȮψłǡҳAҗжΊӜȣԗʤôÏïёëцǌѫŭΘΈƲ',
                                                                            'үƷыòɶķʥΠºɡҮȁΞԖҁʰÈđŨкѬSпԪѠύ$ǋã˽',
                                                                            '8ȲXҌѝǬÌԙԆɊЇ΅ӆӊʡɞɜ˾ԋƬôȞ÷΄Í\x93ĶčȈλ',
                                                                            'УѼҵϾϿԕѷqʟЛЮGɃmľʧÛɀɾƖ±ƻԃѬƱǟн˵ŻĬ',
                                                                            'žз7\xa0ŴùξʈԐĵʋ˪ɦXъҢӟʛωˀł$ҺÈ\x87ƐьōȟĂ',
                                                                            'Ͳ˶Ѭ ɘǶHŃϕ7ƸѱВ¿лɽΒȚҞâƎǈņӲ:ȶҨϬ8Ⱥ',
                                                                            'НÌӶȲϛŬ&ȕéƁʸːǎˉ)ƲɻəҡƋϡώϯŢϏѩЗţůǵ',
                                                                            'ƳȐ;ӋĶʿϧƭƫ\x95ҒĺκǅϋѧҒʌǞƼАюл˲˅ғɏɲȾþ',
                                                                            'ә\x8fϡʿŀϠΆɰϙӃ&ɘˍԀƯŽЇї[ӅƓŮƴȗТʼˀȅǆѯ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʛ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:180445.210743:+0000',
                                                    },
                                    },
                            {
                                        'name': '\xa0ʀ©\u0382ʿɮҞηTͱ˜\u03a2ųū/ӍˋɑϰϮпӹÚϷԕľ\xadéƜʄ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8045980149809046104,
                                                                            -7394410121397944153,
                                                                            -1026182432953511700,
                                                                            -5749182998966145008,
                                                                            1395499570436867889,
                                                                            -8513275784468301731,
                                                                            5201376466279771602,
                                                                            2990483537409387676,
                                                                            -3960166536640684774,
                                                                            2695379209953083135,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӴԎ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҮɇΈѪԞΌШʌ1ȣсԏҟ1\x8dΏ˭ƫūǇɈҡƕɬʸʪAӑҠϤ',
                                                    },
                                    },
                            {
                                        'name': 'ӕřΑ«ҜιÿʵӐ-ϧǡΓҮ҉ÂψѥҸЦǜǂЉ%ѶĪ',
                                        'value': {
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\\ƇχҾĠȕʺǔěěǙǸ˪\x97ΈȶʅēϽǘvӗˍїˉѻ\x7fҼÛɢ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 248908.45216265047,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʉҘʧƾrӾ`Ǳүҍң\x88ʱѼ\x8e˞/Xʝ"ǣǣѝЧ£\x9eóК"Ə',
                    'message': 'ǴʃÅΉҎɭӾΠҞɗ»Ӱɓύõ~ƟΗҬɃѧĶϣɆєīƅαưѐ',
                    'arguments': [
                            {
                                        'name': 'ЬȄU˸ѬȓɂɢӰÏΒ|Җőþɋο҃ԚȆʿ\x80ĖżȸťűɪÂš',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '2ϘӍ]ȶƙɮȳПȮ˨ѶʟĹũ҈ħ˔ŢҽӾȠθЦ˟҉ĉТ¬Ҝ',
                                                                            'ɺʊµʋɸɠΟҠǶÖй¢ČʑӌζƟŉ·?ʷ\u038dӂѠ\x7fųҗԓСÁ',
                                                                            'ӈʈӟ˭˫ɫЪѲɆ\x95ȎѶҬŲΩʎȋΪɮȭ/ӭȬ˪ÔCҗăę˚',
                                                                            'ԀӒȬЉƄʰȼʗϕИŲѕȪͶƃԊœ˰ïÜӪɌȽѶѕӋҭı˕ƅ',
                                                                            'ԟ˽ЈŋԞɈ^Ҽϐ)ΆѥȗЏˏ\u0378\x89ҀҾɯЌΉʖȷӈ˧ЍЏϾʼ',
                                                                            '\x8eǦɅƒϬɂόԫÈѣƼ£\x9bÏԩϷϡͷӪƯʲˣÃʬ\x80ПƇäѪŉ',
                                                                            'Łԑ҅ĭƢȓöӌ"ǖKϹԍӿˌAˉїȨРҶõŻϷ',
                                                                            'ʏӿɁť.ȨϼȚɘҿ҇Óʤ˛м˃ʖћ0Ӻ\x9eˬϪшӛ²ÇеƵ˟',
                                                                            "ϺЂƞĹĂŀƦȣˣϗĞ\x8dƢҽÎǄ˵ȱӁZ¤ƶ'íѶʲʸҾȁČ",
                                                                            '/ºʛǏϖʥЋJ9ʚ2ɽϪМӲӶƿɞˌƺƋҖˑӃԂϸ˽ʹҠǻ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'wӥ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˊɱϜϪÝƠΰFĊÿÞØБȱǔ¹ÅeһÈҰ´ŒgBѨʗ˛ǯҕ',
                                                    },
                                    },
                            {
                                        'name': 'KU˓ŹñǁǚʖīІņΧѡ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6745398290960060967,
                                                                            2728485634616679292,
                                                                            -3036008941714588502,
                                                                            -959281084502989249,
                                                                            -8732021702330922368,
                                                                            -6708953252711163852,
                                                                            1915399837934218400,
                                                                            -7215236628423163296,
                                                                            -9047590319899981783,
                                                                            -425879684436831952,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƳͲāѱVоˣƔȁʪϻǀΎǀӉțƶŦԨυ@ƶȾķ\x8aǈĢÆѸˈ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ìƅĠ\x83Ҍˋ©΅МÀҲЭъ¨ʣԇԮťɛѵ\x9eμ΄IĶӵƢöԮ\x9f',
                                                    },
                                    },
                            {
                                        'name': '҈ʋÚԑ˹ќÏъνIKƆҥŊ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ФƒϓĕԕɠƾɘκǊƼŒ\x820ĿýƸӨɵԬ-\x9fϿȸɷșȥ~ӷρ',
                                                    },
                                    },
                            {
                                        'name': 'ҝÅ҅ϝŨϘģîɖŬǙӪçͱαäȃÏd',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5950308573710505310,
                                                                            -308787318348310427,
                                                                            765118100047255937,
                                                                            2086202102333963813,
                                                                            -21732638663908479,
                                                                            -380913740236755679,
                                                                            -275102163609513853,
                                                                            -1219785503801114240,
                                                                            3025022120567022796,
                                                                            6427270704717228523,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΪùǥƄƕƅԄԃɅͳ¤*ӿѹԦ·ŸǻʰύαòϦӑлԈɹ$ӚǕ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -8760.788676215438,
                                                    },
                                    },
                            {
                                        'name': 'ңŬηԊљɃįϲϯȨ͵Ҭˬ˩ȁȫДΗ҃ȡǓϗØΘӴ(ԩȗҮƐ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҜžʐȕˎĬʘӽĉʲβƷӹȨϼ\x84ʑ&EūЙɚśчɌˣ͵ʊсѺ',
                                                    },
                                    },
                            {
                                        'name': 'ҏʌѺǵƘ҅Ђ\x8bȩěЎɜʲ]áǜÛͼŕβ"˟ЏŇVĐɊÍƧǋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:180445.213853:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѻʵͻ~Ԙɑ˫ýɬǒŹĖбˏΞȑšɪɱҋԓϛ˔л˲т´тӚВ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8551033088582890406,
                                                                            1564283404662638620,
                                                                            -7690231720862018464,
                                                                            -6009352181099457925,
                                                                            3826689189318732252,
                                                                            450201786392843461,
                                                                            5997614338282469772,
                                                                            -4373487311124056512,
                                                                            -5722626711970940713,
                                                                            6993203696504083933,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "ĝô˯сϱÀ\u038dψšŲȨ\x97ʠʶӵΌʏαʻӮ'QϚǜƔƑĘҝǐĸ",
                    'message': '÷ƕ˘ǅиϯǺҖ˨ɪҫʨěκѓŧZʎҐҩњ˖ǺφĪШ¼υŻɆ',
                    'arguments': [
                            {
                                        'name': 'Ȧ˓˛ΥŪPԭ\xadϦʪЙ҂ȪƩЬ\x89҃ҟѩ"ʼĵͳ\x82Ȼ]ѸѹŮκ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -12691.358888800605,
                                                                            194503.2475574657,
                                                                            586612.0677700969,
                                                                            369561.0978998132,
                                                                            151699.92171452055,
                                                                            192616.77791285003,
                                                                            636419.3506627012,
                                                                            222091.16572319472,
                                                                            -23871.747568899926,
                                                                            -6410.0361312873865,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǚˉѷħѮŔѢƵΠˮɻɂҹƇÛƎɁśX^ǙВХοȴĕǶƭӓÇ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 995947.7183559868,
                                                    },
                                    },
                            {
                                        'name': 'Ϟ\x96ǜȟ@ǉЏƩƫÊһѕėƇɠ˨ʋѥԩƾQ½ȪŗȽԟÕˁƬϙ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            94038.17262171899,
                                                                            788270.9618859938,
                                                                            569978.1065470885,
                                                                            481304.9616972874,
                                                                            986452.2409287852,
                                                                            49333.35502668776,
                                                                            341269.511574601,
                                                                            251388.03380371287,
                                                                            600489.0014409588,
                                                                            707005.4270822032,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϲƸʇ\u03a2ѪпЙɴԤɷΛчϩ¬ȳϟǟɏԋǌhϪӳҮâїľ»ϔμ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            971314.2743508199,
                                                                            908616.0714996024,
                                                                            584240.353951479,
                                                                            991559.1225035246,
                                                                            702886.1598058867,
                                                                            847435.3024798741,
                                                                            995034.6940290469,
                                                                            109129.43570316242,
                                                                            74183.81820572334,
                                                                            492964.74154492386,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԋ͵\x88ϴ\x9eƤӰ¯ƾǒźϩΈ0jέµʺЍİÁɷͲ^әɗЍк\x9dӬ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 69.79643931967439,
                                                    },
                                    },
                            {
                                        'name': '˳ϬVЇєȳȁǑΊțüԓЄŝҶǟβƎ¦ǱĮ˟ĥ$½ĩōҊƾȦ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 939987.5814695947,
                                                    },
                                    },
                            {
                                        'name': 'Ɓğ¬ºãϮ˴ǋҍЁʫԢϦϕʉȆūȳϽΞʇɴ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:180445.215729:+0000',
                                                                            '20210203:180445.215741:+0000',
                                                                            '20210203:180445.215747:+0000',
                                                                            '20210203:180445.215752:+0000',
                                                                            '20210203:180445.215756:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʬ\x9bȌӢȺѕӹ¶ǠΎ϶ǍМ˷ΑŰĚŭǌʪĤдšĪîќ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:180445.215960:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ΚØ\u0378\x8dťĺŕë_ςȣƔɹɈ\x7fȳŊÍÔʹɻҩgЈсʃnѕЉƲ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            67622.17920865802,
                                                                            187599.9204875204,
                                                                            559660.4417563253,
                                                                            759289.5196653726,
                                                                            216924.11908356566,
                                                                            363430.1707197966,
                                                                            472029.5874690999,
                                                                            645385.5525578053,
                                                                            445243.00007300917,
                                                                            17093.11423868712,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '²ʙЀˣΘǊƤ@',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1849090749181764803,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǽŎEȶɁʾγԕ÷ɰʷ˳ҊŽƉӺʣҨűӞ*ɸƙжƺĆɜӚԗԏ',
                    'message': 'ƺǹϤ˥҂[ʼɑӶÊωͲϪΖ϶(΅ǵӜΤ˱ƹƉĤǡwӕSυŦ',
                    'arguments': [
                            {
                                        'name': 'ǺħRƐІΜĂĄ·ЌCӶωǄrJŏԐɩǔƦ/Ȃё˯ϲŅɷԫȷ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȷ\x9bԜŘhΑLȬзԡӄ ɷ\u0380ѸΙ¢Ϡśɕ˞ҨԍǵmњCɩЁ˹',
                                                    },
                                    },
                            {
                                        'name': 'ӹͱ¶юƌ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ĘïпƁϋГɎԦńʕđʜ$|ϧğȟ˵6˼ҏԋȫõʸ˗ϓËȤŬ',
                                                                            'ƪčє+{ȞҠȷԌϩфġˁp´\u0382õʏǢѤǓǸШˮԥįʓ϶ǑЬ',
                                                                            'зςŬïƞȢɽǙĶÕԉ¶ѠóӑɥúԨűåΙѷȊӿϞâϐɡӥǨ',
                                                                            'ǭƒ҃šʠɈĸŕ\u038bѸҀыҷдķӪbц\x8dϬșşɚӳƥrԨ\x91?Č',
                                                                            'ŁҬґȃɡӼЪԛИ ˝ӫο6ԙˠ\x9f°ԐϑĹƃǾÁʟɢЄӑȲ~',
                                                                            'ĊԢɡɧȞUЕƁО\u0381ÄϮǁƶƾȮâƭЙęТԚ.Ή\x9c9\u0382?ʧȒ',
                                                                            'ЁɁөÄϫлρћЂEӖĒɐѡȎyˍһŤđʊɐӂѻҧȡѕƆќЯ',
                                                                            'СӞĊӤȓʻ˩t҅7ɗ˗˨ŭģìáğǇșʿήūùφČͲˎЊΞ',
                                                                            'μӖѻȫƦԝŇǙȍn\x80ʽѱŌΗ\x91Ϫ©ȒĚȄԨȰ˖ԗԆѕȂŘo',
                                                                            'ҖҮƉɂĶҧƳѰ˟ˆӈËʈƒ\u0382mҒŰ\x94$ѱķрʰе\x80˒âӫӧ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɍĸĒɦӔϏ7Õʋӌ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
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
                                        'name': 'ïӴӃ˨ϪӫƎƪʺόɆnȶóԊǢʝŏЕӹ7@ũƞ˱Ę˂ΊϘv',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɯτҚӞҾĘμЧҶ˱ėǂÑĭЫЭȇɦԪҳѠ˳\u038dάćϴє˶ČȮ',
                                                    },
                                    },
                            {
                                        'name': 'âϷҏӇĢʣǊƍŎ5ӾǙķԠťұȚ\u0381ӇʩςŝбτƓȽɲΦŨԡ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:180445.217709:+0000',
                                                                            '20210203:180445.217719:+0000',
                                                                            '20210203:180445.217725:+0000',
                                                                            '20210203:180445.217729:+0000',
                                                                            '20210203:180445.217734:+0000',
                                                                            '20210203:180445.217739:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƐԁeɑԛԗȮ\x94˓Ӑѡŀ¸ΒŘAɶ\u0381"ѰīČǸЄʫϽɫĥ\x9eï',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6702127385351695212,
                                                                            -6923934198973386634,
                                                                            -2885365438763976145,
                                                                            6890848612503626554,
                                                                            -7154535106011454658,
                                                                            -8274167366237028797,
                                                                            -1499246100672925203,
                                                                            5404788375021720248,
                                                                            5757232134861430056,
                                                                            4820423832315271318,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǒŕόƨę$Ӧҁе',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 18993.990816435777,
                                                    },
                                    },
                            {
                                        'name': 'ȑȯϚùһӴɄ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            247519344710945705,
                                                                            6749082890076399866,
                                                                            -9082701590609295271,
                                                                            6275118300327514154,
                                                                            7141059741094632103,
                                                                            -8042787718679100566,
                                                                            924000127638261580,
                                                                            -2069479835130636169,
                                                                            5456784289448762576,
                                                                            1391468927651226476,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʂӱϘʐtψVϿѱțɊΩɲȈѺЈѶʎӞS˳ö˧ӫˏЃŬғɇŕ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:180445.218596:+0000',
                                                                            '20210203:180445.218608:+0000',
                                                                            '20210203:180445.218614:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӭЧǆʦΠǞΛͷʯїΣйϸӰҫяІЦƿԎȟ\u0378Έb˜ŋ҄',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϠѮʓ(~ūȮķfp˚\u038dĥɯȷʮȠЀȫŴŘɗɕːôԇЌůѷɥ',
                    'message': 'ѺϳΜƮyЄԃñ\x83%IԇɻΡ\x86ŠSɡýѤˠѱäŊɼцɄ\x80Ґǿ',
                    'arguments': [
                            {
                                        'name': 'ДѯʥΚȤŋ\x80д҇ɒȗȵҥ\x9cɌLɬǪȒͲ{ʙßЯZϱʴ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:180445.219265:+0000',
                                                                            '20210203:180445.219276:+0000',
                                                                            '20210203:180445.219281:+0000',
                                                                            '20210203:180445.219286:+0000',
                                                                            '20210203:180445.219291:+0000',
                                                                            '20210203:180445.219295:+0000',
                                                                            '20210203:180445.219299:+0000',
                                                                            '20210203:180445.219304:+0000',
                                                                            '20210203:180445.219308:+0000',
                                                                            '20210203:180445.219313:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '<ԦȜŸnſ˒MǱéʿũí¯ѳΊ˘ҋ˪ȟŐϱǲĐ˺ҵЅҀѥ,',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԩȪɦ9ΞԜŎЮЉ\u0378ҬȺ?$ƪΣԠ͵Қх0D˒ҀˬӅƠӹ;ɋ',
                                                    },
                                    },
                            {
                                        'name': 'Ԙ%ϞƉѸѢPʩÞʗĨȟżęįĭ\\уƜ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'žɿűǢ϶Ũ΄ŭzřъɛÅѓMŎƑș\u0380ƸԘªTТļêΥ҃ϻ-',
                                                    },
                                    },
                            {
                                        'name': 'ɗŮӰԒðѭÇƗɗįȘ=',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4367215118241970326,
                                                    },
                                    },
                            {
                                        'name': 'ǹ¹ҘЖ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
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
                                        'name': 'ӵƄı×ČƫɪβȠƝ)ɜҡӋĺ5ǄаԀ{ȻȤς',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:180445.220156:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƾBȍΜίʞĂѿǜÓңӚɹ.νЍĶϪ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӹ©Μ˩ƈДΈǞȘŃÈĸԎΒӵМǞƄÄëǥ0ҙŽ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'oñ\u038d/ңʑӴˢԋˁНˌЗŻԄǐßưҧԘıҾԏȔ˜',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1746671851617858372,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӑё',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7315108638647303890,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɍǥǊȠ˚Ν|ЦȈЩʞƝιΤЪȭōňļʝȜȿӯOȬǽѭЏǹ͵',
                    'message': 'ЊϢǃ˸ʟԞϷ\x7f×ćӡĻөǧʊͱl\x99Ņʃ#ĵЍųǘǇǈʵʊΓ',
                    'arguments': [
                            {
                                        'name': 'ҤҦ`=ŇǦɁĽxʧӺ\x93ѫȅ£·PαȪӣ8҈ɹˇƸƈōԈЗO',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6957992253363989081,
                                                    },
                                    },
                            {
                                        'name': 'ϯϘѤ͵',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4374752933053698914,
                                                    },
                                    },
                            {
                                        'name': 'ЮӜĻcӀЏŒʐԣƫ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:180445.221499:+0000',
                                                                            '20210203:180445.221511:+0000',
                                                                            '20210203:180445.221517:+0000',
                                                                            '20210203:180445.221522:+0000',
                                                                            '20210203:180445.221526:+0000',
                                                                            '20210203:180445.221531:+0000',
                                                                            '20210203:180445.221535:+0000',
                                                                            '20210203:180445.221540:+0000',
                                                                            '20210203:180445.221545:+0000',
                                                                            '20210203:180445.221549:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǲӓΌĈ°ʩÔҸѷўȁȵΑО˔ȃȥĥÓђŒЭҽǸЩýӱИ\x85Ǔ',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӟ<ҠȨ\u038dг9ǀЏWļǨУҫwʗʼTčːӉεȨĄΙдʴ\x99ťź',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': 'ąҀȗӢƅǜλÙԡ\x91ǥűτѽȹųƕ\x8aĆӎʵ®³ңşĦKʋśA',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'čχсćʑӄɥȜѺˈʉɺ\x9cȪѩѡƜŨԉиİ˲ҋʽõ\u03787ƕ\u0378Ó',
                                                                            '²\x90¢МɑƻӭƀȕϒӼȞӦÎɤsǽФČ˓ɪʼtzυ·óƔ\x91ũ',
                                                                            'ƱΩιĽÏѪˎсǏӅśȝεȟǻɹŨS˝ЯщϪјҨŌʟȧѲҧͻ',
                                                                            'ūȅȥәт\x90ѝĄŋӹоϟ÷ʅΤĽҡqˁɭӊùÖʭċʚƛɪΌͲ',
                                                                            '˧ǜҏ\\ӤûBśΊєж˼ɼ˓ʅ\x9bӜǔ/ͱXÂɱ˅ϲɫӏĘϛW',
                                                                            '©ğƵơ\x95ŒÏcAжӻǾӣSϣϒƀ\xa0\u0382ĤϷʸÇĢwǡςҡӦȌ',
                                                                            'ǐӓ¢ώĨԀ͵ǘŜӑuʃνʖŦυ˞Ο˪єʎȁԑѫǱωьҡǇD',
                                                                            'ӢӼÏĒȰȊ\x80Ҍ\x9aǰɿĦБgЖ˅9ǼШг҃ˇ²ŗȽʷƱϧщ˕',
                                                                            "ɛϻԬϭǣ\u038bŀҪū˨©,ǩӜҿŝ¢ǆԣͲѾ˩Ą\u0383'ЦsΎχԔ",
                                                                            'ˤҸѾˉƕƐŪίнɽǛǵҿ¯ĴɺЯOԉĨѕӲɅ\x8dϵªӯŸƹπ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȴòԜҠʼӐ}Ņ6˔i҈ɢL',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7656445468551470364,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʺ´Ăvɕ˓\x8býԓňġǎѻњʢüǮҧӍҴε\x95ɔǰſ\x84Ȳʨć«',
                    'message': '҃½҉\x88ʀɗȆΌʲŨƞȤżȭȦƾŊљΣ×ФnԣԧɃȘʳÀĝӬ',
                    'arguments': [
                            {
                                        'name': 'ϼŅʏƖЊͿїɠ\xa0AϭӳÊˆĲŧ\x8a1üđҮĐѦ8ʯĭ\x97ąʧӗ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɦɖ\u0379ЊϘűƕÿŠeȨ·ˢɑΚӏŖ[Ŗʊɨđš·\u038d\x97ίʀέU',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǨӑӈˣѴӸǗмAØʅȝěˤΏӜжſяļɡϜȜ˓ȁʈԫɗȋĞ',
                                                    },
                                    },
                            {
                                        'name': 'ѩp\x83ȁɧԃϓǴΠ~һȑ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6920802764629075439,
                                                    },
                                    },
                            {
                                        'name': 'ӽɡ˰ʙƽѴǽϞΓő',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:180445.223463:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϜȡR·åßɎǌòĚ=rɞǞʶ҂ИϯжѼƂŰΰЯ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            420507.68745574175,
                                                                            518412.20037063095,
                                                                            541849.730388944,
                                                                            -98628.26494281135,
                                                                            381671.1244040697,
                                                                            758732.7614553133,
                                                                            158977.40440539844,
                                                                            242750.5196860988,
                                                                            668923.1051275289,
                                                                            423780.87039976043,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӈȥøŕиŋʺ(ÄɊјƉпмƔӷοŅԦß6ÍȰЅЭƅÂҊǂǱ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:180445.223828:+0000',
                                                                            '20210203:180445.223838:+0000',
                                                                            '20210203:180445.223844:+0000',
                                                                            '20210203:180445.223849:+0000',
                                                                            '20210203:180445.223853:+0000',
                                                                            '20210203:180445.223858:+0000',
                                                                            '20210203:180445.223862:+0000',
                                                                            '20210203:180445.223867:+0000',
                                                                            '20210203:180445.223871:+0000',
                                                                            '20210203:180445.223876:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĵHɂѹûeĻÏһɻԈФǤԣ˻©щ˘Ș˺ҍΙʭв=SéɔͶȁ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:180445.224094:+0000',
                                                                            '20210203:180445.224102:+0000',
                                                                            '20210203:180445.224107:+0000',
                                                                            '20210203:180445.224111:+0000',
                                                                            '20210203:180445.224116:+0000',
                                                                            '20210203:180445.224121:+0000',
                                                                            '20210203:180445.224125:+0000',
                                                                            '20210203:180445.224130:+0000',
                                                                            '20210203:180445.224134:+0000',
                                                                            '20210203:180445.224139:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ү\u0381ΗȋǰҐ\u038dƑʼx£ԒӨԄѹǡѥƌёЊʋ(\x8aǢѼ\x94',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɜŎԥцгIɰɅͷμľ҉҈жŸƴ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8557729631399977597,
                                                                            -7571616269363960412,
                                                                            2730778650466880622,
                                                                            -5926090982716913748,
                                                                            -401541100672516770,
                                                                            -2283585756344892016,
                                                                            -2832397532694598309,
                                                                            -8672908810313123213,
                                                                            7594043742944185272,
                                                                            7155725550943773224,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ºϟɞʤǙӨȁʭ\x9dάӕɧƥҚˤљǡĠʹǊ˹ӶɟŬŧȑʄñӓò',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2036925495249753240,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': ',QвǺίФϞӂҰǛɷƀӹ\x95MІ,Ǽ¦ԅěPӃѲĢӡƱɆʸӧ',
                    'message': 'ċńǥԅҞΉǷːɇӃͺĹŦƾɽTȔβѰԙħʩϛɧąԥј˜ɏȠ',
                    'arguments': [
                            {
                                        'name': 'ΤҖpҧΒǡƁΏDƸӮɜһж˴%ˣƢίωʪΚƋΫ˶ÁʟӺҽӦ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Dӓԭ\x84ɌĄΟ5ȨϸúƜǈԡ҈ϛΉӛƹ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:180445.225251:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ě˝\x8dˎѕȾϳПģ˅LsĉʺомΚäԈȼ¥G˨ȺǅΡŁΪΥЍ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4979472235667356909,
                                                                            4231383299993416865,
                                                                            -7599512121277800920,
                                                                            -5341572226749342821,
                                                                            -5606613616979255147,
                                                                            -1017885482038049760,
                                                                            7431151390370300640,
                                                                            -414930967793459333,
                                                                            -1399599386772854682,
                                                                            -2234296401974448539,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǺǷƲПͻȫϧԉԧŋѷŞΊ˼Ǝ¢ҖƢϯ3χӲǅяɜ&ӝ˱ɝï',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:180445.225660:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Њ˭ȺЂШћωɩƫϾҳәưњĸƧϩɈДɌʫϙq×ҬԞȔΕʱȿ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            432204.9187935733,
                                                                            838177.9290355005,
                                                                            201427.41210201674,
                                                                            444311.0339685364,
                                                                            432726.1890616487,
                                                                            993010.1048410984,
                                                                            889832.142180966,
                                                                            12843.344666675373,
                                                                            339063.83012017614,
                                                                            224124.51451304712,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӷȳƎɪǴǴϻщMŹǏ˪]\x8bтɽˬąȇŜȥüίǸGϜ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            116129.39915967948,
                                                                            58182.13533724265,
                                                                            212906.86566139804,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŉY˵ɷ҉Ȉǲ¶)ԝŃ˶;ɕǨҼ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 154647.24325733102,
                                                    },
                                    },
                            {
                                        'name': 'ΑȲƑǐȢ˅',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ϲͱ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʍÉƢlɖŶԕϪҏӳȹ\x9bȱʛřʳdѝKϝÚQӑöҸрŪҧ§қ',
                                                    },
                                    },
                            {
                                        'name': 'ϗԤέƛɡƅЄԀġɧҡͿ\u03a2ԪˍǦÖЂмėЋɿÄǊʸӬԏ³¼Þ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -58481.12731241025,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȦΫÎ·φȩĖɯʆǄɄŕʬԒԙԣΦƄΒͷБʒϱӰő˧ǒҿƌӠ',
                    'message': 'ȵȼİ;+\x8cҫĞοɅġƯ\u0382Ǣʀ\x9bɝ²ӈ҆ŽƦ˹ķƩ҈ÎЖÂӤ',
                    'arguments': [
                            {
                                        'name': 'īԞ[˶ѩ]ɦр\u0380ȥPˁЍΔʥ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            7232.362532429208,
                                                                            167166.66167908575,
                                                                            27153.018302826342,
                                                                            157675.60491775896,
                                                                            845439.4855481636,
                                                                            481033.7830073477,
                                                                            156223.32187897665,
                                                                            221418.26882671384,
                                                                            483754.87292460154,
                                                                            364322.2870495617,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ņҘŕBϵКtȯѫĒԮԡ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:180445.227165:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҬЄäӭСЩƪɇƚțǓćҼɦєοҒЯԏδϾŎ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1673184622486849579,
                                                                            4168909647966907531,
                                                                            3339985074901996303,
                                                                            -6035130043154821716,
                                                                            6716033292421079036,
                                                                            -7355689831103391939,
                                                                            -6152011033716354273,
                                                                            4689689535885703968,
                                                                            6664301458019719998,
                                                                            831065334381018692,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʹV\x94ɕÄðθΌĘcʬʤǟ{ўʶЌɣЋJʇ˧ĴɽN',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4993067965777287048,
                                                                            -5937319284451933520,
                                                                            1814566456850975201,
                                                                            -3446346886980279974,
                                                                            -762720764470807244,
                                                                            -7196511957428046881,
                                                                            5243661227965112574,
                                                                            -1670263093624756671,
                                                                            -9126947825898320946,
                                                                            704392562352265038,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӹ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ûʹ/ΰȞ΄ȈҪăƒ®',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -683617410195693544,
                                                                            -3771617806953042675,
                                                                            8488235485305698922,
                                                                            7570092766824197119,
                                                                            6889692311139473837,
                                                                            -3042110185455279301,
                                                                            4722145366056542022,
                                                                            1730003544074859772,
                                                                            -6510438568006025500,
                                                                            -6467013798188064368,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˃ęˎʁʨȳǃΌ¹ƝƌɜҤ`TлӉԕǵАĎԪϵͼųƣ˖Ñ\x98п',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1172057475051999476,
                                                    },
                                    },
                            {
                                        'name': 'Ӂĵ˷ΊҘϢĊͳ\x81ƜŻiӪ\x96\x7fȁμaӁѩƖȦ¨ӏʁ˭uʹςɱ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'ªɘ$ԋ\x81ÌCÖȫЉΜ\u0382їȾŠ´ˆѺҌBÃѢsӨ§µŶɟӥԔ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϡǉAԕ&ŴԂҵҶȡʝŘƚɾΙɖќĊѦȖǛɺӬÈрmȌųŻϩ',
                                                    },
                                    },
                            {
                                        'name': 'ÑʻʧԗǝǣӁťŰԍcŜfƯʆҥhȬϡØΥ ƮƹӳĴìĮӨɣ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2838021344063569134,
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

            'scope': 'debug',

            'messages': [
                {
                    'catalog': 'ɛ\x86',
                    'message': 'ђ',
                },
            ],

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
                res = logging.Error.parse_data(test_data)
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
                res = logging.Error.parse_data(test_data)
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
            'identifier': '\x82\x82Џɞ;ΎϑʘϏѴ¾λάӧ˲ϔсʇãͳʣəςԅwӬȼͶȚA',
            'categories': [
                'access-restriction',
                'configuration',
                'network',
                'invalid-user-action',
                'access-restriction',
                'access-restriction',
                'invalid-user-action',
                'invalid-user-action',
                'invalid-user-action',
                'access-restriction',
            ],
            'source': 'ˏʂКðӌЯуȆͱƗϻȀӪ¶ëãʇĂ˩ҪӃƈβπԃʆʝ;ŠΕ',
            'corrective_action': {
                'catalog': 'ʃӃΌϏҚʙ\x80ßǡȅɸ\x91ˬПӟӕ\x9eɓYӞʿQ\x9cĢ˳ˮƴz\x89Y',
                'message': '˜ҹπɇсϐǤǗѢІK҆Ăɞ҇қЮΈӧӥȊѮÚпӏϗÐΫØɃ',
                'arguments': [
                    {
                            'name': "ȝ1ӃɕӣôѼˏ/ԉӔˀHʅĹҡʖǒV|шĐıӹƿԌğ\x81'Ƀ",
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        2652278100446619559,
                                                        850893486947401216,
                                                        7645278663932594571,
                                                        -3110685528419760493,
                                                        7052708611557127978,
                                                        -1539410738795697991,
                                                        -2870583802604224095,
                                                        2426739085807969786,
                                                        20307432196798037,
                                                        -59130576952431007,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ëВӔԝĲр˪Pϱ·ϢʝӎȺšʖ\x9bº\x9b˞ǥÏїгʒưϣˈŤӮ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        882663763898336891,
                                                        -3591890132102124185,
                                                        -4783250951465724592,
                                                        -3902724411880376258,
                                                        -4082812139291229237,
                                                        2468820660099291070,
                                                        -4993849333561217341,
                                                        -3670460843230315044,
                                                        -6057403193852534999,
                                                        1313495907681342477,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʴvЊġ¬ҶȔԟàǛϵǗ\u0379B$\x98Ϥʹ',
                            'value': {
                                        '^': 'int',
                                        '$': -2129246347775923418,
                                    },
                        },
                    {
                            'name': '\x87ϣ˽VңӴάβηpѡȄ˪Ɉ«ȒɩƄņ˝Ù˔Ǟķ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'һȨėӊƔΗӬԇǧ\x9bðŵ \u038bӗʌіù҈ѬѱȶȬʭµʮȀɿȇN',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210203:180445.239966:+0000',
                                    },
                        },
                    {
                            'name': 'Ǌȅ϶ԞǣǊĆЏʧѼН®ώ\x9aЋʜѦԄĘыGɀùœĎČΏMΔ˱',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -6956194027309469491,
                                                        1780967327433610096,
                                                        -367543265190247341,
                                                        7548667712259479476,
                                                        7658231778583269670,
                                                        -4483801824961504243,
                                                        -2196752474200289103,
                                                        -2349398592924446486,
                                                        -3480091991445338732,
                                                        -4167375667384010627,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ϗȜśеÈ³ǼVǿǼѹɍɭϻi˼\x95ҸŏЃʿˊȚÙдʈ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210203:180445.240373:+0000',
                                                        '20210203:180445.240383:+0000',
                                                        '20210203:180445.240389:+0000',
                                                        '20210203:180445.240394:+0000',
                                                        '20210203:180445.240399:+0000',
                                                        '20210203:180445.240404:+0000',
                                                        '20210203:180445.240409:+0000',
                                                        '20210203:180445.240413:+0000',
                                                        '20210203:180445.240418:+0000',
                                                        '20210203:180445.240423:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ɺϻϙӧ\\ЖЃ&ǐŪϷϐNȽӔɪҝΏʂǵҺӕсkÔÊ/nʡк',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        7976545522838527968,
                                                        -927919752113371931,
                                                        2239528371945825981,
                                                        8141526703774963824,
                                                        -8331675956454126795,
                                                        -8377177999055576557,
                                                        5536108862852525933,
                                                        8509577410296332410,
                                                        -8662797696823548884,
                                                        7418204907373548418,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ҏØӢțέǮɏѡêƃ¨щӪƝԀ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ҍϲȯȶǘʖɵ\x99ńˠʟ\xadŠ҂ҋȝҗƥ\x84ȢԉʪԈǶɟEƷȝ˰Ƈ',
                                                        'ϯҙ\x8cǫўьҥĬЛȐΗʺёLɛļԮҘƩ˼Ϋ»bΉһǖ\u038bҮ\x9bǝ',
                                                        'Ʈʌ\u0379ʁ¸\x86ʦԅ˳ҁ]ɇʓ˴ȞƛːàвξҽʕҟԟпҹЌȼĿȑ',
                                                        'щҺɔʹəʐԂƿģэϮΕĝƟ!ŭΔŜɪ»ѻ\x8aαūh\u0379*Мӣ8',
                                                        'ІʆʂԊŔԉà\x8cÚ(ŋӤʅƄƎԈ©ÓԄȓҩáƨñΐΘΣФμ\x87',
                                                        '¼ȷȸœӻФԮòΤÅԛ^ȐʭэҤшçȤЫǏĨĴĆv0žŬПĶ',
                                                        'ŔƜțưƫ˳ʘ\u0378ҔԬҡʔǣҢɬ˥ʊД˸XϺүӉȅŋƑцŖϱï',
                                                        'ԌɧΥɫ:·ɷԚԦȼԘ\x97ƎȲΙυƫʱɛĎzĔǀɈθĹƽđӜύ',
                                                        'ʼ˝кdŘ\x8dȴöӔЍ¬\x7fƁъԗăԃӅΉĴ΅ʧЂɼʒNŕӓÅж',
                                                        'ɅʔȍйѐΠĕǵ\x81RΥŋѡưȯ\x8aʤ0öвίƶƒ5ǇʷɑTӺȐ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ȹɃϨĲӿȞ0Җ˦\u03a2\u0382˨ʶϚɨ¿ԀҘрɬŁ',
                            'value': {
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
                                                        True,
                                                    ],
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'Ƶ$ŷȂϘħІ҂ȇʎŸɼůѝŢʹŭȚëʍğʳʅԦĈɘЋġҁǿ',
                'message': 'DʳďϸµǖȦӂCӪςÈͶÏӰϯȥԊʵȾƙǶȊʽʹǄƷ\\ɝД',
                'arguments': [
                    {
                            'name': 'ЦɀТ4ɶÅáЉѠЀ\xa0ɩүԅϒǰĥʹʋŞŦ¥oǺϫқξʜ\x7fã',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -4681826836660693734,
                                                        -1654533693949665854,
                                                        -3161368551906696253,
                                                        1453220458859224383,
                                                        -1860613640814392503,
                                                        -8639412847865281657,
                                                        8718104771953987001,
                                                        5479466509523266027,
                                                        945290764093280300,
                                                        9189140194589793180,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ƣСŇ;}ϝɴϐєºōҖƻҍʯˎѰǪȝĪϊń(àˠɃúԤҡЗ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210203:180445.242251:+0000',
                                                        '20210203:180445.242261:+0000',
                                                        '20210203:180445.242268:+0000',
                                                        '20210203:180445.242273:+0000',
                                                        '20210203:180445.242278:+0000',
                                                        '20210203:180445.242283:+0000',
                                                        '20210203:180445.242288:+0000',
                                                        '20210203:180445.242292:+0000',
                                                        '20210203:180445.242297:+0000',
                                                        '20210203:180445.242302:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ŕǹҧøԟδňвɣªǄԧӂè³@×˔ɨΎzƔļŢ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ҁЛˡδƷç1eĵ˥ǩĊІƣ\x9dřɉ¾=ʾʱϧϬȨʴѵ\x88ӳє¿',
                                    },
                        },
                    {
                            'name': 'ԊјЪϬƵĜӫӯƃЎҨħпЋ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ʕԆԔ˸ʗöŜţБҠïǈðЇЎҾҀbљțĝҀңҹȫĸM',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210203:180445.242825:+0000',
                                                        '20210203:180445.242835:+0000',
                                                        '20210203:180445.242841:+0000',
                                                        '20210203:180445.242846:+0000',
                                                        '20210203:180445.242851:+0000',
                                                        '20210203:180445.242856:+0000',
                                                        '20210203:180445.242861:+0000',
                                                        '20210203:180445.242866:+0000',
                                                        '20210203:180445.242870:+0000',
                                                        '20210203:180445.242875:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'nϟӋФЗҌʅΖʅÁɔ˯ʴQԜϧϥũІЌƅŀÂƺäˣǚwҮȥ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ªϳɝĳř',

            'categories': [
                'internal',
            ],

            'error_message': {
                'catalog': 'ȮϚ',
                'message': 'F',
            },

        },
    ),
]


class SystemErrorEventTest(unittest.TestCase):
    """
    Tests for SystemErrorEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SYSTEM_ERROR_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.SystemErrorEvent.parse_data(test_data)
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
        for test_name, test_data in SYSTEM_ERROR_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.SystemErrorEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SYSTEM_ERROR_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='SystemErrorEvent'),
            ),

        ),
    ),

]


SYSTEM_ERROR_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'error': {
                'identifier': 'Ƹ²ɚ7&МгҵиυżԦԊˆĊȋϩϬɲѤíʀʭɧTZɶĦ\x94Ѡ',
                'categories': [
                    'os',
                    'network',
                    'access-restriction',
                    'access-restriction',
                    'invalid-user-action',
                    'internal',
                    'os',
                    'invalid-user-action',
                    'access-restriction',
                    'configuration',
                ],
                'source': 'ǵȥŊͶȣʑϋzƣı@ǦņĹн-ķĮ\u0382ǱӻϿ;ɢѹɂŤыƙŗ',
                'corrective_action': {
                    'catalog': '˧˙ȥZԫsÕǸ˫ҀΤԆȔӲͳʤԊ\u0383Ѧǘ˗`ыӼ>ϚԈӥȲȩ',
                    'message': '5éž\x89ѽȩӊΨЦɻҍʌǊӷғʲǦǴXXȓã˃ýǐȑϜʷ\x88\xa0',
                    'arguments': [
                            {
                                        'name': 'ІґūϋɇғɯυԎɝʱ˯Ȕǵŏɥ˝»ƇúԤƏѶǏ}\x8e>,Ƣҝ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɧɹɭ˳ԧЈsŜϧϽтǓf\x89Ì~ćǓŮjĉƇɂÒБчĽ~ȦĎ',
                                                    },
                                    },
                            {
                                        'name': 'ѐÙϑԣяȾƐӈϰűȂÊʟΜ\x91ƗȪˊőˉ',
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
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˉҨѧԐɲ˹ƉʌПɻ˗åŷѓƼXHʗ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            262246.3233089974,
                                                                            950037.0583576111,
                                                                            564711.6642766981,
                                                                            130806.87558930102,
                                                                            788721.228212604,
                                                                            81062.29180899088,
                                                                            405602.08107964677,
                                                                            862835.6012473858,
                                                                            986099.293174956,
                                                                            701967.03026483,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɹЕȦÒԡԃǔҹӺπԧȕΧңÂΞ&ΛӦ\u0378ӽӸǐµDҺȭѓ҅Ɩ',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˪ĪȧéҹԇҐɌɏӷƋɵɷЛ˪"ԑэķĥNǉ3',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɝɸĜоĂùÎɭМï˴аÐԙɘ}wӘӨʯşƶƟƾ˚ƦӪϕÊƙ',
                                                    },
                                    },
                            {
                                        'name': 'ǢͿŸƓ\x8eŷѳ҈à)Ͳâś+ÒΌǓ1ђ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Оʵ˺ĎΘkĩĺ˳ѪҩȡƆǎȗŉΦõtƃφɤϪ\x80ˏƻļӹɬ˝',
                                                                            'ŝȄHƓšćØŲZˤɵǭēԟuԠȺҷ\u038d˶ʵƳčǳʦΨԅΘ˷ͼ',
                                                                            'Sɐƕέг\x8eǿ\xadjǸ˗Λãʃχˠ΄ȤæMВǈϳҝ[ƟҋÄ\x9dØ',
                                                                            'Ŝ˗ǭԁÖ˻=θԀ˚ӕцϦïΪƶΧϬѸӥʱĹ®ˈЕМЋĿƲĎ',
                                                                            'ęэʍ҈χӐӥϪƺǆȡɂʼϱ˶˨WҠΣȽцŉԬŔ\x95Ďχłˍӥ',
                                                                            'ŞʐТ΅ɃƣмϲӺϡЌƔҠǏлǽΦ#ȃԞáyâ˶ԟɴŀ϶ɏͲ',
                                                                            'ÜǌЬϏӢȟоъҌFǧѮŉǆͿƣнóŧȒϗüǦȬѱƌˠ҉\x83ͳ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҾѨѓ\x97ƮƜѰȀđ\x8bĹ\x9cƣϣȳĊҙ˩@ʹ˜҅ɾhѹӄԢԧʄԦ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:180445.235211:+0000',
                                                                            '20210203:180445.235294:+0000',
                                                                            '20210203:180445.235301:+0000',
                                                                            '20210203:180445.235306:+0000',
                                                                            '20210203:180445.235311:+0000',
                                                                            '20210203:180445.235315:+0000',
                                                                            '20210203:180445.235320:+0000',
                                                                            '20210203:180445.235339:+0000',
                                                                            '20210203:180445.235343:+0000',
                                                                            '20210203:180445.235348:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'εLǲѰхďØķƿѡÖ\u0381ΥӅ@ΐĂЖȒѬǥϦӭӾ<ƕϽԚʦÍ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ШÕãʰɠ_БʁӲŦϐʸ{ƸвϓȖӫʦ¥ť\x95˺Ш\x89ÜʷɞҪ҈',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǳǛƵђЃƤϸНɂʴQˋѦΔćé;ʫήв',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -792761905725084448,
                                                                            675725862317637374,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ԓЋ҅аŷӁ\x9fěΨˠҕѾÔϋ3ƟвѿƙÇҰƀo³ϾϥˁԉĠ|',
                    'message': 'ȖɷӋŻʴѥȠǚηУηʛȪѰ˹˥ƹÐɻԋžǳ^Ƙɐϖē¾ƿƎ',
                    'arguments': [
                            {
                                        'name': 'ˣɻ˂¸ӢεƹļēʰρŘ\x9cчѲȓОԧӭƋɗГ҈ҢG',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 153335.49298400516,
                                                    },
                                    },
                            {
                                        'name': '\x9f\x87ŃΕ%ɚ¸ȽʁI¹ŷӌеԈӫҧгuΖďϻӛљѮz¿sˬЊ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 225954.78577714873,
                                                    },
                                    },
                            {
                                        'name': 'ėȵϝŻůЖϡүʵʋ\x84',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŠԞĿçӽʦ6ȕ1ϲNʬЋҧѓ˅҆ӑԀТșƬƢһƯºѦ}Ҿ°',
                                                                            'Ûʕ˻ϳɉȰʳͻтҕŁʣƭϬυ\x8dìóρѺŀȡԣĭ\x82ůԆѧшӭ',
                                                                            'ŨÊӁǍȿŉȺǌõӪɅӞɮȅȉҫсʈÈYʸδщRШЫҍɌɌ~',
                                                                            '˅ʝѐƫ¸ȲúүҷМȏґσǱϕ°ĽЦƩĸ\x9fßâɇҿǯɭļСԢ',
                                                                            'ƕĄЗȵ\u03a2ɰДάëγϲԙĵ˅%ҧͳɅѢɈҜ\x9eԘǩ>ЙЭƎʆŕ',
                                                                            '~\x94ӼƑԮǌϪɋƼɜΐΠʜćҁЌξĈƭ¸ϔÎÎȥԓԂ˽ϐŰȋ',
                                                                            'ΐŭҋǵǽǎȄ\x9bŞԫЯʃʅ¯ǣћ˼њάƳʋɔ\x84ǁԊʮ¸tCj',
                                                                            'βœςåԝČʁƞɈĊȺ·ŕчάɖȼϸǅ"ѶƈƐϊǂȲО\xa0νǼ',
                                                                            'ԍ\xa0´ƈѾȼЊǁ÷ƕǄɾõԦνΕjϝɖвѢ\x92ūӴɄʫǊЅ҇ľ',
                                                                            'ñΟԓˣǷǡʧѪŬŴέŹǲ\\ʾVѿƿѺАȕϗϡϿӐȍaѨҧϵ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȗǻҵÒ˕ʥӹҠȟ˪Ҽӛǒ.ȨѼʙѠʈ°ϝώ¤ӄÒԒ¼ǆԒŐ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'п0ˣȖȻѴŴЋУҔǗˑʃ?®ɮԭhˌĥ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ɠż\u03a2ΐȬ¥ïνΣЬӆĻŎΒ\x8cµїжӠńǘϙӹҡѕϟđԇ+6',
                                                    },
                                    },
                            {
                                        'name': 'Œǈ\x84ԜřžȀT\x93ӓƮƆͺʿˊӢņˀʞӿħˢıʊƎ4ʧ\x84ɕǚ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĠðŘʚ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҡϿ˃ѦӦėΰÜУ\x80ɽǗѨќҰ¡ɺȯqƹąԨʓɏȢ7ź\x8aˇĉ',
                                                                            'Қlğǚԣγӡ˺ɺ˥ŜТȒȳш4ԐӆԇҪѫϘƪϨԓԚ\x86ǃ\x96ĸ',
                                                                            'Ĺʣ»хЊƶѨɇĐȹǆɉǿœȐċŰʑ¥ŗŪɮӧëόƀ¨ųːĕ',
                                                                            'ǧьФӖ%ϮжӐÜƇѨ˻Ӟ˱зʦǍʚµŠȖȑ˝ˌɗǏјяΖα',
                                                                            'ҙӶҽ\u0379Ņƚ3ʢҾˏH˞ʞ0Ѭ0ʁǖѓ|ԓȈ\x86˥ӑÊaʒɰԘ',
                                                                            '˽ʍϐš˖ŞĀҳɈ¶әǓ@ŒÞʛȮˎ-ìŹψ˙ӑԭҴðéÙĵ',
                                                                            'ҰʷǮѾҋԧˮЌʆŉƾԄʒÙĎǤɁэӯҧͷ\x83õƢ\u038d˟ʶĶԢʏ',
                                                                            'ŷɿŷќ˯ӜɍķŠɨϠʜςȿąȮęӬǋʶŀǥѿǭțǸƐхѦČ',
                                                                            'Űˋ|χȽϥ˨ĨѶёˑʲԍЄĴƥѻÿВЛЯʏȳȔǏɁѝ4ыҥ',
                                                                            'ʄԜӨÊο\u0378mʮÑґϣ&ʴ\x86˲ѡȔŮbºӦǭƑѴ\x83Үª9\x99ҝ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȩą^ӓлɄǄʊřŮπԀ҄˫ӧ͵¢Ґ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:180445.237896:+0000',
                                                    },
                                    },
                            {
                                        'name': 'аȔүΥKɼŲmǤҖíŇµ˻',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 372888.2298794896,
                                                    },
                                    },
                            {
                                        'name': 'ІĈČģϜ˼ĊӲ&őɼήɯҧЄƅ\x80ӈ\u0381ΆɺцҰʉѢҳċӶś˾',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:180445.238142:+0000',
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
                'identifier': 'ȩ[ώÙĕ',
                'categories': [
                    'configuration',
                ],
                'error_message': {
                    'catalog': 'Ԥƅ',
                    'message': 'ƅ',
                },
            },

        },
    ),
]


class UserErrorEventTest(unittest.TestCase):
    """
    Tests for UserErrorEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in USER_ERROR_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.UserErrorEvent.parse_data(test_data)
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
        for test_name, test_data in USER_ERROR_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.UserErrorEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


USER_ERROR_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='user_error', name='UserErrorEvent'),
            ),

        ),
    ),

]


USER_ERROR_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'user_error': {
                'identifier': '΄ЈŦϰԦԋǢ\x8c1\u0378ƋɹЌѵĀĴίʰӪʕњÔȑƹPЩ˻ҩŽȇ',
                'categories': [
                    'invalid-user-action',
                    'invalid-user-action',
                    'internal',
                    'access-restriction',
                    'configuration',
                    'network',
                    'internal',
                    'configuration',
                    'internal',
                    'configuration',
                ],
                'source': '¤ʭόɥѕ˽ȥȲԣǅ˦ǦƊċΫ˚ɩǡЃʺ˧ҚʱʫЁŜ\x9fȱӪǼ',
                'corrective_action': {
                    'catalog': ';˥ʭʞԕǓ§\x8bměÂŁοatҹÂŢˊЕʗϊǻӂɐӈ҅ɟЦħ',
                    'message': 'έưҢǇľ_ƨêŒĬřΩʄˉ\x95ο\x80ЄîøϨХŲǡƩș\x9cӆnɍ',
                    'arguments': [
                            {
                                        'name': 'ЏðпɪʕǏ˳',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:180445.243782:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҘШǚϪÇйпv˨ЀԢɬѴŬʤЋԚʍˈ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 290646.56445216865,
                                                    },
                                    },
                            {
                                        'name': 'ǞӂHƥϰ\x86ҜʒȱŁ\x8cϪâȨϴmԤҏŕÕφϏÊΪӧÁ\u0382Ԡ¢˓',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            421930.4703526537,
                                                                            290675.8854051798,
                                                                            525716.63515593,
                                                                            524103.4002621252,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŗƣϦ˙ĩƃőϳǾƮɗıƹŊɨɜұÎ\x99ȒϹϗÏĎŋЃυǀҚȬ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2598915725555413630,
                                                                            7281932162387056693,
                                                                            1009642655964288787,
                                                                            4000178517210283047,
                                                                            8796799396179803716,
                                                                            -2629161501934428468,
                                                                            6384291854308080247,
                                                                            5468628414270284326,
                                                                            6921883776011388779,
                                                                            -1496020039613126775,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЬˎԒĩŰ=ԅϠԁ@ǊǴçԀˡȜʩέόǼΖĿʮϗɌɏɑϯ~Ġ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': '\x84ĮřԆϽϣ·ȘʧƗĦѣ˾ŜʲүϥÝϭĐˊ^ҐѿɚͰӊʐοϠ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -863025352535182876,
                                                    },
                                    },
                            {
                                        'name': '£ˋôÁ}҃ʙϞʖЯ\x8cÜǠżʁǱԧƽRŜβҡӌˌæ[ӨӞˏ=',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˧ԘЂɎŏř ˑԡũʈʪČӼƬ\x83д8ȈдƜ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4500360395453189364,
                                                    },
                                    },
                            {
                                        'name': 'Ȯć7ӘҫIӀԏħăɉȳƻǴƯЖ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -35885.88748022352,
                                                    },
                                    },
                            {
                                        'name': 'ѮƪԠНϘ^',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
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
                        ],
                },
                'error_message': {
                    'catalog': 'ɹ³ÆȑZԃӼˁ˞ѥĦΒɷȕǀуѐļ¼Ȍ\x9bƭЎѼӼśĔƔ',
                    'message': 'óŋˡąΪδҜȈ΄ӖŃӽƣ.Ϛġ˼мȚȄȈӧԦƣeͲ6\x93ȿķ',
                    'arguments': [
                            {
                                        'name': '°ȉɑķŬɲįʫϝҾ=',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4033959620769596901,
                                                    },
                                    },
                            {
                                        'name': 'ԛÕϝǥԮHǀӼƹǐʅŴhɯӰӯ\x9c˰Ώ',
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
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ξ]ЁoǌPŪˤÀѠ_ϰѓ\x86ĆӥƝχ\x8eκčȝÔcӬ˙дɆMɋ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:180445.246323:+0000',
                                                                            '20210203:180445.246338:+0000',
                                                                            '20210203:180445.246344:+0000',
                                                                            '20210203:180445.246349:+0000',
                                                                            '20210203:180445.246353:+0000',
                                                                            '20210203:180445.246357:+0000',
                                                                            '20210203:180445.246362:+0000',
                                                                            '20210203:180445.246366:+0000',
                                                                            '20210203:180445.246370:+0000',
                                                                            '20210203:180445.246375:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ąSҰ҃ӾүǾ¥ƹʱ˵h@y6ȇҦӏŤƖɥҗɱѶΎf&ӓβѠ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ǔȩʊ¸Ͷæԁ϶ȩɣ\u0380ӱӫбљǱsҠo\x84¦țō\x91ӑαύ¢Θƕ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'ɚǲƗʕʒӵĲФ¯ãЃԥ¦£ԏË',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӀӧƌϰİϓŦƨѴґßǵˁΪѥвʓӓ϶ͼŲҴu¹ǵʪuЯѤш',
                                                                            'ȒͿϲƐԮƙҭ\x87cԦ҂ĩЬЌо6ŉӲʀúǤΛί/ԂʱӒӜϗɟ',
                                                                            '(Ⱦũξӥјæɀуұѭ˵Ƶ˞ʼˉ2Ɣʇ\x8bɵȈǊȕʢ®ϕȫǝƨ',
                                                                            'ƕӋΌɟҦʭķǑΩʲΕӵ\x8bɋΞölÏԅʑ\u0383čƉƢγƟΤƾëˈ',
                                                                            'ȥ\x92ʊȐǡЬά{ƭǌѓѸΑPӎυӗ2ÕǮфРϧӀǚԕӢʿυӤ',
                                                                            '%ϳ³°ėʆøʊП˫ƾΎȾčєɷȧϛ<БίӊćȱͱńэҨѴф',
                                                                            'ʹ˩ҫŚΉϽȦʚeçʂ҄ϒÝћ\x8dԍӡΙџƦȰЏϏ˾Ѐǔȥ#ʷ',
                                                                            'ϟ҂юΕ\x97ʩΌÊŨ˓©Ŗɝҹˇůů\u038bƹĴȌԪӓʫȹÂúˏĠǦ',
                                                                            'ȰǶΘϗʋͱŝҬͳǟӑĂɖȭΪ&ʣγΟž˔δҖú˄żӣӜӜ҅',
                                                                            'ĪǄïɨȀӉ\x86ǍΜГ\x95ҥӨΗĂцǗśŀȆɃдϠRƺæȲ+ǐӮ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˒Ԣˍ<,ÃМ=ȭξˋϔП\u0378ȓЯēҔáƇ\u0378\x9dįíʰǉԖрøʛ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ρІԑџ\x9aº4ȴҺА¶і¼κϙӆЗϚƖˠņӪľȃÄĤˁшПɋ',
                                                                            'ϦÍÆUĝЧϱͳПǎ˅ѫɠЕѲ˂śѮɓǚΜԁEԎ\x83ӜӢԕéŝ',
                                                                            'Ξϵь˃Úȭԫќſɢ҂ϫˤ\x97Г˧ҪɌȰÚȣԪƜo\x81³ΚԞҽɫ',
                                                                            'н\u0382Ɗ¼ƖМgΘӼɑŌ҈ӲŜͽ˶йæΘԭʷ"ɺʂôќЕ\u038bѝБ',
                                                                            'ɴәȭŤЫ/АƙϩŃþРҖººҕ|ыĚχңЬŬӒȤˁ\x83ŮмŁ',
                                                                            'ȟ°ŝoˠĻĪ(Ȉ£ҟŭ\x9eҟ)ѢжԮĠĖǅź҆ǂïҖ\x98ĘѴʹ',
                                                                            'ғ÷Ƿǹ&¬˭сȔΦŤǺƗЭȿέͿíԧŊҧĦ^Х҉юâķǤ\x8e',
                                                                            'İǦ\x94ʣ¢PТ\u0378ʀ˰ѦÆΞƪҋÂЧÓíέԛÖmҕˀǂ!?ǓЧ',
                                                                            'ώϪÿѬƢϨƩˉơ˅ѼҴӅʴǇΣϓiƜȷǹÿӾϙƷÚьȪ\x9eɊ',
                                                                            'ȑ҄ѮԨΦλӛИФгҪ,Ņęġѳϔ\x9cѨÑΈΡѮϣΧ˲ЍλŨà',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˞цщŐƈõ͵˙ŉŲ\xa0űŎĐњʻɞRжːĂӄяĦњǪ²ԕɚW',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҧǼɄąñғȮΝ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5702766667340292142,
                                                    },
                                    },
                            {
                                        'name': 'ӏӢѤβȲӆĶũӷξҔϖβȇǸΒɥƃʓǂ4ϱŮóư³&;ψČ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -95649.13272378137,
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

            'user_error': {
                'identifier': 'ѧʵρϙҿ',
                'categories': [
                    'file',
                ],
                'error_message': {
                    'catalog': 'Ӏ˾',
                    'message': 'y',
                },
            },

        },
    ),
]


class GlobalLoggingStateTest(unittest.TestCase):
    """
    Tests for GlobalLoggingState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in GLOBAL_LOGGING_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.GlobalLoggingState.parse_data(test_data)
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
        for test_name, test_data in GLOBAL_LOGGING_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = logging.GlobalLoggingState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


GLOBAL_LOGGING_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='minimum_level', name='GlobalLoggingState'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='output_console', name='GlobalLoggingState'),
            ),

        ),
    ),

]


GLOBAL_LOGGING_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'minimum_level': 'debug',
            'output_file': 'ɴԡƑā.ơĴғ¯Ӥģ¥ӺæóeöȿĂźȟԌѕŤԝǸˈĭјŖ',
            'output_console': True,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'minimum_level': 'debug',

            'output_console': False,

        },
    ),
]
