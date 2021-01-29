# GENERATED CODE - DO NOT MODIFY
# Created on 2021-01-29T00:26:20.578610

"""
Tests for the foreman module.
Extension petronia.core.api.foreman, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import foreman


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
            'action': 'ƐñΔҼѕрŦȏӆ\x9dұ»řԓŜΐėтĴƃÆԫπӼОÔǉś¤Ơ',
            'resources': [
                'ɰ\xa0ɬВЄ˳ͻҺͲȚʧˆΉbΓғƀŚ\xa0/ǹѩԀŅĶŚԎB˔ɣ',
                'ϑɚԍƠàśҭϔϣѻԞȂŘïʅ҆ƻ-φӝǂ,õӇɑѮÀãёď',
                'ɆΔǾ%ЫӓRһƪӵԮұ˦cǉҞЈӨӰȠÔʆ\x83Ќӛɉ\x7fмȗė',
                'ѽƚϩΣãɭſИÎȪˁǱEG¶Ұӡ3ɅѤ\x98˧ԨɳӭѶöˆ-Ԭ',
                'ѦвȨϦ҈Țĺϔ˕nϹŇΪȻѭŶ½ˡα³ƬQŘƋӂUȗxȬŦ',
                'Ŭ7"ǊӃƭӷʕŕȳȳʞ/ĴԙҗuĎǧȋʢҔлӜöŗͼ˴Ԗǎ',
                'Ԡĺ\x90ĊYѸfňąͶƂΩɖͿϘ©˳ͶʨçɳbӉʖƌ¸ȔѭȄΌ',
                'TЬ÷Ίԭы?ӁӺöR˝ώѥϮЧɲҢ˷Ԭçц½ıҩѿ4ҵ\x8dĝ',
                'üөȀƕǺҫ˟\u0381ҭԄťŰͼɶςвҥɢȋġ@ǜɛÅ¸ξʟĘԃ˚',
                'ƟԟδҜ˾Ԃʙ"OǥɎòʼϕǙŧʯƉζїȜσєȐɓɧŷЅƑŐ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'Ȧ',

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
            'name': '\x81\u0379óƟÐǌɠӶ¿ɕ\u038b²ĳΚʹӌοӻӑoºßԪƤѭ˷ҸoӹͰ',
            'version': [
                -6956696604396104635,
                -1594891864534641917,
                -5601394911010932654,
            ],
            'location': [
                'ԌКƀҪΖӐҜǎ˛ɘҺK5ǭɰтҲķ|ț˵ѼÐȅǨˬЯϭҍ˞',
                '\x9fɌȸωǓϴƟԓ϶ǳӗÞɣ°ɲϸ\xadѾ>ԤʸԎϬ®Ƞ{єŻυȜ',
                'ĒʦǒѱōӲћӝʜȥаԗӔҒĥUŋɩһǥþŨyҏèȸӅMӻ҆',
                '\x8eƭʠ·ϱwŲ˃˖ǹǻ҈ЉӫғчͲ҅șʷƢ£ÖΥҀӍɳėʎѕ',
                'ÁŲʟĴɒɉɑäŘüэNŬħ´ċѕƽҽfҁԟƭұǰŠžľ˂Р',
                'ˇĞȰÛǄЗ-ˮÝщÍŽ¶¿ҵƻөіҥˑƽǓbϿ·ŲºϲƢӤ',
                '˜Ȱįй˖ҚÜ˾Цϙȍ˷ı˩ϴɯӞûĕжιӪǃǥɄľĹɀĆS',
                'ˏȯ˟ÞȞǹўɠћζҪΨʌԈì\x9fƝҥķСţ$ş˛ŌŌѰˌɭź',
                '|ΟԮŻɐ½řʆɈјЙѩ͵ʋƍĹʻȾӯʤ\u0381oƯѶŻǃĈˣӳǤ',
                'ЋԡҽǘΔKH˫ËƆʱ8ˣxvĽłϫƹΛПӟϟˇʕ\u0379Οɨyȝ',
            ],
            'runtime': 'ԆÆѩϹz΄ˠɌʣɦĮЉΞIРö½ɥԝ|`ĜʣĩςRΟѼ\x98д',
            'send_access': [
                'ΝԚτƖͼʉЗƟŲԖˤʦƸŐϪ˦ӟϯ6ɕǢĕӊҶӎρNѻӽɡ',
                '\\˻ωӽŢǷԞЭҬԃƳʎØŵĩĵŗɧȞɏʬҔЬVԚʶѝÀ҆ѭ',
                'ƎǱϤɏԩʷʯŝъȳǍτŏșėΡ΅ӿǈƴ˔Ċ˒ʼďQČɳJӆ',
                'ϞьΒ˃ĭǁіħЫś\x7fӰҰԩˌѠɿәґƷќƸέ[Ŕԧ\x8fσ\x92e',
                '\x86϶4\x9bƄʩ\x87ʈƭͿ\u0379\u038dȺƦœБ˺ГÛȞûǴŝϐǜ˩ɖƚðƢ',
                'řɉƷǨԈǇԡӿǽɖϝƤ ŹӮѓƼΠĀßƽҟþԬΜȨźɩѩϦ',
                'ŮɎŕhǼʼɄōɫȣ(ÚÕҟǙɅԚ΅ƩƙӃөĺԣӳϯʐÙʠǪ',
                'ʾXӰĈȍĕʞʺƜĿċǢԅų\x86ԌˏȗƼСϫСʾɟΈÝĞǏҀƢ',
                '®ԫ,ȁê\x83ĥʏɷ',
                'Ȧĉ\x7fʐɟʝϮϊЍқ˲ʎԉOa\x86ѿӵԝ¦HEʎŌ¦%˳ʂԢѢ',
            ],
            'configuration': 'ƣОԢΗԞȶӷЯȸǽӗӋѯӸŐǮʛʗıäΰ<Ţ¢Ԑ\x94ɯͼƣƱ',
            'permissions': [
                {
                    'action': 'ӳәȝȮŖΜ',
                    'resources': [
                            'íY˯ӝƠȵάÂҔ|˽éHŠйѷȳȃq\x92ˏȵ5ûΧ¾ȏҕɿ\x9f',
                            'яŤòƜ0ҚnХ҇ƪɝƿ˙ї¾òӈяΚɔʗĶ·ƈҀ˘ʻɡԬĺ',
                            'ҪǻɺҾЎ\u0381ɣāӝɻλαωɛ2ƥ«ϱƊθˊӥʃŸĭϩԞНԤΔ',
                            '9F·´hѣσԌԑ\x8aҚΟÙʹy˲ˢɻʫǎ×˚Ͷ˓λΩʺȀЩȩ',
                            'Έ"ѭ·âƻɘпˣǿƵҁµŖϛ?ԭƆɪȲ!ƼǜȵШѲǜɸЊí',
                            'ˡĿSȋЭżϏ.ŸǝǲŜȤŸɎҟӑϲԤ¬ŅȼɆΧěͶʕě;ð',
                            'ƝΪˠċƘˎhȂІƥȝӐͲƾ\x84ъΎҬƁƚ˷ѪōԠƻU\u0380ĝƃŹ',
                            'ìƖ®$҇Á\x88ĸ˨8λяϣпǘѴÉӑ\x87ùҴҺЁԉōƗȎʮʮ˸',
                            "ǬǴʣӐȏҫǋ'ȵԋÝЂ×мÇʹϭǭϤѲū\x9fm҉Iɢ3(ͺƒ",
                            'ҫĦçХŔȟȤѫǇинŋƌʹќα˒ƄԘĎǡĤ¬ȩþΚȓ~\xadĚ',
                        ],
                },
                {
                    'action': 'ȝ³Ǳх˜ŵÖԓƜx\x8fΈõѪЉʸ҇рϖζζ\x8bƵӶӱЫˠ\u0378Ҏѐ',
                    'resources': [
                            'ʸӴΑӺômŵϼȩʅͻӘԃӄʹɹ)бԐBԤϳбқӹшԆ=_Ҁ',
                            '˽ůĵɖȪū˺\x9aƗĢ5;zôȫϖ\u03a2ʧ\x9dͲЄλς\x89ͿȺÐéӗ҉',
                            'ҘӴʏĪʂҔǍ×ўϙ\x95˟˕ģԘˌ\x95ȊжåѥҋØэєʕƆčÚӿ',
                            'ƉϖϵϖƿĲԡζϏ_ΟКͺĿ҈ԗɖɵØқǫίԒЛҚҨԌ8Ԑý',
                            'χŒƍ϶\x98ªdǱ\u0378ǰͳҖѮŋĭӣӄˮȄΠɋƟԋӧˮīƕȂʃԉ',
                            'ѨƘāʢļσǁҏψ¿ñĖЁӑÃȫȊ˥ΚTɮΛɽɗŉӿ҇ƚϮʖ',
                            'ΣDԜ=ġȼǒɬѣƟĮĩӅƒnӯŹeƥӊɲɲЮԪŇɛϰϨÿŪ',
                            'еɥƒԚ(ѐsӾ\x88¤ϥÅɝҳ˙ʍˎ\x81ǕFϘϭȠʁʤķѨ±ȸė',
                            'ŗè°*ѼßөбƅǊƓ[ҕǎӰĆѺҶƛȗҟƴΈϩh\x95ċѓ\u0383đ',
                            '\x86кĎDЏϢ\x82ÂºķҪìѪ]ĩĄǊЋɌɞӜЎɘ:ϕĩ˜ƅσŪ',
                        ],
                },
                {
                    'action': '|Ь§ȗѠȔƖԉʢ@ɥѐӉś˲ӋлƼ\x90ҰңϏʥƶ9СaēяͲ',
                    'resources': [
                            '(˝ѴхǢȶƗƦ\x85"ǣȢ×ȭΐŊɻǆÃҁɲәȮёǂʃ˄ȇΛҵ',
                            'ԢрɐʕԡҰ\x91ә@ПŢċ˽ǃ˶ˣȌƜÕͿʐƮ1ӠѷĲƒů\u0381Ɗ',
                            'ωЫɘҡ҂ɟѷĶEϦǟЇȒǢӸÙԂʠΙÃɚη(ӅŁΤʪȏȹĉ',
                            'ѢǉʶÉҋÅØı˨ɯеƵĺåȡŭԚҼΑȒƧϯ҂ѽ˄қƞŔҪʄ',
                            'ķΐɝƁƑƂßLϐʣ±Ѡҧȁ\x8aпԑϓϴПωȮсĶœąŖҬӝӔ',
                            'ˣϓѪ\x87Ϡe(тѦȚΤǺӿΪżĽӑˉ;ȱÅӕÅѺĪŦθɹϺϣ',
                            'ҚѝǇ˜ԖŒºŸžǳNШҖøПkӊ\x9a\x7fĭǁʡԤɹϳŸɐѾБԬ',
                            '½ƋDʑӻʓˏ2ЋӘчʂϳʐɷίѮԦρτǣɕԌʫ˫ѧǻß˫æ',
                            'Ϳö˅ɽӽÃøǱΣŬɛԇҜΜÌdӹϮˠЉǔπϱΜԈ\u03a2ɖԀ˲ӱ',
                            'ǉʔǆīÖĻͱǩĕѳΥͻщȴɥƢɨѫŃȘƗ\x99ϰńɈƣЪDļĔ',
                        ],
                },
                {
                    'action': 'ӕǶȭԑ˩йǾŎ\x95Ąuί½МԎйпӝɭӠºȤʯʄζѻH8ǍŪ',
                    'resources': [
                            'ˠӪѦԅ˅ΰƘЏʳǊůω4ǏʑŇʜƨʪΓ˻Ȇ*ԊęƼİȾĚ;',
                            '˷*ŃЭ©tƣӃϕʆ\x97ƺЌ˨ƖźɎίЬòŎѭ\x9cwԫȞãèΎ\x9f',
                            'kҨΫʔÝ£Ȥȯʼҏ\x8cͱɓ˕Ȁnǲǈ÷ґ˕ƩΉ¡ǹэĈхΎԎ',
                            'ûқɇчɔС˩αҋΎĪ\x94?Ũ˭εŎɋľӂDӮÎČǵǱѾØз˞',
                            '˯\x91˚>ӳϸϛϳoѸrԭˡìßəĄēӊӄźΚҒƌ²ŎԤԜҩΩ',
                            'ĮġúρΗ$ƒĩΌіɋÎӯӕԔƶëԄ=9\u03a2Ǿ˔Þȉʶď\u0380ѤӒ',
                            '\x80ƐΉ˄ĦӹȒĩʔ·ĪτĻуßϘ\u0378ʛ3ЯџзƲ;НгΪӟÀө',
                            'ȆŹȩ˶ӚǼ²ÓԡҦ0ϪʉԎкбϏǶ¦˘\u0380ÆҭВθӇȊєЮư',
                            'ϸϸʠīλΌӌʧӐѸӖҘϹӈ«ϓӕҋ¤ԨǞРơDŎʊΚϩѝ«',
                            'ұчȊυ\x86эԧɔϲǥāȡȔǡȲΡЃɐДɪˇƻˀȊˀ)ơΓYњ',
                        ],
                },
                {
                    'action': '°ǣβŀ!ǥͱʹūψGϞ¶ĕҵȢɣËІħÆЏɲѮ²ɺԫеˆŏ',
                    'resources': [
                            'ıчʅЂħɆԩɯŒɀɩɤǤӈī^ɛșˁ2ќÈӊˎ~«ЪѼ\x92ƀ',
                            'ҚĚǽ2ҥЇɝãҟͽŀņԜĳǖÏìˆ˅ѺĸӴˆ¯Ϋ$PɐÌΩ',
                            "ƈƮΊ˽ϡϰ'F\x96Σ˞7ԨăΓƂǺŋȬҊȞҺRЋɝʎĊүèƇ",
                            'ǱǨʧɡЊ2ɆȋӜƕɱȰľ˽ʐ\x96˫¥îҺеԙŎƝ˭ʥϭˍϢ`',
                            'ȴӻѝîѯЕuǃð˂ȁԚβĹұÛƌɟѬÜý:ȅӑǛ8Élȉ¨',
                            'К¬Ϯž\x88ΣǉҗƯ˸ƂÊĮԡɜȰ1ɛȩβϹè·ǀĀȆȤӠǓɿ',
                            'ѹҿȍƈɣӐɏϮʬʎɽΊӹ˳ŘɯѠўȤάõųŦÔҢ\x8cȒʻǙL',
                            'ŪÔ˓ɚˈɥhФ7ɥЪ˕ЈĈѵѝǄѕЦˡџǇҰ\x8e\x94ĳɖԥм˅',
                            'ѾȢЮŲƅʷϖʬƘ˭ӯʼ\x95ɢԉIЩԦɐŲӦѧɶӰƼΧǼŘȿɞ',
                            'Ѕ϶ŉͱɢˑƇҔϬȸҷҚÞµԑȉňˑɃʩ\x9fȻ˱Џ\x96пДӍӏ]',
                        ],
                },
                {
                    'action': 'ȩƕÓҨďŤњӀͿөӼíїčƔȸ\x8cԕǶWӵɗ΅Ưʍїӵјгɻ',
                    'resources': [
                            'ǀŹ\u038d"ƧƁӕƃşɕȀІŀɠ\x8dÞȗӜ÷δƭőɝ;вĜIɍʙť',
                            'ɈҮҙѾӈ´?ƁѭӪƋʨƖг(ѝF͵\x8bǧǹ\x9aʉėШмӖɚɡɭ',
                            'ÖҮĸϾƎǻцǠΩʹ\xa0všГːǌ҅ˢҫӄĊɽÅͿʇΦĂңǵћ',
                            '\x8dƃϏƴ}вΉԧǖЋнѣΔǳЂƣɭ<(ͽǧόƟҖϛ¡ԧѯяʰ',
                            'Ȓ\x89+ϥԃ˼\\ȑǲƷ҆˂ƉϭҋɵӟŕkŽ˳ʉУǴΒӜmѕӸ\x97',
                            '\x8eʬºʌ&ҒȘʫЋ}\x9dʓˣȃЬӒƨҺģÒȽќиͽϗҹƑWϺԆ',
                            'ώƾԌɶȤɴϾ˚Ô͵¨˞ѲҭυúxɯɏҮɮʩˌbř\x9bɜɈķв',
                            'ҍƉ҅ŀҺҕǋ½Ǫӝ)ѯѬи˼ӿĢԀǡϫù',
                            'ʖȂŹɶɼɺӉ\u0379¬Ҷ\x9eȀȐTѵȰҍԎ˦ѱѭżӬӕƱӖτ1ЗӸ',
                            'ʚԙ¢ͲȋǯDЇ-\x88\u0378ʺǸӕɄĒœԖĹӶŊǱĠȴªƐ\x80΅ʊӁ',
                        ],
                },
                {
                    'action': 'ʑ\u03a2ҔкπϮɞ¤ŽϓM˻ȓÌδĻϏϳВĮͰîʕю˘ƦƲЀЮŴ',
                    'resources': [
                            'ǀ½ǫĂƂӿşĬªȟСϱҏ˙ŻϘԞҌĞЕԗƘȆЮЉĳòҌ҃џ',
                            'ɁϚȫʨģŹ˰ҚͶφˏʐӽÅλ϶Ŀ\x9aВǖК±ӗżƠǱЋȣάΈ',
                            'Ѡ¿ѥϮǈ\x9eƣƅĥ\x88аċƺюѻĽЁȭʢÊѿǍΡϿøˉΠυ˕ѧ',
                            'Ǳт҂ǗœȣÃưʤʭɢѵ˺ӉČѿfВЩҢƾɽªˇɧӣуʐőɇ',
                            'ʋ\u038dɱȂЏҳҏ8ƽɷŜԑ˖ѭҝ\x86vҗwȡ\x91Ѯͳ˙пӛĤ϶Ѣő',
                            'Ȅ˓ӜĦǨϩǦĲQʋɞИdΉĳåȓ]έȑ¢ȀȺʯȭӼҀԇȎ˞',
                            'ŎiƯİǄíQ͵ύљȦƚŽҾҿЦēč£ȼјʥʥӖòϼӖϷ<;',
                            'Ϩ#\x84Ԁˇ¿ɑʌʮŝȎõϻˌŌѓ˟Ę˜σϔŸǂϲÅӵҰĪŝí',
                            'aĊ˸ԩǳYԐƩĚұŏȰϾʞȠϩ˳ǘƬԩΰзӉĮÀԟŎ\x8fĚȚ',
                            'Ȏϐ˹ω\x90ˈӴҳɕĠϨȅZĊϯѶѤ˕}ιВ\x88˷5¤ҮʅŦƘЊ',
                        ],
                },
                {
                    'action': '˓ӣ˾Ӫ\u0382ΜŭʌԐʭǓ˻ƑԆҸ˵ĜØYƪɮ»ǹ˗ԑЩҟӍȠϵ',
                    'resources': [
                            'ԣӎљxɰƺɾ\x83NӲϤɉ\x90ȸҙҹĝŕӔӌԑҠԧΧʜӟǝЫͶԔ',
                            'ԀϹʑÈYǩғS.\x86ԖħĦЈɏĪЫ\x92ĿȲǰ2ЇÚɇˑÒĸԥП',
                            'ѐԬɉЖ=éfîǚƘ˙ŧɹѽԄȘųƌÏȺðӒƛԘƎкȺΚөӏ',
                            'ɀΙгȰşŚʚΑǉѪZϴÉǃΘЦӾ˫ŭǄ˚ҊҦ>Ӡ\u038bǻȚŦ˃',
                            'ӗơ\u0378Ǔҽɢøʻӯə\u0379гǻõӸӪё7ћ҂ԗӲГŀ΅˶ȉ\x9bęШ',
                            '?tɠΰһǠƞѱɲӣȠ»ǧĽӋÆҏΊɎ¿ςϕѣĲӷɠ˓7ʜ\x95',
                            'ϤɥϰƔАӈā×Ě>õşĽϙ\x8aȩÇҖѠƦŽʺ¥ƕʱʍIǛȈҠ',
                            'ȏшӷʟ҆Φ7ãͻЭ˟˔ӂҕƗêɽɿЮ"ή˘Ͻ\x9cʟ΅ɰˁӢʃ',
                            '\u0380XѶăӋĺ!˛µŞʱɞʛω¥ԙЉЯЛтӷŪǇҫϾɸĂ[ɹК',
                            'ӭѧȁӋͺ§Ѯ·ӱĽpϖԨ{ʪϾӈϳ\x81ьЋШɎɊϊųπˌÐα',
                        ],
                },
                {
                    'action': 'ɫӐϻˇаԄљÏAȭԆљ˧ѺBїŢʦʾŧĶɴϯũΐ˵ÿѶ˝ɧ',
                    'resources': [
                            'Ȓ\x91µϩũ*˳ӗ;ΜӠ?ľϽӻсʎĿɌΫіĉɘҝɩʯϡ\u03a2˙˚',
                            '\u0379$ϽΨĖðҮɼčĢ«Φ\u038bяˑɄ4ÃğΣƻȞҫʴѴӘҴł²ɖ',
                            'ЖƭnǖѯhͼкҝŮũϸȼɌ˫қǨҧǵɡmμҍϻǱʲǉгVÌ',
                            'ǛɻË',
                            'ƤʖúΫˑұͰӯ)ʃîɛӝRοњɜ¾ɞƍɯɥ8_ʉβʛϫ+І',
                            'ЫBɸȁӔ0Á_ƀʔǏƍЈξɞϳО^ҷҋӟͻɋέƟϣШǴζҚ',
                            'ԖĚшqÕԨâҞ\x91Ŭ˭ɊϫƠ°,ʨŗӧХ×ΜÜ\xadaΪԑÒĐʊ',
                            'ƛ\x9eÊºǬÄȏ͵Àϓ\x9eЅЧͺѣɐHȄǶ6ҢŌ\x9cͱσɌ\x99ѶLʯ',
                            '\x87κӡƗЏïƬΒπǐľчѭÉјЎǺҿȁѽӾǨźʑÆΨ˃\xa0ξǢ',
                            'ԓ zі@ŸŊтÆіԌР˭Ǫԁ«ɠȂ«ŬëҎʫɮԍĽҭƧƽӨ',
                        ],
                },
                {
                    'action': 'ƞǨƲԊʂæň\x94hѽәσŃԧ˩¤ζɇªÇϫȇЀʸłǾǚ˙\x9cҠ',
                    'resources': [
                            'ΨҥƌϧǈНśҴԮȘiǯϛлҞêԡо¼NѨŻʳƢ\x7fĶř^ϋĘ',
                            'ԓАƤ˷Ş)ɹӷŚŕȼҿŒИʇƐέϡͶӐԚxǼąҶԜȫǠƫċ',
                            ',лЋнɗѢĠđ2ƥȖʃӄҸʣńČÝќϧӃOǺҥҲ@ƠĲѪЖ',
                            'ťӋ϶ƂǵϣƥȍɻůȖӣҧɨ!®íɉɸɣϐδ,ҧΒϼԔ\x91ī\x8b',
                            'ͻЇuǿ˥СƷəѕƹʐ\x8bыɟ;ԌϪzëƬǌèƖþŲɕΫɬCȱ',
                            'é˾ӓΊũӌӑɊůĞǡǡɡșɎzą@ɪϲƧCĩŻɛȴ\x9e΄ʮƚ',
                            'ȉύŷùҦǿӥњΨŸԮ˦îʊƃ=ϛШƣԪΘ˼ӎ~ѫ°Ǡɓ˒ɡ',
                            'Ӟίɕ҉όΘˈǰ\xa0¡ȑξƯӁ:ɄϳԂϫɊˑYљǵȨӂӎ{Ƞĳ',
                            'ҴΫˎñϦԃϳӱŴΚѣ`ѱӔºӺʕǛԘpѰΨϰԄɪǦ\x85ĤӮʬ',
                            'ǮүχɌƙΨƮź\xadËҼȨȵӐѲӫͽҟ˝Η\x90ъŰˎΧÉƶȗɡЎ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '\u03837l',

            'version': [
                -8704669702534653332,
                -8426078855561327343,
                -570236644809324693,
            ],

            'location': [
                '\x89',
            ],

            'runtime': 'ǂ',

            'send_access': [
            ],

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
            'name': 'ůɽƗȜŷĴdǍӬƕǈІӐȷ\u0378ǷўǢŖǉ:ƳŪϔΛOѡγcҲ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ɨΪҭ',

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
            '$': 'ӬŰÿ~ĘʌɴѐЪȇǯН\x9fŒʂĕѰ˦1ʪҬƁѥѴǌǍѹQĘƯ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 4892912642989857652,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 850082.0369362041,
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
            '$': '20210129:002620.496147:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                "ūϪÌŒʯǽƃűɇʽÝΥӛǀԕʖЃ'Ϙ˓ƖɇЏПxϜԟǤЍЗ",
                'eѾǓʎ1ÇҧѼƶǮγËЭѷδæ,ƅMǬӼȖ˽ŶɖǓZɡϜЋ',
                'җ\x94Ӡ(ο\x8bҮĢϩԋÐьƍӷ˙϶\x7fʾΌʰԛϦ{ѲϛɋςΖLͲ',
                'ΠʜхӈИ/uΛҠǁǝԀЉɗѯľѱǀČғïÜG\x94ȶȟɫьɑΊ',
                'ŵѕε<jά\x9aųЕЂƪıȒńӔɉƃ\x80ϔ\xa0ˋ&δȯÇʮʫyɬУ',
                'ƬĜώɻАăʲǫÁÁgǠƇӝ/ǭȊДͱʵє\x98Ď˽ˁЕNåʛǗ',
                'Сµćˍȝɜ\x9däͰ¿ĿĒΤʲšÍįӫϥԙʇҕĂ˯į\x89ϳ\x96κҏ',
                'țĲ˟зȉKcIȗ«ʹŪήPĮœΘĊν\x8eÚɥŜÐ¶ýˢ\x93Ċэ',
                'ȬԡҩЭǫϔϠ\x93Āȸ˚ɞɆǂ`ƠʍʑԤ0ǏƙħĖʬąʇìԁǕ',
                "ʄԀӓǊȇЕɫʅÌҥʂǏӖњͽ'ǦɘȅœǺ\xa0ƋӅřȬϷ<ÑĿ",
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -3444137639797380457,
                -5891948876800153952,
                -2251573892366512749,
                -6222935436008006887,
                -7099479981073705997,
                -835836590094496141,
                -7811400480005906470,
                7046102346305504581,
                945955588510086703,
                -8969458002725633761,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                176284.31353230058,
                924730.8629409379,
                798285.3066966098,
                284543.08259895403,
                560522.0287273754,
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
                False,
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
                '20210129:002620.497431:+0000',
                '20210129:002620.497452:+0000',
                '20210129:002620.497458:+0000',
                '20210129:002620.497463:+0000',
                '20210129:002620.497547:+0000',
                '20210129:002620.497561:+0000',
                '20210129:002620.497567:+0000',
                '20210129:002620.497572:+0000',
                '20210129:002620.497576:+0000',
                '20210129:002620.497581:+0000',
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
            'name': 'JȘ;ҤˁҿĖʴ˧κ˔ƐȚŒʕ˨ΌrÜԦr҄\x89}Ӛӥщƀʧ¥',
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
                    False,
                    True,
                    False,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '-',

            'value': {
                '^': 'string',
                '$': '',
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
            'catalog': '\x8cȣɾӕĥʆӪХ²\u0383Îќ\x8cʈѼԋǡ\x8eĽÛҝξѯ˙Ԁ\u0382ѹҞ\xadЇ',
            'message': "˗\x94ĶƑԅȇɣҋ˰ϯǖ'ѯŨʧϯƕΆɩǎ²ȸŕΒė˲ҷЀͲι",
            'arguments': [
                {
                    'name': 'ΙćLˋͻҪžɩқЭÐ(FɌɟ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        534759345172230612,
                                        5962698013106121920,
                                        -4871362825401003891,
                                        2432704420855631287,
                                        8632738998672340631,
                                        6917724312614963506,
                                        -1266723007663979954,
                                    ],
                        },
                },
                {
                    'name': 'ϓ§>ŔνǓÑƄɝǒϬƖε',
                    'value': {
                            '^': 'string',
                            '$': 'ʺǝΫŭͽBĆʹȷŠҬɒɬ˽ñĹǐo>РȬѰЫ˞Ȫԙ.\u038dӤÑ',
                        },
                },
                {
                    'name': 'ħΥƊϞʂ',
                    'value': {
                            '^': 'float',
                            '$': 880949.4087860415,
                        },
                },
                {
                    'name': 'ϿǪСЦӡХɘĥ°яǇЦ˥Ԣɡã',
                    'value': {
                            '^': 'float',
                            '$': 268683.99159045646,
                        },
                },
                {
                    'name': 'ǹϯȧВsѿ҇ұNιθHȚЕώǾԩӳ\xadǮԥʋъ\u0380ѱ»çϞ¿ϼ',
                    'value': {
                            '^': 'float',
                            '$': 294748.09677631414,
                        },
                },
                {
                    'name': 'Ɍ¬',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        8937527853235535434,
                                        2816212676642138057,
                                        3784306258400586037,
                                        6638303620753668810,
                                        -5953383345077759959,
                                        6206459522459941386,
                                        2275086505123404954,
                                        3188002007576836801,
                                        6734024116134173890,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'Bŷ',

            'message': 'ˮ',

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
                dict(field_name='error_message', name='Error'),
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
            'identifier': 'đŧӅԚӝɫȈҔǇ˸ɝǣӛɧɊӃӔјɊԦĴʾ#ҙȶLĖƩʉĈ',
            'categories': [
                'network',
                'os',
                'configuration',
                'internal',
                'file',
                'file',
                'access-restriction',
                'invalid-user-action',
                'configuration',
                'configuration',
            ],
            'source': 'ÉϵΛȞɻ³fȾŮĞëξžԕˤě\x8cϧūϗ҃ʹ˛ƷȟҽРwǣ4',
            'corrective_action': {
                'catalog': 'ΒjϼþɲΈ҃ϑɯƆıтÑŜȏϫǫЉĵγ\u0382ɖаÇ\x8bĨƸЎ',
                'message': 'd9Oǋɡԟѽ˫ҏȺːϛȑÐҼώfѯҲѝчwʯѫͽˋȲƮҘƢ',
                'arguments': [
                    {
                            'name': 'όǨáˈƳѮ\x92½HԏÜѦңχԩĲӢҮШdƛʆѝ˱VΩÝĝ®¯',
                            'value': {
                                        '^': 'float',
                                        '$': 575931.2652678025,
                                    },
                        },
                    {
                            'name': 'ςЖа\x9cɥѸ¾ԈϥƎɧ=ϺлƎñĂƊ½˳ȥԆǩ\\®ѵʥΤŧȶ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ǖŉϵό$GкźǑϽщҊϊɃƤηжГ?ʘҬ҇īʘ>˾ϚҴʁȬ',
                            'value': {
                                        '^': 'string',
                                        '$': 'МϛǪPǤԊϒðǏ\x91ԆȧԂǗәpԑӹԜχЛ˩ǟʓɫǠѐmɞҬ',
                                    },
                        },
                    {
                            'name': 'ƊȈѵаϑ\u03a2͵¥ЊξӰлˑɆԣɈʓЖșԛéǤƤѿԧʾȹóȮ\x87',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        841.4777305414464,
                                                        10792.758251738647,
                                                        365014.22592311376,
                                                        869749.6717987505,
                                                        637938.4507062215,
                                                        967960.0126931125,
                                                        952265.1258681875,
                                                        427759.82508649374,
                                                        191128.9871395224,
                                                        111852.17992362627,
                                                    ],
                                    },
                        },
                    {
                            'name': "źĨɮŔȔѬțʼ˵ёɼҿѿԑԫĺƈŇε˱ʞʕƘ\xadĤғ'ӋʄԤ",
                            'value': {
                                        '^': 'string',
                                        '$': 'Ėм\u0382hƪӘņ˰Εԥ˓ƝуԝӔΈɞÖƄҧǥӈԒϼ\x9cėԒƯʌҊ',
                                    },
                        },
                    {
                            'name': 'ƶɵʢΘƹϕԮʜI˽\x94Ǉō˜ԋɈƃp\x84čɱ˭Τh',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        306300449998073940,
                                                        -3412888552808039518,
                                                        -3460042582779608057,
                                                        -6676719388809887767,
                                                        -2882624088205719545,
                                                        -6195339017644751329,
                                                        5260938470967072525,
                                                        1687946474366979790,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ȻȢƼ˙ɅʼѰȯЉcѨϟ>жğϧӝɝȲPɂ]к˙ϩĻɯÎЌІ',
                            'value': {
                                        '^': 'int',
                                        '$': -7305273576388143231,
                                    },
                        },
                    {
                            'name': 'ˀцӡб±Aĸˣ0ҖɓӭʡʻŋӏÞ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -8398983191281425898,
                                                        1117294512070928914,
                                                        -4558562350232593313,
                                                        -2294135226469008430,
                                                        3025881790715835089,
                                                        -7663235474046405787,
                                                        6831281312067770012,
                                                        3266601668640230979,
                                                        -4275499617401314956,
                                                        5259183941855951876,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ћʧȄˮǞ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'ҾѕǧĞΘ΄Ѥўűԝ\x83-ŴӂρƔӭӌͶƓжșķгԩЬϵł#Ӝ',
                            'value': {
                                        '^': 'datetime',
                                        '$': '20210129:002620.491441:+0000',
                                    },
                        },
                ],
            },
            'error_message': {
                'catalog': 'ȱõ¤ΰǯˤΚƨҽӈҎhȜуķԓχӕЙǘ¿ӝӞǕÄԂŊЌЦȿ',
                'message': '°ѓ¦ˢɵλˎφ\u038b~Ʊĥ\x90ʋҞŲƟԔ˰ǇƷϟљЌ¼άϦˡŵC',
                'arguments': [
                    {
                            'name': 'K¾ҟòΪ˯>ɭȲȊɓǓήŴˇɮӔĤƥѰҢΨϩĳȼίѭà˟ѐ',
                            'value': {
                                        '^': 'bool_list',
                                        '$': [
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
                            'name': 'ЃјϪ',
                            'value': {
                                        '^': 'bool',
                                        '$': False,
                                    },
                        },
                    {
                            'name': '\x8b',
                            'value': {
                                        '^': 'float',
                                        '$': 250807.92319343745,
                                    },
                        },
                    {
                            'name': 'ƌĞπƱǎɮͼρǓϘґvŜʜÃʹԛҧФҖīӣϧŎɺ',
                            'value': {
                                        '^': 'float_list',
                                        '$': [
                                                        331548.609321705,
                                                        178574.2090631837,
                                                        725970.9219296149,
                                                        450736.654687969,
                                                        784533.20592621,
                                                        593265.6568898926,
                                                        120504.28031183741,
                                                        346158.07292129763,
                                                        806293.0140885691,
                                                        90237.60334270904,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ȠÁόӎ¸ϘϬǤԧ{ɒȕ˔ӭn\x88·˾ŎÍ5˩ˮ˴ĭ҈\u0383ӝ1о',
                            'value': {
                                        '^': 'int',
                                        '$': 7643641571692055959,
                                    },
                        },
                    {
                            'name': 'Ʌц\x88Ƞ˃əȧμ\x97ŘɥӡϺćȤѐЗϣΑԦЩɕźpтưРЌДϬ',
                            'value': {
                                        '^': 'bool',
                                        '$': True,
                                    },
                        },
                    {
                            'name': 'έ',
                            'value': {
                                        '^': 'int',
                                        '$': -5883688333783160957,
                                    },
                        },
                    {
                            'name': 'ǨļłɉˤϡѰƪ\x8dΓʌЦӖíКº˧эԇ',
                            'value': {
                                        '^': 'string',
                                        '$': 'ьϕгÍҔ\x92ƗƜ˄Ƕȯ¼\u038dԑɋνüʿýŕĎơѽԑǽӉȑϻїØ',
                                    },
                        },
                    {
                            'name': 'ҧҘҨć{!ĐŴ\x9cϖϷϗ¹˾Ӟ',
                            'value': {
                                        '^': 'int_list',
                                        '$': [
                                                        -9209563024673135026,
                                                        -2811363252749898932,
                                                        -8320781525648945904,
                                                        -9000708180893800917,
                                                        22361958632553610,
                                                        -3435139561226347769,
                                                        -5564081155455690364,
                                                        -7202617235648346239,
                                                        -4625844527185565843,
                                                        -5872120448404991643,
                                                    ],
                                    },
                        },
                    {
                            'name': 'ӏ\\ŃІŭԧюʱǲrԞʶȪƈøģəϣҨÄQƮðǲΡʼϕ',
                            'value': {
                                        '^': 'string_list',
                                        '$': [
                                                        'ȢƲԬϽŧϪτ/ȔӌГɑ®ʁ#å¨ԗáŨƵΰCˡ\x93\x92Ͽ˒§˕',
                                                        'ǸϹԬѮвћȽЀϧӠ£âΎҋƽȥЉ\x96ϭԑɞĨӽżǐȏѓΎ˶Ƴ',
                                                        'ǞϱĐҲńͶkѭһíɇӂӵ«Ӹ˥ƼĳҢТëǬʰʼgѤҧҐəә',
                                                        'řǂҾȜτû˛ʠӁçɒ´ӅƌԄӅƊŽiÎƗżЮěѱԒűѱϕʖ',
                                                        'οcˬѷ҂иɯȷ·ѡЀЍü ʬӥѤҟ˘ʷŻȑÑŠĀȯ«zȧô',
                                                        'âɡǝϺ[Ϩ¹ĮТɵͿ?đʘ.˳ƣҘ2ƢʖŞԈóAƋӎ \x82R',
                                                        'ӁėΘƊźɣ˴ϯɡw[ơӺƦɟˑĝƧŧɯșÎέуȚʷŴѫЎ(',
                                                        'ɥƑ/¬ƑYћȝΡЭҴŇaѷãϽρҼĢūƳĳȑʌԧ˾ͱсԜԏ',
                                                        'Ћȶϯ.ΈĪĊӺǎʇԂǻǎˇñΞԑāǉԧӟӳůҬʠŪƳǃXξ',
                                                        'ŝԀ\x99иǆåԑģѡϑƣˬӬʚѕʪӽhĔžʎҝΘл\u038dğϳĄѫʑ',
                                                    ],
                                    },
                        },
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 'ϲWǽҎϟ',

            'categories': [
                'invalid-user-action',
            ],

            'error_message': {
                'catalog': '˳ʢ',
                'message': 'ǃ',
            },

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
            'name': 'ӠǪǅӳÌǚɹ\u0378ȩĄԟoȒ˚',
            'error': {
                'identifier': 'ʣʞ҄ҰnͻϽʫ˻χNƇϝУПŐҟҲõԏō\x86ƴФǠ+ƛђƼƨ',
                'categories': [
                    'os',
                    'access-restriction',
                    'network',
                    'os',
                    'network',
                    'invalid-user-action',
                    'invalid-user-action',
                    'file',
                    'internal',
                    'invalid-user-action',
                ],
                'source': '\u03a2ƍѻӜ҉ŁňĈzҐǤńɷ/гȾѻΊψƇĔɦˮɓʅȮԃÂЬϸ',
                'corrective_action': {
                    'catalog': 'ƌˬůʻ¼řƓͷͿĻyжџƔ˴ǫËùŲ˵eʯ˧\u0379ҖϾʣŮ\x88ɋ',
                    'message': 'ϞȼӏҦӽν\x9aXҨˌϰʘөĪǹҽϮέӄEȌOmɗѶͿӆʔɰʰ',
                    'arguments': [
                            {
                                        'name': 'ȰѨ[ȂΦēѰÿÜӀ\x86ČŻӣ%}üɾѕɞˌπaёȫĬʠ\u038brԘ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3316904676236198821,
                                                                            -3479745840543621700,
                                                                            1425655346106540434,
                                                                            -3412549616300857686,
                                                                            -4747640159577625595,
                                                                            6625287298419565346,
                                                                            -7417789484715441531,
                                                                            -3962904018447096519,
                                                                            -3205753847822615377,
                                                                            -94878520700331180,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǷǵƎԅ\x93ŐԎɞŁѦқϦχҘλƯ˩_ʜðɂɉМӽ˧\x86ŌйźX',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɻ˂įŽăËѨ҅ɱɶБœȨoѧÙӾųOͱɘɘԟɟѐԩƄ»ͺÛ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 205866.65432005952,
                                                    },
                                    },
                            {
                                        'name': '\u0382ԧȿƷľѓιƙӑͷҶĒЮΫ\x93˙ѬłîɿʭɛßϰҘξњӜɟр',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            603909.1545668392,
                                                                            566513.6175426556,
                                                                            510285.59537014563,
                                                                            -5432.13873360923,
                                                                            710715.1856125646,
                                                                            472632.7600351968,
                                                                            588213.4728331941,
                                                                            758123.882475478,
                                                                            872932.9676382367,
                                                                            887147.2766915895,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʕˉĊĨҚĊŋϤʇǰП\x96ϜƼǮǍƕңȶ͵æ?ŝǬʋɪÔÇ\\º',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8209847068328767019,
                                                    },
                                    },
                            {
                                        'name': 'ʼ˓ƩǥūȸɥΖɬӴ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210129:002620.480888:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ϩœϔw',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            517082.2281013912,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԇΩэώǮЋȍȫİμńą\x94ӟΰɼϭ_Єƽ\x90ħє҃Ǆ΄đ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ԕ\x9dĪ¿ўɳĲǋΨԭӻȑγӇȚƘǓGǪƠΦƤЇнɗӮȂԏ\x9eԞ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            380608.268351536,
                                                                            636769.6740237431,
                                                                            549556.440092115,
                                                                            760800.4772554365,
                                                                            968043.7514708273,
                                                                            7496.656283988006,
                                                                            534666.5549102682,
                                                                            850628.6851668763,
                                                                            358799.0775823424,
                                                                            425488.3131928233,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'zӤŁԓ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'hѝϴȦĔěκǑˀ҉\x97Òïэq®ΏŷǞʷƣφµєѷƿɸпΔȷ',
                                                    },
                                    },
                        ],
                },
                'error_message': {
                    'catalog': 'ҠұeΌѰɅɚΒϘYҊ˨÷ҁîїțѢӗЪпȒϥԃщȓе¸Ǿ\x9f',
                    'message': 'ӺѥєTǜÁӣ6òɞ\xa0ˠUҷҡă˃AЦÊ©ҳԛʿĪТԄ1АV',
                    'arguments': [
                            {
                                        'name': 'ʛ˘О˄υӪĬǈѩјɂǎǦԜ-ȽԆâiԪƧӵȌŋ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɟМ\u038dǪ6ÁƍʙΪ϶òƅ˟Ԍ¨ʐЏӯДh˨āҸѢћ΅јǫŪҾ',
                                                    },
                                    },
                            {
                                        'name': 'ӏӉħǆ:ʪнѪШɆЏǒɂˣˈ\x8bѨϭǑĕųςϸN˨ϱ\x81ȿ$Ѧ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʢŕʒŜgɣ5ÁΏĸķԗʄϻ˒ȭvʣԑҮǅ,ЀĴǍýҍʾЛ˽',
                                                                            'źƤĩÊưʹʠÏбŬŬʊ\xadɊOɟºȏ¥ΞȗҡѸɓŹϊǶ˴ҫϤ',
                                                                            'ӄïćԧǙќˉˤѴǫЁ"˃βъȃǍÊDƈǟTһӸʕҹόɹӊӭ',
                                                                            'ƕɡЎʽϵ\x82ɱ$ĥǠɈÒȴύћŷ\x97ƳӢЧǡȮÐrɁўȄoͷԉ',
                                                                            'bЙȜȩJI®bӘË˓ЏϙČRϜƤȁċſċ¥ˡϼӉŴÃԗə^',
                                                                            'ƾϥȊǊȾӸӭӣ\u0380ΰζғ˫Ɲ-˃ϱÒˏƠѩӻьƂʋ¾ӱӴ\u0378Ə',
                                                                            'Ԓ(ȒғXӁσӽϯƆ[ɽˉˏѯʾʩ˟ЮȁϜɽταϫяúҽӗǕ',
                                                                            'ԓпϵҗ\x9cΕю\x8dӣ˸ťțγǻǋŋa\x8cӤҹɂТϜΔʉӜÜ\x9aìԢ',
                                                                            'ɋɋԆíίʴ%ȗńм*\x7fȈǷԈΔėǽ˥ȤǀϕԠǿʖiƷ҄ҝː',
                                                                            'ë΄ȨϵˇˎÍȫɦˋʠΦƏϧˮÔψԖӔΉΕĐХâǬϜРӤƊŒ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ö˩Ϝ¥ѱƎο,ŁǽŇ¿˕',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 492641.62676132016,
                                                    },
                                    },
                        ],
                },
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'βXΕ',

            'error': {
                'identifier': '»ŷһԃÐ',
                'categories': [
                    'network',
                ],
                'error_message': {
                    'catalog': 'ҠΏ',
                    'message': 'Ͽ',
                },
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

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='event_id', name='EventTarget'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='target_id', name='EventTarget'),
            ),

        ),
    ),

]


EVENT_TARGET_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'event_id': 'ѓƻűԐųӗĤIˉϓ˫ʡͱƫSϿɮɖɐϞʭʃȴɚĠʎ¦˖ɦԚ',
            'target_id': 'έ˞Ɨ÷ɰļƔ˩\x82ӘɖҺτʴǧɳʴYũÏ\x93ǫψȍȴͱǕǔǼҭ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'event_id': 'ɾӴÇ~ʹ',

            'target_id': '҈њȇ\x8a±',

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
                    'event_id': 'ÚиɹѵʿǢˀáӚ˱\x82ǫͶҪƭ(ӶϖʋΐɶǟԋƜĸîцˁèκ',
                    'target_id': 'čɀӀ˃Ԅӟơ¢Ԃ×ѡϮȚCͷɄĎäϏʻΐģјԢȨеόҬНʇ',
                },
                {
                    'event_id': 'îϻЃ\x99ԜȴӭĢɖӝƂĲ˟дĮԪÞɛȑҺĽͳϼԂєǸѭΨǹę',
                    'target_id': 'Ǣ\x8bѨΪѾƏ÷ȊȥЋƥ.˥б҈ȌáĒ˼ҽΠГԥŅƃŮ\x7fŭѣó',
                },
                {
                    'event_id': 'ҿ`ȶӒŠ\u0383żǤΈͽΉǷʩtͺΧīЍTЬΧӆӚŞŽ˫цĎƹǲ',
                    'target_id': 'ԩϸѯŀŌˠɄ\x96ƚʓɸЛȗƹιӚ˅ɳɚψǟ;ˌÂǽǀσˠŤ*',
                },
                {
                    'event_id': 'Ϩӈ\x89ªę˒ΐf"υ8ȒрćɽКӴφΩΕ\\һŘƭ=ˈŽȤ,Ŧ',
                    'target_id': 'ȮθԂːǖŠĄ³ßʶӷʥЄǴʷ³ҥϹʺѴӦķķɸå˲ɊĴѺӟ',
                },
                {
                    'event_id': 'ԧϹϤÝˌԩ¦ȼӎφγ˨ҨņɦЮϴh¢¥ёгJ\u03794ɰ©Jέƿ',
                    'target_id': 'Κ?ÄӿӊХ˗ĄśȘǲ¦ԟԡˋφ\x84ĤƿПóƿƗȧiҁ˃ɋσѯ',
                },
                {
                    'event_id': 'Ӥ\x80ĝ\x8eǾΝȣӭʧ]ɐvǮӕƝ˖ƙǓɐѣԐǸ¬ԑҚɦǿˬѤӡ',
                    'target_id': 'ü¼˪ùĺѴˌǚ\x98Ѯ:ÑĔɸSϫΕˠ©ȼĿӹƘχӠĊıϐѾă',
                },
                {
                    'event_id': 'Ŋҗȹ}ђӦĖЋƢəȤпΠť^ӲґȁӁ˷ώԛʀʇrvǗÂĶϗ',
                    'target_id': 'Ρ˜џýƘɹǪΊĸЀǯ\x9cʧǻ\x975¬ҘΏΓZЧѯ',
                },
                {
                    'event_id': 'ƒΑʽҠ¾PdɣƂMуӠǷǋ\u0381Ɔ\x95ˣϿѓȞɤДȄ>ɐȌșJћ',
                    'target_id': 'ɵɉӌӷ\x8eǒӵƜĤĀ˧áŭʚµϨϾΏĎŤS˟ĨțЫͼКƧ҉4',
                },
                {
                    'event_id': 'õԞŘāʌȌǁɓÔШ\x94Ͳ˯χ˂ȂʾǪҥѓ±Г\u038dƖЮ˂θůǆ\\',
                    'target_id': 'бǊµԭ˪ЎʐƂsȢΜˢˎ¨ӳZȕτĴюÓȆǜѨӑƹ}ȟKÄ',
                },
                {
                    'event_id': '3²ƱĖɹ»љӺ\x9aL¥ȴБҡΙƕрυϪǕŉBˉ´ͶȓČÓͽ~',
                    'target_id': 'Ѱ1ǐ2е½&ѐfӝÉƹȐ҉ӳ¸ӕӞʤЂЂҴȆϜЇΰυÈӵɁ',
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
                    'event_id': 'ԃϢʋĉ°͵Ҡ\u0380ʥSџΐѼЁʍќѨāʩАκϿЕŨʎȼϗáЂ˗',
                    'target_id': 'ƅ˞ԃɪˬƫӂќĝɁ÷ˌɀΩǿнɲɇϏыҀùƏ³εΜЩƷԗѨ',
                },
                {
                    'event_id': 'ҵƌøǚǫәã6ʺfԧ\x90Ǭď÷Ӑʲ˻ǆӕȾέƺӡЙ#ʣɾǋø',
                    'target_id': 'Ҧʛ\x9cɶ\x8bƯΖÂɓьϿϞѲŒǰǷȶȢԡΨǼđnȖ©˟ӆΗĞʩ',
                },
                {
                    'event_id': ';Ȁ\x94ɣ\x86ɞ\x92őԂƈ˙ˡĎԀ¸ҧɚǃ\u0378eŸɎĦœЌǴɅϞԡˉ',
                    'target_id': 'ӂћԁƄ\u0381ϝǁɣ\u038d',
                },
                {
                    'event_id': 'Þ˻ІԍǶʦɍ?ρʰȍɚ˜ƝˮќϦĒ\x92Ϝѫmǡ˱GÚ\x92ҿ\x9cΑ',
                    'target_id': '\x86ґНеĩлŠĜѐģѡΠӮZӖ\u03a2áԤŰ;ōŹýʰӾʪɻ˜ϜӋ',
                },
                {
                    'event_id': '\xa0ʯƦɾÏӧŐĉǱѝϡԠØʰӈϟҨͷƭʩэ_Ϗѝɝԉδ-Ǣφ',
                    'target_id': 'ȚǱȌǄʙόеƋ\x89ͲP!ĲɸӅӳĒūɅlӋXǽσЯ\x87ϣѢǥҿ',
                },
                {
                    'event_id': 'ΰΒζ˨ɡшĔǌʇŝϒϵӎƪξȣ\x90¹ʙˈЂ˔˟ҋӏԣłЙţă',
                    'target_id': 'ƇŔÛȦщʧϥѓȅӺˤˇʟĢɐȧɞȓǾȩƠɎʙϯÃƍαǆ3Ǿ',
                },
                {
                    'event_id': 'үŞđƱЋȶ˓Ĝʖŕę\x89ƘłƜɨȲҊʻʰ\x90ļŉŝŹМǻ±ѷ2',
                    'target_id': '\x9a~ӀԞϫɷΦϜϦԮımƂȧAšŪíȾǽ\x98ęɍҬĨЩѶƹќљ',
                },
                {
                    'event_id': 'ϚʎȸӶʌѡУǳȒϪ',
                    'target_id': 'ϛƪξǬŨѶСԎһsȰ(оʰµŉhȩɟҬʰ£˱ͷӾӹ\x83ԠʘҔ',
                },
                {
                    'event_id': '+żÚV\x89Ĺ\u0382ЉĶǗăΣѢ҉Ƚƥœɒ¨ΩҟȘÅÈƧ\x80ʣ˅Ԫό',
                    'target_id': '®ˀӕ˶РaҪӿͰŮσӑ\x80ýˉӊ\x8fƱɧέү\x9dѐɚӘԝĻýͲ',
                },
                {
                    'event_id': 'ң\x81Ɛ҉Ѷ\x7fôţ¥ǳ\x89\\\x87ɼǬĮО҆ƂϜԅ͵юpȑʛċ΅"Т',
                    'target_id': 'ϯǥ\u0379ͳ\\ÃөâÑŬ-ìζӻòȵκǽ˻ȷѢюyЈXҟͺρͱ³',
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
