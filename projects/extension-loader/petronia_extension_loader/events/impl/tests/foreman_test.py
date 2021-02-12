# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-11T17:55:39.351958+00:00

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
                'Пҋˠ<ξ2Ҧ˄ψЖb¾иΥǐƲßӣċҼʾƻѸқɄÝҁԤҨѼ',
                'ӄgȬθO¨Đ\x8aђӗѨϼѤѿzʲλЧӻǘ#ƥԙ\xa0њɄ/ӯÜұ',
                'ʣʚάˤϨΕ˷ƠԢʓҸˎĈƻțÅϖŰTСҸ\x96ѴǌԊЙ\x8b҇Ѻ\x98',
                'ЋʏʽEſαѣǲdK҈hęŘwoκȑ9ŽЩʁȄϰΰˆ҃Ȝ¯ɽ',
                'ШѣŏϊоkͿŮǅņͳ¸ʭӑÅήǑϋØԇŊ>ƈϔǘѵ¯ˠyƦ',
                't\x7f˙rԇȽҊȵʞʃƨѳɚȶ=ϣ˴Д\x9fʚ˛ī§ӣţ;Ôӫ˫Ĉ',
                '\x96НȭǓǙѨǌѴǻ˗ϑԢĄЈ/ǈɘι¼ëșÂ&ƤиŔΧαFԆ',
                '˺ǪƒҲΟÈͶΪǼΰѤƓÒØɓѼƴҴӞɺƸĶůŀxǂΈƐÓ˛',
                'îôƀôƬƬɠŚʴ\\Ů´ǝ¸ǥŐЛŁ˥ң3Еš϶Ҥqŝ˻ӘǦ',
                'Āè˅ϿšɕəǨϼȒ®\x80˔ìӼшͿ˰nҝŘƽ˻ŖĉЇӎȓ\x98˭',
            ],
            'source_id_prefixes': [
                'ñǔѯөʅśȴүř¢ǅǑIκĔԪȒ-ԀюɌű$Ʉζ\x93ƸΞvӴ',
                'ԮτǺvƽ\x9c&ҟrǕԀƱИƩϪȎǌϔԫӫ\x88χЈтҌ\x9aͿǷŗӇ',
                'ӆʎОƏҷSƭʀ\x99ЅӇȮɞˉЋ=ȒǕěƟԝ ƇʞǞҟȞº˖Ŭ',
                'd˶ҹʈЇƑϛњԜĭŊξхѼйώӽĄ\x84ͳŝĉɆ\xadȹůҺĮԮ˜',
                'ЧӐлϼ(ƖȲ¾ԡƜѦȆ{êkǿΙԒЪН\x89ǖGȲŔƕЀ§ǷĂ',
                'СЯʪŧǱ\x80ԙċɔĨӄЌʯʾѮΪ˸5мāʗӥGʏ˭ȭ7ԡ¶҂',
                'ЩģÂ\x88ƪ\u0381N˘\\ȁȂϦЙĎ #ԎҨǠˎ˩˟%ȦɄɂƓ҈ϙǛ',
                'ˋĪÞƝͷÛɨǺɨͿҴѱκϠԕþŎǻɤʻÎμƫƣӈ#°±\u0382ԟ',
                'ȦӞ\x9bù8NȱнˮȵȠõҕτo}ҦҫǂǱӸEʵϔ\x97ԏх',
                'ŷш\x87ѵˤҪϥʞɜǅʇƼ˲ȭĤϼҁ²·˦˷ˊϛĚb҉ʱɵǺǑ',
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
            'action': ')ǵѷ¥Ĵ˰ĦҪ\x80ϊ"ʒϮɵҍƔžɚ˃ʹ',
            'resources': [
                '҄ΞɁÜ/ǋЈŐԉцŒȒԜʼȖˎʫȳԥǚĽȷĲӡxɐԨϿӂѩ',
                'ʆАIɗĹƛȈ2ØϢлϋɟҸӹώƃɂŮûΔɮÜҨǸǦȣȜǂɺ',
                '_ЂԪҔǵҶɥʖ˗ǄԄůǍġԧʽ§',
                '΄Ƣԧтğʀo\xa0¬ƽ\x9f˃åѫİȀĀҗғʇFӱďӺ\x81Ȳƅ:ƩÈ',
                'Ҹ\x81,ŻʻȦЀćŌЬʭǱΐȴȆ\u0378ȤȡɰԔŦ.fƧΦǄǞț¡ʔ',
                'ʷҞӗƩѳѸɓdʈ˽уШΑσϲǊдπţҪĭɢDҳìфЂŖҀɨ',
                'ѕɤɲȌMkϰʏǨǌʊǉdΛԕҟʯ¢Ǒ˟ƅˍɦǃ0пÍ8ʨµ',
                'РϭϡȱǆÖγƪгʯҭΎвɃĬǓɛǦўƅɬċχǙă»ɒĖßA',
                'ѤéÌђȨӗŦҳɏȻ˵\x9cάϮƷͰӘŔƳǔʫc˱ƮһƠĶɛΝ\xad',
                '˥Ґ\x83ϒłΖӳʭƇƙǧЎƅǂӫ_ĘĽс"ː\x93Ȏ˗ȋԁƞаͷӯ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': '}',

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
            'name': 'ɮ˧ΐėө4ɼҙҚɵōЉʖƵҔ˙ć˚Ŏǭ\x93˾ΊȸȴӴjǋΥԭ',
            'version': [
                -1755668419001937930,
                -738123839026628669,
                -53243126637536532,
            ],
            'location': [
                'Αƛƨˀчɉ@Ȑɒķ\x91\x84ηƹΦˋǶvÄòōӹӏζЋʎŚʵʱΤ',
                'ʘE©ƦψԦԩѼ˾ϠҎΡʄAĞяЁTªÉǬҗŴʹ|ʣǨҶ7ɹ',
                'ƿƞƭˀr_˻ɣɓӤЛǕ5ԝӸӯʎȀʕǺˬҨʤŽçАȻЬ¿Ϛ',
                'ƚϙɲшʲɨσΦ£ʝƺǿðýӏĿ¨ϭӁЍªoԐŌ|ҩȷßƛЌ',
                'Ћτû\x94ϧ¡ρōѺÝВɠƭȖȏ)˯ʆЧЋѰȁзʘҋǗȄͼşŎ',
                'Ƶ¾ωNРʇ³ˈϐHӮnѳʺŪϣΪĹŰƬύɰϔӋή·ǩМэċ',
                'ӴИчƸѪĲѴɄҧKϊǈBϑǗϙĵӪЕ¶ǑȬϝAИɍȞН_ȷ',
                'íŹӟΜǅɠqЖӕıāÿŰƗͺ˯ĿřԡқԚϡМ˙ĈУёѦfɋ',
                'ǍǣԎƗÃɔíȦʍGɐ˷;ÇǫȈűiӚϏӐБFҸ˺!ɲƚԏӈ',
                '¦ӘĴэӸϜ\xa0зǠнȒŐӔʇpȋΦǂÆÍҔЏʹfάƥĴҟʼʁ',
            ],
            'runtime': 'ȣςɴùƔïӔѽȿÏʩ~ʶǪ=ɩӗºͻёԌ˨0Ɛ@ВɓÈђʟ',
            'send_access': {
                'event_ids': [
                    'ϷÉӇʫѨԖeҲгøƷǥӭƠěїƗʿʊCȧȤʸЬĆЯӛҎ§Ɵ',
                    'ȹ\x9fƓȳɰʓɋ=ĕϚÞ¾ȉΟφŠŎńŠƍҶ˚¢ɦ\x83ǀȳOѠŒ',
                    'ϖͰųˤғӎҥԘɷϴBʱˆύˑЧӕ\x94+ƎĶ»ʉқʰӵĨφˊʶ',
                    'ΕѼǧɍKӘǃɅӔǆȗϵϴǑʼɺԉϵɍɏӨƤŏӼʰ˅ѷƃʣÍ',
                    'Ĺ˨ƨȨ˻ȓĳƗϑңƄцȾХΪ˧ǹɸӂȍѸ¥ͿǘҠңĘȫщ˖',
                    'ˀĸ΅ĹǧђőƸӼ7ɝʔŕŤıŊ¹ǖʶėmΞтǙӼ\x99˔ЬċӢ',
                    '\x8cʫȭǇԡƂӖv¹ʯıӖĚwЉqʱԨĊϝ~ČŌͼ˛ʟѺҚŧˏ',
                    "@˂?ɹłFĴ'ǈїĨƕaµ\x8cɾĭ5 ±˴ѳӀǋƞĒτĳмΌ",
                    '˟Ήúϧ\x92˕"І҅ЏѶʭ¥ЮƑǯɯЫb˩ͺΞԂ;ŎŤɇΪԘ\u0382',
                    'ɐѝӝ˯Ÿ˛`Ĵ҄ʹҌӽùˡҧϜ˘ŋ+ӯåϑк\u038bӇ\x9dŖʲʥǝ',
                ],
                'source_id_prefixes': [
                    'εҳϡĽӴЁΣjcÆҶʵɑ§ʜÝ¿ư¹ҮҍѻʶɄԄȟ^ΒΉƦ',
                    'ͺиԭƪřɭŕӸǼҵЁÂɼ\u0381χāҬ˗ʙôÙΊҒȇĤÝİҭšĮ',
                    'ҩїƠȚǇǚѻ˖\x86ΙЊǞԇӽƦΔŬŇԒƈƈԓŝɁүț҅¸єɝ',
                    'Ȫz@іԇǍ,ӧĩӓ˻ΆΤʵeЯŴԂˤɒȴƛ+ɠΣ˭&Ѡ©ʜ',
                    'ǪԫӼĝ§ę\x85эͿȲĒoҧϷшƪǂъβʹȑӌơӲ¡ˊĬҭԑg',
                    'Ðȁ˞ŵǍʀǒz¼ĸRĦўίψɬωȚҮҹԔˁʙЫĩ|˴ʓѨԞ',
                    'ѧ·҄ʛĠkҫѥʨ7ˤɾʅ¶ÞӮbԏˤPǙ˙ўΪİԤϝτȰX',
                    'ɗȲӞÓʎӟШȫ\x98ҀɍȳȢƚìUҬҺɱєʎϐҕ\x97Ȳ\x7fȫíӋԅ',
                    'ůήÕ҇ǏΥюȍ˚ǎÏǇǚ(ԒļԭӣĐӓоЖ\x7fʴǠԘҖ҃ӄĀ',
                    'аұĦǂѴʿϏɉƘˢӓԑϧºӨάˆԁçʴПńӑãˤǄǲ҈ѭϙ',
                ],
            },
            'configuration': '˒ǳ<űѿʚӫϓŋӲʍǩҽϙɔ҇Ð#űӫª¡ΨĪǰЮв\x93Ҭt',
            'permissions': [
                {
                    'action': 'ϓǧĭõ˰',
                    'resources': [
                            'ΐŋTɕ"ɲͼĸ˛ȚʥôǔĨˇ¶ҦǺϪȭ,<˯ïλȠKǾъł',
                            'ƄкȃȖԭЭ"ϢѐÃʛɍ\x9aԢѸ˕ǐΩҬϑèʌ\x9aѱÙϖҼ<Ύӽ',
                            'ǫѻå˨ĊϷԃЦƍӄΥ˒ɝƩƧԚˢȯĚ˻=ȤҤЯʀѤʀ®üԐ',
                            'əʋέ´ȌʧԛɓvħӻˊŶϬƳθҳϳǽhүčĀљƱƼͶTΡʋ',
                            'Ψ˞ĲԀĝƮǝΥόžϼïӕΥɵɏЌЙŭʲȂÛԈҩʶʭŏɆñƑ',
                            'юѭԚ«˥ƕřÔӖˣѭԙˤ;\x80ǺɕгǾȔĨњΌíĮNВH<Ŧ',
                            'βɐƍ\xa0ǆė}æǺ®ǊϹcÕѯҝŏдȷɷȴVҀǬԓǮĀƻˌˣ',
                            'ʪѮ҉Șî˅\u0383ƌĮȯρȘҍʶǥļͷЗɂԗҀʋ¤ĈΊďԒуҨԈ',
                            'ķ1Ϋǐ\xadǕƓɩҎӅűҬ©ǒŽʹ«¼\u0383МÉ\u0378ԙĐäßϠŇτѢ',
                            'ȸƮłс´¼ԝȮРˎӴʹƿĄԄȡÚҞΜƣΫʑϡÓӆʰɃќЅĎ',
                        ],
                },
                {
                    'action': 'rľňȊĆ¼ҥĶȥҖȻïԂɼɷʵpɴųÐϕĩ\x7f\x9bώ¼ԭϒʶҟ',
                    'resources': [
                            "ɮҘ'ӲОӤҭȞΊĤωǦøH\x94Ƣϩţ\x82бŜҗʼʊ®˃šƈī¼",
                            'ɵƠϰΌ\xa0˦ŝɮƌÐѝń\x96ɣĶА˅ү˜ЍɠǾ\u0378ɘоĢ\u03a2ũȴл',
                            'ƫțȉԗƑʉƿϧûÃ¼ЦѢΡŊĜ{ͻȺĸϩƐ˭ÑYјѹήѺʧ',
                            'șÒҴĐ\x8fϚ˟Ϝˬŗˤĭĳ)ЍӸФ¢ÑB˓ƆԤĘ\u0382:ɕʢªп',
                            'ύʌҊπЈɉ˯ēþİȣŷшіЎҌΡУ\x91ԗʇtӄ3Г˲ȧ\x99ȠĪ',
                            'ϦâˏāϛϮøƁŗӰrɘÝˇĖԦĕĎƶɆӜÜǠ+ұjӖϯȩϘ',
                            '˝Ĺ\x90ϢƦȟˌ˒ϸť˟ăȆāXƩƩǛ¯λЅѓǊ˜ͷҐȵÔƜ\u0382',
                            'Ѕ˰ʾʺòҬșŴҡňō˘)ҘĝÇŹϮˠǫΦϴ΄ӖӘqɗȀɏɑ',
                            'Ӥͷɦ\x8fĿfԋÃɯý˦҄ͽԓɇŲMġ¯ǚПӡѼƕƼ˩Ԟ¤\u0379i',
                            'ѡțȱЀȹΈχϼϑ\\ӷʳҲ½ɩЍӉΓԊӉÁԉнԄɷȄ˞ÑҎŔ',
                        ],
                },
                {
                    'action': '$Ĉȁƻϓѿ˝Ӹ\x9eԗȓĥŻŖȆҖȽϑμΑɥʲ˷ɪǚі\x92Ϟk҂',
                    'resources': [
                            'ȯйӈɦʿȲ¬Чˏǯ˰ǡțœȳ˨ƁǷΈēҧǱФΒ¤ҝōÉҎ8',
                            'ŐŏĜʗțɀåȄSūԞǮȝ˻҂ԍɺϥŲʨфƞҒŞkɵıʠİү',
                            'ŲБ\x82ϽÝϻßåǔěΝ˙\x82˽ɶɷйПΐ˜\x9fҵӰÝrȹµҽ\x92Ĝ',
                            'Ɣ˸ĺǿǵçӨƈˇƴʌƥЄͿɣĩɌʽ>иԙĘԏ:\x96dŢ Вʥ',
                            'ӻĔɵ%Ì"˝ϜъǅǗϸũеԄǙΗїŁԄōїǮԡўïŊқşƛ',
                            'пИЎȺӳəЁƆ˥ϰƿя\x84ǕǚÞ\x85ĤɉӻĲˎœӒҝѮĢӮ͵\x8c',
                            'ѶˣȦ˼э;ãѫƈȃȭ¦ѪϬ,ŸӛЂȚƩԩūʨӜŝsѕƾΨҼ',
                            '\u03a2ȗǂÓ҂ԟëϊũэ«ǧƠô\x99-\x8cõj˶\u038bĄаʿʱǧԄц!Ɖ',
                            'ϨÇȦĸÊԊŭǙԤǆԛʦʞϕƳӽрƅΰӯɼМяѫОЮ˃Ζ\u0383Ò',
                            'Ԗ˭\x88ˈŮ˳ʪѪҌ²Ǯïԏ˄ɫŹ8ȭ°ȀÊŀ¿ђҟO\x94Εɭ%',
                        ],
                },
                {
                    'action': 'ҋ`ԫʜΪΰŮ\x98Кй˗Ǉʀ\x9aʈԒQ˨ğŕʊҠǇǒƁƂÒƎВi',
                    'resources': [
                            'ţԒΧŹɓɎϽ˟ϫĆĊϛǪͲОɛĘÅιӬʅԣϾѲˁÜԒкμӎ',
                            '\x9a³Ӿ˰ȭԢΖϪ˖\x97ЄǷɢʊԎĵê_ҼɃʐыĸ®ҸҀҙ\x8a҇Ð',
                            'ӁÜ|ҭϟ˜¦҂ʮÈΆǱzґ\x96҄±\u0382ҳ\x9dҏţQǶΣnӀ\x94ĭѭ',
                            "ʧһӗŜ'ȈÙηɶʻԌċƧǟѳԦW˸ͼ)Θч˅Ԇƅʲҥзɧɐ",
                            'ҩдνĊˋϷÕVRИȯʥȰФʍɆĂǜԦôѥ¬°зǢ˯{ßa\x99',
                            '©ѥӸɐΝȢʇɘʔʑȩҖηɵƾкұʙƇȋǖэȢьȹԘ϶¨Ǣԍ',
                            'ψ¿хΈύϭϓĠ(ΚʟŋǬ-ήlŔðґğ\u0379ȒjľǎѮϜǪϧĢ',
                            'сɮɩ˕˷ƸѠњӵөϼϜ˞ęЦґȨԕƆǰÞɤέӇɂĊ΄\u0379^Ӹ',
                            'χʁǽѓƃŧũԭɭʔÒҩ˨ǽɮˀǭ©ςȊͶȩŮέ-ıʌЮǡŉ',
                            'ԃѢ@˝ȠʿӞЍӦʞˉСȥǨϓEŞ7ӎǵәҐԅϫ˓ÔǊAоф',
                        ],
                },
                {
                    'action': '¯υǰę÷^\u03a2ҬǫśЗΑØʖҺЖτșСқԗѵ˛Ӯ\x81ǘȫȴ¾Ɨ',
                    'resources': [
                            '˭ĻДͽˈϥ˯ʸЁʷԖCЌ˹ѸϪɢǖɕ®ıʙǟԔ/ɹĨ\x8cț\x9b',
                            'ˑaΔċĥɟԥχɤžӟЕɁҔѲÉѬť\x8cϬ΄˦\x7fZϬ¸Ѱŀǰ˝',
                            'Z©ͶŻϐ\x96ŮӪҹïǟСȁτɋ¿ɰ»ȽȋΡ\x8aȕϻ¼ΘίҩŠW',
                            '¬Ʌӗђγі˨˙ϦзŷĽІjΨʆäĩӭ\x7fɊĘ˝żѷђ˓ƴëˉ',
                            'Î˪ЍӃáȲB\x8dϕuҀ˾6ĔĿBéʊ4ȡŔɿǖȝǷŏÛұɨң',
                            'ÇҶ\x92ũȇŕȆϿ\u0378ӕӎͻ˄џÇ˞ӋΒпʨċҜϞ˶ȠлpҲ·Ӱ',
                            '˶mϗM˒Ԅьƒ*ǝżмĐǡҋɪèʅʢÈΪǃ<t¾ʰūԮΛҹ',
                            '»НӵĳɗřΡĥ¬ȇÉĽηĕǂN\x9cŞѱƜ°EʟǝІμԥτMt',
                            'ӯ˵Ҏɉ¤Ҵčɘ˪ĂÊӜʆİΕĦЃǎϼϖζąĬС҉ǰƧЗÊē',
                            'ГèƯʪϖŨȽƊŰϗҸҚҽͼíίͼëѱұ΅хѾρƹӂҰŠ`κ',
                        ],
                },
                {
                    'action': 'ЙȼȍҹΛʍȸ\x84\x80ѓȢѻǭϧ2ҪӳƒΨϊƛɁӿпϳpŗWŊѹ',
                    'resources': [
                            'Ŧ¬ƪuřƉķȓɛøʝåшҴ\x7fӛǮaҼ1\x8eͽ§μPіJ˴ЬǮ',
                            '-ДӣσȉɤӧҒCˋʟŏlЄ\x96Ρ\x9dŧѣƟϼÃȉûȬ˝ҞɉӁț',
                            'ѻюĤƩɪͼŀF\x88ӘÃǁѓˋľ˳¨ʀӭɯĂүƻMϸɭłΙŮ\x8d',
                            'ʙIϯПŠǖ±ř¢lÂ˺ϐʶ˩Ͼϻοҧ|ŀѭτ=ΉӱžЫЄѾ',
                            'żɶů͵\u0380ҏ˞\x93ȘWхΐƾƹȨ˷ʜЏӎˣ\u0382ӊԫǅɮž˽ЖǾʸ',
                            'ʗϺűÝ¯ȻǍψӤ\x8dΩǍѦťʸȹ>ǚȹķҀƦ͵ʗыόnϱȕÿ',
                            'ҹӦǲԭϛƒ5τŎŃӹҜċҮ\u03a2ԍѷϗӦΊϚǸҩ˶?ΑaÅη$',
                            'Ӿȭʗğԃ;ˡˋˣɗĴӢкȲÛʰuˋѥ»³җĳ˳˸\x8bǓӋϲħ',
                            'ǿɓνӁӜāʄhԚШΧΣ˓ћω˶ʢőŃʽӓŵʱ˅\x7fƿЫ˄Ǣ\u0382',
                            'Ξȅϭǀ˸[ӿʒҐҠȫͻï\x95ƉƉʥӈȏԈßaȞԙǩ[ʹĘȋ˺',
                        ],
                },
                {
                    'action': "ơƓͿӦ'ΈȄԍŜͲȃБǝπϻτʱӼĲźϲųȖζǀӠϕűĥǑ",
                    'resources': [
                            'ˤѱОÉȎõA¹ӨѨӂŗĜ˘@ϽΉ4¾ȫѩҊԂÉJˌĎ7ԃѝ',
                            'ȈβĿ¬ȁË¥ĆɣДƸӀҫʁҧ³Ϡ˛εМһɜłċϔĴƏɔÌ\u038b',
                            'ЪӑǐͷŭӃ˝ӫΪŢǧ˄ӋʘĮȘǳʈɭҨˑц+ΑғΓŦɑϜ\x85',
                            'οмŽͲûԣŞåӕȈԕ\x91ˋƀҩϲŭвԏ˱>)íƮ\x9aǏAϏ˱Ė',
                            '{Čŷɚ½ϜGôÞӀȗϤѬÖҫŷĔM¼ͺύѬϢ(ŔāԈȍнˉ',
                            'ϫƄƈʧ(cӖҰԎǒfƣΆQǛȣɻЗĳcǧŇiӿƠˡɴūӕϼ',
                            'ſwƳʆ\xadřс\x84ҜɁˍŠͶˑMš«ɎЩн˜È˨ѺȧШΌ¿®\u0379',
                            'ƏɐƋŮĦБǠιʐFœͷЩĕƪ\x8aȫП¥ӅWϔ϶΄ʔųÜÈƫƆ',
                            'ˠɽâΊhĽАӝҔˊλľυòԈϨʨųňԕƮʦȳɇ\x96ƵϏì^Ў',
                            'Ȯѩľįvϋ¬ϼ\xad\x9dO˜јѽѠΎςďŒκʹϗɶɸϚŨƫǆ«ψ',
                        ],
                },
                {
                    'action': 'ʍ',
                    'resources': [
                            'ҙҞùӗɽˮƅŸӷӒԥ-ӗ\u038dьӒӪęƓĎòɈÑцÎ\x83ѓN¿Ӳ',
                            "\x8dѪ<ąԓԩ˗TԁԢƜВԢĝŽǲЕ˷ƋɒшΩǽɤ˥'\u0382}ƚƽ",
                            'ɚѼǫӺϔǖˠθӍΥԠ҂ǥ\u038būō¤ǎˮ4ҮǞӛˡғ\u0378пNπ˭',
                            'ϞԣY¶ЛěǏ˔JØѝͰȏ:ɂƞԒɐӣӕӬҊȃēƲҖѾáċҨ',
                            'ƱəĮ\x7fїґ4γɤŉȍ\x8bȢҿƿҘőGƾʝѲ˔ҠʍώʰŊ0ϖл',
                            '˗И҃ǮqҚɐ}ˌ©ʔǸʣяƾȜұρБ˖·ϱ84ΔÞȄǌǀδ',
                            "НԌύȘя÷ǠâʆĕüÑǺ'˺ʧҪΞƻ^ԪɍѤʓʕȔˊ˕ѸĦ",
                            'Ы҉Ā˜ŕÚЄÃΣŬхǝϲǯӀ˽ɱ³ϞЫϭаͽйǖѭΨ ɄȆ',
                            'ĬΗр[¬Ƞxâűţ\x92ЁsX\x8a˘oŤԫ4˶ͰґƟЭӯУʫӃȰ',
                            'ȱӻ¬өǀ£ś\x84˓ʹƋǞѬƓm˹ԣǗrƐOªΞȾWɰʢǇȵ˽',
                        ],
                },
                {
                    'action': 'žǱËïȕǥ§',
                    'resources': [
                            'ʻкџkŶђС-Ĝћ\u03a2ʶ-ɟ\u03834ЮÈЁϚ˗ÞşҗіϾԝɚˬ_',
                            'ǏˡȳˬäʔАԅǿżȗΐЮяņƫŻ\x9eǺΦɷ\u03a2ʤїĺ˭ƠƷ˔ц',
                            'ӾїѠлôºǱэɠŇ¦F°ªʫФɣӫSĻɬўсΆҥЀʟƵИƁ',
                            'ơªʝ\x96\u0378ĵžȈ¡ȶàјǎӑVҾѯcáɒ{ҐЗЮŦÀͰý\x91Ǚ',
                            'Ϊ©ʃʖđ҉ϝўŻɾȴҽƋŏŞʰҟȯѢȫƺӕIѿ(čғѓĔϐ',
                            'Ķ¼ϐrӨɀɇӚіЍӞjРϒKǡ^ЂÞňʣѯиΚɍЅƘʤƷО',
                            '©љ`Aѩ\xadę\x8aҖаɀОŜ\x89ÀȡÁͻƋ\x94Ԇ˫ʽ/ɧ_6˫Ƒƥ',
                            'ŕ¤ɢ¿ƯƢÛΞǶǛʞšɣɩƼŵ',
                            'СĴÁϻˣʹʋЛʱʀʡλ®οϽ6ʟȚʻέʰ҈Ҏ¤ӕҚƄӝȶΜ',
                            'GĻΆīÇ˖˽ԅε҆ԚMΐĎĄԇɦҫϾ¯Œ\x92ɶˆ\x8bиЯΐҨѠ',
                        ],
                },
                {
                    'action': 'ð˖˂˷ЌŜԇôēκκóϛpҳԑȿ·уŽ2G˨ơĒƷӤΧǽ\x96',
                    'resources': [
                            'ȐBʿπÒµǓßʍƴˍʖε\x84ƯːьϧˊӛѾӷǺ˫çŐɰͰсȫ',
                            'ȊýhʜѦ»óǱнӨËŹǲƉ¦YÖʴǥĳώÍăӸƖǧѹąǀ´',
                            'hñɚυǳüƎϐǾƝθɆιҬΤԅԞ\x8eЈË\x96ǛŌɧÈϋɽԩАǓ',
                            ';Ļsʂ˦рĐĈɮ\x80´ĳϪǨ˞EΏђĔ\u0383\x84µΜϐȜΒ©ŦʳɆ',
                            'ñƞpϢсеŜǱѥˬΛŋжʕѡúԢԛҁƠШ˱ЖɮżŹȸʂ˂ʎ',
                            'ӎϲҢ·ө(ǟΦђ˸ӐЪ-\x9bҭ~ӠľϵǑԭĹԞЃɤɃɧǥɟˆ',
                            'ϧǯ\x96ҥ˥ΜӊˁѠïԆʦѥͰҽͼҋǃÍÄϐ˲˸ҖñƊî϶ɔо',
                            'ƬЊJʳѩȩӶʂîȒӢЬԖӚЧˎωӻǔӭɯŵԕԏΓZεǎyө',
                            'ϱԐʧ?έɑķѐϹѶў\x8bɑӝɩˢǀƗ®ѷǔΤǩ\u0382Ҿи¿[ơĔ',
                            'ΗКҭ%ǰ˪ċƨȫʪϋħÓΤƕǱ_ɪϐǿqʦңѠƥ¤êÈȆP',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'σҼ9',

            'version': [
                -129295400057620335,
                -6149741042719534024,
                -2702773625060985749,
            ],

            'location': [
                'ȟ',
            ],

            'runtime': '~',

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
            'name': 'ȳʓĉ¢ŒҐЭŸѲʸ\x89ЉĒ˪ЕԌҿ®ˈĩ˸¾ΖӦ¡\x89ˈȸɴˍ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ţÑË',

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
            '$': '\x9dCЬˊƱʅˈīĎ\x9cͲˈȒ\x9bſȢɄĬĝ҉ӊѣõÚ\xa0ӰÑϟӌɮ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 6829225055373448878,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 789313.2606325255,
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
            '$': '20210211:175539.279435:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                '˭Ȟ×ǕρӏƼԘьӺˋӊ<ˎØɈþӈΗñŧ҅Ѯ7Ͳ˘ȱҜŞҮ',
                'Ƣρɰԫăɥѷ7GлЦӗ\xadŨбǌɄ˝ɿƱάψ\x85ѲǏНƃϻǠ˹',
                'ϩƧԘʣΙғdǯтөɪʑʉǥƌʜ&ƣöÖҵӵƗҦΤȶиdwʋ',
                'ҫθӾӧťʇ-ɯ[ʑņ#ϛŹɚӒ®ȰʫM˵ˍŧXҔάԣϵїĈ',
                'ЏΥ˧ɩÍǫǗ˘/ƴƴȅҲйȡÅʉƾѦbŭƤÒѽ\u0378ӈіʱŝѮ',
                'ІƁéԥɽкƧ\\ҐӐΡƛʆǓрҶ\u0378ТȬ\x94ȣƜҔĪșҷǓȷɫʒ',
                '˹ʰǌΦϰɘźɵɓġȇЛ˚\x8a0ӝεʸԋàǮƖǻʣˎȼƝϿƄɼ',
                'ģҀƑƄNėÎЯƖϣ˔ӂѷQ·æȦj©ԜӤѥŌҞCɠϔ҃ΏǗ',
                '¬ԄԅǯѱϷЃöϑϙŜӣʘȳӛσΛԨ(Ѫʫ\x80rϽǃϙˡϨʗƆ',
                'ȑʣLωҩɟƟηŬɁūѵΰΈƻĨʏңƇ|ǡьϸϯ.¼EpӤk',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -5098022723517533891,
                -3321352950985650554,
                4998825545827772962,
                393274573538573448,
                -6815346831568821862,
                -2825004578693019076,
                -5473528803646672270,
                -7689478555007816148,
                677928643787864061,
                8129692221122450075,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                27510.471940697462,
                346185.00569157116,
                590593.317527811,
                984556.3201419034,
                809748.1263720647,
                568580.2087857563,
                198937.7415140525,
                -21080.72781050911,
                911229.2226835118,
                -70113.6143623071,
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
                True,
                False,
                False,
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
                '20210211:175539.280245:+0000',
                '20210211:175539.280258:+0000',
                '20210211:175539.280265:+0000',
                '20210211:175539.280270:+0000',
                '20210211:175539.280276:+0000',
                '20210211:175539.280281:+0000',
                '20210211:175539.280287:+0000',
                '20210211:175539.280292:+0000',
                '20210211:175539.280298:+0000',
                '20210211:175539.280303:+0000',
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
            'name': 'fȟЀ\x8eȕmВЊ:ˁʤz5ʗԄˉÍҥàƋԒĘԚҋƪǁ¸λϯԃ',
            'value': {
                '^': 'int_list',
                '$': [
                    -6501758669608584374,
                    -2347750211645473509,
                    -3588094578579579323,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'l',

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
            'catalog': 'Ϟƣ«ΞǦȅΎ¾åƈάǵ˫ȐȌ\\ǨǗŖо$\x9dƃ˲ƂřΥӹƦƼ',
            'message': 'ӘjԙâηYŽϣǨѷŌÛ҇ѓŲĦмԀЎǷƀҊƻɁϾґӺΈū˚',
            'arguments': [
                {
                    'name': 'ІГȝŋˏȾĉʜөɩǞİ¹ҎҤȫǺŦЅǒ4¯è\x92˘ȞĹҴNͺ',
                    'value': {
                            '^': 'float',
                            '$': 568421.006217987,
                        },
                },
                {
                    'name': '·ŵż˗˛ɝϗ\x96\xa0ƲɔéȊƭѰϿͼ\x9dĪȖŖΫ˽hͻͼδҚӎѼ',
                    'value': {
                            '^': 'float',
                            '$': -80466.56253406321,
                        },
                },
                {
                    'name': 'Ʃ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210211:175539.277366:+0000',
                        },
                },
                {
                    'name': 'ӆѸ˚ѭɨmŏӈcǌų¬ӅÆƵҚˎǰrß\x92ӧʦМϧΤӡ+UÏ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        264324.18284786126,
                                        629075.1793267723,
                                        299233.4350953591,
                                        73435.0300687165,
                                        480291.28922794457,
                                        17112.955138398014,
                                        780642.795355241,
                                        -45909.95772548083,
                                        949004.9255221144,
                                        429550.407851567,
                                    ],
                        },
                },
                {
                    'name': 'ɼҼ˦Ƕɂŀ\\ʜșʊ½ԋà_ţ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        False,
                                        True,
                                        True,
                                        True,
                                        False,
                                        False,
                                        True,
                                        True,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'ħþŐ˹ZжōǤǾ˾ƷŧɖΕʏǢЌҷȶҭ\x83ӴñɍȰKĝEĔa',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                    ],
                        },
                },
                {
                    'name': 'Ԩ˖ʢŕɆƬıȫOŋЉǗʍԥǡfҮӫϭƹōԌ˫FʣLɌƫǺŮ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -2176170677315850343,
                                        -6976140028349243295,
                                        -1862745314824993257,
                                        -3719538788398870243,
                                        -1645699190363346079,
                                        3047311656417547371,
                                        7496387066056409911,
                                        -5532383672626003959,
                                        -6654723181604365923,
                                        -7615716444464067689,
                                    ],
                        },
                },
                {
                    'name': '˚˩φˮÒÊʺĺŭœҸů.şɱ҅ʹ\x8a`dšīţϣēԇΑ\x9fʆȐ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210211:175539.278484:+0000',
                                        '20210211:175539.278498:+0000',
                                        '20210211:175539.278505:+0000',
                                        '20210211:175539.278511:+0000',
                                        '20210211:175539.278517:+0000',
                                        '20210211:175539.278523:+0000',
                                        '20210211:175539.278528:+0000',
                                        '20210211:175539.278533:+0000',
                                        '20210211:175539.278539:+0000',
                                        '20210211:175539.278544:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ŷԇ¡ɱʗ\x89ȿȝ\x86ОHVѥ\xadѲǊƭҗȑ:êOSĀɛӇϭɫRƣ',
                    'value': {
                            '^': 'float',
                            '$': 867178.6566770413,
                        },
                },
                {
                    'name': 'Ъɰų·',
                    'value': {
                            '^': 'int',
                            '$': 6283806943028950009,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'șĝ',

            'message': 'Ӣ',

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
            'identifier': 'kѤ˯ӌ͵ЫNȲ˛ĖɰȁåԃϵèɫѡҜd¡ˤѴʛüňŘ΅Æг',
            'categories': [
                'file',
                'access-restriction',
                'configuration',
                'access-restriction',
                'file',
                'file',
                'file',
                'os',
                'invalid-user-action',
                'internal',
            ],
            'source': 'ԥɲêƜӬ¦Γ҂ӕÔƅkĈѺѻȚωЈ,р\x916ΑӇʬūҴYRɷ',
            'messages': [
                {
                    'catalog': 'Ͱыkʩ%Ɉ¯ˡȷ˶ҟ\u0383ɦăЩŀȢŋѥŴҴ0ϤӌʘѢȧΝ¯¿',
                    'message': 'ЙŮЁαɲΧˎěÍǹʋЇӞɿţјOŕɳȝȍωʊԫ˝ĥˇEʵɝ',
                    'arguments': [
                            {
                                        'name': 'ʜӝ^ȚŰɢӂ5˃Н\x9dǖ]Ƭ\\ũʕэɹƼˢʡĎ§ƑɇˁϺǙ;',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4413373879403359578,
                                                                            -1270664571487834694,
                                                                            -93470951772956821,
                                                                            8870347519121106955,
                                                                            -627853511528600731,
                                                                            1497256571721221466,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӛʱΚȨ¨ǒ\x9bҷ¬Źϰĕ¾ĳȉΧ˭hʏӠǏŤɅȴw»ĦIͱĤ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Μϝ>ȉ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ӷ;\u0379ȔʶϲԒºӍ%үŞęʖŪ\x8dũ"ĩƇБϥƸȎʐǠȕÄƴѰ',
                                                                            'ѹÓѦ\x88κρҭϤ\x99ѯмҨҡӚϥѴĶȡȎэÜˆӪʿ˄ɴʟǸз¨',
                                                                            'ȲƪÛӈʄ:ЎĹğKťҭϣЦƕƨĶѬʗϞѥӝɑԙӣ\x97џŌĨʪ',
                                                                            'ɋǷßʵȨČςǪƕƧÐȜΝÙğ\x8cϯeμûїΰжпҋľӢWɁ\x95',
                                                                            'νèǨʠ\u038bѺϕɜԝΫ\x87åķȸƝͰťÛ\u0382ƿͰȲıϣӪͿˌgкĹ',
                                                                            'ÕƮˠƱКԡŵʣUE:щɖӪӷȘ˽ƃҽ\x96/ӳʹcμӀß\x9a˯\u0379',
                                                                            '\x90ËцъÓѤʹĐ[©ӲҨӠ\x9aȄѾƮϦÂϬėɎ˦ƔҬŲʝψˆϴ',
                                                                            'ЀΪʹŋѫſ˺ʾȀˍѬǴȦӒ˪ʞφԊԆ˚҆ӑҡǓâǀ\x9d&ƾý',
                                                                            'ǡЫ1ҪƬсłμӽΦȭȤӯλԏ±ԋНʱӋ÷ҚUѭѭ҃ΦTӓԂ',
                                                                            'ѺªҤьʢͻғϣŴˌyВɼ\x95Пʤ҂ιʖӣ×ԪѤʫ\x88[\x8bʊǲư',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǩ$ɣϓĀ[čӱǻ®ԋҮɭѭʩȒӋʹι%Ь',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĮɠȠɆδӌťÂ®ԏȦϽсИ\x9bƓyʐϦӕ7ѤҷӍƾĹςћνɪ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            760541.9689180275,
                                                                            231670.27817422315,
                                                                            449175.32601623854,
                                                                            65114.819047629106,
                                                                            -5409.669801955912,
                                                                            477585.1799441294,
                                                                            652443.9569186212,
                                                                            953055.7697600638,
                                                                            642451.4250421848,
                                                                            395320.8413767017,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ì¿ƾ˴˲ŸƆϝɥÇ\x86Ǜӫȷ\x8aʆς\u0380ȵʞѶРҢʂ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\u038dgŰłɇьˍˈӑČ\xadҔǗɽÚ_ƶĻʩȻUNԌȮƓϺԆơυȝ',
                                                                            'ХυсǬƭӍƑɏ\x84ɍ\x92ɑΥÜȿǳ¦ϔπČȎҝҹҲǓƐʔŜëƛ',
                                                                            'dзОĵΛǬҾʩ˷ÇԎе¸ˮȫЧ¥ҫ\\śȟ|ȏУӅÛ϶ξϓӂ',
                                                                            'ơЗˈ~}Ěϵē\x89ȐʒɒѠɴԑUϢȕǪӯϲӝœπk\x88ϴÏӱψ',
                                                                            'Ӵӽύɵ§ƩíŖ˚ȫҬӆ\x81ȹϠ¢Ė;ϞʶƪӼÃĂ˔ʃƔˊɍҥ',
                                                                            'УԠˆ˽˙Ұт}púҸ¼єǳĂǦñϜɁƙWµ˩ӝОƥµҊ\u0383E',
                                                                            '\x9fɐѱǓˁčгѲѬŏĬЬǕκԄȽě=ƏϬĢȌӊўʢŴϾɡɜҕ',
                                                                            'ӴǤ¸ԔοԈʙ϶Ƚ˥ӑҳʃԍʲѨϣɸʁԄʢŪťԎΞӠˈʞʇ\\',
                                                                            '×Ϫԓ҅ɩÄıűХϺҋǌ˦яˤȏǧǥɓ\x8dԠЌġ\x7fμѭëӇĻг',
                                                                            'ʮŚ\x97ѡьяĦԂΆŮŎѱßΥĵРİéªѥĸ\x8cԦϲԣΟЊ˫¾\x98',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȒԏϙώɄǼĒӎǳӀgʟŁðĲʐƔҔƎʯͻ˺ńąĲЉ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            73.52434744629136,
                                                                            988488.4542400267,
                                                                            969848.3250115144,
                                                                            294165.0417441769,
                                                                            591324.6859859718,
                                                                            474417.87146945554,
                                                                            487005.01209358405,
                                                                            802674.1139534782,
                                                                            581448.8820415786,
                                                                            316206.1434637133,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¶ȏŕұ4ł˗Ѧ\x91ԙ\x9dӆӜҀ\x94Ǘ˸ӷm˨ŗ1ϛÈӦӀɎ&Ȓİ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˥Ɓґɜ҈ǲϐƪdĲú\x9dΡ˄ΊЧͻɓӏ΅ԀˈҌƸ˝ɧƹӴBӭ',
                                                                            'ϠӸ¨ƕΰŵΥΞCÆųϖéԥ\x87\x86ӲĻŤӪȢΪ\x8bҾĦʣǌԗǰu',
                                                                            ';\u0383Úӯî¯ǌɪӉTъ ҧǺҬӥϚŃӖҤԮϮŐI`рŧӈȡï',
                                                                            'š\x9bɸυōɟȀ_ϼZƈЊҮȵĢÓ³\x83ζӺҕ˪пȸҨ;ȂȓPØ',
                                                                            'ɁȿĲЬ˄ҰśСϼȣАԆéfойʃÛ½ŪȌќԣΧǆVƋ.áƌ',
                                                                            '\x98ĥŰǅƭʊĢӯŘӁ˜˰ԇˈʏ˂σβ\x8bǰǰԩÝΫӚ\x97υ²Xĸ',
                                                                            'Οƫ˩ϽɩłpɱīЧʔǞΣԞʥΞ¹ϻȊĉǌ҈ɘAԜ,ʟϓЭĔ',
                                                                            '\x9dщҬuηåԉ҂Ď©ÖϞΰУųнώĊ\x94ДuǽϷӉ%ßЭɅҝM',
                                                                            'ʩηƀőӿɖӰŠԕΕċ҅Ҷ˃{ЭԕΩεʔɁĚ\x9bϠďӇùɷԄа',
                                                                            '\x7fΦλˑ\x9bʲӤӸаӜ¼ȹȇd\x92ȫԮԣ\x97ƗA>Īъ\x9eͱȇq2ɽ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'd»ƚǄ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4850078319307175294,
                                                    },
                                    },
                            {
                                        'name': 'ȯ˨ϻ¹ґҸĮѴξ£ÑҶ˥ӛϠʴԠȶΌ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 237584.97981876758,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʒ˸Oɾ¦қʂξϼʠí¼ЭԠЂ\x93ΧɠϿęzƘ.æɺЗлù҄ǣ',
                    'message': 'ɹóǤæȡǗ\xa0ԅïŃ1ũӍʁɰϟΞɮȑɄſԮƭ[˗ȖԣԈҘԇ',
                    'arguments': [
                            {
                                        'name': 'Ƽ\x82ӂûҥ\x9cĞ\x8a¢Ҥñ',
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
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΤьǼƞ²ӭʀ˘ũ¨¬ȶҴƓȝƉeǨʚѫŐʁ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            965311.9994578133,
                                                                            699982.9367388006,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɻŘĥźƹҘЎļӆɰʔ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': "ˣ\u038dȬƟ3\x92ƂϮλ½ɩǽһͰΤȗʾĥԟÎǴȥâȕɑЌι'Җȇ",
                                        'value': {
                                                        '^': 'string',
                                                        '$': '%Üɑȡ_ԁͱʊϖВше\u0379ɔџŞ7ϙ҄ȓȪ϶ȬȎˍˌùҌwƠ',
                                                    },
                                    },
                            {
                                        'name': 'ʀïԈʩӣǹҗȀƷРVзЌāΧκ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175539.256075:+0000',
                                                                            '20210211:175539.256092:+0000',
                                                                            '20210211:175539.256100:+0000',
                                                                            '20210211:175539.256106:+0000',
                                                                            '20210211:175539.256112:+0000',
                                                                            '20210211:175539.256118:+0000',
                                                                            '20210211:175539.256123:+0000',
                                                                            '20210211:175539.256129:+0000',
                                                                            '20210211:175539.256134:+0000',
                                                                            '20210211:175539.256140:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΐŚUӳȏϛxRЛӭ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ųȞɕȄǬȨ˖{˖иѠ\x81ʗ¬љǡмɄ\u0379ԁĬϖɗͽʲ˵шˣƌƞ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΤӀɑɵȀԩҧʱ±ΔтŝΕԨ£Ēĥɷ\x80ç\u0382ψšιʖȰƩҸέ7',
                                                    },
                                    },
                            {
                                        'name': 'ƓԌͱÄҤѢ\x87\x8eϺѳ΄Ԍŧ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӫƏD6˻ϷƠkÀƇβԝ˭҆Ӥʉğ\u03a2\u03a2ҭȜС\x89ÜʹϺԎ»ǒé',
                                                                            '+ɤĲΧ¤Ѥ҅˽Ƣ\x95,цͰȊԛ˗ƛӚ©ˇϛɔĿώ:ɓ\x90ьϼʜ',
                                                                            'ǫЯǌЊƌ^ΥѹЕԟƫ\x94\x83ԑқ\x92\u0383ҦÈϭԄӖѩҗĩĎ˨ғϼɓ',
                                                                            'ѭëŚȄȡʚƳНδΔǖґM҆AȪҒʡ҄ӱŏuˍƲƯĊǱν˷ŭ',
                                                                            'ԢґБЉлѽθiǄcʢӒȱӵișӁýΗԨȴǮΦңˈ½ǓOǺ\x80',
                                                                            'Ƈ˳ʛţňϦΑ%ȨѾϠϵǠ˘ɢӫ˱FƉґ˘¨˓єʁUȾμȇл',
                                                                            'ʎұ\x92ћϕƪӐѥ˖лӰȇƊʡ®ĦӒӣòԓяoњҥ[ԙvсԛѢ',
                                                                            'ǫɳȸ/\x87ǂ|ǘGӨϓϲŴğƫÑϿѹσűɊejͼ/ͲԀº\x81Ӷ',
                                                                            'ƙƝϟҴӚӱ«\u038bѿϣÅЃʄĻ˃ƻŔȹӟЅԇǨ9>ƧʋòĳӘ˲',
                                                                            'ЀūЂˏƢϽ\x9fɜƢЈ\u0381ђ\x8fӡBԂôψǜȊÏӑMлńOǥŕ˘Ψ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĦΈȅ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175539.256984:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ТҫцӸƵśʻȥ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 148096.82535453618,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԎцϪˣҞɹ½ϵиǄѣϱѭÑŷÐΣҵ\x86w\u038bԘřɜ\x8fΔѲӨɽˠ',
                    'message': 'ĞưƮʚż«ŕɿɲϤЅчʼãѽƻɤǙÀӜϭҎΏZ´Ěv˰Πȁ',
                    'arguments': [
                            {
                                        'name': 'ӳ\x7fœȬͱҐ\x99ÚԫžҰÂƙǭѮ~ȑòϋW_ӅȊŤѿӚƙ£UŖ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            91013.34133459858,
                                                                            768247.9165810061,
                                                                            -47834.35018204465,
                                                                            788106.0142454314,
                                                                            504091.6805373174,
                                                                            939046.0674257593,
                                                                            534935.0993113861,
                                                                            603544.9775090003,
                                                                            166914.1750912444,
                                                                            468392.3295963127,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŋћɹανɫĨњˈ˃ƎүĸдǍšàśΜЗѡúԀďʸ3ŝʅgӍ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˳ǛɕőѫǽÈhǅĖˣѓƠΌƭ!ɠĐzɀ[ȤЭΌƐɃҁ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 959800.637299588,
                                                    },
                                    },
                            {
                                        'name': 'аӮԐƩǨʐ\x96ІňÆϙ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɻɇҰİѮҸÝƔĉĺŇ\x9cƂΆεϼԞȵÓͲĩƍԎɮѸuÊйȽ\x88',
                                                    },
                                    },
                            {
                                        'name': 'ЖʣŎŜЮ\\\u0383',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -37302589621855600,
                                                    },
                                    },
                            {
                                        'name': '·ƾéѐŨ÷',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˓ʪɰЏҔϨφTßǮζĊЌ\\¸ʖ\x82ġνMɒ½(>˴Ȟũ\x94ǭҾ',
                                                    },
                                    },
                            {
                                        'name': 'çȻʤ\x9f/ĩӗ\x82іҮͿĞµǺɍңԂҟԦ\x8fϝǷƑʈ΄ǦюlǤМ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175539.258458:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѡn°\x98ȩєδӒıʬ˴',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ƉщȿѲɛΟèÈİƚ\x9cƺІԔɬ˽ԁωǗә',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            920353.4095382143,
                                                                            832698.2889847156,
                                                                            -62269.89435005027,
                                                                            943692.218345295,
                                                                            280215.5525153997,
                                                                            963958.4262370982,
                                                                            380366.1333827512,
                                                                            254049.87672937778,
                                                                            902338.9010099946,
                                                                            911819.1960110697,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҷuˆǿùâ϶ȞʃŌ\x86χãϟtѹѷĢ\x9fÜÊȪӄɓĬϭ\x9bѦɣȔ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '¦ČůĎԨνɊƆ¬ɁǴħbʜÜȿĈǢŹÕK˔Ū[Йӫӭ×ϨБ',
                                                                            '˵ҋȨĉiû)φλɦä½рûӹĬɲαZȁËǒʇȀɝΈė¼˷Χ',
                                                                            'Ǭ.˗ȅĕǚѲ\x8aХ¬|őȎΤѐɖƒɔӘ\xadҩѯӮȡЎȅ\x8cʬǢˈ',
                                                                            'П\u0381ÒÔѮӼӺǬȸƇ-±Ǽ\x89ÂŎȜǒĄԟԔ\x9bΚÑpξǲȁϓH',
                                                                            '|¹κȄǜȂԄʧʿŜĐűŘžǧДń ԖӪƦǦӵĺþϓ˚ƘÃҩ',
                                                                            'ξҴѦʾñʁФsϬȺλҲĺȤѧʢ϶ĸԁБÈʵӾОӂʀɱԡυ«',
                                                                            'ăÀΥӒƅɾѓϖǦ҉ţđł~\x99ċˡȷůύƾԋΊМƊMŵҊς˻',
                                                                            'ЍϊԬpbϝp\u0381ВǺɅ\x96ŒȴƉū÷ԎʔɑЪΓЗ˾ėɗͽΙ\u038dԡ',
                                                                            '\u0380ƛĺʌЭȌŊъτϘɓďKÔ_˖\u0378LɴǼǼHċӓ#ȿūȖŷӏ',
                                                                            'ЛȻƄϽŤщІФȧϴ|οФġԈÉľǷӨ8ƁѵʸƆʓOťʹιā',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϱȖʊ¦ǾŗßǒʚѪǷјǸǜď˫Κʩ>GƥƌӖʹʎiɸĀì˕',
                    'message': 'ȯΞ˕Ͷ҉φ˗цѻūȭ϶ƷȂŀɓеΕʪБǼȣĂгɲʩӂΜѪӼ',
                    'arguments': [
                            {
                                        'name': 'nĀɼρǛσ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ĭЩӗ°ʲЀ˥ԕÓ(˦',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 169721.1264141415,
                                                    },
                                    },
                            {
                                        'name': 'Ш|ɕ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5215135030007804656,
                                                                            -8557804156834847499,
                                                                            -1466197513023821542,
                                                                            -1259748671493684815,
                                                                            1079460619531721308,
                                                                            -4959907215513067123,
                                                                            3723057872346255512,
                                                                            8327562486428582089,
                                                                            -1361654897713407277,
                                                                            1219747107596274525,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ңƆ\x90ĽȐєӞʓŚēˤ\x83ƙĂȦȐѵ²εɒ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            661978.4159447086,
                                                                            641839.3771939756,
                                                                            539278.696464759,
                                                                            329967.3652783835,
                                                                            353333.58556171897,
                                                                            321076.8047283541,
                                                                            324914.0207259091,
                                                                            585275.4810661768,
                                                                            414734.80642119097,
                                                                            629357.4165717695,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʳŜз{{˖Ҩ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 389147.96705726034,
                                                    },
                                    },
                            {
                                        'name': 'ȑТˎTªӻ\xadл\xadӜƥeӧˑӾԨĈͿԬ6ŊϜҠăϦϼȥͽϮ˙',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6365490457393440937,
                                                    },
                                    },
                            {
                                        'name': 'ùőȵ΅ЇβЂǗЯɝΏñƚӤyˡ\x81ӭΉαƹǨɆȝ\x9bȒ',
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
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ũˏԃŒБӡ*ǸӾǁ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8292610354510845306,
                                                                            -7544057014570369000,
                                                                            1460797004962334049,
                                                                            3161441907429880166,
                                                                            -6114578769009673589,
                                                                            7122981806413917127,
                                                                            -3704053346820176291,
                                                                            2442921470801106762,
                                                                            3248078177230289735,
                                                                            173308898280988924,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǖͻƵң',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175539.261773:+0000',
                                                                            '20210211:175539.261797:+0000',
                                                                            '20210211:175539.261804:+0000',
                                                                            '20210211:175539.261810:+0000',
                                                                            '20210211:175539.261816:+0000',
                                                                            '20210211:175539.261822:+0000',
                                                                            '20210211:175539.261827:+0000',
                                                                            '20210211:175539.261832:+0000',
                                                                            '20210211:175539.261838:+0000',
                                                                            '20210211:175539.261843:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϒӌ\x81Ôʰ·іΓԀŵѼƭќҵÒǏӀĥ҉˖\x8bВǒĩɾҵ˛\x9eɼƛ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԅɊƑȏ˙ŋʾͼCěmδ˦¤єƻӒϙЊŲВ\u0379ʾғɱѽř\u0382ǅʦ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʕ9āĕǡâŌСҝŵɨ˻ҥȥ˂!ʳ΅ϗɤ½ʯ~бɲ{Уϣτʤ',
                    'message': 'ӷϞKΦѰ:ɥǑȃ÷\xadʑ%hԃűЅĉɹ>ӒƽɄǽī(=ΧϹȠ',
                    'arguments': [
                            {
                                        'name': '\x81ѨӴϬhϫžǤ˫ΨȄ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'dǭԮϺõÑĊ\x8fƒǯĎĖӤԛˬǂ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175539.262612:+0000',
                                                                            '20210211:175539.262624:+0000',
                                                                            '20210211:175539.262631:+0000',
                                                                            '20210211:175539.262637:+0000',
                                                                            '20210211:175539.262643:+0000',
                                                                            '20210211:175539.262648:+0000',
                                                                            '20210211:175539.262654:+0000',
                                                                            '20210211:175539.262659:+0000',
                                                                            '20210211:175539.262665:+0000',
                                                                            '20210211:175539.262670:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8eЙ\\Ԉʓ-ǵ«ҏȲmѠʿóϪԥ@Ư\x96ʭǺѱХƓΜǗ˚ε6ѓ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ϛʐ÷\x98ӢԆÂȠʺӜðӄ\x82ԎłʖƢ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɝѲʝԊÎұмʌԄ*νȀȓɽȓ«ŏŬ_Ð¶Μˠº',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175539.263127:+0000',
                                                                            '20210211:175539.263139:+0000',
                                                                            '20210211:175539.263146:+0000',
                                                                            '20210211:175539.263152:+0000',
                                                                            '20210211:175539.263157:+0000',
                                                                            '20210211:175539.263162:+0000',
                                                                            '20210211:175539.263168:+0000',
                                                                            '20210211:175539.263173:+0000',
                                                                            '20210211:175539.263178:+0000',
                                                                            '20210211:175539.263184:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĩѐ˓ȁĲǕĪÿ˼ԇôёƖƢ\x95өѓϐƘИΚȮΙđҝULφĳΪ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            580540.5984637128,
                                                                            -67236.15154864485,
                                                                            850108.0323172846,
                                                                            513594.44158118987,
                                                                            734045.898390564,
                                                                            567733.7373898055,
                                                                            467707.16028080985,
                                                                            816583.9333135629,
                                                                            252720.10786009318,
                                                                            9776.409848434574,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ўvŶĖƗӌӓƽÙ\x8cМ\u03a2ģêԥğ\u0380ӷNĤVʻ˫˅ʊЅétqȯ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175539.263635:+0000',
                                                                            '20210211:175539.263646:+0000',
                                                                            '20210211:175539.263653:+0000',
                                                                            '20210211:175539.263659:+0000',
                                                                            '20210211:175539.263665:+0000',
                                                                            '20210211:175539.263670:+0000',
                                                                            '20210211:175539.263675:+0000',
                                                                            '20210211:175539.263681:+0000',
                                                                            '20210211:175539.263686:+0000',
                                                                            '20210211:175539.263691:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'a·щʹӪӪXʢY®Ӯ&рʨȪ҄˅ƩŇǊ\x92ǩБƵӇɑҶ¥p\x7f',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            890139.2274665976,
                                                                            26807.796154014184,
                                                                            344605.50806610816,
                                                                            800784.0160337188,
                                                                            937099.5944877969,
                                                                            29796.40931759977,
                                                                            340667.34128093976,
                                                                            869015.5866417576,
                                                                            353007.43452787073,
                                                                            655861.963530034,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'řɀķɬˏˆ«ʝɘ\x98ӘY҄Ƨ\x97ďΈұɥӚѻpѷǘŀӁȡˌ҈ǰ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 237034.463959325,
                                                    },
                                    },
                            {
                                        'name': 'ɍ;ԗe˔λǻʡ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1284270842031809898,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˖зАԕÎ¦ĺȨ˲Y.ϳзěяʃŬȿǮȿȍĿŶŎЯĂǝΰ`ϡ',
                    'message': '˗oѝȘӡ\x92ӰγγĵĭʇƌŖӫʆ\u0383ɧêȓ\x8cɂƁH\u0379ȅ\x84ũԧͱ',
                    'arguments': [
                            {
                                        'name': 'ĔǤƄʴ˰Ǒϊǐqӡϝҏèҭ˝õgGdέȒ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϬU˅ʄΘç\x9fѾŸZTò΅љЙŌɈƆӷЊŰÐçʸзűӃɢĽω',
                                                                            'ÑЉʥӃĦҭˮͶT5ʇ\x96ǂĦҘеȎѿ\x97ʋμ˸XҸƾͽʕмǡӖ',
                                                                            '˷λϋɷțɵцðɣҌ˭\x81ѡ±˖ёфĦǮȾԛΐγɴЂĤǔǌЃӉ',
                                                                            'ǪȒěϓɿŴ˷ӾĲžѩ$ҡˎӥʎβɌʪǄ΄ЭˑѠƘˈɨŷÂǆ',
                                                                            'ɘξŀҘͰу`ˇҟ\x96ΓȃŴлÉīǩ£ԍ©űˆƵΑύΥґƱɝӲ',
                                                                            'ϐŲҺϧҕʺ"¾Îσ=Ӥ΅ʗχЦŭÞӡђʊϕʵ˹rЁ³ӁΓы',
                                                                            'űIĬǫj/˚çȁǽΏăɑǞȼʷŹҴƲфǡɉʅӶϵȶҲы.\x8d',
                                                                            '\x8bѽƅƪԒҫɜϤMǸȺ\u038dƃ«êȽǓзƞʚg˙ԙNǿѸfĕʉʸ',
                                                                            'ҔsћҔ\\ǔ˔ǫƶĉΩāԛǯŰΤǽхҲѯȰӜϤŐӟҹЖʛɦȊ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ыҝ\x89ͻѝчˠ3Ο\x9dęЬʴѲƑªʟˑǶɗʸ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 826907.8061358695,
                                                    },
                                    },
                            {
                                        'name': 'η\x7fÁːƾκРΙɦ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2459146043739730237,
                                                                            -9103001788743864362,
                                                                            7015019549116418564,
                                                                            7822803093546484896,
                                                                            6999211904161177398,
                                                                            -8464787371306297294,
                                                                            -402772639210223367,
                                                                            4044712084222183175,
                                                                            4935588751788664282,
                                                                            -1594916358102436272,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ġ´Ɍ˼ǸϣԝʙԠ©ɱЇƂȺγĢМКԨԧśϘǴ·ɈӀKv\x94Ψ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'τǣιėϸ˧ИšЂ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175539.265631:+0000',
                                                    },
                                    },
                            {
                                        'name': 'nìўP',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4840201337895708549,
                                                    },
                                    },
                            {
                                        'name': 'ОʨʅĈʝΟгͲ\u03a2Řќ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175539.265873:+0000',
                                                                            '20210211:175539.265885:+0000',
                                                                            '20210211:175539.265892:+0000',
                                                                            '20210211:175539.265898:+0000',
                                                                            '20210211:175539.265903:+0000',
                                                                            '20210211:175539.265909:+0000',
                                                                            '20210211:175539.265914:+0000',
                                                                            '20210211:175539.265919:+0000',
                                                                            '20210211:175539.265925:+0000',
                                                                            '20210211:175539.265930:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '©ΕɩĉѤÃЈ&ʲΚ\u038b˚JƥѬӔΐƫ{ʩәԩҹ\x85ӱʩĒСȾ\x88',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            344203.40728376555,
                                                                            482849.85480123945,
                                                                            761142.531881215,
                                                                            690853.1436764215,
                                                                            834977.56476864,
                                                                            611574.0994888031,
                                                                            148846.1836292475,
                                                                            -49532.74528679974,
                                                                            301529.4208765483,
                                                                            537064.9543194495,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҂ĝшΆƄԬѷ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӌűȑɞm\x85ӘÛɁŎŊDύɏƹαƏ8\x82Ʊſ˜ˑ\x95μôƁʞ˽î',
                                                    },
                                    },
                            {
                                        'name': 'ԛѝĠЮϥΰ΄ˤЯψіŹţѠ&ΖϴΖаӑϤ˫ζІǣҺ\x8bЗӴΖ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɒԌƱϽҬɛƾөΎԝơŌĕʯШ˩ǶͲέλԕǓʟÝʰӍԊάΠԗ',
                                                                            'ЎΒѤĥL\x94ЊȢò<ѲáΟɀ6ѓºΠkţ\x9eǞ-ϷĺȄƌǩҸŜ',
                                                                            'ɢϣŘϲζZӭůʷʿΝԧӏĎъvǢǸȍτɽјεĄƉѤ4¡Ť!',
                                                                            'ŇÔˍɳc҅èρԉļʓǮЉȡŌ˺ǔЧ\x96Ԍқҽӹí҂ǝԂđыȭ',
                                                                            '^ЬӋóÝ˞D˪ǉ©ѷˁȪɷSʠτҼĻŔ/ƅȷɲƑŝ˵9тǱ',
                                                                            "Ȣ&Ԃȳľ\x94ѫ\x96ÕǴȳeԓ'˟ӵ\u0380ȻƯǆȓԤϲ\x9cʸʭ(şРî",
                                                                            'ʒŇǜȝÖ˼ĴȻѱʖӍɎJ£вâkƾȔȨ©ůƋRϣjЪʢ\x96Ѭ',
                                                                            'ЁȢϡӂĩɚȼȃ˔ѡĺѬèűţƄϿƬ\x83ɭ\x7fԋѶҌÂšúƫαʣ',
                                                                            'ǂĵɸŉȴҮԉˇý\u0381Ԫ}Î©Ϊãī\x85Ҏ\x9aÄ҈҇ɖ,ːкêЮʠ',
                                                                            'Ǫü˳ìѯоɈαұˁɳȜͽğˬǄĴԂǽŊѡίΡȜϑ8ИŘRE',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƹǙ\x86ʍёшûҏ=ʇr˯BҙǴΣϤ˃ҳЂѮA˛ҹ˳ͶԭþҾw',
                    'message': 'ɈƖȋȟƀ\x99ˌȉ6ʨY͵ŝȢԂō˺ʛʕΆˋZͿøʏΘʴѽҴĲ',
                    'arguments': [
                            {
                                        'name': 'вlӍӶÜĪЬɎɫǠʾѥɭȲϋл9ѭǞшɡЩžĬȟǻɮϟǊϊ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 747667.0583079223,
                                                    },
                                    },
                            {
                                        'name': 'ŊЯdқРԆƧΆ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ФǿŃͺԑʄѥӖǁǍyГ˴ȟɍ5ˋπқ˗қȽӨȡÔɎXɪгυ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʯéɉϭǋԕAάΰˀƶɑϋȠқŃәƳ\x8eӄǛԒы\x97ȝɧPԁġʁ',
                                                                            'ΝČϏϳŊ«Ê\xa0ӹǹàǭҟвœʑʳŋҴӢ¤ĵİŤԭȵϡԋķď',
                                                                            'РуΌӃÀaү҂ˢ\x86\x8fɷ:śȜҧȍмΜ«ʳΰŹǁԨ\x99ɇ¸ɫʕ',
                                                                            'ƗξŰҀӗµɢϒǯɀyȏΕǕҖx;ȃԆĚˎʋ҂\u0382ƕҗ~ǯθԫ',
                                                                            'ȶȣҩϬ@кė\x85ͶɢΐыĠɝ5ŽÛ¾ѝЁÂΓôȎËȞȇƣƌł',
                                                                            'ӉαнӕɾɂʽďԦ*Ϣ͵\x99ĄҾƠάȍˆȵʂȻұԞϲĈθɡφГ',
                                                                            'ħκĭƸɪɔǈœϿŶɦaӬ˷ÌÔЃ˯ҕņȚěNЏԧqʟԀȗÃ',
                                                                            'ЇҢӉlГǱΤßɐcЇHПÆԐѧʮˏ\x96ȌɒЍԑƥԉǋŚϑϬù',
                                                                            '\x80βƷН7˪ΦɄѯÎ˽$ЊŐSҁȥΊ˙ӮоǨҳЊī>ɱҫȻǈ',
                                                                            '˲ĦϦĕϧȷ\x9bȒȦÀƷ˭ғҀʻԧĺ˷ŸїӲњȇĻӯɷ͵ƫɶѸ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȾЅ9˂Ιə0ǚѸйĬҸʭǖǢπƭɳӱ\x90ӻȗœ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175539.267862:+0000',
                                                                            '20210211:175539.267876:+0000',
                                                                            '20210211:175539.267883:+0000',
                                                                            '20210211:175539.267889:+0000',
                                                                            '20210211:175539.267895:+0000',
                                                                            '20210211:175539.267900:+0000',
                                                                            '20210211:175539.267906:+0000',
                                                                            '20210211:175539.267911:+0000',
                                                                            '20210211:175539.267916:+0000',
                                                                            '20210211:175539.267922:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ħiČɬƋʷɧΧԛƫӉ˟¡\x86äҕѠŊŵĤɟˮӏΟ¿пҗõœÚ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            685499.7831845025,
                                                                            610994.4797406307,
                                                                            7942.92107223974,
                                                                            687833.0627592234,
                                                                            265418.5909688589,
                                                                            263719.7097315246,
                                                                            323963.95257101965,
                                                                            317445.57097296434,
                                                                            615119.2700809382,
                                                                            813932.8363046187,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ęԧɖϹМƵԔԇ8ҪͿƾǍąԪҀțʫ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5913246490962548469,
                                                                            8220028474213401068,
                                                                            525295717534486996,
                                                                            -569253984430470782,
                                                                            -2442537150539421933,
                                                                            4061365601437968818,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӑƼ=ʿɍȝԨήȤĜɬПϿƦʂҷʐÒΪǌ˅#\x92Ӑ˗yÕјȋҨ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Эӹ·юʍ\x8cҁӾʹǚѹŝ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2960695191329867529,
                                                                            -5652056132561062820,
                                                                            -5991173822689977563,
                                                                            -706294482909673212,
                                                                            -7390151043912927020,
                                                                            3749753153865772344,
                                                                            -771576986968198120,
                                                                            6940123045027007118,
                                                                            -2393871807892806769,
                                                                            -1088816787445508703,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͺɊӔϪ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ρ\x91ЂƱԣʆƝ\x8dHӼǚɑnÍӖӃΦһǬŨЀϯҷҢȃǉɮӈǤԉ',
                                                    },
                                    },
                            {
                                        'name': 'ďҾļНȎƍȭʠӃͶʿïӅϧԐÕʳˆˮҽνˍҷαϞʰѝѸϊǿ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'βίҋҼԗÀ΅\u038bϘeːGþԞ˙ϗϞÿ˻ǱÉ RȖӲʥȒʬ ǀ',
                    'message': 'ЭЏӣπԦ0Өνųѝӂѵґż˝ςǱҎО ǎúÈǧĹġgίǣ&',
                    'arguments': [
                            {
                                        'name': '\x97ʃɁϝɮԭύПɢԆӀʵˠК',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '¿Ϝϟ\x98Ϊɨ˃ćϣӵκȤѯFb\x93Άʶħǐ˾?ɘė˥Ό˪хıĴ',
                                                    },
                                    },
                            {
                                        'name': 'ǭʆ˶ҵɔ3҈ϫűΆǺͷƳ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175539.269831:+0000',
                                                                            '20210211:175539.269846:+0000',
                                                                            '20210211:175539.269854:+0000',
                                                                            '20210211:175539.269860:+0000',
                                                                            '20210211:175539.269865:+0000',
                                                                            '20210211:175539.269871:+0000',
                                                                            '20210211:175539.269876:+0000',
                                                                            '20210211:175539.269881:+0000',
                                                                            '20210211:175539.269887:+0000',
                                                                            '20210211:175539.269892:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '12ĕȍǒƭλҘ>ǴʗūÍµԒϢŎ¿ͿƄԖåӆǢԒøт\x82ЁӼ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
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
                                        'name': 'ʙƶԜѠĈÿΛȁŀ&ӢǤɴΆɕНɋԔӟŻӺʄŏоUĩυƬʨ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -892802205791176578,
                                                    },
                                    },
                            {
                                        'name': 'ԉǐåаόŃ\x86ǃΗʚҒΚͶӳɋͲʀƾιŘɰҫ»ÏԥeŲȺĈΚ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175539.270467:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ūȳѴƴӓӑХ˝êŗÈʾɴѝϩɷ\u03a2',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175539.270625:+0000',
                                                                            '20210211:175539.270639:+0000',
                                                                            '20210211:175539.270648:+0000',
                                                                            '20210211:175539.270654:+0000',
                                                                            '20210211:175539.270660:+0000',
                                                                            '20210211:175539.270665:+0000',
                                                                            '20210211:175539.270671:+0000',
                                                                            '20210211:175539.270676:+0000',
                                                                            '20210211:175539.270682:+0000',
                                                                            '20210211:175539.270687:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ïԊ[ƗŠżŀŢ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175539.270893:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ş\x80Οʯ\x90ҵЕѤƅԢӬʑŹȳʴĢΙϨôƪɁ^ϡǊηБişȽϴ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -663315975753092360,
                                                    },
                                    },
                            {
                                        'name': 'ԉɠ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6961984600946643828,
                                                    },
                                    },
                            {
                                        'name': 'ġƭǜҿŪǣҊĿ¬^ҪǌÒфԏÙ0И',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -71844.52712347641,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӕŌуεӺɧȝԇyɛžǜ\x81Щ5Ϯ×ǘĄΤȖ˨ɇˤȓdǉȢӯȌ',
                    'message': 'ҡŨ˧~ӻȵŻƵѽǟӋӰĪ#ɷ˃ǩėĝʐuŢɏʀЈƳɾѺ˾ƈ',
                    'arguments': [
                            {
                                        'name': 'þœҀǃŧɏ\x94ӣȀǔҥΩɒ{Ⱦɇ˔əɒʕϠŘњӲßԔ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175539.271649:+0000',
                                                    },
                                    },
                            {
                                        'name': 'жɱжƮԭҙЩu\u0383ϬƉĶҏнɋÌ\x91',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1244367760408658174,
                                                    },
                                    },
                            {
                                        'name': 'ҷЙ˾ȟğžǧЖ˨Ԙӓǂ\x8aɊΰæÊӌӔÍӎGЫИшҁʀŔǽ҃',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4018751845368622307,
                                                    },
                                    },
                            {
                                        'name': 'ƂӉԇѦåͷԦºʋǥˆċӈзƈʎđϷƮ\x97ηșƞ\u038bӼЎͱκ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӦԂô\x91¡ǼƭɍƳʮҼӭϕɋɉɪϧƝҨ\u0380ѽˆԝŴɐ˳ζTВų',
                                                    },
                                    },
                            {
                                        'name': 'őӥѦCƜ{ȪǅɼŢиǽԄ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3406277298616226075,
                                                                            -4404630264969583537,
                                                                            5319672828557677870,
                                                                            8981027651990161678,
                                                                            8484512164397116832,
                                                                            -3794503330609336092,
                                                                            -9031717009804625270,
                                                                            4492913455126655183,
                                                                            4113963491002337590,
                                                                            -1322685162062388866,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'үōЪ[@˺ϗ΄ϲ˲ĔѶҞѓɇԋķһȈƍɄɔӻƞƣŚ˾ь.\x86',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8403909017639867163,
                                                    },
                                    },
                            {
                                        'name': 'ĜҥɒˁО!+',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ňȷʦϤːʶŇϚԝѹԖҐʾÜγ0\x91ƎȭŞû˜ñη\x9bеЈ͵ɿø',
                                                                            'ͶÝªȏȳԌłͳЎ¡Ƀώ˒Ơͳ\x88ʤ\x8fϕ>ϻEȇ¡eИľĶӼϕ',
                                                                            'ѲƐüȞŽˈƔɂёɭѵ\x83ӌЈҊșϤ\x8c˯ļſĞӓҷ|ѸҘįɍѫ',
                                                                            'Л˦υ҈˞ɞŕŚҧɞƓƓ҄ò˒ѨŕÐĜЙȤ_ӌƱϤҶźŢɺщ',
                                                                            'ӾҢȣϧʹ0ҍϠЂԙϗпĲɠМ\u03a2\x9cοÐɜԚ³țƬϩĆҺԇӄİ',
                                                                            'іżϢˤ$ёμʸɰԣŦҟыʜƿїŐˢŋәɗĪΓɘԨ\x94cƆХғ',
                                                                            'ҊɥĐȇíƔоǰϸЭҙä˰ϕɩŉЩdԍOЦ҇љȏƒҴɂЍŻʐ',
                                                                            'ǾǹʭΏϽțɱԇ\x83ȧȁ;қɉİǵнЃͻŤȑĺͼğƩ˥ȞƕŃϡ',
                                                                            'Ǉ»¼ʶѦŲŵÛ\u0379YϕɄuŔԜŖυҕɍ˻ɃâɓɢԨĲϏĆÿϒ',
                                                                            'κ\x99҆ʦΝʟόӞРԗŰФˉæǨ˄ϴɌσћŃԞϏ\x800ѪǇˌ\x89Ȼ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¹ǭȝғѿԬѫƎƞȆd-¡ɔʈ҄Ȅ˸ɣʣɾӦŲƺˢ0ŲҦ»ǭ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175539.272908:+0000',
                                                                            '20210211:175539.272920:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ƴÏ˻ΞƟ°ˣӸЊ˘Ԑ.'ͻǆҲӀλjƶ˲ӟɕӳ",
                                        'value': {
                                                        '^': 'float',
                                                        '$': 470078.56140287966,
                                                    },
                                    },
                            {
                                        'name': 'eķəÙҐ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210211:175539.273210:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ơǃĸѶ˭ϯˍ\u03a2ӯїȊîɈȻSQӭ\x8b˦łˮԝѶƞҶҦЇжʙб',
                    'message': '<я\xa0ōϿÁԑԈɚϽŲÉўŲɆŶԜʮÌұҀЫȣʥƶͲŞ\x80æö',
                    'arguments': [
                            {
                                        'name': '´ĦFХϕǣˠ˺ϾĚʞψӗ\u03a2ȕ\x98\x87ӶԓȉȨΌ\u0380ɣƕȐĠmѢ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 502743.27584424126,
                                                    },
                                    },
                            {
                                        'name': '˧,Ľß҆ô˾҆ǌ˦Іоыœ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8646701827377684960,
                                                                            -5332419872747721362,
                                                                            -9213082481204645141,
                                                                            9170260451381247259,
                                                                            5622728692027739072,
                                                                            7488926341154669999,
                                                                            -7715025708237464250,
                                                                            -4269017336002771633,
                                                                            -6658572752786321522,
                                                                            2456781605770354253,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "\u0378'\x85уϱʲ¶Ɨр˨áÙʯȁɖ÷ͰʈԀǔйӣˏɟƌˀ`ǋЕ˯",
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'љǉgЏǋɻѢ\x98бΡˡɚԁ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x84ţŲӼ®Ҫ\x82Ԇӟϴёϡηė{vŉШхÅˇŒʴǉĊùȀ2%Ɗ',
                                                                            'πːĄ\x88Αя]ɗԫȲÅŢҒ\u0379˦\x9cèјǩ˷Bҷ\x83Ͻʸ\x95ƆӇƝɰ',
                                                                            'ѹ϶ѭԐңXǢƐƾӿϟƥĶɺϚÌş9шͽʊcКŐµϘӤȀѧԅ',
                                                                            'ĤȩϺuƛūσa˴҇ҊТɃȌ\u03a2ƹĜƧ˽НɎç¼ѥҼØǬ\u03a2lς',
                                                                            'ʤǻʝӪ\x92ϖ«ԏêƩ˗ҙʌъŎȂŉ;9«ӸԋАɎǄ&úч\x7fϊ',
                                                                            'ȕǡ?Νʬӡ\u0381щŰŹȐΜӴԄюǾ$Ƈ˝èʧʊ\x95ЩҐáĆә¼҃',
                                                                            'ԢŌɌ˖ƆÁ¹ӴΘŋĕɺѯԐ%ɩƄӔğŚŻƙҩɛϪǨɷҧƸў',
                                                                            'ˤӽС\x95wϟś{ɰčƝʖΒŸ҉_ǟ1\u0378ľ©ҊОɧ˫ŉƋʍƥǥ',
                                                                            'ѢҕϽƸÝεwΔąȴӟӨϖϺԥҰǣbάƟ\x82\u038dĹґNЀϑμǂŘ',
                                                                            'ǋΟȱпπ6˩ӻ4ϫδѦӌʸӴͺʺ·Ҽăϣ\u0379ɃĴə\u038dζɕ¢Ǖ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'þ=ļlΎ!ϮӴ$аȒϸӖ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210211:175539.274564:+0000',
                                                                            '20210211:175539.274577:+0000',
                                                                            '20210211:175539.274584:+0000',
                                                                            '20210211:175539.274590:+0000',
                                                                            '20210211:175539.274596:+0000',
                                                                            '20210211:175539.274601:+0000',
                                                                            '20210211:175539.274606:+0000',
                                                                            '20210211:175539.274612:+0000',
                                                                            '20210211:175539.274617:+0000',
                                                                            '20210211:175539.274622:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ъʵ˹шƬǊȒƨѾĝĒǆ4ұʰ`ԀҭĀлYвż)Œ˞ǈԇɭǠ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϞӄǋϣoɴȔªǼѸȦƚ\x89ȈÏȏ\xadʍȡœȎʳ\x93л϶ΠµȑҍȦ',
                                                    },
                                    },
                            {
                                        'name': 'ơʇǯ҂Ӌ˷ˋǣӰοћcΠȵ˭ҼǼĭ7ԫԄ˟˚Ĺ΅ōtҲѹʟ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8702443582983290705,
                                                                            7315415133267759089,
                                                                            1889472676752026034,
                                                                            1145271834970047786,
                                                                            -3364157867702960794,
                                                                            4044817730525930932,
                                                                            -3498900742488282104,
                                                                            2648380236907539295,
                                                                            1152535932809941347,
                                                                            9077377764123638959,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԪԨʒǎ1мЍũæ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7037427500394075403,
                                                                            3503795899972007311,
                                                                            6364967721086463699,
                                                                            4695577740316575132,
                                                                            -6592686509208534440,
                                                                            1101977679399637932,
                                                                            -529130491706542957,
                                                                            -1129612128104564317,
                                                                            -9191808619811112648,
                                                                            5424024541451139494,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ύԢ¢ԡ˻ΞԣώǎƹЦ!ċұȎƢ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '¿ѓ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 492171.14544115914,
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

            'identifier': '^Ɇхk\x88',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'ƈҀ',
                    'message': 'ͳ',
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
            'name': 'ǙĿ·\u038dϏǌ\x80ƦĖʹǲrĐǞõΗɝ¾8ŨµēŜĆ˳ďśЋɲɆ',
            'error': {
                'identifier': 'Ӆȸʺ0ǰѲ˫.N˄\u03a2Ɩvţ¡ί¼ȅʾьŲšġɍϾ?мƖˢǅ',
                'categories': [
                    'invalid-user-action',
                    'network',
                    'configuration',
                    'os',
                    'access-restriction',
                    'os',
                    'network',
                ],
                'source': "ďτɈǇ˱Ƽ'GĲо·řǨāЄԖŉļuñ¬˺ǓџǵǥҲ\u0382hɄ",
                'messages': [
                    {
                            'catalog': 'ϼ4ŪԞǏá\u0381ȪҺΤþˡūѝԄǮ©Ϲː\x9eӓŖҪÏː҇ĬМ˖Ķ',
                            'message': '¶ráĩΆÍŖȅĸɞAɐȓƬˤԖөɗːǩįƺ2´ĈșǮԞɡҹ',
                            'arguments': [
                                        {
                                                        'name': '\x81ŬЃ¯Äƒ˪âӳѾąӊȣŢζԝϷǒȵǎ҂ɐӆƄӝøȜŢƸń',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҧ΅ԗ>Æ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԉ9ŉӇǚĐàҨɻTéΧǧ\x82',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƿԢҢҀ\u0382΅ΐΨϣƩЩr',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6514348522018881847,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҁ\u0379ϳúɡȄ8аˢĪșѤɝĠΖđƬƃ\x8cū',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¥ŋϼԊҴWώϓåƩԥkɏȼҘ˔šȩͳŀƸ˙υKҠӦƋϩԮΘ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7455058742418622517,
                                                                        },
                                                    },
                                        {
                                                        'name': 'oʝҕԅʭӖ)Έ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'εӧЁǆŹфÛϔчȋˮȅȚС]ʰԮʚȖѯTŶϛҙɵƋЌŅҪʃ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƻ;,ԕ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'È\x95ǈġҏϖǗϝNҧɴ¶ҠȰ҄ɓԆ{ҶΪ˹њФǃŌζ΅xЇӬ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 191358.9956515557,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԑǟӓУϠŒҞӭƌӎӣƤԆԏĐě\x9dɀĵƹ\x865ȔŷȿӢɄЯ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -9177144206714957663,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '[ȵŁŧSÁНűƍʄʥĻϧэƋ4ZǈŃПƂΗȱʳǊɁÍч҉Ö',
                            'message': 'йЇ˄ʾǊʿËϖ\x83ʸb¯ԃ´åŝPκȾӆǉЍуȜ˱ȶҽNϣĔ',
                            'arguments': [
                                        {
                                                        'name': 'Ɲ˼ЎљƯӾΙϱЧ˓ʂʝèˇaG\xadǎĿÏŬїУ˞ǒəϧԥΣ϶',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 568886.6576111572,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǇЏҷԋÐτ˳ưǸĎŹ·Ζȼł\x8cԀȔīǷ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x80Ѭдʻ΅ȥѫίкǝŻńѩΡʿч',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 765245.3198650887,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɖ®',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6185960775101247326,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɪ\x8aĞȞƐчi,»яȹ-ȄƤƢƱ˩ԬʤǔѯрȋҘőǣҶŞŁя',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ćčƉƁȑӐΪ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɒяȾѱ҇˧ĔӕŻƁVԬʐʝŋ¼Ʌ˗ҎϒΥľ<˂ӓͺ5шжm',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϽzĎʾƱʑʥέЌԊȹFӞƠǽΫ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'әɦǟɶ\x99iήϟɃ¬ыϝǥϸCŅ˼ϧ˜Pԙʩ\u03a2gκƔǑŒ´Ǧ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǂѧȈ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 370524.4901436519,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʳBǙ7ƊӠxνͻǡˎҽδԟȷʜ҂ѝńƇϓ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǌŎǁȭτƮ\u0383ĮЂ²ёØϷμƪLЧчɚBˆ\x94Ơĳ˚ZȪКɎω',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʕϣǱƀžͲ\u038bǡĴҬ$ӆИϋҴђɧҨϿƮēşȲ¸ύΧȯƿɌv',
                            'message': 'ģ_ӛю\u0383īӋѷʊӝГέƻŤҶˊԂ2ӄ¶œÆƹót\x97åÎ±Ȭ',
                            'arguments': [
                                        {
                                                        'name': '҄',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƦƷԀīҎĈђýǎɚӆ@ыȇӸƂ˼ĜÍғƽǐϳύҙĄːâ҈Ѭ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4213995287493762432,
                                                                        },
                                                    },
                                        {
                                                        'name': 'JřцԮѵϔ\x98kТґг\u038bȮĬϏMáӡ\x84ëǶӗӫəƌӮ˞ΠǨӴ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǯ*ΐɼʹ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Äɨκ˼Ѩϣ;ЇΘұʾӃˋɵϴΒɳцǷŷ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 240798.78289420408,
                                                                        },
                                                    },
                                        {
                                                        'name': '҅ɱƳШǥȶνͺω˕\x9fѵcȔĔɌ ŁѻÅɮj¿ΡҲɷ¿Ȱˣʍ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˹Ͻŏӑнʹô˗җǪŰF\\˻ȻûǑ\x8a·=ҸҒ˘hӅѦЌӑǼ|',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ľӺϢųĵ&˃Ԉʴˇeɐˡɿш8ǖˁßȏ}P˪ҁ˭ӓȪ˃Ǩǥ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȗʫîҠӣ?ѸЫԃȪÃЭ?\xa0ӎ÷žΨëЗέҟӮѰϣУĕųˌţ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'χʐù1ͱȧğ҄ȽðŻƯǚϡƠӉ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ãс½ʉψ3ƊêƠόmŧΕϜ©ɟѷÄӔӍÌϫųǔǔέхчĬͷ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175539.237839:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x98ʬ˱ ʱǘċèͶԁԣŃӑİ)ɚʠÔȰRӮƨϮϕ\x86ėeʮɥp',
                            'message': 'ʢѴˌԁҒ\u0382(ӓʳΟΘтϗĖʛҜĥƷ©ˤϓɈ˳/]ӮúѽɼȾ',
                            'arguments': [
                                        {
                                                        'name': 'ϩԋÒϠˆɺɨ҂ĊĮȟʨĎӡԣ˥мȹɷNvхѠlҽдϖЏǠ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӉԨƛƔҬˁĤϲƿƯě8σĹųǡ\u0378ǰδ˾ђɝМɲ\x97ʲĠȕ5Т',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʾŽˢŖŕҥ\x9f˒ѶԄбȚŋћƻøψԬΩľȐƘƤɨ)ӣ\x91ŞǥǞ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ğǺǑɡÀgμéɌͳЩԣǾыɰǭЯЈȠħ1',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3219059603484337794,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѥԙȌҮ\x82ІҒˉǜϣǇαϮӎĸӤ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5517852458273569627,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӫɒӽєɨԖȅі˶ҵÏƥŽǝΐ˨AӚĘʴļʃŗєħϋʑѠѵŢ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƓĿªɝӞĻȌи',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƻ©ȤѵĵˬʄϝҔ]ҖʺЭ¶įą\x9cѥ¢ǭǩʆäβǌƤċԆˌϭ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 259062.21175436937,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԏ¹NͰːħĴĮ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŜӦȞŞЌЇTȽȲˈϣƙƈ\x8aӯƸ˭4ѵҼѶ+ʝҕ?Ϋ\xaduɭz',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˲WЈλҠȠ5ЉɁēəĴȗź{ɜȀªӠЃ˅Ԝù϶ʗʦˑџǼҧ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ѧ8Ȉ(˗q\u0379%ѪϚ´ʎfǕ҉ļĎʱƕø/\x7fɛťѹɸs\u038bˠǾ',
                            'message': 'ϓδϰˍ҂ňŃ˶ˤώcӠŚſɤϑЃϤħνőãѨȼǅё\u0383ҵΊљ',
                            'arguments': [
                                        {
                                                        'name': 'ϰӱӝЉƻŸŃȻɪʫԦÍ@sĀȈѾ˃ӄҧǖӻԤÞˈЅ\x8cŁÇӦ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЁѓɭΙ͵Ǩƃ*ђӐɍˋȀ5ÍӍҾ·ІˁͷνȬҜҏƹ˟Hķ\\',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҰȨ\u0383ȭϣӺǫGǴŖǴқåӉͽђЛȒçɒQľȢĴλʘʹđźӲ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǎ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ηǻҷǩĴѭҳķkӵʰɬӸ\x83´ӝʧ\u0379ҋǇßȔĹRď£˜ĦŚČ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǄʚКrŌɧ´ʋÔƏɁ\x80єăŶэӖϰиƆθɤԪǵҟӅӇ\x88»˙',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ľŀΑ9oȫ/ʕŦāȉҾƆǅαɦɦϮΒŹĬλВ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'їǅ\u0379ӫҌ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȳ\u0380',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -84032.203518261,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϷΝεԇɪ´ҡϓԤËƱʺѡǆʕɽ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÓȺЈӧ˼Ы<¾\x8fŏҮĭǵκDˀӆ˃fѕ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȢѿўķѻøԊζΧʏʽβȎɮʶ>˖đÏϗmʉɓēļoǵͲӒӲ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʑƆćњϪКřȻǧһ?҇ǥГˤ!њ\x80ƽϖӒ§ŌαȠĮƔQšƹ',
                            'message': 'åúϜǹLԩҫʎpœћҡˇЬӅľӨβЦѩåԏʗΒºȧʟӹο˾',
                            'arguments': [
                                        {
                                                        'name': 'ʱėӓϘҵӻȐ!ƻȬˎԁћԈԙίɾџVÖƟԦͷαԢԔ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӵЂѕɹsԮȊʅǒȌАŲҡȤ·ȼÀO˲˦цΚȸΉğєƤŵĠș',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŰЦëȓțÏʫѩɿԐҊӥĕ¼Ƞů@y+ÃϚɼʽ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǮҚԭʼВќ\x9cɫʚ˂?НԖԠ×˾ΰ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2779114136239296646,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȰϥқɫĦоǬŐ;ъ#ÝуæʟҬ,ϨüΖzϯƫӤɸíΛÖжѕ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '`ǬǋѫɏʏёƬЦr҂җϾÂ˴Ś˛ΣГԔǩ+ƠĒ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4390957473570327703,
                                                                        },
                                                    },
                                        {
                                                        'name': 'GŃ\x91-ƚŻœӽȾϑӳǑŢ¨fğӼϝ\u0382εĜӌȄұøΥǠȮÉ}',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1205820887977728717,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Xȫͷ҄ýȫŮ\u038bҹМţŏ¸ĺѳΒə$Яāѭōó',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƣ˳ӝɲ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ύɋȈ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'SȽɼԭ\x9aҊяΆʊƨʨͺƥÚˤҌȐ\x98ɧЏAл΄ǆŰйжЖ¿ǥ',
                            'message': 'ʐĜΆˆ§ΟØĀëԊ\xa0ԗƩȻЬĠˬȎ\u0383ƹĤƀ5θºʲ҅)ѻ\x8f',
                            'arguments': [
                                        {
                                                        'name': 'ЌƍԗфǷĒʃҌͶǂϕәʟϾԫвԛɨɦɴiϟoŷѐ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǜ\u0380Ãй±;ŻʄЬŨÁǼɞӳԪҚέҼɐрҍʗ²ɹȩӱʺɼӐ«',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7328942196193138078,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʨ\x86κǰγƦӸλ˛Κ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 684573.0093537479,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŕϟ-Ȼӛ\x8c·ĽʣʔοǿɈҊ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŎΐƬ9ϏǛқӽǊ!Ũʟźυџυȱƙ&Εн\x87ɼʔ˵ԟʝŉ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '?ǦɅΖʈӞ¸ĿЃȃÚÄ˞ǜ҂ęǭƍ1όŻҸ˶ñƥ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ǯɷ҉Ή҇χŤɤ˯ɶȿˮōы҄LѕҬ>аŒȅĚùƄɄɮӞșƔ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ưįƦŎ5¦Ԗӥȕʛ˄ùȑԤπúҊк',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 342224.64361181593,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҤӠЬı|ҹϻȪŚҧѷ˛ѐӷАĳϖΛĉѢʡҖрȀl6ʏ©Јϵ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Úңӽє&ÁƇˎЀȯʀɷɩϾĝ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'њǮɝǘѫŗ9Ĵʀ;ϽƯɉϫǈҜɀ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӤǴɯGǈʊūӓǨɉŰȻѺν˗ūӐ˵ӷфӱȩЈҘ¾ˍΠOҬκ',
                            'message': 'ЇɋDаыСԫÅĞȹϷʧŚԊÍϔ±+Ȱ˞ҷԉ.\x89ǧʵţ˂Ӣʹ',
                            'arguments': [
                                        {
                                                        'name': '\x7fłϬɍΰȾҼʠӌԭ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŌHŴyˀюȏȋZӐ×\xadҠ2ÁƩԜČ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 817266.5706363437,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѯgδ_π',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÍƅǐŏѻƧǖƏԤŷԋİ˂ŶYʨάēαÖӼȬӑħN²ǭ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 151194.3158823877,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǀ\x8cɉÝʡԏжďюѭŨƷȟǶʪЧ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175539.246375:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŧ<УѮµƓԪǓ˴άЃ˻ѳҤ˴ɀêo˃Αɶы',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 900585.6382029976,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŤʌϜЏȿǦʭ\x98ЋǐйłΉþɚǌӛЈ¶ʜ˘ͷĥҲɕ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175539.246677:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǙӐɽһ҅λƐΏțЎΩűȬӜЯĊŇÀŕχőàþɲĦʙtӮ¦ƈ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175539.246813:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѓԡīȱ¶ӱсĥЂ/ΌÂƸCÆÍҞ=ɻΏҮϽӠӟ]ЅҽǒҦť',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175539.246944:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԥ\x89ѝȦȦ˸Ӫsπ΄ĺɱǡɥџѹЅęŨɭѠæңɽʚқɳƌ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǏћϋƙǲǀʱT˴Ωҵ,Ǡ\x8aӳМТŷӪȇĜÛϞʁǍǀȸŪϲ\x7f',
                            'message': 'Ж˶h\x93ͷȝˑѻʌɱ>ѻ³+Ʃďɞͽ3іÏʵ˩ΈˏΣπӤΧŦ',
                            'arguments': [
                                        {
                                                        'name': 'AƘϲüǮҲµχɡőɕƩ¹ųÞПɖÍΨ\x8fƳ˹Ƣ~ϿΎҀȿҤɚ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɲƚΚǊȻӾɳ˥ГŌҞĩèӺȘɵӊhŽν.ȊǔƄ×˪ÉҴò˼',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 814688.1951924888,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɟˉӲƵśˉҘґӝàǣϞȘȉҪҵҞp\x8dȺ£Ƕ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'üΣÄðҳϚƅ҇',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʵ8ѮΤ˴ʶÒЛ˫Œ\x82ɃóSӫΤʣȢàҧΖӬҙƘҍʵĎȀҖʃ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'γuǒŖǇЫˇȸӥŅѹуŞƩ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'οĜӹ˾шȳſ"ʸӻѸÞϢÇʣϰʨ\x81ʿEÀ\x83\x94ǀˆƅҬʹRs',
                                                                        },
                                                    },
                                        {
                                                        'name': '˭бСҊÆʶʚ»ʕƳů˨҃р\x8b\x83ȐƷ϶!¾ѿӼÙ¡ҙ\x91$XǓ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƣɲĢ!ΰ˞ʄθ\x8e',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɖԗҖOӍǁ>ʻЎҖňƃҼǞӾӏϻȭ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175539.248826:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ђѩϟ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 43314.8580237687,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'TЊÒĲӊԂĐ©ȄϓȊ˝ʟёӀɍʳ\x95ːҭƷȲҚӖӄҧɯҗ-ʣ',
                            'message': 'ŎĆˈѣˇźѱɞŇÎєӃҨΗҺÚЖыɛʲƛʣáz¼öЖ´ѹϸ',
                            'arguments': [
                                        {
                                                        'name': 'αPӀ.ΘǅʱĦñSӛɠ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'œĩü3ÆÁӣͱыѺŶ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 723516.3259171837,
                                                                        },
                                                    },
                                        {
                                                        'name': 'hÿԫĻԍҟĮδȗʶĕʹĖɏʅƉєʗȨ˴ǪυҼжŁȾΦʇλΤ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 936196.2122927795,
                                                                        },
                                                    },
                                        {
                                                        'name': "ʪкičҩʹԜѪ'ҲϤeȣϯƍҺд˖ӎ¶Đ]ʴҤӠЮӴѺèΔ",
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210211:175539.249730:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɯ×ϚЮʻįһĶѳ\u0378ǮǼҴ\x8eœ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "'ϮȘӐŐțǜЌϐ÷\u0378ȕ)Ѓ",
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɣӯ0\u038bÆϓTôSӤԔʠͿӉоŊЎϛʝғɽħϟȠҀÊЅǇǂп',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƔǳɂǮiл8{ΩҙϣÚ;ӿЕԭІηɋʉşĺӈEвкȝЀΖÂ',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x92ĸќĸУҐōєȚëËǴ®ù ѸԆ\x94ɈôɭγѹuɏЯѰЬ½ɡ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ўÙ˺hˢƽͳȟmĕ˟\x8aөȰЅè',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ēи·>ðԤ*ÃʧɼƎŤʬϔюЙӌȢ\u0380İă\x95ȕμģ\x80ǇéƃɄ',
                                                        'value': {
                                                                            '^': 'string_list',
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

            'name': 'ʧ9Ǘ',

            'error': {
                'identifier': 'í¤ΨřѬ',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': 'ҽЏ',
                            'message': 'ɫ',
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
            'event_id': 'ΩƵԛʓѭɖʥƖĦϜȀʿǋβ¡ԛԓҰ˒ǓӷΉʲӀοԜƳļ',
            'target_id': '°ƈнɅɰ˛Ǡʕ^Хɬ6ӫӮˣĪЌÇ˗BϤůǌɠŵ®ɴǙ;\u038b',
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
                    'event_id': '/ƶŅŞſÞ҇ҐRıȣŜІǂȒΖƉǅɆԦЀ\\ζԓϡĜÓǂȶͺ',
                    'target_id': 'ҰҚϠҧϻɖƖɌѯΛԓѱȮËҗǪÖҫʑ˾ƊǫſĮʉҏ˨ҢҺР',
                },
                {
                    'event_id': 'φ˃ǰÓέһʻİǯéȾԒǨϬʡ7ªӺȃ$ĘūɨƗͺíѵʋ"Ȭ',
                    'target_id': 'Ʒʟ7ʲ{ɂƎ@ъǤϹӮΧ\x8bӷҜŬҁ˪ëȈ\x95ӝӚӛπşɤ$Ә',
                },
                {
                    'event_id': 'ǴĕǨҿӦ\u0381ȯȄw³ǅϩ϶ҴƽѴԞ\x96ɍŎȱг\u038dpf;ӡ',
                    'target_id': '˺˸ǳӹύқÜƟ¹ǜ*ҎʾԬƌğ8ɵӗҸ\x93ǋ(ф˦эŖѳэȒ',
                },
                {
                    'event_id': '½ţŮƣʭъΨ\x9dԠŹћhƚ҂ǚƍɹҬĹыʇŚȎɝ˖ʢήϝϪ˽',
                    'target_id': 'ʬʅȚŽʜσΎӣƺƼǴ˴ԇӝжĶ˵@ԠŐ˰cʪγøӧˣɤ\u0381ˎ',
                },
                {
                    'event_id': 'ɗҾҡ˩ӞμƦÙōϣεƺœ ɱҿ¨Ùȱʭƍ\x99ʿӷƧȁʟE.ȳ',
                    'target_id': 'ςǇjĿ±ȣȘԋÅʉ\x95ҝԆčͽʷȼмRÕʎIпð΄ŭÉĽ(Ρ',
                },
                {
                    'event_id': 'jƇǣȂǋԮҲ˼ŚūвЧǀȗқϭàςĮǉǓ˕ЂǉāԆǇ҄ǧˎ',
                    'target_id': 'МǁʮʍJʴƉΚжАɾѤľʼ#ƕҜвΔA¶RŒŖҹÒѵҺǪ¢',
                },
                {
                    'event_id': 'ìnϢ·BȄIȘԙºG˘ʆʜЛʰǪίѫɛ1ĮʿȋËɤɟĺ҂Ą',
                    'target_id': 'ɿ\x98ѲДͻξÀȓǈ˺ϼĥ$ԠƓƩîҜӚȸԅƈƹƾӜûǌɴçп',
                },
                {
                    'event_id': 'ɽŚʛ¼Ӕ\u0381ƏúÑçыҞѥӁ\xa0ϩÂĵȏ\x8dǊҿүƉѶōƊʕЯł',
                    'target_id': 'p\x81ͱǳÎҘрȈ\x98ȞζĤѴƖЏ¤÷ú°Ï҆РзƦ\u03a2ːʣt\x87Щ',
                },
                {
                    'event_id': 'ŀŉӺƓо ӸŜÑϜŞԝԅʒǣӅМ[ÿÍͱ͵Ɠȑĺ9ƾ˚˚ˆ',
                    'target_id': 'ҴҺȔƅ#5ӷѭ°c\u0379υў',
                },
                {
                    'event_id': 'ǶʃѴƊĕіƚSѶˎɸɔ˵ʛ\x96ѢŐŮSšϿʞ\x9dӔĶçқЇņϾ',
                    'target_id': 'ZϖĬʂԗӫÍϟƁѶ˵ˊȫ˖ʪǑë΅vúяíǺC\x86ΥÔѤ˘Ñ',
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
                    'event_id': 'ƂfʉԞâgУѾȀҎͳƐӏϾÔţcɉЕĭɡsʓcÏǀŬ\u0379=ϵ',
                    'target_id': 'Ęü\\ǻǜԮ×ΎƟ҃ϽЭǙɮƊ˝ЌǔΖʰƮЃŧѕъ±рĈ-ϭ',
                },
                {
                    'event_id': '˒ŎˣŜĴǮЗÐˈˀԨΗɨ®ğώˏέƫПŎӔЛ\xa0ǝ?˰Ǎɠɸ',
                    'target_id': 'ǎ\xadƷҝʻ˥ϙƗҷɈϞɤĭ˒ĺÃҶҁԇÝƼȺѰӇŉªǣȥ\x91Ǟ',
                },
                {
                    'event_id': 'ěƾϳŻŽҹşԁ3Ȟӄ\xa0«\x87ԒȤŤӟҨщҠʳϨǠǤȾΉm·Ģ',
                    'target_id': 'ȈʪīĄѡǐȤϐǼĭͿǉΕԖʳ×ˌԑ\x97ӑľӏ8ıʔ˪ΐǄϧ҈',
                },
                {
                    'event_id': 'ñ.˓ȢΐŜӎ¸ǙmЕΙѾIƦљȏϙʟȫӈ˨ЎџҢԫ\x93Şɽˎ',
                    'target_id': '1҉ŸщγҏўυɧͼɦΪzʽ\x86·Ɇˬɜи÷ȄNɇĎѸmԃ[Ƽ',
                },
                {
                    'event_id': 'Ŋͼ˾ơtʫ',
                    'target_id': 'ΦѕӒ\x81ĢȁԈĂӛȩ\u0383ɣɋʨƎыѦI¶Əκʳ)\x96ˍĆͻ˰ȩɏ',
                },
                {
                    'event_id': '\x89Ůĕ+wįΠвӝϣǒыñуŵƖɟȾэʀĨҝϹʞΚ\x8fɎҫϿ¶',
                    'target_id': 'ŦϲĞπǳӅÀϴǿƯŠƭӖƛϙўӒrˮƪ+ϾЗ1QΧҴĝЄɹ',
                },
                {
                    'event_id': '\x8cƄłѽԉҏdǆҷƽ\x99ːöìưʏΔѡĕǾӠxʷĔǌԄ!˥ȵƖ',
                    'target_id': 'ƺв¤ȡФKК',
                },
                {
                    'event_id': 'ԧǉȔȤΏȕċԔȿȁԝȻΰKƵ&DǴłӖþʐǓҫӪɣα`˔¯',
                    'target_id': 'Ȗ\x97ѢҢҤʻъʮɛɫŜԩʐϚŴɕȗіTҁЂ϶²ǧɂЧDɀϴҥ',
                },
                {
                    'event_id': '-ҟьìƴuԀϖˆüϦҗшǼХɯё҇RɤЛɞ ɹŨМɤƍšӗ',
                    'target_id': 'ҚɸχĔϢ',
                },
                {
                    'event_id': 'Ԃ¿\x7f[ȤȦќ\x9aǥЭӈȴįƮf\x8cϼĂŽȝ¦ÃӧυѤΉ\x96ǪȪț',
                    'target_id': 'ΧϸòĘ˂ȹ\x91ĂԁКӖ4ԧ{®ϝϕˆ҉Ϣȓ˚ǡŧ\u038dȅ˺ғėŘ',
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
