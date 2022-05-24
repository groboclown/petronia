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
                'қͶɳUǯŚ˪ʐѭѐȡŵƁ˩΅ӠǓkφðĄɾÇМҮΝт\x89Ψì',
                'Ǟ(ʳΫƥóŇɲ=ӎȂšīΝѐӓ\x8eԒ\x98чǵ¢\x93Ș)ɧäӛǔß',
                'βǐЈIo¹ΦǒĄʓ.Ώϧɇδԡʠn˓ʤϚĖ°ò˻ґ4λÖǛ',
                'ǘǄuάӼȄѼɮŶ҃ÇμʽϑһϺ4ɡξƍɘ\x88Ʉ˄ӱДё6Ѝқ',
                '\u03a2ʙъљʛŤ˅ƣ˹ӌҥϬŽĺïuɌuɷ˸ěůȦ¸ӕǸfʮƲƻ',
                'ȭŧǋ˶ŦБ\xa0ĳ˰ƨҮħϬȔʀёħŉαˈʾXȇ˅&ҐҐƬ˶ч',
                'ŕһɆ˘УʁjӧϲZǞţȮѥҺˠøŋ©ĕʋžѸ¤Ǽ҇Θ\x8fǘf',
                '҇¿Ӫ\u0379ǌĐӻ£ǡʱ\u0380ɣŒåΏȕğʺϪϼǰƧΤŕЀӐäôɞӵ',
                'ˋуŬ%àӉѵЍӆƉʠӑБDрǨΫÇЩǌȾԉ˰)Âɯǫ4ϥƙ',
                'ˤΐ×˪ѤΑ\u0382\u038b(ԉчԭȆќɧԧȐāɿȹԃȖ͵ĆŠĎɂ\x8eÞϯ',
            ],
            'source_id_prefixes': [
                'ӛŦ҇ȆÓѹʤϥƍΩыϲ\x9bťưĲМŻƣґkә+˭ƓǤɘҮЍӰ',
                'ԁpϚýɟ¸4ΏƾɤѽΊɮƛӑҗƗ:аoԉùӥКѮĕÎȠ\x97ʐ',
                'ŧǯʙяʊʦϕӯ˺ϛƸоϊ˨Ќ\x94ԨɺŘҷЌΦзӊɌL¹ϻ˵ȇ',
                '9ß˫ȖԒÅ\u0378ҺƙĮӋʹԐˢөӮˇƥǊɫѳɒƛƳɰɤʇƯɠϧ',
                'qɂĠʻϦґʃ1ǅVӽŐΨгȢЊϨǊìɵҖŚȏ\\ʳсĴԬ˙I',
                'ƳƎӻʬʯΪDЎǹǽƈĄÖŻӷУGȤʌëșҴųhŇҤĕЇԔ\x7f',
                'ǽТƱтϵФ\x8aӹˠϣҔ϶ğ҇ȇáӰǔˉ8ӼӜˢѓƂӤʸʩϋԮ',
                'ɤ҄ȶȭȑ\x98·¶ΗƤǬöʂnƙЈΜζǎƠĄӏǢѡ?҆ǋΧ\x93ƚ',
                'оӋɜũƷɩȄiɌɖʙξŷıÂƊЮʮɛӘȳέǀѡȘĄĉȵīȊ',
                'ĬƘѠƅ4˯ҔŌ\x9cÆψʳ3ǛчÆŭϙƶӇ¯ԣÿӬҷϝeυGϖ',
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
            'action': 'ϮȫϺԕȢҌԔ϶ǉҡһӢԈкәĚяÏļӹđ\x90ҘǡŻϾΈʖȬȥ',
            'resources': [
                'ʹĬΫԠĻˉƋØçƽðӔV˓PŤƴļˁʠЗ˦ăԜÝЈюͱˌ˫',
                'ȸɍʄіǯӥǀҶǌсѐϣñԍԢƟυϕЖҼǨϹ˯ō\u0380Һąʆҭѕ',
                'ɺȏҿҌ\u038dÇĿĨѤǴȘŦұѹΈĔ\x83ѫԟ¯JӯҾ҅¾Қȓԕ<ʓ',
                'σЭťΥɩǳ˟ΨM-ĵҵ˘\x83ԒɌҊş˜ǿŬҢΘÂç˽ɛŮÖѴ',
                'ˏ5rý6ǟÉ½ɸ\x93˥ӉǠUǘ\u0382ʜ=ńЖ\x95ɹĽʎϋҠÞҿoɺ',
                '*љҺɄӋӔųʹÀj˃oǴdӒӘŦӲӟҏƄˌϞԏǱƼԅ/ϺԔ',
                '˘\x9fдŎʋӚÙĵCƼъΑΘč˅ûĈŁ®ʇюӆЎɢэԝɈԈţɏ',
                'Ñøϸ.ǣϔƳWĪ˝ƕкǺÊǙíɷȕ\x9bŨҭΜ#Άɡ\u03a2ęҺӧȜ',
                'ĦҤͺʩŬϯʱƺЪǅ[×ɊҽЅʰЕȎǉĈŶ{ĿęΜĄ˥ήĹɾ',
                'іǃһȺЯʠҏşŔŖѳɓ(ȡ\x94ÎϨҽǬϵDӊ\x8fΡãĦōкԉԫ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'Ӛ',

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
            'name': 'ɚ˟Ϭˋǀ˵ȕɤ΄ɔәˑћѽņ˅ƞͿÁȎˡтǑőҹЁ҅Ăϛ:',
            'version': [
                -9008204046546045207,
                -6628236496559984554,
                -7496448520573437527,
            ],
            'location': [
                'ÝÄ^ˍǚ/юʧЌԊƹȉ]ƏқɧҫȁAԧӘѲěҚӵɺ\u0380wȨѤ',
                'ӇЖÈʄĮÍÄȮ@їƲӼӥ¨ʴ\x82ϥεǈЅʦϭǰĥȲϘщăȘǝ',
                'ӥӫƼΑɒƇʻЛȚȟɿʁǡљКѩǛ˦˘ŋ<ǢįҸеʹσêŒĺ',
                'ʘƝãӉ ѰĶĳќϑӻԘͰȗсFźĮΙɺ˜ƅҒΝʺɚÎԄғқ',
                'ӫԖ\u0381ÊЭ÷ÑĎʀ¡ΖǕ˛ʙǀɠҪʪΖˮԓӕͶÄтœǜȴͶҩ',
                "ÐɰEϺұ˱ѧȡΞOӪҀƍǪӑȅΓѡéҦԍçϖÕӁ6'ҽǜƚ",
                '¤ʕįØԆӀƑ#ѶǢ«ѡˡɔǺƻҍЈ\x81ԀĤƿ/д˂JƘǤԝ\x92',
                'ƝħƛĄ7*Ҍ\x8f3жй˗\u038bź˰тÂlǉÎʥ}вɴBЋƛȲ\x86Ώ',
                '¡ǚȬӸɧԢ,њПʵюϠΔϼƁϗǗƮҚƤ˅ʁ\x85ѦΑ9˃Щ\u0380ö',
                'ĚkҭƇԭȡǅҋɐЛΨšöϑδþ<ůoľωċª.ПSŇҬʌΏ',
            ],
            'runtime': 'ćó\x92ӄđ˼@ΞХƸ ԕȒʿʓņǒȦПӔԩ',
            'send_access': {
                'event_ids': [
                    '\u0378ĐɘſǒӽɕϥіʝΗʺӒώɨǼ\u0383ɉβϪÂ²žõӜкϣїЛƿ',
                    'іϑɩіɠʭ`JİԄĹφӀ´ŶͱĘϾӊƵΚєŜ\x83ӱԂʞҀ¼Ѭ',
                    '˽ˉԓćƞϨВʳʬʖτˮŵϓͿΧŏɿưАÒͶөǎĵҵӓǶYϟ',
                    'ӬϴҒ¢EԊϧ&ыɨғӞɜǛɞZȪķσůvѽ\u0381ʵĎΙτcŪɘ',
                    'ƬǼʃԐЕэЌǋ˫ïҧжȨΆЋӃԪԨԎҦ¼ƁѢíūÿԬsʽʸ',
                    'ƲЗ\x91ĠˡԔȵȽʤőԑĭʊɲğƲ҂пŕ`ɭҶҋÕTųŦÛΙ°',
                    'ŤΌÆÖӌȆ7ŷlpȌӘjǵņпǭїŀɿԪŒёϤʏȤЪñϜs',
                    'ʐĸçĘȒɄѴ¬ʩɁƥ_ʹȉÎǼԆwŀӓΰψ˧ʰκϥӗ͵ќȈ',
                    'ЅġS˳Ȝ˛ʰĲɴ˖ί¼òγÖ\x94϶κĸɁқǫ˛ΘʒϔΪϜÛˀ',
                    'ǐʇĆԡđɆ҃Ҧʔİ?УЃӆÑϿҵϖ\u0383ʞɡҟoȈԏϲӍϵǺħ',
                ],
                'source_id_prefixes': [
                    'Ǡ҅ΝюJƆ\u0380ɸɂÈǦjҘˈæɋʠΦɨζуе˯һľÅŸΪҚҥ',
                    'ʰƆĜУӡ:Ѱхϫԕ˻Ƚζ˙Ţƕ\u0380яΞѸ?ķİϜũǂˡҧʀʣ',
                    'p[±7ӠЉϖ!\x84ɶŢüƩȣûȪǏǇ\u0380ɖ\u0378Ȉǲƕ˸%Oȶ"\xad',
                    'WŧʹÃżˢјьˤǉŚƬȬӷј\x98½ŔőǳӈϾ¼ҟҏmϰʎˀǼ',
                    '1УÒ®-ҒZŎʦƶÉԠLϩӅϮ³Ρωʟƪ˝ʽ`ҲŖÀŔѥӞ',
                    'ɝŃłҫғÝĚɫԩʰѧßψǁ˄đØξҴǀ"ɱ˘ȻԍăċЉ®8',
                    'ϪƟӺǐ\x88Ӆӈđ˾ˏȪƸʂŮŎӤьԒ\x8cũʇӄһ\x94ӾцNԨȫȊ',
                    '˱îΙüɋƚ\x8cȏǘʷѩσÐ˖ơђǡžԀź¥ӓӿѠŵ-Ʈ҆Ԟɶ',
                    '7ʶ˰Νơîl҉ЄʎɝjґƞόџĴΛ¤ѥ¤δcϓǰ˯ԤԧЃԎ',
                    'Ȫϗ˟ΝŝȀŐŧМϾǣŊАҷç=ĎҖѢϿňȐї<ǘӄ½ԦĚ~',
                ],
            },
            'configuration': 'ԀһӺϽҀ¨ϨÊLƀoӮĘrɜɏϟȇʯ˧½ЋΞ˳ͺŰԨҋӊ\x96',
            'permissions': [
                {
                    'action': 'ԭшҧȭҶǾќǗ`ҍʨϗϔ{ϫƹȅϘҥȼȞНƷëӮ˴Ν.Ģc',
                    'resources': [
                            '˖ȲǶԁȮȩȁƋɫĘ˜IŴ҇ӮԦǫȂ΄θέƬƗėπÌƷǔǄŬ',
                            'ӵԐԝӀĐǗȨΞɁĖѬΧƛǏƂ\x82ŶǓѬһ4ҙ¸ƛƨɝũʤӒȑ',
                            'χĠ#ƧʯÂǒ\x8aЏˁӥº˳ʛ˺ԪȜǿšˆѵΦͽɡşϝȍ@˵ӏ',
                            'ɋėʰ«Ԇ҇ӲŨʑï§ȿUʮØɈ¨ŋŏТηưѠɍɁǑȅԢǍ\x99',
                            '[ȓɔʴŵůеӼĭɪʬԕԪxǁʝҐѾėІŪЎӨΤăΕ$ӋƓͷ',
                            '\x83χťǽϱÉ@ԄѝȨЍіҜϙˍŮđǫÃϭӜԓª\u038dăԠƟҎß\u0381',
                            'ǇŐҹǹШƇϋɾԇȾʞõfϞҺѯÌƿ',
                            '¬ŞƬϐͺǼǩƢ΅ɞӿ\x91ɮөԬʿ\x90®ɪˉјľδϕ(ϓІ˧рЗ',
                            'ʎҍȄѳƮЯДnïʠӎˑѴѰ\x9dҡ5ƽʱ£ϖ±ʰĉI˛Ѓφǫϩ',
                            'ˏĥ¢ǰѽňԮÅʮǔѽӮ££˯хӋҮǸʾ҈ƏĊѮʛуĩËVц',
                        ],
                },
                {
                    'action': 'ĖkυϓƠ΅Ѡɯ°Đ˝ҝɯǎΞӆӔ+үɸõӟâɪЃӵĺȫĸ',
                    'resources': [
                            'ΐƏ҈ӲζԨ´ҥʴěʆτǮӥyƮϮȏ¤ù$πǆѕ¼șΘȞˀ«',
                            'ԅȉԗ˕πӗ8ÁʦɁҊơǵ\x9bĤʙy¸xƆ¹ӸĎϕұßб˓иӹ',
                            'κǷLƷиWˎұȏщöʯ\u038dɱͽČφԖ@ĭѷόкϏϦĝaƧõԜ',
                            'ȻbåνΎϔ\x82V\xadҍŚшӍ3\xa0уң˅ѓŗǧǰĲӚґӯƌϜдô',
                            'ӃƲƠ³˘ʽɍ·ɀ\u0383˗ŻǥǇÍшҞʶѕȗɉʯĉ\x87Ƭӎ,ҠӦӴ',
                            'ȓРǒŠαĎӲɁѰɷĐƜ¤ĶΒˬѵĥ\x92Ə˵ԫξˇìӀϺλѷ0',
                            'ȡlΥǰǲ\x94ę͵ňďņȚƍΡÄъăŏȋºӮâêƃǘԤƕȦȬМ',
                            'ȞÉņΰӼɫҦɩŅĭ@ɲɹζoĢƘԮʎƝҘӑҴ˃ԌљБ˧ӽ\x96',
                            'ǲoӯˀрόԌˮаǯÃʱЉΟ҉ƔГʺîӝǶӓ\x83ĖȔHyŁȮƱ',
                            '¾İӹлȹǞÄҺĭ\x94ѽͼOσΚҾғŻ1ԉΗƢ˳ΐǨԜ\x8dѶˠʭ',
                        ],
                },
                {
                    'action': '˅ȧɕҍaeӹƲƧ҇°ȴƊɻİƙƅò˯˼ƮYϣѯɶǪUmɚʶ',
                    'resources': [
                            'ˇZѯχϏ÷ҼÐӠȿϸμ҅Ԛ¨hÞѺȒԒĽƥgʵϦĒÐІċҜ',
                            'τĆϙĶҺ°ŋǰάΐɋјÛ6nȇĪɄíǽΪџŦȗ%ƑĽŢ\x7fû',
                            'Ҧǝµgеɯˢȉ&BĥʼΞĔǼɅɇΨèҙΉǚɻѹұʩψȬůҎ',
                            "'ĎѸyűīǭɞЦĞҽѾʸ\u0380ОǞ&ҪʆϢɱӽԅÜЭʇқѺԧƘ",
                            "҉ĳ®nʛӿźӻ¨εӔģ¾ЀҀ¿=ƽӞЬʌϿ²ǔΝυ*Őĵ'",
                            '\u038dǷÆîλ¤ƪʽ˄ƛόƾϧFүÏЍєęЭÝύǣɃˀ˼ƻÅˎč',
                            '˼\x8fĵ˜ϼҽ΅ʙRɝϝ@ĺψˊȶǬć҉ͻţoƀĵĹɁЀ҄ʅσ',
                            'ԪŊŐĝΗP˛ǔÙĘόƭʮɈʿѭѓњѷêɅǦƯʓŉkԍś%ƨ',
                            'ˎϳʌӎ\x9d\x9dĸȄʨӀƉMÖĪϿċģ\x84ƜȮƅȩǦ;\x8b\xadɒǕЕӽ',
                            'ɤ·Ŧœ2VĜĶҤÒ҇ĸȽĬӖԡͶƭ\u0378ƵåһŴӂϢʦóƑҋΨ',
                        ],
                },
                {
                    'action': 'ųʦǳǳΣĂԀɎǣф\x7fEβǮѶɐЕųʏǪ\x8b+Ɲȱʍ\x9eϛÒó',
                    'resources': [
                            '˪ΙŅԞɨɀ˃äӗΑÚɵԣšʞιiоĸыĹ\u0382їͼőǷƮȸ¨Ć',
                            'ȯ˩ԒɥȠá\u0382ӀƄŝυѹɭˬӎΫԃγˌѰӐ˥ȓƲǼx\x86Laq',
                            'ƻŘԁҁy˗ҭȉʠƀӄ\x81ϕ\x8cыΚ$«ũԡЩfǊȣˠ҅Мʣѥә',
                            'ԢĉљǰŤƃʍ˪Ӏҟʌ\x84Ğ¼ùȸpûʫȮɶūήɴБÞę%ĭð',
                            'ŹӖƐӦʅŰȕΐϚƄèˢʱæΔÚӼãԁ҂ʂXё˞ĲСğӹǞҥ',
                            '¨âʂϥȾҁѳӪƫзӻɷĒҤһǔΫ\x86óɚňñɴĵҋǑõЁȔ·',
                            'ϹǖɔvЂñȾ¿Ēʪȇɾw˯˅ˣäԟpɢưĖӭƪΰ8ԍčΥҁ',
                            'ЅĤ˪ɇGӯȐӗåȍѥeŧɞ˧ʳʞҍ<˼Ό^ćȜ\x98ӔϽź˺Ȣ',
                            'Å˄ɑʤԭχ£í\x86ûӂ\u038bΤʆśϺʬ/ǒȾӛȦÈΪŐɖъê҇ǝ',
                            'ȐöΡș6ȟӂ<Ҳ\x9c=ȡϑÉ˞˝ϋψɆǩĶș϶®ӱёөӢĮӳ',
                        ],
                },
                {
                    'action': '҅ϺԙÂˁϡϋɻӌˀîcĈӁȓѰĄƚЁԤ˷˛¥ϳʊӻgӵ˘ԣ',
                    'resources': [
                            'ƢĦʡϳɃнɅҳˁʥϐŀєąϭǛȻÃ϶Ъɳϔƺǂ҈ȹϞɳȇg',
                            'ˎcΣ˃΄ӪӨԬӈќɲԪςϭԟ˔¸ɴéHĢȩǆϸӰӷȑʂð>',
                            'ӋÎɿƸĆǝUӹӇӱżѠǲǩӹÃʤůřəɺ˙~ӞʜҠҀάȂӚ',
                            'LŘοƾӀ¶ԎӷȰ\x82E¾ɶӫӌН½ĪÀӀƳˎʸ°ыčϿǝƏͷ',
                            'šӀМûљžƕ˺ЌʲϚΪȪ«ΩȦϡăėĪŵũόɼγɴԦ£)у',
                            'ŵΰЗǍ±ЌȇˉѼÖɢŘƉWgɂŃ҉!ŭо˷Ԭ˔ȅʴЀŽѵ>',
                            'ZðͱҀɿͻfȘϧ§d¥ǠʇВϤҭũʼá\x8aХǻя\x81҂üϽϹЊ',
                            '˃QԆSРʧñǱjƛʽ˻ШȥЦ8ΔǴɧσ5ϙПíΑǄΗʹƨ;',
                            '˟њǚáɾȄ(҄ùӮϵԇÃѨԋӻĦѰЍċÏȕΗ}ϩӻi˗ьϸ',
                            'ԥҽĈ΅ǲŦ\xadǇˇ΅áҺƝéƈĬМÌӽԁҫυ˓ƉƏӴ=Ĳвİ',
                        ],
                },
                {
                    'action': 'ŀσϼɯŵҙēʀʪј˨CόϢƆǊʣǱҒρʶή\x98¶ҎǉĂ˂ƮЏ',
                    'resources': [
                            'ӥ¸ɢŞƬųŞϻʫӕ\x7fˊƗɔĢͱ´jˌqþʆNǴˣДғ\x7fȵӆ',
                            'ёÔЕоѶƵЙɘ\\ΟľĪ´ϣɔUғϽɥίΟxȭӼԙÓˊ§Șĸ',
                            'ҸκʹпÅÈГƮ\x8eб@ƭƁ-ųĝ+¨ƐʂȼQҊҹѠȮϭд1ʱ',
                            'ɥƭѧ)Нþʀ4ԋˬÌ˱%ȋ˔ӰʉӱӉ˪\x82ŨŤſǤȻʼКˍβ',
                            'ǞHвÑΕŬBԌЎŎ˗ЍҬĕԗΝ\\ϣǈцҧϖ˕VӬʆЏǗĉŅ',
                            'ӣÒс¿Ȥʝƺ7ӸƇȇuӺǨŎ\u0383\u0383ϡǮĴȕ˔ţɕӌǘ;ȹˡƹ',
                            'ыȲѲӰĩʓθœ\xadӼǱ[ŢɧiǱǃşѲу¿',
                            'ǒcȹX˂ɗѣæӲԂ\u0383jԐ',
                            'ùԨӓĿOԮĝȞcϚԂϿùȓŃяΎΓÈΣΔКϤġ˯џāì\x99ӵ',
                            'Зķ5ĊӭԂоƬʕКǙʏʩʹȨύ҉ɽȸɓŞ˻ƍɰɹřnƇΙʩ',
                        ],
                },
                {
                    'action': 'пïңŝèԗӦȟПȻӔМʭƅ˄ƛǔ˲\u0380¯іǨʱ\u03a2¼˓В±Ã\x9c',
                    'resources': [
                            'ʐϳ\x7fӨşÚǚ\x8cΡ<ӖΉƴϝɴӵϒǫҲɺԈϤ·Πư˺ɦȫĕӮ',
                            'ҧŤVIÔΠ\x97ϱįƄǃϒ,ƿCӑı˭ǩʝȘѮ˙ɵѯέδÝͽ?',
                            'Ъ8˂ωĎ·mҚà\x8aѰºшȻʷâǣҼƆɻʞʰԈɿВșȄÀӷϜ',
                            'Ųǯ\x83ȯȲîɘ˩˯ʺͿԃӷџʛȯ©¶ɻҮ\x99ӟ¢ŕśʑ\x90ʤǇҷ',
                            'ƲȃǃϛαΒϐŒūʇĬǯ˚ǺʣÙ¶πͰ¹ӍƟҞțȇ\u0378ӾӿΣα',
                            'ȴҳӲƳі£ƲѿӘğȏPÛљȐӢҒјΟˌӘVˇŌʗį˾ЧƬØ',
                            '£ɭӐԑxƄǲҾԧΙтˇżɇȝuҲѰТŝóЏčϛͽЏŧЦщŉ',
                            'ʫĘƟěњǲˁżųŸȹѽӜÜ$е`ġҒÃɴӉµ˯ѺȁγЮƏμ',
                            'Ōʂɲӵч$ǌӁÃϸϞȘΔ˄СЖ:Ĭ˦ѩӚpȉ¯ҿX»ҏȘѓ',
                            'ҒǏϲ҂ΌǙЩƏ·ïѥˍǽɇбԃÊ˒ҲBʺzÃ\u0383ǭͱƿƠӟԘ',
                        ],
                },
                {
                    'action': 'áɆ҅ӄζǃѼÆÑǺŊ\x8a}ҷȒӭǘqśHҋҠҞϪb΅ʂķκı',
                    'resources': [
                            '\x94ʒĊſÀ}ƞǍϤԇϴJEӎψÅ·Ϊ8#\x8bʒĤsğʃȯ\x85ǖł',
                            'sԣơʜƦҭΰʰȾŁǁɵњưҨƷҍ7ϻӯһϥӍǥԓ»ʭɍϣҪ',
                            'έԧvɮͳ\x9fϳUϜΨp˧ϥƼǏԮȟΤqԕѬŰҒĐϛѓЮѷЯԩ',
                            'ěŉɈФĔϤɼű.ĨӞ˨ʶ¹ƱǇ˴\u038dѼюӐшëĐ˸ǍѨɭԍҠ',
                            'ԈϼõɆӺwӁe˱ɓы˒ʕǶi˨ѳưSӥщˠģŬ¯ФɯǸʭĚ',
                            'ԅѓˉΜӘРԥӂ˩˷Ϧ¿ʌԑ˴ΛǾґO¸˔ŰĊӈӡĘҀĀ\x87c',
                            'ιμƱ˄˵ԌϮȨcɖȪŝŒxȅƆʕñɎ˩έӈ¦?ӀɴʌЛƳÚ',
                            'ǖԩ҆ïΣΈǌӵÅçˑʴСҽеǟѠϜˋʿƸǣɨԭċȆξɵĸȳ',
                            'ɊØϟŷǒβL˾V҄ВȔԙВʶÔ˯mĥʉ˼ÏǇƇЊâёsԝɹ',
                            'ќҋЃκŽͱѕөӎөқɢɵ¨ \x96ЬȰξ˽ɅĪΙ˯ӊƃʊžȥέ',
                        ],
                },
                {
                    'action': '"ѵĊɸǠÙʲͷĞňƷϤ´Ǘ΅_ȓɪϴӹ®ӺɿԢӱŹǻќðŉ',
                    'resources': [
                            'ÖĕГҐѾɴȒűǡǾǓȕԥĐsıѯƋʬɢщϾʹҡӸʄȧɂàҼ',
                            'òЬȜωȠΏϊХČѮúěґͳ˦Ĵƌ©ǑƱǘӞάѴɖΠǉӪ˖x',
                            '«âËŏ\x89Ҕäǽϓ\x87ǋͼѿҋЋ0ΧŜĬÛπɶȋȞ҆ˉÈċīʥ',
                            'ȜɠƆǮưӦ¾ξм҇ҙЃųȩɇԑǳ\u0379\x99ұβŋԍȱ˺Ř҃Ѝ¡ř',
                            '\u0381ųΧНʸί϶ɿlĤĭȜʍѸƗѓԕ^ŦŻîƜ\x94ʀÒҏȭxɝȎ',
                            'ԟќˊđԏМȖʙɀŴӮŧƄӲ)VǲөʊÈұēҒ»à\x94ūįҶĬ',
                            'οɰˇХítÞ',
                            'ȭӑ¹ӺԖ6ȾϡĥϤ˳ƌɤԀѨǧԃÐϸƋȍÕ˃˕[ʦиǟрρ',
                            '͵\x9d\u0378őòϔ·ӶưεԂͽfǔҝғɓN˞ƲƁ˂"(ˌ£Ƽǋűǋ',
                            'ćɃ!ccƄɰćвцɐҾĪʪϾ҅ǟЦѽ{ĸżuʝŏŰʧϩǇ\x94',
                        ],
                },
                {
                    'action': 'ЈҥƖwӥχйӡϯБAďӭÁɡ"ǹЊϲÀɳϠΜřʏӘОԓĄù',
                    'resources': [
                            'Ȼͼ(yХ',
                            'Ҍӿϡ\x9dͰʥƜсмИ҈Тρɛʕ\x97ʥЕԞşˇūΡǺЪœЫɞ$ʿ',
                            'Ϫ(ŜlӮϽÛӧҭʢđό}иѠÍˢ!ĉʳӐҋϐ4Ŗ҃ȅµʺQ',
                            'ҽϿ×ƟӛΎϩ˅˶ӉԬĊäX\x96ʙҳ\x8cЂɒŝϒϗ6үȻτӈȨĢ',
                            'Τ˹ӝȡǺĽҴԇϑжӪӁϰƻɼƀĢ˟ҥʒъƣĒɢѕƧ¦Ҫˌʫ',
                            'ýǄŃÞѳ˜ͺӷrȯȑԛƐIÏͳӆұ˯ҏԖ˴ŁǬσːŜρ3\x91',
                            'ŧŰԟȵNҞHЀȀŶȾƳȐҔϗҦāЙԚȣΎɶϴȼǿˇŕɳżЋ',
                            'ϴԕ&Őƾǰ\x9e˔¡ϛŎRƛŏ`ϘƭҲÂͳӻЀˀДĚНҳӳǣX',
                            'ɛ:ЏӐŤҤҒӞЌǔѢ˒ħýDǛǂǔɘ¸њÆˆÎř\u0378ȅԪϞ˩',
                            'ԓԜŘćʳʪѮs*©Ťˇ«ʴ-ӁΔҔԚ9ǌťǬЍєʊϭƾȱÓ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '˹ˡɫ',

            'version': [
                -7588236465366833707,
                -7894267341809664107,
                -6843243373976238091,
            ],

            'location': [
                'ǝ',
            ],

            'runtime': 'Ò',

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
            'name': 'ѫ˻ƧΧȆˏȰƠ2\u0378ӣӯϠɅǠмˣȈсѦӘmҠӁʢΰ&ѓӌ\x9f',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ˍЫў',

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
            '$': 'ЕЬÅFѼԃWьɳ+ЮӳIåŃʧ3șƸRĵ}љʢ¨Ͼʧā`^',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 5412095055434949173,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 269053.4180978487,
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
            '$': '20220523:220031.443843:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'βŜΔ9ʸѳƜƹŹ\u03a2Ҳ˜ԛǖФоƛ҃ÜђϯǉΉƽ\xa0ðʞЬɶȟ',
                'ԗżıƬңȀϋѳùʤƲӱÐƼșЀʨòЛ˶λΑcӧѸԗƇĵ¡д',
                'ïƺ©ӱ¶ЫɰQ\x91ňϢ[ʗŴҋʙԞÁ˺Г3ѹŕӯǻǉКҠҊʂ',
                'ҍÎjgƸƉӮ¢ʸƆ\u0382ȮƶɑʾğȣřԜȞźѫѐȡȈϜǰг{,',
                '\u0379ЋXʱ\x83ЪӠɆʂýʢŃ+ζɔΫcɛţƐƳ¼˫ԍñЧķșƄʌ',
                'ЬǬѭĻȎԮϼ˻\x9fìʵ[ԓЇɞĿ\x7fҙŻʘʆ\x84ҕΊ\u0380ɹ\x96ʠ&ƅ',
                'ǵ˦ӬЪϋŁҊWɋҍҡҧ½ȽӔәļěи҃ÁҲ¾рΆʣ¬ʈ\x8bΟ',
                'ěҗȤҊНȈ҂ĘVΎǦ˔ӗεÖǅӅŖ<ƟʔқΈoԆƅʄϙʿΰ',
                'õőÚüϋʒԈьƶ˔ԓΘɡÄźƲӞԖȞϛϊÿȠͼ\xa0ɫ\x8dƧ҂ȁ',
                'ӮΣ\x82º\u038bĩʂʠşԎʚӀǯҰCмуȥǿϴ˥ϸȢͷːɮǳЋΉǴ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -7677000394501996599,
                -1629300243015214959,
                -2445490062555599745,
                8769801384922138581,
                -7580864364745860422,
                8071598672258644179,
                -2203815368566881536,
                -5239134555749149880,
                3903320295258948863,
                4392682658441178750,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                214413.06162790058,
                553960.7846778426,
                608213.2983498883,
                691222.3909971945,
                453226.88466964196,
                505180.6726431103,
                30736.779991693867,
                128373.99942284447,
                30445.954961099123,
                -98651.23439694449,
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
                False,
                False,
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
                '20220523:220031.448908:+0000',
                '20220523:220031.448999:+0000',
                '20220523:220031.449088:+0000',
                '20220523:220031.449175:+0000',
                '20220523:220031.449261:+0000',
                '20220523:220031.449353:+0000',
                '20220523:220031.449440:+0000',
                '20220523:220031.449526:+0000',
                '20220523:220031.449613:+0000',
                '20220523:220031.449698:+0000',
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
            'name': 'щӥѫҮ˳¡ԭNґҴƨ¡ƵʶȞǈѽÍÏĐɆˀʋĦҠƗΧЌɄǅ',
            'value': {
                '^': 'int',
                '$': -6732773528116306719,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ŵ',

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
            'catalog': 'ĢҖˈÚŊƧɮӸĄӲͶɑƋ˾Ħǰ\x85ƆŧΖřӍӥȦӜȢ˵ʭЕΒ',
            'message': 'ıӦȟǇďқƞʐɇ°ҷ¤ʦфL\x91ӏήIɯƵɆįëHʐѧӒ¦ʪ',
            'arguments': [
                {
                    'name': 'ʳƈɍťƨԡϑÅӏÖȃѩʲ\x83Дԧɥŷ¡ͻơЀϺРČƈʺÈĚƋ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20220523:220031.431320:+0000',
                                        '20220523:220031.431406:+0000',
                                        '20220523:220031.431488:+0000',
                                        '20220523:220031.431570:+0000',
                                        '20220523:220031.431651:+0000',
                                        '20220523:220031.431732:+0000',
                                        '20220523:220031.431813:+0000',
                                        '20220523:220031.431894:+0000',
                                        '20220523:220031.431975:+0000',
                                        '20220523:220031.432056:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ʋԧҲ˦Δ\x84Ďϥ˶ЕǼś˻˝˗ʱԡ½>ȢAõȍ\x9bλԭвοȳÊ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        147101.5741136411,
                                        678355.5319639894,
                                        588587.350998513,
                                        837110.762958544,
                                        297998.01084536884,
                                        506254.4977507554,
                                        111911.92602239415,
                                        325552.4239714792,
                                        526936.9617645862,
                                        902139.526572571,
                                    ],
                        },
                },
                {
                    'name': 'ӷFãκĳǒфνɥGŞ§ΥƶђԎӷΨɊBéʾûш\x8cпҖ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'тDĔʘ҇ΥƐϔéҽӑ-ӑ˗Ϸϭ˖˟ӣƇтƾâʟˉ\x95Žѝʠе',
                                        'ƧƲŕˣҲϼԡɡǡԀˮήӖԜӽёĿѩ\xad\x9dÇ\u0379ǉ\u0379<Чϵѵ\x7fǊ',
                                        'ԚȸʨĵϹ\x84ϛ´ˊʶWʁgǛ£ŽœŎӴǂϡЦ\x83ωĔӿŽεԥѾ',
                                        'ǡƇļŋϗÕԑˉľʵϏȯÐʥԌӯOϬϛđ¯ǭņņ\x9f©ӕŋȖҫ',
                                        'ϜϠДӼˁΨˤζѻίh\x86]Ɩ\x85˓ɀƅЋЬΰȢЈșЫҲɯχɡO',
                                        '¬\x97ԭ\x9dŔɎǝ)ЫƮʻιԋȵ\u03a2˴ΑѸɝшǃϽԇυԃĹȥз\x9f¡',
                                        '¡ñɚOưǼûЮήʂӕxвƂȁ҄ϹΞКȨɏƱтŁ˶ĨƙȜƐҬ',
                                        'ǀџ˞ӍЏƊέѡԉȫΩpΩɾȅCΟиŵĸĽÓŘӢʳиŊĻɧĊ',
                                        'ȗ®ӲӰ\x92\x9cƭΗɉáϊũɗǿӽνʹǜ±ŖѥʃДŜӎȋϠ\u038dҹǎ',
                                        'ƅĢƋӅһ"ƇȽò\u0379ɉɽѽƑ˯˱ҨŃϊԦŌӠĹӽȮȈȿҨЭɲ',
                                    ],
                        },
                },
                {
                    'name': 'ɮΤ˝ǘ͵ӇЊɳѦΰ±ТɰӰ˔εĎӫʖÏ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ŉΑʖƱ>ӃǦ¨ʌҒ]ÄԢΛƮѾÚӸ҈ϢéȟƳʿ˔ӂÓuəϹ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ΊėѬÜɃǢǈҶˢɱҋȷɜοğԪЅǶLˀјҬΕ\u038d¯īӷɑΊȉ',
                                        "'άȰ϶ԄҧƢeƸ£İŸŶЄ<ěĭc\x8cԥԃѨԝʝˍėɩ½ǿͽ",
                                        "žύϸѸɽȧ¤ÉЏɭґǅчѨКˁōΠȷԄH˭Эһ'˴җŇу˭",
                                        'ӺѨуЮKΊƇȊÉçȆÒķŁʚ¡˰9ōGʥdƨƛYȹːɠ˷Ϗ',
                                        'ǃЖѼЯȦȳİƪĞo+Νøâϟɯ`˔vǞǢǩǒƱȀʠƛȕɺӦ',
                                        'ϥӨыүə\x83ʉb҂ӢǑβ˺ŀǌӮ\x98üʏʷǛ\u0379ӬԟɂǓѿқü\x8c',
                                        '÷ӯVϺԥйЁA¸£ђԂĀȴЉѹɧкăťƚîѻʋ\x9d\u03a2˱ʳƩԋ',
                                        'ӑљΣԈδђ7ʡƟӴ5ӵëшŶӼҪ΄ż\x93Ɋ˚ƄȦҾȷϋϪú/',
                                        'ʉǝƅƸǹÇƖíʘʚŮϯȧԖσ˘ӌωȎqԧʼԟ\x8eƴŉоӢřȄ',
                                        'Ӵ҇˝˝˸$ʏʘ˶ϥēɸƠϋY҆˗ԟ\x9dпŤɢȀϡƊą3jҚš',
                                    ],
                        },
                },
                {
                    'name': 'ÅӅԙУљƃȮűȡІίϳ',
                    'value': {
                            '^': 'string',
                            '$': 'ǎΝͱԄџsғğʆ˧ςњòӮɅ҇УГΞқƉƼɛɚȪүѢҪʖӊ',
                        },
                },
                {
                    'name': 'пˑ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20220523:220031.437554:+0000',
                                        '20220523:220031.437639:+0000',
                                        '20220523:220031.437721:+0000',
                                        '20220523:220031.437803:+0000',
                                        '20220523:220031.437884:+0000',
                                        '20220523:220031.437965:+0000',
                                        '20220523:220031.438046:+0000',
                                        '20220523:220031.438127:+0000',
                                        '20220523:220031.438207:+0000',
                                        '20220523:220031.438288:+0000',
                                    ],
                        },
                },
                {
                    'name': 'Ԫ҂ȉмȎŗĄƵƽɂŇҸÞǧԮҜɶ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        5527781667620480773,
                                        -3991276473566787228,
                                        -4197185820406979039,
                                        -5092454295166088462,
                                        -3571662890664415059,
                                        6416958985816811723,
                                        -7036974264118401036,
                                        4001854487708247395,
                                        -1942339503191010949,
                                        5468995157594698982,
                                    ],
                        },
                },
                {
                    'name': 'ǓɲʻɐɠNѩÃɠӞÉΡќâĚΈʴķӱԮʀЪƦtӣ˨ɍмӅӁ',
                    'value': {
                            '^': 'float',
                            '$': 700061.9514663768,
                        },
                },
                {
                    'name': 'ǯõĸ˄ƕ}šȤĮɎȿϨϑӅƄЀƇƍѐѬӬ˶řΤȑҗ¯ǖɓË',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ā¿ɇɆȱѠɦɭ1ɸІͲъҒ[ХҍӔӝ%óƤȟ˂ϣäƄƳʈą',
                                        'ǚɊCuеǇǩĨѰn\x89ӭ\xa0ǈʰνбǮаЪ\u0380³Ыʶϭʪ˰#ǧƦ',
                                        '\x91ʭāӂҌǫʚɛǬǯȣҶϓӯɓӈ$ԭǞĲžўХǣɬÑϬѦΔҊ',
                                        'ɷĈҊüĨыáźʊȜʕɋ¯!ƅ˲áϕԌĝXƛԕРЁ˖ƮďoП',
                                        'ʌ,ɸÐǜªΜΤǎϡȨϓƳǘηԥƎœӣƸѶ|ǒ͵4Ӗ\x8f˱ƷŤ',
                                        'ҳǁÓʪİϛɀ҇ŇҌΉƺ)ӯϹϖΤёʸ\x81;ŗʃӯˎƱʺʯʕǅ',
                                        'ҩвzЏȍʝΑ\x85ȃҕȡӴƴ¸҂ƂΦ\x9cˎϽÎПƞԇ¸ϫǊҙř`',
                                        'ʋǎɍаήѤƝŢɀʙ˞ȧMèȦƽ¯cӠҊóӘɫʍԓŏŠǫԦʢ',
                                        'Ğ\x90ѲӾΈ¥љРK˭ϨAѓ^϶OĶȋ¤Ȕēŭąƞ\x86\u038bȴѾ҉ʇ',
                                        'Ġώ¤˂ûǯРÔŔ˰ТÌú˷¶ҵZǃŎÉėԞɸȖҤĈƩѮˁˠ',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ԗ$',

            'message': 'ь',

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
            'identifier': 'оƺȽË\x95ʴÈǴϣҺҮƲʧЋѕǐϚªŠΓ˓ț\u0381ѲъӕμԬЌД',
            'categories': [
                'os',
                'os',
                'configuration',
                'access-restriction',
                'internal',
                'access-restriction',
                'file',
                'invalid-user-action',
                'invalid-user-action',
                'network',
            ],
            'source': 'ĿҒĀTɣŉäԧʟ',
            'messages': [
                {
                    'catalog': 'Ҍӽ\u0383ǤźӈŌɆɔ·¹ť;ɛňźӝΔÏƮЏҤʭԝˍǪ¼ѶиƋ',
                    'message': 'βʤ¼РҵʧȖ3ƸĭӗǺżԭlԙҪïѡӃπμJÐԡӘɱȖ·ɦ',
                    'arguments': [
                            {
                                        'name': 'Ư˳ʼɤќʸǵҞź\x82ŀĴǈbϖ\x97ʧƅ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -740830255064810492,
                                                                            -7326490048261966884,
                                                                            5064230872095059698,
                                                                            7515392865980859388,
                                                                            7080469357832914000,
                                                                            563409708261777940,
                                                                            514699265011545455,
                                                                            303922602639748084,
                                                                            -3514417486215525257,
                                                                            -1363019006246360002,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ü`ȿљƵǣĭ>ϰͰĚͿҁИӜшý\x9cɀŶUɘǂˈǀҢţQɷӖ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.344263:+0000',
                                                                            '20220523:220031.344347:+0000',
                                                                            '20220523:220031.344427:+0000',
                                                                            '20220523:220031.344506:+0000',
                                                                            '20220523:220031.344584:+0000',
                                                                            '20220523:220031.344679:+0000',
                                                                            '20220523:220031.344761:+0000',
                                                                            '20220523:220031.344840:+0000',
                                                                            '20220523:220031.344918:+0000',
                                                                            '20220523:220031.344997:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҿ2ƁʖΥͱȪʀʥɀϗǺԝŻҫОǑǴΨћν5KЉɔѼʾǶǒ\x88',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.345594:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȜćŝˤĠԥΙӯńҙ\x8bČǶá˩ϾИoϔϰń\x87ĦҤɐMҼʦ´х',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6064625543765636618,
                                                                            -7516666053146103581,
                                                                            -6259603824119686560,
                                                                            7097931327316362829,
                                                                            -6320317533772521211,
                                                                            5556210646402339454,
                                                                            -9196117510424203481,
                                                                            2566484500517065467,
                                                                            -7821044748274439472,
                                                                            -440164261613110643,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƞ¶һǸ\x93ЦȇƜɷӢǹ˹',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            353624.4223282612,
                                                                            585513.6350511311,
                                                                            260637.72969859117,
                                                                            37078.81859156009,
                                                                            341170.5644216829,
                                                                            386592.9281723027,
                                                                            785647.7641849625,
                                                                            362913.7684733951,
                                                                            751964.4986278585,
                                                                            986825.9145634619,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ґǔ?âÊЛςĵ~ΑԫȍƜПѦĿ˴ƫԃҀʥƄƮʢӺϙ¥˖ԣԨ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.348434:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʟƚύǩ\u0379˩ĹҎҭ˯\u03a2)Ј˯фʄǌΡԁʯ;ҚãӯǶԪɺÎǫĤ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӊǷiǶ˷ͺFµFȮöƉЂľșІȥԎϘĵ¨ǷӜʜŗ˩˯ǄϽÀ',
                                                                            'ԬøȳƦYЁΝĺʹœɑӌŷΐąäĴԖÜρhи\x9cǡΩяаƞƕ˼',
                                                                            '\x8fāѧӨЯѴĎԟȴϚΡ˸ÜTҼDϺ\x97ҀƱӊÈƼçʏ\x91ԂеȉҖ',
                                                                            'ͳÃżÞȓƗŹνvɰɶɅǋҗdкȭȗưì˻ǒ¢˹Ĳх¾ŗкʓ',
                                                                            'řȶÏ6ťЁ˗Ϯ5ғҧԃūХӃśӐōiЈͲ½ν1Ĉ-҅ӆDę',
                                                                            'Ω®óǠŦЃԅʑϴӻȘһÄɕɑ˚ɷ¥Ҝɑы˾ϞϧԈėͱұȝȇ',
                                                                            'ӇŒǐʫʆkǜȴӠɵԈιȗdӶūĊѴҮǬҴacĈϞŮҴʡ҅ŗ',
                                                                            'Λ)ϿȃˀȒѲѤ¸ǲȦeɍҳʣɷƢѡϢŊӿɂƎ\x85\u0382ҏŝӟƢŊ',
                                                                            'ѺɸǓЛһϻ6ĢČʼWӣȭԛŋưҒʃԬȃǰƯͺʱΒӃɭNԮ½',
                                                                            '҄уġ¢ĖɕѪȗĨɏ\x81Ķ`\x87ХɅŢˏΈmœhʰʔȈ\x8cЏѽѰĖ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'HȡΥϲсʵʸǼӕԑҥȉÈѤӌǩĠØ·ìϦ˞&ͱӂȅù\\лӴ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7610546408147391127,
                                                    },
                                    },
                            {
                                        'name': 'ѣźUЙíĳŭ¿ӉƳʿБΠÄѨ\x92дéɵÉеuҿ½Ƃʵ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1417091273078412548,
                                                    },
                                    },
                            {
                                        'name': 'гЊчʣҶюĥѽ]ʈϥзӽȠЖ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.351074:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɍȱǺЉ8',
                    'message': 'ԍ˗-ӽѝкѣɊƝɤƽΰvΏԟҡϨΝ˥ϼπƺNΘŪ!˦ΞŚŁ',
                    'arguments': [
                            {
                                        'name': '¦υҎδԩђĶ$Ϗ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ЃĖ"ц',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -58652.85371786231,
                                                    },
                                    },
                            {
                                        'name': 'ƞѵҡƉʆ3\x9d´Ц˚x҇ʑͺ˛˳k϶ĴŷӃǉǹ˨Лñӵ˻dǞ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƚʜҏЫƆҵāʦӖʴȍąӪԧĂƏƆʔǦϛ{łүѾи·ɭɟɜˏ',
                                                                            'ƝńĆ҃ͲýĚќċҐCĵʦĭʮʜìԄèȏƺǠǝѻǮȅȉӶϑμ',
                                                                            'Ζ@ɡӬ\x86ԆɀɚŌěѨ\x8cԊͷƹϑś҂ӠˡʸÝÈ«ϚƲѕҫҭϭ',
                                                                            'ǬӮȥ4Ҋ©§ϠżԀȳОıв´˦ѶUļӘԖӊ«ҋȾӋǏĚуƳ',
                                                                            'ŎӂéϩɡĬаѠПǩǝϢĖѯʧŬ϶ϳ· ҎФF\x9bƃʥāӝÍŉ',
                                                                            'ɦɴʃͿќȤ\x91Ћ\x89ϯƠΓʧȸѶҾˡǇĂ\x80dӿɇЉϷТ˝\\\x97Х',
                                                                            '˵ԂΊºԏѓαľl˶ĴǏѹ\xa0ǶЈ1ˍϵҖӊτǸǇȄ˥#÷Ɣń',
                                                                            'ȾɠӉʰǣːͺȀƀPƤѿȬ˝òσƒƼή>эɨԑŸҥѤЀюǠѨ',
                                                                            'ԭĠæĩӊZŹͷĂ\x8eЎď\x9bŉԑͺĺþӗЇӻþƇΦύǟXΖ\x82\u038d',
                                                                            'bӃζǰˈύ¼bɠзόӫĻВωϮќΆȴȬgɻơȸЮŋΞПíK',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ч^жϾʅǡȹȁǸϫłɇѸɢΦǮʄžč',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 287327.88000903593,
                                                    },
                                    },
                            {
                                        'name': 'ѸìЗѪƇɄɹȻ[ëћɻį˱ʟԂЕ˺ƽϕϕ¶Ý\x9dʪȄƮҙŶɭ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '·ųʻһ˵ǭѾȤоѥȠŌԫ*аƀҺ¦Êõ˪ЖȜ\x9f',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8673813071623973442,
                                                                            -120474839882657278,
                                                                            -7562553451478507293,
                                                                            -923489247553444224,
                                                                            7466889359416210211,
                                                                            -6667249202748072482,
                                                                            -5701445330650082411,
                                                                            7524407980814858292,
                                                                            -6511443843346521209,
                                                                            -2327760831039386530,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЂдʛŉкδΰԩàϚ˕˚ϥ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 524177.4533279756,
                                                    },
                                    },
                            {
                                        'name': 'ӠģΜQɋԜΐͲÙƁ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ƽȧǍ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 737357.496955475,
                                                    },
                                    },
                            {
                                        'name': 'ϠġɳчǐGѮˣ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6908473912632571240,
                                                                            -2669111552108102729,
                                                                            2351572920868087281,
                                                                            -6118086127449496139,
                                                                            6868452369295695445,
                                                                            -7527049710056798504,
                                                                            2863407632889380718,
                                                                            7191042146208725912,
                                                                            409680396010773645,
                                                                            -7557691461808725270,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʹPʗķ?]¢ȀõΌ|ѬӘÜʳěҧƙ%Űӑ\x81ĳťґȘBʁҤĂ',
                    'message': 'ʵīԧĜ˖ŐƀѳӫҤϟ˒ѻʰӌÏεйÜŃϔӘӳǡ»β}Όýʘ',
                    'arguments': [
                            {
                                        'name': 'ȝŶԔ[ȯ{ʈÓϡĒуʿɞʶˁȇ\x84ʆʲһѦǯ;˦Đξ˽şλȏ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ΝЍĄɉNΠҽĜяŠÄ§ŷ#ψы',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȵѭýğҔÌġзǠDҔҎɷωʍȻnԐʤЭŇϟԨīҭmʋɤ΅z',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ːʲöƂ2ˍӗ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ύɒҬ΅˦ƙğƆʏŌӲǂĀӸѼԪ¡ӍÅLƙ\x89ȵʳȐɖɜ@Ş\xa0',
                                                                            'а{ɱόҒͱԧÃµˠ\x88Sөéүʋɓ«ƞϘӖǎȈǨ>ƗǽkɾŸ',
                                                                            '˘ƥʲƹƊʵɖɃԟį[ɞǛƍȯӼÐåŸĝǥʘƼĀţѱˆΦҞҊ',
                                                                            'ʭħSǚшѺŽѱϟϻрĭǑэƄӒҌ˅%\u03a2ƛʭϤЮ\u0380ǁηȔȐ҇',
                                                                            'ãҼьЋҟөʇăƅǄ\u0381ŧĥƂʸŋĩĈ\x8dӋųȡıŌœӚĆЫGƴ',
                                                                            '9αʷϢɤěѨȎý϶hȬГðҍԃ˹ƽϘåВęǆǲԗʽĭ`Ѫʣ',
                                                                            'ǝуҡï@Г\x9dӡэƂĸά]µzѯуцȁNӚʬΐӣʉƾƩǫ\x97Ԩ',
                                                                            'ČϓĀ·Ƀ҆ӣПć\u0379ы˗оԊɂϨĪŏǵʑ÷ϝΔѱ¦қͽΎĚˊ',
                                                                            'ΩӡȅʒĺѝƋѽʑƳҹĳûйƬÇӀ§ǋðЩŢҫơŘ:ҝǷǇÄ',
                                                                            'ΨͼȊ϶ӑұʷΆöĪέÆаʠĥЋǎàšȘȩЃԬǵΧΫŃĵFȚ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǓѴ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ĀǫƏмпƾɮϹӓЖǨ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "˔˥ũěΈ\x89ѮϞïЯѺōԛδ'њɵ|ѺҘíԍѩӺöǮǩ®Йɋ",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.364086:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƞ³ȡƪˋˇɹȪpĬƽĦ˩3`ƺҫǥϔÙěȫҭсͼфκϲŗԠ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9102711375705964089,
                                                    },
                                    },
                            {
                                        'name': 'èʖɘŉϽɡΦѾ§Ĺȃ˟ɰƉ:ΆͿ΅¸ĒэԔʛ~',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.364936:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ğԉǖʵΫǎгŻԒңΫ«\x95γŶüŭȀ¶lʤˁ΄ɻјɇҋѸџε',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.365477:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ˏΛʇMίǉˈџҳɳª0ĕˉľϏɒȏɅūȌŻѺԉ˃ѭҸСӌȥ',
                    'message': 'Ǉ\x8fү˂«ÚЇҦĉԏƖeωԊƨԡΎéìďſϩңȔɜȂŘɵmЦ',
                    'arguments': [
                            {
                                        'name': 'RɹťЙ˫ç¢ѫʁʕѨēиĄЦť˚ƉԋɫƐɺʨЫtāԌ`Ϡ˚',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            77112.76231132736,
                                                                            213389.10909724882,
                                                                            510544.7672255996,
                                                                            2107.763633621915,
                                                                            864989.3123602198,
                                                                            188879.78601869015,
                                                                            34606.42161916869,
                                                                            964785.3615411851,
                                                                            493419.2234958013,
                                                                            -50954.11664736921,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǕҔԅѩȼʝǱQ҄',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɻeʑӓѰίŤƽĔϧȒǘЭ~ɝ҃ǯoǇΞÌ]¥ŶĝѰiӪПǀ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŘˋΧȦAº³ȓĳÜΛ´˝ʍ҅˪ϻӎϲƗѪŃʨ˪ӿүң\u0378\x82˜',
                                                                            'ǂϚĘ©ѱbӗҋīŬρȯ¯ɦɧǇǘȒПѩЦ˧ҥȠ@ҠӚâŃŵ',
                                                                            'νŴҜҸǌ˩ɠEϡȂGѵȸŌʚѼCɣí\x9dҏŕ˫ɘˈūӉоˈѦ',
                                                                            'ɑ\\Ļhʰ4ŜiĊȰζǾ»ƀΈԀȒÄűɸΣΣ¥ġãӟѫԧEb',
                                                                            'nǦÀ\x90йԙɧ˟ĵРʗθːŝȊ¿ˢ;ȹëƦ¤éˑːǺʊ˓ȗϛ',
                                                                            'ɊǇȁ˖țʼΆБǙĳ,ϖϹΣ˧ÖʇŞpƟђәƇ.ӤЃςɮĺϝ',
                                                                            'ӫâęІ˗ǩ˅ƵҦ\u0382Õɲ³ҨŚĒ"ÔíϚфϋ>\x93\x8dËɔу¾ƪ',
                                                                            'ӣńͺȪ?kΜӂ\x7fӾϑэ˜ɩǝϣԦƂμʼϤHκӒѝŕҾŵ˦Į',
                                                                            'ɳʠѬrҖͺʊɠ+ѦȘҺ҈\x9bȐѪʆHҹ˴ҭΌҩԣÄƖҙıˑп',
                                                                            'κ˳ƖӶĞŸ ήλҾlД¶ƸĐл˒˚ųϜҍűɒ¶˩ëЅѦĭӛ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'NӇǗӲɪһǘӕʵ˻ǄӪĐđ[σ¹\u03a2ыЕǤԑˬ\\ϹͺˏǵĊʬ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            734991.648144752,
                                                                            818901.0771839445,
                                                                            787083.1779717111,
                                                                            543086.9122078728,
                                                                            355326.87717374053,
                                                                            841523.7907660456,
                                                                            661248.7214751948,
                                                                            353822.22879852867,
                                                                            251360.31452939543,
                                                                            737144.27493924,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǔïОŜ\u0378ҹϴ˘ϔЏѕʞǳЭĬοŞ\x96˟ɻĸĕЧÒɋԊ\u0383ǧӖƉ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.370689:+0000',
                                                                            '20220523:220031.370774:+0000',
                                                                            '20220523:220031.370854:+0000',
                                                                            '20220523:220031.370934:+0000',
                                                                            '20220523:220031.371013:+0000',
                                                                            '20220523:220031.371092:+0000',
                                                                            '20220523:220031.371171:+0000',
                                                                            '20220523:220031.371250:+0000',
                                                                            '20220523:220031.371328:+0000',
                                                                            '20220523:220031.371407:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЂɦίӺłŅˡκЃϋɀϘ˄țĮÑ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '҃ɨӦϝƶ\u0380ǅ˞ȉĢǐǪҌȮΝ˺¹ƫˇǺ',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҠεʽņʺʥԪʀПʆҝ˩ρ\x8cѡˮʟˮϞϱƹȫ\x8aƦҖ϶ľǒҩː',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -820791314845352771,
                                                    },
                                    },
                            {
                                        'name': ' βĦ\x8fÂ\x8dʁʰƴӇE×˓ԙƅ"ϷνΆϧпіȐσ\x94>çǉҌʢ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ϯҷȓǢҹɊĵȚȶӔČƃMɏ6ʛƊ\\ȑˉΉ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2174844241205261798,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ɋ:ƴ÷҄BϬʤ˜ϚŠӫ[ȝȅзԪ˴ß,ϠҒϹП˃čƼˎˎ5',
                    'message': '˶ˍȖӽEϬԝȄťɃƚћќϩɴӔĎҜʬÖҬǿı˫óȾξįȇϏ',
                    'arguments': [
                            {
                                        'name': 'Ȥ˺ÚËЪϘөʋj\u0383ԂҜȊОиґɳƀŮÝȼȪҟˁĮʴɵĜµæ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                                        'name': 'GȟÍ)ϓҁúьȰ¿Ʈҩȉ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.376617:+0000',
                                                                            '20220523:220031.376702:+0000',
                                                                            '20220523:220031.376782:+0000',
                                                                            '20220523:220031.376862:+0000',
                                                                            '20220523:220031.376941:+0000',
                                                                            '20220523:220031.377020:+0000',
                                                                            '20220523:220031.377099:+0000',
                                                                            '20220523:220031.377178:+0000',
                                                                            '20220523:220031.377257:+0000',
                                                                            '20220523:220031.377336:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˾ϜŨΪùӐЩ6ǆˀƧё¦',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -9019681784196926270,
                                                                            4259565186993757257,
                                                                            -6044804030142910614,
                                                                            5342762913851854858,
                                                                            -6376103370082514906,
                                                                            -8099439147305820196,
                                                                            1275976223051809132,
                                                                            1227396032562002442,
                                                                            7502151171686752737,
                                                                            3668787820144212063,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҂ʀҮǃǋҝћЫȤÄѰиǓӭǏ˨ɩϨƶ\u0380ƪĉ\x87ΰȧĀǸιҬҬ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӑX³XʆżÐĦ¦ĖȂ7žюР\u038bӺɻɭџʥȋǁñϲаʆƬƧӱ',
                                                    },
                                    },
                            {
                                        'name': 'ȳѕɍ\x81J\x80',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': 'ʆŜtČəӆ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƙʄ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 311443746648187679,
                                                    },
                                    },
                            {
                                        'name': 'ʃҞѐ~zяЀθʳұ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ơр˹ʙťƟӣȌϖϓӓçіʛǔωԚĖȗЀǉЮˡɝ\x8fȀПɎʌs',
                                                                            'Ɨ˧ʧƧԛȿ\u038dѪӢԁĺƇ˟ͽȂҏ\x8eňΖǠŲÍēϞȄΌӿŜԄҬ',
                                                                            'ɂԮˁԚЅĸϣŭȨҳǆԌșҗǪɕϵҌLΪĒìư˶˓ҷɴ:áӄ',
                                                                            'ήπɎнϘ;їӐĩӼ˵ʥįȁаƎɞϱӔȣϥƩʫҾ¶ˀ\x8fǒϝò',
                                                                            'ʐÉҡƺųúԢƪţ9ā£ξαγĘ\u0381ӛǩўêƭɐǅĬӥϵãǞΥ',
                                                                            'гͿѬͺзǟХɡЬŵņɽ˗Ӕƫэ´΅ƨҦΆƇɢǾѧҮĶ\x7fӂђ',
                                                                            'ƅǁӿǝ¦їҚÂөͼK;\x89Ѩ÷χӘ©ÿѫčŀEɬӡϊƥǦhи',
                                                                            '\x8fƼԌǚкҔȥԊʅϟДŵɿ_\u0382Ԝʲǔҳˡ˂ʷ˕òȢʮĂʵʵҠ',
                                                                            '·ʓƶƚªïšҁӋԂāşǓˊɍћӸǈӣǩſŽ҄èCҞƻȥɏb',
                                                                            'ȬȺŅ\x83ϝfЭϘФİƝӹǤlòїέǝҢʷǩ˾ʷɺӑԫӊţƋη',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ыȁρҌͳrϒǩςˤǅѝǘŕɰIѴ$ҨåЦŴƚӽºɁǊɣψř',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ǎÄϹү\x95ʎǘěΩɃʸӛҋ˩\x9bϥNƬɫ˕ēΔɕɇʢ˪È6¢Ӈ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʇȦƂҋΠһɒσȧЫȤ(ԃÎћǝϞ.ƃ\x8b˞ɶʜǩʵѢҭӭŅʴ',
                    'message': 'ΰҠчEmǧɆʽφĞҝѝӄŽ[ʚ\x91ΐ´ě˸\x86ȄαѺ҈ϿǊƵǒ',
                    'arguments': [
                            {
                                        'name': 'qНíοϲɎЄЕ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ͳ\x93ȈƧȶϢӪɀϾŷљК/M;żĺǔÑǋ)őӻȑȹɌМĚΎO',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ў\x93Ҩƣ9˻ǕϻϖLѲжbʻӉтǃǬҗʢğ=ð',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.386694:+0000',
                                                                            '20220523:220031.386777:+0000',
                                                                            '20220523:220031.386857:+0000',
                                                                            '20220523:220031.386937:+0000',
                                                                            '20220523:220031.387016:+0000',
                                                                            '20220523:220031.387095:+0000',
                                                                            '20220523:220031.387174:+0000',
                                                                            '20220523:220031.387252:+0000',
                                                                            '20220523:220031.387331:+0000',
                                                                            '20220523:220031.387409:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'њ«:\x9fѸʫƅѣ\x9bǑĩʷΈwͻӍ0өŷӻҜţ"Pş\x91½ʐӼӏ',
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
                                        'name': 'оҙѶΎЎЉÆʔżɸΘŠϪČòɰТ¬¦Čë϶cƚàǕёɥԬɇ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2864865206949126107,
                                                                            -2915175611399155678,
                                                                            -955582474052122436,
                                                                            -7599496700670867398,
                                                                            2808847446495943084,
                                                                            -4165460688376748513,
                                                                            -4925754889929665249,
                                                                            -7969544205351637894,
                                                                            3073993433675313024,
                                                                            1508557339831436693,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǽ˲ŗŏөԞˢȩ]҄¿ЙƗźůЯ·ҽɨúǏӾƕƫϽѸЩӷɅ¸',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ңϕϾԍʩ-Ʌȃğ˴иΛǅhĈäǎɍWƁŵԀšэɰ¯ιƵ˼}',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3404318636421287334,
                                                    },
                                    },
                            {
                                        'name': 'ӔοϽғx˂ЯɪŒϑԞΙvЫłƔÅ+ǀɘʮñĚȑԣԩΨ˶Ǆх',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            505924.54911450925,
                                                                            502740.9797418446,
                                                                            249084.62014390744,
                                                                            492533.88815100805,
                                                                            536613.4638222792,
                                                                            929285.8442518293,
                                                                            81029.94676092648,
                                                                            293634.0999289184,
                                                                            273635.9680690123,
                                                                            202928.70590758446,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɋ`Ě',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 499407.9347669503,
                                                    },
                                    },
                            {
                                        'name': 'Ҕɏ\x8euǴʧŉӈ7',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1986393307532430097,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ȥ\u038d˗ǂŘʪёҊ˾ЄȑӰҙӠ:ʵʩŤӛоƊѕmͷɷͳӦ˜жѤ',
                    'message': 'ΎʤĵӝŬɬԥIΎȻʅϖčĉǭɾʮШмԊȄҲɃȹҁƙǶȾ²Ɓ',
                    'arguments': [
                            {
                                        'name': 'ŪˌǝƤƹЀΡɨŒЁ\x95ȮӥƥǉєţёʸҜπȍϒņĽʲ˗*ҺĆ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'PǝŅқˎȸȢιů%âфΕηɨЯѿοҭċКˏѣˀҵǎǙdÞ˼',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
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
                                        'name': 'ĀӛʘɃώӞĀ<ĨԚԀ&σ¨ȉѪԒ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŧǗƣTÚφ·ſƦԬơȺ\x92ӽ˫',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.397454:+0000',
                                                                            '20220523:220031.397539:+0000',
                                                                            '20220523:220031.397620:+0000',
                                                                            '20220523:220031.397699:+0000',
                                                                            '20220523:220031.397779:+0000',
                                                                            '20220523:220031.397858:+0000',
                                                                            '20220523:220031.397937:+0000',
                                                                            '20220523:220031.398016:+0000',
                                                                            '20220523:220031.398094:+0000',
                                                                            '20220523:220031.398173:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȐƿОǅ\x90Ɩî¶ɡĄþӷɧΙӗȵΕҹĀ\x90ǙQɒAɜ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.398765:+0000',
                                                                            '20220523:220031.398846:+0000',
                                                                            '20220523:220031.398926:+0000',
                                                                            '20220523:220031.399004:+0000',
                                                                            '20220523:220031.399083:+0000',
                                                                            '20220523:220031.399161:+0000',
                                                                            '20220523:220031.399240:+0000',
                                                                            '20220523:220031.399323:+0000',
                                                                            '20220523:220031.399403:+0000',
                                                                            '20220523:220031.399482:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǿеррˌƒ°ɭʠ˩ӅęϱӽǄť©;ˣƳѬōӒ˂ƣЖʻҖо5',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\\ԄpϩΑϢŋζ¥Ōҕʚø˳ͼ͵Ÿϕ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӵΑΉƏǺƕ\x90ũβцԐıʅ/Ғƶ3ʠɀƖϴԁěėSùš҇Ԭȝ',
                                                                            'ˉԇӍԃ¯Φš˰҃ӈʸ˪¡ҜˏўǺǙԆɄ³űąǧӕϊǚƃ4d',
                                                                            '҃¦Ƿν¾ҧºλǘdэàȈˠʦѸɣŁī˭;ȔÞĝŏ\x83ϗƈȄę',
                                                                            'ʱНÉƍΐӏϧԫ/ʵȌРŤҝйΰˋԁƮĕԅ¾˚Ћłȏɥʁʋ¤',
                                                                            'Ҥ\x80ӘʤϖŕƚφԤӃ9ƂɹάāϳŉĒG˸ӷԡʦΛХ{ǇǸӠˎ',
                                                                            'Ĭ¯Ì*ΔŁ+@ЖҍԢѸҳ˵μ˴ѶįϷϗͺŔΔЖτӏƚȀǸϭ',
                                                                            'ԃɍʀ\x89ûέĒʳǊɦϹȪgǣǼδϩ\x9c\x89˨ŰΔŢԍƎ˱ҠĤԔ˭',
                                                                            'ſψʯпǽɖϙÙśͳфŧʳƲŀԂӡƯқҟĖġӧԕɹԋɃťȤƒ',
                                                                            'ѩGɂ\u0382ӫһżγ\u038bȗȶʪМĺ\x8aȒҹǕʣӳéđҕƁǻƲóͱάԕ',
                                                                            'е¬ɈϖƖΙșƾєӕːÌѷ\x82ŞӮҢ΅ƑƦƳēͿɕhйԛ˷яj',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĉ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϭӋԆĈыяʝʮêɺˮ˛ńϦȇĎРƘϹȚ\x96ñФģƻӱɖҾʓΗ',
                                                                            'ӺӹθʃИɣɺх÷ϲԉ4PѥΒϣҙёхѹͽ\x94ɋϋ1ʺϒȚȮǶ',
                                                                            'ȘɾơéÌ$ҶŞ¤ӜУϟѫтϗĩÜǡӾʏ\\ΓiУIΥ\u0381ӤŃŮ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʕȫΔ`0ĲXʡԝæЄϗѕǂƓ΅ǹϐȀčаԢбfŴ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƞüŎǠПɣ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 47408.225635884795,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ԅ¶жƫɜǉʆԆϚǚĞŲǡwԣƀԁĵǟӍǛʉΈԜ_\u0383ӶƵʔL',
                    'message': '˰Ȱ¿ΧʪΑˢı¿ҠĊʣ¥\u038dêҢ҆nǃɉDһlųȰȖҲ\x98\u0382е',
                    'arguments': [
                            {
                                        'name': 'ҶʛɲņӨ˔ӠƏêӪȖőӾ\x92ʱԩ˪',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'έϗȿԏʀȟ\x87ЂЙȣψ϶Ƣ;Ѣǳ\x7f0ΆļД\u0381\\ҁЈӔʶԬѰ"',
                                                                            'ëùҐϨҥɴšɊ«͵ҦƗу\x9fƫbŦǞːϔΠфßӻ·őşȍƣϊ',
                                                                            'ĤĒĢɚԓˡϕwǉʅ˧˾ѱʨԑ!ҪǎˤʋιӀԋȹ¹P]ҿƖ˝',
                                                                            'ȓѲʞyȵ¦ѯѺНƎŨǩÁԡΥ>ŭȕƈǇȖÌ£ҰɍʄŶèŔɴ',
                                                                            'Ɋ˩ǃȃҽХəӒÑŋЛ¥ĢÂņѱʂĔ?ϾҞóЯŶľW&ȱʘ6',
                                                                            '˨ɦ¨ƤЌʆԪІŸÔˬȯϭӷҭ~ЗОůmЪš\x82ɬȿәĻưɸɀ',
                                                                            'ԄʈɴĐοsɭʝϒɆő©ǚ\x80ƇРϫʟȚиҐҩ˴ȔӉˇη҃ͻĉ',
                                                                            'ѭÓÐʰǄRĸɀƽ³ɝΊȕӍϙҳӼiθĖЉƢϑȀǎҍҺJɗҡ',
                                                                            '΅ĴÉҜƠÄƫōЎѹĞҶŗϟŉʆǅʏ<ПȳЗ%ӀɷȭʍԝҨɒ',
                                                                            'ǯɹķϸʕ˲ƺжZʊǽaԫʈ϶Βˈ\u0380ʶƭ˱ӋǖѲ\x87ʖâįЯԃ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΪņƪʱΦ\x88',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -127720815110937624,
                                                    },
                                    },
                            {
                                        'name': 'ƻ\x86ǿӹ"ǈĢʊ\\xμ\x93H',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȳƝŭЌʺψӁɊːȝƲτӑςœȇʤҫɌ\xa0y<Ȣĕ[ҸҮΔõ¨',
                                                    },
                                    },
                            {
                                        'name': 'ѢȽ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǓʯơRһДΐϺþͷơϻʶӧΞИưůЯĈʯ҄Lǌ\x94ó\u038bѯ&Ù',
                                                    },
                                    },
                            {
                                        'name': '&!ȠĜʼҺяʘƐǲѡʖяōΏTҜ#ѤʩʰϮÇ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3225375273965015042,
                                                                            -969347209503889609,
                                                                            -4660642276781422006,
                                                                            -4728787338331548866,
                                                                            1293993451807338563,
                                                                            -2718778190497938804,
                                                                            7173646395401609289,
                                                                            8407224082450489826,
                                                                            8924135676096451296,
                                                                            -7761234483603975239,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'щӧʞĤȬĔҸҺΣҾԞюȭвƋɀќҒΦчаŁϗӔɵ¤ʄȂѻŋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.408556:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ˁӜҋȰʟӭϾҹҽďǭΝȚºǳɒŕΞʍӁԘǡɛЮê[Ɏǋǎɢ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            369067.23925367976,
                                                                            97577.12062156797,
                                                                            796159.310316633,
                                                                            621219.8893109318,
                                                                            458155.56862694887,
                                                                            328233.3811683649,
                                                                            734915.1775324568,
                                                                            820727.9967162809,
                                                                            260445.75945362076,
                                                                            774464.8992783132,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƴѪÜˀЏ\x84өH˥ŅӳЙ{ïԠˏϽ{ʊǱӕҗƫɴ»ԙӪѝʡω',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5954539206024795491,
                                                                            -2768604341445691230,
                                                                            -7553224188265635571,
                                                                            9059789832527051934,
                                                                            -6988180617545616078,
                                                                            -7467466205160501328,
                                                                            1347528241934426157,
                                                                            3814762590609570007,
                                                                            8227689306396547166,
                                                                            -1896243009826169164,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'кԝȢ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ēʴÉЯΕɎʇ\x89ӵЅŉԌȘԨơǧԏ҆ŭʘʄǆʈҡļЪюŏɾІ',
                                                    },
                                    },
                            {
                                        'name': 'ʽ˶ӂѣşȑОθæ\x89дβ˵ƇɦȳʰҰԔzѱƟЖ·',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.411801:+0000',
                                                                            '20220523:220031.411884:+0000',
                                                                            '20220523:220031.411965:+0000',
                                                                            '20220523:220031.412045:+0000',
                                                                            '20220523:220031.412124:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˹ѭӒƪɛˍŊƣŰėʹƏҷCÏÑŤԮ¢ˏØȈ¹ҝˆűȮȪӐ˩',
                    'message': 'ȗPԠǯЬǿ4ÜӖѦˑϟˈɺʾԠɮӮƞ˦ǐɸĀƛǇĖȃÆėС',
                    'arguments': [
                            {
                                        'name': 'Ɗʣ`ǩˏȡȔÚҧȿĔĞҗʽŻɯ%ǮҼȻϒɾѸʭŲTɻ²˞ǟ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.413236:+0000',
                                                                            '20220523:220031.413319:+0000',
                                                                            '20220523:220031.413400:+0000',
                                                                            '20220523:220031.413479:+0000',
                                                                            '20220523:220031.413559:+0000',
                                                                            '20220523:220031.413637:+0000',
                                                                            '20220523:220031.413716:+0000',
                                                                            '20220523:220031.413795:+0000',
                                                                            '20220523:220031.413874:+0000',
                                                                            '20220523:220031.413953:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'cǹȆҿķ\x9cɆˡĔ)ǰθcрċȲԖ˭ƏĐɲʟʛ9',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ԜǴӫϙһЏӐΒ˷иŒзn',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˎáȐƎȘ]ӹɒȰ8ю`ÓȕǄԋʷϗ\x9fȿІЏҜџѮÿ1Ѷƻ ',
                                                    },
                                    },
                            {
                                        'name': 'ɓčϜǇ£˘Г˥ġ½ɂNөXŌǑЪТқҭɀPƴ9PɾƧĿѬς',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 306315.31235266704,
                                                    },
                                    },
                            {
                                        'name': 'ʅŗĶɊĿȉ¤æϥGȏ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ϸǩҥƽƣ\x9b΄żӧŃ\x95ɡТȰҷ΄ˠήŝʌťɤӮnÌ˾ΣƮȴЩ',
                                                                            'ǔʿùҊɿӍϾŝɷϜԠ¸ӖfȕΗŦ0Ԉ\x85ĈȞĳäӴɃЅɰЗŪ',
                                                                            '˩ӆ˻ӚƲí\u03812қѬpìʥҨëҒYȅ0˛ǖКùѪ˚эĹѣɰέ',
                                                                            'ȚĳϽӹԐ\u0380öҝóȃ\u038dĽ°Ĝŵş˱ɐӶmĆсƚѾɦЭÞƢGԞ',
                                                                            'Ӄȶ¤£¨ʲҐқɠʡπЩгn\x87ȉ˺\xadόʑȄύӞĸψȮʙρ¦ӧ',
                                                                            'ìlğɮǷƧҷǅŕςлǄÜƧĦĺʐʆЗäťϞЏŨӞȝˇàӟ˭',
                                                                            'ĬͽΑǇˇӥǁӈǿ\x9aŅЁǼƁþӨѬҋlʉPƁҾʴѣЄӪȍň˸',
                                                                            '˟\x9cѐĪҽеĠΛĚɖʄƫØʩŴµѢ˫ő-ƕɇ9ǭĹ\x9aΟЎϖġ',
                                                                            'ʠϔă˽žӓ^Ԧ\x89\x9cӊǉМLɢϜɿϟʳ\x8eűѼϜʴŔƇȣғΥϺ',
                                                                            'ϐПˏȱЊȂǟʦɛ˄×үŖƠYюǽ˽|ҍˁьʥSΏÄʝĐƽą',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƨɜӯΒĒӁѣŕȒȕɲɯɷƺ´ĜlƱmgǶ\x8aЊ\x85ʦӴȓϢԒԛ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǢȯmɋӝĄǕʬ½ĶċƕһѿɕǋȚѲźñӽGѰЊ˷*ȑˎ¥ŀ',
                                                                            'ͺƹӎƹɁɍρ¥ΪξǷƺåӓæőюЛKɘƋЄξFśȇȂӑьȾ',
                                                                            'ӱӣѹăøʃ\x89ŉӀĬ\x8fϒƾ\x8dȩӗťɓīƩǁέԄˡœҰ˃ìðа',
                                                                            'ΎÙϖʠҊZҰ\x93dƚɠȌʸŗƙȓЛDɩʿϔУψȮĥԦӆHʰϣ',
                                                                            'ǅӝ\x95ΐҮȪƪÿӅѝ6şʦƇԥˑҘϪҐ\x94ǂËǝĔǠϑώĀӝϪ',
                                                                            'РŊʶвǒͳψŒ¡ғŃҙˏéѭʪΆь[ąêǉӹόΆďǒОҫ\x7f',
                                                                            '˖þŽҴɭҢ,к˦ˬʍģ<ψˠʄõŵϯÙнƴ˻ҾӧɾϥЭӋe',
                                                                            '>ǜѫǦˢϳõѪ!εš ŇͼɔZwūξ҈nВɺ\x88Ϣˬ\u038d˨ǒѪ',
                                                                            'ƕЩϭӭɲбВƨcҍ·ǪıЕɟԥϐʅšɮˀϚĀιȇ\x90ˏӦ¹в',
                                                                            'ŀѴæə)˽Ėӄƣ҈ȎӍʪϷʌҹÉʁ˴ćѠ´ӑѾЏԭ¥ͱ˧ŉ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɒʡчɎɚӉАџlǔтşˎɏ҈',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŘɵӳˬȥɆ¡ʔϨȊ҂(Ηϯɢ\x92ԡӫғď˳ӁBГь҉ÅӖţɋ',
                                                                            '˳ϗӰƂųƸư`ƚơơӚȭȰßă˞ǭɪȎӅӌѰԠˑĨŒрɏɂ',
                                                                            'аΝԎĪқϥкԅΓ˒¼ǮЉƅȿ\x83ʆҖϨrЁɠϳ·ѵӕȓқ²˰',
                                                                            'Ǭʾȟȇ;ӽ\x81˝ǆͳѶɌĘŐѧoϳѧĀőӵϛ(ǩѹʵ`Åǵϵ',
                                                                            '\x80ʑБϷєô˺ǭЦͻъWʛԍєɭѥό?ǻȁĥϻҿ\xa0Ĭʅβÿ&',
                                                                            'eњҰϻӂӸΆȄǐԥtǇѦСħȵŀǹϪԁˀлңΕɡŭɳʁUë',
                                                                            'ǲʯĘˋ˥лϕ3ӮŨ$ŇςӍ*»ȩēǦǻčƯƶǖɥĒϵөпǬ',
                                                                            'ȣˇ¾ȚÕąāsƤӁӸDҊ˰ʒȝÙhŎȊ³\x9dʡ˙ћʫ÷ȨӹΚ',
                                                                            'ԭҁ\u038dɲâĠѹʩʴțҰЗćԖϔªˮα˓ϺΒ˷˟ĤίЇϲċˑҰ',
                                                                            'ıԓѓĐͱωɡӔƾўØĴεŵԤчŇ¦ЇŊĒǘɓɘ§ԎӍƢԒь',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¿Ȝ!ԆƀεƪҮЃΈÅþӮƬ˵°ԕǌĩȃdõəŒӅӼρҺhǒ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'әŰ³Ϯj҃ҁƘPíǏЊĂȎƂįήƿѶ˳ǣҵǴΨˍϏӇƏľƛ',
                                                    },
                                    },
                            {
                                        'name': 'țȜWðȎǾϔƦӨłϤƶӿȁĨƶɱɍvҽĵθΎP\x8fӛğƑѽ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -75950.81274087372,
                                                                            150140.83702332358,
                                                                            444413.8102680757,
                                                                            780968.5029982285,
                                                                            635518.663655338,
                                                                            49002.48575385063,
                                                                            -72493.96206466023,
                                                                            -89837.93698933383,
                                                                            294341.8368673552,
                                                                            478055.8195946311,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¦nǙӳʸ#9£śī˔ƘǏȬRъĦȋĤΔưʳвƴт&ʚϐԇύ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2236353223424278179,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȷL\u03a2ϴtЌ˻¨˯şŇƁυҝ˞ѡ!\x87ė\u03a2вцʪȭÐǱӋòɇ½',
                    'message': 'ςыǻ\x99zƈӕY!ЉȃİÝІȁÁĝаʉvψѿ\x86SäňʨΈrӵ',
                    'arguments': [
                            {
                                        'name': 'Фûʄβ@5\x8cɖʖɌZwԐŻΝ˗Ҵɞх,¬',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɾԡɛ˭ԓ΅,PȂ\x9dԕѯō˵ǈ²ϓJҴϽ˔ͻӯ7ρZѤ]ͻď',
                                                    },
                                    },
                            {
                                        'name': 'ҭ ϩƶɝΊÕzīΥʈʹԃͰӖķǼɪØρԫȜơҟУäĨӿ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.423075:+0000',
                                                                            '20220523:220031.423158:+0000',
                                                                            '20220523:220031.423239:+0000',
                                                                            '20220523:220031.423319:+0000',
                                                                            '20220523:220031.423398:+0000',
                                                                            '20220523:220031.423476:+0000',
                                                                            '20220523:220031.423555:+0000',
                                                                            '20220523:220031.423633:+0000',
                                                                            '20220523:220031.423712:+0000',
                                                                            '20220523:220031.423791:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԐԔʅΧǱҟ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.424375:+0000',
                                                                            '20220523:220031.424458:+0000',
                                                                            '20220523:220031.424538:+0000',
                                                                            '20220523:220031.424616:+0000',
                                                                            '20220523:220031.424715:+0000',
                                                                            '20220523:220031.424796:+0000',
                                                                            '20220523:220031.424875:+0000',
                                                                            '20220523:220031.424954:+0000',
                                                                            '20220523:220031.425033:+0000',
                                                                            '20220523:220031.425111:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǌΝ>ϏǥǡƍҥǍΌȯАиһħlҭ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '9Ϲ\x87϶ĂƍŮŇ0Žіə³ԋĥ˜ӫѶӺѝrʉ±σΓȗΥԡъŕ',
                                                    },
                                    },
                            {
                                        'name': 'Ćбф˞ҟʯӽ÷ɟԉѫˁƂƴГϯӋƹʀ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 624904.913249445,
                                                    },
                                    },
                            {
                                        'name': 'RöĭǎÒѽȆ҅ō˔ˬÎûȦ\x8e',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 628482.3241227597,
                                                    },
                                    },
                            {
                                        'name': 'χрΌĭĸ\u038dԥŃУӛ\x82˧Ǚɧӿć',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'DŮәƠDĭʀǨ˴ӈxұŅӨԮтжψϱԌҹӊӥќəʺĩǟ÷Ƨ',
                                                    },
                                    },
                            {
                                        'name': 'ϓѦɢʆȋфɄâͳҜҰѯńоϓӰ\x92ѨʍѬНùίϧØŁŤȳòʯ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 859735.0681879212,
                                                    },
                                    },
                            {
                                        'name': 'ĺȱǩϗG\u0381ԛҶȸιęлʅυρȔȨ§˓ɎƑԎăή',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '˷ϬǍМƑ\x89˰Σ¢',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            798049.9015016069,
                                                                            879452.037833849,
                                                                            257949.30786098324,
                                                                            864152.6989218928,
                                                                            981324.545157552,
                                                                            -82299.62814686356,
                                                                            466833.94072569837,
                                                                            283290.4508290976,
                                                                            116582.31851688336,
                                                                            647324.8783668331,
                                                                        ],
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

            'identifier': '¢ӠvȳҨ',

            'categories': [
                'configuration',
            ],

            'messages': [
                {
                    'catalog': 'Бж',
                    'message': 'Ñ',
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
            'name': 'TōΨɯâɅÐ˗ŊȨҩӋ΄Ȯ˔қʸċǽ%ӪTϾɫŐӦÇҍєӗ',
            'error': {
                'identifier': 'YʻѝKɣӮҰѐǃŽĞϹǘÜХӇȪԝɘΨ\u038dƱʆʢfʒÊģȣӅ',
                'categories': [
                    'os',
                    'access-restriction',
                    'access-restriction',
                    'file',
                    'configuration',
                    'network',
                    'network',
                    'file',
                    'internal',
                    'invalid-user-action',
                ],
                'source': 'ϏĞʴѧ\u038dϟ\x91ҹAπфԈϔÊOėтґǻЀÿŏΙŵԫћѝŬԂМ',
                'messages': [
                    {
                            'catalog': 'Ҋ˄ѴÒǝΐĦƐѢ˕ӓˍ˔',
                            'message': 'ҔXȩψÕϫȮĞЇĢ|ЬŢ;ΙӁҤκѶ˛ɦÂ|Ҙίҡҧϸͷʸ',
                            'arguments': [
                                        {
                                                        'name': 'ΩҮе)ѾX',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 458129.50934436475,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʼ˺ƏǷʷț',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 261958.49987119058,
                                                                        },
                                                    },
                                        {
                                                        'name': '\xad҃ÑɯѺҚɰɵϫıԒэûіЙˇβ£ďЅ\x85˘',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6126629338281559051,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΝԜ˰ѶұʆΘӃˁАӏǧ҉ҽÙmcӰēӉ^ȪĊġˊπԂ·ҫƹ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϼÁѹԛόšĉǒʗԣDüƋԇäЛѐϬ\x8eɧÈОӂζȦɴѽĪԕћ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĸ˧ʽҫĪťȓ·ЩѰɕйɡȫԆîžʡӪҬϢèġµӎºԂлʥҒ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'дԞfщϊʀaƶˬɪĜЊ\x94àñȐˎϹҚӸДϰǢюɾəԭ҅Ӛ҈',
                                                                        },
                                                    },
                                        {
                                                        'name': 'đҴћˮѰүʫɊɭnʻ\x83ȨӻѮn>Ϊ³ϴɔďʷфɰÈ΅ЀΆǡ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.323973:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѡɻǸУȈϹö',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȎϭɒɽԞԬõť͵ІÎҐˮҚҤґĚ\x8bƻȬ˵\x80ǉŸɳаҤ°ɱδ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'гҠυǶЧŭЧԦFɆŸʒэӀɌɂϮ\x8eοǌԟƪƐÉүeԠĘƉȋ',
                                                                        },
                                                    },
                                        {
                                                        'name': '$ɽĝLЦŌà\u038dѪ2ȭõʮϯ˖VȦӭϬʥȶҘџÝϔҋ˄ˢψԉ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ύˑɡԀ˱ϛŗƤƵǻdҿ·ϦŒñЦ˗VѬˏӸȯԥŭ\x8e˛òȍȆ',
                            'message': 'ϤиђkИ?ɨƁ˄³ƋʩюƥјЛжËʊ\x95΅IȤâŨ·ΖP×ɉ',
                            'arguments': [
                                        {
                                                        'name': 'ŅʰӼÑѱЫĬ/ϦȽɵ$qƾΑЖҶɤ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѰǷѫӲНϊсăЅłī.ǂʹ%ǎƧώʨ;ƯԇɬԚ˒ȀӼѻˀõ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6861460832481739324,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʑȪŒƧҁǟ!}ƾʀ\x96\u0378ÌϯŁʚV\x91\x9dɊҟʉ\u0378Ѳ\xa0ЕеңӢÀ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '¸Àӧ¹ʽЖcԕśщgѷԢОƺҢɭȕԤǠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.327517:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԇː',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '´7ѡϽȦιβҶ˥§ĶɯűҹҲҳƙɳňŮαɗƹÝŻūӹ¡Λ˔',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʛȵȴǾːķʫˁǌӏȦπԩɞÉŎȆӎϿүϭWίÇѳΛӋ˱\x95Q',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'TϚǡÎѩŵәȦ˸ϑ҆рІӧʊʗ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¡ɝҦðǟ·ʮӶΗƣǅβϺɴȀċƀΪſĳ\x8b\u0381ѥУăɺʭҵ0ʨ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Rӳ\x89ȔϿ`үǏϚĩʹρ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɍîҐɤч\x94ъɉ҇ɱǕҎѮΐuǠԚнɵщĿǩӘȽӓѻϺ@҃ʴ',
                            'message': 'ɟϢ·ȮҘҕɚŦ˫Ʒ҉ǆҗBɼВҋ¤¡ӬƲϿŕĐϙ}¤ÊЙ2',
                            'arguments': [
                                        {
                                                        'name': '\x97½ӖϔtϨѲсЀҧvЂȉёɻҀŨ˖Ѷê\x93˙',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7644748759559239248,
                                                                        },
                                                    },
                                        {
                                                        'name': 'WԘʓҕАӿ˘ɰ˙ё×ƁПϦʖЮʲʆǻчςΰČÈă\x86Ð§ťϑ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 161630.70861725346,
                                                                        },
                                                    },
                                        {
                                                        'name': 'юΡǁάğѪϕɸIͱ\u03a2³ʺǙĢϓӵBўɴȊΦΉ\x9fˌħͺӻŜŋ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '{ʊѣȸΘƕǹĈʦϢ\u0381®ëɋӑ˰ːϨҬȯǞ1ΒӸɑяһKӞȖ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'őӀRͲǂǏғЉ˙ӃŤƗŐ\x9dŉӭҜүáξƩԭɴÚųϙǥˁǒȚ',
                                                                        },
                                                    },
                                        {
                                                        'name': '$\x9eҚ˔Þ\x8bҡфƇÏˇèƉ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'НĻȎЕȅƏήpIƷԊЊұ˅\x84ű˓lЃ˸ȤďàѾȒΛ˥ɞǷȖ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Љ¾Έѹƛ҇jɨē',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˮѷΈ¿ҀǜƹƺѽӞ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ưӐќ˞\x83όîϬ¯Μ˼ǽDŹķѰýƅàƽԏώɟΤ˩ĩ\xa0÷Ɨ҆',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1194252323913076601,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ιʎƈѼϔßΜԇєĳӤŌԃÅǉĒH˅ɗáăϚ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'oЩĸΊÝ\x85+ǷδǊyΖϢuřǳяɄҔϙϗУӘeΉĞ҇\x83Ǚú',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˕ĄΤùʡɑϴяʿҵŨʧβҨĬԪ\x86ԄƔ4ƽƱɰ¥ҔǋϔȠӴϰ',
                            'message': 'ǧҪȀȄžϔǺԍ¿˒ăΈʔʢŻͿȪ·īϰ˒\x98ǐǹ˲ϾԤԩËӒ',
                            'arguments': [
                                        {
                                                        'name': 'ǊʭûŮƮЙȍŤ˖Δ¢İΎҎҌώҐǵĮГØҐѫҫͼЈїΧԢȭ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɴ\x97ЌһȧăʧɺґӺĖοӮ£ø[Ҟϣ´Ǥ&ƽȨǤɕ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĂҩʹЇԉƗϯǙξɌNϪԭłʌĞz\x89ĳËɬ\x8aVŚ˭Űʋʵˆԍ',
                                                                        },
                                                    },
                                        {
                                                        'name': '6ԀҐƗԇíӡӪӍ˙Pŕ\x86Θԁˊώýĵ˰ҷēΊѣԞ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǓίтӶ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѡͰӂŅƜГͻ\x81ƳȮȃ¨,Ʋτ\x8bϛΓʼƐɳ˾ǓԇƎ\u038bΊϤЯ!',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϯӴҼÿφԃĤ´:ʼʐѧɮʛӉόѧΒȳѐѷӪtзȉåɲː˽ΐ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ʀяȭ«ĎʗнǫϰĜҺ\x80ҫ.ԒŹǳ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.337710:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɒʽԈАɂǙƁӠѓЬӁНп\x84Ć|ÿҡǡʹ_ˇҲŀѝ\x8eʭͶ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԋӉƓШ\x91ɆăʚāƓřǢ¯ԠƮͱьúӅɸ҅β4ѽ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϊЭҢ¾żɄǑӚȭԊЩ\x86ȪʜĜɡÞӡé7`\x8e´ҴϻђӒǵƿ˦',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҆Һ§àɘүӹņ',
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

            'name': 'ʂйé',

            'error': {
                'identifier': 'ҳĊ¾ˈӁ',
                'categories': [
                    'file',
                ],
                'messages': [
                    {
                            'catalog': 'Ūņ',
                            'message': 'ԩ',
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
            'event_id': 'ЯԎϘζιϑ˻ǁǿ\x94ŝ˳Ρʅĵѹ˯ǓÛɢɜʔŋĚ[Ό/\x940р',
            'target_id': 'ϑƈʗ˹҄˪˸ÝŨưĉʂ\x83Ϩ~ӓϺP·ϷӺʸ˲ʹƢԐҪΕɣÈ',
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
                    'event_id': 'ЃόǔыÅȓĥ«ԂǛŉԛĕʀ}Ś«"ǝѥԫάçʤХϏª\x83ʶɱ',
                    'target_id': 'ūсЖΔǽԦũѥ\x90ΏĬWμ˕ȼÅŬ©өƼќɎʒ˱ɡØʙ\x9c\xa0ą',
                },
                {
                    'event_id': "ŷÛҊҡƉ&\u0378ǅήǕĞō©ȉϰϟ'ϯʉҭ\x93ϡūĮ\x86ŗжOǟҚ",
                    'target_id': 'Ԥ¿ʚǞģȿί)ʟЪσˬ˦ҔrĖÃGȁĭųƍ\x9eρёċдřҁһ',
                },
                {
                    'event_id': 'ĭÄԠʺњɤŅѐÓųĩϻƀӮɚѝӵˬУρҥǞθġǛҦêɗ¬ӓ',
                    'target_id': 'AЗƛÏђŏӬȉBϝɘ˖ō\x90ҐғԨŰɴ$˶ʉˑͰΧ\x95ĽȍԤJ',
                },
                {
                    'event_id': 'øБԛԀµɹċɉȝҕʔшѠԓ҉п3ѮԦʗǭΈãўsƞmʝmÃ',
                    'target_id': 'ǲίѫϏӪӋϯ҄ǒšŷΙͻӽ҈˰ǳԈϏŢæ\u038dɹǐĹϙŢʳДý',
                },
                {
                    'event_id': 'Ќɾϫҷ4ԍ϶ҶΞ˒ҪЇδΚƕԚǷʭΔŏƺӐɫ\u0378Ɨ\x8bкƋïӍ',
                    'target_id': 'ɵӅҠǿóȣͱTʩǯɋƍҲӔѶƮɉȨĎӗȊϞδǣМłԖҳˎɣ',
                },
                {
                    'event_id': 'ǵʌԘUʂӢF{\x8bǯ˾ŲÇÅĀ\u0382-ӋƄӐŌϕϳλpє\x9cͰ¥Ⱥ',
                    'target_id': 'əƿȐ\x9b(àŘх˃\x8dɃÌҤǸŋSюɌҕҪĝϳΝЁ˻ĂȣȌǔј',
                },
                {
                    'event_id': 'ԏǈɣϝҺ˱ҌeЃԖņыνʠǤзÖɨΛΚʮˋŻİ˒ɜņǘŒÇ',
                    'target_id': '¢ȅǖɆϽƝʱƕѼёнɑƧήӶAŜɦӊԗõϮüЕĸņŃƶΡˎ',
                },
                {
                    'event_id': 'ҋąӍɺpѡǡЬ\x85Ҷþ¶\x8cǄɨβĭ˶ʊŸǛľї,fϟnҍAʿ',
                    'target_id': 'ȨͶƚǧȡАƚʫǇˤеoǩʽξȤʀʓƘʴɂ˜уr\u0381ȒĻǃǧϺ',
                },
                {
                    'event_id': 'ʏĢșŽӤѥɫήȠ[ѐΛʡosӌùʌҿңӔúʡˤύʈ¡ŃѭӾ',
                    'target_id': 'Mɔ\x8cͶžƵòϚÚƆŹēЏ¿ȮȘǮҴϼԨˮƖǘŬõ҃˛Ċ\x9bĔ',
                },
                {
                    'event_id': 'kǐȍϳŖʱ´§΄ȏtŸɘѡ˙ǒȔЌþ\x8d\u0383jÕǉƙЩʻĲ\x8cĄ',
                    'target_id': 'β˓ӸĊԀėҙϫhéŜҏŹέɎȞѨ\u0378QȰƲήǫǵɨȓϑ\x94ͳ,',
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
                    'event_id': 'Ǔȟɷjüȴ΅ʾƔ4ȈɠΗа\x88ȫƐӮҁűɶӣқÇźИɕΓä\xad',
                    'target_id': 'ǝʓ˸¦ϕ˨ǘɂ¤Ӯ|˷ĠҬ\x8eӼ¼^ҢʌȌӒȟΠχvζƤͽȈ',
                },
                {
                    'event_id': 'Ԝԍ·ʥΜčǙ(оԇгÜȊϱǎ\x87˼ӕϴǶ<ęνÛчзҩȒώŔ',
                    'target_id': 'ĕʑѭϓѓĵʰĽĐƥ£ŋʊҋά\u0379ҟΝ²Ɨƭ\x8eѡҷҢϡӉΒ\u038bϹ',
                },
                {
                    'event_id': 'ʤϣȡˢKʈӌѠǪȟɬǟҚʱ~ŊʹǧǛӓϳĕčҷľ˖˝ȱƀʍ',
                    'target_id': 'ҩ˃\x8aȶδґɎ¤ЅŊєϨŧΚ×\u038bmβЕЦξʱ\x7fćСſΜƵЩȑ',
                },
                {
                    'event_id': 'YκхϢÊԗ˹zcȟϓЁγ\x91ТЉǌ\x85@)ӂНŜԐʣŭǲĢфɋ',
                    'target_id': 'ǂѠыԜέԑƑǹӞȡɸĝͶJǷŪ´ʹ\x87ǖҮҍǆʃàʌʬȧȥB',
                },
                {
                    'event_id': '?Ā˹êoĵȅӥ\x80ǖ\x98ΉΕžԧ\u0383ˑȕįȭ\x85ГЊʳɣӀʕȖò$',
                    'target_id': '®wāɏђν\x96\u0378¤ȶ˜Ǩʄ¢ɳĆġcŽÍÛǘ˚ɂşʜȳΤҒƔ',
                },
                {
                    'event_id': 'ʔΑƚ[чӔˡϛ\x88ĄωΨļԞƧӇԣԝÙǙĄǘƖђǨӁѻѕΑi',
                    'target_id': 'ĒωȦÚɖƄǜdóӃśȾ©^öȷŝ΄νŋϪȸʽӜѝΆ˻ЀɇŅ',
                },
                {
                    'event_id': 'ӵϴUΎӃ˝ҮɯÜѠ»{Ǚ˽ýæʯΜƳǖÚҦэöǕɚ\x88ǍӞϬ',
                    'target_id': 'ӗʹͲȕɋūҠξv8ԚДnȭшҘ-ƬϾ˸Č7ҍМʃȩ2˹ɋӻ',
                },
                {
                    'event_id': 'Þē˨ćȾȂӶΆʎïǘɞŸ˸3\x98Cѧϖ³iǧΆƆŸʀѤɷӵǪ',
                    'target_id': 'ȱЫɖӂԡӥ˺ҳȮ0ГϸʔˠԤ˲ȦMʭϲҨȦvƈԂļԌҡkɁ',
                },
                {
                    'event_id': 'ҎҦȥӘϓčЮΧƌхǱϝþoϋȜμɹϨǋҬƲ±РԜÎЗ\x9fАӦ',
                    'target_id': 'ȤӥƛѪʚϻ\x7fĬǻΠκь\x81Ǐ\x84Ƭ҆щLπ˽ˎDƨҾӂɞyˣϲ',
                },
                {
                    'event_id': 'Ϟȩϊ?rӅĩ˺ϘţҤӨÕѭΓĻϺӪǛȈǦ˲βһѷԖ¦ҿȷϕ',
                    'target_id': 'ĬΤжɇ»Ģãƕ˯ȽʭʁƠКӊӮРʪĉ\x9bϯȓьӍɯяѱ\x83Фә',
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
