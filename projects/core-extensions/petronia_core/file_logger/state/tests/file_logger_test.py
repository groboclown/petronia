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
            'filename': 'jƇ6',
            'message_format': 'ʎďľåӺő,Ķҟ½70Ԉԙ˙ȤʱҴ˽VѽχąӜ\x8dƗόˊԃD',
            'categories': [
                'ʫмǡӹ\x9fԢшҬǥӈӼJøŮԓřΎǀξĞŎƝ˗ęґêIЦňҬ',
                'EöƢɑЯ#ҡΕӒȄЪӬіѝʶďÀýӁʶȺ\x98ɔͲŎÿϵҏ*\u038b',
                'Iϼβ\x91ſЁѦͰķÃÆdяuòӁ±ѭһӾāˈѦļȬԈǗɁ͵Ϫ',
                'ƱMӫѽÖˑδӦŒ˧ˀţͻ_ȻɔԮ.˻ǅҍɭɇςĆӪӨл´ʼ',
                '\x99ǏцΥ»ʭӟЀҶьǪʵĦˏǩѩԟǦϠϔƣӵЄèћΙƄ˻ŮŃ',
                'ɸÅШ˅Ò,ɿǳѨҽȹ`»ƼҲӦЬȮԆ\x89ƪϸӎÕ˶Ӣӻƺɛп',
                'Ζ˱ɃͱǛȨŷ\x97ưþʙĝǤʃŝ',
                '˺˥ʇ_=\x8bMԊKů£āΕ\x92¾ćοƖϽжѝµӮӷʶǱkԌƼҖ',
                'ɉĶ@ƬʦǴ͵ҫΙͳ\xadˌŧƓɧȳTůǜҥӫǡʲЈèԥ˒ȐÉ"',
                'ſKˈЕԀϬ˹ĿΜСȓ¶2ͺӦҋȑűβĭӃŚКҦˍЌ˚І_ʬ',
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
                    'filename': '\x90ԐҿЊƭǮǻ҇ȉћʀģ\x9aіϢƯǗ',
                    'message_format': 'ϠĽɜÁˌƦèαƺϟÖĬčƕǢ!˲ϛʃғΡƿǑ˄˭лˏӚέѹ',
                    'categories': [
                            'Òϗ8ƷMӱɦğŤˈːwɝȠ|уŶϛƃċ҃\x88ʤǬȒӲԨΜХɵ',
                            'ͲÌѿ)ęӽϨ·ϭʀΓĪѧѓќźǢȇ҉ԀöĜєʋ\u0381Ўɐɮ;ʃ',
                            'Ӆȳӊ\x84Ҧ@˪˕ѡEB˅ÞԘѺǮԋПÁω¾ƐɿʊОƚɼɲƵŖ',
                            '¨ʋԝӈщôӁȖͻmǒɇ¡ŊʑҨĹԀ\x99ԞѠȍ\x99ŬǙǭԡђʂͽ',
                            'ӊӗWҴШѯˈʮʘbТөе¼ϴˎƣҴʾpŴ',
                            'ъәǍӤњѸfȨƟf˝ȏÌȞǴϺˀʰу¨ɰbǕ\x86ʂӿѼЗɪҸ',
                            'ͷѸ,ZЪȚJÜԘdȋͿ\u0381ξ',
                            'Ʈϫʃ\x91ӛʤ˗Ż˞œɕ\x90ǍŐǂɆБͰȩпΕǘʨĕðƔ\x9eӈĥƸ',
                            'ŕÔϦʊ˅',
                            'ħɴВϮΈĭ\u038dŧöơИ¹ʿĒÜŎуɩØǙԈƊŵĘȚ^˛Н&Ű',
                        ],
                },
                {
                    'filename': 'ǧҿĐ\u0383ʖGȱѹ"Ԍ·Ҋˢ\x8cɵȬBԇ#вͱƿЎeî˜\u0382ʌˉƵ',
                    'message_format': 'ȘĪӦȀмaˣ˒jǘɽη҇ȍɗΰšĜ4yгǽϳѕĴХȬʺǿČ',
                    'categories': [
                            'ɨͲѥбϯ~ńʡǫǍǟѣĿ˩ΒϏԠҮƿíђ\x98ɂй¨ϏϿĈˤ\x92',
                            'Ȉ¬ɂȞǊϔBƜɭԘȕϞ\xa0ƜӕԆȳ·ʣľӺ_¾Ũˋ,ρɸvƮ',
                            'ȋĄԞГĤ¤ҽřǯѯʧģРШȲǿɉýӞˣ',
                            'ȑѧĒʒϗ(Ӕѻaˉҁì"ÙϿӅƋʷȞ˚ďęʲȫŪƧіȚҸ˥',
                            'ЍTӅNŰō¨ŝÛʧǕƔρȒÊϏΙŁɔĕхҭãɵҌ=ÍԄҕϵ',
                            '\x80âҡԒńΥŽŬƵ\x92űʫʯχԘȏÉŁȠ҅Ȁʚњ҂в7ӐѢЬб',
                            'шǈϷǣӓʺ\x8bæΓҕЩӿ%ÙĽǴЙѭσ5ДԖЯʮƀɫԪʣӾ\x85',
                            'ɶǵʵß2ȄԇԮԄӲ\x9bģȶɵQΚ\xa0үӈĹ.ƳoΙϫŧS˄Ŕϣ',
                            'ϲǨԨӊŰȊϰŁƉǎΓˣÂŸʊˀĜͶҪŗǣǾ=ҽŠïλϤυ\x98',
                            'ƩβрӹюҤ\x80ћ\x9dϖѷɌӀЌˏǩ˩șæĽ3ͽӎАɼѹѰɋ×Ÿ',
                        ],
                },
                {
                    'filename': 'ԗțÿ\x94ҪlŕҤɿγϨˮЭƮʙ/ɡυМϖˮƠ;ʑ˹ŽÖĂųλ',
                    'message_format': 'ЉÝřAĴԀǗƢəȦʬԌЙ¤ƇʚǶҘԓǣóˢӐ],уΧʿ?Ԕ',
                    'categories': [
                            '\x9aX\x97ĲψІ',
                            'èԬßƬЊԬΛʒÀò˚ĕςʦιŪ\u0382ӇѬЭԌЎ¹ŜöʲϓϜԒь',
                            'RӢŰхιΏԕЎǮҿΎӇ\x9aƷ÷ŚƌŌхÐΫIҋɺƁnŃ\x9cęʚ',
                            "ǊSӯэȗǳεиǽǍʲjҒͿѻʶөњѢaÁǦ˨Ȍϭ'ʤŶə˾",
                            'ƛϾ\x93ůͻĨºǒЭ`ìөӷЀҴʀӫa',
                            'ѓ˷тśτЉΟЫłƆºȭɫЧǷǩ\u038dǁщҢцԒˡєϋγƐˇ;ɹ',
                            'ѼЖэѽ˪ǂӻVN?șԕǁNВФʜӤӊѧ)ΟцŅʚxûԥʈÓ',
                            'ϵ΅˫ýӳԅ˺сҨʕDǈŹƥͿʫĄН˶ԈΆ}ȆчѣЎɝЦŦӨ',
                            'ͲƑ¦ӱӆҽùÍɾ',
                            'δßƎȺűƣĢūόƹӁԨŲƲʦĠtʌХƪŉ9ӡĩѭʛϧžƬ\u038b',
                        ],
                },
                {
                    'filename': 'ĹXоқТԢƮΨһϨҔʊjљ΅Tƫĺ^ԉǀʄ҆®зŋͽ[ΙĬ',
                    'message_format': 'ˡ¤¢\x86ŪOžЇȪȚЄ£Ʉ¹áȧʼѬӄK¥\x9fʶЊψ¢B8öѷ',
                    'categories': [
                            'µï˧ӺʼԐʼˣӱФϸƷAãόņΟͲӢ>ʟēс\x8bƪрȲĮϰ¡',
                            'u ћΰБӠΤzϻ%üĳˍ\u0379˚цԭǶν҈ѦɟԮƼ^ǷƷ\x81ʍҷ',
                            '\u0379ȠЫҬʬňӒSŗˁҬѲÂǍÃȭǜƝǠа\x91ƪwƝȜŶ˭ѺԧÀ',
                            'іέƲŴŉʘӕɦʕѡΎӎĩФ˸eɦɚƎǲœɤ¹ѹȖøԋâɄʚ',
                            'ƍbԇѨĹΈԌķɋǼČөǲүѬ΅µǨˢhȏʍɔϐҨ3ӠӮҝο',
                            'ǮĎĢԫӆ©ρ˷ƧҷȯȏдзҎÙџχηɣѷƮΥ8ʓɏŌɜώϾ',
                            'ŏύʷ%ÑҊúʇ$Ʃ\x9dǁCvǬѨɎ˥аӝƓ4ȗǮқʏÃdɚř',
                            '\x96ͳǿƿ˹ӘőҶʦΧѕȦӊмȚȃƘ',
                            'ǌԋʫҔȿŰǶɇnºΈψҖԋ\x8bЈǭλʬ¼\xadȐԃшȰǋ\x7fԄҶǉ',
                            'ɲҦżΒʘϤτŒɄǢњ3зƥϤ\x82QXaҧƻοѷѱДҁˇѯԥ¿',
                        ],
                },
                {
                    'filename': 'ǣԔӲţҿОÁɋ¨ѭѷӼԏЎǒʍоϓ˱κȦÝˣж8˷ӞúǮɍ',
                    'message_format': 'ńƪβƐõҸłʒȧǎŊцү;Ѻ҅įĩ"΅ȩâѬϟϬʀ϶ҳěЁ',
                    'categories': [
                            'Ј\x9fҦδɅѡґǃөӕάΫǎŤű{±Ӈɕ˶˅ȌѕgƓɥʦϯԙɤ',
                            '{ЬԃƉNɏŦ˙ϛ҇IƢǓΓKƌȀȗр\u0378˖ϬɧƁѱ\x9eÜ\xa0ʊĕ',
                            'øġλȷ!҂ΖǔѧƿΌÛͻÓȹӖà\u0380ħҢáħǴā˹ɭӘǭȇԑ',
                            '\xa0ɨǫr"ΈԕϦХφʣ&ӛq\x85иǌɺŗφQ¯ϝԧ҆Ƿԍ.ӿ϶',
                            'į\u0381ʈÁª',
                            'OĠͺђЫ\x9cЩɘťԮŉ',
                            'ÒŐÃèэˎˠƽƦOөҟΠҐ\x81ŗȸɚǺy·ę\x86θҀ;ǘʂӸƽ',
                            'ɲǯЪĐˮǢχЕЂǃ;\x85çƘɉǮxșq¸ŸѧЙНТўќLɡɒ',
                            'ǗƘȮÕ˞ԧȲľЊkœԐĉԬȩРˢɀ\u0378ƻќ͵ˌƵHȑԎùԚ*',
                            'ѽaϲͶԦŖͳҺφӒӇі¥ԬþУҥȞȽΜԟҨšӭ˚ӰʰtГҰ',
                        ],
                },
                {
                    'filename': '\x90ÅԔ¬ǆ˪!ȬƵҲ\x86ϑςБӫYiѠ¯Ͻ=ƷɔоЏăӅʖƂѮ',
                    'message_format': 'ҿȺɫιś˓ԦβȸǷf:\x8dĂҫsӧɤĆľȐʎЊԮЯz[ӯďɿ',
                    'categories': [
                            'Ӫ˫ϝǷˠӢӪʀѷΙ¸\x9fͺԔтҞӫ\x8dĮʔϥ3Ǧʮ~kê4\xadӤ',
                            'Ǔʸԁ\x8dèȵĜ\x8fҝúFӎĿ˭ȏϼŽŀýǃʢѴ\x9dΘѡā$ѸнÝ',
                            '˦ĻχӒ\u0379ΏӃӫț/νˑ.ɘϥР´ͺЬӾ\x84ˠχQĊƮрƴԅ͵',
                            'ξ˜',
                            'ĝɝҟʢʨұϙͿвπŠ¤ƻŗȤЃʨ\x90Ǣňũď?ёξϤԧԬӝɩ',
                            'Β\x84˝˛ȧćӟæďďŸоӺúϱ΄ЏɎљ\x93ξӽĚ%ЫˌŖKšɜ',
                            "ġ˾ʃëˉÀƙφƦċÓʂCΖåõĝ'ʀ^ǄӏŞƤϙŬǔ~Ƥт",
                            'ƙˌśǈτċ˨ԬÕʇǐŵÞʫʰLԜ \x91дԪҶ\x9eӿȩΐӟːо\x92',
                            'ŉȤԏ;фɞԫΝ\x85ĩΎӣϳŦĠ{ɯ+ϑȾϩțϤѠȬҴĩĺɮԀ',
                            'hϖŨғƌʬӮӥʃԓʱӓӯǵѦȅXɾѳɥǧџͲпʹɁѤȭŰ˨',
                        ],
                },
                {
                    'filename': 'ԓӈ#ƪ\x82ҘϬå\u038dņȖÉ\u038dǳўԌʀδӏѹ\x80ɀÖ$ǲ\x86ƠŤЬ·',
                    'message_format': 'ӂόtƐ;ÔÓѽǒãÍĮ*Œ;ϽһʁȰ]IʂʐɃɈŔŕǬɉӈ',
                    'categories': [
                            'ЪËўȵϋŃвΘӒŮԗğϟŌ¾·ǻάǦњìĖŋ\x80͵ȮϺȚAý',
                            '',
                            'ʲұʨ9ơϧԌʜ\x95˲\x9aҰŢѽөȚ҆˔ӻѫĚȥȤʢ\u0380ŪìɪӯϪ',
                            'ňӥŷƑȷˇ˸ǸDˇ\x7fÜʕ¾Ɍ9ˉѸԄZȷӏə˴Ƶ\x97qһρӢ',
                            'ϕÆ˷"˓ƌȅӮƭѕњǳчƌ´ƶϦČмѝӶƦŃѕħԢƩϴOʷ',
                            'ӼΌӴéʢùêЬΰȄŌďéӬœĹҬǸ½ŏ˙ˎɹшԥ\x96¹/ͺ\u0381',
                            'Ǯ˷Ҙ¶ʑʱҶbʳǋԏĹUΧƛŚɮʵ¦ϥѰȅoȑѾϹɚѼϨǏ',
                            'ԘɔȦѬǛ\x9cӕȌǼ˺ƓɖҋЯĚ\u0379ӌϭ҉˥AʖſɫǑȓĘƛJZ',
                            'ϙ*ѻŜūƈͻŚчÐСПɀԒЙʊƼȗǨåаœ˼λœҤͽϕƊŠ',
                            'ˢ˛[ĩ˪4ǮǋԐĪÉ6ÞϋԜíҕĐŭԅ\x9fÁ\x94ЈʰϽϖ',
                        ],
                },
                {
                    'filename': 'ʽӖ˧$ӃėҤĦОήϰѺŝґЌʽĒĮʋöӔƾŚφѼÁӅÌǫ҆',
                    'message_format': 'ϬǳθĊϏ\x95оϺƉΪ\x89Đӕº:Ɠ0˔Ӱɨ+ȨȔәÕωВ¯źе',
                    'categories': [
                            'ećцþ\x98Ș˸ˋ»ԧ\x9e˖ʁҬàгҬϪŝȖЦÃő®ӒЭǺ˞ƅ',
                            'ћШʝ˽ΥKмŮǅĉԫЃǞȃƚӭçӂŒь8ЙÈ˽@Мǳ˥Ȭþ',
                            '϶ĴӌƓςɱʷʐϵҿrƝʹɯԇįγķɿĶʒ¿ԅHÃÜ~ҴӽϨ',
                            'ђ¥\x9cӄ\x80ϰ2ưԛѲЩԊӽ¹Ğŝѿëq¾ϻѺôˢA˼üϓƉϑ',
                            'Ñ\x89ˇ×ˀ¾Ӫ\x96ǵΡSԣȓȽÛɠϣĮ0ƂĹ˗ѹȜŉӴÂɱϼд',
                            'ϦȰԪƹoӚ1Ȱԇò¶ҏҳ=љӽ¢λǬĝҜ\xa0ҾЍʗɒZԤǼǻ',
                        ],
                },
                {
                    'filename': 'ͲӆqΠѵʭĉ³Ƀɠſј\x93ǵ¥ǪǲƱǇɈɲʏϖĚ\x8aвŀÆΘͻ',
                    'message_format': '\x80еϴҜȩɏӾçƏIїӻўq\x98ϮʮèIʑ҇ɘӎ\x8dʋ¨ǵÛѻ\x7f',
                    'categories': [
                            'ҨĹǩŵċ¸ϪԧȩěӹіQñƣƈơЛåʈŉĳӪɵŦЛˌũɍʹ',
                            'ΡΨĴϺΙȆҭʞӓ\x84˞ӌ˴§ʣǧѠȕӛ\x84ǖİʘȚɯӯ\u0382ƸΔҀ',
                            'Ƀ˄ГӷԜ˸ǇÕ~%ŪКƱҏŵȑΌ҃ҤԎȿϠëψ)}ѩȠԧŀ',
                            '˫ŚòŁ5ϙ\x8dƒЁĎϪӴЉЧӻʠ˱ǖŤɹ%ϬíϠʇбҙƜƀУ',
                            'NgιҋǎˤǸɖӋŢ˨(řʔ\u0378ċϗʈ˛ȞÑѺfƜԆɼѰͳĕӊ',
                            "ǩȏͶë'üҦ˵űҔЫńƝʄƻ©Ѓ÷lԖxςУ\x84ԒCϬˮѢ\x9e",
                            'Ѵԩ˞ѻƨÖȵȁŋԎRʂӌԚԀ\x9bζǚ`͵ƽÀˑдʍț(ˍΣÝ',
                            'ξҼȻðƟŌ˟ȜơύҥѽљȳɘǲȏâӅØ\x9dǐȄҷþʲͳ҂ˀΣ',
                            '˂ѕĎӾɒƞ\x8cЭɨɰжƱòΟȹωѿмșƋ¹hҡӯҁȪδlӆæ',
                            'ԍԈʺӪƾԪ\x80ɛȚķԭŻ¦ʙƷ\u0381˚˳ƛˁȇļӖƫ˗ѦĖУѦ\x97',
                        ],
                },
                {
                    'filename': '*ėʦc%кҶѶԩʗїȨԉƧ˞ϣѕɝ;ʆɶоҫƤӦ\u038dѝpŧŵ',
                    'message_format': 'ƄɟϷʑɩҗʓƁŔӲѠšѩƇҌĕε\x80ğηӒşϽԙӰ˟ӖƖӈ˥',
                    'categories': [
                            'ǝԋ\u0382ˍзśǳ˙ėƅæőҴ¤ʗЖŁʹɠɆџǲѿĪϝ\x807Æɐ\u0381',
                            'ʆĈȤ\u0382ňӀdďМҏьϞӅĄ˂Ȧƈҕƅñǧǀ±Ӵ\x95ǂҲǃƞÄ',
                            'Ŕҕ˭ȫ4ԂƩĒMϘӊļ\x9cǡZɒŋɑőĔҎ¤ơɃЯ\x9dҾҿѨʘ',
                            'џҮ¦ōǔþşĬƐϩϑ/ԇɺύңͷǱøďƹ˓ɄʩáүɎȟӉѝ',
                            'ЈǓωɳÞźцξŤʾēЊļҭмǁºçӒȫäӭЍ¥vӂȪȺeї',
                            'ϡȦȠϴπˆȀϺδƃԗʹÊƿԈԔʌÜЕJŌĪʮťɋ\x97ҷǎȜ΅',
                            '4ɶʽѷøϛҪȴ)ҁǖŏÖЙїěȎĽͼіΉПŝǇ˯ԒЫʀ\u038bї',
                            'Šϥüӄ˟ʪ',
                            '',
                            'Ö\x82ʡǘĚÅȇȅAŃʒǇ˾ȎԥǬ',
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
