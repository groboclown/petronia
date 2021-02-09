# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-08T21:23:09.177918

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
                'Ԯöɝǖ˝ӸÆǐƱǋ˽ÔёΙVѱÐǱȰŘәѠsk©ʣȘˌƈѼ',
                'ƃѩό^õдòɽķȫÎё´ɎÝяÈ®ʯҨʼʬƒӏČ7ќƹÿj',
                'ŲðҘЪƃЪ\x8bǱһ\u0383ƮϚ&ȰîҞχԡЎΜ¯ǳcԮĠ\x94ľǴȡʁ',
                'ҷΉΞϒҠʺ\x83\u0383ҮŒѶɷâĈЈɚŽҔ˵įү\x94\u038dĹƶ˚)ľ®ʞ',
                'ɥʭũ\x8eҡҏʫͷӁʒЁˁöЎɵ\x8b Ŋ˭ёʥnv˟$ˬѱȍӌͲ',
                '˫ĴϼCþʻϧΈԝʈȭ҈Y&ЀŽÆϭЉ\x8cσĄғėƥZĕυϤ˻',
                'ŵ˻hћГ˷ϕȸº\x9fǉ˕İЩZҞԈԭʇɡ͵\x9bӭϫ˶ϫ˙ΊȟB',
                'Η˅ҋ¨ȱ˙ҿΩsȠΒeǛȀɵ΄ҋźɬӏaȌʻͱМnģғўɆ',
                'șɇΩ\x84ԕǇʛ·Åɤʪˍġĩ˟ΪһЍeʿřžѐŗЁҍΰҘ²Ō',
                'ӀFʏúϨǝ`φ×ӋˏȂȚӰ\x9c\x88϶ýығ˵ˊџѼȮŹȈàŪȔ',
            ],
            'source_id_prefixes': [
                'Ľ\x93Ԙɹ\\·ȥ˰ʒѲȔŤζŽͲϸӠËǺғĽÇÊƧÃ*ԝȕ˛ȑ',
                'ԥӘґƯʑ˖ѻΈƶҟ®\x95қЬєˠ´ŘƠÝҕq\x99ԥʡš:Шӗȅ',
                'ϭɻӒΖ3ѵ˽ѦƜȐƄԢÖшӀƷ9ӴɻπͺbΡàιҝԇϤqҞ',
                'ɊtǗ@ӺќÿӛAÄԌу*ƁΜʕǯӏрӃɢωĴҷÝǟĿҋ\x7fѲ',
                'ѬĄǜʺūϫӀӭжɥҧӷǫʼɨȝĖʠŮʵӄΚɧ˂Ѿ˺Ȕě͵ѯ',
                'ҼʮĺѝƝɵʰΑ΅ԮƺЮҠɎȍȃь¹ҪΒäǾļǫģƺВЇ¸Τ',
                'ΖŅЙȖԌ˧ΐԩȼȋ˼ŸĶÄϵÍgÀƱɀ\x87ЂȢŔƩӻɟоѧĤ',
                'ƪϧȱуωь\x8fӷǟКԣƹЫȧµƶԖʁřŭȽǣŤ\x9cŉ]Ρɤўǳ',
                '\x97ҝƝƚӆӰĢѯoƙÐƭӱ,ϾɯѫӜÕĕ\x86Ң·ʝһǧǪа½ԍ',
                'ѐʄÒʿϱЃǔʡТƘϕѷӏŁƠб^˳ԑҩÙʌġèʹʒԥĞǱʩ',
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
            'action': 'ɠtӺԗȩт2ӵөЎЂʫԉӶņϰЋǹȅ·ʼɤ˦\x9b˧ʓӠɄҮƺ',
            'resources': [
                'ɗҗƨ˽ŕЂОҞΉƧÿϫΔңɄǴΒĚʺČɿ\x94ƃήaԮӛ˯ǝǾ',
                "ƾʗ\u0381¥\x96ϯʂƻί'ѡõũːîҶϰЖΜȲМαӏɖӍɕӋЈьϓ",
                'Οūĳҹа4Б°AȏԉɠϜǡáϽŏĔ',
                'К˞АԄƢÉÍΜ\x95ʲ2łɹшAƔ\x92ɓģ\u038dǐоӎ&ȎˍҸ˫:˭',
                'ԉyóϙ˂ɰƆƥŮșϟΧBҼƉљ˳Ѣј˧ȶɲƇȺɵȰ˛hʫǊ',
                'ɄɚʬöȒԭŐŹ Ď¤Ƹ,ʯøȊŉŤԌͱ˶ưѣϵɐÆҹϜН¶',
                '϶ėϣɝЙ«҄ʴɚʀӵҲɚƴǀπӱʯQó˙ӹ®тԝ\x9b:ɭεѵ',
                'æǜßў˓Ǯϫ¶ѨŏțƹYĨʽɀԉbiĂҐǩΉĨӇ˻ΐΪόӮ',
                'ǋ_Ưˊ?ǠȀ\x9aůӟɿЫȺԞӸ\u038dćҞӼɔ\x94ȏЎɑω˥ъƽμȃ',
                '8ӲҊчȼυĩƇʎȳҮ҄ĝġѓƉʧӂÕΏκʉLÒҀԑF§šΖ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'ɨ',

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
            'name': 'ѭЄЮҚ˩Оͼ¬òΝˣα˹ţȁœ˃oЧÚƔЊѶą˦њoRёʭ',
            'version': [
                -701109663787072667,
                -7803381922181573489,
                -2072111830836646867,
            ],
            'location': [
                'ѬПǑkͷǯ\u03a2ȹĲÙҟɮ˻αĖgŦɞ˴ÉԉǮŵ΅аƉ\x7fǻʣȿ',
                'ő²\x8eŘԮ˺į|ˑӜ\x88Ǽ\x9bĊӤ]Тʼɛ\x97ąȧđсLөĝǽȹ<',
                'ʞ',
                'ҖĶæΔÔǔ҇ʞԁNЦԊВϵIƆƻǴ\x8aȱǈ҄îӽɀþ҅\x7fт³',
                '˔ƴ˅φ˜z\u0381ƣҖȩʠɏүγq\x95Ҧȼ±ģ˸ǏĽŉȚűξηΪȷ',
                'ǐΥĠ˄ϞԓχOԅŤѡȃçïƑǩǂǝÖıǧ\x8a÷Ūӯ\x91á!ϴԕ',
                'ŖƳЅӏŜІƝ¾ѝѩͼʔćÈŶȝĒ\u038bʡâ¿ϯƨƭ˶ӲŋˉÙĢ',
                'ôŦԁđԧΧӦҋ³μËӀơÁϪȿ\x89ŃӀɧǽѤ_ч˟Ə\x9aрGȪ',
                'ǌҽɑø¡3ƾ£ņ˖ӳĀŎȍŬŪҴȯԚʟŢħ\x87ǃśҀ϶Ӌӿа',
                '?ũͿàԂЧLǸáϕųƯƾȬH˘ɊҢǃԞȸǳŨΟЍƛ2vӏº',
            ],
            'runtime': 'ԅδŮεӢΦƐǒĉАƆƿȄςłʤӔрæ\x84ĄңŭƻдҫүφƋЁ',
            'send_access': {
                'event_ids': [
                    'ǿZԤȶӸæцȜ˖jɓDŒÓ\x8aɎɜtåˡˑѾˎ˟ʲκțƙăϰ',
                    "ԇǗ˫!ĸò˦ԊҨѽчӒwȷŇ˛±șǐԉ˂Ё\x9fҲ҄ǥΨ¨Ϡ'",
                    'ɓüҦ\u0379ҧҎÁǙϔ?ʀҰѪˊǝɜщ˵ԐǪɰȼҲңѥͽ\x9dщϑӝ',
                    'Ӕʺ[ÎѺɟԎŢО˯˞Ѭҥ҃ơĞλɧʵȴµ,.ӸKЄΦӈйƾ',
                    "\x89Ў|ŗŞȃƥɑΨȻӦ'Ԇӌϣ˖і˫ϐŴͻƾ˴ПƵųҳщɪα",
                    'ϽĘӷӘƿћѾтӀĻˬΆís˛εéªƿӥɐçʷіԆ8ЀǼЗз',
                    '҆|ȎwMòҵîUǐ·ѹҤ˒ӑ\u03a2Œ½ʾСҶȧɁƕƏſĩӗϰĳ',
                    'ɢ?˄8ЕɹЏќѸͰČϬĄʥεАŹжěĀ´Ǐ\x85ǽ\x88í2bȊϧ',
                    'ͻ\x9aыƏVďƷWŇҡˇʤɁσQ\x92ɌˋͺňĚſʘԍÞҴѹʊƔǵ',
                    'üԈԈư\u0378ƫźЬς\\ĎƇƏҏԄĤľΞʍӦԅҿ$§ЛČȶÂœƾ',
                ],
                'source_id_prefixes': [
                    'ъGҖϑ\x98ƈԖЛƘ\u0381\x93ɓȦķȸк|άӆũǯȀǸѾшȊª\x89ʑϒ',
                    'Ѱϩɰ~ҼɦӞӨԔǨ\x89шɝʻХϕǆÎˉǑȬǬͿŻЈũͿžϜЩ',
                    'ϕ˂ԙʥЎΖн¬ˬͲИǈƎБƧ\x8fǖҜ˯k³ɢҧԢƏÙˡǳUɏ',
                    'ĎŁņȔϏǯñx#ˠɖЀƠѨАԥǳʆԁ`5"ɃαʯˈĄ¥Еҍ',
                    'ʥΚ\x8cˮ\x88ŹƭżʎԭΕҗˬ8ΕAτ҃ˌϖҴЏ6ĶƫЦiƃs²',
                    "ÁȞѴǣ˙ԎҶχƞǸҚȃ-Ċ:҂\x86ģ'ɵбЀӾ\x81ԠӍНʊũɚ",
                    'ıӼѫƓ\x88AðEҫàˠҕ\x93ǙdūҳȂˎÚ_ĔʡËˏ\x92ƑɼӂΡ',
                    'ЋÐϖƁeÔɩïǢɘʝƛΜƓ˓ˡξӷÒn˵ëɎҡÔӎ϶ӠȚѿ',
                    'ė˯ɆƢүòԉŅʪåԮ&ԬǞˀGȟɊȨ½ϳΡ˲ϣ²ŸɩӾЖӱ',
                    'ʴǹјʱԆʪʧӪΎʡӌoқӚ˺ĒǦ¥ʚʽҗȬØԚͰҶ1\x87Ȣá',
                ],
            },
            'configuration': 'ɍΟɱ˄ҜɓˁʎΠϙɸ\u0380˻ȝϖƥԪѤˌƃ\u0378ȡӰÄÆԟ˸ϦӏĜ',
            'permissions': [
                {
                    'action': "«ȵïw¼ʀӱХȁøдӗ¿ԆêЮƾϽʗ³ϰ'q҄ђ²˪Șśǿ",
                    'resources': [
                            'ɫˡπɅÄиԂ÷ɻòΫȕǧɯĴ®`Б˗Mňɡ\x8dӜӪ˲Ƽİ͵Ɨ',
                            'ıeƌЉҫҠ˪Ǖ˃ϺȴӽҢҵкǬҶĠɦŅТзƽŠ\u0380ԅʨ\x85ѿϔ',
                            'ɄѤʾcę˲ИӒʠϿǸ\x87ǋľĈϜӇɞԋĶɤƕʜηɳː\x88}˦ό',
                            'ˊґǣԌƘǩɡʜZȭJяԬAӏĠÐǉæą˂ŇƮɩӍҩәã§τ',
                            'ǶѬɀΰ˂ȻʇȦЖƁԨ}ɋKΝ˕ǮjíăȈϠ³ɼϟáģҫ¦ė',
                            'ˣpǄБýØϤӦеŝԍůțȟˡȓÓÄѰȼѥеԢ:ƖɑŊѠӶѹ',
                            'Jȳȟ;Ǫ˗ƺŔʗ˖ŌΩ˧ǳΉγΨȁIˈɼȽ˨ɮˢʫǶӕӘȷ',
                            'ƼΧ;И8ɱSҙǹĥÉȬÙрјåԟώ',
                            'Ɔʻź\x8a©\x89Ԣʤԩƌìģԓ\u0380ҀгõΓͻǲҀƌӆÙӠ§ŕӗ˭m',
                            '\u0378ΤѰӛŔɂȄƟVǞăӈƗ\x87˪ԛх³ЮſʿǈмпхȢʑɍ\x92Ķ',
                        ],
                },
                {
                    'action': 'īљŢȻǠ҂ӓÑвîɄʟÁÖȧlóȞȇǥΖʥШʢĿƮȟȆнҗ',
                    'resources': [
                            'ȟǥyTАѸӪȱȇƩʋυŚ´|ѷ.ВȾϊԛɹʌŶДђтЖВ˨',
                            'ŌȑϮ\x84óûǬHËԫԜԒšӗϗԩԩȊƖǍӼɹČ1ʹЛɧΚQɈ',
                            'ÉǭRɊ',
                            'ǆgеÖÀƻCϿήÈ\x9aɶР\x89ˈű£\u038bϧϰʥÄƪˁ]ɜʃҦˇƥ',
                            'Ȥɑ҇ѥɁJĒΞΗѼӄҹmԔƚ˩ÕǶóѥЉʖЏԉ_âԎŤŻџ',
                            'šʃŌùŞҔĢLϼŽǓԖţžԂέ5Ɏǂő"ˑӐдԖҕӍ8Ώʍ',
                            'ГƦҿ=ɢҟѻ3Ǽϐ˅ʆ˓Ҭŀƛ¼qϰҫƻ҉ǰˉϭԭԚӂɩȈ',
                            'ƂƖҁȎФŢûÂŢˡ˕ԜǆιfһпlΊϹ˗ѝӦƯd\x9bƛǳ7N',
                            '»ʉǖϑɅƷł\x97ɮųΒȧȀӢ!ȣʀǧΆȀƮŕ\u0383\x9cʻͼƽҔϓѬ',
                            'ɕŒȈ¿ĨćԏІɹͼӦӼrʰӐ$ķƖϨƊ&ƍ\x8eηϓҲůưnϙ',
                        ],
                },
                {
                    'action': 'Ы҂ωȺʎǶЙФȉƟ˭ԓѕ˨ʍÓЖđÙ\x97ɭ͵ʌ',
                    'resources': [
                            'ǸǅÎȭāԏ[ɉñ˒χʡΛ)ͲɖʏʸԭѤÍʭЩҘʄӯҫ=нŘ',
                            '˓Źȋ>ΏϫәлŽӀҢϡɰɇƾӷûΕл©ɰ˅ΰёßȝŨØhд',
                            'cƣΞӋ#ԧґŦѭ\x95ŋɂʐǋȋŝШǁӇÒ¹ƒþȎŰȆȬŅҧƁ',
                            'ҰǖӔžҐҢˉϙļϊБʧ)ńϏʏƌˁͰʢăαх\x84ąpΌԘδʜ',
                            'ЛĺДƫƫŨӎѬɚ¯2\x90ԠЙęʲΒƺқ¦ʩҐÆȌǀѱԦƝΘǦ',
                            'ϊƾn˚\x82Л˳ГШʔȈȒ©īͲѼǺȀʺѳ\u0382ԙѢÎʣƨNВʵљ',
                            '{ӯԁϽӉʺƦЮïXɕɞɜĨάѼʬͰʚƏМķП˪ЋĔÿЅǀϫ',
                            'Ƭɐ:ĆƳʝώĉΩ˸ʖȍʮˤΫ\x90қʽȱǪȲжðȌѰƨÑԉ\u0382u',
                            'ȚʟϏǒʟȜaà:ӽȘǨцȏҴ΅мӔҥхͱŮ˓ǨɇˠzšОё',
                            '˗ŵɜƌɮɸԑԒĴ\u0380ӵУȢͲђȄӡŵάŔǌ\x98ԨЫśUƒҦʷѼ',
                        ],
                },
                {
                    'action': 'ЗJѠĤƬ\x89˨ʏͽɞ5җθĴƪͳŶƳϧхiҴѵ˶HʊгϬƘø',
                    'resources': [
                            'ƋũɃӬӡγԁЗlƋɷ΄ήZɫǜұƳɡŴǰµĲP`ɝӽƿɷԍ',
                            'ƔϿʿɢˊdsҭÆˀȘљнXɘŊӈ,\x81Ɯư\x9bΗĢVϩεŹÍ\u0378',
                            'ÈƩӞѫFɿƪƳǧҗ˚˨˘ϐԙԤϐɀƭɰόĎŋɦȣͽʗƙʨˠ',
                            'ΉвΎǈÇӑ³Ѐҥ\u0382˳ǀұѺȅԟ:LǏƲ\u0380ЌȱLӌȨ˥ѿŷċ',
                            '`żǜȷќŭʥŝEʁӼ϶\x80Юlĝ ³ӞӦĔÑΑǴ¨Ã\x9cԤïʏ',
                            'ȝӗαmȪҨѹϹʴƗѻdҸӲ˅óәʗ˟ŧϬїαňҩȋºϽԮÕ',
                            'ƯзҩƚƜӪȁ˲В˚ɎԃİʚҋȦ*ʤƋΔμƜыʀЭʞКǄ\x8aҝ',
                            'Ê0ҥҊ',
                            'ÞљӯʚȋѭțƑʫɥɚАrǝıϏУињŌ˺ϙ˂Í¨ːʚўғӲ',
                            'ȬÈ¿},ƼΤǂɀ×Чӡτ\x9dVϏώȃ\x9cБɪſЛАǲɂèȈˆљ',
                        ],
                },
                {
                    'action': '˴ŖʪІëԦЌ˜Ė¬ŴƘƛʇ$Ɣƃє˦ϳ3ʽӁǉ˳¿ɷҒȬç',
                    'resources': [
                            'Ĭν<ʁɇЮѸԃʫωhŃăĉÙԅͱʗҫͺȈϵȄȓƳɜΖ°©Б',
                            'Ǐɪśђ҂˲ʩϰқдÏȊԞɺ]ə\u0383ĻҺDԠӕίГӞƹͳԙѥɊ',
                            'ѝžԎҟ\x8dˑÙςѻħǺҾȫȒЅǭǀƶӿƩϭϛԗϱǱԘĆҜҜÉ',
                            "Ļ'ȟȟǐɝρźLʶʩv<|ψĳ¢ґȘȫɖεyǧбӣǽiѯq",
                            'ČʙкJЁɇȂӶ2ӼȰȠәäҁƎӫ΅ϟӯħŨ҈ĕβόΚђҗԖ',
                            'Ȼǡϝ\x9dɏǔƻĠō¯ԝǓưƠѼѐșӘԆҚǽĪͷĽɟŷ[\x96ӈƑ',
                            'ςóлͽʚϛȒϮșΖǢφɼĚǭǈǐ\u03a2\u0378',
                            'τϡêˤ£ϾǜŖȚǗrƥ$ưĭãˌɜ\x82ɫʷȔȥÑȃȪύε½Ӗ',
                            '®ӂĔıŲˮʭǹȦȮɆё2ʧԊăˎȨ&ſ¼LÊȧώб3όЄΎ',
                            '\u03a2¹Ҁɭ\x86ΕſÃϯȒÈȿƸӊȲғҒѹŹȳӔÞԩѪҥϴ˟ǺıÉ',
                        ],
                },
                {
                    'action': '¦[ԢŻ˓źǱӼҤɃłʓȅОĲʗӦǈ«ԀȲĵʳȄ϶kѝ˗+є',
                    'resources': [
                            'ə˨ϰȤѡԑ \x8cƧό/ǔχȗ˷ȍӻѻζŞҗΞ˗yӐЃˮGˬµ',
                            'ɝƞȭСĈΒшƮÎǪʞЂΚшȱɨǔȑϣǘҮȉаƌιɛʲʣңΨ',
                            'μ5ƶĤё˱ӟ}ΒҨγϿĐǥґˎƺйƋН ˚ΐķϛ\x8cҒсθh',
                            'ˌɰõЁΩǲŤ¦ËʊheĝɝăЍԤȌʧӒпԨtǢʽԝѓƔȨτ',
                            'ʺӍǆ\x96ѧяůǧίФ¾ӢȚҍÎҬƔƓҔŀFȷŚĻʢǦėðӉŸ',
                            'ЅˬɧʯȻɽ',
                            'ƲҍŮǿϞ˶ƏĤѹԘΰӽūɥҔњԗɉύƪӓMӃ;$ǺЃʷōУ',
                            'ɋɶǕЍǣ>øðƢǼ΄bҔϳɧǌ˽˙фſЌΥΛѾŰȥ,Ɩȷь',
                            'ʞʣùЇϔҰʩ_ɃԅαϤTϸҺӃҎɖȀɏwȄҖЭȔƭ°ťĭӀ',
                            'ӾĸӼӰϻ)˯ʏϞɒѦҀи¥όŉĒш\x80Ȅ\u0378ңԐOêâìŸ҈°',
                        ],
                },
                {
                    'action': 'гКŎ±\x91ǴƏȹɷǓͻЋϒыǮc˝\x84ȴҒ˞\x99ΕɳʗÔ˶ЯȍТ',
                    'resources': [
                            'Ǌƺ4μȑψćӰђǺŮҍˤˇΘƘԕƬɞĈ]ūȦĽȷɮɡȤ@ĸ',
                            '~TƏӚΔˇ˚ύȖjǼřWͶεӇȀӞԙ©ʙԥоΊ¤ŧў³ʒԐ',
                            ']ҡɘĜÍƦʏÂҼàşӔȔτӻОϼɁƮΟΚǊȶ1\x8dʤƣĹÎñ',
                            'Ǽͼ˞\u0378ʖњͲ˰ýʷͷӉεԝ҅đҟy˜żǜ¡\x90ԍŹɓőąŕƂ',
                            'ѷԒůӗǐκβ΄ěƿκϜ\u0380ӌ˗јϴƬыĲƬ³ȇĞɧƒPSʽW',
                            'ԩ\x83_ӗʹɀÏУȪīġβԑˆÑƻϼ\xa0ǝώԪ˅ǬśƒͲ_ʷҖ(',
                            'δʰěӶңˉϊ¼Ģ˾ʁȪĨє@ǣ*ԒˈTÅΊèŤϒʛϕϸJĀ',
                            'юȮ\x89˝ϜȧȏMĩęʥ˵ѡȔϟƸ»˽ԬİыͺЋɄΨȮΆɥαÛ',
                            'ϫOǾцԗdPȭπǎƠ(ȸԫƟӁȂωӟѨϓєӒ˲Ԁѱ¦ӜϴƱ',
                            'ԩȑʑчӖ\x9dЂŬԮѣʵYϓ˸Ǹʮ¼Ҍшqǈ\x81ʰeϨʱɪѡФǦ',
                        ],
                },
                {
                    'action': 'åĶìʙА/ɜȈӿƜʧßɁчфȻǯ҂¹ӽԊȵΖϱǸĢ˼ҽҧǨ',
                    'resources': [
                            'хĿĐȆʲDŕɮăέ8ɭԫƚΊțϜϪÖе·dӧĀԐSЭΚɆʂ',
                            'ͱԜÌ9ҳΙōȔ',
                            'ŀҒҎˊŪ\x95ʽήиoÄɵӏӢ ȹǤӿɃԐӑ˨˜ҭԢ˱ǊŎʌP',
                            'ȧϔûĎƖϩqρğĝţ˙Ȱ\x86½\u038bœJԒΧˇҌԄǛŚԬɺν\u0378Ϫ',
                            'dԔƯωÆҊǅʚķԒȂԐǻąЬ\x9eȼϙțĨнС˗ҀϝʑŰʏЦь',
                            'tȉԞ\x84ǓԡӝΠϢ҆ԩӛ\x92Ș,˷˅ʮȹϟ\x9cӑʵσɢΙ5ǋä&',
                            'ʕfŏi³˸ѣý\u038bԂıϏӄAʷÇОŮˇɮ7˺Ěʀяɾƈ˱ӧԫ',
                            'ûϦƁtɆϞĥЍγǿ)ѯǄ˥ǴɑдΔӥɣˠ˃˴ͳǖȳЗ\x82ɫӔ',
                            'ľɌɔԆϾҀ˨ŪȄǀϸS\x8fʶ`Uʃ\x8dǢ$к϶CβƋΘ\u0380үǽƱ',
                            'ĘŐɌ"ƴƠɥ˽уSwԢŪŎȽҶԦѿĵԪŹιŔɞӭþĠĚϑΟ',
                        ],
                },
                {
                    'action': 'Ħɔ\u0383Ś<ӿã\x8d˄Ń҆ȳOȕΞÕьҷƝȔʡǠ¢âǏēɮƬÑ=',
                    'resources': [
                            '˼Ӽ˭үҌɿӀ˱ӅѢӑӫɈЃӂǙЍʅĠȽʎκƜqцԐİȊȹӈ',
                            'ƷΗşʅҞŷŭӄϏеʝǥчƥȭ˰άsѸϏӧʃúhPҸԝΈţ\x99',
                            '˒ÃƃņӌϰҨŲÈЪʛәмʎŕkŵ҄ǶїҦϷɼ0dҟ6˄?ҙ',
                            'Ͱƽ˞Ӌŭ\x84\x8cʽȏŅʝԏ΄ӡÇΠņӚϷɪƐӔˆřϘǣҙӧωƿ',
                            'ͱǳ\u038bɴƋΈȰДȖŬϬκƗӧ҃ԪŬȥӝɑȎɏŔKȳƂЗȻżҖ',
                            'ЏŤʞɺҜØ˺MzƨǎʀϱыƩ˧~ːĽǁ.ȁԣө\x90ʝʲƾǍθ',
                            '˵˻ЇϊЗŪʆ\u038bΟиψ\x81ɝʁжêǘəÔн\x9dԪԩȣϨʀ~ӡĠԑ',
                            'Ԧ҆ʨŒʔӺξҽŕűƾʎīюãƯҁˠ\x94ϯȀϸԌĐưǵȸɄѶť',
                            'ԠµϋΔԣЩȏÙͺӸɚʑņƼϼϪŴЃ҃ŝ\u0379ҐЩǪƦңͳɄԮК',
                            'ʈɣľƷхěКӘЬɚ˓ǙĦȯәЌ¾ĆɁ\x86˶ȰЇԔ5Ȟԋʍʐɶ',
                        ],
                },
                {
                    'action': 'ÞɻΉҸȡбˉ\x9cʯѰʆϯĿҰԗѳŕ˪ǿ\u0382ȥѦоʘѡ\xadǞñĹØ',
                    'resources': [
                            'ãVƨʠƱįƥ˦ӯАзcwҴaɆϙlϘȠ¥\x96ђ0mԆɷšΞˈ',
                            'ǙœϺԞèȌɢ6ÁѱÈѠ:ĻϞƬƕђμňҸϴϬνҕЦņǱϤǺ',
                            'Ǯ',
                            'ȬǦȈňŞ\u0378Ĺˊʇ¿ӠɠŲŠŀԆϋ*bPý:ҵȄӨȯӧ˓ƂӒ',
                            'р¨ҀήǣЇË҇ͼćҼңʅψýүһœңʙǣϊȴҳӁþДʡЏΉ',
                            '¢ёƞшЪȊӭ҈Ϻ˻ğҕk\x81ûǋ.FŗȯŵƦǼƧ΅ƕč\x8dƗԔ',
                            "ȭGƪЂȺˍŵ,Âԭѫ.êƹƴʅɠϏˬԖώǠӿˎ'ͲҗȆɡɆ",
                            'ȄҬλԍĮɣ˼ʻϐєΟ¢ԪҥҎj<\x84ǥð˶ϋлжқːΩʙҠ\x86',
                            'Ɖς¯ϧԁʈЫʄҎȼ¥ϐωd¦ιƆěɫȅñ˞ʍЎŽƘȡĠʃԥ',
                            'ĵѯ¢ҁÄɎĵƨѩ\x8b½ʒЧҝwȦéόčσѱŰјӇǥ˒ҏѻ¡ğ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '\x82Ƌй',

            'version': [
                -1253196572898836956,
                -1877589569119899504,
                -1208982475476643530,
            ],

            'location': [
                '˙',
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
            'name': 'Ξ|°ɛсϣƉ«ΰʒВʛΡ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʞƩʆ',

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
            '$': 'ӽԠѹӾϪϯ\x94ʶӲ΄ñӧțĩϼЛʛǜƿΎƭȦÍҹĻԖԩρϲҳ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 1957476430404603517,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 900332.1551131877,
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
            '$': '20210208:212309.124727:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                '\x87°ʼū¨ҪʉÂԉɚ˝ǑҊÞ҅żkƌ˓ӧł˃ɸϪŤ_Pƅ¾Η',
                'ƜҲЖѴn˱ԐзЩŤǡӶpҲ)ĩĻеɩĲǒЏԇ˭Ԙˬœǐθʣ',
                'ϸǠ΅ȬƳʦ\x8cкəиӗҹӠĽ\x8fȾµϲɀŹɭ%ýȷśҔѯŧɣȞ',
                'ɪļѶʝӘǋĄԒÉ\x80ДԣũсψёÆϤɿ˓шϙ˔ӮДХ\u0379ʟƈӏ',
                '˞ĀϤƑҔĎѐҴҭʜя˟ÎųӵǰɵԏЇԊѤĐԠѥǇϹōE®Ϻ',
                'ϕľɩПВħoҾͺōŲ/Ϯԝϴ˶ɼǱʦǰЃɓʚƢȷŇīȽΊу',
                'σƤƯӾȳÿјǲχԑȪϝ§ǏҮǩŘţʕɠѺөȪһӿǜ˚{΄ɤ',
                'aƍΞƧƱɽȾÿɫŊʸəǈŒúҍԮƢ@;ӼģäɄΫϨƸ©ʽӲ',
                'ʈӺ\x94ΰ\x85wÊӺӣɸӎĊǗӐǱɮѿQҖŏԚӌ϶ϲӎϭµƴѓ˫',
                'ұїһěwuòԬɠѥЭȥƐƴòзѵ`\x95ц΄ȹ&Ŷ\u03a2Fҍ˧Ћν',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                8974361815903038979,
                891294559210549363,
                -4003731956248521748,
                3968829964296649599,
                5500163163230862999,
                4622084862429752210,
                5919972013073069956,
                8329608162066568897,
                -2907736374281091776,
                -4118397890982454281,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
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
                '20210208:212309.126019:+0000',
                '20210208:212309.126042:+0000',
                '20210208:212309.126050:+0000',
                '20210208:212309.126058:+0000',
                '20210208:212309.126066:+0000',
                '20210208:212309.126073:+0000',
                '20210208:212309.126081:+0000',
                '20210208:212309.126089:+0000',
                '20210208:212309.126096:+0000',
                '20210208:212309.126104:+0000',
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
            'name': 'Ӣҧ\x88ѫҘ˖rӺĭҀЃ',
            'value': {
                '^': 'float_list',
                '$': [
                    998538.3100547472,
                    564075.4998906389,
                    348565.7023953296,
                    24575.895663682895,
                    422044.03257760644,
                    -41296.2251842149,
                    224873.29355868633,
                    56700.44239398677,
                    566047.2814526936,
                    274286.34383408236,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ū',

            'value': {
                '^': 'int',
                '$': -6936687197254116336,
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
            'catalog': 'уƫĠßАŢѩгӖѺǮˋˍħɽΡ˼˵Ɲŭɖ˜ãгһGˍŮӍȸ',
            'message': '˞.ќ+ʌ˟ӸЩËwͳƝэȼȎԉϐέˋ<ҊÅҀȞϊЛøþІѝ',
            'arguments': [
                {
                    'name': 'РŧBbóɆќĒ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210208:212309.121894:+0000',
                                        '20210208:212309.121918:+0000',
                                        '20210208:212309.121925:+0000',
                                        '20210208:212309.121931:+0000',
                                        '20210208:212309.121936:+0000',
                                        '20210208:212309.121941:+0000',
                                        '20210208:212309.121946:+0000',
                                        '20210208:212309.121951:+0000',
                                        '20210208:212309.121956:+0000',
                                        '20210208:212309.121961:+0000',
                                    ],
                        },
                },
                {
                    'name': '¥жΐȖϦЭˬȷţҥʛǔͰˋ+ӚȎԒìƼѐɥԀ҇ӠɌɩңƒC',
                    'value': {
                            '^': 'int',
                            '$': 1900927257017598978,
                        },
                },
                {
                    'name': 'ӄ΅\x9fǣЂʦТƌӈʙѽɲåʖƢʡЉϹmǟȵŭȗПȨȗǕʒɶʭ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -8858985790747969166,
                                        -1527005235477449140,
                                        1669106259178363565,
                                        5533616882205773722,
                                        5820301849282901592,
                                        -4646324741428558042,
                                        -6929628456785467995,
                                        -4930942085121982770,
                                        -7745670224755164074,
                                        -7937738987050048467,
                                    ],
                        },
                },
                {
                    'name': 'ȷӘ\\ӆΓЪɦӶȮuĢϧ˱΅Ʉ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210208:212309.122651:+0000',
                        },
                },
                {
                    'name': 'ЩîưҍƣȶZԖϡ©úơʢӁˤ\x93Ӆ!ű˱ǇҐŻ\u038bǵТöƣʥ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        209793.18090629054,
                                        318378.02443515835,
                                        247510.48536160763,
                                        96436.52953063918,
                                        742324.0316339876,
                                        251954.17288778332,
                                        682120.9224166488,
                                        570615.3045927247,
                                        386949.8483647575,
                                        45302.9309605445,
                                    ],
                        },
                },
                {
                    'name': 'ԔǋýQ.\u0378Ӥ҇ΘċłӍȯčπÛǝӥũhҴʸЖз\x9fƵĐʞϚQ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -1596443988889358720,
                                        6461947853960770920,
                                        8792044094478086712,
                                        -1213863839938107280,
                                        -4960248022936015833,
                                        -2238214651810905897,
                                        -1473826848086256379,
                                        7813562751619179625,
                                        -3657260164561758997,
                                        4508880159688175710,
                                    ],
                        },
                },
                {
                    'name': 'ЇѼɘΖɲ«ͱ˫γέӥщз?ŁĨԪӠϥѰȃ\x92˕ѕſȺ)ĺϐʥ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210208:212309.123364:+0000',
                                        '20210208:212309.123376:+0000',
                                        '20210208:212309.123382:+0000',
                                        '20210208:212309.123388:+0000',
                                        '20210208:212309.123393:+0000',
                                        '20210208:212309.123398:+0000',
                                        '20210208:212309.123403:+0000',
                                        '20210208:212309.123409:+0000',
                                        '20210208:212309.123414:+0000',
                                        '20210208:212309.123419:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ƷѼ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        853242.385428566,
                                        86164.35642667528,
                                        129193.40802854189,
                                        362376.21713397093,
                                        -75023.22586239286,
                                        868654.0302700017,
                                        322632.9239618827,
                                        312943.5047094646,
                                        353369.79604339553,
                                        941995.2311917293,
                                    ],
                        },
                },
                {
                    'name': 'ϗģџɛơɥϼĢ!ϑ˶äǿÇʝҜ\x88҄ʸԨȟɝ\x85Ӑќ@ɍ˺Ԍ\x9d',
                    'value': {
                            '^': 'datetime',
                            '$': '20210208:212309.123942:+0000',
                        },
                },
                {
                    'name': 'ԙʢӃźόȵοьΤˊÞΝƣϏӿŬÓȏѣɴîφ',
                    'value': {
                            '^': 'float',
                            '$': 590349.4680332142,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ŏƾ',

            'message': '\x8e',

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
            'identifier': 'ђцǘкθ\x86ʔňɥȖˆͻȰƟӘѮѹȖʮҦАћѤӏƏ/ґØǤˌ',
            'categories': [
                'network',
                'access-restriction',
                'file',
                'internal',
                'network',
                'file',
                'os',
                'invalid-user-action',
                'file',
                'network',
            ],
            'source': 'ċ˴ӧâХÌĻαʉ',
            'messages': [
                {
                    'catalog': 'ВŌ\x8aˬ˘ШϿȔʢɕϡԫɇӉΊŨòӀ˗оϙΪԝʙAɺԎŢΚo',
                    'message': 'ѫvϏȀĕҐԗˤʙқǲɘӹσŞ)ɎȊ\\v#В\x86ӓhгΕˀʟϱ',
                    'arguments': [
                            {
                                        'name': 'аϝɍѡÚ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            113875501413687821,
                                                                            8503332651079661364,
                                                                            2133350095292659007,
                                                                            -166481360258974476,
                                                                            -3396841511656347373,
                                                                            5302285520047506001,
                                                                            -7620417118249685396,
                                                                            8355704990998841801,
                                                                            1026260646135041103,
                                                                            5408422870651529913,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'kпʣǿ˞ѨåěŮćȇӜѺ;нһȧȅҥʲģŝȂȆǛқńʝƛƑ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'U˃ː˓ҏϴɎԝЄƉЙѬӒʺζѸ\x95ѥȩѷԋ\x8dʰӐεѬ˃ȁĦ<',
                                                    },
                                    },
                            {
                                        'name': 'ђƪҴʠ}ʏȯǸø˂Ȟ˓˥˲ϝѵΥ\x87ҟǲKǢÊǛ˭ŔO',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            566419.3214495747,
                                                                            573128.6065437703,
                                                                            662844.6855935394,
                                                                            51256.395978947054,
                                                                            -11298.816446774945,
                                                                            924376.1928462079,
                                                                            236882.1148855831,
                                                                            -61440.98735261525,
                                                                            683562.745845115,
                                                                            919803.1205427544,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϴƐ\u038bΙüȞİԜω˜ĸHƢƊѹфИ\x91ԉ\u038bԮ˾ʷԮȓӬӾеĐE',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212309.092970:+0000',
                                                                            '20210208:212309.092988:+0000',
                                                                            '20210208:212309.092995:+0000',
                                                                            '20210208:212309.093000:+0000',
                                                                            '20210208:212309.093004:+0000',
                                                                            '20210208:212309.093009:+0000',
                                                                            '20210208:212309.093014:+0000',
                                                                            '20210208:212309.093018:+0000',
                                                                            '20210208:212309.093023:+0000',
                                                                            '20210208:212309.093028:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѽ˧ԣʪLΨХȜϣǗäˠǎǗ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ϙƌĿǅœĶ˥ϩȎʺИ˱ΥɚüѳюϏȫϋƻƵųԐшģӆxǅǸ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1072492216555359615,
                                                    },
                                    },
                            {
                                        'name': '®вçĶ\x95œΠҶ҂ǻyӳδˑύǶʬϘ\x8fĞƀѠpǛŖȀɡÒƾԋ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 160114.65682528392,
                                                    },
                                    },
                            {
                                        'name': 'gˏҔ˸ɕӉІӨȹϯˋϗ¥øξҋ\x8cѱ͵Ӯ¥}ȐЫΤʨǡԦʠû',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            249011.06998813164,
                                                                            986293.9497180183,
                                                                            342902.25843576604,
                                                                            212776.93001684244,
                                                                            197044.0141987229,
                                                                            519296.5104165821,
                                                                            648566.4308696161,
                                                                            -32404.525132078707,
                                                                            556946.5857849972,
                                                                            139252.49679640925,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'µϋǕǬΓӀ6ĐÑÖ\x9bѬσƧşə\u0381øӧÝcΐ°ťǓѰǿĢʆҭ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -119998029838374420,
                                                                            -6314071044146139313,
                                                                            -1864900626329188801,
                                                                            5946454550094755748,
                                                                            -5713818079968655019,
                                                                            7999946169991008349,
                                                                            6030650716868952303,
                                                                            4807461154498520283,
                                                                            -1032435766499922231,
                                                                            -8954973711744492492,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˔Ĉġ¦źƌʄǀCɳĶɊYC¸TÊѲˉйǫȚԐ&ô˳ǎϼpǙ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3892625249400797877,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ĵ͵ҴɼɄ«ΈҴѧдβÌÁƋ\\Ą\x8eˬҢԊӄśГԏ[ϵQ˙Ɂ\x9e',
                    'message': "ɹ˳҅Ҽ>HїХɝΏȡÜjԓĜЇԞѭˊʷƸ'C˜ƆҪНх2˰",
                    'arguments': [
                            {
                                        'name': 'ЇƋϫǭΡ-ŔʙӚӭ¹ƎҶЧΎØξʌȍƳOŕĥ{',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212309.095620:+0000',
                                                                            '20210208:212309.095643:+0000',
                                                                            '20210208:212309.095649:+0000',
                                                                            '20210208:212309.095655:+0000',
                                                                            '20210208:212309.095663:+0000',
                                                                            '20210208:212309.095675:+0000',
                                                                            '20210208:212309.095698:+0000',
                                                                            '20210208:212309.095712:+0000',
                                                                            '20210208:212309.095722:+0000',
                                                                            '20210208:212309.095738:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'бã\u038bƓҎΜҞϭуϮ\u0378Òʆ!ЊȫˮǲèǡҦ|ԥȡ$ԜęӺɥǘ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 49308.68071216138,
                                                    },
                                    },
                            {
                                        'name': 'ӘѮϦ\x80ҖεӽƒԂʇȀǵˏԠȴǉ·ŏ˽ӥѽy',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '?ʬԏϳҟšǠҞÔƌʏϧķϳÏzГƤɋʼˏ˱*Śͽ\u0381ûąɀ\x8d',
                                                                            'ғӌԛϣԬʒϣԗɟҵǼéϖʜdʢЛşĴҶӢҼӺΙωԆƍǂӗо',
                                                                            '³ԐǚɺșªðƪөȒӑӥηīҚаĚĄпѕĮΣȩ˓ˋѐϒЗӲΰ',
                                                                            'љËӘƒ҃ΓԜЁϿʖ:ӟȬԧфϴʦ÷\x8bшʰ\x96ƣӶćbѥǰōz',
                                                                            'ԫȇԧ˜ƚȚƯөӵ϶ĻАəҔҾԘˇйǬӫʜǟκµȾϦƳųϹΜ',
                                                                            '*JԛȮʐФ;ԤȬӛϼȇWɝʯōÈŎ·ӗdY˴ȬͶԫɕȚƻƀ',
                                                                            '¥Ä}ʨź>ѣǀƓŧͷMԗαЋρӠƁèԩʻΝƻŰӋɱӶɣΔѐ',
                                                                            'АĤā¢İѽҽɡӸɏоƇҼíɜ«ɍçҷͺ\x8eԪӗȮĤҖӧԘÞӈ',
                                                                            'd©҄è×µԨȭ˭ҸǏ;\x91ɓçĬ˘BƳʺϸĴ&®ǘвțɝ«ö',
                                                                            'Һʆǟ+ͿЃYӦˀͰcѱϓ\x9eԋ\u0383ÆăγǓ˂\x8cҘƅƙʢоăÂƻ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'бҘ§э¶\x96ŎӥԜʮÔďˢіҤΧѷ¦ϳǄѱÿӍµ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7385796427823724268,
                                                    },
                                    },
                            {
                                        'name': 'Α°ēǤ\x98ȤяӴèѽʢΫ˽ԜßdӭƘɷëQƌǴ\u03a2ćӪȩǓͰ¼',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212309.097379:+0000',
                                                                            '20210208:212309.097397:+0000',
                                                                            '20210208:212309.097403:+0000',
                                                                            '20210208:212309.097408:+0000',
                                                                            '20210208:212309.097413:+0000',
                                                                            '20210208:212309.097418:+0000',
                                                                            '20210208:212309.097423:+0000',
                                                                            '20210208:212309.097427:+0000',
                                                                            '20210208:212309.097432:+0000',
                                                                            '20210208:212309.097437:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȶɒÒϕӬǡŤҝήʢоššęǩɚ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ͼɿҥΦ˭ˁȦȷԭȎ\x82ų\x83ƇçRNћαɄӡ˴ϋɬÚƭʎĳƱƪ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˂ƫϴʣԟѩҒӘƸ\xa0ëŝİÝɇȊǃη|ɕұϕƓԂѡħȔʫʁз',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
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
                                        'name': 'íźIʸɘƕҀąάӬʲϺéÍŰb²ſɫ©\xa0к',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɧƢŀʹПÏпfԅŢŋJЩӬŨѺԢ\x88юԊˁĪɖÙˬ}ЉΑЌš',
                                                    },
                                    },
                            {
                                        'name': 'ЪґƻмĹÄȾƨɎ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7450644141325926583,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȄиψΦȍƞҳ¸iӺԃĹπǋíÓΦоȡŴǜΙźƖ±Őą͵Әǆ',
                    'message': 'ӷȢҝҬӿǥůΰȽĢCжӨЍɀӭɯŲ\x8dԔœƳќǞӎ\x9bϫ$ОȾ',
                    'arguments': [
                            {
                                        'name': 'OƗʢȟɄѾРӲӄǴǗǏàƉԏȎϪаƈӌүǿʉԖцÞѧѓʱЃ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            464333.39868597826,
                                                                            469178.69556424604,
                                                                            330091.254657986,
                                                                            410423.93985786743,
                                                                            16272.511697533744,
                                                                            501201.10033310996,
                                                                            216769.17272822786,
                                                                            -71619.09767770584,
                                                                            -38952.16181427582,
                                                                            775783.2549113244,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'црʠԒʋǤǟǧś½ͶεŶŽòđǔќÑʹôˊã',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8755425300603575753,
                                                                            6727869487748334858,
                                                                            -6476220149627908462,
                                                                            3407630056279114552,
                                                                            4143506103980969282,
                                                                            5854311236215425366,
                                                                            1730271956643191823,
                                                                            -2728198133017194437,
                                                                            -1102607539018218969,
                                                                            1784723076142090152,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ă@ѼҸӿ͵\u0379ĊɊʲιėϬϨƙҬȮďɳÚ\x8e<ʕκĽŤǼоϑŔ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɃϷѠԐϚţΙ¹ѥ\\ƽыЙËĎʲ#Ԝ±pȍŨΈĮɊ®\u038bDɻΌ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7585776208045683590,
                                                    },
                                    },
                            {
                                        'name': 'ű²ʄ˼˜ȍѦ\x9e<ȇʰÊìИв\x92ƭЉĒȫŧԏǽĲқƦЪˁʛʄ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŽťϣԆƎԑѥˢӕ˓ƺÍԑӔ÷˧ƿҢ˱ҹҹșĖѱѺԞԈӶǾƦ',
                                                                            "'Ƶ§ȷɹʑξȞæйƝԣƟʩlɦáΑзŽȆȒǦɈҝԟĦƘѳ˰",
                                                                            'ԑı?ϔɠƪQΕñƃΠЌԐȮˆįн¨ɾϼ)ʯ\u0381ҕӸ˷ĴƦ˲ɤ',
                                                                            '\x7f¯-»DƸJĐ\xadԣӟǼƝɬφαΪӚƔȳËӶψ\u0379ԖDҢμϟh',
                                                                            'ʗќҬʲ\x9dϊҴ ȈƽӟӳƟŗӽȠĤȑɰų\u0379҈Ǿԋӵ˩ΚԇzΣ',
                                                                            'ʜÙƂϣĮϥ\x8cΚƞ%QүĜĠɭͽƙʭ\x87XŠѶʂϖԚȈΒƙЩ¨',
                                                                            'εXͱƙ"чГȥķ\x9fґѻȹЀɣӤѠϒϣНԠф·ŇʵŅȠϰɞô',
                                                                            'Љ\x83˾}әģÙԧхϺɖЧɲǌǗҖǝɶ¨ǥԑ·Ĭ¾Ѯ\x9eӉԑŹѪ',
                                                                            'ʯОΘƉʔϘʻŖзµɂƿGϢʈ\x9cςɥȿǈуƍÅż5ӥH¢ɾΝ',
                                                                            '¦ӔǕºhС\x8eč˥ͷ²\x86åиѶĖтфҕШҘһρR˽ωŒǫ/Ɂ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ύî¨ӏɌĔĘЀɡě\u0383ɪǴǥϮįſ҅ϐѭǎОеƘľǤ˹Щ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӴUуŔιҼèéȌцʙїʕδƚς΅Ҥ\x93ЂΥuԒЄȆˠӔ\u0378ʕƟ',
                                                    },
                                    },
                            {
                                        'name': 'Т˄-ͽ˖ȍǽϠƽʙӠ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            155977.2775041553,
                                                                            892705.5126674334,
                                                                            345157.93307532324,
                                                                            500084.0682363986,
                                                                            114988.33819981295,
                                                                            866031.8515693055,
                                                                            123700.84106037984,
                                                                            947048.1189106302,
                                                                            818142.3654616666,
                                                                            689506.0574781604,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЦȶĬåʾ\xa0ԫЋQ˸Ϸ΄ǬΐѵǂHɭϣĶԠԩЊɉ˼ԕӕʟ˴Z',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212309.100406:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĊɖĤϫɡŲҸʀȫϖЋџjϪэǃɸʌѴȷÖϐʒȝcщͰϪȽɋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212309.100619:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǓєɺԡѭƚĸPķΖҝԍʰŲјBԞϵnʂǞӳ\u0383ГU|ѿ˷ʝϛ',
                    'message': 'ҸС\u03a2Ԫìϛџ\x80ЦňЋ{ĠƜϭŲŅЙŞϯͳӮǞƫć\u038d;αɷє',
                    'arguments': [
                            {
                                        'name': 'Ȉ\x92Ȼряԃƥӓ\x8bǋӷ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʢӫʖƁçĭǊоӂȑηȁʅ˙ˢɯӬҋʑʸ˧˭Хы˩ņԧǵϷʁ',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΔŗѰĠĴ\x89ˎćӾĕά£êΆЀҪ·;Ȉľѕ˸ąэʜԀć\x9bѲð',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            104540.62422112937,
                                                                            387835.0403770969,
                                                                            758272.4367066277,
                                                                            82803.26846800474,
                                                                            846056.5731800963,
                                                                            262171.49676015857,
                                                                            923960.8441266386,
                                                                            929065.5908194205,
                                                                            710701.7778434057,
                                                                            241271.27526160126,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɭeԥԗ˚ɗƀŖŹȕ҂5³ҘӁ½°ԓĜѱҞЅԘʡɫƇѮöӺҖ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            531794.0247645474,
                                                                            -70023.76827188552,
                                                                            800916.0115856426,
                                                                            244809.90511027043,
                                                                            39313.24239258739,
                                                                            447189.7759247987,
                                                                            190119.3347288192,
                                                                            771111.5217326676,
                                                                            819271.8821497818,
                                                                            531525.6652528658,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĻŌͰҖӟŕkѧȘ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ś¨ØƻϥӪǿκŰʋİΜтϲȪϺԏŐțɂϨѸȭƭ˟Ϛʡɶɭө',
                                                                            'ʪơώҗяѴкĹǇŁҶаƬȰ˻ϷΡӎӱ÷ԄƬW˲ǰRŖɧʽ9',
                                                                            'сԖôүѥțѓɾАɶƪҤ\x8cϦ¶DÔǮӻԖӅɨέȪѺŅʇÄƲӮ',
                                                                            'ϧƨiǢøίΫk\x8cТŇŹjɏвŽ˪ƍѼɪ«ÎΏWǬϲȍ˗Ғk',
                                                                            "ǫŬøϲĄȁ'Ð҃ƮəȒĳpӗ[ʮǿÉԄɯƠϠ9ƣ˗ćњөǐ",
                                                                            'ρƨÐӈӢԥˣцЄĢԘɚƹņƠԬǈ\x92Ͷ\x97Ԅ$eʺИӺŻȰƳÅ',
                                                                            'ӸƘѰ#ӌǣ(ԇНɌ>Ͻ\x99ԅįԖгЉϜӋťuҦƆͿϴχŵʀЧ',
                                                                            'Ŧӳ˖ҰΗʝЂŚșÕȾ+ɫοΌφʡ\x81¿Òħ0ŸȉǇѬђǀϔƌ',
                                                                            'ˀɻΑŖξ\x9aƑȗвԃ˞mǑЛЦЦͶʮ«ȺΣЇɬϊυĆɋГȡ˗',
                                                                            'ϋ˖¬цҋґʤ>Ӓα\u03a2ԅǔΩāUUԈΔκԙϢƏǃԇ˝ρFɺЄ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǝ\x8aәȐϱ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            365317.0440809136,
                                                                            20481.473577835437,
                                                                            162501.37123880972,
                                                                            464384.4405575602,
                                                                            804985.2879407292,
                                                                            651154.1869017718,
                                                                            907532.150992282,
                                                                            802396.8998898466,
                                                                            411190.4821057928,
                                                                            115640.78129330129,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'éƀƀŰǲɡȆϯŲƆˬ$ǄӵŸʛŵđɡÊèӨä:ҜЀѴĠГǼ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212309.102690:+0000',
                                                                            '20210208:212309.102703:+0000',
                                                                            '20210208:212309.102709:+0000',
                                                                            '20210208:212309.102714:+0000',
                                                                            '20210208:212309.102719:+0000',
                                                                            '20210208:212309.102723:+0000',
                                                                            '20210208:212309.102758:+0000',
                                                                            '20210208:212309.102768:+0000',
                                                                            '20210208:212309.102773:+0000',
                                                                            '20210208:212309.102779:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'yü<ǣэĘϥÉȢƳʝϬ˴ȒʡѓȧȡĚˣΕӱɽǩϦɞШͻæѷ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'PëâʋҁiƛпļдɼĹƔ˓·Қ\x81ȑʏреhԒˋHѧ˯Ȋ®ͽ',
                                                    },
                                    },
                            {
                                        'name': 'ĳ˧ϫäÌʡƒęēŤӜлŘӛÔϹˊ˕ȇȮʇ¬ϜǜĢʛ*ѷ˜ү',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ǘ"`ʞʋ˶ˆɠ\x83ԏɔƕĆѶӬ\x85,/Ģô',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '_ǙЂүϦǕґÌ˅чĠНθЗϕϼǙȁƠ}ėĘ\xa0DÇŲǉԬǄϥ',
                    'message': 'јҩ_öƱìĥЖϰŦӧj¤ӿ¿ӓ}ȅŕӫ\\ҁӀƷͱʂϤďȰĀ',
                    'arguments': [
                            {
                                        'name': 'җÏĈҔӅħу\x99ʢƙcǷ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4006649227224648948,
                                                                            -2732185478703586132,
                                                                            -7744424154294150221,
                                                                            -8375279534182610448,
                                                                            -3209680058873160109,
                                                                            80674299961763622,
                                                                            3341681460915258476,
                                                                            -3996328488528061844,
                                                                            3420887531912818312,
                                                                            2972416831921047790,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŤυӡǞ·Ϟӣ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212309.104069:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɊҬѧɲɼɁ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 737692.1448391103,
                                                    },
                                    },
                            {
                                        'name': 'ЮȩǡιͼҗȺÀʌ϶.',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƟӠʥȔøĖª.ȜŮϩлϰ¿˻ΫӝϹƛҁđʚͲѤǁϲ˾ԙЋª',
                                                                            'ÅʆцɝԭӜЅĈǞZΌβǟϟǨҨЙćÊīҋǑʌμʱÀÏԉεҰ',
                                                                            'ЯЁȰƟʷČӟҋϵȅòҕˁęBɉɈĒłɇȌʦɈΰÛɑɉ˕ȸͱ',
                                                                            'ɲдϏёôČƧ\u038bҪɤɠȇİċѳʦǕķЬ҃ȭϳżЎŊĶαΚ\x95ϭ',
                                                                            'ɪрӞĎĬžйƾÈ҇ЉΦҍʠƶγ˗ɚΧOЩӠ˩Ϥȍȧһ¼˪Ϸ',
                                                                            '>«ŠIξ˴ˮҹ1#ˋӋɷƾΉȧԟҘ˫ҵќϯӢԮҐүʳǝǢͺ',
                                                                            'ҋʖ˵\x9eοæȿҤĤQɠЖΣǃ˅РҋԍљæąҪ˓Ŋ˩ʨǕІÚΙ',
                                                                            '˔ӽĊɱƥБμӇłMǶŔ˰ϣԌ˳ʹƘĮѥάΘʧƛѝӦ*Ȅǯ%',
                                                                            '7аƤɆϘǉĒɹΗũΝ\x85ƮÌЅư°˥Ųқ˼ňԉˬAǒŮĲс[',
                                                                            'ѧȡϹǡЂ˭ȵӧ·ъǦ҄ǊȠʏÚĉFǥƳȿ¯ƛѡÃJΝ¼ȄƵ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŚǑzѯǈҋ@úǿĢȡНϼƱшsΘˤŤþҶƺˊѼưĭ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2445136656717910938,
                                                    },
                                    },
                            {
                                        'name': 'Ŗѩ˩Ӌԕ\x84ҕUɾlΏӻԍīίĸӤż\x9bɞʝǣЛлԕηËŗɫǼ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 781036.6350410874,
                                                    },
                                    },
                            {
                                        'name': 'ӭҕоϔДˉǍ¸ӮɺóІʞБΧȕƼАϳÙý¥ľƋB\x86ѝЙʖХ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4084503847624510466,
                                                                            3211869545890339609,
                                                                            2503985266210693832,
                                                                            690121487093225990,
                                                                            -2495156062831136290,
                                                                            -325943815207616312,
                                                                            -5229506986743739089,
                                                                            -2416061176418186126,
                                                                            -3243815658607362046,
                                                                            6065938178300853846,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѕӣΣѝҔ9юѰzӨöЏùҋǨПΏяϒ҈WӢҮʰҁӻǧѵʽƓ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '9ˏςǌԤӝϬT#\x90˸ʸLŵ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            942936151376905542,
                                                                            -1537744593173413645,
                                                                            -3030064271918115260,
                                                                            4978587935484083563,
                                                                            6330197181702498658,
                                                                            -2813757447215938155,
                                                                            -7868040442433378017,
                                                                            -4652680697692886369,
                                                                            -9056373189065122975,
                                                                            -6856530555394228439,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƣзɆíɨǑ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 606735.7177436942,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԗϻ\x9aƙƇԃʸƻӋďͿ²ӵӸºţɵўϡюзǊŤȧ·їԨȄӲª',
                    'message': 'Ϊ×PО5MʅԠԅ˵Ь˜҅ϮʚǘΊЃþΠͷӨſόȴȃ[ˏ{Ɵ',
                    'arguments': [
                            {
                                        'name': 'ʚԡӓǓʹ¡®˵ƍΩŃ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212309.106239:+0000',
                                                    },
                                    },
                            {
                                        'name': "ѤӏɋьĭȚǕÑɬÆ'˧ΧԫrϟϖˑСӨkӺŰӝú",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2543703624375838297,
                                                                            7005019393370124626,
                                                                            1134795172840701037,
                                                                            5242901556305024202,
                                                                            -5729722330830314134,
                                                                            -4289686297404438530,
                                                                            -2130209450759123380,
                                                                            -1382334557754887077,
                                                                            -5974536772298189551,
                                                                            1442705756136800795,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŵЅȎxɖAʉϯѧҌʍÇĒ˛ŲΨȭ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŹӼӼļοƦϗӂfȊ|6υŕѻҕǂøƶμȿтɌ£ÊХʓѨVҔ',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǾснѢ\u0378èеŧр\x89ҵԎƬÄĞÊǉ\xad\x99lӑƕ\x94ғͶŭç',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϛʘӂӺĵ(˓ӂԂ\xa0ˡý)çʄÛγoĉÙԕǕƯƲ\u03a2ĪǆõӫȀ',
                                                    },
                                    },
                            {
                                        'name': 'źȨũψԃѭҼηϖȦʄш',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': "҂ƹȃƭїŕЌԨȡİ'ѥʱ",
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'jɀάlƒ҉ΡҼˠyєўåÔԙӂȆŎӄӍάŘɤψѓӼ\x8cưͿӍ',
                                                                            'ӻʘʠ\x99ұ\x96ǈOӻζҁńʥƈȊǐàƜз¦ĘσʄŀɢҠ~Ȼɐ\x80',
                                                                            '~ĻɸËȨÖŜͿŁЃó[ȧҖɾǏæ¶тϑӽҫ˱ΟǺĀèȻӆр',
                                                                            'Ӑїˉǽ\x99Ѝ\x7f®ΪUϘҌ\x88ŌəΪԬͳѡЫԥʗȗŠӒâŌҞЬһ',
                                                                            'ѡ\x90ϐ3ķˇˈϮԕΑÃҿīlʒ\x9eӶɡËԩамѕҭʷԒɎŠČʞ',
                                                                            'ιјłˑǥÿʧϷPѽ˪ҲѶТüĸӁƮҏ˭>ǮɆҢɯʿŶàѲƾ',
                                                                            'ҷǜʗʲÙίњȏ΄ϬҁŌΞԒ\x8bǠ8\x8fӆFàάʰŃ©Єʯē<ǃ',
                                                                            'ãĘ>\u038bҠˊһǶĤɭȇȁΑϡĩҞ5ĒԅΨȔҼ˽ĒϿΓҜťȕƠ',
                                                                            'ˡyҒŧƪȼ˳ƖˆƩǖžȎ+ґċÅĶѾȯ\xadЍŲҡtғǱ\x98üМ',
                                                                            'ǭƶʨĨŵԂƕѕϕɟƽ¸˓ҬМʵӍӅюҺŹϳϗƀȌȼҧ.ɪҜ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȯƇƷƗSѝѕiåξɂӆпԜΛӂ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212309.107786:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƥȂьϱӕЌɉ²ҳ\x8aӱԙУйœ˫тö',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -578310495597970592,
                                                                            2486663727005261746,
                                                                            563240701678721028,
                                                                            4064655611752976545,
                                                                            -7861433046629178166,
                                                                            1303048683464443781,
                                                                            -8556072469689472650,
                                                                            2225104028311267458,
                                                                            -4872016524321197134,
                                                                            -1511664047566136386,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '´ʠˍΕѸʐЃŒԋ=',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'oʽŔшӵƙ[˼ƷКҿѴ˰¹ǆР˻ƑǪǣÙңSɎɒźȵǀŐп',
                    'message': 'ÁɖϱшȮЇ2Øĝ˅Џ\x83ǁůɼłýG\x84bʙƳÌɺɊηΩǙχZ',
                    'arguments': [
                            {
                                        'name': 'Ǽʬ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212309.108598:+0000',
                                                    },
                                    },
                            {
                                        'name': 'И¢ǅ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƟǬ6Дʚԅŏ˰ǡĊȅԕˑaάѠȖ½ȥњƪȇʙҨЅˑŀӮʡʈ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212309.108911:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ЖϧJңЂ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            329580.0312388147,
                                                                            272401.1149939736,
                                                                            985671.4441422164,
                                                                            784064.9001243759,
                                                                            481764.4259262673,
                                                                            588209.3535015838,
                                                                            220925.06143912429,
                                                                            303349.7799744362,
                                                                            225343.88577248942,
                                                                            548825.271728879,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȚԃҝпA¯¿ȽӟȒϓ#ēѰˮćáԅĊȇѴ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            701375.8298546086,
                                                                            348866.84322273545,
                                                                            798038.9982011667,
                                                                            -10335.331204866743,
                                                                            -21621.814005627937,
                                                                            787037.5951244669,
                                                                            47651.44421030683,
                                                                            92871.33081236086,
                                                                            749631.5891076957,
                                                                            561425.3419831707,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'íɴɹӭʝα˝',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212309.109860:+0000',
                                                                            '20210208:212309.109888:+0000',
                                                                            '20210208:212309.109909:+0000',
                                                                            '20210208:212309.109925:+0000',
                                                                            '20210208:212309.109943:+0000',
                                                                            '20210208:212309.109957:+0000',
                                                                            '20210208:212309.109976:+0000',
                                                                            '20210208:212309.110010:+0000',
                                                                            '20210208:212309.110029:+0000',
                                                                            '20210208:212309.110041:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\\Ψ˫ÂʈөϏèŕѾҪǁ\xadȲϕӥ҂ԩƊԀɁǨɒЍƬΣ˹āӑȆ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ϣї(¹ɪǮϽ\x81ŅʍʸлȲàǔȝϝԏ$ӡБKáʹ҈lҩϰÍώ',
                                                                            'ŃϚſÙǨе-өɻǃĢӯǞÛСӖɚͺŊ\x9dʓЛͿԭѕȂǷɎΖ[',
                                                                            'ȢmҺǖ˟ȣѨȉӹΗì˞ӟɌĲԇȊĊЂȼķӀѥcʫѼe8À΄',
                                                                            'ðˏwȫʩˬϪϷβēРĄơ\x98ɑ\x87Ϧdх˴ÌȏǣьŦԞơӣĬÕ',
                                                                            'ѾжȺʳɓƴʫĳeȌÊƺʹȠ}І\x98ZʿЌӔ΅ыϚɹ¨Ǽŗɤ+',
                                                                            'Ȉ\x96λ¢YJ еȅǤ0.ςѵ!¤jĂfԍҝȱċѰƸ×ʀɦд\x9b',
                                                                            'ɦxÿҁӨποź˪ӫʘȨǽǫʫυʣ˦ǶхÀdɭѓ˫Ϣ<Ӱ\u03a2h',
                                                                            'ԇӘƻ\x9d.Ӆƕɸˁβ˟ɦϱԔϨïǴÎˮɷǪϽťÁìȋ\x8fѤΚФ',
                                                                            'ҸˈΪwĎˡ/ūțUĝ5BиƟɹθɈӿЄ²ӍåԜȱģіȸӗԫ',
                                                                            '/ɨзПЧϴɨɚ҇Õ\u0383ǗǜԕƍŹӀͳƲйҰɚј˯σσǫǔʪÒ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǑĜԤ\u03a2ĝƥԢ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212309.111863:+0000',
                                                    },
                                    },
                            {
                                        'name': 'žÐЋ,µѥɇŎśϔҹћǇʳҡǷˀ5ĀĈӗ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                                        'name': 'ȠԐŒуĝɱэƖ»ľƧtҖ ˢdҒßΘϧÌыΥѿƪѺ)ѯĮӭ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԜǏҀԘìψȴΎѕϹɞΤǈ˟˭ǔѢ·ȞƄǝŔλƮ',
                    'message': 'ҬƦ¨ÀȮϥªƕˎȂǡ˅ÔńƵɹЩȒěԮɲųɦ@њɲҔķӔ\x99',
                    'arguments': [
                            {
                                        'name': 'Ҩď:ˑͿΤԕӊүōăϟēĭҾҔAяǄîҪȱˌ˪҅ǘԦʬ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˆˣљѻЗІΪäȍƵį˹ ĚżɯНҼӣί;ϊǓǣǭ˩ӥƫɰυ',
                                                                            'ϺҢДѶѠѻɋÌ;ӄҒĄìҢͲ\x8bȠϭNʶŖȔÅΤλ×ѿǠʩȽ',
                                                                            "ĦřŪθъҔ'ƈ¡гҪʸԧϾЀѶhǮǧˤǜŊĻ$ԦĸŞȞȧћ",
                                                                            'ʬb$жүƖ˻˲¬˽˒ɲɘϳǻ£ԗ5WҴʝüÄϏƢӶɞбϧƮ',
                                                                            'ǓAҲʠǦҶȡҨÕXāѪƜƷȫʔǺƼϓÆǷθ˸Ӳԥћyåҍф',
                                                                            '\xa0ĘΤʯѿĨɅʁǍŹΆƁƯ«ĬİϕεuǳѿΫΌԄʊeʸƾЙˏ',
                                                                            'ĕҮȣ\x89ӴƠӅg˴ʰŤ\x87Ĺй˓ǍʊҨGłʖ\x80+Ξ˝ͺԎҭґˇ',
                                                                            'ʁɚ#϶ȬЬϻЮўɘ˭țːȬǐ#ЄĉǧњJӄ\x9dƪͲ˃лɖÓɧ',
                                                                            'ӮÒvĨʊǥ\x96QӕΔɩԣMζ<ʥǒəӵĤ0Ђţ΄ĺǘţѤˮ˓',
                                                                            'ыʚʙªBºƾʟ+ӳԐѯƽʭʯ\u0383ǜƀðӸƛЕа΄·҉Ӏkϡ˾',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԉ˷ʻż\x94ĳƠԁɂȽ~ŝŚȚӖ\x87ʽҀϻ\xa0;ĿÃҚûøŉƁӍΙ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 820327.5860550636,
                                                    },
                                    },
                            {
                                        'name': 'Ѵƕĉҙŕ¾ӾЛɬ]ʹЄκғʨȹģʛ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210208:212309.113398:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӏәʖǼʌљѸǁʜǿȃʘŁČԜʙєѓĐĪ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '`Һ҅ĻîǤʓԄGɫА9ƒνåЭ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 771100.1072549486,
                                                    },
                                    },
                            {
                                        'name': 'ӳ҇ƱɝҨƿ˦ʗбˀŁ\\\x91à˅ǠҗĆɻ\x88Áʤƨ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212309.113788:+0000',
                                                                            '20210208:212309.113798:+0000',
                                                                            '20210208:212309.113803:+0000',
                                                                            '20210208:212309.113808:+0000',
                                                                            '20210208:212309.113813:+0000',
                                                                            '20210208:212309.113817:+0000',
                                                                            '20210208:212309.113822:+0000',
                                                                            '20210208:212309.113827:+0000',
                                                                            '20210208:212309.113831:+0000',
                                                                            '20210208:212309.113836:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Čȵ˥',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ҡƼҾ\x97ĪʔƪϮʽÝϭƓęʧ˃ĲѰȳʶ_ɍͰΐζԂĒҸʿǃԏ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΡƮԌ/ӋӥƯ¹Ψė\x9c2ɻа˧Δ>ҕѣˣв<Wɯˡӳ,¦ȹȎ',
                                                    },
                                    },
                            {
                                        'name': 'Ŋîê',
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
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӨȏƺІώǉˁиˇú_3ΝɀԚϲӇιϽǰJÁЈ#¼ˬ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 244126585907017402,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŭVɞίǹ҇ɳŨȴ<ůҌɋƈËˑɥɥԏŕЋύӇϝŗӊûĶ\u0383Ũ',
                    'message': '͵XāϰȈͷƾгАʘϗȠɴӐĐfѸmƅĳˆȣƨǢʳȞɈѡǢͺ',
                    'arguments': [
                            {
                                        'name': 'Ύв\x97ѼȼʿѼǦæ!',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212309.115370:+0000',
                                                                            '20210208:212309.115392:+0000',
                                                                            '20210208:212309.115398:+0000',
                                                                            '20210208:212309.115403:+0000',
                                                                            '20210208:212309.115407:+0000',
                                                                            '20210208:212309.115412:+0000',
                                                                            '20210208:212309.115417:+0000',
                                                                            '20210208:212309.115421:+0000',
                                                                            '20210208:212309.115426:+0000',
                                                                            '20210208:212309.115431:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x89ɲЇǯͶϵȂӲƌǿˡzӽǖȸIӻЅƗɿЄǀӿ!ƱŘȪƀÙŐ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -956357385646029641,
                                                    },
                                    },
                            {
                                        'name': 'ǌˍˮǒ{ӣ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5536820827557580501,
                                                    },
                                    },
                            {
                                        'name': 'ƙųӓ3ѼȱϖпȃȤĘǒӥ$ȃ\x81ǫȧƩûёʫ\x81',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212309.116030:+0000',
                                                                            '20210208:212309.116045:+0000',
                                                                            '20210208:212309.116051:+0000',
                                                                            '20210208:212309.116056:+0000',
                                                                            '20210208:212309.116061:+0000',
                                                                            '20210208:212309.116066:+0000',
                                                                            '20210208:212309.116070:+0000',
                                                                            '20210208:212309.116074:+0000',
                                                                            '20210208:212309.116079:+0000',
                                                                            '20210208:212309.116083:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϱүûŁ\u0378ԈĵĂ˟Ѯ~Ƞ҂ɨӬԫȍҌйЗǪΘǿЙýұ\x96ЫѷΡ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 420069422648991606,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '¨ýЪшSо¥\x9eŝͱȵƛҌ,Ͱ®ѫŵИ§Ύ˰ҠғйǼсυɊԜ',
                    'message': 'ƭ)BŒ|ȁЩΏԪÛfŵͼέȩ«uʃэΗŦͶ¸бƠɭͽ\u038bϧΫ',
                    'arguments': [
                            {
                                        'name': 'ѤĮ2',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2200500834230619060,
                                                    },
                                    },
                            {
                                        'name': 'ƮΤʧӾ¾ȟ\x99Σ$$ΆǘhȡԫϚȲЏ\x99ÓӒSƻȉ\u0383VĿÇβϥ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ҝһŤӷǖ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '7˦Ņѕ˺ԃҸΟɠИ÷сƐ«dӪ˂ɳЅɖύÎӠνƸϖˆȎϮˇ',
                                                    },
                                    },
                            {
                                        'name': 'ČңҺȎºĨԗǔÍҦŝќηΒӥљȢĈķ8ɂψӝѼθʔɤů*Ţ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212309.117120:+0000',
                                                                            '20210208:212309.117132:+0000',
                                                                            '20210208:212309.117138:+0000',
                                                                            '20210208:212309.117143:+0000',
                                                                            '20210208:212309.117148:+0000',
                                                                            '20210208:212309.117152:+0000',
                                                                            '20210208:212309.117157:+0000',
                                                                            '20210208:212309.117161:+0000',
                                                                            '20210208:212309.117166:+0000',
                                                                            '20210208:212309.117171:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԬѱЊΕȲБӮ:ѱŻҹéĤăʭҟȇɬʀȨU®Oâ˄ɜ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1901286676358018089,
                                                    },
                                    },
                            {
                                        'name': 'Ӧ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210208:212309.117522:+0000',
                                                                            '20210208:212309.117531:+0000',
                                                                            '20210208:212309.117537:+0000',
                                                                            '20210208:212309.117542:+0000',
                                                                            '20210208:212309.117546:+0000',
                                                                            '20210208:212309.117551:+0000',
                                                                            '20210208:212309.117556:+0000',
                                                                            '20210208:212309.117560:+0000',
                                                                            '20210208:212309.117565:+0000',
                                                                            '20210208:212309.117569:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӌςќȖҞΣ!ԧ\x92ĬǔӪìыӪХəԅɫʚǗǤƏč',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1126387539049971425,
                                                                            4985057244422492082,
                                                                            -3249769653302365757,
                                                                            7553963140132609337,
                                                                            3635926854183392831,
                                                                            6825804209457177399,
                                                                            -2329908837133526395,
                                                                            -2186747760286296377,
                                                                            8825495233591292581,
                                                                            7844196433212276021,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Κ£Ҷſшӹȝ\u0381ԢǤ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            929398.4372738334,
                                                                            951044.8576449656,
                                                                            -41061.849190629204,
                                                                            701036.6742010582,
                                                                            467894.33112509,
                                                                            134898.72058466432,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȐҗΡËǉмҤʮQ˺ŅĻǽԏç',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8706583751536843585,
                                                    },
                                    },
                            {
                                        'name': 'ԔƝ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "ɞϸғӨԞ½UӄυͻвÞұнőӏϲ\u0378ȺȀӳ'˒OɔȃˣʀȘԧ",
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

            'identifier': 'Ҷ$ӳлѱ',

            'categories': [
                'file',
            ],

            'messages': [
                {
                    'catalog': 'ưȑ',
                    'message': '\x98',
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
            'name': 'Ġ˔ɈњƳƖӱ˗H$\x9cɣҾƿ˖ľѠөϞҹ\x9eΉэǓɺЭŨdӻĭ',
            'error': {
                'identifier': 'пg¼Ϻ˥ЪѨȆU(¸UӐŪĵϹm\x8cҩҥτĔӄ\x94ȿԝ§ϩψҴ',
                'categories': [
                    'network',
                    'access-restriction',
                    'internal',
                    'access-restriction',
                    'invalid-user-action',
                    'invalid-user-action',
                    'invalid-user-action',
                    'internal',
                    'network',
                    'file',
                ],
                'source': 'ȽϓɤѵɻȭӴţǌƐ¹µϯОǲŮĳΑʓǰƯyϯɻǲәԝѣ\x95ǈ',
                'messages': [
                    {
                            'catalog': 'ƅɵϟϨύͲѥ˱ԁϡǌʥ\x96ӆ˯ĦӃƦѭ\u0380ѓǬϩϏćĶϢҩҿИ',
                            'message': '/ũçƔi˧áΣǔӛƀņȸ˞1˩ȶΌϣϳЃјɧėыɧ\x8dǹǈҐ',
                            'arguments': [
                                        {
                                                        'name': 'ѫǬ)ȠŜоӅʪȋξћƗƚϛʀʓ»ƮёʞЛѕ\x9fӣѣȍӛ£˵Ľ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3639611951778218203,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ёQÄцɘѓВϧŉιñҟсҜ\x81ΒȼȟыʁѴɰЎӆʧɘʰǧ²ė',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212309.064178:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˥ĽОǶιӤȶ҈ʾӣĮƙɩɟćÀԂ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЅɄŊeӃĥěԩϙԏƵ\u0381ѣ\u038dĈ˾9ӥд',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ųʟԚŶǴMéјïҽʺūɌɼåɝyǗĽіǇҙɉȸҭԤȶЪƟ0',
                                                                        },
                                                    },
                                        {
                                                        'name': 'HƍЏXлђбµ͵ȶμùĬҼƞńÛпɛŪɝƒĊҍćɄʹţBˡ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ЮʝƸȠƯҞόȫ^ŸЂ˖ɍώҡõȎɩϏȬԩʀşѩϙѽӋϾɊϛ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Fƣ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĎǛҫ$(҅š҇_ѸȣȟËΝþƎØԄˣʤƱSþƁǛĚΧѿĀԍ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 896875.0537186072,
                                                                        },
                                                    },
                                        {
                                                        'name': 'L"ЗɨΘϋʼљ¥9м%Ҡ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'U·ʴѴɆŬό\xadӺȃ{ċˋśɂÙԛҦɶ+ΕĠĞȫȑKӬҽǕӹ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212309.067012:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǵҫ˴Ԋ\x9cțԓԂҷрҗŻʇɣŜʏѾɰ(ΧĦmмħqń˄ƧͲͱ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǻĄԓĺЋͱёЙӉȐƅ\x8cȓȹ;ʶБŇƿЇŁŒˣ8ʴɕŕɄMƹ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʻ$η˾hЃʥҪΩȉ˦eŭƃƮɏʶșǊԫРʆŉVʊȴДȊЪȣ',
                            'message': '\x9bψ˓ӽѠįľɟŭɌlӁ˓ԅŁΌџЎ\x9d£ҜɿχͿ˦ʂҼù´j',
                            'arguments': [
                                        {
                                                        'name': 'ŉįˌԚПˋǅʱĘɺЫЋ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ĥʁɖ²Ԑ\x98Țʓʅȼź\x96˰\x9aǓ¤еƞτӷƉҬ4_ѩҙ·Ʉɴǩ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'РɄғи\u038bʸԉȀƫϰßœŗʂѮǅϝĔʙҢƮiȌ´Р«sǯʔƔ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3663175709133321239,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӁƜǃ×fόă@ǡȶɣԤͰńʘːi¦wɕΘ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 77066.28356972928,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƅʇфžΌĕϻqТˠ˞ȓűƠƍΦȅϨȎӉҠȽÃѲȠώɠĐҵƱ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԟʄӷ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˇЙ½Ǖ˙œźчŵǌǤΕ\u03a21ҸȮÉѳÊ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˓ҕŜ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 685199.7536569504,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8cϾԫϦΙ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ăŔѨѝ#ΧаӢѦϔćˀĽŕʏÁɠʩıҧāċ˔дхɀǛ²ʶǴ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϊ˲ÄɿӟԁǐΑŜўçǇүӷȶϾSkȦŕă=Ԍ˝ϸȯҶїЖi',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӞƞЇυȳÎбͻ4ÞǅÌˋƱѤǡνǀ˖ΨӭlLŦȄːǀ\x89ӭ·',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӊWİǁѭҾĄťɧkȅŻӰČ*νùҕѫãΟϾÕηÜАtξʹ«',
                            'message': 'ɺˤÐiIѪ®ăЋϬǼȑ˜ǀԝʷϿ{ũÛŁҦ҃ˣЏBаŐĿѺ',
                            'arguments': [
                                        {
                                                        'name': 'ҳλÀƟɟɝ ԞӍĊйθґФҤ˾Ațĳцɑ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ËԨҺҿΰǨЪģχƗÕҗҀ\u0381ǣ϶Ǝ˂ʛ˚',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212309.072126:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˬХ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'фRьΣϳÞDǹѧ˨Nӵ\x9eŦ$ӣ\x7fʺrӥǰФ\x85пͽəÇ\x81øƦ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ІӦȾđÜʕƂƵϟÙȐc˧\u0381\x8d',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'xÎ\x9eǼɲʌΧϦȻ҆ƆϺӀЪlŨɯdЀʪǖ]ɌϮѦԚ\u0379ǋƣȣ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŪϵŮƠ\x8eΞƹͶŉĚѲɨţԂƩϚϯԘʚɋԧͰ˵Ҏɿɇ!\x89Өɦ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 73725.1007552857,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΪӣƖÅτ\x89ˀƢһÏӝǮоΞԁ˟Ƥ˦ʦ]Ψψ҉ŊȍЎ˱ΥБŕ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212309.073686:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӔȻ;ðΖɡŴԚƖ˳Ϭ=˲ΪùЌŔҧπiНΟƘ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Đʮүȡɞкýȼўːύ1ȯʼBӮӱL',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĿД¯Ǧ>Ȇƍſԁ˘ΥϔèīԖɶα\x9aђ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѽÐĹЌƓĽɡĹŎȡiȱƠ˚ˆɑíӊаҾȁŁĚåЌԮϑ˰ϨƷ',
                            'message': 'ѵ˨ɧѕ΅сң;©ȦĢӱґ\x95ƷϛЗԚΜǿŉѺѸƞĐҴӎˮƌƜ',
                            'arguments': [
                                        {
                                                        'name': 'ŝ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҁ¿Џπќŉϼ˳θκǷ;ЅӒ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'įӴ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '³ɪӀƊʆŌϾǘРӥ@ϺÚƸæˏ˂ǭFǚ¥ħȟѤɗҧψɟʔ˨',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΡąȷԦύАҲȂúЋҙҦǥӉОǽѹʇǿȐȤδѥҀѭ϶8ƈҠѽ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŕÚșηŻϮϬ®υʵqý&ǙĕŇȿѶԪьpҶҜÏϬˢ=їĬɮ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 212878.91955383023,
                                                                        },
                                                    },
                                        {
                                                        'name': 'çȏӐˀɒƐ»ҘԞÓʌˉģȧѷüǞɅ\x81˙\u0380y',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͳȄͷ\x83Ä͵òƒĻΤϸћҌӕƠȌʈ˲\x8bƲ\x8fǃ\x87цĆʡ¢βȠψ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212309.078205:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˡßΐӏƔɢÄ+ÏӶ¢ǔ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ļȳΔǄfʽˮҸɁϔғӻɎӐӇȼŷъԦ\u0383ΡмʜŨţťɎК',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212309.078568:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϵәΐȼҲƥ1ÈȝдȘѧԢ\x99ʹȎԙō',
                            'message': 'γҽΈӊʹ˝ҏAAǧŎϕҾ«ЈΚԫўʥҥđ¥ƒÐıȞȤǚΗ,',
                            'arguments': [
                                        {
                                                        'name': 'ʶԞŎeɐџdЎȈǢȌɺîBŐϼ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϫѤ˪ΟŲΉЫî˱vчҧț\x94ӡҤÏͱϦ҆ԦĽ\x91Χϯ¾ҩαҥƼ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɲǔњϓÜϳϪѪќĳĐϵӆѵӅhҖ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ςӉzҳԚѲʳξ¾\u0382ơѬїȘЀ{ɗɾɡҜО\x91ƈɃƦ˄҈Єƛ҃',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɂӿҜԕСhƉɭǫҴˆąѕΧϹ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ģ˚ˤ\x9fȼɔԁ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212309.079806:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'υțoCԗĉ˻ΞƑҢɲЉÖÌɑЌΪϢΓξ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ':әÿКǰŝˍҌԠӶƏ˫ȉЦˁɼʓԩıŚ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 864569.8814439614,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɘʀ˹ȅğϟŢ˚ӾЩƀ{ǷҌѴΌǼƝĊ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -34581.27303775147,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8eš˽Ŏи}ʫ\x87\x93ҽȨgdľӡ¿κρɓ<ҘėѽЩˉūЩ˴ϗԡ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҮϠ\x9bПȡӏ\x9aҤ\x83д',
                            'message': 'ҼƌԄ7ԗʣӛ¹ЅӻɛѼÃɱåǋӋ¦αɹÎɡӞƠǵРώʐϡ˭',
                            'arguments': [
                                        {
                                                        'name': 'ʿ&¢˽ÂšяƕɁԁŶ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѾέŝkǨζѽр҈һϸƖÂȱƕƞӓȊ˝%ҕѤҡ®ÔǘӲ\x88ѣô',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ůɵƂºρɕȄěǅĪΜιŃȓԟȊʐĚәǣ=H',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʄόɀʕɹт˦ӱԗĒ¶]øɉӅǄγԏȝƤΗԙďћЮŴЉҠƵƝ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǆ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212309.081297:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'NԢ˯ӅйŠPКϫϸ\x8cİɿ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˁȼǅҶǃԇ\x9bҋ˝ûȤҘԚΟϊ˷ɟϐ˰UîԮȇŵƬҚНɵȼ\u0378',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Żϋ΅ёɛԈUŌ˶ÏʆƗƯѫаѰϪ©ʼʉШӽё\x8c`ѪӜĈMӫ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƚkА\x81*єȳćÖ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĐʇǴŜѢȝǭЉɕ˕ˊʺ#уζȖ˲ҧǝċϗť;»ʠЈ´ő΄\x98',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǪǁÙӿǅƕҟ˩£ǥťrȏӯǙȀŤҏ÷ȓɊӭ\x8b˗ЛľˇǿͰp',
                                                                        },
                                                    },
                                        {
                                                        'name': 'җΜϼ\x94gѸΒïɅҊ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 969198.1028616799,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӫæԀŽķҮǍĥβԪѠ·ԍҤįʹ|\u0381ɛҞј¼ɇ˺ÜӕǩƋДÛ',
                            'message': 'ƨʸ˶ъùΏϑɈѷȱήԖ\x8cаüĨeƲжȜ(Џ˷˖ʾˉɶҏőι',
                            'arguments': [
                                        {
                                                        'name': 'ï',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŸԍȠŷΚӃӓǭʾҀЬϐ˫3ɰǩΰ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'őǤ(ӖΏϰǞҭɐҧϺӦЬ×/\xadσʤȐŜӌǆǔŴǺ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѧ/QԦèĤʣԞКŽǸ\u0383˖ɿ6ȤӹԩϟҿÀãӧƐț',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӔȴȞʆɋ\x99eȥĦĬϚ˺Ԁɻ҈Ȩȡī\x90öэʜ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'þÂÎϦЩʈǛцÍРʪґŨϨäу¶ǏΐĮɓʨ\u0380&ʱĸΆKØҶ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5177812195513031138,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԆƆƣ`Ԁ˲´¡Ҷχ˞ΨԬȿpϔҋψąӯįȭЙȯԉ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ОѓϔƘҠѮҬƉԅʌЯąϡαģÊrwǠŊ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'δҪӨɃχΆɫ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѽů\u03a2ȊҢѨɈƋ˨oɔѠǨ˚ǨΌ\x96ņźϷΑқΡӽѫѨƓϸôˡ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '¡λοǈϒ˘*ƯĢɕѪˡщɸΌīȎɍɛʛűвͰʱɥԡάȲłҹ',
                            'message': 'Ðũ\x9bƤ°ԬĐͽǏȽõdǋСʯͲŢИɧßԀˇȓԔԏǑăάӸΊ',
                            'arguments': [
                                        {
                                                        'name': 'ѴJʖªɥ˯ǖӃӁԤEӟ&ц;ρϲЂǷø˶\u0379ŔʡθԮƏIЛ͵',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҃ʩïπɦʼιԜTҊҤʘĕӵÓɣδ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǩγǜνͻÃƨHҾϐВ:άůɁȫцʰĿә5ťΗωŖ˔Ԑӑʗˋ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212309.085146:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŀ(ǗȊ˜ѿ«ѬCяԇЄǵԘƯΟɅWӈǭȀЉѷ0ӢЗӱԝϲd',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4938000226863677217,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʀΟыӜRӊΓȲăӦԟΈɑҳƔӋŋ\xa0ϠЁɔʓ\xa0Νˌҕľ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƭѹʢȃ;ѳСќЀτӀɺƍӑίǤҍѦʏ\xadʤɻёɈύ4ɓŚ{Ѣ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7798875520094072294,
                                                                        },
                                                    },
                                        {
                                                        'name': 'αɠÍƐӝȸ\x86ЍηТC¹ҔôѿӸϹӎȝΑʽҁʮzºɛjŲƲʁ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҮАǺԅ¡ԫąœԐɜп¯ÕҢщԭȋʊɾә˃ԠÖşˉϸ\x92üЙǣ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '˾ҽ҆ĕΐ˱Ħђ)\x8eˡƵӂѼӟnѧи˝Ѿĥѧ+īόǓΆɐхЀ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԧѻƨ҈ȺͺԞԕˊÄӏҩ\x86\x8f"',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɟēϙʰđԍͿƍ±ʎԬɜ_zƱŅÑǴȭɌ´τёхœƖDҎӄӐ',
                            'message': 'ĴӐǫ\x9bʉ:ȩͶËȝd\u0379ȴĳԃ¼Ȏ˨ˑόþэ˩ĘǆŊӥҵĽЗ',
                            'arguments': [
                                        {
                                                        'name': '!єŧûA+ţŝϷԬԭɈΊʚ&ŠϼzҾҊˋą2ȸàřͲ)íˍ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'IώƈлǘǸдϧδ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'šˊʺ˒˗ȫкƧʣŢȫȝŴ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6557681765862090466,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӟɱ\x98ŃΥǈBǲǝԬĀǲØȼœ˃кʡȑƓ˭Ųүãљ~ŝ°ԓɁ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212309.087308:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƣŌŏҬϠˮŮ÷ѣˑѕǜ˓´',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӭԄЭЍ¥ǏԀÂ\x91ǨʍӷͱƙҸeæʠI£ϫдϵӑаΗyԢѰĥ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'AéJǭÏԞ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЦњǥŞәQђ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʥÄˆȗȓęȜ\\ϗˀȱҿ®¢ȑǙĐԝʅӾҗ҇',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȭé',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4524282681109613735,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҜˏϚōn!ϰZö˜ӓįӯԌõŁèėВŠáԐЊʝГɰǃƽȣς',
                            'message': '΄ϭö*ȴɈԜΜĕѯϙěǌɕҲϝʕяμɹÜʩ®ƧǒͶÖɣFƸ',
                            'arguments': [
                                        {
                                                        'name': '«',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'пΚCĻŒuόǭ\\:Ойү\u0379ÒҸϦǇÆư¸ˠʶҎ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƱĎӡŤКǭήő҃ǧǭ˔Ȩψϧ\x86CәŤөƐ\x9bǵ¨ǽæγϽ˞/',
                                                                        },
                                                    },
                                        {
                                                        'name': 'AҡƊʝéƌя҄ʝ<ßƌ¯ɮԦҝԂΝƇҨѯƘ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӶˮЂƅɧͻЦҕΆ§ɔƿ©Ɯ˟țӎʙǏ´ғԤÃƕʂԧϳΘʶĞ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҙˣ\x94\x98э\x99ʼлӵā1ғʢşʽͼñƸƩŇĔΖҮÏԫюǣȷχƞ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˶ĴѿӶϻƌͱǅ»Ъ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'éшOΐɠȼԢΟҳȭȏǆ\u038bԁʲʪéқɃѪɚžƖÕƔϫƀҘҍϫ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210208:212309.090012:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǊҰÎɗƎÂîťŭLӖʡNӚԄ«ɗƱϟѓҍCˑȢϘ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÌзыŠ´іȻˊԕΒԪΏŏѣƘ˦ŖͺĻņкćӽЊ ʯωΠ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǕĩʱŷӍɗ)!ԠǕΥ®џǹΠž',
                                                        'value': {
                                                                            '^': 'float_list',
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

            'name': 'Łθ\x80',

            'error': {
                'identifier': 'ьȷҙʮʐ',
                'categories': [
                    'internal',
                ],
                'messages': [
                    {
                            'catalog': '\x8fʏ',
                            'message': 'ш',
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
            'event_id': 'ԇѡЍƒ;вȮȜπĞÃϸԊÝҽśMн·ϴҍӔЅГԛĲCс\xadɃ',
            'target_id': 'ƽήŋΘµ"ȝҭÈʓΩʹ\x82ϟÌѨ\u0381ȱˌˢΫ˻\x9c]ЁϋʤƺͱӸ',
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
                    'event_id': 'ǭϖԠǗѲӄҁҔƜЊĥЦȤȕɰȌ҃QÓǋǏʴθ˭ѕŻҼ<\x9eƭ',
                    'target_id': 'ȲīǸЛȠǸ[ŔȲƐȞÂϝѬl\x88˕ћ)ұӫрXÝРÂǎĀΗą',
                },
                {
                    'event_id': 'Äńөϴȭґоοìŕ<Lɤß\xa0сŝhƧηȮ@Ĳл\u038bӯЁӠѿ¨',
                    'target_id': 'ʒϱ"ӓǙĸЎĉe\x9eȈːLΕƠӮƠΛʱ´ΰ\x8fҭԜ˺ǋϦ$Ʋˊ',
                },
                {
                    'event_id': 'ҖɉvƁΛļ5ięԒˈΨÙεũȗȋ±Ŋ.ǔЇǱLѴĵɷŇmӱ',
                    'target_id': 'ƙũӷǚȍňЪӠВɄ{\x84δŪ¾ɞʻǤƟ˰Ѩχ˓iȯǕğԫͳ˔',
                },
                {
                    'event_id': 'ÅȨʬȸŹѐʉƏǛƨŊ˚лɓ\x87ȐÞВ˙ɘǽϲvͱġĺŴÐɁ\x88',
                    'target_id': 'ȱ\x91ɯɐȗħǇ,ΒӌΟǆˎҭзӢÓ҂ӞęВό\x8bbưǍӦȉŗ\\',
                },
                {
                    'event_id': 'њʂ1tæυƁʳbùgƣѱ҈ґǢɕƊƄ3òǌ»ËǯϰӠԌӣь',
                    'target_id': 'İÿĊÑ«QʬΘ\u038b%¡Ĵ˚ЉˬŵʆȕǱȉΡiѲĢΈƀӮ¾ăǶ',
                },
                {
                    'event_id': 'ϪѓԛǴµΫǫŞӜαѷǿҏ҆ǸϪɆКʳΟǾΠӞʵԐ\x9dҿІНг',
                    'target_id': 'ŨɭԑӧûĈ\u0383σ±ǣ§ȱ˦ɗÏ·~ıŶÓ2ĭˍЅċŐƃҟБɾ',
                },
                {
                    'event_id': 'ΎҬǺɵԚ^)ʉϕʄōϴЈш¶ǡƪǔԐǺιуƿԉʷȿ\x95Ѡαȣ',
                    'target_id': 'Ӱ˪ƴllҝȣΝʽƦǫǱςԒ˹ѕкzһҸʒǺζʏ˾ƳĪҪ\x81Ϸ',
                },
                {
                    'event_id': 'ˑЕӻ΅ϳМΟǪѱЦCģư\x94Ɍσ\x81ϙ\x8fԥȻ϶Ʊ.ÅΝЭрԝH',
                    'target_id': 'ÿԢǳVȫѼð\x9dӵҴɋȏ"ӈ«УȔҭΣȥԍƋѲ·ɢҘưː?ԝ',
                },
                {
                    'event_id': 'ώŷϕʺC˰ϊҎӫγKȡҚƛμǳЕδϒëŰʅȶɻ҄ĀĪ [џ',
                    'target_id': 'hьȅЬɐЦӢŉɑΔ«Ѱ£Ѻԗΰĩ\x85ŁƪŖØѭĖąбũšʫı',
                },
                {
                    'event_id': 'ˈŅҲԔĿӔäĊԘґ[ϡʝѠʭC¥ΌϺųɵϠѭǸȪ˷\x8aЧ˜ȶ',
                    'target_id': '˘Ʌİҙ͵\x83\x97ĳΝgщĢ!Ѕʂʴƒвƽ\x82ΩŐҋ҇ğ\x86ƢʐƗο',
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
                    'event_id': 'ӠHȣщӰ',
                    'target_id': "ӋϣʫӔǺЩԞȂǅĩĭǪƬ˃ÝѣĲξ'ζҸƨýȪ҄ϣԪŔӄА",
                },
                {
                    'event_id': 'ƜƣǟŹaɂȐҏҞԭӻΞɶŞźѼŽǡҺʺԜʯɼŴcɜɷǗвƁ',
                    'target_id': 'EÇőԟǊѮʼԥЖЮ϶ѧŐ\x80ƫӳУϖϠ˘ƥʬșԭØÓÃE¡\x9e',
                },
                {
                    'event_id': 'ʶĬȯͳςӹú\x98ґʹ\x8eˍ\x9aŬʼоʷʦъɗʺӮȶʣϾÐҁıԮQ',
                    'target_id': 'ϳѤџӄϙĮРä˨(ҡΞĹ\x9aѠŘˈӿҜƣќɤŒО҄ЫǒƟϋž',
                },
                {
                    'event_id': 'Āː\x8a\x98ҢѪЭίҶħƳ«ѕϴ˄ÏǫȬčҖƼǫȬƷЬӟ˦ɸ˳ʥ',
                    'target_id': 'ўΊҒ˧ɰȆɂŬêȁɶȘ±ǓΖԛ¬оΩˇˏȏȅŐ˛ĬʼΛЬe',
                },
                {
                    'event_id': 'ͽӪZAЭΕǰ\x92F\x84ԎӬӄɩɲŶæһƟ\xadѕαh;ȌÈӃúάİ',
                    'target_id': '˃ϫŶä΅±ӺƶϜqϿÑɝϝ¡ԀǂԙÈȒ¼ΓǸӖҵԋʽË\x89Е',
                },
                {
                    'event_id': 'ǘœƷӴʴÄ˦ēӚƉł҇\x98ЂѭŻХͳʋ°ƅÂƅĵϊєȪɵм\u038d',
                    'target_id': 'ϙ\x84ŭѭӬǑԓ˓ЊџɄʬÁЫɝȋƊȳºϛĴϕ˻śȸВɪ@ʾƒ',
                },
                {
                    'event_id': 'jΓh\x9fyȇ˸Ҡġ҅\x86ŮХáƀϙԥЦ®ˍ_Ѳԭȗń²ȯ˘χ_',
                    'target_id': 'ŭǢɪ¼ƈ˹ʴӃόĂŔ˴Ϩ˾єÇȰ(®ʒʂʟЎϲŨIæҌ\u038bΝ',
                },
                {
                    'event_id': 'ɐɕѡʓƞТΕŏŬʷźŧ¤šʳȲβơԋƼҝǄƾƏ˕аӇРȊ¿',
                    'target_id': 'ӝѼҘǞǄƘĔɦӪƻȕűҷȬãĵҘʉ\u038bŭ\x80҉ȉġŪ/ȵҗȓą',
                },
                {
                    'event_id': 'ӗǧѿԁDЁμӧŅĤѝΘԆΕаԜ(ïϠńˑɠėǩ\x8aɒʡƖÀκ',
                    'target_id': '\x92Ù˥Ʋf˄ʪϞ\x9fȸƝɏȠWΘPĊA}ѦǜϴԞȀʙ>ŠĚɬʁ',
                },
                {
                    'event_id': '6ш\x8c˙зΩ˲ЂôơƐ§ɿ\x89ѽŽɋϠ\x8bȚаêNëâ=ˌʲʟ҇',
                    'target_id': 'ӭүOшʗϋƮýΔǏUλÉˠ¹řҹíĹȇŚΈͶɉθĦŐҬɮɄ',
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
