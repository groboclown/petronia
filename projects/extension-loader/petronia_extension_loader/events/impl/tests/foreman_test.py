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
                'ĉ˶енǢѵȜģЗèӘ҂κ˽øǺƧrϞ˦ĸȋĺ\x90Ę˒ʺЂН´',
                'ņԗɧ¤ЊП#΄éºɉϓԃ¸ǈǕƋ\x9eΗˑƩϢˀİӰϒîŪπΙ',
                'ĎŹҋìƯ÷ɥɔԑΝӦèȋеʪѭμ#Ԙ\x9aƟԠӂeˊ˅ӈҀӤɾ',
                'ĂԍƦӥÙʢöİǊͷ\x9bįԪŜԨ˟ѦϕҖȫφӤǧҺϫ\x9cϩĹŮ\x86',
                'ǮҊǗƢ˒0҆\x8dũáњŬ½ïζÆȂř˻ŰԕƭˈѽɰǶԥxŗë',
                'ÍˁǿɎ\x99ÄЌeǞɬǛUρǫ\x91ίȭгɡϟѤвǏƝ©ɕҥȊ"ƛ',
                '\x82³ȁүþIMЖǆ3ȀƎ\x89ΊʟƼӴǾ«ŢΧɲАÓ\u0383ΪөΆ9Ȯ',
                'ǣΊɠўѤάªϢϬѥʵ<uɛƪѿʡȃȨ˂ȻӪЖоǹϫƅ\x96ЏŬ',
                'eǕ\u03a2ͽˬB¦ЧӳΡȩɛΐӞ\x8cӁȋӴʾȕǈĳƎѰ%òӉϬĲˑ',
                '÷ЅOĊɔĎЄǅΛУĮΰĭȯͱ\x9aPĕ˩ĺȑώNѐͻϔǠɃ/Ϙ',
            ],
            'source_id_prefixes': [
                'ŔΐʷΛĺʙÐЏƷѝ\x86ҢǭϹʋԢȾ\x92ӖųͶűќ«ʛЁȔӘ§\x96',
                'Ν˅Hk>οÛӬԞƯŸˋ*ϫͰyѺȁΗȒ|ǽƛʧѭǖ\x96Ⱥ¦η',
                ';ŭͺǲņĽɸΤȻӋǗoϬȁˣɐέ¯ԦƷƄ¹ͳ2ɹĢдǫɬΣ',
                '®уÓЅОϹÜ˒ӘԘϗņτȮŶяϕЮ\u038bòҚɱńŵУЁͱÁēȀ',
                'ÌĉŽʼĊȋʒɧŢɨцӊԒƍ\u038dź¡νǺ˱ԨđŵԢ°ßЪы¤Ʀ',
                '«ÖÃѷϐň+Ó0LԋΒM[ʴÙӀѾǛҐïĦȠĎΐԫʥÚÿƜ',
                'ĴΥ\u038bÊʸΖĤòϏѩǴƱϞĊңŭ\xa0ȿǻ˴ŦыХѴĿÝѯǿşњ',
                'ͱǅg\u038d҇ΧǰȳζĹ¦1ϣӅuɑʑЈҏџǚ\x87äǧ˚ѐψΛǶì',
                'ҋϡϳ϶ѾVɆǄǮӄӼÅƹɍʺďˀȵҥuӻǾ\x95С˜»ӬʫʅϾ',
                'ɇ®σɷǟȡqԡыȬҥ\x8bƫ\x88ǚӡȤѯȉU\x84ȅҲ\x9cҔʁƢȷcν',
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
            'action': "ʬ\x96ВȢŒʞʱhԗÌˈƻѽɈҷąϩɰ\x87ŘЙ'ђϜчӁǩĹȬȗ",
            'resources': [
                'ǗǆÜʥϴҭʔ,ϬԣıńΒǱφƯƥǨςƷмŧəʢҀϻӍF[қ',
                'Ļ˲ԁȕĔÉřbƨɊìЯ\x89˒´\u03a2qΑ½Ғ¥ΫТʢźŖ¼Ϗɬ>',
                'gýύѦҒуЏĽĐәɯƗшҮΉ}Ѫƙ˚Öƚ¸˯ª\x8fʻЉŚПƒ',
                'ЎǺūðǁĜZҮʝĮɛÎѣЩӓã˲ǇφĨѓӂΓ\x83³Žêƕκ¼',
                'ƑϻȌ´ΟԁеʭҮΐƛЕΌƝ\x80Ο˾˙ĹҞғ0Ŭ\x88ģʊɹѵS˘',
                'ĶˍҔɞӽҐĺΕƵƉѮñˍǆʑǵѕҲˬùΏ¦jˏюĜҔҧνҘ',
                '¢҅К˩ЄˤΑǧҔҁʾŒҷˤӒΰ\x9d˒ǘӌkӛϣØŁǌʆ\u0382ӠԊ',
                'ɹ͵ӝӁЪƦȖѤʱ\x9aµhӡԏˈȇѫķʟѓ\x9fϺƹƗοˮɋƕ˽Ų',
                'ƾ˻ԮʬȗƝőѤōΝɻͻɰȗĆŇÙϳӢнӛˤĽŧÕĴψρwӞ',
                'ƆͿïφƴ\u03a2ˇϤņɍÜɑvǖǺ¸Ǒǰ҇ӉļƽƑʁ\x99ʋÙɵČƚ',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'ȉ',

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
            'name': 'җǲĨPОQȥБ#ђҵƨӐǱ\x95ѡΡӆH˷ǮԔӺŁԂǛƢԨ˙ε',
            'version': [
                -2384223443813452080,
                -3981322903672260780,
                -1612191489540910412,
            ],
            'location': [
                '˾)ĨƭԠǳXӦŲʨƗWϵƏɟɨǟɕȣЁ҆ÀɟťʫПŵΕūп',
                'ϥʐƭаƝʴʾfЭη\x80ѾÙ΄Ԩ҂ǐР\x83Ҏǵɠ·ɉȭνϯˠԊɯ',
                '˹ӯϿѳȈΰąǊЎʒɴşҞňɒѨɹДŗ˵Ŵü\x9cʈЕϪǘÕ˒¦',
                'ʯүėʁȶǮƀʝǌ\u0382νġ˓Ԇ0ϐ\u0382Ć˗ѳԮӀʟīΕԄ˯ƝĄx',
                'ЅͼʮƝ\x94ωϮȬȎԣơԑɁϜĤӐˍĻїϞlͱΛɶҮңū\x82΄Ҧ',
                'Д˶μϗĳʩҴɒ¹ȴŵɛ+чïµˮȼɚɪáΖЁҌжg˳ӡåǆ',
                'ώєԘŒšɊɫ˴αǟȞɃɒč\x95ʑŲĖÿǊȌү\x8cӘɶʍȽåΊZ',
                '˄ԙ\x89Ľԫ˗õ\u0383ɈȫѯӺQĦҘӈЌԧˏӾʋəѽǉ^λÒɇԬЗ',
                'Ď\x7fχʎ˸ǹЩÒлʛǺлњȽԫé¡Ā±ǟd˱ϹÊĂȕӪ÷țɧ',
                '\x91ǸȎԁ˄3ԭσѹğřƫĔȜłщОӽŉԒћĥӍƘŌ1тЖѠK',
            ],
            'runtime': "ӯӔĭӾßŘʹľɾыˈ!ұİдѤ˺\x96хқȫƴӞ'ԌӚÖēӍМ",
            'send_access': {
                'event_ids': [
                    'ǞҹɍĄDǺĥɾĆĊƲЀϟŢʠԅәϡËƜԐϨ˟Ӌ3ҔƋȘ˭þ',
                    'ɱ°ҫŅӣSΨʒΡƆңȘĒ',
                    'ɷØıŇԘˌÁҶjS"ǟȢʗCˤŶʻɐπλǃϜёȗ³ԍO\x9bȱ',
                    'ˋЯʒÉʛϷϼΈ(ĸοԕѯҗ±ɜсȌęӡвҪһǩʞ`бƭuҚ',
                    'ǪԘ#ӃɴƻΪ˷ҡʜΉϐ˛ǱOƿȺϻѤӠźơɯɹǸ-ЭҕӋʞ',
                    'ǬGӃƭѕƿːĝȗ»ĶɥVοІ˅ƚk<«ȷśҾѶŜƈCӃҵɊ',
                    'Ԋ¢¸H\x91ϜƱKÄʟpͲѫłЀŉχ˫ϊ`ԝÚũ҂ҕʊéʸîϋ',
                    'ԮЪˈǮİɑÅŴ˨ʝķѤÍϱцԮĩӛǂØʻЇϯμƄʹƿɮĉʷ',
                    'şӶǮǃƄțʴĠȂӻŏƽԧɖȿѮйӐɘғʩŹѢ0\u0378ȹWƆҖΘ',
                    '\x81˺ŊʌĄɎé"Р\x8fʩȓȰʭɰӬʚˉҤǓɀϦɅŁBЅśűәӦ',
                ],
                'source_id_prefixes': [
                    'Ȕ\x97ӕŷʜӉ\u0383KЌϗ˱ӣҔ˄ұѐҀЖˤʴǉƵυѶәʂɽԫaϱ',
                    'ʪʩʀŲƼXƣ˅ѷǮџ¦ʩŷȭ¹3ьʅυȬƧίĪQʽʦǠӎӮ',
                    '΄ИАˑL˦ʛЛԪɄńć\x7fʚƚǵƬˁùʙǺʌǛϢ˚ФŕÞưϜ',
                    'ιňɕȵї\x88þȮѨҸԔӢԩ\u0378ɖŦВҽȪγĉўyϞǵǓƸ˃Ĩϖ',
                    'Ѩ»Pɟ\u038dȨǓʄӊĚΔėѮ¤ǿќɎėëʂԘЂÙʙʝ˅ʛљҹӺ',
                    'ͿǂҐ\x80Ғ\x8aҡԈҒѱςϒѩːƑĄʸʲƔϾŷȏöпƆğѬӎ$ĺ',
                    "͵Ăδʾɍȓʊх'ʿoгЋmѮΏȬȈʯԁνȋǏÙŘUǂԚ¥λ",
                    'ЬŮRξѵӀфŀΗһҡύ³ХŘɿ0ŭŎ΅ſǥҟϯФʾӌˬŏё',
                    'ŤϫвƇ1\x7f`ǉüѶɸң\x93ϔă˟У\x81ԅӗåԀíƃɴʶɹƐʬΆ',
                    'ªȶÄˬųƂƦҹͷѯ#ԑͿ\x87jѹˣƷƊĚǩȂΝәңΌϦίƠü',
                ],
            },
            'configuration': 'nӃӟГӫŠϙɵйòǅķũ¬ɨϖЂʅӖȵъ˸\x9bČRЩԒеlƞ',
            'permissions': [
                {
                    'action': 'Ѿέ¬˟\x81ȐĕɳɘŊƩʢхʏ˞ĶưŚӭ˨ϑĀɒ÷ĵuźψȹÑ',
                    'resources': [
                            'ĴƼ\u0378ŵ˦îűΑɥԖӧ»Ɣρɻԟɂȭ΄Ȳ˨Ћġϫˡºą˃ԙƕ',
                            '˳ĐȧǪҬq»Ļ\x98ϒżωĊҨ@ϤmҨȡȐϕǧÖΐʘԋӐĂ΄k',
                            'üЬːǥҡɔ6?ЌΓƉƆƚВ¾˷Ŝˡȩͷ˙ʡӀɹϧĴİˑѾϭ',
                            'Ν`ʿӝĤōyŁӂҔuűҷӢӡȹ\x87˂}ƧΊ΄ԈƃǧʷǵνĥЫ',
                            'ęʪĐˇӕʍǄǇӟȵӞҘĸɑЋҠԛǋ/ШϧӛЃԔßȪÚOγ\u038d',
                            '˭şǁóÏð\x8eȍҕÉ\x81҆ЫƯњϤ\x97ǰɖӤȒπСлő\x88ԎΗˤ˼',
                            'ϺԪɤƑ\x94Ɉϫˌ\x94˳ƂǐʠМʖͻЩ\x95ǖUϖӅśʻǷ¹¦²Ԟ\x8b',
                            'ʷԈ+PǱЖȿω\x9cӕΘйúцώѨˁ\x9aĹˍΰϝ^ӗ«šŬɶϔ\x99',
                            'ǈʍɚǮѰЫçķƲĦĶǗͰԋҋëϴҹQƁΦϊǫ˒˓қöŴӣ\x85',
                            'éˢΘ$ȃͽȇһ˚śĳˌŀëļƦԢʢëĈƍŢ˄ǔØԚɈϕȕŅ',
                        ],
                },
                {
                    'action': 'Ȓ\x90ȒʊʴԨ˲ȊòʌåԉƋE˱Ѷnм\x9cʭǎē˱ŐǺȹˁLćӑ',
                    'resources': [
                            't\x99ϖ˲Ǻ²ӼϚұω˷\\џįŖɄȗУʊʂԋƸѷƋƘτŋхōɱ',
                            '\u0379ӉˑДǅ\x89ҩԡBŃЙӚ˟ӍãϟħӖәÙЬχƹѐ\x83л¤ȶčр',
                            'ԨЖˢӳ˸ӧˆʠɳŝĭɣF˟ЌΞӫЙʦÁȞ:\u0381εђɯÈP\x8b˪',
                            'ӨҺ"ɫŧʳưϘғøэÃϤˤϹѱĖʠЏѬȚѱєѨǍȖşȱωҢ',
                            'ҴЊū¦˭ɞFƶǍѿ˰Ҥǚќїʂυеѭxμ\x83\x80ҒΕäɢ\x89ZÃ',
                            'ЖƗѵιҧĕƸϔ+ҼҸO˫ʡҋȒŲ\x8bжћͷ˛џϺыƭÂĤ˻)',
                            'ӦJ4ǮƃħѸįąΩ*ȏѱӺȹÿˏɵˆɂƂЭџ˓ƍǳĢώÒĝ',
                            'ΏOĬƕЧ8ѡЊѿӖdԂÓŨɰөϿԝ·ŘíΚǛçЌȤ҅ӗϾˇ',
                            '϶ԜɑϣӷГıώƙϲɘÇѪǧğѪΟ;ϻɣбԮτʖēќќЃȃђ',
                            'ΌжбĚԄοˠъӆeǖƙӹҖҽÓɩëǭίƞ˽Î\u0382ƼƞĽˤƍƎ',
                        ],
                },
                {
                    'action': 'шʇIňҴΊʎ¿ÉËԎԎtәάʉԐˠjȿųЂҝԡɰӪӨβԍ',
                    'resources': [
                            'Ў˱ƾОŔ˪ƾΨŃʤŹƗϦьԄ®;ӑŤǆʤɫʫˏÝЗԞ\x9eˎˎ',
                            'ǎŷ§ƍŷ',
                            'эŪ.СΔМțȼҌрǓ§IǲѰˏҦΦPɸľӄkϔǦдԉɞӻĞ',
                            'ĻǤF҆Ŵɐʩ¬',
                            'ͻ\x9fфЂϗΦǙϯԧϖӺϋį΄ȕɰƢkϕѲˈ)Ɲů¡кԫƜҡɳ',
                            'ƾǍƆНʬͼĞÖєϏɚҳśҳԙ²ǙɢʀϑӇĂҿЇǚ\x80źɘͽԜ',
                            'ʮэĴŶĞȣƁɪǪȪпͷѨюԌӥyϟ×ŹȥЇԡҲǔҍчųό¨',
                            '+ƍrRʔHЙ˙ͺɈƐWЃѐϗȮͻTчŕψȂƝ˂ɞёϞҥΐƍ',
                            '>ΚϫnǺӬɕóԄɣʠƸѲs¾ɗŅȬϸ1ĈƩΒДѥƴŸ϶øԟ',
                            'ˢǫНӔxѳʵ\x89ģɉЄΧϙδÏ\x93ɏłƜǞǐȻȰИʬƉŨʻƭƹ',
                        ],
                },
                {
                    'action': 'ʏÕЦ3\x9dªʌǐӈɄ҆оϾȨóюԘǴĳÇϽćwΤɟԥƐΒԇ¬',
                    'resources': [
                            '˕įǾ)ɁσÜԘFҤǙӃơBԁÜϰѲɃʸӡĔΚØЀŧȉŚ¨Ѓ',
                            'ɛʢŠҚҳϣӼɴʬǿВʣś«ҼχƽȔǒѨśΥ»ŐʠϱƗˏӀ˯',
                            'ͲǙƪȎЅěĆϲӊӫ¡ȀǏʲʌӾƞƓмȜ\x84рťˑԝӌƬ|ΐǵ',
                            'ҔãZԙȑШЯŰʣЬ^ǌąΣȝɭžǣǅҫєƽ;ʰшˣмӬҸΑ',
                            'ǜǉƆԁȎʖЋѣĒˠҕɩōı˃ǥρϊ˗ȳ˹ңƎ!ԎÂ©ҕυҠ',
                            'ƔǥӑC¸кϘӘҥźˌϷźŕʐʎαǺӺŨƖϲuтöмƞɈԏӕ',
                            'ˆìÿaԙõҳѻP&ͰŇþΪԥԙӄĢϑОɵ҂˴ɀRҋ©бЊԜ',
                            'IǾ҃;ɨ\x8aӠНŐøuŉȒΖҀНʺё-˒ҒөƭϑʓʻϋѝĤ˃',
                            'ѥŖʃҌӓҌʎÂ1Ǟƽ³ħíѤɐ\x84вŜʫÛΨ˛˴Ӝ;ͻԀƆϵ',
                            'ķvȜϡοÂǆȪѷ`\x9eʀ\x81ŻȨϔ®þ´ȜȬӿИÏ0˶ĩHǫɿ',
                        ],
                },
                {
                    'action': 'ɘҺӛʜʅ@Ȩҙѫ\u038bҟПѝшǚÄʎ§ӊеԛӭ˯ЭC˴\x80ȾĚΡ',
                    'resources': [
                            'ϧɾϣS˕ƶYÝĳĕŇŁΗћʠŻΦʍ˓ĘˣǠÁ˵үѻӘėӸї',
                            'ϢȄʁιЗĶūѾƒҽМѵŜƩϫĈѲ¤ʛȭƳǱԊ˰ƉȻϢƁƭƯ',
                            'ȷƖ1JģïǷʁԐѓ˧¬˄ʔßΊЭȬЄÛϭǔ΅ǓˡƓĿʡұԠ',
                            "ǍҊʆΕõБŲӕƽ½Ř[ҙˤɴǌԍÍѳŀ»ΑɺÌĞ'ңǹQ^",
                            'ĺʘԤ¡ԬЫ£fǽ˼ʒ Иɠʙȇ0Ɔʶлɷ¤ĹWǦĬƛUԭĚ',
                            'ҡɼɐ1ҝûӆƣˇҁĜѵϊ¥9ǩƮ±ɰş\x98\u0383\x98Ôi\x85\x85ʴЪú',
                            'őʭȑϔĘśŽ=àΎ˪Öӷ¤ŖΐȰςɄʆŗ«\u0379ϸΒҸыεÚԓ',
                            'ŵǼ\\Ïû+HʿʎãҥćСƵĐЫȌ½γÉȏőã˔ҒɦǢȹyҠ',
                            '˄ѡϨɎʤï\x84ˮӿHŶɞ»ЛϣҎЗшȴӡ˨ӿкԫǰŗWԢųĪ',
                            'Ä˸ӣưԟԁ~θɔsѸˢѧŰԀ\x86ǷϮʤˏ˷ʯÜŲʁ҇ӷɫɬї',
                        ],
                },
                {
                    'action': 'ҼƃҹΏԇѹjӚԦȬȀī\u0380\xadÒΨȴȧ˫˭ÍɨΡƬіΠ\xadĲыŗ',
                    'resources': [
                            'ǷTńȇ˘ʹÝԏ©ŻҳÜŹʐƨɘΥπƀҷˡЈʉʫШǁʦѭұԬ',
                            'ƍӇӕӍE˔ĿųҽѡЙҊԔʰːεԔǋƧ·ʚǴÓǥʉȄƾ˛Ԭе',
                            'ʯƒĆнαӋТ\u0382ηϥºЊ\u0378´ϼŮ<˄ȩʷę˩϶VχɿʼѤ\x98\x9f',
                            'Ͽ£ϟӐ÷ņӰЭΣȴǍŜ\x8cчʶшүГ0ĐɣуϊЎǭʛɧʸǚğ',
                            'ԬξȏőИϤѠưɶҝ˚ԀʐӘɐƞ҃ǩȐϖҌЗʹыɦĿWӂоɛ',
                            'ƁϏʐϨЄ˧ȜCҥƃ\x8cƙÚxǁωƇͰԀњρŊɛ˝AŜĝ˫ƙ\x99',
                            'ӳʱʎɒɟnÐΌ°ѨӜFƣÛżˉƤªѝƾÙΎ)ģƹ+ēǓяҭ',
                            'Ő\x9b\x94\x9dĊˇҠɥЦƓŒƧэʏϿĻǣҺЌʑŬɳΪ:Ѽ]АЋԀė',
                            '϶ĩӯпËƱЩ½ȀôȿŐӼłȈ¾ї(+Ƙh4ǭ\u0383ǺѰβƫŬɲ',
                            'ɓѫѕǰҾ˲˄ϑҙɠΓRɅ϶˳]ȚnŬļƒΗЯ°˥͵Ω¶Ɗʖ',
                        ],
                },
                {
                    'action': '\u0379ҀȠ¾ƒшТěȪԛĒėӼǔЇнËΊ½ȵǝĎ\u038bȡ¬ǰɇҡЗԄ',
                    'resources': [
                            'Ƨ_ȣ\x8cĨFȦ˜ϋŜǀĺƄŨŰ˶)ϋўǏϧÜȉíˎʧ˥IǢԩ',
                            'ԤʋοɕϟπҰŢŢ¯έǅʭčġѯϬёʩ0\x9c\x83ɩ\x8aѽǥԒƞÕԙ',
                            'ȪʆǊĺȯ҄ƷǙǜĽРȳĊνԟ\u03a2Ù2\x8eνҲђƟҗƸôÖȌϿ¥',
                            'ƕӺϑƍċҍĂНȉǴʫ˝ĭжʒű\u0379\x97гÔԭˋб\u0381˚ͼѹJϓY',
                            'ѱϴâ+ΛρƹʩɬNŝ\xa0˨҆ˬtƖǵĀϑʉћÓɯѩ¯ƵҿÏČ',
                            'ƺʒʓɔɧƿ\u038bнɣȦӧǕǲξл\x8dϋҿnҍIˋ0Ύ˵ȹȅΟɢϙ',
                            'АïӰßkɳӬǟƃĮƿƂƫƢƓȉɟˣ)ҐѯϥŻ±K0ħ|#V',
                            'ъи˒ɐőĘŶȒͲѶҞ·ʘŜ˞ĊȅӃˑɪӴҌǑ˝ηӣư\u0379ς ',
                            'ʁӐ˵ϐȴԗā,ȾʭϋǠʃˀЂ϶ƈȬћò\u038d^ȚƤŸԎ',
                            'αҽοƜčíʜӎʥɔǾƪ\u038dϓʱŪԬȿʾȳ˪ǭ΄Ť¥мϚԓҔʾ',
                        ],
                },
                {
                    'action': 'ƟˠМ˸ӄ\x9eʄǤϸΦҧǕЎ\x80әȅǚӻėȴҮØҷ',
                    'resources': [
                            'ėïƟΉǹϙЬɩH˥дӂɮǚhϋȺҟӫҡ±Ο͵ūЎԞǁ\x80ѾȾ',
                            'bǇʇ˄ԖȾnԋАΜȩͿřіӥƞɨ8ǵīΒŚїƱтhɀˈĩΓ',
                            '͵ӱԥʭʄɊ»ΫƮɁȌō6ńŢ\x8dÊʎãʗ\x95ŐԅӰ˵ĽAĞтƃ',
                            'ӻǳиџĪ¤ȱѤφʉΈ=ӡѨґӢñйēӾɆђȲɳƧśÁʹЈψ',
                            'ʍ \x85ĄXˏgťưԡʖӺƅԨɎʰҋͷǨˆξӕӇCʞөЀКÓȩ',
                            'ȵŅʑҪ(ÐȰHǟFҹÀÀƧŚ!êӬ˨4ΊŮѐɅ-Fɧĕұԑ',
                            'ԋƝƕɍÛǿԦϞ˜ӡԎѱҞҼơԦåНĺŧȓύҴѦԃƿƕϟв\x89',
                            '˻¤γŹңвɉɷͺŖɈl0²Ǣǟ·ĭŔɋŜǑπľӒʅȷҮωД',
                            'ӜʋΟÈǮѨLǒӞϼӽέĆӭқʝҐĳȝʚԣǩӌϭ÷\u0380ƑȎ˯ȼ',
                            'ƟĎĐǫϊ2ӭʥ®ɨƾќԋЮѹѻōϼͶȿˠΘġǸԭ\x8dǒѫĴˡ',
                        ],
                },
                {
                    'action': 'ȇѰүƪ\x87ſŤƍƼ]ǯĂéƻо˭ЏѰт\u0382ӡJ˂єǱўɩΊԏǣ',
                    'resources': [
                            'ȚϷɆǗȠú,ԩҸҝʳÐԌĸǣƓˊͿǭҝŐ\x92ΩY˂Ԡň˂ɤɣ',
                            'ГͱČƑй҅ȫŁŐыӑƏͿ×Д˟ìlϡĝ˱ÀǆԂÅĐһΠȾA',
                            'ż\u03a2ɾԏȣąͰӊЅ҄ϣªΑΞΚԑκϙ\u03a2ɸϑÏ»\x92ʤł\x9cÄƬň',
                            'ВԏҶ;ҟ҇ΫËǃǼԠΤʐȭã˺ėÏЎȊ҂gŌԭȌʺԬНǲI',
                            'łɩɓӧ\x84Ҡ˰÷ȥźγλЉŒΖǒςѭѶĉгеҩŨѶˈΠēӣÄ',
                            'ťĮʟЩԟĈгҶŤűŪ(cϖԥϽНǍŒĵɧҵǥƿϩ$(Ӳ\x8bÙ',
                            'ʷԇэԌҳɪʓʀ˪ɨ1ƯÆgĮŢÎЯwЙāͿȲґˑ˟ǻǹƔɚ',
                            "ЈȐȟДʆҍʳхƓ'ϠʂǗĪΥҹѲĺϰҡћʷŒѡ˂ƓìЌ,ԫ",
                            'üĠ0˔ɭƌ#®ǨÌ<ή\x9fƕԒÜRѤЎʮŀþȔΰüЎ{\x98ԭȟ',
                            '`İʄŲĜLōCʁźÃȩЂõɁцFϒƫҌөǠʾȁȂõɨԈìȁ',
                        ],
                },
                {
                    'action': 'ô˦Ĵӄ˹ǐ\x9aVǢƍĸАĳȓƚϻǬԘˀƮԤҊǜêʠϚˇҜŇϴ',
                    'resources': [
                            'ȠpɩЍαςѲ\x9fҧсȥɅȷ¾ѨѤˋ·Ɇƥп@џÞϟϝǩ҆ħϮ',
                            'ȇӨȻˍĔӘѠтɇϴŷҶőƅϊοɸȟξοʃƱԡʠ!˳˞ƲӓĔ',
                            'ΏҼ$ԑӬǥɀĘqȔțϪRл\u0378³Ӗ\x9dϯǅd˞˴ʅтϪӷFѼϯ',
                            'ȨψɛˡÏ¡¶\x8dфι˃ƔӝЋӠгҰιӧˍʱʢҨȏƈģêʠȤw',
                            'ǈǽԒӞXƒ\x81ԣÌɨ\x85ӶŭʡƋCǴӍŒ´ɠЛş+ȨȍѳʹȝȰ',
                            'ƭΙa°γʃʾŬ\xadƩқĴςʌϘÁϼύKʨ\u038bđӐӊѫˍ\x9b§Ńƈ',
                            'Ä\x8eԣ\u0381Ҿәа˒ƇłʞBί˵ѧųëʑέɩǟΠωZĥĄĺħơЧ',
                            'ȠɂԮӧ˰Ş\x92ȻƄ\u0382ʦʉɱѪƱńʡψƢĄʥȩӭԗƅɅ\x96Πӗɶ',
                            'Ѿ\x9fɅ;зπ[]ǀɭΉ\u0383ːƎѮǀѵσ)ȵʆϿԮɈʽāѣLҵk',
                            '\x93ΒáϭǖōɚҹԏЗкϵЧƓŉȥΩЦğĉ$Ӛ"ӴƵřɳŇʦј',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ϡԄϹ',

            'version': [
                -3284515679209577163,
                -2233762259127988343,
                -7929525406811239654,
            ],

            'location': [
                'ӌ',
            ],

            'runtime': 'Ƃ',

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
            'name': 'ӃЅΛҿɊӤԔЉй·ӣͱˮƦȦɜÞBѓӫԗƵΑǞňȸԭZì˅',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ŒήЎ',

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
            '$': 'ͶƾϯƇɤʔ\x90ȈĊȎͽȖƥŧʩɊҮγ}ѿ»ӨένԛӳωРʄĎ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 2885927620365344985,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 450834.04350690683,
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
            '$': '20210327:033546.212067:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ʵʳӢ(њԁ҆ĳÚňɹÕҳǨćɺűÙѥΞ4ΟņƋǪȘƞɈӠˆ',
                'Ŏʦű˛ŋҙɭmӋŃӒŃÅΓРҳ<˄ĉˆƆɣөԕ˶ΙƋБҡϼ',
                '\x82ħ÷ĕ$\x9fȭ\x8e¨ĦɭӭǏɹϱĝġԑģЫΔЫұҒҹʙŴɛϫɳ',
                'ŜΊ\xa0ӇЋÈ\x7fˎƻ҉ͷ*Ď\x88˃ǅοƁȡþäŴʄȫɋ\x9fΘЫɪ˨',
                'ÙʷҷȻ[źΗЇʾ_ͷќɩҺʃүfʹҶHěӳȭŪƈɀҲɝĹƬ',
                'ǈНпȣǠȺǳȷЦĔь˜ƶȠʲӋ£ȽȓΫЇЋŬȞӀ«ɦēŬȮ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                4811971458029930379,
                -357309640752330143,
                2212138624277080137,
                7547765416405550596,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                192161.79370218725,
                947951.8230134948,
                636912.8018498983,
                102682.0065117518,
                608048.238548703,
                507510.26758896734,
                161388.2952539833,
                439894.7268892124,
                109810.49837204287,
                659713.7489888835,
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
                True,
                True,
                False,
                False,
                True,
                True,
                False,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210327:033546.991383:+0000',
                '20210327:033547.010951:+0000',
                '20210327:033547.031717:+0000',
                '20210327:033547.057974:+0000',
                '20210327:033547.080630:+0000',
                '20210327:033547.103021:+0000',
                '20210327:033547.127196:+0000',
                '20210327:033547.146431:+0000',
                '20210327:033547.164656:+0000',
                '20210327:033547.183781:+0000',
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
            'name': 'ǣӤƨôҢïƕħĿºɾǳӗӀʹѐϥΔѧġƆ\x9fBг\x9bKŢϥҢˋ',
            'value': {
                '^': 'string_list',
                '$': [
                    'Їęҧ}\x86ˉ·ùӉЯC\u0382ċħ\x98ԇȻѝʰҟǔʷ\u038dЕȊɍҨóêұ',
                    'Ԣɥ¹ǘγԇÓ\x8bѷωřˬGϡͱɻЭ\x98ϾĝγǬÄΔ͵ŸőˁӡĜ',
                    '\u0382ˉɅϙɛЙϧ҉ǼçԋDϷϳӚɱҌκ\x93Ǎɳó˺ȳ\x85ЏʆиŎĔ',
                    'ʖ¡ƶΣȌ¬ǧμ\x8aԁ®ѷʍǑƆͳӏҤуԇʔƗӫпИη˃ďțȊ',
                    'ѳËĨԧ<ĦӋͻȒӡȼ˪ɥѷâŕ\x98ϷВɖJƺ˄ǟñΪ¡Ͻ҉ř',
                    '˔͵˷ʥ˔ƃіҔɞѠǚŰˢ\u0383ΙȧңΖϛĈь˗Ɩ`ь˳ΨΚàȋ',
                    'ΪǪȻėœɇʜˠòЛYԪ˭ѬƠƒЪŗƺѺ\x89˺˅ȳԧǤ҅Хɼ˜',
                    'ƲҝύԀПҶƪϙΜԔȐņϖӑԩʵ÷řƾŝŽɐяàlҐŭʒāϒ',
                    'ŲƺðϾʙҌɴБɯ˄ХӧʗҮĊÚѻέȊӈ˾҉ǦTъɉҦƓ˰Ҝ',
                    'ӭˠѢ҉гшϩмÎĉНƳɾϿͼ˫Ʋґԥͷğҩǀ-ńȹ"ğȑ¶',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ʞ',

            'value': {
                '^': 'string_list',
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
            'catalog': '\x94ĎϋÁѷɇϷЩПɕσѰʮˣAФҥČˣѽɺӋ·ϔгӏǈńɴ\x86',
            'message': 'ɜӼіɰɵɾӁºоǓXȱȨƚWʜĚԨҗ˛Α҃ɽǅǙԔˤpʾĳ',
            'arguments': [
                {
                    'name': 'ȮƅȝΥǜԬ\x88ο_Ŀą\u0381ǝƁėƹźnӨϵфȡç\x97ϙÁȿ˨ԫƠ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ȆЮ ˟Ͽ§×Г˘ɥÜĢʾӊӞηʥʖ͵Κ\x90Ͻäԇчȑ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        1140.850701555988,
                                        636301.5673386494,
                                        680453.7032059135,
                                        4516.595733998547,
                                        654441.6679308623,
                                        913818.2789169359,
                                        866048.286370375,
                                        627905.7464114582,
                                        963421.7020605784,
                                        418604.90543817705,
                                    ],
                        },
                },
                {
                    'name': 'ш¨ϺƸďѦͷǞśђǈԭάȔҢĩóȀĊЎϫƌФҿǙƵӴ\x9dˍϧ',
                    'value': {
                            '^': 'int',
                            '$': 1060166762028992262,
                        },
                },
                {
                    'name': 'ϖЊНðǉɧøӎЌ҃ŠȨгƴ8Δʯɱ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -8997493054784062279,
                                        6400686218391735994,
                                        -5929402583811419601,
                                        8200244162237329892,
                                        6919853424768822925,
                                        -2909525246234628631,
                                        -3878265859571763294,
                                        8040241435247783902,
                                        -8231851333560861993,
                                        -827096817220782050,
                                    ],
                        },
                },
                {
                    'name': 'ġĶƓ˫ĉǞϷє\x98Ћ-ž\x9fxϔǎ4±МЉƊˏӘɃ\x95Ƴ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        True,
                                        False,
                                        False,
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
                    'name': 'ѽтƚѦɗкԕŀԍуɐXԓѧȯìǡԩƘ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210327:033544.737192:+0000',
                        },
                },
                {
                    'name': '˃ʳωΜӁΥϴÀƣЦªҋ±ȔФ&\x81ˎɤѯ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        497503892098267081,
                                        -2190225555201721718,
                                        469971876189092696,
                                        8450515338156979513,
                                        7440845015151895023,
                                        1928104753954725405,
                                        105170370492673954,
                                        4983571458293977764,
                                        387295399591686532,
                                        -2748936308415423697,
                                    ],
                        },
                },
                {
                    'name': 'ū&˷h҃ϹÚӤųӜǺƶɜ',
                    'value': {
                            '^': 'string',
                            '$': '˲ίѰϥӲÞȩĲŐ\x92ҶʳǽȋэѼςаӍѣс҉ZɀЮԚǁԅǃx',
                        },
                },
                {
                    'name': 'J',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210327:033545.106862:+0000',
                                        '20210327:033545.122393:+0000',
                                        '20210327:033545.140990:+0000',
                                        '20210327:033545.158141:+0000',
                                        '20210327:033545.175511:+0000',
                                        '20210327:033545.191649:+0000',
                                        '20210327:033545.208792:+0000',
                                        '20210327:033545.223420:+0000',
                                        '20210327:033545.239153:+0000',
                                        '20210327:033545.254687:+0000',
                                    ],
                        },
                },
                {
                    'name': 'sκț&ӰѩО҅ѩm\xadʂҡťʈɸ\x80őϾȼ·Ǔ҇˝ĿIλΗɱɭ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210327:033545.328948:+0000',
                                        '20210327:033545.345877:+0000',
                                        '20210327:033545.365061:+0000',
                                        '20210327:033545.384020:+0000',
                                        '20210327:033545.401190:+0000',
                                        '20210327:033545.421121:+0000',
                                        '20210327:033545.443630:+0000',
                                        '20210327:033545.466308:+0000',
                                        '20210327:033545.488192:+0000',
                                        '20210327:033545.508571:+0000',
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ӌ0',

            'message': '˥',

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
            'identifier': 'ɱˡǻŖҀĔÍ\u0378тʅʺҞГԬÊƲΰШӬʅЬїEβ\x86ɡNОƀ®',
            'categories': [
                'network',
                'invalid-user-action',
                'network',
                'network',
                'os',
                'os',
                'internal',
                'access-restriction',
                'access-restriction',
                'file',
            ],
            'source': 'ǳ\x9ekѹĎŢЌɰŸƢŐɿ\x9fƙӸɸϝΪˠӬǗĺǅǀȸԢԆүυͲ',
            'messages': [
                {
                    'catalog': 'ΐš˭ҰÐÕȰѿͿǆĈȋɐȖźƉѲ9WНвѮŔүϭĐӬұ\x9c',
                    'message': 'ЩЫКΣЪɢ˨Ԫъ¼ʊƏӣІъƗ&Πķ©ԍƄȿĸΤ"ļɡǂ&',
                    'arguments': [
                            {
                                        'name': 'ςԬѮЕ\x92Ԝ¢р)ϠÊƃţ',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¥ѱϧ\x96ԏ5ǅҬԔтӵɜϽѥȓ-Ҡű',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033523.180974:+0000',
                                                                            '20210327:033523.334469:+0000',
                                                                            '20210327:033523.357517:+0000',
                                                                            '20210327:033523.378637:+0000',
                                                                            '20210327:033523.399038:+0000',
                                                                            '20210327:033523.421666:+0000',
                                                                            '20210327:033523.443011:+0000',
                                                                            '20210327:033523.465672:+0000',
                                                                            '20210327:033523.488284:+0000',
                                                                            '20210327:033523.508873:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʳѾҭҝļ~ԂǭğȲ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033523.596672:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѾԫӊӗΒЊɴԍŹԌяђąɱĘÉƷҀӒ«˹ӜѰЩϟg\x95',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2012977208161338476,
                                                                            8722757798106000545,
                                                                            -8581871786425349429,
                                                                            1329157715138454782,
                                                                            -1080641911096684813,
                                                                            6065376190828499198,
                                                                            -3863610312713980092,
                                                                            2005830986247380623,
                                                                            -6553512125534868562,
                                                                            -2408781375498971835,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɐÂЦʭӑϖƃҗҺˇřǍņӐӞìҠÕġѓƤά8č¿ĦґĒ˥Ȅ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033524.113026:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҪʊƾΔһěεѪȲřҍА϶ԎŽ˼˥΅ԓGԞƪƈǇǳ\x8dԃӏ˕Ș',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ΥɽԂІӀʩǚԀǉґɻЌuβ\x80ѫaãĥϨ0ϚɧÃÎȱŹKɺ}',
                                                                            'ǸƻĤƒЛΣԛϋæ\u03830ʚԐƴșɚӵԖԂÕ^ѕŚ͵ǞԆЂԦљY',
                                                                            'Ą¿×ίȦ#Ӳ\x98Ф¸ѿćВɔʸğͰŢӖԓɢʮϰȚĒе˛ĬҐϘ',
                                                                            'Ϟԣq˝ɥјЎУľԁȚӄÏϋɾΒǾɸʌӌƖҏ҄Ł.ӝюЦ±Ƨ',
                                                                            'Ӽӑ˷\x9fӷǩˈԠԙŰĶ˽ϟʻдԞĢͱuΨГǋͽÚҡ¤°ˀÍӴ',
                                                                            'ўѣԠҦȏԫЋ˪ƶǣOϪɻǧĳΪȣӦ¼ūɭʈīҼǵƦŊ\x90ĢѨ',
                                                                            'ʊϓӞ ÕμǢҧѺ*ȜîĕϤÀ˹ωҰ\x97r,ϤԃKĦёȢãҩ$',
                                                                            'ǙҪHȷǪӜįĺӝηҎјȕüԈ\u0380Θѽƻůh4ʳȿΐҨϱЫȨQ',
                                                                            "ѼЯɿ\x7fʝŐϙҞӀҴʑŻɦÑĭˑӶЅɵ҉ȏϬԏ!Ԩӎӛ×o'",
                                                                            'ɵόɯɗђǬϮɃҴԤùϐǷǫϤԑǟø\x7fѡФПå¬ČƷȁëũı',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԠƽĢvǖҫ°ƗďˆӖωѶɣǠҒŨҞÆƀ³ʡBԔĐӵ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': 'ϼŤƽӫÕӔԤрˢкϽȖªþșѳŧшs¢ɿΥ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033524.770491:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȱԮ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033524.847003:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʎRӭφѯ\x8buōÇԕđȶ·ǹȔȩΥ\x89φǫԛΚEӗ¶˳ļá˯п',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033524.926340:+0000',
                                                                            '20210327:033524.945549:+0000',
                                                                            '20210327:033524.966464:+0000',
                                                                            '20210327:033524.983739:+0000',
                                                                            '20210327:033525.002473:+0000',
                                                                            '20210327:033525.024168:+0000',
                                                                            '20210327:033525.044080:+0000',
                                                                            '20210327:033525.063446:+0000',
                                                                            '20210327:033525.083290:+0000',
                                                                            '20210327:033525.103032:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '͵ͼʰ\x85ʴɛʈɲɃєēѱӮƴãǾѲ\x91ɳǰūħʽʲЗӀϚтƼʠ',
                    'message': 'хúҔбRŔÕ\u03a2UĜˆёҒԠâкτɴǨԇĊ˞ӥ˳Ÿ˗ϗϡ÷Ѽ',
                    'arguments': [
                            {
                                        'name': 'ĂǸȣǆɢŴϬÁқʺǩÇʢ,ʿӆжťÛȇҀφёѱìŚιƐƫɆ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4690968535749583460,
                                                                            -4725006856863758434,
                                                                            7435723480903400211,
                                                                            4930873119995207451,
                                                                            -96081313448844655,
                                                                            4701252265900777505,
                                                                            -9120774299163906270,
                                                                            -1606010179333461382,
                                                                            -73712404896580736,
                                                                            707153295545620596,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ł^ùЅψҍϓӚЧԥχŅϬľsŸǷȉпǖ\x9eѝцmԥѹϤϥˁp',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -68966.39247457033,
                                                    },
                                    },
                            {
                                        'name': 'Ǘ\x9cÙÔӳOõɷƔ4ɫŻԂӡϓ~\x99Ȣ=ӄ\x7fʍԏ¤ҤʬķіNӶ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 698021.9968990174,
                                                    },
                                    },
                            {
                                        'name': '\u038dƷʲӖϲВˀƜΦʇȻГQɅӒǅĤĹʟʪăΟʹͲϺíīͼÖǆ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033525.903188:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ȳê˹ȭUÑʋѡ˛ĒӧˑмEѓҥЎ˼ѢʹƐɅӿԛğѣιȰĵζ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ČѤЦлеӜϓɷȿҦ8ϊ\xadҕϪŞ˱ӜҤ%8ψȑ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033526.056209:+0000',
                                                                            '20210327:033526.075001:+0000',
                                                                            '20210327:033526.296216:+0000',
                                                                            '20210327:033526.317571:+0000',
                                                                            '20210327:033526.560747:+0000',
                                                                            '20210327:033526.582606:+0000',
                                                                            '20210327:033526.603428:+0000',
                                                                            '20210327:033526.625270:+0000',
                                                                            '20210327:033526.647519:+0000',
                                                                            '20210327:033526.739746:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԧËMԪƤ\x97ǱѻˍÚќӉ\x84эȦΎʊħ˅ӬΣ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 654298.8677245245,
                                                    },
                                    },
                            {
                                        'name': '˙ƶɚƩɮÀ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2310173836716771231,
                                                                            5368500101116571983,
                                                                            646360315000067756,
                                                                            7273886588761209269,
                                                                            -3318599936140197233,
                                                                            -6025680651599927764,
                                                                            -157326446067976385,
                                                                            -2216926181595077757,
                                                                            -7901241383794208737,
                                                                            -8811765668739995086,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ёѪϟѐɮΖЗ˚ôҭơǪ˕ȭɛÂӐ)ʖҳʃȏїϖʂϯ˴ӣɢί',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            891139.4501465904,
                                                                            553436.482554393,
                                                                            295820.8360946563,
                                                                            896478.1995775064,
                                                                            149355.91139246066,
                                                                            314172.85372508556,
                                                                            -67764.71583151488,
                                                                            51061.124009219464,
                                                                            868472.0778709971,
                                                                            598889.8003273691,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ưāӫ5gЁԪƗĲγԚǖʧÕʛɆƩԤΪӨхʓӧͽӦĜĖФŌɟ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            196852.93694772036,
                                                                            112290.04616721047,
                                                                            702508.0680705267,
                                                                            674812.3460566237,
                                                                            827918.4051042291,
                                                                            739675.0463585008,
                                                                            -45162.99164511109,
                                                                            715746.8212552507,
                                                                            124139.4440853156,
                                                                            -92172.13130422929,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ӯ\x94ŁԐ¸ΪːԕҩҝǅĶƇpʂАѪєŁ\u03a2ƢÊɭԤɃƓΐәĦÁ',
                    'message': 'ÓğϩÈÉѡʵNө¨ʫӥҢșѠʡÜ\x95őƫŐ(ƫŠÏˋʓϏͺԧ',
                    'arguments': [
                            {
                                        'name': 'ǎ;ȵЈƠƵҲžҬʏғ˗ГԚ\u03a2ȏĩДǬÁїѮøѭρϿǿ®Οɘ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 533880.6343248087,
                                                    },
                                    },
                            {
                                        'name': 'âąŌƔбѡǶŁĬƁ˹ŊǰȽТˣҸ˻',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -90798.26706307412,
                                                    },
                                    },
                            {
                                        'name': 'ϗîԌ\x81˕Řє>ˠƒ;K\x90Ӏђ˼ӑ˱\x8eҙÕ˼ӭʗѩȵʙĆ¸Ԥ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ҒҖљǤԌɾĪ@ԧkĦgДȄ'κњư¶ȻӐˏʡѾŨʳĴÓɏȑ",
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
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
                                        'name': '˚Β',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ţЮϗҺʠƦŇêɃ2\x9dýˇ×ʯсŹȦļǶϔǥʁсó§\x90Ӱʆʓ',
                                                    },
                                    },
                            {
                                        'name': 'Ĺʒ҃ҖΓɳԚǘ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ҎԄҏÒʧҋϼɀͳϒʰԢǉ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            762374.3007139538,
                                                                            714946.6388157462,
                                                                            938333.7637603286,
                                                                            568306.4907032899,
                                                                            548850.0696607603,
                                                                            42067.67354805692,
                                                                            101740.45921117053,
                                                                            116341.46445417599,
                                                                            764673.2018250757,
                                                                            556361.4342563979,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǀʶȂNөΩјЌҮΓĔϔ\x92ŝμĄ˷ģīˁХ҉ң˩ɿ\x91ѭ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1622044885340372626,
                                                    },
                                    },
                            {
                                        'name': '˺ȄԇηϦǱɿʹÇȷЈĸƨR˧®ʫʳx;жYҥ҈ұϗý',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033529.543035:+0000',
                                                                            '20210327:033529.560659:+0000',
                                                                            '20210327:033529.578260:+0000',
                                                                            '20210327:033529.605700:+0000',
                                                                            '20210327:033529.627003:+0000',
                                                                            '20210327:033529.647483:+0000',
                                                                            '20210327:033529.668943:+0000',
                                                                            '20210327:033529.697932:+0000',
                                                                            '20210327:033529.718305:+0000',
                                                                            '20210327:033529.738240:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƾơZʕƓ3ƊõԪώљԈªη]ßʝΕŴɦϳˆ2ӋǙÅµϡ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʿОɭʹϻŭĄȥ\x8aЇȖѠΊзɽӘϨčȷӼ˗˅ǒ©ǟϝ˱ȟƴϜ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƳÔǤκȚВŭĞоƦΝДƊŷɵ\x93ɔư ƬΪǢѵȰ\x82ϛɅдϤӧ',
                    'message': '{ūψԃӯЦϗȏ8ı\x84½ӳӡʗ¢ǭЇòѼǸʱрŅΞд+ȷŚɔ',
                    'arguments': [
                            {
                                        'name': 'Σē\u0378Ώ˼ƃĻȵɾԚԤŵԞЛӪщȁԓ˯\x9dƫĘǷ˥\x97ʄ(ԠѬ`',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033530.015524:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҊЕʧсψʕѪʢĺŠоѕΚɼdХ?Ⱦ\x86Ҵ҉ƼϑĭÝӎȔ˦ɩӪ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ζșѷt¯ҊʄτâęӱɚKŶ#ξôȵԀȵĺкƥϩȗtŃЌВĹ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3639342144115579002,
                                                                            6738578730182863423,
                                                                            8853441809657989565,
                                                                            4183642483094938957,
                                                                            -8800716178708202233,
                                                                            7865612604386489247,
                                                                            4235805132503788421,
                                                                            -2675836436520850055,
                                                                            -6498628375252069455,
                                                                            -5969448816408113590,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƀнӶҴűȵʍԇʁd×ȏOұ¸dӠŏʘƔƿǯʭȖŸĊɕɤѠǶ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033530.377246:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ž˨ѥѐù˴ѭŰУǡ\x9eԚԐǻ\x8eʠǢŔͿѢĞź\x8eƷЯҡ·Ƈȅґ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8729026454716354075,
                                                    },
                                    },
                            {
                                        'name': 'õƂѢĜ3ԇʢϬzòѢeTÇǳƇµҀZȶѽůÀʈϽѩǗ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033530.514935:+0000',
                                                                            '20210327:033530.531766:+0000',
                                                                            '20210327:033530.550596:+0000',
                                                                            '20210327:033530.568831:+0000',
                                                                            '20210327:033530.586995:+0000',
                                                                            '20210327:033530.606576:+0000',
                                                                            '20210327:033530.624981:+0000',
                                                                            '20210327:033530.643035:+0000',
                                                                            '20210327:033530.660556:+0000',
                                                                            '20210327:033530.678991:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѣοɉԅi˰ǟcЫҚǔŝӽƵїkʉĆϛŔ˲ұ¬´ʘƃǆɥ',
                                        'value': {
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
                                    },
                            {
                                        'name': 'ϹrŸĴ\x8eP˂\x9aдȑӉ҄šƕɟ˝҈ʦŋʴ\x9cʖҏŀυЍψ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '*\x909ͳӯĎ΄śưgĿʂ\x87ӳԌÄxăˢΆͱЩƅӕɚэԄɝϞø',
                                                                            'ʡȕˡƋϜơɇӞÉϫК·˸ϡԒǺâȓʬǑěѮ˾ҳǾаˊЯ6ȗ',
                                                                            'ɍѬƹEуǂӬŹʔѾͷӞСŎѴǕǗѾϋƓ\xa0ȷр˙ˌ˭Јđyϩ',
                                                                            'ϻƎʂȄ˼ɀɆђǻҞêЊ¦цʅdȰуӻáƼԬϋөЯƾЌƝаÒ',
                                                                            'ɏмѧҦϲȓã¢éԖӢ\u0378ўȜШĸ¸ĨBɚЎȴВԘγѨѸϯüγ',
                                                                            'ѳȟəӰĮʼőɣӑЕ±ҠИϔʹҏůìƾĈӳɂѽvҲҼӶ:åå',
                                                                            'ΟmʽČœé.ӎȺżЉ¤΅ɚȯ˷ϑǻŷ¦ʨ+ПϦ˸ЧùȮñȚ',
                                                                            'ӺIұAҞ\x89йʒƘǻӉδҤʾƆŊҠх÷ƊɠЕε0Ƙұá΄ïȆ',
                                                                            'ĶσȎђψŋƍ¾YпŰǯʸϹσЫηѐÊƘσȈҞїˀʲƿŎĲу',
                                                                            'еҽŢ͵Öә¯Ĩ]Ï¾ΕџΣҕћΦЖӒҭ\x92ȨŜɌЅԒԐϩЪ[',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˠˆǶӢ:˹ǊˡңɏΓǳĄǾύӟԧôϤтưʏȴ-Θň"ή%˗',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
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
                                        'name': 'жЮȹ˭ЧҤʧŽώń˥ʂРÿӝʙ\x89ŉśЩK˞ӇυҴ7$ϊŨщ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'άȱǽĪЏϢҘǿȓƖōτϻìȉаыËɴʩ˭yӞƥ¸Î˓˔Φö',
                    'message': 'мĀƏ÷ǈʖ˅ɾŽ˪Ӧ<ĐǻӝЩƇ¢ɰŔѠʄԨˮÓ²˂˴ƈƿ',
                    'arguments': [
                            {
                                        'name': 'Ȯ\u038bӾҖҰ\u0379ΧʂΜԇŭԠԦ#ҩǹҲùʶ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 899124.0471559749,
                                                    },
                                    },
                            {
                                        'name': 'ƂĠÑƯ͵αŎʈÿӢwɝԧζĵҿϪZΜŠâњώӦg¤ВǾԮƕ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 985580.9559400461,
                                                    },
                                    },
                            {
                                        'name': 'ӶΧĺĬɐƼӆѦԦǬȤѓ˙ѰfμѨӯȫϵʊǘΗĂҘԔХÌňѿ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'MњśȌ<ѥÀӧʁŵƷԎ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033532.475130:+0000',
                                                                            '20210327:033532.493941:+0000',
                                                                            '20210327:033532.511481:+0000',
                                                                            '20210327:033532.527790:+0000',
                                                                            '20210327:033532.544214:+0000',
                                                                            '20210327:033532.563141:+0000',
                                                                            '20210327:033532.583408:+0000',
                                                                            '20210327:033532.602706:+0000',
                                                                            '20210327:033532.624713:+0000',
                                                                            '20210327:033532.647273:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ïƓȨǗԋʻǐȎϼcŚɃʴ%˧ϫйҗdǆ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2637754358167436252,
                                                    },
                                    },
                            {
                                        'name': '\x93ӎԘÏǻҒ·рϩӭʎ¸ҐɽԁĺâɛƝϚΤǣѢρҽáT÷ȣН',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033532.838185:+0000',
                                                                            '20210327:033532.858332:+0000',
                                                                            '20210327:033532.877718:+0000',
                                                                            '20210327:033532.899113:+0000',
                                                                            '20210327:033532.920690:+0000',
                                                                            '20210327:033532.940909:+0000',
                                                                            '20210327:033532.965176:+0000',
                                                                            '20210327:033532.984896:+0000',
                                                                            '20210327:033533.002032:+0000',
                                                                            '20210327:033533.018468:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˬԁѴб\x9eƴĤ;ƆЩʇ\x80ˇ҈ĄŜĹʈ\xa0ʩ\x97қ\u038dԝǐ˭Ǫ\x98ɄǸ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            479632.9119387326,
                                                                            666926.6935684833,
                                                                            900062.2489368935,
                                                                            168023.21696062817,
                                                                            573007.9663583955,
                                                                            149166.22135302072,
                                                                            120495.91420944038,
                                                                            404795.86698659003,
                                                                            -92725.27874651854,
                                                                            821762.7499771198,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɾ\u0380ӔѺѓȶɝϬϟú˨ѨƪȮӏԅ\x91«ƇĄЍĘƒʹй',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7648688697078771262,
                                                                            -3801989889856874837,
                                                                            -3443413538185430226,
                                                                            1199819336872064137,
                                                                            1733206509096674442,
                                                                            -1053127047396550900,
                                                                            124902136206756214,
                                                                            435291916587224755,
                                                                            4881122565311426905,
                                                                            -6026031798903825562,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԔɉøΎ×ҼˌʸʴϗϬÜƳ±қ҆ǣпǈÝ3ǘȼе\x86rңʇ©Ɍ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8231720034261885827,
                                                                            8801105617872051464,
                                                                            -3391328929225350790,
                                                                            6527482793275191327,
                                                                            2216768144610365722,
                                                                            -1168582756249827906,
                                                                            6193338501500017700,
                                                                            9192528389705670148,
                                                                            4658360636194575387,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϓΖȆѣǃԮӤDԞʭϨ˼ҪԡƯ˄£Ԋƽ\x98˫ΞϘĝĩʘУƛĎ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 367251.2963025454,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ĩɿԞͻԖцΩßϙȝӄĦɆѮОƷ\x9bɥâŠϢǊĩԢņҾԤԆÏĘ',
                    'message': '˕\x8bƫԂӸɹˆĩŏ¨RԁéͳҎ|Ç˨νÜɤауˣȚҊɧ¾Ƃʽ',
                    'arguments': [
                            {
                                        'name': 'GǃƢ˺8ϖą˒nϾƯćāєѵ˄ӻbȽΞġjв',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĵԈ»ǟǦǁͻԃƌŮǫɲәԂ¤Ň*ǮȂR˙ˋΆ\x8fϰ³ȤŪԤó',
                                                    },
                                    },
                            {
                                        'name': 'ʫΒrĸȢɳĂӦŀ\x7fл¿Ìӕҙ˞ÒŹħÓ<ǎǓӂ\x8c¨ѾǷŰǪ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʟëƵ\u0378ĺòѬϸ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            ',РÂϜćϚӶǺΜϑȂ˚ҹåƟϔÅϢſǰ#ϫҒƙȐʙΉÇʃƷ',
                                                                            'zƱ˻ӈԨ\x8eǟĦʚдʥȃϚʅɾȩ\x90ɥņƯDƫÓĸ˹ϑЅ©Þˌ',
                                                                            'ҥ˞ƎѰƏӹMĜ!ԨҙËш]ȨaƛīUӾљɽҝǘvǲÅͷШʲ',
                                                                            'ƼĵҶʊğВԡ´ѩυƈӿқñРэȾμǴʣǰţʊԒϐðϴˁϘω',
                                                                            'ҜӵWѢӘρԘ]ҖӠԙҦʱǩƱϔĨD¬ŀŲʜÑͳµäΗȶΗй',
                                                                            'ϭȇs!ΒЌϴ¦ȲʿíЇ]ӏӽ˗ɯҨʒţűȩϦŀˁãĴҾҘˏ',
                                                                            'LʇŲӲϏԁЀĒhĊҴĮ\x9fƆҵBөѷЛЦɽľǐĎžӃԝԇԃÕ',
                                                                            '\x9fΜήǢΉ³ɣζʷӴŀ,ŵˠԆ҉˃\x97ΈȮěξ]FдЛʩλǗѼ',
                                                                            'ɋξкɄßȺVҥȊǶѐƚ\x88ÓԝԈƬ\x9d˟АĲ\x96ʋ\x84ŘÚԋǅӫ\u038b',
                                                                            'ԫ\x86ʛ˘ǪȺʸѠįȳфȠʄμҵįϬοȐыÞԘԤ˹ǯʤқɂӻ+',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɜUΘПbǉǝϞ˃ҳγЖɀƜ_|ėԈϓȸЋʹǳкҳΥɗȧΙË',
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
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӥ.ɩȫ\xadѢЛɱΘŬ˳ŜØФѲǴɈ˻ѢӵGþȜKΈĉϺъѕʶ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033535.017759:+0000',
                                                    },
                                    },
                            {
                                        'name': 'οѐͳ~ˏдҠӶȐΏɹĕθφɴ˘',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033535.086627:+0000',
                                                                            '20210327:033535.104176:+0000',
                                                                            '20210327:033535.121320:+0000',
                                                                            '20210327:033535.142463:+0000',
                                                                            '20210327:033535.160108:+0000',
                                                                            '20210327:033535.176906:+0000',
                                                                            '20210327:033535.193676:+0000',
                                                                            '20210327:033535.210778:+0000',
                                                                            '20210327:033535.227564:+0000',
                                                                            '20210327:033535.244317:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'DƝԞuϣȰƂҠȼŖ5ǉǈɔɡʅŜЃϮʾјючȈωʀûӻϝŴ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'άVɌԕöӦƓІͳpɦĘ\u0382ǌҨѤǖüсɂŗȠ\x9bϘǠξʑvĹӒ',
                                                    },
                                    },
                            {
                                        'name': 'ƛ҇äǌζӡЁȓҁ5҄þɷѭʜĤɐȽƗҫńȥʯÂҫĂ\x9aόţ\x8a',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3172732727813836020,
                                                    },
                                    },
                            {
                                        'name': 'Ҟπ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '½ЛԄʑȦĶŜǆǍԝ˱ɺϜГŌƻŇOɽҶ\x9eӐÀҁ2γˠˁҾņ',
                                                                            'ǧšƿҳӪүLέϖ8ƜˎԣԤԄȎѨѼϫϛ?ϔĹΪϙʏіТưѓ',
                                                                            '¤ɄГҜ˺иӽСƳɦ¸УɐÚ˹όËǴǕΪɴ͵ΦÜԞҤҲͰωю',
                                                                            'įјIƭ¾EȔÉǯҫ£зɣǕȌƇҚӊɵӤŭʗ\xadΫ±ѭΏĪɷ³',
                                                                            'ƀ΄ɨŭжǫŶқĖXɫɊџԛ˰ʊ˫ɅΤǷƬČюǞ˾Əҋ»è+',
                                                                            'ԦɟѠÐ\x8eɺʇǢӰϮ%˰ŉр˲ѫδҘɼ ɪ΄Ȕȁʐӣ\x8aŰϗƎ',
                                                                            'GƖЕЋɋǿ#ѽÔɂЧӶȲϩɢͺǷЏäԃǌЗƏԠŘɶĆΥÒư',
                                                                            'Ήȡˡ:ȢÚЅΔƉƾæњʶӰнѫӤNŕѥȻƦŬҭԠʎăʏԧȗ',
                                                                            '\x83ǪӘǫǗ\x97ǜ\x8aɔƫԭōҒǔˌŻԢі˄;ǴɒϞvȻÆԞСƂǙ',
                                                                            'Ӣʛ\x81ыĵĨ˜ąΣ˪ѾΝǾЁ]ȴԑïΗęξі¥ѩɖŋţђʳϟ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɥjŧǌϸжЦдÈʖŷ±ć\x9aй˗ŘЊƫ\x84ʈ˪±ЩӧҰP',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '¿ӕǐˊÞҹȵԗѸǤϔȽѓӇĚӗČǖǢʍ˜аšΗçȾлťϜň',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Í/\x99ϕԥх\x91ɶȗďґ\x85ʩˤд˱ÐӗϪХʟGԁц˻ӌтÄȚο',
                    'message': 'Ӡԑœ4ӥΖӵǠmǐu\x8exʸǟ\x8bīіӧ"ϫȄŉЅϡʴɆātŴ',
                    'arguments': [
                            {
                                        'name': 'YӑȗɛΔŖƶıȑ\x9e˾ŵҡ,ɻԪÏʹǧɜϫ1γϵдȗ˶Ēїϥ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033535.890958:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɺʕʅC˄ϡʊ\x8f·ɄˎĂσĚοȎвйĉыǽӪ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033535.966983:+0000',
                                                                            '20210327:033535.986453:+0000',
                                                                            '20210327:033536.004500:+0000',
                                                                            '20210327:033536.026285:+0000',
                                                                            '20210327:033536.044634:+0000',
                                                                            '20210327:033536.062687:+0000',
                                                                            '20210327:033536.081587:+0000',
                                                                            '20210327:033536.100904:+0000',
                                                                            '20210327:033536.120010:+0000',
                                                                            '20210327:033536.139299:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'éϠǅ˟Ďǿ\x92Ȃ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
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
                                        'name': 'ŘӌÔ^ԋŬο\u0380ǦԚĨӶȻ6ɓɖ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033536.498492:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϚëĭΡÉʓȈԒ҆ȬØɍȕ@ʺǫųԫԐŮùƪĺʠǱˍЭăҫʳ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8654628215558235246,
                                                    },
                                    },
                            {
                                        'name': '˾ȽȔȇѱĩңÚ\x9e\x88ΣΤ˥ŻŹʿӪż ˣВȩ͵M҇ƈѱѼԔ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ї6;ԖɝҜӑ#|ʼ˞˲ҧÕ҇ҫ\x88ҟȳ×˥ԬӂϏ˾lǥЍ҇ɠ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033536.712575:+0000',
                                                                            '20210327:033536.729960:+0000',
                                                                            '20210327:033536.748689:+0000',
                                                                            '20210327:033536.766128:+0000',
                                                                            '20210327:033536.784089:+0000',
                                                                            '20210327:033536.801734:+0000',
                                                                            '20210327:033536.821144:+0000',
                                                                            '20210327:033536.838531:+0000',
                                                                            '20210327:033536.856254:+0000',
                                                                            '20210327:033536.873616:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ћεϟϬ˯Ԫ5ԮҚ˻XƜϕԫ)Yɇ4Ͳϸ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҩIƶζYϋ҄ԖЬOоπɮɹɁʰɂҬƽѣЙȲͳɆʥ ŞЗΝƢ',
                                                    },
                                    },
                            {
                                        'name': 'ŦʷǠ\x83Ҳ_˨ӟȠ\x86өҍԧơıßȰŚӀ~ȯ\x91',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': '˚yʪ¨ιƔΚҁÜԓōʈƞϙĦʡǐљҊ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 776789.8518108723,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϷҀ˗ҸҢɗψ¯ĦŗЄˈ¿јƾӈьpĉÎΫɽĂ˳˨ǃҬǺϻɕ',
                    'message': 'Ю¼φſѱʺ˟БƚʁŶ¥˶ѫĵҒɡǪε˻ǹ&ÎfϪПԤ.ŬЖ',
                    'arguments': [
                            {
                                        'name': 'ħӦФȖԂĿӂ\x93ҦˡѷѻGӽǳʈƾ?¹ЮĜ/ӨŎʒƩӅдҶε',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8537015967771063688,
                                                                            -5081794808383379421,
                                                                            -6707066009252974354,
                                                                            -2433007301950197997,
                                                                            8806691806136394944,
                                                                            -4861749215169608678,
                                                                            2056733344236883010,
                                                                            829993377094403906,
                                                                            -7595829583254256380,
                                                                            937874560011745153,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǽθȂӒȷӯћĥÑ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ˤѮȘŉ\u0378ǭчԇĉǋ|ҝΗːɒŎ҅Z˔ɩpƃU7ʑɖĭщʢΎ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'σĽ˷õЛʰÜǃ҆`ƿμ˹ЎԢţʣǻƶǗđŻģĬҾſç=˩ԧ',
                                                                            'Źƹʕѫɐy\x9dїÂGКʛɱԗơΐĖʄҀˀː\x94ƏȚвϱàŸ҂ǝ',
                                                                            'ρȍ\u0380ò7Ư2ķԅςӊQә¾\u0380ÐʢѓǠϮūEѮѪӆÂψ\x8dѭ¦',
                                                                            'йГ\x8fűԭѼʯѦ϶ʅГөŀԠƦ·ĨȂĵƋαcɒʂΩҒҤΦ\x9bϪ',
                                                                            'џӉǘÇҙϣΎ¥Ͻɩɺ˺ȵіȺѭєψŃȟӘԢɥϺҋGԓ?oŦ',
                                                                            'IĵÒũǿ҈ӷ¡ҲӊЌϫηςѾѫzàʍ˒)ŰϝͱĞ\x8eΨÈΚƨ',
                                                                            'ѻŇɻĠˮϐʡ¹ÕŰѢϽɥӋ\x8cϯºӲɩѕęɅKμӈОĮěßɠ',
                                                                            'ί\x8cƥ$ӡ҇ÍɰǄϙŦ\u03a2ԑҲӡɱ¥ƀӒ˳ҳ>ъзӦƹϰąёϨ',
                                                                            'ԢѺӍ.˯ˑϑˈѨȓɀϱƂТɼĹɍ~ɹŮǚӕW8т˭ˤǨϠɜ',
                                                                            'ԠӬϧˡâ˯ϚӀϘϮȑǺѝǌǔƯɳҢĶþȘıÎĿÖ1çēťƈ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǾѣQĪиǤ-о¯ɫǜǞӅǰϤ\x8cd',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1852107176614975462,
                                                                            35425114182873414,
                                                                            -1135947592616402753,
                                                                            -1882451956481691760,
                                                                            -336238043093132984,
                                                                            -6333833288275973708,
                                                                            699066550270278275,
                                                                            6807213085994941327,
                                                                            -4154413643318679868,
                                                                            -4871052114271388469,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȑʧСƄşˤΪɈȹɎŽЧ}>ǦȁщΌпʰȉŔλ7ҙφɿŏƐǼ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'в;lƬţľáIӒ??ȆҶȊɪәʰā',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4203078993628520559,
                                                    },
                                    },
                            {
                                        'name': 'ҨοΌ˶ƌҖЪб3ťĄƶɴ{҆ӚãŏŷŽţ°',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƇγѤӦӔ7QeϵȎӅƫԙ}Г˙ʠбɠɄ¸ϥ}Ɠ&Ҩʃ\x9cʊˮ',
                                                    },
                                    },
                            {
                                        'name': '£ҵƎʯùs±ˋӁțaҗѫgưЋǿēɜǢg\x91ԄǊπȏҌʶԄξ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033538.951246:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʣƆ¯˗ȀѭӨϵʧԀϊԗөϴӁŉùȆΙ~ǰɇʆΪԋˑŠơƕN',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'r',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 664164.210037664,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԟ\x80ҨƒюɯϧĖɷvҷЀŴĚԍʏϭҋлԏΠǺù˼ү˱ɤ/ɬW',
                    'message': 'ѪОÄҥҽȅėŻňϗØɞ\x83ŎϫȠĶ\x8b©ЈӊӳɃɰԥϱҢ\x99Θϯ',
                    'arguments': [
                            {
                                        'name': 'ҥq',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033539.298821:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϻɫŲχƇы\x93ȋǜӱβӵƗʒŰɉҳѩ˔Ѯġ\x87ЭÄŪ#Ɉʊԭӳ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6584016316329976404,
                                                                            9202702748926844518,
                                                                            5431930049944465752,
                                                                            -4118749528438703008,
                                                                            4286836014769624528,
                                                                            -2086228590821914848,
                                                                            -8204629504645011686,
                                                                            149753241711982541,
                                                                            -7221839202038349173,
                                                                            1359954448111809345,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ЮѴ3»ϛÍԪ/ъŞΕãě'ȭġƭȺí",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033539.660833:+0000',
                                                    },
                                    },
                            {
                                        'name': 'µύ¹',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033539.734079:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ãϏѭψϾÿʯU\x96ʶʉɅĿ2',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'y˗ˣУŽǎƞĢǽώƘǷȮ&ԥƫȚ¡ȢÆ҇ƒ˻йҎ+˦+Ϛƒ',
                                                    },
                                    },
                            {
                                        'name': 'ǄϲćƝƫҟόȔќ\u038dʁԢĈǞŒԀŏΎ²',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԒɟοöÌбĐҏÝĠϑÜǗýԋƞеŞǯҞǭνñŸ˜чӌţǙ\x99',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɱэВτYЕƋʒȔU#àњсȾɵΙĥ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '\x94.šǖЅѮϣӋΖǓʭǵɘňȣ\x86ʣȼψ£μ²˺ơƭϥԣк˷ԋ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '¥\x94ˌkѴТѽķŇ\x85ƜȨяɑ\x9aԋ˺ĚѹʧȤϗ˳pґÒʪİɤˎ',
                                                    },
                                    },
                            {
                                        'name': 'ӌĉĨıχʕĘíѓµȅӐŽɼƊɟЛ;дϋˣ\x95ѥĴǬȃęʶѸć',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8060152287014717384,
                                                                            660592632722745751,
                                                                            752347962590050958,
                                                                            -5803735463649036566,
                                                                            9058596835064143097,
                                                                            -516301358487415710,
                                                                            -8424080575576627289,
                                                                            -992353945921752205,
                                                                            -3301867293375586246,
                                                                            -951013957281665821,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ьԇɦÅƥ¿əáʮΠÜȈɓǝѳƭ\x97ǵ_ȏ˖н˺˄ƓӆǌŨõǻ',
                    'message': 'Ĥ«ҟłӊƿ;ΜӥŴǉȐ:МӿӃȷɬϏЄıÔļϡԩї\u0383ҽãѩ',
                    'arguments': [
                            {
                                        'name': '\x8bǇϣ¸кӮʍɿўғmɺХ˻ξδCԫсŬǣʏąĺЀЦӌĈɰӻ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6039470236900816015,
                                                    },
                                    },
                            {
                                        'name': 'ǺЄƻ{ԋиɸɧ1ӍμľЅďυсӗ\x83ѽǼďÍØƖȓķԇӞTӮ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϓĴнƎW˻\x8eѽˬ\x94-ΖȢȠʅϲҎǰҐĢͲ·ȸ¤ŐǦ¯ʡøǲ',
                                                    },
                                    },
                            {
                                        'name': 'NԣgȏįƝ?õCƚ˨Ҵʦë`',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ĠˏӇʄƞҲɄӿƾs҅v¹ÓωƯˆҕǕγ³zǡºεϐÇ΅˄Ѳ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѽ)ǷĺбҫοĝΑҝʺɛί±Ʉԟ\x9fċдϩҪ˔tΫѹÿŢѳҮi',
                                                    },
                                    },
                            {
                                        'name': 'ѨѽрɂƍϢˑ¹ЭƵғҁЦȮȸж˓',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'nЊȝЧćύҴœэ\x99ԎKʮѬ\x9eȘДҡкϊiҿÅӜƶ.ӀƬÝѧ',
                                                    },
                                    },
                            {
                                        'name': 'ӨѓŚϑ0ΞşԕēgġóǰĶˡӠʧӐÇFўѪЉÉ.ΰ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7308154589973011776,
                                                                            -4781438936917060081,
                                                                            -9098910562825654416,
                                                                            3565010080675618722,
                                                                            -4598129739257287510,
                                                                            3248081126310665274,
                                                                            1962010709150581415,
                                                                            -2576358737808409416,
                                                                            9159656316299602379,
                                                                            9190340962900927057,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '1ǈӢӛʈʟζͰƔ¹û˜ǣͳӾϹ=ӮԆʐɏǑʏʗ®ɚ\u0378ÃȊӞ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3349537153162189993,
                                                    },
                                    },
                            {
                                        'name': "ҠsήűԪŻοÜƆĵǟ'Ӫǉê>ӱɚ\xa0ϲϔѴэɩhơϜǏɼХ",
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033542.325759:+0000',
                                                                            '20210327:033542.344712:+0000',
                                                                            '20210327:033542.361345:+0000',
                                                                            '20210327:033542.379055:+0000',
                                                                            '20210327:033542.396441:+0000',
                                                                            '20210327:033542.414379:+0000',
                                                                            '20210327:033542.430892:+0000',
                                                                            '20210327:033542.448314:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƓΕĎѶϤĵCɯīŷʏɃņҖ.ʻѢƷӊƱҌŽƜАбĄ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033542.945652:+0000',
                                                                            '20210327:033542.965778:+0000',
                                                                            '20210327:033542.985369:+0000',
                                                                            '20210327:033543.007947:+0000',
                                                                            '20210327:033543.031012:+0000',
                                                                            '20210327:033543.051785:+0000',
                                                                            '20210327:033543.071851:+0000',
                                                                            '20210327:033543.091812:+0000',
                                                                            '20210327:033543.111412:+0000',
                                                                            '20210327:033543.131861:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'οΥ˟',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033543.235274:+0000',
                                                                            '20210327:033543.256101:+0000',
                                                                            '20210327:033543.276355:+0000',
                                                                            '20210327:033543.295627:+0000',
                                                                            '20210327:033543.313768:+0000',
                                                                            '20210327:033543.330959:+0000',
                                                                            '20210327:033543.347740:+0000',
                                                                            '20210327:033543.370847:+0000',
                                                                            '20210327:033543.386000:+0000',
                                                                            '20210327:033543.400629:+0000',
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

            'identifier': 'jїλƸƠ',

            'categories': [
                'configuration',
            ],

            'messages': [
                {
                    'catalog': 'ӒŲ',
                    'message': 'ε',
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
            'name': 'Ȍȋ)Ƕ˼ƲǇ\x88ƎѺБħ҈\xadˆƐ\x88һҏɨȟʃº͵uѽ®дȟҲ',
            'error': {
                'identifier': 'ҁҚϝɸ«Ďԛϟʖɾ$Ӄ\x9eEʻĖ²ƲԩͰӗʰΎҜģʨʵq+Ϫ',
                'categories': [
                    'invalid-user-action',
                    'configuration',
                    'invalid-user-action',
                    'invalid-user-action',
                    'os',
                    'file',
                    'internal',
                    'configuration',
                    'internal',
                    'os',
                ],
                'source': 'ɝÀїĔϒɠμŉĽΊòΧŻԐƧˤЄӷГѷʿђԧMlɯԚʜ1â',
                'messages': [
                    {
                            'catalog': 'ɌǋȒǿЄġʂЍӧfǌɅ4ˋdʆƎŪţјƫ͵L@gяτдԤǈ',
                            'message': '>оӧþͼƲӿʫƙȊŃʾД@ӯǜȴĀȑť͵ЯȆԟ¦Ȱϔ²ԁй',
                            'arguments': [
                                        {
                                                        'name': 'þʽDʚȡĠ҉ӍĻJԋŏҴ\x81É1ϫɠ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɗͺҋʫϒĵӎɷU΄ҐǁȁҚҦДŲ\x8fѣːņÝϋлè´êͳ˖ǵ',
                            'message': 'ťΕǃƓ˗Ƿԏϡҧ˂ԌŽĞ9ϞΝХĢͿ\u038bǟƣλ0áƤ҉ǟǙȫ',
                            'arguments': [
                                        {
                                                        'name': 'һ`ƂŦȯƙӡЌƂȳϬʕƚȎ˯νŵė#˺љɲŭԉȠϝʑ˙ɴƝ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҨҫϞĶĺgȻʊƧӕyʯ`ΝȕʣѿԢ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЌşӀЂΥĿ4әƙŵӴɒbșˇĤιɵˈȼӡӨ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5120936882383152786,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЈυŀӨĞͰǋǸ˓ъAқć*\x94ѦήˎϵΦõǪƵņј',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -99697.45791948379,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ůíɱɶӝɲ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033512.778157:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Óѕήǐԃǜ3¡ƎʠġɊÖà˧ДŇð\x9bҸΙɓ˰ː\u0380ϣΝμϹΔ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɯӄ.ù;ѢҩϢ҉ѾЕ6ƒ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƴWїқȺˢĚ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 596984.3418205325,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɥʱͳÄЊƛTʏƊͿҚĦ(âƆjԋЁǽŞį¬{ɾƅʣŜɐ\x88ʲ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033513.094114:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˗Ѥҫ˛ϻīϸĢεŪʀɔшƢŢҡ˔ʂ÷ŐkŁď˞ϏБϗʷɻɽ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҊΜҽ\x85\x8fǂ´ʰʹ\x9bϳʣɢĔğƴɂȧџˀΈѣ͵ҝǞˉ;ˌЊƘ',
                            'message': 'ԛѲøϬǰ˺ҙĨӋɡƁǹХɸЇϷҐϺƊőЃήǜ΅ґϗįЍӪʝ',
                            'arguments': [
                                        {
                                                        'name': 'ØФȕƱǭȨΉȆԗʤȀOͺjC\x82³ɧʈǇǩ:һνТцˎ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ôȋʒ®Ⱦʏĕѫįθȅˮњɏũ"',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЛƯƮɘ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŦkˏɄLӦ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɇ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Șϟʧ˘Ǐԣ*ѯοЬŜӏΏEҤǕGƼΉɛăѱȆǝѦɍǘɭʢӋ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ъϵυÜĈ\x99ҸɺӞy°ѧІ×ЧθizIEѰƲЂŊɏӤƭӗ˚ԣ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3813738062264676300,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȸɺˠҤӃˠҭОƒɎԨ˯ϻ˳ˤ\x9eƧ\x9fǤȈųн3Ҙȟ҆ȲʹɋŇ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 865213833569532127,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ûϙΛ5Ӯ˳Ǳ˒ƢњԐгǝŖǑсQŭůŅüάέԓЬʢІɏȩ$',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1178306925422219376,
                                                                        },
                                                    },
                                        {
                                                        'name': 'IΆ˸\x8bӽ˞ǨԐҧƋΰŁғǃř®3ԟӅʫ\x86Ĭɮ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 707015.1472962074,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĤĞƓЬάκȆʜġьԗ\u03a2RԃÂȼƂw',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2649475820665985276,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'åǿҕƦќʻх0Ш5˖]ȥĵϧƱԩϛ\x98ϷǄƛӓӵ˨Iμ°Цҽ',
                            'message': 'ԛĸ\x98ӼκƤːΥΧɤ±Äύƌт˶ƫёψȇ˅ѴùΙɚεԟǘЋɚ',
                            'arguments': [
                                        {
                                                        'name': 'ɐɓҍŴĳΕʉΌOÛZӹȢǁӞԚӛz',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 9080034494400130491,
                                                                        },
                                                    },
                                        {
                                                        'name': '˲XϏԞȣʧ\x9fØӍêӿtǟͺ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˬʲԒÅvÖŤĨȖéóȀž(ƛƏEĆ\x88Ѧŧчň˺ĕԠŏǖNϷ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ũǇфұÕ¬Ăχ˩ӶʥƉkêӱʼ\x81ӒºȳƀӒžɛ;ÕԛÒԛ˚',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033515.333213:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŐҤѕҘΩΆȒҭȜ\x9f(ҭԔƮOȖʌЎԡpɍ˩ЎʟfΈʄ˃ѹȳ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǫҸȯӭǝ8ȫԦх~ĳӎTYƑƸǮϗŻȠ\x82',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϥD~ȀΤìʁρȝЬƲԋЧN]ω˪_ȥÚά»ΖƢȐԩƵǘʑư',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɍ)ӅʹςćʹΙʃ΄ơ°ѱϵʆ¹ŕf9ńˇé҇σƱª',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '²ɏΆĻНЋиǋͷť0',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʧΥ\\Ϊ\x95Яҫˁ|ϼĐÝφ\x90ȃ²Ʌ\x89ƝĦϢҴ§ęϲС\x9atЦù',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Оèέ]ȚЃƙʳΠПȘ!ӡŞҏȘпɨĿƋэńƶԡӦѮҺ˓ũȦ',
                            'message': 'ÈщȄҔĬԜʈԒшϪʤǥӎơǽϸǙΪǊÞӂӱк0NӹҡʍΌɹ',
                            'arguments': [
                                        {
                                                        'name': 'мяϐ£wɪȼʞѺӝѿćЦO¶˨ϼф\x9bʟѥƿϺΏ1ζǊ]ʜɟ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ']˳ӔԇʺŻԕ_',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 649773.4875803333,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѭ`ǣöʔϏɀдÞǼԐǗьԃ\x9fԉ҄ԝ\u0382·Čîύƨ\x90ƼȿӪɀѴ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ºϱ˵ˉLƏNžÝ\x86ЂƊǣʾ˜ΥВыŵʻϮǛԋRÏÄɨӽˡL',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӖÎŐӞǒªΜʝ·¥ʲ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 611662.6202976168,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѱȁũќѯŇnïӗӨɫ˾ǠĆ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Uӎ"ȉ˄ǩԄĴҚӜҮҷäʁ˽ΆѢĜхѬϽȋēĒ©ԍϹЌѠτ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǜќ7ǼɔзӡШСЊ<ĥҙԂƃзŝҞáʩӹɒҫɿʊΖ´ČȾ¦',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѴэҋӾí҂ыʗʶӐ&śΔЛϫ҈ƙű˟ɐêBЏӃȖƋǅѵӪƁ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033516.802332:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӅƱ}ԥʖЊɨӋĺӑͳΦŶϰӏЅΪIӹǮʏǶɊÓ\x80žϫkŚõ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ŏǃԉîҳіʒʓԬŖͼϭĩӻeЉƱϫԭƬƿ˫Ǯ\x8aϺЁоȲӀ~',
                            'message': '˻ġЕȢ΅ҋľ;@ϩӋśÇα˅Ǘɮɺš\x87ŝǓÖʗƚʅņǡԩ±',
                            'arguments': [
                                        {
                                                        'name': 'τĘƄͲѫɶǐ˒ʻƴ\x84ϽψΦʈŇǏƤμˮ˫ƟºʛĹĻˍɫÖŧ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӸƗŽƂǭƑǟЃӫp»ŶӠӧзҺ[CӣʺƎŨɞϧɥ¬ƼͳѼļ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȷXҥЖƭ˫ӫŌ͵ӝԟÞЦɥҡʰȚīЛӱΌɎԀ\u0378=ɖҹƾѹđ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033517.497400:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʅȹȌȨЧϲǨȹԑƭȒ\x8cӿœƈԘѶŹ҇ǌȱ)ʊӆD`',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 484924.6244678751,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǝ,ҸњȨŸÖБˆ\x96êȉzŠԁӪĄЙĿòΠѵʖѼҡϰĹ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'хʍƮƽ҈ΌͻԉƮ\x97ъɧųǼ˼ǧӞΆĵЬӈӁǶλʞӸʆӕΊŃ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033517.710575:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9d\x8fʍҪ\x8bǜѵPƃVϭčǟ\x97ǉ\x93ū°Ƃϼ.ʤǊӷӱЕ˾Ɛҧȵ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Џ=ƌϠѲͷ˜Ԡʐ\x91,ɴт(ίƶОМɐͷFŝɮѩŠȰӛL˸ǖ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'đʹүΛģ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3903255258409388359,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҧӮѠ˦Ł\u03a2ΞɺҘʮʹӃȢѣʮ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 736223853516241405,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΛΠɜĎȱΩɸ҂ЩʶƓȵĕԆ˪ʀĔʏǙīįǨšȸ\x9a˧ʕЂµl',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϙΡɟȐˆ˾˩ˎԠςäʟӷϜѴ(ϷӉƼӝԉƹl\x83ȁϩFҖӍŰ',
                            'message': 'AɞƏƓ˱ǲ*ԟō΄ƳǍЇΝж˰-ðÁνȀԎǁǙ+ñςüӌ҅',
                            'arguments': [
                                        {
                                                        'name': 'ǍԅˑѥЖˢѮϫɐɡ.ġͲÃɒҸӉÿάЇΔϸӈřȍȯйҲǨŒ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѲԣˇϟϰĽϣд*ω',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Гј·¦ʖӄЏ{ŒѦǧGњбôĖҵ\x84˸*ƀξ\u0379ĒǛӤϕŊѕѴ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƅԎёɇ{ǰҭëȏӗ͵ȲΎѣТ˘ͷãũЕЈ¯Ë˧Ç\x9cȡǁˆ¦',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'qƝɚÝęĈAϲ˗ļʘЃǪԫūԖƆҔĩЎȱΛͺɱǤҮśȜфΗ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 51485.831083718425,
                                                                        },
                                                    },
                                        {
                                                        'name': 'KʌƱƊΗÀ)ЪҠϑĂŻĹβγěɫȥβЄȵҋɱÞҞàԗ\xa0űΛ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¬ғŽ¶ϲʶӔΛЦë˟ӈ϶ȘиԖӱѢѿɰÏƮуŷΉԋŪ¼˛΅',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033518.973930:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǐɷƭ8҂+ǱԆ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 844456.6354834855,
                                                                        },
                                                    },
                                        {
                                                        'name': 'pӿ˺ԝƠώԫðӦӴӚРъƤЋŜɜč0ȍψ˃ɚƬ\u0381C©Ӳ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3651942714254049183,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x92ѻѬɝҍΤêԈʹŮЏʯƦΡƅµϺӞƳϘ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'bˢҘѼɓХ&=ÜšЂėʤ\xadŖԫҳŷðǶϒ˙{ПuҺÿIķ©',
                            'message': '˚ђшʕˊЀȓӢЗƭнġĶĺĞƗʤQѴ.ɲưΰҗǄӰŮǙЌԓ',
                            'arguments': [
                                        {
                                                        'name': 'ǔѯӦ¡ǲa˕˺ҡƛŅĹɤɟȊəӻԝşÌҿћǯѺ˱ɣʾ\x8c(ē',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȶŭ˅\x85ā',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'SƫƚѳŒ3ǩǊǔˤŅҾЏϓǁԡҖˎϼp~\u0382ԭɪϏЙÏȀҜó',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɷǖŋĬĊʪºѴӆ÷˸ЕȅÆȑρϲϋļӀʚ\x8fǫƖ\x88ɪƇkŻҽ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 193219.34496230882,
                                                                        },
                                                    },
                                        {
                                                        'name': 'WĎԌɯ·ʙԛӵю©áԀӢâʄȊςȣӈËæΑʣѰů',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Íˠ˴',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǒĀʼőƧҜіūũƢƖɮ;ɃȽɌЁѿɸǫӇ\x9dɨǰʑęAÚҾѿ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '[еƒʡʔŃʳԂǳμǶƷϞŐ$ˑİ˯ςǓү\x8eȦɽ¥ǝ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -88240.5259743129,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɐʰÉϴʄ϶Ǵ9ӪάӲҊ˘ρӐsɡʃ&ϻƞʟɽ˲ɒӝǍŝԒ˹',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033519.814017:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǒʟ˓ѧɈŗȉϗŰƹADǛȼғ˗ɂƤβǏǽˢϑǥʕņˎ˄ʉҩ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'џʞ,ӚЂƂ¦ŚĻɰϔ˂ӯǧ\x8cĢȠΔԑtĞIɪŹ\u038bөӽĢӑ\x89',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ƭĉʈ\\қȅȶƙƟûŔqnɄГ˔ԐȢȘԘεΏ΅Û¨ǈҝ8ʉҤ',
                            'message': 'ɦѴɫĩˁЀļϵӸʵăˁΨțʶʜәŘɖˬԒǈŃҭīΥ\x86΅Ʃų',
                            'arguments': [
                                        {
                                                        'name': 'ŔbхӊȈǵέ2ϣȳÈĕȗӦɎǸȋɩKŗÄĿϽӣŇҧԪƱĚȉ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x93ľč}ѠϓvÆҘǞǕʕÀơ-·χʷfӭǶŷѸΝѷˉļʗÃǯ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Х˷\x86ɻɸƕԬϰǥӘώvЦʆŽɴ\x91°ҨÏÐ)ҌъΛҍʜδ|ɓ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЊёχʦΙʞэʘˠŻ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 403229.0426346062,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɋȱήψҩЍЗŖćʯȔϠў-ƊҟØ˃#ҩЗţ˞ĺЊǓʵѬƷò',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033520.348172:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϥǇfKԟӻˇȚLɨӪƥξҷȁƎыƑςūşʏķʱϘðӦји¿',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΟĦƏ˾ƎƁ·ϫɇФƱЍӵɗ\u0378îӾ΅У\x7fǾț',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'иȆĖǝѮ\x84ʈǘưɇ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Їʘǘҋ÷ԭ·¨ƁʜʕFƢȑĘd҂ȋšҬ*ÑԑœҵƢʐȿҤΆ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4973725314356588651,
                                                                        },
                                                    },
                                        {
                                                        'name': 'τ*ԥΣӣϷв3γͿȎȺiωӁԃΓʂћҝȪɟяɸþÑ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƄȴƨŮƛҰßѱĚƊȻƜ7\x9cОƀѝȤѶɽĊďȂ(ȔƐѸŹȗÚ',
                            'message': 'ΆƶrˠʮΠҾʷɨҍ¢ӓНҕӐоŻÓɆŅӋќG³ř^эµˊÉ',
                            'arguments': [
                                        {
                                                        'name': 'ӚȇɍѼːϊìϓШҊӐÅ˰Ԩҳ°įшķʊųȞżЍΕѠԇ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȋȻƀϿ˯Ǘ˹қƛɆ>¹',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¸ʩǴǿbӷʒĢǙӳȔˡνиǍҊ͵ϛȪϧˬΟ°Ś˭μǆÎҘ҄',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -204915957609491264,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȹǰ9kɅ6Ћ¨ɮɈďȏӏď<фɫϔЮвЕūʯǐİ\u0378ʪτɧс',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȭɞÿͷȷǁЙʩαęɄ҃ʚ·\u038d҄ƂƤXĢ#лŘҥӢҏĀ¤ȊҚ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ό\x94ӮЬ«ȱɽʡёǙɬȺǡŕѭӜȊ®ˉµȦ©ɖ¶ƘΚ¼˖äұ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2767656051101945322,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɕȫ˓ʍԖµĈĭϫɗɄ˙ǜҚwǢɑΪБîÌѲʞȊҢêβɪĩ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȑi˶ͱęĪϟϠ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӒˑŎÄ˽',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 784159.0334665057,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ХƵɐ˕ƣӊѶ¸ԞѫŽϢÏʊͰŭҪҞȵҵԖ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -80715.62700550233,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˁСʺǎđŎǣMɵΩˌφɟĊďГɷ\x97ӣȔΰǼʳɜо_ОӼ˩Ж',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3484862260261183869,
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

            'name': 'ĄРħ',

            'error': {
                'identifier': 'ʃàkƳя',
                'categories': [
                    'network',
                ],
                'messages': [
                    {
                            'catalog': 'vӳ',
                            'message': 'Е',
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
            'event_id': 'ɹ\x84ʨԣɄqƑˊɌΞȤh˺ЕŢǂ˚ҝʣǙˈԉίȱӂґїɃʊѢ',
            'target_id': 'xŝƌӊęѕΓȚŔϳҍφС`ɗѻÑѿԭĿ˹ЏƦұƳȜŧˉćӑ',
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
                    'event_id': '°ҸΪЖӠԟοĻɆӱѕπˍɤєκ$<ҸˮҥʐǙΘŬƶéċɬȵ',
                    'target_id': 'ǎʶЉӛӼLˡΒŷď΄hνƦƐ¸ÿ¾ҘʩɣӂǺϘXȘѓǆ',
                },
                {
                    'event_id': 'ӳƺ\x96ŭőɒßԪh_ШχιԆƱ˂\x8eľԋIΗ˼ǾԋҽMŲǀǷȜ',
                    'target_id': 'ϝϱҜùҷ\x81ʆʹҬԐúƸˌȁâȇŰȦЅÊȤkƐE*ɺɳΏăÿ',
                },
                {
                    'event_id': 'ӉƥӭϽȕѸԌΦĸҷ\x93γŻǐɴŰPƖɹǛDŒ\u038d˹БԥÑƢӫӀ',
                    'target_id': 'ɔȚʿƋɂάʓԆɜXȋȌϟɩӉľġ\x82ƋƎŽƤ˝NÉјӮҥȢŀ',
                },
                {
                    'event_id': 'ѵǐÛÞʚӸаƊëɸǞɔʺpǜϹŐΰɨ!єĬœȟàӬȶςĩǢ',
                    'target_id': 'Ā˺цҲƉ%˙ŲԥňƵάʬ´ӮΒӓǴΰ\x87ŀʌԪŭǺͰǽƍѯӕ',
                },
                {
                    'event_id': '҇ԃѧ\x8cҋ¤˴˼ɢØéĝsȋƇcrЍϼĠæϐϚӓ\x9eūљНЪ˰',
                    'target_id': 'ҦϒʚЭƢºµ¾˼трӳȮҾˍ\x8cѡ\x8aʧŴϚѥ˓ÕԌͻQ¼eƩ',
                },
                {
                    'event_id': 'ɇϺӴ\u0380\u0383ОŦĵоBӝĐůĈʓНǍƊЍæƪnӣ˟ϖӢөԘíæ',
                    'target_id': 'ȺԬˈҘĪиöяΆɧǤǞç$ԧќ\x9fÈõɱфԪʜ×ϒҲѬ\x8dϙɈ',
                },
                {
                    'event_id': 'ҬԟҶƀ\x98öηԂˈämÚϚʏƧѣǐûӥĤǦӬȠǴěFĴrƦԟ',
                    'target_id': 'þѻҙAƪ·Ť\x9aҦҌӆÉɗaϜǦá¨ŖQʦТɸȅξШĸǰѤӪ',
                },
                {
                    'event_id': 'ҬӠǋЙǣόѶƠˤƛΜͼmпɃʛЉӠϝȨҢԚĒˣϔӎh^ԌѲ',
                    'target_id': 'Ϋ˺ŧρĴ˂˥ѭƟĦЀӴȕɓԥΟĸĐϠқȮʁФķȴ˅ȎΰɡӖ',
                },
                {
                    'event_id': 'ΊρӯƖј\u0380ƾXƞ҂|ɷάΕƢǠјιсѕ\u0379҂6ɭȴƏˇǠӦ˫',
                    'target_id': '\x91ŏύéҩűČƐʍɐЊȞɪȽКɝŮ҅0ɟUȦГȣÍϨͿɓM*',
                },
                {
                    'event_id': '<˪è²Ğӊ҈rҐƘȃbΦƚƹΚĖ(ąèұ\x84ʄǭDɭӦȨĲǶ',
                    'target_id': '¢ΌΖɶȨˏј\\\x95?pǆӝϕƬǇʰϼʸϼјʯѧfɊ*ɠΟƎ˵',
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
                    'event_id': 'ȂЋͻ$ƆÂͽȦʙ˗ȡŤŞJ:Ȟ\x99ŶKɃͱgҸ˷éŚӓԍʇ\x80',
                    'target_id': 'ȦӜġʦɨǻxɐȩӖԄĹȖł\u0383ϛϞƚӃΎΟÙҋѨʗлŗóԢВ',
                },
                {
                    'event_id': 'ȃ×ҵÅ\x87ӝʯƜ_ΤČǷĄɇ˷ˊәɛ¸ƭËˊǭԑȩʂƌĻƾȴ',
                    'target_id': 'GŰxТҼöƠǧ\x9eħҳɸBʻȮǂÚȔϨčϺˤ˃ϮoǊΖӉйЮ',
                },
                {
                    'event_id': 'ȜǴӰÓʅȣɆѼѫʙѽѢĂҎύοÜƝƿũòάș҇іԞ~˭Ʌљ',
                    'target_id': 'ǵ¿ЁKǠȎΝʻвɼϞзҨҪɍпļѕ\x92ӏɛ«č3ϥĢǧͺɯ˰',
                },
                {
                    'event_id': 'ъʹҏʲȟоγΗ\x8bįĈ%ӔʉÙtљƛ\x81ԂȸÆÞɻΜʁȧ3Үz',
                    'target_id': 'ȇ\u0380οΒӻ²ųŖˍʏc3˴Ώʂ˃(дͻ¯ϗĬrŪǡʅѢϨЮŒ',
                },
                {
                    'event_id': 'ҝȯуnѺƯγʲϩçϽπùЎ»ĻÊǍΩɝòçZ¥ЇЏȭĢÚϤ',
                    'target_id': 'ÚΏʪӇ\x96ҩɅɎʡĦѯѠÖ¬ʸχӸЉɖȑҐήėɛƻȤώǢˡԟ',
                },
                {
                    'event_id': ',ҔҤԍβʗʵ·4ǅʾǒƧϝʞŐҝʽƟ\x95ƇяĈsѽĳѦʟӓӰ',
                    'target_id': 'ԫϼαȊҫǫШƬɈú³ȗҨѮʁπÒǘƦЩ҇țҥɖ\x9d\x9fԇUʒ@',
                },
                {
                    'event_id': 'əЫʷ\x99Ήȳҝ\x9b¡ȹʷұ&ѿñˠȫßǮӢſ\x8bŲˆƩ³ʴěĔӉ',
                    'target_id': 'ȅԨʡǾΞӋлЩƦ£ǒȨĵǈ\x80ƾǺēԠɼʿģʘ\x8dǳɄɆŅќƴ',
                },
                {
                    'event_id': 'wһþ\x9dʓ}Ԅȸ~ςŪCȘєԀΛйͳҎǼ\x7fѢÀфʾƴ\x98ȘǠÑ',
                    'target_id': '˚ϾÒåŕĶ!зѵЊǧȕІʵѭGΦѝȔ`ɂˡӀpϻɤСϿҷԐ',
                },
                {
                    'event_id': 'ưԠ?ѴǊʯԒ\u0378ϊϫΊ\x9bϗƵˇȑƂˬӺˠЊʢɻǃķԟ{śп»',
                    'target_id': 'ĸγưϛӎϸԮЀʴþƍёӄʻȀэƬλd\x99ԪӢĝӨϷҍǊ\x88Ǻԋ',
                },
                {
                    'event_id': 'ƄÒѶʈſǡâΉԢȷŤӡԣҢșб¡ȰӇǞȊĳǎƶƃ\x83X´ÔϠ',
                    'target_id': 'ѡ!ϹǊцšűӣʦ\x99νҁԣ\x84ɐŴӵɶԖÅ®˨Ԋ1ĬэӖ\x9d±J',
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
