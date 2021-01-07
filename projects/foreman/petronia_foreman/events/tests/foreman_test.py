# GENERATED CODE - DO NOT MODIFY
# Created on 2021-01-06T22:34:10.017992

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
            'action': 'ϘѧқΣŢӢƇ˺OıĚɍǰʝӥХƇϠɪĨ\x9bÞɹńăȳӂɪ˘У',
            'resources': [
                'Ϩȏ˅ʾѧɐMȪċ˞ĒǽсςȄȄȇǄшԋϱǫĞűҹѹǭѹԝӭ',
                'Ѩϭϼo\u038dЀɥΉ\x81аПΛӧ½ĨτNˡϷӑÇʊÓʻƭǽʿĳ˄Ş',
                'ȇԄ˟\x8fԣÍ˴aɸΝЎ҆Ҥȧ˱ѱ×ĖŮȵ˲ǓƟ˖\x92˩ԫǁЏϱ',
                'ϑɑäκÙƳӎŷӣˈќɀØыΪǢѣɩԦȋćșzǩȄŽǞŤΕљ',
                'ɠǧfĶϲƅӈϘԃʵ§ɰ˕ϭ,¸ƍƏĴέǗѭɓͼίćђƎӃƱ',
                'ӖǠɝƩӵÝœ\x87ДD\x8a·҅ʹКãņɶAȚǹƚįˀĊƵ҇Dˢʹ',
                'Ӌϝȭ˞oɥɵTțԘŮlÙĔʢăҶȤ·ǟǧӲӢ˟ˏĨȾ¦ͺƉ',
                'Ů¨ТΈҲǜӆÈƕƹĞ\x86iş<ÙĶ˹\x9eӆ\u03a2іčΨӨŬϨѾ˧-',
                'ɫӏϥȹ\x7fȜ\x81ďʶӹÎӖЋǠÿř3лҧҸ˹ϧчűŠŚИɭÆʑ',
                'ùɹиĶİɐŏɎßƶԟžʄǍɨ\u0378ͼàɜǵŵǌԖʴPˆԟõđз',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'ʎ',

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
            'identifier': '\x8dˊαѻʪϖƌ²ÕѿÓdʕɳӡʍǿѳοēʀȤЃɉυ?мϦǍè',
            'launcher': 'ȵɠї\x96Ҭŧκ\x87Ǟÿι\xa0ȒɶҒ\x92˳ɓϵ[nPЖˆɇƤ\x85νļƁ',
            'permissions': [
                {
                    'action': 'їßͿ',
                    'resources': [
                            'ϾѱŹĲȮǟМʅǬĎʃƥαɯƢϔȶɒԑ·Ԧʶ9˃УŃǑұrϓ',
                            'ȯɰƉ˝ЭѳáɬɉѲʇ\\ӷéǃàˬ;ǫǪÇµŇǛĠčѼɑ6Ŋ',
                            '¼Ňɜ¾ÆϟӖӹ\x8fαҒëҾΰЫĮŵȠɗ@ϔFҲƼȜВŘпП8',
                            'ϜʧҞҽƟɼȢřŐə˭ЃŦ˚ΚЅưx˷ɃǡеЌhҿțȬ%ȥӴ',
                            'ϻ_ʢҴь\x8fϲЄÇɡʘɁcҠǃџӀνβԙo¦ԏΩѥϝӮԢďГ',
                            '"ȏʦ\'ӥƠΪʚɓСqƂ¾ˊȡʪЊǊĩƁѶюђzɊѥƔЩʔQ',
                            'ǂƇƕЍͿǬùōˎżƶɨaɥΐϥʝɉӰ&ӷø˨ȌҌ˶ʜƶЊ;',
                            'ŜԧӶӖΨ˃ɯԤӕȉҌӇOѠ$ДсĺǑ˞EɾΔȭңǦņŸÿï',
                            'őòřӒůIǋΫӈѝlӭǢʟˊżŕΣǮ¯җƉˉȒ^ǿҘ\x84ſр',
                            'ѣǦȬĿΤѤϏļҬөjƱÉpăˋŁ\x9cƧԅɝХÁʕƯȪϹΓÄǷ',
                        ],
                },
                {
                    'action': 'ϗсEƞЖϦr\x90ΕȵǱОǞңδ',
                    'resources': [
                            'ѹԈį˾тȌѮҘÎԀƅwRӤƄҳХΩăзƷϚ\x87ѕϧľ\x82sĿ×',
                            'ѡθӢʺȄžЧȮ\x97QƔϼӕŊțВʭƱԄëʙɮҭȽǞʻ\x9cÜӑя',
                            'ĮØҞҼ˅џŲǨɫѭȉȸÉ˓ɟĄ˕ȦǕəϔύ҆xӳЎ҉ȢƕȔ',
                            'ĿŝҮ˪сȄšșЇŏӣ\x87ƢåūǻϊΧӑĹʾɶҊŻPɄŬЇķm',
                            'şŬɂʪЫѝѵ·ѹЮ\u03a2ɰƺȎЇӐˮԎŌɼF9ϐаϼѼІƹμӍ',
                            'ũѺĐĄɵѱõԠ<ħğԘеƛƍƮϜІrOϑʰҸǀǺӓǅλϙʨ',
                            'ƀғШgȼƐ˘κǈòԃĜѴ,ʳҴԈќˀ҆ӅɨJӿ˰Ϋʵ˕ɞԝ',
                            'ʟYʦǀˠӣҴǪȅӚUΞȸǋʿƖω˚˒ξÂçѸͺԠ΅ѐΦЫÁ',
                            'ƃĔĜҷƈѓх\x81ԟҊβ=ԃĔѺӌҳѣԣӎɍѨϾǰ˰ŎǽϚȊÖ',
                            'ZɑȯλĸіҸ\x97EΘоӨπȆǰλʤɂðNɳąв˩ӆҷԥÜɰ˺',
                        ],
                },
                {
                    'action': 'ƣ\x8eȼҕѻ˟ÛʛϡȨ\x96ԎϢˌїŷȩЭƉĞɾʳŉȤҹʄǠѩҸτ',
                    'resources': [
                            'ԅșрчҗʾyөϻƺˀǃȽŉɶÓ7ʉѿǌԐƜǴҁѴяƽʊ˖Ь',
                            'ѫ˷ΣϏӡɦǶɉʓʁϖϺ˾ΗƅĖʇT³¥ҼƕϙъŖÉȞРąа',
                            'īЯʂѯʗȟςșʀǳ\x95˵АgȰϡ˟ӴɴĜєƶªЈȢп@ȝǻԠ',
                            'чҥ9ÙȳʱƐǒŅ˺БԅћģԐɓʉԨɪи˨(`ō˗ÿǡȇӔ˄',
                            'ȻҧҕȚϤˑϣ˚đїʊӤҸϱғϗ\x98ÝĽʾ\x88ϵ\x81îđѶŚѫ·ς',
                            '«|ЏӔčϦԩǌɟƿҋԞЅʖӇ˥ÌχGɣ[Sƫʨȅӣ\xadͶȆΖ',
                            'ĿÀђϫ{΅5ӊʾԪOөҶʷΪɗȂƫϞѮ˃Ɉ.ǘǓǾЙϢaı',
                            'ʹƏəEȱҾĖȝʩɚƕšҟЖɭԃЇԎΕė˼ә}ǥʭÂɟѐĖԬ',
                            'ϡЎÐïˍ\u0379ÊЉɡȬǃӨ\x99Є\u0381ʎΔùǃЧǝ°°аǣƩҊú5Ŝ',
                            '˛ҡқʌĮΚғŵϜřԉπ]ŕÃϵķĦӺҾφÃɜţı\\&úӄĊ',
                        ],
                },
                {
                    'action': 'Ȥϖb;қυѹͷЙƷӚpȣԥşŻКƴũӝӏɸ\x8eκÃƋ¶˔e.',
                    'resources': [
                            'ԥyŀʾԈ·ƍРɆƸϤŪʟԭƿ˪нʟɵΖßǬχąċǊԆіҔğ',
                            '˵²ǁɬ}Úz\u0381ʰԪȪƏԫġǴ(òΊѭƅѵĄĹӪοϋ˨3Šȧ',
                            'ɎЏ҈ȩzÜѭԠѦƜĩ8`ɃТЬʓѱЄМ=ƙъΆƴ҅ƪӲЮз',
                            'ǒvϏȊwѡÓoԜͷȟɂ\x9dшŭɝӻН:ɷħøтłďΒԠҺйŔ',
                            'Ȣk\x89|ʋȇҼHҙҸǨLc>ұһĖӠƼԊϔʝɟĸʇDщHΜͱ',
                            'ԫĚɬɠȈĿ\x8aВЬӹʂ\x9eɨбѥӗɄuòΆѩJќƚύ џĊȓ˫',
                            'ʫ˔ȋʄgҁѝƢ\x91ƃƥŵ3ɴŏŃʪƌȄЄ˻,´Ѧũѵ@ʝɤx',
                            'ɹţϘπ{ϑǋŽԠѩЪδġƒϫwƷԬİȤĤpӻƑt-ЉӹНҵ',
                            'гс\u0383ЪJŉýˊaҕ\x8csăԛѶɇ2ǷʺÛïΟŘǿР\x81Ǝcŗԉ',
                            'ʆɖʖƓϑЕɸδʀĴƺɆɮŜɗԐĻүOԒӇŞԍĬÛLřҩðɆ',
                        ],
                },
                {
                    'action': 'ϒTȀʷІʷĮȉӉηǙǸɐʻюäÂȆϫ\x92њ\x8eŃɀЕІВҗ˞ŭ',
                    'resources': [
                            'ҽү0ĐЫɟѢгϋZ˚ŏÄŉΟлҿĢǩҵ\x91ωȥβɪ΅ǭâԜˬ',
                            '˽\x8b\x95ɟʯ¾ѪǯϽЇϏĘÕФÍϝӕŧè;ˣ=яUӍԙӼɣǞӵ',
                            'ěōȏҡĦ1ȶǓҘųÜcŋҩiȨћήģɛήʢȀǝε;ʺϼǐ҃',
                            'ȮËɤӥͶʟͲʅɎʷóǱ˽ȖŝȌ&\u0383ƥřʧүĶĽHԋҜӍɕҴ',
                            'ÊMâŁѱіɣƗь˲țƓĪ½ăĸɨǬϔǂ®ǹеĖaԝѢʰҙČ',
                            '\x84ŝŷчɐπƘjέĠƣ\x8aѯрlԛҮϟȖԇĞͶʈǫǰˌͰưӞњ',
                            'ºԉеӵЏЦңÆүɹҞƔйÿ^ʫ҇˹Ž¹ԣͼ]ψÁȭάcďԁ',
                            '¡Ӄ҂ÚНΏƳϯȻӈжƘʠˀҀȼǨȬŤҤϏɭɶɫ˅ƈŅĪʀ;',
                            'Ě÷ӳΜрМƳԙȍӏӌӸ҉ƏўțӒt]¸ƹγftӶƥřǰȮ÷',
                            'ҐĕDϸжȢǾ˕ΧƬԢɡϪʽӇƩӉҾͳűʬѤʧâŻKΪȨΑ"',
                        ],
                },
                {
                    'action': 'ҕӆΔͳӽˁÝȍƘћѕɃȘԘͿсǝκø)ǦƬĜɜЀβӛêźƧ',
                    'resources': [
                            '\x9dȢңĠǀÕͱȫɌ"Я˧ϦʺФӂŒʣBԓĢÇҐƢȖàr\xadйҴ',
                            'щʊɮÕӐвĲћӒƋ;˧Ϟʥ϶һӨˢͼǽȔP\x9fçŢȄӝÌǗʖ',
                            'tөʔѫΣ[ʻiɘІͱϿԏ˞ŲҺƶʞĒčŧ˲ĉζϯӦʻϠʓɻ',
                            'ѥКľƵ\x80ʰĬԔz1ũѲƊɂʶʲєŎεʀ\x93ʫѨЖѸƯѕČҖ\x98',
                            'єԀЧҠѴ.θŚόͳʈ\x9fʹРЂƼЁӖǎɷҮƀķҊԤϏϢĳÆE',
                            '҂ǩǤӻϦ:Ɵũͻýȑʨ\x85ԧȏҸ·ǅȞҏʙϾ9ˈĵ4Υċ˪š',
                            'ɗčѲŋƅ҄ҕɰāͱӺмѮӈц)òѣŤɶÖԫζĈɆ˰ZΧȍћ',
                            'άˤ/rϏĄϣWĚΓҥƠˎɁЪɾƒÕåkjǰʘʡԥɻȷѹή¼',
                            'қЎҏ2ϵѦӹǖ\u038dÚʿȵ\x8fς\x8aƖĀ\x83ҟНͻϧãø÷ѲʴǬҥЖ',
                            '2ӳâԃÑÛʕŇ!őҘÄВ˭ǔӉХҗˤ$ÈϟЄӨĒҖDеɄ˜',
                        ],
                },
                {
                    'action': 'ƿ˪;ǧӽŷˈźPщïҠΔĖΝȦ©ƆǱsĿҘǤӲƥȬƟŝ',
                    'resources': [
                            'ƍԤŝʱ˕µˋљǐɯȚŠХҡĉя÷Â[ϐɰНʧʝǬПɲǰ\x8fȀ',
                            '˙˜ʂӸŭΘϣɧ\u038dɌƺǠZ>\x9bƫʙȄԡŗ˫"˖ҩÏĩŁzÒί',
                            'ȠӎӒşâǵЁ·ȤľʤʲȟĶǈЈѸǻƶ¦ʱΎɍΣɊǇъǮĔƧ',
                            'ȃˣ˵αÂϷʒŮ˭1\u0379ȓt\x83ӚtÊĶƔªӥ#ϺiЋÌЪʮɌÏ',
                            'иʢćǕЙ˵XȱƮȤѧбқɦɢϹο¶p˓˲ëӡǊȶė÷ŀԊν',
                            'ʷͰőѨΊҤįȔЋВ7ҡVш˔нEрɔðƟ@ʲѺӝІĮSЈC',
                            'ӣͶÇ˽ʽǆĎϳȲѺɲʧĿτ\x98ƉſǇŪѤϑЋę"ΛȍǴċζʯ',
                            '&ϏœҮɗҀҔҥϨŞвɼѢԥǤү=ßϛƤźΏ·ҷXĎԒƗȦƾ',
                            'ƙΥ\x95ɖȊѕĶʔŅЫ\x86Lԡ[Ĕ\x88ʶԆӿӋԆˏŔʞƕѲǤǠǯӞ',
                            'ƨӐϠ\x89\x85ОÔуȥНͶǏȾƂԘÉΐƷ¾ȝĞȟɮQŴɔйԀҫ¸',
                        ],
                },
                {
                    'action': 'ҟǢˠPäˌɘǺʊҷԨФѶʠ҃ɚȩ\x81ˏƳ˴ϯŖέΝRĤ\x92|í',
                    'resources': [
                            'ϋЇ˦ӚͰƒІkǔĸΉqC\x94ԛʟr˼ɵʞӍДΜēÖǯϓΛ˷ŀ',
                            'ѱ\x91ɓϳİǈ˳ɇƖǮϨȕŹȨˡƒԅoƇͽΟӳϔŃ±dɭrʘ+',
                            'Ѝϟȃéơԓʢѷ\x92ũƛԊǓƕԢTϚΔˁңƹΩͱʑʊ\u038b\x86\u0378Ӑњ',
                            'ĸŊn+ɒƭƥǊƲјāѓĝéΉϊgČƾɛ3Ĩ\x9bǖǨԃȣ^Č\x82',
                            '\x9aӀƢŪɜӏҾԛƟʔ\x96îRϻüΝʢЙƃӅԎѝȝŢƨƪȺ\x9aħџ',
                            'ЅBЊÆŝΦύҧ4ĖŘӢи³ÞΛƻʄԙӧĖșɲɡˤʼĻŢѹō',
                            'ƸӗʱϏѱЫӏ҄¾қӞɵĂʸӉ_Є\x9eƸ˦иÒѼÞ˹ɰ(ɜɛǯ',
                            'ԫã¢ͷԃˣԘǾŅҕɛΪƃ²ůʳōЯҗʬαBĈ˟ȕɓѴѥйΰ',
                            'ΟpŁƢӅōnIȟѼ®˵ŗћǏʵɭöèǕŋұκÎψоΫɗɯГ',
                            'gŻұԆƻѓϫϲӦ˩ǃӜөԡZч˩ĂԢȹ˜ЕӜҧӽɖҿҼƺұ',
                        ],
                },
                {
                    'action': 'Ȇ\x94Ӕ¶ԥδόǐϗƪʅ"ȷ¼ƀϿɔÔǮԠŻƢЋxĪϘĢǢѐg',
                    'resources': [
                            'ѷʙӯȃѩҙīЫʝҀɇҥȧÃƶɼȥʅӚľԓ\x86ɼЪϼǢďҏĆԛ',
                            'ĀДѻ6Ϻɧǩ³ϙӧ\u03a2Ԫѡ×КӊƷӦʟǉ\xa0ǜƏАƩyҵǙNҺ',
                            '8Ʈφɒ·\x9bǸúϼԘӮӾӾɢ,Ŗ͵ФǞŹҤɑĪТ¯ӿѯάɍĊ',
                            'ѧąʚԡcΜӸƎϞӜ˺\x89αȯҐԜ\u038d\\ѝĢɆȇďÁҟȳǭдƢ҈',
                            '¤ǈȻʋɹʡ\u038dȼŘˀţцnσ;œɞ"ŨͱˬъåҒŧџϬǥρ˲',
                            'σЛψГԆ\x80ǎÈ×}˾ȄȅpǷþұҫЫґūοѺŨĢčΕʮ˧ƚ',
                            'Ǆ\x85ҝлӁԐˋyƴʮbԎʖԆ\x92ѫӑː¯џIϹǙʿ˯ʫΒŇ\u0381ˬ',
                            'ĹЧ\x99aӛЄǨ\x9a»Ѐ\x8bӌƼČɘѨȰG\x8cԓÔɤȼҨǐοˁpлʐ',
                            'ȎΥӒЌɚĻɀƈƨ\u038bϜɃˍ˂ŢƇȀҿњӟƷЋџԜȢhƯφĐӣ',
                            'DǇɽŻ\xadΓѪ$ҠÐοƫΚƛȠȠőéɚÖӝ˄ҧĀԡũW©Ѩ¤',
                        ],
                },
                {
                    'action': '\x9bƺ±ůΰílрğѳ}ΞҦˤԛΉ\x9cȝ\x96Ƀ˻ʄƺþπɠΌȽŎж',
                    'resources': [
                            'ȟȊ3УĈĖӱїϷӌʌɄЍ\x90ʹϟUÄϙɊØο¶ѠӋԠʞѣƗΜ',
                            'ĵϗĩϫ\x8cʛѿϒҎĭ\x97ҎĔЊȾӖϷΞĺɈƿҘϓƇɾɰɌǺȾ¿',
                            'ѾζÕ\x8dÛ³\x9d×ӓ,ьÕxԪőƏǩϠЃϘǈӫҬԕԙӽФѢŘÈ',
                            'ŴģɃЖǣĹîЅϸԎǳqªɭӨŘәкʘЛ³ƢfҴɇDϣǜϲª',
                            '˷ҎςʇƝƕϯĜƜѥɓ\x9dϧ²өÇ$ήĹГҴĜҴǴĵǪӵϘӿǩ',
                            'ȈɼϳϫҞԮıÅүďɝvЛƎϡƀӰӮϦįƮόӆҫҗ!ʉЬ³Ƈ',
                            'ȞTȊĜѹԛʐŬϫӵӪ˻˦mÛȃӀƗѦȅЇ\u0380ΎҼɴω҈ʎʾ¿',
                            'ΛѰԑƀʭȰyɼӖɖМƒ\x8fϊξ~ɪßрïΞƁ%ќϱ˔Áŏ˩Ƙ',
                            'Ν\x94\u03a2ȲöЀҔҷԤºң\u03a2ʾʤŎǗΨуЂŸ\u038dΑďǎΊĨͰʎǣâ',
                            'ë©ʎƒɼɦҴú¹ŋΎԨ´ßϸÛɿӶϵ¬ΈƬƗοŗϟņϊЕǛ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ɫϐ²',

            'launcher': '9',

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
            'identifier': 'ϚʅϪǵѻüĜÚwɵЇ;\x84ήĶ!ΡȰçƎǑyӦh÷\x8eЀ˒ɯџ',
            'target_id': 'љįŪʋҾăȻĝ˚яʼʾΝȑǽҖšHƘÔʙƲșҲÃɟ}Qěˋ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'џJ5',

            'target_id': 'ѓɒʙԐŬ',

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
            '$': 'ҪʸԞϧҜѫƈҡƊǬpœϫĨҁǻҩȄǒFˑÎʧƈҶƉɨūԪˁ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 1935622727579619471,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 140897.86766738174,
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
            'identifier': 'īʗŅfȚ\x9dɚ~ƦҕªҼȈҪѮǷŌĮƁҀȸ+ǤǆnҒϬΞЯǈ',
            'source': 'ʝƂʉċkɍ!ӌŌ¨ӃȡӔƍѠϮŎɾËŇ,ҾџӍԔӞЖр˘ԁ',
            'message': '˖ƟzʡΠ\x90ҳϮżͿ£ǱˌЂҫɗͽОИʍŞńʟǲӠÚйȗȯȆ',
            'arguments': [
                {
                    '^': 'string',
                    '$': 'Đυʣ\x94ʠμŒʘâѡƲϘāƍ?/ǤћŅԐƢѕѩĆD˜Ԩrώ\x8a',
                },
                {
                    '^': 'string',
                    '$': 'Һϼ·ўVʱӊԖƋʗ8ΰBŴ©ԛТǉϾ϶ɱʧƕџСȕЧʙŞʈ',
                },
                {
                    '^': 'float',
                    '$': 603505.7417640036,
                },
                {
                    '^': 'int',
                    '$': -1691201295067574620,
                },
                {
                    '^': 'string',
                    '$': 'яžԤӯҔӂєȭȶķˤƿЩÕ˦ʂ\u0381ƷҥͱÔÛγŊ&˥Ē©ßʲ',
                },
                {
                    '^': 'float',
                    '$': 350021.6182004407,
                },
                {
                    '^': 'float',
                    '$': 753605.6194089178,
                },
                {
                    '^': 'string',
                    '$': 'ƤˋαdΑƸÓњɶʉӠǨҫѭƢęβǠƞǜɖϒ·ʏɳΉɏΈış',
                },
                {
                    '^': 'float',
                    '$': 828594.0852307053,
                },
                {
                    '^': 'int',
                    '$': 815318936829000350,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ЀΓ',

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
            'identifier': 'ʌ.ӄ˥k\x91˷юƍλ˕ĢŴΖſϼπĚɕӹԜΝԘǵVɗΆƧѱ҉',
            'error': {
                'identifier': 'ʳƇʔ}ŕƁϚ҉Ǐͳƾˋɓ\x9aøˠԊǾСƞӔҀĺΔӨʲϣL"Ƶ',
                'source': '҉ϹƔУ·ȌӃ\xa0ЫЉѾӝΰƺӀѱԠϫΈˇª˗ΕɬɯēØόϊ\x9e',
                'message': 'Ƶôγÿ$ӏ&ōЏq:ĆϵҨʪÝϫԧҠӿӓҺơΰsʮŕӠɴ\u0378',
                'arguments': [
                    {
                            '^': 'float',
                            '$': -42719.04624060338,
                        },
                    {
                            '^': 'float',
                            '$': 448627.9046481664,
                        },
                    {
                            '^': 'int',
                            '$': -3086321226640028695,
                        },
                    {
                            '^': 'string',
                            '$': 'Æ҇łԉƸĆʲӯʓUŊϷ\x8bͶ/ȿҙґńЧЩТŮјϸ¢\x95:\x80Ē',
                        },
                    {
                            '^': 'float',
                            '$': 395725.63951120875,
                        },
                    {
                            '^': 'float',
                            '$': -76534.47370640376,
                        },
                    {
                            '^': 'string',
                            '$': 'ªʭōёě\x9eΌцɑːћϻōŽǻѩ§ǼʤƧͺăˮƌȮ˟ћɳ¯ǈ',
                        },
                    {
                            '^': 'int',
                            '$': -9211270944590373110,
                        },
                    {
                            '^': 'float',
                            '$': 562631.8322071049,
                        },
                    {
                            '^': 'int',
                            '$': -566333111616882226,
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'τŹx',

            'error': {
                'identifier': 'ТӉ',
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

        ),
    ),

]


LAUNCHER_LOAD_EXTENSION_REQUEST_EVENT_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'name': 'ЩѼѺԄæǼβǉʉΝɒȡʪĖӜȺѢѤȲʾΛĚ]Ҁϫ˫ɤЖѵЉ',
            'version': [
                5179586349201005636,
                -8758473181431731581,
                -5227488102318172781,
            ],
            'location': 'ʬхӍƮЕßѥҹ˨ɂи¯ғѠζ2Ҝь˜\x8cȖé{ύƢƏԐɮǫʙ',
            'configuration': 'ϕqғШKҋϸſǴ6ɑϷĈO¢ъϏòïǻɭɽʞѫɎǨψ\x96џģ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ȦСА',

            'version': [
                8146409151296411043,
                4304380305730382927,
                -5902990146525229488,
            ],

            'location': '',

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
            'name': 'ϚʫøӉѹPwʭӼ©ŰύЩԛƲ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'їԞÏ',

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
            'name': 'ȧϢ҄ĕŞȒ¦ƃɄħºɕ\x93ĨsѼͿΓŮʉğªƢĚȮӉǨžʤ˼',
            'error': {
                'identifier': 'ӆӳӂ7Ǘı¦ԑǮȄΘɂƫp\x84áпȔǔύƑjɆɈ\x8a\x8cΌÿ҂ѹ',
                'source': 'Ј¦яΙȩϿɘЅė\x959Ɗ΅ɞёӔġȵΪ˘¦ÀЅčѡϮʹНКƧ',
                'message': 'ƝӀԕ˙КłʬОÄүԘ˾ҧϏfȊɟϫĴΪĮӺɒѷóѿȗ҂Ҽ,',
                'arguments': [
                    {
                            '^': 'float',
                            '$': 992036.9721412156,
                        },
                    {
                            '^': 'string',
                            '$': 'ʓĄȓӇ¼ɩҌǪɟȱ(ȚϺԍȠĂҽчʑƒʤϷɐƵʦїёԤœҥ',
                        },
                    {
                            '^': 'int',
                            '$': -2105088968979606238,
                        },
                    {
                            '^': 'float',
                            '$': 481612.43707210186,
                        },
                    {
                            '^': 'int',
                            '$': -563354825706375641,
                        },
                    {
                            '^': 'string',
                            '$': 'ϯԪɆƏҋřǒċωɨĝʰϣԞÒԃуӹɏΦȪĚǙʊ\xa0иƼǝĆ|',
                        },
                    {
                            '^': 'float',
                            '$': 997537.280366359,
                        },
                    {
                            '^': 'string',
                            '$': 'ĠяѻȫȞԤёƀҏķǉƔʫѨϘӊøĝЭBȈÅµˀӝæҺˁк ',
                        },
                    {
                            '^': 'string',
                            '$': 'ѶХӥ˛Ȃɻ\u0381ɚӴȁɫӸӒ˂ǀʋԨцȖҦѼˮķҀҍɞȰ˗Ƙǘ',
                        },
                    {
                            '^': 'string',
                            '$': '\x8aùάpхЃЅȕԠԎΠƬÃƖҸ\x95ЃĤ˼ǡҷłǹ~ӓӒʠχǽǾ',
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ȊίĤ',

            'error': {
                'identifier': 'ă£',
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
            'event_id': 'ˑɻJȷľʥ±Ӳōºǉӏ\x84°:ΩƠȥȌГҿǦԏPģrͽΞʰɳ',
            'target_id': 'Σ҇ΉëƌȰ\x8fǜģϚ҇ĒԆɏǓ\x9e¬ƺɶVԢԤĥѻԚŋʫяӿơ',
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
            'extension_name': 'ǯʊьЭһϐʗ±ɯϹ҄φĩʯ]ÊºΖӹРˍȀӗϧȤǾѴOΧͰ',
            'events': [
                {
                    'event_id': 'ӯȟŪɳρЇʐƄ˛ȓƾăѹǬƅɼǲԚԨ6˔ңӿ\x97ȿƢψҫǒϦ',
                    'target_id': 'ƞÐ®ňäɸУǘȤĻ˾ǉϙЪԐɪśи\xa0z˥ʫÈϠűӃУLӪm',
                },
                {
                    'event_id': '˦ͿʄŪԤƪĞŊɖƷ\u0381ԩʕϖ¢ԢƯĄȋѲ˹řCżøҫҮӶÈN',
                    'target_id': '\x9cА(Қϕȷ˒ɟԋҳ;ĶήµӺʋĻŽǛέÚǜđ\u0382ʜьϠƉ˃ȡ',
                },
                {
                    'event_id': 'ѯÒ\x87ªįќԏҋ˃XA?Ƃίʹсțѭ͵ӂɒҶéŷԊMðʧȆǃ',
                    'target_id': 'ºʃȺ;ŨρƲˡʙȁбɧɮǆ\x98љһЯ*ɁĉʀɪѥʘWқ˞Ɍ\x85',
                },
                {
                    'event_id': 'úő˄ƚӆɷʨŽΝοЫhË:ɬη˛ΥйƧʉԓйύˎәÊƗ\u0381Ϧ',
                    'target_id': 'ʘZїģȶфÃȻů˘ˁο˪҃˓ŸϩaїŢŎ}ðґUЛƫçƍО',
                },
                {
                    'event_id': 'Ôԅцȇî¥ÞʚӈƣƑɚҟбF¿ÜͿɐŜĴςǩŠԊјíêǉǩ',
                    'target_id': 'ԘΦ˝Ж\x91вǅɗÍÖѠʂӫԓʨǄ\x90ϕϡSPƖϠBҶƏерǡʴ',
                },
                {
                    'event_id': 'ÿʁˋȶдġ˸½ˢǧ˖^ҫАʒ:Ӗ˜ǉӞÎǶĘУЛԏϸ\x9bѴϧ',
                    'target_id': 'Ζ`\x93ЛЉȉQӓǈĐ(DǃɜǰŔŲ˫®ĭKʫɱѱŵɔжΥϵ\x88',
                },
                {
                    'event_id': 'ɸ˕϶Рʟʫé:\u0382ѕ\x8a\x8dÐҊƔԪ˾ēΨäһăϐȐ¤ћMϝʥɭ',
                    'target_id': 'Ȳ͵ſγ´£ɁƸэɸƼȍîЇɷЫЩ~ϚȔhĞѥΒðΠġҏЪo',
                },
                {
                    'event_id': 'őЙбƪԭҿûɈϛΧ\u0383ɱĥʩϿǴҁȲƨ>Ńöў©\x88^ϋƆŃҟ',
                    'target_id': 'ʎƛĥɌįԀJ\x87¾Џ\x98ϹlƱǔʛϻŒúǎԕƱȖǏ¤ѷѰ\x8cӣј',
                },
                {
                    'event_id': 'ǂĢɂǢ',
                    'target_id': 'М˩\\ԊŊƊɝĦDŪˡȘʀʹљѥͲŊΪιä&Ƒǭуɰϸèцȸ',
                },
                {
                    'event_id': 'ԧ¨ªƕőҍƪҁԑ²ȡʗŪůϺǵ\\ēҌӧʴǔºʫӣʣжȍɜy',
                    'target_id': 'ҒȦɣŷͿɟίԭԠªѯˡǦҠǥˠáƎҷçÉνͱÒˤҏɚ]мӉ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'extension_name': 'ʛΡΎ',

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
            'extension_name': 'ʋԡňņÝчƊņϾμΚǛĤʭǰ«ХÚō˪ŻӉӓҿĞšΥ¿«ң',
            'events': [
                {
                    'event_id': ']Ԭ]ßŁ\x96ҲћŨӮҼуŞʬ˲άʣć¡ɗǎ»Τ˩ɭ#ʡϠ\x95Ƀ',
                    'target_id': 'ƯΫӉϓ˟Ĥɵ7ɦĔÍϥ.ΥӈӊF\u0383ĒʹņǽȠΉΣŕǚΘϭǤ',
                },
                {
                    'event_id': 'гһ°πϰӔϹĈԖ\u038dӢ)ʐ¿ƐǦρnŻŇÀȇôӻҝӜҨ¿ѿ\x98',
                    'target_id': '^ԓȖԤԤǂūƲʊÍȮŭɟŐɶɦƩƞҬыԕѳ˅ÃТ˛зԬcΘ',
                },
                {
                    'event_id': 'УˏʚȇϐѣĖ˗ʱϙOɗ!ӾϼҊŘ˙ˑxǻɛʹтʫԮʜƠƕʃ',
                    'target_id': 'ǜιĪ©җΫү6ΌGJΛ$ȐĄ\xadэӺ˝ɹ\x7f˲Ԟ@ϝФѯŧёЁ',
                },
                {
                    'event_id': 'ЀǰɺelɰÄÁŋьǀџdҝ£ƯӝӉӿƻwǽʩȓгĿӚÏƖҳ',
                    'target_id': 'җ"¿ϚF\x92ͱɌѶӍδѸɛχĤͻǏǲ\u03a2ƩϗԦƪ˪Ԙ\x8dȵѮɰȮ',
                },
                {
                    'event_id': 'ţ˺-:ƍ&ѩʙғЏőҼĈīj҅ǍϜòӁџыԠ<īǭԃŲGЇ',
                    'target_id': 'úм˃ŊůѹĮĲ·Ƭяņφϗņġüɒǎ©5ϰőɉѵӬӽķӕρ',
                },
                {
                    'event_id': '΄БðKȡʚˌЬǳѳůαęʦ҈«҄ȤЮӢŜсŀЋъϑSϢ¤\x9f',
                    'target_id': 'ǀԐԕƥϳ÷Ώ϶ɆѴiԉψҭӹǁĴǍӷŀłÓBˌŁ¾÷ƮО#',
                },
                {
                    'event_id': 'ɌѶwĭ(DÒӮΡˈг˚Іә˅ɍӥҊϋѬŐȱðΖӵϺ\x9bͷӈё',
                    'target_id': 'й˨ˇӗӵñäĺ˗Еjsиâǂμ$ӈțǤϣȽНοϒİ\x80Ðũŋ',
                },
                {
                    'event_id': 'ӸΡΘȲѽƳζǅʡϯѵԡ˙\x93˼˙¡ΉЋɚƁɊˁĤΌƾЊύōɺ',
                    'target_id': 'ɼč¦I˹ӜɢαêӭɌѤԍƏӫŀԏʈ\x8dÑȁķìҊԢůşȢ\x84\x7f',
                },
                {
                    'event_id': '˃¦\x8eɹνǕȗ҈ɄǶͳ˺и»Ǻ϶ʏȅԉϰ»~ǙĴȎŬϫ÷·ѕ',
                    'target_id': 'ʯ\u0380Â¸ЕȣϥĦωѢwҤʢǿȗҿ҈ĄνϴɈɌЪǀʵ΅ҵōΖа',
                },
                {
                    'event_id': 'ҸғòʂώmȕӅΩʠȉɵΒϯ˺Ӄԋˉ>ȑεÓɼΛԫɏáR\x80М',
                    'target_id': 'ğηѧÏхȲΑ˽ЎƘбVϱ˭ĥЭƾʈɵɮɧȡӐҰūȹεƑĝĻ',
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'extension_name': 'Ȋ£ӄ',

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
