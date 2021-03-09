# GENERATED CODE - DO NOT MODIFY

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
                'в˰}ƒҎȸƌΔŃEғƼұЂíɎÆЖИă¡ʞȧϐς˦ʒ\x9fΫȯ',
                '¶Æ\x85FĠą¤ȵñēǓ˼Ԕˇɒ¡îPԈ¨Ү˰\x9eˤFŊӴϿσК',
                'ƣ@ľŻǟ\x99ŠɫЃèȹҟĩȊʋӫƜmPòоϮӑàϷĘŪɘÂƞ',
                'ІĄМ]ɀZ˥ǧǕƄӭϸȓĶΡĥӧǹӕΖǥЩȺЙϳȌ4юeˤ',
                'ϳŮƸѥ\\˸ýŵƸΑbϩ\x8dćŢȶćԧӺЫąΐΠɽɅ\x87\x96\x9dƴԢ',
                'Ƀԛŝ¥АϗËˡͶWǯ;BóҴԤöƴѤʙǁУǽŖЄȡȕɰЮÿ',
                'ČǓĞбȽόìǭΨҖŋ\x7fϤȏ\x86Ӷ\x9b.ŭзʂͷpϷӬʠҶӁö°',
                'ҭȕƳѪԁŖUӦɡǛǬ\x81а\x9fӴԉ\xadҭˉÃөόѬ҃ĖѬҿӭČÓ',
                'ȵˈȡҿ˕ϬБȞʇӟԪå¿ȏөʆUːâˆӌ\x80˩Ӥ\x89!ΧѴÚȳ',
                '˷ҤΣφœԎɗϺȹĲŔʮɘƓũǩƑȅɬКӠђЏǟАӠɔ ϓĦ',
            ],
            'source_id_prefixes': [
                'ǜuƌҕϳr(mŻԀʧʡЎËơҙǁ\x80Ćɂδɼĝ2ºӐҏȩԈC',
                'Ӛ.ɤĀԠѵēâǿ\u0378<˹ȱĶԛ\x98хʫĆуʵȺǠŻ½ˢҼʯ$Ҝ',
                'țÕіÙ.Ŋ»αȄƳœæʜʊөЯçȐˀZˮƞϰƙȄˠѓѫöћ',
                'ʶѧłԝlˌӭʯыԣ÷ѦѨӵϼΏ»˶ȎʂȄǊЌƝ*Ϩ)ȍтÜ',
                'ʿļŹİȡϯѫĚŋťСɅжſȘӟДАңŵƩȰʭǴƳ҆ūьԖÈ',
                'ƁlΆϱà\x83хř¢ĜΤą·Ԅ\x96ƦӕȘ˕ƵѺƢȨ&ƚԬȧģŝN',
                '×Ć:Ď"˸ļћˬϵϴøʑƝǎɈbͷӜȜs҆˨\x9cмǸƟϾɵæ',
                '²x»Б϶ҢҊȶӖ\x90\u03a2mɏҋЅ\u0383β»ϪÏɡУǯӵŝĸԇ˂ȯƾ',
                'ŜȫҚʳӳХƒǨǯƘςӻʝˌя\x97ȎвѺӽǼԇȡÓ¾ͻȪuкϏ',
                'òʚʍÀЗӲǞˢɛ\x9d˖ϻş\x94\x99ӖχΏԞвжЫθќӕґҷӾĄĩ',
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
            'action': '\x84ǣƲǮХɊìƷҳ\x7fȸª·ŨűÎЃ]\x90\x95ЎΔϐčѴ(өŷʭǸ',
            'resources': [
                '˔ŪÌ\u0383ҁŻȢǛҺ˼ͷҪʔǞɖÄǰӃɡŘˆɂɎɄ¶\x91Ǘł\x87ϩ',
                'ЭóOƲрѶ6ɎӘǽјƩűĻ\x8bѤ;ȏΥΗ\x9fəȍʌȶǇћ\x8f{Ǧ',
                'øǾƜťПЍǑɗşƫãɘŹвӴ¾ҘƟƀѬΖƜŐċ¤ϼόʑΣĿ',
                'ˏ~ʞ\xadϧĆіщ\x8fΛŀ®ΏíӖӆŐĄҌӮȞ˼ͼǮȨϔͱ҈eõ',
                'EńМğΠΚΕӯʽͰҹʼʹʔƟɖǄҺԐά҄\x89РŻҨʳșˈΆĀ',
                'ǀҮȠȽŝ¤¯ŅáшɽĢjгӇЋɬˉƣ\x9fҔЭVź³ύԜȜɃğ',
                'ɌŮЯȢϰϴȠɞHҮɦ`ðКώѦŖȓӜӨ&ϰťϻʨºȝ˦Ѝ˰',
                'ɶ˾ˍԧĵ@Ϊ\x83>ˁføԂѻҠӒѼсϒ˧Ͽ',
                'ɆÔΈUǬϛǐΈFˊǃ҇μťĉϤˠʾ˝яЯƿřȣК·3ԇȮĨ',
                'Ɋӊθʻ˞ԬУν˯ΣƾѺʽӑϿDƑϼ<ΆŉƟ£ōҪɩ˜ύΈɛ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'ƺ',

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
            'name': 'eªǍƾН\x80ŲġϦǿʫРDαƀĨɺҜμ\x9b˰Þǔa¦ҟÔяҘХ',
            'version': [
                -944577289118099214,
                -2585781947831136543,
                -8162258998584991515,
            ],
            'location': [
                'vʉǑɕɍӅϝӜ¥\x9bˑ˘ȀҷʯƚԜϦѺчɀèϲ҇ҥǍΉɜøϨ',
                '˸Ƙƞyŭ²НѻŽӋʡ\x88\x85ЎøΰƋҸɺңİďƽҠѥѥPWԒ˩',
                'Έʉ7ƳªĐϞˁѰѐ˛Žà´Ÿ˄щϢӑUɜɑ¤ɏƎ˞&~˵Ӣ',
                'їɞĖ\x8bƬÑΑ¯ˬϝ®ъʴӁTǗѥŐǄҘŜǻԣƁԚѬǩӣ҉Ʉ',
                'ԅʯȗAҋÇȑˁϢ˧ƗϷǔǳʇǸӇɞǎɅѸƔҦӀʄҮсХʤѻ',
                'óǪĨѹɐǒ÷\x98ȲǉĀôǬɠœθǯMưȲӅ@ϾʩȓˍРäͻđ',
                'ԁϸǇɴǉяΎĶϣcөúҪSӨЅɥƮɟ\x9așƦѝλ¿ɋǊ³ϩǷ',
                'ĜԌlӆĈ²ӼĘƁŅåǔ˱ǎŏǰɓ˱ƙΎνқʷƒщŉȺӹҵ˱',
                'ѕɀʞéЄǆ˻ÑƞҨǲФϗƵ˸WˊМɜʰ¯ġɟЊӆʪд×ʒʵ',
                '«ͿďԘϚƦ˯®ĒЄήͱˡ\xadˎƓʧɜÉȴ҆҅ѴΐӃҴĬäӌѐ',
            ],
            'runtime': 'ŲЅ\x98ŒǴʹϺɍðϒɣ˴ƆӠŮƱΓ\x99Ȕ3κɺđЁ\x9dʃӥaЇ¸',
            'send_access': {
                'event_ids': [
                    '\xadȍɿƧȫǗӠԞƼťΣŎұɝYˮeT®ϩΨtǘӵ\x99ԑҁӷʽȇ',
                    'ƾәҡςΝԇ\x7fμϻѐӛӶ҃ԣʼˬɬ˵ː˘tɢέǌ\x92ʧƫŦ˄±',
                    'ɞҺü˫Ҧϕ\x8cǥȘǲƱϷҡЙʺƧɆˎԭΠĮKģĆħȅȥ½рÓ',
                    'ǶÀϷфǒЭѓǼҩʄɞüԖđƍ˥Нԓŉ¼ѣkėϴǪҬ\x89ʧӐа',
                    'ÏӞѪйҌƟfЩҤYBЋâɬʹυӉѬ\u038bσƵŽÜơ˱οÁȭϡƎ',
                    'ƿǞ·ƁӨɝÇНԌğӴöҴK¹Ʃţɫе˙\x92\xa0ԠʯԀHƃΔΛc',
                    'γŇɌjϫȵ\x91ɤЉǠïҮϐ-ЀϣԥƺӝʭԄćƸƛáʥλ\x98Ϣģ',
                    'гεԏǺϳˣȂʪʠ\x9cˉŢӞiȨӗнӏ҄ӧaӼǾәõÜћņTũ',
                    'Ԁ˚ɽУԐǎԨÊ˝ƻ҆ųȯ˓УțʊԗɲěӤɡӉͻԨŽҼþǓЮ',
                    'ʼɐТˆҖӲԫȴȹȓŕŮƴƮÜȴȔϖΒwѐÁҪÍҭʡ\x96ƌ˲ϐ',
                ],
                'source_id_prefixes': [
                    'τŐԧčGûбʬҼ\x84ԃѸ·Ƶ˦ȳȌԂţ^GɓþӊęS§ӪӁϡ',
                    'ƃӶƽЂԈ˖ȇЎĺғˁƒˆŞӳ\u0381\x94¼Ⱦ°ђƞǜӡŶǤ~ϟ҂Ē',
                    'ɶɗLiũȉ˷КҷΞ˸ʑǹѫåŭƪȨσʐǓͰ[ŽƏԕèßάЯ',
                    'ʝŪɯɘѷҭ\u0379ќΤϙλԪǸӹƒѧɊèǾͷƠǋʺʧȦÁZ®ȧɗ',
                    '\x97ǔ˯їʶǓ«ӁҔфњάĝӐƕȏӴъй¢ұΨѠáɵГśѠ˙ǃ',
                    'ƧƮʈкԤÈѻиŜȌщȁϞǉҾʣҏˈʨĀƐǳӞҌΕʂΝ\x96Еŷ',
                    '˅ΟЊɕƇŐԃĕʌaϫȼҀҁɮ\x93ʌȏӒѮƺʰÁǏ\x87ŗ˰òËȖ',
                    'ЮҔѲĕ\x85ǗƾÈŬԦ}Ғ˳²ʛӕϋ£ˣEǑΆӇǍuΊҭƗѩǀ',
                    'Ɖϸŭɵʪ\u038dȶŕѵϕį¥=ɜȋҊÄƵÖҟĔťʳǳԉӒ҃íȹĸ',
                    '΄°нuȥΦɰăΈӲÀԢɾǓ-ĩҫάĢCзūϤɒӡɠ&њμĝ',
                ],
            },
            'configuration': 'ζˌŭӈwĨƺҶ˸˽ϐĶϭΜʷԘƇŅʃԬǁ¸ɀˊ¤¥\u0379\u0378ѩϟ',
            'permissions': [
                {
                    'action': 'ԖϸҾûˊҙǃҭćǻʢӱ˹Ɍ˷Ԓq˸ɒÕӌĂχʞņΙãϮǎĺ',
                    'resources': [
                            'ʨýʘѪηπѼӉҋßūҮƯљɡȜΰяL\u0378ŜΟďҪӌĀ˖°ªÜ',
                            '˭˽ȫϬƴϣҀĭÏǭПÓƽ\x92άыȫŲĠ˅ʍтќǯ\x8fʇƬƎòϜ',
                            'юɬѫȎʂ\x9eԦĊȾì ԦɯǾȱҚӵԁİўȚ˖ΫʟŠɇƈʹ¤ъ',
                            '»Ҙ#0ӄҙАӎӄѲǧƣŰʡӆѬƏęDɉ˱јʋȋӁǻҫØúǩ',
                            'ʜ)ѱºƂґɗщƈ9ӅþʸчдɲǩԐϤģ˞ţʼλ^ʫɀȬfͺ',
                            'ĆâDҳЦǞ\x8f\x9c³ɍƍĊԧ£зԔǾč˵ʑӿуѳ^;РΐЬńœ',
                            'ǜȵШƸϠɛЍԄɏȼҩÀЉϘĵß˾Űήgӑʍӯĕ1Ƭř΄Б«',
                            'ҴǒҒҧǞǻЍ˳ƺɜɻЋҟΣʂȚ˥ɛʤԉgЩ˨Π\u0383ϒÍŀͺԮ',
                            'ȜʌǹșηԮҷ˟\x9dĲӹʊґҫȍTRĽưӸϓӦī˫șӆͽňӄν',
                            'Ԙԗɪϙ˴wƞввʻ˪ΪǘǣƊƞζεɥԅΏӏ¸γѿϐ?ШЌJ',
                        ],
                },
                {
                    'action': 'ΎԨŤŉԎȲƒґԧķС4ŸЕʶˡҥӄӘġӰѲʚʩҰ\x93ƸϾôʯ',
                    'resources': [
                            'ɋʩÆӭɺдҫǪӯŎԔԞêŷœƹҙÖʤPΙҮϑɗўϒɶу\x90Ԯ',
                            'ʳƄƙɱǣŒĢʾ˴ȁɤƐˮҭ©ΕƙÌțYIhɏɥγƤ»ҼОȜ',
                            'ӯѾѤϟɰőǾӽ\x99ˆ˟ЛȺԌąǼ˳˖ŮʑůÅˡԡμђфőο"',
                            'Ƀɉ\xadĉΒƀňӕő¨ƼʂǸĮƚӻ\x8dѵӷΛџӪҿĀѤ½ĒÛ\x89ѿ',
                            'жȼɘŤԕYÅđĉůˬǾ҄гӀƼǱƄȔø\x99Ώҭжǫ4ӗȇċ4',
                            'UѥΰѤȭӐsςξƟſʇИԭѮǾϥſыrϺ˘ԏр\x82ӵ˙У³ʒ',
                            'ɛҀŖŴˮƮěӌ¹˹ӥЂəąȹΦрŵBùКƀǥϛğѷШIƝú',
                            'ӚȦñǠѰӵ\x95ҾϬ҆ˏʚξòѿòԝŬɭȲʟŀä͵ҞԐ"ʎԖƯ',
                            '(ϩǡΓˣɣłҚԡŒɏўԨÅΜ˱ȣҥƯéӮҸ˞ɛʌԭ\x84Şő˭',
                            'ʂǏ\x8f2ǌԛįΆιĝ\u0381сʑφ.ȑƴԙˢЏȔɗÉÍюȌƛΦņѼ',
                        ],
                },
                {
                    'action': 'ĶvīǶѷƗ҅\x81ӔƑϏĲӳÊӽǆȒϬʋȯӲD"ǜʢȅɲ҇ұĝ',
                    'resources': [
                            'śϚюԙяФҞʙźŽƣȬÊҦäЅφģƆʼȿҜȦÓǪɐřƠʄӲ',
                            'ңԦяˁϨ\x88δ˴ӡ}nϭѤ˥»ȑƘҾѽĦ҆ĮСɋŃÜʮ\x97Ǻɻ',
                            '\x80˽ŭЈξɩǸȄŔȵn˪ʡτŏЃĨԗʅʓO˨ɖƴϒкǑё¦ƞ',
                            'ʭĿҒ˅Ȉ»ǛH£əăҬɩͻΦǂƘʭӁƇyðǌˉϒӠÌʂ¹ё',
                            'ЅŪԥӑǉϴͿΔʥR҄ èƌɇԣΞ˙ƵҜɓХźłǧˣĹěŃǗ',
                            'ōʉȑӏϊģˏ˻ҬʕӋÞȢϐв&¯ŇĮ͵Ǝ\x9c¤\x82ҤϘ˸·ϼ\x8d',
                            'ӦԊȀ˕αϰԍˋѲßԧȔƛЍȅəǈҜΚǶdіǱĆ\x95{Ϡā;Ɋ',
                            'ӣȸ+ǭ˒¡ʑȄżƃƄˠʂ¶ӜHДŀƭӱСȲ\x9aĘѼTԝ¦ėç',
                            'Ӥҿʎəƴ˲ʰǬˢҏғҥɥшѿōʠđzǂïÌʧÓ¬ȣÙÖɟə',
                            'Ѷi\\ϧǂőìѳЊÏ˱ʽО$îŬĻȋϲѕĩѯ;îƗџɃϐΡʥ',
                        ],
                },
                {
                    'action': 'ӪțϟʣЗʄԇƏЩOŢǏǸ?ΆʶыώĭΔʪƖҳÃʹðĹϹӳҩ',
                    'resources': [
                            '©qPρǝķɗʴǖВʣͳǲȫμ˖\xadԞʴӳӺКͷȴԦѨѪŁŇй',
                            'Үîǐ;їʡƷʲʾOѻĹεҠюɲϛúƒΰŜϤ˟ɀϸ˃Ҝː#ú',
                            '\x8cѓȱǛΒϨȴҗèȰƫɡҔϫϦ˲¾ȋ\x9b˵Ψ)ΗķŭΎZōyɇ',
                            'žțӨƄaŹ',
                            'ƛǣßǉ~ϑK҇ˇ\x87˛рʳȞ˄ԀȒșķĔǑźŦʧʣŏєʼΏl',
                            'öȒń˒ŊƲϋȚѧҫʠӭˢĬ˜\x98ȟȀѪч\x91ǶǬ¯Җɞɟƒ˹Ä',
                            'ίǝ÷ԛř`ǗȂBħǪOĞ8ɽǠ÷ηÚƺʧlƿĄķəú:ʁ˯',
                            'пɢģЗҏȐϸ\xa0ҚԀҤĔƣҞƥҤӰұǱȺ҆ӛāӾȺɩϿ\u0382vŀ',
                            'Ţéл˫ÜȹшčėˋĮʘԍ\x86З˚ƮĚɯöĀ;ȫǝjϳʡ\u0382ˎY',
                            'ʘ\x88ϪƄаɱ·ԦõëȳčƵӊлȝͼέхђȀɱȬſ\x9eпN\u03a2Ʊĺ',
                        ],
                },
                {
                    'action': 'ˑƿ\x95ҹйŠҺςҼԡÊŐǓǛќËŉʅѲ§',
                    'resources': [
                            'ʗǻǟяӭȪȕЛәǢřӘ[ʸ\x9eӴԡčԫĎӚѷÕʫř΅ςĿÐƊ',
                            'ƱƖѬ·ŲŐĉʾQԛ҈үҪМͼºτǙżʤθӺĢŷ҃¹\x80ċԉѬ',
                            'ɢҿԈ˶ȼˠhϿƦГÒηȎ˗˞ӹΙƥʫő\u0380Ԅґ¥FˏӨʮȺķ',
                            'zðΫνҪҔʳΩǮ#ͿѲå\x81rɕ+ʼԇȘёйɥҔӏȹʆnӑɡ',
                            'Ҹӆ˽ϣέűАсǑŕӄϳ\x9f\x9cɴ҇ȹϓ\u0380ÄßȠӈ\x8bǠĘҲÞʔѤ',
                            'ïɝ&пÔʥаΕ˲ØʕϘƒ¦ԆȅʬœǔǽѶӳIȋȝάҘȷĉÖ',
                            '\x82ȴÿѯϿúɳҗӣǉÀţːÞĈԖġԭѠή\x8eΔӭѽԒ\x98ƟǷϲŏ',
                            '˥λʗɥԃҾœ˝ȷԁ¹ʽïƑӪʫҧҏφƁǌʓΚҒӅλs΄ӵѻ',
                            'úīɂāǻǽПƦΆɠæ\x89&Ɲģž\x80͵ҳǬʐɦɎÑҕÚѴѷғ<',
                            '\xadŲˏѭёǎĸǟɳİȥΫȩяԓͲ8ÔƍɷŊϡђͶQèäҺʜԂ',
                        ],
                },
                {
                    'action': ')lіƛɓ\u0380ɆԬкǭʏѫϹҭéĒȮìĎ}іҩǶѸ9ӚCŀԢν',
                    'resources': [
                            'ȾȖƝŷЧȽΧςŤӍňăɵòιтϜĆ÷Āæ#UdѴ˥ʹ\x90Ũɫ',
                            'уҹϟɧWKŮд6Ä\x7fѾŠԊЁǧǛğ3ɳѶэåϺ˼ΐǀĴяɊ',
                            '¿fӳƈӁÙʗҳćťɓ6ɦĂ§˻ϗ\x9e»ɀԊҺϱѺéËӠдĈÛ',
                            'ӞȓŃȻǁǀsПλɢźơϹʸҗҙѩɞŊɗʟӉӹΙȠƼɂѦ:Ɂ',
                            'ɗµ҇ȢґΑˍȓ<όс˄¸¡ņʔͷİ¼£ƮĈǼOҗͳɪƙɪͽ',
                            '˗ɶN\x9b+ӷњԌќȀΘЪӧgβƚÞ·ƙѨ\x98Ȝ˼ʿдË\xadŔƪʯ',
                            'éʎ\x8ay-\x87ʵӱѿ\u038b\u038bҤƽȔԩ˭ÄқӇŉүЄǠ',
                            'ʚ\x86Ӎ\xadǙѯіχʱćʮƔʶÌхңΞȹJħ\u0379ȻŧѠҷːŦɠҪʂ',
                            'лʢήʼӾћϏΚȄɭRϳXƄĐ϶ȲȻëŲӏβƙξ҆ţʡЏ»ԍ',
                            'Ы˸сƨɡúˌȚś>ƙνšĐťƽӀɿʟąûЄɊÃƔʏѸżϛз',
                        ],
                },
                {
                    'action': 'ͻӱƼϭ7ΣϩӖ˻ϹTT\u0381¦ΚτԕƤ˭\x9abҵΥɫSĊT˝\x9bƟ',
                    'resources': [
                            'ɹΈќʑƠǮҏK\u0380šӸԈӪ҈ϦćˆӁʙĬɭˣȊ҅ǱкҥŻ³˶',
                            '˚ʮϫΈȧȔȵðĉĊӥɭԎ6ˆ*ơМҬÐLɦȷňȬȚ\u0382γ³ș',
                            'ˌ˟ϗǠx˂Ͱþ\x9aǈə,©γʄғæȈƤȪ˺¯ɕҿjŃϟϘͿʳ',
                            'TĠǇěĽԝˊ˞\x90ʈΗϩϷуŖΘÁРʡΗȥҦĿ\x9b˳ŅǀЀ΅Ԕ',
                            ',ſҞЅcχʏqŏѝŀšȦAƽЪΐāϡɎ˱¶±ӟɍȜɤ´ȅȁ',
                            'Lϐ4ŸϵşͷӇ\x86ɒíUøŉ@ƞаɐѓКбɇʋ|ǧҚĕkԒǟ',
                            '4ɌѰƏǈяŃѠ˧éʀď˦λЅl*кˠzÖȼǹ÷ҫǉΣƻӕȈ',
                            '˘8ЊʫϖЭčvµɋʛѹʆŗл˱ŚưĒаɞΪҌǩgʊӐöɝÔ',
                            'εҫʧʅİҝ҆Ƣʧʭò_ϣϮЁƓ\x9bŮ+ќıӶͲƒ˲ȲĽңʧԚ',
                            'ЍљʢŦҝȪɩƒҢӼƏȁԓҳʒұѼχ@ɅѴБĜˈĥȔʖǇ\x9fƃ',
                        ],
                },
                {
                    'action': 'Yo¸ҨЭф1ƞSӖΛiī«ΑȍΛϓ"Пʋ\x81ÅьɵҏӦŔfѬ',
                    'resources': [
                            'ƨ÷ʐԁŁŻϐëʫʏÎåϕЪWί҂țǐɍǈʹɓҚˊӮҥԕÅЍ',
                            'ЏòʅϽİėы3ˠƣԘϓÔĺˏӠōсɳæҔċÙШCΚ´ǂɹǪ',
                            'ԋʅІY˸˳ѫNԜƨÿ)ÙtċĢȾŘɓ\x8dǣ@Ţłѿζ\x97γҕ\x86',
                            'ɸAӥӯЙŨ?ǹȰɘʁͰΊrӋƢɡԥŨѕѥҼΣ\x82ȅǂŷɞҭʡ',
                            "PӒӘàϣϛWɝЕȋǲʸɼ'ƧŸУȪôgʰǶʴЕ«ʯkā\u0380ƈ",
                            'Ũғ7ƞǞŨTŭǂČӼтýΠ˩ǎԁǸìˇoǙôӘüА\u038bƀȳΔ',
                            'ҧˀÔѺȗƘ½\u0380ԀӟʲǨßӕԇ˗Ǟω˺Эǒōԅ¥ӈϓ\x87ʸӀÜ',
                            '҆ТԖoЛăКԎ9Ҳԍ˜щȻУЪҶӇ3ĕď˒Âϙќ¡ӴʖÒ͵',
                            'ʚʳӂʀΊǞœӋѱ\xadˢɵĎζĲŭоϧТŨӵĽ$ҞŸԔΊoȎӨ',
                            'ˁάѥѯŸϦȀŢɀǆԉԞ¨ϲĎƌʆƳ҂ɷĀФ˔ʞśǐɛӫGĦ',
                        ],
                },
                {
                    'action': 'IGЬұʈȕ˜ĽFӏŜȪΣӟ˚ͳOˊ͵ʈšÓQϋ˪қаŲӎԂ',
                    'resources': [
                            'ΠĴԄɔʂƂɂȇ ßlɀʄʠЖѓӛңçŠÝ\x91ŖŇĮʒӑ¬\x93ў',
                            'ʥƗĻԛǕlʾȆÂˮρǉƺƫѓʥΤɐǁͲüԉԠљŴńҌͻ\x88u',
                            'ʆѫоˤӲŒјΑÌΜЧjûćυş˒ɱОmБӴ\x84ЧōфҀwǧθ',
                            'ͽʑÃŹτ4ĊɡʨȰłά\x7fҜȌo[ѴʻʚáʓɶƯʮĐ˂Ƹʘˁ',
                            'ϥʑҤŢɑȰŹƳʈɅϣĹĀɵи÷ÖȁʰӽҧʢǊȦʙҤθĎӟƹ',
                            'ɀmȑǀǪǷƥbɕΡ`ЮĿ£\x87\x90ʍŉ¯\x81ȯԊŽҟƍ?ɃʃÉϟ',
                            'ёҟ˭ȁɅϜǹ˝ŶӵʴũԠіĻԅɶÎ˃ԞԤчıӭʏĞȜυØη',
                            'ǡ(ʃʈȇϜҞìÅ\x88ƼǦΩӗђΝſǌķӒƼǍɄiʸaπαϳѓ',
                            'tӃɅ˷Ī\\ɑˑ>ұԖ*ҐϽØϥДʱУϥʸΥ˭MԧϣԫŽΘš',
                            'ɢ¢2ɖóƀʟȟӆǯÈȹĨĉÏˏ}ǅϿ\u038dȷυӼoƿʘĂ',
                        ],
                },
                {
                    'action': 'ʅӡš˗ћ)ҋТϗ\u038d\x96Ǹaϝ¼ʲѰ¼˟a0ņɼʒυϔцԍ®˻',
                    'resources': [
                            'ЕΧȹԎЫɩ\u0382ѨƷ4ƽϘĭɡǏǌѳƇЋǣԌ×ʎ\x7fӄʧǩͷ˾Ĉ',
                            'БDƫҊι4ɟ/}ƒ<Ѱ$ɵŹǞȧɿćԖ˹ύϊļŝϦűʉϧϘ',
                            'ĂбǥɡʵΌОφφɯĎʑQǗ\xa0ӉØɻқҟѦӕ&ԙЊ˘©ʑҪ7',
                            'ôУ҅ǣǂҔŴҴ҅\u03a2џűϯˁ3ȬsҟЬӇ2żȑϹыɠ\xad҈πʑ',
                            'Šß\x85 ¿ºҟӒΖľˤú¿ƮåȑӾʐс3ûѢҬɫшȏςϥɸǣ',
                            'ŝ\u0378ǑįȵƨʑĻňʐŀϣсťǝǍɝˑԠȔӴʹYԀЯѤцɦɰɭ',
                            'УĖ_ǞɯʋȦ˹ӥ˛ԟфҘ\u0378ȂгÎɢηҦɊϻ1Ψ°ĎþвaӔ',
                            'ҏ\x92ɻϗƫ·ԠŹӏ\u0380ѱŉΆ¹ү\x9dl\x95ϊεɁȶ˳ƢȻӅʹҔAʈ',
                            'Έ\x9bȓӵȬǤϲҙέſΖѲƵǗԨЦýʫÐȋļWˌʥӚ\x8bʟӜŌʡ',
                            '\x93ҪРԤΥ¼ƚшмάҒϕԭӸFÈҗ҂ϡiѷ˽ɾƃ\x81ΝԊɈѭě',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʪӊԇ',

            'version': [
                -59987721231915468,
                -2726506723282594942,
                -1075345030030959181,
            ],

            'location': [
                'z',
            ],

            'runtime': '6',

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
            'name': 'ӪҢӱς°ӓưбѸÖ\u0379ĆҝӀ²ˍʧȦƩӇȩłľЍβʗʁΩɄ\x8a',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʉɉʩ',

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
            '$': 'Θт\x7fґğŶȹüÍ\xa0ǆȐǻǤ˖¯ȳb˹Ɋeǆ\u0382Ƽχ$ȮǄőZ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -2571930472902449388,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': -66280.0342048026,
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
            '$': '20210309:034921.489690:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ϜТԥɱɨξҧȢžЊĎԬɕŻÛİ˾ϒǗϸ=øǨ˱\x8d˻ɯBď@',
                'ȮӟϪЋџɴҋķҍʃŠӾŖõҴʢĔӜҴԍUʙΉӒϨѩƼϘ˪Ӄ',
                'ʁǃĻ\x84Č\u0380ȝņÜˢԏ˓ŷƸϓ˯ľөԦħ\x8f\x8bŔԠȑӮѨǩӏȈ',
                'ðҶԒǠtҧĨƕпʵԚӴԛȃԒɓȆͱǔƐńʕЫʬϠ˯Ӎ«Ͳԣ',
                'ԜίÊԆǌѪЀfϧϛГˢɌŅʤĮĎÆTГʻęȺţΐʁʱƱӻϹ',
                'śʜźůŽЇӨaЏз҈\x9e˴ӰТ˜ͱ;\x8aӤʢ˷ύϋǅÊĄ;҈Ò',
                'ЁÜĝǥȔ9җҜʂŏϗϓVʧԍӎ˞ɣǡȥԏļƩĽΆʈ˥ȥtΆ',
                'ʅОѱϚɍʩЪ˽ʍƖˮДәϾɱǫƭҕ\x7fj±¤ȓĺ˳ҴʄϹ1ԣ',
                '7ĭϿъˢŅźΠѡЅ˜ɻƬǸʔȖŒ҅\x92ʅжΨǖ˛ҡЌˎТԧӓ',
                '˺\u0383Ǒ·ǠƖsԩԠɢӹy\x85ϐȬĬȓӜƨŨűˮѴԒΌKɫɨеɎ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                1839481539404977915,
                -3684773551748354193,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                257520.3090255502,
                457883.63754461484,
                995212.9336310923,
                868827.4876016122,
                30223.584206010783,
                832060.2788895513,
                698466.5579205431,
                307559.0492378761,
                -79536.64144638779,
                273215.07054931973,
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
                True,
                True,
                True,
                True,
                True,
                True,
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
                '20210309:034922.266431:+0000',
                '20210309:034922.283570:+0000',
                '20210309:034922.300754:+0000',
                '20210309:034922.318952:+0000',
                '20210309:034922.335874:+0000',
                '20210309:034922.353708:+0000',
                '20210309:034922.370808:+0000',
                '20210309:034922.387466:+0000',
                '20210309:034922.404915:+0000',
                '20210309:034922.421518:+0000',
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
            'name': 'пЍԅ˅Ȋbȸ&¡ɺʰǟƳӀȝrɁɶҫ©ȁ/\x9d²(Ѣ\u0379JӗЎ',
            'value': {
                '^': 'float',
                '$': 814732.7231460247,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ɦ',

            'value': {
                '^': 'int_list',
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
            'catalog': 'ƹΚƵĻ¯ŴċvдПʣԆáɞԔǥҶШѡΟʝЦ\x9cǵҴáһҍǄȯ',
            'message': 'Üѣˋ.ɖµҦǛ˰ƚ҃ͳѹԝ-ǅçϯ˕ɘ_҆ʽIґè8ŉŋҭ',
            'arguments': [
                {
                    'name': '§\x84)ȢΌ˟X»ҨΔԮ˹ӶʒÕĕϬǂxʐǣɂɖōĹϻȧԮʜ\x9e',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'TҳόѶÇŗϱҫǞәȡ˥ǶαŻѯϺäĠ©ŲƓͶƦƕçϯˎȲc',
                                        'ŌMǻϚØЮŋɀԂCЉ´чʈʎųВӑzȟœϗӠʿΡvԋ΅xƊ',
                                        'ӶҘԚΠīԣ@ɌӻҜPˊ¨ВӀнğήɭѡ˪¥ĽɯΤϳʟԩѿϘ',
                                        'ʞӾԤĞɐĲрʡ½ʧƚΉĈӵWñƨҳΘћőӞëӍ±ЈƿˍŲƒ',
                                        '\x92\x7f\x9eĜƧѵӕ\x83ЩҕȆhȻɜĘ×èѵʮÉ\x93ѷbԁϹĂοŴżv',
                                        'њŢЯ҂ʪ\x91ȫ@đάŷȪ\x8f˵ÙɎ˰ӾѱìΨĮŨȬӥ˫Ӧԩƾʍ',
                                        'mΓϸӀĕӆЄǼŶq\x95Ɗ\x89ǈÄŁѠƘȿǼŭ˦ѧą\u0381ϝϠϻʔ²',
                                        'ĤĂ˝ϖЎњùΟȃʜ\u0381ϱRɩǺΐɽʩǵԊ¶ɋǣˊԘÌƮȦΕȺ',
                                        'Ͱʑϕ\x98Ǖϖ:ԒΣĖѲ¹ƠªХԑϪȞZÚԍǝ˕¯ÌǵdǯȡǷ',
                                        '\xa0Ǉ°ЊʫΪ(¢РϱӽĦ@ӰƄǲ˞˹oҦÜʢғΒʁȐԘƐʖr',
                                    ],
                        },
                },
                {
                    'name': 'ξʅɥăϷɾҺ°ĐǠҎÉȻȽжƧyА',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -843919183964379854,
                                        -669506427173467810,
                                        -4823758032121158150,
                                        739885466599362829,
                                        -6497855808218616117,
                                        5801209395814202481,
                                        -5897892530785225061,
                                        4512717488751194103,
                                        -1097817584819351496,
                                        5836347813842066686,
                                    ],
                        },
                },
                {
                    'name': 'ΥһǹǏф¡ЋΦ\x98ǯÓ^Ѻ\x8cΥųŚȝςŲnĚʨƀċƕµŬZϤ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        3251419623424645010,
                                        5451288249482410552,
                                        -1298629255327858410,
                                        -4716199035353510267,
                                        7010908145161295757,
                                        8843945454095462091,
                                        3238284816697776530,
                                        -5584675963439048068,
                                        -6346948952223533090,
                                        -8106095976512953633,
                                    ],
                        },
                },
                {
                    'name': 'ґԟƢ',
                    'value': {
                            '^': 'float',
                            '$': 756159.5549792792,
                        },
                },
                {
                    'name': 'nыįȚԧҴъėĄԗ{§ćѾʴԫŸÓĴ£˖ġɛ˦\u0380ǲųƖ\u0382f',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210309:034920.186521:+0000',
                                        '20210309:034920.202553:+0000',
                                        '20210309:034920.219176:+0000',
                                        '20210309:034920.236335:+0000',
                                        '20210309:034920.252395:+0000',
                                        '20210309:034920.268566:+0000',
                                        '20210309:034920.284772:+0000',
                                        '20210309:034920.301993:+0000',
                                        '20210309:034920.318864:+0000',
                                        '20210309:034920.334864:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ŮĊŁхK×ѕʆŢɦȿǉӟӜȮШ҉ÖԄįԛŚϜ4ǡ®ԇ\x8aTȂ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210309:034920.417201:+0000',
                                        '20210309:034920.433309:+0000',
                                        '20210309:034920.449361:+0000',
                                        '20210309:034920.465704:+0000',
                                        '20210309:034920.482166:+0000',
                                        '20210309:034920.498615:+0000',
                                        '20210309:034920.514804:+0000',
                                        '20210309:034920.531627:+0000',
                                        '20210309:034920.548888:+0000',
                                        '20210309:034920.566073:+0000',
                                    ],
                        },
                },
                {
                    'name': 'Ӹ]ҿ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210309:034920.656871:+0000',
                        },
                },
                {
                    'name': 'Τэ˃ƼӰρϼ&ŹöɾâǾȀѢԘ\x8dŧŤ\u0379ʕϺĝʹӻȲpuύƤ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'хě\\МӕÂŪѡɘ¢ǖԚÞԩ\x8aϵ6ǈ˩ρȞŸʂÂŰʳ˧Ұ¾\x9a',
                                        'ĆĚѐʣýϜϬ¼ԎǍĉʜψӈǍ;°ǢλЙˢĲԂǘо¨\x9cŀϣЁ',
                                        'ьđˇĒ¿ɉɩǃьǔ˷ˌԨЬԋȰ\x9eǂŀԕґƊɱԌ·ɥĦԧ˚Џ',
                                        'ԩɮȲь[оʲҀёȜqҐ˱б}ͳ0ыɳÒыпȂU˟¿Тĭсļ',
                                        'ŞŒҵƽĩƛ¨ȴϊß¾ũӧÝFüҶgӎʣ-ϗ#ǣѲoӿˊѴƋ',
                                        '¹˸ɑɻɧƅ˼҂ѦөȞĔД˯ңĝϲЀρâÀѓĹŞɫѲ;ьʴ©',
                                        '%ˀĊϲοˮÝŐҺӫƚȪȔΚщҕџԖǚ˨ŧϢϡЌ˸эŜКķʵ',
                                        'ąμ8ҎӾjѯɔ(Ǖ«ʦѢǓƼ˙Ņ˲ǄдҜΓΗ1½ɘЩƺǝв',
                                        'ʟrˇӭˀǏμγƹƌЏϡĢϋ<ȱˬúф1ψŌӟΧȁϡΥ˽ʅ.',
                                        'ԗ\x81¾Ǝ~\x8f¦ҶQƸхϮ\x82nǩǩĲˍ;Sϑèǽ˴ɝƯvʒċΖ',
                                    ],
                        },
                },
                {
                    'name': 'ƝʑŠΤқŁѥȧƕŕɧŖӓӹҘҾ×łǅιΡʉЇ®Ķӣƴ[ӥʈ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ʱͽƊƭĮ´ɵј',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210309:034921.013927:+0000',
                                        '20210309:034921.032251:+0000',
                                        '20210309:034921.050037:+0000',
                                        '20210309:034921.067730:+0000',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': '˺ѐ',

            'message': 'Ç',

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
            'identifier': 'ƖǈˢƸȽˌʊƊƥģƬϿΔб¢Фǰɠϩîӑž\x80Πψʮѭȑ˃ɘ',
            'categories': [
                'invalid-user-action',
                'invalid-user-action',
                'file',
                'file',
            ],
            'source': 'ɯɛɟ2ѣšʔόԛщ¦\x95ưʁñϐǍȽѿȾЬǨĩҴЈȰ\u0378Ԑɝʟ',
            'messages': [
                {
                    'catalog': 'Â9ˤˡ¦=ɲӔ\u0383ɂɅĊÃWƜƦĭ`qǌ҂\x95ƙŽüñɏFͺ˲',
                    'message': ']ҹÓŃӱŬΙƁǴϭԬ˧ʧȗʿʺԈѪԌ˭љϓӉĂÖǴӌ˰Ɂǽ',
                    'arguments': [
                            {
                                        'name': 'ƃǽѩǹˠĪΈԎ¨ĭ\x93ǳȊԭԉϱҸÄɖԑĬƩѱƩԑЍАѳ˹ʠ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 372188.498103256,
                                                    },
                                    },
                            {
                                        'name': ';Іәѯч˅Ӯв\x87Ƨő³ɅϢpǥҥɼëƤ#фÈ˃ͶԧŤɵхˏ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƅŚUʜʀɠѬϱʡɦϬήƗɊÉ¸ǕÓ¦:\u0378ԋҍ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:034904.896213:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȑ¿ӌǌӪϚӊˣţԆҘіȣҒɒ\x98',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ыҔë\x98џсʮΓ˧JӫĐԆôƨͱӬ~ũÐԢԤҺöĵЩӂǽцо',
                                                                            'ҬƯѱӕǭѓңƈť˩ӓȂĊбʍmϵȔȆˎӌŎĥΛȠű\x89ӲȾό',
                                                                            'ƢϧɚεBƼĒʿȟɉҸћÔВѨŶїÂӀwƇήĠ\x97ŭӗßԮУġ',
                                                                            '~Ӵ\x9bϹЗȵɢǿͱԋƢ˰ӞϤȽȂѻKӈS˵ϥПѤÑďҽğ\x9bҺ',
                                                                            'Ǯг˻\x9eӵćӘƍƜѿʥÅ÷˛ǻГʞ\x92ӫȑ"ҲӠξÙʮϵ˟ԗԃ',
                                                                            'ǮαǅäȢϐыŅӭǊϏŜÃìÇdx\u0382ӳçέΧ½ӝȯǊ{ʙϯѩ',
                                                                            'ˡӂҵƥɚªѨŌ˹˻Ŝ˖ԗăͷɢ҇˦ɀpǑіʲĢɑ\x80ˬϋȻù',
                                                                            'ʪϨ˃ÃǅĎƍȺњ5ǷĝRǰҰѤ˚ѐԂπΟ ԟȬΉԔª?ƀȕ',
                                                                            'ĴѰɡŤЄȂãǱóǞϫɯ_Ω˜ş˛\u0382єʩɲΘǠ£©ñӥģȫ҇',
                                                                            'ľůǁʰѿԀxӇʼſđҶѓǖ˥yʱѮɷů¨ԃǽ%Ϛƈʉ*ˍņ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'žɁMȠʀͰǲҩ;ĀŧΡŘě¼\x91ԦøôʼáҬӢƕúƗΠљʿϛ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': '˞҈ԈǟèЂZΔΰcçŎƟ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɍԥǐʰžĒÂапϝŠƴǽǀΥ`ԡȼɍ¾ǭƀɬʹßˮzϼyĈ',
                                                    },
                                    },
                            {
                                        'name': 'ӍӪҕĢǕȞŔÎȕĔϫΩʭȻʱͰёˍɒʚқKΟə@ѷɛ*ǫƍ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3852823087318434930,
                                                    },
                                    },
                            {
                                        'name': 'ΙŋтіԦ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2445474516148860489,
                                                                            306437338009785344,
                                                                            -4176947726768023,
                                                                            5602222593085154269,
                                                                            8673282567774446269,
                                                                            -1410652196536800598,
                                                                            -7781696358818722329,
                                                                            -7842589447863150149,
                                                                            -3562068453881429932,
                                                                            4773904590291053208,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĵӴƼύǬĎĨВŧƁяðʆӻ\x83ҁ˷\\ˮéѴr\x9eӏɗɌϽǘʋŋ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Т`ԘʕC+wӷǟӀҮфɰΔɦ˽\x88ƝͺŵҿƀСÙƒҨȶ#Ùӫ',
                                                    },
                                    },
                            {
                                        'name': '\u0378ύŴ`ҭ)ԛdʾтōΑȬ˝ԁ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ÛҏШі*ΕБɣĮгǬȽȋӄ+ОΓԝðҟφʽУƞĸ?дȃ{í',
                                                                            'ȀɒеǰȬΰ\x84ƙ\u0379ҸƇĝĥąœЩҷɾż`ԃdŔÑǜðҋР;X',
                                                                            'Ө\x91џɓ\x9eɔϻȭ¿ȫɞ\u0383ơϘќGɣěЎɯϢ@ɲΩњΰ£ҲʎƧ',
                                                                            'ŮЅӶԤǙ£ƟўϺɚȱÒ¢ԈҀèʭцʬЇψſőɶθʚԆЈ<\x83',
                                                                            'ʷ\x9eʧϘԬZҨӨŨĊӝҞкƢӟx҈ʟÀдЫоӺКïρ/фÙӈ',
                                                                            'РƍiŔϨˍˎ˯ҭǴ\u03a2ƿпԄŽΚ˫ƐęЮƚөɤ\x88ʷCȕЗɿ\u0379',
                                                                            'Ƒйюɩ<ЁЌ»ĖèԎҼϖзηϑ҄}ƕѫҐžҸŮʀȲƲʧӢӗ',
                                                                            'ҒӚǹӞŋКíƝҐìЭƕʻɿĶZ҆ʈǷĘúюƭаѢˤͱжΰ¦',
                                                                            'ϲˍάѿŷʷΤϰ҂ðϼѪ\x97ѣwůÍǸŁʜŞĿϭʋƳЍ˺ɋʌԗ',
                                                                            'ϴϏȠѕΘ\x97ъȬӓǒлń{ŗJʉħ\\Ñ>ɸФΚњ\x9aӶʅȕȇҙ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ЦƼČ\x80ӍҚɤƮåÃŇǷjΗˍΪºɍòĭĤί\u038bºΏ¬Ɍԙeū',
                    'message': 'İ˷ɷϙŴӫԝ2ǗǰÆǴjÌΝМȎ\x82ӬÎĿĕƓГҗҒğ\u0378Ūȳ',
                    'arguments': [
                        ],
                },
                {
                    'catalog': 'Ι\x90ҦġˀßӓȐ˾ǫʶοłŧʷɒŴʨέҠҲѦаɷȒ?\x8fǵϳԞ',
                    'message': 'Ȝ\u0379ŞɧżƫӀLӞƐԡcѳΒŁӸФŐΗ¬ōϪŻΩȣ|Ϡ/ϧD',
                    'arguments': [
                            {
                                        'name': 'ȶĮǬǜƇѷђӈĞȓӤʵÆȳσԆ\x87ˋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:034906.594506:+0000',
                                                    },
                                    },
                            {
                                        'name': 'щŽԖ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:034906.675141:+0000',
                                                                            '20210309:034906.694751:+0000',
                                                                            '20210309:034906.714736:+0000',
                                                                            '20210309:034906.734053:+0000',
                                                                            '20210309:034906.755161:+0000',
                                                                            '20210309:034906.775458:+0000',
                                                                            '20210309:034906.795890:+0000',
                                                                            '20210309:034906.815614:+0000',
                                                                            '20210309:034906.833728:+0000',
                                                                            '20210309:034906.850788:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ďҘČȑҵԃƁƄcǉÐT-ЂГЭžӜӜέ\x93ΝûҥќʳСR?ϋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:034906.962940:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʅǀ҂ǗȈΪŮŘӀѽʸƮҼϘɳlʵȡ¯ʝǰРΉ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϗÂdΈ&ƆÿɉбʃÄˬȨΌԠǒʇӤȢɃϿÏƽſΑ;ҭÍêƤ',
                                                    },
                                    },
                            {
                                        'name': 'ɼӺҷҁӽȬ·ЯƲ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɪψ}ĖˣȐȳɰҋȵŕяĜͷ¸ҝɜԡ˗äȐӆǒ©ĜќԒҦɌÛ',
                                                                            'ȡη¸/ŧƄѲ¬ˍїԫѾqɎ¹ýȱƾƾѶÝǭǑŮҚƣζϷЁͳ',
                                                                            'эP˦ʈхŢɄʿÂĩƞɲȊϖЦѠ¹ψԁϨhƲɞ0ɖĬ\x96Ó·»',
                                                                            'ϊÉ͵СǲϮƑ\x93ÁǟKʌӛЮµˍǗЏˢɻПиќē\x8d?Ʌ£˛Ҳ',
                                                                            'ӶÇхƆÇĐӊ\u0381ӆɋćª˜ʉǶЇɉȱΌ˫ЏÊäƢăӨчΤԗЋ',
                                                                            'ҙƅšϕƇϾϗś½ƑɈԂй˚ǥ·ǁ»јɥ҇ɈĔЋ|ǋǨƪЎӸ',
                                                                            '҆´ӄŹ(ûМЅҧQ¯IȸӓʎɺǑˇҭζ«XnþˎϢԫƸȔň',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѥѳӸǣɬşʹƋͼϓ҅ˮĬơѐƲЊƎ$˽Ǹɫɲż+ȷÀìIĂ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:034907.489307:+0000',
                                                                            '20210309:034907.520336:+0000',
                                                                            '20210309:034907.551939:+0000',
                                                                            '20210309:034907.575045:+0000',
                                                                            '20210309:034907.598767:+0000',
                                                                            '20210309:034907.622166:+0000',
                                                                            '20210309:034907.645071:+0000',
                                                                            '20210309:034907.669310:+0000',
                                                                            '20210309:034907.693411:+0000',
                                                                            '20210309:034907.716549:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȉ˩ôʚ-ǨƪԋҠϷ(ӌ\x9d',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:034907.828140:+0000',
                                                    },
                                    },
                            {
                                        'name': '˒ɝřɭҭÇïoƧhҶ;',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ļǀҩѐѩĕɚяǞŏùȌ\u0383ҭȰʊɔӁĮʦĘƴ˷ӎ˺ɍФԩčȯ',
                                                    },
                                    },
                            {
                                        'name': 'Ìƚ×əӆċӈ˲·ȠǣͿĆȋűÄʿ4ͲÈřјƯήɨԞ¼Ґ§õ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 104272.92964852162,
                                                    },
                                    },
                            {
                                        'name': 'ԍſƫɆǿҩƭĬ˗НʦцҘ҂Œ\x8cӶнЏԄɼԀȀ\u0378ҨȮ\\ʩýѫ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            765998.1928681212,
                                                                            952892.2307887471,
                                                                            832038.5413511127,
                                                                            654882.8138976757,
                                                                            338552.55317320465,
                                                                            345020.73912667943,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'íɈƱԙʹÌѨūȬĹϔȚϨŎƩƔǏʤÈϴ˦ťϣͱ˥ƌ3ǁÿ˓',
                    'message': 'βƣ\x90Щξцњ\x84ХƃPšȧҿřɎΐɕƲӿѪάûҚɒõ?нǜƭ',
                    'arguments': [
                            {
                                        'name': '˅ņƀŐǟ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5035095310006817113,
                                                    },
                                    },
                            {
                                        'name': 'ǪaϷŪнФFɋɌ\x99ϕ\u0379\x86',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȓ҆ˏȥε<ӈɻƉˠ˰ф°ɣ¥ĨˉǺȢȂɋһʁѪôƤ˃ёǒϒ',
                                                    },
                                    },
                            {
                                        'name': 'ǓĎ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7053017561501737033,
                                                    },
                                    },
                            {
                                        'name': 'ȘťϻԂԬĻʾϯфҍǻîˈЖŝρƯåAƺǉаҲϟtˎЄТƙƐ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:034908.618637:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x94®Ύɴœb|ҐɯϧǏöҵɕ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɀ\x80ʘӝʖĆӸʓΆ΄ɰăßŌϛʉƛоǯʴԫƯρ¸ԭʁҩηѢЌ',
                                                    },
                                    },
                            {
                                        'name': 'ΘԎ˨=˽ѬԀëзȥHϨΒʹÝʆkԛΧŢʘпāϷˀһӸӯ\x93Ǭ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǜϸеӈȾӸěˇëɸțʴӟʜԇϼǥΞͻʷϒƯ˝ȵřÆѮԝƝʊ',
                                                                            '»˘ӿČЊȜȉҤćˀѷȡWΦDğǚŋDȮƴƄǍʹʏǡǭɛΫѤ',
                                                                            '~)ʜɰ\x82ĢΨċξˍԘȥƱѳƨɛόœӚȱʳǅɖǈBŚgƟΦ\x9c',
                                                                            '%ҌˋƞѲȦѧȻƅȕҭҐ҂ќʽĄʯӂҗ\x95ώγaʄһĒKƥȋɴ',
                                                                            '¨Ή҆ӡƖȊʓѸŅзӅ΄ʠϹԖʝ˳ȺƯʋҶ%ŰѿŗˌБʗŅǽ',
                                                                            'ɬӵǮǓ%ɋĬʡƖȏАԂùϜϊŖϦǪôҀ\x89ĶΔʅˍÂ0þƐԋ',
                                                                            'ϣӦŃ1DǴ$řś\xadʧĉ˗őͺѺˈ7Ϯ£ԉUȸđȴ½Tˡ˾ӄ',
                                                                            'ҷԈÀ\x82»ɉҬόýʆξʂɬԮҏF\x8e¯ǣԊΏ+ʁцʈƌԬʲʋɸ',
                                                                            'ȭţгΓʅӂƟҐǦҕȥͲǳdĎ\x94ÍƖ҃ԥėËƙРϖCǽŊőЉ',
                                                                            'ŴąӰƌƭρϜԠøƣïǕΓϻƦϒmĵ\x85Ўȵ˞Ǌ\x8eԄģǱÃϪϙ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĢžЯɓюʴĬÖӾѶӓԓӌӷŖҌΔǎ¢ɶĚȡС˦',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 684253.7380828814,
                                                    },
                                    },
                            {
                                        'name': 'ϛ9Ơ˷YģǄʟʋˤЁʏźǈȏʞȊϬѲǝǸӃ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:034909.191921:+0000',
                                                                            '20210309:034909.211549:+0000',
                                                                            '20210309:034909.231309:+0000',
                                                                            '20210309:034909.250665:+0000',
                                                                            '20210309:034909.270660:+0000',
                                                                            '20210309:034909.289399:+0000',
                                                                            '20210309:034909.308881:+0000',
                                                                            '20210309:034909.328815:+0000',
                                                                            '20210309:034909.348941:+0000',
                                                                            '20210309:034909.368038:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '+ήïǷŠCԖцʖŻǼ\x8bēŮјʎʸĦЯȚԒϕҌƫƉƿķ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 383290.09115150885,
                                                    },
                                    },
                            {
                                        'name': 'ǄǓȍŭL',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĪԣСʚʞ˳ėɄRѳɏӯƃЀȂԠŭɟѸőͺƲ}фad˶ªϰɏ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԟ(ƾȬˊƈ°ΪӏͿɑϸѥˬ϶ϊ\\ɓƮİЈƀ\x93ӋeʿųďëĈ',
                    'message': 'Ԝƻ˧Ϗ\x8fp>ŬɵʎϐʣΝƖƼλ\x8d`щϞɍØʾӀ\x90ġϤȾʟӥ',
                    'arguments': [
                            {
                                        'name': 'ΥѧnӞŶˏÕǙƦӘњʻԕ\x86jɧə˙ĉ¦ȝȘԂƞдļ˹бȭǆ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӧɐɞʏÇѷяԑĜȉ΅gƛgüƍˤȐθ˻ˢŤƌSӟӻ˘ħԝʐ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:034909.799682:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƿ˟ԛxâȹÌƾµԋŦѥȣԋΞĩʝɣ\x9a\x9eȔOѾЎŖІɣϿӸӕ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7446398785727709516,
                                                                            -4022078405903193145,
                                                                            3656169898882889136,
                                                                            -8955593676445562837,
                                                                            -6444490721514897685,
                                                                            1921951117968579518,
                                                                            3051966828218215262,
                                                                            5524606368234395199,
                                                                            -7540689669915245460,
                                                                            5707729886878318237,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x7fù\x96ƮϺВɃȜЈʳưϡłήϟ\x9dƃȱÉȯПȫȯψŹŕǒɊϒ<',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ύ˷Ɖņчӑӫ\x94ŹҙɌњƟԡċ˒ǓûϟЕӼӘȩĤÅӽʚϘϊĂ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1948932223720643777,
                                                                            -8401886769182388706,
                                                                            -1551454681488636561,
                                                                            -4097591698234540832,
                                                                            -4234460210202107203,
                                                                            5150164465552624722,
                                                                            -2666166409744122589,
                                                                            -1570609377936801844,
                                                                            9043534060594556572,
                                                                            -5157950954345750582,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҾǹĵQΒЪǋѭЋѾœ×Ә\u0379ҍӇӇ#ԜѮǝҥϛƃYͲˑѳhÒ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'íĤҦƣʜHҲӃȖ˟Ƃ˾8ZɱWӇəҡƐëԐ˚ΌôǓφ7¡ɂ',
                                                    },
                                    },
                            {
                                        'name': '%ȳĿΞǭƚʬѪϿõѧˁöΙΣ\x9b',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x87ԟsΤŬɭɆтɤВbяһМҶÒȚȾѲѬќҊ\x94Ϧ HþϸҪд',
                                                                            'ԚϺˈǖA˅ӗĭъԗJĦmWϭƊOƇʷhьôʁ^Ƙґ#ŒɼǓ',
                                                                            'ή6˨\x91ӑеĔȾŀʧŒƋ\x98ƄȬҪӎǖԎʼю¤ƙŶζϯˑŗƵѱ',
                                                                            'ςâʛԨtɝζԇėϖ%ɁϪPĔѽʪѯϮЯѡɦąԔȌκ÷ƽ¿Ǟ',
                                                                            'ΘɰǨȬõӌиԠѦǀÅ9ЙƗťѩҟŃѴ˂à\x83\x85\x8eϠǇŐ˷ýͻ',
                                                                            'ӝȖʷfɪōϑҚýӷ\x9bƕƏŗəbЛ°˻ԀÓʜφŏ˾ΫɭǘЦΑ',
                                                                            'Ԋ˪ĨúЈЙƷGɁȡԚ3˵ͱÀ҆ĝʟԥʺӖ¢\x85ÄįȜ\x84*ԥь',
                                                                            'џ~ѮГĒѣϷģԜԈˑȮƐДş\x8cŖƸʽìΚҸǙӜҰʭФӭͲʀ',
                                                                            'èŲԗγ˔ȇŀýΉԆɳƸďЕ\xa0Ƚ\u0381ԦЁǃįȊϻĆ˛Ԇϻ҉\x8aҸ',
                                                                            '.ғΞʡċƩϑȴҶ<ӡͼ<όƣ˓iɉνџɢ·ӊċ¦ƘŝҎʾɏ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԣ¶ԦʴѸƺԂ˖\x86ǻ\x87ӹ9\u03a2БщĥɪԝťȟЋ»\x88ƹˏɤё4Ȋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:034910.922275:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϣĈřÅōӓ³ȘɏöϒzǖюŮǅʩϓԞǣı;ñҊΑ`ȔӛQ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΥſÛ˽ɔέÎĄҊ¿ȑʜāŹȁĪŮϛԆvɽ«ϟʚćϠȗäđǤ',
                                                    },
                                    },
                            {
                                        'name': 'ţȀѻͼʺЊșˆιѕmɇӒҝǐSМ\x99òȦӑϯ£ҤʒдhǬҳʑ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:034911.097883:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȡĮԍєʫ҂ʨ\u0383Ӻ˜ȰŨԕ£ϮüԘɑӔŭzПҀȳmgͽǠƊҋ',
                    'message': 'ыɦĻҩЇ?ʠɬnƻ˒ɣ˓ʷRȌ\x8fʭǥĴʽƐ΅ːlЀԙеȟ«',
                    'arguments': [
                            {
                                        'name': '\x84Ŕ˯çҥҀʣηɅ\u0379ҷтΚ²Ͷ%ѲĈҷΝ˒\x85ōűӁїцέϸ¨',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҍɀεFȕÏXҖӬǩĒҟĖ\x87;\x94ĹҩӾϬʪДčҴЍЙѼєǙƫ',
                                                    },
                                    },
                            {
                                        'name': 'éyӯĴƓĶïΐδĖǽӟ²ЁԫÀΑɁɇ´˜ʽœʸƳͱŹɝϙʹ',
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
                                        'name': 'ʨ҆þɵғЅȧΣýƦπˍÚɫĭĎ˜ÑnЇzĝӕȒМùԣјúč',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            675122.313347093,
                                                                            503790.5526909778,
                                                                            459514.2916888705,
                                                                            268726.79339055595,
                                                                            705373.3251098093,
                                                                            313263.32884772937,
                                                                            781656.7680587218,
                                                                            629012.9347868126,
                                                                            535104.1606994973,
                                                                            762744.8948705839,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¯ҖƦɺӐǤ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6196177609217787543,
                                                                            -5444541605972841089,
                                                                            1114769305091887793,
                                                                            -7577634088138077474,
                                                                            6660649983088376370,
                                                                            6619433770640230300,
                                                                            -886982785255186579,
                                                                            1588763826621304241,
                                                                            -3326630435540443352,
                                                                            4849524522785928033,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ьș$˾ϹӎďΙȐɎϯğųŞйӱHѱǙŹŉǝѠƫɿɏε²ƅɌ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:034912.176459:+0000',
                                                                            '20210309:034912.193903:+0000',
                                                                            '20210309:034912.211499:+0000',
                                                                            '20210309:034912.228928:+0000',
                                                                            '20210309:034912.248120:+0000',
                                                                            '20210309:034912.264983:+0000',
                                                                            '20210309:034912.281849:+0000',
                                                                            '20210309:034912.298865:+0000',
                                                                            '20210309:034912.316006:+0000',
                                                                            '20210309:034912.334853:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΊЇжƮԅҼӿģҧԫŠҷß\x9d\x8dɞӈʋѶϋФѕǝˣˑşîȅЍſ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:034912.424765:+0000',
                                                                            '20210309:034912.441927:+0000',
                                                                            '20210309:034912.459013:+0000',
                                                                            '20210309:034912.475906:+0000',
                                                                            '20210309:034912.493312:+0000',
                                                                            '20210309:034912.510260:+0000',
                                                                            '20210309:034912.529402:+0000',
                                                                            '20210309:034912.547458:+0000',
                                                                            '20210309:034912.564418:+0000',
                                                                            '20210309:034912.581697:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ĳ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѐĻűʉȭţК<ɅϱҔɺǔǞԬȣѣÒҕŪǂЦԄ\x8bƊφĶӒ:+',
                                                    },
                                    },
                            {
                                        'name': 'ƌǉɃBƾӏҚƌ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ΨЋѠäěґ_ǽƖѺ·ѢЊəÃВǥÛɥԂ\x8eѴ¯èɇИɭДʊ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4194709522805663843,
                                                    },
                                    },
                            {
                                        'name': 'вĥ˗Ēϝҿǎ\x91Ԝҁġƙðшчˍ·˨ɤР<',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            852663.4300342774,
                                                                            811477.386141787,
                                                                            887798.9025942229,
                                                                            367337.465764279,
                                                                            918038.8076048949,
                                                                            554813.7919415855,
                                                                            354335.8847098997,
                                                                            3053.2012408687588,
                                                                            728537.0509483,
                                                                            -38791.223668100116,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'вÚˣEz\x8bĈӉ\u0382ĘΠ\x84ƖƟķϓɢǔӺƲ\u038bɳúԤǊ¢П\x9bƒʁ',
                    'message': 'ĕҜˤâʯʀóǿиÛ}Ї\x93ѝ\x923οПPԠӈ?ʻ\x98ŅǱǸõxЁ',
                    'arguments': [
                            {
                                        'name': 'ҼʡӄЫɵ6ŎԗϰĈҸ\u03a2ö˔GŢүǣŽьЧГ±ɠÚеɌ|ƅӺ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '΄ǐ\u038bǔ¯љɀԢ\xadų.Ϧ©ГϽҾŞдʬϿÀѤîӮǅмҢˎ˱ǭ',
                                                    },
                                    },
                            {
                                        'name': 'ÀҟΩŧØӉѹūʺɼɧşÁÍŉʛ\u0380~Ŝ\x9c\x87ʽāvǦ^ŦɳhƤ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5022678747320286091,
                                                                            -1852399713402673902,
                                                                            -7632871032487864550,
                                                                            4895218118971044864,
                                                                            -6386260620895019589,
                                                                            -731233968403903746,
                                                                            -19519835608151722,
                                                                            -4405194312618845678,
                                                                            -9075154582110017701,
                                                                            -6292889255542631835,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӧʰŚӑʨϒĸǺк×ǛԆҒŲˊ§ŕŨӉϽӞǋϽēЧ\u0382ǁɄ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ȂŐť2·Ҙ§ɐō˳҅ѨɫΩʄǤʤҽ\x9bɻ\xa0ůœҙ[ȳǆˎљɌ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƫś¯ǯҒΠ3ƆΏҥzʘӖʵƞŅͳ\x81ԈȫϏβ˦ӽ,ҽӮNнɶ',
                                                                            '\x9fŽҎө\x9eƛʁǧȖԞҦĆϦ@˷ĤƪЄĘǒЕŖҀ\x8bƥǪѻĭǓƶ',
                                                                            'Ϡđ"DȬҘǉҺĻǑ˽ΉϦǴӢ7ԪǟìӞԄƹŷɶӏɿˌVF\u0383',
                                                                            'ķvϭѴřĻţĴ˧ӃªѪ҅Ġǌɐ˒һԁ˻Ǹǅ_{ͷԁԣƁŹÕ',
                                                                            'ʈġɇŏ&ΡҌɆРAʛbƮҘʐ5ŇĉԜіÀϗ˯Д¿žіҏ!ƃ',
                                                                            'ĨAϦŻ˛ƪȕƫʪŶĻ\x97ŭҌĲǫŎ_ŦǹѰҒϸĐɶϠԤѠͱȒ',
                                                                            'ɬ=ǦΔӾLЃ˰ɥʝȸǁßϡ˟ҴÛɣύ>ξǿσϒүȀBɄϼņ',
                                                                            'ѶΌƊwēяғƴģɢԐҖȇNƺ3ʽԁѠЏƵÝмуʋɰÑ΅Ü\u03a2',
                                                                            'ͼŐʫſѶюӌҮĹHőӡуΥǩˡʰɣӚ˱ҥѵԖͻoǸyβûɹ',
                                                                            'DſɦƼù\x85ӴҾ4ԇɽ¿ĠʻϟǅɕͳӋʼ˃ȫӛɿаŘгѧʁǲ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ą\x82îӜӔȀԆȕҎϋӻĞӴҙѵƟŊáΒΝʱƃѻҽdʼӔԅЯή',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 156025.0172280514,
                                                    },
                                    },
                            {
                                        'name': 'ҒЈ˛īѧƈɒӒϰüǕʜόҏǉǠPʚбȫǏBMæģ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5532776101783770974,
                                                    },
                                    },
                            {
                                        'name': '¿Њʈ\x8cȐҍѿĐŨ\x96όьķĽăƹ҃ɶӣșκҶáϠ˕ òżĉü',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8784692000476343863,
                                                                            8026906655835666410,
                                                                            3379904848931356077,
                                                                            5023943593939077191,
                                                                            -4402066187807116323,
                                                                            1252592937193359612,
                                                                            -2530196689051162290,
                                                                            7311486972526659364,
                                                                            4384080511935479344,
                                                                            3466201232483971054,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǏфǿȦѴϊΏϡľЉŁ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 677530.5327193898,
                                                    },
                                    },
                            {
                                        'name': 'ȴҕϞÂʔσć\u0379ʖßǼЌćԃŝЀɪˡǇÙè˦ΡãӏƘЄŇǤк',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            261631.117580579,
                                                                            150983.63357164557,
                                                                            318480.8733601996,
                                                                            415032.07482019195,
                                                                            306479.62366778747,
                                                                            625489.9881157064,
                                                                            601033.9603566813,
                                                                            682953.1932698126,
                                                                            176176.97124696756,
                                                                            832375.9996458531,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȉӠ˦ɂĥԜƔʦŁα\x8f¡ϭΓьҼâϺȅʄÈnˏ*ßʅҀΗЀ˙',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:034914.612924:+0000',
                                                                            '20210309:034914.631747:+0000',
                                                                            '20210309:034914.648359:+0000',
                                                                            '20210309:034914.663194:+0000',
                                                                            '20210309:034914.677379:+0000',
                                                                            '20210309:034914.692577:+0000',
                                                                            '20210309:034914.706984:+0000',
                                                                            '20210309:034914.724216:+0000',
                                                                            '20210309:034914.740844:+0000',
                                                                            '20210309:034914.757757:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'đґХѥʬӘ\x9cłӀϹӷǲӟϔԕͷӌηϋӣʔĢȈΞʍɊȐ¦ü͵',
                    'message': 'WѣǀϻГʸȦw;ˬɟÊɲҽύLҴ˺ɭȠƢĘ˂ˍ6ú¹Ѹзς',
                    'arguments': [
                            {
                                        'name': 'ƘҒǫɳ<϶ǑξƜʘǔ˚ȔҕͷԌӄɓʩ\x9dρҳПӴɟǤϹɹ¦Ȑ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:034914.912240:+0000',
                                                                            '20210309:034914.929025:+0000',
                                                                            '20210309:034914.945951:+0000',
                                                                            '20210309:034914.962740:+0000',
                                                                            '20210309:034914.979454:+0000',
                                                                            '20210309:034914.996869:+0000',
                                                                            '20210309:034915.013881:+0000',
                                                                            '20210309:034915.030771:+0000',
                                                                            '20210309:034915.047402:+0000',
                                                                            '20210309:034915.066103:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '|',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4032211094929058855,
                                                    },
                                    },
                            {
                                        'name': 'ʙv϶˚ɐΑřКɲ*ōѱΕăĤU˭ïӲʵιүиɮћԦȦČŉԅ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:034915.220897:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϋė®k½ŧrЪĚ¿\u0381YĵŦƌӲӁ\x99;kź»ǓѶҹϡʕȵЯҞ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            582121.7629586156,
                                                                            230178.58613942913,
                                                                            826431.8354896636,
                                                                            -39834.438730963426,
                                                                            186527.9746510327,
                                                                            -45005.79288005441,
                                                                            -8818.44843447987,
                                                                            -78421.82501598203,
                                                                            494136.5803212405,
                                                                            324824.2886704358,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '´\x92Α',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ОϾӸЬӌ˾ԍȠӹӁҁőŠϡόρĔјʦԖЌÐ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 953065.3917438597,
                                                    },
                                    },
                            {
                                        'name': 'Į_ǚ˅ĞċӲВ½ͼ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:034915.691774:+0000',
                                                                            '20210309:034915.706834:+0000',
                                                                            '20210309:034915.724838:+0000',
                                                                            '20210309:034915.739042:+0000',
                                                                            '20210309:034915.753928:+0000',
                                                                            '20210309:034915.768434:+0000',
                                                                            '20210309:034915.784988:+0000',
                                                                            '20210309:034915.799590:+0000',
                                                                            '20210309:034915.814224:+0000',
                                                                            '20210309:034915.829054:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϜʊʴeÙ=ФʻͰƐĤ#҅Ɋ˲τɾԠҍĶϊ˜*¼üˤƳсɃʃ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4367457663124794065,
                                                    },
                                    },
                            {
                                        'name': 'ɖǃИЕ*ƩѢ\x8eѠɲ\\ͿԮŧƇ§·@ƞηҼ˼ɮʩˡĔўȖϰǤ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:034915.977678:+0000',
                                                                            '20210309:034915.995885:+0000',
                                                                            '20210309:034916.017172:+0000',
                                                                            '20210309:034916.036945:+0000',
                                                                            '20210309:034916.056699:+0000',
                                                                            '20210309:034916.076846:+0000',
                                                                            '20210309:034916.096006:+0000',
                                                                            '20210309:034916.114286:+0000',
                                                                            '20210309:034916.132836:+0000',
                                                                            '20210309:034916.151114:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'яƁȣʃ\x9aԋʌP˾Ř/\u0382ӆԭԠĢĴĭkʳЧҴѷ\x9cГ҇Юʌ\x95\x83',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҁÐʨɒʈșҌ',
                    'message': 'ЬϝϠùп{ÛɣћǞNŪҊʭśЯəʊɥʔƷϋԔƭЀǭưʈŀÞ',
                    'arguments': [
                            {
                                        'name': 'ɿéɛ4',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ņʉŋѓ˶ӤƉΗ\x934ƢʬЂǃΒГĴ<ѪηϞƌёɌI҃гϿҨʣ',
                                                                            '˧ũƾљŚ˃Ǟɦȧdіʜȑŵ˵ƶƖųҳϭȴгʚĞɜþV\x87ҧǶ',
                                                                            '͵\x8eµɋΆȗçҖʚ҉Ͽ~ǹŐԩđE«ҔʇoѯǝǣĽӀӉ}˘ñ',
                                                                            'Æ$҇ԦͷǪʙŚǟvΕĢȖī˳ѮυǢǋňȜЅҀ¡ň°ӻЅĈɟ',
                                                                            'ЭͰűәSԑǮȲƊτεƁĒɁӳƖƔWͺyɇ҄ʨДǹ¹ȜϜ\u0383Ï',
                                                                            'ǤԭƍʺҔřōϊςӊԍѶˑДʷƼсTȮȖɌҀʾɪяϣěǝ0Ӆ',
                                                                            'ʧЂļΠÂӨ7s˕ś˔ưʅЉЃ;\x8cчŮҥĲˋ¬˼ťѶʗΦҲ\x92',
                                                                            'ϊªСʊɟɠ˅\x84x˪ƣͳØWpЭЕΚ˧ƵћʂĆƸɝɸҝBÀƮ',
                                                                            'Ӽ÷κdИԮưåƕϑϋ2Ӣϯԅɒ\x98ǙŔ¥ԧȾńǩο9Οϗ\x81Ԟ',
                                                                            'Ҡ~4ӠЦ±ӊIҸđ˞җɨ˚ȃʪƍɻӋҪǟʅĉÄręɕϯÙɕ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȖΎΦƢіʁ*ӭɨȼƚàǮŘǦΚÚɍ˭Ԯҥ˛ˢΈӀŕ˟ãљҝ',
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
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ɨӵ²¯ȶ˚β\x84ҴґΈɞӞҭŮΡȮȱȏβÑ½љŃ*ǄÊѣЊΥ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:034917.091745:+0000',
                                                                            '20210309:034917.106472:+0000',
                                                                            '20210309:034917.121810:+0000',
                                                                            '20210309:034917.138482:+0000',
                                                                            '20210309:034917.153975:+0000',
                                                                            '20210309:034917.168103:+0000',
                                                                            '20210309:034917.183424:+0000',
                                                                            '20210309:034917.198544:+0000',
                                                                            '20210309:034917.214020:+0000',
                                                                            '20210309:034917.232128:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\\',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 139758.01089519617,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȂΛȝĞЀѸϜɏԈ¼ʬ\x94хƥ\x81}ŌҝҔȸýΕΩԢŇʹόЀàӕ',
                    'message': 'ѭЁԆѶ˕×˙¤ӻӧԐԤQоЪ}νӸȮӂĸʤ˸ȑԙ˘Ζsϓѧ',
                    'arguments': [
                            {
                                        'name': 'ʣȘΞȱҝɖɼǍďȴÆǡӪǸɶɷhǇĺГǚŅ>Ԩɖ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5619389350852516648,
                                                                            -6928864997950379113,
                                                                            -950516128062329017,
                                                                            5182914478149676863,
                                                                            -7660565979291484981,
                                                                            -8322618547474778825,
                                                                            8983787090822152308,
                                                                            7479044155497603433,
                                                                            -9043917026172076557,
                                                                            8317893920421835333,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΨӡȤӆϰȢδƾӬҗ˾Ϲ×ҥƁӷȰŹɻ\u038dʛ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˃ɐͷŖҬ˪\x87ҦЍȹəųŔˁɺ\x87лžńêˏǵјȎԏ)ŧWƱЃ',
                                                    },
                                    },
                            {
                                        'name': 'ϺÒĕ\x9dɺʐő',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2104607192342960004,
                                                                            -5486907722277464504,
                                                                            -6564736299116480154,
                                                                            -4361496940325322359,
                                                                            -714026627482887612,
                                                                            -790127987614609767,
                                                                            1315737567501351598,
                                                                            4802349502278085062,
                                                                            4634080934841375081,
                                                                            -8095653125897911208,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʁИb4ŏӴÔĒǔӁҽΗ҇Ďι\x9c%ͽʌ\x92:ΛĻ³ēԥϟǹӰç',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            433036.5558444181,
                                                                            886793.6916476837,
                                                                            309824.0177811245,
                                                                            650878.5153644943,
                                                                            789946.9418915148,
                                                                            502244.39325498603,
                                                                            323666.9847536346,
                                                                            649731.3223884112,
                                                                            625614.5622775359,
                                                                            564305.4584715232,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȳƙѺѨϫĂζгŤπѯˑƎӺ;ΣȹǮ˳ƝʕɣƄ',
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
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'άμĈҳЃˢӿɡӋ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '˟yȔӔ@*ƙčɪӊСƋŹQfυēϞǿʹϏϏƼҿǉ˂ÎÄ;ɧ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:034918.559667:+0000',
                                                                            '20210309:034918.579223:+0000',
                                                                            '20210309:034918.596853:+0000',
                                                                            '20210309:034918.613989:+0000',
                                                                            '20210309:034918.631094:+0000',
                                                                            '20210309:034918.648246:+0000',
                                                                            '20210309:034918.665480:+0000',
                                                                            '20210309:034918.685144:+0000',
                                                                            '20210309:034918.706845:+0000',
                                                                            '20210309:034918.723963:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŢΑȕ±ġÍŜƬɪ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2371809511575579395,
                                                    },
                                    },
                            {
                                        'name': 'ƬǵԪԏ¸űϤȿμbЅԇ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:034918.880147:+0000',
                                                                            '20210309:034918.900725:+0000',
                                                                            '20210309:034918.919578:+0000',
                                                                            '20210309:034918.941173:+0000',
                                                                            '20210309:034918.960289:+0000',
                                                                            '20210309:034918.978856:+0000',
                                                                            '20210309:034918.996766:+0000',
                                                                            '20210309:034919.015213:+0000',
                                                                            '20210309:034919.032675:+0000',
                                                                            '20210309:034919.049627:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƊİԂɕƼˌŌɖ\u038bΓӎͳʆƪĺąȘIϑɐПɛӃϺ˦ ϭϒŽʧ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4507063296765403758,
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

            'identifier': 'ӅƚŤÉƛ',

            'categories': [
                'invalid-user-action',
            ],

            'messages': [
                {
                    'catalog': 'zӅ',
                    'message': '\x93',
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
            'name': "'rӧZÐЦµ\x96ԔϗҋƟƴŤKÌΒƝϢӡ\x92ϬӽйщϥҟʠӄǏ",
            'error': {
                'identifier': '˹ſǼˈӧΜȻȌЎъ3ЩͷԤËЄΗ\x80ϝŮâ',
                'categories': [
                    'access-restriction',
                    'file',
                    'file',
                    'invalid-user-action',
                    'configuration',
                    'internal',
                    'internal',
                    'access-restriction',
                    'access-restriction',
                    'configuration',
                ],
                'source': 'ȲɴUÐΰşɱЋƽuȲɭԜ˕ϷϘӼ3ԄǙѲʑԛςїœĆǈØI',
                'messages': [
                    {
                            'catalog': '\x85ӕҷΩɗԀΙɊҶѨΈѲӡțδúϮ˲ΰǕİʠ\x82ʉƑӆӸș\x8dƀ',
                            'message': 'я3îOɖiƋɇЎзɲ;ӄͶԪѸ\u0381˫ɕǫȄ˦αʗkԚȻϾʠź',
                            'arguments': [
                                        {
                                                        'name': 'ŠѦțȫʵ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6588349479278310420,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΚÃƅϗϸ˻ρƬYĝѢȈāǁΆΠ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĀˤЄɰЃM\xadɎР)ϜǙ˅ďʁĔԆɣңɐ˭bҳψʱЬǣҿӅѠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:034856.107498:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƹƩȊÐК',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:034856.174820:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'џ\x98ήΊˣҥæԪƈŸÀƣȶŔϪϞșԆϿ\xadƄοȴˉŤʸöˀ˄ί',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԮLʎɦƬĥ\x84ǶĈʎЏȲ1пœʛ×\\ʌϨ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -66093312438377992,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȃЪԖɷȿDʲįƥrӗ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:034856.344846:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԭѰϘԒș\x7f˚æǮӒɈ˝ØőǼПʝΜпћƢ¨Ūǲ\x87ѹó(]Ά',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:034856.410030:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȽȴjӬ˂ϯӑԄ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:034856.476056:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĴƟӤ\u038b\u038b¿]ψĀŷϚŋ˔gȤӛʹ}',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʝ\u03a2yưӺҪШҁϳЙӇ˓ʎѩˋǂôˤϮѫěӌӊƝˈѢŉМѓӉ',
                            'message': 'ͺӾBĖͱΧԢНÜυˋ~VɗӷөϴċǛрýʼǶǄ\x9dȉĮʉɟ·',
                            'arguments': [
                                        {
                                                        'name': 'ɗ0ҵˑŶԌÚјɫƑĻĳ˵ϜԆĈЩһǨЭǛ˦ϦБɠѓøЫǞÈ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1468233766412670612,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȼϫjŬoєͲũɍ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˦˭шϙЬȹʼѸϟŉϾÇѩƂȘŁЦΙƾǖюġǆˆǠѦʬўğŠ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1199859182113437883,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЈÂŒĵ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5649843745502566068,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ĕ˔ԧҿȠΠҐК¯сƗϒˑ7ǾʏӰԖӼŽѫӝɩϰȖh&ǲЭɟ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 126676.07168221739,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԣĿϺċəÑĄĿíЄijƘôϻҐ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 480001.6943097247,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɧτɌǤ%ȑҀҲȓжӂΩΧɤԂѺƖɵˑ(ФÊԉɍGƮÐĴõ\u0382',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -944006782178394642,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʎjǚ\x8fԥRВɖ»НѤɻƁъϙҺʽǓѹțν\xa0',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ù\x97ԮҴԎǆ҇°˅\x96ǕВĄѱõϿȓ¥ЌȐ҅ӏӁȎƍ`',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȅԕ˗ӳȁΈʣòѕԁȪȀĲ˅ÃɹŘӠϵӝɦѐΨɗƦőʡ˃ĺҾ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'њҟя\x8fƣΧǳɓ¶ðΣÓƞϮêƙÛʖH[ȟǔʳǙƪʭΠбɆӸ',
                            'message': 'ğο\xa0ҚćŇĥԛӀԗǂ¬2ÎĆΘ^ϘƟΤİȻk×ΨҀĹŮʅѐ',
                            'arguments': [
                                        {
                                                        'name': 'Ӯ2ɃϒϛП*ŧűӄV˝ŗЍš9ʼϒʍɮѓл\x9c˾"ŬӺʧҲù',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'л',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5011960534946050833,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƥχǪѪсoҁѦʡȑåņµҀҹӭ~ˏ\x89Ò҅ŪEʙӒŁˀáÅȁ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʤϩƒϰϓ\u0379ԘˮӡřΓ(ʶѳʓ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:034857.644789:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŉǻèʴ˶ÐДЪ×ːԋĵ˒\x84',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 423393.9676481858,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȴĒˎ\xadˮ÷ǠÑƵĕǿÔGʙϿϚяƦϘҼȲԝ\u038dҿ[ôϢͼ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ξ΅ˉѢɒŭйõƦӉǟŀȣÅÂ\x8eξĭǥŅǋɳĈlώzΩ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ʀ¬ƴQƭиĵНˤԘMԅé',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ΦчÒ4ϟʕ®'ȚȆǇĔЃ˘ɵȽъсˌŞ϶ϔâҖЍxͻġѴϘ",
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȬϠ¶/ԝĮȇÀƈˉӱΥϮ\x93ΖɆ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ˌт¶ǸXƑүǮΑƣÄΨģǿРŴͷĬϔɏŇɳʦ˘Ś\u0378Ҭ\x7f˂¹',
                            'message': 'аҐљĐʚŜͺÁ\x82Ѱӽʨʫº\x8báˏәĩӉŵцЇҧîƌT\xa0Μȡ',
                            'arguments': [
                                        {
                                                        'name': 'ѲΫŎɢéюȄϜһΧ˛ǅĮŦϘğðΖӮ\u03a2ťϝԄˡ#ȝ\x95ńԦЖ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӆDñˍѱȱ˞ǮϦ\x9cŁ¤úļűȠɡǦΉЋÈůɑµyɔƑҭ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'εΚҠЈѣµùЅ~ʳʅҪMđύШӭǱьμ˂ȰԃƑȌ±Ӿ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʈҒˡĊǼ¾ư˲ӹrĴЫˆ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': "ѴňʻÎżƱ\x8cњƟǆɚ'ʨ®ҋcѼʸ\x8eÖťͿΛìѡҩ\x8f´ɬő",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϣyԦԖϲ˥ӬԀ\x96ρзĲÑĭИўѱѩˬԡÙɆʐʸАЦѲȟȽǡ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'į.ǣӴϘ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4661042178675453095,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŻѷʫƛЊђӖάИOĥӧЅĝƓǵƹӖĮÿзϑǪʚϹƍĊCÙи',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϊԗ*ШŇțΤ=Ϛ\x80ÀŤзlťҐsә\x9cүϲƐ;Ҩ¢ɛλѾȇҝ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҙеˡ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3447447140555998619,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'SԫÈΙƝʋ˦ӵǋӶEϋʣωəΨԡȄήʕΤАƣʔ\x95ѨÔǾʒ\\',
                            'message': 'aɕ˅ůʔȡ%è¹εƄιƎǛΐЂҹƸØҪҤęɓÔɭéȡӵ¶ȣ',
                            'arguments': [
                                        {
                                                        'name': "оɸɮԚŝˣš\x8fėӊȮȴˉːҲĪJk'V",
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЬѷĉȉѨƋˏϾìӴǃȝӏȌɸʭεǍ>¿Ѱ\x81ΪӔ˹üīяĉҰ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǹƧŋиɥʡɕâŕô˪łǊҖĺʶƸϫĔψ\u0382ƟƾʛҘ\x7fûʖ°Ŋ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҶщƥӀŪȣ˵ѽӇ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:034859.507023:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ηϥΊKÐ\xadìĉ5Ϲąϳ\x88ʥĒб˷',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4386703516494455378,
                                                                        },
                                                    },
                                        {
                                                        'name': 'vХΛЭŤ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҖƂНʣӋЧƂώ£ǫԮ҇ԮЅмϱ]ƏŢƠ³ɭưԈȘūȽǺǛê',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ź>жŞȨ@зźҤM˔ЀǄgΠӉĺďЮ,ĠӚ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'дӖʳ«hНҌ:ͼʎÉóϲ˾Ҥ˞гƇҵʱeϊӠā\xa0\x93Ǘʇї˚',
                                                                        },
                                                    },
                                        {
                                                        'name': '҆˄үӾUǂǠǩũ\u0379\\ˑºӂɓűӾȆ uӶӅʞ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0381',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƭƀˋ\u0381nӈ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '5СȔţ˚ε҅ѾÕØҳˋԉәο9ԖøΥʸӱWәȋцπѶǨʈҮ',
                            'message': 'ţŜˇԙȑˎuɯйї˒ǡӽѤͳʭǫ1ÿΗƪҥpΐ҉ŊɭƍĴ\u0383',
                            'arguments': [
                                        {
                                                        'name': 'ԩƐё˦ʭԭϝΘʡĂǌԮƋȗɣɴÉвɒѯȸƫīǰЮŰƁœϾө',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 65937.29703740001,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԐoԏԈȍɦҷΉщÓɭԥǀǼʩʿåƉһўѱðǣѻȉ1',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ËЅǫȥ˂ʬéʛɡ\u038bӣ\x9fѥёоӏNƂǕƬԧŒȝŸƞҘҩŋ¸ʻ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'XѲ»ԛӻѵЊŪ)ƫҳϭ\x90ϔ\x97ʗԙ6IϺҬ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȐΆ.Ԋ˯Z˳Ӌ˘ӵǽ0ĖʋҰ˨\x9cŭӰщȇΩ\u038bΚǆҘӥɔфŠ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 919281.6582072545,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÎŎʜ:ΡľǓҗԝʚʳϱŀ\x93ҧɚɥжǸϵŕΚȣϬİŏдңԔƱ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĲϢЊԬсŃňȑљϼδʟȟӖυƉѸΖΣĠh',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 317863.30989826744,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԛ÷\u038bГǓʥȩǭƤ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 534947.5753075954,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˋήѹ+ɈȤ˚ͱЁѾʕǌĸ҉\x96чKҷĮ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƽʲϦƗџſ˹',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 130050.64596614867,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ē{ȉFÂˈČҜ¾_ʁǮӴ\u0383ô¡Ø\x8eìθӸ5³ӂӏɋÄѣˆϢ',
                            'message': 'ϬŽћŨʕƤɢӶˈѴȅǲ*1ȯķѵƻ˅ȯϢˤӘĽ[Ѐ|˔ɔ¾',
                            'arguments': [
                                        {
                                                        'name': 'ŧõ\x8c҉ϧʷǺϛӛԭН',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʜû¼ҹœȐǭýÒ\x96ҞЍţƅʩǻЏŻ\u0379ςŸӆШŠϔ8ʻǄ>Ü',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 101346.3706096528,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԧ\x8fƊҨƸΉѯʥĩΫњǒģǼŌǄȄʨȧŌǰ]ˑƫςFʰƨxʀ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ąѓͲɼ¾˹мсČÃ«ɐҫÁ˶ѡƸΧШȍȧĸαĄϞԧÐÀФÎ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¼˹yВþǎΜĎӯ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ČѪɛ˥ǯў\x83ĭȑЉàäθ(ʜðǽҧƤҠvʭÒʳѮɤ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʦ\x8dćƯ¸ϰĎ˛ƪƄzǫʉʹŐȻʱи',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ȏf˃ΉѬǶе4ϪҫӷÛӦdΞʉЯ%ХʩtҺȽ˂\x95ˎǯг˹ɷ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ūɷèƾˬ\u0379æ͵J\x97ǵùqҿԮΨǆĸŲϲȶ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:034901.561514:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɔ0ʵ\u0382;ʷԉϖʌ.ƞӫӇȚКǣΝŜǐѾĘҰѿθϾȓ¡ъʐɯ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǏЪʆșɍʧ¾\x93ÄpӋɈĉѡđFØȒѮ³ƵλнԩȳȀДÈ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '¿əϪβѾЂʇ×ѱԇԦǣÜʄʷʡӚɆӤɛ\x7fЩɪƎ˃ɨȥŌŊʆ',
                            'message': 'ǫЉ¾ɚли¦\u038bӠї±ѷEūԒʜ҄\x92TͲЪȔßўđĿӢ@ʍÇ',
                            'arguments': [
                                        {
                                                        'name': 'ǀ£ЬԥԁӐζ\\\x8fŧʙŧʚј˘њŸMFƐȑ˽8Ԛȣ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 320166.8232973487,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӗΪə¾üǻƀϚ˒Β͵\x98ɪÛ\x8aʹÍуѹКÏƱѷ\x85ˈ.dĶʅ˨',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˖¸ŕԧϫϻ҅0ϠˣȤīH*ϾŹʕЁʐϋϧԦÜ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:034902.053220:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '¹ˣӈǂmƐǙ˚ǞȨӪ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 730693.815131872,
                                                                        },
                                                    },
                                        {
                                                        'name': 'DPҟΕ=ήÁɿ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɴӓ³āȾ~ѡ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȆæЗРҪʞԎŶÍʸҬCϤ˸ԙНƱЯӚʯ,ΔэǼϧɓ˽Ǜdɤ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʨξˀйϫƺӸϧĔѸ˃ȉʞĉʼˌ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĺ\x9e3·Ѯү΅νƂӠˢHÎДѢʾŃɢϷˏ˔ʉɑUƌ˅éϳԀƊ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϵ˰ϯҍləȽęʇʐϥŵŚϠĜϯѽɃϦΗǑˬƨũˀТϧùѓԌ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': ']Űφ˄īfԉˤЮÁӠǈʄJϪЃĪя˱ʇӲʹԏʆҲƽͲȾǟɶ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ēąĮųЈõĉŭϝǞƞƸʙȲű\u0379ƗΔÆҥНʠԘ\u0382ƔɰϛЎϻж',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 791594.899128395,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԍ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Α˽ǠпΎвΙ\x88ƂͻʇԔӢɔǂɻ^ǰрƈǔԖОʍϑƵȔȒȤŔ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ΎͱΤЛõʱũСNʪҠ\x8dҝġİҦnɥȮϖďŖjɵUȬɑʞ˼ķ',
                            'message': 'ǑɏЗíɥʳƳφHϳɺЈ\x93ϴԪˌƆȨˤ¼Шi»ƾΥϮºŔԖҏ',
                            'arguments': [
                                        {
                                                        'name': 'ӄѣϕLѯӿ0ǕǼЏѲèϺŕ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԣ\x9dƢëϚ£ӘщŜƯʐȗҤ҃ɗӌҥτƑѤМͷɐ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɶΖӔԈŢ_ѷt˽LH',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:034902.969219:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǜâǍǚű˪ўҊЬҝ[ɖˊƒ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÿ(ð\x8dɠ\x93',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 194422.9652083186,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӾÒ\xa0ďҥŸǙ\x8e',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǘȷȬӞƌͱ\x9dӴƤń˲ʺıЀŘĉέȐŇ\x8a<жƆ®ōÄǣïҘԁ',
                            'message': 'ʘÇҡIʹɨ¥ХȞʠǫо˫ɨȃ4˟σтўюɳǅƗϾіĐɍȍʖ',
                            'arguments': [
                                        {
                                                        'name': "ҽԭǯԝ\x8cҏ'×¬´ĜĔŇʔyʍ±Мԙќňǜɇ",
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʼӆѸ˦͵ʂ\x89QɠúDОҙƀɤAƙõƤ˕Ǡǰψ¾ϴƃԔʦ¬Ј',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'фǅԭƉĪʁȵ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӣȝάη\x9aİЭԊΆʜΉTȒӧˍДƹѝŁυÐƝȁpŜ˘ґӏζǄ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ғ˔ԋԥǨůӧпĖԔƼċГӞJџ`ʿнöӁǹӔѿŞÚȚʒԦɗ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԙ͵ԈȞҀΊō\x81ɾǴ5ġԠЃΦʸɑǂˆвԣ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӽɈŵİ\u038bҪʀҶʡȱȅӽ˗Ï',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԊƠÑɺƫɸгǫǥĥˏǐʲ¶eԆ;ƿ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8219435456930606290,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҬƨӡƶǯȲǉѽϺǤӜˣ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 379512.74173342297,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ћɺ*Ҹ˰η\x99Λġ¿ľӍԪϗĆƺϞ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӎь\x90ƃƠÌǇȖčʩśƴúҺύɜϴǀͺưſI˕ČҥӃǑφң',
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

            'name': 'еѝϥ',

            'error': {
                'identifier': 'Õϯ҄ϬЍ',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': 'ˍ:',
                            'message': 'Ģ',
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
            'event_id': 'ȓßЙ>ˣȫȂͽȵ҃˒ɞҍІӑsμÝΫ:ǹȭʄýҭɪȐӗȑă',
            'target_id': 'C\x87-ЫùŔӌ\x83εƥ˜ԨҪ9˦Ƒ\x80ѨʑҘǞԓӾϸ˱ͳВʖјң',
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
                    'event_id': 'ҷʜwȤԮӮÑ\u03a2ǳʨƤчğѕ˦˴ԣǑЮȦдˤӶӶ\x8aïǜӭĶ˲',
                    'target_id': 'ɴ+¾ɲöȧəŞǌϺˇT˷ǾeƐҔƍȡʧŒğ`ɄӞˉЄǾҏ҄',
                },
                {
                    'event_id': 'ƤQĤʗĺƵѲҘuçрɻΜ#Ȁ;ă¨θʽԡȸ\x9b,α\x81˳ѳЖƤ',
                    'target_id': 'ËɕsӵÊnҧóːϬԀԁVԅԐмĤɕѩŢǦ2˙˕»Ƈ˅ŭ\x8bҒ',
                },
                {
                    'event_id': 'ŎԀYòσįˬʶȶƎhӆǰ3ӯřƟƸѠ˶!Ĳӎǌ¶ɜĺư»ĩ',
                    'target_id': 'ŅȕѐĎήħͶǐētљқϱˉŀƷɃɬƻ»ńʍҿжӸɢɭƊͳό',
                },
                {
                    'event_id': 'ȨÂщӁȲĩƎȏĽґ\x9cϤ˕-\x86ʬъ©Ǭҧ҄ƻďɍʈƋʪǻĩ\u0381',
                    'target_id': 'ˬ@͵ƮbŃ\x9cЮхǈΐ\u038bòˎuɶҧIǹʫ~ΈƛӨʶӗďŊĘҖ',
                },
                {
                    'event_id': 'Ǔ,ͳͻӹӞЋÍŰϨҢʖêɊƋCàƎ\x84кŐʟǀЮҜÊ\x80ԠĎҀ',
                    'target_id': 'ҾӸ\x94ιщяађʟˢ¸\x87ěĩǡдЩȬΖȩчʰ[Âȍ÷ĎвяΞ',
                },
                {
                    'event_id': 'ǁēȩȢϏÂ\u0381˥ӯɻϨƹǐȺĊņϷċʯҧΆˌýɵϛĄÏƕɈѠ',
                    'target_id': "αä˃\x80ƣʺǉ\x97ʍЩԖŏϻɧàʄ'»ϿЊԉͳ8!ҥӳΉȳӍō",
                },
                {
                    'event_id': 'ɠ®øϳì˽ӬĂЖҟƺƎӅĝұȦĆmƉ|ϳ˲Ԫ',
                    'target_id': 'ťҨԬĻ¶ǼѦĒŖTӢĺÌúƒϓɍЉϒɬʇòʡˈԖæ΅ŏΗΞ',
                },
                {
                    'event_id': 'Ņν*¸@ҝӡļ\x8cďĭa|юbɧԚ}&Ь҄СɝӑͿǭ\x88ǗȺˌ',
                    'target_id': 'ƜѬ<Љϊċ·ſ',
                },
                {
                    'event_id': 'ſȷӤʷϨЩΕŋԉѦʛɱщî¢ɓ˷ӷˮϖʃǟȓηŗҒԬȧʻɄ',
                    'target_id': 'τĬӍώį1ƂĪĈӽū˦ɖ҃pϙǀťӔςжɐѨмԈk҃Χǐŵ',
                },
                {
                    'event_id': 'ѽ_ŘȭξьƇƷɖϻĽƙʢh\x82ÈЫΣ)џĠʣԎƘӗ\x94ɻžčϕ',
                    'target_id': '\x95ԟɩɖӜÒĉϖʷRɐĻϭƗɶɀźɧǪ˧ŷöǨȱąʀY҅ϵ:',
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
                    'event_id': 'ΧɃĎЫк҈Õʼԁˣ*ʱӺɌUҦń³ЪλȵzӝӊґʮÌƙҔи',
                    'target_id': 'ʼŘ^)ʧӬ˭ʇǘ\x85ʴԠȚ ʭǱӡӘʛʏΉ>ԖӬб«ёӹd҆',
                },
                {
                    'event_id': 'Ѡ&ѲŚɯҨɗĸȋҦÇʐǊӚȌŋь΄ЃĀϘ\x9bƟпʩōȰǧɏʀ',
                    'target_id': 'ʿƈưăʀԍƝ@ĕҮԪԉѽ;Тĺҡ˗gϻͱƎϻOöіÞθĔȑ',
                },
                {
                    'event_id': ';\u0383ӎȼÜƸɝƓʣԀȭƏɹĆϙĻҤϓƝɺͰԭӺϦцλʆȯ ԇ',
                    'target_id': 'ɸɳĿФú\x90Ι\x8d҃±ʜȔӏǂŦԤ²ɓSlѦɽԛ\x7fҫɒÐγnʇ',
                },
                {
                    'event_id': 'Q-ϯӢķѤЧʇϙ˕ĪϾʋ¨ԭѮvöӬјƇǄԦɥƴƶҭǭÌԟ',
                    'target_id': 'ŹψȋЮΒÜʜ˝ō2ǫʶȾ9ЯԦԎcӆˎŇԂƛŐɤфόHDϕ',
                },
                {
                    'event_id': 'Αǖ½ҐħʞїƭӪйѳɰΠČЭͷЩƁԖξҲΌ\x82ɴӸшѱUŪð',
                    'target_id': 'ʲӓʞСŠ¶²ǷʜL¬ɧ΅ˮƫϘǄʍϫˋʹǃɺɹҰӏαҒȆʕ',
                },
                {
                    'event_id': 'ʤ\u0382ʮҘȝȋƋҨǺþʡκӨ.ơʞʤ4Ɣˇhyěȓ˰ȀǵƢϋӌ',
                    'target_id': 'ʸ»ɊƟǸ˴íXÝÃτnγʍғүɺĸJýɂѽҔ´˙ӅƿѾΠʵ',
                },
                {
                    'event_id': 'ӈ\u0381Ú˶˪ɅźȳňȾFłӳŚƺʓSfĬȔӰʳξƝӑɱɄƝїȾ',
                    'target_id': 'І\x8dьИϠʸfƕˠ*ǣɮʈʪ¯ťʩҨɻĴ;ϸŠŠƴ˻ȕӺǒˢ',
                },
                {
                    'event_id': 'ʎϣΐɋήĝgӱǽȥЕѬі˥ȒήǬǔa©ʟУФϼUƵѯȍЅԦ',
                    'target_id': 'ҭϠӣҐȬԢ]ɮ˕Ԥ·¾ĴͺȕԌҠɄѯ8ѰɨôϜĄFǹ}ȀƖ',
                },
                {
                    'event_id': 'ķ\x87ȌʉlԥԨ˫Ûң©έɦԢиϑŎϷɪĭӯ˦ӣΖƞAЭӓӑ5',
                    'target_id': 'ľʖɏƾϞө±Ƨϳ\x7fXÚűɡǡ˳ҁҳěɒȇó\x81Ӫӌɼßԝ}ˀ',
                },
                {
                    'event_id': 'ŖõσƁӘӬѲÔҐ@ːöΊЮɩҎɢЪƽÇąԡЅΛӉɷŘΉn\x8b',
                    'target_id': 'Òʐϥ»ʒƗȇÜĺԤɄȼʇÂήјʾщÄōӲ\x91ȔѮӯԇĆ$ǖ˟',
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
