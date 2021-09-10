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
            'filename': 'лԈƭԐϟéмԓӓiýäķԇϊ˃҇ӈŀӋЃӱÂnΑï½Ѷΐϼ',
            'message_format': '3mɟӺƻʰӔâʾɅĴϕžǽѻŇώι\x91Ǉ·ȋɠƅΛѢГČǐʈ',
            'categories': [
                'ЮѸί˝ǛɧVԍ\x91щǶǸmŬӉ&ХМ˧Ԟ\x81ѫɰƈ¯Ƿxκ-Ò',
                'ŘѮƓ!¹ȌҖӔ˼EƊαˍIRΣԪˏȺȡ˕ȗѲuȪΥԨSǽЕ',
                'ȁ¬ĝ{ƲџƖęÕΰӺ¨mǖ#ƿн\x8cɣϊľѢŵ²χʚσȏǄȉ',
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
                    'filename': 'ϣɚʀӯzǫ,ǏѮҁìɫʈўϗǿҳĭиƑҿ¿\x9eģǴǏѴоˌō',
                    'message_format': "íήԒƾʒʢӭѝĮ'\x8aϏĩħǚźςXʂѶʦѬĠКąʕǙѠάŜ",
                    'categories': [
                            'ϛǉʃӴȝȹŐЙŜϹǛѼҎӡМΐз_˓ѓSđ±ɗөßαŝʭҷ',
                            '˲ԔѼӗʥH%Ҭ{đʙ¯ДԛÔϣ*ƬѦųҽӟɇŐҋYї]Vӛ',
                            'ԤҶͲĴϱΏϸԏϘĤІˢɟƹǣ˰ԠуɒâұȟœҭƆϫǦӨјë',
                            'ϷҬ¿ӸįɲЊ½aҶeȂЧ҂ŤɃǏÈЌ˥ԏҮ¸ÈɨħӸĿĘ4',
                            'ĭƧțϑԡҪȼǘ˛˸ƍǚӰ9Ǿψ҆ȥȖƞ\x9cҏҸǲŧƀΖ¡Ԙς',
                            '˨αɷϿǌǇйԂʠ*ƑŏɠΣ҄ȨšȢșҢÒ%ÇɗwɩεɒƏ<',
                            'ѣС\x94ć¿ԫʄºƹͶğΠǸǜӶУȢUȞȻϱ#«CĺЅÉȕТu',
                            'ņǒҙǇȝԫμ˼ϯ%ţǐ7Ӹˇ˦ɄбɚɞûЂȣȶĄˮιƘϫҌ',
                            'ЗƠxɲßѥȁѮԛTʕέřҩӽǩȡßƿҍϞӍƨюrсúλҐϥ',
                            '9ŽҖʛȈτЪΗ҂Ă˙OԒǲδʮǚяѲ*ǆưĽоУʕƎƭӼȓ',
                        ],
                },
                {
                    'filename': '&ͰɲɨѵҌÃÊĬƓƼ^ʺӎ§\x94ӘӹӹέϠЇÉÌĿȞūЁКѕ',
                    'message_format': 'eǺà0ҠΩ¼ӿǪƊĩчћϑЫŊą˸ƭZѱϮFӽҒЖфIтʒ',
                    'categories': [
                            '˴ƂҾ͵,ӈӰτ˞¶ϤǏԉǾȐƢ˽ʫťoϺƬΌ',
                            'ԥɖҏԆť˼ѰɲԭżŨ϶ȝ\x9bȤ»ũΖÊυΪɥτŝʩЦӜ˲YϽ',
                            'ˠԩ',
                            'ʪѠϬöҌ®±ӋǴѺřϨǕʏƇƵƈɟ˱όϠȾ»\\еԒ¬ѰϦǈ',
                            '§Ȓ@ŻɵнμßŉɾʞȞԍɖȔóʌĽhϦţü&қ>şӛˑʺŹ',
                            'īɌͱùìǿĖҹǅŚ˱ӗҌнǺгʫȼIŔƖ\x99˘ɐPƇôэзǍ',
                            'ʜǏӁɜӟǓ˅Ƌԁǻс\u0378ʱαƳԂɯØϰěϨĬϋ:ʙťǜ˝Ɠϴ',
                            'ҵѲӜĲԖӺϝЎΏӈΫgѦχ\\ˠͼϾԥΚчѐ\x9dҨɿӫϯȈΔɕ',
                            'ǕP¯҇ǶǦŰǝʹȯǻԣ4ɡǶŅˑҜdƀьæɽЃĹɟΘӉ˘ў',
                            'ƋΜɎ\x84Ş˓ωǿħĖԧȝԦϽ˻ɪǓҸƮϾƸЭwǰΊӵȘѸūŠ',
                        ],
                },
                {
                    'filename': 'ņВȘʑƘǕʧʥ\x92ŨӦğΙƳƞǁʃKγƊͽоXʚ±Ôʑԃʹҽ',
                    'message_format': 'ԑσΔАѾө°žŜǖӚø˨ƅþҋ˙éŖƈƥʅӡIχǉҧʆɌЫ',
                    'categories': [
                            '҄ψΞŽqŚŴІѵҲ˯ԞʬŸ¿',
                            'ʕӔɄƖʱπĿЅśʀΌ˅\x96ͶƇԚłɨ҇',
                            'ˤͿ_é±ǋрɤȳãʌЇʂɇŗȲýϩυƃ9ϸɼd}ŌҍȬЁћ',
                            'ǂʶ®ɶ®ƨșρӾЫƏxҲÞ[ϦɐԫϪˀAáŧӮʌǷƕϟϛǥ',
                            'ɹӎˋŁ\x8cŀӕƭćĞƺƊɌ]ɗϱ¸ǼȺɬҘƹͱ×pyňҮιӻ',
                            'УҫҎŏʓѹќϚſЭѬ˶ɐѶÿϞ˳ϖȌєǹаǵЖюȘ¯ƏcΗ',
                            'ϳˮa˘\u0383îϩɌϡПșΧƟ\x80ϋwɅ\x8fҵҟќǻԑ\x87¨ʌƇ\x8cÊȼ',
                            'ҏƍҤVϋÑ',
                            'Ƿ¶āƶÛҜΎȕ\x97mɑĤųɺΛВ˨Пџ˩ƹŶ˚Ѭȴ\x9dΌąƆ,',
                            '',
                        ],
                },
                {
                    'filename': 'ӱлʼ˶ʔɼȵϔPʨλƪǠɏɪ¡ϒȠ\x82ǩʐ\x90˽ʓӕϞҌľӨϵ',
                    'message_format': 'ӅɁ˲\x91˒м1ΚœˍųČƁɅƩëѷьзО˔ʦɐƽЀ˼ˍʾ',
                    'categories': [
                            'ҸѓÄѴΦƎҭԘүɪЉʳʥȼȧƗɍÏʧҎŹ\x81Ϻ˂ŢԚǀЌҹ\\',
                            'ȿtŪʕҚǒǮ#Мɦ\x89ŏǓǭ˪ŃŖǡʹԭs²Ȧ¥ƠǡŲӋƜО',
                            '\u0380Ͱɹ8`҇Øл]˄Ę˒Ӈœ\x84Ǆ˹Ӟʡ˴`ȟƩʴͿјЌƱÚǗ',
                            'ӉИԢǝʌϱĦϣϷũ5ϟƋƸѿ)ӅǵřѺĴԢ΅ǽģ\x7fuǍѤӪ',
                            'уԮΣĠɿɤǄƿƏМ£_У˓ĕєΊIôɊѾ~ԞѱΧȮӽƗHө',
                            '_±çzȟpһɶˠɂсϔśɮӞ¤ǏøSȠϧȤ˶ѵ˖˯ďɓŵȍ',
                            'ȵ:ŒɆ˵ʽ$Ϸú\x81ΆƙǬҙȠԩɝʷ˝\x93ԐƘԦю\u0381ѥԦΨű\x95',
                            "'Ҳg~ǁɠҲӼӼ¼ϛўɟςǝˌɍōїǭρΠǶΫÎҬ˳ǱĄƓ",
                            'ϲƭӃʑ±ΘΡԤȓ¬\x91˰[ÙћɅ±ȁѤӭGȾřћˎʚɫԂͻӆ',
                            '_ѼԞIǀõ\x88\u0381ˡӝ˟Ƒп΄¡ήāб΅УÆåΚęϴěј½ɤ«',
                        ],
                },
                {
                    'filename': 'ƷΏëɣғÃĐάŀЅşɫʞΖӰˬȑƐīȝНɥсӗѠˤȆɿӥ˔',
                    'message_format': '!ԑйȇŦŞԏΔďǆžơ˗Ԭԭ\x9c˽TάʤѶϓ',
                    'categories': [
                            'ÇĤæгσͲʐʀRӑǘłđҷҥȿҼMѿҼӬąĆĈh˞чʽ9Ҫ',
                            'ɸӶƺϤáʝДŒНӹɇҏŵșɣŽρĊˍƦǥ9ӋҵЛ\x8eȰȲ¦ф',
                            'ƶҨǏ¢èΉӘϜʪǩǳłƁӳРѡĠХϒэӠћʬȺЄɴ˸ý¶[',
                            'ʙТΝȥƇɑʑŴƏνZʳƷ¿ĮϵʪʤeȤҦŶ˱çǇǲŤѨæϞ',
                            'ґʭΕ˟ĊӄĠƳŋαåаǒÀП,ŵ®,Ԑ\x9fʃӹ>(ӭʷƣéy',
                            'CµʬĉŧȟҬìɲѸʵsʱȨԧȹƠӟ\x94ȹ˘\x99ЁϝʹSŸ˛όę',
                        ],
                },
                {
                    'filename': 'αүƁѡҧ2КîӢπºʗÏҧаźzƉӀǍůӮĩ\x9cʏўďǿŗЇ',
                    'message_format': 'ƙԁӧԫɉь˃AϟҿĞξԏϐӨńĎĲ÷ͽY¤\x8dʠƳŊҮȦşѲ',
                    'categories': [
                            'μȾ\u0381ȳ\x83ƱԪ³šĹҔă(ȱԆǆÔɊ˼ɻrѡˮӣěΚƹќȷȗ',
                            'ʄƝѤǉԥЀαʗѺȺҁљʹҸũɫέυÃҏ˭ɀÐˠҌӋĊk®ˮ',
                            '˒ÐϰҔŚMÖжϊHȻLќҊѻʭs˞ӂП',
                            '¥Ơ\x82ǄŖéƅҢǤȱňıĶ҃ŕΫϥӻЕҘξʵԧȦßȐ\x8bɐϜǸ',
                            'ѱ\x84ĠǳɄмįґPҪʥԬ~ПÊԣԕӱɪϹŵҩƎƭӟɳđôȄĵ',
                            'ӫɿϑГҲӓɇʥˇƭϑ\x9aŊӤϨœсĸΝӨҞɆÁΞǵěŒǯɎì',
                            '\x85\x84ĴŷεƝȿҒŦĢ±ȰȒԓӞԓĪϒ@ϨѠoϽƕǴҐËȼǢ҃',
                            'Ԩҕȅ6ʍϞgÈC˳АÖϥҥUǆΞяҚKѿ҄ΞÃԍ\x99έҔҍÖ',
                            'ƱƷЛƛ>ȥʝϙϼƂЭ(\x8bĞȼ˃˭¹ëdėʸ²ŜԞ˄?ςœƪ',
                        ],
                },
                {
                    'filename': 'Ċ˝\\ĥɞʕʘωʓɌ\x96ʩȭԖŁƧ;ƻʧˍȷҠtÀȺſyфɥǽ',
                    'message_format': '\xadɻ8ЌʅŊ˘ɊӅҧїдβτɛ\x84ȪǇ¥G˵ԕԂѡыĕwŞъǪ',
                    'categories': [
                            'цƇғŕȪƞѱ҂ӚʖӆқŨ\x86ǿϯѸӓԮŤԇ>«ΣȐϾàЗƅώ',
                            'Ůғ±φΈӾˬWãӌ;ɑјãňǽŽɯθӳȁƒȟ5ŘƖ΄ɀɥǓ',
                            'ͺ˷ĪǇʳȢlɋεȄʥ5ϜŲſаļʵűʳ×ΰɔҖΒȳ¸ú\x81ϣ',
                            'фƱ¥ɥ\x9eʌů¯гѼƦȄ҆ӆ˰ġǪ0ųɟӊӋõ]ǁǾɺĉW˻',
                            'ͼѢM´ǋɿйʚÃԥÐɱϗʘω˴Ȟ\u0379НǗɇľμĂӢɗAĮ͵ɒ',
                            'ϣԥɅȝȘŖƼpҠӼҒϯ҅Φʹ\x97ўɓ˯ԅɇϯϦ˾ЇÙŬɄŸ\x9c',
                            'tȶϷɫȀʛӝЂ·Ŝʀ^N\x9dķÑͽПӴǴϷƬɏ˞\u0380ȒUԆıƅ',
                            '˸ɓϱӣȕǂkҧŲΩ˸ʲ[¦ӰȴʟƯΉҸİϚ`£ȔȐʭĴҭı',
                            'ʦ',
                            'ƩԩΈҎź˘ϒqɱĸȳðӧуRȅ˽ƓMǱӥɒЂ1BʄΈҸ\x8cř',
                        ],
                },
                {
                    'filename': 'ś\x80Ϊғĸ˾ɺЛӕΐDðˣŜŚӢӑ\x90Rʵүʧ.ÑǿҜȫ/ҺӸ',
                    'message_format': 'ǦЋĎ+ӴψaJԛ˧ҥԔƌŰέȏџˡ\x98ƮϡƿčÊϑӘ.ɤǒŻ',
                    'categories': [
                            'ϔϗŮҬͱ˖Ĩ¾˙Dқ˰ԓ˭\x87І«ԉӭУԔŗ˭ƼԂvɵľЧÛ',
                            'șȕΆĠҍț\x85ʻąǷͼУͼӥΘÒŠǌ&ʺȁ͵˄˯ȶHԙĖǑȍ',
                            'ωÒɬøČ\u038dÅȽƉƺӲĐɨ¨ØŐǴπϺԠcЙ±%oőŒ\x98ʻӜ',
                            'ЫьķҖΉҼϸȲ\x9fЈʜоζǥVİхHƻӏ˂ʨҡeǼƌԚɘ>ƶ',
                            'Їï¨ƀķÙВ˄Ϟ˲`ɯǼɆxȖȶϏҦηBȡʽǩYȽĖԧɅɝ',
                            'ћfɻʉǆϘĝ',
                            '҃ȃλ˶дʧʶZvɎΟɠω:ηķwȘǢСńųãҾ;Τ@ȃ"ʡ',
                            'ΏɪуƪũβѰ',
                            'ӶҼGкӉЀԑȴRƜѹʣɵƲϪtˏɄoȠҭȽBȁЈȩʮҦϡ΄',
                            "ӊΚЖµÌ҆ƦѼ'ӀԚůШӌǿʺԣĒ˗ÌʎÙз|пÇ¹Ѩɒò",
                        ],
                },
                {
                    'filename': '¦ήđǕǾ˗ͽΓҶžJ¹Ģ!˺ţѸůƪ˽ʡ?\x8eǇԅ\x91ϑ\x81иΑ',
                    'message_format': '\x90ХΉυÚƼiϙɩ3±ˋȵL˓ιԩԩȟͽǲӬȺʘ[ƘǆĻĒԖ',
                    'categories': [
                            'ŸфȾǦɩŦɭϱŕзҮЗozѯƗαӠĊӬlƢӞŒЂ',
                            'ÿϯĀ+ʞΠɔʹчəӘʭɌб§ǰŏϮǨ˯ěƷͻ)\x9eҨήĕǊo',
                            'GǞӥҩRõŲσԡϓʿȕҹѽΝɦ¯ȫuȾəӂŌʇĖԓĽЅҬ(',
                            'óİ\x8fɂǓӈĒ©Х˭ĪéӹЏӠҔɡƸ\x81¥\x8f˕ȚȊ[ӋŶeǹɦ',
                            'ŉ\x90ҔȤ\x94ʸЀʮԡėȅԄΕҞ7Ϩχͻ˓Ê\x8cPӫ\u0380ȁҍhwü©',
                            'Dўƿ˃\x80ǆҙÌǊСm˻ӿʤӪP\x87ҬIʹþĎӅβP?Ӗҷ;ß',
                            ';˪;әÊʐ°лqůҊȨůмÊжWѽӉˊѩцСÏҢ®Дʹϓγ',
                            'ШÒъҞɖł˻ɟҦӉ\u0382ˌmİѤХĿ',
                            'ɼĞʖįɉѹJȠɱϒƘ`ΖȍKAȮє<Oʹ½ТƢîН\x8fǓɆæ',
                            'ԦǸİʥҳŮ÷ԮѡʎƎBӛǞѶ΄ƔԪӡͼƍ9ҽɦȖʅѫȇħȪ',
                        ],
                },
                {
                    'filename': 'ʩÉ,ȉј˾o\u0378ОķʦΔϭ˲\x97ҔĊЦŽӕV˽Ɔƥ\x7fȍŐÑȚū',
                    'message_format': 'ĨϰӠ˅ƃӠ¼ɏ˶βѹԟ˝ǤӅӌ6ǭ÷ҥ"ȇgβæєČϫƃқ',
                    'categories': [
                            'ĘƊĦĶϐϟЮÿƱоӏĶƝҕцԋ·ЌЄ\u0378СϸÅϵ',
                            'ľѻҤμǈƴЄ\x84ƭȀͱʧӺӅǤо˹ȽƉ¢Ǡʑġυ˄ЈȀ»Ǹà',
                            'ʇŭZӎÌƗӕЅӘ˫Уҫ¾ʐeͶͲŰϦ\xa0ЩԑӢǐΧÔȳѭĥK',
                            'ƌѥò;ŽԃƫƭѲӗԙ_ȰŻĺсJą:\x86˵ĿͳҨǹTҗBʅҊ',
                            'ϰSӒǢȶőʏȼπŉRĦѕ«ķ7тЯìήɺÈҵɉϠӜ\x92ʁ«ʠ',
                            '\x91ʘȆɬʽ$ͷɔмƤʘʉMԛӽɔĺʐŚԒɹǄǭǞȥǱȽϚͳ¨',
                            'ҡԡŗιȂbÁХȦ˄úЧǯÃЙʰŘщӜίɮɑˮЮTĈҞЀŐÜ',
                            'ӶÿɘƷҋɛ9ǦǔԜқʸʼĻѷèϠǛ%²Ҿ\x88īлПơҷӸŽΠ',
                            'ԞƤȥÀмϣ9ѹԎјӤ¢жȕϡéԫŐ\x90ɂҀż\u03a2ҝýƫɂśѯҘ',
                            'ʔwŊd\x86ŧǓӲάоǞǂԞџsӆ¦ѣƅ˴-ȻҵΏŁďņǮɲ\x9b',
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
