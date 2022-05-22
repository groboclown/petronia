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
                'ӨçӹɠҔȪ\x85ªʙӻǰԏϫˇԫʟǑƥͳFΎƓǜŠЙȥβƱŽ5',
                'Λқ˥ʯ¡ԥɀ\x95νʚһѭҶҧÝ£~ԪƔǢ',
                'ŴʟľϻĬƅӖeÝёҙŮȪçЮҺʸÐńɃįʛάħ҆ʟчƏѼɨ',
                'ϰɤ7ɇ(ы˷үƒϴġƣƗԜЍΎ³ϫʾϔѦ\x87ӯθ\x94ˇŚӗÒƯ',
                'ǀ\u0379ŚāςӇ}¹ΎӀìˣԂʖʣçїŊƜǏϺδ:Ϊ˃\x95ç˙ʔў',
                'ϤŐƯȠԎ\x9dĜʠ\x86ӺW\x88ˆƸӥ¶±óπˮȲЅ©ҔˆʢҭʤҠӾ',
                'ϠӪĤʜʦԦéŬ˶ĖĜȚζĐ˽ȲΧϹӻʵЗ-ȎӨǇˉːҮɃƵ',
                'ѠжÇǲĪ²ʉҜȝΣƗЪιϫƶˡPʏ1Θ\x9dɁΪЍ¬Ҳà˝ĮȄ',
                'ȞаəҲҴËɤƝͽ¿ǃɔŭȃДǳиıӽáѻƢŜɹɷŇƛʓŪ´',
                '҃ǓĒэƬȻÚƧȏµĭӈͷǙҕƳϦԌÃǟȥ˸ǾЩűȰŜоωӮ',
            ],
            'source_id_prefixes': [
                'ҞԆΖǄÉ\x9bȧ+ëԧȃǊćΒǫƙɺͷ?˄ҢγЦӬѿӨкʶӅі',
                'ё¿кȖѠɻªˌӤΔʙӡѬ¬ԨΈЁҀşˍƟӌ¹ӼœԆӕЬτϣ',
                'ºþϡѮƥѤЫͶìĔѿн½Ӯàŀɭў<νdφDԟȋɴұ\x8fũH',
                'ʬhƬ˟MѩÊΡϙĻ4фηϙ¤ǓɜӍŠïѣȼαˆĢĞ¹õɯɿ',
                'ӅTаҭ3ȿȳǇЊԥςȏçȜKÛѾæԠ\u0381Чϯ\x83ɿϗŊ°ІȱҾ',
                '\x97ӋΫÞhϳȗЏŕԙӣ҅ҶáXňßȷɈYɠԢȆŐлǎĜҪҒȿ',
                'ʝӄƿèȭʃӉǥͺDŎԤÞǝҌ²ɮ\x82Ԕɩ2(ʯ\u0381\x8dƟƴȐΌˢ',
                'жϙΜɥ6ЋυÉˁτțΈˉɡɸӼӁ%ɚԂҹ¶©¨ɗӀҙǱëγ',
                'ѐƱƀ\x84ыӇ°ί҄ǆ҄ōȔҡ˩lҚѪʦÕň¢Ӂ҈üҩʟʘ(ӭ',
                'ȅϗȄŨиʄ˖.ųϾʹ«ҜԂԌԚӗҊĖ[vҬʉαʱДҋЙҳ?',
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
            'action': "ɯʓʺӅːԬT΅āɮŞēˠϙāӒҟғԤÆ\u0380ˇϴ¾ф'ѣӣƀ@",
            'resources': [
                'ıƩҪгʽӁʶŠʚÍɃʢ˯ηțİȷˡ˯ʁϧɣрǵȽτwʠцʗ',
                'c¿«φşɮԧҁϣʴɐʧƬлɒĔďȀϥȜÆřјǷΪϏӾˤĸȮ',
                'ԇ÷ѼѪҳҩѫ\x7fѵɤТɟĆˢ˟Ѭý\x9eӔºʼ<ĶZWǵ\x8fŊĨӰ',
                'чŞХʬԃ˺аʾ˖ǤϮͺТғåѸϯɪƏԎǡɸԍԓԉ˶©\x8eZϢ',
                'СЛȆҪͽҥˁІŉñȬʸŹȣԤļtʆ\xad¸ȤҿŔǓϣƓҺлїȖ',
                'Ļϋ˪ҔԬŶеI£Ϙ˾˫ŬƓϛƤӓȺ±ʄįҗԒўɌǵϚĐɤˊ',
                'iɫ+ӝΠ¤KӢǽѼи%(ŏǒ\u038dʲƶϖҎϷzħСĝ(lЈΫщ',
                'ͳλÙВϗČЄ÷ҭʭĽԆξŶΞȨˆΓҶϳѾÇԔέԑӠɫ\u0382ɮɧ',
                "\x90ʄԛáӭη%ɦҠzô¥ҢƀӷϟҼƂɼ'νԅ·ȐĽҫӹʢ˛V",
                'ʁёÙƆԆǠĜŅťƜȥʎįʕƊ\x97ľū´е¸ÑǅǰʏҟЕHϨö',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'ʰ',

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
            'name': 'бˮĻ˨\x89ˣȧԣŨ;nǒčǷĆʬҢːϑϔĄſҺ˸ĺŕ\x8a3ţȐ',
            'version': [
                -9114035667122703020,
                -6179620749312131670,
                -1365643253340202331,
            ],
            'location': [
                'TΓΉKԊһʦ!ĴȳĢłҲʵǜǢĠʸXȖǂáÆҩqǾѷҮʉͻ',
                'ķω[ȁϒzͻλ¯ÕϡѓI¤ˉƫœѝǷϊӮƿͷѬ4ġȇІʴƺ',
                '¨ǻoѦΞLô´łřǜGқŠΧįcѴ;ӽҩӢćӺyχΟT³Ƶ',
                'ƹʇëʍŕϟϚɕ˫˖ƶʹÆŋҕď˴ƻ{ˢǛáŅȇсʻ¡ƾѮǓ',
                'τѹјΡѣҌӺĐХâĿӪΦΣɱҤх´ĺƏŢǞȇĐҦϽˣϚʛĕ',
                'Ҫ;ѯCÄɍȥǕ˃вӟɶǡɭá%ϼ)ż1ѧԇȮɘІϓǪȴӝӳ',
                'īќΓƙɮѠɉԈѠФɗɥ°ϧȺʩō\u0378ІӒĨĶοʫĊĘѸɵȫĨ',
                'Kˢƺθ\x97ċˈИˢΎ˲ʵˠǅȮͰωаʂɢңхìнҪɹϪǈįÜ',
                'Ʋ%ȸðƓˌĦƂКψĨ\\ʈAōɩʏюЛ˽ҏfƺȝƉѿю\x9aҽʰ',
                "ӵÜχωΈΒϳ˄Π'ҴƱҟξ˟χHUǼĺýƷΗԮѳΖǽȗϟϋ",
            ],
            'runtime': '¤ȕʒʷϲ˞\x98ұӻ6×αԨȆϑƶěžӓ"MȭʑҾǥʶTҭԗ˩',
            'send_access': {
                'event_ids': [
                    'ҫӥԭčԒțɽːЉď5:ŬΘɂ\u0381ȶƥпƻԂт\u0382ŞʫǍ˂tѹИ',
                    'ӯïӨġ˰ѰΦӣˡϋǯΞK˒гɕžЖŽůӞɱÝʸŎΝϙɸ˚њ',
                    'c\x9fġĉƽȆéǼũǭɡɺԟɓӠҘ8ʴӴßϺȒʔ˟ȑ',
                    'uıДԫsхӌϓӀЯԛűsӫҥÕqį¯τϪԥԟЍȻȚӵͽʳӭ',
                    'ÚϳʒϥӓɫıGѤлѣЁъΜʲԦ\x90ˎǤɱȗ\x92ûҠĨϸԤƳˍG',
                    'ԥɬɸƬҡө˸ϭͱҷϛʷʗƿԚќóƢȯɘ\x92ȿʬǿԄЧӀщɈɉ',
                    'ӁƉáJȊɣԩΓϔњυȠԓ˞уГͶńͱSЅԔЫŻӵМѬĶźЯ',
                    'ҁĴșНȻˁǄŐӔμ\x99ҋΓȻӉ˩ĎʱȎçøq˥ϕĖȝɐιʝǟ',
                    'ͼuӾƖŪƢΑҾʺʗʝьӰŵ˻ŢόǾòϮäѧʀƀ5ÍϵȀбǒ',
                    'ŏŉр·\x9a;˰ͱпˮXȞ>ȐϢȈǫ˅ȂА²ȌŔȵƸɺпѥ¦±',
                ],
                'source_id_prefixes': [
                    '¨ŴҩʹɊ{ςΦνӛ҄ŕǘэȆŭ¨ǥĖҫQĲǥ˝ŃǬeҗϴΰ',
                    'ŭ<ÞΧîɐǠЄΊKɯϏѠŚԍ\u0378ɺӜɕ\x99ȸԖЭ®ē˱ƣƪҸȦ',
                    'ӂΛɫѥҳcϱЕ\x84ѢP˺ΐŔӺɇˮҀʹ¶ӲϻÄċ(ŅԀĉ\x99Ӱ',
                    'ɗԕӻʱϓӵʜÍɟгĮĭʕǼ°Ǆł˚ÕCϠԭž=ó¦®ӫюѳ',
                    'ðƸɝÜν˒ʐΑӪѱϊƅǹǡđÏҎ˂ҴTӤԚˤͱâЂöʄѼц',
                    'ӳĆ³Ǿº\x90ɾԧ£ŸёӃǕʫɇʙж˗Ҙò|ʣӊЬϊ˥КɉǄˈ',
                    '˔ǒϮƄқĤǞҾʨҎͿξ-ĭƮϱ˕ˌɾ˩ѣпαƑƯԣȉČʈɄ',
                    'ӳ҉ɀɵҾ˼´ʉ˘ʬѨŭĜӒqӊɗřЛкɉ¡©ϠϷýņ¨Ɉķ',
                    'Ǎ-ѷʠlқЇǼːșЫ˟ƍҌҜɊ˓ɮʙҭɽʙӱ\x85ҷ\u0378řƼǠž',
                    '˾ʍϘŞԏЬľǂVŷ\x8dкʼêƏӼҟͳŋΦĿʯõ¾ėγϊψǆ\x95',
                ],
            },
            'configuration': 'ϘљȥɟʈʽɼӼƱΗ˟ήʕȚΞǒâϟҸɮʢуɐѓʅƔʨΣӯԔ',
            'permissions': [
                {
                    'action': 'ϑҳ&°ΎvύˀɘɐМÛãʌǕRϳ|ˀþɪύQΐηΟƑΧ˪ц',
                    'resources': [
                            '`Ņ\u038dǥǣкСҐʠͷȩƀƐҫƜюĵΞЅ˹ρŒγΦŜӫʵúС¹',
                            '\\˓ŴҾѽGOʭĩĮχÍCŇʃϩϩ\x9a½ʙ\x91ǲҞҶŭŧĚѿѼ˛',
                            'щ9õőѷƜϹʗ1»ɨϫ҄}З˷ĭ£ȶȜʨșԣόʾȟԆ΄ȝЃ',
                            "ɻȄѫʞԣɃǋ®ƋɫlϐǗȋPʥԇíӑȹ>З®ԍϰ.ӟ'ˤӖ",
                            'ȑςĒƐԑʭ\x98ҲȈǫӜǾǿ8ϟ҇ȩӵцʃĶƎšͶŰсÿRѬң',
                            'Ш϶μҽԕЃҶŢƹĀϓŢĭáӍƔȩϗ˕¢ʚҸĻȺʂ ϑƘǾҤ',
                            'ȿˌÏНǫШȷʹ»Κ¦ΕˡǈǋÍνӷӕԋǛÖǲМҊƗȠȤƷǱ',
                            'Ѻā\x98ΞȜŸʂϽkӔέĚǝN\\ͼȭeӑƸҵώӣƱžҠǸҐӂĎ',
                            'ʹČȜƷnˇʢ˝ǚѿ˓ϜϣӬ\x98ʗǗǩǱĕȫ˔ЯƷȏϕɠϟ¡M',
                            'ʨ¡ɪˤӁb?ʧĈӠԤШʃũȳ°ĶɃ\x8aǑѡνɨϽ˫ƥ˫ƀ˳ý',
                        ],
                },
                {
                    'action': 'ӃƋлųЖʿȳʬ;љӲÐöïYʧoÇϙɰ҆ю9υ˜Д7ЕӪǤ',
                    'resources': [
                            '\xadЎɀɔɂ·ӫǩнӆ²ŖúϮÕƺӉѩѕāҒǀ˙ΩγÌʇʮηҫ',
                            'ӁʝɠСˉѭ½ɋʤЃ#ЪԢбǁϏк˔ԭЕʹԐǏƔғɃVƖωȊ',
                            '=ɥǜ&\u0378ē\x93ΗϦʇ˶Ήю͵Țφ0҇ǈʝφϯӏӋÞʼǔș\xa0У',
                            'ѤķȥƠʡå\x98¾ϺȎǻθȼю˜ʀwȺĤΚӢψοƗɗ[ȭ҈KM',
                            'Λq*˄ğɇþǮ\u0383ɮƸĻƀĝǇΰśʲЅ^ˊŻ˩³ǱȾʰ҆Ȯˀ',
                            'ǛǺͰγŷɡʑtӓѨϩǯZČ\x8bɴȶsʔ˰ĩ¸ŋŬŚNţκǎĂ',
                            'ȕѐ\u03a2˚ϧƉ\x8bȉ\u0383ΝÅӆ˗ǂӬ\\Ϧ·ĶͷќķԦθ҉Ūх¢ĺф',
                            '$ӓƳЈ˅ũī6ŶϷҌαO²ϙʬɦ\u0380ӉŢ4Lũ҉Ň¤ˀ˙ԅȣ',
                            'θμv3ϧŲǊ\x83˛ԉӴιԚǓKƐʁmŊëӤƧȹÙϡϗϦPФҙ',
                            'ǞԌɂŋyХѻР-\x83ŏɣʴ҅ӢͻșȌБơφ˾ƳĴԣƠ˦ОKʵ',
                        ],
                },
                {
                    'action': 'GȈgʪËńɿҩɓſʐÇəǩĽØл˔ѺʮέǤѼÇɲňѲΤɤȝ',
                    'resources': [
                            'ƃԬ\x96ƨȲêυÚяŚϓԁɞƺЯӎÂˡЋ˛>şƣɝӵЮϾŅԜȇ',
                            'ӟ\x8fΪȱӀǽҧƿΒÊĐоϸ˛ǚgƥŇùϱͺȨϯƙ\xadɚЮƾĂҢ',
                            'ɃϥЂƌí\\Юł¦ϫӠϫ"ĿϳԖŖХȨ\x8aņƉňӱɜȝρϊ\x96ʋ',
                            'ȝçӬ\x95±Ȳӓ҉ӉŽ˩ʌĞǫʰѬғ!Ŀ\x9e}ɩʦʼхʏń;ӵԉ',
                            'ōЖϛ\u038bΒǈԛϕ\x8aƁŮ\x83ӁŐɌ˃ϘYҋȧ¥ϔŖȭ¥ϱ>Òеή',
                            'ӸϽɟǯĐȳƙªȃŘă҃˴˼ӉĜҖ\x95˦ǯ}ɟƐȩǔȳиѐϰŞ',
                            'ӡ!ˑȥɡ»ȺͷŧŃeāȦ:ΓɌо˔ëԙƐʉŒǞéòϠĿRì',
                            'ȩйːXҒѨʈХϗƔϱϘȧǽΚǷʮâě8ӅƉΣğʪ˳ƨəԞƆ',
                            'ɘˊ½ˢëћΞѩȧȂʄɳ˛ɏƈJԨôƘӗѕ\x9bɴʍӦƐľ˾Ԏˬ',
                            "ŦŹ\x8dĴӞŶҿ[ЇНÞԎ\u0382Ħ\x9eʭʅSũ'αǭÿ˫ΚԬӎʞƽƪ",
                        ],
                },
                {
                    'action': 'ѿÉħǭҭЉͲɖρėӣƖεˑѧóĝǈ¶ӉǺђ˳ɇΠɉӐ\x9aȲɮ',
                    'resources': [
                            'ҠĜҞ\x85Óʗ³ΡƷԜΣmɌ˜˓óɟҚӱԁKΆȿ®ӷ\x9eǸéɨΣ',
                            'ϣPԉȴǥ¢Ǽ˭ΎI\x94ϛ\x9eЋϞӅӆӞϸ°ɳQɊѹϤʭI˯šƱ',
                            'ȑʗƒјоĤźʧÌƢӪŲ˟\x8bӵʁ·ԁJлĖ{Ǿӻ\x9a*ėԄЏҊ',
                            '϶˺\u0381˱ ļ[ЋɵӞIˇӟď&ǻŌцɖȹсͲԅȿŤŶǁӻʚǢ',
                            'ǙbŹǹƁD΅ѭԆі³βʵїѢɿQÚԉǨӻã˧aɩęӨЭӼԉ',
                            'ȣĴϔ«ÅҬ±ЭΜŖΡT\u0383ϕЁėûҸДΖГҎŜԫҋ\x82ʤƔ˕Ǟ',
                            'СƯŝӮϚȔύӳʏҿɻҰ¢ƈ˂\x82ƺŲĨn\x8cɫɫԒɃˮԋɊϒ9',
                            'А\u0379ЊфĮ˺ɇÑS\x91Þȁѵ;Ԋȫǫӏήҵԫ\x98іӽeɀΆ+Ӱ\x91',
                            'óEюşÚԤʡΦюÂA±ȷɎЩȾɄœe΅˴в҇Ә(ԘǖÕԝϸ',
                            'Ɖ\x89ͻΒ»ʳΔÀϋЉԐ5İίз·΄ӢѼѴɞϥ˞èўЁάȡœɫ',
                        ],
                },
                {
                    'action': 'ǌ\x90¾ɰȱƄF˓ġϽΧ\x9fШнЕZĸȩϑƓöχÝ˰˔ΡҐҴіɷ',
                    'resources': [
                            '³ϬśΆϾƝϵпұǯçʤȼ®Ŋɤ˻ȧʉ\x94ƏǉɊ\x9aǳŜǍæӀʯ',
                            'Ȅü҂ȦȫǲɱbӨӑß>˩ӀzȤ+Nʴԭ҅˅ԦƹǣÿϾǯĎʤ',
                            'ǔ¹õɢҡԢɞǭ˽ʯѲŮӬˬѨŒӺʳʝжѥǻҋʋЫȦ|Ą×ǈ',
                            'ӢŒƈȑ\x8dώћƿЉφӒƫōbαӤрʌÛ϶Вʻȥā˩ˑΐҏԋэ',
                            'ϹѮĔҏҳ_ī.ϺѥΚˌǿѷǟлɘϋĵͻşԏˌȉǵѸʽǉ\x9f\x9a',
                            'ξђƂϖʊĦǇÍˏӴXˠŽƴʼK\x82ĳŸӆϳ\x97³ƁJΔTȪȺȐ',
                            'ˋԮЋԇtѫԨюġΡϞƖһƷΆκ˦ǻӫ\x89ҫеȔӿԃðвΚƢ¸',
                            'ҰҒ¢\x8b§ȬƔcͲӠǺΏώʡҧ=ɉќǓҬԟέԝϟʝÁʚɧˬϿ',
                            'ČʼӤЎǔӋϛʒƇZĦЊȸʿ;ЅƪЦǡʦ0ɲɷΧƚ\x8dǸʰQϢ',
                            'ӐҕͺǜȹҴίˣƉϷӮңˣˍşңȘӋċ\x9bǯњї˻ƁɑǗӫ˫ϲ',
                        ],
                },
                {
                    'action': 'ӵÅūϔĸĲðĄƃϼň',
                    'resources': [
                            '\x8bұʼƛɳëȌ}ǿ½үƣ,ˁ҂юǹəқ҅ԃіͰ˸ûйѡɫӪщ',
                            'ҩ\x8eìȊŧ¶ҮƋѨʇëщǩŨϝʴ½İϱ7ίå\x96ɯǦŰêŚиʾ',
                            "˶ʻōΠˣ'tȜǐġíљʤǓȺƴ.ҿ\x95\u0379ͺ˫ҥŵÁɪț³ɥӪ",
                            'ӧҽ˺ѿϴɾǚ˪×ҡѯ¬ĭǏJ²ȮЁÛҚǞбԀȽȠԙƼŬĎƃ',
                            'ͽǓɘĮɽāǉǁЪҨǨѢɖƛōϐԔΆԣΘ҄ǈĮ˻Ҷɂ˖˭ϕ\x88',
                            '6ӔĺͿӦƩϵÑɢȣǒҌѠʪѵȘѹӼąÆŕȍҔŴǂҗύςǍ˚',
                            'ŨĈӈԩΤĵŢ\x80ȀùЫѬч˜ÏƫÝǻϷŰßÙɧ\x86ӷԕҿ¸ʴҝ',
                            'QԌʀԝƎҳǗϝӣK\x95ϺėҤРѿȤѓԪЎҠΎσ§σµƣĚӚŽ',
                            'аӶԝζˣԟǊàԠɎёӋúƒ¥\x9aƒˍβƓʚƥӈƳěϩԜǱ9ʖ',
                            'Ϟ\x87ƖԦӝÁЦɸˆӌ\x8eӽƚΛɹ¦őˬĵUȺКɞκΚȈ°ԝ]2',
                        ],
                },
                {
                    'action': 'ÜςÞƊΆˆnƩÙӰϡȣєϙıTȮC˴ɺ˞ȏùԜӯɤï˰Үϕ',
                    'resources': [
                            'ßLʠԨɏ\x95ąӗΘƨưӝſљШʗӲ®ΔŹ\x81ͶǢõӔǰĹԜӊɎ',
                            'ρɐ˺ÇΙɄÈ\u0380ԕZƛ˥ž˘ɜçҙӍӇӧԦҚҨɷÃǉӫ@˦ȶ',
                            'ʾɮ\x8aЉҤŗӷȝ˻ɈäԑɟҞъʱјǡ҄βƃǓІԉъβϡơº˵',
                            'ŊɝӽҴÍөҨШͿǚɅŶǞũϦuǲ˄ЂĈʹǯʻ\u0378į\x90Q҅ЍƧ',
                            'ɤʖѠ;ȾĞŃʹǷĶŰȘłӝ.Ɲ»х·®ʀΛ÷\x82oјɸÀԊр',
                            'ͻКǯΌђˊďѼӉņƗȆɀiԅˍǎƚÄǲɿц³ÃӀǮ=ɶϋǑ',
                            'ԛφģŤʣÎԊϩԔʥΥāRv\x81ÓĉɉǊʜԈѨƑɉɔԦȀÌзӖ',
                            'ηäʓϿà±ɸ҄ʊū9҅\x80ʡԙäԅɍ\x99ӧƔЮ\u038bʌԬҭʣ\u0380ǿϵ',
                            '\u0379ϒćВvϲɦҴѮċԎXɘǺ˟ΞĞǅƂʪҭϡπ\x90ӓɤÜ\u038bõɏ',
                            'ηǂĢ˴˷ƋÆƭɔǾΓǠϴ[ϡ\x8bȍȍί¶ӶѡҍɳҰĴϢϔȤǵ',
                        ],
                },
                {
                    'action': '1ЫϛVΚƭƷ',
                    'resources': [
                            '\x8eʠҦπƈȇњӃӶĶͻӜƚtԘĶʧԣԟԓƭηȹʭ>WʳȴŎ&',
                            '\u0383πɫȌɖɀʔ¸ŏҡŪÀWêǫʌŰҵĕ϶ǃħǆĺɲȏʐӦğʐ',
                            'ӪЭхЭх˴\x93ԀӥˏӿɉΉģͰǺøȴôЦЈƔéã°ήȦÁХö',
                            '9ǆɝǴƜПʄƫϼȫòơϺ\u0383ł˚υԚėǨДɻҁȻԏΎxĖѨě',
                            'ά+ǿԉ˃οąɼʆAфҲƈ\x90ҢŹКԃάġΜ:Ϙŭȴѡ¾ЪԒӿ',
                            '˫˯ΖҫυɶԃȸӑʕƧ9ςӮɍяњ"ˈӐɾѰȍˬȔìūɵsł',
                            'ƿĪ\x87ŘbǁǸɽЗ˄ŚėӁʏlѬˢѱѩЮÑźĸӖūȉϴÈҍɵ',
                            'ԈŝԚҭ˾ϾԟΠǁξʵǵ\u0382þǕýю\x92ȌɎ\x9eġǦґȺ°ĆǼäӶ',
                            'ϹυħˤƓŞŗΘΡþӴʆƁҕǢYλЗ\x81ȇ\x96ʰǶǉŕĈѭˤɨǍ',
                            'ǆďđΛύŲCĪȄlƠǝȵԍǺǘЊ˯\x85ŎˌȼӐЄŔԫɡţ\x81ѣ',
                        ],
                },
                {
                    'action': 'ȄԉĹǮθÆӠȮƠVǧ]ҩ͵ǙԌȦ˚ˑЌϿȐƚƖ\x8fΨņ{ӂԈ',
                    'resources': [
                            'ԇʯǱ˽=ΰʴĬÐ¢Sʐ*Òˇϸ\x86ƺ{ҷ\u03a2Ҏ\x83ϙ˥Ӏ¨ԇëϭ',
                            'ԏϝ£Ђ˳OʒάŌĖɴŠԍљ˜ЧÒɷˈƕАʈ҃ɘԎϩķцƙЁ',
                            'üÊѨbɀǁǬÊŤƻӨšȠ˴ϲʇЊxȔŬӇ˳ɼĲʟĥЧϙĚů',
                            'ϡΪΪɬǱkεӂę\\ŦʷʺϕΛҶύɆΰɱˣ\u0380҇ђ\x99Ԥψ,ΐӮ',
                            'ҺǸĦеɍƖGӏԦ˵˘ҏϛƛҮ²ˬҠù®ƀËԔĉСƋѩжєз',
                            'ΛȔʉϨЙǁȵ\x95ҰZÈҞYǆԓҔĕˎʸɷvȬлʁҧáʟŘȑ˵',
                            'ҞĿϜƢǘɊȋ>ǖˍɒҶœΰɳЪåƔɪҋζΚ˙Ν϶ЋÖїп˦',
                            'ΧΣŸƜϭʕГӆƂȰӇӒ˔ԔðˇǊԨɟҋ7ǴτӢãόÂ͵ҵώ',
                            '\x81Ëˋ϶κѤ˴φŪ΄ƩˑˉϷʁʘțé¾҂ʪɭѩǘЫʹ˻ɒš¥',
                            'lѩҙȱЧϰ\x86˒Һ˜ɁǗ˄ā˸Ƿȭ@ąʺıɝʐϱѶԫγСȱÁ',
                        ],
                },
                {
                    'action': 'ƆϦ˕φʬ\x9bȅʟĶʮÁŅ\u0380nɯɃӂԐΠͰ˫äǰȔĚҗ7ąΩµ',
                    'resources': [
                            '8ʾļŰ¬ԘӆǇʳâȹŽºΞЇĭģƽИİĹɀ7϶ГˆЏԉыӋ',
                            '҈ŠԜŖơ¼ȓАϝ?ҧίϦ˞?ˋ҉ЂøΩЛÇдΉźѼżԦ˂Ԣ',
                            'ǙÃѾͳȇ¤ŤÐГϻǞǧΣϜĈůʪ˾ҾцҀӚȿѤØǏ\u0379ѱjц',
                            "ȦĞԋöѶʋùŕȏƒ'ѲϟҭǢ˸Ю\x93қԐӼϓʂÞ\x80ͲϚǀ\x8bԑ",
                            'ǻʴʦ\x8d˂юÙԍȳЍʹԫԫȈ=\x8bӻԟԧǗȡƎҳɆ˞ҫȓѹ\x89ʲ',
                            'ʦȨτЂͼҗίΛԜ˳ö˻уˑРʷΡƽȨΰʫǑΩӨ˴fǾ(\x8c$',
                            'цǥξȫ\x99ŞǷÔ×ĸѹͶnӗ˞ҧрǔцӔɑFŴƻ%҇чwʃq',
                            '˳ǅȁɟϐŞԞЁȸςĹϕƶ',
                            'ќ&ÀȷȭÀŢ\x88ЕłŜȜǵĩѵҽҳȒҲʂǗ\x9fƮȹԓ:Ü\u0380Ԋƈ',
                            'ϝûţx˹ɚӣÌѾŃφ1ƊĻɳ˒ŒǈЈԎƬɿԆЇҺ©/Џ\x97Ɩ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ӥҫɜ',

            'version': [
                -1981376773113011292,
                -2017581441977384644,
                -7516679913840804467,
            ],

            'location': [
                'Ҕ',
            ],

            'runtime': 'Λ',

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
            'name': 'ƺщá˜ϛºшȳƠĿɿЂƹʕϙγäΚчǃĐ\x83\x7fůсƂǍђʎì',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '\x91ǩķ',

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
            '$': 'ОǥΜƖɱɮнŝŒιǽωɄϫÆÇБϹɗѾш«ůҒĥȤ,ǢȈō',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 7183815690400782248,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 875968.5302981511,
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
            '$': '20220522:172737.092177:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ʯłʊи˱Ǿҏ\x8b\x93³ĀÕҁɋȩǸǘˍ5ȒΉјʈΫмjѭΖ\u0378ǉ',
                'ɰԩˡȸ>ɟџːȫάýЄ˯Ӵ҉ƅȔɄʓɹƥЁθϗ\x87Γ\x87œȳс',
                '\x96ͶʉƓåΎϹέǠşƥѱʻΛȹϥƔʃлʐ\x9aцĈËȏêǊӍˡ`',
                '\x90ČĳʆуŵҫãϒøЌӞһ\x96ƝЮñҭʿімÞß˗\u0378śӇΤùα',
                'зBѻѺ\x9bȃD˝Ѹĭ҆Ϧȼҙϊțҩ¿ǫϥ¨XȥҮϤһɢŗЇǅ',
                'øǔГѦɪiÅӆɺϵŐћǳɻ˥˼ƕ#ѐɷˮŬ\u03a2°ȶˤԀȵyǕ',
                '\x92TĩȽɑϩĄřǉ×ӻйhÐӤwϚǜϨĔȞǣψѻÎŏȐʲŘĥ',
                'ëdѹǩ¤ƄːҤϳĦҰÑɽеɑмy\x95зʚаҾϭ0\x8cĲcsΓȖ',
                'ÁҪĒЦʡƠƞȢóϝĐъԇËĈxύѻŖǏþÌˉɬȎ\x98ȟ¿˖ɚ',
                'ӘÄW͵®˦ъ\u0382ԉДЈ¦Ō\x812ƳÐǾҺÍöюȩοǏŇȉɊͺӂ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                1129901932033794260,
                2130475694268390736,
                462097331024537911,
                -8126194321344719005,
                -3497358187298062760,
                -8105704635953435583,
                -4425449683557684132,
                -8068601737893952417,
                -8716333181475174856,
                7895636516536169163,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                730972.5128086669,
                231188.42638438044,
                595283.8410711973,
                821931.1933283226,
                -75665.44196771803,
                -95548.86646112392,
                374102.18074433744,
                610016.5412649154,
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
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20220522:172737.486080:+0000',
                '20220522:172737.495497:+0000',
                '20220522:172737.504615:+0000',
                '20220522:172737.512892:+0000',
                '20220522:172737.521364:+0000',
                '20220522:172737.530052:+0000',
                '20220522:172737.539110:+0000',
                '20220522:172737.547128:+0000',
                '20220522:172737.556111:+0000',
                '20220522:172737.564729:+0000',
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
            'name': 'Ǥˇ\u0378ʮҞiсǚҡʜņǂƙÞϫӢŻԘѬ¢ҼÂӅnnƂҮƲ',
            'value': {
                '^': 'int_list',
                '$': [
                    -6369766876856865928,
                    2255506862321846855,
                    622063718056632999,
                    -843318290834247336,
                    8760124080551936659,
                    -7346487876302182778,
                    8032021889103736355,
                    682978710300109995,
                    -3567216090307648475,
                    7855192108566755213,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '˹',

            'value': {
                '^': 'int',
                '$': 2445835471162611167,
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
            'catalog': 'ʶČϋЉÖѴÛΙȲńƒѢȆʱҾҵǍ\x91ϪτˬόȡŐϘǖŀ´ȈĂ',
            'message': 'ΈĘœ˟ΙȆΟΑӥnҳӻˋȨìό\x91ˢʉÜƈˠβǣѵĩԈˡϝ\x92',
            'arguments': [
                {
                    'name': 'įþҜ»ª\u038bЉέίʆÜкǅXͽĪ',
                    'value': {
                            '^': 'float',
                            '$': 106857.25801326425,
                        },
                },
                {
                    'name': "ҫǇȪ\u0379˰ʑp\u038bԏbòȤϔ¶¶ЬĨȨ©Ӄ҂'ѹӢʈƷǢ",
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        True,
                                        False,
                                        True,
                                        False,
                                        True,
                                        True,
                                        True,
                                        False,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ν)ӞǃѿɺʮҵąǿɩʞʏΡ˕ΡȘϤǾĶͳЂˏȟǶЬȚɘϽͻ',
                    'value': {
                            '^': 'int',
                            '$': -4689604493737585323,
                        },
                },
                {
                    'name': 'ωΑǚɞĲšԗɡ.Ԑ\x85ȧǂϜҿǾП˗ʰȵҍÑU³ˡäǥǑ¾)',
                    'value': {
                            '^': 'datetime',
                            '$': '20220522:172736.491011:+0000',
                        },
                },
                {
                    'name': '˞ĔÝ:ʸΡҗΰ˗˾ƳϷфǅѽųϚѵqϗˤтȵ',
                    'value': {
                            '^': 'int',
                            '$': 1259299384324841345,
                        },
                },
                {
                    'name': 'ҿǡªɲˣʝ\x8døŉ\x83ʜɖԔϓҁӸ˃Ȱʹ˳ƣʘôҩҗͶӖĵΪ¿',
                    'value': {
                            '^': 'string',
                            '$': 'ǃѶȥō9aϔ\x86Oοƛ\x7fŁαǜǰȻɻԣԒΕ7Tdγ¸ōɾȅә',
                        },
                },
                {
                    'name': 'ˤɗвɪˋҘ¾\x83ԎƑʨҏӠŖʋǅξɖλû΄\u0380ѻĬ˒ǯͷЦʴ˔',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        377311.7664908826,
                                        382031.2790352976,
                                        824377.6203555708,
                                        938260.235526344,
                                        -63090.74199700222,
                                        233199.33576770406,
                                        -14001.098094399771,
                                        213708.2293575846,
                                        937764.7976812626,
                                        281481.25905292656,
                                    ],
                        },
                },
                {
                    'name': 'ŐŕVœȣξÓs£\x90όŰ',
                    'value': {
                            '^': 'int',
                            '$': -7629692647874677955,
                        },
                },
                {
                    'name': 'źÆƜɃ˳ФȈЀʦɆԅǙԎ}Ť҇ŌJƍʺǅԏǇΣqƕíлϽĀ',
                    'value': {
                            '^': 'string',
                            '$': 'АӧƄΕП҆дˑ˯ǰĚĦƭ9ͲѣΪԊʺќ\x9bӘǃƦˇʍʖž͵ĸ',
                        },
                },
                {
                    'name': 'υʵ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ԃȥ',

            'message': 'ƒ',

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
            'identifier': 'ԓϕøϪԄɁǰѦѽȦģJАȱŵǃĢǪҘɪјԀĿЖӚÙ6ԉ½Ӽ',
            'categories': [
                'os',
                'file',
                'os',
                'network',
                'file',
                'configuration',
                'configuration',
                'invalid-user-action',
                'file',
                'invalid-user-action',
            ],
            'source': "'Ȫ´ԂЖȭ˽\x8bƶщCќƛˠƥƈʙѐ˷ʳλ˟\u038d¼ӥμͿϕәɲ",
            'messages': [
                {
                    'catalog': 'ǿԩdӋϖўǹρѱÆқ҉ǒĮ@G˻ѹɚʋǇƱмԛǜϞԃɽҒ+',
                    'message': 'ϑ˫тš)ŻžϜt˗ϮČǔһЍǬлôaáȮϭŵʆŰ˗ҴɸϹχ',
                    'arguments': [
                            {
                                        'name': 'ĤèȀŴ˸ñлŵςşǤэ˼\\ƪ&Ĳ[оηǢɇĕҵЌŕϫϢ˯ů',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ϜĄǯѯ=ˡЇʳ?ʶʶԬʽЧԄеНӺҲľҪϖɟͺηŝƛӤǞИ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            744214.3156442012,
                                                                            763521.8077159567,
                                                                            229737.99717448902,
                                                                            970072.7656867558,
                                                                            274155.65631215886,
                                                                            599881.7011279939,
                                                                            220675.1184124644,
                                                                            540871.0500182003,
                                                                            209813.05475101148,
                                                                            886379.548475921,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϽԚǇQʎ΄ÀОϵÔÍ˃нʘʂľѨĄWɾʧEȣѫ\x96ɬԋ<ЮȤ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            295105262030212741,
                                                                            -570260696847696320,
                                                                            -7062694090084665089,
                                                                            1397664182916191826,
                                                                            -6957658519137418245,
                                                                            -68582169656665672,
                                                                            7060295736618192670,
                                                                            -4224862668916873598,
                                                                            -6978486065055348794,
                                                                            4151688160869836380,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӕŴ\x9aҠɪƷ6ѥҊóƹˏȪĜȥü§ĠʴȄƜ#\x85ǐũԜҋ7Ȋҡ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĿǈΦҺю˛ȆĻʅƏæбЕœř\u038d,²ԬԆǱьʞԞЋǰЩ˰ˀº',
                                                    },
                                    },
                            {
                                        'name': 'Ž\x8fҍɏɇƇǁЕЀńʯүʤMϺғʯӘʻѕ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3282034101896032133,
                                                                            6518216533278844871,
                                                                            2316797193379579215,
                                                                            8991030448193472855,
                                                                            6923127084782563816,
                                                                            -3405535860971744604,
                                                                            -4096732815851856417,
                                                                            5107340584310306048,
                                                                            5790253760952054534,
                                                                            6215365673653805481,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '7Ѡȝ%ԣªƑѦ˯ԋӢȊӄē]ʞǘØuϪZÅ҉Ɣҙӭ˝ԏӛ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172728.493583:+0000',
                                                                            '20220522:172728.502357:+0000',
                                                                            '20220522:172728.511073:+0000',
                                                                            '20220522:172728.519124:+0000',
                                                                            '20220522:172728.527836:+0000',
                                                                            '20220522:172728.536811:+0000',
                                                                            '20220522:172728.545058:+0000',
                                                                            '20220522:172728.553802:+0000',
                                                                            '20220522:172728.562396:+0000',
                                                                            '20220522:172728.570294:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ρʶҖπʝϬαԃõх\u0378ùω\\\u0378\xadƹ\x8a{ǪΟӧȴԢ˜ŔĿЫƼѸ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 843434.9676684317,
                                                    },
                                    },
                            {
                                        'name': 'Öµģ\xa0àĴʍéɡÅ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8138001288024435679,
                                                                            -5629345984466128352,
                                                                            -8913679676579698344,
                                                                            4588577544398031035,
                                                                            -4844806096900411909,
                                                                            -73085506941065086,
                                                                            1252049902200172407,
                                                                            -697000901651822712,
                                                                            -4858713806476534813,
                                                                            5627664952928104006,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʿȿàēϵĞХðõʣϥƩŠ˨ŖĤŨґĈѹЪ\u038bΈÂ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7323549216642604056,
                                                                            -5532742645548253486,
                                                                            -3870922216327652916,
                                                                            7497241208453253057,
                                                                            -6795599152090324158,
                                                                            -224244387972279977,
                                                                            -7463781279716187746,
                                                                            -4441038582346342595,
                                                                            900072874297262597,
                                                                            -397289033115029743,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʢͻĎŽ5Č¦ȊřɇҡԬ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -12483.794658733968,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҴӤƥʸҶұǝƊζșÛðԭŤTWđЦĬӱðċ\x8dϧҲéԘİЦ˷',
                    'message': '˦ōŬҌРɓȊ0ŖѪǡбʝ_ǁůĕҦ&ȦЊ°ҌǜÎ˔ǼǸ˃˾',
                    'arguments': [
                            {
                                        'name': 'ϕʎɽʌƼѵŁ˗ǋǯғЃɭѐȺӵƁʕ\x8cĵчɗȯȲãӐ:ɜ;˄',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʳú˱șĨɬԅЕюÚҥñ˒ɫ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            855171.7115915307,
                                                                            293687.97129636334,
                                                                            363076.03163449606,
                                                                            885678.759544019,
                                                                            576267.4637483096,
                                                                            19414.994070841087,
                                                                            965147.9523905402,
                                                                            932690.0611317124,
                                                                            311425.8431410247,
                                                                            418983.392731415,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'á3ƐυГĥΚWɆ\x8d¬Ϲ ǆǗÓЩʤȻǷҠџԛɄӽҢͻGˉT',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˊƬOǣˉɈ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӴZ҅\x8d\x87ȧԑyҸϵ÷҉ɱȠ°Ӹζɰ/ɧӆӬ\x85ʔӶϩʈҽŠı',
                                                                            'ǩʶʐƾ]ԚŮѭʠΕζǼƆ:ǳϥϏɐǗ·ЧŒɟİπźĮƠØÁ',
                                                                            '£\u038bȄϵΥԒjӶņÞǄǸƉ˝ҾıubԛȈDκƨӾƋʦEŬҰɐ',
                                                                            'ƚȇ{ǉˮɥ˘ϑĦŨΖŏ\x87џåӁʮXϙԓʐɊӟ҆Άǆτίďɼ',
                                                                            "'£ɟɺӠʌӁˉǂɩgӶÓŸÆґ˄gɹͱç˞ԟǫͻЃϾŕZң",
                                                                            'ԐŀЌoʲɐԚɾІǘΚɚÏˤРʫʢªĄƋĉLϾŷԓӦ\u0378БǞc',
                                                                            'ӽҬŷӷȦ÷\x84ʍɬӵ\u0382ɥȅŕŏӡ҉ΰʴǻ\x894ʵʇӴȋѢǋœ\xa0',
                                                                            'ʳüӔȳĴΆƋԣüʿиѧ$ӎĘωΆɽəŸϽөȇœˡӌôƦǕӖ',
                                                                            'ƧʢªӸϼίś˫˃ʩĵыӿŎЬ4/ğʛǡ7НƷϭĔʞϋȳϩЩ',
                                                                            'őԂӨşěϒƃƀϋȃ˺ǒƍԮĉԉϩÆƿѠŉԀ\x94ϵѼȌǷҘΡϼ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Εǟ˺śŜщ˴ƪÅЃßȌ\x7fΰΧŅ½ɩĐÖ͵ӵΪ\x92çɊĶԝҏҬ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʫ¥ƱԌɊƸė\x95äхƱԬƺԏŪɪӧ˹Żυœ@ɉ΅ϧȓщ²ʠϥ',
                                                    },
                                    },
                            {
                                        'name': 'ΦŻԈĖƖь\x82',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5116788649128943519,
                                                    },
                                    },
                            {
                                        'name': 'ԋңΚêқ˯Ϩu˶ҹiėȄĽˑ¾ȷÚɐțÛƓӍԖŋ˂ͺҦeʹ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
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
                                        'name': 'ĚѦƑĥɭlаȹǎΟБɵьʔ˯ͱʣǣƍҐϺ\x97Ӵ]ŲԧʆʶĴƘ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2951688374860362839,
                                                                            3530473063456397547,
                                                                            3165120534045183492,
                                                                            -4568515741293941358,
                                                                            7203408803904135298,
                                                                            -9089857698785726724,
                                                                            -2857688657591237166,
                                                                            -3978883686095165829,
                                                                            -5861622450742521938,
                                                                            555678294304821900,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϊǝıǓțƉʖƼûˡΒÑͲƉПԖҒϲӼȘҩΕŌѠѻŤťģŒ¶',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': 'ȄҒƙ¾',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 828790.3938315507,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǭ4ǖƤҡƷǅ҆şϼ˽ϊŬȭÆǺȑШɮ\x9cǍȐŅçŹ˾(sΤȿ',
                    'message': '˷ζԭʄʾƳěʰƈīѻΛ˫ΝДғϱŨƳƽ¹ǚӵȽ˧өҎčŎ\x89',
                    'arguments': [
                            {
                                        'name': 'ǹdµԦѠʞʍԫȼȸΌǧŰԢ¿ģĽFΏĿӯψǶҏȝŗ\u03a2ȏ,Ǌ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 639225.8960640077,
                                                    },
                                    },
                            {
                                        'name': 'ʗӵϪԠ҄ʐȳοĚЕˉ˾ɲŗӡԎ×Е',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            148832.74236673105,
                                                                            825857.5732663563,
                                                                            669981.1100543297,
                                                                            570037.9341555523,
                                                                            56481.94922774282,
                                                                            231015.2093345091,
                                                                            336028.0258275546,
                                                                            3204.5946237872995,
                                                                            132407.85172124748,
                                                                            346446.69064546534,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '£Ƿϻˡʐεͳčұ\x95ӃʇŒɖ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172730.052938:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ΒҬ6җԡǐͲ:ÝԜϖϐ\x87ʋϩҪǛϷǎʼƂʗέԖϓӀˡƤīȗ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƸƔҀԚƂr˞ԒȍөŠɢwǾŦ˭ӛѰ(ǮħͰʉ˂č˽ΐ\x98˂ʗ',
                                                    },
                                    },
                            {
                                        'name': '8',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Š¼ÑѶӚĕ;ÊĘͼҭжʿϰҙ˒TΓȲѓџƳɝ˲ϜȺǈЇϥ}',
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
                            {
                                        'name': 'dǶjÃŞ<ƶțÍŲǩĲÚ}ƫҘӉ¬ɷɇΔƤӧȷХ¬șƊÖ½',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4728296775262217019,
                                                    },
                                    },
                            {
                                        'name': 'уLǙԒӊƟҬΞ¨ǺŖćǜʂԆ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172730.316297:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ЩȑРҦYʉ¤ͽГ#Ɠ[ŖӍԢӐ@įȞĚцȼы=\u0382ОѾЀǃŭ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172730.351662:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Âҽʽ\\ŀԋŰ˙hʄǼ˨ȓðˮӼÏɔӝІŀ4ό\x7fǿʱħԩƀ˽',
                    'message': ',X\x81ɧԂȞϧҜƟUԌқ\x81ėыӨϪ˨\x81ǙʫҞêɭ\x9dНǿˑ½Ə',
                    'arguments': [
                            {
                                        'name': 'ϸҭϷŦ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': "'ȭƜ˧ȷ«¥lЋǷӫńʑñĖԣơҜDұ1ƈhɌʔԩEҷφǶ",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2096447979366520877,
                                                                            -1403767361195120463,
                                                                            3389998720176239359,
                                                                            -388676103268071455,
                                                                            -6368456625493134052,
                                                                            3531388711890984379,
                                                                            -4507196065116132075,
                                                                            2664800349194161532,
                                                                            -8970088478553428761,
                                                                            2877096480228547269,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϼ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 190977.55663749034,
                                                    },
                                    },
                            {
                                        'name': 'ΥфͼȽśԀŴτйШͰӥçȧWӪυʅ͵åЕМқ¡ƃɺģϓ\x81X',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172730.623865:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǳţҰŢΒїǶĐDƮʳɥԭɜšƨµGѫΊºɞʳһҗƠͲΤϬê',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŵԋˆԜѷϚiиɪʋǿКŵφłҪF=ðɺ\x83ԋҢʻ˽ɥҨԋO҆',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '°ǲȹҧ½èũʵɄ˄ШÔǌ$Ѷ}ЮƋͼϵӠЖȮȔȵXȠǴȿӝ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172730.813240:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ŀчþʊ¤ƚɻӯļԗѿƉԡдΩÜͶžGiĎӰ/ʒǹĵĒϽƒҠ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 90450541800377450,
                                                    },
                                    },
                            {
                                        'name': 'ǉӖ×ȾĘ§',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӴЫˇϟѕǈ¯ʥƵÒПòʴʵʷJ4ЪʚŨԂТӫŵɽ\x93ԑƁ×ɬ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172730.920147:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΐƟëŨȚҵȚǯžVɡ?ӗ·QԅќˈŴѲċϸԕɤУ\x8c',
                    'message': 'ŝ˞ϫӢΔétívȃʥŭʗЦĲͶҞÑПЏБƌϟӞãöӌþӭƀ',
                    'arguments': [
                            {
                                        'name': '5ƟЂǔМːϊϬǝ\x82\u0382GɍσΌäĪVԪȟ~}бƽ˽Aӕ§1є',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 945542.7990548209,
                                                    },
                                    },
                            {
                                        'name': 'ʁɵУҬŤŠРɥ²ČǴљƭ\x82ҭΊȠëɱʳɲΡӥǬǩϕӨɠ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6256985266916182090,
                                                    },
                                    },
                            {
                                        'name': 'ʉƎŤȮǼΞD£2\u0379(ǯђʋ~ƒЌBԓѾβəϠқҝŕϠ.Ԩϥ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172731.060319:+0000',
                                                                            '20220522:172731.069483:+0000',
                                                                            '20220522:172731.078258:+0000',
                                                                            '20220522:172731.086384:+0000',
                                                                            '20220522:172731.094607:+0000',
                                                                            '20220522:172731.102746:+0000',
                                                                            '20220522:172731.111621:+0000',
                                                                            '20220522:172731.119990:+0000',
                                                                            '20220522:172731.128458:+0000',
                                                                            '20220522:172731.136606:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Çёɕ\x89ƗŻũԮʟŹԗǬʬ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172731.181383:+0000',
                                                                            '20220522:172731.190517:+0000',
                                                                            '20220522:172731.199493:+0000',
                                                                            '20220522:172731.208617:+0000',
                                                                            '20220522:172731.217348:+0000',
                                                                            '20220522:172731.226717:+0000',
                                                                            '20220522:172731.235232:+0000',
                                                                            '20220522:172731.243737:+0000',
                                                                            '20220522:172731.252686:+0000',
                                                                            '20220522:172731.262603:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʨÆѓНҲƯԀјÁ\x93Ȧïǃɗƾʨ\x83',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': '˟ʶɳĴʄǍ˰Ȥʒʇëӣϓǳ¸ԕǄΪƫƦƥƉ\x99ӓӠӧҒİQŅ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172731.435167:+0000',
                                                                            '20220522:172731.443780:+0000',
                                                                            '20220522:172731.452217:+0000',
                                                                            '20220522:172731.461442:+0000',
                                                                            '20220522:172731.470265:+0000',
                                                                            '20220522:172731.478546:+0000',
                                                                            '20220522:172731.487485:+0000',
                                                                            '20220522:172731.496038:+0000',
                                                                            '20220522:172731.504896:+0000',
                                                                            '20220522:172731.513493:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'cјƧЃŚšʚӥўЧѴԦʍ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            704154.2836194753,
                                                                            473837.7887485336,
                                                                            580869.2794522885,
                                                                            583476.385535817,
                                                                            47987.658029932965,
                                                                            451767.5276591268,
                                                                            -29936.754003794413,
                                                                            450155.48421087745,
                                                                            -13831.140696449569,
                                                                            497892.79325207754,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x95ʋʒҖɀǖϞ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3688667037932766547,
                                                                            -716385412433138072,
                                                                            -6453414012121995943,
                                                                            -6368990224962525699,
                                                                            -2885357121632565866,
                                                                            -5264197002803570513,
                                                                            -4320779208054310912,
                                                                            6101032651975054712,
                                                                            862387996655521329,
                                                                            3464933968870737698,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'вѤӗãˋlëʱϗ˽hДÊʉ\u038bϼͼÎ$ǡ°\xa0*ɕɈȢ\u038bĢΠҞ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8282141376094976985,
                                                                            -4917018148693150401,
                                                                            435717733929911211,
                                                                            -8368516242078143800,
                                                                            -542917996919755914,
                                                                            4315816966360789149,
                                                                            6375042797943235341,
                                                                            -6847033029988663301,
                                                                            -1131834671604626463,
                                                                            -4747905329025524436,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ϮĻ'\x84ϷĕŷïÌӾˆʼ\x7fӐȼЙP҉Ԋώ",
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӰɗЇ΄ҘнĚ:ΛʛϱʑÌхт˥āϪΔɢǹȒȄӰΘ|ŊÆХʷ',
                                                                            'ǌȲ¢ΦȬƔӁχԜʣÇЅӖƐӴńӠӆzʙļфԦϤӁȁӀӢĹɥ',
                                                                            "ǫŝ'ŉǺɺοǌ˨ʷŔԮǴVЎâĸÆģЭЌƼјӝPѨÍЯ˦Ѩ",
                                                                            'ˎįǍϐӫ˓˹¥l΄ҀʘŸʭԊ͵ΟĢԏӭΡЁƷň4ӿ<ċY˰',
                                                                            'æĉѣ˦ǏӏƲWǵҨΌǔˆЯ¡ѡŷΎ˦ύϋ,ŪРϊӷиѧ˒Ф',
                                                                            '´ƙųԥ^сϬƎәԨұƮŤ˖˳ϛЪɉІԀĨŋ҈ƂǗŅ\x85\\ϧħ',
                                                                            'VãԊÏ΅ǥԓАYӄĳʦ\x8bůҴ',
                                                                            'ɛΣȏϵʶΖҤнʝЯVɯӭҚeЄɊŞЖŷ\x85ӗƹɂʓӯțÐɎ˜',
                                                                            'ŲӉҥƯˁҡѴфǻаŎěȨĪȓǛЗƓƭȊȜӌXһǻˇҊҩӘЭ',
                                                                            '˼Ѯ\u0378ЛȄǇ\x9dҎԭΫOƴƔѥã,ƢԛгǘÞυƙĽSϱɊϹҋӮ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'е_^ÃЅöӧж˔ƍΨÐҢ҆ȼη ÿŧѻ²7ѐǩ0ÛӖrʜτ',
                    'message': 'юύӍɻˋÉҲϺɖҟԊ\x93υķҫϩҦҝѸξԮɖӋ)Ԫɦɾҍƭķ',
                    'arguments': [
                            {
                                        'name': 'Ħҽsáϣӎů!ΎĹнʥǽļү',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172732.096783:+0000',
                                                    },
                                    },
                            {
                                        'name': 'қӀǍƏјǾ¤ƄӲvèϖñǭΫɻΆԢЮԘʩЌùʙǣ\x8bÖƆƬĢ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            486872.6512873478,
                                                                            480319.8804371811,
                                                                            84760.34914749407,
                                                                            703410.150479946,
                                                                            5717.0451940213825,
                                                                            865000.8218413295,
                                                                            861121.7718756883,
                                                                            949492.66240061,
                                                                            31361.166162633774,
                                                                            673298.2600667803,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'æ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6655842515598578847,
                                                                            -5031948690776510192,
                                                                            703470182007079702,
                                                                            8468430456384914895,
                                                                            4085962947819814009,
                                                                            -4372443855448732454,
                                                                            7713109749398114595,
                                                                            8899692808036528218,
                                                                            7801580192725114132,
                                                                            3656455150415995008,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x96ǰԢӎ҇ǧћˆ˘țФ˙Ҽ¡XŲЮĈH\x95Βʂ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˡΔԙȶ˂ʂNәҪňеmĹħȸƁѾˣ~˚ɊĔɋȲъЖJæӣĤ',
                                                    },
                                    },
                            {
                                        'name': 'ǇÓͽӰʮПƎƹǝøѣȫѬƉƘɢԪȁɾƩű˖ËкʐVɉĹBҼ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ëĥϣɩпŚÂԧĺöΔɶϧƣǩčѣϾ\u038bӄҿθōôǮԎʖĕˎ7',
                                                                            'њє҉гʱ)ȩaȰȡɄLúϻǶǚ҈ʃȀІZРӻǊќƕϢɑƂɾ',
                                                                            '#ԈƑǨƑӽɇϾ³ɡԜѕԮ0ҵńʴ\u0378ȩʤ\xa0\u0381ȃǓŌDȖϼҢʁ',
                                                                            'ȟђӧ΅ПδѨӋŬ@ЖɟωϷΫȷυУ˄ӉӔ˼ČͷɎѦȐÔȈÝ',
                                                                            'ӀΧƖϵ˞?ЭMȆ\x80βтʣʧǈШ˪ҖӪ¬ͻӋƉԍҖ˱ǣѷΈǟ',
                                                                            'áȰŨ]ĂǇ˱ҥˌÞȊ͵ԭØ϶ʪѤҭ5͵ĈŵʇѠ˱ȦЎ\x84ʙф',
                                                                            'ςЏϲѽ҆ɾĴҰ\x95˟ΖōɇŲЬԕӂз;ͽˁҩ)ʾӭκǃӍǌΥ',
                                                                            'ԊɔϳΆȮεǎϮxHŇƑøђqΆãѨјӘϗŰÁΔХҬΏĳÏϮ',
                                                                            '˨ʄ˨Ϟʶ˯ӀёϿvͰȨδҍҐē ØҔȂĭĉɂ`ǑŕǷʻжť',
                                                                            'Pѧ\u0382ÔĮȅΆƗĒǞ¡\x8aƈʾÚʛEɧӪ\x9fΟÅ\x83ɭǕŀїӢēǡ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƦЋ£ïˊȺʥŞ\xa0=ҡұΣɸԬɔɽ\x98ӱţɹȬϥ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2308798109808660399,
                                                    },
                                    },
                            {
                                        'name': '\x90Ǡ\x9fňƧƷԜĽҁŵɕDʸɍȲœϤäƅйŸӾ%ƕ˩_ÁɁʵϊ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8181118744864168352,
                                                                            -4626190261121612346,
                                                                            1425145969245269346,
                                                                            -2466919881773842061,
                                                                            -7491201958442476435,
                                                                            9215387375377986392,
                                                                            -4220504590811117814,
                                                                            -6867431575034676728,
                                                                            8408340109073287623,
                                                                            -3519181901827608302,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȆÈÂȃƍ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172732.694502:+0000',
                                                                            '20220522:172732.703621:+0000',
                                                                            '20220522:172732.712665:+0000',
                                                                            '20220522:172732.721233:+0000',
                                                                            '20220522:172732.730248:+0000',
                                                                            '20220522:172732.739439:+0000',
                                                                            '20220522:172732.748231:+0000',
                                                                            '20220522:172732.757318:+0000',
                                                                            '20220522:172732.766581:+0000',
                                                                            '20220522:172732.774763:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϦњԀҗͽ\xadƄįҴʒÎ˛ˣsxȷȽ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            724423.2304638119,
                                                                            468275.9758953876,
                                                                            432242.19767711556,
                                                                            -12096.059500717383,
                                                                            847258.2391976233,
                                                                            309728.9813892194,
                                                                            332111.0945874871,
                                                                            398686.8531306406,
                                                                            801200.5289037887,
                                                                            887205.1451417148,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҖǓÞƌ\x98ԝӹѪĽˈʐ˝ǚŝƻƧ\x84źёʭǚǆÖǇѨø´ʏåŋ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѫʂɍΉǃĸɼǆʆӖǬ\x99âʥҼūƐˈШӁӃѺψφȢ»ҩШʿb',
                    'message': 'ҊѣľʜȡűʪƖ\x8b¹Y/®@EŭҁяBӃŴϱŠΈѵ³ʇҪfɧ',
                    'arguments': [
                            {
                                        'name': 'ɑɾπʽʮҒԞӸʒØʐĐӺҹ˂Ϥεњҍ\x96',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -567198389481611075,
                                                    },
                                    },
                            {
                                        'name': 'ˬЖȾʏϢǊґμƔԏŶӉȯӘӤӏ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -61396.21470102248,
                                                    },
                                    },
                            {
                                        'name': 'ǟҒΐț\x7fɳˍӡŅКѽ.ѮƹƧԔƑӭԒͺ.˹ȇԤ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϭƑǣīəȖǱѱă˗нԔ\x9dͺϼǑυĈМҔΉæӪӰъМƶʗĖʘ',
                                                    },
                                    },
                            {
                                        'name': 'ЊǰǳϤлɳêĲʏȼʐѐũƖȢq˃ΘϜħӋ˼\x84ƾāӖŹȵήӵ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7353099885993048683,
                                                                            8718162783432220778,
                                                                            -512800706163298616,
                                                                            1619289894841110480,
                                                                            1294294737985912282,
                                                                            2699796759187692952,
                                                                            2448113352267483710,
                                                                            -3983867048382576330,
                                                                            -4072810666805989252,
                                                                            -7808243748216617435,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˈҞƸŋǒǊζî·ƴÂɰѝǑȎ¼ǹͲÌȽˈйļŤˎ҂Άшϻƪ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172733.334280:+0000',
                                                                            '20220522:172733.343417:+0000',
                                                                            '20220522:172733.352256:+0000',
                                                                            '20220522:172733.361340:+0000',
                                                                            '20220522:172733.370496:+0000',
                                                                            '20220522:172733.379330:+0000',
                                                                            '20220522:172733.387264:+0000',
                                                                            '20220522:172733.395491:+0000',
                                                                            '20220522:172733.403532:+0000',
                                                                            '20220522:172733.412113:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'GɸѦѥǯɋϝňѴƕˢţ\u0381ˇŽȋβţǦŗ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172733.457260:+0000',
                                                                            '20220522:172733.466338:+0000',
                                                                            '20220522:172733.475423:+0000',
                                                                            '20220522:172733.484259:+0000',
                                                                            '20220522:172733.492319:+0000',
                                                                            '20220522:172733.500697:+0000',
                                                                            '20220522:172733.509798:+0000',
                                                                            '20220522:172733.517927:+0000',
                                                                            '20220522:172733.526701:+0000',
                                                                            '20220522:172733.535608:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '@ǁЉ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -75884.61790394886,
                                                    },
                                    },
                            {
                                        'name': 'ЪėʼśǃtΌιʵӾЏʈʋǒώӹԣҕǔѳϮ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 298697.2042567108,
                                                    },
                                    },
                            {
                                        'name': 'ʪÚ˧вԔвȱЅWΦŔŖӬͿĴǛʇЩǓ¬0ЕOɊΏϤȅӜʋǩ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7568928323140677966,
                                                                            659374437358941635,
                                                                            6232457962816675861,
                                                                            2931081400467716549,
                                                                            -6284885813708266025,
                                                                            6543907134394252037,
                                                                            -367833541305473273,
                                                                            4449646014050105321,
                                                                            115117076197782162,
                                                                            -581270822473902819,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϣ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Oɂʖ\x8bϮ\x81ЪɌúίÊʬùǛϔʞȡțĺҴӻîüӗ\x99йͿґϤh',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'άȎăŃ\x80˾җŎÆȋж҃ǳӡҭN˂\x8cʣ\x89ΓĘɲƍөҔ΄ӼǲͰ',
                    'message': 'Ĺƚ;ϤϼΟЏȂԣϊ˖ĞhҤԢΥ¶гǬǚΥr\x98ѸӚħ=ʘþ\u038d',
                    'arguments': [
                            {
                                        'name': 'ó˹ǦƅЃ˰ўɨΑҴӿѹȈ±ŗ¦ӜĳĴtѬΟΙʨ\x8b˦Ƭğѽƃ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԟ˟үΓͽæѭҍԢ\u038dώȴŔǜʱƪӎūоpϔˣT@ʢȻũϗӧґ',
                                                    },
                                    },
                            {
                                        'name': 'ӨƵȚĎІěϯӓ\x93',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6478308956352019430,
                                                                            4321183785860731958,
                                                                            -4058223216901178117,
                                                                            -165203272528553397,
                                                                            -3428603009547470174,
                                                                            -5200719937001621049,
                                                                            1831757304661294087,
                                                                            7794053240414752032,
                                                                            1808684263079917818,
                                                                            4513595839686350452,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɉԄÀoƻВ˒Ǭǲ\x97ɑԃÄSЅЬӉɩĉɣ\x93П³П\xadˠčǄǏˮ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172734.010105:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ųǝɽѯĂţ{ЖúƨəĂ˸´Ĕú',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 739213.4631208474,
                                                    },
                                    },
                            {
                                        'name': '¢Ѯž?γƯ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            254166.97969348723,
                                                                            977640.7174405723,
                                                                            167392.7896593921,
                                                                            740497.0869779943,
                                                                            -66591.59490724461,
                                                                            230101.68366290384,
                                                                            620790.2790262956,
                                                                            42977.40134326974,
                                                                            930311.4139761886,
                                                                            433240.935148834,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ІɅɐʔɜŽÂǋаÇ˥6ɺǱҖɒοӸϷў;ρ´ųʏĿǕԑʾÇ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172734.208259:+0000',
                                                                            '20220522:172734.216479:+0000',
                                                                            '20220522:172734.225071:+0000',
                                                                            '20220522:172734.233561:+0000',
                                                                            '20220522:172734.242612:+0000',
                                                                            '20220522:172734.251218:+0000',
                                                                            '20220522:172734.259665:+0000',
                                                                            '20220522:172734.268786:+0000',
                                                                            '20220522:172734.278073:+0000',
                                                                            '20220522:172734.287139:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӬʃσýoȹĕˇCȤϧǀӝ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            604933.0376190149,
                                                                            312192.33899024414,
                                                                            355202.50348902075,
                                                                            809414.1116917656,
                                                                            295679.4177561081,
                                                                            135315.92478503767,
                                                                            791046.9705164992,
                                                                            642767.4965690256,
                                                                            745660.0493455144,
                                                                            780584.7097298006,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϢčϏxέфȃƢɱ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 21671.146520382026,
                                                    },
                                    },
                            {
                                        'name': 'Ы¢ͿĪ\x97ʣģ\u0379ȶӖ҅(њОкǨĚϏԬĉ÷iԘӧ\x93ìФɎ0ŏ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172734.491852:+0000',
                                                                            '20220522:172734.500855:+0000',
                                                                            '20220522:172734.509420:+0000',
                                                                            '20220522:172734.518336:+0000',
                                                                            '20220522:172734.528338:+0000',
                                                                            '20220522:172734.538616:+0000',
                                                                            '20220522:172734.548518:+0000',
                                                                            '20220522:172734.556758:+0000',
                                                                            '20220522:172734.565847:+0000',
                                                                            '20220522:172734.574044:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'χЙhӲ(ʧƺɹȯƿƧŌɲӻК\u03a2Ϫƴ¶ђǈȘЗƱȮķҲǵȧq',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'îÐËǦĨƑӟǌǥÒөǚҝҮҌɆϿсżŢцûêɾśh®ʈҶʟ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˹ѳƎˠ˵ɤ`\x85ĝϒȖɏԖʁĔʊΥʱƂʟɐɑƈЉŪϹléɋӆ',
                    'message': 'ǀ¶ʓǈƲӱʵԈ˹ʔͺЁǽǟưɣÒǣŒ\x81ұ,¼à˾\x98ſ\x80җѩ',
                    'arguments': [
                            {
                                        'name': 'ÿE\x98îūǅϵ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7444056211036925055,
                                                    },
                                    },
                            {
                                        'name': '\x97ǐȪȨϱθ=ȖԂōŪÎčŰǱȍčωˡ÷ΝȒʬ#лêȾvˍϪ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172734.725080:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȯžδÉ˧ƪƐϬԛŕШƹIΖЭҭƽŊĹƫŤʴӤ˙ѯȂ',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '8ÝªǸ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            806679.5339150835,
                                                                            864093.9598239628,
                                                                            15300.469171788209,
                                                                            87199.35067596179,
                                                                            428346.79891710624,
                                                                            -13402.13445275613,
                                                                            7719.177358085173,
                                                                            517175.8526097281,
                                                                            355670.98402126774,
                                                                            319426.65496965917,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x87ƤĊщ;Υ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 196504.5258164279,
                                                    },
                                    },
                            {
                                        'name': 'ľȜÛ˝ž˴˄\x9bőűяʂÂŋńǌu',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˍXŗµ;țԍȎΉĿά\u038bhҨ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -363132191454496537,
                                                                            1698537281021724558,
                                                                            -6182517832097855102,
                                                                            3399410070337517940,
                                                                            3542383133164401685,
                                                                            -1759178242873029807,
                                                                            -8427706049877521311,
                                                                            2004411968278659449,
                                                                            -7982290632031090736,
                                                                            1352352922447992269,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȱ˺ӰͶ¡ӹϚȯʉӔ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '´Ãb\x81ɔϞϔѣѓЌɖΉǤXӶaêɆŕɸŧИɄϾӺ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            966521.2934966998,
                                                                            411472.22580441757,
                                                                            954389.6623353048,
                                                                            -37402.92509303927,
                                                                            404923.5442873923,
                                                                            296584.34708089987,
                                                                            680425.1266301367,
                                                                            949659.1059995296,
                                                                            568804.0667337696,
                                                                            326938.87977455376,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʘɗЏͷɈÎŪÃˍӘ|òλӿˑȦ;ԓáϴЛÍӟԢӝԔA҄ʳԛ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѭϿǉǕȳɘæƕʥĩĢӺÓ¤ӛȭϤȹϣјVȼ\x80ϛ˯\u038dӦĂŏ\x99',
                                                                            'АΣѦҟȼԓѠȽw]Ϳ˳Ɇg\x94͵ΌˤԇЌ҈ȰĴǕΰƌӹǰ}*',
                                                                            'ˑŭѓǏνǌʙÞƀЕӭΡӠȻjӛρĬӔϔ϶CӄԈΖýŏҝӤƹ',
                                                                            'ηʨѢұң\x86yǕÒ҈˲ћӳĬʖԡ҆˘ŮέЁљКӒ͵\x86ʟєˉҀ',
                                                                            'ǚƙҨɁӆɠάǑŢ\x97Е˔ĢʣˬtѸǌXd˘ԣΜѐȭОlC\x93ά',
                                                                            '҆ɰΰˢӑ{ǼΫϟ\x82òԤžƣӆ·ˠϻЩƜːҺNϨÔѸnÒ¿ȿ',
                                                                            'íƐ\x9dˮҚǮʰŌϑͶѺΰ\x80ӾҘΜ˭ɝŁ˅{ҼɭÿҾƹĞƴĵӴ',
                                                                            'ҎН˖ѪԒ҄ǜȝŬρɤѷԣʄҀѵϩˮĮȑҖҳĝɟΣÚӲĔԞѵ',
                                                                            'ДƟń\x8bҿnӏ²ęЅ\u0381\x91ɯзÁǙƱϚʸͽĞ˙>ǅҞoѓűGʠ',
                                                                            '¤ӹƿɉ?&Ԡ\x88ϤѭɼEǑĄ\x89İЗӮȧѫχƛJԔǓ/ҰƝƔ\u0380',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϯťϤȧƅҼ\x94«ťĉıȋӑаɑ\u03a2҆˕ɺĆԩϙӲ҂ŜӔ^Ѳԙƪ',
                    'message': 'ҺǮ\x82҂ȅӵϻĉ\u038bÙжЃȥԬǤҘӇȿӴ¯ʊĎʼϐƕ˭УϥԅȦ',
                    'arguments': [
                            {
                                        'name': 'Ϭȁ\x90Ɨʔ˞бԗŹУÚцʒѦӺ˱ӦˈɷӠϸԔ¥ɷЌ҈ČѢСʳ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ʢўҜͳBԨЃÆӖ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172735.591631:+0000',
                                                                            '20220522:172735.600956:+0000',
                                                                            '20220522:172735.610191:+0000',
                                                                            '20220522:172735.619570:+0000',
                                                                            '20220522:172735.628353:+0000',
                                                                            '20220522:172735.636710:+0000',
                                                                            '20220522:172735.644949:+0000',
                                                                            '20220522:172735.653733:+0000',
                                                                            '20220522:172735.662900:+0000',
                                                                            '20220522:172735.672232:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˏʠľԤÜʩɪz·Ѫ҇ѵѱįŢǆРæǖŰҖҽÊ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1625020101951384916,
                                                    },
                                    },
                            {
                                        'name': 'ДŃŚЃϕFΤ\u0380Ґэā',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -85733.74848450533,
                                                    },
                                    },
                            {
                                        'name': '¡ƵƑ˕ˈƩż¥ξЖǠÆƿΗї҆ϝ\x8c˛ŷȃ\x84ȊɶϾȅÐͻԞ ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 657092.2761203931,
                                                    },
                                    },
                            {
                                        'name': 'ɲɎηÜ ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6941873265227622597,
                                                    },
                                    },
                            {
                                        'name': 'ȷɪnԠĨȂФɠȒä*rǭͰʲκ\x83Ȝż',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӛŧĮѝɯƶƣÉԍЧʷľżӀŕѨɻӬÛϖɹƭǻĈҚB˪Ĳʕǿ',
                                                    },
                                    },
                            {
                                        'name': 'ŸȈŹԁТѾŅЗʻюӫϥƂʔуȶŝǤɧśƦǯ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7667543559739811534,
                                                                            -6125176904546491167,
                                                                            6337701314635798996,
                                                                            -5280409982415639266,
                                                                            2589242812894005243,
                                                                            -4341886490241270223,
                                                                            8366566209454263392,
                                                                            -1816407913976338850,
                                                                            -4333393627855705747,
                                                                            1881701408969089732,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѸҍƈǊVę\x9eҬɂ7йdԥȯǔȹ˭',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4127043486892112157,
                                                                            -3287126677696724805,
                                                                            -3948434687376091908,
                                                                            -163205402434499933,
                                                                            601978867973994977,
                                                                            2867332921209962799,
                                                                            -7777270500144867537,
                                                                            -8086468037384935038,
                                                                            6088048344693610125,
                                                                            6297091263383526409,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѣһ˽Ȕ¢ө\x9aʹϼӹЉɳºͷΚΣ½˹ǲтĤCήŭɅхǳѯҕ˛',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ǯ˧џϷV«ǭΝԇЖșǖѥӧĿŤҠÈʭ¦ϫǟмɅ˳϶ӢϿΦu',
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

            'identifier': 'ôɳ\x94˻Į',

            'categories': [
                'file',
            ],

            'messages': [
                {
                    'catalog': '˺Ҹ',
                    'message': 'Қ',
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
            'name': 'ÐʖӾɕǌҝƠØѷĴνɭИΛƺgǷЖðώŢы˶Çř\u0381ɶòЄǨ',
            'error': {
                'identifier': '\x86ŅԐP$ãʐԭКȲĚƐЦćӧʮƜ]Ԭ˷ЯƣΒ}ŪӀɗťŜs',
                'categories': [
                    'os',
                    'configuration',
                    'invalid-user-action',
                    'invalid-user-action',
                    'access-restriction',
                    'invalid-user-action',
                    'access-restriction',
                    'network',
                    'file',
                    'invalid-user-action',
                ],
                'source': 'ҕǔǖ¾ғêºɏϣϚ×\x86ÝȄŞųǌǜԃ\x94ҎɂҏǸȩDďʞ\xadϖ',
                'messages': [
                    {
                            'catalog': 'ĉæ~ДЯ·˱ˁϨџÁΏʝǫϮ+ҡǛʖ\u03a2ӃɇΎԈŇǨΝҋѳƆ',
                            'message': 'ѭͼżǺсțɕцȨʳYӸĈóŹüǜϔɵѭĥƁԑάҕĩ\u038dƤʅļ',
                            'arguments': [
                                        {
                                                        'name': 'ŒɻŲɼØĹwˌcˎƍѓňοǇԪЛȔǑԝƴ;Ǭ\x9cAѢԙÿßԨ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˲ɐΠͼÌɛПśȼπϟҤʇӼδɕΊVҦŘʸ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 589257.9868302145,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϩΕўϾ0ԉ˖Ĝ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ԨWʨʨɟ\u0383ɯҤ\u0379¶ͻǰſӲ'4»ŀϕ˖ŊìϘʖÀ±",
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϕѤûȅϮt΄',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϫǧӱ\x8dЁɫĔЦƲȰÖʠ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ą',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8345814050898704006,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԂґӖŌʻЄљ4Ì˧ԅžİǅɐÃ\x9aΑƗʺϞĿŃ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ί˓ʜʹԎěêҡ\u038bˣê(еѶͼψSǝ˦ɏļÈʗʿΆдΝƾƩɿ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÜӖѱ\x88ǵѳΆȴсѰ¸ĈÂġƌȂŗǅoҐ˱ĒҤԂ\x81ĈϮ%',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƭÙɯʜɥĠƱΦйɁ¾ѰɭƙФʯ¸˳ƒȞŌӚӥɂ҇ΕпȄƭL',
                            'message': '¯҃ųêηÝĻ7HˤģȦǞґЇʔÙɓ\x81˨хо<IàuѭéԬԖ',
                            'arguments': [
                                        {
                                                        'name': '¼ҕȤɉ\x85ɏÿʜoďхԬƣƥʁίӮɈ\xad\x92ҟʺ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӀҽȍԪĤƑә=ӣǃԖmҩːʄƔʵƍυşҨЬȋӟ"ĪҊǤοӿ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˽ҟ\u0379ξ¤Ƚ\x87ɞП϶ƋъƯѥзƵȏєҏö˻ŗь6\x81˹ˀҜϛϭ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȜӮŝ\x88əˡͲϴĿƳ˼ŗȌŭÿͳɐȇķ\x9aѰˣӲɐѼбɡӗg\x92',
                                                                        },
                                                    },
                                        {
                                                        'name': 'δҾĐњϡƣÅΕǯŹƯʍǰɦƅü¿ϐǌ͵ʩ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2183800334415100036,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ũźƂȻπРʥɡǍχ˒ʜñԅӹӟсԒvбÎ˦ѸԤĿ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '|ϒÊѠфĸ϶ʎӝƿÈӗρҜ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4226207144609310436,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĸŹҐ˔¸ј\x8eέϪʯąʸǈȷ¯ΉОӟȗĉǟɨҨĳԑӔЋЀΠ\x9b',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¸ɎmЄѠϬʊʹќĤʽϓȜфɶԣ˪Ųdȥ\x96ǜťǺʘ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĺɞԋϙķϯʹȋӘϜŇаƚ¦Ϲɮ˂ήȩȡƕ=©ǲ6ȗ˚ńҌ£',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˗҇щǡҢʓЦОɨʤɇчʽҍʇǉ`õǮѵ˕1ǌñΠԖˤŃȬâ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ҍй˂Ǎ·͵ѯǠÕ¡ȽˬȇήÏ˅ȼƚųöġȅԌҴԡŐŋȾŖҡ',
                            'message': 'ĴǨʅѡҰƋҿҁĄǔŞȳɭёAʁȞ.ɡǯ~%*ѲɰқƼΙ©ȝ',
                            'arguments': [
                                        {
                                                        'name': 'ӿ\x87ϻēp@ǣ§ϜʖɜɐάlʉɋƘӣȻˉІ/ЎńţѣǰȰ\u0381Х',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӏ\x91ɇņųʘƯHʨʉӼЧƜɗǨΜɶεIȵѨԉƳΣŁƤ-ʹŐϞ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĸϽ¬ͰǢc\x94ҐǓªĺńҚõΕǓzԟσþҽȃ˨ƴѡѨǱʥƱϜ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǟʫҵѥĚȮʨԓɟÔŀ˪Ҩ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɐȷŁȲïЈ¥é˭ӏΛ˔ӘȿʑJŀδ®ċ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ţ2pBƽӬüvayΛSѥ¢ßœĄҗƘũÌ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȑ\x91ӽ¶ԅƷμЩѰгҿ˘ȰƔĿК˪ĝ˲ΞȾÆлɐќƘSąģ҄',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȦʑŦƮǝªұȞɈʐϦԞɉГŸ҃&¯Ȅö',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƮЄӱҫӶɩӾχLǔˬȖȘԒҙǔѣϨϴǅA\x8aɠʬH>ҺґВĭ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172724.916201:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɯ\u0378ȮƲÀϿɺӟ˴Ý2ԙҔѴ˾ƦцŞώɅŭˤҰðӊ-ȏAϐτ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3440564659369338104,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҙ¯ĔuԗŨɴϬǲԮӭϣˁɔ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 995517.2054092945,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '=ɤŃƘzԡƍѧҪѵX.ϾǦŲѶşʍūțгĚ\x83Øі˪лεӴѽ',
                            'message': 'ԠгʛҗӇǱʫ[˵бТѸҔʮҮ\x9b\x85ɶɅɯŕҦĠæƩŏԠɍΓκ',
                            'arguments': [
                                        {
                                                        'name': 'ϠԮʎӹ/ϖĝƷ¹ɭ¤',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Äÿ2;ʌʔȯ"ʄύɈҟӊӊGџʀzΎĬѴȩǓħɧ˧FćǰԚ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʊ˦˃tɛ\u038dҚёӦƕХ ˆ˰ѧƓ˴ϋҬǥƉРðìв',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4343953171156697927,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȞһıҸƬźľǔѴŸĽƢ\u038dƑаìĆǯɯѸɾ¹èҍԭpԧƈŽΡ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϗǽǁӸάҊǹƞȷɳ\x8eAӨҩҎОƿɠŵȫϿƔ4ĊɋΚĥâşƖ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӊĭēQōİŘƓdȏӸȭƖɍʰ(ʘ\u0378äǷ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҭƍɄŗӍuҖӈî¾ɇŚâ˼sЪϣΆǟťϋΈȉΎΊƝЅӿΎĀ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'èн҇Έ@ҍɐǯƋԦӕ»nǜ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172725.247315:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԩ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɎÜƃ·ȈԝǄƓϜćѓǏǠӆrūĩФќǣӼи\x97˲',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172725.320562:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ОұȌ҈ɫÑƅѧƗʛϪƫȀѮˢǓÚҗӸ҂ķҷtоõҔæƬȦͺ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1042718200006442048,
                                                                        },
                                                    },
                                        {
                                                        'name': 'и˱ΖȋаӮüi',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԗΑĆѧ:ј˧ʊ,ϸԛйϞΔԝǝbêΩƤđʻëϯǙŹļΛФĨ',
                            'message': 'ҊσСˮŖ˵ȩƼĸ·ƋĎƦȟͽŀоԑӦƿƅ5ÿΞӎӋӄцφΩ',
                            'arguments': [
                                        {
                                                        'name': 'ЬДÑşԄӡԓh˱ǂvΝі%ӹČͷѝhȐİϑʥΏӍ\x9cзâȩ¥',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ăͺƳ˷Ȉ¸ЏЕͶɑƲӚ1ɔѣȜӇ-Ѽ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΏΐφkԊӌƽ:Ҟ±sˇҢӏƿ҈Ρ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϵ\x8bưëӃ˔ҿƀХÇ˔˴ƃˢͰ\x92θ˩\x94',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'πѫ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172725.602295:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҼСĞźΡа˸ò\x94ġӕ¯ʗʟŔтҍԓŀӂǞϋɗΠɯЌ˨ƺʐҙ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 259634.78268998908,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ļŲ!áІǝɃфȶÆȮ˽Ē',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԋνɐƸǚȲǎƵвΆʃȝǆ˚ǈω',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЮɎЬӉ·ӻІԂÇљ\x9eƾD˔҆Ņǆ϶yɥͰϝԕӸȮҀι\x82ʠǣ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѴƵǾ\u038b\x80ӱȩɐͺɱɩȥʐ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '~КɒŁv¤ɅϙŒԢ\u0378ğРҞϢ\u0379ŖƯXҭΪҦéӠʊĝϕӊԕӳ',
                            'message': 'Ò\x92ʿӦδЂǠlͱȄʧu˶ϱϼȹōǽƄēʝţȤŢϵ˥ŔѨơή',
                            'arguments': [
                                        {
                                                        'name': 'ǍПӺĚ˕zμ;ùяȠ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɉUͼŤчǳÑлƇсΘǙҒ˙ɺ×',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƕɣ0Λ΄фǐɱSҳΧˠʙУ\x92τƅƴĴөҁȹ˧ʓƻiťŭ¥Ԇ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӱ¥ʞʒԊ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 969575.5658524132,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϣÆÂʩ÷ʆČϜǄʰԃ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 327902.6700377835,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΜӘо$/\x9dʿ-ӣAƼѱ~ԡǯȮȁǧ\x88кƐҗӰķͻɊЉƹÈ\u0381',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '8ˢ\x85ЁϟҔħǹʰзåłLˢ˸Ҍ8ʬԖȒϋƺӌ)ʔǶbɺд҄',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6497811949038933619,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Z#ԇԇУXƂƋ˞yɼԊԮО',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԁà\x98üɋ˃ĒˈýŪѳ\x8eиǁзЯvǭљТԤÕɼʇςѷҞ˳ķʗ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǭ҇ǺcΝϷ\x94ƒϑаVūŒǶƥ˓×ɂǫ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 142633.8890417309,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȎȌɏδƳŹŉЅƩ«ΔҔéҦ¿÷ŢӄѹЯξєɔȀȴûģƄԔӛ',
                            'message': 'XȠŌũôǻƄҷŽˊŚȐΰԐȽƙɓ\x83ʕ˹ӞɰčХ\u0382řȤˢ˦ȗ',
                            'arguments': [
                                        {
                                                        'name': 'ѹLϲƷ\u038dĄȹάʌǭѯĔѭԮȫԭ˼ʢ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ë',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԂʰҟđßөԞԣ˖ϠĆϠӃҌԪөӿІϠϾůƹɿӃ˃ЪҞɷΘȮ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '0Ҷ˗ĤÒäӆ!ѸŤЊózӥԁΖüÀÉŃơӕʯϕУ˔Ǫƚ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҧï×ҵȺӦɔɐƭĆŠԎǗʄʏě£ǭŰíŵҞԄ˸дұ\u038bɨ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172726.388185:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ň±ƩeɑҺơϊʅÿ˕ª˦˗Єů˙Χ˥ğ>ǍưȻ0ĢƔzϹʺ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '϶˹\x9dȑɜ˫|ǂɑȈzȤԉȸӼ©¦ӔÇӬΖʤҺΠш·ǳłϥʮ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'øɒ1АƧ\x89ʟčÌˣƦӤʹÂΊ-ϞΝΗ˘\xa0\u0381ͲѡMσžԊĔʬ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȲɂҵфЈ\u038dΙĦ"¿θ˗˹ƵȋŹɗЋƊ\xa0`ҠӿϦđϱёρύҸ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҝ\x97ρҳˇYÇ\x8cǣуÈҺǯ˛Ɯĝ}È`\u038dɔȞ˱ҤǣɅԮɗ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΓѸЏϵ˄Ӏ¥˜Ň˺ÉȨȢΘYŌȲΧǵȉƇӎ˯Ċ$ϡƫƔϮʏ',
                            'message': 'ˉФйш\x89ђàȞŰԜȹЎƽͻ\u0379ΤЦǷŚǣɀŹΝ\x8bÅ0ŹϢλ2',
                            'arguments': [
                                        {
                                                        'name': '/´NҲPόˣǍӵÅҲΈБҭϡҔѢЭƧŲ˲нȪʍҟÓԙŪћǈ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6831923962335757685,
                                                                        },
                                                    },
                                        {
                                                        'name': '˽ǫӐɗԇ;\u0381Ѣͷʩʟæͻҏ˻вӽӮѣȓЄʴ˾\x8aӫψԂ˰ˈȆ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '³ȍµ@ϝɻ¸ϣ\u03a2ҕҷϟȅ;\x87ϷɁċʡλͱӼ3<ˍǇѮK¼\u0380',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȯӂǷAƩԪƗǈƩќԇӧ¿ӶͷǈϣͶӪɤƃ>ӶůӑюʂŀѲ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ']ƻӂíǌ\x81ɭƄƈȓϙӖЪ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ͼLȬӍ˸ȖϼŕάǦ\x83Ěʭ\u038bԛôŤȦǑGȄȃЍNǍҢöġǙd',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x81PѤɎȢП¹ϳͱЫԣð\x8aϝĻƷŝӡ¼ДƱԈ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǖ¡ѸшЏɴ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˅ГƸΙǐOɀѣѩ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӌѠƝĔϻΖҐ\u0381ƱÜĕjʃŋбlƋ\x90ƖũϔпƟɸɖЫ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'sҘϾĜϿҷ˗ǛѮ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӡо',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172726.947150:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϺǞÂԎіћ¬ζқmɶÎŗҥɲɗbљϼʣ͵ƕ÷σÓċΧŁɰÜ',
                            'message': 'áϣ\u038dςҚτэ\u0381ʐɗɜˍEΧƓĐšïԍ¤ŵƑb|"ͱãĐƤҢ',
                            'arguments': [
                                        {
                                                        'name': '˫ҾўçȜɲʊśξɳǰӳÙŕʏűҸ·DӤŬΝЇΖҩňЕЦӔƁ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 202499.17818453838,
                                                                        },
                                                    },
                                        {
                                                        'name': '\\Δ˛ȄUɖҚ҇ҭʻŸƲ\x9eӓĎͰЏƉͶƲɏſ˚ί¾þʢҡˋϒ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŐLǃ\u0383è˦ϊMǊ\x9aȢÑʌάśƠЉć',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЅʽŃƩ,\u038dŉȺDŠnЧΨђȞ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 731597.524888633,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǚýf¦ČԧԄɋƬҲԈǄѺйȚԇǎӍōԚþʛɪӇЛɾԁʔЛӘ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'зüоɎģƠѩ˨ǆȱʮǢϱʩș˲ɣɀιƽ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3104359337618795199,
                                                                        },
                                                    },
                                        {
                                                        'name': '˛¸aϯƞ{ȷ\x9a¦\x9cҦŉѦƍ˺šʻȦ˨ρӕϺςR˻\x9a҃øԁв',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -73153.8080621557,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʞ˰Ϸϰǥaѓ҆Ȃ8Ǜ\x99Ȩ\u0379ήҫӵψҘϜҚ*;Ǵ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1230223871519852546,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϱȢџɊȱ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƛ\u03a2ʈʘȂǤ©҈ȵΒıìΈαʎӡØçėƫŤҾɖĝƗ˭йĖƁǋ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172727.336007:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˴҇ԊʅƳʶǿѝĸύӲӵԚ&ʹRPǶƇӏԌϜȅӍ±в·ЅϻЇ',
                            'message': 'Ҩʩȴʒ\x83ɰԚўKŁҴǹϡȹӌѱЍΊԧǗ9ʻӣǣθƍȷĹŶѵ',
                            'arguments': [
                                        {
                                                        'name': 'ġӧSĦˑТƄӤ\u038bȳԑӉ¯țђȸҗ\x82ßλБ:µӾпȑȋνɃĭ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'яҕ˸L˷ǑƆȨȮҐ÷ζlόҬŲȳӏς',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x96ɗÿϰ¡ƛѢӝшcΖʴõ˛',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 26680621040444192,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ОԚэʹϑʯǩϷŀӌ]ʌ3ԤŰфʹ҄ŀҥҖŠο˓:ƸɂɍɢȚ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172727.512983:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϑ\x84Ȅɂ{ф<ÙġϧЋɖΉѓʼƎɁͲԚ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƒƉ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'óүȎʱXR¿ҏŎȢяǏǛԑЏҫΙԜҠΜƔϏƳÜΩӿЄ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɔÁĔ\x9f˵A¥RӜ\u038bmɥŸʧȨӨѱ¨Řȍϛ\x89ˑ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '&@˭ˑǚӝƼԐĳĴǟˊѩӥ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '͵jΞˣӽÞJĊŘЇŰřȑɡБзãҵEѕЯґϣʺЈ˰Ɠ\u0380Ҥ¢',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172727.721683:+0000',
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

            'name': 'ͻӿʆ',

            'error': {
                'identifier': 'µÌ¥κư',
                'categories': [
                    'configuration',
                ],
                'messages': [
                    {
                            'catalog': 'ɰÜ',
                            'message': '˶',
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
            'event_id': 'ĳΡĒϿӴǣѾĽЪϒϻҨȈĥЩȕѳ\x9a(ʜ˧ѫЁ˥ȏŋιǞZ\\',
            'target_id': '.˟ǊͺѻʑҋïƥŹх˝ĕƴɦ$ĝϑhԪÂǔ°ԘÇˮɓþǨԒ',
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
                    'event_id': 'ȀӝĬ^ƚԤÎѲ¬ϩ¡ʧȌȡ\x9dƙ\u0379.əѼԉȚөeө\xadҋɫӟǲ',
                    'target_id': '3˟¼ɿ˞ƎČ§рĦЁѷҤSʹҬϋӺěǤŕx\u0381ҖΫӵɨϚ\x92ˠ',
                },
                {
                    'event_id': 'ƳĴɬτΈ҅ƟϟǽӾh˒śəҋҨƏӏԥʋӐ¨\x8c\x93ћʥȥiКʞ',
                    'target_id': 'ΔˤуφӘƚиĵðҒԅǵWҧņǆɂȌ\x94ɠĀо\x86ğωĤΨȨɫ϶',
                },
                {
                    'event_id': 'šǎ Ӯ\x88҆Ӝ˥В˥ϗáƓǖӼщӣ\u0380Οӕιӳ˼ŵӣλƫČεʆ',
                    'target_id': 'Ϭʮ@˟ȱΔ"ìϖƋњ\x8dϋҾΞĊĖǰȢǪʥӣȈ´»ʀɸїǬs',
                },
                {
                    'event_id': 'HȅʹŝӭxnϳӥŞҋJΔ\x9acyԫΕоƵýǩ҂˾\x82E<Ʊʺѻ',
                    'target_id': 'Yόĭv{ѸʯҪ\u038dʒўˣԇ˱ΑϫȕɘŠŒÉĸɟ˔ǏŅaŌƚȕ',
                },
                {
                    'event_id': '*kЩԉŒўǁȨ\u038dąвӨŜÜƨʴĶÄǞӫѺŔƙʵ\x8fLƠ˒ȍ˂',
                    'target_id': 'ɒǮǙҦˇoŁПϙҁҌüʄŮʠˎñ\x8bҀȘēʺɀĖϞͱǻѐѢɓ',
                },
                {
                    'event_id': '²´ʯ҃ΐʢˤΞǅʮʊɔ˳ϰѝѠ/ƛÕϠҝыӧ@э\x8eüƔÙȕ',
                    'target_id': 'äԔĒϕҏ#©ԞgѪ\x9aԥnǙȆлĈɐŻăĚјСϠљĻµȓ"Х',
                },
                {
                    'event_id': 'ơ\x92ϋԎɨΫÃҾ~өƇˁȓ\x9aŁҐųвнƣΚčǯȣ¶ԗúĀћ_',
                    'target_id': 'Κѐ\x98γǲΥȗϻĆĞӼ¾\xa0ʭȮηӭȳ¹жţʆʰɐϓǔԁŉ˨ƾ',
                },
                {
                    'event_id': 'ЭЂԣϱRFƲёs˸Ϋg˃ǪјΚ҇¡ɲяʩǥϞӊѽӍŮ?ɫƇ',
                    'target_id': 'ˌюüʄȲʱ˄ΚϤϵӆǌӜԩ˾ѣͼ˴ýȎɝ¸ðǉġɨӁÒɟÞ',
                },
                {
                    'event_id': 'ÅчƮМɡjӮ5ĎĝÜ®ņӰѶʞӯғĠɅɘʌ҈ƱӍ˚ˎÿԁѴ',
                    'target_id': 'ȍɗĉi»ÎΤ϶\x9e˟ДЪаΝњҏǨķҗώϕ\u0378ʐįͽǼӍВΟԙ',
                },
                {
                    'event_id': 'ňǿȗ4EŞѥƫˌ<ǸͰѴ˫ŗ®ȊӭĭҖԔѷӧþɡɜԫЕðϺ',
                    'target_id': '*˰ŅâɋϝѧƐȁӁĊүĳќ\x9aˇƗŋĤѓѸ\x90ɞϩÙÂIɃzІ',
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
                    'event_id': '\x8f¯ΟÄȨҀεřÅ^ºɞΤȲίь˫ĿДИ\x86ĜџÐŝãΫπӻӂ',
                    'target_id': "аęȽШƅɨӪŝԬȟΰ҆ǑöŢ'ÐԎϴ\x94~ɻƇѷӥӑɠáȐɿ",
                },
                {
                    'event_id': 'ɪĢʧȃȾЊįç%\x9d\u0380˨ҒυϣˣlҽĮζΓԓƌԌϵűƤʭңŉ',
                    'target_id': '=ǙʞʡԡʏǼcŊϸĶќӥ϶ЇŶ®ʲčƹҧЋѣSéǑ$Ζïқ',
                },
                {
                    'event_id': 'ÎJϬ`ȷŋϣѦɣϋ˅ɅЁѡƷęɳАɎǞɏѤ³їΦæʂѨď˃',
                    'target_id': 'ȠӵƇƴӞύ\x9eЎƭАӅȮēΜˋʸaЁɺȋƾʖĕЫ\x83ȧ*ƃҚҽ',
                },
                {
                    'event_id': 'Ϫ˙ďϒƷщЁǢԅҳʿпĨ¹ñȁɩƓǄǈŬͺҁѴΞˡŽҀýͼ',
                    'target_id': 'Ϻˍ˶Щȭ҂ɪмУёѧϑƊǘӔŹƊǚѲɓԟ«ƦɚɷƫǗ\x92ʷɗ',
                },
                {
                    'event_id': '˭ȒfϝӊͶȭNșж\x94sƇƖюȊǦ{шɗȤ>ʫˁҕѧĞѷѸɠ',
                    'target_id': 'ɍƕlˬԠǕʴϞƟeÖƆї!×ȤʓԞɧßʞ\u0383ԔϹȆӚĒ#ӽƈ',
                },
                {
                    'event_id': 'Яєƀә>ǕĮFȬȖϞǿGӕϦɒԉ\u0378ϴĿȯɿȏʲ£ԤϕĹˡһ',
                    'target_id': '.\x82ѥԔʣҼӇ˹Ƽɚ²9҇ƨǓĻлŪαYƟ˱Ņʆă\x8bȕɼȁ',
                },
                {
                    'event_id': 'ƠҜÄԆɗѡԥň¶ċУ´ɽȁǃϗӣжȸȐτ˽ɌīҲƲǧŉłˤ',
                    'target_id': 'ԌëϮȅȫʪĊҸнȻƅÙαʢõƏ\x9d˭¦āqΩϓ\x8fŷϸVђ˔Ψ',
                },
                {
                    'event_id': 'ӣϥ/Ӹɳ\u0381ҟǗ\x975ѓʊɏѥЖŪǱјǉ҅ɅўҘOǯŃʛӿѡʪ',
                    'target_id': 'ͳǾκʛϴɋӼȷʘė¾ӹŧȀǧƩ\x88Ńʢˈһʾҿ˓1ǔ˻"øб',
                },
                {
                    'event_id': 'ӆŤτԅψǞəэ\x88ϨNϫϙΚɧŔþƉbʡҢɣóүɟӣǯ8ϝƗ',
                    'target_id': 'qƉ¾ÄЯȕ ĲԀýȓ\x84ÇȲȿ˨Јź˭Ȱϧ!ɴó²ЃvǦГє',
                },
                {
                    'event_id': 'ʫηϝǪѱӌʂɆŐȩŝόҪØÆõʁ˪ѻ˨ҍΈÃőǄŒ\x8cǯϼе',
                    'target_id': 'ŹгņǝŠʞĥŽ¾ƊʏvĤͲԜзϙѻԐ˶ɝ҄éӆ϶ýνԂɕė',
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
