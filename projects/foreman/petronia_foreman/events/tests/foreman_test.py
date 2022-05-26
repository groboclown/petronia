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
                'ҔȞ>\\ҍħ˴Г\x86ǇƮ˭ƨϞåƈ\x9cҘɻŦȈÓғ\u038bɰʗʺӴʲŅ',
                "ԏ˨ǼɫϖƢAʏί˓eǗϪʖǡαŖʔˇɊ϶ŉHĚ'ъƄѫоf",
                'ЙėØӆѫԛϪԫӭŠʆ\x99Λ4ξЫěδɪŏ˙˳ȇ҉ȣȒŕłʓғ',
                'ĦƔž˶ĕ·ĦVˤȿӻ\x9bČ}kԆӚϚwü¹ưſűȬˢ\x8fŗÝӈ',
                'ϚŤˢЌԈǳϏĳΖϿǏͶîϛŠʃȲЂИ˦ԛɩɮΠĺӰǂԆǻŶ',
                'żɟьɥҡʴ\x7fԒԛԥҁɧшʈ˝ĘȻȥ˺ԏɗʐЍ¨ɞЂ×ҴҒӷ',
                '\x8fɾêӖѸʕ²Ǫϲ`ϴȅӾĢĶԔԆţџĹʲQȄùӉȪҙҽщ˒',
                'ƴ¶őԌĎΖzμӒ9ѾӆmЦȍŴđã&ѿ\x9cɝЯ˛ǵƵ΄ʞʖХ',
                'ŅԇҵȋԇƦԍӣİόԢŞþһɘȡΘԮȡаĠˣԜѡӟɌжўЂύ',
                'ɓęˁƞž=ɛŧPȠӈ5ԄΕƪĢèӘуϭáΊ\x9dӢΈѤ˞\x8eср',
            ],
            'source_id_prefixes': [
                'ϟʩȌԐϢņêůΝѡĻˍЌŔ˘ËɘɕȲҒ҅ϬЩÄЈÌԄϟƶƞ',
                'κӄɅǢŨΌWҔśǃPөҺӵ°ң˚Ӷǁɳào\x9aÁ˓ќȝĭƍǗ',
                'ªǮɠМǞ¡δЋmȓқӳŔҏďūѼхԖĀ|\u0378хчѽɧ˸ƧȌѲ',
                'ʤǈԛҖȊʥҀɿĤO¥ʽӵʲıŖ҉ǅѪƦόȬĞɍ=џǹƨГӞ',
                'ÊԊɐʤҩçņdēκ|ǤaͺĄƤʀӆς\u0382ξԘȣčϽɅǋʉƳǢ',
                'ǕċǜʐɑӐʠ˥˖§ŕΚɭƔԚӚwτє˙þɠǙȃƞӄ°ĪqǸ',
                'ЗJӀӃŇ\u038dѣıʝHřѱŀҔÐҴIƵŔЎϪȝΫǛΡԞšģѷȧ',
                'ʄºʪԌŷČͳӸʂȏήpлȘɹǥÝСӜǙ˶ϮʀϬĺЈȪʦôŠ',
                'ЎƑûkʦΧˀΉшÃϺ¦ȭѲϖˮԣƳÈƀĿӈӱzƉӦË;ЂȒ',
                'ˎʩеĔ҂Ū˶ď\x83ѻїӀ~ϠŠÈϡĶǂS\x92уʻęϧҼθҳΜШ',
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
            'action': 'қʵϋýĐұёʫȳ\x86МИʣјȵΎφǂƝͰ[cԪӤ^Ǟ¨ԤԒû',
            'resources': [
                'ђѼ˾zªͰʶ,ӘĹˏɿƱªɶEƧĩĮÏΏɜĦΈňvŏɐɘÈ',
                'HδĒƯʬҩʎɖ£ſҟɚ7ÝĀʏӡʎӧ',
                'ɋƐзʂӺ·˾µɩ²ӞӺΰ;áQƓčĤ[ĬėѡӋάɜÛõ"ԋ',
                'ǚζ\x9fˋǺBвŉҮʿıˁș%ȹϔӟгѿ˷ʮԠ/ƆɫΓԥī¾ұ',
                'ѰȻϚәԞӻˌ˥ʄӡЖȲŘŘƮȎʿϓɂҟ¼ԄРӁԖŅӞRǲŷ',
                'ʚҡǒʺŇʽÜӨ\x82ˆǈχɀɟţϤãϺôΠǥ˝ӴŪ¶ΕɛUȲԁ',
                'ʓʠʄȩԠ×Ψ˚ŗϯМ\x89Ѧӷѳ¦ŉѷÒäɡȷьҏŁӑӁϚԊơ',
                'ĒʭɍɺӘϸʦƆμͷӐԆîĈҺsчĶǷãğЂεæʗQŗʀϞӨ',
                'ēŢӚԥüȋɜ˾ʴИĻşҰƹŲZԈϴЊțɚЧƊ͵\x83ƻԏґ˗˔',
                '×ǗŃɴ}"ΰЇcѢĬӱˠСɋӷˮʢҩ\x85ΈӈјǈǑǐȺ\x83ĺ-',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'Ř',

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
            'name': '§Ķǅ\xadҭԒɚɶȅԠЧǡɄʝǮƽǽŲʹЈɪѫˋβʅâɰȶӞʴ',
            'version': [
                -3285612627565117991,
                -8682775298149533820,
                -7097536949807449711,
            ],
            'location': [
                'ƐƧһ¤ʦюħǏșǚȩˊŎМĖ®ȌøԚ˵\x80sϮМүŉˋʔ#ƕ',
                'ő,ʢх˗˺ǲуTВѓȳťԞʮ)όЇКƠӋ©ơϮ˾ҙ¬ĭ҅ζ',
                'Ƒ҆ͶԣөҎƏүЎșƶ˸ԋѮΧҲ5һйȲ˗AԭmҸʹҔĉÙɧ',
                '[=ЊǙȡӡԮƞЂӪӎȵˏ\x92ͷǑƳcřēǁъǢȌY҃ïҝӗҥ',
                "Ӕϧ\x9fďΫӱǡπǈɉЯɺĆȿĽѰˢΘúƔЂƽö'³ѴԣŶӢ\x8c",
                '˥қšοÉҜ2ϗθӋɖɘÛơ˙ˍԨ\\\x96ɷˡǔbɐˡ\u0378ˆåƵȳ',
                'ɪˍ\x87XԈ˯ɀčŃ±ͼоȓΔ&ԏǮɋˬўӖdʓÍГƜϰŰһИ',
                'øȓЁЇеx\u0381НſǶзPŉҭɿȻҴξϐɀΑ§ÏԝɨѪéƐĥǠ',
                'ĎǝʢĈ(ƓƉʊ\x92ʃƬԐŉĠ\x9btȂ\x92гӽѝҜҾ£ʥǡЂξХл',
                'ŝð«ӐҵӸϻϞԃԀŃϮЙаǼŵ҇Zс\x91ƗȶGǄ!dűӛͿї',
            ],
            'runtime': 'ϑêʛȻϠűԠāėǱһ˺åĮԏҙӱ¬ɹbƫþгԙ(ù҅ȉQĺ',
            'send_access': {
                'event_ids': [
                    ' ¼Ҕ˄ӌɟ˕)Iёӄ\x80ΆҡÈĄ˯ɵĨõ\u0380ϱˠ\x88Ɖ˟ɬůϜЦ',
                    '\u0379®ŷӾѨѱЊΞӬź˥ξǐƿȹƬΥƙ\x90ɰ˼ƛУȻέǙIȫɪϢ',
                    'ͽӽȘ\u0383ºƋɦʒҡτ%ƋƤǇǺƹƮǧʀϪýǹŁуÕǮ3ΰƪӒ',
                    'шЙЄ\x9føϠʔǡȄϐǋЋEĖĂһ˜Ӂϡƿ1ȆjӦǽɗµ\x91ΎN',
                    'ȉèε²їʎҮȩӛѲ\x90ϕßƪÿɰӊŪčΌЉʫƔ¢bтʠηZʵ',
                    '˂]ǁƴԧÙͺӕɅƥЖ!ǎŒ$\x89ǙÆ˼ˇАưӬЗƓïãƆнҳ',
                    '˹Əˣȅ҈ӱˎ\x7fϰɱЁǢҿɶт²ÂɄˡȍʵÉɋԙ˛ńΡ˗ɫ˸',
                    'Ʉǀɺ£ԣЀ\x8cЌŤϙãӭԤɦƑεȸăԚ҉AкδƬΊDцѧКа',
                    'ŬMԃĸӣęйĚģŕȳлȟɠѡтŨrͱÚƊҸɽԐXԒĔФFº',
                    'ǴӫǄɸtǐιӒȃĥЋ҉_ƯϤɾiÊΐϏ˵Ѵņ_óŃơ\x8bЏϿ',
                ],
                'source_id_prefixes': [
                    'ӆǵ˪¥ɎÂ»ԥˡÎȼǥȕxƊˈѴˠҒ˧ҁʊψΎǙȎƞǁϺɮ',
                    'ŷɧLóĜ˻ʧǢрšƤʁɮɟlҀԪ҂ҝȔƏǃǷҨԂȷʪϴԣӝ',
                    'ϒ҇ˀ˲ȆκӽґҝӘǱêЮűѬɠϒdğĎЕ#e¢ȼ҅ȅÐǁ˽',
                    'ƗĲζ҂ύҘӈƀӱҎèЫûǋāӤȦϧԊʭ¸ѲϸϕΫ^ŦƐϙɜ',
                    '҉ǟ˂ώȩγǓÚϩ˥ЫŐЌˬʚƂƈȬͷёAĦʛ¥ʧB2ѠƭҾ',
                    '\u0383YĒƕŋЯȈY҂ѪR8öӜ˓·ǧǜIӗӪ˻е0ƫʒ\x98ƃ¯ԙ',
                    'ǯɛɜԉҵǯʟɡǥʦϞńɄԬ҈ȰûɉlϠıˏοѰіɓιԈʧ\x87',
                    'ŅŁï҄Ï¶óŇԉ҈˻UþǅƤʅþ˺ϻĚŊУʫҌΆȓпʐĽП',
                    'ÚǶԊŻõԃȽƀŕɣìҽŒхҩ\xa0ʲ˭ϗѾΆҔǼ˯ӂԥτϧ0Ѝ',
                    'ŋÜЂЯѦзҥŪӝθΪκªǘԥ\x8fԧɖԩǋӀ˓ǋNϿΔВԝƈÀ',
                ],
            },
            'configuration': 'ѕƃŔʩŜƇ˟ŭҤЕHЪŧѱèAʿƯОĪǛΟˋəʰҬ\x9dӬȁŶ',
            'permissions': [
                {
                    'action': 'ǐsΛӿǬϳɕ£ːÈɳ\xadƨ˧ӝΦ×òÄ\x85ϺъԝΑį˨\x99\x88ɓ͵',
                    'resources': [
                            "ѣаҹ¥ӴƮLłҠÏLšԢ·αӫОϺɄӕʲиӎA'ȃ\u0380Đԍ˞",
                            'îǳѨǢӧωǩĠLɽрьӚ',
                            'ԇƒîµǮKɁȷʵӯύϥяԁɁ˜Ìҩ=ːΠӐçȐνʭɑ˳Іɔ',
                            'ƌȇϐȧʰpʍӳŶ_Ȫʝдϭ˛ØΥόLʀƽƔΏİůǠėІ«ʐ',
                            'ŵƇ˦ĕƁƜ\x91ŸлįʹςιąȮ=ɃϳÔѪμīжQѱЭ&ρɯǹ',
                            "D˭ҳå˻ΣǺԭŌƐӐ9'ӘȮΠԎĳԅíƢΥҏ͵1Ϗưʠ˕\xa0",
                            '£ƺˠφȻШŵӹӦ˹ȈõTɆɌΨӎҎAƛ˖ʥÿŜƈrԤкŹҴ',
                            'ǊȬȺτʼƭQХʎĐ˂ƘæȥƗˤň\x8dϹīАѹFΰǎԀΟЦìћ',
                            'ÀȐҜцę¥ӴŔɣŤ\x9dʏ҄ϷȫʱћѢŬѝˢҡÞɠÍШɷºɌÕ',
                            'ŁǽƯɤȎʒЩͲϘҧɯҴӐѬɻ҈βфř˖ҌĢ',
                        ],
                },
                {
                    'action': 'ќϡFΌȽËɅζ_ηŏ',
                    'resources': [
                            'OΙϚˮːÈǛҐŝťӟϭÁ°ƭζɖòĎѬ˻ǓƦɨǋӯŹŋ®ǒ',
                            'ƹêӅϖ÷ȁʲԗ҃ʗĄźЧĮӉʧǮҩɊʕʩɉ\u03a2ƺĢЕȑ˩Ҥˁ',
                            'ȂǐѢЍҶƠȴɐ^Ԓ˹ˉ!ҁӫϓ҂ьʺƜľΫʅԗÆŇѓ˂ԞΌ',
                            'Д\x92BΰǘϷǚɶΎԠК3ϭǤҬѵԈ˸϶°\u0381ĚȆ|ɒɣȾ\x91ѻ\x85',
                            'ҴԂНĜŏѫ˂ŻʣĕѲҗнżvOǼƩ§Ăȵ,ӟϖ½\x90Ѯ\x9fˆǟ',
                            'ҘΚƫЋˋДT˜ѺĦДɯѡEǄӬ©ПȊ˨НǚŚĞˁӳ˽¯Θǥ',
                            'ћԤǠӚѩ\x8f»ǰǚѝˎɟŪуt\u0382\u0379¬ĵ\x9eÂ\x9e\x9eĂŨəĘЫϹт',
                            'ȲĂɫţњƓҫiǻůеЅǱċ˷ƔϠјɔҸȽYѸƱ\x80҃һѮ\\Ʋ',
                            'wЀͷȮȑŞēΨɬγʪĹͷƵҥѓǶÓùɶūԞψИ˕ˁ~ͷзМ',
                            'ƛȚʋSфR\x9aҶeˋɛYȹĢПˤÂ"ɆȮԘԐțʀÕˤӒÚуɫ',
                        ],
                },
                {
                    'action': 'ˀӇnҫ˒ǡ·úɵԛЧťћɦvͱĥú\xadƯɎĆԃƖʸφɇBЎá',
                    'resources': [
                            'ʮύЈǺҚȵϩ˪ůȇΣĹҼС˵ʧSӖƧԪwɩәĪ˒ũɮКǺɾ',
                            'ƭҭǒ¶ӡөЂƵśĩώƕҼɶƲӲŷӀʹ˸˰іʄπȈʖ¥Ҟɮ˩',
                            '˧űɕëʉJĬėϔɺҴБēũƘМĪvɳ\x90åʶȵþNȕˮӬԒê',
                            'ȩАϧгəĐΉҨƗȾӈьáƙȕȣǩiǆIΨҒşȵУӝӼԧȷу',
                            'ӕƐ\xa0ДĝѪҼγμŏʀӍҖɔĹɻɨӬøŦϬƂȭȤϩĩ҈ϑȕЯ',
                            '*lҔʴѓаӘ\u0381ǜÈÊжȈȜψǋɮâüsЩͿnͲͻώǮ\u0382ӽȕ',
                            'ЁшΕӛcƩΔΖđȖ\x83Х°НɳҼҁΖųΎƓΰ*ɸџҥӑɠʫ<',
                            'ԕХКьЃΏѷÿĿ˯ɵ\x9dMȓ\x9eϊäǲ\x9dϧԮ\u0382Țѫ\xa0еºЙÛҎ',
                            'ƛʨźұƨɢʼͻŧƖȫуśӖԘӨğƟɋӳŭDӃÚżʾ˩ķ˂ϧ',
                            'Ƀχ¬ϨĶʤÂԠʅõ˚ȃˊɾҞӟǦːʬÕ\x99ĭѼǌÍϠϔͲǵ\x9d',
                        ],
                },
                {
                    'action': '\x8cȃϷќĝȿ£АӁњ¶ŮΟȏǦΚӲv;ΔƝψŃpĕNѮ{ϡǏ',
                    'resources': [
                            'ƈ˯Ųϯҥ˭kΉƟǩʊƦHм\\ŅƥɪɖŮĢţ\x95³˝ÁΖǷҽӲ',
                            'ʴҭқӻ˻ƋƿÆǨҬżøɔʵģΙ\x82\x95Ǻ3Ţπʘ˂Ĳþ!ɉǭθ',
                            'ǲйЖʨŐÑԋԃΑп-[ԇԥɸҲº{\u038dӳϥ¾ƪԢz˒ƚЌŲ˥',
                            'Ƣºɶϥ´ҬͰɂˁȾԎŤΔ·КѭƏȿƏɻіâЕĿϼĪțҀ˟Ŷ',
                            'ԢžшԀϖԌϪƩԓ\x86Ƭ¦ʿʆ[ŅɅóԐ$ҢįϋĳϏ˾ȨËӥ¤',
                            'ѰʇǃӮǊǺƞϞжРźƀԒɻǀӖӼρƌӰęΑЖҏϐѲШӗγӪ',
                            'EWƲ#ƉpϪȧћuxҔ|ʶěύӢϤ,ǓŴӭŕǢӴȢƄ\x92ҋɗ',
                            '¼ˍʜĮНHhɴӫī˘ŪȗtƹBǉԝҋȌҜΎѼĬѝԋ˸Ʊp\x83',
                            'ӶДƢŞūіԦɝÓʒĲ\x8bɥËȫʖɱ˖Ѣĩԗѣ\x92Uɲμϻġʓ\x7f',
                            'ƄƉŌʈ¦ҮԌ\xadŀԛˇÜƌƗ˦ʇƱǅ¸ȱǖˁYéӯ¯=ȬŦҨ',
                        ],
                },
                {
                    'action': 'ԪǸʣлѿ9ӞˁſљАͱlԨӡ¯īʃºήƇɌԤƉΑЩêØθϤ',
                    'resources': [
                            'ԠǋzӋ҅ɭ\x93ѝȐʫ˘ŽЏҲѰҴѦҷЀΘͲɈһūǋɈһǐɳƂ',
                            'ǀИWӛɥԆ[ɪʛˈɽΨҡǵˎĂǓŋдǪΗѨЫ˘ќȑŔ҆ҳʊ',
                            'љ\x98ԕ\u0378q˲¦YǯŹɿʟ҅ʧɹʶŕ˲ǲǽȵËεҌėѺӦҎ˗ʁ',
                            'ǅ˴ƶʪȊїµѡ¢ʣƙɝ¿ϦѤ\u0378ИȦƟÁɌÂҟJэʖʱźɜΨ',
                            'χ˺ƯϹˀǑΛ²ыɬӘʅǕҕŞģıˌЧ΄ɝԆëǧķʪƻΠϱȻ',
                            'ϭұӶ˼ӹŐɽźgƷǗ\u0381;ӐҞäʂӳӊӒ×ǩɄԕъѽƕøϽɟ',
                            'ĂЕPƗмƘΰÈϟӭˊƤÓÒkΎӃ˶ͺĒʜӺƭѨʞԭǊeӽŴ',
                            'ƍΉĐҚɂϟ·ˢG;ĳˍɄȕʿċΗǔϦԕȉѳĻôϜѪб˛ӑɁ',
                            'ϏȦÈʛϔŝʽıǐ7ɼȈӛɷƉΩďɇʎȸԒŭʿͲ;ǬȿΊлж',
                            'ƊʰůɈ9Ȁ¸ЍʡӏǢǒ{ɑûƦnҝƈɎӞȽȻХĝѕ˝ŰҼɦ',
                        ],
                },
                {
                    'action': 'ǀӈЁĨ˹ǶәӤvˈ$ȚӁǝΝҪӅŲԈɒʚҪҷ×ιȺȖ¾ҝЀ',
                    'resources': [
                            'ȵӣȨбŏļÑιŐ˲¯ӜЦшÌπºþ҆ɘҌӑůϡΪӈgǻ\x95Ї',
                            'Ф˖ʷӡ$ëȨɝƱ§ίϴԝ*\x87Ǡ¶ģҎʛÇʟ˦Н\x8cӁǵӯǬȱ',
                            'ŎɱχΝϲÂѐЬΖ˨ř£$ȲкʇȳȖǂ¯D\x95ŭѕϧ͵ѧĆÒ¬',
                            'ÐʎƄњϰκҭÈʏӚİӬSƅЂѾ%ǷрīK\u038d\x81ϤȌľʋʫѻҽ',
                            'mʷŭǉѽӬͺ˨ƫɽԭТyЫˬȼԈÛҤѮЫǓȞʪԪmǕЇ&Ұ',
                            'ϲĈ\x9eŎłӆƘԋѫɷȐùʨœōňÈɛȓĨ¦Ȍҵĵɑm\u0381˜ʩl',
                            'ͳԊĺҿ8лǛ\x9bӛˀȽȶиʙ˚¶йźҲúʧÉϧĄľԘλЋ˖ϰ',
                            'ʰϦɌŋƜМǨǑεȬǃЅԠөΙǛɺ˙īҜ˛ӁȈ¦Ғ¥ūԌÔŮ',
                            'ώϵϮįҊȤȷӥȭґάȥϧщɎˇȖϊkҤɄϫҮùҀϊШǝÌł',
                            'ÐϨѠXŭѺÖΑƋгˎěӸіТʅÊɄʧОЙͻƊҝǑ\x88łќŀǾ',
                        ],
                },
                {
                    'action': 'ğм˟Ҽ&ӡԎҟȷθҐ÷ԑ˞ǆ˜\u038b½ĸơʍƻĮǣǚœруǥϧ',
                    'resources': [
                            'τǕнӹϿîΌӕɋNɈϗřʵϾγźӘԏʭήѺīɤΏϐĭȞˬā',
                            'Ȋ˨ϸþȦͰ§˟ԂҼԭ˯ÑȻȢзΖRâΖӴȠξ˧ͻͲі Ҋт',
                            'ǂ\u038dǜ˰9ǷӋԬȎªŦ\x9e^ԂʮȱȾʳşư\x9dŷλԞ\x90ͶȂ4қƐ',
                            '©ІӚȒӅ\x9dIÐϦ\u0382ɣ˖ǀU¶ΙȚɝЂˡˬ£ԐӔΓҟ\x85Ѽѐʭ',
                            'nðʓÕŘʥyŌ҇ĩÕƨņфǵӮɂɧɎҕǄǵɋ±&ĭɞν»У',
                            'ԚȾԦыΫMʛƒαɅϒȬðʊɸƱˍ\x98ŸѵgԗӖY\x9c˝mɊԤ͵',
                            'όρȸԁͲƌĜϻɸÀұ˼˞ʲс)Μ%ɰԬʳ\x9cӗԈ_ѓɱȰуĈ',
                            'ùƘƯӳҁǢψåҴŃ¸\x84ӮϝеKҡɧťөʴǤӴУε¿ӉӾ2ӯ',
                            'ɝƭ˻ŐӚǛҭųҠǲ-lːÀ®gȺǻο҈ɋҴεԁʳҕ\xad|ӟ\x86',
                            ' ƥЇȿ˻ǯɗ˨Вη\x99\u0381ȈДiͷԒҍҞŔɄɨę\x86ҰȄԗčȜĪ',
                        ],
                },
                {
                    'action': 'ƫŢӊɬƧΊњNҩҢɆԐԒҿơ¸ʮǽҝNɫŲŎʓΜ˯³Ŗ˻ñ',
                    'resources': [
                            'ӀbҜǝɛмȲ\u0380Ϧ(ĭӌµͶӈƐӻͼϰϋПѩϞиvʝ{ʻ҂Җ',
                            '\u0381İǔ˹ʭ|҈aѮɳȔƔʝƤͶɱӆKǉ[\u0381ɞҴяeèҖ͵ă=',
                            'ǇӈӪȻ×ӶɵԎ`¢ǶǦýӉϮǫҼёŻ˪ɠ_ԟӒ\x84Ӊ\x7fɒ|ʹ',
                            'ˮîȞ7źԋЩŁѢəŎ¹\x89Ƨ˷.Āҿƙoî\xadϑғɼϭϨҙ\x80Ǎ',
                            'Ĺ´șϑΝȫǯıӊǻ\x99Ɖ˘gvѡҟФ˱ʷȻеǲʜj\x9cһÿ\xa0ɦ',
                            'kԃӇǖŕϮȋùƭӼйǜƾɭЇʣņϿϒҦ\x89вɚĩþνȫŋƼҷ',
                            '\x90ѲΰӒ҃ŔɮšŌȞԌԤїϲɀ8ԔӍŤȠ\u038bњԤǹɭјϙæέų',
                            'ɄşÇÕ˺ǜɌþƒ˖ΖĖĈŕIмŰçқȴϒʾΛԎϦşʝӕ˄ԇ',
                            'ʔү\x9fҺ)Ğ\x94\x83ȏTξȉаԞȅУѽѾџіˊӱɃ\x81ŨΥѼѥʄƾ',
                            'ŪӥɸөƔˀ\x9f\x84ɣԉɥʛӀвάȕз΄ҁԔϹmқŷѫ¿ϲ÷¬ʬ',
                        ],
                },
                {
                    'action': 'ҙ˰˥£ǽӰтƪŷ;Эȁ\x9bԞƈ²\x8dϏМɩɌԂƫɻÙġŸѲʂʵ',
                    'resources': [
                            'ĝúƮȅűȯàΜ˦Ǆîħ¡ӿ×´ђˍԬԒɷɾaԁԣӾϚΧ<Ž',
                            '\x9fŅķЎёˮŭ',
                            'ˢƤɲȿҫ',
                            'Ī\x8fǜҢ҅âƅӱҧћȡĜҾʍ˜śдΌűȌĲВ˫Β\u038dςλԔŇŭ',
                            '\u038bЉӖ=ӋǇǆɠѹɰӶÝ¹χӞƷʱЙΝȾǶ§ǹôʤȞǯķԉƴ',
                            'ı˗ͲСǔɰ÷ʷȐ\u038dЄ°ŞϢɧle^ɂҝN\x80ИԔĶѪ±ʕ϶Ǘ',
                            'ÿҚʣƕԔηȸÀĚϔȒɐŉΧĈǝ˱.ҿĮɆˏ<ƤϖϯМ&ƞˊ',
                            'ƆѤƄƭ\x81ӘɧőȐʱӦÈԌÈӉǕѓuɐЙϔŅƔȑʵțͻϘ¢϶',
                            'AцfԢЪƖǑċϠj҂Ưҹ0ǊжȢ˸\x946\x8fѷӴЪ>ƳԀɦ\u038dϧ',
                            'ʋΈƘUөāЍŕԉÎдĻλ[đŝ҆Ѱǅԡ\x88Ѕ\x94ЉÐэ¤ԑ5ƪ',
                        ],
                },
                {
                    'action': 'ΥdŘΎΜ7ǯõ\x88Wʫč˙@ӥҸɓîǢӅ§Ĺ\x91ΙѧұԩσŢǀ',
                    'resources': [
                            'ǯʗӑɿБӝ˷ƭɯǄɢή´ȹɿΓň˫ǃÑɨΫӺƉª\x9dƴȸȿ˾',
                            'ԣϨĶ˗ҳFɺћÌĒԥӿҹΈСʗЁƺКJȔÇ¥˽ƍкƹǘ©U',
                            'țƊRʇԒЬĪǡϑіȟĀǼӴ²˳Ǡ˔ ДӨʫҺ¼ԄnӖҽЪɽ',
                            'Ęҗ\x7fƃоxʽΚԬʬӭҁ¡҄ʽʹ˹ÊôcÜɮȬFōԂ˽ЈѕĞ',
                            'LˆǨȨŖǝП×ʱAɎʨĊĆc˨ʩ˞ψң*ϔ˔ǾΙμˁЃ˕ǿ',
                            'ΕǞͺӔҠŸϻư\x90ΙуěǢőþ˕Ӭʵαĺ˵ԣĵҶїΫкƥԗŷ',
                            'ӂˮҝţα´ʁ©ӶăєεѯŇԤ)\u0379ǈҀʨԏԩõȁĲӿźťTǿ',
                            'ϽЏԕůѬcʔąαȹ˷ǰRҺέÉĥӳƬÄňɗĐѸŦѽˢƳΥ˯',
                            'ʌɶȿ¶SҿɾɶԖɨȨŲˏԉǥѝԞǧАҲӣƥaдdѕĽ\x8dȯȸ',
                            '[рѭʎŌʀȹϔѤВΥ¹Ǔɣt>į˂ϱЦ´ƁԦİĎɰȚþĹʘ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʎ˼ž',

            'version': [
                -8050263575071144100,
                -1248186724659655392,
                -3181577397981727214,
            ],

            'location': [
                'l',
            ],

            'runtime': 'Ӈ',

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
            'name': 'ȪЬƭȢϣȉĖǻïĦ҃ϖӉс·\x9dήʿĵ˪˫/õčπƃΪǷƺĶ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ǭ˛)',

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
            '$': 'ɎeǇŃЌѶHҤ˯üĴĉӧΚχΨaΪƘȖȧœȌѩŃҎҋR\x95Ʒ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 4525669257462138422,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 254688.1387986199,
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
            '$': '20220526:210902.222130:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ǆE¹ǚͲʖƖȏ\u03a2˭ȨǬϐɒƉÑZңħ½ǀɄ¸\x88ǠUTƾҚϴ',
                'ń\x89ǐІʸѢĆӆҪ\x85iƝΗȼʃǧӔϊ°ɴˤɻʊ˟ŔηʐξΦȪ',
                '2źǽǖԣ˓ĻκяǯǝʈЦоԥɶ«ηȖǷҮоԈεǣŐʺéǼД',
                'ťÓ_ˉǏҨ÷ǎвǏЕӿńф$ÿàҟąɒϺ˴аУɋАɝ´\x83\u038b',
                'ӂƿŵϤѱыљĉˠӐǄɌÉGƹŮғǛʠν˅ԘÉ\x8aȽȬʤМƛũ',
                'ȟ\x8eʇɌñϿΒǋʈƓɔ\x99СĖǑӏˇăѥʣʏµΏәġ²ǓƝɖȗ',
                '\x84βΣȴÄӐԗӎҵÌʐԘŝтЫŢĂAН»ӞΦ\x96ĘЦĞʋͿˬ҆',
                'ѻʑ"ξҳǽХrȿΤ¶ȓ§DBĬеӕ˚ċ<ǠͼķгҼƨυɯů',
                'ϪŻӑʊ˵ÝŸԮƷКȪǇџȶǴϠƵȽЮȑęτҴ˦ŨόșãϠӹ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -1557971764913336161,
                9090048208846105099,
                7942337936067504697,
                6101010891552466847,
                6082670434481396947,
                8347383472288259315,
                -3273256237442227457,
                1091203564536616930,
                693072066150424489,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                143631.7224235234,
                970792.6617652655,
                935026.9925960787,
                -14104.599716137673,
                741276.5955378215,
                417764.66018489,
                151289.7164644435,
                558716.637212385,
                -70312.80198213313,
                947459.1640817558,
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
                False,
                True,
                True,
                False,
                False,
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
                '20220526:210903.259092:+0000',
                '20220526:210903.283068:+0000',
                '20220526:210903.300713:+0000',
                '20220526:210903.320971:+0000',
                '20220526:210903.337837:+0000',
                '20220526:210903.354525:+0000',
                '20220526:210903.371192:+0000',
                '20220526:210903.389674:+0000',
                '20220526:210903.406605:+0000',
                '20220526:210903.423434:+0000',
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
            'name': 'ӹ\x97ƼƌǇŴҌѱ\x97łʱ͵\x8bƢǝ¨\x81ĂVˉʞǍʹîÝʵɂ®=ȫ',
            'value': {
                '^': 'datetime',
                '$': '20220526:210901.949465:+0000',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'À',

            'value': {
                '^': 'float',
                '$': 878401.4956966526,
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
            'catalog': 'ŷѧɢœæѼĺȜnʻȩʌԢ\x9eӁÑʉ˳ϵҴĒжӦɗȜ\x8f*ơˍӯ',
            'message': 'ϴĻщȶΚȴĎ\x8eǱ\x91Ӥ\x9fωΎƱӨ·˹zˣįɹķȺμЃџ˰Ȏƍ',
            'arguments': [
                {
                    'name': 'ҊƬǆĺϺɔȂ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20220526:210859.807606:+0000',
                                        '20220526:210859.823969:+0000',
                                        '20220526:210859.840921:+0000',
                                        '20220526:210859.858211:+0000',
                                        '20220526:210859.875446:+0000',
                                        '20220526:210859.892208:+0000',
                                        '20220526:210859.908804:+0000',
                                        '20220526:210859.926223:+0000',
                                        '20220526:210859.942879:+0000',
                                        '20220526:210859.959218:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ӎáȏІύӜ\x8bƤËͲƲe¨˹ȴϫίѲŮʝ',
                    'value': {
                            '^': 'int',
                            '$': 5605138095777880585,
                        },
                },
                {
                    'name': 'ÇК\u0380ԗΗƎɜÍΆȲғƌȩˎãϋΩ1ņºФϪ\x80Ѯˤ\x81ěǔýʵ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        894350.2667161176,
                                        869922.4646078462,
                                        471758.66588401305,
                                        64434.93508441135,
                                        738555.06120077,
                                        612291.146790691,
                                        602632.5366259175,
                                        812288.1707999674,
                                        815329.3600995636,
                                        814653.8899017648,
                                    ],
                        },
                },
                {
                    'name': 'ĸ^ƻЯƌȑàBҫђѶɏ,ʜkǁÅˈʨ\x91lsιԄxԌ2ңźˮ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'Ƿ˒ǹĖӺXđεΙɞпƛ\x89҂ā˹ΘżŷϧϼөΟґĲƆŘӜ϶ʙ',
                                        'ҚϋȧvϓłŃӧȚǜ\x8bсŹӇӢгÍуԔʫҡ)ҶЏȓөӫϢԅѴ',
                                        'ɕӡѯƗ[ӞƷƬΫ˹đȳiͼȻȘˑǅɌƿǅ҉·ʕȉǁǝŰƹ(',
                                        '΄úŚǊ)ҤʉӦ\x83|ĀɞХƙʒҽˤьΞȎˑҌɫʦц\x9dDĵȷ˫',
                                        'ȆЮÈБɑɉýϾУΆìˆϾʉƁǀȺqšӺɉªˏҭΉÊҸȷ˧ԥ',
                                        'ċо\x84µɔˏҔƘÔñÂˇʅϵËΒǙʌ¡ЄįΥȊʺ\x9eƆϊŶοϒ',
                                        'ҤҏǩƗӾϰфͻȐˇǏȈʂƗњϊbǠcƩΫԩƃĀóƌύη³Ƌ',
                                        'ǌ҉ˣǔ˭ԓȧү΄ˊ\u038dͻΩȫә~źԄưσî\x83Ę\x92ʶͷѱЈȮǫ',
                                        'ʻ\x9bˉǠŻƮʧ¤ѶÃ˞óӁʧœĲĳfȢǥƳ|ǐ˰ƉЋ(ČТǛ',
                                        '¦Ԑɼ®ʏŮŗӼ\u0378ϼH˓ϞƻТ;˖ф˥ůěͰȂŌƄYřǶǩʝ',
                                    ],
                        },
                },
                {
                    'name': 'ХɽяĆGźÊ^ʈ½ЏҟЊδФНǼǁ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
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
                    'name': 'ͻȀ\x99ǀ҈ˉʞҏњǧǘϙLʦ\x80ȑΎFɆ',
                    'value': {
                            '^': 'int',
                            '$': 6161136856566304246,
                        },
                },
                {
                    'name': 'ԮʨmɰuӦΚ|ÜΦġȣĹƷ\x87KʈØӸŽǿ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        997011.4156982552,
                                        968035.6694418797,
                                        584161.9487989008,
                                        686405.2325905923,
                                        282834.6735647643,
                                        531081.1352827958,
                                        534869.9925519994,
                                        795879.4788215816,
                                        918436.3642104361,
                                        756209.9541926886,
                                    ],
                        },
                },
                {
                    'name': 'Ŷɛnʅ\u0380',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                    ],
                        },
                },
                {
                    'name': 'ÁҊ·ХʑˋĖԨηԈŧĪ˅ҋʅDӣφĞėǦӗ˰ǐűƇɏʜŎ§',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -5084500617067332678,
                                        -4899861580344667901,
                                        3713296147257617105,
                                        5338325576670856825,
                                        -7298522885266860959,
                                        -74334534997827855,
                                        3964528461212341753,
                                        3337173736013689126,
                                        -5007265682258326681,
                                        1561929135358678969,
                                    ],
                        },
                },
                {
                    'name': 'Ŭϱƛө=ʓ"ɴԡÇұ®Ʒԧȍ¸Х',
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
                                        True,
                                        False,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ǸǮ',

            'message': 'Ҫ',

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
            'identifier': 'ċɜ˄ĻˮÆʲӗ#ˠҧȹʈʸκȡɑʁĶʐǱƇŏɠҤǫȭũʐѽ',
            'categories': [
                'configuration',
                'configuration',
                'invalid-user-action',
                'network',
                'invalid-user-action',
                'file',
                'internal',
                'invalid-user-action',
                'internal',
                'os',
            ],
            'source': 'Аоб\x9a˻ĺjĄԭӣŝѨӅŢæĮVқ˰ƩōͻˬǀîŇўӪϾЬ',
            'messages': [
                {
                    'catalog': 'ęöǼRњŧnϵѻȢˍyпĦУ¸ǟƅoą\x9dӌxˤВE\x9aϠoʢ',
                    'message': 'Î\xa0ӕ\x86Ӣѷѝ˞˅ʸЏɵÁ\x91Ŕ=p\x8a\x91úʐͼGɨб~\x94ʥҭʙ',
                    'arguments': [
                            {
                                        'name': 'ɻԄɡѲӶȦΚ˹łɠ˗ӠʈАɕçϋͽ\x85à7ʿΤ_Ǚǉ\x89\x8e',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210844.402403:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ē˨ϚËˮƖҬɝґʀ\u038bÎŚlĪʤīƤ¹¤\x88sɴɎǞБ\x98Þ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            798.0608653477102,
                                                                            851054.0300790011,
                                                                            586868.2162762891,
                                                                            441501.42487837374,
                                                                            801386.1159421665,
                                                                            313966.81268533715,
                                                                            106935.82472682488,
                                                                            750328.027908074,
                                                                            857459.999943653,
                                                                            464028.4202632435,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƿʫ˲ӃϝƗ˺Ư5ő',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3769747989429134557,
                                                    },
                                    },
                            {
                                        'name': 'ЍɞǢίÐǲΪXʙĻĆϧȁɘųӂƝʅȖҞɗʷȲ4ɎӓɻǗɽƽ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Żű˄¦ΟγţЪѮӎêԭϱ҉ҏѳČѮҞÝӄ҅ç˶5ͻƗȕÉƘ',
                                                                            'ĶЮŖţ\x8cʲĻˏͰԃǙŔуƚЀҔѺԚĬϴɒƎHԪɓЗ~ǹʭґ',
                                                                            'ȟˌϳXΦΞԞÝɶƈȨÏ;¹ѯˑ˹ϩCĚЛTʺ˪ĬȧΏєДҏ',
                                                                            'σż˄ÛBˉ¨ΟȊɉυѺʕƬȶǵϧ϶Čȿ2ӣФԇэʒǰ<ƦӞ',
                                                                            'rϽɿ˲ԅҵΈӯȌйϐȀƱǚƪӀИɻԅhԜĉ÷ԪϤϯӊȡĻӌ',
                                                                            'НԓŲӒǈƏșҽϟ˭ќӤ˳ҮҮśkшԨõмCѥĿǨʸŲӋЊ\x89',
                                                                            'ǓϭȇƱȅJπΈɋōǐƝӯёҤοЇV¾-ïϮьˀЩȅΟ`чǢ',
                                                                            'Ƣ$ΖʆCƉŹʦε%ǹӄ.īҀ½ӝƦұ\x91ʢΈğưƁĩǲǣԢŨ',
                                                                            '|ҽӪɄҗҊƫγο˚҂ΘҦи;ɦϖʅЬƋʫӠԘѕ8ŝϮʉҙϴ',
                                                                            '&˺ԤҶøӔ\x81Α˗/ϩʗŰҡͽ˴ÖК˙ǊϽѨěʇйņ\x83ŗԓÑ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȹπԘśþʼÊԖŰυĆѸ҈ӑǯ=ϳΊЦЙJoˠў',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 114334.49245112666,
                                                    },
                                    },
                            {
                                        'name': 'Ѳњ\x9eҎҌǥ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5343835167536894853,
                                                                            7196974557058029631,
                                                                            -5410259475387245251,
                                                                            -4196028832990964113,
                                                                            165845525206845354,
                                                                            -2446194572066209474,
                                                                            542581987460798839,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҧ,ǎȩМń+ȶ˛Ûǐɍ¬ǽРэԦɦӻƁԒʹ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210845.295164:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǜʁǢϮεqŸҜϰŏɷñǫƨǖȓïʠϭɠƼ¤Ԏ˖ӛ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3394597421171760357,
                                                                            3151607298882867206,
                                                                            -5970524618389971216,
                                                                            109046891241761544,
                                                                            4712629021867888850,
                                                                            -2967338545775244420,
                                                                            8008819848204831537,
                                                                            -8513384526519057300,
                                                                            -3274835513126395856,
                                                                            -7216472903002719952,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˶Ёü΄řƿѩԋgӯӥ¨Уΐōԕη҃ĩT5|Χ˔ȕӥӃʕϞҤ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '_ϋЈʪԁӌ\x86ɴ£ЮЧͳˢ³Űǔ<ŠϖɆпΒĵϚ\x87ȠκãǇȂ',
                                                                            'ӇϦΊɳѶ˞ͼǍȥÕÒȍ/āǓ˭ŠűȘŧԊɽêЩĉхƜ½ȕɛ',
                                                                            "ǜҢȈɣ˸ɾώοđĻŵ'ǚɔϼěȫ\u03792бàрsΛ\x88ѩ˵҂ţǘ",
                                                                            'ˀ˔\x8eΓɀ\x88ŶËɥͻŒ\x7fɶϙɤƺӲƑѣȎŖΓϋªӤζѬɀȎŗ',
                                                                            'ˠóіʨʵΘȻʒЉǟǹ{чΒҌ҈ʔ˻ŽЗ³҅ԅŧüªtǏϧ:',
                                                                            'hпʹˎ³ϊʊǕǎҊҫԒ҆\x96Ɔ·ѵjԒŧΐêѨɎ˪ȮRЯǻԃ',
                                                                            'ɑƅȿȢĒˣҚͼԦυ˗çǛҹԒёˀfγʸȹƍͶÇĨŪM}ѝЬ',
                                                                            'ςʅ«ѱƽȥόҗ%ͰҘȖɬӏΡÇʓµBˠèȍĀTԋϳǂҙƾӪ',
                                                                            'ʕҋĖ\x9fөȑŬſҨāɝÿӪάЙӇľѼԘSɤçx\u0379ʫη¢ÊӎƠ',
                                                                            'σ¾ƥĊΛӨȔǨWƱ˔єͼɯĽhʵƊϴҋĈƱѲӚǬÌ/SØå',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҇ǞӉşԜРȠƧȇĳЏǝ҄ɥɩīSƪ\u0381ΥǊȺųŲɕȱįұʐÔ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\x8fĲ¬ѵ\u03a2ĭӃŖŕÿˁȄӵ҆҃ĺˁӌĉҀӄѤѐŗӋɢԘ\u03a2ĸа',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'џ¹\x80ӛʥǌŧНõΕŀƀԑǶˆēĻәȂӷҪɭźʧ҉Үҽ˵ϰR',
                    'message': 'әˣϵ\x92ϐHʉ\\ӫƊƐϒzɡʬT0ͷӔȵҫԝMψŢΧǬɻњѧ',
                    'arguments': [
                            {
                                        'name': 'ɾuƿ|¹\x8cӱʼӘpˡϕɍqвѡȑɊȮЫșΦșɧʶώƁň',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7652051565332668010,
                                                    },
                                    },
                            {
                                        'name': 'ҙã',
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
                                        'name': 'ĽСǂOȯčǡ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5684161859855491388,
                                                                            -8504142876908777308,
                                                                            3073605183576494758,
                                                                            2855708327649670239,
                                                                            7282706027319366356,
                                                                            4428769406381580832,
                                                                            -3413968190481167813,
                                                                            -7250968513514545490,
                                                                            -7115208037212957790,
                                                                            195591751471434532,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƧˁǜAҠǟ¶žÊȎƫҲ2őΉРȯҿùǂ\xadԖԢӲȋΩ=Ӧ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\xadȧˏ\x9fЉg˥ѣ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ι ȢӋGҭ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 564314.2611265739,
                                                    },
                                    },
                            {
                                        'name': 'õнő',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5515054012292331963,
                                                                            -1056561149356938478,
                                                                            6327993035782727293,
                                                                            3607700150675071517,
                                                                            7033870067557208532,
                                                                            5156950636437711928,
                                                                            -2330093342396013740,
                                                                            4358567117187861554,
                                                                            6193199900829246870,
                                                                            236174452869849953,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'νɻ˦\x89ų˦ϡ·ӨӿçΗȨΜŕŢʠ˷Ư\x91˲şѽ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6730538388822880038,
                                                    },
                                    },
                            {
                                        'name': 'äӲ\u03a2Ɩ˹ӯKȎƘοƭȴҴԧϰƑ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ºѠҝӌȼƜχŧѲǜųaʢcȶâȌªԏƓϛϞȎǉʗǁÌΥԙǀ',
                                                    },
                                    },
                            {
                                        'name': 'ʼǫнҔΝ˅fͽȽӜʞΝ ÅȻӆȇȉъѐөϥҕĀʗĒƍśȂҞ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2536530727298048418,
                                                                            -2899230754283050656,
                                                                            8885086196225227040,
                                                                            3617411550155386371,
                                                                            419737011130485925,
                                                                            -7380262458745343392,
                                                                            1659709109054535435,
                                                                            1512367869241190673,
                                                                            193025475184221755,
                                                                            -7958425738948791736,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҫϴӞŏƼĿʆәƑəʍӤťʱөʔEϥΛɁö˴Ŗˢãĵώ҆ȁĤ',
                    'message': 'ľmŰͳð(ɮʉҪ´РūԥċÉњϮшȍɦ˥ȇżʋˬҚŬǭϡʑ',
                    'arguments': [
                            {
                                        'name': '˃іʳ˞ǒʧʎӆĕϜĥʸ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1636728877498559146,
                                                    },
                                    },
                            {
                                        'name': 'ƗǒƷdɽɕǄҵɉ#GŎ\x89ʮƾ§ˑѶ\u0381ёЂŻӓɧʿшӥǈͷĸ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210847.671788:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ъʳ¤ƄɊɜ\x8eξȯʞAˣ˧ʦЧѮ}ҎěĶŪJiњƁҺ҄βÔɐ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƣʹÝrĴѤΚӬ\x99ΒĆĄЕº˶ƨԫӼϽĻϱΪlȁȾ#ψ[Г˾',
                                                                            'ƑˡơͳʔѺѳǕɮġƂÄӠɶȴͲӈҧǞԎƂʗԟ˯Į϶Γ\x91Áɪ',
                                                                            'ʫȓӺн˗ӯȄĿҢѢϕŜ\x90ɠ\x8eϸŠ҃;ԃȏùĞƿӉҧуԐuı',
                                                                            'ńƠѸɘ\x96ͱӵ|ӄ˭Ɓ\x95ӢʗГҙƸˈ%ΒΚΉγȤưʐÏФŉ˵',
                                                                            '¿Ӧșʦ1ƆʋΫÛΒǂҡԝơʡŇºīǾӪ¸ʉҶЌǮ\x9eʏψˍԜ',
                                                                            'ÛӉΰƃƋKȑԌɅ>ĝʯʳąǐлѸū²Ԃłʈ*˒ҐȕǞłЄΩ',
                                                                            'ĥЕӵжό˗ȿʴƢŖT+ϘċƅƠώΗήȗɨρλfƚˍюƠ>³',
                                                                            'ŬħѠšɡĚǧǆϽ1,ξΈ\x92²ŶȃԇϤҲʦ¯ǌɮȢҐҍŴϹȈ',
                                                                            "¿Ϗγ˂њÊȜɈҀWӝԑЗИѮÈє:EÎ¬ŗ'\x81ә©<ўѷ˲",
                                                                            'ѵӁϓØ2Ɩ´ϸŽϾŋҧҥӈĮĎΜĉ˩ПԤΏîiōìƪφȻ3',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΉҴȋŭѰƚ˙ОŬ\u0382ԧ\u0382ҹ±ǞƅОĂĎɇĤϮԗVӮwˀŎΩǸ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6759687700565743909,
                                                    },
                                    },
                            {
                                        'name': 'ƺАǯ8PԞƾԥ¬ƉɗɜώήĎ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Žʩ\x91е˨ŔҜҤϰԄ|ϠĭΒÜêÑΒӻ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8048648691784806550,
                                                                            -4047598748513787915,
                                                                            -1800628316599659636,
                                                                            8902892631650325298,
                                                                            -8368605132949269764,
                                                                            -3121340876651283593,
                                                                            5434431396944112564,
                                                                            -998686921087160197,
                                                                            724343397842363819,
                                                                            -497961614378758617,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8eŀαƩӝȿļƥϚЮ\x85ҁ5ƅңȘҦѓԈɂԞīʼ6ʏŮēûӴϘ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            596813.5432694413,
                                                                            267951.2753629035,
                                                                            128090.26872505105,
                                                                            838525.8585212714,
                                                                            539006.8801055141,
                                                                            529589.1513634275,
                                                                            263756.74023801467,
                                                                            111102.04916953246,
                                                                            449690.0660354103,
                                                                            258681.45519723516,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɳȭ\x85ƞ˕ŭɲҸɓǘψɘԥΛ7ǫÌәÛQӴT',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '±ѧϿgҡϬОʹʰєƴ«ϜԂʍČ_ʹӍĚɗԍȃĤЪůҹɭʯЉ',
                                                    },
                                    },
                            {
                                        'name': 'kəӍ\x91ϨÚ³ЎȨ˯ƫøҔɸƇƌРʋ.ƚØЀʼѦÔ\xa0ɳ˦ôϜ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5337173787774816287,
                                                    },
                                    },
                            {
                                        'name': 'ɁϢДɏԒúΌǠʰ$ǃǞǫƧīæϐÛғɥǸõĝҫĄΰȱӥʥ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -143212711213137569,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ň ͽ÷ʶǳYǂǕϢşǒϛɦ˼ǢҿN¾:ĤƏɂωȒqƃԉ˂ȧ',
                    'message': 'ҒŢǣ>J\u0378ƳˬѦмþԌЫ˥ԞƕǐφȰʦЅɡ6ǶÚӢŋʐǖϿ',
                    'arguments': [
                            {
                                        'name': '˙hЌɇȜͻsςԞʊ˥&҇э',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ŨϹƜÚɿɫ\xa0Ѝêǰ\x9fhӛԢÁ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            842267.5613543965,
                                                                            -26584.916430243902,
                                                                            208867.46818717133,
                                                                            304276.5167182529,
                                                                            139913.93899105166,
                                                                            210169.49279205676,
                                                                            31173.308542930637,
                                                                            281152.56941856374,
                                                                            771419.6581426101,
                                                                            704569.4524864567,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȳŻƾѝƄ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 633456.8275590579,
                                                    },
                                    },
                            {
                                        'name': 'ɩɈԫХǯ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210849.278883:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ѣ˖˩©Ƒҕǉȱm5жĢ˥«Ԥêϼԙ±О¿҅ԢʀǓеΞҩɹʃ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӍİϵǻüΚëȧʰνϒɴωЊЏɐШʾ\x80ĤĉãͺÍίηѭÄ>ȝ',
                                                                            'ņțɒӋĔāɶ4Ų¶˟ǘ\x88ʨӣǉӿҚʿɨƈð\x9b?ʫʠʏǣѷ<',
                                                                            'ĆɂĄЖ3ǄϥӌІľ˰Ɍɀң"Ʀʫӿқ×ÒƜóӤǮºǿҹǆʃ',
                                                                            'ӸӲԌѺӹϵǓȌǡ¢ȖϽҞʝϦĠԚƅÄΡŘνԑƗϘ\x98ĨϿĄƅ',
                                                                            'ĞƫǞŞԠμɜȪȴŐʞхˢĪ˒m˟ȕӹΪQѻԇĺ¼Οʰʽԃˌ',
                                                                            'ɓѹ·ŞƿĚƱΞϱƜм˅ѻ˶\x98ǆӋӂϯҡɗĺʲʍǽ;ЙĖˊȫ',
                                                                            'ƺaë˩бϺˌέϤɀóљӾʀ~ԏɩ±ÿôlͽ҂ɻĒˁɬŽӉК',
                                                                            'Șȸ²ӀҖɠĖυǈЁŠöæ«ɱ¶ЯάƑԫcÁъɖԠοӤIȴr',
                                                                            '0ƍ˂Ԛ\x86dâmĒÞ0цŇĿӛ\x91ʊҗтҵʒӬĮт·υȴ*ӕЈ',
                                                                            '²ʫk%ΥҴǉˎԥļŎŧdCƘ҉ҍɶƐƧϿÉҕȊĖɄŹȀF\x94',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˯ŎʉӆÁ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѱɚӷ͵Ы˶ʭǹЂ\xadԕĉ`÷ʢΖǟ´ӲȦμ˲üЪĉI\x93ȼ΅ó',
                                                    },
                                    },
                            {
                                        'name': 'ƷǭƜɇҧђÎϼɎ˷ӪЫŎ8ϼϳãȻ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            58570080832826680,
                                                                            -4449544730495642683,
                                                                            2061102279740205586,
                                                                            2968536396294736358,
                                                                            5215692596963545758,
                                                                            2152398211701096111,
                                                                            3310825185182501526,
                                                                            1219620048035083604,
                                                                            -3886664664044171593,
                                                                            -8844312255202372247,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Њ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7588721184591374951,
                                                                            881997232737036820,
                                                                            -5233552699016938516,
                                                                            -1167939164354176028,
                                                                            -774599381098189224,
                                                                            -4104592794285706843,
                                                                            -7582575434037386094,
                                                                            8926123524997453115,
                                                                            6079203690467847631,
                                                                            721073610974833081,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĊŅТʜ\x87ϴ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            228688.08498375636,
                                                                            69950.14816511676,
                                                                            555434.3708770665,
                                                                            19599.20071422268,
                                                                            459098.8620271913,
                                                                            765596.1514190519,
                                                                            237575.27227577206,
                                                                            184356.16113435384,
                                                                            290726.8185320198,
                                                                            778132.3234545812,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'WӽѽĎȂœľĎ\x89wŜԠ¶ҿʯǂÔҊЍѡ҄˺цŗǄңƆ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ηӬ£ȲԊ\x8cϨͱLčǼЁƲԬӁϘАϪћԔѥčӌ',
                    'message': 'òќƩʦȨΏ¬ͻʄɾɼGНςŴŎȲӉǨ(ʙәԢŏɄϜǴǮǎ8',
                    'arguments': [
                            {
                                        'name': 'iԏȧǾɇƟ\\ƕăԖωӀŗŴʲşă\x9aȏѴ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӼqǯŉǤҞkϝ7ˉÛЩȺӲԎЊμСÛξę˞ШΟȿȵЋȇԝK',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 337519.0409903717,
                                                    },
                                    },
                            {
                                        'name': 'ȼӁԣԜ˻ǚЖÛ¥_ȖΩПƦFӕĆȱ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            236283.13876593858,
                                                                            834156.3958965065,
                                                                            26769.78595648057,
                                                                            198439.10793761787,
                                                                            106969.73075981328,
                                                                            669979.3242432328,
                                                                            700728.0974398192,
                                                                            230422.30438734422,
                                                                            319405.09056173655,
                                                                            -47589.23741857092,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ŊϸμŪ'ıʘԨ\x87ř±©ƵÿѮσǽҷ-ѝЇҁ\x83ԩëɄѾȼʞʾ",
                                        'value': {
                                                        '^': 'float',
                                                        '$': 522868.7412206606,
                                                    },
                                    },
                            {
                                        'name': 'ƳɫЬb\\ӕʀҐ˥X¬ѸМ¯ӾЀƤǭϽƽ&ʏǣƾЕЬϴӿǏϠ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210851.021237:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɺɽԑӋÇҗУє¶îĢƟŭȝǨɲǷҪ¬',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5851764188243644994,
                                                    },
                                    },
                            {
                                        'name': 'ԙȣ\x94ŧͲҐǁʵģûѣѧ\x9eȅϥрęøԅgϯı\u038dԆԚʖӉʩҾИ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 638065.125479104,
                                                    },
                                    },
                            {
                                        'name': '\x90ǉҒȅīҹƽγ§ªˡѐǟϟ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            758029.5794352662,
                                                                            375105.9504011302,
                                                                            855985.0182907945,
                                                                            569263.3677777121,
                                                                            478098.91460688785,
                                                                            451217.41478511365,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8eˢɰφəɍȇҌɽWрĲЁĞųӬ˱ǜ!ѕ,ˈʓԉԕηʡȦӌa',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:210851.437116:+0000',
                                                                            '20220526:210851.455495:+0000',
                                                                            '20220526:210851.473884:+0000',
                                                                            '20220526:210851.491535:+0000',
                                                                            '20220526:210851.509847:+0000',
                                                                            '20220526:210851.528251:+0000',
                                                                            '20220526:210851.546479:+0000',
                                                                            '20220526:210851.564819:+0000',
                                                                            '20220526:210851.585846:+0000',
                                                                            '20220526:210851.603249:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɹɢӃȘҠŘŘ³ѺƓʋåζɔǇœįÑuΕϩωДcsƜ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '³Z¥şѫϥњʵԊȀ\x95ԬѼĢԨӪǭǻуї\x92ēɑhѬ҅ĎϾљΈ',
                    'message': 'µǃ~ђʓƓҽCΈƞԨгĂӼ˯ӄԇ{ϻõ¶ɯϽ˵ДӹŋőXĢ',
                    'arguments': [
                            {
                                        'name': 'Ͱт_ӮSӜ˖Ўȥ»ɛ˥йξѱΠ\x82ʞƽϸjҲ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ϛϜêӡέӣɉώԡǂŷǯ\x9dƓƷɷ\xa0Πѽǣ«ǟӝȨөãΪΦɢԮ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            506145.0787520433,
                                                                            671588.4284075765,
                                                                            585286.3895949414,
                                                                            740171.5144828741,
                                                                            71103.77305469033,
                                                                            974605.1742263865,
                                                                            271710.8254812361,
                                                                            86633.21098989822,
                                                                            918608.5234147677,
                                                                            346115.57543579966,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҦĭаźÈƈϩҐџлʅӂϱʃȅԦʕǝˌƹ<ӄеƸЁxӶċŖʸ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2473303601274728621,
                                                    },
                                    },
                            {
                                        'name': 'ʏӾƧδŉūżGʐͿϢ½ΆωЊƭͶŴΣ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӯ҅ƭǋҁϭĠϺǄɨϻϮ7Ątӥ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:210852.297699:+0000',
                                                                            '20220526:210852.314064:+0000',
                                                                            '20220526:210852.331780:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'мˎΥɬϹȅҠƟ\x95wĺˉŸĹóŚĻіQϙѲ:ҹƜԌ¾ȊԁƻĆ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 664180.4770258773,
                                                    },
                                    },
                            {
                                        'name': 'ЯȡѣǓʷņ\x94üϸ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210852.488403:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x9aλӾϪ˥ɄӓӺʡ²ГƘśƬΰҧʂŎßˢʊȏǱȢ҈ƿɉӯÚΊ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            888241.0140498428,
                                                                            198184.3197948319,
                                                                            699888.5607570094,
                                                                            80502.87681244093,
                                                                            279368.3231435006,
                                                                            704308.7086110975,
                                                                            354632.1369851958,
                                                                            590720.6681603971,
                                                                            999319.5696570156,
                                                                            31480.234095223714,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԋopǩӬǨѬøгзξȬŇʝ@½ӂ˲ĆЋȉŏωϮҚϪӜϔǦЎ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'һɀ҈ϡŇȤŜm,Ϙľεŧʔ´ѹǮLΣ˾ЄлʇӾȉҫǄˬԓϻ',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҧĬȺûħΘėπŽȦˆβɋϰ¢æųŽѾŸɦŖĂϢ˳ӜӊʇΛģ',
                    'message': 'KʺȡƗҍƊĺϨʺʤ˒ĨūĳӭſɪҖҢҁʓɁȫΊϔϻҹɤͳƆ',
                    'arguments': [
                            {
                                        'name': '˘ĳϻЍöʻȅũŠÚǝ2ɀѢԚàʪƺAƞƣӱȗѪӧҜō±˄Ԏ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210853.233581:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϬӶšɚȳ·ˑɬe',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 634674.3003467447,
                                                    },
                                    },
                            {
                                        'name': 'ΏΞӅɛĵҡǘ˳оХǈğННƚ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210853.377350:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ЙȿīƱвԍȍώԏxЀxӧƣυ\\ӕˎɨr҄;ŤǆHńıǁѼѵ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 750446.6955918949,
                                                    },
                                    },
                            {
                                        'name': 'ǄȞŷǥу҃ϟ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210853.520435:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӼʑøƸѠ˫ǅǑКҦźȪɘˠʪԫɬńѫLѫΤƚśԙ\x86ČƹȒѢ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˦˒¯êЁȃЈǐȕƸӰȓŝņХKЙŇȵθ4њʈԑľϽʞˇ.ġ',
                                                                            'ӼĆŒƙ&ΌΤɣˣEԐЋŇӂЅȞ-Ÿц\u0378ԫкÏɟΗʿԉјίȆ',
                                                                            'ą\x89ȳлȳǩȣŴƱұќ˕ω\x99ȲОӎԈēʵ˛ǓҾɝ=юʕäӱϥ',
                                                                            'ǲξȎƕԁ¯ĭ˼UәʿЀΤж˗dțѲǒΨΊ¡Űȼԑ\x86ĥqѳҟ',
                                                                            '˹Ʒҗöʺ˝АÂҟӬžԐèϺƅɄƹɌÑͷùӅ\x99Ěƅ˵jZФΑ',
                                                                            'zŞâ6ĢbÿɯUȒŞѣς˫\u038dǁĶȿƿʦʟʺɝӵąěϼ҆UŻ',
                                                                            'ΤȵlŶˊɈǂǞɆҋʙɒʭԣj/ӓĂÌѡǓǚăԥ҉җgΥ\u038dȞ',
                                                                            'ƯҾĘς˪Čѐ˨ӰрəԑбĹǢ}ǼϐԩϚ˾Ӑ4ҐňðʍԭŎʉ',
                                                                            '˔ʳĒʮйχƏ\x8dºÝǬ\x95Ǚ˩ӊϘŴ\x80όƻʙȑ҃ɻҹǬӯʷȇ˰',
                                                                            'şҠίŉ΄ЅҦӕњϲϐʂğԧÅƒ˟ȬºɲȴԩȊm҆ƟĹUΚi',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¢t\x94ʶʪҗ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7871684682672635415,
                                                                            -7257079071915116666,
                                                                            8268813984760776165,
                                                                            -7811645892802413796,
                                                                            -9175443385413953034,
                                                                            -4556400592868309645,
                                                                            -2123719064466096503,
                                                                            -5018597412649320132,
                                                                            5532562752016899047,
                                                                            1839324590241106642,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȽӔàԏшЕdӲԧǝˎǫ˷ѿ\u0378ԡЫθȀԭ҉',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 122567.11516568897,
                                                    },
                                    },
                            {
                                        'name': 'βbӔĸ]Ȩ˵цҝ˹ѱ¦ϘҘөʼҗ~ЧӖÆɯ|ȧ¬ɧάӐϞ-',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210854.224956:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҍƬ®ϡϩǮŋϞˊʛ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            685405.110351542,
                                                                            844152.0826614466,
                                                                            717807.2606404609,
                                                                            539261.9082270663,
                                                                            -84581.12522208582,
                                                                            889062.2973788388,
                                                                            432016.58275450976,
                                                                            659174.0850948379,
                                                                            134828.32947071956,
                                                                            834488.5081678068,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ЊΘțƗҎĳћ˼ŲϭϾѸǍƌȔΐӊĳҐҪƕӔШѮ\u0383ÑΖŤŇѰ',
                    'message': 'ȭȣĳːZԋŵͿѰøiϙѶͺ˟\x9cПʀΒ1˖ˣѻɭʅϫҡ˻ɢМ',
                    'arguments': [
                            {
                                        'name': 'GͿÏǕ˾´ºї',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            810986.5274633697,
                                                                            475373.89927470614,
                                                                            96223.02965762885,
                                                                            -32649.44195639927,
                                                                            -89468.17235796833,
                                                                            -86555.6727369947,
                                                                            389802.3860245685,
                                                                            983169.4489819286,
                                                                            543576.2444510168,
                                                                            158191.18402083454,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'đФƭrћӼқĈбӼ\x8a˻үƁЈԝñ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            87743.84827579648,
                                                                            510968.31523563585,
                                                                            8150.945935893324,
                                                                            837548.6024433406,
                                                                            620654.6233568849,
                                                                            323050.7295980139,
                                                                            683268.0355448365,
                                                                            95827.54287805679,
                                                                            254706.07679242262,
                                                                            927195.3882331696,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǚ҅ιԝȑŝҔ\u038d\\ê˅ԫƈΐɊϿȎĖƼŝԆ[',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʔʐӓǽ\x85Ȕ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': 'ńáЇήįψàѩ˙іɣӻĽͻшóАýųԆҪÛʖѢѣΰɉêБƱ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210855.477166:+0000',
                                                    },
                                    },
                            {
                                        'name': '·ΉŨ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ϹĶΗŘɭƐǜȼυěÌʽ¯ýɇ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            66287.9445544345,
                                                                            -77932.90996698357,
                                                                            986217.017468326,
                                                                            405414.1952976528,
                                                                            741568.8538117451,
                                                                            574590.632283281,
                                                                            756747.6371941718,
                                                                            662166.1846954552,
                                                                            952851.3697472576,
                                                                            165419.5391693185,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ιŧӗ\x8dèĦЩϑɈˣ×ÍԫHԇԕƆc\x99βͳϺ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -39780.385474751776,
                                                                            780360.8307828993,
                                                                            547307.3228302116,
                                                                            87412.18574484065,
                                                                            501881.53598847135,
                                                                            47870.22822271538,
                                                                            414295.61502617924,
                                                                            848632.1495315403,
                                                                            375001.46592531155,
                                                                            551738.2894729795,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǶΞɿp˶ƜιΖЉәΈķ\x9aӟĪ$ΊԧѧŖȌ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˫υ\u03832ίϓю²ʭүԤĦӓǩҙƖKúƈT©ԝ˚èɴ¬ӒҞҕɚ',
                                                    },
                                    },
                            {
                                        'name': 'ʣǠ[ĨÀзНψĀđƋɮϪӪГŁĺώЏǜĎϩΉʤĊȵӿЏ\x85Λ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:210856.250764:+0000',
                                                                            '20220526:210856.268627:+0000',
                                                                            '20220526:210856.287072:+0000',
                                                                            '20220526:210856.307338:+0000',
                                                                            '20220526:210856.326552:+0000',
                                                                            '20220526:210856.344969:+0000',
                                                                            '20220526:210856.363062:+0000',
                                                                            '20220526:210856.380680:+0000',
                                                                            '20220526:210856.398144:+0000',
                                                                            '20220526:210856.416166:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԆɟˢżϢхпі\xa0ƺŽǊȁʲӂѧŚĆø\xadϽʄˊ*ʖɢ^ʗÈӿ',
                    'message': 'ƣϺȀƧϧªԝġҟĤ[ҦƣĔɈtqȰæԙέǢ˔ԃʷѢƢȮԎЕ',
                    'arguments': [
                            {
                                        'name': 'ӣǈ¡Ѱϻ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210856.601897:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ЛɉƍѠɥBђΦåҡȍΖӪħƐT\x9cʣʨƄПƨʡFsщ\u038bοԚˬ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɞԘĨċǘʱеӭĪӮɾÝϤ˼őéĿþɰп}Ҳʆ«ΊƜӂЇĪʾ',
                                                                            'F˜IÓѪȉƈЎ*YˎЪrʎҏѕǹɄϨɅӽςģ˟ƻȄԈӁ\x99ɲ',
                                                                            'ÁʱѢĄΖŰӡ\x81ƅмԙʐ\u0379Іԩʛ¶ʙʣҘĢѓ²ŲԎфϦʬŷ˗',
                                                                            'Ǿ҃ʲѪʲ\x81ҜяÕҺăŶϝʰ-¤țǣɾЯâϞμ˯èɧȀӌɸS',
                                                                            'ȃşȺŒśȀŊǨԛћŤЉ˺ƂкԂԦvƞWɜǶ\u0382ťНϾΝǁʷԔ',
                                                                            'ϖƟΔȽγĪğƉӚÆJѤgʨ¢\x93ǬбɖĹўȋāԨƂäԘϕƁΌ',
                                                                            'ʜ~ğчόɇʡ\x83ĻþΖȽƗԙӘҏԇȺǺìƸ´¾БxˤϢĊī/',
                                                                            '˴вңЇƢ{ѐÍ\x8cÓ/ɄҴȼǌɳʨпć˘ǃ5ԮƜȣĦ®ѭʣ˳',
                                                                            '²ӗ]ȧΑX˻ɚɊŢѠѢ\x8bȫǛʎwԬАŪЦȹԃӳʃʫӘƀˊά',
                                                                            'ҳʳӗȍӒΖѭѳhÌƛÓåαί˔Ӟ˨Ξǳӻa¶ģʷǹFӞ5Ӆ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĕÙƑêɄ\x81ǱƖǟvϖˈҁϻрȨ\u0380ƛȵӕǻςʺĪһ2\x95Δ*ϱ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3563358384200301314,
                                                    },
                                    },
                            {
                                        'name': 'Ťӕйψ\x88(tĄSNӀΖԊŮeΒЇȄǧÝв\x86ҙмҊʵϸǙΌ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ӎĳɡ҂π˪Ϊΰ\x8cěʧɈѭȶVƪʰ\x8aźʰӧŸĢӌɯсCԥдɬ',
                                                                            'ÙëƬҨԁƨ/ҍǳЯԩη˼иRɲëÃ\x83éäʪHǼΎҭŊȬEˀ',
                                                                            '-ҬǫĜwŊƅƌʡʇϕϏғɧ\x9dԡΔҹϏϔǍʞƵɡөʪɌЬӔê',
                                                                            'FǆåÑԋΣĪљ΅ʫҦǀȳÄӬʬхʇǞĻuŉ\u03a2ΒҐԟӞǏpĖ',
                                                                            '«ɂÐЍѐƥмĮǞ˘ԣiǾӭŮҚšТΫҺͼőŎǊЎ¥Ǩ\x99ÝΖ',
                                                                            'ǧΜĵΩтѿŬ`ϹȿʯΖƼĒһɡȡɷԝҩşȫ\x99ДΊЊδrԉϴ',
                                                                            'БҎ҈ЁǉŏŌџԎ\x8fʃοκƶӪɩÕΒĿƧȷș±ĺŜћ\x8d\x87ʥɟ',
                                                                            'ˌԋȏ҃˨ӯ˷ˏºĎvфɶgѦVΞԩЭǂΤmƣśĤ\x8afȗʇǠ',
                                                                            'ǖƒɱǪĵВʃԆη˹ȔʥΙԁñʹȩƱŝДԕ\x9bβ\x89ʁюҸѶϏД',
                                                                            'Ǟ˪҈ҏʹѥɶʩ\u0383ĭņʖĺЈӵ˜θɤϗ˶ƒȠѧҼɭԚʗˠǷǱ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '»ȽD¦ǹԡӌżҟŢ ŦȼѫЇԓ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:210857.256594:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x9fðGʞҁĉ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2316789287820832025,
                                                                            367271565307924138,
                                                                            3558547634830689867,
                                                                            294911828490546312,
                                                                            -7769832609367294695,
                                                                            8742813991812670129,
                                                                            -971269377536315157,
                                                                            -1972658043454492843,
                                                                            -6086265649901356948,
                                                                            2890039824322070014,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϮщԢäȱѴϫҋӢ\u0380{Ϙӟ¢kÖǉȈƂ!Ϲ˘Ѩ\x8dγƕ±',
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
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǆÓԍ\x93ȱС<ɤϷSŒѯӵĲɱ4Ӹ˥Ӵς\\˺οϝǔãƝԏEǓ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 92951.27874494757,
                                                    },
                                    },
                            {
                                        'name': 'ʿѯřƨOóķȥΜŨɨǹċӚѩȍíȜҚѽïțϗöː¿ҠΧЮɄ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 291294.8784255903,
                                                    },
                                    },
                            {
                                        'name': 'Ĕю¸ȶIѤ˭ΒǅqдӂơǬΟκĽǻԠËƃʒ˱Є˜ώγ×É\u0378',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:210857.947632:+0000',
                                                                            '20220526:210857.964088:+0000',
                                                                            '20220526:210857.980443:+0000',
                                                                            '20220526:210857.996424:+0000',
                                                                            '20220526:210858.028753:+0000',
                                                                            '20220526:210858.051991:+0000',
                                                                            '20220526:210858.072120:+0000',
                                                                            '20220526:210858.088806:+0000',
                                                                            '20220526:210858.109216:+0000',
                                                                            '20220526:210858.133660:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '΅{ũɊɡɢȎǟƻǾŉűWʰǩӱǺɧϔɛѺϣԃãАͻΠyœϡ',
                    'message': 'FұͶͷϩŭı\x95ƤŔʓгɗũͲӤƎȣͰRтˏʲɯǁΑƫԓćȑ',
                    'arguments': [
                            {
                                        'name': '˹юʣӕŊӡȍԍɔĪˆȲȷέаƫƀӚЩ\x86ÌΆьG]Ћ\u0379Ʈҏм',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 563462.5576561966,
                                                    },
                                    },
                            {
                                        'name': 'ɭƃ˶ɮвϻŭp',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӆҺ҅Ѹ˩ǚӮԀŗΊģ˸œÆDXΫUҳĘΣΌȺГǄԞҸѴʧł',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2798808164098020499,
                                                    },
                                    },
                            {
                                        'name': 'ăдqɲɤԨ¨ˍÉȝΘүwɱƺ»ˮ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -37058867097023870,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƢȾԕƌҪʃȐʶл\x7fSĺσȐԉ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Əȿ[ɂҵ˟ˤһʡ{ϨǝӺ\x94¬Oņư°лϨLZЇӍƳȳÉϒƖ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ŮǅӃʗłdĠƫwŴſʩψ¾ƺͷĞӏ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            290930.2769376707,
                                                                            312221.1409526734,
                                                                            960132.3891238831,
                                                                            931009.3646219871,
                                                                            300516.57423479913,
                                                                            -89111.34431980105,
                                                                            533045.00708971,
                                                                            604917.0216269884,
                                                                            149435.00493382898,
                                                                            226927.77453380928,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'бҗΗԍ˧@άææ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            974135.1757456353,
                                                                            34618.20868135535,
                                                                            974200.9513064751,
                                                                            184344.93338191556,
                                                                            661242.4408447847,
                                                                            175895.5201685737,
                                                                            270064.50976226415,
                                                                            827488.4460882357,
                                                                            185652.20039652893,
                                                                            64973.66099814669,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĞǆϣϨЊƼÔ¢ӴǖĀ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 418956.69243016606,
                                                    },
                                    },
                            {
                                        'name': 'įňґĂ¡"˯ғʈθÁόĢ7ҨӰăЮȌ@ңӗҫԀȨ˼mʅ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5274182701211662855,
                                                                            -8649088465554177229,
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

            'identifier': 'ˑϣѨÕϼ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': '˘<',
                    'message': '˖',
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
            'name': 'Әöăɡ!{á\x9cɳпҚȪcёӑÔѱ&ыӖňXφс\x80ӏrɌ\u0378ˈ',
            'error': {
                'identifier': 'ҺȴɵʛϽϕǁȋЬ\x88ʈŇԌ\x87\u0380˘ͷѢї³ҬǷʖŏͳѪêȑƐӭ',
                'categories': [
                    'network',
                    'internal',
                    'internal',
                    'invalid-user-action',
                    'file',
                    'configuration',
                    'network',
                    'access-restriction',
                ],
                'source': 'ȪĥɌӊèΏγ˛·ϩBȆ>Ąǩ˙ǘ¬АħNϬЖ\x92Ƅ҇ԚˢҠɮ',
                'messages': [
                    {
                            'catalog': 'ѿɛӍԛǁĞӝȗɜϱиҊϙԋԀӦŐþǍȶŎɐTŁ\x92Ą˝ȩЧҖ',
                            'message': "ЈƔʅҬ'ĘϣѦԒԥşΘȫ\x98ŜğȀеĽȃʮԥǩȭҲÿÞďȾż",
                            'arguments': [
                                        {
                                                        'name': 'ʤβκʿȊd\x84Jӂͻ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӊѿ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Όáƈ˼Ɍвąfʲ˱ȉеɒɏǟŬԘѶʔƲʯ¾£ǯːʀ\x97ħĥщ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЌˈŘӒșԉÏ\x84ΞǳŤÈIΒéͼϮɶˍ±ҭȟѪƚǆ÷Ԡŗđ˵',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 93593.68428972072,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӟ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӰӚˡϾΥȚ˛ћъźӌþ;ɨЬűǸƂʜΖǟҖƈºҽΨǒԤɊʏ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '`ȕæʌ\x9cήəǔеǰƾĶВĬҹ¬\u0381˘T«˻ʺʾʹŎˤδñ\x93Ǔ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'όӋӁŗ҃Ý˚ȧ҃JΠMǿʫЃԧɃ\u038bϬЗРǦʐǃ/Ԑ4ǘ=Ɏ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǹ҈ƋɾƢоѡҧɜʑѾԞ#ʽŐĵˆȩƔ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'úăɎюԞҖˡ&ԇÒљˮ\x89Ȇйȴ§ϊεʗ\x95ҹÒ\x8fΔŒϣНɗԁ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ғüӦǣҿϪ^\u0383cʮɳγҢBƾʨόȉʞѴŕűψ6ýԞҙԎÓΡ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\u038dҺΉ΅ǉςğϔÃŬȐ˅ӷɱìýTųώʱ0ƺơНºҦ¢ɥЇδ',
                            'message': '˛2˓Ûӌ\u0380ƞϠʨʙĤ\x82Ė˯ǗЯˑđӫ\x8eWǢҋίЬҎͶŤт\x80',
                            'arguments': [
                                        {
                                                        'name': '\x92\x85Ӊ=ʭδдÕĬ±rѓǗēĦԔ|ӍϛйЯɓԖΧϜʻìɳĈş',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ЇҧӱƝҠ>ŁǆӼÀɌ÷ӫŎ˞ѪbíȀφʝΌ#ΩͶʟξŹҖć',
                                                                        },
                                                    },
                                        {
                                                        'name': '˭ʚΡóҥϱ\xa0ҥƇtɼ.˃ʈЮԋƱ\x93Ąь˓Ϊc˄ȖΎñ\xa0ˑĜ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӥ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʾ\x92Ó+ɊʩT+ǲÆȿĦ|\x8cԂWŌϛԧƕĄ\xa0Ƒʖɒǘ˹ϾɊɚ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҕǖʝҰγöӱԆѕͽѾɣƲ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϕɊȉħ£γϰǂЩќųʞ7ԛŀґǦËӲӋƯϕԓșԪƻȓșĆЈ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȱĀәĚ@҂ǎ˹ѭÀӾåǓу3ʦʰǯƳ˵¸8ͳ«\u0380ˡŇŰҁ~',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȅǾԑˢѢ½ÓɽϦΒɔùӵȭϙ˟Ԕҕþª',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 70996.1281767897,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʓӮɺȕǚȹӑΌЊϽԆʻӨ˓ѾӣƩ2ˡȕǘHϛɕѩԬÂïύǲ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȢϨ\xadɪӔ\xadьŨʋҡPҌѸƯҝǭАИФȭŻѽÐɵ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʺ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '[КҺǵӟ\x86ÈǱǗұǀϰ%ԟӨν<ӫɹӘɺґôӷίɿϴ½Ț˗',
                            'message': 'ʾȧɜ\x9fΦµɷ˽ʫɺû£Ρɠɐɏ0*ÒΩϋ-ƲœыȸLýΠԇ',
                            'arguments': [
                                        {
                                                        'name': 'ǙʿĲ\x9fˌҤҳ8ӾӋϴϝҠʂƜɰɜԋºIκӁǁƲƃЩУĐ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:210838.634956:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Śӫѻ҈Ѿ΅ЮӼԬŕå7ŦѨ;ΣϦǠƀԪˎΪӦԟı',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԥÖϽɓǑʇ9ɪӧ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'MУɝӨѼȻȱɴȤȸȅŒˍĊЉ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:210838.885112:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʶʑɑɲѭʂͺÓӸʊ˶ӼȒʹҫʕěѓÿ\x87ĩ İвԚю\x89юŁç',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʂьƢγӹ\x91αRƀËĲʍƓͶщł¢RɽҤҷίÔǷEhʋЬŇu',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȒѧɁĀĥқªŌØӃɇnɧ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϩŝӚȍ˖ǐ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1903348913544431674,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȸԇ˩ϤԡǕdű;\x89ɔʵˤƛª',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΆӰ¡ǩȍґǞŐϣMƉŉҏ=ȥԪϋȍɞӕȵѼ˄xŁҏүͱɻê',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -19628740221940257,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƟАӨí҅ψƢǜĞģСϹϬ·ƪĝѬΐ;ӻ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ό\x9fӸʟĖęɧóĵӼλƄĮϮȋԄĽǍĿǣԕǞЌһϲ¼ƩǏ£ƺ',
                            'message': 'Ќԡ˭EɓuÊƖqɼĸɍȋʀϓӔɡϓÍ˲ђ˚͵ȗMάӟɛƧԅ',
                            'arguments': [
                                        {
                                                        'name': 'ψ˔;AğӤïȶƎəүҥʗМͰάфŋƀ6ǰĆ»˽śѮӹӻɔ˂',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'cӼʣϩψÑрĳ0ɂèǭЊǀҋԧΊΊΗƱϳƭԈͰ˲ĬˡɽȈʟ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˞ϽǅΘԠvŴǏωĠdӦѿɫӺӛEʭŻˆѷęă҉ˆEэҫʏЕ',
                            'message': '҇ȶ\x93ѼӍʋGʰơ\x9cӖÆˏ҆οќÌĊ˒еɜĮ˹Ԥ=ԈΆ^νӒ',
                            'arguments': [
                                        {
                                                        'name': 'îƟ˟ˡ\x95ҚÞ˟ʵ\x8d¥õ§õƄĻä',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǥĊʹŏóKȦԙɐϴӴɵΰ˝ãΤƬ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҂YˌĉτɕTȟƍÕʈѳǎȑŦǿзåȐ\x96ǚϚǯȁ˺ƾ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x97ΤЄАѻǍRÑʇ×àηűԂҖǐĆÀǴяҟQǍӯѭѥŭ¸ЅŦ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ũт˼I',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԬІ[ӛѓѿǀĐʹϰ',
                            'message': 'ØР¤҉ӢþЁҼʲӑĖ\x8aưΪŞƕӽҕʫƦѴԜкВӧɞԚȟ\x8eè',
                            'arguments': [
                                        {
                                                        'name': 'ĄcƥӸҘȧтǸԎǙ¬ŊʡůƁӴƍƈԓâҪԫɒԢĊȃ³ęŷɻ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ūĔ\x8cĶ\u038dƑµѐǕʼΕŐτĢåԦұԎ˶ŤіʟĂѩͷǻнPœ҇',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѩ˸Ǻfn\u038dāѿÀˡ\\ʟѾԠɸċǃȇwŷćЇ8ŹԂ\x91Ѽƺţ¸',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6043910441654996678,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѮϡÝдęŏǖǙňȴͷϟȼĻōȜМт˧¿Ԃяԕҡ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'æʈǩʔØýΎӞNœԦĚӎƗςǫːʈɎѧſĢȆɣ˻ʥЩĪΟȶ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': "ò'Ĳԅоȯƺĵɫ8Ңԍƃċϝ¸ґԙΆ\x89êԤ\\Kɡн",
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:210840.381210:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǝѢħÓ΅\x93qɠҰӠYӾԍˢ΅ÏɐˍӇȗƮԬˑπ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÔχÕНèӃҮ\u03a2ǒәŔϐԏġѱӼ¿ƝĻӂČʲȓŃ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΣӟǸȒƛѷšŌԈ˦υπɚȒȩөĈŚЋĐӿǲǕʎsАɘ˯˴ʣ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'şҮɼкʌ¹ƭˊ[ǎǞǅİȱ\u0379ȹΰэʱƲӹȯȺŀ\x93DύǫЀӀ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҁ_ɃǩyǴұϝȷѡιдǽÊЃ^ŖѿҝĆѦΫĪѯА\x80¬ωŐѭ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɏ҉ǌžϪvɔƦɿӎĢðѵȽɲϏďɊ¡фƋ[ƻ˜ҤɠӛǍŐԉ',
                            'message': 'ÇӦĩΣňøα×ЯΝӭļůʮҒСНԘôȨŊķǾƓȤőӳѮ˘Ɇ',
                            'arguments': [
                                        {
                                                        'name': 'ʲӔғωсǪΘʦɭңʿëƣĪƼϓȯǵȜěѹÁʢпŖӆ¥ΕɌǮ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѧȌрˁ\x82ɤ§ΆʦҊ˖Ҍˉ7ϫͿҷǵĢҮRϝҫҵ\x94!ьɲ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8075625554032341475,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɧȆ˫ˆòƽѭ;ѭΜȠиŋȴƁĆΝ˙\x80\x81ѝțӅÔǛлʼǖʤ˸',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҚǔÔŌɭӱʭҴ\x7fӒИȏɩǶχ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5898805755373456237,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϰ¢ȧϬƎīÜņѲŹʦǒţ\x89ōҍƧѴԧǻL"\x9d҅Ӭ҉ĸŨû/',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ćͶżö³3ȨȳɓϾÎёçӏԠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:210841.162886:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʫɑŊĠīɆƜÒĎßƮɼӕ5ӗ˴йә<Ǣԃ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŗӗ\x90ɚҴǤ\x87ʻԘŠϋӍϥŏýǝɘͲҗҰǕΡìѬˉӎƀӛЏĥ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҡź\x83ЗІˏӃ²ӝEвїЃӓˑМʫҀƎцѺXйΨкċї˱ǻÚ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:210841.361725:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǃ¨ǮŠѺăáe³ˉӥҊҲ®\u0381ɣȜҰť˟ҏʻЕŐŧ˵',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:210841.428216:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϕБĳʅӃІЪЯgԄq˳Ӄ¤ʃҜӌǂŻ Γȃ˟ͻńGʙŐ\x88ľ',
                            'message': '˨ҎѯɆȈ\u038bˡ¤æӝȁɔĖǎѩƠυɺ\x9bȵϝļÁϗ\x92ʰ¿Ԁƶǆ',
                            'arguments': [
                                        {
                                                        'name': '9Ӹԫ҈҄Ġʎæşū¿ԠĶҳӽˌг˞ɝɤîYʈƛƮ¨ʍʡ";',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɤϬʨсƫÞǢh9ɉHʿ čqɯÖԤӔ_ϿjʚΎƄǟЂěΤι',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:210841.628886:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȾϑИӟAэĝѶǯǻ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҨƜΨԗϠ2×ȺǣԋɼԮΩȽҬέԁ¹ȿĲϲͰϪƈџ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:210841.763993:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '{ĎȱϛИɷȎҀЪŉþѱ;\x97ƨ˧!ω¼åôдӶÎȮĥѣ0ìɈ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '&ŞчVεė҄ʷĺȭǘˮĶӲĞZΛӞIťȏЬȻɜiųͽϯ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 40643.12604980319,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ďϡΚҷŁĕԜҕŵˇ=ͲåƱŠұ\x91ѽƝE\u0382ˁ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'зρъӍ\x8a+ӎɹƹҴǮŻ(ӳ;ʓȀӮȢȽ˯иƀ˝Ԅҏ˷Ҝ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -69946.59858780372,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ύɢΣԣѵōǑϏȃrʨʒĒȲϤǷ˖ҮтƠÄϳȱĽƞȠƣʘʌ´',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ПđЄˑǿƳυʐɷơÍԟƤǃͱ˄ԣͶƖӬÄƷНƱӭŭϡɡʹȠ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 700431.3762663386,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'чһ˂ˎеʢÓӜӮєǱɄɎΑϡņɘǿЍ҈ӟӤӦŢєӰȶѸжX',
                            'message': 'ѶÞЬ£ΧҼӾ\x83ƊǑΨ˯ȼˆϻҿԤӶȏŦϸŢԋƣόѤƱƻpķ',
                            'arguments': [
                                        {
                                                        'name': 'ЎҭϺůȜŅū;ŸҨǡɤȕȹìѣԇԠ˸ǏʱɡˮВʍ˯Ѻ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɨĪ˶ǍƤӿǾӀǳðϼѵыәҵĜɪˇҬƑɔ\x8cҾ˲ˬě',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŶӲҜџьÚǀѷÍʠҙ\x8fΡȼҜǧҢBԛˎĴ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŌҥϗŐΠҋŕҢϷq\x8eƞDÃʽŶԩƣϩoʍԃˎĞFʇô5ʐɈ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӎɹѷ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŀύËʁ*Ȏơ˪ȻǌɰҔѭĭҷӝӌåíѱ˚ϚэRßҎəƩƕ_',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӖΝԉ\xa0ѬQӃÓѸҜdˎ#ʍêżϰȉĦŔԦ,Ɲ[÷ʖ˨ϭҫ»',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:210842.603780:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҟϠĶúҘǷъ$ßƁѫɓБ\x91³eӝšʌǪЛǉ\x82ŝр˂ÉɹĶʚ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǽ\xadƉ˙Όӫ˜Ӝȧɢκ\x9f˙˧ȐȲůĹǇŏ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԗΧДļ\x90Ǘώҳɪɕ·ƖͳԋŏԣĝӧƉ\x81ȍŶƃȣȵȣΞĩȾњ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ʌˇ\x90Θ\x87',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ž=\x8fȿѥϵӨǨҽӎɪĞӯӺėԮѠȆŕŪȁʡʾŝȾǳǒǏʚʑ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2747862748440843748,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʷʇήȢŇKǈȴ˄\x91ʃĈχNŖȘàѾƸѤ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʃβǨǳɐ~ԝӷĞ¢ĸϒ«ȥϜБӯ',
                            'message': 'Ȁ˹ҟQɻжҎЧή©ȠʍӺсʥϽӑKΘΧÃήȪ˦ØЕ\x8fƩ¬Ĝ',
                            'arguments': [
                                        {
                                                        'name': 'ŢˢƿœӅùΒʴӉӗӔǵʓȉ\x92Ґ/ɖƗϷȝĹǽȖİmŌГ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '΄мРɓƇ˾\x96ʥԕY*\u0378ȨÛ\xa0Ëʭ`ıʬŲĨѧƥȕǄшӱ҈ň',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȶŒɒǞǱǱǤǂƴȑД\u0382\x9c\u0378ʍlћȆìʣȨ˸ʼөũуʠ·ɮʹ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƥԬ\x83Ţϸ\x8b;ӮɕFԫøϙʋŴϪ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˌжɂҵӠ\u0378ĜˢȮҨŔ®\\ӐƻҹʀɿõȢҌɘWϊΈǯϋƄƨȴ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5880368569716177093,
                                                                        },
                                                    },
                                        {
                                                        'name': '¿ȑџɖýơԬ÷Ї\u0382ƫUʔЧԈӠĬ·ά\x88Ï¶Ɏưψs\x8a%',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǻɿиџӀԛZ9Ѹͻχ=ɰŊʜøiɸʔ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:210843.544331:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѝЃϰÔȎ§ҊpѶ-',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ûŤƀǈӊϱҨÓкѰΘԔÇ(ιƎζԄӬϖԅɂʪ\u0382ɣѾВƓƞÓ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:210843.697041:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'РʵǀΥҞѦҿ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:210843.761931:+0000',
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

            'name': 'ïΔƴ',

            'error': {
                'identifier': 'ɭƗoʮѭ',
                'categories': [
                    'configuration',
                ],
                'messages': [
                    {
                            'catalog': 'ӥӼ',
                            'message': 'Ϛ',
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
            'event_id': 'ɿԆԭöԬ:ҀѷÓƓέĮɧӋDƹԖƕҚбő˾ǱʶϘˋӁƀѢ\u03a2',
            'target_id': 'yȿôÚʐѼκͶLƺӴɒĲȚČʲрĚŨЇʎΩ˚ұјɱʄԪ\x8bɍ',
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
                    'event_id': 'ʟȽ\x86шϦwˠ9ΠƝϜӺԝҠԬӖĉǧŻ\x88ƽôǡØĂ\x94Οўũг',
                    'target_id': '˫ӛѡҀƍ\x88фpƳ°˙ϐǷǓȲ˔RȼǓТqȐҊ0ĠNԖ«ΚΥ',
                },
                {
                    'event_id': 'ԮƜɦɭ\u0380˫˾\x8dҤϳơřЋƠέJŶĴ˃˼ƨͳӆƇɑȽȧpȋО',
                    'target_id': '¶ȂŮĴА˘ԮҼѥˊ\x91ԫŘHɫϠέ|Ώ3«Ͱʣřʰɿ´϶҂҅',
                },
                {
                    'event_id': 'ȡZҍɔсm˗ˊƕ×Βýˑ2˻ŖǗӲǗԕϮeϱª˹Ω&ƚ¶ќ',
                    'target_id': '\u0379K1¬=\xa0ǯɒщӨҬŅӐӻŻǝԅǮáʴ»ҜƦȄcбԜрMĢ',
                },
                {
                    'event_id': 'ǫͱӖ͵йĆ˵ŌѰʍȓѪϞφʯΉҹŃŸ˴с\x83;ÔɏǨʣγыЪ',
                    'target_id': 'LʾóәXԂ˵Ӏԭ·ƨɌʢзƨˣϴΘʷƳԑˍʓʞ>ɊϲԆ˶҅',
                },
                {
                    'event_id': 'ЦԨǙȤѶoȕԒЛԅÁTѥʻȂ\u0383ίȄwʱȸ\x9cŲƺϻ˭ɎzҕƜ',
                    'target_id': '«żˏҞˢøӭƋɊȓ',
                },
                {
                    'event_id': 'ǈüvʳȩÀ\x88\xadϥӡӰąԗgƃ҃ɑ©˲Ԏ˙ѐcŻʛĮƳϣԠʭ',
                    'target_id': 'ÝȿϗΟěĺŊЬŹԒʃοŻē҉ТȘđƬϰǴԇΕƲMԕЛїǌҥ',
                },
                {
                    'event_id': "ԄӕѪϋǢӷȱʹǞˆѥ\x96ǘАŁƓ\x9a˵ҖŘ¦ѡӗʙӐˠԕŀ'Ҽ",
                    'target_id': 'эt˅ΡĕĢӳƫӡӫѓΪԌӨµVҝǏěʂ·ÖƐʴԨǆ˔Ĉˍý',
                },
                {
                    'event_id': 'ӚǒƭҞѥȍɿΡɢ˳ȍƼXʻ˸ɹφƿқƌnÆ\x9aх\x92QøΉдϾ',
                    'target_id': 'Ŷ/KǺϮ\u0382˄;ńӵʃКτ˫đǡϙԣԫ˶ǲӏӻƵЏɫϓǲ΄Ϗ',
                },
                {
                    'event_id': '҆hΚşξїϨ϶ńεȂǣ˳ɞʘuƢ\x90º2ԜfˀZԛ2qӣ\x9bͿ',
                    'target_id': 'ɋЁ\x84ƜкüʋЊјůǶŶĝƻTЮŞ½ǿϮћǖʪ*ÇҖӗҳβԈ',
                },
                {
                    'event_id': 'ʸʕΉҵɔGǄɬŢV¾ιäơΙɢԉ¯\x87ǱƠʃƸҁĘĭʉиȮԜ',
                    'target_id': 'ӟLмҬĝ\x89ЅƕǫɊƷЛFȿҦƱьƻȦ·ƎŊˊӤԇÆҍˇ͵ΐ',
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
                    'event_id': 'ǻʂЇʤǅŴ˺Ƀ\\ƤŹҳɰƟĥǆԖìǹƬ\x95þǫțȉȊhʢčӣ',
                    'target_id': 'Ϋ\x9fϢιηĸĸŊȌCfʳӖƓéŬ\x81҉ɡxҸЂvԨöąΜQўϝ',
                },
                {
                    'event_id': 'ſƗɉȊĬŚ¦ƀ\x9fǌƁқҩӽσʠÖĬϐȇҝӚŭ\x83ԀξӗќȜҋ',
                    'target_id': 'є÷ʮʓϷƟ´сYťɧ[РǩÒȋ\x8eyӦϪʷ˪\x826ҙǈªАҡî',
                },
                {
                    'event_id': 'ĲɨŝƱл)ȗȒɛfpaҾWLӑҬȜɃĹʫē\u0378ǰ\x82ёĞѡθ˨',
                    'target_id': '˚δ8ɩĘĴʔ˅ʽͲĝȫªҰ\\ή҅®ΠĞrӎҠʯŜҔjїЊЛ',
                },
                {
                    'event_id': 'ϕ?#ЩԌĄ(˓½ĤƊЍǄФĹҖĜʘ˙ϷİџӰ;ʩȊԅӳÞǷ',
                    'target_id': 'ҀжȽЫ\x90.ƖĝΚʹҜ:¿\u0379,ƙΘ¯ĈҜǤ«іϖǫӺȀˏªS',
                },
                {
                    'event_id': 'ʬѳЄȷҊĜӶŜǃ~ӍƠОҍǌϻϖÈ\x94ΥĕїθҬÇĦ҉ΧɗӦ',
                    'target_id': '˃ŗԏ˟ŌϛӄÚġ\x8aϺMАŞŧ\x86ȔƄʜŧƯԫühҷ˱ʼȶƽǇ',
                },
                {
                    'event_id': 'ȫǏŃ«ΰñңӏԜϯΰɪǤ\\Ų{ĈȖ˃вӷͰҘѼԋˣƇȌƔf',
                    'target_id': 'ѵąҫ»ʱʬпɼҁМԈΩύƐєʌƢѺ\x83úȁʌQʐˊԥȷ±Оː',
                },
                {
                    'event_id': 'ѤϬŠŹǟ9đɣɐ@²ΆӳʏČƺȑ[GǷǁϵŧΞȘƬόȏĕҥ',
                    'target_id': 'Ǯ#˫Ӄω϶œOϼ¡˂ԜîԑiɦɥÂƐȿɦӐўƟЊҖηγȹǾ',
                },
                {
                    'event_id': 'ϵңȩʱɲɶʭǊĳҪĶÃѧ\u03a2ƶűԕҒ˃ӛӖãɩϬɺĐϛҹ҄Ǽ',
                    'target_id': 'ƫϤ˳Ұ\x8cǠ\x8eѮНӧωˤ¬ėƘ˖ʺ҉κϯɓҋӌπҼˡÖтӢɏ',
                },
                {
                    'event_id': 'ĵɰͱŽŞϘʍǭԪƎºǜ\x8f\x8aǘĖȮІèŪǑϽкǣӍȍЫƎʧѵ',
                    'target_id': 'ҋgɭҳǈфǦʤɲ˃ѤцӇ$ʀˡ\x8aƵʟԐƌµĀǧԢÃʿяǵΰ',
                },
                {
                    'event_id': '>ʈԀˉǱ³ǃ˂ŉΕρϱüҜĨӺēµaǜǎÃƾΑσϣҚ΅Ⱥв',
                    'target_id': 'ÐƐʅЊǍ˥ɉϋӧɪɯɂʍɯʓȇǼ\x8c\x86ɮ¹\x83ҀȔҹ$½ġȬв',
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
