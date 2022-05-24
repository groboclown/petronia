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
                '\x9dʂϠӴԡϵTǑHԅaŴӛНɕťѕΟХεŃˀɧΥĔʶúǴҵk',
                '˝ĽԨĳºʐ\x8fɡ˺ҕΛӒiɪԗȇ˄ǮѳʿîɿҠʟʶӰ¥сОŢ',
                'ǊƧćŇĀ\x9aӏ¼ϨΣɵѢǾфӹOɎ\x94\u0383εҜŕңəcǁǨȨύρ',
                'Ɵϋ®ɥӆƓŻƀ\x83гƺMʟȞ²ƟҤ·ѵδƧưưGïƊɌ6ĀT',
                'М!ь˯ѪпǿԖͲɒʌˉǠʥľͱҬȻÚn\x98q˶Ғȸ»ǑŀĴɔ',
                'ˢѦeQőɻԤҞưɑΡӑӓ\x9fŏФ\x95\x8fͶтɦƩ\u0383ҹÿ˰ǗȠ³Ӽ',
                'ʁ"ƙїӴѫȠԉɸηӐƗүưԊЭЦ΄ǽɶďKюʎýǷŻͶªą',
                'ˬƯɽϣͳQöϽЫºƩȦīЂƓñȖγѷј˾+˞ñҭёș\u0383ĽͿ',
                'ȴơҳÆƏӻ˕ʢԉbĵÙEǣӧƯˌ\x9dƳþĬ\u0378ǴǷˆП˅ԨũЬ',
                'ĖÂԤ˷ϓ=ѕԪÎĵĀΡόwƅЙЩžŻƂҿƏÑӵ{ȲǻѮ˦ź',
            ],
            'source_id_prefixes': [
                'ίӣГоǽȿɬΖїãɪȣԘΧШ\x84ʑíĚāѤͰ\x96ȜØɄňôȧ¢',
                "'ʮœŌӎǺżԬҜ϶a)ƹ\x94ПĹʊӻƠϼҁƲҼVκˇϮRΓŴ",
                'ӟμϚХgųӮЋȖ˻ȕϦϴƲЌȥӜ\xa0ʕӵ҆Ш\x98ʛίԌ¼ɠԮӝ',
                'јƲʦӴĶϟ}ԑωƩѣ\x8aђƉϞѴƉНƬ˄Ȝ3?ɻɜҗƥÓŷ\x91',
                'ѰӐƧρКʭɁƾĒʚĢƖɺÍԭƆϺΪÖQуϽѣǣϵ΅ѺSƨî',
                'ąʻЍǃǅfĄȐҏƏǢ҅˽˅ƃs2˪\x9aԓН҂ѦÁǾĒϖ˴Ϳυ',
                'ΓɛνҶQƺ;ǁvʂHƔ\x9f˒ǘɮˏɔ\x9aѿҍʜǆХҪ\u0381ŵʩҍǖ',
                'Λ½ƺԞȹVň\u038bãÖ˅ȹÔѨƩѥяõ\x8bńӴɥ\x98ͻ˔Җɍư˛Ү',
                'ӼлġѿŵˆƨыѶ4ҧҚӅϥѢ˝ŒдƏЪUȒ\u0380ɞϭɗȚÕɤё',
                'ȐΞҒҙΑWіɛțʺȰ½ɜȁϷœȋѳzӫǮȱγĒӰΏ<зiέ',
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
            'action': 'ȾĲϛӱNγОӠǴļǄɸ\x81ƛŞŹíўǤGСšȮĨrƝʗDТБ',
            'resources': [
                'ŨƇɩúĸƫʺˤɛƲӿɭǘěïΓŋВԜÅӷӽ˚ƱοϾ˯ðIӟ',
                'ϮɰĦuӟ\x80χԆɵ˛JϢ?Ľ¼ϔї҈ѧρҊԩüʘҗ\x92˲ʲɂ"',
                'κΑAҊɺ\x90|\x89ʙʿВϓřΦюęθҷаԅ˛ȤƍҸǩŕҕӳѬɕ',
                'ΚǢôͳӿԬļ˅ңîıĵúʔȂˮ˴Źʣɂ,ѾЍϟЦkj\x90˕¦',
                'ӸƞГгʛΠɓҿȽɑ\x88ѨӒfɌъĖ\x90\x85ƏɇʖʴΤѠɳʓΊĒԇ',
                'ƇԑħÃǁǡҬɂЛύÏǐǀˣ\x95ȰЩάњЩlЦӪɫșɾӜӱѝĈ',
                'ЪÓλy\x9dƗТњҞʴƾΡνEÖΞÝȟɰÌԝǽк҃ҩξʫԙȨӍ',
                'ɊѣӴŶƇĥǘТʪĐŘȠȱЭ˅ˈņ˽ԏǏėĩˏѤùͲ¦ëȉ˪',
                '§f\x88ī0ӲʟèДƸ\x8a&ʎíƫԜҺųơ˽ԡӵʢʰɤòџ\u038b@ɢ',
                '@ú\x8cāԆǞ(ʽµ¿ѓӫđԭԄѷȎɎ;ԈХϬСѧÏ\xa0\x94ʎŧȒ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'ŵ',

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
            'name': 'Ώ4ɛƦĲӐ҄ҖщӾΕɦƌѠġϝɡʿϒ˓ÇƥDȭʪƥǭѼ¹ο',
            'version': [
                -1655526887182147245,
                -1854773998918865303,
                -7849921005352584503,
            ],
            'location': [
                'ԡͺ<œ˘4LҫΝ˙ǩ҃mѦƲȨԬԙϩАȗľДАʐˌϩŘ\x84ƨ',
                'ʷǡԭɟǜϻϰ\x9bO¢\u0381ǦWɐʗЕҷɣ1šĂΟɑţADуÕͱˇ',
                'ӯŭӐТŐǻɣŻԄѳȵϱÑ;҈ɏӌϓӿҨФӀБʓ}ʫˋǎņȤ',
                'ΌκɞǧÜƝȳȜβĲīԖӝωɁƙɨЫÚǠҗӾɁύ˸ԦЀ\x8fĞѾ',
                'ɞɱǯíήɼρИУԌϔŨ±öè2*ǃĤǲʶϤ\x80ӢȺҬќʆʝƙ',
                'γѩƜҾä҄qǔ"ʊӣӏŢԀӽȧƧԚҭϏŏчìϸȠÍéͱO˚',
                'ѱͻЦŏ>ʮØҚɆɡƯ\x94ƹ\u0383Ɯ҃ʳϷʨMɰĬȫʥĲ\x82Δǁ<Ԓ',
                '\x8fȮʴʯЈÌŔӺ\x7fϿɋś\x8d0еҡәʑΚȥɲӳрŪӁͳBͲîϊ',
                'ľ\x93ˠěÈΎǝ˝ӓɽĘȤ6"żǟ҇ɨǺȆpÚƕC<ɊѢԜ˛˸',
                'Ŗ˪͵Ԧԙσĸ4ʪžoԮѩϺǹɯѐʢtĔ"ВͳԖɘǩϧwοş',
            ],
            'runtime': '҅ʡƵɫɝƻ˵5ƺȻǨʢ',
            'send_access': {
                'event_ids': [
                    'ԫɕÓӲΔľАԚхЄѻȐ®\u0381ɺ³9ΓˠĖȬҹɞȻ˵÷˔Ѫ¾ѹ',
                    'гӪȴº7ѽņюʆĈɅɴǷıӼöϬʨӑΊāЅÝ+ǃϖ"ϻǿȈ',
                    'Ǻоșҙ+ԧʪ˯ĝȓ\x8aŀԭôȜÿþͿ!ɽɟɎ˷ϰ҆*ǦԛӅɿ',
                    'ȢμʦЧŜӯ5ѹ6Ǿԕӄʝˏԫ\u038dƻÇηυƣüɍĚ˓оӟњÇƏ',
                    '\x97ÝЉĆƔ˞\x82zҬŇкʫƠΝӄϥˣʋRdѪҡɱǾќʩʮ\u038bȵʩ',
                    'ͲźˠƮļˑŴƜŃL\x9cȗҮƷΖǒǽȰɈӳŴèδ=лƶʟӢğΘ',
                    'ɓƉǒxiŉѐˑńŰāԁˌΚ\x88Ĭƭдҕ-ȃŋΌўNĝԭғԣ\x9b',
                    'ɄӫȚɑԥΏБңĖƝѲʟŲʙҵ@ʥȤʜΣŉʼÛˏȱCѐ˖-ł',
                    'Ǯ<\x86ФԠɠҍԇӀӄŇԪȧˠԖƔϚɊÝ҈Ң5ӢƯΑҾÎѱŠų',
                    'ЀЋ³ƸnҕǳˤřΏ\x8fŠЈҶӆҫÓ×ʾʑͽӑŵʅǌк7ΓˡÎ',
                ],
                'source_id_prefixes': [
                    'ȋ˄fτҕΤǑϑʒѕÝͻʄěŝĴyΪҨşпļƙʄҶ˞ɟŠԜέ',
                    'ДЮѻŚǳͱҁͼәӓġΝ˳ѱԑԪƙ˗εƣӐĕ˃ÜÆИ)Ԥňǽ',
                    'ŵŦԒѽʹȌÚӉˌëı\u0380Іç˨С¯ˏȐʅˬźρĬθ\u0380ѿӆХ϶',
                    'ҧŵ\u0383Ǝ\\ԍМƩˑƫġόҏ§\x94ΝΟǨȩ\x902΄rŚԎɢ҂ĝӥЦ',
                    '\x9eǺхĤũȣϜRǃϸɩӆ\x97&ιĚҨƆʼþͰĎÛðΗ3ĘʗÀя',
                    'ΠƩϜƔԈœҨхÈӾżә$ϓʼɛžуЄԖeʫǉȯҸzÁ\u038bϾÀ',
                    'ƣǠų~НыƒϣÕӊѽӚFԠĀЎԁΔӠԭбόƳΌљϭЛӋˬg',
                    'ԧѳò˶ȭʠԚ¦āƙѵʌ4Ėƫҝųέƀzɚ\x86ӵʥΫŸɽƗϰĀ',
                    'ӴҚƁƨǗ˻ӈÇƂɾȎУ´ψ҈ɏ˧ÉɌbΝҸ˷\u0378ЧņЪϚΖԖ',
                    'ǟӭϫԃöųĴȩɊȘˮǮӯ˾=ʠÛЃӣҷȮӖɇżњҋϕӽĐQ',
                ],
            },
            'configuration': 'ÌҭǫҟϺЊşΰř$ҪƦЀӗҴcXȓȽȺƆϫwΩɥɨϣԜΉԦ',
            'permissions': [
                {
                    'action': 'kǻ&αǡˉǒɊѮǝЙԫdԗԜԊЯѝҶÅȤ5Ľв˖:ĺҦŰǋ',
                    'resources': [
                            'ԌμΘYÏbϑɌɕ°ĎĊ¢ϢШоϧOҰІͳʩɘʤʒƩ½¨+¬',
                            'ʱˍŭΰƚȠʱкʦ\x91ÈʲͺζɥŷӐЯüƟέŴǀȿǇҡҌ®ÖȮ',
                            'ŻƣЙ$äЎМ\x94ǔiωϑɭųқ·ӁȶNҢʶԒЏƞQĢκÕƣȜ',
                            '\x8eΤԈɤʜͽȍ(ӹνҝϐΓӷŀ\x86ӗҩʯɌϗʪҬÜ©ԞɂÀĐ?',
                            'uçЭ˼ǌÈȊҲŉЍżȫǽʢп˧Ȥ¶ЩǱӣûƭƀXƆЃͽÁċ',
                            'žϽΚɈПγȋЭ&§ŬƾǨʮŊ/Òŗô˙:ʏéćȱѼǏ@ҜN',
                            'ƘɋƸ9\x8eɈIɇʖǇΈǭӐƓƤϙâЛβҸƂʯϩƽÝņȠ;ӭс',
                            'ʱϋӾӺЬ¶Э\u038dȁԮ\u038bˈŸFǭħȭϝ¬ȟ;Aџ\x9fЃu˕ÖŽ˥',
                            '\\ȼϠƲˡŊѵȌ¤ȝÇɏԃĈǉ£άθę°ϩIɦoԭҺҐŪ˫ҕ',
                            'ÎʐɆԣԊ҃]řӈɑɇÁԕҔ·ÚÓϐǟ·˴ĦʣњђˡɹʚGƪ',
                        ],
                },
                {
                    'action': 'ɛӹϲvԃɷƮӳũԋχho3ųΉҝ˪Â<βӲǋ҆ЭcßоʜĆ',
                    'resources': [
                            'ѺƤÑð\u0379Ɛˮ\x81ȃÍŔϧρʁҿѸϱӼżʧӻĆґŔł\x9bʾϤ\x86ʮ',
                            'Ϛ\xad#кӔˎΊΕ˨ɏʯAïƮΙҰʑГΞżȆЃeÞҜ/ǨǒЗҸ',
                            'ΐОӝҨŻҠӼѓȦpĿǌ˺іŭŇťӴƅřÃȦșԑϤĢ\x7fǪò{',
                            'ЀԨˆҽJɡÕϼƅ(ҘŐŋ˧Ӓґ\x8cԢ\x9aȣå˓Ğѕԩ/ˆΚǼԗ',
                            'ԟԍŮӍěŢ\x89ΑɻпąͶWÑǐԀĵRÃɥǬɣȦ\x95ȳȒĹю\x84Й',
                            'ӄǷǏλŏƣт5ϓ\u0382ˇқѵϬğƮΚ·ѡФʿυiԠˇĠEάŠ©',
                            'ǈQǷăŎԀƁİæϞ҂˙Ƿ˟ƉΚҔƼʲԩҳo¤г§ŵńɀͺ^',
                            '\x8dЋΤʰçAй-ԌFÁÙǓ҈ŽҸЙƘ϶˂ǂȏͳԕҍԫɜÊƥΓ',
                            ':ԏɩɖрЗӄӬƫǋłӡЫϭYħєƘї²ƁЙԇџͽ;ΘӱΏȈ',
                            'ɖΫˏ[ɮȂ\x8cƵʭĉҌʎɦԀǮҮʨӲƳAȆőυÒҤѫҵϜѹȎ',
                        ],
                },
                {
                    'action': 'ϙˀʔԛ\x83ϰӖωӃȂԄѷʠˉ\x8c·Ȏőѻ',
                    'resources': [
                            'ьɅӎЊǾɕŞƔƼтɈë˪ӁȾĀȺ¦ӪČґŕϫȠǗѝѳƤҔƅ',
                            'ƏԔŎϸŗĖе\xadɰЄķїâÀԙʆϼ-Ӊ\u0380ҥʧɰɑѲ3ӈҫ_¼',
                            'ðӕ\x99tI\x83ƲрƶȼχЧƿνɲɉȤ˜ӹé͵у΄і˕ԅӯŰʰӚ',
                            'Ӗ\x8fҼʬ\x8faèǰȥĚ˸ΘѲƗ\x89ǻŔ«ҽӍԩ΅ъʃҬѶҿɯлɏ',
                            'Áß\u03a2ӹѻѣҨԓΛӰϚƑȉӉͺêҼ҇ŚŞԍΜJȳ\x86ˌҏƕ\x98ʝ',
                            'Îύұ³ïʢÌČ\x8dĮьɐyɐȐϊȉӿ2²ɟ¤ɉˆӓЗ˒ȡҢș',
                            'Ǉҟ?ùȁтɮʦΑˢϓɓѽ˞EϋΌȡЇˇɻiφȿǠˀɜӆčψ',
                            'ƋƾԏϻΘĝɾιѝƎƃǿʳѡɏƈΡ(θʧǳҎȹǢԊӻšԒǣɲ',
                            'ϗĲΩФ˽ǚ˜ɭΧ\x98ҦɳÐσøģǿӿ\x8dчûѧԠԂӻϽÔ£Jĺ',
                            'ѩȱ\x9eӞɠlҩĎʓԇʿƛ\x98ɯȴҞnǾÏχŔ\u0380ƟѵƷǇюˢaԉ',
                        ],
                },
                {
                    'action': 'ȅœŴ>гΪАԁKѸ7@ȋǐ×ÄaΫȄGûġНú\x98ʻ͵ʨб~',
                    'resources': [
                            '΄öƝ»хɨ°ϰЇАґɊïɳҬњǑņƾ˵Ŵ˦ŖȔLԓąϧĠϯ',
                            'ſɫɩȲ>ɱʨɇӫ´ZҙΦʠΨdğұУЄғφӆάҋ\x86\x8dƻɤЦ',
                            'ҩƞʲȊѓÿWͶé˱τüɚһѼűԫȧԀ҇щʲ˵ʦʥ¼Ǉ¬°ɿ',
                            'ƹҢҀ҂ҏĮʍ҂Ϋ\x8dΚuӢҊ`˙ÂšǼɠƛеŐĄȏΟ˸ŎϫɆ',
                            'ӴԭΥ\x97Ŝϫ3\x82˴ĤҥĀ˯џˉԢʴӹɾɈſȘɇ\u03a2ȏ´ȐËŭˊ',
                            'ƠѺѼşĺΧĎʅӷю¡їȞУӺϘκƴӱ˥ΐɹpBƘϋҸбţԇ',
                            '˂ɔҩȉgÒːҋɒȝЭЁɒӜѾƗԃćřδώŇԒʲĎӘҜɧХԆ',
                            'ŗʘǀБԘΣѕΟ˖ϪǢÓӔǋyЁȌЬƭԔӗǺǤԓǈʪġԅ«ԍ',
                            'ϿԓΦǹːύԁˮĜƸ*Əóȋԉȇˁ˄ňƂȈÍuԝ[ÖУâˌ˛',
                            'јӨȂɦǦԬˡҏă\x8bȮlǡѯӴƉӾρ>ƓӮҴ˯ɛѫŀЅ΄\x9aĉ',
                        ],
                },
                {
                    'action': 'ͺ\x81џёÈ˕ȐĈўãŹ\x8a!Ј_\x87ҒÊ\x7fϮŢòʽØȫ\x9aɒŖѴʚ',
                    'resources': [
                            'ЇÃҲèŊΓϮοFήmƏxϺȲͺƭǈſǒ@©ҫӆϥɜŤˑ4Ӌ',
                            'Ƕĝ¿ǴЄȡΓ\u0378ϧȎĴ˴ΊΆŧΖйΨ˥ʹʳÚњɡ˻ѷƤАɿű',
                            'ˢʵÈʯҝĴ¿ɦƸ҈҃іǡeОіϨКƸλҮ˅ҨĈÛԧҩœӹƳ',
                            '\x9aÊΒԗΤЮнңҜˎȆԮψƭǑЧ=ӢŽKĂȮɄЯϣϸSĲӬŌ',
                            'ƻˡ˫ЄӁ¤ēӎ˓ϘMϢȌ΅ǺɔѢ-ɤг˖Љ\x85˞ʿĂìȃʤÊ',
                            'ĎřȟʕǱшƔȶƄѐҨʲЃ˝ԖƺÈщӹP˟Ϸɐ÷ϖψˊľØѶ',
                            '˦ǣμϫƧѐÐԌϝĭӬ˰Ηţƾ3ύ˼Ім҂ϥƳċ£ΡiǶŻԄ',
                            'ȳĽЫÂȌϳɘѺɽǆǹԤϊ҆ϸЙЃǅΩяɏМΞiõǃłËҍο',
                            'ŝбҚԓ¯ϟαҤǑ˂ӂќÐȈȴŏǩЌΩªˎӄίǹӻʆѢϕÃϕ',
                            'ΒΎϪØÄǵ҇ɵʚ·ʼǤǃѧхԆ˭ÂȩҔăξ¿ϚѹνϖϒΥԧ',
                        ],
                },
                {
                    'action': 'ˋ\x8eȯśț\x80ўҹҮĝρ$ŰԀʻȿѥѯ¥ɭ,тϢ˕ƎΑΘT\x95ɹ',
                    'resources': [
                            'ԭН}ˤǲ\x81ΧɣŵѺ˸ǥШ˕ȝȶ*ѷZȫӷŢӱрʎԙʎÌϡǐ',
                            'ˌʢΙƴǆпϻĪɍÍ>ӍŴ\x92XʤɂәŌԞȾǓŽшȐѶýɎʤÁ',
                            'MąƽƾЏǇśҋɂʂϻʥѶƧѤǒǖŶɑĦψŦÐϝ_×ϘԘʡл',
                            'ɆśοȳȽ\x91ɒɴƐ\x9bɢƉɖԕ˰Öʗ\x98иà҄ʗą\u03a2Ν˙ςόȡ\u0379',
                            'qѵґɥ©ʸ6ȸɫĘ\u0378ĖϟϫĖ1ҧǿΛȥʬ˅ΞȫϺð´ʶȅĐ',
                            'ԟ˦¡ǡǩƎàǼћȃɡɨrйїɊΪЫԅԅΒ˘~áжҞϥā\x8d҈',
                            ')\x99NӹȎċ\u0378ʭiϵϰӓƻ!ЈΗ\x94ɝÃŶƳέρЗˡ҆ԕǥRČ',
                            'θƢ\x82ĠW\x9d˙\x88űԌҿwņȮѨ*ԋӽɩÝɐǒTUϪˎӠҧδû',
                            'łԝɾӄɧˇÜӴӹÿ¬ΎԟLԋԌɾƕ\u0382ȶΩ˴ɧЕв\x83ȧǄ¾ ',
                            'ςʢǧɣЍƇңԔ˓āρŴŸ×СӞʞȈҾƬфõ«ǉ)ȠɂӺǼ\x9d',
                        ],
                },
                {
                    'action': 'ǤҽƪĎӆåƀҨ7\x85ǃμƈǉ*ŜϻŴÄŐǲϳÞƩѭЖǡÊǷӬ',
                    'resources': [
                            'ѻǖ:ҩЯҽԟǘͻʹȜ\x9cԝĿǴʨĈʬ˘ҼÄåˤΎѺѮ*Ќʛи',
                            'хȔҝНƥīԁʷöˑӹLʏѮΨɅ×ƖԁѥĒȠҍНτKɩѱͱE',
                            'ſʵӅʤÑȘэ·ԙȹɣ¦ɋ/óԔ\x83ƟƃƜȠƼ\x84ʝүƊĘλÄѻ',
                            'ΎJȶȌӤƺĐáCϔҎцҦ˺Ñ?ҿǩİϦЫĸѥǗҔ=˅-ô\u0382',
                            'ӖͶԣØŉұ\x95îgπ˗\u038dˁƘȑţȤě\u0381ˣœǦ˸гӯ˪0¦Ѱ\x9f',
                            'ź\x84ӰγɣÚʎǗ҈@ǡɀ\x8aÃΐuˊŠΣƬҒɈĿcʠƖĐӴǨq',
                            "ŷ'ӛҎŻоǠҞ˫Ӝ˄ĂÅŔǃԡɨƸÕΧÍЏâĥąȝ°ĬÜœ",
                            'Ǎ˪{!Ε3ϪϜӡțþȄѨɅϔʈƾɊѧɪэiΓĆĮέgѦŌЯ',
                            'ɻԙ҂ƦԁˮЖUэȀϙҁ\x80ǮʎҎƥǕԌŲʭҞӗǢÚËǾɧɧ˽',
                            'ĤāҔŮϢŶȧˁҋӺӑѠ\x95дӜKƑĉƢÒ\u0380¥ѳќȱ2aѨς\x82',
                        ],
                },
                {
                    'action': 'Ǯ©yύǇʮ·ϖǫɬƗ)Ϣ\u0380ϺфҲȩ¯ԢӿȯђɧɅ5ԠęȖŶ',
                    'resources': [
                            'Ύ¿Ĕ\x85ԦȧÐϦљTȂӺǝӸ\x8d¸ǤŮιэӰƤ˨ҡȊæƲěʅg',
                            'ԑʄĹĪǳҡϣZ\u0382òԣċµʱ҈\xadĪыƾѥSÁʕʁфҏƅҁҊƂ',
                            'ʝѴʘӓȌŏӯҪлԠφĶ˫ԌӬэĥˇʶóǚӫӍԇƾķ0ŊʋǸ',
                            '\u0378ĵϢ\xa0ЅӷђBɞҲʟʂӫɗǐԖǺϊ\x96ԅʋˤҺʅ˕\x89ѼѭāԎ',
                            'ʨƽͼньbŝȽȝҩǇʌѯ\u0381¯ͰҽԦʗϨʬ(ķƓɰŌɣͲɖё',
                            'ØѤξƁʜͰҼāӵӜЧУԜʸɥ?ƱÖȖѥȳѹԧ¸ćиʨШӺƒ',
                            '˹+оЇǬɏŦǏм2Zʗ˅Ǻ¹őƻĢȣʬƚҚżʨǱгιԕ\x8aƳ',
                            'ĉʁϧӔĽԤąĬБϐέȒ\x95ŲɦЁəƝĦϴҜH?ŶћɠśЙĎԨ',
                            'ΰӎɉϤѽĂśɎŢԧΣʠIҲzÐȧЁĎԁȂϔN#ƅíƽəҿϾ',
                            'ėϝǱʧȤê\x87ʁϘѹƸΥЈ\x95ԚʵăqЏ\u038b×˔\x99ăʾɘM\x93(Á',
                        ],
                },
                {
                    'action': 'Й\u0382ĽɌҰчȰɔϑƹɞ9ʋ×εɻɳľΕԡϢΚϯũ\x86ΓOˁǉǿ',
                    'resources': [
                            'ǬϊǜԝȰǺһřƆΚšσšĨ\x82ψ\u0378ӗɝҬʲх\x86ǨʰÕʌόЇӺ',
                            'ͲѧČŘğкo8ʓŁƲԞѹǍÏµҊ«ʠӲw\x9eƬĚӽмӗȧĈŸ',
                            'ĐԐυҠαĘu.Ѷ_Í˺˾ȅĠʓŖȘ˰ˋҀҵČ§\u0378ƜʔǢ³ԫ',
                            'ä<РĻƥī\x92ǐoӖȝҬɖȱЅԮшÀǲӲрŷу?\x9eѸЛΜӣȆ',
                            'НІцôӜǣʪΧȞаǧŲʻѸϭɭáӭƼҤMΛѺ¹ƨɩěλǂˮ',
                            'ѓîʱЂ˨˾xǻƞȊãÓ˖ʵƵόϖƠŵҘώЧÞȡӹ˰ƓҶ\x97њ',
                            '¾ɿ\x88dŌŝ¶ѰʷΔԀˢ\x88ȅϷ\x98vЂҝѲ\x97Ƹ}Ƹrͱƈ/ϓΒ',
                            'ϼ±ȭ˟ɨԨy§=ɱƈπηˢǧʰǟˀѢԠ˚КӵÕũД¼åϲƒ',
                            'ѻ͵ҥЌÍȕ',
                            'ȬμѾĿɔlԓɾȣƿŚʕϞçѼзüҦϩȡӠǔѯŃŇĊA˄ʌϰ',
                        ],
                },
                {
                    'action': 'жŜӃҟҜё×ǅűıʀQ\xa0ê0ϠīƉȉηŻȈϴĵ<īʉƚөτ',
                    'resources': [
                            'Ҹˤ\x7fʅhě©\x84§ǑЌʽƌ¯ҬÞƗȕά\x80ι±ǢɊͼΘӮ9ɖͰ',
                            'é\x85˜Þω\\ǻȄŮ\u03a2ĪңļΓńȊʊÑ\x8cȈĤ˹\x93ĮәƮsЍ\x87ө',
                            'ȦƳ\x97ʘ˟ɼťů\x8aʲɞǸ·\xadȥYҮÁ\x9c\x93ǬşЫŴųɣВù\x83Ү',
                            'ҳƉƩϫͽå҈ƃϣǜ_>ӹɨԙЗҾϳǘЙ\x91ɱ7ҎӖÇIѻƜÑ',
                            'ɫϼȀçωLӜǼǘǹPːĨËЦ˪\u038dˮҊƓɧъӻʔxǾÁòƵϰ',
                            'ӟѤ\x85Ϛλ;ëϬѢӞ¢ȍŏØɾǻӵŀȽŲƬɓǶӜϭȅľѐӛϙ',
                            'ǪюΑѾѹȕ¼ðĞҴ¶҂ŴϗɒԣüwԡñǡɅτŀǗέ=Ȃƙϥ',
                            'Ч҉Ӯ½ĶΌˁԞ\x8c˛Ϳ΅ȎϲȺ3ȦӖƏŦďƘѵŕǕ\x98öЙҘʸ',
                            'ʂӍӟʬˠʲÌбНŒʇȀ!ϺƵnόƌ\xadàӐʿƴͶ\x93<ȌǏŲĞ',
                            '\x85SτԧԮó4ԗűЎđѣğʭ\u0382¨рóįκZǎΫϙζљϝěӏ\x8d',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ƈ\x91Ñ',

            'version': [
                -5449862757870099974,
                -3778427359570241010,
                -7953463959439431236,
            ],

            'location': [
                'ʟ',
            ],

            'runtime': 'Ǵ',

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
            'name': 'zбҎҹ˶ıэ\x82Ʌįʢ²',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ɱjʋ',

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
            '$': '<ԤVċWˬϾʗΒ*Ǭʳȹƥ\x85ċ\xa0Ԏî8ӒņÍɻɝμǍ~Ƴ\u038b',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 2246038842604695409,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 589271.856260362,
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
            '$': '20220523:220031.871851:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ОѥżȒӄȌӱӨîкҁǍЭԑì҆ǽƯɾŜӐΈԁΑŇŷïΐеƞ',
                ':ϝЀ\x93Әˁa\x97õӼ\x9eԜíϓϳҵз˽\x87ҰϧԘ³ϪҙҠʱĴϼĴ',
                'õɁаұ˅ţƔƝҠƟԤ\xa0ȬĤ\x95ıĄӂ˒ĕ0ӵʦùǫư-lɦů',
                'ȼ\x8fƯĚ\u038dҜ˹ШԇŤқΉ\x99ԭĶβǭŬӅӇ½ͱäгʍʮ͵ԅˡǀ',
                'ǰȬ¹ǵ°Ϗτ˒ʙĴ\x8aҟjѡɐϺňԒΦ1ɦ3ŝƖȗægħĦ҂',
                'DňoĄ҆Ȏ\x9dŔÖѭɉȴ±ȷ\x89ˈsĭ\u0381ԪҦшľЖϲŻÐϰөȽ',
                'ҍӛáʋӖčɑƱϱƳŚ\u0383ɡЏɕĸ=\u0379ǕĴӇýʽͳɝˊ½ѦǢǲ',
                'ȇӹēѠʅԌɅðϘʍϙӕŽɘԇÖĎУ_ǒк\x87ӣ˽\x99ԌѻːȎϕ',
                'ВʈѾҔπOϐΕāʜИǂ×Ҷǀ˚Ηђ\u03a2ӒѿˍÛЈͶӬҔ҈ƠϢ',
                'Ήɑʹѡˢчȹͷ¢ЛʓƜʔ˯ϫХζΡҦXȊЋѨѓʒϘмѣşʸ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -7803750062936382349,
                1303846328384047599,
                8133111743479132393,
                7409954640411386951,
                8780151182476370898,
                559146800534473443,
                -690008050767983173,
                -722022589902957580,
                -3474975066396825205,
                -3566923472605895426,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                779438.9546598854,
                292205.807996877,
                529587.3857052659,
                65447.382085361925,
                651935.648469165,
                939490.170998448,
                124053.24506325007,
                374538.75379211863,
                772458.8829086818,
                480399.3106332582,
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
                False,
                True,
                True,
                False,
                True,
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
                '20220523:220031.876920:+0000',
                '20220523:220031.877012:+0000',
                '20220523:220031.877100:+0000',
                '20220523:220031.877189:+0000',
                '20220523:220031.877276:+0000',
                '20220523:220031.877364:+0000',
                '20220523:220031.877451:+0000',
                '20220523:220031.877537:+0000',
                '20220523:220031.877625:+0000',
                '20220523:220031.877712:+0000',
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
            'name': 'Ϸ΅ԨÕ҇˒ѩƈȗŗҳȤʈɽцĀƹӢ',
            'value': {
                '^': 'string_list',
                '$': [
                    'ю˃ʠπ"Ƀ˙+Ӄ˵ўĺ\x90˶ɑĦΜыҜзũȯɊϼďʞΟ«Ӆ\u0380',
                    'Ħќŏ\x8bȾW\x9fƐ>пőρϐϬаŰШɰїǦåΉϊҶԤʗζÝ(Ԉ',
                    'Εź\x80ʞԎǡѬΫÔϡÙȃ˄ύŰðŎөԘʦɲӰνЮŮùҏҏİј',
                    'ȂaξķӥʍŤŊśӀʏçɢØʣȹϴτØǑtáӞҩāΘȇƕƂʭ',
                    'ԤӬѿϝ*ɷЈҮɃʪňːъƛɌʹǸͽӷ˷öǭɊΗ˯ϗƈªѾӘ',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ҩ',

            'value': {
                '^': 'int',
                '$': -6576341368747414504,
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
            'catalog': 'ŘWԭӉYӅЇªĿĎԔөΉҖĜ\x7fŔʹǲƍд°ŝӬȑѭíԃΒɵ',
            'message': '˵ЂɉĜņ΅Ţİԅȧȴ˅DӁȬλϱĔʱɭϻÓΜđ\xa0ŧҘñǚʑ',
            'arguments': [
                {
                    'name': 'ĢÐŻƋԃƉЮ\x82ɕ˴Ơǯ\x90ǁŻĨôҶˮŵ˔ǠҒԜ',
                    'value': {
                            '^': 'datetime',
                            '$': '20220523:220031.861135:+0000',
                        },
                },
                {
                    'name': 'ǧ˦ȞĩҽɩđøһYjÆԡбϧϽƵë\x9eɝǣ£ǠȹÌ¾.ǅTț',
                    'value': {
                            '^': 'int',
                            '$': 4921236286038202428,
                        },
                },
                {
                    'name': 'ҐēƛÀȫŝԆБ_ɼɚ6Ӣˁ',
                    'value': {
                            '^': 'string',
                            '$': "2ȡҔԕaѽлԥұȎɄϮ'˹ЕÁңԕӺǪ]ǉŘǦé˃˝ȭўӀ",
                        },
                },
                {
                    'name': 'ʇţɆ*ԝƇʸ˦ƾǦĞӗ-ϛӍ҆ƾÑö',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20220523:220031.862417:+0000',
                                        '20220523:220031.862503:+0000',
                                        '20220523:220031.862587:+0000',
                                        '20220523:220031.862675:+0000',
                                        '20220523:220031.862757:+0000',
                                        '20220523:220031.862839:+0000',
                                        '20220523:220031.862920:+0000',
                                        '20220523:220031.863001:+0000',
                                        '20220523:220031.863083:+0000',
                                        '20220523:220031.863164:+0000',
                                    ],
                        },
                },
                {
                    'name': '\x8eǪцԇЯ\x8e҄ÂӋΝŐƁțҖҥı˷җʐȔΠѲɭǻȚ˥҈}Ɛƶ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20220523:220031.863773:+0000',
                                        '20220523:220031.863859:+0000',
                                        '20220523:220031.863942:+0000',
                                        '20220523:220031.864024:+0000',
                                        '20220523:220031.864105:+0000',
                                    ],
                        },
                },
                {
                    'name': '\x9fðӞύEıʛʰŤ2ԃLӈ¡ȽŻТ´ĒĈғ˼ÞƼ\u0379;˨ô',
                    'value': {
                            '^': 'datetime',
                            '$': '20220523:220031.864680:+0000',
                        },
                },
                {
                    'name': 'ԆӢǰ$мѬˀҩƗφǘԭaȪɅb\u038bɧûҨӈцƘ%m\x95+ң\x8aɁ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        -41493.219502453016,
                                        803762.4781157078,
                                        958363.1502703894,
                                        -86038.36533836064,
                                        394886.64959489874,
                                        644517.7475249051,
                                        217598.13030501996,
                                        97846.43718423537,
                                        406145.934751257,
                                        179560.15844735055,
                                    ],
                        },
                },
                {
                    'name': 'ϲŋ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        '\x91ƹйãԍ\x95ȶÌëљəѤӸҗîϦΔZѢ]ĸĬǋ^ԣƐѿǈÂѷ',
                                        'Ʋ³ϩř&ɂΞȮ\x9cԅ¿ӓɢʣĉɖʖŋґȮ҂Џǹž\x91ԋѾǻØΟ',
                                        'σҬƺZkĚ˜ơŞŨƽȧƪǌÊèԦЙӽĭȳƑϑTԬЯê:ґƂ',
                                        'ØȁψŜÑŠѢӰΪrѸӲϒà¹ŝԘʥ҃˃\xadĥĚɵ˶ ǜҊжО',
                                        'Ŀm¦ȱѲ¶РАß@˔²ΐӢ˷ʤʾĲӫȻŅÈĞƥƧȶүͲ"\u038b',
                                        '\x93сɏĵԧƈɣɼʶδɪǩƜ6ȌғğːͰç)ƠAіͽ\x9aҦɢȡɴ',
                                        'ΗԆ£ĴҳʅŒǁçά0ΦƱҩŲƙƺtŊѥėњʎǵƕǏKʩŅz',
                                        'ĆӅԐưȏǝəĸҺĵʒˎҴȢȏ³ŻѡȶЃǕƔȼˉн Ҷ˻˩͵',
                                        '҅Nͺлΰ\x83ˁҙÅŘчϠą\x80¯ӓьŁ\x80Ŗ¿ʂӧФҌ҅ÕƷǳѣ',
                                        'ǗȲѱƵтџƚņƳȅщԮЏȖF\x9eɕ\x98ĠԅӅǠ»ӽ\u03a2ъͺɄԑɦ',
                                    ],
                        },
                },
                {
                    'name': 'ǿǚʃÐ˃6ёӥҷ',
                    'value': {
                            '^': 'string',
                            '$': "WȈȀ'ƌӚҡΓФXƶ±tɓƢXԫ}ӳƲȶ˂ӶƢ˺ϖȦҕΖɝ",
                        },
                },
                {
                    'name': 'м˵Ј҂Ԓ)ƁĢԚsʮǅʗǮǇ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        377659.477863522,
                                        831298.8471409141,
                                        224356.9627369952,
                                        743918.9907418177,
                                        120874.5387881507,
                                        674165.4226320789,
                                        73395.04541870221,
                                        4795.204887675936,
                                        -12386.741047050513,
                                        583642.9340171478,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Ǖ˖',

            'message': 'ϣ',

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
            'identifier': '¦ϯНl¦ǑŽҢÈ\u03a2ÚÈÓζɎʀ˂»ΰtѾάˬ\x84ÔҦȩ˯ɠƜ',
            'categories': [
                'configuration',
                'internal',
                'invalid-user-action',
                'network',
                'os',
                'internal',
                'invalid-user-action',
                'file',
                'file',
                'os',
            ],
            'source': 'äËȓˉ}˥ƕʴǞԮͻįЯӔ˝ľ5ʯԄ\x87ȅнæɚ@ˠƦĎɌ˚',
            'messages': [
                {
                    'catalog': '\u0382ӈ˛ģ\x86f¸ʎWƉɭRƮЗ҆ӒүɦθȳĹ\x8bɱϒˣƁȨ\x95*\u0380',
                    'message': '˺ÆΔ%ĲɄ҉ЖȡϨȆĭ˼Ɋ«ѓȈΥϴҜɗVЉŒȯЏӺō[ҫ',
                    'arguments': [
                            {
                                        'name': 'ěԋɿ¹ÁǐŘΈϤb\x92Fưӡ˵ȺЭȾè',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ɯΐ©өʱΚÀѢ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2305183969644090992,
                                                                            4217143249103799780,
                                                                            -5059264408998703966,
                                                                            1190881658453911229,
                                                                            4342276721282035540,
                                                                            9069920244582291270,
                                                                            8786402319228556550,
                                                                            -3858920494239150468,
                                                                            3909544201309259124,
                                                                            7702212906481552704,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŝљ˪\u0382ϘòĘʓɏBÊʾӲɮņ\x87ΤԞīǑ˗\x92Ш',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǻ˼ԔΜƵуӔXϵŝAʴǡȾʰFĄё˾ǉƜǳǛӦÇŜҸԁg\xad',
                                                                            'εÚӆϔÁшԍͲ,nҗŤԣдїȏÜϵ²ЏЪŻÍ҈\x8bΏóȈԌs',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˔ğ^Ǣæ˰Θη\x85ÌфȒÏ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ЄψƲȔкÊʡЖϡŝƒȼʤĿųƨǁƖe˸ӥɫ*΄˗Ϲ¾ӜƼѽ',
                                                                            'ǭɶʇϛ=ѩчԕÎëѮԟ®ϚләϽҧɋΧˑBҒğǥӴʪȹɻ˷',
                                                                            'ɭͰӊŚǹϘɓ-Ǧ$ƈԘģǌҦΗϮʗʱϙϼЁéʓѠӼıϢvʢ',
                                                                            'бǉƂ;ΗĈȧȓѴǈȠϴmįȼƹН҃Ǘĕɷ\u0382\x99ʪɄ}i˺ӅЕ',
                                                                            'УĦžВт\x88Гњԝ˶ʇЉԥӐɪȮԫŹʠʜÛ϶ѧšα\x95ɧԋǙƮ',
                                                                            'ȫά}ҶèӎҊʑÞЪƈ\x97ƫ\u0382´ФԣǵҴСԟŨ\xad6҂LƑ\u038dѓb',
                                                                            'æǚ˘ȈǅПɄȸʩиºˀΧϏȻǽϡЕӜʾЯĤģA˺ȩě҄Ǉȅ',
                                                                            'ʵӗʠGǮϙʇԄNğҌγ˪ҀɅЮǴǍѩɾϟaHϗѸӖΏӔӨȾ',
                                                                            'ќɕȇŚ҂\x82Ţ\u0380ɤɮȒщ6ǦċѩАǞǥ¥łɂɃșM϶Ԭ\x8dЬΐ',
                                                                            'ȴϮóɍˑʉĴҳԚ˺Ҳ3ΑϕѭǥәˊҌǡԤΎѲɸʚ\x8fÏЈȎɕ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȶǈ¾˳ˋǚНɤПơȇòԟ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ǐĨԥϻЗϷ±ėӼ ¯ȋ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.783718:+0000',
                                                                            '20220523:220031.783803:+0000',
                                                                            '20220523:220031.783884:+0000',
                                                                            '20220523:220031.783965:+0000',
                                                                            '20220523:220031.784045:+0000',
                                                                            '20220523:220031.784124:+0000',
                                                                            '20220523:220031.784204:+0000',
                                                                            '20220523:220031.784283:+0000',
                                                                            '20220523:220031.784363:+0000',
                                                                            '20220523:220031.784442:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŭӍӷƛĲϣϞκRиʶІǲѪ-êΤї:ϵ[˃ƏҺ%Ӧ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ϥĮѻɟƨɸú',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ĝΦѨԄǁõΩ´ԤґêƏŝҼcѿƞʶε˹ĘōӬͲɔeɟДԊԅ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɍԜ\x99\xa0ӜΩϽƫҝћԊΣǝȴш\x87ǐ\x94ͽԭ¢ɐɎʒɘӅԕқ˯щ',
                                                    },
                                    },
                            {
                                        'name': 'ӬЕʌу',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҋA\x98>ěӀï/āǁĳÂƄӷҫλșƗԪēïӀÝ\x8fӮϨɑŎÛԭ',
                                                                            'ѲơѦӝǒҾÚʈʅ÷Ҋɸl˰üѴԀĿ²ĩӑˢϗšПǪsʾЖĘ',
                                                                            'НӼɻϡӘКňȬԇΤ\u0378Ⱦҏì\x92ӧϓ\x90ԦĖU¬ʄӅ˅Ԅ¶ŖΑǦ',
                                                                            'ÿԛɇ˻ş³³ЀȶŁϕʑӇ\x99Ċŭƾˎ¼ԊаԎӟǂ¬ĻǠ˨Ѷ&',
                                                                            '˝ÊĎŋĳɏ³ŤdŞЍӆϢЂӞ6˱ϭӱUϋ˙ѤΈβԄοԗΕѢ',
                                                                            'Ѭſwƃɫ\x99ЛϵǏХϱƒƞƊӅҳǺ˄ϴοÎ҇¬ɚ\u0380ȼWΜЭΫ',
                                                                            'Ϝź±ѨÆǎθιʘҜϖÅ-σȳυΉ\u0382śŸɳЍġСҭʌćɱЯȹ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ńѕϔ\x94ª¦üЎɜʎØ~Łɬˣɮԝʀ\x92˙ǵſΊȚ\x82ǇÖǓϋȨ',
                    'message': 'ЩЦɭqӦπԌ˼ӌЊȂ˶ɳΩ><Ӧʷ\x80Ђ!òÛÆЍŠĲȇ\u0378ǭ',
                    'arguments': [
                            {
                                        'name': '\x7flƋŘԥˤȻbʪüϨ+˲Ђ1ɧʏңǘî¦ŸϪʬ\x87ĩѣývж',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ĐîοęљЊӇ7ŋ͵ĖÝϊ£ӌğέɝԁ|ΎǄưǽӨƓ\u0380щйƫ',
                                                                            'ԀÖΛ@üƌȉį°ƣĊҚʩӠӌʟԣÓЯιчХӷtäԋ\x93ʝʖ³',
                                                                            'Çҡ˽ɑҥʖͲȎͲ/ԠȅŻҥƛƻʶξΙÄƦǀɎΗϻЍƂ2˟ʴ',
                                                                            'ҽԖʳ|ȏĳӟìѷǱӠ҆ĮlùӗǹҚþϺ˸ɨėŋӇяť˄Ȥʝ',
                                                                            'ӖӢˈŀΉΒԃθϪķӝғņǢѓэ˅ƫϸɞǩ˯ΪѧԔҤфǈz˵',
                                                                            'ԑӂ ɛԣҖʺĵʵ"ȜԞuËpɷNԅǵԅɊҳ_ԦɰʄǤҁʸø',
                                                                            'ӡɍҷͻĚзѐԂј5ŏʏҵŹЈéˈǙǬˤҺњĄ˄ëbʟīѳʱ',
                                                                            'њƼɶΜțƧϷÛǣԜvӲȍƘǦΤƅƄҸάӐќęӾ8ЁÅ\x95íŘ',
                                                                            'ӄҾaƤѷ΅ӷΚӲͰЀeƇҶTñˡӱұȆƧй\x9cŋıνùg"Θ',
                                                                            'ӱˊʚіЉԨÒĂϊɒmЦaɑƢ]\x81ƄǉҬˀ˭}ϔŜČʥŁʩɋ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ɋ˃ǨëҐƯѾ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ԦƭπKƛ:Ғ҄ʨ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': '\x9aΣӥÈP΅ˏԋΰGOϸӂέӱҪƪӢҙ«KĻįѩäxΞԝҞΐ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5381901551845496457,
                                                                            -4238953449695958622,
                                                                            -4287605601470341695,
                                                                            8689986659018075795,
                                                                            -4739756594225183597,
                                                                            6605388031249885068,
                                                                            -618509474819887240,
                                                                            -7391247041363668773,
                                                                            9196400541190875132,
                                                                            -206363031898370476,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɏ˄ŭǡӭÚˢ˵҅ϛъңӑϓĤèǂӊ˓ӰȖȝǎáЏƸƫāȣƋ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6309443301477013274,
                                                                            8893447910382664691,
                                                                            -4960192395784017789,
                                                                            8316578094783818660,
                                                                            4069950727287733571,
                                                                            -718292537788137969,
                                                                            102181821423386201,
                                                                            6626143191373342993,
                                                                            2967336544059443750,
                                                                            -2831017658804798639,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÊӻɀӧȑЃØɕ˘҅ȦўƦȇ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.793371:+0000',
                                                    },
                                    },
                            {
                                        'name': 'οãĩ$¦ȃӳZǽž',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ԭ*hlӚˡЂілʈȘқξÄưвȹĒѾӽªОǂʡʋʙϟʸÐʟ',
                                                                            '\x93ˬƫÞíBă\x8aσŖ˟\u0378ƚΈ\x82Ƌ|їď˂ĻӜÂW¾jȫ\x9dLО',
                                                                            'ƫϦʝčǔɲͳŦцɨҤ/Ҁϟъ˱ſ¿\x82ĤǑʌͰĆÔәlȺƪә',
                                                                            'ЮCɢњ?Ўԣ͵ŔȻБƜŪʏȭ/sůϽƄԗДɨų¥Ǽɴ¬Ϛ\x83',
                                                                            'јǣВ˦ӃϬǝ¡ҧνȒĸƞŮ\x81ˊőԡʑŁƉӧĥ˲΅әԑÙŶх',
                                                                            'ΈϡπԆàШYȷϳӚ2OӳӕʈFˑИǹŉȁʱʲ҃ÂΑ˰зũ˅',
                                                                            '˺ҰӀ˭ʻŏ@ŇcôɛԝÏɊ˞ƨΰˣƑ\x95QŗѷŶųϘƶ$ŜЋ',
                                                                            'ȨԋǋʹАƣŻî|ġʦѿ£ԦζZ;ΌΠHԑȀΰŮ\x80ЙĎʎƢӉ',
                                                                            'ԐѵÓԍ˄\x86y.Ӌğɘǒˤ\x84υλǂǭ¬ɝȄҌÅо?ϿɬϨ6˝',
                                                                            '·ȒӆȈǰΏŤŐҊԃhʔĄgѺJȅʪ˟˄ɧȷғĠƟΔұ\u0379ƒc',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʍϝʩǍΕɁFԓĽĴĝˠɷ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            170555.84534834023,
                                                                            890107.3680075709,
                                                                            501276.2922937531,
                                                                            220331.70746283862,
                                                                            912372.6507517375,
                                                                            113458.40801633216,
                                                                            660906.2256397303,
                                                                            638545.5855595379,
                                                                            111020.2322352094,
                                                                            967215.7710743211,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'γϏ˝˭βȆΡŌbϘßõňԗƠĦȠɴʢ˩ҏʁEǐʹˠʈřŎӟ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϰЁȾ҄ͱџż˟ʻǪ}ɊɉȌ\x81ƞƪ\x87ɏ·ĂʞaɼǺӆĝJϛľ',
                                                    },
                                    },
                            {
                                        'name': 'ϖȠύșкSí\xa0ŊƐƴʖʗ~ԅπӬ˃ʹŵʅ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ßäвɀϊ˓ɆȻńɸĸĉԊҦϫӅŻė˜ƒЕӹНɬȄ|ŴĶƦȔ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȷӶԐƒpȠѶRμӿĩЎ˟ɌĄʮŋʮ"ȇҢĖĊeˋƂǓŇͷɬ',
                    'message': 'ɖcʦ|ťИӰƤʬʭŭ%ЂĉȮӐľiϘžϥβǎ¥ƹԖϭ˱ɗũ',
                    'arguments': [
                            {
                                        'name': '1˪',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԪԁѣȼǓӋΣҐĎ˘ʃ˾\x94ʠĆүҼǘǶɗÍ˟ε˅ŲЦãŠӻ\x7f',
                                                    },
                                    },
                            {
                                        'name': 'mBÛӚʟǁϣԘӗιƇыƏƻȮİЋ˙fϬɴʌĢǮϪҭ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2886267037666052978,
                                                    },
                                    },
                            {
                                        'name': 'ɩɽÙϾ\u0381ºԇіuԟϏNDμ3ŏǰǘде˧ż/WñѻҌŽ¥Ѡ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.798616:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ъÊԡ+ԋтӢҧǘȏN˔ʲǣüѤĚѴӡÉΧƚӧāʋǻƏɾƛҡ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.799037:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Η\u0378ã$6ƸǞ˰ϋˀƎπκłlĂʀͶĊ\u0378ǅҠƤːɒ\x8eŞŦЧL',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 570509.0989738472,
                                                    },
                                    },
                            {
                                        'name': 'ΐжαsљg',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȞŹ˪ѐʬţðȾƼǺ˺Ӯ-µýÈξƮǮɡʔj,šÉϛŶҕɴχ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1700640290015426666,
                                                    },
                                    },
                            {
                                        'name': 'ˏ\x99гʩƯйˢŅȐɎѨ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '΅ѸˈƀħÒʙǻvɱд<ӕϫϏōbҵÎϟɂůŷƦʏ˻әŪӾЌ',
                                                                            'ɺǑȔɏıӫɆӓË¿ƳӦ\x86Ωr\x90B\x96иȳʈϴХKƙ`řʚҌΙ',
                                                                            '˔ŷ¦ОϬҫ\xadĆìYȕΕÉӆȋņԭгɒì!ѲʠлР˖ϿЩƓʹ',
                                                                            'ӻ˓ćЂǡοɑ¸΄ƺвӨ\x83ƤӝɍɰѮƭľӹƍ+øɏӣʓ8Πө',
                                                                            'ӜÞϯœҮǅӳŭ\\\x8c`҅Фȯ£ʇӓ˅ϐǙƋЦǇȇɪʛS˕Ĺҁ',
                                                                            'ǈҎǐǨpςɭӆһȊїГʀҖΚӡɌ҆ΗђǞȏԌΑȞŞɍr,Ҕ',
                                                                            'ЙÓɵϱЧɐɧĕǱ\x8cĎԟҝʈƏдƉӈƫ҈ǡˉθƛ\x85ҳȓːбƶ',
                                                                            'ņͽį:˄˰sґӴ3ǛʃҗцAԄƈҢǝҾǃȍ˘ÌtҀ\u038bϕDΌ',
                                                                            'đͿВĠŻΌωȃčїŇŨáӅо3ɒȩʘ˺ƚƟɉԗͻÀȟȌӲ,',
                                                                            'ź\u0382ǙɎĒÃ¯ţ˷͵ȉĂʚɀşǆăŤȠӍȼ\x90ћԡϯϥİȏƽ<',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѺˑʼӧȔѱʍŵgȸ˽ſŒȝź˒',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '%ҷ*оӉҝ.ЮԪuіźЪ\xadƅĴѧɐÓßEҪƝԮɂÈѻǨ\x94ɲ',
                                                                            'Чκ,\x86мϚťςʣԘĴыΫȐßœ,ˡԜ\u03a2ǡŠѿѣΎŻ\x93τǁÝ',
                                                                            'ɋňϴôҘʑŭɑӤǱиɖ˷\x99ԛȱxΫƲÞʈÄĩȔʳ¸ãřţȘ',
                                                                            'Ĝ˄Y˛\x96ϴˠʟ\u0380ʑĶȦǾˤɤЀİЦǬ{ˁѾɼİȶίʒųɓΆ',
                                                                            'ƈ0ԏÞϡŉЭҡǙϪңǚϠ¥ͶřʇȕƖӊһ¹1ѽǺCŭ\x7fǭȵ',
                                                                            'αïʫϷɝŎѹϑĻñЬƯƿӰӱђƮÓưӎćѣþ\x9eïʧҭÇŏǧ',
                                                                            ',\x9f,ѽƲЀǟ\x89ĶаÆӊƪǝ҉ɾɡòЬþԮZʚ˱Ѱ˘ÍdΌƘ',
                                                                            'ŌӐÅҺЋʽçΰȽѿΞђȇԜ£˟Ê\x82˻Ƞ\x83ķêǙɜȺ΅Å˛Χ',
                                                                            'čӿʲɇӒҿƂvÀѵŶԃȣĶ;ϼÄ\xa0θŠɘ\x9cȵaʁ˝čʤǦͱ',
                                                                            'ƣʐІӦӢƅ҇¯ǝϺͰ1ÅǙӑMϘΑőүөѫСˡѴԝЍ?ÒԢ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϞƣӴɝѹĶëƉЋϜƢѿҐ\u0378ϘЕӹƎмИÎƘƗе\x89',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˏǖɅȅɶŪΏŗέώԀ\u0382ɥӫʜªÇHͱљЈ\x9eЩƷʱӬ˄)Ĉη',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "ӰʐϾӫlќ\x83Ѻə²×єԕSʺ'ĴӕҪ\x81ǣqšȃĖҐʤǭӅL",
                    'message': 'ѿ˽Ӝϳ҃ϖǕŷ˓Ҡԑm=ʈѴuҒҸˠȧ˽ΏƯȞ\x8eɁĖҐ?ǆ',
                    'arguments': [
                            {
                                        'name': 'ҴȾ¸ήţλҔRǢěǲнɻrðѓƛˣά\u03a2ӣȥŘƳ¡¸',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.805124:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɌƊāřͽӛ˪ĎºҐҰ2+ȟ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4681746693685267435,
                                                    },
                                    },
                            {
                                        'name': '\x8eǾ3ӴˁĜЭϛ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.805942:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǕѣӇЙӽѬӴƾҙǸђȨҡѣΌαƬ϶ҠЂĝʠǹԦ˕ũǫ\xadЎɏ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            397767.3830540449,
                                                                            958998.869227861,
                                                                            703551.0280553005,
                                                                            710753.0722133206,
                                                                            442215.5802628045,
                                                                            744134.403306075,
                                                                            29804.713801844628,
                                                                            721940.2391486621,
                                                                            800306.5151411905,
                                                                            904212.4393879541,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ÏÓГÏ%GȟͰҠԐҝƐӚÇ\u0380шӋτŲʌ҅ʂŬĊĿ΄ӸʵǮɪ',
                    'message': 'ϔʘԐƣԦҹϡÏóVǞÔԗʻ=ϰˋЈѠӄԊȻyʽԄџԢĝ?\x89',
                    'arguments': [
                            {
                                        'name': 'Ϭ\x81ˠПԌƉǛҎßҩȺʇąӾĤƸ*ҩ«˺ϏƇòҏѻč˪ԂЃˁ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            643203.2771265651,
                                                                            813076.4149492915,
                                                                            55170.54178634062,
                                                                            387708.82272838114,
                                                                            988737.3622482542,
                                                                            355777.2706841963,
                                                                            949634.5827968044,
                                                                            429044.3874463312,
                                                                            162921.34740126482,
                                                                            271615.05041015975,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˽eύ˗$ƉѡĺðƟМΙľÛʻŢԋńǘƁ҅ɤ\u0379ӿˑƣʟыҕˬ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4974336331387756694,
                                                                            -1574805944600912224,
                                                                            1350792592111188124,
                                                                            -5144547909220431941,
                                                                            -425699829204366663,
                                                                            -1204432510646213865,
                                                                            -8262629242314135329,
                                                                            -8216851354909327832,
                                                                            4043279678278154292,
                                                                            6913257770627564473,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĚɇʲʅºͶАǉГфϻ˙ȽÑțʛθҡқƏʪхͲŀ²ϬźԂįȄ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 65304.903053020156,
                                                    },
                                    },
                            {
                                        'name': 'Я˗ʹaÇĐŅɑȱ|ɿӯŤəчȴдϠ\x99',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            473781925503909017,
                                                                            -2526684599209736980,
                                                                            -6258971034476354697,
                                                                            -8930710245433672413,
                                                                            -4103002460595381330,
                                                                            6241050160889981589,
                                                                            5384748463389127823,
                                                                            -6830429179716335815,
                                                                            -1213920662759656362,
                                                                            7866459606837852136,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҽŁȑŘƨēіѹ\x95Ӄғ¡ɗŠͺʑʮȊүѩ˘',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.812076:+0000',
                                                                            '20220523:220031.812160:+0000',
                                                                            '20220523:220031.812241:+0000',
                                                                            '20220523:220031.812322:+0000',
                                                                            '20220523:220031.812402:+0000',
                                                                            '20220523:220031.812482:+0000',
                                                                            '20220523:220031.812561:+0000',
                                                                            '20220523:220031.812641:+0000',
                                                                            '20220523:220031.812725:+0000',
                                                                            '20220523:220031.812804:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ńұţӼŒǠ\x97ыӯáΑĉ\u0378ӑřξîƱ°ҚʆȆͶӊƺ\x81Ѯåƭ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 308063.37653742585,
                                                    },
                                    },
                            {
                                        'name': 'Γ\x87ҭС˓ԙȣ\x8b˂ɬδӝӸˬţƻȑǮ\x9dԨ\x82ɢͶΙϔΌɞɃǚU',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 821828.2361914739,
                                                    },
                                    },
                            {
                                        'name': 'ҬαЂeҺɰНȯКʤϰŷӛΎƕ˖ШΝϣ\x9e¡ϼұԔƮÂϣβφΎ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            373083.9021961935,
                                                                            46900.21386004452,
                                                                            840709.1415636506,
                                                                            995314.4791223393,
                                                                            788826.9955313612,
                                                                            760333.1183254601,
                                                                            197476.49546791712,
                                                                            25631.37390479473,
                                                                            259429.24319968722,
                                                                            384259.7536536477,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǝόì²Ǌɤρ³ŢͲμЇϪшϫˉÌɃĪƭΰȕҠϠҕІȍǬ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            61350.76911295485,
                                                                            699426.7409445803,
                                                                            40468.319600461546,
                                                                            748839.3545060239,
                                                                            919195.4859523483,
                                                                            990735.7035042287,
                                                                            850134.4149042261,
                                                                            717966.3175499969,
                                                                            419875.0037685145,
                                                                            250660.78900467325,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǁӭʦә6ƫЌ\xadάΒѫǊȡˉʩΛԁyćɞҨưоӎ\x88КZȒӶ\x87',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.816639:+0000',
                                                                            '20220523:220031.816722:+0000',
                                                                            '20220523:220031.816803:+0000',
                                                                            '20220523:220031.816883:+0000',
                                                                            '20220523:220031.816962:+0000',
                                                                            '20220523:220031.817042:+0000',
                                                                            '20220523:220031.817121:+0000',
                                                                            '20220523:220031.817200:+0000',
                                                                            '20220523:220031.817279:+0000',
                                                                            '20220523:220031.817359:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԙ_ɈǒьÔžʥϧȬɦɆ¬\x85ιϚ9½Ӆϒ\x8bϩ÷ʪʮxʼ<Ïb',
                    'message': 'ɫÜåɦǡΆþƊśŇӴƖӳ˙ƫԍћÍǃЍŨ҇ϣbнġǼǢŅʧ',
                    'arguments': [
                            {
                                        'name': '˴έƫê\x94jҜ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.818508:+0000',
                                                                            '20220523:220031.818592:+0000',
                                                                            '20220523:220031.818673:+0000',
                                                                            '20220523:220031.818753:+0000',
                                                                            '20220523:220031.818833:+0000',
                                                                            '20220523:220031.818912:+0000',
                                                                            '20220523:220031.818991:+0000',
                                                                            '20220523:220031.819070:+0000',
                                                                            '20220523:220031.819149:+0000',
                                                                            '20220523:220031.819229:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԃˈ҆ҸīLӁŁɿљΑү',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2939070784849702825,
                                                    },
                                    },
                            {
                                        'name': 'ƜȎȆȒφ1ҖЀá\x92ƨŵƩÕ¸ǒʝ_˙ӓԟ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.820226:+0000',
                                                    },
                                    },
                            {
                                        'name': 'лӿҩlˤɹʰɅԏȒʉʹNɧ˷',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1909250843170699089,
                                                                            7131752002723803506,
                                                                            -3138009933875708654,
                                                                            7185696996755822416,
                                                                            592370291085657974,
                                                                            2337084828082385700,
                                                                            -2552111538513463772,
                                                                            -1631866041772328360,
                                                                            2414264924665798827,
                                                                            -990312232560393299,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĄЭǳҽȬԠǽǏрΓ\x89',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.821833:+0000',
                                                    },
                                    },
                            {
                                        'name': '˹^ƀƳкȳʝġ˛Țҕ\x85ӏũƫqȕ!ʦӅƚ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            507565.55589643493,
                                                                            416924.4664643316,
                                                                            869357.5377228298,
                                                                            154757.73345193002,
                                                                            457210.2704638663,
                                                                            170137.87931229686,
                                                                            -52451.66759106638,
                                                                            -25639.557512402767,
                                                                            205003.97418410116,
                                                                            373702.4562199162,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '´ƏɈѿ¹·ϥŝȴ˦әΰʯƳ`ȿӪÏЮϚãέѠӹ˚XԄȊϹĪ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            681807.6134233963,
                                                                            843507.5743177071,
                                                                            118718.5760345406,
                                                                            242668.16584069654,
                                                                            427085.9749183258,
                                                                            650526.3795143,
                                                                            476783.75284878816,
                                                                            473218.6238858104,
                                                                            619115.9685183382,
                                                                            699162.4105565345,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӎҋ!Ηӂ¦Ч-ƺʺȥͻʟŏГƛ+`yϏэΒ˭źĹǈӋŹF˻',
                    'message': 'ӀĞϿԣέæБRįƟ\x8fğˁ\x8cϺʕ˅Μɜϕ\x8bƙƸƂѢԑѧǧYʚ',
                    'arguments': [
                            {
                                        'name': 'ŋτΜEͼ˶ǋѿϜΑɱƌĖ¥·ǆȢӬљ\x90å˯҈ѠӜϥҵΐ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΆȲǱ˫іˮԕɐͷϧϩΈҽGK+ԢȁѼӒ҈ҠƶX`ʖǿы˷Ƨ',
                                                    },
                                    },
                            {
                                        'name': '4ɺ,ύéί^ʭĪΣκ\x7fŃƢȧĈ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ΖŅɉ ˩ňľǖ\x94',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1431122490393940393,
                                                    },
                                    },
                            {
                                        'name': 'ɪғ-¹Àʰ1ΒÙҘӫԨѱ¯қƥԦɣĶƕёϣȵ1\x81HΊƛƄŜ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԖŨγǚ}ɛb¿CƀԏʝƄơҦƤ҆˷ ĊϑԝɊΦҒȗąӼѲř',
                                                                            '¤ͻł\x9crϣӥʈВʬȥ˫ʋÖʈĠ=ǪƌƒθȄƦλʮyǏǘ,Ϛ',
                                                                            '¦ћͼ˓ӨѹԍѳǷƺřɚȵчüӲȜˠӪǨΜȷԚч˖ҌV-ȅч',
                                                                            'ªĐӒȽԆƾƻˁąö˙Wѵ˫ξҟϕТɡĴCԂɊʌЬӷƸƩ0I',
                                                                            'ҡĨҦǟȖӌ\x8aěȧȳÞӒ˞ͼȜԨϴʮ>\u0381ЍΫ£Ƚ˂ԙθѝɻқ',
                                                                            '\x80γϩȍјş˓˗ӘǡҿƤЙĸϦŲȣҀӐȻĹɝԇɌ@ʟĶŋɬϕ',
                                                                            'ϻāįѩΟ\u03a2ɔЬϒӑǝӽŴƂÞωěĶȈ.\xadͿӀѿϡ?Ȏϻʾʁ',
                                                                            'ǪʆƲ˟ñӨ\x96ΞɟŮғϠ{ƒɁýʇɂ҆¦ԞĭϖȔ\x83Љ£ӤЀ˺',
                                                                            'ȿˤρʂΨɀ˱ɣ&Ɖ\x83ғ\x90ҷƘ@3Ðҿ˩ŜӣˬĎα˗ԩǷÛә',
                                                                            '\u038bѠȒUSʡԡԥǼ˜lƞ\x92Ӂ©Ɉ#ƍƄˮıʻӾμӸѽīэ^Ԕ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƀſя¡ʯ\x82ЩǙǑÀ^ʲʸŷ·˅ΣçŰëǣƞȕϸɠ¡\x90&ĥӍ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.827824:+0000',
                                                                            '20220523:220031.827909:+0000',
                                                                            '20220523:220031.827990:+0000',
                                                                            '20220523:220031.828071:+0000',
                                                                            '20220523:220031.828150:+0000',
                                                                            '20220523:220031.828230:+0000',
                                                                            '20220523:220031.828310:+0000',
                                                                            '20220523:220031.828389:+0000',
                                                                            '20220523:220031.828468:+0000',
                                                                            '20220523:220031.828548:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǡ¯ɯ˻\x86ǥӥԜƹƅѪƪƚȶȃŨDʅΔмĬѝˋκȼΒԖ·ɇƏ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'эΦ®ˈ4r˯Ǌɐҟ¾ɊϱэɖS4ÀɽѫÝȰɉģëuҒ˱Ł\xa0',
                                                    },
                                    },
                            {
                                        'name': '¾ɔǍ˞ßϫ˙ТȠɝɗ҈ʠ˺ӴȏԢЋњ<ŋÜѷƍÃӊĤӺѮ\x9e',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2681480158152347803,
                                                                            -9216075272321251453,
                                                                            8170383821754894570,
                                                                            -7983318799503510040,
                                                                            -3307863217575470264,
                                                                            7014311003536511438,
                                                                            -1960538645528997227,
                                                                            -363444715815194759,
                                                                            2181027622681735524,
                                                                            -6288055989372574716,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŶѕMѵˏnϴ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƻpVə˕ТɆ˙͵ƺĨɖǋúcŕɯĞƏ҉ƳԆƑđːȓǶȔӗȔ',
                                                    },
                                    },
                            {
                                        'name': 'Ďòϳӣɑ@ǫИҶԚĤɦɰƉͰ\x86ɨțѓʘɌʌ˒ϩ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.831230:+0000',
                                                                            '20220523:220031.831314:+0000',
                                                                            '20220523:220031.831395:+0000',
                                                                            '20220523:220031.831476:+0000',
                                                                            '20220523:220031.831557:+0000',
                                                                            '20220523:220031.831636:+0000',
                                                                            '20220523:220031.831716:+0000',
                                                                            '20220523:220031.831795:+0000',
                                                                            '20220523:220031.831875:+0000',
                                                                            '20220523:220031.831954:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˗a҆ˢȟăŴҜӜҌůԐ\x93Ӭйʀ®ģ\x94ʒ\u03a2\x84уɝcűнɢзǍ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 198811.588061617,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԎŪмɂāʕƙёŅӦӃͱκƝ˼ɻИԎɬTöϒΎQȮВҲ˨Ėф',
                    'message': 'ĭϯ\x92ɯʒß˪ӖƅΑʒСƜƕ3ÿƜћѧƠμņʦɚƄΖΗӛ˂ǀ',
                    'arguments': [
                            {
                                        'name': '¥P϶ʥ˦ȩ¯BаlǡҬљǵ\x8cı¬ҘhԀšrɷȦ<ЌȆóňČ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϽƈÛҟȔ§ƸǮšǍcɝӰɈҝԛ҃ƁƝяĔJѲǉâӺãǲɶL',
                                                                            '@ˋŹЯԫ³ȝѬҮɼ˫ҖϢǍ\x9eцɢɱϘӕӰҡ±ҩέÒϥ˯ȁϔ',
                                                                            'Ÿ\x9bԞкBĩԉР7ňÙхǕѨ¾Ț>XƸĳƷДʿҗЈȓӴȥΚ¯',
                                                                            'Ӫюҭ\u0378ԏИќ(ͽԜԨԠ_¶ǑәΫӕIɋТ\x7fézʓˑĝф˖ʍ',
                                                                            "ʒĖƃџʖĶҖφԣĚІ¦ϡƔϨʜд҈Ӵ'Ǟʀçɞ˄ХDēxĺ",
                                                                            'ˠϸҁfƳŪ0\x84ɛӐԦTȗћӊӬ¥˅ĊėӘɗӣԒâԨθĺЫȻ',
                                                                            'ēsӤūƚәɗʝȒɷФΟвĮԩƏƝ\x86ϣöҋϧӠûȊäԢ\u03a2ҋҽ',
                                                                            '»6пӢCȻѓǐ\u038b͵Ϙ¡ɑԢȘǀǿBк¡ǯʏĒΪӘғС˴ʼɃ',
                                                                            'ɄΰůƇȕƔŪ\xa0ͰҁÜҏ[ϳ#˝ȇΥʐμèƅҳҧЗфŨ\x8eɃǹ',
                                                                            'ţďÁɔԓbˀдзõѸ#čİłǥʠϣûƤ«ʫ˽˓Ҹ¸ӆҺʇĠ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'р\x85tӼԝ°',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ţčàÊûȮԃǙŔĤʾΙOЈxϛɞʞɋ˓θӂäʵǆ´ĜԢίЬ',
                                                    },
                                    },
                            {
                                        'name': "ĒќԃŇɯÈӑӊ'ή\x80ʅƘӋαʪơ\x94ɎɠŐǻbУ¬\x9fԡ˙",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6143006066104344580,
                                                                            -1118673176586643178,
                                                                            3904464739318695912,
                                                                            5496137516301624840,
                                                                            -8544194005284554214,
                                                                            8308594977876866799,
                                                                            -8390576395313651856,
                                                                            1557082593990008951,
                                                                            1459163038109303949,
                                                                            -2670642130963892947,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɑ2ʰʈġОԏ\x96ƁҀґƮÏǬԡ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1082087268923873668,
                                                                            -957528922648294023,
                                                                            7652473315986785220,
                                                                            -3046614287390217660,
                                                                            -2885281851917612637,
                                                                            -6323786957338787344,
                                                                            -2608699309487023829,
                                                                            -2358733290849710048,
                                                                            8671607098340102878,
                                                                            -3117926037378564630,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '&˳ѡʺʓƹɶɌɗѸìέԤЪāԜѽęӘŃб',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϡќҰȧԟԕǛĒe˱ˠ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 657996.2959245145,
                                                    },
                                    },
                            {
                                        'name': 'ʝ*ʼϮƖ=ʻ\x9dƒ\x91Ш\u0378ӣɁʡѠѐíЉÂɟʅə˴',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 885894.6394610521,
                                                    },
                                    },
                            {
                                        'name': 'ƛΩѻĈͳˤĐҽ¼ƫΡɉӣѬřǯҮ©ĵƉξѹżԟ£\x84ѡιF',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѕϱǸŽŊʶʽӎЍǼʤ½ɇƫψϦōʌ\x91ǅ\u03a2ɌѶǹÂΕǡķ˘Ȉ',
                                                                            'ԈŨð½ϚʄȑǇ˼íɣӴϠȻв\x9fɺѳЏœüϮѢӗʙӉϹ>]ľ',
                                                                            'ȄтҿҧðǟϤκџ§ÐfưҤЭшжƔҢäЗʢЋɡԤΎyϓ˔И',
                                                                            'ôȒͻҪӤ҉ɫǥҢŧĨҨȚŻčǃϬɬȽНѵȍ\u038bӲƦɼχĻ«Β',
                                                                            'ǚeнËˊȮ§ҥŲεĸ˗î<ÂƷˬʀǴǟˎ\x8d\x91$ŎӰè¹ȩԉ',
                                                                            '/ʶШ˾ӼЪɥЋťҲƜCɖU\x8cıȹ?ōѱqɇʉԮȓƪɊÈүԘ',
                                                                            'ɹыυŉɸҸˬήɶ˥ÏϦΙˡʨǚTНʉĢ\x8aΚťåɦŇʣȫʮƅ',
                                                                            'Ҩ¤Ӫӗͳ¨Уϻɜу\x80ŒηӐǳΫǽțϩвͷˮÃȯǠѱȚЍEґ',
                                                                            "ӐΥƢɦɈ°Ш˃ƃшӦʯϭΘŅ҈Һhʠƚ҂љκ˘'ΠʥþȴÞ",
                                                                            'ǌɁЇΆÒȐѥҼ\xadӁÑˆûşʫҪɪԫƋΣҁɴҕӉΝӠeʡĆȃ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЪφͷýŁȼçҗїƝИżǁͿǡǧēɽǶǱʂЄ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            663360.229986001,
                                                                            808965.1216446846,
                                                                            350801.42082350206,
                                                                            412548.9382490046,
                                                                            250983.87090593314,
                                                                            405095.584630847,
                                                                            644840.7491320501,
                                                                            681496.8402932253,
                                                                            732118.0057678589,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ψ0ѮɡŖ\x81\x90әѠίЖÃˋƌԦʪňϠӺ0ҟƭбԘÊӲН\x95йԔ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'lǄӬԟiτ\u0379ȃЕťǀӦ{ͶԦ˾ƅƮɸѶǃіȓʜжşƯԣζɠ',
                    'message': 'ŭζз[ȲҨӦɐʰƸŃ#ˏ\x81ΒȂłǍšɜ҂ɜšÖ˲ιǕæƗ£',
                    'arguments': [
                            {
                                        'name': 'θя_ɪȾæͲƖčѨɤOҦĬ϶žђǹɦ˸ƐŎŞɸʁǚʛnļǎ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ƥ\x7fёҠȃȬЭ˺þĺϮс\x84ĴŃʎŧқ˴ƼɚΓє˪ŔțϬÔÝӨ',
                                                                            'ЮĻΙ҇p\x96ɢΟϲǵԙţлʨҖζҧʗӿϹξīѡѠǂ\x9cʏ©\x87E',
                                                                            'öѯЧȼͲŲʤȉϛǺȧ+ƅѴӭ\x81҂ͺ˓pɣB|ʽљdàĶeʰ',
                                                                            'ıΓЯǖӏ+ƑÑ\x8fɫӦνƟҍƑÁҵ˳ΐЅԆϙȇɆ&˶с\x88İͲ',
                                                                            'ƇԮöləp1\x9bŊȨqɫĻѫ\x8aґѥͰ҃nĆ»ϴÝʗǮΐǵǛɁ',
                                                                            'њʐόǿјēСƉɋa˶Έҏʛșŏș˼ҋЈƥɑȱϿñΦƊ§чˏ',
                                                                            "ӊӂӝȃQҵҀ\x9dĒǙ0'ǮңȈƛӷVǵȆƧ[а8ўǣɉӘʶӦ",
                                                                            'ȹf҈ϖȡ\xadȄĆĀɚ£ǵÏӢV˦ýуϤɩƉϽ҂Ȼ \u0381ϒƣȡб',
                                                                            'ǲîȼԈƞʽʣ0ȖÄĹºΚɍ\xadͰƳʅÊҦsΑ҉ƕӦϘǞͽƹŢ',
                                                                            'ιÞVćʀ3ϯѲӠγѦËǕǴҮŏìĭ©Ĵ҉˟ѕ˳ΚНҔͱ¶Ƹ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӏŀϝǔѥ3ωзų*ɶǟ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 570486.7836461656,
                                                    },
                                    },
                            {
                                        'name': 'X\x95Ҟо\x96ŔƖԥʿϒĦɼςԡ®ȟŻ҈ɽʼũɄǿŤā\u038bѓǵ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.845010:+0000',
                                                                            '20220523:220031.845095:+0000',
                                                                            '20220523:220031.845177:+0000',
                                                                            '20220523:220031.845258:+0000',
                                                                            '20220523:220031.845338:+0000',
                                                                            '20220523:220031.845417:+0000',
                                                                            '20220523:220031.845497:+0000',
                                                                            '20220523:220031.845577:+0000',
                                                                            '20220523:220031.845656:+0000',
                                                                            '20220523:220031.845736:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЂбҎº˘ԍưП',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'оԔ% ®ǴƼʫƃ\x890īʪͱƮʳҡňŃѻίұƏҘʗӬİɌăŮ',
                                                    },
                                    },
                            {
                                        'name': 'ŀːėɜҰǃσ¹űōıʾğ˵Ҷ\x96[',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            915680.3774332233,
                                                                            920253.9173821092,
                                                                            965482.2480169027,
                                                                            -94940.07987925765,
                                                                            365514.5530535405,
                                                                            316725.31156150595,
                                                                            337211.5442619375,
                                                                            736611.1604018041,
                                                                            370543.10279291717,
                                                                            610368.400644553,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ZɥʼвĲЉӧŶǱ҃%ΚԇɉцķɹԗҁҫяμʳMưӶËŤΛӄ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 2987.883309723489,
                                                    },
                                    },
                            {
                                        'name': 'ƄҪʄěʶ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 708078.2192248142,
                                                    },
                                    },
                            {
                                        'name': 'ɷΟʧȣӶɒ\x82ԤөИԒñЃƱǪǔ\xa0ВʔǽŃϜ¥ɀϜCӴˍɃ˾',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.848758:+0000',
                                                    },
                                    },
                            {
                                        'name': '¡ǂЗʉӮҥӗϺâĦ˒GϑȦŝʰςŐӋåβ҄ѥȞ!ӕ\x8aКԍ%',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1017907430038682757,
                                                                            6091819978750944919,
                                                                            3275619381255995925,
                                                                            6692823016874542638,
                                                                            -4795111467390326285,
                                                                            2641844481121183622,
                                                                            8774186570528490270,
                                                                            -7012948374851877296,
                                                                            -3516265449873984417,
                                                                            3702489525745899758,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '±оǊľќ»ĈԌЏɣѧѭҜҦ½˒эĎȘϏĬФЙǬė¬nˎԇ8',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȁNҕѐâɯ\x81ĽŐЂԥCλHǲ®ŴŨʊɿ҈ϞYѰśȜӧѺĤĔ',
                    'message': 'ϖͱńυҤ!ʅŮ˦«ԙ0ʲ˭Üƥ%àZΑлɍɟҎІȽɄ²пВ',
                    'arguments': [
                            {
                                        'name': "Źʫˡ'ԭDȄȿӚԜMɦҐY˽ͽ",
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ЙϬˣäǾɩƸ+ҕÈĲąȘǦ˩>PΛҲϬθˣ®ɵԆѳ¦ԗ΅Ι',
                                                                            'ˎÏԐѹɉ˸ÖǺԧз҉òǊ\u0383αχдѣöŐΥɳʥ҇οʒԜ\x9fǛЎ',
                                                                            'е$ˋǕқĀЂ˙ǥ\x82þǽԌОȪфIɕҧ\xa0ұϦǇŢԕ.ҞӣƳǩ',
                                                                            'Ī69ΗǑϖČĿįYΙˏћѮʏжГю©ӓ¼Ȫɲɖ1ѰɘȄȯƬ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ď\x99ȝɅʅѝψ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ЈŅȼѿųϞƌĳɋVӂΪ҃ӜˌζҐǸŻǘхȀԥҠғ\x8bΨҠòг',
                                                    },
                                    },
                            {
                                        'name': 'σɌԕȻϖ?ÝΞɨā{чĠњȳɅȕўӓǄ҃|ԉïԂ\xadˇӣņă',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3781851662691981182,
                                                                            7663421466619207126,
                                                                            4456706221132852509,
                                                                            -1539079311667483152,
                                                                            -5312822913309765132,
                                                                            3646705810163371223,
                                                                            8852675166449447234,
                                                                            1281903304588601413,
                                                                            1699741454680751770,
                                                                            -8578045617334315508,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ťȻΙLBӈΘÚňӴ\u038dōőԈoїý:҈©ϻȵ\x7fБʡʛѯǍ\u0381˴',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.854078:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϟŁЉĸ˥\x92¡®ɨöèƘ^ΝэȄMʶșFʉҞȨǜĴһ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ѽϰƚƀ¯ÖѡǬϢԍȩVǺӲąñϹʦŮɼәˑˢĮ°Æ|Έ\x89-',
                                                                            'âƮ˼ίȣŪ˷ͿÒ˾ňʵӃΘƾôƊʎʋȥʠѾә¦ισƗҷʘҺ',
                                                                            'ÖɼϮʌ˲ԕѨɨȁЦѽǲˊԆҧòƶҹɜЀЎїƎțӁYļέʸʼ',
                                                                            'Ҁ\x93±ɚЁҫӱÔʶ˧ρԫ˵ɺªʶɕ\x9e˃ȩǯԣʁК?ѺӦtƲ¬',
                                                                            '˂Ó\u0380οćŽŔǃˍ0ɆƓǆƠ\x9cλȃϲǔΟ\x81˪P{ЀÝ\x82Źɟʛ',
                                                                            'ӻśҽˋǥĿΙĭĲģǖΗÎǼŷɟǫʤтĭϣŪϪԫӪ\x93жɺʱϏ',
                                                                            '£ƽ\x90ÁσuϛА\x8bÆχtȿԨƲĴҰëǭÉ˄ıƿƯ˘Ʃ:Ѐѧԉ',
                                                                            'МqƈʯҶӔľȀѱ\x8aĵȀɦǑ˓ˎѬĈϣ\u0380ϚōÉΨĂWѭЇԠë',
                                                                            'Ùѕӓ0ӷƀUĄɇƢ˝ŷņќƱɴŋØɉƳȠϔ\x9eɕåуҭѺìΆ',
                                                                            'ɫˈńԫӦԗėԭ˴ƼɧҥΘɮɫИ±ԙ¹ǿΞÈƐȅҸÇIъЌ¼',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǼǵЗНΓғ˛϶TȞԂΣЪуÂÚĉ˂ʾӋƿӹӬЩӟ?ȑɞϏʙ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220031.855892:+0000',
                                                                            '20220523:220031.855977:+0000',
                                                                            '20220523:220031.856064:+0000',
                                                                            '20220523:220031.856145:+0000',
                                                                            '20220523:220031.856225:+0000',
                                                                            '20220523:220031.856305:+0000',
                                                                            '20220523:220031.856385:+0000',
                                                                            '20220523:220031.856464:+0000',
                                                                            '20220523:220031.856543:+0000',
                                                                            '20220523:220031.856623:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȴƭƚƪ¿ɌϖЬɟΑѪŻͺУɒϾǭˮ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4054960477720752113,
                                                    },
                                    },
                            {
                                        'name': 'Ŗ˴\x9dʊԇȘҠԍɅЪЗÍПШƆŃӘˬǁÒȢȺϠū',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -70787.56743090696,
                                                                            208294.74253792613,
                                                                            -49809.037318075214,
                                                                            338720.6705538771,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҨǱȼɨБȩсŀΏΫɤҳөƲèӷɂĄѽƚ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -59073.88983530646,
                                                    },
                                    },
                            {
                                        'name': '\x98ъӆȌұФɖ˵Į+СϓϸҗªͷSßÞĩűӚϳӲ\x9aȻ\x94IòЍ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220031.858778:+0000',
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

            'identifier': 'ЯʰѦώ\x9c',

            'categories': [
                'access-restriction',
            ],

            'messages': [
                {
                    'catalog': 'Oƀ',
                    'message': 'ɿ',
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
            'name': 'ͶʞTРɗИԟʈʶѹϱЙǜǡОѠȒѲřԇӀ?ѪþχƪӚƗĻ2',
            'error': {
                'identifier': 'ʹмǪʁӽϏƑԚΞƱțƵКӣʿǈ҅ȏѭԛУȨЃҖм>ŴɄ҅ǥ',
                'categories': [
                    'internal',
                    'invalid-user-action',
                    'network',
                    'access-restriction',
                    'file',
                    'internal',
                    'network',
                    'network',
                    'network',
                    'os',
                ],
                'source': 'ӪėθԢ\x8d3Ԁɑ˛ƭƧɲ˓pȒaʟ¼ғҽҖʑ*ĐԠˊʹ϶ľʷ',
                'messages': [
                    {
                            'catalog': 'ŧΰHӛΉDҿɱơи˨ΉӨξƶ¢ŰΈӗґʵμІԓȣV0˭ˉЧ',
                            'message': ',ŴoŚΫȋПȹéфԩÏԥȩwыŗɏѯίʲʸǂ϶Й҈Κѝї\x95',
                            'arguments': [
                                        {
                                                        'name': 'đԊqJƹϺˎȸƑ£ϛΛĄhͶƿϯͰюûΌĢѺȪˎʋиʊƧҭ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 874415.2481984259,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǀǜ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 932156.5881303963,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĕʔʠĒӗѭӮ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӓӱǔʔϒӃфԭǞǆȾ÷Şžξ\xadŵΟӻˠżɾ˥өÚԬłǒʤЏ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.731014:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÓςƮҾ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.731433:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'èâƁNˢƵɂͳЅƥ\x90Ԃǐ1ňΠǶƾkʂŏƧДǝ˦ϮƠѝ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȹȂʂ\x9f˚ǥώǒȷӳΞ¨ϿôЯˡ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'БyӚόʑЖǏ?²Ȫ°ӎŴDӎϞȐʙ˴ԟȒԢ¯ς\x8bɈȣҍåШ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɂ\x88ю\x83ȓʫ¼\x8e͵ơ϶',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.733091:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˃ҔĠ)ϔʬȺʊ÷ӻͼƦΔʼB)ϘЁƉ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ţѤԦ èĄȶ©ĻʀѽҪǂƭʒƮĈbĹζǈԤɮ\x89ǥϿѠкÞ҅',
                            'message': '0ҭ>ϭ\x8aďŕłʧ\x7fǱҚƪҟıĭǦëϼӴ5҃ˤːΙˬʁɨŧʊ',
                            'arguments': [
                                        {
                                                        'name': 'Ǧ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ęӸǝǒɹЭ˩Ӡʍ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¤',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7907993614055142420,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҫȟԫȐɁ\u0383êȓšϓҍɛЕŅӒƵϐ˴ƸπǨ˛ŨӖǒδ\x8b>ϊż',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȃх˾Ƀ\x8a\x9boҚɟҘGƜљȺОһŬŇԃʟҔЖ\x7fȴȱôжĆħϣ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϗóǾřÜ˜РȕĀɗԦҕԨԉиÆˠǵҴƛɯÁ˖үUŴҴ˴ʽо',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.736532:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˲WԧѭʆԚľңːЫЅЖųŧĐ϶еШд#ȣԡϪŁõ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʹʻΉ¯Ӂʈ>ԨӖ¾ѓǩӼİ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҖƭӟˉԞÖ©ˬѹĥĵÙЁũаȃ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӎ\u0381ΤӲÙ\x84˶ϾëķФĢȺʭŻϟǛƁѱΪǏԐѐʳǁ©ҥǥYL',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 404813.70410318056,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ęȖţǌ[Óİΰ~.ʬǾԘʰίaԘØåÜɁˡȝļΏ\x95ԥSгˀ',
                            'message': 'ǆϽ¨χǪυΖqɁĐ҄ӱΟǠǏіɨӞɌԭǳʘҜȔҋĤË˘\u0381ǲ',
                            'arguments': [
                                        {
                                                        'name': 'ΠōΪϚūȭǙ\x80ФІ˻',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͳƠ ĴɿԦϽ҅ÀƓӡȕЀγ¤ҥȊ˥ƊϷ\u0383üɿ˽Ӯʃǭɶ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѪϫüȳG¯ɢĆƸçÒʺԭCрÞƸǴҸѵҰųςǩȄЃӮѽ\x9aƐ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɒ$Ēӊԫ+йķӪ\x85ëūëМŰbʛȦƌDћsɯȳ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ā',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'бӏŃϪӮșǣѺĀǹEĕǿġϕԫ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 757771.7024826816,
                                                                        },
                                                    },
                                        {
                                                        'name': 'τͳ\u038dçҠû\x82ČϭʯɯÌēΠ˷ǺƥςӟȧQʆǯԜʀȕþДďȔ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 961138.208531471,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƈUǑŔϧMčęȍ˽¯ġOǌǹ˦ƠԣԝҊņԩΝӀ\\ȳɒӰ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӓƷˡӇȸТҍΧԓ§ĘӴΥ)ҸЏÞʓ\x83ħȏiФҎѭӱ-ģϒҊ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Gĸ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˸;ˇɲ*Âç\\î¥ϡ»ǆɁˀԩӸǫΣ+åΣ%ȈȶЕɟΥӐɄ',
                            'message': 'ɞӏ҇ӎŢ2ÎϱǀԌ\x95ϡǳ\x92ΑȣЕѨħDIҥʀѷ΅ƳĽЎМӈ',
                            'arguments': [
                                        {
                                                        'name': '˶ŏĈѦҰ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǣǶ\x96˕ǍʾϧӋ¶ñǕſěȌʥԟўӜѵ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.744202:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x84ƖԓϳԘ0ûȩýʁɺΞŇƥʮЉӨƒѻӶĿӯԜʄϞ·ԗ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʛêʆjǊ\x9dϗɑðДİ,˼UƕȊɫʻŊсˣǶӞ˒ЮƊʃŜʛЫ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҵÃɻ˕ɫМˣ˩ŵÉʅϦʅўСѫΣĘҀΓӒǹʅҖǌƁ˭ϬMȅ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ͱжʱўĀИғϢѫϞˠͻdŲńØϤƯŪɄýԑϯѦɫƅΪêϤӘ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΔŻ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ơJӃAüFϼƖДҌBͲ\x99ĘɪӪƂћƻηνˬɟČ(=ƙɑңΜ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.745841:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'җΓԭԖȀƊ\x8dɷιѨ\x8cТ@ȲÝȵƕî\x8f=ћàӚΡҥŌȒӢóп',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ГȄТϿÐ*˗˾Ұ\u0379ͽХbǩËΔÅёӧɟȜǦʻǎ\x8bΉСӮͺ3',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΈԚΐƘ=˅ϋϻļĻ\x99ξ\u0379éϏˢWϪ÷ȈŘѣʝ¾Ԉ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.746656:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѐс',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŒѝԐ4ɩȯɗȘʽӖЊτϬƸǜȺƮúɹˀʚАŘϠЫFΊ,ſЗ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ЎτƱўºќǶŘƴƿϗ3ǕƨӇǀńԣҍȳɔʥζęƐ6ӺĥƘщ',
                            'message': 'чʟÚĵӔѿUjʃЭɔϚӟɪÊӁƿȫԦ\u03a2ŻĖΪμǐͲ\x80ϰʘǯ',
                            'arguments': [
                                        {
                                                        'name': 'ӒîʽĢūҊ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4041951863724134210,
                                                                        },
                                                    },
                                        {
                                                        'name': '˓ў',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.748786:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɍΒʕˀϿĚƚҽϺΧгȍȯѓŚѝǦȺa',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƓΗǿ÷˲ʉ\x8dΰȟЦΕʦɡȒĐĨΫʦЪɰýЦҺѤӼӉDѥ[í',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЊɋǣТԎʀJΥȷɷϨŮЍŅУʹ·Ҧʔ˅\x9aǃ˾ˍʜȲТė\x8aϏ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǄϙƮƶəǖ\x98ѫǂψƱǭʀХәӸʹʓьˀԗ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.750450:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˤǙҠ·\x95ʫȆħӏͳʠ\x87',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѱҞΏ6Ñʚ(İȈЙśҖȺʺ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'вˡİ\x98ʅӍƲήўɔÏ˝ԊϠ˃е\x9cʟ4ЯЛѽӝцʢ]ӥӌ°ʧ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͳʭ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɨқƴǄǐҊҞʹġ~ϻΜˡӯǰб˷ΏӠ˪Ӳӏ6ʆϨǃăďűŴ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ͿЀϜ˃țʕǃʚáӶĎ\x8dϥуɭ7Ǵѧɏϔ˂ϓјȃǚʈѪ×Bʩ',
                            'message': 'ϝΉΧ¨œ]ñӏMʡϬЩbŔη¥h\\ǥÌŨȯȶɐχӃȲʃ˝à',
                            'arguments': [
                                        {
                                                        'name': 'ȊѡǅҏCɷ¢κҋ\x81ƱîҶ˪ωʹ\x86Й˔řȔ҇βǢįϬ˳ǀНϳ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˴\x9eВȮļйϏή¨έʨЮʙ˅ȤzжІƶčMΝřӇăȠΨдĦB',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʦɥΜʧɧаĪǟTҲЭ\x8cĖƋԅΜǈӫψҟĤғϘŚľó®WFì',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϩ¿ŋ\x94ÄӯƶӴ˙ҜĥÔ҈ÈɃӏŹŕӫªѫȀķ˹ŷ\x91ѠϳȴǓ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ãºƚÔı§ʭƬ҈ϺͺťɼџԜ@ºʻԣǝϵȀ~òћ·ȒҊϙȸ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 357056.6696321082,
                                                                        },
                                                    },
                                        {
                                                        'name': '6ěȦɕsБΦǨӓJŪҿϭƄÔ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѹɅϽĵƋϦčÍƤȘԨʰҊƺǤķ)ҺŇǊt6ΪǮȽǹêԣӞ˫',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɚ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '^Ѽ:Κ˶ĉÊȳˈĀÚѦԅŦΝ\x92ʷʦѕӓ\\',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Trfғҡòф˲£\x8eŸЇĳDӭɈɵѺŮжĖ˟\x9bӋÝŲǨɘĠĦ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÔƛкөɬϦǬʕőϐŁ˪Ӭ˕ʼFтžϩǢʖǧ¢óʜϜӁƞFӝ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¸ЙϔȉƏΈӲй©Ĩ˴Ϫ˶§\x8fѡȤ˞ΥÆſŘѺɋҤ[ϓʗˊ\x87',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȵǏʞ\\Ǭ˕ɵiшЬn˘ƺɑǵŗƹ*ѡ¿ϭѫȠΈȑӎʘѕϷĐ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -800638971042207715,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԩF×ƮϒʠϖћůʊϨʾ\x8bϙИ·DɁѸǑқ\x99ęžԌϷсŮǷɌ',
                            'message': '.Ӟˍ[ȋ˗ϛЎМӑƤԝȖϞɠζɉƞҩȠҜίӝĜɄоȌЗҽȨ',
                            'arguments': [
                                        {
                                                        'name': 'ƲҢ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƹԦ˞ƖîЍħˠŤ3',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӒΟɚǴʴBɕ¬҉\x95śԁřеȼÂűɮ˓\x86ӻЛôJӒԑø\x9cěʒ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ињвҠɹɇƄǆӰȾąĢ7Ԇ˫șŐӿ=ѥµ`Ƀ˱ҢČ@ȵtԋ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȱɦƶ\x8bČcȗåĢǼ<Ǣ˙ǀfãǚ˦ЮГƍ˳eǉŰȒșңƸѐ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɠƾϾȸʮ˭Ƭ~дȓƚ\x88',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǖ˧ΫϳǭЁњҬeәĔ¿ėψАΉǝŐϖ˛˔ˍ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˔ʀ˥˰VkБőĘ\x9aΩ\xadћϡǥОƦõфƔʕ Ŀ\u03a2¥ƄǄˍĞӯ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЈԮōіȯŕǁƛȚȨԋԗɠˌ¹ӧÎƜʣȧ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЀМëҟΡϿЛ˟ЊKͼ҇',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 677698.7836371679,
                                                                        },
                                                    },
                                        {
                                                        'name': '˧Ĺ\x9còÙ)HČHÃ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƥˉ\u0378˺ҝԕҖȹҖѨʥɔƆȁοˍĄȺӄ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԁӽƭ\x93\x84Җ',
                            'message': 'ѮŏɉǧąȹΕýćʨØĞЩʠñҽѬ\u03a2İӫԥÉѮЇЁŊʿǰîƳ',
                            'arguments': [
                                        {
                                                        'name': 'ķ˟ˡ5Ғʆĩѽ҃7ōҋėӃԐ\x88ԨԗƷ˖Е',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ěn³"ajѠԄ˺Ӡӝ»ǎǟΈ³ŦьξӬԃ0ѳƕ\u038dƠсΎ˛\x90',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƝXbąϐȁҽġ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'øs˨ˬѩ\x7fnzīӗѫŉʏĒӯƶnƼǩԒ˧ŢԈϲћˠϸ˵ȅȅ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.763102:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǐ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '^ϐ¨ƣ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.763912:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ШвѰȅˏɑÀҋ҈ʀ<ȶˋȱƫ/ҭϭΕųĮκϞқbXΖ\x99ҹȋ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӄ˰ǃɕ˻ƷvӞʤҲğе}ũӶƑѰͰ҂ɽʅ*ʢĚÒйӱƝҎŦ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ж\x87ФȑʉͽŵĮĜmňʔˉ˜Dұ ˚ίQ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʌƑȍɁӎtΈȿɌѲйŰŋИЉПđŔȊKŭӌɏůƃϙǪѝƿϝ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʚёγʁќSӪμɒɆȩӿǡbØɎġоƳιˆΝŕȷӅԣШс˫ƒ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɫ˅ЬЅƐˁ\x8eΣ\x82υǂӴѮ@ѴəӢǅ҂»óĀĂ\u0382˞¢˕ƧÐª',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ұĘóҚӌƝʨ\u0378ʹÜκʾȋˣѐҟӫ1ӰыŊŗҞϭƭɫóȲĽӖ',
                            'message': 'ėŷϣԘɍȖԨ˷ƝÏϳшÖ҇ǐзǤϙӄ˲˭Ԕ˒ĀǇȞāę°Õ',
                            'arguments': [
                                        {
                                                        'name': 'ĕʎŠȫäԣԖ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҚҤƪϚiŏcϊϓWӞɋŸĿĹ˟Ǜżϋ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ќɫϺĀƓȳʵżŠˀŷfʯǛѦŻӯΎ~ΝΟ9ÎҎłˬƫɅ˯ԣ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŭԙ\x89ӧΥ¤ϵŝɵЯˬɺ҉ȑ{ϕѪ\xa0K\x93ĮčфȨ˫еĮӝ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5576737468461656674,
                                                                        },
                                                    },
                                        {
                                                        'name': '~ŏСƹүƭwƘʬʹ҇',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 981359.9831547921,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǃ\x96ʓҠĳǮõSʭѭӲˍЏ˒ɒ¸Ѝҩͱ¥хʭГɚšƘɐ³Ҏϻ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѻҏ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӽҺɲ˷\x84Ǥ˹ǣΖϢĹˢŝ\x88ɆʣƭʙǾƝȸҲљįȡеĸϺĪӓ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŞÅΎŧƓƸЛͽԍϷҷʶȆЌĒĈҘӷ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': "ԈИԐǽЪ҃ҮҏȚҼԜ¸Ƶıё'ǒ΅ŹѷWӳĐХκϓѪұ\x99Ș",
                            'message': 'ϸӯŏ`ÅǢDƩÖӟҴƏɳĳѐɀRŶκ\xa0ҾӞŤϮχƯA˖ŀӾ',
                            'arguments': [
                                        {
                                                        'name': '˺ԙϪÐƘЍŲЛӴ\x88íԈαԏǌϡīĽҊЦÏҔγŘӟàԮ\u0382Ξ9',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2409754678625801628,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʔΠƕҡЍ,¼ρҊŪɫͽѰ\x89ǃӂť\u038bNu',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɰΟӬШöčŵγŮ#ʇҺįǺ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220031.771974:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'үñȦЪǄǠѡƖʱЉȯ6җçҩϭʟΓΣ\x95ѻɃ˝ЁϙĸØăŎ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѣ\u0380@ӇѳŘǵʢxƋ˻ƥɚТɂn\xadŤąϠ7ԐHϸǐȁА¿Ѱɨ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'æǷ÷ƌх҉ʤѵ˦Ǒʹʶч\x8eƆǃĕòȜȆƓәĉԈӹƘe˧',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȌIɫçľӁД\u0378˘\x88Ǟ_ɮɐъT\x9f)/ê҈ư²Ƅ1ĶńȨ˱ʲ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4781788288384960059,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѴΈ÷\x8dџ{ɝ˪˽ӖɤĄť',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԂǬԆǒɵʫʇг*ãÇà£ʘ˩Ы\x9eϧμƪқďȧԒӈ˻ҟυɭˇ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Й˄õӜʼŀ=ύӽʔãȊШʴ!ИǀγōԠĶЀĵʴțϱɹҾȶԨ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 771458.8072950161,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɛʒӱҡxɼϧӎԩȚȂϜȲӝ ƆӲŊù3\x9cǤůĭŅtϋHɅȑ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǋűbʘϼԒɴìȚ/ʫŉҧԗævɈЀĻԤЇʽҝͻɭЎΕÑˑū',
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

            'name': 'ВϣŘ',

            'error': {
                'identifier': '˚ҧȬˡƙ',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': '¸y',
                            'message': '\u0381',
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
            'event_id': 'ɿˌȬϭ\x96ԁżӇαһ¹șΪԡřǹ҈Ӹ>Ӄ˭ԓчёϘ˴ʽţβǽ',
            'target_id': 'ĕ}ʺ҂ϫžʱʵǪŘɦÑΖ9ĞkͺѨƤȿĉƥʉ]ҫȓ;Ԉƚѽ',
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
                    'event_id': 'Ш}·Ϋ҈ͼÎ˻Ҋm:ȆqȜˬO<ӿԆÊʲɩˆ9Ϟ>ǻѲơƅ',
                    'target_id': 'ԥЕǇlęŊÒӾҏʓʶ¥σŔƕ',
                },
                {
                    'event_id': 'ɈѠдĔ·\x8cȭŏǤҐ&\x8cȠİɄΕƖɉҳǖĂ©ѠºƦȋˊšė҂',
                    'target_id': 'HѺӇ˦ƭĄЭˁ|ƔĘϯԈ',
                },
                {
                    'event_id': 'ҏҡϨĒͲϭјÑЙɉӽǴΊϫÓ¦ũJҧƓʃěQͰvΡ¶ȐħԄ',
                    'target_id': '҉Ôɘˏ˕ԋȘ³ǓɳӎԎѳЗʜԉѕũʟ˳ ōфѡŋʸˇǤӟî',
                },
                {
                    'event_id': 'ɤƵĺgн~хHӃўԀŧΪÐźːͺiОϻʠ3νˮŘόgɀəԁ',
                    'target_id': 'ϹϽӃӖǒĝҌΩȺɐђԌҲѹɱͽď˳\x88ǑĂԖĝʸNŲΆ ʩ)',
                },
                {
                    'event_id': 'ȣһǇU˩ҽŴ˹ɔѦκҬlʯCǮ¶ɭ\x8d,vȢӡҊӠƖѩпmП',
                    'target_id': '\x85\x8bȩ\u0383ŨʁĽ˟ŗƤдϿȃɰÏԛȆǑʹʅɟůȡӂϣǳɥ˟ǖл',
                },
                {
                    'event_id': 'ʲӨƸώȶăώ˶ӪьɫӲωёȟ½ыƢȁĔӻˮŁÈƕӢ\x9c˖˓ƨ',
                    'target_id': 'ǫÿŪʁȉ˕ŖɎЮ\x83ĔȻ˳ϕГĵpʄƔ]ҵˀǆˬаɼŖSÓө',
                },
                {
                    'event_id': 'ҪȰŌɁŔǯ\x8dŦҽИ}˙Ļ½ˁ˅мǼζ˪ӨţĜǵʣϏҴʺѾθ',
                    'target_id': '£Ƙ\u03a2Ԍ}ψ½ʴ°Ԋ¹ͻиΌ\x81і϶ɪʷШū\x85ɞD¾εǶ°ōД',
                },
                {
                    'event_id': 'ƥɩƟïŷŗ˃Ͻ϶ϣͺԃNɽ˖ÃɛРџʷԡѮÇѶϱъѰќȅҨ',
                    'target_id': 'ʀԃӤƐŇŵʁђ]Ӌɏύƴǝ˩ԦǚƫͲЮʒԁӉEүiʍӼǊƐ',
                },
                {
                    'event_id': 'Ȳvԍ˗ÇjɇгσΓѨІŵӣΚȋ´ӨĩŌn˧Ѵ\u0378ɖ+ʮĞœ҆',
                    'target_id': 'ҩɉФƿưͻҙŧȮы"ǎώƲҮˋ"ɻêѥΩĈАÕƱԫqϟȊƍ',
                },
                {
                    'event_id': '҈¯4¢ƕӧ]',
                    'target_id': 'ъӁæķˆɫ҄ǉƼѻƂǨÓʸӛ˻ǜӌȥŹѰɅɋϷªшйɰÿŧ',
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
                    'event_id': 'оȲģʥkŲҮùϘŰÁԉȝǰүхҮїӲˋԊǪʎԗYƬЂρʌϘ',
                    'target_id': 'ԭXƩZǞʥӫҩǕћҊ',
                },
                {
                    'event_id': 'ϟrńČĀнuӼħąԔŞƋšĎҖǋϮɊǿgЬӡӆƻ˙·Еôċ',
                    'target_id': 'īʽԊϰ\u0379Çԑɠiɉ˾Һˤ˭ʯĺаƶǲßƛԧʹȿΛΎ˟ϘÍȖ',
                },
                {
                    'event_id': 'Ќ-{ŋŢĠ˩ԈŷǫyĘăøϪϚœ\x9aʙСȊїϠȄĸѮΈӵҙ\x95',
                    'target_id': 'ǏǎϓѼґϗdΦĽĺҿȏ\x88ӰКввʺʀˑϰΗӽϛϢǻɁΏӺϫ',
                },
                {
                    'event_id': 'ěá"Ңǧај]ŃѸΠƖǝŭ¯РƧĳӔŅ{ȥɅ>ԩĊ˻ѼҎЖ',
                    'target_id': 'ϤŠňԃќԂĊȥōχrȸΫQɔЈ˧ΘʅǐƢŔȇнĚɫѠͺшԛ',
                },
                {
                    'event_id': 'Ȏɨӵ´Ȗćƀv˫ϪƙŉʵΕżƗv˥ŷMõ:н˼ԠūĚĬʺˁ',
                    'target_id': 'ǭȶ]Ӓŋ0ЛƘäҐԖϪǷүѮÈɎƮɄԊ\x96ŮƁɧ$Ǘ×ɂŁϳ',
                },
                {
                    'event_id': 'ʻВҁwʆӥӭJϵԪťȰɣ҈ШùâŰϗcǔȷҠ±YԋĹδÐӢ',
                    'target_id': 'đȃГʨ"ώīƾɲˠɗƼÖĜ»Ɇ˃ŋǎõâƚɀԏüǚ˦Ȃӏǩ',
                },
                {
                    'event_id': 'Eԟ¦ӃЗҜʙѓ˯ӷrϭɒʂɉȊͻϺԍΒLɖҧˑýǊӹ&сϰ',
                    'target_id': 'ΓśʜљĀ҇˭\x8dʙ\x8aέơcƇģӳÐïԌǈӞů5õŴłϻϚϝ˥',
                },
                {
                    'event_id': '}ίԘЄČŏѭǖɋŐȑǣԝƜ\x9dɪϬӰÄɲ˽ѱɠϛŉjȌɎ˂ѻ',
                    'target_id': 'βӦ\u0378\x7fVɡ\u0380ΌQ˪aơηѻġ\x9cθтԐŋԩǦǡϾ$ьԮϡηɕ',
                },
                {
                    'event_id': '\x91ȣά˺ůΧ·ˍԁłƑ˂ԍɼEҽǰÆҸȮsǂ\u0378ΜɥÁ±ͳʝʼ',
                    'target_id': 'ůɷҠźωȸɧ˫ҮȊȷԞ¢˅˱Χб\x81ɃрȡԇÚÕŚeƜԏɢ¾',
                },
                {
                    'event_id': 'ѷǺ\u0381nɘe3өǜƗ~@ȿʿΒsӂΞĜ¬ƁŀĬƏɦƕƜҋƦΣ',
                    'target_id': 'ơҷǣƖӝͺ˔ѴΒ¯ƑВȩʣҤ˰ϣΖςɕ˼ɓˬӦѯĩӧЈŌӜ',
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
