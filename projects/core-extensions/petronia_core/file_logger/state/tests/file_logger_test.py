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
            'filename': 'ȗƢбˁǶȵʗʲҞɎHíĚԪ˦ΠʽʵŁʳ¾Ѭxɖ˵ŌɌδȯɮ',
            'message_format': 'ԬѺЂǬӹɈɬHëӮ˅iŁʣҒ\x80ɰѐУ˧Ӹ˨śΞćǝԙȝ>ӣ',
            'categories': [
                'Ӄҩγû\x8bơϿĴʌşξι˳Ӿ˞ˡ¼ĀҷxƗΙ˦ȧ\x8fƨȧӚσȺ',
                'öČˠӌɋɏЫ҆Юˢƈʹ4ʹŶƐǊοҌҙӋп}9ɢώʤˎԣӡ',
                'ȵӬʰɸ˥ĔñӪҵʺͳӞѰÒĹǶĹɂ»ҹϫћǑԀƈʸǄ\x94˓ӑ',
                'ӉɢǠӈɻțμ\u0383ӣϸƫӥȅѩȗŨσĸ\u03a2uԧ\x8e',
                '7ϐεҞVȓөͱ\x9aϱǐэΤŌΝͺ;ɨѪȴƾÿŀ˝oɤ\x88Ķdʏ',
                'ʙȻȕȝ\u0381сʜιˌǞƢʃÀ˙ɢ\x9cȆϾӈϗȩÐњПȠŪΊӳˊΣ',
                '.ѽͻԪņşȢѸ\x8eӧʹŘΙȣ\x80ȔԜ҉\x9f[ѲȸЅ\x88Џ˴?ΦŊʂ',
                'Ŷȼχ҂ԞɍӋЩŉʈ\x9aņҷЅЉƥɊ˟üŏ˱Ӯӆ¤ɨєЌʉȋΓ',
                'ɟġπϵĊКaƨѾĂӠԫΕʚʔΐΐőԙнɣȘ)-ëΨǭȥŏ~',
                'ҕǣѷњžҗǲȲԁҳѮԬʫɌ\x80ȨěΉɴƜƹГqң±ǅӠ\x97ѷʻ',
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
                    'filename': '¸˛ӚǽƻΗĚ`҅Ԇ[ϕsĴȫ9˃д˲\x87BĒΜ\xa0ʪǛќƗχʸ',
                    'message_format': 'ϫԮӍȅţĚ˼Їѧ5Ԓ',
                    'categories': [
                            "ʚԮέˡнŉKŭψǐҽӈ˳ӯю;\u038dΚƋčԪҲЌ]ɝѾ'ʅʬȗ",
                            'ȼȼζȨ˹ˌҪɳƇȹbȏƊǱӬÇϷҫ\x92ĄrıxЦʮżͳß˄ˈ',
                            'ӯªӛʞӣ˴ιũ¡\x82қҝѻУѪεӿʱǪϓȸƼkɔѝíKΚ_ʲ',
                            'ӜÓаȢԪѧϗ(ԎɒųԈ.ѩ˃ŲɡǯÃ8ĉ*2ÝŲλ˸+ЉӪ',
                            '˓°\x8dÓԌҠЁԃSƟӏf$ǏŏѴήĪ˰ԄȷѿО\x85ҲeЬǇ¦ϣ',
                            'ӂñ!ɀΏІϗĹǅƩɰ²ԜƅɞέRӷʿ',
                            'ҖԂтźŮ˻ýҊ\x84ϔÌˌ҃\\Ц\x9bТ˩çғƋɹȵπǋͲʻĢʮϷ',
                            'ʤϰǜɍƉ\x94ǮŅмӲɋϿǼўʠҔsņ0\x8bωyˎЖ³я˓5ѠӢ',
                            'ɇʊǙƹКƆǰʍǚħXԑəѪù˺ȔΕӓЗԥȥʕӰБĂҨŉ˲Ú',
                            'ҖȝǚЎʾѵ˘FöΥМǉ΄˫ŒǮcˣœΝА΅é·ɬǗůοǄĨ',
                        ],
                },
                {
                    'filename': 'ԩţˇʛɜ˟ɋӧ\x90ӓ\x86qʴӟ҃Ǘî˫ҭʢєΌʋѧ_cʨņ',
                    'message_format': 'ƎΙԄǌπ˚ǂӘμҺӻ?Ķ\u0382ȕӷʗʊƻõɌɍϲԍԬ¤Ǖԑėë',
                    'categories': [
                            '\xa0ҁϫgƢФȘХęĴԚ]Ŕс}Ǎťнϼϐw/Χơ:˧ʓǻƷƟ',
                            'ěœυĥЯƈȡҵʞǨσς\x97ȏţΦï\u0382\x86Ìԁé˼сIƕƞҒɒԧ',
                            'ЫȿяӼƗˊƾÏˣҟѫʖҞʙ]πȑ-υ',
                            'Ì~ǯƤſaѷȦƑɡqƟɛԎ˥Ē\u0379rɜƖHɢɫįð_ƴÙÁӺ',
                            'ŷǉϫƮԍǙĈ\x94ϛѼєǄлҌ˯ƛɄĬǡĩūϤ\xadȬəӧùɔĢÂ',
                            'z',
                            'ˁќЬҟϢÊʇǦ˖ӍͺБƲMǳʙҮΤЍiҫˣŴδȇҶϜНȰѿ',
                            'ѴWѳ\x8bțÙԝ_Ũ˔ɫӲɝƎɱѐѦϕ˵Ȯǩ҇ӭßҖϲ˦P˞',
                            'ȉʣķʄǆɳ˨ҝɃrǐŎЊƑCȟ˴}Ь²·ЌхͺΞ˭Ƅɹ͵¾',
                            'ԕɂEҨ©ч˄ЎsΞ#ЃwєΡǏĀǾsЦ˭CɩċīǩѨǆɰԋ',
                        ],
                },
                {
                    'filename': 'їΰҳӤкΑƤȿʻ§ёPƼʱѪϝԄϜҴТȁŖ˃3ǏMMӒӧԓ',
                    'message_format': 'εԫԆǍǡǻƹнɤΦҌǆΊǆɑȯϸтƢʆ9Jԓŵ˴ʣ,EӨԌ',
                    'categories': [
                            'ɨӚīǼ.ǜʲƤǽЦ\x90ĉíɹϡϕƬѽЇeӧɠƑȃЫ҃βЮѳĥ',
                            'ԣԩǖp¼яćÝϰѨĠȾǔȧϿȆƨʹЩ{Ùǚʱшı½ӹѥсʵ',
                            'ѡԜȺʧÕ2\xa0ɡϙҤċɠɸ\x98ƵǑҘƦ\u03a2ĵњƻԭ;ŗÃЎ\u0383Їɝ',
                            'ɧιɾ\u0381RȿϣȼĜ͵ѓҵʻіłρϹɝ{ȤǗѷʧɀӽȨâ˯ǽɜ',
                            'ëέɵӹ͵¤âȽĬȿѯϮʀǒҤѹʊŦ˚ԪԈɱːȅʳЉԙр®Ġ',
                            'ƙǦˉԓ\x9dıĬΚѾӌҁ"ß˃ԩ×άːҹϑʲӠƢŎϡõţĝBŒ',
                        ],
                },
                {
                    'filename': 'ųӨӬ\x87ϬЍǐх˱ȥм/\x9cǼ«҉Ǖѻăɛǥҥȕ¥DóʙѣЃ ',
                    'message_format': 'ƃȰК˴Пϝƈ˧ϩÒzԂɹŢşǛ˵ИƳåƚКǏĲuϗФʎh',
                    'categories': [
                            "BǦŏӭӓƝŃϟғϘ˶ªʏӢ§ҷ;ɤYȎʻȐЮԙʩѡʜ¹ɽ'",
                            'ʹ*хφ&`ǭƈʇˢɨΤғȠīǋӍʼӑ\x9aҋфшˠɌцҔoϓǦ',
                            'ˏ˝ҕħԡ²ψТʅŰģǏW52ȱԑАѺ×ʶàхҵϖ˴¹ĢG\u038d',
                            'ĤŸźϥÐԭɃС¿ɟϫ¨пѺϑҍ<үţѓ\u0378˫ńŲʍȯʜǖԞź',
                            'ϛvɛόеţъ"ВŃ˗zÏdǆʚȾοԐȏƁ\x8cҭ˝ǭȯ¶9ɶԘ',
                            'ϻԓѣӇӠźčχˍDŠŔΛßţΞ»ӪҲЊô^ЬΆǪũҕgůʙ',
                            'Ǭu*ӄζĠԮʬΊaԚóǌ҂Β~ԗεWƢǤʧΈӔŻ˞ԩǆ\x9eË',
                            'ęŞΝͿȏƠЭɮʯǶΕԤǌʠŅȪϺũǤǥEśҺҾɻýˆϐɀŁ',
                            "ԔϣơǴǞΒƷ'ѝʑSϿ\u03a2đĲЮſЎĴßiΧϵƄùȑȅɍΩƘ",
                            'ӔÕ\xadΞà\x80˥ϠҌɾŀ×èӕȍЁѬИɅϹ*ˌ˨ǂӥƜɊƑȮɞ',
                        ],
                },
                {
                    'filename': 'ŠӇ϶Ϲ\x9fŶȷϵ',
                    'message_format': "ˤȔ+ϣϟˀӨ˅ЖіҠϨ\x96ƫʬѓǣ'ɭȺ\x9eŦ?KʾϟАǊт¨",
                    'categories': [
                            '\x98źʗӟϨġ©2ɦnƖƂčȢ®ȳÍƌȒДĂiõԏԂʻŘǒӼƃ',
                            '©ΣJ˨\x98ˏ¥əȕҫɖȱϞÖƅζξΰÖ<Ǜ˖ɨĠцЖїǔâǐ',
                            'ŕ\xad˄ɊˈϨ͵\u0379ˀΡúϿӺ¯ņр\x9fĞůҁǶхŪΏмʟ\x9b\x90зҖ',
                            'ʂǤѽ@ӫúԤɖƮéVǨėıҮǯ\x89ę',
                            'КЬѲϡɰȊȯҟǨâoɮmҍĨȅӺӛҧíǮԀʭϗɑțͽȮŀύ',
                            '˾ƾÊҊпΈȬƻȊǱώϭЋ˛ŁɎƲȋӌãӹʗΓɁЪ«ȜȱχȦ',
                            'Ɩ\x82ȨʋӟӷіЅ\u038bѨǠʵ2ɥƏкӰҭԔſΓѰɩˁȃҧȉ£ӔЂ',
                            'Ǧɉʸ˕ѶѼ\u0378ʇӕҒɦƞȏǽǝʤĠóǲʇ8з˷C{ԭǀΨΙò',
                            'М˧ѬʯϮɺӎӐă6ғԈӭƱ˩\x80ѮЦ\x89țɌԉʣǉҡ\x8bғØҍǍ',
                            'üѭĵ\x87ҦŗΡͲ\x9cÕá˓ĈĀȘΜǮƜȬďȂхǮēƧ',
                        ],
                },
                {
                    'filename': 'Ԋ¹ɱ;ˢąЫΟÎɆɗȝԂԐЍģӼƔѾį¯Ɇ(oʫƺɊvĖƴ',
                    'message_format': 'ϢW˗¡ƩĄԒҁбԎԡϤŘàԨҭȮҮ\x9fґˀêǒǁVȳпˌЧĤ',
                    'categories': [
                            'ǁқҧȤɜҜĔǜϫαūLwΌǳˮԜŇǈēϬʨĘȃźИƋF©ϡ',
                            'ȕɨʨ΄ӜōԜŔƶҿӛy*EӱǼ˻шĢɓVÃώˈʢƘʋĢȺ˰',
                            'ΎĵΨȑǠ˅ҬǒЛ{ʯȭŀϊʥƱʣβԣSǡcҕ;ѼȞǗșϮñ',
                            'ϲTτȈѱέӞȡ϶ӵ¹áҩϑÄʾǭɂлǿˬԗɐЛҘƯҋÅɢƈ',
                            'ԘәɞӱƨĬа¹J½Ӯ\x80ȣ˪ɏɗŏӯĽԗѦԅǗҲ×ґԔTˎѓ',
                            'єôӿͶщZȼȺͳðюӶ^ӰɎãНԀΠҿЩУÏԩɬȉԈƕȱ9',
                            'Ъ.w˄ԟшʤӗҊëōʶȐӈ-ˣʉʭΎŜIβ˜ѦƱτŅОʫ˶',
                            'Z<yȠԑɕ÷ė2\x99ǎˤɪƤīŻ\x82\x99ϕ:Aűƣ\u0383«ɻѤӃÇÛ',
                            'ʻӃԁßϒӺʧ΅Ѱ˩ȀԮǯW˯ͻƔǕˀӖƭŇӣϘ\x94ƲǇϧpѝ',
                            'сӷÉʈ\x8dÝҍǚĎˊôʓĶǾƴǙ\x98/ͰҚÁƟɎЩȩɀʨɵԎʊ',
                        ],
                },
                {
                    'filename': 'ёɿ0˗ƥҫΡαԡ˧ѴͰĦ',
                    'message_format': 'xΩΗЉǏϢѴӲΰ±ɤоǣìҼϙȺʛΓ͵ʙȩ²ŵǵύ.ǖ',
                    'categories': [
                            'čԚƚӱBM˼öǲƧҽȉΜɊӀȂ˪ѝƏϧȶŖ«ŝˤ˻ɨÆҎ\x9f',
                            'ǤŚȪʙó0ǏԟеȰŕtǀϿԖóɒӃXȘǜÒȜǚÜƈćΨǿ˘',
                            'ΨÆϨHȺΏΫӸPĕ½ţо$ƃʄYϖЫγдДɩψ\u0381дŋ¶7ĵ',
                            'ƲƓgʧÐ¡ӛԟѿɔŰcԦО£żɌőÏӲȣЍƎʑνυȻӮш«',
                            'ɒ',
                            '\x8es±ʸӠ˵ɨńɻƽсηͺųΛ6АǤƨҌϾԅЈϸħћѕ.ƃŶ',
                            'ӛԩӂԉϱшŦл¸ȎΓ\x9eIĺЈˆÐΟˌϊә˒˫ӸŪԉы',
                            'eƨë\x85ʁҒː\x8bυɑϼжȲ\u038bÕɸwЏɝӑηўˡ\xadξķ˫Ǘˎʷ',
                            '˺˹˽ćʇǿôӸ\xa0κɕēƬü',
                            'ɘÍєАβ˻¡Ȍӄ\x9eПԥŝ˨`ȻӛȫѩĶTҀÛϺȌģτÀĈҽ',
                        ],
                },
                {
                    'filename': '8ʕ\x91άǣ\u038bŚӾ˳ǿϿMūùşFЛҥȵǟ\x9dϩǹʚWРΠɣԟʀ',
                    'message_format': 'ɗžǮĊӖЌʚʶɏȮԍӥȕѾ˲Åć˛ȿZҘŰ\x81ҩҢǊέϠʼΡ',
                    'categories': [
                            '˟ɼƌнȝЊϜwҏҁƚàΰçŹ\x91\x8fϛУӣlLϘʙʚоʯ˨īū',
                            'ӸjǗμ\x95<ƩɔĜ£\x84ΚӂуӦϓʌıэAȀ[˺ƫ_ŶbŶʅӑ',
                            'Ҩķ=˦ɽ¹˝ЯԈɄ1ǽźCԚʺ҇ʡϥʮӡ\x94ůɏ¹ĉȓ˺ƈЛ',
                            'ȝǃǿʿşǥсĲϛԦ[ԄҀЖʜԪԦÛƓŲːĻ¾Ňï˨!ϘϜφ',
                            'Ӱҩ"ҩ˪ϘȶԒњÂɋʰ«PЊȍɹ¥ƉС§ƅ\\ǥғγУʽƪŻ',
                            'ƜӆϘɛĳ˱¤ЎʾŐҹǼʮǱѲ!ˀӶȭìſŎΧӘδ\x9eΗɜ˻Ǔ',
                            'ĖτҬӗјӬ\x87˩ȿӷŞʕǜƆˤ҃Ŧç\x9e˅҇Ʉ˒S\u0383ҟԫ©Þҽ',
                            'ǽƩӱǙԙȐǒ2ʁŢÊ9iɷ$ˤŪǷ\x89Þ\u0383¥ĽƫΓ·ԋлκα',
                            'ƑYƯ\x8cȽťӸśƤ˯ ҠȵŁ¬ǛÓ\x98ψӒƧˬҘ\x94ÖƒъҡΛ˳',
                            'ͻӮә(ÏπWȫҌĶΖѴА>5ϵȏԆǕǳ¯ŮӾђõġγ΅Э\u0379',
                        ],
                },
                {
                    'filename': 'ýˍ҅Ȓ?\x8dΞʷʘĜʃτʭʡӭԙҵɏǤҮũϨ˻Ǆɤ°ϭɵёƮ',
                    'message_format': 'Ĕɝ\u0383ʽԠӀϗĦϦ©Ϡ˹Ҋ˕лѹрØƦpēȆÐĽԅѦǊыǿι',
                    'categories': [
                            "ŎрԧčǪ҇Ϻú\x84ǑňŪԁ\x90ӠаӋ'Ƨ\x91őќĵȗƂóƚȯіɆ",
                            'чϽҴǏ\x96ƊәԘҧҙǐ÷ϬǺƷŶÞнЊћҙӬч±Ïɔīʁзχ',
                            'ϭŃӞeưnЛǈ˹ƱӿіɟxԕηКЮηӢÓľҽ¤ϖʠёČ\x87Σ',
                            'ɚŷǀдϡɰҎùEʳӨAц£χ˜φф\x9f˅өРʮҢʳÀΘǧŀ÷',
                            'ѷӺȺ\x95ʴͺǊԩʼëȤɅԤĚųԌλƔɐ_ƏЄǔ^ȣ\x8cŒƐεʐ',
                            'ʘe\x8fίОЮҀųȸƱŷfmBÚϖԕΗƃ\u0381ˉ˲ɹŶƀϓώΝÊΜ',
                            '',
                            'ʻҏ¥˗oǧ-ʙнɨgЈϙAßԠǫЗϷ҂Āϙ\x91ӜƺtˡеǮǙ',
                            'ŮԫξеѮĈNщ˨ɑѳӪҔМΞҬ#ҚɬΔıģʌ\x8f˚ƽϚϊǗφ',
                            'иɆ˻˯ǓǛӨӥΜĩѤǅҜ\x8dхȤǟғƶ\\ȬƙԪcȯļ<˸`Ř',
                        ],
                },
                {
                    'filename': 'ѯʳǄΌźǹȖȨѐѾɵıaÃɍѕјԓԙiϻǎǉʽʪʮ\x85ҀŔĀ',
                    'message_format': 'ҕǹҺŪшdȁȞ½ϻҶHŕǚŌƔÌȎl{ΧǓo¸КÈVҼïē',
                    'categories': [
                            "ʄѤӞ#ǩɈǿʲȏԘşɅ`ZK\u0382sԬ!Θҙʭȕ'ǶɩννǂQ",
                            '-ÜŉĘ.ĲҗǯʻҌƾҖûARƶΤMΪΏҚÎԔȮʁҚйжǾƮ',
                            'ǼтAdӿƴɪ+ǳɮԏ\x9fûŚ϶ÞȠ\x8dȴ\u0379ͺ\u0380«ɨµВɕ7Ĝ&',
                            "ΕɳÝʒåǾʳԪƁŅEѓʍ°Ȳ˼ԓњЙ×ʟæ˖Ǔ'ŋ«˶ŮÉ",
                            'ªɍЬéƽNԃЧȭ҄ ѩˣѯԘŦԛŇǗӹ˜϶ðёĀ¹FƐϜŧ',
                            'ĹïҁŭnPȄӨǈȨԩϾxɌ˻ŰƒǫҝEϗԒӳȤ$Ǭ÷Ȓ˲Ĉ',
                            '÷ǁҦƈҹЧѨ˸ǩ?CªЊͲκźȈӅѐxҎƶ=ĔәņτЙ\u0381Ǝ',
                            'ϿʰӰҧʼŰGѬȣĞ¦VƌжŬʓƩʣǝ\x7fýԑӨȠ6\x82ЪҮΩҶ',
                            'ԭ¬+Ǎ\'ɧbŜσӯkʏԔѬ¨œǦ"{ѴӨȵƒ¯Ѧƙë҄υД',
                            'ʏʎ§ɼΖ϶ҮɔɃҕǁʥΨƂ\u0378×ƁɑǋǖɰjɈŪɍPÓӾӆŠ',
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
