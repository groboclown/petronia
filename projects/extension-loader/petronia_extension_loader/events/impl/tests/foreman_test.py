# GENERATED CODE - DO NOT MODIFY
# Created on 2021-01-15T16:34:23.229746

"""
Tests for the foreman module.
Extension petronia.core.api.foreman, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import foreman


class PermissionsTest(unittest.TestCase):
    """
    Tests for Permissions
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in PERMISSIONS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.Permissions.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in PERMISSIONS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.Permissions.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


PERMISSIONS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='action', name='Permissions'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='resources', name='Permissions'),
            ),

        ),
    ),

]


PERMISSIONS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'action': 'ȼɤíѲˢϽŷîƦϲǸȏϷԟǑłчƼïŗØѦþǃѕϐɜǕʿѸ',
            'resources': [
                'ϗҾìɞӔ҇țIӻзĢԮɈΪΞʩїΨE\x9bРĈʋúȐRӸ˥&Ґ',
                'Ϧ¥ʷˍǽʃ\x9b˗ĦӼԁпǿЃҜŘ˵ԏˠȿ˕G¤\x9f$ԌӴәӊʀ',
                'ǼɚƅŔŪQ Ï\x87љÞĶ\x90ǽӄԪ\x99тúѬƴǲəȉƃķ\x8f\u0383ыӫ',
                'Ț\x92ĜͻĠПŋ`γή4ϑƢîNĈ§˞ƥҙϨŉϘ³Ã\x8bЃϚʖԔ',
                'Ӏ´ԪԆѧў\x85ԓъPԕɶɇΐɯŏƌЦȲϋѸЕ˳Zʬ:OԮúч',
                "ѼÌҰЫŬЅɈӟŠn·\x90˾Ȍģ'αĄƟǌʝA6ΫŅX҆\x87ѐĬ",
                'Ɍū%ͳĔӫN3ЎȸңɝζȦɨͱǫѰҫɭ\u0378ήоӔАWœ|ЎĆ',
                'ӬdГƒȋԟβǍ{òЈʽΞȧʒǡʰʦғѿcɯΟʰѱʺ&ÊҗϷ',
                'Ɲ=ÿʘµϾǑǪƙϲĳƿˀπÚόȔρzЧԡ\x89ǾʪğƃƁƚ²ý',
                '҆ĪʠœϗӤѾʝ:ÉđуӭĞľϞʅƘ¿ʒԔǴĮω\x91ѕǪͺӣǆ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'ԏ',

            'resources': [
            ],

        },
    ),
]


class StartLauncherRequestEventTest(unittest.TestCase):
    """
    Tests for StartLauncherRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in START_LAUNCHER_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncherRequestEvent.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in START_LAUNCHER_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncherRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


START_LAUNCHER_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='identifier', name='StartLauncherRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='launcher', name='StartLauncherRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='permissions', name='StartLauncherRequestEvent'),
            ),

        ),
    ),

]


START_LAUNCHER_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'identifier': "ʗĺҥ7кӶ~'ҏɱ˻зĝњрƥіeŊȆƏßӓέʜǜ˸ȜΞт",
            'launcher': 'ȦǛϐǉǹԭĪҽԪƋ҈ȖӷѬЪԉΐҞFʳΝ',
            'permissions': [
                {
                    'action': 'lŵ8λ˺ȺŲЁԄψǢΪԝȴѪåӉǇѦЅ\x83õŗǟɞϖф͵\x95Ə',
                    'resources': [
                            'ËàʹԞǚʒƖYТӛ\x98˴#ǰĿȃɽԂΒŉԂҦӣͻ\x87ǞɐӨΝϩ',
                            'ӻ¸ƫƺȤʫɧѽľ¯ϟ«ȴçʚǻĚđŪlʰ\x7fѦќÙʧʟӾ˚+',
                            'ǰBÚɤɨʅŠů˜Ǔ˓ɤţˢ',
                            'ŸϺЫ˕ѲřˁΆԈԥωó=ϦĞÑƗϹʿɸКЩɜϖŞèāԀÿ\x94',
                            'ɰӐТѫϒЍȶ0ҨɓcўĐǂµVӯƩҼҍЬfŢ»ţ¹V\u038dơĴ',
                            '*ȢҦƻŶϞђθЬϲÕϵӿƽɅŊЄԜǑȠӥψŏҊПČ\x85θƐǷ',
                            'ëʒϚ\x9aҿ¹Q<ǱУЫǚӁÍĢћ˾лʼαďЊ/ɤƭɏĦɅϬx',
                            'ʱ˃åǞӱчĲъ%ѹ\x83иӸϝӄӽӀǺ\u0383ˢŮ\u03a2ʞЈӭˌäҍDɁ',
                            '˾ҮӓǬ҆ŭѮԣоȇѢçɟЦÖuʆϷıΈǶǠѴϴɉȔϒ,ѻю',
                            'ΊĠї͵Ňérǂӳ@\x8eś˶їҒ\x94æ˻АƧӉȇcÝВҟ˕ûɵƒ',
                        ],
                },
                {
                    'action': '9ăŷʘԦӞĦҒǣʌ\x83ѷűťԩ˽ð҄ӅȷŤʉġ҄\x83\x90ʓԝzɦ',
                    'resources': [
                            'ҍʹəËßɜěʄ"ȜʢƺѺ˵Ķˤ!ΕĀhƇǑɊҌφӲʧύҖŻ',
                            'ʳϗ\x88Ǎʋėʛ±ȳΙńӡΖѐɢ˚ÓθŕůΦȱҥüҮӟE\x86ͽϗ',
                            'Ͳƀ4¿ϱμ\x83ǂǐȖ\x9bԓÏɎѷ˗ю#ɸʹѪʵʩêϛ\x95ˋȅʞń',
                            '\x8bɘ/ƮRJȾáǨЫԙ\x99ԩLɊķɽϘϿЌйʒϥŌʿúϦʪƚȚ',
                            'ѵέϕɜĿχ\x96ӭԟӄɗýĵеƜ¿ɺʟƧÈӢʷ¯ɔáʷѦdϮ¤',
                            'ʹўНɼΘӄŕőԢ¸ζºϰҟкĸːӥ_\x95?ҽĝď}ƕʲυȤͱ',
                            'Ò6ÅѳΆ.ɆVЖJѯЂғŞԫӔԍɏƸĴˍЂлғ\x82ıǉſįͳ',
                            'ѴȱƪҀԛǋǧȈаȨtҚʗĘʖұσƛ®þ¾ψŉǼфΏʔҒƒĽ',
                            'ʙ\x7fǈ\x91ѭǗǐƭʱɤɕkǪϼˠĝřǝʥȿ´ˇкtрԑȪĂѱǴ',
                            'οÇͷƏ\u038dp˳Ƌ<>ʭˤʱǴ_ϹќÙˋʄǱЍǉϛʦҀҮĹƊҏ',
                        ],
                },
                {
                    'action': '΅ϧŒ 9ĿɄǠBɻϖ\x9bɸðɳРлӼ-ѡҝЃΎԪƿΕӕșńӶ',
                    'resources': [
                            'ʨÎɜȳѮΉĮɻ˩¬ύёƇļһƴϴ`ŜōɔΨ˕#ЈĴͶÆκԀ',
                            'ĹŚѲΗɓʯưĺԡʻ5Ȫę˦ҁ¿ªˍӈʵȠ˶ƤȫӼѐЈʈƎ\x82',
                            'ÇŒΆɷȣĸъɯсíȳͲМʺӻΫϞǩzӨѭȥȳҢɆõˏŢƴ¡',
                            'ɵќǷŸЩȮӒԭҰϨϳ\x9aŏӰӿȤ6\x9eҺ˝ȨӼ\x8aʦĝRūԥɱÝ',
                            'Ğ\u03a2ʻ˰¬ҶÝƤѸʻ6ӻҹ^ђĮĿ.ɮΞȱĳƥʟñ\\ƻŲĒʢ',
                            'ƄȘѡŠԒӺчoԇʐϭΩąѱˑӘʀĩ¶ХҨ˼Ě3ӯҒǝоӈˤ',
                            'ӦȡB҇ҦψÊoӍÖFӕʴҜĬ%ԏʭԉԡʓǑ\\æԏ\x80Æӄ\x89Ō',
                            'ñȀăĝϦǷÓӃʎϷǲԄԭɪəӚѧɔ¡ăϔÙΩʻăƏϮȍӹ²',
                            'ǖΠž\x89˳ˮǥȴǀçбӠҚȞѩқþҴΡöҺԕȺЗҤtÁ4ѠΤ',
                            'Ô˒\x91ɀºȶňʱӧǠͳшԏɑЉÅǢœϧʩ˭ʦʛĘ6ÁԒ\x92Ԋ¯',
                        ],
                },
                {
                    'action': 'ǋ&ɶ˗&ĬǢηϕ\x8eƀ~аѭ¸ΧαǃҡɀшǏ˛+ϕƶκбˠĺ',
                    'resources': [
                            'fȧçȡǱѻǗʬΊԉ\x85Ȇ,ʢ˷ģОðˤǁƦ ЌɔƄȿʰяéβ',
                            'űзĠǾǀáĂƢΊƌ¿ªǦĞ\x96ҬӏĬȲs\x97ϪȅCͿøĖ˸ʴϯ',
                            'ФԘȘʔʖhȺҫԔʾʥ҇ŲѪЀӲӀӭϹǔċʽďѤyȢʯƌ%@',
                            'Ё\u0379Ɉǩ˻¡ϯʲşˣɤǕʿϛvì˥ʶЁҒòϊ:\xadϴſǜÓӐ˚',
                            'ǻǏȲîһĢԀƑŒˢвъȠJƊ¯ӳǔÖɥ\x85MɇԢԍțΓĸąƲ',
                            'ǗϽ3ûîƎӞЧʡβҌõĂ\x92Ԅ\x9cǓɍĆ˾ūӒƎ˶ЍƎ¸ӲɲԦ',
                            'ӄѳԃwɪύӧПŢδǱ,3ҋʿHƘ_ǓΚЧԐĢЭµΫΝȑÐʻ',
                            'ΦԁҨԖɐ\x99ЍŸɵƵďʥȫθφӐӳ҆ѠˇѢƎǗȕԘȻ¼ëƠҋ',
                            'GӍŖ˜ɒ\x95ѳіҴƙȩ%Ƽ΄º\xadŞǔNxǦŏˬn&КʮƢȩϩ',
                            'ϤÎȄӒĬ\u0379ˠːѬЛѕŇĚǀԬɝ˘f}Ɨ¥ŸɒΔ[ʐÛ:cǺ',
                        ],
                },
                {
                    'action': 'ʺҮʪ5ΪϋΪӅ\x95ųҥНͼЍʋʨйəԛĜн¼ǺЯѦïͽЋͷƇ',
                    'resources': [
                            '\u0378ûѾΡǱÅӼɓʚӭő˕źɜìϼɶ*ѵȄǁѼɛШ÷ʝӂƔԆ^',
                            'πAЃаӕȇ\\ĲƦƇ~ʥξιͲǀѣɬˎаˣѡǻĕġǷ·ӈϼǶ',
                            '\u0378¯әǸ§ƯɛҘІҗə@҉tώОϴŁħ\u0382ԂÓŤ\x93ơˉʗυ˟Ё',
                            'ˤʛΪ>\x84ó|qγԥЭĬ҂Ћрϛǩªҧˇűɓ\x9bΰǦãǉϥ¹ʉ',
                            'ʅϩȡўįĝфҰͶĬ³ȡрɴƯƤȒ\x8fӧάǛďŵůӇɌƣǶŖЧ',
                            'ԛг˷\x8dɈǋɂçĸЕǾƈ=ϯŞ¸úȂǡěӌӬĭĺΧ7ɯЙϏǸ',
                            'Ğ®Ơ\x84ÏǍϳÇǍʂ\x90ǵǮόŅŰüТbЪԔōȷƩɊˣѧƑϋä',
                            'ӽŶʴ{ӣ\xadŉӼϠѨΕƨГŌɚĶņØ¡\x9dтҀȶϾbѧ¾υӨӶ',
                            'lƀХΎũäSρÍƪԓJΊ˙Ȑ^ʛЏҌʽѽ\x92\x96ӓӖʢʈŢψó',
                            'ϝюˣҠѧ|MųЩÑɪȮƇξҫϋȼBē˂ҚœVʜїєđȺҽT',
                        ],
                },
                {
                    'action': 'ζˡӋ\u0381Ғ»ȃ)ɟȱõӰcфĻƎϻ΄Ò҅Ǌјŵ¡nԗϴ҃Ӗ˥',
                    'resources': [
                            'ȍŘCҋüШҜťӤŊȍ;\x80ѥȲyРҎȮğɟ\x95ûʙԭƸ΅\x87ŹƱ',
                            'Ψɻ\u03a2\x99Ѿʡªőԛʉ\x9eņȨŐȧԚγăɼlϪ]ӽԝȖ¸ԘϮҟʀ',
                            'Ԓ҉Ѩ\u0379ǭʹЕȰŶӲɭϒǴxҲӷƀÿĂćǿʒǭЍċ\x8aԨɱƓγ',
                            '\x87Ȍ϶ψ˸ĶѲĔƕϻВńËčƂиtĽĪƍДϙБñ',
                            'Қ˥į\x87ȊƇϺǶЄøԝїXӫˏ®gRŎęû9ԑǬìɑŝɰԨҭ',
                            'Ë˃ʠ]\x83Ϡҁφ\x81ǵʿҏЇşœşǒȢȮҤ҃#ԗǢfώɏлωƣ',
                            'ɇāșǀ7č¤ϫȠĨʘňĖҕ˗ƎɆƅӼúҴΎєǡǽɒǶѬǷÆ',
                            'ĜÛŧʉPāō^ϭˇθӤŨȆʗûχЎȐˤ/Ȕσ\x93ӟ\x9fzҦ½҈',
                            'ÄCƊÕ^ŕ˭Ң%ƀϣʜɘàÄÛҞȶɪјҾАѷŀǤҳѻɟʥЛ',
                            '>ʶŧ¦½ɴҗĩŮӐӜҩΙԪʹɾɘʹѓŝăȪęŌÄƺҙɅ¿И',
                        ],
                },
                {
                    'action': 'ϊΛҾћжúƌЩϐԜҐ\x98йƿËҺƼŪéʶσþRЕϚӋσŕā¡',
                    'resources': [
                            'İǬэɛǻĜԪɁѣøԋMʟȄ˧Óʢмҫż\x8eōњĆɴȭѽʡR]',
                            'ϙДСĺŴөžƋѯѯĬɦ<˅íҎơѬ˥\x90МŦԡˍʯʜƦѺȾѮ',
                            'ͽ»Ńҝʁʫ˃ũťҏ˳ȮЂЂÖĚȈʿåӛ\x8b˲ʌ˾Ɣ~Сˁф±',
                            'ȋkǖϮιūŏϭһúˍӳ\x8dʡ\u03a2χCҍǺΟ҇\x7f\x81ƾӇ\xa0ĆҼ\u03a2Έ',
                            'ҲŸ҇ʘ˟ВϾϞNÚsɺΊƆж˂ԀˇѺӶ\x98ǚĒҖÉKˌʐђű',
                            'ҩÎҁƻǭӛʐ(˭ʿˌŊĩӨʁɨїх¯ԦЯϴζɰɥѬҩÖǈ3',
                            'ѾӈҿƩċȂзɼ\x8bɔČѢȞҟˠҪ˰˶ӂɟ¦fΣƈźʐ΄ʅ˘ʩ',
                            'Ȕ=Уѡ҆ҖvǍõѨșΫƕɽԉ˜σѬϛΈźQʪЎҧŕΥιzʩ',
                            'ŮϝØЇăԞŪŮʮŃʣԪҦ^Ƥ\x9aԐρɣϼáÌйԀʞ¾ΙņӔм',
                            'ƝȯԂ˝Ń˨Ώԣ˂ßϹу˗ˮ˲#ưѳѲŜϒƠҝЊǵƭХʼёǒ',
                        ],
                },
                {
                    'action': 'ƆƅұęӠįϾŇĲƂʛЇIQđYěɦӋвҶwлɰʹѿϖɷɕǠ',
                    'resources': [
                            '\x9eǪí)яϭɓΛҗӤƚëԗȭπμ˼ǒȅХÉΐƼǌ\xadȯ\x99ЧÐǪ',
                            'Ŝ¬ςКĤ\x98Íô\x97˂Ӹ˗ʁÞʻðɣ\x9fʂ\x9aџơʷɑûįͶӆTϞ',
                            'ҪƖƠ} ԮΐɫŔʽԁÏȅΛeЖԖ\x9cĖҳȁȾҷ"ŗúЛÞˠŇ',
                            '²гľϏÅɸ\x83aҜǛЎȏìȅςĩцʴӼ\u0383Öïưɓ\x7fǺßψηӧ',
                            'ԬӍӪδ˙ϹʦЅϒǪúȥƺtϓiϒˀĎѴШͰЪˡRƀųŝöǫ',
                            'ƀѣЖΆѢ,ʆŨ-Ӽ˴ԍүĳИǣΥXԟŪҢ·ɰʄѰҤеЭёϛ',
                            '²ÞϵйàάŹϊÏѸʟ¥ҹҺȮģԝ˼Ӳӥӣ˨ρǤӞz\u03a2ŞЦЯ',
                            'ŧͻΦӖѐǼ˅Q\u03a2ў;ςɫđѤŮΟȌʱʂ=ʟɫǄɣĶqʙ˲θ',
                            'řȜ×Ε0ΤЩΆΪ\x9aȑ˟ĎώѯԇȑȬǌzЊ΄{њʸζɧӠҘϚ',
                            'ŴԂûқyëŘÛεͷһϣћˀlҭϋěѣɾϐҫΣλ^өƎˌʪH',
                        ],
                },
                {
                    'action': 'ĖĒÃĔѡ{óǿҽԜǗҸ©ʻ҇ÖɯßϜҼŪϲˇгkзʈ˓ϬҊ',
                    'resources': [
                            'ĥÒħʱёǈɑȖɠWɈʮơӓŏ˂ĤƘȸɊȀ"΄ҪĲȚɁԈԟǪ',
                            '\u038dτÌ]ӧϡ«ЈŰΣtľɆѽԭӑʜ˄ˇѬηÈΉКƽʸÝǺĆȿ',
                            'ԥ˽ƂϼȺюÈđȓÜӲʃŨÁҝ4ӲԘǵҧӮÊ˦Ϙ¤ϡ¼Ňˌʩ',
                            'ʪ Ǧ"ɖͼԣӤæҐηvȖӁǌѕ¥ғ\x9fΌѮ˧ƽǩHӲȉɘǻ½',
                            'Ѓ&ђ\x90Ɖӳ¤ũūÇ˲ӗΥʉУĬÞóʸ\x909ÓМȇ´ǌǪ˜Ęƒ',
                            'ål˰Ϲ&Ⱦӈ¹εŕѼҧ}\u0378МŖǼԟǡóѥđǻ\u0381Ĵξŏ1ѵČ',
                            'ȂōeʚíåʑФ\x7fáȭғŇĻŁǸʑΐʿˀω˽Ǧ\x96ӗə˷ʞΪԙ',
                            'ƃBƉÜİƍƊşɕ\x9eӚƱĻ\x9cċôюԠǛΣM,ӸŴĀТĽӧ˕Ŗ',
                            'ϐBŠ˓\x88ϟˑǙϛóκʯ®ƕϥó˟ӇÜѮʭŅ1˗',
                            'ӦŗɡѷňγĻp͵˹ʜŧĲRҏ³ǥđНӫˬFӓĥȯџфƟʞϾ',
                        ],
                },
                {
                    'action': 'Ǯ˽˟˞ɾΊˢЖт˞ԩȁƇϱǏЎ»ʭƨ¡ƁԊѳΣңǴӄғj',
                    'resources': [
                            'ƶʎҿɊХȤĝҪ¸ϊĕƻdѻ˭кʘŚƛŭʧŝΥϦɻƂǾńŰԆ',
                            'ĩńĞҼԪʸ©ÕƳƎĕˤ˗γШŲĚ\x9dǴӥŏȒɯɥǦɗñȒŖȤ',
                            "ǃ'Ƅȑ˃ѡ\x81˼ˡÚǄҮӚɳҮǏȐɃΕ4Ѱ˫¼÷йĕ\x86Ϭǒɝ",
                            '˚ȟȮҌ¯ǒˌɂʶҲКȵĸѶʨ\x88şˬĩʻЅĉҦŧþƂľǛeƭ',
                            'Ə+ԭƀӭˆǳƵĝҤҥΫҜԗ9ɜ˜Ď˰Ϝ˙Ԩj˾ǳзфĖʪǾ',
                            'ǦÞΓ#ƂɿȻɁkԮЂȂNɩ2ȥˊƣĆ˶Ŷȓ$ĽІŭџĺϒį',
                            'Ɣr9ԘͳҒˑΪQԤϔι\x86˸RĬҫѤğǝІĬЬȎƇЍҶſЬԍ',
                            'ˡŶȴϏǪ¦ʭśɸ\x8cǫĭϹTĸͲϺȈӘǳʳƌԢТy\u0379kȕðƓ',
                            'ǉθǖ5ȮәԀÕÂ®ŘЭʐÚҕћӣʫԄϤŗ`ƊÑÑƬЗĹѩģ',
                            'δ?\x82б¨ǛǹӝΜʯͼҷδϱΉфˏӘєȃȽʅӬÕ\xa0ΞȼƷŀӹ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'Аҋʌ',

            'launcher': 'з',

            'permissions': [
            ],

        },
    ),
]


class StartLauncherSuccessEventTest(unittest.TestCase):
    """
    Tests for StartLauncherSuccessEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in START_LAUNCHER_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncherSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in START_LAUNCHER_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncherSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


START_LAUNCHER_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='identifier', name='StartLauncherSuccessEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='target_id', name='StartLauncherSuccessEvent'),
            ),

        ),
    ),

]


START_LAUNCHER_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'identifier': 'ҥïǧќлQ¤@˼ЮÚǶČӫԨƝГĒɞԖБïėəƮęѭҔЯˎ',
            'target_id': 'φÈɿԊΫҼʐ¬%ĝ\u0378ƳlӯĄVΌǺѫΩ˯ʠUũбйВËİϼ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'é\x80\xa0',

            'target_id': '·ŸςŸ˯',

        },
    ),
]


class ArgumentsTest(unittest.TestCase):
    """
    Tests for Arguments
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ARGUMENTS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.Arguments.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in ARGUMENTS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.Arguments.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ARGUMENTS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [


]


ARGUMENTS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    (
        'string',
        {
            '^': 'string',
            '$': 'ɭŪӊŗĒĴҌCԟ¯w˜\x8eäҷїÂɝӷǹĠϊͼƖÐфƨɭЍϴ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 3420140176778509819,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 274620.6275428737,
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
                res = foreman.Error.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in ERROR_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.Error.parse_data(test_data)
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
                dict(field_name='message', name='Error'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='arguments', name='Error'),
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
            'identifier': 'ȤŇƪ˫ĴýеKѪ£íȪŐˋÛĂҴʰʹȣʆǨ®=òόӴȮ˭ɪ',
            'source': 'ǂ~}Ԗ´ˑ϶\x9eɜѤʀ)˂ʣЫqäҢѹǵǱ/ͳǋ\x82p\x8fʓˊӺ',
            'message': 'ЯГúΪҖȺ˝ȗ\x85ɌɌȡƮӬÖ=ȣɌШǮī\x9aϣΘˑҨ§ҍƿŠ',
            'arguments': [
                {
                    '^': 'int',
                    '$': 7830697149597330389,
                },
                {
                    '^': 'string',
                    '$': 'ǚ²ьȥǹфϿqыɻĸԊ˕ɟHϖ\x95˺ԞÃĳĖɞѷɢ@єЄԨÎ',
                },
                {
                    '^': 'int',
                    '$': 1526097087551011039,
                },
                {
                    '^': 'float',
                    '$': 740204.5915251063,
                },
                {
                    '^': 'string',
                    '$': 'ҞſłǄƢʝǿŒ0ǜЂƤ_ˮˀԦÛA϶ʻǰ˪ЩȒĶϮŕҺ˻Ѫ',
                },
                {
                    '^': 'float',
                    '$': 311484.8349136398,
                },
                {
                    '^': 'float',
                    '$': 729919.1817298224,
                },
                {
                    '^': 'float',
                    '$': 72533.18596823598,
                },
                {
                    '^': 'int',
                    '$': 1439735927265180447,
                },
                {
                    '^': 'int',
                    '$': 7464479940104985473,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'Ʉã',

            'message': '',

            'arguments': [
            ],

        },
    ),
]


class StartLauncherFailedEventTest(unittest.TestCase):
    """
    Tests for StartLauncherFailedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in START_LAUNCHER_FAILED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncherFailedEvent.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in START_LAUNCHER_FAILED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncherFailedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


START_LAUNCHER_FAILED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='identifier', name='StartLauncherFailedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='StartLauncherFailedEvent'),
            ),

        ),
    ),

]


START_LAUNCHER_FAILED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'identifier': 'ʹƎѷŴɄʂž˄ѮҖȞTͻʁ±ϕ˗κlˠԩɚʆ\x8dȑϞÆҍŝ',
            'error': {
                'identifier': 'ʘ\x95ҚıћɈɪȜšчǚԁҩȨςȄůƃɟ˖ӓŁ\u0382Ѷ_ξȉőɘŘ',
                'source': 'Ė\x9b\x86ӼÉ#ŗƨӪ',
                'message': 'Γʷԇͱ"ÄʅԓҟĮеɽщιǏҗȎѴŢʛ҂\x87ŅӆųȯȠŇȗΞ',
                'arguments': [
                    {
                            '^': 'float',
                            '$': 285862.8643389018,
                        },
                    {
                            '^': 'string',
                            '$': 'Ҿɀŏ˥sȂĦҫԈȭǃ¾\x9eǠ)ƒйϛƮˇζǭоϽ@вɭγɽф',
                        },
                    {
                            '^': 'float',
                            '$': 492375.7588351562,
                        },
                    {
                            '^': 'int',
                            '$': -7772581636826819526,
                        },
                    {
                            '^': 'string',
                            '$': 'ҿғ!`ɽӅʃΊŏʷǵĵ/ҰΊ\x95ɱҙЅøЮƱϧҤ˾ԩ&aƜǖ',
                        },
                    {
                            '^': 'int',
                            '$': -8202581542204322734,
                        },
                    {
                            '^': 'float',
                            '$': 393391.6926657858,
                        },
                    {
                            '^': 'float',
                            '$': 309608.2214446172,
                        },
                    {
                            '^': 'string',
                            '$': 'øҖ˰ʋ´OҊԄŒ3АԧȭƛАņ²ѢӊΉȍȼҿɕę{Ǿ÷Ҵ¨',
                        },
                    {
                            '^': 'int',
                            '$': -8535925863107275285,
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'Гɕ\xad',

            'error': {
                'identifier': 'ǐΞ',
                'message': '',
                'arguments': [
                ],
            },

        },
    ),
]


class LauncherLoadExtensionRequestEventTest(unittest.TestCase):
    """
    Tests for LauncherLoadExtensionRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LAUNCHER_LOAD_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherLoadExtensionRequestEvent.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in LAUNCHER_LOAD_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherLoadExtensionRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LAUNCHER_LOAD_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LauncherLoadExtensionRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='LauncherLoadExtensionRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='location', name='LauncherLoadExtensionRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='send_access', name='LauncherLoadExtensionRequestEvent'),
            ),

        ),
    ),

]


LAUNCHER_LOAD_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'Ɯǲ\x9bԠҘXӛά\x91ѝ˱o\x9aſѲÌˀΡÑƞĞԁ˙ԘԦӼNɫŲΗ',
            'version': [
                3162652379801620547,
                7232503037822630664,
                -4196084891972940259,
            ],
            'location': 'ŋȕ\x8dԨ7gԠƉĵíɾD˲Ηѭ?ԪвӢαśɼȬðˡѨé\x8cЉ¯',
            'send_access': [
                '˘ù"ý˒ѭʘԨüSɷȸвȁ"ѱ˖ÕωĲӭ)Ƴ\x9ffӕԥ¥ĥ˝',
                'Ŝ¹ʲѳнʧĄŉιԒЍǑӌɚϴѐѐ¶ğȎɍȳҬɛЦɞѰԌԐă',
                'мɖʼĩǱ\x94˂Й˶ҥλЪǾ,ʇԏ(ǄĜǰзƁҰқǹĆƛĞԭz',
                'Ќĭϊ·ԨïžƻèfȤʳρţѩ\x92ЛԄπƕԧȬ҈ɡıϫҺҎˀͲ',
                'ѢļɂÙ\u0379ÚϤɑ˼Ȼȥѕ«˛ȤԆ˞úѢɖ˵ʄ2FoɂσЭŦʶ',
                'ʼ҉ÎɞΊ\xadϛȅƼѼtÑȷҎżԥʓaԋǘҿċʲ$òԘ1ӘɆѕ',
                'ǿÁé{\u038bҢѸҽȃĹћʟUǫўǛԭWө*іэԩӚɧȉЧϳȚϝ',
                'ЀeͳĭɃɈĪҼΔƊǨ®ϟ˳ԓŀϤпȆǡԄ+ȯАƢϒОԨàӝ',
                'ŧϧƕȴȘξ˃ԐʣȇƀЀњХҊĄȀǠǣʎԁn˾ƐûԘ҉ňˠʽ',
                '½χȒҁѫÞԆɌɃʩɠÆġжҳǬș\x7f4Βʕϡ˕BԮȐ¯«·ʀ',
            ],
            'configuration': 'Ӭ.ƽoθǃ\x82ЛѐŖɪŮƻˇԅϽÈcÿȠӤƔ61ÏɏӺӑ$ӂ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ǽɯÍ',

            'version': [
                -2334319589540370949,
                -1698721880524029754,
                8379496583614951581,
            ],

            'location': '',

            'send_access': [
            ],

        },
    ),
]


class LauncherLoadExtensionSuccessEventTest(unittest.TestCase):
    """
    Tests for LauncherLoadExtensionSuccessEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LAUNCHER_LOAD_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherLoadExtensionSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in LAUNCHER_LOAD_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherLoadExtensionSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LAUNCHER_LOAD_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LauncherLoadExtensionSuccessEvent'),
            ),

        ),
    ),

]


LAUNCHER_LOAD_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ŬѢȕˏϑͰʦú\x9bĊŷiӕ˨ϸςͽȾ+\x9eªͳ˧ɣӖÅˡʶųĀ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ŋ³ю',

        },
    ),
]


class LauncherLoadExtensionFailedEventTest(unittest.TestCase):
    """
    Tests for LauncherLoadExtensionFailedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LAUNCHER_LOAD_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherLoadExtensionFailedEvent.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in LAUNCHER_LOAD_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherLoadExtensionFailedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LAUNCHER_LOAD_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LauncherLoadExtensionFailedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='LauncherLoadExtensionFailedEvent'),
            ),

        ),
    ),

]


LAUNCHER_LOAD_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ÌżȽxόЕɓDԧХWĵϴҠQ˅a;ǍɟʘƽʥNӑЮŶγѺ\x8d',
            'error': {
                'identifier': 'ȽsʳȷȩӣЁ\x9fđ˫ʿɎ˖ˈĸKЗBȨĄĜëɬήκÌƣӔϩλ',
                'source': 'ύѠϜ\xa0ʑÑšʈӟȉɮӟұ¢@ӝİϠ·ԢŧѾʜŬĔζ\x89ѕŚ˚',
                'message': 'ѵԭԉɮʧϋЦԝ\x90Л;˦ɛҀӤûзуĞĺSö\x9bâҌțǍÏԆŏ',
                'arguments': [
                    {
                            '^': 'string',
                            '$': 'ɞԊÅȇĽX;ϗМ˵ЭӮͺʉϫŮšȩɧľ6РćѸqÚӭ¶¿¦',
                        },
                    {
                            '^': 'int',
                            '$': -106094154816651023,
                        },
                    {
                            '^': 'int',
                            '$': -109454927813909337,
                        },
                    {
                            '^': 'float',
                            '$': 328748.96283119265,
                        },
                    {
                            '^': 'string',
                            '$': 'ӒӇ˺ȐȚʆ2ʚǮ',
                        },
                    {
                            '^': 'string',
                            '$': 'ŬҊеСјą˸ȗϢ"ϫΨЌŎѷ.ԟ˵aǛ҅ǮѐƐǣƞʔïҭ˴',
                        },
                    {
                            '^': 'string',
                            '$': 'ғ΅őĩ҄ǀƟԞϖˎʝ$Wʽ"ĆÕȱи÷ұ/ΊȱΘɴɴӴ\u0379˒',
                        },
                    {
                            '^': 'float',
                            '$': 928749.4801200599,
                        },
                    {
                            '^': 'float',
                            '$': 175116.95478643937,
                        },
                    {
                            '^': 'int',
                            '$': -8501892993231897744,
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ѬÂȣ',

            'error': {
                'identifier': '+ԇ',
                'message': '',
                'arguments': [
                ],
            },

        },
    ),
]


class EventsTest(unittest.TestCase):
    """
    Tests for Events
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EVENTS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.Events.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in EVENTS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.Events.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EVENTS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

]


EVENTS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'event_id': 'ΩʒҠηӞ)ѦĘϽͿҼƾ-ϊùϗʹԋԘɊ˲ǐӉğŰ\x9aȡΓɖԓ',
            'target_id': 'ϓСɪͺсԚΧÑʨϑʛɩΑĳĠлɩҎʽʰ+{ǫУƅ&ќкø@',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

        },
    ),
]


class ExtensionAddEventListenerEventTest(unittest.TestCase):
    """
    Tests for ExtensionAddEventListenerEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EXTENSION_ADD_EVENT_LISTENER_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.ExtensionAddEventListenerEvent.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in EXTENSION_ADD_EVENT_LISTENER_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.ExtensionAddEventListenerEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EXTENSION_ADD_EVENT_LISTENER_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='extension_name', name='ExtensionAddEventListenerEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='events', name='ExtensionAddEventListenerEvent'),
            ),

        ),
    ),

]


EXTENSION_ADD_EVENT_LISTENER_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'extension_name': 'ɳĿTŎǭGîł˕ȣŔ˔ΕˣԐɵΪŪƌқӂҗƢÒwÞ÷ΥѬȨ',
            'events': [
                {
                    'event_id': 'ƬТɧìʥɔĒҺΩƓʮʈʟǉ#(LҪɴøЄԋʂɄщ\x86ɭψϯɟ',
                    'target_id': 'ȇ=ʖ³Ԡ҈ȾϚȦ\x95ҸǮƓҺЙĝāκȔżPғАùĺß\u0378пʼÚ',
                },
                {
                    'event_id': 'ԩӷǶ@ʫшӒƁ\x8băҹŴфɼӝZǹΠΧϠгĈѠʗ˕жˠѓˢČ',
                    'target_id': 'Ǔzћ˄ҠɛÎůů\x84ΐűПƅύϭӼƭμ°ʊƙȔ3ҵϬŻӗҒϧ',
                },
                {
                    'event_id': 'ҩ\x9eƴѳǅ҂šțŔѡŗЗϣʁϩЉҿʽˏǮɉH˱RīϫʰμЋȝ',
                    'target_id': 'ϓӷͰ½ШAɪΚЁϨόΑ<Ɖ˧ȑƐϟϦŒ',
                },
                {
                    'event_id': '~ΐԍӊ\x9d\u0378ЋȚΗЛĮ\x9fѥχϨԠȬģơеȿˉː˫ωλƔӈӹÁ',
                    'target_id': 'ѐVϞġЉѣԂ\x89ԑk˦ɾ½ɓʪѰĒȌȚʬśӧ΅ŢГǅήʲȆѭ',
                },
                {
                    'event_id': 'WцРɘжĢѭҥӾĂӳüқ˘L Γ\x8fmȵťóƖєз\x84ҺˏĶʓ',
                    'target_id': 'ѐøǘȥЪɑ\x8bʟ˯ǲ;%ѥͻз7\x7fɇɲӶÏηķdԊĩ\x98єѕ®',
                },
                {
                    'event_id': 'șhӛΦϝßǣ¤˺ȭΒ҃Ȅ҅ŴŎɃϹĩ˜ʤϲʂđȊğӢϘҚĥ',
                    'target_id': 'ʅȕƞ҉ѫӶ\x9aŏƪÕɐþłɕӐƚãOȎ˕ҾŤǗΕƳğɳİšʻ',
                },
                {
                    'event_id': 'ԘМӮ\x97%Ű˞σϵʔFиȄňɧϤ[ǯÆ\x8fʿǛԓʮǗєӷ0sЯ',
                    'target_id': 'їƄ҉ԀŠпμԗ˛˘ŻÊѕěΏǉǢΊҵȇƱğǵЎç³˼ųȭ˷',
                },
                {
                    'event_id': 'ĆRÊРˎŭɹŀɵϦжΪſИĲ¾ɬÛQ˧ǰЕˮȎÜҩΙgǌɓ',
                    'target_id': 'ȎӒӬĝɅrȇȵȠ˴˅ÄӉΙÛNЏ¾Ґ·Ф÷ΉұʶиġÌϙϪ',
                },
                {
                    'event_id': 'Ư)ϖΞƶʏϟʁӄʫǛҺѶ˟\u0380ghİɞoƲóԠ\u0383ʩ˘Xȶʑñ',
                    'target_id': "БȟҺÇτžȑ\x8cʔͻώƢ˼ˤŹťȨǂӀɏįӟþȖ'Ӭџ˩ӌɡ",
                },
                {
                    'event_id': 'ӏƏļҙ"ȴ\u0379ϭģņȀ',
                    'target_id': 'ά©кzȲԑǎÛɷ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'extension_name': 'kδѾ',

            'events': [
            ],

        },
    ),
]


class ExtensionRemoveEventListenerEventTest(unittest.TestCase):
    """
    Tests for ExtensionRemoveEventListenerEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EXTENSION_REMOVE_EVENT_LISTENER_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.ExtensionRemoveEventListenerEvent.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(STANDARD_PETRONIA_CATALOG, i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in EXTENSION_REMOVE_EVENT_LISTENER_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.ExtensionRemoveEventListenerEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EXTENSION_REMOVE_EVENT_LISTENER_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='extension_name', name='ExtensionRemoveEventListenerEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='events', name='ExtensionRemoveEventListenerEvent'),
            ),

        ),
    ),

]


EXTENSION_REMOVE_EVENT_LISTENER_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'extension_name': 'ǿӤåѡ\x85ɁÄĴ1ԪɍƖɅƯԕ˯ʝЌρ˘ǢȶςƳπŮʱǘѕҩ',
            'events': [
                {
                    'event_id': 'ηɮԆϣͼɄί±ȂԮˉƗkÏǸӛЊϠҤÉƉϑž±ңřϥκZϚ',
                    'target_id': 'ЗӟņӔĖϠƁŸǀŘГЊԠǎԇҿΈƷ¯Ŗɲ¾ѪԡȼƨØơɼҶ',
                },
                {
                    'event_id': 'ABˣŖʼκȤċϞ˺Ͷȩȑ-ȉî҈īʸЇ"ʗkύӹǋϬǲɹŎ',
                    'target_id': '\x85ˬBϜ1оΪвÍ\u0379ѹŠӥʻɧйϜ:XЅԪƂѢӍ˲³ĈɿϬH',
                },
                {
                    'event_id': 'ưɢƧԢkQɤ˙\x99?ͲɵĤͲ˓ѝϽ%ɦĄʌѪȂǴҰíġԐӀÒ',
                    'target_id': 'ϺƱͺѕ3Öςϓâ˰Ȝ΅нį΅Ő˛;Š64Ͻҁłơµœƚǜɛ',
                },
                {
                    'event_id': 'ԍʝ˜ϭѝΛǓĝϓϘƫƄ»Ŗφ¯Ез\x87ǥʭ«Ѐˍʸ]ΒӎĜν',
                    'target_id': 'Ʋ°ĬѮ4\u0383ǌĞΖӤ\x8eɍǖÒӷtƈ҂9ʝяćŔŗҒ)Ӽ\x90ѬϹ',
                },
                {
                    'event_id': 'ȜƌŲТҳqʭ%ΊʕsϝɖѯϔNǷә˱њþˎлäЋˤѫʁ¡˜',
                    'target_id': 'Эūİұʖ\x9dĸҴXǑɲǹԥӈiɐ}Ѐçȉ$Ȏο®źПƮÁþF',
                },
                {
                    'event_id': 'ƛǌϵÃͺλĬӜŠǱǚŽӳE\u038bԂРΎɴɗ².\x8fŢǭ\x88ʊƋǠѡ',
                    'target_id': '\x86ѡ\x80ȕԮѷɯÉʧԉԬɊԎČΟɂƆ˳Ы϶ЋđτωȡҬɇΒԈŪ',
                },
                {
                    'event_id': 'ϯŔ\u0382ϰӜОɠҤӸѮ\u0379ҺїнĩωҖÏɥ&\x93æ˰ͻϥƢϫ҆Қɰ',
                    'target_id': 'ќt\x91Ň\x88¹ϊƉǤĭɲȇǞʗ\u0382Φͻ˅ʬ/ϥ4ƷKƧԛǸбǙɘ',
                },
                {
                    'event_id': '˟҄ʢŖίß5нɐ}ӃЉϵ»ċƘĴȅʛÏΊϟѧΒȇçƽ!˗ƶ',
                    'target_id': 'ӭжҺz¾ӌͺ\x84ǫӂғϬЫϨϾŎĭĤÞǉſπTӏϬɿǿÑφԮ',
                },
                {
                    'event_id': '\x88ŵ ϲaɚɵεɐΩ¸йqɹÍȌŌʊ\u038bȂɇȓǮҐǌ\u038bЊ;·ȋ',
                    'target_id': 'ԡҠάȄìҔ\u0382өӾˣ³ŔɓĸҽюņfʟЗˌӷ҄XȕǸҡ%еǠ',
                },
                {
                    'event_id': 'ŃΚȥȘюǴдˤ\x9fΌҞԐ˃ŏϲOӑ\u0378ФǼΨҦȀɱȋˬӪҠÃļ',
                    'target_id': 'ʔаӇҎҾӗ\u0383áȢũԢϸRy@ǿXрͷĀӉжԃĜʔЧ9άϰ˛',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'extension_name': 'ȎȠЋ',

            'events': [
            ],

        },
    ),
]


class RestartEventTest(unittest.TestCase):
    """
    Tests for RestartEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in RESTART_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.RestartEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


RESTART_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]


class StopEventTest(unittest.TestCase):
    """
    Tests for StopEvent
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in STOP_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StopEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


STOP_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    ('basic-parse', {}),
]
