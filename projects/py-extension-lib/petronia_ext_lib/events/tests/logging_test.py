# GENERATED CODE - DO NOT MODIFY

"""
Tests for the logging module.
Extension petronia.core.protocol.logging, Version 1.0.0
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
            '$': '˖ҫǄ\x96ԥĳҼťľÒЭΐ¸\x8e\x90вȞӇцҝϠǥїȔȸÍ6ϧїɯ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -8803671778471437948,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 230500.34285491967,
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
            '$': '20210309:040211.505336:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ʶͲԬΝȄһѢĻȤŃоԫ3ªĐȨÙѹϛΙϺвɒ^κʜʏԉʯІ',
                'ÃȮ½qӃǚҏĖ˾ћӣĆŉԖȁȊ&ѥƛǆӨ˅PƐş˭ɞ\x95ã˜',
                'èÇ\x84ǸԀңʿʣҢÂАίRКĝ˥Ѻ҈ЀɣϞϵӱͲΩȏe´ӳͷ',
                'ǎ\u0383ƤňһɄʃ˵ƫҧſȝεҪҏкόǑʷřwĢѡɄҸÔΖ҃иş',
                'ʌԕöǙĪ?˩Ԁ\u0379Ûѩ˽ԖʾӡоǀҠҿȗƳϒҕħøӦÄΕˑÝ',
                'ԀҎӛɪӾ˛ӕǨËSԨԔ>GȊĥΰƷ`ăʡəѻµūʩȊ;\x94Ù',
                'ƝɶÖѬьџƥø˵tˏǮӸӁ<ѭεŜАУ\x93ȤĹύϰχѪȯ\u0383ō',
                'ǹȘтӹƚ)ҡџЏ\x98ŢԧȒƳ˳ν9ˊҺϲê\x82˯ѽ¶ʤΝдΦȺ',
                'ƨɸąûǓԠƖƄŭɟȵѳµʼԮɂǲâ*Ϯǅ¦ӦĦ\x92ҩҏɭϬŨ',
                'ѼǫаˌǨéϯĶŮsõ˞Ƿřύδіʅvͷ½ɸæ\x7fȀ\x83ǻʌʪŭ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -5123956160524577998,
                -3300284172569509863,
                4005807881221989516,
                -4222101081571615597,
                -5079260582916972250,
                -2162851034548335851,
                9048531915233057207,
                2294020486685254728,
                -3732429886251984320,
                6522667539993397674,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                786572.2524896205,
                728902.0839593951,
                635224.2780146942,
                211908.70343083388,
                474481.62685164355,
                -74507.222069042,
                310049.85858408466,
                430390.639872161,
                379341.1540515688,
                596324.1913199222,
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
                '20210309:040212.493481:+0000',
                '20210309:040212.514314:+0000',
                '20210309:040212.535518:+0000',
                '20210309:040212.556614:+0000',
                '20210309:040212.577511:+0000',
                '20210309:040212.600575:+0000',
                '20210309:040212.622078:+0000',
                '20210309:040212.643231:+0000',
                '20210309:040212.664812:+0000',
                '20210309:040212.686614:+0000',
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
            'name': 'ӋĔ',
            'value': {
                '^': 'string_list',
                '$': [
                    'ɐWE2ĚζǑͰμҸÂǡΧbmΧŎǭрΩЀκИ[ςǜSΊÅĵ',
                    'ӰѶҜʱTƁϸˋϱӡ˅Ŕ¡ɿϜӝӀɁćΫ΅˰ȰÿjŸɢȈȠ˂',
                    'Щʁʪ˻eȒЇ˻ʣҗªſ˰ӵǽӆӃǱ\x96ϜǝʋЍ\x83ôӤÉ\x9c\x9aĮ',
                    'ʼ¤λ×ˑúɭԗšƩϪ\x97ˌΜƞʻʖ\x9f)ωhԫƖƘșĥęӝӊư',
                    'ʉõ˹ĥɏǳЁϤԏиΞˍǭԧИƮщSþ5φжˏƘԪģĽÿŊё',
                    'ɨΉϦιĞг\xad˫\x9fҮīӚΔ҈ŰЫӵˣϳǞѣɅ\xa0ɔΦ\u0381ƐIѐɲ',
                    '\xadшˑѩͱԔmđ\x84ƛȵѐєԇĄωԉƮӏƓɱǶȦ˃ӱ1˷{ѯԡ',
                    'ΔΡӗʝưƓŠŪũƊǽԊҗζɈɤɎ;Ǉ[ъԠΡʸͺƻѷÒǍ¿',
                    'ȓɮʋЋʙԂĒХ\u03a2Ǫ\xadŃʠӰİŭă´ˌmѤƄ£ʦũДǋҺ:ж',
                    'ΒƁєЫ¿ϡθȏԐȒȒˍ˗ԉҺĆєιÇψςĂʇ²ȿ˧ˊÄ˪˅',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'έ',

            'value': {
                '^': 'int',
                '$': 1952061650842191949,
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
            'catalog': '¦ԥTÙԅԂµ>ҋũʪƚψν˱ȀɸŸϐŬĬӡ\x9b҂Ͽȭ˧Зѫț',
            'message': 'ɍԛӡȷZȦáӒǜčʾ\x80˾ȱѕŴɧXǑӔλäАґҀľĭľρЖ',
            'arguments': [
                {
                    'name': 'ԓкԨPQeДʉ)ϟҞБ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ѽʤҊ\x89`ӕԖʳȏˑǛĔʫѣðҊĤĉϓʫԣƈʗѸʺƽƤȦǴŧ',
                                        'ƪѩ÷-ʧʁŒƳȊĘϿyʥ\x93ԩǰ$ȠȩǟȼϭϷʊȵȃӔОƊð',
                                        'ĹˮӉǎіѺԋÜϛ\x90í>ѝɊĶƤv˳ɣƑ¢Ĭ¶ȗ҅Ԓѽ{Ӝк',
                                        'һǉΥwӢ˙eʌ+Ǹƶϋӡɩ\x94ήüĴɖéB\x8f҃ȅåǡǓɾĩʙ',
                                        'ˑĻȺͳΘdǝгÀEѵ.ͷĊχƶʜƨŽžĴ;ғŒϹͱɺʓĉԛ',
                                        'ǕíӿȇԔ²ˀ¤ÝѧȽzIͲćɕácɼќŕƲɯǪӡʸͲңӽҝ',
                                        'ѽ˭ͻŃӱ#ыÝʁɼѭсƌϐԘʙɠ·¹ңζȥÙаɥÃ˅ʡϾJ',
                                        'əҺö.ĦʲɞǂīľҗģiȊɥ+ŷƻɥƐlǾȦʴεԕƞѰ;ș',
                                        'Υ¸ʥǝԅúƑāȵęϬ҂ӗŘϤʉх˻BҐʬʿǳԛűāυäʾϼ',
                                        'EԫћԭŢ\x84кɥęȆũґӼɚԨ˱Ÿҏ}ԩαưұϵŔĞpȷÊӝ',
                                    ],
                        },
                },
                {
                    'name': 'ͲԎѹ˖ӟNώӰĬϖΈʊǅӬõҸɤý®ʞӍԇ_īϐɲİёϘț',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210309:040209.549986:+0000',
                                        '20210309:040209.564978:+0000',
                                        '20210309:040209.579527:+0000',
                                        '20210309:040209.596228:+0000',
                                        '20210309:040209.615118:+0000',
                                        '20210309:040209.633735:+0000',
                                        '20210309:040209.654128:+0000',
                                        '20210309:040209.673163:+0000',
                                        '20210309:040209.694630:+0000',
                                        '20210309:040209.712443:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ΆяĺƆӨǝɬ)ƶʫȂϲţÄ˘ΠȦ\x8a˜ŧʕ\x81Кϩ',
                    'value': {
                            '^': 'int',
                            '$': -2512939205005794183,
                        },
                },
                {
                    'name': '˗CӕƐÂГ\x86ȡюȿĊʴĞĲ«ςȾ\x8cŌӸǹǉЗȣD\u0380ÜÝҸȆ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        501762.16964038974,
                                        521732.21777765686,
                                        625754.5409774894,
                                        732827.6612299054,
                                        275870.43507155875,
                                        526593.3844444673,
                                        261454.98683518218,
                                        132119.00634170917,
                                        973394.2133848099,
                                        916567.0499889568,
                                    ],
                        },
                },
                {
                    'name': 'ϳȂ÷ȾϩÌȋɾЦʚϒǨ˱˫ԪOοϞœԅΌ,ˀČȞЩʢ©Ѳȍ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'Ùʪһ\x86ӎË˳ɕĴλōӢòϷ˰ɫӤãβӥȐѦüԖӣχ¦˯ʵĀ',
                                        'ãӳˁϭƥӧŕA\x82Rȍϰ ɬŢӐŁǣЖ҅˱#ҟмĹΚȲǃ˺щ',
                                        'Ċ\x8dŷĈǆˏҼɠǙ˶ʇϱȏƑңīĠиɑҘі҅"ȲзƱ˞Ûмɢ',
                                        "®'ȴѓ÷œɁѸҌƕʰκǫѻҼɡÝĦĤǦч§ЇIÄӤҤҹʑû",
                                        'ҞĝϽƬǆȫԐΌĵ©ӓЊKȑ\x9aр҅ǫʦÿʀ˯ȽÎҔԣɈ¤Ԏ4',
                                        'Ȯ)ƿōΜȻUѺО!ƍӚýțŊɨoɶǈȞԚζ˙ЙƇɛϚƈ\\ȿ',
                                        'ƍƥώƫϡŨǦùȋ˚ĻάєϤ×ǹ¿n΅яϮxyˁʒȕĭАЁÙ',
                                        '\x81.ǗīUԑϦØωÞʹGԓǂȚҦԆҰў$ɤӨßǢķωϩѐѥŌ',
                                        'ȮјĽŻɷʰԂѓaPãλтĠЁʿ\u0383\x81Ҵԉ¥Ȟ©ШȕƖnϺ°Θ',
                                        'kįяԧԨƧǶ¡ù\x9cӷϪʧßʍΘϣɰxbêɬϥЫɻÏЯĦũ˺',
                                    ],
                        },
                },
                {
                    'name': 'ӽϷӍŅӤ˘ѬǮ',
                    'value': {
                            '^': 'string',
                            '$': 'ʹŔ΅ʝúϤΘҹϑОǋǒ˩Ӕӈđ]ÌѲ˥ɢϛōǝɭÛÓƮƏЩ',
                        },
                },
                {
                    'name': 'ҎЂʯˢ¾ɜӖӘ<ӽP',
                    'value': {
                            '^': 'datetime',
                            '$': '20210309:040210.383918:+0000',
                        },
                },
                {
                    'name': 'ǧӍʦҪλ·ʳϢɽƆ\xadЭώNɿ˺ĎEȢ˔ҰШˋӀѡΉ˃ŃƐϚ',
                    'value': {
                            '^': 'int',
                            '$': 6815632920234878064,
                        },
                },
                {
                    'name': 'ȶϬΚ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': '\u0381ɠм˳ѿȑ=ŨаȀɗ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        34499.57827684458,
                                        172250.50409206323,
                                        865002.5662410705,
                                        -86967.46633482483,
                                        170201.25621628336,
                                        637255.9315725993,
                                        -12627.37641699244,
                                        898312.839430122,
                                        695848.5809349213,
                                        514927.0323520013,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ҞӸ',

            'message': '/',

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
            'scope': 'info',
            'messages': [
                {
                    'catalog': 'ȡӢƕԜѮ¼ö\x9bҁˏӓӟɵԘƂ˄ЖƨϲȌϷҷӷlћԮȻŐϺŀ',
                    'message': 'ʸŮŅ%ȯηҿȷǦ8јdéʩ҈҉ǱêʼèɫΖ&ʷĜƷ¤¤ɨҏ',
                    'arguments': [
                            {
                                        'name': 'ӤɛӕǷτɊɃʘӖЁϧОȶʓǾ˷ҦқȶЈ_ě:ѡТ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040207.090811:+0000',
                                                                            '20210309:040207.108798:+0000',
                                                                            '20210309:040207.131526:+0000',
                                                                            '20210309:040207.149439:+0000',
                                                                            '20210309:040207.169188:+0000',
                                                                            '20210309:040207.185465:+0000',
                                                                            '20210309:040207.205198:+0000',
                                                                            '20210309:040207.226746:+0000',
                                                                            '20210309:040207.247025:+0000',
                                                                            '20210309:040207.266269:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɰʢĈɬέԉѹΩúӑƐʒԫϼʳӎĕĩǽΧƔˎ˄ɆӢӂŭͺɲĈ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "ÌŤѸѱýƎѻaɠв¶Ƙӭ'ȚӅҷʖԭɠÞůƌʺĲѻѤ҃Λǆ",
                                                                            'ǶϳmȵӶďŀƮјÅ-˱čӠŌӂξтĲϞΝҞςӷ\u038dӆɣĒϥӺ',
                                                                            'ʥңÕH҂§˷ҟјѲсǃǄҋȓϿλѰăƘɵ\x86ȯВӑҰηĮĕǕ',
                                                                            'øȢϙŅÛZƎś·éȘϽȹʙǩҏӃ\x8fԚԨΐ˃љӌӳnѮMƢŖ',
                                                                            'ӮʭʧҲʵͼʙgӦπƬ¶Ȩ\x86˕4cƠϹȠΎfɮŒʷҕЅϴͼѨ',
                                                                            'ɤϕǸΑƶϮЕғԌǟҌʆĶ˴įϦQȡςѦ:ŀʁțпƏmɀʛE',
                                                                            '(ǱȪѕГѱӳ\x80Kō˛ѩʁħōѾϹYǩҋǣ\x7fƉɹɓǛÌʞȮҶ',
                                                                            'εм{ӶϭνȂȤΞˍӐǧӺŭĻҡрԄƊϗȂ\\ɭЌԨʻÔƄҭŜ',
                                                                            'ǐѻǛʄМƬȍƴTΊɽĿƕIԋ\x91FƧʝɧǡʜԏǖӍ]ӥ|ԟɸ',
                                                                            'øЧŮɕǘɕά˒γƀţ9Ԩ΅\x9dǶTѭ˜qӋϾʑɅȠȣɁĈΎʳ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ИґҝѤhÐĨxưČӱ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:040207.627696:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʬԙðEǏ¢ɹԒӌ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            20749.42340270149,
                                                                            537984.3945700307,
                                                                            47360.44251375465,
                                                                            217282.46166168025,
                                                                            391506.0885440353,
                                                                            417955.6873419454,
                                                                            751320.2661401602,
                                                                            351738.74533074506,
                                                                            526073.2352667394,
                                                                            -58008.43470557519,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȈѬѸάю',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040208.056946:+0000',
                                                                            '20210309:040208.083163:+0000',
                                                                            '20210309:040208.102014:+0000',
                                                                            '20210309:040208.118006:+0000',
                                                                            '20210309:040208.132536:+0000',
                                                                            '20210309:040208.148101:+0000',
                                                                            '20210309:040208.162234:+0000',
                                                                            '20210309:040208.175988:+0000',
                                                                            '20210309:040208.191876:+0000',
                                                                            '20210309:040208.204939:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x86\x84³ώɝӸæŃ˧ͱȞίƒȗϹïȻѬ˾èðǀ´ƍìħ}ɓҮӮ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǩǀƴȠЌ%Ơ÷ϑɗæʤΒ\x92нļ/ÎҜ˚ЕɇLƏÀØəԘāĭ',
                                                    },
                                    },
                            {
                                        'name': 'ƪίʧȨύ¾C+ͲӉǏǓёϱɩƅǙʶoͶЩuɥ˳ÃȌ҆ƼѾƽ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1790772462008190878,
                                                    },
                                    },
                            {
                                        'name': '\x93ҠӘȧǖƄǪʹԮуӍԩΪρƀĶҺΆ\x8dȠϟϚƚ¹+čÖ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040208.494975:+0000',
                                                                            '20210309:040208.517986:+0000',
                                                                            '20210309:040208.540700:+0000',
                                                                            '20210309:040208.565270:+0000',
                                                                            '20210309:040208.591171:+0000',
                                                                            '20210309:040208.617985:+0000',
                                                                            '20210309:040208.644533:+0000',
                                                                            '20210309:040208.670932:+0000',
                                                                            '20210309:040208.707768:+0000',
                                                                            '20210309:040208.731188:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŉπʧϲ˽@ЮēɠǥâŧɌр\x9dǮ*ϦƲĶ΅ңċЪƃƈΘЮБ҈',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɿw\x84^"šеɜgӝϬӍ҅ίTђљŭԜђҗ\u0378\x8aЀ$˟ƱʇȂę',
                                                    },
                                    },
                            {
                                        'name': 'πİƆă\\ÀǮɳ»ÂАʹǉƐʗC\u0383П\x90ũɆӰǭOƨӆɖƳǳ˘',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6605589569097163968,
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
                    'catalog': 'ɵР',
                    'message': 'Ŧ',
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
            'identifier': 'ΩáҷщsđȑW\x8c-IҸ\x90αϬ¦ӏүсđßʂςýâ˴Ɗģ7\u0378',
            'categories': [
                'network',
                'internal',
                'network',
                'network',
                'access-restriction',
                'file',
                'os',
                'configuration',
                'configuration',
                'os',
            ],
            'source': '¸҂ŀɐέˎƄʗˑϹсаȒѦį-Uȕð|ŋ4ХξүɯƣiǊ&',
            'messages': [
                {
                    'catalog': 'Ζ˽ҫӳ\x8bɕшɕɐƎđΟʓƩ@ХɖәʰѽѨŅs͵˳\x92һВȎ[',
                    'message': 'Ҩ®ӐԐHϙΛӥȭͼϝ·ҼwǚËHӲĬӟÔʊϙиѿԁӷǵ\x8fѺ',
                    'arguments': [
                            {
                                        'name': 'ɠĨ¨ѫǖõ×\u0381ɣϲν§˗ƽЮДјԥϔțĸ˄ʉʲҍΫѨω΅ś',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 497700.53199066455,
                                                    },
                                    },
                            {
                                        'name': 'WǆѽΦ\x8e˸ҝƢĉźuƱϘӇ˓ѤiʊƚĦȢɕԏøƖѴГ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʩľǾΐѵ6ǢьȸҸҳY˖ǶϜѲӯʏĬ\x9bʋԦ΄\u03a2ˆ˝ϣ$ŝ´',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1088384327695198709,
                                                                            -569401899085700575,
                                                                            -123107493607232988,
                                                                            623778452782742303,
                                                                            -7345901199261078370,
                                                                            3947626694927110894,
                                                                            863631182808424540,
                                                                            -6398744931042559403,
                                                                            -2421666415341538880,
                                                                            8813079706555641538,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '5ǘχʹĨϣʺ)Ɔǥӓџʀԭ²ŘНԧϦCԁǣŉșɰA\x9fԛźς',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x82ΰſǝϵӱҽɦҎԣӧχ ɻȡÕ\x91ԭƲРýңδȻƱmώˤѰʓ',
                                                                            'Ѐ\u0381ǉȩмӦӪЊŨӳѶɦ»ēƒʞ/Ίԃ\x93ƲȎѹƜǕȇ¨\x90ƫѠ',
                                                                            'ӳҳηџЁȯŻͼҋɸYF\xadȠƅԄʘ¿сťЧкΎƗëÔ&ȭʿҽ',
                                                                            'ëЍыˤԥҁЕѬԈҒĈĈхÕƠīžұķŀДǸ£ζӭſ*\u0381\u038bz',
                                                                            'ɯǷΆȀ\u0379ыșͰыŕ\u0380Ӥ˸ɠƂńȩʬžΑŻϊӌԩǭϳ˼ҤВɟ',
                                                                            'ΈʣҦγeǉҐNӐÒBδƌˁΕėԌ˃ζǧҊИ÷ƧĄnŕͰςǟ',
                                                                            'ɯԚԋʄǶŴƘ˅ѼǇwʧȝʱLĨǲʮȤτԬ\xa0`MǊΠΒ\x84ƦŰ',
                                                                            'Ӎæ\x9eўäŵҟȴСЄ\x8aѰbɥЉҭțŀлбҪŠѐƍȁέɨӄÃδ',
                                                                            '·ĥԡŢʉҼĉВ>\u038bАˈҨƠĹҧҤԦ\x8d!łˏÖμ˂\x95ɚʤɓÁ',
                                                                            'ѾaɂĂΛӒőˇlүϤЊѐӣΆοʖƿӸЗȆӈ³ĢÂӢTҚԁϧ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʞ˯"ǺѬԌʗɂGˈ˼œ_Φɼ҈ëҮȂ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ҢҩЎɏԛ¾ԍĤĬåԄʿþ?ϙǶНιҊ;Ϟ\x83˒\x88ΤʦǌΙРȡ',
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
                            {
                                        'name': 'ΠϥȄϗȓʆԮΉѾԡʱѕʫŻǃ\x96ǫӗжҥʧÅҗҋΐɣϴƦȢ¥',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040224.363392:+0000',
                                                                            '20210309:040224.383536:+0000',
                                                                            '20210309:040224.404194:+0000',
                                                                            '20210309:040224.424870:+0000',
                                                                            '20210309:040224.448227:+0000',
                                                                            '20210309:040224.472820:+0000',
                                                                            '20210309:040224.493287:+0000',
                                                                            '20210309:040224.514841:+0000',
                                                                            '20210309:040224.533286:+0000',
                                                                            '20210309:040224.553216:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'â\x9fŪѵ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'íϽσǠҊ¨ĚàѴЬħǎΌǺѭƺòϮʆԊϏĎԦǠmŏʙɳȬ¸',
                                                                            'ϊͶҶō˦ª\x9bϏ\x9cӶȋIȋàҼǽɿǧӞӕӞъϢǳſ;Ԭź\x8ak',
                                                                            'ıан\xadsˢ\u0383ˮƌiĹӪЖʹӽЭāƃеóĒЕȸŐφЕʉƍƖΉ',
                                                                            'Î`ϼ҇ļ§ȲÁȑрǄԪĳѧŦɢѹþ.Ԏҷԋ\u0382ϲЩ˂Ԝɨ×ϊ',
                                                                            '˥B`ʵĭ\x96ȾĦԗɯǱяэǀ˝ŏʪЇѰɂǔˏɎÍʙЪΔѴɏʆ',
                                                                            'Ɯä\x89ВʡΥΌ\xa0¼ǨʋČÆƅoƆʦɫϴϲԢƿȍɷŀˢӋҵьҹ',
                                                                            'ўΙЁϕˡϞќȇчх¢ӶɋŹѧ5УbÒӄ˄ϷҌǻ»uñ҆ìѓ',
                                                                            'ÁˊȱҞĜӤКԋКʗ˨ŚвЛĖԋýŝȸ\u0381κČɉνɝʞȭƧӏƣ',
                                                                            'ɎбɑϴфĤ»{Ɨӹ7ɮƆ±Ү\x91εůăԑĈ»Ќʒ&ϼǚȿԞӦ',
                                                                            'ˑԥ˭ɴòƘƞРo)ӂʈ»\u038bԡȃƬʼʩ`¨ĜȆЬƚuͺԣ/ϳ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҥɯʗѽ˜ҩy5Гɚѫͷʯô˰Σǥi˔ĴұʥιŨϟќƧǚźӟ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            503601.2242837703,
                                                                            168081.98472734628,
                                                                            825902.2483731662,
                                                                            348746.97990336845,
                                                                            746733.3246320636,
                                                                            91711.59588334919,
                                                                            951882.166882134,
                                                                            114405.14972964962,
                                                                            178317.5253421453,
                                                                            309943.6441240436,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͷƚɲŶύs˥ϢғИЅíAƷΌӾѸΓԬԛɄƅ8ʑΛ\x8eԗӃΞϯ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ù˼ɞŗӼÜЎ7бɔėġJҨҶʃ¼ѾƎƥҏɟÈ±γɸμĲX˳',
                                                                            'ѥ9ˆŁȶŊҲƃүІɦиÆЇʉщϯČgȱғÚРǤԁЬңӣӯҧ',
                                                                            'ƯҕӢɲÜʠ˞éͿҗ҈r2iʄǋòÔQ˃АnΙӤÀыõӐ˨ȩ',
                                                                            '˗ťǧÐ@ӬӤАµЍƈŢͱeʐԂƫȒɛˤͽΔʥ¤īŉΛī\u0383Η',
                                                                            'ȗΛъΤͿɅԧçόªӸƜ\x7fԥæҫ·ǣ˘ԚˊƢʣ˻gɯbҿĿР',
                                                                            'ӱƻԞӸεhӜӇ˽҅ЫҲ˃ĿUΎʗԃʶѷːĸ¹ȱ@ˡ¬\u038dʇȯ',
                                                                            'N5ʹË˄Ҳɇ\x83ȄϩˈÏɱԀɒѫŐǈΒ;ǣϖǌΆӴαϺȋѼѶ',
                                                                            'ʽqãʱЅэҢ\x9eǃǓǐПԤɗӬǚaĖIŗWŗъγǋĎǑѯŵϝ',
                                                                            'ѡ˲MПӗºӪӕŮʶŮɕҝɘӛ˽Ӊ\xa0ɏѧӧǒҨѣӹшǹеʥY',
                                                                            '˔ˤ§\xad˶ͰǛ˟жЊ?чҥnηˠͶХħɭKѷӽĎ\x8cȭҼ\x9cӐē',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǿτώԏЙөƜÕɬɊʝ0үƘѱ$˪Ǫ¨Ӄ6ƥÑʃΎ҅\u0378ƚñť',
                    'message': 'үβіɢüЃīϺͽʹ>ӯcǜѤҩҨƛȧȌɠѥɨͿǤƵПʹӒъ',
                    'arguments': [
                            {
                                        'name': 'yЬϨҔĘə\u0380ԝɩýʵˡǷǼҨvҢˡýǾЯΟļˆʿά\x95ҮωȚ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԕĵ\x85ӥϩǆÿ\x92ńҤӠȎȄÖχĻǀȇśxα˩εƷΎˋɼҹϊη',
                                                                            'ĢѢ¿˘μǼ1¨ёƠĈƃӼÛşϛϙ\u03a2ϣϫЕ˲ңǾҠŀƵǔ\x921',
                                                                            'Òаτ˶ɷӺɤЌ]Ȳv8ȽǵʞÇЈȌѮҗЅǮȕF"Ã-Ιѷϐ',
                                                                            'Ŝ¬ˠ^ȴńIůҚĊЮϹҙϿǗǼ\u0378ξǪb˟ɱyǇiԫbāДƍ',
                                                                            'ѱɆƊΖMɂӶțԍǽ\x9eтҩЁιƵԈǨľǭ˙ŷ˔\u038bʒĻÊχНɖ',
                                                                            '\u038dǑ°ǮԀ{.ēҋӀгӱʢˣҧȩӆmĚēðπͼң˧ĘΏˮѪǤ',
                                                                            'ɫΨ¼ʔЕ~Ę@cǲqԫĀΚʂȆЌń_Ҭˌϵ҃˧ѠËȏ˦ӊŋ',
                                                                            'ЭɅˣǦ҄\u038b&äӣƐԅťһƱːçӘqǦçŘѶίqĻƤːšț<',
                                                                            'ǚʩǙӊʽЎυӓȆҷɤӌÄŴЛϕÚӯѨӴʂАҴȧљʗиǰǸǉ',
                                                                            'ÒƱҠѶǢΙǽƍµϱDĊЄɣҞƑƞЊӤΉ|ʐˆǑȷǔɐ\u038dɱŜ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ðӎκаƫӝ¤hϕȎӎȖʔҽоŨԚΨυɧþ˾Ȑǌ\u03a2ǘ´χӤ¯',
                    'message': 'ɔɇƤǳÐ\x89ǘ£ԗƂʆѠ$ңƃD҅=ѹӃӻĲ(ԃЌо˰Ђ˻˼',
                    'arguments': [
                        ],
                },
                {
                    'catalog': 'ʅ˵ʫӰϫͷĊμϏѴʍǪ4Ĉӫ\x8eÎǭɓ®ͱĔŁÔЧ¾ưӢ\x94ÿ',
                    'message': 'íˮ÷ƬsũϷÕɁΘԂǠϷцϢɉ7×(īбӈjƨ˼ǢnʄҪ»',
                    'arguments': [
                            {
                                        'name': 'Čɍ&pɄčɷәԗΌȱԝǬȁŦ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ÙȕҾѐģӚĥáǽԞʶʲŐϒҼѻԒɮԄŒӁϋǶҀɄв˳)άʰ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            824659155481741471,
                                                                            260874973230446500,
                                                                            -1606225600664149295,
                                                                            -9167126717667721243,
                                                                            -3189540188578962962,
                                                                            7676338044070826416,
                                                                            -6970916727784456877,
                                                                            -17202206904057780,
                                                                            -2775143083300242296,
                                                                            -7210707258083990534,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȲԀˤԃҐę\x96ÉӃҀϤЙǖԟ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǕŭѲɞ¡рĭƝѯæѢ¼ɓѳʵǇő\x82ѣˉѾ\x99ƞǢǫģЋĭȣÙ',
                                                                            'ʆ˄ӓÅӊҁгŻ˷ìҀǐɫÎԬʤ_ì˭M¶ԕˮˈ\u0380ɿʾϞġЅ',
                                                                            'ĊɤĮϰÜҒȗɒѵ҇ɫ\xadʄϜ\x97ϮЈҤ˖ʨӲʠʩEɢТɩǬSǑ',
                                                                            'ýƎʻԞɃ˞\x99ҐӽĮЂӀȴģȎǹÿ\x94ԁҳȼӁǕ{\x97ëǲ\x87ҟ6',
                                                                            'ʙ˱ϘŃ)ÄґΧӌҩɳÎɬʑÇKǷ˼ęԈ\u038dȌȩ\x96Ɯqһ҅Ǫʌ',
                                                                            '\x96uˊǍàňΑӫюƖä<\xadҎ[ƬƁԞ҉ѵɂ¬×ϓJǕΣͻöɷ',
                                                                            'Ƿ{ófdʫÇ˕ØҎ\u0378ǣɗ×ɔԢ!ʆѨ.϶ʭQʿѰӡϨ҅\x8dȾ',
                                                                            'ƸɲƀʣɶvȌӪ9˾ԤȖǅćÎҙȁ\x812єĳϥȋ¤ɱʉȣϰɦǣ',
                                                                            'ēɛʬƯɀǄĚοŸˌƛԢʘЏβ˗ð÷ǨќǲӋ˂ˁ¢ƞӊ\x84Ĳў',
                                                                            'țˍ<ӸʮΛΆԪǨҥ¥ƗвҪ\x7fçƲǆэSˋʽєɊϱ\x9cЅĸŹ»',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҆ĘɰǛŜǡχɤ~ÂϜЁX\x84ѠЋ˞Ǫҋ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ͽ¡ҁʬǱϢĺkǛǒƲƔñҲVͽS©¨²ʫȏҺȫŔәÇʌЫŉ',
                                                                            'ƃ\x89ҥѸʆǯήȖύͳѽ\x8fӔ\xa0Ҹѱ˻°οѷªĉǗƍʻҟ\x88\x90Ô;',
                                                                            'ϪзˈϘΧɁɶΪԒ˄ȯȚV˖иÑμ\u0380ťÍΒϵЄώϒéӫ¼Ɯԍ',
                                                                            'FєøƒɱĎč˛ѯΪɎ\x99фǲƍjүвӕбƕ˃C\u038d\x92˳ʋ´ŅЩ',
                                                                            'ÉěЅNΣ4ˎϞîӦˉǌ6ȀŉūӕȕϕƥϊȧӻԘ\x86ѯԊȯÞɐ',
                                                                            'ʶӛ+CэɘʭѻмӸҩǺ\x8așϤàηѪǕĳƾ˧ћӳţңʨĆǸ˛',
                                                                            'ǐȤĳǯͲѸyņ£˰Ưҵˏðɮ\u0382+ҏϻWѵƷɘÀŚνԓҹɔ¶',
                                                                            'Υù˳ǂӚɎFѯµv\u0383Ħҗŗ»ҷƧѠѯɩńđ¼ ш.\x9bйӀŷ',
                                                                            '҅φаȒΒԇƜɢƗҼˁ¡±ԈԕƾȱΫȴѕν~ʱeѷ±yðжҎ',
                                                                            'ˈōɨТНΐhîǉŨΩ«Џʠ\x81ѰйSеÇĹДȠ\u0380ʚƖeĘӞü',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӋЌƚ˓ċɖˈːτɩʎóӴʬĆpѣ¦ŲϾӾ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040227.099762:+0000',
                                                                            '20210309:040227.123849:+0000',
                                                                            '20210309:040227.149093:+0000',
                                                                            '20210309:040227.176635:+0000',
                                                                            '20210309:040227.202643:+0000',
                                                                            '20210309:040227.226101:+0000',
                                                                            '20210309:040227.248807:+0000',
                                                                            '20210309:040227.269824:+0000',
                                                                            '20210309:040227.293000:+0000',
                                                                            '20210309:040227.315352:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ìɶƔʬҴҹ-ÄѻԁӂƉӡ˼ɔӓɉ',
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
                                        'name': '*вāѹÙԏʌ{ÅΙюԕљѬʩʛɪ˛ȊϭŻҧLлOĸ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:040227.750064:+0000',
                                                    },
                                    },
                            {
                                        'name': 'хҖ\x89βѠÊÂȬʻ\x8bÊˣǪϕʚϮɕԡϸȁԙǗǿȬДǛȝƪӑ½',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:040227.833298:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҌǸσäѠɹ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': '$ʂe',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŔôÁӠ9ʚΫʅƌ\x82Ϧϸ¿ΨӮȮȗȸѫɗ˝ўĩЕʏŠѿƔΘ\x91',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʮȪ˃9ʏςΤī±vʿͳӃģΕǥȇӫCǳͿӹǨ*çǅ(ёâ҄',
                    'message': 'а˛ѺʧӬɵο\x82\x98ɜƲэɄӀ(ÔƝѠ\\żϑЏĪΙÓϊ°æʢј',
                    'arguments': [
                            {
                                        'name': 'ӨǬ\u0381ȑǻǂԭҀңʕ¦\x80КİČʞϝϞѳѡƅĚ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3836594637151146012,
                                                    },
                                    },
                            {
                                        'name': 'ў+гłϩЇǕϢʼΑȡϗƠј\\ƥΡϔ§ǂИжŏʙϣŧȟФūқ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʂÅͳэī¸ӂ\u0383ԓƫјA{ʻРĬȍЗȳðǙ\x83ӆǜŕҚ¥ҺĬє',
                                                    },
                                    },
                            {
                                        'name': 'ЦʸӓҊѰ;ɦT',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϋѷЋ˽ÕănԁʞƭѫƍѩɞċάϜʦɀĽϕаȭĀÅʞɶ˸Ҋҫ',
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
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɜ±ΓηρʴÛőƱƁϟˁȩЃ˕ȽƎĄƈҴÔҭЀζgmǗ>Ӹρ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ûуƪǩ¹Λбңʄu',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 713058.2309469155,
                                                    },
                                    },
                            {
                                        'name': 'ȝĒԓı¡κ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:040229.460494:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɜɜόƊ£œĉӏͿ˕ȮŖǘԏϞПӔɪԛƎóɁ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2382879480211431797,
                                                                            -4078182248396980154,
                                                                            -6366756254912998450,
                                                                            8467913973406232807,
                                                                            -8060231087279174544,
                                                                            -6517154220657378319,
                                                                            7431604059940446819,
                                                                            4553088020396650068,
                                                                            -854801411562066179,
                                                                            6412485629801438231,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'fȊǼ¬_ԏŇͿſԅƘѤК[ǷԬςԮ\xadϭҸ҇ʿ˅°ʍ˯Ⱥ4ϴ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 757349.1552934184,
                                                    },
                                    },
                            {
                                        'name': 'ϜєɀˋZϚʮЖž,ҎϞщ˝\x8aяŀɶƢϏǔƈ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 554704.1114345497,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϭЅǜà£ˠ¡ΌԎ˥ŚʉЦѓɲ\x8bǽÉ.°¿ҟ²ѠŷKѽǌԆ]',
                    'message': 'Чi\x95˼ɽř\u038bÿȂӂɗЍćȞȦҋǑӍĜÈɐӀҢƎãƌӨZÔſ',
                    'arguments': [
                            {
                                        'name': 'ԢˏӪϬŴ҉ǖңƸ"ŁëǆA\u0381\x99˦ǞОĤǕČ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '\x8ađ¬ĩɥ·ӜƊǋƴʄɞϥѤ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8297589858132348396,
                                                                            7767915276524114032,
                                                                            7194095560270627800,
                                                                            -8851321076087631330,
                                                                            -2437303430112862762,
                                                                            479008007852314970,
                                                                            1340904901780335407,
                                                                            4834406556205188522,
                                                                            -5112249368567205843,
                                                                            -940811072882251873,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'эP%ΧǞľŘƔɺӳцɢϖǩUŒѐԣѦԊƘозɗēϟòcДҊ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            283028084949393055,
                                                                            -3718396052448122329,
                                                                            -7105252323236486916,
                                                                            -6909572733286276818,
                                                                            6166685764060048445,
                                                                            8012350279698142715,
                                                                            -6637874465389226241,
                                                                            -2198145216803207683,
                                                                            6083108365225815509,
                                                                            -6261614120208197319,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȑҿҙǒŻ˯Ɲ®ʂӪ×ĬĿЮԒİșΖҲ\x92ȯ˗ɀƁ˟σΉӾɟЪ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6519023654919972120,
                                                    },
                                    },
                            {
                                        'name': '\x9d\u0381ƺĽ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 165204.15921717085,
                                                    },
                                    },
                            {
                                        'name': 'ΗҫÆjΉŵŉͽѴ)ư˓˦ҴͶìɨςɤϔ\x9dəʙ˺˪ѐѱȽдǺ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '9ǴˏѦʹɋЃɺĒԜà*έŲҷъѯ҆Ҙɍèӱ-ϟȴ°Эԏƌƻ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': ';¹k˽љɽҞ\u0379АÞŘ·¾ҲҤ;ϞȖ˓żàţŃƑΧЍʶ*Ɉƌ',
                                                    },
                                    },
                            {
                                        'name': 'ͳǌĻȶ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            121665.94172951602,
                                                                            498958.9203038259,
                                                                            61165.95765491517,
                                                                            117555.64784578673,
                                                                            778331.0911592382,
                                                                            665688.5429273753,
                                                                            501126.94212845666,
                                                                            819639.057053757,
                                                                            120157.02119304496,
                                                                            530375.364923499,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ľϧĻДѦѭӌʇЭ\xadʊΞƀΎϰѫ)ԬιϗʦɰӞǎʶɏ>Ē.ԟ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȠӮ>Ȼ5ʺЃăóΡƞ\u0380ΊŴȬɫўЩĸ)ϭ0Pǂó\u0380¨˝ȵѽ',
                                                                            '¬ӏкɪжҭȠūÉӣӐɚć|\x96ĬϘǐɞˏƵƣψȝТɋϏҴдŰ',
                                                                            'ѝʌԙćƀҚԐȸʃɴ@ǆƤԕ£Ӊϼˮμü҈ȡӻƓǇȠчoPĦ',
                                                                            'ԧȀĥØƫÉЎʸӉĨǪкȻѶʍώҊQƺӜʉƹȬ\u0379ǮΔшBЇ˹',
                                                                            'ǦɭʔѻсԗƛȐXɏ',
                                                                            '˫ ʓӿӠɝԃɛǯöǑϒPԐʽтǗĽΪҶӔĄŤƚͻʵӀʶļϋ',
                                                                            'ɞǑʼԛʬȓΨԋ˥ȬЀԪbќ<ΡϏÄɝхBɁđȹфýԞԖĵӭ',
                                                                            'ǥ]7ˎЫϑԝÅ˶ӜŌɤʨűÌ¼ȆŋġØʭсø˥Υ½źŽ˖Ǥ',
                                                                            'ōœШƇű˰ϭ\u0379ϽƚϦˮƃF˗ӬРʀCԬÿуϩŻlІĖШƌ&',
                                                                            'ʄŅûѼЙϭϲʜɳ\x98ǡŭʍԢƩƗñёú\u038bγǃνŤɷӡοͰŞԛ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɛќz(ȵ҄',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:040231.657129:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ĒĳƚȳkΪҲǤɎϑ\x8aҥ8\u0380ԔÇNѢԊ«ɊđķǳʘъϿ©Mȱ',
                    'message': 'ӟĖӖӹӪÕτєǡũĮʱ\x93ʱӠΥÂ҆ȠHАƕƀ˴ŖҐ˙¤Ūӗ',
                    'arguments': [
                            {
                                        'name': '¸χѿÖԨўɡԛ«И˪',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            96488.96408035717,
                                                                            454155.78585073317,
                                                                            800506.0677523445,
                                                                            506930.3381355074,
                                                                            320401.4232933398,
                                                                            580082.0725108833,
                                                                            702620.6212736779,
                                                                            490873.252079459,
                                                                            886621.9084482625,
                                                                            707331.3169689616,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '0țχƃɊѼˊOпYѨҙȳΧƯƹѵѾɁ˷˞\x97ǂǌҟѼνҹѝУ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6747763333248632845,
                                                                            -4872021957576798471,
                                                                            3133600838722716914,
                                                                            -8515858785843393380,
                                                                            8065346217331354656,
                                                                            -3581460094493746628,
                                                                            7422844196827138750,
                                                                            3879802539359766372,
                                                                            8430334413329647039,
                                                                            -2392060733914307941,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'DԡрðҰɱӘXќ¤Ȫ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -16361.789610405423,
                                                                            578724.6291331263,
                                                                            460720.0746094736,
                                                                            263100.03283117304,
                                                                            999098.7072703654,
                                                                            351996.70933031576,
                                                                            198651.96097652428,
                                                                            561414.6320230445,
                                                                            840411.3097434832,
                                                                            842012.6069791069,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "Ӻ·ϑȐҥϐ'ӡʸͲüßԥȯƖɡѣͳtΝѲϳǮϱԆӫ˲ǘЊõ",
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            165918.60494631616,
                                                                            412773.78458578134,
                                                                            650883.9871093307,
                                                                            726894.0114405657,
                                                                            834118.4078529872,
                                                                            981413.720350591,
                                                                            773194.6543956473,
                                                                            856950.1307742444,
                                                                            720548.3916170012,
                                                                            915898.2739462334,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˾ΓǗѣƗґǝ϶ϓʥ\xa0ӰʥԁӃöĝƵӛɴ\x80ΦŷǙ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': 'Ӵƃȸ\x874ȜϘѠѨăҒ{ҁØӇŀԡųҹ\xadżͺŤϾȔˠǙĈɾğ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:040233.319473:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȱʸeȐȏ˞ƊőǬǣȜʹŁʹϥ҉ԃ¿²ԑȽ"ͳ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 274257.48623034015,
                                                    },
                                    },
                            {
                                        'name': 'ͽÉǝñѾȚΥĸ§ӂʴȀԔɩƾβъԂMĖϏԨŨ·ƺ˟ԧЌɨê',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '|є\x82цˏԤņéU±Ӈǅюə¯ȓ9ǆԣȓ҇xҬеңҔ˽ϫҰ˭',
                                                    },
                                    },
                            {
                                        'name': 'ҝşԒˁĜǰĒɫɂӓϪĝɿƐʬϜƞцӨˎÅɉҏ˲ǞǎɅɣǿʠ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040233.578511:+0000',
                                                                            '20210309:040233.598876:+0000',
                                                                            '20210309:040233.618458:+0000',
                                                                            '20210309:040233.639784:+0000',
                                                                            '20210309:040233.659300:+0000',
                                                                            '20210309:040233.679025:+0000',
                                                                            '20210309:040233.702744:+0000',
                                                                            '20210309:040233.728409:+0000',
                                                                            '20210309:040233.755207:+0000',
                                                                            '20210309:040233.778081:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɎƁɗϙă',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȦÅфǁѷQʷcĦɤ΄ƆʕЮ\x82ɥËǮʖұҗžʯȇЫ˳ŚĉсŃ',
                    'message': 'ςЖaʢӜԮԮИυ$ь˒ˎɍԤІϥĆөȉí»ŤѵdɉѰҎʾȲ',
                    'arguments': [
                            {
                                        'name': 'ΰ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040234.066141:+0000',
                                                                            '20210309:040234.085737:+0000',
                                                                            '20210309:040234.107246:+0000',
                                                                            '20210309:040234.126480:+0000',
                                                                            '20210309:040234.144779:+0000',
                                                                            '20210309:040234.163729:+0000',
                                                                            '20210309:040234.184425:+0000',
                                                                            '20210309:040234.205271:+0000',
                                                                            '20210309:040234.226522:+0000',
                                                                            '20210309:040234.246281:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ůәѫʓ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʯÅɌ϶ˋѽғмѝqȘѴǵ˧ϣрÿśҐʺ\x98ɪӬƾÒϩɌȦZǾ',
                                                                            '\u0382ǸЙћȭʁΕ¿γǨKӉ˱Ǵӧʓȿ˻ԥѻι˕Ͻ4ėɫX˱Ѡӟ',
                                                                            'άϚιҸиҞŤȌъƞˇŗȇǶ\u0379ĴƳԇ˨\x84ϔę¸ɬƸ˱ђȤεӳ',
                                                                            '҈ƁƏʻ\x97Ȳӫңɦώƀӕη=ŭɍȠwȺԄӯjЇӸΰ҉ӟєԣҥ',
                                                                            'Ǭʧ«ǶП\u0383ӃǄSҋԟͰΌȞcэЕĺѫıǥ˒ȷϋŨŅċϹμɕ',
                                                                            'ЄИɇ\x88ҬʶӾҘúƥˑΨǁúӷǯǕѴ\u0380˖ΞƜȺԐϵїŭұϰ\x93',
                                                                            'ЫȁхЯ҂ͰγԕѴſǩǱЧлËˁĀΒƒȚȴŧ҆рŇүΠĕĿΓ',
                                                                            '\x8bˡ\x95ԙʤ҂ˁƿ\x86ʁƵάìʘÖнˠVɮѮП®Πӊ;әϥƪВԢ',
                                                                            'ќӃǇƲǢȐҠǿƬşӘЭÂҭǸ·ϥξ\x80\x84ĪŒцȼϹјȅРȍx',
                                                                            'МʪʸЉυ\\ЧģВδ®ɳȘƝʭԡĘԍŔƓЇРǨǢү-ІΓ,ѷ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ľϜԊĨХȖĀЦ¨\x95',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040234.698064:+0000',
                                                                            '20210309:040234.718788:+0000',
                                                                            '20210309:040234.736206:+0000',
                                                                            '20210309:040234.755503:+0000',
                                                                            '20210309:040234.775565:+0000',
                                                                            '20210309:040234.794847:+0000',
                                                                            '20210309:040234.816195:+0000',
                                                                            '20210309:040234.838442:+0000',
                                                                            '20210309:040234.861949:+0000',
                                                                            '20210309:040234.884993:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǰųĳӜɤ8ϡʹѹЕʠӦѪƍşˢǦ\x9d˼Ԏ˭˭\x90әDԍơίƿҽ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6974164627953796422,
                                                                            522269897717817779,
                                                                            4777127182758450015,
                                                                            5083519696062423548,
                                                                            5455511190960723139,
                                                                            2121740477339691716,
                                                                            -5023724039779963581,
                                                                            3176877864204350177,
                                                                            -9077487306511179266,
                                                                            -1091665468981724245,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9dʠ\\эĹԝԫA`ŋŉͶ?ΟϳȬΗҘŉ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɕϔҽŴҝƫϏ\u0379\x82Ԣѥ\xa0ȖφϷ\x83űɂŠȳǈʾѾĔбρ/Ӌǿȧ',
                                                    },
                                    },
                            {
                                        'name': 'ϙςҎ˔ӆОlĴǉЇʢɦѡBЕ-ȝʵɉ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ǖ[ΎϒiϛƪԑӺԨʎϮ˶Ш\x94Ĕ˕ȰĴ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '^yԔϖqÒѲûǉċƦǻėfſʠúÁʭɱɟʐŰҜ}ƒÎŐԛˣ',
                                                                            'ЁԞсǷļÊϭ¦ÖԪʞŪӜ҈ʴʱҋϱʖԃƜѠѪɱɮΞѹʊBŷ',
                                                                            'éȞʚͺˡЖӓΎ\u0378ǢōƑҐԭбɗ$ɉϴR˺ͶЏ҃õf\u0380µðZ',
                                                                            'LɟőʂͽTЌŠƐПȌНǢɘĂđsɯџțʈȞĤƽɮӄƥыƘÁ',
                                                                            'ɽ҄ÒʟʱǽɛGûeŷ¿Ĉ\x88ʄʴÎȦǣ҇čΫ҃јȲņ҇\x91Ĩk',
                                                                            'ӥʞƬˮŝ|ϫŝŉǈʷҚɄǳ§ɪ\x95WˈԈɨЋgԠǓˋζɛπĜ',
                                                                            'ÓίŖƲѥĜc˳ήàŤşԣñưÀǴӐ\x82ϵĈpҐӱçΫʼЗɈƳ',
                                                                            'ɇϰ¢ДΩӼƱπĊûƓϺßʓîϠǿϬμŽѯ˽BҏƑ˸ªТȏK',
                                                                            'ÿǞ(ҳrɌǄ˔îǀď˃Ŕӈɪѭ\u0379˃Eȑ_ȐϡɝŞŦƾϞ\x84Ě',
                                                                            'ȮȉΙ˛҃ʡЫυЧpŞŦѣϵοƹêŬȮÅFʥȜвѣӟǊӚʿЩ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˢԏƾşÏơĠ·ˍҟӲϴQͳʵљϳǑ\x91өѣǯƦĮӝӻɴʉĕΏ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ĩҀҋŊҝAÝeȗϨωIʹВʀѧȹˬ*ѽ϶ҤϿӌǰҢҢǤ0ә',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 800778.3038236605,
                                                    },
                                    },
                            {
                                        'name': 'ĔͺǈѱϦű¿ˮ\\ѦΎъɺĠǄ*ԝɱǖ_ӓԭ%Ҁɼêԑ˶ǡл',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:040235.914842:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˽єшϬʳǈӉäӐ\x83ɩԩơӒǰЉϞÚĉǌΈ£ǵʥ!ƼϒϖќԘ',
                    'message': 'Ӡ˯ҴЕӊÂǀԑȥϏřēϭ˝$ӞčČ҆ϯ_ɦϥơґóϺ҈ʽ\xa0',
                    'arguments': [
                            {
                                        'name': 'ũѓǼ\x88ύ×ζӣˋ\u0382ϝE×',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 880907.0533293905,
                                                    },
                                    },
                            {
                                        'name': '´\x95ЙԭɌķƈƄАʟƁźн\x94ӗňεԆЁLʏɊɵ˰ѕǻÀƸ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 851812.6390322273,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƅԖэҌǨ˛ӑˉ7ǘɅʵˎԐźӑӵγ,ԎʸʖFˌįдƼѸȚŵ',
                    'message': 'ǘųԚ˱ðHŰȣʭӵɷũǕϚǯȌҖōҔа҄Ɨ\x86ɬÓÞĐѷ4Ç',
                    'arguments': [
                            {
                                        'name': 'άϿɳǚΊлΰɃŕū¦èɍ¨Ÿөɍƈɮκ˺¯ȉɫöȰɿľíҠ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 993014.4393570472,
                                                    },
                                    },
                            {
                                        'name': 'ʎϋΑӳΒKBЉ˪ЁŒGϙǫȒš˸ЩʌĒBеwЃԄϧƽбÖǚ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3613089431281566097,
                                                                            -2347402653568830967,
                                                                            -3415736415164416253,
                                                                            2821516028998942766,
                                                                            566093513348509836,
                                                                            6417007821919362951,
                                                                            8332173352797451162,
                                                                            -2266020625215692896,
                                                                            837431368930966004,
                                                                            552185297715934624,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԟȧǮңʕ\x82hǑѾƤӛнȞŬȇŕɥ¤ӚąƕɮĥɌΎϨ:Ϻϵĩ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            909435.4410010198,
                                                                            612356.8667448541,
                                                                            268819.91156277125,
                                                                            427914.0095678851,
                                                                            437382.4381683073,
                                                                            653817.6480751092,
                                                                            761001.833323627,
                                                                            838870.0121377298,
                                                                            59634.30341692167,
                                                                            533863.7662263672,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƉūǘǦԝӚɤ¶jŗ^ԚĜ˽Ж\x96\xa0ȲÚSʠʕǟ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            987583.119520104,
                                                                            958156.8251774756,
                                                                            903609.7724781511,
                                                                            32360.313253365282,
                                                                            990332.8034861393,
                                                                            746508.4761362209,
                                                                            91493.07811752165,
                                                                            396554.2109237911,
                                                                            876147.247193478,
                                                                            -35861.7469308486,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˹HϏЈώўAʁўɭ¿ЯƸ"ıȢɰЖѼȂͺƚΆšŝƻŁ\x85Ѥȉ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:040237.311184:+0000',
                                                                            '20210309:040237.331337:+0000',
                                                                            '20210309:040237.359168:+0000',
                                                                            '20210309:040237.386580:+0000',
                                                                            '20210309:040237.413558:+0000',
                                                                            '20210309:040237.437520:+0000',
                                                                            '20210309:040237.460342:+0000',
                                                                            '20210309:040237.481526:+0000',
                                                                            '20210309:040237.505528:+0000',
                                                                            '20210309:040237.526447:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԑwʰɓϞӼ\x93Ԣɢӟԗλҹ\x94ҧΙƍϠã˂ûΥİϧ¥ɕԡѢ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ʺ˨мǓrýĕʳǪǘҟƝ8ИÝΨ\x9c',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9198291455713009881,
                                                    },
                                    },
                            {
                                        'name': 'aǩɛӹ«І\x96ÓëОǓĻǆ˳ϋ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            842423.3462814123,
                                                                            572165.7654788855,
                                                                            929898.4711901691,
                                                                            796200.2272567195,
                                                                            529026.9297279747,
                                                                            238774.4517648401,
                                                                            735127.8673128271,
                                                                            286587.14865272853,
                                                                            41172.01721070518,
                                                                            -53528.513644002654,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԑƢ˺ǪӆοǙϑȆĲȶȐ˕ӆɒʛȽ0ϰ\x98ʦϢɗźԐηǫƯƣŒ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ԂˆʔϻѬίt',
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

            'identifier': 'ҳөʉƮǔ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'Ԡh',
                    'message': '\x91',
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
                'identifier': 'ͺōBɎÈ*ĬÇƭӏǬŉǚԌ\x87ũҚőΪó\u03a2ǕυÎ˥Ƶʾѧώӿ',
                'categories': [
                    'os',
                    'access-restriction',
                    'access-restriction',
                    'network',
                    'invalid-user-action',
                    'configuration',
                    'access-restriction',
                    'os',
                    'configuration',
                    'configuration',
                ],
                'source': '¸Ĕι҇ˀČћǄʵ@ЂǶ7˚ȳҶԥϭȶѪЇũӥ\x9aӤ¡ԧӦˈѿ',
                'messages': [
                    {
                            'catalog': 'ϠƱđőƍϑϣźСƟʙȘ\u0382ŖëТɫӒɻ\x83μпōyѵΣˤƭŮ˖',
                            'message': 'ǟƇѢΉdαɒȪɩ¾ѻ^°Ҙ!ȲΕȺˍɋɄы˴ʛoɁӝċϫα',
                            'arguments': [
                                        {
                                                        'name': 'ʡΥpΊɣOŔɎˤԡӵĄßǸiƈϔ΄ζԈ˘\x83',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '7ν#ƸяǾĹĘĶЬƛʳŚ¼ѭΒ\x9dĈŮςӸϔͼǲУӁˏӡЋɨ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÕǪњƫІЌͳzˀԫҌϷɞ\x82ϊŌŃ\x94ɅƕNЬƍДƈϸԅ¨Ͳ\x9c',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӏгίԘŤƼƍťєɦ$ǩÂȍēШ\x89\x85҇Ĺƀ\x88ԂŬ\x91ų&љǉͻ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʰĺȁшͶϧӁˡĜʐΏ\x9e˯ӬƦʆªʨƦӑҍģɚFӉʜğŚϙů',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԏ˰şʆλа҂Ӭ˕ơǍúƪ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǝƒųÚΗȥɌÁύԉđÜȅЋɴ\x84ˬϜӧɸΔɱ\x9eɪñƞԄYхӻ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ИɇDˑӨ¤ϓłԍµбˑŜƌȡ^ĊĴƗ\x99ɉύóķǀǼŢœ\x85Ȅ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŢЗČҚЖƠˋĭ÷µɄ7Ǹß8GΠчӣŗҼÏŎĸҧDƥѕԘɑ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u038bϡƄˆҿȇɔЪ\x95µх˥ϾӸà¹ѽԈPЂ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʔŌХʭʾsí\x9eԈǵȥ\u0382ʸŎŞ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʫKʴӅ×ģ;ǮԭǀϠΜљϢχ¬ΐθБȗ\\âөѩѳϛЇZĵ',
                            'message': 'ԕʪǈlʠ©ʦĔǁ°÷ʬљʻӚmф\u0382z˱ˣȬΚȕχłĠОϙɱ',
                            'arguments': [
                                        {
                                                        'name': 'ơǝѶͻɮĻѪҜĿǧӱӷʮ]ͺӼtɆȾʛɬæȦͲǘҀҙҷƼн',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7788493329380139156,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԓ³r\u0381хǯ˅ІʆMė(Ϯһ˴϶ėҳұkˮgĒн҃Ғтцσŋ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3095112649765655054,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԫõǠѠ˓\x90ԛϧфκɋ%˖ӜɩȜ\x8aGǃƖā\x9dҁÜŁɼ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŕºžӂʓ϶ʒĂđȦîϾҥҲŔѓӠҪz˝5:ęϯũɧϤԘŉѵ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɳĚ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԝť',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'мǻҟѳѻӥ\x9d˾ɄĹЎūɑąԕĜϫϻ¼ÂϱȜƋŽŎѿØǩ҆ǰ',
                                                                        },
                                                    },
                                        {
                                                        'name': '˓ԫӘњîҐԂʣ\x9fʝ҅Ƞ΄ƝϤԎҗƳϱˋʥ@ʢτɈŶїǕҢ½',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 512145574909835695,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʌŌŗмȓȜzǾ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5712034943972047232,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÖƼŷǚΒЩϏȼ\x93ǗәȎЦΫ¬зʇ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'тʢǼɛƍÿΘÂϏ=ʫĄґҢҵҀȟǰ\u0381ˤǄѶçΜϨŶłʇȻя',
                                                                        },
                                                    },
                                        {
                                                        'name': '\u03a2ǿƢκďýѮʎʠŶŉģ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӒǲJӄҝȮύɦА\u0379øƅѤõϓÛӖɨҢúдʜά\x8bԫϯŌȗѦ˕',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ÊԋʓǖϽťш˩˸ҸŞţÚҲԧ˳ˊʒϡľǖƦϰĻэҀԦǎrт',
                            'message': 'ҟҰɁɬǔκȵӊşð\x9dŔŀʏƟ˚ŝǜR˷Ԅ˧ȺʚˈΌΞǫʹί',
                            'arguments': [
                                        {
                                                        'name': 'ҿ\x86ÔɀҚη',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040215.185062:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӇӇBłŷлŝw˹ңԟþӂĳҀ»¬ӾĳāТǆҹϦͶӅƟǥ\x84Ѕ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 702660.2638958797,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӲìҷĕǑƣΆfɉΎŤŇЃҎƶƮҧƔʂƃ\u0381.«˩\x85϶ɤ˜Ԁ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ħĿι\x9cƲǃκ˝ʤ˚ǷɧѠѹ²',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŭ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƫЅƐ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Р˖ӕѥÙ҆ğԤșөӢǜ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʚѕǃˆ˘ƻ˕ĺ\x91˔шΞǅ¨ǟΧɨΡȶѸɆȬ§şɯʴΪɿˮԣ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʞĭЛġɡ¿ѺиùÜΏԞɒ҂ʄƔɁΦǙҷ"půıӵŚͻÎ˂ϲ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϯʆǑ\x9cȀ-ƟεoɭʀӲӬ~vѰȦЗǜԢʒSĆԢˀȅȗǅҖ9',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040215.979049:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʤԆ϶ËôXu\\Ͱaҕɽ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 661865.2155661014,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '°òРв¿CõĉŊ6Ӽѓ˒ϬʧÚҷCһƾͱǲЪˊЖЍɫ÷ϠɅ',
                            'message': 'ӜƊūϱƵөɕќԂКéЛЬΈǎǹ¤ŖŅɻ΄ԧјϢѼӎнˬ\x84ä',
                            'arguments': [
                                        {
                                                        'name': 'ѦȂϤЉüòǖҤԧǬȚϵ¹ˬѭүҫьЈпłɶ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '˪Ԉԏ¿ҍԠƁĭĸǊÚŬ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040216.333338:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɅЊԪ˄6ɵԮƮӱɍӼɌΤďǅĻĩÏJˍď˃ΞuǹʡԘǼȉҀ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '&ŭЯϕѲтАeĔźKϮнύɎȯɖƃŤȼԢƙÿ\x8fœӻǓΔπT',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϔȫŹč[ˌɟ¤дŨѮγľϑΧʮ\x96ĐϊǲơѹíԄ@ƔəāΩɄ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ςПǛԏ˦ÆԖ\x84%ԔʠèǓӠРƖºΩӗȤһͰͱ͵ƬǋȆƚȢӔ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 323209.61699684523,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǬąϸЉȀωÈ˾ғũӲ1ƫɪ\x96ӤώʪĀíɺͱҒïȉŠͶɱɣc',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6172580087189609080,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ыˏк',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȬɯȮíώԄËǒɳIϵҟʬŏ$ʢŻѩЄгıȮːıōѣ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƽŠΔ˅ͷ£ȳȳ-òԜîӍuˊ˞ȭCð˴Ѭ½ЭͺƜ¼³˟ɃϺ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040217.007477:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x80ŢȃʴȢɏƖĠɠȍɬȇĔзҞƘҸđƤ_\x94ěΣԚϠЇµҝwѨ',
                            'message': 'ƤɀБӏwĎ˵ŨňӺ\x87ƟқĹͿ΄ʽǡ?\x94ͱƈđκҪлƢɹũ϶',
                            'arguments': [
                                        {
                                                        'name': 'ɔʟԕͳŢūћϦ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040217.157672:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǥŀЊϏӒ:ӑì',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -54544.26933677443,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӪÛԬӰΠҨƼϿ\x92ȕАʿǘ\\ÚƠьσƑ!\u038dΔƭ-¸ƑųѢɗԌ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŭӨϡ(еϻЀѝɵcǕɻλŀɮϔ÷ǉͱǸōӎҁѾξТϹÚΆҔ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "\x8aӨѓƛŖЍǮʘӢĻÁ'ÑνӿȌƅС©ҾʋŗϞůԎƞәҾĕъ",
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŚÆǳ ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΗÙͳTʝȈϻȘƙΨ:ïxȄЁëŞ˻ǰōѨɚΒȓɾʹΪҚɟȖ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ѓ\x9c°ŴԜǮϽФƾǢʗqȋѓӕņЧϰ˜ЪyЮƾ×ӧˬчĪȭô',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˤľȁˡĪĮ\x94Ю˴ҋАɌςJ!ƖѫÎʖÐĊϫӅƻҔŢõȦԦ@',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӛİ˝һˤ÷γ˧ѓ˻ēϮ҃ȕ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040217.795809:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͻVй',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1445392089124505141,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Їқ',
                            'message': 'ԔҊ\x9a×_ÉàƆͻʩѫ\x8aͿʽ˕ǆɊńҎʵ˗mϣшύĺԄͳĀ˙',
                            'arguments': [
                                        {
                                                        'name': 'Ϫ[Ϩ˷åu˰\x84ȖˇŮsnǗžǻ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040218.039420:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѦŻ҉ʅѪīĩŚάȤĿȀ(#9ԅėİƭ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĔˆVɾәĒсȄԟuӍӷХʂԧЅ$Ȗϖʈ˜ȴøЅÑσ ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040218.220135:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȲĠôœļăʢѡʼʲԈωǸĊȀȤϊΰЭ_˧ƥéӕЭ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'š;ԂǴęξ#ӡɰӛŽʵĥ\u038b˭ƕЇϚʝl¬íģԜɍ\u0379ųФƬƴ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'şѰаЊΌƕ&Ȭџ\xadˠńŎèČεӠūΣԝEВÛ"\xadĪϒďJ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ПҠĽ˯їχҘȳ˧Їľԫ\x89ʝ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 126806.51729612632,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ηˁ1ʭХ҉жю=ȭʕĀӮįȴɺęԥũǸǯɾϻTˆΗйԘжŧ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040218.701602:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĊĤԌ`ҢКҸ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 799312.2195831665,
                                                                        },
                                                    },
                                        {
                                                        'name': 'üÕʚ±˙·ҰʟФӖƉӚWǁʨɦѹԫûɈɕ#Ŕѩʢǹ\x94bʸ%',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ņ˃ρΝž£л¼ƭѩÊԖƧų˥ɗƆӬΰɏˁɏǍȓҌԗˡҺӅʝ',
                            'message': 'ɃóÄ§ñYőЏƢыʜƌÌϽǔЦҳćȜÆȎǮ\x9fҩιƢÓ\\ã˭',
                            'arguments': [
                                        {
                                                        'name': 'Ľɤ˝ҜËʤѫХӦƆċŜԈ\xa0ζťȄğńԇҍvԝŹƒ\u0378ĖΦϝΏ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Įҹ\x82Ȋ×',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '¨ҷÇ¾ʴ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϪɾԐˬ~ҳηр˹ƪǨǦΎc\x96\x8eʤ˜˧ŞĀʀĄǛ×ƦʎȁǠԞ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ő«œɿѶ\x9bȎɨ϶¶:ăɆ%ѝțýԛ˂ΓԑӳǻðӓԥԨǅȹō',
                                                                        },
                                                    },
                                        {
                                                        'name': 'L¾ˬʋţ˄ќѐųѳƽô˵χϗʹѝã\x83ƄԘĄӓԥ+«.ԩ\x9d\u0382',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "ʣÝДд\x8cΉԤ˨ϡϢǦȴ'еǧΣÑ#ӇԧȏˈAюԇĚԜҌ¼ʭ",
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ф',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʔБɒj,ʬȨъΕμ\u03a2ͲΡȹʩ\x89ŽӦұµǛ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 564492.8003700369,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǯ°ɶ˃Ì˕ƭќʽҶŇгβ¡|ЀˉIгњПΦͼҶĮΉͿʻ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4366291960311733619,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͷRÎΉԮфѪˊőЌαPŽƶѸϳeӒѯŭ\x9fǨOʹͶ˳ɧιӉȴ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ęǘ¶ȨӰ\x93ǐѯ¢ɘŔ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'υӪӡΘqΗ\x9fЗΙ)сѴʹ;Ĉ¶Д1ˉϷӯ˦»ɼùӫ~Ð҆\x8d',
                            'message': 'ЧŦϪ˕¯χӪюÊĄőȬLњɱϿоӊԔЦŅƔƎƐLҧȀȬǐԗ',
                            'arguments': [
                                        {
                                                        'name': '˜Ōŏ\u0378ɁŘŇʣ϶ƵӔĠ˝èЏǤŅøДľ°%\x81ΎøЬ҇ζ4ѫ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĴӀšǭ˱ӚɎ˛φˈîоũƓʲҸ\x93җпnɊǏΝˬ˹ʣʎȍы',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѱ4˅һ˹˾dˌӨÃҿԖīǫɜӎɽӰȆΤœКēşǔ§ԂÏĲ\x80',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040220.078893:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'YƛʯѨǰϳĂǜ÷ϓ[Ɩӿċ˻ҚЕүҊπâёŞŎ˅ŶҤџѱϬ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'LʸŘ\x94Ɗ)ϟɖeіǛ§ɱɳǭƑϱыҖƭƻϿŰ7φ4ѳΔȈх',
                                                                        },
                                                    },
                                        {
                                                        'name': ':ϛΛӿ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 198959.08118572197,
                                                                        },
                                                    },
                                        {
                                                        'name': '˺¯γӍ˥МΆҦѳŵȲȠҩɎðǶʜшɁɩЃʇηɘǎ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѹЯќԛÕΡƸđÃǏǩ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԍŨǸөϣŋŃŤӀǳǴēRβӕȬÀȠʅʮǿΩ5ƫεĻʺǋΛЧ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'эpғЭɍφϭʟ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԅņŬƇ˃ƮЂЧύÉȱĄӠ\x8bϤεҬԤϚ˙Ű/ԁӰŬơǮβhJ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҠӎÒëѬшȢɻϻρЯmɿȁΐВ˷Ƭ\x87\x9cqΛƉɝţʹϿΘ͵ѵ',
                            'message': 'ΒʅçʓӔʟϬλҵǘМÅżĎĆǙƉΛϐÙǏѹʴϡĄ\x9fӦѲÑʪ',
                            'arguments': [
                                        {
                                                        'name': 'E\u0378ʮǦфϪӗSʮǵл1ҺlÌҚͰԄҕȨθêбIͳÇʑÏɪƚ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x80p\x9fþ÷зРɹƺ·Ӥ>ǉѴaΚȾσǛЯdƁȽ3ȱo˅Ŝӡď',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҁǭǂĩсŅW¶йȼFϰʒќʱʅŘӨg\x98ʈµ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'вνcϭò˨ȣǒżˊƝλɇҲӇɲГJ˒їǝǈÜ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1738549414975932428,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͰѱΝɮʥιjӮΎÝ(3мūџȰ˱ɅųſͰεùƓ҈ӍʋōʆФ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŵΰϠпӷÆҦ\x85ԙǗƄ\x95»ôâǬƓϣњϸȴӬÍȇĉ>җÎÅɊ',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9agˈ×ƖɆΚǣԘ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '¨āӳΉÀȗĤƳГӔԬɍԐʊ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5118268776161346451,
                                                                        },
                                                    },
                                        {
                                                        'name': 'У,\x9f',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8540576891793305130,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԇԡϾΛĀʎӓҟɟ8ɰķˤƷðѡƄƑLʮęǓε϶ŹщÞħԩ\x9b',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 349808.8537072478,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԁʐǭЉȕӮ¬ϹkџÔƕď\u038bΘOѧӣʭǊьΙàϲǚɦžӤз',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǋыӦ΄ϩѸľũǚӹѶԩÌю£ŧԒТʞб:ˤǝöĉİƀ0ає',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ÚàуϝѝʉōӚʪȥÒƈρΞŧШ΄Ҹ˓Őǘ҉ӅÉϾȶ0ˢсX',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǇƩЍǭ˝ύϲǥϬTҪҴϣʿ£Χʔ˻Ȁʅɭɺӫ¿Ï˻ҞԨȳƽ',
                            'message': 'ӹÓ\u0382ǱĢͲɊҫӼǹ¾ķԗʂΣ"ƲéӀˍƎлȁкŪºҚˏǺӃ',
                            'arguments': [
                                        {
                                                        'name': 'ϢȻǝʞ6ΕЂéЯɪџʞӇęƋʋȚЍнϟа҄ȱҟȑӨ\x86±Ϥǝ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ο\x85˼wR\x9fэӹĸҏÞґӜɃѕĪȢџѢԊļÇ\x90ψаӧѸқѶ\x8f',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040221.790825:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѼʶȥҲ,ΔȄѱ½Ԗ˶ʵʗ˺ĞԋбȰțɐǰҞƳ˵˕óǾϧѪª',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'чӘȯΘω\x9aӎƢϜʙ;оȾĊűβǛЩ¸Ӆγέ&ч=ɂϪрӨю',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΰȅˈE~ĵϒ$УͺºǞέάÙ~ɱƁFɼªǣЋƸÚҤ8ϰȦǀ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ņƒʙɐόҭȎʊҫƴНΘ\u0380\x8eϥв',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĤʡƱԂɎƏРſӨҒЌťʀƻϯĔČɫԡ!˄ɶʇ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'зԘέŘ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7306809759472548365,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ùϑˏļџУѢǘҍ\u0379ҝʗíʫȭ˯Ř·ƊҒ$öόɝтŷŬЀ˷Ĝ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƻӷӄІʭϠíiȩǏбёθҧŚӤ<ƽҥƌɫĮˤѴ˔\x9bѬ\x88Ĳʇ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 993711.4888532641,
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
                'identifier': 'ƈοŗѻϘ',
                'categories': [
                    'os',
                ],
                'messages': [
                    {
                            'catalog': 'Ψѽ',
                            'message': 'Ȯ',
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
                'identifier': 'čɈ\x92МҳƬÃȆѩӋƩƝɷQӥĺιĐ¤ǒ`1ʡҙɵԍŴÏԗ]',
                'categories': [
                    'network',
                    'file',
                    'os',
                    'os',
                    'os',
                    'invalid-user-action',
                    'configuration',
                    'internal',
                    'network',
                    'configuration',
                ],
                'source': 'ŢʏӻȥӨǇɀûκѽázԤѥɫжϗϚίƹэʺ\x88щűҘǼԐɢϫ',
                'messages': [
                    {
                            'catalog': '˷ɋ&ªȋВӻƲϰƿѭϙ˰ԫΆʣGəԣӡʌǯȢ˂ΗΡͷάɛβ',
                            'message': 'ԂɒӾúĜήşϙҎΆчЗÏȝʼʮΖ\x9bǟɣɕҝғϘΠǣϺѿΆ\x85',
                            'arguments': [
                                        {
                                                        'name': ')ʏϐдFʭŤҋǏĈɾѤǶƨӖΎяȒƎ\u038dÜϥʁȕ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040238.728663:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʽԄѕĊsӣƧ϶ȮĤʪˌĿă',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɯoЍ¯ԣϥӔŸѥ\x84:\x8fχXЂˉǈɅŤϋįκӆԂϭÀǼӥĽ]',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'qЪϿкͻѳƲ\x84ɰɃůεșʍ˧ŝ+.ҥэϬÈȽähԮѡΔҀҶ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'πӇʥӎćΝǚ҇мŗ\x8dtɭҗƫĂʪϪʟг\x85ӰψţòԄ\x85Ûȝō',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɍҴӘΫѵçҘȑˑʳȹ=V˼ƗɿΧЎǊȧŮ9Ėˇ<XБʢФ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƓĲ˼ˮćԭɶʑŭ]ǰ`ūԥɯƮМрĆŚýȷØЬҢўШǩ\x87ɣ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'eŝāΐˇğƿAÀнäÉʏ\u0379ԘƪaHƬϓ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7089340034662966101,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƊƤǼʠÔȰʩcȞϏğ˝š',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 351616.5021641144,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƫԒӌӕ҉ʊϺ˹ɘĵʥ;ĕʓĿˠӑԣǂ˫\x86\x9cϿȡϝõϻЫ\x9f\x9b',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1781187170123089104,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԕΨĸ\x9eØɸӭӈϨѼɔȥΜѣ\x88ĞÂĨӊˍˆϩŘӱǞĴΩӴǨΔ',
                            'message': 'ƌҎĘƂɅИƵɓҔѻūʪʞōғ\x7fѬȄг˜śÞīƝɫʰØϝЧ~',
                            'arguments': [
                                        {
                                                        'name': 'ӼƇ¢ŸɕԝԟȪrѤŁëϷHªӺЃЅϷҧӂąʊĢǭûƇ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ļʆë',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 499156.8091861028,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǎˉȷҚǾʌЌΓęʡΑ\x94ɝıÁɞˡ(ƞŠүŤǎƣƳ˥Ãѿˍ\u0381',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĺĒҵ\x8b7ò҉wȋΜº0ÀаΒѐǑ˝ŷ*|ˏ^Ʃԅ0',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 267441.8825806879,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɋ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '΄FџɃƊӜ҉ɼќКӡӲͰѺΡňByϐĲ˷ļƒLԢЌσŌΘǗ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӅŉǏԤ÷Ǳȼ]ғ ĨƼԇҢΌ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 177935.86345967953,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǖÚß:ǾͼȶlƾƔǟԍŗϞ×èʏĶΰҹǾÁɭѿʝЁʤgνϓ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Z\x8bƕԈȶѤĲˁЫ\u0379ǿӷҢcμȆ΄Dǘ$ѭôɞӣÙЙ\x85ǍнҔ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǉ\x92ԝĥʋѹԣɾɅΡ˦ДSǔȨσäяȣŤ¬қ¡иŹ˅ɳʽèͰ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\\˾ĚÛцǹǍˠȽɺϐɾ4:ƜҙȕЌЖ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040240.409616:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '«Јʼ²ʟ¦Ï3˺ѴĭњϲΩӠÀ',
                            'message': 'ʅʒѷӏӅǳηΚCDÉʀӔ:ȅæ΄ŭǉώȬРћʥТʳԌǯĞȤ',
                            'arguments': [
                                    ],
                        },
                    {
                            'catalog': ']ŚǿҤȠ1ſźɬȏȭѻϽнΌ\xadҳDɮǕәríʇ\x8eвƑɝϋȋ',
                            'message': 'ǉѸŻˉĖŹ\u038bг˽Ϭ\x95\x96П¹μҖƋªԪŮИϓúȪǡїҒԊѶǜ',
                            'arguments': [
                                        {
                                                        'name': 'Ǳδ¤aƋǛƠƻʧОƁͷƞıΛ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ŵ<ɉåȇʍĕԁǛȺm"ˈAØŝɭ¼ώƀЕ_ѴŸʋǕҘɩMĮ',
                                                                        },
                                                    },
                                        {
                                                        'name': "˛йѕҔʙǢ±åӼǂZʺƴ'zїEˬԎɗʛѕŖǢȤϷ˂\x8dϟǱ",
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˻ϭƁȾ¸цœϼ˱ˢŗÕӹŸǃHҖƼ\u0380Ԃ,˻ʖȄҾťˡ%,Ɓ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǊҬѶƖŰɭƼǪˍǕǟҩǥǣƉͰǅŘ>\x9fΞϬҶэœ¢Ύ˒ɧ˱',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƕɴ5[WƠӚȜЯ"nѶÞţƥơŗϣˬ\x93ŨčáŽɞÁːӪѲȏ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȾβцȢȯю҃әҐƖ˦ŋȥҭΧǺŻơκε¡ϷŌǰдҺɵĥ҃ʇ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӎѻȮ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϙŽô4º˔ӈӱҳΒǪY˨ʋӅv!ųþȱк҈ɢτρȀԢΛŭӸ',
                                                                        },
                                                    },
                                        {
                                                        'name': '˖ӗΎȝυOëΏŚķ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2088258663454468859,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ı\x84éƼƿԙƃ\xa0ΨğшϯɃĘȴzȐRыαŒʸɬèêˍàȢɎѲ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ЂҘӠʂ!ʎхθ\x96ЎǭήɈ\x86ǕǨ˰ҸßҶƯʓɉ˰Ӧς\u0381˺Ɲɬ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǉгл',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 864201.1889082522,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ĄÖϖ\x81ǿЛѤϙdȤҨГ\x9bӱȳӿψʂ³ƂʕŽƷ˗Ćϣȳůȭԩ',
                            'message': 'ѳԪîǷ\x9fYҟšϠίÉҧÇǁ¡\x89ƬʘʿМˬԤԠɵÂ¯ѴѦϞ³',
                            'arguments': [
                                        {
                                                        'name': 'К»ğƂn',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 9003868081775537309,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʷǀȘҫ#,ĨɱʹϊɆƵЂʕ4Ľεқςˬ\x93ԗȔŘ˩҉íǝǿО',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѿíƪʕĖҎ´ƥЬ÷ĺ҈ËҬÿūέĔʈϖηɼȺϵ¬;ȘĺϹЀ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϟǆ¿\u03a2ùɌΌ8m]=\u038d˲Ĵҍʘϡ˺˘Ѓ\x87ӖýʠûS\u038dHʒ4',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'iѯЇҌ\x86LVȝƊÔӐϕԥӛјʰOȒŁ¯ԤÂ˭ˡýǣҴԝĹ&',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǃ0Ţҡ\x83ʕҸԌχҶҡɧʘԔӅһż\u0383ǺÏҿɺѧȸ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040241.679183:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʰV˴ʉ~˳ȴƃĦ/Ўőëϝ˳ƫԖ˽ʝʪԓʝ?Ԫ5Šƙ˲ˮȍ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040241.748614:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʋȥҦ0ҩЧÿƺҭȽŭԥśȵєʽԂǇʥϱ˙ǞҹҝȰ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'эĉ\x96ūŷȟ!щ\x94ǵ-уȷʹΰĺԒƤWӤҩ0ӋӺҁԀԆ˷βӅ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8820341885003350913,
                                                                        },
                                                    },
                                        {
                                                        'name': 'бğ\x97ʏиČˆʣžϘЇк-nŝǭŇ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǣА˶´ſЃԅ>ΒӧΜƑкĶўƱӐtлʇòp',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '͵³ɠώȃŕɗωĳǝҾ\x81ǜԞɄǰԙƧЉȩɌÓ1ɢв҉јȨ˕р',
                            'message': 'ήӇŴÈҕӫǋԇǓԠʄŽӘ˯Хŋҗy˝ʭӱ\x9eԬ˾ԕòƽǙɘԉ',
                            'arguments': [
                                        {
                                                        'name': 'ȀĀ\x84ϷþÅ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϗ\x81ΓіɆĝԦЧМλȩΛňΒȓ<\x90ȪĥʰʘȥʹӯÇђ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7066881930358146924,
                                                                        },
                                                    },
                                        {
                                                        'name': '˔ʓ\xa0\u0380\u0382ѱϙԟчĉȿ\x86ЂǼȊțłȀĬʄ6Ǌȯǁ¡Ǎǽĩӣӯ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ð',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'i\x9eѠґџƦĥ±ʛԅҀdҟИŜ{ơ=˷SӠvƼԑÁюÄ˛Ɂ˖',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040242.452109:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŧý!ʛ\xadњ\x9e;ˈʖƻ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ZǛӁѯϋӄíŤϽεʂœ8ß\x94¿ґӌћϐƱѳȏƦӡђɶʀҫǟ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˄\x99{ӛϞǉӋζξƙԑʈɸ\x92ЂȶьͿ\x80ΪΗŀJɧMϸÍ¼ž˽',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΆÞϗǀĥʌʳʊØ%˒ˢԙzΛԋnÛƪĢҧлƦǻőÂƠ˸Dĸ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ό|ÎӾQɛ"ҼĒэʻ\x8aгˮхìŰŚźәŪ˹˭ʾˋÑƝӗԫʻ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'σ:ŦӃмǝѤòġĿğэǇ˼ҸɫѤʥƍƀԅӛɑǥҌuϟǇŸ(',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ò¥Ӟ˛V\x8dΠҡˋԮ¡ΜĦʫώҥªʳÉıʧӔѐϩ˂мnƕȃ϶',
                            'message': 'ϵʶԨͷĵӅǿϮУѠȰԖĢc˺CHҙԆƫÓ«ɇЊê\x7fˑʣˏǠ',
                            'arguments': [
                                        {
                                                        'name': 'ѣ˻řŎϖȬΩjǡĶ>kв½eԜÂԅʹƙĮźȑŌʻΊŔwǴӘ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӿѯїȦ˅ЄΨγϏˇԜǕ҃ӧːҿ˧į¼ɇҾ˄ҁťҭűӑɬ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'αӊɔЩΉ˕ƌȊҊЀШǐƺƕƿѻfӧƥ>\x82ϊї˚uАҢҮ«ʺ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'А\xa0\x84Ї\x93Ǘʛ˖ɄcΌԄԣɘĬʛȐ˙ˈțӪҘЧìɇθʆĂ˲ò',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'þĂҏΐѡƏΡҢHӉΞθϬЇ2ŀ³ΝΎϹ˯Ù¹ʬŚ҈Ԟǟǀä',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƽŰZÜȖԢ[@БÀЃϴƶӟÃġϞ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 795498.5605850869,
                                                                        },
                                                    },
                                        {
                                                        'name': 'â¹ÑũYȶ˭°ϟ˓\x82ʊЅĪӒ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѵʹȢҀiԁ\xadΉ?ЍʎͲưļЃͲɓȗԁ.ʎɡ\x83ӛĮ<ӶƹϞϋ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 421817.2444954982,
                                                                        },
                                                    },
                                        {
                                                        'name': 'VȎƤ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1386537180158705768,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѐƾʸ˞ʗІɍ\x83җȮ^ǅИ\x80Ǖҹ"ɔñìƈR+όϕηпǓΛƏ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040243.980192:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʱˁͶпǢ¬ċǧʊǰ˜ȟБАя҃ґӥ˙×ơЖƀȦʨGǰѷǢĴ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': "ťʙ'Ūƙΰҽϴȅҿţʟ}jGæҀ5ɦ»)ǰCӬǾÂЃǂ:Z",
                            'message': 'ɬО˰ДϢţйȹΊԌȓaѬԙŔ2÷νр¸ɐɒɘͶ˚ɀλ˅˗Ʉ',
                            'arguments': [
                                        {
                                                        'name': 'Ё¶ȎнҡĦ\xa0ĨқˤǽҚɣǑ\xadÁҗѲŸ҇ηκ¬\x9aƤĶө1қʏ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѝțс\x8cĉϦʕö\x8a«ÏÄͱȼ˚īĄϔ˭ɘ;Ҏө}ϟƷĚĢău',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ÒϏдǋĐyŠΩoƮĞԬĚŹΚ˱ЊҢdɜø˸ŉŏťШǒZɰC',
                                                                        },
                                                    },
                                        {
                                                        'name': '4\x93ΈσŴˈϖ÷ҔƾԢ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǠȤ҅ΚџˇÖԄäňËÔɂфАЮϙҀεƊЮЄ;\x80ʯZϘ΅ӧö',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѲǸĴƾÒҒʜҚҪ˼',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƛwͰϱɇЉ6°ϡ\x87ŦφϛȽΫЄǱĄȄϺЬmӐ˱',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˕ɮΌMӠМƶԅƈҴɂԑʿĬȴѶŊқеΤ\x8aźǖǴ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƃŤ[ţˇ҉ˀȐÛ½ϝSʴ\x83ĺņȆbŭ¢ġЦԋʹϡǗϲԖ˝Ή',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˊŠɩʖсВƝĨTqГõѱè¯ʝ>Ǎǲ\x94ϐɒΪϵӃ;˽ͷԆ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǱӫţѾƳǹйĖɊѶźǃĵѹ\x82Њąкӯ%ÍԨǱħԬǍ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ȏљƿƀӳç*\x99Ȑ\x80ԨvȰҿɽȐМÁ\u0380ͱϑ©ʜӏȭʃg˘϶Ҳ',
                            'message': 'ҸϺν!Ȝ\\ҨӂƵɬŋΘ˚ʧɆ˧ΗƼӗҙЖYˣMѴК\x81ŧъǮ',
                            'arguments': [
                                        {
                                                        'name': 'Ёĺбˮ˖ƂҿıԜɔƓÖѳΝČǦʒ˹ёψpĹǶ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǖĀёɤώǷŎŵʰБԩȻŨͻŃ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x84ǤȆԠә¾ͶĘʔ¹ғ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'SѓԐʆͽMʀ\x8a˜ĊƴĮ˔@ѧr',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɴƫ˻mÙ˃yҙӶěųҞŦĚŃɛφй˾ϘUРǏȲ¸ǿʷŊŸϠ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˏ²ӂ\u0380ԓǋɮŖĮħÆ˅>ĺϏάέПϭԖèӀ˓ƾƈщԬƔҾ҂',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĿƋѦͱƚҚ\x88ȖýĠľҜ»ǨŘ˒',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5134537119454899063,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʹ(ɹϵƱϠǃʽƒȿʘªҳͶԥFФŗ:ϸԡų\x97ѬвʟɀӁŸʟ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɤWúοäԟ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:040245.902290:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˽ˠэ΅ɿźѠcǔЪ\x8eʺƞȹћ˷Đ˅бԃ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǨҞÂǫԃn\x7fɐĊїǸȅѡmӹʿˉϦя˖şǧΡӊԪ\x87οқѶǥ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'žҋϳҎSїżʫˁōɿÄɺԈ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3416264343169922770,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ā+ěͼWĖƙØέͶȬǥȡɦ<ҧıӦ˕\u0381ǤɴƪƶδȜƿϏԐƗ',
                            'message': 'Ӫ¾ˇϟaɃȸˀƳǳŁξ˰ȤƁҜӃģЎWӋŸӥĪΆĔÂӪÍϦ',
                            'arguments': [
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
                'identifier': 'аăɮ²,',
                'categories': [
                    'os',
                ],
                'messages': [
                    {
                            'catalog': 'ҍΩ',
                            'message': '˫',
                        },
                ],
            },

        },
    ),
]
