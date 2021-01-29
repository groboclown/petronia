# GENERATED CODE - DO NOT MODIFY
# Created on 2021-01-29T19:26:19.016891

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
            'action': 'ҕɶȔʁŇħŖәĦԛаɢӰɞǩʚǷѡҶǲƑҏ҄ѹˮɵŮϔϿʔ',
            'resources': [
                'ӋĽϫ҄ÌМΨб\x93ьSсҲ˖Ҟ\u0382ĬӐҘ\x81\x9fɸ͵ҜȾîȍƎōЀ',
                "ǽțǎϬ@ԒǊʉʆ}Éʼɉ'îӇTϋЀͳЅğФsčɹƓƆԓҜ",
                'ǊΗϲĽɛ\x9fżӬćʵӉɦɏƒǜɊө\x84Čπə҄ʄƈԧЃβɺ\u0383ȁ',
                'ηGǒ³ҺŏǆɛçҀĸǐÛŲҖɲʤʚƩӲϜōγΊAр(ƘǨʠ',
                'ԃиǻ¸ή\x9eTƆ˹ҬӀϱǪťʽҶɖŰɳƗbnÓӠɄќȵО1Ħ',
                'ȂΛđƆ˽ΙěǿҘҊƥѠИȘɝ\x83ŗѪƁӡƬēˊʷͻѩҩ¸Īͼ',
                'yƤИuǫǓʦƬԍΪЍʹҗʻĐŖ˨˂ÎƪϘϟӤǂӁ¹ȣГνԢ',
                'зʓЁíҰɇ+ũ@ûĦˎɡϠɥɽĹɾԂ\x9cȎͳÌȅԚŒӨȥӽÞ',
                'ĸʤӷΔĵǥƽÙ¸\xa0ҶҩĢΑΚʴϓ͵Ļǆ²ԟƮʾϳˑŌɪÛԡ',
                'ӭƘҁϳǬϋə˲єΠʗʈșȢō˂ȞγȺʮĊƅƧ.ʿȝƒŖϟj',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'ө',

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
            'name': 'ѪƯǗÀυ8"\x90CǡƆǛӼȱΩϭ˚ƺƢκǖвŎԆшʆˋϰ',
            'version': [
                -6122868698683298035,
                -1234220646383986273,
                -2644181768873091537,
            ],
            'location': [
                'ǲķMƞbÖÅʄďǻƼZЗϫΛŢѪƔΎƲʦaΓџƮħŻϩˇԘ',
                'àɹȳĀȝфˀ҄үС+ɐЍâɼ}ΒʴӱϤŒͳɯ§ωҦòǜӀѡ',
                'jʊͲȓӀbü҉Ҙ\x8aſ<ͻNӠԬɬ\u0381EˊŲɏAŔ\x86ΝɈӕЬѸ',
                'Hώҋ)Ƕ˩sǇǄ˯µƇCȕϹ\u03a2ϓǨæƫ¼ψ©/ԭяÀƦʀϺ',
                'ŌțΦÜӜιДԭǝþëӋɉŚżʺžʦ\x92ԎѨǺ+ƫˎƻІǚÛɚ',
                'ǉ˩ªĎʻøēǏ\x8aϴϠԫϵƂ˙μůӚȨҼѮΎ1νƮǄĽǚϧЅ',
                'ɊɘԍӇĺjҺҤ\x8dƕɳӎÛԒą˨\u0381ӓψη˷ɍҾİƼƹЕЉβʻ',
                'ƨѤƏţнɯýŴӲρѹºџĦуӢϜόæЛϸѤȳѪŵ¼āН˦į',
                'ϔºŰӫɡгʮҏɨӞАĊǎљΑĮΧьN§ʿƋɨʜԂ¨ąʴÀȷ',
                'Ʌψʛ;ƠԜʞćԤċC͵TӺεv3fʕӏǱƛϿǾΧҝÍŊǺѷ',
            ],
            'runtime': 'ԡYǀΗИϕ˻1҄Û҉ωԧćѨӵaә\x8dųσP»ѯξӰΔĽāQ',
            'send_access': [
                'ǯȫϕԛǃѺϰʯѦƽƈΪλǣ\xadԓƿƤǊǛǪǵԆԌŐɥ±ԍƤ\x89',
                'ΞpȋӔϟƗϥȊȤʾҲҾɁǖĀĶǈpȾ˨ɞĄǺɝǔ«҄\u0383ìĪ',
                'Ħɭ˱Ƿϵȕʁmʈ˞˯ӸϲЮƋТŭϴΝwԃ͵êӑÃȳƠ-ӽɁ',
                'ǧ¨ШiƱ\x95ӦòЙҒ÷ƬwɈϔӗʧM;±дήÀԘɫΒѻƀ5Ͻ',
                'ƶӎ@ƐǇѨӲȻęԣƤϦΌτ˥Ѥϊȿ.ΥХu\u03a2фԙŔËĮʱƍ',
                "ϪΕɸƺФôҭȥРΒƖΟɠGѻ@ƟБ'ӧѪ³ƅÛ˅БΑɇϮˋ",
                '¾ɣŃŰԑȖY˯ćǊÓӷʦŐʘĬӔΓԦȧйԚҫЇӈɢǸӁ,ϭ',
                'ӖӖąu˳ЉȥΨиєɮȨʡ5хÔ«˥ȃǑцċȗòР˻ǬφØK',
                'Ѐ˸ĴɇФӻːƬҺӛĵŰǿǇ҈ЪʦϵϊǰҤĩԋМ¡ҾļǱω˴',
                'QόĪɩ\u0382θџӝ½Ψɐϒ1ĤȞCŵÁÛҐ~ϙϚДΨʥ"мͼĕ',
            ],
            'configuration': 'Ţ8ʅӌƿUυţѤΖȞHνӳўλϹʐɠȸ\x9aɷȶ\x97Ҽ˳ςʊòӳ',
            'permissions': [
                {
                    'action': 'ʼԔϞӏĄ',
                    'resources': [
                            'Ѩıѵ҈Ҏˤυ1²ʧӁԁˢȷҹЈǞҧ\x9e˱åʲ\u0380Ŧѫ˖ϤӑÃș',
                            '\x86͵ЪԆѦҵ\x93ɩɳԧØЯӎ˓ПӳÝĐѸ\u0382˾ǬЕǞԂԦѷĭʄ\x96',
                            'Ξłț¦ǟǝкʱĿͱƒ˅ӞԍӝŒJϲԮҼ\x8fȢȅҨɌʒРɫʊх',
                            'ɷѸO˧ѱҌаǄͷľǙŹ˺ůÍʟϬԔӑƔʠÍºßӽ\xadŞԑДΐ',
                            'эµɗ°ɁϘӹƹ˅ËԖɏɃ˾ǗæƲ\u03a2пǖńñǝНȀϪԭѰǼʚ',
                            'ӞӈɯЀĒȳɒŻˑOɠѪҳ˛ҬôưγǐƽŻқͽȐ\u0380ϱvӋшЇ',
                            'ˏƃýяѮÉɮƂËȇЋɸӈї\x92ȔӈǃҘύ\u0381\x95vȨ°ԭĬѺԧϭ',
                            'ϨŔčŮĩϺāȕʅϣlȚØѲ˚ȲΝf˃¬ŷƩҫBӒ×ϏǢˣӥ',
                            'χϐǱĆԇĄʈӞÁ˖ҙԬűΰ6ȚŃǯѱƅѺ®şɽҗǃ\x87ĘѦ\x9b',
                            "ӛθğЌЮӥ҃Ƣҡƶ6ѦΑȳþï˅ȇ'Ʀс\x97ƃʮδįĭǲ½њ",
                        ],
                },
                {
                    'action': 'әʾ\x85ȝԞʤ£>ÂрӴάɦȝªξѦΑɡηƖúĬѽÝҿʯɃɭэ',
                    'resources': [
                            'ɒπ˥\u0381\x88ʱɒɗѪԞ0ºѦǵѲѱĊ\x87ӒĢʋЃЍ4Õϛ\x9cƵ¥\x88',
                            'YˋѵčӥƮΛԬÅ³Й_ɃɰЃ´`ΞǣƺȻ¡Ȼ˻ɊшʍȐªʤ',
                            'ķӲҜƆʁŧ\u0381ƴʅÃԀή\x8bдҐѰǏэŕĄÔƒř<HĎ0ϑɐŷ',
                            'ԟЕȿ˛ǼҬѤźȶϧÎÌҏщɪʬǶɏ\x91ȟśɻTԓԅɋɏŵǪΊ',
                            'ϖҺǛҗƺӚŸɭĩƤʹʔ\x97ȁ҆ēŉӞɖĊԍʋԍаЌƔфyДç',
                            'íΖf҇ÍѴϤ˚ϺȚҜȁƑ\x90ʚʫѥƴQƩьǤƠҏŬŊίњиɦ',
                            'Ԣõƺ5ҡɝÌӑ\u038dǽƦɲǘԛʤũŬϡɂƻʨӮǾx¶ҹƛКȼ®',
                            'ȧǪϪ&\x98ǟПЏôϓÿŔÎʗĴĉͻϲϽãȀчҺнǺήĹe0ԧ',
                            '˖¦ȣȠҚêҌńЉƙƣĳθϻʣĔñ\u0381ğƒɞŕɷћð§Ŋțӽý',
                            'Ҧˢ\u038dĜƥȻʣϬÏϗʿѣm£уϱśŌ#ĚкЛɬȶ\x80˳ȴɶғƶ',
                        ],
                },
                {
                    'action': 'źkόΒӘȏͰιǄΌϏʬӨɚΫўϨ]îϬƉĲƵȣĸɿŞԩİȼ',
                    'resources': [
                            'ƱgĦϣΪӾҟѻůīԕ\x89\x95ʨ\xa0ǉʎÌ®ҧѼÂ¦п"Ӣ6ûĲá',
                            'ұήǧɏȱǣĥƙ\x89ĊĤá˓dLâÇǖęφɗ~ŐȘʺEӔǇɶӗ',
                            'ȮƉЖҒΓ\u0381ъԬôԄɣҕ˅źƻԀÑӒύ˦ªϚßʄϼ˹ЍΉƽĪ',
                            'ƎϦɪZėŴĔ\u0383ƇūҟˁȃΕӶǍԊ0ϖ\x81ǯěτӾυ¹ËҾͽĨ',
                            'ʢ*ɈђӔцǟ˵šξɟȕʛʞĀĘΖ҇ɕӻͲĔ#ɌӛͼƽɛɝƤ',
                            'ʵƭȋϏʗlʈŃŧƇÒƪƸИȦȫϵĥǾƸεű˴ĿγԜʦĹҊŸ',
                            'ӢĴÙʥҾǴҸҏǜԍвɚщȸɏɤ˸ĲÏɡěˠǫ\x99ŠЕ˥ɗѶϲ',
                            'ʦėɡϥ˙Л\x8a҄ǊɃþӇˬйî8Ȋćǝ\x88ý=ʤӯ\x9fʷϯ˟Ϋ\x8a',
                            'ǄȩćβĒ',
                            'ȐõüD\x87ȺŠѴ¤ƍЂōϵΑҝƝФȺAȠ¼eͽϯŻϳʻĒϤǢ',
                        ],
                },
                {
                    'action': '˺ʹԥҝ`ѴP\x81õɨϿzǜ¹ɖʳ}ѫ·џȴͲÐʾǎ®\x91ԇӇͿ',
                    'resources': [
                            'ǓdӇҞƜòƁÀφϲū¦ɈªԮũʼL´ʩķӥˎșЅЧϞ_wҼ',
                            'ϫ\x91øУ!ɮҠȡέñćĩğӝķѡѾȷɴǬ҇˫ʸˋӕȠȿǎΖ\x80',
                            '\x92ɐƯB/ȡҺҰ5ŻŀǃȦ±KѪөͺϟӐ=ĢƓʹğҭЦǣǿѬ',
                            'ʉÛԪ³ɕŘХϾƶÃаɮɑŪӖϾҢƐԆѧЂóΆɅΈЎʅÉŷˬ',
                            'YǳũĜ\u0383ήʫχƽ9\x80пɏ Ӆä<˶мZҙˁħɁɵӶΣϮĺΑ',
                            'ȾˌҜǋɧ2ȞӔʕϹ˲ӌѬˏɮҮW˦ЋȇŦ\u0383ÁŎǖү\x97Yԛ˧',
                            'ʅŬŬȗ×ǗίƬƩ\u0381ΞƼЙƘȗàӴ$єωϫӇśƵξNź^Ӂƪ',
                            'ˎԍŘɨѾЕƴƁ*ɼӲїʷǀØ˂ƨ4ҜùʯʾөԔńʩӜЎª5',
                            'ͼɏϾҁеÖ\x7fΌԨˉƀԆ˭ӻɲηÖ˼\x9d7ЗƗԉô"ҦԪэɁԞ',
                            'ĕL7ɡAЧǑ˃ϏȒѸĆΪÙĥÍ?ɢҷʶ±Ѧŏʌƴ\x95ΊŮȕ˯',
                        ],
                },
                {
                    'action': 'вɴ\x93²ĬřΒÀΑç˟ҒȭҦèƷíӱǝӒƧıӥѱʽЁѻǰȌƉ',
                    'resources': [
                            'Ɍɹ˛ӟƿѢҤѪЊӕ\x9bĠџǏkɸƄȕĥҔϻʶ˳ГГ\x84Жɂ˹ʣ',
                            'Ƌļģ@ĐӽѤӝϭŗɘъ«ΞcҙǶҊв\xadԓ\x85ƛǈԞOŇËŞѬ',
                            'Δϐ¬ɍҖĖơѤԤρ\x9b',
                            'ѻʠĴğҶѹ§˺ϿȆ1ϕЧɭӎԬ\x89ӊƽűƒӑЍіӂiҠSӚӺ',
                            'Ʒ+¸ɖИ~ҥӊҹ±cѭǌǃȑŧ\x92ƺΖɕ)QтѼҬѕɦʵű¬',
                            "vϮƗɝЩƯԞ,ѷЋҒŹӼч'ÎӕÁƴʝҡŌӔʖҞŷŶŵѨŦ",
                            'ЈɨћέȚëѣĀɪҗƶáЌĚłżƿFƊōɲэӘ҆ҚԪѕ˫ѲŨ',
                            '°Ŋзс΅ɣλϯǇʐZǕʭrԤʙӼžϋ\x92иҟѿҁμ˖ʼΜɐ¾',
                            'ύа¬мŞԏԦβø,Ԏ?n\x9dɤҵҧʛϤϿȧђпӠˢРԚ<Έh',
                            'qSzĞͶƘ\x89ˍфəƞgǁƀїƠŀŲ;ԮAśŷçƬһɚ(ŝл',
                        ],
                },
                {
                    'action': 'ЮԇІћӸáǖǧь˗ƪЫˀЉˠ/\x88ԄNӋEÄї˱ҠԔЯĺǈË',
                    'resources': [
                            'ΊϛǋŞͼҰϴĭΥȢȣ҆ƖȍǛϊȗÔѥυέʲÝɲĬŴϝ¢ťс',
                            'Ӌ;ƣũͱԜёԖХӁȣѮӋɦЬJΝѻť_ŔҠǒҺӗƼŜԑÞW',
                            'ƫρөGџȟΘ¯Ų]Ҧ\x98ǞѢӼϐƙёȘaÂʲӀƹǹˆʗǫýΛ',
                            'ĔƎƃéSэХ\x90ǨȍΌԓԣwőʒű˔ҕĠϤΓ¦ȽĊhʁҗҧĘ',
                            'ƤɯˠӾ\x80њӡһԎ\x90ΑÆ¼҂Ϻ\x81ʲѷƮȌϕĹΞʽ˶ԄͻҫBè',
                            'ϕǦɴІѠɨʔ˨аɿŬɜɡҢƽɴԉӓ˳łɯ\x96юÈŎʱɓӒïΰ',
                            'ʒʓÉӉèġÆÔč|цCŭԦǌ\x91ƫЭ0ЦΦ˂ŘΝԓĎ\x87Kљȱ',
                            'Ť¡éИûҶҖҠЎđȔĜʙˁхƌГФҤǳϼÐşǙ\u038d˗ʛȝŐj',
                            'ŜǗ҆ӨË˾ɆË¤ӆͳjʣʥɧBėĚǌҹˏ;ƭɣ\x83ʦʝЄ˹ʹ',
                            'ƌцˇģ',
                        ],
                },
                {
                    'action': 'ƁăʶΫǵǪ+ǋφԁȶɹpѮəƀǥʧϸʰƆņ˱\x9aăщÏǿ\x88ǡ',
                    'resources': [
                            'ɅɺʜËӤƬpɱǴѮȵˌÅ¡ȥȷÜƂȨьӲчѦуƂѣɉ¤čЎ',
                            'ĘȩƞƶΖĜкҁѯ\x9bƊҬƧΨѰй҇Đȫm1ʫĊŕΨӝͱħһϝ',
                            'ɎðȀöϷƦº¨Ȼȕŉ\u03a2ÛóҹǄƣǘдг\x8dɍɩЁɞĊÄԌƼö',
                            '&ˌ#ʻ΄ʁɸoˬxӇȓˣƵλĲʅȣʿԋҜƯɾɭɭ\x94ɄǁԜû',
                            'ΨчȟĚƆȤʱ\x81ƬБÕƚɌΞȂǎҷϕȞʈЯ½ǨwŲd6Ȯ°҈',
                            'Ӻ\u0383ƱɐʺϗъpԭӴƘ˒ѮȒȂ҇-өӝʸɷϻѡóŜɇȐnΏz',
                            'ΩƊ˫İɝѐԐєɷźӄɒη»ƩјԤͺƸάÀϹɤbͱӧϫЂ˼Ʒ',
                            'ҊɅɑͶпRɔïɷ˙ѹŕёҌàȪΒƹƂѵΥŠșͽǍˡÆˆÀɆ',
                            'ѭ¬ûÎ\x8eӲ\x82',
                            'kЯ\xadEЩȧԚΰө˒ÖoΔßʽʳ\x84ԃƈԔŷӍȺήƽɔfΞÃЮ',
                        ],
                },
                {
                    'action': 'çоҀ˼ҚɢnѫʑǽĊȞʗΧv¬ϛŃκϫ',
                    'resources': [
                            'ϥƔĿωӖvʊѦƸƾƲ»4ѾӈȵŇΉθѱÓ\x95bѧäΌϨҼƣǻ',
                            'ȽѠЫQўͳɪǕЀʭŀ˕ӎÙ\x9aИͱ˝ǋŅӢƪ\u0383+0Ԝ\x98\x87ԜI',
                            'øɂùǰΟќȌώ\x86ͼ\x84јɎǁŘ^ӥȳƤПԙğѓHϖɚθ^ˁϛ',
                            'öɁŐӟȋɖðщЖɱφĩԡƤ҆µĮӍѡĘϔϲӚԩʍҍʧǟξΌ',
                            'Ӳʇˣ¯³ɜŧмөԘɠTїȭқ˕ųδϷ¤ʔӌǎɀƖʫǷ΄җƁ',
                            '˕ғęўιˢ>ȵШÌҋŹΙʁĔҫėƠүԅΏԨђ˹bʑӘŋͽ\x91',
                            'Ňʫ~¤ƬōιїƁȓȬҏжȊȣИə³ΓǝƞʜʝʿΨţχ\x80ʒś',
                            'ϫļҔƑыүԘŘǆʆȽɴ҇ҼϙпɳϼͶ҇ӆɟʹȷùȑ҂ǣǮ',
                            'ЬŪҰϳÚӑÿĜΘƗɃňѱĐСôҭ:ÉğџԒϹ\u0383Ϳưęĸ\x8eŉ',
                            'ѧǵψӽ˥ΙķˬɚϾ˫ԗЪŋʔ˸ԥˢǤƳśϿӾ˅χ˯ǑňʖɁ',
                        ],
                },
                {
                    'action': 'Ӥĕɼ\x8eƓ˖˲ͺ°Ýģ\u0380ɘ*ʊӪѴϦĈźƋͿΓӿѠÍԤÈéӿ',
                    'resources': [
                            'ŶǼӂԂɔшŗͽOɘʼȈӨ\x8aЙĺ\x92пʤĮȝыӍŮЛǎɺӽȇǍ',
                            'ŻӠϺĊҗŐØɳʻӛУ\x96ЋɀʬʐʞÃƱ\x92ŻӢЙʢ˳^ɺәԆɿ',
                            '\x8dʀˈͶԦӍȊűϐÏɘюҚҷґПĂƘ\x87ˁǖфφǝҺõƄ¾ȸҺ',
                            '¶ʳΟӀ\x8fȸɖʜԖßЙϒŚ\u0380ӓЍʻǫ¯ą%ɏѽӓʬНҟŽωќ',
                            'řяPƃǜͳѯͶ˦҂ϛʓϐԊӗ˷ĦˣҶΫϫȆÊ\x94ɋe^ŊԖķ',
                            'ӦԂԫǫôɈǨб˱ɺ4Ŋƿǝͽɛμ\x87ІΫÆɬ¥ť˼κ|ŉŁӉ',
                            'ɳӸCTϜT˙}ƘĢǈ»ϩ\x87nǡҤŲʌџ˥ЇӒˉǻeӘȑ`Ү',
                            'ʒӨ¿ģҵųʢǶѷц˙¦ұƧИħвĞͰӲǮ\x8eΜʑЋґУȬӢʣ',
                            '\x8eǐèvɞ˄ЋҦѧŸˑŴǔ9ϱĹԃ¦VĲĚɒсƒxʬŅņřƪ',
                            'ȥǎ˘BȧĜѵґ÷ŠϹťĸʯ9трɄòΏѧϥξǅҼϢη5΅\x9e',
                        ],
                },
                {
                    'action': "БΦʱɉµϹɘɏĦϙӁѽ˄Êџ'ɚԃ \x80Ċb\x9dðтơqÎŲϯ",
                    'resources': [
                            'ÖҷώϋĒӽµҥɲԌјѻȔӥΊе\u0378`СǝX҄ԩʯ˫ϓÉϣ˾ú',
                            '¶Ҡ1ʻˌxsųŒąʹĥҐşǼЇˡѼďȝԕǸРR˟Ԗҝ˓Bʝ',
                            'ȷÙӁѥȺǎķЛɝӲΕUğеǖţʮ\x8a\x8cȎҍǝǃǕιƂÊĞ˾M',
                            'ŵ¥Шȥ\u03a2Ɯʬ}фΙĪЄĥӧӟѽҋǌԟңԇȀљӼЖ\u038dЫřŜϨ',
                            'ʇƻȍɰ˺ӆˢԌ\x8cBѠҼäĘȎУЊ2ӖƈДӾ`Ŝ˱½ʙϕҲѩ',
                            'ѣƩоЙԠӼ|ҪˎŭԎŪЖǱʫĴȔʃЪƈɔѱƅҖķ˒τǏĤԍ',
                            'rϴŶӞ͵вЬˇƊϘðϰҍэВˮƄˋϕƺĹƍ5\x90řʮĥϨ˒r',
                            'Ƥ\x8cρ\x8dǹʹэЅВѰΤǽ˗Ͷˢ˯ʹɭͱ\u0382őЗǦʮ[ëʍŰGϾ',
                            '˰ǆǊȐѾҏŊȶʕ\x9bσфɬʄ˲/6ǀϣʱġ`ÖâӽĴ҆ҷ˯\x96',
                            '˧ʑЦύ˯ŒĭɣōҦχǏǃƇǭԉҬɓɱʖʨωʹųϳӤϴʼȵӯ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '͵ɍί',

            'version': [
                -116212565478531391,
                -3763953890390976492,
                -2944113012094830918,
            ],

            'location': [
                '0',
            ],

            'runtime': 'ǒ',

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
            'name': 'ɆүPԁкVōњҚԏϳΠ³ҢďÂ˃ТǸϘгАǈьΛê/.ƨÙ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '¹ԩӮ',

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
            '$': 'ҊҁΑρӅҦƉ\x7fɁųʆҺʟ\u0381ИҞӖ˟Ûš҅ѣМϲɟϾˠѢ\x9bƚ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 3722634146297787568,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 481916.49736509216,
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
            '$': '20210129:192618.935090:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ˋϚƩÜѻΔɁƨТ\x80ƍ˩ӊ·ĚʇƣÇ¯ε˳\u0383vç\x8dFҐʗХԂ',
                'ӸίҭĢ^ВϖÓʙϩǐΣơȕʜͰQȎɼhđ!Uʊҋͱ΅˔ԟҎ',
                'Ԑȕ˺ȎŵǩʠЎQӥŇԜбВҜͼϚɄο\x81\x9eоĄҀ¦ħǣЛϔˇ',
                'Ǹ\xadȽćΑǬЧԞĈԨӏĠĂèƏʎKîÏPʕΦӞѽGŨˆ\x89g¯',
                'žНǲŚǖΚƄҴԝ҅ăFø͵\x9bÈK˷ҍƗƎƵξĺĬ]Żӂΰò',
                'ҹGėĈņť˅ƄƶǗǗԇɾԪĎїϴΡҜéϘùӫѡ҉ÑԋˍÛ˭',
                '˽ʜ˖ʑ\xadɿbÆҭ*ʜцĳÐǅãӐчˀǨˋђϥ˩ĜӃҤËТǀ',
                'Ʒж\x86ʴӿĜǦjȪɋȀмɯӝ҃¯\x8dңԖýȨҾӡ˰Ųɾ[ğ˳ӽ',
                '\u0382ɊұƇǚԧ^ĔYÄ²˭ǮɺʪÓԫѺȖǉӌŮǭ|þűϘpȵΆ',
                'ˤŏǘÁɡǔ¹ʲΈԇuεɤӋШпʧŞлͼȳ³ҮŇѾŪԢ˰ƕ6',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -1020453540439117429,
                4220507739433995317,
                -6450268796389405951,
                6238398437254266786,
                2694139718474957995,
                -228724694849839530,
                7816176223459400048,
                2900384876203758758,
                -4970978874488561759,
                1842154753703671080,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                687018.9447614206,
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
                False,
                True,
                False,
                True,
                False,
                True,
                False,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210129:192618.935943:+0000',
                '20210129:192618.935954:+0000',
                '20210129:192618.935960:+0000',
                '20210129:192618.935965:+0000',
                '20210129:192618.935970:+0000',
                '20210129:192618.935975:+0000',
                '20210129:192618.935980:+0000',
                '20210129:192618.935984:+0000',
                '20210129:192618.935989:+0000',
                '20210129:192618.935994:+0000',
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
            'name': 'Ԕ»Įωгâů',
            'value': {
                '^': 'string_list',
                '$': [
                    'Åę˫ŦƟСġĘǷ¤ɨǕ˼ԫőҸƠɘƣԋϳѫĤΞʙǥЬϦӱø',
                    'ѭĮ\x94ҙԕȑЕȉ\x97ǔқϞǇѣӒϵKɊҧӺԎ˸Ě\\\u0383ӱΜĮʼ\x94',
                    'ƌź\u03a2ðŘԫ5ư\x8aѱΪӠ½Â×Ŷ˕ѧğԬğ·ϭý҅ȳ·˜Ƒg',
                    'Śχɕƴʤ\x88˒ĻӐΫѼŠƧ¸ɛΧɮЋĞʊ\x8fвİõʋӉÓАʅʀ',
                    'ϨƢΜɉϘѠы\x92Ӊҽǘ´ƐÏǯСǬxǰˀȟҶwĹȬ\u0381lҹāT',
                    'ê\x8e\x89Ƭ+ʕȵЂΣԧҸԞӓaϛǡԗ\x88ƣдxɹĈˣŭɖϖҾÎƉ',
                    'ŌΜΤƮɡ)ȋƇԟīƮæϽÍҠªҠˉǺǡˌ˙ЪǞӏһůɷ¦ϖ',
                    'ƖâʗÓ8ëΡӖΙ˃Җ\x9eʏ ǜԢ\x88\u0381ϩɄʾ˙ǽϼˡԅƝҶϯd',
                    'ϢαΘƉ÷\\υ¸ёȭʟƪ±ŝǎѷʳ9ΫȐӯϗƸǠɷҁģ|Ђ\x91',
                    'Ѫē`ʛÝǷӮƇҢʬȮѬˊМΫώ¾ɝŭ\x8dŞƥwɰʏʽ±β\x9fÙ',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ƻ',

            'value': {
                '^': 'int_list',
                '$': [
                ],
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
            'catalog': '¿\x94ƅhӃƦȌӖɁ˥\x86\x87Ǆӱßňэŋ}ȯϭǩдЛ\u0381ȩóˌϿҰ',
            'message': 'ĜǢп˛¬ëɩȯ\x8dľżҋBɺʉʽӥŽ®ɓɻÌyɘϕZ+,ɦɉ',
            'arguments': [
                {
                    'name': 'пΉȋ¤ȱђʎʠɷǏğϲ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        233498.77997633925,
                                        108256.34084551357,
                                        532312.9739991694,
                                        366027.3491649576,
                                        670079.5687348204,
                                        305589.9197069827,
                                        768698.8969390347,
                                        283867.81129413174,
                                        264126.04306001385,
                                        884717.4928842253,
                                    ],
                        },
                },
                {
                    'name': 'ĻчÎƃфÖT¸',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        417894.63161179906,
                                        971409.2519514028,
                                        152223.59710374213,
                                        145977.13688521957,
                                        801343.4195748381,
                                        634971.7314204184,
                                        177495.66142037878,
                                    ],
                        },
                },
                {
                    'name': 'ЬŬ½\x89˺ЕЦˁνʎůμ\x8b·˭À8ѥ:ӸưɠǦŃƿǼʙɉ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -6057473719797709221,
                                        -6503036492269007874,
                                        7280278100946393575,
                                        6830406551640188556,
                                        -301460168102751383,
                                        -6794551769055136324,
                                        -8267696635615881672,
                                        5295411460398538351,
                                        1158310686705505493,
                                        2376711821232816010,
                                    ],
                        },
                },
                {
                    'name': "'Іԏг£ԉ\u03a2ʵεϔɮΫΤӘʕѦǞЈґǉЉ\x95´ӲȺɴԭϪÕι",
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -7605823998558451694,
                                        4692446829876011324,
                                        -7938666292487800334,
                                        4158281933300161744,
                                        -5557938329667593078,
                                        -6802716665090767719,
                                        2704325759816587263,
                                        -3403595821887559051,
                                        -4972474382228908629,
                                        -6726630950813913074,
                                    ],
                        },
                },
                {
                    'name': 'ś\x81Ȭϸ\u0379ǗƣХӄͺԇʯҖ/ɦǉˍʂ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210129:192618.932837:+0000',
                                        '20210129:192618.932862:+0000',
                                        '20210129:192618.932868:+0000',
                                        '20210129:192618.932874:+0000',
                                        '20210129:192618.932879:+0000',
                                        '20210129:192618.932884:+0000',
                                        '20210129:192618.932889:+0000',
                                        '20210129:192618.932894:+0000',
                                        '20210129:192618.932898:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ҼԨƠ<\x8dёʊɮЉϦεʢʭŁϙĂɐɩĥɋέȨ˙æ΄',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210129:192618.933197:+0000',
                                        '20210129:192618.933210:+0000',
                                        '20210129:192618.933216:+0000',
                                        '20210129:192618.933221:+0000',
                                        '20210129:192618.933225:+0000',
                                        '20210129:192618.933230:+0000',
                                        '20210129:192618.933235:+0000',
                                        '20210129:192618.933240:+0000',
                                        '20210129:192618.933245:+0000',
                                        '20210129:192618.933250:+0000',
                                    ],
                        },
                },
                {
                    'name': 'НӎłĔĭȞ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'Ъyǯɢ¯ȟɚĕϫĞŲŗҵʤǳʭ\x98ʣ˲:ÄǢԅȎά',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        637751.5909866404,
                                        342885.6842024885,
                                        101940.39921983617,
                                        843648.8770469899,
                                        897803.0860541228,
                                        457810.78810112004,
                                        510264.1650821812,
                                        690124.4476472448,
                                        810900.6896915409,
                                        999900.55653244,
                                    ],
                        },
                },
                {
                    'name': 'ɊƗȆǴгʊĴǔ\x88ˤҘϲ҃ΰЊ\x98ɷ|Ρѡ®УƈӇʠ2Ҭţĵ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210129:192618.933851:+0000',
                        },
                },
                {
                    'name': 'шɈɰƴǒҿ¶ʎƯ-ʜpŵЮťБʞƈGϧΎѫѧč<ӊǣɲϱΉ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210129:192618.933999:+0000',
                                        '20210129:192618.934008:+0000',
                                        '20210129:192618.934014:+0000',
                                        '20210129:192618.934019:+0000',
                                        '20210129:192618.934024:+0000',
                                        '20210129:192618.934028:+0000',
                                        '20210129:192618.934033:+0000',
                                        '20210129:192618.934038:+0000',
                                        '20210129:192618.934043:+0000',
                                        '20210129:192618.934047:+0000',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'éʑ',

            'message': 'Ê',

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
            'identifier': 'ʀĨǎÒѱμˢћˏӀƏҵïɩΕԬˡ;ǨȔДȠŌªԦϑɯχѫǕ',
            'categories': [
                'network',
                'configuration',
                'configuration',
                'access-restriction',
                'access-restriction',
                'invalid-user-action',
                'os',
                'file',
                'file',
                'access-restriction',
            ],
            'source': 'ĻνĐ\x9aķːдŎӟƙƬɰʥӘşϖΓbʺӊŻˠАÀŗɤϬīőύ',
            'corrective_action': {
                'catalog': 'ʔԎīνǢǎН~ҬÔ\u0381ȓtȥмʹҝχҏǛԘɳzƩǅƮ%Λǝ\x8e',
                'message': '\x98rλȞɨ®ҤԡȮѝΤɲəŽϘʫÙјĀӧѫĺ,˸\u0383Ɣĉ˚\x95В',
                'arguments': [
                    {
                            'name': 'ͿΛȤį+fĝɄrƠȏǩʝΡЊòŐǾԓ',
                            'value': {
                                        '^': 'int',
                                        '$': 5936725844804796401,
                                    },
                        },
                    {
                            'name': 'ĿǶϭɧϠЩ\x8bɣɉ)ƇŻ\x91ЬЍªЮʶθͻζËheʨ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ϥĦȽıѝ˞ϙЛ4ЄѫΣӤѴ.ӚІЏ҂?ŉЅǑɆϮŲϘ˻ͺЎ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ԍӥҮжЫĿѼłʦɟˍΦůǣβҳ˵ȳáςȦ°þЗê{\x9aҲˣƬ',
                                    },
                        },
                    {
                            'name': 'ʂLɫω',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ÃȆâƴŲóДľͺУĔЫӺ\x9bņќɜΌΌӪɉ˪ԘɡØȢ҃Ōʈё',
                                                        '9ʧͽЫǳ˥ƨɿƖǴӦ~ҏȴDƽɍŤϞ1{ʉƎxǭɎˠ˴űſ',
                                                        'Ьғ\u0378ȫ˯ЪǂԮзƤΗ_ɳǖϤԢΠӺҨɰҠζΊǅȏУԪÛʣǥ',
                                                        'ɽ&ȡԂĸиńȃƵϰxеόŧƱӵIЩ~ȇгȧШ\u0383ÂиӄӥƔƫ',
                                                        'ƧɲˢϚZƌƂǉ˚ĵɞʝ±ÍԕґÅқľ¯ΑҵӞǲʍXУ;Çԛ',
                                                        'ŒАńÞȢԜË\x85ϧͳѮĥǫ˲ǜƜÂöÆӼЯʳόīȗǭϩĘ\xa0ӻ',
                                                        'ʞ,˥ǄơԩΗчϞ©ǡ´иȍūǼЁg{ɔƛμЌǣюС˂ˍż¹',
                                                        'Ĳфîç˹ʙ˱҃@³õǡßkƥвʇˉǓģɌԇrѬʵɨ6ҠŶƟ',
                                                        'ѰͷҒ\x9d7ŶȷЅήΚӿɍ˔ˈжʤΠǬΞԂьнǑŠНϙĖӜѣę',
                                                        '¨Ғ˺ȇ\u038bа˶ЫϷȁjʘéϒȏkԠ\x8dԧӿ~ʱÞ\x94żǼǽ·ɎƜ',
                                                    ],
                                    },
                        },
                    {
                            'name': 'дϘǈĥˠŸԟ\x8aƙTͲ˕˂!ĤЉ·Ӧʠ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ЊѐԥýïǮӚȑă%шĺӐ"ϜŅ\x99Ө',
                            'value': {
                                        '^': 'float',
                                        '$': 987865.7189704196,
                                    },
                        },
                    {
                            'name': '<ɀŠócj1JӣˀǾ<\x8dҸß',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        False,
                                                        False,
                                                        True,
                                                        False,
                                                        False,
                                                        True,
                                                        False,
                                                        False,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ś\u0378ӣĨK҄ӾНщΐĄǬĮЏɕϕ¦ͼ\x88όϭŴΫǹ\x8bќ҂ӮƉ҇',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        5173673499942971420,
                                                        3673033571467755519,
                                                        -5091828278231737387,
                                                        -2474893973110417043,
                                                        1445746753056928039,
                                                        6589802800025815444,
                                                        5103355930582543573,
                                                        3367776778090016986,
                                                        1466884803281266142,
                                                        3067350624502249430,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ɸέȫɎɞ\u0380șӬӌ\x83Ǭқш˦\u0378ѵǨИϕӞԊ˃ӝ/ʦЄϏŀ¸ͷ',
                            'value': {
                                        '^': 'int',
                                        '$': -3326057168193912527,
                                    },
                        },
                    {
                            'name': 'ϞȘЯ˒ģȊˋ',
                            'value': {
                                        '^': 'int',
                                        '$': 7412564466816636436,
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': "'ƏӪҼCʔȬ1ÌØίАƪĺСĵÞĠЌ˦ŢйΓʼȅɜʲԮZ˛",
                'message': 'ӱșĽαбΡſ³ȹǧ\x80оѸЖɌˠȟΙ5ЍǕȷƔǕӊ°ϗįΓβ',
                'arguments': [
                    {
                            'name': 'ӺƗďϹŪ\x98ĸώʆϯͼТкК¡%˭\x84ɏϷȾ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210129:192618.936235:+0000',
                                                        '20210129:192618.936244:+0000',
                                                        '20210129:192618.936249:+0000',
                                                        '20210129:192618.936254:+0000',
                                                        '20210129:192618.936259:+0000',
                                                        '20210129:192618.936264:+0000',
                                                        '20210129:192618.936268:+0000',
                                                        '20210129:192618.936273:+0000',
                                                        '20210129:192618.936278:+0000',
                                                        '20210129:192618.936282:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ŋ˩ƽήҀ\x98øҋÌǄ$\x83\x86ѭɭßӒ6êΟѿқƷƜѶƢƭ˩\x92Һ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        824580.7132029379,
                                                        268921.6824874706,
                                                        746923.8919361532,
                                                        381008.1343244573,
                                                        733641.9226935494,
                                                        617107.8729292736,
                                                        725088.9488847568,
                                                        873289.5524033498,
                                                        922262.4000442671,
                                                        538469.004979819,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ò',
                            'value': {
                                        '^': 'int',
                                        '$': -795647283041045187,
                                    },
                        },
                    {
                            'name': 'Пɫӄϕњşƙи8ҡƒ˼ЎĆ$ИԭΙτɫĺ',
                            'value': {
                                        '^': 'int',
                                        '$': -4936017774414032645,
                                    },
                        },
                    {
                            'name': 'ȗʭ,ѱƭО',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210129:192618.937062:+0000',
                                                        '20210129:192618.937075:+0000',
                                                        '20210129:192618.937081:+0000',
                                                        '20210129:192618.937087:+0000',
                                                        '20210129:192618.937091:+0000',
                                                        '20210129:192618.937096:+0000',
                                                        '20210129:192618.937101:+0000',
                                                        '20210129:192618.937106:+0000',
                                                        '20210129:192618.937110:+0000',
                                                        '20210129:192618.937115:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': '\xad²ȀҺϾͲкɡˠӏėʕň\x92ɴϳАԟʥɨҥϵĖŏȅFʽԆ¥ĭ',
                            'value': {
                                        '^': 'int',
                                        '$': -441932747023554298,
                                    },
                        },
                    {
                            'name': 'Ζ\x8f˗ğΔ\x9eʺȢĵЅҵ',
                            'value': {
                                        '^': 'int',
                                        '$': -3542457822361926104,
                                    },
                        },
                    {
                            'name': '}ϓäǵ˩',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        True,
                                                        True,
                                                        True,
                                                        True,
                                                        True,
                                                        True,
                                                        True,
                                                        False,
                                                        False,
                                                        True,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʪľԏҤɭѤ\x97ЯϼшŊ!ȖǡԊѵāĮ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        648581.7071066583,
                                                        547050.8349160777,
                                                        92472.8677871383,
                                                        714298.3497763472,
                                                        192230.05859707063,
                                                        655427.8579882013,
                                                        -51110.345902794616,
                                                        327334.9525835587,
                                                        72795.28820406017,
                                                        688820.5581966046,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ϱʫԓʰ·',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        622665.0144637284,
                                                        987496.089489768,
                                                        53516.52004824928,
                                                        437532.9709816787,
                                                        188889.62291655416,
                                                        152276.09875786176,
                                                        753298.2231607868,
                                                        -87149.15710675392,
                                                        465465.7988384747,
                                                        481912.9057775461,
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

            'identifier': 'σʳȤȰǆ',

            'categories': [
                'configuration',
            ],

            'error_message': {
                'catalog': 'ǣY',
                'message': 'ʭ',
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
            'name': 'ʼԬ¤оɯĒȴӮŁҊ\x8eζŌ>ÀAśƸüϜģЛƭҫʵÏӇԡȕȐ',
            'error': {
                'identifier': 'ȈʢǁɕʵÐŽҮTʛԘͿРɬŏɿͶȡѢϘƝɣˎÆȼÎ˨ìǡɸ',
                'categories': [
                    'os',
                    'access-restriction',
                    'internal',
                    'os',
                    'configuration',
                    'access-restriction',
                    'access-restriction',
                    'file',
                    'internal',
                    'access-restriction',
                ],
                'source': '+Ȗ*¯ƭȷûĝԈ\x7fȲɽсґъ˟ԬŚɅжёкϠҡԂǪÔʭȖĚ',
                'corrective_action': {
                    'catalog': 'ÓÿħУĴSΔӓ\x96\x9aчԉ©лǠǍǵuǁœҚɠɄԂȌđӼěęì',
                    'message': 'ƫɂŴϽƗĻϬȱНðÌҩњҵϧҢϩӲɂɕ˴ѫƋÕíȐǾǏĥҠ',
                    'arguments': [
                            {
                                        'name': 'ͷ϶ϥCΐΌϦŴӊіҫεҜϴkƪӺϲ\x9bӿɵѲľʂ˴ɵǩÆ®¡',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5900566560191969169,
                                                                            -3268431905493257665,
                                                                            -7651573930863039510,
                                                                            -7734555293318613635,
                                                                            -1603706692624090843,
                                                                            304984937504154984,
                                                                            -3997833559449525930,
                                                                            2420004204555633816,
                                                                            4934358184816023132,
                                                                            8954375101072949263,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'SƺԒ¦',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210129:192618.915404:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ǎ*ëƑ˕\x8bɳ_яѥɾ:Ҝӭҿ¾ŸћΞǼԪ˞ĒȼʨώƜǬ\u0381Ӥ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÏԛW~ҀĪƅ˪zøǞɾ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "ҖϚӶƭԑ¬gëҚʚ\x89і}Ǹ[ΔіʓˍɾН'\u038bϻ¢ĩÙšζ«",
                                                                            'ӵbččŽXȬŉƘӹϨӵ¥~˭ѵǪ˧ԈƎȗс˅ƊHʭƺЍӜȗ',
                                                                            '*ϞξӲtċӗ£ɬφϾХ˃àDȒīģѨʔǍȎȭͲtɪǻϪѠa',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǶӒȜѦŝƦӝѼ¬оƽӑϔ6§ɀЊǇȨɤҍР"ѫĪ\x87уŮŒҮ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ӫԙn˒.ę6ĠxŊМȆԋÐˬȟʭԙϋȆӎеĕњѭҡǖûËȍ',
                                                                            'lŨɟԮǮңQźTÃƫНѳЬh˕΅\x91Ѩ҄˴ђӭʊƫΧӡϫƾԥ',
                                                                            '>ԭFĢĺы˘ѾÊɁǼЦˤЪƗɠΒŨøˋǀ˺İˣĠg~Ű*\u0381',
                                                                            'ɧƈцԓƶČýHȼȿƾ®ư±ȩʖĥʜɱŤĽˠΖҺƔɂÒȩlϻ',
                                                                            'ǻжƵ\x82ҖjKԀĆѥ˅ȍ·Üͷȵƍůʼ]Ԋ\x98Ϙјɓ³RɰȠ˼',
                                                                            'ҷ%ɷɷцżӳЙʠ͵ʥϗȴÔĽDϲ-ԧЏлԛșǡ\u03a2иЀǁ.Ƀ',
                                                                            'ąԢˬяÉΡЗ§Ɠ\xa0Ǽõо\u038bСʫɂˆ\x96ŤҌǲ^ӅιŁѻҰԨÑ',
                                                                            'ÍκЖHЙ?φѼӿĜ\u038bѺΣʏȝȦɬ\x80ӑԃЎʗѓ\x9d˯Ͼвą|Ɨ',
                                                                            'зԮțxΈЧ\x9aԪЋҌĪσ˯Ʀ\xa0tΠʎǙϔĖҡɵρ}ҳĞШͳӽ',
                                                                            'VvћȒ$ΡʉϚʵɼѰǢŒƱƒѬ\u038dϒʰ|â=ӃэŗƼƳ\u03a2ӧˊ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɕĮԚі',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210129:192618.918095:+0000',
                                                    },
                                    },
                            {
                                        'name': '˜ѪΤ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210129:192618.918378:+0000',
                                                    },
                                    },
                            {
                                        'name': 'пέƙñɖáQqƜҀ¢ȧҴ\u0379҃ϯǓľʓƺ~6U7ˬ&¾ԖЪá',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3175690084097016124,
                                                    },
                                    },
                            {
                                        'name': 'ĪʿýƲȗĸCʄQȚ4ȤƣŎѫʾуȊÞ\x8aˊN',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɺ˴zŕİâЅ˽tƈzɧδǄ¨\x95#Ԫβ\xa0ʡ\x8dУψ\u0382˸ǩɮͷ\x85',
                                                    },
                                    },
                            {
                                        'name': 'ªҭͺ¬еÙѳıЁűφ\x8eʭęϽԏ·ɣїϝЊιϯμȪ\x9a\x95āȩR',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210129:192618.919422:+0000',
                                                                            '20210129:192618.919446:+0000',
                                                                            '20210129:192618.919460:+0000',
                                                                            '20210129:192618.919474:+0000',
                                                                            '20210129:192618.919487:+0000',
                                                                            '20210129:192618.919500:+0000',
                                                                            '20210129:192618.919512:+0000',
                                                                            '20210129:192618.919525:+0000',
                                                                            '20210129:192618.919538:+0000',
                                                                            '20210129:192618.919551:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ԚԆκˆ·Ҳшù˜ǭĶƻǷͼѷг<ðȽĮVƏôƐϴӝeεšƵ',
                    'message': 'Iǰӆҍ;ӁɽαεϡΚӪŬˎгEʶEſт˾ϘÛ\x91RɈЏƙ]˻',
                    'arguments': [
                            {
                                        'name': 'ӂĥʎηĊ˽ŇԒȡΫηХԜΒɶŚɚūԑţűǋë\x8cҌɃ\x8bȏК',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȋæҝԮȘǥаòзÇðǅɩ\x9cΘɋ\u03a2ϳӓȪбєʮвЊчÊ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ŞѶɄȸ˒ɏҗӥmňҦӶǎбʹŚӞĢӮ˝øγԑÔ/ŸAέƤԪ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4595493479027537426,
                                                                            219859373367047595,
                                                                            -5625075462929274209,
                                                                            4175036674682169627,
                                                                            7166662766300474410,
                                                                            6764557332170186713,
                                                                            8488129112841389841,
                                                                            -6843425966971529027,
                                                                            1910580694275010272,
                                                                            8137154121289261955,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˶ъвǼɶкƶȯłǥɗɣ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -74022.42206424376,
                                                    },
                                    },
                            {
                                        'name': 'ʔ°Ԃ[ȫğѬіұҟϙñϛÓӪǃЏҤԥ\x9fÈʴүƥѲ\x7flԕѭѠ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2254020231557029493,
                                                    },
                                    },
                            {
                                        'name': 'Ŗ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǓԌǩʡȐԓ˔Ɓ¥˪\x81ϠʱͶΩ\x83ˑǵΈ\x8eȷ҇ј0ɫ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5233044235546124736,
                                                    },
                                    },
                            {
                                        'name': '?ƩʘɼѢǸҿˍəϾɤ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210129:192618.924913:+0000',
                                                                            '20210129:192618.924947:+0000',
                                                                            '20210129:192618.924963:+0000',
                                                                            '20210129:192618.924978:+0000',
                                                                            '20210129:192618.924992:+0000',
                                                                            '20210129:192618.925007:+0000',
                                                                            '20210129:192618.925023:+0000',
                                                                            '20210129:192618.925037:+0000',
                                                                            '20210129:192618.925050:+0000',
                                                                            '20210129:192618.925064:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȬєϋɮiˏδȓɈƛИɓǼŨɬÚ*ɾɤƣ˺˩șΊѰɻԃĳɞ\x96',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210129:192618.925617:+0000',
                                                                            '20210129:192618.925636:+0000',
                                                                            '20210129:192618.925649:+0000',
                                                                            '20210129:192618.925662:+0000',
                                                                            '20210129:192618.925675:+0000',
                                                                            '20210129:192618.925688:+0000',
                                                                            '20210129:192618.925701:+0000',
                                                                            '20210129:192618.925714:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'üzҫDŧбˣΩҡķԬŋ÷ҢƫҌƗ6ƫРӃʏŎʡ³ĵ҄ɐʗд',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
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

            'name': 'ɝёî',

            'error': {
                'identifier': 'ʓѻ˪ҧΰ',
                'categories': [
                    'network',
                ],
                'error_message': {
                    'catalog': 'Һʏ',
                    'message': 'ҏ',
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
            'event_id': '÷\x9bNҠ\u038d¿ƯϽӇͷмгʾƘƬȬ+ЕȸąĐѣťņQǇʄɆӰӒ',
            'target_id': 'ԗήϭұҟВƶÛѝ[¾ɄĖӻÁ˖œЖµϪӚ҄ȱԥхʀцϩҩϺ',
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
                    'event_id': '\x9eӓȩɯʫɾПȣȀ\u0381ԟ.ѐΟҊӰµԬҼê\x8fϷȡҞȫЗʿ]ϊƖ',
                    'target_id': 'ŎȿФ.Ю¥сΚѭ)ÂUΜ\xa0ŖˮѫaӱɇЪȸӹԮҭŬdƑ\u0378å',
                },
                {
                    'event_id': 'Şΰ^ϝêÿíϩʪΜʚ˦kӃѥϻȴ¥æЎşʺªӇȡɌќϵĊȫ',
                    'target_id': 'Ⱥӂϲ¸ӇΨπȤƿôѾğϠȃвȻБTǔҊɛʢďɧ¢ΕΌȿЌƍ',
                },
                {
                    'event_id': "˄ʕɃvʹ'LыύЈ˂ɵȠϯÚˍȌ˵oŌǴɖŌʘӺйÙȉĀE",
                    'target_id': "ǎɋȦī\x81ȉĖʚʍӛƝԦвūғѓƒѠÈΑύ\x97\x8cҧ\\þɒĹ'P",
                },
                {
                    'event_id': '^Εȸ˝ΓEoõсȗƍˠʻėхγ˝ԏ+Ӑ7ΨΔʵMƉʨ/Ϫы',
                    'target_id': 'íʕ\x8bΦͷӋƞıԠԁӟĪΆ϶ԙǿ\x90łώïĦЖŬʢʈϙк҃Ǿ+',
                },
                {
                    'event_id': 'ŚƷѸɣёράęƊ˲ύɎ6ŤѤʅҒɂķ@ʣÚèØҡʉŴ¼BΌ',
                    'target_id': 'йˡ}ʮѪ¿ЩǸƍϴÐoɓʰĀʔǸ\x80όʈɧҺԩɍȯѻîǷӞӋ',
                },
                {
                    'event_id': 'ωҙЏYǠӆѪόъԦφñĶŜɊʧȰҺԊȭĄқä',
                    'target_id': '%ФˌȞǳøӹΤʛĶKÖçˇ^мӥ˨Ņ˳ĘҩŇ|тșōϡ',
                },
                {
                    'event_id': '˽ƣͳɟ˶ȺІʽғѨȀʩºъχŲѹēΩȰϺӍӻǑзͳϕϓŉҵ',
                    'target_id': 'όĦǸϤѳғY\x8bǾ¤ɀӭЙԡƌǇҏϽɋǽǪǨι˱ӍҢôЗVώ',
                },
                {
                    'event_id': 'Үєӡő(ǉ`ђӗŮ,ɈϵŶņ#ΑӿĠǚɗ˙ђξʨҗűёҞË',
                    'target_id': 'ȬʌɓҾԆǜɇʽĆҿΓ΄ÖωǯɗƤËăšԑȝϪЖӯ҈ŕˆҨж',
                },
                {
                    'event_id': 'ǧX˽ьњԫΉкԏIȹ<ϗБңΊάȏś҆ȶƧϱώčĦ˽ѨƯҢ',
                    'target_id': 'ǈӃͷƛåұģɆĸɡҳІΘŮӗҗĝʺҙσ\x95ÍӓӈԛҍɐȾȤӓ',
                },
                {
                    'event_id': 'Ç\x94©ʑӦɕϟƜ{ӎȤɈύԬϘņȤѻӠКġʑШɛ҇\\ĸșΦŨ',
                    'target_id': 'ÃҰǪίňʯƬЇe&ʲγƐҌɈΥɫɥ˯KfÁɭªÉөsȡҔ\u0378',
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
                    'event_id': '\u0381ȂǖНƚʵ˕űб~Φε\x8dƌɒ\x84ѱӷţ:}ɐĶÌӚѿ_<Ƞˁ',
                    'target_id': 'Ћ\u0383ƲѝϪǹϢŚϢƮҝǹԙѧÎȯѕčǱПɫӬǷҥβѣyЫԒ=',
                },
                {
                    'event_id': 'ƺ/\x98ªӟŽгȼȲӳӆBŪɒͷ\x88ȴʃʝƨ¨зΏІIȥтȚҨΟ',
                    'target_id': 'ѫ)ŵψıѰӉϮǑИ\x8fǊЇǯэ΅ӰċɔƋùУ\x9eʕ-ʂϽѐԑЁ',
                },
                {
                    'event_id': 'ʾñЌПǘK΅ЃˡÖшˌAɔɨPΝȝӕŕŎӱňæѭɁŝӆĈƗ',
                    'target_id': 'ˏśӺΊ\x9aӞȮʠİҳ\x96Ϟ˛ЬҰø',
                },
                {
                    'event_id': 'ӱώƸîѧ·ļɺɪңʊ,Qʂb]ŵùҒĔ҉Ɍ®¶ĝΟŠΉȊa',
                    'target_id': 'ΏŰơ§ҚƂα˕Ưǈі˲Ҹ²ҪͶϰ˾й½ԫϺԮ˞Ñǯé´Ǥƴ',
                },
                {
                    'event_id': 'ԔÆžĽȘҩ¹ʬ\x81ѮҁԂÃȰ«\u038bϣîąČǁϢãΎѨưœ\\ӐI',
                    'target_id': 'ҁЗĻzɹͿȯЇǢʔӰ\u038d˂ɹƙӢďҗԠˁЄƤţ\x93èĻŃҧԝѲ',
                },
                {
                    'event_id': 'ϝǮяϑĕ˝хǦÓР˴ǝϷΦŔ͵ΆһƖϪ˫³ԍμ˩ǥ˚ҏӈə',
                    'target_id': 'áԭӠҔӉâƌʅ˪ϊǗwĀж\u038dьҌΤ1ßĴZB\x86ƵӇЭľˊĲ',
                },
                {
                    'event_id': 'ЍȏŸ®Ǐśë;ĕӑ\u038bȄқ8ȾҜҧʄ҄ʹзʳĸƈԮљӶԥЖӬ',
                    'target_id': 'p\x9eľȿϑʴŃɅǨȍǍEaΉқӘȵϓĆԎɰʾЖӺƠǘǤ;Żϫ',
                },
                {
                    'event_id': 'ϰʥѥќĨ\u0379Dǒ͵ŰŹΣє \x9eǾΛʐˣ˪ӝѵђоӹŦėŭMæ',
                    'target_id': 'ə\x8aΈǡȭɸɺѥ˕ѐх˃ʥŵÿҜ\x8fāҀãȻГхΡ\x9aȲʣ"ҚĈ',
                },
                {
                    'event_id': 'ÿ)Ψ¿ɐΌɶЪß΄ąʂºǔ˩ƆЂǹϼʟɈɬǍԙМïЁùJ-',
                    'target_id': 'ʾ\x89ѻ²Ʈԩɦ˓ĩƍ¿˞ǽć',
                },
                {
                    'event_id': 'ӐЗʎĉƵԟӭħű>ԚĞɏѳ´ԃ:ГƢЏȢAmwŃƬƱԀřĎ',
                    'target_id': 'ǟʅƜΤЛľˍħùʛԣʽìɃʔr\u0381ԛƵŁ҆ӬǞźʖ\x98Ȅǒh˃',
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
