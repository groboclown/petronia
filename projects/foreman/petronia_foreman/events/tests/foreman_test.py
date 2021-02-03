# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-03T18:04:38.788303

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
            'action': '¥ɌiƄҦƅƠξ҃ѲƦОδҐ@Ӌ˼ӱűʐԄvˤ~ȕÒŸƄԉê',
            'resources': [
                'ηкȴăğ϶ŊpſĎǣźþүϟɋшΐ9ŲʽËǠʥѪȓļʔƒī',
                'ɐ¥ϒЧњ\x8fÔ\x8fӖʑνѽӅǮъͽ"ɾȲɁĺȬͺӋȂČ[\x80Ǫȕ',
                'э',
                'ŀÏΏԤФςÁŷʵϖňȖȪϛMȘӛʟˏA˰Ȝ¿ƢeіĜӣ\x97Ӫ',
                'ЅȣӄʖÝͻ\u038bЪͲăԛӂąΒʶӳѠPβԡϥ[ь˩ßMȽ.Ũӭ',
                'ûͶȯρу\u0383К\x81РЃȾĨʌʤ\x98ʟ»ǃʦѯǽȷӽԥťԅ˧ń˕þ',
                'ΐƯʝʁɭƳЧϗîǰȷ\x8cĹ҃ſȟŋΗ´ӉȵϦӂÏ˜ĳ\x89lø˗',
                'ƙƔOӳȤʉõ?˶ӵԁŴǝʲ\u038bˍ҅ШŽѕϹțŠύ;ҕɁĬЈƍ',
                '˃ˢ˝ȻԤƽ×ƽQӖYΐ³˾ĉĝđѕƮĤӶGõĢ"ƵѺćΥʄ',
                'ʮȜÉŚŵ˝ǇËӆˆöͼзџěϘŰӥȳʚС˺˾ɐcʫVԒ\u0380ǈ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'L',

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
            'name': 'ҖÌâÑđǐ[˻˳ӊԀω\u0380șГŐұԗԓŤ£ŕ)ѣǝȽǦ˧¯˴',
            'version': [
                -832115308618802779,
                -8512060178508615256,
                -7582928111046475968,
            ],
            'location': [
                'ξЍůîΐŊϐ9ϹϪΡ\x93ȂЮԫʫIȿӋўϨɄʃНƿRɕɰӨϥ',
                'єтɦ>ФԬßӋж҂ζ˅еˏɀƛӣιʒҡȒԌ\x94űҧöΑǧʊ§',
                'ΰ\x80ýԃUȄπȁ˃ĈĨʽóƢ˖ȊзƧǠƍƼPҿэȲĥӤǕβҢ',
                'ƸDʠНϽԖ˙ӫɊˊǊСёƠLˍĎǃlȬċʔҤǿĵԓǅӜӨϒ',
                'fɆν·ќȯǥ;ԆÉѱȓ¿Ɲ϶ɾԮ,ψȜԓΈʩϓʢϰɍϥüҞ',
                '¾Þ\x8eˋнҟƐʢŦƕ¿Ǐƚ\x95Ϛǥɱ^ɩϫΚǼ<ϹʢʏǊdȻʅ',
                'ϼÇҐϝыJǗČʨҽѺƋΒǧƜӏϔ\u0378Ɩц˩ìϥεФ\x7fΞ{ñҬ',
                'ОӦ-+˦ѷΧž˜їˢŲɈǋԝʁ\x90Wþȓӵ˨ԇΐ\x89ŵҦˮδӝ',
                'ƻơúЗЛʨ*\x86ŌƂǮéĊˉϼԍϔ)ǺҐMПӒњм˾ȰԅћɈ',
                'ΠԅŅʕǌǪҞϕӔϝÀƠ˟π˜´ǆǟə\x9dʀӟŘíɺ\x85\x92ňİŬ',
            ],
            'runtime': 'ɸϱƖȣǹЈƴœϷΣFҪEǈςӉ1ЪǌҾʜȤѽųƺтA',
            'send_access': [
                'ɒӆĽӲåѠ˘.ȸ˗ȊƜρɂȪĚҸԥȷ˄Ǐυˈ¶ҋӛɃwӢҕ',
                '¹ȱѢȽɆСЗ·ĜĖԚŨɗЎѕϝ&ԦãĈʐŬŨєōũŅ΅ҊŪ',
                'šƶÞɋÂ¥ŞlƓ˙ԭŜ<\u0382ԩГɩʇćԖwѺНӅњöҜүɬǆ',
                'ʉǪдϪ҅ϭˑ\x83лӒƻϒȂą\x8bѴƊГώɀgĪºɨɱǟșͺ\x8e˚',
                'ӞͻǸБƘуñăɡ"ŹƭԜÀɈ[˞ѻϋίӯϸƖĉʵƍϑȒĳ˨',
                'BЫǼѻȋМ×ʤѧkϝȝɜҨϤҌMŅhƢĢĈ÷ù˖Ǉѕ\x8c˪ԓ',
                'ġƳʯĂϑϿÑϾʿ\x84Ɠ"ːӜņԄЌ§˨ĜӪȅǖԀǝŻŐǰĿĤ',
                'Ӫǖ\x99hɾӆƕʟÅғұԑċϺѕ˦ΟӺʉȠ<Ҿ_ʐıPhľzù',
                'ȼǬϓЋýǲ}ͽԌ҆ϳТЭҷɤӫʌŸ«ÅɁȡҗ¾ǡÃ\xadˣό¯',
                'ҙĿǕœӚȆMѐԝэĠ΅˅ұΙÝ_\x9eŻ˦ɜӌЧOȸƄ}Ϩɼԗ',
            ],
            'configuration': 'ҺŃѡšķЃЫγЖӮæӟŻ˔ƠƌȋԉǲȮʥƛȽҋȶſОӟВ\x84',
            'permissions': [
                {
                    'action': 'ɓӳƩџˆĳɨg6ƣĂŹħћλ°ŹӤɚɀǂͲ\x80ΞőЫˆŭǘș',
                    'resources': [
                            '=ċЫГàˀҴgȧсӌɻʟȖɀђͲԋȝЦƱÒ¾ӞѮΒɥΩç\x92',
                            '\x91ӭʗ҅.Ξ¦˦ȧϯ§\x7fþɊöŽǨƒҵϸϵҟŹƸèϊӨϭΩэ',
                            'ȡβǿʓѥϞOûǈâʜnԇϛͲOĖɟόҷҾόζԮƮĿɸ£řб',
                            'ŠͲťϏΆҖ˝ǱБÙ¹ιËԔʮ˓å¸șҶĊӦɺϟэϋӻ˼Ăѧ',
                            'ʱŝŞˇɥԂ\x98â\u03a2[ӒǦԩǘґ˝΄1ԓŦ¼țž˸ϖԃƃɲƦă',
                            'nƂϊԥɼӆSƂįџжўÃȯԃþʺ\x8bɹќӘϯЋ)ζ͵ɓέЛǶ',
                            '\u0383]ȩÙџǇԒhɚŃԭɃȹΣіʎ¯ŽҁͼЄο9ӳeɓɀţİȿ',
                            'ĹϘɀƎƄӇÑʰ\u0381ӢϏΏ˕ҋϒҳŪɺп0ΨɆȕΜԁʦϓŹǩЀ',
                            'Ȼ|˫ЅŬЌεԖțiʖġ`ȜΓҾъ϶УʪҼΫТϗ©ӜʰҊѻi',
                            'ыȽҗƔ\x92ќӤľ\x89ΈлǤѺҡ˹ϋϡ\u0383\x86љώһȵŶϖԘłˉʟț',
                        ],
                },
                {
                    'action': 'ċсӒɪƛʩèζѹģ&ȍ«Юʺνδ˅ϫΜuoƂkʾɔǋɧìИ',
                    'resources': [
                            'ӯɷ#ͶůˊȑԃͻơħϪԙ˾¥ԇƣ>ȢѴԄʊПĽʸΧԇĔ¥Ǝ',
                            'ĜɲƧωŌɿZǲнүʠѝ˘ѽǆ\x95ȇЪʠԈĈˈ\u0381ĎӏҦ×ˎ҅Ƨ',
                            'Ӽψˍ\x9fԜǡџԣPŕ`ƴʒËð\xa0ԏLïXԓå{6ƗԟԦѐ¬ȓ',
                            'ȻǧҜŷƁǫӢЪʯϺ\x81Џň҆ũһʽŲσҤƙӣûϭȜϥҢǘ\x95Ɨ',
                            '˗ŢɴøԑƘĬѯϾÓșƱѭʞԟҁǽ\\·ΝŁӨ^ԝώŌēʫѴĭ',
                            'ńêԩӹ˶Ɩȇȱ¶лŮ˸ˈΉÄԅJNŵȥѓƬћůæƧǱӂňҷ',
                            'ҐΐĪϷӬɕэǁȇӧńϘȇƜӕǊ˾ʂҊҜйѾӀԥǩɕȵѷюӘ',
                            "ӾĪʨФ'Ű͵ƨӎЁȐҗēϗɋѪʰ<ͿҟŲÓɼҥ\x82ҬΐǯȲħ",
                            '>ϭǛѱðщǱϿŒ|ĕΠŐЄŸǺmσғ˾\x94Š[qƚӶӹƪZǠ',
                            'ғҜӾ˔ɡ\u038d˄ϓțɡҘǖ\x88ǠƑäЈ ȵɦˮhрŸ\x94°ðТ\x94Ԃ',
                        ],
                },
                {
                    'action': 'ԙйȿ˪ԫȹŠÏº\x81ˉtʵ҇ɭˑ¶¢ϓȄπώϋԗϩÆ\x9fԏÙɫ',
                    'resources': [
                            'ЭÐƿӑԒƫҭƼzӜȴǉɯπʽѪΆŨӢŇ;дĭέŊ·ĳϛÉż',
                            'îńƤÙмԂЛмББФΏΝ)źΨȇüȘÐҀ:ţdέƎK\u0378ÀƩ',
                            '˘уʤŨÑчΏԌр1Ţɋơ[цӷŮξȫǝԫǕҗԧӑΏϺÃǎҢ',
                            'vȹñ˵ʾʱЛƟĽĵ\x8f¾ŀİɠB²Ǫ½νίԖ\x8eʅl˲ɖΎûæ',
                            'ɟѺΰ°ҤÒĿϗɆѱƚØЭƔӦšɎ&ǥѵϭāδԗ:ɫѭǫųҀ',
                            'óϗҠ?¶\x99ɘӽͰԒŗʋкџРjöѸȰ҅ҶɿëÚȹÀӺ˅˛Ò',
                            'ɢτÞғWǍƑʃłͽЃϖȱԔȂķĮĉŪԔÞћԑʱІҥŜıʓє',
                            'ĶƑ¶˦ȏѸÉȊʹƷǮѩіȣǑӧƟπӊǢǆɅψɇ·-Ūˣϙԟ',
                            'ΓӾӑLӪ&ѳɓͻєʍƂȪ/ϚѿХŠ\x82ɠúŐá˲ŎBĎ¸ϸż',
                            '˴ӠõǐĨ\x8cƛɺ»ƍ¶{ɗϥɜ"юǬɸȥ·ΦʫʤȦ\x94ΖϘΏ',
                        ],
                },
                {
                    'action': 'ϬēɧӜ˰¦Ļµ"ΠҕϝɛĶђ¢ɤĲԠӺϳŭ?ƌ;\\ҮҶOӸ',
                    'resources': [
                            'ӘŉťǗƊħς¨³˦ŭŁиϨP\x99ƕɳʖ˔ӱȌӇώƶєӴīėћ',
                            'ԜƍѪ%ƦȱǻΆԍɦҴϟΉЫ\u0378\x92ЀXƍÎ\x90ſƙÖԈ˫oÿЉŉ',
                            '˰ȂЅǃҝ(ʾ:ǄǞ¿ЎǤΪȧ\x90˙ĞеȚŖӺ˔ʳśɵкκʣƼ',
                            'ӟŗɤɭ˞ŵŇȫϱϱϯҌ˥łˇqә\x84ȲʟѧʼïАɛʖԤƫˠЈ',
                            'ӊ ũɉΆЎЖ÷ϋÀѕҶ\x9fϴӏn\x80үEɖQɶYƚʛ҄ҧïӌͻ',
                            'Ʊʼԁʯȹ\x81ӯʎƁʚŏѰԌʍѦ˞\u0379Ånӻƺź˙Ӽҹ˕Ԣǁ˸ȣ',
                            'ЎȭɆǭǽӷŢ˘0ǫԠãθңӘӃÞЪǍϚ˵ǕʭѼġҢӋџϩǿ',
                            "Ȕȏмǜɪ˓'ҊǌҒȒΰÏįǳ˥Ӡϳԋ˥ϾƴвǺӭԕο\x94/ѹ",
                            'ˣҀȿӪƬƓñʣǯϖ©\x8aʎӢđԦϝϢЎƧ˄ěˆʝϪâįϖԥ˱',
                            'műȆȗаÒʟƷ˕ȯԎΉѓϛſɱǴɵɲÀƩҺͷšʹ&ǠĢ¥ƚ',
                        ],
                },
                {
                    'action': 'һĕŇыìÛP˴VȎĊ',
                    'resources': [
                            'ɥӦΉTǔƨÌРтϕȭӑ\x91ԑFљŽώơΏԛÅĢ҆ŪEϟҤӸʉ',
                            'ĭǻӵΩѪϾňӍԅҏȓƥ˴Ƚ¶/ђɐșϝŪéˆӻґЯρ҅·І',
                            'ёΨŦòѨˬ˘ÙћɑȒƱѸ\x92ÝĐǽ\x91ЊȽʧ?ľӃ\x81˔1ʩѤϼ',
                            'ƹϭԙͼҽɽƲȆȔŝʼ«Iǡʇȡ\x9a˜ĐӏιǡΒФʅÿўёԢԇ',
                            'љÒĚě(w*\u0380ǪΞǕŞҹѦæɼP5ѫϰĄҞǹŅ¤ĴWԮҒ°',
                            'ƣҎ\u038dΐƿš˯ÝӐȦɲƗŎXӖΣ\x98ȽĤЈ¼ϻϑϤȦΣúр#Ѕ',
                            'ΖϊЮĥɧɭӇßӛǸŏčϕͰ4ɯ˯Í˕ɥɲèϿǘ¾σĒϤԋ˗',
                            'ȍƿțDŏԁϳ\x9dŤƟ_ĜũҀхΒ\x85ѴőήRÈ¤ΦяА;Ќȶǆ',
                            'ȐӦnόÇȐӉ1ĬǣȬϼœɊơ\x89βʚӔãӖҦ\x8bϦɉюìԘc\x9b',
                            'àΥΆхÜů\u038bɦȢ¢ΗѽɿϜ\x9cƈϙѯªþïɣ҂ӁԘѓʩ®ҧɡ',
                        ],
                },
                {
                    'action': 'ӴщÏʮ',
                    'resources': [
                            'ȚӹԈŪ8ȴЪɐļЯǦϤJΈ\x92MԆȰϻȻ˫фÒӲԝмȠřƣˎ',
                            'ƨűАѻϱćԈiҫǺɵЈ˕Ìԅ˹âˎØƬʹϲxҭƨȔʖȏ;ˍ',
                            '˗ǓǅŚɀǨΕķ˾ȣĮWѰ6҆ŨӲмɜ\u0379Þ',
                            '˺κƄЦɜ˾ǾŢєхрŊŦρ˪ǽѿơčɳΊлӉĀ½ȵʇϰǶƲ',
                            'җͼɴċɏ`ƿ\x9aɟԢ\x94ЋƸҡέŇ:ƿϥҊʌ\u038bӴΘǬӇϫďέ˴',
                            'кƉLȊӟ·ǐ҄ǲϩ˥ÊԦˆЋӱϢϫƴǱŞȱɇ7ђKҋ\x9dЅĬ',
                            'ƵưțΨ%ϤύOGÉԠΌκ\x83Ѓˡ9ɈґäFĹԆcҠǕǧŌĸЏ',
                            '¾˲ŅӏҍӽҶƛɉԈͽʡҠŏǒΚŵǉŴɋʫ˝\x85Ź˼ȓбҊ Р',
                            'Ś"ѥƧԩӒϡҥʹβͻҎ\xad\x84ϤʐĐ?ҎаwϾҒʣЂԈΠíԪӘ',
                            'ƒΧйeϧâΩҊȄȷѲаЙυ4ǉǹ˷Πɴ˘ŕpҗǖҿaƑQó',
                        ],
                },
                {
                    'action': 'ɘȪϿԝƕĊĨŠʿƉѻПłœÔӀӪʲӑҚοǲҝƂϮG΄ΩʙԌ',
                    'resources': [
                            'ҤԣȜјΩȜĤгϋМ«íʹõɹθâфȡԄ¥PӕЬ\x97`ҊØȞʹ',
                            'ǏŴџ˾єʒʩ҃˜*ɖˍТԉЅԦѹή·хȗ½ӵH',
                            '-қόˢӜӒϣДοʢ9Ͱʷ\x91]ť\x93ǙԄūëĒΟūȤŽ˲ˇԦȋ',
                            'ɉͷăɴÄfΪ˄ɱοԞÅˊԇǀȄȲԜĞñķºâɣѕQúϼӿе',
                            'ɳГÏГ¬Ͱί.ĂüɨŮҎÎԥ²ƻ¾ҋӊϜԤԎ\x84ȣԂҦ҅ηċ',
                            'ǵžӕӄ˝}ʯ¯Ŧ¸йʯȽĚͱĽӀʕĈҩ˾ƙß*ɌѾӚѠҽԞ',
                            '_ÔΆãπʧΓјӛ˥¥ɗŇ\x85ȜǾ:еέԕѐʄBɤΰøөÃ×ʭ',
                            'όƙ\\Ē\x94·$ʎ\x89ɆƂˮӂˢÑHΆɐςȠѰ\u0383ɩĕЯˈˠʲŒȍ',
                            '¢ȟԚу\x81\x89\xa0Ԝ˅ʟТСҿϞǍɪԭӦӂŷbȗŝć\x9bĲśǺÖø',
                            'ћ ɬʟήԎ÷ǣTƙȾЬˀʋћϱ˂ĚøԌʁǑҮԞɹ¯tҖâϢ',
                        ],
                },
                {
                    'action': 'ůĵ҂ĩȡ\u0378ȅ«ǳʐİԂŨҌÈɃ\x93ѭˢȏΞϘͽěǺӒҜ\x82Ӛɣ',
                    'resources': [
                            'íƿԡȅ÷ɇӇοvҫ.ј¸ЭCŉ Ύőө!Ǘ"mƏÃɘýΉȬ',
                            'ǓǾӹȇːϘηȖaťМӎcȋϩͿãʈ˄ǁϑ\x9bǘǴσϨĚǅŵq',
                            'Ģ˽Î\x88ЗƱЮGjĮԇ˽Ǡ˷ѾgRnʛ°ԈҫǭˮɻƽȖɻɁВ',
                            'μĦƊʉϕïƻ4ǮɗǛʏÙ\x83ʳʋ˰ȶ˟tȑЖɣ˳ҝѵĜðǻĳ',
                            'ǥƂǢȋΒȅԐʹýŨӸɕ\\ӠĔȞчņØ\x9aƱҤшЋ΄ϪʬʷЙј',
                            'ʣҕϾ˱йĠʎӁȐșÆԑťȗ˯\u0382ƞ\x91ҋΠʢӛȷƘȱуԢƸwʸ',
                            '\x92ǥBĉӮýƝȼӣĖėeķ',
                            'ʒʙŠʵòƎˊŘɶöӰҧȍ¤êωѴµΗȜΝˣЉȞԃȁɸŚОԖ',
                            'Ȇ\x84ԂΘιʭӎс˝φӄœ˭ɟʶóȧ[ҞкƢȶǗΩɓƸуƓ˥ƒ',
                            'ΘǑђƧäɾ\x7fѡ¥ŮïΛȖ˔ÖϳˮëжϷӘӯǦӶƗ¢ɯӗˋģ',
                        ],
                },
                {
                    'action': 'řŪԈĎȉȱnϼŎʔ\u038dpUćŚ}ÕǐŀрŲǅКõ\x90˼ó\xa0ĖĿ',
                    'resources': [
                            '3ǹĈӾȥ˳ЧѲʛѰ|ǼӴӋȾΣǆ˟ƘŸ\x8eɤρ\x7fӮͿϊ¡ùó',
                            'Ӫʻίэǩɣ¦-˰ԜʍǳŅҊΤȌđΚϏқɋƘüȔĹ^ʴԎѕϠ',
                            'ʞ®ИȄ3ӂîǯҏлЦÙңǯŪŮӊӭÛҙҍУǤøӏԐѣɂĜȞ',
                            'ќwūUԞŬȆɮɊsΏYιѪ\x8fÕʫȋқʙ BƮŬ¯ӫӁ_Ɔɠ',
                            'ƫԑʿ¿+e\x9f\x95ЋЧ²WɹШȡ¼ōǃʑ\x9bѦɆϘӛƑшƵʒČ\xa0',
                            'ЌƬĤԌш˂Ўԁ\x87ƙ˽Ԙʯċôȃ`ӊƺо˨ЭŜȗԦɡ\x85ÏψɊ',
                            'ū¦АȷҘ\u0382ϩ¯ѴUиȧɠƓǂέǢαȗ҂ʔŦŋɗӷǉİхï˔',
                            '¥ҥg\x9cҠƄ·ȑӋ·\u0379ƒƳ\x83ςǊǱFĖÕɋʌɷҥτ¹ԩΏʼϭ',
                            'ʌɔ\x9fшèĤáТɥϪқț˫a¢ιё;˯Ԫ\x9aõҾɛϛ˰ΞǫɈË',
                            '\x80τҒɡԎԖϊɎЗɦϧȎǷÞӒ˕»Ŀʚ$ѻϹȌÔq8ǽΉʉͼ',
                        ],
                },
                {
                    'action': "ƄЎ'\x7fɤΚĚң˒ϾˇҒ&\u0383:.Ɔæ\x91Ҡҋ#",
                    'resources': [
                            "ʾˑ4ǀԮΊ˜˱йŝ\x9bӃѵϼĶ˶гӱΝȶǱѸ'ͶáʕɢѷӀе",
                            'ќÅŶHωʼɫͲ˷ҦÅÔϒѫЕҢðѦӑƸԧʗγζӻҚӆçšϦ',
                            'юОʫǉȪȧʞϰї\u0381ΫǐʝϋǚСӅǙʉ͵¾ÅȟήӖǺć҆ĩѥ',
                            'ûƥЭțɿ˕ґҀϔNǴʨǳӃϪȀ˅ÊѨ3ȡƪӯİӥȋĿҠ-ȏ',
                            'ґçΌӔɵɁƶˤζ¥ØɝеһƵŚƛѾȂĿӘÛ8ŅȺæëȏҕǣ',
                            'ȑǣ\xadрǝʅɨǮÑǱҼѳėʪёǦІaΨˌЛXЊχR˵ӲԤέΌ',
                            'ƔǽӽʠŹϔӢЧ·;ԫɄТÛ9ɳ!ґǎȣӑĖȌ˖ÊɍљЊǾΖ',
                            'ϝӺγөщƑχɮЙɏǔϷӔȄ²ǤˮʋǴ8rŜѱ\x83²§ђӺԢȀ',
                            'ƞţȾξȽȲźȻƕˎ˚ӷТΝƸҨǵɮȘƒӊXȆϬĂԤ˝ґΟy',
                            'ϘʐбƳԛԛȂĲňЍIĬϓѤͼѻΛ¥łǎĦB\x8c',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ѧDb',

            'version': [
                -601186631705615343,
                -6048996432051522702,
                -7301996529437457776,
            ],

            'location': [
                'Н',
            ],

            'runtime': '²',

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
            'name': 'ń¸¢ÙˇɨγŌėˬÜİǍɹѤͼϪʺδӜхȊ2ѥƚӻТѥɭˑ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ԝЉԍ',

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
            '$': 'ҼЮёŮÅӜϞЪћĽƋxɐʽкҭɬѴŮҎŏϗ¹Ԝв-Ԟ˛ӹɻ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 498631215243742274,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 324504.9880096169,
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
            '$': '20210203:180438.728334:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                '»ъûӈԦËїÂŬſ\u03a2Шrȟ75ĘӬ}ԕ|PƂπԛĒ˹ЭɽĴ',
                'ѨƈΘӹѴԤ¢ɬtǲ\x97ȷ-Ⱥˎș!Ƥȫ3?ЄˀǚȲ˺ӁӯΈĐ',
                ' \x82ǐǪѷGȄҐѧˁЏϿѣъIԮȏˊƶϮЩ˦ХрÓ%Ƣ9ϗ˝',
                'ϚǷ¬ΈвЖόɀ\\ő˷ШĘ\xa0uśɱʶíŮūңԎÓ\x83äĄɒŎѱ',
                'Ĩх«¸\x93Ȁ˒˺ӴϰȘҬœϵ\x87ˠԎӓlı©ӎЍ3ϐԗòЅӔđ',
                'ЖӸɶԅϳ\xad˴ÀɠйĚϬϕѺŗˈҾѫOшϘʽ0ҋǨçӧs\x82Í',
                'ĒѧoΒɠġÈʫмļÙʈä҆ɚԫγōʹǈJӒÑČӽ͵Ĭƃϼξ',
                'мđĴėмÖҥƴĢі˙ҺоНȟжƖȕϋԞԢéÊʖŋæ˚ɹўӍ',
                'ǺǸχϖĻΛΜƷ˻ƧˀԜPҴ˙жҙ˷ŦƼȅƵԪѨȾȦӡ\x84ɀӴ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                6674787736936949952,
                6935356862312902026,
                -8278402601933436695,
                6529984107905639769,
                4386436594129694006,
                -3804353055076684163,
                8860330295171550403,
                6550411069965640286,
                7425588278910373097,
                -7600110925233111266,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                876457.3320819158,
                676290.6885854624,
                128009.10865023432,
                573799.4825555288,
                106817.5712421333,
                614409.1208161394,
                552437.8454425044,
                523422.6811107715,
                -5648.360573845348,
                20702.219942894182,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                False,
                True,
                True,
                False,
                False,
                False,
                True,
                False,
                True,
                True,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210203:180438.729322:+0000',
                '20210203:180438.729351:+0000',
                '20210203:180438.729357:+0000',
                '20210203:180438.729363:+0000',
                '20210203:180438.729368:+0000',
                '20210203:180438.729386:+0000',
                '20210203:180438.729391:+0000',
                '20210203:180438.729396:+0000',
                '20210203:180438.729401:+0000',
                '20210203:180438.729406:+0000',
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
            'name': 'ǩԖΓĮlέµͷý²Ŷ~ͺԤɈūņ҃҉b˾\x97Ŵȡ˾ȹҿчȒƄ',
            'value': {
                '^': 'int_list',
                '$': [
                    -2025720458837346286,
                    -463981646262503317,
                    -5776183234153095939,
                    -5332702069051307713,
                    6848803437934389843,
                    276543682839435748,
                    -1289266073855526950,
                    -5727232703294490388,
                    9166736536957879159,
                    -4575307157681414310,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Μ',

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
            'catalog': 'ԐǛNØпΒÛŠʷԕˑɮӔ˛ҸʿԠÜɳЖF³Β˽ɛԤЄFÅ«',
            'message': '˞\\ˠӾϒ\x88ҚΔOȠԁȬ ҵѷćȬũͷɅXԡΏmӘŃˮѷƢȳ',
            'arguments': [
                {
                    'name': 'ďĩЊŲƎʴʥɏӸϻή_¸ʋӢÜˉƿ/ɚǴƲç8Ėȝ9ϡǵh',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        False,
                                        True,
                                        True,
                                        True,
                                        False,
                                        True,
                                        False,
                                        True,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ҥϓ˻Lɞ',
                    'value': {
                            '^': 'string',
                            '$': 'ԘÞҖ΅κЅԎ҆Ѽ\x9dаɕǢʸϐ£pЬƸΧʃԪνŪÙҽ?àДƐ',
                        },
                },
                {
                    'name': 'ϊɲЕϰʀ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        True,
                                        True,
                                        False,
                                        False,
                                        True,
                                        True,
                                        True,
                                        False,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'ӟǴ\x96ΒҁѓƯgζԍ7˖|´čҚ',
                    'value': {
                            '^': 'float',
                            '$': 626569.3535186934,
                        },
                },
                {
                    'name': 'ȳ\x9cČΦ˙βЧӂƾХȘϰŠΌьǙψF7§ñ\x95ÓCː˝',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        6731642191539337374,
                                        -4200576381461849465,
                                        -7097651712581970859,
                                        5605593443710705327,
                                        127454617843993755,
                                        -6320182307049539143,
                                        6406401334786200746,
                                        -8102060166063836440,
                                        -3588963216724038332,
                                        3575340260842007059,
                                    ],
                        },
                },
                {
                    'name': '|ȒԂg',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'Ʈ\x93ȒБƤ,\u0383ӭłɩĔźҁě4h҉ӯϗԀƖ˜əчԫÚʬκŬʬ',
                                        'ŐýʇĶšϷţĚųħЈӿZʆҥɚӉԓ"ĺǨ\x91˞ƯǑӈƁ6Ɋɬ',
                                        'ΖϺǴѸ\\˃\u038d«ɹνєRљǂоαǗӛӼïаŧ{Ĩ΅˜¾ĒCɉ',
                                        'ġԝˬѩͻɭЃGЊŹİіΰȼn҈҇ў:¶ϨΖöƗƥӮ\x8cĴʑӄ',
                                        'ҦηШZν(éЬԈЫĠƷхҰМʫ˝¢ɧψˎˢDқơǗԖđˣļ',
                                        'Ёϸ0ǩûҠˣ¬ÁĖP¥ȦБυĸǇҷЈѧνəóЋƦŻ¾äƟі',
                                        '\x9eώӖ\x86ȳфèӵМЙ\u0380ммә³ǵƣЬϮϥ˯Ӽƀ÷é;¯ŰӴû',
                                        'ҢԆӄŮλΌȼ\x85ưɮ÷\x8fӡˮп¨ԋьÔЍȁŗтͺͽԟǯΌϐϐ',
                                        'Ԡʆъә{ԑˬΔǔ:ÆѶě\x85áӏϼȚѹѐ}ӱŅөŝėǒµϛƬ',
                                        'ԬǴҬQł˅Ҍ˶\x9cŌÑɾɼѶʍ\u0383ΏҳҁȷϞϙǙǳRӳƧһʠӖ',
                                    ],
                        },
                },
                {
                    'name': "Ϙňӵ\x97ʝҔƞϦӶĔʟȘ'ӻŷҦǆĈҁĔŽʁåŤ4ǎńԔǊέ",
                    'value': {
                            '^': 'float',
                            '$': 648000.7680070976,
                        },
                },
                {
                    'name': 'ɼļÇľў-oȢѕȊƚӔнʚųųǚƍϴɎҕ~Ӧ˧ӚҌĀ@Ǌǅ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        2507233660444947074,
                                        -2292078050474111821,
                                        8097136784379359029,
                                        -2422736652903217508,
                                        3956054805136006641,
                                        1561349139949054258,
                                        -3656574080452457345,
                                        -7457834339973927044,
                                        -7419137799473184762,
                                        2184788629859941100,
                                    ],
                        },
                },
                {
                    'name': 'ŁȴʈʚŪŚðƌŻφѡΈɆҼʗɜӉԐɩïоцӼĥ΅Ѻǣ»Cҥ',
                    'value': {
                            '^': 'string',
                            '$': 'ǬɤæϑџҭZƘԮůҋĝǅȄԜţǜЖχ\x9aȖş˯Ѷ~ġӄˤԂ ',
                        },
                },
                {
                    'name': '°ʝӡǭˢҫǭǧь',
                    'value': {
                            '^': 'float',
                            '$': 121588.83896657277,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ЕԨ',

            'message': 'А',

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
            'identifier': 'ʻζό°ѭ\x94ôɈ×ȝԤɇиуː!ĕάΏªrǔíіӀɹʑİM˸',
            'categories': [
                'network',
                'network',
                'network',
                'internal',
                'file',
                'file',
                'internal',
                'invalid-user-action',
                'access-restriction',
                'access-restriction',
            ],
            'source': 'ǱӂϬ\x96ι\u0383φˣąɺčǷĆümӻοƳqѴWĳʺιDʜϸ҆\x9eŤ',
            'corrective_action': {
                'catalog': 'ӳɷƐͽøƃļҹйǸӗɨЭ_ʱİΆ\x88ɥʗΎǑӨª&ɔǜ(ӌ\x98',
                'message': 'ǯϞƂ8љȠ·ƃƺ\u0380ҾӤ˅\u0378ŐòзͷƤϴΔʬѣЩ_βƿɖÝШ',
                'arguments': [
                    {
                            'name': 'ɝ¾ȝ\u038b\x83ǦҪƱЀԓҵȼӲʟәXˋčӑȬʴӈ˦Ͽžǫ\x9dӻЈ',
                            'value': {
                                        '^': 'float',
                                        '$': 529610.6959673855,
                                    },
                        },
                    {
                            'name': 'ӪϦCVäȭǚ\x9aғǧƣȥͼОϲ˅ʶWÖЗɰĀŀο\x9bǶİ вɧ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        279688.31810941856,
                                                        897232.14204067,
                                                        850750.6570747321,
                                                        864645.2670288748,
                                                        589649.2121945674,
                                                        126141.1146796383,
                                                        793764.2179136494,
                                                        451206.20021796157,
                                                        561228.9177317175,
                                                        427930.3600936526,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ƫͱŬȨԢѱԝǿɁǅхԦɓȹČЃͳϊ¡ǒҬBӜЎȜӽƉ˱åϰ',
                            'value': {
                                        '^': 'float',
                                        '$': 521345.59086194495,
                                    },
                        },
                    {
                            'name': '8˟ˡͰǄ2ԀІϜɈ\x81ǘԘψԔɨ',
                            'value': {
                                        '^': 'int',
                                        '$': -9053688312907030956,
                                    },
                        },
                    {
                            'name': 'i\x84λǉúȫϵLɻ˾|Ê)Z´ɦƶʹ\u0382',
                            'value': {
                                        '^': 'float',
                                        '$': 637382.7968990487,
                                    },
                        },
                    {
                            'name': 'əȞʌгɆĞЍȣʉĄjȳ¼˃ίλ`}ƇϤеŚһYŹƙk=ԟɥ',
                            'value': {
                                        '^': 'int',
                                        '$': 4668923067101652090,
                                    },
                        },
                    {
                            'name': 'ʥӽɣ§ʦƽӀҡӾЫ˞ʸŘƇ˓ӣϥҺЪԥƶԘģˣɱ˕ǵ\u0380ɢɩ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210203:180438.723692:+0000',
                                    },
                        },
                    {
                            'name': '3ɈҠ\x7fƸĽу϶гѲƟDʍҭͻԊƆ',
                            'value': {
                                        '^': 'string',
                                        '$': 'Zˤҹ\x83˂ӮʫȴƹƱąӔȜӐӒȹǤ#ÆƾԞŋƐǆɟ҄ΧȷƿȜ',
                                    },
                        },
                    {
                            'name': '¾@ҋeģȞɎśʫϮÜжͽϛĈҙдʼʧǻȼуӚҼĿťʌKλ˳',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        294126.8569131645,
                                                        622735.9441541024,
                                                        683745.15779059,
                                                        758291.6591745337,
                                                        -34914.63751805799,
                                                        -24854.97173451353,
                                                        994844.447771519,
                                                        654624.2199900605,
                                                        143705.14327940726,
                                                        511452.38943291723,
                                                    ],
                                    },
                        },
                    {
                            'name': ';Ƞ>šςӜŽÌJрƩʞҁʠūРҿԌƜěύ϶ÔþιʫϕѝðБ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ыӾŐűλʹѾҜԤӠЩGƲҍºöԢʈʓ£Ć\x91ŘΨƋϯȕΛԍō',
                'message': 'ƪîŷβκǚ®ìǴŋĳíÂĦƚǒХΣ%͵ҌԖʕцÇÈįЦЄ˃',
                'arguments': [
                    {
                            'name': 'ҒɐʎьʑȝɧĞǔɍц',
                            'value': {
                                        '^': 'float',
                                        '$': 6546.280558144528,
                                    },
                        },
                    {
                            'name': 'ƩòčˮОБÒάЮŁϙǷΗʼǍXǗѭ˫ȷΕvεӶŉĭɿɋtә',
                            'value': {
                                        '^': 'string',
                                        '$': 'õAӾлǧʞȂԔѸ˧ƩкοɺΥʛБ;yk\x9aÅЊïԭvŽѝќ˖',
                                    },
                        },
                    {
                            'name': 'ΦѮšŷ\xa0ǐɀƟĒưӳӥ¢',
                            'value': {
                                        '^': 'datetime_list',
                                        '$': [
                                                        '20210203:180438.730023:+0000',
                                                        '20210203:180438.730052:+0000',
                                                        '20210203:180438.730058:+0000',
                                                        '20210203:180438.730063:+0000',
                                                        '20210203:180438.730068:+0000',
                                                        '20210203:180438.730087:+0000',
                                                        '20210203:180438.730092:+0000',
                                                        '20210203:180438.730096:+0000',
                                                        '20210203:180438.730101:+0000',
                                                        '20210203:180438.730106:+0000',
                                                    ],
                                    },
                        },
                    {
                            'name': 'ęѓϞʜԦưɘɬıČŀҘԫMԁÌ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -480212835529547353,
                                                        2718440462502578409,
                                                        -1717100172022311093,
                                                        -2230343860849127026,
                                                        1549429314312080705,
                                                        571637705204361076,
                                                        -8747796189538006626,
                                                        -4956215523095147121,
                                                        -7230492955820655849,
                                                        -4927723616148645270,
                                                    ],
                                    },
                        },
                    {
                            'name': 'řʕЫΉ˙Ҹʛ˭CHɥȬҜĲ;ȲȎҰƂӳӵώȧÈ-ƉҬҜӖƚ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        7945795540982097523,
                                                        -3834150510310287749,
                                                        7099907744863796950,
                                                        5187240710170494480,
                                                        368469940905170926,
                                                        4044452915534047870,
                                                        549734972542007525,
                                                        5233895371847173559,
                                                        -5590051410448505942,
                                                        5395698511119098550,
                                                    ],
                                    },
                        },
                    {
                            'name': 'xĬȴʏņҰơĒʄP\x94±Ŵг',
                            'value': {
                                        '^': 'float',
                                        '$': 336074.0595701257,
                                    },
                        },
                    {
                            'name': 'ʬ¹?ț¿\x84\x81ɻÞԑ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ƊͲүΑӰʤˁāʍГŒȎƃϔԖŁƾϏǘ«ΚȀѹȻŊǍoӽɠД',
                                    },
                        },
                    {
                            'name': 'ѶɸʃƮŐˊř\xadΑǜÃƊϽƪ˲ƆʻӵǗñҡ/ĹЂ®҇ǀʌϜý',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210203:180438.731325:+0000',
                                    },
                        },
                    {
                            'name': 'ˎÌΏɇ œ\x8bdӲҦˀğ¾¼£Π;ǒXέĭҐP·Ф',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ɢӧĬżHэԆ\u03a2ĥ҉ΩӸͱɦӚgŎң',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210203:180438.731657:+0000',
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ű\u0381>×Ҋ',

            'categories': [
                'os',
            ],

            'error_message': {
                'catalog': '³˹',
                'message': '2',
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
            'name': 'Ȁšɾҏ\x99{ǟˈ\x8cʌċΙƝŊԎtцǄȵĈҚǧѢØԗʬ·ōųƉ',
            'error': {
                'identifier': 'ɁѼȁąsņˑjŲ\u0383ԓĚ˕˙Ė˙ŷӂː6ȘťҟǮΡμȢǔƼÔ',
                'categories': [
                    'file',
                    'access-restriction',
                    'network',
                    'internal',
                    'configuration',
                    'internal',
                    'access-restriction',
                    'internal',
                    'access-restriction',
                    'network',
                ],
                'source': 'ńə#ԦЎõǫӱҸǩԭ˛ɡ<ʆЙȇǊЕЂӖЏϾΖζ;ʔЮԒϚ',
                'corrective_action': {
                    'catalog': 'ãƄѻƧĽӽͶ˭ǴԠǧʿƹ˓ʛ\x91ЮRɊұˬћǱɎҮΛŔʒȞӍ',
                    'message': 'ǶɁǳ\x8f˔ȳƱǑ¯ϐϐǜƦuɩǍyĘˤӍ\x89ʶӋΊ;ɛӌ˲ɤϹ',
                    'arguments': [
                            {
                                        'name': '³Ƈƕэƛú!ɁїʭЌҗөʷȅɟ-ũρЋύΉàśˊæһ½ƲЃ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2777243971404270873,
                                                    },
                                    },
                            {
                                        'name': '˓ҠſŔҺv¤ͼǍƁїʿˀϬ\xa0Ǝ8Π¶ѾͷȇʞĔ˂ʽĢ˹˾Ӻ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7592892022381950151,
                                                                            -2140343558786054524,
                                                                            -169918294677341979,
                                                                            570365613345372564,
                                                                            8124591787943358323,
                                                                            -3325774725528946483,
                                                                            -4698611417382796810,
                                                                            3571767617003717515,
                                                                            -1424341054768083521,
                                                                            -994551861588901485,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŸӂʉͳзǙ\x9eӌČŊТȈʒ\u038dСħωï\u0382Ѝɰъ˩ˏƞєԐİȞк',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            933291.0330225511,
                                                                            288283.50583987497,
                                                                            -7301.314239669766,
                                                                            256082.82496996183,
                                                                            891306.074671567,
                                                                            162216.76127422077,
                                                                            883086.4959671947,
                                                                            820333.0975592383,
                                                                            927317.6270439359,
                                                                            560330.3224992789,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҷx',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -74390.8288065158,
                                                    },
                                    },
                            {
                                        'name': 'Ȕʽθ˵ʋϿȕƟƥˉҪĤàƱΦӦǹ\x82ÔЧ˩ʸŢ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ȳnѻˆи:ĘºɳԚϽıǝǮɈˎʧƚʄίӺ˖1\x9fҝЖÞҨDƚ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˖Ї\xadŰâȏПíĖʤ\x8dϷūɨӀѫӓ˖Ĳ×ҞǛųԜǄȊ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -56514.94356547515,
                                                    },
                                    },
                            {
                                        'name': 'ǗŇ\x81ǟvˉ5\x9b«ǴáѧúÈãʉȞŝʓ¡йɹˍǄɣZʱ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210203:180438.713904:+0000',
                                                    },
                                    },
                            {
                                        'name': '£˰͵ѬɉȉƈϫǒģȤԞɴʢӨʜǄɇʤˡЪ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ÃĂɸē',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            399568.28283421625,
                                                                            988905.8520298686,
                                                                            242142.58756694262,
                                                                            775369.6441765083,
                                                                            511438.5738265072,
                                                                            108649.74992873333,
                                                                            259012.12191024178,
                                                                            315181.187645743,
                                                                            747220.1933568574,
                                                                            776473.6039721136,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ķʇςдζďΗҁǹáӚԥԢʿqƲϨԨĞ¯Ӥ¡şΫÆìίÛʷț',
                    'message': '\x9a\x99˩ǳ®Ԗ˅ϫƠҜłTıcΘԃ\x99бʭήцǹӻŹɾ˔ɢљʇā',
                    'arguments': [
                            {
                                        'name': 'ȐɹˉІƧĆʽΖĖ£бǔȟŇŮƊӇÆÕΐԬT·ŌƍLχćʦ\x93',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'әǹɌɏүʱyӦʋſ÷ʺӥϨ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 135914.55090235005,
                                                    },
                                    },
                            {
                                        'name': '¥КӕѤџҩзΎĐԆйľΧǆѫѷϷмɱų',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210203:180438.717069:+0000',
                                                                            '20210203:180438.717108:+0000',
                                                                            '20210203:180438.717125:+0000',
                                                                            '20210203:180438.717140:+0000',
                                                                            '20210203:180438.717155:+0000',
                                                                            '20210203:180438.717169:+0000',
                                                                            '20210203:180438.717184:+0000',
                                                                            '20210203:180438.717199:+0000',
                                                                            '20210203:180438.717213:+0000',
                                                                            '20210203:180438.717228:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԉ\x91љq҅ɥĲ«ПŰĤƽ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƍΩŗзĵЦžԖʆaȆеɒԩǒ§^ʑԫŗϗϴƶҥÖȡŪǼaǊ',
                                                                            "ĕY˶ͿѿȺɾѽҩȤҹĖƯȈхş'ӽUɀԒɞ\x935ƉėɚϣʚÁ",
                                                                            'ʫЊʡʌ2Ҙãԭț҄bƣΜ΅ƸѥѫŎ˚Ѣ¯Ӯ˻ˏԙˆ\x82ÅǗш',
                                                                            '҅Ø\x89яϡƲP\\;όȰȹǆʚЧ˟řѦɎԚ×ғБûӋ\u0379ń@ȽϽ',
                                                                            'Ҳн¶Ƨņ҈ΡιƔҴө3ѶĢ΅ʇ\x89ɰǹˢųÞĿǯѹɨѣЭɬг',
                                                                            'ĥʊïʾƖ\u03a2Ͼ²ðҲŮѠːȌοɑƻƦʡÂӋơς΄;ԂτѠӟͼ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ɛ˽ҥƔÄұĳȌŞÏчȸöҾѯҸȉ˓ԗːӲӲÕżűŇʅO2ɜ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4147750730057848614,
                                                    },
                                    },
                            {
                                        'name': 'МʽԢİƷÒƩ°ǓʵŵǰɠǡʤбƆ;ϨЃwĺHиӼƅ§ҊӨe',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7656835548417021370,
                                                                            8083660644379783749,
                                                                            -721302520610918084,
                                                                            8585791495516280510,
                                                                            -7103771588936692483,
                                                                            -2573846539616299544,
                                                                            996593813423665186,
                                                                            -9025483564987034022,
                                                                            2548487963757464614,
                                                                            4991513858332806563,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϽúʮľɇԘʵǚ·ϷʌǽȿϧǔśчħϕμʵǀѢѨ˕űǭҪ¦ȁ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
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

            'name': 'Ƞʭӻ',

            'error': {
                'identifier': 'Ә·Ωŀʠ',
                'categories': [
                    'network',
                ],
                'error_message': {
                    'catalog': 'ыȌ',
                    'message': 'Џ',
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
            'event_id': 'Ѷ\x87ˮĠķҡёѲӫϞǣԊÉƖÏĂҫˏƵгϫӄɑКɎԓҷϝҵǤ',
            'target_id': '\x89ҔҙüхÓΪƘũł!ɰėаǨԐʅ\x93ҶӾƶý',
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
                    'event_id': 'aǞǑÞҋĒȅXȔïԋƝԈϪŴ\x93\x80ȧӾО\x93Ϣ¯ɘϺĆaѸƢȗ',
                    'target_id': 'yõЌșϻɐƬԑïƹƜ0ҸϭΔϲԒϚÍ¡ǼƳӶôʗЕˌ\x9flǱ',
                },
                {
                    'event_id': 'ȧ\x8e϶ϩӝҞĘÑϫv˜ǫȤ\x92ɣϭҗԐԈWιǾȤʕь/ʐtЈҭ',
                    'target_id': 'Њɗ·ɔӛɯčªԗTǖȏʚΝǎ˗Wɍϡ®ѺѢǒӞɩųє\x9cƑɳ',
                },
                {
                    'event_id': 'ОчғӧʷӝњӊɞɤҿԧˬʣóԥͲɎ¢ҖҐtΰǵЋǹŪʌ\x92ƕ',
                    'target_id': 'Ѱˊӝ˨mǓǿȊĨƅӹ\x87ɜŭ˲şɞŶą\xadĴȂщʿԨÞӾҺȱ\x8b',
                },
                {
                    'event_id': '«ƷĭǠЦǣ\x86ˇ\x82ǒИΉǹѾʤŝ˽ӽԚɰȓčǑʖAͽ¾Ҏԇɖ',
                    'target_id': 'ЩΉˋɑ~ûĪêǭДFλɨċįȌŉԦʌШΦğѳΆŗƮůĦrġ',
                },
                {
                    'event_id': 'ʫųɫșӆ«ο˙АŉΩǟĹ\x87ɏ$ҰӈȷӌӐˠ˚Ã\u0383ȳӜБˠƴ',
                    'target_id': 'ɪ:ҍ\u03a2ǠUУʪúȐȖǫːʉÎˡӝɫǅВĆÌѯӖφzĉɭŮʈ',
                },
                {
                    'event_id': 'ͿѥӮɭƇҿЁԋ\u03a2ҟƣǍϫк§\x90ԞԏȑѧшïĒųɵҭӄɘìΤ',
                    'target_id': '˧ʢUʧӡθϫɨͶи{љОυˤɶȟúìȜ˞ĿЙȓơǩ˅ΞүӋ',
                },
                {
                    'event_id': '\x8bΤрÌŪԓИͳ(àҖҎ°ϼ¨OыΠС\x85őͷˡѵŪÖδҔĵƲ',
                    'target_id': '\x87Ӎ\x84ϖxȸЪȄċˢƏӌӴʆѠϓºЊЗǚưҩˋźԫ*ċɱǞө',
                },
                {
                    'event_id': 'íӋɨ?ŸѲϜǽ\x8cҔíɇʵТ+Яӗī;ȏԛtȻɤȪƐǄȋҾЊ',
                    'target_id': 'И@B<ĄpɞʘvǾ\x81ʏӡ҃ɫѫіyφϜѹξôŞɭƔ˕Ʌžΐ',
                },
                {
                    'event_id': 'ƷмũƔȎͱɲԒʇɂǧϛÜoϞʯΈÍƕɶ˜ѼӸцԃȵ\x9eʭŎʋ',
                    'target_id': 'ӄΊετέԩ7ҒӂǡδD\x9eÓίεԗϣȜNŲϺѫϝǣɣԋƒ[Ӏ',
                },
                {
                    'event_id': 'ͷҁ΄áFxƯ\x86ҬӊųʧԅȊӬԅıǚӄљЀªɣšŮ6ʎoғҺ',
                    'target_id': 'œЂɲǥȇҦĝўΒČƳԍѷӝïâŨȁ˯\x8dǜёüІʹŋǌǈȌќ',
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
                    'event_id': 'ыЈФȍϋ|Čń˽¤ɵоњĚϗϹǏ\x8bˀ˾ѣɦPĢϺӅϩñȻҵ',
                    'target_id': 'ĈԋF҂Ō>щɩȞӄʔǵǎҊǿɦÑō˫ɹȈцԧС¨ěţͺÉɸ',
                },
                {
                    'event_id': 'âˎӃďѭÁϮÅ,ĵɂҢӷҝĥӀϹŊŞϘҐĆ«ȑ%ÉŹҶ҈\u038b',
                    'target_id': 'ʈήɷѹ˯πèʹҁϐβȟǋˍíʓѾ˰ĸĉшїɗħʢˆȖ?ȏɪ',
                },
                {
                    'event_id': 'ёƁņ҄ѴпǍСǝ˯ƞĄϦϼ\x82ǄɎ҃ӉȼǈђϺʟhʘ˶ʛˬȨ',
                    'target_id': 'xˈȃІÁŝ\x8b®ҔŚЏώǛ\x92ΆŋȎɕĉ\x99ȩп\x8fɭӧ˥ђԄԑȆ',
                },
                {
                    'event_id': "ŞӲŏȏʘĝ'ǽǸŶЏдЎʀ(ʰ\x82ӶˆТ\x9fƾǅ×ĵƍҧɫӴǗ",
                    'target_id': 'Ǧ¥ЙˡԥΰŔʼĞӾ˽ЫȞÊʹѦύԍԐƂżʚ\x99Ѻ˅ƨɊČԉŋ',
                },
                {
                    'event_id': '˔ѭŌƴ¼џԀҊŀcѸǃƕΤҵǱΆǣϮÈķЖԤñҲ{Ŧѱшѡ',
                    'target_id': '΅Ѝˆ<MϾιћZ[ѩ҆ӊǩϦVҴǌď˄ˌԀŚʹΙ\u038d²\x82Îΰ',
                },
                {
                    'event_id': 'ƧάvǜӏбМӆįyɋͱ\\еѼҽ2ǽrÖǶԉӅĜ)ҥǾeȿǸ',
                    'target_id': 'Ŭŵ˛ҙáµξĬͿӂӒ%ΝӸ˰ÃʛϐӊʞǷǴΫԛѪ.ђŌǪʗ',
                },
                {
                    'event_id': 'ËӇҐƽ\x96Ԝ\x9eъӿͲŪϤΥѿ˛Ԭ\x85X1Ɏ˱ԔƷľИȵŝìϲҤ',
                    'target_id': '\x98ɩѷʇϸѴԓž˰˅ǼԦ3WɪÜȅʦϧ˔ɠŲÏӗԌĩſɀcŏ',
                },
                {
                    'event_id': 'Ҡ΅ԑ˷ΙѲͷJəјҍʡƹϧˋΝOùȐљ\x8dϣзЗƤ˙ǌĂʱϣ',
                    'target_id': 'Ί$ƟǚǅɦҴÀ\x95Ô;Ёǐ˽ӖτӔN˜ԃϰƫȆ5ĺϠċʉѠʣ',
                },
                {
                    'event_id': 'ӇђŔˁƋɽ\u03a2ҠɈȵ¤˲γ^%ȺÒā\x9aчԝvǜGŗíӇ\x82ӾɃ',
                    'target_id': 'υ«ɯɶƖΨɒ_ΚҏМӣ˰ӿϭчxƤӓԠǝӠſŇľѲ˕ρ<ř',
                },
                {
                    'event_id': 'ʚϚȀî˰Ɔо˩Kӛʩɂɾƈā\u038bĊƃǅ-\u038bͼQэǖŃʆΊг\x90',
                    'target_id': 'ȓ\x8dĵ³ôҙǵһ¯ώ\x98ȊĲʣ˞ʸāϸw˄²ԉÔÕҒѾӶ7Ǜ˟',
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
