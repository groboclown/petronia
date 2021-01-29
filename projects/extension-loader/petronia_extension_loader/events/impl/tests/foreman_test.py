# GENERATED CODE - DO NOT MODIFY
# Created on 2021-01-29T00:26:22.700869

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
            'action': 'ÒĈȨĺɨѩűњӼҡłШбrY¥ǚůДʴȩӾӝűƥεƮϖŽъ',
            'resources': [
                'ĢˈȞƉԁɟҋ6ϣ°҅ХƸWyӱĜ˴»˓ӪëpьęǏӡ÷ƄÅ',
                'ӅӘǫɎGńȯэ[ČƕĹǿÇĪνΗѦϿŀȲðƍҘЦҶԏ¸ɰ˜',
                'nƀԦhԚг6ÚqʎϚҦΎбҫĊ;æCӹ˩ήэΆҟƖӵˈЮʦ',
                'ϱʦʊčԚԠϰɖRǳ}ĜѱÄɖùÎӌ¤ɷ˼ЯŬΞҠӴ˟LU˟',
                ']ԝӰɋԃǻɽȜѭAŝʁˇļǷԇҍãǈɝ\x9fȃɀɪͿǂϴȾνʉ',
                'Ǯ΅άФДҢĆωϴ˘ȏЮǴôϚŵtȪgӿ˸ҍѓȌϸ϶ɬσĭʮ',
                'ЏƱǣ¹ƬӷéЇЊȂĳ˞iʀʒwʐ«˗˞ԈЋΔ>уˢѢɽԕϝ',
                'Ԋ\u0381ɽɓӈūƊǘӫ«ӛʄό˪ï~Ż˩ƳˇӾϺʻ·ΩŸȋȍв\x96',
                'ĆǛЃƙʖǤŬЄȳʹPʇýʙīЉ϶\\ӰʲĶ:ˉĢ°ҺҌɘƏß',
                '=\\Ӧ]ȹ\x92ıǱ҄üəλŻҒƋɄ\x99ǙǓѥΛџÁ˙ÄŮ@πŘҸ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'Ϡ',

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
            'name': 'ːƷĢyʔɘљ҂Ρ.ŬƗĊǸ!ԥʩĔžăʳŅʺʵȰμˤƝϫϩ',
            'version': [
                -2998638156503511122,
                -5392918712073911276,
                -4824055452642757510,
            ],
            'location': [
                'ũœγѺV˸ʶӰ΅РԓʿБҨ®ˎҒԁӦ΄ÏѾˆǃЪ?ƷȘþʅ',
                'ɽϝ¥v˖΄ϑΏǀӞǊ˪ԊȗΕєǇԫʱÎϯʵȖ˥ŭ¸ʛʮÿƧ',
                '¿ƿшßÊЏīҿͼʦΗ¸eñʺPĬŶӕĶ`ӘїÔξőŧͶȭН',
                'ƎиŊңӝϚԅΛѝȎǺЎҋªʭʾԋġǄϣͼȠ·ʟǌn\x98ԓӵ˽',
                'űХҏφřɟԀӫƷĕϙ϶˹ăǃʩ\x94ʗéΙ±ƼψǘΜɼѽҭϝ3',
                'ȱŁɆæԥ~Ă^ӨǰȁӜɸǁƎÊťӚȯԡhˈʢƂɾȁΙÍ\x92.',
                'ŰΰƄω?ƑϢπȿǍŢϝϨʾYŬƲĬŇϓȼˍǎšОɯʙϖҩ˴',
                'ǦʻŔƾ´ZĚϘǥһҭƈƽ˪ƘÍ>éʯJˎùƛ,ͽÑŗчʬō',
                'ʐŭÝŀ\x87ʗˍĹɘçĶСƋύŔҙαűӰμ¨ΏӼɴӪʃѾѴҴɇ',
                '[ơү0Ǹɲ˼ɫ`тǍЍŰB³ӌГǭˑ\x7fкōѿјȨħ#ΥϿҁ',
            ],
            'runtime': '\u0380ͽ˗ҹ\\һӣ\x9dćǦѠĕȫѣƃvѝßɭǇ\x91υʝΘȥƪԡŬʤū',
            'send_access': [
                'ǲȭӺéЍŭƧöқ˨ԟԀȥɽźȿŴĆºƐȟѤƫ\x94Ȕ½ɡ͵ɋ˱',
                'ďУ҈ÔєǦӘà\u0382¬ԕɑţĺʴήĖκҫҵӶǩ»ϥŮ˩kύ¢ŕ',
                'č£ϙʛʊɢɷϻӣĆȹЪПаwåɚȯȌµ˾Ȭĉ0Ż\x7fǿӓˁs',
                'җœԝԔ{έӢҼ<\xa0ȵτŦџÈӾЋ˻ǔΔéƌ˘ѐǫņÓҹʘӹ',
                'ŅÔʶӡƠòϩҐϢѐǁȾĿѕϼ˩X\x8cУǄƯɣȍ\u0382ЈGšҗ½ό',
                'ӦԁȣЩΏͽΌӐҴҋ\u038bƋōąʝǓÈð\x9aʓΟȟņϩ@ʚѫб҇ɯ',
                'ҎϸӟnùƻЩɴɇ҈ˉɡӎ*ĝ2ΊѣǥyǡҨĚŕņьÅǩψԨ',
                'Ǯӵ%\x81Ƨđ˄+¶²ȓжüŹ°˗Үǭ˦ϸεɊ6ӶȝΞɹƈҪҸ',
                'ƙ\x8cп˃ʄɌʴϖԨǇ˗óʾƢʃɷ³ѦĲãʷ',
                'ßΠǝʱ½ŕѺЃǣԖ±ϣхҢƢȴмɈĮӀϹʈdϥƳηѕԤƜП',
            ],
            'configuration': 'ϮƞąȐ)ɩәʰΐ˰ûɯӘŻǨͼ҃РrČϟϙ\x83ɚēʌғhэƭ',
            'permissions': [
                {
                    'action': 'ŋϓӆ\x9aԏɻơкƘЎ§ԋɍǡ\x84сǷ|ǄЍ˱зÛ˺Χԥ˚ʊŗ˩',
                    'resources': [
                            'źn˲чȹѥӤsӆɭÏԌȸʓŠƁӣõǆ×ĕșӟҡ¸ϝϺԪѱӅ',
                            'ˍϫ\x8cԄѪÐƠʲȁԓӑ\xa0¡Ȗưʃp҇їҿΦѳÈÂ\x98ί˅ҒʟӺ',
                            '\x9cƠΏџįΈǚƟȕѿȚϗƝĨȝȶŔ˗ȐɦԗПǃϩҕʇʛķ½Ӧ',
                            'ǀε˖Өɜʔʺ˹TƞϡoċɩˁƑԓҵʠ\\˃ѨĂǐ\x9aƣò|ȂǮ',
                            'ЍϳƥRŽ*Ӗ¸ԄʷʟϝĖīϓ\x92хӂƠƽƴAԆŁ\x8bӈtxƮі',
                            'Ȑɦ\x86ľëИϡʕíđʆѳʄǦˇьȖˀɜґųӵČčɨUŹ!ɤӫ',
                            'Eʪ\x94òҹϽÌҸɨА9˫ȏɈƻκЄҘ«^αѵɶʍǔƹ¤-҄Ť',
                            'ζ¡ϳԇӏˤӧǬȴ\\ȞƪƮķυǩǗσqȉȝˊͼρƾѓҾϋʸù',
                            'į|ʲħ\u0382ațӒ³ʧҳ\x94ʜǈοʤƗʐĺȓǶeʜĬǣĚǠʄÿӫ',
                            'Qŷ>˩ňŔƎ˙ʆŅàǏ\x7fһʹăӲŨԮð\x9cДũ˓\xadÚǂ~ΞѬ',
                        ],
                },
                {
                    'action': 'ł˪і½˗ɉѽΡ¢ƐâŅęҬҠĴɄ¾њɰҊ0ÉÈƥЋĩŮcӁ',
                    'resources': [
                            'ȭÛďÏŁњɸ˙цҴjʑҺüƕͷЗȁĖЋ˾ѠѲWƓǓԛȞǀ˪',
                            'Ǆ\x90öɢҬӉЖФΒʼŔсƌþħȚʵǭyPѥǏхԣȂÚѐmьÚ',
                            'ëȋЈΛ˝ŹОӫǡȭ˞ѝҳӺϬҴƦåƹΆ5ûˬɪ*Бψ&ʹϤ',
                            'ʢϤzЕϣõͳŃJϙͰӻR¾½ˇ¯z\u038bΙƓƊ˦ƍ˵ξ˅;ǥļ',
                            'ɞȔͶ\x86ɳ8ÖũӉԪ҂ȁǦŚЋǉ9ɻўϴÿӋ²ʀϏҩċȡʕӁ',
                            'ˮ\x8aˋԖЬ©łҷѴЀǟɦТҁЙMц¤\x85§ұǚԭƽP\xa0ƌn+Ψ',
                            'ªзҌˎώǌ¼ǍÊ`ҖиͰӁҴȓɽԦϔņĚǸȤbǽʪɦːÓĺ',
                            'r\x80ШСĎńƹL°tȾɠƅҾŷrΎѭΓʁӇѝɖɸ>ĻǫӀǗҀ',
                            'ǭÈХLņǜӮƷ\u0383¡ïɷłǄ\x82ΊѶҕ˂ȆӍԗӀҵɿ!\x83ѪϺƄ',
                            'ƑҦĭǕΧʯϭ\x91Ʒéěİ',
                        ],
                },
                {
                    'action': '\xa0ЈˌŧʬʑñйǐƤИ˂џêÜϗͲʷʝ\u0378ԃɹԦʀԣǖϛv;Π',
                    'resources': [
                            'EПӺìæŐˤҔ±ұ˾ÉӦȆɒǒ=ʙ¡ϑˬəȰʏǭҴѐϨҊˮ',
                            'З˼Pįv\x90˓ŝBԙȗԈ\x95ўчĦȌöҽ¶ʥcҰ&ˎ˷ÏɅ¦ѵ',
                            'ԛα·ҵԖĄȏ\u038dǀ˯ĉ҃ŻȩӝЉċȢŃȊżɬӴƿ˽Ɵ\x81Ő\x85Ϋ',
                            'ǩϭʠкÄ)ɖЗГӅϗӸҌɴĐԈѝȶ˪ȑȍŻƫϓʹͳkЗѓҋ',
                            'ҀԣħԨґ˨ˎÒȎϳΡƒɊԓņӺΐӮѦɮİŲÐӃġɰϥPǺԉ',
                            'ˍǏˡȋìпėqψɟiĂБҋvҽůӢ˳ńʠͿО\u0380Ё®үȴp:',
                            'ќð\x95\x87\\ДҖ6ҜȩӁĊϋԊϥ˼µβ˅ΘѦӜƳΟůʢҔəϤɡ',
                            'ǘPǒŅӵϨǶ¼Η\u038b\x90ʇƺ2Ҳņҵȼͺ;ӄ3[ɱηǰºѥТӏ',
                            'ƓҧƳG˽«ý*ԛHïǗǬʑͼϗϱŔҷϩ2Ė9˞ñíΣˎӫȥ',
                            'Ͽ8ȞæΚюǖȗ}ҮԌЯɊ\u03a2;ǗΑʑťȊԥбëʹԣƄΞ"vԌ',
                        ],
                },
                {
                    'action': 'Ő',
                    'resources': [
                            'ºψǅΛ˥OÁƁАҡÜөŻΟȄГΏ}ʼҍh\x8aȊkɤЏǧõѰȹ',
                            'ǊJʔөȯŵģơ˖}ɕԥưϿr%Ϥđʢä\x98ȾÚǯѕЀŸʺ˃ƨ',
                            'ɝĊȾǥƊŧŌ˻ѡχФϪW¿ɴ\\ǈӠѴȽңϴуǾ\u0382ӗЅ/Ǥ@',
                            'ƚ˱ȓîϒĘԞąΥëƈϕҩӞĢ҇Ϡӏǁȯ˲ҢÿƤԐʑʄγɥH',
                            '˲ĞŁϺѩɤÁщѢӗǆ˨ђӏӲ҂ьѫW¥Ιɑň"ρČӅƪӯɛ',
                            'ë\x9aÖ¬φԑʕɽǬĨÀï \x84>ͼÙĈίȖѬ¡ǱĻѢђǈʟɋ«',
                            'ɓQǂȕКԥͻpҒОǰ»ͻɓʞˇȲ\\ļȰ\x99\xa0ɂĵұĎ҂ԗʜÚ',
                            'ԪԃƏƫ¾ÜӳÃӝΙҞ×ϡљѣ˗ɦҶЉӏíPÀҰкλë¡ƇͲ',
                            '[ƶ҈ԑȢŚĘϯǬνŲўÖɁδLɄÍ˙Ѹӽȕѐ\x89ȆRϡγАİ',
                            'ЅԚʊıż¶ɽȿƍƌгӵǵǊũǙɱӉ҉Ǔeҟsʂ[ҬɺŊȨҢ',
                        ],
                },
                {
                    'action': 'ǶҖȢͳȑz\\ɪ>1ŅЪ\x86ιʲΑωё=ҟӢѨ\x98×ÊЛҴ҃Φƈ',
                    'resources': [
                            'ȷӛȫѬǠŝz|жɀИÈ\x89ʨ\u0381Ѱ¢ђ¥ȎȮѶΡʒӷZĸõýη',
                            '±ξěĖǰ?\x9cȭҥйˈӊѷʱЫ£ҬЏƟƕĳȅìǓœθӒҀȦȤ',
                            'ΞǞЙԬҕтиÌ·Ҵé\x8fɷɍl\x88ȾǉˮľȊǍ˨ҜЧЊѴǄ:˓',
                            'Ƽȹϲӗȑ9WͺȠĻ\x8fęʂȍӤͷϴȱљûРɏһ{ЌԂˣċʭM',
                            'ǔñҗҹӈʤȏʹƍ\u038bƐѪĭӊĞǙͶ¯;S~ѼкЙř¶éˡƪѦ',
                            'ϋёiъĳɡüӍS˻Ӻʹ&ȇʒkҀ\x87ňԉ&˛íǛӘдѩÒ\x80ь',
                            '£oӖǈƂģӛʑőƐѿEˀӥʙǐԗrìԜèҡKğȉĉŞϐȖĦ',
                            'βӫ\x8eӓdʿҢġƴϊɒȠª˫ȉɰɇԕńnѡŴӣԐӶŅϖ϶±ā',
                            '˒ÚӚƘǕī½҅ę&gѮŋĶ\x8eԕɍԪ7Ԥeĳԗ\x7fԃιƧϕ\x84˨',
                            '·Ч@ёΨΦ[οúԝρέʆоǝɺͽɨ\xa0ϝȮѩƣŢǬŕ7Ӈņĩ',
                        ],
                },
                {
                    'action': 'Ĥ}ίKԡȋÔǐҬѡ\x9dƬҠƄ¦ÿcÓ\x9eѽµȦāήҐ~ǂǢԟ\x9c',
                    'resources': [
                            'Ӯȶǯ{ɅȚǓюәДǭиŋɚʠė%ľ\x98΅dǔΠƸΑϊѩ\xa0zҨ',
                            'Ȁ˶ӢΧɾƖǯƌeșƁ8/ΞņԃлѻèʥЦɢѥĭș҇úӞxY',
                            ';ɰԎͽɗÜ˚ʥѿˋѯ]Ђ˕ϡěÉōţϋkŶрϊӷԓʡƢҏD',
                            'ɏγђϱϝɼэœʬɚ˾ӄƸŶʪ=˦ТиĬʦТɲоҭϺ˲ЬκŐ',
                            '~ŢΗҵу¥Єǉːƾєɤ˝ЮŪvŐʧΨȫɆ\x8aњÃʻԕ˹ƇȐϩ',
                            'βέǃǏɯњɠɿāȸ\x90ы~ҒȘʮȅƗдҮſҬȁԖʓҗҏӹҭƉ',
                            'ȄqƢҫӑцlԉҨйʴρԕ˸ˮɸœ˓)ĻȥħɷǮ<Źӣˮӕѩ',
                            'ĵӘǅΑȀϹИĸŊɟЦϐѻˌˈaˡƏќĔ˃ҒǗҬƨϋ˶μŪѧ',
                            'ĦӄԤПԨŁԐѸҲΓĸԜ@ϷǦήǢЃȢϛ8ʑĬȒҺƺˈЦʑə',
                            'ΥԛȊϽɓǯɄɠтȰ\\ġԮģŶǳͺû\x90ЛϦ\x8dԮһī\x99еǬĲ«',
                        ],
                },
                {
                    'action': 'éǏԇH˶ǓҐҚĒԂѨˬʗӏɭ\x8cӦжĵСәɸǆ\x93ǖОΑǔŕԢ',
                    'resources': [
                            'Šˆʩҝɵ҃ӓ\x8e$ġq°ȪҧʮƭϤԔӺιԠӢΟȲԐÊźʾ£ʦ',
                            'ǴШɃɆʤ҇Á¸ĬXìϴѣɌǀΘàģȍĥǋӢԦԜƏ\x9beRĽҋ',
                            'ņʫѨĿы',
                            'ЛҜĜΰȣɓΎ®ӽȩęѺΠѴұōϮяɆԊ5ϙǤΫnêмÉʵΙ',
                            'ΙťԁˋĻҠćŽ¦ҶĹԢҶƗËѥOț®ӃŬQǥӢҪƿĚӑȧɉ',
                            'ȆjпєʎíXͲÚ/ĠϜƸʢɟҼӻǻɭ\x94ƾҌɲΌ\x7fÅζ¯ǪĴ',
                            'ɶ\x7fˍȚ\x84Λƶɿӥͼ\x95ǉӑΠɕ҇\x81˸ɞɇʑũ\x92πѓSѠiÊÃ',
                            "ѳŔƝ¿ɱ\\RпΤQԓХÑѻєÂԥЁіɸȿРҶҀӐǹƤ>'Ӯ",
                            'Ϝ˩řЗ\x8cϷǅēҳЂ\u0378ŸɝЗχͻȲǏģԉӒԗǔĆɈϻĉʳ@ɯ',
                            'ȣʹСӅɡȶЅ˰ԊȺjɶҀǊũªʉŎԞɼǈȇѡԠɈӊɃ1ҭŅ',
                        ],
                },
                {
                    'action': 'åɍĝσЦАϞɸ¨ʤЯǺҾϻƩŌФbȥАхʀͽϢĪßű\x93ԟń',
                    'resources': [
                            'ˏËċŪȡȞȵǯȇ}ѹ˵ӽɇӽʈ`Ԙ6ԑMɱVǀɫĝșɔ3ø',
                            'ʊŶɧόԟěҷ÷ćҌeӀҚѽԃʃԔŽѭαĪˑMԤŞѯБЇȿУ',
                            'ǠüљȜ£¼ƶɔȕư½RͻǕіʛ˴˴8ϙĠʭ²ȟǷҏļϵӲ˦',
                            'ɪ˪ɾɤɲÒˠҔƆȬɌÃēĹǩƜʖͺQҫӽѯĀďґŗƽʸŸҪ',
                            'ȣАͼнˁʪϪˍˣаjԠŊʞ·[Έ˱ɤƣŀЁèŗÚɻ˂ӀȶƐ',
                            'ĎԦȲłϵԧŴǖѪʖӣӐрTǜʽГÜ\u0383ύȶǯϕȬB;ԣëůŎ',
                            'ɕŐ˚ʚѼˠĜ˲ƶлҶҍЁɽÍ\x88¾ӅРĝѥ˰ƾȩȷĕˈ˃ĎX',
                            'ɌԨͼтҚѸü;е«ɡȯàcґřǓ´˔ɥǑʜВȳϓҚʹȿњʺ',
                            '2ȧǮϭȋ¾ХʌȲәHǀѿԒɽƍҎƸ(mˁцӭ\x91ҜȦɝǜɺѨ',
                            'ãʳ˔qңϟw(ʩУϸȒÐˣʈ˛\u03a2Ӓʡδˎ8ѠùʾťӤͶkǃ',
                        ],
                },
                {
                    'action': 'ҲȴëліҚуĐѻΟłЎɸń˅ɂʝȁԫƈƪǸýÁ=FϩҀȵӊ',
                    'resources': [
                            'Ԋ"ϻɴʜĿхƫϭ҅ʒыʁɢȅѰrǂҪʋ\x99ѲʑэЎϭ\x86Ǯ¾Ӊ',
                            'ϳƸϳFΣ4ϋńќΚȉɀԊɋӄĘƴˑɣȣǇ6Óй˱ѿЉңŷ»',
                            'ϺϿțιџȰȯǥǄēӡњƤDΡęň҄ΐ\x9fШƻ×ʉɁ\x90ÀɐXҀ',
                            'mɎͼх\x86ķіИėĺϟļ¿Ӟԗ\x85ˎ˚ĘȹÇӡ\x80ϖ\x88җ²ɐșԆ',
                            'ǀjϝΰȍӾĭ Ɋ%кɿȬΑNyΑŖ\xadmԍпЀɾÔˇГͼÃȷ',
                            'Ƿǘ˺ƌҍhğĉǋYʊʷƆɽΖԧμ4ӢɑŁɷɣӿrǳɀƝаѾ',
                            'ɫѵ\x86ӥԠɖұ;ƾʝҒȸпϼв$ÂԦѱǮ\x9aŶVўĊғһˈϽϻ',
                            'ȀХǚêȑˠŵŅÂļѡЀБΒ˕ɤƪrӹԊӖͲ£°/ĐʭйɄЄ',
                            'ËϑƤǣԩϛĆϦŠˏhƳűˍǿŝӜǿƖɣџȄЙǻҲΜƳ#ʪ҅',
                            '·üҭʑîɰϹбҽĈÐөƧƢ΅ˁQ\u038bаêҙϨ\x83;ӨκЅɿȎʻ',
                        ],
                },
                {
                    'action': 'ƐӥĺѰśņŜƻǭǟǡr8ßӬʶԠƆƘȡʼÅÕȪҕԤћɁАҒ',
                    'resources': [
                            '˦ɭ[ԢƫĚрá$Λǣ˫ɰŜĂѭӄŶӧÞӠОɽбĎӇϩʗȄ˴',
                            'Ԁȏκл\\ʑƱ\x88gҮʟĔИ˾φƽʦʞǖˬɷЀԞжԘо)ŊϚJ',
                            'хǑȂƚʴϿδӔĶ\x93L:ǉʭѡǏ\x9bΩěхѤϲϽЭѭԭю,ĵŚ',
                            '˃Ғ˃Ɣʻ¶ӏνºԠʄ±ɸάԞēżҀӇʗƢ%ЪΙƧ˾ӛǐɇо',
                            'ÑҭϨЇ@ľ\x83ԜʪʱǶ²˰Ωɕȳɂϑfҭĸɐ²ȟҹǖȹӚєȒ',
                            'Í:ѽЕ>ѽӼϿЉ6ΜΣ¬uĺŲβˑȷÊ˲FȻЖοԦдҸʛĨ',
                            'ɐҊāʘ·Ύ\xa0ȾζŮһԗЮfӍnӷɚƠԎͼĵƴԏϩƢ*˩ӔΜ',
                            'Ю*ŝҡuɇįϟΖaūІȮɓ;óʦДӣ×\xadɔŘѥǪέϷĕӠ˖',
                            '\x83ȱ\x8cςДƞð\x82АɾԊȎɥɶϔϙλʊŃљ{ȓЃMăʃԆɼȉõ',
                            'оȚIԙӧʊȪ\x87ӼѹŪ-ςʝɧĸ³Ɨǚʓȭ\x94ȄƉ҈ʀϣѶРϳ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ω˒ԛ',

            'version': [
                -7613555999028876213,
                -6663445600550637588,
                -329068269634558949,
            ],

            'location': [
                '˛',
            ],

            'runtime': 'Ŝ',

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
            'name': 'ƏȤ¿ƅҸɹäˑǁˏͲϡ˽ěʻԪʸЩЗ˰ЬɢǇëȴȹЀŐÈƓ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ŭċƪ',

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
            '$': 'ҚŻ:ƙҪcҒҹɻԩɰŏӡĤćɬҬɶďӤёϲԪԞʴѡ¾ӋЅԮ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 7062931016528758673,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 348863.82120780775,
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
            '$': '20210129:002622.636851:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'Ѷ(ʴVǊǹɕË¹ЬˉӲŀŞƽƶÄѷƫĠˀ*Ӿǳ\x96ҖƽėɷH',
                'Ӣѣř;ЧӶȳԜсǴɘӑϹϪ˻¶pśƽ)úӀĻψрÏѡΔзʒ',
                'ӰZӜɨҚӳȥʾθĴĢжȱʣ#±zÅƯeФĔӊƳ\x9dƂ\x91эʼҟ',
                '~вʏөʑsĸГ=ϹȹƋ˒ĻѡśτӇΓϧ"ԚÚ҄ҕQɵƘθё',
                '˩ӞÞˠΙżϙþΜƊɤũѷѡȸ͵ґ|ǝѲΣΥʺď»ȭҒɞӅƱ',
                'ϒ8ʙɻԗҮȠ$œӋİŴӃʪǸΕvĻ\x85ӗϼŗϣȒƇĀʰΈЦΌ',
                'ʦԐѲӭ΄уљѢ\x89пʨʊϚҐň#ϲ\u03a2ЪǞϴѥ\xa0ƕŘԮǐǥùî',
                'żƈɌƂҴ:ĂΞþԩ˼ǚÐÑϣșӹϟˢ\x9e<҅ҢDҝǆԂ˸ˉά',
                'ʵӅǎф9ԐϔʜƛΜλϟŹJ7ÏÙӨɏӯ1ƗÑϝʌϝ\x9cжϡȼ',
                '\x9fĄɔϙĞäɟʔˉɈcǂɃӾɌƆϠ˘ЈýÉҫŻ\x84ңÖ˅ĴſϠ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                5657056753340527623,
                7867092656513311875,
                3625853217323957525,
                -1361603350936541856,
                -7125756214801600663,
                -6650037021224837503,
                -7406668728966778467,
                -4751521673326860845,
                4030402151444286071,
                -6438495531006159996,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                749905.5626074445,
                811084.0294944914,
                729450.240748707,
                918881.7585751456,
                455452.20923588716,
                212578.8974033948,
                188409.71686675685,
                413898.84328163834,
                147295.4168540241,
                115082.14746590616,
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
                True,
                False,
                True,
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
                '20210129:002622.637727:+0000',
                '20210129:002622.637737:+0000',
                '20210129:002622.637743:+0000',
                '20210129:002622.637748:+0000',
                '20210129:002622.637752:+0000',
                '20210129:002622.637757:+0000',
                '20210129:002622.637762:+0000',
                '20210129:002622.637766:+0000',
                '20210129:002622.637771:+0000',
                '20210129:002622.637776:+0000',
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
            'name': 'ΩĐmƽ\x84ӤҥȴЛɇǵAʜԓʡ\x84ĥŉ¾ХӭΏɔѫϞƅϽӫԀ!',
            'value': {
                '^': 'string',
                '$': 'ӃʉŪɒǷԏӎ5TǽԞ#ԤЏǳ¬ΝǮ\x87ѾѽӞyэм\x8fΤѥϙĬ',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ı',

            'value': {
                '^': 'float_list',
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
            'catalog': 'ļˇѓ¯˘ʄаԌϼȺͶ\x94ҿжԭˋyӓlӱ2\x95ϋʶÚќҚАӴΉ',
            'message': 'ĝ˃˯ɼ)ӬĂ҃rʮԜƌř[©оɽgƯµӬџčЦĵѥZIӯƉ',
            'arguments': [
                {
                    'name': 'ŦǙŴȺ·ӅӎŒӒÓ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ʨ͵Ά΅ԅaβ"Ȼѳȑ@ΜɧŖсйǄ˵Ёñϳ²]nʿǂ',
                    'value': {
                            '^': 'string',
                            '$': 'ʸǢӧΧьˣȚѤʖΓϱΆщӄҢңĠƝųǙʔǧȕРԎȠӠơѕȒ',
                        },
                },
                {
                    'name': '\x8dωȕ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        False,
                                        False,
                                        True,
                                        False,
                                        True,
                                        False,
                                        True,
                                        False,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'Ҳ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        False,
                                        False,
                                        False,
                                        False,
                                        True,
                                        False,
                                        True,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ŋέΝǍƍďǆϘ˳ΉзΈʁĭϘƥ,ЙƀάąԪɶ¯ɱƈˮӨ˾ɗ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'Ȁ\x8aщ÷ѕçӼԧ\x9eҨŬçХ˛ŰЍȦҟυәŞЫȎ#ӑĄԐϏԄ˝',
                                        'õÓӐңƻȕɼōɴԣțʾ8˞´Ϛȥα˰Γ˟4êȑϻţӟ˗Ɵɬ',
                                        'љ\x9cɺЋ˰Ψ¦ϋԖŃΜ+ʡΙƨÀ\x87Ξ?ĲԈԥ^иȺɀǑƠЄӛ',
                                        'яǀԞϙˈaƨϫȽԠѣOɟÒӺІġԄДǼ$Ũ҄ÒЂҙʗșŲҊ',
                                        'Ȓɓҫǅ¼ЀΉȮҎϰ±ǢψɈҟɔƑɐϯ˼ĆȚʣŜ£ιƢПĦɏ',
                                        'Ѣ.ѕȤŨǶɀӀƋ/ŒéԃӳĄγÇǋ·ѣB@ŘӌӢ\x95ŌЦʋλ',
                                        'ȿý_Ӭŝŕ˸Ϗԏ˗ΩWƂř+ƑȝĴҺőйҐǣЗĶə˦ŗĨԓ',
                                        '¾Ćϻ`ҴŰǸӗĠѢʂѫȪʺЎƘҫѕΉӁԭԋŢƳɅŤÍbĦΟ',
                                        'ĠѕǨŝÆȄϿčԭЬȐųђSϲѢǚҶ˟П:ɥʤU&ʏΏԙÞӉ',
                                        '+YԄЍɰʷϢˌϾЭȨʛçқD˸śӍǢʣϽ\x86ǫ"ÅŢҿ˶Ԃÿ',
                                    ],
                        },
                },
                {
                    'name': 'țūηˠńӎń˭ӂԅ;ʙƣҬ\u038dT.ԥ˳ɫzМѠѱԓԝÇȝ',
                    'value': {
                            '^': 'string',
                            '$': 'ԩԥȇѯƦˠŢŃÍϟ¨ӋʷφáаԝuuѱȠςžǂȳqʻȊF\x86',
                        },
                },
                {
                    'name': 'ԮΫӄӺǈɿԚˑĸäēˤқЇϣͽ(ä\x82UÛ҂',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        245307.06926759693,
                                        212688.26125064347,
                                        210852.83101949235,
                                        458831.1584577098,
                                        369164.50265005697,
                                        319352.59515323344,
                                        14721.399483755755,
                                        593441.209285337,
                                        732713.1938069401,
                                        427475.8609764223,
                                    ],
                        },
                },
                {
                    'name': 'ȆʛϊɞώƯȪªɘмϲ´ѭѨéƭſˈπ˻ɯыŖǞǶԎѓ˕Əб',
                    'value': {
                            '^': 'int',
                            '$': -6142614239874819519,
                        },
                },
                {
                    'name': '#}ˀǔԎʛЕ0tƑɂѷϾΞƢǚ¥Нҝľ6Ʉ^ȫãрȆӠwƈ',
                    'value': {
                            '^': 'string',
                            '$': 'ȑɋƖПòҌϰЍƅцG`óĔÈԜѡ\x91.çǾ©ΨԛΪͽǁŭ˳®',
                        },
                },
                {
                    'name': 'ђȅĲҗùҺq\x8bȻϛɊΦΧưȑкƇĶñƶ·ӌҨϜĪşŃӹɎԂ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210129:002622.636109:+0000',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Я҈',

            'message': 'Ӱ',

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
            'identifier': 'ơϽƎǲʽ˵ѓΎχӻӐƽţƢїυŗȃōB0ΦĢƯɧ˨ǒ˓ә\x85',
            'categories': [
                'invalid-user-action',
                'internal',
                'file',
                'network',
                'file',
                'os',
                'configuration',
                'configuration',
                'configuration',
                'invalid-user-action',
            ],
            'source': 'Ӵ˖ɣÖű·#ҤȧҸǛδŰϤϊ\x7fȧƾҙþŝɏɎǻνάýÄǢ.',
            'corrective_action': {
                'catalog': 'қ<ʘˆĜԤɸēѮγЏ,ӝȌЪIʹɝµõƇϝͶѶŷɃã=ɧƦ',
                'message': '˶қĩ²ЁÍ"Ũ|ԨͷђӿҙЙЈҍȡÞ˳Њά˫ÿʹ˗ΙѝoϾ',
                'arguments': [
                    {
                            'name': 'ɿ˒ȊєќǦNkĞ\x9f˂ԦӻΔˉ˚\x99ĩȴӲ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210129:002622.631178:+0000',
                                                        '20210129:002622.631192:+0000',
                                                        '20210129:002622.631198:+0000',
                                                        '20210129:002622.631203:+0000',
                                                        '20210129:002622.631220:+0000',
                                                        '20210129:002622.631225:+0000',
                                                        '20210129:002622.631229:+0000',
                                                        '20210129:002622.631234:+0000',
                                                        '20210129:002622.631238:+0000',
                                                        '20210129:002622.631242:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǸψҮƍҲŨɬѸ#jѳӣ\x7fЍҽμǎѡЏ˓Ĉ˺ˏӵǝĵçΈԊҗ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ĢȧČʴȈśƴʙǆͳ˔ԦưʢœϰӶˏɊҕ\x98ȳͻĢβʹǒ\x86ΰр',
                                    },
                        },
                    {
                            'name': 'ɍҖƌƁӅίȥnϳʉӷˮÇŉǄǚˏƤǈԡԙ˭ѱƩ˒ѮŹ\xa0øƄ',
                            'value': {
                                        '^': 'float',
                                        '$': 212830.2978275097,
                                    },
                        },
                    {
                            'name': 'ǻӠĮѓ҆ȅ3ͳƩƇȵÊ~ĤèѻƜňԧӥԇǚҸ\x9dϻѤеиӝҒ',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210129:002622.631754:+0000',
                                                        '20210129:002622.631764:+0000',
                                                        '20210129:002622.631769:+0000',
                                                        '20210129:002622.631774:+0000',
                                                        '20210129:002622.631778:+0000',
                                                        '20210129:002622.631782:+0000',
                                                        '20210129:002622.631787:+0000',
                                                        '20210129:002622.631791:+0000',
                                                        '20210129:002622.631796:+0000',
                                                        '20210129:002622.631800:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ǱʱķȊʆɝγчØǑǀ\u038b˻ϋʝ\x94',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        6817781901262499163,
                                                        6049820680671750664,
                                                        4800605456647666911,
                                                        4386850296894856775,
                                                        8298397606880369129,
                                                        340015518348929864,
                                                        -6469599926660927060,
                                                        -3327979351411051237,
                                                        3422885719724711430,
                                                        18729467485378645,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӥӰǠěӿǩˇкàΌʈӮƻsÈϝʘī',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        -83733.05675954044,
                                                        -64072.05334147664,
                                                        264231.5509464526,
                                                        490798.8263036305,
                                                        208323.21343792207,
                                                        964775.0872091914,
                                                        313202.35824459884,
                                                        597000.7173575159,
                                                        571731.0829555378,
                                                        479895.9656671783,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ˉцıӛɷťͿѓűЁʜЮpǊԭΑ,ЌÄi҅ɩТ\x96Ãϭʖ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        6261067090279166693,
                                                        -8642434101694968684,
                                                        -8107606393756109499,
                                                        1233982987913635720,
                                                        -7435705076710612284,
                                                        5494372861314553316,
                                                        -2738068064280139451,
                                                        9082643105385305147,
                                                        5405927015318103682,
                                                        -812071036810452399,
                                                    ],
                                    },
                        },
                    {
                            'name': '\u0380ŤкɼģѧĶǁΞԪˬҙпȤӋӼ˪ąŋōÉÍпǎ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ȪΤ˂ѾȠʜΏāЛлȕaə\x85Ǖ˂ҭPɩʛǡԡɓJƍз˟Ήɉď',
                                    },
                        },
                    {
                            'name': 'Θι˽Ǜǧ\x94цɼUʼͲЖƑǀоӛӰʤĖ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ʴćƬGʛѣŨǭГǼÙƛΞĸӇȬÞȪȎʀť˕Ӊǹ¾ϭŹӀ\u0382Ș',
                            'value': {
                                        '^': 'float',
                                        '$': 762541.3054959314,
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ҳΩ͵ûέϗϤȘѪɛдȶΗĈŵʑϰʌÙԩƙ˶β]ʡ\x9eӏӯŘ\x9d',
                'message': '²˵/юΏѾӅѫЀħԖͺҠιӓʗǼͼłӲ\x88ǂĖÑʇӃǄψϲϥ',
                'arguments': [
                    {
                            'name': '<ǢÇ«ϝиʏИǢ2ũτƩДѵ',
                            'value': {
                                        '^': 'int',
                                        '$': 6125138561359209975,
                                    },
                        },
                    {
                            'name': "ǃϰɣӋ'ɈǉОPԆȀNȁЩżúĒʰӼ§ϺϣƉ\xa0ЉŻǨǍςΰ",
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        123641.84788443049,
                                                        620589.8170185678,
                                                        878899.2591456863,
                                                        681093.5518370267,
                                                        341746.2107528385,
                                                        44292.89607744024,
                                                        715083.905531638,
                                                        995752.4005137843,
                                                        321467.66290203616,
                                                        542817.8800563161,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӢŴϚÒϡҶЕȟϡҥđűˌȕǄЦѲȆҮǃΈҹϨЗȋӘϮԅȓj',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
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
                            'name': 'ǈȾПɥ#éɥƼЎÉȠ~åӘɔΛЈҾĢџı',
                            'value': {
                                        '^': 'int',
                                        '$': 2779001496757817172,
                                    },
                        },
                    {
                            'name': 'ɗкХȐϞɡǊƴˑſɖ$ʗû;\u0379˅Кǔ\u0382ŞԐњŚлδӌϳъƠ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        False,
                                                        True,
                                                        False,
                                                        False,
                                                        False,
                                                        False,
                                                        False,
                                                        False,
                                                        False,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ԚĒĦȕȘˍ˂ʆэĘɾñȇɩ\xa0Ǿȭö\u03a2ƚԝҽȀƣˈ?ñѯ\x83Ԧ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210129:002622.639181:+0000',
                                    },
                        },
                    {
                            'name': 'ʞ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
                                                        False,
                                                        False,
                                                        True,
                                                        False,
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
                            'name': 'ϟΉΥфϩȟžƐƄDԥʎÄѷӟ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': 'ȼBζʱЋúΰʈˆīØγàȢTϗʛ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        351512.84109815146,
                                                        -72778.42026352987,
                                                        319981.88174038957,
                                                        946781.3466653046,
                                                        785023.423082803,
                                                        271432.3089256781,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ʹαǾ×ӹʿ˩ÞÖǭġȼԄ¶Uƥϑ˰\x94ҮˠŻƷӀ\x88ɏƤӹӜI',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ˍʘȫӓУ',

            'categories': [
                'invalid-user-action',
            ],

            'error_message': {
                'catalog': 'ѧ<',
                'message': 'ĳ',
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
            'name': '}ĩФϚ®ʑ!ĥŤΞѱҭЊǍ\u0380ʁˤȳԀӂǲ˾ǅǏӎȤǐêё¸',
            'error': {
                'identifier': 'ƔʹĿÒӎʧʎѷÓΩƃŰÔƍ˻ԛCőɦԀ®ÒԊ˝Ȍ\x9dϚϩǸƆ',
                'categories': [
                    'invalid-user-action',
                    'invalid-user-action',
                    'file',
                    'os',
                    'configuration',
                    'access-restriction',
                    'network',
                    'invalid-user-action',
                    'file',
                    'access-restriction',
                ],
                'source': '҄ŭщǾǰ\u0380ѕӚĽŤĤİҌɺɰŦêя6čˊÖϛˌŕɕd\x95δȓ',
                'corrective_action': {
                    'catalog': 'ȥĦOҩžȺӖOoѾԜψȮŸǲ\\¢ѠУɸ\x83˼ƖϤӼÂ\x96Rņџ',
                    'message': 'ȾѶѨȉŔOǡoԣКϔĉ\u0382гÙɽſÁЇͼɈ˱Ƨƿ¦ǏƍŹğż',
                    'arguments': [
                            {
                                        'name': 'Ϧ3Ųϔʐ˟ÛjŚѲˮȵƮ\x9fĕ˒ğɬЈȲ]˅ǥʊĵʛǠƋǒ:',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7856982543456113720,
                                                                            1621119309849454272,
                                                                            1546033150865369489,
                                                                            -4396222632646221853,
                                                                            -86979534918697749,
                                                                            -8749450449509640521,
                                                                            -2778281092122339509,
                                                                            -104800521210164003,
                                                                            -5387138276622670370,
                                                                            -5138004970977857033,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӷŖĮΩ|Ǧɀ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210129:002622.625976:+0000',
                                                                            '20210129:002622.626017:+0000',
                                                                            '20210129:002622.626024:+0000',
                                                                            '20210129:002622.626029:+0000',
                                                                            '20210129:002622.626034:+0000',
                                                                            '20210129:002622.626039:+0000',
                                                                            '20210129:002622.626044:+0000',
                                                                            '20210129:002622.626049:+0000',
                                                                            '20210129:002622.626053:+0000',
                                                                            '20210129:002622.626058:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'áȍ˼',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'йĴKŘǳȢÑȨĲҴ1÷˂ѿøʚϧЄYϪ¯ѯЍ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210129:002622.626512:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʉΠǃ³_Ǒʕ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƕҲӲӔϹӎӴĥXҟҡJÅ˒Ӕ\x93ҳʵԣϷџЙƠіD˹ÀНΑ\x9d',
                                                    },
                                    },
                            {
                                        'name': 'ɮϻĈЪԊî˘Ҙ/Γ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6463622103522450414,
                                                                            2582634683333821686,
                                                                            8171289957136755766,
                                                                            -7441497109046639099,
                                                                            -5935850427314255299,
                                                                            -8651620922325461553,
                                                                            3891761637316667342,
                                                                            -6416254251829370737,
                                                                            4224361994380908036,
                                                                            -9093670947473716032,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҀΨʹĪԢэϧ?ǖő\u0379±ӇӐįΡʟÈǰċǋ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĭПɼΊãɑѬȦҮӶɻ\x86˟ӴӖќҾĬL˛ыɓȪP҉\x7fʵĭç˩',
                                                    },
                                    },
                            {
                                        'name': 'ӎŢƳʢӮЌĐ3ɪáϬ˖ЃɈĺͻEѽSĲҸҡƨǸßβĩϢ˭ŵ',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӠuѸɖдρѵδ<ϙԐƵѪҳȁ!Ƥ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 530677.5688074512,
                                                    },
                                    },
                            {
                                        'name': 'ǵˎоҿǲ?ŠϥҙɑƉԇʔűȘHň˳˚\x9cďʘӘƤҫӴҫƂыþ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 371081.1226126281,
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'γ+ЦÝʚѰkȯӪϖ¯ʛԭʞωȇ¼ǤҰΣKJǯϹкЧгǔςł',
                    'message': 'ҟǷȸщԎÉǐӈаʨ¨>ӸʄʉĖԮҢ\x86Ӈ\xadӓӠȦöǪˊԦŻΞ',
                    'arguments': [
                            {
                                        'name': 'vȌҢʲʫġʦ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȧҹǦӂƙѭмʽɽԉȬțɐŊfkДі\x87ĭɎўŷԍÞȥ϶°ǖ\x84',
                                                    },
                                    },
                            {
                                        'name': 'ҵΗπӈпǦ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'щŦмʨѼɲıˇϕԨѳĦèЁ+\x97Ǽxǎƅӱʏϊ϶ƳȳМАξ˄',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4384199790959871639,
                                                                            6262044881693471086,
                                                                            -6077219396162347463,
                                                                            8387261786572655547,
                                                                            2055141214532571316,
                                                                            4079532094140145185,
                                                                            812833012679382326,
                                                                            -3005215956244716810,
                                                                            7756286032714804506,
                                                                            4724480647575071991,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƐԛσƺɿπʢӝŲǤς',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210129:002622.628632:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ŧ˩ÆѢƝɡʰ˘sQӼǟҡ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȠʀԄċ\x89ɚ˨ˇ\x9aӷĳƩȿĚԌϜĚʈčƖʏӻǒ˝ˏӐλӻċЁ',
                                                                            'ßzүÆѸšӌԋ´ƛûȲ˒ͺə˦ψöСȂɬƧοƧѵҹΑǹœ}',
                                                                            "˱Ԯ˲ð˼\x94ɴçb'SαΦʊ\\Ȯəиӆґ¨ĵɲϔӡїÊěԗǪ",
                                                                            'КԆǩ˯ͺőŮwǽΠ˛ѴҎ\x93n˘ρbƒϋџӇӯŊÒϖӒЈѯ=',
                                                                            'ƧȰȨСѸӮΗ˂ʚƪϽǻłþźˡʬöˋrɇαȑӷӆҬʠʞѝΆ',
                                                                            'нÃCĭ±zʏϖҕǮĘɲӋӑ¤ƈƈАͰԥʖąϏƄˉɠƄÀοĺ',
                                                                            'Ԕ˕ƛтͺœӻčǻʧӉȍľϟÿ˯ԑƑҷȜúɻϿԖǨѓƽЉȸ9',
                                                                            'ХƟҴѯЀʓȹϱ3ĔɶŒӽŻÉ҄ʒϝǥȿϲӉŘϗľȄ˂ɭӋ\x97',
                                                                            'ϽӲΝҍdǬǊ\u038dʜҔϊʗԪњψЖēoVˡʿӇϿ\x9aȪѐ ʡǡˡ',
                                                                            'ȇҊ5і˱ĴҎӺ\x8cřƒʹӚƮΆӆÛϗ|Ͳ{ьŗ\x83ƫŃВCȔΞ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԁѬƁϓƽӽҾţäǆ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7205265406337937776,
                                                                            7557603478645263445,
                                                                            -8394810149288440409,
                                                                            -4315403155482346385,
                                                                            3172124706210704369,
                                                                            -1956565234726148310,
                                                                            7774020038751766379,
                                                                            2095188419977842341,
                                                                            8149722296730700452,
                                                                            -1277989170697420442,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'F',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210129:002622.629413:+0000',
                                                                            '20210129:002622.629423:+0000',
                                                                            '20210129:002622.629429:+0000',
                                                                            '20210129:002622.629434:+0000',
                                                                            '20210129:002622.629438:+0000',
                                                                            '20210129:002622.629443:+0000',
                                                                            '20210129:002622.629448:+0000',
                                                                            '20210129:002622.629452:+0000',
                                                                            '20210129:002622.629457:+0000',
                                                                            '20210129:002622.629461:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȅmђЮäѥÖĚσԦʃɈƟ¼ԝл˅ЩԇȍȉƛˎǭˎƠȒΑĨI',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҥЉΒƻ1ÃĈΨjѩԟӲü˚îҁɡϜŇͿӤȊωþуÎǃӾ\x92ʏ',
                                                    },
                                    },
                            {
                                        'name': 'Ø\x9aUǝжЏǱˢN\x91\u038dȴȐšʠϚψ˂å',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 715103.9467122515,
                                                    },
                                    },
                            {
                                        'name': 'ϲûɮãзȘ˹\x9fÅÎӀσσɱήҁӔєĔěŸʴԘ˲бѝzѲΧȿ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '/\x82ńѷψԕQƩαˮ\x84ӴĝɒĵHɱÊɥҒlȺĠɁѠėЦϳԖǢ',
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

            'name': 'ЯȮȟ',

            'error': {
                'identifier': 'вΐĈɻŶ',
                'categories': [
                    'invalid-user-action',
                ],
                'error_message': {
                    'catalog': 'Īχ',
                    'message': 'ӌ',
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

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='event_id', name='EventTarget'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='target_id', name='EventTarget'),
            ),

        ),
    ),

]


EVENT_TARGET_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'event_id': 'ͱ\x93˞Ӵѷ²ɧсŔ˖ȞÚƸɶԝ\x9bφǐͰǹþǅǹùҤ˖žȞ΅ε',
            'target_id': 'ÜҏƨçŧθþìϒÚϻ<Ԥ\x8d@Ʒζ˨ɢƼȳ\u0381ȄĿЌ϶ңӽˢa',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'event_id': 'ӳςҙ˚˥',

            'target_id': 'ӌΦёӤʩ',

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
                    'event_id': '4ĜŉɲÛҧѣéю˙ơүВɇý2țӱԓБѭӅaA!kƒЧƩӥ',
                    'target_id': 'ʇęёǞȗɆ|НƠ9ңŶ8ӛ҄ѭwÄɄϻʨŷӠωŬǕʡȔчѲ',
                },
                {
                    'event_id': 'ƠѴϸӵȹʌĀҭƭɛѮЎĽԄыoҔˤˋ˗˚ѯѵϕĶ¿ӭĩҭ\x99',
                    'target_id': 'ɰªÑǓǧğьҊӫÑИ϶îѲϹƺΥӔʈӇ\u0383ȻɜǤφƛЍɃ£ŷ',
                },
                {
                    'event_id': '˅ЃĸĲϫ©ÿ\x85ЁƿӲĈƉоԪî˨ΠŵƉnĴњ|xɣԅțҾĮ',
                    'target_id': '˗ԎʆȃρИŗʣÃùĒǟưźÓÎɄ\x95ĄϺđǿşң϶Ζɞ\x88\x9fЫ',
                },
                {
                    'event_id': '}ȷȗʛӟ\x81Ÿ\x90ǗСʆѻ{\x86ƯǐԂɼĖƶj\u0381ойД\x9fĄϺΰʞ',
                    'target_id': '?µʾΔæϰɀԓê\x95ɼѵɡŅƫλǲǪ#βҐǄ#ɡ',
                },
                {
                    'event_id': 'ǫ\u0383ơȺӉρßĲȡҐρǢƟǃҧӎѺͼ·ǘ\x86ΎΟɦŏʇʐѝɉȔ',
                    'target_id': 'ʑ\u0382ˠİäͼ˒ΆȭўTǾҹíƪ\u0383_уŇˑÅǆŬ\x8dĺ[Ǩ˞µ\x9c',
                },
                {
                    'event_id': 'ĺԢ6ơ@;ʬȵ:*ȱКϯзɦ3ǫ¥ɖǼɭʂ\x84ǋǟ˯Фƀ¨Ь',
                    'target_id': 'ӮԆ\x8d¸ʀѵųϕӧʠҐϊвʬéŕSγõJΆȞ:úҒçƜœʅӬ',
                },
                {
                    'event_id': 'ԌкƘЎӻϮҭ3ЗЩԨšŜһϕřƓϽӳѨȴĐθ˾Ɍ\x92ǴѪ\x91ƀ',
                    'target_id': 'ҥŻ"ǨЂǹҡʚ϶Ȥ¾ʁƾ˓Ŀ©ÃũҘ˄śǱӉʈν\u0378NȨѨн',
                },
                {
                    'event_id': 'ʊŧ˱TӼűԜӿԛљξ(Ȗ\u03a2ԦȫǰϽi£ӻƏԁe#®ǐѨѹʵ',
                    'target_id': 'Æˁ2æ+ȠӘñʭŪϷѷ˸ńæѡʹAòƾѬǯɡԌƌРưʜī\x8b',
                },
                {
                    'event_id': 'UȀĠѺĤ\x94ӗȥӈȹǵԒę\x83ƎʧɝВČƣêėԥԒƺŞԕϯ,\x87',
                    'target_id': '-Ι˚ÏλǉGϧ.гӟԓɾÏҰƺ϶˩ć|ȀŜәϞύĐɇ)Ʃӝ',
                },
                {
                    'event_id': 'УҀϪЕлáʱΠЅķŶʰЬΩϗŝˁʖҟҥ\u038d]ӭӾüǯô¼Ƙë',
                    'target_id': 'ƲΕ˯Ǉȋʖϒ^ЏϤʹ\x8dˎΝĤĿѡѯÕŰɼüӗʪ˷ƞŰεSú',
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
                    'event_id': '\u0381Őϴíɤ¡ȢʨĿъ½ӯȮнѷɍВʗϐӖƐėɬLӭǡɧӐӹË',
                    'target_id': 'ÖԍXūӊҍ#ӝ¹ЏǴƐȋȸœ·ʠƤΡΑŬԘNioԀƫµԠ:',
                },
                {
                    'event_id': 'ɷǲë\xa0ɴԧĈǋϮϲÒrԙP£ȣѷ\u0381ÓƌԌȏӴХȨ\u038b(үЃҀ',
                    'target_id': 'Ę¢˷4ȈÃ˲ť}ȢɒҥΗ\x96Ɵā#ƐћƸƿǒ§ĝǃӕaʅҸť',
                },
                {
                    'event_id': 'ɸԀ=ĢȌɅɗōsļ»ɨħύŌȃʬԭА¥˕ʗҬȊ9ƄԊ˾ȎШ',
                    'target_id': '\u0380őΔÄÀԝǻɜίӑĥӳɨѱǓǼϏȻӌŋƜѪȟ©҇ϤЇöʇ˟',
                },
                {
                    'event_id': 'ҜȄcȻșȣ\x9fΕΘˀȟƘЙНŋӲЪҨюӞȚšЇˆСРʭũԐҊ',
                    'target_id': 'ΜƂƜƻ½êӞΙÊӤm\x83\x8bΎ¸ɓΝзĕˌğӥ˛ҭԅ\x92ѦƿlǞ',
                },
                {
                    'event_id': "ÚҎΣͻӠɩӆ'҄N/ɆΏΉ'ŜŝҡȹÈ8ϔ҂Ѐƛ®ԜҀƔУ",
                    'target_id': '\x9c(Ԉ\x90ҺľɇϬ϶ɃҦ\x86şÈĹʐц˴É§ŁϡǫǆƴͲ҇Ĉб˪',
                },
                {
                    'event_id': 'AƾȒÚɱƜƮѓъёƓΒľҞˈ\x91ǘψѬŻʷʔԫˊψѯӡωöф',
                    'target_id': 'Ʃʣ¹ԞɾВǳʼƁëǙЧÌʛЧ[Ґǒŏiǻ˶ ®\u038dðïȲƉé',
                },
                {
                    'event_id': 'ѣӁsʂ-ϘΣ©ȝўΎǼΤςãЖȗ˞ǛǩԭӁ6ɦǍÇҬηƉƞ',
                    'target_id': 'ɍ;ôʺʗпЂɹŕʏė˰Y\x93Ԧ\x95˹˚ïƕсʞҳđҵǏǏиԆ\u0378',
                },
                {
                    'event_id': 'ӗʚŅżæÐԈȻѷгвЃƯъΫǾӈҮѼăuԛɛȥ\x94ňѽˎӉΑ',
                    'target_id': 'Ӣ½ʀƮϺƥǰɅϘǑ8\x89',
                },
                {
                    'event_id': 'ɖʶýЇęҩǆɫѯώ®΅£¬ǎƯlщ\x99ϠǃǬǪʩʏ7ӛ˻ƺʟ',
                    'target_id': 'ˈнОyДӵ\x84ӢԖƪ\u0380ÍΤěǫүҞǀÒɿůzý϶vřV\u0381θԡ',
                },
                {
                    'event_id': 'ЋŰ\u03a2ѥҖʮҁ_ˇħǞġǙҦ"×ğƁѢҫæҶҶŐ˧ȆʍͺДҪ',
                    'target_id': 'ʽ˸ԎȖѓɲđľÎüȹΦδŁƣ\x90\x8bӠɧЈІƒєѦԦ\x88ГƚŊ.',
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
