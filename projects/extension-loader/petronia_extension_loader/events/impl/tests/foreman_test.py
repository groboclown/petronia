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
                'ЅѪЯҥʓUяБϴǂӸĮ˱ɥÏойĽӫħțɄMΞÆˬ˓ψƌ˹',
                'Ƽӌ˶ˁõƜћ˃ԭÂ·Eϝӳ˕ŧȿˌӫӄŃİΤè¼ѿ˧х˜·',
                'ëtƎϘӖЦǻΔȣʞɳŽͳɷÃԜЩЃђ\x98ɫ-ȿ;ӫ¹9ʒӌĻ',
                'ҦȱhҮĥǠȋœӍVĠβˡ˨ТŐĤӾԒǷѩӱʨû¦ΰŨʝʹϤ',
                'ǥǷЗĪ(&øĎʜØӴȮΙ˺\\ɾȨƨХЌ|ďц&ŃΜ\x93ѨĒ\x87',
                '[ļɀʪƓιĻʀϛ\x97ǡíȕɒˇÙʕǖһ˃ζgÓҥɬ\x7fϨұȪ!',
                'ˊ˻ļLѲTӟǎ°\u0378˦ȈīɰԉʱɄΎƫԝΟ÷ӡÆжӒЦȜԚ\u0382',
                'IȼŴ\u03a2˪ӃβԏҪȁʠƌϋĿɌ9ʹΈǖïοáέԝԒs\x8dƒq?',
                'ϴɠȢʕžÞ£ӹ˄ԪɴˌĞʅǑ;"ӛɂҸӖԗŕžЀͻһȭϟЍ',
                'ӅкƮԀҚ×ʃ^®ˌŖȀXȂԛϪȉʘUł˴Ԉ]ǜȹƧƯӰΦõ',
            ],
            'source_id_prefixes': [
                'ǡѳwÝɫ±ɡιƲэrЉ½?85ԑϟõоВȷӼɒԕμǲеɰɤ',
                'HˀėƗƕσƪ\x9bдҀɵ˩ˁԤÏȊԏχп!ġɇѥόɇЧϳԎûƮ',
                '˩ўԐēқ)јņЃĘԤəͺϋеЩӘȈԂˤŧ˽ӡϥεӾƼäɮǥ',
                'ѪԪ\u0378ԤͲǚԭƲÞǔɛDͽҪӶӴɔ҈ÒζѸΪΤѪ˄ƭƤƄÔ%',
                '§ТѸ\x87ǶϱǌôȴϢʭηĂȕӈéŶ+ӖÆɏ\x9cŐȔɮξUѪʃǝ',
                'ԧćʭҎʏΫĲÿ˺ǭчȰƕƞѐû³țҜʹŒǱэǩG[ơ˧˖Ν',
                'ĸɴ/ȡɮ˽GŴмҐϏҠɯŀÑǐОˌˆɇѾњŎё˼*ȁό҉Ͳ',
                'NtӪ ͼΕˁǽ\x9bϿЊɡεҚĲ¿ѲȂҴ~ɆԉɪɠȺΖʼʚÂΑ',
                'ϣϲʆѧÀѰ\x87ōǗԈѰȅÛGЬʙебŎˍЍĴӗʉҽZǄȼˬҼ',
                'ЌѐӼ˲ъ>ɶ˗ŌŝʆΡǉ\xa0|˚˜ėEƽϹ°ƍɯтǟKêʢъ',
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
            'action': 'Ȟ¡xѐſӫзʰ',
            'resources': [
                'ɅTБԇЕϓыҥıśńɉԊˢʇː¨ÁǡͰȄυπ\\ҺDҒ϶ȹƾ',
                'ƜȢŽԔѵͶЌϢP®ʞʮЂҿçϷsȻԣӖƗґȱǲљɏϓΥǓӘ',
                'Ƞǽ\x96ϪˑƟ,ХǫÃļҎǈɰȋȫƚ/ȵģԔеԟŪКзѻнҠǠ',
                'ЧɲаԞʇŢȾθü˝уɍǥ&Ӂ҄ϮĤԚʹɎԐĖÆÌ\x81ǟӸĆӕ',
                'ƵȒŦɯ_\u038dԫëȻЧ ɈͿ˻њȇЪȦǼŦȠϻˣɲłłʳԐΪǂ',
                'ÊŤüԄÐςɦ>ǆЛƄԅǘӞɔёɤƪl(Őӑԧǡ˽ɥoѺǟʃ',
                'ШɶƤŔԏ0ȖρѵΡͼ·\x84қ2ƹ&ȵШҭҝǕɾͼǨȒӥƟԣʺ',
                'fПлўѾ҉ͷ˪θ',
                'ͱþϺĨȊӔǓǩЬĚ˘µĥțэϣǡɕǌњϿͲͶ5бˠԘыҺΪ',
                'ɟНöɅԥ\x96ȑάЀОÎȼӦƩҤgНǓƽʸýʗáΔľϔд;Эǘ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'ʲ',

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
            'name': 'lǵ.`ӞюÅƇ(ėџ',
            'version': [
                -2080933901047041074,
                -9169658631459330993,
                -5880939644318348349,
            ],
            'location': [
                'ɔ[ʜ϶S\x89гϹˮdżƢ¼ŸԍҵȴĝȔӐőȸΝϹùҖRјvɱ',
                'ĵ\x95ԦƬŋǸŗѹɬґEѶ/ȡŊƗԏϏӵʿǜɆηŤЈͼǳȥĳѨ',
                'ө"Ӏτ&ļѡΧώЉɢ˫ƀӣѐӱĻ\x81ԅʑɁǘϛƈӮήԛ\x8fҧΩ',
                'bǾȟҶʐŦ˰ë\xa0\x84ӋɄѤɶʈǕ˹ɞ"ȅι4ũòǢѳбάÍΛ',
                'ːѤű~Њ^Ԣ\x98ȁʰЩνСĊƝ΅ЎćäҘӈǧͱ>éļǵɫ҄ɐ',
                'ÿϱϯԧŃǵ\x9eѶǎΐӝƏɮÇӝϤȉԜÔЌ\x83˲ʜƐɸҊЁĆõͿ',
                'Ĥξкϋ<ǁĻë˘ԇɛ\u0381Ԫ˜\u0378ŷҲȠԤјԟԌӯәòƻʆɘƽϦ',
                'fϒԚœ˚Ɨ4\x91OΐǍŽвԠ\u0381ɜŃɭҌɒǉǒԗˏʁ҉ʢ)Ӫβ',
                'ÁĻΌȓȅƃŰӴ\x87ȂĩͲƨɜΐɡҘʇЃѥ˲ͲԘåhˁōʀƑʤ',
                'ґ^ƳɌΎωʉ\x96ǕЧӥɑńΤwҊȫ˫ʍŹԟŌʀԇ7˔ƣoƋǇ',
            ],
            'runtime': 'ѝ˹Ŧɔ\x96˔ʺǋĖiƜ\x9bƼÑɸ',
            'send_access': {
                'event_ids': [
                    '¶эɴg¬ɝ\u03a2+zǯ\u0380ƾ¢ˤý7ϸʈΌˣЬҧπϥҰŘőɄпĘ',
                    'ǚŶÁԪӫ³ÅȇѕԢОіǸӣƂǅσƱɗџȢΧҽˌ2Ϛǥæʢʰ',
                    'ѼʍфȆԍҞАӄƁˡ˚ʂ˺ǮɹЭšуŚϥ¸\x84˞Ŷ-Ԕɢς©в',
                    'ǈȰæ˄ύȚοѕЈŁ?ҳіȯÈэ\x9f!ҞӄȷĎ°˒ЉͰԭǽҥѨ',
                    '\x85ΝϑŗþÅЀԫб±ʾхċɯԜ\x84¯\u038dγƁ¹¤ğԃϟ˖ųǚЋÄ',
                    'ӹƦϣĒҦˀҒ҅ЪʮӾǼҫɈʺɽĮNƬјЫöЗϿƀȔηǑǼӨ',
                    'ћϨƼУʵӿɺ˓ǸʅԞɈЪ°γΊԖӊĉĹѮǷϢԧԊÇ˾˥˸˵',
                    '&В-ȰʈФȽŽ\x87ӔФЃƹųԒҿɧ',
                    'ŎǮӽEӰ ?ǓĕÏкʢǯɦԧѥŞšНŴԏɤŸѷӅƃÅѱęʦ',
                    'ΫϳĦӧʌmǞӁ΄ҙϣǄǖϸ˘йƜƈǕw\x9eɲԊ˶ρΦψȓǕÉ',
                ],
                'source_id_prefixes': [
                    '΄ʸ¡Īʊ²Ĳɉ\u03a2\u038dǬ΄ƈѴόӣʙɯ˗ЇȦĒδ\x95aƸȈ2ʍЁ',
                    'ʒôȋԀϾԅЄǉÖĘŤЖąǗ]Ŋ÷¯ϳĵŮȟҹУrϕд+ɶϟ',
                    'ʾзЮͷ¶Ǣǣpȣʟή\x86тϟŧưbŏ\x8eƶҨ\x97żʀĽШϺбѐɓ',
                    'г˃6ǟǦŊҾ˽ęˈѧǑΐԦ҂ĘkΑ6Ƽ˃ƝʀЃ=˾ɝ2ȥ\x81',
                    'ÈǓӱϟÒ]˺ЏԮ;϶Ɍǉ£ɝȘŉZӁŗ;ȹЎ˪ϵ˨ϑ҃ӻΨ',
                    'ƹɌԜʫǔӫ\x97ǯΣѳCʦЖԬϞԮԔӺȧ]\x93ǾԃǪǚȝѬ˱ӖÅ',
                    'ĿˣÉ˥ӎϷΪЯpʕrɩŅqȼʨ˘ӼĺƁ~ÅƐȥѽԚ\x9aÑŨǊ',
                    'әӟѦӥ©Ôõ\u038b˼ŧɚƷѾδҥŲɤə\x8eӫȜǝ\x9aλȋǭƋѨ˩ҥ',
                    'ʮҙɹǦΐƦѾŝƇĢƯ˟Ž²ηԩξϊΒʼҊĴƗưѰĐģ˴n,',
                    'ψåȦԪ϶оŚĐƮϪԫʂӤȆ£ԧҷɂƎ˙FԘŕ!&џȋӃςǒ',
                ],
            },
            'configuration': 'ǎʅĀǃΨɟ»җ˕ωƽȨġ³ГæÚř˧Юžk\x99!ΚҿѥҰ\u0381Ș',
            'permissions': [
                {
                    'action': 'ʛҬԞӦȚӏȩˍ˽Ϲдƿ˶ǣʳǉɷǎːĤƶ²',
                    'resources': [
                            'ȽӛǃȝɒƠƒјŦπҙð·ѹѸрԝЖ˥νǱпѴ©Ƭ4˓ʕОӅ',
                            'ǌѐӽ\u038bĐ˝˝\x91ΉԘʍί¡ɷzȢ˗҄ʹJʀѩҫáкȻӐĆʖi',
                            'ðwÍEÃЙɀ˅ɌѵθκһϥdѓǏԒʌӄŧӊiƟ9϶Ц³ԊV',
                            'ͿǩлȋԌѥʣ\u0380śʵЋҥ·ԭ\x86ųɪϭɌIɹ÷ϕӘлӅó1ԃρ',
                            'їӕЊ˵ϑŧѰʐӉĹǧϘаϺ@OƧљԓвύƣȺҌǭÛѧӽǲи',
                            'ʶԦ2áƨ7ɖ˛ũĆà˰ųˡΏƛҼВғ˾ӱсʾʀајţƶҙĽ',
                            'ȅø1\u0381ŻγǡыċȈǣӨ˖ǀ÷ԛTíˆƥНüΚ҉ˢԁ˞Żsҩ',
                            'ɺøƇªӆɯΉʩˇѷČлѨ˪ɗʌйȜȔEԦõȐƂ#"ƄǡӫX',
                            'ʿʢʯǑ¥҈ϛŀÒǝξĜé´żȱϵҼʖϬѳƌЫzӣãЏԭşЅ',
                            'ѿ\xadλÒɊєѩԍӢѷώŮ\x84õDΘϤƮJƯӸȋ\x8cĕӊțӇӅSҺ',
                        ],
                },
                {
                    'action': 'šцƟĲėԎНŦԙJɶőΝÁēǇƲ|ϊɝƢϒ\xa0ӱȦȖӖn\x97ɟ',
                    'resources': [
                            'Ҡȃƶ9г]ѧbѤʤ°ȿΩҷȸχĳ7ԌΡÅӝʥӇʊɂ¥ȹŢӵ',
                            'ϺĞ^Ӫ\x99ДТɃÊǗǀFӇȲɇχZΝŸӲӊӠOȜοϓƨćɒ˸',
                            'уƩԞĔǍЬǲʠ˅ã¹Ċ0ӊŀɤ1ƒ˳ȘѐÏƉƧʶνЉĵƇÕ',
                            'đͳΖɂuǮųƯ\x97ѹΕȭʨφ\x9fҗǤŴБɠЍϕ¡Ǆǻȁ÷(Ҳ#',
                            'ħДˏǐÞɓпӰΔȨfō҅ʸȪƫЪóНĺϥΞ˖ԫa˻9ïΥĭ',
                            '˝ÍÑĕǀʾ<Πԙì˘\x9bIǃɄƧǽѨǅ϶ƓДé΅ҁʫǢǁңk',
                            'ÎϟoóG˼ѾȴѸåŚѕ;Ұϰ˝ΰßšŒSƝє\x88ӳơӿ˗ɴƄ',
                            'Ξ\\ǞǆԪǉˁļ˥*әǏ˚ȀЂˍɩǁ.ƭМӶʋϷƳ\x93ҦЃ2ԓ',
                            'ѵƁԖǧ³ǁҰʹИķνԁѠįԟҜҥϰϪʮEțв8ïƲŸČƼΌ',
                            'юʾƵ5ѲʈуǈҺϴȮӅɟǉͰɝǛϪƱэ˹ϢlƳϻ\x98\x92āŋŃ',
                        ],
                },
                {
                    'action': 'ǜԓȐÍω$ӘŗłƪʲєΡϨɚʭѾ˻ӵ\x91ƪ\x85ȆÀ\u03a2oΐȒĶŖ',
                    'resources': [
                            'γÁѲ¬ɝȎӅʫǝɫ^¬ÆѡоĀͱΆԋɢÁų˞ưˀ¼ǥұǧʸ',
                            'ɝ¹Ň˒ЄʒȫӚ\x94Ǹш\u0383іΧϨ\u0383ѵȑÎɔøʃłąǢȖыӸͿԮ',
                            'ӾŽãƫӬЊĲɯġ\x89˖ưʶɲĉ҂ťћʄшë˕lɶѻɦ\x8d"Ʈȥ',
                            'ë«ĽˎĂĩӒ\x85œѲRĂƮԁzòУжѤ¢)Ǿŭôʟźʤ˼Ǔĉ',
                            'іl˲Ţ˝\x95Sҕрʜ:NơĠwțҳӒа;ʒŻĳȂƢԒ³ɒĕȏ',
                            'ɋ¡˫ˡƑǞδӰ×ϧ~ӡӖfȾćŁɯŊԁĴυċZƞæNĮıʗ',
                            'ȟǍ6ʾř}ӤeØĹSЌԔĥў҆ʖ\x7fCЮƚŐҲɞӘȳϭɗɯƊ',
                            '\u0383ƕϲ˝ˈ\x91ϽӬȕÝ\u0379ƟɪЮΆÓɚ˦þ0ƶԉʔηŁåÄǼɊԈ',
                            'ͽǷſǊВ˙ӊȏʡӷB|ʣĐ¿ѥɬϛɠƼ\x82ΪЂͳƠƦҺϟζЯ',
                            'ʟӧʯӟɻΐЧȑ9ɪӑʁĲ҇tЂęzԋʍ!ɐÍ$ˏМҎνӳ¬',
                        ],
                },
                {
                    'action': '˩ҸůϦƜˉŮҺʏ¹\x85ҊįԇҀǝЯԭʲԦyпǖϧƞɢӾΑɰϦ',
                    'resources': [
                            'Ѡʡ˹ʒ\x82ΐpζϻ!ºƓʼǔʣƃјŽΓ´ɓɠƾɍ˄˰˱ȅŌʝ',
                            '˴ïǌüӶϸmҩȸΩͻŕȏτФͻƟԤˢҞŇԓϦƎɒĤāĖҢȥ',
                            '˔ΐ%˰ɳ^ϩúΏϹ˶ЩӔ8иùÈҨп)ÅƠđɜŰѳӻЃҟρ',
                            'Ɂ˓˭¥ʶҵʳіҜqƖӰϛ\x87ʵϟǚǅ¢ҏĉ£ОŖłŗӛͺăā',
                            'њŠӃђÛ˔ǒƒґƺȘʣƪΣЙеɉϬȃ\u0382ϣĳʸZӄǨɨЩǆȬ',
                            'ȯʓƳέ\u0382YɵԗǚпΈ«σҭ\x90ӾԘǗ˱ĉďŢʬΤϳøѣƺцƤ',
                            'Εйҕ \x88ΡXgвƏʏγҖ',
                            '¡ʡѮçӸҮΔ4SҋʣʼʎӛҲґăҾБ\x85ѵèͶ\xa0§˅ϗҁȾΫ',
                            'ԇӳϑҒӭЂʬŔǎzjӻʈË˾Ý\x99ıмƓҺÄ\x89ä\x99WͶZҞÇ',
                            'ďѨԅ÷ҳǮͽÕӤŴїп®đȜљΜĮǍéҎ¥gиǅĻâҢņЖ',
                        ],
                },
                {
                    'action': 'ԀņϋǽĂҪŨ-ӵҏ˝ԠȽɗōќ\x85џέʁъӗɯЄ\x85ʢ҃Ϗ˥Þ',
                    'resources': [
                            'ңTśǚҲ»ɹӑ\x8aŁдъТöϓѫ\u038dɓɬ˛ó˂ˬӢҟʁ\x86ÙϬ\x8e',
                            'ʟϣːҜȊϱҍΓǇeȥј˭PǚѱӸſУ_ϟyԈÍϮĶʯƊɴМ',
                            'ήʷŠȟˊǌѧӬуӹɽȺԉςӊлҼɅάȠȪȞϥȄuɩ8ɺơ˽',
                            'ʲδŗӛѤ\x9eҵęʨ\x94ҵѕ\xa0ɚ¿ԈͳӟԀǇԊɸ\x85ӕ\x97\x8aҤĈƛ˕',
                            'ƣǸđƛσŖ[ԒҶϊļɇӆ\u038dҨӒğkҌ°αϳʼʭΚʆɞőɍŁ',
                            'ӡҐņƝȱÃӀǖęĪřүбsˆɜмЪҔσÏӁӪGІ\x9bŊ¶Ӹã',
                            'UɌÐҹѩϦƋКԭ\x8aыίǃы²çǛǶĒʳʚłƌƇЩӢԩк˒ϋ',
                            'ΉɄɏŲǻǋ˴úƷѸÓё¿Ǔ|ӜӎвļӳʅʌťǌươÖɚɁЂ',
                            'ɕ˯Ł¸ȉŸɓȌŎϺɟОԠЇҸǰǲÎ"˚ʴƞõ°XɕΤÑӇʴ',
                            'őӆʞ҇\x88ʺѷďˊŨ>˸ɓԬȴĕƐԟιƚϺϹϮđȬ=Ƚȹˁͳ',
                        ],
                },
                {
                    'action': 'ІӢșӹȩӡ+ƪӤӟĢЦ΄ȊˍʚŝuҜЛĖħ^ȵûúʷ˧ƛì',
                    'resources': [
                            'ŴԀŏԈϣγä\x80Њ\xa0ʧӡĄ°ĂӨұϼΖˌǴΥϙŸŊσÏˈΧЦ',
                            "ĵɌǆҕϩԚƘØӈΗҊ'`ͲɹҾϭĲɗǅҹϭƸΜȧ϶ɨáҘƩ",
                            'ƩѲ\x9cǘʅď\x92\x8eĈǹҐȃϪФÆȬƳϴ½òфѶɩŲˬųɖǴ˧t',
                            'ĜɪєϽѧȍ¼˝\x92ŃXYÕѻ¼ġқƕЮҍˈ Ȧ#ŐΝΘǘǓм',
                            'ȎҾßƧˮƘԟʀØаɉ¨řƻԃbӮϽЄʧҩҍӗӃ΄ьªĥɜȸ',
                            'ɭIȕƃɲиƀўԫ¤δSéѸЮƳ\u038bɢӁԦȣ&˝éȕҔȻľԔЪ',
                            'ҋGґЭƌ\x8aźmɧÅʻ\x80ыȼě_ĘʐŻћҙʢă˛ɿӰǄɅќ\u0383',
                            'ӉɌĹ˱ȇǴ&ʿʫȫ҈ǌǈĩ\x85űĖɻ҆ȴǂѡǾδîʑҶ_Ǭ˼',
                            '͵ΉZ«іѲʊҋԑʪжƄȣѡ˒ÛȉÑΒ\x85ЭӺĭӰϳǉŕǵϒԍ',
                            'Ѥɲ\x80\u0382ȾȜӋ^ůԩƩĩ\x83Һҝ\x97фÌġĜ҆ԮӁɚϐȾθ}ӽɿ',
                        ],
                },
                {
                    'action': 'ƳҒҏώǪțHњǁ0ίӿӪɃ\x94ɒͼ˂ơ\x88ʟҗɴȏŅƗĂǴɊǐ',
                    'resources': [
                            'ϱmӳ\x9cŠɎǳХÇɥҽϙþĴ˖Z\x99üfԚČƄΡҽʠIӒǂɠϒ',
                            'ǰ"ΛFҏʏѡȃźĺξґЬƤѺƈÐŠ\x8bͶӓгǛuǗƙŧπ:Ͳ',
                            'ĕϨƱWȤğÿħЍȃǧġϜϨćȎʣөΒɞɞxԆʯΠȱǊƏ·ſ',
                            'ƃŸũʠЕǴЁBɄΉѼʮƦϧȢԢӹмȪΨ˽ʢғϴĽǔż«ѨѢ',
                            'µʫјȨx=ˡơǄaϪҳˑԍɋфҌцҚΦāѻȒԃʣɄ\x85Ϳ˳Ā',
                            'ғԗԎɯ\x97Ȏ˳ȻŒƌâv0ӈHë˚ΝǌΩҬѝǒÙȏj<ӠŤÒ',
                            'ÝѠӎĄĕԙȧVźѸϩǖɅʍϿѮҢԄ1οϵľǊŅѴԁżɞˤȷ',
                            '\x80ԣя¿ǽмӌL\xadӳӧ\x94ȳMȭӆÞϗĘŨӀ˶Τ9ȰwǏȒSњ',
                            'ŭҠӹ\x95ќĀýѤʲȃЛ˽ɅXfʦԦϔ5ԦԨѡҁѻìҢ\u0382Ӟӻ҄',
                            'ӯĠˎһ͵оϤӒȿϙΣΉЉЕΞÃȉŐДʬȸǭŌʺǘ/ĴьǓӛ',
                        ],
                },
                {
                    'action': 'ĂȪœŲрĒҙζԦè\x9fԠɴđǅкӒÖȡÚɔӤϗΝˍҮҴɹ6ɵ',
                    'resources': [
                            'σƯġĉqӛҐюўǤŜǇűь˦\x8fǫƙΖȉЁjȤԫ4Ρ\x87\x82ĝČ',
                            'ʾѐčѾΊӆ˙҅İ˸ι˕Ή\x9eƔ҈ǌӐ¨jłDɲӂ˃\x91Ʈ"\x88˖',
                            'Ћҙ',
                            'ԢÝLΟðıȄ\x81ѰÿӣˑtǵNɛӃ¡Ҹҭ\x9eԖƙȑǸ§ͷϊʈĽ',
                            'ʱͳȿßϙҲȆѸқɹ ҒʀÂѸňγɳʕϯƐǜӧę#ÐӳÌ˦?',
                            '·ȇӫ˜κ¬ˌ˧ǆˆzϤǴžѡԅSɶǉςԊʲƓ\u0380ƙƟê*ѹȠ',
                            'ƂnΨҫΩɤЩǰϘԢЍ·ԂƶʕϹͶХBтȕЭɃǞɟȼӹ˗ԟǡ',
                            'дϐɡӺԘЬŴhȡɧȜ»]x]зѩȊÊϻśˋ¢ťāӘ¤Ά\x95V',
                            'ѺάҮДϬҕʚǃѺΞː˩ƞȕņ˽UțPqɗҳŊСɮϛƱįȭ)',
                            '×ёɦŒˀƍӱͳʕԥ˲υʪcǬɍΧңĴɇ@+ƅЇ˳ԣηˈәȜ',
                        ],
                },
                {
                    'action': 'ǭ÷ŻϣƔUɺˤ˙҆ƝӏQȆ˖ʂʳҐɌθȆ_ɁŢп\u038b˵DƵQ',
                    'resources': [
                            'ūȨ˘˽ŨʇʢFХЊťҕŨϚZ1ΗΠɹεĞѲǋ˚ΟЃƎƾқӘ',
                            'đ§ԕř\x84]ǧЈÛ»÷ǆːҽǶɨÁдąƙŲеҳƣèϮϪ\x80ɔµ',
                            'čЗĤӷɰɺџ˭ȍĲPƹϐV\x91ԞԂʿƅӚơԙѝŭҨ\u0381ǰсēԒ',
                            'ʰǎтӲɕӼȝd˘¯ÆӿͱoűʹȹŷøɈ΄ӱæŤuʻԜȎØŘ',
                            'ŋϭѹЃʂЎǑɂȩs˫ԕ¸ԃƙɶӽэιȰMԪԚÇĺKŀèśҊ',
                            'øНñ>ŚΗѱ\u0381Юїµ_˜ЬҠɁʙŰēʀʏƵÅŏŲ˓ԭǏʖ6',
                            'Ϫ·řřӒ»ƋӹУšɠϷǬҺvгЪÝǤǷΤ?ŴƶǪƴÕ[Ĩɠ',
                            'Ȼ%Ǆϙ\x91ŤϖҖÌʰˆϡЂŅѺɻÁх<lƓʳńєǊƟ0ԔŶˍ',
                            'WмǐаÛǳ\x88ЄәѳȖƨԫӗêҙҊĿÀƹŻЕӟĀŞͱˡIϗǧ',
                            'ϊÞſÜÎśҁѲѿŢvȢɣӕӣԪԎ˞ӻȯ¶ɓȣǁ{ɯӛ˟Wѯ',
                        ],
                },
                {
                    'action': 'ӌÐɜň\x92mԮǯʷ¼ɽԀӀЊκɁ˂ŢʓɅϾЄаɪүûғЪȿÓ',
                    'resources': [
                            'ɴĝŊŊŎÊғ?вʴŉΣƺˁС)ķϏ¹ԭӥÖ`ńĲӗɷȰªD',
                            'ӝįȯ\u0380\x8cӑύˤȎ҈·Ԛ҈ӞЕӾĺǵǩƍÒˢĴԅѵǧVÄɤЀ',
                            'ʛǜʇԠŜÔҰд˘ūТʹԨԜ˽&ЪźџѶʉηӂɍӹǄԜʨиĄ',
                            'ƧѓĘϜɠұСЯʷӓдĴěǒ¾ǰԮɭȢǜľCĺǜΝхҹȯɒʎ',
                            'k҂˴ŽXюÆҞ*˚Ɂʷ¤ҙБʪåУ-ҖĹƈÄΌơƥХŗҸʓ',
                            'ėњϗ\x96õʟϺеЕĹˏх©BӝσɂѡϰӫʾԞҭԘYеλőÇķ',
                            '˳ʱʱȸÄāïЈȵΊΤǳЕcˍӋXÔEȮѪʧĥ˷ʎMƋ\x93йȆ',
                            'ф˴jϩһǋ˫Ƃ˱ÄԘξйύ\u0382ɅǟԘʤбņ{þƫԗƈŚǔϊː',
                            'ΩѵȯЌAάcњ¢ȬǈóĽҹ˴Snȩŉâ5@ѢĒǋaҊϦγɦ',
                            'Ʈ϶ԌɟюíΘЊΞǮĠѲζчӗԚψ҈ʳ1ԭӻ*ăүλmоӡƞ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ű·ƴ',

            'version': [
                -3926281698413114465,
                -783458392245902817,
                -7676555961706409726,
            ],

            'location': [
                'Ă',
            ],

            'runtime': '¹',

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
            'name': '͵тğ˹\u038bǉȧπƬǌӗυйԙŭ¡˰ė˖ɪȜεǝBЛ,ѥΥςŦ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ИxԢ',

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
            '$': 'ЫȮǥʵé®ӵϼеӄƨӼǯӉʂ˗ϒТ³ЎIԟӦŎƓŖɪɇ˅I',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -9186610419594858214,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 641822.6154410053,
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
            '$': '20220522:172801.015385:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ʋ4´ӺΨƤ\x9cԈЀƭΓнǑŮċȗҴԬηԑϙҡˋŎЊϸΎǨϛʑ',
                'Ў˸ĐŴƊɆŌЗ\x7fӷˈΏ˕ӮƳˋʸǴÁΦ"РǡȰƞŚťќ_˧',
                'ʣ¹ǬɄ˻ǀˌ\x9b\x97˙γÏЇœ$ѤΎԕͻȨǫĉƉƾƍƅ\x92ȫӖɖ',
                "ӮÕЗƻêėʒҁԝŉƁţ˼ϩϮĽˎ'ԩҴʷǔɡίȒɧȸȀɔѰ",
                "Б\x85˥ϱԑŅħǈë\x8fΒҝΈԋҳѕ\u0383îŹΞѲєC´˸uʀ4'ˇ",
                'ΨкʘэϱξщбΣȖͿǫ,ȐӤƜȃπŭĭƍʻ϶ԗуʹΐǴɞÄ',
                'ê§ӷҢIl_\x84ш˪ĿӀ!ЌǐмȸѩжӷÌ\x94ԧ5Ѭǲɝ\x81¤Ȑ',
                'ѾϩΩǤЉĦȒýƊӄʄpΔEˌЃʴԬȢφԙł3УŽ\\ˉΐȅĤ',
                'ԖĩŴοЀʧбч¨˪ӖҗԫӡÙúϴƻ_˪.Ϙ˲ħĎľİȠʋĕ',
                'Ź0úїϚƐԭɂʪnԘ˥˘ŇŰӢÇǋŀћ<ϑÚҶ½˒άŎԙɔ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                4657721032566465845,
                -5149020613106129471,
                -6716284528901364594,
                -953137928766119783,
                -5396986323467807761,
                6131854394904456819,
                -931163415356298217,
                -2119998826960071958,
                -7116973959000981816,
                4743635398005259041,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                237918.7382157672,
                870739.8591937469,
                826255.7572706664,
                312606.7054798828,
                417169.7066357046,
                103715.67192414383,
                334302.4191468309,
                391129.4203068285,
                308513.028548011,
                936164.5594677139,
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
                False,
                True,
                False,
                True,
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
                '20220522:172801.482321:+0000',
                '20220522:172801.490438:+0000',
                '20220522:172801.498137:+0000',
                '20220522:172801.506229:+0000',
                '20220522:172801.514451:+0000',
                '20220522:172801.523339:+0000',
                '20220522:172801.531540:+0000',
                '20220522:172801.539851:+0000',
                '20220522:172801.548797:+0000',
                '20220522:172801.557162:+0000',
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
            'name': 'ȏϦď',
            'value': {
                '^': 'int_list',
                '$': [
                    -109335731697035830,
                    -3308770349521708791,
                    -5061419107394554443,
                    -9093185843145539362,
                    7967962552312681954,
                    -4693265186479814388,
                    6416516769996710537,
                    -1657216564051607579,
                    47694146421396425,
                    8215255294973118995,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ӽ',

            'value': {
                '^': 'datetime',
                '$': '20220522:172800.899542:+0000',
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
            'catalog': 'ˇ4ʯ2Ȥűј°ӈbʻŻǉ\x8dКƨǫưńҊĆǱҽ˴ĦɦƬΰɥ³',
            'message': 'òŏ\x8dwɗˀҊ͵ѽʎ˫ҡϲĮ˷\x85ǗāӍŲ˭ԃӨ˨ĨÀěŜPɖ',
            'arguments': [
                {
                    'name': '|υʼӣͿʤñ,ͽjPеśϾȿʱƃάȉϾ˩@',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20220522:172800.136923:+0000',
                                        '20220522:172800.146127:+0000',
                                        '20220522:172800.154190:+0000',
                                        '20220522:172800.162739:+0000',
                                        '20220522:172800.171423:+0000',
                                        '20220522:172800.180144:+0000',
                                        '20220522:172800.189362:+0000',
                                        '20220522:172800.198918:+0000',
                                        '20220522:172800.207853:+0000',
                                        '20220522:172800.215681:+0000',
                                    ],
                        },
                },
                {
                    'name': 'mǭбϬɶ˻ʨʅƨØѴǲɠuȢ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -5403646515039626824,
                                        6854191068698462814,
                                        3224593639535651569,
                                        -8507280464076053715,
                                        4651377574229438974,
                                        -6987010690026092082,
                                        -3317823182510947311,
                                        2633867182007892109,
                                        2427631933359281694,
                                        -3371387493987961689,
                                    ],
                        },
                },
                {
                    'name': 'ƾчбÙʇ¬[Iԣ¨ȁѼϱԏüāϠδгЌȲ˗çɥϋɃɯδӃԦ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        140234.4637517871,
                                        -28561.484536627686,
                                        388615.44942891115,
                                    ],
                        },
                },
                {
                    'name': 'ςăѪŞϻшv˪ўŲѡӼσǴYȐɻқ',
                    'value': {
                            '^': 'int',
                            '$': 3485758659029734991,
                        },
                },
                {
                    'name': 'ѵή˚ȭδҗF\x9cɊʡːтҩ˦ӴφȀҦƦʲŭөbƝƴ\x83ƉЍȨɪ',
                    'value': {
                            '^': 'datetime',
                            '$': '20220522:172800.471285:+0000',
                        },
                },
                {
                    'name': '-˗ҿJϯŶеԫӱϑȒȸǬΕЫǶŮɯϋʡїɊЮ˒ǆΊŪѥʼŅ',
                    'value': {
                            '^': 'string',
                            '$': '&ӨŇœҽӖǷҧåÔ˱ƅŞȺsȔuĀΤТȗǫƕӃшȩA¤®˽',
                        },
                },
                {
                    'name': 'ïɜɗŇӘԆ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        315762.11073744216,
                                        89434.01692450809,
                                        799843.5788185424,
                                        845322.1080656797,
                                        -41623.073389242694,
                                        179157.37377950968,
                                        561785.1204542012,
                                        413044.7597333252,
                                        424722.34925775253,
                                        905566.448158446,
                                    ],
                        },
                },
                {
                    'name': 'ѼƭґЈʟ',
                    'value': {
                            '^': 'int',
                            '$': -2733209506173444608,
                        },
                },
                {
                    'name': 'ɫƊ',
                    'value': {
                            '^': 'datetime',
                            '$': '20220522:172800.691554:+0000',
                        },
                },
                {
                    'name': 'ɀ˟êǡöźȼӧɑΡԩЀҺ҉\x9bҷҡɓϴѹƒӧαѠĚиƗѺΧC',
                    'value': {
                            '^': 'float',
                            '$': 583422.8452301843,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': '\u038dŌ',

            'message': 'Š',

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
            'identifier': 'é˹ëѴņ΅ŜɒǲʍΡΞí\x92ңƵʩȽͶčӤДʎҷ0^ьͽή҉',
            'categories': [
                'file',
                'invalid-user-action',
                'os',
                'access-restriction',
                'os',
                'access-restriction',
                'os',
                'internal',
                'configuration',
            ],
            'source': 'ɏ˶ɸƭǶƒΙ҃ɿѷҲÔĿþ˶\x8bʅȗҹɽӐѡ˧ϔëĎӌɫÈИ',
            'messages': [
                {
                    'catalog': 'ϮÆӝıԔӺѪíŖȩΐÖͰ΄ХӇţЄΚƁHͶʉԅϮΥƤԄԃĽ',
                    'message': '˙ʍʤŝØϡ҈Ǝ\x81ƋČǡɪʸúǚɤƭ˄ĵҧƪȋό\x84ԤƒÐδ˲',
                    'arguments': [
                            {
                                        'name': 'ѣѷԬãσσtƓàђƶʺÖЃȁƍ˖κȝʢʕľ˩āʵϱċ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 173006.04141189373,
                                                    },
                                    },
                            {
                                        'name': 'ȶĬÍȝņҮӰҦΚĸÛНΏėĊѦɁȘɂCԗĤӎǊƞѢŐƴµK',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ĐĮġӣϗΚ\u0378ɒƌ\x97ýƙ°ƻΝƄґůʫƳ˻˯ӌч{ĝԜ\x95Љŝ',
                                                                            'Ћԏг˩ʏοSƟѩќʢҳ҂YǸҧě·ǧ=˭ɯŉҼϻ˃Į˓ӥ´',
                                                                            '˾ȾрӭԏƅĂѿǯƮ\x99ҦǮдϤӵŦʮуҡԌєǌ\x82ҕƅÑƢ˫z',
                                                                            'ѭТʯwѡԕȎөΔɦԍŤѕͳϹºɁҥɉΘˈΞbŻǑƎҁҸśб',
                                                                            'ȰЎҶ«ǄӾѤӪɬįĹ¸ҩѠÝΩƞύʄđǭVȉâЖ!ǚӮӚ8',
                                                                            'ɉϔf\\ɚӓʷƴ ʵӜұȅҤʷ:ŚӡŦäǒԇ6ŪȦϬƴҠЉƠ',
                                                                            'ӞωҥіеŃѸԠǀŃǈ9ǥӪƺêԦԏƪчҤŘɏ¤ԌφήѾԗµ',
                                                                            'ȧθ\x7fǭԪƛӠÎŖ˖һԠķʛӗƯŅǠρȓıҚ\x9cƔŧìӷЭƮЌ',
                                                                            'μЇŢżєΌӄѵ϶ϒǺ÷Eʢӌ*ηԡĺŏԛĦο¹˩Ϣàϗ\u03a2Ѭ',
                                                                            'ЁÀЕÏԪƢ«\x83βƞɆѩȒɓИUΦˌϜфƛÞϩńҁǉʔÍҵˎ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɺƧKÄϹΝǖϥqӿ\x82ԚFƜϷƑι',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 740127.1821575137,
                                                    },
                                    },
                            {
                                        'name': 'ȒƒǿƘͷʵҫĜϜʛøɬīȰ¢МеʍʁФȯɯȽӊ\u038bѺƹнЁ\x91',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3790223336015093988,
                                                    },
                                    },
                            {
                                        'name': 'õʻнȄҾχƩГɾǒȮφáŶzȹЊюǐU˛жРɋȨǦӓЦ\x7fĒ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -86268.39534906541,
                                                    },
                                    },
                            {
                                        'name': 'ΞӊӪ\u0381ºӽԝ®ĒчКȢyΘɟԥŰêƀǦԥӔӮɢğХJǳҮѰ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
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
                                        'name': '\x9fŕ/ӾӉ΄ɘԮ¤ӳɳ!ԩΛþȠ˒ɛӤҭЙсȱӝѶʣ`Ӆ˟Ą',
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
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'κϛέ¢ɡ÷EҸxtħvβˬϭӅ\x89ВǰԡëӲёɩŜQpɉͲʞ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6027274646401648660,
                                                    },
                                    },
                            {
                                        'name': 'ĩšůіΝбԔĤӫԞĿ˙Æ£',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ЗӯĬԫǓѝӤұʢȣѻҥƅɴΆȚ©Ƈ\u0381ƋĦ˭ЙĘѐҝҨҞѬβ',
                                                    },
                                    },
                            {
                                        'name': 'ŒȆѼПéʌӲӮĲĵȇ\xa0öČ~+\x92ȺZӇȢǓb\xa0κʲΣƹÀӰ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8052045455694696316,
                                                                            -1149151606954359197,
                                                                            -2649517646385558472,
                                                                            12596357829761917,
                                                                            -6562230241212593273,
                                                                            -9133754949824334174,
                                                                            3240727411886799276,
                                                                            6237173009047303807,
                                                                            -2891011032030335571,
                                                                            -6774824141195665329,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѿгǰȄʲӯѲæʠʝƷ\u03a28Өǯʟ˃ͰΒ×ΔБˑĢȈΥǛǒɠ@',
                    'message': 'ŦǼǯҁѐԊ³ƾ!ÞȘȣˍΚΦѡŒψќË«Ͱ`ǊѹʚЗÛԙĺ',
                    'arguments': [
                            {
                                        'name': 'ğʀλɗύũθǯαɟ˄ʯ˸ı˺ϹӐԠɽοҒϠИ\x93ƮӐlnҧĥ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'НȴǏɏɫȢғһѶΚϝTĚ҄gƋʐɍ˄',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172752.907508:+0000',
                                                    },
                                    },
                            {
                                        'name': 'өƉɞĹϵИÚÍ\x87',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -9120.364022278445,
                                                                            695807.1695751154,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҄ƴӲўχϠɄŇΩ.±ϥɖ\u038bˎĶɾĶóνϨǈȳƵDѠԌǩѱ΅',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            543155.6109921243,
                                                                            -99698.55858940331,
                                                                            255391.198091424,
                                                                            616278.6991915234,
                                                                            -24132.60331241152,
                                                                            323115.0099762233,
                                                                            374219.61527024134,
                                                                            862227.9527455639,
                                                                            206843.72577660746,
                                                                            802646.7726002533,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɠΰ²ĂϓΌтſŌɈ\x85ϭѠǷԦøǖšƽǻŕЂԩDǮǳѦїƠѪ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172753.113281:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҕӔʙԌ˙ǒʆ͵',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172753.148593:+0000',
                                                                            '20220522:172753.156876:+0000',
                                                                            '20220522:172753.165229:+0000',
                                                                            '20220522:172753.173525:+0000',
                                                                            '20220522:172753.182154:+0000',
                                                                            '20220522:172753.190921:+0000',
                                                                            '20220522:172753.199569:+0000',
                                                                            '20220522:172753.208608:+0000',
                                                                            '20220522:172753.216497:+0000',
                                                                            '20220522:172753.224917:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȷʒƔËτ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˁЇʹ҄ԖŠЇnφҰЬťư[¿\u0379ɟӀқƤƓɥǨÖүÅǔˑĪÐ',
                                                                            'ϼӂ.϶ǯ\x9aѱÐǺϲίɕӆʦńƤ\x9dĺΗϨǣȚԛŸ˫ǢΦĉ\x90ʺ',
                                                                            'eˢ`ҞȢѣŌƔŰvĩςѢ¤Ʃ˃Ǻ϶ŗ\x94ӕХÀĈҹ˗¤\\ąϦ',
                                                                            'ѭɳҭӒɨ\u0379ŞŬΞӯʮϊơĄѡVӁчƍϏȂѹԆӐĭWˑœҞФ',
                                                                            '$ɥŅš˨ȚАũǉ\\˸ɰҊʷä¹҃μƑʱѧˬҥϮПԛŗ¨Υʹ',
                                                                            'ņηÄ)ˮǉɚԎҹó)ɠƹҚʱɸƎ\x9eĪˠǰτǤʥ\u0382ŅȫӢƵˀ',
                                                                            'ΏҒpʿӤπ%ǺgӾŁHАΡàÌȅ§ȳԛέɃԢѪđbckːψ',
                                                                            'ϾĨ¦Ϲ¸ːΫъňŧуҡύƔд˧ҮƘ#ѢыưɔΑʿр˓ͺĢϹ',
                                                                            'Ėʳрėmӡŗϧѱ{şκЊĚХ˨Ӿц͵њǛ#ǽщ\x90ҧԭόˁβ',
                                                                            ',*ɓɛþІ\u03a2ǩĀҸ\x9bĭɊԍǉŭQêIԗpˆӆɪ>ʵҮџҬȁ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ύµЇkԭʬqÍΏϭ҂ѹЎ˲ɔȢɾнЬӊǩ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172753.389379:+0000',
                                                                            '20220522:172753.397236:+0000',
                                                                            '20220522:172753.405294:+0000',
                                                                            '20220522:172753.414366:+0000',
                                                                            '20220522:172753.423788:+0000',
                                                                            '20220522:172753.433394:+0000',
                                                                            '20220522:172753.442914:+0000',
                                                                            '20220522:172753.452512:+0000',
                                                                            '20220522:172753.461832:+0000',
                                                                            '20220522:172753.470692:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϿԪ×ҰԄ$ǅŕχʥΛ*˒ư_҇ѦҸÜ³˲\x81Ϋø»',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6116434748705726596,
                                                                            5061881741842246236,
                                                                            -3541481640580294642,
                                                                            4162121465358859875,
                                                                            6325029060256731174,
                                                                            -2283249404577883042,
                                                                            1775774901406531788,
                                                                            -9113532500009779434,
                                                                            6967091993348325829,
                                                                            -5828786808350545902,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\xad˾ȢӕĺԊӡɋƳƁшˇ͵ǠΖÖ¸țӤǠɫȥǛΰΗvbʬʪĹ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172753.631035:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŋƕԝϓʫѰѰЈǻRόŜʑ϶;ǌҚȫҠϤſӤpɡġӦĸ;әú',
                    'message': 'ҮңӰȢďƍŌɮμ˰³nʿɗYͿŰp˻ϕǃҭǗíȿÇçÝӵ\u03a2',
                    'arguments': [
                        ],
                },
                {
                    'catalog': '˷бĩ\x8eCƲΦwŠĻĸȣЄЅҐН¥®ӘϺ˔ɁʓƺǏɑʦИӑé',
                    'message': 'Κ5ͿǓѾʈǈ\x7fϥӝ\x93ιǨˈϖʪΑϾǥɎʜ*ďԬѣ\x83фˌɜ\x8e',
                    'arguments': [
                            {
                                        'name': 'Ɛ.˩й]]Ϣʺǁȡǫ˸ǻ&ˉ˅ī¶НнƏМӒŔƐ\u0380°ϲ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            939573.6034405988,
                                                                            -91808.93343760289,
                                                                            894735.1091341509,
                                                                            9878.158050318074,
                                                                            438.39638151628606,
                                                                            783406.2988357826,
                                                                            508209.3591679735,
                                                                            84977.08008003203,
                                                                            803281.9821097341,
                                                                            -63268.62347458911,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҿԨòüѬѮưưωʄɛӣNÝªǿҚ˻ζßǝжԚȖǼӜ2Ӑșĺ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
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
                                        'name': 'Сτʪ\u0381ЏɲДҪӯԣƯ˗ðȨ\u0380',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172753.967798:+0000',
                                                    },
                                    },
                            {
                                        'name': 'дȣҌ˓',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ïǄʠπ҂ҋʴǖ˘͵³ϫ\x94ǒҊʁ\x94˖ѩĭĨŬʆʇ҅Σȑà',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
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
                                        'name': 'ʳũ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
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
                            {
                                        'name': 'ϺРΎqУɹˌ\xadȦ\x8cπԤRԅpȗѳɷӿηѝƳŊƭtԠӸўȍf',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3899216703781513048,
                                                                            -7669107244464786738,
                                                                            -6187745253547374703,
                                                                            -3415714253804543765,
                                                                            6570072029593996830,
                                                                            5921072797659910221,
                                                                            -5056313911510732819,
                                                                            8328325089403570823,
                                                                            -710484701877889814,
                                                                            8353841879679755530,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'íǇҊӋÍʅɩƳDìԓƕɰȿϲʕӻŜ®ŃǠΩ˙ȭʐ\x98СŞƻ\u038b',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǧƂƾϻřц\x93ÃɚϿȑ˒˔¹˂ʰçǏєʑ°x"ɲƾԆѧd˖ρ',
                                                    },
                                    },
                            {
                                        'name': 'ӌӆͱҵɘXѼêúҠɯΪѮ҇Ĥ¢ßɲ`ʃ˾ӉʰɗқĬʒɁȆЬ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172754.430980:+0000',
                                                                            '20220522:172754.439953:+0000',
                                                                            '20220522:172754.447830:+0000',
                                                                            '20220522:172754.455810:+0000',
                                                                            '20220522:172754.463711:+0000',
                                                                            '20220522:172754.471737:+0000',
                                                                            '20220522:172754.480770:+0000',
                                                                            '20220522:172754.489892:+0000',
                                                                            '20220522:172754.497759:+0000',
                                                                            '20220522:172754.506179:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ϝý'˸¸ɲĘșƪ´ãŪϗαѦ",
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -28080.723003511142,
                                                                            820412.8092740033,
                                                                            630473.9477744098,
                                                                            916657.8237378208,
                                                                            417233.4217001392,
                                                                            849457.8754964266,
                                                                            138644.95741256597,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԝϥǞҘɧ\u038bʎĭȢʈ¢ɜ҄`ӈŻ˞ˏȓЋĕмɀǨɁΥѻľЙƛ',
                    'message': 'ϝĤ\u03a2ř˕\x87ѽӺÄҨгϺ\x9fтΌӄ¶ΆƳ¹˘пŌşѫıʏӕΨ²',
                    'arguments': [
                            {
                                        'name': 'ȅ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΪӎΚƼŕýϜԔԐƗ\x9fȅΈƒƭǭԎ˺ťq˫ŇҭʵГŪˀǆԫ\x9e',
                                                    },
                                    },
                            {
                                        'name': '|ÉǂȨƸƎĖ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            676999.684970541,
                                                                            547371.8690722208,
                                                                            658179.689440248,
                                                                            573206.2713187395,
                                                                            279053.1418885001,
                                                                            982743.9909183332,
                                                                            -96515.90965525877,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ξƤʸ+ϴҾ·gцӯΓΙ˚ʔʖέʅˡѹ[ӿ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3527164315260379214,
                                                                            2275044439790026427,
                                                                            -2402867525226368365,
                                                                            61902747199919561,
                                                                            3754937122705623732,
                                                                            -6655705115850148880,
                                                                            -8097880920893694462,
                                                                            3464821559973906038,
                                                                            3014937865853521445,
                                                                            5975210837702947106,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѣϣɯ˱)ȎΤłƢGǉįзÆ8ŬĪmӉНºϚҭΒtӰð\x7f\x9bЅ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': '\x85ũŃԥŞʪǪß-ȂѯʎȭеõπˀжďJȋµǥ:үӗїʩs˘',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5110442110385455319,
                                                    },
                                    },
                            {
                                        'name': '¯˧ƳƣΌ¨òԋ\x86ȩ;йĬӌȠ΅Şv˧4҉ȏ¢«÷в;ӰҔʮ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȢƤĞɦԫÒģʫʾΆ˾әЫʞĂ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӕΊΌɐ˄ƁűÌɾĐϰýTϹιȡΕɑļBБͺԬaЀȥɤϦЁ΄',
                                                                            'ЯʢȑʏнɜΆИ7΅˰ЂʓĉҞĘɧ˲ŽӃÁį¦ԝ\x89ѩϲȏǽЕ',
                                                                            'źšĩ϶Ӑ˕ъԮªȽ҆уíԈȩƳp\x84ĎuƲÙȶǀ\x99Åé˖ʛϟ',
                                                                            '˷ӞʦˏҶѻФӥΆҘ҃}ŚϚǖȤЧɓϛÝĽқºчƷӫҳĤȸӋ',
                                                                            'Ŝѐ\x8bԨѼѼȬȿ\u03a2ǅΜ:ԂҡҲӕ˅ơхԩтŜˎѾ ϐІîǳЧ',
                                                                            'dӵǧ^KŵŰӜА˶ԤԛӶºzƑàϼӅɮрͺŻǞǏƷǠԪɺ҉',
                                                                            'ǖΕ\u03a2ͼг˹ӋaëɰƮӶԔԅҊѿɗҊàɧǢ¨ʻ¿ƝӰęĲǆў',
                                                                            'ÓʾˌTӆʿѵϔåȼЃԅ\x8e˻ІơǁѤʜөmӹɿŅёʦҌďΡu',
                                                                            'ƒ7ˤʗʮɚϰӄӀ\u0381ɾŚƟʹѪӇЌ\x98Ň\x91ѼеĨʮϾʡʇΚ¥Ģ',
                                                                            '҆ΒwʰɎҏЧõÚʿ\xa0˙ŸXϩҥԟʢ҆˩Ȍ4ȴâΓe˕-ŬĶ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˽жÃĮƴӺ8҉±ǧӍĐȣʈčϬ"αéΚˆˎĒ¥ÊŴŵ+Ǭǭ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172755.234839:+0000',
                                                                            '20220522:172755.244024:+0000',
                                                                            '20220522:172755.253572:+0000',
                                                                            '20220522:172755.262436:+0000',
                                                                            '20220522:172755.271685:+0000',
                                                                            '20220522:172755.281009:+0000',
                                                                            '20220522:172755.289858:+0000',
                                                                            '20220522:172755.298881:+0000',
                                                                            '20220522:172755.308339:+0000',
                                                                            '20220522:172755.317048:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '»ʟŷiΡѪ¨ҠϧɄ±ԣ˭ĭ˚έД\u0379ά×Ā3ϱϊ¶ŸÐԙӲʴ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʵϰԪΟíȡǂŏG˅ν!Ӹ҉ȇϔȗϣɇ˹Ӽˤ\x9exǑϦĬԎɊϯ',
                                                                            'ýϕңţΒҝиəƍĠĪ҈âǗő¶ҍϚ˧ɍҧţЭʘ7γԄ=\x8cȂ',
                                                                            '˦Ҵ¦þ˺ǸΔ\u03a2˪ԨЧԚʙĎǐķϼѡШƓŒ)~ȯϜ˅ʄҾ;ƈ',
                                                                            'ɛŪŬѴȰȾʇÈШοӈƸįƘϜ\x97vǄ\x81ӉˇΒϋʺ˲źӢO\x9eС',
                                                                            'ӹΩȤΧӼƶ˭ӡʰҞŐѯΚ¨чɶЕŐʰǓ5ӀûМÐłϬȲNϩ',
                                                                            'χɴ˓Ĉȼҁĩ4İĉΓƺɍąѪƔ\x84ΞˠDвҊ˂ӋƽĚʰʸȾʋ',
                                                                            'ˌʐδҨѦǒԢԄӷǧЯ9ҶґԅÓΖȳͷҥѹ°ΠŽÔԛԕɗɠΣ',
                                                                            '·\x93ƶͱӵǀɈzˬоОұ˴ĽÏƾϻЌь\x81ùʱůԤĢ>ȿȝbң',
                                                                            'ǙԠǡʚƜǂėфȺ\u038bġɈÄϒύȷΪϦƴӚ\x80ǻ#ĺMǽӕv˹Ć',
                                                                            'ǆ£ϣѢYȍԧǀƉί\xa0ŏŕ¯ǧªа:ϔӾԜӾÚƯVųΫԤŷҙ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '@ÂѦȧé!Ӗ÷Šġжςҵs˟',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -443681354988553214,
                                                                            -3567785061085949361,
                                                                            -8684234128138772063,
                                                                            6482328953628541814,
                                                                            8403085451021029084,
                                                                            -1317394914402300689,
                                                                            -6571081130906422833,
                                                                            6903356022847619314,
                                                                            -2680379433332616633,
                                                                            -3016269013762841902,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ĨѹƥоΤǁӡè¹Ҿ҉ѸȏѪĪ˹ǟKºŷ˦\u0379ƛъÌźʪȚʅͼ',
                    'message': 'EͷćѸΈоОdȐɞвӹWˣȾǑыϱιˀBǟ\xa0ȬĿõӠʌAɉ',
                    'arguments': [
                            {
                                        'name': '\x81hЗ˃ʷˇ˫dƟԒ¡',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ăɛŹԙɦɯӸԗɧʆϱӝ˴ͲˈɪŜ1˙ӚȨťơ·ӧJȯĩŪh',
                                                                            'Ҽ?Śҁï¹ȌǱɖǕ\u0380ʲϤp¯ӌřśɳǇ©ʰ˕ŌŉʵХΊīѣ',
                                                                            'Rîˈɭмǣ҆ĳɶѨδҫiυʖŲФ´ɌҸːĿašӘƖȁҢɐϊ',
                                                                            'ϻ(ʥϓӇɗƾлŚ+ҔіԖʂšƳɣη,Ǻҧɱ˻đφÂӣȣ\x94Ѽ',
                                                                            'ϘїƃǝΫӭʕ˼þΒĈѨďņśȕɏƚȹӞЭ¨ΐѶǞɽ˗Ԙ¶ј',
                                                                            'ҢΥ~ůЦ}Ӱʙ\x9cʉ"ҮͼѹϩȴάɢƣѠōÚɵԏяʞҵƦ\x9c\x80',
                                                                            'Оʵâԑ˱ҰBτƐЫɤҵ˩ϯčŇӘгĘɈ\u0381ż˼˖ˆġʭ¢йҸ',
                                                                            'ÙŤʱ˳qīŨÙίșόźâÛƼxŕǰˤԣY\u038dɽҩǠȋɶϭɄƣ',
                                                                            'ǳǊń˟ѢΝ\x87\x9bӧОϐú0˯ȼѓǧʼѭǅϵķʮҹRɎΌƀЉ\x90',
                                                                            '´˅ǰƥҍмïвԢȊӬǧǬTėƲõX©ӳŝFƘūң˳ҥɃg=',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҆ƄőѪ\x9aҼɥӉǐ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 530981.1245943255,
                                                    },
                                    },
                            {
                                        'name': 'Hϔ¶\\ʭӲĎщʊ˻ɈĘϥ\x94РƕѸȼ¡ԥ¥˚ɞшфĈƔr|¸',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 774141.5703292408,
                                                    },
                                    },
                            {
                                        'name': 'ˋҠ˯',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172755.830206:+0000',
                                                    },
                                    },
                            {
                                        'name': 'kȢϐcʔϹšʣǼ˥аԫǑX˩ǄӦ%mǴɳ\x86Óȗ¸ɚņеӺτ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 837846.3413737095,
                                                    },
                                    },
                            {
                                        'name': 'ʾҲʜŌʖе˥Ѓǩ\x92ҹÀ¹ʌӋ+эƩ\x8aŔţϺӂӽΞÆ*ɽƖȥ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2253076969627950725,
                                                                            4612308422121101811,
                                                                            -1543738944874479444,
                                                                            8300533399046487330,
                                                                            3952371389213245226,
                                                                            -3844989204251272800,
                                                                            7496282572652828791,
                                                                            117144318387756729,
                                                                            -7455114014692702164,
                                                                            2812172226860848685,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҍƶˊŨхȈɶğɠťНĨόҎ9=ǰ\u0378ŤӶɾӊ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            613522.601946216,
                                                                            988402.8174691682,
                                                                            724171.7371689309,
                                                                            -84503.62137520911,
                                                                            210332.691169188,
                                                                            219147.53709511872,
                                                                            -8375.878001924983,
                                                                            825276.2052166748,
                                                                            879881.9260384054,
                                                                            265120.701773143,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƚҽZÈКѲԧЮѭŝ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172756.140172:+0000',
                                                                            '20220522:172756.148157:+0000',
                                                                            '20220522:172756.156991:+0000',
                                                                            '20220522:172756.165824:+0000',
                                                                            '20220522:172756.174022:+0000',
                                                                            '20220522:172756.182423:+0000',
                                                                            '20220522:172756.190666:+0000',
                                                                            '20220522:172756.200092:+0000',
                                                                            '20220522:172756.208671:+0000',
                                                                            '20220522:172756.217193:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӥȡ%ŒԓƀŽ˼âμϽӺ΅ҏǓѯ\x8eǻŜŰ˙ґūǰ\x93ɺʛƝä˥',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1551637310120381854,
                                                    },
                                    },
                            {
                                        'name': '$ĜԀҒ\x9bѺƶìWŲԠŜӓĪԣ ΠÝƶlɨ9ΥϪдĎğӺʍԈ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5762532588303640488,
                                                                            -6002587904099524899,
                                                                            -7656949581948464650,
                                                                            649680271165211644,
                                                                            6885886042009040270,
                                                                            -9013958943370957965,
                                                                            6322093608697628455,
                                                                            5353884268611209908,
                                                                            -8748462660596913487,
                                                                            -1153142387202232855,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '$ԎϪȖЂ˂³-ƻϛƆūȹͼџǁŔљ°ȢˑȀҧӋƍԞӫɬʻч',
                    'message': '˒\x87Нϔͼμ\x95HΈəʟ\u0383ƕǲ3Ȗb˫ѢБ˚ɻ˘αƍʈ˰ҤРF',
                    'arguments': [
                            {
                                        'name': 'ơŅ˂ъдhʍŕ¯ϡȠ/Ӊǌɖȍ÷Ӿ\u038d',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ζÒΨϊƫѩåžȁʉƫяǑÔɀӈȚάҩöԈĠȧŁϮӝš§ˠF',
                                                    },
                                    },
                            {
                                        'name': 'ɦОӨƾåϽÖ,ѢHʕŻӠĎ\x8dʞΣϒÝÉӴY',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'łЃƾӇЋ˱ϾԍŹѾάͿĥĖɾȊĩWƚδȼĎƌïέǱѽʄʔΞ',
                                                                            '^/ҠƜӣԂОüȥҼȲξЋFȑӚ\u0380\u038bыӒЎŅȃѶƴμҘǰnƵ',
                                                                            'ȑ<ϬǒϨĶ4ТƟǁȪИƏэԎɗǅ\x8aǑʘʘоѰ]ʂĸąφˏĚ',
                                                                            '0˴˯ɢϘƘßʀȐ*Ŀ˰ΒгǢҜɕҿΊįÅүǚáƁ˔Äԉ?Ȩ',
                                                                            'ƒФҘț5Ŏ¸ѸǭϾөɜLiӂϵǻіɣȣӿ Ƹ˰ŦШŃʵǕА',
                                                                            'ЫφǜԊӧђĈǉʙ}ҧĲƘĄȻ\x93ʐҸʯ\x94˽Θ˴ǐȽɉĦǻƿ\x9a',
                                                                            'ſԑǸѣŌǈǂ˲ѩΙϠż\x85ʘĝɈǼĩƆюΚϑǣĂȮ\u038bʻϼø+',
                                                                            'ô˨ϱȂþҰΖʾǥșĳ:ϋҒnŃ΄ЃƨȔǟϒǎԭȲҊxƛјɡ',
                                                                            'ŴþƩ˛ƐȊ¢ĳϵȂŻіȹūËŤͱȐſřΗғ}áϚǬȝ0įP',
                                                                            'ͱѝϥAǫϻħӬƘϥόǃʦʜѕ¤ëŝƭǬѝѮҵɕΞŢÞўΧΡ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƈØí\x8fφͱѬ˃ӮԙΝŧӳƭϯ;Ȼƫ҆УêͱҼȖɄѪƎ\x97òƵ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6406897022533188396,
                                                    },
                                    },
                            {
                                        'name': 'ØГnБǪƣöˉ˻ǽJ×ğнʔŜҰĻɗхȤėӊȥѐĹȹЀ\xadΗ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172756.642437:+0000',
                                                                            '20220522:172756.650888:+0000',
                                                                            '20220522:172756.658741:+0000',
                                                                            '20220522:172756.666581:+0000',
                                                                            '20220522:172756.675638:+0000',
                                                                            '20220522:172756.684161:+0000',
                                                                            '20220522:172756.692166:+0000',
                                                                            '20220522:172756.701358:+0000',
                                                                            '20220522:172756.711056:+0000',
                                                                            '20220522:172756.720077:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϱˌ˩ƅƙ\u0379ͽ\x9bѼɓ˫ƾǥɻϘӥɈ˼ãǊĂ҉Ґ¤Ŋð',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӁСϩԖїζԒ˘ԜЃ˥Μ×ΣȈΉ\x93˗ȑơʌǼʬϙǝΆuÀВ!',
                                                                            '\u0383ϴȪДǮUӦXʧ½Ą\x9cʚ:Ɏêз3Πə˯ɲ!ÎЃǦʕșéá',
                                                                            '¥őэŞȥϻŖȸŗ\x82Hå\x90ϡϡҽЇȗƩƹяĳĎȹρÖµϚƌї',
                                                                            'ȁƏƛŴѸѓͰаũѳЬčŰѫʦͱ¡˵ұìƞnҴΕɺʨŒЏӒϕ',
                                                                            'ϖҘɟѐѢέȕÄļƬӳŸϩ`Ҧ҂ƾȌȱʅûɵ˔ħǣӿӡСɼҠ',
                                                                            '\x86%\u038dɹəϢƏɌƩӹƞЪʾɐÒбȺӛȻÜ\u0380϶ʁŸǑŠԓ˂Ќ\u038d',
                                                                            'iǇĚʗƋύБԀκ«Ԑ˃ʪndàԠүͽÇЈɆԭţΊȃȕƥ\u0383Ɔ',
                                                                            'ͳƪŃƦÄʱMʔΒǧƌRǜʃзλůÌЩŧϨԃ˶ʯ˳ӏŔӴϲ|',
                                                                            'Ҧd˱åñǈ˗ŪΟР=ԠǷϭ˱ǺАͿĢ\xadɥũJӠä×ђɱ;˕',
                                                                            'ȩҙÕыѵæԃ÷ȎʥϼϖŹ\x91ҐѲ˶ÍЄʇΕҎ\x9aǞȧp;Žʆȣ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'šĽԣґɾͼʜҢ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': 'ʨ4ëӹʳƉąŏώEŤXԒяÞǤϭѴ(5ɬYɝͿÃƆä˼Ͼʍ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172757.004658:+0000',
                                                                            '20220522:172757.012407:+0000',
                                                                            '20220522:172757.021504:+0000',
                                                                            '20220522:172757.030812:+0000',
                                                                            '20220522:172757.039630:+0000',
                                                                            '20220522:172757.049111:+0000',
                                                                            '20220522:172757.058183:+0000',
                                                                            '20220522:172757.065961:+0000',
                                                                            '20220522:172757.075322:+0000',
                                                                            '20220522:172757.084312:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'wĀФ˖ǧªƬʿ·?}ǿǃƣ\x91ƺԫ˞÷ͽҍž\u0383Ĝɺώ\x8eʬÆÎ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x81',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            902145.5507652967,
                                                                            894254.881006001,
                                                                            172867.61950998264,
                                                                            680201.814303028,
                                                                            706667.9248756897,
                                                                            830391.404090016,
                                                                            414705.95557313145,
                                                                            848089.3812681239,
                                                                            572662.3020488123,
                                                                            339290.05004431575,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'țɒӽïǺȨӰŹɶƬÉɘŹʟӶҢβԝθǨƒѼ˯',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϭíДІTʢ҅\u038bĆҁʳƐíÎ˵ϓĝȝѿӼǫφӵ˽ˮʏǅΑ˗ơ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'иěƞɭѿčQΝӮĖ˕çǱĿʔʐ>͵ƅʦЍрΐҘȅͲԑƓt\x87',
                    'message': 'ҙѤΚǚ=κƃԂɺГēƓўuύȿarҪҍ˺ţä!˄ʉуԂ¨\x8f',
                    'arguments': [
                            {
                                        'name': 'ɘʓòҖå\u0378щϺÂɣʬҎЗBʒѼЄͼϏшДĒӨ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɨūʮMӋƫǼԝ¡FЌԙԉ˗ϞϣȎǕ¦ȼҥΚŦњǏ5ʲϙυ҈',
                                                                            'ŕҔȘǺҍ\u03a2Ѱ˱3ӜɴĮ\x82ǹӏŋǙԆ×ˌwËƽĩƆϏґ¿Жь',
                                                                            'ҌϮҹɱ˓èњ˷ϵΓȾĈӨΧӥϱоˋʉϼԔϏÁќˡϼvԞƭɿ',
                                                                            'ǐƂʏž˙×ҒЪϱǪȺҹÇƣlȤȜěȖƘĺʣ҇˨ӌQ˓ƫɊć',
                                                                            '6ɄΖĆȴĴԅʎњ#£ЎēďǳƷbBТpѿОСɤ҂ťfє˸Ŭ',
                                                                            'm9ЉưԇTϒʜԫƊғƬԍƓӇКϥĒѨċCƦǉȮǿ´Ͻƃģǹ',
                                                                            'e˕żҳӷvɣӶǋϡôҟɒĚӂ¦ҼƹҠ\u038bȘ˨хϕųȌƼҲjɕ',
                                                                            'ʦУÞһ҄\x97\u0383šǮ´ѝŲɭŋǇʽɀӹƫóƬĹñĪ>ԓϣӰԜǆ',
                                                                            'Ѝ˔ʔ¥дŧз\x80ͳyê6ÿħǞѡÔɡҋмoƽĠѽĽƭ$ӻǂŝ',
                                                                            'ԗȾ#ϻǮx˜ԐҎ\x93Ҟκɂ`ɣέҜŴŨçʢґ˟\x8dĮχĉŎĻÕ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'vѬɩϙРʕФˏɦ\x93ғëĝǩƮζ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172757.562121:+0000',
                                                                            '20220522:172757.570482:+0000',
                                                                            '20220522:172757.579966:+0000',
                                                                            '20220522:172757.587915:+0000',
                                                                            '20220522:172757.596714:+0000',
                                                                            '20220522:172757.606046:+0000',
                                                                            '20220522:172757.615045:+0000',
                                                                            '20220522:172757.624620:+0000',
                                                                            '20220522:172757.633926:+0000',
                                                                            '20220522:172757.642195:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x92\x9eƪ˺ӣŨϴ˳Ǯж˽ǹŎȿά\x7f5ϩʰà\xadһͿǼзɳ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ÍŌ϶Ƃɫ¸*ΦƂӮʍҢӠт;ͲPʅΗӾǸӿ=¢ϷbӦδĆЄ',
                                                                            'ǤĞҶȀίԤ°ʖʗ\x84\x9dǐ\u0382ʅс±ġлБɋ1ɛѽ\u0381О˙)Ǟʁӊ',
                                                                            'ȩжƮ˃ʳΜNȽйǵɡhѹŘ5ƑԞǐ\x80ԍ˯ѥͱÈɦÕɶԄɑȜ',
                                                                            'ǺͿԛǲ;ɦʫрϚʯ˩ɫυЄƑ[ӘƂÂϸʉɌ)ĳ~ӑЦϛɄž',
                                                                            'Уђҋğɥ¦ϼөŌґñŬőɠүԀțʱҋҽ ʄʏѐΓŬƬόQҔ',
                                                                            'ӷίԉɿÕŚҤ£ΛšΣíŗʬЧԤ¡\x8cĒ\x8bʛώ\x9dљŊЬϮщѰ˼',
                                                                            'řБîńʁȁȆ×ȝ\x99Ȧ\xa0ҏèɂ\x91(ŀʭфXİȢϿ\x90ӉϛрŹʈ',
                                                                            '.ҳҼǫƐǯƖѲã;ԏƋҀŎМÞĴʿė˞GѐϟˏȈҚ˶ӣ˒Ⱦ',
                                                                            'ԛǻѻӳҭǸɢԝӞΖΪȪҤѶ҅˙M\x8eȃςɨѹ\x89˂ӊ˶Õо¼Ҍ',
                                                                            'ǸȕƦgчϦұ³ˢЄ҄ҍҌ҃ýίҙҿǴŘ,НʊƍɰǸ\u038bË³ӟ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˚Ϳγ\x9eΤɫMɆӈûϡР\x81ŖģćϻϐªϚͽ˙ϻƤ\x96ɨϤҎϮǇ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            581985.8619789658,
                                                                            203780.99228692905,
                                                                            97158.22586059765,
                                                                            189721.19739793986,
                                                                            819386.5719534038,
                                                                            806337.8872330964,
                                                                            971642.167377494,
                                                                            566324.3517637482,
                                                                            444200.3433712573,
                                                                            122572.57066945356,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˻ɰԡғȢФǯĄʒɶ)ӓГyíW9вďҫͰ˨ɉѤӨˆџҍӤQ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172757.927901:+0000',
                                                                            '20220522:172757.936193:+0000',
                                                                            '20220522:172757.944551:+0000',
                                                                            '20220522:172757.952869:+0000',
                                                                            '20220522:172757.961451:+0000',
                                                                            '20220522:172757.969436:+0000',
                                                                            '20220522:172757.977355:+0000',
                                                                            '20220522:172757.986596:+0000',
                                                                            '20220522:172757.995736:+0000',
                                                                            '20220522:172758.005330:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԟÇƬȵЦ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4592850786178973553,
                                                    },
                                    },
                            {
                                        'name': 'Ť˟ԉа',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2391901159729829546,
                                                    },
                                    },
                            {
                                        'name': '˗ʕҮ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6105556738430346875,
                                                                            8524407973949566415,
                                                                            2700718516849341934,
                                                                            7188692360845292332,
                                                                            -6303828952628473684,
                                                                            1520849428053138759,
                                                                            -171122693430279605,
                                                                            7692582528329978962,
                                                                            491403192803738519,
                                                                            -8955520947765648125,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѣѴ+ħԪΖĚ½ˬԁϒҋӶɿόҁäßϙңԌȌɌ¹Ȓ˯ȀѵƲҔ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172758.237634:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѦɬȆÅу\x8fӻǔώȋšџϿɣǟԤ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172758.268702:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŰhǼ͵ϦǀЈƶ9Óʈƿɩ¥ȢÝ˴ʖҎΊ˅ԗǽӟśýŜȂŮā',
                    'message': 'ɮʉѯԮī¾$đԭȊbϫЍ±ҦӋĔрãҿρoŊλƪ*ɵƌті',
                    'arguments': [
                            {
                                        'name': 'ǫːǢ8пЗγ\x93ϷȴǊґƐęʊ+ДίŴϓɂʸƫ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            834784.1717745316,
                                                                            648310.712171601,
                                                                            169757.10627567262,
                                                                            273459.866865569,
                                                                            420817.3091818772,
                                                                            288524.06404963287,
                                                                            119672.65329115905,
                                                                            -82252.20762473915,
                                                                            423852.8559660239,
                                                                            952802.3345689173,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɄŢųß×їħưԍϷŏѢϺ¼ŭþЬɑϟ\x80ˬʿɑǀ-˔ŧўҢҖ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '£ų\x86ÏǗ˝ʟΰ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172758.494035:+0000',
                                                                            '20220522:172758.502671:+0000',
                                                                            '20220522:172758.511474:+0000',
                                                                            '20220522:172758.520213:+0000',
                                                                            '20220522:172758.528128:+0000',
                                                                            '20220522:172758.537031:+0000',
                                                                            '20220522:172758.545764:+0000',
                                                                            '20220522:172758.555293:+0000',
                                                                            '20220522:172758.563684:+0000',
                                                                            '20220522:172758.572544:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƥšӫΔŏǹȢҚабϒԇГď\x8dά',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6914672771355842148,
                                                    },
                                    },
                            {
                                        'name': 'ζΆҐ\x9a',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2866208245728511552,
                                                    },
                                    },
                            {
                                        'name': 'ӼӵϗũІʷ{ÕʗƅɉįҜ5',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -22041.372290094267,
                                                                            51659.98528221884,
                                                                            242739.24386801134,
                                                                            815343.9169636179,
                                                                            942262.5462699297,
                                                                            924153.1888800726,
                                                                            70830.62831564681,
                                                                            633034.8269728379,
                                                                            417241.5813116162,
                                                                            668481.4599572207,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¬òŦʮɟӃќǫȦŜƇҖ\x92Ԛ¿ÂҾҊĄáʸəǵçӮѽɑÂӸњ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            615242.7305266794,
                                                                            640755.869101079,
                                                                            534936.1371332756,
                                                                            129691.72706084189,
                                                                            801001.3874821035,
                                                                            976785.5883285627,
                                                                            706739.6119956714,
                                                                            -70183.74146696248,
                                                                            137257.18341966663,
                                                                            528494.65822765,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҋԄɘ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1350346685301093190,
                                                                            -2315795159128372618,
                                                                            1661822195288627881,
                                                                            -6313881198791851174,
                                                                            -7000446267860682635,
                                                                            7432868572724522213,
                                                                            4536372468689236997,
                                                                            7194635157155422895,
                                                                            3513557409042810719,
                                                                            -355777642453320647,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҢҨ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɠҀƇёқԣơэfҖȋʣǹ˦άсςʼʖ\x94ĮъǈӶĒƪƶѰǑ˖',
                                                                            'ſЫϬʆ\x89ʟƻϘΡÐ2˔îӳÂϽϹŪЛÂӟÈ&°˦ǉżʁăί',
                                                                            'Ҁёȱ˓џʈҒ0яԢӺŪ#£ҕ¢ț÷ҌǩƊÚҔäѻÆűЋѺʛ',
                                                                            'РҁжɓžʹÁʊˆĒχÙ˭ӹŢçǞʣӐǂ\x90СʗÝïѯɚϒĭώ',
                                                                            '˖ǎѓФʎΉʬҎь˳Ϗƞ\\ԭфé\x95ȒȤÈʄ˘\x8dοƌʦ·ʓĆą',
                                                                            'ĭөM˭ЊΰˠѧɃǂʖŢĘ:ʟԋϒȝ¥ёȓĝҨɵŁ¹ʄƪ˳?',
                                                                            'ŴԝӪʒȦǬԘƪħӗɘȔӵnʎҮҶŻ˗Ŭ×Ǧ\u0382Ơ\u03a2,ǀyЏċ',
                                                                            'bf_ѲġôӍƹ϶EðɲΗģԐȪОŗѐәŢтɶЫʼʻΦ҇ԋ҆',
                                                                            'Q˞ЖoΠɉӵIʆ]ɲʝɷÇˉғқȺ\x92ЯǕʭɛǼ˼ŲͿUԄ]',
                                                                            'ҰȖʅѺϯƢʉlΦȃԞì"āɖгčЙʿǴ¯˰Σōˣό\'Ǎɳ\x83',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɲҗɧəѺӚ˖õөĭˁɃâтǈ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172759.172260:+0000',
                                                                            '20220522:172759.180338:+0000',
                                                                            '20220522:172759.189516:+0000',
                                                                            '20220522:172759.197709:+0000',
                                                                            '20220522:172759.206961:+0000',
                                                                            '20220522:172759.215301:+0000',
                                                                            '20220522:172759.224050:+0000',
                                                                            '20220522:172759.233381:+0000',
                                                                            '20220522:172759.241763:+0000',
                                                                            '20220522:172759.250287:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ńĕɚѺά˞γϫѹ?ԆʲʴӼȏͺüØХŏŚħôъ˾șГʴĊW',
                    'message': 'ĈƻӴȳĮʜTҼɷ˸ɷĖȔԟǓʰɝ\x82ћĐgOͱĐІҾӛǕTŅ',
                    'arguments': [
                            {
                                        'name': 'Ӎ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 727370.6091861657,
                                                    },
                                    },
                            {
                                        'name': '\x92\x90аЁЦϮ?ԫê\x8eϔǣʈƵϹʸȑҸƪВΎłӕψȍ\u0383ѪΑíŰ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 933141.4430450748,
                                                    },
                                    },
                            {
                                        'name': 'ʞԢДƷԖѴԨӸ\x95ǲɪЩÆsνφʑȑǱЩӾ\u0378ԙ˪\x93',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220522:172759.397221:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϸȋ˥цʗ',
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
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʬòǏǭǴΒϼÌħϴĚʨƝgñȃʀóȵΕϟ΅уƒ:ˢBċȗƍ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '҃ӢƊÃØѵ˳ʒʹȫ҈ƫǅ$ˍԠÏєԭӇΓ\x83КÞĕƦýģҷɐ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'қЈԍɖˡΩʃƻǴЇßϮɿɹǈëΰǏǂӷӰˤјĜœƩ˴ɤɘԖ',
                                                    },
                                    },
                            {
                                        'name': 'ŏТçбˋ\x8cƆöѽǍȣʦϸơԏɔĐ\x87Ȱԗ>ğΑȣϫҔʼ}ȸѹ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 9373.848847234796,
                                                    },
                                    },
                            {
                                        'name': '˩ȬŲϱɬĞʅӮɊǜƿğǺ#РŒԈ!Č$%§ɎȖȢȐλåÜź',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172759.658990:+0000',
                                                                            '20220522:172759.666842:+0000',
                                                                            '20220522:172759.675904:+0000',
                                                                            '20220522:172759.684126:+0000',
                                                                            '20220522:172759.692131:+0000',
                                                                            '20220522:172759.701368:+0000',
                                                                            '20220522:172759.710681:+0000',
                                                                            '20220522:172759.719714:+0000',
                                                                            '20220522:172759.728384:+0000',
                                                                            '20220522:172759.737853:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӥ$ǶǿX=Ò¿ˆάҮҜѽRȕɜОɧŹȊɝłŽ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4812472019580652552,
                                                                            -8919777427877417923,
                                                                            -7423892599275170029,
                                                                            -3983934944012785018,
                                                                            -9212158728241039305,
                                                                            -3080928973105764165,
                                                                            2052798321883253735,
                                                                            5786833897942101032,
                                                                            -3311594030886184186,
                                                                            -529678167905457181,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĎʾȮϱ\x9fϱ˔šˉκ×ʴКԣӫ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220522:172759.904403:+0000',
                                                                            '20220522:172759.913836:+0000',
                                                                            '20220522:172759.922391:+0000',
                                                                            '20220522:172759.930889:+0000',
                                                                            '20220522:172759.939851:+0000',
                                                                            '20220522:172759.948883:+0000',
                                                                            '20220522:172759.958421:+0000',
                                                                            '20220522:172759.967862:+0000',
                                                                            '20220522:172759.977126:+0000',
                                                                            '20220522:172759.986529:+0000',
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

            'identifier': 'ϫϭbѧɒ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'ĞŬ',
                    'message': 'Ȇ',
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
            'name': 'ǳΈ˻ʴʻЃΠ˫ҡqĎӐfҁɦϝώ¤ӔʏʋȃΨ˅ŔǕԄơҘҚ',
            'error': {
                'identifier': 'ơȊкԌңſ˯ŹңҟӬƏʢȠđț/ɝȺşШȎƚқϜ¦șԍqB',
                'categories': [
                    'file',
                    'configuration',
                    'access-restriction',
                    'invalid-user-action',
                    'os',
                    'file',
                    'file',
                    'invalid-user-action',
                    'configuration',
                    'configuration',
                ],
                'source': 'ūѺҮԉλʹіãφlӾ\x8eɀȂϥ˘ЍyҤ<Ȣ/ӄĹъ\x92pɡ\x9eZ',
                'messages': [
                    {
                            'catalog': 'ÒʷҋōȶӫƥʑХ\x80Ųϙԋ\x80˞3žɯǿȬϗԐâδ»qώʌȦԍ',
                            'message': 'Ҏ¦ĝƻΐ3˃ԑƁďѹǜӕγһŬЀ\x95ĹʏʋʒӢŀȚԑϚ\x9f҇α',
                            'arguments': [
                                        {
                                                        'name': 'ͽУͶǲÆĂ~ɛşӟˑƓλѼό¶ԏфυƠʣʺõϗ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172749.545013:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǫĆőǴʱҫωњϘ7ćǑ çćɛŐӋƕ¿ĒȔԍӳΝȮ˷ºɊ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172749.586670:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'öιñ˚ϱϾÏśӀ˕ɔѢͱhͱǾ-ȐθөϮΊı;˞ÙǐpӚƁ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɩӇuˏɃԜԙSȫȅ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԐƙиKʨuÎYѤǧʭğұʋĤÐáıżĆ¡˽¡ƻɈ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x81ƬϞOϰЬъԥƛѢ ԉΈХϞŌƊʼҌϕŷŮԞҰўˬÍǣϥˇ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɾтԩ(έŉʉľ\x86ʾӀҟ\x90{СʱŰÃȨ˗˯¶ǐȆǚyƂòӆ˥',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172749.725366:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӽ¥éŠfǞĤşÔƟӇ˖ɆΪӾUѹǒ¿ϵȪʘѦάʏ\u0379ψҦԜ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǛÂĻŋ˖πƘӂŘȔʞ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'βĄСйŰΦϋç8Ӱ˸\x8cлǢɧΏƱҳˠ÷¾ɇŸʬшÙ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6745535607446386716,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЇԞҎȝǎô\x90ïԦӹϋ˝ɒØɎȮ¢/сϸи_',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 765468.7642355686,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'qÑƽƽͺґĄʅѿȳѰĞǴǉu9жƶÉ\x99ɑÝiϲˈ҈ƞе˻Ő',
                            'message': 'ˤЉєĳВÊſǼğʸȲʮƩΧ\x93Ѭɻ҆ŌƍΌʤѩɿǠˮԪĄyʯ',
                            'arguments': [
                                        {
                                                        'name': 'ѝȆeӞĄɖЅª\x9aмîðМ\x88ƛˀЛтͻ˩mʦӛ˔ӆάӦȪ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ғÓģОȱD˨éϩʯ\xa0]ɨҬҮΘĨЍάȩҮҌƤŢ\x89mӛӉȱО',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ň@4ԭӂ˞ĢÐ:ȭƦ˓Ϲ˂ϡ·ˎǽʣɎȗǌӯԡĎƭƶʋ˕l',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԫ¥ϴüVǕŪЍӋ\u038d÷ӷʩĥюŖĢԦԉɺĀƦđʦМŐʰє\x8cΡ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Űŷ˜ˍĵ˻ԪȳȬĤЙͷ#ŤѸΦĻ\x8fќΥҙǗƗAľюŖӓÀ˞',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'pŬϲѧҌʭΰƬȠʩůʖ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4815698755904359910,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӆˤӿНвÎÝΚȡωʗȫҜҿə\x91\u038dúǫòD',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172750.146887:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ХɖïлĜøɾӪƞӁÛÌʽʱѶ:ϹĝӳӍTрÿ˙Οҷ~ӓ[Ҽ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 613151.8181244553,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƣЏϝǅґԖÇ®ʪéˍҚȁĝҽêčĮ\\ҚϢчγɢˌC5ˮԒ°',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʖϩL',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '·áѢæҌƋTҜɛԖ͵ɲ΄&yғŃԌ\x86əǪξԃȭѳԐӛƱϽɂ',
                            'message': 'εàʯҧ˂ӘϑʂˆɢҕΐȦϺˏ¬˹ɅȖ\x93ѼǩɔğҾϪƀ±Ӭ_',
                            'arguments': [
                                        {
                                                        'name': 'ѭDęęгԄÆǱνȡœϭƝ°',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԭ\x8eͿ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΑΛĳѣӆħA7.Kʿώӈρoʏ¯ǈÐҝͳ˖!ɼȄԑ@ĂĖʰ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԚȹыÉ%ыԮơǤʅɤ˯ǏѱƃөǧҎΌxƙКƵɉʉЪǈӂ\x8dù',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 169527.92015876673,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƼɇϨÂұЗʖˏȂӻɂŝͰųͳőǩʹďЬɖ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 54947.13082327621,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʄ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ίɤ®ȧ8ǧĈȲšȌȅŝϨāǱĦAǶ˰˺ŦԣƖŨ˝ΚΈͻɿΗ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЀΟ˶Űöą_ǏˈîѮЍԪΘӵ\x82Ā2҇1\x9eΞώȔжɎΨřӰŉ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ôƾúŧe\x97ȸǄƠ˩ɑͽѺɔˮúűΨˍӠōǂΉEȓȚί\x90Ƃɓ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 7335.551607483605,
                                                                        },
                                                    },
                                        {
                                                        'name': "ʶʕ˨ѺӀȀЄ\x96ƐeM'ЫǢÇ\u0383ӟʍȸѧĞɪƙъEЊɮɭРȄ",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '÷ɴýȜȝƔPЧӺλкЗˡͱ;»ρǷˎԆˑʘƄ¶ˡ¿Ƕӫ˃ɘ',
                            'message': 'Ťч˅˰óӄЙԧҺљäӪϝ¶ǕƔĈƹ]ыϯԊˮғ˦±ЍĝЌğ',
                            'arguments': [
                                        {
                                                        'name': 'ǃŏԋīΡȒԣŠÊLC±ŃŸȔųМХvӸϷϮˢ\x9fцţŽҰӿu',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ͻȉ˱Ƒ¼ӁѓC8',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 241412.08576861233,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʑįѯʈǣȆϽ\x87ЍŋЯɤϫp×Ǽ[ϻпҨӶǧԪòсż',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '·ǸPòҧqұωƀԆ˒ӞӭƐԃîɲўěǽ˳ǴʩŅϧ˔ҽ˄вʜ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƒ÷Ӌeӄҽ҉§ɩѵȠsśƎǪÚ(ĸЦͲßpԢWŹá',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӯǭПΙ\u038bĵ˪ԔTѐĢȹΞϛYƓƉșŜͷ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʴƂˈǨǕϥԛɫѫ҈ѴſӒÌō҃\x8dtʍɘϦЧ@.ǈΒΑѺόʽ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЕνƅЫϣΙƦϓ9мɴƗӠ&ХԠςęЈƱӺҿѝӍΞƵʔΩΒţ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 802370.3862699898,
                                                                        },
                                                    },
                                        {
                                                        'name': '*',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƏѸǐҋ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 133009.78280130416,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɯǴɽҦĆȥΒ˳ɮϹɣÉӠ$ɠӄ\x91љƶÇ4ȖԦ¸ϸ)ȔŞ˯ҳ',
                            'message': 'Ϻ\xadпľ¼Ʒț[ΙÌ"΅ÖĬ\x86Ѽқ¡ǖ\x96ʋ˜ȄʘǁT½5ȇ\x89',
                            'arguments': [
                                        {
                                                        'name': 'ȫƙӢ˖\xa0Ѭ\x92˳ǮǩЯǑ˨Ҡ0˴śϑͼԉξΛȚ÷ϳι\x87ʪɒк',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӸÚԗФ҂ӱӐʀνŞbΦDʥǐ\x80ʹԗĘ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǍäˢĪє\u0378ĻɘϊǰҺÿəǨȏȺɢ¸Ԣ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'њѽO˲ƹĐΡ¡йrҬϺʊÇƲĪӟӄӞƒ`\x7fĉaǱŦϧӄȼѰ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'MïˇɅʀғ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԔīНǣʡēĆЖɶiǘəίˬҏʉ˃ƄʢάӃˉԂ5҅ԩ΅ñ˂Ɏ',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x93ϗС',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1641122955188093120,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǺɶӁϖѶä§˝|ԝϢмϥĴԬӞʋɏƍğӉÆ(ˬ·ҩҟЎʎҾ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'j4\x81ŏȗȣšͳfϵȐϛύY˹âђă˪¿ʰǧʿľΑ˙ʜ˞˟č',
                                                                        },
                                                    },
                                        {
                                                        'name': '¿ъѵʩ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˂ȤϦүρƲԙȬłĺʌԩʛơǬxǹї\x97ѡ\u0380',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8486628234605249402,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȣņȷӨɲˇƁċ˖Ӻͻ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'eΙşю҉Ƈ\xa0ƸɹďɭĤҿǳЯҢƋͿԔԋ¹Ҙ\x84\x89źʬþǧԣƫ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4047756451084958771,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϦϞѓҿʯÏȻь˱СìN˙ϚùΎǙʺӸưŦƵЧʸϼƑ˫+ԪȜ',
                            'message': 'Ǉ\x93\x93ǣʜʀ˯Ȓ~\x99ɱѨ҈ɜԔԨҿҀеϱԂтȆͽȌϣƩϖӀȱ',
                            'arguments': [
                                        {
                                                        'name': 'ǵӐԂԭƦ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʜƜǋåíɫľŤԨ˥.αξő{Ɠʫɯ϶ҴſӾWȆ\x8dȸԪΩȃǯ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΑƿЏũѭǷӷŔҝűϺʺѣяϋԁƃʺŞԝϷΝϮӍ&gǥěϩǡ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172751.507582:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'øӻķĈҿȫ,ΜŔǠϱfκЭ˞3ȏҽ4˸ŕ˕nĜ0Ӵğ»?ς',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220522:172751.542144:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԈǒǺȣҁȠȹ9ìџӄͲŝɴ\x8cѦ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŨɣǬŇ˖ӣƃϗ\x98ӥɄ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϥдˈ\u03a2фɚˢϸȉ\x8aɀNÎʂӤ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǆϴɋ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 345822.99427325703,
                                                                        },
                                                    },
                                        {
                                                        'name': 'čɩКWɽȔЪ\x84˾ϿӪ\x93ŀɣцѹ\x82Мɷ˶Оҁη§',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 580052.1650777949,
                                                                        },
                                                    },
                                        {
                                                        'name': "ҤȍʽҀʻʏьқƁ˾ʱӇȼŻ£%єʂȾƲɑ;Īҵʗť'",
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ґ˺Ƌͺʜ҇²Чƅ',
                                                        'value': {
                                                                            '^': 'int_list',
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

            'name': 'ęͷ\x80',

            'error': {
                'identifier': 'ĭ˅˸Ⱦ$',
                'categories': [
                    'configuration',
                ],
                'messages': [
                    {
                            'catalog': 'ϿҲ',
                            'message': 'ʓ',
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
            'event_id': 'nQˎAώŰȬҢѰfŃƏԉľǕǐˎɂДŜȢƲƤq0ѫȪƇʺԦ',
            'target_id': 'ǋ¸¾ϏOǩәÍɨ\x80əƸѷǴ\x93ɶʷѫPʍЊƲϛɖʖŨˁɦԢԡ',
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
                    'event_id': 'ΧÂӪʏёҾϽü\x84ŨŰȒaӕƮ˜ŕ´HŀĈЇ@Ўʤ$ǫВГș',
                    'target_id': 'МҼѪɐʐхѭ[ǰ\u0383ʔʜ&ЋԃΈŴУҝΫϱϫ°Žєtëыů¦',
                },
                {
                    'event_id': "ѻğƊѹɶ~ϖЁ˺'lˡōƀʅ\x9eƄĦǽ҆¥¾ƬӶѧҮǵIӷе",
                    'target_id': 'ϫЩ&ѻʡUȿϹÅӮhѓ˻ԬɩԂӢӫΡŤėЖȈҙɒ¼ϣÛŷǗ',
                },
                {
                    'event_id': 'ԬѯUǟõұȮȖІàʍҹɝΏĂʝ˱ϻґқΡηÕȠÍӫχӯȨȬ',
                    'target_id': '£ǀЖȁxʺ˟σĻўʬȼƆѫʔҰξѧƦǝœԢĵĉaςʓŵ\x8cТ',
                },
                {
                    'event_id': 'ҕȐķīϑӴҭťҿ˯ʮԂЬЪȲЉɟēǑǬɤмū¹ЈԞƔťϱԓ',
                    'target_id': 'ЙҤѤɔýЖ\xa0ԗѩǉϢŏΜİͿ˅ʶÜȇȯӲɫ˘Јˤ\x99ŭĩԌƸ',
                },
                {
                    'event_id': 'Ɍ%nΕĉŌɬǗƏХќ\xa0˧\x8aңθӱƑÆĊč˷ÂѲʁ\x97о¦\x95ϙ',
                    'target_id': 'řVӡȀȍŹΨćНїǠ˼ʹʖїԌŹљă˓ɤʋǩѨԈӓӼuŘɍ',
                },
                {
                    'event_id': '6ˍǀӜĽaѣĠҟЗ҆ŁқϨӣӐțϻΦр\x8fҫk±qҧѭǡņð',
                    'target_id': 'ȥǣңЛǋ҂ӞÁ0лΝɚƪÎΣÐêǐӱɭ˅Ҫű˶ВşhɦŊӀ',
                },
                {
                    'event_id': 'ȚʍҊĭņȕ\x8bˊɤ;ƹʗϩԫІżǬϱƍȴ¸Ȃ˳ʅYœiƨ÷µ',
                    'target_id': 'УΞԩɈȰǃȘϛǛ˕ΩɬŏĩȽˠ7ɼжuӮʍɀԃȫǵǳȮȐɖ',
                },
                {
                    'event_id': 'ҞϐϿωãˈԢ˯ũԟÓЭƜ˾ªź˶ѧ\x82ӻϛ˚˥ƙɃ\x97ʅ˾Ů˰',
                    'target_id': 'ɄӼϒɔЊκєÂҦԌԖ·aѠҳÛʘ\x8dԨώΑ˟5ӜЫі\u0379ѪEЌ',
                },
                {
                    'event_id': 'ŞҐЏ×ȗĔ\x9cѫoɫõЧϭͱџнԣŰјҸƜɰɼ˒ʬāzƑƓǗ',
                    'target_id': 'ͲԑƵ>ʕԛц˘ĽǀϛɔĢҥQĩŝӧsǾǷʬÅkͿǸƒϲˏԆ',
                },
                {
                    'event_id': 'ө»ɇԩɥԌHȲҏȝʼҸǕ7ɔ˄ɽ;ԣ˱śȾ\x87ǜħҏҙáŻΚ',
                    'target_id': 'Ϊΰ¦ȴĻʋδmWӉƷʤԑԑЇѪŧƃbĉɤϥȪʄҗʤGȞÕŷ',
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
                    'event_id': 'ΰ\x87иϦǍŁљϪ\x97η҇ʰ!ɹԖϡʓ`ǒҦǇGĎɭʚқϜøЉȗ',
                    'target_id': 'CǺƎҟԒα0϶ǍȖǵѶųΤӘȉÞơѵѺQǐïΕЍƮǣεȐя',
                },
                {
                    'event_id': 'ӒԌʓӡϿ\x81ЧΦʈѫK&ӗӣĸϦϧ΄ͰaӈƆȀţѺŮǚ\x92\x85ϙ',
                    'target_id': 'ѺʣԦyʘɶŝ{ӗѼλұ)ä£ӨЙφ˴ÕƍҌʺʞ\x91кα҅Зʌ',
                },
                {
                    'event_id': 'ӴнΪƉɷʬÇıĝӷ\x8eƿǚҙԝΆЁԛƎϘʋ˓1ѐ\\đšΥАЈ',
                    'target_id': 'ҡɴԙϦЀʔˡǶǠ˶ɖϷş˕ɕ:ƥȳcǀŤц˃ýҺ´пЩʊ¹',
                },
                {
                    'event_id': 'ϷʝƐѴǎƌΕЫ˃φ\x8c«ӒԎ*ѪçĬσӋкǡǁɰӌЌĚĳԙԠ',
                    'target_id': 'ťК:ӘǶúοϙŦQȠԃҹқŰҁʠƬȮąŉҳɽʐͶ˺ŅǝĠx',
                },
                {
                    'event_id': 'ǜДӰĸǣʜ¼ɰȘ;σƩʥ8\x98зîˤǄɞĐυÑҨ~ȵǴϖƇ>',
                    'target_id': '˜ä\x87ǚÏΤӢÃЄɩɀƝԖľơЋЧӋǠϳϔЂȠąŏƝѓқƧƒ',
                },
                {
                    'event_id': 'фÄΫȒǜԚZƞԜǶЕzћȸÖʁЮţӠŪƶʘҘԜÙƊςƝʹӖ',
                    'target_id': 'ӯņ8¸cĦҧ½n¾ԢψĉʉӊɩѷλԑşΉŦϵŒыŕҝ¤ɬȟ',
                },
                {
                    'event_id': 'ǣšƲԇˡҳȞįҡȎ\u038dӭœԝѵɞÌLǀШш"\xa0ˠ\x9bѮ¿ǪȎӇ',
                    'target_id': '`ΕȺӛɖɖρʹ˙ΗȻƥëǗwӁѦÕk©àҎΰΙĩčƕůɈΏ',
                },
                {
                    'event_id': 'ϦȴҐʹŗ>ƴȏ΄ҠѿЫѦˤҨыӽЕȀéїɵщȪўȵ"ʵnИ',
                    'target_id': 'ȐċȔӤÃИřkƵ΅ҼˍOëíʺ\x87қЈжǧѿЇ˨ƌɴŹĤʄɣ',
                },
                {
                    'event_id': 'ɨӿɌά\x8dɤӝω҃{ƿӯɌνȇŠɊ\xa0ѹүҼϽƾŋ5˦Ԓϴ6ɑ',
                    'target_id': "ɄɪȊѕ˃ʼϔöŴƎʷĠ}ʈɡӱįɘ'åŦ˅ÿкƇϚ\x92Ԧǣ˕",
                },
                {
                    'event_id': 'ÜŢϯѾͷòψӑĺȚӍѣɡϡΌĎπşβ˚QЯҔƃӳȳҋʱʨƛ',
                    'target_id': 'ҲS4ʌԣДÄřӺПŀӦƪìÞRˋѿʾ±©Łɏӂ˭',
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
