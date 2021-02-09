# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-08T21:23:11.152882

"""
Tests for the foreman module.
Extension petronia.core.api.foreman, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import foreman


class SendEventAccessTest(unittest.TestCase):
    """
    Tests for SendEventAccess
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in SEND_EVENT_ACCESS_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.SendEventAccess.parse_data(test_data)
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
        for test_name, test_data in SEND_EVENT_ACCESS_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = foreman.SendEventAccess.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


SEND_EVENT_ACCESS_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='event_ids', name='SendEventAccess'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='source_id_prefixes', name='SendEventAccess'),
            ),

        ),
    ),

]


SEND_EVENT_ACCESS_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'event_ids': [
                'ГȻșΆαƞȯĐӁ:ϫȓ8Ãúҳ¯ґϬŸ˦\x8fϔư&ѸΆӷђñ',
                'ɊАРС=ʯťЎʇɛ\u0379)ÒϻԭЀ#ǏdТҮӸөҨɍ\u0379\xadʈDđ',
                'ʀ҆ŷӈ\x85ºķф˪gΟ¶ǺçљʪɆбӘӆ¢ϪȽǂӽǢĜƔʢř',
                'ƬïӟėƪǁΌѦƁĐ҂χԙYˏҿǧ҇ʴʺʐϿԒrԍϯOʏԗЀ',
                'ɨeȿǟӺʹԌģǱ¯εЁǑ\x7fϤȤҶZѩɗ|Pýƕɴȹ҅ĳÀɑ',
                'Ҝºɡ\x9cʐýВÏ˒ʒЙœҷʢɠǈőŸϪÐĎϪ¼ӯѼӬϺʣŭҞ',
                'вʠ\u038bI\\ӢǐĝnǔϏӳϞǥƟǗЭҥŧΖŜ҃ŕħӆȩю~λƒ',
                'ƿɬȥ˪ƂiŨȚУ·\u0379ʹʅGȡƋʵƂϕ=Įͺėθʷ³\x96\u0381ŷɑ',
                'ԟˏЭĕΥKȃŋÈµɑ҃IɉИ˴ϸjσ:HãǠͼΠĦèəñӏ',
                'ІVÞƞŠʦŽӁ˥ƌҧѨԖ˧қʵ\x81ӮƝѸӡ¹ЧëϢxƶɗZϔ',
            ],
            'source_id_prefixes': [
                'ɁзCŠǦ\x9fϜѦ<ѦӐˑǏΑʢÎûWƯMƻÐϽҘƸs7Ͱşĉ',
                'ӡƊ\x95ŘΉʂˍӌԓŖÜɒϪƗ˩˓ӕʭɴƜɉŖĔ\x9dʞЎȫƪǎ҃',
                'ӲʷɆ]ΐҚ¥ŕ҄ЅˉϖąíϺĿԍϝѤRǟȒuơ[ўȧ\x844Ϯ',
                'ʙɰкϩԞӪ:ǛǤn\x9aаӏҔUΒӟ¹¢\x84ђ\x9bѴ˽ʓŪ¡ēԦе',
                '¡Ͽфʔ¯ˍÒЇӘíȒƗ҅ʂIӣh$ĊµÙζЖ˾ʡ\u0383ŔƘÎԫ',
                '³\x93ŝ\x8dЩƹӵέϵΌӴӘŊí\x9fЦ˖ԍ˹¬Ԉ\x98ϘǗƌƒˬÛŎϧ',
                'Ѱˡˤęȧˍ҂ʒΏÒ˞ŒσɱĜŰӝϫ',
                'ҎɁԓԌϐÂȻЯ\\СMϻиǮěҥђцŉυĜȪǛӲΕОσшʜӽ',
                'ԃJƅÃ\x82φȡđƶͶćĸɷӪӓԗӡ£Ń«WӅ+ԑϗŴûϸ˰{',
                'ǄκҁʈÅΉtзӝŋǅSA~ӎƏçχӪÖĭ˅ŲóӮʏƺ,Ҍѩ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'event_ids': [
            ],

            'source_id_prefixes': [
            ],

        },
    ),
]


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
            'action': 'Ğ˩ɅʙÏ˅҂ӗǰθ«˂ćǕρв˟êHblԩ\x89Уʥƛ˘Ьԡˈ',
            'resources': [
                'ҧǧ\x824Ý3ÎóӁΖ;γƎʿșѳѲ˺щƁǅ\x84ѯβȣƽХèĦǫ',
                "ĭӷԜϪư'ȁʢӜԄ²ËԖјFÍǒûӄљ\x8fӏŒ˚¹ԁӛΒǡ΅",
                '˨ЋΡÚʓƷʆρцʉϓƍЂƬҚǐʗò.ɟȮѾƑˌͺοFʗХĳ',
                'ŗ\u038dɵˋĉʀʩҷϰîMƊԍŧ:Ò?ˊ\x97¹ĎͽѻÚǅrɨϘΜϱ',
                'ϪđЊȫ\x85\xadЋǼƊ§Ϻ²Ųʬ З_ɖ²ѐőǪҦƮăþΩǰĮʯ',
                'Cҩ×ƋĂŦǡѹˠɰϺˁćѳ{ȑŪëԇϋεҞŲƏQǲźƲǹÆ',
                'ŤŶȭǟҭhÿюɒèӼԋӽÄЖŭʜţðӉ˹ðԥйɈǶrɪľͲ',
                'Ιæ®d\x7fĨˢŨɓʢѽҋԌÑСΣŜĎ-ǶǧɟųƙùÆâɮǵɛ',
                'ťƠЫȩȟiʬˉGÈΖтãʣԢŅƫĻе¼˘ɃćѺƐrŴĒΆӵ',
                'ӓǘùŰĎK^źǬΈоԮȇɹҊʾƯɚŌʢȱkȤ˞ɀŁЇAČʤ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'ê',

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
            'name': 'ĸНĬ\x80QŕŔѪǨԪâѶԁ.ЅϠ҉ќŔҾҵӇő#ҭ+ȣjӫГ',
            'version': [
                -4795760346342163267,
                -8923401228168995580,
                -9092147380265634126,
            ],
            'location': [
                'ΩȚƮȐƺѺϋҾǻӟϺϿдԉƇWóɪ҈ӨбόДΆӦˇӏӟӡɯ',
                'ҭˁːȐƺq=ʆѕ8ҌĭĐΛДΓМҽÃǩϣɸƂɸѐ@rѢǖ\x93',
                'Ƒ\x91ҬÃú;ӆɈњ˲ΪȢmqʫҌѭɍ\x9eȰӟϙ0˔ũƂɉÁȤӬ',
                'Üӡ¼őԟ˗ϳ˂ӪӈɦԅԐƇɄÎшȨɲйлǃ˚ƌĹ\x9eƏ\u038dm\x84',
                'ƴʎˍϩȫϩϲ\u038dŵɱӛǸɗд˄ԟώ˭ɝηÄ¸Űʝ˯@ǱΑϰʝ',
                'ǚȩΜιϑˮʸȾõǠԕκʇƕǴʁôļ\x7fɅԇʱϼʊÜӢфӸӿƵ',
                'ӓɰЈ\x91ˮȄԝӲрΌƃԑ҅ήфưϾ[τԚҲʐτŦъЂюјȂυ',
                '+\u0382И˝ѺЇķԡƶԈ\x94Ҽç.\x8d×\x92ʴ¸ѴƉϦīҖρςӭЅ\x9aƃ',
                'ѡʣΪȑǻĮʓɘ/[ԨγҠӒǸ˺ŉќˡ²ԩԍԌ\x83ҷnȉ\u0381ʁД',
                '¤ϳ¾ȜʛɍȝĘӵƘd8ӿfǌČԅŷ\u0381ʆðǵҨƩŖĊҼԃŔІ',
            ],
            'runtime': 'ԔԄƢeȺÊʼǥ}ӗ\xa0ĮϽ.˥ίȋɃœĩsҀӟˎˈ¡ÓɕŷĨ',
            'send_access': {
                'event_ids': [
                    'ыĮҎǗ\u03a2ǟʱ+ϼƅɋǋϦÇʣǆϩɌȅɒπ?ʱ»ЪӶøŭ¢º',
                    '˞\xa0όцȐρÅҥКzєˈҮ҈ѨѵʜņсĩԛĞӝԐҎҗņӂrӮ',
                    'ԟáǿɷΚɶȓLӖɿϠʩɉӱƾͱºΜ˱ȰµӅđŽέȵ·Ҟŋǽ',
                    'ƫĻоŭ\x98ϵҮц˼ģI\x84ʻŅŬɁ4ӪȐǗĬ;ЭҮąȔƾ҇Ƶҩ',
                    '˵ͰЩЏþͽ:ĜԘġңďȹʔЪȞϼѳȰүЫюȚΐȴʿЩΏßȺ',
                    '\x94ǨѪѧŉːϚŠÇʝJϒ5ƆͽɏɃҦ\xadˋ±ΆDЋLŒХɸ\x83Љ',
                    'DRȽщǭΪɝǾρѩȣƊχӸĵĘНӟɾʮǀҜӾƦ˯Ԁ\x92ŠӦλ',
                    'pɁgŒҗɩɠҼʮҲěĹӤƞӓͰԟПǊ\x88ͳȟ˳ΨɡԐʀRӐŽ',
                    'ΩϡǮгѱʧƻӀΏƥԂȨîZÀmŠΨƬ\u0379ţϏǫȬԑрϒнͼҹ',
                    'ưċŭƍϘȭϷђӧϻϖ¤ìýӳǦ˖ҥćҐĬǜđΎ˷Ӫ@Ӑľз',
                ],
                'source_id_prefixes': [
                    'ĎЮņɍԇԀΒӜŷļˁ\x84ϙ˹ϿёԪ˚ҢƃӱԮƸɢІϲ҈ů\x97Ǘ',
                    'ĴķʚδǷӐӒȔȒĠ+ӻӝȞнÊŧźԫȓǺŅʦͳƶBʇˤңѷ',
                    ']ίɞȯŮԭȪϖ˵ȶñ\x84ıфIȄɅːFζòŴ°ѧͻκ\x9a#ϘÐ',
                    'ș\x97ǂ¥ÇԮѓʻмʹʊЅΌї\x8eˮѨĳ`ϯӾƓӥ}ŘƯĽȢbӛ',
                    'ӦϚÖŘ\x926ӹțΈƔ¥Ǣɤʒ˯íχƁЄȰ',
                    '~˦¦ʆ˱қȮɓ6ĵȼƜϓįɚƺҮưǖńѴӪɳŤ"ǌŇǉȐȢ',
                    'ǗԘʙѡȪвѢӸňĲԘȐѝƌ\xadȽɋʍˮāɥșˬҞϛҽ®\x95ÊɁ',
                    'ȟҪΜƏF\x83Ɂʞ˶êƼң˝ɞřƊʅϗȅɖɪҤɚˬѴіʑĤȬ\x9b',
                    '_җŮiҤϪ(˷ϔŬǫňǫȒĎδ!ԃdӢʣѯƫŌѝǁLÄˊɠ',
                    'ҹ\x8esиЛϴχǤʯƄҡʶhӼƾÀ˦ųˠƶýѼҍĚӅǤϬԚю\x91',
                ],
            },
            'configuration': 'ϊɥȵӞś\x91ҬÝϲĄΡĪӱюǬȕώʓoƻűӵУΎЋғLϯȔː',
            'permissions': [
                {
                    'action': 'į\x81\x9dŬϱ·ѷ \x93ƙƙƮԛʉӣo¾ԭʄԉ¸БЮӿˌĮŹʶЯԤ',
                    'resources': [
                            'ΧЕʱӔрȵʉżƻʷȄǜϴʈͱ˽ιȕӖĤ`ˈћ\u0381Ԟ=ΫԉOѯ',
                            'λЩȡԍ\x9eӟƓΡ\u03a2ЦǤ×ӺȹĦԂȑɬԑÍӊƩ°ѕϧʨΠӭ°ӻ',
                            '|ʧŞȦȞˉӀʡӺйΆδł~ŵļÛџыôŦɵƱƼђîſӱҡώ',
                            'ʉȆǸǔ҄ЊҾǏɢƜěůtǗħѷGr¯ґȉŌǸʞjdӌωˣӼ',
                            'ˣўрƹɹϹ$ƵѥΡЫԉ#ԡɵȂɉѷԖȤьҟȻҺƧΚԩɄĕĊ',
                            '˞\x81ЕŐѤ¢ǳ\x9cĬυôϞɪҭΘ?œſmÄϨÏΝϪ¸¦εŖʛР',
                            'Ҽ]ӦďǺ¿\x80ˬ\x97ǈĠű!ҕǺԞĢѭ\u038b҂ЄɓɰȴɛОԫҟѺŽ',
                            '˄\x9cÄԅǁĝ%Ïʑξ˘˟Ū˸Ӯԣҫ˪ƛϾáʧπǶУ·ʟɪԛҳ',
                            'ѵȤɮeӊɵ˦˦ʥɏƓřté΅Ȥҧӱȷк\x8a˽ДȈÐҀǻķąҸ',
                            'óǰǓ¤ĖлĳőǁŕƭѶ\u0380˸ŇηԨ͵ŹэƃɄ҃˪ΈÂƦԚǾё',
                        ],
                },
                {
                    'action': 'ȟӤňҸφɪҞȻÃ\x81Й˱ĩӭ˜Ü\x9fτĔʰŊĂͼѻ\u0380wЫҖɹƋ',
                    'resources': [
                            'ʌ7ƋїԐ´ɴҀƍM<ʾĳηˡΕδÆʾʤӹCʶїϿɯɱΞǻɵ',
                            'ɿҍƍȲɝAvɶԠǈɨӶ˒\x84lʙʋѦԕ˒˳0ƋюYƱÒИҾh',
                            'ƻÓ8ҝͽbΙǏsƔİƐŤПÚѧСƅȰʎê,ѮǗˀXJмƱʺ',
                            'êҶҶӞȱÁ½ϕìɄҺλӋŐАˁʏ#ԁѓîæӚ]<Ƥ\x85Ӥвɥ',
                            'аͳȁ҃ʁђɣĮΝ°ºԄ˺ȟǫ˾˦Ѵǳз÷ÎϳқȌʺǽʵɹϨ',
                            'ʃ˝įˠãUњѐĀđγӽæΊhƒĨӍȸƅ;ѪþθҀҽǅƎ¤Ǽ',
                            'ϛ˱Ӯư³ӾĤ®ХԒÕңДUйӋϨȵʲ¢ʟЪÞJªǂƾϤϳĈ',
                            'ӚÈņΕʳѦŲΗØȑ³ѷѧ1ҫÏʨӊȯ˓ѬÜêΡưҴѲЕџǢ',
                            'Įҧʼ\u0381Ƣƥ˟νΏЛìӡśΡċțэ!ÃʫЖӂŸŉĵƺ¬üг\x89',
                            'ϮľеӣԓғѯƬƝȟ҆ƐӾπ҇ѡȧǦ«ȼԧxԡśлŵĀ˥υ˒',
                        ],
                },
                {
                    'action': 'ȗРąȪèԄɾьԄєѶʜ\x89˷ďǥӽÛǩӟυˣцâ0,?ΡǿѦ',
                    'resources': [
                            'Ӗȳӛ¥īȪӆAԠϛƘӼρĢʭŲɅȓԉ\x99ËΨęȘșďӆĪÏΐ',
                            "R2ĲɽȨǄϨǪȿԎɤѵ@ý˻Зɿӗ¡'ǾˁǗ\x8b¥ȉuƯѪ˒",
                            "$ŖŤȻʽǵҰԢѯŴȮԗ'ɶÌбưķҤvǸĒȲ¤Ĕt#Ӛ˜϶",
                            'Ķ˓\x97ѿБ˚Ǖ3ίƗşзИѩȁ҉Ȫя$ĊǇҨԚ΅ƽƾɃžΗľ',
                            'εÊćǇӣâǢϰɝďÏ΅ϱ\x9bѠÜΘҔϞ˹ŎǤͲ',
                            'έɵƌȖү!АʠˣǥŢxɢѢȁGӤ˪SɛɎԊӱÈćǆĳƹȃø',
                            'ĭGɉĆȲͰÑEǩΑäԬҶĩúӢΆĺҎѪϜ,˶˩ó҄ΈήǗĹ',
                            'ɷԐӛρƂˏƽsÔѪЦŤΘ\x89ˡўĽƝ¿ßʙЅǁFTњдœԩʦ',
                            '˛ҠԈǂѠĝΤîӃ˭ϝҸеӆˎ˪śʃĿ[ɳæÂ*3ҙх¹Äº',
                            'ήęȈûn\x8fÿўŲăӐБhрċҷԐƅɂēâӱω˦ҺҪÊŔϼg',
                        ],
                },
                {
                    'action': 'ҽԘϑǩѾʠҰRǦɂĞʾšξâɓЩőƅ\x98ɇϚəјɄǦYɄѵŎ',
                    'resources': [
                            'ǸĬȿóʋ¿ώ\u03a2=ʫеƏάǀɍāȎщΣЬ˶ӍͳĝҮ2ǚ',
                            'ȩϙáǷ6ǣƒªǘŗѭΙˑʥˎƴċЋȏӠűʡȁͶȱ|ƵǁƬӭ',
                            'ĩJMiħφҴЪңΘɳǫˏʽɓCǡEĈLʅ1ӊˏѻԒԍðµõ',
                            'ʇ5ɎҴ\x91\x83Ώґ}xˏŤϻȷӠӡқ˕Οɱ\x86ǹѤȖњʹ\u0379Ȳ˦ԡ',
                            'ǑҙʾàλƥѳƥȻÏϰ҉Ԡ·ǙǉƈͲȥΝʌǻñǉԤ÷҆юŢ\x93',
                            'ˊґǝӓѣȣұ˗џӎϑҡΟΤАжɰɨƯɭҐŌ˜ӗǤŭѡo˅җ',
                            'į˒µDϤ\x9b˼òƈѻ\x9dΧԏȚʦƳѧöţͼȴǲȦƋӁ˭Ѩŏ˟ˁ',
                            'ӣďƟʞ˷ԞŬӿąʵƣʊǫù;ӯǙ˥ļʫŜɕɞҋԅń5ǆӖε',
                            'ˏүʭȊȢ\x9a˕Ƨ˛ɨɏɐŻ\x9fƁƉ1¡ӪĨˢҍȝÝdÜʘԠͼƧ',
                            'оӊʪȐϨb҈ѺԎμԐļçĜʞlŭʥʑΒʨѝЙɑʛ\x93Ϸςӝԣ',
                        ],
                },
                {
                    'action': 'ѵWЛŊÑ\x9cĐȻǲʓɃ¨ͲƂƢÏƇȇŏɑВ˳Г˩ǅΕԩӣ˩ȁ',
                    'resources': [
                            'ԛęūзĳƐʫӲŔΜǙȄс`ΌƗϛǅϬ˖ҢбĨѐôОʜƂʿӀ',
                            'ǚԕɮϷSȪКΫĴʺƒΟƲΤИҞUȸļνʿƽǤȋЃ҉ϘԅAɽ',
                            'ǻɂȕ˱ÔѹJZŢͱЅʀ ʖƓȤʃѯϜĸ˾ԡ΅\u03a2ʆғԕѴ;ʍ',
                            'ЦѠҀ˖ǲӂҬĝƮͻсрƙіϩ˵ЂԞ+ВŸУҲô\x8cƐĴӊϏk',
                            'ʑɀЙʽгϞҟ˦љ£āҖψӘƬƼЋǔ ˍϣӫľŮǟēѲàQƝ',
                            'ŁƸϸρҩlΤƮΚѸŝÊδ҇ƾǰ˨ȡѯùԂƥǬҦŃоҚɐ҄¯',
                            'бƌҍӸ',
                            'ϢĔҥăґӣfˋèţɽ\xadƁӈˈʐɀҔЅЌʛ\x81ǱђФцюӾӰ˹',
                            '˨ǞÂʾɽӊӶŻż˧X<\x80ą÷7εβǷɁ҈dýƖ˙ȑΉəƝɢ',
                            'ΚYӠҍԧȖӗôюϡ\u0379ʣʋċԑǹЪœÑϗˆӜʞȺ]ǻѐѴoʱ',
                        ],
                },
                {
                    'action': 'ӧϭԎŖӌª˨¯Ǒǎď.SˀʸëʌëѳΠİͷÈȷΠ"ҴҠǓͷ',
                    'resources': [
                            'ɧřΐ˚\x85ΞѼԉҶŘŶѡӼŴӨǿǱʀďȸƚö<\x8fЌҶӅ˦īΗ',
                            "ȮĨǌȮTҊŘIІɳÝ×ӹǵRΣЬ\x89ӱɺǏKƞЉǅԫЭʊƙ'",
                            'ĭѝȆԁƵŸ®Ƣǹ҄\x9eŦ\x92ɝΎѵћķǿƴƦϑħδŪͻЁą҉Ǯ',
                            '®ʊǈΎѤӇƲʉǾϙŶīȈǠƜƸƞȩĬȇԨȲƋϊҸϡĴɻƐШ',
                            '{|ėŀϸӤŖŴӂƣϨYʑΔӦ-ΟƬ`ÂôαԅϘ\x97ǞϸÍ˨\x96',
                            'ˋɧӔƏӈȵǝÊҀƱvΑœԏŞĒї˻ԆΠӱ˂ͻǥ\u0379Ɲê˛ЀƤ',
                            'ԥӟҺɊйʢȬԕ˦ʴϿЅʚЂǠȉŐӭƸʙ˚ƤͿǯϸƋúǥҺϼ',
                            '˷Ũ3ĶǥӹQѝ\u038bƚҕҠĢÙҿԩƐϻәԭӈÐӓѲ˹ͲԮsϕǨ',
                            'ѳlʕȐʪ\x92ŭʡGԨ˫÷ș6Ȯɪ+Ŭƴ°ʌҵҸԢФZѝʧʶҧ',
                            'ƙΗӠӡϑǭԐȼʡÛΕԃ¹ɷǼǷɞҔԔăѭĕƻùɐ˛ʼ˄ԫ\x8b',
                        ],
                },
                {
                    'action': 'ΫӀ˦ԧĚƲ§˨˾ƜϽҵ0fѾГӆɢȥЙӓƩʏvˏyǕɘʢԡ',
                    'resources': [
                            'ыʩQɃɌʘʂȠѰдҀӭоΕİɜºʜԑȸґЇʎ˼ȆĽВ.ƹҞ',
                            'ԃӼӞ\x9cñ˘Ԟ\x86ŵЊƓѠȶĕǂƿИǳӲŒϏɪɕĀǥѳ6ĕΖȹ',
                            "їÕԔҋӵл'Ɨ҂˅ĦϓќӐԀɎΈҨ΅ѾķçǣΠĔΔƊРÃʧ",
                            'Ӵъӳψ\x95π8ўıǱʵԍѼÌђϼėʬΨ˫ιϦΘŵё=ȗĳИ.',
                            'ƟϷÄӌϮǩƣā¥\xadЕɍҾΛԅ˥Ȗd˗üˑ\x9bˤΤ˶ǏĿɝ¦Â',
                            'Ҝфſ¸\x98сHǩ«ǤūǂıʝҍƆɪĳ!ʓ\x91ήɞǭśЗóϷǿ;',
                            'žƓjŦԄʬźʀϪɠ˽˽и×ɡȤԐɾӂ\x8bТϔƽʩů˺`ӦƆҢ',
                            'ʖùȽѬщƜŵʼȽĉѱZrWǭХÜȒҼеΓЩЯ˔ϼœӚȏΆΪ',
                            'ɵѠ©Ґ˜şњɇnϚ҅Ӧ¯лҊʴ\x9aѬʦǈ˸ĵһжӛČΰįsК',
                            'ҙӨʡɡˏƶӭǈόƨăϸŕƉ=š˕ЖƴϞҨǨο{\x87ą҆όҜ|',
                        ],
                },
                {
                    'action': 'ɇƉǡνëГȿªβȸÌcǊӋԟѩ\u0379Ȭ˧ǆƂϜÃręƑΙŉǠԎ',
                    'resources': [
                            'QƎƸӔĮ\x84ǣÜ\u038bҙӊяƗϒɐӲZЫȈԆǭʐϝµ҆ȷÛϻ,ı',
                            'дҋƻ÷ќΞӜȆԈƋgҫӚƯȭŦÎ˷čӿžǐΓͺŝȴҹΌɰĸ',
                            'ЫTȬŦɔʀΖӌ\u0383ԭкŲǃ˒\x8dϴЌŉċ\xa0oҦˡϡѭƠȕηʽ˛',
                            '\xa0ΜČԣӚǹƷνŴʪλɂ:ԪǃԕƉʄȵӄɯ˗ӅЌ&ǬӳȄЩÌ',
                            'xźӺўӭ\x88Ԃȱĵʇɒҟŝ®бńö\x9fÆ)ҧɽˀɌбȰß\x86ǋԣ',
                            'ҰԓȚΑƛǈӐԀ\xadƂɁ\x9aςɍƝȜȧѥuŧˉȐұӑ\x92ҏÎʪʺȒ',
                            '˷H!ʠK\u03a2ԙҤɈȗʥΡӠΟǥ\x80ТțŽǯ©ΪѠʦҨǙŁʚ\x82Y',
                            'ĳϬµƩ9δҍƔиs˅ȹƇHυʧ±ĖSŉҔûўJˬȟƤԞ˦A',
                            'ͲђĳЙËвûĺŀɉóȹ\x9cҖҔ£ίĊɆŇό=Ф\x90ŁʋοwҊϥ',
                            '9ˍзɃ\u038dȸYӵGϱǵɤЄќζӽ\x95ÍԛԩŽǄʁ^É˭ӽͼŀĐ',
                        ],
                },
                {
                    'action': 'ȢǸ˜)МʶșҶҺɛӍԈɇϢʧòĢзҡďҀӢyW\x89ȏǦ\x8dÇƓ',
                    'resources': [
                            'ȐñҒˠŹɞӲ˦ÎΗƍҶɻϘÖόϿ?ġҁч˓ΒбϤqȖԍŻщ',
                            'ʗƟЌǮòĦ\u0381ҾҏŷͰʃƏ\x8ažύjʞ˫ÝǢÃӨϺԧƗĀµЧ\x85',
                            'ɀΉІ/ĕω˩ǯȘφˤȭӠϤˏτȥĉÓčΉ˨ӍԅıϞҸúżҏ',
                            'ԓˏǰĩʽˀϟ\x9fʿϸϧUĴçǬҋĮΎĞřӃǚǕ\x81ɇȷҾ\x9cьѩ',
                            'ғƆ˖ʯԈƫҌ´¾\x86Ǯǀ\x9fŠΜѳɶȕɧ5ґяSɝđ?ĐШªĹ',
                            'γМЙĊϋϬӃǉ¬ʫԖɦơΖœ΅ſǼРϒÄŏȀīǵê\x8aϙͻҸ',
                            'ƶȨƚϲӮĩѦsϷԚêԮҟ\u0383\x91Ȓ҄Ŷƾİ!ǞƃҗϻʚytȮ˄',
                            'ҌǜϢɱϙƿɜXҬɶɢɞȄžǱӃźʲ˵ϯĦɞ҆ϢӒŶӭϛɅω',
                            'МƋǔŲБĩʅœӃԒ\x9fɾӇБʃćêěԔ˧ǔԌ¨ȘϤ]ԒʞŅȇ',
                            'úƂ˟ʺϕǼоùϭґɧeʽҹ˺\x9aȺ¹aɪӏɾ˃ԏɡʷϽĶ˲\\',
                        ],
                },
                {
                    'action': 'тԮ˕ėʹϙėүХ¥ӐѺßƀӕʢԦȟɦΗ!Π˛ʠȥĤʽΥцӁ',
                    'resources': [
                            'δʯäϏșѹŽ˻ɒҧѲŃТΤŰһѱ£УӀԟʈҳ\u0383ϬˋԘĠΜ˾',
                            'жǌÊĺ`˕ϱǩЅȐЛǟАŋӎδԖbī˂ɗϖɝÈ~ȠѕǭƢ|',
                            'mÁʏǪΰԍķϿÞĲҀˊȡϺӽƷɦǖʔňЇέ҅кȪs^´ʂě',
                            'Ĥʉ҃˜ˮȅbʚɂρɜȾӾӬˢƭěҽÇßϺȯŵħÙƋϘæɈӶ',
                            'гǸҵͱʇδȑϔáȾ2ȫƶŒǒȰŖЈtγ\x9cĢɈ0ӮŭøѿȉȂ',
                            'ͻΗƞЮˤƅЗǾî¬ťԬȏ',
                            '˹Ɏλıǳҩ\x80πzƹƉiˉΖʥҼUʒӂõʓɳҐбʴϨ~¯Ԡ˟',
                            'ϳ҅ó#ǇӉƬëΈԏӲԈԋҤ;ġҪÏ˨ĮӂʮƌΖĩʗȐÏČê',
                            'з÷щԐŞÿϖίѕϿyɶÕԜʝεϑ\x90ͱ\\¹AŌӼЅʶȽͶǍ#',
                            '\u0378Ѽ\x99ӷ]ʵԩȧʰу\x86UƇ\x80ȧђѣǆȫ˪ʖқʖcǤеȅ>˟ē',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '΄ǚΑ',

            'version': [
                -8448085367431760856,
                -5052184207948249622,
                -7216904235534181923,
            ],

            'location': [
                'ż',
            ],

            'runtime': 'y',

            'send_access': {
                'event_ids': [
                ],
                'source_id_prefixes': [
                ],
            },

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
            'name': 'ɯίѡɔўӖʘʺӸUǺΎʷ˵\x8d˜ѱυġǨӹτɧęӘΡнќ¼ӡ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '»ӽλ',

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
            '$': 'Ӭøɿǈмǝѻ\x81κӵZƞɮɼʼșō(ȩϐC!ʦNΤΨ;ӮBĺ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 7627105858403794956,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 664163.194567175,
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
            '$': '20210208:212311.106799:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ϵƬƜ?ơѣΖϏ7ƕ×īӱɀЫğφ\x94ĸ¾ȭƚӐæϊ3\x92ѥɃƢ',
                'ɨĈǩ2Bν)%ϨЈӿ\x87ȍsƜ§л҉Ê7ԬͺʇȌҺìА\x97ȧʟ',
                '`çðϐ˄җϼΒȆȔ˾ʫɇǧΓČːɟϟЈǗÈ˷\x8eEһ*ӂĈɇ',
                'Ƞ˸ƱƇЕЛùзÎЖęΎԞΔ˞ɟƈơɀкʓƻрvˬǸЊȷԋŃ',
                'ëŌð˹ӁόԕÊɯ+ȃѪІӬЕʲύˌ˒ұĹĔŰʽϚƝĲǽМϱ',
                '%ŬӅаƕϡԌĥ<\x81ʾʡιԋŹώƑѢЙΨʦÆҖnϨ˯іȂŁЛ',
                'ЩͼжʃҫǠЎɸø³ӪǊƑäĹоˢК˥ɚɰǺĮ?˅΄ҩԆĂӲ',
                'Ƕ҄ĵöϸҜϧ˷¡ЈėǻʶЕԇŌƩԟϾБΎc¾ˇӇӆǊě\u038bÜ',
                'ýҚǰЯʍĐʍjǽҡ½ӢŬƣŜǒΆɤͺΞªѻʨġƀtˠΈżӷ',
                "t|ʯľęӟ϶ԕԨƊѝɞ¸ʢԑҠӧĥƒЖ\u0383ɖ'ϡęϿѩǮћ˟",
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                3976205760933658572,
                -3146236355409037789,
                1885111615541392877,
                -6558822056711591716,
                -4551666394986957854,
                -3930138473022622152,
                -2810300075374538949,
                -7884367469565207091,
                -7830164135543886829,
                -5963548790218827423,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                446533.63944701676,
                801507.6121463898,
                379360.6996302557,
                405072.8404252418,
                586842.2115743316,
                -15266.131932158838,
                920270.047256884,
                -79317.75338791114,
                548469.1509905526,
                47880.02321496085,
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
                True,
                True,
                True,
                True,
                True,
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
                '20210208:212311.107653:+0000',
                '20210208:212311.107663:+0000',
                '20210208:212311.107669:+0000',
                '20210208:212311.107674:+0000',
                '20210208:212311.107679:+0000',
                '20210208:212311.107683:+0000',
                '20210208:212311.107688:+0000',
                '20210208:212311.107693:+0000',
                '20210208:212311.107697:+0000',
                '20210208:212311.107702:+0000',
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
            'name': 'ыƊ&ԘδȢˈʹɍ\u0379ѡʈҮÚǒŚʳѧŖȢɵƊӳǛx\xadҘɌσе',
            'value': {
                '^': 'datetime',
                '$': '20210208:212311.106602:+0000',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ѯ',

            'value': {
                '^': 'bool',
                '$': False,
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
            'catalog': 'ã¡½ĵЇgҨΗɳȷѺǡӄ҇Ƶ˫ςˈɅƆƪƌͼĹИȩʨԆȊЛ',
            'message': 'ϫԊĬľ6ʯǺӌǟΆÙͼ;ȾϴRХŷϰõWԠϩԭңѯŚʓȂČ',
            'arguments': [
                {
                    'name': 'ÝĈɼъɪ˫\x98ˉāpϑoʐŅĎɤƿӉͳґǛЏϝҐȅ±ΘmɎҎ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -6481031813642871343,
                                        -1609491080312584123,
                                        -6719896350359246351,
                                        3030771271191831577,
                                        6007105381255397719,
                                        4318839759868811291,
                                        -2130234429082746369,
                                        -8183266323213200827,
                                        305074663471971619,
                                        -1076589148534962596,
                                    ],
                        },
                },
                {
                    'name': '˃Ƌл',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210208:212311.103939:+0000',
                                        '20210208:212311.103951:+0000',
                                        '20210208:212311.103957:+0000',
                                        '20210208:212311.103962:+0000',
                                        '20210208:212311.103967:+0000',
                                        '20210208:212311.103972:+0000',
                                        '20210208:212311.103977:+0000',
                                        '20210208:212311.103981:+0000',
                                        '20210208:212311.103986:+0000',
                                        '20210208:212311.103991:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ВzƠтkʹiƭӴ˨ʴʉ˛ӊҎēΦͳԗƏӭ:Ԯ˛ГԅοӝƅҨ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210208:212311.104225:+0000',
                                        '20210208:212311.104234:+0000',
                                        '20210208:212311.104240:+0000',
                                        '20210208:212311.104244:+0000',
                                        '20210208:212311.104249:+0000',
                                        '20210208:212311.104254:+0000',
                                        '20210208:212311.104259:+0000',
                                        '20210208:212311.104263:+0000',
                                        '20210208:212311.104268:+0000',
                                        '20210208:212311.104272:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ǚgɷƕǏϺūˣхϸԄ£',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        122971.52679199,
                                        839090.7181782669,
                                        506974.02072248235,
                                        -76118.59368433949,
                                        653458.1965718216,
                                        591723.794042915,
                                        145211.59104937204,
                                        635930.0893369161,
                                        458684.31320879667,
                                        308747.19796503964,
                                    ],
                        },
                },
                {
                    'name': 'ċʵсԂ˘фӁӣ\\ђϸ<Ԇǐ҉ѷѤƛҾ^ȟԖïűԂʴҽ*¾ҿ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                    ],
                        },
                },
                {
                    'name': 'ѱϐ҆Ű҂ĉŅǲǼ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        452695.5983210129,
                                        774631.4898896187,
                                        247800.97730759892,
                                        382988.9187622632,
                                        229763.49878478394,
                                        119379.16291877674,
                                        134223.9887477071,
                                        577280.1457860343,
                                        565750.514949632,
                                        5135.910579217481,
                                    ],
                        },
                },
                {
                    'name': 'ӈǡŰȬƆʩ|ӾѢ˱ϤԢ©MĿÇь\x85ɑŧĈʘʼ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        True,
                                        True,
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
                    'name': 'ķѴƄɺËȷ˔ÿÔğЧЯύϥӌǦϝɚ+\x9f8+ˑ\x80ò˕ŹĴǁĕ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210208:212311.105539:+0000',
                        },
                },
                {
                    'name': ';ҮTÏȢ˒ʽƴɒɒǷԔӵҙďϧӦ-',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        '\u0383®ѪƏˣ»ǧԥӈǲʯŴƃĶǙѤӵˤΏʃ˓\x98ǲnȗ2üœğǣ',
                                        'јğċɼΰʿέɋɭ҂ҁƲăЌ\u0379ƅ7Z8èϠˆǓѹЛ˭ΨҬľĪ',
                                        'ŕйùɲƤ҅ƌ¸˰ԟ˸ϋñӑ\x9fίҞņ˾ʩzƸ˕хű§˞Ͽј˴',
                                        'ңРƣӜҕԝχĶĥ˧ˎÂǁǭČ˰҇ʃOӆóɩӜƿƒӳȺĞԚw',
                                        'Â¹тԄŋҒѹαӶΔЃć~ªƕΔіҞӿ˛µҜӌѝ&˱ьOǭŕ',
                                        'ҼмǨțöӤ$ћͲßŠΏԭǬҗĘǓ҇ǰӜϑĖΧȠʋӜѻΧÎȆ',
                                        'ŐЁƷɻłʓˁ©ҸθÙԣӦóԦаŌ-ɉ҅ġɾhѿÅЖюπǷń',
                                        'ȄΗĚɕð3Ԩȗ?Ο˞\x9a\u03a2ϱԉĸƿԘȼʁɛªŔ˟ɒͷ˨Ϡóʫ',
                                        'ſ±ăҋ˔ĥ΅ÌǋҁӣʴŁ´Ќȡ˹ʤøÃр˓ăĸǬĉ˘ǧϾƘ',
                                        '\\ɂŏȼȯ˞˒ϑӢWҌӫѾɕ˱\x82ˋªȇϪϼ\u0383ϧΣ¿ôԛ\x9bԭϭ',
                                    ],
                        },
                },
                {
                    'name': 'ɆĥŜԑş',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -1625413893334327269,
                                        -6391743293102897774,
                                        -5990460133963045691,
                                        5075910912199187820,
                                        -5310821731774380328,
                                        -4955223202396523447,
                                        -2304849461487388456,
                                        -1742780417087896444,
                                        397853550171984166,
                                        3098211435378364817,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ͽ`',

            'message': 'Ρ',

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
                dict(field_name='messages', name='Error'),
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
            'identifier': '¤ĝ&˶ĞĪӇΌƈ˩ŚŦǆ¸ĦǜѨˑӇДЖӍȄ4ǂÊÑ˩îe',
            'categories': [
                'file',
                'configuration',
                'file',
            ],
            'source': 'ЅŮĜԨ\x91ԩЖĺǎЮΘƤΡÙɘ\x94ĳKǐŃȐҬɁGѕͺӞкáӵ',
            'messages': [
                {
                    'catalog': '=лS˔IЗ>ǜ¯ǶţНǊ^ДӆƝˑ`ʣȪMԤǺ(¨ΙƖΟʫ',
                    'message': 'ežԩӫ0ЀτȌŎÙƖѶԚûǇұĤжϓԃůҹǲԄǟē\x97ɩЩд',
                    'arguments': [
                            {
                                        'name': 'ΊΎδʆԍґŉ\u0380Ǜï@șʡɞƜˁɕϞϤȄ˒ó˯ʈʿҟɦҹЬ\x9b',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -943032752373449235,
                                                    },
                                    },
                            {
                                        'name': 'ÍåҒВ\x90ǊΛòʗɮςӽȅKΆżǙўϭûɋǹɉ\x97[ɯԊϬïӂ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4795741036092107625,
                                                    },
                                    },
                            {
                                        'name': '±ΕүΝԡƨ»ƯˆЫфӷȋсЛûč\xa0ҖĹѧʇӘԩǺǳʛŮҩʄ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7425213802679901682,
                                                                            -5493145477213723700,
                                                                            -6270307993933022450,
                                                                            6457773768337328122,
                                                                            2470450478303922744,
                                                                            -2233029450966836672,
                                                                            -8314352205558632918,
                                                                            8566301101457791852,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĠA§ҵҬɫÏ6ǭЙā&оǧŜǷɮєɷō˰ԌĩŖϾϙÅɻЄӳ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x8dԠўϰȻӹԅԁšŚ±UÊϿĻѺ¶ӝƍȇϬ˗ɜϔ҇ȷӭȷϤn',
                                                                            'ԇΙӡˎěͺŮªӟ˂Ӝ³ΖЀǂέˊhďĬӋ~Ûɪƕɍ\x81ʥīʜ',
                                                                            'ώԜƵĤȓǘйǮƕǷƙӊǋӠзŕюȠΝƍëȹśʂЬнÉЅæԕ',
                                                                            '˰˴QӦΕжďĨŇʥǕǅВȼʃǃŐλ?ӳpњɄCϸΙǢɊĿɻ',
                                                                            '¹ԛӭԢ\x98ƚӪԇΛīΈѱӐБѓΦΚȚͲSůӝȑФёƏϻˮVȘ',
                                                                            'YbԑĪӻtұʶxӎͳá\x92MϟKĻ иċÁŖцȻΥj\x93юϳҔ',
                                                                            '˾4ҍ˱ĳҪȏʄǥ"ӸɱʱɥЩѰэѮɱϼ҉ҟŝɄɺѽɐʨƏҟ',
                                                                            'ҡθҊќ\x9f8мƅ˟\x88ƠʒҸΔɗәģȺВ\x83ЛŨ¹ӍΔђԁЪ_х',
                                                                            'ԤѓƹԡǺʱԞѻŰĳOнȯϪԀԉѮƳϹΛˬʔϨƂʍǼεʺĦԔ',
                                                                            'ҡŻôҢƥΌӳɒɰȧ6љƽʮȷȌŦqǀњϨуяѲŭҳϏˣҶŁ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȎϽϺdȩƟČŞǼ`ƁӌyϷǣǊъҘʅ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҍ\xadŇʀºʬ\xa0;oԡɁѶҿȢĦԫɉλ;ȱIġ®Τ9Ҿ˙ǌțЧ',
                                                    },
                                    },
                            {
                                        'name': 'ãϻԮͽϠѮ»Ƙ°!\x8fΧ˰Ć@ԥΊԢŨҒϔҨӳτßюʣ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': '҃aǥȞˀϱȍϐƾРӚɁԭĕǮшŁĆɱχ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŬНíɕʝ˂ȵǹɹg0ӇĨǗӢʬʝűǄůŲ\x97Ӊ`˞Пӿ˾ϟÎ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԤңɊſƪѽѧμΞáɑҳRʰΤƍKkưʋʗǼƣ˯ŲԪѹѾϣȰ',
                                                    },
                                    },
                            {
                                        'name': 'ҭӅɣΑŤȵʌ¾ʔıθΓҒϊ\x94ŖȻѫѠ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212311.074538:+0000',
                                                                            '20210208:212311.074553:+0000',
                                                                            '20210208:212311.074560:+0000',
                                                                            '20210208:212311.074567:+0000',
                                                                            '20210208:212311.074572:+0000',
                                                                            '20210208:212311.074578:+0000',
                                                                            '20210208:212311.074584:+0000',
                                                                            '20210208:212311.074589:+0000',
                                                                            '20210208:212311.074594:+0000',
                                                                            '20210208:212311.074600:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ІиðǩvƄʡβԈVƤӸǶŒ\x9dƭ,ϩȿÒ˒˟ͺ*ÍБϵ_\x87ʠ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6975477752038680479,
                                                                            2845106653146285993,
                                                                            -8241054486665960476,
                                                                            906646240185703481,
                                                                            -6118465941542108104,
                                                                            8530469910224221979,
                                                                            8549647487311894293,
                                                                            789169586044926255,
                                                                            -3927644566363996824,
                                                                            -1046218133746255747,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Α˯ɤѝǯ˞˲зĜӃƵѠűȏǄŬŦԣĐѥѳÑʈԌŸÊѴˀѠА',
                    'message': 'Ɣˋӌ˒ΠqϯǷ˂ЃːɬʪɊϡīжŀȳ\x8cɭȑǹҕҲѪӄԝȸÅ',
                    'arguments': [
                            {
                                        'name': '\x8cőǞѻɩӺu,\x87Űƽή½Ҥ\u0383jͺͿţȅȔńûԦθӇŮ˚ψʇ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212311.075566:+0000',
                                                                            '20210208:212311.075580:+0000',
                                                                            '20210208:212311.075586:+0000',
                                                                            '20210208:212311.075591:+0000',
                                                                            '20210208:212311.075596:+0000',
                                                                            '20210208:212311.075601:+0000',
                                                                            '20210208:212311.075606:+0000',
                                                                            '20210208:212311.075611:+0000',
                                                                            '20210208:212311.075616:+0000',
                                                                            '20210208:212311.075621:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'SÞȁѲЃӠԞҞɛƵҾԚ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\xa0]ōĨхҽıԞԐ4ъ½¤ҍǥΐˬIrԌǸϗɳΏНΙǩʃԚѓ',
                                                                            'ʯŏЉƶϯӌӮɉªȖŽȑĩʪҬŪˢοƻЀ˘єϨҼѲȋʙ5\x85щ',
                                                                            'ɘͳҸϮћϫȁêǢŒÚʌ\x89ȪҍωʙšȘɼƞϏԞˤÖ˵λѨΎӉ',
                                                                            'ψɓə\u0383˵ӷFɴѬЪi͵ЏИȎЏԅɟϭǄúϰсϞΰńǟɓǐԃ',
                                                                            'ȫǻʌԜp¼ǙȝȡЮҟӹĻҞϜǇ¸ƷҦιÿ\x96ĺΘϠ\x99˸ƢΝe',
                                                                            'ҭԡӌȇұС,ɛӰǈĞІDӭɬӯËcωĠыjЛԐЁ˔/җōƌ',
                                                                            'ĦҲњòѨ<$ʹčɮД-Ɓ7Ф\x85ɔõȯРƖĒҢ\u038bОɸ\u03a2ʆоМ',
                                                                            '˥ĿЂźʑâΑӠӲèϪ\x86ƫ˔α\x84ǹįҸȾ\x83ʎͻԌƱμƃѸʟȒ',
                                                                            '˝ƝҦĨƭȀıǴμæƥÀėҠϔõŹȻŀȎ˲ΐәɝҳ҅ňmňű',
                                                                            '\x8bŦɳÊΚɖɤɴϊJεbǋƘ\u0380ɷӓ˵`˷ΜĂĊϾ\u0381ЙȁŖȖƪ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĲĻйĂ¡ϳљƳɐ~ɜϱĢӨėȆ\u0382;ǼʜѷǧǟĲҠõ°ƷÝă',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7685973265464155480,
                                                    },
                                    },
                            {
                                        'name': 'ɫÒĽQ«ԐđѮɬ\x9e\x8aŕѶƙ\u03a2ǤҵҫơƀӃʥÐӕΤ҃·fћʖ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƭ˟ɯɯÊ¤ȴƺĘɒɑźҀňȊϼӒɦΪˏöԍŮɬå\u0382ɜȻϫǰ',
                                                                            '˄˭_ԇȬãśϝłĬϬϴѶͻǨъǫԄԤԑƥӮ¯\x87˙Ǩζğ\\Ӎ',
                                                                            'О˟XҮόԝԡèȨӴǎ˪ëӭɕȑÄɠĘòїӹӵҰ\x90ɀ·ӓóŅ',
                                                                            '¢ĳӣțʟӝ¸œϓyǷ\x81ȽĴұʯ˃ңÉǙɸɣ_ȸǬǏŋ·Åю',
                                                                            '˧ȰѣǹåˠӶȩȏҔ$˟ɲʹǩҌǺјŢŁҦƈˆόӔŴŔƷȘș',
                                                                            'ўİZ*ōùҬɫɷȄZʋōɤ˦\x88ϊЈдԎП˥ЦǏˤ˻`ϻęƚ',
                                                                            'Lɉʃû³żɕΚĿmЂПʿðɀ$ċIǠӛŽПЧÁPЬǗϹſ˚',
                                                                            '#ӏ1ӨɏʃɤʝӹoиѲìɐΕɚšɁаԛûEʸҝ\x99ñѼÖ˴ɕ',
                                                                            'ȬϢԃΠǗ¿aЩ҅ЊС£ɶ˸ʆŔŸʽŦǒȁҪιΓԎȣӿҠў͵',
                                                                            'ęʜńȧ΄\xa0Şѓâа\u0380ӖˏbͶήӜʷЫƸi\x9bӗӌ¯ӋŪψεѿ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӯӎıƻЙԣӵ҅ƊϜϹҲЀ҃ǳѻ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -33238.016940798305,
                                                                            846312.3619519603,
                                                                            665578.2305275893,
                                                                            183529.5925794078,
                                                                            -86097.41959127845,
                                                                            81879.76412204132,
                                                                            -26857.58045198019,
                                                                            832763.2478842833,
                                                                            758934.4711374821,
                                                                            69286.73151611266,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˎě',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǻ˱˷v˙ѩ˂ҥԬԜκ\u0382ғēŎĴͷ˶ϩxҳ˓ıьΝƭȅ҄ыĤ',
                                                                            'ήŮ˩ˏ\x9cţƴЛӚӚì˳Ű÷Ϸуję\x88оӉŴƕа\x81\xa0ʹ˺ͷͱ',
                                                                            'ÊÜЈТơˁɣх˲\xa0ɺ˹ϑāь\x99Ś§ԟΊ˼ȫϰϮæхǃƺβŘ',
                                                                            'çJS[όOƩ˃Ȃǈ´ȟʶʵĚɞӍϿϵ˒ƟϕǈȦȗnǋ҅нž',
                                                                            'βʼҾęΙ˘ȉɫӣǭǞyŰȥήхǱ/ȴǾˉǬ!ӽɗӥæЯɆБ',
                                                                            'ʈ;Ǘàфʄ0Ϯ\u038d\u038dþŊɉϳԡɋŊȇѩFҢƠҰďh˷ȬύžȎ',
                                                                            'ɞѾ¡ȷđǎϻѻВДEŒ"ƞ¬ȫ\x8bѪdńғ\x93Ͻ$ȚʍΡԒԞʃ',
                                                                            '\x8fƪʌʵȁʥȹэtĜжй(&ÆяˌЍŌҧԩӎˌфЬϿҥЇӷӟ',
                                                                            '˹ȧǸτЛąЉлн_Еӳƚƺл\x86ɊҊʋϹʝнǆȹϐʼúȀĝƁ',
                                                                            'Јқ®ǵєõѫΗʐwѱʑѪđȵƄʣρȍʩÜ\x9cпɿËҷϚų»Ф',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '@ŹžĥѱΉ\x95ɺϪɠȔǴʪԕĝäɟγȡɐĝΣʺŷɝϻͰƝЧ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ǍϠɲΚ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ʀȩĵ҈ʗϠԢĎʎ;йҹĦϏŉѬӅ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 471447.42852005793,
                                                    },
                                    },
                            {
                                        'name': 'ĔИ˒Ǉ\x88УΧиϋĪʈԜΡѶɨ}ŵſČǇӘϦŪǟŒˏΏ҉ϑӼ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212311.078036:+0000',
                                                                            '20210208:212311.078048:+0000',
                                                                            '20210208:212311.078054:+0000',
                                                                            '20210208:212311.078059:+0000',
                                                                            '20210208:212311.078063:+0000',
                                                                            '20210208:212311.078068:+0000',
                                                                            '20210208:212311.078073:+0000',
                                                                            '20210208:212311.078078:+0000',
                                                                            '20210208:212311.078083:+0000',
                                                                            '20210208:212311.078088:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˞ԄƺĪȻϼԚҞтϼӹϲ˖ҽÏ3ΗѸưòȥàÍȽӣȊѓԜ¥Ϛ',
                    'message': 'ƃ˱ȈιÕšǙϲʎɨӌJԃ˭ѸǅđҬėʴϫʪƍʵˮɠȁзΎƭ',
                    'arguments': [
                            {
                                        'name': 'ҺǷăȝƘԭ8Ί˞Ȓ˛ϬA\x86ÈϨЛ«ЬӀԤɅѦήȋȧŎʡ¶ѻ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '\x8c)\x87UѻÆĩ˽]ԥ˽љ\x88źŘŚāʗ˛ȘҙЧςöDy˩Ͳʋƙ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8030874789098660507,
                                                    },
                                    },
                            {
                                        'name': 'ƁðΤєϦԙ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212311.079139:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÿсʼʸ(ƈŰ˱',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ΕɂΆΆy¼ҖЏƅɳҰΑǱêɋ\x82ԐÑѽǜϽšĆȂϲĩǱɢ҈Ν',
                                                                            'ț}ϝ˃ȌŹҪҠΦЇӇ˵цύӓԉÛѣɵ\u038dúК˞Qǚ\x86Zԣδӂ',
                                                                            'ʵɡΉƒȓ\x96ҥǡɨӌǠʿҎơӲӉ˫ӷҚ\x8fħ+ș˾\xa0żëͽɤô',
                                                                            'ԜŇэV.ϴԮӥŭɪȯȸљɿѥƩӉˮʛѫҵĆ½ΖԧīХǦ˂ƕ',
                                                                            'ˀȐуˌÐ҂ǘԔɻȝwˉȩƖ#ȝìгφ҉aΑгŗÁёýɃЄҋ',
                                                                            'ǶɲЦţҗ\x92űÍԮƈЎȍƘRʡϷÓǢҊÒÓŖц¯ǚÐÍsϠϢ',
                                                                            'ΤǞÕȴГýͰĖɷƲҫЖчʈ˅ƶӠԃЧ˕·˻ԑɛȕӁϝ°ïū',
                                                                            'ɰʺǷĦиʻФÚХŷԀӚǄ˭ԡԖĘԩϔȜΫɨʦԫ΄Ԏ˪χϜÐ',
                                                                            '@ͳ˴˥Â\x8bˢ¨ʫѣԫŰіǸ¡ӶԜψоǿͰ\x97ӅăӬǴǴΉӱӸ',
                                                                            'Ȼ˝ԪɜBѰ\u0379²őʩϤϝ˩ãʁМȵĂʋăАbŬџǆ]αԨʰȰ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǗɝʞƑͼĚɏςŶĒǬЙлęƆӧΕϴǰЉ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            390028.22239802196,
                                                                            604816.2749932356,
                                                                            831637.0838790429,
                                                                            488656.65208835574,
                                                                            866493.8691146588,
                                                                            184356.3998070237,
                                                                            499214.6999155395,
                                                                            124584.94177000786,
                                                                            858557.8265563025,
                                                                            -7308.94975049801,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʝƑǇǟΐßϯҧ¤ȬΙѢ\xadԀǙȰɫǘıҵ&ƴ@ƣʝƽȨҵҹa',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4595605935478126167,
                                                    },
                                    },
                            {
                                        'name': 'ưλʊǘӥĺ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            985990.5148486085,
                                                                            176876.6203904344,
                                                                            943355.8956316124,
                                                                            804805.4740427742,
                                                                            789149.1815563136,
                                                                            204677.3815208425,
                                                                            948770.8830696568,
                                                                            180348.28880229127,
                                                                            517246.2736601512,
                                                                            834969.3768516791,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɑϜɤ\x8eðáɢόǵȂ7;ϙӁĥҦɮѼfǻ\x82ŏӠԐŨĜȋMЅÌ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȑβәΨɝWӞėʓι\x9fĕʍφbНЊϙϨŀMĆëǰ2Úċһ˲ò',
                                                                            'ɲɃѢűԗ¤ĞoɓĂġЭǐɠɓʜѿʹÈήɰӖ҈¯þ\x8bĴƻǠɝ',
                                                                            'ȦɅӈĐŅԆӕµbřҜĒӶΤѲȤŀӃƸÑҞϔkÐΙйÓЏŐ҅',
                                                                            'ɵʌҩÿҷƢфjȸʽɰϫԜӴÛǧƖӣԗҰĞҐѭÅƹøѵϳʢǔ',
                                                                            'ǒɎʻčӼЂȺ\x85āı˩ӼСϷӃĥšя}Æ\\Ǽ˛˻ӄΡ˅ęЗӨ',
                                                                            'ǪȩŦǵˤÂɋŮ=ϰгԧɷ˕kąӻˍğΤҕƘҊʡμʙӆѸŚī',
                                                                            '˵ƝīŲˢδѨк´ΑͺǸʀШʶϞʃÖЖҶҸɛύȴ¼|ɜż/Ϻ',
                                                                            'ÃÝϒ\x9bÖÓȟӢ҆ˢУƁƴǈдԢƽδΩŢЇʩăŭɀ\u0380ǩ˭ĵL',
                                                                            'Ӱǲäˌ¯ʳʬƭ҉ьΦ\x9dʃԜŝΡӠϠ\\ʖBɄԦď˯ѧЦГsҗ',
                                                                            'ˠС\x9cњơ΅ȢǪɥӲNӧѢɩȎԠϬ\x8dƯȔ5ŮʸТȤΗҸԬĴϨ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŢзʏʙȺӕӯ˭ХPÜɱƨʳӌǝΪƺ˛ԫ^ӌԈҚζΧԕҁΔώ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3159345943404121333,
                                                    },
                                    },
                            {
                                        'name': 'ҌǷűĄҌäFѽҡɟҚĻ;ȝқŀʾЦЦG',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȳʈйѡƴȸǦɢϖʲƉÃϳ\u0380ŸГȶ"ʬȘԡƟҦđԆ÷] ĵð',
                                                                            "ôſȺɌҴǔэԌçԈςʥʠŠθʌÈǺ\x8fʭˋˌѮ'\x84Ԥ?ºƑϔ",
                                                                            '¹ƊǟʙƘĩǓō˄ӃсѕĒǏϩȬӜ*ÀˤҒɡ_ɡ*\x9bȅ#£ä',
                                                                            'pЁ\x88ΙĎ\x8dȝRϤɥΨƀƱѸ˅ņʕο\x86ıΉ˖ңϘϙǭ7˜ȐҐ',
                                                                            'қтƣǛӢοǦӟŵkȶźƓ˚жΎYɐԨćǰɛñ˄ôјΨ\x80ʂΟ',
                                                                            'ƞ}ѶԌϼԪĩ\x9bzϗȹБȾʈͶˮӂŏºүѲɀƌЮʱҕј\x8b²ȟ',
                                                                            'ͻƂľƈž¬ҷӭÒǏЫɬŔťЮŐ«ϫçӍЏѿϼΝŖˌŪǽʖǾ',
                                                                            '˕ǗөϷ\x8e\x85eнɜƫʩԓ\x8bљȇήӾȒЈқΦÛ\x8aÆ҄ҒeЂȘT',
                                                                            '҃ԝԆ˖ʓӤёöáˎçȃĳҾȳ`ӡYƜЎɎяıȊӞ˵ԕҳʺҽ',
                                                                            'ǽȆǲ\x8eԟϰѵĉԌȩҥǧSОӐϳÍţǳȒʴ!*ƱƨӥӏϺαԟ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƶΜl˔erVÆѺˇǶҪǞѯˀӔƗӪшʙǼԄφ˥¿ĹɕǛ˪ѡ',
                    'message': 'ĩǉªƙѮĻʭ*˂\xadǟíæǣ!Ɓ¢Ǽѥх\x8dҖϹ\x96ŎȕҟĿδˀ',
                    'arguments': [
                            {
                                        'name': 'ĪÔͻЗ˭ӻ҈ϾĂŻ~ͷԎ˫pʂӗŅɟņʪþɗ҂ӮˊŢ3ǋ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϮѷӣӼ\x99ʚĠsӛХǎƇӥ\u0383ȣˉĨӧʚϽÙяπϺфҫ°PōG',
                                                    },
                                    },
                            {
                                        'name': 'Οϭè˥Шʣ=ɭҝ҂\x83яʓҽěƭÄ«ρ˞ƝӐҘØΪȌͿӆѿƓ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            365767.77200381365,
                                                                            500496.45374361693,
                                                                            314882.4033939458,
                                                                            984693.6367281866,
                                                                            72447.13351607972,
                                                                            585948.9720097734,
                                                                            893249.6055561212,
                                                                            567870.6628662046,
                                                                            -93549.0011990837,
                                                                            215177.1807406284,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӄ˔JʎЬ\u038bӱȌPͷʓǪҸĆҤɵƈWΘɆʺz˙ȡԢԓԋМǚʈ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -41703.302066431155,
                                                    },
                                    },
                            {
                                        'name': 'ҹ\x93ΆXƯ±ʜ҅˙ţΉӷðұʡАƂӐZ|',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7681186681496980672,
                                                                            -6468003130460576590,
                                                                            -4934651867625347805,
                                                                            -369398700390924934,
                                                                            6563826248465989190,
                                                                            1634671158178918108,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԗȧ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5162422520045127728,
                                                    },
                                    },
                            {
                                        'name': ')ӼɓҿúrmɄŧŘ˽ԅȐͼVǞŖſ\x82VӏũѤȬϾĐӾ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǶɨӪÛωБ\x8dđǣԓҩԚǘŸǣʡʷҳ϶ǖÅ˓%ʺҬĆƱӛ\x90ѱ',
                                                                            'dѪȇϿ\x83ӏĽˋwеҜʕ2]ÐŌŮΡεñȑόѓù\u03a2ͿˇͼҬ/',
                                                                            'ƳZȠƈŘҨđδſѓѣύʸЏӞɞĎϱϨϲBҘӆ¹ȬȈ˰;ɐȸ',
                                                                            'Ί¸Ҋ¨ƒͳ΄¥Ɯʹΰя϶ӟEӞπ\u0380āϖӏɰӐQŃÞʋȦĦŉ',
                                                                            "˂\x87Ɏΰӣʕ\x80-˴Ĺƹ҇ɠĖȴƖ'#άƆĤοŻŰȍŗăʬA˒",
                                                                            'ÜǯәЋÌНʟȲʸѶѮЭȬǙʎϢЛĶʯҟ\x808ƩŏˮөԑǨї§',
                                                                            'ϕCȺĢęǧˮφ¹ʌ\u0378ȒγͽöȭӚǋȒϞSϬԏ˷¦ʳȻǩ˲ʅ',
                                                                            'ӧŸӜ,ɇ˲оʍѐȳҺѩÖƴˬ˸ˢđΚ˭ÑԀqŚĪŰˣԖ˗Ǖ',
                                                                            'ƊҭҰȯɓӬȰӦΆбÛɎȏ҅d½ʎӉɓмɅIˤſͻȂʰϷȺƼ',
                                                                            'ŧʋēҚˏôЯǡŶϪȘ\x97Ş¤\xa0ʜɴӆ˚ǃӆąʅѫǤϚøШӯɠ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϙάˀԗǃŪŇǰКȎŰƋДΌJͰ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǶѭǭϞıƦҌȅӔɄIpÏҾɉЀÉϝѠƧôöɂξϩρЯ˃ɶρ',
                                                                            'ѵĤʙΞʶΪɋȁfƄĖ҅ԙǵ%ˉҜѧʜʩӖƿɡлƝľǠƻƣɂ',
                                                                            'вèӅ®ĎЃƿ˽ήȷÙӈAτπț\xa0Ϳ\x99˜ĖǭȷӘϵʓ˕ΟԬч',
                                                                            '6φ~mľθɨ\xadԃҮȂĸºǊĒҎɱ\x84Һ\x86ҎϮѿĽҠҩйɅӴο',
                                                                            '^ŴʵčǿɽҐρəĽ˂ĕЧԊƗĕȌÐ=\xadƛĒѭˑύʨѐŻƍЛ',
                                                                            'ęÌŖӶѮǆČƣɠΠЪΘˇѦǅӎʣҿʇǀеȋ˶˵σΈǏФǧǴ',
                                                                            '˫īɝƈɀ¶Ӊ~Ӧβ¦ҍ&ϧѕВӡƂJтïˎ\u0378ȩѫаӚɟǨδ',
                                                                            'ЋDЍ˫*ԏƌˬҸд¾ѹϘɈɦԌҍԡÈˬҊķїӒӐP˜Ϻ²н',
                                                                            '˷Ԑ}_Ɔź0ɩԑЭԆȑCǤưjγWѢǩҒv\x98ǭƆ΄ԡԮåΨ',
                                                                            "\x8e\x8cѬυÃǂǿ˖ϞŐGя\x90ԛ'!ƞÚӊТЫâ\x91ьƉŰʹɒХѩ",
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ρ9ԂӶŎƕưϑӍoв˾Ĩb1ПĲϕ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212311.085519:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĖɌʋĵŃÖҐѾş_ǡǣlдԋЗƝɄ~çԬԘʅϞųҁЗƄԖ\x89',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212311.085676:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ͰàԢʸԞ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -359334293148226075,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѫʖD҇ɨʆŗ˨+Tôˋ\\ϟǇ',
                    'message': 'ұ¢ϮЉ\\ʙƦ\x84ӈ\u0382ϣǳƩƍӍŪКϠѢјґěίιΔєʞƚ¶ǧ',
                    'arguments': [
                            {
                                        'name': 'ϲɚУԒʄ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'JӒΊԑлȁȭéŴπѷӛҤЇ{"˽ӻњԋŵλʉȮƁͳȧʄqĊ',
                                                                            'ʋҪ}ҋsԃǑˏөҮαÖĿЙϡƏəѐΆϫ§ηɘΝǎѹӣuˉȈ',
                                                                            'ʤǬ7şʨА¤ЈζƤԍɒɎ\x8fûXʕʨшƔϣƥѭɛΤǳɹʴǭԃ',
                                                                            'ďÜхЬѼ˼WЏ҆ɚӸӶХҙqϛѨӤLɐɯкҪbӅɂ@ѾƆO',
                                                                            'Ƽˁ\x80XšКе\x95\u038dΝźŝȚњГ\x83Ƣц˰K˦ƖҾǥȬͿҕƛϘў',
                                                                            '±Ȩ¾ӈȏѺйӓǰʭ˩*ʰ\x80FɞαгĒġΞ˙ɧȫƟϦҨБƻԂ',
                                                                            '҆ΖķʙνEԪɇéõёĴşǖΉм¸[ϨͳōӦnЛrǙѲμǽ3',
                                                                            '«ØĮ҄ɛņˍǢԓýЦǌΌˈԢƥԎɯДΏÓùӋπΎʟϻϰЩϺ',
                                                                            'ɕĘЦȆĹђ˲ЋĲǖѶӑųӳхӋ˼ΥɗǋΖҥûϥӿ˟ӂӛԊŮ',
                                                                            "ÊɬҏщĵȭӸɋԣ'ŝVƶ\x80ƴɠʎĭӐĝƺ-\x88ǊπƭӫσVĨ",
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʃӤҫԇЬʏӄһ˛Ҳǐϓ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212311.086650:+0000',
                                                                            '20210208:212311.086664:+0000',
                                                                            '20210208:212311.086671:+0000',
                                                                            '20210208:212311.086677:+0000',
                                                                            '20210208:212311.086683:+0000',
                                                                            '20210208:212311.086688:+0000',
                                                                            '20210208:212311.086694:+0000',
                                                                            '20210208:212311.086699:+0000',
                                                                            '20210208:212311.086704:+0000',
                                                                            '20210208:212311.086710:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'íΣŅňŅЊƺЃУϟΤο˙ѵнÏŶʌӚΪҕȆÀӇƤϓ«Ȟҷɓ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -58331.720905546725,
                                                                            404168.6215254086,
                                                                            782205.8974562845,
                                                                            387541.42815928324,
                                                                            572550.8205868448,
                                                                            35814.739342112676,
                                                                            660132.4339606687,
                                                                            26089.994387530256,
                                                                            496360.9086836163,
                                                                            -93423.20825320395,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'БĠŤҊһӶŴѻѢԚЎ˒ԟƾ|ŵƃų\x97ɿԮ>¶ŒǓžƘǹŽ\x99',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8556506267780270716,
                                                                            4639244478460790248,
                                                                            -8013103422926254069,
                                                                            -6631106202444398755,
                                                                            -8928886465229485236,
                                                                            4245306217619583865,
                                                                            -1327031504715467001,
                                                                            5676896692049782706,
                                                                            8111555815986784363,
                                                                            -6263453816502822043,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˧Πň',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'φˣɞѳӻӳζĚ˘ÍOǡԘZNźΟƣɢѢҡ\u038dφ:ƿ0ĕɚԉʍ',
                                                                            'чǼƠϫσқҙоʷwáЇʜƣȾɡÛζ\x8dGţϫ҆ғԂĊ҄ȬǳĤ',
                                                                            'ΧћѧƔӌΞȷĝгÑΚÕµ1\x9cɝʢ¢mϬԈǐɎȨƬŉ¶Бοř',
                                                                            'ǚÝˡѸǵŢ˫ићШХ\x88ɴľÝѢҿΞȟɖüϜ\x8cȽԎԭʳЛȤʳ',
                                                                            'ŲĪΣӎ3Ņ\u0383ԃŁʮԠǖɹ˚hͽǷ:ӨўʉɭnԚ;ĥϼҤĭм',
                                                                            "ωԘȯ҄ĆƗ'Ȱ3ʒНȨɼФȊŪŕ>ÓȟеʃγɢʺП\x98\x82ͻß",
                                                                            'ҀΥԧÝĤɁ϶џŬ\x8d0ɬ&ɴƶӲѦϓŹϏȶѧӄСԥϷ@Ͷ҅î',
                                                                            'Ìɤèѵ°ϥ{-ҞξƯɚΙŋǌҬÖкǄ²łИʲ\x86+ѓďhұҶ',
                                                                            'Эǽƣ¾И\u0380eёѤˋљ҂ҊĦЬαԦ϶ǩȢгшªɷҰʣЕ˶ɕϽ',
                                                                            'Ńȿʠ˸ǻ;ƛЊҌǪ\u038bŁ\x99ДԘҒʐÈӼƔäȬƃ\x96ɬʥbԌϠί',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8dɐȷЏҏĒ\x93ʙ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212311.087952:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȥŗʔϝ˦ӂʖͼưԣҒ\u0378½˙ˍʉХŎӭʋD˒6Ң',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ɵ\u038bŎɭGƣлĠҷҺѶɶȕԞʖȇóЗШă\x94ŽнОǵĔǨG7Т',
                                                    },
                                    },
                            {
                                        'name': 'ϼ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 612294.0279844955,
                                                    },
                                    },
                            {
                                        'name': 'ѬƇɠάϢȮрҘιХéЮϫԆƫϊϕ»',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 16788.845578461638,
                                                    },
                                    },
                            {
                                        'name': 'ЌŞѴȒżӼǸ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʷƮʭĦƎЃĤŋȷƽk˷ȥ´кӀϏμԥҙ΅tΠƋɩЭĜĞƹĖ',
                    'message': '`ϩʸ\x8eΛвėȂʌ>ԧˍºҤͻιυѬѭ»ӔʯͿMΖ>·˨Źә',
                    'arguments': [
                            {
                                        'name': 'ϝʡҍɥN\x8dȵЀʝds±ƯʦƦê˻˾ѳļεҟǘМ¶˜',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            689431.3487394628,
                                                                            813407.2374473608,
                                                                            416675.99711967434,
                                                                            805548.6011923867,
                                                                            220628.74188999657,
                                                                            484536.7667260107,
                                                                            329199.7503933357,
                                                                            673891.8023285519,
                                                                            558625.1836002944,
                                                                            -52834.151213237645,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɭ²ʱćʮè˒ϤʸӯĖѷʸ|E\x9fȑ|ʳЋyΙȏȽ^ƈnɛƖϲ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ЪӸǬµǩĬјȌøįȌҥϸ3͵ҋ7ьŌɜˈҌҕ\x92Ϛèă\x87ǩϐ',
                                                                            'ӿ@ιƐĚβÛƭʉcŃǄʡÍ¦åƇѓѿɥςÖʫҦĹƐ¾Δҝʈ',
                                                                            'ˇԟŁЃʀӰŮ£ǰлZƋç8ɖĭɦ²ЛʰģфzʆđϛŮʄԡô',
                                                                            'ʞЪ\x94ӘɧΎǘΦJ¯ȗВɠϵ\x90ζʷDɮɤ,ȬѧЮÍԊӆŏѴĦ',
                                                                            'ϐǑ_άȐǁ˫ÇϔϾϔvҺ҈Ѕ\x82ΝΚ\x92Ӷǅ\x7fђHμɹ[ϗªġ',
                                                                            '˓ĪЗćϪ¡ˣ«Ÿµʨӟƿ˱ʫ\x93ÎэEԙΔрѸʸѡԚеӢʣȦ',
                                                                            'ƙʸƄĴԂҿюӆВɨтɝ\x91ǽѓӧǵǆȚȟŸ\x89BƖ҆Qˁűəǵ',
                                                                            'м#ŖӫψԔϊǥ%͵ѷɍ.έǦ·ӷħӺȞлʦÂȻʒʽӀōЏʧ',
                                                                            'уЕХ˨˴ϞΈЋ4Ԕs\x8fҍ˩țCǊįӦДüҟЎ¾ɒŒƗǊӆд',
                                                                            'Ǔȱ#ŬʟɎŽɱBʱӁ\u0378ĤǐÝƂԎOϩˡӃC/ОԫѹθԊΎТ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8d·/D©ѸʭϨ!ЪӁϫˁśƦҥϸ_UȻΠΦр^ǜҨǲ˶Ȣ\x91',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            916399.3928443181,
                                                                            879589.8479441149,
                                                                            -44422.693223770926,
                                                                            645728.561371988,
                                                                            545321.0438137206,
                                                                            912963.1288755116,
                                                                            879660.85009726,
                                                                            702424.999687231,
                                                                            585658.542795147,
                                                                            294433.17623935046,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': ' Ʊ˓ưɼķ',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŉȸҴ\x8fĜ\u03a2',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4540481095059102784,
                                                    },
                                    },
                            {
                                        'name': 'ҎР,ÏƪQƌĸюϛӶһˉғӃΒǾȚͼÌΥĠŒM£Ӟː}Ͷπ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1861878479229712283,
                                                    },
                                    },
                            {
                                        'name': 'ȾŦԉώҸɑɆőЇ҇ɉǭӇƄӸĠҾąͳŢʽɍǈėj!ВɕϠ˻',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5755462812546932419,
                                                    },
                                    },
                            {
                                        'name': '҆ęãˇԩ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӐҠŷ˼ÜǒɬѡY\x9aѻΣ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 325524336538835546,
                                                    },
                                    },
                            {
                                        'name': 'ŚĔůѢ\x8aЗϦΓλԄԀÉъŘʄųʥ΄',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
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
                        ],
                },
                {
                    'catalog': '9ƐӺȁ˔ĦȲ¾τŖĚеÑǁŔāǏƣԫѶҵĶѣԥьӔ\x8fƩȁŪ',
                    'message': '˞λaħæɮ˳˰˅L˘JƦęƧëԍɟгȌϭІщӈƜq,ýƜӱ',
                    'arguments': [
                            {
                                        'name': 'ȝĦŨÌɵȝ˥ҺЭùìѸ\x80˵ˏʍϚ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'цȋʕlɔʣѸâĬѹ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ψðӶΪπh˒αɨʊЈÝΌЇҘǁϒĸNӞǈ˲ȅŏѶԄϺǷˆ%',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212311.091805:+0000',
                                                                            '20210208:212311.091818:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ŗǁ˃Ї\x89љɸ×ð´\u0381ȕ\xadõVĥβ\xadÑϚʓϙ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ñ\x9dʍ(ƢǞıѠїԪΓǫĬɺӼϥɟӍŽɰЗрsѹӃʀΉgĪԘ',
                                                    },
                                    },
                            {
                                        'name': 'ĦǛȄĳɡŷŕʐȿzɜМđśĆѴѱòÿԭǗƂǩ&Ǭǹªͺƿ{',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'г\x7fκÕdóˤ˖Ňġγ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            685381.5102249831,
                                                                            326035.7966396635,
                                                                            742633.9960042932,
                                                                            557129.1528961275,
                                                                            17958.480613044012,
                                                                            468660.52050720423,
                                                                            50578.3592025399,
                                                                            431227.99238677847,
                                                                            189112.7649114682,
                                                                            560031.2909409654,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǧŎĒέ\x87ίΨӅƽ9',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            79509.3038803038,
                                                                            858856.5362412889,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȅеӳ®?ʃӭЂʑQˍɣƯȱҦςȶˊЊɖɬšŜόȒ˯!\x8bêʏ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            857590.4873534491,
                                                                            382425.77016748517,
                                                                            827818.677939692,
                                                                            919083.527076173,
                                                                            554811.6361060878,
                                                                            -30791.63519733172,
                                                                            627701.8505835055,
                                                                            63435.00005307494,
                                                                            786050.3531482727,
                                                                            -75910.00577732484,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɓŰѢӫсȘπşϞƬɤǮaƨ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 191148.44969761436,
                                                    },
                                    },
                            {
                                        'name': 'Çʕ\u0380Ҩ4ǸëʨĎʃҲq3ˆͿԁβӧϰΣҲμψǂǣ˛ӬͶϲͺ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŒŶŃŧѡĽ˰ͲãˋĮɉ\x9dґѼĴʞɸɸѿѵ˒҃ʶĆɫӷʑřĀ',
                    'message': 'ʡԖˋϡͻԝ҆ȑƪi\\Ǡ4ҿƣ϶Ш˚ѻlβѲϱΪĪBĀŰ\x94Ë',
                    'arguments': [
                            {
                                        'name': 'ȿê',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ķ·ÆvØΕиόÊƷ\x91Ҕƕ˹o\x83ϟȑћjǫҫőҘˤÝǬҐЇѠ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x86ƍǷӴҸrюȐΜыџҎңĨàΞǭѬʳΉЧǾ\x9bʥʪΊ˯ЂF\x9e',
                                                                            'ƓŸëƛ˸ʚƩƩѢ˾èĀ¯Ȟƍ͵Ųȋ҅Ǣѵưģ҅\x9eúÍÞȵȪ',
                                                                            'ɠЛ6ӝӚΊ\u03a2ǯϜΓҦјӿȁĦЅїӻǻ²ƐǧˎĵȓɏkŌхŸ',
                                                                            "θьfԐ˾ӋӸǆɀƌԅ҈ƺĉĽ'Ҿм҆\x86ҧԉņƄ\x9a˪ӁОλ>",
                                                                            'Ŏ*ςϩȒҵӴƏүGϊ¶˂ϻНˊΙ*ďѠӐ¬ϕȕȘΝ!ɲѫρ',
                                                                            'ƟæɔǻűԈɛ\x94<þ7҅ÕГŁӚϾљєǇІЄqɝǞɱ҉ҍԍÑ',
                                                                            'ÆԀɒ¨њԬȓăǂοˌτȿɁƹĊӽɅƈƇƹЃʸ\u0380aÎ%ƤΝǛ',
                                                                            'Ǵ%ɀ£ȶɒͻęрɂxúҏΏçϊ«˄ĥŊҁÉќĄäюˇɎԜQ',
                                                                            '˗ғʙϝǂŎȀǟȤȹ˂ƓŃˆЇƝͳб4ͱϽĘƘđż"ŅϻŰӏ',
                                                                            'þͷǘÐǜ˨ȝȟƩǡύѬԄҀӿеѣԜӟŃҿɠѓύǝӆFԫʉ҃',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ζǇѤnFŃɛÁąŞϦǝ˄˥ÎøŃǢΦǚ˅ʈ`ȵҙǒԭϝơ@',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѴѭȐȒЄоşΧŭĪΪţҟ҉ưǩ\u0382~σ\x99ϟɏүёȗÛÇӘӹχ',
                                                                            '\x96ɇψҪɋĪ¿ƪοүϣͽӗȖ1ȡęÙǨ*ͼǾΘ\x9arƍњɞҢʳ',
                                                                            'ϵǲҜ\x8eǹʃΞ8©ʕqԣԂÇјοϒ˱ХӣƜоːĝιìҙ˫þļ',
                                                                            'ϖ\x7fÚ¤ĪиԙͱʆòǕɄцώʃȮġ9ΎҫϸҞϢӧőƢ¨ԥӭŠ',
                                                                            'Ԋ˧ǡѨ\u0383ǭçìǓѣҏԢϊԗƁӉĤóӼƝșƶFɜӬԠă\x8dÕԬ',
                                                                            'ͷѥgʎ˭ɃʉЪϚȴrƉʾĲˍɄƎmӣʕƯҥҮџÜȼʽ\x99źΉ',
                                                                            'ЯćќоѳԢιňóҁť$[ҡʌPyǯҴŢŦéė´ʦ\u0379ŬƆ˯˵',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϸÞʒƂȆѡ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 814258.2912558494,
                                                    },
                                    },
                            {
                                        'name': 'ȜǵǒжϑPүҋρϵ˦ǈˤǋ˅ѬѨоʩӃӔʥΈ˾Őνÿϓ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212311.095606:+0000',
                                                                            '20210208:212311.095630:+0000',
                                                                            '20210208:212311.095635:+0000',
                                                                            '20210208:212311.095640:+0000',
                                                                            '20210208:212311.095645:+0000',
                                                                            '20210208:212311.095649:+0000',
                                                                            '20210208:212311.095654:+0000',
                                                                            '20210208:212311.095659:+0000',
                                                                            '20210208:212311.095663:+0000',
                                                                            '20210208:212311.095668:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŪlȏǉїȤРԔʨƥ\xa0˫ǕӑʚíǤҊ£ѓĘєΖȓȞʅѣǅˍѣ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϛɽȝŞȶ΅ĩЯçЧźȶщӡ\x9fӿҽԋ\x8e\x8dԔԋȽКȿΈдƤ˺ˣ',
                                                                            'ɡӖƧĹȱЌȀ^ˇ\x8c˗Ǎьʩǜţ ˡϥȖϮ\x80ǺϚɸκЖǂÔκ',
                                                                            'ҿūǵʊӚŅΤ˹ұ\x8dӺǫƍĲǸњӗ˚ƄѤаҌPѨŉҔʲȨƂŨ',
                                                                            'ϒøτƌΐёԟɦԦΦ¶˚VĲӠˉŞƁο˫ƛł\x8eȖҒĽƞɘʵϘ',
                                                                            'уŠӠ4ːʸ˕ĀӅɸ\u0382ó£8ɹ©ѨΡȀɖ\x83τǧÁϚΰɂƵ\x93·',
                                                                            'νŕϫӅԫƗ¡ơĬӉǂżҳźwɹёȽʹԀӒʡƦыͲBĕɈɛЩ',
                                                                            'q¸z˄üДй\x9dƥ.ȄiҮѧƯʤԪǷĸѤΞͱϷЄĝҟȟѨÜБ',
                                                                            'âӇǒ³\u038dǀТԒ«ЭƈǽNʀɖύ\u0378=\u0379ËȄӱɀȵәˁʊњ\u0381Ƙ',
                                                                            'ҡƗђкŠіǎЁԂ\x80ԤѼҮƴȑǆʡ\xa0ΟŪϷҟÐˋx҉ƮЍѨχ',
                                                                            'ҭШԒĲʘÐǋȒǎǖê˥Ĝ\x9dРκɣǪϸƓΑҺѸȄИ\x97άȳΊª',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɟеҭӞӛхʣǞ\x9b˹ƫ>πʔ®ԭȒȧ¸FӾѕ;ЯʠЄǝҧŉ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212311.096347:+0000',
                                                                            '20210208:212311.096358:+0000',
                                                                            '20210208:212311.096364:+0000',
                                                                            '20210208:212311.096369:+0000',
                                                                            '20210208:212311.096374:+0000',
                                                                            '20210208:212311.096379:+0000',
                                                                            '20210208:212311.096384:+0000',
                                                                            '20210208:212311.096388:+0000',
                                                                            '20210208:212311.096393:+0000',
                                                                            '20210208:212311.096397:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĺǻÃϲ\x8a[ԍƑͲʌПϩȹǘſ\x8fºǮҕɾùȢӮĈðȧ˭ŜȢЍ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            333900801740896523,
                                                                            -5197776826077102002,
                                                                            -686749412257148918,
                                                                            2806162289693747121,
                                                                            7286106794238281840,
                                                                            -5309584434487836810,
                                                                            1367165551614525300,
                                                                            -7241872369486278318,
                                                                            7556789314853976650,
                                                                            6836997358771571570,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ɓú΄ŸѬӵ§ʖƱό˟ϺăʵȋÎĿғȜQÈƨ΄Á',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212311.096906:+0000',
                                                                            '20210208:212311.096915:+0000',
                                                                            '20210208:212311.096921:+0000',
                                                                            '20210208:212311.096926:+0000',
                                                                            '20210208:212311.096930:+0000',
                                                                            '20210208:212311.096935:+0000',
                                                                            '20210208:212311.096940:+0000',
                                                                            '20210208:212311.096945:+0000',
                                                                            '20210208:212311.096949:+0000',
                                                                            '20210208:212311.096954:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƎƦԬҌÈʟҁӪǝɡÎøНʗņ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '¾οГq\u0379ǾҳȖц@ϣƦĳ҈ŹлΥƻò¿ŢůʅźʕšǡЉчð',
                    'message': 'Ǝτ\x9fЛƢʳҗϵˤԞйŒǠƣĊūӮ8$гMȝǳŭGТɿϙԐǿ',
                    'arguments': [
                            {
                                        'name': 'ҫɋʖ˅˲p˙\xa0Ȧ\x8d\x9aº˃ƘђǶǞȃžİšЬӧΈҍ\u0381\x8dϴҘ\x8b',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212311.097665:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ļĿӇťŉǫϞʺIѵ;ϟɴŵ˼˝ȣΰŲөѶƆƥ¥ϣÁȦρͶн',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '4¢Ыŧјіûƛщϩò ƀ˦ŪΜԮzÙʲΕŮТϪƲOԆыĲŔ',
                                                    },
                                    },
                            {
                                        'name': 'jǺ.щɗкɅ\x98ФΈōзĔҞ¼üľҶƴǛŽȡЃӖʮõWZÿ;',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϡéÀųҁƭξΔԝǽ˃ƠӰȜʛήƤЁћɩϟҪԌѥҸϊʤǗǊķ',
                                                                            '˂âԞǊğbȶɬ95Ċо\x8f˨ђ\x9bξϜι"°ĭÞѭѧŘʤɛԠΚ',
                                                                            '2÷ПǺĚϿЅϽÝϜȀӄbǀªDϿ˒ȯ´ɬiΚɓɄҗÝ4ñΒ',
                                                                            'ŷνȻӑǯ¹ԅǣТώы\x9dџƿÞҶГӼϪԃǑŗѷήҭǦӘԌ\x8b¾',
                                                                            'ˬ>tǬŝȑĠӞԒǝǥƖɃFƝјȭӆ϶ʹ3҇\u0378ĸЙəČƐʦß',
                                                                            '\x92ˬӆbĹŏʈ҃ĂŖĖɮǝj҆\x85ȇŸǗɉȒɹ\u0382ӧĊǼζџɜ\x91',
                                                                            'Ǯ\\Ⱥ˶ɠͷԁʹӘɥǂѰ,ȤзǽũȎаƚԁдǳ·˼Ȇ,ǏԡW',
                                                                            'ƤҲƇȭĤʬɂįioÒȢӭѫɡηơɚ÷ϛѨÀώ˸ȫ\x9aĢНGĲ',
                                                                            'ʄǒǁ\x87ѩӥ\x82ЈЙѺˬϰȿǎ˪ҨƾҔƻʓƩҢιԨʍŚ\x9f҈Ѓʊ',
                                                                            'фϖʃΤӱˑсD˂җɾīѯǊΉƑɵƃĵФ\x88ƌȶ¦[ƪ\x93ɢϙΌ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'N²Þ¢ѯˬ³Ǵż(ї\x8bЧЕî˜',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2519168719407182255,
                                                                            8669793297730620127,
                                                                            -4624685672033842944,
                                                                            -3613829250539284655,
                                                                            6863017194307446557,
                                                                            64086509813405281,
                                                                            -58240219257049992,
                                                                            -3240966690042330713,
                                                                            -4979171104754950888,
                                                                            -7460126100900103537,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϵ˒Ѣ˾ɊԖ\x7fǹϪԕɆήưȫУϱȔʾ˝-ɔ¾Ғ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϨӠΕӐÂ˒Ŗ=ϹǻѸѧιʠΠÖˢʀÿ÷˴ҐĕƑĲ\x95ƥӊƔɐ',
                                                    },
                                    },
                            {
                                        'name': 'ʸóûȬκҺѹ£ŐəɗҕƛΎǘŢɚÍGЍʉӜѸҩԩӖ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2251368264875016030,
                                                                            -4554934426154604723,
                                                                            8703602422862108398,
                                                                            -3259115841798985963,
                                                                            -5830352244003800247,
                                                                            6262467142750133287,
                                                                            -8999520145721865689,
                                                                            7719233805555576640,
                                                                            4643196154104422268,
                                                                            -4074436262892186003,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˻ƕѡǺ*ϥеǮʌҤѝȂ˷Ƃ˘îϴԁřKϝ\x95ĎɶѭĎūŕ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6612362032516353329,
                                                                            -739246233014262185,
                                                                            1384760377878543022,
                                                                            -6449651412924983789,
                                                                            6495576978092514055,
                                                                            7207449350331785608,
                                                                            -2992979802814871297,
                                                                            -5039970842078651778,
                                                                            -3451376727844560174,
                                                                            972339443196067728,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ǷѬ\x8fРǙŕƱƔ'ЂԃЄԂӔӬ",
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            785026.3118104298,
                                                                            676796.9765835836,
                                                                            407986.62076377275,
                                                                            465761.55136130785,
                                                                            -85766.17885984022,
                                                                            958294.6356602313,
                                                                            758973.5076297586,
                                                                            646064.3646533418,
                                                                            723378.6742385785,
                                                                            654260.9532400358,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĺӾʕȂУ\x9dķ\x9bãˀǟʍĉOΰϣ\x86ψǾþ\x84ϬǷǡԍ\x8aåϪϲœ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212311.099585:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ţ\x8dҢ^ęRʄ´Şӌи',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԬĹѽƖλӭ\x99ͼǵΛȿρņȉϧƮ\x93ƍĄђ¿źxR\x9cɏʰɜ)â',
                    'message': 'ѓǲ/ΝѴ@ǟҿъĊÍåς@ʰЙìςąӿ¶jȅʻʪӇ˕ȩϷμ',
                    'arguments': [
                            {
                                        'name': 'Üʴţ\u0378ЈǊʋrӲлǋҁŠЏҷ˒Ԏʹ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȵԧˋńưӏɀΣ˷Ϟȁԇ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            887030.7358701669,
                                                                            975774.9800464748,
                                                                            499976.7680161181,
                                                                            897286.6296067175,
                                                                            632021.5884229701,
                                                                            945591.4112847374,
                                                                            652806.9683415692,
                                                                            538006.8780393373,
                                                                            923355.0890079839,
                                                                            -76385.08460302174,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƢҟÈÊɅΝĬ¬˫ɜŴϘӵҭĎŢʱ˨ǫSԔȪχГŽɦ\x95Łžx',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ĩ[ԏʛ˙ҙ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˓ŅɺσŰԖÁƻ\x90@αԍ=˾ӲVɳ\xa0˾ҾКɞΚӷ(5ÈǛ_ԏ',
                                                    },
                                    },
                            {
                                        'name': 'ǾʫҳԌĘϠҸʭyɖӻέßΉЯɱә\xadǍȟʶЁʆŞӦЭĢԉԫ¾',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            304368.34106696997,
                                                                            677037.1554389857,
                                                                            316264.49084764416,
                                                                            631100.2623077792,
                                                                            529397.1206313464,
                                                                            -7848.379882519599,
                                                                            597053.1298730487,
                                                                            927803.8814321653,
                                                                            235825.4691402777,
                                                                            374226.9061154995,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ů:ΏƏҤђ˅ɀҘŶʹЪj¡Ϯʫ\x88ˑȅˀTUɼƻLϏʹQİ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 329303.45502362045,
                                                    },
                                    },
                            {
                                        'name': 'хɼǦїÆşп\xa0¦ǟӳʼ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            739240.2839523245,
                                                                            265242.0970268258,
                                                                            -33112.990655842674,
                                                                            495295.0785136949,
                                                                            558010.8782025191,
                                                                            908678.2348367934,
                                                                            20326.584341192924,
                                                                            260881.46797705616,
                                                                            748342.3800105404,
                                                                            822949.6858235276,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƕњ҈ȋƊʛÈˊˑ\x82)ʖӃğ\x96g˳àрŀҧƜąʑƆÁӸіāѶ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ңι¸γӵ\x8eӃӸĵSť\x99\x9aƩƂǙŭҐԅѧԜԘ¤Ǜ˥ҕΧɨӨɛ',
                                                                            'ÿЅÜɹ˘Οҋ7&ċьǏÐƦğÎ\u038dΓ˲˫ƧÒ\u038dɧȉ?ŶƏщ˵',
                                                                            'ŐǗӟIʭ¹ȖǂɠʿŜ˞Ӳ҄үǫŕǾ´Ƥß¦ƀū\x83Ƒʈ;ȯÑ',
                                                                            'ȊéχɐɏūvԨͷʰˇЉŇʴԋΨYҊłϏȚ¿ХҊȳϬ\u0378ŞҐϗ',
                                                                            'ӏƋˍòʻӗӜξpñʐ\x81ԂЌ\u03a2Ť0ı˗Ԏ˼ЊϾӔ"ʙжҴҮϰ',
                                                                            'G˯ХҤ§ʋӲиɛǷ\u0383˕ΆоуԫӌϱйҒ~ȔΜ_ГƕȄőʮǜ',
                                                                            'ϠС\x8aP»GкěβǡΕÚBǦΙȻЪˍǨǰʟӫќҤ\x90Ń˺?ȯѺ',
                                                                            'ʴќɞʺėλŐԅƊBеˇѽȃ#ȯ\x9e£ȷfǦ˳ćPȺþӵИɡɩ',
                                                                            'Ϙόӕѻɴȣ]ϣρ˴щeҕӍтͲ¤и±εѦҪ˨ԁýʔƱЛǐϧ',
                                                                            'ʢВЧͼĽ˯ƸѯRСɀÊʅѦt˲Ӫy¼ɴ¦ÉçĽʙрԥРʯĎ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĂTΘ¿ʲϻÏ˱ԦȺÁģǫԒŎгЂΆͺǤıcԝaBŢϨ«ӯҀ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '\u0380Ɇtσ¦Ԫ҇ʨ˶²ɟɃʾȻʾǭĕ×ԎΰӒѪũʛÎ4ҦĨɛҴ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8124405916725472113,
                                                    },
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'Вϰӥ˹C',

            'categories': [
                'access-restriction',
            ],

            'messages': [
                {
                    'catalog': 'mԫ',
                    'message': '"',
                },
            ],

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
            'name': '\x92ԧ˻ƯũϰɠҳВŝĉɑ¿ͽęŞǡˀ˞ӺŘĝʃѿĽЬ',
            'error': {
                'identifier': 'ԅm҃HѮίФѧҠˣƷŽŋɭ϶¢Ԛʹͼ\u0380ʭӬЪέƠʮƕÀ9ҏ',
                'categories': [
                    'os',
                    'invalid-user-action',
                    'os',
                    'invalid-user-action',
                    'network',
                    'access-restriction',
                    'invalid-user-action',
                    'network',
                    'file',
                    'os',
                ],
                'source': 'Ӑ5¾ͻȄřϐЭŅӟˏŧĭ»Îɮ)ʆɬɵŢ\x84ʾœʃй˭ӊШȡ',
                'messages': [
                    {
                            'catalog': '\x7f½ͻɦ\x8fйŅüȼƴͽ\x93\u0380\x99ӗJǑԤҚ\x89ľɰЁţҽƠũʗǬq',
                            'message': 'ɔʥԕҿεAȂѦĄ\x9fҾǍâ˧ӎЦMȤҟɲԍɹҷȨǜʳeɬvԈ',
                            'arguments': [
                                        {
                                                        'name': 'ʧϧϜӋɷσ˄ԮĹϢƝǀl!ƶȿѪˇΎΟ\xadƆӑȁ˽Qļ¤țЪ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҧ˖ҩąƳɱτˬϴ˥Ұˏ\x7fӭɓ#ÛҔɡ`ԉөͺіԈ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ůĥ\x98ԡ˟хήɂjȶϸҵôͺα˅ӡʺÎɝ%Ѫ%҈lǹ\x95ʞ\x86P',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '½АҼ,ӲВˣʡѠӹ˾\x97\x9cҧĎkÂӱɟÎɟԕƬ˓',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ʸвɿ'ȉ)»eϦıʮ²˽҅Zƺάs\x99ВƐɥэǸΓƃþȵ,ĉ",
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8eг҂ӐHӡʸŝȝvŘˍƹɜѷŦȺЎ҉Y_Ѿζӕˆəλ\x8cǚȯ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ώϖͰˍѷ\u0383ϋ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ұѻɊԗǲ\u0381ЌˆňYŶˬ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɝϐ\x82ѠÕPєµ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʬѲ±ţǞɈъąб\x80ț\x96ʝӨѥΊ\x99ÝéӁѵčƯˠƵӾŲʲѬˮ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'þǷӓəùњ҇ɚɉä˲ɯҤáϑљЮĥ6ϯÙÓHϵǡЀӬҕǑ:',
                            'message': 'ҭ˱јƮİҋʫʸˣшǫ\u0380ҁԀˌΰӎĐ\x81ѱnFϱW\x9dǒ§û·ƻ',
                            'arguments': [
                                        {
                                                        'name': 'aϼɤʈ\x95эǗбϞȦԛÀɜʶϸĨʐȐƛΫĹƷ%ң˟ħʋχ҈ǜ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǎͼŽļӈšϽФȾ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʧćȜʐ§±ϠǿЄċŅкbǓoǻãqБѦĹtɑ)§\u0379ʏ`ˌҩ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȅιƛͼαǮҕř˅§ĜˇдͶɦǴ\x83ļɋ=ξљŝǶҥ\u0378ӞǍʈ˭',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6446815355013720666,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʰǃϕĳźÝÞњ҄ΰźšù\x92ɧ\x88ǐӥʶѩÔĤʅЄ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŢċǺıkĴ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǽ@Ǹŏđ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĵϩЧ˧ԫ\x97ҔIԁıȯȜӺǇǆϬĽύƎϐɳǁ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '§ä7ƿͼӄҤɃķʞǸƀѶȐҵ˦ӸԖ˹АǙӁȕʋӀĦĕɭϬԣ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u038b\u03a2ϘŠ;ӇɼӁʴɒ\u0379÷\x9fϾĊłęɃ\x96ÝЫҽϙÒњӞѬ¼ϾӪ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "g\\6ÖԏǳǪǀРŏ,wЧ;ƘǓʣɍԓ˝Ӛǌ'fГӫҖɷΖӉ",
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\u038dƉʹưŢʡӫ\\ďκǙƎ#ȥʤϓ\x88тĸП8ÜʅĖɤñʍϠѢȹ',
                            'message': 'ΦĝǠҏƗϽ\x8a\x8dˑ¡±єƌÐѱѿʣǾʒӱÿǸāɑ҉ƇHԙůu',
                            'arguments': [
                                        {
                                                        'name': '˼ϟҎVŅ\x83ҽσӒĢδ%ɠ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'łӬŴÒ±ıfɮҾǌκǋЩӡǪϹ`òę҃ˀ˪ΊɿԑүiƒϷȲ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɵɝ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϪČνʩ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'җȝѴĮΒɿϗϾƖrέȋϤƢŮϣѾԒÁζӷĶǀǽԢҗ,ĘĳƧ',
                                                                        },
                                                    },
                                        {
                                                        'name': '˄ˋΠƵ·ƄǥρƽʻµЍЩʃʣŽʝƌʉAϊñłΗњϹԭşӨȎ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'әā±eиôʐǼàιˬğĜɛ\u0380îіѲԊҸĕĝлҍʕǲεЧ²ǘ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ђȯȖǭɰхҨӌ·υηӾ\x85ϜʄԉÉǥΧɄҏǊJӲǌ\x96ƃƍҷŨ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4234150216076992764,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЯͿƹêǎͶ(ȫ¥ȷ¦yȶʅБǟÕ˕e',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '½ƓΜßzȝƁԑmƷ¡ϳƊŮ˫р,щŖӈțӨ+òӊʯ4',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӈ¿"',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɁϭxʹʳӑǫɜѫУКϛкϰϿzвȵ˕Ӣԗ',
                            'message': 'ȯΚnĲӨùІϺ´fȴкɥÍӲΔϝϾȅɿǄȄѤɰγҞκʜɐ\x9d',
                            'arguments': [
                                        {
                                                        'name': 'Ͷ\u038bЌķÒѭŀĐЃӯ˘µɗ@ӤłэŠ\xadҚB¹ΦɗȌφԉϓżϮ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 84741.22288616357,
                                                                        },
                                                    },
                                        {
                                                        'name': '˲',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŴŝɖěԟȄ©С¢ΜεԀʊ{Ā˫\u038bˎЂAҏҨ˙Ӧɏу`ʒäş',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Vб\x85ԧʵȋ_ºҡҋёßȱНƁҍͰΛΆ˗ä',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 146794.14063245992,
                                                                        },
                                                    },
                                        {
                                                        'name': 'LȠȈǋӺ˯Uѵ8Ćɬ4ӊø˱ǯƸǭцʅгɮШ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 707669.8820343773,
                                                                        },
                                                    },
                                        {
                                                        'name': '0ȫ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΤʪџÂŨͰūʋшҊώʆÕΕǴšҿΐ˽ƛϵɍσòtɁÐ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӆϓȓҧȷώǂѧÐ˯ҴʊËϣƲԈѧȏĭŉђɛğĠȜж',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1495932277572076257,
                                                                        },
                                                    },
                                        {
                                                        'name': '¿ѿȸƲƉŪγЉǱƧАѹ\x87ùȉЧ\u0382ƁԀÇȒЋ˺Ӣϔƽԗϼˮǹ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212311.057158:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'œȪȓϟ˔ϕʗʌGʹ˖ÅæȘʾ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ğĴıĥÞˌӇш˜˶ĩѣї7Ӂ<nMʒɛĚ/Ƴ\x80ʕÇȳŒԎV',
                            'message': 'ǺӔˊȗƧəɾΙΖƸӼˮβΛӚҮѥzŔ}ԓǉЕЬ§2Ϛů\x96ү',
                            'arguments': [
                                        {
                                                        'name': 'Ķԋɒ¾-ʲ˺Љʚ¡ɎϙŨԜцîɧŽǳʑŲ\x96ϜŻýǜƨȲOʠ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĺΦɱɻԧɺӖ˯ˡ\x8fƢԐ\u0380ͻΌԍӡͽ˼пɯăԎϬǲ\x7fӾȃԑ\x97',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212311.057903:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ñ§ңϥѪαӝΣ\x96óÎƇʥÌτʾӶҒXяʴζ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6481297255221754496,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʁǬ\x8d˾ТɯУcуƘǟύʺʀԆΎˍсВ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Żʳ´ЊŃҖĹБɗ\x9cåǎ?ǯÆƊDӊѥŜύVͲʨ΄ǀʶƀΧù',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x96đΗіƗXАҡĜqВѶӔˣɰЪDɹʗʳͽ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɅѓɾȰԕȎÞɼǜăˠ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5584220520780968718,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϠӪȸͳ÷ҶБбѨŜϖϻЖɻŉЪԧÁɟɚĕɜԝ\x9dϥ\u0379Ϭ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212311.058887:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': "'ǧѠѫ˖ҷΤţόӌɼĲƗ˦ȖҁӢđşA\x96\x88ЖӋɃǝĴȆŌԨ",
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212311.059089:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ķҗǒæ|ɳҚēϳϊΡǅdpŚаŜԨФľɢʯԧȳ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212311.059258:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϲȂҶɞ˹ωНЄұŚǦŶĘϚǘϹƜȏȃĜ\x92ąʊөǧɜΐ;ɳϲ',
                            'message': 'tȫȲϕҫҠˇʜ˶Ą˽ǎ҃ĤѮ˼ƝбϦƒεĎŏЏΩӦʭƅʹС',
                            'arguments': [
                                        {
                                                        'name': '}\u0382a,čɸʌЉ¶ȮƨӀƫɘ˹ǒÊ҂ǱвƝȟʵǴұЉƛʴͷǒ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѷΧÍҒʥŁňϣțʤŎʳaԘňǻѾ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɩpЯɩh(8\x9eĴ@Ǳʘ҂ρҠɖ®ԋCʢԏ6·ϳŝėћŧ˴щ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʈΖЯɴ˛ōȁЍɅ˘П˷ƈԉŌŉʝɲ˙ƉƜģ%ʖØюƴďȲð',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƗŁМȊ˟ΖĆVɫAȥКŠ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƧƉЌĦӝɃĈŪѯɴƇÅ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŽůÝ˫ǥŷϹɊɮ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 354838.4438863369,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϻ\u0378ɱѪiÛѪέȌш',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7344560347696000717,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӅЛĬԔϧĈȌ\x8fɏʚԝɝʁŨτǚĴ\x80ʊԟӢlƔҰ˪ŽǠ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ş\\ˈƟίʾışʓώ4ӪԘӨ˰ƜδҫũʤãÖчh˳\u0382ïͶ\x9dŝ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -51647.28135656492,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϥʛ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ϫ\x9dƳōѨ©ȕįμƒȥѲ\x95$ȇоŊˠ2Ǳ;ԨʰǶ\x8fԢΜʁ¼ȕ',
                            'message': 'ͺćyӗώϱɀȵӸϩȼҶʺԉӛɣɯTŌνɏԎѲҴ\x8cͷ˒ʮˌǬ',
                            'arguments': [
                                        {
                                                        'name': 'ԜЊ˟ɫԑнěʛňѿƅǻùҬЉŠɑԬёÿ4',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212311.062015:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĬɑёьġѿнͰƾĄ)ĖʎĤƺģѕ\u0380Ɩʷ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7372637462725273082,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ТÐǘφõҕǝ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ƤЯӉĺМƼͻΧѼŠͲșѨ˷ʉëШǀ'ͶΫ",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɂɧǌìɋģԗ\x9cƎDίѠɯϳäĭŏƽúɵʉȜ\u0379ϬѠύ=θÕɳ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 827067.3552729365,
                                                                        },
                                                    },
                                        {
                                                        'name': '>ǮӚъŖ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212311.063949:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƼҠŭȳ3ĦŽԥɡ¹ȸȃı˃ŚΰÜδÃŉҾӵǺȼãϛғO҈ˡ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212311.064331:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԣӥЙÌ÷ӛɮǨɜѨςˋ´ԧуËϬͽpǗ\x8aϦ¨ǘǮˎƣ¹Ėҳ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʁ¥ǳȩӔҿɁϚʚԖК',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 760142.6402982029,
                                                                        },
                                                    },
                                        {
                                                        'name': 'úѮɫˡǇʳħǜñèɱ\x8dёΊĤĩ΅ѱüȎˊНҹӾ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '5ʭӟĸɾĂБҙ6ʪСēéͱǄǶuϴǳҬϑӖĔλʘëӻ÷>ԕ',
                            'message': 'ȥð1фϫφȩǨҿƌϻKӽƢҙϫµΐѹӝтĖӒΉâƍҏĎÕԌ',
                            'arguments': [
                                        {
                                                        'name': '±œZ²@й\u0380ʹʹӡëʼρЂǠCƂǺȻ\u0380ȟ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'XέГėԑƿėŊнĻ\xad\u0382҉ƼʲԚԀʇ0ˈ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƼřϽѝ\x8e¡ȇǥʭǪ˴˄țàʖȃlπsӺɆϠǓяǃϚВăȉʹ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1132866527318263107,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԘмcƸ¡ȭĹщƑƕ˶Ап,ɸĊȞ¹ƶϠȭĵŷȀѠËρ\x8aùŐ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ė',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӸгĹƾǑCŀ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƅǛΪ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'кȃ³',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5869121723559893024,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˈǐ\x8e½ʏчӚpǶʈɔл҉Ԋ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɦɀĪɢЦ\x9a',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5572340803305010644,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x90ƻƷъȸȶiѨ¨˛әӔԚ\x96ϴ\x8dĻɸѭƠχǚԗӦŮJǕŏЈɵ',
                            'message': 'ԔӴ7ʬҩӆƁн΄БǍ˛J˪ХзǜӨIаЎ\\ƨƓʯϣ\x82ʆšÉ',
                            'arguments': [
                                        {
                                                        'name': 'ÏϳÝĪΥȫ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'τҾɗԋҢ½Ǩ˧ˋѺЧzŀǗâʓ˓АԨψƶ˓ŃĚ[ђʋˮqʼ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĆԢɇKјBǊʞƵӶȏƨ҂ɾ˘Ïȯ}ɥԗŝ\xa0ƘEЉεńɬ\x91҉',
                                                                        },
                                                    },
                                        {
                                                        'name': 'МÄʤԅ˟ϱɎӘ:Ξ˴ǃǘЬÂʺƠη¸ÖСvԑ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɔµ˂ӣŻȥӚӿ҂үѵȖǅГҔȝ_ˮþȜʈԊ\u0381ф',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'á\x81ʸ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212311.068253:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˯ϋҥНŘʥʍ˄ANłǍˈȋЯ\u038dǯ|эθуԡ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ͽ.ԡӷǔǊɳ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212311.068607:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ćε҆Ԭ\x91ʟϚҁ϶ҝśǦΈƀɜ\x80ͳêҳϭȽ;ŉ>ϤԁÆϻ˼4',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9eθçӚǘǲԪҋӇӜҫ8Ъ&ƐÆĒʋ"ƤƯźρњhԓȒ˂˘y',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɦßп˵ϵ҇ǈѠ˃ǢŇʣôŃŰωԭ,ϾιÆţʳɮɠʞnŗŇŎ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1533666860812343275,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'fʦǤųѭϚӺϣƱŸӛ|Ħî8ŴĨàŅҷŶǡЪAǶûþчиU',
                            'message': 'ˈӴɬйƒФθˀҧЅťМӑʥģ/ʹʨǢìґňĆԄȏЙ\x87ч\x83ù',
                            'arguments': [
                                        {
                                                        'name': ';Ƚ\x80Ӥӡ҉ˢƉΖÜşϳȟ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӍʏŦӂ˾ˍӪϳλӴçȮ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϝʊôłЛ§ŉϠҼƦĴ¶ʘǪύǫǉǖӌ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Uтҫȉ\x92ɭϼԮȰҧΰΏӽυˋɾǹÄӻ´Σӯ\x86ѨŇ[ȱӶÂŴ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɅƙϪ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 45097.26883560588,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʑ҃їÏÄΠӛËėѡdˤʙƊАĩòюȂơѫĥӜŎĴʬɶԌΤ˕',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȁϮʢȥʄôЄ«',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǶɉɆΑϘ˞ӴѫҦѠhДҭÙʪąΓǚӶѷȦ҈ʀɪŭŘ\x8f·Ξ´',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '°ƟϔŻƾҙѬųЃ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'іǗXӋĮkïȰѼ\u038bſȄǷ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ԯҗ»',

            'error': {
                'identifier': 'ЙƅĆñ˕',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': 'Æǘ',
                            'message': "'",
                        },
                ],
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
            'event_id': 'ƬΊɪûˋť˅ӪϢӔőʛнǵӤӖɍӓʼǛҪλʀҘӴ˯ӨōВͻ',
            'target_id': '҄ʡ΄шõԙѶ+ΝʎÐŐ×ʋÊǝŝ©cɛƆͺÜſʕȲɶǷǯϨ',
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
                    'event_id': 'ȂʬҔ-ʀjɴPƭƓ3ҷтˀŠчӶ¬¬ĩѾɔ\u0382ЭǠӫĿȦǟґ',
                    'target_id': 'ѨƓӭȝπΐӼɌǙɅŁƧɗәЮȿŕW˚\x87xƴũҩïХĎБϩȻ',
                },
                {
                    'event_id': '}ыѱaä\x8fΙ\x98ƿоĖӐƫˮАͺяĥϼǩˠǙǞløJϔGɅϙ',
                    'target_id': 'ðɴȰйѺżѯƃŇ4ĐʥʇċĠғΠѿmγUβȔɾĀǄǟȱ\x9eǛ',
                },
                {
                    'event_id': 'ϋ˃ŭƃԧуŔĖǩɼϓɴĥ²ʙӄ\x9bƌƿȮʎŀ˕҂ͺԞҮÇˠϰ',
                    'target_id': 'ѕөͳëˁϹǦʃɥ˻˰Ǔ˯Ҋη\x9cśӽΎȟԞȈϝâЯŌ҄ĸy˟',
                },
                {
                    'event_id': 'іʿɖӲǅîɘҽӱɢνԧǾѦÖ;ҕǾȫFѥˠѶ[Ͻχϫѯɛı',
                    'target_id': '˻ɽɍÌѝűҷɡȈΟƃžӣ¤ыǋӥƌαŘǉ\u0382têůɯӀŐρ:',
                },
                {
                    'event_id': '\u0380ɨgѱĹ˞шɸ',
                    'target_id': 'ȾʹӼƻȚǋƖѧƳ˙ʃɾ²dϹǅԦȬЃɤρÈɱѶɤǇͻѪʵԮ',
                },
                {
                    'event_id': 'ɅƐ\x8b\xa0νȎˈɤîˎÇJʣʫϤɕԄӲqʴɞϜӨΝ˷ǅ΅\xadӋŅ',
                    'target_id': 'ʈ-ѥϟǅʮҎΥѨˌʾǫʑϤɏҩƸěԖҿèͳĪɳƀήĜũŹɠ',
                },
                {
                    'event_id': 'ǰŷÚʨη5Ԥª˔ԩ=ǶƯġȉ¹ѝr˼нȖўўԌʾěˀҚȞȵ',
                    'target_id': 'ŇfƽʤVȰԃӟԐťχʭԚŭљʈĂȔɟixԔ<ϒ\x8eǧɏǋȃқ',
                },
                {
                    'event_id': 'ʔȢĢɀæ˟џƙɓӚӃԔӇӏѦӯżʀKƺԁɃȷǐgdӗłÀӤ',
                    'target_id': 'țȼʨ˘ʝƁɢǞʞiÕьN˘˙ΜԞƊĜÜȈɫЧпиϩȧџ\u03a2\x9b',
                },
                {
                    'event_id': '˙ѠҦƳʧ¦ј\x8eԐʧȺ¶ďïӳ\x8c˥ĖçӵāˈfĴӓɚхžƖE',
                    'target_id': 'τьƬ¹ȓΎŀ҃ԇҡϰƻɂǓ˚ȵӉĬє¼GɕɡøPǷ˝\x8bşϝ',
                },
                {
                    'event_id': 'ʜѬӮҫ˼ăǄ˄ƋʜύħĆŤɫĽˣĝӱҿĬėǜЊǣιѺȽϒԆ',
                    'target_id': 'ԙӏљċ=ӥӛ˴ȩԩΡǨӾӰƥӠѐŻȮӕˣԫϭдϲȔ\x8aǖùψ',
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
                    'event_id': 'ΰ³ŋĞҐűԄзĿχŐӛӈČˋϙȴӺˍėѺѱʅϝϟȮFŔɟȦ',
                    'target_id': 'ŪŉōǝǋϚ¤˼:Ƈά»ʗåǮĔʌǛÚ·ӟ6ɸ\x89ÏμȽeҸ\x94',
                },
                {
                    'event_id': 'ÙΓΰͷѡĳhǬӱԁчϰ»ŘßʅδȲ\\ԜљȬɳΓ\x8dβϾǻ}ȡ',
                    'target_id': 'ϼǽȶäƬҨćԟғɸũÎͲѥĢǻƚϲΥ¢˕\x97ȣԅĞΞԌĲŋŨ',
                },
                {
                    'event_id': 'ӘҒʋ¼Ɉʂγĩι¡ԩɎԤӓ!˾6ЎԬǴɇЧXэʂђ˘Νǒƀ',
                    'target_id': 'Ѭ҅ɤRӥάȓÛϑǝɓΧÆϚ»΅ѵМǋǂɏԆО˧ŮɴʧƧŨϏ',
                },
                {
                    'event_id': '҄ǜ҈уĜeƚĘԩ˩ɂӚө˺ȭɨŮêÞ\x8eʙӐ\u03a2Ʌ½ſÆƨʹɐ',
                    'target_id': '\x98ˑӷƋеӊԥˏLƋӞʮҠťŁ³m³śŋіHŻ«ˣƇѫʪҁŢ',
                },
                {
                    'event_id': 'ÑǑɿʱҊҲƪ˖ˀүԬªΩɮǞͰ\x92ψ\u0378ˀ˳ƕΜЅҪƒϏǲ,Ҝ',
                    'target_id': 'nӃġӺ1ÇΥРǜȹµ°äǬİsʟ_ˈϟ$\x9aΡόƶƠԨãԦ˕',
                },
                {
                    'event_id': '.ҟÛ\x87°Ґ¹ү[ȅɼȉͻßÕǮŽӈӱŵӋŴөʠǘҰӘӵ¿ŗ',
                    'target_id': 'ȶc~7ҺԡѹɳqϨlΫˠKġ#˳ÚȀɩ¨ʛʾ¥ЃǺҰЙǿ/',
                },
                {
                    'event_id': 'ćФʼůȅɽ˽ˉøσɹУдĥΡөóҊŵѯҕΉΝӾά\x8bʩñҞŬ',
                    'target_id': 'ΌĴˀϠǏқʢҷƬȆ÷ĈÙ˟ε\x93ҧϐáɶŉ³ԥ˔ǬԬƍћǭa',
                },
                {
                    'event_id': '\u038dɎԜԧМ*ΣӗŌѼƓԢ϶Ӓԙ˼\x8cħ҈ħαʊ2ƃŁ÷ʮǾǿӲ',
                    'target_id': 'ɚǆğнĂӽКGˮл\u0382ǷҘЭÔɈ˯Ӛɱ˘ɏ}ωʺZЋс°Ӌҝ',
                },
                {
                    'event_id': 'ˏ˫ӶŇЃϯәhƵĚЃɲƼɖ˦ŦϓʗΝƔõȭѧҋſżӫ\x8fȋƉ',
                    'target_id': "ӒԟӣʘϿϚӴқʹΛϭвʲȦnΦӤΛɗ$Ĳ?'ъǢ=ċ}Ïɬ",
                },
                {
                    'event_id': 'ԖĹŴǦȎȱʴ҆ǥɎ·ķŊȏɨƃȕ]8ʈÚ˾ȡͼ˽Ыēÿбʕ',
                    'target_id': 'ȞƯʓ}ϮʻǚβЉʙĵŕȭы¼ǳŠʗæJͰ\x9bõҨЬўӦĞ˱ͱ',
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
