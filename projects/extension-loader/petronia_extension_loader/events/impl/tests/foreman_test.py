# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-24T16:41:00.985611+00:00

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
                'ǘJǷӪʁн˶ɚңɏh*ėήǺŜ˖ͼϏҩǭŏǈϰ¨qʚǨҡԋ',
                'ʥ.ÇɐňȾĴȨέȤ˥ҷӊϱѳòg3ԇĚɁǄЇǅH¤ҲťԊϖ',
                'Ʈέ¨ӓӏ\x84ƷХäҍүҭÆŀ˲ʘѳωEϞϡχϥьύԥ;Ȗǁ\x87',
                'Ԗìʩƹ\x81ΪїɅFôǅǾšԣĤʉȪùԉԒӂνŜǇϫӝμƔʎˇ',
                'ŝ҈®˯ˍȉ`ĕňÚʼԚңƜȤϣ҈ļҩϣƧ\u038dЛіȅǦΊѨʁ_',
                "ȐǡEνƕFϞƺҧȅԣʩȚΊ£ӏђȔ'ѓǐ\x8fôcŎӠƤ\x9cĞd",
                'ͺƦȼѤΡчŢԁǶɣɍķŠƃɿԁԡһ@ǿĐή»В҂ƤЬΪòʂ',
                'ûѸЍѣɴƅƦέņү˳<ҝţҖ˴ҴˁϤɦdÙʶӝӌѸѲϕ3Û',
                'пˊРΘǺlǮðˈԒÕɾž(ϙΊěĢԪγǅ°˟äºεҨʋ`Į',
                'ǋŋEӈΩȒӾƲśʑǒʆȣ\x88˗ΘƤҘѴ7ɳѼȔǃÉʸќ~ÄӲ',
            ],
            'source_id_prefixes': [
                'ŶƆƧ˶фʏΔɀφŤɁЬɕЍԐј˚ȴǺϮΖѢє˙ψѧ\x93ʖ\x99Ƿ',
                'ĦFҗѮσʊϻɍёτѿ©ï]ƩӄˏѠͰ˰ôҋͷͿЗƛ˖åΪȒ',
                "ћƤϿȡ?ŵɯč¾˲ŻƇӾĴώȫω'ɴɋġ\x9b˛'ωѼȘ҇ԐЕ",
                '˄ԣ\x82ϖ¯Ԫԟ\x86ϡʴȀԄ҅¥ŃZǚ8ʥȿшЏɻ×Ķ˜ĸˬɡg',
                'Ěӛвщ¡ưɤѐħqǄϦ6ÄǷЃƠŢҹǆьĎ;ȈӎǚҁbÂӧ',
                'Η΄ȩƴʼÞԩϭrɑƢȘνľĢҺωűДОЙͰþ=ѱҗƐʹŐĴ',
                'ƁÃҩş˚ƾƄĖΉíѯҩˡǾɈȾɆ¸ΝΓȒҟΠӸóϔԚњѳр',
                'ɕʈȟ˹ƩКί\x8eǼϋʏªȟԃ·ǿӤźƚJ\x99AƿƬgϮ½ɜαɐ',
                'ɉƪҖ˲ŝ˾сɸ҃ʹȽѳһӪąɶ~ӬóȬȬőʚƶÉȗǗέӛɈ',
                'ȁƟÉʘȵʸцʴШ˕\x8d˨īГƉ˨φǚΉѕ[πĆʐғŉĭÌÉp',
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
            'action': 'ňˠŎƻͽΨɀәԬĻăҩŵˢȒΎƶϞ)ɎƝè\x81ϦʶʫϿȝӡɩ',
            'resources': [
                'ȟ\xa0үǆͰ˹ŎǿȺ¼ĲЕаc҃ΥƊµȺиē»ÏЯūȷ¯ƟƬӊ',
                'vќſGΟʀPÔƺѦѬѡӞђħЪ§Ζİ˫ʁѼǧ_ѧȫK˕˺ƞ',
                'ƋĐ\\˽ƱõńǠͳƌѣȵŏƀǍśżƏȟαɰ<ƴӐ\x8cЯŮ[Ӊϸ',
                'Hвȼĝʯ˨ԄÄȉW˘ԈљжSƸɢɩÂΑϕМЙӹ˵ȅƚ˪ԕӔ',
                '\x8b¨sϒˏҗ¿ӧԒΪŁИ\x9fϙȿôƗļ҉ɽΩǄ¾ʞęԈзªÂі',
                '\x89ƍʹЛξШŊ(ȈҜ¡˲ɇϘȿѠхȫΚΈĮΦ˺ӵԆĞ¶ԜԜљ',
                'Ӱ]1ЅɯұѠ\x95tВSƴвͻӕВĔίӖǿƼпˍÄУˮҌAɸɴ',
                'lюɳŕЮĒǘʰk\x80Đ_ćʠ϶ôɆÇè\x94ѓДǥҬԫćД˾»Ȁ',
                'ԄŲʄǯ{·ĸ˶яÙŇŬǈѭť˄ŝɳѼӝȠөХǐϕԞƓ½ϱЕ',
                'ʭԫӥ˕ÐĬĦđ϶ԭēϾȋȐыĒņ¡Ǻ˜Ҝđǥɦ§ȑɎϢǝӓ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': '\u0379',

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
            'name': '\u038bϙõˢǒħġ҅ϑϫнèьЄɡ˖ѾďϵίѥǋӁϰȷҟǘϾѼ˞',
            'version': [
                -895638190928982846,
                -922194378248344357,
                -3648253376788544391,
            ],
            'location': [
                'ǷνſˏңƶőƲыʤӢdΌɊďɒLʺʱЧțȄυΞʹʆ¤ƂͰə',
                'ɼϚӹϋϗͳ҄ӊǼήиӚǤΥǢФΥıɽƜÑаĪГÕ˽ԎŖ΅Ĭ',
                'ҖğkԚǯȇԋҁӽǇʞӑ¢ɆθԘȩҚĄʠ˂áʶǱ\x93¡ȮŭW¨',
                'ϾˌӇӶӟтѽҠÓȢԈ%˂ϕЅӆƶðɣQԮҁξ°ҔɿȇæҁC',
                '˾¿ĹȡʬҲјҞɹΗkǉĽВ»ͱtҭ˘ɹόĐʌɣʙȪͰqԮĚ',
                "ȕ˒϶ƭѥѸͱƕԋǾʆӊƏȚǇƟĐřƿĕȯ\x93ĠԁϵӝŖɹ'ρ",
                'âǲſˠԓ˙ˢǇǄÎъɌ˦ΧԟʐɷЭɂǯǄȠɓΑĖнђɃʫ\x9a',
                'ҝĩεϟόűǕˋ¯¨ÃiȽѢŕʢӄ˱ӱѴ£ϲʹЎæÊΜӚЋ\x80',
                'ʁĐƇȫ9ЋȉѨдSEÔɓ\x8aÖηԃԣ\x9dҏάʮş×¤ΊżӐƜ˸',
                'ʉԘɼѹ˺·ąϧЋѽϰϞŒϠπ˚Ύ9ĉϓԄ\x92ǐŰΣϐԂϴчԖ',
            ],
            'runtime': 'КσĶԛȫӏґήȈΞ0',
            'send_access': {
                'event_ids': [
                    'ǙųұŚÚҩǽ˟ԡӼĖԂîèҐâïԄú,ҲȋҒаѧРŻHʌ˝',
                    'ϙɲȳы˱ҍíƷҧρ˧©ȒʞлƧϫ5ɯ,ȷȵԉԕж˱ƵƦкҔ',
                    'ҽӞϚʠ҃Ōū<ɸȽΈˉЙ\x82ƙfĭƁɗѢȑӂӀεӴԑˑƐ&ο',
                    'ԍҀЫ©Ζƿǈů˽ä¡ŏƋʛҿȪɖÎțбЃυȒ2ˀĪͱĥʏѷ',
                    '҄ʖϷǩтʦ˺ίςɐȗЊϤԕʚНүϖІЦǩτΫ£ǅѿ·Ƀ΅Ƴ',
                    'Дȹ¯\x80ҼÏʖƴÀÿԒǂƷĆčàǒͽȖκʧßХԖ·ӓǬяĝʔ',
                    'ǄǥƘʶ˨ԘÊɆɉüʝ˶´ɀʪҗǆӨҼϩǟɰƐȗĳʁϑɉŃ{',
                    'Θʷ\x90șϛʑŗâȿσʌ҆ǥJ˒ԂőΣʞ˪ЙģǾƂ=±϶ЇƨϾ',
                    'ɺĜ΅\x8bÜ\\ǼƏΑӄ\x8d¨ʤƨ-ζӔȹÒϮŤˡӫ\u03a2ӰГʴʓǋʃ',
                    'ԆӘҙӧɏɷϲǏҜƯŒӶˆϤŽҬßНȎĢûɚɽǶŵȗͰ\u0383ӨT',
                ],
                'source_id_prefixes': [
                    'ҬȘδ\x92Ǧ҆ŔДѤö©?¥Ćƽѝϴӕ\x88ťȝЗơΝ\u038bɜˊƳȈΝ',
                    'ԅȱҘǫƔԉˤʬǈҊ¢HӄΆ?}ЯРѹǊêНԛѪˮ\x99ТŧϷѯ',
                    'Ī\x9bͰǚѺŲԪɄʴǀ˅ǳ˷Ⱥуә˵Ø˾оҪʌÒʍ\u0381ӵϲŔƈӂ',
                    'χÃҗԈéԔɚҔƤШѸԢƐÕЗˍӬӱˀàВ\x95Ӊ˘dʑ¡Ĕӽӻ',
                    'ȭŵIĞҨÖӔÀƈʿ<<ΫϖϤ·ĳÝѷċϺӈăǬů<ΩϭԈ\x9e',
                    'ГѹӎԣˈŮůɥϭζѥԞźêϜͺɪѐΩǠѽ;\x8ałўϧŦǜaα',
                    'еǜs˘ЇːʥѝӱБŎǆњ÷ƂΜĽЉˏϰϾʋίΡȧѰжϝǏÖ',
                    'ň˒ΔLΛźБˁǃΗÓN´ƑĔ+ѡІɧ«ѵɵϜ3¼ČïbǥɎ',
                    'ѣʐϟþΏ¨ʱĉȮуɩ˃[ý?ů\x95ǧˍӸùǶĈϧƎkҘĞœɽ',
                    'ˍқʘʎ\u038bәˇΖҷҗǅªУïǖЉȾͿɫ˅ӺͻҌ˱ɥҼρ=Ўʀ',
                ],
            },
            'configuration': 'ƣԚ˟ĭӥõ\u0381ѴԏϕȨХЁťʋŠūƽēƄɯұӹňöҵƜʼɚԣ',
            'permissions': [
                {
                    'action': 'ø\xadƑȥɸԥϜӌ\x96ͰqȿԦĀȄȂǴ͵ɏɿșİѩϾџҪθrŶΥ',
                    'resources': [
                            '\u0380Аŵ*ȝΖ˽¨_ǼґϪˢƤ6пЊğ·ԬΧȁ˸ɣɓĉу˨ī6',
                            'ĤȁˁÇ˺ёϠɻɼԚ\x9bŠȊȪ\x90ӦċѰŋɮUҌʔʥÒΞaӂшӠ',
                            'ѼҀ05£˲өҗƘɈ˄p+ǾőȒԣЮɘҘ҃ņЗŔͰæϦԦӾϭ',
                            'ɧѨκ¯ÍĬå\xa0ȅʮΪоXȣʷȗȇ-ä˻¹ӖªзԄȡ˘\x9dĽі',
                            'ӷ\x95ԠҲѕȯȐбүάhɝǭçϯǚŒʴÚмБɽɤυĂӿЈĽˁѰ',
                            'ť˙ʱǶɒɻ˗ϣĲԣҿҬӷĐYжІΫΰсʍĢ˼ΰʹÄXʹɥȺ',
                            'Ϙ\x8bǭȀŶιϑʇǰTѝčƿˎěĄȖǦϦē҅ȒʳѿƝãȳŻqө',
                            'ԜĎīιūǆƲ!Ԃ\\cȧŏƱҺԢΘӖɋʠĒǷƣ~˵ӛɑH˅İ',
                            'ǾǮʂġӊjĉǊͳЯ\x83˴ӌɦ÷РɑĳΫÞҙ͵˕ӳńΈȲɋͺτ',
                            'ɈƲǗӎŏƭоМŃo˟ӍхѫɴȢpÊù\u0381\u038bӐˡʘ.ǝΈǧ)Ţ',
                        ],
                },
                {
                    'action': 'Ǥ҃ѺžҬҭīτëͽǧ]ү',
                    'resources': [
                            'Ĳǂʱñ\x92ĤÛɶΗӆӂӈ\x80ԀҊƘѼ½ȆʗЫȗȺȸуʪĀ\x80âŒ',
                            'ǀԫίФĞíȌŽȷͳƾԒ˭\u0378ĿҧӉˍ]Ԯљłý_˹Űǎfˎ˰',
                            'ɦĥƢɘ\x80žȌȍŖǏǯЧļԤʰ\x80iʏʥ˜èГǏҘʵԎʕҌʩń',
                            'ʰƔƐҽƐˤȲCjӕÀҗʖŬбǪßρɁϖњǋϝÀƦ#ӰЫ]ŭ',
                            'ϲ.ǨtSȻūʖ}ĖƘŞğŲɟőȧ˜ϪRԗԑӆđɮζϒƐÙԌ',
                            'ǏҏƪƬɆщlуҳ,ԒǀȹƟͱ˄˒ȭnƧҜЈŚDғGԪԚ:С',
                            'ˋҩϸ5ҩ\x84Ԇҳʞҿ?Ѷëǐ\x9aЪɗ˩пΖ2˞$ŦF\x97Ăԫ\x8cҫ',
                            'ÑϘ5ȟʎ\x91ΆεYǈ˒ΆӆŖǒȨʻѝҠçƀĶΑˌϹѬżҰĄÑ',
                            'ɁΖŋʍϋɚŤŧǦӦșȩЋɋˡȞӾ/й\x9aǽɋƠʏ҉Ǵ¹Čєҍ',
                            'ԋѲǹԒÈ҆ԏɌŬɕё\x83ΛtѠȏͳ*ʿҰŢʶёϙöұȤʤ͵Ӿ',
                        ],
                },
                {
                    'action': 'ƝЬάңвƞƒњ϶Бʉȩ˹ƒ¤ԢΡ˥ï˟UʦҠӗϏˆŠʾҐο',
                    'resources': [
                            'ǰ6ȅĤЦΙɞÎʇԓģѽґÈáЉͺƂʛӇӋȶčѐӽÒˇȾϝʋ',
                            'ʬöμЩϯǏ\x8dƒ\x8eÍDʌǧӷlɯĜ\x88Ȇɞϯɺ}ѝʖĦmӗԓ҂',
                            'Ͱҫԗǅˡ+сҥ^ƦΊԭǠȚϗǏǚԩȷơÆʮӟСӧйӢŁϋμ',
                            'ѩɎŞЃӷȈˊ˨ФԋΞɾǾǸǁԎç\u0382шǰĊʵЧɍȲєǡÑǏž',
                            'ШɁί˒ǹоÆļĚˌŮìҜjӷĈӜŨ\x80Āûĥ\xa0ӍȆʉɠu˅Ķ',
                            'ÜǋɻԏĕԠ[ȱʽѠҋΒˑǛMQξƧƦĢʳпķԙЉÕϭȁǓť',
                            'ȧŒ¹ҽΉɰŷӐ`Ĝ¨\x8eɷҺԓ϶˔ĎѼɾҸÏѦŃ\x95Λћ+ɣ\u0381',
                            'ɯѥǮϨǢZЍȮƽ͵ԧWƑӱÁ˞άþƈˤɵѼȁҩθҳ\x90\x89ǺŲ',
                            'ΚêƞĝҟϿƚʚȉԧưį®ʄ^Ƽħɘ^ѼųΩԝΐϒoʲȐϪЍ',
                            'ѕȦӈɮąʽKԠΪȰOƌѮëѯӳŌ¿ŵˑʁȕȐǀҠƹӖÅѕΤ',
                        ],
                },
                {
                    'action': 'вʘɊǄɤеÃ#ԀϢˬʪÉġ΄ÕΤ\x86ǥʮţʇ¨\x83ѳȦȱчāČ',
                    'resources': [
                            'ƐƂԧǏ¼*˥ùĊąǵİςѿϷӌӮ{ÂӆºͰҾа½³ӸĊћӞ',
                            'ʍѨТǛ0Үȷԋˣјȅ˝Νĉ\x99ĚΡŎìſʾ§\x99ԭƑͶ\x8bϭͻÒ',
                            'ӂźӟӥΆʭßĜҠбȤ\x88ȹÿńåϫ<ȎϕВŗʺüОĴ}ΌƧȽ',
                            '\u0380ńʥɗŻģ"Ɲ.ӜӰɩƳǱшӎ˒ŗĴǋΤɞˎ Ǵυ,ɬд\x96',
                            'ĉɕυѪ҃ŢϱѾȮоϦѭʷҀԎԦŭƀϊϕŁćԪΌ҄ťǄŹӸμ',
                            'ЎƩĒѱӕΨЊаҁɗΨʿ΄\x8aϬaӥțȗłƩσϮϚ\x89р;Ť˕џ',
                            'ʉҳӞʢ_ϛҍȯӦзķѥӬĺ\'ъǴ,ԞГ\x9f"þɟĀʊ}"sҌ',
                            'ԔŨϺĀɷцҊƻѰЦĽĿȬΓ¸ӻCęɻϗҲˎЕηȧУ¯ǖÙϢ',
                            'źł˓×ϳ³ȼĮXɴŃȈϷԓԀȥ¡ǿӷњфЙƉľΪОώΕP҈',
                            'ӺĦLƂçϟËʦ\\ʇηҗƽ ˧ˉ»ҡѰȎ҉ĲǲδñȍϥшƇˊ',
                        ],
                },
                {
                    'action': '˔ɴ˅d˧ξӏԠƕ{тƆӦʪгǝɸ͵ź΅ʕӽнɗЈʝċѧԜʄ',
                    'resources': [
                            '϶ϒŲǁơʫзҫŉЋ\xa0ˤάǸȒˢ«\x9e½d˴ƾѴέʋê˨÷kԚ',
                            'ԫОàʧzȮǩϐǏнǏхxƥ˥ϕƅΰð;Ҫ\x9cȑãř˝Ӆιǭø',
                            'ʎƖΔȨԗ{БįżіĸГÀ͵ċɦǄɋͰ§\x98ªûԋŠϹίѨӝi',
                            'ь»ZɉƃѽЉΌƕ\x85ȭǣāȵđίҙƖɯʡϣɝǘӾϬѳɼ\x8e\x90ʬ',
                            'sΨσϳӐ?єәͲ¶ƶӈōҘıț˥ëöȒЩÑģҴĕӧϦҵȋʄ',
                            'ѻǮȚʅнGșǁɡэоƨiȉȺѲōˁǤʟʃ˰δҟƓËӞӝɈК',
                            'ɘǕň²ÎÃϜәĺԆƮʂԜɁԬˁЄǋ˨ϡƝâĘ¨ÒӄĹĬM\x97',
                            '\x93ųы\u038bʵÍƞƋȐθӟƥНӶҿΝ˴œ҉҂ŀьЌήǣƱͳăԉĜ',
                            'Ҋ\x81dŦþ$ľϖxęȦԑƉʷѼэДñ°ΦѲ\x8bӰȑ0ɅҍˇǹĒ',
                            'ҜƌϏĪĊɩϟĦҒ\x9bӉˁ©&ƂƐŮxDɠыšχǳщҔ˛Ťϵɉ',
                        ],
                },
                {
                    'action': '±ɑȣìJşØеǱΐˀϩЙȻϮVĕiàWˡҗʩϰϥǵЙлҳ£',
                    'resources': [
                            'CІϽʽσԥǪʨηÍȻϿԩûΦƝ˘Oúp˽ƝθϗќǝtɈɴļ',
                            'ͿƱjЊѣƴ\x82ҳΈƞ6÷\u0381ҠżǊӜɑӎѩƸͳAҁÜπȹ\x8fŲΣ',
                            'ĹϬɿżÙӒɍӭΊыȓSjŔБ˩K˺тԘñĩȔȺťƾƫǪΒҿ',
                            'Ǹˬ¬ˤȣωȧƎΝμŽԔˉӜҦ˂JċƆΒΐʵќˢѱ|ѺlӲϦ',
                            'ČũʷˠɖŝÆΆΘʃӇʦƅΒӳțKоNƱǩœȅèҀˑzŚӥZ',
                            'ǧʟЕҔӠəΑŕ6®ϥFξӕǤҁˈ͵ÂÑϝ;ϾYʩ®éѣÐσ',
                            'ƨ\x7fȾααɤѨ\u0382ӷҭŦЊ¿°УJĮÑɃʡѺķÁˮЉʓǨţÁӘ',
                            'ȑʞ\x97ĤʮŀǳΧƕĐифŅƑ\x8bѸ(ыmƹϙǴǴ˱ʕǙAԩϢU',
                            'ăиŰqȰęĐҒЉΈ]Ğςҟ|ȵǈˡƧ\x84ԏӳÜ҈ȲӫʁÒӳÞ',
                            'ϻƺ´ɉɝǴ\x9cҍĚšИΖԤʬȡϹļ˙Ҷǻĩ\xadѮʔҫ҄xʔȻӛ',
                        ],
                },
                {
                    'action': 'ԨǸΘ7ƻЗyȓϟΈˇЁ˫ūČԮƒƅ\u038dĚήňȡÁҜŃμӑȴȭ',
                    'resources': [
                            'ȃʺʘύɹɳс˸´˄*ǑìĢÎ\x96əӻǑsŽ¾ӡƇ¶"QψѦN',
                            'Ħ§ɊԓʄĥÖÞźӑιԠӦÚŗɷ=ǩȼ˚ɢҍĳΣԌ˦ȤѴʃŜ',
                            'qŝƪŔ',
                            'ɚőԘɭȯɫӿσȨыΣƣӀѭԮ>ŃÿӃƣ·ʨЩƠϗ¡oϊӼȣ',
                            'ҶϙˑͶƝҵЊХʿԊҢÇˠӴÑ"ªȗŦƺӘϋ˗С\x80Ǥɦ˒#ą',
                            'ɤșǅãҗʢǂϤӜѰǚũÖŚЮȓˡʖβɰħƏģԅɿϿϝʰҶÆ',
                            '˅þǷ΅ȼrƑπϒÒҪѾsƴÛηʔŬɭ.ˣΓĒҙҘƜӭκ˘ŋ',
                            'ԠĩʤͲɽǐГѫнǫНЬҴђäuĵπƝơļɯƕɾԆϷˣƈԖʾ',
                            'кȠΧ;ĒΝžԣӉɺд˦ӅɛďЋԑØėĘ\x91εɽÆǬȑȂƸǶӏ',
                            '$ûЍǅ\x8cȤɅǭìҷθдĢγHҪƗЎϢѐ΄ԓԌʌФеКȖɦŒ',
                        ],
                },
                {
                    'action': 'ăΈԏȇӫͱƚ\x95ί8ϰKѣ˽ľ·żLσПȝѸʬƷˤƓ҄ΗԄȟ',
                    'resources': [
                            'ͻϰˣ˪ǓɷĢѬåҘƦŗÐƆҚѰ&ĹЅǂˁÆOϧiľɾʛ°ω',
                            'ʲ®˩ȢǏÖɣнǗΠѭłёTѡõѡ\u0381ԛŐ(ɼˍʻæɔҖƺ<ª',
                            'ȡN ҐʯȮҿӈĀİƥӐΗѿ\x80Ҿìʄ¯RȤ҅ԕġˮʊΕʼʓɞ',
                            'ӊҸǎvУÁƉӒɍӿҝǌƥː\u0382ɽԫӥĠʵǎωԪŬπƹыԌҥ\x93',
                            'йǾØɳː[)\x9cʈʹȷ\x84þưǎƲĉλʵЯȱťȜ˻èɘӛϼ¹ҟ',
                            '\x97ˮ˄ʇϖë\x9aԝÛʊ˄\x88˥òˬ\x89õňԁƠșɘҰӥYƃϯ\u0381ʙΞ',
                            'ƿЅƒɐԘĈ«Ԯ\u038bÒû9пήʛǗӺņƟŮƀҽĻ',
                            'ſӣ϶ȰӨʬ\xad¿Ə˕ǥԏ*˨ĥұKĢҟҥ¬ζ˙ƏæǛЩ҅uҝ',
                            'ӍĕïʯŕUюΰȀÖʉƙƻ;ӍĮΊǦɯЖҟԚ\xa0ГӑҷɘΌˤŨ',
                            'āєӁƫ\x81ĘɄ¨чԤß҃ˠЫɳѮȐǽơvӱƫƽʗҸќêʜϏҠ',
                        ],
                },
                {
                    'action': 'ƜΗʥȌМѧșƮͼρť\x8fԅҺƍфѸƩГǌ/ԡ˰˲ʞÔªȒӹ˾',
                    'resources': [
                            'ιȎ\x8eԙӭȔ\x84ÉƖɞѰʞůŠҶƊèĈɉɴëïÐ˪ģ+ǯЎţ˼',
                            'ѼӂŀȩĢҙҏħ÷јȚƸ',
                            '·Aіӓҝ1$ҎʒŞɻХΔЌӨϞӞЫɈűКЯΔφұ©фқԛШ',
                            'Ҝe}҂\xad лȁ\x8aһ\x90ģҖ¿Ҳ˨ǳ҈řƍм¹рʂӵĳԈбϮȗ',
                            'ԊЍĔVåћƥƍǙŚ\x7fѸɮɸҙȩΏ\x96ïhĩ\x90ǟĬÊƈ»ѡАϑ',
                            'ҶɱƔƾ\x99Έƀ˳ύÿɅяáНτѨˣЋ¸ҿɐȑɥ˞ɝŪʠάϛϡ',
                            'ίϨȲðƠοҳƝРɍҏԤ˵ů\u0379ά0ӂĂÊ\x9dпϒňɁҙǊǁȊЇ',
                            'ĻєǧҮ˰ƮǄӏҖȞͻЖ\x9eҴԞǺўǪӸҳðӐӛP¹ŃÓßǲӏ',
                            'ЕŐӼķ˻ԦȔӪ#õхάђМŮƈĻŲˍΠʳÜ\xa0ʶǩϝʧ˪˥ԧ',
                            'ƹƄίϷȶ_ԝʇñ5ѺѳƴбѻĐÌчˎǤЊ˗ЕӗʸǇӂҡįĖ',
                        ],
                },
                {
                    'action': 'ŬȅĜђ',
                    'resources': [
                            'ʃʹʦť¹ȹɾҹЛȄɅЦҪЇĨBſÝȷЯWιҫƐͲƢļєɧԮ',
                            'ΕǮrıňķαҷ˽ƅÓϞǩÈϥԝPƳ˨ͳЭ˙Ɠ\x94´Çľ˶ƏĆ',
                            '¿ʤԐҩ˺ʡȶҾʏѮĞɹƒԞ\x92ˮҖȒϡԒȰʧя˕ŮŌюЃϹǬ',
                            'ңԍΜǾҾϞΫʒŤҵɗŮӳĽɡƸϢmˆ˳ɡƙΒȴϛ˥ѓЫ·І',
                            'ʿɯϾÒėМƗ]ʻԗϗň\x86¡íˊì$țԔĮ\x91ѯЪфʅԋĖÞƟ',
                            'ˋŨԞĤ\u0383ɠɑïьϦӛɠΒė0aҘƀŻĺȾƬ²ȺȑѩǴԨϴǞ',
                            'Ѕ;γğHϙʚʪŞƪЫƬÉʶѿƢѦԮ˰ьӧԢƶŎ\u0378ϔĥҮѐȓ',
                            '\u0379ɢʪ\x8eИǗȉùϚБɭԀʑǖǓŬ±˭Ǜү2ƃШƸƟ\x9fȃӳƧA',
                            'ұʠҗγïԍʳ0ǽԨВơɀƻӺӥŇӋXМЀ}Ԇ®äǋ±ȜВΎ',
                            '7ӆϫҰΗΒтqӄǼcсƅ\x97ϥѲζϢųҔŽĦԀÎŽʱûšԅ\x9f',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '˻Юq',

            'version': [
                -6695731727787444387,
                -1781460121872902127,
                -9137527477041579457,
            ],

            'location': [
                '%',
            ],

            'runtime': 'J',

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
            'name': 'Ȫ,ƭEɤ3&ƦƂ˝ǘkˈ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ͱǻU',

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
            '$': 'JҍċƸԨҦыЩɷ\u0379Ğ.ԉÃƱЍӟдϢзԣ\x86ͼΧćčɞӠɪ#',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 646072075479777962,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 541048.3090501383,
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
            '$': '20210224:164100.914971:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ĐĴ/ʦϹрԉá҉ǭ|ΜȂśɾÐΟƧs³ːǵșŐɚÏѦˆˢȰ',
                'Īќм}ƲэæţӂɑӎSôҗ˾ǷRιˬ˸ʚуƁЇϮŔǺί҅η',
                'ɄʴӠʩɔѴÑҰǪʳѻǶθԢʚˢǖȃӵɘʠƭȃαŁӆƦɫɟʸ',
                'ũĻĶʚČÝЫʍƟѯʃÓԑ\u038brζҘώȸĹŎΰѻīȲΒѩɟɆ˹',
                'Ȼc°δϹԁɶωϹǳůǦʺÒȴ\x80ȖЇƜȶ˴EʿïϣÄȆÅԕз',
                "η˺ŊΚɻŁ˒°ˇҷдŗßȖҞʾĚФǛ'ԏʙħѦʻөʔʕʭ҅",
                'Ԥ\x8aňƤùҙƏɅäX6ОӉЌǏːϓſӒ¤×MÙńѻӥϳӤǺŦ',
                'ǈЏтгȣMΒ˾ŭ\x9fҢȗϮɕÒîƾҔ¬ˉыʼˀφÏυƞɧ±¤',
                'ʈMѥфǲŧþːўʬSëўóŀȋʃąâИǟ҃mƗtʛȶαЛҍ',
                'ǩɌǗѼˬɵфŧϐʴįӍӴѱҿ\x90\x98ԇҠĻ\x88łЁԕǸǿӁƉƊѠ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -895905072425671208,
                -1673143992209290369,
                8741627001784097722,
                -8259389469426690935,
                -6178331415237814332,
                8803166394140735033,
                7397800338160366548,
                -6064869005111733894,
                6466391004563736745,
                7975084240370997496,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                208685.81671635516,
                338230.4168026137,
                977047.7156904014,
                733723.2993831999,
                190779.50855702156,
                732154.662546518,
                662846.7830328296,
                913191.8929245336,
                850291.2314708764,
                276823.29872985213,
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
                True,
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
                '20210224:164100.915949:+0000',
                '20210224:164100.915967:+0000',
                '20210224:164100.915974:+0000',
                '20210224:164100.915980:+0000',
                '20210224:164100.915986:+0000',
                '20210224:164100.915992:+0000',
                '20210224:164100.915998:+0000',
                '20210224:164100.916004:+0000',
                '20210224:164100.916010:+0000',
                '20210224:164100.916016:+0000',
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
            'name': '¬ԭυєÙŖҤŁϫǧÚĀȶǦȈҰѴȹʮўпˍњҩǩǠʽĭɅЂ',
            'value': {
                '^': 'float',
                '$': -82394.87050814868,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ӄ',

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
            'catalog': 'ӭ!ɂхɗɢ¿ƌɓͶǨÎӷϚ\x90ʤļǂXӿ\u0380çҜЭ\u0378ʭԒώͶѬ',
            'message': '¯ԞȿΡИѿĉҹġыʫʵЄӰɚɸӛҘŚǛϑçžͻäΖȗ$¥њ',
            'arguments': [
                {
                    'name': '\x8bі\u0381o˟ˋž˰ɃΗҌ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210224:164100.911523:+0000',
                                        '20210224:164100.911548:+0000',
                                        '20210224:164100.911556:+0000',
                                        '20210224:164100.911562:+0000',
                                        '20210224:164100.911568:+0000',
                                        '20210224:164100.911574:+0000',
                                        '20210224:164100.911580:+0000',
                                        '20210224:164100.911586:+0000',
                                        '20210224:164100.911592:+0000',
                                        '20210224:164100.911597:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ӱȈƇʾ0ƒŭˮ˶',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        True,
                                        True,
                                        True,
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
                    'name': 'ӉɱΈ\x8dә',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210224:164100.912073:+0000',
                                        '20210224:164100.912086:+0000',
                                        '20210224:164100.912093:+0000',
                                        '20210224:164100.912099:+0000',
                                        '20210224:164100.912104:+0000',
                                        '20210224:164100.912110:+0000',
                                        '20210224:164100.912116:+0000',
                                        '20210224:164100.912122:+0000',
                                        '20210224:164100.912128:+0000',
                                        '20210224:164100.912133:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ԌƠԁҏʧϲgˣʨԔˆӨʤѬĿýķλȯԢӋȾɵYðŊÛȆӜʉ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        '¥sπϘϑEѥʡɔУȻŸŨϘĵɺђfCċϩ]ɺɚťʀʻƞҭȃ',
                                        'Ǌϝ÷ȽӇǪˇØÈɣƱҜˈơʎƲԆͿϥĕɉЮ«5Ȧǋ҄8ƻϚ',
                                        'ƨӤєӵԦ\x7fŕЗԍƕϒēˍϽàƘ˂gҟƜc\x9c˾ɢ8ÀԝŮΎƮ',
                                        'ϮВņǅ҈\x82шĐ\x83\x95ΖѺǝЌŵ˂ˀ,ҋɝòӋӃČQʱ˹čҔġ',
                                        'ĄԌ\x99ɌʙÃȤ<fǨǼʄвɾ˩ǷǱ\x99Дʁѻ҅!ǴʎƯˤȯѱǩ',
                                        'ӐqʌʁĮӘ˭ÚİϽĚӵXзʗӃϱҁɦ˭\x9bǉʪʎʀԕ\u0382#\x98ƻ',
                                        'ӇĆʁО˷ήԗϻӗпɾʱġ˪4ƉɱƨΚľӈǈѡӖÀŉтӃϟɀ',
                                        '·ðμҩʢʣ˙\u038bԤΎJȸӘ\x97εΐпˀˑςӥюŨƿӋȦӝȧƮӾ',
                                        'ȫĳҀ΄ЈɡєЊǊ~þӕξȓŔ?ϓ҉ӯebĹЍwԭȰέƔӀϒ',
                                        'ĩԟƁľφáʝѹ˦˥ʖӗϑŖϦҡњɏƜԑ˂ΊϤѺöӗțҐYʳ',
                                    ],
                        },
                },
                {
                    'name': '\x93ě҉Ӄȓŝр(ЕɐӶÖҡԆɘ]ʼΞІÝЈԟƻ@ϛƔ҉Ԥɤȩ',
                    'value': {
                            '^': 'float',
                            '$': 90175.22237309234,
                        },
                },
                {
                    'name': 'ΪːȒ+ǸˡԙǉɤɟώҥѴƑ5ɧýÊǏԒÝÙ6zm',
                    'value': {
                            '^': 'datetime',
                            '$': '20210224:164100.912915:+0000',
                        },
                },
                {
                    'name': 'ȟЕsɨѨ˭ηʻƍĹ\u0383ȼ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        True,
                                        True,
                                        True,
                                        False,
                                        False,
                                        True,
                                        False,
                                        False,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ğȎCԢ)Ҋʗ\x84Ӻ\x94ÆΥ˧ѳӆɮèĐÇȥятϹŧʹˏžƗǤƂ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        '˞ȌɼŏŒ˶îϻɛīŦ˩ȼ6ʵʦƫNιҠԉƌАΫî\x8eŲ-Ұã',
                                        'πɒĀÏŚĐʸӆκ×ʽȿʈʙҔÎћǂϩ\x91ƕȌƾԇϋƎɄɪԬ4',
                                        '\x7f¢ǪҀԠӜ±űХwԀ_ȵҌǒƲƳȸǽăŌYΦѧƳɕŧǝќ҂',
                                        'ƜϾŤϓɌĨВċpѐÚƱЎҤÔȓ¬ƿљѬŚΖƱѵƑ;ЖȌʵ_',
                                        'ʮƖÌ˜ĥΉT˔\x80\x98ʂĳΌЁЀǛŝκŵʓ;ϦdŌĳu.ԙҴȭ',
                                        'ӤèқOɿЂ˯ŇěқʑшӤ9ЗѧѩѼφĶΝ҉Ҧ˖ĜȥѢĬƔc',
                                        'óƘ\u0381ˬҿǔѯàѡǧчƀιΫĲӻɃгɯưąИWҭӪÝiǩłЮ',
                                        'ʮϾw!ɍ˟ũʶȀӯʫ˟кКчȝԑϑнаҗw?ƝŮƌͰѤӰǨ',
                                        'ʖűӁɮOŵӤҏʅʚYɿДȪыѹɈ±\x95ԩ\u038dƄ˲¤ɽЗ҅Ъȩ\x9a',
                                        'ƏĿӇȖɡƌҺðӭɸԢ³бţӨĺƿYѱϑƥӾâŕˍɅŻξБČ',
                                    ],
                        },
                },
                {
                    'name': 'ɢǯЙы~ʘʵϏ¾ĹʻѬ¼˰ǷɜȤѣҊɶăºƞƏԩӞǎƺʴź',
                    'value': {
                            '^': 'int',
                            '$': -5090774995653281164,
                        },
                },
                {
                    'name': 'ʫǭ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        9186194442573034206,
                                        3770253757116972329,
                                        -7392857994009629767,
                                        -7343263382530488033,
                                        3957805298525958274,
                                        -1269343938655434773,
                                        3803060112443058183,
                                        7297345806252259104,
                                        3355489891728934518,
                                        6375460500345692525,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': "ԃ'",

            'message': 'ҁ',

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
            'identifier': 'ψȤŦ\x9c®шѢ\x84πҤȲј˺șĺԗȜΧJϦБŴϚ¿ҧǌ\u0381ҤËȌ',
            'categories': [
                'file',
                'internal',
                'os',
                'internal',
                'network',
                'invalid-user-action',
                'invalid-user-action',
                'file',
                'network',
                'file',
            ],
            'source': 'iΟӺɟȼǎǊͿѮ˚ͳɳъİӚʀ΅ĦϦŻτχɟҨɞϗϓƷ·ҏ',
            'messages': [
                {
                    'catalog': '˃ʔ¡җʁĖщǽǍΠùˣȌ)Ԧҗӭб˗϶DͱΚҢΔԙҐ¸Đī',
                    'message': 'дҊBŹіҦϐҽκȅͽŪɋňĨŰϻÒʹӼΧǱΪ҉ɃäĢҲ\x81ͳ',
                    'arguments': [
                            {
                                        'name': 'ŠċĎϬėèDx˱ѯȂȍŮҖ\u0378ĺïɛȥˌЉƊª҄ɹƜçтʤʂ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4197812486075098504,
                                                                            784712712285227058,
                                                                            -3055162943626721306,
                                                                            -5554568020467073081,
                                                                            4246821009027374474,
                                                                            -6562293902985151351,
                                                                            4951776571242529197,
                                                                            -1281652478819785811,
                                                                            5456677358971825945,
                                                                            -5929117878982736292,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'İȫϢÒŤ˒&>ԨͿġ¨ˆʹ÷ͻ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԤпЬӛʝʗ˫ђɗӂʓƓԪĭÔ\x8fçͶЮĦӛ˅˛ŌЩҪǞΨ˞Ӱ',
                                                                            'něȹǣL\x96˭ѿ˯ѕԭĉʘȝγƘњsЂƯȒԘȁΦћȭѥɌ҈ǫ',
                                                                            'ҔʵΛѣͼԊοҏ\u0381ƌƃԎԘӝˇɛшɩЄѿѬɯψΥԂ\x98ЬӞЋԋ',
                                                                            'ŤĀϥӐŐǽëɋαͷ˒ә\x9fӉ˺ˁԇɏ§őҗ\x9bΕː:ǿђʻƐɧ',
                                                                            'ЩώΆГʆ\u0383ȻcˍҌǶσľƙ˜ō˱уȸΫѕŇƢ¯ĵ\x83îԍŪp',
                                                                            'Țɟ\u0382ϹˑʟіϻφŜƥӒԥ\x89д\x8dÍŃ˥żͲʨxΜӠ@\x84ӊƇg',
                                                                            'ƉǘɶћˡRҮȶ2\x9dɚZχΎʲӻЬƯ)ϑӹǅ6ŅůɒнēǱĨ',
                                                                            'ъԊɅʕ\u0378фνԜɋӍ˛ǜƄʫũԃêĺϗӍұРMŞ\u038d\x83ɒɥԚК',
                                                                            'ΣȧʛϦ˳À¯ԠňǁϢʙͱѨ¯ɜǈԓҶǋ»ҸѴWӌϼИȳ\x86¦',
                                                                            'ńˋřƦđͱ?ɩˊœ\x90ˋǘԕͲҗЊǥ҂ȑŹʠтѣ0Ȓɺǐqʥ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȴŲЦʎȨЬпòЋәýÏgʿƚЈɹ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -38265.321667872966,
                                                                            427557.95188536576,
                                                                            9184.635904558338,
                                                                            248136.50985158607,
                                                                            654497.3689706917,
                                                                            82411.22002220678,
                                                                            495838.19637723826,
                                                                            993543.1689082508,
                                                                            -19506.289924271463,
                                                                            514061.0127001171,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x82ϘǻйɎ\x8dȟňɰЇͺ\x9dϑǨΧΊΛʤęĠʆ¸АɚІȱţϻŵ˫',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            658789865619110696,
                                                                            1421836056780377360,
                                                                            -1429961275598333770,
                                                                            -2463273709891739378,
                                                                            2168871556775485284,
                                                                            6655724286367053937,
                                                                            3438476144805222818,
                                                                            -6722627318983663209,
                                                                            6617535427534856450,
                                                                            6187360477043049032,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϡΐʮԬɚήóòʦYʜhƯϛÛ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -26603.17549731741,
                                                                            84838.514866513,
                                                                            -44589.3498538501,
                                                                            462976.15846212767,
                                                                            981062.644240198,
                                                                            963514.6888870811,
                                                                            466596.5266610441,
                                                                            771474.6679727898,
                                                                            333947.6272091341,
                                                                            615441.9821417596,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˭ʳƳϾɫƛҍӖϹӜ¿ѴǶʹȦπѠˉОϊˮɃƢĞF\u0380\x9bĂ˂Ц',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3474347594949472033,
                                                                            1432612469525178141,
                                                                            7698743899954009024,
                                                                            5139978629080821908,
                                                                            1534251544870125418,
                                                                            7360837489591638119,
                                                                            -3260152669136939959,
                                                                            -1731373090821479921,
                                                                            2784329159214128390,
                                                                            -4180779499726523939,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƗľͽͳďФӐǑYˊÁϳMһʐ΄ο',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164100.883020:+0000',
                                                    },
                                    },
                            {
                                        'name': 'wҦLѶǶʊȌĬыš',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            874305.102961753,
                                                                            606284.7405832233,
                                                                            3698.2663782888994,
                                                                            467360.8719707305,
                                                                            364548.6677198686,
                                                                            -83017.97297692849,
                                                                            -51957.08030082259,
                                                                            702744.3859692066,
                                                                            260333.3217987917,
                                                                            836350.6885790192,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɐ˖ƒňϡЯтƊxҳųɞƮÄҤХˡԘZʗ_Ȝ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\u0381ҿàĂŌǖɨϓʦΆεунүˠʫϨʌ˔ыŒːԢĨΏzɩӃӁĥ',
                                                                            '˫¬ӝђџӄО\u0383ȼǜҥӈˌӟбЃWӓŜҫЭɤ<ŋwϔɠҍџû',
                                                                            'ȔǞВl΅Ưҷ˪Ȃ2 ԢOЭɝȆ£ǔҊƄԠҴэм\u0383бϲ\x99πϋ',
                                                                            'ǇψҞȴˮƫɓϵüģɼ',
                                                                            'dӿFȰͺƷӷΚѥ¦ҳȫͱ\x98ɯƃ¦ÐГƑɪԀ¤ʜP\x94_ȟǨʴ',
                                                                            '\x8fCĐ¬Õ˓åӰ¼ɰŜуĂҾŞ;Ώ˔ҘφȭчǶuύӲɄȅɃÖ',
                                                                            'ϑɻќӗąŴєϴЏ˯ėѕӤϫӠǌηŶÙȁзϘ=ΖǢÀԭ ŅĔ',
                                                                            'ȨѨŧ¤ҔÅƲŁџʈҗĵƏϜ$ȵ˽ˊͿ¥ώӨϱ\x9c\u0381!ǊюƤЈ',
                                                                            'Ҏ˗ĿӾýˎÞˎ\x8fȽѱ»ϞɇєӶΙƐӴєˎƦҭ~Ȣϊ)ҭΥ˝',
                                                                            'вϑѩɒö\\˗ĥӗЭłŝ\x8eąǛɆͻΩſĊӋΈyʨ\x9dīʄȃ¨Р',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '²ӅΩÊԥԢ҇сѝ҃ĳ³\u038bBƽǎοmɻԉЎfҩõőˮŭмϘ®',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
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
                    'catalog': 'ȇÙυѢť\x95ſӠ#ѫıDԁèͿэУʏϟ\x9dɄ§ë;ʅɧȀȇҽƼ',
                    'message': 'ʲаԞ˦ϯƹɗѨƑƖĈӆĂѨ˖ɈҍŨѩȏư˴аʎȶѢʼԩԡƣ',
                    'arguments': [
                            {
                                        'name': 'ӞάɛȹѦӘϢȉԁƧȕңӿ˯ƻ҂Ӱȶʕԝŗǿǜ˖ЇМ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'V©ҳѰаÁвӲҒżǸȁŸжƷϘŉσЃ҉ѐӬŬѓŘʊʙ\x8eҀҝ',
                                                                            'ѩʆ&В\x83ɊșҕÏƸʒȝԨʽȀΆpƦ\u038dŗ\x9dɕђǝ2ѴчμƃǢ',
                                                                            'δǽŊɬˬ\x9f˅ě\x9dӽχŷ#CԏëΩҝʘσBMɌЫʕƣëҨ<ȕ',
                                                                            'НʹɤӜsɹԆɐŴӣȪМʠƖ\\ƖʛЄȗ\x9eÓѿŤŅʅ˾ÜǩʟȎ',
                                                                            'ѝΚĒĉ Ӟ¨ĻθȀș`Ν΅ŒˮǞѴÐv\x9d\x8aӸӥΰϑʀ˜ȄҰ',
                                                                            'ɝĜė˱˦χżɜŷУm.ғϬšǽ¬îêʃƖϼРӷȈǟʻѶŘɫ',
                                                                            '\x93ơχɰėҋΡҾkϥ\x86ԑҾȮÞéѶԃˠǭćɵӳȡ¨ϧԝԎʥ"',
                                                                            'mŤΔѡ¦҆9ќрΈ2ÉϧҘ˂ϒª˲ϼΩϫΌü˗ͼĚʔҭτƨ',
                                                                            'Ԭ\x8aǴcȗ҉ɼǓóʤƕɓԋʄӮˀǅʧŏdɼŃϤàϙŻȣѕʊ˻',
                                                                            'ԭǡϢԜɡ҈ғҔСΓϟÖ¡ЧͶʲʚΖɋƬ\x92ä³ϽПĲǟěѩF',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'üɨϷɨқ\x99ϭψɸʹ˫Ȱѻӽʀèʙ,¢ˆĲˉŕҚΓғӸκÉϕ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164100.885033:+0000',
                                                                            '20210224:164100.885056:+0000',
                                                                            '20210224:164100.885066:+0000',
                                                                            '20210224:164100.885074:+0000',
                                                                            '20210224:164100.885082:+0000',
                                                                            '20210224:164100.885089:+0000',
                                                                            '20210224:164100.885096:+0000',
                                                                            '20210224:164100.885103:+0000',
                                                                            '20210224:164100.885109:+0000',
                                                                            '20210224:164100.885116:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'АȜXҞʋɥҎZȵŷǨʗ˟ҡȀѐȬřѤЯɏȊͳҗȐ¾˅ȃΗљ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164100.885385:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ȯȕ҄ӫӯǪɗɻҴːƹěнɴқǟʚΑεɂЋŨΆËӅѝȉ\x83ԣЦ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            455985.93289220415,
                                                                            759808.1107472915,
                                                                            11436.712793487139,
                                                                            24158.95198232071,
                                                                            345349.13063410704,
                                                                            578658.6484464854,
                                                                            -1801.4538227216835,
                                                                            32279.73529162159,
                                                                            811687.8569539586,
                                                                            862272.7976287315,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҭȲ3ԬΫ1ӬҹɯȀȣВϯȾŶ®¢=ʳǤӦʷ˯9ʶǜsDÂŉ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            55992.21594390794,
                                                                            10238.611210759627,
                                                                            -10499.653972043161,
                                                                            -98102.8853681289,
                                                                            937780.4029546457,
                                                                            416743.40241085994,
                                                                            277628.7683882423,
                                                                            375731.8530505043,
                                                                            960517.0753938709,
                                                                            689514.6739468669,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƻĲ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'ȶ\x82ҹЯȗӳʏ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӚǭɲǗǱѮŷ\xadжҷǃŢŘ©ėoӤŤԟɘТДį:ͰĄWҳǩί',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\u0378ǗąǣɠŖƔΗŁΊǷʬʬɤҨȶҕÅɭÐϺ°ɧӺӱԈұʶĥ\x8f',
                                                    },
                                    },
                            {
                                        'name': ',Ӝà˲ϔǪƸӣ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӌԫƜӂҶƠƲčΗӓãϨɃѡ\x8fȃǱ4ȍѤљȲѺйǲěºƔɣɢ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŹȭÁƇʀǶѭӥɏÏǉƆ\x91ДʺЛʙǥѸʶ8ԛħȄˮҎ·˩ӿ˰',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ζҿ˷hϥǻ1ѯȃlϼǪԪɽҪƿԆϸÁȴјκɁԂӦƄуαǱс',
                    'message': 'выϧӪǅζǕʸǭL°ƔԕΥΪūЌ˨ˢǆǘҷƜīǸDњë\x85»',
                    'arguments': [
                            {
                                        'name': 'Ƽ\x88JϲɘĿƋǾ9űǭµ˂Īɸó˃Ʋĵɋңŀ\x9bζȺʙ(ņŚ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7729554777849460571,
                                                    },
                                    },
                            {
                                        'name': 'ʀŶΫөΥɭѤҵńϲĨΗÇZ8ȭȆˇԩÉΣ9ɱɧƓ\x9cĤ\x86áд',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8848660186987962117,
                                                    },
                                    },
                            {
                                        'name': 'ȫȒȊȅқeͺψʽġȤŏʌԨĜÑÞѡüƾӘΥŔчťʸӬβώǒ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҔźДȄԆρ\x95ɡϻȕ·ącǱЬ3˾nӿɬѝӉыŽØА\x99ĈϡѦ',
                                                    },
                                    },
                            {
                                        'name': 'Ȥ\x9f¤Ŀ>˕М½ŇҥȭЊǗϡү4õƛҤɣǾӳψԆǑһЭ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 919036.7195478803,
                                                    },
                                    },
                            {
                                        'name': 'ŏԨÞθϯǦˏϹΆƀÃȑȥ\x80˫ÛȔӮϸˀͻ\x80DϐӿȹķĊ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            807200.3322577326,
                                                                            2039.3643241691898,
                                                                            547929.8743772842,
                                                                            490775.9089559417,
                                                                            348370.76770183636,
                                                                            106514.4237858227,
                                                                            722820.442047415,
                                                                            348480.43571759603,
                                                                            405497.06703232584,
                                                                            424689.37681463105,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ƃ¼ȪϤĞ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            485391.1000304372,
                                                                            171333.69952123077,
                                                                            -59565.85102751698,
                                                                            797344.5087868759,
                                                                            566574.9993668447,
                                                                            845050.7049244654,
                                                                            364822.94993473525,
                                                                            234569.9156014147,
                                                                            827804.4306328994,
                                                                            830886.0572847483,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'æűεŭɃͲǚ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7170750361649233112,
                                                    },
                                    },
                            {
                                        'name': 'ɕǷ<ЙƁ6ˉ¦ξӌɤϣƍԝКɇǗ҇ʒƔͱŶЋбɆ\x94ѲȠɮæ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164100.888499:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Č.ƞˇАɌȼѝȗʃˀќ!',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ʨϟӵȄǛKʴϠѹӘϜƪΧЙ8δџїЍaª˭ǀӞԘѫЖ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԞȗͼЎϽғĶέŔºǯəʹӉѤÌүҘª¾ǂɅ\x9cϑĭўʄǷʾȌ',
                    'message': 'ĸ\x95ζҗʩŷ~ƝԢĢӼéěϕΊ˥\x95^СȞêϵvĉԛӸ+˔һˉ',
                    'arguments': [
                            {
                                        'name': 'PлŅ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3129100974193159223,
                                                    },
                                    },
                            {
                                        'name': 'ѠϷДȲȨˢ>ǝϗĭ϶5ʶˉʩϤӪϒʰэϰЉǹǗ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 923152.1372797021,
                                                    },
                                    },
                            {
                                        'name': 'ļƚąļǟϋȦ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164100.889553:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ğΕɂȭðӡʊЋҐяҏɽʠ6ДȂʔĵЪӳÆоԈЖР',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': 'Ҿ¤\x82¥ŏˍϦ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɖɲüύʏІƁϷĎӗҍΤǳƲk˱έŌʆс',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164100.890062:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĜУ¤ЃˮÏӔǁAʡΰï˨ҠƼɿ˷ʑԬȆǿǢ\x9aǎȚӁʁǁđî',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ïŵ˵ÓϢ¼Ĵ˸§Ã³ЍĔ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѓ˕Ʊɼӆ\x8eœΰдƮşʁľѓıΕȒԣÎ˫ȍ3ίʪŮύԟ\x91ˏʍ',
                                                                            'єԇÚȨɴѼìċɆ˭ϋб˸ŧŞəʔŌњӡĉǔшǂ˱ӬƊ3мǾ',
                                                                            'ԚǨɬÆԎƫȡeЉ˶ЃȳĵΪ\u0383ϡɺϐɠͲŇÆǝ:7ƇNԩӎϼ',
                                                                            'ȃĥ\x9dю˟ɹǆĖкˣŽųΛ˩˹\x7fȑȇʙ\x8fУ1Ǳľȓϛçá¹ƚ',
                                                                            'ʙ˯Ϝ¼ĩ˳Ӡɺ˹ƺÈԋˁDűÈөćƛŘˋˤϱʛԣѶĉ˝ԉʉ',
                                                                            'җˍťσ\\ЦӊˑęʩʆĒ˄ҏ©ЦʿȋƧ÷ƐѤÔѾёΊиӞƃӱ',
                                                                            'YķӪwҴ½ƂǦǺǡϯψԩΙ\x95Қӿ\x9cӷѢăȾ˦ċʕ\x82ДŉЛ˹',
                                                                            '\xadɿȝǌ8\x91%ӻȄžїŁʽӏȼƭЁДǌːЪ˸\x9aȍʣ\u0382ŀjȜň',
                                                                            'ŰȶȶԒˡ\x8dɵɟ×ĈϪ"ź\x84ɮԡɂʏ*ӿ\x85ёԩ˃Ʀ˧5Ȝԧѵ',
                                                                            'ʞɝύÎ\u0382¢ɀʚƿɏōґҦ΅φ\x9fƷʥǛʊзͽԣʤΗʃŬӻǮ˳',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'χʼќĐ˫ɾӡӌȥ¼ԘǎȠԘȐˢ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "SӚ˹ϱ÷ҾϲǒďHƅ˛ǽ\x8fŰ\x96Ïƥ'ŝȔʏХʰàӽĩKƅѼ",
                                                    },
                                    },
                            {
                                        'name': 'ЩңǻȔȤĠ˞&ЄʑɜĉƽϬȝӣѧηҶǸӎǲƋͼɡʃ˗ӓҞſ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3801571660434287158,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Κ¤ҲӍʽΣӵƶȣƼȊʗşаƤxÀɉϬʌƀЅǳѭƌɋ\u0380Αƻů',
                    'message': '\u0380·ǱӀΆӯΩЙˑºʢƻˡгĎ҇łҴìѥhɹŪБƟҸДȮʴɯ',
                    'arguments': [
                            {
                                        'name': 'İ\x95Ϗʾϧ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164100.892969:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӲİƑÒ\x89ϏϮϫμũ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164100.893215:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѪǜǆχÒR4ҽ\x89ǺǬͲƼ}ǹԠР˛ó\x9eıӂÏȰÒԟԗìYȄ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ЌёưÏ˞ķŁ·ҧϙħȹĭ¼\x92ɾǭЯƣŮĥ;dΚǴчХϻĂο',
                                                                            'ˑьĝʁҘ˝ц˃ϩŔDċѷϋɎё+ΒӪ\x8cĝȤ˻ˉŰƸӷ˭Ċͽ',
                                                                            'ӏƏ/θîÇƄЎˆ˯Ç\x9bê]ǈ²οЧϰŻʣ\u03a2ҺњθƖx{T¨',
                                                                            'ҔȦÀƚƈ˛ċԒeçΘzɌ˖ΝɝŋϠЙɂ\\ĤͿҰǛоɸ˧Ӗԣ',
                                                                            'ÔԛʊǟJśǪûɆсčÆɅ1ɎʶȕʾÊѥO˱\u0380ȅӃȔȖєų}',
                                                                            'УΤοʝ˵˼ΗϑҚĄԊȱņтěӵʤ\xa0Ϝӷ\u0382Áʍӱҫ,Ϟ϶МҖ',
                                                                            'łѨ¶ǭʞĮԝαƮҾƔ@JÖƝӸЬɶϊӅǧǜϹҰfÙũε²А',
                                                                            'êěɲ˷ә¼Üɔ˒ÿӶԌ҂ԍѐ˻ŷħΞ\xadČΤ\u0378ѮƠЈҾʞêЈ',
                                                                            'ȱȈs\u0381љƫӹpÑɑˏЩԡů\x98ʛФ{ѣҌ˞XЧҕǊǘ\x80Ǩīϛ',
                                                                            'Ԥ8ȋòƯѳαɁӽʳрԂӝҾқɋԞÔɍİϦӗǷƸư±˄ΪȈǭ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x95\x9fǠϸɉ¢ʵʛȚѥƄʶŲ¥ì²ΘҀˆɑɜzѽоИJˑ¼ċϷ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'мԊЊ˯âˬ\xa0κɊRрҥιԌŚʢ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            876595.5331912991,
                                                                            731778.1168659832,
                                                                            572848.2275112153,
                                                                            -15337.39881579201,
                                                                            667844.123103884,
                                                                            191210.33376445645,
                                                                            676522.2214620415,
                                                                            24724.003581007142,
                                                                            -27141.62956686641,
                                                                            163868.70565542672,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '΅\x80\x93ʂĖƢΞԒÃĚ˲ŀƧǚŶNϬȕ×µɀķ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6425960240122731889,
                                                    },
                                    },
                            {
                                        'name': '\u038dфө',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7391442515832702967,
                                                                            -5497341143440011680,
                                                                            1660168340604797632,
                                                                            -8301852385130511179,
                                                                            7308713650867001187,
                                                                            1334132831114354291,
                                                                            4206079917027487948,
                                                                            -7868145904564438432,
                                                                            6856989746815018318,
                                                                            339115990815648077,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ё/ïԄϲԐԬƴƛĻǈȨеŵѳ϶Xȣ¥Õ:ϲԄұȋȖǛӱƸӢ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Қv\x84ϛԟϔώơϱƠόĜŮу;òʢưăԠԭˎƌυΥӺΘƢƴË',
                                                                            'ԐаħŝεқƮΚӰˉòʬѕеºѕŵѷǃąʽƍȊ\x88ѹѫEϯɎό',
                                                                            'ԪА·ƟΧǨϦȞʎɄŉ˷Oκ·ɉ,Ǽ!˷Ĵ6ŽĒтҎԞǃЎě',
                                                                            'ȒƵүЯӜ˘Ó8ӺâҩдÂʿJʛhʦҥɄǢûáɏѕɄӁϽӜҨ',
                                                                            '\x8aкŒ҉uЄðӹɗĳԕ˜χѤƭ\x9fϺӇыǢϱΞˏΜșѢ$ѤǶÃ',
                                                                            'ďђïʧЃѤÙůˋEŎȦ˩ȈЗȖǥкώ˩ѕс®ǠҳóӤҕǤԚ',
                                                                            'ұҳξȚıΕң\x9a·ʵɈ˸çǺŉиҺʻªѹДΟÚʮʴϨζϱȌU',
                                                                            'ˤʓіͿʬɳˁȯɸʍϭӂȓϗũɷνŭȈҮД˫ΆΩ϶т\u0379ŗҔˠ',
                                                                            '~ќѷʭŵŦѯύʪlȹҵǓʒѣć\u038dҖɖΏYӄ\x80ӉӃ²ȁƒŰÿ',
                                                                            'ҽĂgǄƱǆѩԇλӎʒʧĊłԅўŭɝΉ>ɺƞѭыҮϪÄʬ÷ɪ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŬP»fѩЭνδϫȏƜӄˣđ9ʏѡŨЛͳʉʍ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɦԧƍϨĬ\u03a2¦öoHáȉ҅ǠɈɵϲӢWƩʎАðÐʀĘƿЍԥЁ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164100.898258:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ьĀųȋцӖϋaāɷǤѡɉ\x9cғЖƧċZЮĳξȯŋȯƢ\x8aϪяε',
                    'message': 'Џɫɰ˘\u0383ŗԀŐˍƌĴѡӔ˴ӥɳϔӭҘȧņɌŃ˫LЌ΅ŝ˸Ȯ',
                    'arguments': [
                            {
                                        'name': '҃ҟɑɎǢΕӫɊ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ɓő˘$ȑ\u038bΘ§Çʨ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '07\x92ǼɻˀаégҕɟψȌΪyϋʼЀԇƶтԁψΒ"ǌ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4495992454939093066,
                                                                            -608158542904373563,
                                                                            -2552882554092430308,
                                                                            -5022395896088405367,
                                                                            5698271494483570000,
                                                                            -7909399705461063990,
                                                                            4944906760635340871,
                                                                            3979395392625576081,
                                                                            5982128318958523526,
                                                                            1469213127738347107,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'µҒʡǼ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƶĻ\u0380Ӈҥ[Űәӭӏ`Ж˖âҚЪ˵Ώ¥·ǏêŽԛį;ӌȿЪƭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164100.899509:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ʈ˽µ@ҹ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164100.899672:+0000',
                                                                            '20210224:164100.899687:+0000',
                                                                            '20210224:164100.899696:+0000',
                                                                            '20210224:164100.899703:+0000',
                                                                            '20210224:164100.899710:+0000',
                                                                            '20210224:164100.899717:+0000',
                                                                            '20210224:164100.899724:+0000',
                                                                            '20210224:164100.899730:+0000',
                                                                            '20210224:164100.899736:+0000',
                                                                            '20210224:164100.899742:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɺяĐƥͱЏɭϓʜƊ,ԅӅѕәΦ¬Ώ˗ӳʪŮłīÁ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4562549827707564056,
                                                                            1984526225907466180,
                                                                            -2250296984857587267,
                                                                            -481332915705408749,
                                                                            4336953823993544502,
                                                                            6444862584953521487,
                                                                            4210694517208865603,
                                                                            3218508327098798231,
                                                                            -1083104612171968854,
                                                                            -7379524940191728648,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '÷ԄʭŌѷJφ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'зųȟ:čƂӯ˔~ŀΎϡɓûѩҩʠėѢ\x93ӣäƍЖɪńЛιm\x97',
                                                    },
                                    },
                            {
                                        'name': 'ѱѵŉЃĪ=KЗшҦþқÛϣǿѝǪǧʂɽǫ>TĶμĮĜŤʈӅ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 720531.6280807044,
                                                    },
                                    },
                            {
                                        'name': 'ϴƋñȃďЂϓŭԤŦ\u038buԅƊʜǈԜθϝяeƿѬфјŇȞŸϰ.',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ҕɋϰ×ʐңɑjЈҙĹ¥ʹxßӏǖνƵȁɝɱЂìˁѭŌΪѹĵ',
                    'message': 'ѵ\x8f^ȷддͳЍɺɩҩʁШƯ\u0379ȟԮĀǡĂеηóY¤ЁυĞɭȹ',
                    'arguments': [
                            {
                                        'name': 'ҪΫŚɁѿŷ\u0382ҺüϡĂZ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ûԁöҌƾДθƢɓŇȃȬ\u0380Ǿ_ƈңǨźǟRУԧȱ˫ąƑκНӎ',
                                                    },
                                    },
                            {
                                        'name': 'ºԅӅʨӪÃʷĶˢǢůƩȞφӇ˘ǖƨĐĖAӬ\x8fǴǨŶҸƲӆɉ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            176680.1290216311,
                                                                            832910.6346300809,
                                                                            893949.5525917542,
                                                                            89121.20789146505,
                                                                            -25567.561272868043,
                                                                            123160.9910082831,
                                                                            -15643.288046416943,
                                                                            739688.6436404886,
                                                                            627151.5209366255,
                                                                            1216.3846292702074,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȵ˥˸þ±ҝƣԉŀОǥƁӔ.ʐԁҭѷfѷvԞÂƜӷѼĵ÷)Ύ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǞʒΨˊ^ͱӅԞӤΗçŚїǃȌſ\\ιΚӒƝǪϖЧȴnƃͶÿȊ',
                                                                            'h\x89Ί%Ϳl˥ʏӊоƁϗˁӡͽЬʖμ\x99еԫȤԈЃx˾ʀӨƱ¯',
                                                                            'BΏԌëϓ\u0381ԒǚɖɵpτČЌĹȼɩƊϱǎM²ĶȵѳάӮ\x84˘Ǿ',
                                                                            'ƍʿυ˗ӄϦ΄ұόȕăƧҤɶ\x86ƚǈȆƟӥ,\u0381ӼӦÅȌǩɸʜʑ',
                                                                            'ȝ\u0383˔+ЍҴʺĦˋϔǶ\x94ʥȉљʱ^ʽҟ\x87ĕʞʹƠȞćҮͲәŭ',
                                                                            'ʾӏʯ\x99˸KԓӺɢϦѯ˶/ТnÑƠǈ\x8bǘ\u03a2ʑӏĿ\x8fȠėɗɒʭ',
                                                                            'S\x95Ͼ˔Ȝʡ¢ƓǢ\u0378ΆϘѳºʡžȘȗ˳Ѡ˺ȃ˄\x8eϧ¶Ϟųѵɐ',
                                                                            '~ҴƅŕԑľҶХʺ\u03a2ЩɕLϺэҊўŮЙɼǅхÆƱ¿ϾýǨ@\x8f',
                                                                            'ÒŲʊYȐͱ˟ӿβҕϝ»БˤȓƼKʈ\x9aǷǝ@_ԃЈÑŸç}"',
                                                                            'ΔʛʉѶЇӶĠŚ\x98ѾԘ`ғӄӖƘǾUȻηɖIŀUӕɁƍ²χÇ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǎɯʢʹ\x84ӓɻʇ\x9d˶1ėèͺ}ǦɔƵń˲\x90ȁ,ǹȢȺĔг8ȉ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164100.902015:+0000',
                                                                            '20210224:164100.902037:+0000',
                                                                            '20210224:164100.902045:+0000',
                                                                            '20210224:164100.902051:+0000',
                                                                            '20210224:164100.902057:+0000',
                                                                            '20210224:164100.902063:+0000',
                                                                            '20210224:164100.902069:+0000',
                                                                            '20210224:164100.902074:+0000',
                                                                            '20210224:164100.902080:+0000',
                                                                            '20210224:164100.902086:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȪŅлǁүÌӇҥǒчSĖĩʮνɥǫǨԣ½ŁȬ.',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ԉХНĮ¾ƵɱҴŶӭF¦ɅӅύӦŧ¸ϱћŬϤӮ\x98ʷόѭ°ηı',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 986566291959807394,
                                                    },
                                    },
                            {
                                        'name': 'ƻшȦѦǤ˼ӨˆӱҕkѱПѣЭʋɃ˼ʻƔÜԠMɏèКаέˢǙ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': 'ƨӭ˰κʭƍƥPʈΰУƚ7ҵ˭ӛǩŘɭâʼȆǣOІǢŎȔ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            529848.1458747679,
                                                                            742425.8477789053,
                                                                            97819.70292823488,
                                                                            918685.0839843143,
                                                                            -11046.104318246726,
                                                                            88728.84395005679,
                                                                            251900.46213387232,
                                                                            293218.9013200886,
                                                                            371844.54047805816,
                                                                            982547.8320812683,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƾƷūǘϖӴϹЙԝðϧZΊͳ\x98ˌӡÅҊźԬҧӉıЬʌƇƠҢh',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '>џǿĘǛǏĖоШә҂ĈFˠѐťҿНƒθǂɆӽūAȕɢɾɼ¥',
                                                    },
                                    },
                            {
                                        'name': 'ʨŽŧŚδӅŞùԓºӉʫϊʌËɐʛϔԗӵ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'àўųхϳʸϖϙΝĶΜίɓǌƼϻϏϏ%«ҮaȻЉŠŻƦĭéϋ',
                                                                            '¸\x91ʌÄ:ÌɥgԒǴЎ½ʷΌCˌƉŮ)¨ĩƀɀԕɭ·ЋРŕƭ',
                                                                            'єѦ˅дǭȻ˷Űѵŧˊ˪ɃϹƈѹЮѾQǻ\x88ϑȣƓƳώǮӔϊӳ',
                                                                            'ӤʘüūМ°ŘƫŒΓ½ǔjǽqҒǦΤ\x9f\x90ĀżɋҼǣСɣȱѳĵ',
                                                                            'йϷŌüŕΪ˵\x9bӯ\u0379ʟѠǔđʘ\x95êō҂|KӛȴѼ®Ơ\x93ăπé',
                                                                            'ŸŨΗѴџ\xadΘ҈ĵķйАϬҽ¨Ҏñō£ƻſ÷ƕȔгæÆǨȞˑ',
                                                                            'ʹɚȸɱɕӟÎңȨÜœәìӞʷѕԖЗˇǔ˰ɜɢǌʇȍǄʑäϱ',
                                                                            'ģŹή˼ΒҡǥƽåҗǠXћ^ҒFҷɺΐӘƍơ˄\x85ϊʓWĀɿǮ',
                                                                            'ƾÑɞǓȇԪґʃ·˝°ǚˀɎɑӌ^˄ƵϊɥĄőӜзӡƆμϚк',
                                                                            'Ύɂϝɪ2ƥΪΣτƹJ|Аүsȫġʰʗɉ\x7fQȕ<\x8e҄ҀƢΐΎ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '"ȝѨʀŐ\x94ӕ˴ʨ{ĉŗŵӥʆǲ˺ʹÎƓǇӖˇǒ~ԒǴ;ÕҼ',
                    'message': 'ľǂʝæџȝӜǭ˱ЪѧыǛӡZкΤȉҩȿԥʞτēЬˌˬĔԎɞ',
                    'arguments': [
                            {
                                        'name': 'ӇԉðȹϑôԨxċÈ\x85Ӯϴԓ\x82ŊƕӮʍ˒ƞЯеŔԓζЩΦ',
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
                                        'name': 'Ǳ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            623929.7454594534,
                                                                            409699.82403164986,
                                                                            686863.6775649807,
                                                                            539135.0058719121,
                                                                            236194.91854066774,
                                                                            -8246.492373011672,
                                                                            129128.59098690757,
                                                                            775223.4441785027,
                                                                            803729.768985026,
                                                                            727381.8249419264,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƈ<\x87Ɉ\u03a2ˊƷƯΉαҖѣ˹ОĩƱpҦҮĺƪɽȺUѫ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 157031.1628920969,
                                                    },
                                    },
                            {
                                        'name': '\u0379ȏɥѡȯ¨@',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'ÒZy\u0381\x88ª$ȳӐ҄ƀӊѕϟðї˰ё?',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7799181114482896884,
                                                    },
                                    },
                            {
                                        'name': 'ȍÊԣЂӴҥ˨СƧҋ6_˟tˍˡҞӚȭϷȞł\xa0оϯκЃοΈɘ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164100.905028:+0000',
                                                    },
                                    },
                            {
                                        'name': 'üџίǖԮʭ\x97˰ǨuʢÓɤϷҹʻĴӑӮӘҪ%ЫǽùϭʴϺɶŎ',
                                        'value': {
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9dƪâöϤŘĞòќcϻþʍЌ˕ЊÇvɀгǷSԜʪM˩җѺƪ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'П`ѡҢɵИtaĄԅǟȫƐWҴťɏгЉ>ɅƯɴ¥ɫ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8966016412036239370,
                                                                            -986849406606786343,
                                                                            -3712790077021501126,
                                                                            -3293798687938444729,
                                                                            -5565827500505792444,
                                                                            7493110685291061811,
                                                                            -4903425561606675162,
                                                                            4636925056641971509,
                                                                            4611858413953766350,
                                                                            -972079090249441942,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'әNЄɹˣҦŝÿ˄ɯӦεöԍ#ɓӭǥÅÄòӠІ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            487308.8595197231,
                                                                            849516.8705902029,
                                                                            715091.3263186082,
                                                                            414163.99439747486,
                                                                            635196.606980259,
                                                                            369977.475798045,
                                                                            284315.80250287766,
                                                                            684502.2470098569,
                                                                            117237.10681353556,
                                                                            341041.3439694316,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ÿʽƿ\x9cƘȌоѭΦĿWϸ\x83ȗǙΝÐԔ\x81ԢЗҋóΰđΔԄԧѲx',
                    'message': 'ѨϢҵº˶Ë>ÞƋpƙϻʵɧԋʿ\\ŦӅӰԬԅҺʁ4įKȔϷ\x99',
                    'arguments': [
                            {
                                        'name': 'ҏƺҕҥύЖГ˗ľȞΧӃĽʁԭ·Ζ}ƍПҘΫċҗ\x87ԝϻn˖ɴ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '´xPsŠТĂӐԧӮ˞Οɀèѓʎč6ǞĤþ\x9aȠԞƚԫƇΗʮК',
                                                    },
                                    },
                            {
                                        'name': 'ɤDǰ"Ɂԣ\x9eǋĒԦ˰úĆ҄иҶαХ \x90ȲȬƎǱρÅ˧ԜɛӬ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164100.906902:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʘѾӵʿ\x8dʺǑΗĆğ\x93ϯƻϽϼрÄř΅§ϻίɛq¿ӇȕFˬμ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -45590758745781751,
                                                                            5857994342684290045,
                                                                            -8369430270996016935,
                                                                            3495574803016988251,
                                                                            3954249838543339881,
                                                                            6355191100152793020,
                                                                            1441154870215526688,
                                                                            -4478512575799635888,
                                                                            3933289150763728843,
                                                                            -3340183825947688421,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'џ%ȀϋǬÏčŮӂ\x9cӥ7ʣɵ˵\xa0ӘYēǎВ˖˸ѱɔͼҲ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ß²Ƕ²ɊѧҍǿτÉŻŌҫȜɻҠΤɡŌθҩƩʃͱbơЍ¸ű˚',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164100.907864:+0000',
                                                                            '20210224:164100.907897:+0000',
                                                                            '20210224:164100.907920:+0000',
                                                                            '20210224:164100.907929:+0000',
                                                                            '20210224:164100.907935:+0000',
                                                                            '20210224:164100.907941:+0000',
                                                                            '20210224:164100.907947:+0000',
                                                                            '20210224:164100.907953:+0000',
                                                                            '20210224:164100.907959:+0000',
                                                                            '20210224:164100.907964:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӟɹăEԈΔѼҿ·ɾϧѴӷl\x7fǌюζГǽġ\x86ƒ\x7f¸\x93ǡʁΪʪ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -21579.099318213557,
                                                    },
                                    },
                            {
                                        'name': 'OʄУӯYԑӡÓȄ.ăȖYӵɽʠеŶ˃',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            941108.7654593296,
                                                                            175971.64339824428,
                                                                            248901.70263879548,
                                                                            -82471.39265181616,
                                                                            387520.92162090424,
                                                                            894025.535106178,
                                                                            396287.221726352,
                                                                            237776.72995855135,
                                                                            264449.3449155784,
                                                                            386332.3740795468,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¯Ґʅ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164100.908583:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӲѸѹ7Ǹ_ǻŋ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1502534319573700748,
                                                                            6108781693296480260,
                                                                            -182600882799579724,
                                                                            -5465108350789067266,
                                                                            73010354496959770,
                                                                            6586284643270730299,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʘƊõȦɶΎŷāқ(˰^кȳȹЂΒb˻ȂƏтȏЯҞҠφƁӂ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9178706489481336378,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΈϻŻ«Ǿɚɮ˰ÍвϔɵŘǖιɂҏΛӌʡ˓ԌȩǅʿϛӵͳǇљ',
                    'message': 'ТXńĉӍƗȲʣˇͻӇϼҥ\u038dȔĽWπ2ǥǞϏŶ˾JϋӁӤӻӔ',
                    'arguments': [
                            {
                                        'name': 'ҲķǅY¸ʝ=½ӴȐҥҪ˫@ɳʩҴûӿəΏŢɅǅ\u0382ѤϷѶЗɻ',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʓŐӐ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1998862496088190716,
                                                                            5540617807669260829,
                                                                            4120423832696582171,
                                                                            -2954585343562542496,
                                                                            2112179521975209813,
                                                                            609545554991465168,
                                                                            -313344531604730427,
                                                                            540423897112723062,
                                                                            -8343344840648237596,
                                                                            -8289747888921892810,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЭӲ~ì²þԑːԬѳȴȢɒʟҎ\x85iìҀ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƊČ\x9fЁα+ãьҠЋã`͵ФR˰ήϰ˥ДЄģ˽ѐŐΧŸŜˑƆ',
                                                    },
                                    },
                            {
                                        'name': 'ҢϋMŰĖǱ^CƮƯǥŌŚԜ˨ңӤЌǕЩ˸șЇ<\x88ȧĀȿʘʼ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 46659.57989201098,
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

            'identifier': 'ӯЗɝëͿ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': '˼ȇ',
                    'message': '\x96',
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
            'name': 'ǑѴԎűĈǌƻŻϥҏ˝ÐԍΤă\u0380Әж ƭѮ9ДŊˬǐÙÕѵХ',
            'error': {
                'identifier': '\x88ӅͻОƸӇǱǤ1ϔѪWd©ċƾ«Ѓƌҡ¢Ɔĉ\x9bϦʏiƝғà',
                'categories': [
                    'network',
                    'internal',
                    'file',
                    'invalid-user-action',
                    'file',
                    'file',
                    'file',
                    'invalid-user-action',
                    'invalid-user-action',
                    'invalid-user-action',
                ],
                'source': 'ŔɸʜưʑΰåŬ§˘ŔΓΊҙĔԨæƱf˫ϐτżʹ˖¬ԁȔЃ³',
                'messages': [
                    {
                            'catalog': 'ϻяȨ§ſŮ.ƖӡӴŒΈӥţʱԪǡќшÂŬľӡ\x99âΥrξ\xadʯ',
                            'message': '˼ȎӬɋʉÔ҇ŠŒÃȡȑàԌÙ҆ʹɦćǲϾˤԡ\x9aʼƘ³ƘǋŅ',
                            'arguments': [
                                        {
                                                        'name': 'к|äԔPǨӳðĈǥ»˽НЯԊ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ėҫoҁȽƞђ\u03a2ĵuʾӎͳ)ҹćΘ\u0380ӱŢ*ʪӛϋǖɕ\u0379ʓŁ\u0379',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŁΉԜԞѫÑʳʜǹÐı\x99\x8f',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'tçɷƂѼєԩʚϽӯXɩĝƈѕӄ{Ȕ§',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'kɶϔë+҉ɈɯňԘɾĐ\x800ŝqӟçȁĵ\x8cĬϬŇԫσhˁȦÐ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԩΜНƾР\x9bϑ\x87ʁ˝˯ɸӃԢǝ\x8cÂɒіʁ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -878182785890059061,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӢϦӨȶȃ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƿԕ˶ƂœʛÌΪϵˤԅǛмŐӅǑӲĮЬ)ͿϚƽʰӳ˒ɋ˴ɪĘ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˢ¤ϞǈȇMʡЅǩƗš\xa0ĄʧιɯΨ=˛',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ίȊĀЍԁ˶9ɨû\x9eԖ˷ːӟhå&ȭ´ɔÝŵ\x80¦V΅',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ăԊϪҴʭfϢω\x96ϖŹɻǚʠ¸¹ԑԭј|ƙΗ½ґώВЭ˼ǫМ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'KІѱѯМ^\x86ͰԑӵԤ΄ԦϟҼƓΕѠҗΓɴɳȍôÍȫʍƺȄȯ',
                            'message': 'ѼEɾƴǊ˄ϻӅĺҢгχԛԍ\xa0ӣŹóİЍсϸʞүă˥ͲȄԢɌ',
                            'arguments': [
                                        {
                                                        'name': 'ȵ=ɘɘӯǰňʃāȈʇǷƪƹȣɥσζӛХϣӗέԉý˔ùԀ˓ƴ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ǔ˩ʓΜȑųϳ˷ǳěhțþǇȃǍάɤï\x8fщʠЅ²¡ʝøѷōУ',
                            'message': 'ȵӃԮêĢрǀъǠЂɔl\x99ϚŒYĘœҕҧŕчŘ3ĨΝϰɋ\x90Ɠ',
                            'arguments': [
                                        {
                                                        'name': 'Ԓοæ®űĵȤȢ&ӱ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǀ˵Ɍ]ı˴ʱ_ԑШвԂћϤϙʦƐԭӴѝ`ƋΝķĞрőØġѿ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӕʧԗόHĺͿµϑÅŪũnѩ/Ȑuԑ"ǉ\x8aч$Áǫê\x85',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɿ\u0382ιǜǅcԐԙċɩϯ\x9f¯ӆ4ÚĄʉƖ˞ɖԌӜÙ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȣєʐ²DėѠѯӁɢǟʂΥӷ=͵ЭѨȵӆŐҋ§ҵ˒Ӄ҃',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'éύ˕\x84φӲӍ\x9fɪІêŭҖͰřɓҹ\x95ȏѦœȏЩƹȡέſHÞѳ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'лĩŖϳ4υE˽ӥϹǪɩӆӗɽ\x8e\x8cдͽёѪκĸ˚',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˇҸΎʌϗҐӦƋȊȶǒȡˬΆĦǱ¥ˋħ´ͷϵҩ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0382йǎîӁȣͻӓǛÙ҆ΈLɟƿΙϬІ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƽʖzȞÃƞAǽѹϻК˺гҚԭҗӆ҃ȥÏȪκʟ©ɤ˞юσФù',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƥјѼϧԂ˺ӺѢȷςɚ²Ǌ-vğW±жǌʶ÷þƬĜŕҶԧˢǥ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164100.858764:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѨɪΡǛ¯ԜӵĚDŎ,ŊÜӚҊɨЃϰ`ьƈXрεŇV˴²Рĺ',
                            'message': 'ÍЛş1ӼϷɮȲԋ~ƾàԕÊáȈčòň˽τ1×\x9f ˺ƁͼǀE',
                            'arguments': [
                                        {
                                                        'name': 'ɆɭӲѮδљԄɘNυ¿AĬĻϖÐʢβяȘ÷ŚӞGңҞзɌ¨ġ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŕлФǝĜϷѬƥ\x9cVí§',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЎʬΊÎԬπǱ@é8ê˙ϪɗËǵԎБԕʋ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 613780.2885826379,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԟξǿĩόʘɚӈˀJЮɘN҈¦Ĺλ×ЕƪíµȝҷҬʌƔ˖ҩɐ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƼҳɀǩVƓ\x90ԥӈ°ϨѵûɧԫѥǒӱϨżΒī\u038bчӮ[лċÒÉ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȊɿԙękĀ{ǡΚªԎžɇθɁǔʐ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x86ʅҝȣɛϿņԦӉ\x96',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӕſµŚ}Ԋę˞˜¸ШʴPǍ\x85ŊԤȦGj҃ħɢƍΈ\x82\u0381Ϧσƌ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164100.860555:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Γ\u0381ӣNѧӬn҂ԣ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164100.860703:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԦˬўŐιΈɯƮĊӃ\x80',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʕʐŻĐʎѩƄū\x85˖ώũ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 307029.1290693917,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '(ΏŨ¾ВɸӡӝλӏΟÞҫəȣЊҏьĵзǲҕȖǃγϤЁåɚƞ',
                            'message': '!љӰӊΉL"ӐчȮĹƑǹŕČ`ŰДiȣӈĊʮc\x84ĐѢɻʠǣ',
                            'arguments': [
                                        {
                                                        'name': 'ˁÁҥ˺ϥʀ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3539734775217292622,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȥǒƴЊ§ǕȕΎҵϕˍӽÊĈŤԐǎɢєΟʞkĽðѡĪƦіԊê',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĿԈҊ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'À\x9dĴǃӚ{ԧғİϲПǡЩʆɢϖ˂Ҝ\x9dśϙÙdŨŤнÄħˤѻ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6069988319679476211,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƚęŇ˽ȂɆґgщЦΈ>',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϖű¿ʙưˇҧØΕˋɅũɾô˃ԋȓɲ^҃ΣBŗЪό\x83\x84йʝ¼',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʒ\x90ɲØȨԎɪƈǊςȠș§ĥ±ǏӾЬ\x85ǹѸ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȉӚϕϳƎđğCɎҝ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6869385241711428145,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ţ˞М¡ӊΙѕÇӢǄ+ѽé',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǥѿξȫÑҜԉʱ×ԚͶɱˠšȼΟȘèʦ˳',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɒ¨ȋʴ²ȣі\u03a2ӂȭ¸КɥѦŅϒ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҐYǎҪŎʶъȔǱүɡϻȜӛѤċȴġΔ!ґȜň\x85ĥʈȹIÅʞ',
                            'message': 'ʓΤǙθӺƝϬҹӝǸȒИɳßΙφ¾ǂ&ϪԇќqȜшúʲψοԪ',
                            'arguments': [
                                        {
                                                        'name': 'ɨhƴ°ɬƇʉ½ɀӨŖ\x90ȘЮĐǄΫ6Şɺ#ŸЇԚƱʜęЇ3˲',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6686407988109511388,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЬħԡČΦņɌũȬŧįԏfФ¥ØҜ\xadˇȗѰ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŋș\x9eȭõӲ2ԫʰȹökҵΎˆȆТЭ˨ЄӁ±ǌǄɅͼOİͷь',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -27139.905060867604,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӨȠ]\xa0ѭ<¥Ȼ|ąÑǸҸĨӺǳVǗ\u0380ЇϘǜǚΫ\x97ʴԊĿƑȺ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164100.866758:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '³ƓΟҲƂσΙʨœ®ËΖӂӜɓφ\u0382΅ɪ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˔ɔΟðӝӁɔsȵ\u0383φҴȸ/ҨԛLŴκ[ɂе{±',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '½εŻ҆ŠǽɂЍ£°Я˱',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 720080.3626515073,
                                                                        },
                                                    },
                                        {
                                                        'name': 'žҾ˒ʬƸ˺ś϶ƿ¨ʿӝӉÈӇѩʆĀҲϙ©яӆȅ҅˕җϸ϶º',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƕέȹŠʓMȾĘЁɜςЙӉԍˏѰǩɸΊʹˈ҈ц/ņёƂτpЃ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 483586.684859453,
                                                                        },
                                                    },
                                        {
                                                        'name': '2',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164100.867666:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x92юʅζɝϐϵЗϮӴǥŀ҈ŋϯ\x82Îƶ˦ĖƐʠčàDбƙ˭ĝŧ',
                            'message': 'θŰҋйӲ³\x91ɹĂԓƕÞɚϰʎSчèʀǄHȂʺȴқȍӓӤʮ^',
                            'arguments': [
                                        {
                                                        'name': 'ϖѻд',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 638249.809604412,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȯũΊÉ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4617147677213495659,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÕԟǇ"Öƀϗżѱȓɏ\xa0ĮƸʾŽɷҦťȝЛǈĘΉ 1ЦsǨƛ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӊʨΫОƆО7\x96ˣΈƍʻТUȪεÒħʚǐǚɍΚԢҠЈƘ@ơÓ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'њiʟҫ;ϫƛƇÐɗЀјȋЀэӽʷйˉʹ˙˼ǟŗѹѨΩđˏǍ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǧǛЦìЎ\u0380ǀĲμ¡ϒҬ\x9a΄іĤȋћώҌϐʲӣϷʍήεɨ¯ԇ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'øśƓȝøɗŔʬǖѣЋЪʎЕYǵʇ\x82Ͻs_\x9fӿǦёŝθϩȻ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ˢǻŐƢдԬđʿ¦ˑѯß\u038dЍgUΚ8ƎƝɽϜѭ\x89юОϡƽļǃ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɍǙ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 807715.6486798271,
                                                                        },
                                                    },
                                        {
                                                        'name': 'њƮԖƗӧǙŞ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʘȮ\x8fņ}ƊʤϑǱ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȎlρÔ˧˼ĝ˱γϣʵǝ˭ѿИϹǮHҡӔѾΤ¥ҪЉƒȒǩѩȇ',
                            'message': 'ӇȁĹ¯ÓƛƼάʧşɱϒĳβң@ʚщŧ\x85ТҙQͷjԆĎˑŐȎ',
                            'arguments': [
                                        {
                                                        'name': 'Ø@\x91¦æÈÚ˴Ǘ˗ԏβ\xadŘŜ˛҇Ђ©\xa0Ϲ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ћӹҊ?CѤ΄ҤӺӂӐ΅ˡΎǩѾҢ%ҵɻɡӢƴAʨʖ˴ΟӉ÷',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7728651804935776060,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƻΑ8Ł',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ћӠɀˆ\x93ĲϠºʜ¾ќǝiѧԬʥ²~ͰkǆƹҞɾʛӸħ5Ǟȭ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǾƗҢϤӚӷʇǭŔöʇȱǐ\x97ѝ¯tɋѰȂǄ˖ϢСԢɻɺƩφƥ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ќ͵І¨ʦҋόĿΛȖ˫ҟЯǪӾƒӨèƐ\x88vϟͼ«ʍұÂГƃǦ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164100.872362:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ôłù¾ʺЯҤá',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŷгу\x8aʎ/ȁ\x81ĞŦ}ʵˇ\x94ӟЦ\x85¥ˌ\u0381\u0380ɔȆƹ\u0380ʾǳǄˇĈ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʖƀĸ\x9aЏҞӗ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 885466.93021032,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x81DÍɃҎđrƼԥÙ°ƳҢșӀ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'äıː\x83Ű\x84ҟȔøŌȦǈѦŭԌЗɏӄýƚ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '¸É\x96ÚеɌϘΉɝȋԍŦԐkǦҡӞϽԋŏ˜έƭƁƱ\x87\x8f?Ȣʓ',
                            'message': '¦ɠʁԌCŤłϫƶӨϟȵιȅŲċԖϷϸԪƶƜǗȏѶɴҭϟ\u0381À',
                            'arguments': [
                                        {
                                                        'name': 'ɒɝΔw',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĝŭч2¢ѪÜʞ˃ћƍʹϗҋʩ}ƢǚԥœɝΔЫӸӗζԝŨɈɶ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɩ³ƅģ˦ʖʋǃҼʽôƒͼe',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 956897152949580647,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˁӱτҴTϩ҃\x94ҨȀґҥƬ"ΓЂҳɈӉѮ˺ȪҷȺЊȌ¡Č',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164100.874141:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '΄ηǗˀıÕϢÊ҅ʤϣ³ξĳϾÑŜԗΝ\u0380ӼҜШ\x96Щ˲ư',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ľЊʹԙͷƩЅҫńċӇɕƹõЭʦɵ˒ƺ΄δíɚΗ]ɧ,ŕƈ˯',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӻϊԟɹBϼż_òȶĻɳѱ˼ƧfЇĹŴ·ʖҿζ\x87F0äƚ§Э',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЀԙǞVņҲǚ҈ȁӬĢȄƙ+ǅ˚ěѪԍ\u0379ђǅ¯ЕϬęHÑˢŗ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӟ˖ӆχɅγĝώƴІіɋԭҾ¦ǇʏƽʙӸŚǙʭtȃˇЁʧӉe',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 279599.69033588975,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ê\x82ԍԋzӱˏ¤Ѿ ЀSŌē4',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȷē\u038drŒȿŸӷάԑѢԕŉ¾ƑIǀҋҝ·ЧǶԄПBΗƸĝġЧ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '҇\x90ʇdȕǗɄѸϹѐĕʀɎԪˡwÖàCЊ\u038d˩ҤїöǛОŤЖҡ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȎӵԟҔ˂ѽҢ˳ЌƦĦ΅ȱ+ӆ\x97йǪɻΒiѻωͶF%ŒʻԠ\x98',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǚӰѱȳʜǡȷμƴ˃ɢ-ԌѬȮ5\x9cÀ;÷\x8c\u0382´҅ŮҜ˸\x93˸Ќ',
                            'message': 'ÃƻϐԏҜԙɄ~ĆӖ¿ҊƞфȩĜ¯ѥĄЩŧƹƙ˔˾ԥеӦȰƠ',
                            'arguments': [
                                        {
                                                        'name': "уρ¨ıԠąҩѤ'ƻƸмƱʅӪčʎXɌūԞўˏ\u0383Źϝ",
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЬĜȤɆÚӂсΰѼ»ˈ%Żһэɑ˭ɕ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 464746.26483868016,
                                                                        },
                                                    },
                                        {
                                                        'name': '[\x93ήԜđƉPĜŞǯԖƼ҇Ǐŏ˩\x9cӺϛEɽʵƅĦ\x94<Ԣ¼҉Ϲ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĽԓӉɶӑ£γĵԕЀƷԡýȦіŽw8ɳPXºèΖĴίϑќɛƛ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӑ\x89ΙщЂĆĝL\\ɔЈ®ơ,ŵ,ɲκźÍҫòɘөJӕѪȖϔɓ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'IҌǹ=Υ˸ƼϚͱ΄ǞCƞĳѢʵҥÁпԛȕʿˣȊѣȉͼƇˈі',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʜʴ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ćбɹǪǫÅл?ĠŲȕԟƤƼɲƐơË/ӃʄƓ˯ԉÝ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƤŮ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '-čźӚŷɽʇ˄ʡ\x97ǕӜ}űЀ¢уœιČƒϘň˩ΘɆԢӭ®Ŏ',
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

            'name': 'ƦÀ¥',

            'error': {
                'identifier': 'ØXÐьĦ',
                'categories': [
                    'access-restriction',
                ],
                'messages': [
                    {
                            'catalog': 'ӎ?',
                            'message': 'Х',
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
            'event_id': 'âİÅϕRӌԗ\x94QʖϾ˕ϓЗɔĶҟćѡŽǛԀ¼шѷӽΊɝς\x9b',
            'target_id': 'ˊˣȜЫҽýнƷΐIγǓȿǦ@āʩÚЁҸ\x7fɨанӕӑԥψȓ\u0381',
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
                    'event_id': '˳ҁŬҎȨ*ӁѺöС*ʆ%ɱҏ˥ҖԬУ¢ØʊȯȄɰˏŋƓҢɿ',
                    'target_id': 'Й\x85¸ÒǁԀǠԮ\x8aɣèэÃ-ɴԝƦǆʜӀ+cԊùƴŨʉҘԪǟ',
                },
                {
                    'event_id': 'ƇѺA¦ǛԢúϮ˩˴ӗоѨˋӺфӺ«ȳj˵ɹǷ҇ʪζѰ˴δί',
                    'target_id': 'ȫЭčŻΐω$ȈѩΖʄĉEʵʌȆÜɃ2ЁνξʸqȖ+ΰԙEƭ',
                },
                {
                    'event_id': 'е\x9bȸƍǙĀ΄?ΛлҬûӧʥƜƞʗȇϨ҉΅УʊāмΙѰƌЖЉ',
                    'target_id': '\u03a2ЃZԑѭϚʰҚԖΠ*xЉԙ\x86іǑøьĎ\x8cEʮ\u0378лΉ~ƬŶк',
                },
                {
                    'event_id': 'ŐŽ/ѨѻϷ˪чПčāҥъӎϙ\u0382ԑģ˕ȁ÷Ɛ˃άΛΥрʋ;\x9f',
                    'target_id': 'ґǇŜӌˋȵԔ1ΫÑ2ԓЇȩЅÖ\x83^ЍΛǧõn\x8b}\u03a2щ¾Ƒɑ',
                },
                {
                    'event_id': 'ā˽ȖȃνʅѨȖήˎјΕӻԟӬ',
                    'target_id': 'ʸ{;ɝȱƚӫƭţπΙŽÎҜʩǄěČҀӶàџаǸӝʘҪΞΨ\x8e',
                },
                {
                    'event_id': 'юŜ\x88Ĝʧȯ\x94rҶ˓яɻa]ÖÑύӪ҅Ŵ½ÂʋɥҜӍϗȱˢ˽',
                    'target_id': 'ĉɦ\x9bèǥұԎϥÌѿьɘȺЈɘɥӝĳїȬѫƟє&įϊϭr\x90˾',
                },
                {
                    'event_id': 'ӖƋюvӴÀ˧ƒŨʉӀԚΪǿκψź1',
                    'target_id': 'Ư\x89ǔŨӗ·ÌͲƤЖ³gōɶƓƢʲ¹ɩȭƈӓТďʏŬрӨŷФ',
                },
                {
                    'event_id': 'ŪѮТ҄Ͱ5ǈ+ÍȄïѮ˻ãϺ\x99ßΤ½˚ԋáҶ+ҏӍǥѲ}ɂ',
                    'target_id': 'NĝˠҚǔēԧѥȌ\x81[Ŀĸő\x90Ԙ\x82ΦͼIƥχÇƓԑ˛ƒŇЧҳ',
                },
                {
                    'event_id': 'ʈĀпиƴϞаʆҊ˄ºҀԃҡɶς҈©ҕ˺ŏʙӝˋϙç\x95ͰĔȽ',
                    'target_id': 'Ƀo«ҩˁʧ˱ҳ\x8fӸӵŘǷӧêɫи"ŁΌѤћ#δƭѽ˲\xadϕ\x94',
                },
                {
                    'event_id': 'υħyǧȐãҜӒӈϵԐ¹ʕǘ\u0379źӓѾŘѢɥԆ+D\\ˉ\x9bӱϛw',
                    'target_id': '\x8fǢ°Ȫ\x8aα҅DƕQ\x93Ȧø˴\x96ɃźҦ8ʺŰ\x98ѯ²Ϙ˪ЛԒťɮ',
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
                    'event_id': 'аȐųĒȬѥӽƧǜǣμuĈȎʉҁӔǿɮʅɚǶӚӝɼΐȫѨ8ǩ',
                    'target_id': 'ԃӮØɫå!ƣɘŮXӳͼъԥƚȲьҾΔϡсΛЃԫӫɖ\x9cӽԟǂ',
                },
                {
                    'event_id': 'нɝƟԕ>Q˘ёŮȡˍÖ+ȭɏǱñʀūӏͶÉ\x9aĸċĿΘѡɁÿ',
                    'target_id': 'ƣӆӵ\x96Jńɜ\x93ΑȞ˅ɋȣŧȒ͵Ŀ9ʲÊϮȍͺӲ\x9eŭӓɟqω',
                },
                {
                    'event_id': 'ȳәǷ҆ŞϷӌˎȽĎΧWƯѶɍĮźС/ƾҕƙӳӂͷ\x95¥SМԭ',
                    'target_id': 'İ˵˫ϨҲNΤǦǓҴѤ˘ǼӕΞȢºLΕҳ»άҪĐ#¨wϧ҅Ē',
                },
                {
                    'event_id': 'ˌϑǊϛǗÞε˰ÅąοPϣ|ŬȽ\x98ΫǗƬѽӣnǥ\x9a˘ɭ˓˷O',
                    'target_id': '\x9cңɍϪΪцԍӥLϡʦǿʕ"ȸȻӸѻςϖȒҠӄÈӞĂѵȀɏʉ',
                },
                {
                    'event_id': 'љȟ˼\x81˫ ȰB\x9c\x90Сҝ÷˧ȁčǇπŎņƲƝļϨŕzθѻɿӋ',
                    'target_id': 'ӛĩȰ*҇ҔʇXUȫΏӘɉͷ˦ÒӹĖ\x8cӂΝҁīҸԄѽӉyF\x8b',
                },
                {
                    'event_id': 'ȗбёчʌԆƄȉʃķÈUІɶўҞǯʢ Ӟļtá;ʚ³IǥƲҽ',
                    'target_id': 'ҬĦŋΤǲȭ¸ԡӎӔѧίԌ\u0378ɺӍʑĮĤԊĜĺǂˌԐІϥӕЕŋ',
                },
                {
                    'event_id': 'ԆǖҦԕХѰњΦʍѠЎц˷ƊΩЇɷζңʁĬOŐǛöӺҔǦĵС',
                    'target_id': 'ԒβȵϯϑӀɋҨɜȦƚˢӴ',
                },
                {
                    'event_id': 'ӂ\x8e:ж˼˜˸ªŜϫȿȜľǈƝƭ˝ŞΧʩº˂ɔǲfɮˎƁɮϩ',
                    'target_id': 'ҽÀćǊҪφƈƔőçА\x99Ƨłɹȅ~Ȯɵ˶ԡɛ˦ŴƯЦ\x9bƪɖϖ',
                },
                {
                    'event_id': 'ěԫϬņ˚˳CɳȺЈÚ\x8bɁͰÃ\x9b\x80҃ѡҫҩŖѥ΄«\x93ҶҚŸˣ',
                    'target_id': 'ɿǧҀ£ԑ˞ЈÏĻȪʰȫŢй˴ҰʐĠ·Ț¿ӬŴʌŇӢɮ',
                },
                {
                    'event_id': 'ͺ\x95фϯԊƻ\x86ȦʮǊжĆlҴǖ˝_Ǒ˲ҎɽԨ˜ǼȧԨȤɥĖϠ',
                    'target_id': 'ϚȴΑϭΑîΛѺʿʔшԞŻɉ+ҹԉɳѮӑϼõрĂŴǌ²îƪш',
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
