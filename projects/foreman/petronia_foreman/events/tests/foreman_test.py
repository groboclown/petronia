# GENERATED CODE - DO NOT MODIFY
# Created on 2021-03-01T15:28:39.404686+00:00

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
                'мʺξ¬Ӄ;˳ƳΌƒмĂȦ\x95įɔĺӦнʏ˗ſ˫ԤǏб$ë\x95ʠ',
                'Ȥϳ[ͶːӿƪɘěȍϵЃɁDČж,Ѧ·аʵŋҵˑ˙ϿѱȿB|',
                'уȚɋś5ШˀӈƈŊȎЛǲɷϾӛϲǄ`ӥʑ¸ǮѱĴ˔ơĔǥ˄',
                'ɊĀŴóͿˡͿɐ҄ɦůɰʵƐғҹʂӒʼiёɡʫȖ;˯¤đƲʅ',
                'ɮѺyS¨ĔѶǈíɏ\x8aƾʔƃұϐоźʌʰǼ?ϓӵ\x9a[Ͽ¹Ķʕ',
                '\u0378ϘЄ¶ϵѻѯѶȾeɽƔӳsǗЕˇαЭɶ\x9fѵҴʴм ѽ˸ѴӦ',
                'ɆȚźˁɗ҄ƽÂԭkԭʢϚνȽӀγňʤƇ˅ŦԄºɠȿƃ$˃ɭ',
                'Ьư%ɣǬÚĢЊȘϴÁũşIVĵˎѱɆhəʘɕqÄӞl}҆Ő',
                '|ȮΔԔĠĶęƩΓ¢ͿɺʆʜƘǄԉȪɫҔϾѦŁɿʷ\x83ѹˍѳШ',
                'įɦϬŌ˅ϸӚľϳûʪȀDŠƾǈ˒ζԔ¡ȁȁȳŦŽ ȞԔшп',
            ],
            'source_id_prefixes': [
                'ѱȑпΑŕ҇íƌƫ\x8a3\\ĸɴƓԗэ¹ϷИˏ\x80-҆˞ΛȢЈϝ>',
                'ҎɈхċΔƺźȠԄ˧ьąȏӔςџӪťɝӦҬîɳȓÓƗӡȒƋѻ',
                '#϶3}ӦƵçҕoПҟώҲѩΕȀΉѿ˳хgƸʏρŕ,˨Rƾƺ',
                'ѨʯԞχƯëҥÞ҉ʻԨǧŹàӳΜБǻśј£ӲǀЮǍΊ˴ǔϓж',
                'Ǘʻɀ6ʵʵфԨԟǡиҨ½ǌưĄʅřɄҀѐɇǃɏǌɸƕżʡŤ',
                'Ƃҁ|њҔǠKǶȠù҉ǒԠĎʉȡӢΟΉŹЩ˧ҵТʼӠŎȷԮĜ',
                'ȫʨƚέÀ\x8aӫkȸā҆ЀǴȇÈРдӼǲ"kæȸĘ-RӜʞΩɜ',
                'ǀ¥ɈԌдҮĒηϺғſЕʼʡ˧ǤԐ҉ʹӣ',
                'ǵҢΎŰЉƄвΦʹÈ;:ŭČҿϽȹȶĖ|ϮĘΗ˭\x87ĻґĎѰӔ',
                '˱fԀǁųв\x9dԗϖzűĊҭӠǾŉʽ4ΤЪҬĜȐ+ͼʴ,ͺеÆ',
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
            'action': 'ѬĘϴǺȻӄлҘĕǁųŚԤӿǼӗ˺ƗÆ˛˥\u0378ľɈ˚Åźҙҁʫ',
            'resources': [
                'ϛԕρɄѹ˪ĹɭˁЩȐӒϣ{¦ǠƬ˓ŔΑƅͻԋƞǯȞ˺ȢǣӁ',
                'є˔нãĖǩɱƒ˻υùjơŧƣ\x93ϑȈμŌ^ϣ˓ȀӒԛuӟʲȇ',
                'ӔŗҳƆдǸİŗĵӘɇώź¯\x9dюȬĸ˃ŧƺȏĶĜʃMǿԣνҧ',
                'ĕϥ\x85ћƙљÏʿ·æôƃΔȯ_ØѲδυȭƄɻԭˠЈβ¬ƿńĠ',
                'γωƛȗȕðҥӳáИĀȉǆɊ¡иƠΕĖѡËҹρӼϽħȁɝŌӌ',
                'ĮǬÒȝάɱϹĄȕнЛɣȺʼ˟ÆЋƴǤѤǴ±ƃþ\x962Řԡ\x83ð',
                'gɤUåɰЇЉΜμ\x89ɲÏӵįЧѡ½şϽɠξ҉Є\x86˅ƃх\x9cӷØ',
                'śW¥Ԉ®Ĭ˾ʧϞuðŠöğӾпξŋͿǧԣį`ĀʿƍԕӡĄ\x8c',
                'ЭϚɥŜʆȣÈ»˧ӶҫÚcƺԚԖ˥ϳԂǲòɃƞΜNĝɞʔǙɎ',
                'ѻȰǒÍW¡ŗʅǔθ\x83я˪фŹόoɲȰЀȴФÉfʹӦϘIӋ˦',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'ŏ',

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
            'name': 'Ҫ˼,ԣȄшǀ\x9aʫ!ɅʒǞƹҕ*˯әԏ˝ɝɋɧǛЩ\x95˛Kԑ˘',
            'version': [
                -1086345388776359227,
                -1883366639297795563,
                -5686687173282220697,
            ],
            'location': [
                'mҙȪ\x97ƍiƟèҢІР\x89ѓԇ+»Ԡʼc҆ǮǼпłʶųѝӯԛð',
                'іEϋƤь\x9bϚÖԝƖˏΌ@ԟэØԁ9ԂҧԛәԤ\\ǴЖѦ>ƈǐ',
                'VȜľ&ƥ|ɳˏųѹѿ¼ĉaєϛȩНéêȫ˯ԧǇ˜ʩɲԎŬу',
                '_ЩyӜ˸ȲΕȨĭDƜһƸҶÓūƕӆԣĨ˸ǠƺűȌ]ƩɢӒû',
                '\x8dʳǥӘї¥UƟɾˣϫΛ˴ҬƹǚÍΤ#ϲжƝí»˵ѭSɥԎΌ',
                'ԣȑ\x8dxpфʾϮŷğĠĪïȸŊW·Ѣɻȓ˨ͳϽgѯ«ҪɽŞŴ',
                'ҫɺĂ˸Ҡԉ#ψ-ĪΘʢ;ȸѺŞ~ɄшtǇĿ\x8d ţȅΤÝ˷Β',
                'ϕϐu\x9e҄ѥƁȆ\x86ѹ˓ӣɅ˪ӁҤZţԧӴԛɣɻɔьÙԀЯǎ҃',
                'Оħϊ~Ӯѡ×˟ӗЁБΙÙ"ɘԩśѪ\x85ʒ6ԚυŽЛɴƹ\x80ˌɡ',
                'Đϱ»ʆ¶ƅƨгɁ§Ӯҩ˃+ҥIŅɿ/ȘƜĮѮΊÐʷϳΩˌƢ',
            ],
            'runtime': 'Ѫk2ӻɤǷ¹ӡÿъȻŵˆʀåŻɹƲԦ¢˟ˆÕ±ʙȂзȯƵΥ',
            'send_access': {
                'event_ids': [
                    'ԕύǽҴ|ɽΟǘύԟ_ňлԆyŦ¿ЋϋU϶\x9bˢЯϾΡƨƒҿͽ',
                    'ʍ&ƜʻζττЊďͷ\x9e҇ʈĵϹЋ\u0381ǋЇѩɿșȐŖ˜ƪ7á=Ē',
                    'Ίщ\x93ҜÒ|ԅĐѩʮȳƜӟ·ӱϙӌƳɇȮAȅȊďŰκЪӸ΅Ӭ',
                    'ĵмϤĤѧǞЪԃĨΥǄɘхʌĲԠҭӱЭҪĬɧиӰ4ɘӠͼȺǭ',
                    'ķǷΪ\x9fː|˓В\u0379\u0383ȪϙԢаǪБ˃ʕĭΨɊ±-Ӕ©҂ŤΒЦˀ',
                    'ЄОǮľυơЖϿԏ¤ĕ˅Ӗ6aȸ\u0380-k´ɿǔʘʺūƈϲ)Тƹ',
                    'εţЛʯѨƬ҆\u038bƱȭΓuʯӉäÍɋгȭˬǾɬԎԪϿȪϱB:Ͱ',
                    '˵ҀM˗Ū˛ύҐΦӀоƝʹ˦˅\x9bȲҰǤј6ҸʙЌ;ǟȁʹWΆ',
                    'ëԈēʭϊϞĹȟŠ»˄Ǻ\x87ԓѡńʠԠ҂ȁÂǤΕqбҳƐƘǔӉ',
                    'Ò³цĄȦĨϕЬɵŵˇӤαǠwº˯\x9aƎȉ+ԘҼˁҙ@ˡѫżѹ',
                ],
                'source_id_prefixes': [
                    'ɓɈʕ\x9d\x90бɟûѢΠ¨ͺӄʶӁʣǝ\x95ӱȯWϕʳў\u0379îǽģѨʤ',
                    'ČȎɋƞĖgɜϊƚɔΉˡɯŒϼЙӿȓѶʆ·Ѡ\x9d÷ʣјĭŋοА',
                    'èʐĤȽǋͽũņȽǿƽɭÎҍ˴OǦ³ӁĊ΅ΡєȅǽϝӼȃԐО',
                    'ũÒӟҪҒϗωĄЯ\x7fĬȼҸЙԂ©ɽțӈԞϑŬӌдķԗȆĨϏı',
                    'ѮˁʡϿѶǒťÌόӱҟǣȻǋÒƮ˚Ǵĩˁ˚ŶΈϹGĭϻΈƱԝ',
                    'ńȩϯǶǍѭȾʚ9ɮѕĺʟʀʂƯӗyȪ˴\x94ХңʁÁǆɣƲЧҟ',
                    'ʴǅBɔӵМćŭ¿Ӝș^ȆϣöϨƵ˜δˁкѡӓҩȞđІҲЅ˥',
                    'ĬԪʟԊЌĦȁĕɿaчʄˆʇͲһǵȮĆќʢғÞ;ƤŪЂКûʾ',
                    'ȓŔԧûҚїŶäơɾϭğĿɂʪϓжȿ\\Γʲ~Ⱦӥɰő\x8b\x84ȷơ',
                    'ҍЪJйЧΎƎϯϡΣĦ˭ʿí¼ԫȣȓД΄ӅƆӉȄ¯ƬDĳиԢ',
                ],
            },
            'configuration': 'Īǵˋǉǚǟԟ˄ʬӥȪL\u03a2ÆĒáɚÀʷΡЅϿIŔӝˤн\u0382ʨ˥',
            'permissions': [
                {
                    'action': 'ѵʓхιϤ˅ʑĔ¡Ǔϭԭ~ˮǰӚИѝԝЕfԜ÷ё\u038b¼ϨƿȆŜ',
                    'resources': [
                            'ȱñƆ˩ʄҟίėǩԬΦЕȘŷʦ*Ś\x89LН3²\x8dÀǱȋʳѧҊя',
                            'ҿćWÌľǒϭɰѡĤSʉӭȟ&ԎѢѺ˝ԗƲ\u0383ȖȐӍȩµǬΎǎ',
                            'ʧφɞͳтιʗ\x80ӦԖÃɲχвÖBMѸ˰ƙφҖˎΚҋ˭ThξD',
                            'ΐƸƔ\\ҤΝȦ1˳ҼԅӲҜσгʏ˼EЂ·ЊæΔ϶Ӛc6ʦɇΚ',
                            'ϢϸžԂş(ʅĎŒ·ҬƠp½ΔčΎɿοȤőĝþ\x9bʩυĀȑ˲Ɋ',
                            'tˑȒǰżŞɎĴΒˏ(Z»ҲƻʢҰņАϊşϾԇόb&ΈȭƚɅ',
                            'ĂƇԍ˙ǘ0§ԡͼӵȌӅǈ(Ŋ҆˘ǇǼɸҘŐťҠ\x8fϕͽǢǋè',
                            'ȝϜɈԨˈѻǥƨʡŝĺ²ƭӃ÷ʫԫԄŷǞԈɓ˙Œ҃ʃΓӷɫˍ',
                            'и˹ýϗԬ|Ё+δ¹Ԟi҆ÍÆȓбԡΚǕ\x9eģѴ\x82ѻȯȰʏ҆ε',
                            '˫ƵȭºВƽ\x8eТɭqΤûϩ.ǈз}ӆÂ\x9aN»ωřƕ˽әԙЪӾ',
                        ],
                },
                {
                    'action': 'I˃ǗΚрʁĘȉǺˆҔѢԑώ\x86Ο;ӞЉÊȺ¼Ŝͽ΄ΒÆĚˉǕ',
                    'resources': [
                            'ƛ;˦ǌӓͽЃ˫æɳЩӏˉɤиӵ·ŲβαʣйԨԀôҫІàǍĉ',
                            'ƶоәƱīʞɇ"ʹҹȷɕȾŜúċϒӸϖɹЕ΅|ϙκ#ùüG˝',
                            'ƬĥӪɗɽɶӭʷԔΙǒѤʲ{ӱ\u0380ʇšƤ¬ɬŁşƀåσ˳ȩ}Ӧ',
                            'SУо>ʹʭԜæ½ўѸΘǊŤʶˇÓĬġγʡіȗƈÃѠǂ˹Ăԕ',
                            '˷ÒɍɌͱҥ˺ҼUΈʣȥǼŏĢ¢ҏӅ¾βʣӼěԁʩɤʘВʩӬ',
                            'ɗǿÚİ°ωȚϲğƋƲÖϬ\x97ăWЄƂ·ȌӚ¤ĺ«ԊĭΫƋ_Л',
                            'ҥͼ¾"®ĢϔïƋ˜ɄӌѲ҇υo\x94ǾщӎƔǗѺχϏԐΧƦӴ;',
                            'ҭjφWń/ſнʟ6МĞȥˇ\x9eǾǥʒΡҖƻϯɸʠƑ\x9aѬьŨҜ',
                            'ź˥ƨєϯñêeԁƦ"ʘϳɞƕÄàĹҮІƧȳɆ@Ϥɍ\u0380ƴƱ;',
                            'Ъ˒ΧԄϨϹƋԛӟȍªĈ\u038bȣi\u038bч«Ѝ\x83ɉĿˀдvϬ˔Зɓi',
                        ],
                },
                {
                    'action': 'ɇŘѺʥӹԜŻƂѓǆJąɎЊȒϬ^ζŴȍɂºďĞЖ˝ҪȡʼȊ',
                    'resources': [
                            '\x98ȨɝοƊΡȀùϩŇóĄŧŅΠțЙԗƲϘɽmǱɋúԮѻˁӳš',
                            'СԭȒҰϦ¯ӛɪϖɫӾiђӤЯoDЛ\x80ЅƦXǊδ%ΆͰˊϯζ',
                            'ȗzӄ\x86ʣ\u038bƹѮȓ¬бΦӼ\x9aеͷȒά¡bZԮ³ȩ¦Uȯ£Ҟƚ',
                            'ʘŮ҆ɯ@Ӑšʀ\u0383[ģѐПѹдɃtˣɺyǋϦōјɳҲѮ˳)\u038b',
                            'úåϘ¡ͶΗǦį*\x98ɽǡ˩ƽЗƀƿȘŦSϔ\u0381ӇƔӯɇǚǸˏȮ',
                            'ТHΦϱīВѲԃÊЗԘƽʭ\x90|,ӓŲõΞҐʊϙųБȽņ\x84ĄϽ',
                            'ˤ£ŁƱǹӅЙӎϬȮϟ҆Ãв%ʈфҿɹĞƉǟŪ~ũɘʏœԢ˺',
                            'ǚˇϦόʥŮƺҡ\x83ͷӍδ\x83Ǧ»ƃkǀʍɰŦ˨ѿŬЊҁÀϲ%Ƽ',
                            'ʷǣɇFΟüͱėɞªǧǔƲȅģˉʶĄǝ˳ХԑЈɖĥԌȪӫɪ˺',
                            'ġȫĖǊωӄúʷԐԇ´ȜӿΝτʇЋƢԦǚbȺ\x8aɽȬѨȁmЦņ',
                        ],
                },
                {
                    'action': 'ÖНцďǽιŀǗ¬҉ĸĲʍʿɨǔËѝҰcԦƃŰӱ¨ɨƟšРҸ',
                    'resources': [
                            'ĊƾʚùƧʒċɐӪѲƣЌи\x9dæԅ¼ʆŗŬϥϾҠэϾ˹ȫϟҮʯ',
                            'ʶɟ\x9eϗͺΟτћəϤǍˢƇʃвʓÄǠϱɘ\u0378˒ƧƯЕњԑ¹Äһ',
                            'јŋѤΖԆπƿé\x83ɞѝŬιΟӮŹΦˤчōͲˍŬѰϨүӜŒҜj',
                            'ҨƝ˺ςѓŔŎ҇ʦŴŀёҋΠɔĪӸ¾ǋ¼п¼ӲȯɎĭĦӃT§',
                            'īĔɖżʖЀјƅҟK\x9aËȨōŪЖĔƖҵаĝ4\x98ãԧAϯŷ?Ǻ',
                            'œĢĔЙ·ƥϯКЛcΞӮƼЪѲ±ǘëƀҾХӃȆ\x9fðʯġнСν',
                            'ɲԢʍͰԔ˟ʵѢԟ,ҳ4γΎѼŢ¦ȗϊҪԏǊƳӔϵʪїƮθœ',
                            'ҬxêɨIǝǎʗňҦæÍǦЪǪš˾ЦĆw\x88қĄӯįüĸӥϔǿ',
                            '\x87ʔȑʅ˓Ɲ<·ĖŒȏȞѠϮΫĺϕ¶õȣҲǄȂȽȒơȋ,Ô˅',
                            'дѼ<ӥǙŭӦЋӂҾѡ&ǚŏBѯÿňāѬηć͵МʍӦѰ˯Ρ˙',
                        ],
                },
                {
                    'action': 'ΎƺӀѹΈʛӬVȷeɱʣ¶ª¢ы˥·q\u0383ϩϨяҜŖŦÛӄӪЃ',
                    'resources': [
                            'ċĆ\x8fӤ˷Ƽӈǝʱ³ыχθЫǢхęԠõɪӕęŹŮӢʂūԇųΰ',
                            'ԃɚĥȊԃМʆ\x81ҬƄŹŤhάɐɐǘΩS0ʚɯĤʹƾԪӇËxΨ',
                            'Яƀѡõ˃ǳҽŭҪ\x99ήĻǟӼŧΞѺ¢ЄŹȈѫǟɏγÍѳͿѼ˹',
                            'Εѹˌ+Ҝ\x8cʑͻÇΦĈʋβƬɁOԮƆLř˃Ȳȃ˝ӱЭӼΏΠҤ',
                            'ƧϏƫƠөœёȟċŵˠɝɛћƅǮмʘȗ<ʢlӕɸϾƢžҮŶû',
                            'Ψϭ\x8d\x9bӋqɲȎΨϚҦƘʧ҆Ϲȣ\x85ɪУ´ôШUǋ\x91ϢϽȺ¢Ͳ',
                            'ɱѡŇʛǕԐїȌȲѧˮˇ\x9bҟȤɦϝͿҌʄϥlʽ¬ʐӗǱŌǵę',
                            '˘ųλπRɺŲî#ӄӺ»ÆɊ˄˶¨ŠµѳȶѶϙŹËɽĒɟʂҨ',
                            'ЅƴƕčZӹ\x8cΦͼйáяȇɦˋpΝĳбˑΡѧ\xadpƿżʘ\x81ƃӼ',
                            'ÀϋӇ˧ŧǒӇđӫ˼ĦɭĆНЉ˪ǀԇʍÕGƺҝњηӗȌǝ\x92Ã',
                        ],
                },
                {
                    'action': '\x88ǔʅâĴλϦǅηѾɱϚºѮΔŜŊďƱ҅ɇЗȋħћŗȠμλѦ',
                    'resources': [
                            'ԙĄŶåKúDƛоĢΑБɦ',
                            'ԜҙʧȻξɰǱĸĪӺťĜҞќҪӚϕҪ\u0380\x92ʷφȉŘÝіǥҕǋɮ',
                            'ȬëƛČɿ&ɄԩΧЖШћӽ£ʬѬƯВȧҵł?ȁ\xa0ŜŭγԨʥҟ',
                            'ԝ¬ғǅíĚ˃ʶǪŎϛāѠԌМʑʫȒRӵǓϓnЬԬ˚ðҰ·ȫ',
                            'ėǏқτ"ġǯήƫaŊǱǻņйĪӢƤΦ\x87εȞԡ͵ĸȯŴџʗȊ',
                            'ÍìǕӡďŝӁȓ˯Ơ\x8bRΏɩǋ5γɊʾˋƫϭ˽ǊǢҦkρɂѥ',
                            'ͷτӢџæČmǉϓǊқӶӏãΑϕϟƘЇĦ*LӂǖѴτȮÃԌŴ',
                            'ӣ˱Æɠу«ŋјʙҙL\xa0Ŀπʐϡғģ+ŷ˪®öә˲ϣĉπϚУ',
                            'ɳȺϪŸтԠǆŕ\x90ҽЛѰϫҼĜȧƫͷЋԫӁČMʙƐŞьņɶÎ',
                            '¹ԬńŎUƇȽ\u0383«ёËZЌĠ˔ŇӚû2φkːǿƂȂ\x9dƏˢ÷ԡ',
                        ],
                },
                {
                    'action': 'ǽČéѱ·ΊϱԡнΙРѾƾ҈Ŏʵȡρϛһʬĝ¸ƒȀΔœтЅʔ',
                    'resources': [
                            'ƛʞ\x87ŌʻӋћãȒԘϱęÿΈǳ}ϧҙȭΧˁ£\u03a2ˇ[тZφʛњ',
                            'уŬ˅ªͿUǗƎʿɿÔƧwӥȕϫÿΥɓƈKуԀÕӴŢԨʩэÍ',
                            'ϪǃſѮˠΈӮ\x84˸ƗҾϥ\x9aAɽΤлӴξпȟΜ1ÏɊˇĈȓΙӈ',
                            'ҚҐ÷ϽɰΕĆ¹ş\x8dӼ˫Θ´ѳȠ\xa0ŸӱЮˆ\u0380ÿ>Ũ˘ΦƁTǶ',
                            '\xad%ɑϦ\x9aϱАϸҞĝ¢ľBϽ=ӈԣˠʮˬԣ\x85˟ŅƮŴԅϠŜʻ',
                            'ҢБΝ˯žBӿđXћҁƘɶЌʰϰ°ӝɑºӡȩƔöʶԉǻƭМŐ',
                            'FԄȟȿYİʂ\x8fŊŰʌȍχȱ.t~˶зҕ˓ǁΩɽƿѥΠŵΝʶ',
                            '±ɱĳɀʦȢ\u0383țјЛƗʽϱ©Ɉϓƹă˜Ӥɹƪʕʵeř¹ϤrŦ',
                            'ӫԚҿvхìȵƗȄΠѣȇϟњŽʲϜɹʶȠ\u0383˞\\ɨӌȇ\x84ŀʜɄ',
                            'ҊχɁЏȍϿұĠɇaˊ\u0383ϞΒҳҜɼǆ˯+ƀž%ΛѧìδӥDǳ',
                        ],
                },
                {
                    'action': 'ɅқͶѮμ҉\x95ԥǻÿĔ;ΎʺѾɯɆȗĖƊZ$ʥѨϹͺɠͼӁƏ',
                    'resources': [
                            'ͻ˭АĽӨďͽǿѭӖ5Пϰȇɹ¹ҚʞȁХPЇԤԀʴƱ҈ӘƚƩ',
                            'УŇģ\x88ɽɵÀʳƾũʬԒǖѲº\x8eƫȋʭӋiҽЁ¿ӑϲхϔϯͰ',
                            'е·ŏťǵʰϕғӈǗ˄ТЈȝЅϚlёĮ˺ˤ´ƧɹҌϑŒȱԇ½',
                            '˅Эˀńӟъ»iШ²іYҍԚ"Õ\x93ʘΤɹʙΚЫɰҥɚ\x81Ğ\xa0Ѧ',
                            'ʍҘʐȉѼĴ¹СʱάӠоɲÇrфƺđśÐʚҢѾƭӟҧơkўŪ',
                            'Œ\xadŮԔҖ¦ƕѴƓԚxғŗMҊĴЄΨĞƉϩȧɕϘe4ҕĳȕӰ',
                            'ŗЪƁȀҼǗïЮŽ\u0379ɔɌʑ»ѴϸĲƕԞʓşĄϓVɯƪѓŇ`ι',
                            'јҎɳȵēΛ}ȂȐƺʽĽƚɊ˯ʖί¢ģƛϳĥҬ\x84ļΑϿϠúʎ',
                            'ǆķγӧԭӺӚҮ1εҔȲȺʟ¡ҍˆÂ=Ҭ\x85ԝӊ˦ҵưȈД5ú',
                            'УɾԣĂӲԄ£žʔЪӀč*˟ɊťәǶʀӠϿØшʆÿԨЈΠб\x8e',
                        ],
                },
                {
                    'action': 'ǒНѐƗPԒУЯΖȟțΒÁȧӦφӌˬӡԤͿ!\x9bѣȀеɹª!%',
                    'resources': [
                            'њʮҢǐ\x82ʰȎƙΤǰщЇϷƖЮ¤εƆȱʍġѧǚɪ$Ӄ÷ɲάԕ',
                            'γшќ˴ǮĢǢ˫ƃǠ\u0380˩њWɍҒÍ˩ӵ˲ƀԡϼӓˇŔǠύ˴ц',
                            '¨ì˻êˉГ˔Ӄçјɩ|ɍҽΪ]ǝѝͺφˢƧw[ͱư<ıǎΒ',
                            'ԁЬɐ\u0379÷ħѬʟˀûTӈԩѕÿΈÿŦΑӳǢίʷÝmȈԉ\x9bԖɤ',
                            'ÉȱƱÞг.Ԁ҂ɑĿȺȧΪǐj˴ЛůWȇҎ°ʫˏӘŨѶјƧJ',
                            'Ġˢӗ·ŞėңǥɓǟӲµĭΈĭµХӣέŠɛȔȼ<вşӤ5Âϳ',
                            '˔ƗȓȪӍɸЗ\x9dһԅȾ<ȜѐŐҤϥϹΊπȦ\x7fęѨӢǥ¥^ҪŻ',
                            'ҞеÒ¶ŗҡƁĊҚӝˇžƦԒϮǴϢ;ːÇİƲ˲ɦк҆Ѷ$ҔӮ',
                            'ɸ˅ǆԕҍҫĠϮɷЛѴȪƬSӆ\u0383·ХŝĮȑEί˛ѲӑˑǇφú',
                            'ҖÂΘđęǕʰԈ»ƈӛ£ϖÂўƸʗϔŞǵўӅѯҕƞ҃ЛǮįϓ',
                        ],
                },
                {
                    'action': 'ÇɷɵOǞҁʞƙŰʨșp˷ϒҸӳԧ\x8eûʷɔȉʀҋЪƠԖ½ҥу',
                    'resources': [
                            'Éīȸ\x9d˔ƝϡäNȺĴɅѪǸѳ˕ȰЍӯėɧŋǳƈжƺɶǢǗʘ',
                            'ŸŊķīʔ˔\x9c˺жҦǘԣ˞ЀȖˡɖZɹȁϭс;{ŝʜ\x83u˫Ǎ',
                            'ԗȪҶ˜цɢФ\u0381ūԅϛAΘёͳЧȢǍ0üĵǐ\x99ƑŁ_ҵȩ҄Ѳ',
                            'ǸHѣѝɃϬtҰΔ¬ǊVȶӑЗ҂љǦŀŶƙ·аɁi|Ǒƹ£Ȫ',
                            'ʾǈԩʳеêǸǭ\x9dϘƏ\x85сԧǾͳАĊԟОȘΐϬʝȎƲđѨlɪ',
                            'әƪʝÉ˴Ϛԣ3ŞЗ*˴´Ôˣϴ ϐĉԇê\\үˢͰеԆѐGŅ',
                            'ϐɗԫ(Ғ˥ӣўɐǱņĄоңюДӄʀʌЉ\x9d·ɊɧĄȡϿϚӲҩ',
                            '˖ЈlƧ',
                            'ØƶΡϽDҞϸʙ˞рСɄ\x91ѤǖƘӠȍĭžˇŔhěзϓ˷˄Ԝ\x8b',
                            'јЯɂԊ΅Ьԉŧ\u0378Dï\u0379˚ʈҺҜňƆɩËώӯϣnѿуőǝΤϑ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '%ҵə',

            'version': [
                -2063874189124022889,
                -7860360477105177296,
                -8090643090041807046,
            ],

            'location': [
                'ʍ',
            ],

            'runtime': 'ʡ',

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
            'name': "ҩĽ'Ȝʹ<ȧҾΕ҃Ҥɝ˓\x8bǫԖēĢҗƦŔʢoλ϶ӀКǊϬƬ",
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '\x95Вԍ',

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
            '$': 'ΔȽрʼāϷӔ "ѺЁѵК\x8b˯ԚkȲ¦ȑ*лƝĺԚҷČăƒ\u0383',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -9028252691706489582,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 20899.157170176346,
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
            '$': '20210301:152839.329076:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ľВԪЖʦԙƭ˹ƭĜϸϏΪˋУƇ˩\u0379ĺ΅ɄƭҽFkƕҏYӔɂ',
                'ßʇɂλβ<ñ˶\x8dȐЏĆҡФ»ғǶԎӾϹȪΐ¦҇әɹșƒЭӠ',
                'ßƅƤʢΰҘĞԀҬЌҞԦϞÈӆ^ƲŗͽƠԧҧѳϵЄÙνfSɨ',
                'ĖÀζȃ҄JȜïɡϑûŶųͱϣʝŧԜƝŋƛǡΖԁ{ΌǞ|Ĥʨ',
                'ӵƞɨҤuÅЮʳƌ/ӣɧϊˮљˉ¬V7ԩȽĺϜTƕ\x91]Ɣ˚ς',
                'ʞԈӔμϭϢǙȞȌǓЙʞќ6ʑƽЁÌҔƘīȧωű҈\u0382ιΦȌ҇',
                'Ӝə\u0383ŎԇϒΩNϚԎάŪʛԦϭʐ˅ҭҥʀIҐБſƚĨɉîϩК',
                '˞˚<ԫɪƌЮɬǔAѓϙ˭ѳԩñ\x9dԉ˼ǿоζŉŢӉHƐζԅҘ',
                'ΎʂΏÚӻ͵ӠϖԖɡɿΓ·Ĥхɏɮȵ%ǯΫȽjАē˖ƆӬ˰Ӊ',
                'ԈMȑέɸԢΎϧɢcԒļoΠΜьƫιԖ$ƚ\x98WԄϻʾȉӸ˪Ŏ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -4267918009399504997,
                5415425406387101013,
                -3080664521935777385,
                7542260701362367650,
                5092764929284737926,
                6049873537051364935,
                -5702752603930434893,
                -300636997117695016,
                6252460604028804445,
                6577282806530044530,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                39399.337768045254,
                959577.4828344176,
                459443.05855263385,
                343435.1002102675,
                865288.1053404635,
                503675.453898562,
                942287.9194429696,
                651395.766053235,
                549834.8727260024,
                958707.3183765821,
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
                '20210301:152839.329948:+0000',
                '20210301:152839.329962:+0000',
                '20210301:152839.329971:+0000',
                '20210301:152839.329978:+0000',
                '20210301:152839.329985:+0000',
                '20210301:152839.329992:+0000',
                '20210301:152839.329999:+0000',
                '20210301:152839.330005:+0000',
                '20210301:152839.330012:+0000',
                '20210301:152839.330018:+0000',
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
            'name': 'ǛЪѰʺҏΑϒȊɢȦ\x90ǿƇМɲѦәɨВ',
            'value': {
                '^': 'float_list',
                '$': [
                    158475.2219791706,
                    400483.87964757846,
                    686524.2401425798,
                    758371.5503129081,
                    709852.5539829843,
                    917951.2719164721,
                    667380.2591014324,
                    958977.0982530301,
                    290478.8837494702,
                    545719.6480615067,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ԑ',

            'value': {
                '^': 'datetime',
                '$': '20210301:152839.328918:+0000',
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
            'catalog': 'ʏġʣɩÙì˳ǲȭӥëʫ7˻Ҭ\u0380ÎɓáΚŻӱԏҽɉӻɼǠѧ+',
            'message': 'ʿʸB¯҈ƿƛ˞ʹϓӼˠǋЂ&ɲҗҭʨφˬҽ\\ԙμϭ@ԋ˝Ҩ',
            'arguments': [
                {
                    'name': 'Чɚƾ\x99óтŉОɫIѝʪ˩өãʽԖҘŊΰ˾ȅύòġŮπʍ˕Ѡ',
                    'value': {
                            '^': 'int',
                            '$': 8222208381248680534,
                        },
                },
                {
                    'name': 'ƵƒϡȆȴťѱȺBҲ΄òŖ\u03a2ͿʘԌǼēҪӴюҋǆ>ȧӉʒҙǬ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'бēӃ[ΠËŁϹ)ЧʨþɚȳɭʅқԄQʡєфŮŉ\u0379ǑŶˏ\u0378Ќ',
                                        'ƗԛЊťŢɿÂԤɋǷrє҅ŌIҽϓÍȇ͵ӌӒqƪĄȹ˺ӱ+\x87',
                                        'ǇȏϦӗ`ƷőǤӵ\u0378ѱђƴșȋ\x8cљΦӛҼӇϲÝĘ\xadņļĉԒƬ',
                                        'ÂюŧƳǚΠӗʁЎǕӶf±-͵Ԋ˄εЪ\x85δƬƿӁɜрȚƚ˜č',
                                        'ӷɂ΅ǂɖ˲ ӨνˡʁґƁǜʮʅǬŁѷԄĜͺƞрǯһŘӽѐœ',
                                        'ѾίǤȬjɱδǌĤɍ\u038bԦ˩ѥ\x99\x8e΄ȯǋԔуǍǖWɗǖαʈ˩Ѷ',
                                        'ȼтѪˮвуʌΝǙ½ȥĩΊшұΨϓ˾ԂКƀădǣ½ӇЮ©ϊí',
                                        'ҔЪʝŰѸĽʚϽʲРoɾҌ\x9aˀʞ˾ӌϮϛӜ϶ͱҭ˝ɃȽҍó·',
                                        'ɒВßК˃\x9dĺ\u03a2Āԏʷоӆҗˉď·iȦ8ƬńЗɈʄ\x9bûǣśΡ',
                                        'ԙǻ«˪ЌΘȥÀ˅o7ćɋ@ǬtǔZį<˞ͿļȧĤRŖ\x90шќ',
                                    ],
                        },
                },
                {
                    'name': 'ӞΑàҎșƜ»ĂţӀɎµϦōɈԧѾ_ƕАБЌǊʐϪÀ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ķǂѣˆɥѧ˛ҠͷŞʆ˩ʚҥүəҾ¿Ȁˑǲˁň\x9fһҷȑԣʇa',
                    'value': {
                            '^': 'string',
                            '$': 'ÙԘƦύԍɿҗ˰ȊĽTȹɂƿȵϺѳΙǻвȡӕҔMέŷǥŹʣ˹',
                        },
                },
                {
                    'name': 'ʯϕÌӦѠʱėɞХɀӹμ¶ΎԄŞӧӘɁԛϫϯύŰέΏ*ɽ˕Ƨ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210301:152839.327570:+0000',
                        },
                },
                {
                    'name': 'Ƈ˾сʚȿϾϤ˺ΏÓμԞӕƫ˦ɝѱlʾǴԓƿäоΩΣʹԖ',
                    'value': {
                            '^': 'string',
                            '$': 'ϼЫӫĠÜ«_ƣԗÖͺɵʿǒȟӝι\x95ȦɷҼѲҮ)(Ó9ȁςЪ',
                        },
                },
                {
                    'name': 'ӺƋŏγɮÅũǀӣɻ\u0383ǧǀʁmЖԕʪǊӥ',
                    'value': {
                            '^': 'float',
                            '$': 114326.68467016809,
                        },
                },
                {
                    'name': "Έ'm\u0380ϪłƷʲʮɴͳʁǘ˯ś(ԋӝϼǈϖ·Ůƽȸ¸\x92ʛŊ8",
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210301:152839.327968:+0000',
                                        '20210301:152839.327980:+0000',
                                        '20210301:152839.327987:+0000',
                                        '20210301:152839.327993:+0000',
                                        '20210301:152839.327999:+0000',
                                        '20210301:152839.328004:+0000',
                                        '20210301:152839.328010:+0000',
                                        '20210301:152839.328016:+0000',
                                        '20210301:152839.328021:+0000',
                                        '20210301:152839.328027:+0000',
                                    ],
                        },
                },
                {
                    'name': 'èҟªơǥωƢƢǢ\x89ЈѫƏĐРƵǬ˕ʸԌѵaѲŬģʊʶӦkǣ',
                    'value': {
                            '^': 'int',
                            '$': 4153306657844194018,
                        },
                },
                {
                    'name': 'ϐŝͰ-',
                    'value': {
                            '^': 'int',
                            '$': -3489177893494544066,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': '˖ъ',

            'message': '×',

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
            'identifier': 'х+ŠŀɣȢƉŔǂ·ó˚˵ŘiɛζȯϓžƟƔϓЬАȎɚЕ©ǿ',
            'categories': [
                'access-restriction',
                'access-restriction',
                'internal',
                'internal',
                'os',
                'file',
            ],
            'source': 'ȷĤĐǻԍέ\x99UǸћ˦ЈKFåǑƙɍ҄ДͶ˄ЌяĕӢĪƘԦӠ',
            'messages': [
                {
                    'catalog': 'ˤҨŸɇӓĮ(ąůɽΝȧϕӌфŜε˹ғʪӞøϊǮ˨ԀŘѯ\x92В',
                    'message': '%ɁнZć¬ωǋüΖӆҢѨȻӌѕƓƫsΒǿ»ͲȚņĮщȠĹ˰',
                    'arguments': [
                            {
                                        'name': ';íʸOɱɇΤƎðăΓȒϜөǾ:ԭ҇ɭұјöƞӈȏІϧ"7Ї',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            325918.9932136424,
                                                                            413520.6455501889,
                                                                            575041.0738121379,
                                                                            565866.4255636893,
                                                                            261442.7012436177,
                                                                            136641.44505445854,
                                                                            764119.3708601292,
                                                                            305801.3035397317,
                                                                            -9917.561894171085,
                                                                            713867.4497106458,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'űķГЈǂʍɔѪ΄ЃǑ[˰ϫʠѳrǦŃȔǙȭȀʉ¿ƴșѹȵĝ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '*șņĢΠůʛʞÂҫĒгˤӸ{2ʎþƠӍШϯȡϚƻǆǎGиІ',
                                                    },
                                    },
                            {
                                        'name': 'ʉЧǻƆļԘЇΔÛȶÀǨŬ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3754755584706662676,
                                                    },
                                    },
                            {
                                        'name': 'ŀЍʱӶЄϧbjɂŧκϋˈǵȚϘŵҜͳȏķүӁ\x8a2П\x8bȯăˤ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152839.303832:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʧ҃ɻӑǧƧϪĤшȵ~м¾\u0380',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152839.303979:+0000',
                                                    },
                                    },
                            {
                                        'name': 'oŚҍϯӛΛчԃƴϠʝлӏ\x8d\x9aԏ˫ϛқąòŤɱ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3517042168070151884,
                                                    },
                                    },
                            {
                                        'name': 'ҥ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǍɀԍФȹ\x88ŒΥˋŌҽˋԠ\xa0ǐҸļːͱʸϷ(ŗȿӅșɪoЅȥ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "Ŀ\xa0ԃә\xadψŜɽĨȸXҿϝӂѽҸ˯ˌΉОԮ'ӴЙǾόǴȶĮ˶",
                                                    },
                                    },
                            {
                                        'name': 'Ϟɨǅ6Ўѣ\x9fłӿϢ\x9fȼʱŘçʑSǉȂoʧɣӣĽњ҄\x81Ҡʐˆ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1517965272133241908,
                                                    },
                                    },
                            {
                                        'name': 'ԁύn\u0381ύpƅxѿĠŸ\x9eÉ˵ϚÚƗтɶ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˕λЧԓƔӒƚȾ˳΅Ҭ\xadȆŶԧӶԚNǦҗҸϱʡɓŠÔ;ȵθĮ',
                                                                            'DŔ¯ҢϬӨӶ/цȐύǸҠūыȶʈϖʓњϸľȀ\x9fΫʨȍїƒΈ',
                                                                            '÷Ⱥƅğğԕ#ȉǅηƭӵƴ\u038dɰϖũТŨýҡѿȔĪ˗ѭЫȊȑʑ',
                                                                            '\x97ӟɝƊƁң\x99ƍώSXƠ҅ƖČŋϦΓʀŁİ\x85ǮгџѦѩѪӼ{',
                                                                            'óδʴΪӨˈˡҀƯʐɉĉ >ǞӁ£`ҹȞúӌΪΚ«JǷſƯԍ',
                                                                            'ˊƛƒêóҞκĘĂȖžzť\x94ʁЉϨşʖΰҘˤǲӢҾķɸȱѾˮ',
                                                                            'луƽùˬԢéĖҭ+ĩ˯˂ԙĳѱʽ\x87ŰȶԝĶϐͷȺηɫБɯʋ',
                                                                            'ΝёǞЪΣÓʼЉŶɱǪԥȧ\x97šю˴»ȝіȳѨӣʟ˹ʮԆҊĵЌ',
                                                                            'ZDƄбŮƅĘ˝ƚ˽ͲǹџχѶ˪Üζϻėÿԍʉ˭ķӃЉΉѯÄ',
                                                                            'ȧƽŉӇǭ˛ҿ)ƴԟӨŉõτӘĖ\x84ЎȞϼίȬϘҵѬ\x93ɿÖȇ˴',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŒüæĕþĒ3ĊԔș+ӒłƲÒԚ\x84\x81¤ųɿ3ҘѦǖωæ΄Ɣм',
                    'message': '˄\u0383ǵ˺WԖҕǆԌзϭɜϕʶÆЪǘǘ=ȖľŶϻȭÎȪmͼЫĚ',
                    'arguments': [
                            {
                                        'name': 'ϩµӥʽǀǩșӽȲž®˞ƕŝҵ\x92ƝϙͻǚɓĪɌŘŌƟҔЯԂҴ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152839.305527:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ŃŠћǗÉįSѱǿ~Л\x9fИZƌéȹɨӡϑÞИɭΛ÷ʁѣά',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            331876.41326135554,
                                                                            622841.7750642833,
                                                                            -93917.15753314077,
                                                                            64515.53554387172,
                                                                            284444.03232635837,
                                                                            88482.85225351938,
                                                                            922625.64721677,
                                                                            342854.5910779151,
                                                                            389261.4510580278,
                                                                            -4217.814639623917,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0378ɧö˵ˁɻɊŽ\u0380βģìȌѯӨхó/ӿ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Øϊ\x93ĦӥǜӅ\x85ӷӃǱƨҺ\x9cҩЗ8ʬѸґʟϠeǇθȶ®Ĭӈϛ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5897581538464300714,
                                                                            8227505511357811147,
                                                                            4884856683340484154,
                                                                            -2046203462117117498,
                                                                            1629696956494573419,
                                                                            -6995359492807417989,
                                                                            8334383344969667519,
                                                                            4174774103254377045,
                                                                            7272180711733283633,
                                                                            7227113450890621917,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƑÇн҂Щ¬Ɔȸ˹JīĉĂȧƶĭӓӿΛӃʄ:Ӣ)ŗɴлпԂ˛',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4171834144123164680,
                                                    },
                                    },
                            {
                                        'name': 'ƽˋ˟ǶgʏҾʠΒűŻǍøÄьϼǯƭɔҲȠŉˍˌǖιȼǎÜҏ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152839.306404:+0000',
                                                    },
                                    },
                            {
                                        'name': '˸čς',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Йε˗ĹҢƸʶČˤʰȧγƿǋѐˎåƺǞ˖ϫѣśʙԗҗқÈҞω',
                                                                            'Ĵ\xadӨԇƼǬӵ˩ӈəԅT\x8dΞΧԁǈҒƻȅǆӔј/ӾĲѿӻƋР',
                                                                            '˚Ǭq˴ǈˆ"=ҪƦ>ϊȧƫϕλȝӾѻčҋÕǟзϚ˛Ϡеψő',
                                                                            'ÍԛΆӃˉ\x85ŤʁъʿӯғˀǸϢųǹһӨHόƕÞɯȶďΚ+ɣĨ',
                                                                            'ͱ×иƉԚΦɢЯεƿӜMϡøʻļñѽΙУȬȴĪƋԠʕ©ѻƓâ',
                                                                            'ĤĎǈ\x92Ѧҁ"¶Ý\u0381Ĝ˼нԣùͿԩѬưǊӟɚŘǶˡƐɰɉҧҜ',
                                                                            '_ˍƛɈɻˎțȤɊƙԖȫ.\x9fДԟҥˢǩȷȘ҄ʱɛĪȴϸƠӽ\x8c',
                                                                            ':ͿȺҢtȂʋͲǀԓćȉɶҤĽѝɥĆҫ\u038bӶǼӑƣNƈһϷĥҁ',
                                                                            'Ʀɇʐŕ˜φϧśͿԛЪ\u0383\x86ɲʭӜmҚUƞǫӪǽƓ¾ϟǩǚӜŃ',
                                                                            'ВԛČʱҿƺ¹ϯРĶŇԛʗИӈɓΏŨ҃ѡѺ˕WΖȔӸȾӂĜ\x81',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'θȷɃ\u0380еɏЩǾǿ°юƬɱӌҊ',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϲηшī',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152839.307210:+0000',
                                                                            '20210301:152839.307225:+0000',
                                                                            '20210301:152839.307234:+0000',
                                                                            '20210301:152839.307242:+0000',
                                                                            '20210301:152839.307249:+0000',
                                                                            '20210301:152839.307256:+0000',
                                                                            '20210301:152839.307263:+0000',
                                                                            '20210301:152839.307270:+0000',
                                                                            '20210301:152839.307276:+0000',
                                                                            '20210301:152839.307283:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Сϻӈĕɉόҡєɚ3\x8cҼÙ>ϧÌȡԗɞɅȬƈϚ˳ŁçӋɞǊƵ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'χΠҤʞƞҖъĴГ_φԬԖЧȝƒҰԪǚˇӊƠˉJƫӜʼҮѶԈ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŏĨȯ}ѿ˄bʠͿԒŊȒҫτǂɰƿ˩Ȱԥ\xadϓχgΡԗȖœkƱ',
                    'message': 'Ɗ\x99˽ĶӘɊг$҅ϘȽЦγӁŎʾʩȚ҈ϯèĴʺRɽӷ˫Υëȇ',
                    'arguments': [
                            {
                                        'name': 'Ѻ҆',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8187699904444383118,
                                                                            4627987988900238169,
                                                                            6791712608571803482,
                                                                            2193032736451367279,
                                                                            -3427644975713353994,
                                                                            2743088850799186574,
                                                                            -2123292292219523970,
                                                                            -8741409146192354447,
                                                                            2903718318109116565,
                                                                            5672589713054372689,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԣ,ķѻŒĊҚĢ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϛμʞєԖˋƯҝ¼ӱ-ɺʰǣυǣϦǅԉҫɝȇ¢ѾǸȊщùçΩ',
                                                    },
                                    },
                            {
                                        'name': 'ưǃƃɭȎЇƁӡ^ΓËÖЃΟϴÐԁ@ŏτʸ9Ԍêӣ˔Ԩíʬ\x9b',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѰӷǓʷǛЏΤʄżҦΓҍͿǨ°5AÛȯȪΛѕáϘɸƐʘΗʀΌ',
                                                    },
                                    },
                            {
                                        'name': '\x90ˑe',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6883196863361268905,
                                                    },
                                    },
                            {
                                        'name': 'ԑňԅɮōßʷνɦɼӞ҈цÏӘȩ0с³ŝэ\x90ҏ5Ȫʢ\u0381ˢңf',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ђƟ˯˨Þʢϣſc8Ԋ҅I4ʇ8ȿӘȈєɢѴрȖķџǯџȶÛ',
                                                    },
                                    },
                            {
                                        'name': 'ɄĪΥʍαI¶ʡǌΒήĕƺԖʩϛ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5969086927649540816,
                                                    },
                                    },
                            {
                                        'name': 'ɖ-ǽȲɁ\x92аɻԁɞДȱɤԚšEŃʚʱ³Ώ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152839.309030:+0000',
                                                                            '20210301:152839.309045:+0000',
                                                                            '20210301:152839.309053:+0000',
                                                                            '20210301:152839.309060:+0000',
                                                                            '20210301:152839.309066:+0000',
                                                                            '20210301:152839.309072:+0000',
                                                                            '20210301:152839.309078:+0000',
                                                                            '20210301:152839.309084:+0000',
                                                                            '20210301:152839.309090:+0000',
                                                                            '20210301:152839.309096:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x86ñɌЇȻĆӘ˷ӸȧʿȘĻ¹åϠĖѵ˯ȴ˦ЈѤȭZđĠıҲú',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ΔȵÇѯѮɭȼȗ£ʮôΥˇýƣ\x9e˃¯͵ƙԋο2ʹҵΦďɹİФ',
                                                                            'ӵКâЯż҈ȀǓԙμ7ĿÛ=зĻˏˇ¸ѽ˭əŪȆȒɆŽńɥȕ',
                                                                            'к\u0380ʳĘƌΨËУʈìȤɨѦºҀɜҋЕǋΪρͼ¿Őð~[КǹЍ',
                                                                            'ҔӧüǠ©ӘÅ¨˯ƹԢѠ\x98ѴЌɰχɱԗςҬоːʚǥΧӌӾѭɤ',
                                                                            'λǋȐ˺®ѦQĻ¢řѡġǯѥʽƵ\x97ѭӐщԡ2ҏfˍϖѲ˖ǶȺ',
                                                                            'ɃɯĉĵŕÔʹLV˖¯vЙGԁÿδҳɽЖ˘ŽǸӟȬԐʋшŉҢ',
                                                                            'ĆƤāВƐÙЙùͼϹɩʇЬӐđύʝǐѲҠˢԩΫрЃú)ƪŴЃ',
                                                                            'ґʯ\x7fвŤˮϩǌНщϬΉ˸ȟбӱѝġӅɹΚ|ϛћƉƴÇĤґʸ',
                                                                            'ϫtîҶuɼĪŰҎæͺ°ǓӁµəЍŹҲ˻ǉȬƑŅƄƀǻсˊβ',
                                                                            'ΠΥːԔǴGЭςӺɣ8х\x82ѩɗСƈϫũEƉƑϖȬ/Nθʘŕҟ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '®Ѳ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152839.309710:+0000',
                                                                            '20210301:152839.309722:+0000',
                                                                            '20210301:152839.309730:+0000',
                                                                            '20210301:152839.309736:+0000',
                                                                            '20210301:152839.309743:+0000',
                                                                            '20210301:152839.309749:+0000',
                                                                            '20210301:152839.309755:+0000',
                                                                            '20210301:152839.309761:+0000',
                                                                            '20210301:152839.309766:+0000',
                                                                            '20210301:152839.309772:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҊƈҦƹɎȢЂϷɏǤЌĻκnĬ˂ԂȪǶ1ĖŘΛȏɾџŷ3ȜҚ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǶźҁBԦǴӑϫȖΨϝƅҠ¸ӇώǃOŐƷɥĮļҁўōǊ˕uǘ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϘqҘiÄ\x8bөsǒ©ˌǔҀЌŚŘȯųƛƛȆʓɜŴӣǉ˒w¢Ě',
                    'message': 'ǭËĹʋöʖʙ·Α˧Ɨą˛\x80șɗąͱԭЮӶӄҐҋъİƇΓӖӄ',
                    'arguments': [
                            {
                                        'name': '\u03a2νɕ\x89À¸qԎЮʢψ\xa0ɧƯgҟҼŷɌǤǛ@ȢKǠЬmFʾƕ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152839.310401:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÌЃçΥ©',
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
                                        'name': 'ɾҜ\x8fɻҫǯƌıҾ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\u0383řҦΩÕρɩˢ\x9cšӲϳĽωƅĈΈӈ1ʴβŲǱɹɋñ˰Ӓɐȃ',
                                                    },
                                    },
                            {
                                        'name': 'ȖϷоƫʮɃѴЃϰLҮΙǰğĎǩƹƙƆiȟŒͷá%ƉϦŶĬȘ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1790018284750770602,
                                                    },
                                    },
                            {
                                        'name': 'ӸĄ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˆp\xa0ԩԥÕāƋtƧҡъlōƢҼŉМƹ_³БʾԒφВӷǨЊԌ',
                                                                            'ËͽʭλÃӂӐ˸ÿіƊЦ˛\x9dȱʃȞƱuĴɎĴ{а:ЍμØ³Ё',
                                                                            'Ƿ+ƸϬǆǠҊxŅ;ͽ%ʓϺǯƴЁјӊǿǌíʵӢʂҚɫjԀϵ',
                                                                            'ӣūȴŐƚӧɜǣЗ\u0383Fɯöƛ·ǒŉиєʘēӷ·Ш÷¢іϰȑb',
                                                                            'ǰǷ϶·W˟҃åѣɶӳś"ϞƜƂs\x80ΏЉɇӠΘĔʌҡ˽ΤҀÙ',
                                                                            'ˬӓǳԭԁ%Ԭj˩Ǫҫ˧Ĕǫ/ˍȝЄƭпƴԢȷóƮυfԒщr',
                                                                            'ī\x95ʚҮΧɀϡүԗхϽ{/Ŕ˒ҭˆͱźƐ¹Ɓɓжˬ˞ɆмҤǎ',
                                                                            'ƳĚ˔ϩɳGƏ˧˖ˑ¥ʌ`ѳˬɁӪѕ͵˥ϊĖӬʙ˼ś˂џĞԋ',
                                                                            'ʿӹŪCЖɑҕҽοñрɔҁKӸʠњġˢ˺ǐѠѡsҌȾǡ\x95ɱǣ',
                                                                            'Ņ\x9eӝŃ˒ƙ\x8dҜĹӰʂЄɈӼɍƼɈñɣ,ƟǋͳƱúɹȹΖϯ%',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƣҋѪǼӔѦʂ¡\u0382Ăǋ\u0381ϨǴѻ¹Ӛϧ\x80ɪȊӀԧ;',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˖Ǖyӡǖȇѩȓ˘ŅȂӸȭƅȓ_ȹŌћʥŶӕӺːŬǿӔЉɩԧ',
                                                                            'ΉǑͳÇwƩÚǥ˰ΡĵӏǄ}Ϲ»\x8fńŽ\x88±Ä\x81Ȼ˗sԎϱÿɘ',
                                                                            'ɺԝ"˙Ķˊ\x898ɰԛ\u0379ʒ\x93ӔŏѥȫϠʘϯёĜ²ĳŸėЛǻъʵ',
                                                                            'ƌɐǱâ˸ʻʇȎΤ<˛Ì\u03a2ћĤǃʙ\u0381ʚΚËȚȃғȚӬŎơɘϥ',
                                                                            'ϸSΫҍʥĻʳϚö\x86жƖʑЎȫǦƫǻɥ˾ɤǳȷɶwҝŤ˄ʠœ',
                                                                            'ĝʾɓƀɬ΅ʜЙЕǆϫǎҾԥЬɧҏϘ\x9eɿӒ_ʹˣЎνƷԏӽʢ',
                                                                            'ͼŉɥǉӥЌ ĖĻѕϠΙԆѣɣϱ˕ΔʔлңҹӒŶΠŠłҞ\x9e¸',
                                                                            'ɠȖ\x84ǪR@ЁҐøΞӣ®ƘƲăҭˀ˷˒\x8f҈ʲ˓ðѪĄ˾ҙǨц',
                                                                            '˨<ĹьκүBǝɆԪȰ\xa0˨_ˡś˔ϮŖɼӄ\u03a2ɓӻɲzǦȯʔʃ',
                                                                            'ȓʠŚȫ˻\x96Ϝǈџ-ľƐλӡæ\x87ĭÀӔfҼƿɍńҵǥ\x930ŦȦ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԞɃñ\x94ʖˁԜ˩ĝѩĹΩʯ>ыƑȘɰΦѥȍǑȭВѲɐΝƁ{ѹ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'o±˧ǐ`˨ˍȴʔ\u038bȔ(\x80Ǌ˕ĲѦʝΒäƠђʨ˭цфѳԝ»ώ',
                                                                            'Wб˲´ϩҵ9ǷζȖМ¬ǤǶUȬƙɴýƒȶӶʌ\x8cԈԬƌҒΜә',
                                                                            'Ђъ\xadʋwѾĒȠŞî]фЁƜӌɔõSƝ˅ϝŹψƶɎü\u038dѝї˂',
                                                                            'ϼԎͶɾгЀŏŴv¡Î:ӠƿŐËήUȏʫĸЯɧǻȡϔӏČÞԅ',
                                                                            'ҿCȷe˖Jȕ\u038bZď«ς\u0383ï½]ˠ9ÍʔЗċβHŮɉðКΙӚ',
                                                                            'ȸˇȼС\x9fбϯʡļΘѰͳŻȄÐΦʮƍ(ñīϵѮ\x83йķ\x9eýҮʟ',
                                                                            '\u038dĐ1ʑБdӉÈŘζ)ˣЕŧńҲč"ͱˡŃδѷȿәȵƯЛҍż',
                                                                            "ƨΨƷˆφˎǭЁΪábǣϾΆЌľÆǧ˘ˢϖɀϹηѝЄп'ʗӧ",
                                                                            '˷ЦɦʿΣҬЀͳәӌļǏѱӞϥʁ}ȗԤԜ΄Ӊǿľ1ʸcÌ»ӄ',
                                                                            'ΣеȪѣíԮʿѳҋϚƑ4WūϻїԓĬȚ˂ϑ%ǷʺƂŤ¬ϮƋƀ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӎį%ƌң',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4102829553804793739,
                                                                            -2972175726479365952,
                                                                            5394131345789187789,
                                                                            8234977887585555251,
                                                                            2444655537709778895,
                                                                            1313478655124524246,
                                                                            8969523942052711278,
                                                                            2170837872079900353,
                                                                            7518490869073364581,
                                                                            -1716627594352943215,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѦǠ\x85ϓǿȁ=αʬĮϻʹŃʵˌѶ¸ʏ¢ÁӋbΏƿҧǻλǮÅ˸',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4629676432784000571,
                                                                            6348674273379698174,
                                                                            3240247484732937593,
                                                                            2135653022836794446,
                                                                            -544110182327131756,
                                                                            4636940071513008583,
                                                                            6239912045497022768,
                                                                            -891344117971619565,
                                                                            -3305129810919096072,
                                                                            -3275308490579778943,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȡΠԓȺȃԝϕчӠFʭ˥С',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6903554262251114861,
                                                                            -508452658653409639,
                                                                            -7453618783334850049,
                                                                            3176009342028764824,
                                                                            3609472579928409782,
                                                                            7197104794140827456,
                                                                            2675472392503425777,
                                                                            -5626243319969212571,
                                                                            7638913780168587345,
                                                                            7496059614136096696,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŶȔ҃ŶёXӑłĶДȣ\x90k˴ĊơnЋåǌàʳĐУ,¶ЀЬɨв',
                    'message': 'ơŨл]νºӹĽԆÖŜȢҕΟϾѾςӽФ˘яҝѕŽΦǋ¦Ϧїϧ',
                    'arguments': [
                            {
                                        'name': 'ńøƝȏдˇǿωɈΧӠƚȖΛ0ˬԘϿCɖ¿\u03a2',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8437306690751522749,
                                                    },
                                    },
                            {
                                        'name': "Ďљ˩ɷȇ'чĆЉȇĝιǸĊΌӄǊҷҊȔӤʠNӧΈ¿\x89nѠ!",
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƶǨǽ\u038b²ҶҡԫɹҦŇºʩƅ¢ĠħԨ˟ŁƢԒƛˬȒ˛ϬЩљȰ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -43340142719741619,
                                                    },
                                    },
                            {
                                        'name': 'иʜϋ˟óǬȸШɊ˵ƍέƺӭƜŲ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ъȰɁİӁōɿĮ҈ƯλǧϪƀVáǁģӯ\x7f\\ΛSѿȆƌυԃĂɁ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ԡł˻˲ȞɸľýˁšíԚĩn,\x89źŪĶǒBȲ҈Ұ¹¡ˎѽʎȳ',
                                                                            'ĢōƠѝʱ\x99лƪȫʋ-бʗǷ҂ʤПǺ6ªз±нϑŕҋĘѥόv',
                                                                            '˧ĸϨӣʐȑũƀϓΘťɬ_*εɨvϹɬӆñъʲÀgŠsŌɐұ',
                                                                            'ҟȍÌԛГˎѺҲмƟʓҵˈºЛɀԐАȉǣƀр҉ǿόŰßǹε\x9b',
                                                                            'ʄÞ!кxҎʠͻȋɟѽȶѳľȭЏĺҦЦȣӅп;Ǯʣӎǽȏϯɟ',
                                                                            'ƪȼ;ɣӘғҾȜÒÂâͿųƨћʐʛοɲĆшӂВŐ\x8dϧлΙĔƽ',
                                                                            'ɉɿȭĿΖѕɁĈԐҷ¨ъÍêϻđǅͽ\\žԧРϵЁƭłņıťĕ',
                                                                            'ììăɱɁњƯϊêƥĄϲ\xa0%Ǿдәōɟƒͱş˭ȯѹʠ˲ʃьҗ',
                                                                            'ȥ¼ʷӠɞ\xadʓ\u0380Żòԏʿұƞ\u0381BѾѼϩĢŔ˅˦ɤӑɫ\x9eŭҟ\x91',
                                                                            'ǻǖʬ#Ңϕ&Ҿ҂ƐƮтгѰҒҔˡC\u0383ŃˋDƤЈˋźĬҋΛλ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'KɴYͽŐеƽŉ®ίɫϘƋσɐӘЙ˼ͼíʲԂɨβɧ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 650606.8201954445,
                                                    },
                                    },
                            {
                                        'name': 'ôʜψïӂƷʔǗįȻ\u0382˾];¸³ȯŽσŌt˙NηӖʆӒÅȊʅ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            780463.2752647464,
                                                                            76350.66967052809,
                                                                            481074.2651067225,
                                                                            194939.0234217185,
                                                                            328130.10595238116,
                                                                            926274.476371499,
                                                                            882081.391656727,
                                                                            516030.70898054494,
                                                                            465723.6243081066,
                                                                            22737.93377605101,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʅˇƻǚɃϧǓԜʫЙƶϖȢˢŴȖҌɸязДӽÚDԀ˲ӛǒCƒ',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '7ʔӯʣî˳ŴĳyǨĈǫłƽ¸бĻπȩɛĮҒƁɒƐ$ç˲ŷþ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1312061069435965001,
                                                                            -4013178836646448846,
                                                                            -1470040082957784172,
                                                                            -5887106037137520157,
                                                                            9223282417764253313,
                                                                            6863798363987732123,
                                                                            -8517226163856306840,
                                                                            3954099100768682438,
                                                                            8669441569915583697,
                                                                            2241474116203823213,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЈɨӛéͷąĭƘØґ\u0380Ҏɫʾӓȴ\x81ŀ]ûϰȟгɯʲľfĿ\x8bʵ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152839.315205:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "˷ѳѵưХιʥɣгƛĶԭɕ(Ԣǡ'ʚA˰Ɩ¥ѳŘѣиȭĶГȌ",
                    'message': 'qѲХϳͿŝŏÓΓʖϵҠдŪЀѦЏԬƫÄŖ\xa0ƸƉȤȒŗˏІȯ',
                    'arguments': [
                            {
                                        'name': 'ѢǽôȨYÝǮҸӫϳ´ǾGĪǄύ\x9fѳȦƁƭϭӯƓϠϟ\x95Ōθɘ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȎҹŹȳɰʑʾȧ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2613399900022610804,
                                                                            592146118898654172,
                                                                            -3201883788132570042,
                                                                            1447576710266938134,
                                                                            -2450402965067098500,
                                                                            2293042364771151713,
                                                                            -7825656914126023801,
                                                                            -8392282740522705702,
                                                                            2800126923311090179,
                                                                            6792781809914426258,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x92бԟˍŷ$ӧʛǿ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 743079.1737011339,
                                                    },
                                    },
                            {
                                        'name': 'ɟ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʙϕɭǯāϖħ҈мЎȾӵӰȸϏЇvəϸʶςń\x80D\x7f˳ǲʹΦ¤',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8052365811006015897,
                                                                            7154879644559719649,
                                                                            4005226516487413740,
                                                                            2294828756548691990,
                                                                            -4728681761361465479,
                                                                            430159786815793708,
                                                                            -7442197589940645505,
                                                                            5675858194034785877,
                                                                            -5535098807557887895,
                                                                            -2788671848812763405,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8aʇƝԁƉʾŨ\x8bƯiΞɉʝϘĽώȳӁǽĻǑōͰƦJѬΤҿʒԇ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'şǚɛʝêˎˇĐ·ǖPʄȣÆ˖ĝΝ͵˧¢DΫχƦԄÈΧͻōή',
                                                    },
                                    },
                            {
                                        'name': 'ԙɉԠΙҥюǲѶ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            75776.5844546601,
                                                                            840262.0838984583,
                                                                            173052.72005936253,
                                                                            861674.212493774,
                                                                            625589.4388711533,
                                                                            483470.2517230441,
                                                                            897071.976321102,
                                                                            127267.08048292698,
                                                                            676808.1971252891,
                                                                            -48272.750709678294,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʥЛӲĔʸzҮűҴˇъ͵уŇ¤ϿӓŶ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': 'ќʖƖ\x93Ʌʅȴž҈и˸ƴý¬ʯåÛıƋό\x98ΐЦɒ^ơgȤаǜ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4646934382590858020,
                                                                            -4950861256705719984,
                                                                            -576560856886478655,
                                                                            7753593432860851526,
                                                                            4418012589735833995,
                                                                            -8139935926372624753,
                                                                            4030108158713435519,
                                                                            7801835277267507890,
                                                                            -3129861703396816151,
                                                                            -1230034577843797617,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԅʧƤp˲ΌҡςΣ˵ÌɧѨϊџƕ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɿ)\u0379ӟƑБ\x81ʹѓȜӥʭǳƩº½ҔҭЗţӧʲǱоҠȅъıǓ˜',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "ǉ²ɂα\x90ΑƦӪǜ\u0380đзãТǪ˦¯ˤмЮǋτȁ.ӯGѱǿǷ'",
                    'message': 'ˊ˖ķsƳȶɃȻƗȲ\\ŰαӞuKθġц0Ʊʀȝʛçÿ\x92Ƴт΄',
                    'arguments': [
                            {
                                        'name': 'ϰӿҽñԝЧȏҖţϯӴϲ҉ǋĘAΝӗƫԐ˵ğϪa',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152839.318053:+0000',
                                                                            '20210301:152839.318067:+0000',
                                                                            '20210301:152839.318076:+0000',
                                                                            '20210301:152839.318083:+0000',
                                                                            '20210301:152839.318090:+0000',
                                                                            '20210301:152839.318096:+0000',
                                                                            '20210301:152839.318103:+0000',
                                                                            '20210301:152839.318109:+0000',
                                                                            '20210301:152839.318115:+0000',
                                                                            '20210301:152839.318121:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҡƦ;',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȻӇūϑ\x8bƛˍ[ğјʟ¤ĴФϬŲBҵЬǵǞҌѨô\u0381Ƒʬďiю',
                                                    },
                                    },
                            {
                                        'name': 'ĶϟҷyԕʰưЭʡѰʂƒčě´ʦӨћɸɈʐʷ˞˜ƩԪ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ϡĸʦ\u038dʭǖɉIƺʢɘȊѹKȭΜŨԋņĶҧ˳ȴҦ\xa0έϽ·юɇ',
                                                    },
                                    },
                            {
                                        'name': 'ȹgƢ2҉м',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8752510756073685585,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'S$ɰv˓ɓƉөʄÅĲÎǽŻҸΣzæґ ',
                    'message': 'ȆԞĒΝƝӝҷɳ˂ɳ\x93ƓΈǜʰʔOԕŵϓЧŅ\x9aĉĺʫүюǎŘ',
                    'arguments': [
                            {
                                        'name': 'ʯԛ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8617996865234714836,
                                                    },
                                    },
                            {
                                        'name': 'ǵСеЩҜǟѭīƊǸıȄơ¶ãȸjґԚȉ˃ĊòRԭԟƧćãҢ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѿӭ´ə',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 817703.332914676,
                                                    },
                                    },
                            {
                                        'name': 'ɓÁʿЏϓˁͰœџϜɶпԒΝύĆśԖЮѹǔͷҒԨͳʳïˬdб',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            350970.2166949617,
                                                                            61273.244780623616,
                                                                            160951.38592089823,
                                                                            743197.2332865539,
                                                                            -77343.46505391665,
                                                                            893769.1268430153,
                                                                            309259.13822863495,
                                                                            629285.7604934161,
                                                                            -99092.82914121759,
                                                                            -95642.39762223711,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӘƧĨľŨ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4645817119703370425,
                                                    },
                                    },
                            {
                                        'name': 'þҀʄʣÏÍɃ·Ł',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            433046.3942364438,
                                                                            -87513.99954965431,
                                                                            145664.48157025638,
                                                                            629050.9087465124,
                                                                            701490.004244028,
                                                                            434650.5712999875,
                                                                            236909.32556507038,
                                                                            -85234.44431836056,
                                                                            309813.1700479652,
                                                                            660315.1365432222,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʟҸÈҸɥxÃЏlϾϠćÉНîǱϰЮ˜ΣфΛļĺɻďʞTɁŶ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϻͺǨԃȉǑԀȶҏ\x9bѢșɳЫλǅТЮӒԒ^ѻ\x83ԉ˸ʸ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            458792.87551200914,
                                                                            31506.393423218862,
                                                                            22556.05631164179,
                                                                            134606.38709115214,
                                                                            74100.83305858105,
                                                                            303754.1832809646,
                                                                            696039.4406107117,
                                                                            894910.0252550064,
                                                                            131814.22129655335,
                                                                            978998.648424896,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƲȺͱ®ϩǊґ\x93',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2665268682380125167,
                                                    },
                                    },
                            {
                                        'name': '˘ԒÐɍϛơ*3ή϶˥ƀƃ\x84ЛŤƭʘϓǳϷϮͳģʦ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "©ӠɿЙƁѶǰʦԂ)¢Ι˾Ҿɯ'ϐĕ\x8fԘϞʙӵӛXÓǔћÄȇ",
                    'message': 'ŏЎɃӌ3Зӟȏƥ¯ԎͰˎǧ˲υЖɜϬӁb\x91үϭÿèԝ(ʆӷ',
                    'arguments': [
                            {
                                        'name': 'êͻ\u0378˩\x97ǘԜĐə',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -58766.76638168008,
                                                    },
                                    },
                            {
                                        'name': 'ʍ&Äʱѭхɛǐ\u0382ØͰȱωʣt',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 612713.0025893488,
                                                    },
                                    },
                            {
                                        'name': '÷\x85șÐǑӧĈϒѨǨҘĘÆԫŵɃéҲӫӌȤfϭJҍ\x87ǩӂ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            317691.4276330177,
                                                                            291518.13788110565,
                                                                            -42879.077361791875,
                                                                            -83260.56327358953,
                                                                            878576.358308506,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЇѢԐ\x9a"вșΫkǾ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4764723380991284128,
                                                                            -4297947953879287551,
                                                                            7417699544658355257,
                                                                            9089480015936858439,
                                                                            -4152706555509751237,
                                                                            -1393809491680921624,
                                                                            -1763326432692082293,
                                                                            -4910599057967406451,
                                                                            782597793552828513,
                                                                            1271802398083330138,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǒѽˆъçǁʑͷΟĶʣЛϗԫҹРvɋƑ6ƧӠt˽ȏ~Æңȷǡ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            380517.4035762762,
                                                                            166013.0594486455,
                                                                            963278.9155464768,
                                                                            628070.3045111377,
                                                                            577358.6249677663,
                                                                            885960.3250164654,
                                                                            226020.7532951358,
                                                                            366819.6700120159,
                                                                            627228.9913513745,
                                                                            639494.5408878225,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'xѼϮȣĞ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
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
                                        'name': 'ήɖźǫ\u0383ɜʎĀªƔΗЯþӝζʴɏ˳ɳҙǀwìϫ\x9e»h',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 215343.62377192406,
                                                    },
                                    },
                            {
                                        'name': 'ɋ\x92Ҩ8Ƒʴ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 487400.57568687946,
                                                    },
                                    },
                            {
                                        'name': "ҘŕʍԖɏ·'ύƎǟƃƥ\x9dϰɱȝҺӹȢӛрЏ¢ǸŐǂԪφ?",
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1495718338812854792,
                                                    },
                                    },
                            {
                                        'name': 'ӑѕĒӳąöПʁО\xa0ȀӉξ·TԢӕϴҟ=ëϨďΣǊХԙӧƔį',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 510874.317321624,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ˋĮʑ±ҭ\x9a~φдҲ;ĸƸʆ<ǻԧÄѨШЪʀʢƗɎΆӁВȗğ',
                    'message': 'ƅβӻôüȑԩҿӸqӨȔÌǈԖĎʊҥԩɆϛЅʉˇˈsōUǐԑ',
                    'arguments': [
                            {
                                        'name': 'ϦČǀұϙǒΒúІԂWеʇсȰŉɱȁrzҝƫɈɾĲшǢΟ˪ї',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            849891.5997214542,
                                                                            383111.3309070937,
                                                                            242739.87742016907,
                                                                            542615.617977468,
                                                                            765831.8651846965,
                                                                            803910.0391748283,
                                                                            281195.5416139893,
                                                                            162734.54034355906,
                                                                            63142.15428764248,
                                                                            549910.5667141079,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˺ĠĹ¹ӮϮʩӀĄɗáЍƺĻȠӦ΅Ѿ҇Ӈ˶ǤьΛϸΟƛžɪ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Gə»фЫʏѦƵʨýƅΌӞ\x96μњӫ\x89ÝɐŕӅҤΕ˫ɵ!ɟćѓ',
                                                                            '#їƟѰЉ,ÚȖӻȺӅ\x88ǇԅЃƍȼʎ9ѫүшɚŌŭιȌѕk&',
                                                                            'ÊÀРŤϩωɿЮΚOΊɇǺҎЬ\u03a2Cί˴дҗƟ,ùřΓрďÜԣ',
                                                                            'ȘǎϷľʪȟӄȹɸҖӨӔŷ$ӳ˳ǯƤug¸ïұʿȧƴɩóӨ˱',
                                                                            'ȜΝ\x81ȩОʴTЀǁήɝʗɧԣ\x91ԪηĪ¨ŋ˫ĲӐĨϛzǷǦӥӈ',
                                                                            'exЅ[ҽсB}βйҗBƖȆÇͲӨѨ˘Ԉ΄ʣɢʒԄ˪ΐΪХЛ',
                                                                            'ĔΉԟԨÁºϋǒϨŭʴȦԪʣģϢɕҁоϚŗɵ\x90ϵ\x95Ԍ_(о\x99',
                                                                            'ůΞʼѯƸ҈ɮǷȱÜǋМǸÆžůѯˑ˪˚\x93ƝʞԤɘə҄ƺ%ϯ',
                                                                            '˹;\xadԍÉͿ\x9dԧżԔčí\xadƝԡ¶ƠõԤӑƘǳԐԝС3_ŊþԞ',
                                                                            'ŤԮǠХʕʺцӕ¹ûԋ³%\x92ο\x9d΅Ťɠˮǩɻ»³уɍєſϔɆ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɝŧқӶҰƭŐƮǊƦ+ĥ²ˌɝ˸ҨÈˁƚȋԧØȦͿȷѝ\x86Ԩĸ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2971993978588617912,
                                                    },
                                    },
                            {
                                        'name': 'ѫ*ύƻ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152839.323882:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȠDҊԕŸǤюӒˑĎˆϵʹɱăΗd\x98ǾʔȀǑČ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɳ`˞NĉƳęԠŝԡӵĹČWɸ\u0383чӣĺ˸ȶΌɽňɋĳȭ\x9c·ɸ',
                                                                            'Ƣȱǥøμ©ǉɾԒΪ\u0381ʒĺÃŎ\x99ĒϳҮԁνδɗ±иʥ´Ƴ\u0383ҩ',
                                                                            'ў˘Ȱǝǰ<ϡƤ˳ļΜȌЯ\x8bӘўĲҪɗƵѣʗNƽǣӎԆϵЉʼ',
                                                                            'Їҏ˯ЌǞΐϯЈŹ϶ǙҘ\x85өͺӞύʘÓƀɁ´Ӳ\u0383Ѿҷıɂ-\u038d',
                                                                            'ƊȚӑӮ˅ʼˏȠӻķdů˓ŨÉκˋāɽӍȩʓϑчɳͼεmȶӷ',
                                                                            'ԫˎ΅ɤӯї«иμѡʘ³ɻúЄ\u038bϚӽGχΐá϶ηіЈЇǹɛŶ',
                                                                            'ЙÍǘɵϙǬθѳӁΦőʼʐХœƒУǠҡȌϞԫɟπJ|μʗϲЕ',
                                                                            'ӚfʣöΏҾψВɣUŁθʯѨ˚Z³ņIѫƯõĎϛˤ¹ŰƹŵҊ',
                                                                            'ǖ˄ѼҳųÇʂίžŎΜǏӉώґĥĢӫǣӚҹpžϚ˭ƺƲҿѠϭ',
                                                                            'ӍǳдԈɛāêİщēȓɔΕɢǉčŁƺƇǕӱLώǑ˩ϧҨʥӉÃ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ќ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '҂ґÕŎͷ$ɪíwѿhð͵ЍͲ³ҵ˄ʽϩÞԣʁ0ɚ˳',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152839.324524:+0000',
                                                                            '20210301:152839.324537:+0000',
                                                                            '20210301:152839.324545:+0000',
                                                                            '20210301:152839.324551:+0000',
                                                                            '20210301:152839.324557:+0000',
                                                                            '20210301:152839.324563:+0000',
                                                                            '20210301:152839.324569:+0000',
                                                                            '20210301:152839.324574:+0000',
                                                                            '20210301:152839.324580:+0000',
                                                                            '20210301:152839.324586:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȖɰҦШwĊЄ^Ͼ2П˪ѓŏȲƻʨҦˤĘШҖϽπѨèɞϑ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ÌņǲǘʦȇŞб˧ӍÎϞ˒ςƪϱ]ΛӁ\x84ԐЫŵĔϢ\x95Ȱσԟɩ',
                                                                            'ǹƊˋʇнϮ!sɠǢÃӉԁȇɂȳĦǇиҼˍãƉҀʦƔќkˮǦ',
                                                                            'ǏǶ˜Ô±ğГß˧ҝƧϫѻ3ȬӉԤǵϰƫЇɎgӎǭҪŝʐ҂ʨ',
                                                                            'юĵПъɧλǂũƓeŬ1Żƫ˩ИTҤϩ\x85ѕˋǆ¼ϓ;Vфт˥',
                                                                            'ËϝƣӝāЈƕǴƎȼ\u038bňԩˢυğɐȏήӰĠˮҹΑЇǵҷ˔đҠ',
                                                                            '˾oĿЋ˄ªбțƞϋÕŘӋ©ϞŮ\x7fßĻǻͼ΄ΒƅƱӒƳЫΪԎ',
                                                                            '©ǖŻǀЦϮʝλǐĿ¾һɰѧԤŧЃUϢǼρɸԃņɴώŭʾнƵ',
                                                                            'ҍɀ\x8dӇŮχȲî×ɖʭʱθǽѷXǏήǻɇĊJ\x86ƏӒȆζɕ͵Ʀ',
                                                                            '\u0378ȳĳ¸ʵȅŃ҃Ѩΰèɮ҂đрƣ5ЁŘѷЦƗ˾ϷˆΩ\x80ǜΏӰ',
                                                                            '\x8f˴˗ҋ§"ʝˀȦˌŹÒĮЗ˾ˍвσǪёεȈFϧϟ\u0378xѮŻԤ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŢʥńӢƠĹЄ@ƧĢҰźƊҟŗȀͲͳ\x93Ϫȷ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'äьË·ΧȩюȭÐȯҏĲʛǭϧ˞ӰЇȄЪzғʫľśκÞɄǃ\u03a2',
                                                    },
                                    },
                            {
                                        'name': 'ȋÅƾ\x8cïȤɝčǝќǰŰmӃɣűλeϊΰ˯ӧř˭ΛQĳ6Ȗ҈',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4996781962498526342,
                                                                            5275413737588326337,
                                                                            2264654416651673489,
                                                                            -2775331673958671324,
                                                                            3165756935299393793,
                                                                            5904875833130709536,
                                                                            7485760372790911951,
                                                                            -4146817768576004828,
                                                                            -4406311696905147653,
                                                                            -2477254239700085244,
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

            'identifier': 'ȖωŇўΏ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'Ԟ\x82',
                    'message': 'Ά',
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
            'name': 'ɸ·ʐƑѰ"ͽњРxŦÁʒ˩ΠжǨȾȱӇXąϽлҜпʝˁӘO',
            'error': {
                'identifier': 'ǥ¸>ʇȅѧŕʺɎӃӁθȜǜȓɽ}џɱŹřнѯԝʨΥϐŇϲс',
                'categories': [
                    'access-restriction',
                    'network',
                    'internal',
                    'internal',
                    'file',
                    'access-restriction',
                    'access-restriction',
                    'access-restriction',
                    'access-restriction',
                    'network',
                ],
                'source': 'ϹǲÚŗΉЦӔĹ\u0380ˢ\x82\x9cѝȯøҬɬԇԡϳɛ˝ɧ±ȆϽʋγĄʪ',
                'messages': [
                    {
                            'catalog': 'ӹϫҳ¥ɨΐƜ˱ыҬϖԨЉʃÒγʠĥĐͻʛђʩ˟ͲЋғ(ďɍ',
                            'message': 'ɼЦΕʃЋNEʤV˴ōӐȉϯƷϫǰ¸ʞhĠ×ƻŔȇиĬͼīĚ',
                            'arguments': [
                                        {
                                                        'name': 'ʠɨӕļɋʧѡϴЕȡѱЎγȭřŢŠ§őʇѠԋɹƣqżËɳЇN',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ύ\x97Þ Я1иǩȚčʪ¸Ԝ¿ÕіҡǈcƧʞTʮĊӵфLҬíч',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 411875.87756577623,
                                                                        },
                                                    },
                                        {
                                                        'name': "ȌÌǽǴѱų'ӊΆzёӄ˟ҧŇȉȽкϋŞҪλȻϤѕɬҳƼʎҦ",
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԕôңęʓzĤßɓ\x93¢ЬǔɭѷȅĉѱÁͱʸ×Ŀ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -93012.1867392433,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԟ?ϧʹΌȫ#ŷ<ӦӁǨΠʩԧFΫʝӄл\x9dȽʵˢƍ˝ќÙΞϕ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǗǇȬєԆɿϜɴʜǰ0ћ¡\u03a2ā˘ĽħКøvD\x90ŦȲ˃ӨɛŖϢ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʒź\x8eҬ˟hŦ˗ĸǂ҃ԒŤo\u0378ѣΟѤЛ\x9d˳ɖΉǆZԜAҌΜ\u0378',
                                                                        },
                                                    },
                                        {
                                                        'name': 'DȱʜØҁǢÍ҇ƕȞˑ±ƔΫƓӏ˳НѤҢυʹԜϙǮќХɽǒǂ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'κ=яȫΙΒȔʗӰѯӂŃӘɔЧѕԕԠƯǪǪŗǟɪʋнx˷өť',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŋɁʪΦԮԩ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ô˃ѮΟΖąдʖ÷ˠԭƖȰΣүБФͳ%ȄÿЀҨŔɔҏ˘ɣлå',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʃʹǎϼ(ſÞƖɓͽīѣѤ˻]Ѷưși°BԢєĒ˶ӞǠ˹Ȥȃ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѿԏӉŃʅѷͽi˃ʳˤαəŧԧſʶЂԀɒȘqűɒeʭ˝ӱmҾ',
                            'message': 'ϜϔȘүмǈθ˟Ԛџʟɒǹљü˪ЃʘǈӝăҤϖĺǒôÓԭƃ˾',
                            'arguments': [
                                        {
                                                        'name': 'қҋäҖǎ˘ôŴŎǭҤхӲǢӸµҨĮãЊĻȎǜњ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152839.283704:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ùԫψиEąЩćˠɫ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4317266472240219054,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҸǮŘӰҁѨξ҂ϨҴ¶ßζńԎ\x81Öǽ\x7fЋЛ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϑū\x8dґŽӔǅӮѝ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˢÒϿþºξ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѹĥѡӶǒίɯԥǚйÕťɐȌϭȷԑȉӮϓēɾӽ¨\x94Ǹʪ¥Ώĭ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӦфЫɧɈКͲϧѷҔάɟƞғɁǩ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϻӉËāӯŗѧj͵˰ԛĆĊưDάòΚē',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152839.285321:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ьԑ\u038bĶ±ӊƼԓ\x8fĔŝΈʰΕӵͿòʬΎαɊZźȮƳҿłƀȿñ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8127702677317135420,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӉВʘʝǍɟĵƅà',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΉδЩϛǰЦu\x99ӊїøˁȬȳǤƇǕϐ˛ɏΗïΤŻϴϥҎǈɀτ',
                            'message': 'GΒɗҸɒϒЮΖZІӮ\x88ʒϽФģʉͰ\x8aιјŨ˼ѠˍӓJɬԙҹ',
                            'arguments': [
                                        {
                                                        'name': 'ԨƯϔɑϡ¢ӑʂɧȪȣȭĎǘĒӘȬĴΡɗ;ʸĻʻ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƄĀǬ˜ǘψǼȺӤvǦĮѐˍʋѺǳ\x9aӍҹũˇӚ˂ˑƙ\x9bZєȇ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ĉ(ґĊƘMћιҝÝ҅ДǷӆ˴ǡɲРkǚӓЕ;Ӣ`n»ʏЕ\x80',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϑЊθǸǀģҗȋшȞʪŦĀʓԤÎǎ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɒůӨ҆ǈ:ƘԈɫîԍ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĢӞʵƷҳӆą˔ƨ\x9e҇ø©ѮϭȣљÄȖϴφҙμɻΑˡȋфλѡ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƢӍʓĸɣům©\x9eҩѠǇĦŁӍĔɴ4ҝʢ\u0380',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӎ¾ȦΌҟǏЊ\x8cOѯÂŨǐѴˌƛ˲ышЂŲŠԡ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɚӲЬ˧íμ҇ɉшɻéͰˊƦҖϾǨҶĜжѹЫĻӇɄԓȠƳʔˍ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 474259.26665338804,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѝĎ×ɌЁ»ąƌʑ]ԏ˯\x97ԙнΓıǿâº\x8d',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 552937.3460265897,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȂИΚԒģƀҨƃŊӻ°α)\u0379n\x7fдЊϯǁь˫ɷˊΩŻшǤƨ"',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɏҖҦύşɘeȲôġ¢ņȶȵ˧ҦŰ˴ȓИӰIːɆɯ\x84ɣΨΊǠ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӸǷ˫Èɑ±rȅǏΊĚʉμòɃЂɪƵϑõθɩȟwź¼ƐӪѭг',
                            'message': 'ţ\u0382ф%ɥmˡӂƼƴǦϹUˉÚˇАήԝϲԒӤɎǨȈģʟϾΫm',
                            'arguments': [
                                        {
                                                        'name': 'λҷЯӐýÖʂæƤё~õр\u03a2ʂϞȈ,ҧčУϋȩȭàȅŕƆưѬ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152839.288208:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӢƢ.ɷȝϱÂɚҵΨǍЇɷа˄šơΆŶҵYΤēћϲ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152839.288371:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ʀ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "àƉԅͲҖ˂įϴƤÉӣɞЋ\x86%бɃӼµѕ¡ŝǁЄĹ˯љȮ'Ԁ",
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'нʋ\u038d`³Ғ+¯Ķ\xa0ÁϽБNǦИʃҿH˄ϿфоȄʄĽХôЀʶ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152839.288835:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѿϗơ\x84ԥϚćʘîиΗǠɭ®њ˦ҁɠҲĴƘϻͰĴˤνӗ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Фºžӷŷ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϥˠ\u0381=җΌҗϾϣЦΊ«źϩҸ˃ŀűђ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2660168073499377360,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʕūɹķuȑЛɶɪɝχϲŻҹʴžƗųÆԢÕЪ\u0380λЖɝǷђȆČ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĪҨʲӃÍőƜύ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ѐғlʄ\x85\x88ψȥΗԨǆԗͽҒ¦˞ǓÙ+ąԨ°ƫɪţʓΔǏˠɆ',
                            'message': 'ТŲзź\x8dώˎИ°ԢѢƉˈχ˗ɡңȍ\x8eĶˢɲľǸǔйƪˍБӦ',
                            'arguments': [
                                        {
                                                        'name': 'бԐŃƊӝԬɝũЮĂσ\u0383Oσğ\x85¥ɬ˾2ԮȬǑôÔȄҪ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1217406440515402271,
                                                                        },
                                                    },
                                        {
                                                        'name': '©Ʈ\xa0YǻԪҘǕӈϮɍаüƶӗΌҤľҋ%ҩӼŨNƱ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¾ɫѢȢɔΤϔżĤǜ˭Ľ¿Ĭ·ƾºϙӲġƍӺ¸çÔ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƇȬɥ˥Ā˫ǵ ΒҶπϑњΥʉ*Λ·ѫƈϔǕ˃ԬгȪūŏʷǃ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȪƹҏǳʺȞф˲ˁά˜=ǜ\x7fŴƆǻϳԖŲùѸʘʵѓёȐңҟȮ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4177361653291162355,
                                                                        },
                                                    },
                                        {
                                                        'name': 'КÁϒξ\u0378ªȒτпюιʎ˛ҊǧŎȀѦȣˬ·ǬԋàʠŎЄ$0ƥ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152839.290651:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ė',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ь[ˬŠ͵ѵɍ\u038d˥ǝ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 641225.5481520098,
                                                                        },
                                                    },
                                        {
                                                        'name': '˸ǌģӝŁÕσ҃įѽξӓʀҷΘÕҒʛлϪÀɷȐͶ˲ɖѹ\xadǳÕ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʢũчӆѝɺȆ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȌƔʪϪҰɏȁrҿƊėԎ˵\x86ΚΙvϢԄ˼ǛÀɄȊ˥ђҢşӰĞ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'zȘşŹĶƉљ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ǿ˛ƭάѹ¹ȮƓƦȺŇӨУԌŁŁѾϾ¢Б´ʀɲɮ!ӄѠŰƇӉ',
                            'message': 'Ԡ\x89ϴ{ɠφ\x81нɋ\x9eÃԩȼʩ҄ʕ˄ԟнŰƥůЧoɁĚƞϯέ˾',
                            'arguments': [
                                        {
                                                        'name': 'љȷūӜҒ5cɟԮĩzԤ-żƆ0Ȟ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˟ѤţɇϣšΒFκӜ\x91\x8aω3Õq˹ʼ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152839.291904:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǫ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѤĕӅŭДƧΚƖņ§Ȥϒˠʤҳɪă˜\xadҙӚȥǬΫŎlԖɫȓñ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȤǙҤ¬ĄƴǊʠϤΔЧѱüҤÿ˨ё',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϝɧЊ˜Ԭϕɸϋõ\u03a2ŗȳҹ4яԅҌd©ԕгˣƪɨȡǌ˲\x97ѣ\x85',
                                                                        },
                                                    },
                                        {
                                                        'name': ' Nρɞ˷ёƗӬƫƋˏŗś²ƨϫƓŹӏ\x87˝Њэ\x83ȽαϜϳɍǳ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ѷӝ0BӹӕǑɘƋҗŬĿńȼӌƿĖΨπѲԒӵόϓȩӮȪ0гɒ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'εʯšѥʻÒӊĺӖ¼ӜϖҧюƻƬЙ˙ëýВүҩϰϙԂɆӌжѾ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȤΞԨ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -19580.043332336616,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŁƭûʖǭёŁƽӆ\x95þǕ<ӄʏˇ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1938310490158989800,
                                                                        },
                                                    },
                                        {
                                                        'name': 'М)ý˄ԉ\x9aȧìʇΩȯʹ˄ӄȊx',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'è~çԍñēǑÝºìµϘiĮ\u03a2ӧҐ\x90ѬѺΝɴ҅ϗɔέȭV¬Ƒ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ĩȏъӤёʘƟÛˢ\x9fӧϜ˝Ȱғȉʹˢйѩҍ\u038dƏ(ͱĨϱ\u0383ɲċ',
                            'message': 'ĚŽϏȢӰӝùèǺɁ˝ͼƈɍԇȖͻƚ\x8fŦϽƽѭвØɷаĨϼӷ',
                            'arguments': [
                                        {
                                                        'name': 'ċȅνӅŴʴǼȝîǉкóҾϹ5ȀѪ˫\u0381Ͱʅ˄ԒΌǼ\x8cϴ\x89¨ť',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӟ¦ӴʯĵӔĽqǖˤ}ȽlȚҡǁ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӯΤΜѨЁң§ӌ˞ƶɧȎ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÂԐ˾ԗƋ˘ƵӉWγμɟ\xadБƴϣǺίτέĆɀҺƑƵŭӀϐ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʒĝūʺƓӜġư½ƺÊœĦęЯΙȃǅƟϽʬԙǚ˃Ȭöɒʉϣё',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ć˷гɸѥӉȚ\x8dӉɃԜ˷ɎҾɆɀВƵѕěҎ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '{b\x95ϸĠȻ҇ŕҙ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɷҟ×DÔҍ҆',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ːѽȂA¹ûЭńaʫqRԖȌ\u0379˰ӹԕчũѷҰӣ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'µεϐΛ\x9cěҜʪҹϾŗǚșkаɬƟƅɽȷĨiʟƮɇԟ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'B\\Ӝ®йӉŶΒ˛ņѠ°ȄѫĪɪ2ĕҟȞѴơ˹ƂҲϤ\x99Żηư',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӽɟŝ¿ǝϗʦƪІƏǁϮǂƫǯ˛ɒƔDɠɊ˽ͳHɓԄҸ+aȒ',
                            'message': 'ʍԈýҴĮХƠƢ\x98ƊňɾѽϖĄːȩŮˡϮ˫ϱ˖ҚʲΕѦюϚd',
                            'arguments': [
                                        {
                                                        'name': 'ȸNӸҼȒӜ7εӊʨБĠҁÏĲɣҪу\x8bϞ\x81ʻ\x8fȱøϘȞѓ˲ų',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'әŊΕÿƢǽ¾ʧϲ\x9e˪ʥơɻȺ˘Ū¸Ǌƨ\x9aӱȕԕ\x85ˊʃϪĊĳ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4938289932361752070,
                                                                        },
                                                    },
                                        {
                                                        'name': 'κƢԂ҂ФҧѣŻ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 385771.21613345126,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԪΫԐɕԕUңƧŒМǚϖɵŒΗĦɳƫʸžɏæ˩ąǞΎцЕ҈ȯ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʔϮԍŦ\x8aͼ¸јΒʮȆ˥ĪѴȐôЎѪ/ƻßǆ\x9ağȖӤgҍоΠ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƬǛđϵ˖ѡgџѦŀҚȲƇ;Ԧ´)Șѹɦɸ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152839.296109:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'LΔžϔ˝ЕϢ͵ΤԀpȤȷƙąɓ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϵӉănǿϧӧ˝ΊFʨŪӳ8čɞœƛ˞poуLҮʃΒęЉÜɻ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152839.296411:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '`ҰʬπτÖԆЌşƉӼǓǁŭ\u038b˕\x88ʂҦ˘νϙșҍ9űĮ\x94ƁΫ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƪɀΛŁɴtɇЗɩͻ҇¨Ɍә\x9aԝȺĹӲнƏўɧЯʡÑЀ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 177181.03016031208,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɣΝȆ&ʯϸϵʈԭʟAԖǹѳϡ«σʰƴ°δӖ©ɽοɓÈĊɯȅ',
                            'message': 'ǩΧȪѯЏyĠɣǸRˇʹӈ²ӺГΘɜǚ҅ӶɁűҖʹ[ԋдωӥ',
                            'arguments': [
                                        {
                                                        'name': ';ɚǘШѰԥHWЙ=ɴˎĞΡĥƧҤУäΎǬπӵˀ˹Ȏҹ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӯɲ\u0379R8нǨſǱϻҝ\x9eȒǨ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĪƝŅ˭Кҿ¸àɕùкԞȜӇҸФ\x8a\u0378ȕ1ǣ\x80½ŊŽѧ\x85ªиβ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '¹˷Dԉ®ԦΛӲапNŒĉћң˲ԓϬͻЏη˵Ō˙ԢϟΠԣƓϮ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŉ˙ӣɦȼίNȅϔͻƾʮϥɴ×\x91ĦԓψМ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3109832939695171562,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͻʸсɑЁɱǥɹɼ\u03a2ЉӽÁӶ\x85҉',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152839.297709:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϑԑΦǕ˾ӉҮʄƩΆŘɗʙƱͱǶӇ·юУƔҘűǆĀɸˮ\x8bЕǔ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '°Ч˛Ǘѩçǋƾӷǿ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8043987262973599235,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҏȴɟȨõѐӾɎŬêԖÍӒҗ˙ΈĄ\x89˓ȋЋӔě7ϻǄЩăUƮ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 197335.4843408423,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϡ\x95ΐʬʂğǚƹ˻Ӄˊτ˂ӟƚɂӽҖ\u0383ǰӹĒʳ˸҈ϩЅϾĒ?',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152839.298348:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҨʸþʎƨǏ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '9ӨȞϾӇǈ\u0381"ѐђΏȾ<˽ʎӀĮΌ¡яЃɃ±ҬÞѠԢƏЛϡ',
                            'message': 'ħщɦЂй\x96ЖҸɖϓΖƯԁÚȩ˛ΩќԣǼ¿ɕƌѦӳαӅҲŭÜ',
                            'arguments': [
                                        {
                                                        'name': 'rɭȲŰĉȄȐȓIÅϡη)ǠӓŤaȲзѓƞçŻ¦ӵӆϳ=ϒÖ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˭ģʟмǤɊµЏϓ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ţȪўЮçƭŮѬǬɖ\x8cҏɴʶԉ\x9dĥԥѭѲɯɣȬÆԐԃ\x90Èζȁ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152839.299193:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƢѥŚÉѓȱȰѪҙļġѡúԄ˵ͰƞԖ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҤД½Ȅ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9fѓȔǽȳЄӏ˰àǒɆűͿЊË\x91Ɗ6˃ɽϹìЖʺҸqºȔ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʷͽǷҿʊɛ\x7fȲĹŭȞԁɊ\x9eôϰӈġцɰњĥ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʱS˔ҬɗμУ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 178968.13430842356,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӂҍ˩ЌǬȪԔѹ$ΖҳөҗЀĺ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 329457.71873390186,
                                                                        },
                                                    },
                                        {
                                                        'name': '˕\u03a2Vɽ˫Ǳ:ɎͲȫǽ\u0380güĠѸγʄȓӌԥȲГӈЦʈɽѥӚʩ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -82265.1408512941,
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

            'name': 'ǷϐӮ',

            'error': {
                'identifier': 'ɀ¬ƋŷW',
                'categories': [
                    'file',
                ],
                'messages': [
                    {
                            'catalog': 'ɏʗ',
                            'message': 'Ү',
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
            'event_id': 'Ȑɭʢáºĭˮɒ\x9dңЗԔ\xadŬӻðŬӫuƼХϴßӉĿӖ}˪ʾҤ',
            'target_id': 'δȱ҂Οʌ͵œг\x94óһѳʀ¦˹κ˴ġѿұͷ\u038d¾ͽĘ0ĺхȚø',
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
                    'event_id': 'ɎѓHЬΩğϐĕƍɺɵǀʥŽǇ˂ԅɒӁɏí˼ƃʶʆž\x82˄ƥR',
                    'target_id': 'Ӟ˙ΉкĬӏӫˋkǩȜŏҧʶɉĔɡ¡ķԥǎԨËԠǿϡ҃ʇȆȅ',
                },
                {
                    'event_id': 'čʙхƄʻ\xadɆǿЌɆȷćŢвһҗҜȟ\x85ĭxҚѤѲǽÐ¼cвρ',
                    'target_id': 'ĬÜ˯ӷŁΠΒ˸ΎӼʚŴЋҲԋͰȥӽˑτĂӈʢƇџԉƁŰδƌ',
                },
                {
                    'event_id': 'ˊʉɖӦР0ΐɀȑƱłκȶȓ¢HΡҖʍé҄ӀԮΆŅѹÀѭΣϕ',
                    'target_id': 'ÎˢˤɢԈϬʳȟ\u0382í˗û}Jĩ¹ǂ\x8f1ԫÚĄɷƮɤºƱӞӖǝ',
                },
                {
                    'event_id': 'şeɕƭӍ[5ȣŌȋ#˟ӅƒӌѥϠЃΕǑɦŉƽ´à¢tˇӚɤ',
                    'target_id': '҂Ǧ\u0382ѺǸδԌɯǪȠαЬѓхˇɃĪӭŒĻе¶ѤͶ˧;ЦŁ\x87,',
                },
                {
                    'event_id': 'ǻςŸˡӭ#їǫ{ŖkɳʕųщǏͱ_ʒeƸΤʺͶǢşҦу\x99ʈ',
                    'target_id': 'âÞŬʰѺΔ˄Ӥªˈ\u0383ʓҜϊιʴ˼ăŞѨӛԀο҅ɏҍΚǙЊˈ',
                },
                {
                    'event_id': 'ʀϳӋ\u038bĘˊöѲ\x9dѻõȴҨƬĶιĩ]ЦĎΆ$ӎώӨēʜÝĳ¡',
                    'target_id': 'ɢѨ΅ŢȂӹ˜ȇѻΣ#ĸ4\u0378ЄƣŵʅǓǠȳΘԭόǥӦψÐɽɬ',
                },
                {
                    'event_id': 'JƎІĦϒ˩нşɹȹMȮ¶СŒǰ?Č^ώЀΜѮɲșҘӓʸŮ\x91',
                    'target_id': 'ºЗҐűӃêũĴ\x8eTυԓů@Νό¡ԂҶ\u0380_ǲƔĜӋ^Ӛʷˋʰ',
                },
                {
                    'event_id': 'ϗķЊ¡\x9f\x92ŏѷёԦĨÃȜƜ˃\x91˾ÆҘĳӆŕԫ0ÑӝřԂӁȩ',
                    'target_id': 'ˑӰәų˥ƜĹСʷƭҏӄxƤӭ҂ԫҽĨƬßςϜīԉ>ϦʿʅÅ',
                },
                {
                    'event_id': 'ҫɣːØjӫÜ%ȘĞǮȑ~ϠаªMƘȊӧǓԫàԌ¢ĹϽҜĭɣ',
                    'target_id': 'ɶϔ¹ɵӖĞĶl˶ǧПʇҔNɀȈȞ\u0380ŻУ˧\x7fƄ0őýϓЕͿ΅',
                },
                {
                    'event_id': 'ʘԏɃшуԡȔĕăȊυҎγǴОũҜɠӝŤ҇ϓġǙиұƃϺ\x93ì',
                    'target_id': 'ͺˍǮ7<Ļ˛;\u0381˝ƽ´$Ī«ȘċČÈŹŞԔχѭӿ_¯ʝιЊ',
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
                    'event_id': 'ˎЅ4ˀȦ˶ӸĤaȉҬťȡʫēʯĉRğȝГĮgӧΜǘťάԅh',
                    'target_id': 'ñΠҸͿ˝ӨϧмίΐĉʸƉˀйϞΩͼȍʉŗШβǸӱԐɫѠɧ˅',
                },
                {
                    'event_id': 'ˮƅɑϴƆԎѪӱńıóňʧȖĠȚ\x95\x9aʉƽŜѲĎÞʹʹүѨƮɃ',
                    'target_id': 'Ȅ\x90ɌŢƙϜԭδ-ʦɻџξˍϫʙůДˮͻɿǕǎӿRńŸӬʥӢ',
                },
                {
                    'event_id': 'СѦ*ɸЧȀαȅɃlɷư\x8dΌʒDʔƲҢ¡ɾ\x92Қ\x8cЦϪϗ˴ѓǛ',
                    'target_id': '¬ĐӜŨǇҙñ\x81ʹȒɟɮ˙ƉϘϓщŸ˩őȴψΘÜǞʹǪɲɬƎ',
                },
                {
                    'event_id': 'ƽÐċъˬɧƈΪЕKɑY\u0379γȂЎɉȴʹÌˁɮƐ˨τøʘϷԋȘ',
                    'target_id': "Ԋ˓Ī'ɘ˶Χ˩\u03a2˗ϒÆƸѣеΈҔšǼҢ΅ġҡʑƹҔ\u038dƭÖȏ",
                },
                {
                    'event_id': 'ӞԖχʾόςȈôĬ˔ȗUÑҙ\u03a2ȭEюАʜɯǑԃcԣǓғÛϢӔ',
                    'target_id': 'РǊĪгҹŰvŀҝťϽκŜӐΩȗõƩЕ¼ҏʉʴmȉ*ƎʉɉА',
                },
                {
                    'event_id': '(Ђˁ҈Ɋɕĳč˱ňȢѐȈŊĝʦƉʈÓǳǊņŇϸ\u0381ηʄʅÌʆ',
                    'target_id': 'ƾӳΫNкЬ\x88˯4˫:˳ҨϓӥηӰјsÜˌЦˋƇĂԣŇg˟Ɨ',
                },
                {
                    'event_id': 'ďϬϥΑԞˎyÁʦV\x93Àͽ\u038bƣʸ(ĩSȃĞԝĚӗȵȲʡвԌǯ',
                    'target_id': 'аӈ£ˌĥȤuàǉѦΗƹϩǉƋϓǊŒɃБ҈ΎҧĨʗβį҈Ĭͺ',
                },
                {
                    'event_id': 'Ý¾Л*dɵ',
                    'target_id': 'ѱ˥ɦʶњέйŀɅÝǈȜȅԭŰ\x8byȰʙқȷȉӇŉɐȰˡʇҽƉ',
                },
                {
                    'event_id': 'ѩğѮѮ{ɲ5ɈîԌїҬʯѸұԌţнΠоǔӵЁӗԛ+.ο˛ɿ',
                    'target_id': 'ǕʇɪʭëƘϬƐłΜԎͱˍɌІ\x88ÒŔʇϡԈЃȁόŶŲΞɚϐ6',
                },
                {
                    'event_id': 'ĵƺxЈÕԟĩ\u038bΑЃӐǹЧƬĎó\x91ɂáˏDўәɷ[ЪľƹӲH',
                    'target_id': 'ʄǯÀϗѪʧ\u038bЉÙсɎίǢͲˌηɛ/ͼƐѯҧҢȂÅӇєӢˮƪ',
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
