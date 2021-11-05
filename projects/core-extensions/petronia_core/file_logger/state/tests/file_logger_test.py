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
            'filename': 'ӘªϓҶґnԮ,΄ǬԔö¾şwΆĒΏĎȃʳʷ˩f\xadӉǬ»ȮƇ',
            'message_format': 'цҸjӭÇÇһǢўÕjŁͶȔҜɓπΑǳ2Ѕžѐąτоǐ!',
            'categories': [
                'άӆĪԠФĞˇΕ',
                'ʜџ˞ӏŸÝŎ&ǹхĞұƱ˭ӬƎͶǛȔ\x9aɢϗϨȺΫǐŮԄƏȉ',
                'ѢѯЯӣԘƔŵƞϖу҄ǟƽŔӺцƁʜӨ\x99ȴ',
                'ŋStӫ3ɟΘ˒˪˷ͱ΅Ԭ҃в',
                'ԭʃʲıĘɣƳ2ѮĽӷŮɑ˲ģөRǌ˫wіkʔҼѳ˄òʷӅѷ',
                'ѣлҰ˵ȽʰȺʙÈċŋǽʵάΙƤЌů>ŢѲѿʞԭƹŒb\x86k1',
                'ó&ʮπɾʺҠΕҦϣҜʔӣŰѡчΤǠζêŬԥͲзƌƷK\x98æ\u0380',
                'ʿȽäϷƾϮ\u0379ɝȁԫ˖Ʃ\x9dmӥкT\x8fϪҪͺĉÓ^ӢǹӡԖϝĤ',
                'ų\xa0Ԉ·ѱʺĹģȈuЂǿӢџѧƎ]ĭǨμӀҧԉѥʵϲȷƀƩХ',
                'ÿPțˁԆƒўӮжФѽӦĹгʱԐʼˉѹGѸɄѱƉ¹ńăӅɷ\x9d',
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
                    'filename': 'bϗzϲ˩ȝЗϣÆÑԮɤóǵSк˂\x8aμĺΔº\x99ԓȒͱ˫ҭȴǢ',
                    'message_format': 'öҜƞҘŶǌ@bFӁˬưɜ˞\x9axԚšЄѼмJѳхmáʥÏʇÑ',
                    'categories': [
                            '\x997ѱ϶ɗƱӒ˾ÐǶ˄Ȏ¾ċɄҼǁWηƪħ˾ˁӇÿŸʣԦɟζ',
                            '',
                            'ĎˋÆӝ\x8dҵȫӍĪǳΌªƼOĦǿʷРʪѲҡԠȓҫʈҌȬgʑϖ',
                            '˦¦Зτ҂ɎǅѓŐҋІÓу˹ǰ˄\u0379τɩÉӨĀԍѭ9ʦʹʩŬȳ',
                            'ˈț˪ŤŌůǮЦα¿ľі˚¼ȭƖħԉRχǾºƩӥ҃\x8fқǨÆå',
                            '҉ӛŃˑɥǚӐθΝɝʽƞƙχǁʀǂĨũ\x7f҂őăӐϼȺСǅФ˞',
                            '΅ӬʂŇ#ů^ӂБ΄\x8fГЮ҇ʝӧ\x7fΓҸ\x84ǁ\x91ŬʡƯύ\x90ЖҍӞ',
                            'ʤΑԋѬ¶ʆB7Ȯ˭ӪҀĹˢæԠɏйо˂ȃĘʰʔǶμԎ',
                            'ГƠ\x91ԉӗɴȘɃ²ƪбЍʬξпϰĜԪƢĢŒΩ\x88ʕĲ˻΅ƣɹŬ',
                            'ѕҊæ\u0381ɴʎǖӦřʮ\x94ˡŖȦ÷ѫџïоǃÃʐϋºпϯ÷ƓҦ2',
                        ],
                },
                {
                    'filename': 'ȁѺфjťƼ¸҅шɼɊĖ\x96φ_өьǌūǿǧģǶ!ͽȷȇś¹Ǉ',
                    'message_format': '˄˻҂ЏɭʭϑȾЂƸӪКС˸Ǧ·ŶÚ9ɳνi\u0379ǁΰȚðĸ¬',
                    'categories': [
                            'µеȹ˙ɾPǞƀРΘѹ\\ϯýвБȟϕɡéԂϚƱҳĈ0ѱýƙ\x8c',
                            'ƛɉˍҪȮęņǐ»\x8b˩ʶȏӯʋμș҅ɅΛß3ͽYнʅʹԪ>Ƽ',
                            'ŘБЧөЍʫєԥԥfħϨŌӔȫbҍ7\x9aČҢΥӠʏ\x8eQǔΉȤư',
                            '͵ӎӧӬВû\u0382ͱʳéԘìХҋЗŧӗζā³Ư1ĴҲʩƌϣξÒ\xad',
                            'ǔǾҨйũǋ#ҡЄԉѣʨƷPƧǦηʗщӒЈԥ%˙Вǣɩȃέή',
                            'ƝŴТĳҋąІƮ˒ØӺĽƳѪ\u038bȡУf˗ӟWɎѠˊŵ«ǡĵȀŘ',
                            'ógŖÏǻϧЍɘчљÀʹÖĸӈԭþʭīҁŲȠȻQψºȟƜʠy',
                            'ȉа\x81ȳðϔуϘƳ҅Еѝ¡Ǡǈ\u0379DɉͿÿӆ\x8eͷЭАΉҘ>=ȁ',
                            'ӨϘΘĢƧ±\x80ǧCIøǌ\x9bƝĜӾʺ˂ĲĐȌԈŖΥûʻΊąɯΪ',
                            'ȮƜӢǺҹˡ',
                        ],
                },
                {
                    'filename': 'ιˁɎŻШĽʟƂǣιәʔ{µτ϶΅ѢʭĊӥtрîəΓ´ѫŊβ',
                    'message_format': 'ƕŭжѿʟЎĦˎΛТӮʽȺúǽϯĵs˕\x91˲țœԁѩŊҽĨϤĠ',
                    'categories': [
                            'ʛƎ4ςƤҾǢϿϑǗв\x83ɢW˭\x94˵ϹЯм¦ǞхϢԌʕѣϤLɲ',
                            'ƃʐËΙŃǼ҆ҶɣǏ˳ĞŚŧМҢźɠɗʩ˻ʻƓƁɂƈɍ\x83Ϊе',
                            'ƪԬӓȄ\x84ǵƜҽӐgІȲ×\x90ȝӉӦгͿ»ėӾͻâϑ$Ʃƌ˘Ǯ',
                            'Лҕϛ˜ŐŘұ˰Ǌũӥ«ѫƔπʪƵϓϑŁ˻ԆʔĊΌӣϟçÐ˃',
                            'χҋŎΈǅïÕžфĳHԪʠǰoʞŗʾѭИӝQΎ҇ȝѤʂȶĻɰ',
                            'αˮȜζǣ҅ǚƮд<pԦό¸Ξӛ˱ěӹbЍʆxԫʍʤϳ',
                            'әҪϬѝ΄ϐӐӋӟіƝǹҵҗƈџż\x97ÔӛǷ˙ȈVǥ҂\x8fƸƔˤ',
                            'ȌçōΨŁҺȯє¢ĤȡԦ˛ɬ\x9d҂ŶǆˮΧιѰΟĮɪϫʵǎîȭ',
                            'vӐ½ũ\x9eǾĞҹ¥Ɔǋūӽ¨7ʢ¢ƻ҉ӖӾÌgИйŊµЏ˟Ņ',
                            'νþԡѩŲҤÿĞ:ЫÌ=½\u03a2ξh˻˙5ÉѴѠхȀԧìήӳӦí',
                        ],
                },
                {
                    'filename': 'ǩƋȯūԝɣѥҚǓʍԫ˝+ŒǰðǭʔƝʀïѰԪĪɒ7ǧʁǶĞ',
                    'message_format': 'ϛ',
                    'categories': [
                            'ӎÔʬЏbѾІ£Ű\u0378ζĀϏѤʠӗˈʼɟ\x8a¨ϋ˓ʚΛÁȿĢk(',
                            'ĳ´7¹ŜɋԓɗĩοϠѳҬѢĳϣԞӨǔ\x99ҢȎӮŦĪ¥ӉҼżŞ',
                            'ήȊ©§ʌӈфǣǞȏэǮÝϹɂYŃʦϝ\u038dŷƪìάȵɵżhřͲ',
                            'і9\x82ƘԦĎŧɴõӕ³\x85љˢДӤƀΝӘӡvņλȩЈƪΚ˼Ơͷ',
                            'ɥҚɗƪӲΞɦƤЦʹ&Aʄ\x81Όώɞɪ\x94(ªԫɵΘΓ˳+ɉƢϬ',
                            '΄ҽ˖Ʊϧӵ΄өʧŴѭԬǃɅϖӜȞΦфβԅӫƥTƴ\x82ĝ҂ԭȸ',
                            'ӢʛƥκǞ҂Ԟì˒Ȅ¶ȼ¥Ų\x96¿º]υǥϮ\x93Ƚɠ\u0380ŒȄЙ®ɀ',
                            'ӃƸЋԁŐǇѩɡ˂õƘҔэЋƕҷǴϞԓӬŔц\x86ΟϴԎśҏɷƄ',
                            'ǼƽӤљʆҢȋʄτʜ,űɴԞӺЧПȰƙΎþϸєђ˽¥ƊČќ\x8f',
                            '˖ФѻƃԨϙýŠΔ˒²Ӷ¿ӴʲѶǶҧpǳ<Ԝі©ɨÿ¬Ҭθ˓',
                        ],
                },
                {
                    'filename': 'ÅОɁ\x95Ţy7ʘӷ"иü˼©ƑџIqϺǢŅϼѥ˯аԧυȃΡ˗',
                    'message_format': 'НӍÑ',
                    'categories': [
                            'ҙёȡʮ˘Ʈ6öҘȭɤәԐԆďΤ2¬ɑ˩ӷȫшҙÔòìҊßŅ',
                            'ĸŐƒéтǠFȆϲƮĂȑʖΤηǫ˟ǦºõĥƔ\x87ӍŻϔҮåԞо',
                            'ˊƆǄȯӂȃɡԙҿƃѢý˳\x8b¨ęӶ&ͶΚşϹfϗƟȏuȄĵ҅',
                            'ѫĴĜѡСǬҥrϨΨKŝɀϚӚѽȞΊ˨ƻɋΠ\x80Ɠ\x97ğΩΰӃʓ',
                            'ƣɲіÝŌΩĊш϶ѡ˥UĹ1ԕΗүԚƩƾ˰ȴ˔ɢɏʔ\x97γғӸ',
                            'ҸӕŜЙˍďɩʾʵkόԈς´ΡфðŢĽŘȇýȀÝϜʖЖ\x94ȧǥ',
                            'Ԣ;Ąӄ˸`SƔȌɠĽÓͺҤķńфǦԎȻԮο\u0382ϗѺΌԢŬӢȃ',
                            'ɟʃĵˌϵҝԫϲʘɖQʏI\x84ԅԌĽӚκñʴIʯȔӽј¹йҩь',
                        ],
                },
                {
                    'filename': '˴нě\x82¬Ϥа˻өÅȿӹԘϼʫđʧѺӭȝӬȦȌӄҷӛ҅т\x84y',
                    'message_format': 'ҢǤѠѝɵ1ƚÇ.ϒѼSѿάҝʮφѢʨÏȏʩŲǰǇíļǓѓх',
                    'categories': [
                            '3Ѐ΅Жȓńƫ\u0382ҽԩ\u0382 ƠƸʪ˦˫Ѫ-˳ʠЊ×Ϛ¤ǵċ\x9bNˬ',
                            'Ӛ˪ʺŪț9ԡ\x9eˎЅҽԌ\x92Ј\x96˯Ęŧ^QŋÉ·`ˤϹâ΄ţг',
                            'ɜЕӻҖÐВѩʇЅŚ~ȷG҈˛ԞȳȍˠͱŕӾɩЯvǝ˗ʽŪʍ',
                            'ФǱ˞ǟǆ\x90үɺύʀĂĈĺϷҳHãͽʎԏÊňϴ\x85ӪʓϛΔӌʆ',
                            'цŹƘĊΠѝȮǬʓԤĥϻőĘѧΫļҬҋßǀҢű˪ϛ~¢ʬʵ&',
                            'ɥфˬƖːjȕӘǭԈηƐ&ŬϔÝԊɆÃĲǸЏԦȋ\x84ҿϬΆξң',
                            'Ϙ\x99ЌЫԢψãͱʗƘJÔǋˉҪÛʀ\u0383ƋƇщóEŶ˃ͶҼȣ¢ǲ',
                            'ɿ»%ϺҨʊˀ$kķӐɜΗ˛ƾʧ҆ΙȹҘȐќѝƭGЩȗúšЎ',
                            'ÝŞèȥµΡдɦĚКӲřĤWđȿŭѻԕɺĶЉЋĭӐьßƃüϳ',
                            'ʎ˄ǥ¢ҺȚϨbȸԤȉѐͺΩLȖçѹӤɹďŔɈîѱŢ˚"ıԅ',
                        ],
                },
                {
                    'filename': 'ŃdıʋϱθöѐŉˑńԀάˤʢpZˊ',
                    'message_format': 'ӟTћЛ\x85¢ƷĈ¨д\\Ǯ¹ɾǰŖѮҁȚʷºiĵRӗʰȔȏÍn',
                    'categories': [
                            'īĈľξӡӝԛˮ\x9bɖ˱λѲĦň\x9ałΞΩϤѼӰҧԆϪϏƩҸV˫',
                            'ȮΔĨ\xadΣӀ/Őσ½ӕȀzĹʪˉŖԨȫѻϸ҈ŎGΞI˭ӆȲ˷',
                            'Δ;\u0380ϯÂ\x9fǝȴҸǶŜѰыcŦ&ʆɇԈĪĽÕЃϤ˾éѽƵŕб',
                            '^ɑѶ҃ɝѫȔɓĉŃћʨÿξҙɗbζ¸ƥξȻɶѪʩΝŞȷǳī',
                            'ԬȉȢ¦ƜШűţ¢įѠˌͺ\u0379ͻƏ^ƽέˍˁ}ӫȣȦϟ˓',
                            'ƗʜrϨʚȧ\x98ôҲȎɼíӤœѰ:ðķǡĿYҶӬÙƿ\x97ĚӐɮʏ',
                            'äuĵͼŵБћΧѺɐӀϗԏ}҇ʡŘ\xa0ƜƪÄȭ˝ΠħάǠԏǒӊ',
                            'ΑϺîíϊԚÈƺӵҊԂӔӈëˊ\u038b',
                            "Ԫ'аЊЗԌĆĉѨӰɣϬƊѱÙоЛɷϧǙWГϜУϗϬѯǸÑӯ",
                            '\u03a2ɨđ¨˂ǜ\x9bƲƬǊĸŉӊѲ¥ХƑҽ˪ԕVåϱПӳ\x7fҀĴƏą',
                        ],
                },
                {
                    'filename': 'ͲЫԦǙƣӚƂ*ŅȒʦҊʬcNŤͽϾҘέŜɡxϠŸԭҢˬʟѡ',
                    'message_format': 'ðɗѐͱɀϤкˊ\u03a2ǉʙӡԨ²ҚͱӳʣɭĐԕΈԭӰɴˊΰɁхf',
                    'categories': [
                            'pӘ\u0381ɹ\x9bʠǙʐƙāϬЛβҬȍ2ÃӟячўȋêȲЭɟ\x8bôԤŘ',
                            "ҭǹÙ;ЅХƺϫƗҲʌò$'˦ļӍʴǒϓѳ¡҉ҙρ ʅԆǗɞ",
                            "ȿƹǛζʆщĠŬé'˹ʗzѓызˤдӛƭʐńώѿҫӸĈǏˆæ",
                            '¬ʗȹӚŭҫÎ ǳѵԟǈ˧ʍǆѼшҶþʘϻ-ǓƍςŷԌѯĉώ',
                            'ҶżʗǖѝʈˍЈχ\x8eȷʽˑũưΤӺͰϳИɲŸјĺѫƈӈҷƹª',
                            'ʑщéʳ{˄ˍӸҁˍϽ˩ɍʏƇĝ˽ʖʡƓ<Hǥ\u0380˶ԘӅʥʌķ',
                        ],
                },
                {
                    'filename': 'ӫԛǺ˪ЍґӤíΥȉѣ3ϾÄʎʤӀƳÍʒǿϱ=ɮ6ƯĊʌĊЙ',
                    'message_format': "ˊŮ'ȦϛГũкƊǵЖŬªŐɾZÄнȮħ·˯ŢͰƟţǒè3þ",
                    'categories': [
                            'ˠАӼÇ,лӬʻTԠŬŨĹΦ',
                            "˄ŨɱӅʹԃ¿ŪӺ҃НȬ'Ⱦӗн\x92uɒɤú4ǒáľƯŘÖҮп",
                            '',
                            'Ӓψą҃ɻĕҘЪɷѽ`Оԅыɒ˰ɦľ\x8bӢĚĹǼĲȂϽÌęɯƗ',
                            'ǀќçǴ˼ƅġ˩бҰʭЌƚǥΒˌ҇Ɯłѥӻ˄ѭҧʩоĂȵǽȀ',
                            'ѮĂҼͷˎʭ\x94Žѣȑ«#˓_φсçɊȢȦéř-ͻŁ\u0378ϞƂHʃ',
                            'ɁѸŨԏˎĄґҎĦһʙҢ²ӂɳƭ7˚ÈϚə˕Ûӭ«ǂĀǢɻЉ',
                            'ϬʾҪŰǻ˄ϭ®Еȴԫ9МƢҔϧȾŃɃʾҊʾƸʵţΚgkɻǐ',
                            '\x8b2Nάɯ˶ΧЅĩǖϕƈÚ˓īʰ\x95ìѡĭ\x99ʽŌĊűīʮɾcɣ',
                            'ĞɏүŶª˚ε¤ǗҊãŷȊҀӻά"җȐªΟŦɆѫù;λќζӳ',
                        ],
                },
                {
                    'filename': 'ɹԤ\x96А$ƌʧƝўǻӐψŒїƕάїљŚñҺ|ӷѭͱ¦ɑѾӧû',
                    'message_format': 'И\u038dЗҞή\u0382ŨҋӬ˄ΪͱËҰ(&ЩԦҚƾ¨ӳѣϠŁӶXVƉª',
                    'categories': [
                            'ʱù\u0381ä˗kɌŬŒǔɴɭɍņœɂ|Ӂȝŏ˫˱ѷøĉȝТǾǥ\x82',
                            'ēÈȊԎѰAŷԑ\x91ɘҁȀʮĥϻ\x98ʻԕΧìƏʌ˂ъГʳҜѩĮȲ',
                            'áâҞɿɭ\x95ЬǮΛÊ\x831Ǜ˾ԃѨÀʗʲ\x86ϰσɜ$˧ȋɴ¡ĈL',
                            'ĠξӆϮ±ȣǰǧЧћȒƖʭɑΜԞʲVȰϫ;ƆćҎԝҺǲћбʂ',
                            'ǰЬӆʨĜҩ´Jӱ]ԞːԊке\x9fЭЀƫДƌǴVтϚʥƀǩΖǸ',
                            'ǳʴ\u0383\x98јƍșȹå4J¸ŐLI˱ʬʯ:BʑдʼltǘxÓԦW',
                            'ʣɬċȶĔύˍˡvňSҁѺɎžƉǡǅӤÚЁ˧ЄͷħǛЍҳ',
                            'ѝŒЏыҔάĺʺкȓǠʩηҮȥÒԭĬҜȓӹ\x80ɞŗȜ[ƳΣ˼μ',
                            'Ԑƴqĩ*ĘңϤǤɝäƓȓȵѯȷϺţýѲ\x94є˛ӚξǾȀ;ϭϚ',
                            'ɤńwљ²ŦтҠΘǲύļØĉŴ˸ɥˑԘƭԑMCzѪӯѻӖɮŤ',
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
