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
                'Ԭeȶ)#ӸњˊӰ¾řȪ/ɿ˹ÏǅȸҰ˧nʹЦğɘǚhǮѷ˰',
                '·˓ԪӦ҄ҹϾΓȸÏ\x99ȞɏƜ˩άѱʶƧɽԣԆɳɗɛɬИƜʌȩ',
                'ĆΨ¥ƵÃßǁ&ԗĺĿ\x9dÙ\x96ǬɾYņ2Ǝы\x8d«ʱ0Ӣιϓéм',
                'UƟýΥƘ@ĶȖυӀ\x95ʗϐǡӟÞϵϊЏϘĥюπЕԮќǑȢҼӭ',
                'ϠғξӅƣȗţȋЭΔĪЌќͷſԗτýϗӢѦĸÕĊʤɟÓ\u0381˞ſ',
                'ʤ¼ӕ҇ǞƱ|ӄǿėж|đȺ\\ѪàĬʪÖȼ8уԪÕϏv˝űȯ',
                'wǕΥɟ¯ϸЮӜӓìӋKɦĘеuӕʦͶēӠϠҼʪ;ѝˁȒpv',
                'ʀŏÕȓßԕÁż@ǽҏӐȉʔĺͳôȒԊYɘʵЁԈйҤȼϊԅų',
                'ƤϊϏЎζӞҘϮƿŬŹӐѥŜӝњĽȼʰƞԊΪnŀ=\u03a2Åĥ:Ā',
                'Șά˹ʘӁӰћϦӮŨ͵·˻ȓɾұĉ\\ҒΫÑҼʩШáϧĿjԜë',
            ],
            'source_id_prefixes': [
                'ёèӏ\x84ǚӀĨԗŝуһ҇ѓóԞЙ!ɤɞǩśҶ¥ŬƆ\x91\x8eŅ¥Ш',
                'ʹѪԆȲ˒αÀӌǶʊ҆ɵťŏ˶Έʩ/ϣ\x88εÊӵӉϷɹԂŻȕĐ',
                'ƅȀ-ӉԒӫƔДӔϲӰѕԃԀʼŦЛSOÁϕ΄ΞЏɍ˩ϣҡқˬ',
                '˅ɐŀ.ɷӞОԑϮ˞\u0380ϯДϠʵ\x8aӈѮŴǷε¦ɫӫɬһǥζҔɃ',
                'в҆mԝ˅ē.ąΚɍƂųvƺʮBǵíѧƇƱѕƫΠWʬЌЍƚѿ',
                'ӦǱȶ§ҷЧГԀǁӃʓɹқԢ±ńŪϛ͵ϮƳȒϥë¤ɩġʊȵҨ',
                '\x80Ѯʚ0\x9bӠŠѴ®˴ʑƀԣ\u0379ќƓһԣҞȇҝöїŤϸśϫ@ß\x9b',
                'űėʶΜǗɗȤûyΗΫԮŀԐӺʥʖѻӠѸΧʹǝƒȈ\x82ɤ˸ΏǷ',
                'ʅҾ\x82Ѻĭͽˬԍʀϱгǰ˳QƆʁПϟ%ŒȓĵɂǜҢʞ.ԘІЮ',
                '\u038dɖ8ưҾÌʮЌǹĭǑǏҮҘɚǖԑīĈǆưϸˏɍԗȐŎ˓ǋ\x90',
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
            'action': 'ź(Ĥσ˳лҤɾôŧc$ƋѕÓ',
            'resources': [
                'ҭϙtľɺΰѝnŐƜҼÐĹǧԖːòŰƬʹϛwǈȟВƊ~Ÿ\u0379ɿ',
                'ʅҡЀɷљҋ;ΪƦӃˏǡĒɄѿȁԠŽǽȝϝǻò\x81Z˟Ӷąҽԡ',
                'İйяɕ˙\x8ctӴÉ˚˙\x84ϷƼǠѹЂ\x92ɁˢΧļǹѻ@ӕЊʘŘԄ',
                'ÆĮʐҫɯgʣʉ\u038d\x98Ѧ_ӌщ˼Ѓ¥λмWѻî\u0381ԕȯɕƑ½ϾŲ',
                'ȀԭшďƁǔ˖ΧųύʼWҌϬқњąÁДΰȺӃÑšѣǷǣɌyɐ',
                'ѭфѓύѤÛӺѳȕƧφсҢԃÙİӒɑ²\u0383ѤǲˏȗЪ˓ϣӣǣ\x91',
                '«\u0378ӺӮΰρӦȯǣͲbťXʣʆ\x80ΜяϻʇˏԗŊɚѵɕεѿ;Ȱ',
                'ЁYȕүŌϞǫӨ°қåƔʱŽҐĮʃѬѻәΞȫүŊʖ͵ŀȲŲĒ',
                'ПUŠǿȖϣ1ǢҸԕӴ=ҼƋЖ/ɒƜԛҠȾеӱbϩÞǢǃGҷ',
                'zԫќԁeӰÜj\xad\\ƓΧЦŠ\x97ϯҏř2ǷЧɵ,ӮèJҏȂȔɑ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'Ǹ',

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
            'name': 'ˏ˭ŃΐҾ~\x8f/ȸф¾ʓ˖ßČǬL˲ˢȨҒÍͽʨ\u0379ƒťÚѮӍ',
            'version': [
                -5812167409431974808,
                -6644400972136223316,
                -2478305589730505987,
            ],
            'location': [
                'қԈтǘľҺǁԍƝПɤςǹʩЮӬ\x84ѣơŶ\x7fɌ>҃2ÊŏӂǇ:',
                'ϡԒ¹ȃњӤгɂʒ˘ҩ˔ÜμkaɊcЖƔʢΖΡϳęƯƣɆķɃ',
                '×˷дҋΔɑԆȴ˯ΎѿȐɌх\x9fѣӗϚǇɩҼЄǥęϪĽЄżԬ҂',
                'ĞӼÐ˕˗ӪĎөŸɆȤЍļʑáoǛҫϡNҼ¾ϤҳȠʂ\x88ќƬԭ',
                'ƛˠǫˁ?\x81ԉ+ǣЛ˘ʆӪ϶ԘѬ˹ʆȭ\x9d\x9eǓȂ\u0380ɇΘȰҋaԍ',
                'ņŚˁӅұ\x9fп\x9eϕÿϊƉɆʚ˚ĐɘʇɯҝђƢ˩ôʫσѓʾȻ˼',
                'ҟΉÙß˕ƨπ/γųѴ\x8dнӹǶʜ˓ӻϹӔҝňƪŘʜÞʔȨѴҠ',
                'ҨʰҰɻёǑȨ\x90ьūМԌ<ǅē£âȵŃÍ)ÈǉѕʞюϯÚaď',
                'ȎŝЊ\x81οзȓРϻиĘʫŲЗй`ĒvҙͺЁ΅TҩˬÕ\x9cčȀ\x91',
                'ӨĳӺpԞİҖǏ\u038bŜϋ\x9aˇɵÙϸįżɘԄѬǩҌX\x8cƂʟŁʢɆ',
            ],
            'runtime': 'ìǫsӱŊ\x94ѨOǍęʱЕtɹϺСǖ¹¹ůуƕѯǅʖʂɼţɸϽ',
            'send_access': {
                'event_ids': [
                    'δ\xa0ä¡ȎȗϳѩжɗŹѓȾɸӑщèαŻɀԇԑӖǕԎɇӅӐԛş',
                    'ĦœĎΰӷǃćɟɺъӽĎ>ʼǠFʃɆЗԌʞ¢ЏƨȊЭɌԁȹѓ',
                    '˝ɚΈƫV&ЃˈȳȠ6ƚiɀͲGͶ\u038bϿë\u0378ӰЬҞĶ*ӁϠҸȂ',
                    'nƻӭГ¤πɘʃÏÀѵȃßúυљɭeâӵӶӪ>΅Ͻǰ(ͳЙĈ',
                    'ӞӏǙϿ˳ˑԭϏɈǬКɑˇʫ\x8aǡ\x8dʃб!Ϊň¤¼ÓԩӽĿ\x98ϗ',
                    '˂ĖÞ^ͽюĉΊԍƱЙɜɺΚФĎǘҖȶ5lȹԃК˹ĉȢ\x90ĸ҅',
                    'ŸäʙŝҸƞƗĴʾĊɸәʤʮÚ]В¯ǤпɈҚӰҙҦǏŋҒәd',
                    'ěԋΩѨéϤԂɢͶȄ\xa0ͶšǧȠLϭΧȧ$¿ӂˬ˱ʢə¾ƾȍß',
                    'şêʱȇӋăӍǾѥȬfХâ`ωǿłƖћǬ`ӥǳɝΝƦӽīόё',
                    'ńȦѫқ\x82ĵе8{ϙҏͳΗΊƳШƚԗȩŸčŇҏΨҧγǴҷπΒ',
                ],
                'source_id_prefixes': [
                    'È*ҖņȻёǊêxĳɅϽ˺ȃ¿RӅΎϋӅǦԃЀӒԌӡíхҞĳ',
                    'fʖðƅιŘѨŀҺҙӘƨȡπӡЁҔ\x9fɘ˩ǌҾČĕʬʩϐΫξҽ',
                    'ʉɞPRҚΆɁÁӓɄuӯЉΧщÎÍƴɦţϕǏӴɼoδПò%ȁ',
                    'ӄŔ\x91ԥφΙʇŽʸʈy0фɸœԇфǎģPů˷ɼϲϚQϿϞȮê',
                    'с¶ȠЁў˖ңőǆБŠɶ\x87΄ԚŦİǿȏ/ӹmĭӞĲь\x86\u0380ѢҌ',
                    'ǑϜˡȖŻχ˒˞āӠͳǐɢǨyDmήœʣñĽƮОʿˀ\x8fɴʓŹ',
                    'Ӧ\x98ǖ˫Ý]μ\x81ͻ¼ĳ\x94ǃԍёŒ»Vϧҏ¿ę¾ѪɘһƱ\x8c®ǘ',
                    'ôɡĆӪзřϑәфϿxҙʹȓԘȀʒΨŰΝŒʷ×ɎӋҊɛƗϭ`',
                    'ҶЀ³¥ÚưЏβȪӍȝƹGȨ®ҿȪǿķЌћϿӽǇʆ˅ƙѡīi',
                    'ͷŲ\x8c҂Čц˕ģЎ|һцǕ\x8eϹρåӢVϢūǺ°ҁǄ\x83ǩίèӪ',
                ],
            },
            'configuration': 'гɿ<Ǎˤˈ˫ɻƊόĕЉѧшĦ¾®ӎ˅ҾџѣƊ§ӸфѿԪǢϝ',
            'permissions': [
                {
                    'action': 'Ζļ«Î˙Dͳ#˦A=\x89ӨšγĘ.ѢԤŌLĲӳЩёƉҬwѣŨ',
                    'resources': [
                            'Λ˯ӥʖňƊӛǭӰ_ÒҭȰƼɡͺɥʳȆɔӞϟŦÞ\x7f¥ȴʌ\x90ɇ',
                            'ȩϿАˑϬfÖƫȸʙʈˊ\x91³_ҷәКĀƼ^ȵÝσɯàʑӢѪ\x98',
                            '©\x8fˑĜŸuӵЩҖκò˘ʪøÕ¸7ЄųφȚǺȉŨɏţÇŷуԜ',
                            'йƣԂiȴԚś\x9füЋҸΖӬͽ\x89ŲӗԍϟѠ\x91҉ËƀӴȬÙɣϵĤ',
                            'ѫЄοƢґbԚ˹ʙΞǢүԨ\u0379џ\x85ЋςĐóԨҝυ˖Ƿ/È»ӼƝ',
                            'ҳ˽ņ°;ǡΚɭʹʨϫϳŎëԩƕƂ1ƅȇӰƺТҖӷ\u038dZıŽˍ',
                            '³ɨ\xad³ǁ[ŶÚōѠҁѧҺͷˬɋχʚǪҶɠǔǠΆɜǰϤę\u0378ʿ',
                            'уϪ²ɐeȓęӃͼҴӾΧԐǢҹ.έɫ˂ҳͼťÅȨ˭ɂ\x8aΥȎ΅',
                            'Œ\xadhӫŬҔÙʹȚĊ˕ńƪƲ\u0383Ūɗ¬ťȌƥÄӱRźѯčӡ˯ʥ',
                            'ˬʃŏɐƱʨ\x99лԋŽɭɈęÉҿ,L/Ӄų\x84ґΐɉ\x9eʼȦқ2Ȥ',
                        ],
                },
                {
                    'action': 'ƒ¡вГ¡ȼćЯɇǓèωǵȫҲА%ӔƎќǹЗőƦǓж§ӫдԡ',
                    'resources': [
                            '¯\x7fʱǑļΧ87ͱķʟƩǞЪǇİ˱ƞŸѲĲЊ\x9fųœҕтƛѺз',
                            'ư¥ӳȕ0˕ÌƪƽêŐ}\x91Ɠ\x84ӽђОȥ¶ɠ˹óɚЏҟ˶\x91ӪC',
                            '5ǍϣӪƚȅˋɜү\u0378˷ɘưÔͷ\u0382âƩEϴ|ӸZƣʶўOϘàp',
                            'ӱҔΞWď·é˒έʹϛќȪ³ΧĻǛŨǫγǱ˅ř˨ρȻŃͱƍò',
                            'ѢýƯ¶ҼíȝĬÒ¬q¥ъʚșƽ#;тǟҠlΡŒķĔ\u0378~ˏΫ',
                            'ΩқR¯ҮȨҖΠϓǺƤƜÊҁϫуͷԈėʔƮУΠӤϊȺ\x9cЛӠŽ',
                            'ʯž;юɐĮñΚHЧĩĳɚ˸*ƑœžКćБͺϯԜћƇÄ˂Аʦ',
                            '·ʇŔȎɟ\x81ĥɏΨü\x82˪Ȝzεǈ\x81ҊŘǲΩԇͶ\x8cːʕяѶ\u0380ӊ',
                            'ʴǑӰɣĒϲ;ҵŜɁɺɮôӬΜIЍЮϱԩWŖ\u0380ſİǜϝϼӯ\x83',
                            "±ӾыԌɇŤÎΕ'ї\u0379ĴȌПÂǙʪԊѶǄϰƒVǷϧTԊжěƘ",
                        ],
                },
                {
                    'action': 'ƗͰĠƣȵг¶ǔŻʸСćiζċњӐӠȆ¢Ӕόәʪҡїӕ¨ʇǪ',
                    'resources': [
                            'шϗǡ˽˛Ţ҇ϓ\u0380ơҨѐŨŏӺϡȠťğдšΥ˪ɹıαηʘӤҭ',
                            'ΖҎǨ1Кʱηɳmʣ@˶˅ɞĚ©ĀƫӒóћƊϻûϷǔǱ\x92Ίч',
                            'ɯȀзҕϻΧÂƑHЌɝύĶûњ)°ƎÛцʏЗɴǥʙ˃ԍƲҽɚ',
                            'лŏӔѳ\u0381ԫҁƍƞНѩҫǗƃàΣʹŽЉýªȫɑϼƅҦƠǸDӌ',
                            'ЫħǞφŬʤĝǏԜ\x8fǿAʝ5ŵßÉˊɋʔȿwҊԜĀǤǵ˗Ⱦł',
                            ']ϥőƩΆэ=ȚӕɾԊPñʭτľǸňӑӍʫҤͼЁƨ!ƧǍŅԃ',
                            'ɔ\x97њғԡΰԀǉέŮíƥɤίȉǱųƺҤёŗɴ\x9aʶό˰ŸɰŉY',
                            'æxʅнƺMʧДɔƋȭʃОЎɚĥԦԚˌӈθӾͱӣԄԕÔƲҋϰ',
                            'ƕˋÐȏèȯƀϲϜƚų˱ǑɏЄԓЏȵȼԜϞ0Ψ\x98Ύ,Ӏ5Jʶ',
                            'ɝíҷ;ǡԎ\x96ЛȆÑԖŇ˥ƩđҸϊϭʀŕɐÞδΔϮûʿс9ɰ',
                        ],
                },
                {
                    'action': 'žњϹξȻҔϡʉȦκŽrȜ\x93ȂҨœІŃÐ¹эѽέӈŹć˞jϴ',
                    'resources': [
                            '\x90Ҍ˳Ҟʆ©ǮäύуŔĿσѱƋļˏġѠ\u038bʭȸʱǮ˧ʖˊдӿÎ',
                            'ΣƋѼĪιʃ\x7fӼȸ҆åģ˽β҇\u0379çɐǊјǬӚC˓ӮӸɥ˖ҍy',
                            '˻4ȂʶˮҹƳŖŸȑͺȈĊѢ˲ʧŌ¹ɔϩ˺GƾӔ˴BŌʔɑ˛',
                            'ђũҗϒ>Ӌ\u0380ʾϸȭΔȴˆö˚Ӻѫ˚aУɥӠрɡȪЍɿǘʓѭ',
                            'ЇŋƔλʟȞӼʱkκũľǒí\x81Ǜ?Ӎϯ\x81˗¹ӊӖȾƥ͵˹шԮ',
                            'ĭƞңɚųĠŞΣҁ\x92ӽƙƃҳʑѴϖǁȸϹɍԂǙ҂ʚЀšџĩԌ',
                            'ǆˁŶԚГh˜ҘϑүŰd˓ӹκĎǌµĹɾӿǢğӷàɼƏ³Á^',
                            'Ѣ¬ʔŊď҅ŗ½\u0381ŪҺHúͺƠFάɗȲѵɥÏ\x9eÎͷҭρ^\x8eƞ',
                            'ΩӢȾ\x7fɓ¹ǪƷΟʝĈɼЭӇеԄʙɧƺ\x99ЧӦҴǨӂˊи˞ǾȆ',
                            'ҭWЈšŗεĜЁКЃǢēÍ\x85z˺ҳșϢǒǫǳԀчҖхԍӜ\u038dԥ',
                        ],
                },
                {
                    'action': 'Ί;ǏƜè¾ŝƹω^ѧϼ3Δҿ9´ƫ4ȼԡwΦˎҋǖæɧ˽Ԏ',
                    'resources': [
                            'ҭғÝ@ÈȀųf»ɢͽǱ~ĨēͶȍTÄƌΡĻÓɖѷ\x9fаΌǬΊ',
                            'ĨƈgΛĉƒɳ·ϛƕԁҿ иԜ҇ǤҖѼӷĆơ»ϦϭźԤƉĎĦ',
                            'ϝАɼϲ5ˁΓǔʗ¬ΐѤЌšƪȭ˥TɵˎĿƩŐːSX˷ӌŭѩ',
                            'ӒΖŻхfλΙ&öԬȲԏǁσiҸɳхӡчҮơňԅˣŲΉüʫԭ',
                            'KԀƐСϥѝĖȊeԢÜüʈÃȡùĹϖ\x86ҙ°ШłЍџȇɨ҇ƀǋ',
                            'ϺӳөͼĤБМȣʿ\x95ѵŅ\x86\x8aĮʥϭʹɶʨȮϷІʷх0Ёμȑȡ',
                            'ӥԪ÷лнмζŏ®Χș˗ҒЬĺʭ1iϢĲ\x83ӡҺÚ´҆ʛ\u0378Ƙʳ',
                            'uӉȽˉǷ˥ʚʧԃɐˇшҥɽ˓ΙʱúʗȢĢĀ҆Úŵӧӡʷđȝ',
                            'ɏϢίњӻľБō\x99˘Ҭŕ³ǩúͲľ\u0379ϧӭŐӞūсɃмҮёоȆ',
                            'ƊΠɀɥοԡȯǱѐ˜Bɺ}Sr\x90zϾΛųӺϾʆӛϿѿԗϯʜʖ',
                        ],
                },
                {
                    'action': 'ХɋǼˢμ§ˋáȡƶȖɴƦҚΰ˩\x82ŭŜãȱȥöРʖȰѱΆ\u038d\x81',
                    'resources': [
                            'δƆĂʳ._ɓʖӕϣЌȻɌUҁ1Ѵҵ@#ʛǲҊӝňƙԢpĬÍ',
                            'ӸŷͿҥӼɀqbΰΚΛɈͼѯъјӷ˗ȇӞʈž΄ƂҨЎ\x9bå"ҍ',
                            'ϥџ\x8dQĬȯϩƉжű]Ÿό˓{¡ϲ=ΡԟɸΑѩMŷ¡щɁğҒ',
                            'ӟ-єШԐʽȉӊ˚ԝӶ°ԙƍwĎ\x9bɅήϺґϲ\x9bʭXӬʳɒΖʇ',
                            '¯đ҃\x96đȝ®ʿЊϋѓĦ\x96°АњҲӟħҔÛѐ΅ʤȁˆĳȤƙF',
                            '£ˌƗӯʇЈҴԟWɰ\x9bɳƊχѤӳOѽι˽ӡ\x8cʲ!БҎǁєʹ\x93',
                            'ʛ\x84Ķ&ϠԚкɐʇӭųϵưǉ ҌűȌ˒ÆƙΞýɩьͽD±oÓ',
                            'ҫÃӿʅŐʫѐƜ\x95ŪѰƍнάԎŢ\x9a\u0380ԭЄԇȳȩϣËЃŌŞŜc',
                            'ϕЂӁYͶ3ǌрҙеϲêѸ½˃ǥӾӒĭɱǚ˃ԣНЪƱĜ\x8aзЛ',
                            'ϵĿǹÄ˯ΔϦ#ӳūƶƱîŸǵǗƉǾʳˋϿˏ¿ʌä\x98ĳФƍǜ',
                        ],
                },
                {
                    'action': 'ӎΨɗɨǺ±5ΠļɸԤљƑоaĐ\x92ϷŠҸµ\u0381Ŝ˝ʱȡиǛƸɟ',
                    'resources': [
                            'Ƒ\x92ΐΙӧϿѯ´ʿÊŰǽʁâӿлӄĀȸʛπЛȦͰʣ˂ЀͻѿӠ',
                            'ϸԁŁмѬҜʀʺў3ĝѰPέƮɉʇͱΓƪȣʮɠџԎƹϰĪтȑ',
                            'ÁʖҫáсԆȑŝԃ÷ԩ÷Ѵϋ§ŴϴԙΩɩƞͳɜЅěàȩα҇ǡ',
                            'ԒȢźŽԋδϰѮҁȥҨωĈ;ҰȍЇƣɨʝԠ=ӁǱΐţħ˧äԣ',
                            'ӊùǂιȀҾȓĂʟΌ˾3\x85őë\x8fˆԢʮӆè˲ΆɦΫſσŇǵБ',
                            'mϮʧ͵Ǽ^\x84ŞǟɥǓ\x83bÕÆʎϋԍïʶßǎɀӣġ.Ŧʒԭǀ',
                            'Ȭ˃ǛӶȬʋF\u0381Ϻʥ"ǕɣҔмεƨό\x8cΐωʬƬɾĕОʐǝϚЪ',
                            'ϛ·ȻϴCƚ΄лŌЋXυϜрΎʋУԉңΥșԏ\x8e˚ˣԛĲğҍʁ',
                            'ɪ͵˦ʮ҄ϽҶ҃<ΘπѨλŽǓHΡǖЃυʍΝř˄\u038b\x80PʌӨz',
                            'ҁ\x8eɿ;WΩÏˋØƾȇаОcȈǰǁ˾Ԓ\x8fҫϓÙнÞ©ԏćȥÈ',
                        ],
                },
                {
                    'action': 'ſ.ˤǙȝϟsώèӵџϯƄǆ˰ÇЬ*ʢ˗ˈëїɸÔåCԡʺљ',
                    'resources': [
                            '~\x83ͶʩiʝӺ{]ǂψĥгѧұҟ,ҾЯȉԅƪ»ɄͻlǛȶʣD',
                            'ˍĸЁηԇļ{έљǃʔψźƔϏԂǌ·ǖиѥrZ*ǨȑԡԦга',
                            '\x87Ɩßzq\x81˙ǚȟͲІɓϙҟɿɌѵӕʗ˫ǬɲÌAǮĭҕЋʰԘ',
                            'ѣ˹ϦђŵԬFѝϖʮίӎöw^ѩʌѯǆеĽ¯Ņ\x90Э*Ε{\u0382Ҩ',
                            'ɀ˩ʺҶ˱ĹŀÈu\x82΄ҢǛ®Ӧ҃\x89ɆϢď͵\x955Ɗé4ҋɝ\x80ǈ',
                            'ǃƒQѬgӜƹӰĂѽҿЄȩɭӹѾÑѺƫҿw£аԘҜгϋӟҌΘ',
                            'ȬΙɍοӭϚŰɤāƀʁʞāѰμƲćɡʽȡɊƠтßό˧v˃ēң',
                            'Ԏӟδçơe˨ӆŶZƋɨϷƋΫĎԎϝʳқƸƧNѭɝ\x8b˗Аŷĺ',
                            'Ѳɲ§ǚȜYɸPǆɼâwĻ\x81(ӤĿИӫȵɈȜN\x8bħԓīÏӻŚ',
                            'ǑϱˀГ»ŉ_өɷģХŹUÐӄϖÆĞ\x80ȄԊŻǔԕ\x93Ȁĉλʀʍ',
                        ],
                },
                {
                    'action': 'ϳȁθɆ0.ƍӭφьéƉeưʛɁϭкƢԩîÿʌȌ*ӽ[ЉύϚ',
                    'resources': [
                            'ĮøđǶüʪʛƛĎʇьӤǱʳKˠџLÉƾЁϕƶѡϠńɮχҶѴ',
                            'ϰɐԌʋЍжǛ¢@ňǓσ,N˼eѤˁѴȑӑʫĵŏ!άԤϼΈõ',
                            '\x88ʉǔɃПԨʄěжWњƵ6Жԗ¥ɠфӾԧÝűİвɇȰ\x85šŲԄ',
                            'ҋˬ˧ǳѱҞʔ9еϨАα{ÜƑŭđП¾ǸɚÙяň¬ϵŏDŭĥ',
                            'ԚƍƋӔɂђԇҙȲӘΘҙ:ҏ4Ѓ&ʹҚǪԟž˶ӛдӓʹƻ΅ɽ',
                            'ӆϯʋüԪԙăυчĝʧұƻӔԡѱΧɘĆÜÂϫγáǦπҳԁȗǞ',
                            'ҸǅƟɰ\x81ԧϚ#ϣѳƜƢѷνŲƎŞώǻǦ.ǙԮєϨ\x88Ǒ΅ԫˮ',
                            '˅ѧΣÈɅѮƅ˹ŇÔ1ɕԐёA©\x90ʴÝĘҸ\x95пӕǋƵʊʏ»˝',
                            'ʭϪȴͷŎǧƹңӞˍOǷʜύ҉;\u0383ˉыЏʆϒqąԗȆxϺ\x89\x8e',
                            'ҥÎұҬ˝Ѿ1Ɓ(ѽpƢǠԇ\x7fʘӻңŗѻȾЃřóЪʀˢԊȊ',
                        ],
                },
                {
                    'action': 'ȅĚӹuǼӌԑϐӝӡƍĀÕȽԑ;ƚԁϢƖоԊЪҍϒ&ŞѤ8Ϊ',
                    'resources': [
                            'Ӹ±Ƞǅ˖ѺD͵ćӘѶǖŪǫʹɼԋɍҁʰμϖ+Ȥέʴǻʪӧʰ',
                            'ѱěȺȺ\x85ŊVĜϤԅÆòɟˆɊӀHǤʦрçκθχϫрȕǼ<Ҽ',
                            'З˚ÙԃѭМқ\x9eмͿñӼǕAOñǑø¾ʋ\x9eǏ҃рщʙɓƜƛƶ',
                            'ҎЍӢĊ;ʸ\x82¦nʻŧ.čϣ3ӯч\x98ɚʸԇĆƌЭźʗĬ\x9fȊʹ',
                            'ȜʭҾİюЧ˽Ȫƴ\u038dƵԘӋϯĬѫΥÉЩώǋʊÂѠтǾЇÖΫȀ',
                            'ӣΧό]ʇ;εņȼѕǶϠ҆ҽʇxʰƌˀȝӐƒȅԢԣ\x90ĝџ\x9cϞ',
                            'хɪɛѬӝсӉӦѻхͽʩʉФİҕŁęϘȅʹОʾŚļԈѭǼǯӰ',
                            'ʗ\x8cı?ʎѨǋ;ǐΑŸʭ:БʲƗÓƏҜɒ\\ЪϥӂɰԁԨï¢ѹ',
                            'nŞϯ\x9a\u0379ǘțłϟ϶ɆқŁѧɀԇƲ҇ӎǍѷʥϐԠ˼ēĮȰтF',
                            'ÑӌώǦ΅Ӥԃĕʲ\x86ԮұġνIɰʠƦĒˍťlőǞ˶τĮŔȊӐ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ī¶ͷ',

            'version': [
                -2700688077211726293,
                -1680179593720488826,
                -6253547494546965040,
            ],

            'location': [
                'ԟ',
            ],

            'runtime': 'x',

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
            'name': '+ϦŊЮƓˣ˕Ҝϊą',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Νĕԗ',

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
            '$': 'ƙϹėѳɭӛУ҆ţɘșψȉӆÈƭɥȷ\x9eȵϛśҴɹпƽɁϕ˭Р',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -4673307526949706822,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': -80433.8731248586,
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
            '$': '20210910:161212.604614:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ѱɦʜЊ˾ϦFțΊʋƴÌǴҸĒÔ¶ϪűόǨдˁŲʸЩ҆ώҦу',
                '˵ӺñХĉҤέǱǎԉǧӒȇǌΙˎԡƐʗӠΖŲȌŞ°ӫđѠȐǩ',
                '\x8dƑņȦӎ\x86˹§˼\x91ĲjȄɒȡȌѨȓ\x90ɟφȰǡϫЃƚͻНőϴ',
                'ģŊ ŊVǹɨđȰұʇĺчȊϦěìʏÈȷïҸӳʹϔǅȥӕԎȗ',
                'ѺɰƼƿѣΉʍüΨfΩƲǂÕѬ\u038bƻVǩĢƻˉȏ\x94ͻƞȶȳ˼Ĥ',
                'ù3ʍϣɢϮ϶˵\x8dѢΔчәĞˆ¦њΉҾȮԇϫѾѿ\x90ɴ\x9aċ{\x94',
                '˗ǀƂßЊɕϘƷοͺǭԍÈĳ²Ɛ\x8e*ɴĖɓůȶԙѶҢҞϮŎ|',
                'øďĠMάƐαѥɯʢŮțʄþϗǴӍ\x91\x81ӻ˹ҬѤeԀдŹŪ\x97ʼ',
                'ȄҎ}ѳȼƼºɧʷɈæƬĽǄԏtԛдȹϐȊɆɋЄʊҳPѵ\x8aã',
                '*ƍ8ȼјʺқȊϜӿvǟĩĥˎ]Į˫φɭ6θɤΔӥҢÛƐǨƶ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                832699810153269310,
                504998726123164197,
                -1321647838680442428,
                -8695167275157117371,
                631539780642787100,
                8990758389529422863,
                -4877484532745759449,
                4004849888831006680,
                -651689735495542465,
                -8728567604854265191,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                363196.2325718139,
                383586.519415054,
                217844.4639459416,
                938868.2984526559,
                64322.119556811056,
                289228.61326889234,
                -84976.36740042074,
                244703.6448847081,
                102774.8765025645,
                113591.26241758102,
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
                True,
                False,
                True,
                False,
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
                '20210910:161213.676821:+0000',
                '20210910:161213.694746:+0000',
                '20210910:161213.717574:+0000',
                '20210910:161213.739795:+0000',
                '20210910:161213.758981:+0000',
                '20210910:161213.778452:+0000',
                '20210910:161213.802058:+0000',
                '20210910:161213.825125:+0000',
                '20210910:161213.851518:+0000',
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
            'name': 'Ú϶ơ҂άϥ˭˯ymЭǂӣǔӻΡЦ^Ӧ',
            'value': {
                '^': 'float',
                '$': 259600.0432736773,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '\x8f',

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
            'catalog': 'IǉԦɄԪҟ¿£ȵǅǡкҡɰΥʚęĕćϢǜŞƌǷü\x80ӟ8˨Ŭ',
            'message': 'ΪVȯƗâµңǾљёүӤМxϵΞ÷Ӧ;ϫΪ_1ŁZ˖ϞзӐϞ',
            'arguments': [
                {
                    'name': '\x98',
                    'value': {
                            '^': 'int',
                            '$': -5192666251624177431,
                        },
                },
                {
                    'name': 'ʒӄȱƂұʵ҈ВтȦ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        -56581.363482048444,
                                        640660.6400218606,
                                        936669.8967717408,
                                        887274.6230664848,
                                        289959.9790205929,
                                        98565.85183028551,
                                        498573.1637155714,
                                        387588.5788837004,
                                        362228.85065817955,
                                        402958.54022244643,
                                    ],
                        },
                },
                {
                    'name': 'ȟ˵ʘŦɪ5ˆйϝ',
                    'value': {
                            '^': 'float',
                            '$': 175798.5079090204,
                        },
                },
                {
                    'name': 'ËҲЭҮʫ¼Ưοƹ\u0381Öǫ~ʹˑҌҀòщșѩȔϱӅLЏИɵ˚ϛ',
                    'value': {
                            '^': 'string',
                            '$': 'ԓŪԒ\x87ńԄɯõύˇґȝшĥǐѰӕϤ§ŹʳƉȺ΄ŋʓ˖\x9břѨ',
                        },
                },
                {
                    'name': 'ƏңԖɓǰɿɫʜррšҊ\x99˾ҒҚй˱вĥ˼ƫ ԝƅʾǿȂԑĳ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210910:161210.842278:+0000',
                                        '20210910:161210.859974:+0000',
                                        '20210910:161210.877513:+0000',
                                        '20210910:161210.898154:+0000',
                                        '20210910:161210.915440:+0000',
                                        '20210910:161210.932980:+0000',
                                        '20210910:161210.950194:+0000',
                                        '20210910:161210.967726:+0000',
                                        '20210910:161210.985003:+0000',
                                        '20210910:161211.002802:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ɱѐɌǕҵΗɞȩϗʍ˨',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        False,
                                        True,
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
                    'name': "ΈʇѬƆЪϯȫƟɳ±ʎȮüҰ~¯'ҾЦÒρ¦ǋЖЅӵõ",
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        '\x87ѓЙȒv¯ӺːŋȁȘʴ҈ȲƯӿ!QǫËʬų9ʘϡŇʧȜ˸ӑ',
                                        '\u0381˓ąЖ҉ѥώԟƮ¨yǨ\xa0ŭϲȪǱǖˎƏχËʌZǥÌԬѯɀƺ',
                                        'ǾʅˋƓΒҕэÀӗϋԥѮҙԈŽӼƧӉjƾŧƞЃȜVҩʙ»jэ',
                                        '\x9aǅUɨǔ˘ΣˁİaЖĒŵ\x8a;ŀƉŨЏǣæȌ[ƯʚҶĹǚǟω',
                                        'ǢƠɽĬ|ȪǍɥ\u0383¿ƎӉІЍҲĕȏјҗӿӓ\x94ùȽƨĬʉ,ǖɦ',
                                        'Ä˂ӥѦ˔ǂʞɇάƜEҤΝʂΩиƠϩĹɿÛɗucȎàţ\x8c®ȕ',
                                        'Ѫoԟ˷ӮtЏ˵ϯΡϨǧΡӕӷνȆҎӷҢ\x94ƺҡDԧƫσϰžӥ',
                                        'ʻĽЋȢԮsşΩʝ÷ɯѕ\x98Ҡ#ÊԫԛҹİɀΔż˨PάĈǶƢȼ',
                                        'õˋӀǿğɽ¶ˡʍѓȞ˞ɼÄεº%ҜιZƖπǺǋȿϳӰĨŀЇ',
                                        'ËѹϭOƞȷѩ5ʜâŪǞƮƜʹʽЀÞȮȆɯőń^ҴпÂģɤɷ',
                                    ],
                        },
                },
                {
                    'name': '΅ʴƂЖɈś\x84ǌ7Ѱ©(ΤÒʰυƗͲόκşҝГǺÅȩЈĪΪɃ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        6424491524356022226,
                                        2169793981110096022,
                                        -2192791582239095044,
                                        7802297901894729523,
                                        -6119817209829904754,
                                        794538601613510254,
                                        -3094660618035236859,
                                        -476082494915014869,
                                        1604944862677451740,
                                        7496515242921508349,
                                    ],
                        },
                },
                {
                    'name': 'ЄΒɰƂļҋǞĤɗ÷εǋĮcˋҬŋΌŅĪʗԉ',
                    'value': {
                            '^': 'float',
                            '$': -37029.02856656483,
                        },
                },
                {
                    'name': 'ǩяͽԧĐγǥƌʹҙ_ѽīϓȗŦ¹˱ЏŀØȋԝǼѬHȸſëü',
                    'value': {
                            '^': 'datetime',
                            '$': '20210910:161212.031660:+0000',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': '\x85б',

            'message': 'Ⱥ',

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
            'identifier': 'ԣǷǙʬâҵθɉ\x94\u0380ʒʛѪюʠІМ2ɷ\x88ҫǮϵL\x9dέЕӸҎҩ',
            'categories': [
                'os',
                'os',
                'access-restriction',
                'invalid-user-action',
                'file',
                'network',
                'configuration',
                'access-restriction',
                'internal',
                'os',
            ],
            'source': 'ăĴФƏӹǮʠɃ)ɓʙʋҥԗɝȿϡʗʵϚԄȘfѭăΛЯȄCˌ',
            'messages': [
                {
                    'catalog': 'Ɣӗҗ*ӄǘНӘԈŊάŽʷǶ\u0382ЍҠɡВɼǪɺΞԗӱȽũƄ\x88F',
                    'message': '\x89UƙͳѼϹ½Ȓ3ϩ\x8cèÝуyǦµɄίªӸű\u038bĂʯȣљʈҶκ',
                    'arguments': [
                            {
                                        'name': '!ӂŔP˕Ŏΐʉ ɭҊɊȿ5Ӣʄˀu\x8c',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8328766984667008316,
                                                    },
                                    },
                            {
                                        'name': 'ČЌʯѣ?iЁë\x81ԝȎŐǬƒѦ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            166060.66879150172,
                                                                            909552.9010276749,
                                                                            428712.49984103383,
                                                                            895308.1528764348,
                                                                            799726.7359738455,
                                                                            237851.27380854567,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʱ˛ԩЛϤōɫ\u03a2ЍΉƣȕЈƵӑǛг',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            233065.08610623615,
                                                                            44662.02030244839,
                                                                            697846.7996216407,
                                                                            580454.2483571471,
                                                                            97135.23455281515,
                                                                            345686.82754975994,
                                                                            555159.483795245,
                                                                            -37507.85641137559,
                                                                            607564.0957843491,
                                                                            471388.0408695224,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x96ůǞΣѯƴǪzԓ˛ǪʙˤP«˜',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 810639.6923171232,
                                                    },
                                    },
                            {
                                        'name': 'ьϝцΜǦɁ;ȽĀӁ\x8fɣҽǊѤжơѓÀ&Ĺ\u0378ĨԤә\x91ƑŞÅȹ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161152.248107:+0000',
                                                                            '20210910:161152.273851:+0000',
                                                                            '20210910:161152.301449:+0000',
                                                                            '20210910:161152.324057:+0000',
                                                                            '20210910:161152.350145:+0000',
                                                                            '20210910:161152.368675:+0000',
                                                                            '20210910:161152.387049:+0000',
                                                                            '20210910:161152.404481:+0000',
                                                                            '20210910:161152.423179:+0000',
                                                                            '20210910:161152.442181:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x98ǣ?ʅųЂШ͵lԭŀƾˡѳΈʽ§г²άȹƸĕɖďǓӎʂƟ1',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͷ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3611746784605196873,
                                                    },
                                    },
                            {
                                        'name': 'ҟ=ļԑĶҌóԢӫіPРӴԢú|ͷ[~ʋүΡӃuÖȋͼı×ԧ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161152.989712:+0000',
                                                                            '20210910:161153.009716:+0000',
                                                                            '20210910:161153.031591:+0000',
                                                                            '20210910:161153.054073:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҎŧÓɄΓԏӄǢƫʇҢˏҌǢdҽůΉʩʈӜʋψŅφӢ=Ģ1ʼ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӂ\x95άƭϛȖɼҜųʘǞʶЮӷǋҩǕгґľәƓÅЙƋŽʑɩýĖ',
                                                                            'øƅȎ\x8dȕɓ҇˄ЃˬˬžÜȪƯƸˌg˼ȉӼÛѼŕϨ1¤Ҍҵѯ',
                                                                            'ÿҫТ϶˲ǏŎϸё\x8cԮѲһųϚŝɌӀʩɮӎĦҧЯĬŝόыѕģ',
                                                                            'ӱюĩӤǅʸеŶʨÏǐǣˣŵʮŝѯΣ\x8eɑаʮϬĵɖßˮ\x93šө',
                                                                            'ѣͲ¤ƇĝӼӚФɭɑǣdνнөʍξѻ˭σ>¦ƴ˳·ӓɔӺнͻ',
                                                                            'їԈǗԮyэěμǑ҄ԀϩɏϕήγαƚԈԫŴmϜƔ|ÑʱԢø$',
                                                                            'AͲԁԉӄ*ǋſʏӋ¢bʴ7ɭҕCίNӛӬʂҫ\x90ӘѴ˳ҍéŌ',
                                                                            'ɁƌŸӆЛŐӴԢ҉ѩƛõԟϩǏɒÀİЕ\u0378Ǻ%ċ\x8fӕȶҙȺЖƤ',
                                                                            'ΎқЩŉɯΌЊÅsƺĒԨŕªƷŬЂȞЊE˞ӝқʧыǒЫÆϰȳ',
                                                                            'ӽÙļ¯¤ŗӮ]ŘǬȥӂˋӧϦȥÀŸЈϢūʦƤɭȀ\x84ŞЍԂʃ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϡŮѧǨӆƒҼ\u0381҅ŷȚÅȗѣӽ˰ƠƟ˯ӟǔž\x81ϝўӰÉĢȚό',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161153.428141:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƬĲ»äѬȌΜ»\x81҈HǷū\x9cЅԐυ\x94ĿϼƚАԑ1ĚĿΓȒƶЮ',
                    'message': 'ˣ|Ӝ}Ҋή{ӱʹԂȎ«hγȁƼ\x90чNʽѽƔѤȿûƫѥʂѹǹ',
                    'arguments': [
                            {
                                        'name': '¸ȵӚΟɱ*ŗϠҾ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2636853238442000039,
                                                                            -6449941485995689786,
                                                                            -4938070897102691610,
                                                                            -599436808879030478,
                                                                            -8794516344131165060,
                                                                            1524481695200053822,
                                                                            2530205800462725680,
                                                                            -3239275719525376351,
                                                                            -4485195569160176539,
                                                                            1939228046239323221,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ύεɥʝ\x8eħƌǤĎΧʂδʕƣӮȉЫӷʩsӃӨ\x8e2˱\u038bҭȦőΊ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7673580587084000003,
                                                    },
                                    },
                            {
                                        'name': 'ӤϵѬEjϫ\x7fӛÞ\u038bȍ҆˻\x85ËЯЙӪʮΦőΙӦʂΩȤяʏƭü',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ӎъϧү\x98ʈƭԊΏΎŮӺƙȠ¸Ȁλƞ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -680981063057777161,
                                                    },
                                    },
                            {
                                        'name': 'ЏѿŸñɪ҉ɆĘѓƑԨáѰō·ʔѤÜӻ;őƍӯƓ\x84ĭԫðɡԀ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '0ӋϕĴ˃Ĺ~]òǄµӐҎҶԋƂäǓŐάǹѰВ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8506244647424983738,
                                                                            5169723140731109538,
                                                                            -6513392040241026231,
                                                                            6699698790069339468,
                                                                            -9010782356957311840,
                                                                            4267159315209255224,
                                                                            8736763997216270058,
                                                                            2777559094507067380,
                                                                            7878475673690437509,
                                                                            -7496464220412436676,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΖʲϬÞˌҥӕʌˆ\u0380ӹɰ,',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161154.509868:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x98ůѱÜƳʢPч˒ȫѩĔŹƓҐȺԁѳà\x94Аk¢ɕð9τҥ14',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161154.601071:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ϗ˰ƤÆӬģҢͻĸň',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˌ°õɳԨǠFЦƼªϧüҮɟΥЕӨӗ(ȶìԈѱǼƗΨƵϷӴʿ',
                                                                            'ӞƨʆαpŰ$jүӨӨ\x99ŧʟǈӇҒ˄ÞлƔԍƟԒ˨Д҈ϰͱʹ',
                                                                            'ǀ\xadƪďәĭϿαĶϓЮсăѾÏȺӐōåҕ˔ҼǻbӴϷʣǉњц',
                                                                            'ѪʼҩŅ˶Ƙ˂\u038bήӄß\x92ͼƊ5ÉӍдʧƞäӰу¯ĞԡƘŰjϺ',
                                                                            'ȋԆ.ŸųǧқÂ9v|γ˲ȚˮɎԁǐ\x8cϐɨƯƌɭƖǹ˯\x9cʜ˲',
                                                                            'НoɵшŅƕ·Љщϋνɓԧˆæɥʳ"ӳŁӋœӨˌӊ˙ΣҀȚҵ',
                                                                            'ϨRϤ¥ЪɒӐҖÍГҎFӽ˳ƛȦԞ¤ҜŚ`ɄҝИѻɝ˔іƨõ',
                                                                            'ҹŖ1ÊŠoӖθ\x8a˩5ҟͽ{ǟȥˉuӟŜӬϸӝϖԅƞӋѦȼd',
                                                                            "ēʃҨþƥяȍИ˳ˇͰӐ8ӼіƻľǻϵҔʷҕϷе§Ҏ'ґĊɴ",
                                                                            'ΐƔźɸѸɶɓųĨǶǐʻ*Ô\u0383ɢǝѻʬɏԃӉɹϘƕ¾\x87ќЖe',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѧΈԇİĊЊjԝΎ\x92ӱÎЁ~ĎѱƋϹµǏŵĒʔˡïҪǅȡȍϫ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΚHʛǠѮKǔѩǄĨÙʁӝњǩiɌџӵcōʽǈʣ»ǅҗ\x7fС˲',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʬ+ȧѫҷȚ\u038bńïţ\u038dŠâ˖ώBҖӃϸԃʝØ£ӆӴƼѲĒɆї',
                    'message': '½ԚΨѮҥҠŁɨƀƀʝvYӟ˫>Ѿɐ\u0382öʭҦɐǥɆԁ5Ĕкŀ',
                    'arguments': [
                            {
                                        'name': 'Ļ\x81ƁǏɩȑȔĬƫÀђЦȵцӺΨvƨ1ʛʲҚЙƶ˚ǜŉĖˊЗ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161155.268495:+0000',
                                                                            '20210910:161155.311300:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÐǽpƁ˨ǨȔǡŠƍΙ#ąҳӣǒӉ˺ĠˆΦˍϵơp˝ϙҁΠ¸',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161155.520980:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÊЗ²©\u0380ƟɑÚHϢşƆ¡ēʲϐӝԭCϋJƦɥűӐ[ԢӪJ\x91',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161155.603728:+0000',
                                                                            '20210910:161155.625054:+0000',
                                                                            '20210910:161155.642286:+0000',
                                                                            '20210910:161155.659660:+0000',
                                                                            '20210910:161155.677925:+0000',
                                                                            '20210910:161155.696017:+0000',
                                                                            '20210910:161155.714384:+0000',
                                                                            '20210910:161155.738056:+0000',
                                                                            '20210910:161155.757130:+0000',
                                                                            '20210910:161155.777306:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÒϕűǵʆǶŹƌŝӼʦєѸʮщPkƜɭ˪ȪĞňαɀ<ȶɆƈƇ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8126885944065930989,
                                                    },
                                    },
                            {
                                        'name': 'ʨϢ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            855018.747538217,
                                                                            519498.5699101252,
                                                                            89818.15332269893,
                                                                            616530.1825866301,
                                                                            621113.1398474424,
                                                                            708458.3962418344,
                                                                            964232.530325602,
                                                                            302728.5051646924,
                                                                            251312.75685760158,
                                                                            -60110.07600096331,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '΅η\u0381źҟπʿ\x8aǅƅ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˼\x87ξҋ_ʫяʛʓЫġȰàǥǆŎӻӞԬǧè²·˾ƱŪƬѺ\u0378ȏ',
                                                    },
                                    },
                            {
                                        'name': 'ͲԢɳΊ\u03a2ӕϏЉѦʹΧ\x8f\x97ƍtƹʂҌ@ƓδЃвζ´\x8aEйʢ\x97',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҒҐԫѩВɤҡԅǺԁʨāmvҐƭƨϚêӑśÆҪΰˢŇӻξɍӬ',
                                                    },
                                    },
                            {
                                        'name': 'Ȋ¨ΨΒΫÛťωΦϱĐӧӊ!ѶĐϘƛ˅Е˾ξ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7554169469386049324,
                                                    },
                                    },
                            {
                                        'name': 'Ϩ˯їʓ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161156.482761:+0000',
                                                                            '20210910:161156.504034:+0000',
                                                                            '20210910:161156.525629:+0000',
                                                                            '20210910:161156.549144:+0000',
                                                                            '20210910:161156.578016:+0000',
                                                                            '20210910:161156.599624:+0000',
                                                                            '20210910:161156.619595:+0000',
                                                                            '20210910:161156.637594:+0000',
                                                                            '20210910:161156.657188:+0000',
                                                                            '20210910:161156.675324:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʞΑ\\ďƘǚÀҢ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4611484469633823475,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˒ʞӦȓɴɑƋ¹ıƢԡϪÑЪТM©ȋǭǻáƳǦūŸ\x87ƑĸʣϾ',
                    'message': 'ӸŅʮԣӫЄԆƙśĈ˫Ҿ\x8e6k\x7f\x94ϻˏӦ҉ƾ\x9eҌȼ˨ЬğĠΛ',
                    'arguments': [
                            {
                                        'name': 'ѣŪӌ×δѭϧπ˚δҕ҇ӬҏªƺҿĞȸÿ\x8fҒΖĵ>ͳōӺàȾ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'ɀΜ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˘ˢҤӥÁÐϥ®ŷ˦ͺǟӰɪAįŊ˂˃īʒtÉӿ\x8aƅҮŕь1',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 237814.94448127825,
                                                    },
                                    },
                            {
                                        'name': 'ϤԐ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ÈjÐbӡƠҟïƫĐӎčŽʺҎЅªώưɡƐŞ©ʟȭγЛϖͽŕ',
                                                    },
                                    },
                            {
                                        'name': '\x9dńŸҶÀóŀĒϡƋÄςʐ+ːĨìƼNǢԙ˼ԬӖșӾʧʛÞʏ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\x7fϭɊ\x8cԩ\x93ѦVѽǻɝϏΗȤӚƓɉŏ¹ɔł\x8f!шɺќψɸǚɯ',
                                                    },
                                    },
                            {
                                        'name': 'өĲ(ΠʓĀȵǀƗλӂʋЕүȆơ²˥ϭΰѬҝŠΨҲΨ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '\x8aωìʴ÷Ӫ\x87ʳ\u0383һϤ1ɄӹҮ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7925571023886013112,
                                                                            2943999270451005408,
                                                                            4128307693316641388,
                                                                            -7272598396695462655,
                                                                            -6340049958801812194,
                                                                            4157293689281485297,
                                                                            -2105447070376376421,
                                                                            -2125850380191614568,
                                                                            6130920096549172108,
                                                                            -845071448239996311,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʍ8èǣїӲȈ\x8bȍƞÐƹϴОӸhƬ\x7fЄӊԕɽΤʏ˫ϔѥKƍ\x96',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161157.905209:+0000',
                                                                            '20210910:161157.931078:+0000',
                                                                            '20210910:161157.959145:+0000',
                                                                            '20210910:161157.990352:+0000',
                                                                            '20210910:161158.014087:+0000',
                                                                            '20210910:161158.036798:+0000',
                                                                            '20210910:161158.060461:+0000',
                                                                            '20210910:161158.085173:+0000',
                                                                            '20210910:161158.107222:+0000',
                                                                            '20210910:161158.128937:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Îɿӗ҄ȍòǙҽɪƳ\x84ͶϪqҰтǣ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1380909667500067224,
                                                    },
                                    },
                            {
                                        'name': 'ºϥԋϖɄʽмÏ)Ї=ǄAЉӣҖъ#',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161158.337708:+0000',
                                                                            '20210910:161158.354867:+0000',
                                                                            '20210910:161158.372124:+0000',
                                                                            '20210910:161158.388611:+0000',
                                                                            '20210910:161158.408237:+0000',
                                                                            '20210910:161158.428995:+0000',
                                                                            '20210910:161158.448891:+0000',
                                                                            '20210910:161158.468105:+0000',
                                                                            '20210910:161158.487521:+0000',
                                                                            '20210910:161158.510647:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ÛӹӈĐȼǗϬ\x8fŎmȖǎŞ҉ŬyςЃПϰʐǳы³áΔƟѿ\xadϐ',
                    'message': 'ŸȐΈӖʠϼϠʬѿŤ˻ӋɿÙıҜɛϦԝȽ7ǹΌӝԜ»ЈϷлŀ',
                    'arguments': [
                            {
                                        'name': 'ȅ˞ǈ×ԖƜ?Ǟ\x9fЪǇÓҵӍɬĆɦťΝӌǨɊЗζȌĘ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161158.689393:+0000',
                                                    },
                                    },
                            {
                                        'name': '6ѭ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 694407254142555962,
                                                    },
                                    },
                            {
                                        'name': 'ҠǶϋŤȸԦʕºC˜',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6990760265314419953,
                                                    },
                                    },
                            {
                                        'name': 'ʁӅĘЍŒĨϘӍ˳ӑҢǝ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161159.079726:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԄɈЯӪ"ƹрνĔʲùԓϡӊѻȋʱԍzʽʿ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӣчԙa˧˯ыбϕɼƉӺçɵǦÂ¾ҙUȮʫÚ˩ѥëѝ\u038dêΥ_',
                                                                            '\x8aȿϚυƠжɱ´¿vԬаӡʸŸҸȓʉ\x90\x82˽рǁ\x8aџˡĽʒɝŤ',
                                                                            'ˏԞɻƦШΧȗ\x9cȂиɦįĊƛ\x86˭˭\x99ʈ҈Ɉϻʩӳǣԭ\x82ȦҙЋ',
                                                                            'ǻϳģчɤчŗӺƩƅțœ˭ϊԏИ\x85Їӎѵϵ\x92Țŋ˲ǻӦЮ\x8e˙',
                                                                            'ԃ~NΘΑѶǇ˟6šӈҌȽÌƶéʕǖŷтζӰП\\ɬƑ\x9cӰȣÈ',
                                                                            'ɱԣΘƿΖqÎ҈¸ˎҫ:Ͱ˯ĪǜԇЄÃӓЪ¿ѸơϿTʳДʒ\x91',
                                                                            'ǒͽ%ҌǅɧȁƓʝǄÏƈԈɧŮчÈɢă\x85ʼέѾ²Шʍ,¸Ζʇ',
                                                                            'ĵ¯ȒƘҪЅΞÞ¤ʶϊ5ƴԅċΆǆȉo˨\u0380ʴҎŮѰ˴ŅýˇU',
                                                                            '˰}ц¿ÞɥǂΝ\x97΅οΐÿ˜һ\xadЉαёŢƍѵαȕŰćƅɌȪu',
                                                                            'ˇºêӱІɦöЃԂ\x96ƞńњȿőѮв\x9cѮ˨ШƹЄÚɺɨǔ«\x85ϳ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÜɽĸдʚÅǧαŤғϪВŧȁƒԒ˫ŔăȃĵƻҼН\u0381ȡʶҖǦð',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            241777.90723669692,
                                                                            233243.834051435,
                                                                            254697.85675176792,
                                                                            397925.09140350594,
                                                                            632593.3536132135,
                                                                            967234.236031852,
                                                                            825121.3951188623,
                                                                            410357.1136358204,
                                                                            254228.91730241483,
                                                                            899510.5013203896,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɳӬzĝPϕϴӆũȤ˒ȡχǩȧ?NЀȩ#ʔηϣĐчōԋȊϸV',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            738215.8885972735,
                                                                            283254.1434821317,
                                                                            161738.21128907154,
                                                                            492914.69728796533,
                                                                            420634.9406238636,
                                                                            372762.5720346486,
                                                                            351713.54748301103,
                                                                            204378.79299607006,
                                                                            694674.1821106392,
                                                                            797570.7353978413,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'őЊфϤдљлҺcϦ\x8fЛϭυÛүè˪ϹɗҬ˝\x9eƗŕʏoʶмϱ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7869527131522089310,
                                                                            6554394168169679006,
                                                                            3350504089245104906,
                                                                            -521051283747074606,
                                                                            6234611506565326424,
                                                                            -8607058429392052932,
                                                                            8999614681865268533,
                                                                            -6764407969839441893,
                                                                            -6347161650209194853,
                                                                            -7777633497279496193,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӌ\u0380ɲЎųƸԫӻɓƫЭ~ɽхԩȝɕQʹǶȒ˽ȥʵ\x8f˶сΉϵƋ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            269886.0569299052,
                                                                            181339.27194867615,
                                                                            674298.5389305705,
                                                                            -44541.72111037956,
                                                                            583215.3121709818,
                                                                            -79817.1090504649,
                                                                            222854.42627127998,
                                                                            958970.7589134292,
                                                                            477945.9824752422,
                                                                            11373.387892960935,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϒрЃǢƶĭ/ťϵͷљƸєˁ˨ȟ7ѫƟʛɧʜƋӀѡυɠԄйƐ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԄѹѕӚѵãԟ@ƺ»Ѱҋӑ*Đʋ˕ИΨѥЬͷÛˍ<ϴŲɧȔǯ',
                    'message': 'ϞԪŜΡϵϳΊѫǘ˼Уǡ·Έ\x9bŁӱińÝѾ\u0381«ÿ˪¤˲úʓѨ',
                    'arguments': [
                            {
                                        'name': 'ŜƁϑɮĐӎдȯ)ĐχTЀɆʻ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            813695.3870024655,
                                                                            395116.54727791244,
                                                                            863219.1355762533,
                                                                            779570.9452870706,
                                                                            703072.5320272268,
                                                                            868933.9555721945,
                                                                            16211.66002555417,
                                                                            140871.984350452,
                                                                            424503.61282513244,
                                                                            221999.13206724107,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʽ\u038dϭǬԆϘ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\u038bΰɼʈ±\x94ѳƀ˰ӨйlĬƵƊVï/+ǥȓΌɽȵҼ\x98ԔȠ^Ѥ',
                                                    },
                                    },
                            {
                                        'name': 'ƚаѧ҅ȚĜŴƣȇɫͳǀʹ\x9fӫȋӫkŘƻѯ_ѥԊǕĪӸ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ѤοәҬЬʤ˫Ҙ\u0379Š .ѴΛĐǾķҰϒΏ6ĕМԄoʚ˛ƊԜǒ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            792847.6377523317,
                                                                            59003.08323356864,
                                                                            759546.430038491,
                                                                            288302.7030942022,
                                                                            644122.637773137,
                                                                            591049.670380101,
                                                                            665935.0117352344,
                                                                            82174.15539098805,
                                                                            596333.3847668822,
                                                                            551083.897889426,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȾȫãΗџɏȢӅxɰ\x8b',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161201.721086:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƏƹƮ%˪χҍƺƃˑȍ˒ЧӰҁȬ΅ăŁǦΎÐ˟ĎҾ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            703412.172003537,
                                                                            32697.79210181441,
                                                                            753264.3191450466,
                                                                            839079.4195214896,
                                                                            785533.6765565748,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѓʥʔӳĩ}ІʧѵηѦҁ˥ТХПãѺą\x9bÇʡϥà¼ΧХѩӕ\u0381',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2104095856125490935,
                                                    },
                                    },
                            {
                                        'name': 'Ϋɽ\u03a2ҳʦ@ǘΡǿʑӦˡžιņÒɹӌğʣǤҽʩϡйÏ͵ĘF|',
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
                                        'name': 'ŽҭyƴţŮ&ÓſдЩВ˓ҡΰνC»άϿΎ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'äƂѨɞøƿҷΒɯ®҈ɛ×ҢõĈҧ:ΏȟȶҐƪǇȠѵжˁJv',
                                                                            'ůӃԇϡˣϢπʝʇκԡťŤЙσϕ¬ÑÂѺ\u0381ӰõmȀǛбȧZȈ',
                                                                            ':ǍˢÃ©ԉɚӫÿҭъ`ȎēŦǑŕξãѭÔӐθƃǦԚª¸Ԩȁ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9bıđӪŦ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȟĭӥҷŴ˂˥І>·*řԠ҉ҽŇǰϱǚƺ҄PʎȖбϸҁǙɵ\x86',
                    'message': 'ćGтӛŷǴҦɗƍχҎψĞ6γҨÒŬӧřǎрŶƟϜƺř˜ѠӐ',
                    'arguments': [
                            {
                                        'name': 'OӢŹфĔ˵&\x99ѩϐԞǂƛȑŃɾʪ°Ӿ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            52132.86031220594,
                                                                            162139.4471723952,
                                                                            712314.837193022,
                                                                            547793.131259294,
                                                                            857448.3335294623,
                                                                            864114.3815149781,
                                                                            411057.13821906346,
                                                                            971575.2368138982,
                                                                            -98129.74506992596,
                                                                            307724.2205508583,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЩƝäзÊϻąίɼԣϸʟӐæʱąƴьɤьüŞΧœ³ȇΈЂɅ^',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161202.975785:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ŒƄȤ\x9fŹȆ×ʙͼğȧȿĈƷÍǸӋ¨Ŏӑњͱкɝʵ\x86ԓϼͻҏ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            940135.6729511382,
                                                                            -58737.725356073635,
                                                                            289722.52244591207,
                                                                            931706.2909459205,
                                                                            987741.7831910753,
                                                                            453337.6848087625,
                                                                            696969.7697218255,
                                                                            147481.24065415235,
                                                                            639390.4449014065,
                                                                            537454.1715454549,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӑĮñɋΣŷØȈ_ҿřïԨΥИҰȆϰ¡ұÎϼȤɋȜưĪȳ˱ʜ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161203.350329:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƼʄɚэХ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            703108.3036682776,
                                                                            494530.45407024515,
                                                                            496100.680279133,
                                                                            295277.20342160354,
                                                                            787113.4546290645,
                                                                            20086.476493554495,
                                                                            605614.7583655309,
                                                                            249179.29020054627,
                                                                            382960.73546883615,
                                                                            575193.117177639,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƇЪӫҳӶѫĶîƀ(nџяԣаĦˈŔ҇γɝǠ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2574241828152983700,
                                                                            7690713831928707823,
                                                                            8231720329292647462,
                                                                            -4508706427083074783,
                                                                            -331152969958819056,
                                                                            6011931196747777019,
                                                                            -6161843094344911480,
                                                                            6508041947351184835,
                                                                            3289014568855665447,
                                                                            4893836073935291293,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϽΑϞĚԉˉϤS¸*˒',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6912938210119084170,
                                                    },
                                    },
                            {
                                        'name': '¤ž\x8bʎЎ´Ȁβϧ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ОҒŕŃPťʷ˹˘˫ҙΞŠÓƉԩәелԗȴĊƁüͿǵԓе\x81ϑ',
                                                    },
                                    },
                            {
                                        'name': 'йήǕɷȆӯũʂҾƌάȡ\xa0ʱҸˇОƪȏƻˀԗAАÞϽĞ˘Ηύ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -3596.7884607023443,
                                                                            -96577.53996874436,
                                                                            882201.2912914129,
                                                                            542909.5980448906,
                                                                            142605.68248448332,
                                                                            268237.77326854016,
                                                                            877745.9028154708,
                                                                            110203.7831933435,
                                                                            879370.2120447097,
                                                                            441993.8092861619,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'åӶĬŦǋǟ&ԔµȴɼϋБ\x80ϖϏ˦ӨȎȒÒӡȇ\x9cɓԋЎòЛ@',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˜҃ƟаȍΖ^Ґéϊ\x85¬дėε˹\u0378æǟĔƦǇ\x82ɍйгǤȭȖҡ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҟȣũȔӴβOɄeȭЄ\u03a2ӕzӻӯпϔҧˏӳӓ¿Ƣ0\x7fď\x82ʰƥ',
                    'message': 'ʵǼБҠһƛΤ´ϊȉʇӐэ-ԌˌƶκÉԘk˝PӀ˾ɽ·ȍШӼ',
                    'arguments': [
                            {
                                        'name': 'ϥʕǁϳϲoӄ˛ƘгРÃКsÈэķļ\x86ǊÕ×ĂӤƐʞЦ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            871118.7583245428,
                                                                            148200.98310214747,
                                                                            804724.2586264716,
                                                                            113928.46864023592,
                                                                            269069.3206825705,
                                                                            916037.0848932978,
                                                                            -81456.90631439077,
                                                                            411672.28533426306,
                                                                            250392.4629664545,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԜҺũЎȣμӃȦ˺ɲ3>ю˄ŽƛӲƚѡ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161204.846171:+0000',
                                                                            '20210910:161204.870500:+0000',
                                                                            '20210910:161204.892274:+0000',
                                                                            '20210910:161204.911215:+0000',
                                                                            '20210910:161204.929196:+0000',
                                                                            '20210910:161204.951036:+0000',
                                                                            '20210910:161204.982182:+0000',
                                                                            '20210910:161204.999671:+0000',
                                                                            '20210910:161205.016807:+0000',
                                                                            '20210910:161205.036898:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΩǸӊ\u038d˔љʑă\x98˓ЉӰʭъˣƊАȴƼʬϰӄ҃Η<ōȢӖŇƥ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
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
                                        'name': 'ήɴϷħ\u0382ΝqʌйȭӻȲ϶¾ăǰ{ŘҖɧƮǀ˵ӫǗ˛ӖЯſѫ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161205.412737:+0000',
                                                                            '20210910:161205.430306:+0000',
                                                                            '20210910:161205.447787:+0000',
                                                                            '20210910:161205.471569:+0000',
                                                                            '20210910:161205.497645:+0000',
                                                                            '20210910:161205.526893:+0000',
                                                                            '20210910:161205.552097:+0000',
                                                                            '20210910:161205.572782:+0000',
                                                                            '20210910:161205.594666:+0000',
                                                                            '20210910:161205.619234:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǻʋ9\u0379řЇǡλбφқԧȾӟƐҲǢ¶ӯзƽӤРʸȋҬ©ɕOА',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161205.719514:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɖ)',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161205.799450:+0000',
                                                                            '20210910:161205.818845:+0000',
                                                                            '20210910:161205.840417:+0000',
                                                                            '20210910:161205.859294:+0000',
                                                                            '20210910:161205.877345:+0000',
                                                                            '20210910:161205.896257:+0000',
                                                                            '20210910:161205.915722:+0000',
                                                                            '20210910:161205.934699:+0000',
                                                                            '20210910:161205.954619:+0000',
                                                                            '20210910:161205.974521:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƑϰѿƟ\u038dȸâ҆ÎȎĴŜɽȔ˹p˃ĆˍŚǈϤʹωĺˏàӸԢ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϝćˑǌɬŕö˯úˍȍ¢ĨҚŌӻύm˃Ӹň\x9dɘђϬʾԠͷsØ',
                                                                            '\x91Ɂ\u0379ŪʲÞӣ˚ҨΧӶțĪǎőѩϕȡȡѭг˄VǻȁкԚƂӟˠ',
                                                                            'ǇҌѫʗҷˮ˪čӱûΜѼʐђǬƠSĦÔԖƅўͻѴ:ɆԢɦÂȅ',
                                                                            'ӮƝғ>ÏԗѠɸүÜʦǋÚoºgѕɮ҅ҿʞȃ-ˀPϲаχӌ\u0379',
                                                                            'ӗƘӁƜǑӐʟĥ»EɳϏ#ԤȬ6īƀӇϖʼ\x97˄\x9däϋρR¥Ů',
                                                                            'ӈ½ċƌŦ˕\x8aƘæϢɢϋƦɭ¡¿cў¼ϝëǯȞӫœȪɶ˯Ϥх',
                                                                            'l;ûѬȩ˅ǟȮςŽ҆щҫŽϾЉƊіɰəĵɉôҸҺ[ӻŲѕÃ',
                                                                            'ǕdŵˎǶɊfˠЉ6ŻɀɳƼʑƉ{Ө\x92ƅ\u038bȖԇŪˣӸӬÃτʔ',
                                                                            'ÆțJЌѫʨΔ\x88\x8b ОԬНҢĠŃfəȜɢ³ŏŶ҂ѧ_ĹєΫр',
                                                                            'ÍӸΧǦӷ\x88Ǖ£Ҕ҃ȈСЍˤѷr!ԨʻųϹϯƏ"ϱϙLϓӆɻ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϗŗǾχĐÍ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:161206.348163:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ͽʔǳϱχŗϸ҉φΏЊϋ`ӷ˘Țɲʟʺʖ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'tƠԤ\x8dȢЗ^ȩ˱ǲćЍɈaѻѨ\x95ˇƜʞԔԄҥɦ˖ăҩÐŻƢ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1267225748175546224,
                                                                            -3491437660039713750,
                                                                            2188256700704766830,
                                                                            -7068914889839612578,
                                                                            -4747210065871390890,
                                                                            1540963605171391718,
                                                                            -7478811539019756926,
                                                                            -6711147101055188533,
                                                                            -4684823618636925753,
                                                                            -420733045753223528,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'vŐӳǒћϠǅ¸ȎŤӀѤгǦyųϿԣǐͷϊЏ˦ϻCĊѼȑſ˙',
                    'message': 'Эôрǳіʬђў_ŷDΔĭØτӜɟѼ÷ͱÆјʹ¸ҜzԡˣȺѶ',
                    'arguments': [
                            {
                                        'name': 'ΟȺҭȊԃǮҚë',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            912538192075597480,
                                                                            -1857566745798885646,
                                                                            1297080830242787737,
                                                                            8779207955895410040,
                                                                            1145822317643557099,
                                                                            1478683297999813498,
                                                                            4543880673668178954,
                                                                            -1218210279616907351,
                                                                            -1944535307265286069,
                                                                            5169335510212161489,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'żԐHҮɥΥӊŤĺʈÔƤơ5ƃʦѥӕŅě ƙȰňʷŜѫǌÒƔ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 344612.67422184086,
                                                    },
                                    },
                            {
                                        'name': 'ԨĽΐɉ\x87ȿԡ˽ɴӏΧҖԪƾDƾŮ_ɺͳ˼ѫԠęήđ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            141134.4910957142,
                                                                            540324.6050274003,
                                                                            359707.2108462585,
                                                                            -58284.083154896434,
                                                                            877930.8234344394,
                                                                            62971.27443323779,
                                                                            804118.0379266156,
                                                                            -58070.88842957664,
                                                                            652101.2993996562,
                                                                            -65163.18668461656,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Jͻ`Ȝ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            987649911616312890,
                                                                            -4333471223215180886,
                                                                            2415403287610274037,
                                                                            -101890711913232980,
                                                                            8097289686943334853,
                                                                            4768727134019462263,
                                                                            -2780940101832959646,
                                                                            4031244576562060952,
                                                                            7441573048972987094,
                                                                            -5474732593317651488,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'δƓòţ˵УħoȇKǯҤ-ϙćӒƼЛȓ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1222228500006151736,
                                                    },
                                    },
                            {
                                        'name': 'Ɣ\u038d\u0378ѸȯΧŬʮҕОʆÓшЗΥʖLԅĵʺ˜-ŎϚѤӤ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӎȫѡŻʜҩʊԏ@ÿγӝԌЮǞөĉ$ȏЧ\x8dŌѸwƫǽù\x7fɷʦ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƚвͶĎʞˈɸȨƗсġĖõχüĽϬВ;ņǷή°ʎʖ\x8cԬǮ҆¾',
                                                    },
                                    },
                            {
                                        'name': 'ҕǯϹ_ʆϑѩß±φкìӊ΄\x97їԘˮƠӲƏϝʣǛxƇʔʙ˅¥',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 658001.0339443872,
                                                    },
                                    },
                            {
                                        'name': 'ȞŭРˏĆѓСǖЦӵʜƶѰҸыTɋƌʭŘХˣÅÐşxǖ\xa0Ϩ\x84',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:161208.581086:+0000',
                                                                            '20210910:161208.613850:+0000',
                                                                            '20210910:161208.644892:+0000',
                                                                            '20210910:161208.666906:+0000',
                                                                            '20210910:161208.689377:+0000',
                                                                            '20210910:161208.709234:+0000',
                                                                            '20210910:161208.729748:+0000',
                                                                            '20210910:161208.748730:+0000',
                                                                            '20210910:161208.767263:+0000',
                                                                            '20210910:161208.785533:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȺƁ˩ÝуνđʫƫˆϫӆQ<ӟ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8599541412612419346,
                                                                            2545787793417473202,
                                                                            -8698105965213951979,
                                                                            3996884898348819910,
                                                                            -9042378047684328645,
                                                                            -5169475394109353312,
                                                                            -446381755926674311,
                                                                            -3205794847822936471,
                                                                            -578079325217302219,
                                                                            5768875268055116152,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'd˪ś¼»\u0383ʟǞΠǔдʵǊ®Ƶѹ\x81ğțɞӒˀ˥ЂΜ\x96ˍϿϛɾ',
                    'message': 'ǤˢȕӼ+ʉńķϻŏοϕӉʂśΡȀʎǐƚϼғƲԇԀ˼Ů˥ŞĊ',
                    'arguments': [
                            {
                                        'name': 'Эӊх',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 11341.505160170767,
                                                    },
                                    },
                            {
                                        'name': 'ǶԙφǙҿԂȝţΝϻԟʠęҡĐ˶dӶч˜ӐϧŬ5ûƁǧӋξŗ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x80ȼŸɧ0&ԮӝyгǥˮпѦųѳҜĮύʒ҈ÅʿȖĞëԨѲȔƨ',
                                                                            'ϙ\u0380ҵ{ΟNϖâϭĘǿЗҍЇȴҊ˲ӔIϟҼ?ɣďkуŁĆϻƌ',
                                                                            '\x93ȱCҰFһ½ҲǈǕ˶ч˧Хҍˉāӫ%¹ӋĕҮӯċЛАϗӋʾ',
                                                                            'CϋŌȳȷëƐȤƾLƿơҽêǣӡŜ{ÜʽҔrȭј҃ͷЏ;ơΰ',
                                                                            'NĎӪ\x85sƏѫʴӶӺωɞϞҐǅєēɒˑҿПπɍӮȲѤԡgщƧ',
                                                                            'ƷɘǁƬдȉĤ˺ӿԃÁùȃǟɽԅȯɂԢǚѱ˴ĖƻǣƜ\x83ӜӮѦ',
                                                                            'СӤөϐ"ÌϻΔЯΊѵʹȕv;ƕhԤbѭɄԕзɆč˩ϵӛʀЊ',
                                                                            'ͽìĺȻDķԈĕıϥeΔҊЎɔȃċйĀĴϝӔЅōĽӇƕķпƏ',
                                                                            'ʌƱΣҶЁϣшҔɃԄИɚˈɽà\x8bűρ˲o\x86ʂ\x99ӱҡчȏїΙI',
                                                                            'ǀĘοɲȆƄĢpԌϹήҚǋI¾ϯӬЫԀʧǐԐĸʆҗƣĔʅ҂ώ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'μ¦ѐk˕ҁԤѬҼƵώό;ë;ƳʏӿĴҎƓǉϹ˖ѵԖǪÙυƅ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 295538.5308099855,
                                                    },
                                    },
                            {
                                        'name': 'ŦѯΒҩƝʩȋ\x95йҐ˛λАҔѽǐȫӌRĺϻΙƝΧ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 890084.4468370791,
                                                    },
                                    },
                            {
                                        'name': 'Ńҟȩ\x8bЧѫSşԁР\x86sŌˑũɟĞ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            848373.1630519311,
                                                                            627950.166920725,
                                                                            772433.5920101578,
                                                                            216335.11085240694,
                                                                            483640.0948623265,
                                                                            12687.323397318309,
                                                                            -14112.548417870974,
                                                                            255558.2141116832,
                                                                            715904.1104549827,
                                                                            637881.1835653856,
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

            'identifier': 'ԗǧˤϨĬ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'ëԈ',
                    'message': 'Ц',
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
            'name': 'ɑїԅс¥ґʸӬыШϼԍрӞĝýƪҪȩqѿ˟ƙγҶϢJϳȸþ',
            'error': {
                'identifier': 'ƾʲVšʳơΤÐ҅Ğ\u0378ѱǡÕѦŹёӎС˪ˑ¦ѺĘQԛΌɣгӵ',
                'categories': [
                    'configuration',
                    'os',
                    'internal',
                    'internal',
                    'file',
                    'os',
                    'internal',
                    'access-restriction',
                    'file',
                    'invalid-user-action',
                ],
                'source': 'Ώɂΐ0ԙ¡6ԔŚǒˠ®ĐΧ˾ӽӊƟЩ\x8dϷʦ\x87МǷÂĻҊnȤ',
                'messages': [
                    {
                            'catalog': 'ӜŜĦʳҥŇҕɄˉǞԓҹŝˀȷŽЍ',
                            'message': 'ӒˣȘсǂƚuĵʼĖϩȋHёȻЋȌЧŰͺɪΈѻҴʤ ˓ø΄A',
                            'arguments': [
                                        {
                                                        'name': 'ΉйÖʹϹ˯ĹοūþĀŠʙɿĄҝΕѾƸӀ˥ēǍΕЊĮӤɰƁԤ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¦ư\x97ЬΎ¥ӘϨŏШˠԐЧΞ\u0378òʕǠ΄ЉYöʌгǋҦԏԍǮ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -77896.89981388475,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɤ\x83ҢʺӘҁԊǉӾί\x98lƳ˵ŊȁϓζžƑMҷǷƗϨ҆',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΣȤʏĪƍѥćřƻǷҕŮ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȋ³˘\x95îԈ\x8eǞѓʾȒŲą#ϩ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӱь˭\x84ą',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ζ\x90ѩȊǘñѸfԤǅЇ\x9c\\ƟωȄlѸǬǣӟųɕǅĔƃǭ\x84Ͳё',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЁęүɆÈDŔӦѠӻɸϴƧǾљҒ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'āčèjçһʮēχə˪σʩʙƩůӶɏĜΌŜǈԉɇѝ¯Ĵ\u0380ɧӒ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7241799890480457861,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǕːѮхɫҰњ(Ǉй˺ңȘʰʬÄ$ѪэǷϧÿҢьëʲɩ¡Ϝү',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɣҋѥƒĦĻȫˮď˽ǒҌ¯öɒ·ØŉMӫȴϭǈΐԂҾͷƘŚ҇',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ûΠƱƓŻԃѦ¹ƉԛҮӭЦҟ˞µҀŨũƈĖŽƙˑʼǥƩǌƫ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161142.360249:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ŻUƝËΖΔш˫ȹĈȽůӋԎȈ\x94δɇ=ðˉ]ȦэӟŖϊήĔô',
                            'message': 'ǅDϢɘƚµţåȻ\x8bğԛŵ\x95ϟÈ@²\x92ʘ˓ǮˈѦӵʱΩѮЈĳ',
                            'arguments': [
                                        {
                                                        'name': 'ѪǉЬ\u038bΓǡыˣƘĥȆѾϕėӋʙΰĜˇ\x91ȎʨƲƯɣӇ\x91ćKӚ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѐʞЄ˪ɘ;fƸȘʅѺӯКҳNџҒzЮʪ˩ê¦цäũú\xad·ǔ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϛɷ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'эˍȎγȣҡˈ\x81\x85ˎìǔΉǱчƯ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'έԩӚcɩЩλĥӧƳԤɧƼЂҿ\x83йÔ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7102587491066694760,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɸǃʡ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'r',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʄø҆ \x89ȁ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 494279.7733303973,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʕˆϺԠȻ\x98',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'їʣä®ҧśт\x8cжӼ˨ЅƮ{ˑTǐϠԧˬʨТИǇm\x86ûœǮӂ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Њ҄ɶԮЇÐԎƥɚ\u0380ˇќҴºщɽˎӳ`ßе',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӦţƲǕѻ҂ӀɝƖū\x9cԪѿŮǉсʴё҈ɒȐŎɝν˳ȶĂͿE˼',
                            'message': 'Ω\u0381ϡϓřΐӻҮΡǆƨĘɴĥԃCÕŬǈПΫəΰѾ˵ОԬӦɐŲ',
                            'arguments': [
                                        {
                                                        'name': 'ʕÆǽ˓˻ЀĴ Ѝ҈\x87Ëϭȥʒ\x91ýŬϬЩԃȤɆʹĭƻ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 369651.55800324696,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Z˦ƴė\x98ʩ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǣ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӓ÷ǧqю\x8bǉ1ͿРѯ{țωΗȍƊÈэűʡҼҁǣŶƔөԋӦԢ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĴǠǂϠƦǁ\x8b³όϡϚʁ˹Ĳ˺˦κӇǆ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ι˥ΌχƄɬȼȗʀ\u0383Ǧ1Ӏԣ¯φКΓɤϳϯơ˃ԬϔZȫɃ˟Ѭ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӬĮʸӈǻ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 215435.16343673767,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x88ʹèɹrϨПΎʰʀψˁ˟Ӿƈ˼×ǝŷüД]БʇˊǤėӂƢ˽',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Pϱ-жԖˋЯ˟Ⱦ\x97Ӄ8Σ\u038bϮΓȘƸǀɗӈĹʰˌȵüƩǽõʻ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'IκǲŅwΉŋβĚzˑŵįp',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҮȕЏȉşǴʽѱǵdөчƞ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3965428727011679760,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǲɢȳƚʫΤƎԥ·_ӡĖʁПԙєЃǒʉȲ˳ψù\x9fǬҙөϭϼξ',
                            'message': 'ϑԥűyňǉɰ˰þԨ˙¾ç˵\u038d͵ȥǘӛΒsˇГʿϷϔŻкèԓ',
                            'arguments': [
                                        {
                                                        'name': 'ȭϊҜ1ʙˬӲȾМM',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'čӈØІϽ\x8cϥʔsЋϻƊԜǹ˧VĶϋ\x8bϴвÚįȡȽǁŎǶˠҍ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӕúҔϥγ;ȩɠπóӣҫЍΫԟ[ɚ¹Ǉ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȬӺәǗ\x9cԆƕȓԤIƙŸöƘΠíӷɜȥΠӦʘɽǡӿʍПŦŀč',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӟſ͵·ӬАоӴʏκ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'äЪіȥҬòӶʡ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'αҖӎ3²ȏΕкłҜϏǅѢͱі¦\xadˬ˳ƹúVĈЇŹιӼ˞Αì',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȘԨTчБСŋù¦\xa0ҤЕñ)ЄǒȬƜΑǭȻȥ3ёȼȡīťŉƹ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΫήǝϏě\x81ɘǨħĪȓψΩӂĐʲӯɔќȰӾŲ¼Ӊäǰ»ƉԮŏ',
                                                                        },
                                                    },
                                        {
                                                        'name': '«pЙФϵрɕßȷÇ\u03a2ʜԑåÆƷ3ϑѷ\x92\x91Ң>Ɉ,ǤǅǕŬ|',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x86нřäĴ\xad&θěø҄ţ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÛʓѨZю˸ѡñӓҞWƛ\u0378ɅԀĢАŕɕ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 540734.6629292438,
                                                                        },
                                                    },
                                        {
                                                        'name': "ŜÐƅåǕÆϜɐͰƎɔ'ĿǲԄķӞҩˍƋšÐқƛОĿìʗũѾ",
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˑ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ιοНͲεџʋƐҩ˾ǐUӮԖɄĶlʼƏԩĥǘʎԪϤϛʐϸӌȅ',
                            'message': 'ǚЖωãɋˏŰƚǎѽŵѻãÄӛϥϷʤҿӏ҃ӝǸz҄ѽΒӕєг',
                            'arguments': [
                                        {
                                                        'name': 'ɞǂԧ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȳkԭ\x93ǌ\x95¾~ϛł\u0383',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĊŀԘwͲœ\u038bӉҿH˙ǃ·ʍǑŚͽЪ\x96ʌòǻӑƮ·4ы˥\x87ӹ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'νԮǸ˩ƮǝΕ˸ŮҝǠ\x80ņ±ΔñȫʠÚωǢȒһÖ\x86ǒԠӥˣѱ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӍǱѧԋԦĔͺԞǚ\x86Ԛ\x86ώșǶťʩзšʤҜǰίѣŋЮȥәZ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Сδ˕ȚӐüˮѨȔԍĞϐԣÀǋġŇцеĄԋǭҹÙѮŖʽнϸ£',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161145.648681:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɘ¡ԦһКϑɨ\\ğЃҙӁӆӶ!χлŊЂѮɗđďĻuƺƖԠÌΙ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 839845.3523360275,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҧ҆Ѫˇ҆ľЁͱрȧёҶқˁҐ\x8fȋČϴϾӄԇϗРP½ʏȒϱĳ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161145.813955:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǉңÂƽʔΐϬ9ȬʗŔɨ҂ÅçŞρʳνϗЀѩϺ°e\x8f',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 427074.24880326795,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȝҿç\x80',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'яŻ\x86öƆīƺùүEÑŤhԞϸСʔĲӯɮќĐƬѵƠ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': "IАƋȌĦԪėҸґГ}ÊϟΝ˜əɭȵҜţĿˤӪԈϳӰҺ'Ʃχ",
                            'message': 'ťӷď\u038d¦ΡццŭɭΰЫɒϷʭΞԓяĖ0ŌÂҊQǕȄLƛ1ŉ',
                            'arguments': [
                                        {
                                                        'name': '\x8eŰƹȪ?£ѵ~ȪˡȄTʧʌҁҐʥǢ\x9dё˞mίɕӪŪİș',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 825277.350696024,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҮƇ½³ºĲԀ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161146.574382:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'õɇŀǈρy˙żðƘɯËųωӝ ŋĝǝҝE˓Ǹ~ƾξԬΰåҵ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʞƽОΣѤÚȰf\u0382ΜӚѴͰҊʫT\x8dæā˾ǺǵƃчϾЭ˅÷Йʲ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ųѠdrЯʢ҂ɠӵҚȗXʞʻƄшʀҙˑ=ǎĂğ:ÿĢǉҮӁɦ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ųҙőȦȴ\x88ԣȻ\x8eǝĆ˓ƍ£ԤɠӠӥ±ӚғɗʩӈϽǓήΔԘˆ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 558224.8118453458,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x96ɵҰέ˒ˠƫʠκz',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԡǭɩÁԚђ˫ŏʉūŃφńÕТ\x8cпҙĠ´%ǶƏ\xa0¿Ңє:Ƒť',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ͱ\x93ѧ˨έж\x9dǶϧŦˬ˃ӧϖрů\x95ϕőȅǞё[\u0379ΖʘЩōâɚ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŹıÏЂiОɳю˼žƞ3џ˔ĦʮԜљқˀҀ<ǫ\u0382ǹʉʃ\x95,',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȄƿƚĄ±Ȣ˾ӊHҥŴƕьʃ˅D˷üğʢͳӘÇĥϐÇӁÆФɦ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҕ>k˒ԊɫĻˍКϟôʙ˻ў˫ưЫӚСÆĆȐʭҒ¡¡ƦӂǮƱ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Lʖɜ£ŻϾϿˌνI\x86ѷКԔʅǐҟǫɈéҊЬΤάƀНǤΜ\xa0ó',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8eĖʦϚßȯǠơ-ϐ\x99iÌǡ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3020452168065105877,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѷǾƃ҆ӬϗÝΨҪʣǩʥŘςŝӠѻΠʫȬӤİɬUďΎß\x97ԕģ',
                            'message': 'ĜԇӠѕɣˮÙЋӖњɂɑєПӌрΉǪϨÒƴϺå+ʌɇȩɸßЙ',
                            'arguments': [
                                        {
                                                        'name': 'Ćҽɡ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161147.395588:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '"ʇΧˣ]ǔ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɫȄĒ¬λoϚ˧ŸMƓԞɯĔĩɴФȀʛżɶ˜ΉӪɄҜ¹ȷ\\ъ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 251213574719930011,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɿƝʺѵεƮ҄ʃßӇҊǏ¨πʆJȚ!φƺų˔μǖθˬΔɅΣ҉',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8741146883839402132,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԋвθω˪ћĪĒǏЮςÁЭПŕɑ˲y¼οșĢɯҏπϞŨŇΙ&',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˸Ļ\x97Ҭ\x81ɠӻψʅˌ3Ȟǉ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ХƊԖTǏюƊӵč\x8fуƓϛӒĞÜďŽÙо£ʹˤжӃƥ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '҃ȕʞԃũÀӽòʪЄŀӵЦ˓ɬʯ˱ɄӌЄԓɩˢȮԄȷɴΏǀĔ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ıϭÝϬӛǓρ´йŇђэϴɽ·ШΫǻŃǣ˟ѾɺɚУ¦õʔαc',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѭќͷΞӜԤØʁȰ>ѕҔКӟƦΎӹ\x8aˡʾӛԞԈS\x91[λÛçѲ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǾĮƶϸŘԁӻ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '!ƞ˪пɷАϑӍːҼӆϔːДʪƨ˱\x87ĐǠЀǟіԆӼʣԢŇƽ˅',
                            'message': 'ЮǭǖŦȦТƪɯ\x91҈ƊΡȦǖҜUӺſɔɑшχɷ˓ԡιԈъ\x88ʄ',
                            'arguments': [
                                        {
                                                        'name': 'ƈȜΫǭνӺѓѤŲMľ\x95ў>Ћţ\x80bǓ\x80ŪĢ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԙѴԢƂɫРʪ˭Ѩѐƴѧ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϫǨȻԣȰj\x92ƒš\xa0ԧ\x8cʃɿұďËзΎ\u0383ǹ÷ɌԠӷoƑӖř\x90',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϡȌ2Ázʄ¤ĖϦ_ɳ^ÝЍӚúˋ\x823ÖǃѿИϭÄʰŭԆȪʀ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161148.399030:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'RϢȄҪјѩîѲ΅ɀʟӮŵ#ò',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƸǴӳϭƑЭЋϋƱ\u0380ǌЮҧʸЊɜЭûӔǍĂάƠȜ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԫПĬԚʓӷåʵÐȖǘ¤ǿ«\u038dʻѿƞ¹ǸιϠҚʲĢēͻЙԬɶ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǒǐ˵хͻ҈ƧϝԢƙæɕǛ7ņBɤ¶ʼƈӦ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1130442492820354522,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɇtǫ+ҙşȋıȨŘԎƁʛφͷțіƧǉѦ1҄ԋϯӮӾПWȲΫ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'óӏŪϬĆÌɁЧǐчǐě¯ŧєăаɒ@ņҶԞҋƅҞ<ƤӪӜЄ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -58371.66731667647,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Gǰ}}˧^ʢßчԢęˮ(˥˘ϢƞƝʯĥ\x86ƺκ҈Βɥ¸ĀόȞ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ŕǆʅ˥˯ЉϻНɦǹϚǸ/ҪÑɄ\u0382Ӹʘѽµƨ©ë\x8cɹƜŊҼʶ',
                            'message': 'ȤŉǙζԤǚoњĲҭŤ\x9aßƿ΅ìͳɔɧ´ɭɁпÜ\u0380ʷʧõ-ə',
                            'arguments': [
                                        {
                                                        'name': 'ǳӛʤπ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6309661184645058037,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӇºЂϦSӲȮɨƑoЋϴӹɅϱʧйӃϲlģŔεĜ˸Єȕл˛V',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʁȰʵʈǷɦʪƈӋӺϗ]ЎϻɴϧϒӰʌŜҧƗΐıӨ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161149.336639:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɟӆԭʬƎϥ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161149.409840:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Țǈ¼ñɾӄʹƤʟʢǫ\x8fʓҢвΛ\x82Ç»"ƕҡЃӹϞ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161149.482839:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˇˮԉϔζ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'æˣ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǢϬͷȂQǘõȬˇžđ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˁӧΝV\x9cΊǰʟƎрЄ˪ҹΥ˭ЏҴ·ҳǩѭЎ\x89ƳʠЂ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2743706039609360385,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÒҐǢòi#ǠѫԓУŦΕŚʈҺȷЏӲттӕ\x93ǌyɲμȥǍёŚ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʚʤƓѝʮԙȝΰAȘçΒЅЃ\x89ĪFĉԗ˘¤ÍςɣŪхбºǠӄ',
                            'message': 'tԬĩчɓѴԒϻYȔԀв˭Þɗɼҭ˘ҼзҚӪԄōŧӜÊġmã',
                            'arguments': [
                                        {
                                                        'name': 'Ĳлэüρ«Ɣːϛ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '1ʚʲ˂ѴEӎ<ɯÌя£ζĆǃΑΚ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 384124.1136965557,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԞӣΔě\x9dƁ˛ҦκŰo¢ȥыʞҕʡɡHƚȯ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ûıѤŋ\x8b\x85bʨɾʚӰ~ϣѰӲO˄ҷӆǼΫӳƃ«`Öҟż˅ɤ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŅˠˌœҡFȏ˲ҾґԈҞӠҺÂɹЧ\u038bŔǠЧşȯʧǶǾԀíҾȼ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 602744.6636546798,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʉԂье[Ӊʰ\x89ҷ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:161150.489434:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Śɧðy5ӞÙ\x91ˑɔ\x93ѻȝаζ˙ȆӲобͽKӛǰʐýʮуƔ˭',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '!ƠщǸ|',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x88\x82½лǂÕʄåhћɠΞӟƲȲιôǮƪАĔƆԠh®¢тэ˩Ӂ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ưƈ˟ΈљЛӿoƋÑĄоϹǼƅ',
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

            'name': 'ϚɎk',

            'error': {
                'identifier': '3HϕĝȦ',
                'categories': [
                    'internal',
                ],
                'messages': [
                    {
                            'catalog': '\u038bԑ',
                            'message': 'Ƶ',
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
            'event_id': 'ΐѰȼZɆөҚɇĺǛ\x95£ǑС8ǙŖ˥Ԯ˄ЏӏȡϲϖӈNɈƗǯ',
            'target_id': 'ƩĞȶ˩άҥϔšƪɝӘʲʭ\x86ʈĤèӏϙΡǨŐε˵ńʩЇΦʯ\u038b',
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
                    'event_id': 'ˮΰȜѰШ˂ķ˟μ\x85ЖӨʌˣѮμǇJҕГЅӸƜÀżάɿǙyс',
                    'target_id': '҇ʣԏԏΒƙiɘɤԥĦӳĲƙȉ÷ψӲʂ_Ϣ´\x8dÇԜҐğФɝЬ',
                },
                {
                    'event_id': '¥ѩʛɠëŐҎҰʴȚğ˝ƹ˛BɬӛΆԟвɢэå˸ʇϕ4μΗƛ',
                    'target_id': 'û˘ͷ!ȡϤʾɓϔÄȬɢџǺҦȁԒԍɴʥҿӹu{ҶȵЃ-Ńʳ',
                },
                {
                    'event_id': '\\KɱҵнƏҪζȢƆȏȖо\x89ҜтҜяʵȩ¼îǹZűӑή2ƛ\x90',
                    'target_id': 'ΌӌγľʿŒӓˮŬžґ0íɪKyʚәÚƂĥ\x90үÓƶΪԗӶʉғ',
                },
                {
                    'event_id': 'ӱЮͼȖΕӏĖɞļ˽ƶʗŁɽPĞÕ˪ʒǟ0ɓǿͰʗВºшǠ5',
                    'target_id': 'ʌÜɗȒҘȆˑ;žπ˫ǻθNгÓoҽƆȆƭϻȿɲѽΎӮ\x90ɖȹ',
                },
                {
                    'event_id': 'ƿ҇±ΊƽвѰӂˊԄɌӖ%˓˷*ѽԐąȍхăѢÐĘҪȿpŚ»',
                    'target_id': 'ӪώˀŢӆĽΕƁIȬƿҲ°Ңƒš¦ΛǧȑƪыҚƈ¸йĆǮǌŏ',
                },
                {
                    'event_id': 'ĴΒªǆΣФüЛȾZǁЊёҁȁ˵ǉʥšӳԝԎ³ѡÏ·ӡŖӥӭ',
                    'target_id': 'ȇΜơѩΩ9ɾϽЅпlť˭жğԂǆӲĻӁӤóŕβîʁ\x8fâέĄ',
                },
                {
                    'event_id': 'ѓǐϠÂԪöɸðʖӁĨϐê+ǪĬAτbԀȳɚÏѼė¼ҹiȣɻ',
                    'target_id': 'ɽ\x94Ēϕуɿɦҡ"ȣƑύĚǏӈĩӂ\x96Ø˕oƏɥĽəȕũȉαș',
                },
                {
                    'event_id': '\x84ǕԔiǹΎѥȒҔ}өƑӥóØӘȝψɒʽЈү˄ϥ\u0380Ďвƨɼ϶',
                    'target_id': 'ͻ÷ЃұъńȇǳŹɔʛϒɫèAĹÉƕϑǀȬȀάĪàjaȑŤȭ',
                },
                {
                    'event_id': 'ɫʟҺʮŽŉʸΥÝǖέӱĂħϔ\x8fåćZ.žʂÃ\x94ҳWŶɻÈȖ',
                    'target_id': 'ǁɧ]șΠ}ŲƁДˉɔť\x89ùĨčӕϑ҃Ԃ£ϟԩɗƣƝυғɂƸ',
                },
                {
                    'event_id': 'ηҔԑҧҎ҄ҸƴИȭʩнνӒԨЅЌͿĮ˔ϱҪŃӐӛkȓʵʮƋ',
                    'target_id': 'ȴԩãċƽƗЃǯŢƗΦϮ˟ɕk\x8cќӔSҸƣɒʊžϬƋҽҟŒҷ',
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
                    'event_id': 'ȝʽmȩЂȌ˼0ȏҁұӤȺ˗Ɋ«ѿlѠƷĖЫϚ¨ϻˡǒŶϜӂ',
                    'target_id': 'ĚãϨɟēҙԭӰ75}SҚҌȘĮƋЮʯ҈|ÜԭϚOӤҙί϶Ư',
                },
                {
                    'event_id': 'ȡΚӕƪѺʢÞρԊӕҔŢϗǑϜCǃÒнˏӈɧÚďѽʪǻӳ"ɏ',
                    'target_id': 'ԭȦúѤȣ˯pԗκáϺŷƥΖАžÍ˶µɰЄ)õӅȆäăƧɔΐ',
                },
                {
                    'event_id': 'Ĝ3ÿɧǎļʘχύГŘҥѕ˲ґѨȶХǫѝġˮʹšÁҵӳðџȰ',
                    'target_id': '˽ԂƤǭɦǢʽ\u03a2ȩҨÞñV˄ëËΠ˘\x90ъѝɖIˆӆЩ{\u03a2ɐȥ',
                },
                {
                    'event_id': '?ƄԦǍαз4ҍ˵ѕ\xadҷџƠСɤĥĲ˅ϬѷȐ˘ɌŹįű˚ѷˊ',
                    'target_id': 'ԝȮǑƖААёȐǶѭԇȨьɆПǆČˆRԞǕɢÙκƿνȧҍĴȘ',
                },
                {
                    'event_id': 'ƐґЙǺŦʼ©ĨӏӅÔԈϫŞʣŨϷрȒȏγԕÝӯѿȂʹɡҩˈ',
                    'target_id': 'ǎĤϊā˵ѕŢή%ʹʉʦɅȇрšɊӋѶƦʍTԑ\x89ĦԍƝQӤЄ',
                },
                {
                    'event_id': '˒ѩźˁԏƠϴ͵ԒϋħÚȆҟˌΑƟǛºҐˍʥрӰˀǥ˘ȻȞԮ',
                    'target_id': '\x97jҔʱʄǶ´дáæǒǠКϚϻƫsɯЎѹê\x81ɓԑ¯σș\x97ԙӈ',
                },
                {
                    'event_id': 'ԓƊʄҐOШӮÐƌѾ˥ȼϛбɆ˽ÀεȀȯBɡ΄є\u0380ʒҁʪϴ˲',
                    'target_id': 'kќŧӷФŎìɷǦи·ħ\x92ʸϸӂʐϵԒϪ\xadʭɎWжϗмÆΧƉ',
                },
                {
                    'event_id': 'ǔƦ˥ƝЌʢ÷ǫѷѯxŅŊƞĜȀēzТ°ƂɌƿǅКğǌєǕш',
                    'target_id': 'ʳӿǭɅ/ʓăϗά;2ȑ»ˍˆɁԏʽλ+ѡΊƪʉХɻўϥǔĠ',
                },
                {
                    'event_id': '\x8cҊ9җљԖʵͱӞȝÍΥʳҊƛʁԆӇѧĒˉʺ˓Ûǣɻ7£ɇ¯',
                    'target_id': 'ϡǁÜԂΨα¾C*ȚĘӤûҕԚϠµҨɑĹԩʀǶєʠ£ӉČґĴ',
                },
                {
                    'event_id': 'ѯʤԨɸʽDŚű˝Ӛɽ6¥ſƥҴȑʐΡϓXʶӶψĿʬĴĳʳɊ',
                    'target_id': 'mϖĠÞíҾϽӡŃЄºſǢäӣКȨͽ˴įћɾɦŒ҅ГϠůŃ˖',
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
