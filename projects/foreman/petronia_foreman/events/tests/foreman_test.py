# GENERATED CODE - DO NOT MODIFY
# Created on 2020-09-01T18:29:17.221724

"""
Tests for the foreman module.
Extension petronia.core.api.foreman, Version 1.0.0
"""

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n
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
                    UserMessage(i18n(m), **a)
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
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]]
] = (
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
)


PERMISSIONS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]]
] = (
    (
        'all-fields-present',
        {
            'action': 'ƌҷƤԇҫŧ\\Γ\x90ӎ\x8b\u03a2ŰхȗɏŚϖϝǐˢÞ0ϴɪ˻ȳɣ϶˾',
            'resources': [
                'ĿӽӪҙjǍŤθӃӢ\x87ӺșʫɜɻfҷˊˇҐȬǢɍîӸŧ˪ȰҸ',
                'ɘқɡ»eҺӆȴĲ˳ѧʰҕǼψ=ƗêхɭĠƲÉʯˉQӭЇƳʂ',
                'áԡαҼ҄ѦȞFѼϏȄŗҮƟЃΑʟӖƲӍʒӪѷ˕\x85ɨѕȬȦƽ',
                'ӰԮϰƆɐƇʶӞ˨ɈˏһӊѡԗZʯъF\x84ĝπgɨ\x92җѓɱϪȚ',
                'ӠѯīƃöɃЌmÖΕ¢ѺˬŉČҿZŦҾ[Ņľ\x8eťŔȾԂΉĎ°',
                'šà\x9eŊϒƨӆgԟȐːǣА\xadǊȿ˾˹ĵӪʒǌˬɊ¤ѥo"Īƚ',
                'ĨӑрÄΊȏƹȤ¥ʬ©҄ȄĨ҈PыщɅƑ¡\x90}һГƫԠΝŭɺ',
                '\x94_ŔƊƺԭőƲĂƎʏȱōϬͰиøǂ<аԑŊ"ǝυȯ;ƹϰİ',
                '\x98ԀƁĵɵȻHȪ\u0380ûБþйШԞѱӚѐҌƭƾəѿќѺɠǺ',
                'ŅHԗυԮƀя˦ȚԏÙԐȀ=҈ɥԮ˳ɫÜ^ζ\u03a2ěϲϓκÇćȑ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {
        
            'action': 'Ľ',
        
            'resources': [
            ],
        
        },
    ),
)


class StartLauncherTest(unittest.TestCase):
    """
    Tests for StartLauncher
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in START_LAUNCHER_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncher.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in START_LAUNCHER_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncher.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


START_LAUNCHER_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]]
] = (
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='identifier', name='StartLauncher'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='launcher', name='StartLauncher'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='permissions', name='StartLauncher'),
            ),
            
        ),
    ),
)


START_LAUNCHER_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]]
] = (
    (
        'all-fields-present',
        {
            'identifier': 'ǲ¤\x8fEԤԅəҗсY˥\x89\u0383Ӌɺ˧ΜЭčØƦǍ˘ǳφ҆҈јVе',
            'launcher': 'śʾԪґĺѣʗЬҥͱӸƒǫǓұ2ÎԗƠȕϔţҜŝЋѿўȉϴυ',
            'permissions': [
                {
                    'action': 'ӧȣŖγЕÔŮªϷ҄Bȯ˦ʻŲ҃ΰӘ˾ĩхɪº¹˾ӣҺ˶ƇМ',
                    'resources': [
                            'ÁяǱ\x9aͲӳȒȕΕ\x82ē_гҋлҥǫɄԃȈӶƉǪтѿϋϨ|кȄ',
                            'ŒbЖӿϨр?ВʲҮĒȁЇШʋÏǯӶ˞ʧǶȑѱÖĉԣĪ\x9dʍ\u0380',
                            'ϐȴķҔͻԓЂїʗеЃǐңÓHɒɢƾԮɎˀÆļϫ¹>Ƹˎǣ\x9d',
                            '·ʹԔàΧԬǘҋ¦ϑтʖˡГΐƻѳ2ΊҎȋЁϥǔӼßa6Ƞ¸',
                            'ώİѾȘμԅһiǬʤ?ӏƾƣԩʬԢѲǻιƦƷƾnɹԒϒʳЛ:',
                            '6ȬőԗoѐөҔ˼ÞPԌňѾĄĺжǹ·°Ԛ¿\x81òèȍòǌrɮ',
                            'Ͼқ/Ξ˦£˪ѩƊӉƙƁǘȽǒӔɟĎԑ?ȒȀΣŵŏǒ\x81ǁȘ\u0382',
                            'İźĭɏ°ƄӫҗĠӻƴЊ\\ԠζԐ˞ɰĺYŃΎùȜԥвġҩөԃ',
                            '\u0382јÐÝÌÒȮԃ4ƚԬ҂тǍ±ԈҐʚӨәϊƱӬǎң\u03a2ҚЌôń',
                            'Ͼ¥ҥͰҠ\u0379Ţŋѷί\u0382үĜЧӗƉȍʍȕԦϺʫ\x9fǾĆé\x96ĉʲÑ',
                        ],
                },
                {
                    'action': 'ԬԆЅηҋν_\x80ȫũ˖ѤҺȳӪÇǨ0AϲÞɘÞ/˹Κ˝ʰκÞ',
                    'resources': [
                            'ǯθ˓Ѥʀ×ΌȡſτȋЍ\\ǎȐ²ϚƬôʺѶЩȵΪӗ°εjљ%',
                            'ɇcȞѝԔԡɪƿӷЁͲϫ˞Ɓ\x8aҰӾҁ®Ѓҥ',
                            'ŕʪƷǮɳѽů˱ňƋϤƺȗĊJѮͻИŴȨC¹Úηʷǃѕдǲг',
                            'ʮȐΛȯԅУǫȾсwÞ',
                            "Ӽѵċ8'ϩͺϊɓʈàԢJϔʶ¿ÛӦΩǢ¼үЏũϽmʮω͵'",
                            'зΞҡɰwϥˮЬàÖɮӿУѰɞuȕӒ\x8aѪħĦԘӔŵƳȬкĶΏ',
                            'ȺΔ\u038bԝϪɪĠFƃ҉ʛǮǉԖɡɵʇԌδʀͲ˻ӰÇ¤<ɥѽǢά',
                            'ƐĽ&ϗΛäǷϐńÊŪɨÙʘʃɭϯѪσ^ѬɚӜ˞¾ˆŻґӱ˚',
                            'ǅ˦ŸХ;Š¹£ƛȻǉ5Ç©ГƊϺϬʆ˧éΜρӒʣȬeȱΩƋ',
                            'ӭ˱οҤgΈñ`пΜȄĨШΩԥϸԕԌӫӶ˛ңŖίăÀɂҊưў',
                        ],
                },
                {
                    'action': 'ϒ\x87ŧѸŢΎҚ\x82Ɯ\x83ѣȾϠЈΏŻѧЭ\x98ĄΒҙɜǞѦжҨ˖ŊΕ',
                    'resources': [
                            'ˤ˰˜ρćǍƥ҂н҉ʮñϭÜĳíήԚϫPѣΒƈĘҏҩӳ7hэ',
                            '^ҏʝ˵ж¾эκȢʣˤ·ӰζǉyӪ˲ЭʪĴεȀłιǯ1ϑˆБ',
                            'ϞΗԑ˃µΖΓϣбŝȢӃҳÉňҺЪŅӺýȼŵΜˏИԑЋǦ\x90[',
                            'ˮ\u0383΄¶ÖǒͱȰʱԭԡɚƁŖϊ"ԪτӠӈԑŃөƞдɤÎϯΑ ',
                            'ȤÇFɏӧƻρӓȢǲηΜ϶ɬԃʑ-ЁԘέŐЮƏƢƣɥƵ\x96.Ǆ',
                            'Ʀ\x9bЃŗȓƱƏ`ΊБҡϪɸ\x96ǀʎ\x8cƠϻĚĠлˮϕľ˰ˣъӄԆ',
                            'ʑĸŗԢѳѳĝӧ/ƴɃ˝҆Ǝΐɚ˜ͱǣ˨ǚȖȃԌБʔȊʞӊÎ',
                            'ѭȟгɡҦ¥ƊЯʬҍzфȰƵˉ/Ŝ\u038dȻg\x91\x957Ȋöӕ˹˦\u038bԊ',
                            'ўҟ.ςԫɺͱ¿˓ѣȧ\x81eΊјȺcǫԖìɔХα˜ɖËԍЗĳь',
                            'ʊ˱ӟˢʛʀǙԙàƩɃb¦ϻ&ȭ\u038dŌɮȾѴǶ˒ÒǲϺʘŌΣɳ',
                        ],
                },
                {
                    'action': 'ЭԅφƔӪϖƯȹԨʟĻɰʝǦ3ƫǆΗƘЗ\x9fǇԮԊС`ÏˈËΰ',
                    'resources': [
                            'ɔƪŖξңȟ\u03a2ώУњŝҌ˙Й҉ÍƼAƀȟȡűŻƘΌԆɐêȯƁ',
                            '5CƱʆŔЌǟƕh"ɊӏҼƚҶԤ΅ˉăҗė\x89ŴóʟΟϱфӋӺ',
                            'ăĔҎ_ξ/S5˼ǖӀàũŜȡњ\x8cĎƯ˴Ǚk\x97ҥӣƒ\x9bӨǔɋ',
                            'ÅɂʶƝґbɉƛӝǑͰѠʁƛʡ\x95Ӻeʬlє:әǻUő˾ƲϼԠ',
                            'ѣԋӌʜěņόΐĸАǌѮĹɗҰϏbºҠŹ\x98Ӗʈ(\x80ϝºćЪǂ',
                            'ÿԙԋҦʛ\u0383ƑƱʿʿ',
                            'ƒΪÇƁџř\x94ţƕľƢΝíϲҌƿќ.¶ʃЈ×Ϲ^Ԣɏϳ˻ΚР',
                            'ΚϘ҉ǛѵzΜąӃȘʋӌѩǈĞɼŕͼmѤӕ˻ĺϒɰҌȆīȯǪ',
                            'Ȟ½ϚҸƝϽǄΤҲКMŦʦȠΈ{ԥǸɌДʽǶˠκΙĒƛr\x9fɀ',
                            'ʦʸӕȅΑƥǪʖiğҮȸґɩѿϷҁ-ΎсӍҠqvɅǚƌƩɾЅ',
                        ],
                },
                {
                    'action': 'i˸4iŸǈǡӡê˾ɉԙӄő¼Α˪ӣӟЈҷϩ˽ˮţΝŎӿˠă',
                    'resources': [
                            'ˈҀXɤԒȅρӀψƎΔɦʫÔԁƫ\x88mЭ¥qӡȜдƴ[Ӻǥɡɩ',
                            'rɈȜƇѝȲʝ¶ЮļȀͷɌ=˻ˮ˔ġҵӹǎσʡԞEʅ˻҉ŭĝ',
                            'ϋ[´ёƎ˵Ԗѝ\x91ϏуɺԎðŰʍϰÜӣŝʛӿфǓȦѭ˶ҿ)ď',
                            '·όаĐ0ѲϢ˙Їҍ\u0381ԎҜԫрҾԊӴΪ΄ҍƀȓňʓҿӒũ˵ȏ',
                            'εӈǘƊїӷӟѠ˯ɇӞʬɀҟǩǀӿʥϣƝˋʴʠ»Ȳː҉Rɳƽ',
                            'ϬOǰӳӆʸŔʑȀǱȊйίȫɵÿǹɯƨǶ\\ӉѲͼуӬĭʿ͵Ѧ',
                            'ΤÅЕǏјӱ\x92ΝθѢʚȫԉăΉːТԐȗ%źĸȭϪíШ.ɞǣ˹',
                            'ƘΕ/Ыԅ}Ϣҙ;ȎЈӖ҉ѦБуɽԛʍ×õϓɥǲҨųʜ˶ϝ\x82',
                            'фˀҡәӝϫɧɢ˾&ȦXǶό±Ǿ΄·ѩЎȼӞʓҥҖ˵\x9dƹǓı',
                            '|ѢΊԬѪӕƏNβщȻҀµӍԈԞ˔ӛΌǚȵЬ%ß\x85ÿΜ˓ɒή',
                        ],
                },
                {
                    'action': 'ʞАX',
                    'resources': [
                            'ȣ˙ϬѶҠӝ\x88\u03a2бɷԛПӊ\u0381KҼҔǯ˓ӚƿѦӶĎ±ӣїϙǧˋ',
                            'ϳͼ\x8bɰďԌȹ˵ӧaВҪȟҚǉɌŨȋƚ»ӬǃɨŕΗĘɖØԁа',
                            'ɋϬӔҁБѺΖ.ϑYŬȾђO\x85ъңĐ¤ӶEϞƕͺȰΚˎOљɵ',
                            'ęÅҺÙ\x7fȓȞǝ\x80ʹɑæФ˶ЧŁɆΤҼŠʃÈϮƍʱОʲƊʤʾ',
                            'ςēĴʸˬɩԡν4·ȤʙĜʱVǃӽϥÜâÝZȢŢщÝЗԁʷ҆',
                            '©ŤҧƸļʘɐЫ³ӽ\u0381ʘ\x83ʚԔƔƇÉǺҽϵчԫƑgȔŖ3т«',
                            'ƃӍSѐŬÒϽϿӝɬҔӓҡԣϧ&ȵӰЗ7ѼΥѦ˧ȫrŎҴԤȎ',
                            'ȸҎΟǶ&ҖĄłоҾϛBƍѢμѸ˙\x8cΣôǂȀԓϪԞʋҰLŨŪ',
                            'ӼĲƟoŷЪ]Ѣôǡ',
                            'ςҀØͼǅɅҷŧԧ΄ϲѕfʇЈĊƢʟӍМɋ\x81ǦΐʣLԌƬ҅ӣ',
                        ],
                },
                {
                    'action': "Ϳ˭ôƽƍΰӱƊȁҿǫʮȿ\x87ȂđƐĥцæʜ 'ƂˮƸˮʬŮX",
                    'resources': [
                            'ӊĪ˖\\íч\x97ιςŲƊRҼǤА˗ҸțӴȈ\x9bѣʯȓԜƃ˖Àŉў',
                            'ȼɳЃϸª˹˗ɨΑΆǨҞԦώǕɅíφpˢw3αԪĈŴѐ˛äω',
                            'ǍӇɝ¾ɳɰүɶБʦ\x93ʹÞìΓʍɡMήІţ',
                            'ñEчÓΥΤ§ćӴ\x8a8q·ѦȤ\x99ѯЌľ¶ўdʤ˂˖ˬΆƧҨɍ',
                            'åӌɒȈƵӳԮɎɅȷӢŰǐӸ²ǻӣ?ӝćиҽЋȊŃұƲϤKІ',
                            'ƎϟҹеІËѶoѶэȣ·m͵',
                            'әѠЯϕұ˴ԖǅДΨÛËÌͳǡŒԪϼŮЋγƈсЬ·ЬʥǊʣҎ',
                            'јϤΧъђгōѫƮɐӒǺńšéŞƧʼȪϭ˗¦Eı˺˳ϥϹǡĲ',
                            'ɋӛƟΩЛщëҢOԋѹǾƿ҇ӡ7Ò҈:\x80ůɜòŬƼ\u0378¾Ðƕǵ',
                            'ҟlƙ;ʹɤˉɲǌŌˊз\xa0ĀǺ$˖´\x82ѿҕКyү\x95˥ҩϻѡʯ',
                        ],
                },
                {
                    'action': 'Ÿŷ˥ʮ×˯Υϣ+ńϥ\x98ёɾҝ\x93{\x88ɿСŹɭƳϝÎчǴ^˝}',
                    'resources': [
                            'Ðӎňцё\x91ШѽӼĭУĪŤ˪αШЈҹƇȱĽʸРӬρ7Ūӕӛƚ',
                            '\x95óϬɳӨɭƊǩʺäƮʢоҫ\u038dκ¹ƵGВƷ¤ĤӽѰƾԎɔӪѳ',
                            'ƌϔŽћϹѐŨ·ĺřΤԩċǄҷȕΉÓƨęǪēʢƑŸԜыбĉ˦',
                            'ɻ½ѰƈXѳfƧ҃ƾӿ4ћɏ˓Ѣ\xadƟΣˎѝŶʳʇNƂ\x9eɮ\x91Ć',
                            'ЧǚľҝҊ<ϒÝӦƮ¦ƿϲȞѝɝǾÙɡǖ´΄ʙӑҎˆ˸bКӼ',
                            'ЁqҾԠѕ˹ӹӡǲ\u0378ˀξƸʔ˂ԍТχĚђɖ\u0381Ȕπсƒ˭ɤ\\ƴ',
                            '˽иǵ\u038bӎȖǼɐӄ˛ϷϖaЬѓ˸ў2qǨ\x81/ɔ\x8cѽĥϭ\u0382Q\x9d',
                            '=ѢƝȠγ\x97υvˉԍčыǉɰХɂ\x92ĐҐэ<ÿǗΕƨuȄДÿȘ',
                            'ʁɗĈӦӠǶ҈ƪ҅ХѾÓiʏǤġƋϱʴ\x9a¨\x94iǤǶҞϔƩËѲ',
                            '˅ǮƿӗΤѦȄɜɎƕĉƬɛɥãFȈɧҹȁ˄ӨΗӤѪΉ\xadfа@',
                        ],
                },
                {
                    'action': 'ǢΐiƷӉƉńȁа³МЁȽīήƿϕѴW_ĀŎµΦҘŬŠǼ!Ҭ',
                    'resources': [
                            'ĞƆѽΈɳϜȴԜ#ϤÄȠŹ\u03a2рèãÁöѱǫћөŸ×ϝ',
                            'ɛǕˍҢͳĺӴǞNəŗCʂДСóӳƎ®ȝКī,ʭ¦àŐѴҾȵ',
                            'ӇѬ˅ǥ\x8eӧϘȁʣȓ+Ҧŕ\x82«Ӿќ ƍΣѬƚрҫӫōΠΐ˓ø',
                            'æɷ˼\x7fȷӌ\u038d҆cěјƻƯѹNЁҌҪûˡ˂Ӥ҉ƖԗϖɘӕŹк',
                            '҆ʇİ˛ưҬĊЈҢȰʟøʏ˓ΧεȞ\x94ŮŨҦˑɀǛΗdˈàŝʲ',
                            'ҥѺɲӊϏşˈ×Aʟ1ϗǍ\x8dӀǬԈ͵ʘ\x8bФǉ"Аŧ˶5ħҌб',
                            'ǋҹмυƤҩ˫ǫ×ǟ\x81ǅƩkԝʄϝцШЊoʏԪъÈ\x90Ύ_Ǟ˧',
                            'íƿƌûӿÄdҤѳƟӇÿѳȧɎMV\x89Ϣ˪έυ{ϑ\x99γjͳϨɏ',
                            'ɞѨӒǶӞѧʶIЂҌё¯яŤϚİӌ\x89ӅѸĺƳX˞Қɍƨĥѱŀ',
                            'ĥ:ӾɩҴйŃʃÚΝŧÎōȅëŽųӪϏ\\ˋҸȠȼʦŇɫȡǅΙ',
                        ],
                },
                {
                    'action': 'ʠȱѧѮƋх',
                    'resources': [
                            '8Mɘƍũ^Ч˾˟ˏġаˍȀјҪ\\˾',
                            'ӤȐˆӛʔ?ÔɽƏϊûҁȕԝðэcҊґǑǵȉċҰjʩқïΡԨ',
                            '2уχѰY҈КϹɞο§ξѿМӉϩЬȋҩͿԆǥʋȢŞƺǏҟƧˌ',
                            'ӧҰΎȞѐҍ\u03a2\\Ȥ&ɿɢ%ȐȜί\x95Π¦ΌӛʐëҔ˗ЖүϵϟǾ',
                            'ȃĉőǙĎѼ"ǺϯʦύWɚӁЊϾí',
                            '½ѫƴÖĴ\x90ŲͽɋҊßАκÉȉȭΆϡ×ԀƋϻΛ\x8aƵы]ҠČʻ',
                            'ɐ˰:҈ђНѧþƨ˟ΠŢВԁĬ',
                            'ʥɳӺӝѽqΔɚӴǥČ˂È|6ҫi}ʺȷăρʭć˓ӿģơŴЦ',
                            'ɉRɲˮ˞ΖʜȠыΡоΗкĖ:˼$ʤ˃œŗ}ЀJҖǼƉÙT½',
                            'ɓɵˠδ˃ɌʹˈƊΜȯɲаȍ;',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {
        
            'identifier': 'yë˶',
        
            'launcher': 'e',
        
            'permissions': [
            ],
        
        },
    ),
)


class StartLauncherStartedTest(unittest.TestCase):
    """
    Tests for StartLauncherStarted
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in START_LAUNCHER_STARTED_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncherStarted.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in START_LAUNCHER_STARTED_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncherStarted.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


START_LAUNCHER_STARTED_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]]
] = (
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='identifier', name='StartLauncherStarted'),
            ),
            
        ),
    ),
)


START_LAUNCHER_STARTED_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]]
] = (
    (
        'all-fields-present',
        {
            'identifier': 'ӒĊҮǑ®ǾˉƩ?GŦ˂r˥ϧʍ˥ȊɡɫԛίƉłƭƾҞƢ˼Ԭ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {
        
            'identifier': 'Ϻ\x88\x9b',
        
        },
    ),
)


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
                    UserMessage(i18n(m), **a)
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
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]]
] = (

)


ARGUMENTS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]]
] = (

    (
        'string',
        {
            '^': 'string',
            '$': '6КйKȡŹΧΠȼͶѧôЈLζҰˤԉǱӿɰƑˌbAǅŗҢˋ¡',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 660283806377121531,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 328478.03853660106,
        },
    ),
)


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
                    UserMessage(i18n(m), **a)
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
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]]
] = (
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
)


ERROR_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]]
] = (
    (
        'all-fields-present',
        {
            'identifier': 'ŷÒhѧĊ\u03a2Ś\x9eʼãħʬЮ`ƗԊӡĲϻθΠѿʜϺĞţ·\\˼ɰ',
            'source': 'ȎǪʉ1˰ʴцҒ\x9cɦЄƝ\x83ĠԪpΥƤϣнʲζvXҭǰʰъҧƵ',
            'message': 'ϱh˾ɫķ\u038b×ċʽ³Ҏ·Ͳī©ŐƹͿǏу˥ΦѪŰѨIȞŮЏɥ',
            'arguments': [
                {
                    '^': 'float',
                    '$': 661923.9235092064,
                },
                {
                    '^': 'float',
                    '$': 125744.42681660492,
                },
                {
                    '^': 'int',
                    '$': -5628281430482041309,
                },
                {
                    '^': 'int',
                    '$': -2527194898626428013,
                },
                {
                    '^': 'float',
                    '$': 747335.9155336944,
                },
                {
                    '^': 'int',
                    '$': 4198828918521410819,
                },
                {
                    '^': 'int',
                    '$': 4294289896002377466,
                },
                {
                    '^': 'float',
                    '$': 684412.3829491981,
                },
                {
                    '^': 'float',
                    '$': 411568.2718375339,
                },
                {
                    '^': 'float',
                    '$': 708466.776150547,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {
        
            'identifier': 'ú\u038b',
        
            'message': '',
        
            'arguments': [
            ],
        
        },
    ),
)


class StartLauncherFailedTest(unittest.TestCase):
    """
    Tests for StartLauncherFailed
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in START_LAUNCHER_FAILED_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncherFailed.parse_data(test_data)
                self.assertIsNone(res.value)
                expected = [
                    UserMessage(i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in START_LAUNCHER_FAILED_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.StartLauncherFailed.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


START_LAUNCHER_FAILED_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]]
] = (
    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='identifier', name='StartLauncherFailed'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='StartLauncherFailed'),
            ),
            
        ),
    ),
)


START_LAUNCHER_FAILED_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]]
] = (
    (
        'all-fields-present',
        {
            'identifier': 'ɵЉнԙЧǈǎΑŽФϚϋӃ<Aμ4ɈҐs˖ӶȉшˏƢɝ΄aĕ',
            'error': {
                'identifier': 'đӼрŁ0ԬԮɻҔϏЎȎȖğ˵ǖƇŪ˂jΛћԃȳˊƭ\x84İťǞ',
                'source': 'ȃ"$ò¯Ȱíυ(ѫɐȫљҨLǕʿʢҎҺÜǴƗϽӦ÷Aό҈α',
                'message': '\u0379ǅȔӐљφʹѨĄǽɒȒΕBǳŜņѱжǅ[3ĵ˦}Ǟ˲ɴҞԄ',
                'arguments': [
                    {
                            '^': 'int',
                            '$': 6598474059175660177,
                        },
                    {
                            '^': 'float',
                            '$': 121065.90155554397,
                        },
                    {
                            '^': 'string',
                            '$': 'ԥǯʞɝ҂ПĔɝɥ²',
                        },
                    {
                            '^': 'float',
                            '$': 377675.0818380693,
                        },
                    {
                            '^': 'string',
                            '$': 'ͳ¿ϪőҹϪϔĽĂЮшӲʏȷĦԡʌŚːδͶӢӞӿaΖӹĭќɫ',
                        },
                    {
                            '^': 'float',
                            '$': 496171.59259072377,
                        },
                    {
                            '^': 'int',
                            '$': -7152525769976975617,
                        },
                    {
                            '^': 'string',
                            '$': 'ʜ',
                        },
                    {
                            '^': 'float',
                            '$': 356079.9010909706,
                        },
                    {
                            '^': 'float',
                            '$': 300502.1444566216,
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {
        
            'identifier': '',
        
            'error': {
                'identifier': '´ǔ',
                'message': '',
                'arguments': [
                ],
            },
        
        },
    ),
)


class RestartTest(unittest.TestCase):
    """
    Tests for Restart
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in RESTART_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.Restart.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


RESTART_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]]
] = (

    ('basic-parse', {}),
)


class StopTest(unittest.TestCase):
    """
    Tests for Stop
    """
    def test_parse_good_exported_data(self) -> None:
        """Data driven tests with no validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data in STOP_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.Stop.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


STOP_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]]
] = (

    ('basic-parse', {}),
)
