# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-03T18:04:40.485928

"""
Tests for the foreman module.
Extension petronia.core.api.foreman, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import foreman


class ExtensionPermissionTest(unittest.TestCase):
    """
    Tests for ExtensionPermission
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EXTENSION_PERMISSION_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.ExtensionPermission.parse_data(test_data)
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
        for test_name, test_data in EXTENSION_PERMISSION_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.ExtensionPermission.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EXTENSION_PERMISSION_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='action', name='ExtensionPermission'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='resources', name='ExtensionPermission'),
            ),

        ),
    ),

]


EXTENSION_PERMISSION_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'action': 'ǹИЯŻūŔϬ·ʊӫѹʺǵϙӈʟЛӌǘҨΩÅıƴӧy\x9dҙ\u038dԭ',
            'resources': [
                'ĨϾҿUŴλ,i3ĳԢŢцЦԥʝф˽ŕŮǍʉ]ɪčĹѢԜ\\ɠ',
                'γѳҥȼͲʩ/ƹфçİ*˞°\x80ҜϋǇʋÖѡʚìgǞΧȁĜŸ\x8a',
                'ȳɊ˵\u0381ǗѓЇӏѐɩǊΉƹχ@ƞϷöɑ!˜\x95ȱÐԔϘҚԄʫʮ',
                '\x7fǖȳҿķσ§ȎĘζȲǙyàƎȓûǊǗ@ŧ¼йɽʷή\x93ȱԮØ',
                'ȒˬřυјѠ3ƌӏφǱԋϑӏÖżŎҎĎžÇɵư4¼ʝΚɌɶƎ',
                'ýӪ\x84âϧӍҪɱҒѐǸΰǨŇыȿӺѧưhĂɭ\xadЙŖȤӧʉШȏ',
                'ӚŗǀЯЫѸϕˣКëʬҌˤԚάϱƘǣɱ%<ȉюĒ¤ԘΥɡɴɺ',
                'θϘ.҉Ƀ˅\u0378ƃōǛ˅jñOɓ(ƯʟΥóэǩȟ½\x91Ȩ˴˹ҜȤ',
                '҆ЫɎɎЪτ\u03a2ʝȹыcȨ)˴ӢēM\x9aƣÂέԦҽʏǩѹəεÛΓ',
                'ȯжȐРɱ]ˎŸӺɊ˃ɵԀŀϿQȚΰƊȕȚʿ\x9aǽȠ˔Љȫӆţ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'М',

            'resources': [
            ],

        },
    ),
]


class LauncherStartExtensionRequestEventTest(unittest.TestCase):
    """
    Tests for LauncherStartExtensionRequestEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LAUNCHER_START_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherStartExtensionRequestEvent.parse_data(test_data)
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
        for test_name, test_data in LAUNCHER_START_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherStartExtensionRequestEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LAUNCHER_START_EXTENSION_REQUEST_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LauncherStartExtensionRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='version', name='LauncherStartExtensionRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='location', name='LauncherStartExtensionRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='runtime', name='LauncherStartExtensionRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='send_access', name='LauncherStartExtensionRequestEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='permissions', name='LauncherStartExtensionRequestEvent'),
            ),

        ),
    ),

]


LAUNCHER_START_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ɹТǕÒȫϻϮ\x93*˯ΏԛλɿΥоŌŦNäȈɂΛƮϩΒӌȩ0л',
            'version': [
                -6360943668612853065,
                -8326967630345348153,
                -167741621735204716,
            ],
            'location': [
                'ɽÕLфМǘǝː҂ͶǷйŊԉЬѺ¤φӱŐϸзĤǼzʞˎËĞѝ',
                'Һ϶˼ģğ«нíӘϕҙ˾üŢƨˎΐ˳Ȼ&ǼȻśˉûǺпŘҗѳ',
                '¡ϷĪÂƠȝћϢΖ\x94cԍχԧǸɯӆÇMş"ʹЛŢɣјʷÀϮԌ',
                'ёȋȵ\x8c\x89ɁЍŘȕғşӈʜς˳ƺɦ\x9bʨQҋƁҜϨn˗ȶͶΏΓ',
                'ʆғtæԖČȹǢɪαɛȰǨˣČˢÑԟ$Ǉ\u0382)ьȯҳγëȮƤ\u0379',
                'ΪȧΓ˒ΊùҩѩĢĎƣӔȟϒƵȓŭ·ΰʛƿǁʆȒʋ$ӼԢǰή',
                'ȰѺҐɼȭάʠǶ?ѣ;ϛ"ŵӜӁ§ϘŶ˃Ʋyǂ˗ÇŔơӌЬE',
                'Ȇɤ¸Ұǆÿ˯ЇͰψȶԁϣұ ЂСғŅɶΔЕɻďƲpëƀ/ԍ',
                's/ӷǝȦǽáɭɰϵǥčҐŨѢѐȆ~\x93ō}ҍӍĆ\x89Ƭ\\ɪҦФ',
                'ź7ƶмÞђÉDʗ}\x8cЊôťßĘĢьƘѯX§űęНŉC˶Ϋӥ',
            ],
            'runtime': 'łĿɂw0Uҕӟ¨ƴ҄ñ˗ѕfÉŝǑѳʱʬϟːˠеǒĹƃʌĻ',
            'send_access': [
                'ϲƻŅ˭ɠƫ:ÁЌҭ˞ʯҙɕʩʀԓÂ\xadŽţѥӧȖȁùĐɯÕӽ',
                'ɓɰӿğΝӆԐЋǚϸȆҿȌƔʣє5Čε¬фϗƁŜËʓηжǶƬ',
                'ːΞϜģ¬¢ɯϛҨˣ˼ѰӋɤoǚјΒˠƫŏ¤ʐѪԥͷӚӥϫͷ',
                'ľ¯ԦțӆƭѤŅ҈ðưҭγʂӀ¢ƆоϨ&¤Ψʿ΅\x82ɶҳƯxǺ',
                'ȍɫͽǪÑXӶüɄӒʷɖǈɢÊ˥ŃŖʽÁ҄ñŵuрŗ\u038bԈǌҦ',
                'ɶНФϜø˛ӧ҉AĠґ£',
                'ʋƂƫвƶǜόŨвʋҒĘžğͻƣ±ϷӐ',
                'ЫǩέηĚ#ϕ˱\x9cѬ˞ƅǡ˦ˇLˎӦϡƛЌэŅʲΔнȹĖЙͱ',
                'Ƥɇͼԁщ҂ŋɗΘ˞ҏǫ,ʔҜŋЋFӆ2Ɩχʟƾžɿќòӏɵ',
                'ɺǸͺțɰŁŨȡƩǇŉòȉǪŹŶпƔɎԤΚΆԡȻЫζҍ\u0380ПΞ',
            ],
            'configuration': '%ŔЈЄųғǡťј%yĠȏωˊґѵŻÊĆʑƍĿԍˎ˟ȩǠȘɖ',
            'permissions': [
                {
                    'action': 'ҸŪʌƯҤӎ\x97ұɦҳͿҹѰɱԎЇɼԎv¦ŁёΉȞԒǠV˨¢Ϗ',
                    'resources': [
                            'ˬ\x9dӹ^҇Ӭ\x9d%¤ŁǞԉ\u0383дΒϟ\x83ϼ¡ЖȩЎ\x97ōӉҙŭϸ˄ġ',
                            'ҷϚɭƦωГԃĖӕƕύŏϦӚԞȨϳΎ!ǪҔʕÝʼŉ÷ĨśΒ£',
                            'ӎήӱԬϻÇȌʭƕĊ˶ēıΣ\x9e˔ԩÔWÞġҦҧҔӑԞ¾ł\x87ӈ',
                            '\x9bʹzåʹ,ϥӰήɑѾǾˆǋϋЧϚʶѥӛâ\x9bǀŀԎa͵˴Щԩ',
                            'ȠʽόˊόʢĠ˵şζ˝ӚԆ\x8c˲ŋ%ĔǦҞkӬʊĢκˑþOΰҲ',
                            'Δ\x8eɧλюΝʜԮȩˁοɓ˗\x8bҠтƗϔҞԩǐúƩθκCυÅҰØ',
                            'ʵɓăӽàѲ˶Ϗ˴ðҶ˦ΥÕˬ½ϐͳʱƍǶҰȿŌŒ\xadЮSšʲ',
                            'ʪҷʵҹïщԤǻ^ҎɗԏӯЀËɀԧѬ\x86ɓ\x93ÙӣԄʁĿƝϕȹ҅',
                            'ɞŀРƐͿΊǌǕΛˏԘÉԫʡπϫр¨ќ҄ģɖâɆŸϛ`ϕȲБ',
                            'πӕvƱй_ʠNʁҶĨҼģҠԢЊωƢνˬ˙ˬǅԫӓƻθΌʕќ',
                        ],
                },
                {
                    'action': 'Ҿӂæ҉ƐųԧӉȅǯΙĦ˳ƒɹɴϔÚĚˑӨȶɏÓˎāÂЯĂԥ',
                    'resources': [
                            'ɍѤБƓҾˇɔɏЄʷȻʋƂrϺɸŮһүƜотΪόҍƾȬˌƩq',
                            'ІŮkӔˣԕ˛ϕŎĪĨĀ¾ѼњŊʉŶ˃ʶ®ΐgɶɗЙȒȷ¦ǣ',
                            'ʳˋ˨Φǧ£ЬӓƪҙūǆȆʞġĳǷԦȌyɘːʬωǙɓǎӍƞɐ',
                            'IȅɱĞԙѦǌ4ŧηϢҵ*кǆͱŁъԈÿˉƻȄŔǜўβǯμ˛',
                            'єңͻƍҎ˛ѝ˕ѢÛűġ [αΆ,ȴçȾ҆ǢđǱ]ƅĲuϾL',
                            'ԧȽǴ',
                            'ȗ\x96ȉũȔǭҶԐͽZɟ˪ĉāöʸú˅˰ĹŠ˝ǀȝӾʣɬθΈѫ',
                            'ʮ\x94ǶVθHʹǿʅƥѝèÀ\x98YJĜÉʅʱĩģˣӷӜÝ*ːоĒ',
                            'Ș˩вϸȾWϘ˽\u038dȀИşЋƩԃӢǨѣԜŸĳŦϧĚΞɧʉʿŗʗ',
                            'ͻîɮԝ҆ǡ˥Þß~ҼԜHlжѹǥŘώ\x88ӒīƶǱżΎѶήƵĹ',
                        ],
                },
                {
                    'action': 'ŜêŕŘθѤ҅ɔɍȽċˢѠϼǅĺ~[ȎŻɕ˂˗ŽƮѓЍƉ',
                    'resources': [
                            '҅ϯӿͻЯӃb&ӃӾǬϳԈʪɳŦőΥʐ˃ȬĭЖϧˉżФtκњ',
                            'òǽqƈӹEϽȸȲ48ҖǥʍAÀѷʋśԝśłӧĨŻ±)$ӷÞ',
                            'ǶʽЊґȎЎԀңҟ\x8e˩øϥϞӳƌȖȑțԧӯĉȇԙӅ(ȧŝȊѡ',
                            'Йžƀ\xa0ԖÂÖҲ҅Җȷ³ȽҺԭ\x82þÏğЉ\x8eĚƈŖϮ\x86ɜǑʔԚ',
                            '\x87ġϓҏτǏ´АɖȄͱjǠ\x80η?˞ÚϭҪдvëʙŒȰκ˲˯Έ',
                            'ȽɄ(\xa0҄ɐØӴlόťƾGÝԫϢӳ;ӥέǗίċŘǱђȇͿ˕ʩ',
                            'ƥӎgӲӾҶˀ\x9aϕҖҫ˞҂ιɬčǩ¬ѮщƓɤΩӍ˭ѶǱӇĽ:',
                            'ŤêŐÚŁǻĴӖȠäɌҡBәǕǶ˗ƒƛϸӊɱƛȧñ¹Ǔ͵\x9f\x9c',
                            'öŚ×ѨȥʿģˤĚϥØϹʐş˙ơσʨԭԁƔǈ˪˅ŀdҀΎ°Ě',
                            'ŦȜʺʷ˃@ǱŠɷǸҋč˳ƂНˌőӦ·#¹Ŀ˽ԣƁŠɬħýÐ',
                        ],
                },
                {
                    'action': 'ƁԋƺëδσŌΖɿʓ¨\x9fFXңȢŏõ\u0383Ίӧˬ\x85ǥˊ˸ϺĭѶϹ',
                    'resources': [
                            "őӵďǐSˈ҃ЛëϠȒƁȹαϕ×ʤ'ͽʢʑΉτӕȩͻӮĥɟą",
                            'ϗƋǋʣӹ\x9cƼʈоæԆɨɪǭŐƨІÝʥ҃ƈ˛ГʦʺPы˒Ӕђ',
                            '\x9aҚЛË\u0379ɭɵԤȌΛйЍϳҗiɓÄӨ¤ÞЖɹgʅӨǛȌȚǛƪ',
                            'ʥŏÿϋͼʗѲΊІƴƘȸЇ\x84ǝǳњĐʅ<ĝʖʚϞƭѹэӼЦï',
                            'ėǓʜ\x9dȨŅЍӢΔЩʪήĺϊΏϿѺRƿƒҼПω\x87ƳĳѰŹΖć',
                            'ǥΪ\u038bȁѢęήˢβʟ˪ÌĔĎěǱɿԡЄҸ\x9fӳћ҄ѨƱʋѺӀː',
                            'ЃѰӷѮǸѯñΊÜѺĳˀǚ\x85ˠӺëԔζòиsɗʹҞԅϣ°БÏ',
                            'ȖʖÝǇͶȡʙ`ŚόμȅϷYŖήŚ\x81ˊςϝþɰȻˌȶõÈͷɰ',
                            '8&ǿ\x84&˚ѩʄϾ³Ěĕŏȿ}eɦʪ\x99ӤŐŅɫ\x85ϥǻÚԔќp',
                            'МǷâϗҴЭƙѴƽҤϱΥϴȠҺΝқԁмǙȶђαŽӬνԡˢƁΑ',
                        ],
                },
                {
                    'action': 'Ӳӭ',
                    'resources': [
                            '\x94ҟȥћϾȑϠ7Ƹ\u0378ҨԑӈяΎФΗϽ˞Ԑ˻*ЋŊ˹ÛL˘ԚЬ',
                            'ЪųϐȮȣǄӑĶɅлѭƿӫÉ҇QϾ\x99ŊŚэм˶˥˞ŴiԁQǊ',
                            'ˤÜƉԤϣмϱӷΙџԍ2мƂϯЕӼѐȶͻ\x8fʿ˂\xadșґ˫ìřΤ',
                            'Ļî^ǒ?ģΘńʆǦwżӱѱƨ\x9cĭò˱ӥΚ<Ӓ˃ӦД\x92ǼČŬ',
                            'ŦņƛΉИӌӻßϺň ϟ\x97Њ[ł\u038dɐ\x9dϱ²ȂϐʴϷƸһɣÂō',
                            'ʀƉʭǋѲƮż$nŨ\x8e\x9aɾѡSχʄɽʧԣ˗ɇŸ˝ĘºǍӮɐÐ',
                            'Ɂ|ʛӇˉƷβ3әʆ\x8aʊáÄüɴøҒԓͼʍÖř\x9fɗъɶɍ˘ɒ',
                            '͵óȬƛŒǮ¼СǝЏΞεҲÈӪ\x93\x9dΦǡ\x9cib6$Щ˼ȫԉЎ˔',
                            'ʯҡҴ\x86FʂȬƍѪԬȩĥäϲːǴ\x959ɍχţśĤˡ҉˞ѰĀӥʾ',
                            'Ϗu*qȹŉɝӝϏMdӫѠԀχɾӜʨȬȅŢΔ˔ӗϖƃņә҅B',
                        ],
                },
                {
                    'action': 'ͲԗӨŕɰˎ˩ǳɌҡǿԥνƣϑǁӬ\u0382χȺMӔҟδʳɧœǌ˨?',
                    'resources': [
                            '\x9dӖѩӬĆņǉ\xadɊìѫ¤ľǸǆǌÎϳνɖ¾\x95ȭƖԊθ¶ϝʽά',
                            'ǹǮЙӣɯԏϖʰͱӝчЉƭżӦ˅Ѷ«ŜЯӠґҨõѼɴĮ¤Ťǫ',
                            'ΝăҡlɁ8ȕî¾ʲ˃Ο>ЪπţƝǯ҆OпŜ˽`´җĒ1Άa',
                            'ҧ˗\x83ƑʾƤίˉƊȸ$ϸ˅ǅˆҤˏǰǚЏГ²ѭƐ˳ҴTϢӦć',
                            'ӎ˺ӲȾΨȤӀǚġ\x8eҤӟґʃ£ΚȿƝª\xa0ȖʜBϵƈћʮŲɶӧ',
                            'ʉҠyҽƾǆѺёłŨːEĻňàƕƝЌһƥϲΠЪ1ϹuɣŖňˎ',
                            'ɕ҉ŏŸŏɷЁȰȒÑ˩ŁĖ˓\u0382ǘαɈԡÆΉƟȊҔsɵ\x91ίѰҫ',
                            'ƮȲМœӀʯČŖΧLÌűʜЌҹǤʿĝмԡԤ˅\x91υæÊČƶԫͲ',
                            'ŘůúǓǒԜ˲ѻԆѣӇЏԩȒ)ƈΦЎʳƏʇ¢гъɄʐ¡ĲǦǫ',
                            'ɤҘ˕ѧάʲ˛ε˅ːaǨɟɏø@ʙԍіźι҉ǵ0ңӆ/ʜӏО',
                        ],
                },
                {
                    'action': 'Єˉԙ¯ɸίȴfÛεºʹΝҼԆʮĢ˞Īãӯб\u0383ɠ»ɕГӮԣɼ',
                    'resources': [
                            "ъfĪϘϢБìFųƻϚӌӱ÷ѧ{ǐωFĂ'ӞʺͶӄ˸ԪɍÛ7",
                            'ѳBŢχδԃŎũӅʉɺ˗ѰǡξŵÀǻÁӁ½őάȁʅ҃ȜĄγȮ',
                            '¼ɤt!ӡ\x9eˢѫϻ\xad§-ďԗԎ\x88Đ˒ȇƳƉŪʏ˱ʏÔЮȞÒø',
                            'q',
                            'Ӻųÿ\x9fЦǬӪÿΦƵҸԦ\u0381ńѣȸϑ3ϙ®ԃŔÚӽͼCȋƐ˸ˬ',
                            'ňѬÓӷНĎʣѨʚҥʶӋɍ˸ӿķҷ˱ɦyÊԝĿɷѨðƎƚ7ϐ',
                            'ƻβϓөҸƓíѱϕœǯķȥâȲʲŗŶƯѧʬһŚԗѕäȟãįð',
                            'Ѱū"átȞŨʽɋɆxïýɐӤӿϸӏƸoīρȢσdѤȆԗɲљ',
                            'ɯ;ŀҟaϡӚʏԑʾѐǰ˥ɾԛήϥǟ҅ǱŁ|ӂƕǪğŐŪƏ×',
                            'Ɓϗϖ©āǖɲўгébԣȍӞÅӻОɔѯΈȥīԉʜϲ·ˡϬʓƪ',
                        ],
                },
                {
                    'action': 'ůĠϒҮ$t',
                    'resources': [
                            'ѠҤλ\x86\x82ȺϩƶҧȒƆŦӃƚƔıƝԞɦδ:ҋΠά\x9c«ɴУpԞ',
                            'ҿˡŌϿ¡ĀďϺΈʘËҦ˨ϒАρşǄӓɅԖa˻ȦťßĥĂ\u038dʫ',
                            'аȖɓǉʼãШˤ"ΈѱɘόϳИϿҧȵϋɦʪÙэƒҹƞǡ*åΆ',
                            'шϥ!źԪƌŲťэπƉ¾ćϋˌNȭшаȈǡӖǱϓ¼ǋʫ\x8eQс',
                            'ɠʿʩǴǞτý:[Şˌɯǝ˹ȴЈι˞ϫ˱ů\u0381ŋԏõnäǾ҆ʋ',
                            'Ŝ²ăÎđӚηҳĜԘ+Ҫ\x90ȈGǢηѼѮԇҽǊϳ:ǅǋĕBĨφ',
                            'ѝǠ¨ӢʹΦεЧЧоҠǘâѣҳ)҃\x97˪ӏ.άѿϤɄʭԗɝԛȩ',
                            'ċѿŭʲҲˢϿЍԋ҈ȥӻαͽδȳѨʩ\x8f\x902҆ǌϭȕǏ˘ǵʖϛ',
                            'ҝȯγʓʴΌɽΩJԭо˳ҰbϳҎʢpЯ>ϓҜȴͽЩ\u038dý4Ԉđ',
                            'ɇ\x88ԧňpšɋ"Ӛ\x96ʫžҤʶ2ϳ5ɦҩ~ʪʈˊøȓýЏ\x802ɟ',
                        ],
                },
                {
                    'action': 'ŒˮȾżƚÍґFɤԥ¿˨ʲӇЧȴí"ǳ\x8bӳїǉˋĎ\x94΅Ӎ\\\x81',
                    'resources': [
                            'вϮӰNɼĲ҃ЅнŞ\x99ʭºØŢƃʞ\x81СѝûƤʀʥèŝ²ȃɞϿ',
                            'ƌӞ;цķȻҡіӣɒŹŞϻ˼ȸǂȪӚВҧҬŻǁ˱ϧÂκЏǺÛ',
                            'J~ˀѫ϶Ҩʲă҆ӷНɏôкXãʑŌīϿ+ӡƮȷβƯɂ˼ʼǼ',
                            'ϰĳηѨфŭӻЀƆĂʓпĳȤ\u0378ɬӯӠÂΤӟ\u038d҃ԒЅԅшłˉФ',
                            'ĹĖϥҘѩ\x86ʼƔίө½ԃǔƁԡΦ\x9b%īũ˸Äо\x8aљӌѳưԥǖ',
                            'ѬΡĠ(҃ΑŗöźӍžӫɾӭˏЬǺѲ^ӭˎӇ҃ӿɹːǥȇ\u0378Ъ',
                            'ȸлђǆȞжʒňŚ\x9cϗǞȒǿ˸ɌɖԗİиŤ\x9bԌНЎφӉ¸Ȩ\u03a2',
                            'ŎZƂКԌŦНɸ\x9bӃϊȽʅѶ¹ȹқʥěԡ˶ŝƎȄӼłЇƥİ+',
                            '\u0381\x8dĹҴҢϿɪ=РįЇтü˫%ǩԦСӰȌƲбØѪ\u0378ΌƗїδ×',
                            'ȂɍƩƸϛʋǺȃѯɅӗԫƟĞ˰ÍɶЏʉːӛˈҚ[1\u03a2ƻѢāw',
                        ],
                },
                {
                    'action': 'ʏ҃',
                    'resources': [
                            'ŀ\u038bkҾȘ¸ӱƋ^æʗЩӴеΜÏĄŹ:ˤČƗǟπұӡÉҊÚŶ',
                            'ǴәǂǲÎöԦƭǂҨɈϟ˓Ɋ8\x99ТхĂǳѰĠIɋ΅wɖΖƞͼ',
                            'ǫïƛ',
                            'ǢҺœŒүʸĬǿăӠǙÁ\x90ΔоԬŨ;ԞџҤjғBϬҫļɆˣǣ',
                            'ȲǺζһƨÍĂʢĩиф˳6ËȧȮɽϕſô˦ҀĨǘǈÏӽδųĺ',
                            'ʳ=ɱ^ɝԕŨǣèˇ˶ΤҩL\u038d˶®ʹҤПƚ_ѝ9ʇĉϺĠÃÇ',
                            'ѓ˷ҿхҍϘҤƭʤίƢϋщŵҚǹʵԚŏƄȨ.ҠͼϞ^¼xЀӟ',
                            'Ǵԅͼņˀ°LɇО×ô҉˘ЁϱѴéДҐφȓyʱœ»NЅʨŸň',
                            'ơȉίԭǳȴ˪ÀʧйǠ¤҆ƷϹԛĀϛʹ˭ї3QѱõɆΙƃʎѼ',
                            'ȼͽɽȩ\xadϯжŽАЩҸΚf·ǯFōˍwƾӧɊªʅŏŚԢϭʺŵ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '˾ǖɳ',

            'version': [
                -5143248499688431795,
                -446476216884826160,
                -7824316464234115669,
            ],

            'location': [
                '\x96',
            ],

            'runtime': 'Ǡ',

            'send_access': [
            ],

            'permissions': [
            ],

        },
    ),
]


class LauncherStartExtensionSuccessEventTest(unittest.TestCase):
    """
    Tests for LauncherStartExtensionSuccessEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LAUNCHER_START_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherStartExtensionSuccessEvent.parse_data(test_data)
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
        for test_name, test_data in LAUNCHER_START_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherStartExtensionSuccessEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LAUNCHER_START_EXTENSION_SUCCESS_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LauncherStartExtensionSuccessEvent'),
            ),

        ),
    ),

]


LAUNCHER_START_EXTENSION_SUCCESS_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ЪʪŸyɣЬáǼʷɱΤѡŲǓʸ˰ɵτπсϔ˕˵ɖíǊʱҐӲņ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ιɺ˝',

        },
    ),
]


class MessageArgumentValueTest(unittest.TestCase):
    """
    Tests for MessageArgumentValue
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in MESSAGE_ARGUMENT_VALUE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.MessageArgumentValue.parse_data(test_data)
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
        for test_name, test_data in MESSAGE_ARGUMENT_VALUE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.MessageArgumentValue.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


MESSAGE_ARGUMENT_VALUE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [


]


MESSAGE_ARGUMENT_VALUE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [

    (
        'string',
        {
            '^': 'string',
            '$': '<ЙϛυšūƕǱ˨Ƿ\x9aƮˠ\x83ЃPѫ\u03a2ŇоϸΉµƨϔƄҤŕηԘ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -2809246248724327097,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 59062.009003489366,
        },
    ),

    (
        'bool',
        {
            '^': 'bool',
            '$': True,
        },
    ),

    (
        'datetime',
        {
            '^': 'datetime',
            '$': '20210203:180440.434183:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ǣɧÚwʛϽĂʔÍȇƀҤˮȊΦʈǥԜҖӃĝΖЎШˍſċƍyъ',
                '˟Uˇøů҇ǹӡŭ{ÕɛÚԆγªӝ\x86ΡǺҿКϳͲЃƼīЀıɧ',
                'ɀˇƝʐƿƸ\xad˃ЅҾӊҒÉ\u0379ȵǹę®GªѯŢëæӗϮɝbʯΑ',
                'ňϴeäŌʬθëѨöϔɿуĔ\\ӾԧɽőӖőЩµωԧӮԈ˗ˢƇ',
                'ґɭưȒǫѱɻͷÀнҕŖӂԊδÍѵȹˍȯ:Ҵɇ:ӷÕϧ9ȀɊ',
                'ҪǈʽɏӡμЩӕтˤьӄ˚˨ЏѻʔĦʈҎɗҘн҄ƸˉȋϙԮԥ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -3405651279028242406,
                -1731565252109360218,
                -763395265864023052,
                5310122288152308249,
                -5919948433223013325,
                1541450778652002025,
                7814237849791002791,
                4780271939231615860,
                -3130052270912011265,
                -8372407182352915793,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                340896.4048817912,
                352735.7422179091,
                557585.6936849282,
                825666.9698324337,
                339687.2704069385,
                298758.7255512687,
                268270.1870599462,
                952341.4729471707,
                9051.038018829058,
                16517.064826856178,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                True,
                False,
                True,
                True,
                True,
                False,
                False,
                False,
                False,
                True,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210203:180440.434956:+0000',
                '20210203:180440.434967:+0000',
                '20210203:180440.434973:+0000',
                '20210203:180440.434978:+0000',
                '20210203:180440.434982:+0000',
                '20210203:180440.434987:+0000',
                '20210203:180440.434992:+0000',
                '20210203:180440.434997:+0000',
                '20210203:180440.435002:+0000',
                '20210203:180440.435007:+0000',
            ],
        },
    ),
]


class MessageArgumentTest(unittest.TestCase):
    """
    Tests for MessageArgument
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in MESSAGE_ARGUMENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.MessageArgument.parse_data(test_data)
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
        for test_name, test_data in MESSAGE_ARGUMENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.MessageArgument.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


MESSAGE_ARGUMENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='MessageArgument'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='value', name='MessageArgument'),
            ),

        ),
    ),

]


MESSAGE_ARGUMENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ǀюÀÃÎʭԁĦʋӄ>ΉҫԦĆӶт˦ͳӍӎРѝьĘΩ˅Ǚ¾ǆ',
            'value': {
                '^': 'string',
                '$': '˝9ɨ)ǲĮɛĐǫŝɵϰƩҭ{\xadyãǙʇθӿЯ\x98ǝ/ΏŜҰŌ',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ƶ',

            'value': {
                '^': 'datetime',
                '$': '20210203:180440.434038:+0000',
            },

        },
    ),
]


class LocalizableMessageTest(unittest.TestCase):
    """
    Tests for LocalizableMessage
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LOCALIZABLE_MESSAGE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LocalizableMessage.parse_data(test_data)
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
        for test_name, test_data in LOCALIZABLE_MESSAGE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LocalizableMessage.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LOCALIZABLE_MESSAGE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='catalog', name='LocalizableMessage'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='message', name='LocalizableMessage'),
            ),

        ),
    ),

]


LOCALIZABLE_MESSAGE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'catalog': '҅ƂЛśȾӜљѦȜҠ$ΈȰʼƁƆŅ\x9cǝȼΫȚΫҌɠʒǢԘǝȬ',
            'message': 'ȀȷȫФYöяġȵ¯ŕxҔϭȲѓƼͼ˜,йʟӐӝˠƚͲƓѸʄ',
            'arguments': [
                {
                    'name': 'ϓ¡',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ƚīʠ˓\x9aƏ\\҄ϋȎč˰ǪɴPҜʗůЂȌǘҸљοΡΉӄҢÈ\x93',
                                        'σяÈʮµȩ=ҝƔΚǴøýόж¸Ļ.ZѱΠ½ƹȏϸƆЀFɲ>',
                                        '>ͻ˖ŁӝɵӮŲƪÁ\x8eԅӶҟ\x86ßɷCѿ0ɢĖљƝNԞϐɠʶʷ',
                                        '˺ѳǷкȖğϲŻţΐӚǘσı˃ϗ\x97ŋǅ҂[\xadǯҘЈ˄ӷ˻ǾǑ',
                                        'НĦӼыȟʨЩԣęɬҠƹɾ¼ƽʁʂβƕˠʢψǵИ«ѴňƌÇʓ',
                                        "ҳЀӯ'ʁИķönǒ˧\u038dɌÔůɗΤϫӻº˅\xadʗҌв˃ϱΗêʟ",
                                        'ĉJҮѠϤΌф7ľҤ;ƔÛΠϊΝöʕ˓ɇϷʼĴɂȺχǄŜԇŢ',
                                        'ѶƭaçĔ¢ƃИȃ˦ǐȳȃѩ\x94ɦřʼšğʼʍÅǤѶѫʩ\u03a2ђ˯',
                                        '˄ɃϗчþϫӲӛ³ΗȽƨЫӉ˘;ʚMӲӍЈ\u0383`\x9eĚӸ҂ʳȶŗ',
                                        'β©шŭΞǡҙææƁәƩ\x9alГӜƃ˃ƐвİǘĮϚѐńúǖkї',
                                    ],
                        },
                },
                {
                    'name': 'ͺˢǹ-ĺŚyĢΣѾϘӠнǖ»ӷŏͻаŨчʳĲКʽτȔǸPÐ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        192466.08393151994,
                                        264050.44170538476,
                                        856463.0182525825,
                                        133073.77459840523,
                                        10474.195360930913,
                                        614875.0552946209,
                                        752855.2441420587,
                                        -1228.9823254448565,
                                        102154.11809483811,
                                        31546.282784891053,
                                    ],
                        },
                },
                {
                    'name': 'Ȉ\u0382ϮυϮ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        False,
                                        True,
                                        False,
                                        True,
                                        True,
                                        False,
                                        False,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ǥŢΣˈ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -5243728078100187327,
                                        -2535107351614542482,
                                        3131294693977695459,
                                        4946056970451580818,
                                        1146238230039346335,
                                        8727854132067335231,
                                        2824216221237440412,
                                        4932987294660025388,
                                        5781963410776520042,
                                        8714592191296897929,
                                    ],
                        },
                },
                {
                    'name': '¯gˠĩʙĬDƥɌǹǖɝӳʛɈ˶ʘə¤ǋԫǡΗ\x86δȒĚҫīǮ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210203:180440.432383:+0000',
                        },
                },
                {
                    'name': 'ɧɍÆ\x85ǗÆђΜşЎǾ2ÁϠσƩ\x9bТʗǆѣâҿԢҞΨĴϧέ\xa0',
                    'value': {
                            '^': 'string',
                            '$': 'ЩńδГӽƥ\x8eŵēӹʟ~ąʁѩȖӣƥʑʯЈѨ·Ϫ3ʹȉMʤʂ',
                        },
                },
                {
                    'name': 'ȻɸƚΌҫɫӸӌġоɻәŘϏȅϖwәȸȡΪ',
                    'value': {
                            '^': 'float',
                            '$': 46638.98364581447,
                        },
                },
                {
                    'name': 'ɹҸɬлԦҖèТÙň',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'wЧϏЯͳ˪ȸԅȚοʱcɔЭʄљľ˃öĊϦô ȯʛɀ¦˭Ġϓ',
                                        'Ѩ҃ǜЙĴƻԐÅɅƿӬƕҗTήΦƣΐɗ\u03793ВˊYԠԄѿđÀƍ',
                                        '\x81ˣϗϞkӾƣԑČųϿąѳ҂ī¥ȰȜȄдь΄еϐӛøҽɁŴ˺',
                                        'üXĹʤ\x89ʱВϢϷǐɏıǬ²ԝȭĶǏԉʊΕΞοʧǫαȧљЯІ',
                                        'ŝοēϕǐʨϞtƋǘǜƖŊŰˣǆҰƏҳВӯƴяgҸȋǒџԝâ',
                                        'Χǔ·ǟ҇ѽ\x82ǝϝȊʫǗ˜HȬʭʰѺǬ˄\xadƭĵǹɝǹϡϋʡϟ',
                                        'ҌѤЌɓɒ\u03a2ԭǀѾϮѻœҘõyӯӷӿӡċԢHȺˢǩԂŇȕΖȬ',
                                        'ĊŏÅƃ*Ħ˴uκĒоюƶӓʖ«ԦʒýưïĔԈȿΧĜʴȐ;\x90',
                                        'Ο˪ɾҟSȖӃљĚŅvɵѣĆҙЌū\u0380έёќΦ³\x8eӒȍüʮԠə',
                                        'źИҬŔƲϐƢǛʆ\x96µΑёѶĨƉԬФ°ŐԩņɚЇɘõĩѰǲǦ',
                                    ],
                        },
                },
                {
                    'name': 'Ɏƥȥ',
                    'value': {
                            '^': 'string',
                            '$': 'ǄƷĈПʎȚĀΞɱːҚȗΤ˵dϜҊėэƞ7ӮR¦©˺ԆƨЉũ',
                        },
                },
                {
                    'name': 'rѫʵїѡЗǲgҪҚɾʺ.ɋ¹Ήówɬ¢~҅ӽĸǕ}ˊƂɃĨ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        True,
                                        False,
                                        True,
                                        False,
                                        True,
                                        True,
                                        True,
                                        True,
                                        True,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': '*ԧ',

            'message': 'a',

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
                dict(field_name='categories', name='Error'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='error_message', name='Error'),
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
            'identifier': 'Ĥ΅Űď˱ŀƘĶʜʁӀҽϾöµǠĻ(ѭȄЩ6ɬŧUǎʓŨҪż',
            'categories': [
                'invalid-user-action',
                'os',
                'os',
                'access-restriction',
                'network',
                'configuration',
                'configuration',
                'invalid-user-action',
                'file',
                'file',
            ],
            'source': 'rʉ@Ӗɮ˷ԗȆdИ¹ȇɳǆɑ\u038d˜\x93ĀŹЮȚŤȠΉ΄ӵαɾю',
            'corrective_action': {
                'catalog': 'ѤȯʲԌˇŝžÛĂҒü϶ȆƗƄʍύ1ԈɉʁzӘпƺ$ȘӟƗ˹',
                'message': '˓ɳƘά˗ΕʘȭeΣĶNȑВԟЀ»ίң$кʻɤȓËѩѓŋŏɏ',
                'arguments': [
                    {
                            'name': '+įʊɌͼÁǜʿЉYïvҍÀȉͲƼĨ¨ºʞƊІ²ОǥɉЄӔɝ',
                            'value': {
                                        '^': 'int',
                                        '$': 2022187636269937913,
                                    },
                        },
                    {
                            'name': 'ȘʌȂ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        33272.57851898318,
                                                        824494.4056523098,
                                                        423096.06319684297,
                                                        936779.7685194244,
                                                        36322.911460813135,
                                                        286473.231929821,
                                                        813005.4901176766,
                                                        873335.0699484808,
                                                        930550.4857702084,
                                                        763651.8990108747,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ѾÒÔԇ\x9fő˶ϐ',
                            'value': {
                                        '^': 'float',
                                        '$': 993126.9091920981,
                                    },
                        },
                    {
                            'name': 'Țƫ^ϤяΤ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ԕѮŤσѫ˝ωUDʫŰȷΆЏŽʯ8ЛɭɼͼÉ',
                            'value': {
                                        '^': 'string',
                                        '$': 'εӮԝɖЊɫ҈ѝŚ³ѩŠТƼRʘЇɒǁǙȵʅʡɜśGȶIхƽ',
                                    },
                        },
                    {
                            'name': 'iМΉȷ˻ӺњŃΦĦ:ЯЁțɌϛ˾Ʀŭɡх',
                            'value': {
                                        '^': 'int',
                                        '$': -8985455277416693876,
                                    },
                        },
                    {
                            'name': 'ԍ҄ȚV7˚ſGԋżѴϽѝËΙȑѾȉҖϒ\x9aƆαӪƿ˨мŕʽǋ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ήǀǿŠʇȼԒμȄФɻρʐʯυɁȔ©ӿФ/ɅфґÁòEıԫʏ',
                                    },
                        },
                    {
                            'name': 'ƾ˪Ɩʉ˘ǽԕѴǪȫҨҷϛˀҙ½\x98GҖ\x8e4µÅΏνɸuɇůӭ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210203:180440.430034:+0000',
                                                        '20210203:180440.430053:+0000',
                                                        '20210203:180440.430059:+0000',
                                                        '20210203:180440.430065:+0000',
                                                        '20210203:180440.430070:+0000',
                                                        '20210203:180440.430074:+0000',
                                                        '20210203:180440.430079:+0000',
                                                        '20210203:180440.430084:+0000',
                                                        '20210203:180440.430088:+0000',
                                                        '20210203:180440.430093:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǮˉɯЩϪ\x8dșĊ\x87ƏҝɻÖ\x94Ӝ\x88ǋȵΣȲy¡ûJӨʠɎ\x88ng',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ĚѷȳΖʡԋɅЩɉȶŭRˢȢ˒¬ϗοɈǓȘĞĺɓȵΩȘ>Ԧӳ',
                                                        'тǞдĒɫʫƑºХǪҚȺɢԑӷ\x82úác҉ƈÂȱ˾҉ƿ1\u0383ʠͲ',
                                                        '˝ɑȭд\\ӞǭȸŨ®Ȭ˟Ĵԧȡ\x8fԆǖɼĿʽȰӞȖҔРЯƗŚǳ',
                                                        "Ŧ'ôŵĬ2ԙ¡бъøћӔϗлΩǢƽȐӟŲѵτŰĒywƥŬƏ",
                                                        'ʱ+ĩ\x9dďԟҙƖtӽѓǧúɒʡʀǚНЪƳΈˊʷȰΫ¶ɄƝТЬ',
                                                        'ɛͱлʹKӏȧЋϹԮӠѹӛζΟ\x97ҰĮдΫĻѬɉɴåЏƏʩѹш',
                                                        'ŜƇѬ˶İӿèǜФȰӿȠȼŵĐėɖΘĂȿ˭λ±ýѩ\x97ԈŻȌú',
                                                        'ԋЫϥƍԅηͲ;˓Û~Ϣ҇Ұ˜ĭΝɱӉХĶıǃӇԕԕÆ΄дӕ',
                                                        'uΖʅѓʓǇύʜŊƚ}ŇVȶ\x9d҇ɺάöѲńǯÙƨƒƽ9ͱȮʇ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ԠϔƚʭтʏǎкȰϚā5\x9bϲʬэʬ\x83ҰԜӴ΅гȆʸԢȹșˮԈ',
                            'value': {
                                        '^': 'float',
                                        '$': -78298.44398948265,
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ǣƷϬЄъȭǣϕӊќâΎœ\x9dөĂпńCҥӭιĔǳôъDʈùЄ',
                'message': 'æȎ\x98ʼҤȥŎ\x87¸ùԊűӻГ\x91_ŁϻÁѝƬɰԙˬɄ3рŘԏӌ',
                'arguments': [
                    {
                            'name': 'ѐ%ʖӝΓψӵà×ΐ˛ʷ\x89ȝŨ˵ϕƋÓҋĻ¸',
                            'value': {
                                        '^': 'float',
                                        '$': 915206.9860534641,
                                    },
                        },
                    {
                            'name': 'mҒ2ǲԩяĳ¡ҏ˱ҙƒŷĘσθǩƱ˛ƞǯɖIЗӡƥÖɛl,',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        39783.06007600011,
                                                        526032.9440917295,
                                                        276027.0804119788,
                                                        999016.0809042668,
                                                        718493.5566771865,
                                                        143988.71299356178,
                                                        853158.9923266234,
                                                        687671.7340249828,
                                                        -36256.36956336399,
                                                        580742.3203052761,
                                                    ],
                                    },
                        },
                    {
                            'name': 'УϔЗЎ]җЀʶ3ȫ˩ȄƷRіԑ\x9dǅЦԫȐŅ2ΎϙјɋȣΗǙ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ÏČЄηyĖϖѥȒһСΕʾЃĄǦ²ʾȠƈíyȒɨЮφľǙ˶ƻ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'у÷ȔΨ²ĦȪĥžӫĻс˞҆/φȷȋɍΒ#ĪËþҒϸԦ§ɡŶ',
                                                        'îұˏŢ\x89Ɍ}ӼƀΩȤԇŏ˺˰å\x8fÑѤԑϑӈӓђΡӋɒςϩʆ',
                                                        'ƥȟЭőɴ6ɽ\u0381ϭóĩҝsġĐԇOȸɲňОłɠҽ\x98ɕЀɎìƽ',
                                                        'ԎȐȞıÑǔˉźӒÑÍÁɃ²ǦЌσ{ˡҮϻӔΪĔӳѾ÷\u0378éā',
                                                        'ѪʴɒӫЯŰȐҝȸ5Ԟƥ\x9fԋƆҝĄӇ˸ȉŘȇљЙɣηԌɋźƉ',
                                                        'ŏҺıӗ҉ʙôЮ\x95ΗһˌũśҺ\u0379ҭӡ\x90ϖǀlϮʸЂɃғӅТ΄',
                                                        'ϒ͵³ÇɆǅӴýĠʏnЊϕԋĕϭлэѧ\x9dǩУɶEȏüƈЋһϯ',
                                                        'ʌ\x95фһӜ\x86ӏυЂƑʹÝPҝѿŧǁʛƚƂ\x94ǖĆҐĭɬ˫Ƚ\x8bF',
                                                        'λß\x9bщФȪʧӁЎʸéΕɞāӤƐ©ѯгǜǷΊŁƞ˔ȮȋņϞȚ',
                                                        'ÇϹÕ Ч{ĺҤΠӣ¤3ľϕƼȜɌ\x9eԚıӹȸӃЍύ˹ĥɋƄ˳',
                                                    ],
                                    },
                        },
                    {
                            'name': 'kґЁ\x9fɞ˦ʔͻŶðʧ\x9aÐmѭ˕˼',
                            'value': {
                                        '^': 'float',
                                        '$': 614048.0101043296,
                                    },
                        },
                    {
                            'name': '/ɼāÑ\u0380ǻ\u0381ň\x94ȟԁӈĒԟǦɍҶȲ˫Ҍǿњ͵˸ǷĴìңǋȑ',
                            'value': {
                                        '^': 'int',
                                        '$': -8779551500422868730,
                                    },
                        },
                    {
                            'name': 'úѯɣ8Ѹ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ğŁӵɕʼ¨â)ҊȂΒˣтБάƴĒϢрӡӅЁū˾ʲӪơҶϴ\x8d',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        6769273904448647262,
                                                        -6609429619158897091,
                                                        624910028233153002,
                                                        -8798858765022680773,
                                                        -7097197716605826520,
                                                        -155173542727109793,
                                                        -9012528450721317516,
                                                        7474884852794229303,
                                                        7133040224311970772,
                                                        -3790013377972892227,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ԢʄĄȰԅнɰƷζ·ҫǍȤ˦\x88ɎʦӁϹϒʲȮГǢϞ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        44693.38119194575,
                                                        195071.74199839064,
                                                        13846.742265248293,
                                                        335765.65463259956,
                                                        804740.003317572,
                                                        59599.78735873627,
                                                        72847.29467963666,
                                                        416494.76667597983,
                                                        287204.8242942863,
                                                        343974.8308258179,
                                                    ],
                                    },
                        },
                    {
                            'name': '\x8fŬƣžсðÀȝ\x89ɂĪŦ˃ЖЊ˸ǲϐ˪ōjǓ\u03a2ĵҗˌЫӟ˨Ԫ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ӦBɤĸϣĪµvӄǄØʗ}j˃Xɳϫ\u0383j8˟˝вӠƹƽÉғ×',
                                                        'ƒԓĴğӬϱóȺʲʈɏȄ˂ʐӷ˗Bə%с˅ˌǳ\x9fǊ{ɦФɑǵ',
                                                        'ҦѩОKԘ˦Ιşɸļ_ҹҍӲʗүʉʴϚǅyƀΗѳΩũҷɛʃӋ',
                                                        'ƦѺĀʤŁÚήÃĀɴӣėψS҅ӪΛRˣϯ˲Ѯ_ԮřʧƦɶҖԚ',
                                                        'ȠȭΊ#²\x9aӺРѶǩΏґѓǹΚоǞΞèѮѼˮϟůʅϙɟ½Çқ',
                                                        'ͼ͵[ʍо}ƚɐǛӯLѺԘ˻äѸƌǛɹĵ҆fɺÄԠ$аҊœҗ',
                                                        'YҙƋӤО҅҉ҨȹƐӫҿ˂Ӱ҅ǉʚįŨŬλĎ˓˜˷ΪˣμÚҁ',
                                                        'ЇϖĪԞŝĝ\xa0ŘıfɧӑŢƆɲɔŜ\x90ɧҥԍΝӳĵι9!>ҹ҄',
                                                        'ǒʖʬΛňύўŢРaˉǤϋɄӗ\x89ϞȚ˻ԕġøϭÎшšËġͳк',
                                                        'ƤόɆӚ\\ɷϯТʔԢĢȯЙįӖϒјς˅ІѪŝħϞĄ¶ҥƩЗ"',
                                                    ],
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ԮǬӅɇĈ',

            'categories': [
                'file',
            ],

            'error_message': {
                'catalog': 'Ʃѝ',
                'message': 'ӥ',
            },

        },
    ),
]


class LauncherStartExtensionFailedEventTest(unittest.TestCase):
    """
    Tests for LauncherStartExtensionFailedEvent
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in LAUNCHER_START_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherStartExtensionFailedEvent.parse_data(test_data)
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
        for test_name, test_data in LAUNCHER_START_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.LauncherStartExtensionFailedEvent.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


LAUNCHER_START_EXTENSION_FAILED_EVENT_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='name', name='LauncherStartExtensionFailedEvent'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='error', name='LauncherStartExtensionFailedEvent'),
            ),

        ),
    ),

]


LAUNCHER_START_EXTENSION_FAILED_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ε˼хзM-÷ˑЧԁқåǋҍǆ˅',
            'error': {
                'identifier': 'ȬȄУǞÏљ,Ŭ_ǘЎŲӲŒӣ˃ŨѥɒƩҎɃңЙ\x85ҒзԨƕґ',
                'categories': [
                    'internal',
                    'configuration',
                    'file',
                    'access-restriction',
                    'invalid-user-action',
                    'network',
                    'configuration',
                    'file',
                    'invalid-user-action',
                    'access-restriction',
                ],
                'source': 'ûϡԖϠɺϓŮýιϭԔNăϤƶPnŽɧҪρӃ+ʩȔҽϱ\x96ȽО',
                'corrective_action': {
                    'catalog': 'ҔӥāʜĒȯǍƩӽȾȈ÷ѺƲө\x8eŋÄ\x8dҊǇĹƎÙӽŭˈưȶʑ',
                    'message': 'Ĵǘɚ˟\x82ǡҤʦӠҁϷʘKoТƪʅҫǙқҨГOǂʯʳƅӄΛǁ',
                    'arguments': [
                            {
                                        'name': 'ŋȷðʅŞ×ҥӝѺʄø\u0382źψƼÄΔȊΒѦІÐҙÉУġʛѱϹӧ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ÉϬkÃϏpҋƄGņϕúϊƬ\x88ѿþɮÈ\u0379ùŢĺ¡YΕuҞϻď',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:180440.422801:+0000',
                                                                            '20210203:180440.422832:+0000',
                                                                            '20210203:180440.422839:+0000',
                                                                            '20210203:180440.422844:+0000',
                                                                            '20210203:180440.422849:+0000',
                                                                            '20210203:180440.422854:+0000',
                                                                            '20210203:180440.422859:+0000',
                                                                            '20210203:180440.422864:+0000',
                                                                            '20210203:180440.422868:+0000',
                                                                            '20210203:180440.422873:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ƅ©αҳɜˍ\x9eω¤ʦ˼¾ĥϜΊ8Ԅʓ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ќ˩ԚŲСоʕʎɓӖʃїѽĪρԥǋĭɊŵ\x91ĳԝɤɋɠ\x8aУӈȝ',
                                                    },
                                    },
                            {
                                        'name': 'ʸˠψ£ҎȠ¸ŇӱʯͿǃ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 150425.92695764854,
                                                    },
                                    },
                            {
                                        'name': 'ҀԖӛĭǕã;þŤԃԢȗéӞǃЍʽƋ×ƚŗ˹+ӊSȡǭҦʫѼ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ч\x8cФlʡӱƟƗϒǓωƛɂЉç½юĳͺԃιҟàƙњ\u038bǾ4ϩƾ',
                                                                            'Ό\u0383ǸʑɕϤɤȷÇˢʴÄŜãɳĨʿƑΧϸīҢ×ʠҥѥgɈʍɝ',
                                                                            'ѿѹɃĄԣԑżΒǾˏǰȧ`ȁŊǾŇȰ\x9bňҍͻĄ7ʞВȎ\x92ʦŨ',
                                                                            'śБ±Ĕʞқ҄ʮЎçȡІɍǢɟȅщɰѕQϓǌЏ\x82ӷԢƬѮÒ\u0379',
                                                                            'ԣӀѓ^ΥŅɄҖʅԭʬУαΧѹɄΕȎ҃LǕςԜť˷҃ǒɺ¼Є',
                                                                            'ԥsňȘĚʨǦ˫Ϭʹ±ƧɣϮƅƍĉč΄ŞØΏțӫʹϔęӯӴʾ',
                                                                            'ғҒβ\x9dΘˏ<ʾˑϥɋȋқϼĽŷƝ˩ϙϹ6DѣԡƈƊŤϱĮч',
                                                                            'ǅͻ\x9dӕĈ=ДƒҌZ˒Ē9\x82ӂϯč΄ʾʧǽƹ҆àĳʬʆɳЙE',
                                                                            'ÞĎώɄϑԡüΉѡʐƊɃЊИˊ˷ɫҌČӁũѐŸðéӖĽ\x88ƄΖ',
                                                                            'ʺǃϭѨϻͺҟԓ¸ĢǯǵƳʹʯԩƊÇͺϱѡѢϘҵŨŃŰѰȯʔ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӹǮΛӍ\x8d\u03a2ϷԜ+5ЕоǋʼȱӰͻʪҜλŞӮП¤ęßѢӨȅΠ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¦Ř\u038dÅŚƜmºәĴűǘͿϴʴȺͻɳęοѻÏFЧψɘȐϱŻ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            469770.7485832039,
                                                                            828446.5065167455,
                                                                            856899.0983076012,
                                                                            339163.2337195372,
                                                                            101892.92835469008,
                                                                            947198.7781186773,
                                                                            -23321.043234426907,
                                                                            405154.4601602262,
                                                                            -11051.949526341748,
                                                                            188898.04061620357,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȅѿȷ˪ʶ\x8aǗӅȆ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2711448927512985342,
                                                    },
                                    },
                            {
                                        'name': 'ɪļӞt3ҙðΒқЩϤŎҸ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            897144.9389288635,
                                                                            207612.6400098136,
                                                                            353961.17173229955,
                                                                            615286.3480246662,
                                                                            244993.12510856817,
                                                                            721107.4656982668,
                                                                            63775.25176694919,
                                                                            180170.9941942353,
                                                                            681233.8085757605,
                                                                            841480.9317847139,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҙԣϩЙÙ˰Ɗ\x88IџϧǒƥɚŁѱϸŠяʁѥʭ;ӣÍԌЈsªÝ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʃѕҡϹűǧʹț^ʣǭϞ϶ȏҰӑѿѩҗϰЍЧԂЌ.ʓӒƦϪ%',
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'мʫѢ\x8bʾʔÎʺѦԎҸʸҬƽѿʩȳθ`ʧɅ4ʛ˳ƳѱѣθԈԃ',
                    'message': 'ØäΑʌrvοͷ˽ͳ˂ϕʆϋΆˆIҧŔҞ\u038d\\˫gŪF÷Aєϧ',
                    'arguments': [
                            {
                                        'name': 'ЏΜңǞˤĶѕňЎЏʆƭSƺǱШȴɶ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1527617087571928219,
                                                    },
                                    },
                            {
                                        'name': 'ӺпŷɐȇÝЦ~ͽ\x8dφˁ҅˒ԟ˲ˏʩҷԥ£ɘǋǙ{҃ŝӫő\x81',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            875884.96348823,
                                                                            348808.04386861087,
                                                                            262545.6345392006,
                                                                            607592.8207771317,
                                                                            869405.259982934,
                                                                            474200.5259872513,
                                                                            296976.86403880414,
                                                                            717609.7544775122,
                                                                            290936.89481115184,
                                                                            680821.9469967317,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˫ˉɯԧĒŀȓԥ\x9bιѱđԆϜȽ[HǬʖϟԓɥƔоϷɟЗƒŵԩ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 238798.3697530668,
                                                    },
                                    },
                            {
                                        'name': 'ϸνťǤӯѬ\x98ˌɉȉĕ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɐԦѧʣΑһΒʃϖ\x91ƮÍ\x8ctґӑ-˙řıgġ\x8cъĳƽ÷ŇɭÇ',
                                                                            'lūǦϨҍҥřԚԚþЊϸҋ˱ӾқĝҟȲʸʉɽФԜ˭ø˪ӈ˒ѵ',
                                                                            '\x9e-ԤԉĩȢőǸ"ť˝\u0383GǴƸͲȂҘǺűӲĺêȅԪʾ¬ʇʓԂ',
                                                                            '&ϮӺԒoӨƹѝӔŞƶғӺȓЋőŗԘΑōʘǭԖȔśƁƪðҁξ',
                                                                            'ͻ˦ЋĈ«·YԮҎΈĚЉǰtǄЎѪƥVӞǾʡqЀМƗDѷϨƺ',
                                                                            'ϘOŇȱԭЀŧĵÛǻĽΛȻ\x8ețʾӞЧ\x82ʫӳεӑеА˗űƩѥˮ',
                                                                            'ÞξѵΟɆҞaʏïΫyкʢƏʧɴԜҌĬйʯäȹΨGƛΐҹϿӜ',
                                                                            'й/ȼŉ҇ʞƻбǖɲÂȶɂύƫIѼʢűҍƃѯёΎΫr\u0382Ԩɫƙ',
                                                                            'œΪτʇƃùȅÝ˵ďǖвŚ)\x85ĦѢʦіǊ<ν˛ɅêϓuȃɋΟ',
                                                                            'ΩɬuɰȧиӃɘŉvΒL˷Įџr5ȒƔӄw˪ͼΔ¤ҢІƸǧʿ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¡Ԩ$ʅºƴϛ\x81ŸƌӒʪǂωǳPб˴ȝЙʢǼϡЯҮ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6340175526544225641,
                                                                            -2247710360711588617,
                                                                            -6541235193871743361,
                                                                            -8804814848370749757,
                                                                            -8662239209095612305,
                                                                            -1504614232547199425,
                                                                            137476517432257628,
                                                                            5646904605514243819,
                                                                            -7384789904827751453,
                                                                            1877792958485194339,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϋȨ\u0383їԎ˂íÊЇŕσӣöқrҨуŌ÷ǻɨóƲğ)ƑŢ±~`',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˟Ӆы˼ʤɌбЩϞʸӲМĞʼƚӥƈβͰғвˮʮƾǢĊҶЖǓʇ',
                                                    },
                                    },
                            {
                                        'name': 'ϔ_ȗõҝÞʸƉȜԞδƕӹʦϡƻϩЩЏ;Śъ\u03a2ǸʟΟƔҸĳǄ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƚǝɽ҃ǷΤυʜȅ˒ǠΗŉӘсŲˀťϷЅŌчΤϭϰĚЉ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 609506.529933299,
                                                    },
                                    },
                            {
                                        'name': 'ŃɭɫǝρȜɵǈθҲëƟȔǥɾ\x87ȘΰǝԈϮȑǑɧþӃӤɭҖe',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1716684710249014532,
                                                    },
                                    },
                            {
                                        'name': 'ĬȇèΕΨƝӷȞʑϩԍ˦Җǯ\x93źȌҴȿĳȠǑƿʀȡÅϺԇɌғ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɔȹʯo.хϳģΏӊıΧӱnKâɈİ˽÷ќ˘ŇЊ˖ҲʘƁӮп',
                                                                            'ӞӸ»ϿðļȈŰЕǂԀǞҞûѯѧюcʅȌӇϼĭɷФŭѤŕˋӿ',
                                                                            'ΓPӿϚԣɍƋǕѴʮȘ;\\ǯĭӏFT\u038běЮȄϝϼποǱśεĞ',
                                                                            '\x80ӼüĲɨǜdɈĽʴÓŊʸЌ=Ԑŗɜ½ÙǐԕǕʓNǝʝ˷ˢϒ',
                                                                            '»ӬћʇōŌлȷʃŭΖñƸ£\x90pÌχ¥ԆҶĕȌcҝɳ/Ӝωǈ',
                                                                            '\x95ƁȫǂǗʕТ\u038dÆ\x88ʁĎяёʉĬɡҨÁοɌǲģ¿ϰХƱҿ˫´',
                                                                            'ΓȦiҶʩȺȅи(ǩåОӪɒӣπVĿĩҦɻ˽ΈԢŮԙͽҘӕз',
                                                                            'ɂɾǙîȴ\u03a2ćѸǡǫɵё҆ǔĚƘhÁы\u0382Ϗ϶ҧƗƎȱȞɸŅԍ',
                                                                            'ȍҺϦϹ§ϛѭȘɁЅǺǁѼƵ´«ȎʑǀsϦ҄ҚˌԩĹȄɖǜŃ',
                                                                            'ѭӯ\x86ɣҟƍːɾʅǊ\x80ȾɢΩЉûҀCĄԖҾǬ˰&χИίӓϙʶ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '·\x98ų',

            'error': {
                'identifier': 'ҨĤÇДí',
                'categories': [
                    'file',
                ],
                'error_message': {
                    'catalog': 'Ҭǃ',
                    'message': 'ӫ',
                },
            },

        },
    ),
]


class EventTargetTest(unittest.TestCase):
    """
    Tests for EventTarget
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in EVENT_TARGET_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.EventTarget.parse_data(test_data)
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
        for test_name, test_data in EVENT_TARGET_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.EventTarget.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


EVENT_TARGET_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

]


EVENT_TARGET_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'event_id': 'ǮЛʧĐƕŷŭӡŦʙƢǥǋǏȓ҄ȧŝɍːΆèӰǧʉԩŴãcК',
            'target_id': 'ҋУϘǲČ3ȡșʋјƕȻq\\Ȏęнʭʨʰ1ʡ\xa0ȺͺдÜˎƔt',
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
            'events': [
                {
                    'event_id': 'ǀĿҊΦ>ѼӟɭÛƐ£ҏȰӟvÇҺӠʛĔԛΓͲɌſǹʺ"ѐȣ',
                    'target_id': '2ɦЛïԎĬˣãϏĎϏѩʄɽϚʩʁʃîϪӰɻĜǢЫǠēӱЉʎ',
                },
                {
                    'event_id': '˓äμԃ\\ȺҔSŐÅȮϭʎМϤÎǄPAêʣӐ˄ɷʁ;\x93\x94҃n',
                    'target_id': 'Ѵҿ˼љʭƮҙ˄ЀŌԂРȻϪПǥåˬ@±ԠұǀϯҬªW҃Үƹ',
                },
                {
                    'event_id': 'ǵǐϳʄąȝƠä¿ϴÎԪͺdʡȩГѴɑԅΦҜƗԈgӻ;ˤoѢ',
                    'target_id': 'ˇgǵŢЅŵ\x89Ѳĝ\x99uʏљǍüǷыȻ«ϜӼВОԖǪċШȩÎé',
                },
                {
                    'event_id': '˼áďҺ҂ƹɨIƥŴiƆĠmϊŠҀɼ\x9bԬňíЈɃêôĨǛ¹ж',
                    'target_id': 'Ł:жÿʼƮʾίЇƂʒǩȑԅƦʨÇåӋҀǋҊӷț˓єˌƤʖɷ',
                },
                {
                    'event_id': 'л*ʟʒ\x81ѢͶŁė«ƆλĎϹÑŝɾѨ©ȔĦ\x8a®ҏʃİԪǿɴʝ',
                    'target_id': 'õЇ*Тӓ3ѿεʮʹʈ¥ğ˦ҵīϲԅҰȧʕƂЯсˏδȋˡ+Г',
                },
                {
                    'event_id': 'ƃùюӚ`Ǳ\x90Ŋњԓϐ\x93ƕȊϜʗφȭѰЅλɚūӛςǛіåɼϋ',
                    'target_id': 'ҧŉʡɔǪƏơҤŀͽɦſѬ±ӎ1iłΝѬʤȒƑșĀ˓Ǎ҈ƥŦ',
                },
                {
                    'event_id': '\u0381ƥΥӠΐɠʭјȹtƗĳЯҐΜҸɘº\x89ӊ\u0379\xa0өґжοǄԉ_Ԡ',
                    'target_id': 'ʳәϢҝsВŗRǙÜkıɪķšŋϡΨȷӓ\x99K˻ŐҘɒˆĥ\x91Ҳ',
                },
                {
                    'event_id': 'ƅҞɠȗĚ˶Ƞӱ˫àмDĖӨƨҌƘзγЙźĂǬАƥӧϗȫʯÀ',
                    'target_id': 'ÛǫŁƌђƔѮϘƧĔĝѨŃĈоэ\x93ćт˺ĭϟôҪҫeʂŹ÷ʓ',
                },
                {
                    'event_id': 'ˑҴáϏĸѺƹќÊ&ÄļӢԝͰ¾ɴƫĘЄκôƙˏϟνɟˀȰђ',
                    'target_id': 'ɞɑåΩ҆ȜӺǺҎҸę˔Ә΄"ÜżƊҾ½ùîЋ7ҶĞĶҎҙJ',
                },
                {
                    'event_id': '҇˕ȼǾŽɩÕ˻˹ӞǋRЌÞaӟŤĤƋ¶ιÏʉҡϦ¶ӷũʶ|',
                    'target_id': 'ĞĘåԭЭĕɜͷ\x98\x97ȯƗҌмĚTǏŀ˳ˤɖїӱȑнљңƢǭɎ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

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
            'events': [
                {
                    'event_id': 'ӉˋѩӜүƓнćʊӅʶЂ˜ԩʟѤ\x9e\x80фѤǩȋϏúԍӧŅ¬}ŏ',
                    'target_id': 'ǉʨҸӸƚRβԬвFѳȣΒíȝːҗ$ԈѸ«ɦŋԘϯ)\x7fĀLԧ',
                },
                {
                    'event_id': 'ª\x92bʳǸќāҐ\u0380ÇӛӸiјʗĘ*ѹԇ˝ãƃʤȹʅˤяӵфΌ',
                    'target_id': 'ӕǦсˮЩ»ύȆ˭\x90˴ǭԮȶ2mѩǖԩңϭ\x96ʀͿȬӓΤͳȶ¤',
                },
                {
                    'event_id': 'Ūͼɿ˚Ҝáϻэʕ¿ѬƜШԊй\x86ԧѓӹtǋƔҔ¶ƅʲ)Á΄ч',
                    'target_id': 'ӢʋȡԜćІԁȁϠöϼԘȲ»ĶϿʻʚϞĠΕūμѯĹ~ȤɉƆЇ',
                },
                {
                    'event_id': 'ǐԛˤ4ǵĵұǈŦÕҿǘŞϦǚŠß˯БΛŔʂǓҎ¾іyɗӈ/',
                    'target_id': 'zԃê˕ψғƾǑЅɆUŴίȪ˳ω[åΥʑпŚύΦϹʪ˙Ђиӵ',
                },
                {
                    'event_id': 'ˣтϖǷʅŶa˨ŽЊʭȚaǐԡӱԋ\x86ӎҺӾčĢˑƣѡҒ\u0381Ýɱ',
                    'target_id': 'ϰ\u038dиŌЁԞҰ´˲ҺʽӚ1ΟÚў´ʐØǁ҄\x81Жǡ;ҰāƊяě',
                },
                {
                    'event_id': 'ȘÁӂбȱáĞȣʔɽӵʗʷñјȤөĚʽƭrɹɡΙŷ\u0380Τ!ƥѽ',
                    'target_id': 'ØӵȧҾƱɴ˔ƖѾ\u0383ӌėāĽÇоĵ2Ίθӛ¬ˌÓŁӀτѮӧĕ',
                },
                {
                    'event_id': 'fѯ¼ʇǷӀ͵běǶƾDԮҲƑɫӇġȹʌʀÊʇāцÄɫŖƞĈ',
                    'target_id': 'ήе@ЂіɬґtΡԩʿÆʀˉƱGɸԈŬ҄õĵёӒʈȇӂҍìϖ',
                },
                {
                    'event_id': 'ǌѼĹΡ˂Ú\x96Ğ\\ȃɇƐӭ˄ƥǛbÁϑяӖ˔ѼτȏϫCϢΤk',
                    'target_id': 'ʁɋμЄд¹҈ġɭҔ_ȦҺ\x94Ȳȗ¸àƖ΅õǓΣҍґöҩҨɰЃ',
                },
                {
                    'event_id': 'ʓjԝėќɻȂǻɐӏěуþȿȏџϭďǛʲ(\x92ƗĐƙˈȢиʞ˹',
                    'target_id': 'ҹӃÈɲȷ\x86˄C҅ЈëҍɋӝʬҝϜŸɕϴĕӃτԃȿȱɠƺŅk',
                },
                {
                    'event_id': '˜ϢǦWԀԓƍӞ¼ҿԭ˜ćҬɾА;yy\x80ҐӬԢȝȼҬҞԩзǞ',
                    'target_id': 'ͽюҋӎƄιȅѸϯˈŒǧѸDϡDɞͿӒǁĐχ¢Ԏ˜ҵԡұǛƨ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

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
