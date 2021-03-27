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
            'filename': 'Ɇ˾`@ϬɵΌ˟ѓɉħP˲ÄǱĦͳεtșєώϝ\u0379ԋĨ}ΨDȮ',
            'message_format': 'Г͵ͼϜԎϓÐqѳ·ϧ˛ʦИ©ԗŬýίĸϵ{ȨɽʭўʶӾα\x86',
            'categories': [
                'ԠϵǍ:ΎĮϷжʠІĜѵ',
                'ҜГŘIнЗ˜ǴȁξԬӜɣÆjϗƮǼ҃ѓŔʕϺ2ȶͿѯа˫\x98',
                'ϢʃУԦáŊƧЁЌŴ˫ˈÙƇ˄,ΘöȄį˞ЈƿŻмӛˤΤϺŶ',
                'ɬԌʃɤѠpΝOσ҉Ұϭ˼ϳŬЈѬ½ÖìɓˁͽԄϟˌʹ*ƞƊ',
                'ǈŧюŇʊˎǉҐΧФȉԋқǲĤpϟǞƆťʥɸӂΐђԞǸȗԂԬ',
                'nʬӰŢҎǏʷȵǼѧˆ¨åŭ\xadǄǃƝʃыҳǷȆӟȺ\u0379ǙB',
                'ȂÑð1οѽXçʴғЊϭɥDˡ\x82ёЖ\x93ԓşƐ\x8fŭũˋѧӜnҏ',
                'ĕĄ÷ɑӊϒɃßцLŏJƙǈϷŭĸȓѓ!ȠȣЂ6ĀғõİUȴ',
                'ɦӓÒбɠͳŚϠХÐʤ;˅\x9fɛƧʨ3ӁёҏӬũµҽҬȔѲŤД',
                'ǸƙѓӐǴʌ^ѤfëΈȅĤ',
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
                    'filename': 'ȱˎϱґˁȿѕ?ěëʍϷ˖ǔеѸ˽ψˇǾƮ˟ơьǙãѭԢʴˇ',
                    'message_format': 'ФǗűǊΨˎƽǳҦˑʰʶȀƚǢ˽ĬΗJǊҺĠɔűЊɔχύǤʞ',
                    'categories': [
                            'όǷǘǳXϣǶğśǮȈŷĞʞʬĿǣѵ¢ÊϽȗ˱ƕӢǿȎÇʙА',
                            '}ΞӖϔ²EϱƵɭÿЧр¢ľȍʤ¦ӧҺɢÐȯӊɯåɕ˷ɍҞÉ',
                            'ι˟ϋ{ȋǰуØӲąӑѮêŞȁoč\x82őѤͰίɄПʝАÆµΧӭ',
                            'ÕҢΣΑɍфϋЈϷ\x82ǇϮĹ˒ɓɮ}Ä˟ԡϾöɨ\x9fŏ˂Рάéé',
                            '¸҅НϳϘǬЇ',
                            ',ǘaӃŽдNǵӻҬНÓɣЇϱ\u0380ƻ˖}ʟ7Ӛ¦Ŀ˗πǳΞſс',
                            '\x96Äɫљҗ˃CɏϴԝĒқ˫ɜǂǐΠʎҶͽǂ˛ȟʨҩêӁҒϟπ',
                            'Ȗϑ-Ԑ˻˃ůўŌӋ˱ɦ\x85Ēŋ§ӖЙ\x91ƆĝǇĊǤĆˮλĲϑƂ',
                            'ģѠȪƏɆɗλ Т2һϓӣҩěF\x9fҨϾ^Țɾ˛Аï÷QˉɘЭ',
                        ],
                },
                {
                    'filename': 'ʅ˘ÐƻĬ˓đƉȴаҩˍӱOԟΫ¶Ȉ¯ŶȋψĹƃɊиΙǽԕȆ',
                    'message_format': 'ԢʁАϽɀǋƗčǇґȠԊ«Ҹ±ɗÝɨǗǻӈϪΰwԚλǖŚɤɆ',
                    'categories': [
                            '˞ɘ\x9bǚԮÒǻDƬ´ʪʴӼϜѸŴԇ+ɷD\u0379щӑ@ѪɑҍӐŚê',
                            'ёĨ8ÊűƖȱŉƽӈʰɍĽѨ1Зˊˡ?ɫѨZǽΞЊљӕИϨɈ',
                            'ѣÓѵԣȝVѺŬȾə\x9cαĴĩɦҺ҇ѠQĊѭsƏҧ˴ɠө\xadq·',
                            'ҝӰӇcѧЮķΦι˒ӥĘɓѮ\u03a2ˋѝѴưʭœҵƉΞŴԢ\x9dßəХ',
                            '¦Ј+\u0380į΄ģȄƧͺï\u0378ȦԋʼʢķѭӔϕsğΫgҊϋæ˥ƈͺ',
                            'ɸȻ\x843ǔЩӫĹɿ!҄кԀˆĩϲƕ\x8cԀÚȊӲmӕɞ©9ӠƋ\u03a2',
                            'ʆhʱǳ\x99ȅԎϱ',
                            'ҽҐд\x80ҙuμĥĈĬҕʎ1˗ҠɯͺΘҐʮ΅ǂΓӃǕǜǇϴΥм',
                            'ɍή½Ƀɭ*ʧĀʻʜńǄĕœ=ɢçɏȤ\x92ӾƆ~ЋΊϸ¿ǯğң',
                            'ɨӍБaʓϧ˹WʹӨшҦ1Ϩ\u0379"ɔď:ѻƻѥɯӣŚżӟЭԅɠ',
                        ],
                },
                {
                    'filename': 'ϬȒԧ0¨Y\u03a2уȂȞʯԇӀǱĚɧѡȣρВҏсԢĒčОȊѻЌǭ',
                    'message_format': 'Х-ЭǍɌԙʝԀϿϟԕ\x9cԝҟʿ˲Ʋ\x94ÁƼԨӾчʥɑҵʇҒΫK',
                    'categories': [
                            'ǤİԩǮϿ˃˕«ùaӭŨϐ|ҴǠǰʳѷ\x83э¾ѤʮԞρӚ=ӹŉ',
                            'ǺŃάϛ§ɍˮǍԦ¡ϢʯҎ˳Ѽ»§\u0378ϋŶΣϭοϪҽȹvsä˘',
                            "ƾʛƴ¡Һ˥ʦȼҪ»Ƀҝ'ĵӘϬϝԦʼœéШҙņɘʏԀšˋ\x84",
                            'ϓѢǳƶӀʮȓʮÿH?ʙËЖIӏЯLΦΫǣчœ\x85Ԍǝ>юӫΦ',
                            'σ˭ŁWҒғЁӒUԓҭʖǋÞŇĽӡƃԔӬӯ\x82υ΄Ѳ\x85Ійɒ˔',
                            'ŏГЎҰƺԪķЬ³\xadτȓ0ҎʂɪǝƍξӬ˲ΒšӚɏ:хūμӽ',
                            '\x81˱GʀƁӐӿїԮϐƭĆ(µ˯·=\x97е˧ȥȗFӮїɂ˔ëΠS',
                            'ƜţʌǴҝƄЯӌŲɡ£иѰ˨ǤCͲˠǯѐŒŐµӏѭϰƸ˼ǵЎ',
                            'җЄ˘ȁħєѦғų˅ѢҠǺRѽӄϡYќŶԖӧŉ͵єЀьʥŋɉ',
                            'ɞƴ҉ĪǷЈĶƯӳϤŌѿǨɇAФ\x95ƽ\x9eĩŉѬƣǥɉȹȖʏӽΖ',
                        ],
                },
                {
                    'filename': 'ɁԬɷ',
                    'message_format': 'η˧ĚˁЛě9ƚҫ\x7fͼҭʁêµÍԢ\u038dƸ/ȗη˺^ɺӌӉӬɡґ',
                    'categories': [
                            'ȦӍέ/ĩγ\x92ӈԡӢΌҠΣҧG˽ӷǠƤéwʘψǉ˾ɒӒ˹¥@',
                            'ό',
                            'ʒиȩϕϫӪXѕȜǂCɐțԐZʪĠЗÀÄǊȋJƵȐЙØҖŦҪ',
                            'ɡüÕóԟΌʉǊ\x8aſ҄ćԩѸмЮӜǱĀЅϭʝƿϹìmΜƉȗȬ',
                            'ӂİ(\u0378Ѭ˚.ľǋƾ\x80ӮſȟФКʫѤԬȃÒƼ˱čŖƻȬźʪҫ',
                            'kȏϰýȯ',
                            '˸kВέǅƸЗɔʆϛԈѺжΠûȐɯѕʌʬԅóЧȫԘӋ҆ѠѺӧ',
                            'ʍ¾ǘӯǶлĐλϒӔԪÖöԧʍŅƗҞӺñǄ҄ķŹ',
                            'ΥϼÍˀӇ1įҖƯˇЖʟϢӈʾǜϘϡɊìЗϜˀƨÖş˨ǕǇр',
                            'àϱͺӼlǃ˓ʕǷԀŵέѬƲѾǸŲҳϦӺӽҮǜҥłʔƸɄƊƵ',
                        ],
                },
                {
                    'filename': "γҌʯӴU'ιơȏϡǸǗ\x90ͷѥlʌ½Үƃ=ƻ\x90θϯ\x80ўɏɢʾ",
                    'message_format': 'ԐҐɵːɷΉγЬаɆßӘ\x9aʸѺʨΒԈM¬ȆԈĬ\x91ÖʾТΤU8',
                    'categories': [
                            '҃čњ˄ƛǒƮӧҟФϬǌĉˤvŽóÌŁԏϒѿȖν$ʹѿJƸČ',
                            'Üœґ\x97ΟчʏʿјêưђϑʴǛoͺΒӤ,Ɗ«ʂǦˣƖϡӆŨʀ',
                            'Vȱɉ;ĘϖҝȀɖҴЙ-ȨųӹЉÜұŖ\x9bơћҌï#ϦȞǍ˩Ȅ',
                            'ϓ˅ƞ\x88ϏɓƏȅμȈ˛ɛƌӺ\x94ɥτŌľϷˡNъΧȨÅκɈψʈ',
                            'ӦtƇɒɚˊźȩϵқшϩɊьȄ¦ΑʶĮķɬʖƵϗ´Ǣ˜ТĥŬ',
                            'ωѸʇɦыư*ɪϼ˴ƵΘӳǑĪİ˴ҭɘȓ;ȝƝРcьá0ΐŃ',
                            '\x9dЙʃѓǕƄшŝΉʋöύƁʯɝχŨɠƬüɝËӏԍ˝ʚ',
                            'ǜʠåΟāŰ҇ͷɇ\x91ϱӃʃ4јơԥǾƃɲ˱ˆQȪǚȰӢЎíĳ',
                            'ӹάӑЧþċǘűԤɃяâʸѳǕǤmӨΧ,ȩБ',
                            '¶ϞȆņȤΝ˩ϋɐőƏƔӊ\x9eӯɎɃȚχɗўöȻŲǨJӋ½oЄ',
                        ],
                },
                {
                    'filename': 'ɸҎ˚ѵґѺŚéŰvɞǘ˄ȹЩЌɆȢй\xad\x8fǭ˷ϭϕÎɝƍҭƫ',
                    'message_format': 'ėÄŚʐƄбϝ\xa0ϗ˟ǫϮǣԌġ˱˒ΤϵąϓϚ˝ɵԆɞӘӃԕё',
                    'categories': [
                            'qĩФƊӮҍŴǰ\xa0ɚŹŖ·ģÒĽӲҳ%ΆãÙΧNΧȈѐˉɻӶ',
                            'ɟƟ϶Ѳ,ũ\x9bғȢ°Џԝβԓ',
                            '-ɣΆǭŝ˅ώϐȘɬsΉ˒ҝ~ċϡĽȳȴȫѼłΨԄӝɄ˜\u038dІ',
                            '\x9eҥDűǳģҚԄǁœϩ>{˩RѶԃӉͽļϚ\u038bʡȐұƚɑÛӀŪ',
                            'àȗʳÑӒ˛ȂʘΕ΄ϿɉȍȑƜˠʲĖ˳ʋЀǑ§ѸǜѕɤЦǦë',
                            'ûʊϭǞʰΕ΄ʽɫϓʜôRńǂăġ"ƯΪĐΣʍ҈Ҡȳ*\x91˵ϵ',
                            'īҹK÷Ͽ$ʤϘ˘ɆǖӚɿē&ĲӐӅ$ОΪВȌ\x99ˑ˷үd˩ѵ',
                            'л\x9fӳКǳƋȓɽǦӯÞѪώјĖȒĄѮÂӵѪˋµГȦ\x91RԂĦξ',
                            '<ªŉYƜiǍȾѝɨÃȮӅˆǥɯÔ\u0380Бηǁ63Ȝ}ǲφ',
                            "τȑȡɦņ'ƣǒʏÈĢùϐӦƨǧKǪԗȿ°\x86ɯƑŇӣНōˏH",
                        ],
                },
                {
                    'filename': 'ȜЂϠĶóЪ\u038bԦуʇȏʾƑĻɃЉȽѠжʚpĐȃԬҺÎȡƧəԉ',
                    'message_format': 'ÐҸ·ɕϚ˫ɽƥÿ\x90ÿϜHǤĜϺǁȧȹ˳ʛÂǜÌ3˄ŹIƁζ',
                    'categories': [
                            'ąÚF\xadΨơ˅ƞ&\x8dȳˊĮΊΨȌ¶ĄѡɿΊ1НԃʤyǛѸή\x92',
                            'ʢþŎѩ\x9eȇ˹ҰÄԌѲˣѓɛԘ\u0383ҞиÐϟœƱҷβЛŲӎʻ\u03a2ԭ',
                            '˟þǘŐų\x95˝ƙѳȿćӦ˧¬Ë\xa0ƱɸʊȦӲʾ;Ж˚İƈɍԊʠ',
                            'ȃßȓ\x81ѱ,ҴъХҳĳŹϢ>ż˥ȸƳ±΅ǌҥȻӲԌǌһӡԥң',
                            'ǍåăМ҉|ɚǕQêнľɌ*ĎŦɅɧȘҌŇĒěТǪǭӦ˯Ǡƭ',
                            '¬әǶËÜ˫ƕǝЉɉ˨Ð˵˂ɹ˶ȭǵѥҊИԎ\x81ƣΌˎ§ϒɞđ',
                            'ƚЈ˧Ɂȋ΅ΉʂӬόԖČw\u038d\x8fùȄæ\x7fĆ˅ŽҚԞGȆϧ\x93Ӹ˪',
                            'ˁǟԮBƝ;Ͻɸ΅Ψħ\x86ɨɰҵř\x9fȡʤԖ\x8dɡˤӜƙӠЙԝʐҟ',
                            'ȼѣŧȁŚʲȣ\x9eſŃ˘ϊɛԔsΝϨ·ȘįƉŵǈ˞ƑǂʐˉRƬ',
                            'Ӧʍş˨»ŰƷǨƱɟɒԔƱЬф\x9c\x87ΨБɜŸ\x8cҰҰʧԪІπ',
                        ],
                },
                {
                    'filename': 'ʢϥ\xa0ŶРъvЕ\x80ʁЂԥҁӆӽùѽϤϑǜǜƲЙΆŶъӊēκβ',
                    'message_format': 'АƨҬöҍԩɐѱ¸ԊİϡмС8ȞÓǪ.ųɷƮƓΠџʝɁˡGʿ',
                    'categories': [
                            'Ԭ˹\u0381ԞΑ_ȗȠĚϧΒνӯѪΐ,ȣϏԝѤαʑʩҜNќԄõԛ\x9b',
                            'ѐԦʖɃȰć҄ňѺԚұƟĠÚ*ɡɘˮЊxҦƺσѻɴƌÖ\x82Ϫɭ',
                            'dæģ2ǍԐǉȀȍ·Ұ·ÀĿѯoïϘS\x8blўʽ˨ͻėȤ4êÖ',
                            '3ɗŰǎϮρźҵǵҍГӀvʩ҇ɀɦԩɥͷɆʅ˴џǢûðρΉɥ',
                            'ҧҨ1`Ѭ¾gΙʙ\x95Ҍ¥ƔсÃǪʩԠƽωҴÓΦԁд¤ǖķȡį',
                            'ѝΡԢʅԥ\x80Ҝ,xMʥ\x90Ѫҁ˂ҴκʨeЋ_\x85ÁMRɃȩǆЁ\x98',
                            'ƸѬBƇɭ`˛hƞ³Ηҗʴ\x9aӕ/ОŤǜà§ҵХʁʢÝƛÈȺv',
                            'ҫ¦˓ƍʂ˖ťƣÒŞƖƺÜúJáǽÈ2/ϼҚʥʘɣ¨ƂȭàŬ',
                            'ǙĦ-\x8fŖԮь˂ǶЎɃˢƍʥѹԪʞʲǂĀÀҬϋγĬџЅƲŲҘ',
                            'ӑÙƜԒΖʠҚĥ±ӷӳԢӢų¤з˼˳ӠԥĒԓѡҚxԍàθǅӏ',
                        ],
                },
                {
                    'filename': 'Ɨ,ӥύƈɎǕĀӕ˒ďƂƲđĘȜʀʛϗķϦӢѣϠʸζ¨ɣ˒Љ',
                    'message_format': 'ŁåĿ\x8aфØρԛ˘ҺêĘȕ\x81ҟłŅŎњmȞ˴ƙʟЯOƁȇĝΫ',
                    'categories': [
                            'ĂũǝѾѶĺńʌͿ\x8eŻɈЉ˩ҾҼͱӟϿuʂ]σǠ4àҮȾǘѤ',
                            'ԌәώŇǢĮǘʙ\\ЫԄСÿŭӾԙǢʴӫ˼ɴ˦Çΰˍ\u0383ƓȐԙŇ',
                            'ϊκПϚ\xadЙӐèʿҴЄљʈ¡-ƇҥҕɪĜɶȉʥÙӪʆdΊ!ǋ',
                            'ɝұŊɌťԬ¯ǷµÌäáуýҺѨҋɘϥƃĆύȍþ˅˛҄Щĵǥ',
                            'ӫʜ£ϾĉȞǿƀΜ\u0380\x81',
                            'ǪѳɍKʹqӎӨΑПԃϢÀɝɣʓģÐʵ@ƹӒҩʞӊŪ\x94ϨΊξ',
                            "ǙŭʤΥȱԑӠǦӚʴÙɸ'zĶыɕʥǠÀӑåʄÛаǀτ˒ȹЖ",
                            'ȏ¼\x8aʳ˙Γԗõō]˗·x˄ӃӜ{҉ŏҢˏ]ύͳ\x99ЗѾ˻Ӵʂ',
                            'ǿϺɿԟԑđ\u0378ǬĔԊŘԊϡŰ˭қѧZȢǶ´Șȫ=ǳˤĢқҲα',
                            'ɽȶӯϖϘƗɤ',
                        ],
                },
                {
                    'filename': 'ЖƸҘɪɅmʛΧʣρҗǊѦw˰бԄ.њTƪԎГԨFȿК\u0378ƙѼ',
                    'message_format': 'оϓĖȩѐ\x98҄ʗ×ơʽɖȅƛϑҤĲӘðҧŦʮьɴjńƕƱʜɗ',
                    'categories': [
                            '˽ϋԑʐĵʥӋҚ˙n҆ӽąҫĝЭчҊÏр˰˂ŁԭȺτĬvΌӡ',
                            'ӌɩϻЁpóԫ\xadǾVЇõÙƝѯ5ϛŹбЯƊ\x91ʃƗëɲGˆȕҴ',
                            'ұԦ˷ѯʭ\u0383˕ǪƒӹƈҀʮʫʦ_ȱȭƺQÃĘâÍ\u0379ЩǡңΝĢ',
                            '\u03a2ϻԙyȨȥӯñԟƥûқώҸЄȿɍˁЃƿ²ɝГǙɀϱ.ʘҖѶ',
                            'âЂˬΕϻӇҐРɴ\u0383\x81ƽӗʊŀҜҖİƐΓϔɇҨQ0¢łȒ¬ί',
                            'ʅˍˎҊĝ҃ЯǉЊŪůѻǾˌ\u03a2\x87ǯѩҵȬȹȵɗӬ\x9eĥϗʘμȪ',
                            'ʞjДΛŷƓſʰҥà˞еϷѧΣѤȟƌʽ˨ȱѼĪȱǯѹɶкƵȐ',
                            'ȷЄђǻǃӑџťҢŘʭҧσяȹúȌɍɔʔҥʳ;Ļ¥΄ώʬνӅ',
                            'гŁζǀ-ү[ї\x95ΑЖ˔ъ˦ǚɠɸ\x89ʔҟȶɲȹщÖƧľÈѽ4',
                            'Ű˦Ćӷ½kȽæϴʞ/ҋȸƂƎИãӻmƛΑȊ\x82ŮăãʀȘжÜ',
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
