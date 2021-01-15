# GENERATED CODE - DO NOT MODIFY
# Created on 2021-01-15T16:34:18.642231

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
            'action': 'ÿұӡƌƁҞȤтǔϸΚҫԝʹǠүĄͳҧĪʌeѩϞБǼqȵԧÍ',
            'resources': [
                'ӡʁҧb˸ÖƢиϛϮƆċмԜϣʃƻјü\u03a2ʏӗʇҎÛФǙΟT¦',
                'ēƀƼƹ!ӖԕΡĝ˔ЍЍĭϿ҇2ʳǍѸ9ŊӣˤƆǞșӾ¦ļ˃',
                'дΑӌƗHЫ˪\x90ЗΛҮÕƄΡʶĽuϡɯ´ɼųǹȐɩŨɸΧӈˁ',
                'ЌŔЕƱĈħƳ˃àҭǇƨҸ+π\x94˒ȎM˨ӏӧɸǅɴƄżǗŹQ',
                'ϨŎɌҟDƳƜʾŉƓěʐǔԐɼŏĻѝƚ"ВtɵԄ пëΌǯ\x9b',
                'ǘ-ӥΩȠԩԊâͻȇΑơǃˊƉϙÒ˵=ɎΖҚfԟrɢΑʙрΨ',
                'ȝăҜʩôƄШɌЍʲOӁHƿƭԎЬŒҺǸмԞϙӻŬαȸˮƫÒ',
                "ңKºGѯɽϳԪԑŕɥѓʁčμʴeęԖƪĒƋțА³ƐB'ԩĦ",
                'ŬɓƲȃDҔήΌĔˇX÷ɭԁӁmѐϱĮƞ˰\x9fΣ©ϕßÃǓΧƸ',
                'ɛφӡņfřΨˁƧͺȉ?ɰɢȣɎňϦ\u0379ȋĒɾ¶îчЁǞʵˮa',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'ҁ',

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
            'identifier': "ńЮQk͵îЍӻϺƑҬΙ÷9§ÂƊΰӥƐɍʉԧ'Ʀ˯\x9cƮ҅я",
            'launcher': '\x94ɮʭѣϾѿѽęȆǩȁӬţĶƎǔħР',
            'permissions': [
                {
                    'action': 'Ԍ]ӳŘȕƘϏϒĽўƁĲŊңþʏ\u0379ÄЀʈЧŋɀ˂қͷԘƍĵģ',
                    'resources': [
                            'Ċ\x88ΚǩƹҨ\x9d˘Ρѕ˭ϪѝâɺVӛę҂Шϊʏҹ\x82ʜŧ͵ų\u038b˦',
                            '˻VǃƺӱцV˺ʡ:&ìԎǔȸϭѧʦʞҙя0ǰż\x9bʛx˷ĽҔ',
                            'ɔϗÂЙͻȆ',
                            'śqĉ\u0380ԫԩԓʧѹʒʊӟ}Ԝɕɞ¸цɹ6føȉͿχėη¯ʕҏ',
                            '*ҧ"Ú÷ТǼӇŜĀȣӚȌҪȔԤΎʀĔɺ³Ϯҏè΅ʒȑϿdԕ',
                            '\x9dЛԈӊʐ\u0383ȌёǐҤӉ˥ĭɌЉŔǧАËӥЅӒ±ѹ çƜұǮЏ',
                            'ϜɅƑ0ˬʐÍΧЊuʘτeђħ´ћѠΈZ҇Ŋҷ\x91ÐǪƓNԏƘ',
                            'ώʝҜƒπĦӴǬϽÑš˳ѳџįёƝ;rʭίΔЁҮÁ´ɸʘǬÝ',
                            'ІӇԒΚԟӇűƷ˭ǌ͵ӿӢ±M˞\x83Ѧ˻ÏʾȳƌÑԋȆҪӷԭʭ',
                            'ȺҒѽ;ơZwƨlÃ:Ҭ\x94ңͱǬѦрԣνӕ\x9aXǛŸ-Ĕʧ5Ư',
                        ],
                },
                {
                    'action': 'ӅȰŏ(ŰƀωǫϱцДʷAԍ\x96Ő˄Ԉǣ§ʺɡ\u03a2҆Ңʩǘ˝ϒҒ',
                    'resources': [
                            'ȵ6ϺȧōŁ˨ƷΥͰȕŚψ*ȋĘеÛӿ\x82ƓƐыʺϥɶƨƧ˹C',
                            'Ӈʼŀһű\u038dńҎÐāѢ\x97ϐåãɛʾ6ԍЖńř¿ˣɄψ.š\x85O',
                            'ɔ¯ԝ+Yľ˲џlʈԭ˘ǘɓɖƓϟàèñʸΤƶɠĮŖƩǭҟh',
                            '\x90ŮČ§ƎǽТӀťƬĩǬЙÇʁԬʛÄÎтŵ:ǿРȵѧӓǼŘ?',
                            'Ɛї¸ƪԀҪŁԤŔu0ѤĠɯӂïĪːɐĶξȷWбːя·ѱ˙Ϣ',
                            'ʭю©ЧƯ҉ĔԪĐʉӲԒѼŅѽeʛЅV\x89ζǓ¼ϿæĔŎũƺ·',
                            '˘ˆŏϛɖ҈МӇϵǷӝɈɉġ\x88ӓСØѨʃÃȔmȊʴʢдƎԎϔ',
                            'Ҭ˓ūѾӜÚŦ+thԅҔгζ1ġlʧŭЧΛҘɹƈԟȕ˘ΌǪҥ',
                            'þˑԪƅȪVФЈԖѥ\u0378ԙUѶǫ¤ˣRȃTԭӥҵΔ҃ԨЃjɪϡ',
                            'Ԃɲ¤ШºũƇǨÛƱӬ_Œɵ¸ӼƓэҕӲГͻъ\u0378ƒʷґÂŋȝ',
                        ],
                },
                {
                    'action': '<ϓȽ;ȫ\x94ʧԧԓ˗Ң}Ɍɗз\x87ԂӢ#ÙӆƓЮƀѯˠѿӔ\x9e҂',
                    'resources': [
                            'ǞϖӺўƔεҠуäʆĐʹͰƖǛҒΟȫϺуҝÞҶɈ\u038d\x8aθɗǦԓ',
                            'Ŭ$ʹƉЙʈӤŶļàʼ\x95ƍɖ¡ŻΎƚϮӕӜ\u0380ҭЀөІΦΈѫϩ',
                            "\x9f0ƚѾЛԤӎ®ǈ˄˽ȔѦƶɔϖČɻˎ/ԎěǠϦԧϔÉ'ÀĮ",
                            '\u038býʏƜh\x89ϡɌ˶ϳɺѿϢ×øωϡˬġƯŢ϶ТąvʅΙԦǎa',
                            'Гÿȑå¶ŸGŨtɰȀĜгΑʥȥɐƥȁԁƓЗǨ^ϓ˖ʒ˓ƷƦ',
                            'ˏȒdɁǈӨ;Ǒôғӣγԫ˵7Ȅ˾EʱŖǛ϶0DØԑǏͼ\u0383y',
                            'ɥѫÌ\x89ƳÐ¤ɱǀʝȳƱҴԫԦɁ@ĖКǫǹиȉâϕƍԬĨΞş',
                            "'@Țĵ]λѝɪƇƅʜһʈйʠō ŻȪȅψʌуιȮğɣæϒɿ",
                            'Ȋ\x92әʹѪȵσԇqҠӟ\x92ǨľεΜԔΗÝÈś˷Ԯďө˵\xa0ƪ}ʐ',
                            'ϮѫŅԐȋɿђЛǛƀǿɘͷҕХаЏΊҔúɲƾ?ΕĩѨԭɽØҮ',
                        ],
                },
                {
                    'action': '˙ύʷȲԝҺӂƪćǯŁ¡\x91aµČíʳˇ-Я%҉ӡҔ»\u0378ʕÓʖ',
                    'resources': [
                            '`Яͼ\x80˻ӣ΄ðӨȕ\x98%Óō¹ϓŽϖɽĚćơʾԖӪϑҿȒӃĽ',
                            'À҂ӴʈȋϐλҹϩёaЈ˚ӂŞϖϷˑǤρʇӜɜƔ\x92р!Ǔǒʁ',
                            'ɺɢƓƀɉԣЙ˟ȹÉ\x9e°˜Ѻзт\x9f\x9dŵеԁ`Έ\x89г˯ƱĜɃΑ',
                            'ʺϗĄȗпʷ\xa0ӻʓǧȉǊϥ˗ҡźԮѳ˫ӥƪƄ¯fƘΘǪjʻџ',
                            "ŊͽsѢCЯ'ϝ˷ą˫ŹuγЋŀŢǽѮµёŵҬЅU˝ĉ[Ʃ҈",
                            'ϙqɱԪκϮДҏƎҼʸfΟϽщҶϘ&Λȩqȣɀ\x87ϯΫīőƣз',
                            '}ǍϧӲĤÊӐĸʣԆƂԦŚ˂ƅРԡǊÂЂ˂ϛˍάƬ_ƥȟȵȦ',
                            'ԃˊ҂˳ĲpҤ˂ϫ\x83ћ&λʔ˴ҳэĨˈƘЅ±˱ŷԠÌƸ\x9fӦʛ',
                            'ΦʈûǼʦωʘªľЌɉЦΉĮхΏһţ¢@ϠƾǌÝ0ĮПÃԟȹ',
                            '˥Āg҅ŭэˤɓ˫ОϱэˣFʽЫˎғěƞ;ʤ¶ƲżӽҁaȂé',
                        ],
                },
                {
                    'action': 'ɣ\x8dcîRӖаɵΈ΅ȐοѸЍҺɜƐΧϯњêǾϫѪԀ˯ɏǖσҍ',
                    'resources': [
                            '6ƕʜǮŒƊИǚƣȫĀζǜˆŀİɺ.Ȃ˩νÉҦѬƒ&ˍЄȈЉ',
                            'ƵѮeŲͰƘ;ƋќȳϒѧŻưĎɺĚ\xadȢɖÊσП\u0383ҹѡϳћȃj',
                            'ħ¯ɯЀũ¼ӅхʌҲ.5Νŗ\u038dȸưʘҳzĭëȽі].ѱ?сџ',
                            'ϳӑюĻǧҊԗӁǨΥϯˀˮўɚû˝ˊŰ¹ãΟíԢǍΗε\x9bǪӞ',
                            'ˢҋӱģȖԢä\x90ȯR³ɂȶ+ĳ҇īӮͳҥ˴Sɸ˯иâȩʛȍԒ',
                            'ȷóˇ\x88ȿołΘì˶ϞҮˣʌЩ$˚ǀϭȬε˒ŌȨĖ\x9dӛΕӤ\x93',
                            'ǥҼ\u0378ӆϢГǪÅŭ7\xa0ŞϲϷƐϞʍǧΫѕɰЀÝ5ѭʌѐƫɸč',
                            'ȉȪȭȥƋɠǇ˴ʽКЌðкӢě\x98\x8dQ0áĚЃǌжîν˷ʆŸʔ',
                            'ӺHɾ_ʸѩƑȝƐɔɞчʛʔ\u03a2ɊȷƖыǪΣXǟԕϒOйѶƗɁ',
                            '\x8eǎӰԇ˵жêˏг/N˭©L\x96²ѡҙÛɅҲԎњxyΖŃ8ȚŜ',
                        ],
                },
                {
                    'action': '϶ЊиǂіvȖ0Ӂæԥŭą>ʸɐǘҁsȻӀ\x97МѪ\x87ұȆâԝʥ',
                    'resources': [
                            'ОϥĚ%ǝʊʟԒΝҳҽӋÕͿԗʋì;%¯҂ǃˣ˵ұϣͶʖѯ¦',
                            'ˏԕƑªҼ˅ΒÇǝ¬Ĺԇ˳ǝǵνɌǸίŹÓƻԣȶʴӔzͷθî',
                            'җЇŀįįӀ',
                            'ȁЄ£ҥΕҥВ҈ЄƊŮȚǎЇŚɯ×²ҶѢԐ˫пϕν\x9fǙʡԏâ',
                            'ŦJΛϺрĄϱɪďЕÿˮŐҡɠűβʐÿȵƮɣӘѾɦɻиӸ\u038bƗ',
                            'ĮԭʀѺΌŷ\x91ΣÌʹδϽǎӇœƙĺѝҨąѲűӆàιҽҷɡ\x81Ԛ',
                            'ӥѵĎϦӋsőǊѸҶƈêʓоʸ΄-εмɇЋ\x81ҩűHʝԪ˱ɊǶ',
                            '1ŵMԜĞ϶σӐД҂˪ųӹЇҟҿ$ΨԗрЏ7σ9шûјĽǦŵ',
                            'ʮ¤Χϙ\x8c\x9aέԦèȭθ϶Ԃζˌĺ˕ǬŃӭ¥ʇӉϊԧłȶÝӯĂ',
                            'ɵȎӤ\u038bɦ¯ÖѾґҥӨ{¬ӫԨΠŐH˕ƹϕƌ¡ϯӖҶ\x91ԌВǏ',
                        ],
                },
                {
                    'action': 'ˑɲ¬ϛξȽâ;ҔȡâǵķɠȜĺˠλRąԮϟTĺǺˇӀ\x91\x83ԥ',
                    'resources': [
                            'VǏ҅˄Ȱ˘ҳ\x97ƛϡʞҥʘԫàƊƨΔˌˢʱξ\x99ƦȩưɝɋƗȟ',
                            'ȚʑӡӄЃӗȑ\u038bЅťɱμɩþɡ~оmɇӨӼЪģӸĤ\x91ɿΉŭČ',
                            'ÖĐǯÃǪǝÏҥWРИ\x97ѪԐӡ҉ƤЈҨʾȈŬ˹\u0379ԣǕ5ϻŦȽ',
                            '³ԗÛí÷éʺΏÄԬҰӳ"сɣӨӸǷϜÊѢɟЁǅʉȃÅϸҢǠ',
                            'ҔʀɬԤҒñŻ\u0383˘˲¥ǈӛɖ΅ШыѽþǰˎϿНҷţӣЗѢɀL',
                            'ȹƹӠǀÅҝа\x80ÃӮҍуӃ˚΄ԡ\x9eɏϚ)ʵŚǣŠʚ˂ϥѓӫ8',
                            'ѨӆԙƾěΥʲo2΄ªĂ˝ѐҟ͵˽¡ӛϖ¬ѮұĞēǆǬġȑԨ',
                            'шϩ϶ϼЃėɹ˂ҸѺˁċĞ!єӥvӣƤ=ԬŴˤбʽΉĳʟˢ˟',
                            'ɰμ\x8cԖҘʐΝ\x85Zü*ǑŽ\x81ſʾ3řêʀӫƊoЭ·Īͼ?Oԧ',
                            'ϹȉŇȌѧαŹʒӢԔƬ·ҡǯʭϰYŢŁȞԙԩԌӚ\x8ešƹϷІÑ',
                        ],
                },
                {
                    'action': 'ǨɹġʾЩ`ɕÓɗĈȝòї˔',
                    'resources': [
                            'ҐͼÞƪӹŉƀˬDԢǗɔнĬӖƻi˰ǖȔŢΎȹһЗѮĞͷϑu',
                            'µ\x84ʸͱҍɌőǛѬś#ѠĿӄǠȔèқϬäҊ҂ĉѾ\x93AӀҵˈP',
                            "ăƝÕȠҘҕ˳œīӿũԇσ ÇѬ7ÎНƫηɩɌļ£'éΗӓӍ",
                            'ϸɽԐˏŽɃϗȥȬÇϖΧÃʋɮ¹¥Ɉ©Ю0ĐʀĿЁɣ\x87ĀѰŋ',
                            'ȆõБdʲɼÜʆËѺ¬ç\x91ùɝþēѹməͻΛ˰çћӑțʗ£ѹ',
                            'ȤʹȊыŕ˵µȵхʭԓŊÄǬҠõɧԨϟǝγĲƾϚɉД%Ȫɬə',
                            'áЮǨҀƂŎ-Ʊʸfȥi\x88ˡҽɇǈtӯgɫǮªˆ\x96=ЁˣˡÌ',
                            'ǯ\x85ǎ˙OΥŁѱΛPǇ2пαĤſˤį\x92/îʠ/ɍҪŚ&ɞ·Ϗ',
                            'ǃӯҁɢɭǌɌ˘ҜłĲƝ҃хɆŀǸˣ\x86ƹʭәŽиɣ\x8ae9Į\x8c',
                            'ˀƪϝǖӊƵƴ҅ώRɋ\u03a2fĳƌÈΙ4Ԣƺǭ¬ӿǵÎҥїӠ˛ģ',
                        ],
                },
                {
                    'action': 'ǛǐĢʻϓɜɧȝ|ɳϮƍǜɓћ˵û{µŪǞǦ˔\x94Ҟ҃\u0379ЬVԣ',
                    'resources': [
                            'Ԟ˫ő}ԗХѳʑıʽ:ДƝkӇe˱ĲƻŪϞϤɤʯΉӑӖЮȨΧ',
                            'ӒˑʣĴ˷ЅТύ\x84οŌαœªŽҷƇԤģҩgԚʕ\x90ˇyБкʘ\x81',
                            'ǎӭÃɛ»϶ҙƺуǬԮӉщ`ȘѱԏńЛ˼ΉȤ˔Ԓɛ%Я˹Ȫȸ',
                            'ʭҵԁŕԖ\u0379Ȧҧǻ{ĚϽƽˬѱ˷ǃаɚç˧щƂǬϘ¢ϖ{Õǡ',
                            '˯ƿԭӓ˭˜ɻŮǅǄȰ\x8bǠ\x85фҮҬҴ*ȧӗã3Ϝ\x8båčƐąɇ',
                            '½œˈҞPƘΒĆÔēÚϹ;ӭěҔѓƙɤ Ĩ¥ʫҕƑčӤ§ʭį',
                            '¸ϭҊàƏȶ:Ǟ6ɲɒѺΖԭqɯť¯áȶơȴˍƷҽɶǷѕҧɡ',
                            'Âӗ*ΥͿŧȑѦ˖σө)ѭѷԊ\x8cŌљΰӯɭ2ƥǵǍǶoΑϙ˄',
                            'bƕsƛ4Ҁ/u²BτΫtǿ.ϜӃ\x9cƺҍϰβŕɹǛўЃɾĨƲ',
                            'ŋͱӶђɚΏêϔƗʶŝӂԘƆ͵ІϣѹŜʕÛԍÚɺxӚѰë÷ԍ',
                        ],
                },
                {
                    'action': '6éӞʳͽȷʓɪ˂ҙƍѢƨŲÔȫ\x95ԟǠЅͳǪĳǙ҆ʾɷȦƟ\x98',
                    'resources': [
                            '¬ҽͽ\x9fʻ\u0378ʑѦ˶ԀӔĄbȞϧ%Ӛҍ˺űɕ\u0380лʬԋńƇĹԜš',
                            'ńŹƛΫͱŁŭ\x81ˠԈɕɲˌϒәӮŌԮ\u03a2ҡҮäȄȁ±ð\x84АϑЪ',
                            'ýѪўŨʏŀΚøÉʡωҔĄρļҭǢĬˋȀυÖӦŏϗƷūϗʞȡ',
                            '\x92ƟŎчȗѢΑƔǆʊϏĮʋRʒЛеRοӿŏȵˎŋϦҼώ\x94Ƽ\x7f',
                            'ҰȤTϮĳίůӝŀmПſȪÑƣŇŷҨƅʧμ˒Ę.dƒƫů{ϲ',
                            'ʨҏȣαƪ˧ϑĦȫҞƁĖǵƮ˽ùťѺÈѳ˛žĩϡӾñģШ·ӷ',
                            'ʋϱĞξ¢ \x92˝рƊϰQȢʤʡkŻí¢ԫӲ˶±p\u0383ӁʱǜƔԟ',
                            'ЮԢɳÀʆӊ1Űͽșӫӝӯ\x82ӎhҚͻSʾχêԗϫƏΎƙχ˗Ɂ',
                            'ѯΐʻѦʪʳЪǬσúԈҙʠӿ\x8aΐ˷ɠϻƉˎԌȪёƊњɡ?Ãz',
                            'йПԊ җɰĥӂΙсĊªőłWŀӘѓѽǮΖΗǞTΞжȉϤ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'kʳÒ',

            'launcher': '[',

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
            'identifier': 'ɪȫˈϘʀŋ5ЉсɓĐϞʦŏЫҾǡÜȼǪģȮŖД¨Ӱǿ¸Įŏ',
            'target_id': '҅λ˹ʡn˘ŪˠɔΘɰӿɁîǵ5cȬ©ηbɮčĩԥө˘ϻʇǶ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'эiԝ',

            'target_id': 'cΟϫƝϯ',

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
            '$': '˷\u0381Ġ˜ΫȯӿԒщč!ԝӺӕĔӚʢɶŸќɣίӾȜӓ\x88ćɤҷf',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -7919405047822893340,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': -16078.694139390544,
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
            'identifier': 'Ťэûδ\x98ǲξ˸ȒēǄˊǥѻԣʹӇ×ʥåůƎШ҃ц\x84чȾɏŻ',
            'source': 'ϾˊxχʧƌПҋЁŧÔʨʼΣǟ/ʧҴӍԝςψϠԥǥШѦӘѽî',
            'message': 'ȴφԙ˾ɘѡҸaԧůηҵÞ+˃ƻϠéϯɖэѱО˃ǡɞʪĕƎǼ',
            'arguments': [
                {
                    '^': 'float',
                    '$': 357083.19601914735,
                },
                {
                    '^': 'string',
                    '$': 'үQ\u0381ЩÜȝɚыGõԟǻΉť#϶ҍùȵɮǡ˻tԟŃ\x80\u0381mҘ˓',
                },
                {
                    '^': 'float',
                    '$': 710506.8202623221,
                },
                {
                    '^': 'int',
                    '$': -7610405580757121697,
                },
                {
                    '^': 'float',
                    '$': 369785.01518282207,
                },
                {
                    '^': 'string',
                    '$': 'ʋʕǾόɃːҮԑЌü.εЃϥĻ-ҸİЖT\x9c´Č',
                },
                {
                    '^': 'float',
                    '$': 500119.6941957944,
                },
                {
                    '^': 'float',
                    '$': -81155.90096576702,
                },
                {
                    '^': 'string',
                    '$': 'ʌҊ˦ŝŇƃǕӜжѽ\x9a˃ѦΩ҉ӈǂǗΗôɾтӆƥķʧΤкαƃ',
                },
                {
                    '^': 'int',
                    '$': -4051410360662205304,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ЅǾ',

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
            'identifier': 'ėńіƑҪæƷӪԤƠΙҪј˔ŵȨŋ҈Ìҋʝеҁɥ˧ϿҺЦƁǧ',
            'error': {
                'identifier': 'ѢŚӣΒ˲£×әӹ`ϮҲϢҧ5ɶƴ¬ʅԘ˩ϦŠԀÆЈIӅҩȠ',
                'source': 'ƃφ*ӂǸŗóϯ˻ӶX˳ӌƑɎʲӱƊƅȆЦԊŢгʷԔԩÇǷ\x8d',
                'message': 'ͳȮǀˌ7Ԟ¥ͱ\x8e҉ǣȊœƂ',
                'arguments': [
                    {
                            '^': 'string',
                            '$': '˟½ʹ϶żψӲЍбĲυPǾǕˣĭѼ҅qĎɳϻԒ¤ҌȦēĻ\x9fӢ',
                        },
                    {
                            '^': 'int',
                            '$': 4255271647631916601,
                        },
                    {
                            '^': 'int',
                            '$': -4645981342613947104,
                        },
                    {
                            '^': 'int',
                            '$': -150374213404648417,
                        },
                    {
                            '^': 'int',
                            '$': 9223350976605217413,
                        },
                    {
                            '^': 'string',
                            '$': 'ǭЦʝǦr}ȜǙѪśТҿŷʱіҭǙėύеԞԎͱϥǣ΄ѫư\x83˽',
                        },
                    {
                            '^': 'string',
                            '$': ' \x94˪SΥӉų˱ɱѹБԕˍƊАÐťήп¸ýņѸŴë,Ŝʒ',
                        },
                    {
                            '^': 'float',
                            '$': 292154.00088539225,
                        },
                    {
                            '^': 'string',
                            '$': 'ԈЋŀjԂæŖ˫ºдԀņѪТNăɴ3ľԓʿˏŃӇӧӳʟӅ[ʃ',
                        },
                    {
                            '^': 'float',
                            '$': 589241.7879053782,
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ҹÏ˯',

            'error': {
                'identifier': 'ƃΤ',
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
            'name': 'ҤßȭƧОѻ·ϑ<ЭƁƇƕ',
            'version': [
                7643320376367344275,
                2008969098373516674,
                -2597197308094582065,
            ],
            'location': 'ЖϹŢӭЖНǪԛŁ|ъªƷыƟ˞ҙɟǜ˼\u0378ЇŗГЈԇŖϘʢʭ',
            'send_access': [
                'ϲԦЖΚȨĒǏƴȼȻˇǃĔŃćâĦΎӄĞƔšƶӺɞhӧр˕Ҭ',
                'ƣԞyǗĀĊ¼Ҁ;ЫɯȑΚϚ ʣԄu҉ёÞďƙԡʯѢєͺȬϝ',
                'Ȇ\x8fɡȠ\x91ËѕӭѺϜ\x95°ǆĠҷ˦ĨΈɫă5тҦʁƅäżӧѿk',
                'Ƈÿͺƭ҅õͽƮÑӆϣŶ\xa0Ɯ>ʀʕʤѓ\x9bԀĕƫ=ԘѨĤ˰ĸ)',
                'ǱǣØʔɧʌЊȌÂӌνɡZԋȱ\x9a˟ʞϬʻƞНҖϩˍÅ¨њȝ^',
                'ӢҬɷšʎƫƸѯ´ӷоχҞɠ\x9bΌ`ƈ]νӫǚÜӗȿԩϽȳęÓ',
                'ԎϺƷˬəпӈЦðеҠVʐɥԊƯţӜȖХϤǽ϶ϗ¶ǢŃŝƊŊ',
                'Ӑ#ǟµvɫƧ Ȁƪ˟Р(ĜƓäҵэóŠ˦άĦĸ¢ΆÕɆЏć',
                '˨Ԁъʳƕрʂӆʱ°ӹӚЀͶЮҬIƯj\x9aӆѰхҾςşуɚǒĮ',
                'ƋǏzȣԙîȏŽʴƘӚnýȖƌ¯ΏσˢƫҴñ\x96ȬԚʞÂƟϢӖ',
            ],
            'configuration': "ԩƨęλÎбѪ'ȚPʕĐíƤчǘĹǼѨΝљΡȥƪӡǇԍǹ˔Į",
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ԝӿе',

            'version': [
                7008873351206914174,
                8220874821353181967,
                -7891037653259929192,
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
            'name': '˗Ϫ"βÙԞΟʌƦDўȎ=ҬțƫȢǊ΄ЄΩšěөɋɨ҉яВȜ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ƱȄă',

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
            'name': 'ɵzϩƵʠωɱψΥǥŏ¸ȩˁӐWđԒѩӊėξͺӝΊѢŊȋȢϋ',
            'error': {
                'identifier': 'εʕȋĞӸʘͻҖˬ˸øҝɴЖҗ\u0380ƾ¸ÏѶMóЉɚʹĶ',
                'source': 'ĕϢҼ˥ϒԇÛŔЅûǕЊfϊѫ\x7f0êϑÚáʑÑɱʋɡƤҀҴЇ',
                'message': 'ĽŻҰõȫ}ǜɔмϙȽȅÛ˷οƧџȰӧΏȶʴʂWϘӓǖʕǻѳ',
                'arguments': [
                    {
                            '^': 'float',
                            '$': 959145.4491728023,
                        },
                    {
                            '^': 'float',
                            '$': 233540.50626203942,
                        },
                    {
                            '^': 'string',
                            '$': 'vĊɰɉ\u0380ҚϿʷѰŐӾгÄЉƙæ\x93ÚҠ.ҕĎȢͼƞƞΦƉŵë',
                        },
                    {
                            '^': 'string',
                            '$': 'ó',
                        },
                    {
                            '^': 'int',
                            '$': -8325232427916586937,
                        },
                    {
                            '^': 'string',
                            '$': "Μ҂˜ϷŝѶ˭Ŝ\u0378ĩԌĳΐ˭ԝμ'ӒГƮɕźȲѴĺƋĥδӟ!",
                        },
                    {
                            '^': 'string',
                            '$': 'έŰĮ~ӴϏАͷҴЯŌˆϧĠʶöӫÃ8ˬԘƟǳ«ǳŤӼЊβҕ',
                        },
                    {
                            '^': 'int',
                            '$': -5642103293363327039,
                        },
                    {
                            '^': 'int',
                            '$': 2350965789418035967,
                        },
                    {
                            '^': 'int',
                            '$': -3443830212610611683,
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ÿԍү',

            'error': {
                'identifier': 'ĘӺ',
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
            'event_id': 'ɗϭĩǿѓʜγҭԌҟԦκɌʯɈτƃðӂʲΜԨſÎʳОԇɂʣү',
            'target_id': 'Šʀʃњчȼη˝kӵԁϿŕԋҢëҚʹҒǉͲӬĹњqӌɯυáљ',
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
            'extension_name': 'ĵưӊƩґʭĮ¦ɳ¤\u03a2θèś`ɜκėˊı·ʕƬH\xadɁ"σѨȑ',
            'events': [
                {
                    'event_id': '¤ЃΫξҧrÞҡèτʥʣӎɱ˞ϽċϬ\x96Â^ͱџҿʷ\x86вĕɟΪ',
                    'target_id': '7НЋʯƤЃ´\u0378Ӹ8ͽĞԈƌ\x8aŀɍŨɱҎ',
                },
                {
                    'event_id': 'ˊΔΟǣҧισӃȥΟƎпˍǠƧІё «ɽɎϭĂϟʋͷґuНϵ',
                    'target_id': 'ƮǅCҺɣř˨ˉǾѐÞÇqÍ+ʝғƝɻѸӘ¹Ťĺ!ǘ\x9dǾâɖ',
                },
                {
                    'event_id': 'н\u0381³\x93І-ЦZюҸǄāɡA½ƘϒɷζɝūѼԘҮϴžƠ҆Ľĳ',
                    'target_id': 'ǒŵ^ίь\x9dļэаųѤƇЍТǐő˰ԍόĮԖė΅Ƌфδԡϔõʳ',
                },
                {
                    'event_id': 'èŹћ˙\u0379VԉаʁƒǈÞ×ʥɿїӕÍˣ4ҋЧϦҌʖηhǙӖǌ',
                    'target_id': '\\҃ҝőΥ϶ΫɜɅğѫˊѥɀǃϐƫҦʹӻЁ¬Ѯ^иʩŴΚƏǂ',
                },
                {
                    'event_id': 'ʈҹƈȹņ×ȏOɩҦQʶVɟêʦ\x94άҠƨČ҅Ӆǔʜϭʖś\x95Ç',
                    'target_id': '\x97ɞÛƗĒřŒԬĴȞȶδɒɾсyѳʭˬŜʟʿŎ҂èɆÍКĝʾ',
                },
                {
                    'event_id': 'ʊϴƈť\x82čɒӸUΦȜʜǏ˽юơȯʈ˗ΐɍЁԠƱ\x98ĨԬ҅Ϥ˘',
                    'target_id': 'ɖ«ı\x93üэċΦ\x9c˩úӢ;ҢÖĬŌԖͰͱºgϧƈҔГӼ˝С\x99',
                },
                {
                    'event_id': 'Η\xadȶљƏҼҬǹ\xad[Òƶ˶ъ9_˴ĳ®˴ˍǝeǔưȪФԣςө',
                    'target_id': 'ΆͷȿȻƬĚїѯФ\x83ωяňϽ¬ѶĳҤɃԘƷӓɫϤ҃śϚ<Ӝǽ',
                },
                {
                    'event_id': '»śƥԁ!˟ðӢðȯ$ӥ\x91ġʃ=ļʂѼˑťƷеˣʄȌкŇĻŎ',
                    'target_id': 'Θ˳ӨɒsøЋѝԙїȍ҅ьЌӳǂǼȋ|ɂѺ˔ɄǞӉȓȏːɵŠ',
                },
                {
                    'event_id': 'ǏѶƕѩҌͶťȗ˦ӥǓʧҕƽҗǻӷҿЄ\u03a2Ā˦ӡ\x9cȬĵнӝБъ',
                    'target_id': 'Ӫ\u038d¾ČȞӄҧϖљĈėЊ˒Ǟoӷјďӄµ˴ðўæ\u038bδȈ®ϗʣ',
                },
                {
                    'event_id': 'ѓӯ¤ϏZǚcɟ˛˒ŗ\x84Ȥŷ˝Ɣ',
                    'target_id': 'ѐŖΨÓһĥɶʳ˻±¯Ɍz¬ÒϘʓjΜɎњǫзȶŠо˽ТŋӮ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'extension_name': 'ӮӲ ',

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
            'extension_name': 'ԡҞǡΰƋϒі˷ǍӕęɼϽКƳЄƠɟУԏϾɸąPȅГŲøIƂ',
            'events': [
                {
                    'event_id': '˦˓їҳƜ&Έ@ĝŇːҘǇѯŷ>¢ԩĺԏæĒǜϿɅé{ъħӣ',
                    'target_id': 'ǘͽőҶңǽǜҘ˛ҕ\u0380ò˩ЇéÆ)\x8aİɝˏʗ\x7f\x8cŏұ\x8fīF6',
                },
                {
                    'event_id': 'ȝǳƔӾ˱ҿȄáǈѺȨ6ċŅPź\x83§\x8fұԑȞӟǣθВȅȅÆƚ',
                    'target_id': 'ӄNӄȔЗťӣϻƝƖùȮŉňȎӃ˲ȇӯӧ¸˕ѩ¢ƺŤсҶɻϷ',
                },
                {
                    'event_id': 'ΨŧЮѺиϫԦǈɌΔԏϧˇЭɭƬŶȣӜ6ȴƍː%ρʖɧǬɔ1',
                    'target_id': '¤ʀƾûӦˌӊЁ\u038bҭɅɣ\x94ŹBʼÂ\u0383˯ҀҐȌЊϽƲфɴ϶ƀө',
                },
                {
                    'event_id': '¦ɋǩ+ϾͽԏďɞƭάЉ҃Ӓ\x83ѯğɚǳέʥҧƗǮȊǌӲʓӗӥ',
                    'target_id': 'ѢĸŰNӚϢ7λЩĄΓԗ˒ƣ¡ͿͲ',
                },
                {
                    'event_id': 'ϏȨMɠԚѺνØһŉŸȕɰӄėİǏԬЁǗƮɁҚ\x99ӒɃǰƱʏƄ',
                    'target_id': 'ġƶ5ːѐLѭʨ©ϽɕőҭʗӢIԉĘ\x9cʚҕыȘǍЉÍīǆ˦П',
                },
                {
                    'event_id': 'Ăķҙϧ϶ђӰΩßИ˚ʡĜʹŖǀԟ.ʱˬĔԢД«ȂǣŠĴGƥ',
                    'target_id': '\xadҘʮɏ϶AĤȦѺӿҎԁΙǓҪ\x96сОȶkȷ\x93Ӹ\x9fÕȥȱʢӺ~',
                },
                {
                    'event_id': 'ϧπŬǴ\x91ԁʃСʨ±ЀӟAŨ˜lđØȃĒˠŷóΠәԃƩʲmѨ',
                    'target_id': 'éϖДƝПЬʻȴȏӋѳɺùȪʹĬµǜѤҀҬшʟKԗŦǱö\x99ï',
                },
                {
                    'event_id': 'ʹǥʐɲͽʠƀǷЊǾӞƙưĚÉʜǭ\x8e\x8fǁрiΧʷʚ˟ӎś\u0382Ĭ',
                    'target_id': 'ƣ\u0382ΐoų[ʤʙɁ³ūЉŽћ',
                },
                {
                    'event_id': 'Πȸŷŷ˞ɄǅƏлĆҦԚkʹƎ\x86s¦ѧȌȤ\u0379ċʡώΪɳʠɽ~',
                    'target_id': 'ɝҹXïњˢч˨ǷƺģӗԫӮ˳ӌïɻiûҙƝ˶\x8aͷΜɌ?ŸK',
                },
                {
                    'event_id': 'ГɻǉϛƗƟεďɮӢǓɿҩӽ҃ƢɻēçӠӟŊŶԒI\x8eǬxҖП',
                    'target_id': 'Ϥ\x93ȟƼv\x96\u0378áȪ˭ѫ˼ϒДʑCϔ҅ҢѴǸ\x93ӏú6ͳÊьƁ\x9e',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'extension_name': '҇ѐӋ',

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
