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
                'lȧ:ØӚМʖѼɱӹӳϞӁʗ\u0380ϰЪŠ˄ɰͽї˔ȡ\x97ӂ9ЪȪư',
                'ɁsĆӈΞѼӚѢɛҧǋɺжȤċşҗŇϐĞIw˜˥Ñϒā˦ǅӹ',
                'ɃêϷăG<ӸʾҖĘъȫӕ;µӰϖЄȉлȑ˲ʜƐ·SǮРȖΚ',
                'ēόÍυˏpˆ˾ɐԪ}ƅ\u0383ΥɺĄҳċѯЃAκőĬȄŲǄĿɚЂ',
                'ˤâӇŇЇ\x9e˱æƑĭψҭӜĞů¿ƕǢƽҘҼȮĻtӨDӡ\x9bоҟ',
                'ӰȍүВʨҢ9ҎбγɯӳȒÓȰJȼģһͰˮǝŮϻȕРʗђBh',
                'ѡʢ¨ʡƘбӁçÝşÀΌˑпШʀƕ\\!Ȯ²ŘɇWɃŭĚ¤ŕϽ',
                'Җ\x82ƨӡѹųįKRЯýфƌΓˇοĐұÍˠέӨӒȤɊ˘ƕʕɼӫ',
                'ьӍȌљѪè˂ǜпdΰƯԒƥ˔ԇ\x87ˋɂтԐāҤѯӅτʿ»ϓӺ',
                '҉ûѼPϙԨʌϨ˚ΎɣǵËӌ¨ƿηͽАQ˺ɧӉϲäҋ˶ǀӮɞ',
            ],
            'source_id_prefixes': [
                'ƴėʴƘƖ҃ɐӵԢҤǴɊʙ\x90ˉƜЏϰρҦǽ˞ȷƎƜƹїӗÜʶ',
                'ÃÊɁ\x8bºʡΎ˘ІˬʶЬӃǿ\x87ʹԗŅЏǂ˵ƈ\x8aƗŘŞҪ˗\x88A',
                'ϼԨŽ\xadАѯҊʌ˂юӰʉǘЎɍ¼ʏʫŃǻȷkϫˊʶŦɞǬƼʌ',
                'ĩȚƭѬҢȾԈœΚΪӐǁžơԗȣӗҪȸǌѶЪӭϺӷͽȜΊԛƉ',
                'жԊ|\x99Ĺӽ΄ʖˑҗӴԞâ{ǈɮƳҷƅʇʒηȼƬƘфŦѕԏБ',
                'ȕЀҸê˧ӮʗёȱĎÔӬʾɨÉÎΐрƉˈ\x8cїɼ\x8bѷĸîśǀӗ',
                'śӎðԖҡFµÉ˕εŅ\u0383ӽÙWʁчЬбӝrΨbҮ§ɩɴʔϰԞ',
                'nĶ%MμΓӨġʚƥĆMΕʺòӁiҝρӂgƅɚʜ©ȓΩӖжƈ',
                'ʓҨсŨõʠȼʹ¯ӕȗȥɲŽbÏԣſӌ˻TԜÍĢҜ7ĴƸ\x9dś',
                'ƁВɺӔԟǼθоьȩѢˣζ?оğȀ\x81˱ŠҖҀҕʚѽά}ɭϱʜ',
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
            'action': '»ӥςˊŐĈƄӆ\x81҃ǘζȎ\x97ȧԘȆƣǫɎҺǀМхėɓʲʿӊɕ',
            'resources': [
                'М\x8aӎƎԈėАϋ¡œĕūеӰќѬʞіѥtʎΟӍЗɴъȹҳʷҽ',
                'ЖԗĬȲ˂ϴͺӃʅéČҝʤѢӊЗγßíҡ@ǌǊԮԧсԀµʃϻ',
                '\x88HȂнϹƐ3ˉõҙӔТ҈ϑϻѾԞΨͶǿμJ|љȣÈĨййº',
                'ʝ',
                'ƓʜǼǹ_\x8c\x95ƗԩѽѼʲԡ¤ƠĪĽ£ҝÿMʹϩԕ˒ñţĩơѬ',
                '\x8c˟ĕ҄ɒψ|Ύ\u038dǳūòДˤВĆӜΛ²ðnãͽƎȧүҠԋsќ',
                'ȼS5H#ϋԅŋ=\x98ŭ˘ѲƀCɏɯϸŃŅýɳ\x91ҖѩťȒÍĜ)',
                'ζ˳ǇұaƉЛӰÝȄŘȵӔςωɬʳҹoŮ¢ȡ\x8aʰƥлģɁÑ+',
                'ɛȊҐԒ\\)ɅȫҫʧѷΪӗΏԦѪҮϓňȷЂ˓ͳG\x95ԨƋύˏυ',
                'ˇҞΊӘ¶ӟǯл˱ͱϾ˗ʱºԢӷЧϧA6ʭɍ*īЯSЮǹ\xa0҈',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'ɩ',

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
            'name': 'ȷ¡ɻȢћҚ3ŰˢȱÔ˴ЍӵŔҔɊˊ˱˹ΩεԤӈҴӧǧԔŽˬ',
            'version': [
                -7250152276870501748,
                -1300236614571997286,
                -2991472847305268353,
            ],
            'location': [
                'ĉкĞĞȣͺДƝΠʻŷʗҙɱȓӭʏңд˶ʦǄȾԑˈȁ϶ȝӳԀ',
                '˒˖}҂ċŐӁϡ˓ѵÞǲφČϝōÝCɽñȏŦʑɧȄǭУŪѫȶ',
                'φȮԈĦē\x8aČɝȕƸǆλ˵ф҄Ƌ˙ùŠʱӿŘѥͱϨȮӪŦɥ\x99',
                'Ŭ˘ɺŜӼüўԑџtμƥɮēқèѪ˕ŅѹȔɂӨ`ӁɭҦöˢ˽',
                'ƓԐƨǡYӃǘЈ˨ä6aҿϑ[ǿ¿ǔǩ˭)νϳѕzƦŮɦϩ±',
                'ǹâxϮġЮ˰Ĳѱӱө¾\x95ΐѪ2ͼҝҞӼӕʞyҝȚϘϳʧϔҭ',
                'ӖàϰȧϿҏçӅƶԮŦɎ\x8a)(ӲӏȍʬɘȠˢ\u038bѩǥҵЂɻӱǩ',
                ' ϵИçҺΣѫɁ^ѿџǾNĤQ\u0381ϕɞѨцȞ\x82Ьɹ\x87Зӫ˟ŋȴ',
                'ŵ&é~ѹʛɪƉʕϕѤfǼѷȿǚӨθ\u0379ĔˠѨzұČĥϽԦ҅ʤ',
                'æӨ\u0379Ǖк˃ƲɱŬӘԙԕЎлÃϨӐĻђŹÔŇʔʧιˍĖ9ӂҶ',
            ],
            'runtime': 'ŌȄӡҊÔʪ9ҴŧŶАĦЕǽŔȶȦ=ћǄБĴvʋƆƍ˞ǽȠȹ',
            'send_access': {
                'event_ids': [
                    'ӂҘзʉǦηȣɾiɝ4Ԣԟ¢Pː\u0378¸Ĉў\u0379ӃǗȤȩӡƘІΰӗ',
                    'ΏєӋÞƠ\x89фʞȜŽ˨\x8bʋЇTăƆÇƷǜ[ђēљȃ.Λ8ȫȝ',
                    'ËҤˊȸКȦʩ˩ӻ¿ЃȨҟιҮģȐiȃ´ɃʤӸWσϊҵѬưͻ',
                    '˱\x8bӱǼƂӕŗΣΛқћ#Ǥɍ҅ǣ:īԡ\x9fʞҏ҄ϩҰˇ\x95Đξˇ',
                    'M\x9bŧϠƞƘȕ˷ˡüςǪɦмʥϮŲΞ\u0381Ә\x92ʁȚϙҲʏαǢȋ!',
                    'ǉüϞ˛ԓќҰϵӏɕŜɯ»єХӺǕȉ\x94ǪҧÙ6ɒŪҴІԬϟw',
                    'ΰǵƦđĎUƮĤˇҙǚΑqʞѸϩǉùѢèΎӘϷI6JьԓǬ˦',
                    '\x9fŝΧЗ¼˲{ԈΌӒτ\x80ɩɈǛӈƇǷļЌĪʲ\\ƅӷɂÈˣƞ\\',
                    'ŒζщϭǝΆЇźȵѲʈУŌ¡¨ӕ\u038bɖ»ӐШʽ6ѯ·ŵ;ѐуˑ',
                    '\x8cdĄ¿íҚŌҹrТʯɤы\x80ƼΏЉʭƑȭШłâʗ¶Ʃƾ\u03a2әі',
                ],
                'source_id_prefixes': [
                    'ԏӹʚΞÌN˩\x98\x9bÊƞĸ˳ǡưΊҽ(Õƙ˘ǄҥÝƩÛшlîΜ',
                    'ӏҮƳҎʏѭΞ˵ϧǍчʭÃˑҁŇɡ¹ӂ˷Ș˖ŗзшЬҵ\x8dżʙ',
                    'њĨӰϻIʫԀˌӜ\u0379?˱ˬʓŀѣũĘԉΦŵ\u038bİĐÎͿҧēÛЇ',
                    'цʡɧJɬӬ˶ҐΥԈʇǳϡʠӧÎ~æȻ\x9fχЅʹЧɎɳƻ˜эɌ',
                    '\x8dÏΜѨįG¾zҸƀх.R[\x86ƹѾʕЀҩ҇6ѵǧϵɆ¦jǃЦ',
                    'χӨ\x9bƚþˏυӢђˋυĥԍˊƌЂԏ»ыШŷŤԉÜτËgŜђˉ',
                    'Ѧҫχǳһȿ¥\xa0ʌĿщуғÚή˦ȏċƵΔYɓȂġėȡǼӌҘǲ',
                    'ϐ˙uΑϑЬοŉжѨÁ±ǏŤ\x8bɇį{ӟʲ\x89ωДƤŤÑǐâʶӲ',
                    '҅©+Ĩ˯ʿŻԗӢ\x92ļϮ˹ú˚Ϟ8ѫηԍɿ²\x88ɾӅƙӅ®Ē1',
                    'ΑΑоʯ˶ɽƠСрřȈųԭˬӵȕȶӌΠԙʤ¢ςɢΞǖϤȅǹɀ',
                ],
            },
            'configuration': 'ϓ\x98ǞǞźϾϣʀÜqкͺ҅fДťК˔ɀΚƘʪӉǓʭѷ҄ƞΔɩ',
            'permissions': [
                {
                    'action': 'ąůʾѶϪ#ȖŜ\x8daũȓo\x80îԢȥ\xadĺ\x96ˎʔŰѻɃ±ŀˮIҭ',
                    'resources': [
                            'áƍϖȫđǴNȘǡőԒȝƀʦĘǕїȚϩіɠĪ¡ĳɄ+ňӄƳԘ',
                            "ʎ'ĠΰȉΦƮȗǟƦ³ԖʡϨ˜ŸϟƌĉЙԢ\x81ˉpɫфͳľȽҟ",
                            'ɪЉɉǔâ˻Ӧ)ԇӯåԧԗ҈ϗ\xadɍ¹ƨǤ%)sѡԜȹљ@ӶƱ',
                            'Ȳ˓дČȣˉȅϴg´ϸ!3ßŬԚrȺ@ǼζЗĕ˵FԆÊʮϧʺ',
                            '΅ԍpмϧʲ*ѥɽӳʦȝˊ:όL¤Ѩǆ˰3ЀˆϛӗƠƯԆФƫ',
                            'BΏӕɯҸ\x8eǺÂǸщNĖԐſ+ϛȀʜʓɾƍίȅǓԣзĮȎƫ˶',
                            'Þ\x98ïťԂбϹ˱ɲʍƄºҤӑÈ<ęȺ\x8d\x92;Ñǝ˺цĿĕȆǔЛ',
                            'ώҧώӶԗирʲ§ˀҥƲη\xadШ˪ӡҶўµ¿Ο§ǂȱϦћūΥB',
                            'ƩɅѠǥȵȰǹȴŇҞÕmԥӇÎǡǀ`ȺǗ]ɰʘʠĲțȢӴȆқ',
                            'Ǣɝ\x93ӥԤԇĔȭώϥ˺ΩɇӖBςȪȵ\x9dʓʊɤdʋÍżƘ¸ԖȲ',
                        ],
                },
                {
                    'action': 'ǵϭð¥ʪǦȥ`ǙΨϼї\u0379ӈǿӌÿȑǏŚ¨ǅӺɇР˝˜ӷζ·',
                    'resources': [
                            'ɋ;ҪŸTŘӲПѽɸǿРŭˀʾǵfǋŸ˹rĔё\x8bʯǝҀɿİŶ',
                            'ē\x9dϵ¸ǈǑñʆƸξԣǨǀŘƁϒαϴÜωԤ|ʸʵǌ˼ԊūӍԀ',
                            'Ć˓ǷʶҕΦβʣɨǗ˄Ų˵ҝɈνAʡ˝ĨďſǍӲçЄɌˮ,ԫ',
                            'mϲ҃QμȕǱňΔɡǍҶȗϋȊǊÁˬ˕әΛɑήʜÎ\x86Ïҡƈ;',
                            'Ӊ²΅ƕǶŴbϸƨҒĢżΰʼάѿΟØ+җʴϞ\x93ˡɊмųßϼ¬',
                            'nȕňƱƌӽȂU~LɐϪɑaȭǒʹȞKɥŮɟˢů',
                            'ѭ˹Ŝņ¿ÖȸЩǌԬʻPƐĐ\x9fƭűf\x8bΡʯȒˀȘѡZӮҭÁȦ',
                            'ŻӛЙϸ҆ǲѕƿІƳòԧƎлłԔӎǥҥщƻ×ʨǪԥɿšҺЁȤ',
                            'ȭȤҁˉŻљ΅CԫΡ˓ӄϬȢ΅Ҡ¤ӤʸʚŢёɼż»ΈYҏ˷Û',
                            'ԂåǊǔ\x81ăΊ\x8f1ˋʣʂїǨΑÖÍńϻԦĖΆψȍлϸҨrźÚ',
                        ],
                },
                {
                    'action': ']ΥǶœǸɲˍˤƍӘǢ˽ϲȻŵƴтӐǤрǜEġӓĹΕơҫǓË',
                    'resources': [
                            'ĮƛԄѩҦÀԓƀ˛ӂϋĊӷҦэʝĴҷ˴ǞТӫɺɃu˄Ȕ¥ěɚ',
                            'ȆƗČɘɘȟ˴½ÞǛʎĺgԡ7ӢϠŮԫ΅ʨӶƨƫǴƿʑĮˈԚ',
                            'ĬìԠÙɇŵæ\u038dӶCѻʡÿЇȄӳΪϔǓȭďǞĸdҸΉЮϤʰÃ',
                            'ǭЛýĲˍϓĕġʞâƙȝ˭ȀκǲɉƲӕѮʼί¶ԥOԞʅŰüѼ',
                            '¿ñbŝӱ.ɳʝźȧ¹;ҎƘc\u0378ȖΝȆǝŦåӓĘÚƪ>Ç)Ŏ',
                            'ɕÜϴÞԭЅ!ȔΤҜˀ͵zԤаļʖʾʂƙ\u0380îЛϑîϕѐЌßӡ',
                            'ıϑҀƒϺ˅К"łƝґӨʔɐůԌüǪɿ˵Ǹѳѝуκáʨǂŝи',
                            'ČύөԮŉęҴЛƧшјӵԪÔÖȵłćԑȟǊǗԈӶĸςé4ʹ\u038b',
                            'ѾκǴәԥßȄɷ\x81BԆӬΠЖДӟӞĔΤԜŷŷȨΒҢƥΏÞŎѿ',
                            'ǖҲźԀŶ҃ѓºýǄϰĕ&Ğκˬźˣεòə\x97ѕ£˂ÀӯɄͻƠ',
                        ],
                },
                {
                    'action': 'ΒƜʂԬΜĀ\x83˗ѐIūb\x91ëřо·ǫ',
                    'resources': [
                            '¿8ьˠʁϻӫÖ·Ӗǵʙ\u038bҝƉȔɷȟÏϐВĶӉЬǃЏҕÔ˰4',
                            'ȿλË\u0380ɲȈɃЌȊě˽&ǉɱ\u0383ŨӳȈ\x98ԣJѢӅCǿŋł\x89ΕЀ',
                            'ӥϺяˠǉ҈цĩӿѯѯѻß\x9eɾѕwĿǛˁӻθӉԃɮƁNy˺ǳ',
                            'ͰҰãƎðÑҦʇ˥ɞИtŘԭʺŤϲʗźöѾѣ\x90\x85ԓˁęχÉ\u03a2',
                            '¡ϘȠʁϨe˩ɣXȦӆѡȉʜԆˌԧřǣӊҠQʔǿŏøǌ¶ȚИ',
                            'ǀЭ¾ћȤąƶЙ˅ƒԈΕġМÉƅńīȕԮèʢ\x7fɊĵӊ$]ʐԨ',
                            'ƽˉϾȷͱʖˢҬđϲ3ԂζҽÂыԨϜ6ҧĥʁ˜ѬĽȗʗ¦ǀƿ',
                            'WƢϐͽŠǌ¨ɺџѳ˘ЄҞþɹ\x92ÑԗҺʫƩΓЋЁˢ\x98ˏǗӳȩ',
                            '£ǬѶԕеѴǂŉеǉϕԪıЩϞʣУɖӽÈʿLԞ¾\x93ԛɥȯkБ',
                            'ƊƜΣҎӷӽȼ¶ϫƛˡϤȢɻȾ\x9aŢų\xadŤѰԑϩΜö҇СҺʴъ',
                        ],
                },
                {
                    'action': 'Őʍύnɱʛ\x96ŧǡGӖѷύҁөʋӴӰżȍԭӆŌҙlƭǷҽǁ˯',
                    'resources': [
                            'ϫƣ\xa0ŧΠþ·ѕǊЊͼ2ˉɚкӘјґēɘɎÛ\x81βŎϮ>\u0383ȗŚ',
                            'ɂǿƐQ\x7fΞdԛϧνɉʊԥeΪȠƾȸǫȺӋΧ\x81ÁƊ,˃îΜΜ',
                            'ǒĘÆηˠХRӻҤ˰¿ȃӱƿϸʺҴԗȼȍЌѷǗŎġǼΤ<ˎƭ',
                            'à˵ŔʰƑȹ˰\x90ѦǱѷћηʛӋ5πȮ\x8a\x93ÛǷġ϶ƳӖɬϨįʷ',
                            'ņĤǲʟԇɰԍsĝưǞϟ˛ȌѩΗϪһԪÅӔοʝ˽сơϔ\x87ǯԛ',
                            'ҍΏƉͱѾІǲҏǵɫƼєʿԅĜЦɖьӳŇˠ\u038b\u0383ҔʿäҜѼ˷˵',
                            'ŔǑԊӧĸȠԪiĬ½ǍȞϒТǭҙЂѕĢaǷÅͳʴÔЈĞЙʸԘ',
                            'ÛʟҜ\x9eĥ\x88Ȗŭ˻ƻ\x9bˀԂ¦Ȇύ\x9a¬ʉȻҔVâʫȯƬЦ-Ȑκ',
                            '҂КϥӐǎ҉ӳːʹΎɘŜ=Ԇĳǯ!öáӢЗΟəą˻ʿЬƋњѕ',
                            'Ѵ˜ÑπҶУэôƤ\x84Ŵȫϛʅ)ǝɞŴԎQϝ·ˏơƲţÖx˦˰',
                        ],
                },
                {
                    'action': 'ćƞǬŵԎȷϝɧǱҔѓВӬƥȞҫϟɳƇԗƙŔҬ˦Ɓ΅шˤDɉ',
                    'resources': [
                            'ƊҔ˚\x8c\x90ѾǻԝϚƾ´Ʉ\x81ǷɥүԢґŤеŚӰÄǂíӔ®ҚȈ^',
                            'ªƔƷʴ҄îЧȿԑýѥd˛ϾʨĀƗpÊĢӘӔȤцŉÜԏҷ\u0382\x90',
                            '¡ЂųПĺƆ˪@ĂțbӓȝІ@ǢĎčΐƬvūʮԬϪБĂʼÛˠ',
                            'ӎǱͷɁ\xa0ƛɻ\x9bӰӒˎВϐԢґʂ\x99\x87¨ǉɧȧHЀˢ˂ɭ´[ς',
                            ';˻iœɡū\x8dғĶԙιіÆǌŞĀ(ŊWϕ]Ńήʔ˯hӋпʥń',
                            'ĶGτ]ƚҙΐΗʥҤɹÒǖʙӶg¡ɀ\x8cі\x80\x8dȽяȪά¯!γϏ',
                            'нkХ˭ǂϖ\u038bĥŶǽҢԃâ˱Ψĉмƺȫĳɞ˦ˁԔг®ϰƔƧ˅',
                            'ɿǄÖϡРĪШѱË(\x9bƤґʠӛѦɑȗЩĂʢʢōўÂǕԓкϟØ',
                            'ɎҕΌӜǕҥǥȓɑÌjԒѬԪԈ΅¡ñöПҗ°˔˛җȫҙ˝ѽΏ',
                            'Ȃ¶Ȗ\x86Π^ďyЫЧĹ`>á˞ÊϙЬԜҝΓŃǉѴӕʗɦҝΟѪ',
                        ],
                },
                {
                    'action': 'ɡõжҏѠµƋȠþҚȼƙȉʫƳԑÑƘťлг->ԓҜԏ5ŀ\u0380Ɩ',
                    'resources': [
                            'ҮĊЈǾϜţˀӪă\\š«ΧȉǅȚSāƙðͶ\x90ҺqӊȶŌÁӯљ',
                            'ϭɮģɮ[ҲȟĹȩ¾ɇԑ˔Îӧőɔё½ãӼҢʾѼĈ˫ŊȡƊέ',
                            'źîи\x94ћʤʴŬǀœ ɺӘԧӯϻѻα©˗ʷÛɻĆĪпĊѸӊɈ',
                            'ȥ˸ĎґɄҮϬϙȘΤʒǯɝԆȏӚȯȤʎYэ{eĭƶ˕љŏιï',
                            'ԐѠʹ\x81)âŗWġͳϷɧ-\x8cΒƕűзňϕξҘѾΰmЀ҄ɨǈî',
                            'ǳ\x97ӀϕɦӃҠƑȓ?ʇӭζɗǔ˳μӥǜǓżİЙǓȐӬâȂǊԟ',
                            '\x91˯(ȊԘɎ\x7fԚƅƇSǤԋŮhʠXйϪԙѾRƂԬŊǆҹ\x81ɀý',
                            '˫ÇǅԚӖʉɔɦŹȴΟúɋþ_ʣԂњȱ\x83¶Ŀʳϡ\u0383\x8fnʅјµ',
                            'АˏϡӗϼнöΩϐґͱЃ˟Ç\x87ˋ\x9dʔÀΡύ>ƻϋǷÚЩĞMơ',
                            'ēńҹȜǾҽˤԩǷʣӄɗωĶïӲʿWΐǸ\x95çЩÈАϟϝȌȇư',
                        ],
                },
                {
                    'action': 'ϚǢɟǆƠêѨ˖įʐǇнӉˆԏǥƷß¾ʍҹȸΗƒӒ˽˝âÑԝ',
                    'resources': [
                            '҈ƧҀМБȯËǊϦҾǯԫкEȅ΄гǒӃљƼɬʇȖΒϠљΩƯá',
                            "˘ˬҝѱƣίȻǫʐӓϺē˱ҤѻoсяŲӧԏ<\x8bџ'ĆόԈŶŧ",
                            'ͶԧΰˏȟϺǝķγͼжЍԈоȓ\x9cуǡӄȵĜȑԚʜŸ\x97ɏѽɲρ',
                            '˹Ӎ\x87ɧәʘŃЁϒЙȁǋǗѲKŖІē˼ǂ\x83˖\x96ǯ͵ЙÿgѷǕ',
                            'ȺͼМԓÎæńťͻυʋñǈĦыиʟtǪΥ\u038dɮѴӳϺӮŠȅŉТ',
                            '-оJЃƲӚӤɮʭȖƄ¯ǻĵ Ӄľ҃Ѭг«ɚѝˉȴˠЫʊъң',
                            'ŲӆƄӡτÔųʭ\x85ɯϽБŃЯ˫Ϟ҄ŠDȂȔʿή˄ˣúúƿȀź',
                            'ύў&ĘÛəɂīη\x7fÕ͵ɮʊм҆)ƚ©ȬЂϒ˯ϟӽсŹπүɇ',
                            'ǳ¶ũʸϴ\\ŧɸtʫƜìľƽĊʱƊɬδŸКӬx¾&ΝҿŉÅĞ',
                            '¦ʯɁɰɻʔѓӰ·7\x9aЈƴʿξмӟˌŌǓľԧĽĽǎʒїҗʽ[',
                        ],
                },
                {
                    'action': 'ʝ҅˼ìÚңƽ˖ԪѺȎǱʬӘѱǥƇԧͷЁϴǮŠʣшԧʍʍñҝ',
                    'resources': [
                            'ǹŏ\x9aěüŬĈЬǼýϰчѨˇeŤҭȷǉɃɲҹѝѣӆǗ˲кKş',
                            'ȾѱЫǰˎŐàɜЂːŊЏӶǂʊʕwȠŧƯyϒĴğÔΕҗÖCč',
                            'ʼҳȇǫԡħōʮο҇ĊфɧҐԮÈ˔Ǔ҈öѮżӧ҂ǜϻ{ɰα"',
                            '҉ǧөȒƾͶΜĆ_ǲǜϝƞÍґҝʳЍǵƑ˖ƉҺűЈ&FͼƑʲ',
                            'œ\x9eůϲ\x80έ˸РƚɦĬѯϰ\x86ɎʾˈΞ˚ȉǄ˚9ӱĬц?Гʗӏ',
                            '(Я˻M˟òӼѣӌÀdȔëϢӴӱȪ;Л\x8fÂ˷˕ˍƦƖмΛ˃Ҍ',
                            '\x89ķҾϥӝǯЉ˳ǫӈʢ\x94ņƒHǲǟëơΐǿϐĲѧʜ².ƘɪЁ',
                            'ѓіԩĤӟɚѹΏһ/ѷɿͼ˫Φ˭ıˍǅϦĞ˙˸Łͽı¢ǎː\x82',
                            'МİȆ\x8dŲКʐiÔҢĩƋԎȃɪȗҒä˾ΚȅǣζНԐ|Ҥʣlǘ',
                            '˭·ϦɚĻ˼{ΞæʳǷɭЩǀĊǮϳл\x9eѷҾʜЌȍȴȢɞǪ\x9eԊ',
                        ],
                },
                {
                    'action': '\x91ό˻Ӓe˚ʽʺʎˎΧОЌȏǍÑr%ҿĦѹѣ¯ν˙ɴ˧ӹʕɻ',
                    'resources': [
                            'ʑЫ\x98ɓџʞňƺĈȣёŻέτЗŹӍɽ\xadɊǇČɳǏŰʧşȹǜǮ',
                            '_ŮҊ#ïý¬ҙĆ²1ȩўФˠҫhʋƌАԎЏ\x85ѺƟʍѯǠͼѢ',
                            '҈ωΛƂşӬŖʤ¿ĳđƭÎÎЅҨɖ\x91Ǟ9ϾӯϯyƆҙʔĒҨΐ',
                            '϶Уʙк\u038bƍщЂƺʳʹƤŶӹLư|ΉťɸʍӒ˪w\x8bƽhÀ_z',
                            'ŉô ʍˆÀɔƏӢ˕ѸюҶɘɲєźʆŹԦĎφ²дӋʓ\x9eϊǱĳ',
                            'Ӹ<ɭ\x9aɚԨгȚ˽ŕҨΛnѥ?ƞ˞ʏƎӖĈʣJ\x97ųѫ\x9dʐҢЋ',
                            '\u0378ԁêӖíüӽɱ҅ɠǯ˵ǬğԮ½úѷ8ϨÍЅšůɱ/¶Ӟэѭ',
                            'ѴӵƌѺĔΘҙӆЌǔѵ˛ͺʵϞ˥ϼĴÏʳŤӚS˘»ŌG Ŋɜ',
                            'ºĥǧˠÃϽʀ©ǱДŦЪæɾ3\x8bȂίΪtơўĸνȪуҰɷҾΰ',
                            'ȾƜǈȑ˪³ГȼIĪȂϜχұƚɨԒѸȊˈԭǻ˂łƊͰ˚ҵԚӳ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ҳ\x99A',

            'version': [
                -5956203122949353571,
                -3645438475032919532,
                -1875460604781168137,
            ],

            'location': [
                'Ζ',
            ],

            'runtime': 'ϰ',

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
            'name': '0ċԁTĪˈʴ',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '\x8fԩí',

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
            '$': 'ʉфŧ¾ɢѕHȾөȋ\u03a2ĂÈQ΄ЊЧұѤĖ¹TɾƻƖ˦ƹ`Ǽɑ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 117893891308005003,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 129401.49625928685,
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
            '$': '20210309:035018.686705:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ЏäǗy¾αE\x99ȓȼДɈɔğӏǠ˸ț˭ǰШτӨĊ˯¦ЦţɝϾ',
                'ģҩ˱£ρŕЁӻƤɔƢџϴǽk˚ҭ\x9b-®ʂǷѹǚæΏƛƪɎ҂',
                'ɡÝ\x95мԙӞӔǳԅԢȬɖÌҢӽΫȢİҋČĆ}żŵōȠӕэӠЫ',
                'ӀʕΘǴ˯˔ȃǰȃŏàϴДӦҠÕБˬnÓƝŋwëїҖƯªӲє',
                'ʳFρіȠ˴ϘßЁ3BȫԞˢ\x81ΰё"ԭɧӺʶƗԏɬpӐƾʝĴ',
                'Ѩγűƀˠϒğ0$˩\u0378ϲӹҴēќЬǝҍ¾εДǯs×ȣ\x8aɃϭʨ',
                '\x92ɍТ3êɐӁӉϓȯɓ¡ϓZ£\x8e°ʼ«ȲçчʩȑiӧԟɴģɁ',
                'ȲHÈ҃¤TӖǴǭäȐʖόŹ\x89в¿ˈúτ>҄҄~Ԗ¨ԇкҖН',
                'иӺĵO|ʽŏɖƒыɲăƭԦm]§ĝşщΫºʲ˫Щ\x84ϗНǀq',
                'бȭžлҎʔɚ\u03a2˘ƿøʂȢąΊÂˠˢȻƦ\x9eȬ\x8aЃӿɶϝωǪą',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                3191474198433167477,
                -5942517755537726131,
                5497176164183991130,
                2513679582062257903,
                -3964482836210764375,
                -2254948208892198901,
                -1801971361974197374,
                497725038140962187,
                3305982732869680537,
                636426018063245509,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                213032.22463310236,
                -10870.888847035181,
                868808.04189042,
                726134.6913578659,
                330118.58286165935,
                10421.871358904522,
                933344.1628637026,
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
                True,
                True,
                False,
                True,
                True,
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
                '20210309:035019.812257:+0000',
                '20210309:035019.834656:+0000',
                '20210309:035019.856832:+0000',
                '20210309:035019.880745:+0000',
                '20210309:035019.903942:+0000',
                '20210309:035019.925173:+0000',
                '20210309:035019.945895:+0000',
                '20210309:035019.968801:+0000',
                '20210309:035019.992416:+0000',
                '20210309:035020.015959:+0000',
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
            'name': 'ëшϑΖVϬʴϿũѵȄþʴ΅Ψ|;ЁѵȗΐвĦ\x7fžŒ',
            'value': {
                '^': 'datetime_list',
                '$': [
                    '20210309:035018.221900:+0000',
                    '20210309:035018.266668:+0000',
                    '20210309:035018.286668:+0000',
                    '20210309:035018.303839:+0000',
                    '20210309:035018.320584:+0000',
                    '20210309:035018.336971:+0000',
                    '20210309:035018.353483:+0000',
                    '20210309:035018.369540:+0000',
                    '20210309:035018.384877:+0000',
                    '20210309:035018.399907:+0000',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ȇ',

            'value': {
                '^': 'bool_list',
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
            'catalog': 'һћӭŴ˘ȗҒҌԫǭαћôȈƐЏĞԎԝFΗ»ǩӮƒԊҞϏSͻ',
            'message': 'RΆğěҭƲ¦ϋĻʜӦőėͺəǃȺ˨йԔҪӃ,ҟǎΣɐƴɮя',
            'arguments': [
                {
                    'name': 'ưjѨɓʘԂлīǊ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ʢ»ȼӯ8\u038bάæˁЙ˞ԓːςƖҒ',
                    'value': {
                            '^': 'float',
                            '$': 915378.0675537823,
                        },
                },
                {
                    'name': 'Иć',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ʒԫoíύįɷʑӪǁͼÅʍ\x99\x8aˠİèӿőǞ\x88ũӇЏɒɹŽǓд',
                                        '\x9bʥԍХWˬӐɷҩǚ\x89Ώϒïϼ˻\x99ӢJԁМԛƵ҃ŃÀƺƐʹʿ',
                                        'jǃӚҦŹǾдǆPԍƿԊЧгJy£;Ҽ˽ƜδϺŗϱÃԏŗοŁ',
                                        'Ť·ϓœǵ:ǑƂ6ƃƥĄŰMї\u0380ĪȄιԢ\u0383\x90QҪНǷåƷeĴ',
                                        '\x9dфƹɒӧȎэИũŵʠŒ҄фǀϮĤЀˆ˭ô\x8bѯĩҨɨԦìlö',
                                        'ÍŕӖ\x7f˭ǓѧαӱўΊŝЊιÀλԎҲɎԃοʪŶ˫Χ¾ʯ-˥ǂ',
                                        'βAН¹ʍʞɨДζşˎҕƒǞуБ¨ɛԕΑҽƛЏńŢөɓқĴҖ',
                                        'Хīk\x7fȀ2ƐҸȁЌԍ4vθГϊ\x98Ī0ңǵзȞѹǌÌ\x9cъǎ˙',
                                        'Ԗɫĝ2ĘÚŎů\x8dɧþŊƜĦǸҦѬεΠ²ҪLί˅|ԒѱѼǿ\x85',
                                        'ГҾӉŐRŸǙԋҋҁԎ¦ɐҵ«ÿ\x9aȋаƾΛӑȆĪ͵ҹȹӆҬһ',
                                    ],
                        },
                },
                {
                    'name': 'фтȨξĄFɚŸӈʛťϾȁͲF˧ȡЎɑА',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ʗЧƲεʺ\u038d\x84ıЯŠũѴˏɡŔЃЦҹˁРVάӜŪȟԚßȖŶ]',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -9095573209365672787,
                                        -2657554212382255445,
                                        -7989461911660427377,
                                        -1587579030499796667,
                                        -8499417447010987365,
                                        -8974194487301207787,
                                        1842724003534138611,
                                        -3840479006820179595,
                                        -7065528009450403153,
                                        -7866938656495021966,
                                    ],
                        },
                },
                {
                    'name': 'БŌÄʜǁòĆǸдӪΊσŹȌ˂˽ќюéςЎȃӧ<VМьκ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210309:035017.648890:+0000',
                                        '20210309:035017.664229:+0000',
                                        '20210309:035017.678358:+0000',
                                        '20210309:035017.693842:+0000',
                                        '20210309:035017.707997:+0000',
                                        '20210309:035017.722505:+0000',
                                        '20210309:035017.736400:+0000',
                                        '20210309:035017.751539:+0000',
                                        '20210309:035017.765487:+0000',
                                        '20210309:035017.781057:+0000',
                                    ],
                        },
                },
                {
                    'name': 'υіǓ\x8aҙϖҘŘÈψÑӳʄȘĉjҌ',
                    'value': {
                            '^': 'float',
                            '$': -3937.2091620270658,
                        },
                },
                {
                    'name': 'ӮЭǫҭɩˀ\x91ʋɢёźǎįȕҠ\x96З',
                    'value': {
                            '^': 'float',
                            '$': 54579.52299004761,
                        },
                },
                {
                    'name': '$εӔɞѡ˙',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ŋñǔɀÒŨɇƕĲ¶ȩƟɢӪ£ӻŚυȴøʵЃѐ΅ɡʹѕұӗε',
                    'value': {
                            '^': 'float',
                            '$': 181895.78676630533,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': ' ȅ',

            'message': 'ɣ',

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
            'identifier': 'ɍơ\x91ӉȆƼʣɣÑǴƶ˒ҟȅŝѨʁԈŸȓҫȺжąŉЂǎȹϷω',
            'categories': [
                'configuration',
                'network',
                'os',
                'access-restriction',
                'invalid-user-action',
                'internal',
                'internal',
                'os',
                'access-restriction',
                'internal',
            ],
            'source': 'ԝɓ»ŅɉÒɓʯ˫ȮƊɨр\x91ɭϔʅϽ$kōӴҎYǂɞEҔυʂ',
            'messages': [
                {
                    'catalog': '>>θŉщԊϬƛϹΗκįųҗõ_Ι˽ɀǾıʗƴåϳƽƲΥˈȐ',
                    'message': 'иύЈъΑԫϲԀҶēƣˌɭþȕżӭïŐɷɨҼ%ƥͼҙɼљǿǪ',
                    'arguments': [
                            {
                                        'name': 'DαһѬÍ\u0382ννǋԇQӽǵȿ¹ИɭԥşҖǞ ԇ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5830393051086718431,
                                                                            -6570529637552945802,
                                                                            7284442281153459278,
                                                                            969523813838143267,
                                                                            8281543664817821901,
                                                                            -8525184998417353883,
                                                                            -6455543561423191659,
                                                                            -5697464188226244599,
                                                                            -866753452504396188,
                                                                            4463630526794991854,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˉˌҔɮѰ\\ǂτvӻU\x85ΝũuӄƓ˖ȲҧǜǎѹųԩćĜſĄĬ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            123235.29407503005,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ъ˭ӄrɖːԒе°ҵΑS',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
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
                                    },
                            {
                                        'name': 'ǜһϥЗƕăϜʹ©ϯϬʶǹʠЅĄńћʰ@ϯťĩƚĘƐʠ˯ԘЫ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035000.929401:+0000',
                                                    },
                                    },
                            {
                                        'name': '˚ӀŃȰƥȍӗ˄īʭ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'űËǓ\x8eȡ˙ωʌӠ7˂~Ї£ԝʑĺ˟}έϬ{ƛˢʚŭȄҪϺέ',
                                                                            'φňÃĝ˕dĦЦСțΣƞҷƀԚYé]ŢȵӍˤ<ύˁƶƙԫԞҿ',
                                                                            'ˉГˬ˹˳KȭŎϐͰͰ{ʤȘйѺϦŘʾʇӋîaVɫǂϳΒʅĬ',
                                                                            'ʚŁВ\x8bǉβҘΆѧ+ΧнʙϏЧȊΘҋЀǋ\x95ĔşЭ˨ɉș\\Ɠ)',
                                                                            '˨ρѦТȘƽԓԕƪ\x85ɃΝԎėŖÜПѝÏќü×¿ˡdFǻ0σʑ',
                                                                            '@ɑїƺԠѩҭ-ćοԗʛƨ˚ëӼϥǛŻlĳxξ´ϚһѠԀ҇¾',
                                                                            '\x80WǘΗž˩ҿÓԬρчɀȖΫɺҔԅԞҡʠɎЭŭ˨ƂΙʏԛ҈Ϳ',
                                                                            'ď·ğƵ\\ԭŃӅйϪ\u0383ȵδ~ƈÙӌďт,ǠʬѮɨŌӐќ½ɵѫ',
                                                                            'ɷдȁʇπŭȈӚÞɣŸȘɣǴʮωˢ÷ǃνȹӖêҙɉ1ǚ\u03a2˾ǵ',
                                                                            'ʟ°ʀԍò@ȁŸɟқδћѦơԝʾВȡɂҟʠͶΰ҄ſғʪƷѵƚ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'iŁÔÙƎ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ΆЧұʠĕΩʂԭƹfůĥǪʐ¼Ĉ\x92ѶȋţĂђԧŇÈӳыς',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 399835.54462837736,
                                                    },
                                    },
                            {
                                        'name': 'ʴďήŏľӐáҩԤƢʎzĪӛγΐ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӍØ(ʶюŲРȤqÀťѠӅ²äҵӨЁˊҋхЦʳƵй÷ѻƇ\\΅',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ζ&ԇĬĤƺȘȉȕʗДáǺŪӡԐΠӢîŦǌñӦ˛+ǉϹԫǕÅ',
                                                    },
                                    },
                            {
                                        'name': 'Ĺң ψҺ\x8cnгԑ˳Ʌғ˘Ʉϙуп',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŷπΜкÛƨӃƺÅušӡǫтяʰң5ǺÙŻԅiϺщǞ¬»ðʹ',
                                                                            'ˊƽҜ\u0383Ɛɧ$ɶLү~қϹǗ˸ϸϔяˍʇɸƘҡѸơǼȢBХ˖',
                                                                            'GћԫѰͶŪȁqSԒɐǙʩт«ЇΔɘιхÜÙҐЉÕǵ˓ʺʄʾ',
                                                                            'ҪЉƏћũϘԠsóçɂǄȑxŧИʥÒѤϢ˝Мŵ\x9bʡӋϦɀǴǒ',
                                                                            'ʅȗĕӴƞɻǦΖғӞȜӠёǢĴϛ˻ԊÏӂэʯmǂϘĉРÜҚϾ',
                                                                            'Ƞ\u0383ӔÙrЋƻț@\x8eҚΝŷɩɪSΖƳ¬ϬĪχ^Џƀ\x9fГ×˔Җ',
                                                                            '˘ѢnưŇȼԀ ϑЂȊŨΜѸ½jʎϞ\u038dȣέȶǵûqѵԔǈɯϼ',
                                                                            'ԂƤɞʒΰ¦ó϶ҭćфťЭҟȍƊѵʗРϔҹˡЍŚ[Ԃ3ү˪Ǣ',
                                                                            'ʍβɘ˶фʨŢԂʔɣҲ6§ĕǀ\x95Ҷɜç\u03a2ͺĜхͺƨÇɭ\xadƍͿ',
                                                                            'Ԯ@¥oſĝϪѶӠѴцƚϦɤ҇|ДАɐɧÓԢϻÝƹǤӂҦÐ\x88',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԚѨϛԖϪԦŲμҔӌҔǥѓ\u038dҭ¡ĖԓɰɉϒҫƏ&»ΊӸ\x82ңԍ',
                    'message': 'ī˧ƼȄϚ˄˂ӌʏïè¾\x8e\x8aȐľĠȵӝɨĉŪЧʃă\x9f\x93ŀȿǡ',
                    'arguments': [
                            {
                                        'name': 'ƅȺӱĚШϛǅʒɑ°ѯӫɹH',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035002.186262:+0000',
                                                                            '20210309:035002.205822:+0000',
                                                                            '20210309:035002.226752:+0000',
                                                                            '20210309:035002.248121:+0000',
                                                                            '20210309:035002.269421:+0000',
                                                                            '20210309:035002.289674:+0000',
                                                                            '20210309:035002.310850:+0000',
                                                                            '20210309:035002.330627:+0000',
                                                                            '20210309:035002.359096:+0000',
                                                                            '20210309:035002.383799:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΝǟВăĐ¤һŬ§ĴͱšÚďͱĩŌъȦҗúȵθÚ/]\u03a2Ùͱӽ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035002.504315:+0000',
                                                                            '20210309:035002.524662:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȋí҉йœÀпɆǺ˄ȷƛԪѵæĒ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
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
                                        'name': 'љˑĐºˆòȊĈyƬμƀ\x82ΡϿɄeжȄԄӃσɓЉƢɦʌӎƵƶ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035002.953019:+0000',
                                                    },
                                    },
                            {
                                        'name': '˃ŀǵӭ\x8dԖЭǬ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΨϙȀŴԘԒʹΐńΫʊϐѮÂΟħӰӟuƱńǅ\x88˄\u0381ѨˮňȖī',
                                                    },
                                    },
                            {
                                        'name': 'ţ҈ǪΡTƝ˟Ѣҹ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ĎϳЛӎ>6΅ǵШЭͿŶԤѓǘԊǏ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            505119.21820814523,
                                                                            201881.35913957813,
                                                                            -78290.13737905603,
                                                                            354859.6737726052,
                                                                            523551.28616044996,
                                                                            500163.7696265158,
                                                                            515600.18297816976,
                                                                            878160.88508569,
                                                                            938136.1968225488,
                                                                            731352.6922721448,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƉжcŧɿǡȚ͵ʎӂʷǵ˝ǹȥw[ѮÅ^söÔąЀӱɎǖӚү',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɬťΪ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʶ¡kˠĴƸӷčǩҲоȘŽхÊ;ΪҡѐɦƮzѰǗђȯ\u0382˅ƘӍ',
                                                                            'ԪǜăƠΊµǵт\x98śɠ°Ϳͽ˪\x80ɴƺʱҤγ5Вʨɛ®ȣæ˛ŏ',
                                                                            'ʜθƽɠʦŒˢӖʉ͵ΕɿЧӅч˴ΑӛʬƇҐЕϹV˰үдèśɱ',
                                                                            'ŀVʙҩəǰǷ\x92ƁԈѷѸȸˁ˷ӻʙǱƹňЩʘÁƿȪԢҺЗǔʺ',
                                                                            'ώӓʅ˦ːƠ%ж_ÃЈ»πʠ˂ԤƨʚDɖɬһĭ·ǌ҃ѼΌǆ-',
                                                                            'ſбɷЯʧ\x80ſȯɾŌцȗˇЍʬ\x9fӉhȮҝȈ˛ЗrӒ҄ЏÇͺé',
                                                                            'ȳɅѝāĐŷƗдå£ȶĜǴǡ\x93˳ѭӟΚӁЦəˀ£ĜЯȇΖ\x8aҕ',
                                                                            'àʁѺÿóϰЍÏȁόϹ˥BĎɪ˦ŦԄƠҼɸ˄ԥηΤѴ\x95ʄρ˵',
                                                                            'ϡĔƆϖĮĹǲæϞɶ˛ғΣΌƫˈɎǐΒǸңZƈѤwΑáƒΥΛ',
                                                                            '\x8f\x8b҅҅ˍʹũғ6Éȕҟ4ƷÕŏȻҖʨ_ǐŧƀǞCˈɪ˦ıθ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѕΎʬ÷ѰҡζİɌ͵ʭҢʐї\u0383ԋ\u03a2ϘЉВΣә˅ǨԟΩŀ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƞɲʂ9ϵtԦҙ´\u038bРµʾŒΓÿĊњɜ˾Țɦ|ЌȂԬƇxǤ\x95',
                    'message': 'ʡ˜ҖǓѸӉ˄ˉӬĳ˭уΠ÷ɆϹđʤԑĢyвӢԫĚΪԄҿʜʑ',
                    'arguments': [
                            {
                                        'name': 'жʘÃćǧ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˮeҳƌùͿȔЁòȂӋɎЪ҄ɸÀҒӕˠŻԍҠʊßƥϷҡƼ\x9bɧ',
                                                    },
                                    },
                            {
                                        'name': 'γǙƁ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 614219.6327082056,
                                                    },
                                    },
                            {
                                        'name': 'ҹ-ΞĝѣΑ˳ʺĺÜ·ʇͰŏ5șѤˮƦ®ҁϊǚç¿ШѰˬȽԣ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -9770.302013582506,
                                                    },
                                    },
                            {
                                        'name': 'ä®ȾˠϾΞɟU\x84¾ǰЌĮɃΡŎҮ]ʐπǲϊӕˉóăƎ҉\x84ǆ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035004.411009:+0000',
                                                                            '20210309:035004.426804:+0000',
                                                                            '20210309:035004.443034:+0000',
                                                                            '20210309:035004.459553:+0000',
                                                                            '20210309:035004.479950:+0000',
                                                                            '20210309:035004.500650:+0000',
                                                                            '20210309:035004.518958:+0000',
                                                                            '20210309:035004.534249:+0000',
                                                                            '20210309:035004.548551:+0000',
                                                                            '20210309:035004.562681:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΚW˜ҕʘʍϔκǐ×ķ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 267199.65777464793,
                                                    },
                                    },
                            {
                                        'name': 'ӍԌɖĀͼеҰĎZӂӞǌË×˓ǘƛӿ˳nȂǪ\x83',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -596490666457513909,
                                                    },
                                    },
                            {
                                        'name': "ȽŲȇƔʤāϟÅƍ'łѲšʗƫ\x88ΩnϦʓ˲v˼ӞŐƆ§ʗȵó",
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӴӓўǥėʵǀƆĉƏňїˉΫěʑӆэѕðЍǚɏ×VĘΧʇԂϚ',
                                                    },
                                    },
                            {
                                        'name': '\x9cȚͷόԫΧɈʣq',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            851620.1231341799,
                                                                            627061.2525850474,
                                                                            312920.5235001729,
                                                                            796046.1975555313,
                                                                            803056.1100139656,
                                                                            757816.7460429806,
                                                                            579651.1178751837,
                                                                            386678.74197706126,
                                                                            144318.3162950122,
                                                                            10597.814862028172,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'İŦˁ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -76779.51090231165,
                                                    },
                                    },
                            {
                                        'name': 'ʵÿуўǢΤ¼ӝҧԅcԠ,Ԕǥm Ȟs˵āȵRȿφїɦqŗß',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԩԇΑƘɌ\x98\u038bϗ;ʎЦϑǼ˯ԏ\x83ßȨǬӿEǪϝΫɛ±υįέХ',
                    'message': 'Lϥϲþԗ\x96Яǔ\x8f\x9eӌчЋ\x8dђǣǧΐΈ¯ΐͽͱ|âͳmǜҹĀ',
                    'arguments': [
                            {
                                        'name': 'ǽΪϡ˝ȉśɀÈàɎǤѓ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'HΠ˽į\x88ԮӱԀ\x95ƍƱάКФιßȟʂŴζˈǖ\x9fƘξʒЉƴɁȰ',
                                                    },
                                    },
                            {
                                        'name': 'ʖ1Ӈ\u0378ǾύҚǂÞȌдƓʲȜȠĄѭѭЈʹҵȡπӘү\u03a2Hүӓƕ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035005.391510:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƉțЮπźΌdʆIϺԮʼгӲ\x82ˉЙǢʱõ\x7f\x86',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ŘҏȊ·?íǽ@\x9bʍƝЊͳҷ\x89лԐŜҹq_\x9e[уɕƲ½ˠɅƙ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            435423.9480667459,
                                                                            908985.1229371009,
                                                                            56272.98977653668,
                                                                            494250.67717914307,
                                                                            905306.684250883,
                                                                            -70788.05483864731,
                                                                            274239.8098843391,
                                                                            206395.05341840273,
                                                                            475986.7913992844,
                                                                            172315.85765243875,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ģóҹǮē¹řȨðűƁġ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035005.824894:+0000',
                                                                            '20210309:035005.842803:+0000',
                                                                            '20210309:035005.860543:+0000',
                                                                            '20210309:035005.877994:+0000',
                                                                            '20210309:035005.895536:+0000',
                                                                            '20210309:035005.916038:+0000',
                                                                            '20210309:035005.937777:+0000',
                                                                            '20210309:035005.962007:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϼ1ɵʋ\x92ͼД¦ʉϺӀɃўӚѭӨҟ˦Ļ\x84Ǧ\x90µʁ_и~˧Ƅʽ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2783769702954025564,
                                                                            2337379300141202208,
                                                                            -3889972641524461740,
                                                                            -7216125681590923618,
                                                                            6584372762506083150,
                                                                            -4166027048545003141,
                                                                            -471433006119833415,
                                                                            -8670816110174702434,
                                                                            5915602215962936782,
                                                                            982960380310980347,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǖʣѴ\x80lǲçɃȌСҧȍÕϫɒÁӐʴȄ˚',
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
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҿ\u0380Ԡӭ˦ΨÛФȚsΐŶξċŷ¥ɜ·ʛΊĎβȊřɃǮáǢàʂ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʫʰUҞԡɳŕ˳ИЇϯőҩλ˶ѣÙѶʻ\x88åȠєÞΩȱ\x94ɣȨѪ',
                                                    },
                                    },
                            {
                                        'name': 'ʗGΐǠqûŋϣА1ʋ6',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "óƉǗ¶˚ǖʑЦė\x90£¾ɢӃƮș'нʭņƹɝԤǉŶӱȝʑĈύ",
                                                                            'ҍ\x9dЍqҰɅӛŕļ\x99ŚȍÿΚʀŗƛɫÓɂѡГȢϧůѣѼɍɐƀ',
                                                                            'ѯħΪÝʲĿğ\x9eԝϳӑʅÅÑȐúԭԊΜ`RӔɭȿM˝ӯĮȲ˴',
                                                                            'ɺƞƶƂ=шѮǽPԂӴªέμ˔ɔǋõ\u0380ηɁ{Ɇхʱ\x89ЉȘϾD',
                                                                            'řԊßŕ\x94ӸÉɹRƺӕԔô`Υʪ&ζɷ˩Ġɉ¨òtɣʵȃvЇ',
                                                                            'ϟƥÊ"ȭЦɠªЩĎŨ\x84ĺԭȤɇƪϳú\x99ͼɓЮҞӶЩŏŨȎԄ',
                                                                            ',ʌτÒѨЁ\x9dŷ˟ӛđYõŶ˽ѮŞЫŏ¶½hʁϘĊ\x85ΔƊӥS',
                                                                            'ĹөƭƊĴǒТ®ΫαӲ±ʇӂқFĞXͿу?Ǘ\x93Ȑοѻżџǂŏ',
                                                                            'Ɔ(ҥԭͼτhԬĉǩĦĢʓżɿâϜԘEΞÍҖРӰΖȼƑƆˊȩ',
                                                                            '˓\x96ĴƯҏɎgǼҷŘ´ˣȆƮҐϱ˺ϙ\u038bΪɹΞȝŇaĎѻƷćԬ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˑûƗӽΡӔĄӸѿ\x9cƨӌƕқӠŬĵ¬ǖiѐШò©ԪǪц',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ѫ³ĭƸǔƤǅϦʲŀͽԨţ©ʈԈӹѩ@ώŁӦδˁċήđƍύ¾',
                                                                            'ÏK©ӺЊϏŃ¹ђ6ΆнŋǼ˘Ӂϰś÷ŽƢʸǝȉȎǀă{\x8bǮ',
                                                                            'ļ\x85ΨȴǹʅȅFʎòĽ%\x8eͻǏdīф\u038dκƔõʤɪɻɌҲЊюĝ',
                                                                            '˜ʊŎ®іЋǐƉƊҝņɃАӰёх2Ę+ɗɣʆϥƷɒѠА%ӏȔ',
                                                                            'ʕ˺ʵƘԐԌмƜ҇ƪ-ƐˏHǛñj¹ӗϽѤŤҬ΅ċƍųŕƝ¿',
                                                                            'ЍñϷȥóԥǝӶÑηǤ˞ѯԡʨΒ§ÂɑϔǼĊԕʔϾƯȔҜΰȝ',
                                                                            'ŉΈӼӁ%\x9dӓǓMȩ҆ÒɢžҪ\x86ʋÊ˞ȸƳĢΦɌƴ¥ёĉЛē',
                                                                            'ſͷŁУΟ}/ǥɬȑƌ¼ɣϚЩ¡ԕǇåϡłθˠǪʁғðÃĠ*',
                                                                            'ɋ\x90\x80ϊΪ˗ҮҌϛ*Ҵɴ²ȁɡsԭÕʜƘсӄӰӑԈɛǑҝˇʾ',
                                                                            'ȃàȈȽ·ķщϺʒӨe-ϖΤĞˊŧǸ%ϹмsЄåԔҽǡŒƤc',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'âԓǘƧÙäʯ1ӉόˋśˆǑƃêũґϿʞȼLÃԞˀҿɒαÎˁ',
                    'message': 'ȇ҅ºłƈӈʖ)ȍʤƂǠȄÞƲʃӄƛЌ=ƨӱǷƲϺÅ\u0378ɡʓГ',
                    'arguments': [
                            {
                                        'name': 'ÇȤөѬʈʼύɐˑҩV\u0382ӗпϓɅȀ\x8cʬØ˥¹ӊºį²£ǳƶϏ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            237636.01360249828,
                                                                            558321.6743613263,
                                                                            219571.3386771931,
                                                                            598170.5378749768,
                                                                            340446.0648962467,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѷĵκѾԁ\u03815ȫ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ζʘЇʕTԏʎηϬΣϼȰ·ęҽ_Ĳ\x99ψώȠƎ¶Дęԕţćʙƻ',
                                                                            'ɋӓ*ɰйǙˇ\x87ŷҾѣХŞ\x97ǀӠҸѯҿ˄ΣҙȐĜУԗӈϨԦС',
                                                                            'ӫȸɫшʠӂҥɐ+\x90ӖдτĒźʣϞϣĝäÄѤƯÒӬƤƭӳӌп',
                                                                            '¯ΉŎ\x8cӫªίɁЗυæĆ°ȧ~ѼǉҪϽʰРθ˸\x8bӎѠȑƈfR',
                                                                            'ǧʟҧ°ʄǶϿϏҘ\u0380÷ȺɃðſѼЂĴȗʔĚӰ¬¨ɹƥɞЮѿƀ',
                                                                            'ŝŇϡϷϏƟʎίƕԝӆƥɈ\xa03ӗѤ(fňʔίΤΦƸ¾ӰЦmȍ',
                                                                            'ҘȦƣҴӿȞľЃŒҔϋӠêĂƱȃý˴ϐʡsƄΏƭϱпǿс\x9aԓ',
                                                                            'ŪɸԢůк#˺ùҊz˗bĉԆҠΫˌϜÞӘȠόȏӞ˶ūүҜʘΎ',
                                                                            '}ɑХ\x98ĥԀǅ˪ԉÎФƀТħҋ҈Ң\x86Ӻ˪ΧЫǦ\x97˩ŤBĮ˛Ρ',
                                                                            'ˬǁӽƠ÷ïʗʵȚԮķѷŌuŕǀɤ«ȂƢɆʭʅȌӹ%ȜĖˏK',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƋǾϚǔƞȼˬǂϡȇ˦ȩˢԪƮҔӃЅ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            236367.24729094288,
                                                                            -73317.62416160111,
                                                                            328555.5284132071,
                                                                            435262.75243672845,
                                                                            838300.9087952105,
                                                                            300764.7826229604,
                                                                            347548.6631395331,
                                                                            804572.0074334847,
                                                                            534194.7356062293,
                                                                            -54175.8138167876,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': ' ӰˍAҤљ\x93^˹˼ɲ¥ӸԤŶК˗ЦŪ\x8fϏtƸ\x9fêӪzŢ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4966274258988838339,
                                                                            -5697199683283126912,
                                                                            -1613979255724168442,
                                                                            1307168473436445284,
                                                                            -6756375108186291711,
                                                                            -8014040200091899982,
                                                                            3072395993002655005,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѪǈΌюˠǽLĝ©¬ˀҐɲŁ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ĆZӟԛļŊê÷єģʭәŁҢԄʿӣǊƎҹeʘЇЇɗЀҿïȢŕ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -57291.74507143161,
                                                                            917080.0095515017,
                                                                            655822.8310765057,
                                                                            431419.79905811325,
                                                                            696083.7090282878,
                                                                            816424.6284072383,
                                                                            63097.90537379039,
                                                                            993761.2297521923,
                                                                            951083.7724706922,
                                                                            -19932.27312797065,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʨϣҪϹЦΛǲ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѹĲΝǲУԧǍӐʟ£ƠĦԏ£sӁԋҰҩҐȌɹŠƙεӗ\x9cѨÚÝ',
                                                                            'O\x8bʐŶƁƧяӧbǰǞNҫȼþ\x80Ь΄WõӀː\x80ϋɽǹČÈ6ɾ',
                                                                            '˂ũрӏ˟ƴΔ)Ȉ҃Ƒ\x9eҸԅԠҷϾɬFҞЖӇΛԨÂǾdˡύѓ',
                                                                            '҇ƒаġѱԀХԨȤƘӋ[ƾӓОlϗƯлԙȖЌѤӫӶ)ę\x9aɹ4',
                                                                            'Ъϯ˟ӜƢӒΖǴʺƧҶЎĔӣʀΡǺа{ÚǬӗǨÝ҂äаȕpИ',
                                                                            'ОȼʿƦԕ\x8cӯҌӸҞĩƘ˂Σ¹ÕìåµӋʋǾУζ\x83ӊњɾчě',
                                                                            'źǕĨćŵÑǥ͵ԞĔƚΙǨ]êθƺ΄ÊX)ǏԖ\x7f5Ҡ;ŒЭŇ',
                                                                            'Ȥθфγ\x90Ԇңξɳďǵ±˻ӞDƀĔƄтʜʺӲ6ҨТȁ˷ǒBǀ',
                                                                            'ŲLȪɁĩþгπʑÌҁQŞɐˣˤĕŝ\x90џĽӁˉƙÑȱӧȥĹ\u03a2',
                                                                            '˭ºĸљΟĄȯϫѪʫӅХʘНɕпåаԃáҿ²О,ԕĀԈԙǴʕ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƧҍˮƓӓĠћ¥ΐяӇϓ˗ϟĐБ˴ҋΙǃǛĻÖǧrԦϢŹɷѡ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȭǦƠϙлȖһÈҽϠ\x83йǍȃ\x94ÛԁȁԒèΩѡıͺÞʒЍζÉǒ',
                                                    },
                                    },
                            {
                                        'name': 'үѤǕ˚\x83Ȱþό»',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ˋ˝ϣʘ\x80ѽː,ӗ\xadŞдʵ\x9f˲ǤТґϤʠӺ˞½ӓǑŶіĖßϺ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'pшЗӪ¬ĠšϠûǊɀʾӈʦɽŚƽӻ¼Οx҄ԭТǼβȭҙřԉ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'øӸ·˥ńȝ·ѤƑωι<ÜƯ¬˴ɭZ0ɧ˪ŇŁχ"Sυτɴ\u0380',
                    'message': 'ήίǥ±ʘͼćϯǌǘǟԪͳ¢ɶēʼʹfɑɞӄӉƀȯΕʤǽǞΠ',
                    'arguments': [
                            {
                                        'name': 'ʷdӳСәĬѲ¸ԛАėƻίǁЏӶǇÉƟΐĂЙ˧Оҹ˶ʩ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ÎӏɢЇȷґæʴԒΒζĺfǁϳϨȏǺʀɭʺΓԇΓԊŏ¸',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1410518880378800792,
                                                    },
                                    },
                            {
                                        'name': '\x85Ԋю°ɚцҦ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɎĎӹɯЪӗϖȶξϡКƏҴҪӗÊϔιüǱȋŬуԎľƖԚȵԨΊ',
                                                    },
                                    },
                            {
                                        'name': 'ˡΌϞȎȨ³ȁΨ»ˇыR¡ӿҎҍӈӧҩʽїԖaɆƚƌԟқ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ШƀпĝˁǚʽѡУόОƚāƂҖЃ˶ʘ˩',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 878907.5310752167,
                                                    },
                                    },
                            {
                                        'name': '@ȞƁԎȖƑ\x91ɘʟMsȸӘљÃξ',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΒȈƪć ҥƇДΈҞĴН˞ŝRĩ-κ˹\x90ŃƚA-ȑ\x95ȏйCϯ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6122176914124454577,
                                                    },
                                    },
                            {
                                        'name': 'ґƍ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5604650436303936142,
                                                    },
                                    },
                            {
                                        'name': 'йЉĨNűǁЪıʗïԚґZĭ1ŀʿ˷ˏǮʨΟр˧ÐǦʈљцš',
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'əɘɅȞɧùŕͽEǍϢA',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
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
                        ],
                },
                {
                    'catalog': 'ΪʛƪȀĊ˧ңϞϞ˾ȯфʫǣϴŜӭŵðӲϵüãŝŁí¢ȇˈ˩',
                    'message': 'ƊӠʊɘǥԚɢ\x9dĐΉҍѲ\x83˯ѓȯFŗáǾÊϙ˱AĤɴǸkЊɎ',
                    'arguments': [
                            {
                                        'name': '¥ҍ~ŧ˲fxǄɯФčЇ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035011.221451:+0000',
                                                    },
                                    },
                            {
                                        'name': '÷\x84ΟˁųЈҞȥлȸӮЄяAƸ;lғ˞\u03a2ˎjѼлƢʵҬ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            355274.33475503395,
                                                                            941321.9841251385,
                                                                            680947.0607626819,
                                                                            398230.4334233837,
                                                                            993504.6304570953,
                                                                            53038.366335614584,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҨȶĨ\u0380ʔƎѕ˻Ґο9βȯԗĊǱtȼˡƥҜΠѼ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            707288.4643098237,
                                                                            703267.4440136503,
                                                                            -84120.37444786057,
                                                                            507784.11274160584,
                                                                            956192.2206865351,
                                                                            974898.7401818363,
                                                                            40567.69036217785,
                                                                            285495.8691075207,
                                                                            52740.01012320112,
                                                                            497728.34687128814,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŁȆȣǹıϫ»ȻʚјɦʠɐЄĽζ˛Ƭũ\x83ȊЋɟ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˠҢÃŹ˻ʔӤěɲƇĿϣËԐͷŜГ¶ƓEϐÉѩƌŭϺɖíщü',
                                                                            'Ӕē˧˺ůƗ]ϙ˸ҌŦǩʯԚ˔ĮψˉǘπμӪxҖǳť+ǬӾԏ',
                                                                            'ǸӺѨƮԫΆĴȯхØˡÌ˗ӫĖŴ±Ӄԩ\x91ƮÇę\x82ǉÒľ/ʄv',
                                                                            'ͼӋπȎѩĮ½ˈƃ¾˲˗ΟjoʼƗӂʉ:ɁЗƈĵǉ)țм˲ɹ',
                                                                            'nӅуԁνľͱƴMhϋʟ˃ГҺ˅ƟȎƳɬȵƩȽ-ʕɘͽҲҶŋ',
                                                                            '˒PƐЎĵԖɬȣĥ¼ɩӪĈŵŗϾ\x91ɴ\x88ƯϷțçŘɩ˭ɚʋҶØ',
                                                                            'Б˫f\x86Ґѥ˲мӁϊɨoӍɖԡǤʹäâȧˁĄƍŢ<˔ӴҺΉϝ',
                                                                            'ȀІʶǖǣǋǓŕÿïɍԤԜĂǛ˼đĥΠńɆΤĵҙ÷_ǈ1ǋ˼',
                                                                            'ԑɖӕbфxȰ´űņРҝҡѾɊĲΞͱċԒȠƄªӰѢʼ\x99@ӳǛ',
                                                                            ':ѣƙȇhĽУ\x96ːьſπнʗˊЦѢЦҒϴĝƶòͳόŔǧ˼ьʻ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'eԖӱπͶϨò˝ªÿΔӓҝǾҜŦĖέԏј˨˰˯ŢЙ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'цҪӭ\x90\x93ʂŏ˭Ư3*ŔʿӖʆ\x85кďΊӻЍӭɦҸƹ*i*AŮ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
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
                        ],
                },
                {
                    'catalog': 'ʲĿԙҵСƖɌғӥąЌɓΠƘ҇ĀɂŃӈӄɃ˃\x9cǽЊЊȃʬ&]',
                    'message': 'Ƨ˘ӘӉҫԊcӅұўĄ˪ɠĆҊϥʣӶӑėС˦υϗTԥӤҪƺŭ',
                    'arguments': [
                            {
                                        'name': 'ͽŷǖҕǙuҝɯĬǯˬҢκƆӀ\x95ǆuмӡͱӁ\x9czыǁșìώ·',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035012.351451:+0000',
                                                    },
                                    },
                            {
                                        'name': 'юҍĂыĝҷƝβԟƙҍϨȉΘʫÆӢ˂ЙԟϭˈДζêЃπĆƀї',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 24253781745875755,
                                                    },
                                    },
                            {
                                        'name': '9ǗѨ¹ʛ\x99ƍТƾΓӠŷͽʿǿɡРѡǬkϵŔOɦʥ\x98VԂΪÅ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            966054.2640253326,
                                                                            217552.63988350815,
                                                                            378654.1878930844,
                                                                            343527.56278891023,
                                                                            -24385.86844625567,
                                                                            260992.4170205674,
                                                                            -2149.794186921252,
                                                                            579380.433365024,
                                                                            155969.86188321188,
                                                                            971614.512433259,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'RԉƫŐͻMȪ¿Čа½г˫ҲӍή£ÖʭȻɕϹǝΒƛĥĮĆͱ҈',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -893890269082643500,
                                                                            -4123782679813130041,
                                                                            731649247323696039,
                                                                            -6203613859729306688,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ćҔÛөŉЈԐǏĤήЁ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210309:035012.865414:+0000',
                                                                            '20210309:035012.883628:+0000',
                                                                            '20210309:035012.900941:+0000',
                                                                            '20210309:035012.918087:+0000',
                                                                            '20210309:035012.934287:+0000',
                                                                            '20210309:035012.950831:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʰƤŗқJПОҭ˟Ȉņ˧Łһ˪°Ύғє9πŬǗ±Ǎ˼\x9a҅ľЍ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3363658487979075241,
                                                    },
                                    },
                            {
                                        'name': 'ǽyVԌɱС˅Ҁ˫',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Œ\x8eβ˾\u03a2ȩȋͽǖΧǅԤƝĎϧϸԒɬŪнƂȊȨ\x9bўēǏ˴О¹',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɖȠиũʠ²ơêÏΟЕҶŬϓщìʾǪӛɴŨ҃γ;Π\u0383λлȲ·',
                                                                            'u΅ӵԢфȿƥǪŤîϣŪϑ\u0380ȔɺԤêιʙɆЁhӸƫȞϏĮǏĞ',
                                                                            'ęȯɬƑƄȯԍĽɚ;ϩɄĹ«ӓӢʮӫҭCЈɆөjѨ8Ȓ$\u0382ə',
                                                                            'ԕиˮϼŹґˇġѾʁƏʢӥǓΣEӪĆщŤűȅſ&ҎMʬČŲӠ',
                                                                            'ɁlÂˉ\xa0ҰљƿʥŽɃ\x81˛Ɉƴг\u038dϕƧǾ˦Кɤ\u03a2ˮҾ˲ċԟţ',
                                                                            'ũѰɽ\u0382˶сȓϒŎŊóϘԭúЯȽ˚ӫďZdΫшӖcȱǀȪɖ÷',
                                                                            'ƇǐǄħѶԝȅČҟɈƩʱŲ¸ϑƳ»нҋ\u038dMɇħ˯ʈ#Ă|Ԭș',
                                                                            '˧ĽͿđĩĺóӷˆϯÕĭӪБªì˒ƅǶƿϜƶΧǑ\x87ϹȂėӄ˂',
                                                                            'ԔƄǆÂзӧɛUǍƮƁ\xa0¿ΜŌ\x9eɽΏ¢ĨӡÀŖƶѮƒȬÌ»Є',
                                                                            'ǠβNÍĒü;\xadӒɟƬӲĺ\x9dʹӫĉѻδęОãĺ-ä΄ĘŧEđ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǛғϘȵ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 123534.53436528955,
                                                    },
                                    },
                            {
                                        'name': 'ǚ˥˒ԅqԘŌ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7863958128649663033,
                                                                            -8900015683646284259,
                                                                            2726777688751718224,
                                                                            3315561527291852830,
                                                                            6900502223624899529,
                                                                            -6337965780764831917,
                                                                            5264580666481603262,
                                                                            -7031933450233877286,
                                                                            1203405970276932984,
                                                                            5797921865629452607,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʮ˯Ӈәʆɾ\x84ï˰ӞŭʭaɅʁG\x83\xa0ʚgʐΨƶŠą¶ˈ~ɃҀ',
                    'message': 'ȞϜӈĮőJĞͶkϖԤŴϫȣ҅ӚƞηɽϚÈ¯Ǵ\x94ԠŃˉөϺƳ',
                    'arguments': [
                            {
                                        'name': 'ƘyʆȄɆƈϨԋЭȊҹϲǍйȡ˧4ӒкώԝÄȌăќǦΰËӇϞ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˟ˣӕűɏ/Ҟűďǂĉ6ЁżСȏйȿɞЈlϒǺGϧϲÕ\u038d>ˇ',
                                                    },
                                    },
                            {
                                        'name': 'ѡӺ~×ϊƴN\u038bňԊ\x8fԍЀǭ²ĵȆˏѽϦȲԫΪƽѳϩΤǸяҚ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӢНŐŮԖΊτƐѩӳüɹˠŻүƟԦöʔʨ\u0381ǲˆõƨɵΛзήI',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7219351171758578027,
                                                    },
                                    },
                            {
                                        'name': 'ͱʟɲĀ\x99ӰȔԎ\x90ѶңʴâȸһĦǳʦŖȬзɢȸɿ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            812423.0247993064,
                                                                            898204.0327938073,
                                                                            446948.79592209775,
                                                                            138310.69203502714,
                                                                            20272.957630457284,
                                                                            837683.4231581966,
                                                                            641195.2762859635,
                                                                            985905.2882441252,
                                                                            647733.843522596,
                                                                            931105.0722382065,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "в\x9cîϲʻƮʯǹʋçvɑ\u038d'æČŏőΑġǴҜԟʞ^ΦźŒ",
                                        'value': {
                                                        '^': 'string',
                                                        '$': '҅ĜԕɋΚ҄ȋLlѶ\x97{Ще¹êfʫӸώ¡őʷӢʬľ\x87ʫȭͲ',
                                                    },
                                    },
                            {
                                        'name': 'Ԑ°ŧɄɯ˺ΎɩȇˠӃԚΞѪ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3226883632979552705,
                                                    },
                                    },
                            {
                                        'name': 'ȠԖЍÒ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3298775365284502492,
                                                    },
                                    },
                            {
                                        'name': 'ͱŁΥϛˈύθˬ˚ǲƼύЧ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ә¦Ĳґ\x93ɘĩ\x7fµłvӒʽҜƀĎӝ҄ѠǡȶɢĬ"ʕȑZƋˡΑ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -54360.77332069859,
                                                    },
                                    },
                            {
                                        'name': 'ʋьǻΨθξĭºѠIβωԬƍńkͻλµΝɨʩƝĞbǵѸ\x80ËƯ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\x93ѧ1ψǮӓ˽çĔÃωǌ˂˲ϋ˃ǥ½¦ÈǢȗĤƎÄƻчƥɬэ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "ƍ'ӚȽȯbҲǔ[ʝЮԤȑˣɒѠƟѹ³ЗΐqÿđΣ_æǄҮ΄",
                    'message': 'ɷ\u0383ӇӂƿѼύōäͼԁԤЂйΠÞϺ҂Ў\x8dƒɽɪĭԦõȃ=Ļ\x95',
                    'arguments': [
                            {
                                        'name': 'һѮáı\u03a2҄ŦȮбBЅƛԢ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7158523073744748048,
                                                    },
                                    },
                            {
                                        'name': 'ŉDʭʩŴÇʓϢό7KʯǕıУ¡ιĆµʊ϶ƻķҐȹѮȣ˲ˆ;',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʥ\x8dΝɔю˜ŏŮͰȢԏϮ^âɷåŮҼ\u0378úĭƐȱԡʂ)BfФŗ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˓ˎǕǭ\x93ҰǻϙͻǯžљȞË]Ƥ҉ʐǪƭѢӗϕϠɘʁɔҊ\u0381Ω',
                                                                            'ȕҊуƄłΐʭɯ¶ǯ\x82ʯϖũ}ӻc\x96Ї˰ɾɕɭűъǫìŴҔƼ',
                                                                            'ίˑǬԦӓ͵ƟzɷʏȏӑƦѽȝ®ҼɜOϥϢԔԪҞӁˁƅ\x8eӡ\x93',
                                                                            'ŜЛͽ9Ɏљ҃ƘȐЅӛŀɾȊʭǛƤˮҗΎDŔŋcbɼ˵ťΝс',
                                                                            'ÍщȌɷӌħѧэåÖı˃Ԣʝ°ŵƎϜӢĸ҂eΚǶĖѼţ\x93Ϫҍ',
                                                                            '˕ϫPҙưНξʯлͽħȱӑʣǉɲżƞƮĹӖ\xad˂Vцʇ¡ѐɗʊ',
                                                                            'ҫʅӗΈŊțȃӐ®Ӵԃɗϛҫ',
                                                                            'śФпŘЋȘ\\6ÓҨńĈƄɺJҭҡȳŵ¶ʂӬɼ\xadǠ8ъǆϸȹ',
                                                                            "ï˓ǍƊɧ]ϖsͰ\x8bЊ¬Ȟ˴хǡȫиϪ͵ͺљɜŢʔʈːӬa'",
                                                                            'ǵ\x97ĺкҗΕŃԩˉ\xa0њɂŸҗкИΒӰÑʎ͵ӛΐΓó˦ѩƲ£Å',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'πҥϮ·дιńʄĞǸӗâ˱υſо\x9b˹˪ǕˊӧƬʄ˦ӽȱǐ˲ȿ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035015.179835:+0000',
                                                    },
                                    },
                            {
                                        'name': 'êŮʾРŷϽƒκҦB>ŖǎƏϱÓεΕɻ˯ˤѰΡæһԗʺưλ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'hǙΫϕȨеϲŬδzɨǼ»ɻ˄ΛƷЅľȨӁȼüǉ\x85ŹȎŀĉұ',
                                                                            '$Ӆ˂˶Ҋ˗ϊɷӨįӽ΄ә\x9dЄŵʼˍӁȴʄғƮѮǢİҏҚɖā',
                                                                            'ʴăпęĳȍɇĔ˫U˲¡ķ¢\x8bİɓѣŨ"LеƏ:¦ˍȹΗŢ:',
                                                                            'Ʒ¸ШԞ!ƪΰæӔāǈɛ´ͻǉȩхуоďԘӞɁ§Ԉħɉɻ²Ћ',
                                                                            '҅Ҡ\x89ΚƬÕɫø`яxȢϡď/њIΉ¤ҩʪӎϦɱµ"фӢɳҎ',
                                                                            'ƙu˜ã·і\x9eɟˈɼԃԣ˞ŌкԛȢj˄оӝŌˬΤМυΒŁɹӵ',
                                                                            '"έǟƵәßфҹҎΰԔԊҠ^\x86ЅǲԨ\x8dЍ©Ȏ¸ÞʄƻɻЊ˹Ŋ',
                                                                            'ԎΧҔʁ^ŸЊ\x9bǧŏ˙ϼ˾Ƌȯɤ4ʢϞьЪԊǼðɏέҨȁȼђ',
                                                                            'ӗӰʀғѮБŔʎʁ\x98ŕłȓΔҊъÅйȑ˻ύĴǶТǋу¯ƯԡҊ',
                                                                            'ȵҬŵĢ6ΑƇ«˕ɁҴɨȒʉ*čϸǥӊêʾĄåђğХɼâǖ\x9f',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҿBʙΒȄпβԦʅϵԈ\u0382ӦÙǚʔϳCЉә˝',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': 'Ōǩ´όԠȂҼ¼ǟѩԌӬǠʁ\x8cʣџҋҿҡ\x9eſ\x80\x9aӍɿʦ˟ŭʭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035015.972209:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӞŊmǇƹβ\\ŤԊȾ\u0381ɎȥƜӛӚÛ˩ĮƈЭΘìѬśėžΕʸ©',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210309:035016.076665:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ˋɤƽшˀКϢ\u0379ǡӁ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2609859879274014013,
                                                                            1521543133500582600,
                                                                            5818543752365155579,
                                                                            978858631066641218,
                                                                            -4254744350791334819,
                                                                            -3415899543769358232,
                                                                            4063627920296880202,
                                                                            6808788979929731105,
                                                                            4613976469796762751,
                                                                            607376316398556366,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҰҤɪңԮҕ&Đ\u0381\u0383ҝӴtѽ"ӮƫƭѸ˹ȲȬ\x8cθ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'А˫\x80ȩǭÄІϷʵÉѝӗԎұɁ-˩ѰϨČƁÎ˗ėĥǡӝʧŉ»',
                                                                            'âKUòĥ)çрxлǴǏӷҌƶғӬщɉΠԌʳĻ҄ǏȞђǴłѷ',
                                                                            '¥Aԥ9\x84ō\x86w(ʉÎƨɽяʬϹҽѱ\x95ˎǌ˞ƌˇԉȈӯǵлБ',
                                                                            'ƸήѸ˫˝ƌQǮ÷¡ҊʹȔ\x88ȴġȪǂ"ɑçцűǹǞϭUOҗɰ',
                                                                            'ŌŅԑФϛF¥ѝ˚*ϯͳʙɎ\x96ɘӕ˩FưɳҼǎƦƩǫƒĕŏÜ',
                                                                            'ФЏȶЛΗ¾ҁ{ƸѠϥѥçƱǿ)ơ\u0379Ԭ/ǣǒӒΐèȥƏǭ˟Ǻ',
                                                                            'ХʹÍԃҞҦ˅ƔďʿƟνş¨ӗďƺôԟɕ=ƥѻщɐĭʆϿӁӪ',
                                                                            'ƏωχΜĦΛЈʘϤƍ˷ъɜÊЂыϽґҐЅȦbĆҺвɺп\x94ȑ\x97',
                                                                            'ҮȃЪʧŧόϊшөōçØ2ϻЇąŉϼ˰ʳŞɸʓěʚɬ˗˶ıȢ',
                                                                            'Ϫ4ǽǉȶό˜rȗ\x85ӆԐ\x8bɰ~ґлǜŴφʊʉƦηɸiҺЇӄͼ',
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

            'identifier': 'ͰąύÔŔ',

            'categories': [
                'access-restriction',
            ],

            'messages': [
                {
                    'catalog': 'ҖͲ',
                    'message': 'ś',
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
            'name': 'ΩʏҊ¶Ξ\u0380 ȁϯͺȋʧȭõɁќjƴŦʙı?ѨtmΗ`ÝԚ˹',
            'error': {
                'identifier': 'ǆĮѝ˘Ԟ\x97Ϛ¯φʞΡĆ҄ƓĦǴЂЛƦƆϡԭĴgѤνĉˡɛȬ',
                'categories': [
                    'network',
                    'invalid-user-action',
                    'network',
                    'access-restriction',
                    'internal',
                    'os',
                    'invalid-user-action',
                    'network',
                    'configuration',
                    'internal',
                ],
                'source': 'Χǆɟ˖Ƣˣï7ɖѸĈƿŭØbћǮùĬǉʽѵͺΎśĴƂҖʀК',
                'messages': [
                    {
                            'catalog': '˔àҧƻ ӥʆҜЭҝǁљ&ϐĉġɎHëüϿΆǉȎԤαǐήӸå',
                            'message': 'ҿӟˁўθȻĴƊǫӆԁʯѥśȪǲƜ˫PƄďʔŻѿșԮĭѢǯù',
                            'arguments': [
                                        {
                                                        'name': '<Ěƽ®шѪǦąӀħʏŸӃҔǖɇϰқ˄Æ\u0382ҙΨĢ\x8bӬʖԊϞҡ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2313226260808462874,
                                                                        },
                                                    },
                                        {
                                                        'name': '˖íˬɅҜ\x8aлԈÊчʿӷ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 612671.447096653,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ßxEǵ˳',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĪΧđǑƄ˰ǪԜ\x88ЁŃɦɤӒ˹θDžƲЁˣѕҨśӖÉφ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:034950.205918:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǚ\x7fʇҹ\x80ҀѢěƺʠòǱаʃϠϿȽŹĆǠ ŏȆʮϟƿӧ;˺с',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6094526305202829767,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȿƧɇÍǣѓψҸ8Ŕν',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Й)ʢǋåƭʻǊ˂ҿϒУϳɨÌΕǫƑˇ˝ιɸ/Rí',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'î˂ɨċňȁpԊǌϱȮƯʂǓĤʬÉûѮʐ}ԑӌԨɲĉÙsӷɻ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɾЀŞʄѥԞBɹԄĚҺԘоԬʟœҨğþԠΞԓǋӘДИbXΥӬ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǅБҩ\x83ͲήӑƴѳǰҙǀʽƝˇӻΌҼǎǓ˥˱QƁԦǾ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʚɦĆƺ˸ӃkǪŴBŌŨϒРšǰȜʝdǰŐѝ\x94ƖÝʄƓϤÛґ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ˣӧıɫϐäÙɄсǇ\x84ЏɤĻπ\u038b\x94ëǹДCȊԫѽЎɭÆŲǁΉ',
                            'message': '¿ӈϨϙӴƶsʩȉƥğĭġoñCˡӚźʔξίҾFnǒӶʹӢѷ',
                            'arguments': [
                                        {
                                                        'name': '\u0381ȺЀ˘ªŢš\\ʳηǍɪѫӴǵԫëҰ>ԪˠԬҎӨзӂƴǶ˄Ŭ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ò8ΣȹШĶӮ©˾ƎɹƁҩþ£ĊÚζž˽ŢT¢¥ξϴ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЃʆÿϳҜǟłŇƹı',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '}ѴӍˣήϒ҉\x86IЀϳĹĐˠ\u0379ҔуζĎҨļͱSЀʧc\x8bȶǵɈ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӿӕŵҞƻϣųƘѿԟͽ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӏ¨ţsɁ\\ʥʨȌ˛UǏ˛ОђʣǱҨʚ\x86ѻƞƘɋǌЇ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'æˮг\x95ӜĜƢҍϼˑȎӨКԝʻӮ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '?Ĵͼʶ˳ʇϨӢ\x91¶ýĝÙøƃ\x85Ô',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҥϖËĚǘƞϯƓòˮ˵ŲԀŰɀҬǐȦǬ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 446782.2154819139,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӱę˸ƊΨлLǫ˼\u038bǫʡĝĳϝŖ²ѰŲɩƠʖӮӴ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 203378.05394570483,
                                                                        },
                                                    },
                                        {
                                                        'name': "мǶΘñGǄӆüȇϙǤ¼ԚҼȿŇͲǾӽϬӭƚƹBɝú´'Ӎ˷",
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 697363.92607165,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ŽИʖ\u03a2ЌʳɟǬŪʜȇ˛ǩɚǡǎʃȉ°ǏƿˠǇҊǢł˪ѥАӉ',
                            'message': 'øƚҷӪ!ӱϊϬȌȭЧϹƒ\x9eԎԀÀ\x92˅ʘƓĖʵҟȇζѧÙϏˡ',
                            'arguments': [
                                        {
                                                        'name': 'ƟɚKȟɂ¯',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '÷Ʒ¿,ɚҟʏϤʇӍ\x9f',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8735714467864650812,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĚčˬȪњęǥȏȆΕ\x99ʹ¥έʈȼǀˆÑѯШƎ$ҋ\x9bԎ͵+˚ɽ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǀbǄмК҂ΒĵЙǠюѢŵʞȨưMԕĔоƺўҢͼԩãώ½Ɇх',
                                                                        },
                                                    },
                                        {
                                                        'name': '˃\u0381\x87ӟŹʴŁ)Ѽ˔@ńǮƶĉдɱǬИį¹ϐæˑϸ҈ȋø?',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'p¬ҠӅʏĸѷɴĹǕϐϚgқЫȸ^',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '°7ѷɴȨ˒ȈџюдȹÿĘέȲěӭʈǻОɱĂ΄ҿʸŁ˓ѝǥñ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Qʿ˰ǰОϭɗѡŤǫг@ŋϝГΊeўԜԙԤŮƺҐÕƷɝ=ůƺ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'èҠĐɰ˃ϯĵƮφ#˖\x81Ӽɝ˦F҈Ɲ\x9e',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӐĶԥƺƖҐǷUҾıϜРҘϵ˙÷ĀǍɸǱǅѶϠЁя',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '{ě\xa0ɞӿnȑќ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'цҀÑȵҋ°īɝϿȷʍɓѰͶԉ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'чӒƿýѰy\x99Ԇ˂çįβɚҌˏѭӓ0эӢӋϓŗɃȝ\x93×ϭĮǸ',
                            'message': 'ſ\x9aƯ˘Ѐώθ\x87ш˟ʘʫ\x95ʗɳЧӃϟąЫ%нʙ˃WƵʟʂь˫',
                            'arguments': [
                                        {
                                                        'name': 'ċȭкx\x9aíǇĠ҂ԛϪϿÊŬȁΗlš\x99ʃƇŭӮóʐƖҷʠĺΨ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6502412894789040579,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѳҝ˺ƁѤ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǵɍρѰϖΥ¤ȋĆŃ\x96Ҥ҅ΒØӻԜʚ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 619891.7531762114,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɽлƈ¥:ҊʑʻʉĄĭѧ}ǦгҴċʋώǁǛT҄È&Ҩйǔțӧ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʹĔҍшĖԕ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˁѦӊӃΏìȽ%MԔҩc^¡',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǳɥGǕǆβǷɉŁΚϒŜΈǟϼĕ;ҰʓӣАμЫԝчųџǖбΡ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǪƆå#\x82ûϻԆȶ˫ŨԕԇɌ˚',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'σčʞĒˈɸ\u03a2ƌ¶ïʲɊƷƛɆµӧҵӚʋˁǊɨMӑŎѵψȽԅ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƥųƕɹ҇',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӚюɓīǏSôӸʯ\u038b\x93ʅɌĉ˱ȽѾʋøҪÔxǍȑ[ѽт Óƚ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɉ¾ȡӊɱӚ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȜIȹ\x98Í$VÞȦĕŪǈƮӇˢʑҫјʲӀĩҦ@Ίǜєýȕǀ˂',
                            'message': 'ҙΣӳЕFӖұǌȖŴΧХŨ<J©Ͷԍ\x81ɡÖ]ҿʚiԫÁϲЪǈ',
                            'arguments': [
                                        {
                                                        'name': 'ʐԭһɫъ¤ЖĤү¼ɬфɧ\u0378©ԇĭͷзоŒˉ\x95ϗē',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '|oʜ«ԇ\x8eĈϷΩ\x94ҺΓџ\x88Ƥ҉ƛӻĴǽ`ƋëɖӪӃưӂǓƈ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 130520.00691121115,
                                                                        },
                                                    },
                                        {
                                                        'name': 'њͽőѶºǜˋѯ&҇ŵȈѭȚĘəʱѬΨ˫ҘɥɲʧɩǆςW',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'КԣСƾ˹ҖČӇ϶¢ɂҸɻѮŪuɿɷΣώɢĚrԈӾƲƦėƮЈ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʈКǭɉѪ×ǿĤʒǏ\xadʖφήdȷԣǵϽŶ ЦΏɍʜ˞ǭĔɤӬ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˂ĈОЅўɢ×8ΑДhďȼiĳ\x81ӨˣБʈɎ˲ ɈЎэϑʣHϰ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0383ӑʽɨҠʃɀ\x93Ė·ёҲҁʲ Ǐğ«MԇДĄύӑǇŐæяúҾ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĻНʐҴ\u0379ȲŵѲĵεÀÍ½˕\u03a2ЖˤěͶȀƉʕɍәԆЋųЀâ¤',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҩ§ԖˣȲȀιӵυ;ȇϰƅĔ|ĦƂÔԒԕ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϏƅЙЌǊ\x94ŸɶBΨ˟ßơ˳ҏǷȻӌËϾƇ˦DҗŉЧãŪţȮ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԣ¤īɺɣӯԃȭ»ŷâ˱ђņƓ˭ĄaȇõŻҘϒѨƢˈɯɫ¾҇',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǛԀǩƓѡѤѸŁȂàˡƑ˜ĩίϾŞ\x98ƻΰΗѨηԍϯƹ#˧<Ӿ',
                            'message': 'Ԍǲ˂ԆԂΡļцɏӇʧxҰ϶ϲÐΘʒi˵ƊÍз©\u0379ʇðоɍƣ',
                            'arguments': [
                                        {
                                                        'name': 'Ʈ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Έʃ9\x96ЇRėúĐȱή·ΙĤɍƅΟҹJǡӷϜЈɠ˹àЬ˚Ѐʻ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'XʠĤЕ\xad\x87ƨÀЎMӗşñїɨ\x84țϟĸԄ˘ӇˢēЮɓ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѐаʞөќԕԄӝдÂȧ(ӈǱӊʙǋŖūԭс\x88ǻʹѽȽ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:034955.494276:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȾřƵɱϙ~É\x83ФȕɽÒǘͽ˸ŔΙҭƂŷ˃їúʘȜ\x8dĺ0Ș8',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¿ƑÊŨҹyщӠϑ§8үʡȇɌ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2428836072013612819,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÌéίțѱNԚϝȕТOˇ˯ȽhȩŌ˰әǌ¼Ќл}\x9bԛΉӯ\x90˪',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΨȿȽ\xadΔЇƃȖàбэŤͻϙ.1ƈиɹɏˮӣ\x8děʀΣł%Ԕʃ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȋЧͷʾý˻ǥĻUǞhȲ\x81ËɣæӭӪ˭ıʩ[Ͱ˞ɌόŕԊҕþ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƳѐȚ:ǞΫdģƘѹįǀЭїċ\x92ˤΏɆҮѩ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': ';ԢĢϠɢеăȲȪ˪ѱƑξЏ|ΨҪāӑҪԕ\x86ƛƃPТϝҽЂ#',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŰϗŪghƠ\x85вӃҨ˄ώǔƦǩҒѺѷΝƼğΞǭŉ8ͽԭÎȵ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˚\x83ԔʜΝӓүѮʂâď$ʴƫͻƶ¾ҏhѷ+<ǐƴÌЮαɲ˻j',
                            'message': 'ÌЏúɭӖˬ҆!ˬѹӢδɶʹȣĉѦʥȷрѬũƖƱ,ƕѿȁǡҞ',
                            'arguments': [
                                        {
                                                        'name': 'ԁǗǴųёѳ\x9dϵ·ξùÇƙūһҖЋąΙȳϴɣ˳м>ˣÎ˦Ɠƿ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:034956.162325:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˾ɨŋӑͺOƄȈʏĉԬЖʩҮӯ˸˛һҴś˅ǳҥͻŲƄҀ¾ͼʭ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8766912162743493263,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƞЮͺѼҦӞ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĝȸɻΤƮɂțДӺɨʟδȂԮӗΓэǽїԓȔ\x83ԛǏʇŔвϪƉȩ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҶäεЈNϲ˨ə˒Λɲď;\x7f΄Ɣ(҉бԝƯʡɆΡø=ӏĬƸć',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҦΫϜєϺ°ԥɭÁˬѾǐИ˄ЇŤÛˑȩΤϫЍƸʤʚůƸȍ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѻӦϼӾǑʣӰđԚ{\x85æӍśѺͺ\x9e\x9cȓтŁ0ǡͻǆƮǷțΧĘ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɜ¬ʘ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ίo¡#\u03804ӜʰѶ|',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʙÞǮҫƓϸΰȟН˖Ρľ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϼΞŀРɌаĎa\x8eЙɰȲ¯ŇԬͿӾƊŧʐǈļљңɮOϋǦҫȴ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƀǥϘFίȲ\x81ʛͶ\x89гţϒɊҕЫωɹÁTȤĠʁ\x8dБKр×ȬJ',
                            'message': '˦ЏÌ\x88ԔCЉͷőФ˲ͳĂӵϐΰŭȏɲԒЭːӴŜĦ1ŅĊΆƄ',
                            'arguments': [
                                        {
                                                        'name': 'ҠȩҒȩşѽƱЇγd',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7983988876850162411,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĢӀΜɷΑҤǎ˶φ\x9bêԖӐĄ\x8dΛ>Ӛh²ɨЎśОǯ˝bēЍ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 737750.3306409662,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȁҏɰö˼ȃФŤϬԧÐљӊƧ"9ƺϭǰþ¡ξ\x81ȍɯѯĐθ¤ʩ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɳʒ|ӱϓѠƠƗ϶ǷʊŖțÝlʲ҈ůËӪϴѶăϽ˽ŜįΞ§F',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'вĠӘԬ·θƸʿ϶ѷʼ҆ӏϑѴΆȤđӦFԖ҃ɏÉοҗӷϖʡˋ',
                            'message': 'ȘҚɃӟбƺ˚Ѵǀ1GʹԟºқńиDƗçȋ\xa0ΒʐБȟԑɺƕŠ',
                            'arguments': [
                                        {
                                                        'name': 'ёȎNǯǌ½úqĲ˽ƅŧ˻ȟˇӠ͵ʢŦϟĞǶȗӶҌ)',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:034957.555879:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '·҃×ďɰϏȏӶсХðәɾâȻΕsóϻҢʒүʸŚҌ~ԛ˳ΰϼ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:034957.635888:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϘѕжђүĭɎϴω˒˲˭ӧФà',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'оȏοϒϜ@҃Ƕ>ШǮɈɻɉѲЧӔΔŔ¬ħňұŅ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɣЊđįЉş\xa0ȇǃԛɬӷǫJԇʺ˰',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȦэÜÇЎȪŽǲsāӰŮʁӭýėНúǗɑ˕ʦ\x95ҘŵʬɑĚ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'κĵǖŮǭιÔЕöНɑ\x94Ќσεŉ˗¦Cxѩƫѥ\x84\x85°sώѾЖ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'fт˯ƇΝǛљԋƺȹϢѵΛԘǭΓԗȅɲȹӔӒ&\x9b',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210309:034958.122609:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ž˚ɗȲҨȫǦƎƻ²а¬iΰԒʭҘԏʰǀɯԉʮŗĳԉІίʭ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'гųŰЋȕȴ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˾ĞʇΜΠP˕ҾĶƲӯӧǫŀȅʖɠ˪ˡ`ӘӞґϞЬʐȍйҡƁ',
                            'message': 'φq£ȁѣ\x82ˉƽϯÆǚҮҔŞϼǇğmǿ\x97ÓʻԑÆǂԃϋĕǨƕ',
                            'arguments': [
                                        {
                                                        'name': 'þʹԂˠӱƕ˥ɰҧЩоԛҜƞȚяǦɱδѥǫʫԀӁԃ\x81ʂΝδǆ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĥζǂĜԟѬΊ˹ʽŷƢÅ©ΏĀ*\x95ÂАŀԧhȾàƄĻțϽҠҋ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 833835.5077146697,
                                                                        },
                                                    },
                                        {
                                                        'name': '˴ԓ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΩӝьĂʡɦȣz˙Ȃɛ|ӽƹБΌ˺\x924\u0382ǞöǱԣʮŎӵїǯʚ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƨˊдҟǛѡ¯ūŏϽËϑͰҒȶˌѧ~ѧǊˀҤųӦŰǄӹʶԟȧ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'óèΡëŏ҃UƇή´ԪҬ¶ȨlȗӮҧϢÞҼϬӁ˯%Ӳӽſϙ^',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʲǆ\x8bѶ¢ɅƁiϨǖ˘ЪԈŐ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԫϧԊĀȺîљ\x8eĖōʷȸɻʋˤɝҝωɁҀӦʃòųέԦƄӐӃ҄',
                                                                        },
                                                    },
                                        {
                                                        'name': 'GƞҨɭȃkҀ¶ƝκĎ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǐvюɌĩԖȹƋwͿà9',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4416807918071985635,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʡψԕԇyϰśĚϡÆƷ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Å¾ù\x9dAƤϺĩԅÃ˟ɰʜłёϳͱԌЏ',
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

            'name': 'ԁѢɭ',

            'error': {
                'identifier': 'ӨΥ¦Ί˱',
                'categories': [
                    'configuration',
                ],
                'messages': [
                    {
                            'catalog': 'ˬԫ',
                            'message': 'ǣ',
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
            'event_id': 'ә~cȝт˷ȻϣɞĵЎѯѭèÁzʣɏǜӖġÞɇЪīыҠ\u038dŨĭ',
            'target_id': 'ϭԋԭ#ԣiЋǣыyΓƌƟȋӁƪοɱØʹł˹˄ÄӞðСӬ҆\x9d',
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
                    'event_id': 'źј[ǋÖΓХŜ\x8eĥĬԥ\x87҉ɤȪсήɶχԐ{ғԉǹǱˆБѬǕ',
                    'target_id': 'åȒԮC\x8bӄŐӢŶŶʣÔțǮə˓вԫ͵ÕΠĳʴΧáȂ\u0382хϚ×',
                },
                {
                    'event_id': '΅&ìʋЇ',
                    'target_id': 'łǭɾӮȜԢ\u038dˎӼσӉɩǅďł˝«ǽù{˃Ƚχλ.аjĐĢҶ',
                },
                {
                    'event_id': 'ѼN҂Ǡ˥ĨаϲŌ˴ĠҺAZƤї˱ƯʹǶδŃӈӠӲѣĄ˟ǉX',
                    'target_id': 'ӥʀºзʕ\x9f\x86Ԅ˟ϳjĥƘԘȷzΉϭŞǆ\x8cаͻ˫ԧgȿЬԚď',
                },
                {
                    'event_id': 'ǣІʄ΄Ɏ˙ˈӛȩȚɐʓÌʨΊҧ\x8fğԭʨɋ˭ÉѓŻȍҐӼφĉ',
                    'target_id': 'ԪԈЂÐӖqӭɐńȫîҀ\x8e˷σαѸѯÄґθЏήεЋԈȂƅρì',
                },
                {
                    'event_id': "Љɕ°Яĺ|ʃԑżЀɈȯԊ¡ǑԊzźҁʵ'ƀΐ˃ДɏЌĩÿɲ",
                    'target_id': 'чhʐɜҴǠȘςąŌԊң˕į\x95ɘəȧɉĽƘʏ{ĥKāJ˅ÂǾ',
                },
                {
                    'event_id': 'Ĕǽ˧ԚίʄЄg·ʜȯʝĞԇ\x7fѭǮӄƍЮѧÈȏŃ´ԞŉʚÊӽ',
                    'target_id': 'ɄɗʒrȎyŤѳÒĺÀȃʭӾΙζϡӅЅȐʺƜϫϋʕ˛\x81Kóc',
                },
                {
                    'event_id': 'ʨǩǲɉϝȿԊēŖɫԮΎҰАѢÐʇäϠҹGȞҝȨӠƎʤČŵ^',
                    'target_id': 'ӣԡȡĖČҚʩγɡϘԆɧүЙ˟¨ɹþǻˢԖăӦιѕЬζКрҦ',
                },
                {
                    'event_id': 'ͽѹŗǁƺЇ;(ӻƓk˙ψɿœШː&µɂϐѴZčǼоȊӘ˖П',
                    'target_id': 'ȒÉϲƿӂҎŊϷςЕˇͿÎѴәȨѐγüů8üſȬZͺӋDÞҊ',
                },
                {
                    'event_id': 'Ϧҟǝ\x8dŢ\x85ʤҠ˷тԋĿɽɹʒēÆ\x97>ӯɬϛŮĉƊĆɍȜіˡ',
                    'target_id': 'ΘŀnӊҌʉ@ҜϏĐĨ˂ȝǤ҄ɷƼЖΫħīŌů\x98ư˕ͺԑ¤\u03a2',
                },
                {
                    'event_id': 'ϼʊҳҬƕ=;ƙҳζʏƲȵɌƑżīϢŭУŌˋТƝЈ\x951ϛ>ʹ',
                    'target_id': 'ƐȟŐ˲ԘѝҢ˵KԣеГʾˇлʃΈ˜ȊśғýҪ³ǙӃϥѮȹɓ',
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
                    'event_id': 'МϘͿҕĚ\x98ЅċʨӌΖƗΪ\x93ϝɸҧȵʎůȲâƗáOϤӃ˓Ôʑ',
                    'target_id': '˃ӋїҨĀʟ',
                },
                {
                    'event_id': 'ÉҋԘѫǇʂLԟҹȰaԍѥα"ԅдƹȍΑӾDɈмČͽ˷үκҵ',
                    'target_id': 'ȟǛƞĭȊαЕǾƖȊɟНΑԆ˘Ê˗óŻЍΚуТүȰǂѨǶԓΗ',
                },
                {
                    'event_id': 'τ\x95ǌϋ҄ѹȞ%ˎˑǻϙóĵɌҚԬ#ũʵȇ\x8dʒϿҨťČĕŽӷ',
                    'target_id': 'ĳʈțŖƲӆɺƑӿӋûԒϭϓȮσ˛ҟǦԩ÷ƐĊȪБ)ϝϔŖƽ',
                },
                {
                    'event_id': 'ıТĽŐȹ.јȽ\x81F%ś¶åʽ\x88ʎǖɕ*ΧΩΓ\x88xБǯƚЍƞ',
                    'target_id': 'ƱаЋȺ2Ǣȍ˖ǮĹĬΨ?ζӊžɶҨҵ7œʨӦϠĆӇɒӇKƠ',
                },
                {
                    'event_id': 'ƎÔ\x91ǲůǜ˼αӨɤʧΐюƝӃ5˚ҌӨҜȿѮӷɭϵĘӄӔʄƤ',
                    'target_id': 'һːφĶѤŋı·ųÙUʧƛþҴƶɳɢӖҵɚҔǡϲ\u0382ȻϺҜ8\u0382',
                },
                {
                    'event_id': 'ԇӿǈιǶǈύǄȥÀѣƧǴЩԗͺĦȐ\u0378ђяŦЛȻҳѰжÀʸɐ',
                    'target_id': "˥ гˇҽсԈŎҵù¹ԄÿĜԤ'\u0379¾ȍōӈƉМǵэԁáʡҥɘ",
                },
                {
                    'event_id': 'ѠŴʹҧƯɞѺԇЖ\x93ԘʭƞǁśȂ\x86µˊҋƀԃsŢԕԦ\x9a_\x8a¼',
                    'target_id': 'ԊԣΦŘ>ΞӑԈӺőшůʚϖǮƶԢɆοӻŲʫ©ɸ˟ŇǄƭʉЙ',
                },
                {
                    'event_id': 'ʙ\x80ϷȆ«έˑx·ҋҰǸǡӅ˳úð˗ӃĠɿùǂϸʎЀҤǲœӀ',
                    'target_id': 'Ϸӌҡɐ\x8aӥ\x89ҊɶԔЕѣЭĹҼɡλϸ\x86ȝǾJÍɲǅ\\ΐɧƻų',
                },
                {
                    'event_id': 'έа˸ҮҔ)ɓēşΡ˙ʚʱUȲĐήК҄',
                    'target_id': 'Ȫϒʭʹұuтԡȩ\u0383˲ƦΤΩƙ\x95æ\x96УΖ¦òυӫΖ\xadʬɃӀę',
                },
                {
                    'event_id': 'ɖɐØќ¸ƙȽơʉ\x99Ω˒«ÀԭԓwϗƤŃȔƄϼ\x83ӓϔ®ĩʊ҆',
                    'target_id': 'ΨΨңˑʬ]βǭȈʶӰǝŀtӒōӧ®ԒĄȈʳӇαϫϞĎӔáа',
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
