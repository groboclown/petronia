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
            'filename': 'ʯƅǺωҋĝáųȬTԍүӽɃŲëͶēɄĥɶÐÎňȇ°Ȏ\x85ɡϘ',
            'message_format': 'ɲӑ¹ϢěԘÑȶѨ˕έТќԪΪаˀȉÇDʷ˯ęŒǪȔλӅūÂ',
            'categories': [
                'ʲ\u0379Ńì(ԎΕӿȼƯӚȀйσÌƀţӂűć$ҼËđѫԑӉ;ĥɼ',
                'ҙQѺЙэ˾máҶ˟ȆҙэњʤZ\x9f¨с',
                '˗ƅǪνҚφʪҀî\u038d0ʏĺƩӟɴӤƗÂ¨ӒΊ.˃ɩȇ\x8eϻøɻ',
                'wʒҗŧӹΎΊɗΒЕϣĊҀĭӳƨˬνˀʣŹȒˣѢқǅӥʽԢӜ',
                'ӆ\u038bd/˛˖ԦƸҷƫʌƒҮŢJȯ<;ǱɌɜÂ',
                'ʳҋӒƺɄ҆×ʬҺSɀ҂Ŋʃ˺ЛˣǙΚȆpҳҫr҂ӅŮÏѾÑ',
                'ˬѕёđ÷,ѠċJҽɃ2şЬĈӂþȟƢԟŒ=өʆΔҋҤƸǫӐ',
                'ҞîʉŀԋλɐΗǆԌºʽƏПϴӟθ\x950Ț×ˍѾɌӌЌˊêǧȩ',
                'ƑȨҠ:ŔȳѼӺͱΣWԒ\u0383ТǡЉʿԕΰǢȻæьӣˠĚøɈɋˉ',
                'Є˘ΝȗÇ ЍΒħԖnŔȜĠӤǝņԖ\x95ѮǜƙȽöјƒԃÍҀѸ',
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
                    'filename': 'ǎɷƚŊřҠƚ',
                    'message_format': 'ƘҰ˂ѪtiϙͱɧǻƼȎϿïΊʴΤɂʏȖɮъͰҷɏȝԘŵbo',
                    'categories': [
                            'ѣˁļYïҜĈ¯¬ĲїʁCҭбȳɬʟ҇\u038dϠҸө«¨ďлʭ%ȷ',
                            '΄ȪϕѝΙƜώŰαɠɲƀŤөˇғoͺ«ǏӗЧЫ˗өӑ\x81ŚǤh',
                            'ĬΛȝđκǃԤ\x8fщͶɢŐ®ſԌМӏƥѩˣЯƣUұҮǵyΰȓ\x89',
                            'ȼӘʦÀǘαӘχʯɭŻҎʽˁŒʳӏȔÁűӏđŸͼâϸǊќʋ8',
                            'ÎĥPl6ˑQїƚԖӨңĀѾ\x8fǷ¯ӸѫІѲă»ɷʝ˘ːȧԞɗ',
                            'ɖԒноȑцƋ§ǠԆȽҴ\x9cбʀυƴʆ®ѠѶüʺǒΐǨ"ŐÈƧ',
                            'ҋε·ƢѾ\x82йǌ˨ɼȫƂyÁσĀûӊҋԜ²˶Đïʯšϩяǣԡ',
                            'ÍαŨƦѲϥԁxƴƺƛɓӗǓв\x96)ϏɻsƔƹҢԆЕǻˢʬǈӸ',
                            'Ѵşҋŕ½ԗĝíƷ)ɫȬʟġҖǾţѰ¾Ϋ¯9ҙŚӍԈĉǇĴɃ',
                            'ѦӱɏɃƠɬśȉƈӁɲҟˑͳ˛ˀǓùƙѫПλШǸʎԓ¡\\ԟҖ',
                        ],
                },
                {
                    'filename': '£ʬ\u0379ǔŏóàɜҮ<ɣ\x7fϸĘӿΊ¡ʇϷϨĊļ˖gӲÌȞљÚǇ',
                    'message_format': '3ԟĪʲʈŉԑҟһƦбƭ:ǀŝυӸřɺӾʧɯѻҸпѕӕɟƔҋ',
                    'categories': [
                            'ұȫʖəҎΎXєӈ¯¤єq\u03a2ΊºtâԉԥйǔŶԭͱҩƝHʄЅ',
                            'ѻϔΡӊГϾɯâ\x85ƛҀкwȉǷ˳ǽɑʶΞ҃ӉһӂEˡƥͽǃѷ',
                            'ĒϨēʖʖΎј\x97ζӿɃӇRʽĢȊŊЎҒԖ\x87¥Ű6¢Ԯ\x91ˁӧ\x8a',
                            'hΌÿԭеʢǶʲĊʦÚÉԐȚæˡð϶ȉcMÈǖØˊпƪԔƙѓ',
                            'θɇΑΑΰÊЧЫӕʡαΆͼȞͲȻŐϕēΝӰǌCӂȋǮÄԏЬŉ',
                            'ȋţϬԍΗŤʈȯɎɱ҂ǦFɖɗ,ǪэςοʔŝȺǯȀћԮЛǎԢ',
                            'ȴϣңĴʐŌҢǢʎñƢǧ§ɌǜƅǇĐɈŒωҙĴҶ˼ƍǗȢΛ˹',
                            'ɴ;ϜȏэҽҷԡһѡԆҁ1ԋUɤȝͶєFʑƆ˰ƉхӺșϸƕΣ',
                            'ΆΞ·',
                            'ƸЮqɾȡӭʫӁĮǡ½ȟɽҋőʙ˃ɆɝӋήʼԬұ\x7fϑǡԑƝȧ',
                        ],
                },
                {
                    'filename': '}ȔŊP¿άƄϞÆɗжҳůͳӛϡƤΩê˷ȷʬǰàЧȥ;ͼȀ˜',
                    'message_format': 'ȽȻɍűҒʢӎ»Ŭϧ\x8c˔ĿқȌɔWǈŚҼſǈΡ˂í˂úђ',
                    'categories': [
                            'ŌΒʟΠŪѽӛŚǪǶʌĉʢɷˀсƏОĐ\x8aУԕˌ˅ĚɋѰǞrş',
                            'ИɱIďuȬřŶÕӿűƥȪƿöƛπΖΚϝƴĕŐÙӧ-ȏб©Ф',
                            '˖5ǅ˱ΐĆkĕϟƔŗȁӿԉϝѮ˖Ԛ҆ћӍeǂȳˍʿ˅Ǝȉž',
                            'жԣѿʾ˳œêѱjϠǂʳȋΛԫ',
                            '҄÷Җ˜\u0382ѝώΟńӺ8ҖɘˮŷԓŏǯśǛ\u038b҈ϵͲȲćȝέȳ«',
                            'Ӟ§;ɈјŚb©\\¬»ƕÖ\x87˚ʍˡӡ9ϮˌÙһŠƘɌӗϬÐό',
                            'ƹˬ<:ͷҘīÞŗЗŲɒЖ¹ͳǼƓʋɕʩάÅǷĬķԬв1Ͷͼ',
                            'GЫ˵ĐΎώ˘řϙӾΘmέрüϣө˗шδžǑǱϡұþåϝǓ҂',
                            'Ȑԛ9νłáâҞ&ѮүòӿӄѰӰζòͰȳƏΕʯȧŲ˒юΚӿÊ',
                            'ӾĻʂҩŊ҇ϱѳ\x81¬V˻Ȳԡ˔ʞϻĀяɭҧĴȨΣ˨ɔ]ɭԡ§',
                        ],
                },
                {
                    'filename': 'άʬ\xadŖʅ˽ԜԙĚɕɀŽθԀvλ°ųʩ˝в\x86²ȠɀǧѥҜҦƳ',
                    'message_format': 'źԘʪғɲ2Ǭ9ȭЁɣʳǇ·ɌԞϵǒƏԌҺȌǶȯϊċłҷȝÇ',
                    'categories': [
                            'ύӉRɤϖ\x84\x88тΡѐDrĄПяҤ÷ЂÿӬɛϱӦ҃ԙέͶƕьǄ',
                            'ԮνƶӏӌИ\x80Ȓ',
                            'ȼp6ƛƔǰș҄ϨPԇКϞþӊň=ž҆ľȆɩŨ˄ĊҵƌŠΈİ',
                            "ѸΧƃӳԞ]'ƝӃ7ɇёѢ\u038dōʅ\x81ɓʷЅгϢ˫ʟ˂ɒСƄ˕ǈ",
                            '¿ȍÂǯ1ƬҤΞԏ΅џǔѠĕԋԆ\x8bƱ&^\x9aχɣÁЂԅƲRҪʭ',
                            'ÙԒƅǁЧƬ˰ķ˧ƶ˭Οϝ\x8a®qГЄɊз\u0378ɏćeӽɠȖƋÕŽ',
                            'Ą҇δϨƇχҭѐӁβӐʱʗԐɂФӣÖӒӁˉ҂QũԚ϶º˖xӧ',
                            'ôƛȺԑԖӗÜӘˡӃ6Έƞ%ɯŀƉҶЋӼ-ϵƊþ9ʆʁ\x84ȌϮ',
                            'ǂԊȾ҅%ρÏȒȞΉПѡŃҗǨ@ѨҁƗ¿ßjчŊÊαҜҧę˨',
                            'Ƽ˞җͱϓ±Ҏ',
                        ],
                },
                {
                    'filename': 'ФǃʊмƇʮ҉ĠƗѹÐˎ˟Ų˥ƄȒКÖ҅\x8cУ˒Ӆԉ,èҴǠ\x82',
                    'message_format': 'ØƨϧÅ\x84ǴҖӟáΦ(гʕpЀ\x88Ϟԟ<ɃҋTªƕЫĚ\x86ѰԊą',
                    'categories': [
                            'ɃÉbЮʧѣșç΄ΉvťС\u038dӶ[˕˭ӌԓʷȱpҮƱоĘϐʁӷ',
                            '\x9cǠϯǙŎϐӜ',
                            'јʹɳӪPƧ\u0382ɍˤЏĴȽѷ±\u03a2ɽ˺ɛhÁȆʡНƵĐ¢ӻĜȥҰ',
                            'ɺѸԁ͵e˧ҞхзżĹʭԦþɵʄƥҬГɠɷѣ˄ΟǡĖѸ\x85Ԛϲ',
                            'ǭѬ6˟ɮ6паƠԊʶȰƵŲŹĀϥƼԙʠŃćȬˍʹ3ȟΥеʶ',
                            'ʀԣʱ\x95ċļСӟҁɉшȝƈǨŮěāȅăǍȸɺҺèéǂЁξΪҸ',
                            'ϐəĸǗƦƼȮƟ˪ƲǄţÄʞѮ˕Ěûȿ³ʮΖīʥΠʦЛƆЯȡ',
                            'ȾƨҁǎӣϼňΑŀũЧ$ΎĤӽɷɥĽ΄Ɯ˰НƆοơӫŪ\x9aɊʣ',
                            'ŜӲǆЧǯŽѰîȓҹǌπˍ˧Rљҕe˂¼өӲνћƂyэϬΚ˦',
                            'ǣǉ\u0382ӓȋΤΎʑҜ\x9eԒȡǻșĞͰ÷ћӖYҁ®ƘÇ®ĹρŀҼƮ',
                        ],
                },
                {
                    'filename': 'ÓɆɤѝѰųˍТÛnƘҪĹ',
                    'message_format': 'Ĺ˥òȍĊΪƚ.ЕǎɂɥƄŊɄ\x7fvˁƈƉҞɰҁŌӣͽǘƐǑɩ',
                    'categories': [
                            'ҨӯьȚ\x81j£±ұϰ#ЈЂŠҮΫƧʔҥǣƌЅˢāͺϽΥψƤ ',
                            '˹ќӞà˫ΒȟǫԤѦˊȹŕŢƕ¢Ѧķһ\xadşЈ˟ôĉЬ®R\x99}',
                            'ȕÊɡŵϩѦҧͱӮτϸɜǎԘxƋӃʦЗ\x95эϠǟўũѹÞҗӋǞ',
                            'ҴКǁɱʒƂԖģǍyɌƧ˭£˗ʮMͱϯϙѠäӽғϺΨѡŕǎd',
                            '»ȇчћҵjȃǏΌӡÎ"ƅθ\x8eӢǤȸʢ˟Ǒƌʃƅ\x8aŏʭ\x98Ъў',
                            'ȀӗЖěωђɦĈˆƸ\x9bǥǀλЈ^χѪҳȗ϶Ρ˷ÇђʲOȖ˻ӊ',
                            'ȪґȸӃҗņҪõͷǣƲҐб϶]ĪƳвwpӣȀтƯаȘǈѿÖˉ',
                            'ьѼȏɧЁϡ˰6ГͿϕɐ\x8dк¢ƛiîȊǉ(ƀԘҲǐǓʟƧӌ2',
                            'ιөȑ\x97ϢҟĆΩŵԃ®ҁòƯɝħɤx\x9cԚȴʀƋțАÒҴɂӭ\x80',
                            "ХĀͲǮþČï˭ƪYϞĂɋ`GȄ¸¾ϳġâŴȞ)ɱ'ŝѢơΫ",
                        ],
                },
                {
                    'filename': 'бǬэ˒ȃ_ЄȗȇȩŸ˛ɓͶǗ˽ͺβ½\u0378ȨϾĚҞҳЦ¾ш?Ϧ',
                    'message_format': 'ɬоæƿ×ɋŸΓǃĄsēγͽϽ ȩZˌJΚŤЏ\x87˅ŧ$ϱ\x9aň',
                    'categories': [
                            'ѸĻӪÓŇťƫĉӘҒŧùƂЛȓͳŦƕϧyúŔěҫҲɬԎͼÃҬ',
                            'ȲҜәEӿӜҩÐϭѴчŜǉŀΝƒəÌϐŦɀƖҿlέˍɑƂɖ÷',
                            'ʖĂ\x86ˋԁΐȡԬ¹нɿǄȓÄËԗϻӐΙӾ{ȊаȗϏȫŅГŗư',
                            'ťŔӂƥ8Й\u0378ËŻӗ2ғàΉ¢ǳŧЗȿ҉ӐŚ\x99ΏυήүǗˀˮ',
                            "ǒ˓˚õˏiɖҋӻŋӰÇLΉȷÿŎӐϫƝ'ԄĹɥ4ȣ½ũŗӆ",
                            '\x7ff\x7fˢɧϻȎ¼ЁéԦOʿяș3ʔ\x98`Ȼ҄Ҹѱнĵѭɦ˦΄Ӛ',
                            'ЮÁдưщˣͿǅ¿ʲӢӲɦ\x81ϛȔɬйƙӳŤɆЛāӶōˌJÄȟ',
                            'ǐʂō˰/ԠƝМʝ9ӥĥèҍÑ\x8eȉһȩӷÃăıǣ:ѐŧ\x99ϸɂ',
                            "¸ώ΄ʵ'Ǫк)¥ǈӯƹŨϋˍԠӛ{Ǖˑʨ(ӗʃҎvѫņ:й",
                            'ɮĘфĐ¢Ҋ{kŜʕ΄ʇжϗǚʜĜɗΠÝҺ\x97ŢӠԫԤΞìГĄ',
                        ],
                },
                {
                    'filename': '\x9bƀƦƧċȅȮӫ҄ÂԛͲĂʳɩәɟӊүЀрѥŮǻ˺ԇɁɓøҶ',
                    'message_format': 'Œ˘ѧǗɗř¬ȃʷċϏįdԄŏÖ˳!ɟÿ\x96[Ʃʨ҂ƠѰ0Ζȁ',
                    'categories': [
                            'кϝαʎƲ˂ДϼšĄʍʃЈВЌʠŝϧʿRɲЏйʮȠӟɧǑɼ4',
                            'ϰҭЛe\x94гωҬљcЪψБʿӣŧʖƠӖʶђҀњhɟĨ+Й\x95˫',
                            'әϩĘӐѡҤʱɭɄҵɓŗŉϫѿźңдǻɃcӔšɑǡ\xa0ġΊƅǼ',
                            '0˼ʍφҤԚ\x92аʆÆʉхOͷ!ŜԜʽ҃ÉӟĮ˚ΰϛǥшŌɩϨ',
                            'Į4ʵʽŖƒʌňЊ\x8cбҚɈӺȓѸ˯в¥ĈʷԃƀηŽяˀæġŽ',
                            'ʩ8ӵ\u038bÙÆԔҞNɷ\x9aҽόÖrУϝӠǰšˮǎш(>ȾιΤϿȜ',
                            'ŽԋѵӛǳԮ҃Ǎҫɹʸ;ƕĖũòˡ҄AȝԒűѡǣοñΜÐρʐ',
                            'ǈŒƈθȹÑҕǸ5CӼÓ]ǯϳ˯ÆĈƣȳυ¥ώ¤@ҩҼɭhΗ',
                            'Ųȱĸ;ëԔԈŌίŠφˢʌŏƩíĨ-˚ӪÂčӻĢ5қЗȞҸù',
                            '\u03a2ĪɻԞ҈ʷϕ\x91Ư_ÓӊȧыIŢԛ',
                        ],
                },
                {
                    'filename': 'ƨЄĨγӇɌҮϊθЖ$оџЍюҝuǭʘǊŔԠŞƩҩЗŵʿϜȼ',
                    'message_format': 'ŲЛˈԝǞ£Ԧ\x9fÎ˸Ó«ԒΑαЩȬΈƒµҝǘū;ɥĸgн\x95ɷ',
                    'categories': [
                            'ԀªīÖƾÇĎ˫υαŜç\x85ÑͻѤåϻо\x8eS\x97϶ĺ˄Ʒʂ˔¿Ҳ',
                            'ƂĚĒƛ҆ӄŠÊȟӋȦΑƸȻξΣųɖʁԮŨǟèǞȑ˄ԥșΞǁ',
                            'ѝȰѓȞǼɞҧУʄǝԕȵƄͲθљƝɕϟÓϘDΖ҉ɠЊҵŴ҇Ѧ',
                            '\u0383˨\x83\u0382Ѻ˵ǑԘқɴȨɱˬпȕȊҏÉ}¤ϽΓԚӃҜvəӴˀƽ',
                            '®҈\x8faĸȦϷҨƁĐTӬ¦wá·ªŐҍɅÑríˉ˻ƉԦŤƋΝ',
                            'я\x9dȄɞӳǮ®ƽ2',
                            'ԬϝҖ\x86\u038bȷ˩SԌǃĦ˜ϩΘȝ϶ҽŐЖÈӭЙʔώЖ,ĢЄŢό',
                            '8ƾʑοʶĀMɁʰʞýñ;ʳ!ϋҙ+\x8fʑЩNĎťρɏԒщŴʃ',
                            'Tɔ5İѤ±ўЄǩѱϖėвҪʳɚΨã\x84ϓɍϠҠŷԜ˓ÌƭŕŁ',
                        ],
                },
                {
                    'filename': 'ю}ǕżɈʟsʗɞԬϙǖɎǍǴаǖ.Ƈϔ ƮԖˠԣáƮ҄\x97ǂ',
                    'message_format': 'ŀɉɗБ˛єƤԠϴK`ɱҹsԦϩƂôьǓˎƢȵĻӷԞȅ¼ʸ^',
                    'categories': [
                            'Ʉҋƽ\x97ιÂҝ<\x85Ñ6ӇȂϮϡ?ʹʝЧΫʒҪ«ͶƨȧӉʹÅʞ',
                            'ɚΎЧϡť´ҭ˭ȂÎɈʵԛNYέŲOԃį!˰Ĥ$Ӡˊ\x8dƃϙσ',
                            'Əȫˠ҄Υ΄ЯӍˣ®тǱˋНǧģǝхƉȫĄĒɚɺӔɆĪ\x99ѣ>',
                            'ʦˌӭőŌȽЦӈȮϺк\x9eĨǼѠǚƖЛŁkz\x88ϗ˻ˉƓÄҋе%',
                            "nš˱÷ϒĺ'Þƽ˓ć",
                            'ӥ҉ʸΙǔʱ²\u038dȜµҟǪѮÁʬɼϙЪШчЦ\x82ѹ×ғхøɛœӬ',
                            'ӜϦҩɛ2˃ŻȟȨƄĳӇӶ\x80Ț=ȷÚԜőԖүӹрǄƁћ\u03a2Ƀɾ',
                            'ŤӑōƏŹɎоЙɆһϮˊɩӰѪΚΩÆ\x94ҩNĜŕԡ',
                            'ԣ»ʷɿyɽeéǖ\x8d¨о˥¦ȕӬѤӿΓԈӌб\x85ǖʃȚ.Ҽʍҷ',
                            'ˣɰөδǼǢĬƠ\x8bˆĢсǪʝ_ԔΥƋsέĪǦӼĶÎÞ<',
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
