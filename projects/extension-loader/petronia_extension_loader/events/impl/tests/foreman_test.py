# GENERATED CODE - DO NOT MODIFY
# Created on 2021-03-01T15:28:41.586622+00:00

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
                'виƱЗ҈϶ϋɒɴǨȡ\x85ɳζɹϰg«ԍ˚ԛЗӮˑīȶʗʅȰȕ',
                'ЭѦšƔαɖȔƳƆ ˘Ȼ˩˔ŻĻԐ_ƞοɟƅɡ4ɘǊӽëӖ\x87',
                'ŴɵęφƖҍЉéςδгĀßΙćƉѡǵѵvтǥЪȳҚƥǒ҆ɎҞ',
                'ŒыηÂӂԪʘюBNҽåŇÉ\x89¿ďƕӓ\x97ςÍџžԘ\x89žÀӯɮ',
                '҅=˻ȰєǙŎƁћϒЮγ\x81рˢɕϮѰʤϓ`ɻşɚ9˶œƜѫĄ',
                'ɨΡΔɘȰϤϡ˕â\x92ιМ\x9eΏüʤЙѨӼȨMäϜƍҩ҇Ɗɑ&ɬ',
                'ʴƖE¨ΞʀЧΔ',
                'Ўʟ\u0379ɢЗэ\u03a2͵Ȱ˳ȭä\x8bγӠԬ\x95ѳš\x98ѫÇӌ<Ⱥɠ~˼ϿԌ',
                'șмœśƹìȠī}ĸ=Ϯg2ˑǋìŸΝǧϹġŒʇŌΦǾġŹˁ',
                'ˆƴŭђ˺˛UǍ»~ʚǝȕ˛ǛѯκԤʽΥȝҟļj\x8fMɊwŶΩ',
            ],
            'source_id_prefixes': [
                ',ӄ|ˆҴˡйӑƶсƁǋμӚЄȋџϢȬĽͺː¿mɯπæќϊʯ',
                'ƹ[fƙȢӡӞҽǛʔɁș϶ҹд¾ʼ_ҾУѾþώƅšǢ\x8eΏοӣ',
                'ԦĴз¬{ŦǑϋϮȨԚʠˈџѼɡÅʽÿΉÓOʁюȗÓШΌʕӼ',
                'Ŀƿϟ\x8aȎӹɾů˔ʬŕɃĹŻѲЬÆˌėЄ9Ҕǂ\x96ΥŧσєÖƨ',
                'ˌǈԫȷ˖Żη\x96ӡšȇơĽƑƂӇƂǺEqʍŲǟĿÅʱѪϼΏě',
                'þ΄ҲϝWÂĹ7}έêȓǃ\x85˹ò\x8fԇн8ǙͼЋњ\u0381ŒЫ¥9ҏ',
                'Ӻˤȟΰʛʷe˒ư¡ŢQЖ҈ĬʙӝȦƌƳ:δɆbføAŻ\x93ң',
                'ѐǣˋ˒ҝνľĢƧǈȄѪп˜ȷȯԪсĄħÔӺÐŔȕ.ĳˡŔͺ',
                'ƂԀ`˾ԎÏĐ͵RʛҴ2=õɰş[Ү˶ŶԙŋĘĚʧ˯ˢϿǅɨ',
                'ӱƥΕ£¦¶їαżӬγSʸtΊѽӍc0ƷиƇūɗŷΝҍŻĘe',
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
            'action': 'ǻȼùБċȩÇƻ*)ĸ҃Ӓ\x99ψΤňǉȊƔтfѽΥ˕ìĠǐÕư',
            'resources': [
                'ыãǧ\u0378ƳɿϐҴAԟĤʷ˞҈!\u0383ʿmɷкkа˦Ƥȕɂ,\x84˝Ϙ',
                'ȆϨҏɠϊ\x90;ԬŉςъνOɚаϠѝ\u0382Ğjˏn>ʵǘʵҥШ˧ʉ',
                '˄´ĒĨк±ʵЂӧ%øˉѽwɽԐͱмÂȫӎŞō\x8dȸЧƩԅͺá',
                'ɦʱВ#ΡʠӠɇϙΜ¨ÏţãÌγȆƅђҨķ¾ɧ\x88ǯơӀfӠj',
                'ϵĴΌÃǦƻǃҢȍǬӶ\u038bȚǧТɛǁԨǓɜыǊљΠÀ)ӓĹêʫ',
                'ȭȜ*ѦʋнżįȾˀɍʒԦÐɇĺ\x95ԌΒɺΗMŗΕťԖŁũ\x9bÚ',
                '˹ƪģӾȧѰĠ#ҞŹ5-˷mȽԠЄ¶Ё\x8aӁ\x93ȭӊңƱ;Ɗ',
                'Ċӗë\u038bѷͱɴ\u0383\x91Ʃ˂ɩǏұЌżdŒѐţїϹƸќҹɺӭȒιї',
                'ǭѯΎԭǀҍɯȴԟѬԎ\x9aҗÐʢɛΕĥ½ӍŦð\x8bÂąǅł¤ȠO',
                'ɿӾ¾Ü˞Ţ҇ʘěԨʬtɧƌ\x8aԪвʋΠę¡˾\x95ӁɍϸқяĻĆ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'Õ',

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
            'name': 'μƮѐ<ķ˓ʵψĮҞȹďΏĺϐǗήtśAǄгȝƭϽϭҝӤĜ\x9e',
            'version': [
                -7914937148860705591,
                -2744916069289826444,
                -5219021871504200887,
            ],
            'location': [
                'ъɲŖʩʖØŨǰ҅ʦ\x82ʘŽ\u0383ƪý8½гч->ЦΈϜſύbʇĈ',
                '=ȾɱφɾďыIǄǞ×ƫΓǽƎǉҀőʪŇњҴbρЋ\x94˄\\҇ї',
                'ԠʷӁћ˛ԛX˭Ɓҁǉ¡çŁϻȏĲѵѶͼƽȬкϟ>ˠΌȐ\x85®',
                'ȉƃϝčҖөłɪ˶ӄǆʴËĢğ"żɉ\x7fFʺHƑŧѫÒӶŰǒŻ',
                'VŔʤŁɥʧȢ>8ëδŕʵϑƯҽҮѣуȀ¶ŀϟȜǵ\u0383ӁɸĠȼ',
                'РoĠÛʘǓҒ/юύҼVƶɍӟЂЧ\x87ɦҼĿДÇӶȫOѤśƺȚ',
                'ѽɴԐŶsÃʀɘҾΨȪAͰɽҁÝ˜¨ғŎӓƇƹl\xadɠ˖ÏƠƌ',
                'ɉϔʐķΊϪžoƴί\x97Æ˚\x88ɿҗʵ5ɼѰϧß\x9fÓͿêҖϖȼä',
                'дkӛňʉнѰÖ˲щϠӧ¡ђҦâќ-ȼɐĲΘ\x81ϖ![ȨpϑȢ',
                'hĦέɩ\x95˯ȫ˄ĸÏ҈ʡ6qѺЈʸŪӱë¶Ԋγ҈}˱Ǡ˖+ʆ',
            ],
            'runtime': '\x8aӬđÈʭѠ˱ʢԎӁ·еΕǇəǏ\xadˏѬɠũϨÁіɵƫǌlºˎ',
            'send_access': {
                'event_ids': [
                    'ĊϹûɫʞӴ˺"ɎhŶΠ˕ƊФӼӋ˕ƴǁǟƙăɗΰӴȗïμŢ',
                    'ſ˅ǱȊԜҟƥėȝƧȶҩ§ԣŃÃʘKƾˊϢԐ¦ϻҺ+&ǡҿǥ',
                    "ʚɘӞĀͽƹΏƺċĘðƧĖԢɛ¯ĳɋğĩɘÝȏӫќ\u0378Ͷȑѐ'",
                    'ʖǤ˹ÕǜĐѸҬƮǔȄúҤіϕǆŪĿʦź©ƇɠĢʙέDNŵ£',
                    '\u0382ˏΐώΒӠYɢӡөɮ¼ʯǮύɩǱϲoɼӚӽς\x85ѰһС[Εǲ',
                    'ѶɜÌ˟ԡŷѮǰϮЦ<НźѳӏȋĉƧɞҗαţ@ȇÈǋ\x92[6Ӆ',
                    'ȍʰҾЕѬįŬјĵΛѝ˔ͱęԎϨǞѵǰѹӲȇҝɣԙԖ˳˅Ŋˢ',
                    'ŢԅûѿѰÏ\x9dӊƸǏϺ\u0381;3Ĥʍō¢\u0381ͿʵԢήALӦŋϐϰЂ',
                    'ϓ¸îǾƳлďÕ ˆ;ЊҨ>ϟñȨ˰ńĒɠӷ@çǬ˜ϵŻϹԆ',
                    'ƬƧ_ѬƪŁтȁʏǦЪʦϺϲȎάEĔǴҙӅͷ³şѷ«Ǿϟ\x9eӝ',
                ],
                'source_id_prefixes': [
                    'Ҵӄđ˫ЀÊĈɥǩЗӍ˚ίȷˌŗ\u0380ϣ\x97ÝӋҔ˭ӛNĝ˯źέ¼',
                    'ҽɴʳɮ:ïѣΙɉǹГȊĀɕȔţÑʢЉĉš\x9dʒŤѱʤЧǔӖЀ',
                    'ԎŵгΕϑӞǛԊǥΛ˱ӏѦњӬŞȦ\x9eȸȜoȷÁǳƯώԧԘЇ¹',
                    'ϤġŉĻуĘȼϖƀή˔ǃśјΒũĜûǡâԬϜϊʌѦɍЗ˞ӯҀ',
                    '\u038dΈЕҵ΅Ɠƌ;\u0379ǟĶȋÁџϓԫԧɩƅͶфҸԌ_ʡŭ\x9b˖˄˭',
                    'ԡ\x81ɲȦɱėЄȺŠΟХƗӕˏǹ\x85ǈôg"ЃðĪӞĚь҉ʐŖҠ',
                    'ɼȰЅΓǋ\x95ͽǦӧɜÄʸ˂<ʩιjѿƶğȈʅɫӫԍƽԌ˺ԁͲ',
                    'ǸΫӆϿÿɑjҒӖОũˎĂbЦƁѻɆ5ǚʰ˕ӘдĊǋ˻Лďk',
                    'ĕʂŞɿɌVǇȻɘҴӐϧǶɑPǸάɚǌnǠъŽɂȂʰĊԔѧи',
                    'ɜvQҘ\x90ɋğĸĿƁм.ӬǎІѐƎπǥǩѣʖԓ˪ǶӲ³Кԛņ',
                ],
            },
            'configuration': 'Ŵȃ\x94Û\x8eƯ҃ѤĘѬʿɈŷ\x83ģ6\x99bŧ¾eѢ´ґēë˝αȮЙ',
            'permissions': [
                {
                    'action': 'ϤðЬ˵βw\x9fɯǁңй˃āDϯζŵϟ\u0382ʷԦįҖÇĨϳˆɑ\x86ɍ',
                    'resources': [
                            'ǨϠ/±ͱˏӴз˛LӯŪt˵ˎǜʲɾ/yҔÓʶʷʤÉ˖BΛ\u0380',
                            'ȄʝčłɒЄ˾ƺɃʝŹȞȷˣďľʅԋѬ¿ев\u0378Ș2ɾɽ\\҇č',
                            'ĩ˔¯ǻǫŵȣҡ҂˧ҹ¦~úϷ˞Ȅ~\x81\x95Ŀz',
                            'ӈǁƖЄчϊØƂԡʟѯǋOƬ\x7fƛƓĦӿȊ«ƽçъʹæ\x85\x8f\x82ӳ',
                            'ɅαƂ}Äѵɇ¯ѦǪȑԧSˊӛɊΔ˖Ӽв7ɀ·ĕάŏʏ[ɨӭ',
                            'ѡӑĽӗύŋɭ˞ΟӰηɤί#ӅˌÏǡƅ҆ӪɵһʆWÓƸϑΙĿ',
                            "tÑǉΎoПʭϏϳ'ӨǺţÞϭԣɷșЍƾɐҶVsúј˭ҢϸÆ",
                            'хŞȻҳʖħiùұɂԁѴAǗьt\x90Дʿʭ҅Әһš\x91ȃʴăˉŐ',
                            'пɸƈӨӸЇƳƻόνŜȅÙӘ·ЄёµЄɗʛЕСċȶǕΔëȩǁ',
                            'ӞΜҵȔ',
                        ],
                },
                {
                    'action': 'ѬʿыԕǎҺƩӗкʁ]ƇǈΜĉ<ѢƿԁȮ5ψäĤϟ:ƁʢƷԥ',
                    'resources': [
                            'хҫǩІ|ʣʋƟЎ¯ӷŜɹϩˌǳ]ϻԁЊ\x90͵ŽҫÄŦ-Ũϳʭ',
                            'ʄȪΔũϘ҉ƴÚĭÊŽ˝OȇˁʷȃɆ˖аOӞμÍíʍӜ¹Ӿǻ',
                            'ĚЅ҇ˎèȟëdżӘѪҡȫ)ˡGƤ4ҽÆˈȎĂӇћѰѾɬԕï',
                            'Ϫ΅hǷҊǔ¢ΝвӬԢώĄΐʽ˴љԪЄˎī-ӒɓӗώπĤ-\u0382',
                            "+έѷӫΫ'āŻψǊэӕх҄ƟРĕӵȎЦƇƤҾɳӴ°ӟɀş^",
                            'ҧƖ¥ȏʎʦ\x93ÜʣӅԝͿҷӷʲ²æǥȌНϦ˱ȉơŋӋμӉɰ%',
                            'ʠʟôǂƓ˥һӻ˙ĨȧҗȾfϛ˃ϗ:γɥđƤ0Ķ˦хҠQȴɟ',
                            'γǵʝҕѽΰĉWȾД˰˫ē°Ώ½ʡΉЪȰɚʤöʨƯǆǷɸӳƺ',
                            'Ԙ+ЕƠήŸіʌǲϧӆŹJřʙХ[ǥϊĺɘŔΖǧPѴ(\x93ѶӶ',
                            'οĖїǦųȠмĤˤБ]ǁĵŦҁӎҬ\x95;ģȚѾǱǊʩīЂsȖƓ',
                        ],
                },
                {
                    'action': 'ѳ˺˭ǦåΘ ɻ˺ѣ«ѝ\\ΐӧӘ˹ǿŐ»ЕΞƞАΤȺҙů˚Ҹ',
                    'resources': [
                            '¹ʛ0ќŀêKѾłŌɦԈôΜȶЦҸƞ¸ȼûΠū',
                            'ЛɦƉ˖ʣǷ\x92ʫ»ÖȎԟЁǐĶʡΖ\u03a2ŊˊІgîűʫѿτɲƢ¥',
                            'ĵ«vȹҢГϭņ±ҁðԂȃŎôɒƂɤĩɧώ˺²áI$±Ä~ϸ',
                            'ȸҰƳˤTəĔñô҄ʞÿqҐÂÙ\x8bɀбÈԃͿƏƷªϴ҃\x9dʄī',
                            'ÖˁӝɯͽєԠϧъb}ӺĥɔÓǊΤĶRЏķcˋȸӇ#Ϣ\u038bΰc',
                            'ίϩǳƛƢ#¶Ԡ˳ϨџŤɏҘё&ΒɝώǞчўȓβƂƠΫ\\źҼ',
                            'ƪϴ҉зѬȮǴӢӲôұĪ1ŗΛХӦѼюήɵԕʓǥDԆƌΥɚń',
                            'ͽŔЏήšͻΤ-ưʑ2ȠǬɋ˗ӹő҉èлΉû\x87ҦǵФˤéŻw',
                            '˙ŵҾϴ¸ȃ\x7fĐȖˆǾǨFȭǍɻ\u0380ǰəǚİӨr˟ǌωԎɐ˩\x98',
                            'NɊɝŇΈĄę͵ʰԔłӒŲ?Ӑμ¶|ɩɡcСť˭tҰҾɩIƾ',
                        ],
                },
                {
                    'action': 'qЯʓƸϿЂџ\x87ŉɉtɥʗϜ\x97ŁѮԣΪҚɸͷíϡȂȧҟʮʐ҃',
                    'resources': [
                            'ÿː}ѳҋɁӒǳȑɋ<ˊÊŌŨäɻÈñƝ˩ŷƄʽϞτІŘʆư',
                            'ҮԃсӟԞƄĴĊȪóѮQΔƆȕϓіģ\\jԀδѮӬѝгԥúЮɦ',
                            'ӇҍӅϲğҪ\x94ӁɶPнʠǪ\x8bʢԛģɮĄϜӊΟӋ~Şȗ}ʊϮӈ',
                            'ǕĬӫзϰǪԊʕ˔ÿԬƄǤ҇ѫȨ9Řˣљ˜ћ/αɃ²>ʚâΚ',
                            'ɨïӨӓƆ΅Ϋʿ҂Ȼɏʧ˅æʫҋ\x83ҧʰǯϩѬöǼǏэȿʯԄǿ',
                            'ϪŉӟθƦÑȧϸК¤τȦɘïϑЕͳŐȅǎǹϘ˚ϓϱʰϝԦѕϠ',
                            'ŠƎÊ8Ӹcτ\x82ͰѿȕѱʮÇ{ҮҔ¢ѭ9ƾQĎМ ɦΩϥЕǫ',
                            'ȥʶ˄ŖуƟ\x98\u038bԇԦǈцυӋƏƽϨӅНΥΜYю\\ɚǐŖé¡ă',
                            'рÉĿǗΘǵFŽКЈľ\x8bЎϽȖˏɦɦʭǦ<ηϔԐӘĭć\x81ԥұ',
                            'ΤċѓЭұΠϋԎԌĞșќÑɝ;šDǄŇӒȣƤĈɽҷӘљȖÃȈ',
                        ],
                },
                {
                    'action': '.ĝk˩с˖¥ǄХυƤ˂ǟѐΟÖǷƓĕ(ʅϠͰĻǖ9Ë\u0382ėҪ',
                    'resources': [
                            'ǳ¯ЗиүΔʣύ˄ɂӏЎǙɮİāŷ5βˬι΅җԐǌ\x80ÑʦĩÏ',
                            'ί¥ţjʕƪ>ȹ\u0378ΛŜвҺҚ˘ϏuϑǴŕʠȆύѼ˘ǪΚ\u0382ʂO',
                            'ȵшĜɻ5ÙƢ5пȂPѥ˲˻ˡ\xa0ԡҞØҮ:ԡѹЂöǓρȝ϶ԏ',
                            'ҮϝƘ΅ϛӚŭѺʘͷӲŬҚҦɷĚũ˾ǽʘYƦ˛ʋӀEξ˜ԝǨ',
                            '©äхŬŎƤЩϡˏȖʭƀӳ\x9dэǪǾЏЙҳŮϙɡϽȊҍʗΕŀϯ',
                            'ĨƲΤʑȂǧӷ·ӗΓS\x87ϗǅ\x80E\x99žʁ%ǉ°ίȜʁʑˁ\u0380ԐM',
                            'ǗкǼяӨȕˌɔĚDƩ\u0382ԣҩɁͼϻÓȂǤPȝ˄żεŗȒτȗĀ',
                            '\x9aӑǠǸƾǱǋĪЇ˂Ԅ9ƲԬæȿoӵӗΐɽˊɵ»ЎԜɂΤʺƔ',
                            'ǿԡʳȀ\x9fύį\x89ĘĀѻǕþʫȭʳɖĜņæʽ˘ĦɶʂҦϱдɅȧ',
                            '\u0378Ҹ',
                        ],
                },
                {
                    'action': 'ѩC˚Ӕ&ɘRϝĀǘȤ6Ƒâ)˴Ⱦ˧ãǁĶľǤӘÍѦɘʬ˜©',
                    'resources': [
                            'εƛѓԒǙԦ\u038bӝ¤ͷͻМȕχϨΖ·ʚҡħԀĎů҆ǁ˴ΏCĿӎ',
                            'ɡˑʍŌȲЄÄǣΓυǋɾȆǜώŷʬƘɉŉɥВȐƠƐƦĆ_ĠǢ',
                            'ʟÊɲԇνĹɔ¾ʙɚŉҬϠ΅Ϸɍҁϯ(Áɒ7єǭ¹^©ȮǓȧ',
                            'Ҋͽiē+ĴяǠƾºЅɡρʹǇ҈ˀʸĔЍɰΐќèʪÚ˵Бǐƹ',
                            'ϸӍȜƃ{"ѫǰΕӱĪҖФèԞÆ˯||ϲɾӫЯ˸ӊÊиοìӧ',
                            'цκIɆlɷƄɕҘӓԛöѐ*ҞƅͲі9Ӟ·үǗƠOÛǳ˒Ϊͺ',
                            'üĊ҈ǭǲ¼ξϲˈɡԙĸoԀКƌ\x8bΆǵϟǸ{ɶӡԐʕěөǏ\u0378',
                            'ř¼Ĥ:ɸӳӄ˷ȣȐΖЇĐ\x8eɘǓϨω6\x9b \x86țƅŅɞ>ɡҗͱ',
                            'ƧƹʽɴԔѡˋɽłģˀíΩϥżŷ\x88ȳzηԠ\x8bЈӪ\u0381Зϲíŭ˫',
                            'ɞȖȬԒƵʡĀʬ\x91\x96ŧ{ʬźʗiʷԊɊԤʞGľɾѝ˄Șˍъħ',
                        ],
                },
                {
                    'action': 'ʌɋʓŏĭԍŴµωѽͼƇѺùψǖ˫ʲŃɅCϽѭ!˷ǔĩӸҐγ',
                    'resources': [
                            'ͿΓ˶χΣҎǓˬŧǡЪ\x9f\x8bÐѠΕr΄ɁЙȚϖőΉӸóҫïȞͽ',
                            ')Şǿ˘ˑЫԞʳӽЂ˪£ğ˲\x99ӨтлȞ°ӣʖā|ϻʍщ˽ˠў',
                            'VΟʜҕƳӡǲŽǿǍʚҪԇӨįɥȔŗðӅƥ˓҆ſ}ƛ?ӥРϥ',
                            'ˢŲϵԕϡ\x9e³ϼΞЮûÑɵȫť\x90¦ʴшɳŦӲ·DҬM0Ɇҹљ',
                            '\xa0ƬɹƧГǽɉδˬϪȱӚѕʥɗ\x8a˫ΦωκɿѰҲЀЍDþÅɨɞ',
                            'ØԑӎĂ\x8dǟ\x7fȥėËƏȝȬʝɛj´˱ǍƀũŸӼɀǦɊ÷ɁΤи',
                            'ƜΈK\x92ѽӏЌͿњƠǄMƙʤɡA«Е˻ʪƸӽͺ#җ\x9fȒũƪĪ',
                            'ˀАѻӧ˭ԛ˱xÛĂƽѻĆǯĜʭʍòҤͺӇ\x9aʊƠҡ©ɏϢĲē',
                            'ɋìȜɠɂ\u038dEǅȝǝʖ˚ԃɅϯƲїŭʥ҉Ş)˯˦¢Ɛǩ|ȫĢ',
                            'ϵѾʹӇЇ҇ơҗÒҗ\x92˸÷ô˓Ƚ¹ъς˄ǷѴ˥ũʿŻˁΏԃѕ',
                        ],
                },
                {
                    'action': 'LǋĮΈЎʎθΗʾǦ´ЧǝԛȭǗzͻԗϨ',
                    'resources': [
                            'џЈƍŧȞԚήȽƔǡҵɟ҃ƎEӘхʴɅƄ\x86ĝ\x8dЍǇōЗӾɫǐ',
                            'ϵ¶ʊǆ\x8fĭ*ĭǑѷͻĢŨíүҐ8ȎƯɺ\x7f҈iɱMӦѰƦԣѮ',
                            'ǖƑϱǣĉλԀɡÐӨϡǆǿɵÚҔɖѐŨϑĪDǓΜԠԍƑë»ԕ',
                            'ΫөǢъĆY&ƯϜSиřιɪϤɢəɮRƒѹˉ΄ɩĞԁӛʰó\x9b',
                            'ӻҩǺԞӆӵԓŌſʹřқоȨфŲԙ_ƙӜ\x93γǯ WӦπҬˏÍ',
                            'ԅœΰΰҺǢ·ďÌ\x81Ӹ¡Α2҆μΟʥëжӄȻɏΡ±҇ϪϪюӗ',
                            'òͱ\x87ǋƶbƌɠȼӖ\x84ƊЍƟ4ƖšΣúçЇƒ˄Ӻȋɮӊ',
                            "\x85ΖҁƌЊ¶Ƅė¹Ыƺ'Щ*ȇыǦĒȡÒͷTɶƊСóÁǚѭȂ",
                            'ƪĀѿЙǯԐɮψʠǊůƣ\x84ƹăƷŶȢѢlȎӧθќ\u0383ʹ\x97BРԖ',
                            'ӜŢýϻˎ˓ԛɹǓˌϯîΐʴЛԎϝԌÙ˞ĒʊʖŔ\x85ѝӀ\x81Ys',
                        ],
                },
                {
                    'action': 'Ңˎ(σźĂǮʰϢƝҚĮǠЏʪԁjƅϸҨ',
                    'resources': [
                            'ȖˈҦˈΎϓσˢλǿөŚјқ˃ΞʨҰǯ¥ȢԂÑњµČѨә˰D',
                            'ѿη+ˆҬĄįĆїϜɳǐұˎ×ɿЇęǃ#NŽґюӬť˶ӆDɼ',
                            'Рìȼԡ«ň´īËͻϝƼx΅ȷϨȐ\x85όѿҊǃ\x96ƈӮöӃӺ¿h',
                            'ȕϩЄɚʬ˹ԉїϬVŁļǸǺԡгЦƄgфȷƃӸŕƆžӧ[ҧҺ',
                            'ĒңżƵшҶ˫ъìƞǍŜƆԟ˺ɁΰҹâˏԛņąлħүάӾ#ŭ',
                            'ǊԫҚ\u0382Ӓ\u038d\x8eσXҌЧŧƑƪȂǫѾʨȓɹŰӜύӇБѳȂȃȧσ',
                            'ə\x7fŶλҷƨe˝ĒʕΖčвǡΖτˁȘȨΫʑцı\\Ȓ!+ļ˃ǰ',
                            '҅5ʴÊȌAŅĽҀ\x9fĺˌ\x87҃ӌOÎˣÔȨkâӣĞӄʡϧǢʌӻ',
                            'ȖɍÍĨӮʻLǦ˜ɩΣьʼʒ˹ÑʌɣŚĥ(Ź(¢ΏӖƄøƞӺ',
                            'үπjƅȏ/˶тĵЪ®ѝ×ϾΓЯђʮsǣĀUЍȈЏ½˰ɡԋC',
                        ],
                },
                {
                    'action': 'ËƥĞԊ҃өΕԠιғƫҒŦɎΓ˳ņǠԨŢӤο',
                    'resources': [
                            'Ϸƫˇ\xa0ȜӻǼ\x85ΔŮ˅/Ǆϩ\u038dЇѢӭŤԏЀŽɷѰƿԊçѤDʹ',
                            'ƳɬөҬԩϲ˧ѩеϾîӚԔΚȘɋč˕˩ƸįɍʧɤFԉƱǄ ҝ',
                            'җҀͶŤȚρ9ĶȄˬˆſƀҴǞƕʟǖƌūØɓȇһӖɅІõӱƵ',
                            '\u038bŁԎǀҝԢſʞʹыҫňĮŋХňCǂѡ\xadèǃzъçƀa×Ǆ)',
                            'пԛɦԝǊǭ¬ŢŌˇ³ǍФϱёӤŶUо\x9cƄҬ±ˮЙϜΗȾɽԩ',
                            '˓АԇėǐĎˤuϘ/ɄȥӰƶʁƶˏӝŖĩƊ<ԈȷƃǬĲ˽ÇȚ',
                            'ƂʗȖĹԋζҊʞőϡѷ÷ʃǘŦԌňПNźӿİǑмȐыҍѭPϜ',
                            'Ľ1Ԙϵŧʗ҅ĥǡÈÙƠ҇Ӧ%Љњ΄<è$¾ӷG·ƞǤƒ®Ǚ',
                            'ϔǨΊˎѥPӚуȾŖχʃÉʔ˪ӢμQΑËҴлԓӐʰЄԈŭϰӲ',
                            'ʷøЌ\x8dе˧ȯVй\x9fϢǱʱÒŧĹȑÊ\x8fŹхʗGʁŚʣӉдǯƵ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ΜÓЍ',

            'version': [
                -3634024290980716382,
                -27323690736922029,
                -287254740865734357,
            ],

            'location': [
                'ξ',
            ],

            'runtime': 'Ƭ',

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
            'name': 'Ȏπ˔ЮèҳŨÚпǄ¦ʤʛ+ʎÙȒѽѫpϝđîĽ\x99\x8bƂƓĻǱ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ĳƚˌ',

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
            '$': 'țӡьƩ¹ӫȈǒжĄ˶ȽΗаǜʙ\x85ɳщʾ~¯ʅ\x8eаƠlÙɲғ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -6794630637679829763,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 652432.6320918512,
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
            '$': '20210301:152841.526499:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ħԒʓςʂǲФǦøśξΨʴƙƤаØŤЖϯǏ҉\x83ӛƆȯӻ\x9eɨв',
                '˺SɩĨ×{ЋƊɱƢťӦʘӾ/Мǥ\x84ƊѨӒʲҕɑĂͽĵǟє¢',
                'ϘԟǔʟЪŀ\x9bƲăρБüÀΥȖņşćŬ²KҏҕʦҔԑԡʵʨҼ',
                'ҤɺÄЭʦϥԓˎ;ԩwP?óʢǝǏˏɿˀϢЛȟӳˊƻ÷ŘŞƳ',
                '˨ɄΟ˃ѧė\xadȲĊĝďԀȼ\x89͵ԫѡΨӷɽiǾƹȒǠϦҏѯǶї',
                'ÍѫǬʐӤĂʟȞ˺ѥ\x9eĦēԈӿĐɤĪғƱӊԩϺÑаԭӬѷͳо',
                'ӻӺƇ/ǎћɳ3ǨԄƮӁӉ˕ėϰɚJЭ˔ĎӱЮlζȴÎď˗W',
                'ʙǚȅɉʘɨϱƛY,єâяԏƿњ¤хƿ-џѤʛБӕИǦПbџ',
                'ɊǧΨ\x8dі\x98˳ʹæͶ˹σȠgưѼąɶŘΟˆӼ҉ѿţěƴgŮŋ',
                'É8˛ˬъĞGȁkŎӁ˘Ѿ\x98ҷ\x7f˨QѸдȂЮɼέ+ɤɱɯЂǌ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -6407974104094061861,
                3527565464017040910,
                -1478330777069201956,
                3556954355380040440,
                1834609484983904778,
                8935030386102728973,
                -624287656937195760,
                114917487508953033,
                -2680952965511018432,
                -1060113131836406436,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                21988.183601528683,
                309327.3780395819,
                -40646.474922792106,
                355670.5574754681,
                946799.8963806324,
                500227.71417391114,
                567137.3190409526,
                557597.8140578537,
                732873.2530854851,
                414922.0560649345,
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
                False,
                True,
                False,
                True,
                False,
                False,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210301:152841.527365:+0000',
                '20210301:152841.527379:+0000',
                '20210301:152841.527387:+0000',
                '20210301:152841.527393:+0000',
                '20210301:152841.527399:+0000',
                '20210301:152841.527405:+0000',
                '20210301:152841.527411:+0000',
                '20210301:152841.527417:+0000',
                '20210301:152841.527423:+0000',
                '20210301:152841.527429:+0000',
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
            'name': 'ƅӔӣƑʮ˅ˣǮʈöǒД\x8dųƻ³ӡχƻųӢŚ˅˾ԕҒķĀŽʰ',
            'value': {
                '^': 'float',
                '$': 123949.67710997135,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ɇ',

            'value': {
                '^': 'bool_list',
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
            'catalog': 'Ӕԡĩ˩ɛŅʭ϶ɨȦ·ɬƠ`\x85ЖЬЉёȊԔѣÉϚ\x86ͿˀĪӐ΅',
            'message': 'Ћ%ŌďƐȢԋͽԑѧδʩόʺʦΞȁşΐΣAЛЬӝЦɎĄƴΘӁ',
            'arguments': [
                {
                    'name': 'ƳӹʧӉ˹ȝЙ?¿ȀжǟҚǝpʄ˩ϡŰ',
                    'value': {
                            '^': 'int',
                            '$': -7565458570091141959,
                        },
                },
                {
                    'name': 'Γ˝',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        False,
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
                    'name': 'Ǯʾ\x9aĨңңѕÈɸϴϊҀǪɕĝŮ҈ǴбӟѲ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210301:152841.524626:+0000',
                        },
                },
                {
                    'name': 'њұӃҌЃ¯ǤƫФ\x81\x91Ҽӣ˰ŴŧǾͱЎćǤµ\u0381Ϸԧ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ÑĖöϊθґϔƩǤϟ>ΏɴÔӭȓ8¦Ǥʬō:ɪтР\u038dżıӯч',
                    'value': {
                            '^': 'datetime',
                            '$': '20210301:152841.524911:+0000',
                        },
                },
                {
                    'name': 'pпş×ӏħ´\x84ѬšΞ҃пŪӥȀ\x99þ\x9dɴlȏ{ʈΝÏԖӍ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210301:152841.525079:+0000',
                                        '20210301:152841.525096:+0000',
                                        '20210301:152841.525104:+0000',
                                        '20210301:152841.525110:+0000',
                                        '20210301:152841.525116:+0000',
                                        '20210301:152841.525122:+0000',
                                        '20210301:152841.525142:+0000',
                                        '20210301:152841.525147:+0000',
                                        '20210301:152841.525153:+0000',
                                        '20210301:152841.525159:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ĳʵŰɀĔȹϥЏ\u038bҍĔԖϙĲʛϫÌƍ˽z˴ϔuϮ!Êϻʕ9\x82',
                    'value': {
                            '^': 'float',
                            '$': 461259.28077306773,
                        },
                },
                {
                    'name': '8φĺϋΘǼљȉɌԞ˅÷OС`ˮДόĈԭȓ',
                    'value': {
                            '^': 'float',
                            '$': 946579.7191565719,
                        },
                },
                {
                    'name': '\u038d΄ңºҥĩĖûԒ˶é˓ϸԧϑǜɆwĀÁ\x8cԎЏ^βϑƔƐʃҋ',
                    'value': {
                            '^': 'float',
                            '$': 695203.5579037209,
                        },
                },
                {
                    'name': "ϳӨǌȎΙӥǹкĂ'ԪʢÆ˾)ϸɲªˌ¯˯ѓϰżѷɌĨď\x9bʅ",
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210301:152841.525842:+0000',
                                        '20210301:152841.525857:+0000',
                                        '20210301:152841.525864:+0000',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'іʊ',

            'message': 'Ȓ',

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
            'identifier': 'АJǍҠȐĬŠȍΩ\x83ɥԟӕ˛\x82ƚΉĵ`ѥɺɷqĚǌƥĬɮп\u03a2',
            'categories': [
                'os',
                'os',
                'configuration',
                'internal',
                'network',
                'network',
                'internal',
                'internal',
                'file',
                'os',
            ],
            'source': 'ӹŒўϼçҘʵ:ɛѠHƈ˹\x91\x88)ϸϺƄϽƸėƜӻӅǢ\u0381ӤʐΑ',
            'messages': [
                {
                    'catalog': 'Әͺ¾ľȁҽΦȂ˥ȋȌǾʻєŋϘöŔŊУ¦ϮΔϹ',
                    'message': '0¸ӬƢϼϖŇƃǥƏōș`ēԘҤɻЀѿʯо\x80˧ӖʱäԖȴЅѰ',
                    'arguments': [
                            {
                                        'name': 'ȯ«ζг"Ñ2мѴͰҥǍĚѪ[Ͼ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            709489.0252554045,
                                                                            264930.98934640957,
                                                                            257138.31209031685,
                                                                            852099.837788427,
                                                                            206880.48040501075,
                                                                            310231.09729559463,
                                                                            585655.5699751404,
                                                                            164213.76930327155,
                                                                            321496.18062630773,
                                                                            975380.1995676253,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ДӧӤƘǌuˌŔÖɃ¸ІCĂ3Ȏѡн˯юσ£ҨϚŖʐĜѱ\u0378δ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3133673344659105455,
                                                                            9110857664490430478,
                                                                            -7315137787832467695,
                                                                            -712537797159313876,
                                                                            -2943974904989931602,
                                                                            -4467799162145640905,
                                                                            430414304086116002,
                                                                            8205679720390424674,
                                                                            -1265816363390280675,
                                                                            3042721892591192886,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʾƄӡ\\Рȑl˫Оҵy\x9eԊ¼ʹȋƢλ˦һљԜҚȊԦŀ ˕ΰȆ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.498392:+0000',
                                                                            '20210301:152841.498407:+0000',
                                                                            '20210301:152841.498416:+0000',
                                                                            '20210301:152841.498422:+0000',
                                                                            '20210301:152841.498429:+0000',
                                                                            '20210301:152841.498435:+0000',
                                                                            '20210301:152841.498441:+0000',
                                                                            '20210301:152841.498447:+0000',
                                                                            '20210301:152841.498453:+0000',
                                                                            '20210301:152841.498459:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǄˏƑǬƓQҾɲпŋƲӒJŐϗ\x87ƴě\x93ϘʜУŷǙыεʇΊҢң',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.498702:+0000',
                                                                            '20210301:152841.498714:+0000',
                                                                            '20210301:152841.498721:+0000',
                                                                            '20210301:152841.498728:+0000',
                                                                            '20210301:152841.498734:+0000',
                                                                            '20210301:152841.498740:+0000',
                                                                            '20210301:152841.498746:+0000',
                                                                            '20210301:152841.498752:+0000',
                                                                            '20210301:152841.498758:+0000',
                                                                            '20210301:152841.498764:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ғʨƑϾñěgгƛχЃʗʶΐǿÃРOƭQΉҹõǤΨɓ1ͻҶӿ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            630943.873089326,
                                                                            512035.7547482323,
                                                                            476040.56787901884,
                                                                            988949.5414363365,
                                                                            867032.1030364975,
                                                                            941605.9887721101,
                                                                            281878.1431390944,
                                                                            169708.13245155173,
                                                                            62863.26860404556,
                                                                            -95352.43827404088,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÀΫԋҠw˟CgүϗƋɔɊӼ˳ǊԐƱÎεΝĝÕǚʯ˭¼đôϳ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 748968.7610197783,
                                                    },
                                    },
                            {
                                        'name': 'ñǢѮɯԁΧȲswżĒɘ)ҝōΓ˴œϤн¡ˢҼ/ιϘΗLέū',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΩʑúɶʰǑԮƱӍ˱Ѡ\x99ΐɱϫѹѳǗŞȜҫʩΧ¤ƫΐϧɯrѽ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            821531.4571924106,
                                                                            370923.9626474819,
                                                                            311134.6160248799,
                                                                            652799.6401243528,
                                                                            285369.6425263761,
                                                                            273630.7670282104,
                                                                            22644.045904202765,
                                                                            477446.55723868555,
                                                                            724431.2949805087,
                                                                            923483.078434371,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҧϬΤkŕƪϺϒƄýˋφԐћ®\x9aԜʽòӥÛ\x82Σ\x91ǲ²ňӲőп',
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
                                        'name': 'ƁҙʚҌЉļяƓˢ×ˣǨɄģӑΉƺҙ;ɮ\x90Ԋǘѝƶ˞ħĈ˃Ԥ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӲǾǌƈµήɀĸõˍ͵˕ƾΗ˹±¯ÛɚϚҍҴɹμҲëӁɏɦα',
                    'message': 'λЈʸPѵσąӐÞ\u038b\u0381ȪшҔуϰčŞК˓þ҇ɇΊË\x9bӻƥŅƚ',
                    'arguments': [
                            {
                                        'name': 'ɓŕҒȚ˂Җ«mņԓωƥҩΛɼѭȳΩȭʈƚȸͿmѕɏǠĚcÒ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɞѢˑÍɬ¥ȷÓѷζʷ!',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152841.501064:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ăȍ7ΡɛψđŔƠ΅ϺЕæŒα*Ţ»ǱC˒Ȑ;Ǎӭ\u0380ԍƳӼș',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5224567974996011894,
                                                                            -9114388750487216751,
                                                                            3836267850608305319,
                                                                            -2197267585206188810,
                                                                            -9023448740272135472,
                                                                            5140502684795062533,
                                                                            -5698647003251009090,
                                                                            -8409946884380987838,
                                                                            -8036778884673165622,
                                                                            6782849554202167343,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѩϓqЖ˔Ӹ]ʎԨтҙԦϻԧȚӋϥÆţѲсѿ-ёƪӲҽPȟ҈',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɠȠȡɴŗЭŰόΖбV\x90ȸĘӈӞмηļȅ[ԕøҴˑΣϙɠǤƈ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ҵǒ[ʩғ~ĔϴҍҢϱΪŰN¨Бȴ¥ɮͷɪTεĤǟпȮŴǽ9',
                                                    },
                                    },
                            {
                                        'name': '`ɍѯгřΙӠʛĎϢɳЁÔ\x94ƣτπЫȆÙɯɒσ˧|śΞƶɔ1',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8153153850837128851,
                                                                            -3296091733893453173,
                                                                            -5951066414188832137,
                                                                            -1273270576463450720,
                                                                            -7853469624907026541,
                                                                            -8948173863019360318,
                                                                            -3581999950054633097,
                                                                            4875792468841152631,
                                                                            1349277019270467207,
                                                                            1491555785120533204,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϳi6ȸɠеŎтÜИgτ¹ǏĔԝNԏe҂ԀƏЭϩƗʇWţ.Ĺ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': 'ШŤĸkȚȏzЯƀϸ(ѴƊ˺ԭӥԖ˯Ѓ\u0378Ƹ҃ÄϗŧɽǌϚ±ɦ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152841.502378:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÄLΌıĒӎ\x93ÝϞƊǱѹϲϦеʓʍѨrƢʵԖ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʅ\x7fƅУʉ¾\x8cЃЃӃʭԡψùƋ\u03a2ċǻԣƿ½ΈѥΥΞԖѐӥªҊ',
                                                                            'ϐӗ\u0379ѯOŸĢԢȻϺԖɫ˃һɞʘɝȫɾЫЛŌҘɣ\x86˫˃Ȯʶ.',
                                                                            'ƋԍĈӚӽҾ´ыԄԓȅʔѨƷф«ʎİӶ)ė¬ĥȠѯFaϞԩű',
                                                                            'ӺϝнɎԖб.ԦŁrł¬ʙїјщӈԩHҩӥеЫɎτѧήƿƄȂ',
                                                                            'ȐҖϓϹԗП_ČҾѓưʉ˟wɂʵйŽѧԈÞwøàԑԒѰζё\xad',
                                                                            '͵ӻ\x89ǚĶʄţϛǋ#őʟϺӒɵåÕĵƦȳӌԭȯҮǅԀÄ˾Ь˄',
                                                                            'ƫ˘˲ĘƱʪȃӒ»¸ɢƐɳVxłʈ\x8aѤˬ˂Ҋԏԉƺήbчʤν',
                                                                            'ǸòҾχȽ¢ӝ¥˂Їˀͳ2ȱƊЛȠ\x99Ū~șȴ¿ȮǐˆфÑ҆Ρ',
                                                                            'ξҬЍéԉȉƃӖζСЋ҃ƨǳ˅ҏӶʘuǍʙʫӉá\x98Ӆέʷ§ǲ',
                                                                            'юłsͼԦǄƜвҼҕȦҿÇëѩϐȠɔɔ\x96О&˷ғǮȐԈƔϬđ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÓљҽůņÐд',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152841.502998:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': ';ҿΎқʍТӌqxů\x8cķѢ%ˑɪѫcŢĢAӹҤǄľg\x88ȫӞϰ',
                    'message': 'ȎӑƊªɐȾďCʊˇΡń\x8dҍŷì\u038dѦÄǔґђŏԭǵ˓DҼϒη',
                    'arguments': [
                            {
                                        'name': 'ћ\x86ёҜɋ"ųΐϔžæϪѝˮŊĵӢΩöŚӣѻӯöůăˑшеǤ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '=ħțӃǜÐԉєѳɨϴːβĀǣјŎςТԤéҍѫѸҪÙ΄ǡʘу',
                                                    },
                                    },
                            {
                                        'name': 'ΪњȵÝӃŢťˆͿӏǏYĠÐи×ͶқԝѹЁŌ,ɷ˪Şʛēº9',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 943732.3318756362,
                                                    },
                                    },
                            {
                                        'name': '˾ǿ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5362103354286808921,
                                                                            -7442345468418417336,
                                                                            7477300363106194750,
                                                                            5334113357743485558,
                                                                            8096696956889412118,
                                                                            2546374483658174345,
                                                                            213794118020050008,
                                                                            -1498830612702724256,
                                                                            1257423472151117375,
                                                                            1617091348521611388,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҿїӫ&{ʘξÛcєЕƬ\x96ĺɏ¨сϔdӨɃǓҫо,ԙŠϻæ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152841.504208:+0000',
                                                    },
                                    },
                            {
                                        'name': '˸ȌĲԬʃҽğзɡŎңӁ˻ΏϡpӚѯ˖ǭțҹXːΊǍJăďҴ',
                                        'value': {
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9cǔ¢ϳ£ɆϺҞʛƚр˩Ҹɒēƨ¼XƋͷε\x8cǅԩÆ&ΐʰҟѼ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            ":ɾϩȦʨb¤Ǽ\x8fӻӯʢʴÈΎɒŐέӹ;ЫϋȚÞϴʷǺ\x89'с",
                                                                            'ҸԕŨφěӠYʃсԂЭŽυċRӱȾƧˮҿ÷±\u038d˯ΒΫԃÞȦˮ',
                                                                            'ςİ\x91ӷ\x80GˀâѪȍĔӜ˙ɘ\u038bЍȻ*˵ǽԕӯűҬɊ\xadƏ$ϼŰ',
                                                                            "ҍϯ;'А˽Îρѷyśв,ƏēѪӆ^Ъԫťϯх\x9bɖǿԩάÿ\x91",
                                                                            '3Ӽ\x9fЍƝşȎĉъʗ+ϊ%Ȧˮʼϰċ\x8aɮȹСѠґѮύɁ˵ƻƧ',
                                                                            'юĦӁҨ҈ӵѕԋāƏʥǸԐγƦ˗¯ϼƭƺ?ƄŐ~ʖƞSɔπѥ',
                                                                            'ϴҶǎČøE&ϟԓĀ`ĵȉáπʱͿʀŧўƗ\x9fɪӗhŰˡϊȟȟ',
                                                                            'ҙӴhƓƳɼэ=˘ӱǍĩʇɃʜϐ˾τӱ\x99ћʿˀϗ?ѻбҢѠα',
                                                                            'ԨʇņӐөÆʳːш҇ӡ\x8eЖʛсHΏƪȘƻˋįøɎϮҵȟʘʾБ',
                                                                            'ϐКҬUϤiɀɛҵОƲѷ¹ƣӏĨƎŧˇшśόƝŜȜўқњɽЅ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϜαŰԎ˸\u038d¥Ʉ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 926520.321458095,
                                                    },
                                    },
                            {
                                        'name': 'ϏɆϮÎȐ˲ɤƙӸǤӉJƫȪȉԙQO6ЗÍ0#\x8b˹ͽȦ¼Ċɩ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƕÑ˶ҭȫϽΛЦʂǝ1\x7fϩɕѷС\x7fČϿdʘȻѴ˴πďӵΠúĶ',
                                                                            'ͰʤʦԪԔ\x98ʰ\x81ƍЅˀә½ŝȨјЍØϩϗǨӟÊŘѿӽʁϡD˵',
                                                                            'ıӟ_Ž½§ƞj˫\x9cЅżΕɀшԢєίӢġɯǻ\u0382ĵќkύҨҚ\\',
                                                                            'ǝ±ʹŜѿÁʻʔΟρЃʐu©ʀɊřϡ?ÎśϋӌŽΨȸ\x8dīȸ˼',
                                                                            'κǞȻ˃ÆŔʺЪіɡ˅ĥμΙт\u0378ǱгΈƦϙԪ`\x9bɖƶʵяʵʊ',
                                                                            'ҷәϱɊʈ˞\x8aĐϘъÝʶ˸ı¦ë\u03a2ǈ0иϰʺϺѬӊɨͱЊǟϽ',
                                                                            'Ӥ\x8e¸ОҼԁˆ˚ӧʅΣɿѶ҆ȱϫϊɹ\x9f¬ǔɞҿ˄ɠʽ\x8fзɕł',
                                                                            'ɧǠυfÜͶĿΨĶÞqԮҏģɌԀǽӍÍƔÑѯӨȂȯȆΊ>ӰɆ',
                                                                            'ѫÛĵǤəǊƆΝӉӾȠϟΗʡԁӚѕ˗ǻӂˁǪȡ˂ʦȮ¥ԮМϯ',
                                                                            'Гє˼ҧǧʇǨLÁʱѢ\x89ǎѓJoƳâ˙ĘΓ϶Θ2ł\x8bӉɯϾˢ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԏ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 207811.4269669262,
                                                    },
                                    },
                            {
                                        'name': 'ӳӉȐƽНɬԫÞΞ"ԨĉdȘӷɐʈƩŹєіɎʜPÐ¢ϹӘýƿ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            521934.3015461345,
                                                                            350242.9545500899,
                                                                            778161.2281601299,
                                                                            450543.18455015833,
                                                                            650059.7139640448,
                                                                            697583.8097941513,
                                                                            808781.7501569426,
                                                                            862647.3591617704,
                                                                            1199.169198843112,
                                                                            179871.43391912803,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȚȩRʤ$ʅЛș¢ГɱҊāşҫȜѫSʒϜɩxϚŸģ˒ӥΜĵ҈',
                    'message': 'зɼ`Άʹӗ˰ǠǢԌƂÜ˙ôȽζӪÕҦŠ҅ʼƩɨˮ҆ԙϣ@x',
                    'arguments': [
                            {
                                        'name': 'ͻǶǟɘ҈ɞӺχϽƏГ³Ž',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ÝԀǉĂȅдʠҁ)πǙǤʤԈȲʝӚɨ\u038bКƥВԟæöԈʕˁʋп',
                                                    },
                                    },
                            {
                                        'name': 'ŭѧvҖЎʯϚΉѨȖˑϋ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            761813.3022042187,
                                                                            651266.4170183927,
                                                                            805351.1817812042,
                                                                            103843.24128083905,
                                                                            839511.7320132164,
                                                                            665533.4661732786,
                                                                            370957.3264382564,
                                                                            554798.3451089397,
                                                                            -45233.540000220986,
                                                                            19329.452548553352,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Łlщɪ6ɴϠȺƃоǩȮÅÜǿШʋǙӂΣӾϧȘӑоǛdѤŻǿ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            450372.02563409193,
                                                                            793627.7842697853,
                                                                            920892.2810353593,
                                                                            933444.6459419003,
                                                                            917630.816036839,
                                                                            451008.8167822866,
                                                                            388537.7381218684,
                                                                            323775.17944980215,
                                                                            233580.73809197935,
                                                                            855656.4244716001,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϪҜџԍāǅӗÙĄÔÇ\x81\x8aҗƶ˽Е˽˸ҠĩɏƧѣ҉ȂʦòԌʭ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.506913:+0000',
                                                                            '20210301:152841.506928:+0000',
                                                                            '20210301:152841.506936:+0000',
                                                                            '20210301:152841.506942:+0000',
                                                                            '20210301:152841.506948:+0000',
                                                                            '20210301:152841.506953:+0000',
                                                                            '20210301:152841.506959:+0000',
                                                                            '20210301:152841.506964:+0000',
                                                                            '20210301:152841.506970:+0000',
                                                                            '20210301:152841.506976:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɪRϻɣÒ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152841.507184:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϻйӽ\u03a2σϲ˃˶ƄψɝƹʛɣÝҏƘħЫ2ǊɽƫɠӤźЩ˻ˍî',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.507328:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'LŧЖ¹²ˤŕũԏ"ʀ˼įҶȴŃĵǍŜłӀͰƨ¹ƚѱЗɭԋӤ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
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
                                        'name': 'ҢʤƚζҤҕȩɩŝ´ɮjԕ>ѴҖķŭƩÝϝ\u038dңӨ˰ȅF˧īӻ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1885880727533247062,
                                                                            -4280913075301349068,
                                                                            7239129596449332287,
                                                                            -2876202063692958011,
                                                                            -2163630358479530808,
                                                                            -917685651086869322,
                                                                            -6592828220522319463,
                                                                            -2602805098963614888,
                                                                            8487555788294810341,
                                                                            4921991252963954925,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ы¬[ѸѺȒͱȡǞĩŏɱéȻȓčtaўʖˉƩƭАȅԧ\x83£ǲ©',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.507981:+0000',
                                                                            '20210301:152841.507993:+0000',
                                                                            '20210301:152841.508000:+0000',
                                                                            '20210301:152841.508006:+0000',
                                                                            '20210301:152841.508011:+0000',
                                                                            '20210301:152841.508016:+0000',
                                                                            '20210301:152841.508022:+0000',
                                                                            '20210301:152841.508027:+0000',
                                                                            '20210301:152841.508033:+0000',
                                                                            '20210301:152841.508053:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'љȣέŲ¡ӉȼΆƣҗƌˀȳɜFͲɐǘ\x98\x7fҏЯɠʱЈΓ˩ѿȒƿ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\x8aÈʺӿӯBʮȊ¾ǫ9ӑƠƺɠͳĲɹуŁˢğυÛmˈśń\x8fε',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ÌЀÿЄƛ҉ǱʬǣǈΘ\x80ģˁϒԨƺӟ5˹ҿΆȃ˫ǺƂϑǵқӖ',
                    'message': 'ȝҘζʷȊӣƹҺ\x96ӾБ\u0379ȈŷѢeˎӡü˹кЏ\u0382ԓˀ΄ˀӑǓǨ',
                    'arguments': [
                            {
                                        'name': "ў\x9aǱύϸ'ԍғѯԆȘǐԥƯɷӿҳȸ\u038dǞ\u0380ƻîǭīʟтΆŨӎ",
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ôȇЏʿɆΖмȸ¡έʒȲˤҗƷǌǹΞЅГ{ΔÎѥƳîňѢ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7279312780088158459,
                                                    },
                                    },
                            {
                                        'name': 'гˍƫҫр˵©ƨȎmĺŘÓǗƂʗČƷGĂдюśҳϚÊ`\x8f˦',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 171697222593438733,
                                                    },
                                    },
                            {
                                        'name': 'żҝԄˣʇǞρ˔ɑrӔϣ\x9d\x89ƚˍԮGӸӏԌӰ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '˕²ŅqǏŀП<Еŝγžʌ\x8cѡϒϩӉϢƈпϪф',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7750934998529237246,
                                                                            -85013126374923760,
                                                                            4312004368476651265,
                                                                            6379616113969847047,
                                                                            2490331180619920078,
                                                                            8412824910395574278,
                                                                            -696098030805183005,
                                                                            8872598381652200356,
                                                                            -8102251206423465372,
                                                                            -9093099271368933494,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЫƗеɓò˳Ѹơ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.509727:+0000',
                                                                            '20210301:152841.509741:+0000',
                                                                            '20210301:152841.509749:+0000',
                                                                            '20210301:152841.509756:+0000',
                                                                            '20210301:152841.509762:+0000',
                                                                            '20210301:152841.509769:+0000',
                                                                            '20210301:152841.509775:+0000',
                                                                            '20210301:152841.509781:+0000',
                                                                            '20210301:152841.509787:+0000',
                                                                            '20210301:152841.509793:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɊǝрʭˏͿÀ\x97Ϝ©\x88ȥƅǹ˕ȀvÎҝӡҝ\u03a2ѡ˶ŻβʰƱĦĶ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            275293.73126909795,
                                                                            905594.8395388331,
                                                                            153036.46158365268,
                                                                            884899.510952435,
                                                                            382845.68677987735,
                                                                            34110.33891088047,
                                                                            890037.2600454587,
                                                                            681865.7092362574,
                                                                            538126.8578369888,
                                                                            387325.91143151757,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӆ˷ʢοӸǖͳSϰԓɕњ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.510299:+0000',
                                                                            '20210301:152841.510311:+0000',
                                                                            '20210301:152841.510320:+0000',
                                                                            '20210301:152841.510327:+0000',
                                                                            '20210301:152841.510333:+0000',
                                                                            '20210301:152841.510340:+0000',
                                                                            '20210301:152841.510346:+0000',
                                                                            '20210301:152841.510352:+0000',
                                                                            '20210301:152841.510358:+0000',
                                                                            '20210301:152841.510364:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÚǴпtԥğͲ\xadԤʐXѴɚчʽҼБ҄Ï˺ҟѽиʘͶɡìSƘɣ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '\x9b1ıºj»ǙɄƬƼ\x99ƶѠԝԙύӧŶО˽ЄӬЖОˏӅʌȾÞя',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.510757:+0000',
                                                                            '20210301:152841.510769:+0000',
                                                                            '20210301:152841.510777:+0000',
                                                                            '20210301:152841.510784:+0000',
                                                                            '20210301:152841.510790:+0000',
                                                                            '20210301:152841.510796:+0000',
                                                                            '20210301:152841.510803:+0000',
                                                                            '20210301:152841.510809:+0000',
                                                                            '20210301:152841.510815:+0000',
                                                                            '20210301:152841.510821:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': ';ŹˈӘȺΒŀӰϽɱЦΗÕϻ˦ƒԙѷĭ\u03a2ԟӐ³ӉȵӡɽїǜϨ',
                    'message': 'Ϙʙѽ\x96ǪtʵѲǅígËѯ˵ƸҐ\x83ԡӪʧΝ˼ӒĀóƤѯȐîǺ',
                    'arguments': [
                            {
                                        'name': 'ɞŋ´ƁӣźɠƢКӆʠ«ʥϔɏ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -30070137608454099,
                                                    },
                                    },
                            {
                                        'name': 'íȫȬӱΒмƎ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ƥ\x9aǂԩтˤÑЪϱϪȫʦćиƷҖĬǢäúɣϬ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 372303.3251221397,
                                                    },
                                    },
                            {
                                        'name': 'ВɓĘǇǎ˔˦ԉúъΣѸuʅњűŰɩʃԠêѩƅŞЩХæҤȡӅ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ҘɭŏHӷț1ҕʭĶӁŤ˫ŷϯ\x85x=BȩԑˇŦȮʙŀϨÀɱı',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.511915:+0000',
                                                                            '20210301:152841.511928:+0000',
                                                                            '20210301:152841.511937:+0000',
                                                                            '20210301:152841.511944:+0000',
                                                                            '20210301:152841.511950:+0000',
                                                                            '20210301:152841.511957:+0000',
                                                                            '20210301:152841.511963:+0000',
                                                                            '20210301:152841.511969:+0000',
                                                                            '20210301:152841.511975:+0000',
                                                                            '20210301:152841.511981:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'IŹӢɢұфˣϴ\x89˓ҤŪʛʫѿĿλ\u0379³ŇcƍŴŃѮˏŃЍ˞¦',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1098615483036058141,
                                                    },
                                    },
                            {
                                        'name': '\x9dӅ˒ìЋӃďĂ϶ʫʊįʆҫȍǩHȾŸЮԟ1ɓԚxǲǷȐѽ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            15254.30044722317,
                                                                            320902.0850570382,
                                                                            186066.93790601712,
                                                                            522750.4820347993,
                                                                            141249.36096365488,
                                                                            660623.0278200265,
                                                                            316001.4678899855,
                                                                            48006.497656317515,
                                                                            299303.25770336244,
                                                                            103774.23243959111,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÀгͰΣ˷ǄѨͿ\u0381ԚÅʈΣБԭɥԡo˱ǲʳЩәȴȌ҃ҟԨűʾ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            471783.79734685854,
                                                                            691243.9011962927,
                                                                            411949.8839128209,
                                                                            973651.7536023692,
                                                                            23774.68788099065,
                                                                            677359.4483784171,
                                                                            224838.24869083433,
                                                                            468621.180293667,
                                                                            305987.18190063594,
                                                                            29723.27449492787,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǹ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2230239473429913611,
                                                                            -3755557154990781590,
                                                                            6130257128793923410,
                                                                            -8378848085695127513,
                                                                            -6031390750863424548,
                                                                            -6235870955374439444,
                                                                            4019359195943435753,
                                                                            2698291706698084208,
                                                                            -761434694353767043,
                                                                            6741703495060922624,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˝ƎЦπҤь¤ІӍν',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6293988065399847330,
                                                                            -2798703863892879935,
                                                                            799244565606744448,
                                                                            4067936468463283651,
                                                                            7223882176181067314,
                                                                            -730170679822476552,
                                                                            755828483722620997,
                                                                            -4443341425291213525,
                                                                            -1788975293629823458,
                                                                            3779211609092749573,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ӽɜ\x87ƮԎϹȝJĉАJҺŊӾơf˾tĽ϶ҋϘȜԗΒ˲ɱԟӞӛ',
                    'message': 'ǕҀмъΩȲμԚ˭ѾӌȞɦùʊӌʉ˞ҽӐƭ˰ȟfɦÀǔђјǥ',
                    'arguments': [
                            {
                                        'name': 'ʙǃϪƪǀӦĦʦ˩Ĵĵ ӠЇƊσɝċ»Ƴđ˄ԏήȨoʨέîÉ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152841.513711:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ŴҦɱǘЪȚ/ø8',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1637474749710511611,
                                                    },
                                    },
                            {
                                        'name': 'ƆӒŊƵōHúɚ=ϖӖҠƣѓÛϏήńѓҽͳȣŕ\x97iͺɜӴŇ¢',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.514012:+0000',
                                                                            '20210301:152841.514024:+0000',
                                                                            '20210301:152841.514032:+0000',
                                                                            '20210301:152841.514039:+0000',
                                                                            '20210301:152841.514046:+0000',
                                                                            '20210301:152841.514052:+0000',
                                                                            '20210301:152841.514059:+0000',
                                                                            '20210301:152841.514065:+0000',
                                                                            '20210301:152841.514071:+0000',
                                                                            '20210301:152841.514077:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˉĐ_ȂЈśxøӛӑƋĻϰ·ˋɹȎȁӰѳѼľΡρǋԇōϥӁо',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152841.514324:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ЈǂȇƺɢȯáϏŰϭ\u0379Ǔ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ϋňǗ(Ǚɕ!ԎΗԅ\u0379ȕԮҍʳ1ǉ˅ɍɠς',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8767946696074528388,
                                                                            -8627115326951714198,
                                                                            -2582323017471863905,
                                                                            -2063521559874835423,
                                                                            -505069450286898751,
                                                                            8422574185227128122,
                                                                            -1140506766331685889,
                                                                            1232515632020530324,
                                                                            4495409446363897505,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǦaÖŵǋԣȥϖǌ\\ϧʴ-ьѰ˵',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2895865808817264619,
                                                    },
                                    },
                            {
                                        'name': 'ǟqӨǪŖ˫\u0383Ů*ԀÞҎΏɒԑ˵˹Ю\xa0ǙϭŭЧѣǗγ˴ƿά˼',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 881951.7489972297,
                                                    },
                                    },
                            {
                                        'name': 'ǰЈƊ°ŖŶΈĔѥĨȠӾԏőϺ˟яĨϷϮ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 749775.1021921189,
                                                    },
                                    },
                            {
                                        'name': 'YżTԨCļƬү´ȨȜЈЖҺÐɣɚӹ˂ψ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7129615857185690159,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'рȱĻAСªĉξȱ¶ğ҅ӮώЖϕʴȢĸ7?h\x8dàвƹӽӤ3ӵ',
                    'message': 'ʊӊюҼεˣĹɖ˟ơǤċʖyКɱԗѢɢԭȤԐ\xad΄\x9c\x8eNϻĊя',
                    'arguments': [
                            {
                                        'name': '\u03a2ϯѬлэҭĩƜǎzɟœҼПɗ\x96|ʞΊƅʤůОǦԒřĊ˫ϨӔ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210301:152841.515690:+0000',
                                                                            '20210301:152841.515703:+0000',
                                                                            '20210301:152841.515711:+0000',
                                                                            '20210301:152841.515718:+0000',
                                                                            '20210301:152841.515724:+0000',
                                                                            '20210301:152841.515731:+0000',
                                                                            '20210301:152841.515737:+0000',
                                                                            '20210301:152841.515743:+0000',
                                                                            '20210301:152841.515749:+0000',
                                                                            '20210301:152841.515755:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŒӟäŴuçЭδǫ҈ɰˤıˬȽǕˡƎSӭк˓ҡƱϾϞГ±Ӽ:',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -785702688147464150,
                                                                            5433362342808722862,
                                                                            -6169978662358145085,
                                                                            -8205971573015414373,
                                                                            8306735465424224844,
                                                                            -8977362750829084692,
                                                                            -7828351302174167277,
                                                                            -407047329050317159,
                                                                            1977814670411270933,
                                                                            7917566416152165814,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϢźʪĊ/Я ëʨ\x93ĲƬPϤ϶ƷŚуİҏ\x86ӻī\u0381ˍa\u0383ΉƄʨ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʭTiťÚʔӴљľǽ°˸ӤѤbϰЮĜˁĘĴͷзʕśʛŀѸƥ˙',
                                                    },
                                    },
                            {
                                        'name': 'ǴєǒѸʯȆ\x93ΰŅϏԙʳŵϮ˞Ȓʲ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ҹӇƹVϚРuΜř͵ѐ3åĜӝӨ®Ɔ\u0381ƍё!Ɛå϶ϘƯýҝԪ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6513781522031425716,
                                                    },
                                    },
                            {
                                        'name': 'ϜǺЩÕÆŭŲ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 325151.63702706265,
                                                    },
                                    },
                            {
                                        'name': 'ɤ\x9aӧʪÅΪтΞ\x9fŘˏ\x95\x9fƽƶǶ\x99Ϙ\x86ƒ¤ŕ©ΧӕОƎ\u0382tЌ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7400566504976858841,
                                                                            -3164718212648331691,
                                                                            -4999157936238435495,
                                                                            7540967383976292762,
                                                                            -1171205825820591007,
                                                                            7077509189029077969,
                                                                            3952131685313210985,
                                                                            -8871604870380347335,
                                                                            -183128698912334586,
                                                                            -6864146805554472560,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϦӰĄʋύɏзΙ¬дöәӷà7ȧѐĴ\x83«ԏ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1863588109290531785,
                                                    },
                                    },
                            {
                                        'name': 'їӲƌ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            393557.34847842425,
                                                                            493657.9638621912,
                                                                            448012.4022063315,
                                                                            802965.0274810898,
                                                                            929836.1690826765,
                                                                            304246.53093334206,
                                                                            52533.82318098756,
                                                                            538332.5616896854,
                                                                            95115.44184298455,
                                                                            268634.2622211205,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ю\x87yʜƎӪɞ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĹҲҘʚƎџ´ʫsƻӑϐάʐĵͿɼŷİĴԛĒg¹ΥљiҔѼ˹',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ċȢ҃ɵ#ǃÕϗЊǙҵΰεɅʭҥʪӀɧҦǻGѹΗŋӅǏ×ͼȬ',
                    'message': 'ŉл˨¯9ԟǱӁÇ\x99¨ɗǈӿҞʗ\x8c;ˁǟϞôНΆͿ.ϡɚ\x85ё',
                    'arguments': [
                            {
                                        'name': 'ɢењȠ҅ƬɍJ',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŧŰɦ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 839795.7634243928,
                                                    },
                                    },
                            {
                                        'name': 'Bɥɛs\x80Óɵѭ{φ\x82¿ĪθΒ˯\x94ʴɺē³řʗӃԈӁħ\x86ɩђ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152841.518303:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÇҤRȭ˚Ȳĥ˚ɺǁԧÖɕȘͷȢɅгÃːȱҢӱϰȦғїĪøȨ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5684862402876623192,
                                                    },
                                    },
                            {
                                        'name': 'ӏƁɔαtϴǉɃйńϕÞAϩ\x9eΪŲѺͷːсԢɘңßƚǭ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 851874.3201924695,
                                                    },
                                    },
                            {
                                        'name': 'ǎɁĿȕŃ*ĒƾӕΡKŌоѽƔ÷ӄŇƹǂӿӝɅ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ҋѵơƚ5óµԣǀ¢~ԇӍ5ʻӊŠɹˌιȅѕ:ЉԌǨ\x8bčѕ²',
                                                    },
                                    },
                            {
                                        'name': 'ã΄ȳȣ{ŬːGaǱɥЖαʪȪ(',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȡÂɚ6ӽĖiƚɉſŋŽõŰʠñƛİыӼƢʗɶҙŝϽĹ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -44774.050172634015,
                                                                            266369.3195021851,
                                                                            -59463.25292319926,
                                                                            832359.4821834723,
                                                                            652444.2433067102,
                                                                            763641.871988649,
                                                                            682165.2246366742,
                                                                            184499.8426839118,
                                                                            484606.3165827227,
                                                                            583136.4724125102,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΟȘӎǩʹĈɶΕϺŪҀжħԧі;µ\x86\x8eĴϫʶƁƒǉıʖġҗє',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            436320.8302851254,
                                                                            613146.8942737121,
                                                                            488904.19919495936,
                                                                            932867.7864069738,
                                                                            316919.80543121573,
                                                                            356029.59139271925,
                                                                            216914.9080235978,
                                                                            745240.9268762595,
                                                                            -92217.82607792411,
                                                                            569005.12154536,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'оʙиПBȨΥЪϡԅң_äιϠԭɨƘёΥԑԈƁʶυ{Ԛ/ĘӐ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҸлкʴŦð҉ǀȈíϹȃĭɄēѾȇʦʓɮpȦʾϸĶĬȖɎ¥Љ',
                                                                            'ӊѹԖĴǹƫВCǹџŞτԘȰ\u0379˺ƨǹ&ѼĀȻ˙Όэ<˪Ơ+ũ',
                                                                            'ҥ˫ӾπҦ҈sԮřЙŌʿ:ΧЛŘŴƇÛҥǳƠȑƛǡˆɒʥȘԜ',
                                                                            'ȒñїˆҶԍʮ%ɮĉȫeªŷЭƏȟƽψƝϥɳûǁ¥LаҶԊƅ',
                                                                            'ŪӘŤɠǞ\x8cȖҁЬAԚВćƏƖ\x8dŪщΡԏďĳđԜξ\x99ŐʤǛɭ',
                                                                            'îЌĆŌϺŗϤƯһ˾Ū\x9bàӗƞəûϼӌɈb~Íˋү Џ\x9dſƥ',
                                                                            'ʂtȊҰΆɤϽѤԑθŝĶĝЪʘ}ĴǐːԦĺԟәðǊˏ˅ƩƎ/',
                                                                            'ҭ˥ԊŏυӖǽ|ĔҡκĦщѩ½Ǯľøʂ҂ρ¡àǚ©ȜϽӰӺк',
                                                                            'ʽʉЃƵȱє˹ɤ]ɴϓĐơOʦø/ǈp¡Ŭ΅ϳ\x9eþ}y*#Ͼ',
                                                                            'ԂиВŭʿɄĆșʰǚƆ;ˢ\x84Ǎʰ³ƈљ˶KҢІԕʱϧŝəЧɯ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȳӵҊԍ¤ξθø§öɇĺԗòƴбЖǆĜξПǊƶȫЫѷ\x9bȝÖȟ',
                    'message': 'ϏʛÒɓȴīɓȶôĥz\x88ѱ\u03a2{ɀϓ\x93ǻм˫ƒ]УȖϳͱł\x96ƿ',
                    'arguments': [
                            {
                                        'name': '&ıȇØŏ#ҪҾšú\x83ϟƐαäRŷɇΖ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 264147961819047185,
                                                    },
                                    },
                            {
                                        'name': 'ҽňzȹΝѠƧ˽A\x85πɨdƪǴΨϼɻŮԞ\xadЮłÝǖ±ɖΞɑљ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152841.521251:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҀðӦтΩ\x9ecԜԑșȩǼy˕ԝʤȳʘƸҀą´ԒɈ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 604462845635184994,
                                                    },
                                    },
                            {
                                        'name': 'sԨ\x82˟«',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2275622063469016243,
                                                                            5813656786443593347,
                                                                            -3499174961994397657,
                                                                            5759143254093516677,
                                                                            3561861730010357603,
                                                                            703536470351266002,
                                                                            2315007266457579861,
                                                                            -2004454405776146344,
                                                                            -1603023118833321669,
                                                                            6062454014764142686,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͱ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            518926.7481571032,
                                                                            805534.2650601327,
                                                                            637604.9954096532,
                                                                            763452.0733179398,
                                                                            173917.26655953046,
                                                                            380937.6862731601,
                                                                            645407.6759428207,
                                                                            502995.3767991926,
                                                                            38892.271165525424,
                                                                            699194.7263646738,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƒʺÇ\x83˂',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210301:152841.522003:+0000',
                                                    },
                                    },
                            {
                                        'name': 'µѧ˵Ԯ¶ĘЏŊӧԏ\x90ѯͼŃ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5963806712208969084,
                                                                            4044495559183136965,
                                                                            7492456778697133465,
                                                                            -6142470999802314729,
                                                                            922045349958090447,
                                                                            -7707179335359242602,
                                                                            -3208640717474179911,
                                                                            2832220536781602994,
                                                                            -1802788791982807620,
                                                                            -3130681176878570502,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƩȧҜӏL¬˩ӴøтОɄНΠ\x87ɭ¤ӈҙЮˋυӺԇӱʯMDԏ\x81',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3378745398361858097,
                                                                            4165760383876451346,
                                                                            -7801512945672670464,
                                                                            5671172072652913355,
                                                                            -5047620875666334414,
                                                                            -4733160699019289372,
                                                                            -389038365513081723,
                                                                            6382259958181721861,
                                                                            20495249083337404,
                                                                            -408121319486839184,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԦŉӰyÒΖӠ\x85.ӂͼǿұԖ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 803112.5171798568,
                                                    },
                                    },
                            {
                                        'name': 'ӗʮȊȭ˾ОѤі',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1130585267379450514,
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

            'identifier': '@ЄӎͽЍ',

            'categories': [
                'access-restriction',
            ],

            'messages': [
                {
                    'catalog': '͵í',
                    'message': 'Ϙ',
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
            'name': '҈Ǣε˂ŕˠøϝϽ҉τǂȎЅɁșȑӄʓğȷǪӯȄΦОщУҾĤ',
            'error': {
                'identifier': 'A8ϷѮ˟ĭțƮrԙҚňљӱļĒѝÚsѸй³ЀˍԜӷԉʟ~˷',
                'categories': [
                    'internal',
                    'file',
                    'network',
                    'invalid-user-action',
                    'invalid-user-action',
                ],
                'source': 'ΗԖԒҶѡŒϟĶɶǠ_ΛǏϣøϋ{<\x89ʂżqŃηːĉ\x9aδжɂ',
                'messages': [
                    {
                            'catalog': 'ÅӔϚϬϬǓӬȐҰƵȽԃθ˒ǻȾƊӕåӔτ^ӯϨλԌŔή÷Ӫ',
                            'message': 'ӉӹʵϮѵʀ\x89ơқņίɶŋäΡʑɃҫ¡ʛǮ`çџĘԒ\x844Дĭ',
                            'arguments': [
                                        {
                                                        'name': 'ԠξłƭӓbғӿÌѱəK',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȐЍ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԝҡˣÚн˅ˋӅhͱОα',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 703669.8768413259,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÊΤ˴ЪӵΘǀ³ϩҾӗǫȌ˨#ϸӑʿ˷Æ\u0380Ҡ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϵӰ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƽЛ·éԑӔҀԦòФ\x92СТΠǦȝѯUζ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҥϑ˄Ȗŝƿ˞ϔưŽŪǞǨ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƣͱȻϸɵĢʗRǔǺ˓ˑÃωκ¡Ԡ:"ȃϓƏԫ«öϟćƗ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '©ϕˈƫŻʊԗӅ˖\x7f\x97\u0379yќԕªƳǙǡЫϺʖЂȥɟɁ\x95]τԀ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'áȚǮØˀϜƇѩӗͰ\u038b*ӶŦ¸ӗ\x829ΐʄɿõԥӤԥŗԠ\x7fҥɺ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1689291846170597082,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǻoĂÝ\x91ϜɄϠƅȧũҤɱɠɦ\x96č¾ɷƎҙƜÒΥÚԚˮˍƌȝ',
                            'message': 'ґНJʈѝҖ˛҉ĜͶÚĨŠʒ҇ĔƔъĖԟʸҞħĖɝȝ\x9cħeσ',
                            'arguments': [
                                        {
                                                        'name': 'ϛ7Ʀԇz˫˴νʮәе>ϏϿӶtԕԊӒҭ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЀXÛԭɈƶĆѠӸэҾ¼Ѩɬ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӟ\x8cʅŊ\\ǐϖћȲ\u038dĥbʘʸȋϸŉЄЁӮmǞ¡˶²ΦІ˙ŀň',
                                                                        },
                                                    },
                                        {
                                                        'name': '˳ΉŨɃǶӰԊʻӧеΖδǶТӄ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2348938564730594203,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ğϳӝÍҪɸζΈόǐƢЇϔāȆʶĳBϣӊǕøԕԚȱ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 280035.1268409636,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӣǌ\x92ΛͼĤп¤ӘӆҌӥ\xad¬ýüҶƗȌӄǝɑȓΎˡêΡʉӶМ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '<ΰжΎǈg',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѫ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӃɡoƇΞƬɜʘ¾ҬɄXɭӸǸɲͿɦҲԥěˑ\x82еҐÂοlõù',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 799512.4760028691,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʕϚСĉгLȆҧгŅϕǠ@M˽ȰĦų˟Ş',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĉӀŤƍU}иɤ˟ǰɪ\x90ģƆϞŷҸ˻ɰͲ9϶ʴэИϮΧ_W˩',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӊҗƎģßťĢҋ*ȄʴҨŌǒԛ҂Ȅɕϛ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԍĞѠƐĭʭÛĿƢѤǬ\x8cΠԞMԄмʓhӘƝʓӫ\x95¿ıёϵ˹;',
                            'message': 'ɡơʆǑӬƐԣӋӟ\x8bʻ˂αΚ\x92ϻЯȂĝƑΛÒôҘσƁǙȕΏƔ',
                            'arguments': [
                                        {
                                                        'name': 'éΡԘǦĨğƈ¾҂ɻɲ>įªɂʩʬěӅүˌȥϋ²φ˙ϟ2ȉѪ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'aҴʬѳƃ`Б*«ɎťнӴΌԖѓK˞Ԫҵ9Ș×zҐȢʚԝ҆Ǻ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɾoϹŞɩwŹјĶƣʇķЦŪԂˮ\x89VΠѐѽӺÌɎɟİƍЙ¾',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.482297:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '"ϟ˛ҁϧɞԝ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'FCdϛǕҌƱ\x9bŠӟm\x9fӖРʸҩϦФɢˆ\x8eԚ΅ΠċϷʂ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3065191734740184958,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʔǡΓӢêŦΘɈŊαţ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.482752:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˠcϸŠǠΞŔdΦǩkϤϢЃɞY\x9cBĕ"ҦĘɤӘʧ1ҿԃЀ\x9b',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ёƐ˸ȴ҆Ӗ˦ԦҝȓОΌ˨ԩƵԁ˴ҋŢϓίąƽƊŔкǉƇvӄ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 493750.61333641096,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ŵɾЦȪͼӞƨ¥ŝńϮòξĿΑҿȴ\x8aӡ\u03a2ͿǼ^˷\x95ƄˇҋĄҝ',
                            'message': '©ɐđϞӜʾӸҰ<үĎ¸жшʖΗχȄ҇љʯʓĔѨĞė˜ВҐ½',
                            'arguments': [
                                        {
                                                        'name': 'ӽđЄ˃ҼϝϨҁíÐҒЭƪΤͲǺɒĎӗ˸оŏϹѵғØŝĺ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'gѢŖżθʸFѳȠЩĊɺȥʪË˾',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '¶ĚҁċΪϧԉˑǮʮȃӉΧΈĜćʂòԧӷӷϷӾԍӱʮӴʂЬx',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʆΉωɅҺz˘ğЍиϓuŗˣЧ¶ʫȆņIѠρɕúĕϣͶΊŚύ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ı˶łd\xa0ŢWǧԌƐѳӘ_³ǭ˽ǣƷѻ7ʕÆŮҳϋæι˵ϼѠ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'әƦҺJΫѝțɁĄćƚːπ˙ǅΆΣ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 275671.66160079074,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʚ˃˙Ήϒ˨ǠZ0sѐˠҬ˰яӇћȨì·',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '÷Ħ¼ϧ(.ćЧˊɃβҘȕѡìϡĺ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'č˼ɛđ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.484586:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѼJͰȫӏ\u0381˲ϿЮԣĐŶɇ@ĬʕĮөȊƊΧ\x9bŋ\\ӑƮȈӮƥǐ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŋёĳӾɾƭЁõűÌɊϖ΄ΦЉɌшɻÓӿƵΉ©dõǑЙČʀƟ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɈÞ\x9cľɤͿˢǷĐɎ\x9e\x9d#ΫīӉƚȥfКҀДȤV\xa0ň«¶ˉϱ',
                            'message': 'Ěγ\x82ˬōΫңȄԄҘАϨӘƊȏЙȻ˾ɑp˷εъǞűʫu\x99ǊΠ',
                            'arguments': [
                                        {
                                                        'name': 'ƞ¬ҽƲ˂ķ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8424885236316695484,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʖăǿԣͿ\x9bŗϧîȰĢōŧɑ˭ʳѿӬӍϠτ\x8dΫЮЂĸƵƽʗȦ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΏζLâӝ\u0381ΝßϡΊŧ{g˦ǟςɂ³˶˽ϸT\x86їUŢĔԍӸϣ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x89ђŝԕȲ˭ņȵфĤΕДʍӎ²ģҦ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 357334.71398725966,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЗРŎɴ5ūǀТԎãęΌϏÇҏŲĹʴþԩ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƆмͻͽϝϦǜMɶҲЄϧ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˒iʶ´Ǻϛӟһû\x83ϒϰƯˮȜҏΩԦI\x8cȉŶĢӎŚԖɝԤĘʤ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʒ˭аǠԡԪɿʓѿŕψǷĹЫӥάΒ˓',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԪǆˤЗʉԘź\\ŖɎԥ\u0383ѦąÞɷѡ\xadҍøůGӯdԀĊƝϳʴΘ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'IԫΞɞέҬ?ŝϒ˦\x9aҍϟЌǹРT§˄ц¾ӌtˣʺǸųǒˠӴ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͳƃƷ\u03a2ΔħȋųȇˏȼƮɂÚԓƹƄ\x96ÐyȨƤÂҜɇȂțϱϰΑ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3216009355976272452,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɷ{r`ϴŗϳɋŇˑҾ˰ªǏǐŤңÑ˾ģТīǍƹĦʤ҆ЦHӼ',
                            'message': 'Ưњɮƕ˓Ƚѕłƾʝƌĉ¦ˇӭƭʟ\x8bƋϯșІr3Ȕ.ϣѸ\x91җ',
                            'arguments': [
                                        {
                                                        'name': 'ӃɽɔϪ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'wӻŭϤͽĺ˨ǧʥ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.487149:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΝŲŇăβ҈½ӇFăѠƝȶƦρƲҞǨƺыÒӚѬǣºÎi',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -14914.902782589605,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѯ·ʴ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'άρɅǿȞǖɚɰѐСЧǘȣԉ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҮѺΓıʃӫӾӉΪǡŲʡ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ОóˤǎȢɩк\x99ԫӪǫũӹƽĹˠÀѝĈʄѫ«ҷ˸ӻʕ;ıǸϱ',
                                                                        },
                                                    },
                                        {
                                                        'name': "˽ӋƧűˇ'ˋьĤѵоʀʾ`Ӣq\u0381з³GƝȜӾvЕϑ˕ϭѕӶ",
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 329648.5960268956,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ө+ӉѝĲХНƍβȽȣсԄ¡ɔНL®Ӥİ^Ɔuϒ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʊɸԦΐЕ"ÿʛº\x9dɣ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.488518:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӧɌ·DÍѢԉόϤхƫ\u0379ˆЧæϔҶрұѱʖΫM`ӹθÛƙNė',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 371646.2517367099,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƧƪÛʱи\x95èãԝÉѹĚҁҨǒԎĴêЪќħŗȀǕҷҺОьϖІ',
                            'message': 'ȈʈĶҧʼɚœӑȇԘˮӊĀŭĽɜèˌӼðӊ҅ʳȸǞӮƣҌЂΰ',
                            'arguments': [
                                        {
                                                        'name': 'нȦʾȪȓ˹ОǿQȣŅκҽϞ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˥ŴƶƢV\u0378~ŚȩʗǴ"νƹĈ"ӐȔЇϷϿˁŶǳǌőƐѦņ˒',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'šІѥƌ˃ƪԢϙ©\x86˽ӾǞ¦ѼӚȡχʜȖɕʎЮԦԟѷЍƢҚ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 634034.8644403277,
                                                                        },
                                                    },
                                        {
                                                        'name': 'zɦǂА',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȳēïɃӀˇȨǜ|ʘĞQʱrϴԃѓ]ТυɊԝӝǙгɺгΒҥÁ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƵҙɹƑˢǂԨȭ2μǀɝѸǳ˞ƊƄKɗԋ`ėιȎҨƪώШ]>',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʩɍӲž˄Ƌ\u0380\x9bеӪ҆ΆԈÒȧŻƚωͳ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 40913.50142462333,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҴɄԁӄȲȓÎȅԊbʷйŠшVù',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ήԖƈƥĖҜӯԑԘѝGë\x8eҒʯË',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.490386:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ůķӊͺЀγӃȅƇҗJɤӫԇώµjϥ\xa0ԧЕʐƊəȾϑŕϬĚД',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɥ˽ȓKӁԃųȇρ;ȨԪïΏҕԨħϖɭ.ѳɪчΎяХ˝Ԭʬɸ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.490666:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǏȼӔɸǯ˥őÐǀΤƛѥìĔCƣoҙшэ«Эɬԕ×ȝŋмȥƧ',
                            'message': 'ô%ʞŎЄҫÌ¤ƊdˮԘƦĨӜϠãͰяɍҤϿμɔͳĦĬΡȦӈ',
                            'arguments': [
                                        {
                                                        'name': 'үӉŏȣ΅˰ʼ˰Ќȴ×ʬǂgȘƬĠʄĦƅ˽ƘàԂĦˢҮϠ&Λ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƮӢΪǂ҇ȉ҂Ŕлđ˷ϒ˔řӋÚƽ˔ʃǫӶŲĘ¼й',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŬřŘͶˁъ*ԏĬԙƘͰҘf<Ő',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5247663122881696258,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǗƚӸȬȏǐ`рƙϔz¿ɇȣ\x9dmųѥȣϊӼȇØČʩԢŽԜӈƄ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 880242.2396145167,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԫǷɭÀÑçӋЬĂҭùӘ˥ŔɵhĽ9оǿ҂ŷƣÊɥȄıǠˇŦ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȦǮȎҧǝЊÒƵƙѠ˭ҽԫV+ΊұĢWσϡmљǧ\u038dύ\x91ˎǖ1',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'νĴǏðϏŢPԧ\x9cπȋbӜʉʖзŦҎ˄L˖ʥ;¸ΞɾʋlʏӀ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 496929.23108669836,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӼγTƗRӕȸȡԆѷ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 595462.5734733591,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϣ·бħȌƹ˰ӹρѥ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.492244:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǉʺ»\x91Ҹ£ʱʉϹȚĔrįҁ±ȫƛ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǖʘxůљӀXРҟȫȿԞ\x97ӥԑʉЍϢÝǀɟ\x9aɓԜđƞʋк®ǟ',
                            'message': "Μ+ưȥβɜӮН҇ʹTБƦëѢɐԥʽ'СӦ¥-\x9bƛҳƠҭɻҁ",
                            'arguments': [
                                        {
                                                        'name': 'ȒͿɥÆҁțÍЄȴÅˁӰԂ˾уǸǨ˦\x84vҨҿǂ˺ƜˉϴԤǎľ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԃЀ˄µθƸũǓԇɗșʏQϾΏ҉2ӧ¿ҚOƋϣ\xa0ϾȊŤХ}ʎ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7629513709068728789,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʇŸ!īҤȼ¶ť¼ʩШͺƖАѩĄ«ƻȨȍɧʊ\x98ӨƖͻλԐĤΑ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȫĆϿȇɃǱϯ8ҀŬ©ҝī,ΔѼκɎпƳÄŌ\x99ԤƞϰýǘӠҽ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7071862762583692249,
                                                                        },
                                                    },
                                        {
                                                        'name': '+',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7209160681012040229,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ү˾ŖƕÒϬΗɲƜʐǯӛρӳ?ǌīΔç;',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2365775761507352117,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҨЙʶɪJΆ˼ԙˏǶȀƎƴлͰ4ɣѣéг',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 858608.3650961657,
                                                                        },
                                                    },
                                        {
                                                        'name': '˥ȧӲơ˟Ɛӗӗ˪ɻ˧ϙѾԚдӑȧǳǖӔǊʍ˖.ϒ¤ѵŷʒȄ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ŭʺ˻\x94ǵƯ\x8aҶx]ЮХӫȾѫ\xa0ҔԆªԉЅƧѱ\x8aԃ˸0Ҁѓϓ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΣB2ɥÝʥÝ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.493926:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ђτ˄ϟǒ˃ЉдС©uƼ͵\x8d2ԤӈˎҨǟтөĜǡƱѵɔҌƲű',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.494069:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'шЯƟїŚġԙɆǰуӖƷÀPѰӉĩԊŗϝ`\xadAЈѬԚŠӍȆǽ',
                            'message': 'zĎÁӫªʦǎΪІŚǃχΎÅӺɓ9χĄʀƣѬǕΣɱ#ԃvwŉ',
                            'arguments': [
                                        {
                                                        'name': 'Ҙȯҹ9\x9cәħʫŘқǵҵŪҗгӘŵ\x94ԁˎĦº҆Bŭðʗ\x89ͷˆ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'яҼŖĹßϔӑͽљǺ9ʳȭςϐɦʟƯɍĔ҄Ǆǆ\x9aЯԠӷ`Ÿӯ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǖΡŐҲЖ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210301:152841.494610:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȅ\x9eЩϫ`ʸCҘ˼ǶɼУԄǔ·˯ѴϓϫԀŀ"ϯԋϚ6ŜОŖF',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'µӜRӞ-mҤÿԛȨǜʢʯ˷ҹҩΒ"ԍźӓѯɲңʶƉƨѨʊ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '/ĽğǷγƉU7ά\x80ʢϖǼɜ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʯʍ;¡ʣҨ\u038bƄɲϹ7ɯɰɖŭѪѫӨӧ\x9d',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԏϊôǴΔĒтeƥԆӖqgѭɌűӴԘЕ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 510877.0223523311,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x80ЯΑͷğәň',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϔÊҝǺȓκʥɪHɻÈ%ϕ³ѮfźУ®ɎԂǱ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŲÌWƣ\x83ίIϛӝƚӣɞϪɯ¡ǘ\x8c˃ɩǧ˥¹ʿάŒʕǕэˇϓ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'пǆʫҋȢȧȑϝХšŎ\x8aҖӜМÑǰǢɪu҃ĥϹͳȆţșƈԞǄ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "otȠ҅Ҙěȟ\u0383Ɉ\xa0ԂCјԒÎŷȏʢwҘ˟ΤҥԌӛŷ'čԉř",
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

            'name': '˰ӀÉ',

            'error': {
                'identifier': 'ªΘҲ`\x8d',
                'categories': [
                    'file',
                ],
                'messages': [
                    {
                            'catalog': 'јǲ',
                            'message': 'Б',
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
            'event_id': 'ѫǅϸʉӳƦАʗтɸѴӉȈίԭåΏҀȿͿȐӼʢƉϴӲЙƊɴԡ',
            'target_id': 'ϰÏȤǇǖǳґü´ɻԛΨ&ɳâ\u038dԇʚÃΖϡӟάѢńǟε˜Ѽˣ',
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
                    'event_id': '\u0381³ǔƒ+ȰAŌ\x93ϑěɨϿÕʮġƢȺň\x8dƉǓĖĳ˃ΡÛʙgґ',
                    'target_id': "ÅAΣɷӛ\x9cO$E'е#ЖӴԁ¯ЅɈ3ζŝƟəȘʧ×,ÿŀʕ",
                },
                {
                    'event_id': 'ɩǢćϠgŝÈˠCöŎɒȸәĶƝ ҴFφDϘµİķÐ$ѼĮл',
                    'target_id': 'ɖĠϊƾʬ=\x97Ȯкпɷ±ɓ˩ǳƏЪàʴaϗˬ˾ӄҔЌτĒԈЯ',
                },
                {
                    'event_id': 'Ơɋ\x8f÷ů©Ƽ\x87ЅƬӾ2ўȿˬŊĵ΄ʔНψҖϹƅmʹг]ҫƙ',
                    'target_id': 'ÒЬƚÃǉūЈĭďʡ\x95ӎĄ ɨӮ2ƚÞʉ-ѐμǍÖĎάǣĂȰ',
                },
                {
                    'event_id': 'ɄȍʴѭǈċȫԇªȊϱśĨƒ¬ЩİKӯȣ}ÎΗЏѭӪȜμ\u0382ӱ',
                    'target_id': 'ŒΧƧ°ʵvßһМƆґǜҬ˪¹ѶŹƆΕίӁОɏӠǊΤӯѝҮƼ',
                },
                {
                    'event_id': 'ѢɓeӄȫŷͶҫЌpÍ*ҼѕҪӔӗђζɑӦӳȔΣˍƈøèɌđ',
                    'target_id': 'úćXΨ˭ɁΏɲˬȣѸͷń´Ώ÷ʟOԬcҁżҦўȖўӶҕ˨Ӈ',
                },
                {
                    'event_id': "ĂζηʛƖԂǮ'žȼδnƀɻrǓԔȞɔɂϦԍ\x8fѢƲ©ѳŮǛϣ",
                    'target_id': '\x9eʽӘџÊȵѕ>ɒ-ЬɼςƨҲϋӺŗ~ʊӭΗϦ^ʾ\u0383ҤЕ\x96Ԗ',
                },
                {
                    'event_id': 'ӓӰ·Ѩйњƺ\x85ȀÕωѝŕǵƹ±πʆȷѭҜӃʷµèXʉқåĻ',
                    'target_id': 'uʁҡ;ğЋǷɊɜnɈƶ$ƊШӠӆ©ɔʍтĔȫƮ§ďĦɪЬ˸',
                },
                {
                    'event_id': 'ΐƸҺӣΚ\x96ʆȭЬКĢЕȆņ\x88ĔnĵΏ˘ȗȳʦȡǝӢÒŤųʃ',
                    'target_id': '˧tĀ\x91йȃȢďͳÙƮΐϻΥǷϢͷӌԌǉχǂĭϺ&ζŷӌϏβ',
                },
                {
                    'event_id': 'Ӷҩ\u0380ȓӿљΛǪҏӿӔӼϴҌºәҬδɽǄƞͰŒҙГȝНӁѳԡ',
                    'target_id': 'qǭͺ˨ʳө˲ҮȇɕοԊϔqɷбп,\x86ƯȬμȝЁƶüϘԠŰС',
                },
                {
                    'event_id': 'ƙȆȤcŞоԫԦ°ԝΌƣň҄ǴÌϼèјҬ:Fń\x90Ī˾ːΆԡɇ',
                    'target_id': '°\x7fįϠΉ$ēĳϵҳк)ǲƦϸЏɖʸɼÓƓϭŅ˼ȶϦSǨϾ',
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
                    'event_id': 'ǃXƼMѱЬWƫ҄шиԅƳÿʚ¦ɷΡļӌéȾюʤʣϤȞʹԀԬ',
                    'target_id': 'ÍùǊϰǥ˯Ψɰ\u0381јЮԝɏƓĒȭԆ˧ħԮ:āƘϻӺˋТѹӭ\u0380',
                },
                {
                    'event_id': 'дԛȟǛɚȿϬѻƕïџȧљ\x9aγЧϕǷ\x87\u0382ɤħɏΊ/ºгĥÓĦ',
                    'target_id': 'ʔʏҕǯ\x9fåǥӺнуșрϬӥğŻӺŊɿŭȼӂøҐĒѶvăЎɼ',
                },
                {
                    'event_id': 'ǿЮȜ1ҌƄȶȨԁˑӀӾǘƇҚ˻ԉϒ\x9fˣԚԣęvå¶ƟҷƂΙ',
                    'target_id': 'ɠԑȹɗǮєˀ§Ċ%EˇɛȆԟӮɭuǥ·ȳϩƜӡĤӺŗ\x99ҩĚ',
                },
                {
                    'event_id': 'ʖѳЌ˒еÖӢǶ˄ɖϨӌʔǎѧƜЄϙžԌżáҁlį҆ȅʅϲƝ',
                    'target_id': 'ƁˁͽɟɸΏΖȠʫąӷÃȵȑҥϩЬ˭ЩʗĴϨϤӉϪʐ˒Ԝͻѵ',
                },
                {
                    'event_id': 'ČʢʔΩԀΎЅӓLÊԮǢϔnɏϓŀˢѧɘǔȔԅʅ\x9bϪУȝǘĊ',
                    'target_id': 'ϧyĒͼ˅ӷΑŹɉò1яʷ\u0378ƛʓīûΆɋԕɂҥÓϨ\x9b\u038b²҇ď',
                },
                {
                    'event_id': 'ȡӟМYѸŢuRɻ¥ѤΙȞ\x94ԤʔΠƛȴӜǱâńҸɉҌÌ\x87ŋԌ',
                    'target_id': 'Љȍ˱ħѷřàіǚҐʴГΆ;JbŮ\x8fȧΧҠɇҀїъԫȯ¦ėƂ',
                },
                {
                    'event_id': 'ɒu5rġł£ѣâ˹ůϧƘ˱4бҎŢȭʙ\x82υѩ\x83Ӡĸ)Ѡˆʓ',
                    'target_id': 'ѶBΙЧ\x85oȅɸ˨ЭЗұҕ<΅Ȳ\x9dŻCĆѩчȎ¸˲ĕÊΨĵԃ',
                },
                {
                    'event_id': 'Ȫ˄ƚ|ŸϡʆĥїāôǤ@ѱѾѻ.žнФȐаɀřӁľfȝřЋ',
                    'target_id': 'ȃИŨӏ\\ԨɗӧďЍҡȓǼϵҾӐqЮĭȿǎR\\¹h¥ҢҨıǙ',
                },
                {
                    'event_id': '×üӳиҸќѝӨǘȓ҇ӒӁŧ˭ġÚčȪxōɢÑóųÏìӹƩ˪',
                    'target_id': '΅ɕΝϷƫ¾ӪГψ8ҨżʗЍħΡȆ\x9eШOΩɈϸ\u0380λÀү?Ɉ£',
                },
                {
                    'event_id': 'Ҹʕ±ҝΑvЬσѶĥ±BǧʕΗԗѱēŖΰϘѱņɄ',
                    'target_id': '˪ďӠĆҫĘԧǱыԄ\x86Ӫӗҡp˟ҘƊ·ӿȐ҉ѕԥʛ¡éϛȜ%',
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
