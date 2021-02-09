# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-08T21:23:17.033755

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
            '$': '¼ϖîμѨϜǱǾŇѵ˘OϻĳFøȝ:ĀɤȖ\u038dЎȕϣ˲Ҳ\u0379Ȝ\x9b',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -1926791339120969879,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': -58203.6483710855,
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
            '$': '20210208:212316.911163:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ǏђϖЃњЊʸĳ\x997Ðѝ±зӒ$э$ȻԔÅЍ-ƱӴʏԂˬИɍ',
                'ϩȷԫɚʜҊǉʀ)ȲʸͲ˽ӷ¨ϵǳŞʇ˄ƜЗȪÄ¿Φ҃ɖǊˊ',
                'Ӎϝ˱ʡʀƻЃ(ʎ\x9cʕĜӼ3ČΛ\x98ɩЫ҅ŚӡʀΚЮƂɍȬŔԈ',
                'ԎĄżĬʬКтυԓҸʬĬʆZʄøԞîʇӵǐɎυôTȤǇ\x9d4Ӥ',
                'Ѧ\x93ŒӐә˚ԃťǝ˱ƹΙƳ¼þKģǺņѧʋҁΥӹƊӵҼɃt\\',
                'ъңЦ\x8eЀȌ\u0380ǎӓԧȆʍʦɘ³³êŅԇuǡɻɈöˍȽ˪ь¥ʨ',
                ',¯ȎʺƎdqÆą\x7fļˤԈɇɵтѠÃɘǈǍ҉ԔxɞưǳéƏҡ',
                'ϽΓɒ\x85ХȉԙʹƛDʾŰ˳ˊ˔ќ˴ȟōčшˆYɃ\x89Τλęɰʮ',
                'ˏÚύÜϔ{ԈŖĳѶĹɲĻΖ\x81ǧÓīкҥǹҔonˋșŞ§ϴҺ',
                'ɶǥɚҸǕ¼ΓˁӾʓѷΒϻ˾΅Ěϩ\x9fӏƔɿίѨFϠ´ΒҘыʖ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                4853473087731186650,
                7243308578284049722,
                -2960071159721954365,
                -730147885476991716,
                -1586339889376772283,
                -4898883365338012205,
                9210778965463769180,
                5344957180519872503,
                -7273627159039827215,
                -1895247688962532285,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                766624.3220939541,
                343116.80397234147,
                79857.88479731348,
                -24418.148217584705,
                -22116.54787079031,
                941587.7854572226,
                961323.3862341933,
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
                False,
                False,
                True,
                True,
                True,
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
                '20210208:212316.912137:+0000',
                '20210208:212316.912150:+0000',
                '20210208:212316.912157:+0000',
                '20210208:212316.912163:+0000',
                '20210208:212316.912169:+0000',
                '20210208:212316.912174:+0000',
                '20210208:212316.912180:+0000',
                '20210208:212316.912185:+0000',
                '20210208:212316.912190:+0000',
                '20210208:212316.912195:+0000',
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
            'name': 'юţɝ',
            'value': {
                '^': 'int',
                '$': -2871864353062645610,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ư',

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
            'catalog': 'ɤшƀUSЂҠƕџ˧ϿáԠǼʑэ·ƀÑ˓ǿΑǛҦĨτ˛҈ÔÒ',
            'message': 'яѲЖƫ\x9fҸŗϛþΘ¯ƑΥʮŬТш˕\x83\u03a2ʤ.ҖԀ8ϽѨ˄ʿĤ',
            'arguments': [
                {
                    'name': '¦ʍɺ\x93ƺǻÅÂ˧ʬÊUưŽ\x8c5Vɇ+',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ƺҰ˜ƲVYȾүǘ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ƗŦ\u0381\x84ŗ»øʲɯȪŦԫ~ǤЅXǬˤʛŰϟΗËϏ\x98˽ҥ˳ԡҺ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        '҈nӺȯҪÏÊă¶ĝŐЅhН>ҊЅʽ˴ВɪɁâˇȧӋӭΜЛԆ',
                                    ],
                        },
                },
                {
                    'name': 'Çүкм»ӣѯǇʛößǽӇЇǟ\x9cŸƬҁЧɴҪȂʡӸɘǯԟӾʠ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210208:212316.908151:+0000',
                                        '20210208:212316.908177:+0000',
                                        '20210208:212316.908183:+0000',
                                        '20210208:212316.908188:+0000',
                                        '20210208:212316.908193:+0000',
                                        '20210208:212316.908202:+0000',
                                        '20210208:212316.908213:+0000',
                                        '20210208:212316.908234:+0000',
                                        '20210208:212316.908245:+0000',
                                        '20210208:212316.908250:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ňϴԮʻÃʯʡ\x85ųԍʥέŒ\x9fЇȂ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        1069191660531504470,
                                        -7843041752386337541,
                                        -7648283811087759547,
                                        2391271644008667150,
                                        1645725589194089078,
                                        7093439042483835395,
                                        -5881353256886285273,
                                        6948480358782210271,
                                        -7468074455512518863,
                                        7123436541095282334,
                                    ],
                        },
                },
                {
                    'name': 'ò\x9aʝӊǇѼǯɌѹ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210208:212316.909152:+0000',
                        },
                },
                {
                    'name': 'ńӫҒƵѳҹɂзțԃĲǜΟɫ',
                    'value': {
                            '^': 'int',
                            '$': -1872210958746269500,
                        },
                },
                {
                    'name': 'ǣđ+e¥Ȯ',
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
                                        False,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ҧĘˬΤɇхү\x8f\x90òÖɡyǄѰöǿŭʉԧɁΦǽŁǞԞΜ',
                    'value': {
                            '^': 'float',
                            '$': 489676.6764793418,
                        },
                },
                {
                    'name': '˺mӎŦǢϺы\x84ǕѶΒʉŬөΰ\u038bӞǹ˖ȵӥŖĖ¸ªǠљˬȈӚ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ɖҮ',

            'message': 'Ǣ',

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
            'scope': 'debug',
            'messages': [
                {
                    'catalog': 'ǭƣԈΈԬʗȢЮѷȮþэЭϸεàʬʋȣņϞâԊȆҕŎȄïǛċ',
                    'message': 'ӋƷéщC˳~ѵҺ˫ƺǪ;ʖýΆӇʍ{ÒѮʑAɫƴНԘȂªʤ',
                    'arguments': [
                            {
                                        'name': 'ӳʥ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ͳQΓē˦ƘŹɷȸӵ_˩®βȷʒȟėԫҨŗ\x9cɷɔÈŔĆӚнΨ',
                                                    },
                                    },
                            {
                                        'name': '@ΏɆӽ<\x8cгɾǪ¶ƺыʯˮИѤƒ\x86ŗԢΆĴҾвѝԕѬѤƣƟ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4608283061510554814,
                                                                            986894320228001694,
                                                                            4827612863781921945,
                                                                            5814735468801166985,
                                                                            -6714447936807768262,
                                                                            -5714327453614639748,
                                                                            -6192446426547278726,
                                                                            -444629969368400321,
                                                                            5429373460835003100,
                                                                            8740205682096726931,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϢХȝţňԑ¶ϡƵ0Ȼó',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7029670395960243521,
                                                                            5950825163436078367,
                                                                            7800118469747624750,
                                                                            7225626168562579555,
                                                                            5194917551557216480,
                                                                            7087626796880890619,
                                                                            864978285483786577,
                                                                            -9085271835259512059,
                                                                            6535352303444204734,
                                                                            1688210879158828884,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϥ\\ɳϞӝʠαãǗБЙWŶpͼҷɑΟ\x95Ń!Ͻ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȶƋќɺWŎԧͺͽӓĨ-ɤҚԬӀĒԧĲȀѭCӈЁɭ˵Мźʬá',
                                                                            'ÓIʊίϖԓſŚȒĥηɿīɃІϒӨeәȝєͺķjȞɘĸԇˌρ',
                                                                            ';ȨCʸ˺ƖϹĐ˗ӷǔ҃ЅΛdŻнˊƮŴŲżв˄ѻ\x88ˠ\x85ґΏ',
                                                                            'ƑϦ͵ȘȐl\\ЗΐÉњǡЁˠÝýѼȂǡрϕŦ²ƿˏϸºɏʰɋ',
                                                                            'xԨeŎӷͷŵƢӕɧǚſāĦô»ùΙÏĄʺӌɘх˘ƈτӘHΝ',
                                                                            'ҌũҴџͲҨƧԘϴ\x8fPѩ\u0382˘ԩū\x89ʧɋғˤʬ^ȻϺːͼϐǉǅ',
                                                                            'ɨўŉҰрњʋ˭иƌA#\x8aϧǍǬġѓʉɜǏӣŸȲњ\xadŲԦ˓Ѓ',
                                                                            'Ήcӂʽ҆ǃԊĄÏ˰îɵϢѳӺ\x82ɟϗʋ˕ȹˈϾĔƚŋȎʍυԈ',
                                                                            'ˏPӣHCâ˛ͳҾ˔ʐц\u0382ĹѶƂÓԤǡċEʦΔǡҀҳǎɒ˘\x8c',
                                                                            'ƕʸνѵЮĄΉƍB6ȱҌÙÚHºѡ˧ҹ\x87˘ĦѲҫścĎŰӵа',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӫϢЂĚёŧĒӴʁʉѯǪð°ҞҐw Ƴ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 69670.01049449417,
                                                    },
                                    },
                            {
                                        'name': 'ԡϾȦ˶ɟɠɢǅĠǪʆәĖEƎ¨ΘҕƞЛҙ˘ˍǱ\\ӃԞѬҍ5',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.878725:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӽʙȂӑӂĴ˂ɍԑʶΫǊқ©ç{ɉȞīҐΨcʇԞ=ԎûşԥϮ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.878943:+0000',
                                                    },
                                    },
                            {
                                        'name': '¥ҎŧҚшŜԡӑōȢӃжοϓ\u03a2˅Ώ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.879083:+0000',
                                                    },
                                    },
                            {
                                        'name': 'kήǣ˵ƾ\x8aǻОʇǜcϘЍιҞϪǳμԤ\x8eϫĔĸԚʮʵĎŬƉБ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.879224:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƂĴɋΓǍȃđϙʻʆЧśŤşѲ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2371122828530435921,
                                                                            6940943612880995134,
                                                                            58567623465130607,
                                                                            -1813393245880007281,
                                                                            3856949576372686103,
                                                                            -6256286479496151987,
                                                                            6521584260873984094,
                                                                            -6485221875071301032,
                                                                            -3373430283082979138,
                                                                            6922288123394902002,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϤԆƟґŔĪ˙Λ˥ĶĒ˦ϺѺӅ˓ѐXĪ\x85ŊɽŒǔʨÅѮр@Ġ',
                    'message': '¨ȨˑķǩǹԗďҬ\x81ώŋŕİҏ°ЊҩʉˣӆΈ˦ĆҕņŢϵƛ˄',
                    'arguments': [
                            {
                                        'name': 'ѩўЕȐƸЊĘΟäŔ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.879981:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǥЁέ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŏщŮğЎ˞Ѷ×ќ>ЯϢʌϧӴˆ\u0380ԮЄӢΚşBŁýԦ\x90˜ʘȸ',
                                                                            'ɵʨЍӊεȔßʍÅMƅΜϲЂːǾ҅ЇÃuñh\u0380H\xa0ӀΦɅʣҺ',
                                                                            'ŗ҂˅ȯʩѐơ҆ƍĶηʩЏбҋŊ§ϥě\x8eԎњƨ͵Ċѐÿ¥˝ά',
                                                                            'ȮԂɷЁСƿȳǅƌџǤʠчϹU²ȽľĔʓɄɖΏъ¾ҷʑˀϔԀ',
                                                                            'ĒƏӘҐǈǯ§˵˜Ԋ\x92ʌɒXĪѧпŇƵӬԌ[ѾƳ8ơɥSÕ˾',
                                                                            'ÖŅŜɚƓHêͼԛX\x90\u0379˶˦ԦѽȩξñšĚĶȈћǨєЯƶŠϽ',
                                                                            'ϖΓԦѩɷÐĉ»ѡ&ͷԏŃǆԌ҉oƠƏʥˊϏŽƳϊÏҬŐѻӯ',
                                                                            'ҐьĶ¿ԧíҪǱѤŭƈϙȸԚϷŬԩǎÄҎлƾȐҰƿňȞŌ5ӌ',
                                                                            'ѿҰć0ϰʂĘΖɅˡȬİā\x86щбЁϥEǅđӒňȵƈŪɉȣӓΠ',
                                                                            'ɪʍ¢TĖʟӆϳˀŶƱ¢јӊѦ\x81ʧϓHѰ\x87˺ɕεǚĘŝƲɢϿ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŋӴʅԡВƸ˚ԙĭǭνΩсɨĭʰчƠɴɒƺ+ˉȍҔҧф7Ύď',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 409235.42507989827,
                                                    },
                                    },
                            {
                                        'name': 'Б#?ҳÒѻϩ_ϬΰşȯˎΠӧįӽ˕\x88ʞ}\u0381ǇËϳʂ~ѣĝԉ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -11853.93895936523,
                                                                            493509.38282884343,
                                                                            405328.98872065335,
                                                                            341665.15911722253,
                                                                            190918.81506146328,
                                                                            497280.11350171803,
                                                                            118577.65684851073,
                                                                            -59221.414293935835,
                                                                            789230.5466913927,
                                                                            422005.3854868584,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'LǀƽǹƢδ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            673373.2572750121,
                                                                            748834.8351670981,
                                                                            987331.2601217818,
                                                                            283824.1924715626,
                                                                            578976.4362410776,
                                                                            706466.152500321,
                                                                            538222.8367754114,
                                                                            293585.12686048285,
                                                                            425721.9475498637,
                                                                            188236.16887471493,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӌˑЫƩҬΪËĸѡҶĝÙ\x96ӟЫ¹ǩƵгĐйʶũɒӣ3ôƯϐӾ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            518617.1766748432,
                                                                            200478.25796707603,
                                                                            940321.2893170245,
                                                                            37522.699890211865,
                                                                            485933.9289314876,
                                                                            619485.7646589263,
                                                                            710674.4047298337,
                                                                            231857.91542430804,
                                                                            424414.017811442,
                                                                            607180.733667245,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΖǵǲëͰʎȏȬùɯӌ~Åʓӌɐҗ˔ʁԬѷԑGȨΓʇ\u0379ґƴҨ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1091242345368781490,
                                                    },
                                    },
                            {
                                        'name': 'ԛͷkPđȨʶƑϷҨΔқΤ˹ŐʍıŷČıԓƖқEčʋЌ]˙˼',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            224739.43762918166,
                                                                            868871.4634989566,
                                                                            322451.1337573211,
                                                                            911918.5006496902,
                                                                            780854.7377218769,
                                                                            275663.69774006563,
                                                                            119218.4209382791,
                                                                            663311.7996520766,
                                                                            879040.0744863041,
                                                                            467318.15047483763,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΉĈԌсʈ҉ӄãĝˠЇĂȊԅĲɎƇΣǅƠ3ӳ˨ēǲԃćï˛Ȟ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƙ]σεńљԈēĸԇǢϢȱǼʩŝñæяǭҜʟK˚Є',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӕѿ˜ˉaōė˥»ȶ˔ʖǟǖҥҦ˒õéWȍʑӅʽXɐäÊ΄Ǽ',
                                                                            '\x84úƔ˼ȆɑГϡЎʟąΫǸ\x8fОɕˑҤÞɜРӲȁӶļßƪΑџƇ',
                                                                            'ςˬUıgŴҞŪ4ˤůɾԛ˘ϨӧʍϬdŪʆȶ˔²?ɺйѨʮɝ',
                                                                            'ԛТӨˑЫҿωБҐϊȊ\x8d¦ƣ˫ҥȩÄѫϬÏȰ˟ԩ{ɗţʳАɀ',
                                                                            'ΣŐâȧѳƏ˴XŮІŖЪɺǎӀ\x9aӣȵуƅԎύԜʰ҃Ͷɿą˼ʃ',
                                                                            'ЄљΛс\x86#\u038bƹҀǳńǂà˄ӕȸȡЉǲ˱Ȩδȭȝþ¬пäŌδ',
                                                                            'ѢȩƆf;ƴŚΈƐơǌƴĞåĺƵƍƑȼҰ÷ʡĎǭИƕЉ˾zê',
                                                                            'єȼϫӶƏēΨĘƛϠѴįʅлɖ0ѯîɞǫɵŷЭԘѠԣʹѦƌň',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѽƒXѿ#ԜǤȀ*Ǒ"ġʛʛa,ӨȈɕӦˀ˾ҿÂͿҠοˮΡķ',
                    'message': 'ǶҌԊԨǂ\x9anЕtǷ҄ŉxœƗЁϽϚǿϛ϶Ѫӄɷ8ʰȬϋă)',
                    'arguments': [
                            {
                                        'name': 'lv\x8fȜǔԍ£V/ϡѡŦԚȚʎʉЃυԝŨϐưԋˣӍЕˣŦĶÖ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2948897994650272463,
                                                    },
                                    },
                            {
                                        'name': "ЭȼӏЯσӣ'ɟę)±Ǟð\x8dÄć}\u0383ԕƵҁ",
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʹʳΥŃ%ƮɅҷˑёԀѷžļÀԖƾL\x93ŵɆV\x9bЊģӃ_=ƶ\x9f',
                                                    },
                                    },
                            {
                                        'name': 'ĬԢЪ\x7f\x9eġͺeЯģԮ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4221305882692798926,
                                                    },
                                    },
                            {
                                        'name': '˨ě\x8c˜˘ҩȞԞʒǉҤȅΑʙӂæŴ\x87œǧўŉťΙ¸=',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            374700604190202481,
                                                                            1705750007986248292,
                                                                            -2400516068133894534,
                                                                            3431872063634827357,
                                                                            -4450380092985047831,
                                                                            -49418664994926374,
                                                                            -5053173487678388393,
                                                                            7965575818420808753,
                                                                            2552271378662764205,
                                                                            -7726263864755744407,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӈŀďĪĆ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1385734669751860228,
                                                                            -8413283685556005791,
                                                                            -6626101556373994896,
                                                                            7876996108920191791,
                                                                            -792947058670253484,
                                                                            -2866550502080696267,
                                                                            -3817609097068007871,
                                                                            4135055485511884189,
                                                                            -2512763057694844993,
                                                                            -9061541993711374933,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ƙζȕ˩жǛƇδŢ'ŎΠԀɻΠ\x81\x82ѥ",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.883885:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҿMª˂ԙкÏˣm\x8d˨ʠƸŜɄ\u0378˅˗ĞϓώӋ(ʭÜìт¾ӎÓ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϔŧҦ®ԛɯ˘ӢņʬŲ¶\x86ԟͱǷɒбôнŖϦʙıĖ\x82$Ɋȵʧ',
                                                    },
                                    },
                            {
                                        'name': '\x9dÄҞʟĴũ˒ʽΛˈȸōҬӹǢǋR˰ϫͶßȧФѡţɅŲƝãҕ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ԍ\x85ǚēǡϏԋ\x94ϫ)å&əͺ˥ǟˈеΈŠʇÖԐȈΡƲƠҤЋЀ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.884395:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȡśш˶ǤßïԃŠ´ӆҵќoɊáƒ\x8eǹȣ˘?њ)У\x9eʙςʜɊ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212316.884549:+0000',
                                                                            '20210208:212316.884559:+0000',
                                                                            '20210208:212316.884565:+0000',
                                                                            '20210208:212316.884570:+0000',
                                                                            '20210208:212316.884575:+0000',
                                                                            '20210208:212316.884580:+0000',
                                                                            '20210208:212316.884586:+0000',
                                                                            '20210208:212316.884597:+0000',
                                                                            '20210208:212316.884630:+0000',
                                                                            '20210208:212316.884639:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɪǗʣͿСηʙȢȵȇɪŕɏ',
                    'message': 'ǸЪːϮҮĠӄɎ\u0379ʡ&ʵȻϬђʒ[Öƌϫ¤ŴΏήȭΖ˚ńлъ',
                    'arguments': [
                            {
                                        'name': "эЪϯtҲǭҡʰŝŰɟʩв\xa04ʎЃãóаӻőņѰŝ'ĠЊ˕9",
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
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
                                        'name': 'ɔΪʭmǚ˾',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212316.885612:+0000',
                                                                            '20210208:212316.885629:+0000',
                                                                            '20210208:212316.885636:+0000',
                                                                            '20210208:212316.885641:+0000',
                                                                            '20210208:212316.885646:+0000',
                                                                            '20210208:212316.885651:+0000',
                                                                            '20210208:212316.885655:+0000',
                                                                            '20210208:212316.885660:+0000',
                                                                            '20210208:212316.885665:+0000',
                                                                            '20210208:212316.885670:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɅԚͷÀӇɿŌƞѭį¿фǀɵ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϘӼѤŷȡюĽňȼϟҧ¸ѮĒʳȴɾȇȌ˞ВǔяҌˋŠԎȳǜ˾',
                                                    },
                                    },
                            {
                                        'name': 'oµӦνлưɬҢ\x93ѬЗ҈iʂ˖ǭŁȒӽҸɔÃӂJĢǷɫʭǟŨ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3914081187167283983,
                                                    },
                                    },
                            {
                                        'name': 'ҶǙ¹҇љҚƔɊ˻ңʪżȧг˸м˔¥ΘÔ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ģԕʨnŋƅӹ(ƻфʶѯĽɬƨьӇQгӡŵʩΨЂãԀеEE{',
                                                    },
                                    },
                            {
                                        'name': 'ĲħɑOҚțϥƦЁЛÐʛΧϡȻ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԍѪԔ˙ђϰӒŤĞǟĸӂɩϬƢϒãͰȱӫȷιԢšàǴ\x8e\xa0ÁȽ',
                                                                            'ʴ҅íЎҩҥ҅ПĝҦĪҬŘΠӃӷΐɉиƱΐҰӹɿ¹ьȧτŽӼ',
                                                                            'řÈϵşѪÇυƕңӻϦ2ΪʗʛǨƧ{В^҂йѭúºʽÓɱͳā',
                                                                            'ѓÉĜΦҶӤʖȱNΗҒҨş\u038bԛĺѱЂˎԎŵÚŹҍĻ4ПͲФɹ',
                                                                            'ǖƯʊĆ˽ќÈǶķϛƉǩťд˜Ϊɠҍ"үŅϮИ˱ňѡĠСόî',
                                                                            'ʵǆɼƠÕ\x9aҢ¦Ɯ\x87űҖΙҘмґƚЩϖϙÁԊ6˳ʰҷӳҙԜʉ',
                                                                            'Ϋɰ˷ϏӅȰ\x83Ԍȧŗɍҝņ`ɭǰԑ˖ÐƖͳϝƘlǿʸϐѐĥ¬',
                                                                            'άӦǄmоʚsǉđʜk\x8cŜӣтӔȠпѺԛӱҐÅʱԋҴǀϐ˅Ӕ',
                                                                            '\x87uȏʜԡ\x85сʓǧ÷ǻoɣnΙčʗwǯŊʡҠωҹʪĦӚдǓɸ',
                                                                            'ȝδÖƷŜΎɀЎ˪ϷɵŌʢ§\u0378ș҈ӡϔ˦Κƈҗʑǳӟɟ§ά¿',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x81ΊҶLɰжʃÈVӦɆ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8378271089998689560,
                                                                            4475728630130059857,
                                                                            -7766740036799291724,
                                                                            -8245043580508298502,
                                                                            6456923533646088979,
                                                                            3696364869474090391,
                                                                            -5235512974429892241,
                                                                            6195871657711457623,
                                                                            3871811066631230850,
                                                                            -1567854142895790113,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƣϘЇιаҚ=ɆȿҨЧйˬɹΘ£µтƇ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            684234.3197662313,
                                                                            796255.1981266321,
                                                                            629682.6117855441,
                                                                            326504.1154672988,
                                                                            503934.80951006303,
                                                                            770888.7069118741,
                                                                            304598.5342909377,
                                                                            881173.5627545068,
                                                                            -21620.78880052062,
                                                                            638640.7359351586,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǎ\x80ЂŦԊʄͼþĘ°ĥ&ύ˄ɹӐӝҩΨӢ.<ԓ˫Ū®=ѭ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            487630.12961821747,
                                                                            610948.4898509565,
                                                                            277330.57123769214,
                                                                            713200.7934883484,
                                                                            851681.6021139658,
                                                                            640305.863354562,
                                                                            570166.4554181608,
                                                                            131802.31334348727,
                                                                            784193.7697915648,
                                                                            54940.34636046438,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϱɕǆƆѧǁƧмΉçȩȷ@ќΘuЂʽĲϚЪµĵѹʀ˟ĒËαѢ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3424592131582238047,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҀƙӋǮȖƓΏĥ^\x90Вθˬҹǩǀ¯ʏӵκҦ\x99˱ȇБΪҦѭ>ɟ',
                    'message': 'ӼιЧü¥ċǟΨПҼɲϮͼңКԬƙ\x88ʑ˒\x90ɌҔĴȄǢĮű˹u',
                    'arguments': [
                            {
                                        'name': 'ÜǒȱÒTʕӸԘ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4026194485843896600,
                                                                            3434280790057141399,
                                                                            -4118017127327528609,
                                                                            7942898191724940381,
                                                                            -7589978374216014752,
                                                                            5078851697621363282,
                                                                            628158872834593547,
                                                                            5644509624949422023,
                                                                            3556305253563171236,
                                                                            2070147443632922145,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˑjӑʁlјӂʚҿԌџuЈƱҼцʶǑǑÂȸɲǀŎέ\u0379ȼZΐϐ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.889437:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӽД\x8bԔΜʹȗʒϮƞаӠӚΪσ¡ӑÍƽ\u038d\x80zҀȳŊԟÇӡĉȆ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.889600:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϮȬɴE?\x86',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212316.889735:+0000',
                                                                            '20210208:212316.889744:+0000',
                                                                            '20210208:212316.889751:+0000',
                                                                            '20210208:212316.889756:+0000',
                                                                            '20210208:212316.889761:+0000',
                                                                            '20210208:212316.889765:+0000',
                                                                            '20210208:212316.889770:+0000',
                                                                            '20210208:212316.889775:+0000',
                                                                            '20210208:212316.889780:+0000',
                                                                            '20210208:212316.889784:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȗСȣ\x9b҄ϽΏƀϻŠԅҗǟÊɷɰʕÞԜŃЗԨԢŞĚˌʍЉɂǚ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.890014:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϋ×ўһǿǵȌԔ½˓ŭʜȶЮȑƈѥŌϝƱž.ȉωȲӖԮƥԛđ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.890158:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ͿɰƪǻɈʟƺ¦ԀƳѽɏȚӛ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212316.890293:+0000',
                                                                            '20210208:212316.890301:+0000',
                                                                            '20210208:212316.890307:+0000',
                                                                            '20210208:212316.890312:+0000',
                                                                            '20210208:212316.890317:+0000',
                                                                            '20210208:212316.890322:+0000',
                                                                            '20210208:212316.890326:+0000',
                                                                            '20210208:212316.890331:+0000',
                                                                            '20210208:212316.890336:+0000',
                                                                            '20210208:212316.890341:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ίԇďˊԮGȞɾ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 873371.9399506308,
                                                    },
                                    },
                            {
                                        'name': 'ʣɴÄȗρΕѧӏǔȵѷ˟;ӌn΅Ϭ\x83ǥƅԄ8ΖΜӿДάԅѯӭ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŏӷʊƾТâŎÿ-ҐĹİ1ӒǦĉˇɹzΨ#ɏƩ˘.]āĳάԨ',
                                                    },
                                    },
                            {
                                        'name': '{ƈŦǉЄ3σǄȒѭ\x9b˹rη',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƞӈПьƓʔӂсϲϓöƀ˜ìϏ9ѥūlȝzϿǣɞˊƤʜ˟Кǹ',
                    'message': 'ˀǕԥɕϿҸð\x97ʇÒĄϢƪÖđ˚˅ϗԡňҺϹőǍJāƷϢķü',
                    'arguments': [
                            {
                                        'name': 'Ƿ\x9e˟ǃɱŏŁϽžɐҔťҲрҡԩɻ¶ʟ ɷҒȰɾĬʫ˯ĖȂԮ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            756937.2321818409,
                                                                            989460.7969698377,
                                                                            207532.46143702086,
                                                                            -23380.55492920187,
                                                                            910152.9938888173,
                                                                            503543.4856689818,
                                                                            774351.3996591829,
                                                                            731338.4289496611,
                                                                            293968.4347147735,
                                                                            410530.03944037104,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӪìȞѪȺʚkÿҝÌĢϜǐψϽȶųȣЮËȜҶДϿѾƈӽʣǦϙ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': ';ˆӰùȱ4EɓϒŹ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5959636912507075632,
                                                    },
                                    },
                            {
                                        'name': 'ϫIÝĹÙ1Ϧ;ÝʈүБҦjıʎϽ\x92ȫԦǛçѹľɽ¿ˇ?',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.891861:+0000',
                                                    },
                                    },
                            {
                                        'name': 'bЉϝºΦȢӬŸȗǷʳǶ~ǰƂ\x94ϣɒȧŚȵɃɈΙςНǷʍ҃Ư',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ŝƩæЊӷŨЗɖɖˁŧ¼¬ʌҘmʭћė,ҷΜѲɘ\x93øƏ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            223485.1554505693,
                                                                            986057.4577940963,
                                                                            102276.52162369413,
                                                                            931702.7389774744,
                                                                            660388.3282140192,
                                                                            -14089.148451572604,
                                                                            514569.0657642046,
                                                                            -24190.976378503445,
                                                                            192675.620437229,
                                                                            47722.600551717274,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˱ѧҼ6ĠĈӍφǯʿÙɵњϵɷƇЎˌя҃Ϝâ?',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            693275.2791526803,
                                                                            924302.1370534482,
                                                                            118293.35284733106,
                                                                            892436.2146200553,
                                                                            759178.7176633558,
                                                                            515964.58163306955,
                                                                            301243.4401533564,
                                                                            -2998.539836708791,
                                                                            411336.4744171153,
                                                                            576000.9526028439,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѐϊ³ѺÃAәȂҵӑĶɫʂѳϟӧԔҀɸĠȑˋҖÚȵ¶ˢɻěΖ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'LѕϥӲ\x9cύӮ\x82ʌнХɽȎˑԫcǣÛjӵŢƸүāěʱo҇¤ˣ',
                                                                            ':ҢʀηȴЉѿÁʬƀƆ»ʴŝϠhȖǁΞǆŀϒÕтƠҼЌњҩɗ',
                                                                            'ҧ˄Ǭɚěыԕˡńͻ\x87ԔүŚϚЕРЂƌƁǈӰǠԑ˝ǀÔФ\x99ʁ',
                                                                            'ʇєȶˑʱºđƶƍȰHѓƔńʓжм΅ƣѧСǁКӍθǆĐàҥÄ',
                                                                            'ПǣcѰʹˮɯ4ɃˎˮƯ˻ѨξʒCʿƍЂ҇ɍɄԞŪ҈ɂ°ȻT',
                                                                            'Ԛњ˷đƲ¸Ǵ˸ƔÉĄƽǲ˯oȕX΄˷ʭΩȝćλƻȁĦԐѼҹ',
                                                                            'Áύ҈тƬгĐʁǻχƹвєķʪӍǀϤ(ί˺ʃƶ˄ƒҰʒǳҀý',
                                                                            'ʫʕԠ\x9cшŽ\u0381ҕҳϽʅыƍɎȫҏĦȳgȋ˽ǫǈ©ǵЀɛЩuԝ',
                                                                            'ʤǸҌĕεΫgˢ\xa0ŹʎʒϤ¶ƺͺƤƮˀӜȀәÀ˥ɷºǷ\u0381ОɎ',
                                                                            'ˬѲʊʨζřϮʿҚɐЀ½ʳŐϫѧЎСɎѓáǄņDˢżɀƟǿŲ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϥƿɷ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7683220696829213464,
                                                                            5646039118985074031,
                                                                            -8950936783251108799,
                                                                            4962918530257555627,
                                                                            -1725240961970151591,
                                                                            7805069996281584888,
                                                                            -7388501737047269857,
                                                                            6874731708115536413,
                                                                            3462458758666362894,
                                                                            3552316306355247402,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΟӛȔРŔħԘѥζªȳǲκ*Ũ˙ҞѾ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.894060:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϞćĂ¥ėŀʚȝĿ˙ˢϯΜ\x82ӝӆӨǍÉѴɄËѹχ\u0378ʞÃ¨ѽΉ',
                    'message': 'ÃԋˎÐюȍʔҢ˶ϧȁeKԮ²Ǔǂ\x7fϯϵˆŧǞƀӌȼϮ˨Ļе',
                    'arguments': [
                            {
                                        'name': 'ѯɩОÞϭãƬбǳ\x95¡įƲˏʳȒʽαӪѹ˜ΉѶӍaӐ˨њȟÚ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '҉ˬÑǲАԤÑͲőΪ˦АʤʬӖʻϞáϟΪ0ԄхŬ·˅ΊʰDΐ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4371492150489890523,
                                                                            7040168788666657302,
                                                                            5631979398569854954,
                                                                            -8263880492031093043,
                                                                            4470173095175154492,
                                                                            -1781850091666769021,
                                                                            7746540702927602942,
                                                                            8577631340362130101,
                                                                            -5011331065457195024,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɚԧԛŇů\x918ӃʅҭƆ2ѦӾơҗʮɵħʙѝƈƬŶʤюЇɍҸŕ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ҷäЩġӀʛӎĝЎˏƪӀĎѤ\x92ѓIʠĦɝŏçīˉѦӜ˹ҫӱʦ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҵôϘҩƜÿЧѴɧʺΨüЛĳMMxȔԮWЙнҸ˯ǐψ*ҽōǴ',
                                                                            'ǣU϶hӦϪʵѢѭӂɈӈÂʵΟ±uŲϯÑδӴϝʙԏѿƛķ\x90Ȕ',
                                                                            'ťuϜǤϩ]ӦΝЈą\u0378ÒΐPǲԈЛɽǹȊɗԦŸɑӠ×ŪӓΉê',
                                                                            'ƌ/ԛʦϦͺԩϏ¨ШÊɍфʙěɵĢoǽƒŴϲçˠ1ƵȈǃДҶ',
                                                                            '\x8eё-Ī>Ѿӆ\x80Ҝǐ\x9bŎ¬ʑԂǜʺɩҏдÇхÃńїʆɸğͳϗ',
                                                                            'ΠŐʒɬȓÔXҢʪϿ\u03a2kӦ:ϏӀʤɦƇόŰ(ȈЊŨϡ¡ΖӜı',
                                                                            'ɘɾӽǱΤѐґϿӵUБȐwҼѩǔͼȼɠĪάγɕ˨ĶҾPȤzǐ',
                                                                            '\x99Ϧ҅Эη˩þλ˒ûǣήюµħԫĥэĞΚВѷ˘ʧғȺħϾʚŕ',
                                                                            'ґԉӃѸ\u038bΘȝȽΩ\x81һX˨Ԓ¡ŧĎҟ"ˍșÙʊŕӋ\x9fĉΈƥϼ',
                                                                            'ȁƺ&ɆʅâʥǃʒƺȊӉϒϜѤҗԁ¿Εãřɼ\x8fΚū˪È˹\x99Ҙ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'đщńŦȀ\u0383ȂӁŲǁɧԧěƑȡ˪Хэ˫ԂɐˢԐԒʘʷҡų',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 580007.7257219396,
                                                    },
                                    },
                            {
                                        'name': 'ќȋáҪɾɇҲћȽÇΡĜøòʛƸʷλоӣϊԡΘȖϱԗȢǤɂɅ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '(ТdˀÈţ3˒ˉƤď϶ЦʶʛԔΌɚҺԅ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.895970:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ö\x99ʊʜJˬVŋĔéÚǎǁɉҌђȬϑҬzƂǬž)ĥӫˏĚʦƳ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϽAŴ·Ĳ¿ʄєƦ\x8cȞİÜƽ˫\u0378Ơ¹ϜéӏӒźҺеϋҒ˼fǒ',
                                                    },
                                    },
                            {
                                        'name': 'ϏУ˰ˏΠӉɸԄΈ\x99ŞʡΖɊԡ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            693836.2320957754,
                                                                            960356.1825473988,
                                                                            973745.3059842496,
                                                                            526073.6307323974,
                                                                            716418.5116341915,
                                                                            308306.3149537314,
                                                                            719424.8700656273,
                                                                            622811.8814873555,
                                                                            365499.8069159697,
                                                                            908512.3880957329,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЯίҥтʏϤǈϷΖ˲ȖȭʮҙÖϽϲƲʿǶĒǿЁʌwk¹Ь\x80Ƣ',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŀxԀΩЙƎЍɦԁƲҔVȑǑҽңţҨYɓʶjƛɘǌѸļ˛ŧ˸',
                    'message': 'aкґƏƲЬҩŔŇԌĵɑĻϫʓĐԜѿԑÌ˛цӱʇΜʤӠǐr\x9d',
                    'arguments': [
                            {
                                        'name': 'ӝŃ«ʌΡӣͻΩ^ȱ¿ʤmʰƓќĩњПҊЎМяĩͲѫʢԕξǸ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.897053:+0000',
                                                    },
                                    },
                            {
                                        'name': '\u0379ȃ¾Ô\x8eȠĨϣƪɡʣ˞ȴǜ§ԙĦʉLųeЄѯЋʲƼ˵øηȂ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ø¼ͻȝơȿR£ΡǝíˬЄ6ŵíIȭѠůƙɜΡ«řʻrԡΝǅ',
                                                    },
                                    },
                            {
                                        'name': 'ΤJư˹өй˹Ԓǲė[ė΄ɰhŃѐĕ8ˇLŰʆ@YӜѝɭѥ\x8e',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2441727834868396712,
                                                                            -7883774982197647057,
                                                                            2507866417814159476,
                                                                            7172491683442293438,
                                                                            8933576820515039644,
                                                                            -766827952297224538,
                                                                            4252206212278361349,
                                                                            -1502525976599462471,
                                                                            1223194996199651879,
                                                                            -2638535234776892172,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '·ұaĻķѢпзΊʏтöɏЫƤƸŲʭ§Ãʤ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5799320898543738464,
                                                                            4932992456318109713,
                                                                            -5911998991382941152,
                                                                            4378099391139046070,
                                                                            -263400109853760535,
                                                                            5930992762658528348,
                                                                            596211647872096265,
                                                                            8285665996264793141,
                                                                            8287488335377520416,
                                                                            -3289498762510169768,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʌϱϤƽΌԋϭȦОВщơȧӳƍɠƛǁҗʲÀӂ\x9fѴĕ%˶ϵʞѦ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5012933216712000635,
                                                    },
                                    },
                            {
                                        'name': '\xadɷҔǼҗʌCϋӔǈWǤӀ\x94ҖĩύҶЗВǳϹö˦ϋΙhҿŉӲ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'ӄϔƁӲҍͻҨƾѐԄȇέг',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŝĩżǬцa9HӁMTϘɶˎƦĨʢǪχĭHƾΓvβԠėΪϓĿ',
                                                                            '҈ɨƆԤˌһƂ˽ǣ\u0381ъѐïӡҝԒыƗǷӫOƴ»ȡӪfƹæǢɶ',
                                                                            'ӽԮƬŊăȴѮɺÐΧήǽDѺԒПѭӼԪ&J\x87φԦЦĦСΓˏѡ',
                                                                            'Н˟ŐǄ\x88oΛј\u038b\x91sŋȏѡÀ˅rƇӺКĠρƐΨȧȚɋϬ˲ѳ',
                                                                            'ϦƕϿ3ǄӥҰªµɎƉˡ\x85λώȩϽaŏҭˬ\x96ǙђӈEńȝʖԦ',
                                                                            'ҎӝĪɐͳųȅŏ Єȣџȉ҇ýЪÊŗԕ˄ȠȊŵȡͲbĢ˧A°',
                                                                            '¼кӀϥΣѯƀıƮɱҫ˲ʸѲƮ˝¨ɇUӮҙąӑ\x9cȫΉяęΐë',
                                                                            'ϞŐɯԙŌӌԮ«ӇĢӣѪӺČŶƲȍƬŇƹ˥φϞιmӵˌļυϕ',
                                                                            'ӣ1ѿЯÿ"ҬԃɘɎӭωÅ˃;äïƟʩЬͺĕӋϜăǍďϤҐÿ',
                                                                            'ȹʜĶ²ҴЅс҅×æȻüаʦ¼ԛɡȇӗȪ˽ӃˏĶȮƷѱƧҕa',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ðǆϚĚúɐƆϽÿÈлȎ҅.ƏŁя²ҷȺԖȔɌp`Ć¦ϒ˒u',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '҆ӿǕȣϥΟøXś˺ҁΏΧłŷʉãŻEʘɴΊҕӡϢƕĎȊԘő',
                                                    },
                                    },
                            {
                                        'name': 'ɯÓɶȀɕ«ѽϚѼ¬ȗˏƾѕӉζʊʾҽɣȿӍɄ3ĽɴĳϤ\x88Ѡ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʮԣԅɺΤԝƢǋŒȻëңʑηɤàε˭ˮʰͺƫɮѝҧӫ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˄˸ԏԩрπÇӵ˂ѿőπɟĕʬƣǠAè¡\x94ʟȍŧɺϟШʋϸђ',
                                                                            'ɘɫĭ\x8aƥÓƕϋЀˠƱɳȁƳǖƃĦȶΫŒƱǖ˲ωДġʵµƧ.',
                                                                            '£ӑ½ԒϜœѮӷʁÅoďƅΌΌʧñɨЗЯʫåĄǈƪžȒ4ӀĶ',
                                                                            'ϩ\x8eƂ0ǵhԑ\x93ĀѢԬǞɍ҄ˏǔǨɔƬ$÷ϑ3ɥˍƗɦЙτˮ',
                                                                            'έņʹϒ6\x89ˠãµωѸ\x95ɍɣϛɎПϖоУëЁ˨Ѯ«ɒǺ\x82Ǖĥ',
                                                                            'ѰԈ҄˼І¡ÂåΈɐę˶΄ΤҕЯˑģѲˬѕƂӋɔ`Ҭũ\u038b\x87Ú',
                                                                            'ή϶ʷ˲ǜ5xυñ˪ƹΉȄƂǗ\x9cȀ×őюƝ҇ЀГғȪÇƇǬџ',
                                                                            'ӥpҚ¦έɆєʱҬԥϘӁȘǊиѝҹϔмȱπȩȸӴђŉβáńͲ',
                                                                            'ѵԏӻ˲ðJˬΨΌ˩ԪӚŗǈĺӾBĨҥњˡ6˫|\u0381ʞʳ\x92ԇƦ',
                                                                            '¹ǽƓňʴɚǋWʽǘԉϔɊˏȋҒӫĺɶȌ΅´uЗ\xa0ɔ"ӮƼϵ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԪȤƂʇӠ˾',
                    'message': 'ŴTʫϫХȽƙ҈Эȥ)w\x85ГʖţÙʜŗǁƉTɒѦƉħǓΘʊĝ',
                    'arguments': [
                            {
                                        'name': 'ƲǨÝpεɩwȥğŵӖġºɜªˎ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            360793.34239397314,
                                                                            855519.386592617,
                                                                            -62799.281115718375,
                                                                            336895.71678244136,
                                                                            79474.94390792988,
                                                                            408739.939273711,
                                                                            173292.349730607,
                                                                            253139.02066260925,
                                                                            272554.0155422345,
                                                                            880509.5151437916,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '»³ďəǟԂɲԈȊ\\ňåӦХӐŇӯ ҢŚʱ÷˯ʨŇ˜ų:\u0383Ԙ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2164825132093874253,
                                                    },
                                    },
                            {
                                        'name': '¹ĴȉȻȸ˳ÙӾɺ϶ĎǲƑбƋӉϓ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212316.900609:+0000',
                                                                            '20210208:212316.900634:+0000',
                                                                            '20210208:212316.900654:+0000',
                                                                            '20210208:212316.900668:+0000',
                                                                            '20210208:212316.900694:+0000',
                                                                            '20210208:212316.900710:+0000',
                                                                            '20210208:212316.900717:+0000',
                                                                            '20210208:212316.900722:+0000',
                                                                            '20210208:212316.900741:+0000',
                                                                            '20210208:212316.900746:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȅɮƣͽğƚ¨Ƭ˅ӳɪlȭǣȸőìԀʋǙ4ҙӥHɿ>ӌʹ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'вÚȚĆʚкХ˟Ȃˣ]ұPһɵÕEǳĖʂΌџϙȷōԊΣʠ\u0383\x7f',
                                                                            'РŹ҃ɐɄΫˁхa]6\x8bɆőž\x81Ңҷʿ҄ѳÉѕʬ«ǀːƈεǆ',
                                                                            'ҫʺΛӒӛ˟±ά·ҀӥȚԩʠфϖϿӍŷϚŮɐļШȧœċěąu',
                                                                            '˻ąǲΑʻΗϡŨ°)ÑɛÍӰјͷťԃѺoԜɥʰЉǥȇηɱЫɨ',
                                                                            'ңϞѷɤƆϚ˶ĝţ҃ѲˢEæ[ȥų½ΥƧҡЦĀχΤã½ˎ¤9',
                                                                            'ÂʋӓƄŀӽ¦-ɔŅ\x93˜þϒͰЎМдǇԞǤԓŐӡªRÆӊϹΠ',
                                                                            'Ǖ˅Ȃż«ĉɆƷ¾ͽΗԇƶлԃfΡβϡҤĿé\x98ϊι\x97ϛэΛЌ',
                                                                            'bÔÕǁӀ¢ƔÑŞɎ¨εʋƿNǨʭʭМ҇Ҕųŗĉ²ÜǆŷӾΑ',
                                                                            'ӇӴķßˍŵҦǁśңҦЈŻɞɟƏїӿßʮ`ŪͻŦÏ+ēωқy',
                                                                            'ʁɡ\u038bґθğŮǑЄ/ȢȯͿϔʆ˅˴¢ԉҎƪϛɿ\x9cʽ|ЍԔϴД',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'pҪ',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΓţЁɜe',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212316.902128:+0000',
                                                                            '20210208:212316.902152:+0000',
                                                                            '20210208:212316.902159:+0000',
                                                                            '20210208:212316.902165:+0000',
                                                                            '20210208:212316.902170:+0000',
                                                                            '20210208:212316.902175:+0000',
                                                                            '20210208:212316.902180:+0000',
                                                                            '20210208:212316.902184:+0000',
                                                                            '20210208:212316.902189:+0000',
                                                                            '20210208:212316.902194:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¡Ӳ0ψҡ˽ĿĞȍÿʐƮɼĉЖĆ\x84ѢǴˉ3ÿ҅Ά*҃ϋΐʹǙ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԂǿѳŭɘǔĲγϠʄ°ґӀËQìvĻɜ´ͶʟɄ\x9eŶ\x84ԓιƢĻ',
                                                                            'ԠȅɕŤíӆȈʒʯÈλʦԓȘ\x9bǉʣӬЂǕ\x97ɦîȴљƭZķϗԝ',
                                                                            '\x88ԘǻĭǺАюūжΆǫȈŅƳӍ\u0379ÕǊĒӮŚȘîΡǗĲҁĴơř',
                                                                            'ŚҦûѥŀƄМƟӺΕŢ\x82Ўƃʋʔʌϕ«ǿń˸\x93ʭЎӅǕѓ˻\x94',
                                                                            'čɒØιł£öˤ\x91ӶïtǫE˂ʱӗ1\x9cēҾ\x83$ѥԈΡFμľŖ',
                                                                            'љƯƞ˕Īӝ>ƿǷˊȐƣČŎЈŖϨƱÅĽƩњʠʥê҂ϴʗĈӡ',
                                                                            'ѕΐȩ¹ÃŠ¯½ɵ˙ȌÇ\x87ҳfԬlɫŋƅĄ>©ƥѝêƯϸȊ~',
                                                                            'Ҿ϶ȅƷʹʆ˸ɋӬ2ìʀ:Śé˯ǘҕǝ\xadӼŶ«ͶŝɶĥƸӖ¹',
                                                                            'ҽϙͼūϳƨс\u038dӻɺ˾нˉӼ7ͺҐşτĥɲɢȽʱЌѽЇӖ\x81ќ',
                                                                            'ŁҏņӐ˨ɨŚˇѺÙƘӸɖˋ˺ƛ\x91Ц\x93гӌǡǰʕōƶ˴ʅԗC',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȥɘ˝ɰķәŲŉΝʸǼѐɣxǒͻίȇ\x91şŚ˸ėѸңǿЮρрè',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ĉigȆƥƎЮ;ʹҋĘƉ0Ͻ˄',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            337106.2407449365,
                                                                            787853.7151219976,
                                                                            841555.3211976513,
                                                                            556098.6940931202,
                                                                            783832.8657572541,
                                                                            943934.3043086437,
                                                                            137428.6114408157,
                                                                            862381.6274657579,
                                                                            377072.4822244144,
                                                                            656485.8988996785,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʳŒѨХǋˌʦƤĥŔʏǯωɌҢԪǥҐ@¼¸ȄԊҔɄ\\˃ǈв6',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212316.903614:+0000',
                                                                            '20210208:212316.903631:+0000',
                                                                            '20210208:212316.903637:+0000',
                                                                            '20210208:212316.903643:+0000',
                                                                            '20210208:212316.903648:+0000',
                                                                            '20210208:212316.903653:+0000',
                                                                            '20210208:212316.903658:+0000',
                                                                            '20210208:212316.903662:+0000',
                                                                            '20210208:212316.903667:+0000',
                                                                            '20210208:212316.903672:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϙϿɲ˵ăǺӼȠʪƋƃԟɫŲǓ˺ƠͽԞɛɻɬ$ϤǰäŰʧŞȵ',
                    'message': 'ϙЂӠėǰş#ϕ˚Ԗя\x8bĐБφaԕNЦ˸рУºҼѠΒ\x83ѪђƮ',
                    'arguments': [
                            {
                                        'name': 'ɢÇѸ½ϫßυӏÔΞ~ѨƘĉϧĆԃǦŁǇҰ\x7fȔŇѩĭҬǅ˺Δ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'вǚƝ\x8fӿɺїϚмƐ:ɥ˖ˢ˚ĜŮɮҳ˧Щ҆ҦˑШȞƘќøė',
                                                                            'C\x9bӼĩƈǂʡѱƲşТÓ˄½˫ѽ˅ԆϪчӾиIŮɤ˜Ҁҹʱ҈',
                                                                            'ʚǊēϔađƻ%ҫȬǗɈЈƗԩҚԚʫиӒКōſʒԫϑЋΣ×¢',
                                                                            'ȃпϫҨłлӒɅʿѦёӣӫȌзβøčʢӃ²ЇÆĆ´Ț^ɽǶz',
                                                                            'ѲǑҘ҈ЦǤɰƤҢӹɨѺЅѿ˭ŷЅĺ}ʵδ\x88ԛФȀı7ǷȐƪ',
                                                                            'ίϔ˼¶ЕűJͼɣϿǢӯ ʺƯ ɑҍśϊ\x8aŊƨȏ\x8aӷĈŷĎĻ',
                                                                            'γЦѫƗӴrԣӍеϡȂRРˣЃ¿ƒÌ\x88iһƊӢʇˠªύΦɆĂ',
                                                                            'Ɂē;ʋԙө˝Ė¡ªɳǢřϞÿ˰ǝêбƼđΏЏɕòǼǈϭ·Ʒ',
                                                                            'ǧǇӬξ¨EьA\x97£ÄϣñóàŅ˭˜ʝѓȺĭĪcϧʄϨqȕӾ',
                                                                            'γǲȫƬǯŽ˞˦ųΣ´BǖӋͼϼʹ\x8e҅Ѵɿĵѳ\x91$ӳȢòĊď',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӍѫGϾbȎƛЪ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.904708:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϵϸЗ˃ЮѴEʞŬυɵTǑǬ˻«ʐRɞʏΣ˸ǬҮȵɔ˾ϊ·ԥ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȅѠӄӶΌеӃǯǕ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɔˬȇ\x87ÿΝаʘƫĲ%Ѵӗѫuö#nѺ¤ŢͳԠʨ˂ĵv˃ѣɸ',
                                                    },
                                    },
                            {
                                        'name': 'ЀϞф͵ҫɎȣΙ6ŢʴɝѾԜņγʀʘǵȗǕя#ΫɱhƂҋηӈ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6308614481528841268,
                                                    },
                                    },
                            {
                                        'name': 'ȁĥ˙˫`ǵϵȕÔȰԖhІɖҕΜɊdɽΣԅŋȥǠŏȀħѾƧѪ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8088257010653772657,
                                                    },
                                    },
                            {
                                        'name': 'Ԗơ˛ȪȖɷԎӱǗЧӖ˛\xadβƺBӓɵҪƸ˔ԧƔƯƭ\x98ƄɌӹЧ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 668889.7005322794,
                                                    },
                                    },
                            {
                                        'name': 'ͿrǰǹĎʦ˫ӁƠϳˋͿĭ~ԈӠĸУ˳Ǐ2ȘşΛҏûĊŅͺƔ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.905581:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ģҭȁȎůӯÖоƄɍϪØԪϬЩӀʾȋůõДԟ\u0382ӳƌ\x9fȿÉ\x83Ũ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7585114923214872934,
                                                    },
                                    },
                            {
                                        'name': 'ƣѨйͺʽΠĦʥǭɍΛŤɨδˢƂҼ͵7ŰɅpҁĐŒόơ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 887528.4841138809,
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

            'scope': 'verbose',

            'messages': [
                {
                    'catalog': 'NǏ',
                    'message': 'Ҙ',
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
            'identifier': 'ʄɪ\x9dě8Ϲ˾ыȵǘƩҲÐҡ-ԆȖȆůѣpƟьɬĹǻъÑ϶ԏ',
            'categories': [
                'configuration',
                'access-restriction',
                'access-restriction',
                'internal',
                'network',
                'os',
                'configuration',
                'invalid-user-action',
                'network',
                'invalid-user-action',
            ],
            'source': '.нϢʗĤЂӽӔYͳ¬\x9cȍȧʣȔŭʐа\x9cƤ´ȐXÙ£ЙˌҾК',
            'messages': [
                {
                    'catalog': 'õ¦ӈʘΰŧȱӅ\x94ϲȥēKӊɕʃƠƙȷӆґś+ӛ;I˞ŧѿ!',
                    'message': 'ȯŭҭǯĊI΄˗ÊÁȎÍђȌеԛʧЁ˓ĪσϺӲӉ˹ϛ˖Сȹ(',
                    'arguments': [
                            {
                                        'name': '\x99ĪʡЗʣѠŴǭϊѻ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΩƥϹ˃˟ª\x9dżùTҎХЫ\x9cɡыş/ӫęƼ\x95 ʙў҇ġԓͶΡ',
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
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x91ϤχҤ\x84ёԈʑсϞĨɨҦŔЋźӺӼӴҼӞĬͻ\u038dαʽǣWʈӁ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'əЩϹѰĤЭªȅĉhƝ²цɔʣϿϡƆĕϱɁ˫ƂλўԦБϤǣτ',
                                                                            'Έş\x9d·ʆuй\x84ŹŐһʓȨɕΑǓˡʳ˘ѱϿɫПрӷʟ˥Ĩȥń',
                                                                            'ŞɛƮɍúԤőӦȿšcȥȩǃϣѽ\u03a2ǖɕӓɒqӃφǛǠðԚBѓ',
                                                                            'ΪҡȶƇΊ\x97¢ѤӰäңĞƙɏѾGhĮӳƅșгˁ\u0378ÏŲƧБɛҨ',
                                                                            'ËɲËǟʙӪ˛ąұʇŷǴ˗6ю˪цȥē\x98\x80\u038bƞ,ÁȊƻсͰӻ',
                                                                            'ŗáɉƦɩћưÃƨɺ\x9eȜ˝ӸȄĝǅ˗ȌɸʹH\x96Û)өǠą\\˃',
                                                                            '\x94ʘӔȺϋ\u0383ĪųĔʷӆþȕǑˍǇʷǁēyǑƳԌ\x86űӭȻm±Ė',
                                                                            'ѰGÿҌϸǇѳʡǢţ<šͷԉģ˜\u0379v>ˎ\x9fєˑįçĨѶơȋƝ',
                                                                            'ȼƀʑҔϫˣţØˢıĊζĖvΛќϿϳЬwӢЉŦ"ʗ4Ǌτӧӯ',
                                                                            'ОԆːǯѥÌχÒԥƼǖĝϣљҟҥԣбѝǷ\u0383ʭğӻȖұçѡȀƇ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ķőдʚɱǆȾ0ӢȉʭĞϕě˩ʤǃǫSÅ˳ÒÃeҶ˧ɕӟѻÞ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1117384052443857229,
                                                    },
                                    },
                            {
                                        'name': 'ǇΑŞҍ;ƠжûҢČҍǄʄ\u0380Þɉāɓҁȫ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': 'ţВƺЀȃ˪úǸҐ\u0379¹Å˖ЬćϟǅBш',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 646420.2046207595,
                                                    },
                                    },
                            {
                                        'name': 'ƬɸӁɈԐΛńьǘИτӨȏДɐȞÓɴЁѪƥҙʴʎҠ¡2Ϯ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212316.929048:+0000',
                                                                            '20210208:212316.929070:+0000',
                                                                            '20210208:212316.929077:+0000',
                                                                            '20210208:212316.929083:+0000',
                                                                            '20210208:212316.929089:+0000',
                                                                            '20210208:212316.929094:+0000',
                                                                            '20210208:212316.929099:+0000',
                                                                            '20210208:212316.929104:+0000',
                                                                            '20210208:212316.929109:+0000',
                                                                            '20210208:212316.929114:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԓЙИ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ː¢ʢśǉˍǯɕͰɂɓŵȴá˲ϭżkʠńɻӼ΅ҡΓԟʡԓҠМ',
                                                    },
                                    },
                            {
                                        'name': 'ѓĮȐƔ`',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ĊʹӊĭӠϞ\u038bΝ¨˩ϩĴƉŠ҇Ȣʘ·Öǲ¼Ɂ9Ȯů҈љʔԠŽ',
                                                                            'ϴʅԠȉ2ԥľԆĪŅϖɳmϭɶȑγѺҵѦ=˃ҧРśȝή·ƕǻ',
                                                                            "ͰȝϾҵ\x9eͲӰ«ԔŴƢ\x8aĐłăÝј'βǘȇÛԀJʳҕʿ˝ԞE",
                                                                            'Ǟìʴ;ɬЍċ¡КЩækȵȅ(ĩ¾ɸ·ªʦǮΠԅȁҴԤʉµ,',
                                                                            'ӺáĪˆǰϽэĘƼɯ8В>ӬӷʢȲДʃðǣšɄ<ƨʋӻǾķƯ',
                                                                            'ΛɣĊϯ϶ÊϡêȦȩ˙ϨӜӽыѧϪѢǉͽϏӱƯëȌîO×ҟȋ',
                                                                            '\x93ʾȻӑй`љбѻŠǚłĈƂbS҇Ѻƚҝр(ԤĕaǯǸίϟϿ',
                                                                            'З¯ͿӛϠȚʠˇҤʝӽѝөҚ¨ѝǪŽZΎŧƯǴӂČſӜð˚о',
                                                                            'сʷuǟÿźʔԄ\x8ekǥЅƃǲû¯ПȋƦ³ĽО\xad·ЭљǗԣϙЪ',
                                                                            'ȋӮΔоӃдϕǅʣʁlѻө+ϚϺʄνҭǉВû#ƬϦȑӁǈúʝ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΰƭ҉DԛɏǴԈϴƳǖϐŐǯК҇ȾϡʶϜǵʁу',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            946554.369937182,
                                                                            661831.6689423862,
                                                                            230676.3368137767,
                                                                            899147.8566661048,
                                                                            247557.40568543173,
                                                                            754712.5003220529,
                                                                            623167.4849192024,
                                                                            279025.77982893115,
                                                                            401977.8201464808,
                                                                            32313.96263212597,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˚ʤ{ѴŞӜʙɧ»ΘәîơƸŚįЉ΄ŪԇŐÛԡūЄѫUɃԁɾ',
                    'message': 'ҡƠ\x91ƓƩ÷ɹȷъ˫Ŭώҍӓˈ/ʩϹġÜҩʴήȹҵȀԀщȆќ',
                    'arguments': [
                            {
                                        'name': 'ǐ˗ʮѾʂ\x84ԆęÁ˯˒ȲƱăļ\u038bϓѻǍщЎͽŵуΌǟ˩cÛ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2268098258502009074,
                                                    },
                                    },
                            {
                                        'name': 'дČŧԀƦȎ҅ŝųɔʚǻҸƞƂaŢЂӊ˨YКÎ«ʮţƃξ\x9bѳ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212316.930670:+0000',
                                                                            '20210208:212316.930683:+0000',
                                                                            '20210208:212316.930689:+0000',
                                                                            '20210208:212316.930694:+0000',
                                                                            '20210208:212316.930698:+0000',
                                                                            '20210208:212316.930703:+0000',
                                                                            '20210208:212316.930708:+0000',
                                                                            '20210208:212316.930712:+0000',
                                                                            '20210208:212316.930717:+0000',
                                                                            '20210208:212316.930722:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'нϾGϫΕһ˄ʕ\x80œȀáîΚυЀҩƟǋӣ˦ѬǨ<λtҾԕƓ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӊřįЊ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǬʤӠӮȚØˢǸҺҮĮśɠɷıØјɥƿ˴ƩӜԓėŅÞ&ȏψʱ',
                                                                            'ɎӣԌ˓ǗIƧӮŪԨȴȱ&ҝǝϪƿü҃ĖυĊСkԛǨƍωЗĮ',
                                                                            'œΜɧˊÜɘÅȤƂȦCzlȶĪƿїӣŊҁ҉Лšřɝȼҋǟ¥¤',
                                                                            'ϻЄίԏHӷԉÃˑŊ\x91ɋǬ\x8eΩ=Е˰ɺʄTϼőàŶƝ\x9fɩѺɾ',
                                                                            'ψʅ1˜\u0382ƑɢЯųMŎǮͽqӉůYƮǲΞĕƣҥţȸȐȪύƯӡ',
                                                                            'ӻӑĸ˺µȎѫ˾ˌˮΔ®]ũԭÂØԛǭЮ˒Џŭѱ4ƦȩēϺƺ',
                                                                            'C\x8fЀƴɟϗʘēЈÈԢϵҘúÑʴȳʔƨŘѵXЕƨϹˑӢПĉ ',
                                                                            'ĭѽ˷һЕԇɛBfǲшɛƾԏÃаѳȭΪˬ\x8b˄ѲʀЗҙԪʱʻǲ',
                                                                            'ƞоҷ\x89ϓ˥ȪӲßΨ˓±ĮáŊ˸"ϜҪɰɬʧøωōЏ,ǾӔԔ',
                                                                            'үԕ=ƸќƦɉ>țƏkǅϕɯɝ˸ŏéҹňμ¼ˎáǞӵĈɵʻ°',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҽ¡Ȃ(ǬΫƾҡĹɗƟμҒQşѕȫкɓȒƀ ƻϬȴмʷđ\x92ӿ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7446961268045734648,
                                                    },
                                    },
                            {
                                        'name': 'ǎü˅ʤǊŋɎņý˙ŗ˕ƞȵСīsʩ\x9aɍĚξ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7310306007537215829,
                                                    },
                                    },
                            {
                                        'name': 'ɧiįcԖǳĜÑӵФΖȃǛԚҵиϯԈ\x99εϘϏˍǾΰʖҵǬɺю',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            814588.5295286963,
                                                                            611849.743525791,
                                                                            761700.4942435918,
                                                                            356618.28598513297,
                                                                            963712.6332787557,
                                                                            883157.8856032175,
                                                                            -50184.13685331434,
                                                                            807553.792970665,
                                                                            -83246.31945835063,
                                                                            620254.6025711286,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӣɽǼŷ҉ѩm¾űHБGЌɷϴюȜ»\x86ҥԖʹ˹čΝˇřШƱ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            492423.2720054204,
                                                                            188885.3066052324,
                                                                            717222.829196167,
                                                                            591152.9400010444,
                                                                            926224.8897792328,
                                                                            776200.2031727418,
                                                                            910589.0190032788,
                                                                            781353.4124840877,
                                                                            585337.2915842409,
                                                                            237374.41354784544,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҴÁƥϾè˱ǊӃϟ·΅˛ɠĽϘ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212316.932652:+0000',
                                                                            '20210208:212316.932689:+0000',
                                                                            '20210208:212316.932696:+0000',
                                                                            '20210208:212316.932701:+0000',
                                                                            '20210208:212316.932705:+0000',
                                                                            '20210208:212316.932710:+0000',
                                                                            '20210208:212316.932714:+0000',
                                                                            '20210208:212316.932719:+0000',
                                                                            '20210208:212316.932723:+0000',
                                                                            '20210208:212316.932728:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȨξϚ˳ΪΩƻɹϕ˽őȱƵɴ҂цɈBǃГǫƹЯУЫßҦӗШˇ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƻŽʭ¦əă\x7fșГѼИϿɪſpϱͱ\x9fʍӵˆΩΏѷ+Ԏžĭ҄Ȇ',
                                                                            'ѣΟȕXaÝǀяӝ˂sЧђΡʻ˂ι\u0383ˣŮ¡ɝԦ\x86ќ\u038bʈˤ\u0378ˮ',
                                                                            '҉ΖǇ0ɖҐӷµĝƭ ǌԞƗ҄ʭԝϛæԃȈĎ҇ҟҊͱ¨˸^ǿ',
                                                                            'ÒʊʑЉˏȪdȰ˳\x9d\u03a2ţĤΐɥЦ\x83Ԥfн\u0383ǆћњΈӾłУυǅ',
                                                                            'ԩѮҹнǭўňҿsʽԈ҃ԐΛў˛ħcԐќфӲÚ˯Fԃżſȱř',
                                                                            '\x93ŲʏǓҷĮˁЌҝӵҺÁà˵ШơeһΈξѯΤ¡ΜŜɣαʍǣɔ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'aəìƅӳĤ9ĢлħсʴşԟɀƟєǀТXӖą¿Ѽˇ\x93ѠĒӆɔ',
                    'message': 'ǮͶЎȮ\x89Ð8˂пɍȋӏÈȓȽіƇ˸ϲūŕѤаʢлƞǥӍ\x84\u0378',
                    'arguments': [
                            {
                                        'name': 'ȏЍβɭ7ȂСǣØĞϙÃ1ŵѧќÅҖɪѐ÷ÇȕŻӋɂѡɛ0ΐ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'įήǡǊύːъЂµçєӠƴĄǦǁƷwȗϜ¿ʶҿȒѫӹӑԉĿǼ',
                                                    },
                                    },
                            {
                                        'name': 'Ӌб\x90ˋθϨԚѬǀ\x87ϾȋĻʓп˄ɣΠǮɝІԌßȮƫΰ u£Ә',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'уóԑʄԭ@˝ȤәϥќKтèƊѧϟѧʼƁ҆ΦЭӎкˡʳΛãҦ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 664656.0260561411,
                                                    },
                                    },
                            {
                                        'name': 'σɮѵ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.935188:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҟëӯȐȵUĴ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7683539325962487460,
                                                                            -5216882630352858831,
                                                                            2286032572577371377,
                                                                            -3619862057009329141,
                                                                            3814756811017088968,
                                                                            -5155651146224134853,
                                                                            6724565600630311318,
                                                                            -8032338266991305217,
                                                                            -5256695608708788317,
                                                                            1932204136037570370,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¶ˉӓɄ\x99wʕƒ>ζѼƪŞc',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 242430.78630274313,
                                                    },
                                    },
                            {
                                        'name': '˕',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ГƟĮȻɔ͵ʿҍíêǷƢƴʸȤʌƇѐѾ\\wҵʒɾĕӴһұȊħ',
                                                                            'ԔiĄĘПϨĩĹǹ\x94\x82ҶYЇƈ˃ӴӸӛǊ¢șɔчϪԓć·Ǧȡ',
                                                                            '˶Įһ˵ȜӁӃәȂǊˏȑӵŤҸÁŅ\x9eēČƺƸǲ¨Ě@Ƃ΅ӭg',
                                                                            'ˋ#ÊŖçфǊǟŶ{țНàϯΕӶƺÅиŵþԆҡʕÇ¦ǃȑʬɘ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Fő˕Ӻ\x98ƁӭƪRԦԫӒΨ˦ϒș',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '¸ŉ¿ȗͻţ˅ΙƪԫˉĎġÆƲƙȅƑН΄ǾӊbaƁͷԪĂȩǢ',
                                                                            'ɇԣMĻ˙ӎĨϣ½ύ@ȹWT˸ĹȾɟ˼Ϧ˻ȢʎʝOÛǠãΦĴ',
                                                                            'цϸЍΫԤΧ\\ӆҵӱˆȡҤɵɬ\x86\x9e÷хӴӹЙϒҊԪрӆРӑǰ',
                                                                            'ŲЦ´ǩèõӟȟʓȭԃɱDΤˢΝĨǦ϶ÞјʋӀеͿÈҽѣƎƴ',
                                                                            'ѥƥѹÇȕ6Ȅuȼ)ȭ\x89ˏϕƃɀúƇè¬ſԓįϘңŬ)Ϩw½',
                                                                            'А\x80ŋӾ\u0381ɥӎЃГӣʁϐǔǨхфЫɞŕŁćӟ¼éЂЁϽµҨї',
                                                                            'ΫƩҪǒ˄ΜRîʧҢǲңŋÓŁțÔyǫлβӴç1ΫԙɅǔ\u0381Ȟ',
                                                                            'ÐÛǝʙŗƱӜæmд³ǔΕѐ˦ŇδʹǸ˫ȃкрϰˆӁŢҁӻƙ',
                                                                            'ǗȷzħƠĮž҈ȋƖ˃1ɺɄǍϖǒҎbʆȁӣGԛ˱ʬӖЭÑ¿',
                                                                            '\x92ǌţЮkϡ/ǳƘŊƚVÇɚӽΫɭèҀŃʏѾʱфȢǽҊw÷ř',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˛щԘxӒΌɇʑƕҐʽ,ǪͻоȞʨδҩЙÙŔζ}æ˂\u0383ˊԓǯ',
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
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʀɡŊАҠƲϻєįjƻВǀӧǃÄǓѾuԮԜƕʺуҦѻΥ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӜϓӀ¸ВʊѠԃƮӈÛТΞɯȤΈǸЇƾƕɀˊқӶԞɄŗͱĨj',
                    'message': 'ˁǿčԛ¹ƮΌɍϑ×ɳˑхĐǎÓңǷ˩ϫǱʀ\\ԥ҉ŬɯǮМı',
                    'arguments': [
                            {
                                        'name': 'ҜƥƕŅЫѵćsʪğ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': ')ŞǫяиĄϐ\x92ϴѠΛɣc\x80ӧɑӇɅƶʼsѮ˝·ǋϭԦ҈\u03a2δ',
                                                    },
                                    },
                            {
                                        'name': 'ԫ\x9cŎőҝŤԆɹƑăƂѭ(Åŭʵ¿ɲńȹϼşÞΒʾŴ\x86ъЂӅ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.937935:+0000',
                                                    },
                                    },
                            {
                                        'name': 'qшț˧ÙӢЩĉεɐӹңкď҇pþɪ\x91åϜ҈ɤ˘ϨˀԁȉѰ8',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.938085:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǝ\x9dФ$ʌӺɄњėʱǌĕєhӫ˸ƐжȋnӆѓҹÔ·ѺҡԆҌɁ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ưĚв_Ìı\x98ξΧΤӓӼҼ˶ʈäɝƎ$ДËƬυЄ˛ʔĿʣԧͲ',
                                                                            'ȨƯͼлʈɏԌ\xadŉР˙йǈ\x88\x8cˊԁȊÈϰʆʨπŧΆΙљч\x8fʅ',
                                                                            'µŅӍ˹ΧҟǍӣĆƠăǐϞЩţʯϴœɩк˦òƻ\x9fԬ@ӂƕӁǜ',
                                                                            'λЯśêǉʄЀʙďȀО#jʱƘʘŁŴÈɇƵØ\x8dЀɤΆìƭżʂ',
                                                                            'ЬZƟG˖ϩǬђƥҤaÁԪɞJѣʒŔХΝӱԘӽϫƑǋЪήǹа',
                                                                            '˥O¡ΤʹǚӷϜʔ҃ҐԠƟсӟ˴ŎӍ×ӱȆӻ˯¹\x9aƤFáȫҜ',
                                                                            'ȟDƣ¢ƹHǷԆз¡ȴєπͽ¬ȽјƷȦŔ.ЁȏϒƄǘ?Ň5ҟ',
                                                                            'ϱɎʓЯĹ;ЈΡɧъƶͷγɟе\x86ԮԪёΛѣәϬʐ˴ϩɿ1ҝȍ',
                                                                            'ǡѴӡ҉ΥǥĴΎʄ5юǒӴíҤΝϮɢĚʰЃ«ԊҩˎȃȥõТВ',
                                                                            'ƓҥԉǀVґΧɌŌ˾-ԄǱȲ˳ѨЧǋҁ³ɾʟɯӢĨƷǘ]ſȫ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɑžӷ˳ŘǠXyųЦĖ1ǿņѮʯ2љyţЍɯzŵͿΡƏ˔ƍX',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212316.938646:+0000',
                                                                            '20210208:212316.938656:+0000',
                                                                            '20210208:212316.938662:+0000',
                                                                            '20210208:212316.938667:+0000',
                                                                            '20210208:212316.938671:+0000',
                                                                            '20210208:212316.938676:+0000',
                                                                            '20210208:212316.938680:+0000',
                                                                            '20210208:212316.938685:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¥ĎȓЮĻĿǏʐǣ7АęĔJŻӭѸÍ\xa0þnʃЇ˓ȝĒɆҜːҶ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            881548.2981488042,
                                                                            -91273.00214434626,
                                                                            977723.4019861671,
                                                                            708784.7758924986,
                                                                            446104.4244869987,
                                                                            -15756.498596665508,
                                                                            628868.419715795,
                                                                            615821.1067350026,
                                                                            754130.0467647688,
                                                                            929904.7906625136,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x94Ӹ\xadYñʓ˴¾tќͰ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Πԗ¨θȮȇǝҏ˝˭ȾĞӏȼˈƵǜĜħȬʦГdѤȕŗɥŤƵǈ',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ƿ˺ψ˴ǼҠҧɉƛϮαӋä˱čΠǔ˷kăƧʓ³ęɒÌƙӂ\x8aȇ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 150809.6342178873,
                                                    },
                                    },
                            {
                                        'name': 'ԬŶÒϜ˶\u03a2',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.939705:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'æϯʜU>ʝҁÕ:κБЇԖÏӬԒҘԞŉӱĺǢҢ\x8cΙωMíԓϥ',
                    'message': 'ЯǺӚȄuȖɗΪηкԒ˯ћ,ƅҧȳňͻӓԕɠxϦ\x81ȟɞǫĈƕ',
                    'arguments': [
                            {
                                        'name': 'QԭґPԏұ³ȪƞӅˬʕŲgƷłDɹ\x8d»^ВҡѹȲΠŎňӂΒ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212316.940384:+0000',
                                                                            '20210208:212316.940410:+0000',
                                                                            '20210208:212316.940417:+0000',
                                                                            '20210208:212316.940422:+0000',
                                                                            '20210208:212316.940427:+0000',
                                                                            '20210208:212316.940431:+0000',
                                                                            '20210208:212316.940436:+0000',
                                                                            '20210208:212316.940441:+0000',
                                                                            '20210208:212316.940445:+0000',
                                                                            '20210208:212316.940450:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѱϘɐЎΚś\u03a2ʒƷѹýǔʮӻьė0ҴƘʨΑȆØώǔņ҅ı»Ɨ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.940778:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ļӪɡҾқҌɯĽӺǵ^ǥˠҐǮéàϖȡʣǓȢʩǒŚԚε\x80ȼˊ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3883216403447393567,
                                                    },
                                    },
                            {
                                        'name': 'ȁƌɃͲͰΏϻɫ½ɓǶˤˆϏʌԬZƒ\x7fɿ˛ǷŇƛϺψʃ˛ҿё',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5008491585751579188,
                                                                            -1825523390843134224,
                                                                            -1404306958098521398,
                                                                            5649375622616990351,
                                                                            -7305847119020827227,
                                                                            1227121223359227670,
                                                                            4041098785784555881,
                                                                            -6487057372580945901,
                                                                            -2377886792874724336,
                                                                            -7375998157356218507,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӇĽ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˘ҊʧȯƜĻĳ·ѼхžͺğźȝȟΕѵ˺ԤʢƝӶхÅǔźԙϮΚ',
                                                                            'į\x89ɮǘѰ\x9aԤϝŢɒѵUӒН\x9aŪɊüӈȉϏнȱșĞėǦЁԧĥ',
                                                                            'ӖɊҋӔǈ¬\x92ͽ\x83ӏȖƱŭűӈчʒ"Ф\x8aӶ1Ɔ7ǔĵĤϕԎϊ',
                                                                            'Ȃùƪ\x8aӄӊ˭ΣΘġͰņӤőʪϧZԤƃїԉ\x80˛ʾ\x91ќγ\x85Ƴǯ',
                                                                            'Ӹ5ĲZ˱Ƌ°сǺʄ3r´ѝϤǜȉЛϐƣŨƞΤɽȖ×ȿ5Џɸ',
                                                                            "ƽţ'ɋĖĆЩ˳ǩʻгɰŎˮČеӉŧϟЌÒįȧіīņ`ǩĺϴ",
                                                                            'ЭTʇ˒ҏƕԎǞă§лǩýÚ˳ϰłԁӶӺцHѴҕЇƜc)Ӎӿ',
                                                                            '\x9cȬѬϺΏʹǉАǕŌŰѰѤΞ\u038d˵˺ăϢǇǔʤӼȀѾ6Ѡ¾ͽò',
                                                                            'Ǆ˽ƏȢӳʄư9лɥǰȅ˪ҝǎʛӯƌόĀçҮˬýҦmíƶƺԝ',
                                                                            'ǫѩӞŮЍĥƊȖԋ]šÿƅʺЖȇ҉ˇҜ˃χò°°ƟϻϮtԃΏ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ĳɴɀ\u0381ðѶªԥȵћŉΓʅ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 269568.98600193684,
                                                    },
                                    },
                            {
                                        'name': 'ȷɵôɾŭȉУʦĩ΄ȰěȺÛѰЌд\u0380ӎζǥЇӑ\x90ʃʫ͵ϛӕ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8386229996232184225,
                                                    },
                                    },
                            {
                                        'name': 'ƘğƧԏʖȯ\x88ɯˠѸqȄҎ҇ƍ\u0383ũԔƇΰÎŵ\x8bΙʪ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            214330.3803292337,
                                                                            409611.227389892,
                                                                            -16337.948514866439,
                                                                            850614.7793804962,
                                                                            246457.80921645858,
                                                                            818299.4595397813,
                                                                            680621.1474041955,
                                                                            710299.7990851373,
                                                                            257300.19168605085,
                                                                            991911.891129663,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɵԜɅźˠȺ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '¿ŊӉú°ӜФȋŎãρø҅ӜɢƓǘӵĽӸjťԎˈ\x9e˽Ɵɳ˹ʽ',
                                                    },
                                    },
                            {
                                        'name': '&Ľҡү˙ɟҫ4ýѨУǣΨç˫ɲϬ9ǫ\x9bԫͳ÷ɠԍŁȊȠĬǇ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x97ĒĀԌˌʴʊɸ҈ÒΧѳĐɑèԎŊϑaƐťͺƄĢɔήɟЛň\x8d',
                                                                            '3ӊŤȼĲӉΥ\\Ϸ9ϜφҨĵɩΪǷΟȚŷγōҞԂȟǍϧΠ˨Ϯ',
                                                                            'ĦÙ˂äΈǏӌθǕÓƸͼȾʊЉιţȊ;ПMУʄœПɹːӷƎƞ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ǳ\u0381ƬǼɑҁØfΐҲł˚ϬţŦ\x93˃ɐˍԓШşґɈģԨɾƚʐö',
                    'message': 'ԨʥɇáÅҡȋˢʀΗŞȠȚdϸɖ*ЏΚέʵпӲUԨрηӄeć',
                    'arguments': [
                            {
                                        'name': 'ĈԄғ\u0378ǰѳʃǘCÐŅφϴĂͿœŹþϮӏ/ԝ¿œͶŹÒʄɜü',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            284769.04709578364,
                                                                            292798.63172774133,
                                                                            380220.4203632194,
                                                                            605662.4635885971,
                                                                            935658.5522155166,
                                                                            38901.47071172492,
                                                                            158226.7097607995,
                                                                            230085.31981918938,
                                                                            4465.207884904987,
                                                                            -9506.83040974893,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˦ŉ1tɾΛɁŽǆƎԬĨ%ȈҰćŽ˅ԕĮ/dǼÔλѥĊԖ\u03a2ԡ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Į˃Ƥɸʖȹͽs\x86ĺπŎcö¦ƟģӦѓÖţˈ˥ÒϵɊԝԮ҇ϯ',
                                                                            '®\u0382ȁӔʟƕУĊѥHцüĔȕsÚʉǣ2ƭӞɘӲԌϦҞӁî]ƴ',
                                                                            'ʽĎöıͳɫйψX˥ˡԝ\x8a#ҶҠGǧʩŜԎȤԮˀ˒%ϳɫśǚ',
                                                                            'Ǖ(Ŕ˧ӂ!ɟŻ˅LɈҩLӻȩˏƔ҃ɭҎԍсªН\x8bŋĳºӗ\x96',
                                                                            'ʧ¶ÒεʁǨԌMѶɖԩǐЅǚћȿâķȎȬȁɽ˛ÀpɄѴ҂9\x8a',
                                                                            'ʲϲĤGʺVЃχӭӼƇѵØģo[ѭԋ˺ōľǠˋϘѫ˦Ϻ`ıȰ',
                                                                            'җ˝ɍϩԍ΅ɷȊԈǵˆѵΜμЯÎ˭ʊѥŎǭ\x9cʃyfу˯˔ǌĢ',
                                                                            'ɄќҘӱϜϙϞ(Ŋʕ|Хшëԡǐȴ\x96ɓɕӨƊÈ`пԕѸǻǗϖ',
                                                                            '+ȇԇЬɡǽǵ\x99ɧѬˬȡϾФ΅ҵǃӠŝԈŌ·àѧ\u0378ǭʾА\x7f˴',
                                                                            'ȉȓń˧ȞȒɢȳĈӛKΚћĥʄá%ǇʄѨԝ1ΞϼЄFԊÏϙϞ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϵ;Η҉É˺ӺϥЇπș¢Ɍʍȫ\x97%ʨҵɚÙ>nԜKÙφÃҋʦ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6188547300658542292,
                                                                            4662336719492780956,
                                                                            6831102622292988081,
                                                                            -3853077348713770288,
                                                                            -6496821541729588273,
                                                                            -999178952492916264,
                                                                            -7194196806727869784,
                                                                            -6411993684441552877,
                                                                            -2177214787093082437,
                                                                            4238714920139029432,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8fʗО˾Ƅ¾əÊĠ:ĂԉŸɚɼǾÛΪ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.944403:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѪǚЏƻƂϺӂѬβƴŒеԟ4\x91хȉԧФrӁďͼёãʶԢԞɈȈ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            423407.84065528674,
                                                                            847901.3864623553,
                                                                            111473.11206637794,
                                                                            24992.425145274756,
                                                                            927749.3537495561,
                                                                            608198.1476513922,
                                                                            335292.7469131055,
                                                                            -664.3729858248844,
                                                                            450605.12662284146,
                                                                            1261.5997411774733,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˨ĩąǢʬƋ|ąAЖǥYɭӖП϶˒цҪȗʡǬĶԩ¿ʊλˮˀӪ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӷЇȤÂіԦŽ#˅ҥŅǙŒԘëšã1ҙӁҪΥ͵',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
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
                                        'name': 'Ȏʽ˰ӊѴɮɸĮȏуΰΛΤʳ҃ñљԓȓüĂɤѽH·ѯŝ҆Ĩē',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5842266099213305413,
                                                    },
                                    },
                            {
                                        'name': 'èǂßϷІŉlŗʽҲŚuԈŚžĝλʿî±ÑǻțȠӛ\x92јĺĢ˝',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            962427.5395711132,
                                                                            398776.6027619711,
                                                                            507137.77585607197,
                                                                            -31253.17058820212,
                                                                            241377.0269192519,
                                                                            446241.6099216525,
                                                                            35164.92291305115,
                                                                            779644.966139003,
                                                                            276932.41509796766,
                                                                            300794.1413857273,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '²ˇ΄ǼíҜèǇΑɒ;ĸҒƷϘѽ ԄȿΖϢɫͿ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӯҊўСϝπԎҀɍΓȡҮӔ\x96ŵёfʦѬhӶǳʂ\x9eʳ\x9fȥәȕά',
                    'message': '˥ǲ˓јĠΜħƓŹîŴ¤dѸƌüϢŨƢјųÜPԁΏѠ΄цЏʦ',
                    'arguments': [
                            {
                                        'name': 'άɢôʖĵҶύɍăԠӐŢψȻ\x8eнȖβyĜçƋэQкƩ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7338528103683805996,
                                                                            -9158130131556433803,
                                                                            -5985459091263025808,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҭȇøҬ϶ȽʙҼ\u0380ҥӹ˓҇Ё\x83Ƕҥ˙ȻëĎԩĺäӓȓȼOPȔ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            240309181996265033,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЦČŢîœξĐȥʳȕɓíάǵÎǤԝǇ¿ʞΌԘ\x9eҰǂ˻',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            779145.2426927168,
                                                                            298036.60557696293,
                                                                            628364.247995539,
                                                                            483961.68137537944,
                                                                            288711.7531550816,
                                                                            802092.1758121678,
                                                                            476560.3296261217,
                                                                            217425.98091615224,
                                                                            455133.57514632144,
                                                                            336992.2992181967,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʥӺӁĻʎ²ӣɹɠ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7180867057583457961,
                                                                            3624290353307545984,
                                                                            -8985882650503880544,
                                                                            -6207103252192573991,
                                                                            -715810922132539555,
                                                                            8081142692485887610,
                                                                            -2295025038722245920,
                                                                            -5595510881776959822,
                                                                            8881020211930390912,
                                                                            7386812620560817059,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƢԚΏʨӄҿɷɳ²Ҝŷҡϔѳ˧ŀť5ÈΎλº2ɹʦ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˟ʅɌͱɪПșĦѷщХʛƣʼĸǺѦòљ˶ƂȈ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2978201081814886031,
                                                                            -9080147749862231142,
                                                                            2195725713070499709,
                                                                            6675716019086987886,
                                                                            -3157521369250486786,
                                                                            8669498190644429538,
                                                                            1144813658013573891,
                                                                            2416706806989841448,
                                                                            -8903208350969879408,
                                                                            -4075746371796081150,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǎǡԕ ҌϺɓεƎ¸ɝкĢлϱщӃĨēʵǌЮѽдҝη˶ӲɊō',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212316.947544:+0000',
                                                                            '20210208:212316.947558:+0000',
                                                                            '20210208:212316.947565:+0000',
                                                                            '20210208:212316.947570:+0000',
                                                                            '20210208:212316.947575:+0000',
                                                                            '20210208:212316.947581:+0000',
                                                                            '20210208:212316.947586:+0000',
                                                                            '20210208:212316.947591:+0000',
                                                                            '20210208:212316.947596:+0000',
                                                                            '20210208:212316.947601:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԣ¿ȢӨ҆Òԏһ˕Κ҂ӫ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĒԜƈ˧ȸ^ɼΆɱÃ{ќĴѿӔұȕԄǗłҦCЂyӳҬ\xadɭɲц',
                                                    },
                                    },
                            {
                                        'name': "ϢʧƌȆĿӋɳ\x9dψƄБʐ{đŅƅ'ЙǈӂгôΩçɔ҃˖ŉƪψ",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.948181:+0000',
                                                    },
                                    },
                            {
                                        'name': '˽¾ƦыßӓéӶԋʦζΘҺɀόÓΕŸΎŷȇɜЌҠЃ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ԋ5ĭɗÐҙ°kǀ˧ϮΰŭуTҖϋǼȶ_ʀưłȏΧώˊʨźӓ',
                    'message': 'ĝԭƽɭӨŭʢǳУŹfǪƚìԉ˪ÍԦf21іǥāњˀ/ςȗϣ',
                    'arguments': [
                            {
                                        'name': 'ͷϷǐ͵ƿ*ŅòԏҫѫǐҢζӢΉѿϙ*ǪÞðѝӇ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'Ɵ˖ɂƆѼθԡΨɭȿЪŵϙ˱ǶğÛhã',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8213304188275101484,
                                                                            1074695344041399502,
                                                                            -48552278810301859,
                                                                            -4796831950047800807,
                                                                            4072681503652499898,
                                                                            5292652639978528823,
                                                                            5705814617786207319,
                                                                            3549485185990649528,
                                                                            -2557768356546154028,
                                                                            572931147892724357,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȏwʶÊƬďĠƊ4Ӹѝɖ\x96ƯсҽâSϠηÖӖ˰Ͱ҉ˌΣ˦Қ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.950264:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'еϽǫĹӑĀЯ¾ɫ˂ΌΔŉŻħζĉ´ʈȀɷԤï\x81Ω«èƺƤ=',
                    'message': 'ƄїÖǹҡƘɆĆмԃѽòťcЗϪѿǸɚȰρÅϿԋzӨhŠɦǖ',
                    'arguments': [
                            {
                                        'name': 'ŌʣӗӉТɚԠ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ŝɪˤĻɂǮÞϩҧԥʼԐɃљҋˠӃǃǳҙƯZьȉʔɓˬƜ\x89ʃ',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ũϛȄ9ŀƓťȬрФȭϕŒͺöĻƙ˟ƻ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 538138.228810632,
                                                    },
                                    },
                            {
                                        'name': 'Ъ҃˨;bж\x98КËľˡËԚÁâʊǎŅȂӆҙӤŅƖŮ|ÓҺɩʫ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212316.951222:+0000',
                                                                            '20210208:212316.951235:+0000',
                                                                            '20210208:212316.951241:+0000',
                                                                            '20210208:212316.951246:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǁ˕ԌŠǻəИDʇьƀăщ΄Ҋ«йԛǯːРçƿ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ǔӝōб\u0381ǮѳҮĿϊȕwȅΐȰ\u038bЗʉĔĸʷȔˠȿDԜĂʴʫȺ',
                                                    },
                                    },
                            {
                                        'name': '\x9bίY˻ÀɫА®˷I®ԎÒ\x95ˢЫºҡXșÕҕ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '͵ŮҢί3ƻψâ˻ǟ¢ȊĤ(&!ȝFˀŀҦʝÿƃǫƔԄτ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                        ],
                },
                {
                    'catalog': 'ʠư¥ϝа9ĒȐʭoǜtԥĔұӮǜЀǓͻśɘĴ\u03a2ǒωѝ?Êƞ',
                    'message': '\x91ӂӕӄԩӹáʽюýǋӍλʍėбˊγДӠǪJБλɟыâӹԮψ',
                    'arguments': [
                            {
                                        'name': 'ƒОȧώґɀϾӮȉˇЅčԏΒΚбá»ҏыǚģѥʶңĺȰ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212316.952261:+0000',
                                                    },
                                    },
                            {
                                        'name': '˘Ύ΅ÂþҐˢɜѩǍŃȿХӨɢɑ#ƻɺ±ģԌŰŌó-',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ƿαɃТӶƘͰͼ¯ˉ˻ɳѹƢцʜŸƢʇÛȷːЍȸɶʻʭ-Ãƪ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 522476.72272659175,
                                                    },
                                    },
                            {
                                        'name': 'ϰĖͽŌǫΉԚЛķ`ɓӍύŷνī',
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
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '|÷Ƙ_6Úʺ\xadνӺ\u0378ϥÞ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 12091.250609086623,
                                                    },
                                    },
                            {
                                        'name': 'ԝўѥӫÌрǬξϋϲł!Ӥ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6520384491217324944,
                                                    },
                                    },
                            {
                                        'name': 'ƩȎ˩ēȇͶҼ·ƫІˋԘĘϽǃϫŁӬѥ\x91ƄЇìζƗҞŬ\u0382ʜ[',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ЁϤΤҵʍQɄ\u03a2ǿԥæωгďϕϳŘɹzƧӡԆєȣѺ\x7fѨ˽',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԍ9Ρ}ӢͽхǏùшΗѕŚwCĸƮжćЃԫпңӝԍΤǢ¦ĪЈ',
                                                    },
                                    },
                            {
                                        'name': 'ÁāҨ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
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
                                        'name': 'kŏͷŠ¤Ԇρþʂ˷МħpáĩԤǶҫҪ\x83ċƟɃɽƇԉƸ×ɪħ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 782932.265743838,
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

            'identifier': 'ԈKǭʕǋ',

            'categories': [
                'configuration',
            ],

            'messages': [
                {
                    'catalog': 'ƾī',
                    'message': 'î',
                },
            ],

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
                'identifier': 'åϭÌԔҰϱϴϋʈΣҼʗïΚŏԊƴҭλǍҐĥĞ϶ȸϱYǀɤ˲',
                'categories': [
                    'invalid-user-action',
                    'access-restriction',
                    'internal',
                    'internal',
                    'file',
                    'file',
                    'file',
                    'os',
                ],
                'source': '\x99ŢРéƠȩ\x90Ϭ\x98ͽдӐŵȢƩҵɁϽӚÜѳϛ˲ɖРЉʓςнs',
                'messages': [
                    {
                            'catalog': 'ʟϾӤaɼƼğ\x9b3Ʉ\x9cϭƯɇăԗ\x92βŎ®\x8aǔɋ\x90şʉ>īҘ¦',
                            'message': 'ҢҀѷӍϬͼćӇk`сČǲˬȁĦ«ȮЖfӆͿɾуˋȈȹѾȳЦ',
                            'arguments': [
                                        {
                                                        'name': 'ǈлόɷΆQѡ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Č@|ӐöÝĈɑɐԨϦʋκήЄΛȐÝ˳бЧÚͷĔ\x86qдʾfΑ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'д\xa0ˏL´и\x96ʣőӔ+ƟTF҅ԧ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɱʓɹʼΓ·ЧƥĦȰyÎгě®ɉҶʇ¡d˔ʵѬѺѬӿɸZØ@',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 181021.38547293545,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ξňԈʚȋͶ¦\x85ƷýƤļ҆ΌȝżȊгаČKɼIѶНćĉő',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8466890502213343208,
                                                                        },
                                                    },
                                        {
                                                        'name': '´ΑԋИЂΧńԆӨģɟǇēŨ¯ӆŋӆʽǨƢҸӊϓȋӐ!ʺɷϜ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӏ½:ŋòѓш·ɥ\x8aƅàǐΘӢ˵°ȦɱūҷǷƼʁϴū¬ɸǿ\x91',
                                                                        },
                                                    },
                                        {
                                                        'name': 'φҳʡ˾ȃǒ˵˭õťɝѿƻ˗\xa0ʵωǙȘŵƜƋɃԑό҈ŝţ\u0383\u038b',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϣԒ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 739450.8501338933,
                                                                        },
                                                    },
                                        {
                                                        'name': '2ϧ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 602825.9824714992,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƨ\x92ŌъϧĴƌƭЦʰÎЈӟǼʋƃʦѸđĕŃΑҴǅǄʄăƞΗІ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212316.914125:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѴԟȒ}ɼ0\x81ӏ%ŻȂzǨLĘʩύԔɀҨӢϙԙŝӖ&*ԅƺт',
                            'message': 'ÐΠū;ҫϲĚɜƣĲӴʯçóǺԀгѨĉĶɺùԘӳ³ɬΖǗӶЮ',
                            'arguments': [
                                        {
                                                        'name': 'ϻŢ҉ŁÑȟȀʖϜ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʒȌҺ˙ЈеǋʟΒљˇԘËɾȂ\x8aȄņƳЉýҫęøьú)ϳӹĜ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212316.914816:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҙ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 520250.57277833717,
                                                                        },
                                                    },
                                        {
                                                        'name': 'PĴƕ˭ЂΦÂ˨ҼΠǴĚǄɈũŅ\u038dʲN¶ǙˡǺľϝȴʌЅõӾ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӅÇΞӇґХƹęƦϐϾ\x9b˛ˣˇƎʾ\x9cȊҲƢӜͰʈ½ѯӈ~',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7034157195178599279,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӽ¥}ƝχtϪ<χϼӲϽϴǙȏ˖',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϫӛѥǰYԙάԀŸȨо0\u038dľ҇ϸȟȋԞɣ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ЍǻȆȁ˄ЄҢǂЇî˙Ƒ.\x91ňʶ>϶OΔɸӫÝǃϥΦõŠŷ\x9d',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǈҝѵԢ§ΊгИҼшĎӽɪõǰѨѹȄƟȖħŚñ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Г',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x94ȗƦ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212316.916332:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʣÁϖƏħΧ7tēɛʺϣԖºǦȉūțEŵʟΙϚơɾĭȮǞΦŭ',
                            'message': 'Ɓӎʕɂ\x82ԟÚԮfЂƾҕ\u0380ѳÖRӀɻёѲΟ,ɶż\x9bƟǥ˂ҏƎ',
                            'arguments': [
                                        {
                                                        'name': 'ΘϰыŮ}ӣ˓аӈώsňτÎАҎʢɪɧАÆȃɗ϶ΥЕҶŊµћ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'YѨs϶сłƶϳʖԓЪЕ\x9eŢǰǇ\x95ϙEƘΰÑҏԖўΞÁӨѶ\x9b',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǥԡ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '΄(ԊΘөϜ҅ʇƦƄ\x9fΗТŅ\x9dɚʁŚʳеFhɕԇʢԙxҮκª',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x98ѧԢ˦˒ĥ}ϪĆСĨԟӠɩҪǘǝɅŴ΄',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǰÍk\x7f˲ШɎΪĈ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 620141.3535210164,
                                                                        },
                                                    },
                                        {
                                                        'name': '˘<ɵNӆșǏ8ʿ\x87ӡĎԡǭΎªʕρșςţόҵǦĄϯɪɈˑ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'œǀň҆SȼüőќɶȟЌ˳ԃʖřϋ©`ʂ1ɛǥŪсȋ˳в#ϣ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϯτʐ˛˦ãѸϵǲ*;ѷ҇\x82ȲЋUυпȽҠϴɶѥƖAʰfǉλ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȇâфƶӷѽȨԜŅԒ\x8fʽǺ0ԣúРѼìƮҽ*ԖƗ\x9bԢʶИ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8461352724566675980,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԘΜˍǑzπƵȲѺȁҢэKȿѹɚǇϚяѽѮ9ʴ˓ŹӊЁȧ·ʁ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ŭͶŊɃӁМ˜ңũӶͶϣЂǄȖζɇθxɡȣ˜ɝɯǱԑȧӟϟʔ',
                            'message': 'γʗϺȪηŬȵɗưԊ˵ǴgqƨԀƟ²ɨÔļЃДtɘҙǰƣƅɑ',
                            'arguments': [
                                        {
                                                        'name': 'ӛɾ˄Ǜуn͵ʃŐƯϖӣċНԔϚ&˚іЗĞ˃ɬӫй¼уӃ´\u0379',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212316.919592:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӍЊϝѦĈŎʂêȰɦƬӰӅӬ˖ΧΑҥЇϓʴѺ\x85ԪǉȚɴАʹ҇',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ôɬɋʸ˨ΐmϳЙ8×ȓɱЂʒӽȑФѨԛҞ˵ƬĆȕ\x8cϚԧʇʟ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǻȮɰĞEЩÚ=ˬΉĒʲҡӪŖͻɷзώÅ{ҖŒ¥ьϐӜƎ\x88ι',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¦ÁƯãͻϫώӋˊɕŵΝ¹Ѯʥ\x88ơËԖʄ¨ɮěɛɁщЎçǕ\x9e',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʛ`Ⱥ˃ȁҬϬú˰\x9cΏΚњɌ҃ǷСĕПΧʡLԧrɰćǼȹӲɿ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'œʉoÜ˷ƜʂǽԅΖû·ČϤҭZŭ]зӺŅʩlȷʠԀк\x7fԋ\xad',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƟҬç˴Άˋ;ˡ\x84ÑŤʢԬȣ\x99ƧξӤѾĝǹƈɔɬΓя¿ЇУǲ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ņĚźɾXȵɹι\x97ŻΥҍЭȢǎĂ\x8aÈŰȏ«ĉŗɉʾ\x86ƳÐԉχ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʸǺȱņľрĐ˨ÈЖǔпɕƊʔϢŜΑ-ҥɑǉʱ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȩѤˍŚДɆуρ¡ҨɝjϓˆˠƝӃԐQʃȣȝęԜ ɨƁϩΩԆ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɖϥϋɖϞ\x83Ŀ«ЩȚ\u038bƉɽĚϠȹéŅЌȕ3ήɋԂĐ\u0383ӉÕƵ\x92',
                            'message': 'ΠȲʮκʛҫXαЬѺ˒Üȵ!ԦѹϫMˍǢȈɗ˅Ċĩ˟ƧΝßӖ',
                            'arguments': [
                                        {
                                                        'name': '˳ʒƅ\x99ŻȾʛć',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212316.921429:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': "ɗɳ'",
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'дǐȡ\x9f0њϢǫȅĖĤį\x91ńc!ů˫ǩҝʺӁӶňȤƦőγdÊ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212316.921726:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϠјҽŁĥҡҫȂżʈkΡǚέëԝƃϳʓʅ\u0383˜ÿ³ʎпɷӷâ\u0383',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǁϾ°Х·S.ʐź,φ\x9dЇȥϑÉ$ӜљŽΧºи\u0381ԓɉ¤уoƁ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÌĬҢԀԫӸǶȨBͺӃϐӑϱʶλЀãԀI',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '˲ɺʏ\x8cĻĸȯ˓',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȿʰЙԠ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0378XʦƆŨҼЅƱƜŕȖȤȭʵʽȒ*Ж®$ǷѷǙȹѯJǄΰ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 186895.97110171377,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȃѠâҁǾҦʟ~˥ɕÇϯДѦŘђɁԘΩɉǲŢƅȲôǭҋƐ¡Α',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϨҸƲӚɠ÷ƍǦȒѩȯұϋԥ¼ņ˅ϠŰӗȊӷЧαÏùф¥ώw',
                            'message': 'ҋňɠӆԑ˧ʭ@ҔĨΞƙΊЂӷѿ\x84˶ŮɴԡȵʽҙZã±ɵγʜ',
                            'arguments': [
                                        {
                                                        'name': 'DF¤ÔÙϯΞ\\ǷʖРһѳĚǌÃПҌCϾΜӮϷȐ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'СTſјSǃŉLԇέϬӸǾæѴȗ;ñ^ʘЙuʁƬƮĆƭ\x9cï',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѳϐӘ½ӿ˟ҫˍәŋӽgζϵǁӒӭЁʠfǙ\x87\x98ʝʅϜϾŵѱƏ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÜӁ\x95ӴʃќʆʫϿǨŧɘøƔϏǡͷȟӒʌȺÂԈʿ¤ˍʃӢn҇',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʀŜȏϽďpӲΞɶӭʿТƅÞϩÿʼǹƛ-ʄγņʍïǘʺŎ¨Ъ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƺĿǒӘư9\x91Ń˦ĉʑĬ\x83PɃё¹ӞʄˊœɆʙyȶԜɾьТ<',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ʈž=ηҙɄѮŷҟψř"˷učԟƗĚю¸ÇŁѿЋ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӐʒŪňʓJήΛŁ\xadĊЌ<AɴЀӀȰ˒ǱŜλÆFϕɀ˔èЖˬ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȯеќʎ;ɉąЅȇ%ԑѵвʞҵǋбҕԢeѾͿ҇Ԗ\x8eƞĝʔѠλ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212316.924569:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÊuȏϢʞƉҶɦȗU',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΐhТӲȮÖkʸԅ\x97ʝʹѕţОѢӐ˥Źў~ȈҝӰưύѡ\u0381ȫȄ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѭvŨ˧µϝϖҲʁӦʆЄӝ˥ŀЇĩӷ',
                                                        'value': {
                                                                            '^': 'bool_list',
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

            'error': {
                'identifier': 'g¿ˏÖ"',
                'categories': [
                    'network',
                ],
                'messages': [
                    {
                            'catalog': 'ʘγ',
                            'message': '¢',
                        },
                ],
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
                'identifier': 'ğсȳɲbƭӵ¨ƾƝbɾ5ɻӏùϮψ%˖ϕҠĴ˴ҔʧҕžӲщ',
                'categories': [
                    'configuration',
                    'os',
                    'configuration',
                    'file',
                    'access-restriction',
                    'os',
                    'os',
                    'os',
                    'os',
                    'invalid-user-action',
                ],
                'source': 'ʿÙҪɃΡƵӛéƆӖǠԫшlǢEŲΪѵɖŔʺϦζˊβǧŢʀʓ',
                'messages': [
                    {
                            'catalog': 'ЩтҵϘ¯ÉɐȅɓϦĹӐ¨ʖąÅҁɵĒư¨ǷѮȅ¾еҢӀ ҂',
                            'message': 'ҙʶϨȿɫˠôӗԖόŴ˂kДΚȘȘѡĘшѭнlɏeŵČұԟѴ',
                            'arguments': [
                                        {
                                                        'name': 'WʿԖΪжӰΞΉԐϔʑϳɨ˗ʽ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u038dӨ\xadwӇɢϿíjœӼƑɪάЊѠƥҭǟˆɮͰĖΦƛƂәŐź±',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '϶Èīҷ\x8f¾¤YϽӽťП¾ƔͲҗ.BΏʶβӅʰȴЎƧɄ\x88ȻŪ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŔǇ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҞʘêєŵϭҁŴɩЍЏ\x8aƎӚӤɎʼ`ȰîѺĮŌ˚Ŵԑϻɢys',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǶЀ-ğ!˔ɩ{ԒЋѢȢӪțďҲƠҏʭÉɐɰɞǕƫ\\zĭƳ\x81',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӆˆӇĸƞ9ќΛÌйОĝŲћƔΚǧ˦£ɗ?^ɴ˯ϑƕǠąǼǥ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϝˑF\x89҅',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɈӅƊöГƙǡŗªǷȞΑԢƙĵǕ˻ЅѥѕuĮ˰ȆѬЂћʇɃϩ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'цʖäǿʍěӱӃ¦Α²ʐˏƆaƴlʫ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ƃ\x91ϜГСó\x8fʠϫҮ\u038dʝѳϑΈίԣʮӯȍʧɨӑԡ҅ÓˈÂΈŢ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'уkΟȺяЬϨʍƤǀ\x8dΏȧЂЭǉʕȗ˅gƽˡȉӎʡɐъȔ͵Ͼ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8530202934101117290,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǷŘñɠӒҁǆ7§ђƧ?ѾǇͷҶđŹӫȇȐʦeȌɴͲ\xad½χͽ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 806294.9333940566,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԝ˩҃҆ΫǖԣȾĄʸƨ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212316.956986:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȅˤΣơ(+ѥƽЄǇ\x98ȹŸҴƉļȌȩPϵuoԔϛԛLˠϧ\x8bÔ',
                            'message': '7ʭιΙΞþ\x9aӻωeªҴɹ¿Ćq2\x85ǹà˙ƈӟ=\x8bȡ˟ѽʠҚ',
                            'arguments': [
                                        {
                                                        'name': 'ԩ²Ƀĥɓǂѵ&x^оˁʬʳԖгƃC÷\x8bҗӪӞǐ¯ǈɏɱĉ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '¨ħ˛΅dϯЇ\xa0ƄѣӐ\u0381Ϝʕ+bɌϏΓϬϛʍ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212316.958136:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҥӄ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӫͶѓβʎŢќԭɗőȍá_˳Ӥ\x8bʋĉʂxΣigʔϊСӑҞʥӵ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԨʳɠѢˣʭʢϜ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԊсˬҜťԟ×Ǜ\x96[0Ӡӧć\x92ѾƿˠǱξȺ\x94ƀŀҤƸξ¥+Ë',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŋЅˤϤӃƧˣɩхŽѦӴѿW\x8fϬɿ}Ľɑ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɏх|уƓТΌϳϵҀx˃ԕͼƜԉ¶ȅӭÆżT¤ŸεͼƝѹ\x92ŕ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɚҊ%ϖŠƟͱȻΫʔŷњǖӌƸԁӊ.ѥã?ĪȉИчψɦ˗ġĺ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ђӤˋɳT΄ɹɸ\x98ɦЬżēɶɳåŷŃБaЋԟɑΒɻ\x85ũѰ\x88Ɓ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӅóʁӘȤӿŨ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Э\x9d˛jɄľİĿӬԅʘΙĎЉʥ\x91ҍūҫѺ҈ʣԢşʠν˺ϣηÐ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'DˁѴЌǸƖqȷϫĈүʘԘĒ˙^ƱǵĺϥȭAɇƌѯēŝɚ˧μ',
                            'message': 'ʹƟȁǔϛÃɫǘÌöΰƕҟäа²PΟȣ#ӌҗńаȝΑϤńЂɏ',
                            'arguments': [
                                        {
                                                        'name': 'ƻҥϔӊύΞ\x95ҤѽʊӂӼùҶƮϹ˟Ē<Ӛ˗ʙUϣȷʳºаǮĊ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȩЪŨήƳXЃ¡Ώ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212316.959892:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʩ˽ƐΩω.ҭĤѰǒȱщ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӑƩԤԢНnўċxǄɛώÕʅɀԃҖ˳ʨϩτɦʗɐͻȀiŌǹʈ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЕːʷÅԞİɰһ¡ȴƥͺȱҰ\x93öϮо\x8cĺƞ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212316.960341:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϪǅƲзɑӥ¨ӠԓǤőȳԡȇȪ˟Ϩ҄ďeɩͿʭΞǣʡDƣқĹ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4349694243778522796,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɦʅӠʇəҕӌӽΖ·ǬĪƃʚˑӑҠʯý',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 266368.6360625988,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĄǼӚƤJЪ˚ʹϹƄɶ¹˾ɭѷʛǫˡɮɜȮҚнȄϛΝǺȹȉđ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ªѪėГǭҪäϿĠѴ9ʁȕȍϕЌʦ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 497708.42046017037,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʤгĽȬËȆˮӅ\x9fˠÇʐΏ\x8eѬŋǤ#ňX=ƿ˩˃ǺƯѴԩȽ@',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϻҕά˼҈ωCǮɥϨЄëɝÑϷʄʍЇǛГƟȪӇҹĮǐЏѿѣǣ',
                            'message': 'ŜƼǰʻȹρҁĝҏ\\ĵȻèνƯĸϪǃŶÄԤʖʁѓʯΒʲҗԧϮ',
                            'arguments': [
                                        {
                                                        'name': 'ϫēǣ}ʌŇ˧ǡȮѡǳǑӲЎTӇňɍӓҍιˡԗʴңƞїőÑ©',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'шţкǎŦ\u0383ʷ%ҲÈШ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӣΔƘѤÈEіʳдŦӌȊԒʑӃWӶƴ\x8fʨԑ˻ȐʼǊ²SϷԇȤ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÁɧѤʢȪɃʑъҴXύυìȳǊиζΐɔ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ǎɻ҈Ĝ\x81ҕРԐνͺ:ǫ\x95҄ŇҀĿԩɔ҇ЭюɊȼ\u0378һИјҍп',
                                                                        },
                                                    },
                                        {
                                                        'name': '҅ѷЮwжčЄЖ\u03a2',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƽŖ\x90υǼƗ˾ԂȰӡɭӖ\x97ƔĂȨЦ˽җЛşͻЌƝǮșɘөϪѭ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԧ5ԅɵԠŻќȩǅ\x96ŴʽϔÂŽΔƉńκ˟÷ǡ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӂCʯʭЮвşɬüΐ\x90ƶӼȐΔĎΤКί',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ШˆʓЧĽÑ˲ωέĘΕƿPĦĦĞПąѫņўȵͼяĝУǢ҆ǽѲ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԧәʇƈˬ?ɔƯΐϘÔȧˊФˡĦ\x97Ċ¬ҁƊĕԇǞ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǋԟРʜǟɌўƲδ˪ȣӜђɀˮѷʺĒƦȭά˱Ңi\x84\x8fØθĨȢ',
                            'message': "ɳԜǍϝßȸӦ'ÊӝЄϞ˘Îĳ\x9cͼҚǑɴîʴǃ¯җȌԆǬ\x8cԃ",
                            'arguments': [
                                        {
                                                        'name': 'ƾ~ŠǕũіʌӕˁӹʜĢҝӀѺȽ"ɧЄƁɏԕϙğʏǡʱºłҋ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ьКνBԎïčɭ~ЮκѺ˗ȃĕžп',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'џҳǰȚʑĴõԢǊҡĠǼ˺ͻCǮōļƝ˔°ѝʱҸ»ñȠѩ\x83я',
                                                                        },
                                                    },
                                        {
                                                        'name': 'δǎԫӶƷC˅Νӷ\x8fʍΆƜнӐUĖ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӆҖнӷΒúн¡ƅИʓЄΟĉДИ±ǛѱƞӒɖʌΫҠ˜ǈτʢù',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǧϱʘϧŽʀΕƓ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʡѦ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212316.964377:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'υƋԊѥĢΠeɠ3XѰ҆ȩȩφʕҌťʰǢѮūԕҪ6ŋȪȜҬ\xad',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ų',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'юƐ\x8cͲøӴŎHȪɡпѧĸΩwԐ¾\u038bʿҾλïŢҳΡʅо\u03a2ǀˊ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϰɤǲѶÏӈǃчȅΆİԏѼɒͶĊϦ ϊͽҡ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʂѢȫĆ˃ӂÛɁŬʋvІƮƠȀѥϣʅŷʦƧѰůΌįϨӿ ˾˨',
                            'message': '˳҆ǤǗіБӾσƴʬǒҘЬɡйѽ~ʤūkϣ\u0378ƚɧΰЊņ@ɂ\x83',
                            'arguments': [
                                        {
                                                        'name': 'ȳѮȽɮ˴ЁҌɒӀǗ$ɉ òɨǇԃɳԊ\u0380ǌɂɽ&ơұØŒăд',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'yúʹԛǢåόΕȽǓ×ɤЏҝHɄőкǿϠӴ˔˫ӂӰ\x81ƋѣҞΞ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '2(˺Ƀя\x96Ƕǧҋr%ĀӨǂ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĀÚſήǄʅÐӁϨ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 568208.5021166577,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΰЙЍǱǣмŚìϵùǆӇѵΚe{NԖϴѷǬҶӡӈԛƘ%ӽΎƣ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x84ӔšэǼ\x9fȨѦ˒ҋƌ³ЗϡǊ6ҋ\x90Fu]ÕȰѫ\x94ɲńԧφą',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˉШļ˵Ś\x97˪ǩƳҙƄrǮ϶',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5337520185426028872,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȼöƅȟ\x9dǵω˨ӪΖýĢɨȯĦФŊɽƹĬϮôƑʚ¸оĔ˗Ğο',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѷċԆĮ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϩΰɏ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '/ĹӚɧϪѲӰĞ˫ΝŋʬǱЬÛśӞ˺ˊŐǒ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212316.967748:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϩѱĩξśωbшϒϬбӵ\u038dǎĉ҇ʟȚДzŇŖΤҌҌĜʷу˺ǲ',
                            'message': 'ȤВSю\\ӽkȡĖѼΌ²ʦǃΓưΧ-ҴтŦųíɠ#ЉѣҌƓÛ',
                            'arguments': [
                                        {
                                                        'name': 'ʗ|ӇѩÁЫ\x9a\u03a2ȈɹrҳƻȾˀӀǲгџɒƤʩљђž\x8b\x9bʕОΕ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϐ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '*Җǡš¼\u0381ΖӰșɒǀԑјЉįĘʭѪÀƨҗļǄґѱśυΖ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ҵʽ\x90˸ŐңƘҐʁєɽӴȜ¬ЅʔԉӌвχΣίԭҡǙˡνWҬО',
                                                                        },
                                                    },
                                        {
                                                        'name': 'άƪXȤ¯ӼħҭφÔ˂αĕϬϻĭ²ϋɜ¯ŽќėƯ\x8dгƥƐԪĚ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212316.968671:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǥuɭРɲъŇͰҸˀĻí\\ƁϹԣ\x96®ɔȂБϳӇƺȤϡ˽åʙń',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϾхP2ΘʨϴƃӍ0ǝkɚçϧīǾɜɒΪĜϠƇϋĽΧʎӡƫӁ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 174893.69116602658,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÑťΣȡƫåãʵтŹŝ`ЋˀȀ҆ïÖƯȟП˛ƸïϮЍɽǍӂŎ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǯǊϹƎԙѺϽøŇћ¶˫ƘθШ?ԂǙ˩ҡǳ¹ǤӃŐϏȻǡƐƒ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӕ$ϩ˅ÐԑѩӋÄżɋĘӲΌΙs',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '&Г\x84iuļҶǗɹȕΖǣĒżѵǜϲЍјąҽ΄hªţȮƮзʸ˩',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƿiдÄƽΑЉuȜЁǍϧĢԥϑћӱʸǒ5ӞҨ˄ҖκĊʂϘʚ\x9d',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ŝФ˛vФ×ѩ˯ϽԒ¡ԃ½ԠʔρӺͼŮũɪͻBȈ\x88ȚǙэ҉Ù',
                            'message': 'ʪŷоǘŎњ˰\x85ϽԐôԟӌȊԁfȠȮĴŲӎȀŊˉԫȮÌ$˽ǎ',
                            'arguments': [
                                        {
                                                        'name': '£<ǿ]ďºǒЫΥгʙǤ˖φ-ƶʬчųàίŸΎρÛʫ˧ǍӂË',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212316.969970:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԘѦɤԂì҂ϼê҂Ċƕҗ˝Ϯň˼\u0380ϯГõ ѤʳƇǸȁĨĆŷœ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '©ЗϢ\x84Βƻ\x84ǠɣHƬɥǫҊΊǏµŨɭȽęäѺҲ\xa0ʳ˄˧ϒЊ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԆɊdƧΙ5γΔǇ£жȶԓǣËёЬ:ҡ˔xƪƶäʤɰŢˤʣӗ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȒԍȁҴəȐєƚĠÉѹƣЄ_βeΖǫɹϏ\x83΄ʗƘ`ĳҌåȟӏ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '¶ɆêәɀФΐʼʧʮԐ\x91ʡҸԖв¡ĽȅͽÅ±ӄϗVŭěŔȽȺ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӏ\x94α˅Ŧõ҃Ɓӑ®ȏʦԡЌКɮÓʷ˲ŋϰƱԔП˓ɉʒɾѪe',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȯϺԤҞǴƟҰɝˮ\x9bЖԔЈʇyɾĵ˦ĽȨƶŻҮǛ\x97ѿƪǡїӯ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϖʉԐĀ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѷ\u0383Ŋóë+ɓǡñԘ{Ԉťҍ҂2ԞɁʵΙWʙƔ\x80Ƽ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɎfȺԂǥŷ{;ӔĂʰɶȈüǅљƣƈÜŬɝɩ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӧı˷Ӂ\u0380ÛɦΊ˺ΨēѯӍνɔƘĀзα\u0380ӚŐ½ʏɄąȮfӭ¹',
                            'message': 'ƑЫϵƴҕ:wвͽȯȣźǛ;ϋȸҤƢԤʵӉԇ;ø¶ϖЯƥPҧ',
                            'arguments': [
                                        {
                                                        'name': 'Ѣ϶˘БӖιĤǮǍɱʓơŰŹƺȵ\x84œƚЦǼԀ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Оџ²ưʾ5\u038b!nψĤĤ\x84ʈMɟɎţǞƂpȮ;ĺǅƛ ¡\x97ŗ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͲʵѥɹʈɛòÕ\u03a2Ϛϖԍ\\ĨϜʱuѰ;ѮOкʨQďQʋťԘº',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϺƄāǧ9ʪͶx˯ԣЧќΩѴͿƗȈʌʄŀāšƼMʵEɛӷҷȊ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 36021.87108295041,
                                                                        },
                                                    },
                                        {
                                                        'name': '±ōģї',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4290751247868681273,
                                                                        },
                                                    },
                                        {
                                                        'name': ';ǣҩϦ˪ɢϲɐжьˆӹ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ːǯəβʇ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӆ\x8ehϬʠƻԨñƦһϡȿѦǏŉÂčуƷƴȔψϯˢΰԐӥɟʄŽ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŔӘƿÒϴ˯ѡŶūԮ\x83Τ˙ɟϹǑƹɤ2ƿǦѶ\\ƕį£Zŀ\x92ǎ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɯ϶ĐƝYʹǣɇȃƣǚõDşʓ¾Џƻʒ&˖ǾҥŀÒя:ϭԞÈ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ьǽҟ˴ͱцŅˑ_Ӈ9ӕɈ\x91ЖΆəҟɉíǬÇ¢ңюȟ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212316.974091:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ŞÛЗҿˈʻϽұɄҁϫԠӪѕŚ4ӾǦЯ<\u0380ǞǬɺѳϱϫǿԛε',
                            'message': '\x7fѰŒgˇ˺ďEƙÊʫȃŃԘÔОưɿѿȩѹʁĒȘʛĨɪүЎӷ',
                            'arguments': [
                                        {
                                                        'name': 'Ȱҥ®ӋƖ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3425234157726418671,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʂұϟ˷Ј˞şϯЪ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ī˰ɻԪħȦȐȻɲϩхʜŝф',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʑ\x9eÝļϘɋe¶Ǘ.ϻΥΠÐʾǃтуĔʻϓ/ίҪǬ\x89ѧΒ´Ӣ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'rȺ˅ÍϹĹҞĆԦΉȚҮƯ\x9c\u03a2ӋѷƴɼмĒĮļYCӡήƗ[ӌ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8463059813785397710,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ηŝ£»҃μѭќʂǩÝ˂ƹɨοйūңŜУ«ϨÄ(нˣîǄΟ\x9d',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9fҝԒżϋƝʔæҷρнƧԊ҆ʆҚVӎϢĈЋѤвĀńЮǅ˅ȑů',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǵϚġҥƸšΗĽLц©ŪêѳƥÒΆɃƝǵˊϾϑȝɸǡӜЗˍͼ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ã˞ƺRӕȲБ"ɄȢӂŁΎȍɔǛӴ϶ϺҷΤŏ\x84ϾđɌϪ¾¢ƣ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -810875456950653288,
                                                                        },
                                                    },
                                        {
                                                        'name': 'qɏϞЫ»ԝВϗȰhȵfɢÍђԚ˄Ͼ×ÉĬԀ\x95ȃȊ˲ϼэěԂ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 236186.59470324055,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԊǇаʂǧ϶pưѧϸʡϕ\u03a2ƚΤ\u0383ҦȷŝŬ',
                                                        'value': {
                                                                            '^': 'string_list',
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

            'user_error': {
                'identifier': 'Ŷƫӽ˨ѭ',
                'categories': [
                    'file',
                ],
                'messages': [
                    {
                            'catalog': 'Ѫ]',
                            'message': 'Ƌ',
                        },
                ],
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
            'minimum_level': 'info',
            'output_file': 'ŴҕӀԇʷƠКѪЏǬ˰Ȁ¡ɐ\u0381ωďľ#ӞƖήφͱÄ1ʚʃȯϞ',
            'output_console': True,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'minimum_level': 'info',

            'output_console': True,

        },
    ),
]
