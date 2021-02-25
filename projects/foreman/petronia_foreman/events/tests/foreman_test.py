# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-24T16:40:58.334338+00:00

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
                'όŃѶɩɂӫɨѭ´˳0WËώίñ\x9fŗЗ¿ŒҴÌ\x7fә\x8fτ˭ԉƭ',
                'iюȫΓΧÅăҞӥʰȶο΄ɺЍʠлγȀƵ©Ĉʐ¹ʘǚGʏβ\u0378',
                'ѼӧџɂҎĿϩԐįӬИʟÀɼ˫Ǡӽʻj`R-ˀѴưĴщĜǔǅ',
                'NɸɹȥĲԎiΓҐаˋˈѺʄχаtŁЇȨȜʴѝӡ\x834ѢǠʵˮ',
                'ªҰĽŵƊÿԡɻƁɾҜ=ǶˎЖԟΐeΆəЖȘѩļúЗјñșǰ',
                'ĢŻřɣIҭʍcůƮȐӘÄʋǙеɔϽȈǖЩƈ\x99ӦϊĉЬ˞ȇN',
                'ǒƯЗKΊϛЦ҈ѐ˯ÙҨ÷Šæ\xa0ϱѯ˖оӎʬԄϻ(ҕɩҿ˜V',
                '˱Ӊԧȷ[ʩȺӣȒԎȤжĻўӉʱΣƣ˶ƔπϼЕѾ÷˾ϯʹɌ˩',
                '.³ӐϕȊʎĝƾ0ДϼӔɈ»ӱʹԡǼɕԐ˃ӹ҇ӲːȨŬԄƪϭ',
                'ĝ²ƹȂAФįƾqƝӒȬѝѽ1ϾDŭ^Îʨ\x9dţԎɸΆʭϴĒ\x9c',
            ],
            'source_id_prefixes': [
                'ӈŦ\x97ͲȁӛX³ԐZŠŔҶЎʾďϔÞҤǄӒʌͶӬЋԫЩԜŘҤ',
                'ӑőΕȒӾҲӌĒƉńɶɗȉЋћëѽҿϩ\x9aȯԫПĘʃĕʨʣWҴ',
                'âцѦZɞƎүϓ¥ͷѢƀыȍˤϟáεWͱF˾ŔúӞ/ќÀæΆ',
                'ȧжΣȹ7҂҇ƉǫԞġøºˤǄɩ϶ŷҠɒǿ@ƉȮŞ˕ԬƱī;',
                'οˏԢҡĀӮџǁэȚh҆ΌʡȄх˷ɴԔ^ð͵ўλжΊͺцə|',
                '˾҆şԡŶł{ʒ΄ȵĮϳ\x8b¡\x8bраŅ˼ӬҩԔυĎԄÚĸΦȄƯ',
                'ӯʕЩȲ\x9eΨʭιɾɒȢ˼ǚЊҐҖҴҗŏĴǽЇԆ¿Ǫƹľӳ}ğ',
                'ϳǉϜǔʹ®ǅ\x99:ŖϨƈԪ˩ͺѥˬЃǅŋȵԇĒ\u0378а\x82әřŏJ',
                'ӥЏƲϾѹҍǛɩ¯ʓĄȝҹР¯ΈѲʙЍԜʩû϶ǹϕŦЋíӄӸ',
                'łμÛо\xadʗĭtʥ˘ĝΟØȩïяюϾʸЛʅńɈӬԢщƒȚLӮ',
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
            'action': 'ͲҷѸÄíϲFҾϩC\u0383ȱ0ą\x99ƻţЭ˵ìȷǃϙϱaĆϧ\x8fΌ¿',
            'resources': [
                'λƂŸˉͶЂFҍЬȳüЄϺÃļeȡ˺ʞɬіƠ\x8bϵˈȲȓ§ά»',
                'ʵϰ\x8aϴ˸Њư¦˓ҔŝQɇ˫ԨԈʜϱĆ˥ʐѫ\x90ľѫоίȓǭɗ',
                'ӠєǇҽƨƂ\\*ɃЌρčʊſ\x87\x90ŷȖЛяѶ\x8eʃ3âүĶsɲÞ',
                'ǀPsҝŕ˕ȺǆҜζƯĆНũˆé;ʀͶМƄʐЀ˲a҃˒јīӈ',
                'ůϭȒŖɑċɘμŖˈ҅Ӽ˨\u0382šԑӔų"Ѻɬɖȑ\x80cɍ\x9eČΙˡ',
                'ӰT',
                'ǲǩåΔϬɸΨȋЃӖӜȁͽ˖čӲȯϬOǇ˘˕ƗɣäЬЕŴƏˇ',
                '҇ģԎůΆɿÑǸmÊʻϤѫŚ°ӕмЫΞȯ=СͺǯӮΏӓџȑԅ',
                '0ԑҀFҌɳʺɅʴŉʱĉ*šǦʏӬɏȥÎԆˡŧҼΥɩ˕ŇʙƇ',
                '{ƷήцĜcԧɖӰӝЫȂk˕ʵҙҔҸğiҨȓ!İƌőԌʳȤ\x7f',
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'action': 'G',

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
            'name': 'ӧſԌ_Ƕ\u0381ұӥūǞǡѠMӠ˛ΐ˷ƵЕҠϬɕǙΝϠ˄ȆΫуʀ',
            'version': [
                -8557775348880086346,
                -1125499993340447324,
                -2159841974222948201,
            ],
            'location': [
                '\x81ӱБ˸Ý˧\x9a\x80ԁyǸƀӂ\x9aÜ¿ʐʁ7žӺȗνʠΘҳпǱÎЬ',
                'ЏԜʍɌȝΡϯ\x95ȏ`ÈũƞˇŋgкԌȵ÷ӉņĮĭϛɷ«áбǐ',
                'ÓӏϟԟȄтоŸӤьʱȽŏ\x84ӆǁ\x8a4ȫĔŉ\x84ǻɺƐӷóðԬ\u038b',
                'ēɷĊ˯ПԭΟŌɭʣɻʿ\x92ÓǩѢˍ\x9fԋЧλŠȕєǺʝÄтԈԖ',
                'ĈĆԜ+ѮȪôùʘњǬ\x98tſ˸ҏΗЮӢƯɾŧÌĽь1Ӎ\x86ѹǌ',
                "Fİ\x8aîşȽԤ±ʟɿˆҾԦɶϱˤĒАʾ'ӝõ˝θɖËҺҖдǇ",
                'ҩԦӁǑơѬȐϽȇŭBТÜ5ўʱɼȼƍϥҲƜӉ\x83Ȑ\x80ϤФҲ1',
                'ȍͱҜǟ%лӻΑúǗBӧÖϧΑҩ©Є¾ԃЧŤÖΦǌǤәțĔŔ',
                'ҪϺш˭ȇγjIϘǂΧˣ˧тɷŎәůќβɑΆ»ʨΑ¸÷\x89Қԭ',
                'Ԍǹ˞ӻˏ\x98pȡȳФȞҪɭªšɺЭɹʔOǻͷ<ǰɿċɊЂƋν',
            ],
            'runtime': 'lϱ\x82īēРŸk',
            'send_access': {
                'event_ids': [
                    'ƞȶ˗eɷ-ɩџӡ¤ˏãѽȲλѲ"TǦόºʈѿųͻɭŐŭрǉ',
                    '$ԗ\x92łͿǬԆĎǔМϤ\x9bʪžŵ\xad/ҟȘιʚΤƭɟњ]ʁөып',
                    'ǑR\x9fǑθĝҡȂXЛsΕˈƵяӶʹAΊ0Ū¡δѩŻʺt˄ȅ˙',
                    'ȍсϏΚ\u0382сaЮƿɖѰˋø\x87ӠũɝэiˢӟѥͰѲ˔ȤѺ\x89ĉȈ',
                    'ïƯϚ\x8dëфąΤģсƓΞȋʲNŇǮ\u0380ϛӗЀŐїͼ¦ԟҹƴУr',
                    'ΨѺѦ˦Ԇɗқc\xa0ӕԅ\u0382ЇļӣÛhтşТoĸȲђΧҭҒҬQſ',
                    'ʯϫƿʛНʆģåɖ°ÙȟΖŠƕҫψϘεŚƀЯÇțEg\x90ńшɢ',
                    'ҟϫɻфv˻ҩÊԪΗˢŧǻΐ˭İћ˱áʀɚɱǔǆɑěӍɬԩʿ',
                    'ˏ5ǦӫӪѢDˡOȮǺƽǐ\x8bϤҮɽĸŁþЖԬН\x9b;Ѝχμĸĵ',
                    'ЭˎȖɝɡӄÈӉ˄ġŗ²\x95Ҹϒñ˯μōΥʹ¶ʠӑˮUƯҊ˃ɿ',
                ],
                'source_id_prefixes': [
                    'ŉО϶ʦĀ\x9aǎăxŀ:όӣәƼăːϤҲđ·ʾϘϪγΝ\x8fvϻ\x88',
                    'ʙÄǈ\x7fˏϱЏµ«Ɩþ\u0379Һ5¸ŢŚϱ˒ͼǹʻӟόŶӣɥɥτƷ',
                    'ҥÇʄǮ}ŁȂĽɀ\u03a2ƐԍŘϝɅŃ\xadϖМˆͺɋľК\x8e˃ƸъЉϘ',
                    'ǛĢłѻ6Ė»ɧҾ\u0383ʹ\x94АţɁ6πЮɓШPƋìέˬDӞӽ±ˈ',
                    '\x96˅ΖƃбӲƻǔď\x8aʯа˴Ő˅ƂŻϺԭƅԣŀ\x85ӵʏҝЎПƲѐ',
                    'щ$ȗ_ɒØpˋƍʲ\x87\x9dŢМθX5ŕʒɷӗǃσAв\x84ǿѡʬԧ',
                    'οŮ[ȵčзʪԧ!ѽӻӂƾѮЍӨóɒǑƉώɲ`тЦϕ˾Ԑѯӂ',
                    'έͿΠӮŬòĩϑǭҝˢˢ¥Έ˄ԍӜϲ˳ſЪӱŔύҒˤΊμоɅ',
                    'ИǧЍьɜĈЉӯʪáӈѭӓɦôŕԫʂќŜ\x96ʔǲĩТȍҹǸӷʗ',
                    'ÉϬϡǩԚѐ˾ʞɆL,ҭøϧѥˇӟџԏÍΝӹ³ϥĻϞ˫ԊҏҴ',
                ],
            },
            'configuration': 'Ô¢ˎɁSÅȋкӥϙʒ!âɍǁ*ȬǾҺüȁҼӢƞϳĴ½ˊŵİ',
            'permissions': [
                {
                    'action': 'ӟȾȟҜЕ*ԎʿʆЋǂ#ļџÀǝďƥҤϞщӞϘϑҧȿìҗÒҊ',
                    'resources': [
                            'ӑӤμ˕һʽ˥БӿɭņϤÍҠǇǥʌƹџŀɄѱр΄ѠTÿ¶҇Ǩ',
                            "ïξкԨÞìǬǃƭǪΦǀϜņҰ҂ȢΒ]ĺѥ'ǩǒȥéɑӯϭ˫",
                            'ϸ6ʈәҊӷӜʖңʄȃßάƉϚGÁӟ\u0382΅ȰIӱәŖHԬ]Ӈʇ',
                            'ɧιŸɬӔɠШvКҵŌ¹öҰИԑÙеφ˥\x8d͵ʘʾŖ\x96ˆŷшӛ',
                            'ϋ϶˖ТĶԏԥɚƫðЇˀ§ŰȣҟήɷӂĆνĄϏәјơѳ\x99ʈɦ',
                            'ϲԤІԤӜӰʆƚFѕƓ_ý҅˯ƖѻÍʅƖ˦ԥ\u03a2ҸцßTɏ³â',
                            'ˌ¥ѸƷ@˶φӑĠćɸðӴũљʚϺƈͷšĠǒĔϧѡы.\x95Ű1',
                            'ԋQϲƦƢϚł˱ΧΝȵӸʆɽЉŎЧјюЫĄňʪɿƗDγŹʱІ',
                            'ˈсąOҺ\x9a˝ρʜdɿˈÉт)ŕdñѝʝ.Ÿȁ˦ȏЄBԭЬǣ',
                            'ƱϥʇҬőyʰ:M\x87Ƿ\x82˥ӫӢȘùƹƤþЅѢ\x8cϔтìЛǴƬɀ',
                        ],
                },
                {
                    'action': 'ЀӹŰƘѻɣǦƄ6ѣ²ÐɨәӸҚˈĈѨŚӤȶɊȻšɉȞ˥ȉҚ',
                    'resources': [
                            'ӃʋÏΒ\xa0ˁɽįŕï\u03a2˯óӐƇʹНņĤ˧Ǟˋ',
                            'ɗƚӔƚҿȇӋÏԑƞΥҽ\x8dǑˋƪäµɎ\x8dŏ˫\u03a2ϔͱVϳϵϓҡ',
                            'ØВ<ȻҞҨћȁϩӼƊ˗ӎБ\x9a°Ƿ:ӕ{ҨώξϩŌėĎҹˢ\x87',
                            'ƞλїгмϿ¹Œŉ½˧ɆбѰ҆đъήïɢƍɹ\x90˅ȦMЄӀ\x9eʋ',
                            '÷ƝѿíʝԎũҔ5ԅΓђĢī˗Ĵŀ&˴ԊӝƻˈƛΎИ\x9fͳΟƌ',
                            'Ҩ˴ϯŇſǧĖѯȪƵ9F\x90¬ƭҰӉĒ¹ɋҰʤʸϥԐ;ΒNˀҨ',
                            'ʹÂҬɸʷЇИǚǩÀϩzН˔ƜбƥƧŉʆͳӢԊƺ$Ԇƕϭ˒ě',
                            '҅\u038byøȣ\xadʁњӄ˂˰ΖʪǫrӆϽƍ˳ϭСuGΎʩ\u0378Ѯʄ÷ʅ',
                            '˻ƆΞӴaӝ-ȭˇʆɨʡȍԬːΦԦÊΤÍ˖ȠǳaоʳëɝАɧ',
                            'М˸J[ȊҧŨɄʑ˰ӱĤǚʮõȺLșȏǶȸʛфʹ\\іɍϺɣȤ',
                        ],
                },
                {
                    'action': 'Ɖ«Ⱥ£˭Á˟ŇǅɢԍμĨпж\x92sξӊHΖǮ£/ɱԭɿɳ˄ı',
                    'resources': [
                            'ύхщ#ӟ¥ɻǴ҅ǮԔĝŌΌӄ÷ɩɁÛ˺сѯË¨öʈŁjѧԟ',
                            'ƺҪʖȒˬʩʽώҪăδV\x86ӵ¼\x8c҇ďŶϲʎçƱǒÑяʖû΄s',
                            'ĞзϱƎȾƦȕːҺ˾Ѷ]ΜӖԮƫӳԒÐĵ\u0380ŝ!˰æȧȈ,ӒΫ',
                            'űѱźɡΏ¢ЗНİп҇vԫƖ:ҭɔχҟӺЏ΄Κбʵұ\x9aԃԚǩ',
                            'ϛ˶éɴђŽȨȤԭļЋ\x9fhΜԓ\x80РқϸЄʁóǇˢȵΏƱЄıһ',
                            'ҶϢ³ԆĔѢġĠϰуĵɫſýΩʖϕɟǟӺђ˵ĊąɦƬͺ\u038bЄю',
                            '˨ʹІԢ@ЈӹƧɂſťnƄԈƁʃØʃɉwŢ˥˔ˬӨԫőˏԔÊ',
                            'ɚԧɜԒlȪ¬ƀӂÇζͻƬÔ§\x82ŭ¸υǤőȈзεҝǍļԙӊԀ',
                            'ӯuԌƸѶʴĬſҒǨ˙ƎBţǙӨʂƽȉѻȧɌŋϠ^ҀӾƪЇҠ',
                            'ʨгƩХ҉ɂ˥ƫɃƪ\x9e\x8b˩·ү&ЛӖΏƟԛӞʷŢīŭ˃ŧǝҀ',
                        ],
                },
                {
                    'action': 'ƶǆҬɻȿƏäƞϠҾ',
                    'resources': [
                            'Ѵĺу¨əĞʦȶÌɶЌʓѹΒÙǖɢӝɵƓəԠѺőʍйˁĩȌʐ',
                            '˚ǶñӘrҡ¾ɬʛűҜ§ÝϦ\x88ѱĹѼҟʟϏ\x8egűƃÏϠȥçä',
                            'ė\u0380ɪЂ˽şοþ±ĂȚƝžéǅйÆčԭҚMҠɁǏӠʣҒ)ȹʔ',
                            'ǆЭΨʌęүÒƝɜǟϭͽρӑˑԚѵĜӖѡѲ˝xƁѹeԃʩлǯ',
                            'ƭѶτԅϣʺΟɓĜӁЏ6bƒǒҫїŦϳȣӑЛˁ˩ƵӛϒȺńЇ',
                            '\x96zԁɷŗđǂ˟ȎɽГԊЀƠĘçҕŞ˦ŸљŅŦƮӘĢéƷʂʎ',
                            'Ʊ\u038bΚДˀϲ£4ҶěĖ5ĎӡņɠiʄϑͷǅΥΞ\u038bӆǈŢƝ˔ȴ',
                            'ϝĸ˲ŭƵϓ',
                            'ƒé\x87ŔθƷģǯϏв=˅ҾԓўРbųċο×ӸƀɬǊАϤ҃ʺĄ',
                            'ŋҰȯ\x94ǽ˒΄ɹԪѯˮԜŦˮрɹԄϛƄѿѓʌŪhŤжŗ°ǶȞ',
                        ],
                },
                {
                    'action': 'ÌӡƚŨŗ]ӗԆҭǊ\x88ÓğİɤѷĹӴ˛ʇļ\x84ŘţԎʾӒѴԝΞ',
                    'resources': [
                            'ХɽϿǔ»ӪξʍȂƖƢ\x8cǡ\u038bҒ˙ΘϲԬŞʋӽŖѡӖΈɑʄ\x92Ӱ',
                            'ƈřɧ˥ƣҒъĖ;ƁUӧġõ%ҤŕĖɓфВȴ\u0381ɐѪұAǬĵŅ',
                            'Ӻ˭ąљҬ\x9cʵ-Өӗфȼ\x97\x86ȘãѩŞ˪҇γʵɔʩķưǴɤĸʳ',
                            'ͼ¨\x8c˃ԉҧ\x98˵ÑԙԕяǁύŤľϴ@ѵ\x91щ¨˜Ȧɪ\x98ҟ±ħ(',
                            'мӔͻйŁŹѹԬàɟʷȯӑȌČЇÖ%ҁепĐMԟũԄʍ5Ūӳ',
                            'ʱV«ĸȱɚªʐȩȾ÷êġˌҤĹĭ',
                            'ʭǲԄѷ«˰±Ʋӡ½¼˼ϤҦϚÅʴ\x99ʣǟŭɍѥèǩԣ\u038d Ѯӱ',
                            'ѧӀΠ\x99ŭȫz7˲ʚʤ˴\x91ǖͳvç¢ɋZӍÀϏˌдѴϴͽǖï',
                            'ҮĤӤАɫVœԃ\x91\u0380ǶcĞӢԂƁвʦAíãňŁ˜ĐšǮчͿF',
                            'Ǉҏ¯ȞɈвƧжŜā~еÅӳӳҩǺƖķWȩǤɺʨɎ#Ƈп·˽',
                        ],
                },
                {
                    'action': 'ęǯĈȥΪ¿ŧԨΝ\x9fУȫΠϦЪňȷϔ9ҚдЏƈνϛƳΞʊхΩ',
                    'resources': [
                            'ϰ¸юǅşБЃʘͿ©ŷȢѣ\x87ȍÕƛӫųԤǾϿĺʉÆƘȄǌЛт',
                            'd˼¾Įʱů',
                            'ΗԜ2ˌώӆϑԭΪϒԐҨѨɘаȿȏӁ˖ʍ˥ͿrӐОǺǦ©ĒǤ',
                            'ӼŵȝŔǰɮƍÖ\x8c$ǃɔêØȔõǄӶɲǾҺОƒЗЦ˵ҭƑưȽ',
                            '˸ȫGϼLŠȰwҦљ§ʭɺӦľԚˑ,Ŕыľі°ԁ\x96˒1ɟƂȈ',
                            'nÄʥŁȢҧƜѤΧţѥŝöŒҫɏIҋҶ¸ƭɫԁ·С\x90ѥσΟu',
                            'УɣƂ˳ә˺ΗóćǢ÷űȲ&θŠ\x9fОҼӴԡ͵ƇʍģǬԤˆrҙ',
                            "ԘĹǋȖ\x92ęl}óƀƷƘɀɇ#ӗ\x99\x96ɆƦ˯ԨѝľӱF'Š˚ɮ",
                            'ŇĄŤ˯ƿʝЃ&ҽņϰ˝ßҫgʠʍԐąģǺ°ɴƟƞʪΗʃĭЇ',
                            'ԆΰȥǺöȮŜӐъɃĄƛԪʋҹ˵VʖƊҡЁ¾ĤˉƟƔęĉѵˬ',
                        ],
                },
                {
                    'action': 'ΒǼΘЎĸǁ\x8fˤѣȾÅʑHԫĔ1ʏȨ˅ĥŀϨÈ¿ǦÇ\x88ΥǕȜ',
                    'resources': [
                            'OƥʷɳԑʦȏϪųǇƽϯюʕԌƗΕҚхƃƞɞҨԋӭʨɐǏʪЈ',
                            'ЧȩȹʱˡѩҝӲѢ8ɒĸѤԀʱʕΞ\x9fп˔ϫӗȆгĽǣȸΞ\x81н',
                            'ϋÐɤȲӋҐħԜǃХғΨˁҍſƔ\u0379ʌΏҺҕÉĬåęҒФĘʂĈ',
                            'ƉұŌȓ˓ĽũƎϺǱĠƮǮЂПαќĽͽѓ˗ԘԨϨҨƂ¼Xʋɍ',
                            'ͺʆƦɔң҈ǀūȱɻҺΦм\x9dШўϥаƌϫc`Ҕ҂ӛѣȓɶԅȴ',
                            'EΞɍ҅əάŎđȌ]ǿƐƳϾĪǈЎ;КĉŒ˜ȳӑЌҊ×ЪϰE',
                            'ϲɚ˒¹ЬʹxɇѡӧQhǦʣҠɞʌԬϙ#\x87ҹĎƬǳȋ¾-Ĭf',
                            'ǙшΨѵuƪFӦɄςɰӌơɘĂͳIķԬɡʀΣǁǾIĽ`\x81ɮɸ',
                            'ͱϤCs˒Ùƃ;ϖӧǳΨʢËрʪΌǗɜĸӡ\\ȀñǋɧΗ6Ȏр',
                            'рˉѢʀƩѨϣƔȇĸ˵ГĜ\xadȷԆөhɶȹή˷Mϐȟ7ƅѦӼȲ',
                        ],
                },
                {
                    'action': '҃aºÖяʲԞҕΨҺ¬ÕSɂŉˮѪĝÆѢΐΚǠǵňʔȯnƂʮ',
                    'resources': [
                            'ʨĨĹϺņϪ[t=ϚÍȓҀҲϲγȏºƖŰʩѼэ\xa0њɘGƋͱ˓',
                            '\x91ʀĉԊϕґПǴÿӧž\x8cǺΡơų$dїңËѭ(ѣǩɺə?ƴĳ',
                            'ÌўJүϥʁѮ¼\x96Ώă/:Т¢[μԔƪǛĸҶɩ^¼ɏәƵϱǬ',
                            'ȷύƊ\x9bӜϠ¯9ԘUλǵȿʸ˝G`ȎƉʹˊɷεóœ\x8aɫЖӖƩ',
                            'şǮƝψǓëĕʵ©PȟĸˣȌн\x89/ԩ˦аҔrʿˡŋkȖgӺr',
                            'óɚɥœ\x8cϟ\u03a2űşːӖƁģʅԨĔqϽȓċȎӕȚҖӏѰʹüԒǳ',
                            'ԄҶԩԙӀфҋǟʹ}£ϖǆCáĩćϱʖѲ÷һáƬɭğҎ\u0382ѡӢ',
                            'йɌԘӯ\x88žϿϱӢяӬǟ<Ɗdɥɖ˂϶²ƍǾωϑ˹ΪӴϫǏΨ',
                            'ʖѤͰƪĽȇӛӞƒEʲǏωԪϱ&Цä:ЉӝƮьɲ҈ӆɧÏѾɰ',
                            "Ý'άJљǞѬȚΑÜʋRƽŋƹƑŒԜ\x8fȥɀѮΠԦƞǐɕİρω",
                        ],
                },
                {
                    'action': 'ϲԫѬӦřŶċƤЇӨˌʰҳ˜ª҈Ѵ¸ɣРȜƺȉƺӒ&ƵʐΧȤ',
                    'resources': [
                            'ЂӕœЇ\x85ͽŻӗÏɥ˟ɒˣӈŒþȏ£ψԣȃыӌłͰǡʍΆϔӏ',
                            'ØԧЋӠɸİƍς@ɹԭЖǤƲҸȉȬǤдɸƄϔʒˮԈϬԢȞʞȟ',
                            'ѬƽŇ˕҂ŮǳҏԃԪΊðÐvƢēȇ˯ѐȿĿõĦK҉ԉΊĩϖŎ',
                            'ʧӡɛ8˼bǖ˽Ƈђсǣ¡ŢҀ',
                            'ÇӒȮǔє¨Ô˟ʅ6ϡ΄÷ψƮϴƍȎдßȋİР\x8fmƭЪҢâҏ',
                            'ȚԃϪɚșĖƱԦţӸȸÌÔĭŜɩǹĠŤɜ¼\x9fτȺϣќɵĚк~',
                            'ˠ´uƏʃϙсȪŕȼQĸŬĭɊɀˈͱӼҷʐǝыӿɈÂўɚ³у',
                            '«ľŁϨ½Ѷ1þ˫ɌλHŎ%ɒɺҰ½ɗŦԥŃȜ¦ȶɩʒȭɤζ',
                            ' źȓ˛СэŚ˾ԈiЕҵƗ@ʱϖ7ԒKϧ\x8fńœΡƉǌ@ŮѺ6',
                            'ýӠʐˍԃУ<ѓǌƠΆşĐː\u0379ӠĮ\x9dŘ\x93Ƅ\x9aӕύƃɏӉ˰ŀǋ',
                        ],
                },
                {
                    'action': 'CĊ\x8cµȝϜ\u03a2дӇSĉф÷ԗšʟʖͶZĦǜ϶ƍǾΦӁɹͿԬŞ',
                    'resources': [
                            'ΉWҍ¿\u0379±ʟËûԬyŨ˪ҢĆ§ΉÒԫ;S˅1ͰϠйÂʬǕΉ',
                            'ԑ\x8b\x84ȘȨnưϾ҇ңΩѮʿ\u0383fƘëǟӬоWǹ˗ȡɞɡӾFϞɕ',
                            '!ƒӡˍˣĔǌŧΕŷОŴɓKґԁͼǕȐˢ\u0378LŔɍʶŞ\x89ÃЅù',
                            'ÒµŶңʦˍ˦ġ0ҊΊӶǨƭǓ\xa0ɟ;ѧFȁε=мɵӳɪсѺK',
                            'ѯvӤȳƿԭ\x99UœȥȞΨ҂уŋXʴçʕƲҽԚʘҿȌ˂ӣҗ÷ω',
                            'Ƴ¿ũ¥!ǀŉǕĈ',
                            'ҟŗԠgºʡɱҙ\x9eʥȴϛдɴ ȟ\x8bìŰǯăҼӞȢ\u0382ʗяĉʏɦ',
                            'ӥȺɆPͶӮΌԆӪΘ\x87ˊƮ˸Ԡɚ·AӔƌȫӽiҙâηεeԪŖ',
                            "ěȲ\x8cμ'ŔɲsϬȴѶʊȿηɃɮҏƽȻćұƖŋҼѿȟщ¾ƽj",
                            'ҁѩԒ?ΡɋhɽԢУŢӬʰ҄ȇ>Ԕӆ˰ˆ0:ЃƛаʰăÃȦǺ',
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '˫Ƅҩ',

            'version': [
                -4028875384203109485,
                -2278559652490032873,
                -5852974434964266639,
            ],

            'location': [
                'Ή',
            ],

            'runtime': 'Λ',

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
            'name': 'ŉŧΧͶӈő\x9aʇ˯ǲư˓ϺŢɭҔ\x9aҷӗ-Ĝԡöˇʆ˫ʡдRё',
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ўĳ\x86',

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
            '$': 'ʤӍǳς[ȵ§ǣĳ£ζǳɦΚѹЋfjѳϫϺˠ1l˗.Ʉɗʡ»',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -5567867660651337390,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 121423.560735879,
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
            '$': '20210224:164058.265895:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ΉĐ\u0383ƏѢšķƴǌЪȾȆӞȡɓҼ\x84ƒȑʧŒӏȪŧӃ¸Һǹщҙ',
                'ȋϘϹęӈȁϗΒӇΉģϾ8дȟʷɃџΕƪûËľɪϟ\x97ķχʡƝ',
                '#ϖφ+ʘȽ˦oпϩҚʌʿʲϠͻǘԝĹ\x9fŔΤӹЌԒ˺Ѓ5gƯ',
                'τ?ԘYз¡»΄фǹѻȲƨи\x9dѲǠӴȼŔǩӑøɞʩ\u038bYʺƼέ',
                'ԂѥέƋ\x85Г˞ҘΎ©ѶфǓ\x82)ΰ°ͺԙǡҩ˕+ͼĽıŧȡƱл',
                'ƳѢˣÊў˘βǛӇДƴĥƨwҠʟ¹8Ũѧг\x9ećҎ3ʺѝňǯB',
                'Ƙ\x9bͰďзљǡɣȹϓҴ²¸ΖѱϤƞЩΥЩԣpϨȪ˕ѵʀǟјī',
                'ýǂʋ˳ʃЃɖ;рƦćѨņӗϿҝΡŜưȐʝˍӾʀķɞ`ϛȇλ',
                "˺Í҉ƭǬȏЩу{ȣȝНѰЁӜ+\x9cğ\u038dΔԗHŠ'ƒÓƽŧɭǎ",
                'ˇШфǖФаʯϽӫԞїŵďԎOŞŢɸùƄh¼шʋѝǷϘϞ7þ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                2298359928411361011,
                -8206441455690536537,
                3389463622953065437,
                -1223876002251107358,
                -1584127585848139278,
                576145793014756420,
                1940419133245825090,
                -4733800992557284684,
                -3602648209280696019,
                734633363894153577,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                231848.04054338188,
                377867.0824163977,
                910484.974922042,
                623263.5742974794,
                -6301.387262588803,
                585892.3327788021,
                104841.99019218457,
                291860.71390233625,
                127502.10654972776,
                403804.0244216949,
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
                False,
                False,
                False,
                False,
                True,
                False,
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
                '20210224:164058.266787:+0000',
                '20210224:164058.266800:+0000',
                '20210224:164058.266809:+0000',
                '20210224:164058.266816:+0000',
                '20210224:164058.266823:+0000',
                '20210224:164058.266829:+0000',
                '20210224:164058.266836:+0000',
                '20210224:164058.266842:+0000',
                '20210224:164058.266848:+0000',
                '20210224:164058.266854:+0000',
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
            'name': 'ɮ¼ȺľɴņχƬĠžˠιÿԖƼʼ>ȓ',
            'value': {
                '^': 'datetime',
                '$': '20210224:164058.265672:+0000',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'Ƨ',

            'value': {
                '^': 'datetime',
                '$': '20210224:164058.265741:+0000',
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
            'catalog': 'ϱĨ\x8c˘ϚнңöЏΰƙјȕʒÞӾt˰ȗϚЇԑԍ/ĺŊǻÕŢԁ',
            'message': 'ҀBӅΆԈʘŀӦǏΊӡŽϓĔϞ)ǮЩÜʺŪ«ǾƵϑĸԚ\x84Ӄʮ',
            'arguments': [
                {
                    'name': '˅˕ń',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ӍԙϭϙǬԂԕÏƶѓ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ȣŇӒÉθƕȹӢǈ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        984965.6000339808,
                                        62371.9923685026,
                                        748823.3289319103,
                                        988486.9317674472,
                                        823339.0221206823,
                                        173900.82345897082,
                                        270670.1987548811,
                                        839605.9776301977,
                                        -80025.49064627664,
                                        4661.085943308513,
                                    ],
                        },
                },
                {
                    'name': '-åĳơɿ\u0380ѯ˨ўlíÍСƥΕïˤҵÀsΙȂґϏΙԑж\x91Ý',
                    'value': {
                            '^': 'float',
                            '$': 45645.7864080306,
                        },
                },
                {
                    'name': 'AΰɾĚ6ǇƉƁѸ˺ӕiȢǫŰ˴\u0378ǴɄ³ÎΕѰʕĔʵPɆǓ\x9a',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ʭ\u0378Ţȴ¦Ƹс',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        '\u038bΙϦ\u038bǾƋğͿҕˀEȑʚįҁԭ˓щʈŮǓåϴǗӈԤӎӮΔʶ',
                                        'čįΤĲǽÅ\x97ӭϩÝ.ɻŐɸҮȾϤȫƼϾˮϗφ˚Ξ0ƿϪËԞ',
                                        'ΛԣĞʼб\x89ȄvkŢҙˬ˕ʜ˲ΐϭʸßѐȱϗӵ˭ќњš\x87ƪϕ',
                                        'äωЇӂƲɓţWҾӥΥϙ,áʃzϙЦƻӘ˒°ӼҫǦΛͱԦΤΚ',
                                        'ÄԜ4¸цŽÊ*ғʀЛʜƾ˞ƖǃeԀҮЎĶőƸΦǁÌˋŤʐā',
                                        'ϯÏtNɘʒǳεфѫѣǮі҈ʤʾЃŵɢ˗tυҫȷʊ\x8eÇΊЁȻ',
                                        'ΘѧǮˠȔǊӗχԛӃȻƕĬҚıԩʾΧӑǍˎʍƔǰΞÂŠđӇ\x8e',
                                        'Ȭ˓ʶџʧǥǫФ\x9bĢˠ&ә҅ƅǺ\x8aπΧвϽœȬ6ɄˣѠŔ0б',
                                        'AÐԂϟѺΔ`ơягĠӞŭҫșˣ\x87đ\x96oΫˍȲ\x9dӖηԋȐgƿ',
                                        'ΕΧŷϊ˜ΔӅ΅\x9a(˨ùɯŸϦ`1țÕфȒѨŵӴ_əӪÍҨu',
                                    ],
                        },
                },
                {
                    'name': 'ЀɁɦϥŐϏʹ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'Š¦LěĶíȚŽΜ˚o',
                    'value': {
                            '^': 'float',
                            '$': 735963.9593153157,
                        },
                },
                {
                    'name': '*\x87Ӟ§˂г\u0380Ԛϗ',
                    'value': {
                            '^': 'string',
                            '$': 'ǫҷȤȉ˒\x8erđԦ˸ǹɕđĒдΉԒҿѫҗӧƕ;ͲǪϏκèЖʂ',
                        },
                },
                {
                    'name': '·ϷŅƹ£į˄ĺќѨΎί\x9bXϥŀȩ\x93ӤԘйρсµ',
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
                                        False,
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

            'catalog': 'Ƥâ',

            'message': 'Ʋ',

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
            'identifier': 'ˮӣǱЕќɢqɘȺoґӃ}ѳҁҏÎv˰ȲǩήɏZȴÜϬɂɂЪ',
            'categories': [
                'file',
                'os',
                'configuration',
                'file',
                'file',
                'internal',
                'configuration',
                'os',
                'internal',
                'access-restriction',
            ],
            'source': 'ѯγ\u038bƑȆƪįʼ',
            'messages': [
                {
                    'catalog': 'ҕƼѮѵʀƬѣʥΰ˨ϗɽŀĺǣƿѺӝјӻȣɉʐŴIԗӨҷŻѕ',
                    'message': '{¿\x7fϬ´iʄȜʪӝә¹ԗˎŪѮӺΣɫԂ˳˦ԡÆτ˟ӴϛƯʔ',
                    'arguments': [
                            {
                                        'name': '¤ϖʉKÎРĚԈʪwǽ\x8cǇįӀH\x95ЌȺ°Y¢ȳѸÿɑȐҦʱű',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѳɄ\x9cĻОŧþaԚà£ąɄˇGČ·¿ʍˇ\u038bΜÈʮ*Ķδ}Σ\x93',
                                                                            'ӆҗӦӓȴɒƐМ\u038dҞϧȐãЕŞеӴԆKΤεɋӹʃȗАӴ˪ĨƏ',
                                                                            'ȳһqȀ\u0379ºśĺ{ǣӭӮťȡĒɶǣѱȢО?ӼãїŒԩȈәǥӋ',
                                                                            '«ѾЕϾʌǭȿĕ\x96ԅ`ƏϠ\x96¬Ʒ£Φǲά\x9fƹϴĿŗхѤ˷Δɑ',
                                                                            'ӣҍ\x8fӏ\u0379UOƶɖŋhzǃƧǃҥԤɗӂæѶϩԕȕΎөšїWǅ',
                                                                            'јȗĻʀϔѺԚϷЬɰÉƹ7ѡνǔúˡŤѶoǹ\x85ʎɌʢÅõѩţ',
                                                                            'ˢřĈәŬͻƨγѿƞЏӷ\x9dȊǇ¢âȢżdѼʤ^ǉхƸѪ\xadϻψ',
                                                                            'ԠsĎԘɢч\x87έ\x8fɜɷ·ҧϘĢēΰoȷӘʟǊǇy\x99ŠűJŶȄ',
                                                                            '\x9cӢȆsԣӲ¶ÆǉђÐϕƌȾķĭǦĪ\x9fѪϛ\x9eãϡʥʟǭ\x8aŁϝ',
                                                                            'Ɓǒοҽ\u03a2ȑƛУҒ5ϣσȫġӺЙЂӗԠҙʅʛϏεȀӎƙΉȈȤ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƊàɏѝňξźѝηĂĄǨƀҐÑɇˇʠĚȬÌ®ƉǘȃʀȬ\x95лъ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
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
                                        'name': 'ɢŋŮĩƐӧdʢ¹ɠˉt\u0380ŅȾ҅þŕԮ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164058.238319:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɅÉюҦͶ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7174628472573362390,
                                                    },
                                    },
                            {
                                        'name': 'ñþϽ>Υ϶OҤвɢХƉĤɍȤѼϏƼʮ\\hÁԫɞǣ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 881210.0861237533,
                                                    },
                                    },
                            {
                                        'name': '˥фɾĶθ\u03a26««ȆӶӂĤʃ´ϡ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2690604047703155857,
                                                    },
                                    },
                            {
                                        'name': 'ËºçŊԊŐԊϖ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            635450.1781298005,
                                                                            -36586.71583412738,
                                                                            541460.8049214588,
                                                                            583833.3168974809,
                                                                            307467.0862717368,
                                                                            925420.7952734428,
                                                                            169565.1405218941,
                                                                            29302.169176721276,
                                                                            919453.4791768383,
                                                                            46537.23297909973,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '^εӅɫĔƳ[DʗӠЧҸ˒ΰЕʍɤѮƃѐ\u038bё:Ө`RКωӻȾ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            298664.68106011057,
                                                                            26148.866456219606,
                                                                            912458.7048172917,
                                                                            461765.87593511224,
                                                                            290053.13182550535,
                                                                            -40333.96536922895,
                                                                            604300.8420503805,
                                                                            312075.54446963733,
                                                                            472739.9307483443,
                                                                            477466.2350937916,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "жȐơͻθυĬB_ʏэǅVǁњѨǮԮЍͼΎԗ˝þ'\u0378ο˩Ӫ",
                                        'value': {
                                                        '^': 'float',
                                                        '$': 159615.22349635442,
                                                    },
                                    },
                            {
                                        'name': 'ƳƒȕÿɟÄȝӽţӢǬЬ&σѪʯ·υĨȧЇ¼ǤɚϹŁ˓ńьж',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164058.241153:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӲιÄßъŹæȔĘϐϩ:ҪȌȽӺ\u0378+ʂĽιԪɅÅ®јιɿ˸ɿ',
                    'message': 'Ӗɾ\x91ϡАɟʩƈȸőôʦΥǡŸ±˞vʹɤɎӏȇѫˁͲʭȥǛŒ',
                    'arguments': [
                            {
                                        'name': 'G',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164058.241602:+0000',
                                                    },
                                    },
                            {
                                        'name': 'kŃ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϷȤҽFʠѫʑǽƖkͲʑȃЮχƗòӖÐӇãǆĞǃƏƫѮŴŷҵ',
                                                    },
                                    },
                            {
                                        'name': 'ɃčкΏɷǼӨĤƵŴĮɖʵЫ §Çθ˚ʤȡʞѥ˅õǎĵ\x81Ĭμ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            9188574440819803827,
                                                                            -7056831696157425160,
                                                                            -3966422215921097238,
                                                                            4979265158645768371,
                                                                            -8411599538044287238,
                                                                            6545529773398278094,
                                                                            -5100379232099655917,
                                                                            -1910082885737004614,
                                                                            -8053283228918709504,
                                                                            -9194151775257875740,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΑmѭӘŗѥ¬țπгwˋƝͲã«ƖƀҔ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            255092.03701390716,
                                                                            893435.1937362647,
                                                                            519527.76550327544,
                                                                            382388.0008637809,
                                                                            -6174.541053415,
                                                                            -93184.42998848249,
                                                                            42002.27679689042,
                                                                            643918.51530247,
                                                                            333969.63029585895,
                                                                            603273.6481736765,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȧc_Ӂȭѵώäҋ˚ĻŰʐāƇǜǤҗŖ˄ңHƐΤϜѴƂҕȒʲ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164058.242460:+0000',
                                                                            '20210224:164058.242476:+0000',
                                                                            '20210224:164058.242484:+0000',
                                                                            '20210224:164058.242491:+0000',
                                                                            '20210224:164058.242497:+0000',
                                                                            '20210224:164058.242503:+0000',
                                                                            '20210224:164058.242509:+0000',
                                                                            '20210224:164058.242515:+0000',
                                                                            '20210224:164058.242521:+0000',
                                                                            '20210224:164058.242526:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'йȠͻ҉W¡Σ3ȼȶѲ\x82 ѣʇʶtҌmϠζƾˠĕƾTшįřϑ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6711093131105441435,
                                                    },
                                    },
                            {
                                        'name': '3\x7f\x9cȈ¿ʘκϫâǡș',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4875359384087582602,
                                                                            8454693149025013678,
                                                                            -4243566130577722928,
                                                                            -526471866558086766,
                                                                            -8155084322355743319,
                                                                            -3300963815893455395,
                                                                            6318757638257178162,
                                                                            6255084865443369478,
                                                                            -1918132844780865375,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˇ;ĳmԠЬʖƙ4һИѡӌNúҏâԘӆʹƝǮϾ\x8a«ɦƁơǺѶ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԀɔΤ˒2)ǏԧƕȻЯĴӏҟȣͰ\u038dʐFтϊЄҴΔѵ΄Úɲģɽ',
                                                                            'ɶ\\\u038dƸѭzģī®ɏ¶ʩòEŭРêϞơƻǏŊ\x98!ʻϟҩӥʹǷ',
                                                                            'ȕGɩӋɣѣô˯Ѫәҿć~þԀѓҁͳ˝Ѽħ\x9bȝżBżǀӒƩǟ',
                                                                            'AëǕñȇēƠЎԃθưԀƘȔԈ_ſѡƮ\u0383ŅGѦӸǲãȃeȕҴ',
                                                                            'ʾʔÅǭǸҧ\x85ѹЄȵɽȡрӿɮːÛ\x95Ю\x9cԄѴϧZпϬǁǺǜe',
                                                                            'гʹˠ7ŶÏņ\x89γ\x9aƌӍВЬͻӥвϷŮgĞÁѾįϏťӺԀyѻ',
                                                                            'ΥȖѻөĩŵǄ¨ćµѱ©ʼǜҤƥԎ\x87Ρ©˂ˀǵʃԬÂѩҷҴơ',
                                                                            'ĐƴôťƱßӍʔƅΒҷƁȣ¸ЦcƿϾ£ģȏ˜Ԉ"1ӰλěDɸ',
                                                                            'ʽȀѲ˜ʻƹɸ˸ΧpʜӮĔЅĜ?љΏɮΠԣήЧҳƨȨσ;ʞ8',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϹƲñĻӷ¨ɓӼʦÈ;ĲŊ˨ϼЂȒԟƽ<âȉϼ\xad҆*ĠѦɗŹ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӥhɔƪʡÆ!JƏʖġǎƘȍɔ\x7fҀȀЦ\x93ƙӚϓԅғӝ͵ҬӚњ',
                                                    },
                                    },
                            {
                                        'name': 'Ѩӵ\xa0_Οҿ˒˺PɞÕӧԢȪʬũřȘǠӡɽÄЫӃƕȿѿǁ\u0382ҏ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3732524682062006707,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ԅɸàϓ',
                    'message': 'ԤXˮö˩Ӏ҃λҍĤȨʧȨƚȯĩȆǥïƔÀԫԜ§Jƈ҈XƲϩ',
                    'arguments': [
                            {
                                        'name': 'ˆ\u0381ϘϜņʸ\x94\u03a2μǴÙČǾĚ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʙʮ˘ǼƔɿ\xad·´ȷԔѬӮʌĜНXЭƻʍǈTɓҒѻǁʜҝʖʷ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164058.244362:+0000',
                                                    },
                                    },
                            {
                                        'name': '\u0378ʈ\x8b϶\x83ȗй϶yеѯЄwӏ·ѐП˽Ǔ˜ЫǱÇΔԅâǓ¢ԡҁ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2851908985999770436,
                                                    },
                                    },
                            {
                                        'name': 'ǤϮţΣ˅ΐϳȬІЅŖğҹůZ²љиȊʿӸŝĳґǖ\x9fҬ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӏ\x83EƣȐ\x98&ĄŀΪҧƅΪwсȞѼǇѴÝyɈʅ;ĚӺ\u0379ŔϠƠ',
                                                    },
                                    },
                            {
                                        'name': 'Äɬõ\x98ΊˑķºǧκѴĚͰʑҏԜE\x94ƨЉЅƮˢÝ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ďŝȡΩƼԎ½һʒȅϬНԕ'ͼrʘâͱЏӶȍÐțϝѐKʔǣA",
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'úǸҩ\x83ΕʒɎĚƣѸʖɯśϷǥАϑϓʿӑѧԆ*Ū%Éɦӟ\u0380ѥ',
                                                                            'WdӫͼźѮŞНщ4Ȣˤб²ĉʄʪƳ͵ƽβȜѢӚѷWȋӫŽɃ',
                                                                            'Õ˚ГҬǣ¦ˋԈ˵šǷйω\x87ʸāҒƺ#ҹƍӲŜЅї˓´ʛȾ˒',
                                                                            'Ε"ȦԃƑ÷ɷρʚԡǜȷȟϛЇʾӽӘĒРƀǉɯÞħ\x82ԟśҍ˸',
                                                                            'Ēʤ˹җμIɂ¹ȧõȲ=ɏԫǰ\x91Ā\x8fέðǋ}\x93ӁЁԆǆСɩ&',
                                                                            '§˻ːрөŻωʈоŐɸΤS_ŐĩҟľTEôļǽƅ#ӿô¡ΊѮ',
                                                                            'ƋƹʴũӮӍТyòćБҳНŖô\x82ƖȌċЩЪ˕ąɡХԀЇӎӔϓ',
                                                                            'ŧɠͷɍĳ΅©Ɵźӗт˟ȎƘƜΎԤüвɓǍƴЌňӡʶΟô{Ҟ',
                                                                            'ԡvԆʭлϓˑɐУϺƣԕ§ʅȴͶęԐӮѿеУRЍӧƧûΘÂЄ',
                                                                            'ƸaĦϓҞӞɍǉЎ˝ƔȍҗżƧҾȦǃēǾȧύɗkǕ˞ƃ`Ξλ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӊ?ØԆѣƢҼ˼*ζǿс¬ӘΞǆpϭҚԐҐ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
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
                                        'name': 'ǥȏșčўȇħĄӦĤǙЅϱɛȇĪӒįźıͻӋӨŴ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
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
                            {
                                        'name': 'Ԃ˖ԇʔűТtŜÈƪԀԎ2ęǄͷº',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '»ҏĄʠԭ\x8cKĐɚѾ4',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            650857.7204683246,
                                                                            594910.3781210035,
                                                                            96229.80877842612,
                                                                            55280.2218282033,
                                                                            702145.7718279691,
                                                                            249978.51664721163,
                                                                            424895.06133269914,
                                                                            859293.4144007928,
                                                                            225590.61523813137,
                                                                            109884.00622651249,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȬķÑӀþşœəοғ¡ӬĶƥÓ5ǆ˃řШʱӭKÙəѓ\x84ϭѯσ',
                    'message': "ÃƲČ\x8fϣϒӠ\\ѭҘƭπϮĂíʈȄ'ǪŸЁϓ˯yň\x95ɿϴƝŐ",
                    'arguments': [
                            {
                                        'name': 'Ʉɛӛ˥ϽЕӟͽɉ(ʫљřƛП´ηîɦӚʋϤǂȾϽɘ3þˠ҈',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǺˡњȣʗǨҡªí;ȏѬф½\u0379±ǺɸИMʛǻϝ˓џν·ҐȐʩ',
                                                    },
                                    },
                            {
                                        'name': 'џǃѨƦ{ԢǘªҧӔҀǋЮÒ¢ʍтàҌİƂӁıq\u0378ȖɮӹԈ˦',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ćŹıϤҊȰ\x8fĲ3\x89ÖԅԤC\u0378ʫ˨ʫбƱ΄ƞȴ˫ǈɓņΆҿϸ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5480162843981523403,
                                                    },
                                    },
                            {
                                        'name': 'oϐҏēuϩфԢ\u038dӁŘϯǬǾӼЗ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 349080.7899408193,
                                                    },
                                    },
                            {
                                        'name': 'ԊǽĩiίҽҸϓԏǞӹŹŁ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            369246.54644458817,
                                                                            -88471.83583620901,
                                                                            259047.3598527155,
                                                                            568746.7110475218,
                                                                            296095.5182410408,
                                                                            385723.4301272991,
                                                                            710962.8516871765,
                                                                            21211.792883017522,
                                                                            364049.05304388335,
                                                                            499624.3967766544,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЏdǨˢRϩƃԡûěуʡɄɟҨ\u03a2',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ҡ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ф϶ǋ¹şήŁȀӹƷѨҥËǄ\x86ѯȹŇɌRʦυ˺uΐȺеΰчƨ',
                                                    },
                                    },
                            {
                                        'name': '½',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6702819062315598360,
                                                                            -4576143245904291354,
                                                                            5980230432817612661,
                                                                            -64754960915931807,
                                                                            1026175702902870218,
                                                                            6604273905804698156,
                                                                            2202541966188929195,
                                                                            -5111499648674886415,
                                                                            -3353343689440098625,
                                                                            20447486888331247,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƫˇϬяҀĺäȑԀʌӳɽґÉжґǊDβ\u038bȇxĐƗ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': ' ôКԊΛѷыСƯ#ʮӂāԊɸˀѩбåϽɵҙмćϙӤϒϸŸƽ',
                                                    },
                                    },
                            {
                                        'name': 'ĶĸѷŹńSļʰ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -80579.48086151901,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƩήΤыØʨș˳ҀΌȯǬêǦ§Ӿ/˳ɰԁɂƅ\x92ѯʶд\u0383ƿѮǃ',
                    'message': 'έƎ9Ď\x8bƎѡhVмţȮȹōϲҽÝѱÂȫ¯ɡɶЧǗǕȬyą˔',
                    'arguments': [
                            {
                                        'name': 'ҷ«ʯǉŹӌƠɾӃɧѓɱÙʅЉɟȖ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'мǅĂFͷҼˢʅÈ\xa0ˢӖӠșҮ\xa0ʮÐПǂԈ˗\u038d˻˖ɁӢΎǍś',
                                                                            'Ҍ˹ͳ˜ʍυÚ˄ӫÁˁˤӶϿцԜєΓƺ҅ԉh˱ԡʼͳǛȂԦȠ',
                                                                            '˼ʺӖɋɡјǯƝѦȔŢɴĩʰҠњFĔơðͼƔʏœ}kоΦºԂ',
                                                                            'ɎǇҖӄĪ˝юЭzͻԜϗË)ěŨ˙жӻðǵƹӎȺӪȦŨѻъǎ',
                                                                            'ϱфË˞šȃʋ6ä˛ȑΖɿ҂ǲ5³ɈĮʹƏԠϳҀԋзʋȡԄɆ',
                                                                            '%ϼšƋϼϷϾсīɵʉӇҾψпԥҟϴhҙ2ɖȡԩƏɪϜѡϺϞ',
                                                                            '҅ƘѷӓĵȃɿȸȋӶǇҝf˾%ǣĹĪҝĢϨϰϒЧσ˷ӝѶӟɇ',
                                                                            '˵ƔȾőĝưƆ´҆ΆƂαǅϯϷѯˆ\x99˽Ə ƄȎӷҳӰэӊΪņ',
                                                                            'ˀҭť\u0380ҩāΎӪĕѡʞƠžǕʥƜÞ÷ӳȖЫУѧΙ¯§Uʜ˩ϝ',
                                                                            'љϥΑҵЅϿйǚФÙҥҘĆÈŬlϞ§ϋͱŝˎøʜɔŬԣыɋӰ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǝӳʃЀɋΚπDĻǝȻɖԈȹEϟ\x98ĥеιӃ^ЅиGȬɍ˱ȷź',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 479485.95273663907,
                                                    },
                                    },
                            {
                                        'name': 'ʎǱȉɢʃČǿƧǕƹŷάbʱӳɘ˽ш˳ёшВӷ\x82ǒϙMôÿ;',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            162600.98884021305,
                                                                            713678.7323816812,
                                                                            915322.2568700913,
                                                                            889601.9136906896,
                                                                            -39614.09858020524,
                                                                            435769.96896827105,
                                                                            712842.7747290889,
                                                                            321880.6643633871,
                                                                            -36499.03419843627,
                                                                            -25164.622762148778,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҎӯΩԡíȥǼӐǌЩƽ*ёʫ˜ƌßңғ£ˎ\x9bŶӦЀʷҰͳ˭ɽ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164058.249163:+0000',
                                                                            '20210224:164058.249178:+0000',
                                                                            '20210224:164058.249186:+0000',
                                                                            '20210224:164058.249192:+0000',
                                                                            '20210224:164058.249198:+0000',
                                                                            '20210224:164058.249204:+0000',
                                                                            '20210224:164058.249209:+0000',
                                                                            '20210224:164058.249215:+0000',
                                                                            '20210224:164058.249220:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǶĻǇЗǈ˥ưѢ',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĔϔƘʯčɞ\x8fźχϸˌʞŗ˭ϋВЁ\x91ǞПѢ˗ȼjΙɐˇĪȾʰ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164058.249659:+0000',
                                                                            '20210224:164058.249671:+0000',
                                                                            '20210224:164058.249678:+0000',
                                                                            '20210224:164058.249684:+0000',
                                                                            '20210224:164058.249690:+0000',
                                                                            '20210224:164058.249695:+0000',
                                                                            '20210224:164058.249700:+0000',
                                                                            '20210224:164058.249706:+0000',
                                                                            '20210224:164058.249711:+0000',
                                                                            '20210224:164058.249716:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ëʐ˷ҊǸҮŒȐФĚŹʴЩϱƶȍĪ˫ʊԀȬǇüȮĘøʩì\x99ԟ',
                    'message': 'ЂРFjԕǬäы\x8aˀɤЀįώƉˁżϮРʂ\x8fzǂś҅ԟÉԜȣȠ',
                    'arguments': [
                            {
                                        'name': 'οϡÞμŪˍ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164058.250164:+0000',
                                                                            '20210224:164058.250176:+0000',
                                                                            '20210224:164058.250183:+0000',
                                                                            '20210224:164058.250189:+0000',
                                                                            '20210224:164058.250194:+0000',
                                                                            '20210224:164058.250200:+0000',
                                                                            '20210224:164058.250205:+0000',
                                                                            '20210224:164058.250210:+0000',
                                                                            '20210224:164058.250216:+0000',
                                                                            '20210224:164058.250221:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŃҬʀԄΙЎņ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ѫȰGѿԭ³yɥɥɏϙ\x90ǞԇǰɴɕҰӘѭTЫʝ/ͼǩɁ˄Ѱχ',
                                                                            'ËʹǸÃ˪àƫĭцļ»ɵшċԮˬЃĠͲȲłʪǰВԊ-ԤʎŅa',
                                                                            '«βΧʚѿĹҠҭǡǙʱŵβяΣԝŖƭӤϋŒҿȜ҅8ʞ˺σ҉Ơ',
                                                                            '\u03a2ŪȰǱƅ˪Έʳȃ\x9cÝ\u0380ˢԩɄϭʏƸ½ӬҚğʄ˰ɫȹ΄\x7fђû',
                                                                            'ɂ˴ϿZǑѕϡ\x99ŊϠȈШңх«iΤ˜ƩǖŁɼ\\ΉͻӨèοсʍ',
                                                                            'ĕρÿ˓ü\x9f$dƂǇƑσʾȠēˊ/şҸíɒЕЯĻYÀ\x82ŚΓ˱',
                                                                            'ҫȸЄ3|щɊԓ3÷Зӣӣ˟ˬǲĝ˪˟ƺØŽѮσľìҿ¨Сx',
                                                                            'ͺĮǕˎȸfΒĠ.ћ»ƎӿŇиń\x8dѦӾͶƣͿȗԤǻїüϦeА',
                                                                            "ʿьŘŊŲӜƨ='ÎςϓЄƫƎʫúӋćǎʼЛФǭŅŒŉμΟѲ",
                                                                            'ĶԙɢǄȘˣͼΏΚҡŨʟҕ;˨ԁɈʋȴǂй\x8cŰͳɒƏȿŀΊΛ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϗŉˇ§˹ϜѵԍеǍϦԬNˮԝŠ҆ǤăĀȶmΩ\\пӯʬЪѡӓ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            730691.4746216933,
                                                                            78928.5139895317,
                                                                            454807.8306580703,
                                                                            30021.33116369041,
                                                                            51355.5121719451,
                                                                            519255.59678422613,
                                                                            344370.43046140607,
                                                                            521029.6827886194,
                                                                            515087.1793091177,
                                                                            620663.4492429767,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҖȷϲϷҴъԙőțȒŋ\x82ϠƴǾ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164058.251326:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ωûҕôi',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '1ƿЛƆ\u0379',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164058.251576:+0000',
                                                                            '20210224:164058.251588:+0000',
                                                                            '20210224:164058.251595:+0000',
                                                                            '20210224:164058.251601:+0000',
                                                                            '20210224:164058.251606:+0000',
                                                                            '20210224:164058.251612:+0000',
                                                                            '20210224:164058.251617:+0000',
                                                                            '20210224:164058.251622:+0000',
                                                                            '20210224:164058.251628:+0000',
                                                                            '20210224:164058.251633:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɡÇ\u0380҅',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164058.251835:+0000',
                                                    },
                                    },
                            {
                                        'name': '˪Dǁ$ѹ˶ĮÇӐȀôϏӭǦĻƟȨҀѷwϊ>ċǾƄԇʍѼˮē',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164058.251970:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʵƒƶĤ\\˰ósѿŀęДҕрǶŸ»ҧԖūЉȡÛ˶ҏǉжԊ²ρ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ĵŖɚҦŲϋǸЃѥ¢ƊSЩ«ϊȪ¦ҷѦ˻рЈʇŜΗΌãͱ¹Ҁ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164058.252226:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƔИƿҿ҇ĕʱǌώϓPԚ˔ˢ',
                    'message': 'χԐχђƌ^ǈŅĊŊǋþƚ\x80Ӷɚȿѫɕ\x9bƉl\x9bͲɡӥҵžƃЗ',
                    'arguments': [
                            {
                                        'name': 'ɁʙѹωǬÓɰːӉΧǭŕӬʊқŶ½;ŬĒƞț\x85ѭǧ»Нϻ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5912755415727047732,
                                                                            -6659957851792984901,
                                                                            5219096904428238014,
                                                                            -1055147619459872855,
                                                                            -1182005228183485516,
                                                                            -7423488837108674162,
                                                                            8580133854347384943,
                                                                            -2703237201087738121,
                                                                            1011673516912079376,
                                                                            -4317169123832662978,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'œԕȓZӣɧ҉єĎŎǪʏεɶ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164058.253772:+0000',
                                                                            '20210224:164058.253796:+0000',
                                                                            '20210224:164058.253803:+0000',
                                                                            '20210224:164058.253810:+0000',
                                                                            '20210224:164058.253815:+0000',
                                                                            '20210224:164058.253821:+0000',
                                                                            '20210224:164058.253827:+0000',
                                                                            '20210224:164058.253832:+0000',
                                                                            '20210224:164058.253837:+0000',
                                                                            '20210224:164058.253843:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'үԠӘǙϬҠʄǱΔ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŢӣVί',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5295195824840031374,
                                                    },
                                    },
                            {
                                        'name': 'ΓщƸҵƿĉаҷįһѸˊҾ¡Tȅ˫Јĥȉ\x86\x96ЂϠӥʚîκŧ¤',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 677222.9274988667,
                                                    },
                                    },
                            {
                                        'name': '¼ʾԟNϹԕпǍϝ\xadπ÷ŉ\x94Ԭ˫xЀ¶δқȩĖɯñ\u038bʞʱŗª',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '§YȩЃѭ#ĳ¿ì\xadǼȞίҤ˧µϦːӅÓЮŌʮǕρԮЎʂɒӜ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ґDʕΞƬȊӫӵѓϰӳѻхǷmƒǥʖùϚӿυӀʐȰЅǪԀщˊ',
                                                    },
                                    },
                            {
                                        'name': 'Ƙ\u0380ʙȒΣӻϗҁƦϿ,ƸȣӔ\x7fǩ˝Ҿ\x83ԥ¢їϩԜӡʰ\x8eķɑʂ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '`ʝ˘ΝŃ˙\x91ȃǈ˛\u0379˘Ѩ)τĆƖTŵЛˍ\x85ƾФcƜ˻ɱšϼ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ѻ¥ǅ˧ԓɈʒˀӓͷʚϠĊÏĹœa÷ԛɆŎЩЙσɌĐτҜҶԊ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8052518366558217013,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѯåӟӵЇːҍѾѿ҇Гʬђōҳ˟ʎ\u0382ȹʣʪ\x99ϠˆŷЖ+ҽ2¤',
                    'message': 'ƻɅΚ¹1JЃяϊӰˇɰԜ¨ҙѽʭѧϞ\u0379Ǝ\x96ɽьǖŌ{ρɃԋ',
                    'arguments': [
                            {
                                        'name': 'ƌʬƽӮǚɏȝѸӓӒӧǬϽɧʧý\u0382:ɻӸâԑOƵŦ˒МːFŮ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3824058158922612472,
                                                    },
                                    },
                            {
                                        'name': 'ОǘƺĽдʒǟʬЏʏҩŻōѵƀӇɎʊҒѫҠʮɣйÚɬŠ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            621898.6550030838,
                                                                            192082.7178814349,
                                                                            -77264.98210835119,
                                                                            428418.7392540177,
                                                                            18575.13721587404,
                                                                            682673.9201972896,
                                                                            546890.7575916849,
                                                                            206290.02888241952,
                                                                            325423.9690216876,
                                                                            410163.7303332861,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӧ«ɈƠʶǼҧΛřˋҘȞѳȴ\u0378ɇɲ΅ПёцӓǐͺɄŅʤķɉȢ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164058.255727:+0000',
                                                                            '20210224:164058.255740:+0000',
                                                                            '20210224:164058.255748:+0000',
                                                                            '20210224:164058.255754:+0000',
                                                                            '20210224:164058.255759:+0000',
                                                                            '20210224:164058.255765:+0000',
                                                                            '20210224:164058.255770:+0000',
                                                                            '20210224:164058.255776:+0000',
                                                                            '20210224:164058.255781:+0000',
                                                                            '20210224:164058.255786:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԟ˗οěψыũĖϦ˴Ԉӧ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164058.255995:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÎҶɕƹ\xadԀɉԜɀΎϫc҃ǯɳ¯ƺӐ΄ÙƤŀϗɬŰʨԬǐ҆ă',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 308561.80863429676,
                                                    },
                                    },
                            {
                                        'name': 'W¿Ԟ\u0383ԙʅЂƊÄҲŎƕ\x9aĸĈŊʡǋϵӊăśӮHʱяӆkφų',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            23490.15015439228,
                                                                            805107.0085364202,
                                                                            768821.3727945883,
                                                                            564103.8820734665,
                                                                            846563.307776235,
                                                                            895616.7744640447,
                                                                            422074.7594942296,
                                                                            434943.5738601476,
                                                                            575948.7339893022,
                                                                            742894.8675086267,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɒɇҿƦų?КɼѦŐ§Ǖ>č?śӧʚп˗ÿÏϾӣɀ\u038dĒɵȴҔ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ѿή¥®ȢƺųɋԄYԝ/ɛоƶф͵ɤ˶ǚʂѧɘӜĜӤĩϹĦˏ',
                                                    },
                                    },
                            {
                                        'name': 'ɯӃĹƄΖȳ@ΖϹΘCŶӷҠы',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 43267.095730097644,
                                                    },
                                    },
                            {
                                        'name': 'ʴćŅёϷе\x8bҪȒϲˑΟ҅ԇǞĦ˾ПƿǑΚәʶƞсџƨӉŦΩ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164058.256747:+0000',
                                                                            '20210224:164058.256759:+0000',
                                                                            '20210224:164058.256766:+0000',
                                                                            '20210224:164058.256772:+0000',
                                                                            '20210224:164058.256778:+0000',
                                                                            '20210224:164058.256783:+0000',
                                                                            '20210224:164058.256789:+0000',
                                                                            '20210224:164058.256794:+0000',
                                                                            '20210224:164058.256799:+0000',
                                                                            '20210224:164058.256805:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'śѨΌĞΌÇǐ@ƴˏδэ]jӻ˘тɡǸΦő÷њPǟӓѣ\x95ҳР',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 787633.426495865,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ı\x9fȶ\x97ϒҲɫȉҧͽŧ;ȱӨŶϨύЉԤ¶ŸӚƈ',
                    'message': 'ȿͰȣĢ\x8cƌ˲Ŷ˙ǮȢ\x97ÿŘƴ.\x81ɌȚђҘŲԙƭʜǋVѰċǗ',
                    'arguments': [
                            {
                                        'name': 'ȝ҆˹ϤȞǺн©Ñʗϱ¿ԊʨƚЕĦќџεǤԙкΰДȊŹV½Х',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 659672.7846003169,
                                                    },
                                    },
                            {
                                        'name': '\x8dҟЖʈĚқŢ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -62354.987526109166,
                                                                            769061.761384745,
                                                                            -19372.45933667387,
                                                                            -10661.431721667643,
                                                                            319746.2677211661,
                                                                            707695.5869707718,
                                                                            354696.90453126293,
                                                                            893547.8946788879,
                                                                            809859.5525564858,
                                                                            99366.38608923162,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˋίϼɓБ\x9aûőĮΦύҽĩ˭ǨË\x8b¸ƎǞԃƓԙο',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ќ6Ŝž<ư\x94ȶ˫˝ƦG\u038bŉʼҬҴНʁȵɶǮæɑӰŅÿм£ˏ',
                                                    },
                                    },
                            {
                                        'name': '¤ԓԁѬƄɖϠoҵԬʘԊ˄ʁқȠ1',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164058.257893:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ΐǪƢˑǑʨȂɭӭ҈ƞњżϧĮҴЊïĜ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʦßɣҞƗӃԂŧAɡŊͿŦĸԩөʬҒȠ>ұNǲԤǖĽlәԘ҃',
                                                                            'ƭĿʱξҤŁʴþïĊ˶ǅÙ˧ҝҫ\\¾Ƒ˪řƏŶқƊmϺа9ǿ',
                                                                            'ΨŭйŽϞϦ˨ťóњý˯ȧυŜɈ_ÒƲǚԟʖ˩˺ƒƽšюĐϽ',
                                                                            'ɘɫśÓӰW\x9fԇƁӥǼϭѝDΦ§Ԁ&НлеѤх´Ŧ˄ͻĒɽƏ',
                                                                            'ςŗxҽ˷ʈУŁ\x80ϋȠҒԗ&H6ǆɍN˾ǜȮ˓Ʃ¼ʔǂӣʪҦ',
                                                                            'ЧѱɏϛͶɯȞɌϬȊ´}Ϋļ҃ϣŷſŎоʝѩҳɥӪӴΗѰǗƳ',
                                                                            'ΔТȗ˫ǓŽϘͱˋƂԩâǃĲ"ɐέғύҟСͲ|ўѡЋӷԄѡŻ',
                                                                            'ƜĿϯqŃǪɶˣɋȋɶЪȪɮǍǠʀȉϐyό\x87ӃeĞɜ Ē˕`',
                                                                            'ǫ~KѺϔβ&ǚƙыĄĥmτǹ˞ɬд´ɮŤİҧɀѰåуřȴ˸',
                                                                            'ӞŋϫΟPĚ˔ΫϣĸƮԒæѦŒўǥǮԏЏųΓɔNϢ˞˂Ҳġ˻',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƒԣτˏyƝˀѿ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -59374.46306634335,
                                                                            305451.995939283,
                                                                            288766.92719976074,
                                                                            47196.53902873624,
                                                                            752126.0262026174,
                                                                            910631.5944579958,
                                                                            734631.3446115457,
                                                                            408021.0538981026,
                                                                            139211.06567904906,
                                                                            499121.9544970705,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Į\x97*ʊӨш\x82\x86ӢҼλѼǭþʸǀşĻѷČüƖªƃ\x80ˀӐӺұԌ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164058.258735:+0000',
                                                                            '20210224:164058.258750:+0000',
                                                                            '20210224:164058.258758:+0000',
                                                                            '20210224:164058.258765:+0000',
                                                                            '20210224:164058.258772:+0000',
                                                                            '20210224:164058.258778:+0000',
                                                                            '20210224:164058.258784:+0000',
                                                                            '20210224:164058.258790:+0000',
                                                                            '20210224:164058.258796:+0000',
                                                                            '20210224:164058.258802:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'aË9ʕȾ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ёлϢtóҪζҺЕtԢӃɻȆˣӈɟҸʒ˄ˁĺτқɁЧԃÊ¸\x8e',
                                                                            '˯ԁ0ëϱϣҧǞνBšΉǙvϛŷįɢʤĪȸӼџÝʺʹҴѭШԄ',
                                                                            'sΆΨӺƻÙªIdȜˡ\x9fҹˡƕņϭτ®óԫϓŵ©ċʍӐӣØʇ',
                                                                            'ѕƺ*ʷϰʐϊĠȢǿӋѠćŐ˅«ƉÊҪП˓ȕж\x92әҩѧԖЈѼ',
                                                                            'λǱ˲Ɍĸ±ӴΆƶПɃҪŰˤKьɚΏуӤηǙʧˑÁÖΓˈˋǜ',
                                                                            'Ń\x96ϙӿҏ\x8b;ɨϡǿʫĮүШƫΧРŽþҘԂȗȮƹӕșƪȼήÄ',
                                                                            'ϷV:ѪҜɤӦоħҚϮԮ¸ƀϑŶiʃùԋΙуōGɠЄͷвƣȮ',
                                                                            'ʢ˄ψ˷ЛϚȓҫɈͽϻ˜ΰϺĜѪþńƽΞźǽͳбԛˎӺɩǰӖ',
                                                                            'Ȕīȁ˱zǂȘζѬ¢ԗҨȧʘYOɰC{ҼƟϪ\x8eŚ\x83ɴԫоơ˫',
                                                                            'ŎʀăĞʣÆ½ǁʿҿÆʚƦ;Π|ί˻XлåԚˢɁАӅƛŖΎ\x9d',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ͼ;ӟČͶϤȅɗȋƍԑϓѠȇˑɔŗѣѾ(QƓ¬ʝ҉˃ɈӤΣŷ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -19557.50977078406,
                                                                            946656.3552726603,
                                                                            3696.845723445498,
                                                                            478833.3224748381,
                                                                            676898.7715741737,
                                                                            939103.9943164757,
                                                                            542424.1208647785,
                                                                            838978.99031461,
                                                                            272491.8865516436,
                                                                            -32683.499039486356,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǯȒǘśėÞЖȳԞ«ĔфүϢФșӊ\xadƿƘҰŰÛú¯ӞΣ&\x9dǃ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 259205.21798979404,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƊˠАќŔz˘Ǥɑʸǒɜ˚ӁɑϾϱӌ\x95Ű҅Ӫ',
                    'message': "őĦ'ƅ|ʗȸя\x8aĠůͶĻӿӶðмĮƄΤ˛ɳӆ5αϋӝҔѼɆ",
                    'arguments': [
                            {
                                        'name': '\x9eЂńYsӧҸƿÛŊүˮͽUàˎϽ@˖ƐΜΪȳͰАŀΙѝћď',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': ')ʑŋǜɱдѳԖ\x91ʛ¦όѼɃK˘Įӆҙưй)Ї˃ˮĳ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
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
                                        'name': 'ҋϘԝ\x93ӡJǬĩΖϡљ˞ǯǬżĜњŦŐá˫Ǹ˹Ĥыʲʜ3ҝɏ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2808602885302785447,
                                                    },
                                    },
                            {
                                        'name': '˝ŇӎΦțϹΞʵƤī¹ŕҹԊÚþ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӃѶЉйϡŔȮ˩ɜŮwΒ\x8fӉ΄·˴˖ԀĿӍl3ҳζƘҝԩˣӡ',
                                                                            'ӗϬüăήģӺʰɌȠ\x84ΔΔpӡЗѦҏɢͺж«ДjӝƃКƔϗŬ',
                                                                            'ԜҡӒ¤Ύɡǖ¬Ŵх÷ȺȃҏҔǘдѦˆоłƣɠ\x93ӹԆЖ˝ЅϺ',
                                                                            '˵ԛϿǁďŨǩ˺ȡїǅÕɋÏÚgΚɝȶѷԃĝίʊľςӶͼȑ˼',
                                                                            '1ĕʬſ¸ǣʪYɅԉ\x8aWͱ¬ʌӴǩϵƮƈĂª·єǝѽɃ҂5»',
                                                                            'ҋȅξʥӈЭЗԭϦ»4˦ʏˍȴǄqҾ´ȚÖ9ӦĚǮŸɁIӇı',
                                                                            '\u0381ӝ˩ѺУ*ϓŏ˭ӆ˭Ш\x9aӰʻĹƨ@ƸƼeԈŌœҊԈȓȮɓʚ',
                                                                            'đЍјԓЗȰhҳɗұ?-Εɩ«ȦΖцӑϟψɚӂŀҸӫΛΝҟѐ',
                                                                            'ӌҲƼƺϝ˦ȵѭŀӌү¤ǜЄţҏ҈oϾԜȋɉƘŒΌȇЃʗӠӷ',
                                                                            "Ө+ϢцүćΦ'ѼáҁϻȥӸɻȈ˧ξӏğʴÉŴѥ\x85ӸαҤτό",
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƔƦføԓӅЈʗяǕӁϴɞӅˈʒѽҷɜӦĉԝıȏɝ\x99Ǌ\x8fˉύ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7032585736076414982,
                                                    },
                                    },
                            {
                                        'name': 'ҩÚȹzʾϦӘģ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164058.261227:+0000',
                                                                            '20210224:164058.261242:+0000',
                                                                            '20210224:164058.261250:+0000',
                                                                            '20210224:164058.261256:+0000',
                                                                            '20210224:164058.261261:+0000',
                                                                            '20210224:164058.261267:+0000',
                                                                            '20210224:164058.261272:+0000',
                                                                            '20210224:164058.261277:+0000',
                                                                            '20210224:164058.261283:+0000',
                                                                            '20210224:164058.261288:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ұ˾ɗˋ\x9aŗʌĨӍǜ\\˺Ν˫ĻШюСEħБЃԃ˸˨Ɓ϶ԜôƠ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            253196.30406545498,
                                                                            662495.7832722848,
                                                                            284642.7257699467,
                                                                            15803.423174435113,
                                                                            523178.09099181544,
                                                                            -39495.96520914114,
                                                                            466984.68165923946,
                                                                            73155.25042408981,
                                                                            41880.66120547871,
                                                                            735173.5130812334,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӋǚԈƋҘ×lӍȠǄɔϗή˙ơˮ2ΌԐѣŽMǬԦ϶Ҳɨ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164058.261743:+0000',
                                                                            '20210224:164058.261755:+0000',
                                                                            '20210224:164058.261762:+0000',
                                                                            '20210224:164058.261768:+0000',
                                                                            '20210224:164058.261774:+0000',
                                                                            '20210224:164058.261779:+0000',
                                                                            '20210224:164058.261784:+0000',
                                                                            '20210224:164058.261790:+0000',
                                                                            '20210224:164058.261795:+0000',
                                                                            '20210224:164058.261800:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǳΆˡƬǤæʞĥĤӾɊ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210224:164058.262009:+0000',
                                                                            '20210224:164058.262020:+0000',
                                                                            '20210224:164058.262027:+0000',
                                                                            '20210224:164058.262033:+0000',
                                                                            '20210224:164058.262039:+0000',
                                                                            '20210224:164058.262044:+0000',
                                                                            '20210224:164058.262049:+0000',
                                                                            '20210224:164058.262055:+0000',
                                                                            '20210224:164058.262060:+0000',
                                                                            '20210224:164058.262065:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Hɮ\x84ˬnɶԀßҦԋɮĠŚɵҔҰҡҚâʵĆЉtΒԩëсʭĪȫ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210224:164058.262281:+0000',
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

            'identifier': 'ŰӪǻȿŒ',

            'categories': [
                'invalid-user-action',
            ],

            'messages': [
                {
                    'catalog': 'ΘɅ',
                    'message': 'Ţ',
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
            'name': 'Σzɘҝ¼ԎΑҰɈĻКVҴ\x98äδžуȓ-ǲǪҨΎɝ\xadϬĵάǏ',
            'error': {
                'identifier': 'ʻɎнѶƕɠb®ϴжӔƧlūȐȄԉΫԅ[ǔĀѩĕ¤Ǩ˱ԬѠf',
                'categories': [
                    'access-restriction',
                    'invalid-user-action',
                    'internal',
                    'configuration',
                    'os',
                    'access-restriction',
                    'file',
                    'os',
                    'configuration',
                    'access-restriction',
                ],
                'source': 'ҧȔԦƺQȭɒQƖϊЙ³ŅХѯɯϫ˃˪ŋmƞtҏ˙хxѼԆ}',
                'messages': [
                    {
                            'catalog': 'ōƧŋɉγϚ¡νĶʾ˸Ãȓ˄Ͻ2ƾ\x97дǳҏÿǞPdȆ¯ʮͲҎ',
                            'message': 'οêËҩśґǷњǟʞҮҨʂǮʏȘûņцǻʺμäúķӣӠōBƎ',
                            'arguments': [
                                        {
                                                        'name': '¨HŵԢЧԁ҆ʻŻϐĜȿҫǺŇŝдǖɖ\x8bÊ¿ǕɍǇԜƝĕʸɃ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x92ϘҠÑȪΧjźÐˮȂǳδгɲԐӆƛzѻВɪσϰǢɕʑѮƦà',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4243213253136402780,
                                                                        },
                                                    },
                                        {
                                                        'name': 'BѾΩɩԇº&ȫНþɵʵĪжɯuƭʘԏϚӍÇ\x85ҟѳΛԤԒʯȩ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164058.217733:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҵ˴|Ҝȱӈ\\ǈʀɄŲʤԦǤϮȵÔɋ:δǝȆ˕',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŗƘӸϳҫӟӜνҚƱӾıĆ£ùĠөƥǤȾ8ҦѰɴ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϺɆьХˆ"χƳ˴Ϧʕ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': "ЯƧƬʶƿɎɽCđŜǂѷ'óĉ˂Ǌ",
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 327580.2390991822,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɪԞƼʈ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ğ\x8eíʑϿƏŉÕʓлҡʧюьаЀњλΟԣԏģєϢ˲ϡΠϹӑύ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¼ϊӼǔǸDʼŻ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'įĢ6>ˣ˃ӡϴҖϰԘȽȰʹӹƝɚļʙDϡǋԖԇʪĤπjȜĪ',
                            'message': 'ȽаӍˣҡҕbȄřŲcǇҠрưӻǉŭʛ\x90αθõʋƘƁԛĐЌʕ',
                            'arguments': [
                                        {
                                                        'name': 'WΜʘ҃ȉΊʂ³ʌϣҟǰϻʉçȏɕɕ\u0383ňªʞòӪӨ\u0382ǃf˟Ȩ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϯrƕ-ϼҍźζѨǾщğHŻ2сźȞӌӎ%ɺÖɃЍ¬ŢƲщԈ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4960873367820880781,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Αҗї\x9fŁъˈAҦʬĶJňĳЃ¶ҵϬǔͰԞӵЪѮźʿ\x8dΫƀǔ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˞ΗŽʄЫřǲ уˆ§ВШʾFғƨʡЫsҊғʨǞϝӈǻōҢķ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x90ƎЙ\x82ӂτʮΎ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʱɱƙ΄Ɏ\x98Π,ѭҼҹ˧Ä3ӎƠǆ¦Ç(χǈî˄ɜ҆Ϻåɓ:',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŠЌñ϶ĞЋӭӄҫКЕ\x88ȎλӁ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "īҋĹÕǜѵ˞ͱ'rĜЁВǡɠѬФ®ÕMӖÒȱűƯċʎˏ˚ȟ",
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4603136529356042768,
                                                                        },
                                                    },
                                        {
                                                        'name': '¤ťԗҴδbҙѨ\u0382ˋЁ\x8dҖųӀȔϙɕҁeцҦэ\x9fԓƌ§\u038bο˽',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 191961.19082178292,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŵφϞҘʸǟɃ$ûĝςɤƥ϶\x92ų¾ƁƹȮӬʮƁ\u0383ҏíͲŇӯ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 536416.5760391355,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѡŭːȇ2ΦԇQπÀƷϲˈ˺˽Ϝƿ\u0382ԔĂǝҝήΈZèɍ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ˁSėԓϻςųДԁȸǐ\x83ʣ\u0379ǬɳÃͽЧϳȏă,ѶŇĒϫϴӍη',
                            'message': '\xadǀ¿Cӽ£ҙӻɿӫʽǩΗōϢȅƧԌŨ˘ʒcĿÅҀ¶~Ǽςɉ',
                            'arguments': [
                                        {
                                                        'name': 'ϊȬʗΙQƫį»\u0380Ğϫӷùџ9˰ςK§ǆġϖѿƾˆ\u0380ȇɎҨϙ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ďĨˉǥɭψϐɬź\x8aӴӍϫșªǯɫѢĲӽΆż˃¤νԆƆʼȩΖ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ąˍ¤ÇƊŦƛԄºӣǻϦ7gÅҘŪŊҸ΅˭*ԁę˪˩ʜϲǺĉ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¼ɐĬҾ҈ҿÇϨеΠȤNɴʶɌOǽ+$ťҡǝԣȣӄ_ŤʙуΕ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĪƠġԜɭӁǪ˶',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˧Ȅģ=ÈӎлÎĳĥ˩цԟҧүω҆ÆˋѕƀÍӰˢʤǢӂҤР\x87',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'хώҐʡə˖ΰԅ\u0381έԣϚҳ˱ωӳӵҨ΅lĽˊĪ˥ɈŖϨȠίó',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȳŀz\x88ǼÍĆȥР)ŽYԧԮʝcđ0҄Ҏ`ǯԓԘşāʾɚҠÏ',
                                                                        },
                                                    },
                                        {
                                                        'name': '˂ǪЍʈҍňÿԭ¢ŲЩȠ\x98µ5ʋ3˴ǧƂz"ͷѯ\x9eøGigϤ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 924943.0522461454,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŇЍѢzНǈǷҜŦșɈƧΦ˂PɛqȜФЧƽƻβȥņ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '×žŞÒʽžӕŇƧƊΠȓΆЧ˚čũΌʫѷѺ\x91ЇǌЋƄԌĦѦҏ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ж\u0378\x96Ȑ*ȁƐ˳ɹUÔɎǷѩѦėȨԩм/ê҈',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӤїӓџΘ˵\x93ѾθѪȪŁ\x88ŲĸƶͿъǓˣҠ_ɍĴ¹ŨŅ˼È\u03a2',
                            'message': 'ʽƓƫåϛ¢õҕΔдʧƭ?ūIɗτU\x83ϧζюн\x81ŰЗ¿¨ҠӀ',
                            'arguments': [
                                        {
                                                        'name': 'ŏӒ˸ԤǡѶԄǱƫɌΓӼ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ġ˱˔ǭѮΩ҉ӫLɝøĻҎԔǢƾƶõεΛОƉɁȿ˥З',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɿNσƋΖɸ\u038dǠӌнҕrğè\x90ɪϾïȅȢʯˁϽ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164058.223849:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'əʜźԫÚγ|ĐǂɚğȬæΨuÏːŘƟͱɡҧъЌ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΎѾ\x87ϛ#ĤɘΘ3ӊϸӆˢŪ˸ĪɨɃͱΞкƸÁѱʹŦlǅȞԠ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ȇŉ'Ĭƙ\x96ȝ˸ҍсÆсѧҀ\u0378ήΒџɓӱƲҬ˒ҭ\x8e",
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164058.224331:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x81ȟ¥UȱӟźӼ\x94ҁӹѰĩ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164058.224466:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǻʋϰÚϷİɥƩ§ȃӵϦĎŉԤ˩ĐĳΝ҅Ϋ\x89ΥƠįÄ˱Ɖϱ˕',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'sÏȬ4ʷřχÙ˯¸ЄпύύЏǁ\x91ðԀȾǩv{ŲƧɾпÇĔɘ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȥĠăтͰȞ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˟ɠʇΡɖϏȪ\x97¹ȅӚƭʆ\x8eʌө˨Ϊԉҭȧ\\ϽŵĻӬ>˟ŜϨ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϒȷŦƁǼ}\x89ɥΞ\x81ΒȨɰɊ$Ԑ»µ҇6ɓhнɧŉчҪИѽȌ',
                            'message': 'ǐЛʨǫȾӺ˛ˮĤфӠ˴ˆȥΪȻɭϟʟɏȸɯЭȹϊ\x969ƶΠZ',
                            'arguments': [
                                    ],
                        },
                    {
                            'catalog': 'αəƇԏǢυļȾЋâҭǏĽΨɛģδεŹϐɇάƩØȈҵ·ԌcӚ',
                            'message': 'ϓϙЧȏԟ¼şÉ.\x9eϒčĘ¯Ӿƚԏ6Ľ͵Ȝԅďώŉќ\x90Ⱦϼˑ',
                            'arguments': [
                                        {
                                                        'name': 'Ɨϸʽ\x7f ʨŚϓʖЛϋ¸ȝӱͳҶҸəϕ\x9fϟɒâԫӉřSȆ)',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4810316963590776829,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ëǫβҏòәΆϋσʻǱʎ ɗăͲ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ÆҏƣΨ\x9fԠκԣ÷ǖǲ\x85ƥġҧʗƾƱőҗņ°ʄэʌŒғѯʦӀ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϩɝǥɵ\x93ҪƠπөɡưȘюҝҋĉÍ˹Ϲ˝ƻˣ§ҶüԡοӼʢɫ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164058.225786:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϮɒҽˣʌšҜƺάҚöLKӤɳѶȸ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԢČȋÙѬÂ?ПƾӻĚѡϱԛRµъĻɀё ɕϨЃɣƍʺFʹԕ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƎɱƒÑȐеįǇȢʋ\x92яȎв2Ġ¶ӑʀkΩ˶ɈΟȥ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6333348355863882838,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɂƈȔӈʕӶӿǺˍǦŚɘϵԈѡҍц',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ůςƍЬΘ=˦ŬүˉӍӁЭВȄƵϸҩ˖ѝ²αˁEшȶҁª-Š',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɞ\u0383ӫΏȡνȿϴHſѦȆӔĎʬɣȡΜmҨɉʶʻχͱԞȘ®ʘϞ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӻ\x89ЉΖмˑɫίϦJƆϟ\u0378Q®čɑl%˔',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 907202.3603207726,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƝǡKˎěơ[ӄ,ΌȍǾ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x99˒ЗùșƏȃѵegŹͻ\u038bԬӾӲяŅƳƓӰĵ+kԔńEɵҘȞ',
                            'message': 'ȐӨľ˼ɫɛÒӜӂщ˛ϟȗԮиǝe`ǜS˫ǃÀˀŐϿǩŎģā',
                            'arguments': [
                                        {
                                                        'name': '\x93\x9dŉü¢ˢƫƯʷʋÈХƌeAƄʆҴɠ:˭ΐƧλ\x8aχɲ˽И\x81',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȯлԢʊ·ŤѶŻʟӛѴʝŷRөԂȾӋɯҞӻΊН$Ɉµ˯хĝ\u0380',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǫЫi[˦ö7ӽĕІŨЋЖɺǡМ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʥʘ˖οʤ~ĖҬŕ˪â˾ϯԬÎсǋÅǦΒ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ľȭ҆ɑþ˛ΜƬéĢӐΘĶYǅͶĭșÇɄǚĩΌΐbMөįˀh',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԣǗԦȦ\x9dΖWҴĳĖǅԚМȾȇß',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʎïȞӍһǖƏȆ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8996191262815053177,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŗŀňťҲɚҊ\x8aɽʤĖԮ\x92ĢԇэҲ˼ʨŏԅĂi˽ɋƄΎǮƌɸ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɋРµĖӝҎѿұÖԙàϗþƀԩǪўŧ¯ˢ˛ʩҰф',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': "Ӓʏ·1ǂʛǿͺ˗тїgҫҫʕǔʇ\x92'оϣʜюƄȬ+ɀŇӀ˜",
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϮΨǦȴɎӑлȼмΆ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϜΒɨɿoȁΪʙ˝Ъѱ˭Ŭ˴ɞδŭŝ¯ͿƇƟ҉\x96ƺҰʡԭҝĘ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǎɓȽҨeΕ ÄɒSј',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 526722.9819048431,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԡ]˷Ԉůȁѐѡчğȁ҆ɈɑʴȄȲҨʋ˪ȧлҁƭҘѼ\u0382Țԭ¬',
                            'message': 'ƘZkˣŒѨДȍϫϠȍэ¡ůԚʅӐ ƶǀϋǭơȩɔăƀ&ȇβ',
                            'arguments': [
                                        {
                                                        'name': 'ŮεʔΛɚɐҚˊÏ8\x8dƁĀvуǼԪbȢǐԘʛ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ιӉхΔ\u0382œϼǽВlόԅåňҫȓUĊɊ!҂¤ƊúβĖŹȉƁԉ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'aUĄĭϨʡĝΒƨ^ΫîàDþϜǱϾʶΒа¶˳ξТ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 994119.3625331146,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҨХɄėЊ\x92œ҇ī\x8aȃȔʌʵҾǁĶƫЎĩϔǐѠԞ˶ĹƇ\x9d',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4357095480218519058,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѮǣŖËʬӨ˞СŽÎʸí¦\x9cϼǥћЂɣȎìƛԎɊјѣЄąϾ$',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'țRȄùʅƭӖʁŇǁÑǩӓϣԝɽǔ½ӸǯʳƎ¿£¼Ʊ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3549418871229238795,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9fĈˇ\x99і[÷ƼțǩΌѱԊǡ\x7fŬʣƼǝΖѭVВȆ\x90',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x98ьǗ©ŌЌԉŢǷÈΑһö¡ãŧ\x90п5ɅĹ\x87\x8dҌɲǲ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŤƘ˳ӦγѐĦЗrĠѦҎ\x8bɈaδhØ˱\x9bѩǡӣӪ\x9dʎĭϞβԥ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164058.230262:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '.СĔѴѳκԦƔʜԨѹ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǺϲΦȕʠώǏʬŇϱϐѠËɘǂLΓɪ5ЕȗЇŏ^Ū',
                            'message': 'ƶЯɥҺêİт˞ԥǕ<άʝƢŷÃӏǠΓ\x8b\u0379ʥҺԌŮǄҷƃ\u0383Ã',
                            'arguments': [
                                        {
                                                        'name': "ԢȓƽǻŗuˎVӅφλċǥôѵ]\x84ƻɩżʟŀƂ'ǕĥʺСΐʎ",
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 151897.42179114663,
                                                                        },
                                                    },
                                        {
                                                        'name': 'tNѭMĠɌĻїˢ?\x9eʓԇЅӡƗdĂ\u0380ҀҔ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164058.230962:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƿĆ*φʱЧƣʆǪљϓʒ+вԓ˞ø±ƭΖϘ~џĵàӷǸʏөƑ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˒ɤӉЧìãДВ\xa0ѨɲˡRшɾԉȈXԑăЅςɸʟѦ\x81Īɯê&',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ʀϕ/ǵҚђËƔԟȷпԈʏɉ¿ˑˊńʏ\u0380˅ynϛƂњ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҰηҋЉŀǹŔ# ƦǚҚԦqŲƽσю\x9dƵјԨѸП\u0383ƘΐłѠĽ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϕX҆ҀbțΰЋǴˤʮGёͺɲǿ¥¡\x83',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЏũʋŊЛƉȂѯȂеɞɣ˦ђϸƢĺнΖ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƤЀÚΝǃÎϠтͽʫ˶ŽϚ\x8c¤Č-ӚђϕҪЌԇϑÁȑđʻ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӸĕßǺӫ΅Ǿæwέ˾+Ɇ×;żΩˮĞ\x9dƪƕȿǹȇ9ʅ˥Ԯʉ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȝƣ|ɀȕǜϤ҆pӁǜʨȀëҮŘюÉөǼʙƄuǁѩwƩїςċ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѹʡȗȬŧˮβèǳȻħϵӎ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164058.232332:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ъ_ɱԦ×8ȁĎҡ\x9că¬ӭĈџӡУȣċǴϮȻȭÒҴȣҔшĀɓ',
                            'message': 'Ԭ5ȐĴԡʷӒԣҠǙˢ³4êѡİԂљԥΪҗѓѥϖӇ4˽ēĊ«',
                            'arguments': [
                                        {
                                                        'name': 'Ńōϒ\u0380ɍӞ\x9dʤáňϛ\x98ıâØ§ʘhʞƤΘ˭ZkщϯҢʵԏϫ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͱȪіɰϵ*ğϙӇҍɢʍƇʅɤʹђұԙʞϿΊϱЃϿɗӍԎƅϒ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7261536970781134050,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ķɤȘɪӻԕƁӜӜȆҚR<ëʰê4ԬԔʀМȶÍҹƘŗÖʛ˳ȸ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210224:164058.233100:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѠЙșəêҴ˔tʓƋЪν\x8fԍͲΌѾñŖHΈŐʴơүĞКԍшĒ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƯεȄpҒ˛¿ɓΧƇϼƄǮȖ`ʛŅi¿ ьȵϳӢͲXЂǑΙâ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҸR¾ϟƆŒˊҏɪ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȩԍɫTƫɶӇǷǲύξĿ˶ǿƲ˽ɏȋťƘːϻėȿѓʾíΉ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¬ҙʩӱŏɓΩӿ\u038b»ʶȄkĉѣŉЋəθ҄ԐŝĞҨ\x90>ʽ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ϲľùóǧʉ˦ѻѐґşŇŸԫʤ˙ƪԏҺ͵аѣɱéӣʬҒӅŊǑ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŤҖÃ®Ίƣ\u0380˞ÙйԦȋ˟Ϟøі\x91ȆκԒ2ŇȇЗǠĄįǟʇɍ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɟɚ˭Жѓɯ˚˲ËԧI',
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

            'name': 'ωҹЌ',

            'error': {
                'identifier': 'љċWѥȆ',
                'categories': [
                    'file',
                ],
                'messages': [
                    {
                            'catalog': 'ƶȻ',
                            'message': 'Ě',
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
            'event_id': '\u038dƱǈCһϟѾЛӌtЊцĊЧЩѳƋŰĘɰʲȢҵψĻǜǎ˷}Ϧ',
            'target_id': 'ΠɎǈу£ǬΐҗĒŲŮβÚʍөɗUΗáĺωύ˲\x8bȦоά˾ΐȺ',
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
                    'event_id': 'öűH8Uĸ§ΥĦĶ\x90ĶŶĩ˯ӹΰʁŵ˜ԫBrӵϵпŀʞhЅ',
                    'target_id': 'ǧŧӧαĠһͼǢȟԖΑʶӷМRȱʵѺɖͱ&ɵʲ\x882-ťѡцʝ',
                },
                {
                    'event_id': 'ҐӑȿĊĂ˱ðƧɱȣϨƯȝ~ˈȯϲŸHӏö΄ίΩýŔȠiԁʃ',
                    'target_id': '4ʗǨтѧĄϩҴ\x9eѵǫͳːяȱʊÎʻɃʠIʤ˄эʎжŅΐϺɻ',
                },
                {
                    'event_id': 'ƲрįҦ©°ș˄ȱDϘ\u03a2ƆЋŲСɲҁɞȺ˛rѲӝȬɁþɤԆĬ',
                    'target_id': 'Ǫƣ¹ӗȰҵԜύĮѤɟΓúɟʸȚɜ,ԈѧϨϳщäʐ\x9eɫĆϭʵ',
                },
                {
                    'event_id': 'ˎӑɎõɒCѩɐ˃ҼǦԭ\x96ҢϛΥæđºþƮǵӳϘͲnԏϬӞá',
                    'target_id': 'чӫѦǚŗʕÓđĄӜœuʀҨǡʈТʛВ\x95џȞοʺ˧÷ȾŢԜ\x84',
                },
                {
                    'event_id': 'ƣςă%ї]õ\x91Қ˞©\x91ǽΊϗ(ÆǫљnΨѤƘΞɐŵγ\x8dҟƖ',
                    'target_id': 'ԜлӾӨīҍӆЖѬƟ&´áȯΒˆó\x9eŸĕɱȩͽˎ}ōƀӖӚҿ',
                },
                {
                    'event_id': 'Ӏɋ1ԝ\u0380ѿі¶Û\u0380ƵϹѶЇПҸҢӵNЦƌīŵԤǠɅSσĥH',
                    'target_id': 'lĄ\x80Ί\x86ĴԇŜȹ¾ĚҘʼɟΓђмėҝ3ѤʁśԚoӂ(ǏΠˡ',
                },
                {
                    'event_id': 'ʎҽʉ}ʘǡϩ\xad-șӝʁдκДţμaƽ˱ZчVnǝӲƺ-ǁ\x82',
                    'target_id': 'ԔɰˡƂǜүǍѱɀΰĉԗЭĶФӨҴzŤҀώ҈ːǬƏȑϖ\x9cşȞ',
                },
                {
                    'event_id': 'ѸȼӊTˈȻ\x98ԒƼτǐӭŠѝȂɋʴŉɥÛƤɢоϝЗ\u0382Ў҅Ĝ˕',
                    'target_id': 'ÅѣҺÜǼŦоȡԕмñÔȁʄǌˢϾыĪɚҼҋ+ѳǑϬƤΗΜǟ',
                },
                {
                    'event_id': 'ƛѲϒ˚Ѝәʜ\x86ΦνҲΘʜ˔ӫΞҷƁ\x91;\u038d˯πԎϽďʩțàΘ',
                    'target_id': 'ƥӷòʂʇǆΖǐʹϾЌɢ3ьώϣĩȥ˒/ҟ˹şǜҁˮԏԁ0ʹ',
                },
                {
                    'event_id': 'ѢнʨѹǶǙǜǗŨ˪w\x91τ˨ŢɑΩɹɋÕ~εøʅэɶɪƜ\x85ņ',
                    'target_id': 'ŎǩȒӞǻϻԌӬȡNłЈã˕äȗ\u0382~Ƚüү£÷ĳɕҵЦ˓һ<',
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
                    'event_id': 'ʐчͿɢȵɶŔӍǫBÊЪǊȩΝԈЍåɻʖȤƉ`БʭĉΏОфе',
                    'target_id': 'хԪɸˋ\x8c·ĹΠөiϪϻʹŶȅʖȝëϣэȶďʷ\u0383ζӳнÍ\x92Ƥ',
                },
                {
                    'event_id': '\x8b\u038bˆЊ¸˦ĞѵԎ\xa0Ϊ\x8dǚСýĆð,Ģȃȿыѵ6˹ćĂȵɢ2',
                    'target_id': 'Ô\x83ҥϟЩӨľǷϾƓθ·ÃʿŃ˪ĿǮɵƂƕȫΦǙͺŧīáq˶',
                },
                {
                    'event_id': 'єŬʹƏΕ³ǠѶɴӜоýɏҐȳǿӏ\x93ѹ-\x8e˕ƝХҮÉ˛ӐѫȚ',
                    'target_id': 'ИˢĢ\x93ѡΙӷí4ćºǹǰɲґǒϵƹǸ¥ϣ¿Xº˄éϔƠӵȾ',
                },
                {
                    'event_id': '(ɘΓʧΠӜƀ',
                    'target_id': 'ʇǱχҲѶǲǨƩ˧I͵ќʃűȥÑЛÇƠ¾ҷȈ\\-ЁÛÁ\u0382\u038dĜ',
                },
                {
                    'event_id': 'ŭзʓ\x8eƝÝ~ȃȧǎ\u038bЇóʆҫ\x89ЩӥɼҸɼ˭ϠşϹԢÄπˌx',
                    'target_id': 'ÅʭŖƵӴІҽƶoʯӣŌ;5ǤѭɖħǺˮ\x80ҭИaҭþԇТԗů',
                },
                {
                    'event_id': 'ԈōXǘóBтЈӠȆôѿѸŎҾ\x9dӓȎԔԛˊͼΦŒÄÁ-ǣȖĭ',
                    'target_id': 'ř\x96ԇͼİ£ѱ\x8a˂ɊϹƅɿŸɝ/KҧΘ˜$ÞwΪѯǚЀ¿\x82ú',
                },
                {
                    'event_id': 'Ӹҹ˷\x92ЖĄϒѢɢ½¤\u0378Ь\u0380˄ʦŐМҬҍѬLϋ.\x9eȯ˃þµѾ',
                    'target_id': 'ҜӻȪ.ĠӽѺ3ĉɔʁg˱Ĉʘ\x99@ͱӆɠѣҊ!\x9d҈˓ƓҚӌȸ',
                },
                {
                    'event_id': '˼ͰOϩǄЙԧ]\x87ʣOǐŗFďÓȃǁαЀ˫śԁƺȅ҂ɥГTU',
                    'target_id': "'!ѪŤ\\Ӈ˸ԥҚOʀŅԡ÷ԃ»ΗŜ¦ɂǄԊХϯȇΤǢLêς",
                },
                {
                    'event_id': 'ϻÓԍԏÍМ\x9dȠҰ\u0379Ȯŀ\x81ő8ƉfpKјȃÇғʎΕäØӗǭд',
                    'target_id': 'řοĎʉ\u0379ǃÄæʠӚ$ҙϢőòѐ˔ǚǤγŔ<ÔǥΗɊʄϱζɦ',
                },
                {
                    'event_id': 'tҥz˹ωəǎκˢԞһ˾\x87ԇ´ԡŰƐѪԅнэ?Љˋˢǽɜ³Ė',
                    'target_id': 'ͷԋæʗǥ\x81Ĳ¥ТәɝǢʘ9\x9cδҩο\x8dҝԀƺϴǉDˠ˶ͷQˆ',
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
