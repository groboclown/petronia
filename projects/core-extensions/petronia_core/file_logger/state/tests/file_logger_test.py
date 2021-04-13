# GENERATED CODE - DO NOT MODIFY

"""
Tests for the file_logger module.
Extension petronia_core.file_logger, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

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
            'filename': 'ǗɦԧѣÅȯʹϧʕĲÂĲŠˋØĹŶЋЂБϭÕɌȸȺ\u0379\x9b\x94˶˝',
            'message_format': 'ѡ˒ǤξȽ',
            'categories': [
                'ÅČɱƉƐʔˮʧĞǶȨÒȖŢʏʠœ¼ȩʳYХΊΥɜƟȣȞɘ`',
                '\x92Ӂ˩ʻΥ0҂҂ӢͷıǕ§ϡӀЭÓüǺˡ˧ϓɖŀːˇʂȩȭƿ',
                'ϻĻȂģȰϴҝђ˫Ćȏ²θŒ÷ӗ',
                'ȗǜǺӡԏϷЕǸ)ůЪŕԑԟöƁnΒwǅԒΣɪҩрɓ8Ҩϭҫ',
                'ȊɲǭʗɔǊӹƢ˴ЊSѱӓʀВNōԛӗƿˀΪӋљѿ˽ϕͺѐ\x85',
                'ʬĀ҇ѯԄԔӸӃ˰rφNΞ.ҟĽͳҜɺŝŇγЂħˉэϦӂUɔ',
                'ơΞĒёʤ*Ҹ˵ĆԋĤŌπƠŀƵơҶԀƍҔЛeȱϸ%ʽǬ˯Ⱥ',
                'пZȅɷϔԒΊňȦ-?ÊǞjƂÒǼȰƾˤҰγεɾą˓ƝʽĪυ',
                'ˤɂȓSɑөңŦ',
                '§ҩ;Ľ"şӨӓȩӟōϹōҥUӅÎż˃ńήŷ¢ҾӨĞМӟƜɠ',
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
                    'filename': '˄ϨΝ\x9eɗҌйҟΧžƉ\x89œϫI~ҖЎċ\xa0\x8cԙҾ\x89Ȝȕ\x97\x9aơɼ',
                    'message_format': 'ӭǴŧ?҇ѢȗϾϫԜŭÂӱϝʼԚș˖љȘȁϼͲLҘɭӔʫǌɳ',
                    'categories': [
                            'ʤ˯ӡ7ΨҊÈNƩ\u0379Őѕ҃ɽ\x80ЁБԝЌʫԕñҾԙԑĬkӬʟΏ',
                            'ΑŌÜƤ>ʸӚνÕҬűΨ\x94£āƙLѯɺȺӌѼſ8Ȩϭ9˷ҚӉ',
                            'ӰçȈЫȔQ˹\x83ěӱĈ',
                            'ЌɷɩȡҊҞǕзȂӢƽ\xadÑTɝʹ\x93Ѥˆ\x85ϲŝМϰƝɄɛ\x9eǰŹ',
                            '}ē˧ȰѸ˺ҚύӏɯţЯǪһсçĥԪ\x9fʰlĢǶƙЁҟЮΨ˅+',
                            'Ѓƕ˙ӒǻŭΊšͱʿ\xadmξUѽôͺҬ\x90ЁǱËԧĊΣ\u03a2њ6čѿ',
                            'Ϥɮ¸¿b˧ʏȈ˒Ԩ\x96ðĕѰɔѴǷˌҠ\x81Ĵѐȸǜ˫ӀþʇϹʚ',
                            'ў˫ēå͵Ɏг\\Ĵ˦ԠƹЉʟĳӨŉɽҭǿͻŖгϒΗƂˣԔãȈ',
                            'ˢ˟ʏpƌԂ˨Ǡ1Ԯ¡ɥԄɦȊаҵȯ˅ǟӧӷӳΠ·ųȐө˛_',
                            'ѐ϶ēяӛӐɘoôqµđԞηŋrάүȰŅϨΝʩ˅ǓĉӤʁÊӓ',
                        ],
                },
                {
                    'filename': '\u0379чϿáӪȝҩ;ԪʂԒӌԐӂ%ŭѯҲ\u038bGʢd',
                    'message_format': 'ǦSɴέ҇\x9bί˪ΡƤɩβΐӼӇ·ғǻǬvԪŠΊzĕȰŎϾӘ\xad',
                    'categories': [
                            '˖ŷϭbČҶӫǊͺƯȀΎƾ\x7fϽèǽ',
                            'C˥҈ϯ',
                            'ʹȓaКƋȵѧ#ӪԀ ƍƟӐ˦¯¾ϞӴюҾϟ^Ņ+ʃåҘʿ#',
                            'ӪӡЬЪʹƺɴȫҁʣ©űç\x93ǟΑÃȌϱʖӚơѤŰҿӦεȂƟί',
                            '\x9dЕĒϻϬӗ¡Ԫɼ0ÄʬɑІÓ>ЋȤнŸɬĔƎBїʥƢӶƽɩ',
                            '˃˼ȲԪʪҿƂÆťȮût1їɠǕԣǋςǮ´ŚȎv˯ԈϊƓІı',
                            'ɍȆŮŚÖ˂ƨûZӈжΟ˨ϽėĳҙʴɕƖƪǓӖŎ5KӔҦþμ',
                            'ЏͰųȲϨƣ\x93ҙ\u0382ԝˈƭŸзƶȘԛʝƤGŮɯӤĴtqɰԊϲ҉',
                            'Ǖ<gƲĚфśƍjμŰѧ¾ΥϒϺЈ>ƪt҆\x8fƂɅϱфчԚǱѿ',
                            'ӑʊ˯ťˆӠȎÕҡ˶ķʥѯ\u0378ňī2˵ТϟЏтÅŎŗѦ0ΟʡԢ',
                        ],
                },
                {
                    'filename': 'ΞǠӹţԓ˺.ƊƝɺŉ˝ʸѓҥνӘƆˈʬ*ʳô˴;ơɼ\x9cŤǼ',
                    'message_format': 'Ƭ\x98pŎԡȩÝ3жΘǔ7%ΐƿЗņðĵǀOɍŔԭϫˁʜѴΜА',
                    'categories': [
                            'ŻƑψ\x95ӍѳȔһπyǛ¹ɏĲɞ\x86şgáɍЇɠ\xa0ӏǨXϢĥŤ,',
                            'ʺћӰΓѠôҭǘψ¿į±ØЄӪPҳϘɤû˘Ԑ˼ƣęá¨Ʒ:ē',
                            'ʴΒƠΕӸɱΠĬãˑ˚äʛЯЌэЂ\x87~ƢǘҶɰoªǡɚΪǺ^',
                            'ȊģъӚƽ҇ӿ]ҭʕμĸŁʲѤ˗ĘҺ˽ΨMΰʑԉ҈ǪОɵΈɬ',
                            'Ʉλ¼ѪԢȩı\u0381\u0380ԃ˶ԟʉɒ;ОĪĸч8ԚУ\x933˳Ãǘɤǋȃ',
                            "ԊɆňƞΝĵԭ˒Ҋ~ɏǸӛȷҏȜј\u0380ɐ'ѝȊɖϦϫɪĎɣҢԒ",
                            'ЩΑԉΓʀ\x88҆ś˶˘ÁŚӂĖȽҰɍʀˠ÷ȅԙӗÙeɰΨƳȔӐ',
                            'қΆѳʴĒʩĪuɧϊɿҡђћƛǡѲƩϱiːыʃæGÂϩɤǴӨ',
                            '˘ѳиҩ˝ȽʬƩτɥÌνΰǄԊřӲįɆåШ·ӭüԑ',
                            'ԞƽӻłsŝќδҖĚģцČȇ\u0380ȪȍĴǎʥħƹ',
                        ],
                },
                {
                    'filename': 'ˡѥͽÁöĂǔԇӱƊʧǯȀʄ½Sτ9ɔȦ¯0ʪЄȿʗΑŻôѵ',
                    'message_format': 'ŦȣƢяƩΓ˕аȿɸÈlˊÇөȲӣԁΰіǐªǄϿǶşʥњӑș',
                    'categories': [
                            'ЂӒɷΏ˒ĬţȪʓ#\u0380{Ɯԇƻ\x9bʩϫûZɓ?ÓHѥʓāǴʸԛ',
                            '·î\x90ȶɄüƅϓ\u0383ƴПΈƋĥͷȳƀѮŮԤ',
                            'ӈĘŢͼʶʧÈɡйшyԄʨchԞČɺğ|\xa0˽ōœœ¡ɤɯыԡ',
                            'őyюυѹšƈϵҏҧӻɶɧȎŤΕ!ʔсɩôDήǓɹ˽ɑɪʌˠ',
                            'tϬŻǕĪЙȼ\x93лϊƹ˽ăʗ҆\x97ȑĤ5ĕԦϢΙ:ϲΌƿӥĸϲ',
                        ],
                },
                {
                    'filename': 'ϨĝɓϨåҳƱӬѬū^ɮƻǖ³DЌҦƫʷ\x8bΨϑŠĤ\u038bmɗӜ\x9c',
                    'message_format': 'ňɿѮψһșķӕʹΣ҉ԎÚőʉѣƓӋȾэїª҃гЀɾԒĆMp',
                    'categories': [
                            'Qϟ6ϜǕuɉҺϑʊҵĈλӺӞ×ԔԎƂÇ\xadğ?¸ЁǁəŽǤȐ',
                            '\x81γάԧ\\zϓԜФêӒʮͶʋɰʜƺ˲ʀƼҳӌρÚʛjӰԫT\x8e',
                            '',
                            'д\x97оȡÙϻÇҭȺȮƨԕļѕӥª˟:ƇʽƌЋҐlάȳбϸөm',
                            'Ԧ\x82ǅƢԖʆӍ}ϏʫýϰϠěЅӾ«ѵŵбԇӏԪԋҐĖʰԮàѐ',
                            'ķˊӚжȇǷCŴԘΓʪųʱԆʔ·а϶ɤκí\u0378ƱĒǏêԕѠЄг',
                            'ѓ˓ηΩКʧuϹơƋҩƃǚǈƨôĸҴďǙΜʅʰǱϽˊҿ\u0378ô\x92',
                            'ΞſŉƘȾȂ˝ǂɳĔ)Ǟѐ˙ϾԦУPĺѓåǓ҉Ӗ',
                            'EçʌΞȠuĪxѩζҷʮҊҋơҡѷȦѦя½Тǀ,ђҺǌ{\x9aF',
                            'PǕшϕčѴЋԒ˲ɀӿѭЊʸðȺ?ƾΞřʊѽƑϙȫʀԎâЎµ',
                        ],
                },
                {
                    'filename': 'ȜĈӃӅ2ϕȩюΒɜʜǒϜΔƀſϥʘӻ˭нģ˖ʹƗƱűǗǈβ',
                    'message_format': 'ʋнőԁBӖӖɢĄґϓπЖŪ:˅ҩȆəӚΡƃ˞*ðɴʠԟѢӱ',
                    'categories': [
                            'àҩƽЈɊ·\u0379ƾÿʄì˼ϞΒɹƲАƍɚĶ҃©ßӜɄϝҹԉ0Қ',
                            'lȍȐɊ}iȝԃήÄȡǩӍbԦȆ\x8cѲ\x8aӦƂ±ϦѩũǵӻʩʕӋ',
                            'bōȃ§ρ;ÍѼӬžZ*˵ӃϺ\x85Ń˳ԑ\x87ûԭϳËͺЈѿӕӞʶ',
                            'ӈԏʡξȾ*˒ƃŃӥΝӬԮԛѐϟ\xadԄӤȥùʹÊѪPϟɰñΐ',
                            'ħ\u0381ǆˡ5χUҚWʞȷӤȳɢEʟ\x90ȟШѢĶQϮĂďӧÓˮɧѼ',
                            'ŊіȸéťɯìŉȓϿϳӶͲф2ÿ˼ȏΞȟȊέɟэаőÃȲĀ˻',
                            'ǯǸľɭϹÎεϞȅû\x98һłŒхωƅґҷМҴ«˵ӘͻҭňΤȤ¥',
                            '¬ѴчϥC3ǑÁΠUҴΗɋҕǣ\x92ʟˎ˼ũĶô\u0382ϴȶ҉Ƈ3ɭ\xad',
                            'ӃӦɩ\u038b±҃ιʏƑȲɘÄÄÛäĥ˅ʜʮƚ\u038bϖǤăԦũ˽$Аɽ',
                            'ԨɄҠǂ\u0383ƏԗϠǂȪƀЂƍЁЪΫѐԧŌ\x8dēú\xa08¿Ҹ\x90ȴʷӃ',
                        ],
                },
                {
                    'filename': 'ÖƛʆƲǂөεϴԮʌѬɎ¤`Л¸©ҎǨțϓɼ\x9eж˻\x98ÄЫįƟ',
                    'message_format': 'ɀӶҫpRʦɘʯѶzϑҙŎ˝ĳåɫŒ\x92ӿԂЫԫřXЙŕ˸-ԍ',
                    'categories': [
                            'ʵΊÉˑ+ʤЫPȣјƫƥÐҙ!ǃŢ-˃ͲƩ҇ȚлˍɋĂ¯ΎǇ',
                            'i}ˎˉŏԄʊЗҕƐҲҬѹ˕ȏ®ʉɋǮͺӬĎșƐ˛ɕÎɁμʅ',
                            ' ˟Уωԧc²Ǝ\x7fɀʩǧçӳMȈğˈʝųr΅ȟȶǆӴС\\˼s',
                            'ɏȌ5ԭñűџӉөȕşȒҽϣǌќYѽϫƥȪСZŖǛʱДІˏζ',
                            'ǒѡƎǒĚӱBϔ[ŎňƸ\x9aÄѕҍ\x8fԃʩǏѰШr&˩ԫ)œЙ)',
                            'ФώýƊяȨԑƱ{ªïÂȡÕАτҷҿǅϖÕůɣΪ\x91ŋϳӮΦԧ',
                            'ĞˡŔС)ħϮƭЉѯĹМϝťĘӽȣƢªV\x81\x80ɲ\x92ˠǅӲϺԭѫ',
                            'ʯԩԆ\\Ίn\x89ĊşǱƖԡΚδ8ʭȟʐѓҐςǟ˚\xadɂʫŹƠ¢Ę',
                            'ˎ@ȝԔҟʈЭɹƃ²kѧ ʨӾƼѥεƊГɩêÙˇúЪјчÜÎ',
                            'âԦ]ʟƙlllЪԜþúȧ˲ϤΩӦ\\ƀƶȡɣё\x9dőӾδХҞË',
                        ],
                },
                {
                    'filename': '϶ͻŃЛо˺ĨԈŭɉ΄˞ʐЫБƓÞǐҭͻ©ҿƌʇҞϨ˓ѷєƕ',
                    'message_format': 'Ư#ѫЊͿʀ»ƷǼȂϒԅӗJϗƣύыʍӚƗgʘˊћϾѐоϢД',
                    'categories': [
                            'ƴ§ʠѹҠдŢЌÜӞӦ¶ȧʩӜԬɮҙɼѰЁʞғϿШɖрΑӖԐ',
                            'ǍΧБЅǺ\x8dȾȸ˧ЏʞѷˋǊǤ˗ӄŀȘŰ?ҭƴԣ\x8fJȃЂÒΩ',
                            'ƤӾҵƞÛӐƔŇǦ˅ˏǔƹʺjЫԪǑҢεӨĖ˄ɿǃƹ\x89¨ʥњ',
                            'ːxΐɤȆʯͳѬΎϪƓōрˌűϤѢɱ\x9eüϔāо¬\x9dʊĮк·Ҧ',
                            'Ԇȗƣȁƒ',
                            'ɺ҉ϦɹʑkұÀȃ\x93~ю˵ȴѷȬ<4ƗΰPƿҰҳӻϔǐҬɾЙ',
                            'ǳƄ\x86',
                            'ʘҟ@ɖŰŁʍȈΥ¹˲ӨǢѾɨŜǠƬ\u0383ɽĴÞ{ɚԭûŦԦƕĔ',
                            '˶ƦЋǉɇΚ`ŉũӿžƿnʊƥȲƢǮśАńԚłӗʆȑӞԜȧǺ',
                            'å˾Šɫ~ʔŇДǥӀπőȩƠȹ9šƳˆџͺԩ<¬śҙʠħɂŭ',
                        ],
                },
                {
                    'filename': 'õϩԒөFÊͺŁxɻйƕ¥ɕ҇ƁÝàΌГΊàŁ>ǓǜǈҠƊɍ',
                    'message_format': 'ɥÜˠͼȼRԡϕԖѾéʬҦŪҷʍҨϲҎΕӱБɡϬȱ;ģtτе',
                    'categories': [
                            'ŃѫɨłĨɛϻҋσƋŀӪуɘoBȱɥŭɾΌûûÈŻӋˌƜī',
                            'ǩǖʀѺΔȫ҃ªyЙϤԨʏ˩Ӱʡˬ\x7fѿʊwƆƙÌƩʡԂ˷ʩʣ',
                            'ǒͻ\x97ψVҙɷ\x8d¤ûǞǓчHƘƐˊҪɤ˓ıˢ>ӽ\x90ЈʙΥӏ\x88',
                            'ɐǢΫŃǮğĨҼǜӳď«ȗӂΊҎĢÆǡˌʺɵʙɍɒǓԨňĚȖ',
                            'ȝůЇЖǊơԈѾvǱıЈ\x90ψϘϙκ˃ýɴǌķƠʋӝԑȡ[íȦ',
                            'ǃ\x97ԧúԑǌťßŔҬεǜԜ\x94ЃːԑԪƲǁȊǡʇʞӇĭƃԙķǉ',
                            'Ɂ|ĕќʋӷƩԬÈƲȜĬΒǝģФȼòŔţİ˒ɔѲǰ\x8cɝĐlě',
                            'ʲ?ŦɧʧͽΏȁéǺBĥԪņĬϧʺӚӞē˸\x9eĿǶ\x86<ˡÑәы',
                            'ҕIİѼŜφ˙ǒұʨʞĶhӌό\u0383¦ĉσґƩϙѭ\x9bΞę0ǨѼӛ',
                            'ęΐξǹ»ԃ;ʯϺŰӱўӅԡʴʻЫFԢϫӦЇĐҏ¿ʢЌǵ\x80Ξ',
                        ],
                },
                {
                    'filename': 'ԂĆмϭǇŔϦр˦9¬¥\x84èφҔФŋǅҟԉϔΆʩ/ĩҔҰөϵ',
                    'message_format': 'ŵҬɺϾɏԞǑϓƮҘƉŜρʇōǝ¨ÎÖǤɏëӏӬ½˫ϴҁðD',
                    'categories': [
                            'ôEǃ',
                            '9\x82Șũǽɸ\u0381ǁԨӐҡøϝ҅˾ɴɃυBȡεΐƓ6ǝĉť[Iƙ',
                            'șç˭Зӌğ˫˶ʽǇĿ˭˟ÔƜƕĕϸņɅЙɫԄäжȶ˔ȏǢǬ',
                            '҈Ѹȗ;Ǩќɐ˭Ҏ\x97@ДθÕ\u0378ʊʋђƉ҂ńΆȡ\x97϶\x92Ԧɵǫг',
                            'ԥxʱПǑ˹ȍŒǍҝ˕ȝυ\u038bŵʴƀΡХUƣўvǟʕ/',
                            '҂ҐӦԪϪЕԑɎʴϺˆґŲѴҗбϖƽϟҗ\x89ȏŬ҂ʁιʯ\x8cŦţ',
                            'ξɽЛıɃȮȻğЫƅŔӅÔѶ˯ķȤȭȻВʎgʮΒȳϷÛ˘ϝԆ',
                            'ƍλȌпϮϺԓɞԓɝ\x92ǨϞԗϺΧķӪ',
                            'ˣ¸εú˧ǘҊɬʺӰCЕløѶΖĿȫĲɸΫҮɹɏʬƟўœҰЖ',
                            'ʡɩχԃˑ˘ǜхӄlΏŘτθϡhŋѸҚ"ǫϜÝʚɍΆçƨƂć',
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
