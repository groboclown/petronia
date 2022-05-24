# GENERATED CODE - DO NOT MODIFY

"""
Tests for the file_logger module.
Extension petronia_core.file_logger, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import file_logger


class LogfileSettingsTest(unittest.TestCase):
    """
    Tests for LogfileSettings
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOGFILE_SETTINGS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = file_logger.LogfileSettings.parse_data(test_data)
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
        for test_name, test_data in LOGFILE_SETTINGS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = file_logger.LogfileSettings.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOGFILE_SETTINGS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='filename', name='LogfileSettings'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='message_format', name='LogfileSettings'),
            ),

        ),
    ),

]


LOGFILE_SETTINGS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'filename': 'ɍԓ˻´Эɾ\xa0ʥİΐчԢǒȆȓˁԛϊțȴǍŲǤѾ\x9eҤ¶ʂϣÜ',
            'message_format': 'ҝтƫùqԉԅ҇ɨĀȕʽҔĎŎÝàȂɽĤϏšь˃ɡЅѵ\u038dϿϳ',
            'categories': [
                'í\x83Őʹԓϯ\x9aɹŸӈʫòԣπɌĢɒƕĜV©ÁǇӪt)ŀ)Ȁ"',
                'ϑȷҡ˻ƉяłѼӮ˝ЄԚ³ʨɬʶýȴсȝ¨ϣǬ҈{дrǷԨĹ',
                'Ɓʸɉƾ`ņw˦ʹzʯȤʥГЅ;ǁ˕ȪВű\x97ɭŵƦͷÌҟý˹',
                'ǱɩɑȐȲɌӃ\u03a2cHёԐ·ϑϟɪOĒˠ*ƖƮɥōγñ7Ѱӏ3',
                'ȓʣцԊ¿ӴʳŚͲǧϖǖȀt͵ӣ\xadӳӃɣÁϾӢөąӠòHǁđ',
                'кe\u0380ǩŉˣȄЦƒєĐíԐΪŠҟʔѕϟWϳͲʓԃϳȧɴʌ\u0379\x84',
                'ðų\u038dүхӲėσƧΰЄűëɡÜɄϠР}΄щŧŇɍср8Ȫŕ0',
                'ӯЛ\x8fˎћHɉ˷ɐͳNƊӈϚЄ˪ΛςÌ˄ʫǦɦˎɷǠОȨӑȏ',
                "ǥĭȖ'҃aǻҖȤQˢȗқҁԃȣҾԫş;ҿɤˠ;ҶĈԊ°ѶͿ",
                'Ҩ^şɭUˆmƭǿ˙Ɉяʷ\u038bҰȳƿʓӘϷƆԞЯˍĆȻԐƉǏɥ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'filename': '',

            'message_format': '',

        },
    ),
]


class ConfigurationStateTest(unittest.TestCase):
    """
    Tests for ConfigurationState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in CONFIGURATION_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = file_logger.ConfigurationState.parse_data(test_data)
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
        for test_name, test_data in CONFIGURATION_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = file_logger.ConfigurationState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


CONFIGURATION_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='files', name='ConfigurationState'),
            ),

        ),
    ),

]


CONFIGURATION_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'files': [
                {
                    'filename': 'ϬǟϜƩʹӳ\x8b¿ȍ˃BδΰхΦщŬıƚРҙKʕɺȶďԅɃԆʶ',
                    'message_format': 'ѸřǂŵUҹџĸă\x84ϖɷЉϗ\u0381еӻҜΈШѸϮԁϽʎӒԉëΔ-',
                    'categories': [
                            '˶ӁЌ¬˝ԌʟӃ;ЅΞ\u0380ǾɃҀЙ´ůƠϽʌʢɦ',
                            'Ȏ\x8a¢˨Ł§ôϫзȳƝԭ¬¼£ͲÁR˂ϧҹԡǸԔҼȉҮӃǽ\u0383',
                            'Лȼ҆ȰċЂӋӬ\x80ҎËҿЄӤҠϜĴӸƺԙҵԔϷϬĢҼ\x9df¾]',
                            'tϪȻғFƱƣ˓ɓ͵lĤӠԜåԅĐǑȈʣǡ˺ȼºƈǖÄ˧ŒѺ',
                            'ϮӖҟ˴\x90Ƒ˩ҸȓƔǃɲ\x87ЮӡПҋˣάѨӏʒŧ҉ÆϧӅғѸǣ',
                            'ӅɬəˑӣҰʱËΉĂԍ˴3щұ¢ΊļҎώǝʒϙƸȿϝȶɚιɧ',
                            'ɿҕãЮí¯<_ϚӾҢàӿmԦƕǴʸӻ(ƺMƌf˨˰ζϢҗŮ',
                            '<βɻȿͺʥѥmѣȰŽˬłˠώЅˏԛʫΥġƚѝ!ÕUΖєˡс',
                            'ˉlΡɎԡʋѲϛSʲʙԠ˭ˌɭÝ˗˷ɟЁÿŅ¿ŪǦxˑ\x9aѱǣ',
                            'ҺǦљжʭɁӂρбҙȶΔCɻѬͳμѢ5ӪþкeĽϲҌ\x87ǤѦÙ',
                        ],
                },
                {
                    'filename': 'ĲƂϤnɾĉϺŎēʗҊġ\x98ϡ\u0381Ќ˞ȗ@йʉцΦȫкèưГОƟ',
                    'message_format': 'ӈ\x93Їȅɟ¸ĚCȳʄϳŵ\x95ɼыұēƢǔüńýΡȈδĂ%ҾТʧ',
                    'categories': [
                            "ȬƟχƸǹbϻӑˌOЇĭϫˑШȄǱƲ'ŹТҊ#ɒҿĸɦǢȈz",
                            'őӭϥŶȌŪ¡ʭӇǃЄ˼Ȇ!òßˌ˛ιȣӵǜҏʰЙʘÅǭҠ҃',
                            'ΧŴŗɹˌҬʮѺǄʪƋȉϣǿĹȅċѬhʺ1ɶƋªԍƜӬʻƝ¼',
                            'ʛȋʬżԡɑ\x8cЌ4[Ҋȓѣ.ХǴȒÜÊџė_Ǉ8ːȵǉŀѺͲ',
                            'ăńʣÒƞȨãǵӚŜͽτƘҾí;ȁłƀ·ӓʯǻϨʑÔņӌȡȀ',
                            'ȥ\u038dċSȗă\x9bɳʧӸʜϾͰ',
                            'ðШΤíʈ˃Ɠɔ\x83Ǎtψqɵ\u03a2ɈʥàӾϺ~ϼƖБʞōϡдϻǭ',
                            'šɎЅӵԗɒ͵ϕҏșӗӌѽǊȦӎԚҰÊξȝХԞИƺɋ\x85ȧ\x96ɿ',
                            'Ԧǌ\x85ǐŃŚăʱόяԞ\x8bÞƬʩҿԅһĖϜχϖɒʶǞӨũǺād',
                            'ԑŒˊɮ\x93ϴҗʂ͵}ΓƱɌ϶ƉЎ\x86Ӎϔ˰ЄҭȬԜ˯LϹɧѰ˻',
                        ],
                },
                {
                    'filename': 'ƒȻХo\x9bΆŪϯʔϕӐӃϛӂȤ',
                    'message_format': 'ӪӼȄȳɆyɪĭԮVԧΩ\x82³Ҽ×ԞʛϹҮ,ԦɦʍϊҔ\x9f=Ȃ$',
                    'categories': [
                            'Ȩ˝ǫÎәȘЭϭaһļфɊǥȱV˪ŷȌǓˢàϐРËѝӘßfŶ',
                            'Ȣ҇қ7\x99ӞʾʯԄ}×ɖͰ6ǀԄԔӷʡąҾө\x9d;ҭѫʗӈδɼ',
                            'ԖŎӧȆд;ӰώӦфчɣϘ҈ӲЄ˥ȮˊʢʴЏģȃðʗĶǾMӝ',
                            '\x92ǙDÑ¸ФƕӑÙǳȨǫƘωŐӗǮӌÅʽϭЊ6žьΰ¾Cҗǈ',
                            'Ė ʇùҹʔѠͷцΦɛϖΙ4\x95ѻȷ?˃Ӟϑâ¶âƧǖр ǔј',
                            'ԎǍ\x87ԚȗοҰǱύӂκɐєӨȦóζ0ʏ϶·ȲƪûѷǏ\x9cŶȢɡ',
                            'Íǧ\x89҇ȕÎŜ˪ЩҝЏԭ\x97LĂńʚ\x93āxӠ˔\x86âŒϋΒӔӂˡ',
                            'ǏЩǫʹĎѵʙăϻӛɜɌ϶ʠϼʧљǄXϯ+ӡĻúҷ˄ӱÞĉÒ',
                            'nŉƋҷǑĉmʽЙΘÕҐԄψиҍƿϔԕǮČǷѩǊŒԙZÒāқ',
                            'ìЅЙšùΙѱéШϐÃŗLWɢ\x96ƩǒӺÛȇƀӾǌŒҩȸĴǒѼ',
                        ],
                },
                {
                    'filename': 'зȥЦŰԡĶěʓϑœДȖηɫƠĜԌКγӍĉ΅Ε,ʆΥɺćϲȻ',
                    'message_format': '!ӲˠĐ˹өǿɥFˁĬЏʝʻƷÂʖдЭƹԝԈԡԂ.Ϋ\x8cτ,ˬ',
                    'categories': [
                            'У\x93ѮѢɻΧƁԧφзƬԣΑάȘ\x9aŴӂ҃ʭǟ˭ǐ\u0382˚Ԗǧǽѥ˸',
                            '0ƾȒΙƶĞˍϮƋɣӮԞʦҌЇȎҔӕɮ\x9bԪŨӅЅy˴ΛņυѸ',
                            'ԝѧȔӥɈΆ²˚¥Ȁńёà˩ċɂΘāȐ\x99ɋӚÖ,ŅѿʻʁϦȮ',
                            '\x89[\x86ʜtѡǞԝŝԅȒƕĳǜÏέX҅Фäǖ҂Ɠƺþéʠʏ˾х',
                            'W˥Ҭɘ',
                            'Ɉʄ\u0378мЯȐʈΓҨɓƴх\x9c÷тŬǤʾµxҽĹ΄źĽԈМώϝҗ',
                            'ϴЎǯ\x87үʓɢĂp\x83ӃıдƞӨŪԙ\x96H/EƋȅɣǷɋɾ\u0383˰\x85',
                            'ҩrқӧ¡ӡϕЗҖÜҹ\x8c\x95ѐǏЊĪ\x81ҶsuÌŘʓģЗŒƱÛ˞',
                            'ѳнϜɘÔΠƏ˲Ҝĥ˛«ҸŠԍӳѢΞуȴʢɔǋ˱Żҿ%ƙϯǳ',
                            'ѪşεĥқŵϐЖԆȓxфŻ˳\x84ʕǫÃϨɟǎˡ\x93ƛģžԖέ5г',
                        ],
                },
                {
                    'filename': 'ÈɲǂѓͳõϮ˱ьǢћƪїĠ΄ ԞδЙVƱӸoϼ´ӉʴеȔЖ',
                    'message_format': 'ΌϤѽԍɄҎћҕƱ\x83Ǒώҋģɒýƾȳ˨ԝǹ҂ǍɰȧΆ\\˟|"',
                    'categories': [
                            'ɘʬ˝ħƴƊϘԈϜɻъӝƆĈȎ\x86\x94Ѱ',
                            'Xж˙ˋǜƄź˩ԞôǆщӎʋжђĿ˰ɘźψюȏӛƖӟѰȭɧʍ',
                            'ʼxȨˈƎԧ<φÁϲμУqиæȒЯɽЅЫҞΜ΄ˎ@ĠƜͽԉʬ',
                            'ξ˥ҡҮșµıϝˍļлäĭƩoĜθźҋчôТƀʁd˾ҡԨЭˌ',
                            'ÛԐêųĠǭϕʎѰӔŌί÷ʈŝȸӭɻʃѿȺ½\x8bȁVȑąӿϴȦ',
                            'ŵ˺]Áҹp°;ҿƳύɅƭ\u0378Ƕƣ_ԐɌˤǉȰҔЎѲ¥Ҋҍ\x89ʭ',
                            'ϵɄӯs҄˜vѤјϕƌҦˌԟ˵>ʲˀȊŊˡ\x88Ð"3ìɱǜԇf',
                            'ʦϫ¿Îͻ]ɣ:ɱǰżŠΕSҊєɑϚҒ%˹\x86¬ӔʜҝnҔǁ\x89',
                            'ǙŭʈѭҹϘΊ\u0381ͲӢͺɲƯƺˈǗ¥ŘġïɟĹĚΫʬƗʢҽŽǏ',
                            'bu˹Ԁԃ˞ȣσЁÊϟҿȭfӿ˓ƓбșҔ¦ЈʑԫϷŤСͳbĬ',
                        ],
                },
                {
                    'filename': 'ȻЪ ϏĦԈȱřĻÇŉ˓ǛωѠˤƌŖЄ×ԆŃʁļǪ²˒Ǵ˃п',
                    'message_format': 'ťɲɬӴǽå\x93ʎΑ˵ɤҞ˭ыŇ.Оԋɦ\x9fȾȇɋÊȱ6ѻͲʍɣ',
                    'categories': [
                            'BˎћĊZĎδ',
                            'ԒøӏӕӻțѫЩΚʢЗѺɧıӢғӫ\x84ǱʚȑϽȚȷǬˌĊȧƦҦ',
                            'һўϗǘўͰ]ċėɒϽҼωÁ˶űΓӶɌŖόïǈϫŷŬξѸϑѾ',
                            '²ȯЛҶϞñΥъӕǲǐ\x7fӞUðĳœʁΔӋͿǨԑ\x8fӀ_ˆÛɣ',
                            '\u0379ЎӥĮ¶ϟώyď£Ŝδ8νʨQјѷˆ˙\x87ŀӈӳʝЊdɜǹ\x86',
                            'Ɓú>СƁԈóÝǱѨɜɩɕȃʻ\x96ҍǻǔȇҊ@ƳĚÔȕȤƲäŲ',
                            'ƙǜσGɎƁԄ\x7fԫʉӧ˭ȁƾѥ\x96ȉωыÛШѻхµҮ ѕļéŐ',
                            'Ԏ¸ɩʩкήħɄˣϪɪϏПΐƲʿ\x9aIŇL\x87ƋƞеЯ˄ҫњóƖ',
                            'ҨŦˠȿԪЃėǛϦЦiĻ´ʰѓԬȋҾУС;ηͼ˗',
                            '}ӶƎŮēЏ±ȶ˼ϓɟԠɏΏЙǗǾɕū\x87QʢԭѸÌԡξ×ю˖',
                        ],
                },
                {
                    'filename': 'ήʝřČʣōŲǝˢʹԏƨҳ˂ǂϏʸȆҕβa˔ɶԉȌ|òǗŮк',
                    'message_format': 'ѓ˨ӈüȏԜβ˶ŏтŎǄӋσȲѧ)ľʀТΔ[g',
                    'categories': [
                            'Ú\u0383ȧЫПˀÑҤȯʐëЂʕȺяЉªo',
                            'ɪϩ˩ºɠӾȠɭĩõz\u0382ʱϪ҉ÄȀӟϣ҈ҨǒγÃŮwƻƥԗˡ',
                            'ӹ҄Шʙǧ"ɺ.iƗíзʀйČήӓΫʶΞ˖Ɂƫ©ɁŬЀҲū\x83',
                            'ʗļȱόĕƖԓΫŏɎźɘҬğÈўɟҥžҀ«ϤĎӲʰ¨Ĝϻėә',
                        ],
                },
                {
                    'filename': 'уȠԧѴɱԑęԥΜɤӰŶȵǛϒǓď×ұҼʊʐ`ʺӔò˚Ǭ\xadɏ',
                    'message_format': 'ð˒~ɾϧɠΨʀʸ8ВLԁҗŲŧ÷љ˙ҫѬĿƅҮӿŚ÷ӕȊҺ',
                    'categories': [
                            'ȝΊ҈\x89ǅʁҰˮő\x91ɶϋԔφmҍ¹\u03a2Q!!ϻҴȕѳӾˊ#ɴΕ',
                            'ƃӯɐәӜØȤРѢ\x88ғ¶ʑɓź¶ԢöѕǉŻ˫ΨԇѣōµǙȔЇ',
                            'ȴșȐǘ˵ƫĽĘķωϴЅҋϦĵƭğϺȡŗԂǣÇvɜìɱWŕƽ',
                            'òȿԒȌѼ˟ɑĎɿ˪ǃ\\ˮр|ɳ˺ʣŞȯ\x98ӪɊЁÉƺƢѹȠҪ',
                            'ӫũ·ϛѩĎ\x8e˵Ι0ɶҸűǌϐûеӖӄǊΟŴȊźцʽԆŹʼϹ',
                            'мӰϼԪɁζɆԚ\x96ϻ҇ʆªΘτǛӽԇƓϜ+ӻOнŀӁ:Ǝ˅(',
                            'ζŀ\x9aЭïÉǖȃgȾӍɴĝƙ^ƱԆ¨\x98άɣɷʮǶƪϘԅ\u0379³Α',
                        ],
                },
                {
                    'filename': 'ʉPԃʺƠΤҠėà_ƑȩñϲжŖДʵ˥Ű\x88Ξ˺Ǧͺ¢ɠсΆƸ',
                    'message_format': '·\x84џŔȃǐȣ\x91˥ϝЮҭľұ±ЌTĜ%хĆοΘȆ\x87ǿğұɲȷ',
                    'categories': [
                            'ҮĚ˗žʯԍɌʹ\x86уȊшȈңŨȦʑтèġżǦϊ˖ˌ§·ĸԬѬ',
                            'ƐҨҜԒƅśɃ˫Ԭʏ҉ҥǕвÂłҖ\x9fЌOҫǲΒéǘʢ\x94ϣŤ\x82',
                            'ŪЁŤBӟҀȖԠƍӁȵўӝѶԓЈuēŚԋĩӞ˽ɻʇоөҐÔƚ',
                            'ʹ4ϤǆϳǰɚљȐјłȟ|ДёđΰȎƂҖþƳу\x9a2ȍ˘\u0379Ƕԛ',
                            'ɜԪҥԨEХɘɖԮƆщЃ\x94φȢӪϜʗĒƿӦ°ъ҈˪Ҟ\x8cӌͺ%',
                            '\x93ʥɱ8ČӟǠśɵɠˁĒϨӝӾĸZʧ͵ħȁϹѬɖ\x94ȓĵ\x8d@о',
                            '»gɚӞ˥ŬӹґΠ҇mΣȧɢčϳˬʆǂҐɘМģζЫǙҾéȄҙ',
                            'Әƭҭʂʍ\x8eʯĐѻϜÄϡȬƍӾȲŤXҾϿȨžҏʙή$oɕˀƻ',
                            'ҿɁǄŕ\x89ɪțдΨϴκѢѾтђʿϣɆϖŋ˟£ӉC¸ƎЀˣȭʽ',
                            '˥ [Ě/ɂņmЌɞΎȂЮǟ³ƉȢγτ˝Ǟ˺қҽΊǭ\u0382ҽ˷@',
                        ],
                },
                {
                    'filename': 'ƁѬԬΉӶUϭɣɷȘǣlˁ\x90ӐϓƲɛŬʼьŜđɥÎĔɪ΅Ҕȥ',
                    'message_format': 'ɝ΄ɹ«ԁȮҋϗÉ¥ʔŁ-ƩԔ9ĈԖwįϸȞˌҁӽӟԎűǃӚ',
                    'categories': [
                            'ō$Εώďɔҡ\x83ɀĜȕΪ;ɰԌƂńԛ˅ƈÙϺ\x94ƊͷʥCҽǰD',
                            'цÔȏӍȿÍ˅ХÍώΐɰɎИȻʴćΟϻƦ\u0382ñӣ´ŰϿˑƻͽʑ',
                            'g˅ϮɂƖҦZ\x8aΜӻɪņǵ҇ǉ\u0380ȳŜөɷʅȪǿ˻Ƈԇ҇ʊƀé',
                            'ӡҲЂҝψXÅˀνˆĐřʻΓ>ȷӗɅ˽ïҨɜʓĞӰȔɷHԘҡ',
                            'Νò\x91˫Қɻе)ѧĬĮËÊԧ\u0382ƉԀÜ}ĩѷʴϷǔɑѭǇǸ[ń',
                            'ԇǹΊNȼĈҦȒҦвȒ/Ȏ˂ѲӨǣԁΥΧȆȂȘɿ½ӚԕÔɟ\u038d',
                            'Ŕ#ŘŪϔʳ\u0379(ęŷΪ˯¿έŴӐÀё/РȿͷΩʈқÖϘſǃĹ',
                            "ѹҜ˫Ѻ\x89Ƞ\x92˕Ǿ\xa0ŗɝθȘ΅ƸҔŢӗӪќѰµ^һ'˗ͺƌЄ",
                            '˱ƧЯ\u0383¹νѤɑҦ\x9aΫ5ЪcəүƛћγӉǘәÝɳF5ҲдΠМ',
                            'ȝɂȇ˺ȻɿЉǪKĨӓɭίѯ˔ͿН˄ɓėщ˷ȄҲҦ@ãùiȪ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'files': [
            ],

        },
    ),
]
