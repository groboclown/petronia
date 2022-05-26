# GENERATED CODE - DO NOT MODIFY

"""
Tests for the foreman module.
Extension petronia.core.api.foreman, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

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
                'ԤƵэ˞Ѽʧġʤ˸ɏʏҪʯŤǄ\x7f·ЋǁзτԀԜ˽˃\x86ÄˣȆÛ',
                'ЯәȝŋӴǯёŰʼǿăǽ\x85ςlΈśŭºȂИӠԒğҬÄДɣʪʌ',
                'ÕԁΑǥͳӅѣ0ӧĮϩц˦ҹǴɁϸвΔВԠӠĢ:ҸȘøыǋI',
                'ԞқӸȷ\x97ԟϤԥӀeԡīɀ˔Ã3ÉҨɅƟćӜӛ_ǁӞ˅xяĮ',
                '˯ɤрѢʴȨ\\Ԟ˫ĞƀĔӛɑÿҪGӫʷɬ˔ǷÞęěƾōЍɞ*',
                'єƞоʅƳӨƝбȫǸєƽЎĎʆo˵ǚ\u0383ÙȰɷζɎȶəзύβή',
                'Қ±ԏǑЀЖȰЂ\x8eәnҪǇѝȘĨµƫƐɢˢƜӻ\u038dɥˍBǈƇY',
                'юυÙǨǖƽʋÅϨśԃ%ǆǜÊʀȀƤƻΛĂyʗЁŷ҆ˈŋƯԒ',
                'ĴϭԒ˪ҩӕǽTѳɨțУ}Ұ(γŚО·ȘǬЊȮԬѿӨҵЭЮȭ',
                'ԟƳͱʷʞɸ"șԜу-ĺѦьƎĆɒĠРlŴ\x7fғƝњεөԢԂĢ',
            ],
            'source_id_prefixes': [
                '˞/Ҩďɽǚĝ˫ЙćӤȠӪΘŭǔĺӀ˲ŏӡ%СɝƿïˢЙďΣ',
                'ԩ\x85eӰАϸƏͷαɤʮșÞԚԫƱϼӷɼǸąƳӣ¦ҺˆеђʋƢ',
                'ӢгǮәȻϝ*Ǥ҅łȇȩĄțÏεÈҿćԛǎ\x9cƳ\x84ˁЛţ˲ĞȖ',
                'wÁɜӴωҰƛɽɒѐvÌ˷¥ƭˈҽǝеʺhҚɴѷƨ(ʢɈóž',
                '˒Ѩ¥Ü˜ÇͷЩƖǄɜτΟŭÏªҞ\x90οɓVӁͽǩǶūÑ˲ҝͲ',
                'χʍ½ìьҿ¿ǦȓөɦȄ¯ћ¡ɹˮϽųĳÁƌ_ԆΦ\x96?ӟƬȽ',
                'ƨӦүɿяÓǿǉÕ\x9fҡҘʆĻϞο}҉ЌȁăǭYǣÇƎҍМˤқ',
                '·ʝª҅ɬӡʲŗƯЫǸ\x9aǿŢïНлƂ+ÿξЀA}ʬҶЍŪ\u0380Ҍ',
                'ɝzͰӰĉЎĬП&¾ΨΠĺɇɝČȫɖԠ?ùФ£\u038b΅ȯSщɡԣ',
                'ĈMϬӂΆɜɰńŪВϝҬχO˥ͳҝʍҥĊӔȭɂσɠƹĻƖöʼ',
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
            'action': 'ǲҗ>ȫʢԓȄěō<¦ȖȘΐȷѻɈfćȌ7\u03a2ͲҹNɐдԁΆЕ',
            'resources': [
                'ȫiʗȡƿÒѻƗϨʛӬĤϟłљŢϕʉԟ',
                'ЩŽúĬ˄˫ĝΆӿ˛ĞлȈƥƪMωŲȼί˖ԔØԐӅǒϜѭΥr',
                'ϫͶĩƍӈ҆ҒЌǞω#ҪƭϙϚőȾåԨĒӗÈ\x85ƓȩĎҍƊѳȂ',
                'ΛħӦА\x9c˙ȈƒtǕőÓ˅ȏ˳АĝӥθϰЁ$ɺϊǢŇ´Y΄Ԛ',
                '˼â҃\x9dӥȕ\x89öϛĖьƝӸ˘ϯɊʇųҏȟ[ӔƞϱʿŗUҺӬÛ',
                'ǥ˄ĜɢРŁˠȆưȊеYЇƦĴȗҝʨʨQЈϤҶгiʤӌќҌԝ',
                'ö˒Ͻǭ·ːàMñʵĦУдπԚІ\x93ˑΞтŃЎӳ¥φŚҠƻʌ°',
                'ĨΞϧΡùɀљǈƤʐ%ɾçȑӷƲұʻҲ˶˧ӹǐɫo9ʹBƈЊ',
                'œѱ&Ώí҉ўǈ"ҘřɍǪϦτȢπ+ŗжОЬ`Ҭßƺɵ;\u0381Ʊ',
                'Ӹ`ŇɚѯȈѢϑҒБϧK;ˎ\x98˖ϻÿ2ĺҭʛҸǂʨʮѱʓЎȗ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'Ɵ',

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
            'name': 'ňćȨОŇ҆\x83uҵАƤIӹϧͳǹɱK ǨБ˒',
            'version': [
                -1455036596221021,
                -1819874750051542768,
                -7049297542825493892,
            ],
            'location': [
                'șҷΙƣɾƠѻҤЖϺӍ{ӞӵοϵLȡԭɄҿņ÷ĝłӕ\x85Ƭ>Λ',
                'ԆȗüɫƄǓ˭з4ȔԦҖȯ¢ѪйͲφӍǝӔʊ\x9bXĺΉɋʚŀȘ',
                'ƉŹE"ĒâМƼЕ¾^Ͻ˕ʛТǾɛ²ǉĦǊϴțɼæиӪɮĶğ',
                'υĲAĿǂѱяƛŁĵChҒ«ŦЃЮκĭ˓Ư#ҬƐǝЉyňӣƍ',
                'ƻʉƫ¯Ûų×όʌ\x81;ƎКрÚѸϰҚŤȁɓҐƄѹƾŻώ\x8fʞù',
                'şěȵҵЪSϑžΉ,ЪөӒɩȀīªˊрģӽԦο˒˞ɿ@ȏɁτ',
                'а ȏǧÜʴ\x9dŠ˖ƧόĲˈϹÎŎƘ#ʈ˨\x9eÐƪÀǮҋȇ/ɺǛ',
                'EҦĘЕȪȒӽЖŕЧǙɡԂƝɄʓҷ˴ʇ7$ԅ˄ʘ}ñ=Ƶµӥ',
                'ЃϹʨҌŋ˦ҌɼǓωeɅīӤЧ¡ұАèiѽмǳґǷȥуѬöΟ',
                'ÅϐĖșŃͺƕ\\ØԍÕѳҒѡƳǈ\x91PĨťҌ\x93˶ɨ|ĥșĻ˟g',
            ],
            'runtime': 'ԑƵĺęƙͶɽĕχƾzȝȨѹWǵϐҐϨÎ˩ԞˉӮǿȪ?ǋΫ˺',
            'send_access': {
                'event_ids': [
                    'ўƼϕȽ>ĕƇǖˉфΜѷȚ˄҅ѪȃTϢʟ˦ѸŎʼÆԂȻԊдě',
                    '¡ȥΙˇъȽǫЧӏϛ¾зҷˎĈʮĕЂԎŹ¹Ĕ˟ªĆӬŤɰŒѦ',
                    '҇ļԤßѳǆ@ŞѕцíѿǖȎ»Ǩϒ{úěҾЂǄƋΉ·ĚԏFʒ',
                    'ɔ˫£ºˈǫŢkàӚɂ˰*yɣˢǱgϤ\xad/ǯҼöԬøʐͰV\u038d',
                    'ǆή\x91Az\x9bΠɵҳǵф˸Źҍ1ьѨΔԕ\u03a2ĴЂзʴњÖүǆġѺ',
                    '΄ɠȌϑʎ;QКјӦΘŊʌƞË\x9bԬŁ\u038dŻΚϔǃÓч\x8dΰMǝŘ',
                    '˰ҤҮǪǺ',
                    'ћαʦȓκğ;ʯҶıԥǛэ!ɯϓSĴƧʮªcϐѡԧ\\ʓÌ˲ǜ',
                    'ѢRǏ~yˊ¤ӋφëӼΊéƐǘΣӞӣ7Ƅѧ\x8aʐˌӋѶӓʈIƟ',
                    'ÙǙƁpҤǞέбίӁ\\ƥŀʞ\x85İ}ǏƅБΪ@˜ѡüȢªÞūɉ',
                ],
                'source_id_prefixes': [
                    'ӀǟԦːˑӀ\x97ƕҵψʚӍƷ\xa0сԬԌȷāЋǬҘςχSȀsʭ\x9cε',
                    'ʇǗ\\QЗӳӁbҕ§ѳÏʚӿ¨UѳĹăɪήρӯνιӦġјɼѹ',
                    'ĄȮНσ:ȹҢGţΆōǎԚϝĩľęӅǒƟĠАŴАҖϬzё¥ȼ',
                    'ȤԄʡĊǁİˤð+ɝŽʆˎӟɤАÂΝŗȷ',
                    'Қϫ¥ȅϤʉБҔɟɗҮбʶù£ƯĎƓĘüҩλƆәFʖψҽΫҗ',
                    'ӦӿłǉƷ\x91ģɕȁŲ˓ӉưΚ˛ФңϭʬΙӲʠl΅Ԍԙϝ΅ɺ\x99',
                    'ĺӊШžӿȸƹƭҳRҺƒĪǭђǃÎƋҎ\x98йƲӘHαƬɝµɅÄ',
                    'ǈӪčɓΏϷ˂ʴß˝ɣΐćǨѧǖϪєǼğƟЛǤͶǲľʕ~Ӣϊ',
                    'ԖΠȼ>ʿĳԎɁЦaϻŽĈĄΐʋǭ¢ɟӇұӻžƜǊŐƛʹȌʈ',
                    'ȴΉӬZuŖҀ³œĖǖƛҟǞΔǎ7ºОqӵƜȼҵ·˘j\x9fӫˠ',
                ],
            },
            'configuration': 'ΉȏяγƦʩȽ΅ЋӏӔiΆʙTƱÖѺȄНͼ\xa0;ĩȦǧЍӾҪʕ',
            'permissions': [
                {
                    'action': 'Ϸŧȕ[ʬѿΥų\u0382ԎɳŇҢӳԩâɌŗɘͿğɏƱ)ˇӍŴöѳ¢',
                    'resources': [
                            'ϞԓОƬϰӬΔыԔƦǺϑёͲ\x8dOϷEeΧӦэǈȱІĈɋͺǑχ',
                            'Ԗ\u038b¬ʅΜ҆Ӷӻǎӯǅ¸ͿϼƐӇ~˅βΌ˰˄мǣɂ=ɽ²Ϋϥ',
                            'ƇӸjӁɘй˫ӇtăΜӢԡǸРfȚʥɑÜϨҐŽǱÒ\x84ϚйɥЎ',
                            'ǆnˇ>\\ɼӋһ\u03a2ŷ˼ѯʟɴїϞѥǋϠ5{ώĐƜщȂˈĈ±ǯ',
                            'ʭèʝЯӯЃрӪşӺ^ƾ˔Ô',
                            'Uȕ·%уPκǔОԙΞХɍ\x8fɮӊЁΙsPȱԢ\\ǯÛӂљöАˣ',
                            'ѴίЌϟӌĸɃˎʈʙż²ќ{ЋϦ˼ΤŐɴѿʹkͿCӛˇɸǫù',
                            'ƻѩ\u0382ζĊĭyǾȬңϭ9ʓͱǞìI]ɺʃđΰ.ԗӎχнƴɤй',
                            'ÁɺҁɄԢ{\u0378ɊƁƷƫλӂƐͼΕȒǲħԫѰБӄξӮkέȵӖ³',
                            '½ƮϭŞ_хϗ?éȥώҙɈȐψΌϙѼӕҘ[ӀȠʱθʤɡҹ\x9bÆ',
                        ],
                },
                {
                    'action': 'ѣ˃ǹʤɌǱWʔɅȊźɌˬѯҺȫΆǞѩѩ\u038dǰʁϡβŽʻШбǭ',
                    'resources': [
                            'ŪǇʷϊ˗ɊżξƂöɿôȟЄчӿӧˏҙәԤˮˎΰ϶ʡÔ\u0380ԮΠ',
                            'ΚˤŢǂ`Ѳ=$ɤ˨Ǜӳҥσзǝҁ3ʹμƹǍҬʮRƴԇų\x97ϐ',
                            'ёƌ˳sӠDʠ^ǠĘђҗΤрɢѻͼ',
                            'ϘƴΎįϾ.ɼȜЗőǕζѐƚòҖƯƋŷкΞуŀΌϬvъƊƽʽ',
                            'ƬɋЙҨÞħÏӔѐϗƟˮҲԫǛ½ŇƹʭђҸıοȾĴϻz˶ȿǫ',
                            'κтġ˱d϶ӆŇɮƞҖϋǮԂΡǼǥӘ\u03a2\x8eԄǞЮƠɆɌʶχʧϯ',
                            'ϛѡʥƝſǟϒЅҭǍ]öúӭмʹɤŹɥԣDήɇϼˊ˝ÝԜх³',
                            'ŃʔƙȬΏǅǓӫƢ\xadȦӞӮʳũΌËʡӹҩ˱ȼԇҺвȖȲźĠŷ',
                            'ˏϊјȼԉͰgǕƄξЙƘҭѣʘҸɨϳΐΐԢłËŇsԭɭӠƇϹ',
                            "ϔ\x96ŵ\x82ҔŸӄƕų˱ԟ'ƨϴψh˜˳ЬƐƲɣË¬ӽHɡƳȉ\x8c",
                        ],
                },
                {
                    'action': 'ȏXˬϣȽТʣɚЯү˥S˓Т΄=ɥɵ\u038bԧˉ%ӚɗП҈Ǔ\x88ѐЬ',
                    'resources': [
                            'ϽĪȾΑɕӣ=4ͱȉŌ%ƙώzˍȯхŊǞʙҟύƃ0ӣɝȅΑȩ',
                            'ĬϮʓΕĳŔϴɣΕїρϐJѠƴϤȸàӚYǐcΦ˽Ҳӫɋ˓ÿͻ',
                            'ԨɬQҹ˨ЦѓŉаxΕɊŶҊƜɴɰˁÙƈΝ˓ǓӻȌȺӇҌцщ',
                            'Љ\x7f\x98эЋÌĈNÐʂˎѫěǜҲşĴƛç?˱ȆӇɠΆӷҌƌ@Ӊ',
                            'ȩШŐbΩȓԏϖËԂʰο˶ӾƻɛʕȸәʽʬʙċǨԫɝΈϸéǤ',
                            'ѫχ!ƠˌΒĬ\x85ʠİûВC@ȨԊÃӳǬϱțðģ\x97ƩЄΨąЂЋ',
                            'ӫӨˑσӁӍϚϭÒ\x81ʣɄю\u0380Ө˳ȞӨΑόЦΌ\u03a2=ŽʪǞ˙ɤȝ',
                            'Ƿ˂ϰİ\x9aϋ\x8c\x85ˤѺВЋĔǿҗáĉԅϵҒЦˀőʜſѯOɠβц',
                            'όȓ˫ǞҏɞˎԊөŏǝ¬˽ѨǣԥϣҙɷˀǲǫӐϣˡӠÀȐ[Ģ',
                            ':ā?\x96ˁɎԦӶéNШπ(Ιӻ;Ϊ:ϸ°ƞ×Ң\\Ʉ{ýùҾʈ',
                        ],
                },
                {
                    'action': 'ѻǸύςë¾Ћӻ\x9eʤȣǠʶƘŋŻ¹ƔňҌЛėԪȟǊŤЅɴĺɞ',
                    'resources': [
                            'ΈԫɻӖ¼ȃÌ˧ӽƐʚȜϲgčǄʿȏē!ȤȴԠϧѦ¥ϯҩϑɁ',
                            'ҊѠВԤөƌҊёCÕÖēөƨԡЄÑ',
                            'ʡȟǴЗƞȉƜ\u0378āȟͰӶǃӲ\x84ςƦȒºɥϝƉѶԩήǪ˰қԓ˼',
                            '˘ΒŬˬɭΥƔŲ\x87ɀôţʮЌСԖѴͷĂêțЉʘΛ£ӽϤńӪF',
                            'ĔɫļͶюӋнʩǲѫЖˆɰČЇmƕ\x87ǉɚъұĔȜ\u0383ˀʅÙ&ő',
                            'ǟƘϹӅԞўľĦһѧщ<ɵøӱƜΕ\x92ɴǨӲɒšΠɽåϸóҫȫ',
                            '˸xƐôȬ.ѼνȬşɗ\\Ԃ~ԦӚϳʢ#Ҥ´Άƻ˼ʂ\u0381ĦϏɱ\x89',
                            'ͱŲǇ\x98ЈƟ˲ʋҗɳÍѫ\x80ӁåәȘô҇Г£\x8dӱæƗҢӄƼϵŦ',
                            'ΏȝċЇĨӦӽͰ-σǪ{ɑӮƤɁɂрéƮǤΗҟƷϠ@ύŠˁӣ',
                            'ҔĬÿǢ7NȎ˃ȮƲɣѨԎӹǭ˥<ƿǳкҩøŶӦzǑәÒŃŇ',
                        ],
                },
                {
                    'action': 'ÝĹъ\u0380ѣϘǅϢĹÐґΡˑйȉΧʈӞ\x8fΔÛʭvȋűӁӸéͶу',
                    'resources': [
                            "ѱɰ·ҽǀŀ'āÞѹҖƀƁɿżʟ0ӖŤķ·ʰǀ\x93ùµǃ~˦ů",
                            'Аӹ! ưǌғˡ˱úw\x96ʊ\u0382ώӠџљзӡԔçė·ǌоΧϞÿɆ',
                            'ίͺѠϵ>ʡžʭÇ˚ҞϷ²ЂĬϝ:ԅǯʽÇΌƭϾɿЭжȥƛѪ',
                            'ŕԂňÜͰȰǑǿJĽ\x91kӫ_ӫǩ0ҊЖʥϼ˲Ƒǜѿ˗ɛЌƉŮ',
                            'Ƥ\x8cś҇ωѸĮˬʾÏИapEπξӋǻPńÆĕԆƁдƚθҖɐӥ',
                            'ΌǦɓ~ƞɸŬ!ˑъϬʽҵΒǮάƕӔǚĸāǃϪŕȖӪɕѿɳ#',
                            'ĹŪȏĝZĥŹéɿǫɭ?ĉĖхcǵǶʩϓѵ7ÆΎʅΚΜơʸɩ',
                            'lǝƍɧ;\x9aʈɃυǽĠԚѢУ\u0379и҄Ŕ˒ɵ&мѸΠĚű҈˼ҋc',
                            'ÜГǓÒÃġvĎ\u0381Ţ\x84ʣϻΊ˽[Êí҅àˋЍåʺѥϴɽ\x91\x83Ϝ',
                            'ɺӕȵɪё˓ԋǿˮʳϕӨȑũϝӤȨĦκ\u0381˖ϕƽŇˣѫϐ˞´˽',
                        ],
                },
                {
                    'action': '˭ΡԂåѬȓвѴҖŠaˇλğǒʜɱĊ\x98ųŶȔӟӈ¨ÁÜˏͲÚ',
                    'resources': [
                            'Ϝ\x87нŖŨȥп[ϝřîƷˏȗ˺!ԥԍƌƧ¯\x87ˑ˭ąѢ˂ɪ¨ţ',
                            'ҏѼѡεӢ÷\u0381ƿťΤŃ҆ΒǲÿӨđʽ\x9bɏϘ:řbƧ<ўȯƠƘ',
                            'ÔƠDċӹƊǙÐԧԥ˫ӻřʐE©öĖˤºЀȺѝъƞԑˤˮ¦ǜ',
                            'ˍç\x82ϮǙɿђώrЄ΅şbͱӄкӺĸāюȄĸĎѳpȺƭĭδЊ',
                            "rӳɓpѭνȊѭÏΏɣà]ǡ'Ѯɖ҂ƤлʑĮɼ»ΨãϽԒӪӜ",
                            'ТЉЎ\x9eļϜүǀɴҝǟȯƷ<ƖϛԦӕȺОßUһtñǻˎɃԠL',
                            'ԄМʵ¡ƴǬΓѢǍϼԔǭӅЛȦΙα¶ǪäŹĿӄɗë͵ʨ4Хʫ',
                            '˟ľ\x90ɺÞɱ¿ԁ\x8fëҚЮԡϹƽѓųĸ˭Ĳ˝Ĳôòlԃё¸·Ƚ',
                            '˕ήҀ¬ɨӅĖә®PԨ©\x98ΫǙ҃ʄɂҏǋˤ·ƽҙоȥɏƼ8S',
                            'ȴҀǋӮgΨů җŬɥƓϪàǂïˣ£Ȥ"ѨиĤˬ\x99ĳԪʓάª',
                        ],
                },
                {
                    'action': 'ÇǛϦ0ҍXǰūŋюǆɢd{ɸȏïʧ«ύĞƹ˼ƄďǮΈ¾ӤӞ',
                    'resources': [
                            'ϑϖ¾ѐ\x88ǛϣӺӊɔś͵\u0383ƌϥ@Ф°КƉɜʊɀͳ\u038bußоΙ˂',
                            'ҰMЃсη\x83ЙɺʻԅƬãŴ.\x8cƳжɈҜКеȹþѿӳϚˁӮɨŖ',
                            'ѿˀģ8ϬˋˢӼ;¼Ӽ˸Ƴ˘\x88ɋˬӫϗӡЙҲȹŃӝƉƹʾφʻ',
                            'ǫåԫƮ×ȽЧϔԌcξңӠЀŢɌө˂FӏѫӼ\x82ɀ˟ĔŨѿȐǐ',
                            'ʳӧɡҌϚΎEĖǸǾҳуƎđԪӎ8ʆŀͻƔÉŇ¯ɲө]Üԇʿ',
                            'ǛĤʵ҄ōχȗƾѹ·ɆȦ҃ΫԪˢKɠǾΆƱӷŷȑƏɻʻBΠĮ',
                            'аԐӄпpԇîѭɾəъЏԓӌǣ˘JїRXõɪкɱÉΔļҙǡØ',
                            'Хń°śˎӷʔɶяʷϣïŏυѷőɎÈþγΑЩʍô\u0383ωӘɇĕ҈',
                            'ѡćùкӎҾƐʤϥʘ˚?ƕԌԇŎԪ˲ȓϙ~ӷЋԍCӾƅҧϻŸ',
                            'ԝČƝҤѺԭҠƶь\u038dõÊñΠ\x81ЩȞʑĐʋȞɢʸѹ˹пҚхɥņ',
                        ],
                },
                {
                    'action': 'ɷșԜUңѻЩlώŀ\u0378ȎƙǓ\u0380LϓͶÐ/ɤ¿γțͰɢˢӊіЃ',
                    'resources': [
                            'ӄʴÂαǏÓ2ǎЌγƜƉ.қYEŇ˕ƴж\x9fϖNÁΚʡ\x87ŶLԏ',
                            'пвɷҰѝƙkȢʞԐǽЇɋilɓΕƠϟƫæčĩ¡ŢŐΐǼѯŗ',
                            'ӫӽɇԏтѱϭӆЕǥ҂ϻȷƝЎ~ȸʀϣȲ\\ӄŖú^ҹĊš¿l',
                            'ɣҊщ',
                            'ĊҵėɜѹƮƠʔƋϣ˟ӛǠWɀ8ȼҍϩǓhÄз˃ёeğѫȨҫ',
                            'ΎɡɵɐıèҦMˑɦžȜӑԬЦҽɧєйʾy˃ѣϪPʮƇԣĞҝ',
                            '˕ȋӀȹɨ˽ϭ˰ğ&Ϭʦ3ƆƻąȆлΊnҶϩŘȼϛƁԨԉљǅ',
                            'Ǐ\x96ϡʊ\x8eȵˢ˂њύ?ʮėЮƨͺgѦXǫπˈ\x9bɀқυʁҭӉG',
                            '>цɡɬСҮcνҗñ˓FŨз}ќĸοLěξĶμͷФ\x8eѭώmʈ',
                            'ɳ¬@Ѥѝ|ƚ©Ƭ^ļȼœȷϤ¹ΠϴȴԂśĜѮɳ˶ú˥ҳΔǷ',
                        ],
                },
                {
                    'action': 'ГǬұɳ6Ҡ´Ґφ!ѰЇʻΙǶưȼҩƌêǟοҿӅʁѕƂͳ¡Ѣ',
                    'resources': [
                            'ΒȵԮƒźŔ\u0383ĽҔΣğǮȠĄĝoЊԪɢΧӵ;ǩƗύΈɕҠӼμ',
                            'ϠǩѻϞƟϔӵӕLŞʂÖŕӴѓȝʤӶƟЄƳӺОƖԙʳκ³ЊC',
                            'Ƣќ^ӓʷöҞлΖŇYMӳǏȃʰȘЊˬφˋϽϠӆӿcϫԭɮ:',
                            ';źɢԕǓȡϢχΠϓɕҶūǾÌѾĂ8˗ȌͶϪƜrĄƽ˂ӨWǻ',
                            'Į;ʳɺȗϥ{ǊĊ˓¿Ӵ˗ǉ\x96ϦжńǮlЭϔȱϦҰdϋÅ\x8bɶ',
                            'ʆϑ?ӕųĚòөĢòSϞĄиҙƌԪ҃ÂџϞ˧ο\x82ĔǾЦ®˓Й',
                            '\x9aĸ˔Ȏйȁω±\u038bǲ˽ƙҴɚӺǻʥώˠɛȚOőǦ˻ǝӳġǝɮ',
                            'ɯрё6\x91ж8¥КĿҜTyѨкѼīТʓͷԦ˨ϺʚG1ǼҿřϠ',
                            'ԘªɾԭüͺI\u0382ʦγȸʬȯ\x99ĆͲƈƃbúчŏʘWПϾʢͻơЙ',
                            "ҋř9цԆ\x81Ӽѝ'ðӎҙѶѶӇ˾Ʒ҂ʧ\u03a2ӛ\x93ÄӸаÐǁϪƑǎ",
                        ],
                },
                {
                    'action': 'ƟͻʉЃϒ\u0380Ó˚ɮ?\x9eţϿÈÿĕѥȣǺȸWќˉъȻȬ"һπń',
                    'resources': [
                            'ĩʪ\x80ӨϮɎɩʖӯѶŕŒÕEȠ΄ƬΘʴҽХΕ\xa0ǚʇȱɼķӄɾ',
                            'ԔĪԃþĹ\x9bɹ@ŪȆѭȭƸŢȺ|˧rƠ˼Ӱ˹ѸȊʩρɚȇŗˬ',
                            '΅ϥΑζЇɀCǫДѺϦϏă3ӯҜʐÕӆˣȁ˼ѰǗVԀďʪ˸Σ',
                            'ԅͼėŎχыӬΐ\x96Ђ˳ҢЂģԨГɛcŎɥ;ɂɐśŇ¿Ø\x8dƏЈ',
                            'ψɐƀϷρʰʖŰDŊ\u0383нźˠr˙ƂǕ{ïŀ7әŲǶĲӛԅƛÛ',
                            'Ŭɡɗ¥ņԙʳ҅Øɢɍ¶ƽ¢Î˅ŻŨа\x96ǰӽ\x9a\x9aврөŬЏʆ',
                            'cŪɇћīԣ΄b/Ą,ǮʉЦ İjɼѰoКԎɲž˪ǓмǮӉϛ',
                            'Ĥғ˹ǑԚȝќLΐҏʯτʅӂ\x92Ə҅ЙԈѫǇсϪҨ˝`АȊŧԈ',
                            'Ϋ^ȸƞˏŐ˟ˋŲv˵ƚˊbǐÓÆʄýΒЃøōźʻò˾ɎВȲ',
                            'ϛ҃ȡ(ŠзӡЧ\xadǟȜϫҢ҄ȀĆɓƵ¸ǼˡӠƯύȞſɰŮѸҳ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ώʌӻ',

            'version': [
                -5422611060540717065,
                -4087374880846276741,
                -171102654413713267,
            ],

            'location': [
                'Ю',
            ],

            'runtime': 'ƶ',

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
            'name': '_WƹʷØўлȰΟ΄¦ɽŉŔȅǍСҼǤƅƤɞ\x82ȥĥǿĂnө˛',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ĩǨ(',

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
            '$': 'Ϟ\u0381Ȋɸ\x96\x94ϓȜôƚʨǹҀɡLͿČŴРτұŻζƈˍâӸʉԒћ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -2797309538464594025,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 402859.3583304247,
        },
    ),

    (
        'bool',
        {
            '^': 'bool',
            '$': False,
        },
    ),

    (
        'datetime',
        {
            '^': 'datetime',
            '$': '20220526:211008.074451:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ԮûŢʀυΒόƸϊ\x9fǁҽĵĝϤӌƚǏˆѪȍȾ\u0378QЮίEöѥv',
                'ɕĥЪХϑΰń?˓ԋӤӷСƣ˥Ǚ˸ƐЬӥƈș0ҊǻȞgŌsȗ',
                '˟ńїӯʹʣʏ˚ѭŖŌȖ\x8aε:yҎǽÌȴçðψˎΑԧѕΡҾƧ',
                'ƻǑɹʗ\u0383ĬӫøĝǦȠԠуƈί²jʦƹ8dҮʁȉфҢ͵Ƌş ',
                'ԄǘǛϗ&ʲŷЁÚѹϽҌѹȩɟÚѮ_ΉǍԮϿ\x8aˈɖuşͽӛ˯',
                'Ӻ˒ȵƩˬϴΏҭɲιϝͺƤ)Ƌłĳҫ\u03a2ʳƷΦѿϋǈ¤ǵʊѶń',
                'ŻȂľВŇϧÞdʌƩ«Ɏǳ0їŪԕѿxȻʏąϱε±ˍŧѡǋ7',
                'ёӲƩ҄ǊnɓΎȰЯ7ƱǆѿƔ\x91ԝʗѢűİgȐʿɜþǶʇǟӎ',
                "ĬʭдjÀɠ8ŉʕƑҰ'ίʋêӪš˝˒знìϣ\u038bɮȣϱ»Уç",
                'û¾ӷˢӤΏѳƕȫҀμΘˆÉƔоϊԜƭϤЈцƆŒÄÎԄ£qɯ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                3433348809034000076,
                -1363797899035682447,
                -2617803708261763873,
                -6482201341839811576,
                -375865733762871126,
                -8431111478708759769,
                -2665256388716957197,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                741627.9503229879,
                -89826.21619917025,
                710271.0703558496,
                916934.1762040849,
                65094.21342892389,
                77261.10184479752,
                830094.0445110457,
                809163.8611349477,
                468788.9216475723,
                78118.50727725215,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                True,
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
                '20220526:211009.053985:+0000',
                '20220526:211009.075166:+0000',
                '20220526:211009.096253:+0000',
                '20220526:211009.118000:+0000',
                '20220526:211009.139061:+0000',
                '20220526:211009.160368:+0000',
                '20220526:211009.182854:+0000',
                '20220526:211009.203483:+0000',
                '20220526:211009.228464:+0000',
                '20220526:211009.250155:+0000',
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
            'name': 'ΞXͼƯʥ1ɒӞΣӨY\x94ΩȾ\x85ԞѺťŕхųʌӰǚѴ-ΑǏJı',
            'value': {
                '^': 'float',
                '$': 784496.7441747857,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ǐ',

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
            'catalog': 'ôу҈ǝ&ιεҊ˞Χțzƶƽ\u038d\x86ƬÝ˧cЀȭƅǜτӯǖҪҖЛ',
            'message': 'ͽѩʂâƐɒĭŕʑ>ӝʋæϩδȇŒӚԉƚҬÆɲh\u0381˯ѴВɓ>',
            'arguments': [
                {
                    'name': 'ʖǗǘʸˮĵʞСΡѥ¿ʰƄΙΏɪņ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': '҂ŌĲϨāǪÅȃƳҾċϗ<ţϥɘʑʎÖûЕζȴ˼ÆƊѬɆΙŠ',
                    'value': {
                            '^': 'datetime',
                            '$': '20220526:211005.798230:+0000',
                        },
                },
                {
                    'name': '˭ҶЮȟƘÓӣӮԃ]\x8c£¦ɻɟˉӧϯßĝК',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        True,
                                        True,
                                        True,
                                        True,
                                        True,
                                        False,
                                        False,
                                        False,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'ƫÎÁɁʚΘұˍʃЪҸǒ',
                    'value': {
                            '^': 'float',
                            '$': 147087.97371338095,
                        },
                },
                {
                    'name': 'ǢɶŒ²ɯǧAƅÃÑЍȚϬʓϷǚӬÚψ¶ŕƔВǴj˃ƺƺœ˷',
                    'value': {
                            '^': 'datetime',
                            '$': '20220526:211006.276379:+0000',
                        },
                },
                {
                    'name': 'г-ŚӅЁЇń',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        6329202177580070251,
                                        6326439260490540107,
                                        -7290771193138109966,
                                        -1923362181801495231,
                                        8081442053601509785,
                                        8371004862686000430,
                                        6798460645039982459,
                                        -3850559761281850837,
                                        -666417173379228524,
                                        -3441407436879734235,
                                    ],
                        },
                },
                {
                    'name': 'WҖɼЁưήѡȜƽ:½ϸлʂҀ·',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ΒƺĮɫ\x8bƮŧ҇ƥύЄù\x9fƗE˽ūԘШԧѶǣX҆\u0378˸ѱċǛɊ',
                                        'ʟčȅʥɢνŪɟCΥɓЯǾͳҵˡÇƇ˪ʯŉҐøϫǨKωΩΈʳ',
                                        'ǳȄ1ǯ΄ơnԦиFђʹʳϽӋбʵĕѦʍÕƎӇɞǝŨɠѣƮ˞',
                                        'ſÊɠʎ;ĉ ѭ\x8aɖ҃O˰À/ōĿ¬œǅԈԗɣЫͷτϵӬʊ\x87',
                                        'ҜǗҞõōņŘɕǐӎϤʹŇѓɱʗçgӹÞš\u0378 ǙѪlɱҎǡу',
                                        'bЏKvғʌǵ2ЮҷˈѦэӘҎ7Ĕ¾ȳ ˫ɃҐѬ\xa0Œқ×Εϰ',
                                        'ԧĨӑsԭļă;ȥʻʲ\x98ɊɎ\x97ӬÕƟЮɈ˩҄ЈºϥҳƔ|ǉė',
                                        'İӸѕѼǤʌȷóӵԂɨΏɜȃԭϱ˜ѻʓ˷ҠǙѮљĦɸǽˬȄ˝',
                                        '$×џíʽǱȤҝƋлGɼ˧ԔʼӜƝˬԤD¹ԨȆ˜ǖӼϗϒΔǈ',
                                        'ɁѵΑДԏЭ˳ÍπŤҹѓѝɓÒȏЄʅΒŸʀĩПōɩќmɪłɼ',
                                    ],
                        },
                },
                {
                    'name': 'πɄ҆¬ϸĀӢSɗӖ\x9fЃΦӲƳ˂ӱԔʈў΄ĔӚҤeЄ\x7fЫïY',
                    'value': {
                            '^': 'datetime',
                            '$': '20220526:211006.985097:+0000',
                        },
                },
                {
                    'name': 'ЉUƴ.ҵǏ6ȯҊ҆ńƬrŋǫļ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        478799.04709413473,
                                        150990.28908321421,
                                        21858.519399468772,
                                        159539.82351371855,
                                        786475.7518993379,
                                        646138.970089436,
                                        402957.3997505426,
                                        214122.60901753663,
                                        -66520.06338691873,
                                        677867.5227094737,
                                    ],
                        },
                },
                {
                    'name': 'ԉ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        -41677.17040719876,
                                        -3166.149921716409,
                                        912031.4031621867,
                                        502220.47174385877,
                                        382664.394898094,
                                        9187.377156825343,
                                        988357.6368029267,
                                        290810.7653418134,
                                        337137.72598880803,
                                        895401.0896293087,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ǜϢ',

            'message': 'Ͱ',

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
            'identifier': 'ɸʳΜԏһPŠ\x86Lǔ\x88ЀƽÎūƽĤˈӟӡǣɘΪгȰЉҖԧͽǯ',
            'categories': [
                'access-restriction',
                'configuration',
                'os',
                'file',
                'file',
                'os',
                'os',
                'os',
                'os',
                'file',
            ],
            'source': 'ơϞÔӝϱYҮǑǝÑф9ѻ«ēxʠѱӭȼȭ3ȭƾ\u0383\x9b҄őЂΒ',
            'messages': [
                {
                    'catalog': '\x84цŨУϽԏѴƌɝĴ?Ϙɀí¨ѱɿDűҸǇġ¾ÏǢϽfʤ·П',
                    'message': 'ŧЅĶǇŀʳҸӰɫҤȽѫK˭ΘȟƇΠȘЅƻ\x8eΛƷãӐːёŠ%',
                    'arguments': [
                            {
                                        'name': 'ӟùƥκʦî\x8eȥѽOΟʬπї˝ΆϊϙʰǓɲΑʉ˗ί',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210944.084535:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ˬ;ȧĉӀнźŀϺҝѲű˽ɓΣʩЯΒæãϡӓӎǁĝɒͶ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:210944.198925:+0000',
                                                                            '20220526:210944.223374:+0000',
                                                                            '20220526:210944.248107:+0000',
                                                                            '20220526:210944.277213:+0000',
                                                                            '20220526:210944.302679:+0000',
                                                                            '20220526:210944.328688:+0000',
                                                                            '20220526:210944.353187:+0000',
                                                                            '20220526:210944.378505:+0000',
                                                                            '20220526:210944.402852:+0000',
                                                                            '20220526:210944.433898:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҤӟӼΣЁʥʵƦǶȜɊά5¥Ιϗϴɡԓ˖ҤƖοĊˋΉÞşӖϦ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȐƟҪƧɜģʹŮǒрӻƂҧϮ҇±~ǱʔʬӲӋ˜\x86˟Ӆ\x81Ӊ˪ӧ',
                                                                            'Ŕǥӻɫƛĵѭʪ\u0381İŕ8n;Ŧ÷ңïʎȴƔӫҌʏʦƳǩąɒʱ',
                                                                            '˥ƐƜŌƱҁѭƇɆĖǴņĩђΆ°ξϨŖ.дȢЯ˝ǕȊҝäCA',
                                                                            'ˎύŏуˍǁȟüӉʮʂ4ɲKʺƋƝǻџӚҥ,èPԠĥŜѺѧş',
                                                                            'ƎԏƁɮӕΙĕƅÃʻɎҘԌЭɓȠȂəȡƊƄ,ƅš˨ԢÙεȩɷ',
                                                                            'έɣƞʝЛӯɄɧǸĿ˳Ͷ\x85ґɡ¯}ҺɺȚ\x8bȤ\x98рĨrϜʧ\xad¼',
                                                                            'ϯƕùľПȢy¡ʈӟаçǛЈƍƜΧӨҴѠŞ\x86\xad:ӡЇåЪеҦ',
                                                                            'ȎǾÂɜŹхzɺћϫȱȗóR\u0381ƔЦɊĿŽɍԢōʌЮƸФʑí҃',
                                                                            'ӑργϳѩʡÅλȓɥǼӼȔϤȓǹ˓ſȮԫѸӇͶLϲҗřѵπÐ',
                                                                            'ёƗИư\x8aӖԄĦĿЅțΝæƜΛĸʒЦ\x99ɭʖpɻ_ÁʃϮɎôb',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӘQ\x81ҌѭЀʡɸʫӭӿƠԭÝ²ɱϞȯÍѾҵкŀÄxҢчƄ@Ҵ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210944.982261:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Δ/ġԌӺʽΨЭѰΖǲȇĆѺǑͻĪҵϺΈʐўŊ\x9bӲ˲ĽϤϕǳ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3909697306114078417,
                                                    },
                                    },
                            {
                                        'name': 'ƀŝTǫȎόľ҉ӢΕύ\x7fΰѮҫāÅΙεʆƳ¤',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӣԄ\x96нʗˀ˧ŭɵ\x80-<®ԍĥüĝж҃ҷͼΫӗ¨яҀԋŊ\x7fΣ',
                                                                            'ҎϘӑԐ½êͽԈӮÔú\x94ӵʆ˽ǥάÉÇʌΨɌϽіȭѧɣųîǭ',
                                                                            '0җњНmԁӽĞͻƤğǉ\x97ԟƉĖɲˋԧԈȻѢɊ\x80ѰĒ+õКН',
                                                                            ';гƛ±\x9eϸvaӈӷŀŕ҇ӰΩ\x8cҩȪŊĠǍHÁšɿʵcҖŋ҃',
                                                                            '\u03a2ͷҤŪΫȕÉĚҸѓĞʜѱċγѐyŽϬʚόȡǮɑƸĳήŷǍƵ',
                                                                            'ǽĒ«ğĐǨĮПʾĹʺŎӗ\x85À¨ˮÑƶҟʪҐȁ˪ƑƈΖǩЁƬ',
                                                                            '\u0378Ⱥ×xÇЏė\u0380Ɉě*ЪʻтǧϨǐЙ ¹ɚʹӨԕœМŋӧ΅Ȅ',
                                                                            'Źè3ȉį˭¨ŎŶ´yȕɑȣϯƴɜƪԖϧǬ³\x88Ъҕʏʫkȣǭ',
                                                                            'ɥќ?ΝLŸ˽˔ΗÎʬƈž҉ġǋǭǱ\x91ƅ˔ȁWɝԤȁFԟǼ˕',
                                                                            'DҺΫêǿƉáņʯёԫ\x8d7ǻ˻βśɎ·1õƕ;ɼ˓ЗČӒʙĈ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ùĪʐѝ¨ŃȾàцƋîŹʩĢȗQΨӜNĀBДʾɔɠͻ\x9bUǙγ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'aǌëĳԂӦǹÃѓˡ\u038dʜһãάɐŞϸӺËҠԂ˖˵ӒőЕʧǑ^',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:210945.779030:+0000',
                                                                            '20220526:210945.806689:+0000',
                                                                            '20220526:210945.836134:+0000',
                                                                            '20220526:210945.869138:+0000',
                                                                            '20220526:210945.904512:+0000',
                                                                            '20220526:210945.937236:+0000',
                                                                            '20220526:210945.964087:+0000',
                                                                            '20220526:210945.994297:+0000',
                                                                            '20220526:210946.019690:+0000',
                                                                            '20220526:210946.063064:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʼƽǌʇ+ϥ\u038bŌʝǳƟ˘ʹΠ¨ԍ҅Ū:ξћΕȴĉϢoàɫ&ӊ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĎŴԍмӑʳ˭Œ\u0380ԜŮ˱Ԡɹ˔ʌƀåʈйÙǑŌȧ˜@Ɯfʧ\x7f',
                                                    },
                                    },
                            {
                                        'name': 'ԕŻλρŘґӯ\x9e˼ȀΠІ\u0382Ŋɘ\u0382äŞǙŬҐϓǧh˥΅ǹһƔӆ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 416152.59572074085,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƆȩŎŶǹȎŉɚʷŶǷТӝ͵ůӎԂӲү\x8cľ¬ǓΚǷД˓ǩҡќ',
                    'message': 'āцƁő\x98ĺˤ\u038dáɻĉәîЦƏơҔɩ΄ɨƼȓȵԇΒ]ƚļҷҶ',
                    'arguments': [
                            {
                                        'name': '×ńұȮœԌɀƲǞˎ˾wӫήͿËɐǜ±ѝРǱ³ГɊ¸ˏÍĤϲ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            101026.24732258549,
                                                                            763174.5692603488,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǻʑ¿Ćҳ*ȈќʓŀɎɰ$ɨÝΟÃʚϏΐӄȰʘͼЌҼ˘öБĦ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4023057859741612893,
                                                    },
                                    },
                            {
                                        'name': 'ǼźŁπȸЃҊ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210946.874637:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ІԥοƵǀʙȒÁȿӚȶͷ˒\x89ΡӜσωʅȍѕ϶ӀƅǅŵҀБϋ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5358544876476363904,
                                                    },
                                    },
                            {
                                        'name': 'ӺϔſʙӃȫş',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɗËϡҜj¹˂źқӹʉЖӠϜԠSƁ\u03a2gϽѭ˃ǗĞǋ?\u0379sδɃ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -351638659131253810,
                                                                            8520064194127673711,
                                                                            -4297983280239024137,
                                                                            2188476519522779454,
                                                                            -430049764109853178,
                                                                            -3868599504715414852,
                                                                            -6415987864919451247,
                                                                            -1384025607526818235,
                                                                            6086540995933409996,
                                                                            135285094462179760,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӐϽˋˬūӭʔɃĿΑшǋWЎʴԗԖϠњ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            970016.4069640767,
                                                                            612670.5756010992,
                                                                            88741.75237350201,
                                                                            37709.41916686113,
                                                                            222578.60667943757,
                                                                            1011.819463003063,
                                                                            473129.43461724336,
                                                                            393394.5418902132,
                                                                            958854.0790255852,
                                                                            730271.4466529827,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'μ\u03a2Ê,ҁëβӣÖŧʲɹʴ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 66376.7422925792,
                                                    },
                                    },
                            {
                                        'name': 'Ǐ˴γƵɴđˢұzҫ˲˟Î',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'GŠǓ\x8cĸȌʫйϳήБèν\\ǿʏƟŶãɏчƅϞfƛÛªҝʡѲ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2425583077770508943,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Jӽ¸ʉђ΄ʳӼƀϠŐϑΗTϑŠʁČӊ\x87ϪԑąƶʙǪʪéʲħ',
                    'message': 'ûΤˌГ[ȣʅŐӯԑϤǓӰć\x9eǗ¥\x94ŶʦƋЀıнÏԥąѫѿĆ',
                    'arguments': [
                            {
                                        'name': 'ћĝѷÉΩȐç\x81ʚËΠ)ԔοҪҲӦÒѻɎҤ®ʚйӔȄ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǝ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϺǰƶòӝwFɆ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:210949.534978:+0000',
                                                                            '20220526:210949.555842:+0000',
                                                                            '20220526:210949.576264:+0000',
                                                                            '20220526:210949.599139:+0000',
                                                                            '20220526:210949.624577:+0000',
                                                                            '20220526:210949.651052:+0000',
                                                                            '20220526:210949.689767:+0000',
                                                                            '20220526:210949.715246:+0000',
                                                                            '20220526:210949.743160:+0000',
                                                                            '20220526:210949.764841:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ðИř˴3ȘҨԙǸ˃ɗ҂ĭÙФŪȚҽǌӚ£ӈþϕɡŤ͵Ќʨ\u038d',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:210949.883097:+0000',
                                                                            '20220526:210949.905234:+0000',
                                                                            '20220526:210949.928169:+0000',
                                                                            '20220526:210949.950353:+0000',
                                                                            '20220526:210949.974587:+0000',
                                                                            '20220526:210949.995209:+0000',
                                                                            '20220526:210950.019067:+0000',
                                                                            '20220526:210950.042403:+0000',
                                                                            '20220526:210950.068487:+0000',
                                                                            '20220526:210950.094578:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʯϗΑЧԄ˸òËʑʻĐԄξĕ°сmÖтέĨ°àāe˒ɷЭɤӈ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ԩ˦0Ѵɩ˃ΡφƆ3ÿ¶ƛˑԨʶŤ\x9bǷѷ\x9d«ƕ2ȎȳĀΡ\x87ԣ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʝɘЛϽ\x90ċdѓ}xþԌǉĩц\x850хưȥˆϨЦƞѶ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            444491.61469055014,
                                                                            25640.852949904845,
                                                                            166746.00436429295,
                                                                            789555.0804908593,
                                                                            -16025.01971201021,
                                                                            311332.77587086614,
                                                                            550069.3874425086,
                                                                            686047.7699919838,
                                                                            639050.2361073726,
                                                                            931319.6586850076,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǍʤƣТЂÌʳʚϊŊΦɤίť˯ԥěʫʯҁɖ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            822934.0061568372,
                                                                            877625.23159776,
                                                                            966627.9449763403,
                                                                            993997.2311931215,
                                                                            739233.0979757261,
                                                                            315913.5557275456,
                                                                            634569.6179300421,
                                                                            233519.11985182425,
                                                                            208603.88618216902,
                                                                            857670.5880010437,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ħұЁīLρ\x88ЯǓ˟ϲϕϳ˄фƗϒ˅˲ŌʢǂĵƧЊσͶʋʾ³',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3865806216791597461,
                                                                            -3839565548340813863,
                                                                            7574856538839939701,
                                                                            -3872455881899290509,
                                                                            8216766310227718311,
                                                                            4174059993437196418,
                                                                            -7254879165952181344,
                                                                            1792048463204555183,
                                                                            -6158159601551230502,
                                                                            -6186385205361318365,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɰҞŐѦğ%Şɭǈ˙ȟʰυƨūѴɯӲƙɥǫğ¦ҐŖдìԈԝґ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6710365870146277797,
                                                                            845837209897310283,
                                                                            -228211336127897189,
                                                                            -7614878991695942040,
                                                                            6951380334077672245,
                                                                            -6311875266419299595,
                                                                            -2512769616290464236,
                                                                            -7683436112136915416,
                                                                            -3503161439275745171,
                                                                            2184251990364462366,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŔńЉǡȚƕUǲӚ´ĕ¼ƬƻºΒѩӥĶҡ˷ͿɡӞѪĺјϫϧЯ',
                    'message': 'Ӣϒͼĺ˚ʏ˶ϩŝͰIG\x90λèǃΫҸҵӲä¯ǞҠмāǼΖDͽ',
                    'arguments': [
                            {
                                        'name': ')˼ӘʉªɻӝC¯ǥҏƳҶˋѓȦѵ8ϭȬҡeôԈʛɔɰʀӦӜ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:210951.954667:+0000',
                                                                            '20220526:210951.987255:+0000',
                                                                            '20220526:210952.015177:+0000',
                                                                            '20220526:210952.038098:+0000',
                                                                            '20220526:210952.058875:+0000',
                                                                            '20220526:210952.078945:+0000',
                                                                            '20220526:210952.104686:+0000',
                                                                            '20220526:210952.136287:+0000',
                                                                            '20220526:210952.163332:+0000',
                                                                            '20220526:210952.187176:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Æː¦ǝbȺŜñJԭɞӿϩˈʔġŻȦŞĠѐ_ʬяϘʽǀƭŏѧ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ɇӛ\x91ϨѴƴ¦ѐȚ˓ΤŠȠƭӌǹƨĤ\xadσęǡɾĽɐ\x93\x99ʖΆʵ',
                                                                            'Șʒŋέ\x9bɨӿŨΙǏԌԄɚǊ˕ѵ͵ӤQħѴǬɥ҉Ĕӻτę\x80ѓ',
                                                                            'ҡÍSƕ\x89ΝєǱĿȵҔÿѡҞɳӸ˭ϓÿѰάėйωʘƺN(Öќ',
                                                                            'ӿȽԆ˼Йʖ΅˴\x86ЅҊǑȟǯӢ˕;оԥє˝\\ʎͲϠɍȑҐӶҒ',
                                                                            'Ł˗ԑӦą\x9dѪҥƖů˕˕ͽǞ\u0383ɹӝϬǹКrԧ$ɯŚǥ ԡɲ\x81',
                                                                            'ЄWɇϤΩÉΗӅɵI6ÜřЅҌѮËԮҀpΓʽԨҚЧɎˑЄk<',
                                                                            'Я\x86ЦίǠԈFĪȔƕńϜɉƭЮ˩ȡʂħждҤөǶlш«kҩΠ',
                                                                            '³ƹφдǛЫû!ɻӿ҆:ɕůʾȼɗZėĄλmɓ˥ʸǉӽϊοӤ',
                                                                            'ʿƯԤǄΔΓҀºʷʢ͵Ҏ;ѧÏ˹˅ÊȗĊ³9ȼ҇ñчсɷȍĄ',
                                                                            'ʗǗǰƠɟԡΤƗőзȍȰӿɈаɞҙ£}ѠŃ\u0379ӣ˕ŊŜƲ˕ÔЅ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˠ˃ȳώĐ΄ǟԄѰԎȬđ5ϔΩх',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            724179.5166263586,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԁȕĺ\u0379ˈ˯ѮƅҍʫЗʹɇŽЉСʀʮƣ¢˥sԕη¤ϼƍǝƯ©',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʏεӛaRѮѪŻҐӏƕԊөΛªȗIԓΫMԧѓԘãϾ²RǞˣğ',
                                                                            'ѻΦҪρõӠŪѕϮЬȖʕ\x89ɩϡ¤˞ǗҰ·җӛԈЄ¿˖ôÄŊǥ',
                                                                            'ˀԗȲʏhԆ҄ȔɵкkϋɤͰ¥șûυΗËʤҎ\x87ξӪſχǻƶГ',
                                                                            'ӭ5[Ň<ŝ·Ɠ¹ŚԛþПġ\x8b±˟BŋǶʟǭÕȓΆŹāӴ˧ȟ',
                                                                            'ɠӂϠǍϏŜżӒǴɨǙƂО!˻ΨǡȟƑ/eʦǬȫǬ:žө¡Ä',
                                                                            'ΌԙϚƳŒҿ!Ԕňӆϖơɴʈȋȇb=Ǚ§ӿƌǏѫȋˋ¦м$ˑ',
                                                                            'ΨҍЪȒÂəΛЕκǴĵ\x89ҁғœƸțԫŉȽǼ_ӎǈӨϞХӤԃ\x9d',
                                                                            'ϨӰʛ½ȬҺІѻɅſśQĤԪѓǂϯҟ¤\x9aԝыНҍϰƂʤɳĹƨ',
                                                                            'ϩшʥ\\½ҲǳԣȳɘÊЎɀǃɮҺ¹χȾӅȻʽаіǫ·;Šцƴ',
                                                                            'ŠĈnӊӫλɰʉĿƪǣ˗¹cɽ˄\x8fȀγЭǬĜƫλ±¥ƮsƱˢ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɘҫĂΚтѦřӡʐ҆ķҟӍ\u03a2˅˞ö˼J',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': '6ǻԑģɞʤͷɯ҈ԩРdϲǰȺИÊӲCȈ˺ſҙúɖћ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5381015916378114715,
                                                                            1546861883145123949,
                                                                            -5145350358958686137,
                                                                            7188092331874549463,
                                                                            -5910856826190690878,
                                                                            8398923139164685814,
                                                                            -2214427813627770006,
                                                                            4086031820729545927,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'œŐ\x9aϕưǍӸɹŨѱɼҽʩō0ƹ\x92ҐßEӿǫϦ˸ҤțҲ˺ȷς',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 918620.3651922209,
                                                    },
                                    },
                            {
                                        'name': 'Ҽǵλʔɵ³ʻԜѭɤzӑƴȒãàſɫˑӥҾȾ˂ΎќȩρǦÏӷ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ĥüŀjŧЗ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7590837933501714081,
                                                    },
                                    },
                            {
                                        'name': 'αɦ',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'θ˕ǓȠĚβŦƺӺˤīδǀʹȿҾӅ˃ԑ\x9fʴƫdӦ?ϗФԆZԜ',
                    'message': 'éӒӁʚӚŊȚƉ6ȉ>Ăԝ\x91ҧмέǳϭʎŬ§ƫӳåŞƒӆτʤ',
                    'arguments': [
                            {
                                        'name': '*Εğ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:210954.705833:+0000',
                                                                            '20220526:210954.731049:+0000',
                                                                            '20220526:210954.754693:+0000',
                                                                            '20220526:210954.798534:+0000',
                                                                            '20220526:210954.827264:+0000',
                                                                            '20220526:210954.861726:+0000',
                                                                            '20220526:210954.892682:+0000',
                                                                            '20220526:210954.917610:+0000',
                                                                            '20220526:210954.944841:+0000',
                                                                            '20220526:210954.984914:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɓˎĔɝÓϐ\x7f"Ƙɣ҇ϣΕŇͱ҉ďŵА˚¹×',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            678584.3164314191,
                                                                            512864.36848117306,
                                                                            264748.4932554013,
                                                                            -57150.57734040023,
                                                                            109110.9111982125,
                                                                            -12570.174345674212,
                                                                            413580.00181603176,
                                                                            161859.93058402452,
                                                                            707202.9588624188,
                                                                            567089.0454535191,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ě8ɉκΩӼŰɴǚӥ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                                    },
                            {
                                        'name': 'Ŀ2еʿ˨ȟˌǘҙΨíυ˥',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210955.937652:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ԅ§ƅˢӠɛEñĔñԏGζÎ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210956.058695:+0000',
                                                    },
                                    },
                            {
                                        'name': '˸˹ҋşЫĔӀˑ҆\x82ԚzſŖɛƒɥȪBϽƺƳȽŰƌԄԦɑԚӱ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ɯǁ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ʱ˒',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2210553682692301157,
                                                                            -4919006050506900251,
                                                                            1125065934902763456,
                                                                            -2651814252943133509,
                                                                            5862244364836585402,
                                                                            -4057595142599808027,
                                                                            -6686453167871997052,
                                                                            3709458827777148369,
                                                                            -8060212227803069948,
                                                                            1938780107204572682,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͷȞĨǵѕˌQ·ΗҪƁ¾ËʨÔʌϒϪУŖ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ϘɊȸΜЂ&ǘǣƂ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -9061261632425442062,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϞПӺϻθǞŵӡˀF˭ǡ|ŌʮГ×Ԓʴ\x91өԎ\x81ƳÞʩѵ\u0383ƎΤ',
                    'message': '¬˄ȕʨμȠɣ˱ƞάŌӍΨԢɹ¾ɔЄԫҹȖĚΚ\x95ӏ\x87Ƙѫʂø',
                    'arguments': [
                            {
                                        'name': 'ĚĂЁӼĶ˞§ïfɂНЋȼԝ˵\u0379Ԯ҈Ÿ˫ԗ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:210956.998005:+0000',
                                                                            '20220526:210957.020633:+0000',
                                                                            '20220526:210957.041698:+0000',
                                                                            '20220526:210957.066107:+0000',
                                                                            '20220526:210957.087143:+0000',
                                                                            '20220526:210957.108639:+0000',
                                                                            '20220526:210957.130240:+0000',
                                                                            '20220526:210957.152320:+0000',
                                                                            '20220526:210957.172876:+0000',
                                                                            '20220526:210957.193896:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԃӴɘèŃʌòƿȍʂŰëŨа^ȢУ\x93ũΞъɘǆѥˌΞ˛ŗƠă',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': 'ÖʟԑSАͼ[ϛƴҎƦǃȱ˃ɫϧHʳǯȢŇǩԚ\x85ϲȈÝї',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 757630.3526096557,
                                                    },
                                    },
                            {
                                        'name': 'ƯБ˔ͱ\x8eˈӆ:УϽƺÚҋ\u038bǨ˺ĴŮМ˙ˬÊɤuǻˠʥΖɬĆ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѹɰįҀëɪҺиr\xa0ÜǯÊȶĆĖѰНȓϵͼСͼӺˊ]Ҭӫқʂ',
                                                    },
                                    },
                            {
                                        'name': 'ȼŃίюЖʢіы',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210957.771930:+0000',
                                                    },
                                    },
                            {
                                        'name': '˘ƣƛǳҫμÜǾxҨĺðÇSʇτԆ˔ŗŖԡǒĨӷ\u038dԧɡєď¹',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210957.856235:+0000',
                                                    },
                                    },
                            {
                                        'name': '!ơΒҽȉ§ĭǤÑ˄ʾ˄ĽrȌ_ʔʼŧϕƉɳĻνɕĉɲp',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '®ϔҜҴѨúǭѿƲνȳ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -47502.67478823826,
                                                    },
                                    },
                            {
                                        'name': "϶ԫ3ɒ\x9aˈƖ˒Ѵˢ'Ȅ\x84Ƞ϶ďӴѳѭο}ѸϣʷAťԮ÷ƢW",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7694881954928710131,
                                                                            3917402464321785503,
                                                                            2205812836739057658,
                                                                            1754229669163567024,
                                                                            7985627129362896967,
                                                                            3550823911202480563,
                                                                            -6279274852494377072,
                                                                            -25013515609677606,
                                                                            -3245887591363475519,
                                                                            -4995733547753381899,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˞ʕԪөÌӺžȝЏǥʽǜ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʩhӃɇХФҩɈȍɛҌwǒƉӇʚŭýшЙϬşȋ±\u0383Ϡѹ˶ˤŲ',
                    'message': '\u0381xҁΧ\x81ΎǣұĞ~ҰȍϋǒQϒè¿ʆ˰ɡυÂ;ϷźӔȗˎϤ',
                    'arguments': [
                            {
                                        'name': 'ѺžTµȕɦӓǒî϶ƾƬòɃYЫӅҔˆʑëσԟĴ½\x93ΚŅƼЌ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4466280813820136501,
                                                                            5122887675999354927,
                                                                            -877204329527394274,
                                                                            1801286736832002043,
                                                                            1932361162229225527,
                                                                            -6095312579097008992,
                                                                            5249973276377874870,
                                                                            6432663642887330541,
                                                                            -58627445587114736,
                                                                            -6247822871109351625,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '"ɳϷġŭĽԙҒjɞǻЁêŅƻƪԌĐӵȈȐ\x96ƙʝȢȣΩ\xa0Ŀ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 825688.8217577904,
                                                    },
                                    },
                            {
                                        'name': 'Ȃ˴ԘΏę«ĿԩʬşǹȝӾԉhϚʺЁ!ǹ˽',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ЭɃĂͽěʚɇϝăȣЛӮ¿ӣӹ˹ӺРЦĲʳКĥƷ;ʖíёȆΊ',
                                                    },
                                    },
                            {
                                        'name': '\x8cӭѨÕжʗѩŋĮȆçӖО\x8fѕȅԁ\x82ˉ˄ăȺɅȖŵƾÚÇíȕ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'nķ\x88ʶǃʈQƉюˮͶЩҬɂ\xa0ƧΔʙπКӓӵʿ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': 'ǤдɯFϡϏăʺ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210959.658219:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ˢ˹ĠӎѮ˩ЄǸɩĠÀɗɇɈϡɯԟҙĠ΅ҚbИѲ΅ɆҀ˲ВҎ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210959.744445:+0000',
                                                    },
                                    },
                            {
                                        'name': 'űƝȭûĵ˞ƆʟȾ˔ΖȈĊʔaʑŀÔы®\x81ʐ2ϴʽ\x8fΕӔȻЮ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210959.829114:+0000',
                                                    },
                                    },
                            {
                                        'name': '1҅ЄŇɯ¶ƖIӴԌ\x92˨ӥˬþҫà¸ȁŻȔĲϊʻΎ҉ǂ\x84Øμ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'gŐ°˙ѪПэVGˊ;ĺāү˔ӵ\x8cǦ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            9027886138257681333,
                                                                            63840522011788196,
                                                                            4736064167997509212,
                                                                            -1170986657412748969,
                                                                            6401577098603720778,
                                                                            -3453205730828691422,
                                                                            -7541411441235030483,
                                                                            2450089020603448786,
                                                                            -1161231858794215038,
                                                                            -9013395463472005372,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˓ͶҫƕӗɕüǵǘƢèP®ǃΑčȐïѾΪђĀʞɗΠЦƤ\x7fĨԘ',
                    'message': 'ѝ.ԁŜƗŗʐÓčвVŌŘ҉ɒŹоƮʅԤӧÎ\x8d9@ɍ=ѿ\u0378ȝ',
                    'arguments': [
                            {
                                        'name': 'ʶŅҽʼρĴʧҎҁΈ1ɋǖοѳ¥ʮĜѮѧ˳Ѹ\x7fкÁ§˾ȏƶο',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 916877.3891432411,
                                                    },
                                    },
                            {
                                        'name': 'Ϻ¼W\x84',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            596120.2659687271,
                                                                            780338.0096929553,
                                                                            846382.8196648594,
                                                                            961702.427924416,
                                                                            -6689.009763411319,
                                                                            423078.89317882416,
                                                                            467867.6700837243,
                                                                            73629.39430570698,
                                                                            -44310.91871038444,
                                                                            180612.18798665667,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'аˇȎ®ǦϽǼӲ˚ʮԨӱɑЭpÓʂθɵɒХʷǴǃƏÃε\u0382М˳',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211000.987896:+0000',
                                                                            '20220526:211001.008817:+0000',
                                                                            '20220526:211001.029400:+0000',
                                                                            '20220526:211001.049797:+0000',
                                                                            '20220526:211001.071807:+0000',
                                                                            '20220526:211001.094810:+0000',
                                                                            '20220526:211001.120689:+0000',
                                                                            '20220526:211001.141294:+0000',
                                                                            '20220526:211001.162047:+0000',
                                                                            '20220526:211001.182617:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'īΩµɊǅȉїЦѢ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ːȕʴКҨʾПҤƱѥŝ®ʋʅøȑЈΐф-ϑҠưDϜfɤ,рӳ',
                                                                            "іЊ¿ǜ9ϣԏвǸόѤȮȴFϩЂ˳ʘƿÛÄѧ˛ş'ʿǬǴԨğ",
                                                                            '˝ΛŇѷп\x88ԘѾƌɳӖ×ΤσąȭƥѨǋа*ǶɈƓǩ\x9fƙ¶BÃ',
                                                                            '\x88ƫj\x7f\x9dʡιҌɢɼƕҧ˶˔ѬˏțbԆäůϞɩ<ǺɛɸʐьƎ',
                                                                            'Ҿ\x89ϜҠǑ¦͵ΏSǙΞɲӺǝӣэɱ˧ӼѱϹԛЎˊʀȉӋɀʠ\\',
                                                                            'ÉɛήǓiɊčɆǄǆϙȻ/ʽň˼иӘΔå\x82ӞԗŃȗЛˊâǛλ',
                                                                            'Sʇʔ˺ƀǔȦ˵įϭ˛ȯы{ÍԅFėхiûϬʑиɣϬζŕȒ%',
                                                                            'Ӛгӓ\\º]ϡşХǀЭŇņА$ÁȊɼ˱һрͳ҃ɕҷȰ?ȧӒƊ',
                                                                            'ˁǜԃӾŅёԞҲ\x9dй˪ǽ5ð˅ʤΜѤ˭<ԡіЖ˹ųȀцуѿʞ',
                                                                            'ŖγmƸΦѼ˹ΧǮXˑчŎУȼ˟ŦȤđɢϤʔӭ˞Ј\u0383ˈýĔю',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȕ\x96ЎȊȊêŅƱµәťͲԥҪǴъŃŉʭҮůЀʔdå',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҊȲ\x99ŬĜ?ϒӬάҐ_ͳŁˬȣҫɖȄĒ҅ȝͽПŖі\u0381>Żħύ',
                                                                            'R\x8fӓWəѨΪċƚɴŽLύ=ТԎɹYӽsĨɆiʀӼǗąӜÀx',
                                                                            'Ĉȁƈϗˑ\x8eƩƴѰπĉМǄǽȞÃҤˀǎν҇˔ԒƅҸļцÓÅɝ',
                                                                            'èӮĚĨ¬ĹԆҎίѦ\x83äӶǲӌ҂ʠюG\x81ʐ;ή]ϜҽʬˮӠ\u038d',
                                                                            'ҨƩΊǿ˨ӕŸ\x9cƲɫθˉєƙȕѲƒNʉӿɏȜӔԣˍnŞ<ÿҲ',
                                                                            'ɏȇ\x9dEʉǑ-ˁҗӊԊĘʽӇXԔòӭ˾ŗǉìǊɫɊŋƌŃĩҌ',
                                                                            'ѧԕÅǭǋ8ӂэƼΨĀɀÐҩ=ǫѐɴǨ\x93Ǖ[ʖğʃĥ\x89ϒɢŮ',
                                                                            'Ǳ˔ŢζԠćǖǘģƉЉѹҜȑзȊϐΝѢŒˊόưВǻZΘѶԉÌ',
                                                                            'ȜîNĭ*Ʒ\x91Â\x99yɂӜ%ɅcҖɩɍɆ˄м[Ԙӛ\x8báĖıǰ#',
                                                                            'ôҏɂ˫ȅтБ¦ǋ¤ӷϤƂǛ˔Ñ£ΌȺΖϙΆÄҿԧӎƴбβʯ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˏȋҡɻȹԓҁсӧϊһƁɎͷơ§ѳ\x7f',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7205393726969914405,
                                                                            -6344967982220589117,
                                                                            -8913543814125187104,
                                                                            3350295839196003989,
                                                                            7402935133999816934,
                                                                            -7938299243960381716,
                                                                            -5391087417290193280,
                                                                            6606593287484923336,
                                                                            1110014455188133321,
                                                                            -8700534024505307039,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǐƕ˚\u03a2ûʹÆɢԤԑ҂5ǡίσӑӾƲĲϵȤжΚғʊȗżɅӂμ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211002.189978:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ǜ\u0379ůиѯɷDӼҮˉÎϸӽɂ˃ӓԛВ\u0378h)ʘʽ²˷јȍʨѡ~',
                    'message': 'Нҹɝ9ːŖÚü҄ӐʹɳiWo\x87|ĈϔZƘԗώ˲ΜѣγλŢӹ',
                    'arguments': [
                            {
                                        'name': 'ӊʱżǑBƄӥэȻˈŉуʭОΓʫÐƷǏ8ҊƯŀϥŠѪ·e˶С',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6664244475903790250,
                                                    },
                                    },
                            {
                                        'name': 'ĈϏͻĒíÔѕҴɉӋǖÔɱλʧӂϪ\x87',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5928317892923316548,
                                                                            3700070580895632680,
                                                                            -1325282944009354060,
                                                                            755165559798505618,
                                                                            -7705252148708064495,
                                                                            7196229637800254767,
                                                                            9121410724153191170,
                                                                            -6906220204818703493,
                                                                            6965129958389453782,
                                                                            5553527650045776304,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԅ\x8bѽОeӉ¼цſˍĎȹũ?јЅŅ˳ɳЦƤҎȾĜЦɆɹǘŶĠ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȓ&ԒɨӬʥʽʲƝϠӸĲω',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6698720561244104341,
                                                                            -428681471507018277,
                                                                            -2411161676518760136,
                                                                            -8384496112246288551,
                                                                            -3393212354688612630,
                                                                            -5984406719438519540,
                                                                            -6411046542131245062,
                                                                            -9156059401758476238,
                                                                            8085938374446355130,
                                                                            -3309532192203471167,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɐϘӆҚ\x85Zv',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2200763137100638011,
                                                    },
                                    },
                            {
                                        'name': 'Ѵ`įĂȲãÃюǉҽȀ?ûΥѡD±ƨ§Зȍʻ?ǲaʑəÉӧƇ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            486090.4818897005,
                                                                            352763.9726699177,
                                                                            863201.702480649,
                                                                            -82580.815077045,
                                                                            917774.6002608413,
                                                                            358030.91627730895,
                                                                            891191.630821607,
                                                                            332787.9900188552,
                                                                            882196.6669857844,
                                                                            303965.6693944564,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǲȪǴǖʇ\u038dƷCǿӈƟѻƛЊӴǀƞϹâʥťЁӉʹԛҜ\x97Ԉδғ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǁϦϮſɲ6Ɩ҃ȷǙ\x8aǾԟҐФ\x81ôќsĬΣĶlѫʶ§ε˨9з',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 357149.23021003656,
                                                    },
                                    },
                            {
                                        'name': 'TҲɭӹνʷ\x979ŘЙʨʖ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 911260.9290345799,
                                                    },
                                    },
                            {
                                        'name': 'Çmȵ҆Ε¢Ҽ\x860ԃPʊƕz',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1462457606230560114,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʉ;ØιϭɂǆȈȯNUƩˁħΡЂuԞţÕÐĸщӦŖƚДfϛϞ',
                    'message': 'ҳŐßŮ«œǛ>ùƂ0˦Шț\\ÓЏYѭʓǇǴŅĆ\x9eсÙʛѠ\x91',
                    'arguments': [
                            {
                                        'name': 'sˌȁƾΘӋǑȸӼțʺ*ƵԬƓÙЉŘӼɒАƘ˒ºǊϲԩȯͰŜ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8605354608225546918,
                                                    },
                                    },
                            {
                                        'name': 'ϽšΚ\x86͵\x9aƲYоɃ³ƢԭӝРΎϕuҗѻӻƅϗǝԡһԦŃӉƓ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            586455.5844304921,
                                                                            832703.931604506,
                                                                            993556.539998698,
                                                                            358426.3888628442,
                                                                            838406.9530617328,
                                                                            117124.74433828515,
                                                                            243549.93257400807,
                                                                            156739.29369088844,
                                                                            886513.5175832841,
                                                                            190113.99442822544,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӈʇԦʐ\u0378\x91Ńÿ=зҸɥGʰIǣȀˇŬ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7994605893609285097,
                                                    },
                                    },
                            {
                                        'name': 'ԌИӄİɿ»ËǃƯҕɜǑҞЅ\x8aҔԜЖ˃ɽɟȪȬ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            548295.8039331419,
                                                                            154425.59847249096,
                                                                            -3801.693662017875,
                                                                            327516.4781692447,
                                                                            205329.02535541856,
                                                                            609329.3066141935,
                                                                            313494.4357527747,
                                                                            52381.47673830151,
                                                                            341209.57296246657,
                                                                            316032.27175680926,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӢĲȗ˴¤5ʞ%È˰ӥʎ\x95\x9c&ЬҟʉˉшĲыϧʭl¥ΙñȎ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȯʈ»҆ˣ˖΅ʃоӑҲǸɬʴѻėӯɷů%ƆōˑɛҖїŖǇ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 56378.49582802731,
                                                    },
                                    },
                            {
                                        'name': 'ǾҁшӕiǼϛʒΕ\x99ЂˤԛĮҳ<ƕ\u0381ȈǨŔµѺƗǙŢĬӋſϷ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 413686.29080473894,
                                                    },
                                    },
                            {
                                        'name': '\u038bɻű\x7fҌɹȘìѦ#\xa0ǩŧßéɍʏнΏѲɍтѐ\x94ǶВǗɛұЫ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȾˮÉдȞũŬλӒÄʈȘӧơѬƏͼɅΌӣѦ÷Қ]ē˖ľǑɄԗ',
                                                    },
                                    },
                            {
                                        'name': 'ȬјűgàѥǨ\x87˾ɣϑϭӁЌʀřͱɨǥ`МʞƃѼSɼțѦԛǐ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211005.273558:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ύӽéϟ\x86ʬӧbŮÚԜΘϒɭiЏ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 776491.3392558829,
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

            'identifier': 'КȪɗчş',

            'categories': [
                'configuration',
            ],

            'messages': [
                {
                    'catalog': 'Ҩƣ',
                    'message': 'ƹ',
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
            'name': 'ęŊŔҶ\x9eƑЉWǮңɅѓԆѫӣҙ҈҂@',
            'error': {
                'identifier': 'ͼ˒ɦЁʚҤΪƳіѼƗѻ>ϴѢǔ}˳^nНȪɿ˒ČЍĖϧŎґ',
                'categories': [
                    'configuration',
                    'invalid-user-action',
                    'invalid-user-action',
                    'internal',
                    'file',
                    'file',
                    'access-restriction',
                    'access-restriction',
                    'configuration',
                    'access-restriction',
                ],
                'source': 'ìҿ˲ɟĹʶМӏпӌˑŗ˸ƭҺǡϚėѪϪΏѷuƍʥťɉƛЍ®',
                'messages': [
                    {
                            'catalog': '˘ƳӐαχ±ǭ\x8cˍö˄ʤ2ˋԦÉʿҔ˅\x94ϝ>МˤǪ\x91˸ҟęÜ',
                            'message': 'ĕÂĭƘGÁ¹ʅҎҘӃѝю¶˵ɴЫ˞iЂĠÉʞɺԁŲϛĀʭͻ',
                            'arguments': [
                                        {
                                                        'name': 'ȫɷɛΩĈԁҸģΑ϶Ļѵ}ɾҍӀĆѦ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԏ\x95ĽҰς÷ԒʤʿϖəСɞҐԕĉҖɡЯϋɀȺӕȨUʌԗ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƅυ+\x8cǽѣ\x8eɪǣĎʿԗʱ\x90ϭuŞӿřȯϷǸ[ȮЈëӼƥҚá',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '΅ΦψʊƈΖϮŌƌǛıρͷ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӥΜšӾǅПϤǪԨжϡɚŤˡUӔˁͳϡ\x8eıΎʟ˸ǬɁԪ˹ӯӟ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҀϓĻȢÛϔȐҬ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϴƙʿϴϱϣԂ[Ǧşϓщ\x99ӽƀŮɝӀƺɈþɂȖК',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ËɘʞφƣǼ҄ēŔBɓƕ_\u0380ӏǣġЃˬͷҜљɳ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӯԤʺɟÃ϶Ʃyʻϐш˄ԋȋȇтµȇӁƆʚ˼èİϽŹŲPŨˎ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ùϟ<Ԇ\x9dӏӣȆǑ\x80WǫŋǡśϳλѻԘΟ\x94҇ĊŎέūѯÆ\x80˚',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϴmϼɤř"ɇüҞԓ°ŏįƥ҄˒\u0382ѱ˯ʻƓӧŃαϋûвŘӦe',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\u0383oԀɊ`ö1ʠVҿ˚oǖ',
                            'message': 'Ȃû5ȬɗʃİϓϺӻәP;ɝцȈѾÛîγƙȈ²ŉӹƋϫjǒÍ',
                            'arguments': [
                                        {
                                                        'name': 'ăbϜ҇',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3838703524871822538,
                                                                        },
                                                    },
                                        {
                                                        'name': 'шȣοȧƭӾԎǢȓԅ˨ʞɔȀ˲ҙʚнʰ͵',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǆȈӉOĒƇҒǀR҈\x7fǮɣɐΚȎĒɠˣӷҕϦ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҺӛǠШǰȯɱπř\x91ǪѭYů¥ŪЍɦȕǽ˲ȓȒ¶ʿ˻(ӡϷƂ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 273030.048456609,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ʋȟŧåʵӄӿɂ˅ӔǧǫȼѹyɻȡŹñЈΡãÂӜƬΟʸӆ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5383678695421529914,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Єɵɞįǜ£ŖΈӓäҾϦȿɑƗӧҬƩɵΩ\x83¿ƌѯѸЉΘˀԖȍ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ôȗʲ\x87ɯќ\x89ӯ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0379ĩȰӇ\x89νE¹ӒŎ·ˁԛ[ӈŏӤ1Ěɵҕ\x83ӟħŅȰΈ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1807673958122692331,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȃӻβ\x97ǀªƹɑƏƲҔѼоГȫӌɎ\x9eҌͷʨȌĦ·ҽ+ˈƨҦͰ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 53076.19808107501,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ьʉƀѶϸџz\x81ȯʒ8ƭСʪ\\DΰӿȔ¾ЄR',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ґʬūɍǟӣ˩\x8bЍǠȏøιн:ɼʍԓƓwɊ˼½ı҉öʟѾęɶ',
                            'message': '=ЪöƑΩӽĜȳÂďȉĶɾʅ\u0383ё\x86\x96ͲǢσĽλˁ\u038bӖŹơʪȇ',
                            'arguments': [
                                        {
                                                        'name': 'ǃӠ\x84\u0378őʇφ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʪԎńTǉϴʸҚƤԃҡ!Ɂԕ1Đ"ƃѨӣɚӹ<ХӰȧɟǤϳĜ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ф',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1964088222037940604,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԮуҶЅ\x8aРϨåЕϤƦį¤ǚ;ӔҲϟќɺʃƨӠ°ƧɮԢ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'eћ-ŋƯϖɼҦ3ғ»śƮ²ś§оŭºĂΉŢĤÏRƨЮəϏб',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǂԊӆÓĲԝģƧͶƂʴ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˡA¦ːȔΧɟWѣϷ+ÿΠԝʏÛˑđʶȴѺΪʂϸϩʷɡӮӢ҈',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʒΆŜұĬʏúǗА\x88ΙśȱùĈǼȕ\x90ӆtʘŒЖȗӳƀƝѩȡԉ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЅɪƲϻȇȩΈĆƴ\u0383ƶZԂϿэſnНʫшĨЧ˒\x87ǖŽѭҙˑ˾',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӥȝªìȢĦǶǥȒ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԫ1æÓϨ\x80ƫư˪УʠƗǅ˨Ŀț:Ҙɪ˩ŽϴȣěЕѴˏȈŚǶ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 473312.7402408314,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɵĔԠͻϩ Îd҇ΏͻӰԋҽǵđϙƦЗƏľԑѫємɻЉƄҫѝ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 166404.06852804247,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɎɫĊ\x88ԃӾϒԉ\x99˦ŦԆΣϠãϐɄɚƴē˕ήёêȄԦǑǲϨ/',
                            'message': 'Ҽ˲\x99ʫǰЫËЍΡ˕\x83˰ϜӴnŞ˴ǖ©ɻєГϗÉǫǟΆɊΊӟ',
                            'arguments': [
                                        {
                                                        'name': 'űԫĿǴøас˯˸Xɏͼĳ\u0382˸ȨŰӸπˣˢĺ§ѫ2Ëϣɶя+',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʭЫάÃӢҶȱԝ"оԐċˡǝϟЧΕȺ˖ȯ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'țЩűҍȎΠǇЈ·DǀΦϺϖĳþYЪ˯',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƺƘȡVͼχԦȅŧϿμʤɹ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҷŜәɺŻʋʄЎʈȬɖłǕōϟǇKõƛ\u0382TҥѬɘîN1аϡΚ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȟ˧ϺґèʚРɱŵ҅ҋԟªБҮĭĚėļǆxʃȾѷα,ȳɠ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'cȎǥȖȔӀѤƹɔҊҗćuтȗ2˸ҧҋǢԓξƮč˽\u03a2ɣƠËM',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŔĹ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'лʏŉȄ,ď˞ѨÅȋȳŵрˮӂˡэóɇӘ3sƇǦх¥pϼk¸',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѬĉŁāͲʿˬͺɳԍͳӧФЀ5˒XˌеϒДŀŔяąϷ¯dǏƩ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'MôģǎċӢԑÃțϭӺĩǶ_ЂǤ/',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:210935.463586:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'æ<ƏӞͶ¸ёǀˁəҤqūȏĴϤƂʨˊŪɑҴʩj\\ӕϟ\x7fХȒ',
                            'message': 'ƹҲ+ÒњҜàΝdɸҴɯϟǅɦƱĕɧӑжəÆƁĀїԑѽÅGǪ',
                            'arguments': [
                                        {
                                                        'name': 'ӝȽӁwǢёöқѫªűɂFЁ;9ԢÐӎàȁԞŮ^uȻʕԖϪ˴',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȑ¸â\x89§ǵӦćʇɔѬ\x8dɁɢ\x82ɄɞѡȒӂǟ*Уф',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:210935.796277:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӥ]ɏèζŧ\x89ӥÄѾŔŧÓгɁө\x82ѱȑўϑнҐԃϭ҄ǽĹƌͲ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˤԀгΉ9ψɐŻǲ҉МÆπпŚϦę+˱ҳԕɋχǷʪƠϔNr\x86',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ÿ\x8dԡԐƖÜҒ\x82ԋѾȻ˔ȪɌěʾНΏɣ\x9c¦nώ;ԛ\x8eǧǫBӎ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'śԬҵѥѭӲɌķĻcƉȆɆůưύԟ\x81ʱǾϕҷƮāŦщǀĢʧə',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ΧČɸʴӵЩ'XʲȔƊςԮɖЪƦЮÈȿ0υȃȜǔĊĢǮʳзӒ",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЍˈҁșӯŦίǩΙЍÈ8UѨ<ωñʳϘōĘȩ˔е',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˗ĀPǕфʿҏƩæѨ!ƴöǾӽȫʿЁӡLӾƇ\x95ǨҎз2\xadÒɘ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'zÂŲ¯ӷāŒ˾ѥђΆ/ʙӅЀǸņƴé´Ԥ\x81ȇ҃ŞϢȠϯ˛Ǝ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'øśʿˈϤǤƭbǙļʩnə˺ćƐЧғҙľĥӖKЊЊĝÔǤȨҽ',
                            'message': 'ʘЀ˧ъžлƋɷӌȔˈʮҿªȇ¼ČȚĕ҅ΧɢԚҵԐɝƢßҶÒ',
                            'arguments': [
                                        {
                                                        'name': 'U-ҶȪο˰ķͻȕȈҤҹ:ʂ;èӛИ҉\u038bɵÁӯŉȶĺӞϊƒ~',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Јz˱',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ïŹ\x93tįƞ!ÓѻҐ˄ӡϢȪǰŏƇ;ɛάʢˊʨÑ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 683069.6565585198,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ːˎ҄®ǀǕĭ!оƻӫҴǦԤʟν|ОЦˉȵӢɁԣʽ¿Лÿкw',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŁϖưƪЁɭʁԒ3TʄξaƘғɩʍȌǚĐģǪƺӀPȜȥџЈЍ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ðψ¸ĥϙѢšȑ9åξƷѹ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŋКԍýY¨ΊȾǤϨ˒ÿȱ˶ĪБòζ˾ҧhÀ|¯qϗ˫ǳÌ\x94',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŐʷΞҏкҏнǄØаOЅ\xadÓŁɯȹʔҩѴˢѴӖĳӥϯЅƥɸΧ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˆҭÇνӽʚԊϮϳԮƀǁωÒʖОςѨΪηȟˢөӾ\x96¦ӽπȝ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ż\x8eBxӮɶЙƘӁҪͼ\x99Б',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӡΉӔұ2ȯĸȊѐΏɫʈ҃ΗŊäυĖŅĥŝУρѵЩøÉˌȭã',
                            'message': 'τ˾ƾϗςԇѡΧĪџϟԀӭɬԋZәцǒȆύȃΖÐΠƇ&Ƿϛŝ',
                            'arguments': [
                                        {
                                                        'name': 'ñȩjĐХ6ԂӵӚ²ȂʣĢ6ӲɝҮ½ӫƺҢĩÉʹȑσ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŲΪΒӢȎυ}ʼӼή-cϵɦ7ȹϒ˸ҬԬѵҙ±ʭďΘӗ:Ңǫ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Нӻ\x9cϬЭ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:210939.243184:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԃTЃȷΎÒĐϔҹӪĺǰӤʄƥ\x94ĦԨȞęŻyez˰ҷϿʉмϯ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ļ÷Əұϛ\u0381Йɿǁ7ԎYωŠ϶ОŴƲˁвΟ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'χ¤ӜɷϴΖƺÁȣŻʍơ:Δȱ¼ӵäųǢȊύFŀƽЌq<Ӽê',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʰϪȈѴˀςQҪґ\u0381ĺ\u038dę\x9f˒ǉϾėԁ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'рăЗҎͲɸԩӍ˥ѐϻ×ЧǼԢñx˗υïӶΆцɇƯǱũҵԩŋ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ăӟΧ}ϝтɯƌѫʕ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6420626685351579490,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӈИҜҩʖȚŇ\x84н˦ϨЁʰ\x9fӵ\x93ƜӟаЗƇϟЧԬ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 276737.9070450875,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҍΦŗ˯Ґ\x96ǈѸƂζj\u0378ƭӿ҆ӘčËχĒΑȼΌ˕əțçǮМϼ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5597017783215544449,
                                                                        },
                                                    },
                                        {
                                                        'name': 'їØϤǨŇЎ?ʊǭβȉ˙ΤĈ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 450620.87993731524,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǁΕŋЛ҂˄Ŏ˕ƴǵswˬȎͼԙӼŚ\u0378ŠʇňĽȥɆˤнĮ\x90ç',
                            'message': 'ÓÿѴӺÍ\u0381ĿȪΦʃĥєƢȫţӵȔƱĳѝ·ƑΊҼНɻ|ϠЕЈ',
                            'arguments': [
                                        {
                                                        'name': 'ҶˇȃϷ҉¹ȩɕ:ˢԉɔgċϛфʞ\x86ŽƖҜљңȇƘ7ŚŜ|ӌ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 148360.85654733118,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϦwӝđЎ˞ɯμϕÅ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ç˪ȳ˵ϙıLʕȌƾŗʫɿһѩǛŠЮȣǬTʦӥêǎΪåˢςT',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȕ×Ŵɮ¼ǷÔǰƤϜɓ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƺϼĐ\x87\x8fʯɪǥÜɩ^Ȟԥ\u0381ɨѡ;,ˠ¢ʋAѷĸōǯ˕ΙHЁ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƥ5;ǹǇϹьĖІɟŉЫӗ\x84˱шĸĩ҂ҢŚΫЏʠȴFϥξ ˠ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʛҳK`э',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ƨǩǅͻ\x91ă1ԘҊQɒӟ΅УяԗҒҹϋȳһ\x84Ǳӳ˘ȢɌʄVН',
                                                                        },
                                                    },
                                        {
                                                        'name': '>Ҁ:Ѱ·WɀЗӃк{ÌɑŎЫ˛ӹаβʍŋ˝Ϊ`WoҴ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ёωzF_ЛϱԤϤǧшrёТ:ɍßηÚžҤĦ˕ͷǏǑƽ\x9dӥκ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:210941.150123:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ι',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'OƚӏȴФΈοќVƈѽƤ˫˞҇Ǘ҈ϑýҺłƸƹҢҍ/Ǿғәӯ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ŮǳęϚʓ҆ъȤĞť҉Ҋ©öΔѿƈћΧŊyȖɤŒ˴ҕŠʹņЃ',
                            'message': 'ƵɐÏҲǣА>υΫ\u0379ϰη vǜϊԨÆг˼Зˌ8ЖˊϤΎĈǰV',
                            'arguments': [
                                        {
                                                        'name': ';ɡǂȸΪӉӶǪЧЋǗúƘļʘ\x93ěǾДːĒ4ˮұûŎƐęōȇ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЉčϘ[ÛǋņŀʩΚŬ*',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǻ\x9eġ¾Χԍˑ϶ӢѲʷ?ˏӇǥȲͰϽˑíҫԚͼϊǀӾıȎȦù',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'õƷѫҭџѤǽ¬˝ҩ=вƠϯɧɫԫΦд\x80\x8dŏϡҫӐˍƜƫÖ<',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƿŪÒϫʝñƵ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 622473.1575153848,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɸñɸȪʆ~ÿҋŷҶǶӁɹϞoÚƂ˒ŕ¯ɼԝȢȅĹŷĮӁƕҳ',
                            'message': '\u0380ÏʳЅЩʫƘӟȓҽȇóμ҆ʪǖȔѸӸñʛȁƕĖrįƸӬÃЇ',
                            'arguments': [
                                        {
                                                        'name': 'ұЁLǡȪһʟũɉʄǇԩϷΤŭȍƨŖɠҖˡʣʅȯҥҌ\x8e\x8dǛ\u03a2',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ņ҆iː®jϋ¼\x9dľѦ»ǶûƨёϣԕɩͲɩ϶ɘӤ¨ɖϼОɾƢ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÓӆĥgЫļȾϹƝ˛ɞQĎ\xadgԎэѕƋэH˓ƞÀéʮĚ+ūӔ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ãľҭČαǌϤǌƨғƣȋʫԛԔƢȷSÂW[ȓйȒ\x8aԪќŎiΙ',
                                                                        },
                                                    },
                                        {
                                                        'name': '®',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɣуʩ˨Ϡ˲Ǡԥ%ȢÔɬ®ІҤȜ?҈ō˗Ƙɰ\x8aϵɴŲ§',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɮͰӄчˇɕЩȖø)Ʈ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӺΖ˄\x93ˡ˔ˈЏ\u038dŎ˝&ȹΌӚc\x82Ȃʙŭ0ЖåȫǉɷӴΩ˸v',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 792028.7350701137,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˈвÌҥʞ˒ƈˤéŠʪž\u0382țόӯƎɩśţñʸzȭÎŋˌ˔ʣǙ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȾώGƛ˲',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'γǣȓɽˬøŅÇʜϞk9HǊ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ёӈǟ%dǵþ_ѷѲĥґӌϧǜǙҢÁƷĪƈƓōʶȵӉŢŸҟɍ',
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

            'name': 'ӄùƦ',

            'error': {
                'identifier': 'ƱαƗ)Ƀ',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': 'ɉʺ',
                            'message': '͵',
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
            'event_id': 'ÿ\u0378ĵҚҙͻϯӜә·ϩΛ΅ˬțƀŞǣɅϛǥԇˣȝɯ˘ӆϪИӳ',
            'target_id': '΄ЈƃӪ\u03a2ԈѪÂȻӰƌοȄɂȞĢ$űƬÂʦȴϬΧ΅ɱȕӫƿw',
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
                    'event_id': 'ѭјФǑҘ¡[ωĳάǁͱϾćѧ\x99φ²ġГȇʎРɩЅŴԬŞ\x86Ϭ',
                    'target_id': 'ǬԒҿҳǽȜ\x99ɤǚӠϹӈϘǥӕƊƥȤƋÒ\x9aȅƋΓȳġҼӔɡ˅',
                },
                {
                    'event_id': 'Ѿӕšǟʓ3οĦÑˋϲ˚ёѕИɛͱľёȷȀÄӲȴГьĜӳғı',
                    'target_id': "Ǟ+)ϧΓƫψ\u0381ėσПɏ΅ЍInę·ΤąŻěÍ'ŏã\x88jIк",
                },
                {
                    'event_id': '\x88ļʥӂɯВƠ\x85ƐħʹÌѪǌ\u0379ϱЬԪҲŲƫϗȣΕɜã\x96Ƿҋӈ',
                    'target_id': 'ě\x9eăÚāщǜUǴѪŲÊҔʂҧĞэϜǢΛϲƂȁԫϰӆΤˎŃȩ',
                },
                {
                    'event_id': 'ǑӺ˂Ǹŀ½ƷɽёȾ&ХʕęɦŃơŅĥͳ¡ԗļқзҩǨɷΣĝ',
                    'target_id': 'ҰǼʓʧzʯƀʖέΙe˧˅ϩīó˦ϴǋɷĊˊРЮҽАϲчk*',
                },
                {
                    'event_id': 'Ɠ$ʵxȆЊϚаƆčѭʋɅ˙ɚȑ\u03a2ϩǩƔ˟ʞȧǿɭӻγχЌʾ',
                    'target_id': 'ŀϊϙǫӾ˸ȳȢʒÈʶТǬ\x89ҀǩH}ĢjBʲ§ƔȱЭϊƣҤʄ',
                },
                {
                    'event_id': 'ŶŸЦǑȲҡÙԊЀNϵʾҸ˧ÀΐћɊƭhsōʆ-ԍΕŚÖhʥ',
                    'target_id': 'ɩѬÂцŐͼȖȕͱҽķƫϺςІΛǙǞɭеʚӐ~˄µÈϏɹ)ĥ',
                },
                {
                    'event_id': 'ǵԌÞúʾƆΕӊɲҧЅČȺĳʟ΅TʟɾAҍΒɧѾʸЦʡӄY9',
                    'target_id': 'ƫǠџɈŔҭŲϔЋӚňϻʥ˼ԕĊȞιŋÜɈʨІÈҘŐҝΩðÁ',
                },
                {
                    'event_id': 'ΞɫpγʎќҐʙ\x9f¥˸ђԙҿɤǹаɒó\u0381ųƁȉѶɽԈÉЩЀ҈',
                    'target_id': 'ɣʽӣȡōʭ\u0382ӚʷƧ˺ɉÃΥ¨ŭŔςљԧÈΘ¾\x99ϣʜυԎ\u038bД',
                },
                {
                    'event_id': 'ɼđ˼˫˽Ǽ˸ӔқſĀҘ\x8aʔũ~ȫУŹůǦǕN\x80čэƃεҔš',
                    'target_id': 'gѹą#ʏÜøӧѹˉϞȚʂbʠȩӕ\x8bˆĲíǴ¡ƵfяĢĀʾM',
                },
                {
                    'event_id': 'ҬъĈΪΑҧѰȹPjųϫԃȏрȫѸRЁ¢9ʅŃҕʕԓɆŤϗԎ',
                    'target_id': 'Ğ˛ÕѺƙŖƍѹ¬Ԑǒ\x7fȊ~ѠƧǡ˘ϪʼKʩ/īӃˁȢљ˺Ψ',
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
                    'event_id': 'ĵӥʶӞƊȱ˖ʤԑѼҲ~əĭνÏԞ¼˪ƀŃ"ƎӁɩŔВљҎР',
                    'target_id': 'ȎũӵЃǈҪɽĺźǭŞćĘ˞ӮƪłɚѤΌĂϸĴŎÊ\x9cGƱʠɗ',
                },
                {
                    'event_id': 'b¯҉÷ϊӳѩʽϿʦԣӈɇ˃ȼІʨƫȞԐ҇ÀԊɱǉǟǴԒщƤ',
                    'target_id': '@ɚ3ԧɾϚåŭ¯Ӂŝ0кˍʊҒą\x85ǉ˅ʖèȃҠʶϡόλēϖ',
                },
                {
                    'event_id': 'ƔƩ\x92ԁɥª$ʵȭʬþȴԆɋŋǑŭƁ\x8aȊȑÿƧɵʈǢɻǍƷΜ',
                    'target_id': '~ĄŢBȝʁʆѵ˭ëÊ҂łЎȭɨɝˬNŢŭiȚʇϧΒӍϺҒ˫',
                },
                {
                    'event_id': 'ъԎЎÕԄѲԢɽ˝ҹöƧЖПŎƅȌϝŋǱȿʉ˚Ζ+юjīƂʡ',
                    'target_id': 'χʬǬŞņ\x83ЧÙˡЈΥĞǵuΰʔѝƧĒī[ÇϕԖ&ŁƬəԙx',
                },
                {
                    'event_id': 'ûiё˟ơȪѴа˅ȀMɱïЅφȴÞȋңÞыК\x8c;ĪͼѬԍű ',
                    'target_id': '˯ϯx/Җ0Ķ΄ƱґԬ³ˮьҔǳʳԫÆˎЬЮϝӨʴ²³ʕĿΛ',
                },
                {
                    'event_id': 'ϕбąāƉӚ\u038dƓčɃφǜѼƁ¸ҾöϽƊҬťĢρҫ\x8eԡѐ¾ʟ˽',
                    'target_id': 'ϒѡӆɒϜҧ~еǤ¦ǂφǭGɬęË\x82ѫ˫ѢѣǡD×ȿԖʻġǭ',
                },
                {
                    'event_id': '4ǶЩɓɕӕҀǐƘðԮϟx\x952ӶȺʆǙнŖ\x86ƾʿH\u038b·ɺȵł',
                    'target_id': 'ʌҹɲԎ4ѐĤϧÉϟTäĜĺźʞӊӠρǅĒȆ@ʠ˱Κ_\x81ȺЍ',
                },
                {
                    'event_id': '®\u0378ğWԗŏҰŒȢԨ˹áĥ˾¢\x96ǿ\x99ȋɞÿӵ\x9aԙȮќĕϳѴԛ',
                    'target_id': 'ˡʴWǟѻ˩ΏͺҝцźK˱ӗɶƩѴMΧĵÒ˲˅ҤÐ%ԮĽǢƶ',
                },
                {
                    'event_id': 'WҾ͵β˽ʫü\u038bΆˇǞʃƭϥҲЩ\u0380ȬҸDϬɷ{\x8eϯҌƕǢ˄Ҵ',
                    'target_id': '϶ĀãƟҢр4ɓ!\x91´ƛóĈĴ˷ѥ¾ĎȀ\u0382ɾȳƲΘ!@³Θϙ',
                },
                {
                    'event_id': 'ӜɰřӾӔҪ-ѶȳИɕӔѺџЬ΅ϠaʥˋλȨǷȓӿϨѽOǌƫ',
                    'target_id': 'Ŷ˘ɍwӳ¿ċɃŋɛҲơҀäĮåҥШƷģŭđԌ\u0383ƤȂːΨ\x8bΓ',
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
