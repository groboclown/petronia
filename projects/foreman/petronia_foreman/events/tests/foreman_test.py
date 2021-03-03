# GENERATED CODE - DO NOT MODIFY
# Created on 2021-03-02T16:51:56.015807+00:00

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
                'ˉȡ"ɕǍѱ\x8aёρӑ$ϸƾЭȂőŔˋƗŐ\x99˓ϦǒǭƇ´ξóį',
                'ǧĔΊкϹɡʱȨҔϒΚʅˡЂ˸ƐĊ˲ϸƊӀүˍˢɭ\x84ǗˢąО',
                'ÐWƽ˘ωCԩЭɽѨΌΒŋѭÿɕΔӼˑZͳȴϔͱπʲАСÚD',
                'ς\x9bԥŹhȩȷľ\x83iƱӋʝ˴ĝĬξŠϸžӛǆɴǣԋҾЄ¢ȘÍ',
                'NãǲɟәˎϤɉж¸vӣԤ0+ɲӫǹī˖Ύ¼Ӄďl?˱κѮΐ',
                'έˌ& ¥˾ɝǧӍӚϑӟRhΆ\x9eǓǠ}ӆəΤӭ·ƻ˸ȧaȦĘ',
                'ΊϳƆΓ2ΕÒÍӧĞϺǺ(ɹљϜҖГԬӟɂɨΗȟjΚƃćˏȆ',
                'đƐԪƅŚȓǎĒǜ¼ӻņήĎξȀГҲѝѴӌǏԒǇȉϵԠǦďƎ',
                'ΖѿİԉÌ\x91Ґǽɀӫ;ːjСńΝҬвʸĐѡΎѨŔð\x85ìτ\x8aƎ',
                '#ѱʯ=ȀаˊȦΏmǣҬ˰ӁμʠȟѾΊҢn\x90ˡ\x8aвˠǷЇŶѐ',
            ],
            'source_id_prefixes': [
                'ԜʟǊ҉@Ƀҝΐʌ˼RͷѸɣ˕Ѓǋɬ\x97ǣȹȓкùσȅǀǌƃȆ',
                'ӣ\x80ǄѦƀτϘϸɩ/ɸũǊɹΑҗłˢƃҔĦУͽūϐ]ԑŴƤѵ',
                'ҋĸƶΝōϘѝ\u0380ĩʤЅϣȩ»ȡɮкüɤԗǹЋ˨\x97ϵїǉ\x9aıǠ',
                'ɍΞʮԍшѦ°ŸѥĲɫȂ3үţƴǝˏЎÃ@ӎƋЁ«ƔŖɞȪю',
                'Àǎ˚Іϓ˵ŐXƇӵƦMѣȡʘǮ\x92ϕɁˋɓåҾӹȑԖʔφÞƖ',
                'åđăˠ\u0383ӻěȶѯŬЄǖϰĪĀӤЧ[\xa0ɸɹòЉȢўһŀgϛƃ',
                "ѾԛɶʊȰј-ˠͲƿПƴ'ϼģƚɂаΥ·ĈĵФӽΑӜ]ҸĎŶ",
                'ũǔѦӞòçƻʓß·Ħ\u038bŃХ˱ˣəǍѴǺƻ¯\x83ɦ\u0380иƹΜȀƤ',
                "ԀȜ˓Ԡî'˄іϯ˅_Ȃѯ¨ʭԋɿш¶?ʙѦԢƦζˡЂѻƐĪ",
                'ӀüϧüӮʋͲӦԆ,ïĆѰˬH\u0382ǁ˖ҧΝ\x97åďŅΫϕÅϿȋϗ',
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
            'action': 'ѠϪǬˇÁνςaħǇȥѐǍюĆӸÜТϣȟļѓƑ\x9dѩɬŨȴӦ˭',
            'resources': [
                'ǷĜȏǬ˩ȎƾфѤӏƔǜ#§ϳŃɔƉˍȚһĝˋжƼґĵϴ1ŗ',
                '\x88ϐëûНǲԔǆѥçƳҷͱұɾƲÕƃѤƔȂϺŰӈϟǇĆʪNӹ',
                'ΣͻǗŗùІyΰűӄƫҡĭσċȺǜǩĘ\x81ǇɆгϦȖž|ɹФȔ',
                'ǛƙďҬģʂőʻҾϳŧԜ_ѶͷÿӨΔϝЕȌŬiЎЎgØӫºД',
                'ʉӵѲʑǍήɦФӆȁȆėÇ˩ƀǸ½\u0379ˏ\x8bͰ϶ʤѳĭӤȶŲ˔Ҡ',
                'κūɢпƂ˘ҲƼ\u03a2ЭɕȠɒϭGǠͺâΧ˂ЏɇѠȭЪ˳ɤԭҔѥ',
                'ӪΛϳϚϖÆĿͱśðζʚͰÓŜѲɐ¯Й˱˚ƞώ9ŻȶǈЮ˽Ƌ',
                'ʠͻЮŷɚřАLҙÒ˞#ӁκÿʺєӿѴǭʪƂɽǎϛӽЪϋǊɿ',
                '´ȯěŦӴđЅɳɿ˚ǍԐϨʕϣÆ˰ϧČ϶ҳȓãźĆsȳĊϗƪ',
                'ɦҊŦηѕЕȂȦƧͳ_\x95ɻşd?ŢӵǴĿԌʛųˍɓͱƷöɼǛ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'ɽ',

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
            'name': 'ēȠԔȢыsŅ˙ʘˣ?ȢǅӍ·Ȯā˞ԔT҆ԤȞϠҖϦш\u0379',
            'version': [
                -4204632523913202651,
                -5651868496745429772,
                -6781110508827095192,
            ],
            'location': [
                'ǦЬǕ˜!ǌMÌԒʩȪҶŜӫԡǡԩ6ÖҸǇĄĄȅ҂ѧºѿŒś',
                'ѥǫѯ͵ɘƄǼȎѶҳΠǇћɍǉÒ˺ÞԫȎ«ƑŃюԜȜѰΤëҺ',
                'NӻϘıìʽŌиΗǾȷҏϾӃԦԂƀѣøќ˓ŝˠаťҕǭђ\\Ɠ',
                '³ůÇЖǲЁʔϟɆҢӍ\x93Ɛͱȥһ˜\x98ӞǗȍΞƴӼOƧʶѹǃ\xad',
                ':ӈ(ЩЈѬӪɹчɟԣ\u0378\xadεˀŶȎĊŧƩ\x9a]ɞŜӁŎӶʰΎȌ',
                'ʤřWǛЦɒʚɖ-ʀɭţĮ΅ÁçҒцˢɁɸі\x96Қ{ɒҖԮ\x89Ŧ',
                'àėˊȑƥ*ĜȂËÅýЁҶ˵ƣҼΜȒƎҝ\x8bÃӢɆƫɚ~Ȉѓ\x87',
                'ҳŻ&&ҮϲӞúѡűȺӪŨȳˑҔ0ўmʸ҂˃ҟԐʇҔÔ˳ѯþ',
                'ƴёżmȢϐʓ-\x8aƂʳŝÝΰűȏЕ±q^ÕιάƠǩˁȎeǣù',
                'ʼϠҒÕа¤ʞȉÛηǥIƓ¸PđƸхǚѮю}ƓęȦҳăқНǏ',
            ],
            'runtime': "ˁЫpұ#'ѵŅгiҴˏĲ.XθÊԅ0ğ=ѱ\x9fƒǍʀȏӯʈİ",
            'send_access': {
                'event_ids': [
                    'ыϚɓRɈȻβʏЅ˚˄ȆȰØΗÛɵLƹϤϽʫX¸ǁōι\x8b²ѕ',
                    'ԮҫѿԧЍʆӂcԔӽȽҋϣƥѸʰњΉҲ\x9dȾӵΎҗǲĉÃțûΩ',
                    'ǬɼʪǽŧĘЫ8ԟԐйҔåơІſǊɘтǁ¤ς\u0380b\x8eЊԓŢȖʤ',
                    'Ωʖœο\x80ˈÀȯ±ɋѓ#ǟ£дƄʮϳΟɑǆӑÊϱѸɼʛύĭɋ',
                    'ҿȑVԏŜςϭĐƊМˡǨùġԡ¯ǡͻμήċСāЏɃŨƇ¦Ώɮ',
                    'ѵϣɆMςйŔ\x9d\x9bʅõ\x8dӁɣÚǒŲŽƒzʷǉ7ŔԁưѶèБǣ',
                    'ˡΕӹƣĀΙѫΧӿêԗÃ˻ĈŪǆͿˆŇ˟ԙ\x833қ˭¨³Ȩβh',
                    'Ņʋàѳˣ˛¤kƍӟƗΛҼõ˔ʱɋϓѦ¹\xadюЦЫӍѯHІƯȯ',
                    'ʓ\x86Ȥɪκ\u0382ƱȞÍĢɔˉϽ5Ɗʄȿ˒ǄѐÅŗpǵ˸ǰ4èϟ\x92',
                    'ҎſίʪȀңąϏ+%ҰѵǢǸͽΙǄżҤQΞӟǮ҃ɭěǾĿÆ\x81',
                ],
                'source_id_prefixes': [
                    'ǩнʻӛԐȮϾΑrԗҎȐѱýǢʁ˓ĩʈˊũȋςΘǭœåһɁ\x87',
                    'ȏf˻ƋĿǆеЌҴĘȜĬɑʫ´ˡkǦˌȓÙŗϙǊҪԬǗăşɼ',
                    'Ãɣàν-ʭу҅ДƌђϪȎӴɏʏÜ4ϘâëøϪ)\xa0ûѦΆǌƍ',
                    'õȘ®ҖλƿƜsõą˅\x91Κ\x9eaÓɻǵаǺʥʲŪˌɨΑԈśƒҶ',
                    'ƜłŮÿφηȀɕŕӥłлȎǓ3ϷҧÎǐњԝК\xadӏӀťȗȉŗˊ',
                    'л҃ȩwɫ΄ʡЅ²¡ǮԙӫκăńÙÊǖ˭ĲҷīœſҬϗÉ˳',
                    'ǟ?ǘʞŔӷŶ҅ЏdîρǟȉǏĪŰâӭŁ\x86ǍӉµјȠǸЇíĪ',
                    'ɖɯ˦ŐΜÄțçǷɆӈĒ˜ƃfѲƢʒ¸Ԕʹ\x9dʄрȉȚƃȫȣ±',
                    "ɄɉƨƌϰˬǫǏϰЙ\x8aь҂ǗҷӇ'ӫ͵ƞҡΙ˪ΥӾüʘѺԗȟ",
                    'yƚьԆͺϣѰśď\x87ʑ˻ϐʄɻŠưŚƥ˨Ūџ\x91ʂԚҫ æ6Ǿ',
                ],
            },
            'configuration': 'қԅɕ\x83ȵ`Ŋ˅µtҕþԫàІΚϗһDōĳzŮυӢӡИΖѐĂ',
            'permissions': [
                {
                    'action': 'ʧJпƔ5ˆԕөɃ{ȾФџǖщӆʪшŶϥԈžΐγЙӖÁ҅ȶ˞',
                    'resources': [
                            'σ˰ŠҗƏЧȒԬ\x91ŅZԅİȴϰŕƨȝǢЇšФ·Ӛ˄ϪʥƑəБ',
                            'ÛǅıǵƖȊ;ӯǺɉþемĂΗҚѰ˨ɟҦˍˣȡ1ȆԔŢЪˑҲ',
                            "¿źɷŦċӶýǃԆʱɇ\x90öҧҚӾжçɹʺʻ'\u0379\x9aɒћҳҚԪˮ",
                            'TČƆĵѦѓÑȂüȂ\u0378ԑΜˍΆŗřÝɓģkȞҭ<ƯÏЗҸϜΛ',
                            'ǵïȁő3ɒʬǞĐʃ\x96ΕѐªҗҽȄȞϣˍξɁî҅жĕǕҴʥƐ',
                            'ƫӸрȇŜǯœ÷ηɍſźɚӂʖV«ˤÁ˱ҍǴĝÍīюĐʁVɰ',
                            'ˁѯҳХǼξûϯÁƄͼӂ\x97ʖͿϑw¥ѥђɕɹʬӒώʕvɵΤh',
                            '҉ȓƄaҟĴΦͽЇр˩ƔǣĿ\x9dŶΖ¨\x9eȁҀķòӖԓ\x9eʠԇƤ:',
                            '(Щ˗къîΙǾŻ˯ÙļÈ4¬ȐůÒʵѱ\x95ˢΎƵҘɳϓΘƳǀ',
                            'ќ˳ϹɮƧѥƖʸĽ˰IˠħʴΩʠĮћƛёƛȅƂȧPŒΰ2ΧԠ',
                        ],
                },
                {
                    'action': '˥ЯĢƂɵϼPɡϹȱȴĞƼ¸_ƎĻәͺҏƓρʬҐɤåɘӄʨӽ',
                    'resources': [
                            'ёĭĜ&ʜЁЅ¯¾]ĮŋpмүԬƀҢ˙ň˰ȄδɖÜ˜ŀЃҾИ',
                            "ӢɢѡƃѸǚдΧ[=':ŨɃȫɵ÷τ˘ζτ³ ӝʷÞ\xa0ԑŐǼ",
                            'ЏȳʩŶҗϩĕNƸϚǱʁʹɞʜкШʨǳˁƯ#ŀ5\x88<ơʢģʊ',
                            'ʤϕČʘȅүäƼʕ϶Ʌ҅ƥƄǐӱÕĺ1ԀҽţǭϺӰ˞Èɂ˴œ',
                            'nԬ˙ʙùҠϤϠί˽ҵċƍԅɂ×ӓåʦ΄ƿȈ-Ž˪ƮİψԠƪ',
                            'ЙÃĀψɣïǊ·Ѥӫ.ʥΞķӂĝӣƉȥ-ѪqƋ}ƔӮ£·ǟc',
                            'Ԁ˃ǟǘ͵ȉЌʄɧэ|īƜōǩ\u0381Ęǒ,ŧīНđƨƷżÆǊ\x89\xa0',
                            'ȎӠʡϢƜєѢϬĪƺ;ĠɤȰNŀ҈³ΡļȣZϫѸεĶl\u038bˈν',
                            'бǫĖǿϏϱäŉӃѱÌΖ4ĨъƄпƑҥӎʦěȼγУÖňх¨Ԡ',
                            '1ЀτúÌƓƏìįϬϒǸƫ˩Ξςˌɞ\x936`ҽƂҷѭƍéϪӪȏ',
                        ],
                },
                {
                    'action': 'äєȰыԔʨԟьȮŨǱǇŨɜzϐˌԝȣƚϬҶĺĜ',
                    'resources': [
                            'ѳԓЫŨѕԭƌңЖÎʒˬʷŠͲź΄\u0378ȞȄƛ˞ɐȝȼϞʥʆҒ˔',
                            '½\xa0³П\x98ƃԊЎΊȲΘʌ(ąCҲмӐ{ʢȩЀýɄʺγÊеԙб',
                            'ĤŻεͻϋʁ΄ɷϭΡoȫȽöǊȉȭл҇ɠӞǷȏӫþϏѭbă\x8d',
                            'ӜȮ\x9bӻǝpÝJ҃κϷ}њĪ\u0379ĩ~EÒϣĈȣƘ¸ʈ΄əǁgǢ',
                            'ҷŞĊΚҬŨϟɺÓЏ\x8bʾϊѫѠðƛʘŉʏÁľȄêКш\x80\x85ƀѭ',
                            'Ąūʁ7ӜҀƭʸûиơ\x9fУ+ΒѤѼʠ\xadӵǙӟΏҏʱȥπTk¡',
                            'ϸƈË˔ΕӜƿƐғˆíԟԢџƭӌǈҬӐϕ\u0383πƕԝɥƒɝУɧȱ',
                            "ѶɷŵżĺѦŚӲűʅнáСє\xadшȴ\x97ö'²ĮҏҮ\x85ӹԗԍ˙Ŵ",
                            'Îʲαúʰ¢ӹʏéΜχϪҮрѪȦ˱ŕĳɌğɧξУη˞ǝû\x80ɟ',
                            'шсˤʵʼͷӇıЀȐƉÿËŜyʋǛίˎˣÜüӌҶҡƨ˺oҼς',
                        ],
                },
                {
                    'action': 'wϙ˹Ԇk"Άͼʖô˼ôǘɃŜҤȃʠČϕůңκϠϾļιgʈ@',
                    'resources': [
                            'ҵZӦӤӸϸ˔Ʊȸ*&ʕ1öΚз²zğǭɜơƲёǚɒӒǖʇê',
                            'РƔ#ҍułӦΖЀԖɀгÚϷʣė\x9dĞȍЍžˉ,˳ӒȟԬЎŒѦ',
                            'Rζ·Λʒ',
                            'ʧÿСШʆŕȶΎΨǸÜʥҀȠ҆ΓӬǏНŸʶ˧ŲöΙƳΓƔӏЭ',
                            '˥ԕÛӢϜǚÓĊёɌӍӟǄEȶǎȇƗƵшӺƫ§ʿįɂȇϪŪϭ',
                            'ԪĂM\x9eǇԭŐũ¢źӋʃӾĠɇΘĝѹӥïɊʩдȝĺ˲ɂɑӹŦ',
                            'ˤβԅË˥ϪŬ҇θȀƇϊĈ®ǫоÔѳ҂ŕƲŃκģǼɩŭʋƍƝ',
                            'xЭҴïΓˮԞʡñVÕǢɁԮ҇;ΚɖĭʒЁ¨ʩϢĴƓ͵ə=Ν',
                            'ʿʡЮʇϤãϧǗɠΌāǗʾͰèŘψѰÈФĘȣǢȵˋӥÉӼо\x7f',
                            'ÉʨĲУ\u03a2g!ЈүҾò¼Сȋӊ9Ԅ\u0382ÁĊƨκɕoɣɉ\u0381ǀ\x90ǥ',
                        ],
                },
                {
                    'action': 'Ϧ\x9eςʷџėȼėxŹ¬ŁßāѣɁŒ\u0381ʼұʇ_ԌнұӀɴ˽Μӈ',
                    'resources': [
                            'ѴƤɢ®ʹ˶ԖќȮÆҤŘɗoŊƖçԎσƊˇƀңľƱɒӭĘӛδ',
                            'ʼȏѥвτœť˰ǮҴɣҐαϻɂηʂŗԬƟç÷ǫımƞɥƧ(π',
                            'ɞхͿω˞UͶŚҦҭɑцɵ¥Ǎ϶ƥȳпƅʲΌÓǫ?\x9aԟ;ƱϿ',
                            'ЬӦ\x97ԍԏԚɥщЈЩ˫˃¼Ϭϋ·ȿɂƏƩɍȶҪԎ-ұƀԕ»ɴ',
                            ';ÝԪÕ\u0378ȞЊ:хľŇVV˷ȳăӼ˜ԭd\x99ҜԇjǘԢ˷¼ď{',
                            'ƻΰÒˏηӍŤƵԁζŅɘȁN\x8fӝˌRŹǅ=ԕǚҪϸҳΊѝӘɆ',
                            'ſʑԐОмƫƒЏΕ͵ҡҪҦΘƃ˽ӌŻȪɤʯȃʴζ|ĽҘʙŤƊ',
                            'ϲőҙŽǵÂʫ(ϋƻυɐԓĤӅʲҝҭǔȼ˝ӗ˃ӴƿƨѪ\u0380ǛЪ',
                            '\x8bȰȁӒӀəРôҟԗ˛ҮɽԞ|ӘЅΕÍʧϾȦĂԓǣϓǂǐҊҥ',
                            'ȎĚΉϛnο"ƞϨĿōҪƛʳБϭȳӠӆŸːƌ@ҁңČʑ¹ʼȣ',
                        ],
                },
                {
                    'action': 'ͶˍјѕƮâǥϑȎωşΩǾν:ȵŬ£ѥϞЧ3Ѹ˾ƱŹӝ˱ԂŐ',
                    'resources': [
                            'ÍΪʯӟˤǏӦĎßԭύ,ԅҙĮŻũġӜӸľѩ҉\x8bкĬ¿ƀϷë',
                            'N˨˷ĥĩÆDʋφĄЋƐóʁǹʹҏƨǴϬƴӹȕċ˚ӐΉӐƲʔ',
                            "ҚȘŏӗ»ȹǥďѤԕnɓÂ\x8dKōŷœИɳɦ»Ԉ˂'ӟЩįЩс",
                            'ӑ\x93Ӿx\x90\x8dťҙŽŪϤЭϙӣǧÆθķʷ\u0379Ğ§ӪkҖʖəʘźҗ',
                            'ƭʎǿÝŋΏȉɜƇ^ҳѓԋ¥ˆȻ˕ʞϨϺŬīϾ˓ЭʤӴǥȲÿ',
                            'ӌѼӺǹʡªΜ˟Ɓ#вϊȳǛȔɡ@ÃΟЃɈƪН\xadņýƸKɋў',
                            'Σ¼ƆҘӂÍҿƈωÖ}M\x8bÆĄɵɄДԘƛϦӺȓ\x84ʩюÜɲȜı',
                            'Ќ£ɦǴӌǩAцѻЋǝǫʤӥɴӪ˂ſ˧ǛțҒơϳԄӅЈô{ʂ',
                            'ҭ\x87ŕ÷Ъ4¢(Ԧ¯\x9bˁňȟЄ³φԡǪЌoRėÔɺʍ˙ĥǠ}',
                            '˴ҝɫԩ˖ȑÕБҪ·τǻˬԢÔÀˉђƒ҆˯ǖҟΔ»˕ӷOɹҡ',
                        ],
                },
                {
                    'action': 'ȉȆѼ\\Ƿ\x8aňХΫ8˵ƘӉӢÆ¼ƲįÇАѽ>ǧ·ѦϸªΞt˖',
                    'resources': [
                            "҂ԝƁӍБƺ\u0378&ÐԤ˭û˽ѧ¤pĳCʚ\\Ăʺ\x98қϙ\x9cƶǵž'",
                            'ɠϤϭƬбˏŔӴӃҳǊʓҥЉ,ŏ\x9b\x87ӜȄƘǦƄԏȾӏԓԢŊΉ',
                            'ȩμЂҁɴϳĩжϽũʥͱӼƴĆΩγΦӑǂȻІ\x9fӅȨŃaҙԮȏ',
                            'ʎɝ¹įȱ¸\x97ѪʫЖµñӥНÔ˳ɾ|ə&ΈĝmǴʞʧΖӀѦ\\',
                            'ͻ^ɼϺʋˉЦHΎҷ˗ΰϏĕӗȖϴʕҮǣtΔҏѪФӸǁѹŕэ',
                            'ԫѪґЌԚӶiȤӌЩĞԒԀъʹȝbЩȲҮιәņ\u038d)Ƀ®ǝȤл',
                            'ӐıīϑʨĪȤĈƭԛˁËȎˁƾȞѼ|ʞŏʋӛӔ\x90ŅÑѺʥӎɊ',
                            'ɠџ\x8dǻӼÌ\x92ƋßоѡȨϯӈɊŮWїҒŦБԐЉϽϊҚ]ӓĐʏ',
                            'ȶԜɫ<ЈЕԐäǊ˲ŊÝύΨ\u0383Ǩ\\ҢāǛδАҋŅ˕Țɖı*ӱ',
                            'Ɉί\u0378ҔЫ˕\x87fïʦƺ=ȲҩұȟҲĽϪŚҥ',
                        ],
                },
                {
                    'action': '¤ҭˆǮϝͿԍԋĘ',
                    'resources': [
                            'ӧΓёџnÒΐŴЛǽÈˠEїʐǾñЈ)ԣϔ҂ˁʖҐҊÒѣĂ!',
                            'иЭűǡӷӉƎǱǢɱԕß\x8aêƅŞӊͷԌĊԉaâπƗĊįàϗϪ',
                            'ÞΤїêŴǰƣƀƮМѳʢɘҎ,ǽă\x9fƚǽԓтĥȾύĊΣùǭӶ',
                            'ͳУĹԄ΄αɬɷϓӬC\x83ԏ\x90ϵʭ\x9fϩԮčǳФΔϔïlªбʃĽ',
                            'ȲŠt˫ĸƵǲŦͰɥȮǻęͶɬɝʾ˪ÿӧёϐˇԫʕӯɥьƗ·',
                            'ԥʬϡDь×øӮƮÑȎǑӶԍяΣӸʸ҉ӰŰѯ\u0379ҝ˜ėɭѩˀʖ',
                            'ǫҝO˚ˣƖϲӠȥκXƸ¨˶ʘǸĮɸèЊȋ±áңќčԇ\x89Åϲ',
                            'ИϟĎҔӈĩȀ˨ϒɨ˨ȸ˝Ì\xa0ƪ˒ӯӠԚɷkҒƭȘǅӾƞ&З',
                            'ąϪӈΣϟ½Èśȱ\x8fŶʣ\x7f˭ѱк;ɌђȖҪ϶νΉãƜYͳŶ˺',
                            'ƝӴġәȾчʡΡҎĝʨ~δɱȻǦÃ˘ЫyǌΔˍƑːˈʱБʗJ',
                        ],
                },
                {
                    'action': 'ƏάˉԩЅЙ',
                    'resources': [
                            'vџĳŚŝćƧœрǜ˚Ǔρʄ\x98ƌ:ʭϧž\x9cйī˃LƛѭюҊo',
                            'ƥΓŮ҆Κɱ˖ƄƕϱԭԧΨφ\x87ʂҪњƚ\x8cσ҅SâΖҙϢƞǝ6',
                            'ӛŮϱюƸοɂϔǮʃƣҬŌƈ˦ZżƹɞˍʢɜԑaįSeҲªȐ',
                            'ПñĿӰ˄ԟVЇ˘όηҨɌƅ¢ΤʨсЦȏҖƨüˋΛҳ҄А˕Ԁ',
                            'ɗċȨ7ȇƔ¬\u0383û˸ǙɃ\x89ĶɬŵӛƣɏɜΝúӸ˂λɐϕο͵È',
                            "ȩӕƨʕ'ūȏǮЂĬϯȷˍӓӣŵчȭʕƙǺјη\xadɕ\x98Ԑľ΄Ś",
                            'Ғӗ´Ôʙ˒·ŸˀNŴąϱ\x82ŕӋķ҇ͰʺĪȰɭßΧ˾џÎ´ϣ',
                            'ĭǠU\x8bĘǊӛƠԎǅΑʩѨğǒӍ\x86\x98Ѭɡѥüу\xa0ɼѪǎŷԖƠ',
                            'ǯ҅ĤҖÃεʷŶЭǊőŚˏͱЇʈӉʤɼ\u0380ӯˍƽȉїҽ˘ɆɌѼ',
                            'ǒßѐ\u0382ÞcǺȇȬӏζʌƏ8Ƙήϻҳ˯ҡҕЅµñϭɾ×˽ƫ\x98',
                        ],
                },
                {
                    'action': 'Ȭϟ>Ʉɏ¨ƟȐĶȞ˵aөŤηǉԫʣΥȤϢƹïԌȀԥĉΨwҖ',
                    'resources': [
                            'ÎʠԍІ\x8fůӑŉӴʴƃˤȏ:ΝĩȆӍơȴԮĚʀ˸ѪϕЮҧî0',
                            'ӜĨɅǅҝʺǃʕ\x8bʯÿĜȝѓɩдƆŸsÒţӦʩϙƎ˭ӇƼšə',
                            'ǉǔФȌҬňƻüiʂɂҤΛϡ˽ôɒÆʹԌˊΚȡɉȮӯЍâӉ³',
                            'ʋ(ԗΜɚɪǰЌťĨʂґĭɏȟʦiУ\u0380Ήė"ԅņ҄ǐɯ\x94Ȭʩ',
                            "ӻЇ˹ƭЏƝɆűȬġKђЌӇ'ğȺ˙ȊоΟћţϡɳpΙhҎӊ",
                            'ȆɼėӱūӌĶЏɗnиеԞʴ-˒ļΫϩәО_ιҖɈǯϸϙƥǵ',
                            'ͻŤÃЏ¾ˉƶӪŘěÿǩXαϱŵċo˅©ȪƨдɃÆƀʿӼ˸Ð',
                            'Ӗ˙ȘɵИϔҩѷϮԭù˘ΜǸgƊӟОȩʙăƉͼƊ®ϑȷǈú˸',
                            'ӋήÒĿ2ƵҨѻϺĽƖɄnŃӷӶЪξԛΈ\x9cψϛҳΓуԒџˑИ',
                            'nӕčӔшϵԧĖԖţ8=ɸҙοѲӨӶźoƪАЀҵͿßƽ΄ɘЩ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ƺʂð',

            'version': [
                -1505954169366513767,
                -5298391749537234407,
                -9109941386258191733,
            ],

            'location': [
                'â',
            ],

            'runtime': 'ɧ',

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
            'name': 'Ьɿ[ĬǹһşʔŨӾԇ\u0381ŸгɞBƔΟʾǃĺ9ɴI4\x99ȃӇɚÃ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '\x8aƓϭ',

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
            '$': 'ÖȢӉI˘Ǥӟ\x92Ɓ[҅ńǒȑйΨΈvƣǋĺϠƠҘƓÕӮΌɶɕ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -2019164806571587799,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 976716.7359459051,
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
            '$': '20210302:165152.398944:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ӽԦɸԩ´Ɵѻ=ҒǉɁЈƲіԈЅτǗѸ˳Þŕʘ°ћμ҃ɐ\x8fϏ',
                'rƴУһұПʔǺ˕ρТűʾƈʜӉΫͼŕɮÑɝʠβTѬӨǽƁԏ',
                'ˢ\u0380ѷ°ѢХʐӇӭ˹Ģ΅ϹȺǟԔνИτ˚(фёӲ\xad*ϧǱҏe',
                '/ĉȎͱёсůүҹģˉβε˼ҏʠΦϿøãÚ(ʳKьȍƒдѻŔ',
                'ģϏ\x95ρ\u0380{Ŝ¥ʙҐύǓʜ˧ûԓδΉƏҨÎŏƺã-ġɲ°ėƷ',
                'ʹ΄ēȓѷʄІѽ˙\x81ƴƹүň˶ÚÄjϤ\x87Нӛˬь?ɪϿŽɖԚ',
                'ҩһЈBöâɗĢжÛŁҝJάʜˡӆɯԋ˲ЖȲӶҿѬǇѢΤӼƭ',
                'ԞЖιļȩùѬëӹϳΤϥXцлԮͼԛƍɦĹΓȨĢ\u0382ȼőӶŶ`',
                'jԬ҈´ШӄθäџǼЌϗӈƫνбЬƸыЦ§ӮҔēɲiʻ\\ǔ»',
                'Йӆɷργȡȕ°ʭͰûЀΒӻŁΡ\x84ПȸÃäЀ\x83ļǜǺɵΔΥƇ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -175434429225283402,
                1528383821411686598,
                268674459787711496,
                651801397343061813,
                -6903115404030945966,
                -5121236417041705111,
                -8446092983572569165,
                -4945361344716008889,
                -9205127286471365316,
                6838047280451486615,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                823012.8516756671,
                476796.9426745763,
                559854.7374041567,
                874325.1806486069,
                209979.49000490253,
                297147.05112144427,
                327981.2019314624,
                370986.0724455045,
                534312.0094957321,
                33011.36096759682,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                False,
                False,
                True,
                True,
                True,
                True,
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
                '20210302:165153.674551:+0000',
                '20210302:165153.702367:+0000',
                '20210302:165153.733042:+0000',
                '20210302:165153.759499:+0000',
                '20210302:165153.783524:+0000',
                '20210302:165153.807496:+0000',
                '20210302:165153.832707:+0000',
                '20210302:165153.857888:+0000',
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
            'name': "˾'ǺȸÏϒ/ş˰ʏãσӄȽ΄",
            'value': {
                '^': 'int_list',
                '$': [
                    160321454982584815,
                    -2944713584234812527,
                    5277398709972785187,
                    6679375913370352885,
                    1547203910390268272,
                    8314692571231199506,
                    8390590266482930193,
                    4241676651141980488,
                    -4292762500386273602,
                    1864300088883655149,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ƙ',

            'value': {
                '^': 'datetime_list',
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
            'catalog': 'ˇѸњɜЮ\x9aбʉŐюùҁƙϭȲΦȚǔϮǚDԙӰ˺ЋϮǉμ±ʌ',
            'message': 'ΧŋԉKǐǎSӠ˃¬\x92ӠгƥwɲΡίЫчƯʛȷ˥ффǸÁЬ#',
            'arguments': [
                {
                    'name': 'ӅˇƱԭΗɚǂϜҥɌϸŠμЊƃƮ\u03a2ΝϐϗβǱÊɍΔ\u0379ƇƽÛ˟',
                    'value': {
                            '^': 'float',
                            '$': 893152.6514661954,
                        },
                },
                {
                    'name': 'ćëюǈħńą>ƀmɢīҷ¾ƅÒȖȐҤơϛíСɺаȑŞ»РÀ',
                    'value': {
                            '^': 'int',
                            '$': 2870121298549992686,
                        },
                },
                {
                    'name': 'ʃя\x89sУþФѾ˷Ĕ¨ʓӐўzϠҜȼҋǵӻӧԚқɺɢЉьЙƿ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210302:165149.456808:+0000',
                                        '20210302:165149.477709:+0000',
                                        '20210302:165149.498288:+0000',
                                        '20210302:165149.519463:+0000',
                                        '20210302:165149.540087:+0000',
                                        '20210302:165149.560615:+0000',
                                        '20210302:165149.581910:+0000',
                                        '20210302:165149.602548:+0000',
                                        '20210302:165149.623052:+0000',
                                        '20210302:165149.644003:+0000',
                                    ],
                        },
                },
                {
                    'name': 'όɘƨˁӓӞʓ©ыҚɌͳԋɫʴɨmМɚԭџ|ԁɜȹǚ҃ҾɛŰ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        6736122170209615096,
                                        -3075230033574086084,
                                        -4656314112500075938,
                                        1803578017112847668,
                                        7327466034237643450,
                                        -3936901547089300745,
                                        917485867936895706,
                                        -3788504011791743062,
                                        -7297212957672270752,
                                        -952364304151629783,
                                    ],
                        },
                },
                {
                    'name': 'ī9ĉʦȋưİԘϡ͵ѭӓΊ)ЪfǝаӡæӿПѭʷэ\x9aƦǬͻӱ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': ':шʑɕƏ\x9c\x81\u038bƳһ¼ļǏο˧ӓǿԪā\x8dϴ˞ǥơѠƇԗѓ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        3632134377125539566,
                                        -5512083254025777432,
                                        5511199784801011983,
                                        4436326558212551778,
                                        -3950632245701106120,
                                        -5862940810230478347,
                                        -4896175932978890783,
                                        -692492345385258778,
                                        -690429381625246358,
                                        -730251239553914166,
                                    ],
                        },
                },
                {
                    'name': 'ˤȓģăyёùϨ',
                    'value': {
                            '^': 'int',
                            '$': 3855759434394665250,
                        },
                },
                {
                    'name': 'ȠûÕȥɔĖ\x86ώΪԨŚʆŘϵ\x8aŢͳ\x82ʂƻϷ<ԅÕӠϧұÐǃϋ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210302:165150.699384:+0000',
                                        '20210302:165150.722194:+0000',
                                        '20210302:165150.743666:+0000',
                                        '20210302:165150.764803:+0000',
                                        '20210302:165150.787354:+0000',
                                        '20210302:165150.808214:+0000',
                                        '20210302:165150.828782:+0000',
                                        '20210302:165150.850472:+0000',
                                        '20210302:165150.873496:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ЛǛÉʄԥӑ˪Èʸ˂ȡÒѳзſ˻зȝāϥŔĘLOʻҳWOϵ·',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        6025923104671055155,
                                        5188967839337738102,
                                        7852202162897020050,
                                        -4700675877725054234,
                                        -1409149916978194942,
                                        -7571258040448780432,
                                        -6805573020047380089,
                                        -3762645873485147752,
                                        1911311534092154300,
                                        -8734397078301002556,
                                    ],
                        },
                },
                {
                    'name': 'ԥѬҽҜŶ4œő',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ѶѢπҍ¶υÁĆɇ\x9b˻fŃÒԔȸĮºԦеѶшoӼԌʬИϞҜӽ',
                                        'ͼ{ҰӟŨȯØĹԇԄȒѢҎϭұLɤ˯ʞˋêȡϊΆʏήɞάĵʥ',
                                        '\x89ˣ˜Γɥ˻ѥ×Ũ˦ІʎҍōŨɱ˝Ȱěhɹ^vŭ˘лˑԭǽӀ',
                                        'ýϻς˄ӯɝɪýş#ӁĄȑΫůΙ˙һȄĦ˧їì˹ςËѢkȋ˞',
                                        'ÄʽÜдð҄\xa0>Ơƚ˔ǃɺ~ɤ\x80Ćǚʂ·ƨϹˎҀ^ȝϛɲҸӋ',
                                        'ѽɢ˂ʺÜÎҳ\x81ç¸ϡһʌŠǉƖҤʞάӘɆzȫѪJħÀČͿź',
                                        'Л˲řĮѪ%ѣJ¬ƎԇþҪϋċőΧЪѿľҺĜ5ƽɷǸϳŜѧʏ',
                                        'ĄЯѢɳѥтƕʳ\x98иŌŅNλƾъŜӈΔԝӸϻ3EΠǒѺʲйˇ',
                                        'ƔȆӋUėȇӫӢĸż7ϲ҉ѤАbĉÇɺӦЫxĵȆӆЉȟƚІŨ',
                                        'ϧұϖԊΐˠͻЦ\x87ĸИҤ»ѰŶӎ\u0383Ν˥ƋƶӨ˜Ėũɖl\xad¦˶',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ԮĨ',

            'message': '\x9a',

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
            'identifier': 'ʁӆюɲǠЋѯ\u0382ɢuѩ˒¦\u038b˒L˟ӻйǻЇ{ĺýĘȉƿԈˤʎ',
            'categories': [
                'network',
                'file',
                'access-restriction',
                'network',
                'network',
                'invalid-user-action',
                'configuration',
                'invalid-user-action',
                'file',
                'invalid-user-action',
            ],
            'source': 'ǵÒ{ӼƓӰ˰őуʗX\x81˻ǯƵʲӊ\x95^ƍΏԏз<á˕ŉǤϯ¶',
            'messages': [
                {
                    'catalog': 'ŗʎœҫÿ˧ǹ҆ϿŲKwŤҹӢ\x88ϟ=Ў®\x98еʷӷĢџԔӣҒɠ',
                    'message': 'Ӿˢɾʮƌөƞſх[ѳьȝøϋáҸдȃϳʳѸӽϿ˃Гɟ¢ӔȪ',
                    'arguments': [
                            {
                                        'name': 'ȟ~ˉȗъӽȝе˝ӣ˅ўй8ƹǘȶŠ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165128.937144:+0000',
                                                    },
                                    },
                            {
                                        'name': '÷Ӕоεƺȹ¬ϧЈɉĻɭŏġƎΕıϘЮŔǋĸ\xa0ǌÙͳ/ҒƎǨ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8434930606444398292,
                                                    },
                                    },
                            {
                                        'name': 'ġiϫ\x8dβȫҼ˰ˏ҃ЫƾӲˈ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 332478.00192881556,
                                                    },
                                    },
                            {
                                        'name': '\x85ĨƫңӊɒʙϦʤɩˌҴʜ΄\x95ƔŕκΚņĸӡШӟȱɺ˜Іɰ2',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            763823.42986916,
                                                                            497021.00917812984,
                                                                            45452.0709062691,
                                                                            831322.1690724262,
                                                                            75880.75383753932,
                                                                            494758.99908659316,
                                                                            777633.244496537,
                                                                            719016.2596549991,
                                                                            109039.86186436441,
                                                                            924587.3855053147,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Д\x92ĴҺӭӒ\u0382˧ÁϙȌԮώάѷ˹ԃŤӈőүɇԙ˪@ɴЖʻϼƟ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȍЇɼǒ\x8cĂǺǸǈŊœΩԏ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165129.693396:+0000',
                                                    },
                                    },
                            {
                                        'name': 'HϸʆɢɍʱǓɻg˃\x8b\x85ēʰɨċ\x94Ļʗč˝ӺçΎΖİ˄\x82>ό',
                                        'value': {
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѯϕρоɿdɟʋӬǩǳѦɡǴ˞Ҍё˟ĳăӦ¥Ңǹǖ˶ӕʺȇ',
                    'message': ' ӠҋӐǓƐΩPͲ»tѓtͱiӅԖĩ\x9fԑĶ!ʕЃЭǉʗѸy÷',
                    'arguments': [
                            {
                                        'name': 'ӅΚˈһšЪҋҌ¾ƲҀõșˀˈ-ԏLӫϔԞͽ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165130.151911:+0000',
                                                    },
                                    },
                            {
                                        'name': 'gýФҳBƓʾêѷԗʺйƭɿϘδˎĊƥӪѴΦԃɥéҟӘ\x8fĻϦ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ΫįӗɆΩԓ¬УȊϨѦΙѵӼȐjζ}ʧź˧Ѯ˫ưҁ\x86Ňªϥԥ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
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
                            {
                                        'name': 'ʥãUςʜҙǘǗϫΎčƺˆǾʯǝȌɏǦjaȴŞ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȬӾ-ƴåΈŤɯȸͳÛŷˈȢӺ˙ήʙȴυςƵç°~ǝĥ&ǄӢ',
                                                                            '®ξˏϺӇӖȨϠȧðfòXŖ{ЬУŠ˻УʻѱȽ\x8e˩ĥɁӠǂв',
                                                                            'ŽюɾŒϭƣİɸɨUЩӢȟį+ΕʱÉ0æ¼ԫ˹\u0379˲ǴΑʿРȋ',
                                                                            'ɃԢЭҁ0ʑǊΖηӁį(\xa0ˊœϮƤ\x9dǎǣöŹɩЊüʴſAѣ˒',
                                                                            'ǙŖðȓԦ~Њ˞ŊǆΙҔΔӨ¢ӿǣШíæôЊƃǷɟȞεːгɑ',
                                                                            'ŋəˋÈΖˋ\x92õӊˤЦЉāҸҵÑҠˮǴΤϐĒˉB§ҎЉǇԕѻ',
                                                                            'ωȬӫɜʹ;\x99ȟđӉǄ^ͳǅQŵϢ˯ŲžƣҶϡӗɒɞƯƸʼӪ',
                                                                            'ҩČƲʏ˥ļԧ=¡ʭɚɺěԅ¥ƶӑХϨĩεʇØԉˏ«҄кëϭ',
                                                                            'ѸHρξ˥Oѡ˜Ë΅ĄYӭņ˹ŧʷӰ¼ϋуǸѝцðǚɇèӭǦ',
                                                                            'ԁîɤɲȺH΄ќŴóԐʹǝĺѤ"Ē\x93Ӷɞ˒ȋ2˝¢ӸɄ\x8c\xadԦ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʵØǧńԭ˛ÂûȢӐąŅЧΥşЕɌș˽Ҟ˖ϳѯȴίůЊȅƪȫ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8982943694486514359,
                                                    },
                                    },
                            {
                                        'name': 'ӻӿ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƊƜȳ϶ρ³ʖ˫vÂ]ǖʑɺǷƳ*ҹԑµ˶őӸјҗ˨ư\x7fΥ¶',
                                                    },
                                    },
                            {
                                        'name': '˗ˣĤТǄēЧØ\x90ʢҎġg\u0382˳άё\u0379ɐϭΚхмĝ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӬxǴŽѻͳníѠϝŹђ҂ЀˆɾҎ¬{ҧǱ\x90βˉÉä\x88ӈсӨ',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѶÉǚǖԬҺЁ.SƆþÇEЊԢѯʍϙªˣǥҪи¾ÍҐΗİϗő',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4909191553592858905,
                                                                            -557095113363920071,
                                                                            -1120846816828391852,
                                                                            7745583551913070508,
                                                                            -4650719809417798348,
                                                                            4422222528991574203,
                                                                            5779883515099111613,
                                                                            4172458469539790219,
                                                                            5784380709188036923,
                                                                            1962656314530425944,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƑŬЃǥ&ҝˉѨäӸԏǷƏɅȜŉљήı˻ʟCʲхȻϸϔ϶ãƛ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            608217.5999937577,
                                                                            812945.8101156737,
                                                                            234359.23372470093,
                                                                            204278.19912328344,
                                                                            526308.1750921095,
                                                                            441320.65958597045,
                                                                            915188.358315382,
                                                                            325447.56914827897,
                                                                            279840.039782663,
                                                                            222681.34371105675,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ξ)ñȡӴɪҝʽӔЧČƳz˗gΥǀɽ˳К×cЙ8ßʐ˜Ěéǌ',
                    'message': 'ԋϐÜɱEўʆʧѓ҂F®¸Ԩ˽ˉǂϽӰԑʋĩwʩȻΨ\x9eӤѬԦ',
                    'arguments': [
                            {
                                        'name': '\x9aΎʜһԮɴ˙ƗХ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            643986.9161178797,
                                                                            529567.2438545241,
                                                                            761547.9424286858,
                                                                            701472.4155527729,
                                                                            107362.28227831807,
                                                                            174227.4034895639,
                                                                            711000.5480545844,
                                                                            17060.010671006137,
                                                                            513343.1467246149,
                                                                            210238.3024066906,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '²įƗʜǊȞȁμɻʀ˷ɡ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165132.877275:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѱ\x86țɉËӨОĎʕΔʵϊȯʔ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'D¿ɻc¤ЧˮƜ]·ǯʱ\x91όŃӚԂѰĚρgРͰBЩġˠΆ¶ό',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ε½ӸуǳʐơŁѫ¥ǝΌЇ*Л®7ÏѐΜΐӬɹʔѪ\x93ɜã\u0379Ơ',
                                                    },
                                    },
                            {
                                        'name': 'Ӌ\x96ϪŭěΆңͳәӗ¦ϷŧѹЩʢΏǬƼǉÍҳʨŭ7ÔįRȹл',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԒΨԮįɡȤʉsɉΟĠƠɯ/ϞÈɸ\x86ĊźџѓˀβʹöȦǉ\x83ƌ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4059850529747617344,
                                                    },
                                    },
                            {
                                        'name': 'ÅȾµǍ˶\x90҅Ĉıе«ɰ\u0383jӭŤčĮźÔϊÍļŖϱɪƃɨȅӎ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҽҔѸΉϠǓɐқѴɞεơ;ãѾőΦGʝųȶӨɑʏƈ˦',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165133.680257:+0000',
                                                                            '20210302:165133.701240:+0000',
                                                                            '20210302:165133.722402:+0000',
                                                                            '20210302:165133.742783:+0000',
                                                                            '20210302:165133.763267:+0000',
                                                                            '20210302:165133.792115:+0000',
                                                                            '20210302:165133.815428:+0000',
                                                                            '20210302:165133.836766:+0000',
                                                                            '20210302:165133.858393:+0000',
                                                                            '20210302:165133.879100:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɓţƦȭμƸÅōГśѹ_εɁΦԉQѿƑĎȱ˞чӛΪʊǕÃǡʖ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5536374408177258368,
                                                    },
                                    },
                            {
                                        'name': '˥ÅʫȪʖƵгѹʓʳțМԅȟȯÕƛΨĥɖȀƠǚ+мґʋӍ\x92Ҭ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2730134308563361462,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΙӤʓù²ώ`χҴӆŒ˚\x9eǪƭíИӉ˃ɨ˹ǋȚƗƤùˎԜ±¹',
                    'message': 'c\x99ƪӇáӿȐȫÕȦЕɀɹ\x84ҺԒȔуæϕԝʽЃè&ĞĆȨώȬ',
                    'arguments': [
                            {
                                        'name': 'ʸą)χʚKͼ_ҢЪήȿ°ǤǨű',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ŔŬ˳_ʊĻ˵Őϭ¹ė\x97ЗĨªĵϧǻҘнĎҫÎά',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '»жįŜBɴԩîѹȖŝǥ ʫыŉǏŧċͼȉƲ˽Ųʃ˅.ƜBĸ',
                                                                            'ΕЊǥƖƱ\x9aüҀҨųӇі˸²ϔ*τӻΏʡIÙŽӸѬλčнΟϯ',
                                                                            'îќŝŊлПиһЍ\x81đԗVĄĠξϊ·ǏǳȔƲɪŶɸˮδÅƞȖ',
                                                                            'žõŪɛʶҭӺĹрƢѱ\x93˪țƉăBνȆ+ӔѥʽiʀӫľɔȽ5',
                                                                            'ί@ƚȡ\x98ʽϯĜΓƿōƤʠɰśИԏMОѤЋ`˔҇˨ҾԕǙɻΗ',
                                                                            'ӷĜԢҩÛϞӏΡwƱѣɅȮMȡϰŏғ\x9fʲΌɇȘÒѲʶĂɇɔɯ',
                                                                            'ԧŊŪǱ҂Ҋ҄ıǒΫҜҕєόӶ\x90ϠŅа\x80ŹӼÊ\x92õæԆҕԝΚ',
                                                                            'οʫԬʮҲ\x9eǅЭƧÚƢɬǴԮP\xa0ҞЬӱɹǪϾѪӁԖ§ȀǨđÄ',
                                                                            'ҰƏәʻωӋщƒф϶°ǞrǾƍҙ\xa0ŐĐԉȄЈǚԇԃѮƤÔXǐ',
                                                                            'óŰǎȟŚÓЋğ·ŷȱνҋŖɌθЏ\x88\x91ҬʎʰǮȦЕʹЇϐĝʌ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʍӞͼжʀҙӃЏашэȹċȀхӸѐǹ\x93lӆȢͶſFĠȟӱϼ»',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165134.735585:+0000',
                                                                            '20210302:165134.758156:+0000',
                                                                            '20210302:165134.780840:+0000',
                                                                            '20210302:165134.802477:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Àˊȅî\x93Σє+Ӗζ_ȎҦ˜ÑЧҼěЇ#\x90ӛŵƸ×ÀӂΗ!ǽ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            83767266519344256,
                                                                            -1434885047382814415,
                                                                            -7416468895803851975,
                                                                            -6443385042282182489,
                                                                            3746049940246263346,
                                                                            5853130897392557820,
                                                                            -4206056041352696802,
                                                                            6294583537984403642,
                                                                            -299482952354392460,
                                                                            5829010511942719875,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʾ˭ϟßӈĳѥМjқ~ʠȈӣѧƯӒůǅҞŘǑʦѐӒϘ>ǚ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165135.205451:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ΎʄʡХºƊɴ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'љBʹҔżαǠ6ΜɃʅӲԊ\x9aȑoϳКάSȏϕɡΦU\xadΚίҕw',
                                                    },
                                    },
                            {
                                        'name': 'EgРѕzтϩrкҝʶħҋЯīɬɧĮϠԅƴȑԛ§%ǉƬԧƞ@',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5921587735659975611,
                                                                            4974151342326806360,
                                                                            -1181991232175287988,
                                                                            269102105586016500,
                                                                            1554969355027226907,
                                                                            8974442778785343126,
                                                                            3581390004586079250,
                                                                            1198866151490466535,
                                                                            -4467435554750734385,
                                                                            -3461226987152125645,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΎԣÞgή',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165135.669043:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǒĺ˪ͲȧѡϭȳǚǟҴ҃Ëɦɵ|˯ӕӅʬªʊʃΈѨŅŎŊƣÓ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'і2ӴԕѩĥҨȢ·êů\x86ƠҍÙҩƤѱΔͷ?ˮϴıͷʛυĜǊ8',
                                                                            'ƄΡнPЙυƀÅǖķpѦάę¶ʾϹŁүŔȲѤȞˈѱХʟаŪϼ',
                                                                            'ԈҢŴşƧƪȲѻƖʆƤ\x98Ơâʹҵ˒ǈƮԝѮΠĈɯʭìðƾƂr',
                                                                            'Ňˮ˞˞ӛʀßɴШѲ¶Ƴ\x9fˉȒĂ˵˦ǞȿԠŧUǔʩsĕ`ҵĽ',
                                                                            'ȧȢΎºǥϗ˅~ΛËӉΎȇȲpļ\x96Ǚƴʏ$iǳÞ˾ǡӰΑ˲Ǳ',
                                                                            'gƓԒȸЈЅÚ\x8aíɾɓгΫʝːɪ\u03a2ӂƤњěĐ\x88ҝ9\x82ĸÌЅԣ',
                                                                            'ЕϞԑԘ®ҴŔѐÈōΑɏǑ\x89Υśæĝʟзԝҗȁ\x86ύҔǻә\x818',
                                                                            'ӴȥʮĎРέÜӠҪí˄ΈƎәҰȌΎ;ӂůʐщУʰ\x9aӘʼѠÕ҃',
                                                                            'ʱÙǶ˄ѐ¹\u0378ȵ\x8bŽɈǂ>ͽʍГϩԄҫ΅ǖҫ¡όʣЄěҙĀm',
                                                                            'ǹƀϕӄɊʲñǏ\u0380įϫśʤɷŢЌ\x94$ĮʴЉϦȂɅêϪϥΤ˵ȟ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɦ˽ǲĎǗʙϺɨJÍƤϢkҹЍȹʻαǣǟȶĴǈʵâҥϑÈùɔ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŠӞȁЏЙΎɈԫŎˑҜųĳб½°ԍͷ\x81ˇцǲϒεҫ˒ɻ¥Оd',
                    'message': '\x9bʜΖȎȏŋψǄ8ԅԋϯжıŎȊӆͽȊĪˮϙхůγʘÛ ϟT',
                    'arguments': [
                            {
                                        'name': 'ʆȓѯwUХƻΎʳ¤\x92҉wȓ˔ȱ˶˛ɯɽŭӮ\x9eǷӄĖɌ˜Ӎȱ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '9ҍǒïИԔǼGѱԟђȡʒŎÎʙμȩˋƁӕЊɉȻңƽž\u0383˅ƶ',
                                                                            '\x8cήӢ\x97ӻӲɕΜʫÐð\x8bǋɪԟϐĄԃǘŶӜӺԨā҉ɺɿɓėҋ',
                                                                            '˖ҷɰƥ_;ȢƧύҕʷɐ\x87©Ĵjc\x9f©¥Ě҅əϚȳLίл¢ȇ',
                                                                            '¿_Ѽ˔ȿΥюȲɫʰÒſ(\x8eГûΠïѯЫĘԎȤԂsņÏΈӉǒ',
                                                                            'ǉǈęʨ½Ŋʎҡĝv˘ԡϹģȱѦƍ%ƽȄͿȱ\x83Ĭ˸ηǘҽѳԚ',
                                                                            'ɉϦѥ~ϙκӸӇϻνĘĭΣ\x9e$\x7fÀȽśϨń˹ЉͻҔǖɍę\x90ǅ',
                                                                            'ц\x9cӏϓŔҏϬɤdɷϧǸÝ҈ԏȬѭ+ԣʃҺБǪϛӢíӢƓƋɀ',
                                                                            'ϮƎɓˢĹǧWĘӎҩ˺ĖŚю-Е{úѰԀҬĴKԤɀŦ¥ϕдҳ',
                                                                            '«˽HǅÝĵԈƽϡӮиɬǚԦ°ӝ\x84ыϟЮӘƒё_Ӝ£aɀɭɣ',
                                                                            'Àω~ȟˁӌҫȑʩ%Ѝëŷˠі˵ѻϚʌэ\u0382ͼԤƨԍƒгTšҲ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЈŉЎԭǿϷӐǊʌλѹ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '\xadҟΉɋýˮΡӔӏԃҫƼύϯǯΧőËȴȽ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165136.503293:+0000',
                                                                            '20210302:165136.530228:+0000',
                                                                            '20210302:165136.557025:+0000',
                                                                            '20210302:165136.583559:+0000',
                                                                            '20210302:165136.607322:+0000',
                                                                            '20210302:165136.631800:+0000',
                                                                            '20210302:165136.656726:+0000',
                                                                            '20210302:165136.683949:+0000',
                                                                            '20210302:165136.710232:+0000',
                                                                            '20210302:165136.736839:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȴ\x91ßɠҫƩϗ҇ÝϙΨƋlġƴU\x88JЉɹȤѕм˸Π\\ҲȻ=\x88',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165136.865281:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ӛłνǃʕń˞#ӭZ\x89ȹӓѺӽʗϩȑѾҹʧЧɐȵKϿȄǮԥҌ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ÑįͲԧΡơĭǘäӯђș\x8aϐĽϋԔЛʴĪҕ˸ǴŴƅĔþѬќƑ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            144370.32013642526,
                                                                            584930.970042298,
                                                                            52838.84964878915,
                                                                            637066.2089677429,
                                                                            -4870.060992258921,
                                                                            549221.2732234243,
                                                                            327909.49507179065,
                                                                            832421.2425472337,
                                                                            150346.01303933834,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʑB',
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
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϧϜйąƏĤƥ¹ӟǚɺШ_ўrȨťʧʵˎǄкѮŶЈǁ^Rяӄ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': 'ɮĘɘщǟʭǖʂ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5743856114643673910,
                                                                            4771600312332525897,
                                                                            -704709857588918116,
                                                                            2469353274814527899,
                                                                            -635295364060039744,
                                                                            -417233046591883688,
                                                                            -3567017315033910501,
                                                                            6098910211803705812,
                                                                            -4386187753215745999,
                                                                            3105243372973511692,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʊŏӽπçԀˣĕʓƠҢqțұǛчюћƱӝɭҮʣΑԘЈǃѽñǞ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ⱦι˜ǗӝſŎδӎřνȒͷɳľàsέζ˘\u0381ѻ˄ңŴÞÛƯѓϣ',
                    'message': 'ǧҸτП&ʢͼ˨Ψÿ\x87φʧTǃ_Ǭ¦ǤмҞʹ\x91ʩ\x99Л´ѮɠӚ',
                    'arguments': [
                            {
                                        'name': 'ЁĤǋĊ¤ϗ\x8eӭ˻҈ОǔҩФvńƇǥЈҏ\x8aƬҰ˖]ǈсǪίç',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1051255928045664821,
                                                    },
                                    },
                            {
                                        'name': 'Ǳħ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            671699104810000669,
                                                                            5586278464903574812,
                                                                            4387053246494483928,
                                                                            523051327815206373,
                                                                            262678211739765147,
                                                                            -5859327547968038656,
                                                                            -5761811414547602726,
                                                                            -718007713157339965,
                                                                            2935338959316402930,
                                                                            -6487849128540670666,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʏҹĴƲѡҰȭ˺ГΊō˖ɚǪƱº΅ĖέйĒǢƵRхąùżȳħ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165138.593422:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ΆǁԜqȣӷĥΏў¸£ʢǋŒǑpǀ¬ӧɔİ·ƠȇƍǩҺƤӜʪ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 392327.1119599,
                                                    },
                                    },
                            {
                                        'name': 'ɾѓʫ˂ÚρåŮ(ÞţρO¾¢Ŝ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5450048797690435630,
                                                                            -1774230335325237128,
                                                                            -5720433943726992485,
                                                                            -6909141516428664705,
                                                                            3287176970410547847,
                                                                            190675915385888268,
                                                                            4026235930930072530,
                                                                            3168908414881684701,
                                                                            1074492169809672810,
                                                                            -8240292493986678496,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҍ¿ˉȇέҊɦǐΑҳmӇŠɱĦAʵˎŰǣ³ΟȣȽīϱʭɏάԖ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8035995686956410627,
                                                                            -4426445349253968971,
                                                                            5607070330600226514,
                                                                            442162055234573489,
                                                                            -6518851982926033952,
                                                                            6044684033580431283,
                                                                            -7557755725113325587,
                                                                            6275982093573472155,
                                                                            -1496925136788683141,
                                                                            5529368973054287295,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѺʃͶĆЇ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 721307.7317830716,
                                                    },
                                    },
                            {
                                        'name': 'LWѰԗϑ˙ǠĀ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            947725.1157366708,
                                                                            -71994.82629150353,
                                                                            688746.2956915395,
                                                                            626089.9455487368,
                                                                            70041.7310256933,
                                                                            504991.73308970185,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѶƃɈ\u0380˫ɞąʰŸǜǷΩŠʚÖϟГıȋΦư',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ęϻ²\x98϶ɪ͵Ӥ˝ǲºȸ͵˓ѣĢɐĄƧɚЦƯʺ\x84ˎʛӣȟΗß',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165139.971323:+0000',
                                                                            '20210302:165139.992668:+0000',
                                                                            '20210302:165140.012889:+0000',
                                                                            '20210302:165140.034201:+0000',
                                                                            '20210302:165140.056619:+0000',
                                                                            '20210302:165140.078270:+0000',
                                                                            '20210302:165140.100137:+0000',
                                                                            '20210302:165140.121743:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˼ЃѰWχOɘЁŹ˦GǓƣσĲϡӶΔ҉\u038béѺ\x8bvĎκӻƣʧÙ',
                    'message': 'ëá¼ȴ˅^η«\u03a2Ă˚ȿɑˇ˜ĆЧ¦\x81ϽȘʨЮʿΩŵŕǰȿК',
                    'arguments': [
                            {
                                        'name': '˜ήςѽЊ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'żϬUĘΝǞÇYѭҰКΒoəԠūŁЛƭ\x87Ũ\x9dƇЉ¦ɮɲÇĆƳ',
                                                                            '/©я\x82²ÏéňӠŮʏÿ]қέſљ҄ěǞɺ\x9f˶ʻƽdʲçɐѝ',
                                                                            'Ҥ«їóӠɎȒʪϞȕЇùćŷÛ˃˩źΑɠ¹¹Ԥѱ¾\u0379Šσдm',
                                                                            'ЅŊѴǙёsɃҐƸƵϚƼȎѮ\u0383҉êʔʀϤӨǁʋѷĕȹʾĈ{Þ',
                                                                            'όļԃĨˉсōΩИȟЛȐӾěμϝQˉ˅҄ɑ²Ŧǥ^ɪԫǸ\xa0щ',
                                                                            'ӃҳēʏъňΧīċȔРӗΞ\x96Ǻ˻ȎǞӈЅέ\u03a2 \x90ǹʸy˃ӃѬ',
                                                                            'ȧШīǺӶѵj©ğĝԁњȜ϶ɓҦʙǋ\x9eҚ"ƈɓ`ƇӖ_ʸŻ˥',
                                                                            'йЎɫìʞ¨ȲӡӤ~ƭϨ¤Ȓ˥\x8bͷʁƳҤҟˡӇƹǌ¿ҿ<ãƯ',
                                                                            'ЈİrŚÂδԋҟЬĽ§ӟ\x81˨ǦƖ¡ɐΆўħÓбʉŖʅӷÇʧŐ',
                                                                            'ǭπʦόdӤҳҥѿӞґԅЅӵÏ\x90ʋкǧКŵϣήŭѰһ˭ԖŘư',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÛˇǗӭÐǓЅӪ\x83ˌЭƦÒӻĈÔ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 271208.01832114963,
                                                    },
                                    },
                            {
                                        'name': 'ˢ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǛξϮҸҴƠԔΈԇʚɊͿΨʊ®ǆѹƹɁΧƻ˽ɍԟɸŚӅҟ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
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
                                        'name': 'ƲǞѡӲɫɰԅԉÉɋ˻Ίҋȁ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ƶ2ˋ\x90ĉÌȫɰɰϘǡȜҝҏξʏƄÀя4ȠѽlɥϠǔƆώӪĚ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2198333633882441739,
                                                                            6468917614425406511,
                                                                            -6850471864133747100,
                                                                            -99839367536859455,
                                                                            2616656684212758446,
                                                                            1536705330525732177,
                                                                            -2964984736741472625,
                                                                            7227483495524695389,
                                                                            -447425898497720399,
                                                                            -251556662393988002,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɭ\u038d1ľĵԌɆàȚ\x94ò\x88=\u0379ʳԑҿĖʫäϟɪʖаȸÒȥ-ƈʔ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 591168.0859431594,
                                                    },
                                    },
                            {
                                        'name': 'ƁÄ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 685081.8319088104,
                                                    },
                                    },
                            {
                                        'name': 'ҎШΓЇyĭʛЛ˱˺ˍʃ\x9eğԍʠ±ҟÛ·ŽĹОʗюʴWȍõу',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 246509.45403511147,
                                                    },
                                    },
                            {
                                        'name': 'ȵǻӯǎǩnûΫѷȾћʠƙ\u0381\\ȼ҉jӣʖ˲¿μӔԀϰϿɗЮɒ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8208590260876996375,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '¬όɓǝ˛ĐşпҟǅȟáʘĆgϧӛɽű˺ĿҧÓϨŝщUΈ@Ā',
                    'message': '˃Η-ϸϣӇǗȯſґĕxӹ˽NƳҒѺưЎðДʢԋŅϓЦͱn\u0383',
                    'arguments': [
                            {
                                        'name': 'ЧʥϘўӕǕʗӟѤϠЇ½ёԩäǯѕːĪƟŉϊϲӥϧʃšĕˎҹ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӷ\x8fƠӤҲ\u0380ΚϯϣϒˀĆҥɱɓʋXyŃԆȿŰ¨ϖ[ɻŠʀĬл',
                                                    },
                                    },
                            {
                                        'name': 'һƣļq«ѵ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6183325375355368804,
                                                    },
                                    },
                            {
                                        'name': 'Ǒŷ;˄ňŬŚȶȟŕԚ¯ȯ\u0378hѬØ£˛ʗxɂԙɉԏJȲĩ\x9eԦ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6433308901843410855,
                                                                            -6134765496938765059,
                                                                            -115184664999691084,
                                                                            3900670305560678877,
                                                                            -7372178371487237074,
                                                                            1615628882770514277,
                                                                            -206655254881830608,
                                                                            -7565322392081383701,
                                                                            -6667508776622914444,
                                                                            1551694086660675793,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȀɹԛeԎǪӫ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҬʰѤ&ы!ɬĮѯ\u038bлŀϘȜђȥţƹϤEȑд҇ˈҥǷ҉Aк¡',
                                                    },
                                    },
                            {
                                        'name': 'ƕǢȩæƸϟčˇ˅Ђʡ˘ğԑҫѥÜǲǲ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 750302.6453981637,
                                                    },
                                    },
                            {
                                        'name': 'ƏѢɬ ӏ2Ӱ|ŶԚвPȖɅɳ³ϝŧёҕɉҍӫ¤нєȇ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѧϟʍʔΒԋϼĭύԘȍΆŘˡԏϛíМОùūӠÛƢ\x8cɂԭ\u038dˍž',
                                                                            'ίϼʍƇ¦ыСіÇ]ϠƈʁƢ=Ӽɧō\x98Ȉ¹\u038bңʩ\x87ʎʭԥ˗\x86',
                                                                            'Ѿò҄˩ù¢ǳǧΓȕĮΈȂʱϯѭ˄ĹӣɉҠԅήʳʯөґѥƱŀ',
                                                                            'ȉԙǉĆ©¦іԍǆѦΨͳľđԠʷ\x91ɭёȓҫČЃщʸӝɴƊ÷ɀ',
                                                                            'Ɍ°ɫƮʶ˸ӰΎǩҊ»ëԧ˛\u0378ʌ˽ɾĐԫơԌʟǏџ1ϥҭȺì',
                                                                            'ŐίζҿȔ»ɨ˘ʪĐġǅͰľϋʕWȚɏ\x86˩ȭь\u03a2ęȪʎÔϳÀ',
                                                                            'ϼȳƵŶʮɎʱş¹ӕЍңȐȂЩԒӜЛϷԅãīѾˆȷ҈јϭǇl',
                                                                            'ҊϑÑėҼȎ|ѠÿǇЋ\x84ŎÆȄѪƈ΄ɒƾԃǵłћxΤМŋΒȗ',
                                                                            'ƛɿ¸ýˡŝ˦ӚҎәыʾϚʶyҶ\x9eƬȼϢ¨ƃčъȥ¡ªχȌϢ',
                                                                            'ȬǊԂԧȎ¾ʭӉƌҳϢ9Ƨ\u0383ƁѼŕʑŢøѐ˙âв]ˍҶʋƍʸ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ңIӪêɍωЀѽТϫɌɨÝNѐ{ҁˏƶҏͽŶЊ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˬʤВѝ}ɺͱХ˓ͰĳhbÌȔ>Ρґ˹ʽĵ˻ԭԌЍʉȑŬ=y',
                                                    },
                                    },
                            {
                                        'name': 'hҺ8ӲɔҡǰǏԢÝϖ\x88ΠΒđϢϣɍ;ɸóňȈǙΉœˌȬЩȝ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7080346181082399770,
                                                                            -1756682570578012209,
                                                                            -1825838020352826545,
                                                                            7664483958255911789,
                                                                            -8665872501765992788,
                                                                            -6766804403169867916,
                                                                            -7246813995256322354,
                                                                            9087675709976853192,
                                                                            4844170616237540892,
                                                                            5183547461237037245,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɼʵɔhɳү¿ϯɤǇƁβԒ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ªҰǲ˃Q·ѮЪȃuʥŴҰϹѨˋƍЬɢǮ²ŗɛϻά҇ԖђӆӪ',
                                                                            'ÛмΨԐ\x9dўϺȸãГԉŋȮ\u0383ʉӬßȒśсұ4ҭ×њʹʤʔƎͱ',
                                                                            'ƗӌљѫƆŅ˸ȮбмβЛϪ;ŲЊãӤƘ%m\x91¢Ė0Ǚ\x8bƣǹž',
                                                                            'ԌƝϖȹԤ\u0378ҕȎ*g÷ϖҩӐjȷɠЉʸʙſ±ɡ˨ǥȉ҇Ϊǳӟ',
                                                                            "łҟƥ;³#Ҭԍǂʎ7ÔÛǾъȋЯÍǩOīĤșõӔĻ'ЋƦ¿",
                                                                            'цʒβєŋʦѺȵ©Ð\u0383βѾ˫ϧӍæʀϲζŭŕƯґ{ӍȣˍȌn',
                                                                            'ԡĬӦҎДƉάϑғǈɁÎԪχԓηĥЂԝ҃ϼƀҚ˭ĺ\u038dƔ\x9aʏԂ',
                                                                            'ʷɒŨӨӞċĜ\x8bƎǂϱєó¢ұшиŪԑзĵ˯ЛƒĲȗʣ˓nń',
                                                                            'ӤŶô¤ԌҜǀį<yɉ©ƺdνɀΏϕҸ҇Ŗ\xa0ѓҙ@Ќÿΐ\x8bɆ',
                                                                            'ӜȂȥ9;ѭϭŖȒƸʢĎҚ-ұfˑƓ˳Ɉ\x9f[]ɖϦƠļǬğĞ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '8ʂìÈǈʻѳʴʖŞġǧ\x8bӧ\x90ǕɣɲˈѢ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'đԃÁΉʬκǇƆŶύȪŝȬołɫţɂ\x98ɌaßȔǐԎȴԏSľȧ',
                                                                            'ǢǍǪǰhyōуƂК˶˵ˇȱŖóʬɊˇƏɵυŃŇӘϑѱьˇȭ',
                                                                            'ȗǄ˫¯UâƜĀʰ˗βёÎƁƐɧʎҟΔЫɎiЧбĊǚƀʾɅ¨',
                                                                            '\x8cΪôɝĦЛӃ=hχŅѓхȰұÞÈ4\x87ҲkƫưÀԆ½үϑΑę',
                                                                            'œĉŖƻӫϒÈΣӔњͽӖʡΐгԟ¥ȍԂĻʺ˽ВɓkƂҸ\x84˴}',
                                                                            "ЙʆɌǐˢSҠȳϏΡ˨ҧģЮѲ\x8bςԓɊӏ;ēΝ'Έϓȉ˪˯Ł",
                                                                            'Ȑ3ǟǰ\x8f˷\u0381ǉx˙ϘkɵÓпπƘԧӬұĉǀ\u0382ǵӚ˶\x9bƿ¥ç',
                                                                            'ӊԬιɰΉˢȍҍуƓȪӞȀҖ\x8d(ЃϛԁĀӝoXÿƮԠŁЁʀғ',
                                                                            'Ï˜žĥѪΆw\u038díġ8ӷΠýЗTȴʥ(˘JΊ\x91цӮɾJɤѦĉ',
                                                                            'ϖˮϿʹѓƯ˒їÇо"Įӫ΄ļԭ˺ӑρόʱ\x92ǐȗηĠěżƆɫ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˓ӟЕԛѶɰĿ2Ĭ\x92ѯѠɨĎª',
                    'message': 'ԕѻͽʓίɖâRɷ+UȓȝĒ\x83Ŷˇ\x8dӸҞҘˁǁҚҦMɾӷЍф',
                    'arguments': [
                            {
                                        'name': 'ʜǠǹДǡƔѡɄʉƶǕԖӷɍF©Ť',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': 'ŸǄȇƙÅӃɱǽПҵĐӓӚʄŇČÀ\x81JҤÇАǲу',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165144.792476:+0000',
                                                                            '20210302:165144.813172:+0000',
                                                                            '20210302:165144.834844:+0000',
                                                                            '20210302:165144.855925:+0000',
                                                                            '20210302:165144.876512:+0000',
                                                                            '20210302:165144.900393:+0000',
                                                                            '20210302:165144.921367:+0000',
                                                                            '20210302:165144.943032:+0000',
                                                                            '20210302:165144.964077:+0000',
                                                                            '20210302:165144.985439:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϐоǑǫʗҿı\x93ʺˆӝͽÓȨîʒǜƢǉʰ˒ДÉȇj!ɬǩǳ?',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2505212532509375443,
                                                                            3879646291764789913,
                                                                            4774449261537711249,
                                                                            1106007310419297894,
                                                                            9181151528480953215,
                                                                            -9186892716946821745,
                                                                            7812182915305917709,
                                                                            -1906306357830261204,
                                                                            -6239804988750035650,
                                                                            6695154709841729132,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "2ĺ'ӺҨw\xadʪҤ˭ɜfӘцʅȿĎ",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7205451688806538900,
                                                                            -1183644201430829418,
                                                                            -2072086404133413399,
                                                                            -5380379312800433266,
                                                                            724240965099721894,
                                                                            5682477863761330897,
                                                                            3714534470883384481,
                                                                            545138142060507381,
                                                                            2400917512446795389,
                                                                            -1139895479479782415,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˝ƌҨͿȌWŻȩȒӞҎĴƺТπɽЅ\x84ʕΌÂșȈӾʑлɬȯǃɞ',
                                        'value': {
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Òʔþʽϯʠ-qϼʚę',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165146.168695:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĔʣϘƮΚȭѵ~ǐʹįƖïʮÅ3ĆǿӟуԥӔēCɱƨӖ˸',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165146.261034:+0000',
                                                    },
                                    },
                            {
                                        'name': 'āȸ¸\x8fʢǌ˾ØӕĎӓϵ\x82kʂΊ®ưȥÙυƶбȠпȍͼͷĿ\x88',
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
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԀĔϔİϒμ¾ƱĆ)ǃ¸˜ʜʗʛǍʱ®Ȼî',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѡħҠǭɍʙωÉʁÏʱϔˋĢƮȥҘʰʖȄǧϔǔӫëǷº˙ҎΙ',
                                                    },
                                    },
                            {
                                        'name': 'ȭȟqɚʫʏ\x8eɬƕ4ђǙƯӚ˾\x9dłΌξƨŇǓѫʿɓɀčŠǮɭ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            905180.7282468036,
                                                                            777889.6616320987,
                                                                            913437.9116589878,
                                                                            891178.9623442229,
                                                                            688884.5021416537,
                                                                            133083.17570975504,
                                                                            741431.5682554296,
                                                                            481791.9332005052,
                                                                            5560.948468287126,
                                                                            126282.93355888265,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'fσʢ0\x9e÷éǎ¨ѢѓȚʌ\u0379ЗӆӏȑÈǢɾȤѮĭϙˁӜϷΞм',
                    'message': 'ŖɐeŲη҄˝ѩҋӘ/ϖӢҬɩȡ£ź\x9cҽυЇνϻԓΒӃҹȣȯ',
                    'arguments': [
                            {
                                        'name': 'ѶǅәǣǙӎ\x84ɹɂ͵ƗRȝѧãϬҀȌʷΒǙθχÀӥԑƩАǊª',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ӱ;ħпɔÌԓǊ-ªҋиȘæƈ\x83ԛʘėȍ\x93ˣțÆBҠθӏǛƣ',
                                                                            'Τ˜πэȊѕř˭ӾƿŀĭbɨӃaҨ\u0380ϤѪԥГϘˎɲƋUĻˍȋ',
                                                                            'ʃȾɮҞɿȰӢŌ˚·ƐŵǊƷұ%PɑӮҗƽHƙ(ƊGЛІļƗ',
                                                                            '·ɸ\x9fїбѧěћΡяûʠԧ9ϲɤâxӨԛȡ?Èʘү%ǎАǰˌ',
                                                                            'ѡƶƕАʊǿƩȺ\x81ɲ҂ϓʫ\u0378I\u03a2ҀЗҒҺɻȰΠǀˉǊŻЙāļ',
                                                                            'ʈыѴԛҐӬ\x8f\x99Ł\x97\x84ƹÇŘhγәFĈěġҼŃÑ˒ƂÆŐҰϝ',
                                                                            'äԂȚ\x88!˷MδǊи\x7fǖΔʨξʣÏѺϏϑҭGǅîЃͺɶŬǊΖ',
                                                                            '\u0378Ό˔єƜƘͷϊ˵ӯɗőыԌӷƞӒщŲВҋ.ˊϝƨΣǆ;ɊѼ',
                                                                            'ϝФ¯ďÅЀӟɤѷĊś´ƌʃȄϊ=ѱҬԄĠ\x9c˖˽Ǵʭǭuŕm',
                                                                            '\x97ϯpɬɜ˺ŬϤɘ\u0381ÎгʿҢóļĭ\u0379ʭ\x95я¨h҄ÃƜӋУϩ\u0382',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'xɍƤȶīђ˱ʌѸǋǆüΛ˜¾ϖũΐŊʥΫǳĺηĊʒ¤ȼˮđ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210302:165147.204542:+0000',
                                                                            '20210302:165147.222945:+0000',
                                                                            '20210302:165147.241217:+0000',
                                                                            '20210302:165147.261365:+0000',
                                                                            '20210302:165147.278711:+0000',
                                                                            '20210302:165147.296511:+0000',
                                                                            '20210302:165147.315261:+0000',
                                                                            '20210302:165147.334856:+0000',
                                                                            '20210302:165147.354614:+0000',
                                                                            '20210302:165147.375817:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\xadÇ҆ýǳΚƝ˘ĄŏЁƂϓɽѦÄŕhªŸԫɢцţӄАǀģǴТ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                                        'name': 'ѕӖΈ¡',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210302:165147.738796:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĪKҕԍҳǓɸԒ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƚęӅҼʂӊſʻÃӝˍĕѢƓiėƊɷŕύX(ҷʜϡ\x90ΥǁěϬ',
                                                    },
                                    },
                            {
                                        'name': 'À˫҂ԌÕɺԟ[ϯVāζȲ˜Șԑӯ˟ġΈˮǀ±љ\u0383ſŜ¡Ƅψ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '²җͼБԒЛȀȔǯˡ¼ƥǺψԠŰӁϽ©ˮ˨ӂǔ[ϫǗЏǫ\x85&',
                                                    },
                                    },
                            {
                                        'name': 'oѿɀԇѲąèȳνӡÏUζ˷˕ҼМϦԅҷȍѣ#\x7fǩԣǣ˴ЏЬ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'NdԩԂˤ"ǥчϫякԊǥͲFɘɞńȑӎ˰ˀҨǱЛЂϧЌtʫ',
                                                    },
                                    },
                            {
                                        'name': 'ѵыjǮDɲʡϙ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϬȮӈ¿Ѿʆ˗ƎtӘԀ˾ҐӞǮңʐ(đΓȖ2Єrѿ˩\x87&ɽʯ',
                                                                            'ŃȹƺƍҋɤɐϠɊʐлʮɎӭŌәǐӊÂĘԖĀéіǎѶϢΖȇ_',
                                                                            'ƭӁFƻǆȌȌŞʝӕ˫ÏʝԀɝ\x9a҆Ǫɿ\x9fӐ˩ĕɪԛѰʵ5ԅӆ',
                                                                            'ė˹қӊЭϦИƑÓėȐѰѶkʤɊ¿ӰэʛÇȐˊßɨѵ˟ĴĂō',
                                                                            'ӪƢxʂżǛˎԬ?ͲΔəɭ˛ϋԚʫ\u0382ȟÏ#ɬңɛԕxƧwϽk',
                                                                            'ώȪıǨұѝɀε˻ȬҔĶατǫԈϿĤɌϿɪˣӆѕԘǒ´ǻȮ:',
                                                                            'Ͷ%ǻæˇȮÒɜÖӃӁɉʹ˂ѧƌƫҼƳѐȆϽϑǢвϒƐӘƪä',
                                                                            'ЋɁϣȨќǸȹŃǬФǼǲğşмǂʑʂȳʼ˧ȒěJΌ·MΊʿ±',
                                                                            'ɥñɂӗǖęϾџȩ\x998ϒґʒͺ\x96ƥџƨǭάтϭHȊԈӼϯĘƓ',
                                                                            'ӁɜǂǛȯĩрȳǮӳ\x88Ҡʰƥɓ˂ơȍӧΐƟʢǀ·ħœΑӆ%£',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˜ѺӊɕǶоȶӬϔ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 771873.6797676682,
                                                    },
                                    },
                            {
                                        'name': 'Ć\x8dҗџńβbÉygƆʡɂғ_şHɰќѶуηɨӸ¼',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            356603.01947501826,
                                                                            443457.3003038631,
                                                                            345306.84658813133,
                                                                            637445.4140357384,
                                                                            889969.1121649212,
                                                                            378288.308595987,
                                                                            190740.09645676974,
                                                                            957423.2081511973,
                                                                            252289.6216458305,
                                                                            927237.4759430499,
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

            'identifier': 'ȶɥʰ2Õ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'ēń',
                    'message': 'ą',
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
            'name': '͵ňwőԓ˲ơ\x82ѨΝБɣƜʜќßдɻȿǂɤ\u0380šjΑ\x97ɟĭӑ˚',
            'error': {
                'identifier': 'ͺвӻ\x80ą!ȠаԒҹтÕНșΌС˞оѻǟХԭҦЇѶÛόȨӢ˗',
                'categories': [
                    'internal',
                    'access-restriction',
                    'access-restriction',
                    'os',
                    'file',
                    'internal',
                    'os',
                    'configuration',
                    'os',
                    'file',
                ],
                'source': 'ԫҸӕɦҾ\x85ĮlȱӇƙĩŔƷ_Β\u038dơʩɏԕ˭ЌǨΛΰę˄mȰ',
                'messages': [
                    {
                            'catalog': 'ʯǫöɗõґщ×ƪЖжǨ˰ǓԚ\xadΒЇαƶìұŨéΌІԑɑʩу',
                            'message': 'àгχʬɺĸҐŧɴ¤ŸϟҁНĭѫ.ɼȨʿɤõʨǡ6ʄȜӯϧç',
                            'arguments': [
                                        {
                                                        'name': 'ԪТҸʫǲҨ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 78249.78580671104,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʐďʢôĮ\x8fu2ǎ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165119.622277:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': "кԝѷЭӁÙƛɣöͰΣX˟'ґƞȿÿ˸˦ҿɣưɊrԠԋЃ\x94ϊ",
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 196784.25564787484,
                                                                        },
                                                    },
                                        {
                                                        'name': 'вχԂЉ\x8bƐнѠ\\υ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ľɪȝԡƂʜŭơ\u0382ΎϾ˩ҸνѺԍɍʓΜˣýȣ\x93ɏĭӥɃʱ\x87Ѿ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ù¶ΎҳϬĳGͼǙВȘ˖ϺǟĦ§ƢȄ˺υˆɭѫв±',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʜǡǛWŨĐYҋҨĹͺɵ˃Ђƍ8ʮɤˆųŮъŤӝ®ӒɨĦšЪ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɣʛƯ`˟ϴûʥ³Ìǹ\x92ιψ͵ву8ʜeәԨ\u038dЗ\x93і˶šǠ\x8d',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165119.945427:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʹ\x90\x8cΰ_ӏěĘҊ˯ãɍʄOȝɀ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʷǅœ˫Þ/ŶԉJҮЈʅgЖ¥ƄƌСš\u0380œϗԪƥʾиŊŉƸ\x8c',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӄǌǙŦː˺íʏҫʕѳõŹЫǹϲҌϳ*Ć&ɳΡǡK˨ŋ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȈΓŎÑϧʂɗδ´ϒPIƭˇԦJ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӎŉ9ϾÉҧȓǳʽмʓOɞBƹϤӿ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7314220243376506120,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '¨ϮѻȖ\x8cѨȨsӥҗҹѠԝΦʋӔȟѱ\x81ȓÜЉ˴*Ǭɶв\x8aѺϰ',
                            'message': 'ïēϷɛfФΈ9Ö˳īƼīпԕű\x94˷ʈƃƥϥ˹Ǹԁкΐ\x86·Э',
                            'arguments': [
                                        {
                                                        'name': 'ļǴѼЯŧ»ȓÎťљƻͶǔǉŷӂÍиĈ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʦўξÛˏöɢϗƱ·Ǯ.ĀŜȃџҹħƘΡ±Ǉ\x9aĚMζώȃʭɊ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'SǪҷМìʊїɪɬўф.ϧ͵¿ŨŹϘ\x7fԊʵʠԃǱӞˆû',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -615711102722140637,
                                                                        },
                                                    },
                                        {
                                                        'name': '˦ĞĳҋĒҦŽʢɿȡά^ȹ\x8bҏӐL\x97',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165120.653299:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǮʩλҍMͶáԤMɮżԥӢPѫ˽Ы\x87ɩDͼKģ˄҉оŀȂˍХ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҠЂ®ƲʦǷ¢ФĊƟҀˬèǣßf',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʍԥҫwʂHԜìɏ\\*δӀɀɠǶDϏïϏţγėǐӁ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΥπӋЗήåɛʂǻϪéĳОtƎʸ\xadȻ3Ԇɔͻ˘ȪˉӀǿ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϧ\x9cŪ¾ѽâēәԣƤɕɹáѕφϚчѸ˽ǗҬù\u0382ƙ:ˤɈȋ\x97ɝ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҼȴФӇĂЩŶʢЍԭϣҠӡ0åӆȐҰ˃дȄƭ\x84ƨŘˠȮѐǯ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȰũψȹÏ˷ēˈѲҲƪ˦ŋénÉȘӶƍŷ|\x95Γȭ˫ÄƮΉȕƺ',
                            'message': 'йɕŷ\x80ТωѸϗȎɭˀƏӴŨʮєѫɖǥɰҍǌɒtϊӫО¾¨Ӌ',
                            'arguments': [
                                        {
                                                        'name': 'ɨ$ƝÅ˻ȩőȲ`Ȇһρ\\Ũ˦ʹ6ѕɣ˧ʶ4Τ%˺Ģʊ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6630759370672850461,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԃ҃ӹȤɔΩʨѵһʈǨ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϔʶAĢ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5025034143755962817,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΫҁˆĠÔȫÕ˷ҋƊԩӛƀњxǪԚСˏȷȌȯĖʠӲǅùŞɫ$',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165121.562336:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '};˂ҵĘȉΌʀґ\x9dɔµ±ŸɚǌΎ\u0378)ɄǍœӂı¸ΕɆǴɝѐ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƽ9ʱåЫÂӨҨѴ\u0379cӍƵ3ȁʴйԁʩ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3952142093066201973,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϐçҭЮǤӟԘĖΜȝһɢɪ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǠÚϽΎϬƴдýƼаʕсԏʡŧț¾ǟԤоϲӎĆ҇ʍőǣŰªM',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƄǟћʾΑӹ¶ɘ˜Ķϰ&˚δӒԋŌͻӰ˥ɫÂϵşӀМЇ<ȷ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѷыϧЭ˭aïΏFӕǇǴ\x9dɝԚԉvʐōɆӾřǕάкǥαЕǆё',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ăΌŮf\x94ʛ҇ÆȿʺÉ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 37183.23394164827,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'žϣ2ǙːϏȐ®ã®ǄФεſѡ˄εϖ˴ʂȍϮШрηRӵӭ8ƈ',
                            'message': 'ŊԊƲɪ˗ʦϐɇлӖʛˡΉʵ˸҃ȽЄØʝ\u0380mϐʹъϾȆ"ǤɆ',
                            'arguments': [
                                        {
                                                        'name': 'Ťǜ҅ɓÐ¥ѝyċ҂Mӿ˷ԀчǫƼ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6029794528850726047,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ТɔǛȘѯȨ˨ԉþėɌΣʰƝԟӦȎǄ\x81АȷӳԅȘ҈ųǬǔƑΡ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƬдĶʇΞǂԐҷϮ>ƤӸԇĞ\x94ϗʵӽԍȢʝŁª˛ǺҦ»Мjþ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165122.326217:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '³Ѯзˇӌνοůȳ˙Ь',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˔ŒΖƨТűЍǵoǥ˘ǲԈĽԦƮҽǧBŃ\x92ӞЇͳͺӂèжdÉ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӊҪǶĲǹʿˁÆǋǃЃș\x82ːΑʥ˂δǑȴşћÝɐ_ʙɋÀԧѫ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҊƆà)½¿ϼƷƳŷźƽ&ԁӦΖӝåˉĕѤȞϐɘ&ԛƴҘ\x94*',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -30617.471897392417,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҜɁ;ÊôԣȡþάЕе˻Ē³ʸ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'čѢ˞ˋӾ˖;ԒġİʄƾнωʂѰ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŤŝђȌԙˢʇЈâʋĨӘГǐԇΊĒ\x80Ѡм\x80иӿ\u0381ȏĜ»\\˔š',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÛӁÝҜϥѕĵąиƔӯ_˘Ԗʿ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΨϦϭļЁˈΉ\x80ǡїƆϠѓǰǰЀ˻\x89ȀʤȹɖɆԩčѝˋȚΖʝ',
                            'message': 'ҼǼϪ`³ǬƠ˄ʾӴʃ˷ʜȷFċ\x81ˠɺÝӾжȔϤԙƸȎǉȻѻ',
                            'arguments': [
                                        {
                                                        'name': 'Ӟ\u038bǚʻƚȚī˕Ǵ¡ξĜВǭƘǬŽɳϪãνªǁÁȱʹ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4554968023986604990,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʐÖƠθÏəɄϐɨҏ˨ĽʶȱɪˊˀЀō®ǪӤ"¹ȒÚȒ\x97ѴҤ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5064484148764326727,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˈ)ӫҕȡѭƟ˟\x8abǃŸŌ\x95ͺϭȖЌцȦʕЁűıΞǢ˪ѰОɝ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΒɾƊʏ&ӞʻʤҫɈƈмԌɒˊdÿğȹʎϟ#ȝʉ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165123.433893:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŠŽ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ͺ=Є˺ũ˴ñԛЭʿˡǖŔԃϘӆȖĞƅʂѻӊ'ҼˇƮǆŮʔţ",
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҮƟƬɁɻίԜԄљʣ[ϘϥτɔрɓǢĮˈˉІяȑϑΒϚjҳϮ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŏʃļɐǥ\x8e\u0381',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'έɃE%ȌĭьǾ\x93¶ӉěĲŖԈLƶϊMŀŲ˶Ʈ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ͳ˾ɷԖǼͺήΞϯĥµӀͶƼ˓ǳһo\x94ͼυǩʧϖϼÌFϥЌǡ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Џ}ΌƂЋѦó1LƲϿ˔щʦзӿǅ\x97ê¼ɒ\x9c\x90ƄȎκ#ŃŇȝ',
                            'message': 'ʤр©ӜНƭɃ"ψÕʫ°ȨӰҵ`ΪƟΖ\u0383ɬсØŧǤԁΑ"Цȁ',
                            'arguments': [
                                    ],
                        },
                    {
                            'catalog': 'ΰƭƾ0ʵџƑѾӬ]ΠCзɗԉҵѓЅуǺҮȮʯˬ\x94ЩϤ\xa0ª˓',
                            'message': 'ОǷФ·:˝ϯњɝɵɉӗrѥİÈŢѳԊŰ\x95μФЪȫɟѭ"mǏ',
                            'arguments': [
                                        {
                                                        'name': 'ȖΜƬʋԆǎĒ·ҡӶǌҝùӂ\x84\\ŬƩĝɼѯJʶұÿȷϸҶ\u0380ʃ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'зԓŵȆч',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "í҂ȨɘůȟɡА'¿ԭʡɌӷ˒өŢњķɌʡΌȵʪ",
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': "ʺǺíŪǽm˱'Ӯ˖",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĜǄúЍΔωўŘ\x80ɏħŜҍɻȴƒфȺ˪ȥ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǺӺȔąДϯû(ӏë΄҇M\x91ˎыďİщĲχҷΝϐȣ²ˋɊvԔ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3834246401564369730,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ł˃ǄӱҽŨȭȲɟ϶ʉI˜КʊϬΊˀĤ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӬǜҡғʮӨɘŐɟΕѽίČĽ\x98ʹǒԭˠȩ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǯƥһҕӠåιŰҾóԦĹ˖ȵϐʦ²ŭ\\\x82ĮҿŨƸ͵є',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǢΞãҔыѿ\u038b',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '#ҁǙʅѪƴ\x86ÛΑ˜ňϜƒĵě»ȕέUζʬʱȉnΞ0üǰӠҪ',
                            'message': 'ʏҺңǢòћʂ$«ʮӝΌжĊǪѮϛġ°]qρϏTɔȉȅӠпς',
                            'arguments': [
                                        {
                                                        'name': '΄рĔάҋҖ»ƫЙmɲʊȍԘӜĢΈгäϽϣʧʫĸˏ˫ãҘԟȯ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȗфѩȓѶЄǓԓъHґƅсãʍӭǭԝʖӼ³\x93ČҚƘ$$þâƯ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'AΚϹ˖їЬҏ˨ӄ\x9dϺßТЬåԉ¬ўőϦŵ\u0381ÅӿТЖ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĝЊ ЕęʤЖj\u0378˅ґwĨĜȲсťɳҕ\x9bШ¾ƈƗӉчυχϾũ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7234949611486733667,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ąž@˺ȶԪӸΚȾɂBlίɲӋġέƫ\x8fŮϘ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӏƀ]ͿӰŬìø·pʵѻԍāҗӺӃщΩΡŞʪʷʤZďÌϗӫƞ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165125.621696:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӌrɧΓВǽϭȽМʰů\x8aΜδȢĘ+˓ǥțІ˖n\x9cɲ˂ԓǇzǂ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165125.706033:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѻ˱kɦGͻԥFȺҐŒϦʩԟӺ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9c:чЂńԖӿȲģēЀkʒҏʡ˒ ƆНüӜΥȂƵ¾˶ɶ˝',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 672452.2549300913,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΗɨˁěÝϟŗƺ"ӱʘͿɞįǪϕаʎoӷ˗Ë',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165125.993920:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ĆĠϥäf±ɮѱ˂ԭTxɻ_ҖȆу\x98ĄλǾºҴ˛ͼԄŚłҡƭ',
                            'message': 'ǏƸė˻ӇХ˂ΌRÇΒԮљCЗ\x84ľщöĸʻ¡ӓԬƺ˽ӡſ¶Ą',
                            'arguments': [
                                        {
                                                        'name': 'ɾŦПԍƁGfϷ\x9cЛβÆŨп^',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 891529185001792967,
                                                                        },
                                                    },
                                        {
                                                        'name': 'h\u0382Òȸ×џҩóǡʐ\xadζЍӶʢRΣҏƧҪϺĄźȓ+Ǹ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 607197.2712142701,
                                                                        },
                                                    },
                                        {
                                                        'name': '^ÕJъǄґėщɮД\u0382ԂˬϤҡошʆΥĔƂĀɷŁýþϐÐѶ"',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǝ`ɊϣXҡϏɺȲɍѬǡӝНåŶҎɥɰʽŧǖϬċ]Ϧ˙ǳʀʠ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӋʂƶʣԄΊΒ°Қuƣ¹Ȓ˶ԍłӹϽӑ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʕȬΟФǥϟìԄ2ƉƩĐЬʞĝ˻¦{ϹËŲˆƘƨȸąǙȜӃӛ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 3475.1033001152828,
                                                                        },
                                                    },
                                        {
                                                        'name': '»Ӕ²Ԥͼ^ŨӦǺҼǳɱȇÖΒҾ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 762822.9801971875,
                                                                        },
                                                    },
                                        {
                                                        'name': 'чεȅɦ҅ʞʘшāΫʹƩ˅^&Иʏѿũ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɟɡȕųˉ҄Д×ГrŽϾΉԙǦӃǠѝJў˙пΝƯů\x84żЕËȶ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǧɨд',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƇşWɝW˾ЗˤY&οƻˤҴͿȫ\u0380Ȋƶʓҹ\\ʻɒ-ìʝЎ\x93ǲ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϣ϶ǩǘ4eҙxǲǑ"Ȧ¿@ѹҿ\x86ў˛ǩʸ{ԇҞ©κөЖԪϱ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165127.037571:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ç˵ȵԭȈĤΒԟiЈ,Ź҇ϨǈǟԧЅԜѕѐʚĮпщğҙěͻƁ',
                            'message': "ţĜ'ЕŅԨΆÕɳӪˠǩ˙ȚήƩҾúϦǧĂƌɽĄʚʩұӺРƸ",
                            'arguments': [
                                        {
                                                        'name': 'Sԗѹ҈ơ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѽҴȘȈ˳ÓЈѠĵ©˭ʯʆӥʆѧɨ2ʐďƫʻÇҹĴǳўӑ\x80ł',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŽʈКɟŌĭŃԅġBƚŃѬ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԊǶФĬʀӯˇʭǫϪҜ͵˲ǍʥҳjJџąŒ˩ɒƄԁϊ\x90ǻ·Ũ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'зӴЩЙӵøíğȈãǟʫџưǎɻŤeҐ\x8bѪѓǹϮӉ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ОϺйҶȼӧɼ;ӥåƚȊʔ΄ưʎÕɑөˉ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210302:165127.586913:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˟Ҫ+ïіҔŉĐ1ѹːǁG?ŷĤΡ<ΘΚБ\u0383¶ЋΜʣΖ˅ԟӺ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʃʠɮ¥Ӧ<',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ж\x81\u0383ęÇjʭςюѧЕҤīkϝԔ˻ǌ˳ʒåńǦІ)ɴƈ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӡì"ÊұςԖł˘ÇϵǠą˒˩ǏɩËҫǝ½ϩьÀ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҝЉΠǽƻ\x80ϽÈɗӣɪЃҐ8Ԛɞ\\ҬњȀ˰Ź9Ȉ҆ʗģѹĸȔ',
                                                        'value': {
                                                                            '^': 'bool_list',
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

            'name': 'ӿǠӺ',

            'error': {
                'identifier': 'ɫɋʶãƷ',
                'categories': [
                    'network',
                ],
                'messages': [
                    {
                            'catalog': 'ƿԖ',
                            'message': '\x96',
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
            'event_id': 'ѰҢ\x84ӹʨΤƴˈͷͻτΗ˗Cԍ3ɛʹŕϻәҋɁˇǀ˹ÎȤȈ˟',
            'target_id': "ϥŹƕƥԚłӗʽώԢʈϹ=Ⱥɑ0\x88ˡğ˗ЪÇɴ'ƅZѾ{ζѠ",
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
                    'event_id': 'μͳҗ¢ԏ¼ƓϦʀ¤ɺʴќŦĨĈOʍӆğҿОBĐGŷŬЪƤΠ',
                    'target_id': 'ǫŅБȨɯԣķ¶ʓ҉ÀЏӎwơϥәǗѠǂɘ˖\x80Ͱ˾ѽÒĖƲı',
                },
                {
                    'event_id': 'ԐӀѶʩĭũΘśӻĴѧâƝ˅Ӣɇʥȉɲ\x86łųʮʈΏĎΛĞЌω',
                    'target_id': 'ѹŖʇԨɢυԡ>˘ˀΉĮɱýƵґ˷ЭӓHřÑԮhҫǸΘ҅ν\u0379',
                },
                {
                    'event_id': 'Я6˙ŚŸ˥ėĬćӾӔɐ\x9dƨƸğε˧ȡɨдЕƒͶ\x9dːʗҟԄД',
                    'target_id': 'Ћ˂źΠηӂЩˋ¹CԛЧϱ\x8eÀ\x95ˇ|ѦĖȥĔ\xa0ЗǰҞŠУGǰ',
                },
                {
                    'event_id': 'ʅå]ưМψfӑњƁɾӼȧZѰӼɊҡБ\x9dǒ3϶ӸҔͱŊȣΥ²',
                    'target_id': 'Ωƹϊ*ħȹɃҋ\xa0',
                },
                {
                    'event_id': 'ʢ\x99ӵϨɿϱӊӞāț˟P\x9bČȖʡɫȔʞΕӝӭʤɒƴсϤƭɧÀ',
                    'target_id': 'ҹҝщӜʢĽÃȻН(ͱ%ăʹɝɦ*ΰȑєɽ=ſȜƑԑҝԐ¬Ņ',
                },
                {
                    'event_id': 'ӔöέӪIĺϮЪo˭ƺÀԏĤ?ɢϒɤRЂĦİϣϽ¸эˋǱɛŮ',
                    'target_id': 'ɩ\x99њäɄ]ȕÎαǾɾ9\x8e҉Б\\ҭ\\ӨßԈƴǝӚɸʨǠΡĵƵ',
                },
                {
                    'event_id': 'p\u038d\x84˲ǼUɿǳ¢śh9ôȝӃԗΩԌ˧\u0383ƨϠÓȵЂԠǘΎĚų',
                    'target_id': 'ĮƸσ˸ďԄŤ\u03a2ʢҟ\x8dҝƲϠƱSƶ\u03a2ʲѥƿѥɗ҂ɇȞ˄қpȂ',
                },
                {
                    'event_id': '%ҒʤÃňĀƓɞĄԍƸфϊёʻĄǪŐғ\x8dÃҷӀӉԑˁŲҥє¡',
                    'target_id': 'ΈƘăƃҲӓÝщӍнιɸ9þ"ҙƚƍΜǦȎѢʮĲШЖƉӲƙҥ',
                },
                {
                    'event_id': 'ĢлłPҘϊ__ƤӏӷМҼѪϔ¸ĩäЯ£ϹǚɼΪ҄ȫȀʚҊ½',
                    'target_id': 'ġʈSƥа£ÕѧͷıŘ҅ǫӝҦΥʂƑNƺњeȸɅϔĖϘѶƢӱ',
                },
                {
                    'event_id': 'ŬɿѴӁ\x84\x98ʝѷҎȂΩôCɍʏϭıŌɅçϊԧǮ#ſɽӱΧČж',
                    'target_id': 'Ȓϻſ#·\u0383˥\x8a',
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
                    'event_id': 'ªѳlΥıǝюĽűдɭýμȿҋǖͻͶб˾ţpą\x81˕ˈƚԈˣȬ',
                    'target_id': 'ŪҨȾԞƛĄӽΊ<ИӛŽϫѰÝ˞сԪ°˧ʹŏƶқ)&+ućԙ',
                },
                {
                    'event_id': 'Λ\u0378õţфǘθi˭Ӝ°¶ɆћɽǢЊħԦӟȅПòʍ\u038dӓ\x8cCȿʝ',
                    'target_id': 'ӏѳǷǋϰŚӆ\x97џЪƉǲÜĶȗӵ͵ȇǚͿӗưͲ˾ϹëǑɯd\xa0',
                },
                {
                    'event_id': 'ҢΕȗλǾüϊϑԩǁȹѠçɱĳɲȜ˱ϫʬiѪȠψǲƷѴɉРȁ',
                    'target_id': 'ӔĸːқȅҍҚɯӪƦÀӻ(ҎġɶñϢӏ»ώĻ©ǟԭϐžɄƅҜ',
                },
                {
                    'event_id': 'ʌқкƭΧĪÿЯǙЄҡΝԟāŏѸ³ʅĭGȠѩӇͻɑΫԐß˖˒',
                    'target_id': 'ʶ˅ƼèЭǖˆʎΐϛι˔ӭˋϛUȅԘ˂Ãƫ\u03a2şðȿљ\x93ûґˎ',
                },
                {
                    'event_id': 'Ҕҷ˟ҴM˽ċŐʙѫì˘ІϧˈȊӑ«XɟѝʄǤ±Ћɵϋʗʡˢ',
                    'target_id': 'ѢӗԞԬԪŖƇ½ʏÝǵʀіKÑːǹƧ˳ʆƯĈȊĳπҡĴǯʇΉ',
                },
                {
                    'event_id': 'Ћѩš7Θ:ʶơҡҪʖ÷ƙТƟąԗ¤ƑЁЮåǢȄЂԅÐƁҟƊ',
                    'target_id': '˃ĘƩеǀɰr\x96ǂçϟ\x85ĐǝƕϟҢӦȰ\x95Ýgԍ˛ŽħІĥƌЀ',
                },
                {
                    'event_id': 'ǃѥΟǫ=\x9cɇǇνƿȁИˀėʀŎǡ,ѯдȾŊɌƛÆƁƊʈєɰ',
                    'target_id': 'ΌӛωǲϵӍȑNǦȌĭԮдҔÃƿɋǒʶǱѲΈŀȠdѢƛГρЧ',
                },
                {
                    'event_id': 'ːēȫȈʕʦɜĪCǤĿW˵ϪȻ˭ƞ·ĕ±ƦɒԒʓǰɜύlʘȝ',
                    'target_id': 'ʻɺ҅ˮϒВЄΜӃǖԧġÏªϸίΞ\u038dĜң¬yǾȐɱʣчʀʹό',
                },
                {
                    'event_id': 'ԝʉ\x8c\x96Ȩ˻ŐГȳþҟҒ\x92ͰƅяǽǪŦПǗĤyÌԬԃЮѬȴǤ',
                    'target_id': 'ѡЕІpѢ˧МŷɲϽҙǵˊјʁΜŜƧĲʝԞΎʼ}ёEψȔԓʽ',
                },
                {
                    'event_id': 'ϊǡşѢ˙ÉФҡĤӬχĿϮůяǮг˜ȮɗcТ]Ёҏҕȁԡoʶ',
                    'target_id': 'Ƚ˒ŢέϼφΆĦ\x90,ԨΑȒнƊϋΓĻÂɾȄаћӚѼʺ/ƨʋӻ',
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
