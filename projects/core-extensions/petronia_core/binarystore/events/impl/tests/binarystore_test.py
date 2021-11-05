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
            'mime_type': 'ĄԐӝʦǄϞñÅӄś҄',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'mime_type': 'Аʻӏ',

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
            '$': 'ԩźʢу҉ņ¥ʀƧơʾǜѠ˖пԚqɪfӦˋӃӹǆӁƯѾʺ\u0383Χ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -1211962245331983263,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 269063.5512079923,
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
            '$': '20211104:182113.838296:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'њԈɅ¬ѮҸМɺÙȰǨӃˆ\x7fǓͺˣͺӆÊҕ\u0383ϸ\x85ʜͻèʇbƒ',
                'Ϥȡ\u0382ѝЈϫϘѥ\x9eγӼĠɃōƕ&ӜϢŊцŕЎӢϗκ˅˹ɣʓİ',
                'ēƌȣŁɯŁ²\u038dҁɚěӐāĔІUɒÎ)ŸѢФʟгƼԇūΓʵÍ',
                'D˳ǨĽɘŧӥ\x8e=TŝѩʧԦqy¶ҥȇʱĄȝŬ\x84ÏĨͼяȘ҃',
                'ϓǝԖķJѺΠҗʙθѴƧǢɄlӖŦ¥ЗȏќҝȕԣФҺǼaӓӖ',
                'ņЪūǟΫԧХЊʠ&ΊǍ\x82ɐÚδɤԪƱ!ˊ¿ӸÜѵȇȂ\u038bЗƃ',
                'ƩћŀĴǚɛ!İѪŞ҂ҷ҃õрı˶8ʳƊgԪѮȤϩΈˈÖΛΡ',
                'ϿǖʓǻćӖёϷӝ\x83ůZǫºΪɨƷʉёƚѣ˧ȋԂ˩ǝǣԇôǃ',
                'ҽǴЇЁɒ¡˹ɓʷǤӎʦŬɛѸÌΞʜϧєћкȐƭʍӉͺÏǎÁ',
                'ҹńɞ\x92e&3ЪЋӏɅåf¯ŎTСɯγ\x8eʍ>ˡ˳ɌÌĈрԪх',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -2542764539253462746,
                2312862965932254214,
                3438527657305163572,
                -5967292218699305251,
                1506955831444617167,
                5450378076582126105,
                -2350545432920846982,
                -693274940288020929,
                8976404933094120523,
                -2144748329803578279,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                670522.752370987,
                555779.4756915723,
                94507.37859614444,
                63518.21717828166,
                687717.6445849205,
                578137.1843424313,
                659256.7738797461,
                692583.1821104446,
                789905.1645486129,
                330109.0451600799,
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
                False,
                False,
                False,
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
                '20211104:182114.779172:+0000',
                '20211104:182114.796177:+0000',
                '20211104:182114.813069:+0000',
                '20211104:182114.833038:+0000',
                '20211104:182114.849721:+0000',
                '20211104:182114.866532:+0000',
                '20211104:182114.883016:+0000',
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
            'name': 'ΔƇɖ³ǜћHĚӰň\x86ÍϩɻȌҬśuŴ͵ЛѣÙӢЊƷ\x8bқɲӗ',
            'value': {
                '^': 'string_list',
                '$': [
                    'òϣγşҦˋ}ʩКԒϷϿх˜ϼъ˵ȺƔНΘěʚǾƣ\x87ǴԔʎã',
                    'ѤɄːƤƉΟȃǳȼҔȃЉ\u038bƒǙУдӦӶϧҐ´ηϧdĖłƞЦ\u03a2',
                    'ŹŤЅԏ-\u03a2ŸӣźŞʹˈɪň˕θǙφΠȽșДňǂν¯ϬΏǻʘ',
                    'ʗǹҡ˾4´Σϖ˴ǳ_ΤĜԊҶӪѥʊћɑЪÓȈυƃƞԁ\x9fύ³',
                    'ȐɃɈǻʢД\u0380\x7fƽԈ%ďȞ÷Ϳшɥ\x8aKȜjϓϗΕĒNрÞʭʠ',
                    'ѺͺύRӢԦȞNčȤŴ\x8a(щΙΈґĽӁ҇Ӑԗɾϗήü{ĕiƨ',
                    'ҩΩЦɃƃӡҚϥķʐѣԡʒkОSҕɒyԃɩĎɏƗðɉҕŚЌӟ',
                    'ӂˠ[ȫԐǵƈŁ\x8cѥѯY³ʄŀ˂цϒǱϻɑтeͷʇ/Bƽː\xa0',
                    'Ґɻ΄ТĩЀȥҭʽϳΣtþӣTȑӹњ«ѮԄˬɶѪȂԡΐǣĳʠ',
                    'ŚǸ˭ԙǜGӐϘΣ;ʋȧϻϚƟ\x8aǳĲϟθ˟ĦΤȬŒɦÑnǫҬ',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ă',

            'value': {
                '^': 'datetime_list',
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
            'catalog': 'ͱǰʄϾʸҝԚȏ˙QȠǢĚΠYƵ\u038bƌƃƅʣҺίǠŒЇϯɻНӎ',
            'message': 'ϢВļѧӒΏɌưϳȎʠϒ˩ƢŇЅƺ-ҽѠĆÀȬϏζѢɶпшŁ',
            'arguments': [
                {
                    'name': '*~{ɠO%вĹмɬɏΗПȇȎχ/Ľ\x98Gş',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20211104:182111.786165:+0000',
                                        '20211104:182111.802826:+0000',
                                        '20211104:182111.824527:+0000',
                                        '20211104:182111.841170:+0000',
                                        '20211104:182111.857415:+0000',
                                        '20211104:182111.873795:+0000',
                                        '20211104:182111.890223:+0000',
                                        '20211104:182111.906325:+0000',
                                        '20211104:182111.922645:+0000',
                                        '20211104:182111.939299:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ÄUөŲΧ',
                    'value': {
                            '^': 'int',
                            '$': -3596616562558315030,
                        },
                },
                {
                    'name': 'ҐςʁǏԎƁљЎɍɗ\x9aņѝȩ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -2702663786275762334,
                                        2854308376779628571,
                                        1387588783199551296,
                                        6549162819904482147,
                                        8056172482192106645,
                                        5268970913126266893,
                                        1380893113928342643,
                                        1030372703504894984,
                                        -5707384243638114469,
                                        2162913092579683056,
                                    ],
                        },
                },
                {
                    'name': 'ћ˷ŦНȮǕ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ƩΧєԠͿóǨǵѱɛĖɪTи΄ŉϨӱĉήʤůÕˤ϶јϬkϊǈ',
                                        'ɌΟǉǀĬΦʭϗǚϙ͵ˀ:ΫŧʵƧƾːĲ«ɨī˲ȍԏǄϠрҭ',
                                        'ω1ƤǏĲПԈѾɧӨԖҠ˖\x8cΤцč,ɪʤOѪěӢҮʌΥǅ˱Ļ',
                                        'өĉԁƴԒ¥ɜαƪĐǃaΓĹ?ŜӎʆбǕҩҐԭЬɢVҜȧȦ҂',
                                        'õǲɑŁҊԀŦԏ˒ѯ\x7f\x9búɌȌǽĲяӕЗŏӯϜјįĎњƀˊē',
                                        'ƀ®ȟΙΝУϰӰҌǆ\x98ΡГȧùĴΝɩěˑǚčîǗӫ±ѫĿĔө',
                                        'žæ\u0381èǣʡ\x80Ƽ˃˘˳;˗ԀȫK9nɟ˴ӷɝϮ˦ʫËϑҺҗǊ',
                                        '˰;ɬԞƍŻώѾԔʌϪΖȕʳΉˀ2ΨĕҥøʼҎԭÏɖǃ˺tł',
                                        'T»ÄřɯɁ˴XʬȈmЭäԡ\x91čğčναȸɼźàǵ\x89ǭ?όÐ',
                                        'ʊåаҙĩǇGȅ\x91ƿϒŝʶԮͷοԬɐҦԜӥæƨѾIˡө\x85ӻč',
                                    ],
                        },
                },
                {
                    'name': 'ÒļԃƪϡϸӿӔLɰėK;ЩʲӶǚʴgľèǇηКƊʞ\x8cĽȢ',
                    'value': {
                            '^': 'float',
                            '$': 274484.1541517131,
                        },
                },
                {
                    'name': 'nЂά˷ûɓоѽEŃǙʙλŐԥҐǜөǠbȆ˂Ӷ˫ȿɆʷųчz',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        -60835.390654707255,
                                        521848.75019944145,
                                        60096.32421598869,
                                        622180.7751183655,
                                        760547.673627019,
                                        877854.5592226271,
                                        552346.7142364844,
                                        391998.98919314425,
                                        649542.6429857041,
                                        899073.5250366884,
                                    ],
                        },
                },
                {
                    'name': 'ȍɋȻӨʟBӖҩˋӲнҋҕxΏ˽ҘҪԃäǟʞӭўƿ\x8aɒԭeɞ',
                    'value': {
                            '^': 'string',
                            '$': 'ʈxʳŤЃËǚʆŧƂiųӆ\u03a2ˁα˭сλ:ǄõзΡзӆĶAеϛ',
                        },
                },
                {
                    'name': '\x9cĩȺѭ',
                    'value': {
                            '^': 'string',
                            '$': 'ӮĕϟӷľѹÞИȚЎǢ¾ϛУ\x87ͳєѷńʍЎԞ˒Űɐ·ГЪ¨і',
                        },
                },
                {
                    'name': '¶ğϩТʺ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'Ҙȹ¿РԨČŻâӪεМƺǃðҸÞӀơʷ˶҆Ͼ3ϹЇ±ӐԘҰӆ',
                                        'ұȷ\x9bΚΞ͵ƟÂȓƘ\x8dӪ«\x91ǯɩ2\u0378|ҊĴɄКƸQө¬ɅǛР',
                                        'Ѡȱǆǃ¨Ӝ\u0379ѥÂįҴƾɋƣÈıĘȸǲǒϺŰɠɈʄΡ^\x87ɂë',
                                        'ʳҝɶϋʤŸҰљ{ӻ˜ɛąɍ©ҠļÊÉɼʷ˪ƒĺϪ҆ĎсȰԔ',
                                        'eQ\xadĹȊȄϫЅʰҴ˽MуȤлўϸѝʂҧǿXɥƢȍҙɺӵ\x91Ŋ',
                                        'Ж͵҇ҒͲɂǟȩß\x8bǋƁiШȧǽȬtĦѡ³˘ϤʿϠύƲɄПϦ',
                                        'À\x7fԔЧ\u038buя:ЈԀIΎ˲ŲKÄȚҁµ¥ԜѭʢƧЦȩDƶϜρ',
                                        'DҡәйɵώѪ[ŴƑȶŌ+уƒ!ӯ˱Íđ0\x8bɬȺѨȷȞ˦Ƌđ',
                                        'θԔǪͻ˗¿ˮʎǿ˖ˈ¢лǱѹҖ\x83ю͵öŬ˺йȦʶУӄкп´',
                                        'ѿӶΒүj\x89ŗΒǈѨρơʺќӋψv!\x8eÒҠӯɊ\u0383ŻőìɩŹŔ',
                                    ],
                        },
                },
                {
                    'name': '\x8aԒ^(',
                    'value': {
                            '^': 'string',
                            '$': 'cǶǖˊ\x85Ѐ\u038dӔːӢșEԔØRɦªɭҾқƳʩɚ²Дƈϲ²ӽ\x8b',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ϤӶ',

            'message': 'ͺ',

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
                'catalog': 'ӓǗхȢ\x91ѥ\xa0ӷǻјʭӅȣÄF˷Ė˨ңˬñɛωǧЎȨӍɹʿʦ',
                'message': 'ùϲέĵȂΌѻϑƌƤФƫ\x87ÁӊΕпЅĊɸŊ˝ȫ8¾ǢŌиƩх',
                'arguments': [
                    {
                            'name': 'ϧԝԡ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20211104:182110.314346:+0000',
                                                        '20211104:182110.332313:+0000',
                                                        '20211104:182110.349387:+0000',
                                                        '20211104:182110.367290:+0000',
                                                        '20211104:182110.385046:+0000',
                                                        '20211104:182110.402908:+0000',
                                                        '20211104:182110.422621:+0000',
                                                        '20211104:182110.440217:+0000',
                                                        '20211104:182110.457956:+0000',
                                                        '20211104:182110.478505:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'Ȣ\x8d%éŪɽ˲}',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20211104:182110.614718:+0000',
                                    },
                        },
                    {
                            'name': '˃ÌͰ@ǟԧwûӶɥ˕ň÷ѳĲȀϝцFƘɹʧШϦ˙Ͳђ\x8fœƿ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20211104:182110.680799:+0000',
                                    },
                        },
                    {
                            'name': 'ĈŨĈĔϝ/ϦŌĶÒsɬȼȐƔѰøҬˎ\x80ЂɨΖԋȦІЀŠY ',
                            'value': {
                                        '^': 'float',
                                        '$': 437189.66236456216,
                                    },
                        },
                    {
                            'name': 'ŢʃүԎǆ°ƈ',
                            'value': {
                                        '^': 'int',
                                        '$': -2519273120001919786,
                                    },
                        },
                    {
                            'name': 'ʼ¥¿ĊκΈţČůÐɷQȰЕШ¢ϫӷϔȰąǜδЅ%˪ωпɲá',
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
                                                        True,
                                                        False,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǺΰƛϾ,\x8fҨŤ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ǷͲùѥїʯTȁП+Ӆ\u0378Ġ\x8aѝũ0Ѯoƈβ4Ǌ΄ә˟ƟƬʭƁ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
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
                            'name': 'Œ\x92˕пŔˎ}ɼ\x88ɧҎӁЃąŸȂ˯)ƅɀҔɝЌǸÏΌѫɚƅϝ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20211104:182111.442435:+0000',
                                    },
                        },
                    {
                            'name': 'ΑƑɻǬΟϘȽӸԡюGЬΨɶӱçӽɏʱѩɽŮȆӧã2ӏҊĔȼ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
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
                'catalog': 'ΩӃ',
                'message': 'ə',
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
            'store_id': 'ÏӹҥԦЁͼԗҎŽ҇ӪÛԝʞùŪȜˏɕ³҈ƍ\x96τĢӋµӀѳҬ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'store_id': 'É0ķԊă',

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
            'state': 'deleted',
            'mime_type': 'ȡʕʧψәĿħѾԤҌÓƼȔŎȼƄԍͲКȳѓȮʬκȿ¨Ñ\x8cĘͽ',
            'sha256': '9ɼˎϲɉĴԐӀÃǼˮɓȜΓH¯ѨŚĦʻƿĤƅP2dɯМĀх6ӯĶӟΨȷӼSӮ˧˻ҾQԨˤǰĊį¸ӾˌɩСǶΤő˜²ԢˏÐΗǈӨ',
            'size': 5271274693856804817,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'state': 'active',

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
            'store_id': 'ϴѩUs\x9eˮѽ;ìχѧĞÝ\x8e ŚƋԢ,ɩѭȞӆ6˛Ԏ]ɨҽѨ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'store_id': 'ĝƌǇɅ\u03a2',

        },
    ),
]
