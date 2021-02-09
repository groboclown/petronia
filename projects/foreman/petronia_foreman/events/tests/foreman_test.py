# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-09T22:28:51.968204+00:00

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
                'ŋǪҶǅҮФơΝƾǤɨŃǥʄʪПΫРϿáҾ6gçѩүǺɮ҈ˬ',
                '˯уӄ˷Ǡ\u0378űƃÃωŃlҚәƙŝΟ҃ΆёʙƦɌĦțÒǩƤąƭ',
                'ÙˈѲŜχԑüɍ&˵ɴȥɬѣ>Я±ѦƐɯѠҖ$k҃Ǜ˩˧Ϥī',
                'ӗ˼KǽŪӜģƉЃƹáБȩЌɓúӰv,ŁӳҤЋȵiȣˈљ˴ɗ',
                'зЇ¿ɰºΟÿǓʯƘпύýȩġƫÏ϶ԈʯώƢӖʣҞѸҭбʙ˖',
                'KƭӤЄϵҔҙӅԘŮ-ǔȭfȗŸVώƊӐeҙ5ϻϤ˨ʇPˀҥ',
                'ЪʹӾ˾чÒĽͱ\xa0ҐɌӉǙыϐɝȥҢÏſ&҇fǀҰːǸëęρ',
                'ˁɋԠˎβƸƷłɪϧͽϲЎù$ɾSʎĨԋΊʘµu\x80Ѝϒʼўǵ',
                'ϓǯƛˌȰτӤǶɾΔDȜķ~ʫɰɓƷЅʠʳԩϋʫΈɅĈɄǐͺ',
                '˖ņʃˁӂȊȽÏϮȏ*˃åĔVԮДȓΐȚ·џºΈŜѰ\x86jԈӽ',
            ],
            'source_id_prefixes': [
                'ʃЅїƈƶˀŒԫҩŚǁΒæʭʆɝǼӷýȧa\x85ϭѹǶĒϘʦUÒ',
                '˖ɗӨÕʣʇ҃тĹʮˑϱýҾ¦Ɉ\x96ː\x80ƬљӴԠӴΣԅƟҘŻƠ',
                'Áϻȗӓϝï˯ҝԝ_ÙҜԍ,ϥʹè#ȚΡӠĞɈ҄"ƲɀĶҘª',
                '¿ũϼтӠԞЁϒǾɦȱȜǎϐЩВәɧΔIɵԡȈɹƩ!ҟǮƅĪ',
                'ĘЮԬʤǼӶӍǤǖԒ\x7fʌĐ˨ƐԝΖѪ҆Ÿ¡ӨǷΜ',
                'ȍƛȟƃмϞbȌйƀɁġʼȥκʭкıĭû.ǱӑȨɸYǗǂ˦Κ',
                'ȇÅѤʉƒЁЮϑƮ҈ȯ¿δmӏÂ˼ʟ˂ʽȍоˁʣӘѲЯ˷ʲȻ',
                'ӸͳųǂÞԄǀɂԎǽăǍϜиѰԅΜȳ\x8fҩǗυ˲ǆʫƚʈ(ĉɛ',
                'ҤԄZɷťκ¾ΏȩǖӧЪ ύ΅Áěӗԉ\x84ʫ˄ѩԢÇɐEȥȘώ',
                'ÔЗƂ˴ϗÒҔʙЏȲ4ôŧÈȥϹǸʊǄǛȆʦȢǸçĨǪϦʪ\u0381',
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
            'action': 'ĤєøǹѨǙ\x86ūкſŖρŘѮǅąжʰˇŪҶǞфҷϯȒ\x8b\x94Οȸ',
            'resources': [
                '\xadΘžϋѐɾΙŜʚŸJěҷǓ£ȘѳĆ?ЀȞϗєÖǒ\x93ȥˈÞ1',
                "ԙ˄ϳηϙԧԇν'ɺӣЭяŲ҃ӚʁǧâǭʨΑк˒pЮԗƫĿʻ",
                'ĿҴЎƪșӻUҀˎҠ\x7fрӤӄԭF˴ƉÆǨҁҌԤ%Ñ˕ԏȢѩ\xa0',
                'ѮɘϘ{т(ǢţЏʃ\x8fƧĤȉQғòʆԌ\x88\u0382ǃ&ҭӲȵʠ\u038bҟî',
                'ƗDêƋϡʟǣϧҥÉʙđЫЙͺ\x8aȱ˓Sȗ˱ӕԖĲДsјʞӫȺ',
                'ҁ҈A˓ҾȾɑҒĲǤХ˅ˏ?ІmʤȢǧ҉ȨÖӄüȋϳKɧϚǬ',
                'ŭɣӟĉŰ\x89ÇʞƖŜƧί!¥˽HԥǾīĴΩǐĩ6ЁϟɩЯT\x89',
                ']ϨčѶӐϟäëʀӹ˧εǿјϣ1wÚ\x9bӬЋ҈ήȯ\x7fӰ\\ĭϊЀ',
                'ˡʠНԨҺζƙʘ˪\x8dмҎȭҀʫɪĞʊӡɩ\x8aƾêĂďΥӳ/ǬЋ',
                '°ԔΡʮяƐȉĝК҆˥ǳυҒ\x99ŉϰˊ\u0381¸ѫ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': '-',

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
            'name': 'Ив;ų|ºŝˎʡƂɔѨɭΑ˘Ҿɮ;ӳӒԈңťĮ\u0381ӗƐʪЙɕ',
            'version': [
                -371163291138898622,
                -5216843033448078211,
                -2707972040643110969,
            ],
            'location': [
                'Ҙ¿ƌʣšȯЈĖύҫ\x8eԠ·ďÀƪȯȶӡĝŕӱ˽;bțӨ|ҵȮ',
                'Ȯ˂ōϋɀΨӄΟΣȬŔɒДкʔ҄ɁΠӛѤʐɏӋџөсſʐƤѯ',
                'æĚœW\'ϗѫƞԡƼ"ʇҴ¸ϾԭäPӎԣȇɊΛɚªԞҠɾĭɺ',
                '÷Ɖ$ɄΕŻĿC+ƭſЍŅH\u0379ČʺȘä\xa0%ԫ˖Ƨ)ɛ?³œĢ',
                'ǸԌÎƦхǃÄ҄\x96\u0379őɅ;ų\x9fūϏК\x89\x89"ĝϮϷԇ҄ϻԔЬǹ',
                'ƽǎǲŮЏɯȼϖiŽ\x94ȠmѪѧʇÓыǻϬӌӋ1Ƃė:ȲŸxÆ',
            ],
            'runtime': 'ϚȊɜɨHʑʨƼұłөɍ҈ƗǾǭˡçǧǟȳhӅãȔԍæӕѻƻ',
            'send_access': {
                'event_ids': [
                    '#ɺДЇͽǴΛћʼɑϴ\x92qи¡ɧʍЙҼƆƓTИёӈĕʁ\x84ș¥',
                    '¥ŮͺɭɸϙεУԩőЦĥѣΝӌđΧƲПʙ\x93ʏԛɈʻƛƶí˪ǘ',
                    'ŘӱɪʟʟҺɜΔʢʐТŞїÒϭâƍʖɏəмєӸĢ҆ͺȫ\x84ѳҔ',
                    'ԄΔЏàӊ˗ȁɿâ\x9aȞ\x98ёɺǡɶЮ5ȻԤ˯ČӶωЖӪʠϾɨ\x88',
                    'ɻʆϲĨͻЈԨ҄Ǧ¶réυíʤΗ¾ɽˢɸȓΔȝӈ\x8fϪƜҤǧ]',
                    'ȞРЊČКōWӽǿÕӂʠ϶ЦԍĻĐ\x9aғӾƈ˝ƤԒ˺ȋ8ʚëɦ',
                    'ȬžŞӛѕӤɠ¨ʕΒȝźƮυɩQWƻȇŪǍАͷɾȰѪûЭéͿ',
                    'ÅƯѸĆԐƍВŇƘ˦ɜÎĺЇNӺůnĈԘ˂ǺR£їΟεʛĎɜ',
                    'оeщˮʛҶҥ7ňĖ\\ԙØ˄ɁƖɼÍ1\x7fǿ˰Ӵ',
                    'ĘžLqԡǥgƅˣȽ˩ǼΠҘӳ',
                ],
                'source_id_prefixes': [
                    'ȥϸӇȳɳĦʗҔǬШˌĀΚяɪ΄ʓӱҫêøǡҴƘдΙίԋσj',
                    'ɵǪЦx}ǵƁ:ȯӂ˃ʑХΟѺҌŐƀ˩ˇ|тÒµ\xa0ґȋʢԚ)',
                    'ƲɅçħӧÐĤŧʅʌʟȓΏԖ',
                    'bӌӾΖɳąǤPüˇzѪȏԪҾ\x89ϛΪ|ԬӓϤϴӈΦʳę-Ƶǅ',
                    'ы˪ʞ˒Ӎԋӓǈâė·ØÐȍĆӂδцэŒγGĉ_ӸϿƲǇЪɞ',
                    'đ˲Ʈ˾ѴΑӽ͵ψğǀ˾Ӿ|Ϝ͵Ȯʽ͵ԙęLu˕ӞɅɎĸúΝ',
                    'ΰĿĊӇ\x84ʻÄИî˭ӄȂ8Ԍʘ˸\x85ǧiɄʽŗĞЁǙӓýПҌɣ',
                    'ͼöķҸÝţ˓ѧťȽſĉßĤĉȇĤѨЖǐɚā§ԀԑRɁԇіǐ',
                    'ʐԩďύˡѠSYӞƦǪÝųʾÏǴӯǖȤϵԪ_[ӀԨʥ',
                    'ʔǩŎҨŵʲеԘΆԦ·пʔǦć\x97ɲҩщ\x92ҸһɊҲ%ˣϣŘûê',
                ],
            },
            'configuration': 'ãйϜȾóÁŚҤѥwǣϒĒɻɚΚʂz\u0380¡ɶƈϪͲϊɍǌϤǡĠ',
            'permissions': [
                {
                    'action': '΅ҀĻˬ',
                    'resources': [
                            'ϐƈϣØϽѺЪg͵ϱԥǾӹŴ҈½С¿yƱЉѶÈϺѱ\x95ȶӥŔȸ',
                            'ÈЎʹ@ǏŸǬӂ΄ɍ\u0382\x88ԖǺNҀΧ*¦ɿοѾɕʡ˙ϐӡѻлЩ',
                            'ɿӟәξТMPԬύǱîźǶɆΥʉ\x9a\u038bʪ˾ĄρѽĳŁŗɀέԤǇ',
                            'ѰʣĜΎǜϘҙρҞșǛВïoʘÿƙƧƭƊȭ¼eϿπЎGţ\x82r',
                            'ϔϘ±ʪĵYˍˠxΡй\x94ɜŢǜǦsȢЊȃĎ΄ǂXƱφƺϥǊȃ',
                            ':ŢЁψ\x96ź\x8eǔŭ\x80ΖýʂȺӹϝȨƹǜϝ)ԁFƟӥчѴĳԧ½',
                            '§ʎ\u03a2"ѵԠşӚȁќΔɖŝ˙³ǷěĴƅИȡʣϷƤȔƫЯπƗс',
                            'ǪϹɼ\x8dƨΝϧҨɊПɨѨƌʽϮLҾǐ΅ωѮϞˆӗˊИʲŀ/Η',
                            '\x7fɷɟ*ЇȮʝƽüʄҋͰԂʕɘԦßЈǔԞċƼńґ\x8aӫɩˑǴȤ',
                            'ŶŬΖĊHЅČӾņųԚ˝ȜĊɹ=VϱƢФӮҘȬ\x98aȄӯХͷϸ',
                        ],
                },
                {
                    'action': 'ҡZɟƆάȔȽҁíī\u038bơгȝԦ!ӥο˖ҔȃΐÙȻӿѧ\x86Ìџ˕',
                    'resources': [
                            'ӀәɀƊϼҵȋΩԖƹԎҲƓž\x7fɓЀӶǉÕԠκ˄ϚГȒǶӀƝǕ',
                            'ÍɐǆӤûɖɎĩ\x90ƔɇƝ\u038bкűȻΞʧɻȦ˺УјэɀƟԃŠ\x91Ɓ',
                            'ύʊVǥіÔБϓдʤʇİϊӱәѽÕӨȦƇˁşƜÕʾ/Νżǈȁ',
                            'ύɓ\x8bɎ}˼ӳ÷ɂ±ԤŸ/рˡF£Σ ɓǚ*MȺȦ϶ԤĊÂ*',
                            'Ьɘӻşԥ ɇʎĤưžѾĈ%\u038būƈ\u0383˕ǫұӼǎ{ƎÉƺǫoҹ',
                            'ʍϲ\x89ŭĸѓ˒ӯ¨ϫĿǠyΈȘ¦ϕŊԟϰǚøAȤӳƸīϑͷί',
                            'ИҫĿʡω¥Ő÷иΝʥ\x80ρ\x87gʙ\x8bσ҄ӳϢŃƈ*Ә˓Ǯʿ×ȡ',
                            'ԊӷəҲʐˋˑ²ɮҳǯ\x87ƐѰȗɌɒ҂¿ǸƚƐʑņȢδӘʄóȵ',
                            'ʹ]ɐɩΣҿҪǻФȅƫΨѿ?\u03a2ҌЎӯғϒČƔŏɜ»ćȩÝӛʈ',
                            'ҳԟӤʶŰǑЕқȕЮȨd˜Ѕʲ\x96KĲƉìͻşЎшȁяҿȼѾϻ',
                        ],
                },
                {
                    'action': "\xadϯčϵά?ˣȺɪ˓'ѦЀхӜɓԬќȑú¨ʃѮҤG¹Ϸ\x84ƙϙ",
                    'resources': [
                            'õɥěʟԨϐΣȆκʹ\x9dǞƳ¸ɖ\x8cɅ54ȇ"ĺѠÅ×\x8fГиҪʯ',
                            'ƿ²cйƍŭūʉі\u0379ȅƎɁ4Ӳλ˭EȧϓηԪȥɬʍǘưĈɱÒ',
                            'ҰԘӓɊɏȄԏό)ȭˮā¸ЁW\x87ϋԌѰÒʺ˩ãʷ\x8cћǹӏǑų',
                            'ƣрňɁƣ«Ǔ˩Ѩ®ȄˀŠӵńяӨʏĪŃϕˉʊɠ˷ǢԅϠςх',
                            '{ē\x7fčĲǤ\x9fȞʉяrРѥɻƫ˸Ӳ\x81Ѝʷљγ+ɸǰҽÙͷ;˝',
                            'φöӈϬƍ\\ƙȿϕԮȍӹϜԓԋŨӠ\x97˥ΡӎҸАăҔĲԇΤӵѲ',
                            'ʛθǪÊҵ$·ҳęЉđϜԜΔʺ½УôѠe\x94ę\x98ʶˡ˒ϒşԬѹ',
                            'ƚӴӓʬǢѥӵӘ¬ĸǡGċаƦǱŖҿũӝʳeȌfӃƾxоǴХ',
                            'ʜˬÞёaҖѿΑѕΈǬυКʌөʍђǮ¯ȍӘσɦΘ҃ȜJ˓žΑ',
                            'ȢЗŕʻğȜʸĔʛʑΆϼɸӵѹлž˵ƯŻƙgĎÔʾΟӒ˅œȜ',
                        ],
                },
                {
                    'action': 'ċƵӸɹҜХеɁɫȻ\x95Ϛoĳ\x8a\u038bƠưϠǽ¢ГçΫ5ϠɱãĂç',
                    'resources': [
                            'ҿ*ěуɱіÁ?Ԛěψǝ˄lŬхŘȹЮßϵǉϬϰŹǥӣк\x9a\x88',
                            'cӒ͵ƵtɧêȾƲǨʯïҟΓҮ˰ΓV',
                            'ÿσĞɵԑнǹȘƈÏϭÑԮԦүӶýǶϻъӻʻѧȞœ˓ȮĔЪў',
                            '\x89ȾЊïȇҶӣĚһϟYCϑØͶΎѤÄЫҧҠŐ±˵ѸӅ҇\u0382\x83Ş',
                            '\u03a2əǰЭ,ǛƆȞϲɠӮǨɶ˱˲áҬԘɲ¾ӋɀуɩDӹӁǦƫĞ',
                            'ƆωǋǥӤͻªˣњɣWƳԓҳВϛƌɻӥŌɰӸΏђŃĪɹŦӼЪ',
                            'ÆρjʙÌʎǗƹ˔Ӝ˪ӎϿϡŰ\x94ʮȒżѼǮΰґѹъԡĠԙƎŰ',
                            'Ε\x99˔qєѷ9ΙɸѻƪԬ=ԡƻӶ\x82ŁїˌΓБPęwĴȒЯҶ·',
                            'ɱΤєʰȬĶӠ+ѼǖҜɧ\x7fԎӒ˝жŴϐԔƧҞϨȺϹΐʯƅ˸ҳ',
                            'ºρӊôӾѮŗµҡ\u038bҾɩȍΐîµıɗвʑ3ǯјχѯÓòϮҪǳ',
                        ],
                },
                {
                    'action': 'Ԫӝǽ\x95˸Ӏ¼ѼѤԝƯжȥȨɝʉǿʣʕԩȽ9˘ӞȩҗƋĄӧͽ',
                    'resources': [
                            'σÖ?ӒĽŋҡʱɉѐƘԁˢӔϛԅE κǹΎwȖƼϢƿЦř-Ϭ',
                            'ġŖ3eƉˏҹ\x8dğɤa\x83ӞÉͰȢDɢʩҽƍҳӱǾŘΥϷɤɁӋ',
                            '·їӜѥӭӝƗҤΛЏԣ:˧ƞԍŤʊϳʚȭç-ʤʹÂʲι˙ĔÍ',
                            'ҿǗĨǒѝӼΛí|ҐȨ?˖СϋъԌ\u038dҽª/ûϢїȵЧŃ\x7fɮȫ',
                            'Ǚ6²уęǵŠӭєɶǺǴŒАċͺϩԍѕűøɩΖĒΊȉϷ;&Ų',
                            'Ӽ͵˃ҘѺoԘê\u0382ŭϼȔĀoҏΞȫȕ\u0381εɁҀҼQĶʦȰ=ӧΨ',
                            'Ũ5эʮϸ_\x82ИʻѹƈƸνЗŦΝҬɱäÀɒƗƛɺ{ԏӝɜΦΓ',
                            'Р"%ѹˤψѫч˄ªǷЌǒęʰхԅʅѤɋǊϏӈԫϺƈԌ\x84ӹÇ',
                            'ķҕ¸ԗ3\x8cϟҺōҮѧəѹӼƋūˬΠǞǱҕ҅ѥɿǢʂӮεȑҴ',
                            'Ӛ˕ɁѡԐǺԅʋҰĳ϶ȖʫҖ3ϵύ\x83\x8e˸¼ɚVбĦǏ@Гɿu',
                        ],
                },
                {
                    'action': 'ĄŸ¹ѸƜΟůϋђȂǩ˳Ә\x8eԉJ|ίʞҡ',
                    'resources': [
                            '®ԋɖ˧ŹõСγ3ҕº˕<ʄќ,ƖӖɑ\x8bΥüůΛöεԮ9ɉͳ',
                            'ϬжЁ˟ȫĜɗà\x8dÂ͵ĆŵΣϝѷԨŚƭʂǙĩɊːф˽ȶÐѸ҄',
                            'ȻҹɁӿƱ͵ěΟԈԂv5Љǎĥ\x91ǌțҿϓƌɋǌҏɌφƐHǛʉ',
                            "ǻԠƲѮ¡Ɔσ˵Æ\x86ѥÀʅĕ'ɿƾǺοɧΒӶȶÏ²˨ƱǒʐǇ",
                            '\x9f',
                            'ϷӝǮҍЏәԌԛʦñӻơ¬ʀӀʁɫʱ9Țϊ҈ǚ˄ˇ·!ϸĐȽ',
                            'ӑźʖɅŐ˺ĂѶǵЂѫυ$αʒцԓ҈ԬƒҜԅӵώŃʲǯåuû',
                            'Ŏϖс;χТø ŔȲѫĞˏ}ɺĺΏ¢ȫЂϫӺ\u0382ӳ\x97żñҙƈȠ',
                            'Ǟ˞ԜǋѴɸ˗Éѽ˔ԬӅǠԐНȑ΄ʛͲԖȥд¦ȼ+ӝťŶ˩2',
                            'ҷоÞӟЅǨδӫѝѦ8ȸӚʓбҗЕѾȚʲØϩƋ¶ƞԡƆș˲č',
                        ],
                },
                {
                    'action': 'ӕƩԝʷӊДϒʪδǢԚҪ˺ѾЙ¿%ǹòӛĩ\x8b\u0383VȏǍßҫҌƐ',
                    'resources': [
                            'ƻʲӅ˅ѴĂŅĂʟΉʨҜϐ§żяÔҎ¦Ϥ¯˩ɺӿȏҀҼΨӉđ',
                            'ԍɀŗŉͿʷЂ/јʋɕ҇˞\xadãņȆŜьϒĿɔœɖ\x83«ęȝ*Ȥ',
                            'ąǳҲɸɎùúǋЧΗөȧѴ/ˮԆ\u0379ĵȌˍͳMҤǺf!ІĊÖԥ',
                            'ӀĜğ˓ŘҗԆÈκUǼ©Ȋ`кϊƜʫ\x9bďȀηØЋϝʿōӕǝƍ',
                            '¨ÙÚə΄˅ҥвҐű±ˋáϔ\x97щŗшȴĹМɖπŪǤѪɯўɠƦ',
                            'Ń\u038b˙\u0383өʰϾƇšϗԨϬÌíӆҴѮӷƭƗɷŪҪɹԢƎУlȘҵ',
                            'ˀǴԙҹщĬѡӇșԏԖťʑßĔԂς®Ӹә\x80ƪтƄ ӹ˚ãĽӝ',
                            'ºѺҮ_ҲŬB\x8bȀŢƆжѲȔ\u03a2ÆԎƢȬʘΒ`\u0383ƪЪԎ\x8aǘŚŌ',
                            'āЯӜÕ˝Ϝӓ˵ћĽĴɆȝŅY˅rǄѐȽĢȺԆǳøɜϿùΐɂ',
                            'ŻϜüӈƶ¿ÍƝЦúƯ`˜\u03a2Ѕɍę×ӮˠĎӱέ϶~˲ƹӧƿи',
                        ],
                },
                {
                    'action': 'ԑmƑ:ȣȱβ\x93ȖƾȣļŽ\x93ѻȣҏκ΅¿˘ʥƜgΎԩǝĹЃԘ',
                    'resources': [
                            'ЁӥƛåȭɗӋěӈҾɆΜӽ3Ƥ\x8cɡçӈ΄ɫˆηǦЈ\x81ӦϳgΘ',
                            'Xȓәη¹ļϓӹʯԍɋƶ.¬Ю9ϮŤ҅ŲˈЋʲāŨÞ\x86ˇІҙ',
                            'ЇԁдȿȀ˦όKȲѰàùʒíƍǗЦӄƎC ôÒġşӶӢϺþǹ',
                            'ƌ\x92ʻԂϾЄӅÁõϓπˬɌǯĎ¦ɩ,\x9fŮπсЁĔȡɍϮќŋ§',
                            'ɏŦ\x94ʰO\x9eҊҀĭҮƯ·ɥ÷ӹѾΈƙgόЄWĚ\x90Wґϱ˴Şɔ',
                            'ӬɴӽҮȯΧҷ\x92Ⱥɐēķɼł1ƯȲÌōɪΜƒĶώĤ¢Îʋʸΐ',
                            'ȾӊǙԗìЉɃˢƚĜ0ȳțƽØ!ÂZɖ\u0380ӭԅҍщŦ ωʊxʪ',
                            'ӆȸ\x92%ȷϬԧʇΛǞǗЛҴqԟȘʅɐϊòɓƟɦƼ\x90ԍίϪΒĮ',
                            "'ǺƮoҺĳΜέԝȯ϶ŭʦ¨ԬɄȗ*ǳŻƬī˴εŉoэϚԨɇ",
                            'ΫČíԁ\x8cѻӌΖӒȻšµǝőљŁĀʝȣɪӭɉĀȀԄưƞ˽ӸÖ',
                        ],
                },
                {
                    'action': '͵ҐxʜԧБʏҠǞĊaǣȤ\u0379ʄżķĀЊȡvƃéʴΠǹȏUЉϣ',
                    'resources': [
                            "ҠԩʚŗÊ'ȵ¨aã˘Ű ±KĨɂƥ¨ΰýъǧɂΥÓŜϡɁr",
                            'ӛӉӺƳwЕͺưΧϝƆ˕u˞ǆǌԇƵĳџЃѿơϰ!\x82ʕ\x8dňÉ',
                            "\x7fТ΅γ'tĄѝѯœPϬŘͳӥȮƼ_ȪҘ҃ʄԨϵƾŅѹɬҾӗ",
                            '˞ɏŏǜӊӚжƷƐm\x9b\u0379ΥԧЗƥïȺǮԉɥƦЭШ;ʌƠΏȐы',
                            'ѹȠȣΕΣóҥˁϭΦĳԧ·üМҮIˌā÷ˎǔȢϝƑҍʹҨѿү',
                            'ϤєǫʚΖ˜ɝҿ>©ёԐ6ʇ΄Ȍ³»ƆŇƳϢБȝÆРĀʹɜŋ',
                            "ά҂ԔͱËëԒɫöɓǼõÖʩÉ-ƔОÑэūҎ)ŗ\u0382ЫʪƧ'ȵ",
                            'ύɗǬүȬ!_ΓŤʹʦ˚ӫΊϜЃΰ҈ȎІȇΞҙĖ\x96ӱЫɿǿđ',
                            '\x8bо҄ǙԨǷǧʼςRҽĕ%ǥԐt¥їκӻɴãϠλDǬζ\x85ɣā',
                            'ʅҙЄĲ˰uŠӗĳâƗƻѫ˽?ҽίõΔ4ʉԣʝƐʟȂƋʢǅϏ',
                        ],
                },
                {
                    'action': 'ǈǋØˉš]ЉҖϊуԚĸöҨм\x9fĜÑӾίºεǙÊʀԅӉԉɭӕ',
                    'resources': [
                            '\x8dɰǹѶӧϾ˩ЪѫϘәԮЌȌȫkgҾĞҕЩɢȂ3Ƙϩεʐĩԑ',
                            'tǗȓсɳ1бƑнҫŨξȧҵФʀɰǯЌ͵ΟӫÓӅŖЮӖbƃә',
                            'ӕҬѷĤőӥя\u038bƚЀҵǇҘʉϫ´ȃӉʟǔƌ«ǣΉӜǎҨɻΙ$',
                            ']ЭȒʨ',
                            'ĖƐӵīΩĹЄ\u0380ǡԚ˭ƾҳƭ҇ѹî˃íȱȒΥʧҽŋѳ;πȿǡ',
                            '9ˀйҍȎćɃѽɤάȨȵϛ¹ÞD˃°ѹîƷǼδřӪΑд3þӘ',
                            'ѸȫƫҌȑɧʅ«ʹĺҷΓΈɄ҆ƨˇȜѵlɿҝшˋѦУ¥µХʴ',
                            'ӻЬuƃțǬʄɉłɬĤԭϝĖϱgŸˑȡӞ~˹Ƀ\x86FǭэʡʪƑ',
                            '˹ѣŲϪƷ\x86I·ѐƊѿʀԏӪȷʀǁNȔњȊϩӔҀ\\ɋjΔǼF',
                            'ӯĿѠͺǻƢÍГ˒ıÄȣ-ĤӠȴŝę³ɞΑњÏµ҉Àçwыɫ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʢǌǥ',

            'version': [
                -7818277357290402176,
                -7888936706025036004,
                -945123193541212463,
            ],

            'location': [
                'ɇ',
            ],

            'runtime': 'ǽ',

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
            'name': 'é¿ΞƤг\x84ӹ(sżȻЇȁçǋ©ΉЁ¼t˰ΔϬ\x86҅\x8eМōѹŌ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Юɭφ',

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
            '$': 'NώʺƍӴȿʪʳ«ȍһ=ѤˑθϻҟϵÕϺҵѶԜƉιaǜұӃȜ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -5372488901565855168,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 488976.3822476239,
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
            '$': '20210209:222851.909010:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ҡϜȍӅӒțйТÍƵԮí]\x8bњϪ/˦ŸİēƸǕ§OӳğˏŲθ',
                'vЉϫџ˒˩Wϓ9ӦȴϤѼĽ|#МýЛ\x9câđ˦ѱʹΤԆďΓ©',
                'ҟøǭġɽʽӡµѦΛǝǝȣɝͱъưǪ7\x9fÄˊ˜χɷӼ˖fӑǐ',
                "Оʧ]MӝҬϖb'˂Ŕ'ʏϲΎгð6Ȟ˗aϡÞʦϤ˦aXԙá",
                'ƱφȆϹ¬ůýԜÐ˟ľɣȒ9ΜšʤƊ`ɑΫɟɠǎ¶ЯŨ;ѐɴ',
                'Ϟˎα\x97ǊǤȴæųTόԏÝӕυǡǕѪˉԐϢѤʌϪҡĜϫȷ@Ś',
                'Йȡ˥QâƕȸïӡЄɒʹ(ŞΪɒяʄчȕıδȞϏОҞЃƹı\x91',
                'ԎȢчƬ°ŵ˭Ϟ˳ϹԎӵƑŏΏЃʘ΄Ä҅ȩµǴʀӮɘǊɗ\xa0Ț',
                'ƝҵЊȄсòÆŮ˒ŕʇһССSԃ¼э˜ĴD\u0383ϼĄ\u03a2҈Ȝģ:Ϭ',
                'ϪċŴԞßğԉE˵яθǮvʋӁѥóЈӲŇ\x89Ϊ7˜ӈӷIʴƈ(',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -4192562252248165704,
                -1708600521597886448,
                -2243454916408543497,
                4544858081073171617,
                -9142509684442285127,
                5971261278172556786,
                146566075918329210,
                -4828694382142892837,
                1503332319574451287,
                -7609164098438827331,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                248060.45580410148,
                342951.244626529,
                121333.44690942814,
                654060.7079482084,
                192963.6629236868,
                -69579.4168604021,
                195280.18286970654,
                614257.8277898047,
                625388.8598391834,
                834835.7471199924,
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
                False,
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
                '20210209:222851.910539:+0000',
                '20210209:222851.910581:+0000',
                '20210209:222851.910602:+0000',
                '20210209:222851.910622:+0000',
                '20210209:222851.910635:+0000',
                '20210209:222851.910649:+0000',
                '20210209:222851.910666:+0000',
                '20210209:222851.910684:+0000',
                '20210209:222851.910701:+0000',
                '20210209:222851.910719:+0000',
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
            'name': 'Ϛģ˪ы',
            'value': {
                '^': 'int_list',
                '$': [
                    1459283167838869855,
                    5714206857228871864,
                    3595680357664935520,
                    777198191657727064,
                    8031700180072076314,
                    5871138912882137017,
                    5002432912706859353,
                    -7099555397070596304,
                    -679043318612314233,
                    5805810903443745659,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʜ',

            'value': {
                '^': 'int',
                '$': -895902030370487499,
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
            'catalog': '\x82ƆϤЈ\x80όѿȻλƫŢȑȰÔË¯ǉϿżǎыПǶɚêćŏѧѴ˛',
            'message': '˷aԙĐ?˒ĻСwҬÃͰΐğǺΩϭƶ˝ʢļΈȢİ%ԞɆĤØӀ',
            'arguments': [
                {
                    'name': 'ӌRƵΐξԂҺȯÆҀLτ˟ʃΏͶϦ"ҥѹР˶Ϭ\x88ƫüӍøϮŸ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210209:222851.905535:+0000',
                                        '20210209:222851.905565:+0000',
                                        '20210209:222851.905573:+0000',
                                        '20210209:222851.905580:+0000',
                                        '20210209:222851.905586:+0000',
                                        '20210209:222851.905592:+0000',
                                        '20210209:222851.905598:+0000',
                                        '20210209:222851.905604:+0000',
                                        '20210209:222851.905610:+0000',
                                        '20210209:222851.905616:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ӭύȔρϜʽƉQͻüϛґȎ1ʆɒН\x9aƫϢɯҡƏИиʸ\x7f',
                    'value': {
                            '^': 'datetime',
                            '$': '20210209:222851.905863:+0000',
                        },
                },
                {
                    'name': 'ɎɧɵҲƽӺхӻҰњþ˹ǣΟȿНҺmϻćɌŜӶЅ§ȋӪǵϡѣ',
                    'value': {
                            '^': 'string',
                            '$': 'ĪɼѣĜʛÄœҧίŶͺșʥȦ˛ȄВÂԬϋӿηӠïыÔϫ˘§м',
                        },
                },
                {
                    'name': 'ԇÁ^ȼҭǢȡȶѼʟҞďýĉƂʝшХȕǘʙ΄Ȱѐ0ĚԢΙ\u0379Ď',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ðGYҠʠćƋñӈ˙(Шj˦ΡŊԗȡάǽԮǹ:Υ˟ˊǰѲǚ\x9b',
                                        'ÝϐЎҷŽ«ǥǲϫºʗɘɄΥԡȫάŝ~ŐдДʘʖĺɜÜΎғ\u038d',
                                        'ԏș˥ųƻʱÜѼȧӹ҂ÏŢ#ȺõҽȌƿˀӋʮψʟϷbdƖ¥Ы',
                                        'ӏǒʌҖЫɣǄÁȓƴÃDǙΕǊϟӉʙΗѯŦ˧ʶͰ<mŊɞ¬ɤ',
                                        'Ű\x7fτҀԆáäϑɭ˃ѾϱϷRŘѰǪŻʌϚǫ˗~ÑȠÛĭƉƪЀ',
                                        'ǠьǣψʗΏЧĨ\x9cʖýƏХҳРΨʽΜϺͺѳǧɆӈʴ\x96ǒǖɱѥ',
                                        'oìǍƘƁӕЭƐԟūǎˆͲѝӴɯϾУɍȗұǤǼӗ\u038dãĔɐўɺ',
                                        'ŴƎӻӒ҄Ƃ\x9eĲţėǿɮ\x8cкӖӛOӢӍˍϸäË҇7˅ϷɢƑ҉',
                                        'Ē2KØ҉U¦ͺʩԦ˭ǝÄʾδӄʋŤϬέʃ0ʐ2ǔōǮʘųБ',
                                        'ːŖʔȕŮͿÍӳӇŐǳ/ŪҌÁϹìҘǋӠЏ\xa0ĐǆӒȭʗ\x96Ųƥ',
                                    ],
                        },
                },
                {
                    'name': ',ƣăñÕűµІӭэ\x9cĭì¹ØҥUϻţʅԇ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        5261826808328749950,
                                        8817862117731159503,
                                        -6784649684597937178,
                                        8866822416940410120,
                                        -983651805310705619,
                                        -8373945339798267324,
                                        -7607525906163461046,
                                        -6324155709354276503,
                                        -7834718524001702923,
                                        -5208043033205105124,
                                    ],
                        },
                },
                {
                    'name': 'ƏZͽ(ȂɅšȥ<ȤςʴҚϣщ#ĔЎƤУҀҽԔĂȋʂD˰γϘ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210209:222851.906917:+0000',
                        },
                },
                {
                    'name': 'ӦŔ~ɢhΒɣЩɾЀ\x97ӤЪJɗмҝжĢνϒбtÐοѺ³˪ΝԬ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'PѪʃʖΖΙˣԃӰɞ\x97ϓϗԙрʯƩæЭɲҍ˷ʆü˜ɐԇϒƾń',
                                        'еӠефѷȫЀˆѤvˤɫȒϷԜєӲҤ¡ԝɡ\x88ЉêӲʭΫ˄вȴ',
                                        'М\x98ķԈ\x90ĈΌ¦˫ŐѤҏʰШ\x85Ѵ\xad҈ёďÞČԐĻĻ˙ʞəѰ1',
                                        'ëϾʪʍүҚӈNƻώʫɄҎȺ҅,R\u0381Ȇ¶Ʀρüθɋ¢Țȇ\u0381ź',
                                        '²ǥʎϊ\x87¬ǪɕԂͽȝϓлŞґɻΤ\x80ɶԤϝđϚΒҷň ӆʩЫ',
                                        'ϖ\u038bԌŤǰѫϢӲʸɀѹŦԦƌ/ŅƈšƾšˎˣϮӏ%Ԡ.ɖũǢ',
                                        'ĄΨ;ҫåўâȂb.ѳʰķЂȳԣөRҐƍĄw©ɴƾԊ҈ƀƳү',
                                        'äƬа΅ĕΎѨ\u038b#ßǿƸːʖ˒ҧϻƄơųæœϦƫűʉśÊΖɵ',
                                        'ƦӷØ?ǤǻҩҟǪ¤ұǆɑÔӹśʓɚȭ)εӅЗʌbҋŊɼĥƷ',
                                        'ϕӚèЍӥMОɟҜеӼ˝ƀбԑӊcλɭЄαϯӔ˥ϖvēѯ(ˉ',
                                    ],
                        },
                },
                {
                    'name': 'šώĦǎӏν~ӅÿîŕǺ\u0379ɜÚтшÀ˶ϴѥ\x93ҬġʥŹ\x94Ƅǚѯ',
                    'value': {
                            '^': 'string',
                            '$': '˧ŐӎӜcȐűБϴξɪƉ*ǜӁ÷\u0378ƠɵFǄνͼƹǔѡŃˑϽŠ',
                        },
                },
                {
                    'name': 'ƦZ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'нҚŴʣԝ҆нпǣrҾƓŐ˓ʹƈÜųƐǄӲͺΆĴǡʾԎɰlȋ',
                                        '˽ĘŲc\x7fʅáіωˡԟĻąӅåӏ(±ƅgȌȜQƅƐӍ˶Мԙf',
                                        "ӑ˸ξԪ'ϺͺʐƣϹdȖԞԥԂΨңцǯřҋȌҀǌɻɑҩ΄Øʷ",
                                        'Ȯ˝Čȓ\x92ғǻ˔ͻю˹ӿɾѨʝ˽ªӭӄ\x94¥ЯfѰǵwϱ˯ϏȜ',
                                        'ΝиŪдŌʕ˖ǙæҝÃϰ¯ԫϭҮхҒʊѪԐĠΈЄ9ɼƂƠĪʛ',
                                        'ҌǕϛʭɚ\x9fҺ˺®ǯмПԨфƴŵԓҫΨȇӈmAĩřӽΙϦήď',
                                        '¨Ñ!҈ɋŠƎǦл¶ŜWûCˮ;)ԐϮĀȠŽ3ʿ\x93ѫ\x94ȸʊƺ',
                                        'ȍ¦ю˥ɷřӄŌ\x82ɉéʠǐЙǱӛЃґħɍΫǊԏԄʬúŀΞяȆ',
                                        'Ң¹ʸƚɾǜˉɢ"ƤѥGʥλ\x87żŧǝʲřNƤҙIʳ҃lϳȫѴ',
                                        'ǓdĂőҏĬ\u0380ǬǩAɼ͵ŐÕЦâ²ƝҊӹăғΣ?ʰ\x80T\x8aZγ',
                                    ],
                        },
                },
                {
                    'name': 'ȓе¶фƑŗɰșĂ\xa0HΚG(Ǒѓ\x99\x83Ȓ΅\x8dȻϕ~',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ȽˤԒĸί^ąϕɜ£ԟҎǨɍȿ\x9eї.\x9cɝʭʣϕÙͼΟpƸǁѫ',
                                        'ŒĘӬZƋӁЃưϵmZƷŋБıΞ\x8bÕý˃ȇɐəɱƾɍԌïŋǆ',
                                        '÷ʗʞĿÅќʶƆɠӃɜŻˁ˹пɡˑѰвJɸK˫4ъřҵ˽ШѠ',
                                        '³DΧĭúӥÍĤĹmҪϤšɓɉź3˽¡ĎљǩνЪнĦș˃ϿӉ',
                                        'vѺǡѹ҉ӓĐ{ơхѳɶ\x98ӡǗ2ϸýǺʾÒƋǱēԌѭ˾ɑǊN',
                                        '°Ԑ\x80йӧƥӠȔώӝhԗн;·΅ʉiԊ^кȱĘϋĽ҄Ҽ&ǰí',
                                        'ȇêɀjНϚęɭɸȔx#ʭʕµιīcМψ˨©Ƭʛвǆʞ9eǯ',
                                        'Φѫє¦ʷδ˝ІΖƙӇҾԐȄĕbƾҊ3ŷŎı¼ӸɅЗͰvӽǭ',
                                        'ėѲĤȾӱɅ\x80ʯӈУȩĞǿ˲ЄƱɟ<ƤǙΨʖǑЭҤǸ1ƫŲȨ',
                                        'ΔÃӰ\x85Ū\x90ҌϽÓ«ƛÌʧӿЃȋ"˒ҥ¢ĿŷƪʝҟˏƗ˞øȄ',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'tǥ',

            'message': 'ύ',

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
            'identifier': 'ȍZƨљΝϋӨĕñʅŒʲǙXÛԖÌԫӓԤÏ9ɴώȢòǌǼïǞ',
            'categories': [
                'configuration',
                'file',
                'network',
                'invalid-user-action',
                'file',
                'internal',
                'configuration',
                'access-restriction',
                'file',
                'access-restriction',
            ],
            'source': 'јČԟǐΊӴđɜЙΊȿkȮ˹сơЧЬǌԋëˢҝˢЋñǅǚƳɄ',
            'messages': [
                {
                    'catalog': 'ЖѰŻŃƨʭģп½ƭϬŜǣɣ',
                    'message': 'ӡ҆ҫ҅ʜ¹Ԡϵʱɳʴѽϧ˟ԆƽЉɦhѺԭķXȈêϣ\x98ϒԅ˨',
                    'arguments': [
                            {
                                        'name': 'řǃƃǴϟѪǩΙϱNʌҠӔӱ҅ˍͰӁŗҾёƝƤϣɟǒѧҾҡʷ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɡПѥȯŃȹήǾÄĢ\x9fϜӼѪ˱ș\x81ǧϘƆΜʀƾÏ(ȉɴϩʽɽ',
                                                                            'ųƂαǀƕϨҷʄ\xa0μʽȇ˝ЎĕѮƢɶ\x97ċӇѵͼτɾϰʑҖ҆Є',
                                                                            'лӍ£Ԭь˅ɋ^ѷΰYνʘȝσυȬǈ¸˥ДԪɽѓΫŲήʨʥɀ',
                                                                            'hƁΥӏί0ʆ˩ͰɄΤϢ˩ǰѻҙIɦвÆʑͲӞɨœñΞɦԈđ',
                                                                            'һȸĩm¾űѡʳͷJυүȡҷȡΌљ¶ǔʗІϘƎʂVɑӃŠәń',
                                                                            'ϰUʯȣɕϡ>\x96ǪǹȞԘԫЁҊüԑǶ\x8aͺɮȟЯӮîԭĜȍѐc',
                                                                            'ҖǺ&_ϑɷԏ4Ȟӣ¹ƲɇĆ˝ʴƸȽӲӂŞêɶЧӓ˩4œƃҌ',
                                                                            'ƾӁȜǷˎҐ?¬V%ɵǠЎ˒áφʠͱǾӀԨɢ?҉ɏˢ®Гʶȕ',
                                                                            'ǥɇОƃηгЫɨĴɌɤƞɉIԢҏҵǏз˻лѺ\xadʾǙȣȨζÉӹ',
                                                                            'ϴ˒әЮ˯*ňΏàжί£ІѯӤΔҘċԤѢ¡ϽɴɘɼаɱԖĖԏ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¬ԏʣˢʥȕČȋȚȵЄĚïШԫʀЎĨ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 98492.75569247329,
                                                    },
                                    },
                            {
                                        'name': '\xa0dŢǏѯīύӀŏњеċˇНӁaŋŤǐɋwтұҁϲūǞ¶Ҍσ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222851.868523:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʢԫÊƌӸ҈Ĭӳɹ8ƩԂԇµė˟À^ļМǭʖ\x8aîԇϧЁî',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'śĢν\u0379ѰǊʋŢƭ`ӴЭƆҗ«ΌҠГЅʭȲ«˱ƦȕɒҔΌȮό',
                                                                            'ХʇǪӄӘƵϹÐλŌϞɉɃф\x9dΨԀȴȟɰõǵɅȍϋӌ=πdˊ',
                                                                            'Ǣ¸ԭµˏӉΌŨđ˅ЌƣOǏԨ͵¥әìx\xa0ϫȡŪƙχрКԃԛ',
                                                                            'ɺәˢˣƟ!ԧȬԀ϶өФˌώʥŖƸЭ\x9a!҄ĴЊɛǩʇ \x8eǶ҃',
                                                                            'ŉƖúƸԟ˚ѵҜŲȰ҃ȟ\x9fÓɺƾȁЃʑ҆ζQü˻ͽǌɍнӗ-',
                                                                            'ΕѩтȾʣ®\x89ШǊ²ΐѹ¥rƭ˒\u0379ЖǵŦƸͼχɪδ"ĔӌÑϤ',
                                                                            '\u038dэ˅ӜȇĄŴɐп˺Ċȅ΅ͳËʟóàȔ˶ϗКĈȪƕǌϾǶЅȟ',
                                                                            'ɊΚТĳqЛАŉyƲ\u0379ʡǘˉˊãЃΗΑŐŤȚʱҦ˼ŸǄӿ˲ɚ',
                                                                            'ƸϖƨŀѹȩʌMǾԑϐʏÄśΛaƅϮж҄ԒеϙѭŪɫŋĮƚȂ',
                                                                            'ӘРƓϛНɰVĐćдѧĭoǎðљɆҤȋɹƜʐŒŘʕԦԂ˽Ƅҿ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˣɠΨʃǗӦˠłĺȏƴї/ЌɓʷǦɌҏƈȢK˳Ɛΰʾ¬Ѓå',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 844397.7438703883,
                                                    },
                                    },
                            {
                                        'name': 'Юҥ1йҗҎǅϻƥЭ<Ҽы°\u0379Ӓ,ƥˈ˺ıĸǊ\x99ſŐȴ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -52064.8430867942,
                                                    },
                                    },
                            {
                                        'name': 'ȃƛщǲо5êӘй>Ö\\"ҁː\x80ĉԩþӡǷɶ+Ĺ˂ʉĩнҵӄ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѻЋϮѺȦΜρƉƕŕǬƟˇȿˢҰ½őц×ä',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϧʇĩφǕÎӰ«ʛЮÀǡҽԨċRģäӱρXɌ\u0381ΟQï˃Jʐł',
                                                    },
                                    },
                            {
                                        'name': 'ĥ ʔ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 705436.8852042706,
                                                    },
                                    },
                            {
                                        'name': 'ѻӓϹλŠϚǢΨфӏʬ\x85ѧϑǅҺɱӁƖˇԒ\x87ԖҳӪŲEҶŏ\x9a',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɼϔÞ;ɩʚ¯)ħʒǔѬƖóƞĭƻѭɘϏāwοӮˡБуěӅФ',
                                                                            'ƧʩИԛWƗϼ³ӥҜ\\ŧͰʈá£_ƲǐƧɽƴìξ´˄ӎίҶɜ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ӷ Ѫ˲ɇ\u03a2ʩπДнJŔßȊӷȰȥŎԢǲҞο´0ǷɎҊĺǍ˓',
                    'message': 'ϫćǾŔνȮͱγ˴^ȺУŦ҄GΌȴ˨ȽĄЁƎґ\x86ˊƣ\u0378ǨшȻ',
                    'arguments': [
                            {
                                        'name': 'ɥԬς\x9cũƪh',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222851.871587:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƃðăɑОƑ˩ϙЧ±ΗCƕͼǉЦȒŠϋɄѥѵņD˛ÒтхӏƠ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8733653019297398245,
                                                    },
                                    },
                            {
                                        'name': '\x83ЇǑθ§ѫĭȂȠѵӥǐѸƹ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ĭȭǃ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222851.872662:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƋϊƃƩűɳǤβԠ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƴǳȼȣũĜԐӶǡêșULī\\řԎбӗƢϡǓöΐÌƐŨˇҹҡ',
                                                                            'Ğԃɸ˓Ѷ·ӑήɪI\x93εʸȋӸɳԌʥ.è\u0381ǥ§Ћ\x81ɯу¾Ҋπ',
                                                                            'ǣâ°ť\x7fȘЏʧʵ·\x92˲rŶġÈʗƆš¸łĹœdàԖҟãƇԏ',
                                                                            '\x80ʥǞɦӦŒȫíрˀѨŭЭњŮѷθªҴ¡\x9bϐԙĨвęºѐ·ɕ',
                                                                            'ѽ\x93Ƭǔԑʡɏʹˠ˝үƷßÛҬǇІ\x81R҈Ģǘʏ\x96ωϝҭû|\x7f',
                                                                            'һϰϘ«ѷ˗с\u038bѝ$õƞҕЊϳӟ˟ŮжЃF\u0378ѯξо¡ɳ°ЉУ',
                                                                            'AˡҸ˷ŗɄĺÙȈζ҈ʕЂ~˱ϦѧԟĉʞɦҢƟǼӁ˫γěΔą',
                                                                            'ӭʵēčǀƒOȃΊśȮ҃ƴƜʀǵϞЍŻūЀ\x88ÚġӬ\x82ϾΝɭĚ',
                                                                            'ӵtfҊЀě\x92ђ?\x9fηʃ!ҽҷ˶ǽΑLʅԘфԢЩ˽§ȿ\u0383ɤʘ',
                                                                            'ÈдҜΛĳŕԡ¿ԃҝǫƕϽґȏ¶½ǜ±Ò·ǱϯЊґΥëѢĕİ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÖζѱҊǑͿĀɃӴɪĿðȱýмЍªˉˁǒ+C҈ЭɌcͲʈ¶\x8c',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ΉΎŇWӠǻɹ×ԁ\u0379\u0379+ґӉӤĠŚͰɩѩӡȖȒȣПʍÍ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
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
                                        'name': 'ɺÒ\x93Й¸¢zØԣƸ˸΄ʜƩΝ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ōЍŸ\x95ӑЃҸƢΏѳü΅˖êčǅȳȰ\x8c˘īŭθoɛҢɿГɑʤ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            635591.628215588,
                                                                            195817.34419138276,
                                                                            877041.2014301124,
                                                                            898223.2757018101,
                                                                            117282.07209761252,
                                                                            985129.3980425689,
                                                                            646395.076664293,
                                                                            564556.6130990615,
                                                                            556250.1170499931,
                                                                            711179.3568803363,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȪЃĹѓŵƉΚԏ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222851.874066:+0000',
                                                                            '20210209:222851.874083:+0000',
                                                                            '20210209:222851.874091:+0000',
                                                                            '20210209:222851.874098:+0000',
                                                                            '20210209:222851.874105:+0000',
                                                                            '20210209:222851.874111:+0000',
                                                                            '20210209:222851.874117:+0000',
                                                                            '20210209:222851.874123:+0000',
                                                                            '20210209:222851.874129:+0000',
                                                                            '20210209:222851.874135:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Чȕśĉɳƅ˛ϫѹȠйҌɳ҇Ȋy\x93Ͱz˵ƍьҦӝҢŴȉʫɎӁ',
                    'message': 'DВ\u0383ȑӲӁŭ²˳ȗѢVԮԚŃƍ!ʙÿϖʇЗ҆ӹ°үȨōԣҸ',
                    'arguments': [
                            {
                                        'name': 'ŉʀơ·҈ʟċŇ´ʄѴȢUΪÀԓ',
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
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȩ°˷_Эϣ͵Åȟ҈˻ǕŬNΪʧYƎGĄŦĘ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ώ˛ŭдʂӃ[ŶˆӅЊƝҽƧɦ¢[ō˭˂ſŦǏ˸εUϭќƍǊ',
                                                    },
                                    },
                            {
                                        'name': '_ûҽԝǳϐȰή',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˧ʍκÖ΅ьԜƽŵȊԙѶàˡԪͼΞфƪΫνИƚӞ2\x82҃»Ĭɚ',
                                                    },
                                    },
                            {
                                        'name': 'ÂÇʅnÐ«cαӿϙáŵƱ+ѕϸȝʀW6ʌΠːǟʷɍԜxОˉ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222851.875195:+0000',
                                                                            '20210209:222851.875209:+0000',
                                                                            '20210209:222851.875265:+0000',
                                                                            '20210209:222851.875272:+0000',
                                                                            '20210209:222851.875279:+0000',
                                                                            '20210209:222851.875285:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'fʜƌ°5_ԎӯҷͷΥѹ\x86Вщʾ\x95ӌѠΒїѕτԓË҆Ò®Ǎˁ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1901360075077866574,
                                                    },
                                    },
                            {
                                        'name': 'Ό˧\x8cʘƲĈɥӴϯȳҮЂȨǯ˕ӘÅþѢŠǃШɟĔѾǸƶҥӂҙ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4551534165043406204,
                                                    },
                                    },
                            {
                                        'name': 'ØïΤɂʆ\x9cǅ4ʅ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222851.875851:+0000',
                                                                            '20210209:222851.875866:+0000',
                                                                            '20210209:222851.875874:+0000',
                                                                            '20210209:222851.875881:+0000',
                                                                            '20210209:222851.875887:+0000',
                                                                            '20210209:222851.875893:+0000',
                                                                            '20210209:222851.875900:+0000',
                                                                            '20210209:222851.875906:+0000',
                                                                            '20210209:222851.875912:+0000',
                                                                            '20210209:222851.875918:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ČЙкϪ\x8aȶIƓԔ/чǩЇӋ˺ɠϟˤҐгŚϜέgA@\u038bȉȩ$',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '϶ВɆȣ¹Ĉːԁɤâу_ΞǮƼƢƿˢĠƔŜ\x8aЬMʨìϾȹÙȸ',
                                                                            '˻ϝΖ˄¶ɜӘσΙӐƙӂɵǓŮfӅ\x8cєѵǺƉж\u0379ϋЍ˄9"ӝ',
                                                                            'ͶԙBσ~¸wˌçŴɪƙΫһȵă˄őÂӰˇp\x85u7ǄËɸˠǗ',
                                                                            'ˤňM΄кΜpǒʁɺȱϵ6Ŷә˄ЦҚМ\u038bҹщ^ѝԔԔȱɏ\xadö',
                                                                            'ϯьɮˍјćζĳˎӣ\u0381˝zҢJ˷šκԈ\x9aН҃ɟёĜɴӿпfԇ',
                                                                            'ɭÍˈÃ;χ˭ҳƵEÄŢ+˔ŎрƉʳѷpѾț9ӷWӢѡˋĕq',
                                                                            'ӶʚзƆϞο\x7fγӷǈŃѾżúŕԤ¨ʪӡЕӅӁҶнϒάƘ¼Ι\x9d',
                                                                            'ϒŻΝľgƍ˛ƼˑҹǰsĈƲźǅǌѫʰƞèöϥӮά˩ċҌȰ\x83',
                                                                            'ǩjϢľn¤ǲ˄ҀÒXɘ҄ѳǬҔѓôÝYȵҽЌԣлʪδôГɱ',
                                                                            'ūƓÝ!\x89ѯϏǄ\x82ҮęʨźěɏȽɣ˂ʽƶ\x99ƕӞαѥԡŔcʩԣ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȢģλĎԩѽîL',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -514672824767848776,
                                                                            1330898255740248837,
                                                                            9208301736661032545,
                                                                            -344687800022663001,
                                                                            -2552525060765383362,
                                                                            -8968953027598993703,
                                                                            -4235180672041395087,
                                                                            -9110025496933247594,
                                                                            3873225656529604147,
                                                                            -4874067031894340727,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҇ţɢф',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8020750119791163467,
                                                                            -8215895130074379840,
                                                                            5927375219192140723,
                                                                            2361229650425627606,
                                                                            -6935822990636590642,
                                                                            1521990245398482595,
                                                                            -7574915943719021421,
                                                                            -1688442195245020278,
                                                                            -327483050015237587,
                                                                            6663443973569161473,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "ǙƗÞȴ¾ɬEԪӆKĒˣɎҔ'@ѢЂͲʇɚ^ϝäʇňѳˇΧУ",
                    'message': 'QљǶǠҫˡӫĤφąԍҤyѣǂmva>˄=CщёȌϊžѰЫύ',
                    'arguments': [
                            {
                                        'name': 'ſC\x94ùʃŚԬtсѣʏƐҦҵА\x99ʋϾʶˢɔDҀ\x8eʾӮ˾ʺӵǿ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'јԝлóïŨʃĀǬѹüɽǁӁǣʰѷɽѠȧŜƭʄʕȕȹӗεĖW',
                                                                            '΄ïæʒƲȹĒ\x9eδĽкǹʯтЖѫįʾĞǸџϠ\xa0ӜЌĐʬĔ\x97ӑ',
                                                                            'ӣцƀò\x9eУƌ£ԮʟkʤLʪʬρΆϬ=ԥѿΓЏѠȫΡ*ȗñˉ',
                                                                            'ԃ˺bGƪЃɻ҇ȍҹͻƑԪϏ\x83ʉωƖȦҌǛļәёÈуѵƫ{\x95',
                                                                            'Ѕƌʓò\x97ӃŲʧΩĿϬȈѵ\x97Ӥȕ˺ƍщ\x97è˖ΛѱԘȨȓӒГų',
                                                                            '͵ӡ«ҎƧĸΘ%͵ΩΠɇԧ҉љîўϣҧΎӮ¨^ǸΊөҞςѥЦ',
                                                                            'ҡǸǛʔϼȸ{ėӂʼʼ\x99PӤ*νȎÖʏǶԌЄə˯cƽѰ\x90в˞',
                                                                            'ãѻÞɥсъѐčͿǷłŅǺȎĿǞƚҶ΅Üɒӟ˫϶ɔҊƓҘϯ¿',
                                                                            'Зˋ˧Ȣѭ!vǆӭ#ŽӹȿɀǋϷ½άˬϷѦ˃ơűЯ\x88wĝ\x8eʪ',
                                                                            'ɈӮāǁʦΡδȅˀ$¾˝˥ɾǗϧӁɯҸЮԇҠҁĘ[üÎǰςȷ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˞щҪiɘ)ηʉЬƓ˺ƅȧәÕҪ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȉҺԕĀìϔЂӔɶiī˺ϏΙ;ŐΖʣǣѲƜĲҒĚ]ϖüЌĢ¼',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1711758809474809832,
                                                                            7008275390316915203,
                                                                            -5497197533322543101,
                                                                            2506144875970592848,
                                                                            3559062219817992762,
                                                                            7125334240418309709,
                                                                            -3444641369553859486,
                                                                            1241689076217936198,
                                                                            -812827544815453104,
                                                                            -5891807581118716326,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Я',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʆÃͿĖŅυрǪʾʮ\u0380ΡĦЯΫўƑǹ*е҉Ƹқ´ҠȧƆǪƐ˗',
                                                    },
                                    },
                            {
                                        'name': 'ϣӓʟԆϼšȸʠŶʦέťӮ˃`ÀџHŻēʹǭнŷ¶ʃˍŘ҅',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222851.879191:+0000',
                                                                            '20210209:222851.879236:+0000',
                                                                            '20210209:222851.879257:+0000',
                                                                            '20210209:222851.879277:+0000',
                                                                            '20210209:222851.879292:+0000',
                                                                            '20210209:222851.879315:+0000',
                                                                            '20210209:222851.879333:+0000',
                                                                            '20210209:222851.879351:+0000',
                                                                            '20210209:222851.879367:+0000',
                                                                            '20210209:222851.879385:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϰēŸҼGʮΆԮ˵Ǟp·ɠĤ˒ʙˇ×Еɣ)\u0379sʳ\x85ʻƛƝѽӺ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӕ˱ʞÊɰ;\u0381wŧȀϳґȕӦƛʇũ\u03a2˕ʈГ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 391756.6757130294,
                                                    },
                                    },
                            {
                                        'name': 'ҶΛΥ\u0381ʧǕÝJƻÓİɲĦʁšʂЉӅϛƒɓĔЯԍɍȷ˃ǹϬӖ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŕƙԢ%˙ʄŻ¾ɂͺҙìÒŹÏұπҚНɺˢʶ\x86äŉƋÀȓИӬ',
                                                                            'ʝɶòεmɣǺ˚ʴѩфбӡΆnӋǠȿ¥\x97ϵlϬɠѾǑ¬ϨҋŪ',
                                                                            "őOѾçƲˢϬǛΐ]ÛӧɼΊҾњѺf'ɎȥҎâӂÉȪНĔԭ˛",
                                                                            'ӎʡԊǎќŜ˰j˽ʈψȈɝʷȩѪűǊӦ¬IɊњʜıʈȡӲƪԀ',
                                                                            'ɔԁżȤ·˪ƘƇˌȑ]ȪɼɿѨɴ\x85&ѮэɒùυψʩđˮԞίΈ',
                                                                            '˸ΊѤϜȢԋһФ.ηʘҦф˅ī˟œΛъЧʷɼԜ\x93ŒϷÀԂhю',
                                                                            '\x8fџиŕ°҂ÖП˃ʒΧλԈɓ˄ʘєɺϕӰ˪ɆĴšſѻОЗЦ[',
                                                                            'ƶΌєʜPƔӱȗԃАŉ0ұԠƻҠɹ\\ǲDΩ8ʵϠϜlɂʧ˕Њ',
                                                                            'YĥѪʶз\x9eҞэǵӖέơR%ȧыԫӵ[˻ԀȢŀҗ:ԖȏėӤӉ',
                                                                            'Ŏ^Ǜw\x7fТ«~ǸˇɋȑГˋɥҩӡǄƾÜьǨǊѤӲʌΚʭӞŋ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʹʥˁÎϫӑÒţQϳϥÙłиϪλȁЎȸԬǴ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʗʚνЀҜ3ŰӷôŎƸ΅Ņǈš²\x90ϟɻŎlжӖPΣ˂ČЯµ»',
                                                    },
                                    },
                            {
                                        'name': 'TϥͻӜԠϤѨΤӏϩѐȭ¶>ħϣρ͵ԒѧҿɐĢԜÂ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1940074914219514243,
                                                                            -4725899579613053413,
                                                                            7128019846402315652,
                                                                            3717004809261911623,
                                                                            -1771010122139423149,
                                                                            -5253386574736782049,
                                                                            7049200239447472691,
                                                                            6656237204993980726,
                                                                            -6965137266244648140,
                                                                            6159368656234544526,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Шȱ9ļÙƙȔ+ǒҗԚɉǆõʥʽƘΠɧӗ¦ƤҼśìǔƘ˻шғ',
                    'message': 'ǖɏ˓Ϊ˥ȰqԞƸơĹͽ°ȬмǧˢȐ\x8f˭oԄήϪҳӻҦ¨Ңň',
                    'arguments': [
                            {
                                        'name': '˦ӂǛØɐàѣКΰķ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɤDӀϹώęԅԃ¥БĜӳ§ÉęÍŴΎ\x88ҬÛϣӏө˷\x8dƜԋԞч',
                                                                            'ΑϥɺͷΒʭАӰƏţƧϋóǾѱȧǕäоϾӞ˺ˍȒӧΡˠĊ£ł',
                                                                            'ҌӺӦ1ÿ\x9aҡʻҒʄ˕ʐƋԅºӤƐǠʼϒĚЈɕҟοоłƸʆĆ',
                                                                            'őŕԌҴμ˪ȷãϒeԪҤǵϬ\x87ιѫˣ\x8fҲЕȶȻНҲĥșҡѪy',
                                                                            'иƦЈП3lˑȎӫʼЯήΗɞԩҡƿԮśеЧˋҫʐǼȈϏđѐ¸',
                                                                            'Ьџ˖ΉӴЮjł.ɖɫ\x84ɨūҷØþӊ[ȶүϘȿӢǷȉӔ˅ӻV',
                                                                            '\u0380Ԍɱƣëϯʪ\x8et¼ԃŸķɆiüϘœɚӆZˈкЂдʄȄʧ͵ĳ',
                                                                            'һtΕ˔ʑӋδѮѵ˸Ņ\xa0ßɕТˠУɃɃҝʘ˱AӸнáԟŭ˄Ť',
                                                                            'ú҇dѣĸƝ´ѮʒƕsɔȠϖҿγś\u0380ȋŉԫΰʢυ!Œԩ3çт',
                                                                            'ǇȠº\x97Ȁʳ\x99ϓЄσ½Ʉ˔ӌɮĿjƑċĮѿЛÍ7ԇͱԣʢȝİ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЀρӃȾeˮƥϏËІѐӯ˞˥ĮȖ½ĭː',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222851.882262:+0000',
                                                    },
                                    },
                            {
                                        'name': '&Ɯ˃\xad\x7f˓κ¢0ˣĞѬŞȞӨǎŨȺԉƇôϲ¯ιĥđ0ʘɬ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222851.882420:+0000',
                                                    },
                                    },
                            {
                                        'name': '9ѭ\x93δҟІԠÔʧ˨тÜƹөΏťƁѰΉϋǴȘɛλø˕;YŰҮ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 856202.1506132778,
                                                    },
                                    },
                            {
                                        'name': 'ң˾ÉśεӋáˀ8\xad²Ƕœ\x83ҔāȱŬЯϠĮϝеɟćΞӹǛ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŉΣŮυʻҧ¶\u038bȤ\x88ǾɂΧԤКҖɩřźʌ\x8dǌɑǕƵ˽iưӎέ',
                                                    },
                                    },
                            {
                                        'name': 'γčʱ҂ϸȇӵҙҪӿҥɼҲǿϹôʚ˯Д\x97DɦӃƚѹ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1009498059747672029,
                                                    },
                                    },
                            {
                                        'name': 'Ćʥϡ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 190106.4514150013,
                                                    },
                                    },
                            {
                                        'name': 'ϢӂϠΟυɳϙˊžΊŁΈǂ˂ӂчlùѓ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -4633.007605144361,
                                                    },
                                    },
                            {
                                        'name': 'ʡұϯΗɻuÆƓűɱǑɛӆƞȺĈśѿyɫÌ\u038dɛΩϊӯŬŦӴʇ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3228517017988638801,
                                                                            -569808073605893307,
                                                                            6168345410121377926,
                                                                            3467894173458362166,
                                                                            -272311829421770925,
                                                                            -6128941004143176832,
                                                                            -379808082736101145,
                                                                            5674925001882296969,
                                                                            -6200565169634313725,
                                                                            -5639840686103757696,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϼЁƽÝͱǃӎ\u0380ľҝǤɰіĂ҉§ѠďʴuƁ4\x9fŏҗdȳ\x90ʺÏ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ķЂɤҦѻϟĮЧƁΧКɝ\x8eŢϓɝƀсŶʪɄϋHƊҹЍӆЧЁӈ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȬȘϲý1\x99ҤαǜʘΗǼ·ӓӔ[ɭэΎðɟɥģBGӌ;ǍÇ\u0382',
                    'message': '\x8eЧʪ˾YңŚȀʙͳƇɴӷɯ˱ʐГÁǡ\u0379ǜԝ§ќɜũ˗ˍ\u0380λ',
                    'arguments': [
                            {
                                        'name': '\u038dщϐиӘŦƣźƁ¾ȳ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4926673472512640124,
                                                                            3033126297977422187,
                                                                            -8487821241789314208,
                                                                            4699745886414011051,
                                                                            -6152351615559092382,
                                                                            -2783128408029959601,
                                                                            -7464351825666155922,
                                                                            -4452514418992183840,
                                                                            -6276394020403331144,
                                                                            7108838096411989078,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʞʥēŠлěΞӀǿƃʏƽ˧ĶӮ\\ėĖȸжˆǻʈġÒ҉ͻȝȑ`',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ə˃ɟԔц;Ӫː˘ϒȭҒ҃ͶDÕёÛ\x98˚ưѮþĶʡǖĊɀεη',
                                                                            'Ӈ\x82ȉmҾĂӗǦԤáǦoԊÞʹƤѥԞÊҨӺϋМȓȧʜɥɺӾɍ',
                                                                            'Ϡȩź¯˚ƾԣ˱\x97ϫ#Ԭŀˈ=ӭόѲҡɈ*ω`ӋҚ˱¿Ғ˨Ɗ',
                                                                            'ȭяɀȒRԈУ˥ɫӵ¼ˣϛƃƧʫХΌɪȽ\xa0ì!ϗųқЫĶԒϬ',
                                                                            'Û\x80Ҡ¨Ү˝ŷҾĵĊɅЋϢфWӡΓԦӚӲʞвʙҢӐčǃһʔ\x9b',
                                                                            'Ї{Ӽ±ĪԋǰȰř˜Ѻèúҁʃӑ\\ѤӏƗ\x8dſѾǬ×ĚƎӕӤĿ',
                                                                            'Đ#aӨVνч˻ƱDΟӈͶū¾΅ЎΗʎʃåӈԪɵȗ\x93ƺǡƨѓ',
                                                                            'ǱӸĚԥ\x87ƢŃJμ˛îΒfιϗӯŴѣ5=ƫ)ű\x9eӍσĝ˴˩\x83',
                                                                            'æ˳Ӥ˺ʮ:Ǧ£ǃȒŝmɹğ\u0383ĂȺҗ=ԚȮӴ˸˓ϷȋͶ˨˄\x9d',
                                                                            'ĸМ˜οͲ9|ӛŘȘà\x9dƐŘǚҗΕϼ\u0379˲ϘƯŖ~\x93ӗǡ¿ѰȾ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÌӉÁǋ5ӄԇѲˡʊǷџѴɂȽԨȺǠˊť',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            309164.9572782069,
                                                                            255011.2129146061,
                                                                            682047.6183222932,
                                                                            17635.07301571846,
                                                                            392822.54567400937,
                                                                            139240.09664965596,
                                                                            435030.9341131778,
                                                                            287906.01907465624,
                                                                            65163.79580699396,
                                                                            634846.6653461133,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԝϛӮӵǹΏƾʒVųg΄ʃīӾ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3388591805130465130,
                                                                            -8476225482421537536,
                                                                            -4525839408814871393,
                                                                            3744221931815472832,
                                                                            -2150420370060425066,
                                                                            5663451556367896498,
                                                                            -3216124101915729521,
                                                                            -1784238986235083501,
                                                                            -1615640833259944721,
                                                                            -2730050549687537088,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǭQѲŀȣӹԙŷЄҠȏΊÎµАѶ{',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -492472541597899416,
                                                    },
                                    },
                            {
                                        'name': 'ɚłытӕςȆƏԇȧŏȬʨЉŁӟ\x9cΔȺƏϥΧSӬǑыȚСƐĠ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'џϘóΊƟå¼μ˃¡ť˽ˏAŶ~ϜƯԝ²\x99ӅΆӉʖϸʕΐӵǩ',
                                                                            'ӜˋǉҍІњӍʴȣ˘ʕɬ˚}ҏʱѴOĄ{ϱҚСɏòɆԊʑ0ĵ',
                                                                            'сͼɟǬԟşρɢЭőԐŌѲmЉШƮԚȰɟĈŔˠƸµʔɩȞġр',
                                                                            'η\u0383ιԔя˟ƘБȁnɢԌξĻԒƟѰ҅щǞĢĞʒCѦÕȂԂє\x82',
                                                                            'Þ˵ӰʵɧǅҔƘϝξɘƗɀń¿Ǻ\x9eȏƅ@˴gТaϷѐúÚȶҝ',
                                                                            '\x89ӗ˶\x95Ɵ°ȹ˛ԃ\x88҇ƱΐʗâȔ\x88mǪƢӵ¡ʠʘyυӱ®ԅĸ',
                                                                            'ѺԤŰԦΘӤ-ŧµųƍВˬɬ¸э\x9fʔO+ĐҝëɅӯӺγξɶɝ',
                                                                            'ˎ\x9eêʽȷҚϬэҽʓƥ|әӵƬĨʾψÇɦӍƫɷөӖǢæȢ\x8aë',
                                                                            'ΫԙÅ˦ӝҳӇ˥ԑŖů˹ìл\x9ftř\x87˝ԖǔӾɜ&ȋn˦ʲĩů',
                                                                            'ϘШΡąѣĊфJ\x80Шƿ˘іҭł%ȕʀǼǃԨŴíОϛ%ӓ"ˌΊ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѼķFΞơǴƚԘʅƖҴG',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4106846353462547145,
                                                    },
                                    },
                            {
                                        'name': 'ϳɢ,θοǂԐǧ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ҌŞɇ¢ř\\Μ˵',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2481772064920727394,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŢǷê6ďѝϖ¶҅˭Ѐű\x9dΛˣӥҿЅSɘͰ^ƃÙтŸУ˼д*',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
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
                        ],
                },
                {
                    'catalog': 'ЙͼƐxͺʣƪӔ˘đӨΕфҰƳӦѮȒƖӀŝϥΐЖɞʦϧΏȽŖ',
                    'message': 'ˤͳċѷñõњľǧ\x8bμԅ˯PԡѺҐũӚҜҫӵȵǖΐĵ˹ßӲӱ',
                    'arguments': [
                            {
                                        'name': 'ɦҡä˯ĠΖǴɒҹJȦĮБʏНUЗӷЫƏĳЩɉʐȟœǱѵǃb',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΆјϝĽ;ŽϖˎΘЄ#ԑѺʆЋ˸ƚäéΔϧȓ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222851.888902:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ӣ˳W»uǧȃɩü#εĒėǔʳψêś',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222851.889185:+0000',
                                                                            '20210209:222851.889212:+0000',
                                                                            '20210209:222851.889232:+0000',
                                                                            '20210209:222851.889250:+0000',
                                                                            '20210209:222851.889267:+0000',
                                                                            '20210209:222851.889285:+0000',
                                                                            '20210209:222851.889304:+0000',
                                                                            '20210209:222851.889321:+0000',
                                                                            '20210209:222851.889339:+0000',
                                                                            '20210209:222851.889357:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȸғ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'śԈȑѝĞӼΆҹҎŋȧŇtѵȊ´ɂȷ\x99ȸʝЯƲξ%ƈɷǹŢɰ',
                                                                            'ĔūЋ˚Ȑ˞Ӟ˭ҁ=˺őѰĂƾԇĿɭ°ͲƽʛčưȶϘÿêѷə',
                                                                            '{ͿȈϡҟϦάęǻΎƧкηţɱ\x96ƇԜĺΩүɂӹˡʪȫӿʂ]ó',
                                                                            'ЮćŪ˕ÆɯӼαŐԋũ8ŐӓĐRς\u0378ſ˝Ʋʗϫė\x8a\x86әȤЌǼ',
                                                                            'ЭñƧʃЍʝ!¡ŨɰѻʫϦʚФ˜ʡǁě2äĶϼœİǿ/!ȸǝ',
                                                                            'ʻŶÐ¤ΝΆĜΘô˭φɩфƪɸӖ˲ςЇЀĳĈïǃЫҋÆ˝ƛĂ',
                                                                            'ʹǬϧѼȎЧҗ˫ԏùǟΪ҇ҘОũċUrǨƱ¡ӌ¦˭ѮƄ\u03a2ƉĆ',
                                                                            'ĄΕЗгƄψϊ˺\x80ɿÌɾӦчťɝӲëіʘЈțɝǰɁɪӂ<ȁи',
                                                                            'ɏ,ļVѵԚ\x90¼ĝÐǪÏҡțҁũwԕѠҕˢɦĤаɜϧȚƕȴˡ',
                                                                            'МǵċȮ¯фˆʔϲÀϛҏǟ´ˠʒψƒϖƝʟϙȱåɆ@˶Ɉȡԧ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '°ʉȂӏəǉƄĊɧϏǨŐе\x93á\x92',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222851.890168:+0000',
                                                                            '20210209:222851.890185:+0000',
                                                                            '20210209:222851.890194:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '2èĲˬѨɄυƄƟ˫Ѕ}ʹЯԡŏԦɈȺ˝άι',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5525992678703624025,
                                                                            -5043623422037073364,
                                                                            2521986639722246302,
                                                                            4581678667600538572,
                                                                            4835361044385648717,
                                                                            2071609211474373493,
                                                                            8735646034590179475,
                                                                            -7695166228055703993,
                                                                            -5902696719343529253,
                                                                            -1199829114670866972,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΩeȡÅѬūƌΧȹ͵ԉʾɶФģȻhɱTÃ¶϶˞щʹĒʆʃѺʙ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222851.891036:+0000',
                                                    },
                                    },
                            {
                                        'name': '˚ƱȚԒƛʊчӿȝxƍˁʎʫŽԣǞŪӕ\x8dРȬԣä\x87ϨPӮɁȾ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3876437471270116487,
                                                                            5683922674591433992,
                                                                            3324464824262591706,
                                                                            8570398530836067904,
                                                                            1238611859345799660,
                                                                            -2238848496374018782,
                                                                            -3070331469157207707,
                                                                            5172227544300061299,
                                                                            -8113095966564990043,
                                                                            4332112265917017862,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɍÜѰǧñ˅<Ϸï҇PÉŬ;\u0379ɁЯ\x9dϵȌǞҬʮʕѝȘε~Ə3',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            42035.7477772515,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˇҌʷεğɪǊƽXV·ЮųūԢÀϩ҂0ѪɟÏ×б·ç˚ȩЧ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6197371779947096386,
                                                                            -6624545093697245238,
                                                                            6305274788145593853,
                                                                            4471391223367051261,
                                                                            -1506395026280436575,
                                                                            4983572582725369128,
                                                                            1228086020944148918,
                                                                            5411954131850653142,
                                                                            3433980132679404797,
                                                                            -4189022807255979844,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŰҀ˄ƐãǼ±õÖƁfΨYьʔΔı¤Ư˷υŒ:yһȚĉҮˡў',
                    'message': 'Њ|ϲˇɖaТɌӺ.ę©ΣʧʏΖˈÍӗǙŋʯƁБ\x80Ğҫ1ƛ˲',
                    'arguments': [
                            {
                                        'name': 'зƭĴʌ˃ǡωС',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222851.892186:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȘɧδԤɋĀϼȤԬǦϹȅɠ¥Νʳǉµƹ˓ȶ·ŰġNƚĺʿǳя',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9aΊÏĘćJȡôʁʷȅΓĐɧőŊђʣƫp',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĜʲZӚѠɳӑҁƯψd±ϑǏЗʌėǍқеԅū\x97ƒν˪ɹҲ˔[',
                                                    },
                                    },
                            {
                                        'name': 'ñbţԏƇƅɛƏĉĤƉɏųɵŮӷ±ʮģҟ\x8eiӊϸΰӊ˳Xĩð',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7808004565951971741,
                                                    },
                                    },
                            {
                                        'name': 'ȵĭ͵Υҥӗ˳ӇŊМNӸӑѼϏʸзŧǟѻΦȝlɥӃx',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԣ҃˪',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɳ8ԪěЄ;һӻ!ćήǇWѮϱƕѿǇŉ\u038dʆАƳбĢԎфƿōѤ',
                                                                            'ȶɓԎӒſԫҊ³˾ɥӦ¥Ѫńη7ȢƱćŵ"ȻéϕԧĆУȧM\x80',
                                                                            'Ǡ˝ĳԎ\x93ſҕСҁɲͼѕƹ\u0380½ȟhзǣчȗɾʉͰӮогĹz5',
                                                                            'EάԘɉ2ňːЙ¾·ӯӻщԚ:ímΰVűϵľ¼Ȯҥ\x93җαȹķ',
                                                                            'ũƏ˟ŪΐŨʥАϕԚɿ\x94ӑ\x8aðҎϤřÃζҙϜɝųÉêЕƘÈʮ',
                                                                            'ˣӹɐҙʬ{\x98\x85˪ҊǓϞˣšǂǧьDҌȜʁҩbɸ҄¬ʪţĖį',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'KΩϤʼɡѪɁÜĽːʜlΓҘȴʿ˦«ʩ:ЀСҁ\x96ɈİԊ˱\x8dK',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ТѝİӰɐόзǘӻΝøƩɁʘЭМψӸ±΄ǃǻџȭҚϋɺȒǡγ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɺϊԪɲѤѵΕǴεҴΣĒɣĊKĎϧρęƆҶƧӺ˯ĎǴ˃;Ǯˢ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2839591331536420838,
                                                                            5809308188980365191,
                                                                            3620958194959606722,
                                                                            -4048628268536523425,
                                                                            -4117469164718573155,
                                                                            956172216400797584,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'љЉ˄ѹϬAwЌeˎөæуăњǔШѓ)šΥȚß',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3319765715686426327,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҧґÈԬ¾ԝǯΧƁ ӏʹPҹʇ\u03a2ҘǴƴʴí\x8fʯʭƂĹ҃ѽфԬ',
                    'message': 'FԆЉˍȦǌʀӈ\x84SγԭӇ\x80АӛΛƎӴξňԉŪӻӗƿƝħҔȜ',
                    'arguments': [
                            {
                                        'name': '˰ƫ$\x91ԥnÖQʦ˗Ҿ:ӆ˷ыǇƄɤ˻Ҟ\u038bάɊĎǒ҂ҫȑέҙ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
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
                                        'name': '\x85Ɛ¤Ѽ·ʢȬҚϔ˸ӿƙӹζȈÇ-ųѻɿ˯TīӹƆTҪȎŝ´',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222851.896125:+0000',
                                                                            '20210209:222851.896183:+0000',
                                                                            '20210209:222851.896204:+0000',
                                                                            '20210209:222851.896222:+0000',
                                                                            '20210209:222851.896265:+0000',
                                                                            '20210209:222851.896288:+0000',
                                                                            '20210209:222851.896306:+0000',
                                                                            '20210209:222851.896325:+0000',
                                                                            '20210209:222851.896343:+0000',
                                                                            '20210209:222851.896362:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȸӮĔеƬĖ³ĺÓӗ¬ΚɝҀ.ͱԨρȂƧΧǗǥц',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222851.896842:+0000',
                                                                            '20210209:222851.896859:+0000',
                                                                            '20210209:222851.896867:+0000',
                                                                            '20210209:222851.896874:+0000',
                                                                            '20210209:222851.896880:+0000',
                                                                            '20210209:222851.896899:+0000',
                                                                            '20210209:222851.896905:+0000',
                                                                            '20210209:222851.896911:+0000',
                                                                            '20210209:222851.896917:+0000',
                                                                            '20210209:222851.896923:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĩӗǻȦӥʦӓɄƚέ¾ҟȑZŪˡǆǠ¯źɣӰщҠČͻԍϝȌ˔',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210209:222851.897168:+0000',
                                                    },
                                    },
                            {
                                        'name': 'яɍˈШǒ҃ȴʍӺʢƮ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': '˱Ƅɑ˕ǲǏҧǼzɟϊӴǅȭӕ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ʴ˵ЯȍȺŋϦǎȍɞӬȯĘ-ϢʵӌɛfμаžɅӭЗϚӛδȐ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 976891.0466295008,
                                                    },
                                    },
                            {
                                        'name': 'ɉƾ¦\x8fƥĨԭ',
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
                                        'name': 'ŃbŤ˾ɱѱ\x99Ìіż˽',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5390526855326541917,
                                                    },
                                    },
                            {
                                        'name': 'ԟ˪ȿʜфϴģĞ˔ӚӓԬ˰ЅԠĞƓȨ͵ɋȳԩ˭ϯʝţ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Αȕ8ȪςԬǴ²ͻ҉яƄШԚɎϕ\u0380ņʚɩƾAɝϫԜɈѡáńŊ',
                                                                            'ƿғҚÔĶӹ˩ςɠɖ\u038dʵàҧҥӓʉѰӾƺԥʊϱɺϑĝΰΘĠ˪',
                                                                            '\x95ȠͶʜɕͻԫ҇ӆӍ˸Ӧəź½ǍƞК6ʽɴƅӹӰϬ҇˫ɶǋÖ',
                                                                            'ϴɳΥĒБʿǤ˻ѼЛøԫπѶ˨÷ƶÊ\u0378ԉ¶όԇʛǬүОѧΉǛ',
                                                                            '˾}ˠÇêʱɶ¹9ɉӘӗѽ\u0381ːŴ˜В\x82ǳϘҥϩԆҊưʔϰсҼ',
                                                                            'ɃiΗтǜҫǗ\x83ɘϴTғѳ;GŪӕƏ˫αQh˧ԆǠ:òʠ\x92ɲ',
                                                                            "ϺȘ¨Ż˻vӮÚM¯JЕɷΟҕƃ\x9fAʋ'ƿӇ˄ХĈŁgȵĳҭ",
                                                                            'ʚѫϕкǸ΅FфʩƦьϔ\x97h҇ˣ¡ԨƏɲąÝ\u0382ʙΫ\u038by˕5Ԭ',
                                                                            '˳ÂĂĳļäЊŸΦӹӗɟί˜ŐǆӲǵxǏΫ˘ϿΎØҠÒʴɇŜ',
                                                                            'ĂҗȸhʉơӎӜâЎ$ǚĕÔ˷Ƚơő˃ɩčԁǂ\x9dԩʶƗ¸ũ˂',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'лąЇӗƁͷÒſËѡѲɷүҌΜMƩɎ!©ͿʀӄχŅюʖ϶ĵƧ',
                    'message': 'ǜԎɵљŹҩɓʄęӏхŷeϛª®ɘĉǄǻʶγϏ\x9bʄ\u0383˛ȣ΄ƹ',
                    'arguments': [
                            {
                                        'name': 'ӹǑәɽěЏǔϒʔɱΑΤɅǩҿʨЊ\x99Ǻѥȏʘʷ\x9aΐФŲΣèƼ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҏʓɉҎʦǳʣϢӬүɀ\x83ԍԬ˚Λ<ʰĈÖʸœ£νǂʏǶ×ˀΎ',
                                                                            'ҕΖѾ˫НÏӨˋϠщłѬοѬĵѸŨɹԆ˹ȋӤ\x9aŘ\x91ƝΓõ˘ϱ',
                                                                            'ɴŖʯѴ"Ҿ×ӌͶϳƄƖŰˠɞьнѮ\x9dɇїћmϋ8ΘÖӤǕƬ',
                                                                            'äÚēȴΔƓѾβȄɄXêΏЮãэ˫ɋ¢ƋR\x8cŽЎ½kʉÖǓƹ',
                                                                            'зαhśx˳ҼrsƋάȃʺϥƩїҚʽŧʏǫƌ(ſðԖӇҮʺӸ',
                                                                            'ȘԙʮыφǪŒúǒе˩ЫȳԪг\x9a˧љĻ7υԐ˯yʍzІÃӌέ',
                                                                            'Ŗƹ\x9cʤΛɄиV˘ÝԀзҮә\x99ϟˬәȦˏƣÏűǈұӝӏŪԚϛ',
                                                                            "d˗р˄ȺͶνŝӎĀ§ǥӃԠҢŞȺʊӟȲȣ*'ĒχũŋŔƕə",
                                                                            "&ȼǙ¾Íɳ˛ɧр˵ҷѹԢϘ\x96ƭɥȶϱ'ƆÊÍзͻɃіЧ=Ʉ",
                                                                            'ΟÆȵŧԢʴzô¿ɥ\x84ҏʪφӴɎNУϾÀÐƝȁǟvϾîǍϾˆ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȖǏ˕ĐǤǡǍĥʒмȨ-Ў',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϓǛӮĠWѬ\x9e\x81ʩȒӱˁŖɳľҬ˒ӤЏʧÂԎϜªԟэʬɕʽʃ',
                                                                            'ΘƇҲʍơϿù҂ѩĥjʩЬüɂΊϤɘǵМǅƑİӧɐҪɗȽëҪ',
                                                                            'uˁɥɡϻӡ½vέƬԓĠҁ~4Ȇ(ӮȆʃÊͳЀԏϲЗʳΨԤ\x8d',
                                                                            'şÆєȪ˛ЀɴʼʷǗɜҳˤȱÆǱȷԎǐʹͰÞ§ӀȖͰӈΝҭϋ',
                                                                            'ԩЇfɠÿшČú)"ѼЗӽɛϘtρ˱¶ɷÀĉϴѨґǃκȦҸȬ',
                                                                            'ҥŰϵǛҿAȸƬŖƺΜȑɍ×ʝԤң҄Ϡňë\x9bíɕ¨Ȑ˳Ԟǵς',
                                                                            'ϚşϯʪƃҐҷκоħҐӎķŚZĻ˨ϚԖ\x90ÊȮǤϧЙĂѪԢȲ˹',
                                                                            'δɰȫѽɚȂ\u038bψǘʜyѬʿЀɦӦÚԆϹŮϬмҋҊȼѼĀɈ˲\x9b',
                                                                            '}ˣŃЫàЖʢήӔ\u0381ԉ~ûaȚϷӳиŃЮрϋѸĳĭǡΓțҼȩ',
                                                                            'ʚԎΈIҰПƔђ»к\u0381ԭΙąʜԬΚюΈӟмsц˯ΨůщˤĀę',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȀʆĆ҈ɄɣĦЯƁʥυЖƩĦǟνŏΆбņöˡӼòϞĸΓϵaɉ',
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
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӲȘο¸ʹѮȉʍõΎ҉',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222851.900886:+0000',
                                                                            '20210209:222851.900915:+0000',
                                                                            '20210209:222851.900924:+0000',
                                                                            '20210209:222851.900930:+0000',
                                                                            '20210209:222851.900936:+0000',
                                                                            '20210209:222851.900942:+0000',
                                                                            '20210209:222851.900948:+0000',
                                                                            '20210209:222851.900954:+0000',
                                                                            '20210209:222851.900960:+0000',
                                                                            '20210209:222851.900966:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ůĒǡƗ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210209:222851.901256:+0000',
                                                                            '20210209:222851.901277:+0000',
                                                                            '20210209:222851.901290:+0000',
                                                                            '20210209:222851.901301:+0000',
                                                                            '20210209:222851.901312:+0000',
                                                                            '20210209:222851.901332:+0000',
                                                                            '20210209:222851.901343:+0000',
                                                                            '20210209:222851.901357:+0000',
                                                                            '20210209:222851.901374:+0000',
                                                                            '20210209:222851.901392:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ėȘңԅӞşΥʢθѶɫǫѹ~ǼЧȰгƬʄ¯ӛ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            751173.628157962,
                                                                            963902.9657425303,
                                                                            484810.73599711875,
                                                                            481059.2748514812,
                                                                            903056.798311799,
                                                                            333093.7251591911,
                                                                            198195.79332583968,
                                                                            503117.22677169496,
                                                                            715040.3893357676,
                                                                            213784.83220741892,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȫ',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˉǙˌÉЗɥʄŒфӂ^âʈΚϤͶԜжqʍԫ¨Ϯ@å',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7768886856400795425,
                                                                            5570365743197347883,
                                                                            2422865192988694531,
                                                                            5183193229742817054,
                                                                            8171472522390778327,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȼƼʛȼƾȴԤˑǊȨŤ\x93Ż\x9dǻʖɥͱӊĉв"ɱҺяǍĎÆˋƌ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'εҷΰĜάǘτЩдνΈȞǐӓɏ%ѩŚȆѡǟȬϯńϧѽˑҡʂǹ',
                                                                            'Ƣʘ*ˎӗӜѴ8šвЏƑʗӑωĖēǾüҚɪȹΑȈѫҫǿˬǰĥ',
                                                                            '˱ӎ¬ћƥҺǐҼӌҚ˟ҾϷˢX˹ϙăҳɻȧѽËѢŌ˜ĹСÌȩ',
                                                                            'zĒɔԮͳδȻĩʅŅǪïǁgɭǅWϲɽʉDÀӱų½ȜÃùќɀ',
                                                                            'Ҷ»ɢʰҸЦʻσԝ˒ϮԞхËȨhȻȭĦaʉíƣƮԨƱɮàȂɸ',
                                                                            'ȾδǑ˄NƆȝȽˍ·ɣ\x8aІ+_ЮĭëʢҞӕȪyҌɝ˧˹XϪԜ',
                                                                            'ɅԨũRГċ҅ίӉΆĘƕɚԇŉЎ҇҇³ķШϹ!ȄεɼŴƇĀБ',
                                                                            'ҐғǯԪӷŒϬҁѽҢʁΖƯȯ\x84İħɶŏ҉ʲЗͰǴǷҙĂԒȫŗ',
                                                                            'ϬяǺ\x8bƪϮ\x84¤ūŗ΅ԭĆòӊɯȿ˔ΚϲʪӶӖıʲƪʢӱϭǏ',
                                                                            'ԁƶǋɦиưɊėͰԫҙҔʧ˺ƎȈц[ϯѶӥν¬Ųϲýāǻ˘Ǔ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҞӰʾ3[0НɣćȑˍlΕɌΜӐíɡ\x7f',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3542004885403433869,
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

            'identifier': 'ʵРҏÀд',

            'categories': [
                'os',
            ],

            'messages': [
                {
                    'catalog': 'ˤ6',
                    'message': 'ǿ',
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
            'name': 'ҲʫʱȦāɰĽҼǼԁƆůyɰʥo҈ˀ\x8cҝļƬǜΓӑȲőʩ\x9fΙ',
            'error': {
                'identifier': 'ά\x9aƇЯüʐʻ˳ĦωҞţσǊˏǽʆӷҜǄ£\x90HçʵÖÿŵЍ\x94',
                'categories': [
                    'internal',
                    'access-restriction',
                    'internal',
                    'os',
                    'file',
                    'os',
                    'access-restriction',
                    'network',
                    'file',
                    'file',
                ],
                'source': 'ǲҾ"šЛȫóȖũхѲͿӏĚņǀҗǸ\u0382ԝͺĳҤùˆԐΔɛ˕Ͼ',
                'messages': [
                    {
                            'catalog': 'αѠǖӽȂή¢Ìā\x93˔ӀԘŶŀǨɎҤҕʊЂΗӒΓGĹȩАоӎ',
                            'message': 'ӊvͶԩӭŶͽӋSȠhˡυЕ\x9cχŧίũɢʋðЈмƘƼқɓӣĖ',
                            'arguments': [
                                        {
                                                        'name': '˖Ѻ˝mдбĦ҆Ȝʙ¿iҼΒΖӮ$ɨƱӷȿƁmVʗЁė˚\x83σ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4867017279421721283,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȚʼЎaΌѹʰМĕѺ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222851.838833:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԚӳdȍĉћŹȶ˅ɘʮT÷Ɯ\u0381',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϲʸȑ^оǷηǋ\x7f¥ʴϼʻъ˨\x91ƹ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϡ˯ɱϞǨҁȦîƝȂƦӝϝGǾc\x8eȈʒӲйȼԇӐǫŶȉ$Z˜',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƸȩЮҩüɭȽʲ˯¢ǊȆҌʗǪ˽ǙɶќɍÖӸȝҥϓҕˑ˰~/',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϸ`Ҥ˴Ɏ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222851.839846:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȝϞ9ǥǾ˨',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'źВʨԒ,ϡʃzƐ\x9cȈӑҒɺǉҐȁSŎ·ԨϹͲ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĸ§Ȇȵªһҏ҉ƈȇˆ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӟĳԭЯˏη҂ΕșҎɮҁɯҀͱŮ¦ΟǷ8ύbȥϡʷŘѧǲʪ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʲɘΠѕÊjϙ\\{ёǺӟԕЀҰ§ʐʰӂϒϸΰşȜÛΪЯΟÓԏ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѕMȤЖҺϗɍȋʸÏү{Ι˦u;ʦJƑω±ғƭ҇φªШӠɩє',
                            'message': 'ΤϭĂԣΏЍхɭʗљʔЙȆňƨìÉ¹@µϚŞ\\ɔӋʊωʣǾӜ',
                            'arguments': [
                                        {
                                                        'name': 'Α',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '=ɵҔ˛ǥĦԊǑЂӵ"ZŪȮ˛ΰЖђĤģЇҬ´Өδ˚ҹŠņƚ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 697339.3623069645,
                                                                        },
                                                    },
                                        {
                                                        'name': 'þ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5430362459723256175,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĭʤľŔǆĳ˱ʊӁԣ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x86\x88ˎӋ[ɭϝΉԁÃ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҷӆ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˌзʒʇĊ\x89ʾǴΈΈŰʱ¹ȧǵɟѹ?ӒЊƿʾį',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2050857578763300988,
                                                                        },
                                                    },
                                        {
                                                        'name': '¬ʐӫЭΔϱԒԜҸĖ\x9eqˉĽħǭɼ¿à',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2972972918952557709,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǧ˄҇þȶ˚ӣӞқ4ȿ˳ǽ¡ђIҹ˖ȯBƆĿщƔζɘ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'íԮDԘȦɸҚӛϋŁѣȈџŊɭѣѡшӶQʆϧϗћӍΦϮhĪ˥',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5701214388200206579,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'nͽȂɌ\x9eɜ®ŴƉ˯ҍUҩѝıѻǶȈәєıţκʀGŸέ¼Ғc',
                            'message': 'ӴҰIԔǟ\x98AЅĸҤːʪäКǆΎǝɃҁӐїȗɎȱ˛џʚӾ)˽',
                            'arguments': [
                                        {
                                                        'name': 'К',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʽWɂʕҎȇє˫iӡҺ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԗĖđſƓϱƊˢͳѯԢƔҕͰιіѝёьʁɉЊ˫ұϱʵҶđѶԚ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ч˧\x9cТɡȚî˞aŵԕ5ȏ˴ǽǞҹ¾Ɂ˱ʅҍɉɬōʾɓ_˞ŧ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɖĬēƗŎ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϲeâ\x97ķɯԊɈż',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɍȠłϭ©Ϭԓ2įɃŅѺχĞɷːĴQǚ\x9cĥȍϥŢǏŴɕ\x8aYӪ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʅɸɦӄ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϋ˕ӾȬǙ>ʤ˗ĭɀɂϺìĠ\x9dƬǾ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϗ)ΰǠԠԘǰŞϑˇ˯šƁҙ˄ʨĸҕØԬРҜ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'дΓȘƾǵˡԢǍңɊëҢ\x87\x9bʩǼҌȮȑѩιʰφƒɢéʠÄƝſ',
                            'message': '\x9fȵϜǞгȣӣƼΫԞΨƯɻϐΓȠʈϻŧϟЁʦӔȄяÂӢĘ9Ӷ',
                            'arguments': [
                                        {
                                                        'name': 'êŌ(Ȑȟ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3873026683067942774,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɠ,˳ԐҜĮǋІҖ;ģīņĭЫ˫VɆ\x90¹пŰvĥƔN\x96¡Ђk',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4166065519435812678,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŖЂ°źȀ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЁȥƳѨСϝЌǰΜǟνň¬ǍΊɃҠĥä˅',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʗɭǐтϱˍЉ÷iэƸԘѯůѫ\x99ĩŪѽƠ\x99ɏӒƩÝ\x9c¢˵Іԛ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɫӲДəƙ˱ƞǾȓΖϡÃ˄{ːҰ3ʉҷŗɘĿ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '΄ԃҥԗηѬoϋƾǛƼηÅĮĆҔ\u0381oѯψмӽƖ ˪ƾ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1881627068442587910,
                                                                        },
                                                    },
                                        {
                                                        'name': 'уɎêIÇxԪüƅ˜ӹŻȯәȡӈԣϑ!ĹӕƍԅȪ˔',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 804290.9532410782,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȑɺҫÂ+ԆҝmȪyҪêγҧҿoƱ»Әn˟ƊӄйЗ©ȎЙ\x84ү',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҵɊĜ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӿЉΆϜŷ3ƙ;ëʎЖѿә\x7fdɹæμÊxŞȿŬЊɄΘƸԪɚЄ',
                            'message': 'ΡӂӫӈGͰȻƣœʧʳѥŬƽɆ˱HϪΛǏұĜԫȕѪɲҹɻ\u0381҈',
                            'arguments': [
                                        {
                                                        'name': 'ТÕϴ˫јɎт\x81ƒˋМ\x84Ҏȃ˗Ћ7Ē˳Ȋ®ˀśЭԚĠk˵Ȯǃ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȱѯǤђ\x9dҸДɀňϫĊÖӁȯӹϥȰɬƎϞʗϰǕƏΚɰ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ċџ˶#ӴЈҜѯƋÖ÷ŶŇİ҇UʦÂԃҬýöΰʣ\u0381ȶĢÚϷʩ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѱϱDЊˈӎuȡҧΟʗʢŊŒӞÇűіęŐɖʢғЭζÂĒ˝Ȣŧ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϙϾġŅ\u038bʏɮ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8771823667496147040,
                                                                        },
                                                    },
                                        {
                                                        'name': '^NƏқǥ0ðДɸ[˳ǌ3ϔыåƳҖȣĹԝƄΐħʐ\u0383Űɉɑ³',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3447384027265091507,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʑƺϞҜ˯ҟҙ˄ŗԄʑʜƟÐƷИŊ·\u0383ʖ¤ԓǕΖ҂',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '΄ƵŗæϳӔƈɟƛƛí͵ҶңɠˉѿŇЯœÝʾ ԡҚBďǸzȽ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʢɰԟƑûœӤˡӒОƨҼěŹÐԢ˩śчĤǰkηίę\x9dйˊѵʲ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȐѠøˑƭȇ\x9aΙƁΉАЫƋΊʜ\x90üŏԮʽϪɯƛƊϳȫŠԧӄˀ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222851.850257:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȄɰΖ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǬԭŤĊϝǶχï˄ʾȥǭ·ĕ˦[ϹǫȌЛʇ˂ýȠ½ΑΰώēѺ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȋóʛȂΊǎeїҞʭƉɧѯǘӘǓ\x94ƼʯӆҚ\u038bƣøH¡γӦuЗ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƔĠÝǇǪϲҪіϻЅ!ºıԂŷŢЉB°ϽңʷɓĮ',
                            'message': 'OҍĔԟ˩ʞҜΒΰ҈ЕĦĊέÅʮ¦þǹȺˑʼиƾҰԬ˓įѪ\u0380',
                            'arguments': [
                                        {
                                                        'name': 'ŘҚРϧƪ¦ʨˡҠ`Η',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 763.6167530737148,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˠʫĮƸȰȑʗƥѰΆĕʎLʚKц´ЩɛʛΘЮ\x8bãɉҫХ\xa0sѸ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Å',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 822782.4445644405,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϨҗΎсƜɓƍ˺Ьçɗ¥υ\x88ǂʫӁǤΗёƴӽȖƶC\x87џ0џ%',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĿpєʐӁӆɭΪƋƇƱĮƭљÆ˜Ϭ˞ЍƬǙɪԊǾʾИΖоӑǩ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΑʐǱӐΥ\x8cЪһΖΐ¦˴ѧϡØ\x9d\x97Әό\x81Έŕώ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˽ĮͳӋѩ˭\x8aыҭÝq',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҿӑԀîvϗ#ŹҿīÙԇӁϫɗԅ˅ѮţЩ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222851.855905:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҲʱŷWҴԂʖ˼Ĕɒ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϕɷͷǃǞÉȔԕӊ±\x82ϝ҉ȚȻ˦ĊќȧÙ¸yş',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ļφũǧӘZÌ˩ëʵԝ˽Ԥ\x90ĦȽĖfǶʛë˽ѸҳȮ±#ɲӑÈ',
                            'message': '7ǀϾЕʔʚʋTԡ҈+чŁǍԊъΑЌǵԧӬĪƩԋӍιϴ\x8e\x8ej',
                            'arguments': [
                                        {
                                                        'name': 'ȋƯħĞԒsѓˬƁоȸɢθĺӁǿ4сϽ3äƄƞˀҕʛʯʜϮԞ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 854816963666145633,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϻɶjȣӕ˚БīԜȋ϶Ηβσĩ§áɂ¿Є˟ϼǔʣԔМҿú©Ԗ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5461906290869185714,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ť©ƂƅɳΎ˓ſì\x8cөζɴűҟ\u0382ЙíЅɀѺȥɠɐΣ,ЌҭǌǞ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȦӱǶàȪ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8748566363204215589,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӫȋҘƣӜë҈җҰζ˞qԆȐµŢĝ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѕηéӉХɢɟȑҚǍӡʡƞ\u0378ńҍŧʞӻ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ω¿ьԨϨȼεƆo',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ξżĐνϺʶƑγʘyćЇɜ˧έʮÆ\x86=пb|іʗŬȎә©ӳ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ž˩ʇƻĆƶ\\²ςӑǾԦħȹ˲˰ȻŁXĲϋʠȀƆȜλԒКвϝ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǢƑѫɄ˽ϞҥԅĸN˼ψǷͺƮɥĶĨɊ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 417001.29285408196,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʐӉӀ®ʷԖBʝǯξʽ£Ғԏμ5ξӎөDѼάѡрΘȰɈԒʢӚ',
                            'message': 'Ӣԥ˨Ӵѓř[їюȝʇϺĜ$vϕƚҪ҂ƊǭѹéϿÿиӈƪą\x94',
                            'arguments': [
                                        {
                                                        'name': "ûxȒҴvʅϤϐηıǋĤϬ˨ɮΥĉħάȠϠʚ'ϒ2ɯ\x98ҭƊ7",
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2785174351738144803,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɤӚŴІӻŶҞãȫ×Ѵ2Ќф\u038dϼѦ˛ȼϧϕσʞĦɷ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԫ1ȾȻ\x99ӌ¡ȝɩʾͷѲ÷Ͽ+¨ƎƑӎǄ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ČEҪȍȩĜǄ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 544308.0728934162,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӲӖʉБɲ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɂʰáƟώϡѪӔˈ\x93ʱєǅ϶ԄҖӓ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѼĤ˰ЪʿSЍʙ"Іġ˺d˯Х{ҕ˞ɲưŊ¿ˊ˒ҥΨɯϥÎǂ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҙǷԔδΩҜüŢÛӥʖΕˋɈǶǰϥĪЧĔδφŞѵǁşє·',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΊʀѶҁӐʨƑҥϓŶőӷǎĐūȰǚł',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǜΤ×ĂһǼѺ¾ϙǂ\u0382ǀɅΠӖԧҹҭɟϑϺϨȺsϋĔĤӍĚħ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6479546623890188980,
                                                                        },
                                                    },
                                        {
                                                        'name': '(ŮҕБʖƷ@ǏԬ˭',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ͳ\x84ĝҪƑЇOƀ˸6ąϹӎÔɜʯ¡Ǽιɨ\x82ЭƦǳӿІϸɸɓҷ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʪňӬbϔ\u038bϕϽɼуŬԏĻӯӃԎǢîcC҇;`ͼĤ}ʽл·ϓ',
                            'message': 'җљӄÉɘҖц\x89Dʮ˱Ŧʅ_ЮĕȂх҈ѡɪ˄ΝɾNƍʰƔєҖ',
                            'arguments': [
                                        {
                                                        'name': 'ζȲʌʅŞЌźΔƨй:ɁȗԣƹͻΤϾ\x8dũ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6433782863851266085,
                                                                        },
                                                    },
                                        {
                                                        'name': '^ǄͶяėѿҁϣƽӞɯ\x81Q\u0383Λ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɅĥĿǟҐѸȐĤƨѿˍƨԩԏ^ԈӰ0ѨѶӽōОƗϵ·Ǽ¥Ž¯',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƙīяmӣҵ˫ŊňӪѳҗʀ¡ƭѷʝɰ˷рçѣ!ɯԣζч\x7fćђ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222851.861194:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϏӳϑːSѫǂʲҌʴĉ˷\x98ȭ|ŭͰБƎ|\xadоϲǲ+Êˍʁԏǖ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222851.861396:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӻŵŊMҺӔζǍҤɨϕӟǠȫԊСϏȺѢϐЛԠ\x8fžϺʳ5ċӣŃ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210209:222851.861687:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɋĀԔћѿ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƣ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʱɘ\x7fɸȯÜϕ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʹɪӨǎΟ\x84όęӼʺ9Ň',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 930390.9527711199,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԑҀήϢ\x8a.ǄsˌȹȆͶóϻЊҤԃӎп÷ɋjґΪЯĶ˾ƾǐɼ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6032166865631129299,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ċȺŕӅξҙµɬȑԑ΅ƱǓӢГЦċιȼнʮѩөƔԕӔΆų',
                            'message': 'ˎҭҕŊ\x7fǺˢ/ŭȅѸŮ˲Ĺɦˈ҉˨ɯʯӄԞәǴ\x8eȳƅϲ҉½',
                            'arguments': [
                                        {
                                                        'name': 'ѦʿҳҘ\x90ȍЈ˲ӀўԎԙȝΝǏЉːɪҚЭűИʊʼΏѬʈǉʍɳ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѻӼѐˢ˝Ń˹ɻÄюΣ\x86Ɠ˜ЂɖԩƢӴ©ĴϐѬοƘԣÞУ˱\x9c',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Їǥšȓε\u0378-҈[ԬÇԚԓƩƓю',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4613804399410917676,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɣѥǽƭpWɫʦɥӃӶ:ŏĆʃҠƛӧɑWºńϪԬǀϑѶÆƢÙ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʞStηϱӣôɱü',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʔOÒԏȷЍӶϝƆ\u0382\x9dпϊСȸή',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʂӧԢаʧӆ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6084506243993581222,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Θ˝¯Ҡ\u0382Ʋǐˠ\x96ͺҏǫŮхӧđǧВѥˉ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĕ¨kˮ1ʿԋɆӽ{ʞςƋϭϱɎжŒԨӘʝ˃ЇɖΰǼǌʢϨo',
                                                                        },
                                                    },
                                        {
                                                        'name': 'þԄŘJЗ˩OΰĜƩʣћɶƞҺ\x8cʟΒȶʃƮʍԄĝ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʥąҨǳĬǹȇԙƑ:ιΠЈċ˛óϒѽĴЁɳ\x84ЌʹӏьͲˤӓё',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɨԠӯÓWǣңˬºɔʁʕƖΒԢȰĩЄǟƉгҘëŀěǯ˺ƢͿġ',
                                                        'value': {
                                                                            '^': 'datetime_list',
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

            'name': 'α±Ћ',

            'error': {
                'identifier': 'ѿ½˛ɉǃ',
                'categories': [
                    'configuration',
                ],
                'messages': [
                    {
                            'catalog': 'ΫÊ',
                            'message': '˩',
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
            'event_id': 'ҏιȂ\x8d΄uӔĮʏ˫)Ņ$ЪůƆԐҩvԋĦƅҭǀa˗Ԇԡ҂Ӓ',
            'target_id': 'ԀȷɯZԉʏţǠĴʇǛĬǉ#˃ѶŗʘШʳNʌ˵ҺͼžǢęҫЫ',
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
                    'event_id': 'ɘρPńϸɰǔ\xa0ԤV˚İǆǰҬѠŇӣщåԪоԓzň#ǥˊʙƱ',
                    'target_id': 'һϬӌìɆ\x92`Ļȹӥѯ\xa0ќ˛*ÁоFˣˏʛǆӯΞқɺɿɅȸӻ',
                },
                {
                    'event_id': 'ԨÑ«ȴʀ³˶ʱđŐϚ.ƑȈʈŢ˚Όα˛ҹț\u0381ˤĸʑԒΡѥ´',
                    'target_id': 'đ^ΰʦӲт\u0379ȘKȬ6Ϯɼь5ΊþЛǻÒώŵ\x8aВԟΤιыčº',
                },
                {
                    'event_id': 'ӏƗ¦ÂѠԅϵÂçӝѫϙƨΑÆĹ\x95˲ƬɱӖȺ«њχ¥ȟЈϷҐ',
                    'target_id': 'Ľ"ç\x9f˟ԪʮɆǢдʋȺÌΨҊIұď˟йǬÔ\x8eŔŭԊŤɼўӉ',
                },
                {
                    'event_id': '[ӵ©ȈƼǊŖɳΐ°\x80ĐȳɌϧйнӤʜӃҰÔƏÈƾӱί˶рС',
                    'target_id': '˔ϐŖvέáӝɓң\u0378Ґ\\ÛϖδĳѶȌЖѥ¯ñƓ4ȱô"ϔɐˋ',
                },
                {
                    'event_id': '\x90ưОƊȚȯѭѕφΔΘʫű~ˇ+ȗΪЉжƑѡǯœʰɨʪʹƏҘ',
                    'target_id': 'ӎɾ®ԙˌǢȵǡӪĸѦÀϓǴƞxʊЭ˳ϽƌôνơЯ¦k\x9a^ʧ',
                },
                {
                    'event_id': 'OӋђѼʫԥqʗĽɋÚǹӈΦхϊčĎǔŻο',
                    'target_id': 'ѼȕʚˈȤʳǔ_˦ǣҙˍcæƒѰ\x93ϔΒӹȈʋʿɭѥ§щͿǾʍ',
                },
                {
                    'event_id': 'òü\x7fԗÁΰԖϴў´ĩƧƻ˘ƏҐǏԒԍɊѼӥ\x8eңӱȞ˟ϪǦЉ',
                    'target_id': 'Ĝ˰\x85ÄŴҞɷÊƺūқ¸\x8aŉ8шӮǥМÞʬɓɪӉɵԠƴЊƋƎ',
                },
                {
                    'event_id': 'Ʉûǝǥњwȝθƽъƌť˼ӑİγƁɰŗї`öφåҙʦ6Ĳˈӹ',
                    'target_id': 'ƘӍԡҌҵ˒ȟ˥ȯϝԧλ˧Ѕ˗ӭĢϦƸĜ~ɇŎUɱԚнÍáǔ',
                },
                {
                    'event_id': 'ƏȄ\x84˥xǹ˲6ԕˏϥʦ˻âĮԌʁ:ÛØқџ˕ÿӛĒρϘѐͶ',
                    'target_id': 'ӧѳƲȐ\u03a2ÔˇȇгΘď2\x99ÓͶǆƛ˹όșÖуӼ^ѺΜ΄ʅȩͷ',
                },
                {
                    'event_id': 'ÁӐɣÆĒſӝȊђǮӝҠԊf6ͳЈßӗHҍЫı2ǦōʡȸҐԚ',
                    'target_id': 'ͽөȼÏщ1ӥȂҟƌ˲ŚӪѾҙȄΣŁҳχæǆӸξéϞ˫ʄêȒ',
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
                    'event_id': 'ÐӦŧƎλИ\x81˷ʞлћʥʉϰǀɩŻ͵ӰήӔѶԔқ\x99ĦȄϊήì',
                    'target_id': 'ѧω\x87ԍыǪĄԊðųƒӷĆȸвғā]ˠRȜÃǩïІһƬÃPʯ',
                },
                {
                    'event_id': 'ʇԜƷƺуɋөƈӏÒһƓÑѱİ˪»ˊʲΰѷҰуѶxɚιˬɁЃ',
                    'target_id': '҅ǳĲûęļǵpȴс^҂ɋд:ӗ·ɪɆƷмǦɌүƄʉȀҡȠŞ',
                },
                {
                    'event_id': 'ӘƨϝŞȵǠČHЪňͽҸĠϨқÖ˺ʾ¦ѶШ.ˣɜ˝ĺ\x8dŭΚˊ',
                    'target_id': ']ïфȘͻĲˀ˃ĒҜԒӺŮäҵԩǈĵʺǽɷâKĿťĪíƑҲ\xad',
                },
                {
                    'event_id': 'ԉȚǼÎτǚ¨ѣΆ0ĹsЖ,пǵӦłɠԃˎĈ?ŒԣʨƕȄэ4',
                    'target_id': 'ϹͿѐÜ¦ΡŔÑşˡ˒Ǩ˫ʒƖѷ¡ǝȐȺøƬôǔʏɒʮ˶˻ń',
                },
                {
                    'event_id': 'Қӝ\x80ċˢ\x81Ӗ¸я˕ĺ5Áʩ¡ű8ΔӖРȵÓɵҕïŋǊÛŽԄ',
                    'target_id': '\x99Жϝӂƪ˓śȎǢ\x96љиļҨĥιłƤ^ҙˡԐɥȉþΗԄϏȳŤ',
                },
                {
                    'event_id': '{ïͺюϐȎƒСÖ\\ґȕtƷӾ\x89$Ų)ԉϧǟЏʡƧ˶Ҙˏ˛ŉ',
                    'target_id': 'ʢӠѥɚƚIŒʝʭԟ¶ί\x8fΞ¹˾ÃԅѐͶɎ.ɎΎ$ҺʬJ͵å',
                },
                {
                    'event_id': '7>4ȏȅԌǽŵšӜʉǉ)ͺ҈ʹƬńǖɪƛ˓ĕѫ¦ÇÜеşŃ',
                    'target_id': 'ӵɹħʌОɁʺu\u0379ǐíВ͵¡ҷӬКϣɱӫȎԓnԚцԎǏŨǑʅ',
                },
                {
                    'event_id': "\x85ǹѥĈIƈѸӓÊΝãңηţ'łąѧ\x94ȗɛϱэʙӗĠΆƐǒ,",
                    'target_id': 'țâǠɲМēǈǁҊд\x81ɕÒŖϐͷȟуʞϫŃΈ¥ԈαŹϳ\xa0Ԭɠ',
                },
                {
                    'event_id': 'ƑĝѶ˙\u0383΅ОЭҥͲӾǷ\x96ƅûêџɶP`ÒˌӗОԂԁҌ#V҄',
                    'target_id': 'ƯΟЍČƘйƙ˳СӐ\\Ơʛ\u0382Ç˔źȄǡӓ΅ţ»ɭΟӌӛĿ˧Ҫ',
                },
                {
                    'event_id': 'ҦtД˟òЃќƵУȜ\u0383Α˨ņЎΓ\u038bɔʠĽǀ]ʔѭΡ\x86ȿªҗ˼',
                    'target_id': 'ƞƣҐХАNηѩʹΌŹơŕ\x89˝Ҵ˺»αJʛțϬȍӔϔǨқͿr',
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
